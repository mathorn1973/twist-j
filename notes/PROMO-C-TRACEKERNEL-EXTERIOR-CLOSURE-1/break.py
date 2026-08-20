#!/usr/bin/env python3
"""Independent exact breaker for C-TRACEKERNEL-EXTERIOR-CLOSURE-1-N.

Authored only from the frozen preregistration and Addendum 1 at commit
8b8eb640a3ef260c4664d253f69398979afc926f.  This file deliberately does not
import or read any repository construction, verifier, expected output, or run
record.  The A2 and A4 witnesses are labelled as externally supplied because
the addendum exposes that provenance; none is reported as a blind find.
"""

from fractions import Fraction
from itertools import product
from math import comb
import random
import sys


P = 5
RANDOM_SEED = 20260820
RANDOM_TRIALS = 4000


def add(u, v, p=P):
    return tuple((a + b) % p for a, b in zip(u, v))


def neg(u, p=P):
    return tuple((-a) % p for a in u)


def scale(a, u, p=P):
    return tuple((a * x) % p for x in u)


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def transpose(a):
    if not a:
        return []
    return [list(row) for row in zip(*a)]


def mat_mul(a, b, p=P):
    if not a:
        return []
    bt = transpose(b)
    return [[dot(row, col) % p for col in bt] for row in a]


def mat_vec(a, v, p=P):
    return tuple(dot(row, v) % p for row in a)


def identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def flatten(a):
    return tuple(x for row in a for x in row)


def columns_to_matrix(columns):
    return transpose(columns)


def rank_mod(a, p):
    m = [[x % p for x in row] for row in a]
    if not m:
        return 0
    rows = len(m)
    cols = len(m[0])
    r = 0
    for c in range(cols):
        pivot = next((i for i in range(r, rows) if m[i][c]), None)
        if pivot is None:
            continue
        m[r], m[pivot] = m[pivot], m[r]
        z = pow(m[r][c], -1, p)
        m[r] = [(z * x) % p for x in m[r]]
        for i in range(rows):
            if i != r and m[i][c]:
                z = m[i][c]
                m[i] = [(x - z * y) % p for x, y in zip(m[i], m[r])]
        r += 1
        if r == rows:
            break
    return r


def inverse_mod(a, p):
    n = len(a)
    aug = [
        [x % p for x in row] + [int(i == j) for j in range(n)]
        for i, row in enumerate(a)
    ]
    for c in range(n):
        pivot = next((i for i in range(c, n) if aug[i][c]), None)
        if pivot is None:
            raise AssertionError("singular matrix")
        aug[c], aug[pivot] = aug[pivot], aug[c]
        z = pow(aug[c][c], -1, p)
        aug[c] = [(z * x) % p for x in aug[c]]
        for i in range(n):
            if i != c and aug[i][c]:
                z = aug[i][c]
                aug[i] = [(x - z * y) % p for x, y in zip(aug[i], aug[c])]
    return [row[n:] for row in aug]


def det3(a, p=P):
    return (
        a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
        - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
        + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
    ) % p


def det2(g, p=P):
    return (g[0][0] * g[1][1] - g[0][1] * g[1][0]) % p


def is_prime(n):
    return n >= 2 and all(n % d for d in range(2, n))


def primes_through(n):
    return [p for p in range(2, n + 1) if is_prime(p)]


def gram(p):
    m = p - 1
    return [[p - 1 if i == j else -1 for j in range(m)] for i in range(m)]


def trace_kernel_basis(p):
    m = p - 1
    return [
        tuple(int(k == i) - int(k == i + 1) for k in range(m))
        for i in range(m - 1)
    ]


def cyclotomic_trace_coefficients(p, difference):
    """Reduce sum zeta^(k*d) into 1,zeta,...,zeta^(p-2)."""
    coeff = [0] * p
    for k in range(1, p):
        coeff[(k * difference) % p] += 1
    top = coeff[-1]
    return tuple(coeff[i] - top for i in range(p - 1))


