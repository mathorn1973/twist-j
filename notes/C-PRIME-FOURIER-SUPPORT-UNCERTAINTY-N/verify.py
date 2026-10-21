#!/usr/bin/env python3
"""Exact checks for C-PRIME-FOURIER-SUPPORT-UNCERTAINTY-N.

NON-CANONICAL note, layer L1. Python standard library only, exact integer
arithmetic only, no floating point anywhere.

Ring model. Z[zeta_N] is represented as Z[x]/(Phi_N(x)) with Phi_N the
N-th cyclotomic polynomial, computed exactly. Phi_N is the minimal
polynomial of zeta_N, so an element is zero in Z[zeta_N] exactly when its
reduced coefficient vector is zero.

Fourier matrix. F_N = [zeta_N^(x k)] for x, k in Z/N. The transform used
for supports is fhat(k) = sum_x f(x) zeta_N^(-x k), i.e. the matrix
[zeta_N^(-x k)], which is the image of F_N under the Galois automorphism
zeta_N -> zeta_N^(-1).

Run from the repository root:
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
  python3 notes/C-PRIME-FOURIER-SUPPORT-UNCERTAINTY-N/verify.py
"""

from itertools import combinations, permutations
from math import comb
import sys


# ---------------------------------------------------------------- polynomials

def poly_divmod_monic(num, den):
    """Exact division of integer polynomials, den monic. Low-to-high lists."""
    num = list(num)
    q = [0] * max(1, len(num) - len(den) + 1)
    dd = len(den) - 1
    for i in range(len(num) - 1, dd - 1, -1):
        c = num[i]
        if c:
            q[i - dd] = c
            for j, d in enumerate(den):
                num[i - dd + j] -= c * d
    rem = num[:dd]
    return q, rem


_PHI = {}


def cyclotomic(n):
    """Phi_n as a low-to-high integer coefficient list."""
    if n in _PHI:
        return _PHI[n]
    poly = [-1] + [0] * (n - 1) + [1]  # x^n - 1
    for d in range(1, n):
        if n % d == 0:
            poly, rem = poly_divmod_monic(poly, cyclotomic(d))
            assert all(r == 0 for r in rem)
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    _PHI[n] = poly
    return poly


class Ring:
    """Z[zeta_n] as Z[x]/(Phi_n)."""

    def __init__(self, n):
        self.n = n
        self.phi = cyclotomic(n)
        self.deg = len(self.phi) - 1
        self.zero = (0,) * self.deg
        self.one = self.reduce([1])
        self.zp = [self.reduce([0] * e + [1]) for e in range(n)]

    def reduce(self, coeffs):
        _, rem = poly_divmod_monic(list(coeffs) + [0] * self.deg, self.phi)
        rem = rem + [0] * (self.deg - len(rem))
        return tuple(rem[: self.deg])

    def from_exponent_counts(self, counts):
        """sum_e counts[e] zeta^e, counts indexed by e in Z/n."""
        return self.reduce(counts)

    def add(self, a, b):
        return tuple(x + y for x, y in zip(a, b))

    def neg(self, a):
        return tuple(-x for x in a)

    def mul(self, a, b):
        c = [0] * (2 * self.deg)
        for i, x in enumerate(a):
            if x:
                for j, y in enumerate(b):
                    c[i + j] += x * y
        return self.reduce(c)

    def is_zero(self, a):
        return all(x == 0 for x in a)


# ---------------------------------------------------------------- minors

def perm_sign(p):
    s = 1
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if p[i] > p[j]:
                s = -s
    return s


_PERMS = {}


def signed_perms(k):
    if k not in _PERMS:
        _PERMS[k] = [(perm_sign(p), p) for p in permutations(range(k))]
    return _PERMS[k]


def fourier_minor(ring, rows, cols, orientation):
    """det [zeta^(orientation * r * c)] for r in rows, c in cols.

    Each Leibniz term is a single power of zeta, so the determinant is an
    integer combination of zeta^e; it is accumulated as exponent counts and
    reduced exactly modulo Phi_n.
    """
    n = ring.n
    counts = [0] * n
    for s, p in signed_perms(len(rows)):
        e = 0
        for i, r in enumerate(rows):
            e += orientation * r * cols[p[i]]
        counts[e % n] += s
    return ring.from_exponent_counts(counts)


def minor_census(n, orientation=1):
    ring = Ring(n)
    by_size = []
    zeros = 0
    for k in range(1, n + 1):
        total_k = 0
        for rows in combinations(range(n), k):
            for cols in combinations(range(n), k):
                total_k += 1
                if ring.is_zero(fourier_minor(ring, rows, cols, orientation)):
                    zeros += 1
        by_size.append(total_k)
    return by_size, zeros


# ---------------------------------------------------------------- transforms

def transform(ring, f):
    """fhat(k) = sum_x f(x) zeta^(-x k), f a list of ring elements."""
    n = ring.n
    out = []
    for k in range(n):
        acc = ring.zero
        for x in range(n):
            acc = ring.add(acc, ring.mul(f[x], ring.zp[(-x * k) % n]))
        out.append(acc)
    return out


