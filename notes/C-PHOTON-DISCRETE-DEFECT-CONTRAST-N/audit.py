#!/usr/bin/env python3
"""
Exact audit for C-PHOTON-DISCRETE-DEFECT-CONTRAST-N.

PUBLIC, NON-CANONICAL. This is an algebra audit only. It does not test a
thermodynamic limit or close P1.

Standard library only. No floating point.
"""

from __future__ import annotations

from itertools import product

P = 5

# Z[zeta_5] in the basis 1,z,z^2,z^3 with
# z^4 = -1-z-z^2-z^3.
R = tuple[int, int, int, int]
ZERO: R = (0, 0, 0, 0)
ONE: R = (1, 0, 0, 0)


def add(x: R, y: R) -> R:
    return tuple(x[i] + y[i] for i in range(4))  # type: ignore[return-value]


def neg(x: R) -> R:
    return tuple(-v for v in x)  # type: ignore[return-value]


def sub(x: R, y: R) -> R:
    return add(x, neg(y))


def scale(n: int, x: R) -> R:
    return tuple(n * v for v in x)  # type: ignore[return-value]


def mul(x: R, y: R) -> R:
    c = [0] * 7
    for i, a in enumerate(x):
        for j, b in enumerate(y):
            c[i + j] += a * b
    for k in range(6, 3, -1):
        a = c[k]
        if a:
            # z^k = -(z^(k-4)+z^(k-3)+z^(k-2)+z^(k-1))
            c[k - 4] -= a
            c[k - 3] -= a
            c[k - 2] -= a
            c[k - 1] -= a
            c[k] = 0
    return tuple(c[:4])  # type: ignore[return-value]


ZPOW: tuple[R, ...] = (
    (1, 0, 0, 0),
    (0, 1, 0, 0),
    (0, 0, 1, 0),
    (0, 0, 0, 1),
    (-1, -1, -1, -1),
)


def zpow(k: int) -> R:
    return ZPOW[k % 5]


def conj(x: R) -> R:
    out = ZERO
    for i, a in enumerate(x):
        out = add(out, scale(a, zpow(-i)))
    return out


def gal(x: R, r: int) -> R:
    out = ZERO
    for i, a in enumerate(x):
        out = add(out, scale(a, zpow(r * i)))
    return out


def W(f: int) -> R:
    return add(scale(2, ONE), add(zpow(f), zpow(-f)))


def to_phi(x: R) -> tuple[int, int]:
    # phi = -z^2-z^3, so A+B*phi = (A,0,-B,-B).
    a0, a1, a2, a3 = x
    assert a1 == 0
    assert a2 == a3
    return a0, -a2


def from_phi(a: int, b: int) -> R:
    return (a, 0, -b, -b)


# ---------------------------------------------------------------------------
# 1. Local exact finite difference in Z[zeta_5].
# ---------------------------------------------------------------------------

local_checks = 0
for f in range(5):
    for r in (1, 2):
        lhs = sub(W(f + r), W(f - r))
        rhs = mul(sub(zpow(r), zpow(-r)), sub(zpow(f), zpow(-f)))
        assert lhs == rhs
        local_checks += 1

assert local_checks == 10
print("LOCAL_DIFF PASS checks=10")


# ---------------------------------------------------------------------------
# 2. Frozen toy incidence complex over F_5.
#
# D maps two link variables to three plaquette variables:
#   f0=a0, f1=a1, f2=a0-a1.
# Boundary is D^T on binary plaquette chains.
# ---------------------------------------------------------------------------

D = (
    (1, 0),
    (0, 1),
    (1, -1),
)
E = 2
NP = 3
LINKS = tuple(product(range(5), repeat=E))
CHAINS = tuple(product((0, 1), repeat=NP))
SOURCES = tuple(product(range(5), repeat=NP))


def d_of(a: tuple[int, int]) -> tuple[int, int, int]:
    return tuple(
        sum(D[p][e] * a[e] for e in range(E)) % 5
        for p in range(NP)
    )  # type: ignore[return-value]


def boundary(s: tuple[int, int, int]) -> tuple[int, int]:
    return tuple(
        sum(D[p][e] * s[p] for p in range(NP)) % 5
        for e in range(E)
    )  # type: ignore[return-value]


def dot(s: tuple[int, int, int], b: tuple[int, int, int]) -> int:
    return sum(s[p] * b[p] for p in range(NP)) % 5


def primal(b: tuple[int, int, int]) -> R:
    out = ZERO
    for a in LINKS:
        f = d_of(a)
        term = ONE
        for p in range(NP):
            term = mul(term, W(f[p] + b[p]))
        out = add(out, term)
    return out


