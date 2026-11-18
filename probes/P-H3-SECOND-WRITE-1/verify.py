# SPDX-License-Identifier: Apache-2.0
"""Four-wire H3 continuation after the first causal write."""
import json
import subprocess
import tempfile
from hashlib import sha256
from pathlib import Path

import kernel as k
import measure
import witness


HERE = Path(__file__).resolve().parent
CLOCK = (0, 1, 4, 5, 8, 9)
WIRES = ((0, 7, (-2, 0, -1, 0)), (1, 28, (-3, 0, -1, 0)),
         (2, 8, (1, 0, 2, 3)), (3, 31, (0, 1, 0, 1)))
LAUNCH_DIGEST = "8e65f16a2f545c566c3b2fa915fd993f3fd0e78644a17b12567a42ccc434c4cd"


def check(ok, context):
    if not ok:
        raise ValueError(context)


def emit(section, value):
    print(json.dumps({"section": section, "value": value}, sort_keys=True, separators=(",", ":")))


def encode(field):
    return " ".join(str(i) for cell in field for word in cell for i in k.reported(word))


def decode(parts):
    values = list(map(int, parts))
    check(len(values) == 512, "complete field required")
    words = [k.from_j(*values[i:i+4]) for i in range(0, 512, 4)]
    return tuple(tuple(words[i:i+4]) for i in range(0, 128, 4))


def launches():
    raw = (HERE / "launch43.json").read_bytes()
    check(sha256(raw).hexdigest() == "1a4d47ff21e95385f93fe05915aed409a38d1ebb40f3e2f0e724c6f8eb267d7f",
          "literal launch differs from predecessor")
    template = tuple(tuple(k.from_j(*word) for word in cell) for cell in json.loads(raw))
    findings, digest = k.Findings(), sha256()
    orbit, _, ready = k.bare_reference(findings, digest)
    check(not findings.counts and set(ready) == set(range(85)), "bare clock")
    clock_words, fields = set(), []
    for rank in range(85):
        original = orbit[(ready[rank] - 1) % k.PERIOD]
        field = [list(cell) for cell in template]
        for s in CLOCK:
            field[s][k.CORR] = original[s][k.CORR]
        for source, target, bias in WIRES:
            field[target][k.CLK] = k.add(original[source][k.CLK], k.from_j(*bias))
        fields.append(tuple(map(tuple, field)))
        clock_words.add(tuple(field[s][k.CORR] for s in CLOCK))
        check(k.reported_account(field) == measure.LEDGER, ("launch ledger", rank))
    launch_hash = sha256("".join(encode(f)+"\n" for f in fields).encode("ascii")).hexdigest()
    check(len(clock_words) == len(set(fields)) == 85 and fields[43] == template, "phase integrity")
    check(launch_hash == LAUNCH_DIGEST, "ordered predecessor launches")
    return fields


def native(fields):
    queries = "".join(f"2 {i} 0 {encode(f)}\n" for i, f in enumerate(fields)).encode("ascii")
    with tempfile.TemporaryDirectory() as build:
        exe = Path(build) / "renew"
        subprocess.run(["g++", "-std=c++20", "-O3", str(HERE / "renew.cpp"), "-o", str(exe)], check=True)
        run = subprocess.run([str(exe)], input=queries, capture_output=True, check=True)
    check(not run.stderr, "unexpected native stderr")
    header, *lines = run.stdout.decode("ascii").splitlines()
    columns = header.split()
    rows, ends, snapshots = {}, {}, {}
    for line in lines:
        parts = line.split()
        if parts[0] == "WITNESS":
            _, rank, tick, event, stage = parts[:5]
            key = (int(rank), int(tick), event)
            cuts = snapshots.setdefault(key, {})
            check(stage not in cuts, "duplicate witness")
            cuts[stage] = decode(parts[5:])
        elif parts[0] == "END":
            _, rank, scanned, bit = parts[:4]
            rank = int(rank)
            field = decode(parts[4:])
            check(rank not in ends and k.reported_account(field) == measure.LEDGER, "terminal ledger")
            ends[rank] = (int(scanned), int(bit), field)
        else:
            row = dict(zip(columns, map(int, parts), strict=True))
            check(row["rank"] not in rows, "duplicate result")
            rows[row["rank"]] = row
    check(set(rows) == set(ends) == set(range(85)), "missing launches")
    return rows, ends, snapshots


def main():
    fields = launches()
    rows, ends, snapshots = native(fields)
    emit("protocol", dict(launches_sha256=LAUNCH_DIGEST, clocks=85, ledger=measure.LEDGER,
                          second_work="function", identical_inputs_and_paid_work="exact_work"))
    for rank in range(85):
        row = rows[rank]
        scanned, bit, end = ends[rank]
        check(row["scanned"] == scanned and bit == (1 ^ (scanned % 2)) and row["inverse"] == 1,
              ("terminal state", rank))
        first, _ = measure.trial(fields[rank], 2, rank)
        first_tick = first[measure.HEADER.index("work_tick")]
        check(first_tick == row["first_write"] and first[2] == row["source125"], ("first write", rank))
        check(not first_tick or first[measure.HEADER.index("paid_work_tick")] == 159, ("first escrow", rank))
        emit("rank", dict(**row, end_sha256=sha256(f"{bit} {encode(end)}\n".encode("ascii")).hexdigest()))
    for (rank, tick, event), cuts in sorted(snapshots.items()):
        check(set(cuts) == {"pre", "c", "b"}, "partial witness")
        post_c, post_b, _ = measure.native(cuts["pre"], tick, k.account(fields[rank]), (rank, tick, event))
        check((post_c, post_b) == (cuts["c"], cuts["b"]), "snapshot mismatch")
        record = dict(rank=rank, tick=tick, event=event,
                      pre_field_sha256=sha256(encode(cuts["pre"]).encode("ascii")).hexdigest(),
                      memory=witness._local(cuts["pre"], post_c, post_b, measure.MEMORY),
                      worker=witness._local(cuts["pre"], post_c, post_b, 28))
        if event in ("function", "exact_work"):
            record["compensated"] = witness.inspect_contact(cuts["pre"], tick)
        emit("snapshot", record)
    for rank in (0, 22, 43):
        row = rows[rank]
        hit = row["function"]
        prefix = 8192
        if hit and hit <= 32768:
            prefix = max(prefix, hit + 64)
        prefix = min(prefix, row["scanned"])
        detail = witness.replay(fields[rank], hit or None, prefix, fresh_source_window=64)
        check(detail["first_qualifying_later_work"] == (hit if 0 < hit <= prefix else None),
              ("Python first later work", rank))
        for a,b in (("pre_worker","pre_worker"), ("radiation","radiation"),
                    ("receiver_ready","ready"), ("joint_ready","word_ready")):
            when = row[b]
            observed = detail["readiness"][a]
            check(observed["first"] == (when if 0 < when <= prefix else None), ("readiness", rank, a))
            if prefix == row["scanned"]:
                check(observed["count"] == row[b+"_count"], ("readiness count", rank, a))
        if detail["witness"]:
            form = detail["witness"]["last_formation_before_read"]["cut"]
            check(form == [row["work_formation_tick"], {1:"C",2:"B"}[row["work_formation_cut"]]],
                  ("continuous retention since last formation", rank))
        emit("python_replay", dict(rank=rank, **detail))


if __name__ == "__main__":
    main()
