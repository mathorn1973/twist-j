#!/usr/bin/env python3
"""Exact, standalone F1--F9 audit for P-U-AFRAME-GATE-AUDIT-1.

PUBLIC / NON-CANONICAL / L1. Author: A. M. Thorn. SPDX: Apache-2.0.
Definitions: Public Canon v102, a632c6a162dc87e60104d7a478e7650a6d5c4a1b,
DEF-NATIVE-WORD-CURVATURE-CLASS; FIELD-CHAIN-FIRST-WORK shared proof 2;
U-NATIVE-INVARIANT-AND-NOWRITE. The source manifest binds the definitions.

The affine rows, branch table and prefix table were written from those
definitions and the exposed preregistration, without reading the submitted
proof, verifier or scientific output. No mutable file is a runtime input.
All scientific computation starts in main(). A frozen predicate failure
prints a concrete witness and RESULT FAIL, then returns exit status zero.
An uncaught exception is an execution failure, not a scientific negative.
F9 is finite regression only. The all-time claim requires the written
induction whose complete base and one-step premises are audited here.
"""

from collections import Counter, defaultdict
from hashlib import sha256
from itertools import permutations, product
import json


P = 5
ZERO2 = (0, 0)
ZERO4 = (0, 0, 0, 0)
ZERO6 = (0, 0, 0, 0, 0, 0)
NAMES = "abcde"

# A row is (integer offset, ((input coordinate, coefficient), ...)).
# Coordinate order is (p1,p4,p1p,p4p,q,r). Reducing only at the end of a
# row makes the integer affine source explicit and independent of h laws.
GENERATORS = (
    ((0, ((1, 1),)), (0, ((0, 1),)),
     (0, ((3, 1),)), (0, ((2, 1),)),
     (0, ((4, 1),)), (0, ((5, 1),))),
    ((0, ((2, -1),)), (0, ((3, -1),)),
     (0, ((0, -1),)), (0, ((1, -1),)),
     (0, ((4, -1),)), (0, ((5, -1),))),
    ((2, ((2, -1),)), (1, ((3, -1), (5, 1))),
     (2, ((0, -1),)), (1, ((1, -1), (5, -1))),
     (1, ((4, -1),)), (0, ((5, -1),))),
    ((2, ((0, -1),)), (1, ((1, -1),)),
     (3, ((2, -1),)), (4, ((3, -1),)),
     (1, ((4, -1),)), (1, ((5, -1),))),
    ((2, ((0, -1),)), (1, ((1, -1),)),
     (3, ((2, -1),)), (4, ((3, -1),)),
     (2, ((4, -1),)), (1, ((5, -1),))),
)

A_F = ((1, 0, 1, 0), (0, 1, 0, 1),
       (-2, 1, -1, 1), (1, -3, 1, -2))
B_F = ((4, -2, 2, -1), (-2, 6, -1, 3),
       (2, -1, 2, 0), (-1, 3, 0, 2))
L = ((1, -3, -1, -2), (-3, 4, -2, 1),
     (0, 5, 1, 2), (5, -5, 2, -1))
V_INV = ((1, 2, 1, 2), (2, -1, 2, -1),
         (0, -5, 1, -3), (-5, 5, -3, 4))
V_H = ((1, 1, 1, 1), (2, 1, 2, 1),
       (0, -1, 1, 0), (-5, -2, -3, -1))
TRIANGULAR_IMAGE = ((5, 3, 0, 0), (0, 1, 0, 0),
                    (0, 0, 5, 3), (0, 0, 0, 1))
I4 = ((1, 0, 0, 0), (0, 1, 0, 0),
      (0, 0, 1, 0), (0, 0, 0, 1))

# Derived before execution from k=s+2t and the five affine trace/h laws.
# Each row is (selected generator index, next trace, h expression).
# H=h(x), K=h(a x), R=(r,-r), J exchanges the two h coordinates.
BRANCH_ROWS = (
    ((0, 0, "K"), (1, 4, "-JH"), (2, 0, "-JH+R"),
     (3, 4, "-H"), (4, 4, "-H")),
    ((2, 2, "-JH+R"), (3, 1, "-H"), (4, 1, "-H"),
     (0, 3, "K"), (1, 1, "-JH")),
)
PREFIX_WORDS = ("ace", "bbd", "cce", "dbd", "ebd")


