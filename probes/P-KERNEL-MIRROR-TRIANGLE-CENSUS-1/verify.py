#!/usr/bin/env python3
"""P-KERNEL-MIRROR-TRIANGLE-CENSUS-1: exact finite letter-group census.

Public adaptation of a disclosed, previously computed NON-CANONICAL candidate;
SOURCE.md gives custody and PREREG.md freezes the known target table. Scope is
L1: the five specified affine involutions on (Z/5Z)^6 as permutations. This
is not a claim about selected update U, coupled cells, physical curvature,
decoders, measures, exponent 10, or post hoc P1-P5 observations.

The main calculation uses the linear quotient and Schreier translation rank,
never an enumeration of all affine group elements. Explicit words generate a
rank-six translation basis; a nonzero covector changes sign under the linear
parts. Ten pairs, ten triple rows and the full group are compared with frozen
targets. crosscheck.py independently recomputes orders and orientability from
coordinate permutations, orbit/stabilizer frames and a doubled action. The
single public command executes both implementations:

    python3 probes/P-KERNEL-MIRROR-TRIANGLE-CENSUS-1/verify.py

--selftest runs only toy machinery (no letter census). Public executions,
including selftests, follow the public pin. Exact standard library only;
deterministic, no files written. Exit 0 means all checks and frozen targets
agree. Exit 1 means a failed consistency check, target mismatch or crosscheck;
exit 2 means unsupported arguments. A failure is preserved, not relabelled.
"""

import sys
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, product
from pathlib import Path

sys.dont_write_bytecode = True
CROSSCHECK_SHA256 = "880f670d8cd9eda087c8b145527c70743c376bfca9ccb3290822c948f088c9b9"

P = 5
N = 6

# ---------------------------------------------------------------------------
# The five letters (copied from probes/P-CENSUS-REPLAY-1/verify.py).
# ---------------------------------------------------------------------------
S_VEC = (2, 1, 2, 1)
U_VEC = (0, 1, 0, -1)
C_D = (2, 1, 3, 4, 1, 1)
V_E = (0, 0, 0, 0, 1, 0)


def gen_a(x):
    p1, p4, p1p, p4p, q, t = x
    return (p4, p1, p4p, p1p, q, t)


def gen_b(x):
    p1, p4, p1p, p4p, q, t = x
    return ((-p1p) % 5, (-p4p) % 5, (-p1) % 5, (-p4) % 5,
            (-q) % 5, (-t) % 5)


def gen_c(x):
    p1, p4, p1p, p4p, q, t = x
    b4 = ((-p1p) % 5, (-p4p) % 5, (-p1) % 5, (-p4) % 5)
    return ((b4[0] + S_VEC[0] + t * U_VEC[0]) % 5,
            (b4[1] + S_VEC[1] + t * U_VEC[1]) % 5,
            (b4[2] + S_VEC[2] + t * U_VEC[2]) % 5,
            (b4[3] + S_VEC[3] + t * U_VEC[3]) % 5,
            (1 - q) % 5, (-t) % 5)


def gen_d(x):
    return tuple((C_D[i] - x[i]) % 5 for i in range(6))


def gen_e(x):
    return tuple(((C_D[i] + V_E[i]) - x[i]) % 5 for i in range(6))


LETTERS = (("a", gen_a), ("b", gen_b), ("c", gen_c), ("d", gen_d), ("e", gen_e))

# ---------------------------------------------------------------------------
# Affine algebra over F_5. An affine map is (M, v): x -> M x + v.
# ---------------------------------------------------------------------------
ZERO = (0,) * N
IDM = tuple(tuple(1 if i == j else 0 for j in range(N)) for i in range(N))
IDENT = (IDM, ZERO)


def mat_vec(M, x):
    return tuple(sum(M[i][j] * x[j] for j in range(N)) % P for i in range(N))


def mat_mul(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(N)) % P
                       for j in range(N)) for i in range(N))


