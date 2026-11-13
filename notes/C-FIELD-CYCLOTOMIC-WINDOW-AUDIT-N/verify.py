#!/usr/bin/env python3
"""Exact successor audit; universal statements require PROOF.md.

Adapted from the public predecessor at ff603881d1c297a6bbb63f88df455a4b4bf3ea74.
The old primary remains failed and unchanged. This is new code under a new pin;
PREREG records both corrections and the already-exposed targets.
"""
from fractions import Fraction as Q
from hashlib import sha256
from itertools import product
from pathlib import Path


def eye(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def tr(a):
    return [list(row) for row in zip(*a)]


def mm(a, b):
    return [[sum(x * y for x, y in zip(row, col)) for col in tr(b)] for row in a]


def mv(a, x):
    return [sum(u * v for u, v in zip(row, x)) for row in a]


def add(a, b, scale=1):
    return [[x + scale * y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def times(a, k):
    return [[k * x for x in row] for row in a]


def power(a, n):
    out = eye(len(a))
    for _ in range(n):
        out = mm(out, a)
    return out


def det(a):
    b = [[Q(v) for v in row] for row in a]
    value = Q(1)
    for k in range(len(b)):
        pivot = next((i for i in range(k, len(b)) if b[i][k]), None)
        if pivot is None:
            return Q(0)
        if pivot != k:
            b[k], b[pivot] = b[pivot], b[k]
            value = -value
        p = b[k][k]
        value *= p
        for i in range(k + 1, len(b)):
            q = b[i][k] / p
            b[i] = [x - q * y for x, y in zip(b[i], b[k])]
    return value


def inverse(a):
    n = len(a)
    b = [[Q(v) for v in a[i] + eye(n)[i]] for i in range(n)]
    for k in range(n):
        i = next(i for i in range(k, n) if b[i][k])
        b[k], b[i] = b[i], b[k]
        q = b[k][k]
        b[k] = [x / q for x in b[k]]
        for i in range(n):
            if i != k:
                q = b[i][k]
                b[i] = [x - q * y for x, y in zip(b[i], b[k])]
    return [row[n:] for row in b]


def integral(a):
    assert all(Q(x).denominator == 1 for row in a for x in row)
    return [[int(x) for x in row] for row in a]


def charpoly(a):
    # Newton identities, descending coefficients; exact divisions in Q.
    c = [Q(1)]
    traces = [None] + [sum(power(a, j)[i][i] for i in range(len(a)))
                       for j in range(1, len(a) + 1)]
    for k in range(1, len(a) + 1):
        c.append(-sum(c[k - j] * traces[j] for j in range(1, k + 1)) / k)
    return integral([c])[0]


def smith(a):
    """Euclidean row/column operations, retaining both unimodular witnesses."""
    a = [row[:] for row in a]
    n = len(a)
    u, v = eye(n), eye(n)

    def row_swap(i, j):
        a[i], a[j] = a[j], a[i]
        u[i], u[j] = u[j], u[i]

    def col_swap(i, j):
        for m in (a, v):
            for row in m:
                row[i], row[j] = row[j], row[i]

    def row_add(i, j, q):
        a[i] = [x + q * y for x, y in zip(a[i], a[j])]
        u[i] = [x + q * y for x, y in zip(u[i], u[j])]

    def col_add(i, j, q):
        for m in (a, v):
            for row in m:
                row[i] += q * row[j]

    for k in range(n):
        options = [(abs(a[i][j]), i, j) for i in range(k, n)
                   for j in range(k, n) if a[i][j]]
        if not options:
            break
        _, i, j = min(options)
        row_swap(k, i)
        col_swap(k, j)
        while True:
            i = next((i for i in range(k + 1, n) if a[i][k]), None)
            if i is not None:
                row_add(i, k, -(a[i][k] // a[k][k]))
                if a[i][k]:
                    row_swap(i, k)
                continue
            j = next((j for j in range(k + 1, n) if a[k][j]), None)
            if j is not None:
                col_add(j, k, -(a[k][j] // a[k][k]))
                if a[k][j]:
                    col_swap(j, k)
                continue
            bad = next(((i, j) for i in range(k + 1, n)
                        for j in range(k + 1, n) if a[i][j] % a[k][k]), None)
            if bad is None:
                break
            row_add(k, bad[0], 1)
        if a[k][k] < 0:
            a[k] = [-x for x in a[k]]
            u[k] = [-x for x in u[k]]
    return u, a, v


def rref5(a):
    a = [[x % 5 for x in row] for row in a]
    pivots = []
    row = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(row, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        a[row] = [(x * pow(a[row][col], -1, 5)) % 5 for x in a[row]]
        for i in range(len(a)):
            if i != row:
                q = a[i][col]
                a[i] = [(x - q * y) % 5 for x, y in zip(a[i], a[row])]
        pivots.append(col)
        row += 1
    return a[:row], pivots


def field(c):
    e, f = len(c), len(c[0])
    ct, g = tr(c), mm(tr(c), c)
    t = [eye(e)[i] + c[i] for i in range(e)]
    t += [[-x for x in ct[i]] + add(eye(f), g, -1)[i] for i in range(f)]
    b = [times(eye(e), 2)[i] + c[i] for i in range(e)]
    b += [ct[i] + times(eye(f), 2)[i] for i in range(f)]
    r = [eye(e)[i] + c[i] for i in range(e)]
    r += [[0] * e + times(eye(f), -1)[i] for i in range(f)]
    ti = [add(eye(e), mm(c, ct), -1)[i] + [-v for v in c[i]] for i in range(e)]
    ti += [ct[i] + eye(f)[i] for i in range(f)]
    return t, ti, b, r


def energy(b, x):
    return Q(sum(u * v for u, v in zip(x, mv(b, x))), 2)


def main():
    root = Path(__file__).resolve().parents[2]
    sources = {
        'canon/CANON.md': 'b4ebf2ffc7393b703d65ce62cf3e0ee382e7309a563d99ec866ee3fa82f9ba7f',
        'canon/REGISTRY.tsv': 'a2abce1a4538785ac6a7c7874c2366a3531d460027188510394930c6d222559a',
        'canon/EVIDENCE.tsv': '1258ea3dd14a5e2b512b69b08ac647626d4fac169a1ba0b6cd770832bb735600',
        'canon/DEPENDENCIES.tsv': 'c1b0cee2b9e320ed05ba4004da3a2265cbd2bbafe45dd18f59fb29790d477214',
        'canon/GATES.tsv': '85f7db365ff38988dbf2a994f4d8d0ba380ac00d368bcc50e4313daee9aff744',
        'notes/INTEGER-AUTOMATON-COMPOSITION-PROGRAM.md':
            '354c4b5292c89ab521654a642f056c39f4c99e688b5e34891369c23980d9dfd7',
    }
    for name, expected in sources.items():
        assert sha256((root / name).read_bytes()).hexdigest() == expected, name
    c = [[1, -1], [-1, 0], [0, 1], [0, 1]]
    d = [[1, 1, 1, 0], [-1, -1, 0, -1], [0, 0, -1, 1]]
    g = [[2, -1], [-1, 3]]
    assert mm(tr(c), c) == g
    assert mm(d, c) == [[0, 0]] * 3
    t, ti, braw, r = field(c)
    assert mm(t, ti) == mm(ti, t) == eye(6)
    assert mm(mm(tr(t), braw), t) == braw
    assert mm(r, r) == eye(6) and mm(mm(r, t), r) == ti
    embedding = [row + [0, 0] for row in c] + [[0, 0, 1, 0], [0, 0, 0, 1]]
    extraction = [[0, -1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0],
                  [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1]]
    assert mm(extraction, embedding) == eye(4)
    a = mm(mm(extraction, t), embedding)
    b = mm(mm(tr(embedding), braw), embedding)
    assert mm(t, embedding) == mm(embedding, a)
    assert mm(mm(tr(a), b), a) == b
    assert all(det([row[:k] for row in b[:k]]) > 0 for k in range(1, 5))
    p5 = eye(6)
    pa = eye(4)
    for j in range(1, 5):
        p5 = add(p5, power(t, j))
        pa = add(pa, power(a, j))
    assert pa == [[0] * 4 for _ in range(4)]
    assert power(a, 5) == eye(4) and a != eye(4)
    s = [[1, 0], [1, 0], [0, 1], [1, -1], [0, 0], [0, 0]]
    assert mm(t, s) == s and mm(p5, s) == times(s, 5)
    assert mm(p5, embedding) == [[0] * 4 for _ in range(6)]
    w = [embedding[i] + s[i] for i in range(6)]
    assert abs(det(w)) == 5
    wi = inverse(w)
    numerator = integral(times(wi, 5))
    d6 = [row + [0, 0] for row in d]
    assert mm(d6, embedding) == [[0] * 4 for _ in range(3)]
    assert mm(d6, t) == mm(d6, r) == d6
    assert mm(mm(tr(r), braw), r) == braw
    assert power(t, 5) == eye(6) and p5 != [[0] * 6 for _ in range(6)]
    doubled = [row[:] for row in embedding]
    for row in doubled:
        row[0] *= 2
    assert mm(p5, doubled) == [[0] * 4 for _ in range(6)]
    assert det(mm(extraction, doubled)) == 2  # Same rational span, index two.
    assert mv(extraction, mv(embedding, [1, 0, 0, 0]))[0] % 2 == 1
    assert a == [[1, 0, 1, 0], [0, 1, 0, 1],
                 [-2, 1, -1, 1], [1, -3, 1, -2]]
    assert b == [[4, -2, 2, -1], [-2, 6, -1, 3],
                 [2, -1, 2, 0], [-1, 3, 0, 2]]
    # Phi5 vanishes on the rank-four active space and equals 5I on the
    # complementary rank-two static space; W invertible certifies both.
    seed = [0, 0, 1, 0]
    module = tr([mv(power(a, j), seed) for j in range(4)])
    assert abs(det(module)) == 1
    module_inv = integral(inverse(module))
    companion = [[0, 0, 0, -1], [1, 0, 0, -1],
                 [0, 1, 0, -1], [0, 0, 1, -1]]
    assert mm(a, module) == mm(module, companion)
    assert det(module) == -1
    assert module == [[0, 1, 0, 0], [0, 0, 1, -1],
                      [1, -1, 0, -1], [0, 1, -2, 1]]
    assert mm(module, module_inv) == mm(module_inv, module) == eye(4)
    jmat = add(eye(4), power(a, 2))
    assert charpoly(jmat) == [1, -3, 4, -2, 1]
    assert sum(jmat[i][i] for i in range(4)) == 3 and det(jmat) == 1
    ell = mm(add(eye(4), a, -1), add(eye(4), power(a, 2), -1))
    assert mm(ell, a) == mm(a, ell)
    assert mm(ell, ell) == times(power(a, 3), 5)
    assert mm(mm(tr(ell), b), ell) == times(b, 5)
    adjoint = mm(mm(inverse(b), tr(ell)), b)
    assert mm(adjoint, ell) == times(eye(4), 5)
    assert det(ell) == 25
    assert ell == [[1, -3, -1, -2], [-3, 4, -2, 1],
                   [0, 5, 1, 2], [5, -5, 2, -1]]
    kinv = mm(power(a, 2), ell)
    assert mm(kinv, ell) == mm(ell, kinv) == times(eye(4), 5)
    assert adjoint == kinv == [[1, 2, 1, 2], [2, -1, 2, -1],
                              [0, -5, 1, -3], [-5, 5, -3, 4]]

    def preimage(y):
        z = mv(kinv, y)
        if any(x % 5 for x in z):
            return None
        return [x // 5 for x in z]

    u, diag, v = smith(ell)
    assert abs(det(u)) == abs(det(v)) == 1
    assert mm(mm(u, ell), v) == diag == [[1, 0, 0, 0], [0, 1, 0, 0],
                                        [0, 0, 5, 0], [0, 0, 0, 5]]
    rr, piv = rref5(kinv)
    assert len(piv) == 2
    hermite = eye(4)
    for row, p in zip(rr, piv):
        hermite[p][p] = 5
        for col in range(4):
            if col not in piv:
                hermite[p][col] = (-row[col]) % 5
    to_h = integral(mm(inverse(hermite), ell))
    from_h = integral(mm(inverse(ell), hermite))
    assert abs(det(to_h)) == abs(det(from_h)) == 1
    assert mm(hermite, to_h) == ell and mm(ell, from_h) == hermite
    assert all(hermite[i][j] == 0 for i in range(4) for j in range(i))
    assert hermite == [[5, 3, 0, 0], [0, 1, 0, 0],
                       [0, 0, 5, 3], [0, 0, 0, 1]]
    residues = list(product(range(5), repeat=4))
    image = {tuple(x % 5 for x in mv(ell, y)) for y in residues}
    admitted = 0
    for y in residues:
        z = preimage(y)
        member = z is not None
        explicit = (y[0] + 2 * y[1]) % 5 == 0 and (y[2] + 2 * y[3]) % 5 == 0
        assert member == explicit == (tuple(y) in image)
        if member:
            admitted += 1
            assert mv(ell, z) == list(y)
    assert admitted == len(image) == 25
    outside = [0, 0, 1, -2]
    assert energy(b, outside) == 5 and preimage(outside) is None
    assert mv(kinv, outside) == [-3, 4, 7, -11]
    false_accept = [0, 0, 1, 1]
    assert (false_accept[0] + 2 * false_accept[1]) % 5 == 0
    assert (3 * false_accept[0] - false_accept[1] + false_accept[2] - false_accept[3]) % 5 == 0
    assert mv(kinv, false_accept) == [3, 1, -2, 1]
    assert preimage(false_accept) is None
    false_nonimage = [0, 0, 1, 2]
    assert preimage(false_nonimage) == [1, 0, -1, 1]
    assert mv(ell, [1, 0, -1, 1]) == false_nonimage
    assert energy(b, false_nonimage) == 5
    assert energy(b, [1, 0, -1, 1]) == 1
    assert energy(b, [1, 0, 0, 0]) == 2
    assert energy(b, mv(jmat, [1, 0, 0, 0])) == 3
    assert mm(jmat, times(add(a, power(a, 2)), -1)) == eye(4)
    assert energy(b, seed) == 1 and energy(b, mv(ell, seed)) == 5
    assert mm(mm(tr(jmat), b), jmat) != b
    assert mm(tr(ell), ell) != times(eye(4), 5)

    full_ell = mm(add(eye(6), t, -1), add(eye(6), power(t, 2), -1))
    assert mm(full_ell, s) == [[0, 0]] * 6
    pstatic = times(p5, Q(1, 5))
    extension = add(full_ell, pstatic)
    assert mm(d6, extension) == d6
    nonintegral = next(i for i, col in enumerate(tr(extension))
                       if any(Q(x).denominator != 1 for x in col))
    assert mm(extension, embedding) == mm(embedding, ell)
    assert mm(extension, s) == s
    assert mm(d6, full_ell) == [[0] * 6 for _ in range(3)]
    assert mv(extension, [1, 0, 0, 0, 0, 0]) == [Q(17, 5), Q(-3, 5),
                                               Q(-9, 5), Q(-9, 5), -1, 3]
    assert mm(pstatic, pstatic) == pstatic
    assert mm(mm(tr(embedding), braw), s) == [[0, 0]] * 4
    split_energy = mm(mm(tr(w), braw), w)
    out_energy = mm(mm(tr(mm(extension, w)), braw), mm(extension, w))
    assert out_energy == [[split_energy[i][j] * (5 if i < 4 and j < 4 else 1)
                           for j in range(6)] for i in range(6)]
    # The full integer lattice glues active/static parts with one residue.
    gluing_count = 0
    for electric in product(range(5), repeat=4):
        raw = list(electric) + [0, 0]
        coords = mv(numerator, raw)
        admitted_gluing = all(x % 5 == 0 for x in coords)
        charge = mv(d, electric)
        assert admitted_gluing == all(Q(x).denominator == 1 for x in mv(extension, raw))
        assert admitted_gluing == ((2 * electric[0] - 3 * electric[1] + electric[2] + electric[3]) % 5 == 0)
        projected = mv(embedding, mv(extraction, raw))
        assert (projected == raw) == (charge == [0, 0, 0])
        representative = [charge[0], 0, 0, charge[2]]
        assert mv(d, representative) == charge
        assert admitted_gluing == ((2 * charge[0] + charge[2]) % 5 == 0)
        gluing_count += admitted_gluing
    assert gluing_count == 125

    controls = [[[0, 0, 0], [0, 0, 0]], [[1], [0]],
                [[1, 0], [0, 0]], [[2, 0], [0, 0]], [[3, 0], [0, 0]]]
    for cc in controls:
        tc, ic, bc, rc = field(cc)
        n = len(tc)
        assert mm(tc, ic) == mm(ic, tc) == eye(n)
        assert mm(mm(tr(tc), bc), tc) == bc
        assert mm(rc, rc) == eye(n) and mm(mm(rc, tc), rc) == ic
        assert mm(mm(tr(rc), bc), rc) == bc
    assert field(controls[0])[0] == eye(5)
    assert power(field(controls[1])[0], 6) == eye(3)
    assert power(field(controls[2])[0], 6) == eye(4)
    unstable = field(controls[4])[0]
    assert mv(unstable, [0, 1, 0, 0]) == [0, 1, 0, 0]
    assert unstable[0][0] + unstable[2][2] == -7
    critical = field(controls[3])[0]
    ac = [[critical[i][j] for j in (0, 2)] for i in (0, 2)]
    jordan = add(ac, eye(2))
    assert jordan != [[0, 0], [0, 0]] and mm(jordan, jordan) == [[0, 0], [0, 0]]
    cc = [[1, 1], [1, 0], [1, 0], [0, 1], [0, 1]]
    tc, _, bc, _ = field(cc)
    cv = mv(cc, [1, 1])
    dc = [[1, 0, -1, 0, -1], [-1, 1, 0, 1, 0],
          [0, -1, 1, 0, 0], [0, 0, 0, -1, 1]]
    assert mm(dc, cc) == [[0, 0]] * 4
    assert mm(tr(cc), cc) == [[3, 1], [1, 3]]
    assert mv(mm(tr(cc), cc), [1, 1]) == [4, 4]
    state = [0] * 5 + [1, 1]
    for n in range(13):
        predicted = [(-1)**(n+1)*n*x for x in cv] + [(-1)**n*(2*n+1)]*2
        assert state == predicted and energy(bc, state) == 2
        assert mv(dc, state[:5]) == [0, 0, 0, 0]
        state = mv(tc, state)
    print('PRIMARY PASS: exact field, lattice, L5 and 625 image residues; 25 admitted, 600 rejected')


if __name__ == '__main__':
    main()
