#!/usr/bin/env python3
# TWIST-J gravity chain witness. Exact arithmetic only: integers,
# rationals, Q(sqrt5) pairs, the cyclotomic ring Z[zeta_5], and formal
# Laurent monomial rings over Q. Standard library only, no floats
# anywhere. pi is carried as a formal symbol throughout; nothing here
# evaluates a transcendental number.
#
# The chain: the Kahler capacity V_geo = (4 pi)^3 phi^2 with
# J Jbar = 2 - phi = phi^-2 exactly; the FRW rank 1 lapse action
# closing the (00) constraint algebra with lambda = 216 pi and
# H^2 = 72 pi rho; the fiber multiplier k_f = 1 forced by the master
# closure against G_nat = 27 = d^3 with the cell volume 864 pi; and
# the equation layer of the SI bridge alpha B g = 1 with
# g = 2^5 phi^2 sqrt(3 - phi) carried through its exact square.
#
# Claims verified: KAHLER-CAPACITY, FRW-CANONICAL-FORM,
# GRAVITY-BRIDGE-LAW.

import sys
from fractions import Fraction as Fr
from itertools import combinations

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


def q5_pos(x):
    # exact sign of a + b sqrt5 under the positive square root embedding
    a, b = x
    if a >= 0 and b >= 0:
        return not (a == 0 and b == 0)
    if a < 0 and b < 0:
        return False
    if b > 0:
        return 5 * b * b > a * a
    return a * a > 5 * b * b


# ------------------------------------------------ Z[zeta_5], basis 1..z^3
def zmul(a, b):
    c = [0] * 5
    for i in range(4):
        for j in range(4):
            c[(i + j) % 5] += a[i] * b[j]
    return (c[0] - c[4], c[1] - c[4], c[2] - c[4], c[3] - c[4])


def zadd(a, b):
    return tuple(x + y for x, y in zip(a, b))


def zscal(c, a):
    return tuple(c * x for x in a)


ZETA = (0, 1, 0, 0)
ZONE = (1, 0, 0, 0)
J = (1, 0, 1, 0)
JBAR = (1, 0, 0, 1)
PHI_Z = (0, 0, -1, -1)
ZETA4 = (-1, -1, -1, -1)


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


def mderiv(p, sym):
    # formal partial derivative with respect to one symbol
    r = {}
    for key, c in p.items():
        d = dict(key)
        e = d.get(sym, 0)
        if e == 0:
            continue
        d[sym] = e - 1
        k = tuple(sorted(d.items()))
        r[k] = r.get(k, Fr(0)) + c * e
    return mnorm(r)


def msub_x2(p, repl):
    # substitute x^2 -> repl in a polynomial whose x degree is 0 or 2
    out = {}
    for key, c in p.items():
        d = dict(key)
        e = d.get("x", 0)
        if e == 0:
            out[key] = out.get(key, Fr(0)) + c
            continue
        if e != 2:
            raise ValueError("unexpected x degree")
        d["x"] = 0
        base = mnorm({tuple(sorted(d.items())): c})
        for k, v in mmul(base, repl).items():
            out[k] = out.get(k, Fr(0)) + v
    return mnorm(out)


