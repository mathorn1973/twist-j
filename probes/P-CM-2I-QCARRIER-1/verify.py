#!/usr/bin/env python3
# verify.py -- accepted exact verifier for public probe P-CM-2I-QCARRIER-1.
#
# Claimed in issue #245 against Public Canon v30 (tag canon-v30, content
# commit 857223fcd5e7bc8c8e68f1df768d6e8222b24ee0). Adopted from the
# reviewed pre-pin candidate notes/P-CM-2I-QCARRIER-1-PREP/verify_draft.py
# (PR #244, commit 873fec4) with only this header changed. The incubation
# outputs were known before this pin, so the probe is result-exposed and
# confirmatory; PREREG.md discloses this.
#
# Scope: one fixed marked COLOR-INTEGRAL-LIFT representative, its Galois
# twists, the ordered rho (+) rho^tau pair, the complete equivariant
# tau-semilinear Hom calculation, the norm obstruction, one order-eight
# integral lift, the single-branch invariant Gram line, and one balanced
# pair similitude. No decoder Q/QCarrier, L5/L6, U(1), or lift selection.
import sys
from fractions import Fraction as F


RESULTS = []


def check(name, condition):
    ok = bool(condition)
    RESULTS.append(ok)
    print(("PASS " if ok else "FAIL ") + name)


# ---------- K = Q(zeta_5), exact in the basis 1,zeta,zeta^2,zeta^3 ----------
def red(v):
    c = v[4]
    return (v[0] - c, v[1] - c, v[2] - c, v[3] - c)


def zadd(a, b):
    return tuple(x + y for x, y in zip(a, b))


def zsub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def zneg(a):
    return tuple(-x for x in a)


def zint(n):
    return (F(n), F(0), F(0), F(0))


def zmul(a, b):
    v = [F(0)] * 5
    for i in range(4):
        if a[i] == 0:
            continue
        for j in range(4):
            if b[j] != 0:
                v[(i + j) % 5] += a[i] * b[j]
    return red(tuple(v))


def gal(a, exponent):
    v = [F(0)] * 5
    for i in range(4):
        v[(i * exponent) % 5] += a[i]
    return red(tuple(v))


def zinv(a):
    columns = []
    for j in range(4):
        e = [F(0)] * 4
        e[j] = F(1)
        columns.append(zmul(a, tuple(e)))
    aug = [[columns[c][r] for c in range(4)] for r in range(4)]
    rhs = [F(1), F(0), F(0), F(0)]
    for c in range(4):
        pivot = next((r for r in range(c, 4) if aug[r][c] != 0), None)
        if pivot is None:
            return None
        aug[c], aug[pivot] = aug[pivot], aug[c]
        rhs[c], rhs[pivot] = rhs[pivot], rhs[c]
        scale = 1 / aug[c][c]
        aug[c] = [x * scale for x in aug[c]]
        rhs[c] *= scale
        for r in range(4):
            if r == c or aug[r][c] == 0:
                continue
            factor = aug[r][c]
            aug[r] = [x - factor * y for x, y in zip(aug[r], aug[c])]
            rhs[r] -= factor * rhs[c]
    return tuple(rhs)


Z0 = zint(0)
Z1 = zint(1)
ZETA = (F(0), F(1), F(0), F(0))
PHI = (F(0), F(0), F(-1), F(-1))
IPHI = zsub(PHI, Z1)
PHI2 = zmul(PHI, PHI)
SQRT5 = (F(-1), F(0), F(-2), F(-2))


def integral(a):
    return all(x.denominator == 1 for x in a)


def unit_in_OK(a):
    inverse = zinv(a)
    return inverse is not None and integral(a) and integral(inverse)


def to_F(a):
    # x + y sqrt(5), with sqrt(5) = (-1,0,-2,-2).
    if a[1] != 0 or a[2] != a[3]:
        return None
    y = -a[2] / F(2)
    return (a[0] + y, y)


def sign_at_principal(pair):
    x, y = pair
    if x == 0 and y == 0:
        return 0
    if x >= 0 and y >= 0:
        return 1
    if x <= 0 and y <= 0:
        return -1
    dominant_x = x * x > 5 * y * y
    if x > 0:
        return 1 if dominant_x else -1
    return -1 if dominant_x else 1


