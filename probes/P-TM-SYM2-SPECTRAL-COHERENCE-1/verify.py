# verify_tm_sym2_spectral_coherence_1.py
# Formal verifier for candidate C-TM-SYM2-SPECTRAL-COHERENCE-1.
# Python standard library only. Exact arithmetic in Q(sqrt5) as Fraction
# pairs a + b*sqrt5. No float in any assertion. Deterministic.
# Independent code path from the session recon: structural (rho, bits)
# selector parametrization; gauge from det +1 signed coordinate matrices
# filtered by line-set preservation; characteristic polynomial by signed
# permutation expansion; realizability by the direct 18 x 9 cross-product
# linear system.
import sys, itertools
from fractions import Fraction as F

def add(u, v): return (u[0] + v[0], u[1] + v[1])
def sub(u, v): return (u[0] - v[0], u[1] - v[1])
def mul(u, v): return (u[0]*v[0] + 5*u[1]*v[1], u[0]*v[1] + u[1]*v[0])
def neg(u): return (-u[0], -u[1])
def inv(u):
    n = u[0]*u[0] - 5*u[1]*u[1]
    assert n != 0
    return (F(u[0], 1)/n, F(-u[1], 1)/n)
def div(u, v): return mul(u, inv(v))
def gal(u): return (u[0], -u[1])
def sgn(u):
    a, b = u
    if a == 0 and b == 0: return 0
    if a >= 0 and b >= 0: return 1
    if a <= 0 and b <= 0: return -1
    return (1 if a > 0 else -1) if a*a > 5*b*b else (1 if b > 0 else -1)
Z = (F(0), F(0)); ONE = (F(1), F(0))
PHI = (F(1, 2), F(1, 2))

CERT = [0]
def cert(label, cond):
    if not cond:
        print("FIRED-OR-STOP: " + label)
        sys.exit(2)
    CERT[0] += 1
    print("CERT %02d PASS %s" % (CERT[0], label))

def dot(x, y):
    s = Z
    for i in range(3): s = add(s, mul(x[i], y[i]))
    return s
def vgal(x): return tuple(gal(c) for c in x)

# frozen carrier
V = [(Z, ONE, PHI), (Z, ONE, neg(PHI)),
     (ONE, PHI, Z), (ONE, neg(PHI), Z),
     (PHI, Z, ONE), (PHI, Z, neg(ONE))]
SIGMA = (1, 0, 3, 2, 5, 4)
W3 = ("001", "010", "011", "100", "101", "110")
NPERM = (5, 4, 3, 2, 1, 0)
TRANSFER = {"001": ("101", "011"), "010": ("110", "100"),
            "011": ("110", "101"), "100": ("001", "010"),
            "101": ("001", "011"), "110": ("010", "100")}
EDGES = tuple(sorted((W3.index(w), W3.index(x))
                     for w in W3 for x in TRANSFER[w]))
R2 = add(PHI, (F(2), F(0)))

cert("field sanity: phi^2 = phi + 1 and (phi+2)^2 = 5 phi^2",
     mul(PHI, PHI) == add(PHI, ONE)
     and mul(R2, R2) == mul((F(5), F(0)), mul(PHI, PHI)))
D = {}
okd = True
for i in range(6):
    okd = okd and dot(V[i], V[i]) == R2
    for j in range(6):
        if i != j:
            D[(i, j)] = dot(V[i], V[j])
            okd = okd and (D[(i, j)] == PHI or D[(i, j)] == neg(PHI))
cert("six lines: |v_i|^2 = phi + 2 and all pairwise dots are +-phi", okd)

# structural selector class: window pairs by lex minimum, line pairs by sigma
WMIN = (0, 1, 2); WMAX = (5, 4, 3)          # {001,110},{010,101},{011,100}
QP = ((0, 1), (2, 3), (4, 5))
sels = []
meta = {}
for rho in itertools.permutations(range(3)):
    sr = sum(1 for a in range(3) for b in range(a+1, 3) if rho[a] > rho[b]) % 2
    for bits in itertools.product((0, 1), repeat=3):
        s = [0]*6
        for k in range(3):
            head = QP[rho[k]][bits[k]]
            s[WMIN[k]] = head
            s[WMAX[k]] = SIGMA[head]
        s = tuple(s)
        sels.append(s)
        meta[s] = (sr, (bits[0] + bits[1] + bits[2]) % 2)