def vadd(x, y):
    return tuple((x[i] + y[i]) % P for i in range(N))


def vsub(x, y):
    return tuple((x[i] - y[i]) % P for i in range(N))


def compose(F, G):
    """F o G: x -> F(G(x))."""
    return (mat_mul(F[0], G[0]), vadd(mat_vec(F[0], G[1]), F[1]))


def compose_word(*factors):
    """Arguments are written left to right; the rightmost acts first."""
    result = IDENT
    for factor in factors:
        result = compose(result, factor)
    return result


def power(F, exponent):
    result = IDENT
    for _ in range(exponent):
        result = compose(result, F)
    return result


def apply(F, x):
    return vadd(mat_vec(F[0], x), F[1])


def affine_of(f):
    v = tuple(c % P for c in f(ZERO))
    cols = []
    for j in range(N):
        e_j = tuple(1 if k == j else 0 for k in range(N))
        img = f(e_j)
        cols.append(tuple((img[i] - v[i]) % P for i in range(N)))
    M = tuple(tuple(cols[j][i] for j in range(N)) for i in range(N))
    return (M, v)


def aff_order(F, bound=100000):
    G, k = F, 1
    while G != IDENT:
        G = compose(G, F)
        k += 1
        if k > bound:
            raise RuntimeError("order bound exceeded")
    return k


def mat_order(M, bound=100000):
    G, k = M, 1
    while G != IDM:
        G = mat_mul(G, M)
        k += 1
        if k > bound:
            raise RuntimeError("order bound exceeded")
    return k


def det_mod(M):
    A = [list(r) for r in M]
    det = 1
    for c in range(N):
        piv = next((i for i in range(c, N) if A[i][c] % P), None)
        if piv is None:
            return 0
        if piv != c:
            A[c], A[piv] = A[piv], A[c]
            det = -det
        det = det * A[c][c] % P
        inv = pow(A[c][c], -1, P)
        for i in range(c + 1, N):
            f = A[i][c] * inv % P
            if f:
                A[i] = [(A[i][j] - f * A[c][j]) % P for j in range(N)]
    return det % P


