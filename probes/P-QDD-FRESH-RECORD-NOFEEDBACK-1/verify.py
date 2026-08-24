#!/usr/bin/env python3
"""Exact audit for P-QDD-FRESH-RECORD-NOFEEDBACK-1."""

from fractions import Fraction as Q
import inspect

BASE = "4ef54f0c34f80897af0121a2d93b710e70a8377c"
ISSUE = 470
F5 = (0, 1, 2, 3, 4)
UNITS = (1, 2, 3, 4)


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
    ident = eye(n)
    aug = [list(a[i]) + list(ident[i]) for i in range(n)]
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


def basis(n, i):
    return tuple(Q(j == i) for j in range(n))


def kron(a, b):
    ar, ac = shape(a)
    br, bc = shape(b)
    return tuple(
        tuple(a[i // br][j // bc] * b[i % br][j % bc] for j in range(ac * bc))
        for i in range(ar * br)
    )


def kronv(*vectors):
    out = (Q(1),)
    for v in vectors:
        out = tuple(x * y for x in out for y in v)
    return out


def perm(image):
    n = len(image)
    if sorted(image) != list(range(n)):
        raise ValueError("permutation")
    rows = [[Q(0) for _ in range(n)] for _ in range(n)]
    for c, r in enumerate(image):
        rows[r][c] = Q(1)
    return tuple(tuple(row) for row in rows)


def sharp(a, g, gi):
    return mm(mm(gi, tr(a)), g)


def dot(v, g, w):
    gw = mv(g, w)
    return sum((v[i] * gw[i] for i in range(len(v))), Q(0))


def first_nonzero_column(a):
    r, c = shape(a)
    for j in range(c):
        v = tuple(a[i][j] for i in range(r))
        if any(v):
            return v
    raise AssertionError("zero matrix")


def image(c, b, x):
    return (b + c * x) % 5


def hoff(a, k):
    return k * (1 - a) % 5


def build_j_witness():
    """Build only from the public J step and target-independent affine data."""
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
        return mm(cols(tuple(vertices[image(c, b, x)] for x in range(4))), vertex_basis_inv)

    affine = {(c, b): rho(c, b) for c in UNITS for b in F5}
    stabilizer = {(a, k): affine[(a, hoff(a, k))] for a in UNITS for k in F5}
    p = {
        k: scale(Q(1, 4), sum_mats((stabilizer[(a, k)] for a in UNITS), 4, 4))
        for k in F5
    }
    q = {k: sub(i4, p[k]) for k in F5}
    r_sign, c_plane, j_plane = {}, {}, {}
    for k in F5:
        gk = stabilizer[(2, k)]
        alt = sub(add(sub(i4, gk), mpow(gk, 2)), mpow(gk, 3))
        r_sign[k] = scale(Q(1, 4), alt)
        c_plane[k] = sub(q[k], r_sign[k])
        j_plane[k] = mm(gk, c_plane[k])
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
        "R": r_sign,
        "C": c_plane,
        "J": j_plane,
    }


def sum_mats(xs, r, c):
    out = zero(r, c)
    for x in xs:
        out = add(out, x)
    return out


def moving(data, k, e, r, s):
    return add(
        scale(e, data["R"][k]),
        add(scale(r, data["C"][k]), scale(s, data["J"][k])),
    )


def pointer_and_writer(p, t):
    i2 = eye(2)
    x = mat(((0, 1), (1, 0)))
    u = add(kron(p, i2), kron(t, x))
    s_low = perm((1, 0, 2))
    s_high = perm((2, 1, 0))
    e0 = mat(((1, 0), (0, 0)))
    e1 = mat(((0, 0), (0, 1)))
    writer = add(kron(e0, s_low), kron(e1, s_high))
    full = mm(kron(eye(4), writer), kron(u, eye(3)))
    return u, writer, full


def sparse_initial(v, cells):
    key = [0]
    for _ in range(cells):
        key.extend((0, 0))
    out = {}
    for i, x in enumerate(v):
        if x:
            key[0] = i
            out[tuple(key)] = x
    return out


def apply_fresh_step(state, cell, p, t):
    """Act on system and one fresh pair; old cells are copied unchanged."""
    out_u = {}
    a_pos = 1 + 2 * cell
    m_pos = a_pos + 1
    for key, amp in state.items():
        if key[a_pos] != 0 or key[m_pos] != 0:
            raise AssertionError("cell not fresh")
        s_in = key[0]
        for s_out in range(4):
            lo = p[s_out][s_in]
            hi = t[s_out][s_in]
            if lo:
                k = list(key)
                k[0] = s_out
                k[a_pos] = 0
                out_u[tuple(k)] = out_u.get(tuple(k), Q(0)) + amp * lo
            if hi:
                k = list(key)
                k[0] = s_out
                k[a_pos] = 1
                out_u[tuple(k)] = out_u.get(tuple(k), Q(0)) + amp * hi
    out = {}
    for key, amp in out_u.items():
        k = list(key)
        k[m_pos] = 1 if key[a_pos] == 0 else 2
        out[tuple(k)] = out.get(tuple(k), Q(0)) + amp
    return {k: v for k, v in out.items() if v}


def expected_branch(v, cells, pointer_value, record_value):
    key_tail = []
    for _ in range(cells):
        key_tail.extend((pointer_value, record_value))
    out = {}
    for i, x in enumerate(v):
        if x:
            out[(i, *key_tail)] = x
    return out


def drop_old_record(state, old_cell):
    pos = 2 + 2 * old_cell
    out = {}
    for key, amp in state.items():
        reduced = key[:pos] + key[pos + 1:]
        out[reduced] = out.get(reduced, Q(0)) + amp
    return {k: v for k, v in out.items() if v}


def main():
    source = inspect.getsource(build_j_witness)
    forbidden = ("E_low", "E_high", "target_low", "target_high", "TARGET_TOKEN")
    assert all(word not in source for word in forbidden)
    data = build_j_witness()
    i4, g, gi, d = data["I4"], data["G"], data["GI"], data["DJ"]
    vertices, affine, h = data["VERTICES"], data["AFFINE"], data["H"]
    p, q, rr, cc, jj = data["P"], data["Q"], data["R"], data["C"], data["J"]
    gates = 1

    assert mpow(d, 5) == i4 and mm(mm(tr(d), g), d) == g
    assert tuple(sum((vertices[k][i] for k in F5), Q(0)) for i in range(4)) == (Q(0),) * 4
    for x in F5:
        for y in F5:
            assert dot(vertices[x], g, vertices[y]) == (Q(4, 5) if x == y else Q(-1, 5))
    assert vertices[2] == (Q(-1),) * 4
    gates += 1

    assert len(set(affine.values())) == 20 and affine[(1, 1)] == d
    for (a, b), rab in affine.items():
        assert mm(mm(tr(rab), g), rab) == g
        assert all(mv(rab, vertices[x]) == vertices[image(a, b, x)] for x in F5)
        for aa in UNITS:
            for bb in F5:
                product = (a * aa % 5, (b + a * bb) % 5)
                assert mm(rab, affine[(aa, bb)]) == affine[product]
    gates += 1

    for k in F5:
        assert mm(p[k], p[k]) == p[k] and sharp(p[k], g, gi) == p[k] and rank(p[k]) == 1
        assert mm(q[k], q[k]) == q[k] and sharp(q[k], g, gi) == q[k] and rank(q[k]) == 3
        assert add(p[k], q[k]) == i4 and mv(p[k], vertices[k]) == vertices[k]
        assert rank(rr[k]) == 1 and rank(cc[k]) == 2
        assert mm(rr[k], rr[k]) == rr[k] and mm(cc[k], cc[k]) == cc[k]
        assert sharp(rr[k], g, gi) == rr[k] and sharp(cc[k], g, gi) == cc[k]
        assert add(rr[k], cc[k]) == q[k]
        assert mm(rr[k], cc[k]) == zero(4, 4) and mm(cc[k], rr[k]) == zero(4, 4)
        assert mm(jj[k], jj[k]) == neg(cc[k]) and sharp(jj[k], g, gi) == neg(jj[k])
        assert mm(cc[k], jj[k]) == jj[k] and mm(jj[k], cc[k]) == jj[k]
        assert mm(rr[k], jj[k]) == zero(4, 4) and mm(jj[k], rr[k]) == zero(4, 4)
    gates += 1

    token = 0
    t_star = sub(rr[token], cc[token])
    assert sharp(t_star, g, gi) == t_star
    assert mm(sharp(t_star, g, gi), t_star) == q[token]
    assert mm(t_star, t_star) == q[token]
    assert t_star != q[token] and t_star != neg(q[token])
    assert mm(t_star, p[token]) == zero(4, 4) and mm(p[token], t_star) == zero(4, 4)
    assert mm(q[token], t_star) == t_star and mm(t_star, q[token]) == t_star
    gates += 1

    s_low = perm((1, 0, 2))
    s_high = perm((2, 1, 0))
    for s in (s_low, s_high):
        assert mm(tr(s), s) == eye(3) and mm(s, s) == eye(3)
    _, writer, _ = pointer_and_writer(p[token], t_star)
    assert mm(tr(writer), writer) == eye(6) and mm(writer, writer) == eye(6)
    assert mv(writer, kronv(basis(2, 0), basis(3, 0))) == kronv(basis(2, 0), basis(3, 1))
    assert mv(writer, kronv(basis(2, 1), basis(3, 0))) == kronv(basis(2, 1), basis(3, 2))
    gates += 1

    samples = (
        q[token],
        neg(q[token]),
        t_star,
        moving(data, token, Q(1), Q(3, 5), Q(4, 5)),
    )
    for t in samples:
        u, w, f = pointer_and_writer(p[token], t)
        gp = kron(g, eye(2))
        gpi = kron(gi, eye(2))
        gf = kron(kron(g, eye(2)), eye(3))
        gfi = kron(kron(gi, eye(2)), eye(3))
        assert mm(sharp(u, gp, gpi), u) == eye(8)
        assert mm(sharp(f, gf, gfi), f) == eye(24)
        for v in (basis(4, i) for i in range(4)):
            lhs = mv(f, kronv(v, basis(2, 0), basis(3, 0)))
            rhs = tuple(
                a + b for a, b in zip(
                    kronv(mv(p[token], v), basis(2, 0), basis(3, 1)),
                    kronv(mv(t, v), basis(2, 1), basis(3, 2)),
                )
            )
            assert lhs == rhs
    gates += 1

    r_vec = first_nonzero_column(rr[token])
    c_vec = first_nonzero_column(cc[token])
    mixed = tuple(r_vec[i] + c_vec[i] for i in range(4))
    first = mv(t_star, mixed)
    second = mv(mpow(t_star, 2), mixed)
    assert rank(cols((first, second))) == 2
    assert mpow(t_star, 2) != t_star and mpow(t_star, 2) != neg(t_star)
    gates += 1

    high_state = sparse_initial(mixed, 3)
    old_prefixes = []
    for cell in range(3):
        high_state = apply_fresh_step(high_state, cell, p[token], t_star)
        old_prefixes.append(tuple(next(iter(high_state))[2 + 2 * j] for j in range(cell + 1)))
    assert old_prefixes == [(2,), (2, 2), (2, 2, 2)]
    assert high_state == expected_branch(mv(mpow(t_star, 3), mixed), 3, 1, 2)

    low_seed = vertices[token]
    low_state = sparse_initial(low_seed, 3)
    for cell in range(3):
        low_state = apply_fresh_step(low_state, cell, p[token], t_star)
    assert low_state == expected_branch(low_seed, 3, 0, 1)
    gates += 1

    # Old-record no-feedback control: changing an old record cannot change the
    # system/fresh-cell output, and the old record itself is preserved.
    state_l = sparse_initial(mixed, 2)
    state_h = sparse_initial(mixed, 2)
    key_l = next(iter(state_l))
    key_h = next(iter(state_h))
    amp_l = state_l.pop(key_l)
    amp_h = state_h.pop(key_h)
    kl, kh = list(key_l), list(key_h)
    kl[2], kh[2] = 1, 2
    state_l[tuple(kl)], state_h[tuple(kh)] = amp_l, amp_h
    out_l = apply_fresh_step(state_l, 1, p[token], t_star)
    out_h = apply_fresh_step(state_h, 1, p[token], t_star)
    assert all(key[2] == 1 for key in out_l) and all(key[2] == 2 for key in out_h)
    assert drop_old_record(out_l, 0) == drop_old_record(out_h, 0)
    gates += 1

    # Exact outcome repeatability holds although the conditional ray moves.
    assert mm(q[token], t_star) == t_star and mm(p[token], t_star) == zero(4, 4)
    assert rank(cols((first, second))) == 2
    assert tuple(next(iter(high_state))[2 + 2 * j] for j in range(3)) == (2, 2, 2)
    gates += 1

    # Projective idempotence is the added equation T^2=+/-T. The witness fails.
    assert mm(t_star, t_star) == q[token]
    assert q[token] != t_star and q[token] != neg(t_star)
    for t in (q[token], neg(q[token])):
        square = mm(t, t)
        assert square == t or square == neg(t)
    gates += 1

    # Record sufficiency is strictly stronger than record persistence: the
    # same terminal HIGH symbol occurs after one and two runs, but rays split.
    assert rank(cols((first, second))) == 2
    stable = mv(q[token], mixed)
    assert rank(cols((stable, mv(q[token], stable)))) == 1
    gates += 1

    # Target comparison is deliberately last.
    one4 = tuple(tuple(Q(1) for _ in range(4)) for _ in range(4))
    target_low = scale(Q(1, 4), one4)
    target_high = sub(i4, target_low)
    target_token = 2
    assert p[target_token] == target_low and q[target_token] == target_high
    target_star = sub(rr[target_token], cc[target_token])
    assert mm(sharp(target_star, g, gi), target_star) == target_high
    assert mm(target_star, target_star) == target_high
    assert target_star != target_high and target_star != neg(target_high)
    gates += 1

    assert gates == 14
    print("P-QDD-FRESH-RECORD-NOFEEDBACK-1")
    print(f"BASE_COMMIT {BASE}")
    print(f"ISSUE {ISSUE}")
    print("CLASS_INPUTS J-step,F5,AGL1,fresh-pointer,blank-LOW-HIGH-record")
    print("TARGET_INDEPENDENCE PASS")
    print("RECORD_WRITER alphabet=3 reversible=YES")
    print("FRESH_PROTOCOL cells=3 append_only=YES prefix_preserving=YES")
    print("NO_FEEDBACK old_record_controls=NO")
    print("GENERAL_EXTENSION admissible_T=ALL proof=INLINE")
    print("OUTCOME_REPEATABILITY LOW=YES HIGH=YES")
    print("J_WITNESS T=R-C selfadjoint=YES involutive=YES")
    print("PROJECTIVE_IDEMPOTENCE witness=NONIDEMPOTENT")
    print("RECORD_HISTORY witness=HIGH,HIGH,HIGH")
    print("POSTSTATE_RAYS first_second=SPLIT")
    print("RECORD_SUFFICIENCY status=EXTRA_PREMISE")
    print("TARGET_TOKEN 2")
    print("TARGET_EFFECTS realized=YES")
    print("DECISION NONIMPLICATION")
    print("O2_GLOBAL_STATUS UNCHANGED")
    print("SAMPLING NOT PROVIDED")
    print("CANDIDATE_CEILING T restricted-L4-theorems")
    print("ALL PASS 14/14")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
