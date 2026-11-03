#!/usr/bin/env python3
"""Independent blind reviewer for P-RELATIVE-CONTACT-WORKBANK-REUSE-1.

Written from scratch from the equations and prose of PREREG.md/PROOF.md
in PR #1879 only.  No author code, data or output is read.
Conventions are frozen in the sibling PREREG.md (posudek), sections V1-V8.
Standard library only, exact integer arithmetic.
"""
import argparse
import hashlib
import sys
import time
from fractions import Fraction

# ---------------------------------------------------------------- ring O=Z[j]
# Element: tuple (a0,a1,a2,a3) in basis (1, j, j^2, j^3), 1+j+j^2+j^3+j^4=0.

ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
TWO = (2, 0, 0, 0)
RHO = (0, 0, 1, 0)          # rho = j^2


def zadd(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2], a[3] + b[3])


def zsub(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2], a[3] - b[3])


def zneg(a):
    return (-a[0], -a[1], -a[2], -a[3])


def zmul(a, b):
    # Polynomial product, degrees 4..6 reduced by
    # j^4=-1-j-j^2-j^3, j^5=1, j^6=j.
    p = [0] * 7
    for i in range(4):
        if a[i]:
            ai = a[i]
            for k in range(4):
                p[i + k] += ai * b[k]
    return (p[0] - p[4] + p[5],
            p[1] - p[4] + p[6],
            p[2] - p[4],
            p[3] - p[4])


def rho_mul(a):
    # Multiply by j^2 directly: j^5=1, j^4=-1-j-j^2-j^3.
    return (a[3] - a[2], -a[2], a[0] - a[2], a[1] - a[2])


def qform(z):
    s = z[0] + z[1] + z[2] + z[3]
    n = 5 * (z[0] * z[0] + z[1] * z[1] + z[2] * z[2] + z[3] * z[3]) - s * s
    assert n % 2 == 0
    return n // 2


def eps(z):
    return (z[0] + z[1] + z[2] + z[3]) % 5


RHO_POW = [ONE]
for _ in range(4):
    RHO_POW.append(rho_mul(RHO_POW[-1]))
U_E = [zsub(ONE, RHO_POW[e]) for e in range(5)]   # u_e = 1-rho^e
W_E = [zadd(ONE, RHO_POW[e]) for e in range(5)]   # w_e = 1+rho^e
U1 = U_E[1]                                       # u
W1 = W_E[1]                                       # w
B_EL = W_E[2]                                     # b = 1+rho^2


