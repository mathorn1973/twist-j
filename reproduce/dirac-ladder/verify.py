#!/usr/bin/env python3
# TWIST-J Dirac ladder witness. Exact arithmetic only: integers,
# rationals, Q(sqrt5) pairs, Gaussian integers, and Laurent
# polynomials over Z[i]. Standard library only, no floats anywhere.
#
# The ladder: u = 2 phi^n and v = 2 phi^-n on the light cone
# u v = 4 = m^2; the spinor floor N(phi) = -1; the ladder root
# Fm = [[1,1],[1,0]] whose square is the Arnold cat map, tied over Z
# to the modulus carrier and mod 5 to the 1-jet of the J-carrier;
# the Dirac step D_J(m)(z) = S(z)(I + i m X) with zero free
# parameters, det = 1 + m^2 = 5 = p for the electron, and the exact
# mass shell; the ladder Z_2 (conductor 5) and the spin Z_2
# (conductor 8) distinct; the checkerboard between the rungs a
# Gaussian tower (1 + 2i)^n with c^2 + d^2 = 5^n; the fermionizer
# Phi_f(s) = 1 - 2^(1-s); one beat = one boost times one alternator
# tick; the alternator is breath at one scale and Thue-Morse at
# every scale.
#
# Claims verified: DIRAC-LADDER, LADDER-LIGHTCONE, SPINOR-FLOOR,
# FIB-ROOT-TIES, FIB-ROOT-CARRIER, DIRAC-STEP-THEOREMS, DIRAC-STEP,
# LADDER-SPIN-PLACES, CHECKERBOARD-GAUSS-TOWER, FERMIONIZER,
# LADDER-ALTERNATOR-BASIS, TM-BREATH-TOWER.

import sys
from fractions import Fraction as Fr
from itertools import product
from math import comb, gcd, isqrt

CHECKS = []


def check(tag, description, ok):
    CHECKS.append(("%-12s %s" % (tag, description), bool(ok)))


# ------------------------------------------------ Q(sqrt5): a + b sqrt5
def q5(a, b=0):
    return (Fr(a), Fr(b))


Q5_ONE = q5(1)
PHI = (Fr(1, 2), Fr(1, 2))
PSI = (Fr(1, 2), Fr(-1, 2))


def q5_add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def q5_sub(x, y):
    return (x[0] - y[0], x[1] - y[1])


def q5_mul(x, y):
    return (x[0] * y[0] + 5 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def q5_scal(c, x):
    return (Fr(c) * x[0], Fr(c) * x[1])


def q5_conj(x):
    return (x[0], -x[1])


def q5_norm(x):
    return x[0] * x[0] - 5 * x[1] * x[1]


def q5_pow(x, n):
    if n < 0:
        nx = q5_norm(x)
        x = (q5_conj(x)[0] / nx, q5_conj(x)[1] / nx)
        n = -n
    r = Q5_ONE
    for _ in range(n):
        r = q5_mul(r, x)
    return r


# ------------------------------------------------ integer matrices
def mat_id(n):
    return tuple(tuple(1 if i == j else 0 for j in range(n))
                 for i in range(n))


def mat_mul(A, B, mod=None):
    n = len(A)
    rows = []
    for i in range(n):
        row = []
        for j in range(n):
            v = sum(A[i][k] * B[k][j] for k in range(n))
            row.append(v % mod if mod else v)
        rows.append(tuple(row))
    return tuple(rows)


def mat_pow(A, e, mod=None):
    R = mat_id(len(A))
    if mod:
        R = tuple(tuple(x % mod for x in row) for row in R)
    for _ in range(e):
        R = mat_mul(R, A, mod)
    return R


def mat_scal(c, A):
    return tuple(tuple(c * x for x in row) for row in A)


def mat_add(A, B):
    return tuple(tuple(x + y for x, y in zip(r, s)) for r, s in zip(A, B))


def mat_sub(A, B):
    return tuple(tuple(x - y for x, y in zip(r, s)) for r, s in zip(A, B))


def mat_mod(A, mod):
    return tuple(tuple(x % mod for x in row) for row in A)


def mat_order(A, mod, bound):
    I = mat_id(len(A))
    R = mat_mod(A, mod)
    for k in range(1, bound + 1):
        if R == I:
            return k
        R = mat_mul(R, A, mod)
    return 0


def mat_rank(A, p):
    M = [list(row) for row in mat_mod(A, p)]
    n = len(M)
    rank = 0
    col = 0
    while rank < n and col < n:
        piv = next((r for r in range(rank, n) if M[r][col] % p), None)
        if piv is None:
            col += 1
            continue
        M[rank], M[piv] = M[piv], M[rank]
        inv = pow(M[rank][col], -1, p)
        M[rank] = [(inv * x) % p for x in M[rank]]
        for r in range(n):
            if r != rank and M[r][col]:
                f = M[r][col]
                M[r] = [(x - f * y) % p for x, y in zip(M[r], M[rank])]
        rank += 1
        col += 1
    return rank


def m2_det(A):
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]


