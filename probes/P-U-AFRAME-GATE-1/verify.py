#!/usr/bin/env python3
# Copyright 2026 A. M. Thorn
# SPDX-License-Identifier: Apache-2.0
"""Frozen exact falsifiers for P-U-AFRAME-GATE-1, the native shell gate of U."""
import sys
from collections import Counter
from hashlib import sha256
from itertools import product
from pathlib import Path

P = 5
STATES = tuple(product(range(P), repeat=6))
PISTONS = tuple(product(range(P), repeat=4))
ZERO = (0, 0, 0, 0, 0, 0)
HZERO = (0, 0)
THETA = tuple(bin(n).count('1') % 2 for n in range(4097))
SHEET = ((0, 4, 0, 4, 4), (2, 1, 1, 3, 1))
FIXED_D = (1, 3, 4, 2, 3, 3)
FIXED_E = (1, 3, 4, 2, 1, 3)

AF = ((1, 0, 1, 0), (0, 1, 0, 1), (-2, 1, -1, 1), (1, -3, 1, -2))
BF = ((4, -2, 2, -1), (-2, 6, -1, 3), (2, -1, 2, 0), (-1, 3, 0, 2))
LM = ((1, -3, -1, -2), (-3, 4, -2, 1), (0, 5, 1, 2), (5, -5, 2, -1))
VINV = ((1, 2, 1, 2), (2, -1, 2, -1), (0, -5, 1, -3), (-5, 5, -3, 4))
VH = ((1, 1, 1, 1), (2, 1, 2, 1), (0, -1, 1, 0), (-5, -2, -3, -1))
LVH = ((5, 3, 0, 0), (0, 1, 0, 0), (0, 0, 5, 3), (0, 0, 0, 1))
I4 = tuple(tuple(int(i == j) for j in range(4)) for i in range(4))

# Branch table of PROOF.md section 4: (z,t) -> (generator, next trace, h law).
TABLE = {
    (0, 0): (0, 0, 'A'), (1, 0): (1, 4, 'NJ'), (2, 0): (2, 0, 'C'),
    (3, 0): (3, 4, 'N'), (4, 0): (4, 4, 'N'),
    (0, 1): (2, 2, 'C'), (1, 1): (3, 1, 'N'), (2, 1): (4, 1, 'N'),
    (3, 1): (0, 3, 'A'), (4, 1): (1, 1, 'NJ'),
}
WORDS = {0: (0, 2, 4), 1: (1, 1, 3), 2: (2, 2, 4), 3: (3, 1, 3), 4: (4, 1, 3)}


class Fired(Exception):
    """A frozen mathematical predicate failed."""


def need(condition, label):
    if not condition:
        raise Fired(label)


def red(v):
    return tuple(c % P for c in v)


def generator(x, k):
    p1, p4, p1p, p4p, q, r = x
    if k == 0:
        y = (p4, p1, p4p, p1p, q, r)
    elif k == 1:
        y = (-p1p, -p4p, -p1, -p4, -q, -r)
    elif k == 2:
        y = (2 - p1p, 1 - p4p + r, 2 - p1, 1 - p4 - r, 1 - q, -r)
    elif k == 3:
        y = (2 - p1, 1 - p4, 3 - p1p, 4 - p4p, 1 - q, 1 - r)
    else:
        y = (2 - p1, 1 - p4, 3 - p1p, 4 - p4p, 2 - q, 1 - r)
    return red(y)


def trace(x):
    return sum(x) % P


def step(x, t):
    k = (trace(x) + 2 * t) % P
    return generator(x, k), k


def h(x):
    p1, p4, p1p, p4p = x[:4]
    return ((p4 + 2 * p1) % P, (p4p + 2 * p1p) % P)


def w_map(p):
    p1, p4, p1p, p4p = p
    return (p4, p1, p4p, p1p)


def neg(v):
    return red(tuple(-c for c in v))


def swap(v):
    return (v[1], v[0])


def in_c(y):
    return (y[0] + 2 * y[1]) % P == 0 and (y[2] + 2 * y[3]) % P == 0


def law(name, x):
    hx = h(x)
    p1, p4, p1p, p4p, q, r = x
    if name == 'A':
        return ((p1 + 2 * p4) % P, (p1p + 2 * p4p) % P)
    if name == 'NJ':
        return neg(swap(hx))
    if name == 'C':
        return ((-hx[1] + r) % P, (-hx[0] - r) % P)
    return neg(hx)


