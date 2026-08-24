#!/usr/bin/env python3
"""Exact audit for P-QDD-RECORD-NATURALITY-FORK-1."""

# Accepted bytes are pinned before the first formal execution.

from fractions import Fraction as Q
from itertools import permutations
import inspect

BASE = "e6845b96fc19a47c473761ad49d4f8a7812c2f58"
ISSUE = 476
F5 = tuple(range(5))
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
        z = aug[c][c]
        aug[c] = [x / z for x in aug[c]]
        for r in range(n):
            if r == c:
                continue
            z = aug[r][c]
            if z:
                aug[r] = [aug[r][j] - z * aug[c][j] for j in range(2 * n)]
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
    """Permutation p after q."""
    return tuple(p[q[x]] for x in range(len(p)))


def inverse_perm(p):
    out = [0] * len(p)
    for i, j in enumerate(p):
        out[j] = i
    return tuple(out)


def swap_perm(n, i, j):
    out = list(range(n))
    out[i], out[j] = out[j], out[i]
    return tuple(out)


def centralizer_equations(p, group):
    """Rows for XP=0, PX=0, and Xg-gX=0 on sixteen variables."""
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


def subgroup(generators, identity):
    seen = {identity}
    stack = [identity]
    while stack:
        x = stack.pop()
        for g in generators:
            for y in (compose(x, g), compose(g, x)):
                if y not in seen:
                    seen.add(y)
                    stack.append(y)
    return frozenset(seen)


def build_record_groupoid():
    """Build only from J, the regular simplex, and binary record partitions."""
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
    stabilizers = {k: tuple(pi for pi in all_perms if pi[k] == k) for k in F5}
    p = {
        k: scale(Q(1, 24), sum_mats((simplex[pi] for pi in stabilizers[k]), 4, 4))
        for k in F5
    }
    q = {k: sub(i4, p[k]) for k in F5}
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
    }


def local_s4_automorphism_audit():
    """Coxeter-image audit for Aut(S4)=Inn(S4)."""
    group = tuple(permutations(range(4)))
    identity = tuple(range(4))
    s1 = swap_perm(4, 0, 1)
    s2 = swap_perm(4, 1, 2)
    s3 = swap_perm(4, 2, 3)
    triples = []
    for a in group:
        if compose(a, a) != identity:
            continue
        for b in group:
            if compose(b, b) != identity:
                continue
            if compose(compose(a, b), a) != compose(compose(b, a), b):
                continue
            for c in group:
                if compose(c, c) != identity:
                    continue
                if compose(compose(b, c), b) != compose(compose(c, b), c):
                    continue
                if compose(a, c) != compose(c, a):
                    continue
                if len(subgroup((a, b, c), identity)) != 24:
                    continue
                triples.append((a, b, c))

    inner = []
    for h in group:
        hi = inverse_perm(h)
        inner.append(tuple(compose(compose(h, s), hi) for s in (s1, s2, s3)))
    return tuple(triples), tuple(inner)


def pointer_block(b, out, inp=0):
    if shape(b) != (8, 8):
        raise ValueError("pointer block")
    return tuple(tuple(b[2 * i + out][2 * j + inp] for j in range(4)) for i in range(4))