def m2_charpoly(A):
    return (1, -(A[0][0] + A[1][1]), m2_det(A))


def charpoly_faddeev(A):
    n = len(A)
    Af = tuple(tuple(Fr(x) for x in row) for row in A)
    M = Af
    cs = []
    for k in range(1, n + 1):
        ck = sum(M[i][i] for i in range(n)) / k
        cs.append(ck)
        if k < n:
            Mk = tuple(tuple(M[i][j] - (ck if i == j else 0)
                             for j in range(n)) for i in range(n))
            M = mat_mul(Af, Mk)
    return (Fr(1),) + tuple(-c for c in cs)


# ------------------------------------------------ Gaussian integers
def gi_add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def gi_mul(x, y):
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def gi_conj(x):
    return (x[0], -x[1])


def gi_pow(x, e):
    r = (1, 0)
    for _ in range(e):
        r = gi_mul(r, x)
    return r


def gm2_mul(A, B):
    return tuple(tuple(gi_add(gi_mul(A[i][0], B[0][j]),
                              gi_mul(A[i][1], B[1][j]))
                       for j in range(2)) for i in range(2))


# ------------------------------------------------ Laurent over Z[i]
def lp(d):
    return {e: c for e, c in d.items() if c != (0, 0)}


def lp_add(pq, qq):
    r = dict(pq)
    for e, c in qq.items():
        r[e] = gi_add(r.get(e, (0, 0)), c)
    return lp(r)


def lp_neg(pq):
    return {e: (-c[0], -c[1]) for e, c in pq.items()}


def lp_sub(pq, qq):
    return lp_add(pq, lp_neg(qq))


def lp_scal(g, pq):
    return lp({e: gi_mul(g, c) for e, c in pq.items()})


def lp_mul(pq, qq):
    r = {}
    for e1, c1 in pq.items():
        for e2, c2 in qq.items():
            e = e1 + e2
            r[e] = gi_add(r.get(e, (0, 0)), gi_mul(c1, c2))
    return lp(r)


IPOW = ((1, 0), (0, 1), (-1, 0), (0, -1))


def lp_eval_i(pq):
    r = (0, 0)
    for e, c in pq.items():
        r = gi_add(r, gi_mul(c, IPOW[e % 4]))
    return r


def lm_mul(A, B):
    return [[lp_add(lp_mul(A[i][0], B[0][j]), lp_mul(A[i][1], B[1][j]))
             for j in range(2)] for i in range(2)]


def lm_sub(A, B):
    return [[lp_sub(A[i][j], B[i][j]) for j in range(2)] for i in range(2)]


def lm_eq(A, B):
    return all(lp(A[i][j]) == lp(B[i][j]) for i in range(2)
               for j in range(2))


def fib_lucas(nmax):
    F = [0, 1]
    L = [2, 1]
    for _ in range(2, nmax + 1):
        F.append(F[-1] + F[-2])
        L.append(L[-1] + L[-2])
    return F, L


def paths(n, s0):
    tal = {}
    for seq in product((0, 1), repeat=n):
        a = seq.count(0)
        R = (1 if seq[0] != s0 else 0) + \
            sum(1 for j in range(1, n) if seq[j] != seq[j - 1])
        key = (a, R, seq[-1])
        tal[key] = tal.get(key, 0) + 1
    return tal


def bpair(nn, kk):
    if kk == -1:
        return 1 if nn == -1 else 0
    if kk < -1 or nn < 0 or kk > nn:
        return 0
    return comb(nn, kk)


