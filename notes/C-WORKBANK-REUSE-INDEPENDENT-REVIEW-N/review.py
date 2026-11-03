#!/usr/bin/env python3
"""Independent review aid for PR1879, P-RELATIVE-CONTACT-WORKBANK-REUSE-1.

NON-CANONICAL / L1. Review instrument, not a probe verifier and not evidence
that changes any public status. Written from the text of PROOF.md at source
pin 6f6570bbbddfc496131dd31c5fdacaaa9e1cd9e5 and the Public Canon v108 contact
and common-apparatus sections. The target verify.py, its EXPECTED.txt and the
supplied PR1879 review code were not read or imported before this file ran.

Arithmetic is done in a cyclic representation of O=Z[j], namely Z[x]/(x^5-1)
reduced modulo the all-ones vector to j-basis coefficients (1,j,j^2,j^3).
Multiplication by rho=j^2 is a cyclic shift; it is cross-checked against a
separately written j-basis linear map on every new contact entry. Q is
computed both by the coefficient formula and as Tr(z*conj(z))/2.

Usage (from the repository root or anywhere):

    python3 -I review.py WORD535.txt

The single argument is the unchanged v108 fixture, used only to compare the
independently rebuilt 535-contact word. Standard library only, exact integers,
no randomness, no network, no file writes. Every check raises SystemExit with
a message on failure (no bare assert is relied on, so -O cannot disable it).
"""

import hashlib
import itertools
import re
import sys


def need(cond, msg):
    if not cond:
        raise SystemExit("FAIL: " + msg)


# ---------------------------------------------------------------- arithmetic

def norm5(c):
    t = c[4]
    return (c[0] - t, c[1] - t, c[2] - t, c[3] - t)


def lift(a):
    return (a[0], a[1], a[2], a[3], 0)


def add(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2], a[3] + b[3])


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2], a[3] - b[3])


def neg(a):
    return (-a[0], -a[1], -a[2], -a[3])


def mul(a, b):
    A, B = lift(a), lift(b)
    c = [0] * 5
    for i in range(5):
        if A[i]:
            for k in range(5):
                c[(i + k) % 5] += A[i] * B[k]
    return norm5(c)


def rho_cyc(a):
    A = lift(a)
    c = [0] * 5
    for i in range(5):
        c[(i + 2) % 5] = A[i]
    return norm5(c)


def rho_lin(a):
    # j^2*(z0+z1 j+z2 j^2+z3 j^3) with j^4=-1-j-j^2-j^3, written directly.
    z0, z1, z2, z3 = a
    return (z3 - z2, -z2, z0 - z2, z1 - z2)


def conj(a):
    A = lift(a)
    c = [0] * 5
    for i in range(5):
        c[(-i) % 5] = A[i]
    return norm5(c)


def trace(a):
    return 4 * a[0] - a[1] - a[2] - a[3]


def q_formula(a):
    n = 5 * sum(x * x for x in a) - sum(a) ** 2
    need(n % 2 == 0, "odd Q numerator")
    return n // 2


def q_trace(a):
    n = trace(mul(a, conj(a)))
    need(n % 2 == 0, "odd trace")
    return n // 2


def eps(a):
    return sum(a) % 5


def even(a):
    return all(x % 2 == 0 for x in a)


