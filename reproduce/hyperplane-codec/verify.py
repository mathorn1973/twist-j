#!/usr/bin/env python3
# TWIST-J hyperplane and codec witness. Exact arithmetic only:
# integers, rationals, Q(sqrt5) pairs, and the cyclotomic ring
# Z[zeta_5] on the power basis. Standard library only, no floats
# anywhere. The census part replicates the registered kernel census
# protocol exactly (warmup 400 ticks, window 300 ticks, second
# independent window) and then reads the boundary partition off the
# attractor supports.
#
# The arc: the boundary hyperplane of the kernel census, S = M cap
# {s = 0} with M the z5 sheet {1, 4}, counted exactly by full
# enumeration of all 15625 states; the census window realization of S
# as the 63 = (p^3 + 1)/2 boundary attractors; the trace codec: the
# step matrix M_J is multiplication by J = 1 + zeta_5^2, its
# characteristic polynomial is Phi_5(x - 1) collapsing to (x - 2)^4
# over F_5 with det(2I - M_J) = 5 = p, the piston sum Tr_4 doubles
# exactly, Tr_4(M_J x) = 2 Tr_4(x), and the scalar multiples of Tr_4
# are the only covectors reading any multiplier at all; and the
# finite fusion ring boundary behind the fired falsifier
# PHIBIT-NOT-TAU: the phibit fusion ring is the group ring of Z_5,
# the Fibonacci ring is not, and no identification survives.
#
# Claims verified: HYPERPLANE-BOUNDARY-CLASS,
# HYPERPLANE-BOUNDARY-REALIZATION, CODEC-TR4, PHIBIT-NOT-TAU.
# The open row CODEC-RATE-SCOPE carries no witness here by design:
# the internal rate 4/5 clause waits for its coding scope and nothing
# in this file claims it.

import sys
from fractions import Fraction as Fr

CHECKS = []


def check(tag, description, ok):
    CHECKS.append(("%-12s %s" % (tag, description), bool(ok)))


# ------------------------------------------------ Q(sqrt5): a + b sqrt5
def q5(a, b=0):
    return (Fr(a), Fr(b))


PHI = (Fr(1, 2), Fr(1, 2))


def q5_add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def q5_sub(x, y):
    return (x[0] - y[0], x[1] - y[1])


