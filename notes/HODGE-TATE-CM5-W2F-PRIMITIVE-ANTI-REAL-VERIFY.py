#!/usr/bin/env python3
"""Exact finite verifier for the CM5 W2F primitive anti-real no-go.

NON-CANONICAL. Standard library only. No floating point.

Reproduces the finite parts of
HODGE-TATE-CM5-W2F-PRIMITIVE-ANTI-REAL-NOGO-2026-09-11.md:

* all 20 generic mod-5 anti-real residue classes;
* all 156 generic five-primary Lagrangian planes for each residue;
* the exceptional ramified five-primary double-contraction census;
* the absence of a compatible exceptional five-primary 3-plane;
* the final f=phi two-adic contraction ranks;
* the exhaustive 97,155 three-plane audit over F_2;
* the unique small Diophantine survivor f=phi;
* the final theta-order / Perry-threshold inequality.
"""

from fractions import Fraction
from itertools import combinations, product
from math import gcd


# ---------------------------------------------------------------------------
# Basic exact linear algebra
# ---------------------------------------------------------------------------


def rref_mod(rows, p):
    A = [[int(x) % p for x in row] for row in rows if any(int(x) % p for x in row)]
    if not A:
        return tuple()
    m, n = len(A), len(A[0])
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if A[i][c]), None)
        if pivot is None:
            continue
        A[r], A[pivot] = A[pivot], A[r]
        inv = pow(A[r][c], -1, p)
        A[r] = [(x * inv) % p for x in A[r]]
        for i in range(m):
            if i != r and A[i][c]:
                f = A[i][c]
                A[i] = [(A[i][j] - f * A[r][j]) % p for j in range(n)]
        r += 1
        if r == m:
            break
    return tuple(tuple(row) for row in A[:r])


def rank_mod(A, p):
    return len(rref_mod(A, p))


def nullspace_mod(A, p):
    M = [[int(x) % p for x in row] for row in A]
    if not M:
        return []
    m, n = len(M), len(M[0])
    r = 0
    pivots = []
    for c in range(n):
        pivot = next((i for i in range(r, m) if M[i][c]), None)
        if pivot is None:
            continue
        M[r], M[pivot] = M[pivot], M[r]
        inv = pow(M[r][c], -1, p)
        M[r] = [(x * inv) % p for x in M[r]]
        for i in range(m):
            if i != r and M[i][c]:
                f = M[i][c]
                M[i] = [(M[i][j] - f * M[r][j]) % p for j in range(n)]
        pivots.append(c)
        r += 1
        if r == m:
            break
    free = [c for c in range(n) if c not in pivots]
    basis = []
    for fc in free:
        v = [0] * n
        v[fc] = 1
        for i, pc in enumerate(pivots):
            v[pc] = (-M[i][fc]) % p
        basis.append(tuple(v))
    return basis


def rref_subspaces(n, k, p):
    """Generate every k-plane of F_p^n exactly once in RREF."""
    for pivots in combinations(range(n), k):
        pivset = set(pivots)
        base = [[0] * n for _ in range(k)]
        free = []
        for r, pc in enumerate(pivots):
            base[r][pc] = 1
            for c in range(pc + 1, n):
                if c not in pivset:
                    free.append((r, c))
        for vals in product(range(p), repeat=len(free)):
            rows = [row[:] for row in base]
            for value, (r, c) in zip(vals, free):
                rows[r][c] = value
            yield tuple(tuple(row) for row in rows)


def pair_mod(v, w, J, p):
    return sum(v[i] * J[i][j] * w[j] for i in range(len(v)) for j in range(len(w))) % p


def mat_mul(A, B):
    return [
        [sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))]
        for i in range(len(A))
    ]


# ---------------------------------------------------------------------------
# Exterior algebra in the fixed integral H^1 basis
# ---------------------------------------------------------------------------


def form2_from_matrix(M, offset=0):
    out = {}
    for i in range(len(M)):
        for j in range(i + 1, len(M)):
            if M[i][j]:
                out[(i + offset, j + offset)] = Fraction(M[i][j])
    return out


def add_forms(*forms):
    out = {}
    for form in forms:
        for key, value in form.items():
            out[key] = out.get(key, Fraction(0)) + value
    return {k: v for k, v in out.items() if v}