sels.sort()
cert("structural selector class: 3! * 2^3 = 48 distinct equivariant bijections",
     len(sels) == 48 and len(set(sels)) == 48
     and all(s[W3.index("".join("1" if c == "0" else "0" for c in w))]
             == SIGMA[s[W3.index(w)]] for s in sels for w in W3))

# gauge: det +1 signed coordinate matrices preserving the line set
def matv(M, v):
    return tuple(add(add(mul(M[r][0], v[0]), mul(M[r][1], v[1])),
                     mul(M[r][2], v[2])) for r in range(3))
def parallel(u, v):
    return (mul(u[1], v[2]) == mul(u[2], v[1])
            and mul(u[2], v[0]) == mul(u[0], v[2])
            and mul(u[0], v[1]) == mul(u[1], v[0])
            and any(c != Z for c in u))
Gset = set()
for p in itertools.permutations(range(3)):
    sp = 1 if sum(1 for a in range(3) for b in range(a+1, 3) if p[a] > p[b]) % 2 == 0 else -1
    for eps in itertools.product((1, -1), repeat=3):
        if sp * eps[0] * eps[1] * eps[2] != 1:
            continue
        M = [[Z]*3 for _ in range(3)]
        for j in range(3):
            M[p[j]][j] = ONE if eps[p[j]] == 1 else neg(ONE)
        pi = []
        good = True
        for i in range(6):
            u = matv(M, V[i])
            hit = [j for j in range(6) if parallel(u, V[j])]
            if len(hit) != 1:
                good = False; break
            pi.append(hit[0])
        if good:
            Gset.add(tuple(pi))
G = sorted(Gset)
cert("gauge from det +1 signed coordinate matrices preserving the line set: order 12",
     len(G) == 12)
orbs = []
seen = set()
for s in sels:
    if s in seen: continue
    o = sorted(set(tuple(pi[x] for x in s) for pi in G))
    for t in o: seen.add(t)
    orbs.append(o)
cert("free postcomposition with exactly 4 orbits of 12",
     len(orbs) == 4 and all(len(o) == 12 for o in orbs))
cert("orbit minimal representatives equal the public record",
     sorted(o[0] for o in orbs) == [(0, 2, 4, 5, 3, 1), (0, 2, 5, 4, 3, 1),
                                    (0, 4, 2, 3, 5, 1), (0, 4, 3, 2, 5, 1)])
def orbfib(o):
    fs = set(meta[t] for t in o)
    return fs
cert("orbits are exactly the four (chi_Q, chi_F) fibers of the structural characters",
     all(len(orbfib(o)) == 1 for o in orbs)
     and sorted(next(iter(orbfib(o))) for o in orbs)
     == [(0, 0), (0, 1), (1, 0), (1, 1)])
FIB = {k: next(iter(orbfib(orbs[k]))) for k in range(4)}
def eps(f): return (f[0] + f[1]) % 2

# realizability by the direct 18 x 9 cross-product system
def rref_null(rows, ncol):
    Mx = [r[:] for r in rows]
    piv = []; rr = 0
    for c in range(ncol):
        p = next((i for i in range(rr, len(Mx)) if Mx[i][c] != Z), None)
        if p is None: continue
        Mx[rr], Mx[p] = Mx[p], Mx[rr]
        iv = inv(Mx[rr][c])
        Mx[rr] = [mul(iv, t) for t in Mx[rr]]
        for i in range(len(Mx)):
            if i != rr and Mx[i][c] != Z:
                f = Mx[i][c]
                Mx[i] = [sub(Mx[i][k], mul(f, Mx[rr][k])) for k in range(ncol)]
        piv.append(c); rr += 1
    gens = []
    for fc in [c for c in range(ncol) if c not in piv]:
        g = [Z]*ncol; g[fc] = ONE
        for i, c in enumerate(piv):
            g[c] = neg(Mx[i][fc])
        gens.append(g)
    return gens
def det3(M):
    t1 = mul(M[0][0], sub(mul(M[1][1], M[2][2]), mul(M[1][2], M[2][1])))
    t2 = mul(M[0][1], sub(mul(M[1][0], M[2][2]), mul(M[1][2], M[2][0])))
    t3 = mul(M[0][2], sub(mul(M[1][0], M[2][1]), mul(M[1][1], M[2][0])))
    return add(sub(t1, t2), t3)