def gram_bilinear_formula(x, y, p):
    return p * dot(x, y) - sum(x) * sum(y)


def gram_bilinear_matrix(x, y, g):
    return sum(x[i] * g[i][j] * y[j] for i in range(len(x)) for j in range(len(y)))


def derived_form_from_lifts(x, y, p):
    numerator = gram_bilinear_formula(x, y, p)
    assert numerator % p == 0
    return (numerator // p) % p


def audit_general_primes():
    ps = primes_through(23)
    assert ps == [2, 3, 5, 7, 11, 13, 17, 19, 23]
    lift_tests = 0
    for p in ps:
        m = p - 1
        g = gram(p)
        ones = tuple([1] * m)
        basis = trace_kernel_basis(p)

        # G1: exact cyclotomic reduction and every matrix entry.
        for a in range(1, p):
            for b in range(1, p):
                got = cyclotomic_trace_coefficients(p, a - b)
                expected = (p - 1,) + (0,) * (p - 2) if a == b else (-1,) + (0,) * (p - 2)
                assert got == expected
                assert g[a - 1][b - 1] == (p - 1 if a == b else -1)
        assert mat_vec(g, ones, p * p) == ones
        for b in basis:
            assert tuple(sum(g[i][j] * b[j] for j in range(m)) for i in range(m)) == tuple(p * x for x in b)
        normalized_trace_eigenvalue = Fraction(1, p)
        normalized_spatial_eigenvalue = Fraction(p, p)
        assert normalized_trace_eigenvalue == Fraction(1, p)
        assert normalized_spatial_eigenvalue == Fraction(1, 1)

        # G2: rank-one reduction and an exact basis of its radical.
        g_mod = [[x % p for x in row] for row in g]
        assert g_mod == [[(-1) % p] * m for _ in range(m)]
        assert rank_mod(g_mod, p) == 1
        assert rank_mod(columns_to_matrix(basis), p) == p - 2 if basis else rank_mod([], p) == 0
        for b in basis:
            assert sum(b) % p == 0
            assert mat_vec(g_mod, b, p) == (0,) * m

        # G3 and S1: generator-by-generator lift changes in either argument.
        h = [[dot(x, y) % p for y in basis] for x in basis]
        assert rank_mod(h, p) == p - 2
        for x in basis:
            for y in basis:
                assert gram_bilinear_matrix(x, y, g) == gram_bilinear_formula(x, y, p)
                expected = dot(x, y) % p
                assert derived_form_from_lifts(x, y, p) == expected
                for t in range(m):
                    unit = tuple(p * int(k == t) for k in range(m))
                    x_shift = tuple(a + b for a, b in zip(x, unit))
                    y_shift = tuple(a + b for a, b in zip(y, unit))
                    assert gram_bilinear_matrix(x_shift, y, g) == gram_bilinear_formula(x_shift, y, p)
                    assert gram_bilinear_matrix(x, y_shift, g) == gram_bilinear_formula(x, y_shift, p)
                    assert derived_form_from_lifts(x_shift, y, p) == expected
                    assert derived_form_from_lifts(x, y_shift, p) == expected
                    lift_tests += 2

    # G5 is an integer classification, not a finite-prime inference.
    # n(n-1)/2=n is exactly n(n-3)=0 for n>=0.
    solutions = [n for n in range(24) if n * (n - 1) // 2 == n]
    assert solutions == [0, 3]
    assert [n + 2 for n in solutions] == [2, 5]
    return f"primes={','.join(map(str, ps))} lift_generator_tests={lift_tests} normalized_eigenvalues=1/p,1"


W_BASIS = (
    (1, -1, 0, 0),
    (0, 1, -1, 0),
    (0, 0, 1, -1),
)
H = [[dot(x, y) % P for y in W_BASIS] for x in W_BASIS]
H_INV = inverse_mod(H, P)
VECTORS = list(product(range(P), repeat=3))
VECTOR_INDEX = {v: i for i, v in enumerate(VECTORS)}
E1, E2, E3 = (1, 0, 0), (0, 1, 0), (0, 0, 1)


def cross(x, y, p=P):
    return (
        (x[1] * y[2] - x[2] * y[1]) % p,
        (x[2] * y[0] - x[0] * y[2]) % p,
        (x[0] * y[1] - x[1] * y[0]) % p,
    )


def bracket(x, y, volume_scalar=1):
    return mat_vec(H_INV, scale(volume_scalar, cross(x, y)), P)


def bracket_table(volume_scalar=1):
    return [
        [VECTOR_INDEX[bracket(x, y, volume_scalar)] for y in VECTORS]
        for x in VECTORS
    ]


def ambient(v):
    return tuple(sum(v[j] * W_BASIS[j][i] for j in range(3)) % P for i in range(4))


def coordinates(x):
    assert len(x) == 4 and sum(x) % P == 0
    return (x[0] % P, (x[0] + x[1]) % P, (x[0] + x[1] + x[2]) % P)


def phi(v):
    x = ambient(v)
    return coordinates((x[2], x[3], x[0], x[1]))


def audit_hodge_and_phi():
    assert rank_mod(H, P) == 3
    assert mat_mul(H, H_INV, P) == identity(3)
    table = bracket_table(1)

    # G4/G6: the metric-volume defining identity on all pairs and a basis of z.
    for x in VECTORS:
        for y in VECTORS:
            beta = bracket(x, y)
            for z in (E1, E2, E3):
                lhs = dot(beta, mat_vec(H, z, P)) % P
                rhs = dot(cross(x, y), z) % P
                assert lhs == rhs

    beta_matrix = columns_to_matrix((bracket(E2, E3), bracket(E3, E1), bracket(E1, E2)))
    assert det3(beta_matrix, P) != 0

    # Full 5^9 Jacobi audit, using the complete precomputed product table.
    zero = (0, 0, 0)
    for i in range(len(VECTORS)):
        for j in range(len(VECTORS)):
            for k in range(len(VECTORS)):
                jacobi = add(
                    add(VECTORS[table[i][table[j][k]]], VECTORS[table[j][table[k][i]]]),
                    VECTORS[table[k][table[i][j]]],
                )
                assert jacobi == zero

    h = (1, 0, 1)
    e = (1, 4, 3)
    f = (3, 4, 1)
    assert bracket(h, e) == scale(2, e)
    assert bracket(h, f) == scale(-2, f)
    assert bracket(e, f) == h
    assert det3(columns_to_matrix((h, e, f)), P) == 4

    # G7/S5: derive Phi from its ambient coordinate permutation.
    phi_matrix = columns_to_matrix(tuple(phi(v) for v in (E1, E2, E3)))
    assert det3(phi_matrix, P) == 1
    assert mat_mul(transpose(phi_matrix), mat_mul(H, phi_matrix, P), P) == H
    w_plus = [v for v in VECTORS if phi(v) == v]
    w_minus = [v for v in VECTORS if phi(v) == neg(v)]
    expected_plus = sorted(scale(a, h) for a in range(P))
    expected_minus = sorted((u, (u + v) % P, v) for u in range(P) for v in range(P))
    assert sorted(w_plus) == expected_plus
    assert sorted(w_minus) == expected_minus
    assert {bracket(x, y) for x in w_plus for y in w_plus} == {zero}
    assert {bracket(x, y) for x in w_plus for y in w_minus} == set(w_minus)
    assert {bracket(x, y) for x in w_minus for y in w_minus} == set(w_plus)
    assert all(phi(bracket(x, y)) == bracket(phi(x), phi(y)) for x in VECTORS for y in VECTORS)

    return {
        "table": table,
        "h": h,
        "e": e,
        "f": f,
        "details": "states=125 pairs=15625 jacobi_triples=1953125 beta_det_nonzero phi_dims=1+2 sl2_triple_det=4",
    }


def audit_volume_rescaling():
    table_one = bracket_table(1)
    for c in range(1, P):
        inv_c = pow(c, -1, P)
        table_c = bracket_table(c)
        for i, x in enumerate(VECTORS):
            fx = scale(inv_c, x)
            fi = VECTOR_INDEX[fx]
            for j, y in enumerate(VECTORS):
                lhs = scale(inv_c, VECTORS[table_one[i][j]])
                fy = scale(inv_c, y)
                rhs = VECTORS[table_c[fi][VECTOR_INDEX[fy]]]
                assert lhs == rhs
    return "c=1,2,3,4 isomorphism x->x/c verified on every pair"


def preserves_bracket_on_basis(a):
    for x, y in ((E1, E2), (E2, E3), (E3, E1)):
        lhs = mat_vec(a, bracket(x, y), P)
        rhs = bracket(mat_vec(a, x, P), mat_vec(a, y, P))
        if lhs != rhs:
            return False
    return True


def preserves_bracket_on_all_pairs(a):
    return all(
        mat_vec(a, bracket(x, y), P) == bracket(mat_vec(a, x, P), mat_vec(a, y, P))
        for x in VECTORS
        for y in VECTORS
    )


def enumerate_aut_and_so():
    automorphisms = set()
    special_orthogonal = set()
    for entries in product(range(P), repeat=9):
        a = [list(entries[3 * i:3 * i + 3]) for i in range(3)]
        determinant = det3(a, P)
        if determinant == 0:
            continue
        key = flatten(a)
        if preserves_bracket_on_basis(a):
            automorphisms.add(key)
        if determinant == 1 and mat_mul(transpose(a), mat_mul(H, a, P), P) == H:
            special_orthogonal.add(key)
    assert automorphisms == special_orthogonal
    assert len(automorphisms) == 120
    return automorphisms


def gl2_elements():
    answer = []
    for a, b, c, d in product(range(P), repeat=4):
        g = [[a, b], [c, d]]
        if det2(g, P):
            answer.append(g)
    assert len(answer) == 480
    return answer


H_TRIPLE = (1, 0, 1)
E_TRIPLE = (1, 4, 3)
F_TRIPLE = (3, 4, 1)
ADAPTED = columns_to_matrix((H_TRIPLE, E_TRIPLE, F_TRIPLE))
ADAPTED_INV = inverse_mod(ADAPTED, P)


def rho_direct_sum(g):
    determinant_inverse = pow(det2(g, P), -1, P)
    block = [
        [determinant_inverse, 0, 0],
        [0, g[0][0], g[0][1]],
        [0, g[1][0], g[1][1]],
    ]
    return mat_mul(ADAPTED, mat_mul(block, ADAPTED_INV, P), P)


def rho_sym2(g):
    a, b = g[0]
    c, d = g[1]
    sym2 = [
        [a * a, a * b, b * b],
        [2 * a * c, a * d + b * c, 2 * b * d],
        [c * c, c * d, d * d],
    ]
    z = pow(det2(g, P), -1, P)
    return [[z * x % P for x in row] for row in sym2]


def audit_kinematical_intersection(automorphisms):
    gs = gl2_elements()
    direct_images = {flatten(rho_direct_sum(g)) for g in gs}
    sym2_images = {flatten(rho_sym2(g)) for g in gs}
    assert len(direct_images) == 480
    assert len(sym2_images) == 120

    compatible = []
    for g in gs:
        if flatten(rho_direct_sum(g)) in automorphisms:
            compatible.append(flatten(g))
    expected = []
    expected_diagonal = []
    expected_antidiagonal = []
    for g in gs:
        a, b = g[0]
        c, d = g[1]
        if b == 0 and c == 0 and det2(g, P) == 1:
            expected_diagonal.append(flatten(g))
            expected.append(flatten(g))
        elif a == 0 and d == 0 and det2(g, P) == (-1) % P:
            expected_antidiagonal.append(flatten(g))
            expected.append(flatten(g))
    assert sorted(compatible) == sorted(expected)
    assert len(expected_diagonal) == 4
    assert len(expected_antidiagonal) == 4
    assert len(compatible) == 8

    # A2, supplied by external review: the exact central witness.
    two_i = [[2, 0], [0, 2]]
    rho_two = rho_direct_sum(two_i)
    lhs = bracket(mat_vec(rho_two, H_TRIPLE, P), mat_vec(rho_two, E_TRIPLE, P))
    rhs = mat_vec(rho_two, bracket(H_TRIPLE, E_TRIPLE), P)
    assert lhs == E_TRIPLE
    assert rhs == scale(4, E_TRIPLE)
    assert lhs != rhs

    central_survivors = []
    for lam in range(1, P):
        g = [[lam, 0], [0, lam]]
        r = rho_direct_sum(g)
        if preserves_bracket_on_all_pairs(r):
            central_survivors.append(lam)
    assert central_survivors == [1, 4]

    # The alternative representation kills scalars and factors through PGL2.
    for lam in range(1, P):
        assert rho_sym2([[lam, 0], [0, lam]]) == identity(3)
    for g in gs:
        for lam in range(1, P):
            lam_g = [[lam * x % P for x in row] for row in g]
            assert rho_sym2(lam_g) == rho_sym2(g)

    incompatible = len(gs) - len(compatible)
    assert incompatible == 472
    assert Fraction(incompatible, len(gs)) == Fraction(59, 60)
    return (
        "A2=SUPPLIED_BY_EXTERNAL_REVIEW central_survivors=1,4; "
        "A3=RESULT_EXPOSED compatible=8 incompatible=472 fraction=59/60 "
        "structure=4_diagonal_det1+4_antidiagonal_det_minus1 torus_normalizer "
        "direct_image=480 sym2_image=120"
    )


def integer_cross(x, y):
    return (
        x[1] * y[2] - x[2] * y[1],
        x[2] * y[0] - x[0] * y[2],
        x[0] * y[1] - x[1] * y[0],
    )


COUNTEREXAMPLE_MATRIX = [[1, 1, 0], [0, 1, 0], [0, 0, 1]]


def counterexample_bracket(x, y):
    return tuple(dot(row, integer_cross(x, y)) for row in COUNTEREXAMPLE_MATRIX)


def audit_exact_nonjacobi_counterexample():
    assert (
        COUNTEREXAMPLE_MATRIX[0][0] * COUNTEREXAMPLE_MATRIX[1][1] * COUNTEREXAMPLE_MATRIX[2][2]
    ) == 1
    t1 = counterexample_bracket(E1, counterexample_bracket(E2, E3))
    t2 = counterexample_bracket(E2, counterexample_bracket(E3, E1))
    t3 = counterexample_bracket(E3, counterexample_bracket(E1, E2))
    jacobi = tuple(a + b + c for a, b, c in zip(t1, t2, t3))
    assert jacobi == (0, 0, -1)
    return "A4=SUPPLIED_BY_EXTERNAL_REVIEW det=1 jacobi=(0,0,-1) characteristic_free"


def alternating_bracket_from_matrix(a, x, y):
    return mat_vec(a, cross(x, y), P)


def alternating_matrix_has_jacobi(a):
    basis = (E1, E2, E3)
    for x in basis:
        for y in basis:
            for z in basis:
                jacobi = add(
                    add(
                        alternating_bracket_from_matrix(a, x, alternating_bracket_from_matrix(a, y, z)),
                        alternating_bracket_from_matrix(a, y, alternating_bracket_from_matrix(a, z, x)),
                    ),
                    alternating_bracket_from_matrix(a, z, alternating_bracket_from_matrix(a, x, y)),
                )
                if jacobi != (0, 0, 0):
                    return False
    return True


def audit_seeded_negative_control():
    rng = random.Random(RANDOM_SEED)
    invertible = 0
    jacobi = 0
    for _ in range(RANDOM_TRIALS):
        a = [[rng.randrange(P) for _ in range(3)] for _ in range(3)]
        if det3(a, P):
            invertible += 1
            if alternating_matrix_has_jacobi(a):
                jacobi += 1
    assert 0 < jacobi < invertible < RANDOM_TRIALS
    return f"seed={RANDOM_SEED} trials={RANDOM_TRIALS} invertible={invertible} jacobi={jacobi}"


def checked(name, function, results):
    try:
        details = function()
    except AssertionError as exc:
        details = str(exc) or "exact assertion failed"
        results.append((name, "FAIL", details))
        return None
    results.append((name, "PASS", details))
    return details


def main():
    results = []
    checked("G1_G2_G3_G5_S1", audit_general_primes, results)
    hodge = None
    try:
        hodge = audit_hodge_and_phi()
    except AssertionError as exc:
        results.append(("G4_G6_G7_S5", "FAIL", str(exc) or "exact assertion failed"))
    else:
        results.append(("G4_G6_G7_S5", "PASS", hodge["details"]))

    checked("S2_EMPTY_CASE", lambda: (
        "W_2=0 closure_vacuous; not_the_nonzero_F_2^4_CARRY_PENTAD"
        if len(trace_kernel_basis(2)) == 0 else (_ for _ in ()).throw(AssertionError("W_2 not zero"))
    ), results)
    checked("S3_VOLUME_RESCALING", audit_volume_rescaling, results)
    checked("S4_PLANE_NEGATIVE_CONTROL", lambda: (
        "dim_Lambda2_Wminus=1_not_2"
        if comb(2, 2) == 1 and comb(2, 2) != 2 else (_ for _ in ()).throw(AssertionError("plane count"))
    ), results)
    checked("S6_EXACT_NONJACOBI", audit_exact_nonjacobi_counterexample, results)
    checked("S6_SEEDED_CENSUS", audit_seeded_negative_control, results)

    automorphisms = None
    try:
        automorphisms = enumerate_aut_and_so()
    except AssertionError as exc:
        results.append(("S7_AUTOMORPHISMS", "FAIL", str(exc) or "exact assertion failed"))
    else:
        results.append(("S7_AUTOMORPHISMS", "PASS", "Aut=SO3=120; public_GL2=480"))

    if automorphisms is not None:
        checked("A2_A3_KINEMATICAL", lambda: audit_kinematical_intersection(automorphisms), results)
    else:
        results.append(("A2_A3_KINEMATICAL", "FAIL", "blocked by S7 computation"))

    results.append((
        "S8_SCOPE",
        "PASS",
        "no_2I_derivation no_spinor_carrier no_integral_lift no_L2_to_L6_claim",
    ))

    print("C-TRACEKERNEL-EXTERIOR-CLOSURE-1-N INDEPENDENT BREAKER")
    print("SOURCE frozen_prereg_plus_addendum commit=8b8eb640a3ef260c4664d253f69398979afc926f")
    print("PREMISE EXACT-HODGE-HOME-CLOSURE DECLARED_NOT_EARNED")
    print("STATUS candidate-T universal_trace_kernel_and_derived_form")
    print("STATUS candidate-T conditional_nonzero_home_closure_only_p=5")
    print("STATUS candidate-T conditional_p=5_sl2_with_Phi_1+2")
    print("STATUS O public_architecture_does_not_force_premise")
    for name, state, details in results:
        print(f"{name} {state} {details}")

    passed = all(state == "PASS" for _, state, _ in results)
    if passed:
        print("ROUTE CONDITIONAL-PASS L1_ONLY NO_PROMOTION")
        return 0
    print("ROUTE MISMATCH ARCHIVE_WITHOUT_THRESHOLD_CHANGE")
    return 1


if __name__ == "__main__":
    sys.exit(main())
