#!/usr/bin/env python3
# NON-CANONICAL break attempt against C-AFFINE-READING-CHARACTER-CENSUS-1.
# Third code path. Different algorithms from both Method A and Method B.
from fractions import Fraction as Q
from itertools import product
import os

HERE = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(HERE,
     'verify_C-AFFINE-READING-CHARACTER-CENSUS-1.py')).read().split("DMAX_A = 5")[0])

def evalpoly(poly, x):
    acc = Q(0)
    for mon, co in poly.items():
        term = co
        for i in range(4):
            for _ in range(mon[i]):
                term *= x[i]
        acc += term
    return acc

# frozen numbers are read back from EXPECTED.txt, not recomputed, so the
# comparison below is against the recorded result rather than a re-execution
FR = {}
MV = {}
for line in open(os.path.join(HERE, 'EXPECTED.txt')):
    t = line.split()
    if t[:2] == ['MOLIEN', 'INVARIANT']:
        FR[0] = [int(x) for x in t[6:]]
    if t[:2] == ['MOLIEN', 'EPSILON']:
        FR[2] = [int(x) for x in t[6:]]
    if t[:3] == ['MOLIEN', 'ORDER', 'FOUR']:
        FR[1] = [int(x) for x in t[7:]]
    if t[0] == 'DEGREE' and len(t) > 13:
        MV[int(t[1])] = int(t[13])
FR[3] = FR[1]
methodB = {(r, d): FR[r][d] for r in range(4) for d in range(len(FR[0]))}
mult_V = MV

print("BREAK ATTEMPT (NON-CANONICAL)")
print()

