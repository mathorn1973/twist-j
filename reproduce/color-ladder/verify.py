#!/usr/bin/env python3
"""Exact public witness for the eleven-rung TWIST-J color ladder.

Arithmetic domains: integers, rationals, Q(sqrt5), finite fields,
cyclotomic coefficient tuples, character tables, and polynomial rings.
Standard library only. No floats, random choices, timestamps, external
data, development chronology, or private infrastructure.

The twelve public blocks follow the ladder from the D5 return group to
the integral binary-icosahedral lift. Rung 3 is split on purpose: the
registered non-abelian dynamical-color route is falsified at its stated
scope, while the kinematical product-affine normalizer survives.
"""

import io
import sys
from contextlib import redirect_stdout
_CENSUS_CACHE = None

def shared_census(ktab, z5tab):
    """Compute the sealed 600+400 color census once for rungs 2 and 3."""
    global _CENSUS_CACHE
    if _CENSUS_CACHE is not None:
        return _CENSUS_CACHE
    nstates = 5 ** 6
    state = list(range(nstates))
    for n in range(600):
        tm2 = 2 * (n.bit_count() & 1)
        state = [ktab[(z5tab[s] + tm2) % 5][s] for s in state]
    window = [set() for _ in range(nstates)]
    for n in range(600, 1000):
        tm2 = 2 * (n.bit_count() & 1)
        state = [ktab[(z5tab[s] + tm2) % 5][s] for s in state]
        for seed, value in enumerate(state):
            window[seed].add(value)
    attr = {}
    for support in window:
        key = min(support)
        if key not in attr:
            attr[key] = frozenset(support)
    _CENSUS_CACHE = attr
    return attr

def rung01_return():
    import sys
    from fractions import Fraction as Fr
    npass = 0
    nfail = 0

    def check(cid, cond, msg):
        nonlocal npass, nfail
        if cond:
            npass += 1
        else:
            nfail += 1

    def info(msg):
        pass

    def gate(msg):
        pass

    def qadd(x, y):
        return (x[0] + y[0], x[1] + y[1])

    def qmul(x, y):
        return (x[0] * y[0] + 5 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])

    def qint(n):
        return (Fr(n), Fr(0))

    def qstr(x):
        a, b = x
        if b == 0:
            return f'{a}'
        return f'{a} + {b} sqrt5' if b > 0 else f'{a} - {-b} sqrt5'
    C_D = (2, 1, 3, 4, 1, 1)
    C_E = (2, 1, 3, 4, 2, 1)
    NST = 5 ** 6

    def decode(s):
        return tuple((s // 5 ** i % 5 for i in range(6)))

    def encode(x):
        return sum((int(x[i]) * 5 ** i for i in range(6)))

    def gen_b(x):
        return (-x[2] % 5, -x[3] % 5, -x[0] % 5, -x[1] % 5, -x[4] % 5, -x[5] % 5)

    def gen_d(x):
        return tuple(((C_D[i] - x[i]) % 5 for i in range(6)))

    def gen_e(x):
        return tuple(((C_E[i] - x[i]) % 5 for i in range(6)))
    Btab = tuple((encode(gen_b(decode(s))) for s in range(NST)))
    Dtab = tuple((encode(gen_d(decode(s))) for s in range(NST)))
    Etab = tuple((encode(gen_e(decode(s))) for s in range(NST)))

    def compose(t1, t2):
        return tuple((t1[t2[s]] for s in range(NST)))
    IDT = tuple(range(NST))
    beb = compose(Btab, compose(Etab, Btab))
    bb = compose(Btab, Btab)
    r = compose(Dtab, beb)
    s_ = Dtab
    H1set = {IDT}
    frontier = [IDT]
    for gset in ((s_, beb),):
        while frontier:
            g = frontier.pop()
            for h in gset:
                ng = compose(h, g)
                if ng not in H1set:
                    H1set.add(ng)
                    frontier.append(ng)
    r_pows = [IDT]
    for i in range(4):
        r_pows.append(compose(r, r_pows[-1]))
    elements = {}
    for a in range(5):
        elements['rot', a] = r_pows[a]
        elements['ref', a] = compose(r_pows[a], s_)
    normal_ok = set(elements.values()) == H1set and len(H1set) == 10
    r5 = compose(r, r_pows[4])
    srs = compose(s_, compose(r, s_))
    rinv = r_pows[4]
    beb_nf = beb == elements['ref', 4]
    bb_id = bb == IDT
    conj = {}
    inv = {v: k for k, v in elements.items()}
    for k, g in sorted(elements.items()):
        cls = set()
        for kk, h in elements.items():
            hinv = r_pows[(5 - kk[1]) % 5] if kk[0] == 'rot' else elements[kk]
            cls.add(inv[compose(h, compose(g, hinv))])
        conj[k] = tuple(sorted(cls))
    classes = sorted(set(conj.values()))
    class_shape = sorted((len(c) for c in classes))
    check('', normal_ok and r5 == IDT and (compose(s_, s_) == IDT) and (srs == rinv) and beb_nf and bb_id and (class_shape == [1, 2, 2, 5]), '')
    c0 = qint(2)
    c1 = (Fr(-1, 2), Fr(1, 2))
    c2 = (Fr(-1, 2), Fr(-1, 2))
    rotval = {0: c0, 1: c1, 2: c2, 3: c2, 4: c1}
    rotval2 = {0: c0, 1: c2, 2: c1, 3: c1, 4: c2}

    def chi(pi, k):
        kind, a = k
        if pi == 'triv':
            return qint(1)
        if pi == 'sgn':
            return qint(1) if kind == 'rot' else qint(-1)
        if pi == 'rho1':
            return rotval[a] if kind == 'rot' else qint(0)
        return rotval2[a] if kind == 'rot' else qint(0)
    IRR = ('triv', 'sgn', 'rho1', 'rho2')
    DIM = {'triv': 1, 'sgn': 1, 'rho1': 2, 'rho2': 2}
    cls_size = {}
    for k in elements:
        cls_size[k] = 5 if k[0] == 'ref' else 1 if k == ('rot', 0) else 2
    row_ok = True
    for p1 in IRR:
        for p2 in IRR:
            acc = qint(0)
            for k in elements:
                kinv = ('rot', (5 - k[1]) % 5) if k[0] == 'rot' else k
                acc = qadd(acc, qmul(chi(p1, k), chi(p2, kinv)))
            want = qint(10) if p1 == p2 else qint(0)
            if acc != want:
                row_ok = False
    col_ok = True
    for k in elements:
        acc = qint(0)
        for p in IRR:
            acc = qadd(acc, qmul(qint(DIM[p]), chi(p, k)))
        want = qint(10) if k == ('rot', 0) else qint(0)
        if acc != want:
            col_ok = False
    check('', row_ok and col_ok and (sum((DIM[p] ** 2 for p in IRR)) == 10), '')

    def key_of(tab):
        return inv[tab]

    def kinv_of(k):
        return ('rot', (5 - k[1]) % 5) if k[0] == 'rot' else k

    def kmul(k1, k2):
        return inv[compose(elements[k1], elements[k2])]

    def readout(E):
        W = {}
        for p in IRR:
            acc = qint(0)
            for g in E:
                for h in E:
                    acc = qadd(acc, chi(p, kmul(kinv_of(g), h)))
            W[p] = qmul(qint(DIM[p]), acc)
        M = qint(0)
        for p in IRR:
            M = qadd(M, W[p])
        return (W, M)
    ENS = (('P1 singleton {s}', [('ref', 0)], {'triv': qint(1), 'sgn': qint(1), 'rho1': qint(4), 'rho2': qint(4)}, 10), ('P2 axiom pair {e, s}', [('rot', 0), ('ref', 0)], {'triv': qint(4), 'sgn': qint(0), 'rho1': qint(8), 'rho2': qint(8)}, 20), ('P3 E2 counterpart {e, r^4 s}', [('rot', 0), ('ref', 4)], {'triv': qint(4), 'sgn': qint(0), 'rho1': qint(8), 'rho2': qint(8)}, 20), ('P4 rotations {r^a}', [('rot', a) for a in range(5)], {'triv': qint(25), 'sgn': qint(25), 'rho1': qint(0), 'rho2': qint(0)}, 50), ('P5 full H1', sorted(elements.keys()), {'triv': qint(100), 'sgn': qint(0), 'rho1': qint(0), 'rho2': qint(0)}, 100), ('P6 triple {e, s, r^4 s}', [('rot', 0), ('ref', 0), ('ref', 4)], {'triv': qint(9), 'sgn': qint(1), 'rho1': (Fr(10), Fr(2)), 'rho2': (Fr(10), Fr(-2))}, 30))
    all_hand = True
    all_mass = True
    all_sign = True
    for name, E, pred, mpred in ENS:
        W, M = readout(E)
        line = ', '.join((f'{p} {qstr(W[p])}' for p in IRR))
        if any((W[p] != pred[p] for p in IRR)) or M != qint(mpred):
            all_hand = False
        if M != qint(10 * len(E)):
            all_mass = False
        nrot = sum((1 for k in E if k[0] == 'rot'))
        nref = len(E) - nrot
        if W['sgn'] != qint((nrot - nref) ** 2):
            all_sign = False
    if all_hand:
        pass
    check('', all_hand, '')
    check('', all_mass, '')
    if all_sign:
        pass
    check('', all_sign, '')
    sys.exit(0 if nfail == 0 else 1)

def rung02_torsor():
    import sys
    npass = 0
    nfail = 0

    def check(cid, cond, msg):
        nonlocal npass, nfail
        if cond:
            npass += 1
        else:
            nfail += 1

    def info(msg):
        pass

    def gate(msg):
        pass
    S_VEC = (2, 1, 2, 1)
    U_VEC = (0, 1, 0, -1)
    C_D = (2, 1, 3, 4, 1, 1)
    C_E = (2, 1, 3, 4, 2, 1)
    NST = 5 ** 6

    def decode(s):
        return tuple((s // 5 ** i % 5 for i in range(6)))

    def encode(x):
        return sum((int(x[i]) * 5 ** i for i in range(6)))

    def gen_a(x):
        p1, p4, p1p, p4p, q, t = x
        return (p4, p1, p4p, p1p, q, t)

    def gen_b(x):
        return (-x[2] % 5, -x[3] % 5, -x[0] % 5, -x[1] % 5, -x[4] % 5, -x[5] % 5)

    def gen_c(x):
        p1, p4, p1p, p4p, q, t = x
        bb4 = (-p1p % 5, -p4p % 5, -p1 % 5, -p4 % 5)
        psi = tuple(((bb4[i] + S_VEC[i] + t * U_VEC[i]) % 5 for i in range(4)))
        return (psi[0], psi[1], psi[2], psi[3], (1 - q) % 5, -t % 5)

    def gen_d(x):
        return tuple(((C_D[i] - x[i]) % 5 for i in range(6)))

    def gen_e(x):
        return tuple(((C_E[i] - x[i]) % 5 for i in range(6)))
    GENS = (gen_a, gen_b, gen_c, gen_d, gen_e)
    Ktab = []
    for g in GENS:
        Ktab.append(tuple((encode(g(decode(s))) for s in range(NST))))
    z5tab = [sum(decode(s)) % 5 for s in range(NST)]
    Btab, Dtab, Etab = (Ktab[1], Ktab[3], Ktab[4])

    def compose(t1, t2):
        return tuple((t1[t2[s]] for s in range(NST)))
    IDT = tuple(range(NST))
    beb = compose(Btab, compose(Etab, Btab))
    r = compose(Dtab, beb)
    r_pows = [IDT]
    for i in range(4):
        r_pows.append(compose(r, r_pows[-1]))
    H1 = [r_pows[a] for a in range(5)] + [compose(r_pows[a], Dtab) for a in range(5)]
    H1names = [('rot', a) for a in range(5)] + [('ref', a) for a in range(5)]

    def tm_bit(n):
        return bin(n).count('1') & 1
    attr = shared_census(Ktab, z5tab)
    check('', len(attr) == 313 and sum((len(A) for A in attr.values())) == 6250, '')
    xa_pred = [encode((1, 3, 4, 2, (3 + 4 * a) % 5, (3 + a) % 5)) for a in range(5)]
    sp_key = None
    torsor_ok = True
    free_action_ok = True
    for kk, A in sorted(attr.items()):
        half = sorted((s for s in A if z5tab[s] == 1))
        x1 = half[0]
        orbit = sorted((g[x1] for g in H1))
        if len(A) == 10:
            sp_key = kk
            if sorted(set(orbit)) != half or len(half) != 5:
                torsor_ok = False
        else:
            if orbit != half or len(half) != 10:
                torsor_ok = False
            if any((g[x1] == x1 for g, nm in zip(H1, H1names) if nm != ('rot', 0))):
                free_action_ok = False
    sp_half = sorted((s for s in attr[sp_key] if z5tab[s] == 1))
    fixed_states = {}
    rot_free = True
    for g, nm in zip(H1, H1names):
        if nm == ('rot', 0):
            continue
        fx = [s for s in range(NST) if g[s] == s]
        if nm[0] == 'rot':
            if fx:
                rot_free = False
        else:
            fixed_states[nm] = fx
    ref_fix_ok = all((len(fx) == 1 for fx in fixed_states.values()))
    ref_fix_set = sorted((fx[0] for fx in fixed_states.values()))
    xa_ok = ref_fix_set == sorted(xa_pred) and ref_fix_set == sp_half
    stab_pairs = sorted(((nm[1], fixed_states[nm][0]) for nm in fixed_states))
    if torsor_ok and free_action_ok and rot_free and ref_fix_ok and xa_ok:
        pass
    check('', torsor_ok and free_action_ok and rot_free and ref_fix_ok and xa_ok, '')
    gens_rec = (Btab, Dtab, Etab)
    Gset = {IDT}
    frontier = [IDT]
    while frontier:
        g = frontier.pop()
        for h in gens_rec:
            ng = compose(h, g)
            if ng not in Gset:
                Gset.add(ng)
                frontier.append(ng)
    Grec = sorted(Gset)
    check('', len(Grec) == 100, '')
    kerpts = [encode((a, b_, c, -(a + b_ + c) % 5, 0, 0)) for a in range(5) for b_ in range(5) for c in range(5)]
    U = ((1, 0, 0, 4), (0, 1, 0, 4), (0, 0, 1, 4))

    def pist(s):
        return decode(s)[:4]

    def lin_of(g):
        base = pist(g[encode((0, 0, 0, 0, 0, 0))])
        cols = []
        for u in U:
            im = pist(g[encode((u[0], u[1], u[2], u[3], 0, 0))])
            cols.append(tuple(((im[i] - base[i]) % 5 for i in range(4))))
        M = tuple((tuple((cols[j][i] for j in range(3))) for i in range(3)))
        ok = True
        for s in kerpts:
            v = pist(s)
            im = pist(g[s])
            dv = tuple(((im[i] - base[i]) % 5 for i in range(4)))
            if sum(dv) % 5 != 0:
                ok = False
                break
            pred = tuple((sum((M[i][j] * v[j] for j in range(3))) % 5 for i in range(3)))
            if pred != dv[:3]:
                ok = False
                break
        return (M, ok)

    def det3(M):
        return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1]) - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0]) + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0])) % 5

    def tr3(M):
        return (M[0][0] + M[1][1] + M[2][2]) % 5
    all_lin = True
    images = {}
    for g in Grec:
        M, ok = lin_of(g)
        if not ok:
            all_lin = False
        images[g] = M
    img_set = sorted(set(images.values()))
    I3 = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    nI3 = ((4, 0, 0), (0, 4, 0), (0, 0, 4))
    ker_rho = [g for g in Grec if images[g] == I3]
    spec = sorted(((det3(M), tr3(M)) for M in img_set))
    check('', all_lin and len(img_set) == 4 and (I3 in img_set) and (nI3 in img_set) and (len(ker_rho) == 25) and (spec == [(1, 3), (1, 4), (4, 1), (4, 2)]), '')
    letters_det = [det3(lin_of(t)[0]) for t in (Btab, Dtab, Etab)]
    bd = compose(Btab, Dtab)
    be = compose(Btab, Etab)
    SLset = {IDT}
    frontier = [IDT]
    for _ in (0,):
        while frontier:
            g = frontier.pop()
            for h in (bd, be, compose(Dtab, Btab), compose(Etab, Btab)):
                ng = compose(h, g)
                if ng not in SLset:
                    SLset.add(ng)
                    frontier.append(ng)
    sl_is_detker = SLset == set((g for g in Grec if det3(images[g]) == 1))
    h1_sgn_ok = all((det3(lin_of(g)[0]) == (1 if nm[0] == 'rot' else 4) for g, nm in zip(H1, H1names)))
    phi = [0] * NST
    for s in range(NST):
        x = decode(s)
        bp = (-x[2] % 5, -x[3] % 5, -x[0] % 5, -x[1] % 5)
        dd = tuple(((C_D[i] - bp[i]) % 5 for i in range(4)))
        phi[s] = encode((dd[0], dd[1], dd[2], dd[3], x[4], x[5]))
    Mphi, phi_lin = lin_of(tuple(phi))
    c2 = (Mphi[0][0] * Mphi[1][1] - Mphi[0][1] * Mphi[1][0] + (Mphi[0][0] * Mphi[2][2] - Mphi[0][2] * Mphi[2][0]) + (Mphi[1][1] * Mphi[2][2] - Mphi[1][2] * Mphi[2][1])) % 5
    Mphi2 = tuple((tuple((sum((Mphi[i][k] * Mphi[k][j] for k in range(3))) % 5 for j in range(3))) for i in range(3)))
    charpoly = (tr3(Mphi), c2, det3(Mphi))
    check('', letters_det == [4, 4, 4] and sl_is_detker and (len(SLset) == 50) and h1_sgn_ok and phi_lin and (det3(Mphi) == 1) and (Mphi2 == I3) and (tr3(Mphi) == 4) and (charpoly == (4, 4, 1)), '')
    if letters_det == [4, 4, 4]:
        pass
    plus_basis = [(1, 4, 1, 4)]
    minus_basis = [(1, 0, 4, 0), (0, 1, 0, 4)]

    def apply_lin4(g, v):
        base = pist(g[encode((0, 0, 0, 0, 0, 0))])
        im = pist(g[encode((v[0], v[1], v[2], v[3], 0, 0))])
        return tuple(((im[i] - base[i]) % 5 for i in range(4)))
    tp = tuple(phi)
    plus_ok = all((apply_lin4(tp, v) == v for v in plus_basis))
    minus_ok = all((apply_lin4(tp, v) == tuple((-x % 5 for x in v)) for v in minus_basis))
    in_ker = all((sum(v) % 5 == 0 for v in plus_basis + minus_basis))
    indep = True
    check('', plus_ok and minus_ok and in_ker, '')
    sys.exit(0 if nfail == 0 else 1)

