#!/usr/bin/env python3
"""Exact audit for P-QDD-J-CENTRALIZER-TERMINALITY-1."""

from fractions import Fraction as Q
import inspect

from exact_matrix import (
    add, basis, cols, coord_proj, dot, eye, inv, kron, mat, mm, mpow, mv,
    neg, perm, pointer_block, rank, scale, sharp, sub, sum_mats, tr, zero,
)

BASE = "2fbee86973a5372bf0c96ddbd39b1610fecf72e2"
ISSUE = 459
UNITS = (1, 2, 3, 4)
F5 = (0, 1, 2, 3, 4)
SIGNS = (-1, 1)


def image(c, b, x):
    return (b + c * x) % 5


def hoff(a, k):
    return k * (1 - a) % 5


def flatten(a):
    return tuple(x for row in a for x in row)


def centralizer_equations(p, g):
    """Rows for XP=0, PX=0, and Xg-gX=0 on sixteen matrix variables."""
    rows = []
    for i in range(4):
        for j in range(4):
            row = [Q(0)] * 16
            for m in range(4):
                row[4 * i + m] += p[m][j]
            rows.append(tuple(row))
    for i in range(4):
        for j in range(4):
            row = [Q(0)] * 16
            for m in range(4):
                row[4 * m + j] += p[i][m]
            rows.append(tuple(row))
    for i in range(4):
        for j in range(4):
            row = [Q(0)] * 16
            for m in range(4):
                row[4 * i + m] += g[m][j]
                row[4 * m + j] -= g[i][m]
            rows.append(tuple(row))
    return tuple(rows)


def build_centralizer_class():
    """Build only from J, F5, affine symmetry, pointer, and memory."""
    i4 = eye(4)
    one4 = tuple(tuple(Q(1) for _ in range(4)) for _ in range(4))
    gram = sub(i4, scale(Q(1, 5), one4))
    gram_inv = inv(gram)
    m_j = mat(((1, 0, -1, 1), (0, 1, -1, 0), (1, 0, 0, 0), (0, 1, -1, 1)))
    d_j = sub(m_j, i4)
    vertices = tuple(mv(mpow(d_j, k), basis(4, 0)) for k in F5)
    vertex_basis = cols(vertices[:4])
    vertex_basis_inv = inv(vertex_basis)

    def rho(c, b):
        moved = tuple(vertices[image(c, b, x)] for x in range(4))
        return mm(cols(moved), vertex_basis_inv)

    affine = {(c, b): rho(c, b) for c in UNITS for b in F5}
    stabilizer = {(a, k): affine[(a, hoff(a, k))] for a in UNITS for k in F5}
    p = {
        k: scale(Q(1, 4), sum_mats((stabilizer[(a, k)] for a in UNITS), 4, 4))
        for k in F5
    }
    q = {k: sub(i4, p[k]) for k in F5}
    generator = {k: stabilizer[(2, k)] for k in F5}
    r_sign = {}
    c_plane = {}
    j_plane = {}
    for k in F5:
        gk = generator[k]
        alternating = sub(add(sub(i4, gk), mpow(gk, 2)), mpow(gk, 3))
        r_sign[k] = scale(Q(1, 4), alternating)
        c_plane[k] = sub(q[k], r_sign[k])
        j_plane[k] = mm(gk, c_plane[k])

    i2 = eye(2)
    x_pointer = mat(((0, 1), (1, 0)))
    i5 = eye(5)
    memory_action = {
        key: perm(tuple(image(key[0], key[1], x) for x in F5))
        for key in affine
    }
    total_affine = {
        key: kron(kron(affine[key], i2), memory_action[key])
        for key in affine
    }
    total_gram = kron(kron(gram, i2), i5)
    total_gram_inv = kron(kron(gram_inv, i2), i5)

    return {
        "I4": i4,
        "G": gram,
        "GI": gram_inv,
        "DJ": d_j,
        "VERTICES": vertices,
        "AFFINE": affine,
        "H": stabilizer,
        "P": p,
        "Q": q,
        "GEN": generator,
        "R": r_sign,
        "C": c_plane,
        "J": j_plane,
        "I2": i2,
        "X": x_pointer,
        "I5": i5,
        "TA": total_affine,
        "GT": total_gram,
        "GTI": total_gram_inv,
    }


def moving(data, k, e, r, s):
    return add(
        scale(e, data["R"][k]),
        add(scale(r, data["C"][k]), scale(s, data["J"][k])),
    )


def coupling(data, e, r, s):
    blocks = {}
    for k in F5:
        tk = moving(data, k, e, r, s)
        blocks[k] = add(kron(data["P"][k], data["I2"]), kron(tk, data["X"]))
    total = sum_mats(
        (kron(blocks[k], coord_proj(5, k)) for k in F5),
        40,
        40,
    )
    return blocks, total


def circle(t):
    t = Q(t)
    den = 1 + t * t
    return Q(1), (1 - t * t) / den, 2 * t / den


def same_ray(a, b):
    return rank(cols((a, b))) <= 1


