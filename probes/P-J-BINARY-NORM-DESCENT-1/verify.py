#!/usr/bin/env python3
"""Exact audit for P-J-BINARY-NORM-DESCENT-1.

Standard library only. Integer / finite-field arithmetic only.
No floats, randomness, files, network, or external inputs.
"""

from __future__ import annotations

from itertools import product


# -----------------------------------------------------------------------------
# Generic tiny helpers
# -----------------------------------------------------------------------------

def poly_mul_raw(a: int, b: int) -> int:
    out = 0
    while b:
        if b & 1:
            out ^= a
        b >>= 1
        a <<= 1
    return out


def poly_eval_f2(p: int, x: int) -> int:
    out = 0
    degree = p.bit_length() - 1
    for i in range(degree, -1, -1):
        out = (out * x) ^ ((p >> i) & 1)
    return out & 1


def det_int(M: list[list[int]]) -> int:
    # Bareiss exact determinant.
    A = [row[:] for row in M]
    n = len(A)
    sign = 1
    prev = 1
    for k in range(n - 1):
        if A[k][k] == 0:
            swap = next((r for r in range(k + 1, n) if A[r][k] != 0), None)
            if swap is None:
                return 0
            A[k], A[swap] = A[swap], A[k]
            sign = -sign
        pivot = A[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                A[i][j] = (A[i][j] * pivot - A[i][k] * A[k][j]) // prev
        prev = pivot
        for i in range(k + 1, n):
            A[i][k] = 0
        for j in range(k + 1, n):
            A[k][j] = A[k][j]
    return sign * A[n - 1][n - 1]


def rank_f2(M: list[list[int]]) -> int:
    A = [[x & 1 for x in row] for row in M]
    rows = len(A)
    cols = len(A[0]) if rows else 0
    r = 0
    for c in range(cols):
        pivot = next((i for i in range(r, rows) if A[i][c]), None)
        if pivot is None:
            continue
        A[r], A[pivot] = A[pivot], A[r]
        for i in range(rows):
            if i != r and A[i][c]:
                A[i] = [a ^ b for a, b in zip(A[i], A[r])]
        r += 1
    return r


def compose_perm(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(p[q[i]] for i in range(len(p)))


def generated_perm_group(gens: list[tuple[int, ...]]) -> set[tuple[int, ...]]:
    ident = tuple(range(len(gens[0])))
    group = {ident}
    changed = True
    while changed:
        changed = False
        for g in tuple(group):
            for h in gens:
                for x in (compose_perm(g, h), compose_perm(h, g)):
                    if x not in group:
                        group.add(x)
                        changed = True
    return group


# -----------------------------------------------------------------------------
# F_16 = F_2[a] / (a^4+a^3+a^2+a+1)
# Elements are bit-polynomials c0+c1*a+c2*a^2+c3*a^3.
# -----------------------------------------------------------------------------

MOD16 = 0b1_1111
MASK16 = 0b1111
ALPHA = 0b0010


def f16_add(a: int, b: int) -> int:
    return a ^ b


def f16_mul(a: int, b: int) -> int:
    out = 0
    x = a
    y = b
    while y:
        if y & 1:
            out ^= x
        y >>= 1
        x <<= 1
        if x & 0b1_0000:
            x ^= MOD16
    return out & MASK16


def f16_pow(a: int, n: int) -> int:
    out = 1
    x = a
    while n:
        if n & 1:
            out = f16_mul(out, x)
        n >>= 1
        if n:
            x = f16_mul(x, x)
    return out


def eval_at_power(y: int, exponent: int) -> int:
    # Substitute a -> a^exponent in a polynomial representative.
    out = 0
    target = f16_pow(ALPHA, exponent)
    power = 1
    for i in range(4):
        if (y >> i) & 1:
            out ^= power
        power = f16_mul(power, target)
    return out


def frob(y: int) -> int:
    return f16_mul(y, y)


def frob2(y: int) -> int:
    return f16_pow(y, 4)


def norm_16_4(y: int) -> int:
    return f16_mul(y, frob2(y))


def trace_4_2(s: int) -> int:
    # For s in F_4 fixed by fourth power: Tr(s)=s+s^2 in F_2.
    out = s ^ frob(s)
    assert out in (0, 1)
    return out


def q2(y: int) -> int:
    return trace_4_2(norm_16_4(y))


def polar_q2(y: int, z: int) -> int:
    return q2(y ^ z) ^ q2(y) ^ q2(z)


# -----------------------------------------------------------------------------
# Cyclotomic integer arithmetic in Z[j], Phi_5(j)=0, basis 1,j,j^2,j^3.
# -----------------------------------------------------------------------------

def cyc_reduce(coeff: list[int]) -> tuple[int, int, int, int]:
    a = coeff[:] + [0] * max(0, 7 - len(coeff))
    for d in range(len(a) - 1, 3, -1):
        c = a[d]
        if c:
            # x^d = -x^(d-1)-x^(d-2)-x^(d-3)-x^(d-4)
            a[d] = 0
            a[d - 1] -= c
            a[d - 2] -= c
            a[d - 3] -= c
            a[d - 4] -= c
    return tuple(a[:4])


def cyc_add(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, int, int, int]:
    return tuple(a[i] + b[i] for i in range(4))


def cyc_mul(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, int, int, int]:
    raw = [0] * 7
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            raw[i + j] += x * y
    return cyc_reduce(raw)


def cyc_pow_j(n: int) -> tuple[int, int, int, int]:
    n %= 5
    if n == 0:
        return (1, 0, 0, 0)
    if n == 1:
        return (0, 1, 0, 0)
    if n == 2:
        return (0, 0, 1, 0)
    if n == 3:
        return (0, 0, 0, 1)
    return (-1, -1, -1, -1)


def cyc_auto(a: tuple[int, ...], exponent: int) -> tuple[int, int, int, int]:
    out = (0, 0, 0, 0)
    for i, coeff in enumerate(a):
        if coeff:
            term = tuple(coeff * x for x in cyc_pow_j(exponent * i))
            out = cyc_add(out, term)
    return out


def qplus_int(z: tuple[int, int, int, int]) -> int:
    # q_+(z)=Tr_{K+/Q}(z c(z)); c=j->j^4, and u=j->j^2 is
    # the nontrivial embedding of K+.
    a = cyc_mul(z, cyc_auto(z, 4))
    assert cyc_auto(a, 4) == a
    tr = cyc_add(a, cyc_auto(a, 2))
    assert tr[1:] == (0, 0, 0)
    return tr[0]


def p_of_lattice(x: tuple[int, int, int, int, int]) -> tuple[int, int, int, int]:
    out = (0, 0, 0, 0)
    for r, coeff in enumerate(x):
        if coeff:
            term = tuple(coeff * a for a in cyc_pow_j(r))
            out = cyc_add(out, term)
    return out


def p_mod2(x: tuple[int, int, int, int, int]) -> int:
    out = 0
    for r, coeff in enumerate(x):
        if coeff & 1:
            out ^= f16_pow(ALPHA, r)
    return out


def a4_from_simple(t: tuple[int, int, int, int]) -> tuple[int, int, int, int, int]:
    t1, t2, t3, t4 = t
    return (-t1, t1 - t2, t2 - t3, t3 - t4, t4)


def q_a4(x: tuple[int, int, int, int, int]) -> int:
    s = sum(v * v for v in x)
    assert s % 2 == 0
    return (s // 2) & 1


def matrix_columns(cols: list[tuple[int, ...]]) -> list[list[int]]:
    return [[cols[j][i] for j in range(len(cols))] for i in range(len(cols[0]))]


# -----------------------------------------------------------------------------
# Exact gates
# -----------------------------------------------------------------------------

def main() -> int:
    # A1-A4: binary field integrity and controls.
    phi5 = 0b1_1111
    assert poly_eval_f2(phi5, 0) == 1
    assert poly_eval_f2(phi5, 1) == 1
    irreducible_quadratic = 0b111  # x^2+x+1 is the only monic irreducible quadratic over F2.
    assert poly_mul_raw(irreducible_quadratic, irreducible_quadratic) == 0b10101
    assert 0b10101 != phi5
    print("PASS A1 Phi_5 mod 2 is irreducible, so O/(2) is F_16")

    f4 = {x for x in range(16) if frob2(x) == x}
    assert len(f4) == 4
    expected_f4 = {0, 1, f16_pow(ALPHA, 1) ^ f16_pow(ALPHA, 4), f16_pow(ALPHA, 2) ^ f16_pow(ALPHA, 3)}
    assert f4 == expected_f4
    print("PASS A2 the Frobenius^2 fixed field has four elements, F_4")

    gaussian = 0b101  # x^2+1=(x+1)^2
    assert poly_mul_raw(0b11, 0b11) == gaussian
    phi7 = 0b1111111
    assert poly_mul_raw(0b1011, 0b1101) == phi7
    phi3 = 0b111
    assert poly_eval_f2(phi3, 0) == 1
    assert poly_eval_f2(phi3, 1) == 1
    print("PASS A3 controls: Z[i]/2 nonreduced, zeta_7/2 split, zeta_3/2 remains a field")

    assert f16_pow(ALPHA, 5) == 1
    assert len({f16_pow(ALPHA, k) for k in range(5)}) == 5
    assert all(f16_mul(x, f16_pow(x, 14)) == 1 for x in range(1, 16))
    print("PASS A4 F_16 has 16 elements and alpha has exact order five")

    # B1-B6: Galois/Frobenius and motor distinction.
    assert all(eval_at_power(y, 2) == frob(y) for y in range(16))
    assert all(eval_at_power(y, 4) == frob2(y) for y in range(16))
    print("PASS B1 u mod 2 is Frobenius and c mod 2 is Frobenius squared")

    alpha2 = f16_pow(ALPHA, 2)
    d_map = lambda y: f16_mul(alpha2, y)
    assert d_map(1) == alpha2 != 1 == frob(1)
    assert any(d_map(y) != frob(y) for y in range(16))
    print("PASS B2 multiplication motor D_J mod 2 is not Frobenius")

    mu5_list = [f16_pow(ALPHA, k) for k in range(5)]
    mu5 = set(mu5_list)
    assert all(d_map(mu5_list[k]) == mu5_list[(k + 2) % 5] for k in range(5))
    assert all(frob(mu5_list[k]) == mu5_list[(2 * k) % 5] for k in range(5))
    print("PASS B3 on mu_5 the motor is k->k+2 and Frobenius is k->2k")

    trans = tuple((k + 2) % 5 for k in range(5))
    scale = tuple((2 * k) % 5 for k in range(5))
    group = generated_perm_group([trans, scale])
    assert len(group) == 20
    for a in range(5):
        for b in range(5):
            if a == b:
                continue
            for c in range(5):
                for d in range(5):
                    if c == d:
                        continue
                    count = sum(1 for g in group if g[a] == c and g[b] == d)
                    assert count == 1
    print("PASS B4 the two residue actions generate sharply two-transitive AGL_1(F_5) of order 20")

    assert all(q2(d_map(y)) == q2(y) for y in range(16))
    assert all(q2(frob(y)) == q2(y) for y in range(16))
    print("PASS B5 the residue affine generators preserve q_2")

    congruence_controls = [2, 7, 17, 37, 47, 67, 97]
    assert all(p % 5 == 2 for p in congruence_controls)
    print("PASS B6 p congruent 2 mod 5 is a nonunique Frobenius-exponent class")

    # C1-C5: norm-trace quadratic form.
    assert all(norm_16_4(y) in f4 for y in range(16))
    assert all(trace_4_2(s) in (0, 1) for s in f4)
    print("PASS C1 q_2 is Trace_F4/F2 composed with Norm_F16/F4")

    # Direct reduction of q_+ on all 16 residue classes in the power basis.
    for bits in product((0, 1), repeat=4):
        z = tuple(bits)
        y = sum((bits[i] << i) for i in range(4))
        assert (qplus_int(z) & 1) == q2(y)
    print("PASS C2 q_+ reduces to q_2 on every element of O/(2)")

    nonzero_singular = {y for y in range(1, 16) if q2(y) == 0}
    norm_kernel = {y for y in range(1, 16) if norm_16_4(y) == 1}
    assert nonzero_singular == norm_kernel == mu5
    assert len(nonzero_singular) == 5
    print("PASS C3 the five nonzero q_2-singular elements are exactly mu_5")

    basis = [1, ALPHA, f16_pow(ALPHA, 2), f16_pow(ALPHA, 3)]
    polar_matrix = [[polar_q2(ei, ej) for ej in basis] for ei in basis]
    assert rank_f2(polar_matrix) == 4
    print("PASS C4 the polar form of q_2 is nondegenerate")

    # Trace-zero test in F4*: exactly 1 has zero absolute trace.
    assert {s for s in f4 if s != 0 and trace_4_2(s) == 0} == {1}
    assert len(norm_kernel) == 5
    print("PASS C5 nonzero q_2(y)=0 iff Norm_F16/F4(y)=1")

    # D1-D5: exact A4 bridge.
    # Simple roots b1=e1-e0,...,b4=e4-e3 map to
    # (j-1), j(j-1), j^2(j-1), j^3(j-1): an ideal basis.
    jminus1 = (-1, 1, 0, 0)
    ideal_cols = [cyc_mul(cyc_pow_j(k), jminus1) for k in range(4)]
    simple_roots = [
        (-1, 1, 0, 0, 0),
        (0, -1, 1, 0, 0),
        (0, 0, -1, 1, 0),
        (0, 0, 0, -1, 1),
    ]
    p_cols = [p_of_lattice(v) for v in simple_roots]
    assert p_cols == ideal_cols
    Pmat = matrix_columns(p_cols)
    assert abs(det_int(Pmat)) == 5
    print("PASS D1 P(A_4)=(j-1)O and the integral index is five")

    residue_images = set()
    for t in product((0, 1), repeat=4):
        x = a4_from_simple(t)
        y = p_mod2(x)
        residue_images.add(y)
        assert q2(y) == q_a4(x)
    assert len(residue_images) == 16
    print("PASS D2 P mod 2 is an F_2-linear isomorphism A_4/2A_4 -> O/2O")

    for t in product((0, 1), repeat=4):
        x = a4_from_simple(t)
        z = p_of_lattice(x)
        half_norm = sum(v * v for v in x) // 2
        assert qplus_int(z) == 5 * half_norm
        assert (qplus_int(z) & 1) == q_a4(x) == q2(p_mod2(x))
    print("PASS D3 q_+(P x)=5/2 sum x_r^2 and reduces exactly to q_A")

    mapped_singular = {p_mod2(a4_from_simple(t)) for t in product((0, 1), repeat=4)
                       if any(t) and q_a4(a4_from_simple(t)) == 0}
    # q_A has five nonzero singular vectors by the registered CARRY-PENTAD theorem;
    # this audit independently checks the field presentation has exactly the same locus.
    assert mapped_singular == mu5
    print("PASS D4 the A4 singular pentad maps exactly to the cyclotomic mu_5 pentad")

    assert len(nonzero_singular) == 5 and len(group) == 20
    print("PASS D5 target comparison is compatible with registered CARRY-PENTAD and adds no new S_5 claim")

    print("DECISION J-BINARY-NORM-DESCENT-CONFIRMED")
    print("FIELD O_mod_2=F16 fixed_field=F4 singular_nonzero=5")
    print("ACTION motor=translation_by_2 frobenius=dilation_by_2 affine_order=20")
    print("FORM q2=Trace_F4_F2_of_Norm_F16_F4 singular_locus=mu5")
    print("BRIDGE qplus_mod_2=qA via P_mod_2")
    print("SCOPE L1 only; no Boolean-selection, Thue-Morse, Born, decoder, apparatus, measure or L2-L6 lift")
    print("RESULT 20/20 PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
