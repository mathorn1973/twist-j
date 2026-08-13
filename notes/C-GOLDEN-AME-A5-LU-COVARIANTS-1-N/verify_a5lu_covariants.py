#!/usr/bin/env python3
"""Deterministic mod-41 scan of the frozen A5/LU covariant diagrams.

The dense contractions use signed int64 exactly.  Before any contraction the
script proves the uniform bound

    40^6 * 6^11 < 2^63-1,

which bounds every entry of every intermediate/final n<=3 contraction before
reduction.  Thus NumPy supplies speed only; no floating point is involved.
"""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
from itertools import permutations, product
from pathlib import Path
import re

import numpy as np


P = 41
Z_IMAGE = 6
PIN_BYTES = 8515
PIN_SHA256 = "55fbc0ba2747b4e5adc5a5abd15ac7241a461ff8182268ebdae464d8a29cc9ae"
INT64_MAX = 2**63 - 1
RAW_BOUND = 40**6 * 6**11


def parse_rows(block: str, allowed: str):
    rows = [r.strip() for r in block.split(";") if r.strip()]
    out = []
    for n, row in enumerate(rows):
        toks = re.findall(allowed, row)
        if len(toks) != 36:
            raise ValueError(f"row {n}: {len(toks)} tokens")
        out.append(toks)
    if len(out) != 36:
        raise ValueError(f"{len(out)} rows")
    return out