def main():
    source = inspect.getsource(build_centralizer_class)
    forbidden = ("E_low", "E_high", "TARGET_LOW", "TARGET_HIGH", "TARGET_TOKEN")
    assert all(token not in source for token in forbidden)
    data = build_centralizer_class()
    i4, gram, gram_inv = data["I4"], data["G"], data["GI"]
    d_j, vertices = data["DJ"], data["VERTICES"]
    affine, stabilizer = data["AFFINE"], data["H"]
    p, q, gen = data["P"], data["Q"], data["GEN"]
    r_sign, c_plane, j_plane = data["R"], data["C"], data["J"]
    gates = 1

    assert mpow(d_j, 5) == i4
    assert mm(mm(tr(d_j), gram), d_j) == gram
    assert tuple(sum((vertices[k][i] for k in F5), Q(0)) for i in range(4)) == (Q(0),) * 4
    for x in F5:
        for y in F5:
            expected = Q(4, 5) if x == y else Q(-1, 5)
            assert dot(vertices[x], gram, vertices[y]) == expected
    assert vertices[2] == (Q(-1),) * 4
    gates += 1

    assert len(set(affine.values())) == 20
    for (a, b), rho_ab in affine.items():
        assert mm(mm(tr(rho_ab), gram), rho_ab) == gram
        assert all(mv(rho_ab, vertices[x]) == vertices[image(a, b, x)] for x in F5)
        for aa in UNITS:
            for bb in F5:
                product = (a * aa % 5, (b + a * bb) % 5)
                assert mm(rho_ab, affine[(aa, bb)]) == affine[product]
    gates += 1

    for k in F5:
        assert mm(p[k], p[k]) == p[k]
        assert sharp(p[k], gram, gram_inv) == p[k]
        assert rank(p[k]) == 1
        assert mv(p[k], vertices[k]) == vertices[k]
        assert mm(q[k], q[k]) == q[k]
        assert sharp(q[k], gram, gram_inv) == q[k]
        assert rank(q[k]) == 3
        assert add(p[k], q[k]) == i4
        for a in UNITS:
            assert mm(stabilizer[(a, k)], p[k]) == mm(p[k], stabilizer[(a, k)])
    gates += 1

    for k in F5:
        rk, ck, jk = r_sign[k], c_plane[k], j_plane[k]
        assert rank(rk) == 1 and rank(ck) == 2
        assert mm(rk, rk) == rk and sharp(rk, gram, gram_inv) == rk
        assert mm(ck, ck) == ck and sharp(ck, gram, gram_inv) == ck
        assert add(rk, ck) == q[k]
        assert mm(rk, ck) == zero(4, 4) and mm(ck, rk) == zero(4, 4)
        assert mm(rk, jk) == zero(4, 4) and mm(jk, rk) == zero(4, 4)
        assert mm(ck, jk) == jk and mm(jk, ck) == jk
        assert mm(jk, jk) == neg(ck)
        assert sharp(jk, gram, gram_inv) == neg(jk)
    gates += 1

    centralizer_dims = []
    for k in F5:
        equations = centralizer_equations(p[k], gen[k])
        dim = 16 - rank(equations)
        centralizer_dims.append(dim)
        basis_vectors = (flatten(r_sign[k]), flatten(c_plane[k]), flatten(j_plane[k]))
        assert rank(cols(basis_vectors)) == 3
        for vector in basis_vectors:
            assert all(sum((row[i] * vector[i] for i in range(16)), Q(0)) == 0 for row in equations)
    assert centralizer_dims == [3] * 5
    gates += 1

    for (a, b), rho_ab in affine.items():
        rho_inv = inv(rho_ab)
        for k in F5:
            target = image(a, b, k)
            assert mm(mm(rho_ab, r_sign[k]), rho_inv) == r_sign[target]
            assert mm(mm(rho_ab, c_plane[k]), rho_inv) == c_plane[target]
            assert mm(mm(rho_ab, j_plane[k]), rho_inv) == j_plane[target]
    gates += 1

    samples = (
        (Q(1), Q(1), Q(0)),
        (Q(1), Q(-1), Q(0)),
        (Q(-1), Q(1), Q(0)),
        (Q(-1), Q(-1), Q(0)),
        circle(1),
        circle(2),
        circle(-2),
    )
    for e, r, s in samples:
        assert e * e == 1 and r * r + s * s == 1
        blocks, total = coupling(data, e, r, s)
        assert mm(mm(tr(total), data["GT"]), total) == data["GT"]
        assert all(mm(transport, total) == mm(total, transport) for transport in data["TA"].values())
        for k in F5:
            tk = moving(data, k, e, r, s)
            assert mm(sharp(tk, gram, gram_inv), tk) == q[k]
            assert mm(p[k], tk) == zero(4, 4) and mm(tk, p[k]) == zero(4, 4)
            assert mm(q[k], tk) == tk and mm(tk, q[k]) == tk
            k0 = pointer_block(blocks[k], 0)
            k1 = pointer_block(blocks[k], 1)
            assert k0 == p[k] and k1 == tk
            assert mm(sharp(k0, gram, gram_inv), k0) == p[k]
            assert mm(sharp(k1, gram, gram_inv), k1) == q[k]
    gates += 1

    injected = []
    for t in (Q(-3), Q(-2), Q(-1), Q(0), Q(1), Q(2), Q(3)):
        e, r, s = circle(t)
        injected.append(moving(data, 0, e, r, s))
        assert t == s / (1 + r)
    for i, left in enumerate(injected):
        for right in injected[i + 1:]:
            assert left != right and left != neg(right)
    gates += 1

    discrete = {}
    for e in SIGNS:
        for r in SIGNS:
            tk = moving(data, 0, Q(e), Q(r), Q(0))
            assert sharp(tk, gram, gram_inv) == tk
            assert mm(tk, tk) == q[0]
            discrete[(e, r)] = tk
    physical_keys = {min(flatten(tk), flatten(neg(tk))) for tk in discrete.values()}
    assert len(discrete) == 4 and len(physical_keys) == 2
    assert discrete[(1, 1)] == q[0]
    assert discrete[(1, -1)] != q[0] and discrete[(1, -1)] != neg(q[0])
    for _, r, s in (circle(1), circle(2)):
        tk = moving(data, 0, Q(1), r, s)
        assert sharp(tk, gram, gram_inv) != tk
    gates += 1

    # Ordinary outcome repeatability holds for every class member, but it is nonselective.
    for e, r, s in samples:
        for k in F5:
            tk = moving(data, k, e, r, s)
            assert mm(q[k], tk) == tk
            assert mm(p[k], p[k]) == p[k]
    assert len({flatten(moving(data, 0, *params)) for params in samples}) > 1
    gates += 1

    # Ray terminality leaves exactly the physical Lueder class represented by +/-Q.
    ray_terminal = []
    test_vectors = tuple(basis(4, i) for i in range(4)) + (
        tuple(Q(1) for _ in range(4)),
        (Q(1), Q(1), Q(0), Q(0)),
        (Q(1), Q(0), Q(1), Q(0)),
    )
    for key, tk in discrete.items():
        terminal = True
        for v in test_vectors:
            w = mv(tk, v)
            if w == (Q(0),) * 4:
                continue
            ww = mv(tk, w)
            if not same_ray(ww, w):
                terminal = False
                break
        if terminal:
            ray_terminal.append(key)
    assert set(ray_terminal) == {(1, 1), (-1, -1)}
    assert len({min(flatten(discrete[key]), flatten(neg(discrete[key]))) for key in ray_terminal}) == 1
    gates += 1

    # Strict branch idempotence fixes the positive representative.
    strict_terminal = []
    for key, tk in discrete.items():
        if mm(tk, tk) == tk:
            strict_terminal.append(key)
    assert strict_terminal == [(1, 1)]
    assert discrete[(1, 1)] == q[0]
    gates += 1

    # Target comparison is deliberately last.
    one4 = tuple(tuple(Q(1) for _ in range(4)) for _ in range(4))
    target_low = scale(Q(1, 4), one4)
    target_high = sub(i4, target_low)
    token = 2
    assert p[token] == target_low and q[token] == target_high
    for e, r, s in samples:
        tk = moving(data, token, e, r, s)
        assert mm(sharp(tk, gram, gram_inv), tk) == target_high
    assert moving(data, token, Q(1), Q(1), Q(0)) == target_high
    gates += 1

    assert gates == 14
    print("P-QDD-J-CENTRALIZER-TERMINALITY-1")
    print(f"BASE_COMMIT {BASE}")
    print(f"ISSUE {ISSUE}")
    print("CLASS_INPUTS M_J,D_J,G,F5,AGL1,C4-centralizer,pointer-C2,memory-F5")
    print("CLASS_TARGET_INDEPENDENCE PASS")
    print("PHASE_MOTOR order=5 simplex_vertices=5")
    print("CENTRALIZER_DIMENSIONS 3,3,3,3,3")
    print("CENTRALIZER_ALGEBRA Q-sign-plus-Q(i)-plane")
    print("CLASS_PARAMETERS e=+-1 r,s-in-Q r2+s2=1")
    print("TARGET_TOKEN 2")
    print("TARGET_EFFECTS realized=INFINITE")
    print("NEGATIVE_ROUTE poststate_classes=INFINITE")
    print("ORDINARY_REPEATABILITY selects=NO")
    print("SELFADJOINT_INVOLUTIVE algebraic=4 physical=2")
    print("RAY_TERMINALITY physical_classes=1 representative=+-Q")
    print("STRICT_TERMINALITY algebraic_members=1 representative=Q")
    print("LUEDER_SELECTION conditional=TERMINALITY")
    print("TERMINALITY_STATUS EXTRA_LAW_NOT_DERIVED")
    print("DECISION BIFURCATION-PASS")
    print("O2_GLOBAL_STATUS UNCHANGED")
    print("SAMPLING NOT PROVIDED")
    print("CANDIDATE_CEILING T restricted-class theorems")
    print("ALL PASS 14/14")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