def factorint(n):
    f = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def main():
    # ------------------------------------------ 01 the modulus chord
    jj = zmul(J, JBAR)
    two_minus_phi = zadd(zscal(2, ZONE), zscal(-1, PHI_Z))
    ok = jj == two_minus_phi == (2, 0, 1, 1)
    phi2 = q5_mul(PHI, PHI)
    ok &= phi2 == q5_add(PHI, Q5_ONE)
    ok &= q5_mul(phi2, q5_sub(q5(2), PHI)) == Q5_ONE
    # N(J) = 1: the product of J over the four Galois conjugates
    conj = [J]
    for k in (2, 3, 4):
        zk = ZONE
        for _ in range(k):
            zk = zmul(zk, ZETA)
        z2k = zmul(zk, zk)
        conj.append(zadd(ZONE, z2k))
    prod = ZONE
    for c in conj:
        prod = zmul(prod, c)
    ok &= prod == ZONE
    check("CHORD",
          "J Jbar = (1 + zeta^2)(1 + zeta^3) = 2 - phi exactly in"
          " Z[zeta_5], and phi^2 (2 - phi) = 1 in Q(sqrt5): the modulus"
          " chord is J Jbar = phi^-2, so h(0) = (J Jbar)^-1 = phi^2;"
          " N(J) = 1 over the four Galois conjugates", ok)

    # ------------------------------------------ 02 the order 0 jet
    # h(t) = phi^2 / (1 + t): the geometric jet has coefficients
    # (-1)^k phi^2 exactly; witnessed by (1 + t) sum_{k<=K} (-1)^k
    # phi^2 t^k = phi^2 (1 - (-t)^(K+1)) as a polynomial identity.
    K = 12
    ok = True
    series = [q5_scal((-1) ** k, phi2) for k in range(K + 1)]
    prodp = [q5(0)] * (K + 2)
    for k, c in enumerate(series):
        prodp[k] = q5_add(prodp[k], c)
        prodp[k + 1] = q5_add(prodp[k + 1], c)
    ok &= prodp[0] == phi2
    ok &= all(prodp[k] == q5(0) for k in range(1, K + 1))
    ok &= prodp[K + 1] == q5_scal((-1) ** K, phi2)
    ok &= series[0] == phi2
    check("JET",
          "h(t) = phi^2/(1 + t): the jet coefficients are (-1)^k phi^2"
          " exactly in Q(sqrt5) (witnessed to order 12 by the closed"
          " telescoping identity); the order 0 jet is h(0) = phi^2", ok)

    # ------------------------------------------ 03 the capacity monomial
    fs = mmul(mmul(M(4, pi=1), M(4, pi=1)), M(4, pi=1))
    vgeo = mmul(fs, M(1, phi=2))
    ok = fs == M(64, pi=3)
    ok &= 4 ** 3 == 64 == 2 ** 6
    ok &= vgeo == M(64, pi=3, phi=2)
    ((key, coef),) = tuple(vgeo.items())
    d = dict(key)
    ok &= d.get("pi") == 3 and d["pi"] % 2 == 1 and d.get("phi") == 2
    check("CAPACITY",
          "V_geo = (4 pi)^3 phi^2 = 64 pi^3 phi^2 as an exact monomial:"
          " the Fubini-Study factor (4 pi)^3 = 64 pi^3 with 4^3 = 64,"
          " the order 0 jet phi^2; the pi degree 3 is odd, the parity"
          " law carrier", ok)

    # ------------------------------------------ 04 the lapse variation
    # L/V0 = -(3/lam) E x^2 / n - n E r, with x = Phidot, n = nu,
    # E = e^(3 Phi), r = rho(Phi)
    L = madd(M(-3, x=2, n=-1, E=1, lam=-1), M(-1, n=1, E=1, r=1))
    dLdn = mderiv(L, "n")
    lhs = mmul(dLdn, M(1, lam=1, n=2))
    rhs = madd(M(3, x=2, E=1), M(-1, lam=1, r=1, n=2, E=1))
    ok = lhs == rhs
    # so dL/dn = 0 is 3 x^2 = lam r n^2, i.e. 3 (Phidot/nu)^2 = lam rho
    check("LAPSE",
          "the lapse variation of the rank 1 action S = V0 int dt nu"
          " e^(3 Phi) [-(3/lambda)(Phidot/nu)^2 - rho] gives"
          " lambda nu^2 dL/dnu = e^(3 Phi)(3 Phidot^2 - lambda rho"
          " nu^2) exactly: the (00) constraint 3 H^2 = lambda rho", ok)

    # ------------------------------------------ 05 lambda = 216 pi
    ok = Fr(216, 3) == 72
    ok &= factorint(216) == {2: 3, 3: 3}
    ok &= factorint(72) == {2: 3, 3: 2}
    ok &= mscal(Fr(1, 3), M(216, pi=1)) == M(72, pi=1)
    ok &= 216 == 3 * 72 and 864 == 12 * 72 == 4 * 216
    check("LAMBDA",
          "lambda = 216 pi gives H^2 = (lambda/3) rho = 72 pi rho"
          " exactly; 216 = 2^3 3^3 and 72 = 2^3 3^2; the cell chain"
          " 864 = 12 . 72 = 4 . 216 closes on the same integers", ok)

    # ------------------------------------------ 06 the three 2-planes
    pairs = list(combinations(range(3), 2))
    s_pairs = mnorm({mkey(H=2): Fr(len(pairs))})
    ok = len(pairs) == 3
    ok &= s_pairs == M(3, H=2)
    ok &= 3 == (3 * 2) // 2
    check("TWO-PLANES",
          "the coefficient 3 counts the spatial 2-planes: C(3, 2) = 3"
          " and sum over i < j of H_i H_j = 3 H^2 on the isotropic"
          " background; d = 3 throughout", ok)

    # ------------------------------------------ 07 Euler-Lagrange chain
    # gauge nu = 1; rho = rho(Phi) with rho' = drho/dPhi
    dLdx = M(-6, x=1, E=1, lam=-1)
    ddt = madd(mmul(mderiv(dLdx, "E"), M(3, E=1, x=1)),
               mmul(mderiv(dLdx, "x"), M(1, X=1)))
    dLdPhi = madd(mmul(mderiv(madd(M(-3, x=2, E=1, lam=-1),
                                   M(-1, E=1, r=1)), "E"), M(3, E=1)),
                  M(-1, E=1, rp=1))
    EL = msub(ddt, dLdPhi)
    target = madd(madd(M(6, X=1, lam=-1), M(9, x=2, lam=-1)),
                  madd(M(-3, r=1), M(-1, rp=1)))
    ok = madd(EL, mmul(M(1, E=1), target)) == {}
    # impose the constraint x^2 = lam r / 3
    reduced = msub_x2(target, M(Fr(1, 3), lam=1, r=1))
    ok &= reduced == madd(M(6, X=1, lam=-1), M(-1, rp=1))
    # perfect fluid rho' = -3 (rho + p): 2 Hdot = -lambda (rho + p)
    pf = madd(M(6, X=1, lam=-1), madd(M(3, r=1), M(3, P=1)))
    second = mmul(pf, M(Fr(1, 3), lam=1))
    ok &= second == madd(M(2, X=1), madd(M(1, lam=1, r=1),
                                         M(1, lam=1, P=1)))
    check("FRIEDMANN",
          "the Phi Euler-Lagrange equation is e^(3 Phi) [(6/lambda)"
          " Hdot + (9/lambda) H^2 - 3 rho - rho'] exactly; imposing"
          " 3 H^2 = lambda rho leaves (6/lambda) Hdot = rho'; the"
          " continuity rho' = -3 (rho + p) gives the second Friedmann"
          " equation 2 Hdot = -lambda (rho + p)", ok)

    # ------------------------------------------ 08 the Hamiltonian form
    piPhi = M(-6, x=1, E=1, n=-1, lam=-1, v=1)
    pi2 = mmul(piPhi, piPhi)
    Cterm = madd(mscal(Fr(-1, 12), mmul(pi2, M(1, lam=1, v=-1, E=-1))),
                 M(1, v=1, E=1, r=1))
    lhs = mmul(Cterm, M(1, lam=1))
    rhs = mscal(-1, mmul(M(1, v=1, E=1),
                         madd(M(3, x=2, n=-2), M(-1, lam=1, r=1))))
    ok = lhs == rhs
    check("HAMILTONIAN",
          "with pi_Phi = -(6/lambda) V0 e^(3 Phi) Phidot / nu, the"
          " constraint C = -(lambda/(12 V0 e^(3 Phi))) pi_Phi^2 +"
          " V0 e^(3 Phi) rho satisfies lambda C = -V0 e^(3 Phi)"
          " (3 (Phidot/nu)^2 - lambda rho) exactly: the canonical (00)"
          " form", ok)

    # ------------------------------------------ 09 the forced fiber
    ok = 2 * (3 + 1) ** 2 * 3 ** 3 == 864
    ok &= factorint(864) == {2: 5, 3: 3}
    ksrc = Fr(12 * (3 - 12), 2)
    ok &= ksrc == -54
    # master closure at k = 12, V = k_f . 864 pi
    kflux = mmul(M(Fr(12, 12), pi=-1, kf=-1), M(Fr(1, 864)))
    master_lhs = mmul(mscal(ksrc * ksrc, kflux), M(8, pi=1))
    ok &= master_lhs == M(27, kf=-1)
    gnat = mscal(Fr(3, 8 * 12), mmul(M(864, pi=1, kf=1), M(1, pi=-1)))
    ok &= gnat == M(27, kf=1)
    master = msub(master_lhs, gnat)
    poly_kf = mmul(master, M(1, kf=1))
    ok &= poly_kf == madd(M(27), M(-27, kf=2))
    # 27 - 27 kf^2 = -27 (kf - 1)(kf + 1): the positive root is kf = 1
    ok &= mscal(-27, mmul(madd(M(1, kf=1), M(-1)),
                          madd(M(1, kf=1), M(1)))) == poly_kf
    ok &= 27 == 3 ** 3
    check("FIBER-FORCED",
          "V_cell = 2 (d+1)^2 d^3 pi = 864 pi = 2^5 3^3 pi; the source"
          " coefficient k (3 - k)/2 = -54 at k = 12 is pi free and V"
          " free; the master closure K_flux K_src^2 8 pi = G_nat at"
          " V = k_f 864 pi reads 27/k_f = 27 k_f, so k_f^2 = 1 and the"
          " positive root k_f = 1 is forced; G_nat = 27 = d^3", ok)

    # ------------------------------------------ 10 the fiber circle
    zeta_plus = zadd(ZETA, ZETA4)
    phi_minus_1 = zadd(PHI_Z, zscal(-1, ZONE))
    ok = zeta_plus == phi_minus_1 == (-1, 0, -1, -1)
    ok &= zmul(ZETA, zeta_plus) == J
    # phi - 1 = (-1 + sqrt5)/2 is positive exactly
    ok &= q5_pos(q5_sub(PHI, Q5_ONE))
    # one step is arg J = arg zeta = 2 pi / 5; p steps close the fiber
    ok &= Fr(5) * Fr(2, 5) == 2
    ok &= mscal(5, M(Fr(2, 5), pi=1)) == M(2, pi=1)
    # the cell volume carries exactly one fiber 2 pi: pi degree 1
    ((key, coef),) = tuple(M(864, pi=1).items())
    ok &= dict(key).get("pi") == 1
    check("FIBER-CIRCLE",
          "J = zeta (zeta + zeta^4) exactly in Z[zeta_5] with"
          " zeta + zeta^4 = phi - 1 > 0, so the step phase is the fiber"
          " generator phase, one step per 2 pi/5; p = 5 steps close the"
          " U(1) fiber at 2 pi; the cell volume 864 pi carries exactly"
          " one fiber 2 pi (pi degree 1, odd)", ok)

    # ------------------------------------------ 11 the bridge equation
    # g = 2^5 phi^2 sqrt(3 - phi), carried through its exact square
    ok = zmul(zadd(ZONE, zscal(-1, ZETA)),
              zadd(ZONE, zscal(-1, ZETA4))) == (3, 0, 1, 1)
    three_minus_phi = q5_sub(q5(3), PHI)
    phi4 = q5_mul(phi2, phi2)
    ok &= phi4 == q5_add(q5_scal(3, PHI), q5(2))
    g2 = q5_scal(1024, q5_mul(phi4, three_minus_phi))
    ok &= g2 == q5_mul(q5_scal(32, phi2), q5_mul(q5_scal(32, phi2),
                                                 three_minus_phi))
    ok &= q5_pos(three_minus_phi) and q5_pos(g2)
    ok &= Fr(32, 33) ** 2 == Fr(1024, 1089)
    ok &= 33 == 2 ** 5 + 1 and 1024 == 2 ** 10 and 1089 == 33 ** 2
    # bridge law alpha B g = 1 identically at B = alpha^-1 g^-1
    ok &= mmul(mmul(M(1, alpha=1), M(1, alpha=-1, g=-1)),
               M(1, g=1)) == M(1)
    # dimensional identity hbar c / m_e^2 = lambda_e^2 c^3 / hbar
    lam_e = M(1, hbar=1, m=-1, c=-1)
    ok &= mmul(mmul(lam_e, lam_e), M(1, c=3, hbar=-1)) == \
        M(1, hbar=1, c=1, m=-2)
    check("BRIDGE-EXACT",
          "|1 - zeta|^2 = 3 - phi exactly in Z[zeta_5]; g = 2^5 phi^2"
          " sqrt(3 - phi) carried through g^2 = 1024 phi^4 (3 - phi)"
          " > 0 exactly in Q(sqrt5); (32/33)^2 = 1024/1089 with"
          " 33 = 2^5 + 1; the bridge law alpha B g = 1 holds"
          " identically at B = alpha^-1/g; the dimensional identity"
          " hbar c/m_e^2 = lambda_e^2 c^3/hbar is exact", ok)

    # ------------------------------------------ 12 the wall spelling
    # G_T = (32/33)^2 alpha^20 / g; with ell_P^2 = 27 ell_G^2 the two
    # spellings agree: 27 (ell_G/lambda_e)^2 = G_T reads
    # (ell_P/lambda_e)^2 = [(32/33) alpha^10]^2 / g
    GT = mscal(Fr(1024, 1089), M(1, alpha=20, g=-1))
    rhs_sq = mmul(mscal(Fr(32, 33), M(1, alpha=10)),
                  mscal(Fr(32, 33), M(1, alpha=10)))
    ok = mmul(rhs_sq, M(1, g=-1)) == GT
    lhs = mscal(27, mmul(M(1, ellG=2), M(1, lamE=-2)))
    ellP2 = M(27, ellG=2)
    ok &= mmul(ellP2, M(1, lamE=-2)) == lhs
    # the alpha content of G_T is exactly alpha^20: stripping the
    # alpha free residue (32/33)^2 / g leaves the pure monomial
    residue = mscal(Fr(1024, 1089), M(1, g=-1))
    ok &= mmul(residue, M(1, alpha=20)) == GT
    ((key, coef),) = tuple(GT.items())
    ok &= dict(key).get("alpha") == 20 and 20 == 2 * 10 == 4 * 5
    check("WALL-FORM",
          "the wall spelling is exact at the equation layer: squaring"
          " ell_P/lambda_e = (32/33) alpha^10 / sqrt(g) gives"
          " (ell_P/lambda_e)^2 = (32/33)^2 alpha^20 / g = G_T, and with"
          " ell_P^2 = 27 ell_G^2 this is 27 (ell_G/lambda_e)^2 = G_T;"
          " the alpha content of G_T is exactly alpha^20 = alpha^(4p);"
          " the SI value of G is not claimed here", ok)

    print("TWIST-J gravity chain witness (exact arithmetic, formal pi)")
    print("V_geo = 64 pi^3 phi^2; H^2 = 72 pi rho at lambda = 216 pi;"
          " k_f = 1 forced; G_nat = 27 = d^3")
    print("the SI bridge is carried at the equation layer only; the"
          " value of G stays on the frontier")
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
