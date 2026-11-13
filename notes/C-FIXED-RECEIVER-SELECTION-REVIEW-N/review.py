#!/usr/bin/env python3
"""Independent review checker C-FIXED-RECEIVER-SELECTION-REVIEW-N.

Status: NON-CANONICAL / L1.  This file is a review instrument.  It is not
Canon text, and it changes no target file, registry row, status, Canon text
or release.

Implements: notes/C-FIXED-RECEIVER-SELECTION-REVIEW-N/PREREG.md, the frozen
checks R1 to R10 (section 6) and the exploratory outputs X1 and X2
(section 7), under the arithmetic conventions of section 4, the common
objects of section 5 and the output contract of section 8.

Source boundary (PREREG section 3).  The writer of this file read only:
  - PREREG.md of this review;
  - at target head 3d8d364cb981bb5d53bbede432fb5a4ac4181709, via git show:
    RECEIVER-CONTACT.md, RECEIVER-DYNAMICS.md, RECEIVER-OBSTRUCTION.md,
    STOCK-BOUND.md and REVIEW-RESPONSE.md of
    notes/C-LOADED-CURRENT-WORK-PHASE-COMPATIBILITY-N;
  - the section of canon/CANON.md that defines O, q and the total contact
    (RELATIVE-CONTACT-INTEGRAL-LAW and its preamble).
No target code, expected output, run record, result file, manifest, source
pin file, informal checker, scratch file, PR, issue or CI text was read.
Before the pin the file was only parsed for syntax; nothing in it was run.

Runtime contract.  Standard library only.  No floating point anywhere:
integers and fractions.Fraction only, zero tolerance.  No file reads, no
network, no subprocesses, no clock, no randomness, no dependence on the
working directory.  Stdout is exactly one JSON line followed by LF, printed
only after every check passed.  Any failed check raises AssertionError, so
the process exits nonzero and prints no PASS line.
"""

# Runtime and memory estimate (operation counts; CPython 3.8 or later):
#   ordinary contacts (each one O-product, about 5-10 us):
#     R1 ~0.2M, R3 ~0.09M, R5 ~0.35M, R6 ~0.1M, R7 ~0.12M, R8 ~0.04M,
#     R9 ~0.45M, X1 ~0.1M; total ~1.5M contacts, about 10-20 s.
#   Q evaluations (closed form plus trace form, about 10 us): ~0.6M, ~6 s.
#   R10: two 400x400 rank computations modulo a prime, at most ~32M modular
#     element updates each in list comprehensions, about 3-8 s each; 242
#     Bareiss determinants of 20x20 integer matrices (~2.7k steps each,
#     ~0.7M big-integer steps), about 1 s; ~1e4 products in Z[zeta_25] of
#     at most 400 coefficient products each, about 1-2 s.
#   Expected total: roughly 30-120 s, far below the 900 s limit.
#   Memory: the largest object is one 400x400 integer matrix (plus a working
#     copy); the census dictionaries hold a few thousand short tuples.
#     Peak well below 200 MiB, far below the 2 GiB limit.

import hashlib
import itertools
import json
import sys
from fractions import Fraction

STATUS = ("NON-CANONICAL / L1; independent review checker "
          "C-FIXED-RECEIVER-SELECTION-REVIEW-N")

CHECKS = 0


def check(cond, message):
    """Count one executed check; raise AssertionError(message) if cond fails."""
    global CHECKS
    CHECKS += 1
    if not cond:
        raise AssertionError(message)


# ---------------------------------------------------------------------------
# PREREG section 4, Ring: O = Z[j] in the basis (1, j, j^2, j^3) with
# j^4 = -1 - j - j^2 - j^3.  Multiplication is cyclic five-coefficient
# convolution modulo j^5 = 1, then reduction.
# ---------------------------------------------------------------------------

ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)


def ext5(a):
    """Four basis coefficients -> five cyclic coefficients (j^4 entry 0)."""
    return (a[0], a[1], a[2], a[3], 0)


def red5(w):
    """Reduce sum_r w_r j^r (r = 0..4) to the basis, j^4 = -1-j-j^2-j^3."""
    w4 = w[4]
    return (w[0] - w4, w[1] - w4, w[2] - w4, w[3] - w4)


def cyc5(u, v):
    """Cyclic five-coefficient convolution modulo j^5 = 1, unreduced."""
    w = [0, 0, 0, 0, 0]
    for i in range(5):
        ui = u[i]
        if ui:
            for k in range(5):
                vk = v[k]
                if vk:
                    w[(i + k) % 5] += ui * vk
    return w


def mul(a, b):
    return red5(cyc5(ext5(a), ext5(b)))


def add(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2], a[3] + b[3])


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2], a[3] - b[3])


def neg(a):
    return (-a[0], -a[1], -a[2], -a[3])


def smul(n, a):
    return (n * a[0], n * a[1], n * a[2], n * a[3])


def jpow(s):
    """j^s for any integer s."""
    w = [0, 0, 0, 0, 0]
    w[s % 5] = 1
    return red5(w)


def conj5(a):
    """Cyclic five-coefficient vector of abar (j^i -> j^-i), unreduced."""
    e = ext5(a)
    u = [0, 0, 0, 0, 0]
    for i in range(5):
        u[(-i) % 5] += e[i]
    return u


def conj(a):
    return red5(conj5(a))


def galois(a, k):
    """The Galois map j -> j^k applied to a."""
    e = ext5(a)
    u = [0, 0, 0, 0, 0]
    for i in range(5):
        u[(k * i) % 5] += e[i]
    return red5(u)


# ---------------------------------------------------------------------------
# PREREG section 4, Account: Q by the closed form and by Tr(a abar)/2 with
# Tr(j^r) = 4 if 5 | r and -1 otherwise.  Every Q the checker uses goes
# through Q(), which computes both and checks that they agree.
# ---------------------------------------------------------------------------

TR_J = (4, -1, -1, -1, -1)


def q_closed(a):
    c0, c1, c2, c3 = a
    num = 5 * (c0 * c0 + c1 * c1 + c2 * c2 + c3 * c3) - (c0 + c1 + c2 + c3) ** 2
    check(num % 2 == 0, "Q closed form: odd numerator")
    return num // 2


def q_trace(a):
    w = cyc5(ext5(a), conj5(a))
    tr = TR_J[0] * w[0] + TR_J[1] * w[1] + TR_J[2] * w[2] + TR_J[3] * w[3] + TR_J[4] * w[4]
    check(tr % 2 == 0, "Q trace form: odd trace")
    return tr // 2


def Q(a):
    qc = q_closed(a)
    qt = q_trace(a)
    check(qc == qt, "Q: closed form differs from Tr(a abar)/2")
    return qc


# ---------------------------------------------------------------------------
# PREREG section 4, Contact: admitted exactly when all four coefficients of
# x-y are even; then s=(x+y)/2, t=(x-y)/2 and C(x,y)=(s+rho t, s-rho t)
# with rho=j^2.  Otherwise the pair is fixed.
# ---------------------------------------------------------------------------

RHO = jpow(2)
RHO_INV = jpow(3)


def admitted(x, y):
    """Admission predicate, written separately from contact()."""
    return all((xi - yi) % 2 == 0 for xi, yi in zip(x, y))


