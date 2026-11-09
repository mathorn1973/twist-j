#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Blind independent checker for PR #1961 (C-S3-HEIGHT-PHASE-INTERFACE-N, CONSTRUCTIVE-3).

Written from the PR texts (CONTRACT.md, PROOF.md, PREREG.md, README.md, REVIEW.md
in both directories) and the public predecessor texts in main
(P-RELATIVE-CONTACT-VARIABLE-ARRIVAL-1/CONTRACT.md + WORD535.txt,
P-RELATIVE-CONTACT-WORKBANK-REUSE-1/PROOF.md + PREREG.md), under the frozen
conventions K1-K8 of this review's PREREG.md.  No author executable or expected
output was opened before this file was frozen.

Reads exactly one file: probes/P-RELATIVE-CONTACT-VARIABLE-ARRIVAL-1/WORD535.txt
(public fixture in main).  Standard library only, exact integers, no randomness.
Prints one PASS/FAIL line per check R01-R15, then RESULT PASS (exit 0) or
RESULT FAILURE (exit 1).
"""
from __future__ import annotations

import hashlib
import itertools
import os
import sys
from collections import deque

Vec = tuple
Phi = tuple

ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
JJ = (0, 1, 0, 0)
RHO = (0, 0, 1, 0)
J3 = (0, 0, 0, 1)
J4 = (-1, -1, -1, -1)
TWO = (2, 0, 0, 0)
PHI = (0, 0, -1, -1)

FAILS: list[str] = []
LINES: list[str] = []


def out(line: str) -> None:
    LINES.append(line)


def check(name: str, ok: bool, detail: str) -> None:
    if not ok:
        FAILS.append(name)
    out(f"{name} {'PASS' if ok else 'FAIL'} {detail}")


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


# ---------------------------------------------------------------- ring O = Z[j]

def add(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2], a[3] + b[3])


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2], a[3] - b[3])


def neg(a):
    return (-a[0], -a[1], -a[2], -a[3])


def scal(k, a):
    return (k * a[0], k * a[1], k * a[2], k * a[3])


def mul_a(a, b):
    """(A) polynomial product reduced by t^4 = -1 - t - t^2 - t^3."""
    prod = [0] * 7
    for i in range(4):
        if a[i]:
            for k in range(4):
                prod[i + k] += a[i] * b[k]
    while any(prod[4:]):
        for deg in (6, 5, 4):
            coef = prod[deg]
            if coef:
                prod[deg] = 0
                for s in range(4):
                    prod[deg - 4 + s] -= coef
    return tuple(prod[:4])


def mul_b(a, b):
    """(B) 5-cyclic convolution, then subtract the fifth coordinate."""
    r = [0] * 5
    for i in range(4):
        if a[i]:
            for k in range(4):
                r[(i + k) % 5] += a[i] * b[k]
    return (r[0] - r[4], r[1] - r[4], r[2] - r[4], r[3] - r[4])


mul = mul_a


def vpow(a, n):
    r = ONE
    for _ in range(n):
        r = mul(r, a)
    return r


def conj(a):
    a5 = (a[0], a[1], a[2], a[3], 0)
    r = [0] * 5
    for k in range(5):
        r[(5 - k) % 5] += a5[k]
    return (r[0] - r[4], r[1] - r[4], r[2] - r[4], r[3] - r[4])


def tr_k(a):
    return 4 * a[0] - a[1] - a[2] - a[3]


def eps5(a):
    return (a[0] + a[1] + a[2] + a[3]) % 5


def even(a):
    return (a[0] & 1) == 0 and (a[1] & 1) == 0 and (a[2] & 1) == 0 and (a[3] & 1) == 0


def mod2(a):
    return (a[0] & 1, a[1] & 1, a[2] & 1, a[3] & 1)


def qf(z):
    s2 = z[0] * z[0] + z[1] * z[1] + z[2] * z[2] + z[3] * z[3]
    s1 = z[0] + z[1] + z[2] + z[3]
    num = 5 * s2 - s1 * s1
    assert num % 2 == 0
    return num // 2


def h(v):
    p = mul(v, conj(v))
    assert p[1] == 0 and p[2] == p[3], ("non-real", v, p)
    return (p[0], -p[2])


def p_add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def p_scal(k, x):
    return (k * x[0], k * x[1])


def p_mul(x, y):
    a, b = x
    c, d = y
    return (a * c + b * d, a * d + b * c + b * d)


def p_tr(x):
    return 2 * x[0] + x[1]


def mult_matrix(a):
    cols = [mul(a, e) for e in (ONE, JJ, RHO, J3)]
    return [[cols[c][r] for c in range(4)] for r in range(4)]


def fmt(v):
    return ",".join(str(x) for x in v)


# ---------------------------------------------------------------- named constants

U = sub(ONE, JJ)              # 1 - j
B = sub(ONE, RHO)             # 1 - rho
J = add(ONE, RHO)             # 1 + rho  (= w of the old apparatus)
W_OLD = J
X = (1, 1, 0, -2)             # 1 + j - 2 j^3
BB = add(ONE, mul(RHO, RHO))  # b = 1 + rho^2
JINV = neg(add(RHO, vpow(RHO, 3)))
RHO_POW = [vpow(RHO, k) for k in range(5)]


def rot(r):
    return RHO_POW[r % 5]


# ---------------------------------------------------------------- contact engine (K2, K3)

CACHE: dict = {}
STATS = {"contacts": 0, "admitted": 0, "swaps": 0, "pairs": 0}


def pair_transition(a, b):
    """Literal contact on an ordered pair; verifies pair invariants on first computation."""
    key = (a, b)
    hit = CACHE.get(key)
    if hit is not None:
        return hit
    diff = sub(a, b)
    if not even(diff):
        res = (a, b, False)
    else:
        s = ((a[0] + b[0]) // 2, (a[1] + b[1]) // 2, (a[2] + b[2]) // 2, (a[3] + b[3]) // 2)
        d = (diff[0] // 2, diff[1] // 2, diff[2] // 2, diff[3] // 2)
        rd = mul(RHO, d)
        a2 = add(s, rd)
        b2 = sub(s, rd)
        # pair invariants (K3): sum, Q, h, residues
        if add(a2, b2) != add(a, b) or qf(a2) + qf(b2) != qf(a) + qf(b):
            raise AssertionError(("pair invariant", a, b))
        if p_add(h(a2), h(b2)) != p_add(h(a), h(b)) or eps5(a2) != eps5(a) or eps5(b2) != eps5(b):
            raise AssertionError(("pair invariant h/eps", a, b))
        res = (a2, b2, True)
    CACHE[key] = res
    STATS["pairs"] += 1
    return res


def apply_ops(state: list, ops, trace: list | None = None) -> None:
    """ops: sequence of ('C', i, k) or ('S', i, k); state mutated in place."""
    for op in ops:
        if op[0] == "C":
            i, k = op[1], op[2]
            a2, b2, adm = pair_transition(state[i], state[k])
            state[i] = a2
            state[k] = b2
            STATS["contacts"] += 1
            if adm:
                STATS["admitted"] += 1
            if trace is not None:
                trace.append("A" if adm else "R")
        else:
            i, k = op[1], op[2]
            if eps5(state[i]) != eps5(state[k]):
                raise AssertionError(("swap residue mismatch", i, k))
            state[i], state[k] = state[k], state[i]
            STATS["swaps"] += 1


def apply_ops_checked(state: list, ops, trace=None):
    """Same, but with full-state invariants after every primitive (compiler scale)."""
    inv0 = full_invariants(state)
    for op in ops:
        apply_ops(state, (op,), trace)
        if full_invariants(state) != inv0:
            raise AssertionError(("full invariant", op))


def C(i, k):
    return ("C", i, k)


def S(i, k):
    return ("S", i, k)


def rep(ops, n):
    return list(ops) * n


def inverse_ops(ops):
    inv = []
    for op in reversed(ops):
        if op[0] == "C":
            inv.extend([op] * 4)
        else:
            inv.append(op)
    return inv


def full_invariants(state):
    tot = ZERO
    hh = (0, 0)
    q = 0
    for v in state:
        tot = add(tot, v)
        hh = p_add(hh, h(v))
        q += qf(v)
    return (tot, hh, q, tuple(eps5(v) for v in state))


def ser_state(state):
    return ";".join(fmt(v) for v in state)


def ser_ops(ops):
    return ";".join(f"{op[0]}{op[1]},{op[2]}" for op in ops)


# ---------------------------------------------------------------- compiler construction (PROOF §1-§5)

def heights(t):
    return (add(U, scal(t, B)), sub(U, scal(t, B)))


def input_I(t):
    hp, hm = heights(t)
    return [hp, hm, ZERO, ZERO, X, TWO, J, neg(J)]


X_S = {
    -2: sub(U, mul(J, B)),
    -1: sub(U, B),
    0: U,
    1: add(U, mul(RHO, B)),
    2: add(U, mul(RHO, mul(J, B))),
}


def d_ref(s):
    return neg(mul(mul(B, X_S[s]), JINV))


def stock_Z():
    return [U, sub(U, mul(J, B)), sub(U, B), d_ref(-1), d_ref(0), d_ref(1), d_ref(2)]


def word_P():
    return [C(0, 8), C(0, 9), C(0, 10)]


def word_M(s):
    ds = 12 + s
    return [C(0, ds), C(ds, 5)]


def word_W(p):
    return [C(5, 7)] + [C(6, 7)] * (5 - p) + [C(5, 7)] * 4 + [C(6, 7)] * p


def word_A():
    ops = word_P()
    for s in (-1, 0, 1, 2):
        ops += word_M(s) + word_W(s + 2) + inverse_ops(word_M(s))
    ops += inverse_ops(word_P())
    return ops


def clock_target(t):
    return (mul(rot(t + 2), J), neg(mul(rot(t + 2), J)))


# ---------------------------------------------------------------- old apparatus (WORKBANK PROOF §5, VARIABLE-ARRIVAL CONTRACT)

def bank_empty():
    return [neg(BB), BB] * 5


def bank_marked(p):
    bk = bank_empty()
    bk[2 * p] = neg(mul(RHO, BB))
    bk[2 * p + 1] = mul(RHO, BB)
    return bk


def bank_label(bank):
    """Decoder: exact match against M[p]; None for empty or invalid."""
    for p in range(5):
        if list(bank) == bank_marked(p):
            return p
    return None


F_WORD = [C(0, 1), C(1, 2)]
Y_TABLE: list = []


def build_y_table():
    """Y_n = F^n (0,2,0) for n = 0..9, computed once before any counted run."""
    st = [ZERO, TWO, ZERO]
    for _ in range(10):
        Y_TABLE.append(list(st))
        apply_ops(st, F_WORD)


def source_Y(n):
    return list(Y_TABLE[n])


def clock_X(r):
    return [mul(rot(r), W_OLD), neg(mul(rot(r), W_OLD))]


# old controls (0,u_old,0,0,w,0): the old apparatus' u is 1-rho, i.e. this note's B (CONTRACT §1)
CONTROLS = [ZERO, B, ZERO, ZERO, W_OLD, ZERO]


def core_I(n, r):
    return source_Y(n) + clock_X(r) + list(CONTROLS) + bank_empty() + bank_empty()


def build_S():
    O1 = [C(1, 5)]
    A0 = [C(5, 9)]
    O2 = [C(9, 10)]
    T = [C(3, 4)]

    def Bc(c):
        return [C(c, 9)]

    def E(c):
        return A0 + Bc(c) + rep(A0, 4) + rep(Bc(c), 4)

    def Einv(c):
        return Bc(c) + A0 + rep(Bc(c), 4) + rep(A0, 4)

    def L(q, p):
        ap, bp = q + 2 * p, q + 2 * p + 1
        return rep([C(3, ap)], 4) + rep([C(ap, bp)], 4) + [C(3, ap), C(ap, bp)]

    def SCAN(q):
        ops = []
        for p in range(5):
            ops += [C(3, 10)] + L(q, p) + rep([C(3, 10)], 4) + T
        return ops

    WA = E(6) + O2 + SCAN(11) + rep(O2, 4) + Einv(6)
    WB = E(7) + O2 + SCAN(21) + rep(O2, 4) + Einv(7)

    def D(c, d):
        return rep([C(9, c)], 3) + rep([C(9, d)], 3) + [C(9, c), C(9, d), C(9, c)]

    def V(c, d):
        return A0 + D(c, d) + rep(A0, 4) + D(c, d)

    R = O1 + WA + WB + V(7, 8) + V(6, 7) + rep(O1, 4)
    Finv = rep([C(1, 2)], 4) + rep([C(0, 1)], 4)
    Sw = R + Finv + R + F_WORD + F_WORD + T
    lengths = {"L": len(L(11, 0)), "SCAN": len(SCAN(11)), "E": len(E(6)), "WA": len(WA), "WB": len(WB),
               "D": len(D(7, 8)), "V": len(V(7, 8)), "R": len(R), "S": len(Sw)}
    return Sw, lengths


def read_word535(path):
    ops = []
    with open(path, "r", encoding="ascii") as fh:
        for line in fh:
            line = line.strip()
            if not line or ":" not in line or not line[0].isdigit():
                continue
            body = line.split(":", 1)[1]
            for tok in body.split():
                assert tok.startswith("C(") and tok.endswith(")"), tok
                a, b = tok[2:-1].split(",")
                ops.append(C(int(a) - 1, int(b) - 1))
    return ops


W6_PLACES = [(1, 4), (1, 4), (4, 5), (1, 4), (1, 4), (1, 4), (1, 6), (1, 6), (1, 6), (1, 6), (1, 4), (1, 6)]


def word_K(a, d):
    ops = []
    for p in range(5):
        q = (p + 1) % 5
        places = {1: a + 2 * p, 2: a + 2 * p + 1, 3: a + 2 * q, 4: a + 2 * q + 1, 5: d + 2 * p, 6: d + 2 * p + 1}
        for (i, k) in W6_PLACES:
            ops.append(C(places[i], places[k]))
    return ops


# ---------------------------------------------------------------- assembly layout (CONTRACT §4 with h=7)

A_PORTS = [31, 32, 33, 34, 35, 36, 3, 4] + list(range(37, 44))


def remap(ops, ports):
    return [(op[0], ports[op[1]], ports[op[2]]) for op in ops]


def archive_bases(k):
    return [(44 + 20 * i, 54 + 20 * i) for i in range(k)]


def cartridge_base(k, i):
    """Cartridge i (1-based, i=1..k-1)."""
    return 44 + 20 * k + 5 * (i - 1)


def initial_assembly(seq):
    """seq: list of (n, t). Returns the full initial state and k."""
    k = len(seq)
    n0, t0 = seq[0]
    st = source_Y(n0) + clock_X(0) + list(CONTROLS) + bank_empty() + bank_empty()
    hp, hm = heights(t0)
    st += [hp, hm, ZERO, ZERO, X, TWO]
    st += stock_Z()
    for _ in range(k):
        st += bank_empty() + bank_empty()
    for (n, t) in seq[1:]:
        hp, hm = heights(t)
        st += source_Y(n) + [hp, hm]
    assert len(st) == 39 + 25 * k
    return st, k


def assembly_program(k, A_ops, W_ops, Winv_ops):
    """Returns list of (label, ops) segments in chronological order."""
    A_m = remap(A_ops, A_PORTS)
    Ainv_m = inverse_ops(A_m)
    segs = []
    for i in range(k):
        a_base, b_base = archive_bases(k)[i]
        segs.append((f"A{i}", A_m))
        segs.append((f"W{i}", W_ops))
        segs.append((f"KA{i}", word_K(11, a_base)))
        segs.append((f"KB{i}", word_K(21, b_base)))
        segs.append((f"Winv{i}", Winv_ops))
        segs.append((f"Ainv{i}", Ainv_m))
        if i < k - 1:
            cb = cartridge_base(k, i + 1)
            segs.append((f"SWAP{i}", [S(0, cb), S(1, cb + 1), S(2, cb + 2), S(31, cb + 3), S(32, cb + 4)]))
    return segs


# ================================================================ checks

G625 = list(itertools.product(range(-2, 3), repeat=4))
G81 = list(itertools.product(range(-1, 2), repeat=4))
G256 = list(itertools.product(range(-1, 3), repeat=4))


def r01():
    ok = True
    ok &= add(add(add(add(ONE, JJ), RHO), J3), J4) == ZERO
    ok &= mul(PHI, PHI) == add(PHI, ONE)
    ok &= mul(J, JINV) == ONE and JINV == (0, -1, -1, 0)
    ok &= vpow(RHO, 5) == ONE
    pairs = 0
    for a in G81:
        for b in G81:
            ok &= mul_a(a, b) == mul_b(a, b)
            pairs += 1
    for a in G625:
        for b in (JJ, RHO, U, B, J, X, PHI):
            ok &= mul_a(a, b) == mul_b(a, b)
            pairs += 1
    # Phi_5 over F2
    rem = [1, 1, 1, 1, 1]
    for deg in (4, 3, 2):
        if rem[deg] & 1:
            for s in range(3):
                rem[deg - 2 + s] ^= 1
    ok &= any(rem[:2]) and (sum([1, 1, 1, 1, 1]) % 2 == 1)
    classes = [v for v in itertools.product(range(2), repeat=4) if any(v)]
    for x in classes:
        for y in classes:
            ok &= not even(mul(x, y))
    # orders in F16
    def order_mod2(v):
        acc = ONE
        for n in range(1, 16):
            acc = mul(acc, v)
            if mod2(acc) == mod2(ONE):
                return n
        return None
    ok &= order_mod2(RHO) == 5 and order_mod2(U) == 15
    ok &= mod2(vpow(U, 3)) == mod2(J4) and mod2(mul(U, U)) == mod2(J) and mod2(B) == mod2(J)
    rho_group = {mod2(rot(e)) for e in range(5)}
    ok &= mod2(mul(U, JINV)) not in rho_group
    ok &= mod2(vpow(W_OLD, 3)) == mod2(rot(4)) and mod2(W_OLD) not in rho_group
    ok &= mod2(mul(W_OLD, W_OLD)) == mod2(BB)
    # Hermitian constants
    ok &= h(U) == (3, -1) and h(B) == (2, 1) and h(J) == (2, -1) and h(X) == (5, 5) and h(TWO) == (4, 0)
    ok &= h(add(ONE, mul(RHO, RHO))) == (1, 1)
    ok &= qf(U) == 5 and qf(B) == 5 and qf(X) == 15 and qf(TWO) == 8 and qf(J) == 3 and qf(BB) == 3
    for v in G625:
        ok &= qf(v) == p_tr(h(v)) and 2 * qf(v) == tr_k(mul(v, conj(v)))
        if v != ZERO:
            ok &= qf(v) > 0
    check("R01", ok, f"ring, F16 (rho order 5, u order 15, J=u^2, u/J outside <rho>), constants, mul_A==mul_B pairs={pairs}")


def r02():
    ok = True
    n = 0
    for a in G256:
        for b in G256:
            n += 1
            a2, b2, adm = pair_transition(a, b)
            ok &= adm == even(sub(a, b))
            if not adm:
                ok &= (a2, b2) == (a, b)
                continue
            # C^5 = id, C^4 inverse
            x, y = a2, b2
            for _ in range(4):
                x, y, _ = pair_transition(x, y)
            ok &= (x, y) == (a, b)
            # orientation independence
            c2, d2, adm2 = pair_transition(b, a)
            ok &= adm2 and (c2, d2) == (b2, a2)
            if a == b:
                ok &= (a2, b2) == (a, b)
    check("R02", ok, f"contact law on pairs={n}: parity guard, identity on refusal, pair invariants, C^5=id, orientation-free")


def r03():
    ok = True
    Z = stock_Z()
    for s in (-1, 0, 1, 2):
        ok &= mul(J, d_ref(s)) == neg(mul(B, X_S[s]))
    table = [((1, -1, 0, 0), (3, -1), 5), ((-1, -2, -1, -1), (2, 1), 5), ((0, -1, 1, 0), (3, -1), 5),
             ((-2, -3, -3, -2), (5, 5), 15), ((1, 1, 0, -2), (5, 5), 15), ((-2, -2, 0, -1), (5, 0), 10),
             ((-1, -2, -3, -4), (10, 5), 25)]
    for z, (val, hh, q) in zip(Z, table):
        ok &= z == val and h(z) == hh and qf(z) == q
    ez = sum(qf(z) for z in Z)
    hz = (0, 0)
    sz = ZERO
    for z in Z:
        hz = p_add(hz, h(z))
        sz = add(sz, z)
    ok &= ez == 80 and hz == (33, 14) and sz == (-4, -10, -6, -10)
    ok &= neg(mul(B, JINV)) == (1, 2, 2, 0)
    ok &= h(mul(B, JINV)) == (3, 4)
    ok &= h(X_S[-1]) == (3, -1) and h(X_S[0]) == (3, -1) and h(X_S[1]) == (7, -4) and h(X_S[2]) == (10, -5)
    ok &= X_S[2] == mul(U, U)
    for t in range(-2, 3):
        I = input_I(t)
        ok &= sum(qf(v) for v in I) == 39 + 10 * t * t
        ok &= tuple(eps5(v) for v in I) == (0, 0, 0, 0, 0, 2, 2, 3)
        full = I + Z
        ok &= sum(qf(v) for v in full) == 119 + 10 * t * t
        hf = (0, 0)
        for v in full:
            hf = p_add(hf, h(v))
        ok &= hf == (52 + 4 * t * t, 15 + 2 * t * t)
        hp, hm = heights(t)
        ok &= qf(hp) + qf(hm) == 10 + 10 * t * t
    check("R03", ok, "stock table (7 values, h, Q), E_Z=80 H_Z=33+14phi Sigma_Z=(-4,-10,-6,-10), input accounts 39+10t^2 / 119+10t^2, residues")


def state15(t):
    return input_I(t) + stock_Z()


def r04():
    ok = True
    exp_par = {-2: (1, 0, 1, 1), -1: (0, 1, 1, 0), 0: (1, 1, 0, 0), 1: (0, 0, 0, 1), 2: (1, 0, 1, 0)}
    pars = set()
    for t in range(-2, 3):
        st = state15(t)
        init = list(st)
        tr = []
        apply_ops_checked(st, word_P(), tr)
        exp_tr = ("A" if t % 2 == 0 else "R") + ("A" if abs(t) == 2 else "R") + ("A" if abs(t) == 1 else "R")
        ok &= "".join(tr) == exp_tr
        ok &= st[0] == X_S[t]
        ok &= mod2(st[0]) == exp_par[t]
        pars.add(mod2(st[0]))
        apply_ops_checked(st, inverse_ops(word_P()))
        ok &= st == init
    ok &= len(pars) == 5 and (0, 0, 0, 0) not in pars
    check("R04", ok, "separator traces (even|+-2|+-1), x_t values, five distinct nonzero parities, P^-1 restores")


def r05():
    ok = True
    n = 0
    for t in range(-2, 3):
        base = state15(t)
        apply_ops_checked(base, word_P())
        for s in (-1, 0, 1, 2):
            n += 1
            st = list(base)
            ds = 12 + s
            tr = []
            apply_ops_checked(st, word_M(s)[:1], tr)
            if t != s:
                ok &= tr == ["R"] and st == base
                apply_ops_checked(st, word_M(s)[1:], tr)
                ok &= tr == ["R", "R"] and st == base
            else:
                ok &= tr == ["A"] and st[ds] == ZERO and st[0] == add(X_S[s], d_ref(s))
                apply_ops_checked(st, word_M(s)[1:], tr)
                ok &= tr == ["A", "A"] and st[ds] == B and st[5] == J
            apply_ops_checked(st, inverse_ops(word_M(s)))
            ok &= st == base
    check("R05", ok, f"markers on {n} (t,s) pairs: refuse off-sample, zero reference and gate J on sample, M^-1 restores")


def r06():
    ok = True
    n = 0
    for p in (1, 2, 3, 4):
        # active
        st = [ZERO] * 15
        st[5] = J
        st[6], st[7] = J, neg(J)
        tr = []
        apply_ops_checked(st, word_W(p), tr)
        exp = "A" + "R" * (5 - p) + "AAAA" + "A" * p
        ok &= "".join(tr) == exp
        ok &= st[5] == J and (st[6], st[7]) == (mul(rot(p), J), neg(mul(rot(p), J)))
        n += 1
        # inactive on every phase
        for r in range(5):
            st = [ZERO] * 15
            st[5] = TWO
            st[6], st[7] = mul(rot(r), J), neg(mul(rot(r), J))
            tr = []
            apply_ops_checked(st, word_W(p), tr)
            ok &= "".join(tr) == "R" + "A" * (5 - p) + "RRRR" + "A" * p
            ok &= st[5] == TWO and (st[6], st[7]) == (mul(rot(r), J), neg(mul(rot(r), J)))
            n += 1
    check("R06", ok, f"writer cases={n}: active phase-zero rotation to p, inactive identity on every phase, gate restored")


TRACES: dict = {}


def compile_run(A_ops, inputs, stock, checked=True):
    """Run A on each input+stock; returns (ok, traces, endpoints, cuts)."""
    ok = True
    traces = {}
    ends = {}
    cuts = 0
    for t, I in inputs.items():
        st = I + list(stock)
        init = list(st)
        tr = []
        if checked:
            apply_ops_checked(st, A_ops, tr)
        else:
            apply_ops(st, A_ops, tr)
        target = init[:6] + list(clock_target(t)) + list(stock)
        ok &= st == target
        changed = [i for i in range(15) if st[i] != init[i]]
        ok &= changed == [6, 7] or (t == -2 and changed == [])
        traces[t] = "".join(tr)
        ends[t] = tuple(st)
        inv = inverse_ops(A_ops)
        if checked:
            apply_ops_checked(st, inv)
        else:
            apply_ops(st, inv)
        ok &= st == init
        cuts += len(A_ops) + len(inv)
    return ok, traces, ends, cuts


def r07():
    A_ops = word_A()
    ok = len(A_ops) == 95
    inputs = {t: input_I(t) for t in range(-2, 3)}
    ok2, traces, ends, cuts = compile_run(A_ops, inputs, stock_Z())
    ok &= ok2 and cuts == 2375
    TRACES.update(traces)
    tl = [traces[t] for t in range(-2, 3)]
    ok &= len(set(tl)) == 5
    for i in range(4):
        ok &= tl[i] != tl[i + 1]
    adm = {t: traces[t].count("A") for t in range(-2, 3)}
    fp_w = sha(ser_ops(A_ops))
    fp_tr = sha("\n".join(tl) + "\n")
    fp_end = sha("\n".join(ser_state(ends[t]) for t in range(-2, 3)) + "\n")
    check("R07", ok, f"compiler |A|=95 endpoints exact for t=-2..2, only slots 6,7 change, inverse 380, cuts={cuts}, "
                     f"admitted_per_t={[adm[t] for t in range(-2, 3)]} FP_WORD={fp_w} FP_TRACES={fp_tr} FP_ENDPOINTS={fp_end}")
    return A_ops


CASES = [[(n, t)] for n in (0, 1) for t in range(-2, 3)] + [
    [(0, -2), (1, 2)], [(1, -1), (0, 1)], [(0, 0), (1, 0)], [(0, -2), (1, 2), (0, 0)]]


def r08(A_ops, W_ops, Winv_ops):
    ok = True
    aux_by_k = {}
    for seq in CASES:
        st, k = initial_assembly(seq)
        ok &= len(st) == 39 + 25 * k
        st2 = sum(t * t for (_, t) in seq)
        tot, hh, q, _ = full_invariants(st)
        ok &= q == 177 + 78 * k + 10 * st2
        ok &= hh == (70 + 30 * k + 4 * st2, 37 + 18 * k + 2 * st2)
        ok &= tot == (1 + 4 * k, -9 - 2 * k, -6, -12)
        input_slots = {0, 1, 2, 31, 32}
        for i in range(1, k):
            cb = cartridge_base(k, i)
            input_slots |= set(range(cb, cb + 5))
        aux = tuple(st[i] for i in range(len(st)) if i not in input_slots)
        ok &= len(aux) == 39 + 20 * k and sum(qf(v) for v in aux) == 177 + 60 * k
        ok &= aux_by_k.setdefault(k, aux) == aux
        for (a_base, b_base) in archive_bases(k):
            ok &= sum(qf(st[i]) for i in range(a_base, a_base + 20)) == 60
        segs = assembly_program(k, A_ops, W_ops, Winv_ops)
        fwd = [op for _, ops in segs for op in ops]
        nc = sum(1 for op in fwd if op[0] == "C")
        ns = sum(1 for op in fwd if op[0] == "S")
        inv = inverse_ops(fwd)
        ok &= nc == 27345 * k and ns == 5 * (k - 1)
        ok &= sum(1 for op in inv if op[0] == "C") == 109380 * k and sum(1 for op in inv if op[0] == "S") == 5 * (k - 1)
    check("R08", ok, "assembly formulas from built states: N=39+25k, E=177+78k+10sum t^2, H, Sigma, common aux 177+60k, archives 60, word counts 27345k / 109380k, swaps 5(k-1)")


def r09(path):
    S_ops, lengths = build_S()
    ok = len(S_ops) == 535
    ok &= lengths == {"L": 10, "SCAN": 80, "E": 10, "WA": 105, "WB": 105, "D": 9, "V": 23, "R": 261, "S": 535}
    file_ops = read_word535(path)
    ok &= file_ops == S_ops
    W_ops = rep(S_ops, 10)
    Winv_ops = inverse_ops(W_ops)
    ok &= len(W_ops) == 5350 and len(Winv_ops) == 21400
    K = word_K(11, 31)
    ok &= len(K) == 60 and len(W_ops) + 2 * len(K) + len(Winv_ops) == 26870
    for r in range(5):
        st = [ZERO] * 11 + bank_marked(r) + bank_empty() + bank_empty()
        before = STATS["admitted"]
        inv0 = full_invariants(st)
        apply_ops(st, word_K(11, 21))
        ok &= st[11:21] == bank_marked(r) and st[21:31] == bank_marked(r) and full_invariants(st) == inv0
        ok &= STATS["admitted"] - before == 41
        apply_ops(st, inverse_ops(word_K(11, 21)))
        ok &= st[11:21] == bank_marked(r) and st[21:31] == bank_empty()
    check("R09", ok, f"S from blocks == WORD535.txt contact by contact (535), block lengths, |W|=5350 |W^-1|=21400 |K|=60 |U|=26870, "
                     f"K copies M[r] with 41/60 admitted, FP_S={sha(ser_ops(S_ops))}")
    return S_ops, W_ops, Winv_ops


def r10(S_ops, W_ops, Winv_ops):
    ok = True
    # source period
    ys = [tuple(source_Y(n)) for n in range(10)]
    ok &= len(set(ys[:9])) == 9 and ys[9] == ys[0]
    delta = {0: 1, 1: 8}
    for n in (0, 1):
        for r in range(5):
            st = core_I(n, r)
            init = list(st)
            inv0 = full_invariants(st)
            for step in range(10):
                apply_ops(st, S_ops)
                ok &= full_invariants(st) == inv0
            exp = source_Y((n + 10) % 9) + clock_X(r) + list(CONTROLS) + bank_marked((-r) % 5) + bank_marked((-r - delta[n]) % 5)
            ok &= st == exp
            apply_ops(st, Winv_ops)
            ok &= st == init
    check("R10", ok, "stopwatch W on all 10 ready cores == closed form (Y_(n+10), X_r, controls, M[-r], M[-r-Delta_n]); W^-1 restores; invariants at every S boundary")


def r11(A_ops, W_ops, Winv_ops):
    ok = True
    delta = {0: 1, 1: 8}
    c0, s0 = STATS["contacts"], STATS["swaps"]
    boundaries = 0
    finals = []
    fresh_profile_ok = True
    for seq in CASES:
        st, k = initial_assembly(seq)
        init = list(st)
        inv0 = full_invariants(st)
        boundaries += 1
        segs = assembly_program(k, A_ops, W_ops, Winv_ops)
        done_archives = {}
        prev = list(st)
        bases = archive_bases(k)
        fresh_counts = [sum(1 for (a, b) in bases if st[a:a + 10] == bank_empty() and st[b:b + 10] == bank_empty())]
        for label, ops in segs:
            # residue equality check for swaps is inside apply_ops
            apply_ops(st, ops)
            boundaries += 1
            if full_invariants(st) != inv0:
                ok = False
            kind = label.rstrip("0123456789")
            i = int(label[len(kind):])
            n, t = seq[i]
            r = (t + 2) % 5
            a_base, b_base = bases[i]
            if kind == "A":
                exp = list(prev)
                exp[3], exp[4] = clock_X(r)
                ok &= st == exp
            elif kind == "W":
                exp = list(prev)
                exp[0:3] = source_Y((n + 10) % 9)
                exp[11:21] = bank_marked((-r) % 5)
                exp[21:31] = bank_marked((-r - delta[n]) % 5)
                ok &= st == exp
            elif kind == "KA":
                exp = list(prev)
                exp[a_base:a_base + 10] = bank_marked((-r) % 5)
                ok &= st == exp
            elif kind == "KB":
                exp = list(prev)
                exp[b_base:b_base + 10] = bank_marked((-r - delta[n]) % 5)
                ok &= st == exp
            elif kind == "Winv":
                exp = list(prev)
                exp[0:31] = core_I(n, r)
                ok &= st == exp
            elif kind == "Ainv":
                exp = list(prev)
                exp[3], exp[4] = clock_X(0)
                ok &= st == exp
                ok &= st[31:37] == input_I(t)[:6] and st[37:44] == stock_Z()
                done_archives[i] = (tuple(st[a_base:a_base + 10]), tuple(st[b_base:b_base + 10]))
                fresh_counts.append(sum(1 for (a, b) in bases if st[a:a + 10] == bank_empty() and st[b:b + 10] == bank_empty()))
            elif kind == "SWAP":
                exp = list(prev)
                cb = cartridge_base(k, i + 1)
                for src, dst in zip((0, 1, 2, 31, 32), range(cb, cb + 5)):
                    exp[src], exp[dst] = prev[dst], prev[src]
                ok &= st == exp
                n2, t2 = seq[i + 1]
                ok &= st[0:3] == source_Y(n2) and (st[31], st[32]) == heights(t2)
                ok &= st[cb:cb + 3] == source_Y(n) and (st[cb + 3], st[cb + 4]) == heights(t)
            # earlier archives untouched
            for j, (ar, br) in done_archives.items():
                aj, bj = bases[j]
                ok &= tuple(st[aj:aj + 10]) == ar and tuple(st[bj:bj + 10]) == br
            prev = list(st)
        # decode from archives only
        decoded = []
        for (a_base, b_base) in bases:
            pa = bank_label(st[a_base:a_base + 10])
            pb = bank_label(st[b_base:b_base + 10])
            if pa is None or pb is None:
                decoded.append(None)
                continue
            d = (pa - pb) % 5
            if d == 1:
                n_dec = 0
            elif d == 3:
                n_dec = 1
            else:
                decoded.append(None)
                continue
            r_dec = (-pa) % 5
            decoded.append((n_dec, r_dec - 2))
        ok &= decoded == seq
        fresh_profile_ok &= fresh_counts == list(range(k, -1, -1))
        ok &= st[11:21] == bank_empty() and st[21:31] == bank_empty()
        ok &= all(st[a:a + 10] != bank_empty() and st[b:b + 10] != bank_empty() for (a, b) in bases)
        finals.append(ser_state(st))
        # full literal inverse
        fwd = [op for _, ops in segs for op in ops]
        apply_ops(st, inverse_ops(fwd))
        boundaries += 1
        ok &= st == init and full_invariants(st) == inv0
    contacts = STATS["contacts"] - c0
    swaps = STATS["swaps"] - s0
    ok &= contacts == 2597775 and swaps == 50
    check("R11", ok, f"assembly cases={len(CASES)} cycles=19 boundaries={boundaries} contacts={contacts} swaps={swaps} "
                     f"archives untouched, decode==input, full inverse restores, FP_FINALS={sha(chr(10).join(finals) + chr(10))}")
    check("R12", fresh_profile_ok, "fresh archive pairs per stage k,k-1,...,0; work banks empty after each stage; no empty archive at the end")


def r13():
    ok = True
    classes = {mod2(U), mod2(ZERO)} | {mod2(mul(rot(b), J)) for b in range(5)}
    ok &= len(classes) == 7
    ok &= 2 * qf(B) == 10 and qf(sub(ONE, mul(RHO, RHO))) == 5 and mul(J, sub(ONE, RHO)) == sub(ONE, mul(RHO, RHO))
    for t in range(-2, 2):
        ok &= 39 + 10 * t * t != 39 + 10 * (t + 1) * (t + 1)
    tl = [TRACES[t] for t in range(-2, 3)]
    ok &= all(tl[i] != tl[i + 1] for i in range(4)) and len(set(tl)) >= 3
    check("R13", ok, "root-proof finite checks: bare-seed classes distinct mod 2, adjacent-height distance arithmetic, trace separation of A")


def r14(A_ops):
    inputs = {t: input_I(t) for t in range(-2, 3)}
    # mutant (a): clock seed (J, J)
    inputs_a = {t: input_I(t)[:7] + [J] for t in range(-2, 3)}
    det_a = False
    try:
        det_a = not compile_run(A_ops, inputs_a, stock_Z(), checked=False)[0]
    except AssertionError:
        det_a = True
    # mutant (b): a_2 = u + J B
    Zb = stock_Z()
    Zb[1] = add(U, mul(J, B))
    det_b = False
    try:
        det_b = not compile_run(A_ops, inputs, Zb, checked=False)[0]
    except AssertionError:
        det_b = True
    check("R14", det_a and det_b, f"mutant_seed_detected={det_a} mutant_a2_detected={det_b}")


def r15():
    edges = [C(a, b) for a in range(8) for b in range(a + 1, 8)]
    root = tuple(tuple(input_I(t)) for t in range(-2, 3))
    targets = [clock_target(t) for t in range(-2, 3)]

    def is_goal(node):
        return all((node[i][6], node[i][7]) == targets[i] for i in range(5))

    visited = {root}
    queue = deque([(root, 0)])
    count = 1
    result = None
    max_depth = 0
    unexpanded_depth6 = False
    while queue and result is None:
        node, depth = queue.popleft()
        if depth >= 6:
            # not expanded: children of depth-6 nodes are outside the depth cap
            unexpanded_depth6 = True
            continue
        for e in edges:
            child = []
            for stt in node:
                lst = list(stt)
                apply_ops(lst, (e,))
                child.append(tuple(lst))
            child = tuple(child)
            if child == node or child in visited:
                continue
            if count >= 20000:
                result = ("INCONCLUSIVE", "state cap")
                break
            visited.add(child)
            count += 1
            max_depth = max(max_depth, depth + 1)
            if is_goal(child):
                result = ("FOUND", f"depth {depth + 1}")
                break
            queue.append((child, depth + 1))
    if result is None:
        result = ("INCONCLUSIVE", "depth cap") if unexpanded_depth6 else ("NO_GOAL_IN_COMPLETE_ORBIT", "orbit exhausted")
    out(f"R15 OBSERVED bfs_result={result[0]} reason={result[1]} visited={count} max_depth={max_depth}")
    return result


def main() -> int:
    out("C-S3-HEIGHT-PHASE-INTERFACE-N-REVIEW-1 review.py")
    path = os.path.join("probes", "P-RELATIVE-CONTACT-VARIABLE-ARRIVAL-1", "WORD535.txt")
    build_y_table()
    r01()
    r02()
    r03()
    r04()
    r05()
    r06()
    A_ops = r07()
    S_ops, W_ops, Winv_ops = r09(path)
    r08(A_ops, W_ops, Winv_ops)
    r10(S_ops, W_ops, Winv_ops)
    r11(A_ops, W_ops, Winv_ops)
    r13()
    r14(A_ops)
    bfs = r15()
    out(f"TOTAL contacts={STATS['contacts']} admitted={STATS['admitted']} swaps={STATS['swaps']} distinct_pairs={STATS['pairs']}")
    out(f"CHECKS=14 FAILED={len(FAILS)}" + ("" if not FAILS else " " + ",".join(FAILS)) + f" BFS={bfs[0]}")
    out("RESULT PASS" if not FAILS else "RESULT FAILURE")
    sys.stdout.write("\n".join(LINES) + "\n")
    return 0 if not FAILS else 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except AssertionError as exc:
        sys.stdout.write("\n".join(LINES) + "\n")
        sys.stdout.write(f"ASSERTION {exc}\nRESULT FAILURE\n")
        sys.exit(1)
