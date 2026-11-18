# SPDX-License-Identifier: Apache-2.0
"""Run the frozen cascade, preparation, and two-word experiments."""

from collections import defaultdict
from hashlib import sha256
from pathlib import Path
import subprocess

import dual
import measure as m
import natural_verify as nv
import observe


OBSERVER_HORIZON = 512
CONTROLS = ("phase", "sign", "omit")
SEED_ROW = (
    "rank", "donor", "rho_power", "negative", "applicable",
    "source125", "restore157", "held158", "first159", "earliest_later", "exact181",
    "live_C_move", "phase_C_move", "sign_C_move", "live_B_tag", "phase_B_tag",
    "sign_B_tag", "phase_C_distinct", "phase_B_distinct", "sign_C_distinct", "sign_B_distinct"
)
SEED_TOTALS = (
    "recipes", "arms", "source125", "source_and_restored_and_held", "first159",
    "earliest_later181", "retained_exact_chain", "phase_active_idle", "sign_active_idle",
    "sign_two_active", "recipes_phase_active_idle", "recipes_sign_active_idle",
    "recipes_sign_two_active"
)


def exact_digest(text):
    return sha256(text.encode("ascii")).hexdigest()


def native(executable, query, outdir, name):
    run = subprocess.run([str(Path(executable).resolve()), str(query)], check=True,
                         capture_output=True, text=True, encoding="ascii", timeout=120)
    m.require(not run.stderr, (name, "unexpected stderr", run.stderr))
    (outdir / f"{name}.tsv").write_bytes(run.stdout.encode("ascii"))
    return run.stdout


def j_cells(coefficients):
    m.require(len(coefficients) % 16 == 0, "incomplete coefficient record")
    return [[coefficients[j:j + 4] for j in range(i, i + 16, 4)]
            for i in range(0, len(coefficients), 16)]


def cascade_summary(text, launch_fields):
    rows, locals_, direct, baseline = {}, {}, {}, {}
    for line in text.splitlines():
        label, raw, *columns = line.split()
        rank = int(raw)
        if label == "BASE":
            baseline[rank] = list(map(int, columns))
        elif label == "DIRECT":
            control, *numbers = columns
            flags = list(map(int, numbers[:6]))
            direct.setdefault(rank, {})[control] = {"values": flags}
            if rank == 43:
                direct[rank][control]["cells"] = j_cells(list(map(int, numbers[6:])))
        elif label in {"ROW", "LOCAL"}:
            control, region, event, *numbers = columns
            key = rank, control, region, event
            if label == "ROW":
                rows[key] = list(map(int, numbers))
            else:
                locals_[key] = list(map(int, numbers))
        else:
            raise ValueError(f"unknown cascade row {label}")
    m.require(set(baseline) == set(launch_fields), "cascade baseline coverage")
    m.require({rank for rank, row in baseline.items() if row[1:] == [1, 181]} ==
              set(observe.RANKS), "cascade 159/181 coverage")
    reports = [observe.run(launch_fields[r], r, OBSERVER_HORIZON) for r in observe.RANKS]
    checked = observe.compare_native(reports, text)
    native_witnesses = {}
    for name in CONTROLS:
        for region in ("all", "site29", "site30"):
            for event in dual.PRIORITY:
                key = (43, name, region, event)
                if not rows[key][-1]:
                    continue
                tick, site, *coefficients = locals_[key]
                native_witnesses[f"{name}/{region}"] = {
                    "tick": tick, "site": site, "event": event,
                    "cells": j_cells(coefficients)
                }
                break
    independent = {}
    for report in reports:
        rank = report["rank"]
        chosen = {"anchor": report["anchor"], "forks": report["forks"],
                  "direct_182": {}, "near_first": {}, "native_first_writes_to210": {}}
        for row in report["early_native_work"]:
            if row["site"] in (29, 30):
                chosen["native_first_writes_to210"].setdefault(row["site"], row)
        for arm, local in report["direct_182_site29"].items():
            chosen["direct_182"][arm] = {
                key: local[key] for key in ("same_pre_C", "same_incoming_radiation",
                    "fixed_recipient_donor_sector", "full_recipient_sector",
                    "strict_sender", "escrow_payer", "fixed_radiation_matter_roots")
            }
        if rank == 43:
            for arm, comparison in report["comparisons"].items():
                for site in (29, 30):
                    events = comparison.get(site, {})
                    first = {}
                    for name in ("first_donor_work", "first_strict_donor_work",
                                 "first_donor_active_tag_flip", "first_matched_active_tag_flip"):
                        if name in events:
                            item = events[name]
                            first[name] = {key: item[key] for key in (
                                "tick", "donor", "same_pre_C", "same_incoming_radiation",
                                "strict_sender", "escrow_payer", "fixed_recipient_donor_sector",
                                "fixed_radiation_matter_roots"
                            )}
                    if first:
                        chosen["near_first"][f"{arm}/{site}"] = first
        independent[rank] = chosen
    matrix = {}
    for rank in observe.RANKS:
        matrix[rank] = {
            f"{arm}/{region}": [rows[rank, arm, region, event] for event in observe.EVENTS]
            for arm in CONTROLS for region in observe.REGIONS
        }
    return {
        "native_sha256": exact_digest(text),
        "native_ranks": len(baseline),
        "native_live_ticks": sum(row[0] for row in baseline.values()),
        "event_order": observe.EVENTS, "event_row_order": ["tick", "site", "live_tag",
                                                          "alt_tag", "site_tick_count"],
        "matrix": matrix, "rank43_gate_witnesses": native_witnesses,
        "witness_cell_order": ["live_pre_C", "live_C", "live_B", "live_vertical_donor_pre_C",
                               "live_horizontal_donor_pre_C", "alt_pre_C", "alt_C", "alt_B",
                               "alt_vertical_donor_pre_C", "alt_horizontal_donor_pre_C"],
        "direct_182_site29": direct,
        "direct_value_order": ["live_C_matter_move", "alt_C_matter_move",
                               "live_C_radiation_move", "alt_C_radiation_move",
                               "live_tag", "alt_tag"],
        "independent_horizon": OBSERVER_HORIZON, "independent_rows": checked,
        "independent": independent
    }