def half(a):
    need(even(a), "non-exact halving")
    return (a[0] // 2, a[1] // 2, a[2] // 2, a[3] // 2)


def contact(x, y):
    d = sub(x, y)
    if not even(d):
        return x, y, 0
    s = half(add(x, y))
    t = half(d)
    rt = rho_cyc(t)
    need(rt == rho_lin(t), "rho representations disagree")
    return add(s, rt), sub(s, rt), 1


ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
TWO = (2, 0, 0, 0)
RHO = (0, 0, 1, 0)


def rpow(e):
    r = ONE
    for _ in range(e % 5):
        r = mul(r, RHO)
    return r


def u_(e):
    return sub(ONE, rpow(e))


def w_(e):
    return add(ONE, rpow(e))


u, w, b = u_(1), w_(1), w_(2)
need(b == (0, -1, -1, -1), "b in j basis")
need(q_formula(u) == 5 and q_formula(w) == 3 and q_formula(b) == 3, "Q(u,w,b)")


# ------------------------------------------------- interned values and cache

VALS = []
IDX = {}
QV = []
EV = []
HV = []
M = 1 << 24


def iid(v):
    r = IDX.get(v)
    if r is None:
        r = len(VALS)
        need(r < M, "intern overflow")
        IDX[v] = r
        VALS.append(v)
        qa, qb = q_formula(v), q_trace(v)
        need(qa == qb, "two Q computations disagree")
        QV.append(qa)
        EV.append(eps(v))
        HV.append(mul(v, conj(v)))
    return r


CACHE = {}
STATS = {"cache_entries": 0}


def make_entry(key):
    ix, iy = divmod(key, M)
    x, y = VALS[ix], VALS[iy]
    x2, y2, adm = contact(x, y)
    # local certificates on every distinct entry
    need(add(x2, y2) == add(x, y), "pair sum")
    need(q_formula(x2) + q_formula(y2) == q_formula(x) + q_formula(y), "pair Q")
    need(add(mul(x2, conj(x2)), mul(y2, conj(y2)))
         == add(mul(x, conj(x)), mul(y, conj(y))), "pair Hermitian")
    need(eps(x2) == eps(x) and eps(y2) == eps(y), "slot residues")
    need(rho_cyc(x2) == mul(RHO, x2), "rho multiplication path")
    # orientation symmetry C(i,k)=C(k,i)
    y3, x3, _ = contact(y, x)
    need((x3, y3) == (x2, y2), "contact orientation symmetry")
    # rho equivariance including the guard
    xr, yr, admr = contact(rho_cyc(x), rho_cyc(y))
    need(admr == adm and xr == rho_cyc(x2) and yr == rho_cyc(y2), "equivariance")
    # C^5 = identity
    a, c = x, y
    for _ in range(5):
        a, c, _ = contact(a, c)
    need((a, c) == (x, y), "C^5")
    r = (iid(x2), iid(y2), adm)
    CACHE[key] = r
    STATS["cache_entries"] += 1
    return r


def run(st, word):
    """Execute a word on an id-state in place; return admitted contact count."""
    cache = CACHE
    adm = 0
    for kind, i, k in word:
        if kind:
            st[i], st[k] = st[k], st[i]
        else:
            key = st[i] * M + st[k]
            r = cache.get(key)
            if r is None:
                r = make_entry(key)
            st[i] = r[0]
            st[k] = r[1]
            adm += r[2]
    return adm


def ids(vals):
    return [iid(v) for v in vals]


def ncontacts(word):
    return sum(1 for kind, _, _ in word if kind == 0)


def nswaps(word):
    return sum(1 for kind, _, _ in word if kind == 1)


def C(i, k, n=1):
    return [(0, i, k)] * n


def SW(i, k):
    return [(1, i, k)]


def literal_inverse(word):
    out = []
    for kind, i, k in reversed(word):
        out += [(kind, i, k)] * (1 if kind else 4)
    return out


def support(word):
    s = set()
    for _, i, k in word:
        s.add(i)
        s.add(k)
    return s


OUT = []


def say(line):
    OUT.append(line)
    print(line)


# ----------------------------------------------------------- section 1 law

def check_contact_law():
    box = range(-1, 2)
    elems = [tuple(t) for t in itertools.product(box, repeat=4)]
    n = adm = 0
    for x in elems:
        ix = iid(x)
        for y in elems:
            key = ix * M + iid(y)
            r = CACHE.get(key) or make_entry(key)
            n += 1
            adm += r[2]
    need(n == 81 * 81, "box size")
    # equal entries are fixed even though admitted
    for x in elems:
        x2, y2, a = contact(x, x)
        need(a == 1 and (x2, y2) == (x, x), "diagonal fixed")
    # O/2O = F_16 facts used by the proof
    red = lambda z: tuple(c % 2 for c in z)
    need(red(rpow(1)) != red(ONE), "rho != 1 mod 2")
    for e in range(1, 5):
        need(not even(w_(e)), "1+rho^e nonzero mod 2")
    need(not even(b), "b nonzero mod 2")
    say("LAW box pairs=%d admitted=%d diagonal_fixed=81 F16_facts=PASS" % (n, adm))


# -------------------------------------------------- section 2 local lemma

W6 = [(1, 4), (1, 4), (4, 5), (1, 4), (1, 4), (1, 4),
      (1, 6), (1, 6), (1, 6), (1, 6), (1, 4), (1, 6)]


def w6_on(base_places):
    return [(0, base_places[a - 1], base_places[c - 1]) for a, c in W6]


def check_parity_guard():
    for P in range(5):
        for Qp in range(5):
            x = neg(mul(rpow(P), b))
            y = mul(rpow(Qp), b)
            x2, y2, a = contact(x, y)
            need(a == (1 if P == Qp else 0), "opposite-sign guard")
            if a:
                need(x2 == neg(mul(rpow(P + 1), b)) and y2 == mul(rpow(P + 1), b),
                     "admitted phase increment")
            y3, x3, a3 = contact(y, x)
            need(a3 == a and (x3, y3) == (x2, y2), "positive-first rule")
    say("GUARD opposite-sign (-rho^P b, rho^Q b): admitted iff P=Q, both +1: PASS (25 cases, both orders)")


def phase_model(P, Qp, R, S):
    adm = []
    st = [P, Qp, R, S]
    rule = {(1, 4): (0, 1), (4, 5): (1, 2), (1, 6): (0, 3)}
    for a, c in W6:
        i, k = rule[(a, c)]
        if st[i] == st[k]:
            st[i] = (st[i] + 1) % 5
            st[k] = (st[k] + 1) % 5
            adm.append("A")
        else:
            adm.append("R")
    return tuple(st), "".join(adm)


def check_local_lemma():
    agree = 0
    restored_fresh = []
    for P, Qp, R, S in itertools.product(range(5), repeat=4):
        vals = [neg(mul(rpow(P), b)), mul(rpow(P), b),
                neg(mul(rpow(Qp), b)), mul(rpow(Qp), b),
                neg(mul(rpow(R), b)), mul(rpow(S), b)]
        st = ids(vals)
        before = list(st)
        word = w6_on([0, 1, 2, 3, 4, 5])
        trace_adm = []
        for kind, i, k in word:
            key = st[i] * M + st[k]
            r = CACHE.get(key) or make_entry(key)
            st[i], st[k] = r[0], r[1]
            trace_adm.append("A" if r[2] else "R")
        model, madm = phase_model(P, Qp, R, S)
        got = [VALS[x] for x in st]
        exp = [neg(mul(rpow(model[0]), b)), mul(rpow(P), b),
               neg(mul(rpow(Qp), b)), mul(rpow(model[1]), b),
               neg(mul(rpow(model[2]), b)), mul(rpow(model[3]), b)]
        need(got == exp and "".join(trace_adm) == madm, "phase abstraction")
        need(st[1] == before[1] and st[2] == before[2], "places 2,3 untouched")
        agree += 1
        if R == 0 and S == 0 and (model[0], model[1]) == (P, Qp):
            restored_fresh.append(((P, Qp), model[2:]))
    rows = {(0, 0, 0, 0): ((0, 0, 0, 0), "AARAAAAAAARA"),
            (1, 0, 0, 0): ((1, 0, 1, 1), "RRAAAARRRRAA"),
            (0, 1, 0, 0): ((0, 1, 0, 0), "RRRRRRAAAARA")}
    for init, (fin, word) in rows.items():
        need(phase_model(*init) == (fin, word), "local row %s" % (init,))
    need(phase_model(0, 0, 1, 1)[0] == (2, 1, 1, 2), "occupied-target counterexample")
    say("LOCAL W6 ring=phase-model on all %d phase states: PASS" % agree)
    say("LOCAL rows (0,0,0,0)->(0,0,0,0) 10A, (1,0,0,0)->(1,0,1,1) 6A, (0,1,0,0)->(0,1,0,0) 5A: PASS")
    say("LOCAL occupied target (0,0,1,1)->(2,1,1,2) source not restored: PASS")
    say("LOCAL fresh-target inputs with source restored: %d of 25 (P,Q) -> %s"
        % (len(restored_fresh), " ".join("%d%d:%d%d" % (p, q, r, s)
                                         for (p, q), (r, s) in restored_fresh)))


# ------------------------------------------------------ section 3 copier

def copier(a, d):
    word = []
    for p in range(5):
        q = (p + 1) % 5
        word += w6_on([a + 2 * p, a + 2 * p + 1, a + 2 * q, a + 2 * q + 1,
                       d + 2 * p, d + 2 * p + 1])
    return word


_BANK = {}


def bank(p=None):
    if p not in _BANK:
        out = []
        for i in range(5):
            ph = 1 if i == p else 0
            out += [neg(mul(rpow(ph), b)), mul(rpow(ph), b)]
        _BANK[p] = tuple(out)
    return list(_BANK[p])


def scale(vals, t):
    return [mul(rpow(t), v) for v in vals]


def check_copier():
    K = copier(0, 10)
    Ki = literal_inverse(K)
    need(ncontacts(K) == 60 and ncontacts(Ki) == 240, "copier lengths")
    need(support(K) == set(range(20)), "copier support")
    banks = [bank()] + [bank(p) for p in range(5)]
    need(len(set(map(tuple, banks))) == 6, "six distinct bank states")
    for bk in banks:
        need(sum(q_formula(v) for v in bk) == 30, "bank account")
        need(tuple(eps(v) for v in bk) == (3, 2) * 5, "bank residues")
    cases = 0
    for r in range(5):
        pattern = None
        for t in range(5):
            st = ids(scale(bank(r) + bank(), t))
            src0 = st[:10]
            adm = 0
            pat = []
            for p in range(5):
                seg = K[12 * p:12 * p + 12]
                for kind, i, k in seg:
                    key = st[i] * M + st[k]
                    e = CACHE.get(key) or make_entry(key)
                    st[i], st[k] = e[0], e[1]
                    pat.append(e[2])
                    adm += e[2]
                need(st[:10] == src0, "source restored at module boundary")
            need([VALS[x] for x in st] == scale(bank(r) + bank(r), t), "copy identity")
            need(adm == 41, "admitted count 41")
            if pattern is None:
                pattern = pat
            need(pat == pattern, "rotation keeps admission pattern")
            run(st, Ki)
            need([VALS[x] for x in st] == scale(bank(r) + bank(), t), "inverse")
            cases += 1
    # documented boundaries: not an involution; occupied target outside contract
    st = ids(bank(2) + bank())
    run(st, K)
    run(st, K)
    need([VALS[x] for x in st] != bank(2) + bank(), "K is not an involution")
    occ_bad = 0
    for r in range(5):
        for p in range(5):
            st = ids(bank(r) + bank(p))
            run(st, K)
            if [VALS[x] for x in st][:10] != bank(r):
                occ_bad += 1
    say("COPY K(M[r],M_empty)=(M[r],M[r]) all r x 5 global rotations=%d cases, 41/60 admitted, "
        "source restored at 5 module boundaries, 240-contact inverse: PASS" % cases)
    say("COPY boundary: K.K != id on (M[2],M_empty); occupied targets (M[r],M[p]) with source "
        "not restored: %d of 25 (outside contract, informational)" % occ_bad)


# ------------------------------------------------- section 4 obstruction

def check_obstruction():
    """Sanity check only: the algebraic proof in PROOF section 4 suffices."""
    edges = [(i, k) for i in range(4) for k in range(i + 1, 4)]
    results = []
    for name, bb in (("b=1+rho^2", b), ("b=1", ONE), ("b=u", u)):
        E = (neg(bb), bb, neg(bb), bb)
        A = (neg(mul(RHO, bb)), mul(RHO, bb), neg(bb), bb)
        T = tuple(mul(RHO, v) for v in E)
        need(A != T, "A != T for nonzero b")
        start = tuple(iid(v) for v in E + A + T)
        seen = {start}
        frontier = [start]
        while frontier:
            nxt = []
            for st in frontier:
                for i, k in edges:
                    new = list(st)
                    for off in (0, 4, 8):
                        key = st[off + i] * M + st[off + k]
                        e = CACHE.get(key) or make_entry(key)
                        new[off + i], new[off + k] = e[0], e[1]
                    new = tuple(new)
                    if new not in seen:
                        seen.add(new)
                        nxt.append(new)
            frontier = nxt
            need(len(seen) < 1000000, "orbit cap")
        e_ids = tuple(iid(v) for v in E)
        t_ids = tuple(iid(v) for v in T)
        single = set(st[0:4] for st in seen)
        for st in seen:
            need(st[8:12] == tuple(iid(mul(RHO, VALS[x])) for x in st[0:4]), "F(T)=rho F(E)")
            need(not (st[0:4] == e_ids and st[4:8] == t_ids), "obstruction violated")
        need(t_ids in set(st[4:8] for st in seen), "T is reachable from A alone")
        results.append("%s:words-orbit=%d single-orbit=%d" % (name, len(seen), len(single)))
    say("OBSTRUCTION algebraic proof checked; BFS sanity: no word with F(E)=E and F(A)=T, "
        "although T is separately reachable from A; F(T)=rho F(E) on every reached word; %s: PASS"
        % " ".join(results))


# ------------------------------------------------ section 5 read apparatus

def _Y(a):
    if a == 0:
        return (ZERO, TWO, ZERO)
    if a <= 4:
        return (u_(a), w_(a), ZERO)
    e = a - 4
    return (ZERO, w_(e), u_(e))


def _X(r):
    x = mul(rpow(r), w)
    return (x, neg(x))


_YT = [_Y(a) for a in range(9)]
_XT = [_X(r) for r in range(5)]


def Y(a):
    return list(_YT[a % 9])


def X(r):
    return list(_XT[r % 5])


CONTROLS = [ZERO, u, ZERO, ZERO, w, ZERO]


def core(s, r, pa=None, pb=None):
    return Y(s) + X(r) + CONTROLS + bank(pa) + bank(pb)


O1 = C(1, 5)
A0 = C(5, 9)
O2 = C(9, 10)
TT = C(3, 4)


def Bc(c, n=1):
    return C(c, 9, n)


def Eblk(c):
    return A0 + Bc(c) + A0 * 4 + Bc(c, 4)


def Einv(c):
    return Bc(c) + A0 + Bc(c, 4) + A0 * 4


def Lblk(q, p):
    a, bb = q + 2 * p, q + 2 * p + 1
    return C(3, a, 4) + C(a, bb, 4) + C(3, a) + C(a, bb)


def SCAN(q):
    out = []
    for p in range(5):
        out += C(3, 10) + Lblk(q, p) + C(3, 10, 4) + TT
    return out


WA = Eblk(6) + O2 + SCAN(11) + O2 * 4 + Einv(6)
WB = Eblk(7) + O2 + SCAN(21) + O2 * 4 + Einv(7)


def Dblk(c, d):
    return C(9, c, 3) + C(9, d, 3) + C(9, c) + C(9, d) + C(9, c)


def Vblk(c, d):
    return A0 + Dblk(c, d) + A0 * 4 + Dblk(c, d)


RW = O1 + WA + WB + Vblk(7, 8) + Vblk(6, 7) + O1 * 4
FW = C(0, 1) + C(1, 2)
FINV = C(1, 2, 4) + C(0, 1, 4)
SW535 = RW + FINV + RW + FW + FW + TT
WW = SW535 * 10
WINV = literal_inverse(WW)
DELTA = {0: 1, 1: 8}


def check_word(fixture_path):
    lens = [len(Lblk(11, 0)), len(SCAN(11)), len(Eblk(6)), len(WA), len(WB),
            len(Dblk(7, 8)), len(Vblk(7, 8)), len(RW), len(SW535)]
    need(lens == [10, 80, 10, 105, 105, 9, 23, 261, 535], "block lengths %s" % lens)
    with open(fixture_path, "rb") as fh:
        raw = fh.read()
    digest = hashlib.sha256(raw).hexdigest()
    need(digest == "ca6bdd7a9b43e329cbc3630f26e32125b1d16a9872b9563e57733f5c408c916b",
         "fixture hash")
    pairs = []
    for line in raw.decode("ascii").splitlines():
        if re.match(r"^\d{3}-\d{3}:", line):
            pairs += [(int(a) - 1, int(c) - 1) for a, c in re.findall(r"C\((\d+),(\d+)\)", line)]
    need(pairs == [(i, k) for _, i, k in SW535], "rebuilt S differs from WORD535 fixture")
    need(ncontacts(WW) == 5350 and ncontacts(WINV) == 21400, "W lengths")
    need(support(WW) == set(range(31)), "W support is the 31-slot core")
    say("WORD S rebuilt from block equations: lengths 10,80,10,105,105,9,23,261,535; "
        "equals WORD535 fixture (sha256 ca6bdd7a...916b) contact by contact: PASS")


def check_source_clock():
    for a in range(9):
        st = ids(Y(a))
        run(st, FW)
        need([VALS[x] for x in st] == Y(a + 1), "F(Y_a)=Y_(a+1)")
        st = ids(Y(a))
        run(st, FINV)
        need([VALS[x] for x in st] == Y(a - 1), "F^-1")
    need(len({tuple(Y(a)) for a in range(9)}) == 9, "nine distinct sources")
    st = ids([ZERO, TWO, ZERO])
    for n in range(9):
        need([VALS[x] for x in st] == Y(n), "Y_n=F^n(0,2,0)")
        run(st, FW)
    for r in range(5):
        st = ids(Y(0) + X(r))
        run(st, TT)
        need([VALS[x] for x in st] == Y(0) + X(r + 1), "T(X_r)")
    need(len({tuple(X(r)) for r in range(5)}) == 5, "five distinct clocks")
    say("SOURCE F nine-cycle, Y_n=F^n(0,2,0), F^-1, clock T five-cycle: PASS")


def predicted_events(s, r):
    ev = []
    for t in range(10):
        if (s + t) % 9 == 0:
            ev.append((t, "first"))
        if (s + t - 1) % 9 == 0:
            ev.append((t, "second"))
    acts = ["A", "B", "skip"]
    return [(t, which, acts[n], (-(r + t)) % 5 if acts[n] != "skip" else None)
            for n, (t, which) in enumerate(ev)]


def decode_bank(vals):
    for p in range(5):
        if vals == bank(p):
            return p
    return None


def check_read_stage():
    table = []
    for s in (0, 1):
        for r in range(5):
            st = ids(core(s, r))
            events = []
            for t in range(10):
                need([VALS[x] for x in st[:5]] == Y(s + t) + X(r + t), "S boundary phases")
                for which, pre in (("first", []), ("second", FINV)):
                    run(st, pre)
                    before = [VALS[x] for x in st]
                    run(st, RW)
                    after = [VALS[x] for x in st]
                    need(after[:6] == before[:6] and after[9:11] == before[9:11],
                         "R restores source, clock, g, h, t")
                    for tok in (before[6:9], after[6:9]):
                        need(sorted(tok) == sorted([u, ZERO, ZERO]), "one-token selector")
                    if after[6:9] != before[6:9]:
                        sel = "ABS"[[before[6], before[7], before[8]].index(u)]
                        nsel = "ABS"[[after[6], after[7], after[8]].index(u)]
                        need("ABSA".index(sel) + 1 == "ABSA".index(nsel, "ABSA".index(sel) + 1),
                             "selector cycles A->B->skip->A")
                        if sel == "A":
                            need(before[11:21] == bank() and after[21:31] == before[21:31],
                                 "A write on fresh A only")
                            lab = decode_bank(after[11:21])
                        elif sel == "B":
                            need(before[21:31] == bank() and after[11:21] == before[11:21],
                                 "B write on fresh B only")
                            lab = decode_bank(after[21:31])
                        else:
                            need(after[11:31] == before[11:31], "skip preserves banks")
                            lab = None
                        need(sel == "S" or lab == (-(r + t)) % 5, "write label -clock")
                        events.append((t, which, {"A": "A", "B": "B", "S": "skip"}[sel], lab))
                    else:
                        need(after[11:31] == before[11:31], "inactive read preserves banks")
                run(st, FW + FW + TT)
            need(events == predicted_events(s, r), "event table s=%d r=%d" % (s, r))
            got = [VALS[x] for x in st]
            need(got == core(s + 10, r, (-r) % 5, (-r - DELTA[s]) % 5), "W endpoint")
            run(st, WINV)
            need([VALS[x] for x in st] == core(s, r), "W^-1 restores I(s,r)")
            if r == 0:
                table.append("s=%d:%s" % (s, ",".join("(%d,%s)" % (t, wh) for t, wh, _, _ in events)))
    say("READ W=S^10 on all 10 inputs: 20 R boundaries each, events match mod-9 table %s; "
        "endpoint (Y_(s+10),X_r,controls,M[-r],M[-r-Delta_s]); literal W^-1 restores: PASS"
        % " ".join(table))


# ---------------------------------------------------- sections 6-8 program

def layout(k):
    arch = [(31 + 20 * j, 41 + 20 * j) for j in range(k)]
    cart = [None] + [31 + 20 * k + 5 * (j - 1) for j in range(1, k)]
    return arch, cart, 26 + 25 * k


def program(k):
    arch, cart, n = layout(k)
    segs = []
    for j in range(k):
        if j >= 1:
            pi = []
            for i in range(5):
                pi += SW(i, cart[j] + i)
            segs.append(("Pi", j, pi))
        a, d = arch[j]
        segs.append(("W", j, WW))
        segs.append(("KA", j, copier(11, a)))
        segs.append(("KB", j, copier(21, d)))
        segs.append(("Winv", j, WINV))
    return segs, n


def initial(k, tup):
    arch, cart, n = layout(k)
    s0, r0 = tup[0]
    st = core(s0, r0)
    for j in range(k):
        st += bank() + bank()
    for j in range(1, k):
        st += Y(tup[j][0]) + X(tup[j][1])
    need(len(st) == n, "slot count")
    return st


def accounts(idst):
    E = sum(QV[x] for x in idst)
    S = ZERO
    H = ZERO
    for x in idst:
        S = add(S, VALS[x])
        H = add(H, HV[x])
    res = tuple(EV[x] for x in idst)
    return E, S, H, res


def check_supports(kmax):
    for k in range(1, kmax + 1):
        segs, n = program(k)
        arch, cart, _ = layout(k)
        flat = []
        for _, _, wd in segs:
            flat += wd
        need(ncontacts(flat) == 26870 * k and nswaps(flat) == 5 * (k - 1), "forward counts")
        inv = literal_inverse(flat)
        need(ncontacts(inv) == 107480 * k and nswaps(inv) == 5 * (k - 1), "inverse counts")
        need(max(support(flat)) == n - 1 and min(support(flat)) == 0, "address range")
        need(support(flat) <= set(range(n)), "support within carrier")
        pos = 0
        last = {}
        ends = {}
        for name, j, wd in segs:
            for idx, (_, i, kk) in enumerate(wd):
                last[i] = pos + idx
                last[kk] = pos + idx
            if name in ("KA", "KB"):
                ends[(name, j)] = (pos, pos + len(wd) - 1)
            pos += len(wd)
        for j in range(k):
            for name, base in (("KA", arch[j][0]), ("KB", arch[j][1])):
                lo, hi = ends[(name, j)]
                need(all(lo <= last[x] <= hi for x in range(base, base + 10)),
                     "archive untouched after its own copy")
        for name, j, wd in segs:
            sp = support(wd)
            if name in ("W", "Winv"):
                need(sp <= set(range(31)), "W support")
            elif name == "KA":
                need(sp == set(range(11, 21)) | set(range(arch[j][0], arch[j][0] + 10)), "KA support")
            elif name == "KB":
                need(sp == set(range(21, 31)) | set(range(arch[j][1], arch[j][1] + 10)), "KB support")
            else:
                need(sp == set(range(5)) | set(range(cart[j], cart[j] + 5)), "Pi support")
    say("SUPPORT k=1..%d: forward 26870k contacts/5(k-1) swaps, literal inverse 107480k/5(k-1), "
        "segment supports exact, every archive bank last touched by its own copier: PASS" % kmax)


INPUTS = [(s, r) for s in (0, 1) for r in range(5)]


def run_program(k, tuples, label):
    segs, n = program(k)
    arch, cart, _ = layout(k)
    flat = []
    for _, _, wd in segs:
        flat += wd
    inv = literal_inverse(flat)
    total_c = total_s = 0
    checkpoints = 0
    decoded = set()
    ref_aux = None
    acc0 = None
    copy_adm_ok = 0
    input_addr = set(range(5))
    for j in range(1, k):
        input_addr |= set(range(cart[j], cart[j] + 5))
    aux_addr = [i for i in range(n) if i not in input_addr]
    varying = None
    first_vals = None
    for tup in tuples:
        init_vals = initial(k, tup)
        st = ids(init_vals)
        init_ids = list(st)
        acc = accounts(st)
        aux = [st[i] for i in aux_addr]
        if ref_aux is None:
            ref_aux, acc0 = aux, acc
            first_vals = init_ids
            varying = set()
        need(aux == ref_aux, "common auxiliary preparation")
        need(acc[0] == acc0[0] and acc[1] == acc0[1] and acc[2] == acc0[2], "input-independent accounts")
        for i in range(n):
            if init_ids[i] != first_vals[i]:
                varying.add(i)
        for name, j, wd in segs:
            s_j, r_j = tup[j]
            if name == "Pi":
                for _, i, kk in wd:
                    need(EV[st[i]] == EV[st[kk]], "swap of equal residues")
            adm = run(st, wd)
            total_c += ncontacts(wd)
            total_s += nswaps(wd)
            cur = [VALS[x] for x in st]
            if name == "W":
                need(cur[:31] == core(s_j + 10, r_j, (-r_j) % 5, (-r_j - DELTA[s_j]) % 5), "W core")
            elif name == "KA":
                need(cur[11:21] == bank((-r_j) % 5), "work bank A restored after copy")
                a = arch[j][0]
                need(cur[a:a + 10] == bank((-r_j) % 5), "archive A written")
                need(adm == 41, "KA admitted")
            elif name == "KB":
                need(cur[21:31] == bank((-r_j - DELTA[s_j]) % 5), "work bank B restored after copy")
                d = arch[j][1]
                need(cur[d:d + 10] == bank((-r_j - DELTA[s_j]) % 5), "archive B written")
                need(adm == 41, "KB admitted")
                copy_adm_ok += 1
            elif name == "Winv":
                need(cur[:31] == core(s_j, r_j), "complete 31-slot core restored")
            else:
                need(cur[:31] == core(s_j, r_j), "core loaded with next input")
                prev = tup[j - 1]
                need(cur[cart[j]:cart[j] + 5] == Y(prev[0]) + X(prev[1]), "parked restored input")
            # whole-carrier closed form at every segment boundary
            for jj in range(k):
                a, d = arch[jj]
                done_a = jj < j or (jj == j and name in ("KA", "KB", "Winv"))
                done_b = jj < j or (jj == j and name in ("KB", "Winv"))
                sa, ra = tup[jj]
                need(cur[a:a + 10] == (bank((-ra) % 5) if done_a else bank()), "archive A state")
                need(cur[d:d + 10] == (bank((-ra - DELTA[sa]) % 5) if done_b else bank()), "archive B state")
            for jj in range(1, k):
                exp = tup[jj - 1] if jj <= j else tup[jj]
                need(cur[cart[jj]:cart[jj] + 5] == Y(exp[0]) + X(exp[1]), "cartridge state")
            a2 = accounts(st)
            need(a2 == acc, "complete E, sum, Hermitian and labelled residues")
            checkpoints += 1
        # archive-only decoder
        cur = [VALS[x] for x in st]
        rec = []
        for jj in range(k):
            a, d = arch[jj]
            pa = decode_bank(cur[a:a + 10])
            pb = decode_bank(cur[d:d + 10])
            need(pa is not None and pb is not None, "decoder rejects")
            dd = (pa - pb) % 5
            need(dd in (1, 3), "decoder difference")
            rec.append((0 if dd == 1 else 1, (-pa) % 5))
        need(tuple(rec) == tuple(tup), "decoded tuple")
        decoded.add(tuple(rec))
        run(st, inv)
        total_c += ncontacts(inv)
        total_s += nswaps(inv)
        need(st == init_ids, "full literal inverse restores every coordinate")
    need(len(decoded) == len(tuples), "decoder injective")
    E, S, H, _ = acc0
    say("%s k=%d tuples=%d slots=%d E=%d aux_E=%d (%d addr) sum=%s H=%s varying_coords=%d "
        "checkpoints=%d copy_pairs_82_admitted=%d contacts=%d swaps=%d decoded_distinct=%d inverse_restores=%d: PASS"
        % (label, k, len(tuples), n, E, sum(QV[x] for x in ref_aux), len(aux_addr), S, H, len(varying),
           checkpoints, copy_adm_ok, total_c, total_s, len(decoded), len(tuples)))
    return E, S, H, n, sum(QV[x] for x in ref_aux), len(aux_addr), total_c, total_s


def check_resources(results):
    for k, (E, S, H, n, auxE, auxN, _, _) in results.items():
        need(n == 26 + 25 * k and E == 68 + 74 * k and S == (2 * (k + 1), 0, 0, 0), "resource formulas")
        need(auxE == 68 + 60 * k and auxN == 26 + 20 * k, "auxiliary formulas")
    need(results[3][2] == (108, 0, -74, -74), "k=3 Hermitian 108-74j^2-74j^3")
    bounds = []
    for k in range(1, 7):
        B = 0
        while 5 ** B < 10 ** k:
            B += 1
        bounds.append("k=%d:min%d/built%d" % (k, B, 2 * k))
        need(B <= 2 * k, "construction above counting bound")
    say("RESOURCES slots 26+25k, E 68+74k, aux 68+60k on 26+20k addr, sum 2(k+1), "
        "k=3 H=108-74j^2-74j^3; counting bound 5^B>=10^k %s: PASS" % " ".join(bounds))


def main():
    if len(sys.argv) != 2:
        raise SystemExit("usage: review.py WORD535.txt")
    check_contact_law()
    check_parity_guard()
    check_local_lemma()
    check_copier()
    check_obstruction()
    check_word(sys.argv[1])
    check_source_clock()
    check_read_stage()
    check_supports(6)
    results = {}
    for k in (1, 2, 3):
        tuples = list(itertools.product(INPUTS, repeat=k))
        results[k] = run_program(k, tuples, "EXHAUSTIVE")
    need(results[3][6] == 403050000 and results[3][7] == 20000, "k=3 trajectory totals")
    for k in (4, 5):
        sample = [tuple(INPUTS[(i + m * j) % 10] for j in range(k))
                  for m in (0, 1, 3) for i in range(10)]
        results[k] = run_program(k, sample, "SAMPLE(not proof)")
    check_resources(results)
    say("CACHE distinct contact entries certified=%d interned values=%d" % (STATS["cache_entries"], len(VALS)))
    body = "\n".join(OUT) + "\n"
    print("REVIEW-OUTPUT-SHA256 %s" % hashlib.sha256(body.encode()).hexdigest())
    print("ALL REVIEW CHECKS PASS")


if __name__ == "__main__":
    main()
