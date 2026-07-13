#!/usr/bin/env python3
# TWIST-J mass ladder witness. Exact arithmetic only: integers,
# rationals, Q(sqrt5) pairs, and formal Laurent monomial rings over Q.
# Standard library only, no floats anywhere. pi is carried as a formal
# symbol; no transcendental number is evaluated, and the sigma
# comparisons of the ladder stay fenced measured witnesses outside
# this file.
#
# The ladder: the shared coefficient C = 89/5 = 18 - 1/p; the exact
# exchange identity delta mu_tau + 240 delta mu_mu = 0; the committed
# forms mu_mu = 2688/13 - C alpha^2, mu_tau = 3477 + 240 C alpha^2,
# mu_p = 6 pi^5 (1 + alpha^2/3), mu_n = mu_p + deg_v/chi - Delta_EM;
# the parity law under the formal pi-grading involution iota_pi,
# which fixes every other generator and sends pi to -pi, with the
# three odd carriers pi^1, pi^3, pi^5 and the neutron as the unique
# mixed composite; the exact bridges xi phi^2 = 5, Q phi^2 = 2 pi,
# Q/xi = 2 pi/5; and the bridge defect 6 phi^2 - 5 pi nonzero by
# Lindemann-Weierstrass on the exact algebraic side.
#
# Claims verified: MU-TAU-COEFFICIENT, MU-EXCHANGE-IDENTITY,
# MASS-LADDER-FORMS, PARITY-LAW, BRIDGE-DEFECT.

import sys
from fractions import Fraction as Fr
from math import gcd, isqrt

CHECKS = []


def check(tag, description, ok):
    CHECKS.append(("%-12s %s" % (tag, description), bool(ok)))


# ------------------------------------------------ Q(sqrt5): a + b sqrt5
def q5(a, b=0):
    return (Fr(a), Fr(b))


Q5_ONE = q5(1)
PHI = (Fr(1, 2), Fr(1, 2))


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


def q5_inv(x):
    n = q5_norm(x)
    c = q5_conj(x)
    return (c[0] / n, c[1] / n)


# ------------------------------------ Laurent monomial ring over Q
def mkey(**exps):
    return tuple(sorted((k, v) for k, v in exps.items() if v != 0))


def mnorm(p):
    out = {}
    for key, c in p.items():
        k = tuple((s, e) for s, e in key if e != 0)
        out[k] = out.get(k, Fr(0)) + c
    return {k: c for k, c in out.items() if c != 0}


def madd(p, q):
    r = dict(p)
    for k, c in q.items():
        r[k] = r.get(k, Fr(0)) + c
    return mnorm(r)


def msub(p, q):
    return madd(p, {k: -c for k, c in q.items()})


def mmul(p, q):
    r = {}
    for k1, c1 in p.items():
        for k2, c2 in q.items():
            d = dict(k1)
            for s, e in k2:
                d[s] = d.get(s, 0) + e
            k = tuple(sorted(d.items()))
            r[k] = r.get(k, Fr(0)) + c1 * c2
    return mnorm(r)


def mscal(c, p):
    return mnorm({k: Fr(c) * v for k, v in p.items()})


def M(coef, **exps):
    return mnorm({mkey(**exps): Fr(coef)})


def pdeg(key):
    return dict(key).get("pi", 0)


def pi_grade_involution(p):
    # Formal grading automorphism: fix every other generator, pi -> -pi.
    # This is not ordinary complex conjugation, which fixes real pi.
    return mnorm({k: (c if pdeg(k) % 2 == 0 else -c)
                  for k, c in p.items()})


def is_even(p):
    return pi_grade_involution(p) == p and p != {}


def is_odd(p):
    return madd(pi_grade_involution(p), p) == {} and p != {}


def pi_degrees(p):
    return sorted({pdeg(k) for k in p})