def realizable(pi, use_gal):
    src = [vgal(v) for v in V] if use_gal else V
    rows = []
    for i in range(6):
        t = V[pi[i]]
        for (r1, r2, tc1, tc2) in ((1, 2, 2, 1), (2, 0, 0, 2), (0, 1, 1, 0)):
            row = [Z]*9
            for c in range(3):
                row[3*r1 + c] = add(row[3*r1 + c], mul(src[i][c], t[tc1]))
                row[3*r2 + c] = sub(row[3*r2 + c], mul(src[i][c], t[tc2]))
            rows.append(row)
    gens = rref_null(rows, 9)
    if not gens: return False
    cands = [g[:] for g in gens]
    if len(gens) >= 2:
        cands.append([add(a, b) for a, b in zip(gens[0], gens[1])])
        cands.append([add(a, add(b, b)) for a, b in zip(gens[0], gens[1])])
        cands.append([add(add(a, a), b) for a, b in zip(gens[0], gens[1])])
    for g in cands:
        M = [[g[3*r + c] for c in range(3)] for r in range(3)]
        if det3(M) != Z:
            return True
    return False
perms = sorted(itertools.permutations(range(6)))
lin = sum(1 for pi in perms if realizable(pi, False))
cert("linear realizability count over all 720 line permutations: 60", lin == 60)
galset = [pi for pi in perms if realizable(pi, True)]
cert("exponent-one realizability count over all 720 line permutations: 60 [C4]",
     len(galset) == 60)
Wg = set(pi for pi in perms
         if all(pi[SIGMA[i]] == SIGMA[pi[i]] for i in range(6)))
cert("exponent-one intersection with the 48-element centralizer W: 12 [C4]",
     len(Wg) == 48 and sum(1 for pi in galset if pi in Wg) == 12)

# two-graph
def sd(i, j): return sgn(D[(i, j)])
tvals = [sd(i, j)*sd(j, k)*sd(k, i)
         for (i, j, k) in itertools.combinations(range(6), 3)]
cert("two-graph split of the 20 triples is 10 + 10 [C5]",
     tvals.count(1) == 10 and tvals.count(-1) == 10)
cert("Galois conjugation flips every pairwise dot sign [C5]",
     all(sgn(gal(D[k])) == -sgn(D[k]) for k in sorted(D)))

# signed transfer operator and characteristic polynomial
def Lmat(s, flips=None):
    if flips is None: flips = (1,)*6
    L = [[Z]*6 for _ in range(6)]
    for (wi, xi) in EDGES:
        d = D[(s[wi], s[xi])]
        if flips[s[wi]]*flips[s[xi]] == -1: d = neg(d)
        L[xi][wi] = d
    return L
def charpoly(L):
    co = [Z]*7                          # coefficient of x^k at index k
    for p in itertools.permutations(range(6)):
        prod = ONE; fix = 0; sp = 0; ok = True
        for i in range(6):
            if p[i] == i:
                fix += 1
            else:
                e = L[i][p[i]]
                if e == Z: ok = False; break
                prod = mul(prod, neg(e))
        if not ok: continue
        for a in range(6):
            for b in range(a+1, 6):
                if p[a] > p[b]: sp ^= 1
        co[fix] = add(co[fix], prod if sp == 0 else neg(prod))
    return tuple(co)
s0 = (0, 2, 4, 5, 3, 1)
cert("characteristic polynomial is representative-sign invariant (flip spot check)",
     charpoly(Lmat(s0)) == charpoly(Lmat(s0, (1, -1, 1, -1, 1, -1)))
     and charpoly(Lmat(s0)) == charpoly(Lmat(s0, (-1, 1, 1, 1, 1, 1))))
polys = {}
for s in sels:
    polys[s] = charpoly(Lmat(s))
cert("one characteristic polynomial across all 48 selectors [C2]",
     len(set(polys.values())) == 1)
cp = polys[s0]
print("CHARPOLY det(xI - L_s) = sum_k c_k x^k, c_k = a + b sqrt5:")
for k in range(6, -1, -1):
    print("  c_%d = (%s) + (%s) sqrt5" % (k, cp[k][0], cp[k][1]))

