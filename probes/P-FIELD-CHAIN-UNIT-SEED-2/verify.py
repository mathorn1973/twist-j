# P-FIELD-CHAIN-UNIT-SEED-2 exact audit. NON-CANONICAL / L1.
# Successor of abandoned P-FIELD-CHAIN-UNIT-SEED-1; fixture-level fixes
# only (zero-coefficient cleaning, minimizer pairing), same mathematics.
# Matrices transcribed from Public Canon v102, shared proof section 2 of
# FIELD-CONSERVATIVE-CHAIN-LAW. Standard library only; exact integers.
import itertools
from math import isqrt

BF = ((4, -2, 2, -1), (-2, 6, -1, 3), (2, -1, 2, 0), (-1, 3, 0, 2))
AF = ((1, 0, 1, 0), (0, 1, 0, 1), (-2, 1, -1, 1), (1, -3, 1, -2))
L = ((1, -3, -1, -2), (-3, 4, -2, 1), (0, 5, 1, 2), (5, -5, 2, -1))
VINV = ((1, 2, 1, 2), (2, -1, 2, -1), (0, -5, 1, -3), (-5, 5, -3, 4))
I4 = ((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1))
YBAR = (0, 0, 3, 1)
SHELL_CAP = 5


def H(y):
    a, b, c, d = y
    return (2 * a * a - 2 * a * b + 3 * b * b + c * c + d * d
            + 2 * a * c - a * d - b * c + 3 * b * d)


def matvec(m, v):
    return tuple(sum(m[i][j] * v[j] for j in range(4)) for i in range(4))


def matmul(m, n):
    return tuple(tuple(sum(m[i][k] * n[k][j] for k in range(4))
                       for j in range(4)) for i in range(4))


def matsub(m, n):
    return tuple(tuple(m[i][j] - n[i][j] for j in range(4)) for i in range(4))


def scalarmul(s, m):
    return tuple(tuple(s * m[i][j] for j in range(4)) for i in range(4))


def det_bareiss(m):
    a = [list(row) for row in m]
    n = 4
    sign = 1
    prev = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            piv = next((i for i in range(k + 1, n) if a[i][k] != 0), None)
            if piv is None:
                return 0
            a[k], a[piv] = a[piv], a[k]
            sign = -sign
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                a[i][j] = (a[i][j] * a[k][k] - a[i][k] * a[k][j]) // prev
            a[i][k] = 0
        prev = a[k][k]
    return sign * a[n - 1][n - 1]


def check(cond, msg):
    if not cond:
        raise AssertionError(msg)


def clean(poly):
    return {k: v for k, v in poly.items() if v != 0}


# 1. Inherited matrix identities, exact (transcription guards).
check(matmul(matsub(I4, AF), matsub(I4, matmul(AF, AF))) == L,
      "L != (I-Af)(I-Af^2)")
check(matmul(VINV, L) == scalarmul(5, I4) == matmul(L, VINV),
      "Vinv L != 5I")
check(det_bareiss(L) == 25, "det L != 25")

# H polynomial agrees with y^t B_f y / 2 as coefficient dictionaries.
HPOLY = {(0, 0): 2, (0, 1): -2, (1, 1): 3, (2, 2): 1, (3, 3): 1,
         (0, 2): 2, (0, 3): -1, (1, 2): -1, (1, 3): 3}
from_bf = {}
for i in range(4):
    for j in range(i, 4):
        v = BF[i][j] if i == j else 2 * BF[i][j]
        check(v % 2 == 0, "B_f/2 not integral")
        if v // 2:
            from_bf[(i, j)] = v // 2
check(clean(from_bf) == clean(HPOLY), "H polynomial != B_f form/2")

# 2. Sum-of-squares identity (Canon Hraw certificate at the P embedding):
# 4H(y) = (2a-2b+c-d)^2 + (2a+c)^2 + 2(2b+d)^2 + c^2 + (c+d)^2,
# verified as an exact polynomial identity by coefficient expansion.
FORMS = [((2, -2, 1, -1), 1), ((2, 0, 1, 0), 1), ((0, 2, 0, 1), 2),
         ((0, 0, 1, 0), 1), ((0, 0, 1, 1), 1)]
