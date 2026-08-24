#!/usr/bin/env python3
# verify_tm_walsh_inertia_1.py
# Candidate C-TM-WALSH-INERTIA-1, TWIST-J project incubation lane.
# Written AFTER the freeze of PREREG-C-TM-WALSH-INERTIA-1.md
# (prereg sha256 155b0a0ecf767278f67b3fb4fc5a75e22d1c9918b1bc49c262f7f9c67f57e667).
# Python standard library only. Integer arithmetic only. No float anywhere.
# Deterministic stdout. No wall clock, no hostname, no machine identifier.
# Env: LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC

import sys

PASS = 0
FAIL = 0

def check(name, cond):
    global PASS, FAIL
    if cond:
        PASS += 1
        print("PASS " + name)
    else:
        FAIL += 1
        print("FAIL " + name)

# ---------- exact primitives ----------

def pc(x):
    return bin(x).count("1")

def pc2(x):
    c = 0
    while x:
        c += x & 1
        x >>= 1
    return c

def t(n):
    # polarized Thue-Morse sign, t(n) = (-1)^(s_2(n)); B6 twin popcount
    s = pc(n)
    if s != pc2(n):
        raise AssertionError("popcount mismatch at %d" % n)
    return -1 if (s & 1) else 1

def walsh(vec):
    # unnormalized W[u] = sum_x vec[x] * (-1)^(pc(u AND x)); in place butterfly
    w = list(vec)
    n = len(w)
    h = 1
    while h < n:
        for i in range(0, n, h * 2):
            for j in range(i, i + h):
                x = w[j]
                y = w[j + h]
                w[j] = x + y
                w[j + h] = x - y
        h *= 2
    return w

def inertia(w):
    p = 0
    q = 0
    z = 0
    for v in w:
        if v > 0:
            p += 1
        elif v < 0:
            q += 1
        else:
            z += 1
    return (p, q, z)

def conv_matrix(sign):
    n = len(sign)
    return [[sign[x ^ y] for y in range(n)] for x in range(n)]

def matvec_eig_ok(sign):
    # complete eigencheck: A chi_u = W[u] chi_u for all 2^k characters
    n = len(sign)
    A = conv_matrix(sign)
    W = walsh(sign)
    for u in range(n):
        chi = [(-1 if (pc(u & x) & 1) else 1) for x in range(n)]
        for x in range(n):
            s = 0
            row = A[x]
            for y in range(n):
                s += row[y] * chi[y]
            if s != W[u] * chi[x]:
                return False
    return True

def newton_esym(M):
    # exact elementary symmetric functions of the 4x4 integer matrix spectrum
    n = 4
    P = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    tr = []
    for _ in range(4):
        P = [[sum(P[i][a] * M[a][j] for a in range(n)) for j in range(n)]
             for i in range(n)]
        tr.append(sum(P[i][i] for i in range(n)))
    t1, t2, t3, t4 = tr
    e1 = t1
    v = e1 * t1 - t2
    assert v % 2 == 0
    e2 = v // 2
    v = e2 * t1 - e1 * t2 + t3
    assert v % 3 == 0
    e3 = v // 3
    v = e3 * t1 - e2 * t2 + e1 * t3 - t4
    assert v % 4 == 0
    e4 = v // 4
    return (e1, e2, e3, e4)

def esym_of(vals):
    a, b, c, d = vals
    e1 = a + b + c + d
    e2 = a*b + a*c + a*d + b*c + b*d + c*d
    e3 = a*b*c + a*b*d + a*c*d + b*c*d
    e4 = a*b*c*d
    return (e1, e2, e3, e4)

# ---------- V1: the 16 two-bit gates (E6) ----------

