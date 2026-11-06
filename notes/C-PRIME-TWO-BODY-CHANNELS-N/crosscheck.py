#!/usr/bin/env python3
"""Same-session second algorithm in doubled trace coordinates; not blind review."""
from collections import defaultdict
from fractions import Fraction as R
from hashlib import sha256
from math import gcd, isqrt, lcm


def to_trace(ab):
    a, b = ab
    return 2*a+b, b


def to_coeff(tb):
    t, b = tb
    return (R(t)-R(b))/2, R(b)


def norm(tb):
    t, b = tb
    return (R(t)*t - 5*R(b)*b)/4


def positive(tb):
    return tb[0] > 0 and norm(tb) > 0


def lattice(tb):
    a, b = to_coeff(tb)
    return a.denominator == b.denominator == 1


def denom(tb):
    return lcm(*(t.denominator for t in to_coeff(tb)))


def exhaustive(z):
    tz, bz = z
    out = defaultdict(set)
    for t in range(1, tz):
        for b in range(-t+1, t):
            if (t-b) % 2:
                continue
            rest = (tz-t, bz-b)
            if positive((t, b)) and positive(rest):
                r, s = int(norm((t, b))), int(norm(rest))
                out[(r, s)].add(((t-b)//2, b))
    return out


def solve(z, r, s):
    tz, bz = z
    T = int(norm(z))
    D = T+r-s
    delta = D*D-4*T*r
    if D <= 0 or D >= 2*T or delta < 0 or delta % 5:
        return set()
    u = isqrt(delta//5)
    if 5*u*u != delta:
        return set()
    out = set()
    for v in {-u, u}:
        nt, nb = tz*D+5*bz*v, bz*D+tz*v
        divisor = 2*T
        if nt % divisor or nb % divisor:
            continue
        t, b = nt//divisor, nb//divisor
        if (t-b) % 2:
            continue
        assert positive((t, b)) and positive((tz-t, bz-b))
        assert norm((t, b)) == r and norm((tz-t, bz-b)) == s
        out.add(((t-b)//2, b))
    return out


def mirror(z, x):
    tz, bz = z
    tx, bx = x
    denominator = 4*norm(z)
    a = tz*tz+5*bz*bz
    return ((a*tx-10*tz*bz*bx)/denominator,
            (2*tz*bz*tx-a*bx)/denominator)


def prime_support(d):
    p = 2
    ans = []
    while p*p <= d:
        if d % p == 0:
            ans.append(p)
        while d % p == 0:
            d //= p
        p += 1
    if d > 1:
        ans.append(d)
    return ans


def reflected_when_lattice(z, x):
    m = mirror(z, x)
    return m if lattice(m) else x


def main():
    box = [(a, b) for a in range(1, 9) for b in range(-8, 9)
           if positive(to_trace((a, b)))]
    ledger = sha256()
    tests = present = points = 0
    cards = [0, 0, 0]
    for ab in box:
        z = to_trace(ab)
        brute = exhaustive(z)
        T = int(norm(z))
        for r in range(1, T):
            for s in range(1, T):
                got = solve(z, r, s)
                assert got == brute.get((r, s), set()), ('trace channel', ab, r, s)
                assert len(got) <= 2
                tests += 1
                present += bool(got)
                points += len(got)
                cards[len(got)] += 1
                tail = ';'.join(f'{a},{b}' for a, b in sorted(got))
                ledger.update(f'{ab[0]},{ab[1]}|{r},{s}|{tail}\n'.encode('ascii'))
    print(f'G1 PASS totals={len(box)} norm_pairs={tests} admitted={present} states={points}')
    print('CHANNEL_CARDINALITIES ' + ','.join(map(str, cards)))
    print('CHANNEL_LEDGER_SHA256 ' + ledger.hexdigest())
    pairs = admitted = distinct = 0
    for a in box:
        for b in box:
            x, y = to_trace(a), to_trace(b)
            z = (x[0]+y[0], x[1]+y[1])
            mx, my = mirror(z, x), mirror(z, y)
            assert positive(mx) and positive(my)
            assert norm(mx) == norm(x) and norm(my) == norm(y)
            assert (mx[0]+my[0], mx[1]+my[1]) == z
            assert mirror(z, mx) == x and mirror(z, my) == y
            assert lattice(mx) == lattice(my)
            d = denom(mx)
            assert denom(my) == d and int(norm(z)) % d == 0
            assert all(p % 5 in (1, 4) for p in prime_support(d))
            out = reflected_when_lattice(z, x)
            assert reflected_when_lattice(z, out) == x
            pairs += 1
            admitted += lattice(mx)
            distinct += lattice(mx) and mx != x
    print(f'G2 PASS pairs={pairs} integral_reflections={admitted} distinct={distinct}')
    for c in range(1, 65):
        z = to_trace((c+1, c))
        T = c*c+3*c+1
        assert int(norm(z)) == T
        assert denom(mirror(z, (2, 0))) == T//gcd(T, 5)
    bad = solve(to_trace((18, 23)), 1, 181)
    good = solve(to_trace((15, -1)), 1, 181)
    assert bad == set() and (1, 0) in good
    assert to_coeff(mirror(to_trace((3, 2)), (2, 0))) == (R(13, 11), R(16, 11))
    assert to_coeff(mirror(to_trace((4, 3)), (2, 0))) == (R(25, 19), R(33, 19))
    print('G3 PASS family_c=1..64 blocked_209_channel=0 same_norm_control=allowed')
    z, x = (8, 0), (3, 1)
    assert mirror(z, x) == (3, -1) != x
    assert norm(x) == 1 and norm((5, -1)) == 5
    print('G4 PASS distinct_norm_preserving_maps=2 unequal_norm_witness=1,5')
    print('STATUS same-session second implementation; not independent review or second architecture')


if __name__ == '__main__':
    main()
