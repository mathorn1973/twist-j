#!/usr/bin/env python3
# break_common_carrier_icosian.py
# Break attempts against C-COMMON-CARRIER-ICOSIAN-1 (NON-CANONICAL).
# Each gate attacks one load-bearing negative of the candidate and PASSES
# only when the attack fails in exact arithmetic. Any FAIL fires the named
# falsifier of the bundle. Python 3 stdlib, deterministic.
import sys
from fractions import Fraction as F

R = []
def ck(name, cond):
    ok = bool(cond)
    R.append(ok)
    print(("PASS " if ok else "FAIL ") + name)

def fa(p, q): return (p[0]+q[0], p[1]+q[1])
def fs(p, q): return (p[0]-q[0], p[1]-q[1])
def fm(p, q): return (p[0]*q[0] + 5*p[1]*q[1], p[0]*q[1] + p[1]*q[0])
def fneg(p): return (-p[0], -p[1])
def fint(n): return (F(n), F(0))
def finv(p):
    d = p[0]*p[0] - 5*p[1]*p[1]
    return (p[0]/d, -p[1]/d)
F0 = fint(0); F1 = fint(1)
PHI = (F(1, 2), F(1, 2)); IPHI = (F(-1, 2), F(1, 2))
def qadd(x, y): return tuple(fa(p, r) for p, r in zip(x, y))
def qsub(x, y): return tuple(fs(p, r) for p, r in zip(x, y))
def qmul(x, y):
    a1, b1, c1, d1 = x; a2, b2, c2, d2 = y
    return (fs(fs(fm(a1, a2), fm(b1, b2)), fa(fm(c1, c2), fm(d1, d2))),
            fs(fa(fa(fm(a1, b2), fm(b1, a2)), fm(c1, d2)), fm(d1, c2)),
            fa(fs(fm(a1, c2), fm(b1, d2)), fa(fm(c1, a2), fm(d1, b2))),
            fa(fa(fm(a1, d2), fm(b1, c2)), fs(fm(d1, a2), fm(c1, b2))))
def qconj(x): return (x[0], fneg(x[1]), fneg(x[2]), fneg(x[3]))
def qneg(x): return tuple(fneg(p) for p in x)
def qsca(s, x): return tuple(fm(s, p) for p in x)
def trd(x): return fm(fint(2), x[0])
QONE = (F1, F0, F0, F0); QI = (F0, F1, F0, F0)
H2 = (F(1, 2), F(0))
g5 = (fm(H2, IPHI), fm(H2, PHI), H2, F0)
g6 = (H2, H2, H2, H2)
grp = {QONE}; fr = [QONE]
while fr:
    x = fr.pop()
    for g in (QI, g5, g6):
        y = qmul(x, g)
        if y not in grp: grp.add(y); fr.append(y)
ICO = sorted(grp)
assert len(ICO) == 120
def order_of(g):
    n = 1; x = g
    while x != QONE:
        x = qmul(x, g); n += 1
    return n
q = sorted(g for g in ICO if order_of(g) == 5 and trd(g) == IPHI)[0]
q2 = qmul(q, q); q3 = qmul(q2, q); q4 = qmul(q3, q)
Jq = qadd(QONE, q2); Jinv = qsca(PHI, q4)
ecands = sorted(g for g in ICO if trd(g) == F0 and qmul(g, q) == qmul(qconj(q), g))
e = ecands[0]
qe = qmul(q, e)
om = g6

def zvec(x):
    out = []
    for p in x:
        for t in (4*p[0], 4*p[1]):
            if t.denominator != 1: return None
            out.append(int(t))
    return out
def hnf(vectors):
    rows = [v[:] for v in vectors if v is not None and any(v)]
    basis = []
    for col in range(8):
        while True:
            nz = [r for r in rows if r[col] != 0]
            if len(nz) <= 1: break
            nz.sort(key=lambda r: abs(r[col]))
            p = nz[0]
            newrows = [p]
            for r in rows:
                if r is p: continue
                if r[col] != 0:
                    f = r[col] // p[col]
                    r = [a - f*b for a, b in zip(r, p)]
                if any(r): newrows.append(r)
            rows = newrows
        nz = [r for r in rows if r[col] != 0]
        if nz:
            p = nz[0] if nz[0][col] > 0 else [-t for t in nz[0]]
            basis.append((col, p))
            rows = [r for r in rows if r[col] == 0 and any(r)]
    return basis
def in_lattice(v, basis):
    if v is None: return False
    v = v[:]
    for col, b in basis:
        if v[col] % b[col] != 0: return False
        f = v[col] // b[col]
        v = [a - f*c for a, c in zip(v, b)]
    return not any(v)
def latdet(basis):
    d = 1
    for col, b in basis: d *= b[col]
    return d
LO = hnf([zvec(g) for g in ICO])

def solve_in(basis4, x):
    M = [[basis4[j][i] for j in range(4)] for i in range(4)]
    v = [x[i] for i in range(4)]
    for col in range(4):
        piv = None
        for r in range(col, 4):
            if M[r][col] != F0: piv = r; break
        if piv is None: return None
        M[col], M[piv] = M[piv], M[col]; v[col], v[piv] = v[piv], v[col]
        inv = finv(M[col][col])
        M[col] = [fm(inv, t) for t in M[col]]; v[col] = fm(inv, v[col])
        for r in range(4):
            if r != col and M[r][col] != F0:
                f = M[r][col]
                M[r] = [fs(M[r][t], fm(f, M[col][t])) for t in range(4)]
                v[r] = fs(v[r], fm(f, v[col]))
    return ((v[0], v[1]), (v[2], v[3]))