def scale_form(c, form):
    c = Fraction(c)
    return {k: c * v for k, v in form.items() if c * v}


def wedge(left, right):
    out = {}
    for I, a in left.items():
        for J, b in right.items():
            if set(I) & set(J):
                continue
            inv = sum(1 for i in I for j in J if i > j)
            K = tuple(sorted(I + J))
            out[K] = out.get(K, Fraction(0)) + a * b * ((-1) ** inv)
    return {k: v for k, v in out.items() if v}


OMEGA = [
    [0, 1, 0, 0],
    [-1, 0, 1, 0],
    [0, -1, 0, 1],
    [0, 0, -1, 0],
]

R = [
    [-1, 2, 0, -2],
    [0, 1, 2, -2],
    [-2, 2, 1, 0],
    [-2, 0, 2, -1],
]

OR = mat_mul(OMEGA, R)

D = add_forms(form2_from_matrix(OMEGA, 0), form2_from_matrix(OMEGA, 4))
E = add_forms(form2_from_matrix(OR, 0), scale_form(-1, form2_from_matrix(OR, 4)))

D2 = wedge(D, D)
D3 = wedge(D2, D)
E2 = wedge(E, E)
E3 = wedge(E2, E)
DE2 = wedge(D, E2)
D2E = wedge(D2, E)

QBASE_D = add_forms(scale_form(5, D3), scale_form(-1, DE2))
QBASE_E = add_forms(scale_form(5, D2E), scale_form(-1, E3))


def uv(m, n):
    u = Fraction(
        5 * m**3 + 40 * m * m * n + 80 * m * n * n + 3 * m + 40 * n**3 + 4 * n,
        8,
    )
    v = Fraction(-(m**3 + 4 * m * m * n - 8 * m * n * n - m - 8 * n**3), 8)
    return u, v


def q_form(m, n):
    u, v = uv(m, n)
    out = add_forms(scale_form(u, QBASE_D), scale_form(v, QBASE_E))
    assert all(x.denominator == 1 for x in out.values())
    return {k: int(x) for k, x in out.items()}


def contraction_matrix_2(form_mod, p):
    pairs = list(combinations(range(8), 2))
    quads = list(combinations(range(8), 4))
    rows = []
    for J in quads:
        row = []
        for I in pairs:
            if set(I) & set(J):
                row.append(0)
                continue
            inds = I + J
            K = tuple(sorted(inds))
            coeff = form_mod.get(K, 0)
            inv = sum(1 for a in range(6) for b in range(a + 1, 6) if inds[a] > inds[b])
            row.append((coeff * ((-1) ** inv)) % p)
        rows.append(row)
    return rows, pairs


def contraction_matrix_3(form_mod, p):
    triples = list(combinations(range(8), 3))
    rows = []
    for J in triples:
        row = []
        for I in triples:
            if set(I) & set(J):
                row.append(0)
                continue
            inds = I + J
            K = tuple(sorted(inds))
            coeff = form_mod.get(K, 0)
            inv = sum(1 for a in range(6) for b in range(a + 1, 6) if inds[a] > inds[b])
            row.append((coeff * ((-1) ** inv)) % p)
        rows.append(row)
    return rows, triples


def bivector_coords(u, v, pairs, p):
    return tuple((u[i] * v[j] - u[j] * v[i]) % p for i, j in pairs)


def map_zero(M, vector, p):
    return all(sum(row[i] * vector[i] for i in range(len(vector))) % p == 0 for row in M)


def skew_matrix_from_bivector(vector, pairs, p):
    W = [[0] * 8 for _ in range(8)]
    for c, (i, j) in zip(vector, pairs):
        W[i][j] = c % p
        W[j][i] = (-c) % p
    return W


def normalize_projective(v, p):
    first = next(x for x in v if x % p)
    inv = pow(first % p, -1, p)
    return tuple((x * inv) % p for x in v)


def fixed_vector_map(u, C2, pairs, p):
    """Matrix of w -> C2(u wedge w)."""
    rows = []
    for outrow in C2:
        row = []
        for j in range(8):
            e = [0] * 8
            e[j] = 1
            biv = bivector_coords(u, e, pairs, p)
            row.append(sum(outrow[k] * biv[k] for k in range(len(biv))) % p)
        rows.append(row)
    return rows


