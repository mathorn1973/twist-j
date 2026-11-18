# SPDX-License-Identifier: Apache-2.0
"""Five-coefficient third-site replay of the inherited four-wire launch."""

import argparse
import json
from pathlib import Path

import kernel as k
import measure as m


ANCHOR = 181
SOURCE = 28
O = k.from_j(0, 1, 0, 1)
O_WORD = O, k.scale(-1, O)
PHASE = m.W_WORD
SIGN = O_WORD[::-1]
RANKS = (0, 22, 43)
EVENTS = ("C_matter", "C_radiation", "B_branch", "B_live_vs_idle",
          "B_matched_matter", "B_matched_radiation")
REGIONS = {"all": tuple(i for i in range(32) if i not in (28, 31)),
           "site29": (29,), "site30": (30,),
           "outside": tuple(range(28))}


def encoded(words):
    return [k.reported(word) for word in words]


def record(pre, cut, site):
    return m.triple(pre, cut, site)


def increment(contact, result):
    return tuple(k.subtract(a, b) for a, b in zip(result[:2], contact[:2]))


def matter_mate(site, bit):
    height = k.HEIGHT
    x, y = divmod(site, height)
    first = y % 2 == bit
    return x * height + (y + (1 if first else -1)) % height, int(not first)


def radiation_mate(site, bit):
    x, y = divmod(site, k.HEIGHT)
    return ((x + (1 if x % 2 == bit else -1)) % 8) * k.HEIGHT + y


def project_donor(recipient, sender, orientation):
    def project(a, b):
        pair = (a, b) if orientation == 0 else (b, a)
        return k.contact(*pair)[orientation]
    return tuple(project(a, b) for a, b in zip(recipient[:2], sender[:2]))


def hybrids(actual_matter, alternative_matter, actual_rad, alternative_rad):
    entries = {}
    for i, matter in enumerate((actual_matter, alternative_matter)):
        for j, radiation in enumerate((actual_rad, alternative_rad)):
            contact = (*matter, *radiation)
            output, tag = k.scatter(contact)
            entries[f"{i}{j}"] = (contact, output, tag, increment(contact, output))
    return entries


def hybrid_summary(matrix):
    return {
        name: {
            "post_C": encoded(contact),
            "post_B": encoded(output),
            "tag": tag,
            "increment": encoded(change),
        }
        for name, (contact, output, tag, change) in matrix.items()
    }


def sector(matrix):
    aa, ar, am, mm = (matrix[name][3] for name in ("00", "01", "10", "11"))
    matter = aa != am
    radiation = aa != ar
    if matter and radiation:
        return "both"
    if matter:
        return "matter"
    if radiation:
        return "radiation"
    if aa != mm:
        return "joint_only"
    return "unchanged"


def escrow(pre, alternate_sender, donor, site, tick, ledger, target):
    payer = next((i for i, cell in enumerate(pre) if i not in (donor, site)
                  and cell[:2] == alternate_sender[:2]), None)
    if payer is None:
        return None
    modified = m.replace(pre, donor, (*pre[payer][:2], *pre[donor][2:]))
    modified = m.replace(modified, payer, (*pre[donor][:2], *pre[payer][2:]))
    m.require(k.account(modified) == ledger, (tick, donor, site, "escrow account"))
    contact, complete, tags = m.native(modified, tick, ledger, ("local donor exchange",))
    m.require((contact[site], complete[site], tags[site]) == target[:3],
              (tick, donor, site, "escrow projection"))
    return payer


def inspect(pre, cut, other_pre, other_cut, site, tick, ledger, routes):
    live_c, live_b, live_tags = cut
    off_c, off_b, off_tags = other_cut
    mate, orientation = matter_mate(site, tick % 2)
    horizontal_mate = radiation_mate(site, tick % 2)
    m.require(project_donor(pre[site], pre[mate], orientation) == live_c[site][:2],
              (tick, site, "orientation"))
    from_other = project_donor(pre[site], other_pre[mate], orientation)
    sender_matrix = hybrids(live_c[site][:2], from_other, live_c[site][2:], off_c[site][2:])
    site_matrix = hybrids(live_c[site][:2], off_c[site][:2],
                          live_c[site][2:], off_c[site][2:])
    swapped = sender_matrix["10"]
    assert (live_c[site], live_b[site], live_tags[site]) == sender_matrix["00"][:3]
    assert (off_c[site], off_b[site], off_tags[site]) == site_matrix["11"][:3]
    strict_sender = (
        live_tags[site] != 0 and live_c[site][:2] != pre[site][:2]
        and from_other != live_c[site][:2] and swapped[2] == 0
    )
    payer = None
    if strict_sender:
        payer = escrow(pre, other_pre[mate], mate, site, tick, ledger, swapped)
    return {
        "tick": tick,
        "site": site,
        "donor": mate,
        "recipient_endpoint": orientation,
        "live": record(pre, cut, site),
        "control": record(other_pre, other_cut, site),
        "live_donor": record(pre, cut, mate),
        "control_donor": record(other_pre, other_cut, mate),
        "live_horizontal_donor_pre_C": encoded(pre[horizontal_mate]),
        "control_horizontal_donor_pre_C": encoded(other_pre[horizontal_mate]),
        "same_pre_C": pre[site] == other_pre[site],
        "same_pre_C_matter": pre[site][:2] == other_pre[site][:2],
        "same_incoming_radiation": live_c[site][2:] == off_c[site][2:],
        "distinct_native_increments": sender_matrix["00"][3] != site_matrix["11"][3],
        "fixed_recipient_donor_sector": sector(sender_matrix),
        "full_recipient_sector": sector(site_matrix),
        "fixed_recipient_hybrids": hybrid_summary(sender_matrix),
        "full_recipient_hybrids": hybrid_summary(site_matrix),
        "strict_sender": strict_sender,
        "escrow_payer": payer,
        "fixed_radiation_matter_roots": routes.get(site, [None, None]),
    }