def natural_summary(text, launch_fields):
    witness_pairs, first = nv.witness_rows(text.splitlines())
    by_rank = defaultdict(set)
    for key, pair in witness_pairs.items():
        nv.check_pair(key, pair)
        for _, arm in pair:
            by_rank[arm.rank].add(arm)
    if first:
        by_rank[43]
    for rank in sorted(by_rank):
        nv.replay(launch_fields[rank], rank, by_rank[rank], first if rank == 43 else {})
    ranks, matches, readiness, contacts, writes, selected = {}, {}, {}, {}, {}, {}
    for line in text.splitlines():
        tag, *items = line.split()
        if tag == "RANK":
            rank, ticks, count, inverse = map(int, items)
            m.require(inverse == 1, "natural terminal inverse")
            ranks[rank] = ticks, count
        elif tag == "WRITES":
            rank, site, b1, b2, tick, gate, *coefficients = map(int, items)
            if rank == 43:
                writes[site] = {"tag_counts": [b1, b2], "first_tick": tick, "first_tag": gate,
                                "first_C_B": j_cells(coefficients)}
        elif tag in {"CONTACTS", "MATCH", "GROUPS"}:
            if tag == "CONTACTS":
                rank, writer, reader, carrier, *counts = items
                dest = contacts.setdefault(f"{writer}/{reader}/{carrier}", [0, 0, 0])
                for i, count in enumerate(counts):
                    dest[i] += int(count)
            elif tag == "MATCH":
                writer, reader, carrier, event, *counts = items
                matches[f"{writer}/{reader}/{carrier}/{event}"] = list(map(int, counts))
            else:
                writer, reader, carrier, *counts = items
                readiness[f"{writer}/{reader}/{carrier}"] = list(map(int, counts))
        elif tag == "ARM":
            event, side, carrier, *numbers = items
            writer, reader, rank, w_tick, w_tag, r_tick, bit, moved, r_tag, *coefficients = map(int, numbers)
            key = f"{writer}/{reader}/{carrier}/{event}"
            cuts = j_cells(coefficients)
            selected.setdefault(key, []).append({
                "side": int(side), "rank": rank, "write": [w_tick, w_tag],
                "read": [r_tick, bit, moved, r_tag],
                "writer_C_B": cuts[:2], "donor_pre_C": cuts[2],
                "receiver_pre_C_B": cuts[5:]
            })
        elif tag != "#":
            raise ValueError(f"unknown natural row {tag}")
    m.require(set(ranks) == set(launch_fields), "natural rank coverage")
    return {
        "native_sha256": exact_digest(text), "native_ranks": len(ranks),
        "native_ticks": sum(row[0] for row in ranks.values()),
        "natural_writer28_B_count": sum(row[1] for row in ranks.values()),
        "raw43_writes": writes, "contacts": contacts, "readiness_groups": readiness,
        "match_count_order": ["pairs", "both_rank43", "both_moved"],
        "matches": matches, "paired_witnesses": selected,
        "independent_witness_pairs": len(witness_pairs), "independent_ranks": sorted(by_rank)
    }


def seed_summary(text):
    totals = {}
    retained, candidates = [], []
    for line in text.splitlines():
        tag, *items = line.split()
        values = list(map(int, items))
        if tag == "SEED_SUMMARY":
            totals = dict(zip(SEED_TOTALS, values, strict=True))
        elif tag == "SEED":
            row = dict(zip(SEED_ROW, values, strict=True))
            if (all(row[k] for k in ("source125", "restore157", "held158", "first159", "exact181"))
                    and row["earliest_later"] == 181):
                retained.append(values)
                if row["phase_C_distinct"] or row["sign_C_distinct"]:
                    candidates.append(values)
        else:
            raise ValueError(f"unknown seed row {tag}")
    m.require(totals and len(retained) == totals["retained_exact_chain"], "seed totals")
    return {
        "native_sha256": exact_digest(text), "totals": totals,
        "row_order": SEED_ROW, "chain_count": len(retained),
        "chain_rows_first12": retained[:12],
        "with_C_contrast_count": len(candidates), "with_C_contrast_first12": candidates[:12]
    }


def run(query_path, executables, outdir):
    query = Path(query_path).resolve()
    outdir = Path(outdir).resolve()
    outdir.mkdir(parents=True, exist_ok=True)
    launch_fields = dual.baseline_rows(query)
    cascade = native(executables["cascade"], query, outdir, "cascade")
    cascade_data = cascade_summary(cascade, launch_fields)
    encoded = dual.run(query, cascade, executables["dual"])
    natural = native(executables["natural"], query, outdir, "natural")
    natural_data = natural_summary(natural, launch_fields)
    seed = native(executables["seed"], query, outdir, "seed")
    return {"cascade": cascade_data, "preparation": encoded, "natural": natural_data,
            "seed": seed_summary(seed)}
