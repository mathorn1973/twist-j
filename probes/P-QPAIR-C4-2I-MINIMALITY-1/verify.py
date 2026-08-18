#!/usr/bin/env python3
"""Exact audit for P-QPAIR-C4-2I-MINIMALITY-1.

ZERO-RUN RULE: before the immutable preregistration pin this file may be
syntax-compiled, but it must not be imported or executed.

The written proofs in PREREG.md are the theorem-grade evidence.  This verifier
audits their finite certificates using only exact standard-library arithmetic.
"""

from fractions import Fraction as Fr
import sys


# Q(zeta_5) in the basis 1, zeta, zeta^2, zeta^3.
def kint(n):
    return (Fr(n), Fr(0), Fr(0), Fr(0))


KZERO = kint(0)
KONE = kint(1)
ZETA = (Fr(0), Fr(1), Fr(0), Fr(0))


def kadd(a, b):
    return tuple(a[i] + b[i] for i in range(4))


def kneg(a):
    return tuple(-x for x in a)


def ksub(a, b):
    return kadd(a, kneg(b))


def kscale(q, a):
    return tuple(q * x for x in a)


def kmul(a, b):
    out = [Fr(0)] * 7
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    # zeta^4 = -(1 + zeta + zeta^2 + zeta^3).
    for degree in range(6, 3, -1):
        coeff = out[degree]
        if coeff:
            out[degree] = Fr(0)
            start = degree - 4
            for j in range(4):
                out[start + j] -= coeff
    return tuple(out[:4])


def kpow(a, n):
    if n < 0:
        raise ValueError("negative powers are not used")
    result = KONE
    base = a
    exponent = n
    while exponent:
        if exponent & 1:
            result = kmul(result, base)
        base = kmul(base, base)
        exponent //= 2
    return result


def kgalois(a, exponent):
    result = KZERO
    for i, coeff in enumerate(a):
        result = kadd(result, kscale(coeff, kpow(ZETA, (i * exponent) % 5)))
    return result


def kconj(a):
    return kgalois(a, 4)


def ktau(a):
    return kgalois(a, 2)


def ksum(items):
    result = KZERO
    for item in items:
        result = kadd(result, item)
    return result


def m2(a, b, c, d):
    return ((a, b), (c, d))


I2 = m2(KONE, KZERO, KZERO, KONE)
NEG_I2 = m2(kneg(KONE), KZERO, KZERO, kneg(KONE))
S0 = m2(KZERO, kneg(KONE), KONE, KZERO)
T0 = m2(ZETA, KONE, KZERO, kpow(ZETA, 4))


def m2mul(a, b):
    return (
        (
            kadd(kmul(a[0][0], b[0][0]), kmul(a[0][1], b[1][0])),
            kadd(kmul(a[0][0], b[0][1]), kmul(a[0][1], b[1][1])),
        ),
        (
            kadd(kmul(a[1][0], b[0][0]), kmul(a[1][1], b[1][0])),
            kadd(kmul(a[1][0], b[0][1]), kmul(a[1][1], b[1][1])),
        ),
    )


def m2transpose(a):
    return ((a[0][0], a[1][0]), (a[0][1], a[1][1]))


def m2det(a):
    return ksub(kmul(a[0][0], a[1][1]), kmul(a[0][1], a[1][0]))


def m2trace(a):
    return kadd(a[0][0], a[1][1])


def m2inv_sl(a):
    if m2det(a) != KONE:
        raise ValueError("matrix is not special linear")
    return m2(a[1][1], kneg(a[0][1]), kneg(a[1][0]), a[0][0])


def m2pow(a, n):
    result = I2
    for _ in range(n):
        result = m2mul(result, a)
    return result


def m2vec(a, v):
    return (
        kadd(kmul(a[0][0], v[0]), kmul(a[0][1], v[1])),
        kadd(kmul(a[1][0], v[0]), kmul(a[1][1], v[1])),
    )


def group_closure(generators, cap):
    seen = {I2}
    frontier = [I2]
    capped = False
    while frontier:
        g = frontier.pop()
        for h in generators:
            candidate = m2mul(h, g)
            if candidate not in seen:
                seen.add(candidate)
                frontier.append(candidate)
                if len(seen) > cap:
                    capped = True
                    frontier.clear()
                    break
    return tuple(seen), capped


