#!/usr/bin/env python3
# RECON, NON-CANONICAL. Exploration against Public Canon v97 (tag canon-v97, main 738e0421).
# No preregistration was frozen before this ran; results are audit input, not candidate labels.
# Exact arithmetic only (integers mod 5, Fractions, Q(sqrt5) pairs). Standard library only.
# Run from the root of mathorn1973/twist-j:
#   LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC python3 <this file>
import importlib.util, itertools, sys
from fractions import Fraction as Fr

spec = importlib.util.spec_from_file_location("census", "reproduce/census/verify.py")
census = importlib.util.module_from_spec(spec); spec.loader.exec_module(census)
P = 5
OK = []
def check(name, cond):
    OK.append(bool(cond)); print(("PASS " if cond else "FAIL ") + name)

# ---------- Part 1: affine form of the native generators on F_5^6 ----------
def affine(g):
    c = g((0,)*6)
    cols = [tuple((g(tuple(1 if k == i else 0 for k in range(6)))[k] - c[k]) % P for k in range(6)) for i in range(6)]
    L = [[cols[j][i] for j in range(6)] for i in range(6)]
    for x in itertools.product(range(P), repeat=6):
        if tuple((sum(L[i][j]*x[j] for j in range(6)) + c[i]) % P for i in range(6)) != g(x):
            return None
    return L, c
AFF = {n: affine(g) for n, g in zip("abcde", census.GENS)}
check("1.1 all five generators are affine on all 15625 states", all(AFF[n] is not None for n in "abcde"))

# fibre (q,r) action: identity for a, point reflection x -> 2c - x for b,c,d,e
inv2 = 3
centres = {}
ok = True
for n in "abcde":
    img = {}
    for x in itertools.product(range(P), repeat=6):
        y = census.GENS["abcde".index(n)](x)
        img.setdefault((x[4], x[5]), set()).add((y[4], y[5]))
    ok &= all(len(v) == 1 for v in img.values())
    f0 = next(iter(img[(0, 0)]))
    if n == "a":
        ok &= all(next(iter(v)) == k for k, v in img.items())
    else:
        ok &= all(next(iter(v)) == ((f0[0]-k[0]) % P, (f0[1]-k[1]) % P) for k, v in img.items())
        centres[n] = ((inv2*f0[0]) % P, (inv2*f0[1]) % P)
check("1.2 fibre map depends on the fibre only; a is identity, b,c,d,e are point reflections", ok)
print("     reflection centres on the fibre:", centres)
check("1.3 centres equal the four exceptional readies (0,0),(3,0),(3,3),(1,3)",
      set(centres.values()) == {(0,0),(3,0),(3,3),(1,3)})

# ---------- Part 2: invariant alternating forms on F_5^6 (three-pentit reading) ----------
def nullspace(M, ncols):
    M = [r[:] for r in M]; piv = []; r = 0
    for c in range(ncols):
        pr = next((i for i in range(r, len(M)) if M[i][c] % P), None)
        if pr is None: continue
        M[r], M[pr] = M[pr], M[r]
        inv = pow(M[r][c], P-2, P); M[r] = [(v*inv) % P for v in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] % P:
                f = M[i][c]; M[i] = [(a - f*b) % P for a, b in zip(M[i], M[r])]
        piv.append(c); r += 1
        if r == len(M): break
    basis = []
    for fc in [c for c in range(ncols) if c not in piv]:
        v = [0]*ncols; v[fc] = 1
        for i, pc in enumerate(piv): v[pc] = (-M[i][fc]) % P
        basis.append(v)
    return len(piv), basis
pairs = [(i, j) for i in range(6) for j in range(i+1, 6)]
def omega(v):
    O = [[0]*6 for _ in range(6)]
    for k, (i, j) in enumerate(pairs): O[i][j] = v[k] % P; O[j][i] = (-v[k]) % P
    return O
def rows_for(L, mult):
    out = []
    for (r, s) in pairs:
        row = [(L[i][r]*L[j][s] - L[j][r]*L[i][s]) % P for (i, j) in pairs]
        k0 = pairs.index((r, s)); row[k0] = (row[k0] - mult) % P
        out.append(row)
    return out
best = 0; dims = {}
for mults in itertools.product((1, 4), repeat=3):
    rows = []
    for n, mu in zip("abc", mults): rows += rows_for(AFF[n][0], mu)
    _, basis = nullspace(rows, 15); dims[mults] = len(basis)
    for co in itertools.product(range(P), repeat=len(basis)):
        if any(co):
            v = [sum(c*b[k] for c, b in zip(co, basis)) % P for k in range(15)]
            best = max(best, nullspace(omega(v), 6)[0])
print("     dims of invariant alternating forms by multiplier (a,b,c):", dims)
check("2.1 no invariant alternating form on F_5^6 has rank above 2 (multipliers +1 or -1)", best == 2)
rows = []
for n in "abc": rows += rows_for(AFF[n][0], 1)
_, basis = nullspace(rows, 15)
allrows = []
for b in basis: allrows += omega(b)
_, rad = nullspace(allrows, 6)
kappa_ok = all(sum(v[:4]) % P == 0 and v[4] == 0 and v[5] == 0 for v in rad)
check("2.2 invariant forms span exactly Lambda^2 of (kappa,q,r); common radical is the 3-dim sum-zero piston", len(basis) == 3 and len(rad) == 3 and kappa_ok)

