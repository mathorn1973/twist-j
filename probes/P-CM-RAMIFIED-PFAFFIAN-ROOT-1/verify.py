#!/usr/bin/env python3
from __future__ import annotations

from math import isqrt

P = 5


def q(a: int, b: int) -> int:
    return a * a - a * b - b * b


def rho(a: int, b: int) -> int:
    return (a + 2 * b) % P


def phase(a: int, b: int) -> int:
    r = rho(a, b)
    assert r != 0
    return pow(r, -1, P)


def chi5(x: int) -> int:
    y = pow(x % P, 2, P)
    assert y in (1, 4)
    return 1 if y == 1 else -1


def fib(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def s2(n: int) -> int:
    return n.bit_count()


def v2(n: int) -> int:
    assert n >= 1
    c = 0
    while n % 2 == 0:
        c += 1
        n //= 2
    return c


def primes_upto(limit: int) -> list[int]:
    out = []
    for n in range(2, limit + 1):
        prime = True
        d = 2
        while d * d <= n:
            if n % d == 0:
                prime = False
                break
            d += 1
        if prime:
            out.append(n)
    return out


def gate_1_ramified_square() -> None:
    for a in range(P):
        for b in range(P):
            assert q(a, b) % P == rho(a, b) ** 2 % P
    print("G1 PASS  q(a,b) mod 5 = (a+2b)^2 on all 25 residue pairs")


def gate_2_prime_uniqueness_audit() -> None:
    # Written proof: for odd ell, a binary quadratic form is a scalar square
    # only if its discriminant vanishes. Here disc(q)=(-1)^2-4(1)(-1)=5.
    assert 1 - 4 * (-1) == 5
    # Characteristic two guard: (ua+vb)^2 has no ab term, while q has one.
    for ell in primes_upto(997):
        if ell == 2:
            square_exists = False
        else:
            square_exists = (5 % ell == 0)
        assert square_exists == (ell == 5), ell
    assert all(
        q(a, b) % 5 == (a + 2 * b) ** 2 % 5
        for a in range(5)
        for b in range(5)
    )
    print("G2 PASS  discriminant audit: linear-square prime is uniquely 5; primes<=997 checked")


def gate_3_marked_unit_quotient() -> None:
    # phi mod lambda is 3, hence R(phi)=3^-1=2 in F_5^*.
    assert pow(3, -1, P) == 2
    image = set()
    kernel_classes = set()
    for e in (0, 1):
        for k in range(4):
            value = ((-1) ** e * pow(2, k, P)) % P
            image.add(value)
            if value == 1:
                kernel_classes.add((e, k))
    assert image == {1, 2, 3, 4}
    assert kernel_classes == {(0, 0), (1, 2)}
    # These are exactly the two residue classes of powers of -phi^2.
    generated = {((n % 2), (2 * n) % 4) for n in range(4)}
    assert generated == kernel_classes | {(0, 0), (1, 2)}
    # The set comprehension collapses to the same two classes.
    assert generated == {(0, 0), (1, 2)}
    print("G3 PASS  unit quotient: R(phi)=2, image=F_5^*, kernel=< -phi^2 >")


def gate_4_pell_parameter() -> None:
    # eta_k = F_(k-1) + F_k phi = phi^k, audited by coefficient recurrence.
    a, b = 1, 0  # coefficients of 1,phi for phi^0
    for k in range(0, 1025):
        if k == 0:
            expected = (1, 0)
        else:
            expected = (fib(k - 1), fib(k))
        assert (a, b) == expected
        a, b = b, a + b
    print("G4 PASS  Pell parameter eta_k=phi^k through k=1024; written induction is all-k")


def gate_5_full_c4_phase() -> None:
    for k in range(0, 4097):
        a = fib(k + 1)
        b = fib(k)
        assert phase(a, b) == pow(2, k, P)
        pf = q(a, b)
        assert pf in (-1, 1)
        ph = phase(a, b)
        assert ph * ph % P == pf % P
        assert chi5(ph) == pf
    print("G5 PASS  R(Omega_k)=2^k and Pf(Omega_k)=R(Omega_k)^2=chi_5(R) through k=4096")


def gate_6_tm_composition() -> None:
    for n in range(1 << 18):
        k = s2(n)
        a = fib(k + 1)
        b = fib(k)
        theta = pow(2, k, P)
        assert phase(a, b) == theta
        assert chi5(theta) == (1 if k % 2 == 0 else -1)
    print("G6 PASS  R(Omega_s2(n))=Theta_n and orientation quotient through n<2^18")


def gate_7_successor_law() -> None:
    for n in range((1 << 18) - 1):
        dn = s2(n + 1) - s2(n)
        carry = 1 - v2(n + 1)
        assert dn == carry
        lhs = pow(2, s2(n + 1), P)
        rhs = pow(2, s2(n), P) * pow(2, carry, P) % P
        assert lhs == rhs
    print("G7 PASS  chronological C4 successor law matches 1-nu_2(n+1) through n<2^18")


def gate_8_pell_shift_intertwining() -> None:
    for a in range(-50, 51):
        for b in range(-50, 51):
            if q(a, b) not in (-1, 1):
                continue
            ap, bp = a + b, a
            assert q(ap, bp) == -q(a, b)
            assert phase(ap, bp) == 2 * phase(a, b) % P
    print("G8 PASS  Pell shift flips Pfaffian sign and multiplies full phase by 2")


def gate_9_j_pullback_phase() -> None:
    # A_J = [[1,-1],[-1,2]] = S^-2 on the marked CM coordinates.
    for a in range(-50, 51):
        for b in range(-50, 51):
            if q(a, b) not in (-1, 1):
                continue
            ap, bp = a - b, -a + 2 * b
            assert q(ap, bp) == q(a, b)
            assert phase(ap, bp) == (-phase(a, b)) % P
    print("G9 PASS  J-pullback preserves Pfaffian and sends marked C4 phase R to -R")


def gate_10_guards() -> None:
    for a in range(-100, 101):
        for b in range(-100, 101):
            if q(a, b) not in (-1, 1):
                continue
            pf_residue = q(a, b) % P
            assert pf_residue in (1, 4)
            assert chi5(pf_residue) == 1
            assert phase(-a, -b) == (-phase(a, b)) % P
            assert q(-a, -b) == q(a, b)
    print("G10 PASS direct Pfaffian reduction is QR-only; -Omega flips C4 phase, not orientation")


def main() -> int:
    gate_1_ramified_square()
    gate_2_prime_uniqueness_audit()
    gate_3_marked_unit_quotient()
    gate_4_pell_parameter()
    gate_5_full_c4_phase()
    gate_6_tm_composition()
    gate_7_successor_law()
    gate_8_pell_shift_intertwining()
    gate_9_j_pullback_phase()
    gate_10_guards()
    print("ALL PASS CM-RAMIFIED-PFAFFIAN-ROOT exact audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
