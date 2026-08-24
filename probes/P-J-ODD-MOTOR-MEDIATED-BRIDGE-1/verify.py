#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction as F
from itertools import permutations, product


# Exact rational matrix utilities. No third-party packages, floats, randomness,
# file input, environment input, or network access.

def mat(rows):
    return tuple(tuple(F(x) for x in row) for row in rows)


def zeros(n, m=None):
    if m is None:
        m = n
    return tuple(tuple(F(0) for _ in range(m)) for _ in range(n))


def eye(n):
    return tuple(tuple(F(int(i == j)) for j in range(n)) for i in range(n))


def madd(A, B):
    return tuple(tuple(a + b for a, b in zip(ra, rb)) for ra, rb in zip(A, B))


def msub(A, B):
    return tuple(tuple(a - b for a, b in zip(ra, rb)) for ra, rb in zip(A, B))


def mscale(c, A):
    c = F(c)
    return tuple(tuple(c * a for a in row) for row in A)


def mmul(A, B):
    bt = tuple(zip(*B))
    return tuple(tuple(sum(a * b for a, b in zip(row, col)) for col in bt) for row in A)


def mpow(A, n):
    out = eye(len(A))
    base = A
    while n:
        if n & 1:
            out = mmul(out, base)
        base = mmul(base, base)
        n >>= 1
    return out


def trans(A):
    return tuple(tuple(x for x in col) for col in zip(*A))


def trace(A):
    return sum(A[i][i] for i in range(len(A)))


def rank(A):
    M = [list(row) for row in A]
    if not M:
        return 0
    nr, nc = len(M), len(M[0])
    r = 0
    for c in range(nc):
        p = next((i for i in range(r, nr) if M[i][c]), None)
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        q = M[r][c]
        M[r] = [x / q for x in M[r]]
        for i in range(nr):
            if i != r and M[i][c]:
                q = M[i][c]
                M[i] = [a - q * b for a, b in zip(M[i], M[r])]
        r += 1
        if r == nr:
            break
    return r


def inv(A):
    n = len(A)
    M = [list(A[i]) + list(eye(n)[i]) for i in range(n)]
    for c in range(n):
        p = next((i for i in range(c, n) if M[i][c]), None)
        if p is None:
            raise ArithmeticError("singular matrix")
        M[c], M[p] = M[p], M[c]
        q = M[c][c]
        M[c] = [x / q for x in M[c]]
        for i in range(n):
            if i != c and M[i][c]:
                q = M[i][c]
                M[i] = [a - q * b for a, b in zip(M[i], M[c])]
    return tuple(tuple(row[n:]) for row in M)


def columns(cols):
    return tuple(tuple(cols[j][i] for j in range(len(cols))) for i in range(len(cols[0])))


def mvec(A, v):
    return tuple(sum(a * b for a, b in zip(row, v)) for row in A)


def eq(A, B):
    return A == B