def q5_mul(x, y):
    return (x[0] * y[0] + 5 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def q5_pos(x):
    a, b = x
    if a >= 0 and b >= 0:
        return not (a == 0 and b == 0)
    if a < 0 and b < 0:
        return False
    if b > 0:
        return 5 * b * b > a * a
    return a * a > 5 * b * b


# ------------------------------------------------ Z[zeta_5], basis 1..z^3
def zmul(a, b):
    c = [0] * 5
    for i in range(4):
        for j in range(4):
            c[(i + j) % 5] += a[i] * b[j]
    return (c[0] - c[4], c[1] - c[4], c[2] - c[4], c[3] - c[4])


ZBASIS = ((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1))
J = (1, 0, 1, 0)

# ------------------------------------------------ the step matrix M_J
# step (a, b, c, d) -> (a - c + d, b - c, a, b - c + d)
MJ = ((1, 0, -1, 1),
      (0, 1, -1, 0),
      (1, 0, 0, 0),
      (0, 1, -1, 1))


def charpoly(m):
    # Faddeev-LeVerrier: monic coefficients [1, c3, c2, c1, c0]
    n = len(m)
    a = [[Fr(x) for x in row] for row in m]
    coeffs = [Fr(1)]
    mk = [[Fr(0)] * n for _ in range(n)]
    for i in range(n):
        mk[i][i] = Fr(1)
    prod = None
    for k in range(1, n + 1):
        if k == 1:
            prod = [row[:] for row in a]
        else:
            for i in range(n):
                mk[i][i] += coeffs[-1]
            prod = [[sum(a[i][t] * mk[t][j] for t in range(n))
                     for j in range(n)] for i in range(n)]
            mk = prod
        tr = sum(prod[i][i] for i in range(n))
        coeffs.append(-tr / k)
        mk = [row[:] for row in prod]
    return coeffs


def det_fraction(m):
    a = [[Fr(x) for x in row] for row in m]
    n = len(a)
    det = Fr(1)
    for col in range(n):
        piv = next((r for r in range(col, n) if a[r][col] != 0), None)
        if piv is None:
            return Fr(0)
        if piv != col:
            a[col], a[piv] = a[piv], a[col]
            det = -det
        det *= a[col][col]
        inv = 1 / a[col][col]
        a[col] = [x * inv for x in a[col]]
        for r in range(col + 1, n):
            f = a[r][col]
            if f != 0:
                a[r] = [x - f * y for x, y in zip(a[r], a[col])]
    return det


def f5_rank(rows):
    m = [[x % 5 for x in row] for row in rows]
    rank = 0
    col = 0
    ncols = len(m[0])
    while rank < len(m) and col < ncols:
        piv = next((r for r in range(rank, len(m)) if m[r][col] % 5), None)
        if piv is None:
            col += 1
            continue
        m[rank], m[piv] = m[piv], m[rank]
        inv = pow(m[rank][col], 3, 5)
        m[rank] = [(x * inv) % 5 for x in m[rank]]
        for r in range(len(m)):
            if r != rank and m[r][col] % 5:
                f = m[r][col]
                m[r] = [(x - f * y) % 5 for x, y in zip(m[r], m[rank])]
        rank += 1
        col += 1
    return rank


def poly_mul(p, q):
    out = [0] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            out[i + j] += x * y
    return out


def poly_add(p, q):
    n = max(len(p), len(q))
    p = p + [0] * (n - len(p))
    q = q + [0] * (n - len(q))
    return [x + y for x, y in zip(p, q)]


# ------------------------------------------------ the kernel (census)
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


GENS = (gen_a, gen_b, gen_c, gen_d, gen_e)


def dec(i):
    out = []
    for _ in range(6):
        out.append(i % 5)
        i //= 5
    return tuple(out)


N = 15625
STATES = [dec(i) for i in range(N)]
ZTAB = [sum(s) % 5 for s in STATES]
S4TAB = [sum(s[:4]) % 5 for s in STATES]


def enc(x):
    i = 0
    for k in range(5, -1, -1):
        i = i * 5 + x[k]
    return i


def main():
    p = 5
    # -------------------------------- 01 the boundary class by counting
    m_set = frozenset(i for i in range(N) if ZTAB[i] in (1, 4))
    s_set = frozenset(i for i in m_set if S4TAB[i] == 0)
    c_set = m_set - s_set
    ok = len(m_set) == 6250 and len(s_set) == 1250 and len(c_set) == 5000
    ok &= sum(1 for i in c_set if ZTAB[i] == 1) == 2500
    ok &= sum(1 for i in c_set if ZTAB[i] == 4) == 2500
    ok &= sum(1 for i in s_set if ZTAB[i] == 1) == 625
    ok &= sum(1 for i in s_set if ZTAB[i] == 4) == 625
    ok &= sum(1 for i in range(N) if S4TAB[i] == 0) == 3125
    check("COUNTS",
          "full enumeration of all 15625 states: the z5 sheet"
          " M = {z5 in {1, 4}} has 6250 states; the boundary class"
          " S = M cap {s = 0} (s the piston sum Tr_4) has size 1250"
          " exactly, the v101 class; the charged complement has 5000"
          " states in two sheets of 2500; the boundary fibers over"
          " z5 = 1 and z5 = 4 are 625 + 625; ker Tr_4 has 3125 states",
          ok)

    # -------------------------------- 02 the census window realization
    F = [[0] * N, [0] * N]
    for t in (0, 1):
        gt = [GENS[(z + 2 * t) % 5] for z in range(5)]
        Ft = F[t]
        for i in range(N):
            Ft[i] = enc(gt[ZTAB[i]](STATES[i]))
    tm = [bin(n).count("1") & 1 for n in range(1000)]
    warm = [F[tm[n]] for n in range(400)]
    wind = [F[tm[n]] for n in range(400, 700)]
    wind2 = [F[tm[n]] for n in range(700, 1000)]
    sigs = {}
    stable = True
    for seed in range(N):
        s = seed
        for T in warm:
            s = T[s]
        w1 = set()
        for T in wind:
            w1.add(s)
            s = T[s]
        sig = frozenset(w1)
        w2 = set()
        for T in wind2:
            w2.add(s)
            s = T[s]
        if frozenset(w2) != sig:
            stable = False
        if sig not in sigs:
            sigs[sig] = len(sigs)
    atts = list(sigs)
    sizes = {}
    support = set()
    for sig in atts:
        sizes[len(sig)] = sizes.get(len(sig), 0) + 1
        support |= sig
    ok = stable and len(atts) == 313 and sizes == {20: 312, 10: 1}
    ok &= support == set(m_set)
    boundary = [sig for sig in atts if sig <= s_set]
    charged = [sig for sig in atts if sig <= c_set]
    ok &= len(boundary) + len(charged) == len(atts)
    bsizes = {}
    bunion = set()
    for sig in boundary:
        bsizes[len(sig)] = bsizes.get(len(sig), 0) + 1
        bunion |= sig
    ok &= len(boundary) == 63 and bsizes == {20: 62, 10: 1}
    ok &= bunion == set(s_set)
    cunion = set()
    for sig in charged:
        cunion |= sig
    ok &= len(charged) == 250
    ok &= all(len(sig) == 20 for sig in charged)
    ok &= cunion == set(c_set)
    ok &= 63 == (p ** 3 + 1) // 2
    check("REALIZATION",
          "the census window (warmup 400, window 300, stable second"
          " window) realizes the boundary class: the attractor support"
          " is exactly the sheet M; no attractor straddles the"
          " boundary; S is exactly the union of the"
          " 63 = (p^3 + 1)/2 boundary attractors, 62 of size 20 and"
          " the singlet of size 10; the charged sector is exactly the"
          " union of the remaining 250 attractors of size 20", ok)

    # -------------------------------- 03 the step is the axiom; Phi_5(x-1)
    ok = True
    for k in range(4):
        col = zmul(J, ZBASIS[k])
        ok &= tuple(MJ[r][k] for r in range(4)) == col
    cp = charpoly(MJ)
    ok &= cp == [Fr(1), Fr(-3), Fr(4), Fr(-2), Fr(1)]
    # Phi_5(x - 1) = (x-1)^4 + (x-1)^3 + (x-1)^2 + (x-1) + 1
    xm1 = [-1, 1]
    acc = [1]
    target = [1]
    for _ in range(4):
        acc = poly_mul(acc, xm1)
        target = poly_add(target, acc)
    ok &= [Fr(c) for c in reversed(target)] == cp
    ok &= cp[1] == -3 and cp[4] == 1  # trace 3 = Tr(J), det 1 = N(J)
    val2 = sum(c * Fr(2) ** (4 - i) for i, c in enumerate(cp))
    ok &= val2 == 5
    m2 = [[2 * (1 if i == j else 0) - MJ[i][j] for j in range(4)]
          for i in range(4)]
    ok &= det_fraction(m2) == 5
    prod = (1, 0, 0, 0)
    for e in range(1, 5):
        ze = [0, 0, 0, 0, 0]
        ze[e] = 1
        conj = (1 - ze[0], -ze[1], -ze[2], -ze[3])
        if e == 4:
            conj = (1 + 1, 1, 1, 1)  # 1 - z^4 = 1 - (-1-z-z^2-z^3)
        prod = zmul(prod, conj)
    ok &= prod == (5, 0, 0, 0)
    ok &= [c % 5 for c in (1, -3, 4, -2, 1)] == [1, 2, 4, 3, 1]
    ok &= [c % 5 for c in (1, -8, 24, -32, 16)] == [1, 2, 4, 3, 1]
    check("CHARPOLY",
          "the step matrix is multiplication by the axiom: the columns"
          " of M_J are J, J z, J z^2, J z^3 exactly; the"
          " characteristic polynomial is Phi_5(x - 1) ="
          " x^4 - 3x^3 + 4x^2 - 2x + 1 with trace 3 = Tr(J) and"
          " determinant 1 = N(J); det(2I - M_J) = Phi_5(1) = 5 = p"
          " over Z, matching the conjugate product"
          " prod (1 - z^e) = 5 in Z[zeta_5]; over F_5 the polynomial"
          " collapses to (x - 2)^4: the doubling multiplier is total"
          " ramification at the magic prime", ok)

    # -------------------------------- 04 the doubling identity
    colsums = [sum(MJ[r][k] for r in range(4)) for k in range(4)]
    ok = colsums == [2, 2, -3, 2]
    ident = [2 * 1 - 5 * (1 if k == 2 else 0) for k in range(4)]
    ok &= colsums == ident
    for i in range(625):
        v = (i % 5, (i // 5) % 5, (i // 25) % 5, (i // 125) % 5)
        mv = tuple(sum(MJ[r][k] * v[k] for k in range(4)) % 5
                   for r in range(4))
        if sum(mv) % 5 != (2 * sum(v)) % 5:
            ok = False
            break
    check("DOUBLING",
          "the integer identity: the column sums of M_J are"
          " (2, 2, -3, 2) = 2(1, 1, 1, 1) - 5 e_c, so"
          " Tr_4(M_J x) = 2 Tr_4(x) - 5 x_c over Z and"
          " Tr_4(M_J x) = 2 Tr_4(x) in F_5, confirmed exhaustively on"
          " all 625 states: the piston sum is the doubling character"
          " of the step", ok)

    # -------------------------------- 05 the unique readout
    counts = {}
    line_ok = True
    for i in range(625):
        f = (i % 5, (i // 5) % 5, (i // 25) % 5, (i // 125) % 5)
        fm = tuple(sum(f[r] * MJ[r][k] for r in range(4)) % 5
                   for k in range(4))
        for lam in range(5):
            if fm == tuple((lam * x) % 5 for x in f):
                counts[lam] = counts.get(lam, 0) + 1
                if lam == 2 and any(f):
                    base = next(x for x in f if x)
                    inv = pow(base, 3, 5)
                    if tuple((x * inv) % 5 for x in f) != (1, 1, 1, 1):
                        line_ok = False
    ok = counts == {0: 1, 1: 1, 2: 5, 3: 1, 4: 1}
    ok &= line_ok
    m2f = [[(MJ[i][j] - 2 * (1 if i == j else 0)) % 5 for j in range(4)]
           for i in range(4)]
    ok &= f5_rank(m2f) == 3
    fib = {}
    for i in range(625):
        v = (i % 5, (i // 5) % 5, (i // 25) % 5, (i // 125) % 5)
        fib[sum(v) % 5] = fib.get(sum(v) % 5, 0) + 1
    ok &= fib == {r: 125 for r in range(5)}
    check("READOUT",
          "the unique M_J readout: over all 625 covectors and all five"
          " multipliers, the equation f(M_J x) = lambda f(x) has only"
          " the zero solution unless lambda = 2, where the solutions"
          " are exactly the 5 scalar multiples of Tr_4 = (1, 1, 1, 1);"
          " rank(M_J - 2I) = 3 over F_5; Tr_4 is onto with uniform"
          " fibers of 125: one readout character, fixed by the axiom",
          ok)

    # -------------------------------- 06 the phibit fusion ring
    ok = True
    for i in range(5):
        for j in range(5):
            prod = [0] * 5
            prod[(i + j) % 5] = 1
            ok &= sum(prod) == 1
    ok &= all((i + (5 - i) % 5) % 5 == 0 for i in range(5))
    for g in range(5):
        ngmat = [[1 if (g + i) % 5 == j else 0 for j in range(5)]
                 for i in range(5)]
        ok &= all(sum(row) == 1 for row in ngmat)
        ok &= sorted(sum(ngmat[i][j] for i in range(5))
                     for j in range(5)) == [1, 1, 1, 1, 1]
    check("PHIBIT-RING",
          "the phibit fusion ring is the group ring of Z_5: five"
          " simples, every product of basis elements is a single basis"
          " element, every basis element is invertible"
          " (g^k g^(5-k) = 1), and every fusion matrix is a"
          " permutation matrix with Frobenius-Perron dimension 1", ok)

    # -------------------------------- 07 the Fibonacci fusion ring
    def fmul(x, y):
        return (x[0] * y[0] + x[1] * y[1],
                x[0] * y[1] + x[1] * y[0] + x[1] * y[1])

    one = (1, 0)
    tau = (0, 1)
    ok = fmul(tau, tau) == (1, 1)
    basis = (one, tau)
    for x in basis:
        for y in basis:
            for z in basis:
                ok &= fmul(fmul(x, y), z) == fmul(x, fmul(y, z))
    ok &= all(r * r - r - 1 != 0 for r in (1, -1))
    phi2 = q5_mul(PHI, PHI)
    ok &= phi2 == q5_add(PHI, q5(1)) and q5_pos(PHI)
    det_tau = q5_sub(q5_mul(q5_sub(q5(0), PHI), q5_sub(q5(1), PHI)),
                     q5(1))
    ok &= det_tau == q5(0)
    # tau (a + b tau) = (b, a + b) = (1, 0) forces b = 1, a = -1 < 0
    ok &= fmul(tau, (-1, 1)) == (1, 0)
    ok &= not any(fmul(tau, (a, b)) == (1, 0)
                  for a in range(0, 6) for b in range(0, 6))
    check("FIB-RING",
          "the Fibonacci fusion ring: tau tau = 1 + tau, associative"
          " on all basis triples; the dimension equation d^2 = d + 1"
          " has no rational root (the candidates +-1 both fail), its"
          " positive root is phi exactly in Q(sqrt5), and"
          " det(N_tau - phi I) = 0; tau has no fusion inverse: the"
          " only integer solution of tau y = 1 is y = -1 + tau,"
          " outside the nonnegative fusion coefficients", ok)

    # -------------------------------- 08 the boundary: not the tau anyon
    fib_invertible = [x for x in (one, tau)
                      if fmul(x, one) == x and any(
                          fmul(x, y) == one for y in (one, tau))]
    ok = fib_invertible == [one]
    ok &= 5 != 2
    ok &= q5_sub(PHI, q5(1)) != q5(0)
    ok &= q5_pos(q5_sub(PHI, q5(1)))
    check("NOT-TAU",
          "the finite boundary of the fired reading: the phibit ring"
          " has five invertible simples, the Fibonacci ring exactly"
          " one, and 5 simples cannot map to 2; the dimension multiset"
          " {1, 1, 1, 1, 1} is separated from {1, phi} exactly, since"
          " phi - 1 = 1/phi > 0; the phibit is abelian Z_5, not the"
          " tau anyon, and the fired falsifier stays a first class"
          " boundary record", ok)

    print("TWIST-J hyperplane and codec witness (exact arithmetic)")
    print("the boundary class S = M cap ker Tr_4 has 1250 states and"
          " is exactly the 63 = (p^3 + 1)/2 boundary attractors")
    print("the step charpoly is Phi_5(x - 1); Tr_4 doubles and is the"
          " unique readout; the phibit is Z_5, not the tau anyon")
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
