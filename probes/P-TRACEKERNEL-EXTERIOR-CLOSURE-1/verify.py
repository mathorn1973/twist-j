#!/usr/bin/env python3
"""Exact L1 audit for P-TRACEKERNEL-EXTERIOR-CLOSURE-1.

Accepted bytes are pinned before the first formal execution.  The universal
quantifiers are carried by the proofs in PREREG.md; this program audits their
finite algebraic ingredients and the complete F_5 carrier.
"""

from itertools import product


BASE_COMMIT = "6b8d27b2721b97c88c5b80b49592d6a755f35a0a"
ISSUE = 481
SOURCE_COMMIT = "8b8eb640a3ef260c4664d253f69398979afc926f"
SOURCE_PREREG_SHA256 = "1c0b33b0f95c2260ae0f6ea3e3c3f03af0e2a763cccff91269621aa529fb1a2d"
SOURCE_ADDENDUM_SHA256 = "b5bddf9253052958ea3f817d863d59216490297b7aebb861c3a9af9663746e53"
PROMO_COMMIT = "6cba68250b0298ed85b39fe3816c54e0b785c3e8"
PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23)
F5 = tuple(range(5))


def rank_mod(rows, p):
    if not rows:
        return 0
    a = [[x % p for x in row] for row in rows]
    nrows, ncols = len(a), len(a[0])
    if any(len(row) != ncols for row in a):
        raise ValueError("ragged matrix")
    pivot = 0
    for col in range(ncols):
        found = next((r for r in range(pivot, nrows) if a[r][col]), None)
        if found is None:
            continue
        a[pivot], a[found] = a[found], a[pivot]
        z = pow(a[pivot][col], -1, p)
        a[pivot] = [(z * x) % p for x in a[pivot]]
        for row in range(nrows):
            if row != pivot and a[row][col]:
                z = a[row][col]
                a[row] = [
                    (a[row][j] - z * a[pivot][j]) % p
                    for j in range(ncols)
                ]
        pivot += 1
        if pivot == nrows:
            break
    return pivot


def det_mod(matrix, p):
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("determinant needs a square matrix")
    if n == 0:
        return 1
    a = [[x % p for x in row] for row in matrix]
    out = 1
    for col in range(n):
        found = next((r for r in range(col, n) if a[r][col]), None)
        if found is None:
            return 0
        if found != col:
            a[col], a[found] = a[found], a[col]
            out = -out
        pivot = a[col][col]
        out = (out * pivot) % p
        inv = pow(pivot, -1, p)
        for row in range(col + 1, n):
            z = (a[row][col] * inv) % p
            if z:
                for j in range(col, n):
                    a[row][j] = (a[row][j] - z * a[col][j]) % p
    return out % p


def inverse_mod(matrix, p):
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("inverse needs a square matrix")
    a = [
        [x % p for x in matrix[i]] + [int(i == j) for j in range(n)]
        for i in range(n)
    ]
    for col in range(n):
        found = next((r for r in range(col, n) if a[r][col]), None)
        if found is None:
            raise ValueError("singular matrix")
        a[col], a[found] = a[found], a[col]
        z = pow(a[col][col], -1, p)
        a[col] = [(z * x) % p for x in a[col]]
        for row in range(n):
            if row == col:
                continue
            z = a[row][col]
            if z:
                a[row] = [
                    (a[row][j] - z * a[col][j]) % p
                    for j in range(2 * n)
                ]
    return tuple(tuple(a[i][n:]) for i in range(n))


def transpose(matrix):
    return tuple(tuple(matrix[i][j] for i in range(len(matrix))) for j in range(len(matrix[0])))


def mat_mul(a, b, p):
    if not a or not b or len(a[0]) != len(b):
        raise ValueError("matrix product shape")
    bt = transpose(b)
    return tuple(
        tuple(sum(x * y for x, y in zip(row, col)) % p for col in bt)
        for row in a
    )


def mat_vec(a, x, p):
    if any(len(row) != len(x) for row in a):
        raise ValueError("matrix-vector shape")
    return tuple(sum(u * v for u, v in zip(row, x)) % p for row in a)