class PredicateFailure(Exception):
    """A scientific falsifier, as distinct from an execution error."""

    def __init__(self, falsifier, predicate, witness):
        super().__init__(predicate)
        self.falsifier = falsifier
        self.predicate = predicate
        self.witness = witness


def require(condition, falsifier, predicate, witness):
    if not condition:
        raise PredicateFailure(falsifier, predicate, witness)


def equal(actual, expected, falsifier, predicate, **context):
    if actual != expected:
        raise PredicateFailure(
            falsifier, predicate,
            dict(context, actual=actual, expected=expected),
        )


def native(generator, x):
    return tuple((offset + sum(coefficient * x[column]
                               for column, coefficient in terms)) % P
                 for offset, terms in GENERATORS[generator])


def h(x):
    return ((2 * x[0] + x[1]) % P, (2 * x[2] + x[3]) % P)


def k(x):
    return ((x[0] + 2 * x[1]) % P, (x[2] + 2 * x[3]) % P)


def swap2(v):
    return (v[1], v[0])


def neg(v):
    return tuple(-a % P for a in v)


def add(v, w):
    return tuple((a + b) % P for a, b in zip(v, w))


def residue(v):
    return tuple(a % P for a in v)


def W(p):
    return (p[1], p[0], p[3], p[2])


def in_C(y):
    return (y[0] + 2 * y[1]) % P == 0 and (y[2] + 2 * y[3]) % P == 0


def in_S(v):
    return (2 * v[0] + v[1]) % P == 0 and (2 * v[2] + v[3]) % P == 0


def invariant_V(x):
    z = sum(x) % P
    chi = {1: 1, 4: -1}[z]
    return ((x[0] + x[2]) % P, (x[1] + x[3]) % P,
            chi * (x[0] - x[2] - 2) % P,
            chi * (x[1] - x[3] - 1) % P)


def theta(n):
    return n.bit_count() % 2


def matrix_product(a, b):
    return tuple(tuple(sum(a[i][q] * b[q][j] for q in range(len(b)))
                       for j in range(len(b[0])))
                 for i in range(len(a)))


def matrix_vector(a, v):
    return tuple(sum(coefficient * value for coefficient, value in zip(row, v))
                 for row in a)


def matrix_subtract(a, b):
    return tuple(tuple(x - y for x, y in zip(ra, rb))
                 for ra, rb in zip(a, b))


def matrix_scale(a, factor):
    return tuple(tuple(factor * x for x in row) for row in a)


def transpose(a):
    return tuple(zip(*a))


def matrix_power(a, exponent):
    result = I4
    for _ in range(exponent):
        result = matrix_product(result, a)
    return result


def determinant(a):
    # The 4! Leibniz terms avoid any pivoting or division convention.
    total = 0
    for permutation in permutations(range(len(a))):
        inversions = sum(permutation[i] > permutation[j]
                         for i in range(len(a)) for j in range(i + 1, len(a)))
        term = -1 if inversions % 2 else 1
        for i, j in enumerate(permutation):
            term *= a[i][j]
        total += term
    return total


def twice_energy(y):
    return sum(x * value for x, value in zip(y, matrix_vector(B_F, y)))


def tuple_digest(points):
    payload = "".join(",".join(str(c) for c in point) + "\n"
                      for point in sorted(points)).encode("ascii")
    return sha256(payload).hexdigest()


class Carrier:
    """Full lexicographic carriers and actual affine transition tables."""

    def __init__(self):
        self.states = tuple(product(range(P), repeat=6))
        self.pistons = tuple(product(range(P), repeat=4))
        self.index = {x: i for i, x in enumerate(self.states)}
        self.z = tuple(sum(x) % P for x in self.states)
        self.h = tuple(h(x) for x in self.states)
        self.gated = tuple(value == ZERO2 for value in self.h)
        self.images = tuple(tuple(self.index[native(g, x)] for x in self.states)
                            for g in range(P))
        self.transitions = tuple(
            tuple(self.images[(self.z[i] + 2 * t) % P][i]
                  for i in range(len(self.states))) for t in range(2))
        self.sheet14 = tuple(i for i, z in enumerate(self.z) if z in (1, 4))
        self.gate14 = tuple(i for i in self.sheet14 if self.gated[i])
        self.C = {y for y in self.pistons if in_C(y)}
        self.prefix3 = None
        self.permanent = None