def v1_gates():
    ok_eig = True
    ok_aff = True
    ok_bent = True
    spectra = {}
    for a0 in (0, 1):
        for a1 in (0, 1):
            for a2 in (0, 1):
                for a12 in (0, 1):
                    sign = []
                    for idx in range(4):
                        x = (idx >> 1) & 1
                        y = idx & 1
                        F = a0 ^ (a1 & x) ^ (a2 & y) ^ (a12 & x & y)
                        sign.append(-1 if F else 1)
                    W = walsh(sign)
                    spectra[(a0, a1, a2, a12)] = (sign, W)
                    if not matvec_eig_ok(sign):
                        ok_eig = False
                    nz = [v for v in W if v != 0]
                    if a12 == 0:
                        if not (len(nz) == 1 and abs(nz[0]) == 4):
                            ok_aff = False
                    else:
                        if sorted(abs(v) for v in W) != [2, 2, 2, 2]:
                            ok_bent = False
                        want = (3, 1, 0) if a0 == 0 else (1, 3, 0)
                        if inertia(W) != want:
                            ok_bent = False
    check("V1.gates16.eigencheck", ok_eig)
    check("V1.gates16.affine.rank_one_pm4", ok_aff)
    check("V1.gates16.bent.abs2.inertia_by_a0", ok_bent)
    check("V1.XOR.spectrum", sorted(spectra[(0, 1, 1, 0)][1]) == [0, 0, 0, 4])
    check("V1.AND.spectrum", sorted(spectra[(0, 0, 0, 1)][1]) == [-2, 2, 2, 2])
    check("V1.OR.spectrum", sorted(spectra[(0, 1, 1, 1)][1]) == [-2, 2, 2, 2])
    A = conv_matrix(spectra[(0, 0, 0, 1)][0])
    A2 = [[sum(A[i][k] * A[k][j] for k in range(4)) for j in range(4)]
          for i in range(4)]
    check("V1.AND.involution_A2_eq_4I",
          all(A2[i][j] == (4 if i == j else 0)
              for i in range(4) for j in range(4)))
    return spectra

# ---------- V2: diagonal conjugation invariance (E7a) ----------

def v2_diag(spectra):
    signA, WA = spectra[(0, 0, 0, 1)]
    A = conv_matrix(signA)
    base = esym_of(sorted(WA))
    ok = True
    for dm in range(16):
        D = [(-1 if (dm >> i) & 1 else 1) for i in range(4)]
        M = [[D[i] * A[i][j] * D[j] for j in range(4)] for i in range(4)]
        if newton_esym(M) != base:
            ok = False
    check("V2.AND.diag_conjugation_charpoly_invariant", ok)

# ---------- V3: carry models (E7b, E7c) ----------

def v3_carry(spectra):
    WA = spectra[(0, 0, 0, 1)][1]
    slab = sorted([2 * w for w in WA] + [0, 0, 0, 0])
    for name, f in (("AND", lambda P, Q: P & Q), ("OR", lambda P, Q: P | Q)):
        sign = []
        for idx in range(8):
            P = (idx >> 2) & 1
            Q = (idx >> 1) & 1
            K = idx & 1
            F = f(P, Q) ^ K
            sign.append(-1 if F else 1)
        W = walsh(sign)
        check("V3.%s_XOR_K.spectrum" % name,
              sorted(W) == [-4, 0, 0, 0, 0, 4, 4, 4])
        check("V3.%s_XOR_K.active_inertia_31" % name,
              inertia(W) == (3, 1, 4))
        check("V3.%s_XOR_K.eigencheck" % name, matvec_eig_ok(sign))
        if name == "AND":
            check("V3.AND_XOR_K.slab_equals_2x_AND_spectrum",
                  sorted(W) == slab)

# ---------- number-theory tables ----------

def spf_sieve(N):
    spf = list(range(N + 1))
    i = 2
    while i * i <= N:
        if spf[i] == i:
            for j in range(i * i, N + 1, i):
                if spf[j] == j:
                    spf[j] = i
        i += 1
    return spf

def factor_sqfree(n, spf):
    # returns ascending prime list if squarefree, else None
    ps = []
    while n > 1:
        p = spf[n]
        n //= p
        if n % p == 0:
            return None
        ps.append(p)
    return ps

def mobius_spf(n, spf):
    cnt = 0
    while n > 1:
        p = spf[n]
        n //= p
        if n % p == 0:
            return 0
        cnt += 1
    return -1 if (cnt & 1) else 1