# battery and epsilon blindness
def F1(s):
    p = 1
    for (wi, xi) in EDGES: p *= sd(s[wi], s[xi])
    return p
TRI = set()
for a in range(6):
    for bidx in (W3.index(t) for t in TRANSFER[W3[a]]):
        for cidx in (W3.index(t) for t in TRANSFER[W3[bidx]]):
            if (cidx, a) in EDGES and len({a, bidx, cidx}) == 3:
                TRI.add(min([(a, bidx, cidx), (bidx, cidx, a), (cidx, a, bidx)]))
TRI = sorted(TRI)
def F3(s):
    return sum(sd(s[a], s[b])*sd(s[b], s[c])*sd(s[c], s[a]) for (a, b, c) in TRI)
def F3A(s):
    return sum(sd(s[a], s[b])*sd(s[b], s[c])*sd(s[c], s[a])
               for (a, b, c) in itertools.combinations(range(6), 3))
def blind(fun):
    vals = {}
    for k in range(4):
        vs = sorted(set(fun(t) for t in orbs[k]))
        if len(vs) != 1: return None
        vals[k] = vs[0]
    e0 = set(vals[k] for k in range(4) if eps(FIB[k]) == 0)
    e1 = set(vals[k] for k in range(4) if eps(FIB[k]) == 1)
    return (vals, not (len(e0 & e1) == 0 and e0 != e1))
b1 = blind(F1); b3 = blind(F3); b3a = blind(F3A)
bp = blind(lambda s: polys[s])
cert("battery F1 edge-sign product is orbit-constant and epsilon-blind [C3]",
     b1 is not None and b1[1] and set(b1[0].values()) == {1})
cert("battery transfer-triangle tau sum (2 triangles) is orbit-constant and epsilon-blind [C3]",
     len(TRI) == 2 and b3 is not None and b3[1] and set(b3[0].values()) == {0})
cert("battery all-triple tau sum is orbit-constant and epsilon-blind [C3]",
     b3a is not None and b3a[1] and set(b3a[0].values()) == {0})
cert("characteristic polynomial is epsilon-blind [C3]",
     bp is not None and bp[1])

# all-pairs similarity witnesses with P in {id, N}
UND = sorted(set(tuple(sorted(e)) for e in EDGES))
ADJ = {i: sorted(j for (a, b) in UND for i2, j in ((a, b), (b, a)) if i2 == i)
       for i in range(6)}
def witness(LA, LB):
    for P in ((0, 1, 2, 3, 4, 5), NPERM):
        if any((LB[x][w] == Z) != (LA[P[x]][P[w]] == Z)
               for x in range(6) for w in range(6)):
            continue
        need = {}
        good = True
        for (wi, xi) in EDGES:
            q = div(LB[xi][wi], LA[P[xi]][P[wi]])
            if q == ONE: need[(xi, wi)] = 1
            elif q == neg(ONE): need[(xi, wi)] = -1
            else: good = False; break
        if not good: continue
        d = [0]*6; d[0] = 1
        stack = [0]
        req = {}
        for (x, w), v in need.items():
            req.setdefault(x, []).append((w, v))
            req.setdefault(w, []).append((x, v))
        while stack:
            n = stack.pop()
            for (m, v) in sorted(req.get(n, [])):
                if d[m] == 0:
                    d[m] = v*d[n]; stack.append(m)
        if 0 in d: continue
        if all(d[x]*d[w] == v for (x, w), v in need.items()):
            return (P, tuple(d))
    return None
count_id = 0; count_N = 0
Ls = {s: Lmat(s) for s in sels}
for i in range(48):
    for j in range(i+1, 48):
        w = witness(Ls[sels[i]], Ls[sels[j]])
        if w is None:
            cert("all 1128 selector pairs admit a witness with P in {id, N} [C1]", False)
        if w[0] == (0, 1, 2, 3, 4, 5): count_id += 1
        else: count_N += 1
cert("all 1128 selector pairs admit a witness with P in {id, N} [C1]",
     count_id + count_N == 1128)
print("WITNESS first-found split: direct-id %d, direct-N %d (deterministic order)"
      % (count_id, count_N))
print("RESULT: PASS (%d certificates green)" % CERT[0])
sys.exit(0)
