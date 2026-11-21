# SPDX-License-Identifier: Apache-2.0
"""Confirm launch-only encoding at the receiving event located by the cascade."""

import argparse
import hashlib
import json
from pathlib import Path
import struct
import subprocess

import kernel as k
import measure as m

WRITER, CUT = 28, 181
CLOCK = (0, 1, 4, 5, 8, 9)
EI = struct.Struct(">512q")
PRIORITY = ("B_matched_matter", "B_matched_radiation", "B_live_vs_idle", "B_branch")


def cells(numbers):
    m.require(len(numbers) % 16 == 0, "incomplete cells")
    return tuple(tuple(k.from_j(*numbers[start + 4 * lane:start + 4 * (lane + 1)])
                       for lane in range(4))
                 for start in range(0, len(numbers), 16))


def flatten(field):
    return tuple(c for cell in field for word in cell for c in k.j_coefficients(word))


def baseline_rows(path):
    fields = {}
    for row in path.read_text(encoding="utf-8-sig").splitlines():
        mode, rank, depth, *words = map(int, row.split())
        m.require(mode == 2 and depth == 0 and rank not in fields and len(words) == 512,
                  "invalid unchanged launch row")
        fields[rank] = cells(words)
    m.require(sorted(fields) == list(range(85)), "baseline ranks")
    return fields


def target_row(text):
    found = {}
    witnesses = {}
    for line in text.splitlines():
        record = line.split()
        if record[:4] == ["ROW", "43", "phase", "all"]:
            found[record[4]] = tuple(map(int, record[5:]))
        if record[:4] == ["LOCAL", "43", "phase", "all"]:
            witnesses[record[4]] = cells(list(map(int, record[7:])))
    for name in PRIORITY:
        tick, site, actual, other, count = found[name]
        if count:
            pre, c, b, _, _, alt_pre, alt_c, alt_b, _, _ = witnesses[name]
            return (name, tick, site, actual, other), (pre, c, b, alt_pre, alt_c, alt_b)
    return (None, 0, 0, 0, 0), ()


def unpack_writer(numbers):
    tag, first_active, first_b2, earlier_active, earlier_b2, tag159, gated159 = numbers[:7]
    return {
        "tag181": tag, "first_active_before181": first_active, "first_B2_before181": first_b2,
        "active_before181": earlier_active, "B2_before181": earlier_b2,
        "tag159": tag159, "qualifying159": gated159, "local181": cells(numbers[7:])
    }


def to_jsonable(writer):
    return {**writer, "local181": tuple(tuple(k.j_coefficients(w) for w in c)
                                        for c in writer["local181"])}


def replay_python(launch, stop, sites):
    field = launch
    ledger = k.account(launch)
    saved = {}
    for tick in range(1, stop + 1):
        if tick in sites:
            c, b, tags = m.native(field, tick, ledger, "independent launch encoding")
            site = sites[tick]
            saved[tick] = (field[site], c[site], b[site], tags[site], b)
        else:
            _, b = k.native_step(field, tick % 2)
        field = b
    return saved


def independent(original, encoded, writers, target, witness):
    name, tick, site, tag, alt_tag = target
    stop = tick or CUT
    sites = {CUT: WRITER}
    if name:
        sites[tick] = site
    actual = replay_python(original, stop, sites)
    alternate = replay_python(encoded, stop, sites)
    for arm, observed in zip(writers, (actual, alternate)):
        event = observed[CUT]
        m.require(arm["local181"] == event[:3] and arm["tag181"] == event[3] == 2,
                  "independent 181 B2")
        m.require(event[1][:2] != event[2][:2], "independent 181 material change")
    a, b = actual[CUT][-1], alternate[CUT][-1]
    phase = k.from_j(0, 0, 0, -1)
    expected = m.replace(a, WRITER, (*(k.multiply(word, phase) for word in a[WRITER][:2]),
                                      *a[WRITER][2:]))
    m.require(expected == b and a[WRITER][:2] != b[WRITER][:2] and
              b[WRITER][:2] == m.W_WORD, "distinct emissions at the same worker")
    reverse = expected
    for step in range(CUT, 0, -1):
        reverse = k.inverse_step(reverse, step % 2)
    m.require(reverse == encoded, "independent inverse-designed launch")
    if name:
        m.require((*actual[tick][:3], *alternate[tick][:3]) == witness,
                  "launch-only pair does not reproduce stage-one local witness")
        m.require((actual[tick][3], alternate[tick][3]) == (tag, alt_tag),
                  "launch-only target tags")


