#!/usr/bin/env python3
"""Exact audit for P-QDD-RECORD-COMPLETE-STABILIZER-1."""

from fractions import Fraction as Q
from itertools import permutations
import inspect

BASE = "1ca497af6e3b9f9ec389e9fd1cc241003aca1688"
ISSUE = 474
F5 = tuple(range(5))
UNITS = (1, 2, 3, 4)
SIGNS = (-1, 1)


def mat(rows):
    out = tuple(tuple(x if isinstance(x, Q) else Q(x) for x in row) for row in rows)
    if not out or not out[0] or any(len(row) != len(out[0]) for row in out):
        raise ValueError("bad matrix")
    return out


def shape(a):
    return len(a), len(a[0])


def zero(r, c):
    return tuple(tuple(Q(0) for _ in range(c)) for _ in range(r))


def eye(n):
    return tuple(tuple(Q(i == j) for j in range(n)) for i in range(n))


def tr(a):
    r, c = shape(a)
    return tuple(tuple(a[i][j] for i in range(r)) for j in range(c))


def add(a, b):
    if shape(a) != shape(b):
        raise ValueError("shape")
    r, c = shape(a)
    return tuple(tuple(a[i][j] + b[i][j] for j in range(c)) for i in range(r))


def scale(x, a):
    x = x if isinstance(x, Q) else Q(x)
    r, c = shape(a)
    return tuple(tuple(x * a[i][j] for j in range(c)) for i in range(r))


def neg(a):
    return scale(-1, a)


def sub(a, b):
    return add(a, neg(b))


def mm(a, b):
    ar, ac = shape(a)
    br, bc = shape(b)
    if ac != br:
        raise ValueError("product shape")
    bt = tr(b)
    return tuple(
        tuple(sum((a[i][k] * bt[j][k] for k in range(ac)), Q(0)) for j in range(bc))
        for i in range(ar)
    )


def mv(a, v):
    r, c = shape(a)
    if c != len(v):
        raise ValueError("vector shape")
    return tuple(sum((a[i][j] * v[j] for j in range(c)), Q(0)) for i in range(r))


def mpow(a, n):
    r, c = shape(a)
    if r != c or n < 0:
        raise ValueError("power")
    out, base = eye(r), a
    while n:
        if n & 1:
            out = mm(out, base)
        base = mm(base, base)
        n >>= 1
    return out


def inv(a):
    n, m = shape(a)
    if n != m:
        raise ValueError("inverse")
    aug = [list(a[i]) + list(eye(n)[i]) for i in range(n)]
    for c in range(n):
        p = next((r for r in range(c, n) if aug[r][c]), None)
        if p is None:
            raise ValueError("singular")
        aug[c], aug[p] = aug[p], aug[c]
        q = aug[c][c]
        aug[c] = [x / q for x in aug[c]]
        for r in range(n):
            if r == c:
                continue
            q = aug[r][c]
            if q:
                aug[r] = [aug[r][j] - q * aug[c][j] for j in range(2 * n)]
    return tuple(tuple(aug[i][n:]) for i in range(n))


def rank(a):
    r, c = shape(a)
    w = [list(row) for row in a]
    p = 0
    for j in range(c):
        q = next((i for i in range(p, r) if w[i][j]), None)
        if q is None:
            continue
        w[p], w[q] = w[q], w[p]
        z = w[p][j]
        w[p] = [x / z for x in w[p]]
        for i in range(r):
            if i != p and w[i][j]:
                z = w[i][j]
                w[i] = [w[i][k] - z * w[p][k] for k in range(c)]
        p += 1
        if p == r:
            break
    return p


def cols(vs):
    if not vs or any(len(v) != len(vs[0]) for v in vs):
        raise ValueError("columns")
    return tuple(tuple(vs[j][i] for j in range(len(vs))) for i in range(len(vs[0])))


