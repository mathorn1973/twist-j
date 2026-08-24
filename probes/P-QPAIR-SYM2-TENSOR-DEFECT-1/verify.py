#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Exact audit for P-QPAIR-SYM2-TENSOR-DEFECT-1.

Authority: none.  Zero-run preregistration verifier.  The written proofs in
PREREG.md carry the universal characteristic-not-two claims; this standard-
library verifier audits exact rational coordinates and generic polynomial
identities.  It must not be imported as a module.

Formal run (only after the immutable pin):
  LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
    python3 probes/P-QPAIR-SYM2-TENSOR-DEFECT-1/verify.py
"""

import sys
from fractions import Fraction
from itertools import product


F = Fraction
ZERO = F(0)
ONE = F(1)
TWO = F(2)
HALF = F(1, 2)
QUARTER = F(1, 4)

FAILURES = []
GATE_COUNT = 0


# ---------------------------------------------------------------- matrices

def matrix(rows):
    """Freeze a rectangular matrix as tuples of Fractions."""
    out = tuple(tuple(F(x) for x in row) for row in rows)
    if out:
        width = len(out[0])
        if any(len(row) != width for row in out):
            raise ValueError("ragged matrix")
    return out


def zeros(nrows, ncols):
    return tuple(tuple(ZERO for _ in range(ncols)) for _ in range(nrows))


def identity(n):
    return tuple(tuple(ONE if i == j else ZERO for j in range(n))
                 for i in range(n))


def madd(a, b):
    return tuple(tuple(a[i][j] + b[i][j] for j in range(len(a[0])))
                 for i in range(len(a)))


def msub(a, b):
    return tuple(tuple(a[i][j] - b[i][j] for j in range(len(a[0])))
                 for i in range(len(a)))


def mscale(scalar, a):
    scalar = F(scalar)
    return tuple(tuple(scalar * x for x in row) for row in a)


def mmul(a, b):
    if not a or not b or len(a[0]) != len(b):
        raise ValueError("matrix product dimension mismatch")
    return tuple(
        tuple(sum((a[i][k] * b[k][j] for k in range(len(b))), ZERO)
              for j in range(len(b[0])))
        for i in range(len(a))
    )


def transpose(a):
    return tuple(tuple(a[i][j] for i in range(len(a)))
                 for j in range(len(a[0])))


def mvec(a, v):
    if not a or len(a[0]) != len(v):
        raise ValueError("matrix-vector dimension mismatch")
    return tuple(sum((a[i][j] * v[j] for j in range(len(v))), ZERO)
                 for i in range(len(a)))


def outer(u, v):
    return tuple(tuple(x * y for y in v) for x in u)


def kron_vec(u, v):
    return tuple(x * y for x in u for y in v)


def kron(a, b):
    """Kronecker product with basis order (a-index,b-index)."""
    return tuple(
        tuple(a[i][j] * b[k][ell]
              for j in range(len(a[0])) for ell in range(len(b[0])))
        for i in range(len(a)) for k in range(len(b))
    )


def columns_to_matrix(columns):
    if not columns:
        return tuple()
    nrows = len(columns[0])
    if any(len(col) != nrows for col in columns):
        raise ValueError("column dimension mismatch")
    return tuple(tuple(columns[j][i] for j in range(len(columns)))
                 for i in range(nrows))


def rank(a):
    """Exact Gaussian rank over Fraction."""
    if not a:
        return 0
    work = [list(row) for row in a]
    nrows = len(work)
    ncols = len(work[0])
    pivot_row = 0
    for col in range(ncols):
        pivot = next((r for r in range(pivot_row, nrows)
                      if work[r][col] != ZERO), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        lead = work[pivot_row][col]
        work[pivot_row] = [x / lead for x in work[pivot_row]]
        for r in range(nrows):
            if r == pivot_row:
                continue
            factor = work[r][col]
            if factor != ZERO:
                work[r] = [work[r][j] - factor * work[pivot_row][j]
                           for j in range(ncols)]
        pivot_row += 1
        if pivot_row == nrows:
            break
    return pivot_row


def determinant2(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def permutation_matrix(basis, transform):
    index = {label: i for i, label in enumerate(basis)}
    rows = [[ZERO for _ in basis] for _ in basis]
    for col, label in enumerate(basis):
        rows[index[transform(label)]][col] = ONE
    return matrix(rows)


def swap_matrix(m, n):
    """V tensor W -> W tensor V for dimensions m,n."""
    rows = [[ZERO for _ in range(m * n)] for _ in range(m * n)]
    for i in range(m):
        for j in range(n):
            rows[j * m + i][i * n + j] = ONE
    return matrix(rows)


def vscale(scalar, v):
    scalar = F(scalar)
    return tuple(scalar * x for x in v)


# ------------------------------------------------------ generic polynomials
# A polynomial is {exponent_tuple: Fraction}.  Zero coefficients are absent.

def pclean(p):
    return {mon: coeff for mon, coeff in p.items() if coeff != ZERO}


def pconst(nvars, value):
    value = F(value)
    if value == ZERO:
        return {}
    return {(0,) * nvars: value}


def pvar(nvars, index):
    mon = [0] * nvars
    mon[index] = 1
    return {tuple(mon): ONE}


def padd(p, q):
    out = dict(p)
    for mon, coeff in q.items():
        out[mon] = out.get(mon, ZERO) + coeff
    return pclean(out)


def pneg(p):
    return {mon: -coeff for mon, coeff in p.items()}


def psub(p, q):
    return padd(p, pneg(q))


def pscale(scalar, p):
    scalar = F(scalar)
    return pclean({mon: scalar * coeff for mon, coeff in p.items()})


def pmul(p, q):
    out = {}
    for left, a in p.items():
        for right, b in q.items():
            mon = tuple(left[i] + right[i] for i in range(len(left)))
            out[mon] = out.get(mon, ZERO) + a * b
    return pclean(out)


def psum(terms, nvars):
    out = pconst(nvars, ZERO)
    for term in terms:
        out = padd(out, term)
    return out


def pdet2(a):
    return psub(pmul(a[0][0], a[1][1]), pmul(a[0][1], a[1][0]))


def mvec_poly(a, v):
    if not a or len(a[0]) != len(v):
        raise ValueError("polynomial matrix-vector dimension mismatch")
    first_nonzero = next((p for p in v if p), None)
    if first_nonzero is None:
        raise ValueError("cannot infer variable count from zero polynomial vector")
    nvars = len(next(iter(first_nonzero)))
    out = []
    for i in range(len(a)):
        out.append(psum((pscale(a[i][j], v[j]) for j in range(len(v))),
                        nvars))
    return tuple(out)


# --------------------------------------------------------------- Q(zeta_5)
# Coordinates mean c0 + c1*z + c2*z^2 + c3*z^3, z^5=1 and
# z^4=-(1+z+z^2+z^3).

def qred5(values):
    c4 = values[4]
    return (values[0] - c4, values[1] - c4,
            values[2] - c4, values[3] - c4)


def zpow(exponent):
    values = [ZERO] * 5
    values[exponent % 5] = ONE
    return qred5(values)


def qmul(a, b):
    out = [ZERO] * 5
    for i in range(4):
        for j in range(4):
            out[(i + j) % 5] += a[i] * b[j]
    return qred5(out)


# ------------------------------------------------------- typed composition

def push_bilinear(left_map, carrier, right_map):
    return mmul(mmul(left_map, carrier), transpose(right_map))


def composition_audits():
    # The barred vectors are deliberately independent typed coordinates.
    v = (F(2), F(-1))
    vbar = (F(3), F(4))
    w = (F(1), F(5))
    wbar = (F(-2), F(3))
    vw = kron_vec(v, w)
    vbwb = kron_vec(vbar, wbar)

    herm_left = outer(vw, vbwb)
    herm_right = kron(outer(v, vbar), outer(w, wbar))
    sym_left = outer(vw, vw)
    sym_right = kron(outer(v, v), outer(w, w))

    # Bilinearity on arbitrary matched tensors.
    a1 = matrix(((1, 2), (3, 4)))
    a2 = matrix(((2, -1), (0, 5)))
    c1 = matrix(((3, 1), (-2, 4)))
    c2 = matrix(((0, 2), (1, -3)))
    bilinear = (
        kron(madd(a1, a2), c1) == madd(kron(a1, c1), kron(a2, c1))
        and kron(a1, madd(c1, c2)) == madd(kron(a1, c1), kron(a1, c2))
    )

    # Naturality with independently typed right maps for H.
    f = matrix(((1, 2), (0, 1), (3, -1)))
    fbar = matrix(((2, 0), (1, -1), (4, 3)))
    g = matrix(((1, -2), (2, 1)))
    gbar = matrix(((3, 1), (-1, 2)))
    left_map = kron(f, g)
    right_map = kron(fbar, gbar)
    natural_herm_left = push_bilinear(left_map, kron(a1, c1), right_map)
    natural_herm_right = kron(
        push_bilinear(f, a1, fbar),
        push_bilinear(g, c1, gbar),
    )
    s1 = matrix(((1, 2), (2, 4)))
    d1 = matrix(((3, -2), (-2, 5)))
    natural_sym_left = push_bilinear(left_map, kron(s1, d1), left_map)
    natural_sym_right = kron(
        push_bilinear(f, s1, f),
        push_bilinear(g, d1, g),
    )

    # Associativity, symmetry, and tensor unit on exact arbitrary carriers.
    e = matrix(((2, 1), (1, 1)))
    associative = kron(kron(a1, c1), e) == kron(a1, kron(c1, e))
    swap = swap_matrix(2, 2)
    symmetric = mmul(mmul(swap, kron(a1, c1)), transpose(swap)) == kron(c1, a1)
    unit = matrix(((1,),))
    unital = kron(a1, unit) == a1 and kron(unit, a1) == a1

    return {
        "product_herm": herm_left == herm_right,
        "product_sym": sym_left == sym_right,
        "bilinear": bilinear,
        "natural_herm": natural_herm_left == natural_herm_right,
        "natural_sym": natural_sym_left == natural_sym_right,
        "associative": associative,
        "symmetric": symmetric,
        "unital": unital,
    }


# ----------------------------------------------------- reordered 2x2 carrier

E_BASIS = tuple(product(range(2), repeat=4))  # (V_1,V_2,W_1,W_2)
E_INDEX = {label: i for i, label in enumerate(E_BASIS)}
I16 = identity(16)

ALPHA = permutation_matrix(E_BASIS,
                           lambda t: (t[1], t[0], t[2], t[3]))
BETA = permutation_matrix(E_BASIS,
                          lambda t: (t[0], t[1], t[3], t[2]))
TAU = mmul(ALPHA, BETA)

P_PLUS_PLUS = mscale(QUARTER, mmul(madd(I16, ALPHA), madd(I16, BETA)))
P_PLUS_MINUS = mscale(QUARTER, mmul(madd(I16, ALPHA), msub(I16, BETA)))
P_MINUS_PLUS = mscale(QUARTER, mmul(msub(I16, ALPHA), madd(I16, BETA)))
P_MINUS_MINUS = mscale(QUARTER, mmul(msub(I16, ALPHA), msub(I16, BETA)))
P_SYM = mscale(HALF, madd(I16, TAU))


def coefficient_matrix(coefficients):
    a, b, c, d = coefficients
    return ((a, b), (c, d))


def composite_square(coefficients):
    x = coefficient_matrix(coefficients)
    return tuple(x[i][j] * x[k][ell] for i, k, j, ell in E_BASIS)


def product_square(v, w):
    return tuple(v[i] * v[k] * w[j] * w[ell]
                 for i, k, j, ell in E_BASIS)


def kappa_vector():
    out = [ZERO] * 16
    out[E_INDEX[(0, 1, 0, 1)]] = ONE
    out[E_INDEX[(0, 1, 1, 0)]] = -ONE
    out[E_INDEX[(1, 0, 0, 1)]] = -ONE
    out[E_INDEX[(1, 0, 1, 0)]] = ONE
    return tuple(out)


KAPPA = kappa_vector()


def composite_square_poly(entries):
    x = ((entries[0], entries[1]), (entries[2], entries[3]))
    return tuple(pmul(x[i][j], x[k][ell])
                 for i, k, j, ell in E_BASIS)


def expected_kappa_poly(scalar_poly):
    return tuple(pscale(HALF * KAPPA[i], scalar_poly) for i in range(16))


def transform_polynomial_matrix(g, x, h, nvars):
    """Return g*x*h^T for 2x2 polynomial matrices."""
    out = [[pconst(nvars, ZERO) for _ in range(2)] for _ in range(2)]
    for i in range(2):
        for j in range(2):
            out[i][j] = psum(
                (pmul(pmul(g[i][p], x[p][q]), h[j][q])
                 for p in range(2) for q in range(2)),
                nvars,
            )
    return tuple(tuple(row) for row in out)


# ------------------------------------------------------------------- gates

def gate(name, condition, detail=""):
    global GATE_COUNT
    GATE_COUNT += 1
    ok = bool(condition)
    if not ok:
        FAILURES.append(name)
    line = "CHECK %-58s %s" % (name, "PASS" if ok else "FAIL")
    if detail:
        line += "  " + detail
    print(line)


def main():
    print("P-QPAIR-SYM2-TENSOR-DEFECT-1 verifier")
    print("exact typed composition, reciprocal gauge descent, and Sym^2 9+1 determinant line")
    print("the determinant line is not a Bell state or the two-qubit singlet")
    print("")

    comp = composition_audits()
    gate("P1.product.H(vw).matched", comp["product_herm"])
    gate("P1.product.S(vw).matched", comp["product_sym"])
    gate("P1.matched-products.bilinear", comp["bilinear"])
    gate("P1.naturality.H.typed", comp["natural_herm"])
    gate("P1.naturality.S", comp["natural_sym"])
    gate("P1.associativity", comp["associative"])
    gate("P1.symmetry", comp["symmetric"])
    gate("P1.tensor-unit", comp["unital"])

    # Formal bidegrees in powers of lambda and c(lambda).
    h_v = (1, 1)
    s_v = (2, 0)
    h_w = (-1, -1)
    s_w = (-2, 0)
    degree_add = lambda left, right: (left[0] + right[0],
                                      left[1] + right[1])
    weights = {
        "HH": degree_add(h_v, h_w),
        "SS": degree_add(s_v, s_w),
        "HS": degree_add(h_v, s_w),
        "SH": degree_add(s_v, h_w),
    }
    gate("P2.factor-gauge.formal-weights",
         weights == {"HH": (0, 0), "SS": (0, 0),
                     "HS": (-1, 1), "SH": (1, -1)})

    one_z5 = zpow(0)
    lambda_z5 = zpow(1)
    c_lambda_z5 = zpow(4)
    inverse_lambda_z5 = zpow(4)
    inverse_c_lambda_z5 = zpow(1)
    hs_weight = qmul(c_lambda_z5, inverse_lambda_z5)
    sh_weight = qmul(lambda_z5, inverse_c_lambda_z5)
    gate("P2.zeta5.cross-weights.nontrivial",
         qmul(lambda_z5, c_lambda_z5) == one_z5
         and hs_weight == zpow(3) and sh_weight == zpow(2)
         and hs_weight != one_z5 and sh_weight != one_z5)
    gate("P2.zeta5.cross-weights.reciprocal",
         qmul(hs_weight, sh_weight) == one_z5)
    gate("P2.zeta5.composite-and-matched.invariant",
         qmul(zpow(1), zpow(-1)) == one_z5
         and weights["HH"] == (0, 0) and weights["SS"] == (0, 0))

    # Commuting involutions and exact projectors in the 16-dimensional ambient.
    zero16 = zeros(16, 16)
    gate("P3.alpha.beta.commuting-involutions",
         mmul(ALPHA, ALPHA) == I16
         and mmul(BETA, BETA) == I16
         and mmul(ALPHA, BETA) == mmul(BETA, ALPHA))
    gate("P3.simultaneous-swap.involution", mmul(TAU, TAU) == I16)
    joint_projectors = (P_PLUS_PLUS, P_PLUS_MINUS,
                        P_MINUS_PLUS, P_MINUS_MINUS)
    gate("P3.projectors.idempotent",
         all(mmul(p, p) == p for p in joint_projectors)
         and mmul(P_SYM, P_SYM) == P_SYM)
    gate("P3.projectors.orthogonal.and.complete",
         all(mmul(p, q) == zero16
             for i, p in enumerate(joint_projectors)
             for j, q in enumerate(joint_projectors) if i != j)
         and madd(madd(P_PLUS_PLUS, P_PLUS_MINUS),
                  madd(P_MINUS_PLUS, P_MINUS_MINUS)) == I16)
    gate("P3.sym.projector.eq.plusplus-plus-minusminus",
         P_SYM == madd(P_PLUS_PLUS, P_MINUS_MINUS))
    ranks = (rank(P_SYM), rank(P_PLUS_PLUS), rank(P_MINUS_MINUS))
    gate("P3.ranks.10.eq.9.plus.1", ranks == (10, 9, 1),
         "ranks=%d,%d,%d" % ranks)
    joint_ranks = tuple(rank(p) for p in joint_projectors)
    gate("P3.joint-ranks.9-3-3-1", joint_ranks == (9, 3, 3, 1),
         "ranks=%d,%d,%d,%d" % joint_ranks)
    gate("P3.kappa.joint-signs.and.Pminusminus",
         mvec(ALPHA, KAPPA) == vscale(-ONE, KAPPA)
         and mvec(BETA, KAPPA) == vscale(-ONE, KAPPA)
         and mvec(TAU, KAPPA) == KAPPA
         and mvec(P_MINUS_MINUS, KAPPA) == KAPPA)

    # Nine explicit product squares span exactly the ++ image.
    basis_vectors = ((ONE, ZERO), (ZERO, ONE), (ONE, ONE))
    product_squares = tuple(product_square(v, w)
                            for v in basis_vectors for w in basis_vectors)
    product_rank = rank(columns_to_matrix(product_squares))
    all_plusplus = all(mvec(P_PLUS_PLUS, square) == square
                       and mvec(P_MINUS_MINUS, square) == (ZERO,) * 16
                       for square in product_squares)
    gate("P3.product-squares.rank-nine", product_rank == 9,
         "rank=%d" % product_rank)
    gate("P3.product-squares.span.exactly.plusplus",
         all_plusplus and product_rank == rank(P_PLUS_PLUS))

    # Generic four-variable determinant coefficient.
    vars4 = tuple(pvar(4, i) for i in range(4))
    x4 = ((vars4[0], vars4[1]), (vars4[2], vars4[3]))
    det4 = pdet2(x4)
    projected4 = mvec_poly(P_MINUS_MINUS, composite_square_poly(vars4))
    gate("P3.symbolic.Pminusminus.x2.eq.det-over-2-kappa",
         projected4 == expected_kappa_poly(det4))

    # Generic 12-variable determinant character under X -> g X h^T.
    vars12 = tuple(pvar(12, i) for i in range(12))
    x = ((vars12[0], vars12[1]), (vars12[2], vars12[3]))
    g = ((vars12[4], vars12[5]), (vars12[6], vars12[7]))
    h = ((vars12[8], vars12[9]), (vars12[10], vars12[11]))
    transformed = transform_polynomial_matrix(g, x, h, 12)
    transformed_entries = (transformed[0][0], transformed[0][1],
                           transformed[1][0], transformed[1][1])
    projected12 = mvec_poly(P_MINUS_MINUS,
                            composite_square_poly(transformed_entries))
    character_scalar = pmul(pmul(pdet2(g), pdet2(h)), pdet2(x))
    gate("P3.symbolic.determinant-character",
         projected12 == expected_kappa_poly(character_scalar))

    # Direct exterior-character audit on the missing line.
    g_num = matrix(((2, 1), (3, 2)))
    h_num = matrix(((1, 4), (2, 3)))
    line_action = kron(kron(g_num, g_num), kron(h_num, h_num))
    character = determinant2(g_num) * determinant2(h_num)
    gate("P3.exterior-line.detg-deth.character",
         mvec(line_action, KAPPA) == vscale(character, KAPPA),
         "character=%s" % character)

    # Exact product and unnormalized Bell controls.
    product_coefficients = (F(3), F(-1), F(6), F(-2))
    phi_plus = (ONE, ZERO, ZERO, ONE)
    psi_minus = (ZERO, ONE, -ONE, ZERO)
    zero_vector = (ZERO,) * 16
    half_kappa = vscale(HALF, KAPPA)
    gate("P3.control.product.det-zero.and.no-minusminus",
         determinant2(coefficient_matrix(product_coefficients)) == ZERO
         and mvec(P_MINUS_MINUS, composite_square(product_coefficients))
         == zero_vector)
    gate("P3.control.unnormalized-Phi-plus.det-line",
         determinant2(coefficient_matrix(phi_plus)) == ONE
         and mvec(P_MINUS_MINUS, composite_square(phi_plus)) == half_kappa)
    gate("P3.control.unnormalized-Psi-minus.det-line",
         determinant2(coefficient_matrix(psi_minus)) == ONE
         and mvec(P_MINUS_MINUS, composite_square(psi_minus)) == half_kappa)

    def norm_squared(coefficients):
        return sum((x * x for x in coefficients), ZERO)

    def normalized_concurrence(coefficients):
        det = determinant2(coefficient_matrix(coefficients))
        return TWO * abs(det) / norm_squared(coefficients)

    gate("P3.control.concurrence.product-zero.Bell-one",
         normalized_concurrence(product_coefficients) == ZERO
         and normalized_concurrence(phi_plus) == ONE
         and normalized_concurrence(psi_minus) == ONE)

    print("")
    print("SUMMARY gates=%d pass=%d fail=%d" %
          (GATE_COUNT, GATE_COUNT - len(FAILURES), len(FAILURES)))
    if FAILURES:
        print("FAILED " + ",".join(FAILURES))
        return 1
    print("RESULT ALL_EXACT_GATES_PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
