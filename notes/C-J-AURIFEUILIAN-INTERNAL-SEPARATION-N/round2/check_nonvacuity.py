#!/usr/bin/env python3
"""Exposed integer certificates; see NONVACUITY_PREREG.md."""

import json
from math import gcd


def bezout(a, b):
    old_r, r = a, b
    old_x, x = 1, 0
    old_y, y = 0, 1
    while r:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_x, x = x, old_x - q * x
        old_y, y = y, old_y - q * y
    assert old_r == gcd(a, b)
    assert old_x * a + old_y * b == old_r
    return old_r, old_x, old_y


def main():
    f, next_f = 0, 1
    for _ in range(125):
        f, next_f = next_f, f + next_f
    supplied = (
        (-1, 2775001, 6362780164662187387605023763432934660589177501),
        (1, 13181501253515178490001, 1339507616024322442312867213751),
    )
    cases = []
    for sigma, left, right in supplied:
        n = 5 * f * f + 5 * sigma * f + 1
        assert left > 1 and right > 1
        assert left * right == n
        divisor, x, y = bezout(left, right)
        assert divisor == 1
        cases.append({
            "sigma": sigma, "A": str(n), "left": str(left),
            "right": str(right), "bezout_left": str(x),
            "bezout_right": str(y),
        })
    print(json.dumps({"cases": cases}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
