#!/usr/bin/env python3
"""Independent breaker for C-RH-HADAMARD-WEIL-CAYLEY-1-N.

Written from PREREG.md before verify.py. Standard-library exact arithmetic only.
This is NON-CANONICAL incubation support, not public evidence.
"""

from fractions import Fraction as F


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


def hadamard_energies(z, w):
    # normalized H2 energies; sqrt(2) cancels in norm squares
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


def run():
    betas = [F(1, 5), F(1, 3), F(2, 5), F(1, 2), F(3, 5), F(2, 3), F(4, 5)]
    gammas = [F(1, 7), F(2, 5), F(1), F(7, 3)]
    cases = 0
    off = 0

    for beta in betas:
        for gamma in gammas:
            z = xi(beta, gamma)
            w = partner_xi(beta, gamma)
            assert w == inv_conj(z), (beta, gamma, z, w, inv_conj(z))

            r2 = norm2(z)
            es, ea = hadamard_energies(z, w)
            A = beta * beta + gamma * gamma
            B = (F(1) - beta) ** 2 + gamma * gamma
            ea_formula = (F(1) - 2 * beta) ** 2 / (2 * A * B)
            assert ea == ea_formula
            assert es - ea == 2
            assert (ea == 0) == (beta == F(1, 2))

            # Pullback channel matrix [[1+ea,1],[1,1+ea]]:
            # determinant = ea(ea+2), so rank 1 exactly on the line.
            det = (F(1) + ea) ** 2 - 1
            assert det == ea * (ea + 2)
            assert (det == 0) == (beta == F(1, 2))

            # Power ladder. x = (r^2+r^-2)/2 = 1+ea_1.
            x = F(1) + ea
            for n in range(1, 9):
                zn = cpow(z, n)
                wn = cpow(w, n)
                esn, ean = hadamard_energies(zn, wn)
                assert ean == cheb_T(n, x) - 1
                assert esn == cheb_T(n, x) + 1

            cases += 1
            off += beta != F(1, 2)

    # Strict subharmonicity control for the radial defect E(beta,gamma).
    # After direct differentiation,
    # Delta E = 2*P/(A^2 B^2), with d=beta-1/2 and
    # 8P = 16d^4 + 32d^2 g^2 + 24d^2 + 16g^4 + 8g^2 + 1 > 0.
    # The breaker only checks the frozen exact polynomial identity is positive
    # on the rational attack grid; the written proof must justify differentiation.
    for beta in betas:
        d = beta - F(1, 2)
        for gamma in gammas:
            eightP = (
                16 * d**4 + 32 * d**2 * gamma**2 + 24 * d**2
                + 16 * gamma**4 + 8 * gamma**2 + 1
            )
            assert eightP > 0

    print(f"BREAKER PASS: {cases} rational Cayley pairs, {off} off-line cases")
    print("BREAKER PASS: partner, H2 energy, rank, and n<=8 power ladder exact")
    print("BREAKER PASS: radial defect strict-subharmonicity polynomial positive on attack grid")
    print("BREAKER VERDICT: no counterexample found; Hadamard invertibility itself adds no data")


if __name__ == "__main__":
    run()
