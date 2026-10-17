#!/usr/bin/env python3
"""Exact audit of five frozen field-cell types; Python standard library only.

No exploratory execution preceded the public pin. Universal statements are
proved in PROOF.md; the matrix checks audit those coefficient identities.
"""
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, permutations, product
from pathlib import Path
import json
import sys

SOURCE_MANIFEST_SHA256 = "cbe7ca144d9e8822d92d375c5684a5826a8f9fedd25c91e817533c3b1d13e7cf"


class ScientificFailure(Exception):
    pass


def require(condition, label):
    if not condition:
        raise ScientificFailure(label)


def eye(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def zero(m, n):
    return [[0] * n for _ in range(m)]


def tr(a):
    return [list(row) for row in zip(*a)]


def add(a, b):
    return [[x + y for x, y in zip(r, s)] for r, s in zip(a, b)]


def scale(c, a):
    return [[c * x for x in r] for r in a]


def mul(a, b):
    return [[sum(x * y for x, y in zip(r, c)) for c in zip(*b)] for r in a]


def block(a, b, c, d):
    return [r + s for r, s in zip(a, b)] + [r + s for r, s in zip(c, d)]


def diag(values):
    return [[v if i == j else 0 for j in range(len(values))]
            for i, v in enumerate(values)]


def det(a):
    n = len(a)
    total = 0
    for p in permutations(range(n)):
        inversions = sum(p[i] > p[j] for i in range(n) for j in range(i + 1, n))
        term = (-1) ** inversions
        for i in range(n):
            term *= a[i][p[i]]
        total += term
    return total


def poly_mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def charpoly(a):
    """Leibniz determinant of XI-A, independent of the Gram formula."""
    n = len(a)
    out = [0] * (n + 1)
    for p in permutations(range(n)):
        inversions = sum(p[i] > p[j] for i in range(n) for j in range(i + 1, n))
        term = [(-1) ** inversions]
        for i in range(n):
            term = poly_mul(term, [-a[i][p[i]], int(i == p[i])])
        for j, x in enumerate(term):
            out[j] += x
    return out


def rank(a):
    a = [[Fraction(x) for x in row] for row in a]
    r = 0
    for c in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        q = a[r][c]
        a[r] = [x / q for x in a[r]]
        for i in range(len(a)):
            if i != r:
                q = a[i][c]
                a[i] = [x - q * y for x, y in zip(a[i], a[r])]
        r += 1
    return r


def vec(a, v):
    return [sum(x * y for x, y in zip(row, v)) for row in a]


def divergence(vertices, edges):
    d = zero(vertices, len(edges))
    for j, (tail, head) in enumerate(edges):
        d[tail][j] += 1
        d[head][j] -= 1
    return d


def active(g):
    k = len(g)
    return block(eye(k), eye(k), scale(-1, g), add(eye(k), scale(-1, g)))


def active_energy(g):
    k = len(g)
    return block(scale(2, g), g, g, scale(2, eye(k)))


def raw(c):
    m, k = len(c), len(c[0])
    g = mul(tr(c), c)
    return block(eye(m), c, scale(-1, tr(c)), add(eye(k), scale(-1, g)))


CASES = [
    ("digon", 2, [(0, 1), (0, 1)], [[1], [-1]], [[2]],
     [1, 0, 1], 4),
    ("triangle", 3, [(0, 1), (1, 2), (2, 0)], [[1], [1], [1]], [[3]],
     [1, 1, 1], 3),
    ("digon-digon", 2, [(0, 1), (0, 1), (0, 1)],
     [[1, 1], [-1, 0], [0, -1]], [[2, 1], [1, 2]],
     [1, 0, 1, 0, 1], 6),
    ("digon-triangle", 3, [(0, 1), (0, 1), (0, 2), (2, 1)],
     [[1, 1], [-1, 0], [0, -1], [0, -1]], [[2, 1], [1, 3]],
     [1, 1, 1, 1, 1], 5),
    ("triangle-triangle", 4, [(0, 1), (1, 2), (2, 0), (1, 3), (3, 0)],
     [[1, 1], [1, 0], [1, 0], [0, 1], [0, 1]], [[3, 1], [1, 3]],
     [1, 2, 2, 2, 1], None),
]


def audit_case(case):
    name, vertices, edges, c, g, polynomial, order = case
    m, k = len(c), len(g)
    d = divergence(vertices, edges)
    require(mul(d, c) == zero(vertices, k), name + ": DC")
    require(mul(tr(c), c) == g and rank(c) == k, name + ": Gram/rank")
    a, b, t = active(g), active_energy(g), raw(c)
    p = block(c, zero(m, k), zero(k, k), eye(k))
    br = block(scale(2, eye(m)), c, tr(c), scale(2, eye(k)))
    ainv = block(add(eye(k), scale(-1, g)), scale(-1, eye(k)), g, eye(k))
    require(mul(a, ainv) == eye(2 * k) and mul(ainv, a) == eye(2 * k), name + ": inverse")
    require(det(a) == 1, name + ": determinant")
    require(charpoly(a) == polynomial, name + ": characteristic polynomial")
    require(mul(t, p) == mul(p, a), name + ": active embedding")
    require(mul(mul(tr(p), br), p) == b, name + ": metric pullback")
    require(mul(mul(tr(a), b), a) == b, name + ": active energy")
    require(mul(mul(tr(t), br), t) == br, name + ": raw energy")
    for size in range(1, 2 * k + 1):
        for indices in combinations(range(2 * k), size):
            minor = det([[b[i][j] for j in indices] for i in indices])
            require(minor > 0 if order else minor >= 0, name + ": positivity minor")
    require(rank(b) == (2 * k if order else 2 * k - 1), name + ": energy rank")
    if order:
        power = eye(2 * k)
        for n in range(1, order + 1):
            power = mul(power, a)
            require((power == eye(2 * k)) == (n == order), name + ": minimal order")
    else:
        v, u = [1, 1, -2, -2], [0, 0, 1, 1]
        nmat = add(a, eye(4))
        require(vec(nmat, u) == v and vec(nmat, v) == [0] * 4,
                name + ": nonzero Jordan chain")
        require(vec(b, v) == [0] * 4, name + ": zero-energy eigenvector")
        require(rank([u, v]) == 2, name + ": independent Jordan vectors")
        require(polynomial == poly_mul([1, 0, 1], [1, 2, 1]), name + ": factorization")
    count = 0
    for esigns in product((-1, 1), repeat=m):
        r = diag(esigns)
        for fsigns in product((-1, 1), repeat=k):
            s = diag(fsigns)
            cc = mul(mul(r, c), s)
            gg = mul(mul(s, g), s)
            aa = active(gg)
            sr = diag(list(esigns) + list(fsigns))
            sa = diag(list(fsigns) * 2)
            require(mul(mul(d, r), cc) == zero(vertices, k), name + ": oriented boundary")
            require(mul(tr(cc), cc) == gg, name + ": oriented Gram")
            require(raw(cc) == mul(mul(sr, t), sr), name + ": raw conjugacy")
            require(aa == mul(mul(sa, a), sa), name + ": active conjugacy")
            require(active_energy(gg) == mul(mul(sa, b), sa), name + ": metric conjugacy")
            count += 1
    print("CASE", name, "raw_dim=" + str(m + k), "active_dim=" + str(2 * k),
          "static_dim=" + str(m - k), "char_ascending=" + str(polynomial).replace(" ", ""),
          "det=1", "order=" + (str(order) if order else "infinite"),
          "energy=" + ("positive_definite" if order else "semidefinite_nullity_1"),
          "orientation_checks=" + str(count), "PASS")
    return count


def canonical_check(manifest):
    # Minimal source excerpt is frozen in this probe, not future Canon bytes.
    source = manifest["canonical_field"]
    cf, af, bf = source["C"], source["A_f"], source["B_f"]
    gf = [[2, -1], [-1, 3]]
    require(mul(tr(cf), cf) == gf and active(gf) == af and active_energy(gf) == bf,
            "canonical coordinate equality")
    s, ss = diag([1, -1]), diag([1, -1, 1, -1])
    require(mul(CASES[3][3], s) == cf, "canonical face orientation")
    require(mul(mul(ss, active(CASES[3][4])), ss) == af, "canonical A conjugacy")
    print("CANONICAL A_f_and_B_f_exact_marking PASS")


def main():
    data = (Path(__file__).parent / "SOURCES.json").read_bytes()
    if sha256(data).hexdigest() != SOURCE_MANIFEST_SHA256:
        print("INTEGRITY_STOP source=SOURCES.json")
        return 2
    manifest = json.loads(data.decode("utf-8"))
    print("FROZEN_SOURCE_MANIFEST canonical_refs=" + str(len(manifest["files"])) + " PASS")
    failed = []
    orientations = 0
    for case in CASES:
        try:
            orientations += audit_case(case)
        except ScientificFailure as error:
            failed.append(str(error))
            print("SCIENTIFIC_FAIL", str(error))
    try:
        canonical_check(manifest)
    except ScientificFailure as error:
        failed.append(str(error))
        print("SCIENTIFIC_FAIL", str(error))
    if failed:
        print("FIELD_CELL_SHEAR_CENSUS_SCIENTIFIC_FAIL failures=" + str(len(failed)))
    else:
        print("FIELD_CELL_SHEAR_CENSUS_PASS cases=5 orientations=" + str(orientations))
    return 0


if __name__ == "__main__":
    sys.exit(main())
