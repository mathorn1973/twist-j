#!/usr/bin/env python3
# TWIST-J Maxwell closure witness. Exact integer arithmetic only:
# integer chains on finite complexes, integer Smith normal forms, and
# F_5 elimination. Standard library only, no floats anywhere. The
# symbolic identities are carried as exact linear algebra: each edge
# or face symbol is a basis vector of an integer coordinate space, so
# an identity in 32 or 96 symbols is a vanishing integer vector.
#
# The closure: the Bianchi identity dF = d(dA) = 0 identically in the
# 32 edge symbols of the tesseract, with gauge invariance an identity;
# Gauss as the boundary equation on the closed 2 x 2 x 2 spatial torus
# with Smith divisors all 1, a constructive dipole, and the integrated
# law on all 256 regions; the inhomogeneous pair on the 2^4 torus with
# conservation an identity in the 96 face symbols, Smith divisors all
# 1, H_1 free of rank 4 with explicit winding certificates; and the
# obstruction pair counted in p: Gauss solvable iff the total charge
# vanishes mod 5, the current pair iff conserved and all four winding
# numbers vanish mod 5.
#
# Claims verified: MAXWELL-BIANCHI, MAXWELL-GAUSS-CHAIN,
# MAXWELL-AMPERE-CHAIN, MAXWELL-OBSTRUCTION-P, MAXWELL-CLOSED.

import sys
from fractions import Fraction as Fr
from itertools import combinations, product

CHECKS = []


def check(tag, description, ok):
    CHECKS.append(("%-12s %s" % (tag, description), bool(ok)))


def vec(n):
    return [0] * n


def vadd(a, b, s=1):
    return [x + s * y for x, y in zip(a, b)]


def is_zero(a):
    return all(x == 0 for x in a)


def matmul(A, B):
    rows = len(A)
    mid = len(B)
    cols = len(B[0])
    out = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        Ai = A[i]
        for k in range(mid):
            a = Ai[k]
            if a == 0:
                continue
            Bk = B[k]
            Oi = out[i]
            for j in range(cols):
                Oi[j] += a * Bk[j]
    return out


def snf_divisors(mat):
    m = [row[:] for row in mat]
    R = len(m)
    C = len(m[0])
    divs = []
    t = 0
    while t < min(R, C):
        # find the smallest nonzero pivot in the submatrix
        best = None
        for r in range(t, R):
            for c in range(t, C):
                v = m[r][c]
                if v != 0 and (best is None or abs(v) < abs(best[2])):
                    best = (r, c, v)
        if best is None:
            break
        r0, c0, _ = best
        m[t], m[r0] = m[r0], m[t]
        for row in m:
            row[t], row[c0] = row[c0], row[t]
        again = True
        while again:
            again = False
            p = m[t][t]
            for r in range(t + 1, R):
                if m[r][t] % p != 0:
                    q = m[r][t] // p
                    m[r] = vadd(m[r], m[t], -q)
                    m[t], m[r] = m[r], m[t]
                    again = True
                    break
            if again:
                continue
            for c in range(t + 1, C):
                if m[t][c] % p != 0:
                    q = m[t][c] // p
                    for row in m:
                        row[c] -= q * row[t]
                    for row in m:
                        row[t], row[c] = row[c], row[t]
                    again = True
                    break
        p = m[t][t]
        for r in range(t + 1, R):
            if m[r][t]:
                q = m[r][t] // p
                m[r] = vadd(m[r], m[t], -q)
        for c in range(t + 1, C):
            if m[t][c]:
                q = m[t][c] // p
                for row in m:
                    row[c] -= q * row[t]
        # ensure the pivot divides the rest of the submatrix
        fixed = False
        for r in range(t + 1, R):
            for c in range(t + 1, C):
                if m[r][c] % p != 0:
                    m[t] = vadd(m[t], m[r])
                    fixed = True
                    break
            if fixed:
                break
        if fixed:
            continue
        divs.append(abs(p))
        t += 1
    return divs


def f5_solve(Amat, rhs):
    R = len(Amat)
    C = len(Amat[0])
    aug = [[Amat[r][c] % 5 for c in range(C)] + [rhs[r] % 5]
           for r in range(R)]
    piv = []
    r0 = 0
    for c in range(C):
        p = None
        for r in range(r0, R):
            if aug[r][c] % 5:
                p = r
                break
        if p is None:
            continue
        aug[r0], aug[p] = aug[p], aug[r0]
        inv = pow(aug[r0][c], 3, 5)
        aug[r0] = [(x * inv) % 5 for x in aug[r0]]
        for r in range(R):
            if r != r0 and aug[r][c] % 5:
                fac = aug[r][c]
                aug[r] = [(aug[r][k] - fac * aug[r0][k]) % 5
                          for k in range(C + 1)]
        piv.append(c)
        r0 += 1
    for r in aug:
        if all(x % 5 == 0 for x in r[:-1]) and r[-1] % 5:
            return None, piv
    x = [0] * C
    rr = 0
    for c in piv:
        x[c] = aug[rr][-1] % 5
        rr += 1
    return x, piv