def route_step(routes, pre, cut, other_pre, other_cut, tick):
    """Condense surviving all-matter paths to the first intersite C transfer."""
    live_c, live_b, _ = cut
    off_c, off_b, _ = other_cut
    contact_routes = {}
    for site in range(len(pre)):
        mate, orientation = matter_mate(site, tick % 2)
        ordered = (site, mate) if orientation == 0 else (mate, site)
        roots = [None, None]
        for lane in range(2):
            if live_c[site][lane] == off_c[site][lane]:
                continue
            base = [pre[parent][lane] for parent in ordered]
            for endpoint, parent in enumerate(ordered):
                root = routes.get(parent, (None, None))[lane]
                if root is None:
                    continue
                branch = base[:]
                branch[endpoint] = other_pre[parent][lane]
                projected = k.contact(*branch)[orientation]
                if projected == live_c[site][lane]:
                    continue
                if parent != site and root[0] == ANCHOR:
                    root = (tick, "C", parent, site, lane)
                roots[lane] = root
                break
        if any(root is not None for root in roots):
            contact_routes[site] = roots

    propagated = {}
    for site, roots in contact_routes.items():
        branch = list(live_c[site])
        for lane, root in enumerate(roots):
            if root is not None:
                branch[lane] = off_c[site][lane]
        changed, _ = k.scatter(tuple(branch))
        output_roots = [None, None]
        for lane in range(2):
            if changed[lane] != live_b[site][lane] != off_b[site][lane]:
                output_roots[lane] = next(root for root in roots if root is not None)
        if any(root is not None for root in output_roots):
            propagated[site] = output_roots
    return propagated


def audit_terminal(field, start, first, last):
    for tick in range(last, first - 1, -1):
        field = k.inverse_step(field, tick % 2)
    m.require(field == start, (first, last, "terminal inverse"))


def comparisons(pre, cut, other_pre, other_cut, site):
    live_c, live_b, tags = cut
    other_c, _, other_tags = other_cut
    live_tag, other_tag = tags[site], other_tags[site]
    matter = live_c[site][:2] != other_c[site][:2]
    radiation = live_c[site][2:] != other_c[site][2:]
    branch = bool(live_tag and live_tag != other_tag
                  and live_c[site][:2] != live_b[site][:2])
    idle = branch and other_tag == 0
    matched = idle and pre[site] == other_pre[site]
    return dict(zip(EVENTS, (matter, radiation, branch, idle,
                            matched and matter and not radiation,
                            matched and radiation and not matter)))


