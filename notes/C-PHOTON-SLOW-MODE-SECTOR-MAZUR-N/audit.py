#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction


def sector_mazur_fixture() -> tuple[int, int]:
    # Each sector is represented in a T-eigenbasis:
    # (positive eigenvalues, real symmetric/Hermitian insertion matrix).
    sectors = (
        (
            (Fraction(1), Fraction(2, 3), Fraction(1, 4)),
            (
                (Fraction(2, 5), Fraction(1, 7), Fraction(-1, 9)),
                (Fraction(1, 7), Fraction(-3, 8), Fraction(2, 11)),
                (Fraction(-1, 9), Fraction(2, 11), Fraction(1, 6)),
            ),
        ),
        (
            (Fraction(3, 4), Fraction(1, 2)),
            (
                (Fraction(-1, 3), Fraction(2, 13)),
                (Fraction(2, 13), Fraction(5, 9)),
            ),
        ),
        (
            (Fraction(4, 5),),
            ((Fraction(7, 10),),),
        ),
    )

    checks = 0
    strict = 0
    for L in (2, 3, 4, 5, 6, 8):
        Z = sum(sum(lam**L for lam in lambdas) for lambdas, _ in sectors)
        assert Z > 0

        rhs = Fraction(0)
        for lambdas, E in sectors:
            Zw = sum(lam**L for lam in lambdas)
            mean_num = sum(E[a][a] * lambdas[a] ** L for a in range(len(lambdas)))
            mw = mean_num / Zw
            rhs += (Zw / Z) * mw * mw

        for t in range(1, L):
            lhs_num = Fraction(0)
            for lambdas, E in sectors:
                n = len(lambdas)
                for a in range(n):
                    for b in range(n):
                        lhs_num += (
                            E[a][b]
                            * E[b][a]
                            * lambdas[b] ** t
                            * lambdas[a] ** (L - t)
                        )
            lhs = lhs_num / Z
            assert lhs >= rhs, (L, t, lhs, rhs)
            checks += 1
            if lhs > rhs:
                strict += 1
    return checks, strict


def normalization_fixture() -> int:
    checks = 0
    # kappa^2 L * [ER^2 / (kappa^2 L^3)] = ER^2 / L^2.
    for L in (2, 3, 4, 5, 6, 8, 10):
        for kappa2 in (Fraction(1, 2), Fraction(7, 3), Fraction(11, 5)):
            for ER in (-17, -4, 0, 3, 29):
                lhs = kappa2 * L * Fraction(ER * ER, 1) / (kappa2 * L**3)
                rhs = Fraction(ER * ER, L**2)
                assert lhs == rhs
                checks += 1
    return checks


def site_index(x: tuple[int, int, int], L: int) -> int:
    return (x[0] * L + x[1]) * L + x[2]


def shift(x: tuple[int, int, int], axis: int, delta: int, L: int):
    y = list(x)
    y[axis] = (y[axis] + delta) % L
    return tuple(y)


def edge_index(x: tuple[int, int, int], axis: int, L: int) -> int:
    return site_index(x, L) * 3 + axis


def divergence(r: list[int], L: int) -> list[int]:
    out = [0] * (L**3)
    for x0 in range(L):
        for x1 in range(L):
            for x2 in range(L):
                x = (x0, x1, x2)
                s = 0
                for axis in range(3):
                    incoming = edge_index(shift(x, axis, -1, L), axis, L)
                    outgoing = edge_index(x, axis, L)
                    s += r[incoming] - r[outgoing]
                out[site_index(x, L)] = s
    return out


def winding(r: list[int], axis: int, L: int) -> int:
    total = 0
    # Cut x_axis=0, summing positive axis links based on that cut.
    ranges = [range(L), range(L), range(L)]
    for a in ranges[(axis + 1) % 3]:
        for b in ranges[(axis + 2) % 3]:
            x = [0, 0, 0]
            x[axis] = 0
            x[(axis + 1) % 3] = a
            x[(axis + 2) % 3] = b
            total += r[edge_index(tuple(x), axis, L)]
    return total % 5


def total_flux(r: list[int], axis: int, L: int) -> int:
    total = 0
    for x0 in range(L):
        for x1 in range(L):
            for x2 in range(L):
                total += r[edge_index((x0, x1, x2), axis, L)]
    return total


def winding_fixtures() -> int:
    checks = 0
    for L in (3, 4, 6):
        for axis in range(3):
            # One straight + loop, then its charge conjugate and a two-loop control.
            for copies, sign in ((1, 1), (1, -1), (2, 1), (2, -1)):
                r = [0] * (3 * L**3)
                for copy in range(copies):
                    transverse = [0, 0, 0]
                    transverse[(axis + 1) % 3] = copy
                    transverse[(axis + 2) % 3] = 0
                    for s in range(L):
                        x = transverse.copy()
                        x[axis] = s
                        r[edge_index(tuple(x), axis, L)] = sign

                assert all(v in (-1, 0, 1) for v in r)
                assert divergence(r, L) == [0] * (L**3)

                w = winding(r, axis, L)
                R = total_flux(r, axis, L)
                assert (R - L * w) % 5 == 0, (L, axis, copies, sign, R, w)
                assert R == sign * copies * L
                checks += 1
    return checks


def topology_only_control() -> int:
    checks = 0
    # A residue class alone does not fix the sign of an expectation.
    # For every nonzero residue a in {1,2,3,4}, a and a-5 straddle zero.
    for a in (1, 2, 3, 4):
        positive = a
        negative = a - 5
        assert positive > 0 > negative
        # Choose exact convex weights making the mean zero.
        # q*positive + (1-q)*negative = 0 => q=(5-a)/5.
        q = Fraction(5 - a, 5)
        mean = q * positive + (1 - q) * negative
        assert mean == 0
        assert positive % 5 == negative % 5 == a
        checks += 1
    return checks


def main() -> int:
    mazur, strict = sector_mazur_fixture()
    norm = normalization_fixture()
    wind = winding_fixtures()
    topo = topology_only_control()

    print(
        f"PASS G2: exact rational sector-Mazur fixtures checks={mazur} "
        f"strict={strict}."
    )
    print(
        f"PASS G3: kappa/L normalization identity checks={norm}; "
        "final power is E[R]^2/L^2."
    )
    print(
        f"PASS G5/G7: ternary winding-loop fixtures checks={wind} "
        "obey divergence zero, R_i == L w_i mod 5, and charge conjugation."
    )
    print(
        f"PASS G6: residue-only zero-mean convex controls checks={topo}; "
        "topology alone cannot force a sector mean."
    )
    print("ALL PASS: slow-mode sector-Mazur finite audit complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