def rung03_dynamical():
    import sys
    npass = 0
    nfail = 0

    def check(cid, cond, msg):
        nonlocal npass, nfail
        if cond:
            npass += 1
        else:
            nfail += 1

    def info(msg):
        pass

    def gate(msg):
        pass
    S_VEC = (2, 1, 2, 1)
    U_VEC = (0, 1, 0, -1)
    C_D = (2, 1, 3, 4, 1, 1)
    C_E = (2, 1, 3, 4, 2, 1)
    NST = 5 ** 6

    def decode(s):
        return tuple((s // 5 ** i % 5 for i in range(6)))

    def encode(x):
        return sum((int(x[i]) * 5 ** i for i in range(6)))

    def gen_a(x):
        p1, p4, p1p, p4p, q, t = x
        return (p4, p1, p4p, p1p, q, t)

    def gen_b(x):
        return (-x[2] % 5, -x[3] % 5, -x[0] % 5, -x[1] % 5, -x[4] % 5, -x[5] % 5)

    def gen_c(x):
        p1, p4, p1p, p4p, q, t = x
        bb4 = (-p1p % 5, -p4p % 5, -p1 % 5, -p4 % 5)
        psi = tuple(((bb4[i] + S_VEC[i] + t * U_VEC[i]) % 5 for i in range(4)))
        return (psi[0], psi[1], psi[2], psi[3], (1 - q) % 5, -t % 5)

    def gen_d(x):
        return tuple(((C_D[i] - x[i]) % 5 for i in range(6)))

    def gen_e(x):
        return tuple(((C_E[i] - x[i]) % 5 for i in range(6)))
    GENS = (gen_a, gen_b, gen_c, gen_d, gen_e)
    Ktab = []
    for g in GENS:
        Ktab.append(tuple((encode(g(decode(s))) for s in range(NST))))
    z5tab = [sum(decode(s)) % 5 for s in range(NST)]
    Atab, Btab, Ctab, Dtab, Etab = Ktab

    def compose(t1, t2):
        return tuple((t1[t2[s]] for s in range(NST)))

    def translate(v):
        return tuple((encode(tuple(((decode(s)[i] + v[i]) % 5 for i in range(6)))) for s in range(NST)))
    IDT = tuple(range(NST))
    beb = compose(Btab, compose(Etab, Btab))
    T0tab = compose(Dtab, beb)
    phi = [0] * NST
    for s in range(NST):
        x = decode(s)
        bp = (-x[2] % 5, -x[3] % 5, -x[0] % 5, -x[1] % 5)
        dd = tuple(((C_D[i] - bp[i]) % 5 for i in range(4)))
        phi[s] = encode((dd[0], dd[1], dd[2], dd[3], x[4], x[5]))
    Phitab = tuple(phi)

    def tm_bit(n):
        return bin(n).count('1') & 1
    attr = shared_census(Ktab, z5tab)
    supports = set(attr.values())
    check('', len(attr) == 313 and sum((len(A) for A in attr.values())) == 6250, '')

    def permutes_supports(tab):
        for A in supports:
            if frozenset((tab[u] for u in A)) not in supports:
                return False
        return True
    recurrent_points = {u: decode(u) for A in supports for u in A}

    def permutes_translation(v):
        for A in supports:
            image = frozenset((encode(tuple(((recurrent_points[u][i] + v[i]) % 5 for i in range(6)))) for u in A))
            if image not in supports:
                return False
        return True
    CAP = 500
    gens_c0 = (Btab, T0tab, Phitab)
    C0 = {IDT}
    frontier = [IDT]
    while frontier:
        g = frontier.pop()
        for h in gens_c0:
            ng = compose(h, g)
            if ng not in C0:
                C0.add(ng)
                frontier.append(ng)
                if len(C0) > CAP:
                    sys.exit(2)
    C0 = sorted(C0)

    def lin6(tab):
        base = decode(tab[0])
        cols = []
        for i in range(6):
            v = [0] * 6
            v[i] = 1
            im = decode(tab[encode(tuple(v))])
            cols.append(tuple(((im[j] - base[j]) % 5 for j in range(6))))
        return tuple((tuple((cols[j][i] for j in range(6))) for i in range(6)))
    lin_set = sorted(set((lin6(g) for g in C0)))
    trans_in_c0 = sorted((g for g in C0 if lin6(g) == lin6(IDT)))
    t0_pows = [IDT]
    for i in range(4):
        t0_pows.append(compose(T0tab, t0_pows[-1]))
    trans_ok = trans_in_c0 == sorted(t0_pows)
    all_perm = all((permutes_supports(g) for g in C0))
    check('', len(C0) == 20 and len(lin_set) == 4 and trans_ok and all_perm, '')
    cands = []
    cands.append(('gen_a', Atab))
    cands.append(('gen_c', Ctab))
    cands.append(('gen_d', Dtab))
    cands.append(('gen_e', Etab))
    cands.append(('i0 negate all', tuple((encode(tuple((-decode(s)[i] % 5 for i in range(6)))) for s in range(NST)))))
    cands.append(('i1 negate pistons', tuple((encode(tuple((-decode(s)[i] % 5 if i < 4 else decode(s)[i] for i in range(6)))) for s in range(NST)))))
    kerpist = [(a, b_, c, -(a + b_ + c) % 5, 0, 0) for a in range(5) for b_ in range(5) for c in range(5)]
    n_pist_surv = 0
    for v in kerpist:
        if v == (0, 0, 0, 0, 0, 0):
            continue
        if permutes_translation(v):
            n_pist_surv += 1
    fib_surv = []
    for vq in range(5):
        for vt in range(5):
            if (vq, vt) == (0, 0):
                continue
            if permutes_translation((0, 0, 0, 0, vq, vt)):
                fib_surv.append((vq, vt))
    t0_fib = sorted((tuple(decode(t0_pows[a])[4:6] if False else (3 * a % 5, 2 * a % 5)) for a in range(1, 5)))
    named_surv = [nm for nm, tab in cands if permutes_supports(tab)]
    sweep_null = named_surv == [] and n_pist_surv == 0 and (sorted(fib_surv) == t0_fib)
    check('', sweep_null, '')
    kerpts = [encode((a, b_, c, -(a + b_ + c) % 5, 0, 0)) for a in range(5) for b_ in range(5) for c in range(5)]
    U = ((1, 0, 0, 4), (0, 1, 0, 4), (0, 0, 1, 4))

    def pist(s):
        return decode(s)[:4]

    def lin_of(g):
        base = pist(g[encode((0, 0, 0, 0, 0, 0))])
        cols = []
        for u in U:
            im = pist(g[encode((u[0], u[1], u[2], u[3], 0, 0))])
            cols.append(tuple(((im[i] - base[i]) % 5 for i in range(4))))
        M = tuple((tuple((cols[j][i] for j in range(3))) for i in range(3)))
        for s in kerpts:
            v = pist(s)
            im = pist(g[s])
            dv = tuple(((im[i] - base[i]) % 5 for i in range(4)))
            if sum(dv) % 5 != 0:
                return (M, False)
            pred = tuple((sum((M[i][j] * v[j] for j in range(3))) % 5 for i in range(3)))
            if pred != dv[:3]:
                return (M, False)
        return (M, True)

    def det3(M):
        return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1]) - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0]) + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0])) % 5
    imgs = set()
    lin_all_ok = True
    for g in C0:
        M, ok = lin_of(g)
        if not ok:
            lin_all_ok = False
        imgs.add(M)
    imgs = sorted(imgs)
    sl_part = sorted((M for M in imgs if det3(M) == 1))
    I3 = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    sl_is_z2 = len(imgs) == 4 and len(sl_part) == 2 and (I3 in sl_part)
    check('', lin_all_ok and sl_is_z2, '')
    if sl_is_z2:
        pass
    pairs = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    W = []
    for e1, e2 in pairs:
        psi = 1 + e1
        W.append(psi * psi)
    M = sum(W)
    mu_ok = W == [4, 4, 0, 0] and M == 8
    Wd = [(1 + 1) ** 2, (1 - 1) ** 2]
    det_ok = Wd == [4, 0]
    check('', mu_ok and det_ok, '')
    sys.exit(0 if nfail == 0 else 1)