def nform(n, a, R, s0, s):
    if s0 == 1:
        return nform(n, n - a, R, 0, 1 - s)
    b = n - a
    if s == 0:
        if R % 2:
            return 0
        r = R // 2
        return bpair(a, r) * bpair(b - 1, r - 1)
    if R % 2 == 0:
        return 0
    r = (R + 1) // 2
    return bpair(a, r - 1) * bpair(b - 1, r - 1)


def chi5(n):
    r = n % 5
    if r == 0:
        return 0
    return 1 if r in (1, 4) else -1


def chi8(n):
    r = n % 8
    if r in (1, 7):
        return 1
    if r in (3, 5):
        return -1
    return 0


def phif(s):
    return 1 - Fr(2) ** (1 - s)


def main():
    F, L = fib_lucas(220)

    # ---------------------------------------------- 01 the light cone
    ok = True
    for n in range(0, 61):
        u = q5_scal(2, q5_pow(PHI, n))
        v = q5_scal(2, q5_pow(PHI, -n))
        ok &= q5_mul(u, v) == q5(4)
        ok &= q5_mul(PHI, u) == q5_scal(2, q5_pow(PHI, n + 1))
        ok &= q5_mul(q5_pow(PHI, -1), v) == q5_scal(2, q5_pow(PHI, -n - 1))
        ok &= q5_conj(u) == q5_scal((-1) ** n, v)
        ok &= u == (Fr(L[n]), Fr(F[n]))
    for n in range(0, 201):
        ok &= L[n] * L[n] - 5 * F[n] * F[n] == 4 * (-1) ** n
    check("LIGHTCONE",
          "u = 2 phi^n, v = 2 phi^-n: u v = 4 exactly, one tick is"
          " u -> phi u and v -> v / phi, conjugation swaps the legs with"
          " sign (-1)^n (n <= 60); 2 phi^n = L_n + sqrt5 F_n and"
          " L^2 - 5 F^2 = 4 (-1)^n (n <= 200)", ok)

    # ---------------------------------------------- 02 the spinor floor
    ok = q5_norm(PHI) == -1
    for n in range(0, 21):
        ok &= q5_norm(q5_pow(PHI, n)) == (-1) ** n
    for k in range(1, 9):
        ok &= q5_mul(q5_pow(PHI, k), q5_pow(PHI, k)) == q5_pow(PHI, 2 * k)
    # x^4 - x^2 - 1, the minimal polynomial of sqrt(phi), is irreducible
    # over Q: no integer root (candidates +-1), and an integer quadratic
    # split (x^2 + a x + b)(x^2 - a x + d) needs b d = -1, so b + d = 0,
    # then b + d - a^2 = -1 forces a^2 = 1 while the x-coefficient
    # a (d - b) = +-2 a must vanish: contradiction.  Hence sqrt(phi) has
    # degree 4 over Q and does not lie in the quadratic field Q(sqrt5).
    ok &= all(r ** 4 - r ** 2 - 1 != 0 for r in (1, -1))
    ok &= not [(a, b, d) for a in range(-2, 3)
               for (b, d) in ((1, -1), (-1, 1))
               if b + d - a * a == -1 and a * (d - b) == 0]
    # rung three: phi^3 = 2 + sqrt5; a square x + y sqrt5 with
    # (x + y sqrt5)^2 = 2 + sqrt5 needs 2 x y = 1 and x^2 + 5 y^2 = 2,
    # hence 4 t^2 - 8 t + 5 = 0 at t = x^2, discriminant -16 < 0.
    ok &= q5_pow(PHI, 3) == q5(2, 1)
    ok &= 8 * 8 - 4 * 4 * 5 == -16
    check("SPINOR-FLOOR",
          "N(phi) = -1; the alternator is N(phi^n) = (-1)^n; even rungs"
          " halve inside Q(sqrt5); odd rungs do not: x^4 - x^2 - 1 is"
          " irreducible over Q and phi^3 = 2 + sqrt5 is not a square in"
          " Q(sqrt5)", ok)

    # ---------------------------------------------- 03 the ladder root
    FM = ((1, 1), (1, 0))
    CAT = ((2, 1), (1, 1))
    BMOD = ((2, -1), (-1, 1))
    PD = ((1, 0), (0, -1))
    ok = m2_det(FM) == -1 == q5_norm(PHI)
    ok &= mat_mul(FM, FM) == CAT
    ok &= mat_mul(mat_mul(PD, CAT), PD) == BMOD
    ok &= m2_charpoly(FM) == (1, -1, -1)
    ok &= m2_charpoly(CAT) == (1, -3, 1) == m2_charpoly(BMOD)
    ok &= q5_mul(PHI, PHI) == q5_add(PHI, Q5_ONE)
    phi2 = q5_mul(PHI, PHI)
    ok &= q5_sub(q5_mul(phi2, phi2), q5_scal(3, phi2)) == q5(-1)
    Ac = FM
    for n in range(1, 31):
        ok &= Ac == ((F[n + 1], F[n]), (F[n], F[n - 1]))
        ok &= m2_det(Ac) == (-1) ** n and Ac[0][0] + Ac[1][1] == L[n]
        Ac = mat_mul(Ac, FM)
    check("FIB-ROOT",
          "det Fm = -1 = N(phi); Fm^2 = [[2,1],[1,1]] the cat map,"
          " P-conjugate over Z to the modulus carrier [[2,-1],[-1,1]]"
          " with P = diag(1,-1); x^2 - x - 1 squares onto the boost"
          " polynomial x^2 - 3x + 1; Fibonacci powers carry Cassini det"
          " (-1)^n and Lucas trace (n <= 30)", ok)

    # ---------------------------------------------- 04 the mod 5 towers
    MJ = ((1, 0, -1, 1),
          (0, 1, -1, 0),
          (1, 0, 0, 0),
          (0, 1, -1, 1))
    NEG2 = ((4, 0), (0, 4))
    NEG4 = ((4, 0, 0, 0), (0, 4, 0, 0), (0, 0, 4, 0), (0, 0, 0, 4))
    ok = mat_order(FM, 5, 25) == 20 and mat_pow(FM, 10, 5) == NEG2
    ok &= mat_order(CAT, 5, 25) == 10 and mat_pow(CAT, 5, 5) == NEG2
    ok &= mat_order(BMOD, 5, 25) == 10 and mat_pow(BMOD, 5, 5) == NEG2
    ok &= mat_order(MJ, 5, 25) == 20 and mat_pow(MJ, 10, 5) == NEG4
    check("TOWERS",
          "mod 5 the towers close: ord(Fm) = 20 = 4p with Fm^10 = -I;"
          " ord(Fm^2) = 10 = 2p with (Fm^2)^5 = -I; the modulus carrier"
          " closes at 10 with -I at 5; ord(M_J) = 20 with M_J^10 = -I:"
          " -I sits at half period on every member", ok)

    # ---------------------------------------------- 05 the 1-jet tie
    cp = charpoly_faddeev(MJ)
    ok = cp == (1, -3, 4, -2, 1)
    M2_ = mat_mul(MJ, MJ)
    M3_ = mat_mul(M2_, MJ)
    M4_ = mat_mul(M3_, MJ)
    CH = mat_add(mat_sub(mat_add(mat_sub(M4_, mat_scal(3, M3_)),
                                 mat_scal(4, M2_)), mat_scal(2, MJ)),
                 mat_id(4))
    ok &= CH == tuple(tuple(0 for _ in range(4)) for _ in range(4))
    ok &= tuple(c % 5 for c in cp) == (1, 2, 4, 3, 1)
    ok &= tuple(c % 5 for c in (1, -8, 24, -32, 16)) == (1, 2, 4, 3, 1)
    MJ2 = mat_sub(MJ, mat_scal(2, mat_id(4)))
    ranks = [mat_rank(mat_pow(MJ2, k), 5) for k in (1, 2, 3, 4)]
    ok &= ranks == [3, 2, 1, 0]
    ok &= (2 * 3) % 5 == 1 and (2 * 2) % 5 == 4 and (3 * 3) % 5 == 4
    FM3 = mat_sub(FM, mat_scal(3, mat_id(2)))
    ok &= mat_rank(FM3, 5) == 1
    JET = ((2, 0), (2, 2))
    JETINV = ((3, 0), (2, 3))
    ok &= mat_mul(JET, JETINV, 5) == mat_id(2)
    gfound = None
    for a, b, c, d in product(range(5), repeat=4):
        if (a * d - b * c) % 5 == 0:
            continue
        g = ((a, b), (c, d))
        if mat_mul(g, FM, 5) == mat_mul(JETINV, g, 5):
            gfound = g
            break
    ok &= gfound is not None
    check("JET",
          "charpoly(M_J) = x^4 - 3x^3 + 4x^2 - 2x + 1, confirmed by"
          " Cayley-Hamilton over Z; mod 5 it is (x - 2)^4 with ranks of"
          " (M_J - 2I)^k equal to 3, 2, 1, 0: one Jordan block J_4(2);"
          " residues J = 2 and J^-1 = 3, the two square roots of -1; an"
          " explicit g in GL_2(F_5) conjugates Fm to the 1-jet"
          " [[3,0],[2,3]]", ok)

    # ---------------------------------------------- 06 the step form
    S = [[{-1: (1, 0)}, {}], [{}, {1: (1, 0)}]]
    X = [[{}, {0: (1, 0)}], [{0: (1, 0)}, {}]]
    K2 = [[{0: (1, 0)}, {0: (0, 2)}], [{0: (0, 2)}, {0: (1, 0)}]]
    U_E = lm_mul(S, K2)
    U_P = S
    ok = lm_eq(U_E, [[{-1: (1, 0)}, {-1: (0, 2)}],
                     [{1: (0, 2)}, {1: (1, 0)}]])
    coeffs = set()
    for row in U_E:
        for ent in row:
            coeffs.update(ent.values())
    ok &= coeffs == {(1, 0), (0, 2)}
    ok &= lm_eq(U_P, [[{-1: (1, 0)}, {}], [{}, {1: (1, 0)}]])
    SX = lm_mul(S, X)
    ok &= lm_eq(lm_sub(U_E, U_P),
                [[lp_scal((0, 2), SX[i][j]) for j in range(2)]
                 for i in range(2)])
    ok &= lp(SX[0][0]) == {} and lp(SX[1][1]) == {}
    check("STEP-FORM",
          "D_J(m)(z) = S(z)(I + i m X) has entries {z^-1, i m z^-1,"
          " i m z, z} with coefficient set {1, i m}: no continuous"
          " parameter; massless is the one sided shift diag(z^-1, z);"
          " the mass insertion i m S X is purely off diagonal", ok)

    # ---------------------------------------------- 07 the invariants
    tr_E = lp_add(U_E[0][0], U_E[1][1])
    tr_P = lp_add(U_P[0][0], U_P[1][1])
    ZM = {1: (1, 0), -1: (-1, 0)}
    ok = tr_E == lp({-1: (1, 0), 1: (1, 0)}) == tr_P
    det_E = lp_sub(lp_mul(U_E[0][0], U_E[1][1]),
                   lp_mul(U_E[0][1], U_E[1][0]))
    det_P = lp_sub(lp_mul(U_P[0][0], U_P[1][1]),
                   lp_mul(U_P[0][1], U_P[1][0]))
    ok &= det_E == {0: (5, 0)} and det_P == {0: (1, 0)}
    disc_E = lp_sub(lp_mul(tr_E, tr_E), lp_scal((4, 0), det_E))
    disc_P = lp_sub(lp_mul(tr_P, tr_P), lp_scal((4, 0), det_P))
    ok &= disc_E == lp_sub(lp_mul(ZM, ZM), {0: (16, 0)})
    check("INVARIANTS",
          "trace = z + z^-1, mass free; det = 1 + m^2, momentum free:"
          " electron det = 5 = p, photon det = 1; disc = (z - z^-1)^2"
          " - 4 m^2 as an exact Laurent identity", ok)

    # ---------------------------------------------- 08 the mass shell
    ok = lp_sub(lp_mul(ZM, ZM), disc_E) == {0: (16, 0)}
    ok &= lp_sub(lp_mul(ZM, ZM), disc_P) == {}
    ok &= sum(c[0] for c in disc_E.values()) == -16
    ok &= all(c[1] == 0 for c in disc_E.values())
    ok &= lp_eval_i(disc_E) == (-20, 0)
    check("MASS-SHELL",
          "Ehat^2 - phat^2 = m^2 exactly for every z, as the Laurent"
          " identity (z - z^-1)^2 - disc = 4 m^2; the photon closes the"
          " light cone at m = 0; the band reads Ehat^2 = 4 = u v at"
          " z = 1 and Ehat^2 = 5 = det = p at z = i", ok)

    # ---------------------------------------------- 09 the rest coin
    KG = (((1, 0), (0, 2)), ((0, 2), (1, 0)))
    ok = gi_add(KG[0][0], KG[1][1]) == (2, 0)
    ok &= gi_add((1, 2), (1, -2)) == (2, 0)
    ok &= gi_mul((1, 2), (1, -2)) == (5, 0)
    lam = (1, 2)
    lam_poly = gi_add(gi_add(gi_mul(lam, lam), gi_mul((-2, 0), lam)),
                      (5, 0))
    ok &= lam_poly == (0, 0)
    K2G = gm2_mul(KG, KG)
    ok &= K2G == (((-3, 0), (0, 4)), ((0, 4), (-3, 0)))
    ok &= (-3) ** 2 + 4 ** 2 == 25 == 5 ** 2
    z0 = (Fr(-3, 5), Fr(4, 5))
    ok &= z0[0] * z0[0] + z0[1] * z0[1] == 1
    ok &= (2 * z0[0]).denominator != 1
    roots = [(a, b) for a in (-1, 0, 1) for b in (-1, 0, 1)
             if a * a + b * b == 1]
    ok &= sorted(roots) == [(-1, 0), (0, -1), (0, 1), (1, 0)]
    ok &= all(z0 != (Fr(a), Fr(b)) for (a, b) in roots)
    check("REST-COIN",
          "the rest coin I + 2iX: trace 2 = L_0, eigenvalues 1 +- 2i"
          " with sum 2 and product 5, charpoly x^2 - 2x + 5;"
          " (I + 2iX)^2 = -3I + 4iX on the 3-4-5 triple; (-3 + 4i)/5 is"
          " not an algebraic integer and the only roots of unity in Q(i)"
          " are 1, -1, i, -i: the unitarized rest coin has infinite"
          " order", ok)

    # ---------------------------------------------- 10 the two places
    ok = chi5(7) == -1 and chi8(7) == 1
    ok &= chi5(23) == -1 and chi8(23) == 1
    ok &= gcd(5, 8) == 1
    ok &= all(isqrt(n) ** 2 != n for n in (2, 5, 10))
    check("PLACES",
          "chi5 (conductor 5, the sqrt5 place) and chi8 (conductor 8,"
          " the sqrt2 place) differ at the witnesses 7 and 23;"
          " gcd(5, 8) = 1 and none of 2, 5, 10 is a square, so sqrt2 is"
          " not in Q(sqrt5): the ladder Z_2 and the spin Z_2 are"
          " distinct place attached Galois involutions", ok)

    # ---------------------------------------------- 11 the place swap
    ok = gi_mul((2, 1), (2, -1)) == (5, 0)
    ok &= gi_mul((2, 1), (-1, 1)) == (-3, 1)
    ok &= gi_mul((2, -1), (-1, 0)) == (-2, 1)
    ok &= gi_conj((2, 1)) == (2, -1) and gi_conj((1, 2)) == (1, -2)
    ok &= m2_det(FM) == -1 == q5_norm(PHI)
    ok &= gi_mul((1, 2), (1, -2)) == (5, 0)
    check("PLACE-SWAP",
          "5 = (2 + i)(2 - i) in Z[i]; i = 3 mod (2 + i) and i = 2 mod"
          " (2 - i): the inverse fourth root datum is a place choice;"
          " conjugation swaps the primes above 5 and the rest"
          " eigenvalues 1 +- 2i: charge conjugation is the place swap;"
          " det family: boost -1 = N(phi), photon 1, electron"
          " 5 = N(1 + 2i)", ok)

    # ---------------------------------------------- 12 the skeleton
    ok = True
    for n in range(1, 11):
        for s0 in (0, 1):
            tal = paths(n, s0)
            ok &= all((R % 2) == (0 if s == s0 else 1)
                      for (a, R, s) in tal)
            for a in range(n + 1):
                for R in range(n + 1):
                    for s in (0, 1):
                        ok &= nform(n, a, R, s0, s) == \
                            tal.get((a, R, s), 0)
            byR = {}
            for (a, R, s), c in tal.items():
                byR[R] = byR.get(R, 0) + c
            ok &= byR == {R: comb(n, R) for R in range(n + 1)}
    check("SKELETON",
          "the reversal parity law R = [s != s0] mod 2 on every path;"
          " one binomial pair per case equals the exhaustive census"
          " (n <= 10, both starts); the transition census is C(n, R),"
          " so the sum of t^R over paths is (1 + t)^n exactly", ok)

    # ---------------------------------------------- 13 the Gauss tower
    ok = True
    for n in range(1, 9):
        for s0 in (0, 1):
            tot, same, cross = (0, 0), (0, 0), (0, 0)
            for (a, R, s), c in paths(n, s0).items():
                w = gi_mul((c, 0), gi_pow((0, 2), R))
                tot = gi_add(tot, w)
                if s == s0:
                    same = gi_add(same, w)
                else:
                    cross = gi_add(cross, w)
            g = gi_pow((1, 2), n)
            ok &= tot == g
            ok &= same == (g[0], 0) and cross == (0, g[1])
    cs, ds = [1], [0]
    gp = (1, 0)
    for n in range(1, 21):
        gp = gi_mul(gp, (1, 2))
        cs.append(gp[0])
        ds.append(gp[1])
    for n in range(0, 21):
        ok &= cs[n] * cs[n] + ds[n] * ds[n] == 5 ** n
    for n in range(1, 20):
        ok &= cs[n + 1] == 2 * cs[n] - 5 * cs[n - 1]
        ok &= ds[n + 1] == 2 * ds[n] - 5 * ds[n - 1]
    UEi = tuple(tuple(lp_eval_i(U_E[i][j]) for j in range(2))
                for i in range(2))
    UPi = tuple(tuple(lp_eval_i(U_P[i][j]) for j in range(2))
                for i in range(2))
    ok &= gm2_mul(UEi, UEi) == (((-5, 0), (0, 0)), ((0, 0), (-5, 0)))
    ok &= gm2_mul(UPi, UPi) == (((-1, 0), (0, 0)), ((0, 0), (-1, 0)))
    check("GAUSS-TOWER",
          "the totals are (1 + 2i)^n with the diagonal in Z and the"
          " cross in iZ (n <= 8, both starts); the tower obeys"
          " x^2 - 2x + 5 with c^2 + d^2 = 5^n (n <= 20); zone edges at"
          " z = i: the electron step squares to -5I, the photon step"
          " to -I", ok)

    # ---------------------------------------------- 14 the fermionizer
    ok = phif(0) == -1 and phif(1) == 0 and phif(2) == Fr(1, 2)
    for s in (2, 4, 6, 8, 10):
        ok &= phif(s) == Fr(2 ** (s - 1) - 1, 2 ** (s - 1))
    ok &= phif(-5) == -63 == -(2 ** 6 - 1)
    zeta_m5 = -Fr(1, 6) * Fr(1, 42)
    ok &= zeta_m5 == Fr(-1, 252)
    ok &= phif(-5) * zeta_m5 == Fr(1, 4)
    check("FERMIONIZER",
          "Phi_f(s) = 1 - 2^(1-s): the bit Phi_f(1) = 0, the duty cycle"
          " Phi_f(2) = 1/2, the stalemate Phi_f(0) = -1, the Mersenne"
          " form (2^(s-1) - 1)/2^(s-1) at even s; Phi_f(-5) = -63 ="
          " -(2^6 - 1); zeta(-5) = -1/252 and eta(-5) ="
          " Phi_f(-5) zeta(-5) = 1/4", ok)

    # ---------------------------------------------- 15 the beat
    STEP = (PHI, PSI)
    BJ = (PHI, q5_sub(q5(0), PSI))
    ALT = (q5(1), q5(-1))
    ok = q5_mul(BJ[1], PHI) == Q5_ONE
    ok &= (q5_mul(BJ[0], ALT[0]), q5_mul(BJ[1], ALT[1])) == STEP
    ok &= (q5_mul(ALT[0], BJ[0]), q5_mul(ALT[1], BJ[1])) == STEP
    ok &= (q5_mul(ALT[0], ALT[0]), q5_mul(ALT[1], ALT[1])) == \
        (Q5_ONE, Q5_ONE)
    ok &= (q5_mul(STEP[0], STEP[0]), q5_mul(STEP[1], STEP[1])) == \
        (q5_mul(BJ[0], BJ[0]), q5_mul(BJ[1], BJ[1]))
    ok &= q5_mul(STEP[0], STEP[1]) == q5(-1)
    ok &= q5_mul(BJ[0], BJ[1]) == Q5_ONE
    for (a, b) in ((1, 1), (2, 3), (1, 0), (0, 1), (5, 2), (3, 3),
                   (7, 1)):
        pa, pb = Q5_ONE, Q5_ONE
        for n in range(0, 61):
            En = q5_add(q5_scal(a, pa), q5_scal(b, pb))
            Pn = q5_sub(q5_scal(a, pa), q5_scal(b, pb))
            inv = q5_sub(q5_mul(En, En), q5_mul(Pn, Pn))
            ok &= inv == q5(4 * a * b * (-1) ** n)
            if (a, b) == (2, 3):
                ok &= inv != q5(0)
            if (a, b) == (1, 1):
                ok &= En == q5(L[n]) and Pn == q5(0, F[n])
            pa = q5_mul(pa, PHI)
            pb = q5_mul(pb, PSI)
    for a in range(1, 6):
        ok &= 4 * a * a == (2 * a) ** 2
    check("BEAT",
          "one beat is one boost times one alternator tick: STEP ="
          " B_J A = A B_J with A^2 = I, STEP^2 = B_J^2, det STEP = -1 ="
          " N(phi), det B_J = 1; the invariant E^2 - P^2 = 4 a b (-1)^n"
          " exactly, 7 amplitude pairs (n <= 60); at a = b = 1 the"
          " readings are L_n and sqrt5 F_n and the balanced shell reads"
          " m = 2a", ok)

    # ---------------------------------------------- 16 breath and TM
    NTM = 1 << 16
    t = [0] * NTM
    for n in range(1, NTM):
        t[n] = t[n >> 1] ^ (n & 1)
    ok = t[:8] == [0, 1, 1, 0, 1, 0, 0, 1]
    ok &= all(t[2 * n] == t[n] for n in range(NTM // 2))
    ok &= all(t[2 * n + 1] == 1 - t[n] for n in range(NTM // 2))
    s = [1 - 2 * b for b in t]
    ok &= all(s[n] == (-1) ** n * s[n >> 1] for n in range(1, NTM))
    ok &= all(s[2 * m] + s[2 * m + 1] == 0 for m in range(NTM // 2))
    ok &= all(sum(s[j << k:(j + 1) << k]) == 0
              for k in range(1, 13) for j in range(NTM >> k))
    ok &= all(sum(s[:1 << k]) == 0 for k in range(1, 17))
    for s0v in (1, -1):
        w = [s0v]
        for _ in range(1000):
            w.append(-w[-1])
        ok &= all(w[n] == s0v * (-1) ** n for n in range(1001))
    ok &= s[1] + s[2] == -2
    poly = [0] * 8192
    poly[0] = 1
    for k in range(13):
        stepk = 1 << k
        poly = [poly[i] - (poly[i - stepk] if i >= stepk else 0)
                for i in range(8192)]
    ok &= all(poly[n] == s[n] for n in range(8192))
    check("TM-BREATH",
          "t(2n) = t(n) and t(2n+1) = 1 - t(n) with the alternator"
          " factorization (-1)^t(n) = (-1)^n (-1)^t(n div 2) below 2^16;"
          " aligned dyadic blocks and prefixes cancel; sliding"
          " cancellation forces the pure breath s(0) (-1)^n and"
          " Thue-Morse breaks it at s(1) + s(2) = -2; prod(1 - x^(2^k))"
          " matches (-1)^t(n) below 2^13: breath at one scale, TM at"
          " every scale", ok)

    print("TWIST-J Dirac ladder witness (exact integer arithmetic)")
    print("D_J(m)(z) = S(z)(I + i m X); electron m = 2 from u v = 4;"
          " det = 1 + m^2 = 5 = p")
    print("the ladder dictionary is read at D; its theorem layer is"
          " verified here")
    print()
    passed = 0
    for i, (name, okv) in enumerate(CHECKS, 1):
        tag = "PASS" if okv else "FAIL"
        if okv:
            passed += 1
        print("%s %02d %s" % (tag, i, name))
    print()
    print("RESULT %d/%d %s" % (passed, len(CHECKS),
                               "ALL PASS" if passed == len(CHECKS)
                               else "FAILURES PRESENT"))
    return 0 if passed == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