# ---------- Part 3: discrete Wigner function of one pentit ----------
# A(q,p)|k> = w^(2p(q-k)) |2q-k>, w = zeta_5. Monomial: (target index, exponent of w).
def A(q, p): return [((2*q - k) % P, (2*p*(q - k)) % P) for k in range(P)]
def mul(M, N): return [(M[N[k][0]][0], (M[N[k][0]][1] + N[k][1]) % P) for k in range(P)]
def inv(M):
    R = [None]*P
    for k in range(P): R[M[k][0]] = (k, (-M[k][1]) % P)
    return R
pts = list(itertools.product(range(P), repeat=2))
I5 = [(k, 0) for k in range(P)]
check("3.1 every phase-point operator is an involution with entries in mu_5", all(mul(A(*a), A(*a)) == I5 for a in pts))
check("3.2 conjugation by A(a) sends A(x) to A(2a-x) for all 625 pairs",
      all(mul(mul(A(*a), A(*x)), inv(A(*a))) == A((2*a[0]-x[0]) % P, (2*a[1]-x[1]) % P) for a in pts for x in pts))
# sum over all 25 operators equals 5*I: entry (j,k) = sum over (q,p) with 2q-k=j of w^(2p(q-k))
tot = {}
for (q, p) in pts:
    for k in range(P):
        j, e = A(q, p)[k]; tot.setdefault((j, k), [0]*P)[e] += 1
def cyc_to_q5(c):   # sum c_m w^m, real when c_m = c_{-m}; returns (x, y) meaning x + y*sqrt5
    assert c[1] == c[4] and c[2] == c[3]
    return (Fr(c[0]) - Fr(c[1] + c[2], 2), Fr(c[1] - c[2], 2))
check("3.3 the 25 phase-point operators sum to 5 times the identity",
      all(cyc_to_q5(tot[(j, k)]) == ((Fr(5), Fr(0)) if j == k else (Fr(0), Fr(0))) for j in range(P) for k in range(P)))
def sign_q5(x, y):  # sign of x + y*sqrt5, exact
    if y == 0: return (x > 0) - (x < 0)
    if x == 0: return (y > 0) - (y < 0)
    if (x > 0) == (y > 0): return 1 if x > 0 else -1
    return ((x*x > 5*y*y) - (x*x < 5*y*y)) * (1 if x > 0 else -1)
def wigner(psi):    # real vector psi (Fractions); returns dict point -> (x,y) in Q(sqrt5)
    n2 = sum(t*t for t in psi); W = {}
    for (q, p) in pts:
        c = [Fr(0)]*P
        for k in range(P):
            c[(2*p*(q - k)) % P] += psi[k]*psi[(2*q - k) % P]
        x, y = cyc_to_q5(c); W[(q, p)] = (x/(5*n2), y/(5*n2))
    return W
def negativity(W):
    sx = sy = Fr(0)
    for (x, y) in W.values():
        if sign_q5(x, y) < 0: sx -= x; sy -= y
    return sx, sy
W0 = wigner([Fr(1), Fr(0), Fr(0), Fr(0), Fr(0)])
check("3.4 basis state |0> is the uniform count 1/5 on the line q=0", all(W0[(q, p)] == ((Fr(1, 5), Fr(0)) if q == 0 else (Fr(0), Fr(0))) for (q, p) in pts))
u0 = [Fr(4), Fr(-1), Fr(-1), Fr(-1), Fr(-1)]          # QDD LOW direction: basis vector 0 projected off the uniform vector
Wu = wigner(u0)
neg = negativity(Wu)
print("     Wigner values of the LOW direction (x + y*sqrt5), multiset:", sorted({(str(x), str(y)) for (x, y) in Wu.values()}))
check("3.5 the LOW direction has negative Wigner entries; total negativity is exactly sqrt5/5", neg == (Fr(0), Fr(1, 5)))

# ---------- Part 4: all 624 QDD preparations ----------
ell = (0, 1, 2, -2, -1)
allneg = True; lowok = True; minneg = None
for pvec in itertools.product(range(P), repeat=4):
    if not any(pvec): continue
    v = [ell[t] for t in pvec]; s = sum(v); Q = sum(t*t for t in v)
    psi = [Fr(-s, 5)] + [Fr(t) - Fr(s, 5) for t in v]            # sum-zero embedding, coordinate 0 carries no source
    W = wigner(psi); nx, ny = negativity(W)
    allneg &= sign_q5(nx, ny) > 0
    if minneg is None or sign_q5(nx - minneg[0], ny - minneg[1]) < 0: minneg = (nx, ny)
    # LOW weight as phase-space overlap 5*sum W_psi*W_u0 must equal s^2/(4(5Q-s^2))
    ax = ay = Fr(0)
    for a in pts:
        (x1, y1), (x2, y2) = W[a], Wu[a]
        ax += x1*x2 + 5*y1*y2; ay += x1*y2 + x2*y1
    lowok &= (5*ax, 5*ay) == (Fr(s*s, 4*(5*Q - s*s)), Fr(0))
check("4.1 all 624 QDD preparations have strictly positive Wigner negativity (none is a stabilizer state)", allneg)
print("     least negativity over the 624 preparations (x + y*sqrt5):", str(minneg[0]), str(minneg[1]))
check("4.2 the signed phase-space overlap reproduces s^2/(4(5Q-s^2)) for all 624 preparations", lowok)

print("SUMMARY %d of %d checks PASS" % (sum(OK), len(OK)))
sys.exit(0 if all(OK) else 1)