def run(field, rank, horizon=2048):
    """Report first per-site endpoints for each same-account comparison."""
    if rank not in RANKS or horizon <= ANCHOR:
        raise ValueError("expected a prespecified anchor rank and a post-anchor horizon")
    field = tuple(map(tuple, field))
    launch = field
    ledger = k.account(field)
    m.require(k.reported_account(field) == m.LEDGER, (rank, "launch account"))
    for tick in range(1, ANCHOR + 1):
        pre = field
        cut = m.native(pre, tick, ledger, (rank, "live"))
        field = cut[1]
    m.require(pre[m.MEMORY][:2] == m.W_WORD and cut[0][m.MEMORY][:2] != m.W_WORD,
              (rank, "181 word consumption"))
    m.require(cut[2][SOURCE] == 2 and field[SOURCE][:2] == O_WORD,
              (rank, "181 B2 anchor"))
    phase_unit = k.scale(-1, k.power(4))
    m.require(tuple(k.multiply(phase_unit, word) for word in O_WORD) == PHASE,
              (rank, "phase rotation"))
    restored, tag = k.scatter(field[SOURCE])
    m.require(restored == cut[0][SOURCE] and tag == 1, (rank, "anchor inverse B1"))
    starts = {
        "phase": m.replace(field, SOURCE, (*PHASE, *field[SOURCE][2:])),
        "sign": m.replace(field, SOURCE, (*SIGN, *field[SOURCE][2:])),
        "omission": m.replace(field, SOURCE, restored),
    }
    for name, start in starts.items():
        m.require(k.account(start) == ledger, (rank, name, "fork account"))
        m.require({i for i, cell in enumerate(start) if cell != field[i]} == {SOURCE},
                  (rank, name, "fork support"))
        if name != "omission":
            m.require(start[SOURCE][2:] == field[SOURCE][2:],
                      (rank, name, "fork radiation"))

    result = {
        "rank": rank,
        "horizon": horizon,
        "anchor": record(pre, cut, SOURCE),
        "forks": {name: encoded(start[SOURCE]) for name, start in starts.items()},
        "early_native_work": [],
        "early_native_column": [],
        "direct_182_site29": {},
        "comparisons": {name: {} for name in starts},
        "native_rows": {name: {region: {event: {"count": 0, "first": None}
                                        for event in EVENTS} for region in REGIONS}
                        for name in starts},
    }
    active = dict(starts)
    lineage = {
        name: {SOURCE: [
            (ANCHOR, "B", SOURCE, SOURCE, lane)
            if start[SOURCE][lane] != field[SOURCE][lane] else None
            for lane in range(2)]}
        for name, start in starts.items()
    }

    for tick in range(ANCHOR + 1, horizon + 1):
        pre = field
        cut = m.native(pre, tick, ledger, (rank, "live"))
        live_c, field, live_tags = cut
        if tick <= 210:
            result["early_native_column"].append({
                "tick": tick,
                "cuts": {site: record(pre, cut, site) for site in range(28, 32)},
            })
            for site, tag in enumerate(live_tags):
                if tag:
                    result["early_native_work"].append(
                        {"tick": tick, "site": site, **record(pre, cut, site)})
        for name, other_pre in active.items():
            off_cut = m.native(other_pre, tick, ledger, (rank, name))
            off_c, active[name], off_tags = off_cut
            roots = route_step(lineage[name], pre, cut, other_pre, off_cut, tick)
            lineage[name] = roots
            reports = result["comparisons"][name]
            for site, tag in enumerate(live_tags):
                other_tag = off_tags[site]
                witness = None
                if tick == 182 and site == 29:
                    witness = inspect(pre, cut, other_pre, off_cut, site, tick, ledger, roots)
                    result["direct_182_site29"][name] = witness
                for event, occurs in comparisons(pre, cut, other_pre, off_cut, site).items():
                    if not occurs:
                        continue
                    for region, sites in REGIONS.items():
                        if site not in sites:
                            continue
                        row = result["native_rows"][name][region][event]
                        row["count"] += 1
                        if row["first"] is None:
                            if witness is None:
                                witness = inspect(pre, cut, other_pre, off_cut, site,
                                                  tick, ledger, roots)
                            row["first"] = witness
                if tag == other_tag == 0:
                    continue
                live_change = increment(live_c[site], field[site])
                off_change = increment(off_c[site], active[name][site])
                entries = reports.setdefault(site, {})
                categories = []
                if live_change != off_change:
                    categories.append("first_increments_differ")
                    if tag:
                        categories.append("first_live_work_changes")
                if tag and not other_tag:
                    categories.append("first_work_on_off")
                if tag and other_tag and tag != other_tag:
                    categories.append("first_active_tag_flip")
                    if pre[site] == other_pre[site] and live_c[site][2:] == off_c[site][2:]:
                        categories.append("first_matched_active_tag_flip")
                mate, orientation = matter_mate(site, tick % 2)
                alternate = project_donor(pre[site], other_pre[mate], orientation)
                if tag and alternate != live_c[site][:2] and live_c[site][:2] != pre[site][:2]:
                    branch, branch_tag = k.scatter((*alternate, *live_c[site][2:]))
                    if live_change != increment(alternate, branch):
                        categories.append("first_donor_work")
                        if branch_tag == 0:
                            categories.append("first_strict_donor_work")
                        elif branch_tag != tag:
                            categories.append("first_donor_active_tag_flip")
                unseen = [category for category in categories if category not in entries]
                if unseen:
                    if witness is None:
                        witness = inspect(pre, cut, other_pre, off_cut, site,
                                          tick, ledger, roots)
                    for category in unseen:
                        entries[category] = witness

    audit_terminal(field, launch, 1, horizon)
    for name, final in active.items():
        audit_terminal(final, starts[name], ANCHOR + 1, horizon)
    return result


