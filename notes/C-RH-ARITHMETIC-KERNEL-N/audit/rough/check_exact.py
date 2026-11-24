"""Integer comparison of the large-support direct and quotient formulas."""

from bisect import bisect_right
from itertools import accumulate
from math import isqrt


LIMIT = 8192
CHARACTER = (0, 1, -1, -1, 1)
CHARACTER_SUM = (0, 1, 0, -1, 0)


def cube_root_floor(value):
    lo, hi = 0, 1
    while hi**3 <= value:
        lo, hi = hi, 2 * hi
    while hi - lo > 1:
        midpoint = (lo + hi) // 2
        if midpoint**3 <= value:
            lo = midpoint
        else:
            hi = midpoint
    return lo


def trial_support(n):
    least = n
    weight = 1
    p = 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            if p % 5 not in (1, 4) or n % p == 0:
                return 0, 0
            least = min(least, p)
            weight *= -2
        p += 1
    if n > 1:
        if n % 5 not in (1, 4):
            return 0, 0
        least = min(least, n)
        weight *= -2
    return weight, least


def split_primes(limit):
    prime = [False, False] + [True] * (limit - 1)
    for p in range(2, isqrt(limit) + 1):
        if prime[p]:
            for multiple in range(p * p, limit + 1, p):
                prime[multiple] = False
    return [p for p in range(2, limit + 1) if prime[p] and CHARACTER[p % 5] == 1]


def products_from_sieve(primes, limit):
    support = {1: (1, limit + 1)}
    for p in reversed(primes):
        new_products = {
            d * p: (-2 * weight, p)
            for d, (weight, _) in support.items()
            if d * p <= limit
        }
        support.update(new_products)
    return support


def direct_values(x, ordered_support, trial_table):
    cutoff = cube_root_floor(x * x)
    left = bisect_right(ordered_support, cutoff)
    right = bisect_right(ordered_support, x)
    rough, complement = 0, 0
    for d in ordered_support[left:right]:
        weight, least = trial_table[d]
        term = weight * CHARACTER_SUM[(x // d) % 5]
        if least**3 > x:
            rough += term
        else:
            complement += term
    return rough, complement, rough + complement


def rough_quotients(x, primes):
    cutoff = cube_root_floor(x * x)
    least_cutoff = cube_root_floor(x)
    q_bound = cube_root_floor(x - 1)
    pi_cutoff = bisect_right(primes, cutoff)
    first_p = bisect_right(primes, least_cutoff)
    total = 0
    for j in range(1, q_bound + 1):
        y = x // j
        prime_count = bisect_right(primes, y) - pi_cutoff
        upper_p = bisect_right(primes, isqrt(y))
        semiprime_count = sum(
            bisect_right(primes, y // primes[i]) - i - 1
            for i in range(first_p, upper_p)
        )
        total += CHARACTER[j % 5] * (-2 * prime_count + 4 * semiprime_count)
    return total


def complement_quotients(x, prefixes):
    cutoff = cube_root_floor(x * x)
    q_bound = cube_root_floor(x - 1)
    total = 0
    for p, prefix in prefixes.items():
        if p**3 <= x:
            base = prefix[cutoff // p]
            total -= 2 * sum(
                CHARACTER[j % 5] * (prefix[x // (p * j)] - base)
                for j in range(1, q_bound + 1)
            )
    return total


def main():
    trial_table = {n: trial_support(n) for n in range(2, LIMIT + 1)}
    trial_table = {n: term for n, term in trial_table.items() if term[0]}
    primes = split_primes(LIMIT)
    sieve_support = products_from_sieve(primes, LIMIT)
    assert trial_table == {d: term for d, term in sieve_support.items() if d > 1}
    ordered_support = sorted(trial_table)
    prefixes = {}
    for p in primes:
        if p**3 > LIMIT:
            break
        values = [0] * (LIMIT + 1)
        for e, (weight, least) in sieve_support.items():
            if least > p:
                values[e] = weight
        prefixes[p] = list(accumulate(values))
    for x in range(1, LIMIT + 1):
        rough, complement, total = direct_values(x, ordered_support, trial_table)
        grouped_rough = rough_quotients(x, primes)
        grouped_complement = complement_quotients(x, prefixes)
        assert (rough, complement, total) == (
            grouped_rough, grouped_complement, grouped_rough + grouped_complement
        )
    print(f"PASS independent factorization/product census and B,H,R through {LIMIT}")

    p = 19
    n = 6 * p
    assert p**3 > n and p**3 <= n * n
    outer_shift = trial_table[p][0] * CHARACTER_SUM[(n // p) % 5]
    assert outer_shift == -2
    print(f"FIRE omitted outer cutoff, d={p}, N={n}, signed support shift {outer_shift:+d}")

    p = 11
    d = p * 19
    n = p**3
    assert trial_table[d][1]**3 == n and d**3 > n * n
    inner_shift = trial_table[d][0] * CHARACTER_SUM[(n // d) % 5]
    assert inner_shift == 4
    print(f"FIRE nonstrict least-prime cutoff, d={d}, N={n}, signed support shift {inner_shift:+d}")


if __name__ == "__main__":
    main()
