#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Test exact one-payer restoration of the original six H3 clock words."""

import argparse
from collections import Counter
from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True
import verify

k = verify.k
HEADER = verify.HEADER
CLOCK = verify.CLOCK


def emit(section, value):
    print(json.dumps(dict(section=section, value=value), sort_keys=True, separators=(",", ":")))


def read_modes(path):
    raw = path.read_bytes()
    sections = [json.loads(line) for line in raw.splitlines()]
    protocol, = (s["value"] for s in sections if s["section"] == "protocol")
    screen, = (s["value"] for s in sections if s["section"] == "screen")
    if protocol["columns"] != HEADER or len(screen["rows"]) != screen["eligible"]:
        raise ValueError("incompatible primary transcript")
    rank = protocol["target_rank"]
    rows = [dict(zip(HEADER, row, strict=True)) for row in screen["rows"]]
    modes = sorted(row["mode"] for row in rows if row["rank"] == rank and row["work_tick"])
    if len(modes) != 18 or len(set(modes)) != len(modes):
        raise ValueError(("unexpected strict auxiliary mode set", modes))
    return protocol, modes, sha256(raw).hexdigest()


def prepare(protocol, modes):
    findings = k.Findings()
    digest = sha256()
    bare, _, ready = k.bare_reference(findings, digest)
    ranks = list(range(protocol["ranks"]))
    if findings.counts or digest.hexdigest() != protocol["bare_sha256"] or set(ready) != set(ranks):
        raise ValueError("bare reference mismatch")
    originals = [verify.stock.baseline(bare[(ready[rank] - 1) % k.PERIOD]) for rank in ranks]
    reference = protocol["target_rank"]
    original = originals[reference]
    ledger = k.account(original)
    clock_port = {(site, k.CORR) for site in CLOCK}
    bare_seeds = [bare[(ready[rank] - 1) % k.PERIOD] for rank in ranks]
    variable_port = {
        (site, lane) for site, cell in enumerate(bare_seeds[0]) for lane in range(len(cell))
        if len({field[site][lane] for field in bare_seeds}) > 1
    }
    ports = (("six", sorted(clock_port)), ("phase", sorted(clock_port | variable_port)))
    states = {reference: verify.native_baselines([original])[0]}
    radiation = ((2, "CLK"), (k.CORR, "CORR"))
    cases, support = [], []

    for mode in modes:
        field = verify.field_for(states, reference, mode)
        if field is None:
            raise ValueError(("strict auxiliary construction disappeared", mode))
        target = field
        depth, _ = divmod(mode, 10000)
        for tick in range(depth, 0, -1):
            field = k.inverse_step(field, tick % 2)
            if k.account(field) != ledger:
                raise ValueError(("inverse ledger", mode, tick))
        replay = field
        for tick in range(1, depth + 1):
            replay = verify.measure.native(replay, tick, ledger, (mode, tick, "preimage"))[1]
        if replay != target:
            raise ValueError(("inverse round trip", mode))

        for profile, port in ports:
            prepare_repairs(profile, port, radiation, originals, reference, mode, field,
                            ledger, cases, support, variable_port)
    return cases, support, {**dict(ports), "phase_delta": sorted(clock_port | variable_port)}


def prepare_repairs(profile, port, radiation, originals, reference, mode, field,
                    ledger, cases, support, variable_port):
    if not port:
        raise ValueError("empty input port")
    original = originals[reference]
    base_clock = tuple(original[site][lane] for site, lane in port)
    old_clock = tuple(field[site][lane] for site, lane in port)
    if any(lane < 2 for _, lane in port):
        delta_m = k.subtract(k.add(*(original[s][l] for s, l in port if l < 2)),
                             k.add(*(field[s][l] for s, l in port if l < 2)))
    else:
        delta_m = k.ZERO
    base_radiation = tuple(original[site][lane] for site, lane in port if lane >= 2)
    old_radiation = tuple(field[site][lane] for site, lane in port if lane >= 2)
    delta_u = k.subtract(k.add(*base_radiation), k.add(*old_radiation))
    delta_h = k.subtract(k.add(*(k.norm(word) for word in base_clock)),
                         k.add(*(k.norm(word) for word in old_clock)))
    payers = []
    if delta_m == k.ZERO and delta_u == delta_h == k.ZERO:
        payers.append((None, None, None, None, None))
    elif delta_m == k.ZERO:
        for site, cell in enumerate(field):
            for lane, name in radiation:
                if (site, lane) in port:
                    continue
                old = cell[lane]
                new = k.subtract(old, delta_u)
                if k.subtract(k.norm(old), k.norm(new)) == delta_h:
                    payers.append((site, lane, name, old, new))
    support.append(dict(parent_mode=mode, profile=profile,
                        delta_M=k.reported(delta_m), delta_U=k.reported(delta_u),
                        delta_H=k.reported(delta_h),
                        changed_slots=sum(a != b for a, b in zip(base_clock, old_clock)),
                        payers=len(payers)))
    for site, lane, name, old, new in payers:
        fixed = [list(cell) for cell in field]
        if site is not None:
            fixed[site][lane] = new
        for port_site, port_lane in port:
            fixed[port_site][port_lane] = original[port_site][port_lane]
        payer = None if site is None else dict(
            index=site, xy=divmod(site, k.HEIGHT), lane=name,
            before=k.reported(old), after=k.reported(new))

        input_profiles = [(profile, port)]
        if profile == "six":
            input_profiles.append(("phase_delta", sorted(set(port) | variable_port)))
        for input_profile, delta_port in input_profiles:
            launches = []
            for rank, baseline in enumerate(originals):
                assigned = [cell.copy() for cell in fixed]
                for port_site, port_lane in delta_port:
                    change = k.subtract(baseline[port_site][port_lane], original[port_site][port_lane])
                    assigned[port_site][port_lane] = k.add(fixed[port_site][port_lane], change)
                launch = tuple(tuple(cell) for cell in assigned)
                if any(launch[s][l] != baseline[s][l] for s, l in port):
                    raise ValueError(("input projection mismatch", mode, rank))
                launches.append(launch if k.account(launch) == ledger else None)
            if launches[reference] is None:
                raise ValueError(("repaired reference ledger mismatch", mode, site, lane))
            cases.append((mode, input_profile, payer, launches))