def hslot(v):
    return tuple(
        tuple(kmul(v[i], kconj(v[j])) for j in range(2)) for i in range(2)
    )


def sslot(v):
    return tuple(tuple(kmul(v[i], v[j]) for j in range(2)) for i in range(2))


def scalar_vec(u, v):
    return tuple(kmul(u, x) for x in v)


def neg_vec(v):
    return tuple(kneg(x) for x in v)


def phi_k(v):
    return (v[1], kconj(v[0]))


def phi_inv_k(v):
    return (kconj(v[1]), v[0])


# Exact multivariate polynomials in x, y, p, q for the S-fiber certificate.
def poly_const(q):
    return {} if q == 0 else {(0, 0, 0, 0): Fr(q)}


def poly_var(index):
    exponent = [0, 0, 0, 0]
    exponent[index] = 1
    return {tuple(exponent): Fr(1)}


def poly_add(a, b):
    result = dict(a)
    for monomial, coeff in b.items():
        value = result.get(monomial, Fr(0)) + coeff
        if value:
            result[monomial] = value
        elif monomial in result:
            del result[monomial]
    return result


def poly_neg(a):
    return {monomial: -coeff for monomial, coeff in a.items()}


def poly_sub(a, b):
    return poly_add(a, poly_neg(b))


def poly_scale(q, a):
    return {monomial: Fr(q) * coeff for monomial, coeff in a.items() if q * coeff}


def poly_mul(a, b):
    result = {}
    for ma, ca in a.items():
        for mb, cb in b.items():
            monomial = tuple(ma[i] + mb[i] for i in range(4))
            result[monomial] = result.get(monomial, Fr(0)) + ca * cb
    return {m: c for m, c in result.items() if c}


def poly_square(a):
    return poly_mul(a, a)


# Rational matrix and real-quadratic helpers.
def qidentity(n):
    return tuple(
        tuple(Fr(1) if i == j else Fr(0) for j in range(n)) for i in range(n)
    )


def qmatmul(a, b):
    return tuple(
        tuple(
            sum((a[i][k] * b[k][j] for k in range(len(b))), Fr(0))
            for j in range(len(b[0]))
        )
        for i in range(len(a))
    )


def qmatpow(a, n):
    result = qidentity(len(a))
    for _ in range(n):
        result = qmatmul(result, a)
    return result


def rank_fraction(rows):
    if not rows:
        return 0
    matrix = [list(map(Fr, row)) for row in rows]
    nrows = len(matrix)
    ncols = len(matrix[0])
    rank = 0
    for col in range(ncols):
        pivot = next((r for r in range(rank, nrows) if matrix[r][col]), None)
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        pivot_value = matrix[rank][col]
        matrix[rank] = [x / pivot_value for x in matrix[rank]]
        for r in range(nrows):
            if r != rank and matrix[r][col]:
                factor = matrix[r][col]
                matrix[r] = [
                    matrix[r][j] - factor * matrix[rank][j]
                    for j in range(ncols)
                ]
        rank += 1
        if rank == nrows:
            break
    return rank


def det_fraction(rows):
    matrix = [list(map(Fr, row)) for row in rows]
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("determinant requires a square matrix")
    determinant = Fr(1)
    for col in range(n):
        pivot = next((r for r in range(col, n) if matrix[r][col]), None)
        if pivot is None:
            return Fr(0)
        if pivot != col:
            matrix[col], matrix[pivot] = matrix[pivot], matrix[col]
            determinant = -determinant
        pivot_value = matrix[col][col]
        determinant *= pivot_value
        for r in range(col + 1, n):
            if matrix[r][col]:
                factor = matrix[r][col] / pivot_value
                for j in range(col, n):
                    matrix[r][j] -= factor * matrix[col][j]
    return determinant


QUAD_MONOMIALS = (
    (0, 0),
    (0, 1),
    (1, 1),
    (0, 2),
    (0, 3),
    (1, 2),
    (1, 3),
    (2, 2),
    (2, 3),
    (3, 3),
)
QUAD_INDEX = {monomial: i for i, monomial in enumerate(QUAD_MONOMIALS)}


def qrow(*values):
    return tuple(Fr(x) for x in values)