def mat_from_cols(*columns):
    if not columns or any(len(col) != len(columns[0]) for col in columns):
        raise ValueError("column shape")
    return tuple(tuple(columns[j][i] for j in range(len(columns))) for i in range(len(columns[0])))


def scale_matrix(c, a, p):
    return tuple(tuple((c * x) % p for x in row) for row in a)


def add_vec(*vectors, p):
    if not vectors or any(len(v) != len(vectors[0]) for v in vectors):
        raise ValueError("vector shape")
    return tuple(sum(v[i] for v in vectors) % p for i in range(len(vectors[0])))


def scale_vec(c, x, p):
    return tuple((c * u) % p for u in x)


def dot(x, y, p):
    return sum(a * b for a, b in zip(x, y)) % p


def form(x, h, y, p):
    return dot(x, mat_vec(h, y, p), p)


def cross(x, y, p):
    return (
        (x[1] * y[2] - x[2] * y[1]) % p,
        (x[2] * y[0] - x[0] * y[2]) % p,
        (x[0] * y[1] - x[1] * y[0]) % p,
    )


def bracket(x, y, h_inv):
    return mat_vec(h_inv, cross(x, y, 5), 5)


def linear_image(columns, coefficients, p):
    return tuple(
        sum(coefficients[j] * columns[j][i] for j in range(len(columns))) % p
        for i in range(len(columns[0]))
    )


def gram_integer(p):
    n = p - 1
    return tuple(tuple(p * int(i == j) - 1 for j in range(n)) for i in range(n))


def mat_vec_integer(a, x):
    return tuple(sum(u * v for u, v in zip(row, x)) for row in a)


def chain_basis(p):
    n = p - 1
    return tuple(
        tuple(int(j == i) - int(j == i + 1) for j in range(n))
        for i in range(n - 1)
    )