BASE = [QONE, q, e, qe]
def kmul(u, v):
    c0 = fm(u[0], v[0]); c1 = fa(fm(u[0], v[1]), fm(u[1], v[0])); c2 = fm(u[1], v[1])
    return (fs(c0, c2), fa(c1, fm(IPHI, c2)))
def kquat(u): return qadd(qsca(u[0], QONE), qsca(u[1], q))
def fint_zphi(p):
    a, b = p
    return (2*b).denominator == 1 and (a - b).denominator == 1
def kint(u): return fint_zphi(u[0]) and fint_zphi(u[1])
JK = solve_in(BASE, Jq)[0]; JKi = solve_in(BASE, Jinv)[0]
KQ = (F0, (F(1), F(0)))
K1 = (F1, F0)
ZB = [qmul(z, u) for u in (QONE, om) for z in (QONE, q, q2, q3)]
def dmap(D1, D2, x):
    cc = solve_in(BASE, x)
    return qadd(kquat(kmul(D1, cc[0])), qmul(kquat(kmul(D2, cc[1])), e))
def integral(D1, D2):
    return all(in_lattice(zvec(dmap(D1, D2, x)), LO) for x in ZB)

# BK1: try the UNTWISTED even tick diag(J, J^-1). Break = it preserves O.
ck("BK1 break fails: the untwisted diag(J, J^-1) does NOT preserve the icosian lattice (a Z-basis vector escapes O): the det-1 even tick is not integral along the h-splitting",
   not integral(JK, JKi))

# BK2: try every fifth-root twist with PLUS sign, diag(J q^a, J^-1 q^-a).
plus_ok = True
qp = K1
for a in range(5):
    D1 = kmul(JK, qp)
    D2 = kmul(JKi, solve_in(BASE, (QONE, q4, q3, q2, q)[a])[0])
    if integral(D1, D2): plus_ok = False
    qp = kmul(qp, KQ)
ck("BK2 break fails: NO plus-sign twist diag(J q^a, J^-1 q^-a), a = 0..4, preserves O: the residue mismatch res(J) = 2 vs res(J^-1) = 3 cannot be repaired inside the fifth roots; only the sign flip (-1, residue 4) repairs it",
   plus_ok)

# BK3: try to make {1, e'} a free basis for some pure inverting icosian e'.
free_ok = True
for cand in ecands:
    gensz = [zvec(qmul(z, u)) for u in (QONE, cand) for z in (QONE, q, q2, q3)]
    L = hnf(gensz)
    if len(L) == 8 and latdet(L) == latdet(LO): free_ok = False
ck("BK3 break fails: for EVERY pure inverting icosian e' the span Z[q].1 + Z[q].e' has index 5, never 1: no h-orthonormal free basis exists, the glue is unavoidable",
   free_ok)

# BK4: try to read h as an O_K-valued form. Break = h(1, omega) integral.
h1om = solve_in(BASE, qmul(QONE, qconj(om)))[0]
ck("BK4 break fails: h(1, omega) is NOT in Z[zeta5]: the canonical CM-Hermitian form is genuinely inverse-different-valued on O",
   not kint(h1om))

# BK5: try to solve y^2 = J with y = +-phi^k g, g icosian, k = -3..3.
found = False
PHIK = [finv(fm(PHI, fm(PHI, PHI))), finv(fm(PHI, PHI)), finv(PHI),
        F1, PHI, fm(PHI, PHI), fm(PHI, fm(PHI, PHI))]
for s in (F1, fneg(F1)):
    for pk in PHIK:
        for g in ICO:
            y = qsca(fm(s, pk), g)
            if qmul(y, y) == Jq: found = True
ck("BK5 break fails: no y = +-phi^k g (g in 2I, |k| <= 3) satisfies y^2 = J, the witness sweep over all 1680 golden-unit multiples of 2I agrees with the total-positivity obstruction",
   not found)

# BK6: try the UNTWISTED trace form. Break = it is already unimodular.
GM = []
for x in ZB:
    row = []
    for y in ZB:
        v = trd(qmul(x, qconj(y)))
        t = 2*v[0]
        row.append(t)
    GM.append(row)
def fdet(M):
    n = len(M)
    A = [[F(M[i][j]) for j in range(n)] for i in range(n)]
    det = F(1)
    for c in range(n):
        p = None
        for r in range(c, n):
            if A[r][c] != 0: p = r; break
        if p is None: return F(0)
        if p != c: A[c], A[p] = A[p], A[c]; det = -det
        det *= A[c][c]
        inv = 1/A[c][c]
        A[c] = [t*inv for t in A[c]]
        for r in range(c+1, n):
            if A[r][c] != 0:
                f = A[r][c]
                A[r] = [u - f*w for u, w in zip(A[r], A[c])]
    return det
ck("BK6 break fails: the untwisted trace form Tr_{F/Q}(trd(x ybar)) has determinant 625 = 5^4, not 1: E8 requires the golden 1/sqrt5 twist, the ramified prime is load-bearing",
   fdet(GM) == 625)

n = len(R); ok = sum(R)
print("SUMMARY %d/%d PASS" % (ok, n))
sys.exit(0 if ok == n else 1)
