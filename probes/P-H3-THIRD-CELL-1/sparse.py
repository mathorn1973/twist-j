# SPDX-License-Identifier: Apache-2.0
"""Exact sparse preparations and first events in the initially empty column."""

import argparse
from collections import Counter
import json

import kernel as k
import launches
import measure as m


HORIZON = 128
BANK = 6
SEED = 31
COLUMN = tuple(range(28, 32))
EMPTY = (k.ZERO,) * 4
DELTA_M = k.from_j(-9, 2, -2, -3)
DELTA_U = k.from_j(1, 1, -3, 9)
VARIANTS = {
    "0": ((0, 0, 0, 0), (-7, 1, 1, 0), (-2, 2, -4, 6)),
    "1": ((1, 0, 0, 0), (-7, -1, 1, -4), (-2, 2, 0, 6)),
    "J": ((1, 0, 1, 0), (-7, -1, 1, -4), (0, -2, -4, 6)),
    "O": ((0, 1, 0, 1), (-7, -1, 1, -4), (0, -2, -4, 6)),
    "2": ((2, 0, 0, 0), (-7, -1, 1, -4), (-2, -1, -3, 6)),
    "2J": ((2, 0, 2, 0), (-7, 2, 0, -4), (0, -2, 0, 6)),
    "2O": ((0, 2, 0, 2), (-7, 2, 0, -4), (0, -2, 0, 6)),
}
EVENTS = ("spread", "active_B", "active_elsewhere_B", "matter_contrast",
          "radiation_contrast", "column_reflection_break", "reflection_break")


def preparation(field, variant):
    m.require(field[BANK] == field[SEED] == EMPTY, ("bare preparation sites", variant))
    a, p, q = (k.from_j(*coeffs) for coeffs in VARIANTS[variant])
    bank = (p, k.subtract(DELTA_M, p), q, k.subtract(DELTA_U, q))
    modified = m.replace(field, BANK, bank)
    modified = m.replace(modified, SEED, (a, k.scale(-1, a), k.ZERO, k.ZERO))
    m.require(k.reported_account(modified) == m.LEDGER, ("sparse account", variant))
    return modified


def reflected(site):
    x, y = divmod(site, k.HEIGHT)
    return x * k.HEIGHT + (1 - y) % k.HEIGHT


def first_nonzero_matter(field, sites):
    return next((site for site in sites if field[site][:2] != EMPTY[:2]), None)


def first_disparity(field, sites, subset=slice(None)):
    return next((site for site in sites
                 if field[site][subset] != field[reflected(site)][subset]), None)


def first_contrast(field, subset):
    return next((site for site in COLUMN[1:]
                 if field[site][subset] != field[COLUMN[0]][subset]), None)


def scan(start, ledger, horizon, rank, variant):
    first = dict.fromkeys(EVENTS)
    field = start
    for tick in range(1, horizon + 1):
        pre = field
        cut = m.native(pre, tick, ledger, (rank, variant))
        contact, field, tags = cut
        for stage, layer in (("C", contact), ("B", field)):
            sites = {
                "spread": first_nonzero_matter(layer, COLUMN[:-1]),
                "matter_contrast": first_contrast(layer, slice(2)),
                "radiation_contrast": first_contrast(layer, slice(2, 4)),
                "column_reflection_break": first_disparity(layer, COLUMN),
                "reflection_break": first_disparity(layer, range(len(field))),
            }
            if stage == "B":
                sites["active_B"] = next((site for site in COLUMN if tags[site]), None)
                sites["active_elsewhere_B"] = next(
                    (site for site in COLUMN[:-1] if tags[site]), None)
            for event, site in sites.items():
                if first[event] is None and site is not None:
                    first[event] = {
                        "rank": rank, "tick": tick, "stage": stage, "site": site,
                        **m.triple(pre, cut, site),
                    }
        if variant in ("bare", "0"):
            m.require(not any(tags[site] for site in COLUMN)
                      and first_nonzero_matter(contact, COLUMN) is None
                      and first_nonzero_matter(field, COLUMN) is None,
                      (rank, variant, tick, "zero matter sector"))
        if variant in ("1", "J", "O"):
            for layer in (contact, field):
                a, b = layer[SEED][:2]
                m.require(first_nonzero_matter(layer, COLUMN[:-1]) is None
                          and a == k.scale(-1, b) and not k.even(a),
                          (rank, variant, tick, "isolated antipodal odd seed"))
        if variant in ("2", "2J", "2O") and tick == 1:
            m.require(first["spread"] is not None and first["spread"]["site"] == 28,
                      (rank, variant, tick, "even seed immediate contact"))
    for tick in range(horizon, 0, -1):
        field = k.inverse_step(field, tick % 2)
    m.require(field == start, (rank, variant, "terminal inverse"))
    return first


def summarize(results):
    summary = {}
    for event in EVENTS:
        witnesses = [row[event] for row in results if row[event] is not None]
        order = lambda row: (row["tick"], row["stage"] == "B", row["rank"], row["site"])
        summary[event] = {
            "ranks": len(witnesses),
            "first": min(witnesses, key=order, default=None),
            "by_tick_and_stage": [[tick, stage, count] for (tick, stage), count in
                                  sorted(Counter((row["tick"], row["stage"])
                                                 for row in witnesses).items())],
        }
    return summary


def run(bare_fields, horizon=HORIZON):
    """Audit the unmodified preparations and all seven sparse families."""
    bare_fields = tuple(tuple(map(tuple, field)) for field in bare_fields)
    m.require(len(bare_fields) == len(set(bare_fields)) == 85, "85 distinct bare launches")
    groups = {name: [] for name in ("bare", *VARIANTS)}
    reflected_ranks = []
    for rank, bare in enumerate(bare_fields):
        m.require(k.reported_account(bare) == k.BARE_ACCOUNTS, (rank, "bare account"))
        m.require(all(bare[site] == EMPTY for site in COLUMN), (rank, "bare empty column"))
        if first_disparity(bare, range(len(bare))) is None:
            reflected_ranks.append(rank)
        groups["bare"].append(scan(bare, k.account(bare), horizon, rank, "bare"))
        for name in VARIANTS:
            start = preparation(bare, name)
            groups[name].append(scan(start, k.account(start), horizon, rank, name))
    return {
        "horizon": horizon,
        "launches_per_class": len(bare_fields),
        "bare_launch_empty_column": len(bare_fields),
        "bare_launch_reflection": {"count": len(reflected_ranks), "ranks": reflected_ranks},
        "classes": {name: summarize(rows) for name, rows in groups.items()},
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--horizon", type=int, default=HORIZON)
    options = parser.parse_args()
    print(json.dumps(run(launches.bare_inputs(), options.horizon), sort_keys=True))


if __name__ == "__main__":
    main()