def f5_rank(Amat):
    _, piv = f5_solve(Amat, [0] * len(Amat))
    return len(piv)


def q_rank(Amat):
    m = [[Fr(x) for x in row] for row in Amat]
    R = len(m)
    C = len(m[0])
    rank = 0
    col = 0
    while rank < R and col < C:
        p = next((r for r in range(rank, R) if m[r][col] != 0), None)
        if p is None:
            col += 1
            continue
        m[rank], m[p] = m[p], m[rank]
        m[rank] = [x / m[rank][col] for x in m[rank]]
        for r in range(R):
            if r != rank and m[r][col] != 0:
                f = m[r][col]
                m[r] = [x - f * y for x, y in zip(m[r], m[rank])]
        rank += 1
        col += 1
    return rank


def main():
    # ------------------------------------ the 3+1 tesseract (symbolic)
    tverts = list(product((0, 1), repeat=4))
    tedges = [(v, i) for v in tverts for i in range(4) if v[i] == 0]
    tfaces = [(v, i, j) for v in tverts
              for i, j in combinations(range(4), 2)
              if v[i] == 0 and v[j] == 0]
    tcubes = [(v, t) for v in tverts for t in combinations(range(4), 3)
              if all(v[i] == 0 for i in t)]
    teid = {e: n for n, e in enumerate(tedges)}
    tvid = {v: n for n, v in enumerate(tverts)}
    NE = len(tedges)
    NV = len(tverts)

    def tshift(v, i):
        w = list(v)
        w[i] += 1
        return tuple(w)

    # A: each edge symbol is a basis vector of Z^(NE + NV); the last NV
    # coordinates carry the gauge symbols Lambda.
    DIM = NE + NV

    def edge_form(v, i, gauged):
        f = vec(DIM)
        f[teid[(v, i)]] = 1
        if gauged:
            f[NE + tvid[tshift(v, i)]] += 1
            f[NE + tvid[v]] -= 1
        return f

    def dA_face(v, i, j, gauged):
        f = vec(DIM)
        f = vadd(f, edge_form(tshift(v, i), j, gauged))
        f = vadd(f, edge_form(v, j, gauged), -1)
        f = vadd(f, edge_form(tshift(v, j), i, gauged), -1)
        f = vadd(f, edge_form(v, i, gauged))
        return f

    ok = (NV, NE, len(tfaces), len(tcubes)) == (16, 32, 24, 8)
    Fsym = {(v, i, j): dA_face(v, i, j, False) for (v, i, j) in tfaces}
    for (v, t) in tcubes:
        i, j, k = t
        dF = vec(DIM)
        dF = vadd(dF, Fsym[(tshift(v, i), j, k)])
        dF = vadd(dF, Fsym[(v, j, k)], -1)
        dF = vadd(dF, Fsym[(tshift(v, j), i, k)], -1)
        dF = vadd(dF, Fsym[(v, i, k)])
        dF = vadd(dF, Fsym[(tshift(v, k), i, j)])
        dF = vadd(dF, Fsym[(v, i, j)], -1)
        ok &= is_zero(dF)
    check("BIANCHI",
          "on the 3+1 tesseract (16, 32, 24, 8): with 32 independent"
          " edge symbols as basis vectors, dF = d(dA) = 0 identically"
          " on all 8 cubes: the homogeneous Maxwell pair is an exact"
          " identity of the chain complex", ok)

    ok = True
    for (v, i, j) in tfaces:
        diff = vadd(dA_face(v, i, j, True), Fsym[(v, i, j)], -1)
        ok &= is_zero(diff)
    check("GAUGE",
          "gauge invariance is an identity: F[A + d Lambda] = F[A] in"
          " 16 additional vertex symbols on all 24 faces of the"
          " tesseract, exactly", ok)

    # ------------------------------------ the 2 x 2 x 2 spatial torus
    sverts = list(product((0, 1), repeat=3))
    svid = {v: n for n, v in enumerate(sverts)}
    sedges = [(v, i) for v in sverts for i in range(3)]
    seid = {e: n for n, e in enumerate(sedges)}
    SV = len(sverts)
    SE = len(sedges)

    def shead(v, i):
        w = list(v)
        w[i] = (w[i] + 1) % 2
        return tuple(w)

    B = [[0] * SE for _ in range(SV)]
    for e, (v, i) in enumerate(sedges):
        B[svid[v]][e] -= 1
        B[svid[shead(v, i)]][e] += 1

    divs = snf_divisors(B)
    ok = divs == [1] * 7
    ok &= all(sum(B[r][c] for r in range(SV)) == 0 for c in range(SE))
    check("GAUSS-Z",
          "Gauss as the boundary equation bd E = rho on the closed"
          " 2 x 2 x 2 spatial torus: the Smith form of the boundary"
          " over Z has all seven elementary divisors equal to 1 (rank"
          " 7, no torsion), and the augmentation annihilates the image:"
          " over Z the equation is solvable iff the total charge is"
          " zero", ok)

    a = (0, 0, 0)
    b = (1, 1, 0)
    Evec = vec(SE)
    Evec[seid[((0, 0, 0), 0)]] += 1
    Evec[seid[((1, 0, 0), 1)]] += 1
    rho = [sum(B[r][c] * Evec[c] for c in range(SE)) for r in range(SV)]
    ok = rho[svid[b]] == 1 and rho[svid[a]] == -1
    ok &= sum(abs(x) for x in rho) == 2
    ok_int = True
    for mask in range(1 << SV):
        inside = {r for r in range(SV) if (mask >> r) & 1}
        crossing = 0
        for e, (v, i) in enumerate(sedges):
            t_in = svid[v] in inside
            h_in = svid[shead(v, i)] in inside
            if h_in and not t_in:
                crossing += Evec[e]
            elif t_in and not h_in:
                crossing -= Evec[e]
        if crossing != sum(rho[r] for r in inside):
            ok_int = False
            break
    ok &= ok_int
    check("DIPOLE",
          "the constructive dipole: an oriented two edge path solves"
          " bd E = delta(b) - delta(a) exactly over Z, and the"
          " integrated law holds on every one of the 256 vertex"
          " regions: the oriented crossing sum equals the enclosed"
          " charge", ok)

    x5, piv5 = f5_solve(B, [0] * SV)
    ok = len(piv5) == 7
    rho5 = [0] * SV
    rho5[svid[(0, 0, 0)]] = 2
    rho5[svid[(0, 1, 1)]] = 3
    sol, _ = f5_solve(B, rho5)
    ok &= sol is not None and all(
        sum(B[r][c] * sol[c] for c in range(SE)) % 5 == rho5[r] % 5
        for r in range(SV))
    rho_bad = [0] * SV
    rho_bad[0] = 1
    bad, _ = f5_solve(B, rho_bad)
    ok &= bad is None
    ok &= SE - 7 == 17 == SE - SV + 1
    check("GAUSS-F5",
          "the Z_5 Gauss obstruction is counted in p: rank 7 over F_5"
          " with the augmentation on the image, so solvable iff the"
          " total charge vanishes mod 5; the zero sum charge (2, 3) is"
          " solved constructively, the unit total charge is obstructed;"
          " the cycle space has dimension 17 = E - V + 1", ok)

    # ------------------------------------ the 2^4 torus (Ampere face)
    verts = list(product((0, 1), repeat=4))
    vid = {v: n for n, v in enumerate(verts)}
    edges = [(v, m) for v in verts for m in range(4)]
    eid = {e: n for n, e in enumerate(edges)}
    faces = [(v, m, n) for v in verts
             for m, n in combinations(range(4), 2)]
    fid = {f: n for n, f in enumerate(faces)}
    V4, E4, F4 = len(verts), len(edges), len(faces)

    def head(v, m):
        w = list(v)
        w[m] = (w[m] + 1) % 2
        return tuple(w)

    B1 = [[0] * E4 for _ in range(V4)]
    for e, (v, m) in enumerate(edges):
        B1[vid[v]][e] -= 1
        B1[vid[head(v, m)]][e] += 1

    B2 = [[0] * F4 for _ in range(E4)]
    for f, (v, m, n) in enumerate(faces):
        B2[eid[(head(v, m), n)]][f] += 1
        B2[eid[(v, n)]][f] -= 1
        B2[eid[(head(v, n), m)]][f] -= 1
        B2[eid[(v, m)]][f] += 1

    ok = (V4, E4, F4) == (16, 64, 96)
    prod12 = matmul(B1, B2)
    ok &= all(is_zero(row) for row in prod12)
    check("CONSERVE",
          "on the 2^4 torus (16, 64, 96): bd1 bd2 = 0 as an exact"
          " integer matrix identity, so bd1(bd2 G) = 0 identically in"
          " the 96 independent face symbols: every solvable current is"
          " conserved, as an identity", ok)

    divs2 = snf_divisors(B2)
    ok = divs2 == [1] * 45
    ok &= q_rank(B1) == 15
    ok &= (E4 - 15) - 45 == 4
    check("AMPERE-Z",
          "the Smith form of bd2 over Z has all 45 elementary divisors"
          " equal to 1 (torsion free) and rank(bd1) = 15 over Q, so"
          " H_1 of the 2^4 torus is free of rank 49 - 45 = 4: the four"
          " winding classes of the closed spacetime torus", ok)

    def f_mu(mu, e):
        v, lam = edges[e]
        return 1 if (lam == mu and v[mu] == 1) else 0

    ok = all(sum(f_mu(mu, e) * B2[e][f] for e in range(E4)) == 0
             for mu in range(4) for f in range(F4))
    Jw = []
    base = (0, 0, 0, 0)
    for nu in range(4):
        Jv = vec(E4)
        Jv[eid[(base, nu)]] += 1
        Jv[eid[(head(base, nu), nu)]] += 1
        Jw.append(Jv)
    P = [[sum(f_mu(mu, e) * Jw[nu][e] for e in range(E4))
          for nu in range(4)] for mu in range(4)]
    ok &= P == [[1 if i == j else 0 for j in range(4)]
                for i in range(4)]
    face0 = fid[((0, 0, 0, 0), 0, 1)]
    G0 = vec(F4)
    G0[face0] = 1
    loop = [sum(B2[e][f] * G0[f] for f in range(F4)) for e in range(E4)]
    ok &= sum(abs(x) for x in loop) == 4
    ok &= all(sum(B1[r][e] * loop[e] for e in range(E4)) == 0
              for r in range(V4))
    check("WINDING",
          "the four winding certificates f_mu annihilate bd2 exactly"
          " (4 x 96 pairings all zero) and pair with the four"
          " elementary winding currents as the identity matrix; the"
          " contractible square loop is bd2 of its own face and is"
          " conserved", ok)

    sol1, _ = f5_solve(B2, Jw[0])
    J5 = [5 * x for x in Jw[0]]
    sol5, _ = f5_solve(B2, J5)
    ok = sol1 is None
    ok &= sol5 is not None and all(
        sum(B2[e][f] * sol5[f] for f in range(F4)) % 5 == J5[e] % 5
        for e in range(E4))
    fz = sum(f_mu(0, e) * J5[e] for e in range(E4))
    ok &= fz == 5
    check("OBSTRUCT-P",
          "the current obstruction is counted in p: the single winding"
          " current is obstructed over Z_5 (elimination exhibits the"
          " contradiction), while five parallel windings are solved"
          " over Z_5 constructively and stay Z obstructed with"
          " certificate value 5", ok)

    r2 = f5_rank(B2)
    r1 = f5_rank(B1)
    stack = [row[:] for row in B1]
    for mu in range(4):
        stack.append([f_mu(mu, e) for e in range(E4)])
    r_stack = f5_rank(stack)
    ok = r2 == 45 and r1 == 15 and r_stack == 19
    ok &= r2 == E4 - r_stack
    check("IFF-RANKS",
          "the iff by exact F_5 ranks: rank(bd2) = 45 = 64 - 19 ="
          " dim ker(bd1) - 4, with rank(bd1) = 15 and the four winding"
          " certificates independent on the cycle space: the current"
          " pair is solvable in the Z_5 theory iff the current is"
          " conserved and all four winding numbers vanish mod 5", ok)

    print("TWIST-J Maxwell closure witness (exact integer arithmetic)")
    print("Bianchi and gauge invariance identically in the 32 edge"
          " symbols; conservation identically in the 96 face symbols")
    print("the obstruction pair is counted in p = 5: total charge mod 5"
          " and the four winding numbers mod 5")
    print()
    passed = 0
    for i, (name, okv) in enumerate(CHECKS, 1):
        tag = "PASS" if okv else "FAIL"
        if okv:
            passed += 1
        print("%s %02d %s" % (tag, i, name))
    print()
    print("RESULT %d/%d %s" % (passed, len(CHECKS),
                               "ALL PASS" if passed == len(CHECKS)
                               else "FAILURES PRESENT"))
    return 0 if passed == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
