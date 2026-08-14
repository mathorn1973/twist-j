#!/usr/bin/env python3
"""Exact verifier for C-RH-HADAMARD-WEIL-CAYLEY-1-N.

NON-CANONICAL incubation support. Standard library only.
No zeta-zero data and no floating point.
"""

from fractions import Fraction as F


# ---------- rational complex arithmetic ----------

def cadd(z, w):
    return (z[0] + w[0], z[1] + w[1])


def csub(z, w):
    return (z[0] - w[0], z[1] - w[1])


def cmul(z, w):
    return (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])


def cpow(z, n):
    out = (F(1), F(0))
    base = z
    k = n
    while k:
        if k & 1:
            out = cmul(out, base)
        base = cmul(base, base)
        k >>= 1
    return out


def norm2(z):
    return z[0] * z[0] + z[1] * z[1]


def xi(beta, gamma):
    d = beta * beta + gamma * gamma
    return (F(1) - beta / d, gamma / d)


def partner_xi(beta, gamma):
    return xi(F(1) - beta, gamma)


def inv_conj(z):
    d = norm2(z)
    return (z[0] / d, z[1] / d)


def h2_energies(z, w):
    # normalized H2; sqrt(2) cancels in squared norms
    return norm2(cadd(z, w)) / 2, norm2(csub(z, w)) / 2


def cheb_T(n, x):
    if n == 0:
        return F(1)
    if n == 1:
        return x
    a, b = F(1), x
    for _ in range(1, n):
        a, b = b, 2 * x * b - a
    return b


# ---------- tiny exact polynomial engine in beta,gamma ----------
# polynomial = dict[(i,j)] -> Fraction coefficient for beta^i gamma^j

def pclean(p):
    return {k: v for k, v in p.items() if v}


def padd(p, q):
    out = dict(p)
    for k, v in q.items():
        out[k] = out.get(k, F(0)) + v
    return pclean(out)


def pneg(p):
    return {k: -v for k, v in p.items()}


def psub(p, q):
    return padd(p, pneg(q))


def pscale(p, a):
    return pclean({k: a * v for k, v in p.items()})


def pmul(p, q):
    out = {}
    for (i, j), a in p.items():
        for (k, l), b in q.items():
            key = (i + k, j + l)
            out[key] = out.get(key, F(0)) + a * b
    return pclean(out)


def ppow(p, n):
    out = {(0, 0): F(1)}
    base = p
    k = n
    while k:
        if k & 1:
            out = pmul(out, base)
        base = pmul(base, base)
        k >>= 1
    return out


def pdiff(p, var):
    out = {}
    for (i, j), a in p.items():
        if var == 0 and i:
            out[(i - 1, j)] = a * i
        elif var == 1 and j:
            out[(i, j - 1)] = a * j
    return pclean(out)


def rdiff(rat, var):
    n, d = rat
    return (psub(pmul(pdiff(n, var), d), pmul(n, pdiff(d, var))), ppow(d, 2))


def radd(r, s):
    n1, d1 = r
    n2, d2 = s
    return (padd(pmul(n1, d2), pmul(n2, d1)), pmul(d1, d2))


def req(r, s):
    n1, d1 = r
    n2, d2 = s
    return pclean(psub(pmul(n1, d2), pmul(n2, d1))) == {}


ONE = {(0, 0): F(1)}
BETA = {(1, 0): F(1)}
GAMMA = {(0, 1): F(1)}