def mul(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(len(b)))
                       for j in range(len(b[0]))) for i in range(len(a)))


def sub(a, b):
    return tuple(tuple(x - y for x, y in zip(ra, rb)) for ra, rb in zip(a, b))


def scal(c, a):
    return tuple(tuple(c * x for x in row) for row in a)


def transpose(a):
    return tuple(zip(*a))


def matvec(a, v):
    return tuple(sum(a[i][k] * v[k] for k in range(len(v))) for i in range(len(a)))


def det(a):
    if len(a) == 1:
        return a[0][0]
    return sum((-1) ** j * a[0][j] * det(tuple(row[:j] + row[j + 1:] for row in a[1:]))
               for j in range(len(a)))


def energy(y):
    num = sum(y[i] * BF[i][j] * y[j] for i in range(4) for j in range(4))
    need(num % 2 == 0, 'energy numerator parity')
    return num // 2


def vee(x):
    p1, p4, p1p, p4p = x[:4]
    chi = 1 if trace(x) == 1 else -1
    return red((p1 + p1p, p4 + p4p, chi * (p1 - p1p - 2), chi * (p4 - p4p - 1)))


def digest(rows):
    text = ''.join(','.join(str(v) for v in row) + '\n' for row in sorted(rows))
    return sha256(text.encode('ascii')).hexdigest()


def f1():
    trace_law = {0: lambda z: z, 1: lambda z: -z, 2: lambda z: 2 - z,
                 3: lambda z: 2 - z, 4: lambda z: 3 - z}
    qr_law = {0: lambda q, r: (q, r), 1: lambda q, r: (-q, -r),
              2: lambda q, r: (1 - q, -r), 3: lambda q, r: (1 - q, 1 - r),
              4: lambda q, r: (2 - q, 1 - r)}
    need(THETA[:3] == (0, 1, 1), 'driver prefix')
    fixed = {k: [] for k in range(5)}
    involutions = 0
    for x in STATES:
        z, q, r = trace(x), x[4], x[5]
        for k in range(5):
            y = generator(x, k)
            need(generator(y, k) == x, 'involution')
            involutions += 1
            need(trace(y) == trace_law[k](z) % P, 'trace law')
            need(y[4:] == red(qr_law[k](q, r)), 'quotient law')
            if y == x:
                fixed[k].append(x)
        for t in (0, 1):
            need(trace(step(x, t)[0]) == SHEET[t][z], 'sheet map')
        y = x
        for n in range(3):
            y = step(y, THETA[n])[0]
        need(trace(y) == 1, 'synchronization after 011')
        if z in (1, 4):
            for t in (0, 1):
                need(trace(step(x, t)[0]) == (4 + 2 * t) % P, 'X14 closure')
    counts = tuple(len(fixed[k]) for k in range(5))
    need(counts == (625, 25, 25, 1, 1), 'fixed-point counts')
    need(fixed[3] == [FIXED_D] and fixed[4] == [FIXED_E], 'fixed points d,e')
    return ('checkpoints=15625 involutions=%d sheet_t0=0,4,0,4,4 sheet_t1=2,1,1,3,1 '
            'fixed=625,25,25,1,1 synchronized_after_011=15625' % involutions)