sos = {}
for f, w in FORMS:
    for i in range(4):
        for j in range(i, 4):
            v = w * f[i] * f[j] * (1 if i == j else 2)
            if v:
                sos[(i, j)] = sos.get((i, j), 0) + v
check(clean(sos) == clean({k: 4 * v for k, v in HPOLY.items()}),
      "SOS identity fails")


def box_for(k):
    # Any integer y with H(y) <= k lies in this box, by the SOS identity:
    # each squared form is <= 4k, and 2*(2b+d)^2 <= 4k.
    s = isqrt(4 * k)
    t = isqrt(2 * k)
    return (s, (t + 2 * s) // 2, s, 2 * s)  # bounds for |a|,|b|,|c|,|d|


# 3. Enumerate the complete H <= SHELL_CAP box once; bucket by shell.
ba, bb, bc, bd = box_for(SHELL_CAP)
shells = {k: [] for k in range(SHELL_CAP + 1)}
for y in itertools.product(range(-ba, ba + 1), range(-bb, bb + 1),
                           range(-bc, bc + 1), range(-bd, bd + 1)):
    h = H(y)
    check(h >= 0, "H negative in box")
    if h <= SHELL_CAP:
        shells[h].append(y)
    check(H(matvec(L, y)) == 5 * h, "H(Lx) != 5H(x) in box")
check(shells[0] == [(0, 0, 0, 0)], "H zero set in box is not {0}")
units = sorted(shells[1])

# 4. Gate residues: image of L mod 5 equals the 25 criterion residues.
gate = sorted(r for r in itertools.product(range(5), repeat=4)
              if (r[0] + 2 * r[1]) % 5 == 0 and (r[2] + 2 * r[3]) % 5 == 0)
check(len(gate) == 25, "gate residue count")
image_mod5 = sorted({tuple(v % 5 for v in matvec(L, x))
                     for x in itertools.product(range(5), repeat=4)})
check(image_mod5 == gate, "L image mod 5 != gate criterion set")

by_residue = {r: [] for r in gate}
for u in units:
    r = tuple(v % 5 for v in matvec(L, u))
    check(r in by_residue, "unit image outside gate")
    by_residue[r].append(u)

# 5. Coset minimum for YBAR: min H on {y in L Z^4 : y = YBAR mod 5}
# equals 5 * min{H(x) : Lx = YBAR mod 5}; searched shell by shell.
check(YBAR in by_residue, "YBAR is not a gate residue")
minimizers_x = []
min_shell = None
for k in range(1, SHELL_CAP + 1):
    cand = sorted(x for x in shells[k]
                  if tuple(v % 5 for v in matvec(L, x)) == YBAR)
    if cand:
        min_shell = k
        minimizers_x = cand
        break
minimizers_y = [matvec(L, x) for x in minimizers_x]
check(len(set(minimizers_y)) == len(minimizers_y), "L not injective here")

# 6. Deterministic report. Exposed targets are printed as data.
print(f"box_bounds_a_b_c_d={ba},{bb},{bc},{bd} shell_cap={SHELL_CAP}")
print("shell_counts=" + ",".join(str(len(shells[k]))
                                 for k in range(SHELL_CAP + 1)))
print(f"units={len(units)}")
for u in units:
    lu = matvec(L, u)
    print(f"unit {u} Lu={lu} Lu_mod5={tuple(v % 5 for v in lu)}")
hit = [r for r in gate if by_residue[r]]
empty = [r for r in gate if not by_residue[r]]
for r in gate:
    print(f"residue {r} multiplicity={len(by_residue[r])} units={by_residue[r]}")
print(f"residues_hit={len(hit)} residues_empty={len(empty)} empty={empty}")
if min_shell is None:
    print(f"coset_minimum=NONE_WITHIN_CAP{SHELL_CAP} ybar={YBAR}")
else:
    print(f"coset_minimum={5 * min_shell} ybar={YBAR} "
          f"minimizer_count={len(minimizers_x)}")
    for x, y in zip(minimizers_x, minimizers_y):
        print(f"minimizer x={x} H(x)={min_shell} y=Lx={y} H(y)={H(y)}")
ust = [u for u in units if tuple(v % 5 for v in matvec(L, u)) == YBAR]
print(f"unit_preimages_of_ybar={ust}")
print("PASS P-FIELD-CHAIN-UNIT-SEED-2")