# ---------------------------------------------------------------------------
# Generic five-primary audit: 20 residue classes x 156 Lagrangians
# ---------------------------------------------------------------------------

u1 = (1, 3, 1, 0)
u2 = (2, 2, 0, 1)
BASIS5 = [
    u1 + (0, 0, 0, 0),
    u2 + (0, 0, 0, 0),
    (0, 0, 0, 0) + u1,
    (0, 0, 0, 0) + u2,
]

J5 = [
    [0, 3, 0, 0],
    [2, 0, 0, 0],
    [0, 0, 0, 2],
    [0, 0, 3, 0],
]

planes5 = list(rref_subspaces(4, 2, 5))
lag5 = [P for P in planes5 if pair_mod(P[0], P[1], J5, 5) == 0]
assert len(planes5) == 806
assert len(lag5) == 156


def coord5_to_std(c):
    return tuple(sum(c[k] * BASIS5[k][i] for k in range(4)) % 5 for i in range(8))


def generic_plane_passes(m, n, P):
    Q = q_form(m, n)
    assert all(v % 5 == 0 for v in Q.values())
    Qbar = {I: (v // 5) % 5 for I, v in Q.items()}
    C2, pairs = contraction_matrix_2(Qbar, 5)
    h1 = coord5_to_std(P[0])
    h2 = coord5_to_std(P[1])
    biv = bivector_coords(h1, h2, pairs, 5)
    return map_zero(C2, biv, 5)


generic_residues = []
generic_passes = 0
for m in range(5):
    for n in range(5):
        if m == 0 and n == 0:
            continue
        if (-m + 2 * n) % 5 == 0:
            continue
        generic_residues.append((m, n))
        count = sum(1 for P in lag5 if generic_plane_passes(m, n, P))
        assert count == 0
        generic_passes += count

assert len(generic_residues) == 20
assert generic_passes == 0


# ---------------------------------------------------------------------------
# Exceptional five-primary branch: residue (m,n)=(2,1)
# ---------------------------------------------------------------------------

Q_exc = q_form(2, 1)
assert all(v % 5 == 0 for v in Q_exc.values())
Q_exc_bar = {I: (v // 5) % 5 for I, v in Q_exc.items()}
C2_exc, pairs_exc = contraction_matrix_2(Q_exc_bar, 5)
assert rank_mod(C2_exc, 5) == 23
K2_exc = nullspace_mod(C2_exc, 5)
assert len(K2_exc) == 5

# Projective elements of the 5-dimensional kernel. Decomposable bivectors are
# exactly those whose 8x8 skew matrix has rank 2 (p is odd).
projective_kernel = set()
for coeffs in product(range(5), repeat=5):
    if not any(coeffs):
        continue
    v = tuple(sum(coeffs[k] * K2_exc[k][i] for k in range(5)) % 5 for i in range(28))
    projective_kernel.add(normalize_projective(v, 5))

assert len(projective_kernel) == (5**5 - 1) // (5 - 1) == 781

compatible_planes = set()
for biv in projective_kernel:
    W = skew_matrix_from_bivector(biv, pairs_exc, 5)
    if rank_mod(W, 5) == 2:
        P = rref_mod(W, 5)
        assert len(P) == 2
        compatible_planes.add(P)

assert len(compatible_planes) == 156

# Exceptional theta pairing: L/5 = 4 Omega on each four-dimensional block.
J8 = [[0] * 8 for _ in range(8)]
for off in (0, 4):
    for i in range(4):
        for j in range(4):
            J8[off + i][off + j] = (4 * OMEGA[i][j]) % 5

for P in compatible_planes:
    assert pair_mod(P[0], P[1], J8, 5) == 0
    # Vectors extending P while remaining double-contraction compatible must
    # lie in the simultaneous kernel of w -> C2(u wedge w), C2(v wedge w).
    M = fixed_vector_map(P[0], C2_exc, pairs_exc, 5) + fixed_vector_map(P[1], C2_exc, pairs_exc, 5)
    extension_space = nullspace_mod(M, 5)
    assert len(extension_space) == 2

exceptional_three_extensions = 0


# ---------------------------------------------------------------------------
# Final f=phi two-adic audit
# ---------------------------------------------------------------------------

Q_phi = q_form(0, 1)
assert all(v % 4 == 0 for v in Q_phi.values())
Q_phi_bar = {I: (v // 4) % 2 for I, v in Q_phi.items()}

C2_phi, pairs_phi = contraction_matrix_2(Q_phi_bar, 2)
assert rank_mod(C2_phi, 2) == 27
K2_phi = nullspace_mod(C2_phi, 2)
assert len(K2_phi) == 1
unique_biv = K2_phi[0]
unique_skew_rank = rank_mod(skew_matrix_from_bivector(unique_biv, pairs_phi, 2), 2)
assert unique_skew_rank == 8  # nondecomposable, so no independent order-4 pair

C3_phi, triples_phi = contraction_matrix_3(Q_phi_bar, 2)
assert rank_mod(C3_phi, 2) == 48

# Use bit masks for the exhaustive 3-plane check.
row_masks = []
for row in C3_phi:
    mask = 0
    for i, bit in enumerate(row):
        if bit & 1:
            mask |= 1 << i
    row_masks.append(mask)


def det3_mod2(rows, cols):
    a = [[rows[r][c] & 1 for c in cols] for r in range(3)]
    return (
        a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
        - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
        + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
    ) & 1


def plucker3_mask(rows):
    mask = 0
    for i, cols in enumerate(triples_phi):
        if det3_mod2(rows, cols):
            mask |= 1 << i
    return mask


def C3_zero(mask):
    return all(((mask & rowmask).bit_count() & 1) == 0 for rowmask in row_masks)


three_total = 0
three_pass = 0
for P in rref_subspaces(8, 3, 2):
    three_total += 1
    if C3_zero(plucker3_mask(P)):
        three_pass += 1

assert three_total == 97155
assert three_pass == 0

# Therefore for H_2 ~= (Z/4)^a x (Z/2)^b:
#   a <= 1      (no independent pair of order-4 reductions)
#   a+b <= 2    (no compatible three-dimensional H[2])
# so |H_2| = 2^(2a+b) = 2^(a+(a+b)) <= 2^3 = 8.
phi_H2_upper = 8
phi_H5_upper = 5
phi_H_upper = phi_H2_upper * phi_H5_upper
phi_threshold = 50 * (2 + 4**2)
assert phi_H_upper == 40
assert phi_threshold == 900
assert phi_H_upper < phi_threshold


# ---------------------------------------------------------------------------
# Unique small Diophantine survivor
# ---------------------------------------------------------------------------

# S=(m+n)^2+n^2 <= 9 implies |n|<=3 and |m+n|<=3, hence |m|<=6.
small_survivors = []
for m in range(-6, 7):
    for n in range(-3, 4):
        if gcd(m, n) != 1:
            continue
        if m % 2 != 0 or n % 2 == 0:
            continue
        S = m * m + 2 * m * n + 2 * n * n
        T = m * m + 6 * m * n + 4 * n * n
        if m + 2 * n <= 0 or T != 4 or S > 9:
            continue
        small_survivors.append((m, n, S, T))

assert small_survivors == [(0, 1, 2, 4)]


print("generic five residue classes       =", len(generic_residues))
print("generic five full planes passing    =", generic_passes)
print("exceptional C2 rank                 =", rank_mod(C2_exc, 5))
print("exceptional compatible two-planes   =", len(compatible_planes))
print("exceptional three-plane extensions  =", exceptional_three_extensions)
print("phi C2 rank                         =", rank_mod(C2_phi, 2))
print("phi C2 kernel dimension             =", len(K2_phi))
print("phi kernel bivector skew rank       =", unique_skew_rank)
print("phi C3 rank                         =", rank_mod(C3_phi, 2))
print("phi compatible three-planes         =", three_pass)
print("phi three-planes checked            =", three_total)
print("phi H2 upper bound                  =", phi_H2_upper)
print("phi total H upper bound             =", phi_H_upper)
print("phi Perry threshold                 =", phi_threshold)
print("small primitive survivor            =", small_survivors[0])
print("RESULT: W2F primitive anti-real finite audit PASS")