def real_conjugate(pair):
    # The nontrivial automorphism of F/Q is tau restricted to F.
    return (pair[0], -pair[1])


check(
    "M1 field conventions: sigma=tau^2 fixes F, while tau(phi^-1)=-phi",
    gal(PHI, 4) == PHI
    and gal(PHI, 2) == zneg(IPHI)
    and gal(IPHI, 2) == zneg(PHI),
)


# ---------- matrices over K ----------
def matmul(a, b):
    rows = len(a)
    inner = len(b)
    cols = len(b[0])
    return tuple(
        tuple(
            sum_k((zmul(a[i][k], b[k][j]) for k in range(inner)))
            for j in range(cols)
        )
        for i in range(rows)
    )


def sum_k(values):
    total = Z0
    for value in values:
        total = zadd(total, value)
    return total


def matsub(a, b):
    return tuple(
        tuple(zsub(a[i][j], b[i][j]) for j in range(len(a[0])))
        for i in range(len(a))
    )


def matgal(a, exponent):
    return tuple(tuple(gal(x, exponent) for x in row) for row in a)


def matdag(a):
    return tuple(
        tuple(gal(a[j][i], 4) for j in range(len(a)))
        for i in range(len(a[0]))
    )


def matscale(scalar, a):
    return tuple(tuple(zmul(scalar, x) for x in row) for row in a)


def flatten(a):
    return tuple(x for row in a for x in row)


def matrix_from_flat(values, nrows, ncols):
    return tuple(
        tuple(values[i * ncols + j] for j in range(ncols))
        for i in range(nrows)
    )


def det2(a):
    return zsub(zmul(a[0][0], a[1][1]), zmul(a[0][1], a[1][0]))


def tr2(a):
    return zadd(a[0][0], a[1][1])


def block2(a, b, c, d):
    return (
        tuple(a[0]) + tuple(b[0]),
        tuple(a[1]) + tuple(b[1]),
        tuple(c[0]) + tuple(d[0]),
        tuple(c[1]) + tuple(d[1]),
    )


I2 = ((Z1, Z0), (Z0, Z1))
O2 = ((Z0, Z0), (Z0, Z0))
S = ((Z0, zneg(Z1)), (Z1, Z0))
T = ((ZETA, Z1), (Z0, gal(ZETA, 4)))
I4 = block2(I2, O2, O2, I2)
mI2 = ((zneg(Z1), Z0), (Z0, zneg(Z1)))
mI4 = block2(mI2, O2, O2, mI2)