def contact4(a, b):
    """Total contact on 4-coefficient elements. Returns (a', b', admitted)."""
    d0 = a[0] - b[0]; d1 = a[1] - b[1]; d2 = a[2] - b[2]; d3 = a[3] - b[3]
    if (d0 | d1 | d2 | d3) & 1:
        return a, b, False
    s = ((a[0] + b[0]) // 2, (a[1] + b[1]) // 2,
         (a[2] + b[2]) // 2, (a[3] + b[3]) // 2)
    d = (d0 // 2, d1 // 2, d2 // 2, d3 // 2)
    rd = rho_mul(d)
    return zadd(s, rd), zsub(s, rd), True


# ------------------------------------------------- second (5-coefficient) path
def to5(z):
    return (z[0], z[1], z[2], z[3], 0)


def from5(c):
    return (c[0] - c[4], c[1] - c[4], c[2] - c[4], c[3] - c[4])


def mul5(a, b):
    out = [0] * 5
    for i in range(5):
        if a[i]:
            for k in range(5):
                out[(i + k) % 5] += a[i] * b[k]
    return tuple(out)


RHO5 = (0, 0, 1, 0, 0)


def contact5(a4, b4):
    """Contact computed in cyclic 5-coefficient representation."""
    A = list(to5(a4)); B = list(to5(b4))
    diffpar = [(A[i] - B[i]) & 1 for i in range(5)]
    if any(p != diffpar[0] for p in diffpar):
        return a4, b4, False
    if diffpar[0]:
        A = [x + 1 for x in A]          # add (1,1,1,1,1) = 0 in O
    s5 = tuple((A[i] + B[i]) // 2 for i in range(5))
    d5 = tuple((A[i] - B[i]) // 2 for i in range(5))
    rd5 = mul5(RHO5, d5)
    return (from5(tuple(s5[i] + rd5[i] for i in range(5))),
            from5(tuple(s5[i] - rd5[i] for i in range(5))), True)


# ------------------------------------------------------------ prepared family
Y_STATES = [(ZERO, TWO, ZERO)]
for _e in range(1, 5):
    Y_STATES.append((U_E[_e], W_E[_e], ZERO))
for _e in range(1, 5):
    Y_STATES.append((ZERO, W_E[_e], U_E[_e]))
X_STATES = []
for _r in range(5):
    _x = zmul(RHO_POW[_r], W1)
    X_STATES.append((_x, zneg(_x)))
CONTROLS = (ZERO, U1, ZERO, ZERO, W1, ZERO)
DELTA = (1, 8)


def bank_empty():
    out = []
    for _ in range(5):
        out.append(zneg(B_EL)); out.append(B_EL)
    return out


def bank_marked(p):
    out = bank_empty()
    rb = rho_mul(B_EL)
    out[2 * p] = zneg(rb); out[2 * p + 1] = rb
    return out


BANKS = [bank_marked(p) for p in range(5)]
BANK_EMPTY = bank_empty()


def input5(s, r):
    return list(Y_STATES[s]) + list(X_STATES[r])


def core_elems(s, r):
    return input5(s, r) + list(CONTROLS) + bank_empty() + bank_empty()


def after_w_core_elems(s, r):
    return (list(Y_STATES[(s + 10) % 9]) + list(X_STATES[r]) + list(CONTROLS)
            + bank_marked((-r) % 5) + bank_marked((-r - DELTA[s]) % 5))


def initial_elems(triple):
    st = core_elems(*triple[0])
    for _ in range(6):
        st += bank_empty()
    st += input5(*triple[1])
    st += input5(*triple[2])
    return st


def final_elems(triple):
    st = core_elems(*triple[2])
    for (s, r) in triple:
        st += bank_marked((-r) % 5)
        st += bank_marked((-r - DELTA[s]) % 5)
    st += input5(*triple[0])
    st += input5(*triple[1])
    return st


INPUTS = [(s, r) for s in (0, 1) for r in range(5)]
TRIPLES = [(INPUTS[i0], INPUTS[i1], INPUTS[i2])
           for i0 in range(10) for i1 in range(10) for i2 in range(10)]


def decode_archives(archive_elems):
    """Read ONLY 60 archive elements. Returns triple or None."""
    labels = []
    for bi in range(6):
        bank = archive_elems[10 * bi:10 * bi + 10]
        lab = None
        for p in range(5):
            if list(bank) == BANKS[p]:
                lab = p; break
        if lab is None:
            return None
        labels.append(lab)
    out = []
    for j in range(3):
        a, ap = labels[2 * j], labels[2 * j + 1]
        d = (a - ap) % 5
        if d == 1:
            s = 0
        elif d == 3:
            s = 1
        else:
            return None
        out.append((s, (-a) % 5))
    return tuple(out)


# ------------------------------------------------------------------ words
# Contact word: list of (i,k).  Mixed program: list of (kind,i,k), kind 0=C,1=S.

def rep(edge, n):
    return [edge] * n


def build_S():
    """Primary build of S from the block definitions (A-PROOF sec.5)."""
    O1 = [(1, 5)]; A0 = [(5, 9)]; O2 = [(9, 10)]; T = [(3, 4)]
    F = [(0, 1), (1, 2)]
    Finv = rep((1, 2), 4) + rep((0, 1), 4)

    def Ec(c):
        Bc = [(c, 9)]
        return A0 + Bc + rep((5, 9), 4) + rep((c, 9), 4)

    def Ec_inv(c):
        Bc = [(c, 9)]
        return Bc + A0 + rep((c, 9), 4) + rep((5, 9), 4)

    def Lp(q, p):
        a = q + 2 * p; b = a + 1
        return rep((3, a), 4) + rep((a, b), 4) + [(3, a)] + [(a, b)]

    def SCAN(q):
        out = []
        for p in range(5):
            out += [(3, 10)] + Lp(q, p) + rep((3, 10), 4) + T
        return out

    W_A = Ec(6) + O2 + SCAN(11) + rep((9, 10), 4) + Ec_inv(6)
    W_B = Ec(7) + O2 + SCAN(21) + rep((9, 10), 4) + Ec_inv(7)

    def D(c, d):
        return rep((9, c), 3) + rep((9, d), 3) + [(9, c), (9, d), (9, c)]

    def V(c, d):
        return A0 + D(c, d) + rep((5, 9), 4) + D(c, d)

    R = O1 + W_A + W_B + V(7, 8) + V(6, 7) + rep((1, 5), 4)
    S = R + Finv + R + F + F + T
    parts = dict(L=Lp(11, 0), SCAN=SCAN(11), E=Ec(6), WA=W_A, WB=W_B,
                 D=D(7, 8), V=V(7, 8), R=R, S=S)
    return S, parts


def build_S_second():
    """Second build of S: token-expansion encoding, written separately."""
    base = {}

    def C(i, k):
        return [(i, k)]

    def pw(word, n):
        out = []
        for _ in range(n):
            out.extend(word)
        return out

    base["O1"] = C(1, 5); base["A0"] = C(5, 9); base["O2"] = C(9, 10)
    base["T"] = C(3, 4); base["F"] = C(0, 1) + C(1, 2)
    base["Finv"] = pw(C(1, 2), 4) + pw(C(0, 1), 4)
    for c in (6, 7):
        base[f"E{c}"] = base["A0"] + C(c, 9) + pw(base["A0"], 4) + pw(C(c, 9), 4)
        base[f"E{c}i"] = C(c, 9) + base["A0"] + pw(C(c, 9), 4) + pw(base["A0"], 4)
    for q in (11, 21):
        scan = []
        for p in range(5):
            a = q + 2 * p
            lp = pw(C(3, a), 4) + pw(C(a, a + 1), 4) + C(3, a) + C(a, a + 1)
            scan += C(3, 10) + lp + pw(C(3, 10), 4) + base["T"]
        base[f"SCAN{q}"] = scan
    base["WA"] = base["E6"] + base["O2"] + base["SCAN11"] + pw(base["O2"], 4) + base["E6i"]
    base["WB"] = base["E7"] + base["O2"] + base["SCAN21"] + pw(base["O2"], 4) + base["E7i"]
    for (c, d) in ((7, 8), (6, 7)):
        dd = pw(C(9, c), 3) + pw(C(9, d), 3) + C(9, c) + C(9, d) + C(9, c)
        base[f"V{c}{d}"] = base["A0"] + dd + pw(base["A0"], 4) + dd
    R = base["O1"] + base["WA"] + base["WB"] + base["V78"] + base["V67"] + pw(base["O1"], 4)
    return R + base["Finv"] + R + base["F"] + base["F"] + base["T"]


W6_LOCAL = [(1, 4), (1, 4), (4, 5), (1, 4), (1, 4), (1, 4),
            (1, 6), (1, 6), (1, 6), (1, 6), (1, 4), (1, 6)]


def K_modules(a, t):
    mods = []
    for p in range(5):
        q = (p + 1) % 5
        places = (a + 2 * p, a + 2 * p + 1, a + 2 * q, a + 2 * q + 1,
                  t + 2 * p, t + 2 * p + 1)
        mods.append([(places[i - 1], places[k - 1]) for (i, k) in W6_LOCAL])
    return mods


def K_word(a, t):
    out = []
    for m in K_modules(a, t):
        out += m
    return out


def invert_contacts(word):
    out = []
    for e in reversed(word):
        out += [e] * 4
    return out


def contacts_to_ops(word):
    return [(0, i, k) for (i, k) in word]


def build_forward(W, W_inv):
    """Returns (ops, meta). meta: stage segments and archive K ranges."""
    ops = []
    meta = {"stages": [], "archive_K": [], "swaps": []}
    for h in range(3):
        seg_start = len(ops)
        ops += contacts_to_ops(W)
        for (src, tgt) in ((11, 31 + 20 * h), (21, 41 + 20 * h)):
            ks = len(ops)
            ops += contacts_to_ops(K_word(src, tgt))
            meta["archive_K"].append((tgt, ks, len(ops)))
        ops += contacts_to_ops(W_inv)
        meta["stages"].append((seg_start, len(ops)))
        if h < 2:
            ss = len(ops)
            for i in range(5):
                ops.append((1, i, 91 + 5 * h + i))
            meta["swaps"].append((ss, len(ops)))
    return ops, meta


def build_inverse(ops):
    out = []
    for (kind, i, k) in reversed(ops):
        if kind == 1:
            out.append((1, i, k))
        else:
            out += [(0, i, k)] * 4
    return out


# ------------------------------------------------- run-length encoding (exact)
def rle_encode(ops):
    codes = []
    run = None  # (i,k,count)
    for (kind, i, k) in ops:
        if kind == 1:
            if run is not None:
                codes.append((run[0] << 14) | (run[1] << 7) | run[2]); run = None
            codes.append((i << 14) | (k << 7) | 0)
        elif run is not None and run[0] == i and run[1] == k:
            run = (i, k, run[2] + 1)
        else:
            if run is not None:
                codes.append((run[0] << 14) | (run[1] << 7) | run[2])
            run = (i, k, 1)
    if run is not None:
        codes.append((run[0] << 14) | (run[1] << 7) | run[2])
    return codes


def rle_decode(codes):
    out = []
    for code in codes:
        i = code >> 14; k = (code >> 7) & 127; n = code & 127
        if n == 0:
            out.append((1, i, k))
        else:
            out += [(0, i, k)] * n
    return out


# ------------------------------------------------------------- fast ID engine
SHIFT = 20
MASK = (1 << SHIFT) - 1


class Engine:
    """State = list of element IDs. Cache key packs (run-length, ida, idb)."""

    def __init__(self):
        self.ids = {}
        self.elems = []
        self.qvals = []
        self.epsvals = []
        self.cache = {}

    def intern(self, z):
        i = self.ids.get(z)
        if i is None:
            i = len(self.elems)
            assert i <= MASK
            self.ids[z] = i
            self.elems.append(z)
            self.qvals.append(qform(z))
            self.epsvals.append(eps(z))
        return i

    def id_state(self, elems):
        return [self.intern(z) for z in elems]

    def elems_of(self, state):
        return [self.elems[i] for i in state]

    def build_entry(self, run, ida, idb):
        a = self.elems[ida]; b = self.elems[idb]
        for _ in range(run):
            a, b, _adm = contact4(a, b)
        return (self.intern(a) << SHIFT) | self.intern(b)

    def apply_rle(self, st, codes):
        cache = self.cache
        build = self.build_entry
        for code in codes:
            n = code & 127
            i = code >> 14
            k = (code >> 7) & 127
            if n == 0:
                st[i], st[k] = st[k], st[i]
            else:
                ida = st[i]; idb = st[k]
                key = (n << 40) | (ida << SHIFT) | idb
                packed = cache.get(key)
                if packed is None:
                    packed = build(n, ida, idb)
                    cache[key] = packed
                st[i] = packed >> SHIFT
                st[k] = packed & MASK


def apply_contacts_elems(state, contacts):
    """Literal element-level execution. Returns (new state, admission flags)."""
    st = list(state)
    flags = []
    for (i, k) in contacts:
        a, b, adm = contact4(st[i], st[k])
        st[i] = a; st[k] = b
        flags.append(adm)
    return st, flags


def apply_ops_elems(state, ops):
    st = list(state)
    for (kind, i, k) in ops:
        if kind == 1:
            st[i], st[k] = st[k], st[i]
        else:
            a, b, _ = contact4(st[i], st[k])
            st[i] = a; st[k] = b
    return st


# ------------------------------------------------------------ my serialisation
def ser_state_A(elems):
    return ";".join(",".join(str(x) for x in z) for z in elems).encode("ascii")


def ser_state_B(elems):
    return b";".join(("%d,%d,%d,%d" % z).encode("ascii") for z in elems)


def ser_ops_A(ops):
    return ";".join(("S" if kind else "C") + str(i) + "," + str(k)
                    for (kind, i, k) in ops).encode("ascii")


def ser_ops_B(ops):
    parts = []
    for (kind, i, k) in ops:
        parts.append((b"S%d,%d" if kind else b"C%d,%d") % (i, k))
    return b";".join(parts)


def sha(data):
    return hashlib.sha256(data).hexdigest()


# ------------------------------------------------------------------- checking
class Fail(Exception):
    def __init__(self, klabel, msg):
        super().__init__(msg)
        self.klabel = klabel
        self.msg = msg


def expect(cond, klabel, msg):
    if not cond:
        raise Fail(klabel, msg)


def mat_mul(A, B):
    return [[sum(A[i][t] * B[t][j] for t in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def check_K1_ring():
    expect(qform(U1) == 5 and qform(W1) == 3 and qform(B_EL) == 3,
           "K1", f"Q(u,w,b)=({qform(U1)},{qform(W1)},{qform(B_EL)}), want (5,3,3)")
    expect(B_EL == (0, -1, -1, -1), "K1", f"b={B_EL}, want (0,-1,-1,-1)")
    # Matrix of rho-multiplication (columns = images of basis vectors).
    cols = [rho_mul(e) for e in
            [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]]
    R = [[Fraction(cols[j][i]) for j in range(4)] for i in range(4)]
    A = [[Fraction(2) if i == j else Fraction(-1, 2) for j in range(4)]
         for i in range(4)]
    Rt = [[R[j][i] for j in range(4)] for i in range(4)]
    expect(mat_mul(mat_mul(Rt, A), R) == A, "K1", "R^T A R != A for Q-form")
    R5 = R
    for _ in range(4):
        R5 = mat_mul(R5, R)
    ident = [[Fraction(1) if i == j else Fraction(0) for j in range(4)]
             for i in range(4)]
    expect(R5 == ident, "K1", "R^5 != I")
    expect(rho_mul(RHO_POW[4]) == ONE, "K1", "rho^5 != 1 in elements")
    expect(all(zmul(RHO, z) == rho_mul(z) for z in
               [(a, b, c, d) for a in (-1, 0, 2) for b in (-1, 0, 2)
                for c in (-1, 0, 2) for d in (-1, 0, 2)]),
           "K1", "generic zmul by rho disagrees with rho_mul")
    box2 = [(a, b, c, d) for a in range(-2, 3) for b in range(-2, 3)
            for c in range(-2, 3) for d in range(-2, 3)]
    for z in box2:
        expect(qform(rho_mul(z)) == qform(z), "K1", f"Q(rho z)!=Q(z) at {z}")
        w = z
        for _ in range(5):
            w = rho_mul(w)
        expect(w == z, "K1", f"rho^5 z != z at {z}")
    box = [(a, b, c, d) for a in (-1, 0, 1, 2) for b in (-1, 0, 1, 2)
           for c in (-1, 0, 1, 2) for d in (-1, 0, 1, 2)]
    npairs = 0
    for a in box:
        for b in box:
            npairs += 1
            out4 = contact4(a, b)
            out5 = contact5(a, b)
            expect(out4 == out5, "K1",
                   f"4-coeff vs 5-coeff contact differ at {a} {b}: {out4} vs {out5}")
            x, y, adm = out4
            expect(qform(x) + qform(y) == qform(a) + qform(b), "K1",
                   f"Q not preserved at {a} {b}")
            expect(zadd(x, y) == zadd(a, b), "K1", f"sum not preserved at {a} {b}")
            expect(eps(x) == eps(a) and eps(y) == eps(b), "K1",
                   f"epsilon not preserved at {a} {b}")
            if not adm or a == b:
                expect((x, y) == (a, b), "K1", f"refused/diagonal not fixed at {a} {b}")
            # C^5 = id and C^4 = inverse, literally.
            x1, y1, _ = contact4(a, b)
            p2, q2 = x1, y1
            for _ in range(4):
                p2, q2, _ = contact4(p2, q2)
            expect((p2, q2) == (a, b), "K1", f"C^5 != id at {a} {b}")
            p3, q3 = a, b
            for _ in range(5):
                p3, q3, _ = contact4(p3, q3)
            expect((p3, q3) == (a, b), "K1", f"C^5 (direct) != id at {a} {b}")
    return npairs


def account_of(elems):
    return sum(qform(z) for z in elems)


def sigma_of(elems):
    s = [0, 0, 0, 0]
    for z in elems:
        for i in range(4):
            s[i] += z[i]
    return tuple(s)


def check_local():
    """Small literal audits. Returns detail dict."""
    d = {}
    # Preparation accounts, from definitions.
    d["acct_input"] = account_of(input5(0, 0))
    expect(all(account_of(input5(s, r)) == 14 for (s, r) in INPUTS),
           "K2", "some input account != 14")
    expect(account_of(list(CONTROLS)) == 8, "K2", "controls account != 8")
    expect(account_of(BANK_EMPTY) == 30, "K2", "empty bank account != 30")
    expect(all(account_of(bk) == 30 and sigma_of(bk) == ZERO for bk in BANKS),
           "K2", "marked bank account/sum wrong")
    expect(all(bk != BANK_EMPTY for bk in BANKS) and len({tuple(b) for b in BANKS}) == 5,
           "K2", "marked banks not 5 distinct non-empty")
    expect(all([eps(z) for z in bk] == [3, 2] * 5 for bk in BANKS + [BANK_EMPTY]),
           "K2", "bank residue vector != (3,2)^5")
    expect(account_of(core_elems(1, 3)) == 82 and sigma_of(core_elems(1, 3)) == (4, 0, 0, 0),
           "K2", "core account/sum != 82/4")
    # Source / clock cycles, literally.
    for a in range(9):
        out, _ = apply_contacts_elems(list(Y_STATES[a]), [(0, 1), (1, 2)])
        expect(tuple(out) == Y_STATES[(a + 1) % 9], "K4", f"F(Y_{a}) != Y_{a+1}")
    for r in range(5):
        out, _ = apply_contacts_elems(list(X_STATES[r]), [(0, 1)])
        expect(tuple(out) == X_STATES[(r + 1) % 5], "K4", f"T(X_{r}) != X_{r+1}")
    expect(len(set(Y_STATES)) == 9 and len(set(X_STATES)) == 5,
           "K4", "source/clock states not distinct")
    expect(all([eps(z) for z in y] == [0, 2, 0] for y in Y_STATES)
           and all([eps(z) for z in x] == [2, 3] for x in X_STATES)
           and [eps(z) for z in CONTROLS] == [0, 0, 0, 0, 2, 0],
           "K2", "source/clock/control residues differ from text")
    # Six-place copier cases (phases at places 1,4,5,6), literally.
    nb, b = zneg(B_EL), B_EL
    rb = rho_mul(B_EL); nrb = zneg(rb)
    r2b = zmul(RHO_POW[2], B_EL); nr2b = zneg(r2b)
    w6 = [(i - 1, k - 1) for (i, k) in W6_LOCAL]
    cases = [
        ([nb, b, nb, b, nb, b], [nb, b, nb, b, nb, b], "AARAAAAAAARA"),
        ([nrb, rb, nb, b, nb, b], [nrb, rb, nb, b, nrb, rb], "RRAAAARRRRAA"),
        ([nb, b, nrb, rb, nb, b], [nb, b, nrb, rb, nb, b], "RRRRRRAAAARA"),
    ]
    for ci, (init, want, admword) in enumerate(cases):
        out, flags = apply_contacts_elems(init, w6)
        got = "".join("A" if f else "R" for f in flags)
        expect(got == admword, "K8", f"W6 case {ci}: admission {got} != {admword}")
        expect(out == want, "K4", f"W6 case {ci}: endpoint mismatch")
    d["w6_admitted"] = [10, 6, 5]
    # Occupied-target boundary counterexample, phases (0,0,1,1)->(2,1,1,2).
    out, _ = apply_contacts_elems([nb, b, nb, b, nrb, rb], w6)
    expect(out == [nr2b, b, nb, rb, nrb, r2b], "K4",
           f"occupied-target W6 endpoint mismatch: {out}")
    # Full bank copier K on 20 slots, all marks, literally.
    kw = K_word(0, 10)
    kinv = invert_contacts(kw)
    expect(len(kw) == 60 and len(kinv) == 240, "K8", "K or K^-1 length wrong")
    noninv = 0
    for r in range(5):
        init = BANKS[r] + BANK_EMPTY
        st = list(init)
        adm_total = 0
        for m in range(5):
            st, flags = apply_contacts_elems(st, kw[12 * m:12 * m + 12])
            adm_total += sum(flags)
            expect(st[:10] == BANKS[r], "K5",
                   f"K source bank not restored at module {m}, mark {r}")
        expect(st == BANKS[r] + BANKS[r], "K4", f"K copy failed for mark {r}")
        expect(adm_total == 41, "K8", f"K admitted {adm_total} != 41 (mark {r})")
        back, _ = apply_contacts_elems(st, kinv)
        expect(back == init, "K6", f"K literal inverse failed (mark {r})")
        twice, _ = apply_contacts_elems(st, kw)
        if twice != init:
            noninv += 1
        # Rotated corollary: same word on rho^t-rotated pairs.
        for t in range(5):
            rot = [zmul(RHO_POW[t], z) for z in init]
            rout, _ = apply_contacts_elems(rot, kw)
            rwant = [zmul(RHO_POW[t], z) for z in (BANKS[r] + BANKS[r])]
            expect(rout == rwant, "K4", f"rotated K failed r={r} t={t}")
    expect(noninv >= 1, "K4", "K unexpectedly an involution on all marked cases")
    d["k_noninvolution_cases"] = noninv
    out, _ = apply_contacts_elems(BANK_EMPTY + BANK_EMPTY, kw)
    expect(out == BANK_EMPTY + BANK_EMPTY, "K4", "K on blank source changed banks")
    return d


def check_boundary(eng, st, eps0, where):
    e = sum(eng.qvals[i] for i in st)
    expect(e == 290, "K2", f"E={e} != 290 at {where}")
    expect(sigma_of(eng.elems_of(st)) == (8, 0, 0, 0), "K2",
           f"Sigma != (8,0,0,0) at {where}")
    expect([eng.epsvals[i] for i in st] == eps0, "K2",
           f"labelled residue vector changed at {where}")


def fresh_bank_count(st, empty_ids):
    n = 0
    for bi in range(6):
        if st[31 + 10 * bi:31 + 10 * bi + 10] == empty_ids:
            n += 1
    return n


def run_stage(eng, st, h, sr, ctx, eps0):
    s, r = sr
    pre_all = list(st)
    pre_core = st[:31]
    eng.apply_rle(st, ctx["W_rle"])
    expect(st[:31] == ctx["afterW"][(s, r)], "K4",
           f"after-W core mismatch, stage {h}, input {sr}")
    expect(st[31:] == pre_all[31:], "K3", f"W touched slots 31..100, stage {h}")
    check_boundary(eng, st, eps0, f"after W stage {h}")
    after_w_core = st[:31]
    for (src, tgt, lab) in ((11, 31 + 20 * h, (-r) % 5),
                            (21, 41 + 20 * h, (-r - DELTA[s]) % 5)):
        work_before = st[src:src + 10]
        for mi, codes in enumerate(ctx["Kmods"][(src, tgt)]):
            eng.apply_rle(st, codes)
            expect(st[src:src + 10] == work_before, "K5",
                   f"workbank at {src} not restored at K module {mi}, stage {h}")
        expect(st[tgt:tgt + 10] == ctx["marked"][lab], "K3",
               f"archive at {tgt} != M[{lab}], stage {h}")
        expect(st[:31] == after_w_core, "K5",
               f"core before W^-1 is not exactly the after-W core, stage {h}")
    check_boundary(eng, st, eps0, f"after copies stage {h}")
    eng.apply_rle(st, ctx["Winv_rle"])
    expect(st[:31] == pre_core, "K5",
           f"core not restored after W^-1, stage {h}, input {sr}")
    expect(st[31:31 + 20 * h] == pre_all[31:31 + 20 * h], "K3",
           f"earlier archives changed in stage {h}")
    check_boundary(eng, st, eps0, f"after W^-1 stage {h}")


def audit_cache(eng):
    seen = set()
    n_entries = 0
    for key, packed in list(eng.cache.items()):
        n_entries += 1
        run = key >> 40
        a = eng.elems[(key >> SHIFT) & MASK]
        b = eng.elems[key & MASK]
        for _ in range(run):
            if (a, b) not in seen:
                seen.add((a, b))
                o4 = contact4(a, b)
                expect(o4 == contact5(a, b), "K1",
                       f"cache pair cross-representation mismatch at {a} {b}")
                x, y, _ = o4
                expect(qform(x) + qform(y) == qform(a) + qform(b)
                       and zadd(x, y) == zadd(a, b)
                       and eps(x) == eps(a) and eps(y) == eps(b), "K1",
                       f"cache pair invariant failure at {a} {b}")
            a, b, _ = contact4(a, b)
        expect(a == eng.elems[packed >> SHIFT] and b == eng.elems[packed & MASK],
               "K1", "cache entry disagrees with literal contact iteration")
    return n_entries, len(seen)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Independent blind reviewer (see PREREG.md)")
    ap.add_argument("--triples", type=int, default=1000,
                    help="number of ordered triples to execute (1..1000, default 1000)")
    args = ap.parse_args(argv)
    ntr = args.triples
    if not 1 <= ntr <= 1000:
        print("FAIL: --triples out of range", file=sys.stderr)
        return 1
    t0 = time.monotonic()
    done = set()
    detail = {}
    try:
        detail["k1_box_pairs"] = check_K1_ring()
        detail.update(check_local())
        # ---- words and counts (K8), from my own literal builds
        S, parts = build_S()
        S2 = build_S_second()
        expect(S == S2, "K9", "primary and second builds of S differ")
        lens = {k: len(v) for k, v in parts.items()}
        expect(lens == {"L": 10, "SCAN": 80, "E": 10, "WA": 105, "WB": 105,
                        "D": 9, "V": 23, "R": 261, "S": 535},
               "K8", f"subword lengths {lens}")
        W = S * 10
        W_inv = invert_contacts(W)
        expect(len(W) == 5350 and len(W_inv) == 21400, "K8", "W / W^-1 length wrong")
        fwd_ops, meta = build_forward(W, W_inv)
        inv_ops = build_inverse(fwd_ops)
        nf = sum(1 for o in fwd_ops if o[0] == 0); ns = sum(1 for o in fwd_ops if o[0] == 1)
        ni = sum(1 for o in inv_ops if o[0] == 0); nis = sum(1 for o in inv_ops if o[0] == 1)
        expect((nf, ns, ni, nis) == (80610, 10, 322440, 10), "K8",
               f"program counts {(nf, ns, ni, nis)} != (80610,10,322440,10)")
        expect(5350 + 60 + 60 + 21400 == 26870 and 3 * 26870 == 80610, "K8", "U arithmetic")
        expect(len(TRIPLES) == 1000 and len(set(TRIPLES)) == 1000, "K8", "triple set != 1000")
        expect(1000 * (80610 + 322440) == 403050000 and 1000 * 20 == 20000, "K8",
               "inventory arithmetic")
        expect(26 + 25 * 3 == 101 and 68 + 74 * 3 == 290 and 5 ** 4 == 625 < 1000 <= 5 ** 5,
               "K7", "k=3 resource/capacity formula substitution")
        done.add("K8")
        # ---- RLE fidelity: decompression must reproduce every literal word
        W_rle = rle_encode(contacts_to_ops(W))
        Winv_rle = rle_encode(contacts_to_ops(W_inv))
        inv_rle = rle_encode(inv_ops)
        fwd_rle = rle_encode(fwd_ops)
        for name, codes, ops in (("W", W_rle, contacts_to_ops(W)),
                                 ("W^-1", Winv_rle, contacts_to_ops(W_inv)),
                                 ("forward", fwd_rle, fwd_ops),
                                 ("inverse", inv_rle, inv_ops)):
            expect(rle_decode(codes) == ops, "K8", f"RLE decompression != literal {name}")
        kmods = {}
        for h in range(3):
            for (src, tgt) in ((11, 31 + 20 * h), (21, 41 + 20 * h)):
                mods = K_modules(src, tgt)
                rles = [rle_encode(contacts_to_ops(m)) for m in mods]
                for m, codes in zip(mods, rles):
                    expect(rle_decode(codes) == contacts_to_ops(m), "K8",
                           "RLE decompression != literal K module")
                kmods[(src, tgt)] = rles
        # ---- static support: archives never touched outside their own K (K3)
        arch_slots = [(base, set(range(base, base + 10))) for (base, _, _) in meta["archive_K"]]
        krange = {base: (ks, ke) for (base, ks, ke) in meta["archive_K"]}
        for idx, (kind, i, k) in enumerate(fwd_ops):
            for base, slots in arch_slots:
                if i in slots or k in slots:
                    ks, ke = krange[base]
                    expect(ks <= idx < ke, "K3",
                           f"archive at {base} touched at op {idx} outside its K")
        for h, (ss, se) in enumerate(meta["stages"]):
            allowed = set(range(31)) | set(range(31 + 20 * h, 51 + 20 * h))
            for (kind, i, k) in fwd_ops[ss:se]:
                expect(i in allowed and k in allowed, "K3",
                       f"stage {h} op touches slots outside core+own archives")
        for h, (ss, se) in enumerate(meta["swaps"]):
            allowed = set(range(5)) | set(range(91 + 5 * h, 96 + 5 * h))
            for (kind, i, k) in fwd_ops[ss:se]:
                expect(kind == 1 and i in allowed and k in allowed, "K3",
                       f"swap block {h} touches unexpected slots")
        # ---- literal (non-RLE, element-level) audits of W and W^-1, all inputs
        for (s, r) in INPUTS:
            out, _ = apply_contacts_elems(core_elems(s, r), W)
            expect(out == after_w_core_elems(s, r), "K4",
                   f"literal W action mismatch for input {(s, r)}")
            back, _ = apply_contacts_elems(out, W_inv)
            expect(back == core_elems(s, r), "K6",
                   f"literal W^-1 failed for input {(s, r)}")
        # ---- literal complete forward+inverse for triple 0 (engine cross-check)
        lit_fin = apply_ops_elems(initial_elems(TRIPLES[0]), fwd_ops)
        expect(lit_fin == final_elems(TRIPLES[0]), "K4",
               "literal full forward, triple 0, differs from closed formula")
        lit_back = apply_ops_elems(lit_fin, inv_ops)
        expect(lit_back == initial_elems(TRIPLES[0]), "K6",
               "literal full inverse, triple 0, does not restore initial state")
        detail["literal_triple0"] = "forward+inverse element-level, no RLE/cache"
        # ---- engine context
        eng = Engine()
        ctx = {"W_rle": W_rle, "Winv_rle": Winv_rle, "Kmods": kmods,
               "afterW": {sr: eng.id_state(after_w_core_elems(*sr)) for sr in INPUTS},
               "marked": [eng.id_state(bk) for bk in BANKS]}
        empty_ids = eng.id_state(BANK_EMPTY)
        input_ids = {sr: eng.id_state(input5(*sr)) for sr in INPUTS}
        core_ids = {sr: eng.id_state(core_elems(*sr)) for sr in INPUTS}
        # Single U (stage 0) for all 10 inputs, engine path.
        for sr in INPUTS:
            trip = (sr, sr, sr)
            st = eng.id_state(initial_elems(trip))
            eps0 = [eng.epsvals[i] for i in st]
            run_stage(eng, st, 0, sr, ctx, eps0)
            expect(st[:31] == core_ids[sr], "K5", f"single U did not restore core {sr}")
        # ---- decoder injectivity on closed-form archives, all 1000
        arch_seen = set()
        for trip in TRIPLES:
            arch = final_elems(trip)[31:91]
            expect(decode_archives(arch) == trip, "K3",
                   f"closed-form decoder mismatch for {trip}")
            arch_seen.add(tuple(arch))
        expect(len(arch_seen) == 1000, "K3", "archive records not injective on 1000 triples")
        detail["decoder_injective_on"] = 1000
        # ---- main trajectories
        aggA = hashlib.sha256(); aggB = hashlib.sha256()
        final0_elems = None
        fresh_seq_seen = None
        for ti in range(ntr):
            trip = TRIPLES[ti]
            st = eng.id_state(initial_elems(trip))
            expect(len(st) == 101, "K2", "carrier != 101 slots")
            init_ids = list(st)
            eps0 = [eng.epsvals[i] for i in st]
            check_boundary(eng, st, eps0, f"initial triple {ti}")
            aux = [st[i] for i in range(101) if i not in
                   list(range(0, 5)) + list(range(91, 101))]
            expect(len(aux) == 86 and sum(eng.qvals[i] for i in aux) == 248, "K2",
                   f"auxiliary account != 248 on 86 slots, triple {ti}")
            expect(sum(eng.qvals[i] for i in st[0:5] + st[91:101]) == 42, "K2",
                   f"input-system account != 42, triple {ti}")
            fresh_seq = [fresh_bank_count(st, empty_ids) // 2]
            archive_snapshot = list(st[31:91])
            for h in range(3):
                run_stage(eng, st, h, trip[h], ctx, eps0)
                expect(st[:31] == core_ids[trip[h]], "K5",
                       f"core != prepared stage input after stage {h}, triple {ti}")
                expect(st[11:21] == empty_ids and st[21:31] == empty_ids, "K5",
                       f"workbanks not blank after stage {h}, triple {ti}")
                fresh_seq.append(fresh_bank_count(st, empty_ids) // 2)
                new_arch = st[31 + 20 * h:51 + 20 * h]
                expect(new_arch != empty_ids * 2, "K3",
                       f"stage {h} archives still blank, triple {ti}")
                if h > 0:
                    expect(st[31:31 + 20 * h] == archive_snapshot[:20 * h], "K3",
                           f"earlier archives changed by stage {h}, triple {ti}")
                archive_snapshot = list(st[31:91])
                if h < 2:
                    base = 91 + 5 * h
                    mid_before = list(st[5:31])
                    for i in range(5):
                        expect(eng.epsvals[st[i]] == eng.epsvals[st[base + i]], "K2",
                               f"swap residues differ, block {h} slot {i}, triple {ti}")
                    eng.apply_rle(st, rle_encode([(1, i, base + i) for i in range(5)]))
                    expect(st[0:5] == input_ids[trip[h + 1]], "K4",
                           f"next input not loaded after swap {h}, triple {ti}")
                    expect(st[base:base + 5] == input_ids[trip[h]], "K4",
                           f"spent input not parked in cartridge {h}, triple {ti}")
                    expect(st[5:31] == mid_before, "K5",
                           f"controls/workbanks changed by swap {h}, triple {ti}")
                    expect(st[31:91] == archive_snapshot, "K3",
                           f"archives changed by swap {h}, triple {ti}")
                    check_boundary(eng, st, eps0, f"after swap {h} triple {ti}")
            expect(fresh_seq == [3, 2, 1, 0], "K7",
                   f"fresh archive-pair sequence {fresh_seq} != [3,2,1,0], triple {ti}")
            fresh_seq_seen = fresh_seq
            expect(st == eng.id_state(final_elems(trip)), "K4",
                   f"final 101-slot state != closed formula, triple {ti} {trip}")
            expect(st[11:21] == empty_ids and st[21:31] == empty_ids, "K3",
                   f"records left in workbanks at end, triple {ti}")
            dec = decode_archives(eng.elems_of(st[31:91]))
            expect(dec == trip, "K3", f"archive-only decoder failed, triple {ti}")
            check_boundary(eng, st, eps0, f"final triple {ti}")
            fin_elems = eng.elems_of(st)
            aggA.update(ser_state_A(fin_elems) + b"\n")
            aggB.update(ser_state_B(fin_elems) + b"\n")
            if ti == 0:
                final0_elems = fin_elems
            eng.apply_rle(st, inv_rle)
            expect(st == init_ids, "K6",
                   f"complete literal inverse did not restore initial state, triple {ti}")
            check_boundary(eng, st, eps0, f"after inverse triple {ti}")
        detail["triples_executed"] = ntr
        detail["fresh_pairs_sequence"] = fresh_seq_seen
        detail["cache_entries"], detail["cache_distinct_pairs"] = audit_cache(eng)
        done.update({"K1", "K2", "K3", "K4", "K5", "K6", "K7"})
        # ---- fingerprints under my frozen serialisation (K9)
        fp = {}
        for name, ops in (("S", contacts_to_ops(S)), ("W", contacts_to_ops(W)),
                          ("K(11,31)", contacts_to_ops(K_word(11, 31))),
                          ("forward", fwd_ops), ("inverse", inv_ops)):
            a, b = ser_ops_A(ops), ser_ops_B(ops)
            expect(a == b, "K9", f"my two word serialisers differ on {name}")
            fp[name] = sha(a)
        init0 = initial_elems(TRIPLES[0])
        for name, elems in (("initial_triple0", init0), ("final_triple0", final0_elems)):
            a, b = ser_state_A(elems), ser_state_B(elems)
            expect(a == b, "K9", f"my two state serialisers differ on {name}")
            fp[name] = sha(a)
        expect(aggA.hexdigest() == aggB.hexdigest(), "K9",
               "my two serialisers differ on aggregate of final states")
        fp[f"aggregate_finals_first_{ntr}"] = aggA.hexdigest()
        expect(sha(ser_ops_A(contacts_to_ops(S2))) == fp["S"],
               "K9", "second S build fingerprint != primary")
        detail["fingerprints"] = fp
        done.add("K9")
    except Fail as e:
        elapsed = time.monotonic() - t0
        for klabel in ("K1", "K2", "K3", "K4", "K5", "K6", "K7", "K8", "K9"):
            status = "FAIL" if klabel == e.klabel else ("PASS" if klabel in done else "INCOMPLETE")
            print(f"{klabel}: {status}")
        print(f"FAILURE [{e.klabel}]: {e.msg}")
        print(f"Scope: {'full' if ntr == 1000 else 'PARTIAL'} (triples={ntr}/1000)")
        print(f"Elapsed_seconds (operational only): {elapsed:.2f}")
        print("RESULT: FAIL")
        return 1
    elapsed = time.monotonic() - t0
    for klabel in ("K1", "K2", "K3", "K4", "K5", "K6", "K7", "K8", "K9"):
        print(f"{klabel}: PASS")
    print(f"K1_box_pairs_crosschecked: {detail['k1_box_pairs']}")
    print(f"K1_cache_entries_audited: {detail['cache_entries']}")
    print(f"K1_cache_distinct_pairs_audited: {detail['cache_distinct_pairs']}")
    print(f"W6_admitted_counts: {detail['w6_admitted']} (cases elsewhere,p,q)")
    print(f"K_admitted_per_mark: 41 of 60; K_noninvolution_cases_of_5: {detail['k_noninvolution_cases']}")
    print(f"Literal_triple0: {detail['literal_triple0']}")
    print(f"Decoder_injective_closed_form_on: {detail['decoder_injective_on']} triples")
    print(f"Fresh_archive_pairs_at_boundaries: {detail['fresh_pairs_sequence']}")
    print("Archive_consumption_per_experiment: 2 banks = 20 slots, preparation account 60")
    print("Archive_consumption_3_experiments: 6 banks = 60 slots, preparation account 180")
    print(f"Contacts_per_forward: 80610; swaps_per_forward: 10; contacts_per_inverse: 322440; swaps_per_inverse: 10")
    print(f"Inventory_contacts_if_full: {1000 * (80610 + 322440)}; executed_triples: {ntr}")
    print(f"Executed_contact_applications_literal_count: {ntr * (80610 + 322440)} (RLE/cache-audited, see PREREG)")
    for name, val in detail["fingerprints"].items():
        print(f"Fingerprint[{name}]: {val}")
    print(f"Elapsed_seconds (operational only): {elapsed:.2f}")
    if ntr == 1000:
        print("Scope: full (triples=1000/1000, forward+inverse)")
        print("RESULT: PASS (full)")
        return 0
    print(f"Scope: PARTIAL (triples={ntr}/1000) -- all executed checks passed, inventory not complete")
    print("RESULT: PARTIAL-PASS (not a full pass)")
    return 2


if __name__ == "__main__":
    sys.exit(main())