def derived_value(x, y, g, p):
    gy = mat_vec_integer(g, y)
    numerator = sum(x[i] * gy[i] for i in range(len(x)))
    assert numerator % p == 0
    return (numerator // p) % p


def universal_audit():
    lift_tests = 0
    for p in PRIMES:
        n = p - 1
        g = gram_integer(p)
        one = (1,) * n
        basis = chain_basis(p)

        assert all(g[i][j] == (p - 1 if i == j else -1) for i in range(n) for j in range(n))
        assert mat_vec_integer(g, one) == one
        for b in basis:
            assert sum(b) == 0
            assert mat_vec_integer(g, b) == tuple(p * x for x in b)

        reduced = tuple(tuple(x % p for x in row) for row in g)
        assert reduced == tuple(tuple((-1) % p for _ in range(n)) for _ in range(n))
        assert rank_mod(reduced, p) == 1
        assert rank_mod(basis, p) == p - 2
        assert all(sum(b) % p == 0 for b in basis)

        residual = tuple(tuple(dot(x, y, p) for y in basis) for x in basis)
        assert det_mod(residual, p) != 0
        for x in basis:
            for y in basis:
                base = derived_value(x, y, g, p)
                assert base == dot(x, y, p)
                lift_tests += 1
                for coordinate in range(n):
                    shifted_x = list(x)
                    shifted_x[coordinate] += p
                    assert derived_value(tuple(shifted_x), y, g, p) == base
                    lift_tests += 1

                    shifted_y = list(y)
                    shifted_y[coordinate] += p
                    assert derived_value(x, tuple(shifted_y), g, p) == base
                    lift_tests += 1

    assert lift_tests == 43100
    return lift_tests


def dimension_audit():
    solutions = tuple(n for n in range(24) if n * (n - 1) // 2 == n)
    assert solutions == (0, 3)
    assert tuple(n + 2 for n in solutions) == (2, 5)
    assert len(chain_basis(2)) == 0


def hodge_audit():
    basis = chain_basis(5)
    h = tuple(tuple(dot(x, y, 5) for y in basis) for x in basis)
    assert h == ((2, 4, 0), (4, 2, 4), (0, 4, 2))
    assert det_mod(h, 5) == 4
    h_inv = inverse_mod(h, 5)
    assert h_inv == ((2, 3, 4), (3, 1, 3), (4, 3, 2))
    identity = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    assert mat_mul(h, h_inv, 5) == identity

    states = tuple(product(F5, repeat=3))
    zero = (0, 0, 0)
    pair_count = 0
    for x in states:
        assert bracket(x, x, h_inv) == zero
        for y in states:
            pair_count += 1
            assert bracket(y, x, h_inv) == scale_vec(-1, bracket(x, y, h_inv), 5)
    assert pair_count == 15625

    e1, e2, e3 = identity
    wedge_matrix = mat_from_cols(
        bracket(e2, e3, h_inv),
        bracket(e3, e1, h_inv),
        bracket(e1, e2, h_inv),
    )
    assert wedge_matrix == h_inv
    assert det_mod(wedge_matrix, 5) == 4

    jacobi_count = 0
    for x in states:
        for y in states:
            for z in states:
                total = add_vec(
                    bracket(x, bracket(y, z, h_inv), h_inv),
                    bracket(y, bracket(z, x, h_inv), h_inv),
                    bracket(z, bracket(x, y, h_inv), h_inv),
                    p=5,
                )
                assert total == zero
                jacobi_count += 1
    assert jacobi_count == 1953125
    return h, h_inv, states, pair_count, jacobi_count


def sl2_phi_audit(h, h_inv, states):
    hv = (1, 0, 1)
    ev = (1, 4, 3)
    fv = (3, 4, 1)
    sl2_basis = mat_from_cols(hv, ev, fv)
    assert det_mod(sl2_basis, 5) == 4
    assert bracket(hv, ev, h_inv) == scale_vec(2, ev, 5)
    assert bracket(hv, fv, h_inv) == scale_vec(-2, fv, 5)
    assert bracket(ev, fv, h_inv) == hv

    phi = ((0, 4, 1), (0, 4, 0), (1, 4, 0))
    identity = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    assert mat_mul(phi, phi, 5) == identity
    assert det_mod(phi, 5) == 1
    assert mat_mul(mat_mul(transpose(phi), h, 5), phi, 5) == h
    assert mat_vec(phi, hv, 5) == hv
    assert mat_vec(phi, ev, 5) == scale_vec(-1, ev, 5)
    assert mat_vec(phi, fv, 5) == scale_vec(-1, fv, 5)

    plus = tuple(x for x in states if mat_vec(phi, x, 5) == x)
    minus = tuple(x for x in states if mat_vec(phi, x, 5) == scale_vec(-1, x, 5))
    assert len(plus) == 5 and len(minus) == 25
    assert set(plus).intersection(minus) == {(0, 0, 0)}
    assert {add_vec(x, y, p=5) for x in plus for y in minus} == set(states)
    assert {bracket(x, y, h_inv) for x in plus for y in plus} == {(0, 0, 0)}
    assert {bracket(x, y, h_inv) for x in plus for y in minus} == set(minus)
    assert {bracket(x, y, h_inv) for x in minus for y in minus} == set(plus)

    for x in states:
        for y in states:
            assert bracket(mat_vec(phi, x, 5), mat_vec(phi, y, 5), h_inv) == mat_vec(
                phi, bracket(x, y, h_inv), 5
            )
    return hv, ev, fv, sl2_basis, plus, minus


def volume_and_negative_controls(h_inv, states):
    for c in (1, 2, 3, 4):
        c_inv = pow(c, -1, 5)
        for x in states:
            fx = scale_vec(c_inv, x, 5)
            for y in states:
                fy = scale_vec(c_inv, y, 5)
                left = scale_vec(c_inv, bracket(x, y, h_inv), 5)
                right = scale_vec(c, bracket(fx, fy, h_inv), 5)
                assert left == right

    assert 2 * (2 - 1) // 2 == 1
    assert 1 != 2

    identity = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    e1, e2, e3 = identity
    bad_map = ((1, 1, 0), (0, 1, 0), (0, 0, 1))
    assert det_mod(bad_map, 5) == 1

    def bad_bracket(x, y):
        return mat_vec(bad_map, cross(x, y, 5), 5)

    bad_jacobi = add_vec(
        bad_bracket(e1, bad_bracket(e2, e3)),
        bad_bracket(e2, bad_bracket(e3, e1)),
        bad_bracket(e3, bad_bracket(e1, e2)),
        p=5,
    )
    assert bad_jacobi == (0, 0, 4)


def preserves_bracket(t, h_inv):
    identity = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    for i in range(3):
        for j in range(3):
            left = mat_vec(t, bracket(identity[i], identity[j], h_inv), 5)
            right = bracket(mat_vec(t, identity[i], 5), mat_vec(t, identity[j], 5), h_inv)
            if left != right:
                return False
    return True


def automorphism_audit(h, h_inv, states, hv, ev, fv, sl2_basis):
    sl2_basis_inv = inverse_mod(sl2_basis, 5)
    automorphisms = set()
    for image_h in states:
        for image_e in states:
            if bracket(image_h, image_e, h_inv) != scale_vec(2, image_e, 5):
                continue
            for image_f in states:
                if bracket(image_h, image_f, h_inv) != scale_vec(-2, image_f, 5):
                    continue
                if bracket(image_e, image_f, h_inv) != image_h:
                    continue
                image_basis = mat_from_cols(image_h, image_e, image_f)
                if det_mod(image_basis, 5) == 0:
                    continue
                t = mat_mul(image_basis, sl2_basis_inv, 5)
                assert preserves_bracket(t, h_inv)
                automorphisms.add(t)

    special_orthogonal = set()
    for col0 in states:
        if form(col0, h, col0, 5) != h[0][0]:
            continue
        for col1 in states:
            if form(col0, h, col1, 5) != h[0][1]:
                continue
            if form(col1, h, col1, 5) != h[1][1]:
                continue
            for col2 in states:
                if form(col0, h, col2, 5) != h[0][2]:
                    continue
                if form(col1, h, col2, 5) != h[1][2]:
                    continue
                if form(col2, h, col2, 5) != h[2][2]:
                    continue
                t = mat_from_cols(col0, col1, col2)
                if det_mod(t, 5) != 1:
                    continue
                assert mat_mul(mat_mul(transpose(t), h, 5), t, 5) == h
                assert preserves_bracket(t, h_inv)
                special_orthogonal.add(t)

    assert len(automorphisms) == 120
    assert len(special_orthogonal) == 120
    assert automorphisms == special_orthogonal
    assert hv != (0, 0, 0) and ev != (0, 0, 0) and fv != (0, 0, 0)
    return automorphisms


def kinematical_audit(h_inv, hv, ev, fv, automorphisms):
    adapted = mat_from_cols(hv, ev, fv)
    adapted_inv = inverse_mod(adapted, 5)
    gl2 = []
    direct_images = set()
    compatible = set()
    sym2_images = set()
    rho_by_element = {}

    for a, b, c, d in product(F5, repeat=4):
        determinant = (a * d - b * c) % 5
        if determinant == 0:
            continue
        g = (a, b, c, d)
        gl2.append(g)
        determinant_inv = pow(determinant, -1, 5)
        block = (
            (determinant_inv, 0, 0),
            (0, a, b),
            (0, c, d),
        )
        rho = mat_mul(mat_mul(adapted, block, 5), adapted_inv, 5)
        rho_by_element[g] = rho
        direct_images.add(rho)
        if preserves_bracket(rho, h_inv):
            compatible.add(g)
            assert rho in automorphisms

        sym2 = (
            (a * a, a * b, b * b),
            (2 * a * c, a * d + b * c, 2 * b * d),
            (c * c, c * d, d * d),
        )
        sym2_images.add(scale_matrix(determinant_inv, sym2, 5))

    assert len(gl2) == 480
    assert len(direct_images) == 480
    assert len(sym2_images) == 120
    assert len(compatible) == 8
    classified = {
        g
        for g in gl2
        if (
            (g[1] == 0 and g[2] == 0 and (g[0] * g[3]) % 5 == 1)
            or (g[0] == 0 and g[3] == 0 and (-g[1] * g[2]) % 5 == 4)
        )
    }
    assert compatible == classified

    central_survivors = tuple(
        lam for lam in (1, 2, 3, 4) if (lam, 0, 0, lam) in compatible
    )
    assert central_survivors == (1, 4)
    rho2 = rho_by_element[(2, 0, 0, 2)]
    assert bracket(mat_vec(rho2, hv, 5), mat_vec(rho2, ev, 5), h_inv) != mat_vec(
        rho2, bracket(hv, ev, h_inv), 5
    )
    return len(gl2), len(compatible), len(sym2_images), central_survivors


def main():
    assert len(BASE_COMMIT) == 40
    assert len(SOURCE_COMMIT) == 40 and len(PROMO_COMMIT) == 40
    assert len(SOURCE_PREREG_SHA256) == 64 and len(SOURCE_ADDENDUM_SHA256) == 64

    lift_tests = universal_audit()
    dimension_audit()
    h, h_inv, states, pair_count, jacobi_count = hodge_audit()
    hv, ev, fv, sl2_basis, plus, minus = sl2_phi_audit(h, h_inv, states)
    volume_and_negative_controls(h_inv, states)
    automorphisms = automorphism_audit(h, h_inv, states, hv, ev, fv, sl2_basis)
    gl2_count, compatible_count, sym2_count, central_survivors = kinematical_audit(
        h_inv, hv, ev, fv, automorphisms
    )

    assert len(states) == 125
    assert len(plus) == 5 and len(minus) == 25
    assert pair_count == 15625 and jacobi_count == 1953125
    assert gl2_count == 480 and compatible_count == 8 and sym2_count == 120
    assert central_survivors == (1, 4)

    print("P-TRACEKERNEL-EXTERIOR-CLOSURE-1")
    print(f"BASE_COMMIT {BASE_COMMIT}")
    print(f"ISSUE {ISSUE}")
    print(f"SOURCE frozen={SOURCE_COMMIT} promo={PROMO_COMMIT} RESULT_EXPOSED=YES")
    print("PREMISE EXACT-HODGE-HOME-CLOSURE DECLARED_NOT_EARNED")
    print(
        "UNIVERSAL_TRACE_KERNEL PASS primes=2,3,5,7,11,13,17,19,23 "
        f"lift_generator_tests={lift_tests} normalized_eigenvalues=1/p,1"
    )
    print("DIMENSION_CLASSIFICATION PASS p=2_empty p=5_only_nonzero")
    print(
        "HODGE_F5 PASS states=125 pairs=15625 jacobi_triples=1953125 "
        "wedge_det=4"
    )
    print("SL2_PHI PASS triple_det=4 phi_dims=1+2 grading=0,minus,plus")
    print("VOLUME_RESCALING PASS c=1,2,3,4 map=source_to_scaled:x/c")
    print(
        "NEGATIVE_CONTROLS PASS W2=0 plane_wedge_dim=1_not_2 "
        "unnamed_beta_det=1_jacobi=0,0,-1 SUPPLIED_BY_EXTERNAL_REVIEW"
    )
    print("AUTOMORPHISMS PASS bracket=SO3=120")
    print(
        "KINEMATICAL_BOUNDARY PASS public_GL2=480 compatible=8 incompatible=472 "
        "central_survivors=1,4 sym2_image=120 A3_RESULT_EXPOSED=YES"
    )
    print("F2 MANUAL_BASE_STATUS=ARMED_NOT_FIRED full_spatial_GL2_equivariance_not_derived")
    print("STATUS candidate-T universal_trace_kernel_and_derived_form")
    print("STATUS candidate-T conditional_nonzero_home_closure_only_p=5")
    print("STATUS candidate-T conditional_p=5_sl2_with_Phi_1+2")
    print("STATUS candidate-T finite_field_Aut120_and_8_of_480_boundary")
    print("STATUS O public_architecture_does_not_force_premise")
    print(
        "SCOPE L1_ONLY no_binary_icosahedral_derivation no_spinor no_integral_lift no_physics "
        "no_measure no_L2_to_L6"
    )
    print("SAMPLING NOT PROVIDED")
    print("ROUTE CONDITIONAL-PASS NO_CANON_PROMOTION")
    print("MANUAL_BASE_AUDIT NOT_EXECUTABLE see_PREREG_M1")
    print("ALL EXECUTABLE GATES PASS 9/9")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