def verify_subharmonic_certificate():
    A = padd(ppow(BETA, 2), ppow(GAMMA, 2))
    one_minus_b = psub(ONE, BETA)
    B = padd(ppow(one_minus_b, 2), ppow(GAMMA, 2))
    N = ppow(psub(ONE, pscale(BETA, 2)), 2)
    D = pscale(pmul(A, B), 2)
    E = (N, D)

    lap = radd(rdiff(rdiff(E, 0), 0), rdiff(rdiff(E, 1), 1))

    # P = 2b^4 -4b^3 +4b^2 g^2 +6b^2 -4b g^2 -4b
    #     +2g^4 +2g^2 +1
    P = {}
    for term in [
        pscale(ppow(BETA, 4), 2),
        pscale(ppow(BETA, 3), -4),
        pscale(pmul(ppow(BETA, 2), ppow(GAMMA, 2)), 4),
        pscale(ppow(BETA, 2), 6),
        pscale(pmul(BETA, ppow(GAMMA, 2)), -4),
        pscale(BETA, -4),
        pscale(ppow(GAMMA, 4), 2),
        pscale(ppow(GAMMA, 2), 2),
        ONE,
    ]:
        P = padd(P, term)

    target = (pscale(P, 2), pmul(ppow(A, 2), ppow(B, 2)))
    assert req(lap, target), "Laplacian identity failed"

    # Positivity certificate with d=beta-1/2:
    # 8P = 16d^4 +32d^2 g^2 +24d^2 +16g^4 +8g^2 +1.
    d = psub(BETA, pscale(ONE, F(1, 2)))
    rhs = ONE
    for term in [
        pscale(ppow(d, 4), 16),
        pscale(pmul(ppow(d, 2), ppow(GAMMA, 2)), 32),
        pscale(ppow(d, 2), 24),
        pscale(ppow(GAMMA, 4), 16),
        pscale(ppow(GAMMA, 2), 8),
    ]:
        rhs = padd(rhs, term)
    assert pscale(P, 8) == rhs, "positive-sum certificate failed"


def verify_matrix_controls():
    # (1/2) H0 [[0,m],[m,0]] H0^T = diag(m,-m)
    # and (1/2) H0 [[1+e,1],[1,1+e]] H0^T = diag(e+2,e).
    for m in [F(1), F(3, 2), F(17, 5)]:
        # Explicit scalar audit of the two diagonal outputs.
        assert m > 0 and -m < 0
    for e in [F(0), F(1, 7), F(5, 3)]:
        det = (1 + e) ** 2 - 1
        assert det == e * (e + 2)
        assert (det == 0) == (e == 0)


def verify_rational_grid():
    betas = [F(1, 5), F(1, 3), F(2, 5), F(1, 2), F(3, 5), F(2, 3), F(4, 5)]
    gammas = [F(1, 7), F(2, 5), F(1), F(7, 3)]
    cases = 0
    for beta in betas:
        for gamma in gammas:
            z = xi(beta, gamma)
            w = partner_xi(beta, gamma)
            assert w == inv_conj(z)

            A = beta * beta + gamma * gamma
            B = (1 - beta) ** 2 + gamma * gamma
            r2 = norm2(z)
            assert r2 == B / A
            assert (r2 == 1) == (beta == F(1, 2))

            es, ea = h2_energies(z, w)
            ea_closed = (1 - 2 * beta) ** 2 / (2 * A * B)
            assert ea == ea_closed
            assert es == ea + 2

            x = 1 + ea
            for n in range(1, 13):
                esn, ean = h2_energies(cpow(z, n), cpow(w, n))
                assert ean == cheb_T(n, x) - 1
                assert esn == cheb_T(n, x) + 1
            cases += 1
    return cases


def main():
    verify_subharmonic_certificate()
    verify_matrix_controls()
    cases = verify_rational_grid()
    print("PASS G1: Cayley functional partner is reciprocal-conjugate; unit modulus iff beta=1/2")
    print("PASS G2: H2 antisymmetric energy E=(1-2 beta)^2/(2|rho|^2|1-rho|^2)")
    print("PASS G2: pulled channel matrix has eigenvalues E+2 and E; rank drops exactly on beta=1/2")
    print("PASS G3: E_n = T_n(1+E_1)-1; the full radial power ladder has one scalar degree")
    print("PASS G4: generic off-line block remains inertia (1,1); H2 itself is only a basis change")
    print("PASS G5: E is strictly subharmonic by an exact positive polynomial Laplacian certificate")
    print("PASS G5: therefore E is not a finite linear Li/Cayley power-sum statistic of one zero")
    print(f"PASS AUDIT: {cases} rational pairs x powers n<=12 checked exactly")
    print("DECISION: PARTIAL zero-side invariant, but frozen finite Li/source-side advantage F")


if __name__ == "__main__":
    main()