def cube(primes):
    k = len(primes)
    M = 1 << k
    prod = [1] * M
    for x in range(1, M):
        lb = x & (-x)
        i = lb.bit_length() - 1
        prod[x] = prod[x ^ lb] * primes[i]
    tv = [t(prod[x]) for x in range(M)]
    a = [-v for v in tv]
    return M, prod, tv, a

def c_subset(k, tv):
    # c(n) = sum_S (-1)^(k-|S|) t(n_S)
    M = 1 << k
    s = 0
    for x in range(M):
        s += tv[x] if ((k - pc(x)) & 1) == 0 else -tv[x]
    return s

# ---------- V4: explicit matrices (E1, E3) ----------

def v4_matrices(spf):
    targets = [n for n in range(1, 106, 2)
               if factor_sqfree(n, spf) is not None]
    targets += [1155, 15015]
    ok_eig = True
    ok_tr = True
    ok_fro = True
    for n in targets:
        ps = factor_sqfree(n, spf)
        M, prod, tv, a = cube(ps)
        A = conv_matrix(a)
        if sum(A[i][i] for i in range(M)) != M:
            ok_tr = False
        if sum(A[i][j] * A[i][j] for i in range(M) for j in range(M)) != M * M:
            ok_fro = False
        if not matvec_eig_ok(a):
            ok_eig = False
    check("V4.matrices.trace_2k (%d n)" % len(targets), ok_tr)
    check("V4.matrices.frobenius_4k", ok_fro)
    check("V4.matrices.eigencheck_complete", ok_eig)

# ---------- V5: census (E2, E3, E4, E8) ----------

