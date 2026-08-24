#!/usr/bin/env python3
"""Exact audit for P-QDD-COMMUTATOR-SATURATION-CLOSURE-1."""
from fractions import Fraction as F
from itertools import product

BASE = "5e077db1a33924bbaaeb8498046605a21e1b0a0d"
ISSUE = 509
CHECKS = []


def ck(label, cond):
    CHECKS.append((label, bool(cond)))


def M(rows):
    return tuple(tuple(x if isinstance(x, F) else F(x) for x in row) for row in rows)


def I(n):
    return M([[int(i == j) for j in range(n)] for i in range(n)])


def Z(n, m=None):
    if m is None:
        m = n
    return M([[0 for _ in range(m)] for _ in range(n)])


def T(a):
    return tuple(tuple(a[j][i] for j in range(len(a))) for i in range(len(a[0])))


def add(a, b):
    return M([[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))])


def sc(c, a):
    c = F(c)
    return M([[c * x for x in row] for row in a])


def sub(a, b):
    return add(a, sc(-1, b))


def mul(a, b):
    bt = T(b)
    return M([[sum((x * y for x, y in zip(row, col)), F(0)) for col in bt] for row in a])


def mv(a, v):
    return tuple(sum((x * y for x, y in zip(row, v)), F(0)) for row in a)


def outer(v, w):
    return M([[x * y for y in w] for x in v])


def pw(a, n):
    r = I(len(a))
    b = a
    while n:
        if n & 1:
            r = mul(r, b)
        b = mul(b, b)
        n //= 2
    return r


def inv(a):
    n = len(a)
    w = [list(a[i]) + [F(i == j) for j in range(n)] for i in range(n)]
    for c in range(n):
        p = next(i for i in range(c, n) if w[i][c])
        w[c], w[p] = w[p], w[c]
        d = w[c][c]
        w[c] = [x / d for x in w[c]]
        for i in range(n):
            if i != c and w[i][c]:
                q = w[i][c]
                w[i] = [w[i][j] - q * w[c][j] for j in range(2 * n)]
    return tuple(tuple(w[i][n:]) for i in range(n))


def rk(a):
    w = [list(r) for r in a]
    m = len(w)
    n = len(w[0])
    r = 0
    for c in range(n):
        p = next((i for i in range(r, m) if w[i][c]), None)
        if p is None:
            continue
        w[r], w[p] = w[p], w[r]
        d = w[r][c]
        w[r] = [x / d for x in w[r]]
        for i in range(m):
            if i != r and w[i][c]:
                q = w[i][c]
                w[i] = [w[i][j] - q * w[r][j] for j in range(n)]
        r += 1
        if r == m:
            break
    return r


def det(a):
    w = [list(r) for r in a]
    n = len(w)
    out = F(1)
    sign = 1
    for c in range(n):
        p = next((i for i in range(c, n) if w[i][c]), None)
        if p is None:
            return F(0)
        if p != c:
            w[c], w[p] = w[p], w[c]
            sign = -sign
        d = w[c][c]
        out *= d
        for i in range(c + 1, n):
            if w[i][c]:
                q = w[i][c] / d
                for j in range(c, n):
                    w[i][j] -= q * w[c][j]
    return sign * out


def tr(a):
    return sum((a[i][i] for i in range(len(a))), F(0))


def dot(v, g, w):
    return sum((v[i] * sum((g[i][j] * w[j] for j in range(len(w))), F(0))
                for i in range(len(v))), F(0))


def sign_normal(v):
    for x in v:
        if x:
            return v if x > 0 else tuple(-y for y in v)
    return v


I4 = I(4)
J4 = M([[1] * 4 for _ in range(4)])
G = sub(I4, sc(F(1, 5), J4))
GI = add(I4, J4)
MJ = M(((1, 0, -1, 1), (0, 1, -1, 0), (1, 0, 0, 0), (0, 1, -1, 1)))
DJ = sub(MJ, I4)
e0 = (F(1), F(0), F(0), F(0))
u2 = mv(pw(DJ, 2), e0)
P = sc(F(1, 4), outer(u2, u2))
Q = sub(I4, P)
sharp4 = lambda a: mul(GI, mul(T(a), G))

B = M(((1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, -1, -1)))
L = M(((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0)))
H = mul(T(B), mul(G, B))
HI = inv(H)
A = mul(L, mul(Q, mul(DJ, B)))
I3 = I(3)
O_STAR = M(((-1, -1, -1), (0, 1, 0), (0, 0, 1)))


def lift(w):
    return mv(B, w)


def m4(v):
    return dot(v, G, v)


def rho4(v):
    return sc(F(1, 1) / m4(v), mul(outer(v, v), G))


def pure4(v):
    return (m4(v), rho4(v))


def branch4(o):
    return mul(B, mul(o, mul(L, Q)))


def centralizer(a, b, c):
    a, b, c = F(a), F(b), F(c)
    return M((
        (c - F(5, 4) * a, -a - F(1, 4) * b, -F(3, 4) * a + F(1, 4) * b),
        (-F(1, 4) * b, c - F(1, 4) * a - F(1, 2) * b, F(1, 4) * a - F(1, 4) * b),
        (a, b, c),
    ))


def orth_error(a, b, c):
    x = centralizer(a, b, c)
    return sub(mul(T(x), mul(H, x)), H)