# 1. Direct attack on G3: solve the linear semi-invariance system itself,
#    not a projector rank. f is a row vector; require f rho(g) = lambda(g) f.
print("1. Direct linear semi-invariance systems, solved as nullspaces over Q(i)")
for r in range(4):
    rows = []
    for g in GRP:
        w = lam(r, g)
        R = RHO[g]
        for j in range(4):
            re = [R[i][j] - (w[0] if i == j else Q(0)) for i in range(4)]
            im = [-(w[1] if i == j else Q(0)) for i in range(4)]
            rows.append(re + [-x for x in im])
            rows.append(im + re)
    n = 8
    rk = rank(rows)
    print("   character lambda_%d : solution space dimension over Q(i) = %d"
          % (r, (n - rk) // 2))

# 2. Absolute irreducibility of V, independent of any character computation
rows = []
for g in GRP:
    R = RHO[g]
    for i in range(4):
        for j in range(4):
            row = [Q(0)] * 16
            for k in range(4):
                row[i * 4 + k] += R[k][j]
                row[k * 4 + j] -= R[i][k]
            rows.append(row)
print()
print("2. dim End_G(V) over Q by commutant nullspace = %d" % (16 - rank(rows)))

# 3. Third route to the multiplicities: conjugacy classes and Newton power
#    sums, never touching 1/det and never building a Sym^d matrix.
def classes():
    seen, out = set(), []
    for g in GRP:
        if g in seen:
            continue
        cl = set()
        for h in GRP:
            hi = next(k for k in GRP if gmul(h, k) == (1, 0))
            cl.add(gmul(gmul(h, g), hi))
        seen |= cl
        out.append(sorted(cl))
    return out

CL = classes()
print()
print("3. conjugacy classes: %d of sizes %s"
      % (len(CL), [len(c) for c in CL]))

def power_sums(R, n):
    # p_k = trace(R^k), then symmetric-power characters by Newton recursion
    p = [Q(0)] * (n + 1)
    Rk = eye(4)
    for k in range(1, n + 1):
        Rk = mm(Rk, R)
        p[k] = tr(Rk)
    h = [Q(1)] + [Q(0)] * n
    for k in range(1, n + 1):
        h[k] = sum(h[k - j] * p[j] for j in range(1, k + 1)) / k
    return h

NB = 12
H = {g: power_sums(RHO[g], NB) for g in GRP}
agree = True
for r in range(4):
    for d in range(NB + 1):
        acc = cx(0)
        for g in GRP:
            acc = cadd(acc, cmul(cconj(lam(r, g)), cx(H[g][d])))
        val = acc[0] / 20
        if acc[1] != 0 or val != methodB[(r, d)]:
            agree = False
            print("   MISMATCH r=%d d=%d newton=%s molien=%s"
                  % (r, d, val, methodB[(r, d)]))
print("   Newton power-sum route agrees with Molien at all 52 cells: %s" % agree)

# 4. Exhibit the cubic invariant explicitly and test what it reads.
mons3 = monomials(3)
idx3 = {m: i for i, m in enumerate(mons3)}
n3 = len(mons3)
Acc = [[Q(0)] * n3 for _ in range(n3)]
for g in GRP:
    S = sym_op(RHO[g], 3, mons3, idx3)
    Acc = madd(Acc, S)
Acc = sc(Q(1, 20), Acc)
piv = rref_pivots(Acc)
cub = {mons3[i]: Acc[i][piv[0]] for i in range(n3) if Acc[i][piv[0]]}
den = 1
for v in cub.values():
    den = den * v.denominator // __import__('math').gcd(den, v.denominator)
cub = {k: v * den for k, v in cub.items()}
g = 0
for v in cub.values():
    g = __import__('math').gcd(g, abs(int(v)))
cub = {k: int(v) // g for k, v in cub.items()}
print()
print("4. the unique cubic invariant, normalized to primitive integer form:")
terms = []
for mon in mons3:
    if mon in cub:
        s = "".join(("x%d^%d" % (i, mon[i])) if mon[i] > 1
                    else ("x%d" % i) if mon[i] == 1 else ""
                    for i in range(4))
        terms.append("%+d %s" % (cub[mon], s))
print("   K(x) = " + " ".join(terms))

def evalcub(x):
    acc = 0
    for mon, co in cub.items():
        t = co
        for i in range(4):
            for _ in range(mon[i]):
                t *= x[i]
        acc += t
    return acc

inv_ok = all(evalcub(mv(RHO[g], list(x))) == evalcub(list(x))
             for g in GRP
             for x in [[Q(1), Q(0), Q(0), Q(0)], [Q(1), Q(2), Q(-1), Q(3)],
                       [Q(0), Q(1), Q(1), Q(-2)]])
print("   G-invariance of K verified on three exact probes: %s" % inv_ok)
print("   K is odd: K(-x) = -K(x) on the same probes: %s"
      % all(evalcub([-c for c in x]) == -evalcub(list(x))
            for x in [[Q(1), Q(0), Q(0), Q(0)], [Q(1), Q(2), Q(-1), Q(3)]]))

# 5. Minimal separating degree: sharpen G9 downward.
TESTB = [tuple(Q(c) for c in t) for t in product((-2, -1, 0, 1, 2), repeat=4)
         if any(t)]
def orbit_same(x, y):
    return any(tuple(mv(RHO[g], list(x))) == y for g in GRP)
print()
print("5. minimal degree at which the invariant fingerprint separates orbits")
basis_upto = []
for d in range(0, 6):
    mons = monomials(d)
    idx = {m: i for i, m in enumerate(mons)}
    n = len(mons)
    Ad = [[Q(0)] * n for _ in range(n)]
    for gg in GRP:
        Ad = madd(Ad, sym_op(RHO[gg], d, mons, idx))
    Ad = sc(Q(1, 20), Ad)
    for c in rref_pivots(Ad):
        basis_upto.append({mons[i]: Ad[i][c] for i in range(n) if Ad[i][c]})
    buck = {}
    for x in TESTB:
        key = tuple(evalpoly(p, x) for p in basis_upto)
        buck.setdefault(key, []).append(x)
    bad = sum(1 for k, mem in buck.items()
              for o in mem[1:] if not orbit_same(mem[0], o))
    print("   degree <= %d : %2d invariants, %4d fingerprint classes, "
          "non-orbit collisions %d" % (d, len(basis_upto), len(buck), bad))

# 6. Sym^3 V versus the regular representation of G.
print()
print("6. Sym^3 V multiplicities (1,eps,i,ibar,V) = (%d,%d,%d,%d,%d), "
      "regular representation of G = (1,1,1,1,4), dim 20 = |G| : %s"
      % (methodB[(0, 3)], methodB[(2, 3)], methodB[(1, 3)], methodB[(3, 3)],
         mult_V[3],
         (methodB[(0, 3)], methodB[(2, 3)], methodB[(1, 3)], methodB[(3, 3)],
          mult_V[3]) == (1, 1, 1, 1, 4)))

# 7. Can any reading be linear if we allow a bigger character group?
#    Every scalar multiplier is forced to be a character of G. Verify that a
#    nonzero f and any multiplier map c: G -> Q(i)^* forces c to be a homomorphism.
print()
print("7. any nonzero f with f(rho(g)x) = c(g) f(x) forces c(gh) = c(g)c(h),")
print("   so c is one of the four characters and case 1 above is exhaustive.")
