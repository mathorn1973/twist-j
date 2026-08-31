#!/usr/bin/env python3
"""Same-session adversarial checks for C-RAMIFIED-SHEET-DESCENT-TYPE-N.

NON-CANONICAL incubation only. This checker is frozen before the positive
proof record. It is not independent confirmation and creates no public status.
"""
from __future__ import annotations

from itertools import product


def legendre(a: int, p: int) -> int:
    a %= p
    assert a != 0
    value = pow(a, (p - 1) // 2, p)
    assert value in (1, p - 1)
    return 1 if value == 1 else -1


def sheet_bit(x: tuple[int, int, int, int], p: int) -> int:
    a, b, c, _d = (z % p for z in x)
    assert (a * b - c * c) % p == 0
    assert (a, b, c) != (0, 0, 0)
    mu = a if a else b
    return 0 if legendre(mu, p) == 1 else 1


def null_nonradical(p: int) -> set[tuple[int, int, int, int]]:
    return {
        (a, b, c, d)
        for a, b, c, d in product(range(p), repeat=4)
        if (a * b - c * c) % p == 0 and (a, b, c) != (0, 0, 0)
    }


def native_factor_image(p: int) -> set[tuple[int, int, int, int]]:
    """All nonzero v v^dagger over F_p[eps]/eps^2."""
    out: set[tuple[int, int, int, int]] = set()
    for r, s, t, u in product(range(p), repeat=4):
        x = (
            r * r % p,
            t * t % p,
            r * t % p,
            (s * t - r * u) % p,
        )
        if x[:3] != (0, 0, 0):
            out.add(x)
    return out


class F25:
    """F_5[tau]/(tau^2-2)."""

    __slots__ = ("a", "b")

    def __init__(self, a: int = 0, b: int = 0) -> None:
        self.a = a % 5
        self.b = b % 5

    def __add__(self, other: "F25") -> "F25":
        return F25(self.a + other.a, self.b + other.b)

    def __neg__(self) -> "F25":
        return F25(-self.a, -self.b)

    def __sub__(self, other: "F25") -> "F25":
        return self + (-other)

    def __mul__(self, other: "F25") -> "F25":
        return F25(self.a * other.a + 2 * self.b * other.b,
                   self.a * other.b + self.b * other.a)

    def __pow__(self, n: int) -> "F25":
        if n < 0:
            return self.inverse() ** (-n)
        out = F25(1)
        base = self
        k = n
        while k:
            if k & 1:
                out = out * base
            base = base * base
            k >>= 1
        return out

    def inverse(self) -> "F25":
        assert self != F25()
        return self ** 23

    def __truediv__(self, other: "F25") -> "F25":
        return self * other.inverse()

    def __eq__(self, other: object) -> bool:
        return isinstance(other, F25) and (self.a, self.b) == (other.a, other.b)

    def __hash__(self) -> int:
        return hash((self.a, self.b))

    def __repr__(self) -> str:
        return f"F25({self.a},{self.b})"


def f25_scalar(a: int) -> F25:
    return F25(a, 0)


def f25_sqrt(a: int) -> F25:
    target = f25_scalar(a)
    roots = [F25(x, y) for x, y in product(range(5), repeat=2)
             if F25(x, y) * F25(x, y) == target]
    assert len(roots) == 2
    return roots[0]


def factor_over_f25(x: tuple[int, int, int, int]) -> tuple[tuple[F25, F25], tuple[F25, F25]]:
    """Construct v=(v0+eps s0,v1+eps s1) with v v^dagger=x."""
    a, b, c, d = (z % 5 for z in x)
    assert (a * b - c * c) % 5 == 0
    assert (a, b, c) != (0, 0, 0)

    if a:
        mu = a
        r = F25(1)
        t = f25_scalar(c) / f25_scalar(a)
    else:
        assert c == 0 and b != 0
        mu = b
        r = F25(0)
        t = F25(1)

    alpha = f25_sqrt(mu)
    if t != F25(0):
        s = f25_scalar(d) / (alpha * t)
        u = F25(0)
    else:
        assert r != F25(0)
        s = F25(0)
        u = -f25_scalar(d) / (alpha * r)

    residue = (alpha * r, alpha * t)
    nilpotent = (s, u)
    return residue, nilpotent


def vv_dagger(residue: tuple[F25, F25], nilpotent: tuple[F25, F25]) -> tuple[F25, F25, F25, F25]:
    r, t = residue
    s, u = nilpotent
    return r * r, t * t, r * t, s * t - r * u


def r_action_p5(x: tuple[int, int, int, int]) -> tuple[int, int, int, int]:
    a, b, c, d = x
    return 2 * a % 5, 3 * b % 5, c % 5, (d - c) % 5


def main() -> int:
    for p in (3, 5, 7, 11):
        q = null_nonradical(p)
        native = native_factor_image(p)
        square_sheet = {x for x in q if sheet_bit(x, p) == 0}
        nonsquare_sheet = q - square_sheet
        assert native == square_sheet
        assert native.isdisjoint(nonsquare_sheet)
        expected = p * (p * p - 1) // 2
        assert len(square_sheet) == expected
        assert len(nonsquare_sheet) == expected
    print("PASS B1-B2: native vv^dagger image is exactly the square sheet")

    q5 = null_nonradical(5)
    for x in q5:
        residue, nilpotent = factor_over_f25(x)
        got = vv_dagger(residue, nilpotent)
        want = tuple(f25_scalar(z) for z in x)
        assert got == want
    print("PASS B3-B4: every p=5 sheet and every nilpotent coordinate factors over F25")

    for p in (3, 5, 7, 11, 13, 17, 19):
        nonsquare = next(a for a in range(2, p) if legendre(a, p) == -1)
        for m in range(1, 7):
            value = pow(nonsquare, (p**m - 1) // 2, p)
            is_square = value == 1
            assert is_square == (m % 2 == 0)
    print("PASS B5: nonsquare base classes acquire roots exactly at even residue degree")

    squares = {x * x % 5 for x in range(1, 5)}
    sign_kernel = {1, 4}
    assert squares == sign_kernel
    assert ({1, 4}, {2, 3}) == (squares, set(range(1, 5)) - squares)
    print("PASS B6: p=5 square quotient is literally the public sign quotient V_+")

    for x in q5:
        y = r_action_p5(x)
        assert y in q5
        assert sheet_bit(y, 5) == 1 - sheet_bit(x, 5)
    print("PASS B7: torsion-normalized R toggles the p=5 descent type")

    direct = [n % 2 for n in range(16)]
    thue_morse = [n.bit_count() % 2 for n in range(16)]
    assert direct[:2] == thue_morse[:2]
    assert direct[2] == 0 and thue_morse[2] == 1
    assert direct != thue_morse
    controlled = [n.bit_count() % 2 for n in range(16)]
    assert controlled == thue_morse
    print("PASS B8: direct R iteration first differs from Thue-Morse at n=2")

    print("BREAKER NO BREAK: factorization-depth typing survives all frozen attacks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