def contact(x, y):
    d0 = x[0] - y[0]
    d1 = x[1] - y[1]
    d2 = x[2] - y[2]
    d3 = x[3] - y[3]
    if (d0 | d1 | d2 | d3) & 1:
        return x, y
    s = ((x[0] + y[0]) // 2, (x[1] + y[1]) // 2,
         (x[2] + y[2]) // 2, (x[3] + y[3]) // 2)
    t = (d0 // 2, d1 // 2, d2 // 2, d3 // 2)
    rt = mul(RHO, t)
    return add(s, rt), sub(s, rt)


def contact_inverse_formula(x, y):
    """The inverse law: rho replaced by rho^-1 = j^3 (used only in R1)."""
    d0 = x[0] - y[0]
    d1 = x[1] - y[1]
    d2 = x[2] - y[2]
    d3 = x[3] - y[3]
    if (d0 | d1 | d2 | d3) & 1:
        return x, y
    s = ((x[0] + y[0]) // 2, (x[1] + y[1]) // 2,
         (x[2] + y[2]) // 2, (x[3] + y[3]) // 2)
    t = (d0 // 2, d1 // 2, d2 // 2, d3 // 2)
    rt = mul(RHO_INV, t)
    return add(s, rt), sub(s, rt)


def contact_pow(x, y, k):
    for _ in range(k):
        x, y = contact(x, y)
    return x, y


# ---------------------------------------------------------------------------
# PREREG section 4, Units: U10 = {+j^s, -j^s : s = 0..4}.
# ---------------------------------------------------------------------------

U10 = tuple([jpow(s) for s in range(5)] + [neg(jpow(s)) for s in range(5)])

# ---------------------------------------------------------------------------
# PREREG section 5, Stocks and alphabet.
# ---------------------------------------------------------------------------

A_R = (1, 2, 1, 0)            # a, with R = 1 + 2a
STOCK_R = (3, 4, 2, 0)        # R = 3 + 4j + 2j^2
STOCK_T = (1, 2, 0, -2)       # T = 1 + 2j - 2j^3
STOCK_S = (2, -2, 1, 0)       # S = 2 - 2j + j^2
J_EL = add(ONE, jpow(2))      # J = 1 + j^2
PHI = add(add(ONE, jpow(1)), jpow(4))   # phi = 1 + j + j^4

# R3 alphabet, in the order listed in PREREG R3.
ALPHABET = (ZERO, ONE, jpow(1), jpow(2), jpow(3), jpow(4), neg(ONE),
            J_EL, A_R, STOCK_R, STOCK_T, PHI)


def account(slots):
    total = 0
    for x in slots:
        total += Q(x)
    return total


def slot_sum(slots):
    total = ZERO
    for x in slots:
        total = add(total, x)
    return total


# ---------------------------------------------------------------------------
# Exact integer determinant by fraction-free (Bareiss) elimination.
# ---------------------------------------------------------------------------

def bareiss_det(mat):
    m = [list(row) for row in mat]
    n = len(m)
    sign = 1
    prev = 1
    exact = True
    for k in range(n - 1):
        if m[k][k] == 0:
            piv = -1
            for r in range(k + 1, n):
                if m[r][k] != 0:
                    piv = r
                    break
            if piv < 0:
                check(exact, "Bareiss: inexact division")
                return 0
            m[k], m[piv] = m[piv], m[k]
            sign = -sign
        mk = m[k]
        pkk = mk[k]
        for i in range(k + 1, n):
            mi = m[i]
            mik = mi[k]
            for c in range(k + 1, n):
                qt, rm = divmod(mi[c] * pkk - mik * mk[c], prev)
                if rm:
                    exact = False
                mi[c] = qt
            mi[k] = 0
        prev = pkk
    check(exact, "Bareiss: inexact division")
    return sign * m[n - 1][n - 1]


def frac_matmul(A, B):
    n = len(A)
    inner = len(B)
    cols = len(B[0])
    out = []
    for r in range(n):
        row = []
        for c in range(cols):
            acc = Fraction(0)
            for t in range(inner):
                acc += A[r][t] * B[t][c]
            row.append(acc)
        out.append(row)
    return out


def int_matmul(A, B):
    n = len(A)
    inner = len(B)
    cols = len(B[0])
    out = []
    for r in range(n):
        Ar = A[r]
        row = []
        for c in range(cols):
            acc = 0
            for t in range(inner):
                a = Ar[t]
                if a:
                    acc += a * B[t][c]
            row.append(acc)
        out.append(row)
    return out


def mult_matrix(a):
    """Integer matrix of multiplication by a on O in the basis (1,j,j^2,j^3)."""
    cols = [mul(a, jpow(i)) for i in range(4)]
    return [[cols[c][r] for c in range(4)] for r in range(4)]


# ---------------------------------------------------------------------------
# PREREG section 5, Receiver: W = [C(p,X), C(p,q)]^5, stock contact first in
# each block.  Literal inverse: reversed W, every contact replaced by C^4
# (forty contact attempts).  Both act on a slot list by slot indices.
# ---------------------------------------------------------------------------

def receiver_slots(slots, pi, qi, xi, record=False):
    s = list(slots)
    decisions = []
    history = []
    for _block in range(5):
        for kind, ai, bi in (("stock", pi, xi), ("balanced", pi, qi)):
            x = s[ai]
            y = s[bi]
            adm = admitted(x, y)
            nx, ny = contact(x, y)
            if not adm:
                check(nx == x and ny == y,
                      "receiver: a refused contact moved its pair")
            s[ai] = nx
            s[bi] = ny
            decisions.append(adm)
            if record:
                history.append((kind, adm, tuple(s)))
    return s, decisions, history


def receiver_inverse_slots(slots, pi, qi, xi):
    s = list(slots)
    attempts = 0
    for _block in range(5):
        for ai, bi in ((pi, qi), (pi, xi)):
            for _rep in range(4):
                x = s[ai]
                y = s[bi]
                adm = admitted(x, y)
                nx, ny = contact(x, y)
                if not adm:
                    check(nx == x and ny == y,
                          "receiver inverse: a refused contact moved its pair")
                s[ai] = nx
                s[bi] = ny
                attempts += 1
    return s, attempts


def stock_readings(X):
    """PREREG section 5, Inputs: input b is (p,q)=(j^b,-j^b); reading Q(X_out)."""
    readings = []
    runs = []
    for b in range(5):
        start = [jpow(b), neg(jpow(b)), X]
        out, _dec, _hist = receiver_slots(start, 0, 1, 2)
        readings.append(Q(out[2]))
        runs.append((start, out))
    return readings, runs


def is_success(readings):
    return len(set(readings)) == 5


def pointer_slots(r):
    """Two-pair pointer: low pair (j^r0,-j^r0), high pair (j^r1,-j^r1)."""
    r0 = r % 5
    r1 = r // 5
    return [jpow(r0), neg(jpow(r0)), jpow(r1), neg(jpow(r1))]


# ---------------------------------------------------------------------------
# PREREG section 5, Clock layout and words.  Ten slots; pair k is slots
# (2k, 2k+1).  A pair swap (a,b) is the slot swaps (2a,2b), (2a+1,2b+1).
# ---------------------------------------------------------------------------

def pair_swap(a, b):
    return [("S", 2 * a, 2 * b), ("S", 2 * a + 1, 2 * b + 1)]


SWAPS_FWD = pair_swap(3, 4) + pair_swap(2, 3) + pair_swap(1, 2) + pair_swap(0, 1)
SWAPS_REV = pair_swap(0, 1) + pair_swap(1, 2) + pair_swap(2, 3) + pair_swap(3, 4)


def word_powers(m):
    """Forward contact powers: 3(m+1) mod 5 on pair 0, 3m mod 5 on pairs 1-4."""
    return [(3 * (m + 1)) % 5] + [(3 * m) % 5] * 4


def compressed_word(m):
    w = list(SWAPS_FWD)
    for pr, pw in enumerate(word_powers(m)):
        w += [("C", pr)] * pw
    return w


def padded_word(m):
    w = list(SWAPS_FWD)
    w += [("C", 0)] * 3
    k = (3 * m) % 5
    for pr in range(5):
        w += [("C", pr)] * k
    for _blk in range(4 - k):
        w += [("C", 4)] * 5
    return w


def inverse_word(m):
    w = []
    for pr, pw in enumerate(word_powers(m)):
        w += [("C", pr)] * ((5 - pw) % 5)
    w += SWAPS_REV
    return w


def run_word(slots, word):
    s = list(slots)
    attempts = 0
    swaps = 0
    for op in word:
        if op[0] == "S":
            i = op[1]
            k = op[2]
            s[i], s[k] = s[k], s[i]
            swaps += 1
        else:
            pr = op[1]
            s[2 * pr], s[2 * pr + 1] = contact(s[2 * pr], s[2 * pr + 1])
            attempts += 1
    return s, attempts, swaps


COMPRESSED = [compressed_word(m) for m in range(5)]
PADDED = [padded_word(m) for m in range(5)]
INVERSE = [inverse_word(m) for m in range(5)]


def amp_to_slots(z):
    """Neutral pairs (z_k, -z_k), p the first slot and q the second."""
    s = []
    for zk in z:
        s.append(zk)
        s.append(neg(zk))
    return s


def is_neutral(slots):
    return all(slots[2 * k + 1] == neg(slots[2 * k]) for k in range(5))


def v_amp(z, m):
    """Amplitude formula V_m(z) = (j^(m+1) z4, j^m z0, j^m z1, j^m z2, j^m z3)."""
    jm1 = jpow(m + 1)
    jm = jpow(m)
    return (mul(jm1, z[4]), mul(jm, z[0]), mul(jm, z[1]), mul(jm, z[2]),
            mul(jm, z[3]))


# PREREG section 5, Delta preparation: e0 puts (1,-1) on pair 0.
E0 = amp_to_slots((ONE, ZERO, ZERO, ZERO, ZERO))


def clock_ticks(slots, m, n):
    s = list(slots)
    for _ in range(n):
        s = run_word(s, COMPRESSED[m])[0]
    return s


def attach_pair(n):
    """PREREG section 5: after n ticks the receiver is attached at pair n mod 5.
    The single source of the attachment rule, used by experiment()."""
    return n % 5


def experiment(m, stock, n, start=None):
    """n ticks of V_m from start (default e0), then the receiver attached at
    pair n mod 5 (p its first slot, q its second) with the stock in slot 10."""
    clock = clock_ticks(E0 if start is None else start, m, n)
    pr = attach_pair(n)
    out, _dec, _hist = receiver_slots(clock + [stock], 2 * pr, 2 * pr + 1, 10)
    return clock, out


def vm_matrix_O(m):
    """5x5 matrix over O of the amplitude map V_m (columns V_m(e_k))."""
    cols = []
    for k in range(5):
        e = [ZERO] * 5
        e[k] = ONE
        cols.append(v_amp(tuple(e), m))
    return [[cols[c][r] for c in range(5)] for r in range(5)]


def o_matmul(A, B):
    n = len(A)
    out = []
    for r in range(n):
        row = []
        for c in range(n):
            acc = ZERO
            for t in range(n):
                acc = add(acc, mul(A[r][t], B[t][c]))
            row.append(acc)
        out.append(row)
    return out


def o_diag(entries):
    n = len(entries)
    return [[entries[r] if r == c else ZERO for c in range(n)] for r in range(n)]


# ---------------------------------------------------------------------------
# R1 Ring and contact law.
# ---------------------------------------------------------------------------

def r1():
    # R1: Q(closed form) = Tr(a abar)/2; Q > 0 and Q >= 2 on nonzero [-3,3]^4.
    box3 = list(itertools.product(range(-3, 4), repeat=4))
    check(len(box3) == 2401, "R1: size of [-3,3]^4")
    for c in box3:
        qc = q_closed(c)
        qt = q_trace(c)
        check(qc == qt, "R1: Q(closed form) != Tr(a abar)/2")
        if c != ZERO:
            check(qc > 0, "R1: Q not positive on a nonzero element of [-3,3]^4")
            check(qc >= 2, "R1: Q < 2 on a nonzero element of [-3,3]^4")

    # R1: the 6561 ordered pairs in [-1,1]^4.
    box1 = list(itertools.product(range(-1, 2), repeat=4))
    pairs = [(x, y) for x in box1 for y in box1]
    check(len(pairs) == 6561, "R1: number of ordered pairs in [-1,1]^4")
    n_adm_moving = 0
    for x, y in pairs:
        check(contact_pow(x, y, 5) == (x, y), "R1: C^5 is not the identity")
        check(contact_pow(x, y, 4) == contact_inverse_formula(x, y),
              "R1: C^4 differs from the rho^-1 inverse formula")
        nx, ny = contact(x, y)
        check(add(nx, ny) == add(x, y), "R1: contact changed the pair sum")
        check(Q(nx) + Q(ny) == Q(x) + Q(y), "R1: contact changed the pair Q")
        adm = admitted(x, y)
        if not adm:
            check(nx == x and ny == y, "R1: a refused pair moved")
        # Tie contact()'s internal parity branch to admitted() in both
        # directions.  A refused pair is fixed; on the admitted branch the
        # pair moves exactly when t = (x-y)/2 != 0, since rho != 1 and O is
        # a domain.  So "moved" holds exactly when admitted and x != y.
        check(((nx, ny) != (x, y)) == (adm and x != y),
              "R1: contact branch differs from the admission predicate")
        if adm and x != y:
            n_adm_moving += 1
    # [-1,1]^4 contains admitted pairs with x != y (e.g. x=1, y=-1), so the
    # tie above is exercised on the moving branch, not only on fixed pairs.
    check(n_adm_moving > 0, "R1: no admitted pair with x != y in [-1,1]^4")

    # R1: exactly 16 of the 256 pairs in {0,1}^4 x {0,1}^4 are admitted.
    b01 = list(itertools.product((0, 1), repeat=4))
    n01 = 0
    n_adm = 0
    for x in b01:
        for y in b01:
            n01 += 1
            if admitted(x, y):
                n_adm += 1
    check(n01 == 256 and n_adm == 16, "R1: admitted count on {0,1}^4 x {0,1}^4")

    # R1 Unit covariance: C(ux,uy) = u C(x,y) and Q(ux) = Q(x).
    check(len(set(U10)) == 10, "R1: U10 does not have ten distinct units")
    for u in U10:
        for x, y in pairs:
            ox, oy = contact(x, y)
            cx, cy = contact(mul(u, x), mul(u, y))
            check(cx == mul(u, ox) and cy == mul(u, oy),
                  "R1: unit covariance of the contact fails")
            check(Q(mul(u, x)) == Q(x) and Q(mul(u, y)) == Q(y),
                  "R1: Q not invariant under a unit of U10")

    # R1 Golden unit: phi = 1 + j + j^4, phi^2 = phi + 1, Q(phi) = 3.
    check(mul(PHI, PHI) == add(PHI, ONE), "R1: phi^2 != phi + 1")
    check(Q(PHI) == 3, "R1: Q(phi) != 3")

    # R1 Norm identity on every nonzero a in [-2,2]^4.
    nonzero2 = [a for a in itertools.product(range(-2, 3), repeat=4) if a != ZERO]
    check(len(nonzero2) == 624, "R1: number of nonzero elements of [-2,2]^4")
    for a in nonzero2:
        w = cyc5(ext5(a), conj5(a))     # a abar as a cyclic vector
        check(w[1] == w[4] and w[2] == w[3], "R1: a abar is not real")
        cf0 = w[0]                      # x0: coefficient of 1
        cf1 = w[1]                      # x1: coefficient of j + j^4
        cf2 = w[2]                      # x2: coefficient of j^2 + j^3
        A = cf0 - cf1
        B = cf1 - cf2
        check(red5(w) == add(smul(A, ONE), smul(B, PHI)),
              "R1: a abar != A + B phi")
        qa = Q(a)
        check(qa == 2 * A + B, "R1: Q(a) != 2A + B")
        N = bareiss_det(mult_matrix(a))
        check(qa * qa - 5 * B * B == 4 * N, "R1: Q(a)^2 - 5B^2 != 4N(a)")
        check(N >= 1, "R1: N(a) < 1")

    # R1 Completeness bound (B1).
    G = [[Fraction(5 * int(r == c) - 1, 2) for c in range(4)] for r in range(4)]
    G_inv = [[Fraction(2 * (int(r == c) + 1), 5) for c in range(4)] for r in range(4)]
    I4 = [[Fraction(int(r == c)) for c in range(4)] for r in range(4)]
    check(frac_matmul(G, G_inv) == I4 and frac_matmul(G_inv, G) == I4,
          "R1: G and G^-1 do not multiply to I")
    box5 = list(itertools.product(range(-5, 6), repeat=4))
    check(len(box5) == 14641, "R1: size of [-5,5]^4")
    for c in box5:
        qc = Q(c)
        for ci in c:
            check(5 * ci * ci <= 4 * qc, "R1: 5 c_i^2 > 4 Q(c)")
    check(Q((5, 2, 2, 2)) == 32, "R1: Q(5,2,2,2) != 32")
    n_outer = 0
    for c in itertools.product(range(-8, 9), repeat=4):
        if max(abs(ci) for ci in c) >= 6:
            n_outer += 1
            check(Q(c) > 44, "R1: some c in [-8,8]^4 with |c_i|>=6 has Q<=44")
    check(n_outer == 17 ** 4 - 11 ** 4, "R1: outer shell of [-8,8]^4 miscounted")


# ---------------------------------------------------------------------------
# R2 Receiver with R.
# ---------------------------------------------------------------------------

R2_READINGS = [32, 17, 2, 7, 27]
R2_TERMINAL = {1: (1, 1, 1, 1), 2: (3, 2, 0, -1), 3: (2, 3, 3, 1),
               4: (1, 0, -1, -1), 5: (3, 4, 2, 0)}
R2_TERMINAL_Q = {1: 2, 2: 27, 3: 17, 4: 7, 5: 32}
R2_WORK = [0, 15, 30, 25, 5]


def r2():
    a = A_R
    one_a = add(ONE, a)
    check(STOCK_R == add(ONE, smul(2, a)), "R2: R != 1 + 2a")
    check(Q(STOCK_R) == 32, "R2: Q(R) != 32")
    check(Q(a) == 7, "R2: Q(a) != 7")
    check(Q(one_a) == 10, "R2: Q(1+a) != 10")
    prod = cyc5(ext5(one_a), conj5(a))
    check(prod == [7, 4, 1, 2, 6], "R2: (1+a) abar coefficients")
    check(sum(prod) == 20, "R2: (1+a) abar coefficient sum")

    # R2: R_n = 1 + a + rho^n a, p_n = 1 + a - rho^n a, and the terminal table.
    r_n = {}
    p_n = {}
    rho_n = ONE
    for n in range(1, 6):
        rho_n = mul(rho_n, RHO)
        ra = mul(rho_n, a)
        r_n[n] = add(one_a, ra)
        p_n[n] = sub(one_a, ra)
        check(r_n[n] == R2_TERMINAL[n], "R2: terminal stock state R_n")
        check(Q(r_n[n]) == R2_TERMINAL_Q[n], "R2: Q(R_n)")

    readings = []
    for b in range(5):
        k = (2 * b) % 5
        start = [jpow(b), neg(jpow(b)), STOCK_R]
        out, dec, hist = receiver_slots(start, 0, 1, 2, record=True)
        # R2: the ten admission decisions.
        expected = []
        for i in range(5):
            if i < k:
                expected += [False, True]
            else:
                n = i - k + 1
                expected += [True, n == 5]
        check(dec == expected, "R2: admission decisions differ from the rule")
        # R2: after n admitted stock contacts, p = p_n and stock = R_n.
        n = 0
        for kind, adm, st in hist:
            if kind == "stock" and adm:
                n += 1
                check(st[0] == p_n[n] and st[2] == r_n[n],
                      "R2: state after n admitted stock contacts")
        check(n == 5 - k, "R2: number of admitted stock contacts")
        check(out[2] == r_n[5 - k], "R2: terminal stock is not R_(5-k)")
        reading = Q(out[2])
        readings.append(reading)
        # R2: work released by the stock.
        check(Q(STOCK_R) - reading == R2_WORK[b], "R2: work released by stock")
        # R2: account 36, slot sum conserved.
        check(account(start) == 36 and account(out) == 36, "R2: account != 36")
        check(slot_sum(out) == slot_sum(start), "R2: slot sum not conserved")
        # R2: untouched companion -R: account 68, total sum zero.
        comp_in = start + [neg(STOCK_R)]
        comp_out = out + [neg(STOCK_R)]
        check(account(comp_in) == 68 and account(comp_out) == 68,
              "R2: account with -R != 68")
        check(slot_sum(comp_in) == ZERO and slot_sum(comp_out) == ZERO,
              "R2: total sum with -R not zero")
        # R2: the forty-contact inverse restores the complete state.
        back, attempts = receiver_inverse_slots(out, 0, 1, 2)
        check(attempts == 40, "R2: inverse is not forty contacts")
        check(back == start, "R2: inverse does not restore the state")
    check(readings == R2_READINGS, "R2: readings for b=0..4")
    return readings


# ---------------------------------------------------------------------------
# R3 Raw triples.
# ---------------------------------------------------------------------------

def r3():
    check(len(ALPHABET) == 12 and len(set(ALPHABET)) == 12,
          "R3: alphabet does not have twelve distinct elements")
    n_triples = 0
    for p in ALPHABET:
        for q in ALPHABET:
            for X in ALPHABET:
                n_triples += 1
                start = [p, q, X]
                out, _dec, _hist = receiver_slots(start, 0, 1, 2)
                check(account(out) == account(start), "R3: total Q not conserved")
                check(slot_sum(out) == slot_sum(start), "R3: total sum not conserved")
                back, attempts = receiver_inverse_slots(out, 0, 1, 2)
                check(attempts == 40 and back == start,
                      "R3: literal inverse does not restore the triple")
    check(n_triples == 1728, "R3: number of triples")
    start = [ONE, jpow(1), ZERO]
    out, dec, _hist = receiver_slots(start, 0, 1, 2)
    check(dec == [False] * 10, "R3: (1,j,0) is not all-refused")
    check(out == start, "R3: all-refused input (1,j,0) moved")


# ---------------------------------------------------------------------------
# R4 Labels, re-encodings and semantic controls.
# ---------------------------------------------------------------------------

def r4():
    # R4 Two-pair pointer, all 25 labels r = r0 + 5 r1.
    n_labels = 0
    for hi in range(5):
        for lo in range(5):
            r = lo + 5 * hi                 # r = r0 + 5 r1 with r0=lo, r1=hi
            n_labels += 1
            base = pointer_slots(r)
            start = base + [STOCK_R]
            out, _dec, _hist = receiver_slots(start, 2, 3, 4)
            check(Q(out[4]) == R2_READINGS[hi],
                  "R4: pointer reading differs from the R2 reading at b=r1")
            check(out[0] == start[0] and out[1] == start[1],
                  "R4: low pair changed")
            check(account(start) == 40 and account(out) == 40,
                  "R4: pointer account with R != 40")
            check(account(start + [neg(STOCK_R)]) == 72
                  and account(out + [neg(STOCK_R)]) == 72,
                  "R4: pointer account with R and -R != 72")
            start_t = base + [STOCK_T]
            out_t, _dec, _hist = receiver_slots(start_t, 2, 3, 4)
            check(account(start_t) == 30 and account(out_t) == 30,
                  "R4: pointer account with T != 30")
            check(account(start_t + [neg(STOCK_T)]) == 52
                  and account(out_t + [neg(STOCK_T)]) == 52,
                  "R4: pointer account with T and -T != 52")
    check(n_labels == 25, "R4: number of labels")

    # R4 Re-encodings (1+5t) r mod 25 for all 125 pairs (r, t).
    n_pairs = 0
    for r in range(25):
        digits = []
        for t in range(5):
            n_pairs += 1
            rt = ((1 + 5 * t) * r) % 25
            check(rt % 5 == r % 5, "R4: re-encoding changed r mod 5")
            digits.append(rt // 5)
        n_distinct = len(set(digits))
        check((n_distinct == 5) == (r % 5 != 0),
              "R4: high digits distinct exactly when r mod 5 != 0 fails")
        if r % 5 == 0:
            check(n_distinct == 1, "R4: high digits not all equal for r mod 5 = 0")
    check(n_pairs == 125, "R4: number of (r,t) pairs")

    # R4 Witness r = 13.
    labels13 = [((1 + 5 * t) * 13) % 25 for t in range(5)]
    check(labels13 == [13, 3, 18, 8, 23], "R4: witness labels")
    digits13 = [lab // 5 for lab in labels13]
    check(digits13 == [2, 0, 3, 1, 4], "R4: witness high digits")
    readings13 = []
    work13 = []
    starts13 = []                           # actual re-encoded preparations
    outs13 = []                             # their complete output states
    for lab in labels13:
        start = pointer_slots(lab) + [STOCK_R]
        out, _dec, _hist = receiver_slots(start, 2, 3, 4)
        starts13.append(start)
        outs13.append(out)
        readings13.append(Q(out[4]))
        work13.append(Q(out[4]) - Q(start[4]))
    check(readings13 == [2, 32, 7, 17, 27], "R4: witness readings")
    check(work13 == [-30, 0, -25, -15, -5], "R4: witness signed stock work")

    # R4 Semantic controls (S1): five names on the unchanged r = 13 state.
    # The "five identical complete output states" half is an identity
    # control by construction: a name enters neither a slot nor the word,
    # so equal input states give equal histories by determinism.  The
    # general statement (identical preparation, joint dynamics and
    # observation rules give identical receiver histories) is the induction
    # of RECEIVER-OBSTRUCTION.md section 1; it rests on the hand review
    # (PREREG section 11), not on this finite check.  The checks below make
    # the control a contrast: the five names leave the input state equal to
    # the witness preparation for label 13 and reproduce its complete
    # output, while the five actual re-encodings are five distinct
    # preparations with five distinct complete output states.
    names = []
    starts = []
    outs = []
    for t in range(5):
        name = ((1 + 5 * t) * 13) % 25     # character exponent; not a slot
        names.append(name)
        start = pointer_slots(13) + [STOCK_R]   # the state ignores the name
        out, _dec, _hist = receiver_slots(start, 2, 3, 4)
        starts.append(start)
        outs.append(out)
    check(len(set(names)) == 5, "R4: the five names are not distinct")
    check(names == labels13, "R4: names are not the re-encoded labels")
    check(all(s == starts13[0] for s in starts),
          "R4: a name assignment entered the input state")
    check(all(o == outs[0] for o in outs),
          "R4: name assignments changed the complete output state")
    check(outs[0] == outs13[0],
          "R4: semantic-control output differs from the witness run at r=13")
    check(Q(outs[0][4]) == 2, "R4: semantic-control reading != 2")
    check(len(set(tuple(s) for s in starts13)) == 5,
          "R4: actual re-encodings are not five distinct preparations")
    check(len(set(tuple(o) for o in outs13)) == 5,
          "R4: actual re-encodings do not give five distinct complete states")


# ---------------------------------------------------------------------------
# R5 Root clock.
# ---------------------------------------------------------------------------

DENSE_FIXTURES = [
    (ZERO, ZERO, ZERO, ZERO, ZERO),
    (ONE, ZERO, ZERO, ZERO, ZERO),
    (ZERO, ZERO, ZERO, ZERO, J_EL),
    (ONE, jpow(1), jpow(2), jpow(3), J_EL),
    (STOCK_R, A_R, neg(ONE), ZERO, PHI),
    tuple(smul(2, x) for x in (ONE, jpow(1), jpow(2), jpow(3), J_EL)),
    (ONE, ZERO, J_EL, ZERO, neg(jpow(1))),
    (ONE, ONE, ONE, ONE, ONE),
    (STOCK_T, STOCK_S, STOCK_R, A_R, ONE),
]


def neutral_fixtures():
    fx = []
    for site in range(5):
        for el in ALPHABET:
            z = [ZERO] * 5
            z[site] = el
            fx.append(tuple(z))
    fx += DENSE_FIXTURES
    return fx


def r5():
    fixtures = neutral_fixtures()
    check(len(fixtures) == 69, "R5: 5x12 single-site plus 9 dense fixtures")
    j1 = jpow(1)
    # R5 Neutral fixtures.
    for m in range(5):
        for z in fixtures:
            nonzero = any(x != ZERO for x in z)
            s0 = amp_to_slots(z)
            acc0 = account(s0)
            s1 = run_word(s0, COMPRESSED[m])[0]
            check(s1 == amp_to_slots(v_amp(z, m)),
                  "R5: compressed word differs from the V_m amplitude formula")
            check(is_neutral(s1), "R5: state left the neutral subcarrier")
            check(account(s1) == acc0, "R5: account not preserved")
            sp, attempts, swaps = run_word(s0, PADDED[m])
            check(sp == s1, "R5: padded and compressed endpoints differ")
            check(attempts == 23, "R5: padded word is not 23 contact attempts")
            check(swaps == 8, "R5: padded word is not eight slot swaps")
            check(run_word(s1, INVERSE[m])[0] == s0,
                  "R5: literal inverse does not restore the neutral fixture")
            cur = s0
            period = 0
            for n in range(1, 26):
                cur = run_word(cur, COMPRESSED[m])[0]
                if n == 5:
                    check(cur == amp_to_slots(tuple(mul(j1, x) for x in z)),
                          "R5: five ticks do not multiply every amplitude by j")
                if period == 0 and cur == s0:
                    period = n
            check(cur == s0, "R5: 25 ticks are not the identity")
            check(period == (25 if nonzero else 1), "R5: least period")

    # R5 Raw fixtures: slot i of state o is alphabet[(7o+3i+i*i) mod 12].
    raw = [[ALPHABET[(7 * o + 3 * i + i * i) % 12] for i in range(10)]
           for o in range(40)]
    check(len(raw) == 40, "R5: number of raw fixtures")
    for m in range(5):
        for s0 in raw:
            s1 = run_word(s0, COMPRESSED[m])[0]
            check(run_word(s0, PADDED[m])[0] == s1,
                  "R5: raw padded and compressed endpoints differ")
            check(run_word(s1, INVERSE[m])[0] == s0,
                  "R5: literal inverse does not restore the raw state")
            acc0 = account(s0)
            five = list(s0)
            for pr in range(5):
                five[2 * pr], five[2 * pr + 1] = contact_pow(
                    s0[2 * pr], s0[2 * pr + 1], 3)
            cur = s0
            for n in range(1, 26):
                cur = run_word(cur, COMPRESSED[m])[0]
                check(account(cur) == acc0, "R5: raw account changed at a tick")
                if n == 5:
                    check(cur == five, "R5: five ticks differ from C^3 on every pair")
            check(cur == s0, "R5: 25 raw ticks are not the identity")

    # R5 Minimum neutral account.  A neutral state has account
    # 2 sum_k Q(z_k) (RECEIVER-DYNAMICS.md eq. (R1), using Q(-z) = Q(z));
    # every nonzero amplitude has Q >= 2 (checked by R1 on [-3,3]^4; the
    # bound on all of O is the norm identity, hand review, PREREG section
    # 11); hence a nonzero neutral state has account >= 4, and e0 attains 4.
    # The finite checks below record each step on the 69 fixtures.
    check(account(E0) == 4, "R5: account of e0 != 4")
    for z in fixtures:
        check(account(amp_to_slots(z)) == 2 * sum(Q(x) for x in z),
              "R5: neutral account != 2 sum Q(z_k)")
        if any(x != ZERO for x in z):
            check(all(Q(x) >= 2 for x in z if x != ZERO),
                  "R5: a nonzero amplitude has Q < 2")
            check(account(amp_to_slots(z)) >= 4,
                  "R5: nonzero neutral fixture with account < 4")
    return fixtures


# ---------------------------------------------------------------------------
# R6 Clock experiments and relative phase.
# ---------------------------------------------------------------------------

R6_TABLES = {
    "Q32_ticks_1": [[32, 17, 2, 7, 27], [27, 32, 17, 2, 7], [7, 27, 32, 17, 2], [2, 7, 27, 32, 17], [17, 2, 7, 27, 32]],
    "Q32_ticks_13": [[2, 32, 7, 17, 27], [17, 27, 2, 32, 7], [32, 7, 17, 27, 2], [27, 2, 32, 7, 17], [7, 17, 27, 2, 32]],
    "Q22_T_ticks_1": [[22, 12, 2, 7, 17], [17, 22, 12, 2, 7], [7, 17, 22, 12, 2], [2, 7, 17, 22, 12], [12, 2, 7, 17, 22]],
    "Q22_T_ticks_13": [[2, 22, 7, 12, 17], [12, 17, 2, 22, 7], [22, 7, 12, 17, 2], [17, 2, 22, 7, 12], [7, 12, 17, 2, 22]],
    "Q22_S_ticks_1": [[12, 7, 22, 2, 17], [17, 12, 7, 22, 2], [2, 17, 12, 7, 22], [22, 2, 17, 12, 7], [7, 22, 2, 17, 12]],
    "Q22_S_ticks_13": [[22, 12, 2, 7, 17], [7, 17, 22, 12, 2], [12, 2, 7, 17, 22], [17, 22, 12, 2, 7], [2, 7, 17, 22, 12]],
}
R6_TABLE_SPECS = [
    ("Q32_ticks_1", "R", 1), ("Q32_ticks_13", "R", 13),
    ("Q22_T_ticks_1", "T", 1), ("Q22_T_ticks_13", "T", 13),
    ("Q22_S_ticks_1", "S", 1), ("Q22_S_ticks_13", "S", 13),
]
STOCKS = {"R": STOCK_R, "T": STOCK_T, "S": STOCK_S}
STOCK_Q = {"R": 32, "T": 22, "S": 22}


def r6():
    for name in ("R", "T", "S"):
        X = STOCKS[name]
        qx = STOCK_Q[name]
        check(Q(X) == qx, "R6: stock account")
        for m in range(5):
            # R6: one tick -> only pair 1, amplitude j^m;
            #     thirteen ticks -> only pair 3, amplitude j^(13m+2).
            for n, site, amp_exp in ((1, 1, m), (13, 3, 13 * m + 2)):
                # site is the frozen occupied pair of PREREG R6 (pair 1 after
                # one tick, pair 3 after thirteen) and stays literal; it is not
                # derived from n.  attach_pair() is the attachment rule that
                # experiment() actually uses (PREREG section 5).  The check
                # ties that code path to the frozen pair at which the clock
                # check below expects the only occupied pair.
                check(attach_pair(n) == site,
                      "R6: experiment() does not attach the receiver at the "
                      "frozen occupied pair")
                clock, out = experiment(m, X, n)
                expected = [ZERO] * 10
                expected[2 * site] = jpow(amp_exp)
                expected[2 * site + 1] = neg(jpow(amp_exp))
                check(clock == expected, "R6: clock state after n ticks from e0")
                # R6: complete account 4+Q(X), or 4+2Q(X) with -X, sum zero.
                check(account(clock + [X]) == 4 + qx and account(out) == 4 + qx,
                      "R6: complete account != 4+Q(X)")
                comp_in = clock + [X, neg(X)]
                comp_out = out + [neg(X)]
                check(account(comp_in) == 4 + 2 * qx
                      and account(comp_out) == 4 + 2 * qx,
                      "R6: complete account with -X != 4+2Q(X)")
                check(slot_sum(comp_in) == ZERO and slot_sum(comp_out) == ZERO,
                      "R6: total sum with -X not zero")
                # R6: receiver inverse, then clock inverse, restore e0 and X.
                back, attempts = receiver_inverse_slots(out, 2 * site, 2 * site + 1, 10)
                check(attempts == 40, "R6: receiver inverse is not forty contacts")
                rest = back[:10]
                for _ in range(n):
                    rest = run_word(rest, INVERSE[m])[0]
                check(rest == E0 and back[10] == X,
                      "R6: inverses do not restore e0 and X")

    # R6: the six tables, rows s = 0..4 (stock j^s X), columns m = 0..4.
    tables = {}
    for tname, xname, n in R6_TABLE_SPECS:
        X = STOCKS[xname]
        rows = []
        for s in range(5):
            xs = mul(jpow(s), X)
            row = []
            for m in range(5):
                _clock, out = experiment(m, xs, n)
                row.append(Q(out[10]))
            rows.append(row)
        check(rows == R6_TABLES[tname], "R6: table " + tname)
        tables[tname] = rows

    # R6 Relative identity: final(V_m, X) = u final(V_0, u^-1 X), u = j^(nm).
    for n in (1, 13):
        for m in range(5):
            for xname in ("R", "T", "S"):
                X = STOCKS[xname]
                u = jpow(n * m)
                u_inv = jpow(-n * m)
                check(mul(u, u_inv) == ONE, "R6: u u^-1 != 1")
                _c1, out_m = experiment(m, X, n)
                _c0, out_0 = experiment(0, mul(u_inv, X), n)
                check(out_m == [mul(u, x) for x in out_0],
                      "R6: relative identity of complete final states fails")
                check(Q(out_m[10]) == Q(out_0[10]),
                      "R6: q_n(m,X) != q_n(0, j^(-nm) X)")

    # R6 Simultaneous covariance: start (u e0, u X).
    for n in (1, 13):
        for m in range(5):
            for xname in ("R", "T", "S"):
                X = STOCKS[xname]
                _c, out_1 = experiment(m, X, n)
                for u in U10:
                    start = [mul(u, x) for x in E0]
                    _cu, out_u = experiment(m, mul(u, X), n, start=start)
                    check(out_u == [mul(u, x) for x in out_1],
                          "R6: simultaneous covariance of the final state fails")
                    check(Q(out_u[10]) == Q(out_1[10]),
                          "R6: simultaneous rotation changed the reading")

    # R6 Gauge conjugacy over O: D_m V_0 D_m^-1 = V_m.
    i5 = o_diag([ONE] * 5)
    v0 = vm_matrix_O(0)
    for m in range(5):
        d = o_diag([jpow(k * m) for k in range(5)])
        d_inv = o_diag([jpow(-k * m) for k in range(5)])
        check(o_matmul(d, d_inv) == i5, "R6: D_m D_m^-1 != I")
        vm = vm_matrix_O(m)
        check(o_matmul(o_matmul(d, v0), d_inv) == vm, "R6: D_m V_0 D_m^-1 != V_m")
        # R6 Holonomy: product of the five hopping coefficients is j.
        cycle = sorted(((k + 1) % 5, k) for k in range(5))
        support = sorted((r, c) for r in range(5) for c in range(5)
                         if vm[r][c] != ZERO)
        check(support == cycle, "R6: V_m support is not the five-cycle")
        hol = ONE
        for k in range(5):
            hol = mul(hol, vm[(k + 1) % 5][k])
        check(hol == jpow(1), "R6: holonomy of V_m != j")
    return tables


# ---------------------------------------------------------------------------
# R7 Stock census, Q <= 32, and the canonical digest (also used by R8).
# ---------------------------------------------------------------------------

R7_DIGEST = "a176b08e95b22febaf0e5edec05a6024a271cb08e26050ff6ad795134ecf142c"
R8_DIGEST = "c09ba2caeb2c494642a664140ac8d8574268e7af120b59de68467e9061448cad"


def canonical_records(successes, census):
    keyed = sorted((Q(c), c) for c in successes)
    return [{"Q": q, "stock": list(c), "readings": list(census[c])}
            for q, c in keyed]


def canonical_digest(records):
    payload = json.dumps(records, sort_keys=True, separators=(",", ":")) + "\n"
    return hashlib.sha256(payload.encode("ascii")).hexdigest()


def level_counts(stocks):
    counts = {}
    for c in stocks:
        q = Q(c)
        counts[q] = counts.get(q, 0) + 1
    return counts


def str_keyed(counts):
    return {str(k): counts[k] for k in sorted(counts)}


def r7():
    box5 = list(itertools.product(range(-5, 6), repeat=4))
    check(len(box5) == 14641, "R7: size of [-5,5]^4")
    candidates = [c for c in box5 if Q(c) <= 32]
    check(len(candidates) == 1811, "R7: number of stocks with Q <= 32")
    census = {}
    successes = []
    for c in candidates:
        readings, runs = stock_readings(c)
        census[c] = readings
        if is_success(readings):
            successes.append(c)
            # R7: every success's full inverse restores all five inputs.
            for start, out in runs:
                back, attempts = receiver_inverse_slots(out, 0, 1, 2)
                check(attempts == 40 and back == start,
                      "R7: inverse does not restore a success input")
    levels = level_counts(successes)
    check(levels == {22: 40, 28: 40, 32: 40}, "R7: successes by level")
    check(len(successes) == 120, "R7: total successes")
    check(all(Q(c) >= 22 for c in successes), "R7: a success below 22")
    success_set = set(successes)
    check(STOCK_R in success_set and STOCK_T in success_set
          and STOCK_S in success_set, "R7: R, T or S does not succeed")

    # R7: T and S readings, T work, j^3 S readings.
    check(STOCK_T == add(sub(ONE, smul(2, jpow(3))), smul(2, jpow(1))),
          "R7: T != 1 + 2j - 2j^3")
    check(STOCK_S == add(sub(smul(2, ONE), smul(2, jpow(1))), jpow(2)),
          "R7: S != 2 - 2j + j^2")
    check(census[STOCK_T] == [22, 12, 2, 7, 17], "R7: T readings")
    check([Q(STOCK_T) - x for x in census[STOCK_T]] == [0, 10, 20, 15, 5],
          "R7: T work")
    check(census[STOCK_S] == [12, 7, 22, 2, 17], "R7: S readings")
    j3s_readings, _runs = stock_readings(mul(jpow(3), STOCK_S))
    check(j3s_readings == [22, 2, 17, 12, 7], "R7: j^3 S readings")

    # R7 'For T' bullet as read by PREREG-AMENDMENT-1.md (coordinator edit
    # before the pin): the frozen text 'Q(1+2j-2j^3-1)=Q(j-j^3)=5' equates
    # Q(T-1)=20 with Q((T-1)/2)=5.  The intended object is a=(T-1)/2=j-j^3.
    # T - 1 = 2(j - j^3) with Q 20; Q(a) = 5; Q(1+a) = 7; (1+a) abar.
    a_t = sub(jpow(1), jpow(3))
    check(sub(STOCK_T, ONE) == smul(2, a_t), "R7: T - 1 != 2(j - j^3)")
    check(Q(sub(STOCK_T, ONE)) == 20, "R7: Q(T - 1) != 20")
    check(Q(a_t) == 5, "R7: Q((T-1)/2) = Q(j - j^3) != 5")
    check(Q(add(ONE, a_t)) == 7, "R7: Q(1 + j - j^3) != 7")
    check(cyc5(ext5(add(ONE, a_t)), conj5(a_t)) == [2, 0, -2, -1, 1],
          "R7: (1+a) abar coefficients for a = j - j^3")

    # R7 Accounts: high pair plus T or S: 26, or 48 with the companion.
    for X in (STOCK_T, STOCK_S):
        for b in range(5):
            start = [jpow(b), neg(jpow(b)), X]
            out, _dec, _hist = receiver_slots(start, 0, 1, 2)
            check(account(start) == 26 and account(out) == 26,
                  "R7: high pair plus stock account != 26")
            check(account(start + [neg(X)]) == 48
                  and account(out + [neg(X)]) == 48,
                  "R7: high pair plus stock and companion account != 48")
    # R7 Accounts: two-pair pointer plus T: 30, or 52 with the companion.
    for r in range(25):
        start = pointer_slots(r) + [STOCK_T]
        out, _dec, _hist = receiver_slots(start, 2, 3, 4)
        check(account(start) == 30 and account(out) == 30,
              "R7: pointer plus T account != 30")
        check(account(start + [neg(STOCK_T)]) == 52
              and account(out + [neg(STOCK_T)]) == 52,
              "R7: pointer plus T and companion account != 52")

    # R7 Minimum record and canonical digest.
    records = canonical_records(successes, census)
    check(records[0] == {"Q": 22, "stock": [-4, -2, -2, -3],
                         "readings": [17, 12, 7, 22, 2]},
          "R7: minimum record")
    digest = canonical_digest(records)
    check(digest == R7_DIGEST, "R7: canonical digest")
    return {
        "candidates": candidates,
        "census": census,
        "successes": successes,
        "levels": levels,
        "records": records,
        "digest": digest,
    }


# ---------------------------------------------------------------------------
# R8 Box census [-2,2]^4, no Q cutoff.
# ---------------------------------------------------------------------------

def r8():
    census = {}
    successes = []
    for c in itertools.product(range(-2, 3), repeat=4):
        readings, _runs = stock_readings(c)
        census[c] = readings
        if is_success(readings):
            successes.append(c)
    check(len(census) == 625, "R8: number of stocks in [-2,2]^4")
    check(len(successes) == 32, "R8: number of successes")
    levels = level_counts(successes)
    check(levels == {22: 16, 28: 8, 32: 8}, "R8: successes by level")
    records = canonical_records(successes, census)
    digest = canonical_digest(records)
    check(digest == R8_DIGEST, "R8: canonical digest")
    return {"stocks": len(census), "successes": successes, "levels": levels,
            "records": records, "digest": digest}


# ---------------------------------------------------------------------------
# R9 Rotation rule (B4).
# ---------------------------------------------------------------------------

def r9(candidates, census):
    check(len(candidates) == 1811, "R9: candidate list is not that of R7")
    for c in candidates:
        rotated = []
        rot_readings = []
        for s in range(5):
            xs = mul(jpow(s), c)
            readings, _runs = stock_readings(xs)
            for b in range(5):
                check(readings[b] == census[c][(b - s) % 5],
                      "R9: reading_{j^s X}(b) != reading_X(b-s)")
            rotated.append(xs)
            rot_readings.append(readings)
        if c != ZERO:
            check(len(set(rotated)) == 5, "R9: the five j^s X are not distinct")
            check(len(set(Q(x) for x in rotated)) == 1,
                  "R9: the five j^s X have unequal Q")
            flags = [is_success(rd) for rd in rot_readings]
            check(all(flags) or not any(flags),
                  "R9: the five j^s X neither all succeed nor all fail")


# ---------------------------------------------------------------------------
# R10 support: Z[zeta_25] = Z[X]/(Phi_25(X)), zeta = X, integer coefficients.
# Elements are 20-tuples of coefficients of 1, zeta, ..., zeta^19.
# ---------------------------------------------------------------------------

PHI25 = [1 if i % 5 == 0 else 0 for i in range(21)]   # X^20+X^15+X^10+X^5+1
PHI5 = [1, 1, 1, 1, 1]                                 # X^4+X^3+X^2+X+1
PHI25_NZ = [(i, PHI25[i]) for i in range(21) if PHI25[i]]
CZ_ZERO = tuple([0] * 20)
CZ_ONE = tuple([1] + [0] * 19)


def cz_reduce(poly):
    """Remainder of an integer polynomial on division by the monic Phi_25."""
    w = list(poly)
    if len(w) < 20:
        w += [0] * (20 - len(w))
    for d in range(len(w) - 1, 19, -1):
        c = w[d]
        if c:
            base = d - 20
            for i, ph in PHI25_NZ:
                w[base + i] -= c * ph
    return tuple(w[:20])


def cz_mul(a, b):
    w = [0] * 39
    for i in range(20):
        ai = a[i]
        if ai:
            for k in range(20):
                bk = b[k]
                if bk:
                    w[i + k] += ai * bk
    return cz_reduce(w)


def cz_add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def cz_sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def cz_scal(n, a):
    return tuple(n * x for x in a)


def cz_const(n):
    return tuple([n] + [0] * 19)


def cz_sum(items):
    acc = CZ_ZERO
    for x in items:
        acc = cz_add(acc, x)
    return acc


def cz_zeta(e):
    w = [0] * 25
    w[e % 25] = 1
    return cz_reduce(w)


def cz_pow(a, k):
    acc = CZ_ONE
    for _ in range(k):
        acc = cz_mul(acc, a)
    return acc


def cz_conj(a):
    """Complex conjugation of the principal embedding: zeta -> zeta^24."""
    w = [0] * 25
    for i in range(20):
        if a[i]:
            w[(24 * i) % 25] += a[i]
    return cz_reduce(w)


def emb(o):
    """O -> Z[zeta_25], j -> zeta^5."""
    w = [0] * 20
    w[0] = o[0]
    w[5] = o[1]
    w[10] = o[2]
    w[15] = o[3]
    return tuple(w)


def cz_matmul(A, B):
    n = len(A)
    return [[cz_sum(cz_mul(A[r][t], B[t][c]) for t in range(n))
             for c in range(n)] for r in range(n)]


def cz_matvec(A, v):
    n = len(A)
    return [cz_sum(cz_mul(A[r][t], v[t]) for t in range(n)) for r in range(n)]


def cz_conj_transpose(A):
    n = len(A)
    return [[cz_conj(A[c][r]) for c in range(n)] for r in range(n)]


def cz_diag(entries):
    n = len(entries)
    return [[entries[r] if r == c else CZ_ZERO for c in range(n)]
            for r in range(n)]


def poly_shift_one(p):
    """Coefficients (low to high) of p(X+1), by Horner's rule."""
    res = [0]
    for c in reversed(p):
        new = [0] * (len(res) + 1)
        for i, r in enumerate(res):
            new[i] += r
            new[i + 1] += r
        new[0] += c
        res = new
    while len(res) > 1 and res[-1] == 0:
        res.pop()
    return res


def eisenstein_at_5(p):
    deg = len(p) - 1
    return (p[deg] == 1 and all(p[i] % 5 == 0 for i in range(deg))
            and p[0] % 25 != 0)


def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def rank_mod_p(rows, p):
    m = [[x % p for x in row] for row in rows]
    nrows = len(m)
    ncols = len(m[0]) if nrows else 0
    rank = 0
    for col in range(ncols):
        piv = -1
        for r in range(rank, nrows):
            if m[r][col]:
                piv = r
                break
        if piv < 0:
            continue
        m[rank], m[piv] = m[piv], m[rank]
        inv = pow(m[rank][col], p - 2, p)
        prow = [(x * inv) % p for x in m[rank]]
        m[rank] = prow
        for r in range(rank + 1, nrows):
            row = m[r]
            f = row[col]
            if f:
                m[r] = [(x - f * y) % p for x, y in zip(row, prow)]
        rank += 1
        if rank == nrows:
            break
    return rank


def coord(k, i):
    """Q^20 coordinate: amplitude k, basis coefficient i of (1,j,j^2,j^3)."""
    return 4 * k + i


def op_matrix_20(op):
    """Integer 20x20 matrix of a Q-linear map on Q^20 = O^5 (x) Q."""
    M = [[0] * 20 for _ in range(20)]
    for k in range(5):
        for i in range(4):
            z = [ZERO] * 5
            e = [0, 0, 0, 0]
            e[i] = 1
            z[k] = tuple(e)
            out = op(tuple(z))
            col = coord(k, i)
            for k2 in range(5):
                for i2 in range(4):
                    M[coord(k2, i2)][col] = out[k2][i2]
    return M


def jv_op(i, k):
    """The map j^i V^k on O^5 (V = V_0)."""
    u = jpow(i)

    def op(z):
        for _ in range(k):
            z = v_amp(z, 0)
        return tuple(mul(u, x) for x in z)
    return op


def commutation_system(V):
    """Rows of the linear system XV - VX = 0 in the 400 unknowns X_ab."""
    n = len(V)
    rows = []
    for a in range(n):
        for c in range(n):
            row = [0] * (n * n)
            for b in range(n):
                vbc = V[b][c]
                if vbc:
                    row[a * n + b] += vbc
                vab = V[a][b]
                if vab:
                    row[b * n + c] -= vab
            rows.append(row)
    return rows


PRIME_1 = 1000003
PRIME_2 = 998244353


# ---------------------------------------------------------------------------
# R10 Linear algebra and spectra, exactly in Z[zeta_25].
# ---------------------------------------------------------------------------

def r10(fixtures):
    # R10 Eisenstein: Phi_25(X+1) and Phi_5(X+1) at 5.
    p25 = poly_shift_one(PHI25)
    p5 = poly_shift_one(PHI5)
    check(len(p25) - 1 == 20 and eisenstein_at_5(p25),
          "R10: Phi_25(X+1) is not Eisenstein at 5")
    check(len(p5) - 1 == 4 and eisenstein_at_5(p5),
          "R10: Phi_5(X+1) is not Eisenstein at 5")

    # R10 The root j = zeta^5: 1 + j + j^2 + j^3 + j^4 = 0.
    cz_j = cz_zeta(5)
    check(cz_sum(cz_pow(cz_j, k) for k in range(5)) == CZ_ZERO,
          "R10: 1 + j + ... + j^4 != 0 for j = zeta^5")

    # R10 The roots lambda_t = zeta^(1+5t): lambda_t^5 = j, pairwise distinct.
    lam = [cz_zeta(1 + 5 * t) for t in range(5)]
    lam_inv = [cz_zeta(-(1 + 5 * t)) for t in range(5)]
    for t in range(5):
        check(cz_mul(lam[t], lam_inv[t]) == CZ_ONE, "R10: lambda_t^-1")
        check(cz_pow(lam[t], 5) == cz_j, "R10: lambda_t^5 != j")
    check(len(set(lam)) == 5, "R10: the lambda_t are not pairwise distinct")

    # R10 Basis: the exponents 5i + k are exactly 0..19, each once.
    exps = sorted(5 * i + k for i in range(4) for k in range(5))
    check(exps == list(range(20)), "R10: exponents 5i+k are not 0..19 once each")

    # R10 Eigenvectors: V w_t = lambda_t w_t.
    v5 = [[emb(x) for x in row] for row in vm_matrix_O(0)]
    w = [[cz_pow(lam_inv[t], k) for k in range(5)] for t in range(5)]
    left = [[cz_pow(lam[t], k) for k in range(5)] for t in range(5)]
    for t in range(5):
        check(cz_matvec(v5, w[t]) == [cz_mul(lam[t], x) for x in w[t]],
              "R10: V w_t != lambda_t w_t")

    # R10 Left vectors: <l_t, w_t'> = 5 if t = t', else 0.
    for t in range(5):
        for t2 in range(5):
            pairing = cz_sum(cz_mul(left[t][k], w[t2][k]) for k in range(5))
            check(pairing == (cz_const(5) if t == t2 else CZ_ZERO),
                  "R10: left/right vector pairing")

    # R10 Projections and reconstruction on every neutral R5 fixture.
    for z in fixtures:
        zc = [emb(x) for x in z]
        nonzero = any(x != ZERO for x in z)
        c5 = [cz_sum(cz_mul(zc[k], left[t][k]) for k in range(5))
              for t in range(5)]                     # 5 c_t
        if nonzero:
            for t in range(5):
                check(c5[t] != CZ_ZERO, "R10: zero projection of a nonzero state")
        for k in range(5):
            rec = cz_sum(cz_mul(c5[t], w[t][k]) for t in range(5))
            check(rec == cz_scal(5, zc[k]), "R10: 5z != sum_t (5c_t) w_t")

    # R10 Commutant: the 20 maps j^i V^k, their rank, and the nullity of XV=VX.
    v20 = op_matrix_20(jv_op(0, 1))
    basis_mats = []
    for i in range(4):
        for k in range(5):
            M = op_matrix_20(jv_op(i, k))
            check(int_matmul(M, v20) == int_matmul(v20, M),
                  "R10: j^i V^k does not commute with V")
            basis_mats.append(M)
    check(len(basis_mats) == 20, "R10: number of maps j^i V^k")
    check(is_prime(PRIME_1) and is_prime(PRIME_2), "R10: modulus is not prime")
    flat = [[M[r][c] for r in range(20) for c in range(20)] for M in basis_mats]
    check(rank_mod_p(flat, PRIME_1) == 20,
          "R10: rank of the j^i V^k modulo 1000003 != 20")
    system = commutation_system(v20)
    check(len(system) == 400 and all(len(row) == 400 for row in system),
          "R10: commutation system is not 400x400")
    sparse = [[(ix, v) for ix, v in enumerate(row) if v] for row in system]
    for vec in flat:
        check(all(sum(v * vec[ix] for ix, v in row) == 0 for row in sparse),
              "R10: a map j^i V^k does not solve XV = VX")
    for p in (PRIME_1, PRIME_2):
        check(400 - rank_mod_p(system, p) == 20,
              "R10: nullity of XV = VX modulo p != 20")

    # R10 Invertible filters: det P(V) != 0 for all 242 nonzero P in {-1,0,1}^5.
    i20 = [[int(r == c) for c in range(20)] for r in range(20)]
    vpows = [i20]
    for _ in range(4):
        vpows.append(int_matmul(vpows[-1], v20))
    n_filters = 0
    for P in itertools.product((-1, 0, 1), repeat=5):
        if not any(P):
            continue
        n_filters += 1
        PM = [[sum(P[k] * vpows[k][r][c] for k in range(5)) for c in range(20)]
              for r in range(20)]
        check(bareiss_det(PM) != 0, "R10: a filter P(V) has determinant 0")
    check(n_filters == 242, "R10: number of nonzero filters")

    # R10 H_m = 2I - j^m V - j^-m V* = (I - j^m V)*(I - j^m V); eigenvalues;
    # gauge conjugacy H_m = D_m H_0 D_m^-1.
    i5 = cz_diag([CZ_ONE] * 5)
    v5_star = cz_conj_transpose(v5)
    H = []
    for m in range(5):
        jm = cz_zeta(5 * m)
        jm_inv = cz_zeta(-5 * m)
        A = [[cz_sub(i5[r][c], cz_mul(jm, v5[r][c])) for c in range(5)]
             for r in range(5)]
        lhs = cz_matmul(cz_conj_transpose(A), A)
        Hm = [[cz_sub(cz_sub(cz_scal(2, i5[r][c]), cz_mul(jm, v5[r][c])),
                      cz_mul(jm_inv, v5_star[r][c]))
               for c in range(5)] for r in range(5)]
        check(lhs == Hm, "R10: H_m != (I - j^m V)*(I - j^m V)")
        for t in range(5):
            e = (1 + 5 * (t + m)) % 25
            mu = cz_sub(cz_sub(cz_const(2), cz_zeta(e)), cz_zeta(-e))
            check(cz_matvec(Hm, w[t]) == [cz_mul(mu, x) for x in w[t]],
                  "R10: H_m w_t != mu w_t")
        H.append(Hm)
    for m in range(5):
        dmat = cz_diag([cz_zeta(5 * k * m) for k in range(5)])
        dmat_inv = cz_diag([cz_zeta(-5 * k * m) for k in range(5)])
        check(cz_matmul(dmat, dmat_inv) == i5, "R10: D_m D_m^-1 != I")
        check(cz_matmul(cz_matmul(dmat, H[0]), dmat_inv) == H[m],
              "R10: H_m != D_m H_0 D_m^-1")

    # R10 Ground mode by the exact integer comparison of d = min(e, 25-e).
    # Hand-review premise, not computed here: at the principal embedding
    # mu = 2 - zeta^e - zeta^-e = 4 sin^2(pi e/25) = 4 sin^2(pi d/25), and
    # 4 sin^2(pi d/25) increases strictly on d = 0..12 because pi d/25 < pi/2
    # there.  That real-analytic ordering is not a finite exact statement in
    # Z[zeta_25] and cannot be certified by ring arithmetic without floating
    # point.  It rests on the hand review (PREREG section 11,
    # MATHEMATICAL-REVIEW.md).  The code checks only the integer ordering
    # of d and the frozen bullets: the argmin vector, the m = 0 d values,
    # d != 0, and mu != 0 exactly in Z[zeta_25].
    argmin = []
    for m in range(5):
        ds = []
        for t in range(5):
            e = (1 + 5 * (t + m)) % 25
            d = min(e, 25 - e)
            ds.append(d)
            check(d != 0, "R10: d = 0")
            mu = cz_sub(cz_sub(cz_const(2), cz_zeta(e)), cz_zeta(-e))
            check(mu != CZ_ZERO, "R10: mu = 0")
        if m == 0:
            check(ds == [1, 6, 11, 9, 4], "R10: d values for m = 0")
        dmin = min(ds)
        check(ds.count(dmin) == 1, "R10: ground mode not unique")
        argmin.append(ds.index(dmin))
    check(argmin == [0, 4, 3, 2, 1], "R10: argmin t over m = 0..4")
    return argmin


# ---------------------------------------------------------------------------
# X1 Level counts up to Q <= 44 (exploratory; not a falsifier).
# ---------------------------------------------------------------------------

def x1(census):
    stock_counts = {}
    success_counts = {}
    for c in itertools.product(range(-5, 6), repeat=4):
        q = Q(c)
        if q <= 44:
            stock_counts[q] = stock_counts.get(q, 0) + 1
            if c in census:
                readings = census[c]
            else:
                readings = stock_readings(c)[0]
            if is_success(readings):
                success_counts[q] = success_counts.get(q, 0) + 1
    return {"stock_counts_by_level": str_keyed(stock_counts),
            "success_counts_by_level": str_keyed(success_counts)}


# ---------------------------------------------------------------------------
# X2 Symmetries of the 120 successes (exploratory; not a falsifier).
# ---------------------------------------------------------------------------

def x2(successes):
    sset = set(successes)
    orbits = set()
    for c in successes:
        orbits.add(tuple(sorted(set(mul(u, c) for u in U10))))
    return {
        "closed_under_negation": all(neg(c) in sset for c in successes),
        "closed_under_conjugation": all(conj(c) in sset for c in successes),
        "closed_under_galois_j2": all(galois(c, 2) in sset for c in successes),
        "closed_under_galois_j3": all(galois(c, 3) in sset for c in successes),
        "U10_orbit_count": len(orbits),
    }


# ---------------------------------------------------------------------------
# PREREG section 8: output.
# ---------------------------------------------------------------------------

def main():
    r1()
    r2_readings = r2()
    r3()
    r4()
    fixtures = r5()
    tables = r6()
    res7 = r7()
    res8 = r8()
    r9(res7["candidates"], res7["census"])
    argmin = r10(fixtures)
    x1_out = x1(res7["census"])
    x2_out = x2(res7["successes"])
    result = {
        "status": STATUS,
        "R2_readings": r2_readings,
        "R6_tables": tables,
        "R7_candidates": len(res7["candidates"]),
        "R7_level_counts": str_keyed(res7["levels"]),
        "R7_successes": len(res7["successes"]),
        "R7_digest": res7["digest"],
        "R7_min_record": res7["records"][0],
        "R8_stocks": res8["stocks"],
        "R8_level_counts": str_keyed(res8["levels"]),
        "R8_successes": len(res8["successes"]),
        "R8_digest": res8["digest"],
        "R8_min_record": res8["records"][0],
        "R10_argmin": argmin,
        "X1": x1_out,
        "X2": x2_out,
        "checks": CHECKS,
        "verdict": "PASS",
    }
    sys.stdout.write(json.dumps(result, sort_keys=True, separators=(",", ":")) + "\n")


if __name__ == "__main__":
    main()