def gram_hat(b: tuple[int, int, int]) -> R:
    amps: dict[tuple[int, int], R] = {}
    for s in CHAINS:
        beta = boundary(s)
        amps[beta] = add(amps.get(beta, ZERO), zpow(dot(s, b)))
    out = ZERO
    for amp in amps.values():
        out = add(out, mul(amp, conj(amp)))
    return out


primal_cache: dict[tuple[int, int, int], R] = {}
hat_cache: dict[tuple[int, int, int], R] = {}

for b in SOURCES:
    zp = primal(b)
    gh = gram_hat(b)
    assert zp == scale(5 ** E, gh)
    primal_cache[b] = zp
    hat_cache[b] = gh

print("GRAM PASS sources=125 link_fields=25 binary_chains=8")


# ---------------------------------------------------------------------------
# 3. Galois covariance on every source.
# ---------------------------------------------------------------------------

galois_checks = 0
for b in SOURCES:
    for r in (1, 2, 3, 4):
        rb = tuple((r * x) % 5 for x in b)
        assert gal(primal_cache[b], r) == primal_cache[rb]
        galois_checks += 1

assert galois_checks == 500
print("GALOIS PASS checks=500")


# ---------------------------------------------------------------------------
# 4. Real-subfield integrality and untwisted integer normalization.
# ---------------------------------------------------------------------------

real_checks = 0
for b in SOURCES:
    ab = to_phi(hat_cache[b])
    assert from_phi(*ab) == hat_cache[b]
    real_checks += 1

n_a, n_b = to_phi(hat_cache[(0, 0, 0)])
assert n_b == 0
assert n_a > 0
assert real_checks == 125
print("REAL_SUBFIELD PASS checks=125 normalization_integer=YES")


# ---------------------------------------------------------------------------
# 5. One-plaquette defect Galois transport.
# ---------------------------------------------------------------------------

def src_add(
    b: tuple[int, int, int], p: int, amount: int
) -> tuple[int, int, int]:
    c = list(b)
    c[p] = (c[p] + amount) % 5
    return tuple(c)  # type: ignore[return-value]


def src_scale(
    r: int, b: tuple[int, int, int]
) -> tuple[int, int, int]:
    return tuple((r * x) % 5 for x in b)  # type: ignore[return-value]


def defect_hat(
    b: tuple[int, int, int], p: int, r: int
) -> R:
    return sub(
        hat_cache[src_add(b, p, -r)],
        hat_cache[src_add(b, p, +r)],
    )


defect_checks = 0
defect_pairs: list[tuple[int, int]] = []
for b in SOURCES:
    for p in range(NP):
        d1 = defect_hat(b, p, 1)
        d2_at_galois_source = defect_hat(src_scale(2, b), p, 2)
        assert gal(d1, 2) == d2_at_galois_source

        a, bb = to_phi(d1)
        a2, b2 = to_phi(d2_at_galois_source)
        assert (a2, b2) == (a + bb, -bb)
        defect_pairs.append((a, bb))
        defect_checks += 1

assert defect_checks == 375
print("DEFECT_GALOIS PASS checks=375")


# ---------------------------------------------------------------------------
# 6. Exact Z[phi] two-mode collapse.
#
# phi^2=phi+1. We avoid division by checking
#   (3-phi)x^2 + (2+phi)(x^sigma)^2 = 5(A^2+B^2).
# ---------------------------------------------------------------------------

Q = tuple[int, int]  # a+b*phi


def qadd(x: Q, y: Q) -> Q:
    return (x[0] + y[0], x[1] + y[1])


def qmul(x: Q, y: Q) -> Q:
    a, b = x
    c, d = y
    return (a * c + b * d, a * d + b * c + b * d)


def qscale(n: int, x: Q) -> Q:
    return (n * x[0], n * x[1])


def qsigma(x: Q) -> Q:
    a, b = x
    return (a + b, -b)


def check_collapse(a: int, b: int) -> None:
    x = (a, b)
    xs = qsigma(x)
    lhs = qadd(
        qmul((3, -1), qmul(x, x)),
        qmul((2, 1), qmul(xs, xs)),
    )
    rhs = (5 * (a * a + b * b), 0)
    assert lhs == rhs


collapse_controls = 0
for a in range(-12, 13):
    for b in range(-12, 13):
        check_collapse(a, b)
        collapse_controls += 1

assert collapse_controls == 625

for a, b in defect_pairs:
    check_collapse(a, b)

print("INTEGER_COLLAPSE PASS controls=625 defects=375")
print(
    "AUDIT PASS; discrete_defect_identity=EXACT; "
    "binary_pair_gram=EXACT; integer_two_mode_reduction=EXACT; "
    "thermodynamic_floor=OPEN; P1=OPEN"
)