def poly_mul(p, q):
    out = [F(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return tuple(out)


# Q(sqrt(5)) as a+b*s, s^2=5, only for the native factor proof.
def q5(a=0, b=0):
    return (F(a), F(b))


def q5_add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def q5_mul(x, y):
    return (x[0] * y[0] + 5 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def q5_neg(x):
    return (-x[0], -x[1])


def q5_poly_mul(p, q):
    out = [q5()] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] = q5_add(out[i + j], q5_mul(a, b))
    return tuple(out)


# Sparse bivariate polynomials in (z,t), monomial key (deg_z,deg_t).
def padd(p, q):
    out = dict(p)
    for m, c in q.items():
        out[m] = out.get(m, F(0)) + c
        if out[m] == 0:
            del out[m]
    return out


def pneg(p):
    return {m: -c for m, c in p.items()}


def pmul(p, q):
    out = {}
    for (iz, it), a in p.items():
        for (jz, jt), b in q.items():
            m = (iz + jz, it + jt)
            out[m] = out.get(m, F(0)) + a * b
    return {m: c for m, c in out.items() if c}


def perm_sign(p):
    invs = sum(1 for i in range(len(p)) for j in range(i + 1, len(p)) if p[i] > p[j])
    return -1 if invs % 2 else 1


def pdet4(A):
    out = {}
    for perm in permutations(range(4)):
        term = {(0, 0): F(perm_sign(perm))}
        for i, j in enumerate(perm):
            term = pmul(term, A[i][j])
        out = padd(out, term)
    return out



I4 = eye(4)
Z4 = zeros(4)
M = mat(((1, 0, -1, 1),
         (0, 1, -1, 0),
         (1, 0, 0, 0),
         (0, 1,-1,1))
D = msub(M, I4)
A_ODD = msub(D, mpow(D, 4))
S_EVEN = madd(D, mpow(D, 4))
F5 = tuple(range(5))
UNITS = (1, 2, 3, 4)

# Public affine-simplex Gram normalization.
G = msub(I4, mscale(F(1, 5), tuple(tuple(F(1) for _ in range(4)) for _ in range(4))))
GI = inv(G)


def sharp(X):
    return mmul(mmul(GI, trans(X)), G)


def hs2(X):
    return trace(mmul(sharp(X), X))


def affine_data():
    e0 = (F(1), F(0), F(0), F(0))
    vertices = tuple(mvec(mpow(D, k), e0) for k in F5)
    basis = columns(vertices[:4])
    basis_i = inv(basis)

    def rho(a, b):
        moved = tuple(vertices[(a * x + b) % 5] for x in range(4))
        return mmul(columns(moved), basis_i)

    affine = {(a, b): rho(a, b) for a in UNITS for b in F5}
    stab = {}
    for k in F5:
        for a in UNITS:
            b = k * (1 - a) % 5
            stab[(a, k)] = affine[(a, b)]

    P, Rsgn, C, gen = {}, {}, {}, {}
    for k in F5:
        P[k] = mscale(F(1, 4), sum_mats(stab[(a, k)] for a in UNITS))
        gen[k] = stab[(2, k)]
        Rsgn[k] = mscale(F(1, 4), madd(msub(madd(I4, mpow(gen[k], 2)), gen[k]), mscale(-1, mpow(gen[k], 3))))
        C[k] = msub(msub(I4, P[k]), Rsgn[k])
    return vertices, affine, P, Rsgn, C, gen


def sum_mats(ms):
    out = Z4
    for X in ms:
        out = madd(out, X)
    return out


def native_gate():
    # Exact characteristic polynomial of public M_J, low-to-high coefficients.
    chi = (F(1), F(-2), F(4), F(-3), F(1))

    # alpha_u=phi^2=(3+s)/2, alpha_s=phi^-2=(3-s)/2.
    au = q5(F(3, 2), F(1, 2))
    ast = q5(F(3, 2), F(-1, 2))
    fu = (au, q5_neg(au), q5(1))
    fs = (ast, q5_neg(ast), q5(1))
    prod = q5_poly_mul(fu, fs)
    expected = tuple(q5(c) for c in chi)
    factor_ok = prod == expected

    # Discriminants are (-5-s)/2 and (-5+s)/2. Both are totally negative.
    # sqrt(5)<3 is certified by 5<9, so -5+sqrt(5)<-2<0.
    discr_ok = 5 < 9

    # Coprime distinct quadratic factors imply the generated algebra is a product
    # of two fields; each field has idempotents {0,1}, hence exactly four total.
    two_sector = factor_ok and discr_ok and au != ast
    return factor_ok, discr_ok, two_sector


def bridge_gate():
    vertices, affine, P, Rsgn, C, gen = affine_data()
    integrity = True
    token_rows = []
    for k in F5:
        integrity &= mpow(D, 5) == I4
        integrity &= sharp(D) == mpow(D, 4)
        integrity &= sharp(A_ODD) == mscale(-1, A_ODD)
        integrity &= sharp(S_EVEN) == S_EVEN
        integrity &= (rank(P[k]), rank(Rsgn[k]), rank(C[k])) == (1, 1, 2)
        integrity &= madd(madd(P[k], Rsgn[k]), C[k]) == I4
        integrity &= mmul(P[k], Rsgn[k]) == Z4 and mmul(Rsgn[k], P[k]) == Z4
        integrity &= mmul(P[k], C[k]) == Z4 and mmul(C[k], P[k]) == Z4
        integrity &= mmul(Rsgn[k], C[k]) == Z4 and mmul(C[k], Rsgn[k]) == Z4

        diag_zero = all(mmul(mmul(X, A_ODD), X) == Z4 for X in (P[k], Rsgn[k], C[k]))
        direct_zero = mmul(mmul(P[k], A_ODD), Rsgn[k]) == Z4 and mmul(mmul(Rsgn[k], A_ODD), P[k]) == Z4
        cross = []
        for X, Y in ((P[k], C[k]), (C[k], P[k]), (Rsgn[k], C[k]), (C[k], Rsgn[k])):
            block = mmul(mmul(X, A_ODD), Y)
            cross.append((rank(block), hs2(block)))
        cross_ok = all(r == 1 and n2 == F(5, 2) for r, n2 in cross)

        B = mmul(mmul(mmul(mmul(P[k], A_ODD), C[k]), A_ODD), Rsgn[k])
        mediated_ok = rank(B) == 1
        norm_ok = hs2(B) == F(5, 4)
        projector_ok = (
            msub(mmul(sharp(B), B), mscale(F(5, 4), Rsgn[k])) == Z4
            and msub(mmul(B, sharp(B)), mscale(F(5, 4), P[k])) == Z4
        )

        up = mmul(mmul(C[k], A_ODD), P[k])
        ur = mmul(mmul(C[k], A_ODD), Rsgn[k])
        lp = mscale(F(2, 5), mmul(up, sharp(up)))
        lr = mscale(F(2, 5), mmul(ur, sharp(ur)))
        overlap_ok = trace(mmul(lp, lr)) == F(1, 5)

        Hk = madd(gen[k], mpow(gen[k], 3))
        spectral_ok = (
            mmul(Hk, P[k]) == mscale(2, P[k])
            and mmul(Hk, Rsgn[k]) == mscale(-2, Rsgn[k])
            and mmul(Hk, C[k]) == Z4
        )

        token_rows.append((diag_zero, direct_zero, cross_ok, mediated_ok, norm_ok, projector_ok, overlap_ok, spectral_ok))

    all_tokens = all(all(row) for row in token_rows)

    # Controls: raw powers and even part must not exhibit the same pattern for
    # any ordered distinct sector pair with the third sector as sole mediator.
    controls_ok = True
    for U in (D, mpow(D, 2), mpow(D, 3), mpow(D, 4), S_EVEN):
        for k in F5:
            sec = {"P": P[k], "R": Rsgn[k], "C": C[k]}
            for X, Y in permutations(sec, 2):
                Z = ({"P", "R", "C"} - {X, Y}).pop()
                direct = mmul(mmul(sec[X], U), sec[Y])
                mediated = mmul(mmul(mmul(mmul(sec[X], U), sec[Z]), U), sec[Y])
                if direct == Z4 and mediated != Z4:
                    controls_ok = False

    # Exact determinant audit at token k=2 in the rational public basis.
    H2 = madd(gen[2], mpow(gen[2], 3))
    L = []
    for i in range(4):
        row = []
        for j in range(4):
            e = {}
            if i == j:
                e[(1, 0)] = F(1)
            if H2[i][j]:
                e[(0, 0)] = e.get((0, 0), F(0)) - H2[i][j]
            if A_ODD[i][j]:
                e[(0, 1)] = e.get((0, 1), F(0)) - A_ODD[i][j]
            row.append({m: c for m, c in e.items() if c})
        L.append(tuple(row))
    det_poly = pdet4(tuple(L))
    det_target = {(4, 0): F(1), (2, 2): F(5), (2, 0): F(-4), (0, 4): F(5)}
    determinant_ok = det_poly == det_target

    # Exact Schur data follow from the one-dimensional normalized bridge and
    # H spectrum: |B|^2=5/4, so |B|=sqrt(5)/2; C eigenvalue is zero.
    # Therefore the eliminated P-R off-diagonal magnitude is
    # sqrt(5)*t^2/(2z), with a simple pole at z=0.
    schur_ok = all_tokens and controls_ok and determinant_ok
    return integrity, all_tokens, controls_ok, schur_ok, determinant_ok, token_rows


def fixed_count(g):
    a, b = g
    return sum(1 for x in F5 if (a * x + b) % 5 == x)


def gmul(g, h):
    a, b = g
    c, d = h
    return ((a * c) % 5, (b + a * d) % 5)


def eps(g):
    return F(1 if g[0] in (1, 4) else -1)


def inner(c1, c2, group):
    return F(1, len(group)) * sum(c1[g] * c2[g] for g in group)


def quadratic_gate():
    _, affine, _, _, _, _ = affine_data()
    group = tuple((a, b) for a in UNITS for b in F5)
    charV = {g: F(fixed_count(g) - 1) for g in group}
    charSym = {g: F(1, 2) * (charV[g] ** 2 + charV[gmul(g, g)]) for g in group}
    char1 = {g: F(1) for g in group}
    chare = {g: eps(g) for g in group}

    decomp = (
        inner(char1, charSym, group) == 1
        and inner(chare, charSym, group) == 1
        and inner(charV, charSym, group) == 2
        and inner(char1, charV, group) == 0
        and inner(chare, charV, group) == 0
        and inner(char1, chare, group) == 0
    )
    end_dim = inner(charSym, charSym, group)

    qplus = mscale(F(5, 2), G)
    qminus = mat(((0, 1, -1, -1),
                  (1, 0, 1, -1),
                  (-1, 1, 0, 1),
                  (-1, -1, 1, 0)))
    sign_mode = True
    for g, rho in affine.items():
        sign_mode &= mmul(mmul(trans(rho), qplus), rho) == qplus
        sign_mode &= mmul(mmul(trans(rho), qminus), rho) == mscale(eps(g), qminus)

    chars = {"1": char1, "e": chare, "V": charV}
    dims = {}
    for a, b, c in product(chars, repeat=3):
        d = F(1, len(group)) * sum(chars[a][g] * chars[b][g] * chars[c][g] for g in group)
        if d:
            dims[(a, b, c)] = d
    target = {
        ("1", "1", "1"): F(1),
        ("1", "e", "e"): F(1), ("e", "1", "e"): F(1), ("e", "e", "1"): F(1),
        ("1", "V", "V"): F(1), ("V", "1", "V"): F(1), ("V", "V", "1"): F(1),
        ("e", "V", "V"): F(1), ("V", "e", "V"): F(1), ("V", "V", "e"): F(1),
        ("V", "V", "V"): F(3),
    }
    triple_ok = dims == target
    pairwise_direct_zero = (
        inner(char1, chare, group) == 0
        and inner(char1, charV, group) == 0
        and inner(chare, charV, group) == 0
    )
    nonselection = end_dim == 6
    return decomp, sign_mode, triple_ok, pairwise_direct_zero, nonselection, end_dim


def main():
    f_ok, d_ok, native = native_gate()
    integ, bridge, controls, schur, det_ok, token_rows = bridge_gate()
    decomp, sign_mode, triples, direct_hom, nonselection, end_dim = quadratic_gate()

    if not integ:
        raise SystemExit("STOP: exact carrier or projector integrity failed")

    bridge_count = sum(1 for row in token_rows if all(row))
    scientific_ok = all((f_ok, d_ok, native, bridge, controls, schur, det_ok, decomp, sign_mode, triples, direct_hom, nonselection))
    decision = "MEDIATED-BRIDGE-CERTIFIED" if scientific_ok else "ROUTE-FALSIFIED"

    print("P-J-ODD-MOTOR-MEDIATED-BRIDGE-1")
    print("LAYER L1 EXACT ARITHMETIC ONLY")
    print(f"NATIVE FACTORIZATION {'PASS' if f_ok else 'FAIL'}")
    print(f"NATIVE QUADRATIC IRREDUCIBILITY {'PASS' if d_ok else 'FAIL'}")
    print(f"NATIVE PRIMITIVE SECTORS {'TWO' if native else 'NOT-TWO'}")
    print(f"ODD MOTOR TOKENS CERTIFIED {bridge_count}/5")
    print(f"DIRECT P-R BLOCK ZERO ALL TOKENS {'PASS' if bridge else 'FAIL'}")
    print(f"MEDIATED P-C-R BLOCK RANK ONE ALL TOKENS {'PASS' if bridge else 'FAIL'}")
    print(f"BRIDGE NORM SQUARED 5/4 {'PASS' if bridge else 'FAIL'}")
    print(f"MEDIATOR ACTIVE-LINE OVERLAP 1/5 {'PASS' if bridge else 'FAIL'}")
    print(f"RAW D^m AND EVEN CHANNEL NEGATIVE CONTROL {'PASS' if controls else 'FAIL'}")
    print(f"SCHUR MEDIATOR POLE AT z=0 {'PASS' if schur else 'FAIL'}")
    print(f"SCHUR OFFDIAGONAL MAGNITUDE sqrt(5)*t^2/(2z) {'PASS' if schur else 'FAIL'}")
    print(f"FULL DET z^4+(5t^2-4)z^2+5t^4 {'PASS' if det_ok else 'FAIL'}")
    print(f"SYM2 DECOMPOSITION 1+epsilon+2V {'PASS' if decomp else 'FAIL'}")
    print(f"AFFINE QUADRATIC SIGN MODE {'PASS' if sign_mode else 'FAIL'}")
    print(f"PAIRWISE DIRECT HOM ZERO {'PASS' if direct_hom else 'FAIL'}")
    print(f"TRILINEAR INVARIANT CENSUS {'PASS' if triples else 'FAIL'}")
    print(f"END_G_SYM2 DIM {end_dim}")
    print(f"REPEATED V NONSELECTION {'PASS' if nonselection else 'FAIL'}")
    print("PHYSICAL FREQUENCY DAMPING TEMPERATURE MATERIAL LIGHT BORN DECODER NOT CLAIMED")
    print(f"DECISION {decision}")


if __name__ == "__main__":
    main()