def v5_census(spf, N):
    count_k = {}
    ext_k = {}
    ext_examples = {}
    rank1 = {}
    inert = {}
    bad_id = 0
    bad_c2 = 0
    bad_mom = 0
    bad_bound = 0
    bad_ext = 0
    bad_equiv = 0
    bad_rank1 = 0
    bad_sign = 0
    bad_bridge = 0
    n = 1
    while n <= N:
        ps = factor_sqfree(n, spf)
        if ps is not None:
            k = len(ps)
            M, prod, tv, a = cube(ps)
            W = walsh(a)
            c1 = c_subset(k, tv)
            # second path: mu(n/d) by independent spf factor count
            c3 = 0
            for x in range(M):
                mu = mobius_spf(n // prod[x], spf)
                if mu == 0:
                    bad_c2 += 1
                c3 += mu * tv[x]
            if c1 != c3:
                bad_c2 += 1
            sgn = 1 if (k & 1) else -1          # (-1)^(k+1)
            if W[M - 1] != sgn * c1:
                bad_id += 1
            # S2 bridge: c = (-1)^k * sum_S t(n_S) (-1)^{|S|}
            alt_sum = 0
            for x in range(M):
                alt_sum += tv[x] if (pc(x) & 1) == 0 else -tv[x]
            if c1 != (alt_sum if (k & 1) == 0 else -alt_sum):
                bad_bridge += 1
            if a[0] != 1 or sum(W) != M:
                bad_mom += 1
            if sum(v * v for v in W) != M * M:
                bad_mom += 1
            if abs(c1) > M:
                bad_bound += 1
            nz = [u for u in range(M) if W[u] != 0]
            ext = (abs(c1) == M)
            alt = all(tv[x] == (1 if (pc(x) & 1) else -1) for x in range(M))
            topone = (len(nz) == 1 and nz[0] == M - 1)
            if ext != alt:
                bad_equiv += 1
            if ext != (topone and (M == 1 or W[M - 1] == M)):
                bad_equiv += 1
            if ext:
                ext_k[k] = ext_k.get(k, 0) + 1
                if len(ext_examples.setdefault(k, [])) < 6:
                    ext_examples[k].append(n)
                if c1 != sgn * M:
                    bad_sign += 1
                if W[M - 1] != M:
                    bad_ext += 1
            if len(nz) == 1:
                u0 = nz[0]
                rank1[(k, pc(u0))] = rank1.get((k, pc(u0)), 0) + 1
                okchar = all(
                    a[x] == (-1 if (pc(u0 & x) & 1) else 1) for x in range(M))
                if not okchar or W[u0] != M:
                    bad_rank1 += 1
            inert.setdefault(k, {})
            key = inertia(W)
            inert[k][key] = inert[k].get(key, 0) + 1
            count_k[k] = count_k.get(k, 0) + 1
        n += 2
    check("V5.census.c_two_paths_agree", bad_c2 == 0)
    check("V5.census.E2_top_eigenvalue_identity", bad_id == 0)
    check("V5.census.S2_normalization_bridge", bad_bridge == 0)
    check("V5.census.E3_trace_and_parseval", bad_mom == 0)
    check("V5.census.A5a_bound", bad_bound == 0)
    check("V5.census.E4_equivalences_both_directions", bad_equiv == 0)
    check("V5.census.E4_extremal_top_value", bad_ext == 0)
    check("V5.census.E4_forced_sign (B5 adversarial: 0 violations)",
          bad_sign == 0)
    check("V5.census.rank_one_character_criterion", bad_rank1 == 0)
    print("CENSUS N=%d odd squarefree by k: %s" % (
        N, " ".join("k%d:%d" % (k, count_k[k]) for k in sorted(count_k))))
    print("EXTREMAL counts by k: %s" % (
        " ".join("k%d:%d" % (k, ext_k[k]) for k in sorted(ext_k))))
    for k in sorted(ext_examples):
        print("EXTREMAL k=%d first: %s" % (
            k, " ".join(str(v) for v in ext_examples[k])))
    print("RANK1 census by (k,|u|): %s" % (
        " ".join("(%d,%d):%d" % (k, w, rank1[(k, w)])
                 for (k, w) in sorted(rank1))))
    for k in sorted(inert):
        rows = sorted(inert[k].items())
        print("INERTIA k=%d patterns(pos,neg,zero):count | %s" % (
            k, " ".join("(%d,%d,%d):%d" % (p, q, z, c)
                        for (p, q, z), c in rows)))

# ---------- V6: witnesses beyond the sieve ----------

def is_prime_td(p):
    if p < 2:
        return False
    d = 2
    while d * d <= p:
        if p % d == 0:
            return False
        d += 1
    return True

def v6_witnesses():
    wl = [
        ("k6", 255255, [3, 5, 7, 11, 13, 17], None),
        ("k7", 4849845, [3, 5, 7, 11, 13, 17, 19], None),
        ("A7k4", 7461177, [3, 23, 71, 1523], -16),
        ("A7k5", 55888786221, [3, 23, 503, 857, 1879], 32),
    ]
    for tag, n, ps, cexp in wl:
        prodall = 1
        okp = True
        for p in ps:
            okp = okp and is_prime_td(p)
            prodall *= p
        check("V6.%s.factorization" % tag, okp and prodall == n)
        k = len(ps)
        M, prod, tv, a = cube(ps)
        W = walsh(a)
        c1 = c_subset(k, tv)
        sgn = 1 if (k & 1) else -1
        ok = (W[M - 1] == sgn * c1 and sum(W) == M
              and sum(v * v for v in W) == M * M and abs(c1) <= M)
        check("V6.%s.E2_E3_bound" % tag, ok)
        print("WITNESS %s n=%d k=%d c=%d inertia=%s" % (
            tag, n, k, c1, str(inertia(W))))
        if cexp is not None:
            nz = [u for u in range(M) if W[u] != 0]
            check("V6.%s.extremal_value_and_rigidity" % tag,
                  c1 == cexp and abs(c1) == M and nz == [M - 1]
                  and W[M - 1] == M and c1 == sgn * M)

# ---------- V7: even squarefree degeneracy (E5) ----------

def v7_even(spf, N):
    bad = 0
    cnt = 0
    for n in range(2, N + 1, 2):
        ps = factor_sqfree(n, spf)
        if ps is None:
            continue
        cnt += 1
        k = len(ps)
        M, prod, tv, a = cube(ps)
        c1 = c_subset(k, tv)
        W = walsh(a)
        if c1 != 0 or W[M - 1] != 0:
            bad += 1
    check("V7.even_squarefree.c_zero_and_top_kernel (%d n)" % cnt, bad == 0)

# ---------- V8 and breakers ----------

def v8_fences():
    c3 = t(3) + 1  # c(p) = 1 + t(p)
    check("V8.fence.convolution_not_pointwise_at_3",
          c3 == 2 and (-1) * t(3) == -1 and c3 != (-1) * t(3))
    check("V8.fence.t_not_multiplicative_pair",
          t(3) * t(11) != t(33))
    check("V8.fence.t_not_multiplicative_triple",
          t(3) * t(5) * t(7) != t(105))

def b1_b2_inversion(spf, N):
    # divisor lists
    divs = [[] for _ in range(N + 1)]
    for d in range(1, N + 1):
        for m in range(d, N + 1, d):
            divs[m].append(d)
    # c by mu*t with spf mu
    c_conv = [0] * (N + 1)
    for n in range(1, N + 1):
        s = 0
        for d in divs[n]:
            mu = mobius_spf(d, spf)
            if mu:
                s += mu * t(n // d)
        c_conv[n] = s
    # c by forward inversion of t = 1*c, no mu at all
    c_rec = [0] * (N + 1)
    bad = 0
    for n in range(1, N + 1):
        s = 0
        for d in divs[n]:
            if d < n:
                s += c_rec[d]
        c_rec[n] = t(n) - s
        if c_rec[n] != c_conv[n]:
            bad += 1
    check("B1.forward_inversion_no_mu_agrees_N%d" % N, bad == 0)
    check("B1.even_annihilation_in_window",
          all(c_rec[n] == 0 for n in range(2, N + 1, 2)))
    # mu by trial division
    bad2 = 0
    for n in range(1, N + 1):
        m = n
        cnt = 0
        sq = False
        d = 2
        while d * d <= m:
            if m % d == 0:
                m //= d
                cnt += 1
                if m % d == 0:
                    sq = True
                    break
            else:
                d += 1
        if not sq and m > 1:
            cnt += 1
        mu_td = 0 if sq else (-1 if cnt & 1 else 1)
        if mu_td != mobius_spf(n, spf):
            bad2 += 1
    check("B2.mu_trial_division_agrees_N%d" % N, bad2 == 0)

def b3_b4_witnesses(spf):
    # n=7: rank one on u=empty
    M, prod, tv, a = cube([7])
    W = walsh(a)
    check("B3.n7.rank_one_u_empty_c_zero",
          W == [2, 0] and c_subset(1, tv) == 0)
    # n=33: rank one on u={3}
    M, prod, tv, a = cube([3, 11])
    W = walsh(a)
    nz = [u for u in range(M) if W[u] != 0]
    check("B3.n33.rank_one_u_size1_c_zero",
          nz == [1] and W[1] == 4 and c_subset(2, tv) == 0)
    # B4 polarization on n=15
    M, prod, tv, a = cube([3, 5])
    W = walsh(a)
    Wn = [-v for v in W]
    p, q, z = inertia(W)
    check("B4.polarization_swaps_inertia", inertia(Wn) == (q, p, z))

def main():
    N_CENSUS = 200000
    N_SMALL = 20000
    print("C-TM-WALSH-INERTIA-1 verifier v1")
    print("ranges: census=%d small=%d" % (N_CENSUS, N_SMALL))
    spectra = v1_gates()
    v2_diag(spectra)
    v3_carry(spectra)
    spf = spf_sieve(N_CENSUS)
    v4_matrices(spf)
    v5_census(spf, N_CENSUS)
    v6_witnesses()
    v7_even(spf, N_SMALL)
    v8_fences()
    b1_b2_inversion(spf, N_SMALL)
    b3_b4_witnesses(spf)
    print("SUMMARY PASS=%d FAIL=%d" % (PASS, FAIL))
    return 0 if FAIL == 0 else 1

if __name__ == "__main__":
    sys.exit(main())
