"""Exact rational matrix utilities for the pinned centralizer verifier."""

from fractions import Fraction as Q


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


def coord_proj(n, i):
    return tuple(tuple(Q(r == i and c == i) for c in range(n)) for r in range(n))


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


def pointer_block(b, out, inp=0):
    if shape(b) != (8, 8):
        raise ValueError("pointer block")
    return tuple(tuple(b[2 * i + out][2 * j + inp] for j in range(4)) for i in range(4))
