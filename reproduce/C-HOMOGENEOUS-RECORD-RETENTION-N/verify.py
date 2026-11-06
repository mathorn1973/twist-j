#!/usr/bin/env python3
"""Exact standard-library verifier for C-HOMOGENEOUS-RECORD-RETENTION-N.

PUBLIC, NON-CANONICAL. Audit of the analytical retention theorems stated in
notes/C-HOMOGENEOUS-RECORD-RETENTION-N/PROOF.md for the law of the public
Canon v105 claim HOMOGENEOUS-CAPTURE-CURRENT-RECORD.

Uses only the Python standard library (fractions.Fraction, int, math.comb,
math.factorial, math.isqrt). No floating-point arithmetic, no file reads, no
network calls and no randomness. Assertions guard every exact gate.
"""

from __future__ import annotations

from fractions import Fraction as F
from math import comb, factorial, isqrt
import sys


# ============================================================================
# 0. Frozen parameters (PROTOCOL.md, section 4)
# ============================================================================

Z_REC = 100                 # receiver site z
H_WIN = F(1, 1000)          # half width h of the energy window I_E
P_ONE = F(1, 1000)          # object momentum half width p_1
W_K = F(1, 1000)            # pulse momentum half width w around k_0
N_IBP = 5                   # integrations by parts = bump order N_b
RHO_P = F(1, 10)            # complex radius rho_P for the bound branch
RHO_K = F(3, 10)            # complex radius rho_k for the pulse band
T_RET = 10 ** 6             # future-uniform window n >= T (macrosteps)
EPS_RET = F(1, 100)         # tolerance on ||(I - R1) psi_n||
M0 = F(440, 53)             # imported v105 resolvent bound, |w - z| = 1/8, P = 0
N_MIN = F(8424, 11449)      # imported v105 bound |<b_0, chi_b(P)>|^2, |P| <= 1/12
OM_SUP = F(1, 7)            # log(8/7) <= 1/7 bounds |Omega(P) - g| on the disk
PI_LO, PI_HI = F(333, 106), F(355, 113)
PREC = 10 ** 40
MODULUS_TABLE = (2 * 10 ** 5, 5 * 10 ** 5, 10 ** 6, 10 ** 7)
SIM_STEPS = 4               # exact physical-law steps in group 2
DARK_STEPS = 5              # exact steps for the eternal dark-token record


CHECKS = {"n": 0}


def check(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)
    CHECKS["n"] += 1


# ============================================================================
# 1. Certified rational bounds
# ============================================================================

def sqrt_lo(x: F) -> F:
    """Rational lower bound of sqrt(x) for x >= 0."""
    x = F(x)
    assert x >= 0
    n = (x.numerator * PREC * PREC) // x.denominator
    return F(isqrt(n), PREC)