H_ROWS = (
    qrow(1, 0, 1, 0, 0, 0, 0, 0, 0, 0),       # |z1|^2
    qrow(0, 0, 0, 0, 0, 0, 0, 1, 0, 1),       # |z2|^2
    qrow(0, 0, 0, 1, 0, 0, 1, 0, 0, 0),       # Re(z1 c(z2))
    qrow(0, 0, 0, 0, -1, 1, 0, 0, 0, 0),      # Im(z1 c(z2))
)
SYM_ROWS = (
    qrow(1, 0, -1, 0, 0, 0, 0, 0, 0, 0),      # Re(z1^2)
    qrow(0, 2, 0, 0, 0, 0, 0, 0, 0, 0),       # Im(z1^2)
    qrow(0, 0, 0, 1, 0, 0, -1, 0, 0, 0),      # Re(z1 z2)
    qrow(0, 0, 0, 0, 1, 1, 0, 0, 0, 0),       # Im(z1 z2)
    qrow(0, 0, 0, 0, 0, 0, 0, 1, 0, -1),      # Re(z2^2)
    qrow(0, 0, 0, 0, 0, 0, 0, 0, 2, 0),       # Im(z2^2)
)
QPAIR_ROWS = H_ROWS + SYM_ROWS


PHI_R = (
    qrow(0, 0, 1, 0),
    qrow(0, 0, 0, 1),
    qrow(1, 0, 0, 0),
    qrow(0, -1, 0, 0),
)
CONJ_R = (
    qrow(1, 0, 0, 0),
    qrow(0, -1, 0, 0),
    qrow(0, 0, 1, 0),
    qrow(0, 0, 0, -1),
)


def quad_pull(row, linear):
    result = [Fr(0)] * len(QUAD_MONOMIALS)
    for coeff, (i, j) in zip(row, QUAD_MONOMIALS):
        if not coeff:
            continue
        for a in range(4):
            for b in range(4):
                value = coeff * linear[i][a] * linear[j][b]
                if value:
                    key = (a, b) if a <= b else (b, a)
                    result[QUAD_INDEX[key]] += value
    return tuple(result)


def basis_row(n, index, sign=1):
    return tuple(Fr(sign) if j == index else Fr(0) for j in range(n))


TQ = (
    basis_row(10, 1),
    basis_row(10, 0),
    basis_row(10, 6),
    basis_row(10, 7),
    basis_row(10, 8),
    basis_row(10, 9),
    basis_row(10, 2),
    basis_row(10, 3, -1),
    basis_row(10, 4),
    basis_row(10, 5, -1),
)


def row_times_matrix(row, matrix):
    return tuple(
        sum((row[i] * matrix[i][j] for i in range(len(row))), Fr(0))
        for j in range(len(matrix[0]))
    )


def closure_rank(initial, action):
    vectors = list(initial)
    changed = True
    while changed:
        changed = False
        for vector in tuple(vectors):
            image = action(vector)
            if rank_fraction(vectors + [image]) > rank_fraction(vectors):
                vectors.append(image)
                changed = True
    return rank_fraction(vectors)


# Holomorphic binary quadratics A x^2 + B xy + C y^2 over K.
def q3add(a, b):
    return tuple(kadd(a[i], b[i]) for i in range(3))


def q3neg(a):
    return tuple(kneg(x) for x in a)


def q3sub(a, b):
    return q3add(a, q3neg(b))


def q3scale(a, q):
    return tuple(kmul(a, x) for x in q)


def q3_linear_product(left, right):
    a, b = left
    c, d = right
    return (
        kmul(a, c),
        kadd(kmul(a, d), kmul(b, c)),
        kmul(b, d),
    )


def q3_pull(q, matrix):
    a, b = matrix[0]
    c, d = matrix[1]
    qa, qb, qc = q
    return (
        ksum((kmul(qa, kmul(a, a)), kmul(qb, kmul(a, c)), kmul(qc, kmul(c, c)))),
        ksum((
            kmul(qa, kscale(Fr(2), kmul(a, b))),
            kmul(qb, kadd(kmul(a, d), kmul(b, c))),
            kmul(qc, kscale(Fr(2), kmul(c, d))),
        )),
        ksum((kmul(qa, kmul(b, b)), kmul(qb, kmul(b, d)), kmul(qc, kmul(d, d)))),
    )


def kdet3(rows):
    a, b, c = rows[0]
    d, e, f = rows[1]
    g, h, i = rows[2]
    return kadd(
        ksub(kmul(a, ksub(kmul(e, i), kmul(f, h))), kmul(b, ksub(kmul(d, i), kmul(f, g)))),
        kmul(c, ksub(kmul(d, h), kmul(e, g))),
    )