def parse_source(path: Path):
    raw = path.read_bytes()
    assert len(raw) == PIN_BYTES
    assert hashlib.sha256(raw).hexdigest() == PIN_SHA256
    blob = hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest()
    assert blob == "e0d0e171d58b3360c39595d677ffc401a466112d"
    m = re.search(r"U\s*=\s*\[(.*?)\]\s*\.\*\s*w\.\^\s*\[(.*?)\]\s*;", raw.decode(), re.S)
    if not m:
        raise ValueError("matrix blocks not found")
    labs = parse_rows(m.group(1), r"(?<![A-Za-z0-9_])(?:0|a|b|c)(?![A-Za-z0-9_])")
    exps = parse_rows(m.group(2), r"(?<![A-Za-z0-9_])(?:[0-9]|1[0-9])(?![A-Za-z0-9_])")
    entries = {}
    for row in range(36):
        for col in range(36):
            lab = labs[row][col]
            if lab != "0":
                entries[(row//6, row%6, col//6, col%6)] = (lab, 2*int(exps[row][col]) % 40)
    assert len(entries) == 112
    return raw, entries


def diagrams_for(n: int):
    out = []
    for q in range(4):
        for piq in permutations(range(1, n)):
            other_legs = [ell for ell in range(4) if ell != q]
            for choices in product(tuple(permutations(range(n))), repeat=3):
                pis = [None]*4
                pis[q] = tuple(piq)
                for ell, pi in zip(other_legs, choices):
                    pis[ell] = tuple(pi)
                out.append((q, n, tuple(pis)))
    return tuple(out)


def descriptor_text(d):
    q, n, pis = d
    return f"q={q};n={n};" + ";".join(f"pi{ell}=" + ",".join(map(str, pis[ell])) for ell in range(4))


def build_tensors(entries):
    z = Z_IMAGE
    w = z*z % P
    c = (pow(z, 5, P) + pow(z, -5, P))*pow(2, -1, P) % P
    a = c*pow((w + pow(w, -1, P)) % P, -1, P) % P
    b = (pow(w, 2, P) + pow(w, -2, P))*a % P
    amps = {"a": a, "b": b, "c": c}
    A = np.zeros((6,6,6,6), dtype=np.int64)
    Abar = np.zeros_like(A)
    for x, (lab, e) in entries.items():
        A[x] = amps[lab]*pow(z, e, P) % P
        Abar[x] = amps[lab]*pow(z, -e, P) % P
    return A, Abar, amps


def einsum_spec(d):
    q, n, pis = d
    # Labels 0 and 1 are the open row/column.  The remaining 11 labels are
    # the contracted wires for n=3 (7 for n=2).
    open_i, open_j, nxt = 0, 1, 2
    left = [[None]*4 for _ in range(n)]
    right = [[None]*4 for _ in range(n)]
    left[0][q] = open_i
    right[0][q] = open_j
    for ell in range(4):
        if ell == q:
            for r in range(1, n):
                left[r][ell] = nxt
                right[pis[q][r-1]][ell] = nxt
                nxt += 1
        else:
            for r in range(n):
                left[r][ell] = nxt
                right[pis[ell][r]][ell] = nxt
                nxt += 1
    assert all(all(x is not None for x in scope) for scope in left+right)
    return tuple(tuple(s) for s in left), tuple(tuple(s) for s in right), (open_i, open_j)


def contract(A, Abar, d):
    left, right, output = einsum_spec(d)
    args = []
    for scope in left:
        args.extend((A, list(scope)))
    for scope in right:
        args.extend((Abar, list(scope)))
    args.append(list(output))
    raw = np.einsum(*args, optimize="greedy")
    assert raw.dtype == np.int64
    return raw % P


def scalar_value(C):
    d = int(C[0,0])
    if all(int(C[i,j]) == (d if i == j else 0) for i in range(6) for j in range(6)):
        return d
    return None


def sparse_n2(entries, values, bars, d):
    """Independent sparse ordering for the n=2 orientation audit."""
    q, n, pis = d
    assert n == 2
    items = tuple((x, values[x]) for x in sorted(entries))
    partial = {}
    for y in sorted(entries):
        key = y[:q] + y[q+1:]
        partial.setdefault(key, []).append((y[q], bars[y]))
    C = [[0]*6 for _ in range(6)]
    for x0, v0 in items:
        for x1, v1 in items:
            xs = (x0, x1)
            ys = [[-1]*4 for _ in range(2)]
            for ell in range(4):
                if ell == q:
                    ys[pis[q][0]][q] = x1[q]
                else:
                    for r in range(2):
                        ys[pis[ell][r]][ell] = xs[r][ell]
            other = tuple(ys[1])
            vb = bars.get(other)
            if vb is None:
                continue
            key0 = tuple(ys[0][ell] for ell in range(4) if ell != q)
            base = v0*v1*vb % P
            for j, vb0 in partial.get(key0, ()):
                C[x0[q]][j] = (C[x0[q]][j] + base*vb0) % P
    return np.array(C, dtype=np.int64)


def rotation_power(power):
    R = np.array([[3,19],[-19,3]], dtype=np.int64) % P
    out = np.eye(2, dtype=np.int64)
    for _ in range(power):
        out = out @ R % P
    return out


def deterministic_orthogonals():
    mats = []
    for q in range(4):
        V = np.zeros((6,6), dtype=np.int64)
        for block in range(3):
            V[2*block:2*block+2, 2*block:2*block+2] = rotation_power(q+block+1)
        assert np.array_equal(V @ V.T % P, np.eye(6, dtype=np.int64))
        mats.append(V)
    return tuple(mats)


def local_transform(T, Vs):
    raw = np.einsum(Vs[0],[0,4], Vs[1],[1,5], Vs[2],[2,6], Vs[3],[3,7],
                    T,[4,5,6,7], [0,1,2,3], optimize="greedy")
    return raw % P


def covariance_audit(ds):
    # A generic deterministic prime-field tensor makes orientation errors
    # visible; conjugation fixes all its entries.
    T = np.fromfunction(lambda i,j,k,l: (1 + i + 2*j + 4*k + 8*l + i*j + k*l) % P,
                        (6,6,6,6), dtype=int).astype(np.int64)
    Vs = deterministic_orthogonals()
    TV = local_transform(T, Vs)
    checked = 0
    digest = hashlib.sha256()
    for d in ds:
        C = contract(T, T, d)
        CV = contract(TV, TV, d)
        q = d[0]
        target = Vs[q] @ C @ Vs[q].T % P
        assert np.array_equal(CV, target)
        digest.update((descriptor_text(d)+":"+",".join(map(str, C.reshape(-1)))+"\n").encode())
        checked += 1
    return checked, digest.hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("source", type=Path)
    args = ap.parse_args()
    assert RAW_BOUND == 1486016741376000000
    assert RAW_BOUND < INT64_MAX
    raw, entries = parse_source(args.source)
    assert pow(Z_IMAGE,40,P) == 1
    assert all(pow(Z_IMAGE,d,P) != 1 for d in (1,2,4,5,8,10,20))
    A, Abar, amps = build_tensors(entries)
    ds2, ds3 = diagrams_for(2), diagrams_for(3)
    assert len(ds2) == 32 and len(ds3) == 1728
    listing = "\n".join(descriptor_text(d) for d in ds2+ds3)+"\n"
    print("SOURCE bytes", len(raw), "sha256", PIN_SHA256, "support", len(entries))
    print("ARITHMETIC F41 z", Z_IMAGE, "order40 YES conjugate", pow(Z_IMAGE,-1,P), "amplitudes", amps)
    print("INT64_EXACT_BOUND", RAW_BOUND, "LT", INT64_MAX)
    print("DIAGRAMS n2_per_leg 8 n2_total", len(ds2), "n3_per_leg 432 n3_total", len(ds3),
          "list_sha256", hashlib.sha256(listing.encode()).hexdigest())

    # Independent sparse/dense orientation check for all 32 n=2 diagrams.
    values = {x:int(A[x]) for x in entries}
    bars = {x:int(Abar[x]) for x in entries}
    for d in ds2:
        assert np.array_equal(contract(A,Abar,d), sparse_n2(entries,values,bars,d))
    print("ORIENTATION_AUDIT sparse_vs_dense_n2", len(ds2), "PASS")

    transcript = hashlib.sha256()
    counts = {(q,n):Counter() for q in range(4) for n in (2,3)}
    nonscalar = []
    for d in ds2+ds3:
        C = contract(A,Abar,d)
        s = scalar_value(C)
        rec = descriptor_text(d)+f";scalar={s}" if s is not None else descriptor_text(d)+";matrix="+",".join(map(str,C.reshape(-1)))
        transcript.update((rec+"\n").encode())
        print("COVARIANT", rec)
        if s is None:
            nonscalar.append((d,C))
        else:
            counts[(d[0],d[1])][s] += 1
    print("SCALAR_CLASS_TRANSCRIPT_SHA256", transcript.hexdigest())
    for q in range(4):
        for n in (2,3):
            print("SCALAR_COUNTS", "q",q,"n",n, tuple(sorted(counts[(q,n)].items())))
    print("NONSCALAR_COUNT", len(nonscalar))
    assert not nonscalar

    # Exact finite-field covariance audit on a generic, non-AME tensor for
    # every orientation; this supplements (not replaces) the index proof.
    checked, covhash = covariance_audit(ds2+ds3)
    print("COVARIANCE_AUDIT generic_tensor nonmonomial_orthogonal_tuple diagrams", checked,
          "PASS transcript_sha256", covhash)
    print("VERDICT MOD41_NO_BREAK_THROUGH_ALL_FROZEN_N_LE_3 INCONCLUSIVE")


if __name__ == "__main__":
    main()
