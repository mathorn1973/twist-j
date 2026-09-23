#!/usr/bin/env python3
"""Exact review witness for an overbroad WLS reachability statement.

Uses rounded Gaussian-control means printed in the supplied audit, regarded
as exact rational INPUT DATA, not exact Maxwell expectations. Changes the
assumed standard-error profile. This is outside the incubation prereg's
constant-relative-error family and does NOT fire its frozen falsifier.
All inequalities are exact. No production run or public probe is executed.
"""
from fractions import Fraction as F

L = (12, 16, 24, 32)
Y = tuple(F(n, 10**7) for n in (4957806, 3853003, 2326458, 1403118))
SE = (F(1, 1000), F(1, 1000), F(1, 20), F(1, 20))

def fit(power: int, errors: tuple[F, ...]) -> tuple[F, F]:
    x = tuple(F(1, n**power) for n in L)
    w = tuple(1 / e**2 for e in errors)
    a = sum(w)
    b = sum(ww * xx for ww, xx in zip(w, x))
    c = sum(ww * xx**2 for ww, xx in zip(w, x))
    d = sum(ww * yy for ww, yy in zip(w, Y))
    e = sum(ww * xx * yy for ww, xx, yy in zip(w, x, Y))
    det = a*c - b*b
    assert det > 0
    return (c*d - b*e)/det, c/det

def main() -> None:
    print('Independent NON-CANONICAL review: WLS error-profile sensitivity')
    print('Input means:', ', '.join(map(str, Y)))
    print('Input standard errors:', ', '.join(map(str, SE)))
    for power in (1, 2):
        b0, v0 = fit(power, SE)
        positive = b0 > 0 and b0*b0 > 100*v0
        print(f'M{power}: intercept={b0}; variance={v0}')
        print(f'M{power}: intercept > 10 * SE(intercept): {positive}')
        assert positive
    baseline = tuple(yy/100 for yy in Y)
    b1, _ = fit(1, baseline)
    b2, _ = fit(2, baseline)
    assert b1 < 0 < b2
    print('Original constant-relative-error profile: M1 negative, M2 positive')
    print('No falsifier of the original restricted audit is claimed.')
    print('RESULT PASS')

if __name__ == '__main__':
    main()