def audit_batch(exe, cases):
    requests = [
        f"{case_id} {rank} 0 {verify.encode(field)}\n"
        for case_id, (_, _, _, launches) in enumerate(cases, 1)
        for rank, field in enumerate(launches) if field is not None
    ]
    if not requests:
        return {}
    process = subprocess.run([str(exe)], input="".join(requests).encode("ascii"),
                             capture_output=True, check=True)
    if process.stderr:
        raise ValueError(process.stderr.decode(errors="replace"))
    schema, *lines = process.stdout.decode("ascii").splitlines()
    if schema.split() != HEADER:
        raise ValueError("native schema mismatch")
    rows = {}
    for line in lines:
        row = tuple(map(int, line.split()))
        if len(row) != len(HEADER) or row[:2] in rows:
            raise ValueError(("invalid native row", row))
        rows[row[:2]] = row
    expected_keys = {(case_id, rank)
                     for case_id, (_, _, _, launches) in enumerate(cases, 1)
                     for rank, launch in enumerate(launches) if launch is not None}
    if rows.keys() != expected_keys:
        raise ValueError("native query domain mismatch")
    return rows


def report(cases, rows):
    totals, distinct_launch_lists = Counter(), set()
    best = None
    for case_id, (parent_mode, profile, payer, launches) in enumerate(cases, 1):
        data = [rows.get((case_id, rank)) for rank in range(len(launches))]
        digest = sha256()
        launch_digest = sha256()
        counts = {key: 0 for key in HEADER[2:]}
        for rank, (row, launch) in enumerate(zip(data, launches)):
            if launch is None:
                digest.update(f"{case_id} {rank} ineligible\n".encode("ascii"))
                launch_digest.update(f"{rank} ineligible\n".encode("ascii"))
                continue
            digest.update((" ".join(map(str, row)) + "\n").encode("ascii"))
            launch_digest.update((verify.encode(launch) + "\n").encode("ascii"))
            for key, value in zip(HEADER[2:], row[2:]):
                counts[key] += bool(value)
            priority = verify.priority(row)
            if best is None or (priority, -case_id, -rank) > best[0]:
                best = ((priority, -case_id, -rank), case_id, rank)
        distinct_launch_lists.add(launch_digest.hexdigest())
        totals.update(counts)
        emit("repair", dict(case=case_id, parent_mode=parent_mode, profile=profile, payer=payer,
                           eligible=sum(row is not None for row in data), ranks=len(data),
                           ineligible=[rank for rank, launch in enumerate(launches) if launch is None],
                           counts=counts,
                           rank_rows_sha256=digest.hexdigest(),
                           launch_rows_sha256=launch_digest.hexdigest()))
    emit("total", dict(cases=len(cases), rank_rows=len(rows), distinct_launch_lists=len(distinct_launch_lists),
                      counts={key: totals[key] for key in HEADER[2:]}))
    if best is not None:
        _, case_id, witness_rank = best
        parent_mode, profile, payer, launches = cases[case_id - 1]
        for rank, launch in enumerate(launches):
            if launch is None:
                continue
            row, detail = verify.measure.trial(launch, case_id, rank, details=rank == witness_rank)
            if tuple(row) != rows[case_id, rank]:
                raise ValueError(("Python/C++ row mismatch", case_id, rank))
            if rank == witness_rank:
                best_witness = dict(case=case_id, parent_mode=parent_mode, profile=profile, payer=payer,
                                    rank=rank, row=row, detail=detail)
        emit("replay", dict(ranks=len(launches), eligible=sum(x is not None for x in launches), witness=best_witness))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("primary", nargs="?", type=Path, default=verify.HERE / "EXPECTED.txt")
    parser.add_argument("--exe", type=Path, help="optional executable built from the pinned audit.cpp")
    args = parser.parse_args()
    protocol, modes, transcript_hash = read_modes(args.primary)
    cases, support, ports = prepare(protocol, modes)
    emit("protocol", dict(primary_sha256=transcript_hash, original_rank=protocol["target_rank"],
                         ranks=protocol["ranks"], strict_auxiliaries=len(modes), columns=HEADER, ports=ports,
                         priority="pinned endpoint priority, then ascending repair ID and rank"))
    emit("parents", support)
    if args.exe is not None:
        rows = audit_batch(args.exe.resolve(), cases)
    else:
        with tempfile.TemporaryDirectory() as directory:
            exe = Path(directory) / ("audit.exe" if os.name == "nt" else "audit")
            command = ["g++", "-std=c++20", "-O3"]
            if os.name == "nt":
                command.append("-static")
            subprocess.run([*command, str(verify.HERE / "audit.cpp"), "-o", str(exe)], check=True)
            rows = audit_batch(exe, cases)
    report(cases, rows)


if __name__ == "__main__":
    main()
