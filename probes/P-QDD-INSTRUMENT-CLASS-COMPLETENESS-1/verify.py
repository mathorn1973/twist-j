#!/usr/bin/env python3
"""Exact audit for P-QDD-INSTRUMENT-CLASS-COMPLETENESS-1."""
from fractions import Fraction as F

BASE = "a25e2c640295962a7983f16d940347b2b7c1525e"
ISSUE = 515
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


def vvadd(v, w):
    return tuple(x + y for x, y in zip(v, w))


def vvsub(v, w):
    return tuple(x - y for x, y in zip(v, w))


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


def dot(v, g, w):
    gw = mv(g, w)
    return sum((x * y for x, y in zip(v, gw)), F(0))


I4 = I(4)
J4 = M([[1] * 4 for _ in range(4)])
G = sub(I4, sc(F(1, 5), J4))
GI = add(I4, J4)
MJ = M(((1, 0, -1, 1), (0, 1, -1, 0), (1, 0, 0, 0), (0, 1, -1, 1)))
DJ = sub(MJ, I4)
e0 = (F(1), F(0), F(0), F(0))
ONE = (F(1),) * 4


def sharp(a):
    return mul(GI, mul(T(a), G))


def projector(u):
    d = dot(u, G, u)
    return sc(F(1, 1) / d, outer(u, mv(G, u)))


def reflection(w):
    d = dot(w, G, w)
    return sub(I4, sc(F(2, 1) / d, outer(w, mv(G, w))))


U = [mv(pw(DJ, k), e0) for k in range(5)]

ck("A1 authority", BASE.startswith("a25e2c64") and ISSUE == 515)
ck("A2 Gram inverse", mul(G, GI) == I4 and mul(GI, G) == I4)
ck("A3 J motor", pw(DJ, 5) == I4 and mul(T(DJ), mul(G, DJ)) == G)
ck("A4 regular simplex", tuple(sum((U[k][i] for k in range(5)), F(0)) for i in range(4)) == (F(0),) * 4
   and all(dot(U[i], G, U[j]) == (F(4, 5) if i == j else F(-1, 5)) for i in range(5) for j in range(5)))

PS = []
QS = []
OS = []
KS = []
phase_ray_witnesses = []

projectors_ok = True
reflections_ok = True
effects_ok = True
support_ok = True
inequivalent_ok = True

for k in range(5):
    p = projector(U[k])
    q = sub(I4, p)
    w = vvsub(U[(k + 1) % 5], U[(k + 2) % 5])
    z = vvsub(U[(k + 3) % 5], U[(k + 4) % 5])
    o = reflection(w)
    kh = mul(o, q)

    projectors_ok = projectors_ok and (
        mul(p, p) == p and sharp(p) == p
        and mul(q, q) == q and sharp(q) == q
        and add(p, q) == I4 and mul(p, q) == Z(4) and mul(q, p) == Z(4)
    )
    reflections_ok = reflections_ok and (
        w != (F(0),) * 4 and dot(U[k], G, w) == 0
        and mul(sharp(o), o) == I4 and mul(o, o) == I4
        and mul(o, p) == p and mul(p, o) == p
        and mul(o, q) == mul(q, o)
    )
    effects_ok = effects_ok and (
        mul(sharp(p), p) == p
        and mul(sharp(q), q) == q
        and mul(sharp(kh), kh) == q
    )
    support_ok = support_ok and (
        mul(p, kh) == Z(4) and mul(kh, p) == Z(4)
        and mul(q, kh) == kh and mul(kh, q) == kh
    )
    v = vvadd(w, z)
    qv = mv(q, v)
    kv = mv(kh, v)
    ray_diff = outer(qv, qv) != outer(kv, kv)
    inequivalent_ok = inequivalent_ok and kh != q and kh != sc(-1, q) and ray_diff

    PS.append(p)
    QS.append(q)
    OS.append(o)
    KS.append(kh)
    phase_ray_witnesses.append(ray_diff)

ck("B1 five token projectors", projectors_ok)
ck("B2 five rational phase reflections", reflections_ok)
ck("B3 reflected branch exact effects", effects_ok)
ck("B4 reflected branch two-sided support", support_ok)
ck("B5 reflected branches are sign-inequivalent", inequivalent_ok and all(phase_ray_witnesses))

# Two-phase control at target-independent token k=0.
P0, Q0, KSTAR = PS[0], QS[0], KS[0]
low2 = [P0, P0]
high2 = [Q0, KSTAR]
tau2 = [1, 0]

ck("C1 two-phase exact effects", all(
    mul(sharp(low2[m]), low2[m]) == P0 and mul(sharp(high2[m]), high2[m]) == Q0
    for m in range(2)))
ck("C2 two-phase ordinary repeatability", all(
    mul(high2[tau2[m]], low2[m]) == Z(4)
    and mul(low2[tau2[m]], high2[m]) == Z(4)
    for m in range(2)))
ck("C3 two-phase ready isometry data", sorted(tau2) == [0, 1] and all(
    add(mul(sharp(low2[m]), low2[m]), mul(sharp(high2[m]), high2[m])) == I4
    for m in range(2)))
ck("C4 two-phase post-state phase nonselection", high2[0] != high2[1]
   and high2[0] != sc(-1, high2[1]))

# 256-phase cycle control. It audits the class at the memory scale exposed by O1,
# but imports no O1 sampler or denominator computation.
L256 = 256
tau256 = [(m + 1) % L256 for m in range(L256)]
low256 = [P0 for _ in range(L256)]
high256 = [Q0 for _ in range(L256)]
high256[-1] = KSTAR

ck("D1 256-phase update is permutation", len(set(tau256)) == L256 and min(tau256) == 0 and max(tau256) == 255)
ck("D2 256-phase exact effects", all(
    mul(sharp(low256[m]), low256[m]) == P0 and mul(sharp(high256[m]), high256[m]) == Q0
    for m in range(L256)))
ck("D3 256-phase ordinary repeatability", all(
    mul(high256[tau256[m]], low256[m]) == Z(4)
    and mul(low256[tau256[m]], high256[m]) == Z(4)
    for m in range(L256)))
ck("D4 256-phase law is not phase independent", len({high256[m] for m in range(L256)}) == 2
   and KSTAR != Q0 and KSTAR != sc(-1, Q0))

# Target comparison last.
ELOW = sc(F(1, 4), J4)
ck("E1 target comparison last", U[2] == tuple(-x for x in ONE) and PS[2] == ELOW and QS[2] == sub(I4, ELOW))

bad = 0
for label, ok in CHECKS:
    print(("PASS " if ok else "FAIL ") + label)
    bad += int(not ok)
print("CLASS finite_memory_pointwise=A_rep_fibres")
print("REALIZATION arbitrary_finite_phase_family=rational_ready_isometry")
print("PHASE two_and_256_phase_nonselection=YES")
print("ARCHITECTURE finite_memory_not_global_O2b_completion")
print("DECISION FINITE-MEMORY-FIBRE-BOUNDARY")
print("O2A UNTOUCHED")
print("O1 UNTOUCHED")
print("SAMPLING NOT PROVIDED")
print("RESULT %d/%d PASS" % (len(CHECKS) - bad, len(CHECKS)))
raise SystemExit(1 if bad else 0)