def local_coefficients(witness):
    cells = []
    for arm in ("live", "control"):
        cells.extend(witness[arm][cut] for cut in ("pre_C", "post_C", "post_B"))
        cells.append(witness[f"{arm}_donor"]["pre_C"])
        cells.append(witness[f"{arm}_horizontal_donor_pre_C"])
    return [coefficient for cell in cells for rail in cell for coefficient in rail]


def compare_native(results, source):
    expected = {}
    for result in results:
        rank = str(result["rank"])
        for name, regions in result["native_rows"].items():
            arm = "omit" if name == "omission" else name
            for region, events in regions.items():
                for event, record in events.items():
                    key = (rank, arm, region, event)
                    count, first = record["count"], record["first"]
                    if first is None:
                        expected[("ROW", *key)] = [0] * 5
                        continue
                    cut = [first["tick"], first["site"]]
                    expected[("ROW", *key)] = [*cut, first["live"]["tag"],
                                                first["control"]["tag"], count]
                    expected[("LOCAL", *key)] = [*cut, *local_coefficients(first)]
            direct = result["direct_182_site29"][name]
            live, other = direct["live"], direct["control"]
            moves = [record["pre_C"][sector] != record["post_C"][sector]
                     for sector in (slice(2), slice(2, 4)) for record in (live, other)]
            expected[("DIRECT", rank, arm)] = [
                *moves, live["tag"], other["tag"], *local_coefficients(direct)]
    horizons = {str(result["rank"]): result["horizon"] for result in results}
    lines = [line.split("\t") for line in source.splitlines()]
    native_horizons = {columns[1]: int(columns[2]) for columns in lines
                       if columns[0] == "BASE" and columns[1] in horizons}
    m.require(native_horizons.keys() == horizons.keys()
              and all(native_horizons[rank] >= limit for rank, limit in horizons.items()),
              ("native comparison horizon", native_horizons, horizons))
    seen = set()
    for columns in lines:
        if len(columns) < 2 or columns[1] not in horizons:
            continue
        spec, rank = columns[:2]
        length = {"ROW": 5, "LOCAL": 5, "DIRECT": 3}.get(spec)
        if length is None:
            continue
        key = tuple(columns[:length])
        values = list(map(int, columns[length:]))
        target = expected.get(key)
        if spec == "LOCAL" and values[0] > horizons[rank]:
            m.require(target is None, ("unexpected Python local", key, target))
            continue
        if spec == "ROW" and native_horizons[rank] > horizons[rank]:
            if values[0] > horizons[rank]:
                values = [0] * 5
            equal = (target is not None and values[:4] == target[:4]
                     and values[4] >= target[4])
        else:
            equal = values == target
        m.require(key not in seen and equal, ("native comparison", key, values, target))
        seen.add(key)
    m.require(seen == expected.keys(), ("native row coverage", expected.keys() - seen))
    return len(seen)


def summarize(result):
    """Keep full early cuts and only the earliest endpoint of each per-site type."""
    summary = {key: result[key] for key in ("rank", "horizon", "anchor", "forks",
               "direct_182_site29", "early_native_work", "early_native_column")}
    summary["native_rows"] = {
        arm: {region: {event: {
            "count": row["count"],
            "tick": row["first"]["tick"] if row["first"] else None,
            "site": row["first"]["site"] if row["first"] else None,
        } for event, row in events.items()} for region, events in regions.items()}
        for arm, regions in result["native_rows"].items()
    }
    summary["first_site_details"] = {
        arm: {site: rows for site, rows in collection.items() if site in (29, 30) and rows}
        for arm, collection in result["comparisons"].items()
    }
    summary["first_per_site"] = {
        arm: {site: {name: witness["tick"] for name, witness in rows.items()} for site, rows
              in collection.items() if rows}
        for arm, collection in result["comparisons"].items()
    }
    return summary


def main():
    import launches
    parser = argparse.ArgumentParser()
    parser.add_argument("--horizon", type=int, default=2048)
    parser.add_argument("--rank", type=int, choices=RANKS, action="append")
    parser.add_argument("--native-tsv", type=Path)
    parser.add_argument("--summary", action="store_true")
    options = parser.parse_args()
    fields = launches.four_wire(launches.bare_inputs())
    results = [run(fields[rank], rank, options.horizon)
               for rank in options.rank or RANKS]
    native_rows = None
    if options.native_tsv is not None:
        native_rows = compare_native(results, options.native_tsv.read_text(encoding="utf-8-sig"))
    if options.summary:
        results = list(map(summarize, results))
    print(json.dumps({"results": results, "native_rows_checked": native_rows}, sort_keys=True))


if __name__ == "__main__":
    main()
