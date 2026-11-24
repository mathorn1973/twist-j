#!/usr/bin/env python3
"""Independent blind reviewer for PR #1865 contract (see PREREG.md).

Written from the PR texts only. Reads no author code, data or output,
and no file at all. Exact integer arithmetic only.
Convention: element of O=Z[j] is (a0,a1,a2,a3) = a0+a1*j+a2*j^2+a3*j^3.
"""
import argparse
import hashlib
import sys
from collections import Counter

ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
JGEN = (0, 1, 0, 0)
RHO = (0, 0, 1, 0)
JJ = (1, 0, 1, 0)   # J = 1+rho
UU = (1, 0, -1, 0)  # u = 1-rho
D = 12
EDGES = tuple((0, k) for k in range(1, 16))  # 15 contacts, 16 core slots


def add(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2], a[3] + b[3])


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2], a[3] - b[3])


def scal(k, a):
    return (k * a[0], k * a[1], k * a[2], k * a[3])


def mul_a(a, b):
    """Multiplication A: polynomial product, reduce j^4=-1-j-j^2-j^3."""
    c = [0] * 7
    for i in range(4):
        for j in range(4):
            c[i + j] += a[i] * b[j]
    for k in range(6, 3, -1):
        coeff = c[k]
        if coeff:
            for t in range(k - 4, k):
                c[t] -= coeff
            c[k] = 0
    return tuple(c[:4])


def mul_b(a, b):
    """Multiplication B: cyclic length-5 convolution mod j^5-1."""
    a5 = list(a) + [0]
    b5 = list(b) + [0]
    c5 = [0] * 5
    for i in range(5):
        for j in range(5):
            c5[(i + j) % 5] += a5[i] * b5[j]
    return tuple(c5[i] - c5[4] for i in range(4))


def epow(a, n):
    r = ONE
    for _ in range(n):
        r = mul_a(r, a)
    return r


JPOW = [epow(JJ, k) for k in range(17)]
JINV = sub(ZERO, add(RHO, epow(RHO, 3)))  # -rho-rho^3
JINVPOW = [epow(JINV, k) for k in range(17)]
U2 = mul_a(UU, UU)
UJ_POW = [mul_a(UU, JPOW[k]) for k in range(17)]       # u*J^k
U2J_POW = [mul_a(U2, JPOW[k]) for k in range(17)]      # u^2*J^k


def bar(z):
    """Automorphism j -> j^4, built from images of basis elements."""
    img = [ONE, (-1, -1, -1, -1), (0, 0, 0, 1), (0, 0, 1, 0)]
    r = ZERO
    for i in range(4):
        r = add(r, scal(z[i], img[i]))
    return r


def trace_o(w):
    return 4 * w[0] - w[1] - w[2] - w[3]


def q1(z):
    num = 5 * sum(x * x for x in z) - sum(z) ** 2
    assert num % 2 == 0
    return num // 2


def q2(z):
    t = trace_o(mul_a(z, bar(z)))
    assert t % 2 == 0
    return t // 2


def eps(z):
    return sum(z) % 5


def is_even(z):
    return all(x % 2 == 0 for x in z)