def rank_mod(vectors):
    A = [list(v) for v in vectors]
    r = 0
    for c in range(N):
        piv = next((i for i in range(r, len(A)) if A[i][c] % P), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        inv = pow(A[r][c], -1, P)
        A[r] = [(x * inv) % P for x in A[r]]
        for i in range(len(A)):
            if i != r and A[i][c] % P:
                f = A[i][c]
                A[i] = [(A[i][j] - f * A[r][j]) % P for j in range(N)]
        r += 1
        if r == len(A):
            break
    return r


def group_data(gens, cap=20000):
    """Finite group generated by affine maps gens.

    Returns (lin, t, order, lin_elements): lin = order of the linear image,
    t = F_5-rank of the translation subgroup (kernel of the linear-part
    map), order = lin * 5^t. The kernel is generated by the Schreier
    generators u s rep(u s)^-1, which are pure translations; a subgroup of
    the translation group F_5^6 is an F_5-subspace, so its order is 5^rank.
    """
    reps = {IDM: ZERO}
    queue = [IDM]
    trans = []
    i = 0
    while i < len(queue):
        M = queue[i]
        w = reps[M]
        i += 1
        for Ms, vs in gens:
            M2 = mat_mul(M, Ms)
            w2 = vadd(mat_vec(M, vs), w)
            if M2 not in reps:
                if len(reps) >= cap:
                    raise RuntimeError("linear image exceeds cap")
                reps[M2] = w2
                queue.append(M2)
            else:
                d = vsub(w2, reps[M2])
                if any(d):
                    trans.append(d)
    t = rank_mod(trans) if trans else 0
    return len(reps), t, len(reps) * P ** t, queue


def tri_type(l, m, n):
    if 1 in (l, m, n):
        return "DEGENERATE"
    e = Fraction(1, l) + Fraction(1, m) + Fraction(1, n) - 1
    if e > 0:
        return "SPHERICAL-REDUCIBLE" if sorted((l, m, n))[1] == 2 \
            else "SPHERICAL-PLATONIC"
    if e == 0:
        return "FLAT"
    return "HYPERBOLIC"


def triangle_record(g, h, k):
    """Full record for three affine involutions g, h, k."""
    l = aff_order(compose(g, h))
    m = aff_order(compose(g, k))
    n = aff_order(compose(h, k))
    typ = tri_type(l, m, n)
    lin, t, order, _ = group_data([g, h, k])
    rec = {"orders": (l, m, n), "type": typ, "lin": lin, "t": t,
           "order": order}
    if typ == "DEGENERATE":
        return rec
    e = Fraction(1, l) + Fraction(1, m) + Fraction(1, n) - 1
    for mm in (l, m, n):
        if order % (2 * mm):
            raise RuntimeError("dihedral order does not divide group order")
    chi = Fraction(order, 2) * e
    if chi.denominator != 1:
        raise RuntimeError("non-integer Euler characteristic")
    chi = chi.numerator
    _, _, plus, _ = group_data([compose(g, h), compose(h, k)])
    if 2 * plus == order:
        orientable = True
        if (2 - chi) % 2:
            raise RuntimeError("odd 2 - chi on an orientable surface")
        genus = (2 - chi) // 2
    elif plus == order:
        orientable = False
        genus = 2 - chi
        if genus < 1:
            raise RuntimeError("non-orientable surface with chi > 1")
    else:
        raise RuntimeError("rotation subgroup of index other than 1 or 2")
    rec.update({"excess": e, "chi": chi, "plus": plus,
                "orientable": orientable, "genus": genus})
    return rec


PASS = 0


def check(name, cond):
    global PASS
    if not cond:
        print("FAIL  " + name)
        print("RESULT  STOP")
        raise SystemExit(1)
    PASS += 1
    print("PASS  " + name)


def only_2_5(n):
    for q in (2, 5):
        while n % q == 0:
            n //= q
    return n == 1


# Known target table from the disclosed, previously computed candidate.
# These values are frozen before the first public execution, not fitted later.
EXPECTED_PAIRS = {"ab": 2, "ac": 10, "ad": 10, "ae": 10, "bc": 5,
                  "bd": 10, "be": 10, "cd": 10, "ce": 10, "de": 5}
# Each row: (pair orders, linear-image order, translation rank, group order,
#            exact excess, Euler characteristic, orientable genus).
EXPECTED_TRIPLES = {
    "abc": ((2, 10, 5), 100, 0, 100, Fraction(-1, 5), -10, 6),
    "abd": ((2, 10, 10), 8, 2, 200, Fraction(-3, 10), -30, 16),
    "abe": ((2, 10, 10), 8, 2, 200, Fraction(-3, 10), -30, 16),
    "acd": ((10, 10, 10), 40, 3, 5000, Fraction(-7, 10), -1750, 876),
    "ace": ((10, 10, 10), 40, 3, 5000, Fraction(-7, 10), -1750, 876),
    "ade": ((10, 10, 5), 4, 2, 100, Fraction(-3, 5), -30, 16),
    "bcd": ((5, 10, 10), 20, 3, 2500, Fraction(-3, 5), -750, 376),
    "bce": ((5, 10, 10), 20, 3, 2500, Fraction(-3, 5), -750, 376),
    "bde": ((10, 10, 5), 4, 2, 100, Fraction(-3, 5), -30, 16),
    "cde": ((10, 10, 5), 4, 2, 100, Fraction(-3, 5), -30, 16),
}


def explicit_translation_and_sign_audit(forms):
    a, b, c, d, e = (forms[name] for name in "abcde")
    eq = (0, 0, 0, 0, 1, 0)
    er = (0, 0, 0, 0, 0, 1)
    u = (0, 1, 0, 4, 0, 0)
    au = (1, 0, 4, 0, 0, 0)
    s = (2, 1, 2, 1, 1, 0)
    s0 = (2, 1, 2, 1, 0, 0)
    as0 = (1, 2, 1, 2, 0, 0)
    tq = compose(e, d)
    bd_comm = power(compose(b, d), 2)
    tr = compose(power(bd_comm, 2), power(tq, 4))
    tu = compose_word(c, tr, c, tr)
    tau = compose_word(a, tu, a)
    h = compose(c, b)
    h_inverse = compose(b, c)
    dh_comm = compose_word(d, h, d, h_inverse)
    ts = power(compose(tu, power(dh_comm, 4)), 3)
    ts0 = compose(ts, power(tq, 4))
    tas0 = compose_word(a, ts0, a)
    witnesses = (tq, tr, tu, tau, ts0, tas0)
    basis = (eq, er, u, au, s0, as0)
    expected_h_matrix = tuple(tuple((IDM[i][j] - (u[i] if j == 5 else 0)) % P
                                   for j in range(N)) for i in range(N))
    check("T1 explicit translation words yield six independent directions, "
          "h=cb and [d,h] have the stated affine forms",
          h == (expected_h_matrix, s)
          and dh_comm == (IDM, vsub(u, vadd(s, s)))
          and ts == (IDM, s)
          and all(F == (IDM, v) for F, v in zip(witnesses, basis))
          and rank_mod(basis) == N)
    ell = (1, 4, 1, 4, 0, 0)
    negative_ell = tuple((-x) % P for x in ell)
    check("E1 nonzero linear covector ell=(1,-1,1,-1,0,0) changes sign "
          "under all five linear parts; affine c contributes offset 2",
          any(ell)
          and all(tuple(sum(ell[i] * forms[name][0][i][j] for i in range(N)) % P
                        for j in range(N)) == negative_ell for name in "abcde")
          and sum(ell[i] * forms["c"][1][i] for i in range(N)) % P == 2)


def frozen_target_and_crosscheck(pairs, records, lin5, t5, order5):
    actual = {name: (R["orders"], R["lin"], R["t"], R["order"], R["excess"],
                     R["chi"], R["genus"]) for name, R in records.items()}
    check("V1 ten pair orders, ten complete triple rows and full group "
          "(200,6,3125000) equal the disclosed frozen targets",
          pairs == EXPECTED_PAIRS and actual == EXPECTED_TRIPLES
          and all(R["type"] == "HYPERBOLIC" and R["orientable"]
                  and 2*R["plus"] == R["order"] for R in records.values())
          and (lin5, t5, order5) == (200, 6, 3125000))
    helper_path = Path(__file__).with_name("crosscheck.py")
    if sha256(helper_path.read_bytes()).hexdigest() != CROSSCHECK_SHA256:
        raise RuntimeError("crosscheck.py differs from its frozen SHA-256")
    import crosscheck
    independently_computed = crosscheck.compute_records()
    comparison = {
        "pairs": pairs,
        "triples": {name: (R["orders"], R["excess"], R["type"], R["order"],
                            R["chi"], R["orientable"], R["genus"])
                    for name, R in records.items()},
        "full": (order5, P**N, lin5),
    }
    check("X1 independent permutation, orbit-stabilizer and doubled-action "
          "implementation agrees on all 21 records and full orbit/stabilizer",
          independently_computed == comparison)


# ---------------------------------------------------------------------------
# Machinery self-test on toy groups. Never touches the letters.
# ---------------------------------------------------------------------------
def perm_map(perm):
    def f(x):
        y = list(x)
        for i, j in enumerate(perm):
            y[j] = x[i]
        return tuple(y)
    return f


def selftest():
    print("== S. machinery self-test on toy groups ==")
    E0 = (1, 0, 0, 0, 0, 0)
    E1 = (0, 1, 0, 0, 0, 0)
    r1 = affine_of(lambda x: tuple((-c) % P for c in x))
    r2 = affine_of(lambda x: tuple((E0[i] - x[i]) % P for i in range(N)))
    r3 = affine_of(lambda x: tuple((E1[i] - x[i]) % P for i in range(N)))
    R = triangle_record(r1, r2, r3)
    check("S1 three point reflections: (5,5,5) HYPERBOLIC, |G| = 50, "
          "chi = -10, orientable genus 6",
          (R["orders"], R["type"], R["lin"], R["t"], R["order"], R["chi"],
           R["orientable"], R["genus"])
          == ((5, 5, 5), "HYPERBOLIC", 2, 2, 50, -10, True, 6))
    s1 = affine_of(perm_map((1, 0, 2, 3, 4, 5)))
    s2 = affine_of(perm_map((0, 2, 1, 3, 4, 5)))
    s3 = affine_of(perm_map((0, 1, 3, 2, 4, 5)))
    R = triangle_record(s1, s2, s3)
    check("S2 S4 by adjacent transpositions: (3,2,3) SPHERICAL-PLATONIC, "
          "|G| = 24, chi = 2, orientable genus 0",
          (R["orders"], R["type"], R["order"], R["t"], R["chi"],
           R["orientable"], R["genus"])
          == ((3, 2, 3), "SPHERICAL-PLATONIC", 24, 0, 2, True, 0))
    u = affine_of(perm_map((1, 0, 3, 2, 4, 5)))
    w = affine_of(perm_map((2, 3, 0, 1, 4, 5)))
    found = None
    for p, q, r, s in product(range(5), repeat=4):
        if len({p, q, r, s}) == 4 and p < q and r < s and p < r:
            perm = list(range(6))
            perm[p], perm[q] = q, p
            perm[r], perm[s] = s, r
            v = affine_of(perm_map(tuple(perm)))
            if (aff_order(compose(u, v)) == 5
                    and aff_order(compose(v, w)) == 3):
                found = v
                break
    check("S3a a third involution completing (2,3,5) exists in A5",
          found is not None)
    R = triangle_record(u, w, found)
    check("S3b A5 hemi-icosahedron: SPHERICAL-PLATONIC with orders {2,3,5}, "
          "|G| = 60, chi = 1, non-orientable genus 1",
          (sorted(R["orders"]), R["type"], R["order"], R["chi"],
           R["orientable"], R["genus"])
          == ([2, 3, 5], "SPHERICAL-PLATONIC", 60, 1, False, 1))
    m1 = affine_of(lambda x: (x[0], (-x[1]) % P) + tuple(x[2:]))
    m2 = affine_of(lambda x: (x[1], x[0]) + tuple(x[2:]))
    m3 = affine_of(lambda x: ((1 - x[0]) % P, x[1]) + tuple(x[2:]))
    R = triangle_record(m1, m2, m3)
    check("S4 square lattice mirrors mod 5: (4,2,4) FLAT, |G| = 200, "
          "chi = 0, orientable genus 1",
          (R["orders"], R["type"], R["lin"], R["t"], R["order"], R["chi"],
           R["orientable"], R["genus"])
          == ((4, 2, 4), "FLAT", 8, 2, 200, 0, True, 1))
    n1 = affine_of(lambda x: ((-x[0]) % P,) + tuple(x[1:]))
    n2 = affine_of(lambda x: (x[0], (-x[1]) % P) + tuple(x[2:]))
    n3 = affine_of(perm_map((0, 1, 3, 2, 4, 5)))
    R = triangle_record(n1, n2, n3)
    check("S5 three commuting mirrors: (2,2,2) SPHERICAL-REDUCIBLE, "
          "|G| = 8, chi = 2, orientable genus 0",
          (R["orders"], R["type"], R["order"], R["chi"], R["orientable"],
           R["genus"])
          == ((2, 2, 2), "SPHERICAL-REDUCIBLE", 8, 2, True, 0))
    R = triangle_record(n1, n1, n2)
    check("S6 repeated mirror is DEGENERATE", R["type"] == "DEGENERATE")
    check("S7 type function on the classical list",
          [tri_type(*x) for x in ((2, 3, 3), (2, 3, 4), (2, 3, 5), (2, 2, 7),
                                  (2, 3, 6), (2, 4, 4), (3, 3, 3), (2, 3, 7),
                                  (2, 10, 10), (5, 5, 5))]
          == ["SPHERICAL-PLATONIC"] * 3 + ["SPHERICAL-REDUCIBLE"]
          + ["FLAT"] * 3 + ["HYPERBOLIC"] * 3)
    check("S8 det and rank helpers", det_mod(s1[0]) == 4 and det_mod(IDM) == 1
          and rank_mod([E0, E1, vadd(E0, E1)]) == 2)


# ---------------------------------------------------------------------------
# The census.
# ---------------------------------------------------------------------------
def census():
    forms = {}
    states = list(product(range(P), repeat=N))

    print("== G. consistency gates against registered rows ==")
    ok_inv = ok_aff = True
    for name, f in LETTERS:
        F = affine_of(f)
        forms[name] = F
        for x in states:
            y = f(x)
            if f(y) != x:
                ok_inv = False
            if apply(F, x) != tuple(c % P for c in y):
                ok_aff = False
    check("G1 every letter has exact order two on all 15625 states",
          ok_inv and all(forms[name] != IDENT for name in "abcde"))
    check("G2 every letter is affine on all 15625 states "
          "(KERNEL-WEDGE-AFFINITY)", ok_aff)
    check("G3 det M_g = 1 for every letter; a, b linear; c, d, e strictly "
          "affine (KERNEL-WEDGE-AFFINITY)",
          all(det_mod(forms[n][0]) == 1 for n in "abcde")
          and forms["a"][1] == ZERO and forms["b"][1] == ZERO
          and all(forms[n][1] != ZERO for n in "cde"))
    check("G4 the five letters are pairwise distinct maps",
          len({forms[n] for n in "abcde"}) == 5)

    def comm(g, h):
        gh = compose(forms[g], forms[h])
        return compose(gh, gh)
    check("G5 fired commutators equal the registered translations "
          "(FIRED-COMMUTATOR-NOGO): [d,e] = T(0,0,0,0,3,0), "
          "[b,d] = T(0,0,0,0,3,3), [b,e] = T(0,0,0,0,1,3)",
          comm("d", "e") == (IDM, (0, 0, 0, 0, 3, 0))
          and comm("b", "d") == (IDM, (0, 0, 0, 0, 3, 3))
          and comm("b", "e") == (IDM, (0, 0, 0, 0, 1, 3)))
    ac = comm("a", "c")
    check("G6 the silent control [a,c] is not a translation "
          "(FIRED-COMMUTATOR-NOGO)", ac[0] != IDM)

    lin5, t5, order5, lin_elems = group_data([forms[n] for n in "abcde"])
    lin_orders = [mat_order(M) for M in lin_elems]
    check("G7 linear image of the letter group has order 200 with exactly 24 "
          "elements of order five (NATIVE-LINEAR-HODGE-ORDER5-OBSTRUCTION)",
          lin5 == 200 and sum(1 for o in lin_orders if o == 5) == 24)
    linf, _, _, _ = group_data([forms[n] for n in "bde"])
    check("G8 linear image of the fired subgroup <b,d,e> has order 4 "
          "(NATIVE-LINEAR-HODGE-ORDER5-OBSTRUCTION)", linf == 4)

    explicit_translation_and_sign_audit(forms)

    print("== B. pair orders (Coxeter matrix of the letters) ==")
    m = {}
    for g, h in combinations("abcde", 2):
        o = aff_order(compose(forms[g], forms[h]))
        o2 = aff_order(compose(forms[h], forms[g]))
        if o != o2:
            check("pair order independent of composition order", False)
        m[g + h] = o
        print("      m_%s%s = %d" % (g, h, o))

    print("== B. triples ==")
    recs = {}
    for g, h, k in combinations("abcde", 3):
        R = triangle_record(forms[g], forms[h], forms[k])
        name = g + h + k
        recs[name] = R
        if R["type"] == "DEGENERATE":
            print("      %s  orders=%s  DEGENERATE" % (name, R["orders"]))
            continue
        e = R["excess"]
        print("      %s  (m_%s,m_%s,m_%s)=(%d,%d,%d)  excess=%d/%d  %s  "
              "|lin|=%d  t=%d  |G|=%d  chi=%d  %s  genus=%d"
              % (name, g + h, g + k, h + k, R["orders"][0], R["orders"][1],
                 R["orders"][2], e.numerator, e.denominator, R["type"],
                 R["lin"], R["t"], R["order"], R["chi"],
                 "orientable" if R["orientable"] else "non-orientable",
                 R["genus"]))

    print("== B. the full letter group ==")
    print("      |linear image| = %d   t = %d   |<a,b,c,d,e>| = %d = 200 * 5^%d"
          % (lin5, t5, order5, t5))

    print("== A. the corollary of the registered linear order ==")
    check("A1 |<a,b,c,d,e>| = 200 * 5^t with 0 <= t <= 6, a {2,5}-number",
          order5 == 200 * 5 ** t5 and 0 <= t5 <= 6 and only_2_5(order5))
    check("A2 no element of the linear image has order divisible by 3",
          all(o % 3 for o in lin_orders))
    check("A3 every pair order m_gh has only the prime factors 2 and 5",
          all(only_2_5(o) for o in m.values()))
    check("A4 no triple is SPHERICAL-PLATONIC and no triple carries a 3",
          all(R["type"] != "SPHERICAL-PLATONIC" and 3 not in R["orders"]
              for R in recs.values()))
    check("A5 fired pair orders lie in {5, 10}",
          all(m[x] in (5, 10) for x in ("bd", "be", "de")))
    check("A6 no triple is DEGENERATE",
          all(R["type"] != "DEGENERATE" for R in recs.values()))

    frozen_target_and_crosscheck(m, recs, lin5, t5, order5)

    print("== H-B1. is every letter triple hyperbolic? ==")
    by_type = {}
    for name, R in recs.items():
        by_type.setdefault(R["type"], []).append(name)
    for typ in ("SPHERICAL-PLATONIC", "SPHERICAL-REDUCIBLE", "FLAT",
                "HYPERBOLIC", "DEGENERATE"):
        print("      %-20s %2d  %s" % (typ, len(by_type.get(typ, [])),
                                       " ".join(by_type.get(typ, []))))
    nonhyp = [n for n, R in recs.items() if R["type"] != "HYPERBOLIC"]
    if nonhyp:
        print("H-B1 FIRED  non-hyperbolic triples: " + " ".join(nonhyp))
    else:
        print("H-B1 HOLDS  all ten triples are HYPERBOLIC")
    return nonhyp


def main(argv):
    if argv[1:] == ["--selftest"]:
        selftest()
        print("RESULT  SELFTEST %d/%d PASS" % (PASS, PASS))
        return 0
    if argv[1:]:
        print("usage: verify.py [--selftest]")
        return 2
    try:
        selftest()
        nonhyp = census()
    except RuntimeError as err:
        print("FAIL  internal consistency: %s" % err)
        print("RESULT  STOP")
        return 1
    print("RESULT  %d/%d PASS  PART-A NO-PLATONIC-TRIPLE  FROZEN-TARGETS MATCH  CROSSCHECK AGREES  %s"
          % (PASS, PASS, "H-B1 FIRED" if nonhyp else "H-B1 HOLDS"))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
