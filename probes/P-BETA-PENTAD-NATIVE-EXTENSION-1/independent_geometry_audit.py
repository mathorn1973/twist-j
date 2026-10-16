"""Exact, independent finite check of the bracket -> pentad -> binary bridge.

All arithmetic is in F_5 or F_2.  No external dependencies.  This is an
analysis witness, not a Canon registration or a verification of native U.
"""

from collections import Counter
from itertools import combinations, permutations, product
import json

B = ((2, 4, 0), (4, 2, 4), (0, 4, 2))
BINV = ((2, 3, 4), (3, 1, 3), (4, 3, 2))
I3 = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
R = ((3, 2, 2), (0, 0, 4), (2, 2, 2))
P = ((1, 1, 3), (0, 2, 0), (2, 1, 4))
PINV = ((3, 4, 4), (0, 3, 0), (1, 1, 2))


def mv(m, x):
    return tuple(sum(a * b for a, b in zip(row, x)) % 5 for row in m)


def mm(a, b):
    return tuple(tuple(sum(x * y for x, y in zip(row, col)) % 5
                       for col in zip(*b)) for row in a)


def transpose(a):
    return tuple(zip(*a))


def det(m):
    a, b, c = m[0]
    d, e, f = m[1]
    g, h, i = m[2]
    return (a * (e * i - f * h) - b * (d * i - f * g)
            + c * (d * h - e * g)) % 5


def bracket(x, y):
    a, b, c = x
    d, e, f = y
    return mv(BINV, ((b * f - c * e) % 5,
                     (c * d - a * f) % 5,
                     (a * e - b * d) % 5))


def form(x, y):
    return sum(a * b for a, b in zip(x, mv(B, y))) % 5


def q(x):
    return form(x, x)


def projective(x):
    lead = next(a for a in x if a)
    return tuple(a * pow(lead, -1, 5) % 5 for a in x)


def apply_frame(m, frame):
    return frozenset(projective(mv(m, x)) for x in frame)


def permutation_parity(p):
    return sum(p[i] > p[j] for i in range(len(p))
               for j in range(i + 1, len(p))) % 2


def matrix_order(m):
    z = I3
    for n in range(1, 121):
        z = mm(z, m)
        if z == I3:
            return n
    raise AssertionError("Order exceeds group size")


assert det(B) == 4 and mm(B, BINV) == I3
assert det(R) == 2 and mm(transpose(R), mm(B, R)) == I3
assert det(P) == 1 and mm(P, PINV) == I3

# The triple-product identity is trilinear, so these 27 checks are exhaustive.
for x, y, z in product(I3, repeat=3):
    rhs = tuple((form(x, y) * zz - form(x, z) * yy) % 5
                for yy, zz in zip(y, z))
    assert bracket(x, bracket(y, z)) == rhs

lines = sorted({projective(x) for x in product(range(5), repeat=3) if any(x)})
square_lines = [x for x in lines if q(x) in (1, 4)]
frames_enumerated = {frozenset(t) for t in combinations(square_lines, 3)
                     if all(form(x, y) == 0 for x, y in combinations(t, 2))}
assert len(lines) == 31 and len(square_lines) == 15
assert len(frames_enumerated) == 5
assert len(set().union(*frames_enumerated)) == 15
assert all(sum(form(x, y) == 0 for y in square_lines if y != x) == 2
           for x in square_lines)

# Use explicit labels only to print matrices and permutations.
labels = ["F0", "F++", "F+-", "F-+", "F--"]
frames = [frozenset(projective(mv(R, x)) for x in I3)]
for s2, s3 in ((1, 1), (1, 4), (4, 1), (4, 4)):
    s = (1, s2, s3)
    vectors = [tuple((2 if i == j else 1) * s[j] % 5
                     for j in range(3)) for i in range(3)]
    assert all(sum(x * x for x in v) % 5 == 1 for v in vectors)
    frames.append(frozenset(projective(mv(R, x)) for x in vectors))