def half(z):
    assert is_even(z)
    return tuple(x // 2 for x in z)


def contact(a, b):
    """Total contact from definition. Returns (a', b', admitted)."""
    d = sub(a, b)
    if not is_even(d):
        return a, b, False
    s = half(add(a, b))
    t = half(d)
    rt = mul_a(RHO, t)
    return add(s, rt), sub(s, rt), True


class Audit:
    def __init__(self):
        self.ok = {}
        self.msg = {}
        self.count = Counter()

    def note(self, rid, cond, detail=""):
        self.count[rid] += 1
        if rid not in self.ok:
            self.ok[rid] = True
        if not cond:
            self.ok[rid] = False
            self.msg.setdefault(rid, detail)

    def verdict(self, rid):
        return self.ok.get(rid, False)


AUD = Audit()
PAIRS = set()
NCONTACT = [0]


def apply_edge(state, i, j):
    PAIRS.add((state[i], state[j]))
    NCONTACT[0] += 1
    a2, b2, adm = contact(state[i], state[j])
    state[i], state[j] = a2, b2
    return adm


def run_word(state):
    """Returns (final_state, admissions, after_edge0_slots01, after_edge1_slots02)."""
    st = list(state)
    admissions = []
    snap1 = snap2 = None
    for idx, (i, j) in enumerate(EDGES):
        admissions.append(apply_edge(st, i, j))
        if idx == 0:
            snap1 = (st[0], st[1])
        if idx == 1:
            snap2 = (st[0], st[1], st[2])
    return st, admissions, snap1, snap2


def run_inverse(state):
    st = list(state)
    for (i, j) in reversed(EDGES):
        for _ in range(4):
            apply_edge(st, i, j)
    return st


def v2m(x):
    v = 0
    while x % 2 == 0:
        x //= 2
        v += 1
    return v, x


def source_state(q, n, archives=None):
    a = scal(2 * (q - 1) * n, UU)
    b = scal(2 * n, add(scal(q - 1, UU), (2, 0, 0, 0)))
    st = [a, b, scal(2, JJ)] + [ZERO] * 13
    if archives is not None:
        st = st + list(archives)
    return st


def total_q(state):
    return sum(q1(z) for z in state)


def total_sum(state):
    r = ZERO
    for z in state:
        r = add(r, z)
    return r


class ReaderError(Exception):
    pass


def reader(active, cascade):
    """Only current active slot + 13 cascade slots. Returns (m, v, r) or
    the string 'DEPTH_LIMIT'; raises ReaderError on malformed input."""
    if len(cascade) != 13:
        raise ReaderError("cascade length")
    if all(z != ZERO for z in cascade):
        return "DEPTH_LIMIT"
    v = 0
    while v < 13 and cascade[v] != ZERO:
        v += 1
    if any(z != ZERO for z in cascade[v:]):
        raise ReaderError("nonzero after zero")
    r = mul_a(JINVPOW[v + 1], active)
    if not (r[1] == 0 and r[3] == 0 and r[2] == -r[0] and r[0] > 0):
        raise ReaderError("bad r shape %r" % (r,))
    return r[0], v, r


def prefix_expected(q, n):
    a1 = scal(2 * q * n, UU)
    b1 = scal(2 * n, add(scal(q, ONE), scal(-(q - 2), RHO)))
    a2 = scal(q * n + 1, UJ_POW[1])          # u*J*(qn+1)
    c2 = add(scal(q * n, U2), JPOW[2])       # q*u^2*n + J^2
    return a1, b1, a2, c2


def final_expected(q, n):
    """Closed-form final core state (independent of iterated contacts)."""
    x = q * n + 1
    v, m = v2m(x)
    _a1, b1, _a2, c2 = prefix_expected(q, n)
    st = [ZERO] * 16
    st[0] = scal(m, UJ_POW[v + 1])
    st[1] = b1
    st[2] = c2
    for s in range(1, 14):
        if s <= v:
            st[2 + s] = scal(x // (2 ** s), U2J_POW[s])
    return st, v, m


NINV = [0]
DEPTHS = {"A": Counter(), "B": Counter()}
FINGER_LINES = []


def process_case(q, n, corpus, archives=None, depth_limit=False):
    tag = "q=%d n=%d %s" % (q, n, corpus)
    init = source_state(q, n, archives)
    core_init_q = total_q(init[:16])
    formula_q = (40 * q * (q - 1) + 32) * n * n + 12
    AUD.note("R09", core_init_q == formula_q, tag + " source Q")
    fin, adm, snap1, snap2 = run_word(init)
    a1, b1, a2, c2 = prefix_expected(q, n)
    AUD.note("R09", snap1 == (a1, b1), tag + " after C01")
    AUD.note("R09", snap2 == (a2, b1, c2), tag + " after C02")
    AUD.note("R09", total_q(fin) == total_q(init), tag + " total Q kept")
    AUD.note("R09", total_sum(fin) == total_sum(init), tag + " total sum kept")
    AUD.note("R09", all(eps(fin[i]) == eps(init[i]) for i in range(len(init))),
             tag + " eps per slot")
    AUD.note("R02", all(q1(z) == q2(z) for z in fin), tag + " Q1=Q2 final")
    if archives is not None:
        AUD.note("R12", fin[16:] == list(archives), tag + " archives kept")
        AUD.note("R12", total_q(fin) == core_init_q + sum(q1(z) for z in archives),
                 tag + " archive account")
    back = run_inverse(fin)
    NINV[0] += 1
    AUD.note("R11", back == init, tag + " full inverse")
    rd = None
    try:
        rd = reader(fin[0], tuple(fin[3:16]))
    except ReaderError as e:
        AUD.note("R09" if not depth_limit else "R13", False, tag + " reader " + str(e))
    if depth_limit:
        x = q * n + 1
        AUD.note("R13", x == 2 ** 14, tag + " x=2^14")
        AUD.note("R13", all(z != ZERO for z in fin[3:16]), tag + " 13 nonzero")
        AUD.note("R13", fin[0] == scal(2, UJ_POW[14]) and is_even(fin[0]),
                 tag + " active 2uJ^14 even")
        AUD.note("R13", rd == "DEPTH_LIMIT", tag + " DEPTH_LIMIT")
        AUD.note("R13", adm == [True] * 15, tag + " all admitted")
        expc = [scal(x // (2 ** s), U2J_POW[s]) for s in range(1, 14)]
        AUD.note("R13", fin[3:16] == expc, tag + " cascade formula")
        AUD.note("R13", fin[1] == b1 and fin[2] == c2, tag + " leftovers")
        return fin
    exp, v, m = final_expected(q, n)
    AUD.note("R09", v <= D and m % 2 == 1 and (2 ** v) * m == q * n + 1, tag + " v,m")
    AUD.note("R09", fin[:16] == exp, tag + " final closed form")
    AUD.note("R09", adm == [True, True] + [s <= v for s in range(1, 14)],
             tag + " admission prefix")
    AUD.note("R09", all(fin[2 + s] != ZERO for s in range(1, v + 1)), tag + " first v nonzero")
    AUD.note("R09", all(fin[2 + s] == ZERO for s in range(v + 1, 14)), tag + " tail zero")
    if isinstance(rd, tuple):
        rm, rv, r = rd
        AUD.note("R09", (rm, rv) == (m, v), tag + " reader (m,v)")
        AUD.note("R09", r == (m, 0, -m, 0), tag + " r shape")
        AUD.note("R02", q1(r) == 5 * m * m, tag + " Q(r)=5m^2")
        num = (2 ** v) * m - 1
        AUD.note("R09", num % q == 0 and num // q == n, tag + " arithmetic inverse")
        if corpus in DEPTHS:
            DEPTHS[corpus][rv] += 1
    # R15: output is not a fresh source, not pure m, leftovers remain
    fresh = source_state(q, m)
    AUD.note("R15", fin[:16] != fresh, tag + " != E_q(m)")
    AUD.note("R15", fin[0] != (m, 0, 0, 0), tag + " active != pure m")
    AUD.note("R15", fin[1] == b1 and fin[1] != ZERO and fin[2] == c2,
             tag + " leftovers remain")
    if corpus == "A" and archives is None:
        slots = ";".join(",".join(str(c) for c in z) for z in fin[:16])
        FINGER_LINES.append("n=%d|%s" % (n, slots))
    return fin


def det_set():
    vals = (-2, -1, 0, 1, 2)
    s = [(a, b, c, 0) for a in vals for b in vals for c in vals]
    s += [(0, b, c, d) for b in vals for c in vals for d in vals]
    return s


def check_ring():
    AUD.note("R01", epow(RHO, 5) == ONE)
    AUD.note("R01", all(epow(RHO, k) != ONE for k in range(1, 5)))
    tot = ZERO
    for k in range(5):
        tot = add(tot, epow(RHO, k))
    AUD.note("R01", tot == ZERO, "1+rho+..+rho^4=0")
    AUD.note("R01", add(JJ, UU) == (2, 0, 0, 0), "J+u=2")
    AUD.note("R01", sub(JJ, UU) == scal(2, RHO), "J-u=2rho")
    AUD.note("R01", mul_a(JJ, JINV) == ONE, "J*Jinv=1")
    AUD.note("R01", JINV == (0, -1, -1, 0), "Jinv tuple -rho-rho^3")
    S = det_set()
    AUD.note("R01", all(mul_a(a, b) == mul_b(a, b) for a in S for b in S),
             "mul A == mul B on deterministic set")
    AUD.note("R02", all(q1(z) == q2(z) for z in S), "Q1=Q2 on set")
    AUD.note("R02", q1(UU) == 5 and q1(JJ) == 3 and q1(scal(2, JJ)) == 12
             and q1(ONE) == 2 and q1(ZERO) == 0, "Q(u),Q(J),Q(2J),Q(1)")
    AUD.note("R02", all(q1(epow(JGEN, k)) == 2 for k in range(5)), "Q(j^k)=2")
    # contact closed form vs definition, on admitted pairs from S
    ok = True
    for a in S[::11]:
        for b in S[::13]:
            a2, b2, adm = contact(a, b)
            AUD.note("R04", adm == is_even(sub(a, b)), "admission iff even diff")
            if not adm:
                AUD.note("R04", (a2, b2) == (a, b), "refused = identity")
            else:
                alt = (half(add(mul_a(JJ, a), mul_a(UU, b))),
                       half(add(mul_a(UU, a), mul_a(JJ, b))))
                if alt != (a2, b2):
                    ok = False
    AUD.note("R04", ok, "contact == ((Ja+ub)/2,(ua+Jb)/2)")


def check_symbolic():
    import sympy as sp
    q, n = sp.symbols("q n")

    def sadd(a, b):
        return tuple(sp.expand(x + y) for x, y in zip(a, b))

    def sscal(k, a):
        return tuple(sp.expand(k * x) for x in a)

    def smul_fixed(f, a):
        # f integer tuple, a symbolic tuple
        c = [sp.Integer(0)] * 7
        for i in range(4):
            for j in range(4):
                c[i + j] = c[i + j] + f[i] * a[j]
        for k in range(6, 3, -1):
            coeff = c[k]
            for t in range(k - 4, k):
                c[t] = c[t] - coeff
            c[k] = sp.Integer(0)
        return tuple(sp.expand(x) for x in c[:4])

    def seq(a, b):
        return all(sp.expand(x - y) == 0 for x, y in zip(a, b))

    def scontact(a, b):
        s = sscal(sp.Rational(1, 2), sadd(a, b))
        t = sscal(sp.Rational(1, 2), tuple(x - y for x, y in zip(a, b)))
        rt = smul_fixed(RHO, t)
        return sadd(s, rt), tuple(sp.expand(x - y) for x, y in zip(s, rt))

    ui = tuple(sp.Integer(x) for x in UU)
    a = sscal(2 * (q - 1) * n, ui)
    b = sscal(2 * n, sadd(sscal(q - 1, ui), (sp.Integer(2), 0, 0, 0)))
    c = tuple(sp.Integer(x) for x in scal(2, JJ))
    diff = tuple(sp.expand(x - y) for x, y in zip(a, b))
    AUD.note("R05", seq(diff, (sp.expand(-4 * n), 0, 0, 0)), "a-b=-4n symbolic")
    a1, b1 = scontact(a, b)
    exp_a1 = sscal(2 * q * n, ui)
    exp_b1 = sscal(2 * n, (q, sp.Integer(0), -(q - 2), sp.Integer(0)))
    AUD.note("R05", seq(a1, exp_a1) and seq(b1, exp_b1), "symbolic after C01")
    a2, c2 = scontact(a1, c)
    uj = tuple(sp.Integer(x) for x in UJ_POW[1])
    exp_a2 = sscal(q * n + 1, uj)
    exp_c2 = sadd(sscal(q * n, tuple(sp.Integer(x) for x in U2)),
                  tuple(sp.Integer(x) for x in JPOW[2]))
    AUD.note("R05", seq(a2, exp_a2) and seq(c2, exp_c2), "symbolic after C02")
    AUD.note("R05", all(sp.denom(x) == 1 for x in a1 + b1 + a2 + c2),
             "symbolic prefix integral")
    # R06 source account/sum symbolic
    def sq(z):
        return sp.expand((5 * sum(x * x for x in z) - sum(z) ** 2) / 2)
    totq = sp.expand(sq(a) + sq(b) + sq(c) - ((40 * q * (q - 1) + 32) * n ** 2 + 12))
    AUD.note("R06", totq == 0, "symbolic source Q formula")
    AUD.note("R06", sp.expand((40 * 3 * 2 + 32) - 272) == 0, "q=3 coeff 272")
    stot = sadd(sadd(a, b), c)
    exp_s = sadd(sscal(4 * n, (q, sp.Integer(0), -(q - 1), sp.Integer(0))),
                 tuple(sp.Integer(x) for x in scal(2, JJ)))
    AUD.note("R06", seq(stot, exp_s), "symbolic source sum")
    # R07 one cascade step with free Y
    y = sp.symbols("y0:4")
    x = sscal(2, y)
    o1, o2 = scontact(x, (sp.Integer(0),) * 4)
    AUD.note("R07", seq(o1, smul_fixed(JJ, y)) and seq(o2, smul_fixed(UU, y)),
             "C(2Y,0)=(JY,uY)")
    # R02 Gram eigenvalues; R03 norms; R16 family identity
    g = (5 * sp.eye(4) - sp.ones(4, 4)) / 2
    AUD.note("R02", set(g.eigenvals()) == {sp.Rational(1, 2), sp.Rational(5, 2)},
             "Gram eigenvalues {1/2,5/2}")

    def mult_matrix(e):
        cols = [mul_a(e, basis) for basis in
                [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]]
        return sp.Matrix(4, 4, lambda r, cc: cols[cc][r])
    AUD.note("R03", mult_matrix(UU).det() == 5, "N(u) det = 5")
    AUD.note("R03", abs(mult_matrix(JJ).det()) == 1, "N(J) det = +-1")
    m_expr = (3 * n + 1) / 2
    AUD.note("R16", sp.expand(272 * (m_expr ** 2 - n ** 2)
                              - 68 * (5 * n ** 2 + 6 * n + 1)) == 0,
             "272(m^2-n^2)=68(5n^2+6n+1) for m=(3n+1)/2")


def check_pairs():
    for (a, b) in PAIRS:
        a2, b2, adm = contact(a, b)
        AUD.note("R04", add(a2, b2) == add(a, b), "pair sum %r %r" % (a, b))
        AUD.note("R04", q1(a2) + q1(b2) == q1(a) + q1(b), "pair Q")
        AUD.note("R04", eps(a2) == eps(a) and eps(b2) == eps(b), "pair eps")
        x, y = a, b
        for _ in range(5):
            x, y, _ad = contact(x, y)
        AUD.note("R04", (x, y) == (a, b), "C^5=id")
        x, y = a2, b2
        for _ in range(4):
            x, y, _ad = contact(x, y)
        AUD.note("R04", (x, y) == (a, b), "C^4 inverse")


def check_reader_boundaries(sample_fin):
    fin = sample_fin
    inp = (fin[0], tuple(fin[3:16]))
    out1 = reader(*inp)
    # mutate non-reader slots in a copy of the full state; reader input unchanged
    alt = list(fin)
    alt[1] = (99, -7, 3, 5)
    alt[2] = (-11, 0, 42, 1)
    out2 = reader(alt[0], tuple(alt[3:16]))
    AUD.note("R14", out1 == out2 == reader(*inp), "reader ignores slots1,2; deterministic")
    casc = list(fin[3:16])
    if sum(1 for z in casc if z != ZERO) >= 2:
        casc[0] = ZERO
        try:
            reader(fin[0], tuple(casc))
            AUD.note("R14", False, "gap cascade accepted")
        except ReaderError:
            AUD.note("R14", True)
    try:
        reader(ONE, tuple([ZERO] * 13))
        AUD.note("R14", False, "bad r shape accepted")
    except ReaderError:
        AUD.note("R14", True)
    AUD.note("R14", reader(ONE, tuple([ONE] * 13)) == "DEPTH_LIMIT",
             "synthetic all-nonzero DEPTH_LIMIT")


def check_residue_and_bound():
    init3 = source_state(3, 3)
    fresh5 = source_state(3, 5)
    AUD.note("R15", eps(init3[1]) == (4 * 3) % 5 and eps(fresh5[1]) == (4 * 5) % 5
             and eps(init3[1]) != eps(fresh5[1]), "eps obstruction 3->5 slot1")
    AUD.note("R16", total_q(init3) == 272 * 9 + 12 == 2460, "account E3(3)=2460")
    AUD.note("R16", total_q(fresh5) == 272 * 25 + 12 == 6812, "account E3(5)=6812")
    AUD.note("R16", total_q(fresh5) - total_q(init3) == 272 * (25 - 9) == 4352,
             "gap 4352 = 272*(m^2-n^2)")
    for n in (3, 7, 11, 99, 4095):
        v, m = v2m(3 * n + 1)
        if n % 4 == 3:
            AUD.note("R16", v == 1 and 272 * (m * m - n * n)
                     == 68 * (5 * n * n + 6 * n + 1), "family n=3 mod4 n=%d" % n)
    # necessity arithmetic: with B=0, 4352 <= B is false
    AUD.note("R16", not (4352 <= 0), "B=0 cannot meet necessary bound 3->5")


def main(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument("--scope", choices=["full", "sample"], default="full")
    args = p.parse_args(argv)
    full = args.scope == "full"
    print("SCOPE %s" % args.scope)
    AUD.note("R08", len(EDGES) == 15 and EDGES == tuple((0, k) for k in range(1, 16)),
             "word 15 edges")
    edge_payload = ";".join("%d>%d" % e for e in EDGES).encode("utf-8")
    print("EDGE_FINGERPRINT_MINE sha256=%s bytes=%d payload=%s"
          % (hashlib.sha256(edge_payload).hexdigest(), len(edge_payload),
             edge_payload.decode("utf-8")))
    check_ring()
    check_symbolic()
    a_ns = list(range(1, 4096, 2)) if full else list(range(1, 256, 2))
    b_ns = list(range(1, 128, 2)) if full else list(range(1, 32, 2))
    sample_fin = None
    for n in a_ns:
        fin = process_case(3, n, "A")
        if n == 27:
            sample_fin = fin
    for q in range(1, 10):
        for n in b_ns:
            process_case(q, n, "B")
    c_ns = [1, 3, 5, 7, 15, 27, 85, 1365, 4095] if full else [1, 3, 27]
    arch_vals = [ZERO, ONE, JGEN, UU, JJ] if full else [ZERO, JJ]
    nc = 0
    for n in c_ns:
        for a16 in arch_vals:
            for a17 in arch_vals:
                process_case(3, n, "C", archives=(a16, a17))
                nc += 1
    process_case(3, 5461, "W", depth_limit=True)
    exp_a = Counter(v2m(3 * n + 1)[0] for n in a_ns)
    exp_b = Counter(v2m(q * n + 1)[0] for q in range(1, 10) for n in b_ns)
    AUD.note("R10", DEPTHS["A"] == exp_a, "depth dist A vs independent v2")
    AUD.note("R10", DEPTHS["B"] == exp_b, "depth dist B vs independent v2")
    if full:
        AUD.note("R10", all(DEPTHS["A"][d] > 0 for d in range(1, 13)), "depths 1..12 occur")
        AUD.note("R10", DEPTHS["B"][0] == 256, "256 depth-zero in B")
        AUD.note("R09", len(a_ns) == 2048 and 9 * len(b_ns) == 576, "counts 2048/576")
        AUD.note("R12", nc == 225, "225 archive cases")
        AUD.note("R11", NINV[0] == 2850, "2850 full inverses, got %d" % NINV[0])
    print("COUNTS A=%d B=%d C=%d witness=1 inverses=%d contacts=%d distinct_pairs=%d"
          % (len(a_ns), 9 * len(b_ns), nc, NINV[0], NCONTACT[0], len(PAIRS)))
    print("DEPTHS_A %s" % dict(sorted(DEPTHS["A"].items())))
    print("DEPTHS_B %s" % dict(sorted(DEPTHS["B"].items())))
    check_pairs()
    if sample_fin is not None:
        check_reader_boundaries(sample_fin)
    check_residue_and_bound()
    payload = ("\n".join(FINGER_LINES) + "\n").encode("utf-8") if FINGER_LINES else b""
    AUD.note("R17", len(FINGER_LINES) == len(a_ns), "fingerprint lines == corpus A")
    AUD.note("R17", all(line.count(";") == 15 for line in FINGER_LINES),
             "each line 16 slots")
    print("FINGERPRINT_MINE sha256=%s payload_bytes=%d lines=%d"
          % (hashlib.sha256(payload).hexdigest(), len(payload), len(FINGER_LINES)))
    ids = ["R%02d" % i for i in range(1, 18)]
    allok = True
    for rid in ids:
        ok = AUD.verdict(rid)
        allok = allok and ok
        extra = (" :: " + AUD.msg[rid]) if rid in AUD.msg else ""
        print("%s %s (checks=%d)%s" % ("PASS" if ok else "FAIL", rid,
                                       AUD.count[rid], extra))
    print("RESULT %s" % ("PASS" if allok else "FAILURE"))
    return 0 if allok else 1


if __name__ == "__main__":
    sys.exit(main())