def f2():
    a2 = mul(AF, AF)
    a3 = mul(a2, AF)
    a5 = mul(mul(a2, a2), AF)
    need(a5 == I4, 'A_f^5=I')
    need(mul(sub(I4, AF), sub(I4, a2)) == LM, 'L=(I-A_f)(I-A_f^2)')
    need(mul(AF, LM) == mul(LM, AF), 'A_f L=L A_f')
    need(mul(LM, LM) == scal(5, a3), 'L^2=5A_f^3')
    need(mul(a2, LM) == VINV, 'Vinv=A_f^2 L')
    need(mul(VINV, LM) == scal(5, I4) and mul(LM, VINV) == scal(5, I4), 'Vinv L=5I')
    need(mul(mul(transpose(LM), BF), LM) == scal(5, BF), 'L^t B_f L=5B_f')
    need(det(LM) == 25, 'det L')
    need(det(VH) == 1, 'det Vh')
    need(mul(LM, VH) == LVH, 'L Vh')
    cset = [y for y in PISTONS if in_c(y)]
    need(len(cset) == 25, '|C|')
    image = Counter(red(matvec(LM, x)) for x in PISTONS)
    need(set(image) == set(cset), 'residue image of L')
    need(set(image.values()) == {25}, 'residue preimages')
    lifts = 0
    for y in PISTONS:
        v = matvec(VINV, y)
        divisible = all(c % P == 0 for c in v)
        need(divisible == in_c(y), 'Vinv criterion')
        if divisible:
            need(matvec(LM, tuple(c // P for c in v)) == y, 'integral preimage')
            lifts += 1
    need(lifts == 25, 'integral lifts')
    return ('af_order=5 l_factor=EXACT l_square=5Af^3 vinv_l=5I energy_scale=5 det_l=25 '
            'det_vh=1 residue_image=25 preimages=25 vinv_criterion=625 integral_lifts=%d'
            % lifts)


def f3():
    kernel = []
    for p in PISTONS:
        wp = w_map(p)
        need(w_map(wp) == p, 'W involution')
        need(h(p) == ((wp[0] + 2 * wp[1]) % P, (wp[2] + 2 * wp[3]) % P), 'h via W')
        need((h(p) == HZERO) == in_c(wp), 'gate iff W in C')
        if h(p) == HZERO:
            kernel.append(p)
    need(len(kernel) == 25, 'ker h')
    need(sorted(w_map(p) for p in kernel) == [y for y in PISTONS if in_c(y)], 'W(ker h)=C')
    for x in STATES:
        need(generator(x, 0)[:4] == w_map(x[:4]), 'W is the piston action of a')
    need(energy((1, 0, 0, 0)) == 2 and energy(w_map((1, 0, 0, 0))) == 3, 'W not H-isometry')
    gate = [x for x in STATES if h(x) == HZERO]
    sheets = Counter(trace(x) for x in gate)
    need(len(gate) == 625, '|G|')
    need(all(sheets[s] == 125 for s in range(5)), '|G n X_s|')
    need(sheets[1] + sheets[4] == 250, '|G14|')
    return ('pistons=625 w_is_a_piston=YES ker_h=25 w_ker_onto_C=25 h_e0=2 h_we0=3 '
            'gate=625 per_sheet=125,125,125,125,125 g14=250')


def f4():
    for x in STATES:
        hx = h(x)
        p1, p4, p1p, p4p, q, r = x
        need(h(generator(x, 1)) == (-hx[1] % P, -hx[0] % P), 'b law')
        need(h(generator(x, 3)) == neg(hx) and h(generator(x, 4)) == neg(hx), 'd,e law')
        need(h(generator(x, 2)) == ((-hx[1] + r) % P, (-hx[0] - r) % P), 'c law')
        ha = h(generator(x, 0))
        need(ha == ((p1 + 2 * p4) % P, (p1p + 2 * p4p) % P), 'a law')
        need(ha == ((2 * hx[0] + 2 * p1) % P, (2 * hx[1] + 2 * p1p) % P), 'a law 2h form')
        for k in (1, 3, 4):
            need((h(generator(x, k)) == HZERO) == (hx == HZERO), 'b,d,e gate and complement')
    pairs = {(h(p), h(w_map(p))) for p in PISTONS}
    need(len(pairs) == 625, 'a pair bijection')
    other = (1, 3, 0, 0, 0, 0)
    need(h(ZERO) == HZERO and h(other) == HZERO, 'a witness gate')
    need(h(generator(ZERO, 0)) == HZERO and h(generator(other, 0)) == (2, 0), 'a witness split')
    gate = [x for x in STATES if h(x) == HZERO]
    a_keep = [x for x in gate if h(generator(x, 0)) == HZERO]
    need(len(a_keep) == 25 and all(x[:4] == (0, 0, 0, 0) for x in a_keep), 'a keeps gate')
    c_keep = [x for x in gate if h(generator(x, 2)) == HZERO]
    need(c_keep == [x for x in gate if x[5] == 0] and len(c_keep) == 125, 'c keeps gate')
    return ('checkpoints=15625 b=-Jh c=-Jh+(r,-r) d=-h e=-h a=2h+2(p1,p1p) a_pairs=625 '
            'a_h_only=NO a_keeps_gate=25 c_keeps_gate=125 bde_gate_and_complement=PRESERVED')


def f5():
    pairs = 0
    for x in STATES:
        z = trace(x)
        for t in (0, 1):
            y, k = step(x, t)
            kk, zz, name = TABLE[(z, t)]
            need(k == kk, 'branch generator')
            need(trace(y) == zz, 'branch trace')
            need(h(y) == law(name, x), 'branch h law')
            pairs += 1
    return 'branches=10 pairs=%d table=MATCH' % pairs


def f6():
    x14 = [x for x in STATES if trace(x) in (1, 4)]
    g14 = [x for x in x14 if h(x) == HZERO]
    need(len(x14) == 6250 and len(g14) == 250, 'X14,G14 sizes')
    pairs = 0
    fixed_found = []
    moved = []
    for t in (0, 1):
        target = (4 + 2 * t) % P
        for x in x14:
            y, k = step(x, t)
            need(trace(y) == target, 'absorbing sheet')
            need(k in (1, 3, 4), 'selected generator on X14')
            expected = neg(swap(h(x))) if k == 1 else neg(h(x))
            need(h(y) == expected, 'Klein law')
            need((h(y) == HZERO) == (h(x) == HZERO), 'gate and complement absorbed')
            pairs += 1
        image = Counter(step(x, t)[0] for x in g14)
        need(set(image) == {x for x in STATES if h(x) == HZERO and trace(x) == target},
             'image of G14')
        need(set(image.values()) == {2}, 'two preimages')
        fixed = [x for x in x14 if step(x, t)[0] == x]
        need(fixed == [FIXED_E if t == 0 else FIXED_D], 'fixed point on X14')
        need(h(fixed[0]) == HZERO, 'fixed point gated')
        fixed_found.append(fixed[0])
        moved.append(sum(1 for x in g14 if step(x, t)[0] != x))
    need(moved == [249, 249], 'moved gated points')
    complement = len(x14) - len(g14)
    return ('pairs=%d law=KLEIN g14_image=125x2 complement=%d fixed_t0=%s fixed_t1=%s '
            'moved=249,249' % (pairs, complement, ','.join(map(str, fixed_found[0])),
                               ','.join(map(str, fixed_found[1]))))


def f7():
    x14 = [x for x in STATES if trace(x) in (1, 4)]
    for x in x14:
        for t in (0, 1):
            need(vee(step(x, t)[0]) == neg(vee(x)), 'inherited V law')
    g14 = [x for x in x14 if h(x) == HZERO]
    via_v = [x for x in x14
             if (2 * vee(x)[0] + vee(x)[1]) % P == 0 and (2 * vee(x)[2] + vee(x)[3]) % P == 0]
    need(g14 == via_v, 'G14 = V^-1(S)')
    values = Counter(vee(x) for x in x14)
    need(len(values) == 625 and set(values.values()) == {10}, 'V preimages')
    fibres = Counter(frozenset((vee(x), neg(vee(x)))) for x in g14)
    whole = Counter(frozenset((vee(x), neg(vee(x)))) for x in x14)
    need(all(fibres[label] == whole[label] for label in fibres), 'whole R fibres in G14')
    sizes = sorted(fibres.values())
    need(len(fibres) == 13 and sizes == [10] + [20] * 12, 'R fibres of G14')
    return 'v_law=12500 g14=V^-1(S) v_preimages=10 r_fibres=13 sizes=1x10,12x20'


def prefix_expected(x0):
    s = trace(x0)
    p1, p4, p1p, p4p, q, r = x0
    h0 = h(x0)
    if s == 0:
        return (((p1 + 2 * p4) % P, (p1p + 2 * p4p) % P),
                ((-p1p - 2 * p4p + r) % P, (-p1 - 2 * p4 - r) % P),
                ((p1p + 2 * p4p - r) % P, (p1 + 2 * p4 + r) % P))
    if s == 1:
        return (neg(swap(h0)), h0, neg(h0))
    if s == 2:
        return (((-h0[1] + r) % P, (-h0[0] - r) % P), h0, neg(h0))
    return (neg(h0), swap(h0), neg(swap(h0)))


def f8():
    orbit = [ZERO]
    words = []
    for n in range(3):
        y, k = step(orbit[-1], THETA[n])
        orbit.append(y)
        words.append(k)
    need(orbit == [ZERO, ZERO, (2, 1, 2, 1, 1, 0), (0, 0, 1, 3, 1, 1)], 'zero start states')
    need(words == [0, 2, 4], 'zero start generators')
    need([trace(x) for x in orbit] == [0, 0, 2, 1], 'zero start traces')
    need(all(h(x) == HZERO for x in orbit) and orbit[3][5] == 1, 'zero start gate and r3')
    gated3 = Counter()
    gated_by_time = {s: [0, 0, 0, 0] for s in range(5)}
    permanent = []
    both = []
    only0 = only3 = 0
    for x0 in STATES:
        s = trace(x0)
        x = x0
        hs = [h(x0)]
        ks = []
        for n in range(3):
            x, k = step(x, THETA[n])
            ks.append(k)
            hs.append(h(x))
        need(tuple(ks) == WORDS[s], 'prefix word')
        need(trace(x) == 1, 'prefix synchronization')
        need(tuple(hs[1:]) == prefix_expected(x0), 'prefix h table')
        if hs[3] == HZERO:
            gated3[s] += 1
        if hs[0] == HZERO:
            for n in range(4):
                gated_by_time[s][n] += hs[n] == HZERO
            if all(v == HZERO for v in hs):
                permanent.append(x0)
        if s == 0:
            if hs[0] == HZERO and hs[3] == HZERO:
                both.append(x0)
            elif hs[0] == HZERO:
                only0 += 1
            elif hs[3] == HZERO:
                only3 += 1
    need(all(gated3[s] == 125 for s in range(5)), 'gated from n=3 per sheet')
    overlap = sorted((2 * r % P, r, 3 * r % P, 4 * r % P, 4 * r % P, r) for r in range(5))
    need(sorted(both) == overlap and only0 == 120 and only3 == 120, 'X0 overlap')
    expected_time = {0: [125, 5, 5, 5], 1: [125] * 4, 2: [125, 25, 125, 125],
                     3: [125] * 4, 4: [125] * 4}
    need(gated_by_time == expected_time, 'initially gated by time')
    per_sheet = Counter(trace(x) for x in permanent)
    need([per_sheet[s] for s in range(5)] == [1, 125, 25, 125, 125], 'permanent per sheet')
    need(len(permanent) == 401 and [x for x in permanent if trace(x) == 0] == [ZERO],
         'permanent total')
    return permanent, ('zero_start=a,c,e traces=0,0,2,1 r3=1 words=ace,bbd,cce,dbd,ebd '
                       'gated_at_3=125x5 x0_overlap=5,120,120 prefix_gated=1,125,25,125,125 '
                       'permanent=401')


def f9():
    x = ZERO
    for n in range(4096):
        need(h(x) == HZERO, 'zero orbit gated')
        if n >= 3:
            need(trace(x) in (1, 4), 'zero orbit synchronized')
        x = step(x, THETA[n])[0]
    need(h(x) == HZERO and trace(x) in (1, 4), 'zero orbit endpoint')
    horizon = 40
    for x0 in STATES:
        x = x0
        h3 = None
        orbit = None
        for n in range(horizon + 1):
            if n == 3:
                h3 = h(x)
                orbit = {h3, neg(h3), swap(h3), neg(swap(h3))}
            if n >= 3:
                need((h(x) == HZERO) == (h3 == HZERO), 'regression gate status')
                need(h(x) in orbit, 'regression Klein orbit')
            if n < horizon:
                x = step(x, THETA[n])[0]
    return 'regression_only zero_orbit=4097 initial=15625 horizon=%d' % horizon


def custody():
    root = Path(__file__).resolve().parent
    for line in (root / 'INPUTS.sha256').read_text(encoding='ascii').splitlines():
        if not line.strip():
            continue
        digest_hex, name = line.split(None, 1)
        name = name.strip().lstrip('*')
        actual = sha256((root / name).read_bytes()).hexdigest()
        if actual != digest_hex:
            sys.stderr.write('INTEGRITY STOP %s\n' % name)
            sys.exit(2)


def main():
    custody()
    permanent = None
    steps = (('F1', f1), ('F2', f2), ('F3', f3), ('F4', f4), ('F5', f5),
             ('F6', f6), ('F7', f7), ('F8', f8), ('F9', f9))
    for label, check in steps:
        try:
            out = check()
        except Fired as fired:
            print('%s FAIL %s' % (label, fired.args[0]))
            print('RESULT FAIL first=%s' % label)
            return
        if label == 'F8':
            permanent, out = out
        print('%s PASS %s' % (label, out))
    g14 = [x for x in STATES if trace(x) in (1, 4) and h(x) == HZERO]
    print('G14_SHA256 %s' % digest(g14))
    print('PERMANENT_SHA256 %s' % digest(permanent))
    print('RESULT PASS h_laws=EXACT a_law=NOT_H_ONLY gate_image=C all_time_gate=INDUCTION '
          'inherited_V_corollary=YES')


if __name__ == '__main__':
    main()