def kron(a, b):
    ar, ac = shape(a)
    br, bc = shape(b)
    return tuple(
        tuple(a[i // br][j // bc] * b[i % br][j % bc] for j in range(ac * bc))
        for i in range(ar * br)
    )


def sum_mats(xs, r, c):
    out = zero(r, c)
    for x in xs:
        out = add(out, x)
    return out


def basis(n, i):
    return tuple(Q(j == i) for j in range(n))


def sharp(a, g, gi):
    return mm(mm(gi, tr(a)), g)


def dot(v, g, w):
    gw = mv(g, w)
    return sum((v[i] * gw[i] for i in range(len(v))), Q(0))


def flatten(a):
    return tuple(x for row in a for x in row)


def compose(p, q):
    """Permutation composition p after q."""
    return tuple(p[q[x]] for x in range(len(p)))


def affine_perm(a, k):
    return tuple((k + a * (x - k)) % 5 for x in F5)


def centralizer_equations(p, group):
    """Rows for XP=0, PX=0 and Xg-gX=0 on sixteen variables."""
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
    for g in group:
        for i in range(4):
            for j in range(4):
                row = [Q(0)] * 16
                for m in range(4):
                    row[4 * i + m] += g[m][j]
                    row[4 * m + j] -= g[i][m]
                rows.append(tuple(row))
    return tuple(rows)


def annihilates(rows, vector):
    return all(
        sum((row[i] * vector[i] for i in range(len(vector))), Q(0)) == 0
        for row in rows
    )


def build_record_class():
    """Build from J, the regular simplex and record partitions only."""
    i4 = eye(4)
    one4 = tuple(tuple(Q(1) for _ in range(4)) for _ in range(4))
    gram = sub(i4, scale(Q(1, 5), one4))
    gram_inv = inv(gram)
    m_j = mat(((1, 0, -1, 1), (0, 1, -1, 0), (1, 0, 0, 0), (0, 1, -1, 1)))
    d_j = sub(m_j, i4)
    vertices = tuple(mv(mpow(d_j, k), basis(4, 0)) for k in F5)
    vertex_basis = cols(vertices[:4])
    vertex_basis_inv = inv(vertex_basis)

    all_perms = tuple(permutations(F5))

    def rho(pi):
        moved = tuple(vertices[pi[x]] for x in range(4))
        return mm(cols(moved), vertex_basis_inv)

    simplex = {pi: rho(pi) for pi in all_perms}
    stabilizers = {
        k: tuple(pi for pi in all_perms if pi[k] == k)
        for k in F5
    }
    p = {
        k: scale(Q(1, 24), sum_mats((simplex[pi] for pi in stabilizers[k]), 4, 4))
        for k in F5
    }
    q = {k: sub(i4, p[k]) for k in F5}

    affine = {
        k: tuple(affine_perm(a, k) for a in UNITS)
        for k in F5
    }
    affine_mats = {
        k: tuple(simplex[pi] for pi in affine[k])
        for k in F5
    }
    generator = {k: simplex[affine_perm(2, k)] for k in F5}
    r_sign = {}
    c_plane = {}
    j_plane = {}
    for k in F5:
        gk = generator[k]
        alternating = sub(add(sub(i4, gk), mpow(gk, 2)), mpow(gk, 3))
        r_sign[k] = scale(Q(1, 4), alternating)
        c_plane[k] = sub(q[k], r_sign[k])
        j_plane[k] = mm(gk, c_plane[k])

    return {
        "I4": i4,
        "G": gram,
        "GI": gram_inv,
        "DJ": d_j,
        "VERTICES": vertices,
        "PERMS": all_perms,
        "SIMPLEX": simplex,
        "STAB": stabilizers,
        "P": p,
        "Q": q,
        "AFFINE": affine,
        "AFFINE_MATS": affine_mats,
        "GEN": generator,
        "R": r_sign,
        "C": c_plane,
        "J": j_plane,
    }


def main():
    source = inspect.getsource(build_record_class)
    forbidden = ("E_low", "E_high", "TARGET_LOW", "TARGET_HIGH", "TARGET_TOKEN")
    assert all(token not in source for token in forbidden)

    data = build_record_class()
    i4, gram, gram_inv = data["I4"], data["G"], data["GI"]
    d_j, vertices = data["DJ"], data["VERTICES"]
    all_perms, simplex = data["PERMS"], data["SIMPLEX"]
    stabilizers, p, q = data["STAB"], data["P"], data["Q"]
    affine, affine_mats = data["AFFINE"], data["AFFINE_MATS"]
    r_sign, c_plane, j_plane = data["R"], data["C"], data["J"]
    gates = 1

    # J phase motor and regular simplex.
    assert mpow(d_j, 5) == i4
    assert mm(mm(tr(d_j), gram), d_j) == gram
    assert tuple(sum((vertices[k][i] for k in F5), Q(0)) for i in range(4)) == (Q(0),) * 4
    for x in F5:
        for y in F5:
            assert dot(vertices[x], gram, vertices[y]) == (Q(4, 5) if x == y else Q(-1, 5))
    assert vertices[2] == (Q(-1),) * 4
    gates += 1

    # Complete S5 representation and group law.
    assert len(all_perms) == 120
    assert len(set(simplex.values())) == 120
    identity = tuple(F5)
    assert simplex[identity] == i4
    for pi in all_perms:
        rpi = simplex[pi]
        assert mm(mm(tr(rpi), gram), rpi) == gram
        assert all(mv(rpi, vertices[x]) == vertices[pi[x]] for x in F5)
    for pi in all_perms:
        for tau in all_perms:
            assert mm(simplex[pi], simplex[tau]) == simplex[compose(pi, tau)]
    gates += 1

    # Five complete record-partition stabilizers and their projectors.
    assert tuple(len(stabilizers[k]) for k in F5) == (24,) * 5
    for k in F5:
        assert all(pi[k] == k for pi in stabilizers[k])
        assert len({tuple(pi[x] for x in F5 if x != k) for pi in stabilizers[k]}) == 24
        assert mm(p[k], p[k]) == p[k]
        assert sharp(p[k], gram, gram_inv) == p[k]
        assert rank(p[k]) == 1
        assert mv(p[k], vertices[k]) == vertices[k]
        assert mm(q[k], q[k]) == q[k]
        assert sharp(q[k], gram, gram_inv) == q[k]
        assert rank(q[k]) == 3
        assert add(p[k], q[k]) == i4
        for pi in stabilizers[k]:
            assert mm(simplex[pi], p[k]) == mm(p[k], simplex[pi])
    gates += 1

    # Complete S4 moving-support centralizers have dimension one.
    full_dims = []
    for k in F5:
        group = tuple(simplex[pi] for pi in stabilizers[k])
        equations = centralizer_equations(p[k], group)
        dim = 16 - rank(equations)
        full_dims.append(dim)
        qv = flatten(q[k])
        assert annihilates(equations, qv)
        assert rank(cols((qv,))) == 1
    assert full_dims == [1] * 5
    gates += 1

    # The complete record class is exactly +/-Q, one physical class.
    physical = set()
    for k in F5:
        for sign in SIGNS:
            tk = scale(sign, q[k])
            assert mm(sharp(tk, gram, gram_inv), tk) == q[k]
            assert all(mm(tk, simplex[pi]) == mm(simplex[pi], tk) for pi in stabilizers[k])
            physical.add(min(flatten(tk), flatten(neg(tk))))
        assert len({
            min(flatten(scale(sign, q[k])), flatten(neg(scale(sign, q[k]))))
            for sign in SIGNS
        }) == 1
        assert mm(q[k], q[k]) == q[k]
        assert mm(neg(q[k]), neg(q[k])) == q[k] and mm(neg(q[k]), neg(q[k])) != neg(q[k])
    assert len(physical) == 5
    gates += 1

    # Reversible binary pointer realization for both signs.
    i2 = eye(2)
    xptr = mat(((0, 1), (1, 0)))
    gt = kron(gram, i2)
    gti = kron(gram_inv, i2)
    for k in F5:
        for sign in SIGNS:
            tk = scale(sign, q[k])
            u = add(kron(p[k], i2), kron(tk, xptr))
            assert mm(sharp(u, gt, gti), u) == eye(8)
            assert mm(sharp(p[k], gram, gram_inv), p[k]) == p[k]
            assert mm(sharp(tk, gram, gram_inv), tk) == q[k]
            assert mm(sharp(p[k], gram, gram_inv), tk) == zero(4, 4)
    gates += 1

    # Affine C4 centralizer has dimension three with R,C,J basis.
    affine_dims = []
    for k in F5:
        equations = centralizer_equations(p[k], affine_mats[k])
        dim = 16 - rank(equations)
        affine_dims.append(dim)
        basis_vectors = (flatten(r_sign[k]), flatten(c_plane[k]), flatten(j_plane[k]))
        assert rank(cols(basis_vectors)) == 3
        assert all(annihilates(equations, vector) for vector in basis_vectors)
        assert add(r_sign[k], c_plane[k]) == q[k]
        assert mm(j_plane[k], j_plane[k]) == neg(c_plane[k])
        assert sharp(j_plane[k], gram, gram_inv) == neg(j_plane[k])
    assert affine_dims == [3] * 5
    gates += 1

    # R-C is an exact nonterminal affine witness and fails full S4 covariance.
    noncommuting_counts = []
    for k in F5:
        tstar = sub(r_sign[k], c_plane[k])
        assert sharp(tstar, gram, gram_inv) == tstar
        assert mm(sharp(tstar, gram, gram_inv), tstar) == q[k]
        assert mm(tstar, tstar) == q[k]
        assert tstar != q[k] and tstar != neg(q[k])
        assert all(mm(tstar, g) == mm(g, tstar) for g in affine_mats[k])
        count = sum(
            mm(tstar, simplex[pi]) != mm(simplex[pi], tstar)
            for pi in stabilizers[k]
        )
        noncommuting_counts.append(count)
        assert count > 0
    gates += 1

    # S5 transport carries the complete partition objects across tokens.
    for pi in all_perms:
        rpi = simplex[pi]
        rpi_inv = inv(rpi)
        for k in F5:
            target = pi[k]
            assert mm(mm(rpi, p[k]), rpi_inv) == p[target]
            assert mm(mm(rpi, q[k]), rpi_inv) == q[target]
    gates += 1

    # Strict representative idempotence chooses +Q, while the sign quotient is one class.
    for k in F5:
        positive = q[k]
        negative = neg(q[k])
        assert mm(positive, positive) == positive
        assert mm(negative, negative) == positive
        assert mm(negative, negative) != negative
        assert min(flatten(positive), flatten(negative)) == min(flatten(negative), flatten(positive))
    gates += 1

    # Target comparison deliberately last.
    one4 = tuple(tuple(Q(1) for _ in range(4)) for _ in range(4))
    target_low = scale(Q(1, 4), one4)
    target_high = sub(i4, target_low)
    token = 2
    assert p[token] == target_low
    assert q[token] == target_high
    gates += 1

    # Scope and final integrity.
    assert gates == 12

    print("P-QDD-RECORD-COMPLETE-STABILIZER-1")
    print(f"BASE_COMMIT {BASE}")
    print(f"ISSUE {ISSUE}")
    print("CLASS_INPUTS M_J,D_J,G,regular-simplex,S5,record-partition,pointer-C2")
    print("CLASS_TARGET_INDEPENDENCE PASS")
    print("SIMPLEX_AUTOMORPHISMS order=120 group=S5")
    print("PARTITION_STABILIZERS tokens=5 order=24 group=S4")
    print("FULL_CENTRALIZER_DIMENSIONS " + ",".join(str(x) for x in full_dims))
    print("RECORD_COMPLETE_CLASS algebraic=2 physical=1 representatives=+Q,-Q")
    print("STRICT_IDEMPOTENCE representative=+Q")
    print("AFFINE_STABILIZERS tokens=5 order=4 group=C4")
    print("AFFINE_CENTRALIZER_DIMENSIONS " + ",".join(str(x) for x in affine_dims))
    print("BOUNDARY_WITNESS R-C full_noncommuting=" + ",".join(str(x) for x in noncommuting_counts))
    print("TARGET_TOKEN 2")
    print("TARGET_EFFECTS P2=E_low Q2=E_high")
    print("LUEDER_SELECTION conditional=RECORD_PARTITION_COMPLETENESS")
    print("PREMISE_STATUS EXTRA_LAW_NOT_DERIVED")
    print("DECISION RECORD-COMPLETE-SELECTION")
    print("O2_GLOBAL_STATUS UNCHANGED")
    print("SAMPLING NOT PROVIDED")
    print("CANDIDATE_CEILING T restricted-class theorems")
    print("ALL PASS 12/12")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
