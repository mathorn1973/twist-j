#!/usr/bin/env python3
"""Independent full-matrix native contact audit; requires public pre-run release.

No primary contact implementation was read before the byte freeze.
The proof check uses the fibre coefficient sign, independently of a
one/two/three-step collision or translation proof.
"""
import argparse
from contextlib import nullcontext
import hashlib
import itertools
import json
import os
from pathlib import Path
import sys

CHECKS = 0


def require(test, label):
    global CHECKS
    CHECKS += 1
    if not test:
        raise AssertionError(label)


def identity():
    return tuple(tuple(int(i == j) for j in range(7)) for i in range(7))


def affine(rows, constants):
    return tuple(tuple(row)+((constant % 5),)
                 for row, constant in zip(rows, constants)) + ((0,0,0,0,0,0,1),)


def generators():
    a = affine(((0,1,0,0,0,0), (1,0,0,0,0,0), (0,0,0,1,0,0),
                (0,0,1,0,0,0), (0,0,0,0,1,0), (0,0,0,0,0,1)), (0,)*6)
    b = affine(((0,0,-1,0,0,0), (0,0,0,-1,0,0), (-1,0,0,0,0,0),
                (0,-1,0,0,0,0), (0,0,0,0,-1,0), (0,0,0,0,0,-1)), (0,)*6)
    c = affine(((0,0,-1,0,0,0), (0,0,0,-1,0,1), (-1,0,0,0,0,0),
                (0,-1,0,0,0,-1), (0,0,0,0,-1,0), (0,0,0,0,0,-1)),
               (2,1,2,1,1,0))
    neg = tuple(tuple(-int(i == j) for j in range(6)) for i in range(6))
    return a, b, c, affine(neg, (2,1,3,4,1,1)), affine(neg, (2,1,3,4,2,1))


def multiply(a, b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(7)) % 5
                       for j in range(7)) for i in range(7))


def apply(matrix, state):
    vector = tuple(state)+(1,)
    return tuple(sum(a*b for a, b in zip(row, vector)) % 5
                 for row in matrix[:6])


def projection(state):
    return sum(state[:4]) % 5, state[4], state[5]


def projected_step(k, q, r, n):
    i = (k+q+r+2*(n.bit_count() % 2)) % 5
    candidates = ((k,q,r), (-k,-q,-r), (1-k,1-q,-r),
                  (-k,1-q,1-r), (-k,2-q,1-r))
    return tuple(a % 5 for a in candidates[i]), i


def native_history(head, maps):
    state = head
    states, word = [head], []
    for n in range(3):
        i = (sum(state)+2*(n.bit_count() % 2)) % 5
        state = apply(maps[i], state)
        states.append(state)
        word.append(i)
    return tuple(states), tuple(word)


def write_json(path, data):
    path.write_text(json.dumps(data, sort_keys=True, separators=(",", ":"))+"\n",
                    encoding="utf-8")


