#!/usr/bin/env python3
"""Check of the written proof of the loop-area theorem. Exact arithmetic in O/5 = F5[j]/(j-1)^4.
With l = log j = -(u + u^2/2 + u^3/3), u = 1 - j: sigma_a(l) = a*l, the powers 1,l,l^2,l^3 are a basis,
and for d = sum d_m l^m the l^k coefficient of d*sigma_a(d) is sum_(m+n=k) d_m d_n a^n."""
from itertools import product
import random


def red5(v5):
    return tuple((a - v5[4]) % 5 for a in v5[:4])


def mul(x, y):
    acc = [0] * 5
    for i, a in enumerate(x):
        for k, b in enumerate(y):
            acc[(i + k) % 5] += a * b
    return red5(acc)


def gal(a, x):
    acc = [0] * 5
    for i, c in enumerate(x):
        acc[(a * i) % 5] += c
    return red5(acc)


def add(x, y):
    return tuple((a + b) % 5 for a, b in zip(x, y))


def sc(t, x):
    return tuple(t * a % 5 for a in x)


ONE = (1, 0, 0, 0)
u = (1, 4, 0, 0)                                   # 1 - j mod 5
u2, u3 = mul(u, u), mul(mul(u, u), u)
assert mul(u3, u) == (0, 0, 0, 0)                  # u is nilpotent of index 4 modulo 5
inv = lambda n: pow(n, -1, 5)
ell = sc(-1, add(add(u, sc(inv(2), u2)), sc(inv(3), u3)))
ok = all(gal(a, ell) == sc(a, ell) for a in (1, 2, 3, 4))
print("PASS" if ok else "FAIL", "sigma_a(l) = a*l in O/5 for a = 1..4")
P = [ONE, ell, mul(ell, ell), mul(mul(ell, ell), ell)]
vecs = {}
for c in product(range(5), repeat=4):
    v = (0, 0, 0, 0)
    for cm, pm in zip(c, P):
        v = add(v, sc(cm, pm))
    vecs[v] = c
print("PASS" if len(vecs) == 625 else "FAIL", "1, l, l^2, l^3 is a basis of O/5")
rng = random.Random(5)
ok = True
for _ in range(3000):
    dint = tuple(rng.randint(-20, 20) for _ in range(4))
    d = tuple(a % 5 for a in dint)
    dm = vecs[d]
    for a in (1, 2, 3, 4):
        got = vecs[mul(d, gal(a, d))]
        want = tuple(sum(dm[m] * dm[k - m] * pow(a, k - m, 5) for m in range(k + 1)) % 5 for k in range(4))
        ok &= got == want
    herm = vecs[mul(d, gal(4, d))]
    ok &= herm == (dm[0] ** 2 % 5, 0, (2 * dm[0] * dm[2] - dm[1] ** 2) % 5, 0)
print("PASS" if ok else "FAIL", "coefficient formula; d*conj(d) = d0^2 + (2 d0 d2 - d1^2) l^2 modulo 5")
# exact pieces: d1^2 = (l^2 coefficient of d*sigma_2(d))/2 ; d0 d2 = (l^2 coefficient of d^2 - d1^2)/2
ok = True
for _ in range(3000):
    d = tuple(rng.randint(0, 4) for _ in range(4))
    dm = vecs[d]
    c1 = vecs[mul(d, d)]
    c2 = vecs[mul(d, gal(2, d))]
    d1sq = c2[2] * inv(2) % 5
    d0d2 = (c1[2] - d1sq) * inv(2) % 5
    ok &= d1sq == dm[1] ** 2 % 5 and d0d2 == dm[0] * dm[2] % 5 and c1[0] == dm[0] ** 2 % 5
print("PASS" if ok else "FAIL", "d0^2, d1^2 and d0*d2 are combinations of coefficients of d^2 and d*sigma_2(d)")