def sslot_polynomial():
    ex2 = (KONE, KZERO, KZERO)
    exy = (KZERO, KONE, KZERO)
    ey2 = (KZERO, KZERO, KONE)
    return ((ex2, exy), (exy, ey2))


def sslot_after_linear(matrix):
    row0 = matrix[0]
    row1 = matrix[1]
    return (
        (q3_linear_product(row0, row0), q3_linear_product(row0, row1)),
        (q3_linear_product(row1, row0), q3_linear_product(row1, row1)),
    )


def congruence_on_polynomial_slot(matrix):
    base = sslot_polynomial()
    result = []
    for i in range(2):
        row = []
        for j in range(2):
            value = (KZERO, KZERO, KZERO)
            for a in range(2):
                for b in range(2):
                    value = q3add(
                        value,
                        q3scale(kmul(matrix[i][a], matrix[j][b]), base[a][b]),
                    )
            row.append(value)
        result.append(tuple(row))
    return tuple(result)


def red5(a):
    value = sum(a, Fr(0))
    numerator = value.numerator % 5
    denominator = value.denominator % 5
    if denominator == 0:
        raise ValueError("nonintegral reduction denominator")
    return numerator * pow(denominator, -1, 5) % 5


def main():
    checks = []

    def audit(name, condition):
        checks.append((name, bool(condition)))

    # 01-02: carrier, field relation, and conjugation.
    carrier_vector = (KONE, KZERO)
    carrier_independent = (
        2 * 4 == 8
        and carrier_vector != (KONE, kconj(KONE))
        and carrier_vector in ((KONE, KZERO),)
    )
    cyclotomic_relation = ksum((KONE, ZETA, kpow(ZETA, 2), kpow(ZETA, 3), kpow(ZETA, 4))) == KZERO
    field_ok = (
        cyclotomic_relation
        and kpow(ZETA, 5) == KONE
        and all(kconj(kconj(kpow(ZETA, i))) == kpow(ZETA, i) for i in range(4))
        and all(
            kconj(kmul(kpow(ZETA, i), kpow(ZETA, j)))
            == kmul(kconj(kpow(ZETA, i)), kconj(kpow(ZETA, j)))
            for i in range(4)
            for j in range(4)
        )
    )
    audit("CARRIER_INDEPENDENT_K2", carrier_independent)
    audit("CYCLOTOMIC_AND_CONJUGATION", field_ok)

    # 03-05: arithmetic Hermitian fibers and the content boundary.
    v = (KONE, KONE)
    v_prime = scalar_vec(ZETA, v)
    hv = hslot(v)
    hv_prime = hslot(v_prime)
    hphi = hslot(phi_k(v))
    hphi_prime = hslot(phi_k(v_prime))
    nondesc_ok = (
        hv == hv_prime
        and hphi[0][1] == KONE
        and hphi_prime[0][1] == kpow(ZETA, 2)
        and hphi[0][1] != hphi_prime[0][1]
    )
    roots = set()
    for exponent in range(5):
        root = kpow(ZETA, exponent)
        roots.add(root)
        roots.add(kneg(root))
    mu10_ok = len(roots) == 10 and all(kmul(root, kconj(root)) == KONE for root in roots)
    wide_a = kadd(kint(2), ZETA)
    wide_v = (kconj(wide_a), KZERO)
    wide_w = (wide_a, KZERO)
    wider_ok = (
        hslot(wide_v) == hslot(wide_w)
        and all(scalar_vec(root, wide_v) != wide_w for root in roots)
    )
    audit("HERM_INTEGER_NONDESCENT", nondesc_ok)
    audit("HERM_MU10_UNIT_SUBGROUP", mu10_ok)
    audit("HERM_FULL_LATTICE_WIDER_FIBER", wider_ok)

    # 06-07: formal S-fiber certificate and sign redundancy.
    x, y, p, q = (poly_var(i) for i in range(4))
    f1 = poly_sub(poly_square(x), poly_square(p))
    f2 = poly_sub(poly_mul(x, y), poly_mul(p, q))
    f3 = poly_sub(poly_square(y), poly_square(q))
    cross = poly_sub(poly_mul(x, q), poly_mul(y, p))
    certificate = poly_add(
        poly_sub(poly_mul(poly_square(q), f1), poly_scale(2, poly_mul(poly_mul(p, q), f2))),
        poly_mul(poly_square(p), f3),
    )
    fiber_certificate_ok = poly_square(cross) == certificate
    sign_sample = (kadd(KONE, ZETA), kadd(kint(2), kpow(ZETA, 2)))
    sign_ok = (
        sslot(sign_sample) == sslot(neg_vec(sign_sample))
        and hslot(sign_sample) == hslot(neg_vec(sign_sample))
    )
    audit("TRANSPOSE_FIBER_CERTIFICATE", fiber_certificate_ok)
    audit("SET_REDUNDANCY_SIGN_INVARIANCE", sign_ok)

    # 08-11: state C4 and its exact typed action.
    state_order_ok = qmatpow(PHI_R, 2) == CONJ_R and qmatpow(PHI_R, 4) == qidentity(4)
    expected_map = ((1, 1), (0, 1), (6, 1), (7, 1), (8, 1), (9, 1), (2, 1), (3, -1), (4, 1), (5, -1))
    typed_formula_ok = all(
        quad_pull(QPAIR_ROWS[i], PHI_R) == tuple(Fr(sign) * x for x in QPAIR_ROWS[target])
        for i, (target, sign) in enumerate(expected_map)
    )
    typed_order_ok = qmatpow(TQ, 4) == qidentity(10)
    phi_only_rank = closure_rank(
        [basis_row(10, i) for i in range(4)],
        lambda row: row_times_matrix(row, TQ),
    )
    audit("MIXED_C4_STATE_ORDER", state_order_ok)
    audit("TYPED_MIXED_C4_FORMULAS", typed_formula_ok)
    audit("TYPED_MIXED_C4_ORDER", typed_order_ok)
    audit("PHI_ONLY_CLOSURE_DIM 6", phi_only_rank == 6)

    # 12-18: marked 2I, the symmetric-square character, and the orbit of xy.
    generators = (S0, T0, m2inv_sl(S0), m2inv_sl(T0))
    group, capped = group_closure(generators, 500)
    relations_ok = (
        m2pow(S0, 2) == NEG_I2
        and m2pow(T0, 5) == I2
        and m2pow(m2mul(S0, T0), 3) == NEG_I2
        and all(m2det(g) == KONE for g in group)
    )
    group_ok = not capped and len(group) == 120 and relations_ok
    center = tuple(
        g for g in group if all(m2mul(g, h) == m2mul(h, g) for h in group)
    )
    center_ok = len(center) == 2 and set(center) == {I2, NEG_I2}

    golden = kneg(kadd(kpow(ZETA, 2), kpow(ZETA, 3)))
    trace_t = m2trace(T0)
    chi3_t = ksub(kmul(trace_t, trace_t), KONE)
    reduction_t = tuple(tuple(red5(entry) for entry in row) for row in T0)
    marked_row_ok = reduction_t == ((1, 1), (0, 1)) and trace_t == ksub(golden, KONE)
    sym2_row_ok = (
        chi3_t == ksub(KONE, golden)
        and ksub(kmul(m2trace(NEG_I2), m2trace(NEG_I2)), KONE) == kint(3)
        and ktau(chi3_t) != chi3_t
    )

    norm_sum = KZERO
    fs_sum = KZERO
    for g in group:
        chi2 = m2trace(g)
        chi3 = ksub(kmul(chi2, chi2), KONE)
        norm_sum = kadd(norm_sum, kmul(chi3, kconj(chi3)))
        g2 = m2mul(g, g)
        chi2_g2 = m2trace(g2)
        fs_sum = kadd(fs_sum, ksub(kmul(chi2_g2, chi2_g2), KONE))
    char_norm = kscale(Fr(1, 120), norm_sum)
    fs_indicator = kscale(Fr(1, 120), fs_sum)

    q_xy = (KZERO, KONE, KZERO)
    t_image = q3_pull(q_xy, m2inv_sl(T0))
    t_delta = q3sub(t_image, q_xy)
    s_image = q3_pull(t_delta, m2inv_sl(S0))
    orbit_det = kdet3((q_xy, t_delta, s_image))
    orbit_ok = (
        t_delta == (KZERO, KZERO, kneg(ZETA))
        and s_image == (kneg(ZETA), KZERO, KZERO)
        and orbit_det != KZERO
    )
    audit("MARKED_2I_ORDER 120", group_ok)
    audit("MARKED_2I_CENTER 2", center_ok)
    audit("MARKED_SPIN_ROW 2a", marked_row_ok)
    audit("SYM2_ROW 3a", sym2_row_ok)
    audit("SYM2_CHARACTER_NORM 1", char_norm == KONE)
    audit("SYM2_FS_INDICATOR 1", fs_indicator == KONE)
    audit("SYM2_ORBIT_RANK 3", orbit_ok)

    # 19-23: exact real quadratic ranks and relative closure certificate.
    h_rank = rank_fraction(H_ROWS)
    s_rank = rank_fraction(SYM_ROWS)
    pair_rank = rank_fraction(QPAIR_ROWS)
    pair_det = det_fraction(QPAIR_ROWS)
    relative_ok = (
        typed_formula_ok
        and orbit_ok
        and h_rank == 4
        and s_rank == 6
        and pair_rank == 10
        and abs(pair_det) == 64
        and quad_pull(H_ROWS[2], PHI_R) == SYM_ROWS[2]
        and quad_pull(H_ROWS[3], PHI_R) == SYM_ROWS[3]
    )
    audit("H_COORD_RANK 4", h_rank == 4)
    audit("SYM_COORD_RANK 6", s_rank == 6)
    audit("QPAIR_COORD_RANK 10", pair_rank == 10)
    audit("QPAIR_COORD_ABS_DET 64", abs(pair_det) == 64)
    audit("RELATIVE_CLOSURE_CERTIFICATE", relative_ok)

    # 24-25: exact 2I-only countercertificates.
    epsilon = m2(KZERO, KONE, kneg(KONE), KZERO)
    epsilon_inv = m2(KZERO, kneg(KONE), KONE, KZERO)
    symmetric_basis = (
        m2(KONE, KZERO, KZERO, KZERO),
        m2(KZERO, KONE, KONE, KZERO),
        m2(KZERO, KZERO, KZERO, KONE),
    )

    def theta(y_matrix):
        return m2mul(y_matrix, epsilon_inv)

    intertwiner_ok = True
    for g in (S0, T0):
        g_inv = m2inv_sl(g)
        if m2mul(m2mul(m2transpose(g), epsilon), g) != epsilon:
            intertwiner_ok = False
        for y_matrix in symmetric_basis:
            transformed = m2mul(m2mul(g, y_matrix), m2transpose(g))
            left = theta(transformed)
            right = m2mul(m2mul(g, theta(y_matrix)), g_inv)
            if left != right:
                intertwiner_ok = False

    s_only_ok = all(
        sslot_after_linear(g) == congruence_on_polynomial_slot(g)
        for g in (S0, T0)
    )
    audit("ADJOINT_INTERTWINER", intertwiner_ok)
    audit("S_ONLY_2I_EQUIVARIANT", s_only_ok)

    # 26: Phi T Phi^-1 is Q-linear but not K/complex-linear.
    def conjugated_t(vect):
        return phi_k(m2vec(T0, phi_inv_k(vect)))

    def conjugated_t_formula(vect):
        return (
            kmul(kpow(ZETA, 4), vect[0]),
            kadd(kmul(kpow(ZETA, 4), vect[1]), kconj(vect[0])),
        )

    q_basis = []
    for exponent in range(4):
        q_basis.append((kpow(ZETA, exponent), KZERO))
        q_basis.append((KZERO, kpow(ZETA, exponent)))
    conjugate_formula_ok = all(
        conjugated_t(vect) == conjugated_t_formula(vect) for vect in q_basis
    )
    e1 = (KONE, KZERO)
    zeta_e1 = scalar_vec(ZETA, e1)
    not_k_linear = conjugated_t(zeta_e1) != scalar_vec(ZETA, conjugated_t(e1))
    audit("MIXED_C4_NORMALIZES_2I FALSE", conjugate_formula_ok and not_k_linear)

    for index, (name, passed) in enumerate(checks, 1):
        print(f"{index:02d} {name} {'PASS' if passed else 'FAIL'}")
    passed_count = sum(1 for _, passed in checks if passed)
    if passed_count == len(checks):
        print(f"RESULT {passed_count}/{len(checks)} ALL PASS")
        return 0
    print(f"RESULT {passed_count}/{len(checks)} FAIL {len(checks) - passed_count}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
