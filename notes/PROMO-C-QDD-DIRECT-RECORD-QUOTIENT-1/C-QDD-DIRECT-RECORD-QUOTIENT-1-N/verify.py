#!/usr/bin/env python3
"""Exact audit for C-QDD-DIRECT-RECORD-QUOTIENT-1-N.

NON-CANONICAL incubation. The direct record is computed in Q(zeta_5) from
field arithmetic. No factor map, effect pair or Born pairing is used.
"""

from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import product

BASIS = tuple(tuple(F(int(i == j)) for i in range(4)) for j in range(4))
POW = BASIS + ((F(-1),) * 4,)
ZERO = (F(0),) * 4
LAMBDA = (F(1),) * 4
ELL = (0, 1, 2, -2, -1)


def add(a, b): return tuple(x + y for x, y in zip(a, b))
def sub(a, b): return tuple(x - y for x, y in zip(a, b))
def scale(c, a): return tuple(c * x for x in a)

def mul(a, b):
    out = [F(0)] * 4
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x and y:
                p = POW[(i + j) % 5]
                for k in range(4): out[k] += x * y * p[k]
    return tuple(out)
def conj(a):
    out = [F(0)] * 4
    for i, x in enumerate(a):
        p = POW[(-i) % 5]
        for k in range(4): out[k] += x * p[k]
    return tuple(out)
def tr(a):
    cols = [mul(a, e) for e in BASIS]
    return sum(cols[j][j] for j in range(4))
def pair(a, b): return tr(mul(a, conj(b))) / 5
LAM_NORM = pair(LAMBDA, LAMBDA)


def mmul(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))) for i in range(len(a)))
def mscale(c, a): return tuple(tuple(c * x for x in row) for row in a)
def eye(n): return tuple(tuple(F(int(i == j)) for j in range(n)) for i in range(n))
def minv(a):
    n = len(a); I = eye(n)
    aug = [list(a[i]) + list(I[i]) for i in range(n)]
    for c in range(n):
        p = next(r for r in range(c, n) if aug[r][c])
        aug[c], aug[p] = aug[p], aug[c]
        z = aug[c][c]; aug[c] = [x / z for x in aug[c]]
        for r in range(n):
            if r != c and aug[r][c]:
                z = aug[r][c]; aug[r] = [x - z * y for x, y in zip(aug[r], aug[c])]
    return tuple(tuple(row[n:]) for row in aug)
def outer(v): return tuple(tuple(v[i] * v[j] for j in range(4)) for i in range(4))
def matrix_T(w):
    cols = [scale(pair(BASIS[j], w), w) for j in range(4)]
    return tuple(tuple(cols[j][i] for j in range(4)) for i in range(4))
def beta(x): return tuple(F(ELL[x[i]]) for i in range(4))
def qkey(v):
    A = outer(v)
    return tuple(x for row in A for x in row)
def direct(v):
    w = v
    if w == ZERO:
        return ("ZERO_SUPPORT", F(0), (F(0), F(0)), "ZERO_DENOMINATOR", "ZERO_DENOMINATOR")
    m = pair(w, w)
    c = pair(w, LAMBDA) / LAM_NORM
    lo = scale(c, LAMBDA); hi = sub(w, lo)
    wl = pair(lo, lo); wh = pair(hi, hi)
    rho = mscale(1 / m, matrix_T(w))
    return ("SUPPORTED", m, (wl, wh), ("DENSITY", rho), ("NORMALIZED", (wl / m, wh / m)))


def main():
    G = tuple(tuple(pair(BASIS[i], BASIS[j]) for j in range(4)) for i in range(4))
    Ginv = minv(G)
    q_to_d = defaultdict(set)
    d_to_q = defaultdict(set)
    q_fibres = Counter()
    reconstruct_fail = 0
    density_only = set()

    for x in product(range(5), repeat=6):
        v = beta(x); qk = qkey(v); d = direct(v)
        q_to_d[qk].add(d); d_to_q[d].add(qk); q_fibres[qk] += 1
        if d[0] == "SUPPORTED":
            m = d[1]; rho = d[3][1]
            Arec = mmul(mscale(m, rho), Ginv)
            if tuple(y for row in Arec for y in row) != qk:
                reconstruct_fail += 1
            density_only.add(d[3])
        else:
            density_only.add(d[3])

    assert len(q_to_d) == 313
    assert len(d_to_q) == 313
    assert all(len(s) == 1 for s in q_to_d.values())
    assert all(len(s) == 1 for s in d_to_q.values())
    hist = Counter(q_fibres.values())
    assert hist == Counter({50: 312, 25: 1})
    assert reconstruct_fail == 0

    # h:C->Q for any reduced factor is forced pointwise by h(f(x))=q(x).
    # The finite audit records the quotient cardinality and equality partition.
    print("C-QDD-DIRECT-RECORD-QUOTIENT-1-N")
    print("STATUS NON-CANONICAL INCUBATION")
    print("R1 DIRECT_EQUALITY_IFF_Q_EQUALITY q_to_D_singleton=1 D_to_q_singleton=1 PASS")
    print(f"R2 CLASSES {len(q_to_d)} FIBRES 1x25+312x50 PASS")
    print(f"R3 Q_TO_RECORD_BIJECTION q={len(q_to_d)} records={len(d_to_q)} PASS")
    print("R4 TERMINAL_FACTOR_OBJECT written_universal_proof_required AUDIT_PARTITION_PASS")
    print("R5 MINIMAL_FACTOR_CARDINALITY 313 written_surjection_proof_required")
    print(f"CONTROL DENSITY_ONLY_CLASSES {len(density_only)} LESS_THAN_313={int(len(density_only) < 313)}")
    print("GUARD direct Route A dictionary fixed; no Born/effects/apparatus/physical D_matter/layer lift")
    print("RESULT candidate-T conditional_on_written_proof")

if __name__ == "__main__": main()