def main():
    source = inspect.getsource(build_record_groupoid)
    forbidden = ("E_low", "E_high", "TARGET_LOW", "TARGET_HIGH", "TARGET_TOKEN")
    assert all(token not in source for token in forbidden)

    data = build_record_groupoid()
    i4, gram, gram_inv = data["I4"], data["G"], data["GI"]
    d_j, vertices = data["DJ"], data["VERTICES"]
    all_perms, simplex = data["PERMS"], data["SIMPLEX"]
    stabilizers, p, q = data["STAB"], data["P"], data["Q"]
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
    identity5 = tuple(F5)
    assert simplex[identity5] == i4
    for pi in all_perms:
        rpi = simplex[pi]
        assert mm(mm(tr(rpi), gram), rpi) == gram
        assert all(mv(rpi, vertices[x]) == vertices[pi[x]] for x in F5)
    for pi in all_perms:
        for tau in all_perms:
            assert mm(simplex[pi], simplex[tau]) == simplex[compose(pi, tau)]
    gates += 1

    # Five complete record stabilizers and their projectors.
    assert tuple(len(stabilizers[k]) for k in F5) == (24,) * 5
    for k in F5:
        assert all(pi[k] == k for pi in stabilizers[k])
        assert mm(p[k], p[k]) == p[k]
        assert sharp(p[k], gram, gram_inv) == p[k]
        assert rank(p[k]) == 1
        assert mv(p[k], vertices[k]) == vertices[k]
        assert mm(q[k], q[k]) == q[k]
        assert sharp(q[k], gram, gram_inv) == q[k]
        assert rank(q[k]) == 3
        assert add(p[k], q[k]) == i4
    gates += 1

    # Strict naturality is the one-dimensional S4 centralizer.
    strict_dims = []
    for k in F5:
        group = tuple(simplex[pi] for pi in stabilizers[k])
        equations = centralizer_equations(p[k], group)
        strict_dims.append(16 - rank(equations))
        assert rank(cols((flatten(q[k]),))) == 1
        assert all(
            sum((row[i] * flatten(q[k])[i] for i in range(16)), Q(0)) == 0
            for row in equations
        )
    assert strict_dims == [1] * 5
    gates += 1

    # Independent finite audit of Aut(S4)=Inn(S4).
    automorphism_triples, inner_triples = local_s4_automorphism_audit()
    assert len(automorphism_triples) == 24
    assert len(set(inner_triples)) == 24
    assert set(automorphism_triples) == set(inner_triples)
    gates += 1

    # Complete weak-covariant family +/-rho(h)Q and its normalizer action.
    algebraic_counts = []
    sign_class_counts = []
    strict_counts = []
    gauge_class_counts = []
    for k in F5:
        group_labels = stabilizers[k]
        group_mats = tuple(simplex[pi] for pi in group_labels)
        members = {}
        for sign in SIGNS:
            for h in group_labels:
                tk = scale(sign, mm(simplex[h], q[k]))
                members[(sign, h)] = tk
                assert mm(p[k], tk) == zero(4, 4)
                assert mm(tk, p[k]) == zero(4, 4)
                assert mm(sharp(tk, gram, gram_inv), tk) == q[k]
                hi = inverse_perm(h)
                tsharp = sharp(tk, gram, gram_inv)
                for g in group_labels:
                    expected = mm(simplex[compose(compose(h, g), hi)], q[k])
                    assert mm(mm(tk, simplex[g]), tsharp) == expected
        assert len(set(members.values())) == 48
        algebraic_counts.append(len(set(members.values())))

        sign_keys = {
            min(flatten(tk), flatten(neg(tk)))
            for tk in members.values()
        }
        assert len(sign_keys) == 24
        sign_class_counts.append(len(sign_keys))

        strict = [
            tk for tk in members.values()
            if all(mm(tk, g) == mm(g, tk) for g in group_mats)
        ]
        assert len(set(strict)) == 2
        assert set(strict) == {q[k], neg(q[k])}
        strict_counts.append(len(set(strict)))

        gauge_keys = set()
        gauge_group = tuple(members.values())
        for tk in members.values():
            orbit = tuple(mm(a, tk) for a in gauge_group)
            gauge_keys.add(min(flatten(x) for x in orbit))
        assert len(gauge_keys) == 1
        gauge_class_counts.append(len(gauge_keys))

    assert algebraic_counts == [48] * 5
    assert sign_class_counts == [24] * 5
    assert strict_counts == [2] * 5
    assert gauge_class_counts == [1] * 5
    gates += 1

    # Nonterminal transposition witness in every record block.
    witness_failures = []
    for k in F5:
        others = [x for x in F5 if x != k]
        tau = swap_perm(5, others[0], others[1])
        tk = mm(simplex[tau], q[k])
        group_mats = tuple(simplex[pi] for pi in stabilizers[k])
        commute_count = sum(mm(tk, g) == mm(g, tk) for g in group_mats)
        witness_failures.append(24 - commute_count)
        assert commute_count == 4
        assert mm(sharp(tk, gram, gram_inv), tk) == q[k]
        assert mm(q[k], tk) == tk and mm(tk, q[k]) == tk
        assert mm(tk, tk) == q[k]
        assert tk != q[k] and tk != neg(q[k])
        assert mm(tk, tk) != tk and mm(tk, tk) != neg(tk)

        fixed = [x for x in others if x not in (others[0], others[1])]
        w_minus = tuple(vertices[others[0]][i] - vertices[others[1]][i] for i in range(4))
        w_plus = tuple(vertices[fixed[0]][i] - vertices[fixed[1]][i] for i in range(4))
        w = tuple(w_plus[i] + w_minus[i] for i in range(4))
        tw = mv(tk, w)
        ttw = mv(tk, tw)
        assert rank(cols((tw, ttw))) == 2
    assert witness_failures == [20] * 5
    gates += 1

    # Same typed pointer record and effects do not select strict naturality.
    i2 = eye(2)
    xptr = mat(((0, 1), (1, 0)))
    gt = kron(gram, i2)
    gti = kron(gram_inv, i2)
    for k in F5:
        others = [x for x in F5 if x != k]
        tau = swap_perm(5, others[0], others[1])
        t0 = q[k]
        t1 = mm(simplex[tau], q[k])
        for tk in (t0, t1):
            u = add(kron(p[k], i2), kron(tk, xptr))
            assert mm(sharp(u, gt, gti), u) == eye(8)
            assert pointer_block(u, 0) == p[k]
            assert pointer_block(u, 1) == tk
            assert mm(sharp(pointer_block(u, 0), gram, gram_inv), pointer_block(u, 0)) == p[k]
            assert mm(sharp(pointer_block(u, 1), gram, gram_inv), pointer_block(u, 1)) == q[k]
        assert t0 != t1 and t0 != neg(t1)
    gates += 1

    # Target comparison is deliberately last.
    one4 = tuple(tuple(Q(1) for _ in range(4)) for _ in range(4))
    target_low = scale(Q(1, 4), one4)
    target_high = sub(i4, target_low)
    token = 2
    assert p[token] == target_low and q[token] == target_high
    gates += 1

    assert gates == 10

    print("P-QDD-RECORD-NATURALITY-FORK-1")
    print(f"BASE_COMMIT {BASE}")
    print(f"ISSUE {ISSUE}")
    print("CLASS_INPUTS M_J,D_J,G,F5,S5,binary-record-partition,pointer-C2")
    print("CLASS_TARGET_INDEPENDENCE PASS")
    print("SIMPLEX_AUTOMORPHISMS 120")
    print("RECORD_STABILIZERS 24,24,24,24,24")
    print("STRICT_CENTRALIZER_DIMS 1,1,1,1,1")
    print("S4_AUTOMORPHISMS coxeter=24 inner=24")
    print("WEAK_NORMALIZER algebraic=48 sign_classes=24")
    print("STRICT_NATURALITY algebraic=2 sign_classes=1")
    print("TRANSPOSITION_WITNESS commutes=4 fails=20 involutive=YES terminal=NO")
    print("OBSERVABLE_QUOTIENT extended_gauge_classes=1")
    print("REGISTERED_EQUALITY sign_classes=24")
    print("TYPED_RECORD same_effects=YES same_terminal_symbol=YES strict_selection=NO")
    print("TARGET_TOKEN 2")
    print("TARGET_EFFECTS P2=E_low Q2=E_high")
    print("DECISION NATURALITY-FORK")
    print("STRICT_LAW_NATURALITY conditional=LUEDER")
    print("PUBLIC_ARCHITECTURE_DERIVATION NOT_PROVIDED")
    print("O2_GLOBAL_STATUS UNCHANGED")
    print("SAMPLING NOT PROVIDED")
    print("CANDIDATE_CEILING T restricted-L4-theorems")
    print("ALL PASS 10/10")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
