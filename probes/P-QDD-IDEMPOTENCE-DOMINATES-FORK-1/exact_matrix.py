"""Exact Fraction matrix utilities for the pinned QDD verifier."""

from fractions import Fraction as F

def mat(rows):
    out = tuple(tuple(x if isinstance(x, F) else F(x) for x in row) for row in rows)
    if not out or not out[0] or any(len(row) != len(out[0]) for row in out):
        raise ValueError("bad matrix")
    return out


def shape(a):
    return len(a), len(a[0])


def zero(r, c):
    return tuple(tuple(F(0) for _ in range(c)) for _ in range(r))


def eye(n):
    return tuple(tuple(F(i == j) for j in range(n)) for i in range(n))


def tr(a):
    r, c = shape(a)
    return tuple(tuple(a[i][j] for i in range(r)) for j in range(c))


def add(a, b):
    if shape(a) != shape(b):
        raise ValueError("shape")
    r, c = shape(a)
    return tuple(tuple(a[i][j] + b[i][j] for j in range(c)) for i in range(r))


def scale(x, a):
    x = x if isinstance(x, F) else F(x)
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
        tuple(sum((a[i][k] * bt[j][k] for k in range(ac)), F(0)) for j in range(bc))
        for i in range(ar)
    )


def mv(a, v):
    r, c = shape(a)
    if c != len(v):
        raise ValueError("vector shape")
    return tuple(sum((a[i][j] * v[j] for j in range(c)), F(0)) for i in range(r))


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
        pivot = next((r for r in range(c, n) if aug[r][c]), None)
        if pivot is None:
            raise ValueError("singular")
        aug[c], aug[pivot] = aug[pivot], aug[c]
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
    work = [list(row) for row in a]
    pivot_row = 0
    for j in range(c):
        pivot = next((i for i in range(pivot_row, r) if work[i][j]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        q = work[pivot_row][j]
        work[pivot_row] = [x / q for x in work[pivot_row]]
        for i in range(r):
            if i != pivot_row and work[i][j]:
                q = work[i][j]
                work[i] = [work[i][k] - q * work[pivot_row][k] for k in range(c)]
        pivot_row += 1
        if pivot_row == r:
            break
    return pivot_row


def det(a):
    n, m = shape(a)
    if n != m:
        raise ValueError("determinant")
    work = [list(row) for row in a]
    out = F(1)
    sign = 1
    for c in range(n):
        pivot = next((r for r in range(c, n) if work[r][c]), None)
        if pivot is None:
            return F(0)
        if pivot != c:
            work[c], work[pivot] = work[pivot], work[c]
            sign = -sign
        q = work[c][c]
        out *= q
        for r in range(c + 1, n):
            if work[r][c]:
                factor = work[r][c] / q
                for j in range(c, n):
                    work[r][j] -= factor * work[c][j]
    return sign * out


def cols(vectors):
    if not vectors or any(len(v) != len(vectors[0]) for v in vectors):
        raise ValueError("columns")
    return tuple(tuple(vectors[j][i] for j in range(len(vectors))) for i in range(len(vectors[0])))


def sum_mats(items, r, c):
    out = zero(r, c)
    for item in items:
        out = add(out, item)
    return out


def basis(n, i):
    return tuple(F(j == i) for j in range(n))


def flatten(a):
    return tuple(x for row in a for x in row)


def sharp(a, gram, gram_inv):
    return mm(mm(gram_inv, tr(a)), gram)


def dot(v, gram, w):
    gw = mv(gram, w)
    return sum((v[i] * gw[i] for i in range(len(v))), F(0))