# ---------- exact linear algebra over K ----------
def rref_K(matrix):
    a = [list(row) for row in matrix]
    if not a:
        return a, []
    ncols = len(a[0])
    pivots = []
    row = 0
    for col in range(ncols):
        pivot = next((r for r in range(row, len(a)) if a[r][col] != Z0), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        scale = zinv(a[row][col])
        a[row] = [zmul(scale, x) for x in a[row]]
        for r in range(len(a)):
            if r == row or a[r][col] == Z0:
                continue
            factor = a[r][col]
            a[r] = [zsub(x, zmul(factor, y)) for x, y in zip(a[r], a[row])]
        pivots.append(col)
        row += 1
        if row == len(a):
            break
    return a, pivots


def rank_K(matrix):
    return len(rref_K(matrix)[1])


def kernel_contains(matrix, vector):
    return all(sum_k(zmul(c, x) for c, x in zip(row, vector)) == Z0 for row in matrix)


def rank_Q(matrix):
    a = [list(row) for row in matrix]
    if not a:
        return 0
    rank = 0
    row = 0
    for col in range(len(a[0])):
        pivot = next((r for r in range(row, len(a)) if a[r][col] != 0), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        scale = 1 / a[row][col]
        a[row] = [x * scale for x in a[row]]
        for r in range(len(a)):
            if r == row or a[r][col] == 0:
                continue
            factor = a[r][col]
            a[r] = [x - factor * y for x, y in zip(a[r], a[row])]
        rank += 1
        row += 1
    return rank


# ---------- the fixed integral 2I lift ----------
group = {I2}
frontier = [I2]
overflow = False
while frontier and not overflow:
    current = frontier.pop()
    for generator in (S, T):
        product = matmul(current, generator)
        if product not in group:
            group.add(product)
            frontier.append(product)
            if len(group) > 130:
                overflow = True
                break
G = sorted(group)


def order(a):
    power = a
    n = 1
    while power != I2:
        power = matmul(power, a)
        n += 1
        if n > 200:
            return 0
    return n


check(
    "M2 the fixed marked lift closes to 120 integral determinant-one matrices",
    not overflow
    and len(G) == 120
    and all(det2(g) == Z1 for g in G)
    and all(integral(x) for g in G for x in flatten(g)),
)

minus_I = mI2
minus_S = matmul(minus_I, S)
geometric_core = {I2, minus_I, S, minus_S}
twists = {a: {matgal(g, a) for g in G} for a in (2, 3, 4)}
check(
    "M3 every nontrivial twist meets the fixed matrix set exactly in <S>",
    all((twists[a] & group) == geometric_core for a in (2, 3, 4)),
)


# Explicit sigma intertwiner; q = zeta-zeta^4.
q = zsub(ZETA, gal(ZETA, 4))
C0 = ((Z1, q), (zneg(q), Z1))
marked_sigma = all(matmul(C0, matgal(g, 4)) == matmul(g, C0) for g in (S, T))
trace_T = tr2(T)
check(
    "M4 marked twist-isomorphism-class stabilizer is {1,sigma}; this alone is not descent",
    marked_sigma
    and det2(C0) != Z0
    and trace_T == IPHI
    and gal(trace_T, 4) == trace_T
    and gal(trace_T, 2) == zneg(PHI)
    and gal(trace_T, 3) != trace_T,
)


def Pi(g):
    return block2(g, O2, O2, matgal(g, 2))


def class_function(exponent):
    result = {}
    for g in G:
        key = (order(g), gal(tr2(g), exponent))
        result[key] = result.get(key, 0) + 1
    return result


class_functions = {a: class_function(a) for a in (1, 2, 3, 4)}
golden = [g for g in G if gal(tr2(g), 2) != tr2(g)]
pair_character_rational = all(
    zadd(tr2(g), gal(tr2(g), 2))[1:] == (F(0), F(0), F(0)) for g in G
)
P_tau = block2(O2, C0, I2, O2)
P_sigma = block2(C0, O2, O2, matgal(C0, 2))
P_tau3 = block2(O2, I2, matgal(C0, 2), O2)
pair_twist_intertwiners = {
    2: P_tau,
    4: P_sigma,
    3: P_tau3,
}
pair_twist_intertwiners_invertible = (
    det2(C0) != Z0 and det2(matgal(C0, 2)) != Z0
)
check(
    "M5 pair character is Q-valued and explicit intertwiners certify Galois-stable isomorphism class",
    class_functions[1] == class_functions[2] == class_functions[3] == class_functions[4]
    and len(golden) == 48
    and all(order(g) in (5, 10) for g in golden)
    and pair_character_rational
    and pair_twist_intertwiners_invertible
    and all(
        all(
            matmul(p, matgal(Pi(g), exponent)) == matmul(Pi(g), p)
            for g in (S, T)
        )
        for exponent, p in pair_twist_intertwiners.items()
    ),
)


# ---------- Hom systems over K ----------
def hom_system(source_exponent, target_exponent):
    columns = []
    for variable in range(4):
        values = [Z0] * 4
        values[variable] = Z1
        x = matrix_from_flat(values, 2, 2)
        column = []
        for g in (S, T):
            left = matmul(x, matgal(g, source_exponent))
            right = matmul(matgal(g, target_exponent), x)
            column.extend(flatten(matsub(left, right)))
        columns.append(column)
    return [
        [columns[col][row] for col in range(4)]
        for row in range(len(columns[0]))
    ]


span_rho = [flatten(x) for x in (I2, S, T, matmul(S, T))]
span_tau = [[gal(x, 2) for x in row] for row in span_rho]
check(
    "M6 both golden branches are absolutely irreducible (full M2 span)",
    rank_K(span_rho) == 4 and rank_K(span_tau) == 4,
)

end_rho = hom_system(1, 1)
end_tau = hom_system(2, 2)
check(
    "M7 both branch centralizers are exactly the scalar K-lines",
    rank_K(end_rho) == 3
    and rank_K(end_tau) == 3
    and kernel_contains(end_rho, flatten(I2))
    and kernel_contains(end_tau, flatten(I2)),
)

hom_tau_rho = hom_system(2, 1)
hom_sigma_tau = hom_system(4, 2)
check(
    "M8 both diagonal blocks of an equivariant tau-semilinear pair map vanish",
    rank_K(hom_tau_rho) == 4 and rank_K(hom_sigma_tau) == 4,
)

hom_sigma_rho = hom_system(4, 1)
check(
    "M9 allowed off-diagonal Hom spaces are K*C0 and K*I2",
    rank_K(hom_sigma_rho) == 3
    and rank_K(end_tau) == 3
    and kernel_contains(hom_sigma_rho, flatten(C0))
    and kernel_contains(end_tau, flatten(I2)),
)

def pair_semilinear_system():
    columns = []
    for variable in range(16):
        values = [Z0] * 16
        values[variable] = Z1
        b = matrix_from_flat(values, 4, 4)
        column = []
        for g in (S, T):
            difference = matsub(matmul(b, matgal(Pi(g), 2)), matmul(Pi(g), b))
            column.extend(flatten(difference))
        columns.append(column)
    return [
        [columns[col][row] for col in range(16)]
        for row in range(len(columns[0]))
    ]


pair_system = pair_semilinear_system()
upper_basis = block2(O2, C0, O2, O2)
lower_basis = block2(O2, O2, I2, O2)
check(
    "M10 full pair kernel has K-rank 14/nullity 2 with the antidiagonal basis",
    rank_K(pair_system) == 14
    and kernel_contains(pair_system, flatten(upper_basis))
    and kernel_contains(pair_system, flatten(lower_basis))
    and rank_K([flatten(upper_basis), flatten(lower_basis)]) == 2,
)


# ---------- cocycle and order ----------
mu_matrix = matmul(C0, matgal(C0, 4))
mu0 = mu_matrix[0][0]
mu_pair = to_F(mu0)
check(
    "M11 C0 is an integral unit intertwiner on all 120 elements with mu0=-phi^2",
    all(matmul(C0, matgal(g, 4)) == matmul(g, C0) for g in G)
    and all(integral(x) for x in flatten(C0))
    and unit_in_OK(det2(C0))
    and mu_matrix == matscale(zneg(PHI2), I2)
    and mu0 == zneg(PHI2),
)

norm_phi = zmul(PHI, gal(PHI, 4))
class_minus_one = zmul(mu0, zinv(PHI2))
check(
    "M12 cocycle representative realizes class [-1] and is totally negative",
    norm_phi == PHI2
    and class_minus_one == zneg(Z1)
    and mu_pair is not None
    and sign_at_principal(mu_pair) == -1
    and sign_at_principal(real_conjugate(mu_pair)) == -1,
)

order4_target = gal(zinv(mu0), 2)
target_pair = to_F(order4_target)
positive_witness_pair = to_F(norm_phi)
check(
    "M13 exact sign certificate: order-four target is totally negative and witness norm positive",
    target_pair is not None
    and positive_witness_pair is not None
    and sign_at_principal(target_pair) == -1
    and sign_at_principal(real_conjugate(target_pair)) == -1
    and sign_at_principal(positive_witness_pair) == 1
    and sign_at_principal(real_conjugate(positive_witness_pair)) == 1,
)

phi_I2 = matscale(PHI, I2)
B0 = block2(O2, C0, phi_I2, O2)


def semilinear_compose(first, second):
    # Apply second, then first. Twist exponents multiply modulo 5.
    m1, k1 = first
    m2, k2 = second
    return (matmul(m1, matgal(m2, k1)), (k1 * k2) % 5)


NU = (B0, 2)
check(
    "M14 explicit d=phi lift is integral, invertible, equivariant, and swaps branches",
    unit_in_OK(PHI)
    and unit_in_OK(det2(C0))
    and all(integral(x) for x in flatten(B0))
    and all(semilinear_compose(NU, (Pi(g), 1)) == semilinear_compose((Pi(g), 1), NU) for g in G)
    and all(B0[i][j] == Z0 for i in range(2) for j in range(2))
    and all(B0[i][j] == Z0 for i in range(2, 4) for j in range(2, 4)),
)

NU2 = semilinear_compose(NU, NU)
NU4 = semilinear_compose(NU2, NU2)
NU8 = semilinear_compose(NU4, NU4)
nu2_block_diagonal = (
    all(NU2[0][i][j] == Z0 for i in range(2) for j in range(2, 4))
    and all(NU2[0][i][j] == Z0 for i in range(2, 4) for j in range(2))
)
check(
    "M15 nu^2 is block-diagonal sigma-semilinear (not bare conjugation); nu^4=-I, nu^8=I",
    NU2[1] == 4
    and nu2_block_diagonal
    and NU2[0] != I4
    and NU4 == (mI4, 1)
    and NU8 == (I4, 1),
)


# ---------- single-branch Gram line and balanced pair similitude ----------
H0 = O2
for g in G:
    term = matmul(matdag(g), g)
    H0 = tuple(
        tuple(zadd(H0[i][j], term[i][j]) for j in range(2))
        for i in range(2)
    )
check(
    "M16 H0=sum g^dagger g is sigma-Hermitian and invariant",
    matdag(H0) == H0
    and all(matmul(matdag(g), matmul(H0, g)) == H0 for g in (S, T)),
)

h11 = to_F(H0[0][0])
h22 = to_F(H0[1][1])
det_h = to_F(det2(H0))
check(
    "M17 H0 is totally positive definite at both real embeddings",
    all(x is not None for x in (h11, h22, det_h))
    and all(sign_at_principal(x) == 1 and sign_at_principal(real_conjugate(x)) == 1 for x in (h11, h22, det_h)),
)


def hermitian_from_parameters(p):
    a = zadd(zint(p[0]), tuple(p[1] * x for x in SQRT5))
    d = zadd(zint(p[2]), tuple(p[3] * x for x in SQRT5))
    b = (p[4], p[5], p[6], p[7])
    return ((a, b), (gal(b, 4), d))


gram_columns = []
for variable in range(8):
    p = [F(0)] * 8
    p[variable] = F(1)
    h = hermitian_from_parameters(p)
    column = []
    for g in (S, T):
        difference = matsub(matmul(matdag(g), matmul(h, g)), h)
        for value in flatten(difference):
            column.extend(value)
    gram_columns.append(column)
gram_system = [
    [gram_columns[col][row] for col in range(8)]
    for row in range(len(gram_columns[0]))
]


def hermitian_parameters(h):
    aa = to_F(h[0][0])
    dd = to_F(h[1][1])
    if aa is None or dd is None:
        return None
    return [aa[0], aa[1], dd[0], dd[1], *h[0][1]]


h0_parameters = hermitian_parameters(H0)
sqrt5_h0_parameters = hermitian_parameters(matscale(SQRT5, H0))
in_gram_kernel = lambda vector: all(
    sum(gram_system[r][c] * vector[c] for c in range(8)) == 0
    for r in range(len(gram_system))
) if vector is not None else False
check(
    "M18 invariant single-branch Hermitian space is exactly the F-line F*H0",
    h0_parameters is not None
    and sqrt5_h0_parameters is not None
    and rank_Q(gram_system) == 6
    and in_gram_kernel(h0_parameters)
    and in_gram_kernel(sqrt5_h0_parameters)
    and rank_Q([h0_parameters, sqrt5_h0_parameters]) == 2,
)

H_pair = block2(H0, O2, O2, matgal(H0, 2))
balanced_left = matmul(matdag(B0), matmul(H_pair, B0))
balanced_right = matscale(PHI2, matgal(H_pair, 2))
check(
    "M19 balanced pair identity: B0^dagger H_pair B0 = phi^2 tau(H_pair)",
    norm_phi == PHI2
    and matmul(matdag(C0), matmul(H0, C0)) == matscale(PHI2, matgal(H0, 4))
    and balanced_left == balanced_right,
)


passed = sum(RESULTS)
print("SUMMARY %d/%d PASS" % (passed, len(RESULTS)))
sys.exit(0 if passed == len(RESULTS) else 1)
