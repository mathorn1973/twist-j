#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Phase-2 comparison helper (NOT part of the frozen checker).

Re-derives the reviewer's own states with the frozen review.py primitives and
re-serializes them in the author's formats, so that the author's recorded
hashes (word JSON, assembly final states, BFS visited order) can be compared
with the reviewer's independent computation.  Run from the repository root:

    python3 notes/C-S3-HEIGHT-PHASE-INTERFACE-N-REVIEW-1/compare_after_run.py \
        notes/C-S3-HEIGHT-PHASE-INTERFACE-N-REVIEW-1/RUN-VERIFY.txt \
        notes/C-S3-HEIGHT-PHASE-INTERFACE-N-REVIEW-1/RUN-ASSEMBLY.txt \
        notes/C-S3-HEIGHT-PHASE-INTERFACE-N-REVIEW-1/RUN-SEARCH.txt
"""
from __future__ import annotations

import hashlib
import json
import os
import sys
from collections import deque

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import review as rv  # noqa: E402  (the frozen checker, imported for its primitives)


def sha_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def main(verify_path, assembly_path, search_path) -> int:
    rv.build_y_table()
    verify = json.load(open(verify_path, encoding="ascii"))
    assembly = json.load(open(assembly_path, encoding="ascii"))
    search = json.load(open(search_path, encoding="ascii"))
    lines = []
    ok_all = True

    def rep(name, ok, detail):
        nonlocal ok_all
        ok_all &= ok
        lines.append(f"{name} {'MATCH' if ok else 'DIFF'} {detail}")

    # --- compiler word in the author's one-based JSON format
    A_ops = rv.word_A()
    one_based = [[op[1] + 1, op[2] + 1] for op in A_ops]
    enc = json.dumps(one_based, separators=(",", ":")).encode("ascii")
    raw_equal = one_based == verify["word_one_based"]
    flipped = [i for i, (m, a) in enumerate(zip(one_based, verify["word_one_based"])) if m != a]
    norm_mine = [sorted(p) for p in one_based]
    norm_author = [sorted(p) for p in verify["word_one_based"]]
    lines.append(f"word_one_based_raw {'MATCH' if raw_equal else 'DIFF-CONVENTION'} positions_with_reversed_orientation={len(flipped)} "
                 f"(mine follows PROOF §3 literally, C(d_s,g); author canonicalizes a<b); my_raw_json_sha={sha_bytes(enc)}")
    rep("word_one_based_orientation_free", norm_mine == norm_author and len(flipped) == sum(1 for m, a in zip(one_based, verify["word_one_based"]) if m == a[::-1]),
        "95 unordered pairs equal in order; every raw difference is a pure orientation flip (contact map is orientation-free, review.py R02)")
    enc_norm = json.dumps(norm_mine, separators=(",", ":")).encode("ascii")
    rep("word_json_sha256", sha_bytes(enc_norm) == verify["word_json_sha256"], f"author format recomputed from my orientation-normalized word: {sha_bytes(enc_norm)}")

    # --- stock and transformed x
    Z = rv.stock_Z()
    rep("stock_four_coefficients", [list(z) for z in Z] == verify["stock_four_coefficients"], "seven values")
    rep("transformed_x", [list(rv.X_S[t]) for t in range(-2, 3)] == verify["transformed_x_four_coefficients"], "x_t values")
    rep("stock_accounts", verify["stock_q"] == 80 and verify["stock_h_coefficients"] == [33, 14] and verify["stock_sum_four_coefficients"] == [-4, -10, -6, -10], "Q=80 H=33+14phi Sigma")

    # --- endpoints and traces
    ok, traces, ends, cuts = rv.compile_run(A_ops, {t: rv.input_I(t) for t in range(-2, 3)}, Z)
    e_ok = all([list(v) for v in ends[t]] == verify["complete_final_states"][str(t)] for t in range(-2, 3))
    t_ok = all(traces[t] == verify["forward_admission_traces"][str(t)] for t in range(-2, 3))
    rep("complete_final_states", ok and e_ok, "five 15-slot endpoints equal state by state")
    rep("forward_admission_traces", t_ok, f"five traces equal; admitted per t={[traces[t].count('A') for t in range(-2, 3)]}")
    rep("complete_initial_q", all(verify["complete_initial_q"][str(t)] == 119 + 10 * t * t for t in range(-2, 3)), "119+10t^2")
    my_tr_fp = rv.sha("\n".join(verify["forward_admission_traces"][str(t)] for t in range(-2, 3)) + "\n")
    rep("FP_TRACES_from_author_data", my_tr_fp == "075ca8281d2cb629f800e5e2ea3e9e49452159db915bbe2c76c09ffcae71863a", f"{my_tr_fp}")
    my_end_fp = rv.sha("\n".join(rv.ser_state(tuple(tuple(v) for v in verify["complete_final_states"][str(t)])) for t in range(-2, 3)) + "\n")
    rep("FP_ENDPOINTS_from_author_data", my_end_fp == "46b86040ef87c325d1417beb27546494c80b5d5706cb3e0e09c56bf7f023e549", f"{my_end_fp}")

    # --- assembly final states in the author's digest format
    S_ops, _ = rv.build_S()
    W_ops = rv.rep(S_ops, 10)
    Winv_ops = rv.inverse_ops(W_ops)
    c0, a0, s0 = rv.STATS["contacts"], rv.STATS["admitted"], rv.STATS["swaps"]
    digests = []
    for seq in rv.CASES:
        st, k = rv.initial_assembly(seq)
        segs = rv.assembly_program(k, A_ops, W_ops, Winv_ops)
        fwd = [op for _, ops in segs for op in ops]
        rv.apply_ops(st, fwd)
        digests.append(sha_bytes(json.dumps(st, separators=(",", ":")).encode()))
        rv.apply_ops(st, rv.inverse_ops(fwd))
    author_digests = [row["final_state_sha256"] for row in assembly["cases"]]
    author_inputs = [[tuple(x) for x in row["inputs"]] for row in assembly["cases"]]
    rep("assembly_case_order", author_inputs == rv.CASES, "14 cases in the same order")
    rep("assembly_final_state_sha256", digests == author_digests, "14 digests equal in the author's JSON format")
    contacts = rv.STATS["contacts"] - c0
    admitted = rv.STATS["admitted"] - a0
    swaps = rv.STATS["swaps"] - s0
    rep("assembly_counts", contacts == assembly["contact_cuts"] == 2597775 and swaps == assembly["swap_cuts"] == 50
        and admitted == assembly["accepted"] and contacts - admitted == assembly["refused"],
        f"contacts={contacts} admitted={admitted} refused={contacts - admitted} swaps={swaps}")
    rep("assembly_per_case_Q_H", all(row["Q"] == rv.full_invariants(rv.initial_assembly(list(map(tuple, row["inputs"])))[0])[2]
                                     and tuple(row["H"]) == rv.full_invariants(rv.initial_assembly(list(map(tuple, row["inputs"])))[0])[1]
                                     and row["slots"] == 39 + 25 * len(row["inputs"]) for row in assembly["cases"]), "Q, H, slots per case")

    # --- BFS visited order in the author's digest format
    edges = [rv.C(a, b) for a in range(8) for b in range(a + 1, 8)]
    root = tuple(tuple(rv.input_I(t)) for t in range(-2, 3))
    targets = [rv.clock_target(t) for t in range(-2, 3)]
    order = [root]
    visited = {root}
    queue = deque([(root, 0)])
    generated = unchanged = duplicate = 0
    expanded = 0
    found = False
    while queue:
        node, depth = queue.popleft()
        if depth >= 6:
            break
        for e in edges:
            child = []
            for stt in node:
                lst = list(stt)
                rv.apply_ops(lst, (e,))
                child.append(tuple(lst))
            child = tuple(child)
            generated += 1
            if child == node:
                unchanged += 1
                continue
            if child in visited:
                duplicate += 1
                continue
            visited.add(child)
            order.append(child)
            queue.append((child, depth + 1))
            if all((child[i][6], child[i][7]) == targets[i] for i in range(5)):
                found = True
        expanded += 1
        if len(order) >= 20000:
            break
    dg = hashlib.sha256()
    for node in order:
        flat = [list(v) for stt in node for v in stt]
        dg.update(json.dumps(flat, separators=(",", ":")).encode("ascii"))
        dg.update(b"\n")
    rep("bfs_visited", len(order) == search["visited"] == 12853 and not found, f"visited={len(order)}")
    rep("bfs_counters", generated == search["generated"] and unchanged == search["unchanged"] and duplicate == search["duplicate"]
        and expanded == search["fully_expanded_nodes"], f"generated={generated} unchanged={unchanged} duplicate={duplicate} expanded={expanded}")
    rep("bfs_visited_states_sha256", dg.hexdigest() == search["visited_states_sha256"], f"{dg.hexdigest()}")
    rep("bfs_status", search["status"] == "INCONCLUSIVE" and search["reason"] == "DEPTH_CAP", "author INCONCLUSIVE / DEPTH_CAP; mine INCONCLUSIVE / depth cap")

    lines.append("COMPARE " + ("ALL MATCH" if ok_all else "DIFFERENCES PRESENT"))
    sys.stdout.write("\n".join(lines) + "\n")
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:4]))