ck("A1 authority", BASE.startswith("5e077db1") and ISSUE == 509)
ck("A2 Gram inverse", mul(G, GI) == I4)
ck("A3 motor", pw(DJ, 5) == I4 and mul(T(DJ), mul(G, DJ)) == G)
ck("A4 support", u2 == (F(-1),) * 4 and mul(P, P) == P and sharp4(P) == P and rk(P) == 1
   and mul(Q, Q) == Q and sharp4(Q) == Q and rk(Q) == 3 and add(P, Q) == I4)
ck("A5 W basis", H == M(((2, 1, 1), (1, 2, 1), (1, 1, 2))) and mul(L, B) == I3 and mul(Q, B) == B)
ck("A6 compressed motor", A == M(((-1, -1, F(-3, 4)), (0, 0, F(1, 4)), (1, 0, F(1, 4))))
   and det(A) == F(-1, 4) and tr(A) == F(-3, 4))

OS = (I3, sc(-1, I3), O_STAR)
ck("B1 representative branch equations", all(
    mul(sharp4(branch4(o)), branch4(o)) == Q
    and mul(Q, branch4(o)) == branch4(o)
    and mul(branch4(o), Q) == branch4(o)
    for o in OS))

GRID3 = [tuple(F(x) for x in t) for t in product(range(-2, 3), repeat=3) if any(t)]
VGRID = [lift(w) for w in GRID3]
ck("R1 pure record projector", all(
    mul(rho4(v), rho4(v)) == rho4(v)
    and sharp4(rho4(v)) == rho4(v)
    and rk(rho4(v)) == 1
    and tr(rho4(v)) == 1
    and mv(rho4(v), v) == v
    for v in VGRID))
ck("R2 reconstruction", all(mul(sc(m4(v), rho4(v)), GI) == outer(v, v) for v in VGRID))
SMALL = [lift(tuple(F(x) for x in t)) for t in product((-1, 0, 1), repeat=3) if any(t)]
ck("R3 sign fibres", all((pure4(v) == pure4(w)) == (sign_normal(v) == sign_normal(w)) for v in SMALL for w in SMALL))

COEFF = (-2, -1, 0, 1, 2)
ck("C1 centralizer formula", all(mul(centralizer(a, b, c), A) == mul(A, centralizer(a, b, c))
    for a, b, c in product(COEFF, repeat=3)))
ck("C2 eliminate b", all(orth_error(a, b, c)[1][1] - orth_error(a, b, c)[0][0] == F(5, 4) * F(b) * F(b)
    for a, b, c in product(COEFF, repeat=3)))
ck("C3 eliminate a", all(
    orth_error(a, 0, c)[0][0] - orth_error(a, 0, c)[2][2] == F(a) * (7 * F(a) - 8 * F(c)) / 4
    and orth_error(a, 0, c)[0][1] - orth_error(a, 0, c)[0][2] == F(a) * (F(a) - 4 * F(c)) / 2
    for a, c in product(range(-3, 4), repeat=2)))
ck("C4 signs only", all(orth_error(0, 0, c)[0][0] == 2 * (F(c) * F(c) - 1) for c in range(-4, 5))
   and centralizer(0, 0, 1) == I3 and centralizer(0, 0, -1) == sc(-1, I3))


def saturated(o):
    oa = mul(o, A)
    ao = mul(A, o)
    return all(pure4(lift(mv(oa, w))) == pure4(lift(mv(ao, w))) for w in GRID3)


ck("S1 sign representatives saturate", saturated(I3) and saturated(sc(-1, I3)))
XI = sub(mul(O_STAR, A), mul(A, O_STAR))
ck("S2 noncentral witness", mul(T(O_STAR), mul(H, O_STAR)) == H and pw(O_STAR, 2) == I3 and XI != Z(3) and rk(XI) == 2)
ck("S3 port detects witness", not saturated(O_STAR))

TPLUS = branch4(I3)
TMINUS = branch4(sc(-1, I3))
TSTAR = branch4(O_STAR)
ck("I1 sign representatives projectively idempotent", mul(TPLUS, TPLUS) == TPLUS and mul(TMINUS, TMINUS) == sc(-1, TMINUS))
ck("I2 witness not projectively idempotent", mul(TSTAR, TSTAR) == Q and TSTAR != Q and TSTAR != sc(-1, Q)
   and mul(TSTAR, TSTAR) != TSTAR and mul(TSTAR, TSTAR) != sc(-1, TSTAR))

ELOW = sc(F(1, 4), J4)
ck("T1 target comparison last", P == ELOW and Q == sub(I4, ELOW))

bad = 0
for label, ok in CHECKS:
    print(("PASS " if ok else "FAIL ") + label)
    bad += int(not ok)
print("CLASS repeatable_pure=O(W,H)_times_Q")
print("SATURATION COMM-SAT=Xi_zero=sign_class=projective_idempotence")
print("ARCHITECTURE current_contract_does_not_derive_COMM-SAT")
print("DICTIONARY terminal_event_commutator_saturation=UNADOPTED")
print("DECISION SATURATION-DICTIONARY-BOUNDARY")
print("SAMPLING NOT PROVIDED")
print("RESULT %d/%d PASS" % (len(CHECKS) - bad, len(CHECKS)))
raise SystemExit(1 if bad else 0)