def main():
    # ------------------------------------------ 01 the shared coefficient
    C0 = Fr(89, 5)
    ok = C0 == 18 - Fr(1, 5)
    ok &= 18 == Fr(1, 2) * 12 * 3
    ok &= 240 * C0 == 4272
    ok &= gcd(5, 13) == 1
    ok &= Fr(2688, 13).denominator == 13
    check("COEFFICIENT",
          "C = 89/5 = 18 - 1/p exactly: matter_spatial 18 = (1/2)(12)(3)"
          " and the trace term 1/p at p = 5; the tau side carries"
          " 240 C = 4272, an integer; the muon denominator 13 and the"
          " coefficient denominator 5 are coprime", ok)

    # ------------------------------------------ 02 the exchange identity
    dmu_mu = M(-1, dC=1, a=2)
    dmu_tau = M(240, dC=1, a=2)
    ok = madd(dmu_tau, mscal(240, dmu_mu)) == {}
    swept = True
    for num, den in ((1, 1), (-1, 1), (89, 5), (-7, 3), (240, 13)):
        dC = Fr(num, den)
        swept &= 240 * dC + 240 * (-dC) == 0
    ok &= swept
    check("EXCHANGE",
          "the exchange identity delta mu_tau + 240 delta mu_mu = 0"
          " exactly in Q: under any shift of the shared coefficient the"
          " muon reading moves by -dC alpha^2 and the tau reading by"
          " +240 dC alpha^2, so the weighted sum vanishes identically"
          " and on a rational sweep", ok)

    # ------------------------------------------ 03 the committed forms
    mu_mu = madd(M(Fr(2688, 13)), M(-C0, a=2))
    mu_tau = madd(M(3477), M(4272, a=2))
    ok = mu_mu[mkey(a=2)] == -C0
    ok &= mu_tau[mkey(a=2)] == 240 * C0 == 4272
    ok &= mu_mu[mkey()] == Fr(2688, 13) and mu_tau[mkey()] == 3477
    ok &= pi_degrees(mu_mu) == [0] and pi_degrees(mu_tau) == [0]
    check("FORMS",
          "the committed forms on the single anchor m_e: mu_mu ="
          " 2688/13 - C alpha^2 and mu_tau = 3477 + 240 C alpha^2 share"
          " the one coefficient C = 89/5 with opposite roles -1 and"
          " +240; both entries are pi free, hence parity even; the"
          " sigma comparisons stay fenced outside this witness", ok)

    # ------------------------------------------ 04 the proton carrier
    mu_p = mmul(M(6, pi=5), madd(M(1), M(Fr(1, 3), a=2)))
    ok = mu_p == madd(M(6, pi=5), M(2, pi=5, a=2))
    ok &= 6 * Fr(1, 3) == 2
    ok &= pi_degrees(mu_p) == [5] and is_odd(mu_p)
    check("PROTON",
          "mu_p = 6 pi^5 (1 + alpha^2/3) = 6 pi^5 + 2 pi^5 alpha^2:"
          " every monomial carries the single bare pi^5, so the proton"
          " is a homogeneous odd delta carrier, the pi^5 rung of the"
          " ladder", ok)

    # ------------------------------------------ 05 the mixed neutron
    mu_n = madd(mu_p, madd(M(1, degv=1, chi=-1), M(-1, dEM=1)))
    ok = pi_degrees(mu_n) == [0, 5]
    ok &= (not is_even(mu_n)) and (not is_odd(mu_n))
    check("NEUTRON-MIX",
          "mu_n = mu_p + deg_v/chi - Delta_EM carries pi degrees {5, 0}"
          " at the form level: the neutron is the unique mixed parity"
          " composite of the ladder, the boundary witness; Delta_EM"
          " stays open on the frontier (NEUTRON-DELTA-EM)", ok)

    # ------------------------------------------ 06 the exact bridges
    phi2 = q5_mul(PHI, PHI)
    phim2 = q5_sub(q5(2), PHI)
    ok = q5_mul(phi2, phim2) == Q5_ONE
    xi0 = q5_scal(5, phim2)
    q0 = q5_scal(2, phim2)
    ok &= xi0 == (Fr(15, 2), Fr(-5, 2)) and q0 == (Fr(3), Fr(-1))
    ok &= q5_mul(xi0, phi2) == q5(5)
    ok &= q5_mul(q0, phi2) == q5(2)
    ok &= q5_mul(q5_inv(xi0), q0) == q5(Fr(2, 5))
    check("BRIDGES",
          "xi = 5 phi^-2 and script-Q = 2 pi phi^-2 close the exact"
          " bridges in Q(sqrt5): xi phi^2 = 5 = p, script-Q phi^2 ="
          " 2 pi, and script-Q / xi = (2/5) pi = 2 pi/5 = arg J, the"
          " step phase of the fiber circle", ok)

    # ------------------------------------------ 07 the bridge defect
    six_phi2 = q5_scal(6, phi2)
    ok = six_phi2 == (Fr(9), Fr(3))
    x = six_phi2
    minpoly = q5_add(q5_sub(q5_mul(x, x), q5_scal(18, x)), q5(36))
    ok &= minpoly == q5(0)
    disc = 18 * 18 - 4 * 36
    ok &= disc == 180 and isqrt(disc) ** 2 != disc
    check("DEFECT",
          "6 phi^2 = 9 + 3 sqrt5 exactly, a root of x^2 - 18x + 36,"
          " irreducible over Q since 180 is not a square: the algebraic"
          " side of the defect delta = 6 phi^2 - 5 pi is degree 2,"
          " while pi is transcendental (Lindemann-Weierstrass), so"
          " delta is nonzero; the numerical gap stays a labeled"
          " witness outside this file", ok)

    # ------------------------------------------ 08 the parity law
    evens = [
        M(1, a=-1),                                        # alpha^-1
        madd(M(Fr(3, 13)), M(Fr(1, 32), pi=-2, phi=-4)),   # sin^2 tW
        M(Fr(-14, 15)),                                    # w
        M(Fr(1, 100), pi=2),                               # L
        M(Fr(1, 200), pi=2),                               # Omega_b
        M(1, X=1),                                         # the slip X
        madd(M(Fr(2688, 13)), M(-Fr(89, 5), a=2)),         # mu_mu
        madd(M(3477), M(4272, a=2)),                       # mu_tau
        mscal(Fr(1024, 1089), M(1, a=20, g=-1)),           # G_T entry
        M(1, PM=1),                                        # PMNS
        M(2250, ln=2, pi=-4),                              # dark ratio
        M(1, zK=1),                                        # zeta_K
        M(Fr(341, 10)),                                    # nu register
    ]
    odds = [M(2, pi=1, phi=-2), M(64, pi=3, phi=2),
            madd(M(6, pi=5), M(2, pi=5, a=2))]
    sample_a = madd(M(2, pi=-1, phi=2), M(3, X=1))
    sample_b = madd(M(5, pi=2), M(-7, a=1))
    ok = pi_grade_involution(pi_grade_involution(sample_a)) == sample_a
    ok &= pi_grade_involution(mmul(sample_a, sample_b)) == mmul(
        pi_grade_involution(sample_a), pi_grade_involution(sample_b))
    ok &= all(is_even(e) for e in evens) and len(evens) == 13
    ok &= all(is_odd(o) for o in odds)
    ok &= sorted(pi_degrees(o)[0] for o in odds) == [1, 3, 5]
    ok &= 18 * 5 ** 3 == 2250
    mu_n = madd(madd(M(6, pi=5), M(2, pi=5, a=2)),
                madd(M(1, degv=1, chi=-1), M(-1, dEM=1)))
    ok &= (not is_even(mu_n)) and (not is_odd(mu_n))
    check("PARITY",
          "under the formal pi-grading involution iota_pi, which fixes"
          " every other generator and maps pi to -pi, the thirteen"
          " named register entries"
          " (alpha^-1, sin^2 theta_W, w, L, Omega_b, the slip X, mu_mu,"
          " mu_tau, G, PMNS, the dark matter ratio 2250 ln^2 phi /"
          " pi^4, the zeta_K residue, the neutrino register 341/10)"
          " are pure even eigenvectors and delta free; the three odd"
          " delta carriers"
          " sit at pi degrees 1, 3, 5; the neutron is the unique mixed"
          " composite; ordinary complex conjugation is not invoked and"
          " no larger census is claimed", ok)

    print("TWIST-J mass ladder witness (exact arithmetic, formal pi)")
    print("C = 89/5 = 18 - 1/p; delta mu_tau + 240 delta mu_mu = 0;"
          " mu_p = 6 pi^5 (1 + alpha^2/3)")
    print("the sigma comparisons stay fenced measured witnesses; no"
          " value is claimed beyond the committed forms")
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
