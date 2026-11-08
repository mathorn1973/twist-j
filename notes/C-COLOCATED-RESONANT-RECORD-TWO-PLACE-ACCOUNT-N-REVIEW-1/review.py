#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Independent checker for PR #1959 (C-COLOCATED-RESONANT-RECORD-TWO-PLACE-ACCOUNT-N).

Written from the equations in the PR texts (PROOF.md, PREREG.md, ERRATA.md,
README.md) and the frozen conventions K1-K10 of this review's PREREG.md.
It reads no file, writes no file, uses only the standard library, exact
integer and Fraction arithmetic, and prints one PASS/FAIL line per check
R01-R14 followed by RESULT PASS (exit 0) or RESULT FAILURE (exit 1).
"""
from __future__ import annotations

import hashlib
import itertools
import sys
from fractions import Fraction
from math import gcd

Vec = tuple  # (v0, v1, v2, v3) in the power basis (1, j, j^2, j^3)
Phi = tuple  # (A, B) meaning A + B*phi in Z[phi]

ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
JJ = (0, 1, 0, 0)        # j
RHO = (0, 0, 1, 0)       # j^2
J3 = (0, 0, 0, 1)        # j^3
J4 = (-1, -1, -1, -1)    # j^4 = -1 - j - j^2 - j^3
J = (1, 0, 1, 0)         # 1 + rho
JINV_CLAIM = (0, -1, -1, 0)
PHI = (0, 0, -1, -1)     # -j^2 - j^3
C_SHARP = (-1, -2, -2, 0)

FAILS: list[str] = []
LINES: list[str] = []


def out(line: str) -> None:
    LINES.append(line)


def check(name: str, ok: bool, detail: str) -> None:
    status = "PASS" if ok else "FAIL"
    if not ok:
        FAILS.append(name)
    out(f"{name} {status} {detail}")


# ---------------------------------------------------------------- ring O = Z[j]

def add(a: Vec, b: Vec) -> Vec:
    return tuple(x + y for x, y in zip(a, b))


def sub(a: Vec, b: Vec) -> Vec:
    return tuple(x - y for x, y in zip(a, b))


def neg(a: Vec) -> Vec:
    return tuple(-x for x in a)


def scal(k: int, a: Vec) -> Vec:
    return tuple(k * x for x in a)


def mul_a(a: Vec, b: Vec) -> Vec:
    """(A) polynomial product reduced modulo 1 + t + t^2 + t^3 + t^4."""
    prod = [0] * 7
    for i in range(4):
        for k in range(4):
            prod[i + k] += a[i] * b[k]
    # reduce t^6, t^5, t^4 using t^4 = -1 - t - t^2 - t^3 (highest first)
    for deg in (6, 5, 4):
        coef = prod[deg]
        if coef:
            prod[deg] = 0
            # t^deg = t^(deg-4) * t^4 = -t^(deg-4) * (1 + t + t^2 + t^3)
            for s in range(4):
                prod[deg - 4 + s] -= coef
    # after reduction, degrees 4..6 may have been refilled by lower shifts:
    # deg 6 shifts into 2..5, deg 5 into 1..4, deg 4 into 0..3; redo until clean
    while any(prod[4:]):
        for deg in (6, 5, 4):
            coef = prod[deg]
            if coef:
                prod[deg] = 0
                for s in range(4):
                    prod[deg - 4 + s] -= coef
    return tuple(prod[:4])


def mul_b(a: Vec, b: Vec) -> Vec:
    """(B) 5-cyclic convolution of (a0..a3, 0), (b0..b3, 0), then subtract the 5th coordinate."""
    a5 = (a[0], a[1], a[2], a[3], 0)
    b5 = (b[0], b[1], b[2], b[3], 0)
    r = [0] * 5
    for i in range(5):
        if a5[i] == 0:
            continue
        for k in range(5):
            r[(i + k) % 5] += a5[i] * b5[k]
    return tuple(r[t] - r[4] for t in range(4))


def mul(a: Vec, b: Vec) -> Vec:
    return mul_a(a, b)


def vpow(a: Vec, n: int) -> Vec:
    r = ONE
    for _ in range(n):
        r = mul(r, a)
    return r


def conj(a: Vec) -> Vec:
    """j -> j^4: coefficient of j^k moves to j^(5-k mod 5)."""
    a5 = (a[0], a[1], a[2], a[3], 0)
    r = [0] * 5
    for k in range(5):
        r[(5 - k) % 5] += a5[k]
    return tuple(r[t] - r[4] for t in range(4))


def tr_k(a: Vec) -> int:
    """Tr_{K/Q}: Tr(1) = 4, Tr(j^k) = -1 for k = 1..3."""
    return 4 * a[0] - a[1] - a[2] - a[3]


def eps5(a: Vec) -> int:
    return sum(a) % 5


def in_2o(a: Vec) -> bool:
    return all(x % 2 == 0 for x in a)


def half(a: Vec) -> Vec | None:
    if not in_2o(a):
        return None
    return tuple(x // 2 for x in a)


def mult_matrix(a: Vec) -> list[list[int]]:
    """Columns are a*1, a*j, a*j^2, a*j^3 in the power basis."""
    cols = [mul(a, e) for e in (ONE, JJ, RHO, J3)]
    return [[cols[c][r] for c in range(4)] for r in range(4)]


def det4(m: list[list[int]]) -> int:
    f = [[Fraction(x) for x in row] for row in m]
    d = Fraction(1)
    for col in range(4):
        piv = next((r for r in range(col, 4) if f[r][col] != 0), None)
        if piv is None:
            return 0
        if piv != col:
            f[col], f[piv] = f[piv], f[col]
            d = -d
        d *= f[col][col]
        for r in range(col + 1, 4):
            fac = f[r][col] / f[col][col]
            if fac:
                for c in range(col, 4):
                    f[r][c] -= fac * f[col][c]
    assert d.denominator == 1
    return int(d)


# ---------------------------------------------------------------- Z[phi]

def h(v: Vec) -> Phi:
    """v*conj(v) = A - B j^2 - B j^3 = A + B*phi; computed from the product (K2)."""
    p = mul(v, conj(v))
    assert p[1] == 0 and p[2] == p[3], ("non-real product", v, p)
    return (p[0], -p[2])


def q(v: Vec) -> int:
    a, b = h(v)
    return 2 * a + b


def p_add(x: Phi, y: Phi) -> Phi:
    return (x[0] + y[0], x[1] + y[1])


def p_sub(x: Phi, y: Phi) -> Phi:
    return (x[0] - y[0], x[1] - y[1])


def p_scal(k: int, x: Phi) -> Phi:
    return (k * x[0], k * x[1])


def p_mul(x: Phi, y: Phi) -> Phi:
    # (A + B phi)(C + D phi) = AC + (AD + BC) phi + BD phi^2, phi^2 = phi + 1
    a, b = x
    c, d = y
    return (a * c + b * d, a * d + b * c + b * d)


def p_tr(x: Phi) -> int:
    return 2 * x[0] + x[1]


def p_norm(x: Phi) -> int:
    return x[0] * x[0] + x[0] * x[1] - x[1] * x[1]


def s_forms(v: Vec) -> Phi:
    v0, v1, v2, v3 = v
    s0 = v0 * v0 + v1 * v1 + v2 * v2 + v3 * v3
    s1 = v0 * v1 + v1 * v2 + v2 * v3
    s2 = v0 * v2 + v1 * v3 + v0 * v3
    return (s0 - s1, s1 - s2)


# ---------------------------------------------------------------- carrier and contacts

class Carrier:
    """x at vertex A, list of slots at vertex B, field F.  K3/K4/K5."""

    def __init__(self, x: Vec, slots: list[Vec], current=None):
        self.x = x
        self.slots = list(slots)
        self.f = neg(x)
        self.current = current if current is not None else sub(RHO, ONE)
        self.cuts = 0
        self.admitted = 0
        self.area: Phi = (0, 0)
        self.snapshot = self.invariants()
        assert self.gauss_ok(), "initial Gauss laws fail"

    def gauss_ok(self) -> bool:
        return add(self.f, self.x) == ZERO and sub(self.f, total(self.slots)) == ZERO

    def invariants(self):
        tot = add(self.x, total(self.slots))
        eps = (eps5(self.x),) + tuple(eps5(s) for s in self.slots)
        e_full = 2 * (q(self.x) + sum(q(s) for s in self.slots))
        h_full = p_scal(2, p_add(h(self.x), sum_phi(h(s) for s in self.slots)))
        return (tot, eps, e_full, h_full)

    def contact(self, r: int) -> bool:
        """One primitive cut C(x, slot r).  Returns admitted flag."""
        v = self.slots[r]
        d = half(sub(v, self.x))
        admitted = d is not None
        if admitted:
            i = mul(self.current, d)
            self.x = sub(self.x, i)
            self.slots[r] = add(v, i)
            self.f = add(self.f, i)
            self.admitted += 1
            self.area = p_add(self.area, h(d))
        self.cuts += 1
        if not (self.gauss_ok() and self.invariants() == self.snapshot):
            raise AssertionError("cut invariant violated")
        return admitted

    def word(self, edges: list[int]) -> list[bool]:
        return [self.contact(r) for r in edges]

    def inverse_word(self, edges: list[int]) -> None:
        for r in reversed(edges):
            for _ in range(4):
                self.contact(r)

    def state(self):
        return (self.x, tuple(self.slots), self.f)


def total(slots) -> Vec:
    t = ZERO
    for s in slots:
        t = add(t, s)
    return t


def sum_phi(items) -> Phi:
    t = (0, 0)
    for it in items:
        t = p_add(t, it)
    return t


# ---------------------------------------------------------------- fixtures (K10)

G625 = list(itertools.product(range(-2, 3), repeat=4))
G81_A = list(itertools.product(range(-1, 2), repeat=4))            # 81 incl. zero
G80_C = [c for c in G81_A if c != ZERO]                              # 80
ODD_SEEDS = G80_C + [C_SHARP]                                        # 81
EVEN_SEEDS = [scal(2, c) for c in ODD_SEEDS]                         # 81
PROFILES = [(1, 0, 0, 0, 0), (0, 1, 0, 0, 0), (0, 0, 0, 0, 1), (1, 1, 1, 1, 1),
            (2, 1, 0, 0, 0), (0, 0, 3, 0, 0), (1, 2, 3, 4, 5), (5, 4, 3, 2, 1),
            (7, 0, 0, 0, 1), (2, 2, 2, 0, 0), (1, 0, 1, 0, 1), (10, 1, 1, 1, 1)]
POLARIZATIONS = [(1, 0, 0, 0), (1, 1, 0, 0), (0, 1, -1, 0), (1, 2, 2, 0)]
RHO_POW = [vpow(RHO, k) for k in range(5)]
THREE_RHO = add(scal(3, ONE), RHO)
ONE_MINUS_RHO = sub(ONE, RHO)


def fmt(v: Vec) -> str:
    return ",".join(str(x) for x in v)


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


# ---------------------------------------------------------------- R01

def r01(jinv: Vec = JINV_CLAIM) -> bool:
    ok = True
    ok &= vpow(JJ, 5) == ONE
    ok &= add(add(add(add(ONE, JJ), RHO), J3), J4) == ZERO
    ok &= mul(PHI, PHI) == add(PHI, ONE)
    ok &= tr_k(PHI) == 2
    ok &= mul(J, jinv) == ONE
    ok &= abs(det4(mult_matrix(J))) == 1
    ok &= det4(mult_matrix(ONE_MINUS_RHO)) == 5
    pairs = 0
    for a in G81_A:
        for b in G81_A:
            if mul_a(a, b) != mul_b(a, b):
                ok = False
            pairs += 1
    for a in G625:
        for b in (JJ, RHO, J, PHI, C_SHARP):
            if mul_a(a, b) != mul_b(a, b):
                ok = False
            pairs += 1
    check("R01", ok, f"ring identities, J_inverse={fmt(jinv)}, det(J)=+-1, det(1-rho)=5, mul_A==mul_B pairs={pairs}")
    return ok


# ---------------------------------------------------------------- R02

def r02() -> None:
    ok = True
    for v in G625:
        hv = h(v)
        ok &= hv == s_forms(v)
        ok &= 2 * p_tr(hv) == tr_k(mul(v, conj(v)))
        ok &= p_norm(hv) == det4(mult_matrix(v))
        if v != ZERO:
            ok &= p_tr(hv) > 0
    check("R02", ok, f"h==S-forms, 2Q==Tr_K(v conj v), N(h)==det, Q>0 on grid={len(G625)}")


# ---------------------------------------------------------------- R03

def r03() -> None:
    ok = True
    ok &= h(ONE_MINUS_RHO) == (2, 1)
    ok &= h(sub(ONE, J4)) == (3, -1)
    ok &= h(J) == (2, -1)
    ok &= h(THREE_RHO) == (10, -3)
    ok &= p_mul((2, 1), (3, -1)) == (5, 0)
    ok &= h(THREE_RHO) == p_add(p_scal(4, h(J)), h(ONE_MINUS_RHO))
    cur = sub(RHO, ONE)
    for d in G625:
        ok &= h(mul(cur, d)) == p_mul((2, 1), h(d))
        ok &= p_scal(5, h(d)) == p_mul((3, -1), h(mul(cur, d)))
    check("R03", ok, "h(1-j^2)=2+phi h(1-j^4)=3-phi h(J)=2-phi h(3+rho)=10-3phi (2+phi)(3-phi)=5 h(i)=(2+phi)h(d)")


# ---------------------------------------------------------------- R04

def r04() -> None:
    ok = True
    b0 = []
    f2 = ONE_MINUS_RHO
    f4 = sub(ONE, J4)
    for c in G625:
        a, b = h(c)
        ok &= h(mul(f2, c)) == (2 * a + b, a + 3 * b)
        ok &= h(mul(f4, c)) == (3 * a - b, 2 * b - a)
        q2 = q(mul(f2, c))
        q4 = q(mul(f4, c))
        ok &= q2 == 5 * (a + b) and q4 == 5 * a and q2 + q4 == 5 * q(c)
        ok &= (q2 == q4) == (b == 0)
        if b == 0:
            b0.append(c)
    ok &= len(b0) == 49
    c1, c2 = f2, f4
    ok &= q(c1) == 5 and q(c2) == 5
    ok &= q(mul(f2, c1)) == 15 and q(mul(f2, c2)) == 10
    ok &= h(ONE)[1] == 0 and q(mul(f2, ONE)) == 5 and 5 * q(ONE) == 10
    fp = sha("".join(fmt(c) + "\n" for c in sorted(b0)))
    check("R04", ok, f"theorem1.3 grid={len(G625)} B0_count={len(b0)} counterexample 15!=10 E2(c=1) 5!=10 FP_B0={fp}")


# ---------------------------------------------------------------- R05

def r05() -> None:
    ok = True
    n = 0
    for x in G81_A:
        for v in G81_A:
            n += 1
            car = Carrier(x, [v, neg(add(x, v))])  # untouched neutralizing companion
            before = car.state()
            adm = car.contact(0)
            ok &= adm == in_2o(sub(v, x))
            if not adm:
                ok &= car.state() == before
                continue
            d = half(sub(v, x))
            ok &= car.area == h(d)
            ok &= add(car.x, car.slots[0]) == add(x, v)
            ok &= eps5(car.x) == eps5(x) and eps5(car.slots[0]) == eps5(v)
            ok &= q(car.x) + q(car.slots[0]) == q(x) + q(v)
            ok &= p_add(h(car.x), h(car.slots[0])) == p_add(h(x), h(v))
            # C^4 after C restores; C^5 = id
            for _ in range(4):
                car.contact(0)
            ok &= car.state() == before
    check("R05", ok, f"contact law pairs={n} refusal==odd difference, identity on refusal, C^5=id, invariants")


# ---------------------------------------------------------------- R06

def theorem2_run(a: Vec, c: Vec, current=None):
    h0 = add(a, scal(2, c))
    u = neg(add(a, h0))
    car = Carrier(a, [h0, ZERO, u], current)
    init = car.state()
    adm = car.word([0, 1])
    after = car.state()
    car.inverse_word([0, 1])
    restored = car.state() == init
    return adm, after, restored, car


def r06(current=None, record: bool = True) -> bool:
    ok = True
    cuts = 0
    resonant = []
    for a in G81_A:
        for c in G80_C:
            adm, after, restored, car = theorem2_run(a, c, current)
            x2, slots, f2 = after
            h1, z2, _u = slots
            cuts += car.cuts
            ok &= restored and adm[0]
            s1 = adm[1] and x2 == a
            s2 = adm[1] and f2 == neg(a)
            s3 = adm[1] and z2 != ZERO and x2 == a
            s4 = a == mul(J, c)
            ok &= s1 == s2 == s3 == s4
            if s4:
                resonant.append((a, c))
    ok &= cuts == 64800
    ok &= len(resonant) == 38
    # Proposition 1 at (a, c) = (1, 1)
    a1 = ONE
    lhs = add(a1, add(add(a1, scal(2, ONE)), ZERO))
    rhs = add(add(a1, scal(2, a1)), ONE_MINUS_RHO)
    ok &= lhs != rhs
    # resonance trajectory on 624 nonzero seeds of G625
    nres = 0
    for c in G625:
        if c == ZERO:
            continue
        nres += 1
        a = mul(J, c)
        h0 = add(a, scal(2, c))
        ok &= h0 == mul(THREE_RHO, c)
        car = Carrier(a, [h0, ZERO, neg(add(a, h0))], current)
        d1 = half(sub(h0, a))
        ok &= d1 == c
        car.contact(0)
        ok &= car.x == scal(2, c) and car.slots[0] == scal(2, mul(J, c))
        d2 = half(sub(ZERO, car.x))
        ok &= d2 == neg(c)
        car.contact(1)
        ok &= car.x == a and car.f == neg(a)
        ok &= car.slots[0] == scal(2, mul(J, c)) and car.slots[1] == mul(ONE_MINUS_RHO, c)
        aa, bb = h(c)
        ok &= h(h0) == p_add(h(car.slots[0]), h(car.slots[1]))
        ok &= q(h0) == 17 * aa + bb and q(car.slots[0]) == 12 * aa - 4 * bb
        ok &= q(car.slots[1]) == 5 * (aa + bb)
        ok &= car.area == p_scal(2, h(c))
    fp = sha("".join(fmt(a) + "|" + fmt(c) + "\n" for a, c in sorted(resonant)))
    if record:
        check("R06", ok, f"theorem2 pairs=6480 cuts={cuts} resonant={len(resonant)} grid_seeds={nres} FP_RESONANT={fp}")
    return ok


# ---------------------------------------------------------------- R07

def r07() -> None:
    ok = True
    # Phi_5 over F2: no root, not divisible by t^2 + t + 1
    phi5 = [1, 1, 1, 1, 1]
    ok &= sum(phi5) % 2 == 1          # Phi_5(1) odd
    ok &= phi5[0] % 2 == 1            # Phi_5(0) odd
    # polynomial division of t^4+t^3+t^2+t+1 by t^2+t+1 over F2
    rem = phi5[:]
    for deg in (4, 3, 2):
        if rem[deg] % 2:
            for s, coef in enumerate((1, 1, 1)):
                rem[deg - 2 + s] ^= coef
    ok &= any(rem[:2])
    classes = [v for v in itertools.product(range(2), repeat=4)]
    ok &= len(classes) == 16
    nz = [v for v in classes if any(v)]
    products = 0
    for u in nz:
        for w in nz:
            products += 1
            ok &= not in_2o(mul(u, w))
    check("R07", ok, f"Phi_5 irreducible over F_2, classes=16, nonzero products={products} all nonzero mod 2O")


# ---------------------------------------------------------------- R08

def bank_run(c: Vec, m: int, channels: int = 5, targets=None):
    """Five-channel bank (K4 ordering); returns carrier after forward word, admitted flags, init state."""
    if targets is None:
        cs = [mul(c, RHO_POW[k]) for k in range(channels)]
    else:
        cs = targets
    a_m = mul(J, cs[m])
    slots = [neg(a_m)]
    for k in range(channels):
        hk = mul(THREE_RHO, cs[k])
        slots += [hk, ZERO, neg(hk)]
    car = Carrier(a_m, slots)
    init = car.state()
    edges = []
    for k in range(channels):
        edges += [1 + 3 * k, 2 + 3 * k]
    adm = car.word(edges)
    after = car.state()
    return car, adm, init, after, edges, cs


def r08() -> None:
    ok = True
    cuts = 0
    odd_pass = 0
    even_fail = 0
    witness = 0
    fp_lines = []
    for parity, seeds in (("odd", ODD_SEEDS), ("even", EVEN_SEEDS)):
        for c in seeds:
            aa, bb = h(c)
            onehot_all = True
            for m in range(5):
                car, adm, init, after, edges, cs = bank_run(c, m)
                x_after, slots_after, f_after = after
                exp_z = mul(ONE_MINUS_RHO, cs[m])
                exp_h = scal(2, mul(J, cs[m]))
                onehot = x_after == mul(J, cs[m]) and f_after == neg(x_after)
                for k in range(5):
                    hk, zk = slots_after[1 + 3 * k], slots_after[2 + 3 * k]
                    if k == m:
                        onehot &= hk == exp_h and zk == exp_z
                    else:
                        onehot &= hk == mul(THREE_RHO, cs[k]) and zk == ZERO
                if parity == "odd":
                    ok &= onehot
                    ok &= sum(adm) == 2 and adm[2 * m] and adm[2 * m + 1]
                    ok &= q(slots_after[2 + 3 * m]) == 5 * (aa + bb)
                    ok &= h(slots_after[2 + 3 * m]) == p_mul((2, 1), h(c))
                    ok &= car.area == p_scal(2, h(c))
                    e_full = car.snapshot[2]
                    ok &= e_full == 4 * q(mul(J, c)) + 20 * q(mul(THREE_RHO, c))
                    ok &= e_full == 352 * aa + 16 * bb
                    ok &= car.snapshot[3] == p_add(p_scal(4, h(mul(J, c))), p_scal(20, h(mul(THREE_RHO, c))))
                else:
                    onehot_all &= onehot
                    if m == 1:
                        ok &= adm[0]
                        ok &= slots_after[1] != mul(THREE_RHO, cs[0])
                        witness += 1
                fp_lines.append(fmt(c) + "|" + str(m) + "|" + fmt(x_after) + "|" +
                                ",".join(fmt(slots_after[1 + 3 * k]) + "," + fmt(slots_after[2 + 3 * k]) for k in range(5)) + "\n")
                car.inverse_word(edges)
                ok &= car.state() == init
                cuts += car.cuts
            if parity == "odd":
                odd_pass += 1
            else:
                ok &= not onehot_all
                even_fail += 1
    ok &= cuts == 40500 and odd_pass == 81 and even_fail == 81 and witness == 81
    fp = sha("".join(sorted(fp_lines)))
    check("R08", ok, f"theorem3 seeds=162 phases=5 cuts={cuts} odd_onehot_pass={odd_pass} even_onehot_fail={even_fail} even_witness_m1_k0={witness} FP_BANK={fp}")


# ---------------------------------------------------------------- R09

def r09() -> None:
    ok = True
    c = mul(ONE_MINUS_RHO, JINV_CLAIM)
    ok &= c == C_SHARP and not in_2o(c)
    ok &= h(c) == (3, 4) and q(c) == 10
    ok &= mul(J, c) == ONE_MINUS_RHO
    for k in range(5):
        ck = mul(c, RHO_POW[k])
        ak = mul(J, ck)
        h0 = mul(THREE_RHO, ck)
        h1 = scal(2, ak)
        z = mul(ONE_MINUS_RHO, ck)
        ok &= q(ak) == 5 and h(ak) == (2, 1)
        ok &= q(h0) == 55 and h(h0) == (18, 19)
        ok &= q(h1) == 20 and h(h1) == (8, 4)
        ok &= q(z) == 35 and h(z) == (10, 15)
        ok &= p_scal(2, h(ck)) == (6, 8)
    # two-selector port (K8): channel 0 target a0 = 1 - rho, channel 1 target a1 = (1 - rho) rho^4
    a0 = ONE_MINUS_RHO
    a1 = mul(ONE_MINUS_RHO, RHO_POW[4])
    targets = [mul(a0, JINV_CLAIM), mul(a1, JINV_CLAIM)]
    ok &= mul(J, targets[0]) == a0 and mul(J, targets[1]) == a1
    results = {}
    for label, m in (("P27", 1), ("P35", 0)):
        car, adm, init, after, edges, cs = bank_run(C_SHARP, m, channels=2, targets=targets)
        x_after, slots_after, f_after = after
        results[label] = (q(slots_after[2]), q(slots_after[5]))
        ok &= x_after == mul(J, cs[m]) and f_after == neg(x_after)
        other = 1 - m
        ok &= slots_after[1 + 3 * other] == mul(THREE_RHO, cs[other]) and slots_after[2 + 3 * other] == ZERO
        car.inverse_word(edges)
        ok &= car.state() == init
    ok &= results["P27"] == (0, 35) and results["P35"] == (35, 0)
    check("R09", ok, f"c#={fmt(c)} h=3+4phi Q=10 helper 55->20 quantum=35 area=6+8phi port P27={results['P27']} P35={results['P35']}")


# ---------------------------------------------------------------- R10

def r10() -> None:
    ok = True
    channel_checks = 0
    for c in ODD_SEEDS:
        aa, bb = h(c)
        w0 = 5 * (aa + bb)
        for prof in PROFILES:
            W = [0] * 5
            H = [(0, 0)] * 5
            for k in range(5):
                for _ in range(prof[k]):
                    car, adm, init, after, edges, cs = bank_run(c, k)
                    z = after[1][2 + 3 * k]
                    W[k] += q(z)
                    H[k] = p_add(H[k], h(z))
            sn = sum(prof)
            sw = sum(W)
            sh = sum_phi(H)
            for k in range(5):
                channel_checks += 1
                ok &= W[k] == prof[k] * w0
                ok &= W[k] * sn == prof[k] * sw
                ok &= p_scal(sn, H[k]) == p_scal(prof[k], sh)
                if prof[k] > 0:
                    ok &= Fraction(W[k], prof[k]) == w0
    check("R10", ok, f"theorem4 seeds=81 profiles={len(PROFILES)} channel_checks={channel_checks} shares==count shares (rational and Z[phi])")


# ---------------------------------------------------------------- R11

def r11() -> None:
    ok = True
    n = 0
    for c in ODD_SEEDS:
        for m in range(5):
            n += 1
            cm = mul(c, RHO_POW[m])
            x = mul(J, cm)
            h1 = scal(2, x)
            z1 = mul(ONE_MINUS_RHO, cm)
            # dead-time lock with fresh blank
            car = Carrier(x, [h1, ZERO, neg(add(x, h1))])
            adm = car.word([0, 1])
            ok &= adm == [False, False] and car.x == x
            # occupied record back-reaction
            car = Carrier(x, [h1, z1, neg(add(add(x, h1), z1))])
            adm0 = car.contact(0)
            d2 = half(sub(z1, car.x))
            ok &= not adm0 and d2 == neg(mul(RHO_POW[(m + 1) % 5], c))
            adm1 = car.contact(1)
            x_new = mul(add(ONE, mul(RHO, RHO)), cm)
            z_new = mul(sub(ONE, mul(RHO, RHO)), cm)
            ok &= adm1 and car.x == x_new and car.slots[1] == z_new
            ok &= (car.x, car.slots[1]) != (neg(mul(RHO_POW[(m + 1) % 5], c)), cm)
            ok &= car.x != x and car.slots[1] != z1
    check("R11", ok, f"theorem5 lock cases={n} backreaction cases={n} x'=(1+rho^2)c rho^m z'=(1-rho^2)c rho^m")


# ---------------------------------------------------------------- R12

def r12() -> None:
    ok = True
    for a0, b in ((5, 4), (7, 6)):
        P = [2, a0]
        cosw = Fraction(a0, 2 * b)
        cheb = [Fraction(1), cosw]
        for n in range(1, 26):
            P.append(a0 * P[-1] - b * b * P[-2])
            cheb.append(2 * cosw * cheb[-1] - cheb[-2])
        for n in range(1, 26):
            ok &= P[n] % 2 == 1 and gcd(P[n], 2 * b ** n) == 1
            ok &= Fraction(P[n], 2 * b ** n) == cheb[n]
            for e0 in POLARIZATIONS:
                ok &= gcd(gcd(gcd(abs(e0[0]), abs(e0[1])), abs(e0[2])), abs(e0[3])) == 1
                scaled = [Fraction(e, 1) * cheb[n] for e in e0]
                ok &= any(s.denominator != 1 for s in scaled)
                ok &= all((s * 2 * b ** 25).denominator == 1 for s in scaled)
    check("R12", ok, "theorem5.3 modes=(5,4),(7,6) n=1..25 P_n odd, gcd(P_n,2b^n)=1, Chebyshev agreement, 4 primitive polarizations")


# ---------------------------------------------------------------- R13

def r13() -> None:
    ok = True
    e = (1, 2, 2, 1)
    ok &= e != C_SHARP and h(e) == (2, 3) and q(e) == 7 and 5 * sum(h(e)) == 25
    for c in G625:
        aa, bb = h(c)
        ok &= 4 * q(mul(J, c)) + 20 * q(mul(THREE_RHO, c)) == 352 * aa + 16 * bb
    aa, bb = h(ONE)
    ok &= 200 * aa + 60 * bb == 200 and 352 * aa + 16 * bb == 352
    cur = sub(RHO, ONE)
    for d2 in G625:
        x1 = scal(-2, d2)
        ok &= sub(x1, mul(cur, d2)) == neg(mul(J, d2))
        if d2 != ZERO:
            ok &= add(x1, mul(cur, d2)) != neg(mul(J, d2))
    check("R13", ok, "errata E1 (1,2,2,1): h=2+3phi Q=7 quantum=25; E3 352A+16B on grid, 200!=352 at c=1; E4 sign identity")


# ---------------------------------------------------------------- R14

def r14() -> None:
    # (a) wrong current sign must break the Theorem 2 equivalence on >= 1 pair
    mutant_a_detected = False
    try:
        mutant_a_detected = not r06(current=sub(ONE, RHO), record=False)
    except AssertionError:
        mutant_a_detected = True
    # (b) wrong inverse must break R01
    saved = list(LINES)
    saved_fails = list(FAILS)
    mutant_b_detected = not r01(jinv=(0, -1, 0, -1))
    del LINES[:]
    LINES.extend(saved)
    del FAILS[:]
    FAILS.extend(saved_fails)
    check("R14", mutant_a_detected and mutant_b_detected,
          f"mutant_current_sign_detected={mutant_a_detected} mutant_J_inverse_detected={mutant_b_detected}")


# ---------------------------------------------------------------- main

def main() -> int:
    out("C-COLOCATED-RESONANT-RECORD-TWO-PLACE-ACCOUNT-N-REVIEW-1 review.py")
    r01()
    r02()
    r03()
    r04()
    r05()
    r06()
    r07()
    r08()
    r09()
    r10()
    r11()
    r12()
    r13()
    r14()
    out(f"CHECKS={14} FAILED={len(FAILS)}" + ("" if not FAILS else " " + ",".join(FAILS)))
    out("RESULT PASS" if not FAILS else "RESULT FAILURE")
    sys.stdout.write("\n".join(LINES) + "\n")
    return 0 if not FAILS else 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except AssertionError as exc:  # a violated cut invariant is a failure, not a crash
        sys.stdout.write("\n".join(LINES) + "\n")
        sys.stdout.write(f"ASSERTION {exc}\nRESULT FAILURE\n")
        sys.exit(1)
