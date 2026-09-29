#!/usr/bin/env python3
"""Exact audit for C-PHOTON-CONTACT-SOURCE-OPT-N.

PUBLIC, NON-CANONICAL. Standard library only.
Author: A. M. Thorn <thorn@twistj.com>
License: Apache-2.0.
"""

from fractions import Fraction


def source_constants(t: int):
    a = Fraction((t*t + 1)**6, 64 * t**11)
    r = Fraction(2 * (t**4 + 1), (t*t + 1)**2)
    s = Fraction(4 * t*t, (t*t + 1)**2)

    # Independent cleared-denominator checks from
    # exp(-5 log t) cosh(log t)^6,
    # 1+tanh(log t)^2,
    # cosh(log t)^(-2).
    assert 64 * t**11 * a.numerator == (t*t + 1)**6 * a.denominator
    assert r == 1 + Fraction((t*t - 1)**2, (t*t + 1)**2)
    assert s == Fraction(1, 1) - Fraction((t*t - 1)**2, (t*t + 1)**2)
    assert 0 < s < 1 < r < 2
    return a, r, s


def certificate_power(t: int, k: int) -> Fraction:
    a, r, _ = source_constants(t)
    qbase = a * (1 + 6*r)
    return qbase**24 * r**k


def main():
    best = None
    all_rows = []

    for k in range(24, -1, -1):
        passing = []
        for t in range(2, 33):
            cert = certificate_power(t, k)
            if cert < 1:
                passing.append((cert, t))
        if passing:
            passing.sort(key=lambda x: (x[0], x[1]))
            cert, t = passing[0]
            best = (k, t, cert, len(passing))
            break

    assert best is not None
    k, t, cert, count = best
    rho = Fraction(k, 24)

    # Frozen special rho=1/2.
    khalf = 12
    half = []
    for tt in range(2, 33):
        cc = certificate_power(tt, khalf)
        if cc < 1:
            half.append((cc, tt))
    if half:
        half.sort(key=lambda x: (x[0], x[1]))
        half_cert, half_t = half[0]
        half_text = f"PASS t={half_t} cert24={half_cert}"
    else:
        half_text = "FAIL"

    print(
        "GRID PASS "
        f"rho={rho} k={k} best_t={t} passing_t_count={count} cert24={cert}"
    )
    print(f"RHO_HALF {half_text}")

    for tt in range(2, 33):
        a, r, s = source_constants(tt)
        if tt in (2, 3, t, 32):
            print(f"SOURCE t={tt} a={a} r={r} s={s}")

    # Maximality on the frozen density grid.
    for kk in range(k+1, 25):
        assert all(certificate_power(tt, kk) >= 1 for tt in range(2,33))

    assert cert < 1
    print("AUDIT PASS; source_grid_optimized=YES; full_Xi=OPEN; P1=OPEN")


if __name__ == "__main__":
    main()
