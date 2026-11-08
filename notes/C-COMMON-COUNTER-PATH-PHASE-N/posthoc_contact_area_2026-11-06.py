#!/usr/bin/env python3
"""POSTHOC to RECON-PATH-PHASE-ONE-CARRIER, Part K. NON-CANONICAL, L1, exact.

Written after the frozen run showed that the whole area vector (A,B) mod 5,
not only its trace 2A+B, had no holonomy on the audited orbits. Exploratory:
nothing here was preregistered. Questions:
 P1  why: exact Galois-twisted coboundaries and an F5 rank certificate;
 P2  integer lattice of loop invariants (count, A, B) on complete orbits;
 P3  the explicit closed loop w * sigma^-1 at I_-2, replayed literally.
Own code path, standard library only, integers and Fractions only.
Usage: python3 -I -B posthoc_contact_area_2026-11-06.py <path to WORD.txt>
"""
from collections import deque
from fractions import Fraction as Fr
from hashlib import sha256
from itertools import combinations_with_replacement
import random
import sys

FAILS = []


def chk(name, cond, detail=""):
    print(("PASS " if cond else "FAIL ") + name + ((" " + detail) if detail else ""))
    if not cond:
        FAILS.append(name)


# ---------------------------------------------------------------- O = Z[j]
def red5(v5):
    return tuple(a - v5[4] for a in v5[:4])


def mul(x, y):
    acc = [0] * 5
    for i, a in enumerate(x):
        if a:
            for k, b in enumerate(y):
                acc[(i + k) % 5] += a * b
    return red5(acc)


def gal(a, x):
    """sigma_a: j -> j^a"""
    acc = [0] * 5
    for i, c in enumerate(x):
        acc[(a * i) % 5] += c
    return red5(acc)


def add(x, y):
    return tuple(a + b for a, b in zip(x, y))


def sub(x, y):
    return tuple(a - b for a, b in zip(x, y))


def sc(t, x):
    return tuple(t * a for a in x)


ONE = (1, 0, 0, 0)
RHO = (0, 0, 1, 0)
ZERO = (0, 0, 0, 0)