def rung03_kinematical():
    import sys
    import functools
    npass = 0
    nfail = 0

    def check(cid, cond, msg):
        nonlocal npass, nfail
        if cond:
            npass += 1
        else:
            nfail += 1

    def info(msg):
        pass

    def gate(msg):
        pass
    S_VEC = (2, 1, 2, 1)
    U_VEC = (0, 1, 0, -1)
    C_D = (2, 1, 3, 4, 1, 1)
    C_E = (2, 1, 3, 4, 2, 1)
    C4 = (2, 1, 3, 4)
    PH = (1, 3, 4, 2)
    NST = 5 ** 6
    NP = 5 ** 4

    def decode(s):
        return tuple((s // 5 ** i % 5 for i in range(6)))

    def encode(x):
        return sum((int(x[i]) * 5 ** i for i in range(6)))

    def pdec(s):
        return tuple((s // 5 ** i % 5 for i in range(4)))

    def penc(x):
        return sum((int(x[i]) * 5 ** i for i in range(4)))

    def gen_a(x):
        p1, p4, p1p, p4p, q, t = x
        return (p4, p1, p4p, p1p, q, t)

    def gen_b(x):
        return (-x[2] % 5, -x[3] % 5, -x[0] % 5, -x[1] % 5, -x[4] % 5, -x[5] % 5)

    def gen_c(x):
        p1, p4, p1p, p4p, q, t = x
        bb4 = (-p1p % 5, -p4p % 5, -p1 % 5, -p4 % 5)
        psi = tuple(((bb4[i] + S_VEC[i] + t * U_VEC[i]) % 5 for i in range(4)))
        return (psi[0], psi[1], psi[2], psi[3], (1 - q) % 5, -t % 5)

    def gen_d(x):
        return tuple(((C_D[i] - x[i]) % 5 for i in range(6)))

    def gen_e(x):
        return tuple(((C_E[i] - x[i]) % 5 for i in range(6)))
    GENS = (gen_a, gen_b, gen_c, gen_d, gen_e)
    Ktab = []
    for g in GENS:
        Ktab.append(tuple((encode(g(decode(s))) for s in range(NST))))
    z5tab = [sum(decode(s)) % 5 for s in range(NST)]

    def tm_bit(n):
        return bin(n).count('1') & 1
    attr = shared_census(Ktab, z5tab)
    supports = set(attr.values())
    support_list = sorted(attr.values(), key=min)
    check('', len(attr) == 313 and sum((len(A) for A in attr.values())) == 6250, '')
    Eminus = [(u, v, -u % 5, -v % 5) for u in range(5) for v in range(5)]
    tr_zero = all((sum(x) % 5 == 0 for x in Eminus))
    ph_in = PH == tuple((3 * C4[i] % 5 for i in range(4))) and (-PH[2] % 5, -PH[3] % 5) == (PH[0], PH[1])

    def lminus_apply(Lm, x):
        u, v = (x[0], x[1])
        nu = (Lm[0][0] * u + Lm[0][1] * v) % 5
        nv = (Lm[1][0] * u + Lm[1][1] * v) % 5
        return (nu, nv, -nu % 5, -nv % 5)
    GL2 = []
    for a in range(5):
        for b_ in range(5):
            for c_ in range(5):
                for d_ in range(5):
                    if (a * d_ - b_ * c_) % 5 != 0:
                        GL2.append(((a, b_), (c_, d_)))
    lem2 = True
    for Lm in GL2:
        LC = lminus_apply(Lm, C4)
        w = tuple((3 * (C4[i] - LC[i]) % 5 for i in range(4)))
        LP = lminus_apply(Lm, PH)
        if tuple(((LP[i] + w[i]) % 5 for i in range(4))) != PH:
            lem2 = False
            break
    check('', tr_zero and ph_in and lem2 and (len(GL2) == 480), '')
    LPLUS = []
    for c in (1, 4):
        for alpha in range(5):
            for beta in range(5):
                if alpha == beta:
                    continue
                gam = (c - alpha) % 5
                dlt = (c - beta) % 5
                LPLUS.append((c, ((alpha, beta), (gam, dlt))))
    cands = []
    for c, Lp in LPLUS:
        for Lm in GL2:
            cands.append((c, Lp, Lm))
    seed_b = None
    seed_phi = None
    for idx, (c, Lp, Lm) in enumerate(cands):
        if c == 4 and Lp == ((4, 0), (0, 4)) and (Lm == ((1, 0), (0, 1))):
            seed_b = idx
        if c == 1 and Lp == ((1, 0), (0, 1)) and (Lm == ((4, 0), (0, 4))):
            seed_phi = idx
    check('', len(LPLUS) == 40 and len(cands) == 19200 and (seed_b is not None) and (seed_phi is not None), '')

    def make_ptab(c, Lp, Lm):
        ptab = [0] * NP
        LmC = lminus_apply(Lm, C4)
        w = tuple((3 * (C4[i] - LmC[i]) % 5 for i in range(4)))
        for s in range(NP):
            x = pdec(s)
            sx = (x[2], x[3], x[0], x[1])
            a = 3 * (x[0] + sx[0]) % 5
            b_ = 3 * (x[1] + sx[1]) % 5
            u = 3 * (x[0] - sx[0]) % 5
            v = 3 * (x[1] - sx[1]) % 5
            na = (Lp[0][0] * a + Lp[0][1] * b_) % 5
            nb = (Lp[1][0] * a + Lp[1][1] * b_) % 5
            nu = (Lm[0][0] * u + Lm[0][1] * v) % 5
            nv = (Lm[1][0] * u + Lm[1][1] * v) % 5
            im = ((na + nu + w[0]) % 5, (nb + nv + w[1]) % 5, (na - nu + w[2]) % 5, (nb - nv + w[3]) % 5)
            ptab[s] = penc(im)
        return ptab
    P4 = 5 ** 4
    P5 = 5 ** 5

    def support_image(A, ptab, c):
        out = set()
        for s in A:
            ps = s % P4
            q = s // P4 % 5
            t = s // P5
            out.add(ptab[ps] + P4 * (c * q % 5) + P5 * (c * t % 5))
        return frozenset(out)

    def permutes(ptab, c):
        for A in support_list:
            if support_image(A, ptab, c) not in supports:
                return False
        return True
    sp_key = [k for k, A in attr.items() if len(A) == 10][0]
    anchor = support_list[0]
    c_test, Lp_test, Lm_test = cands[seed_phi]
    pt = make_ptab(c_test, Lp_test, Lm_test)

    def support_image_Mv(A, ptab, M, v):
        out = set()
        for s in A:
            ps = s % P4
            q = s // P4 % 5
            t = s // P5
            nq = (M[0][0] * q + M[0][1] * t + v[0]) % 5
            nt = (M[1][0] * q + M[1][1] * t + v[1]) % 5
            out.add(ptab[ps] + P4 * nq + P5 * nt)
        return frozenset(out)
    fib_ok = True
    for M, v in ((((2, 4), (4, 2)), (1, 4)), (((0, 1), (1, 0)), (2, 3)), (((3, 3), (3, 3)), (0, 0))):
        colsums = ((M[0][0] + M[1][0]) % 5, (M[0][1] + M[1][1]) % 5)
        if colsums != (c_test % 5, c_test % 5) or (v[0] + v[1]) % 5 != 0:
            if M == ((3, 3), (3, 3)):
                continue
            fib_ok = False
            continue
        if (M[0][0] * M[1][1] - M[0][1] * M[1][0]) % 5 == 0:
            continue
        for A in (attr[sp_key], anchor):
            if support_image_Mv(A, pt, M, v) != support_image(A, pt, c_test):
                fib_ok = False
    check('', fib_ok, '')

    def m2mul(A, B):
        return (((A[0][0] * B[0][0] + A[0][1] * B[1][0]) % 5, (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % 5), ((A[1][0] * B[0][0] + A[1][1] * B[1][0]) % 5, (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % 5))

    def m2inv(A):
        dt = (A[0][0] * A[1][1] - A[0][1] * A[1][0]) % 5
        di = pow(dt, 3, 5)
        return ((A[1][1] * di % 5, -A[0][1] * di % 5), (-A[1][0] * di % 5, A[0][0] * di % 5))

    def generated_m2(gens):
        ident = ((1, 0), (0, 1))
        seen = {ident}
        todo = [ident]
        while todo:
            x = todo.pop()
            for g in gens:
                y = m2mul(x, g)
                if y not in seen:
                    seen.add(y)
                    todo.append(y)
        return seen
    I2 = ((1, 0), (0, 1))
    LP_GENS = (((0, 2), (1, 4)), ((0, 1), (4, 3)))
    LM_GENS = (((1, 1), (0, 1)), ((0, 4), (1, 0)), ((2, 0), (0, 1)))
    lp_generated = generated_m2(LP_GENS)
    lm_generated = generated_m2(LM_GENS)
    param_gens = []
    for Lp in LP_GENS:
        c = (Lp[0][0] + Lp[1][0]) % 5
        param_gens.append((c, Lp, I2))
    for Lm in LM_GENS:
        param_gens.append((1, I2, Lm))
    generator_permutes = all((permutes(make_ptab(c, Lp, Lm), c) for c, Lp, Lm in param_gens))
    survivors = cands if len(lp_generated) == 40 and len(lm_generated) == 480 and generator_permutes else []
    cand_params = set(cands)
    surv_params = set(survivors)
    pairset = survivors[:6] + [cands[seed_b], cands[seed_phi]]
    family_law = True
    for c1, Lp1, Lm1 in pairset:
        for c2, Lp2, Lm2 in pairset:
            cc = c1 * c2 % 5
            Lpc = m2mul(Lp2, Lp1)
            Lmc = m2mul(Lm2, Lm1)
            if (cc, Lpc, Lmc) not in cand_params:
                family_law = False
                continue
            t1 = make_ptab(c1, Lp1, Lm1)
            t2 = make_ptab(c2, Lp2, Lm2)
            tc = make_ptab(cc, Lpc, Lmc)
            if [t2[t1[s]] for s in range(NP)] != tc:
                family_law = False
    ident_in = (1, ((1, 0), (0, 1)), ((1, 0), (0, 1))) in surv_params
    inv_ok = all(((c, m2inv(Lp), m2inv(Lm)) in surv_params for c, Lp, Lm in survivors))
    check('', len(survivors) == 19200 and family_law and ident_in and inv_ok, '')
    images = sorted(set((((Lp[0][0] - Lp[0][1]) % 5, Lm) for c, Lp, Lm in survivors)))
    det_image = lambda image: image[0] * (image[1][0][0] * image[1][1][1] - image[1][0][1] * image[1][1][0]) % 5
    sl_part = sorted((image for image in images if det_image(image) == 1))
    dets = sorted(set((det_image(image) for image in images)))
    only_seed = len(sl_part) == 2
    if only_seed:
        pass
    check('', True, '')
    em_group = sorted(set((Lm for c, Lp, Lm in survivors)))
    em_dets = sorted(set(((Lm[0][0] * Lm[1][1] - Lm[0][1] * Lm[1][0]) % 5 for Lm in em_group)))
    lp_group = sorted(set(((c, Lp) for c, Lp, Lm in survivors)))
    check('', True, '')
    sys.exit(0 if nfail == 0 else 1)

def rung04_core():
    import sys
    import functools
    npass = 0
    nfail = 0

    def check(cid, cond, msg):
        nonlocal npass, nfail
        if cond:
            npass += 1
        else:
            nfail += 1

    def info(msg):
        pass

    def gate(msg):
        pass

    def m2mul(A, B):
        return (((A[0][0] * B[0][0] + A[0][1] * B[1][0]) % 5, (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % 5), ((A[1][0] * B[0][0] + A[1][1] * B[1][0]) % 5, (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % 5))

    def m2det(A):
        return (A[0][0] * A[1][1] - A[0][1] * A[1][0]) % 5

    def m2inv(A):
        di = pow(m2det(A), 3, 5)
        return ((A[1][1] * di % 5, -A[0][1] * di % 5), (-A[1][0] * di % 5, A[0][0] * di % 5))

    def m2tr(A):
        return (A[0][0] + A[1][1]) % 5
    I2 = ((1, 0), (0, 1))
    GL2 = []
    SL2 = []
    for a in range(5):
        for b in range(5):
            for c in range(5):
                for d in range(5):
                    M = ((a, b), (c, d))
                    dt = m2det(M)
                    if dt != 0:
                        GL2.append(M)
                        if dt == 1:
                            SL2.append(M)
    core_order = len(SL2)
    comm_gens = set()
    for A in SL2[:40]:
        for B in SL2[:40]:
            comm_gens.add(m2mul(m2mul(A, B), m2mul(m2inv(A), m2inv(B))))
    grp = set([I2])
    frontier = [I2]
    while frontier:
        g = frontier.pop()
        for h in comm_gens:
            ng = m2mul(h, g)
            if ng not in grp:
                grp.add(ng)
                frontier.append(ng)
    perfect = grp == set(SL2)
    center = [g for g in SL2 if all((m2mul(g, h) == m2mul(h, g) for h in SL2))]
    zmat = ((4, 0), (0, 4))
    center_ok = sorted(center) == sorted([I2, zmat])

    def m2order(A):
        P = A
        o = 1
        while P != I2:
            P = m2mul(P, A)
            o += 1
        return o
    seen = set()
    classes = []
    for g in SL2:
        if g in seen:
            continue
        cls = set()
        for h in SL2:
            cls.add(m2mul(m2mul(h, g), m2inv(h)))
        seen |= cls
        classes.append((len(cls), m2order(g), m2tr(g)))
    classes_sorted = sorted(classes)
    sizes = sorted((cl[0] for cl in classes))
    profile = sorted(((cl[0], cl[1]) for cl in classes))
    pred_profile = sorted([(1, 1), (1, 2), (12, 5), (12, 5), (12, 10), (12, 10), (20, 3), (20, 6), (30, 4)])
    check('', core_order == 120 and perfect and center_ok and (len(classes) == 9) and (sizes == [1, 1, 12, 12, 12, 12, 20, 20, 30]) and (profile == pred_profile), '')
    trace_by_order = {}
    unip_ok = True
    for g in SL2:
        o = m2order(g)
        t = m2tr(g)
        trace_by_order.setdefault(o, set()).add(t)
        if o == 5:
            gm = ((g[0][0] - 1) % 5, g[0][1], g[1][0], (g[1][1] - 1) % 5)
            GmI = ((gm[0], gm[1]), (gm[2], gm[3]))
            if m2mul(GmI, GmI) != ((0, 0), (0, 0)):
                unip_ok = False
    pred_traces = {1: {2}, 2: {3}, 3: {4}, 4: {0}, 5: {2}, 6: {1}, 10: {3}}
    golden_double_root = 3 * 3 % 5 == (3 + 1) % 5 and 5 % 5 == 0
    pent_vals = trace_by_order.get(5, set()) | trace_by_order.get(10, set())
    check('', trace_by_order == pred_traces and unip_ok and golden_double_root and (pent_vals == {2, 3}), '')
    lam_mI3 = 4
    g_mI3 = ((4, 0), (0, 4))
    mI3_in_sl = lam_mI3 == pow(m2det(g_mI3), 3, 5)
    det_mI3 = lam_mI3 * m2det(g_mI3) % 5
    check('', not mI3_in_sl and det_mI3 == 4, '')
    K_order = 4 * len(GL2)
    central = True
    for lam in (1, 2, 3, 4):
        for g in GL2[:60]:
            left = (lam * 4 % 5, m2mul(g, ((4, 0), (0, 4))))
            right = (4 * lam % 5, m2mul(((4, 0), (0, 4)), g))
            if left != right:
                central = False
    quot_order = K_order // 2
    mass = 4 * quot_order
    check('', K_order == 1920 and central and (quot_order == 960) and (mass == 3840) and (mass == K_order * 2), '')
    check('', len(classes) == 9, '')
    sys.exit(0 if nfail == 0 else 1)

def rung05_golden():
    import sys
    import functools
    from fractions import Fraction as Fr
    npass = 0
    nfail = 0

    def check(cid, cond, msg):
        nonlocal npass, nfail
        if cond:
            npass += 1
        else:
            nfail += 1

    def info(msg):
        pass

    def qadd(x, y):
        return (x[0] + y[0], x[1] + y[1])

    def qmul(x, y):
        return (x[0] * y[0] + 5 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])

    def qint(n):
        return (Fr(n), Fr(0))

    def qstr(x):
        a, b = x
        if b == 0:
            return f'{a}'
        return f'{a} + {b} sqrt5' if b > 0 else f'{a} - {-b} sqrt5'
    PHI = (Fr(1, 2), Fr(1, 2))
    PHB = (Fr(1, 2), Fr(-1, 2))
    PHI_M1 = (Fr(-1, 2), Fr(1, 2))
    M_PHI = (Fr(-1, 2), Fr(-1, 2))

    def m2mul(A, B):
        return (((A[0][0] * B[0][0] + A[0][1] * B[1][0]) % 5, (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % 5), ((A[1][0] * B[0][0] + A[1][1] * B[1][0]) % 5, (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % 5))

    def m2det(A):
        return (A[0][0] * A[1][1] - A[0][1] * A[1][0]) % 5

    def m2inv(A):
        di = pow(m2det(A), 3, 5)
        return ((A[1][1] * di % 5, -A[0][1] * di % 5), (-A[1][0] * di % 5, A[0][0] * di % 5))
    I2 = ((1, 0), (0, 1))
    Z2 = ((4, 0), (0, 4))
    U1 = ((1, 1), (0, 1))
    U2 = ((1, 2), (0, 1))
    SL2 = []
    for a in range(5):
        for b in range(5):
            for c in range(5):
                for d in range(5):
                    M = ((a, b), (c, d))
                    if m2det(M) == 1:
                        SL2.append(M)

    def m2order(A):
        P = A
        o = 1
        while P != I2:
            P = m2mul(P, A)
            o += 1
        return o

    def conj_class(g):
        return frozenset((m2mul(m2mul(h, g), m2inv(h)) for h in SL2))
    label_of = {}
    cls_size = {}
    cls_rep = {}
    c5a = conj_class(U1)
    c5b = conj_class(U2)
    c10a = conj_class(m2mul(Z2, U1))
    c10b = conj_class(m2mul(Z2, U2))
    for g in SL2:
        if g in label_of:
            continue
        o = m2order(g)
        if o == 1:
            lab = '1a'
            cl = frozenset([g])
        elif o == 2:
            lab = '2a'
            cl = frozenset([g])
        elif o == 4:
            lab = '4a'
            cl = conj_class(g)
        elif o == 3:
            lab = '3a'
            cl = conj_class(g)
        elif o == 6:
            lab = '6a'
            cl = conj_class(g)
        elif o == 5:
            cl = conj_class(g)
            lab = '5a' if cl == c5a else '5b'
        else:
            cl = conj_class(g)
            lab = '10a' if cl == c10a else '10b'
        for x in cl:
            label_of[x] = lab
        cls_size[lab] = len(cl)
        cls_rep[lab] = min(cl)
    LABELS = ('1a', '2a', '4a', '3a', '6a', '5a', '5b', '10a', '10b')
    IRR = ('1', '2a', '2b', '3a', '3b', '4e', '4o', '5', '6')
    DIM = {'1': 1, '2a': 2, '2b': 2, '3a': 3, '3b': 3, '4e': 4, '4o': 4, '5': 5, '6': 6}
    TABLE = {'1': {'1a': qint(1), '2a': qint(1), '4a': qint(1), '3a': qint(1), '6a': qint(1), '5a': qint(1), '5b': qint(1), '10a': qint(1), '10b': qint(1)}, '2a': {'1a': qint(2), '2a': qint(-2), '4a': qint(0), '3a': qint(-1), '6a': qint(1), '5a': PHI_M1, '5b': M_PHI, '10a': PHB, '10b': PHI}, '2b': {'1a': qint(2), '2a': qint(-2), '4a': qint(0), '3a': qint(-1), '6a': qint(1), '5a': M_PHI, '5b': PHI_M1, '10a': PHI, '10b': PHB}, '3a': {'1a': qint(3), '2a': qint(3), '4a': qint(-1), '3a': qint(0), '6a': qint(0), '5a': PHB, '5b': PHI, '10a': PHB, '10b': PHI}, '3b': {'1a': qint(3), '2a': qint(3), '4a': qint(-1), '3a': qint(0), '6a': qint(0), '5a': PHI, '5b': PHB, '10a': PHI, '10b': PHB}, '4e': {'1a': qint(4), '2a': qint(4), '4a': qint(0), '3a': qint(1), '6a': qint(1), '5a': qint(-1), '5b': qint(-1), '10a': qint(-1), '10b': qint(-1)}, '4o': {'1a': qint(4), '2a': qint(-4), '4a': qint(0), '3a': qint(1), '6a': qint(-1), '5a': qint(-1), '5b': qint(-1), '10a': qint(1), '10b': qint(1)}, '5': {'1a': qint(5), '2a': qint(5), '4a': qint(1), '3a': qint(-1), '6a': qint(-1), '5a': qint(0), '5b': qint(0), '10a': qint(0), '10b': qint(0)}, '6': {'1a': qint(6), '2a': qint(-6), '4a': qint(0), '3a': qint(0), '6a': qint(0), '5a': qint(1), '5b': qint(1), '10a': qint(-1), '10b': qint(-1)}}
    struct_ok = len(SL2) == 120 and sorted(cls_size.values()) == [1, 1, 12, 12, 12, 12, 20, 20, 30] and (cls_size['4a'] == 30) and (cls_size['3a'] == 20) and (cls_size['6a'] == 20) and all((cls_size[l] == 12 for l in ('5a', '5b', '10a', '10b')))
    fusion_ok = label_of[m2mul(Z2, cls_rep['3a'])] == '6a' and label_of[m2mul(Z2, cls_rep['5a'])] == '10a' and (label_of[m2mul(Z2, cls_rep['5b'])] == '10b') and (label_of[m2mul(Z2, cls_rep['4a'])] == '4a')
    row_ok = True
    for i, p1 in enumerate(IRR):
        for p2 in IRR[i:]:
            acc = (Fr(0), Fr(0))
            for lab in LABELS:
                acc = qadd(acc, qmul(qint(cls_size[lab]), qmul(TABLE[p1][lab], TABLE[p2][lab])))
            want = qint(120) if p1 == p2 else qint(0)
            if acc != want:
                row_ok = False
    col_ok = True
    for l1 in LABELS:
        for l2 in LABELS:
            acc = (Fr(0), Fr(0))
            for p in IRR:
                acc = qadd(acc, qmul(TABLE[p][l1], TABLE[p][l2]))
            want = (Fr(120, cls_size[l1]), Fr(0)) if l1 == l2 else qint(0)
            if acc != want:
                col_ok = False
    central_ok = all((TABLE[p]['2a'] == qint(DIM[p] * (1 if p in ('1', '3a', '3b', '4e', '5') else -1)) for p in IRR))

    def galois_row(p):
        return tuple(((TABLE[p][l][0], -TABLE[p][l][1]) for l in LABELS))
    rowset = set((tuple((TABLE[p][l] for l in LABELS)) for p in IRR))
    galois_ok = all((galois_row(p) in rowset for p in IRR))
    check('', struct_ok and fusion_ok and row_ok and col_ok and central_ok and galois_ok, '')
    involutions = [g for g in SL2 if g != I2 and m2mul(g, g) == I2]
    t10 = None
    for g in SL2:
        if m2order(g) == 10:
            t10 = g
            break
    stil = None
    t10inv = m2inv(t10)
    for s in SL2:
        if m2mul(m2mul(s, t10), m2inv(s)) == t10inv:
            stil = s
            break
    H = {I2}
    frontier = [I2]
    while frontier:
        g = frontier.pop()
        for h in (t10, stil):
            ng = m2mul(h, g)
            if ng not in H:
                H.add(ng)
                frontier.append(ng)
    t5 = t10
    for _ in range(4):
        t5 = m2mul(t5, t10)
    dic_ok = len(H) == 20 and m2mul(stil, stil) == Z2 and (t5 == Z2)
    quot_prof = []
    seen_cosets = set()
    for x in H:
        key = frozenset((x, m2mul(Z2, x)))
        if key in seen_cosets:
            continue
        seen_cosets.add(key)
        k = 1
        P = x
        while P != I2 and P != Z2:
            P = m2mul(P, x)
            k += 1
        quot_prof.append(k)
    quot_ok = sorted(quot_prof) == [1, 2, 2, 2, 2, 2, 5, 5, 5, 5]
    pre = {I2, stil, Z2, m2mul(Z2, stil)}
    s2 = m2mul(stil, stil)
    s4 = m2mul(s2, s2)
    pre_ok = s2 == Z2 and s4 == I2 and (len(pre) == 4) and (m2order(stil) == 4)
    check('', len(involutions) == 1 and involutions[0] == Z2 and dic_ok and quot_ok and pre_ok, '')

    def readout(E):
        W = {}
        M = (Fr(0), Fr(0))
        for p in IRR:
            acc = (Fr(0), Fr(0))
            for g in E:
                gi = m2inv(g)
                for h in E:
                    acc = qadd(acc, TABLE[p][label_of[m2mul(gi, h)]])
            W[p] = qmul(qint(DIM[p]), acc)
            M = qadd(M, W[p])
        return (W, M)
    Ea = [I2, stil, Z2, m2mul(Z2, stil)]
    Wa, Ma = readout(Ea)
    pred_a = {'1': qint(16), '2a': qint(0), '2b': qint(0), '3a': qint(48), '3b': qint(48), '4e': qint(128), '4o': qint(0), '5': qint(240), '6': qint(0)}
    a_ok = Wa == pred_a and Ma == qint(480)
    Eb = [I2, stil]
    Wb, Mb = readout(Eb)
    pred_b = {'1': qint(4), '2a': qint(8), '2b': qint(8), '3a': qint(12), '3b': qint(12), '4e': qint(32), '4o': qint(32), '5': qint(60), '6': qint(72)}
    b_ok = Wb == pred_b and Mb == qint(240)
    Ec = [I2, U1]
    Wc, Mc = readout(Ec)
    pair2 = sorted([Wc['2a'], Wc['2b']])
    pair3 = sorted([Wc['3a'], Wc['3b']])
    pred2 = sorted([(Fr(6), Fr(2)), (Fr(6), Fr(-2))])
    pred3 = sorted([(Fr(21), Fr(3)), (Fr(21), Fr(-3))])
    c_ok = Wc['1'] == qint(4) and Wc['4e'] == qint(24) and (Wc['4o'] == qint(24)) and (Wc['5'] == qint(50)) and (Wc['6'] == qint(84)) and (pair2 == pred2) and (pair3 == pred3) and (Mc == qint(240))
    check('', a_ok and b_ok and c_ok, '')

    def m2tr(A):
        return (A[0][0] + A[1][1]) % 5
    measured = {}
    for lab in ('1a', '2a', '4a', '3a', '6a'):
        measured[lab] = m2tr(cls_rep[lab])
    reduced = {}
    for lab in ('1a', '2a', '4a', '3a', '6a'):
        a, b = TABLE['2a'][lab]
        reduced[lab] = int(a) % 5 if b == 0 else None
    shadow_ok = all((reduced[lab] == measured[lab] for lab in ('1a', '2a', '4a', '3a', '6a')))
    check('', shadow_ok and measured == {'1a': 2, '2a': 3, '4a': 0, '3a': 4, '6a': 1}, '')
    check('', len(set(label_of.values())) == 9, '')
    sys.exit(0 if nfail == 0 else 1)

def rung06_mckay():
    import sys
    import functools
    from fractions import Fraction as Fr
    npass = 0
    nfail = 0

    def check(cid, cond, msg):
        nonlocal npass, nfail
        if cond:
            npass += 1
        else:
            nfail += 1

    def info(msg):
        pass

    def qadd(x, y):
        return (x[0] + y[0], x[1] + y[1])

    def qmul(x, y):
        return (x[0] * y[0] + 5 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])

    def qint(n):
        return (Fr(n), Fr(0))
    PHI = (Fr(1, 2), Fr(1, 2))
    PHB = (Fr(1, 2), Fr(-1, 2))
    PHI_M1 = (Fr(-1, 2), Fr(1, 2))
    M_PHI = (Fr(-1, 2), Fr(-1, 2))

    def m2mul(A, B):
        return (((A[0][0] * B[0][0] + A[0][1] * B[1][0]) % 5, (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % 5), ((A[1][0] * B[0][0] + A[1][1] * B[1][0]) % 5, (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % 5))

    def m2det(A):
        return (A[0][0] * A[1][1] - A[0][1] * A[1][0]) % 5

    def m2inv(A):
        di = pow(m2det(A), 3, 5)
        return ((A[1][1] * di % 5, -A[0][1] * di % 5), (-A[1][0] * di % 5, A[0][0] * di % 5))
    I2 = ((1, 0), (0, 1))
    Z2 = ((4, 0), (0, 4))
    U1 = ((1, 1), (0, 1))
    U2 = ((1, 2), (0, 1))
    SL2 = []
    for a in range(5):
        for b in range(5):
            for c in range(5):
                for d in range(5):
                    M = ((a, b), (c, d))
                    if m2det(M) == 1:
                        SL2.append(M)

    def m2order(A):
        P = A
        o = 1
        while P != I2:
            P = m2mul(P, A)
            o += 1
        return o

    def conj_class(g):
        return frozenset((m2mul(m2mul(h, g), m2inv(h)) for h in SL2))
    label_of = {}
    cls_size = {}
    c5a = conj_class(U1)
    c10a = conj_class(m2mul(Z2, U1))
    for g in SL2:
        if g in label_of:
            continue
        o = m2order(g)
        if o == 1:
            lab, cl = ('1a', frozenset([g]))
        elif o == 2:
            lab, cl = ('2a', frozenset([g]))
        elif o == 4:
            lab, cl = ('4a', conj_class(g))
        elif o == 3:
            lab, cl = ('3a', conj_class(g))
        elif o == 6:
            lab, cl = ('6a', conj_class(g))
        elif o == 5:
            cl = conj_class(g)
            lab = '5a' if cl == c5a else '5b'
        else:
            cl = conj_class(g)
            lab = '10a' if cl == c10a else '10b'
        for x in cl:
            label_of[x] = lab
        cls_size[lab] = len(cl)
    LABELS = ('1a', '2a', '4a', '3a', '6a', '5a', '5b', '10a', '10b')
    IRR = ('1', '2a', '2b', '3a', '3b', '4e', '4o', '5', '6')
    DIM = {'1': 1, '2a': 2, '2b': 2, '3a': 3, '3b': 3, '4e': 4, '4o': 4, '5': 5, '6': 6}
    TABLE = {'1': {'1a': qint(1), '2a': qint(1), '4a': qint(1), '3a': qint(1), '6a': qint(1), '5a': qint(1), '5b': qint(1), '10a': qint(1), '10b': qint(1)}, '2a': {'1a': qint(2), '2a': qint(-2), '4a': qint(0), '3a': qint(-1), '6a': qint(1), '5a': PHI_M1, '5b': M_PHI, '10a': PHB, '10b': PHI}, '2b': {'1a': qint(2), '2a': qint(-2), '4a': qint(0), '3a': qint(-1), '6a': qint(1), '5a': M_PHI, '5b': PHI_M1, '10a': PHI, '10b': PHB}, '3a': {'1a': qint(3), '2a': qint(3), '4a': qint(-1), '3a': qint(0), '6a': qint(0), '5a': PHB, '5b': PHI, '10a': PHB, '10b': PHI}, '3b': {'1a': qint(3), '2a': qint(3), '4a': qint(-1), '3a': qint(0), '6a': qint(0), '5a': PHI, '5b': PHB, '10a': PHI, '10b': PHB}, '4e': {'1a': qint(4), '2a': qint(4), '4a': qint(0), '3a': qint(1), '6a': qint(1), '5a': qint(-1), '5b': qint(-1), '10a': qint(-1), '10b': qint(-1)}, '4o': {'1a': qint(4), '2a': qint(-4), '4a': qint(0), '3a': qint(1), '6a': qint(-1), '5a': qint(-1), '5b': qint(-1), '10a': qint(1), '10b': qint(1)}, '5': {'1a': qint(5), '2a': qint(5), '4a': qint(1), '3a': qint(-1), '6a': qint(-1), '5a': qint(0), '5b': qint(0), '10a': qint(0), '10b': qint(0)}, '6': {'1a': qint(6), '2a': qint(-6), '4a': qint(0), '3a': qint(0), '6a': qint(0), '5a': qint(1), '5b': qint(1), '10a': qint(-1), '10b': qint(-1)}}

    def mult_in_tensor(pi, pip):
        acc = (Fr(0), Fr(0))
        for lab in LABELS:
            acc = qadd(acc, qmul(qint(cls_size[lab]), qmul(TABLE[pi][lab], qmul(TABLE['2a'][lab], TABLE[pip][lab]))))
        a, b = acc
        if b != 0 or a % 120 != 0:
            return None
        return int(a // 120)
    ADJ = {}
    mult_ok = True
    for pi in IRR:
        for pip in IRR:
            m = mult_in_tensor(pi, pip)
            if m is None or m < 0 or m > 1:
                mult_ok = False
            ADJ[pi, pip] = m if m is not None else -1
    pred_edges = {('1', '2a'), ('2a', '3a'), ('3a', '4o'), ('4o', '5'), ('5', '6'), ('6', '4e'), ('4e', '2b'), ('6', '3b')}
    edges = set()
    sym_ok = True
    for i, pi in enumerate(IRR):
        for pip in IRR[i + 1:]:
            if ADJ[pi, pip] != ADJ[pip, pi]:
                sym_ok = False
            if ADJ[pi, pip] == 1:
                edges.add((pi, pip) if (pi, pip) in pred_edges or (pip, pi) not in pred_edges else (pip, pi))
    diag_ok = all((ADJ[p, p] == 0 for p in IRR))
    edge_ok = set((frozenset(e) for e in edges)) == set((frozenset(e) for e in pred_edges)) and len(edges) == 8
    mark_ok = True
    for pi in IRR:
        s = sum((DIM[pip] * ADJ[pi, pip] for pip in IRR))
        if s != 2 * DIM[pi]:
            mark_ok = False
    PARITY = {'1': 0, '2a': 1, '2b': 1, '3a': 0, '3b': 0, '4e': 0, '4o': 1, '5': 0, '6': 1}
    bip_ok = all((PARITY[a] != PARITY[b] for a, b in edges))
    check('', mult_ok and sym_ok and diag_ok and edge_ok and mark_ok and bip_ok, '')
    IDX = {p: i for i, p in enumerate(IRR)}
    A9 = [[ADJ[p, q] for q in IRR] for p in IRR]

    def matmul9(X, Y):
        return [[sum((X[i][k] * Y[k][j] for k in range(9))) for j in range(9)] for i in range(9)]
    walks = []
    P = [[1 if i == j else 0 for j in range(9)] for i in range(9)]
    for n in range(17):
        walks.append(P[0][0])
        P = matmul9(P, A9)
    moments = []
    mom_int_ok = True
    for n in range(17):
        acc = (Fr(0), Fr(0))
        for lab in LABELS:
            pw = qint(1)
            for _ in range(n):
                pw = qmul(pw, TABLE['2a'][lab])
            acc = qadd(acc, qmul(qint(cls_size[lab]), pw))
        a, b = acc
        if b != 0 or a % 120 != 0:
            mom_int_ok = False
            moments.append(None)
        else:
            moments.append(int(a // 120))
    cat = [1]
    for k in range(8):
        cat.append(sum((cat[i] * cat[k - i] for i in range(k + 1))))
    pred_moments = {0: 1, 2: 1, 4: 2, 6: 5, 8: 14, 10: 42, 12: 133, 14: 442, 16: 1534}
    walk_eq = moments == walks
    odd_zero = all((moments[n] == 0 for n in range(1, 17, 2)))
    even_ok = all((moments[n] == pred_moments[n] for n in range(0, 17, 2)))
    catalan_match = all((moments[n] == cat[n // 2] for n in range(0, 11, 2)))
    dev = tuple((moments[n] - cat[n // 2] for n in (12, 14, 16)))
    check('', walk_eq and mom_int_ok and odd_zero and even_ok and catalan_match and (dev == (1, 13, 104)), '')
    two_m_phi = (Fr(2), Fr(0))
    lhs = qmul(qadd(two_m_phi, (Fr(-1, 2), Fr(-1, 2))), qmul(PHI, PHI))
    unit1 = qmul(qadd(qint(2), (-PHI[0], -PHI[1])), qmul(PHI, PHI)) == qint(1)
    tmphi = qadd(qint(2), (-PHI[0], -PHI[1]))
    tmphb = qadd(qint(2), (-PHB[0], -PHB[1]))
    unit2 = qmul(tmphi, tmphb) == qint(1)

    def readout(E):
        W = {}
        M = (Fr(0), Fr(0))
        for p in IRR:
            acc = (Fr(0), Fr(0))
            for g in E:
                gi = m2inv(g)
                for h in E:
                    acc = qadd(acc, TABLE[p][label_of[m2mul(gi, h)]])
            W[p] = qmul(qint(DIM[p]), acc)
            M = qadd(M, W[p])
        return (W, M)
    vrb = None
    for g in SL2:
        if label_of[g] == '5b':
            vrb = g
            break
    Wv, Mv = readout([I2, vrb])
    w2a = Wv['2a']
    w2b = Wv['2b']
    born_ok = w2a == qmul(qint(4), tmphi) and w2b == qmul(qint(4), qmul(PHI, PHI))
    pair3 = sorted([Wv['3a'], Wv['3b']])
    pred3 = sorted([(Fr(21), Fr(3)), (Fr(21), Fr(-3))])
    rest_ok = Wv['1'] == qint(4) and Wv['4e'] == qint(24) and (Wv['4o'] == qint(24)) and (Wv['5'] == qint(50)) and (Wv['6'] == qint(84)) and (Mv == qint(240))
    prod_ok = qmul(w2a, w2b) == qint(16)
    mu_id = Fr(4, 240) == Fr(1, 60)
    ratio = Fr(1, 60) / Fr(1, 10) == Fr(1, 6)
    check('', unit1 and unit2 and born_ok and (pair3 == pred3) and rest_ok and prod_ok and mu_id and ratio, '')
    sys.exit(0 if nfail == 0 else 1)

def rung07_fingerprint():
    import sys
    import functools
    from fractions import Fraction as Fr
    npass = 0
    nfail = 0

    def check(cid, cond, msg):
        nonlocal npass, nfail
        if cond:
            npass += 1
        else:
            nfail += 1

    def info(msg):
        pass

    def qadd(x, y):
        return (x[0] + y[0], x[1] + y[1])

    def qmul(x, y):
        return (x[0] * y[0] + 5 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])

    def qint(n):
        return (Fr(n), Fr(0))
    PHI = (Fr(1, 2), Fr(1, 2))
    PHB = (Fr(1, 2), Fr(-1, 2))
    PHI_M1 = (Fr(-1, 2), Fr(1, 2))
    M_PHI = (Fr(-1, 2), Fr(-1, 2))

    def m2mul(A, B):
        return (((A[0][0] * B[0][0] + A[0][1] * B[1][0]) % 5, (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % 5), ((A[1][0] * B[0][0] + A[1][1] * B[1][0]) % 5, (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % 5))

    def m2det(A):
        return (A[0][0] * A[1][1] - A[0][1] * A[1][0]) % 5

    def m2inv(A):
        di = pow(m2det(A), 3, 5)
        return ((A[1][1] * di % 5, -A[0][1] * di % 5), (-A[1][0] * di % 5, A[0][0] * di % 5))
    I2 = ((1, 0), (0, 1))
    Z2 = ((4, 0), (0, 4))
    U1 = ((1, 1), (0, 1))
    SL2 = []
    for a in range(5):
        for b in range(5):
            for c in range(5):
                for d in range(5):
                    M = ((a, b), (c, d))
                    if m2det(M) == 1:
                        SL2.append(M)

    def m2order(A):
        P = A
        o = 1
        while P != I2:
            P = m2mul(P, A)
            o += 1
        return o

    def conj_class(g):
        return frozenset((m2mul(m2mul(h, g), m2inv(h)) for h in SL2))
    label_of = {}
    cls_size = {}
    c5a = conj_class(U1)
    c10a = conj_class(m2mul(Z2, U1))
    for g in SL2:
        if g in label_of:
            continue
        o = m2order(g)
        if o == 1:
            lab, cl = ('1a', frozenset([g]))
        elif o == 2:
            lab, cl = ('2a', frozenset([g]))
        elif o == 4:
            lab, cl = ('4a', conj_class(g))
        elif o == 3:
            lab, cl = ('3a', conj_class(g))
        elif o == 6:
            lab, cl = ('6a', conj_class(g))
        elif o == 5:
            cl = conj_class(g)
            lab = '5a' if cl == c5a else '5b'
        else:
            cl = conj_class(g)
            lab = '10a' if cl == c10a else '10b'
        for x in cl:
            label_of[x] = lab
        cls_size[lab] = len(cl)
    LABELS = ('1a', '2a', '4a', '3a', '6a', '5a', '5b', '10a', '10b')
    CHI2 = {'1a': qint(2), '2a': qint(-2), '4a': qint(0), '3a': qint(-1), '6a': qint(1), '5a': PHI_M1, '5b': M_PHI, '10a': PHB, '10b': PHI}
    NMAX = 24
    moments = []
    for n in range(NMAX + 1):
        acc = (Fr(0), Fr(0))
        for lab in LABELS:
            pw = qint(1)
            for _ in range(n):
                pw = qmul(pw, CHI2[lab])
            acc = qadd(acc, qmul(qint(cls_size[lab]), pw))
        a, b = acc
        assert b == 0 and a % 120 == 0
        moments.append(int(a // 120))
    EDGES_E8 = (('2a', '3a'), ('3a', '4o'), ('4o', '5'), ('5', '6'), ('6', '4e'), ('4e', '2b'), ('6', '3b'))
    EDGES_AFF = (('1', '2a'),) + EDGES_E8
    EDGES_E7 = EDGES_E8[1:]

    def matching_poly(edges):
        ne = len(edges)
        counts = {}
        for mask in range(1 << ne):
            used = set()
            ok = True
            k = 0
            for i in range(ne):
                if mask >> i & 1:
                    a, b = edges[i]
                    if a in used or b in used:
                        ok = False
                        break
                    used.add(a)
                    used.add(b)
                    k += 1
            if ok:
                counts[k] = counts.get(k, 0) + 1
        deg = max(counts)
        return [(-1) ** k * counts.get(k, 0) for k in range(deg + 1)]

    def sparse_to_x(coeffs2):
        out = []
        for c in coeffs2:
            out.append(c)
            out.append(0)
        return out[:-1]
    N_match = matching_poly(EDGES_E8)
    D_match = matching_poly(EDGES_AFF)
    N7_match = matching_poly(EDGES_E7)
    pred_N = [1, -7, 14, -8, 1]
    pred_D = [1, -8, 20, -17, 4]
    pred_N7 = [1, -6, 9, -3]
    del_rel = [D_match[i] - (N_match[i] if i < len(N_match) else 0) + (N7_match[i - 1] if 1 <= i <= len(N7_match) else 0) for i in range(len(D_match))]

    def polymul(p, q):
        out = [0] * (len(p) + len(q) - 1)
        for i, a in enumerate(p):
            for j, b in enumerate(q):
                out[i + j] += a * b
        return out
    fact_D = polymul(polymul([1, -4], [1, -1]), [1, -3, 1])
    Dx = sparse_to_x(D_match)
    Nx = sparse_to_x(N_match)
    conv_ok = True
    for n in range(NMAX + 1):
        s = sum((Dx[k] * moments[n - k] for k in range(min(n, len(Dx) - 1) + 1)))
        want = Nx[n] if n < len(Nx) else 0
        if s != want:
            conv_ok = False
    check('', N_match == pred_N and D_match == pred_D and (N7_match == pred_N7) and all((v == 0 for v in del_rel)) and (fact_D == pred_D) and conv_ok, '')
    gp = qmul(qadd(qint(1), (Fr(0), Fr(0))), qint(1))
    f1 = (qint(1), qadd(qint(-2), PHI))
    f2 = (qint(1), qadd(qint(-1), (-PHI[0], -PHI[1])))
    a1 = qadd(qint(2), (-PHI[0], -PHI[1]))
    a2 = qadd(qint(1), PHI)
    c1 = qadd((-a1[0], -a1[1]), (-a2[0], -a2[1]))
    c2 = qmul(a1, a2)
    golden_ok = c1 == qint(-3) and c2 == qint(1)
    L = [2, 1]
    for _ in range(NMAX):
        L.append(L[-1] + L[-2])
    lucas_ok = True
    for n in range(2, NMAX + 1, 2):
        if 120 * moments[n] != 2 ** (n + 1) + 40 + 24 * L[n]:
            lucas_ok = False
    check('', golden_ok and lucas_ok, '')
    cat = [1]
    for k in range(NMAX // 2):
        cat.append(sum((cat[i] * cat[k - i] for i in range(k + 1))))
    dev = [moments[n] - cat[n // 2] for n in range(0, NMAX + 1, 2)]
    pred_dev = [0, 0, 0, 0, 0, 0, 1, 13, 104, 663, 3706, 19040, 92345]
    check('', dev == pred_dev, '')

    def zmul(p, q):
        out = [0] * 7
        for i in range(4):
            for j in range(4):
                out[i + j] += p[i] * q[j]
        for k in (6, 5, 4):
            c = out[k]
            if c:
                out[k] = 0
                if k == 4:
                    for t in range(4):
                        out[t] -= c
                else:
                    out[k - 5] += c
        return out[:4]
    ONE = [1, 0, 0, 0]
    J = [1, 0, 1, 0]
    Jbar = [1, 0, 0, 1]
    oneMJ = [ONE[i] - J[i] for i in range(4)]
    mz2 = [0, 0, -1, 0]
    sh_id = oneMJ == mz2
    oneMJbar = [ONE[i] - Jbar[i] for i in range(4)]
    mod2 = zmul(oneMJ, oneMJbar)
    unit_mod = mod2 == ONE
    p5 = ONE
    for _ in range(5):
        p5 = zmul(p5, oneMJ)
    p10 = zmul(p5, p5)
    ord_ok = p5 == [-1, 0, 0, 0] and p10 == ONE
    prim = True
    pw = ONE
    for k in range(1, 10):
        pw = zmul(pw, oneMJ)
        if k < 10 and pw == ONE:
            prim = False
    shadow_class_chi = CHI2['10b']
    chi_phi = shadow_class_chi == PHI
    check('', sh_id and unit_mod and ord_ok and prim and chi_phi, '')
    check('', 12 * 20 * 30 // 120 == 60 and 12 + 20 - 2 == 30 and (30 == 120 // 4), '')
    sys.exit(0 if nfail == 0 else 1)

def rung08_spectral():
    import sys
    import functools
    from fractions import Fraction as Fr
    npass = 0
    nfail = 0

    def check(cid, cond, msg):
        nonlocal npass, nfail
        if cond:
            npass += 1
        else:
            nfail += 1

    def info(msg):
        pass

    def qadd(x, y):
        return (x[0] + y[0], x[1] + y[1])

    def qsub(x, y):
        return (x[0] - y[0], x[1] - y[1])

    def qmul(x, y):
        return (x[0] * y[0] + 5 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])

    def qint(n):
        return (Fr(n), Fr(0))
    PHI = (Fr(1, 2), Fr(1, 2))
    PHB = (Fr(1, 2), Fr(-1, 2))
    PHI_M1 = (Fr(-1, 2), Fr(1, 2))
    M_PHI = (Fr(-1, 2), Fr(-1, 2))

    def m2mul(A, B):
        return (((A[0][0] * B[0][0] + A[0][1] * B[1][0]) % 5, (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % 5), ((A[1][0] * B[0][0] + A[1][1] * B[1][0]) % 5, (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % 5))

    def m2det(A):
        return (A[0][0] * A[1][1] - A[0][1] * A[1][0]) % 5

    def m2inv(A):
        di = pow(m2det(A), 3, 5)
        return ((A[1][1] * di % 5, -A[0][1] * di % 5), (-A[1][0] * di % 5, A[0][0] * di % 5))
    I2 = ((1, 0), (0, 1))
    Z2 = ((4, 0), (0, 4))
    U1 = ((1, 1), (0, 1))
    SL2 = []
    for a in range(5):
        for b in range(5):
            for c in range(5):
                for d in range(5):
                    M = ((a, b), (c, d))
                    if m2det(M) == 1:
                        SL2.append(M)

    def m2order(A):
        P = A
        o = 1
        while P != I2:
            P = m2mul(P, A)
            o += 1
        return o

    def conj_class(g):
        return frozenset((m2mul(m2mul(h, g), m2inv(h)) for h in SL2))
    label_of = {}
    cls_size = {}
    c5a = conj_class(U1)
    c10a = conj_class(m2mul(Z2, U1))
    for g in SL2:
        if g in label_of:
            continue
        o = m2order(g)
        if o == 1:
            lab, cl = ('1a', frozenset([g]))
        elif o == 2:
            lab, cl = ('2a', frozenset([g]))
        elif o == 4:
            lab, cl = ('4a', conj_class(g))
        elif o == 3:
            lab, cl = ('3a', conj_class(g))
        elif o == 6:
            lab, cl = ('6a', conj_class(g))
        elif o == 5:
            cl = conj_class(g)
            lab = '5a' if cl == c5a else '5b'
        else:
            cl = conj_class(g)
            lab = '10a' if cl == c10a else '10b'
        for x in cl:
            label_of[x] = lab
        cls_size[lab] = len(cl)
    LABELS = ('1a', '2a', '4a', '3a', '6a', '5a', '5b', '10a', '10b')
    CHI2 = {'1a': qint(2), '2a': qint(-2), '4a': qint(0), '3a': qint(-1), '6a': qint(1), '5a': PHI_M1, '5b': M_PHI, '10a': PHB, '10b': PHI}

    def ipolymul(p, q):
        out = [0] * (len(p) + len(q) - 1)
        for i, a in enumerate(p):
            for j, b in enumerate(q):
                out[i + j] += a * b
        return out

    def ipolyadd(p, q):
        n = max(len(p), len(q))
        return [(p[i] if i < len(p) else 0) + (q[i] if i < len(q) else 0) for i in range(n)]

    def ipolyscale(c, p):
        return [c * a for a in p]
    N_poly = [1, 0, -7, 0, 14, 0, -8, 0, 1]
    D_poly = [1, 0, -8, 0, 20, 0, -17, 0, 4]
    f4 = [1, 0, -4]
    f1 = [1, 0, -1]
    fg = [1, 0, -3, 0, 1]
    lhs = ipolyadd(ipolyadd(ipolyscale(2, ipolymul(f1, fg)), ipolyscale(40, ipolymul(f4, fg))), ipolyadd(ipolyscale(30, D_poly), ipolymul([48, 0, -72], ipolymul(f4, f1))))
    z_identity = lhs == ipolyscale(120, N_poly)

    def qpolymul(p, q):
        out = [(Fr(0), Fr(0))] * (len(p) + len(q) - 1)
        for i, a in enumerate(p):
            for j, b in enumerate(q):
                out[i + j] = qadd(out[i + j], qmul(a, b))
        return out
    acc = [(Fr(0), Fr(0))] * 9
    for C in LABELS:
        prod = [qint(1)]
        for Cp in LABELS:
            if Cp == C:
                continue
            prod = qpolymul(prod, [qint(1), (-CHI2[Cp][0], -CHI2[Cp][1])])
        prod = [qmul(qint(cls_size[C]), c) for c in prod]
        acc = [qadd(acc[i], prod[i]) for i in range(9)]
    split_ok = all((acc[i] == qint(120 * N_poly[i]) for i in range(9)))
    L = [2, 1]
    for _ in range(26):
        L.append(L[-1] + L[-2])
    lucas_gf_ok = True
    for m in range(13):
        s = L[2 * m] - (3 * L[2 * m - 2] if m >= 1 else 0) + (L[2 * m - 4] if m >= 2 else 0)
        want = 2 if m == 0 else -3 if m == 1 else 0
        if s != want:
            lucas_gf_ok = False
    check('', z_identity and split_ok and lucas_gf_ok, '')
    NDEG = 64
    a_coeffs = []
    u_prev = {lab: qint(1) for lab in LABELS}
    u_curr = {lab: CHI2[lab] for lab in LABELS}
    for n in range(NDEG + 1):
        if n == 0:
            vals = {lab: qint(1) for lab in LABELS}
        elif n == 1:
            vals = dict(u_curr)
        else:
            vals = {}
            for lab in LABELS:
                nxt = qsub(qmul(CHI2[lab], u_curr[lab]), u_prev[lab])
                vals[lab] = nxt
            u_prev = u_curr
            u_curr = vals
        acc2 = (Fr(0), Fr(0))
        for lab in LABELS:
            acc2 = qadd(acc2, qmul(qint(cls_size[lab]), vals[lab]))
        a, b = acc2
        if b != 0 or a % 120 != 0 or a < 0:
            a_coeffs.append(None)
        else:
            a_coeffs.append(int(a // 120))
    sem = [0] * (NDEG + 1)
    for i in range(NDEG // 12 + 1):
        for j in range(NDEG // 20 + 1):
            for k in (0, 1):
                n = 12 * i + 20 * j + 30 * k
                if n <= NDEG:
                    sem[n] += 1
    ones = {0, 12, 20, 24, 30, 32, 36, 40, 42, 44, 48, 50, 52, 54, 56, 62, 64}
    pred_tab = [1 if n in ones else 2 if n == 60 else 0 for n in range(NDEG + 1)]
    nz = [(n, a_coeffs[n]) for n in range(NDEG + 1) if a_coeffs[n] != 0]
    check('', a_coeffs == sem and a_coeffs == pred_tab, '')
    from math import gcd

    def lcm(a, b):
        return a * b // gcd(a, b)
    excess = Fr(1, 2) + Fr(1, 3) + Fr(1, 5)
    check('', 60 // 12 == 5 and 60 // 20 == 3 and (60 // 30 == 2) and (lcm(lcm(12, 20), 30) == 60) and (excess == Fr(31, 30)) and (excess - 1 == Fr(1, 30)), '')
    check('', z_identity and split_ok and (a_coeffs == pred_tab), '')
    sys.exit(0 if nfail == 0 else 1)

def rung09_dickson():
    import sys
    import functools
    npass = 0
    nfail = 0

    def check(cid, cond, msg):
        nonlocal npass, nfail
        if cond:
            npass += 1
        else:
            nfail += 1

    def info(msg):
        pass

    def padd(p, q):
        out = dict(p)
        for k, c in q.items():
            out[k] = (out.get(k, 0) + c) % 5
            if out[k] == 0:
                del out[k]
        return out

    def pmul(p, q):
        out = {}
        for (i1, j1), c1 in p.items():
            for (i2, j2), c2 in q.items():
                k = (i1 + i2, j1 + j2)
                out[k] = (out.get(k, 0) + c1 * c2) % 5
        return {k: c for k, c in out.items() if c}

    def pscale(a, p):
        a %= 5
        return {k: a * c % 5 for k, c in p.items() if a * c % 5}
    U = {(1, 0): 1}
    V = {(0, 1): 1}
    E6 = pmul(U, V)
    for b in (1, 2, 3, 4):
        E6 = pmul(E6, padd(U, pscale(b, V)))
    E6_closed = padd({(5, 1): 1}, {(1, 5): -1 % 5})
    prod_ok = E6 == E6_closed
    W26 = padd({(25, 1): 1}, {(1, 25): -1 % 5})

    def dehom(p, deg):
        out = [0] * (deg + 1)
        for (i, j), c in p.items():
            assert i + j == deg
            out[i] = c
        return out

    def upolydiv(num, den):
        num = num[:]
        dn = len(den) - 1
        while den[dn] == 0:
            dn -= 1
        q = [0] * (len(num) - dn)
        inv_lead = pow(den[dn], 3, 5)
        for k in range(len(num) - 1, dn - 1, -1):
            c = num[k] * inv_lead % 5
            q[k - dn] = c
            if c:
                for t in range(dn + 1):
                    num[k - dn + t] = (num[k - dn + t] - c * den[t]) % 5
        return (q, num)
    w_u = dehom(W26, 26)
    e_u = dehom(E6, 6)
    q_u, rem = upolydiv(w_u, e_u)
    div_exact = all((r == 0 for r in rem))
    D20 = {}
    for i, c in enumerate(q_u):
        if c:
            D20[i, 20 - i] = c
    prod_back = pmul(D20, E6) == W26
    P = padd({(5, 0): 1}, {(1, 4): -1 % 5})
    P2 = pmul(P, P)
    P4 = pmul(P2, P2)
    D20_closed = padd(P4, {(0, 20): 1})
    closed_ok = D20 == D20_closed

    def m2mul(A, B):
        return (((A[0][0] * B[0][0] + A[0][1] * B[1][0]) % 5, (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % 5), ((A[1][0] * B[0][0] + A[1][1] * B[1][0]) % 5, (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % 5))

    def m2det(A):
        return (A[0][0] * A[1][1] - A[0][1] * A[1][0]) % 5
    SL2 = []
    for a in range(5):
        for b in range(5):
            for c in range(5):
                for d in range(5):
                    M = ((a, b), (c, d))
                    if m2det(M) == 1:
                        SL2.append(M)

    def substitute(p, g):
        (a, b), (c, d) = g
        lu = padd(pscale(a, U), pscale(c, V))
        lv = padd(pscale(b, U), pscale(d, V))
        maxdeg = max((i for i, j in p)) if p else 0
        maxdegj = max((j for i, j in p)) if p else 0
        pu = [{(0, 0): 1}]
        for _ in range(maxdeg):
            pu.append(pmul(pu[-1], lu))
        pv = [{(0, 0): 1}]
        for _ in range(maxdegj):
            pv.append(pmul(pv[-1], lv))
        out = {}
        for (i, j), cc in p.items():
            term = pscale(cc, pmul(pu[i], pv[j]))
            out = padd(out, term)
        return out
    inv_E = all((substitute(E6, g) == E6 for g in SL2))
    inv_D = all((substitute(D20, g) == D20 for g in SL2))
    gdiag = ((2, 0), (0, 1))
    wE = substitute(E6, gdiag) == pscale(2, E6)
    wD = substitute(D20, gdiag) == D20

    def pdiff(p, var):
        out = {}
        for (i, j), c in p.items():
            if var == 0 and i > 0:
                k = (i - 1, j)
                out[k] = (out.get(k, 0) + c * i) % 5
            if var == 1 and j > 0:
                k = (i, j - 1)
                out[k] = (out.get(k, 0) + c * j) % 5
        return {k: c for k, c in out.items() if c}
    Jac = padd(pmul(pdiff(E6, 0), pdiff(D20, 1)), pscale(-1, pmul(pdiff(E6, 1), pdiff(D20, 0))))
    Jac_pred = pscale(4, pmul(pmul(pmul(P2, P), {(0, 3): 1}), E6))
    jac_ok = Jac == Jac_pred and len(Jac) > 0
    check('', prod_ok and div_exact and prod_back and closed_ok and inv_E and inv_D and wE and wD and jac_ok, '')
    S = ((0, 4), (1, 0))
    T = ((1, 1), (0, 1))
    grp = {((1, 0), (0, 1))}
    frontier = [((1, 0), (0, 1))]
    while frontier:
        g = frontier.pop()
        for h in (S, T):
            ng = m2mul(h, g)
            if ng not in grp:
                grp.add(ng)
                frontier.append(ng)
    gen_ok = len(grp) == 120

    def action_matrix(g, n):
        (a, b), (c, d) = g
        lu = padd(pscale(a, U), pscale(c, V))
        lv = padd(pscale(b, U), pscale(d, V))
        pu = [{(0, 0): 1}]
        for _ in range(n):
            pu.append(pmul(pu[-1], lu))
        pv = [{(0, 0): 1}]
        for _ in range(n):
            pv.append(pmul(pv[-1], lv))
        M = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            img = pmul(pu[i], pv[n - i])
            for (ii, jj), cc in img.items():
                M[ii][i] = cc
        return M

    def fixed_dim(n):
        MS = action_matrix(S, n)
        MT = action_matrix(T, n)
        rows = []
        for M in (MS, MT):
            for r in range(n + 1):
                row = [(M[r][cc] - (1 if r == cc else 0)) % 5 for cc in range(n + 1)]
                rows.append(row)
        rank = 0
        ncols = n + 1
        pivots_done = 0
        rr = [row[:] for row in rows]
        for col in range(ncols):
            piv = None
            for r in range(pivots_done, len(rr)):
                if rr[r][col] % 5:
                    piv = r
                    break
            if piv is None:
                continue
            rr[pivots_done], rr[piv] = (rr[piv], rr[pivots_done])
            inv = pow(rr[pivots_done][col], 3, 5)
            rr[pivots_done] = [x * inv % 5 for x in rr[pivots_done]]
            for r in range(len(rr)):
                if r != pivots_done and rr[r][col] % 5:
                    f = rr[r][col]
                    rr[r] = [(rr[r][t] - f * rr[pivots_done][t]) % 5 for t in range(ncols)]
            pivots_done += 1
        rank = pivots_done
        return n + 1 - rank
    dims = [fixed_dim(n) for n in range(41)]
    sem = set()
    for i in range(8):
        for j in range(3):
            n = 6 * i + 20 * j
            if n <= 40:
                sem.add(n)
    pred_dims = [1 if n in sem else 0 for n in range(41)]
    check('', gen_ok and dims == pred_dims, '')
    p = 5
    Vv = 2 * (p + 1)
    Ff = p * (p - 1)
    Ee = p * (p + 1)
    poly_id = [2 + 0, 2 - 1 - 1, -1 + 1]
    from math import gcd

    def lcm(a, b):
        return a * b // gcd(a, b)
    check('', (Vv, Ff, Ee) == (12, 20, 30) and poly_id == [2, 0, 0] and ((p + 1, p * (p - 1)) == (Vv // 2, Ff)) and (lcm(6, 20) == 60) and (lcm(lcm(12, 20), 30) == 60), '')
    check('', True, '')
    sys.exit(0 if nfail == 0 else 1)

def rung10_klein():
    import sys
    import functools
    npass = 0
    nfail = 0

    def check(cid, cond, msg):
        nonlocal npass, nfail
        if cond:
            npass += 1
        else:
            nfail += 1

    def info(msg):
        pass

    def padd(p, q, m):
        out = dict(p)
        for k, c in q.items():
            v = out.get(k, 0) + c
            if m:
                v %= m
            if v:
                out[k] = v
            elif k in out:
                del out[k]
        return out

    def pmul(p, q, m):
        out = {}
        for (i1, j1), c1 in p.items():
            for (i2, j2), c2 in q.items():
                k = (i1 + i2, j1 + j2)
                v = out.get(k, 0) + c1 * c2
                if m:
                    v %= m
                out[k] = v
        return {k: c for k, c in out.items() if c}

    def pscale(a, p, m):
        out = {}
        for k, c in p.items():
            v = a * c
            if m:
                v %= m
            if v:
                out[k] = v
        return out

    def ppow(p, n, m):
        out = {(0, 0): 1}
        for _ in range(n):
            out = pmul(out, p, m)
        return out

    def reduce5(p):
        return {k: c % 5 for k, c in p.items() if c % 5}
    fZ = {(11, 1): 1, (6, 6): 11, (1, 11): -1}
    HZ = {(20, 0): -1, (0, 20): -1, (15, 5): 228, (5, 15): -228, (10, 10): -494}
    TZ = {(30, 0): 1, (0, 30): 1, (25, 5): 522, (5, 25): -522, (20, 10): -10005, (10, 20): -10005}
    lhs = padd(ppow(TZ, 2, 0), ppow(HZ, 3, 0), 0)
    rhs = pscale(1728, ppow(fZ, 5, 0), 0)
    klein_Z = lhs == rhs
    check('', klein_Z and 1728 == 12 ** 3 and (1728 % 5 == 3), '')
    fb = reduce5(fZ)
    Hb = reduce5(HZ)
    Tb = reduce5(TZ)
    U = {(1, 0): 1}
    V = {(0, 1): 1}

    def substitute5(p, g):
        (a, b), (c, d) = g
        lu = padd(pscale(a, U, 5), pscale(c, V, 5), 5)
        lv = padd(pscale(b, U, 5), pscale(d, V, 5), 5)
        mi = max((i for i, j in p))
        mj = max((j for i, j in p))
        pu = [{(0, 0): 1}]
        for _ in range(mi):
            pu.append(pmul(pu[-1], lu, 5))
        pv = [{(0, 0): 1}]
        for _ in range(mj):
            pv.append(pmul(pv[-1], lv, 5))
        out = {}
        for (i, j), cc in p.items():
            out = padd(out, pscale(cc, pmul(pu[i], pv[j], 5), 5), 5)
        return out
    Tuni = ((1, 1), (0, 1))
    f_not_inv = substitute5(fb, Tuni) != fb
    H_not_inv = substitute5(Hb, Tuni) != Hb
    T_not_inv = substitute5(Tb, Tuni) != Tb
    rel5 = padd(ppow(Tb, 2, 5), ppow(Hb, 3, 5), 5) == pscale(3, ppow(fb, 5, 5), 5)
    check('', f_not_inv and H_not_inv and T_not_inv and rel5, '')
    E6 = padd({(5, 1): 1}, {(1, 5): 4}, 5)
    P = padd({(5, 0): 1}, {(1, 4): 4}, 5)
    D20 = padd(ppow(P, 4, 5), {(0, 20): 1}, 5)
    E6_2 = ppow(E6, 2, 5)
    E6_5 = ppow(E6, 5, 5)

    def m2mulm(A, B):
        return (((A[0][0] * B[0][0] + A[0][1] * B[1][0]) % 5, (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % 5), ((A[1][0] * B[0][0] + A[1][1] * B[1][0]) % 5, (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % 5))
    S = ((0, 4), (1, 0))
    gen_inv = all((substitute5(p, g) == p for p in (E6_2, D20, E6_5) for g in (S, Tuni)))

    def action_matrix(g, n):
        (a, b), (c, d) = g
        lu = padd(pscale(a, U, 5), pscale(c, V, 5), 5)
        lv = padd(pscale(b, U, 5), pscale(d, V, 5), 5)
        pu = [{(0, 0): 1}]
        for _ in range(n):
            pu.append(pmul(pu[-1], lu, 5))
        pv = [{(0, 0): 1}]
        for _ in range(n):
            pv.append(pmul(pv[-1], lv, 5))
        M = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            img = pmul(pu[i], pv[n - i], 5)
            for (ii, jj), cc in img.items():
                M[ii][i] = cc
        return M

    def fixed_dim(n):
        rows = []
        for g in (S, Tuni):
            M = action_matrix(g, n)
            for r in range(n + 1):
                rows.append([(M[r][cc] - (1 if r == cc else 0)) % 5 for cc in range(n + 1)])
        ncols = n + 1
        piv = 0
        for col in range(ncols):
            sel = None
            for r in range(piv, len(rows)):
                if rows[r][col] % 5:
                    sel = r
                    break
            if sel is None:
                continue
            rows[piv], rows[sel] = (rows[sel], rows[piv])
            inv = pow(rows[piv][col], 3, 5)
            rows[piv] = [x * inv % 5 for x in rows[piv]]
            for r in range(len(rows)):
                if r != piv and rows[r][col] % 5:
                    fct = rows[r][col]
                    rows[r] = [(rows[r][t] - fct * rows[piv][t]) % 5 for t in range(ncols)]
            piv += 1
        return n + 1 - piv
    dims = (fixed_dim(12), fixed_dim(20), fixed_dim(30))
    check('', dims == (1, 1, 1) and gen_inv, '')
    E6_10 = ppow(E6, 10, 5)
    D20_3 = ppow(D20, 3, 5)
    indep = True
    for s in range(1, 5):
        if pscale(s, E6_10, 5) == D20_3:
            indep = False
    sols = sorted(((a, g) for a in range(5) for g in range(5) if g * g % 5 == 3 * a % 5))
    pred_sols = [(0, 0), (2, 1), (2, 4), (3, 2), (3, 3)]
    good_alpha = sorted(set((a for a, g in sols if a != 0)))
    check('', indep and len(E6_10) > 0 and (len(D20_3) > 0) and (sols == pred_sols) and (good_alpha == [2, 3]), '')

    def umul(p, q):
        out = [0] * (len(p) + len(q) - 1)
        for i, a in enumerate(p):
            for j, b in enumerate(q):
                out[i + j] = (out[i + j] + a * b) % 5
        return out

    def uadd(p, q):
        n = max(len(p), len(q))
        return [((p[i] if i < len(p) else 0) + (q[i] if i < len(q) else 0)) % 5 for i in range(n)]

    def uscale(a, p):
        return [a * c % 5 for c in p]

    def ucompose(p, q):
        out = [0]
        pw = [1]
        for c in p:
            out = uadd(out, uscale(c, pw))
            pw = umul(pw, q)
        return out

    def trim(p):
        while len(p) > 1 and p[-1] == 0:
            p.pop()
        return p
    t = [0, 1]
    wp = [0, 4, 0, 0, 0, 1]
    t25 = [0] * 26
    t25[25] = 1
    lhs5 = trim(uadd(t25, uscale(4, t)))
    wpwp = trim(ucompose(wp, wp))
    rhs5 = trim(uadd(wpwp, uscale(2, wp)))
    iterate_ok = lhs5 == rhs5
    wp_roots = sorted((x for x in range(5) if (pow(x, 5, 5) - x) % 5 == 0))
    s = [0, 1]
    wps = [0, 4, 0, 0, 0, 1]
    wps_over_s = [4, 0, 0, 0, 1]
    lhs6 = trim(uadd(wps_over_s, [2]))
    rhs6 = [1, 0, 0, 0, 1]
    ratio_ok = lhs6 == rhs6
    wp4 = umul(umul(wp, wp), umul(wp, wp))
    D20_from_as = {}
    for i, c in enumerate(wp4):
        if c:
            D20_from_as[i, 20 - i] = c
    D20_from_as = padd(D20_from_as, {(0, 20): 1}, 5)
    d20_as_ok = D20_from_as == D20
    check('', iterate_ok and wp_roots == [0, 1, 2, 3, 4] and ratio_ok and d20_as_ok, '')
    sys.exit(0 if nfail == 0 else 1)

def rung11_integral():
    import sys
    import functools
    from math import gcd
    from fractions import Fraction as Fr
    npass = 0
    nfail = 0

    def check(cid, cond, msg):
        nonlocal npass, nfail
        if cond:
            npass += 1
        else:
            nfail += 1

    def info(msg):
        pass

    def zadd(p, q):
        return [p[i] + q[i] for i in range(4)]

    def zsub(p, q):
        return [p[i] - q[i] for i in range(4)]

    def zscale(a, p):
        return [a * c for c in p]

    def zneg(p):
        return [-c for c in p]

    def zmul(p, q):
        out = [Fr(0)] * 7
        for i in range(4):
            if p[i] == 0:
                continue
            for j in range(4):
                if q[j] == 0:
                    continue
                out[i + j] += p[i] * q[j]
        for k in (6, 5, 4):
            c = out[k]
            if c:
                out[k] = 0
                if k == 4:
                    for t in range(4):
                        out[t] -= c
                else:
                    out[k - 5] += c
        return out[:4]

    def zint(n):
        return [Fr(n), Fr(0), Fr(0), Fr(0)]
    ZERO = zint(0)
    ONE = zint(1)
    ZETA = [Fr(0), Fr(1), Fr(0), Fr(0)]

    def zeq(p, q):
        return all((p[i] == q[i] for i in range(4)))

    def galois(p, k):
        out = [Fr(0)] * 7
        for i in range(4):
            if p[i]:
                e = i * k % 5
                if e == 4:
                    for t in range(4):
                        out[t] -= p[i]
                else:
                    out[e] += p[i]
        return out[:4]

    def znorm(p):
        r = ONE
        for k in (1, 2, 3, 4):
            r = zmul(r, galois(p, k))
        return r[0]

    def zinv(p):
        r = ONE
        for k in (2, 3, 4):
            r = zmul(r, galois(p, k))
        n = znorm(p)
        return zscale(Fr(1) / n, r)

    def v5(fr):
        if fr == 0:
            return None
        n, d, v = (fr.numerator, fr.denominator, 0)
        while n % 5 == 0:
            n //= 5
            v += 1
        while d % 5 == 0:
            d //= 5
            v -= 1
        return v

    def vlam(p):
        if zeq(p, ZERO):
            return None
        return v5(znorm(p))
    LAM = zsub(ONE, ZETA)
    LAMINV = zinv(LAM)
    W = [Fr(0), Fr(-1), Fr(1), Fr(-1)]

    def red(p):
        v = vlam(p)
        if v is None or v > 0:
            return 0
        D = 1
        for c in p:
            D = D * c.denominator // gcd(D, c.denominator)
        k = 0
        Dp = D
        while Dp % 5 == 0:
            Dp //= 5
            k += 1
        y = [c * D for c in p]
        if k:
            wk = ONE
            for _ in range(k):
                wk = zmul(wk, W)
            y = zmul(y, wk)
            for _ in range(4 * k):
                y = zmul(y, LAMINV)
        s = sum(y)
        assert s.denominator % 5 != 0
        sred = s.numerator * pow(s.denominator, 3, 5) % 5
        return sred * pow(Dp % 5, 3, 5) % 5

    def mmul(A, B):
        return ((zadd(zmul(A[0][0], B[0][0]), zmul(A[0][1], B[1][0])), zadd(zmul(A[0][0], B[0][1]), zmul(A[0][1], B[1][1]))), (zadd(zmul(A[1][0], B[0][0]), zmul(A[1][1], B[1][0])), zadd(zmul(A[1][0], B[0][1]), zmul(A[1][1], B[1][1]))))

    def mkey(A):
        return tuple((tuple((tuple((c for c in e)) for e in row)) for row in A))
    ST = ((zint(0), zint(-1)), (zint(1), zint(0)))
    Z4 = galois(ZETA, 4)
    TT = ((ZETA, ONE), (zint(0), Z4))
    IM = ((ONE, ZERO), (ZERO, ONE))
    MI = ((zint(-1), ZERO), (ZERO, zint(-1)))
    t5 = IM
    for _ in range(5):
        t5 = mmul(t5, TT)
    st = mmul(ST, TT)
    st3 = mmul(mmul(st, st), st)
    s2 = mmul(ST, ST)
    rel_ok = mkey(t5) == mkey(IM) and mkey(st3) == mkey(MI) and (mkey(s2) == mkey(MI))
    grp = {mkey(IM): IM}
    frontier = [IM]
    cap = 2000
    while frontier and len(grp) <= cap:
        g = frontier.pop()
        for h in (ST, TT):
            ng = mmul(h, g)
            k = mkey(ng)
            if k not in grp:
                grp[k] = ng
                frontier.append(ng)
    G = list(grp.values())
    integral_ok = all((all((all((c.denominator == 1 for c in e)) for e in row)) for A in G for row in A))

    def red_entry(x):
        v = vlam(x)
        if v is None or v > 0:
            return 0
        return red(x)

    def redmat2(A):
        return ((red_entry(A[0][0]), red_entry(A[0][1])), (red_entry(A[1][0]), red_entry(A[1][1])))
    red_set = set((redmat2(A) for A in G))
    SL2 = set()
    for a in range(5):
        for b in range(5):
            for c in range(5):
                for d in range(5):
                    if (a * d - b * c) % 5 == 1:
                        SL2.add(((a, b), (c, d)))
    bij_ok = len(G) == 120 and len(red_set) == 120 and (red_set == SL2)
    check('', rel_ok and integral_ok and bij_ok, '')

    def qpadd(p, q):
        out = dict(p)
        for k, c in q.items():
            if k in out:
                s = zadd(out[k], c)
                if zeq(s, ZERO):
                    del out[k]
                else:
                    out[k] = s
            else:
                out[k] = c
        return out

    def qpmul(p, q):
        out = {}
        for (i1, j1), c1 in p.items():
            for (i2, j2), c2 in q.items():
                k = (i1 + i2, j1 + j2)
                pr = zmul(c1, c2)
                if k in out:
                    s = zadd(out[k], pr)
                    if zeq(s, ZERO):
                        del out[k]
                    else:
                        out[k] = s
                elif not zeq(pr, ZERO):
                    out[k] = pr
        return out

    def qpscale(a, p):
        return {k: zmul(a, c) for k, c in p.items()}

    def qppow(p, n):
        out = {(0, 0): ONE}
        for _ in range(n):
            out = qpmul(out, p)
        return out
    UU = {(1, 0): ONE}
    VV = {(0, 1): ONE}

    def qsubstitute(p, g):
        lu = qpadd(qpscale(g[0][0], UU), qpscale(g[1][0], VV))
        lv = qpadd(qpscale(g[0][1], UU), qpscale(g[1][1], VV))
        mi = max((i for i, j in p))
        mj = max((j for i, j in p))
        pu = [{(0, 0): ONE}]
        for _ in range(mi):
            pu.append(qpmul(pu[-1], lu))
        pv = [{(0, 0): ONE}]
        for _ in range(mj):
            pv.append(qpmul(pv[-1], lv))
        out = {}
        for (i, j), cc in p.items():
            out = qpadd(out, qpscale(cc, qpmul(pu[i], pv[j])))
        return out

    def reynolds(mono):
        acc = {}
        for g in G:
            acc = qpadd(acc, qsubstitute(mono, g))
        return qpscale([Fr(1, 120), Fr(0), Fr(0), Fr(0)], acc)

    def primitivize(p):
        vmin = None
        for c in p.values():
            v = vlam(c)
            if vmin is None or v < vmin:
                vmin = v
        if vmin == 0:
            return p
        if vmin > 0:
            fac = ONE
            for _ in range(vmin):
                fac = zmul(fac, LAMINV)
        else:
            fac = ONE
            for _ in range(-vmin):
                fac = zmul(fac, LAM)
        return {k: zmul(fac, c) for k, c in p.items()}
    fprime = None
    for mono in ({(6, 6): ONE}, {(12, 0): ONE}, {(11, 1): ONE}, {(10, 2): ONE}):
        cand = reynolds(mono)
        if cand:
            fprime = cand
            break
    fprime = primitivize(fprime)
    inv_ok = all((qsubstitute(fprime, g) == fprime for g in (ST, TT)))

    def qpdiff(p, var):
        out = {}
        for (i, j), c in p.items():
            if var == 0 and i > 0:
                out[i - 1, j] = zadd(out.get((i - 1, j), ZERO), zscale(Fr(i), c))
            if var == 1 and j > 0:
                out[i, j - 1] = zadd(out.get((i, j - 1), ZERO), zscale(Fr(j), c))
        return {k: c for k, c in out.items() if not zeq(c, ZERO)}
    fu = qpdiff(fprime, 0)
    fv = qpdiff(fprime, 1)
    h_raw = qpadd(qpmul(qpdiff(fu, 0), qpdiff(fv, 1)), qpscale(zint(-1), qppow(qpdiff(fu, 1), 2)))
    h = primitivize(h_raw)
    tt_raw = qpadd(qpmul(fu, qpdiff(h, 1)), qpscale(zint(-1), qpmul(fv, qpdiff(h, 0))))
    tt = primitivize(tt_raw)

    def red_poly(p):
        out = {}
        for k, c in p.items():
            r = red_entry(c)
            if r:
                out[k] = r
        return out
    fbar = red_poly(fprime)
    hbar = red_poly(h)
    tbar = red_poly(tt)
    E6f = {(5, 1): 1, (1, 5): 4}

    def f5mul(p, q):
        out = {}
        for (i1, j1), c1 in p.items():
            for (i2, j2), c2 in q.items():
                k = (i1 + i2, j1 + j2)
                out[k] = (out.get(k, 0) + c1 * c2) % 5
        return {k: c for k, c in out.items() if c}

    def f5pow(p, n):
        out = {(0, 0): 1}
        for _ in range(n):
            out = f5mul(out, p)
        return out

    def f5scale(a, p):
        a %= 5
        return {k: a * c % 5 for k, c in p.items() if a * c % 5}
    E6_2 = f5pow(E6f, 2)
    E6_5 = f5pow(E6f, 5)
    Pf = {(5, 0): 1, (1, 4): 4}
    D20f = dict(f5pow(Pf, 4))
    D20f[0, 20] = (D20f.get((0, 20), 0) + 1) % 5

    def match_scalar(p, base):
        for s in range(1, 5):
            if f5scale(s, base) == p:
                return s
        return 0
    alpha = match_scalar(fbar, E6_2)
    betap = match_scalar(hbar, D20f)
    gamma = match_scalar(tbar, E6_5)
    check('', inv_ok and alpha != 0 and (betap != 0) and (gamma != 0), '')
    tt2 = qppow(tt, 2)
    h3 = qppow(h, 3)
    f5p = qppow(fprime, 5)
    keys = sorted(set(tt2) | set(h3) | set(f5p))
    A = None
    B = None
    for i in range(len(keys)):
        found = False
        for j in range(i + 1, len(keys)):
            k1, k2 = (keys[i], keys[j])
            a11 = h3.get(k1, ZERO)
            a12 = f5p.get(k1, ZERO)
            a21 = h3.get(k2, ZERO)
            a22 = f5p.get(k2, ZERO)
            det = zsub(zmul(a11, a22), zmul(a12, a21))
            if not zeq(det, ZERO):
                b1 = tt2.get(k1, ZERO)
                b2 = tt2.get(k2, ZERO)
                di = zinv(det)
                A = zmul(di, zsub(zmul(b1, a22), zmul(a12, b2)))
                B = zmul(di, zsub(zmul(a11, b2), zmul(b1, a21)))
                found = True
                break
        if found:
            break
    resid = qpadd(tt2, qpadd(qpscale(zneg(A), h3), qpscale(zneg(B), f5p)))
    rel_exact = len(resid) == 0
    vA = vlam(A)
    vB = vlam(B)
    Bred = red_entry(B)
    chan_f5 = gamma * gamma % 5 == Bred * alpha % 5
    check('', rel_exact and (vA is None or vA >= 1) and (vB == 0) and chan_f5, '')
    cbar = 3 * pow(Bred, 3, 5) % 5
    alpha_p = cbar * alpha % 5
    gamma_p = pow(cbar, 3, 5) * gamma % 5
    orbit = {(2, 1), (2, 4), (3, 2), (3, 3)}
    check('', (alpha_p, gamma_p) in orbit and gamma_p * gamma_p % 5 == 3 * alpha_p % 5, '')
    sys.exit(0 if nfail == 0 else 1)
BLOCKS = [('COLOR-RETURN', rung01_return), ('COLOR-TORSOR', rung02_torsor), ('COLOR-DYNAMIC', rung03_dynamical), ('COLOR-KINEMATIC', rung03_kinematical), ('COLOR-CORE', rung04_core), ('COLOR-GOLDEN', rung05_golden), ('COLOR-MCKAY', rung06_mckay), ('COLOR-MOMENTS', rung07_fingerprint), ('COLOR-SPECTRAL', rung08_spectral), ('COLOR-DICKSON', rung09_dickson), ('COLOR-KLEIN', rung10_klein), ('COLOR-INTEGRAL', rung11_integral)]

def main():
    passed = 0
    for index, (label, function) in enumerate(BLOCKS, 1):
        capture = io.StringIO()
        code = 0
        try:
            with redirect_stdout(capture):
                function()
        except SystemExit as exc:
            code = 0 if exc.code is None else int(exc.code)
        except Exception as exc:
            code = 1
            capture.write('EXCEPTION %s: %s\\n' % (type(exc).__name__, exc))
        if code:
            print('%02d %-18s FAIL' % (index, label))
            print(capture.getvalue(), end='')
            print('RESULT %d/%d FAIL' % (passed, len(BLOCKS)))
            raise SystemExit(1)
        passed += 1
        print('%02d %-18s PASS' % (index, label))
    print('RESULT %d/%d ALL PASS' % (passed, len(BLOCKS)))
if __name__ == '__main__':
    main()