assert set(frames) == frames_enumerated

autos = {}
for a, b, c, d in product(range(5), repeat=4):
    delta = (a * d - b * c) % 5
    if not delta:
        continue
    m = ((a * a, -2 * a * b, -b * b),
         (-a * c, a * d + b * c, b * d),
         (-c * c, 2 * c * d, d * d))
    m = tuple(tuple(pow(delta, -1, 5) * x % 5 for x in row) for row in m)
    C = mm(P, mm(m, PINV))
    assert det(C) == 1 and mm(transpose(C), mm(B, C)) == B
    for x, y in product(I3, repeat=2):
        assert mv(C, bracket(x, y)) == bracket(mv(C, x), mv(C, y))
    action = tuple(frames.index(apply_frame(C, frame)) for frame in frames)
    assert permutation_parity(action) == (delta not in (1, 4))
    autos[C] = action

assert len(autos) == 120 and len(set(autos.values())) == 120
assert sum(permutation_parity(p) == 0 for p in autos.values()) == 60

# An independent orthonormal-column enumeration checks completeness in SO.
unit = [x for x in product(range(5), repeat=3) if sum(a * a for a in x) % 5 == 1]
assert len(unit) == 30
rinv = mm(transpose(R), B)
so = set()
for x in unit:
    for y in unit:
        if sum(a * b for a, b in zip(x, y)) % 5:
            continue
        for z in unit:
            if (sum(a * b for a, b in zip(x, z)) % 5
                    or sum(a * b for a, b in zip(y, z)) % 5):
                continue
            m = transpose((x, y, z))
            if det(m) == 1:
                so.add(mm(R, mm(m, rinv)))
assert so == set(autos)

transposition = ((4, 0, 4), (0, 4, 3), (0, 0, 1))
assert autos[transposition] == (1, 0, 2, 3, 4)
assert matrix_order(transposition) == 2
order_four = ((0, 0, 1), (0, 1, 0), (4, 1, 0))
assert matrix_order(order_four) == 4

# The already-canonical public Phi, expressed in the difference basis.
phi = ((0, 4, 1), (0, 4, 0), (1, 4, 0))
assert phi in autos and matrix_order(phi) == 2

# Binary carrier: even subsets of the intrinsically defined five frames.
E = [a for a in range(32) if a.bit_count() % 2 == 0]