def f1(m):
    fid = "F1"
    equal(len(m.states), 15625, fid, "full checkpoint carrier")
    equal(len(m.pistons), 625, fid, "full piston carrier")
    fixed = [[] for _ in range(P)]
    sheet_maps = [[set() for _ in range(P)] for _ in range(2)]
    for i, x in enumerate(m.states):
        z = m.z[i]
        expected_traces = residue((z, -z, 2 - z, 2 - z, 3 - z))
        q, r = x[4:]
        expected_qr = ((q, r), residue((-q, -r)), residue((1 - q, -r)),
                       residue((1 - q, 1 - r)), residue((2 - q, 1 - r)))
        for g in range(P):
            image = m.images[g][i]
            equal(m.images[g][image], i, fid, "generator involution",
                  generator=NAMES[g], x=x, image=m.states[image])
            equal(m.z[image], expected_traces[g], fid, "generator trace law",
                  generator=NAMES[g], x=x)
            equal(m.states[image][4:], expected_qr[g], fid, "generator q,r law",
                  generator=NAMES[g], x=x)
            if image == i:
                fixed[g].append(x)
        for t in range(2):
            image = m.transitions[t][i]
            sheet_maps[t][z].add(m.z[image])
            if z in (1, 4):
                equal(m.z[image], (4 + 2 * t) % P, fid,
                      "selected synchronized sheet", x=x, t=t)
        image3 = m.transitions[1][m.transitions[1][m.transitions[0][i]]]
        equal(m.z[image3], 1, fid, "trace synchronized after 0,1,1", x=x)
    equal(tuple(len(points) for points in fixed), (625, 25, 25, 1, 1),
          fid, "fixed-point census")
    equal(fixed[3], [(1, 3, 4, 2, 3, 3)], fid, "d fixed point")
    equal(fixed[4], [(1, 3, 4, 2, 1, 3)], fid, "e fixed point")
    for t, expected in enumerate(((0, 4, 0, 4, 4), (2, 1, 1, 3, 1))):
        for z in range(P):
            equal(sorted(sheet_maps[t][z]), [expected[z]], fid,
                  "complete selected sheet table", t=t, z=z)
    equal(tuple(theta(n) for n in range(3)), (0, 1, 1), fid,
          "actual driver prefix")
    print("F1 PASS states=15625 generator_cases=78125 selector_cases=31250")