def audit(out):
    maps = generators()
    require([n.bit_count() % 2 for n in range(3)] == [0,1,1], "actual clock prefix")
    for matrix in maps:
        require(multiply(matrix, matrix) == identity(), "full generator involution")
    word_matrices = {}
    signs = {1: [], 2: [], 3: []}
    shifts = {1: [], 2: [], 3: []}
    words = []
    for z in range(5):
        states, word = native_history((z,0,0,0,0,0), maps)
        words.append(word)
        cumulative = identity()
        for t, i in enumerate(word, 1):
            cumulative = multiply(maps[i], cumulative)
            word_matrices[z, t] = cumulative
            eps = cumulative[4][4]
            require(eps in (1,4), "fibre coefficient sign")
            require(all(cumulative[a][b] == 0 for a in (4,5)
                        for b in range(4)), "word fibre independent of piston coordinates")
            require(cumulative[5][5] == eps and cumulative[4][5] ==
                    cumulative[5][4] == 0, "common fibre scalar coefficient")
            signs[t].append(eps)
            shifts[t].append((cumulative[4][6], cumulative[5][6]))
    require(signs == {1:[1,4,4,4,4], 2:[4,1,1,1,1], 3:[1,4,4,4,4]},
            "exposed prospective sign profiles")
    require(all(len(set(profile)) > 1 for profile in signs.values()),
            "nonconstant sign excludes nonzero source-sum gain")
    records, histories = [], {}
    for head in itertools.product(range(5), repeat=6):
        states, word = native_history(head, maps)
        z = sum(head) % 5
        require(word == words[z], "word depends only on initial total trace")
        projected = projection(head)
        for t in (1,2,3):
            projected, idx = projected_step(*projected, t-1)
            require(idx == word[t-1] and projected == projection(states[t]),
                    "full matrix history versus independent projection")
            require(apply(word_matrices[z,t], head) == states[t],
                    "matrix product versus selected full history")
            require(all(type(x) is int and 0 <= x < 5 for x in states[t]),
                    "every full coordinate canonical")
        histories[head] = states
        records.append({"head": head, "counters": [0,1,2,3],
                        "states": states, "selected_indices": word})
    require(len(records) == 15625, "complete full-state table")
    if out is not None:
        write_json(out/"FULL-HISTORIES.json", records)
        write_json(out/"FIBRE-ACTIONS.json",
                   {"signs": signs, "shifts": shifts, "words": words})

    # Verify every projected source-sum class has an actual source/readout lift.
    for k0, s in itertools.product(range(5), repeat=2):
        if s:
            v, A = (s,0,0,0), (pow(s,-1,5),0,0,0)
        else:
            v, A = (1,4,0,0), (1,0,0,0)
        require(any(v) and sum(v) % 5 == s and
                sum(a*b for a,b in zip(v,A)) % 5 == 1, "source class lift")

    survivors = {t: {s: 0 for s in range(5)} for t in (1,2,3)}
    totals = {t: 0 for t in (1,2,3)}
    mismatch_histogram = {t: {} for t in (1,2,3)}
    rows_checked = 0
    stream = ((out/"RECEIVER-WITNESSES.jsonl").open("w", encoding="utf-8", newline="\n")
              if out is not None else nullcontext(None))
    with stream as witness_file:
        for k0, s, q0, r0 in itertools.product(range(5), repeat=4):
            for wq, wr in itertools.product(range(5), repeat=2):
                if not (wq or wr):
                    continue
                for Bq, Br in itertools.product(range(5), repeat=2):
                    if (Bq*wq+Br*wr) % 5 != 1:
                        continue
                    offset = -(Bq*q0+Br*r0)
                    for t in (1,2,3):
                        mismatches, first = 0, None
                        for x, y in itertools.product(range(5), repeat=2):
                            pistons = (((k0+s*x) % 5,0,0,0) if s else
                                       ((k0+x) % 5, -x % 5,0,0))
                            head = pistons+((q0+wq*y) % 5,(r0+wr*y) % 5)
                            endpoint = histories[head][t]
                            got = (Bq*endpoint[4]+Br*endpoint[5]+offset) % 5
                            wanted = (x+y) % 5
                            rows_checked += 1
                            if got != wanted:
                                mismatches += 1
                                if first is None:
                                    first = (x,y,got,wanted)
                        totals[t] += 1
                        mismatch_histogram[t][mismatches] = \
                            mismatch_histogram[t].get(mismatches,0)+1
                        if first is None:
                            survivors[t][s] += 1
                        record = [t,k0,s,q0,r0,wq,wr,Bq,Br,mismatches,first]
                        if witness_file is not None:
                            witness_file.write(json.dumps(record,separators=(",", ":"))+"\n")
    require(totals == {1:75000,2:75000,3:75000}, "complete receiver class by time")
    require(rows_checked == 5625000, "all25 rows of each225000 configuration")
    require(all(value == 0 for by_s in survivors.values() for value in by_s.values()),
            "receiver survivor falsifies proposed obstruction; full negative STOP")
    return {"status":"PASS", "checks":CHECKS, "full_heads":15625,
            "full_parameter_tuples":438750000000,
            "receiver_configurations":totals, "input_rows":rows_checked,
            "survivors_by_time_and_source_sum":survivors,
            "mismatch_histogram":mismatch_histogram,
            "sign_profiles":signs,
            "scope":"same-reader independent affine preparation; t1..3 actualU"}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", "--out", dest="out", type=Path)
    args = parser.parse_args()
    output = args.out
    if output is None and os.environ.get("TWISTJ_EVIDENCE_DIR"):
        output = Path(os.environ["TWISTJ_EVIDENCE_DIR"])/"independent"
    if output is not None:
        output.mkdir(parents=True, exist_ok=False)
    result = audit(output)
    if output is not None:
        write_json(output/"SUMMARY.json", result)
        manifest = {p.name:hashlib.sha256(p.read_bytes()).hexdigest()
                    for p in sorted(output.iterdir()) if p.is_file()}
        write_json(output/"MANIFEST.json", manifest)
    sys.stdout.buffer.write((json.dumps(result,sort_keys=True,
                                       separators=(",", ":"))+"\n").encode("utf-8"))


if __name__ == "__main__":
    main()