def q2(a):
    assert a in E
    return (a.bit_count() // 2) % 2


def b2(a, b):
    return (a & b).bit_count() % 2


singular = [31 ^ (1 << i) for i in range(5)]
assert {a for a in E if a and q2(a) == 0} == set(singular)
assert len(E) == 16
assert all(q2(a ^ b) ^ q2(a) ^ q2(b) == b2(a, b) for a, b in product(E, repeat=2))
assert all(any(b2(a, b) for b in E) for a in E if a)

coordinate_to_E = {}
for x in range(16):
    a = 0
    for i in range(4):
        if x & (1 << i):
            a ^= singular[i]
    coordinate_to_E[x] = a
    carry = ((x.bit_count() * (x.bit_count() - 1)) // 2) % 2
    assert q2(a) == carry
assert set(coordinate_to_E.values()) == set(E)
assert coordinate_to_E[15] == singular[4]
for omitted in range(5):
    four = [a for i, a in enumerate(singular) if i != omitted]
    combinations_of_four = {0}
    for a in four:
        combinations_of_four |= {b ^ a for b in combinations_of_four.copy()}
    assert combinations_of_four == set(E)


def act_binary(p, a):
    return sum(1 << p[i] for i in range(5) if a & (1 << i))


binary_actions = set()
for p in autos.values():
    action = tuple(act_binary(p, a) for a in E)
    assert all(q2(a) == q2(b) for a, b in zip(E, action))
    assert all(act_binary(p, a ^ b) == (act_binary(p, a) ^ act_binary(p, b))
               for a, b in product(E, repeat=2))
    assert all(act_binary(p, singular[i]) == singular[p[i]] for i in range(5))
    binary_actions.add(action)
assert len(binary_actions) == 120

# Every binary isometry is determined by its action on the five singular
# vectors; checking all their permutations therefore exhausts O(E,q2).
all_binary_actions = {tuple(act_binary(p, a) for a in E)
                      for p in permutations(range(5))}
assert binary_actions == all_binary_actions


# Common A4 lattice bridge: its residual quotient at 5 and reduction at 2.
def T0_to_difference(x):
    assert sum(x) % 5 == 0
    return ((x[1] - x[0]) % 5,
            (x[1] + x[2] - 2 * x[0]) % 5,
            (x[1] + x[2] + x[3] - 3 * x[0]) % 5)


def lift_difference(v):
    a, b, c = v
    return (0, a, (b - a) % 5, (c - b) % 5, -c % 5)


def permute_vector(p, x):
    y = [0] * len(x)
    for i, j in enumerate(p):
        y[j] = x[i]
    return tuple(y)


coordinate_frames = []
for i in range(5):
    others = [j for j in range(5) if j != i]
    f = set()
    for plus in combinations(others, 2):
        x = tuple(0 if j == i else (1 if j in plus else 4) for j in range(5))
        f.add(projective(T0_to_difference(x)))
    assert len(f) == 3
    coordinate_frames.append(frozenset(f))
assert set(coordinate_frames) == set(frames)

for x in product(range(5), repeat=4):
    x = x + ((-sum(x)) % 5,)
    t = T0_to_difference(x)
    assert q(t) == sum(a * a for a in x) % 5
    for c in range(5):
        assert T0_to_difference(tuple((a + c) % 5 for a in x)) == t

signed_matrices = set()
for p in permutations(range(5)):
    sign = -1 if permutation_parity(p) else 1
    columns = [tuple(sign * a % 5 for a in T0_to_difference(
        permute_vector(p, lift_difference(v)))) for v in I3]
    m = transpose(columns)
    assert m in autos
    assert all(apply_frame(m, coordinate_frames[i]) == coordinate_frames[p[i]]
               for i in range(5))
    signed_matrices.add(m)
assert signed_matrices == so
signed_01 = transpose([tuple(-a % 5 for a in T0_to_difference(
    permute_vector((1, 0, 2, 3, 4), lift_difference(v)))) for v in I3])
assert signed_01 == ((1, 0, 0), (3, 4, 0), (4, 0, 4))

result = {
    "status": "independent scratch analysis; no Canon status change",
    "B": B,
    "orthonormal_basis_R": R,
    "det_R": det(R),
    "projective_line_census": {
        "total": len(lines),
        "isotropic": sum(q(x) == 0 for x in lines),
        "square_norm": len(square_lines),
        "nonsquare_norm": sum(q(x) in (2, 3) for x in lines),
    },
    "frames": {label: sorted(frame) for label, frame in zip(labels, frames)},
    "SO_count": len(so),
    "distinct_frame_actions": len(set(autos.values())),
    "element_order_census": dict(sorted(Counter(map(matrix_order, autos)).items())),
    "square_determinant_PGL_subgroup_size": 60,
    "transposition_witness": {"matrix": transposition, "action": autos[transposition]},
    "order_four_witness": {"matrix": order_four, "action": autos[order_four]},
    "canonical_Phi": {"matrix": phi, "action": autos[phi]},
    "binary_state_count": len(E),
    "binary_singular_nonzero": singular,
    "binary_orthogonal_group_count": len(binary_actions),
    "coordinate_to_even_subset": coordinate_to_E,
    "A4_coordinate_frame_labels": [labels[frames.index(f)] for f in coordinate_frames],
    "A4_signed_S5_count": len(signed_matrices),
    "A4_signed_transposition_01": signed_01,
    "all_assertions_passed": True,
}
print(json.dumps(result, indent=2, sort_keys=True))