def run(query_path, cascade_stdout, dual_executable):
    query_path = Path(query_path)
    original = baseline_rows(query_path)
    target, witness = target_row(cascade_stdout)
    name, tick, site, _, _ = target
    native = subprocess.run([str(Path(dual_executable).resolve()), str(query_path),
                             str(tick), str(site)],
                            check=True, text=True, capture_output=True, timeout=60)
    encoded, records, receiver, simple, simple_receiver = {}, {}, {}, {}, {}
    principal = None
    screen = None
    for line in native.stdout.splitlines():
        label, *numbers = line.split()
        rank, *numbers = map(int, numbers)
        if label == "LAUNCH":
            m.require(rank not in encoded and len(numbers) == 512, "encoded launch row")
            encoded[rank] = cells(numbers)
        elif label == "ENCODED":
            delta, first, second = numbers[:4], unpack_writer(numbers[4:59]), unpack_writer(numbers[59:])
            records[rank] = {"rank": rank, "launch_changed_sites": delta,
                             "actual181": [first["tag181"], first["qualifying159"],
                                           first["active_before181"], first["B2_before181"]],
                             "encoded181": [second["tag181"], second["qualifying159"],
                                            second["active_before181"], second["B2_before181"]]}
            if rank == 43:
                principal = first, second
        elif label in {"ENCODED_GATE", "SIMPLE_GATE"}:
            at, loc, same_pre, same_rad, distinct_c, distinct_b, actual_tag, other_tag = numbers[:8]
            m.require((at, loc) == (tick, site), "incorrect target")
            a_pre, a_c, a_b, b_pre, b_c, b_b = cells(numbers[8:])
            if label == "ENCODED_GATE" and rank == 43:
                m.require((a_pre, a_c, a_b, b_pre, b_c, b_b) == witness,
                          "native target witness disagreement")
            item = {"same_pre_C_cell": bool(same_pre), "same_C_radiation": bool(same_rad),
                    "distinct_C_matter": bool(distinct_c), "distinct_B_matter": bool(distinct_b),
                    "tags": [actual_tag, other_tag]}
            (receiver if label == "ENCODED_GATE" else simple_receiver)[rank] = item
        elif label == "SIMPLE":
            changed, distinct = numbers[:2]
            first, second = unpack_writer(numbers[2:57]), unpack_writer(numbers[57:])
            simple[rank] = {"changed": bool(changed), "distinct_emissions": bool(distinct),
                            "tags181": [first["tag181"], second["tag181"]],
                            "material181": [
                                [k.j_coefficients(v) for v in arm["local181"][2][:2]]
                                for arm in (first, second)
                            ]}
        elif label == "SCREEN":
            tried, distinct, decoded, position, exponent, negative = numbers
            screen = {"tried": tried, "distinct_emissions": distinct, "decoded": decoded,
                      "winner": [position, exponent, negative] if position >= 0 else None}
        else:
            raise ValueError(f"unexpected dual row {label}")
    m.require(set(encoded) == set(original) == set(records), "encoded rank coverage")
    m.require(len(set(encoded.values())) == 85, "encoded launches not injective")
    m.require(principal is not None and screen is not None, "missing principal record")
    digest = hashlib.sha256()
    for rank, field in sorted(encoded.items()):
        m.require(k.reported_account(field) == m.LEDGER, (rank, "encoded launch ledger"))
        a = original[rank]
        changed = [
            sum(first[:2] != second[:2] for first, second in zip(a, field)),
            sum(first[2] != second[2] for first, second in zip(a, field)),
            sum(first[3] != second[3] for first, second in zip(a, field)),
            sum(a[site][3] != field[site][3] for site in CLOCK)
        ]
        m.require(changed == records[rank]["launch_changed_sites"],
                  (rank, "launch stock counts"))
        digest.update(EI.pack(*flatten(field)))
    independent(original[43], encoded[43], principal, target, witness)
    return {"target": {"category": name, "tick": tick, "site": site},
            "encoded_launches_sha256": digest.hexdigest(),
            "launch_changed_sites_order": ["matter", "CLK", "CORR", "original_six_CORR"],
            "encoded_runs": [records[rank] for rank in sorted(records)],
            "principal_181": list(map(to_jsonable, principal)),
            "encoded_receiving_event": receiver,
            "simple_screen": screen, "simple_runs": simple,
            "simple_receiving_event": simple_receiver}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", type=Path)
    parser.add_argument("cascade", type=Path)
    parser.add_argument("native", type=Path)
    args = parser.parse_args()
    print(json.dumps(run(args.query, args.cascade.read_text(encoding="utf-8-sig"),
                         args.native), sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