def sqrt_hi(x: F) -> F:
    """Rational upper bound of sqrt(x) for x >= 0."""
    x = F(x)
    assert x >= 0
    n = -((-x.numerator * PREC * PREC) // x.denominator)
    r = isqrt(n)
    if r * r < n:
        r += 1
    return F(r, PREC)


def exp_hi(x: F, terms: int = 40) -> F:
    """Rational upper bound of exp(x) for 0 <= x <= 1."""
    x = F(x)
    assert 0 <= x <= 1
    total, term = F(0), F(1)
    for j in range(terms):
        total += term
        term = term * x / (j + 1)
    return total + 3 * term


def sci(x: F, digits: int = 4, up: bool = True) -> str:
    """Deterministic decimal mantissa/exponent rounded up (or down)."""
    x = F(x)
    assert x > 0
    e = 0
    while x >= F(10) ** (e + 1):
        e += 1
    while x < F(10) ** e:
        e -= 1
    scaled = x / F(10) ** e * 10 ** (digits - 1)
    m = -((-scaled.numerator) // scaled.denominator) if up else scaled.numerator // scaled.denominator
    if m >= 10 ** digits:
        m //= 10
        e += 1
    s = str(m)
    return f"{s[0]}.{s[1:]}e{e:+d}"


# ============================================================================
# 2. Exact arithmetic in Z[i][zeta_5] (zeta = exp(2 pi i / 5))
# ============================================================================
# An element is a 10-tuple (r0, i0, ..., r4, i4) for sum_j (r_j + i i_j) zeta^j
# modulo 1 + zeta + ... + zeta^4 = 0.

ZERO = (0,) * 10


def f_gauss(gr: int, gi: int) -> tuple:
    return (gr, gi) + (0,) * 8


def f_add(a: tuple, b: tuple) -> tuple:
    return tuple(x + y for x, y in zip(a, b))


def f_sub(a: tuple, b: tuple) -> tuple:
    return tuple(x - y for x, y in zip(a, b))


def f_int(a: tuple, m: int) -> tuple:
    return tuple(m * x for x in a)


def f_gmul(a: tuple, gr: int, gi: int) -> tuple:
    out = []
    for j in range(5):
        r, im = a[2 * j], a[2 * j + 1]
        out += [gr * r - gi * im, gr * im + gi * r]
    return tuple(out)


def f_rot(a: tuple, p: int) -> tuple:
    out = [0] * 10
    for j in range(5):
        t = (j + p) % 5
        out[2 * t], out[2 * t + 1] = a[2 * j], a[2 * j + 1]
    return tuple(out)


def f_conj(a: tuple) -> tuple:
    out = [0] * 10
    for j in range(5):
        t = (-j) % 5
        out[2 * t], out[2 * t + 1] = a[2 * j], -a[2 * j + 1]
    return tuple(out)


def f_mul(a: tuple, b: tuple) -> tuple:
    out = [0] * 10
    for j in range(5):
        ar, ai = a[2 * j], a[2 * j + 1]
        if ar == 0 and ai == 0:
            continue
        for k in range(5):
            br, bi = b[2 * k], b[2 * k + 1]
            if br == 0 and bi == 0:
                continue
            t = (j + k) % 5
            out[2 * t] += ar * br - ai * bi
            out[2 * t + 1] += ar * bi + ai * br
    return tuple(out)


def f_canon(a: tuple) -> tuple:
    r4, i4 = a[8], a[9]
    return tuple(a[j] - (r4 if j % 2 == 0 else i4) for j in range(10))


def f_iszero(a: tuple) -> bool:
    return f_canon(a) == ZERO


def f_norm(a: tuple) -> tuple:
    return f_mul(f_conj(a), a)


def add_to(state: dict, key: tuple, value: tuple) -> None:
    current = state.get(key)
    new = value if current is None else f_add(current, value)
    if f_iszero(new):
        state.pop(key, None)
    else:
        state[key] = new


def states_equal(a: dict, b: dict) -> bool:
    keys = set(a) | set(b)
    return all(f_iszero(f_sub(a.get(k, ZERO), b.get(k, ZERO))) for k in keys)


def total_weight(state: dict, predicate) -> tuple:
    total = ZERO
    for key, value in state.items():
        if predicate(key):
            total = f_add(total, f_norm(value))
    return f_canon(total)


# ============================================================================
# 3. The v105 law in integer form (scale 125 per macrostep, global e^{-i beta}
#    omitted on the one-carrier sector)
# ============================================================================
# Token key:  ('T', R, r, d, y, lab, mem, ref)
# Pulse key:  ('P', R, r, d, x, b, lab, mem, ref)
# Object coins d = 0..3 are (++, +-, -+, --); pulse banks b = 0, 1.

M5 = (  # 5 * M_2 as Gaussian integers (re, im)
    ((1, 0), (0, 2), (0, 2), (-4, 0)),
    ((0, 2), (1, 0), (-4, 0), (0, 2)),
    ((0, 2), (-4, 0), (1, 0), (0, 2)),
    ((-4, 0), (0, 2), (0, 2), (1, 0)),
)
DISP = ((-1, 0), (0, -1), (0, 1), (1, 0))  # (delta R, delta r) per coin


def contact_pass(state: dict) -> dict:
    """Integer form 5*C of the homogeneous contact on all labels."""
    out: dict = {}
    for key, value in state.items():
        add_to(out, key, f_int(value, 5))
    sites = set()
    for key in state:
        if key[0] == "T":
            _, R, r, d, y, lab, mem, ref = key
            if r == 0 and R == y and d in (1, 2):
                sites.add((R, lab, mem, ref))
        else:
            _, R, r, d, x, b, lab, mem, ref = key
            if r == 0 and R == x and b == 0 and d in (0, 3):
                sites.add((R, lab, mem, ref))
    for s, lab, mem, ref in sorted(sites, key=repr):
        t1 = state.get(("T", s, 0, 1, s, lab, mem, ref), ZERO)
        t2 = state.get(("T", s, 0, 2, s, lab, mem, ref), ZERO)
        p0 = state.get(("P", s, 0, 0, s, 0, lab, mem, ref), ZERO)
        p3 = state.get(("P", s, 0, 3, s, 0, lab, mem, ref), ZERO)
        alpha = f_gmul(f_sub(t1, t2), 0, -1)          # sqrt2 <a, psi>
        beta = f_sub(p0, p3)                          # sqrt2 <b, psi>
        x_tok = f_gmul(f_sub(f_int(alpha, -1), f_int(beta, 2)), 0, 1)
        y_pul = f_sub(f_int(alpha, 2), beta)
        add_to(out, ("T", s, 0, 1, s, lab, mem, ref), x_tok)
        add_to(out, ("T", s, 0, 2, s, lab, mem, ref), f_int(x_tok, -1))
        add_to(out, ("P", s, 0, 0, s, 0, lab, mem, ref), y_pul)
        add_to(out, ("P", s, 0, 3, s, 0, lab, mem, ref), f_int(y_pul, -1))
    return out


def coin_pass(state: dict) -> dict:
    """Integer form 5*M_2 on the object coin."""
    out: dict = {}
    for key, value in state.items():
        d = key[3]
        for a in range(4):
            gr, gi = M5[a][d]
            new = key[:3] + (a,) + key[4:]
            add_to(out, new, f_gmul(value, gr, gi))
    return out


def carrier_pass(state: dict, z: int, physical: bool) -> dict:
    """Integer form 5*E*Q on pulses (receiver SWAP at bond (z-1, z) when
    physical), and 5*I on standing tokens."""
    out: dict = {}
    for key, value in state.items():
        if key[0] == "T":
            add_to(out, key, f_int(value, 5))
            continue
        _, R, r, d, x, b, lab, mem, ref = key
        u1 = value if b == 0 else f_int(value, -2)
        u2 = f_int(value, 2) if b == 0 else value
        # bank-1 amplitude u1 at x: stays (coefficient 1) or hops to bank 2 at x+1
        add_to(out, ("P", R, r, d, x, 0, lab, mem, ref), u1)
        swap = physical and x == z - 1
        l2, m2 = (mem, lab) if swap else (lab, mem)
        add_to(out, ("P", R, r, d, x + 1, 1, l2, m2, ref), f_int(u1, 2))
        # bank-2 amplitude u2 at x: stays or hops to bank 1 at x-1
        add_to(out, ("P", R, r, d, x, 1, lab, mem, ref), u2)
        swap = physical and x == z
        l1, m1 = (mem, lab) if swap else (lab, mem)
        add_to(out, ("P", R, r, d, x - 1, 0, l1, m1, ref), f_int(u2, -2))
    return out


def shift_phase_pass(state: dict) -> dict:
    """Object streaming S followed by the contact phase Gamma at r = 0."""
    out: dict = {}
    for key, value in state.items():
        dR, dr = DISP[key[3]]
        R, r = key[1] + dR, key[2] + dr
        new = (key[0], R, r) + key[3:]
        add_to(out, new, f_rot(value, 4) if r == 0 else value)
    return out


def law_step(state: dict, z: int, physical: bool) -> dict:
    state = contact_pass(state)
    state = coin_pass(state)
    state = carrier_pass(state, z, physical)
    return shift_phase_pass(state)


def calibrate(state: dict, z: int) -> dict:
    """The half-line calibration T: swap carrier and memory labels at y, x >= z."""
    out: dict = {}
    for key, value in state.items():
        if key[0] == "T":
            _, R, r, d, y, lab, mem, ref = key
            if y >= z:
                key = ("T", R, r, d, y, mem, lab, ref)
        else:
            _, R, r, d, x, b, lab, mem, ref = key
            if x >= z:
                key = ("P", R, r, d, x, b, mem, lab, ref)
        add_to(out, key, value)
    return out


def carrier_left(z: int):
    # index 4 is the token site y or the pulse site x
    def predicate(key: tuple) -> bool:
        return key[4] < z
    return predicate


def tensor_memory(spatial: dict, phi: dict) -> dict:
    """chi (label index 1) tensor sum_k |d_k> phi_k on the reference."""
    out: dict = {}
    for key, value in spatial.items():
        for (k, ref), (gr, gi) in phi.items():
            if key[0] == "T":
                new = key[:5] + (1, k, ref)
            else:
                new = key[:6] + (1, k, ref)
            add_to(out, new, f_gmul(value, gr, gi))
    return out


# ============================================================================
# GROUP 1: LABEL_ALGEBRA (Theorem 1 on the complete 26-label alphabet)
# ============================================================================

def audit_label_algebra(n_labels: int = 26) -> int:
    start = CHECKS["n"]
    labels = range(n_labels)
    swap = {(j, k): (k, j) for j in labels for k in labels}
    check(all(swap[swap[p]] == p for p in swap), "J involution on 676 pairs")
    check(all(swap[(1, k)] == (k, 1) for k in labels), "J(e_1 x d_k) = e_k x d_1")
    # Two-site calibrated vector: left amplitude cl at z-1, right cr at z.
    cl, cr = (2, -1), (1, 3)
    phi = {(k, ref): ((k + 1) * (1 - 2 * ref), (k % 3) - ref) for k in labels for ref in (0, 1)}
    phys = {}
    for (k, ref), (pr, pi) in phi.items():
        left = (cl[0] * pr - cl[1] * pi, cl[0] * pi + cl[1] * pr)
        right = (cr[0] * pr - cr[1] * pi, cr[0] * pi + cr[1] * pr)
        phys[("L", 1, k, ref)] = left
        phys[("R", k, 1, ref)] = right       # calibration swaps on the right
    wrong = sum(a * a + b * b for (side, lab, mem, ref), (a, b) in phys.items() if mem != 1)
    norm_cl = cl[0] ** 2 + cl[1] ** 2
    off = sum(a * a + b * b for (k, ref), (a, b) in phi.items() if k != 1)
    check(wrong == norm_cl * off, "wrong-memory weight = |left|^2 (1 - |phi_1|^2)")
    ideal = {}
    for (k, ref), (pr, pi) in phi.items():
        ideal[("L", k, 1, ref)] = (cl[0] * pr - cl[1] * pi, cl[0] * pi + cl[1] * pr)
        ideal[("R", k, 1, ref)] = phys[("R", k, 1, ref)]
    keys = set(phys) | set(ideal)
    dev = 0
    for key in keys:
        a = phys.get(key, (0, 0))
        b = ideal.get(key, (0, 0))
        dev += (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
    check(dev == 2 * norm_cl * off, "full-record deviation = 2 |left|^2 (1 - |phi_1|^2)")
    check(all(phys[("R", k, 1, ref)] == (cr[0] * phi[(k, ref)][0] - cr[1] * phi[(k, ref)][1],
                                          cr[0] * phi[(k, ref)][1] + cr[1] * phi[(k, ref)][0])
              for (k, ref) in phi), "old memory/reference amplitudes sit in the carrier label")
    n = CHECKS["n"] - start
    print(f"PASS GROUP 1 LABEL_ALGEBRA: {n} checks; {n_labels} labels; {len(swap)} swap pairs")
    return n


# ============================================================================
# GROUP 2: PHYSICAL_CONJUGACY (exact local law versus calibrated evolution)
# ============================================================================

def initial_spatial(z: int) -> dict:
    s: dict = {}
    g = f_gauss
    # token at y = z-1 in contact configuration (iB coin), will emit at z-1
    add_to(s, ("T", z - 1, 0, 1, z - 1, 1, None, None), g(0, 1))
    add_to(s, ("T", z - 1, 0, 2, z - 1, 1, None, None), g(0, -1))
    add_to(s, ("T", z - 1, 0, 0, z - 1, 1, None, None), g(1, 0))
    # token at y = z, right of the receiver, contact configuration
    add_to(s, ("T", z, 0, 1, z, 1, None, None), g(1, 1))
    add_to(s, ("T", z, 0, 2, z, 1, None, None), g(-1, -1))
    add_to(s, ("T", z, 0, 3, z, 1, None, None), g(2, 0))
    # pulse at x = z-2 with a distant object
    add_to(s, ("P", z - 7, 1, 3, z - 2, 0, 1, None, None), g(1, 0))
    add_to(s, ("P", z - 7, 1, 3, z - 2, 1, 1, None, None), g(0, 1))
    # pulse at x = z+1 in partial contact configuration (A coin, bank 1)
    add_to(s, ("P", z + 1, 0, 0, z + 1, 0, 1, None, None), g(1, 0))
    add_to(s, ("P", z + 1, 0, 3, z + 1, 0, 1, None, None), g(-1, 0))
    add_to(s, ("P", z + 1, 0, 0, z + 1, 1, 1, None, None), g(0, 2))
    return s


PHI_TEST = {(0, 0): (1, 0), (0, 1): (0, 1), (1, 0): (2, 0), (1, 1): (1, 0), (2, 0): (0, 0), (2, 1): (1, -1)}


def current_increment(state: dict, z: int) -> tuple:
    """2 * (-4) * (|U1(z-1)|^2 - |U2(z)|^2 + Re<U1, SWAP U2>) in field form, where
    U = sqrt5 * Q applied after 5C and 5M_2; equals 2 (L_{n+1} - 125^2 L_n)."""
    phi = coin_pass(contact_pass(state))
    u1, u2 = {}, {}
    for key, value in phi.items():
        if key[0] != "P":
            continue
        _, R, r, d, x, b, lab, mem, ref = key
        if x == z - 1:
            add_to(u1, (R, r, d, lab, mem, ref), value if b == 0 else f_int(value, -2))
        if x == z:
            add_to(u2, (R, r, d, lab, mem, ref), f_int(value, 2) if b == 0 else value)
    n1 = total_weight(u1, lambda k: True)
    n2 = total_weight(u2, lambda k: True)
    cross = ZERO
    for (R, r, d, lab, mem, ref), value in u1.items():
        other = u2.get((R, r, d, mem, lab, ref))
        if other is not None:
            cross = f_add(cross, f_mul(f_conj(value), other))
    inner = f_add(f_sub(f_int(n1, 2), f_int(n2, 2)), f_add(cross, f_conj(cross)))
    return f_canon(f_int(inner, -4))


def audit_physical_conjugacy(z: int = Z_REC, steps: int = SIM_STEPS) -> int:
    start = CHECKS["n"]
    spatial = initial_spatial(z)
    phys = calibrate(tensor_memory(spatial, PHI_TEST), z)
    off = sum(gr * gr + gi * gi for (k, ref), (gr, gi) in PHI_TEST.items() if k != 1)
    left = carrier_left(z)
    crossings = 0
    for n in range(steps + 1):
        expected = calibrate(tensor_memory(spatial, PHI_TEST), z)
        check(states_equal(phys, expected), f"U_rec^n = T (U^n x I) T* at n={n}")
        wrong = total_weight(phys, lambda k: k[-2] != 1)
        lam = total_weight(spatial, left)
        check(f_canon(f_int(lam, off)) == wrong, f"wrong-memory identity at n={n}")
        if n < steps:
            inc = current_increment(phys, z)
            nxt_phys = law_step(phys, z, True)
            nxt_spatial = law_step(spatial, z, False)
            check(f_canon(f_int(total_weight(phys, lambda k: True), 15625))
                  == total_weight(nxt_phys, lambda k: True), f"unitarity of the local law at n={n}")
            lam_phys = total_weight(phys, left)
            lam_next = total_weight(nxt_phys, left)
            lhs = f_canon(f_int(f_sub(lam_next, f_int(lam_phys, 15625)), 2))
            check(lhs == inc, f"record increment = -(1/4) carrier cut current at n={n}")
            if not f_iszero(inc):
                crossings += 1
            phys, spatial = nxt_phys, nxt_spatial
    check(crossings > 0, "nontrivial receiver-bond flux occurs")
    # negative controls: no receiver swap, or the swap on the wrong bond
    first = calibrate(tensor_memory(law_step(initial_spatial(z), z, False), PHI_TEST), z)
    start_phys = calibrate(tensor_memory(initial_spatial(z), PHI_TEST), z)
    check(not states_equal(law_step(start_phys, z, False), first), "negative control: free edge fails")
    check(not states_equal(law_step(start_phys, z + 1, True), first), "negative control: shifted edge fails")
    n = CHECKS["n"] - start
    print(f"PASS GROUP 2 PHYSICAL_CONJUGACY: {n} checks; steps={steps}; "
          f"physical keys={len(phys)}; nonzero bond-flux steps={crossings}")
    return n


# ============================================================================
# GROUP 3: RECROSSING_AND_NO_PARKING
# ============================================================================

def lp_mul(a: dict, b: dict) -> dict:
    out: dict = {}
    for i, x in a.items():
        for j, y in b.items():
            out[i + j] = out.get(i + j, 0) + x * y
    return {k: v for k, v in out.items() if v}


def lp_add(*ps: dict) -> dict:
    out: dict = {}
    for p in ps:
        for k, v in p.items():
            out[k] = out.get(k, 0) + v
    return {k: v for k, v in out.items() if v}


def lp_scale(p: dict, c) -> dict:
    return {k: c * v for k, v in p.items() if c * v}


def pulse_step_1d(state: dict) -> dict:
    """Integer form 5*E*Q of the free pulse on l^2(Z) x C^2."""
    out: dict = {}
    for (x, b), v in state.items():
        u1 = v if b == 0 else -2 * v
        u2 = 2 * v if b == 0 else v
        for key, val in (((x, 0), u1), ((x + 1, 1), 2 * u1), ((x, 1), u2), ((x - 1, 0), -2 * u2)):
            out[key] = out.get(key, 0) + val
    return {k: v for k, v in out.items() if v}


def audit_recrossing_and_no_parking(z: int = Z_REC) -> int:
    start = CHECKS["n"]
    # V(w) with w = e^{-ik}: entries as Laurent polynomials in w.
    v11 = {0: F(1, 5), -1: F(-4, 5)}
    v12 = {0: F(-2, 5), -1: F(-2, 5)}
    v21 = {0: F(2, 5), 1: F(2, 5)}
    v22 = {0: F(1, 5), 1: F(-4, 5)}
    det = lp_add(lp_mul(v11, v22), lp_scale(lp_mul(v12, v21), -1))
    check(det == {0: 1}, "det V(w) = 1 identically")
    tr = lp_add(v11, v22)
    check(tr == {0: F(2, 5), 1: F(-4, 5), -1: F(-4, 5)}, "tr V = (2 - 4w - 4/w)/5")
    disc = lp_add(lp_mul(tr, tr), {0: -4})
    lhs = lp_scale(lp_mul({2: 1}, disc), 25)
    rhs = lp_scale(lp_mul(lp_mul({0: 1, 1: 1}, {0: 1, 1: 1}), {0: 1, 1: -3, 2: 1}), 16)
    check(lhs == rhs, "25 w^2 (tr^2 - 4) = 16 (w+1)^2 (w^2 - 3w + 1)")
    s5_lo, s5_hi = sqrt_lo(F(5)), sqrt_hi(F(5))
    w0_lo, w0_hi = (3 - s5_hi) / 2, (3 - s5_lo) / 2
    check(0 < w0_lo and w0_hi < 1, "branch point w0 = (3 - sqrt5)/2 lies in the open unit disk")
    check(s5_lo > 0, "w0 is a simple root (derivative 2 w0 - 3 = -sqrt5 != 0)")
    check(w0_lo > -1, "w0 differs from the double root w = -1")
    check(v12 == {0: F(-2, 5), -1: F(-2, 5)}, "V12 = -2(1 + 1/w)/5 vanishes on |w|=1 only at w=-1")
    # Exact light-cone recrossing witness: bank-2 pulse at x = z+2.
    state = {(z + 2, 1): 1}
    left_weights = []
    for m in range(4):
        left_weights.append(sum(v * v for (x, b), v in state.items() if x < z))
        total = sum(v * v for v in state.values())
        check(total == 25 ** m, f"free pulse unitarity at m={m}")
        if m < 3:
            state = pulse_step_1d(state)
    check(left_weights[:3] == [0, 0, 0], "record exactly held for m = 0, 1, 2")
    check(state.get((z - 1, 0)) == -32, "unique light-cone path amplitude -32/125 at x=z-1")
    check(F(left_weights[3], 25 ** 3) == F(1024, 15625), "recrossing weight 1024/15625 at m=3")
    n = CHECKS["n"] - start
    print(f"PASS GROUP 3 RECROSSING_AND_NO_PARKING: {n} checks; w0=(3-sqrt5)/2 simple; "
          f"left weight 0,0,0,1024/15625")
    return n


# ============================================================================
# GROUP 4: SYMMETRY_AND_DARK_RECORD
# ============================================================================

def object_step(state: dict) -> dict:
    """5 * W on object-only keys ('O', R, r, d)."""
    out: dict = {}
    for (tag, R, r, d), value in state.items():
        for a in range(4):
            gr, gi = M5[a][d]
            dR, dr = DISP[a]
            R2, r2 = R + dR, r + dr
            v = f_gmul(value, gr, gi)
            add_to(out, (tag, R2, r2, a), f_rot(v, 4) if r2 == 0 else v)
    return out


def reflect(state: dict, n: int) -> dict:
    out: dict = {}
    for (tag, R, r, d), value in state.items():
        add_to(out, (tag, 2 * n - R, -r, 3 - d), value)
    return out


def audit_symmetry_and_dark_record(z: int = Z_REC, steps: int = DARK_STEPS) -> int:
    start = CHECKS["n"]
    check(all(M5[3 - a][3 - b] == M5[a][b] for a in range(4) for b in range(4)),
          "J_c M_2 J_c = M_2")
    qc = (1, 0, 0, -1)
    check(all(qc[3 - a] == -qc[a] for a in range(4)), "J_c Q J_c = -Q, hence W(-P) = R W(P) R")
    check(all(DISP[3 - d] == (-DISP[d][0], -DISP[d][1]) for d in range(4)),
          "streaming displacements reverse under (R, r, d) -> (-R, -r, 3-d)")
    chi0 = {(0, 0, 0): 1, (0, 0, 3): -1}
    check(all(chi0.get((0, 0, 3 - d), 0) == -v for (_, _, d), v in chi0.items()),
          "R chi_0 = -chi_0, hence N(-P) = N(P)")
    n0 = z
    for R in range(n0 - 2, n0 + 3):
        for r in range(-2, 3):
            for d in range(4):
                e = {("O", R, r, d): f_gauss(1, 0)}
                check(states_equal(reflect(object_step(e), n0), object_step(reflect(e, n0))),
                      f"[R_n, W] = 0 on basis state {(R, r, d)}")
    # dark state of PROOF_CURRENT_RECORD_INTERFACE section 6.2 at token site n0 = z
    dark = {("O", n0 - 1, -1, 0): f_gauss(1, 0), ("O", n0 + 1, 1, 3): f_gauss(1, 0),
            ("O", n0 - 1, 1, 0): f_gauss(-1, 0), ("O", n0 + 1, -1, 3): f_gauss(-1, 0)}
    check(states_equal(reflect(dark, n0), dark), "R_n d = d")
    alpha = {("O", n0, 0, 1): f_gauss(0, 1), ("O", n0, 0, 2): f_gauss(0, -1)}
    check(states_equal(reflect(alpha, n0), {k: f_int(v, -1) for k, v in alpha.items()}),
          "R_n alpha_n = -alpha_n")
    cur = dict(dark)
    for m in range(9):
        overlap = ZERO
        for key, value in alpha.items():
            if key in cur:
                overlap = f_add(overlap, f_mul(f_conj(value), cur[key]))
        check(f_iszero(overlap), f"<alpha_n, W^m d> = 0 at m={m}")
        cur = object_step(cur)
    # eternal record: dark object with a token at y = z in the physical frame
    spatial = {}
    for (_, R, r, d), value in dark.items():
        add_to(spatial, ("T", R, r, d, z, 1, None, None), value)
    phys = calibrate(tensor_memory(spatial, PHI_TEST), z)
    for m in range(steps + 1):
        check(all(k[0] == "T" and k[4] == z and k[6] == 1 for k in phys),
              f"token parked at y=z with memory d_1 at m={m}")
        check(f_iszero(total_weight(phys, lambda k: k[6] != 1)), f"(I - R1) psi = 0 at m={m}")
        phys = law_step(phys, z, True)
    n = CHECKS["n"] - start
    print(f"PASS GROUP 4 SYMMETRY_AND_DARK_RECORD: {n} checks; Omega even; "
          f"dark token record held exactly for m=0..{steps}")
    return n


# ============================================================================
# GROUP 5-6: SUCCESS_SECTOR and RETENTION_CERTIFICATE
# ============================================================================

def poly_bump(order: int) -> list:
    c = [F(0)] * (2 * order + 1)
    for j in range(order + 1):
        c[2 * j] = F(comb(order, j) * (-1) ** j)
    return c


def poly_deriv(c: list) -> list:
    return [i * c[i] for i in range(1, len(c))] or [F(0)]


def poly_l1_bound(c: list) -> F:
    return sum((abs(ci) * F(2, i + 1) for i, ci in enumerate(c)), F(0))


def poly_square_integral(c: list) -> F:
    total = F(0)
    for i, a in enumerate(c):
        for j, b in enumerate(c):
            if (i + j) % 2 == 0:
                total += a * b * F(2, i + j + 1)
    return total


def ibp_terms(order: int) -> dict:
    """Expansion of L^N F with L F = (F / Phi')'. Keys (a, e, q): coefficient of
    F^(a) * prod_b (Phi^(b))^(e_b) * Phi'^(-q), b = 2..N+1."""
    terms = {(0, (0,) * order, 0): 1}
    for _ in range(order):
        new: dict = {}

        def put(key, c):
            new[key] = new.get(key, 0) + c

        for (a, e, q), c in terms.items():
            put((a + 1, e, q + 1), c)
            for idx, eb in enumerate(e):
                if eb:
                    e2 = list(e)
                    e2[idx] -= 1
                    e2[idx + 1] += 1
                    put((a, tuple(e2), q + 1), c * eb)
            e3 = list(e)
            e3[0] += 1
            put((a, tuple(e3), q + 2), -(q + 1) * c)
        terms = {k: v for k, v in new.items() if v}
    return terms


def ibp_constant(terms: dict, norms: list, ders: dict, kappa: F) -> F:
    total = F(0)
    for (a, e, q), c in terms.items():
        t = abs(c) * norms[a]
        for idx, eb in enumerate(e):
            if eb:
                t *= (ders[idx + 2] / kappa) ** eb
        total += t
    return total / (2 * PI_LO)


def retention_constants(z: int = Z_REC, order: int = N_IBP, p1: F = P_ONE, w: F = W_K,
                        rho_p: F = RHO_P, rho_k: F = RHO_K, h: F = H_WIN) -> dict:
    c: dict = {}
    s5_lo, s5_hi = sqrt_lo(F(5)), sqrt_hi(F(5))
    c0_lo, c0_hi = (9 - 5 * s5_hi) / 16, (9 - 5 * s5_lo) / 16
    g0_hi = (s5_hi - 1) / 4
    check(-1 < c0_lo < c0_hi < 1, "cos k0 = (9 - 5 sqrt5)/16 in (-1, 1)")
    check(c0_hi < 1 - w * w / 2 and c0_lo > -1 + w * w / 2,
          "pulse window [k0-w, k0+w] inside (-pi, 0): right-moving plus band")
    vel2 = lambda cc: 2 * (1 - cc) / (3 - 2 * cc)
    vmin = sqrt_lo(vel2(c0_hi + w))
    vmax = sqrt_hi(vel2(c0_lo - w))
    check(0 < vmin <= vmax < 1, "group velocity bounds 0 < v_min <= v_max < 1")
    check(p1 <= F(1, 100) and p1 <= F(1, 12), "object window inside |P| <= 1/100 and |P| <= 1/12")
    e_p = exp_hi(rho_p)
    q_p = M0 * (e_p - 1)
    check(q_p < 1, "complex Neumann product M0 (e^rho_P - 1) < 1")
    m_res = M0 / (1 - q_p)
    m_pi = m_res / 8
    r_p = rho_p - p1
    check(r_p > 0, "Cauchy radius r_P > 0")
    e_obj = {b: factorial(b) * OM_SUP / r_p ** b for b in range(2, order + 2)}
    v_b = p1 * e_obj[2]
    check(v_b < vmin, "bound-pair group velocity v_b < v_min")
    energy = vmax * w + p1 * p1 * e_obj[2] / 2
    check(energy <= h, "product states lie in the energy window I_E")
    e_k = exp_hi(rho_k)
    cosh_k = (e_k + 1) / 2
    r_g = F(4, 5) * (w + rho_k) * cosh_k
    check(1 - g0_hi - r_g > 0, "gamma disk avoids the arccos branch points")
    s_min = sqrt_lo((1 - r_g) ** 2 - g0_hi ** 2)
    check(s_min > 0, "|sin eps| bounded below on the k disk")
    r_eps = r_g / s_min
    e_pul = {b: factorial(b) * r_eps / rho_k ** b for b in range(2, order + 2)}
    s_max = sqrt_hi(1 + (g0_hi + r_g) ** 2)
    mp = {1: (1 + e_k) / (5 * s_min), 2: (F(4, 5) * cosh_k + s_max) / (2 * s_min)}
    bump = poly_bump(order)
    ders = [bump]
    for _ in range(order):
        ders.append(poly_deriv(ders[-1]))
    lb = [poly_l1_bound(dd) for dd in ders]
    ib = poly_square_integral(bump)
    check(ib > 0, "bump L2 integral positive")
    a_g = sqrt_hi(2 * PI_HI / (N_MIN * p1 * ib))
    a_h = sqrt_hi(2 * PI_HI / ((1 + vmin) / 2 * w * ib))

    def n_obj(j):
        return F(1) if j == 0 else factorial(j) * m_pi / r_p ** j

    def m_pul(i, j):
        if j == 0:
            return F(1, 2) if i == 1 else F(1)
        return factorial(j) * mp[i] / rho_k ** j

    g_norm = [a_g * sum((comb(a, cc) * p1 ** (1 - cc) * lb[cc] * n_obj(a - cc)
                         for cc in range(a + 1)), F(0)) for a in range(order + 1)]
    f_norm = {i: [a_h * sum((comb(a, cc) * w ** (1 - cc) * lb[cc] * m_pul(i, a - cc)
                             for cc in range(a + 1)), F(0)) for a in range(order + 1)]
              for i in (1, 2)}
    terms = ibp_terms(order)
    kappa_c = (vmin - v_b) / 2
    k_obj = ibp_constant(terms, g_norm, e_obj, kappa_c)
    k_pul1 = ibp_constant(terms, f_norm[1], e_pul, kappa_c)
    a_inf = g_norm[0] / (2 * PI_LO)
    b_inf = f_norm[1][0] / (2 * PI_LO)
    c_sum = sqrt_hi(b_inf ** 2 * k_obj ** 2 + a_inf ** 2 * k_pul1 ** 2)
    c.update(dict(s5_lo=s5_lo, vmin=vmin, vmax=vmax, v_b=v_b, energy=energy, q_p=q_p,
                  m_pi=m_pi, r_eps=r_eps, s_min=s_min, terms=terms, e_pul=e_pul,
                  f_norm=f_norm, kappa_c=kappa_c, c_sum=c_sum, k_obj=k_obj,
                  k_pul1=k_pul1, order=order, z=z, a_g=a_g, a_h=a_h, n_terms=len(terms)))
    return c


def eta_bar(c: dict, t: int) -> F:
    order, kc = c["order"], c["kappa_c"]
    tt = F(t)
    head = sqrt_hi(1 / (kc * tt) + F(1, 2 * order - 1))
    kpow = sqrt_hi(kc) / kc ** order
    root_t = sqrt_hi(tt)
    tsum = root_t / tt ** order + root_t * tt * 2 / ((2 * order - 3) * tt ** order)
    return 2 / c["s5_lo"] * c["c_sum"] * head * kpow * tsum


def delta_bar(c: dict, t: int) -> F:
    order, z, vmin = c["order"], c["z"], c["vmin"]
    kd = vmin - F(z - 1, t)
    check(kd > 0, f"free-tail ratio kappa_delta > 0 at T={t}")
    kd1 = ibp_constant(c["terms"], c["f_norm"][1], c["e_pul"], kd)
    kd2 = ibp_constant(c["terms"], c["f_norm"][2], c["e_pul"], kd)
    d0 = t * vmin - z + 1
    check(d0 > 0, f"free-tail distance D0 > 0 at T={t}")
    s = d0 ** (-2 * order) + d0 ** (1 - 2 * order) / (2 * order - 1)
    return sqrt_hi((kd1 ** 2 + kd2 ** 2) * s)


def audit_success_and_certificate(constants: dict | None = None, t_ret: int = T_RET,
                                  eps_ret: F = EPS_RET, table: tuple = MODULUS_TABLE) -> int:
    start = CHECKS["n"]
    c = retention_constants() if constants is None else constants
    n5 = CHECKS["n"] - start
    print(f"PASS GROUP 5 SUCCESS_SECTOR: {n5} checks; v_min>={sci(c['vmin'], 6, False)}; "
          f"v_max<={sci(c['vmax'], 6)}; v_b<={sci(c['v_b'])}; "
          f"energy spread<={sci(c['energy'])}; q_P<={sci(c['q_p'])}")
    start6 = CHECKS["n"]
    check(c["n_terms"] > 0 and c["c_sum"] > 0, "nonvacuous certificate constants")
    bounds = {}
    for t in sorted(set(table) | {t_ret}):
        bounds[t] = (delta_bar(c, t), eta_bar(c, t))
    d_t, e_t = bounds[t_ret]
    eps = d_t + e_t
    achieved = eps <= eps_ret
    n6 = CHECKS["n"] - start6
    print(f"PASS GROUP 6 RETENTION_CERTIFICATE: {n6} checks; N={c['order']}; "
          f"L^N terms={c['n_terms']}; C_cook<={sci(c['c_sum'])}; kappa_c>={sci(c['kappa_c'], 4, False)}")
    for t in table:
        val = bounds[t][0] + bounds[t][1]
        print(f"MODULUS T={t}: sup_(n>=T) ||(I-R1)psi_n|| <= {sci(val)}")
    verdict = "ACHIEVED" if achieved else "NOT ACHIEVED"
    print(f"RETENTION TARGET T={t_ret} eps={eps_ret}: delta<={sci(d_t)} eta<={sci(e_t)} "
          f"eps_cert<={sci(eps)} {verdict}")
    return n5 + n6


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("Exact audit requires assertions enabled")
    sys.stdout.reconfigure(newline="\n")
    total = 0
    total += audit_label_algebra()
    total += audit_physical_conjugacy()
    total += audit_recrossing_and_no_parking()
    total += audit_symmetry_and_dark_record()
    total += audit_success_and_certificate()
    print("SCOPE: declared ideal product success family in Ran Q_full only; "
          "actual v105 normalized selected component NOT SHOWN in family; "
          "exact permanent retention NOT CLAIMED")
    print(f"VERIFY PASS C-HOMOGENEOUS-RECORD-RETENTION-N total_checks={total}")


if __name__ == "__main__":
    main()