def contact(x, y):
    delta = sub(x, y)
    if any(a & 1 for a in delta):
        return x, y, False, False, None
    d = tuple(a // 2 for a in delta)
    s = tuple((a + b) // 2 for a, b in zip(x, y))
    r = mul(RHO, d)
    x2, y2 = add(s, r), sub(s, r)
    return x2, y2, True, (x2 != x or y2 != y), d


def AB(v):
    a0, a1, a2, a3 = v
    s1 = a0 * a1 + a1 * a2 + a2 * a3
    s2 = a0 * a2 + a1 * a3 + a0 * a3
    return a0 * a0 + a1 * a1 + a2 * a2 + a3 * a3 - s1, s1 - s2


# v * conj(v) = A + B phi with phi = -j^2 - j^3: cross-check AB against ring multiplication
rng = random.Random(11062026)
ok = True
for _ in range(2000):
    v = tuple(rng.randint(-9, 9) for _ in range(4))
    A, B = AB(v)
    ok &= mul(v, gal(4, v)) == (A, 0, -B, -B)
chk("AB(v) equals v*conj(v) = A + B*phi computed by ring multiplication", ok)

# ---------------------------------------------------------------- P1 exact coboundaries
ok = {1: True, 2: True, 3: True, 4: True}
trials = 0
for _ in range(20000):
    x = tuple(rng.randint(-9, 9) for _ in range(4))
    y = tuple(a - 2 * rng.randint(-4, 4) for a in x)
    x2, y2, admitted, changed, d = contact(x, y)
    assert admitted
    trials += 1
    for a in (1, 2, 3, 4):
        before = add(mul(x, gal(a, x)), mul(y, gal(a, y)))
        after = add(mul(x2, gal(a, x2)), mul(y2, gal(a, y2)))
        factor = sub(mul(RHO, gal(a, RHO)), ONE)               # rho*g(rho) - 1
        ok[a] &= sub(after, before) == sc(2, mul(factor, mul(d, gal(a, d))))
chk("P1 identity: Delta[x g(x) + y g(y)] = 2 (rho g(rho) - 1) d g(d) for g = sigma_1..sigma_4",
    all(ok.values()), "contacts=%d" % trials)
factors = {a: sub(mul(RHO, gal(a, RHO)), ONE) for a in (1, 2, 3, 4)}
print("   rho*g(rho)-1 in the power basis:", factors)
chk("P1 the factor vanishes exactly for complex conjugation only", factors[4] == ZERO and all(factors[a] != ZERO for a in (1, 2, 3)))

# quadratic forms on Z^4 as vectors of the 10 monomial coefficients a_i a_k, i<=k
MONO = list(combinations_with_replacement(range(4), 2))


def form_of(fn):
    """coefficient vectors (one per output coordinate) of a quadratic map Z^4 -> Z^m by interpolation"""
    e = [tuple(int(i == k) for i in range(4)) for k in range(4)]
    m = len(fn(e[0]))
    out = [[0] * 10 for _ in range(m)]
    for idx, (i, k) in enumerate(MONO):
        if i == k:
            val = fn(e[i])
            for c in range(m):
                out[c][idx] = val[c]
        else:
            vi, vk, vik = fn(e[i]), fn(e[k]), fn(add(e[i], e[k]))
            for c in range(m):
                out[c][idx] = vik[c] - vi[c] - vk[c]
    return out


exact_forms = []
for a in (1, 2, 3):
    exact_forms += form_of(lambda v, a=a: mul(v, gal(a, v)))
hermA, hermB = form_of(lambda v: AB(v))
ok = True
for _ in range(500):                                     # the interpolated forms reproduce the maps
    v = tuple(rng.randint(-6, 6) for _ in range(4))
    mon = [v[i] * v[k] for i, k in MONO]
    vals = []
    for a in (1, 2, 3):
        vals += list(mul(v, gal(a, v)))
    ok &= vals == [sum(c * m for c, m in zip(f, mon)) for f in exact_forms]
    ok &= AB(v) == (sum(c * m for c, m in zip(hermA, mon)), sum(c * m for c, m in zip(hermB, mon)))
chk("P1 interpolated coefficient vectors reproduce d*g(d) and (A,B)", ok)


def rank_q(rows):
    rows = [[Fr(a) for a in r] for r in rows]
    rk, col = 0, 0
    while rk < len(rows) and col < 10:
        piv = next((i for i in range(rk, len(rows)) if rows[i][col]), None)
        if piv is None:
            col += 1
            continue
        rows[rk], rows[piv] = rows[piv], rows[rk]
        for i in range(len(rows)):
            if i != rk and rows[i][col]:
                f = rows[i][col] / rows[rk][col]
                rows[i] = [a - f * b for a, b in zip(rows[i], rows[rk])]
        rk += 1
        col += 1
    return rk


def echelon_f5(rows):
    basis = []
    for r in rows:
        v = [a % 5 for a in r]
        for b in basis:
            piv = next(i for i, a in enumerate(b) if a)
            if v[piv]:
                f = v[piv] * pow(b[piv], -1, 5) % 5
                v = [(a - f * c) % 5 for a, c in zip(v, b)]
        if any(v):
            piv = next(i for i, a in enumerate(v) if a)
            inv = pow(v[piv], -1, 5)
            basis.append([a * inv % 5 for a in v])
    return basis


def in_span_f5(basis, r):
    v = [a % 5 for a in r]
    changed = True
    while changed:
        changed = False
        for b in basis:
            piv = next(i for i, a in enumerate(b) if a)
            if v[piv]:
                f = v[piv] * pow(b[piv], -1, 5) % 5
                v = [(a - f * c) % 5 for a, c in zip(v, b)]
                changed = True
    return not any(v)


rq_exact = rank_q(exact_forms)
rq_all = rank_q(exact_forms + [hermA, hermB])
bas5 = echelon_f5(exact_forms)
print("P1 rank over Q: exact forms d^2, d*s2(d), d*s3(d): %d ; with A and B added: %d (of 10 monomials)" % (rq_exact, rq_all))
print("P1 rank over F5 of the exact forms: %d ; A in span: %s ; B in span: %s"
      % (len(bas5), in_span_f5(bas5, hermA), in_span_f5(bas5, hermB)))
chk("P1 over Q the Hermitian forms A,B are independent of the exact forms (loop area can be nonzero)", rq_all == rq_exact + 2)
cert = in_span_f5(bas5, hermA) and in_span_f5(bas5, hermB)
chk("P1 CERTIFICATE: A mod 5 and B mod 5 lie in the F5 span of exact forms, so the Hermitian area of every closed contact loop is in 5 Z[phi]", cert)

# ---------------------------------------------------------------- P2 integer lattices on complete orbits
U = (1, -1, 0, 0)
B0 = (1, 0, -1, 0)
X = (1, 1, 0, -2)
TWO = (2, 0, 0, 0)


def prep(t):
    return (sc(t, B0), sc(-t, B0), U, U, X, TWO)


def target(t):
    return (add(U, sc(t, B0)), add(U, sc(-t, B0)), ZERO, ZERO, X, TWO)


def hnf_add(basis, v):
    """maintain an integer row echelon basis (list of rows) of the lattice spanned so far"""
    v = list(v)
    for idx in range(len(v)):
        if not any(v):
            break
        row = next((b for b in basis if next(i for i, a in enumerate(b) if a) == idx), None)
        if v[idx] == 0:
            continue
        if row is None:
            if v[idx] < 0:
                v = [-a for a in v]
            basis.append(v[:])
            basis.sort(key=lambda b: next(i for i, a in enumerate(b) if a))
            return
        while v[idx]:                                    # euclid on the pivot column
            if abs(row[idx]) > abs(v[idx]):
                row[:], v[:] = v[:], row[:]
            f = v[idx] // row[idx]
            v = [a - f * b for a, b in zip(v, row)]
        if row[idx] < 0:
            row[:] = [-a for a in row]
    return


def orbit_lattice(start, cap):
    n = len(start)
    pairs = [(i, k) for i in range(n) for k in range(i + 1, n)]
    pot = {start: (0, 0, 0, 0)}                  # integer potentials (Nchg, S, A, B) along the BFS tree
    queue = deque([start])
    basis, capped, ndef = [], False, 0
    while queue:
        st = queue.popleft()
        p = pot[st]
        for i, k in pairs:
            x2, y2, admitted, changed, d = contact(st[i], st[k])
            if not changed:
                continue
            a, b = AB(d)
            nl = list(st)
            nl[i], nl[k] = x2, y2
            nxt = tuple(nl)
            cand = (p[0] + 1, p[1] + 2 * a + b, p[2] + a, p[3] + b)
            have = pot.get(nxt)
            if have is None:
                if len(pot) >= cap:
                    capped = True
                    continue
                pot[nxt] = cand
                queue.append(nxt)
            else:
                df = tuple(c - h for c, h in zip(cand, have))
                if any(df):
                    ndef += 1
                    hnf_add(basis, df)
    return len(pot), capped, ndef, basis


for label, start, cap in (("I_0", prep(0), 10 ** 7), ("I_1", prep(1), 10 ** 7), ("I_-2", prep(-2), 200000)):
    size, capped, ndef, basis = orbit_lattice(start, cap)
    a_div = all(r[2] % 5 == 0 and r[3] % 5 == 0 for r in basis)
    s_div = all(r[1] % 5 == 0 for r in basis)
    print("P2 orbit %s states=%d%s nonzero integer defects=%d ; lattice basis rows (Nchg, S=sumQ, A, B): %s"
          % (label, size, " (CAPPED)" if capped else " (complete)", ndef, basis))
    chk("P2 %s every loop has S, A, B divisible by 5" % label, a_div and s_div)
    cnt = [r for r in basis if r[0] % 5]
    print("   count not divisible by 5 on some loop: %s" % bool(cnt))

# ---------------------------------------------------------------- P3 explicit closed loop
raw = open(sys.argv[1], "rb").read()
assert sha256(raw).hexdigest() == "6fed5cf015526726db5e47b060e583db00af77db21b54c5dbe47b79de78b65a7"
word = [(int(l[0]) - 1, int(l[1]) - 1) for l in raw.decode("ascii").split()]
perm = (1, 0, 2, 3, 4, 5)
sigma = [tuple(sorted((perm[i], perm[k]))) for i, k in word]
loop = word + [e for e in reversed(sigma) for _ in range(4)]
st = list(prep(-2))
mid = None
tot = [0, 0, 0, 0, 0]          # changed, admitted, S, A, B
for step, (i, k) in enumerate(loop, 1):
    x2, y2, admitted, changed, d = contact(st[i], st[k])
    if admitted:
        a, b = AB(d)
        tot[1] += 1
        tot[0] += int(changed)
        tot[2] += 2 * a + b
        tot[3] += a
        tot[4] += b
        st[i], st[k] = x2, y2
    if step == len(word):
        mid = tuple(st)
chk("P3 loop w then literal inverse of sigma(w): midpoint is G_-2 and the state returns to I_-2",
    mid == target(-2) and tuple(st) == prep(-2), "attempted contacts=%d" % len(loop))
print("P3 loop totals: changed=%d admitted=%d S=%d A=%d B=%d ; mod 5: changed=%d admitted=%d S=%d A=%d B=%d"
      % (tuple(tot) + tuple(t % 5 for t in tot)))
chk("P3 loop: count holonomy 2 mod 5 with S, A, B all 0 mod 5", tot[0] % 5 == 2 and tot[2] % 5 == 0 and tot[3] % 5 == 0 and tot[4] % 5 == 0)
print("RESULT", "PASS" if not FAILS else "FAIL", "fails=%d" % len(FAILS))