def f2(m):
    fid = "F2"
    identities = (
        ("A_f^5=I", matrix_power(A_F, 5), I4),
        ("L=(I-A_f)(I-A_f^2)", L,
         matrix_product(matrix_subtract(I4, A_F),
                        matrix_subtract(I4, matrix_power(A_F, 2)))),
        ("A_f L=L A_f", matrix_product(A_F, L), matrix_product(L, A_F)),
        ("L^2=5A_f^3", matrix_power(L, 2), matrix_scale(matrix_power(A_F, 3), P)),
        ("Vinv=A_f^2 L", V_INV, matrix_product(matrix_power(A_F, 2), L)),
        ("Vinv L=5I", matrix_product(V_INV, L), matrix_scale(I4, P)),
        ("L Vinv=5I", matrix_product(L, V_INV), matrix_scale(I4, P)),
        ("L^t B_f L=5B_f", matrix_product(matrix_product(transpose(L), B_F), L),
         matrix_scale(B_F, P)),
        ("L Vh triangular image", matrix_product(L, V_H), TRIANGULAR_IMAGE),
    )
    for name, actual, expected in identities:
        equal(actual, expected, fid, name)
    equal(determinant(L), 25, fid, "det L")
    equal(determinant(V_H), 1, fid, "det Vh")
    image_counts = Counter(residue(matrix_vector(L, y)) for y in m.pistons)
    equal(sorted(image_counts), sorted(m.C), fid, "L residue image equals C")
    equal(len(m.C), 25, fid, "C cardinality")
    for y in sorted(image_counts):
        equal(image_counts[y], 25, fid, "uniform L residue preimages", y=y)
    for y in m.pistons:
        numerator = matrix_vector(V_INV, y)
        integral = all(value % P == 0 for value in numerator)
        equal(integral, in_C(y), fid, "Vinv residue kernel iff C", y=y,
              numerator=numerator)
        if in_C(y):
            preimage = tuple(value // P for value in numerator)
            equal(matrix_vector(L, preimage), y, fid,
                  "exact integer inverse on C representatives", y=y,
                  preimage=preimage)
    print("F2 PASS matrix_identities=9 determinants=2 residues=625 image=25 preimages=25")


def f3(m):
    fid = "F3"
    image_of_kernel = []
    for p in m.pistons:
        wp = W(p)
        equal(W(wp), p, fid, "W involution", p=p)
        a_piston = m.states[m.images[0][m.index[p + (0, 0)]]][:4]
        equal(wp, a_piston, fid, "W equals piston action of a", p=p)
        equal(h(p), ((wp[0] + 2 * wp[1]) % P,
                     (wp[2] + 2 * wp[3]) % P), fid, "comparison h formula", p=p)
        equal(h(p) == ZERO2, in_C(wp), fid, "gate iff W in C", p=p)
        if h(p) == ZERO2:
            image_of_kernel.append(wp)
    equal(len(image_of_kernel), 25, fid, "piston gate cardinality")
    equal(len(set(image_of_kernel)), 25, fid, "W injective on piston gate")
    equal(sorted(image_of_kernel), sorted(m.C), fid, "W gate image equals C")
    e0 = (1, 0, 0, 0)
    equal(twice_energy(e0), 4, fid, "H(e0)=2")
    equal(twice_energy(W(e0)), 6, fid, "H(W e0)=3")
    equal(sum(m.gated), 625, fid, "full gate cardinality")
    gate_sheets = Counter(m.z[i] for i in range(len(m.states)) if m.gated[i])
    equal(tuple(gate_sheets[s] for s in range(P)), (125,) * P, fid,
          "gate cardinality on every sheet")
    equal(len(m.gate14), 250, fid, "G14 cardinality")
    print("F3 PASS pistons=625 kernel_h=25 G=625 sheet_gates=125,125,125,125,125 G14=250")


def f4(m):
    fid = "F4"
    for i, x in enumerate(m.states):
        H = m.h[i]
        R = (x[5], -x[5] % P)
        expected = (k(x), neg(swap2(H)), add(neg(swap2(H)), R), neg(H), neg(H))
        for g in range(P):
            equal(m.h[m.images[g][i]], expected[g], fid,
                  "complete generator h law", generator=NAMES[g], x=x)
        equal(expected[0], residue((2 * H[0] + 2 * x[0],
                                    2 * H[1] + 2 * x[2])), fid,
              "a law equals 2h+2(p1,p1p)", x=x)
        for g in (1, 3, 4):
            equal(m.gated[m.images[g][i]], m.gated[i], fid,
                  "generator preserves gate and complement", generator=NAMES[g], x=x)
    pair_values = {(h(p), k(p)) for p in m.pistons}
    equal(len(pair_values), 625, fid, "piston -> (h,h after a) bijective")
    witness = (1, 3, 0, 0, 0, 0)
    equal(h(ZERO6), ZERO2, fid, "zero witness h")
    equal(h(witness), ZERO2, fid, "nonzero witness same h", x=witness)
    equal(m.h[m.images[0][m.index[ZERO6]]], ZERO2, fid, "a zero witness")
    equal(m.h[m.images[0][m.index[witness]]], (2, 0), fid,
          "a distinguishes equal h witness", x=witness)
    a_kept = {i for i in range(len(m.states))
              if m.gated[i] and m.gated[m.images[0][i]]}
    zero_piston = {i for i, x in enumerate(m.states) if x[:4] == ZERO4}
    equal(sorted(a_kept), sorted(zero_piston), fid, "a gated survivors exactly zero piston")
    equal(len(a_kept), 25, fid, "a gated survivor count")
    c_kept = {i for i in range(len(m.states))
              if m.gated[i] and m.gated[m.images[2][i]]}
    gate_r_zero = {i for i, x in enumerate(m.states) if m.gated[i] and x[5] == 0}
    equal(sorted(c_kept), sorted(gate_r_zero), fid, "c gated survivors exactly r=0")
    equal(len(c_kept), 125, fid, "c gated survivor count")
    print("F4 PASS generator_cases=78125 piston_pair_values=625 a_survivors=25 c_survivors=125")


def expected_branch_h(symbol, x):
    H = h(x)
    if symbol == "K":
        return k(x)
    if symbol == "-JH":
        return neg(swap2(H))
    if symbol == "-JH+R":
        return add(neg(swap2(H)), (x[5], -x[5] % P))
    if symbol == "-H":
        return neg(H)
    raise ValueError("unrecognized frozen branch expression")


def f5(m):
    fid = "F5"
    row_counts = [[0] * P for _ in range(2)]
    for t in range(2):
        for i, x in enumerate(m.states):
            z = m.z[i]
            g, next_z, expression = BRANCH_ROWS[t][z]
            equal((z + 2 * t) % P, g, fid, "ten-row selector index", t=t, x=x)
            image = m.transitions[t][i]
            equal(image, m.images[g][i], fid, "selected generator map", t=t, x=x)
            equal(m.z[image], next_z, fid, "ten-row next trace", t=t, x=x)
            equal(m.h[image], expected_branch_h(expression, x), fid,
                  "ten-row next h", t=t, x=x, expression=expression)
            row_counts[t][z] += 1
    equal(row_counts, [[3125] * P, [3125] * P], fid, "complete ten-row coverage")
    print("F5 PASS selector_cases=31250 rows=10 cases_per_row=3125")


def f6(m):
    fid = "F6"
    equal(len(m.sheet14), 6250, fid, "synchronized carrier cardinality")
    for t in range(2):
        gate_images = Counter()
        fixed = []
        moved_gate = 0
        for i in m.sheet14:
            x = m.states[i]
            g = (m.z[i] + 2 * t) % P
            image = m.transitions[t][i]
            equal(m.z[image], (4 + 2 * t) % P, fid,
                  "absorbing next sheet", t=t, x=x)
            require(g in (1, 3, 4), fid, "absorbing generator is b,d,e",
                    {"t": t, "x": x, "generator": NAMES[g]})
            wanted = neg(swap2(m.h[i])) if g == 1 else neg(m.h[i])
            equal(m.h[image], wanted, fid, "absorbing h step", t=t, x=x)
            equal(m.gated[image], m.gated[i], fid,
                  "G14 and complement each invariant", t=t, x=x)
            if image == i:
                fixed.append(x)
            if m.gated[i]:
                gate_images[image] += 1
                moved_gate += image != i
        wanted_image = [i for i in m.gate14 if m.z[i] == (4 + 2 * t) % P]
        equal(sorted(gate_images), sorted(wanted_image), fid,
              "T_t(G14) equals full target gate sheet", t=t)
        for image in sorted(gate_images):
            equal(gate_images[image], 2, fid, "exactly two gate preimages",
                  t=t, image=m.states[image])
        expected_fixed = (1, 3, 4, 2, 1, 3) if t == 0 else (1, 3, 4, 2, 3, 3)
        equal(fixed, [expected_fixed], fid, "one synchronized fixed point", t=t)
        require(m.gated[m.index[expected_fixed]], fid, "fixed point belongs to G14",
                {"t": t, "fixed": expected_fixed})
        equal(moved_gate, 249, fid, "moved G14 checkpoints", t=t)
    print("F6 PASS synchronized_cases=12500 images_per_bit=125 preimages=2 fixed_per_bit=1 moved_gate=249")


def f7(m):
    fid = "F7"
    values = {i: invariant_V(m.states[i]) for i in m.sheet14}
    v_fibres = defaultdict(list)
    r_fibres = defaultdict(list)
    for i in m.sheet14:
        x = m.states[i]
        v = values[i]
        v_fibres[v].append(i)
        r_fibres[min(v, neg(v))].append(i)
        equal(m.gated[i], in_S(v), fid, "G14 is V-preimage of S", x=x, V=v)
        for t in range(2):
            image = m.transitions[t][i]
            equal(values[image], neg(v), fid, "V(next)=-V", x=x, t=t)
    equal(sorted(v_fibres), list(m.pistons), fid, "V reaches every F5^4 value")
    for v in sorted(v_fibres):
        equal(len(v_fibres[v]), 10, fid, "uniform V preimages", V=v)
    gate_r_fibres = []
    for label in sorted(r_fibres):
        fibre = r_fibres[label]
        gate_count = sum(m.gated[i] for i in fibre)
        require(gate_count in (0, len(fibre)), fid, "G14 is a union of whole R fibres",
                {"R_label": label, "fibre_size": len(fibre), "gate_count": gate_count})
        if gate_count:
            gate_r_fibres.append((label, fibre))
    equal(len(gate_r_fibres), 13, fid, "gated R fibre count")
    equal(sorted(len(fibre) for _, fibre in gate_r_fibres), [10] + [20] * 12,
          fid, "gated R fibre sizes")
    print("F7 PASS invariant_cases=12500 V_values=625 V_preimages=10 gated_R_fibres=13 sizes=10,12*20")


def prefix_h_values(z, x):
    """Hand-composed h expressions for the actual bits 0,1,1."""
    H = h(x)
    K = k(x)
    JH = swap2(H)
    R = (x[5], -x[5] % P)
    if z == 0:  # a,c,e: r is unchanged by a, and c contributes R.
        return (K, add(neg(swap2(K)), R), add(swap2(K), neg(R)))
    if z == 1:  # b,b,d: the two b maps restore the complete state.
        return (neg(JH), H, neg(H))
    if z == 2:  # c,c,e: the two c maps restore the complete state.
        return (add(neg(JH), R), H, neg(H))
    if z in (3, 4):  # d,b,d or e,b,d; both have h signs -,J,-J.
        return (neg(H), JH, neg(JH))
    raise ValueError("invalid checkpoint trace")


def f8(m):
    fid = "F8"
    bits = tuple(theta(n) for n in range(3))
    zero_prefix = [m.index[ZERO6]]
    zero_word = ""
    for t in bits:
        i = zero_prefix[-1]
        zero_word += NAMES[(m.z[i] + 2 * t) % P]
        zero_prefix.append(m.transitions[t][i])
    expected_zero = (ZERO6, ZERO6, (2, 1, 2, 1, 1, 0), (0, 0, 1, 3, 1, 1))
    equal(tuple(m.states[i] for i in zero_prefix), expected_zero, fid,
          "zero-orbit exact four checkpoints")
    equal(zero_word, "ace", fid, "zero-orbit first generators")
    equal(tuple(m.z[i] for i in zero_prefix), (0, 0, 2, 1), fid,
          "zero-orbit first traces")
    equal(tuple(m.h[i] for i in zero_prefix), (ZERO2,) * 4, fid,
          "zero-orbit gated prefix")
    equal(m.states[zero_prefix[3]][5], 1, fid, "zero-orbit r3=1")

    prefix3 = []
    h3_counts = [0] * P
    individual = [[0] * 4 for _ in range(P)]
    all_four_counts = [0] * P
    permanent = []
    overlap0 = []
    initial_gate0 = set()
    future_gate0 = set()
    for i, x in enumerate(m.states):
        z = m.z[i]
        prefix = [i]
        word = ""
        for t in bits:
            previous = prefix[-1]
            word += NAMES[(m.z[previous] + 2 * t) % P]
            prefix.append(m.transitions[t][previous])
        equal(word, PREFIX_WORDS[z], fid, "complete prefix word by initial sheet", x=x)
        equal(tuple(m.h[j] for j in prefix[1:]), prefix_h_values(z, x), fid,
              "complete prefix h table", x=x)
        equal(m.z[prefix[3]], 1, fid, "complete prefix trace3", x=x)
        prefix3.append(prefix[3])
        gate_flags = tuple(m.gated[j] for j in prefix)
        h3_counts[z] += gate_flags[3]
        if gate_flags[0]:
            # These are four separate intersections with the initial gate.
            # They are deliberately not cumulative prefix intersections.
            for n in range(4):
                individual[z][n] += gate_flags[n]
        if all(gate_flags):
            permanent.append(i)
            all_four_counts[z] += 1
        if z == 0:
            if gate_flags[0]:
                initial_gate0.add(i)
            if gate_flags[3]:
                future_gate0.add(i)
            if gate_flags[0] and gate_flags[3]:
                overlap0.append(x)
    equal(h3_counts, [125] * P, fid, "h3 gate census on every initial sheet")
    expected_overlap = sorted(residue((2 * r, r, 3 * r, 4 * r, 4 * r, r))
                              for r in range(P))
    equal(sorted(overlap0), expected_overlap, fid, "X0 initial/future gate overlap parametrization")
    equal(len(overlap0), 5, fid, "X0 initial/future gate overlap count")
    equal(len(initial_gate0 - future_gate0), 120, fid, "X0 initial-only gate count")
    equal(len(future_gate0 - initial_gate0), 120, fid, "X0 future-only gate count")
    equal(individual, [[125, 5, 5, 5], [125] * 4, [125, 25, 125, 125],
                       [125] * 4, [125] * 4], fid,
          "separate boundary gate counts conditioned on initial gate")
    equal(all_four_counts, [1, 125, 25, 125, 125], fid, "gate at all four boundaries by sheet")
    equal(len(permanent), 401, fid, "permanently gated initial census")
    equal([m.states[i] for i in permanent if m.z[i] == 0], [ZERO6], fid,
          "unique X0 permanently gated initial checkpoint")
    m.prefix3 = tuple(prefix3)
    m.permanent = tuple(permanent)
    print("F8 PASS initial_states=15625 future_gate=625 X0_overlap=5 permanent=401 by_sheet=1,125,25,125,125")
    print("DIGEST G14 rows=250 sha256=" + tuple_digest(m.states[i] for i in m.gate14))
    print("DIGEST PERMANENT_INITIAL rows=401 sha256=" + tuple_digest(m.states[i] for i in m.permanent))


def f9(m):
    fid = "F9"
    i = m.index[ZERO6]
    for n in range(4097):
        equal(m.h[i], ZERO2, fid, "zero orbit remains gated in finite regression",
              n=n, x=m.states[i])
        if n >= 3:
            require(m.z[i] in (1, 4), fid, "zero orbit synchronized in finite regression",
                    {"n": n, "x": m.states[i], "trace": m.z[i]})
        if n < 4096:
            i = m.transitions[theta(n)][i]
    for initial, x0 in enumerate(m.states):
        H3 = m.h[m.prefix3[initial]]
        allowed = {H3, neg(H3), swap2(H3), neg(swap2(H3))}
        i = initial
        for n in range(41):
            if n >= 3:
                equal(m.gated[i], H3 == ZERO2, fid, "finite all-initial gate equivalence",
                      initial=x0, n=n, x=m.states[i], h3=H3)
                require(m.h[i] in allowed, fid, "finite all-initial signed-swap h orbit",
                        {"initial": x0, "n": n, "x": m.states[i],
                         "h": m.h[i], "h3": H3, "allowed": sorted(allowed)})
            if n < 40:
                i = m.transitions[theta(n)][i]
    print("F9 PASS finite_regression_only zero_checkpoints=4097 all_initial_checkpoints=640625 synchronized_checks=593750")


def main():
    print("PROBE P-U-AFRAME-GATE-AUDIT-1")
    print("SCOPE PUBLIC NON-CANONICAL L1 exact_finite_audit")
    try:
        carrier = Carrier()
        for check in (f1, f2, f3, f4, f5, f6, f7, f8, f9):
            check(carrier)
    except PredicateFailure as failure:
        print(failure.falsifier + " FAIL predicate=" + failure.predicate)
        print("WITNESS " + json.dumps(failure.witness, sort_keys=True,
                                      separators=(",", ":"), ensure_ascii=True))
        print("RESULT FAIL")
        return 0
    print("RESULT PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