def support(ring, vec):
    return sum(1 for v in vec if not ring.is_zero(v))


def integer_vector(ring, ints):
    return [ring.reduce([v]) for v in ints]


# ---------------------------------------------------------------- gates

results = []


def gate(name, ok, detail):
    results.append(ok)
    print(f"GATE {name} {'PASS' if ok else 'FAIL'} {detail}")


print("C-PRIME-FOURIER-SUPPORT-UNCERTAINTY-N verify")
print("arithmetic exact Z[x]/(Phi_N); no floating point")
r5 = Ring(5)
print("Phi_5 coefficients low-to-high " + ",".join(map(str, r5.phi)))

# G1: Chebotarev at p = 5, both orientations.
size5, zero5 = minor_census(5, 1)
size5c, zero5c = minor_census(5, -1)
total5 = sum(size5)
gate(
    "G1_P5_ALL_MINORS_NONZERO",
    zero5 == 0 and zero5c == 0 and total5 == comb(10, 5) - 1
    and size5 == [comb(5, k) ** 2 for k in range(1, 6)] and size5c == size5,
    f"minors={total5} by_size={','.join(map(str, size5))} "
    f"zero_F={zero5} zero_conjF={zero5c}",
)

# G2: the support deduction, mechanized. For every nonempty S and every T
# with |S|+|T| <= 5, some |S| x |S| minor of [zeta^(-x k)] with rows k in
# the complement of T and columns x in S is nonzero, hence no nonzero f
# supported in S has fhat supported in T.
pairs = 0
bad = 0
for s in range(1, 6):
    for S in combinations(range(5), s):
        for t in range(0, 6 - s):
            for T in combinations(range(5), t):
                pairs += 1
                comp = [k for k in range(5) if k not in T]
                rows = tuple(comp[:s])
                m = fourier_minor(r5, rows, S, -1)
                if r5.is_zero(m):
                    bad += 1
expected_pairs = sum(
    comb(5, s) * sum(comb(5, t) for t in range(0, 6 - s)) for s in range(1, 6)
)
gate(
    "G2_P5_SUPPORT_BOUND_6",
    bad == 0 and pairs == expected_pairs,
    f"(S,T)_pairs_with_|S|+|T|<=5={pairs} blocked={pairs - bad}",
)

# G3: sharpness. P_a(t) = prod_{k=1}^{a-1} (t - zeta^(-k)); f_a(x) is the
# coefficient of t^x. Then fhat_a vanishes at k = 1..a-1.
splits = []
ok3 = True
for a in range(1, 6):
    poly = [r5.one]
    for k in range(1, a):
        root = r5.zp[(-k) % 5]
        new = [r5.zero] * (len(poly) + 1)
        for i, c in enumerate(poly):
            new[i + 1] = r5.add(new[i + 1], c)
            new[i] = r5.add(new[i], r5.neg(r5.mul(c, root)))
        poly = new
    f = poly + [r5.zero] * (5 - len(poly))
    fh = transform(r5, f)
    sf, sfh = support(r5, f), support(r5, fh)
    splits.append(f"{sf}+{sfh}")
    ok3 = ok3 and sf == a and sfh == 6 - a
gate("G3_P5_SHARP_ALL_SPLITS", ok3, "splits=" + ",".join(splits))

# G4: attribution, other primes. Chebotarev holds for every prime; checked
# here for p = 2, 3, 7. The bound p + 1 is not special to five.
prime_detail = []
ok4 = True
for p in (2, 3, 7):
    sizes, zeros = minor_census(p, 1)
    prime_detail.append(f"p={p}:minors={sum(sizes)}:zero={zeros}")
    ok4 = ok4 and zeros == 0 and sum(sizes) == comb(2 * p, p) - 1
gate("G4_PRIMES_2_3_7_ALL_MINORS_NONZERO", ok4, " ".join(prime_detail))

# G5: composite boundary. For N = 4 and N = 6 vanishing minors exist and the
# subgroup indicator beats the prime bound N + 1.
comp_detail = []
ok5 = True
for n, ints in ((4, [1, 0, 1, 0]), (6, [1, 0, 0, 1, 0, 0])):
    ring = Ring(n)
    sizes, zeros = minor_census(n, 1)
    f = integer_vector(ring, ints)
    fh = transform(ring, f)
    sf, sfh = support(ring, f), support(ring, fh)
    comp_detail.append(
        f"N={n}:minors={sum(sizes)}:zero={zeros}:subgroup_split={sf}+{sfh}"
    )
    ok5 = ok5 and zeros > 0 and sf + sfh <= n
gate("G5_COMPOSITE_4_6_BOUND_FAILS", ok5, " ".join(comp_detail))

passed = sum(1 for r in results if r)
print(f"VERDICT {passed}/{len(results)} {'PASS' if passed == len(results) else 'FAIL'}")
sys.exit(0 if passed == len(results) else 1)
