#!/usr/bin/env python3
"""Independent, result-exposed break attempt for C-V103-BRIDGE-SYNTHESIS-N.

Target: PR #1571 head 2a3250932553c1c36e88c48f0aa0d2f69f99f2b6, claim #1569.
Written from the Public Canon v102 definitions (native generators, field
marking, image criterion, contact section), not from any source verifier.
Python standard library only; exact integer arithmetic (int, Fraction); no
float anywhere. Every item prints PASS or FAIL; a FAIL is a candidate
counterexample. This is an audit script in a notes package, not a probe.
"""
from fractions import Fraction
from itertools import product

P = 5
FAILS = []

def report(name, ok, detail=""):
    tag = "PASS" if ok else "FAIL"
    print(f"{tag}  {name}" + (f"  [{detail}]" if detail else ""))
    if not ok:
        FAILS.append(name)

# ---------- exact matrix helpers ----------
def mat(rows): return [list(map(Fraction, r)) for r in rows]
def matmul(A, B):
    n, k, m = len(A), len(B), len(B[0])
    return [[sum(A[i][l]*B[l][j] for l in range(k)) for j in range(m)] for i in range(n)]
def matvec(A, v): return [sum(A[i][j]*v[j] for j in range(len(v))) for i in range(len(A))]
def transpose(A): return [list(r) for r in zip(*A)]
def ident(n): return [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]
def scal(c, A): return [[c*x for x in r] for r in A]
def madd(A, B): return [[a+b for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]
def msub(A, B): return [[a-b for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]
def meq(A, B): return all(a == b for ra, rb in zip(A, B) for a, b in zip(ra, rb))
def mpow(A, n):
    R = ident(len(A))
    for _ in range(n): R = matmul(R, A)
    return R
def det(A):
    A = [r[:] for r in A]; n = len(A); d = Fraction(1)
    for i in range(n):
        piv = next((r for r in range(i, n) if A[r][i] != 0), None)
        if piv is None: return Fraction(0)
        if piv != i: A[i], A[piv] = A[piv], A[i]; d = -d
        d *= A[i][i]
        for r in range(i+1, n):
            f = A[r][i]/A[i][i]
            for c in range(i, n): A[r][c] -= f*A[i][c]
    return d
def minors_positive(S):
    return all(det([r[:k] for r in S[:k]]) > 0 for k in range(1, len(S)+1))
def charpoly(A):
    # Faddeev-LeVerrier, exact; returns coefficients c[0..n] of X^n + c1 X^(n-1) + ...
    n = len(A); M = [[Fraction(0)]*n for _ in range(n)]; c = [Fraction(1)]
    I = ident(n)
    for k in range(1, n+1):
        M = madd(matmul(A, M), scal(c[-1], I))
        ck = -sum(matmul(A, M)[i][i] for i in range(n))/k
        c.append(ck)
    return c  # X^n + c[1] X^(n-1) + ... + c[n]
def polymul(a, b):
    r = [Fraction(0)]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): r[i+j] += x*y
    return r

# ---------- canonical data ----------
A_f = mat([[1,0,1,0],[0,1,0,1],[-2,1,-1,1],[1,-3,1,-2]])
B_f = mat([[4,-2,2,-1],[-2,6,-1,3],[2,-1,2,0],[-1,3,0,2]])
L   = mat([[1,-3,-1,-2],[-3,4,-2,1],[0,5,1,2],[5,-5,2,-1]])
V_inv = mat([[1,2,1,2],[2,-1,2,-1],[0,-5,1,-3],[-5,5,-3,4]])
I4 = ident(4)

def H(y):
    a, b, c, d = y
    return 2*a*a-2*a*b+3*b*b+c*c+d*d+2*a*c-a*d-b*c+3*b*d
def H_form(y):
    yv = list(map(Fraction, y)); return sum(yv[i]*B_f[i][j]*yv[j] for i in range(4) for j in range(4))/2
def Lint(u): return [int(x) for x in matvec(L, list(map(Fraction, u)))]
def mod5(v): return tuple(int(x) % P for x in v)

print("== A. field algebra (inherited identities, rechecked)")
report("H literal polynomial == y^t B_f y/2 on grid", all(H(y) == H_form(y) for y in product(range(-2, 3), repeat=4)))
report("A_f^5 = I", meq(mpow(A_f, 5), I4))
report("sum_j A_f^j = 0", meq(madd(madd(madd(madd(I4, A_f), mpow(A_f, 2)), mpow(A_f, 3)), mpow(A_f, 4)), scal(0, I4)))
report("A_f^t B_f A_f = B_f (H invariant)", meq(matmul(matmul(transpose(A_f), B_f), A_f), B_f))
report("L = (I-A_f)(I-A_f^2)", meq(L, matmul(msub(I4, A_f), msub(I4, mpow(A_f, 2)))))
report("det L = 25", det(L) == 25)
report("L^2 = 5 A_f^3", meq(mpow(L, 2), scal(5, mpow(A_f, 3))))
report("V_inv = A_f^2 L", meq(V_inv, matmul(mpow(A_f, 2), L)))
report("V_inv L = L V_inv = 5I", meq(matmul(V_inv, L), scal(5, I4)) and meq(matmul(L, V_inv), scal(5, I4)))
report("L^t B_f L = 5 B_f", meq(matmul(matmul(transpose(L), B_f), L), scal(5, B_f)))
report("B_f positive definite (Sylvester, exact)", minors_positive(B_f))
report("H(Lu) = 5 H(u) on grid", all(H(Lint(u)) == 5*H(u) for u in product(range(-2, 3), repeat=4)))

# image criterion and residue sets
G_L = {((3*s) % P, s, (3*t) % P, t) for s in range(P) for t in range(P)}
K = {(a, (3*a) % P, c, (3*c) % P) for a in range(P) for c in range(P)}
crit = {r for r in product(range(P), repeat=4) if (r[0]+2*r[1]) % P == 0 and (r[2]+2*r[3]) % P == 0}
imgL = {mod5(Lint(u)) for u in product(range(P), repeat=4)}
report("|G_L| = |K| = 25", len(G_L) == 25 and len(K) == 25)
report("image of L mod 5 == criterion set == G_L", imgL == crit == G_L)
def W(y): return (y[1], y[0], y[3], y[2])
report("W(K) = G_L", {W(k) for k in K} == G_L)
report("K != G_L as sets", K != G_L, f"|K cap G_L|={len(K & G_L)}")
# kernel lemma over residues: Lu = 0 mod 5 iff u mod 5 in G_L (i.e. u in L Z^4)
kerL = {u for u in product(range(P), repeat=4) if mod5(Lint(u)) == (0, 0, 0, 0)}
report("ker(L mod 5) == G_L (so ker pi_L = L Z^4)", kerL == G_L)
# A_f on G_L as shear (s,t)->(s+t,t)
def Afmod(r): return mod5(matvec(A_f, list(map(Fraction, r))))
report("A_f acts on G_L by (s,t)->(s+t,t)", all(Afmod(((3*s) % P, s, (3*t) % P, t)) == ((3*(s+t)) % P, (s+t) % P, (3*t) % P, t) for s in range(P) for t in range(P)))
fixed = {r for r in G_L if Afmod(r) == r}
report("A_f-fixed subgroup of G_L = {(3s,s,0,0)}", fixed == {((3*s) % P, s, 0, 0) for s in range(P)}, f"{sorted(fixed)}")

print("== B. unit shell H=1")
# polynomial identities on grid {0,1,2}^4 (degree-2 identities are determined there)
def Q(a, b): return 3*a*a+2*a*b+2*b*b
grid = list(product(range(0, 3), repeat=4))
report("4H = Q + (2c+2a-b)^2 + (2d-a+3b)^2 identically", all(4*H((a,b,c,d)) == Q(a,b)+(2*c+2*a-b)**2+(2*d-a+3*b)**2 for a,b,c,d in grid))
report("2Q = 5a^2 + (a+2b)^2 ; 3Q = 5b^2 + (3a+b)^2", all(2*Q(a,b) == 5*a*a+(a+2*b)**2 and 3*Q(a,b) == 5*b*b+(3*a+b)**2 for a,b,_,_ in grid))
# B's own four-square identity, as quoted in ACCEPTANCE RB4 (independent bound route)
report("4H = (2a-2b+c-d)^2+(2a+c)^2+2(2b+d)^2+c^2+(c+d)^2 identically", all(4*H((a,b,c,d)) == (2*a-2*b+c-d)**2+(2*a+c)**2+2*(2*b+d)**2+c*c+(c+d)**2 for a,b,c,d in grid))
# bound from the first identity: |a|,|b|<=1, |c|<=2, |d|<=3 ; from the second: |a|,|b|,|c|<=2, |d|<=4
BOX = 6
units = [u for u in product(range(-BOX, BOX+1), repeat=4) if H(u) == 1]
report("|U1| = 20 (box +-6, both derived boxes inside)", len(units) == 20, f"{len(units)}")
report("all units satisfy |a|,|b|<=1,|c|<=2,|d|<=3 and |a|,|b|,|c|<=2,|d|<=4", all(abs(a)<=1 and abs(b)<=1 and abs(c)<=2 and abs(d)<=3 for a,b,c,d in units))
fib = {}
for a,b,c,d in units: fib[(a,b)] = fib.get((a,b), 0)+1
report("fibers 4+8+4+4, none at +-(1,1)", fib.get((0,0),0)==4 and fib.get((0,1),0)+fib.get((0,-1),0)==8 and fib.get((1,0),0)+fib.get((-1,0),0)==4 and fib.get((1,-1),0)+fib.get((-1,1),0)==4 and fib.get((1,1),0)==0 and fib.get((-1,-1),0)==0, f"{sorted(fib.items())}")
# H integer-valued positive definite => H(u) >= 1 for u != 0 ; check no nonzero u with H<=0 in a box as sanity
report("no nonzero u in box with H(u) <= 0", all(H(u) >= 1 for u in product(range(-BOX, BOX+1), repeat=4) if any(u)))

print("== C. residue classification 20 + 5")
piL = {u: mod5(Lint(u)) for u in units}
report("pi_L injective on U1", len(set(piL.values())) == 20)
report("image(pi_L) subset G_L", set(piL.values()) <= G_L)
report("image(pi_L) == G_L minus fixed subgroup", set(piL.values()) == G_L - fixed)
report("no unit hits any of the five fixed residues (brute)", not any(r in fixed for r in piL.values()))
# independent check of the energy-kernel argument: difference of two distinct units never in L Z^4
report("u-v (distinct units) never in L Z^4", all(mod5(tuple(x-y for x,y in zip(u,v))) not in G_L for u in units for v in units if u != v))
report("A_f u - u never in L Z^4 for a unit", all(mod5(tuple(int(x)-y for x,y in zip(matvec(A_f, list(map(Fraction,u))), u))) not in G_L for u in units))

print("== D. native dynamics")
def g0(x): a,b,c,d,q,r = x; return (b,a,d,c,q,r)
def g1(x): a,b,c,d,q,r = x; return (-c,-d,-a,-b,-q,-r)
def g2(x): a,b,c,d,q,r = x; return (2-c,1-d+r,2-a,1-b-r,1-q,-r)
def g3(x): a,b,c,d,q,r = x; return (2-a,1-b,3-c,4-d,1-q,1-r)
def g4(x): a,b,c,d,q,r = x; return (2-a,1-b,3-c,4-d,2-q,1-r)
G = [g0,g1,g2,g3,g4]
def z(x): return sum(x) % P
def step(x, t): return mod5(G[(z(x)+2*t) % P](x))
def theta(n): return bin(n).count("1") % 2
def orbit(x0, N):
    xs = [mod5(x0)]
    for n in range(N): xs.append(step(xs[-1], theta(n)))
    return xs
def h(x): a,b,c,d,q,r = x; return ((b+2*a) % P, (d+2*c) % P)
def piP(x): return x[:4]
ALL = list(product(range(P), repeat=6))
report("each g_j is an involution on F5^6", all(mod5(g(mod5(g(x)))) == x for g in G for x in ALL))
J2 = lambda hh: (hh[1], hh[0])
neg = lambda hh: ((-hh[0]) % P, (-hh[1]) % P)
report("h(g0 x) = 2h(x) + 2(a,c)", all(h(mod5(g0(x))) == ((2*h(x)[0]+2*x[0]) % P, (2*h(x)[1]+2*x[2]) % P) for x in ALL))
report("h(g1 x) = -J2 h(x)", all(h(mod5(g1(x))) == neg(J2(h(x))) for x in ALL))
report("h(g2 x) = -J2 h(x) + (r,-r)", all(h(mod5(g2(x))) == ((-h(x)[1]+x[5]) % P, (-h(x)[0]-x[5]) % P) for x in ALL))
report("h(g3 x) = h(g4 x) = -h(x)", all(h(mod5(g3(x))) == neg(h(x)) == h(mod5(g4(x))) for x in ALL))
# no h-only law for g0
pairs = {}
for p4 in product(range(P), repeat=4):
    x = p4 + (0, 0)
    pairs.setdefault(h(x), set()).add(h(mod5(g0(x))))
report("no h-only law for g0 (some h value has >1 successor)", any(len(v) > 1 for v in pairs.values()))
report("p -> (h(p), h(g0 p)) bijective on F5^4", len({(h(p+(0,0)), h(mod5(g0(p+(0,0))))) for p in product(range(P), repeat=4)}) == 625)
G0 = {x for x in ALL if h(x) == (0, 0)}
report("|G0| = 625 and G0 = pi_P^-1(K)", len(G0) == 625 and all(piP(x) in K for x in G0))
report("h(x)=0 iff W pi_P(x) in G_L (gate-to-shell bridge)", all((h(x) == (0,0)) == (W(piP(x)) in G_L) for x in ALL))
X14 = {x for x in ALL if z(x) in (1, 4)}
report("|X14| = 6250", len(X14) == 6250)
report("selection on X14 uses only g1,g3,g4", {(z(x)+2*t) % P for x in X14 for t in (0, 1)} == {1, 3, 4})
D = G0 & X14
report("|G0 cap X14| = 250", len(D) == 250)
for t in (0, 1):
    img = {step(x, t) for x in D}
    target = {x for x in G0 if z(x) == (4+2*t) % P}
    pre = {}
    for x in D: pre.setdefault(step(x, t), 0); pre[step(x, t)] += 1
    report(f"T_{t}(G0 cap X14) = G0 cap X_{(4+2*t)%P}, |image|=125, each 2 preimages", img == target and len(img) == 125 and set(pre.values()) == {2})
    fixedpts = [x for x in D if step(x, t) == x]
    report(f"T_{t} fixes exactly one point of G0 cap X14", len(fixedpts) == 1, f"{fixedpts}")
    report(f"T_{t} preserves zero and nonzero h on X14", all((h(step(x,t)) == (0,0)) == (h(x) == (0,0)) for x in X14))
# zero orbit
zo = orbit((0,0,0,0,0,0), 1 << 16)
report("x0=x1=0, x2=(2,1,2,1,1,0), x3=(0,0,1,3,1,1)", zo[0] == zo[1] == (0,0,0,0,0,0) and zo[2] == (2,1,2,1,1,0) and zo[3] == (0,0,1,3,1,1), f"{zo[:5]}")
report("x4 = (4,2,0,0,4,4) via g1 (theta3=0, z3=1)", zo[4] == (4,2,0,0,4,4) and theta(3) == 0 and z(zo[3]) == 1)
report("h(x_n) = 0 for all n <= 2^16 on zero orbit (finite witness)", all(h(x) == (0,0) for x in zo))
report("x_n in X14 for all 3 <= n <= 2^16", all(z(x) in (1,4) for x in zo[3:]))
rho3 = W(piP(zo[3])); rho4 = W(piP(zo[4]))
report("rho3 = (0,0,3,1) in G_L minus fixed", rho3 == (0,0,3,1) and rho3 in G_L and rho3 not in fixed)
report("rho4 = (2,4,0,0) in fixed subgroup (no unit preimage)", rho4 == (2,4,0,0) and rho4 in fixed and rho4 not in set(piL.values()))
# which boundaries n<=2^16 have residues with no unit preimage?
nounit = [n for n, x in enumerate(zo) if n >= 3 and W(piP(x)) in fixed]
report("boundary 4 is the first n>=3 with residue in fixed subgroup", nounit[:1] == [4], f"first few: {nounit[:8]}, count<=2^16: {len(nounit)}")
# 3-step synchronization
img3 = {}
for x0 in ALL:
    x3 = step(step(step(x0, 0), 1), 1)
    img3.setdefault(z(x0), set()).add(x3)
report("each initial sheet X_s maps onto X_1 bijectively (3 steps, bits 0,1,1)", all(len(v) == 3125 and all(z(x) == 1 for x in v) for v in img3.values()))
gated0 = [x0 for x0 in ALL if h(step(step(step(x0, 0), 1), 1)) == (0,0)]
report("625 initial checkpoints gated at boundary 3; 125 distinct gated targets", len(gated0) == 625 and len({step(step(step(x0,0),1),1) for x0 in gated0}) == 125)

print("== E. coset minimum at boundary 3")
cands = [y for y in product(range(-BOX, BOX+1), repeat=4) if mod5(y) == rho3 and mod5(y) in G_L]
# y in L Z^4 iff residue in G_L (proved above); so these are coset points in the box
Hs = sorted((H(y), y) for y in cands)
report("min H over coset box = 5, unique argmin (0,0,-2,1)", Hs[0][0] == 5 and Hs[1][0] > 5 and Hs[0][1] == (0,0,-2,1), f"{Hs[:3]}")
ustar = (0,-1,-1,2)
report("L u* = (0,0,-2,1), H(u*)=1, H(y*)=5", Lint(ustar) == [0,0,-2,1] and H(ustar) == 1 and H((0,0,-2,1)) == 5)
report("V_inv y* / 5 = u* (unique integer preimage)", [Fraction(v, 5) for v in matvec(V_inv, list(map(Fraction,(0,0,-2,1))))] == list(map(Fraction, ustar)))
report("u* is the unique unit with residue rho3", [u for u in units if piL[u] == rho3] == [ustar])
# RB9 arithmetic
report("RB9: displayed expansion equals 4, correct H(u*)=3+1+4-1-6=1", (3*(-1)**2+(-1)**2+2**2-(-1)*2+3*(-1)*2) == 4 and 3+1+4-1-6 == 1 == H(ustar))
report("RB3: (L^t L/5)[0,0] = 7 != B_f[0,0]=4", matmul(transpose(L), L)[0][0]/5 == 7 and B_f[0][0] == 4)
u0 = (0,0,1,0); v0 = [int(a+b) for a,b in zip(u0, matvec(A_f, list(map(Fraction,u0))))]
report("RB8: (I+A_f)(0,0,1,0)=(1,0,0,1) with H=2, not 3", v0 == [1,0,0,1] and H(v0) == 2)
report("RB1: H(e0)=2 (literal first basis vector)", H((1,0,0,0)) == 2)

print("== F. W is not an isometry")
report("H(Wy)-H(y) = a^2-b^2+ac-bd identically", all(H(W((a,b,c,d)))-H((a,b,c,d)) == a*a-b*b+a*c-b*d for a,b,c,d in grid))
report("H(e0)=2, H(W e0)=3", H((1,0,0,0)) == 2 and H(W((1,0,0,0))) == 3)

print("== G. message families (section 4)")
def chart_to_x(Aa, Bb, Cc, Dd, q, r):
    # A=a+c, B=b+d, C=a-c-2, D=b-d-1  (mod 5; inverse of 2 is 3)
    a = (3*(Aa+Cc+2)) % P; c = (Aa-a) % P
    b = (3*(Bb+Dd+1)) % P; d = (Bb-b) % P
    return (a,b,c,d,q % P,r % P)
def x_to_chart(x):
    a,b,c,d,q,r = x
    return ((a+c) % P, (b+d) % P, (a-c-2) % P, (b-d-1) % P)
report("chart inverse consistent", all(x_to_chart(chart_to_x(A_,B_,C_,D_,0,0)) == (A_,B_,C_,D_) for A_,B_,C_,D_ in product(range(P), repeat=4)))
report("h1+h2 = 2A+B and h1-h2 = 2C+D identically", all(((h(x)[0]+h(x)[1]) % P == (2*x_to_chart(x)[0]+x_to_chart(x)[1]) % P) and ((h(x)[0]-h(x)[1]) % P == (2*x_to_chart(x)[2]+x_to_chart(x)[3]) % P) for x in ALL))
report("h1 = B+2A is FALSE in general (refuted literal clause)", not all(h(x)[0] == (x_to_chart(x)[1]+2*x_to_chart(x)[0]) % P for x in ALL))
N = 1 << 13
# original family
ok_prefix = ok_nogate = ok_prefix_eq = ok_support = ok_tailparam = True
tails = {}; supports = {}
quot_hist = {}
for lam, mu in product(range(P), repeat=2):
    x0 = chart_to_x(1, 0, lam, mu, 0, 1)
    xs = orbit(x0, N); k = (lam+3*mu) % P
    exp = [((1+k)%P,(1-k)%P), (k%P,(3-k)%P), ((1+k)%P,(1-k)%P), ((-1-k)%P,(-1+k)%P)]
    if [h(x) for x in xs[:4]] != exp: ok_prefix = False
    if xs[2] != xs[0] or z(x0) != 2: ok_prefix_eq = False
    if any(h(x) == (0,0) for x in xs): ok_nogate = False
    tail = set(xs[3:]); tails[(lam,mu)] = tail; supports[(lam,mu)] = set(xs)
    if len(tail) != 20 or len(set(xs)) != 22: ok_support = False
    for x in xs[3:]:
        A_,B_,C_,D_ = x_to_chart(x); s = A_; zz = z(x)
        if s not in (1,4) or zz not in (1,4) or B_ != 0 or C_ != (s*zz*lam) % P or D_ != (s*zz*mu) % P or x[5] != (zz-s-x[4]) % P: ok_tailparam = False
        if h(x) != ((s*(1+zz*k)) % P, (s*(1-zz*k)) % P): ok_tailparam = False
    quot_hist[(lam,mu)] = [(z(x), x[4], x[5]) for x in xs]
report("original: prefix gate values (1+k,1-k),(k,3-k),(1+k,1-k),(-1-k,-1+k)", ok_prefix)
report("original: x2 = x0 (g2 involution), z0 = 2", ok_prefix_eq)
report("original: no gate point on any of 25 orbits up to n=2^13", ok_nogate)
report("original: each orbit support 22 = 2 prefix + 20 tail (n<=2^13)", ok_support)
alltails = set().union(*tails.values())
report("original: 25 tails pairwise disjoint, total support 550", len(alltails) == 500 and len(set().union(*supports.values())) == 550)
report("original: tail parameters s,z in {1,-1}, B=0, C=sz lam, D=sz mu, r=z-s-q, h=s(1+zk,1-zk)", ok_tailparam)
report("original: all 25 quotient (z,q,r) histories identical (n<=2^13)", len({tuple(v) for v in quot_hist.values()}) == 1)
# fixed-time piston distinguishability vs h distinguishes only k
ok_dist = True; ok_hk = True
for n in range(0, 64):
    pist = {(lam,mu): piP(orbit(chart_to_x(1,0,lam,mu,0,1), n)[n]) for lam,mu in product(range(P), repeat=2)}
    if len(set(pist.values())) != 25: ok_dist = False
    hv = {(lam,mu): h(orbit(chart_to_x(1,0,lam,mu,0,1), n)[n]) for lam,mu in product(range(P), repeat=2)}
    if len(set(hv.values())) != 5: ok_hk = False
report("original: full piston distinguishes all 25 pairs at each fixed n<64; h distinguishes exactly 5 values", ok_dist and ok_hk)
# alternative family
ok_prefix = True; gate_pts = []; ok_support = True; ok_tail = True; ok_ctrl = True
alt_tails = {}; alt_supp = {}
for lam, mu in product(range(P), repeat=2):
    t = (3*(1+mu-lam)) % P
    x0 = chart_to_x(mu, 0, 3, 0, 2-mu-t, t)
    if x0[4] != (3*lam+mu+4) % P or x0[5] != (2*lam+3*mu+3) % P: ok_ctrl = False
    xs = orbit(x0, N)
    exp = [((mu+3)%P,(mu-3)%P), ((-mu+3+t)%P,(-mu-3-t)%P), ((mu+3)%P,(mu-3)%P), ((-mu+2)%P,(-mu-2)%P)]
    if [h(x) for x in xs[:4]] != exp: ok_prefix = False
    for n, x in enumerate(xs):
        if h(x) == (0,0): gate_pts.append((lam,mu,n,x))
    tail = set(xs[3:]); alt_tails[(lam,mu)] = tail; alt_supp[(lam,mu)] = set(xs)
    if len(set(xs)) != len(tail)+2 or xs[2] != xs[0]: ok_support = False
    for x in xs[3:]:
        A_,B_,C_,D_ = x_to_chart(x); zz = z(x)
        if C_ not in (2,3) or zz not in (1,4) or B_ != 0 or D_ != 0 or A_ != (2*C_*zz*mu) % P: ok_tail = False
        if h(x) != ((C_*(2*zz*mu+1)) % P, (C_*(2*zz*mu-1)) % P): ok_tail = False
report("alternative: q0=3lam+mu+4, r0=2lam+3mu+3", ok_ctrl)
report("alternative: prefix gate values as stated", ok_prefix)
report("alternative: exactly one gate point, (lam,mu)=(2,0) at n=1, checkpoint (2,1,2,1,1,3)", gate_pts == [(2,0,1,(2,1,2,1,1,3))], f"{gate_pts}")
report("alternative: support = prefix 2 + tail, x2=x0", ok_support)
report("alternative: total support 150 = 100 tail + 50 prefix (n<=2^13)", len(set().union(*alt_tails.values())) == 100 and len(set().union(*alt_supp.values())) == 150, f"tail={len(set().union(*alt_tails.values()))} supp={len(set().union(*alt_supp.values()))}")
report("alternative: tail C in {2,3}, z in {1,4}, B=D=0, A=2Cz mu, h=C(2z mu+1, 2z mu-1)", ok_tail)
report("alternative: initial (q0,r0) distinguishes all 25 pairs (det 2)", len({chart_to_x(mu,0,3,0,2-mu-(3*(1+mu-lam))%P,(3*(1+mu-lam))%P)[4:] for lam,mu in product(range(P),repeat=2)}) == 25)
# one-shot occupied
ok_pre = True; ok_gate = True; quot = {}; ok_graph = True; ok_payload = True
graph = set()
for B_ in (2,3):
    for zz in (1,4):
        for D_ in range(P):
            for r in range(P):
                a = (1+B_+2*B_*zz) % P; c = (-1+B_-2*B_*zz) % P
                b = (3*(B_+D_+1)) % P; d = (3*(B_-D_-1)) % P; q = (zz-3*B_-r) % P
                graph.add((a,b,c,d,q,r))
report("one-shot ready graph has 100 states", len(graph) == 100)
report("one-shot graph: exactly 20 states with h=0, all with lam=3-BzD=0", sum(1 for x in graph if h(x) == (0,0)) == 20)
for lam in range(P):
    xs = orbit((lam,0,(-lam)%P,0,0,0), N)
    if h(xs[0]) != ((2*lam)%P,(-2*lam)%P) or h(xs[1]) != (lam,(-lam)%P) or h(xs[2]) != (lam,(-lam)%P): ok_pre = False
    for n, x in enumerate(xs):
        if (h(x) == (0,0)) != (lam == 0): ok_gate = False
    for x in xs[3:]:
        if x not in graph: ok_graph = False
        # payload read lam=3-BzD on tail
        A_,B_,C_,D_ = x_to_chart(x); zz = z(x)
        if (3-B_*zz*D_) % P != lam: ok_payload = False
        if h(x) != ((-2*B_*zz*lam) % P, (2*B_*zz*lam) % P): ok_pre = False
    quot[lam] = [(z(x), x[4], x[5]) for x in xs]
report("one-shot: prefix h = (2lam,-2lam),(lam,-lam),(lam,-lam); tail h=(-2Bz lam, 2Bz lam)", ok_pre)
report("one-shot: gate iff lam=0 at every n<=2^13", ok_gate)
report("one-shot: all tail states lie in the 100-state graph; payload 3-BzD reads lam", ok_graph and ok_payload)
report("one-shot: five occupied quotient histories identical", len({tuple(v) for v in quot.values()}) == 1)
xe = orbit((0,0,1,0,0,0), N)
report("absence: never passes gate, h1+h2 != 0 at every n<=2^13", all(h(x) != (0,0) and (h(x)[0]+h(x)[1]) % P != 0 for x in xe))
qe = [(z(x), x[4], x[5]) for x in xe]
report("absence vs occupied: controls differ at n=2 ((0,0) vs (1,0)), agree for n>=3 (n<=2^13)", (xe[2][4],xe[2][5]) == (0,0) and (orbit((0,0,0,0,0,0),3)[2][4], orbit((0,0,0,0,0,0),3)[2][5]) == (1,0) and qe[3:] == quot[0][3:] and qe[2] != quot[0][2], f"abs q2={qe[2]} occ q2={quot[0][2]}")
# quotient generator restrictions
def quotg(gx, x): return (z(mod5(gx)), mod5(gx)[4], mod5(gx)[5])
report("quotient restrictions (z,q,r),(-z,-q,-r),(2-z,1-q,-r),(2-z,1-q,1-r),(3-z,2-q,1-r)", all(
    quotg(g0(x),x) == (z(x), x[4], x[5]) and quotg(g1(x),x) == ((-z(x))%P, (-x[4])%P, (-x[5])%P) and
    quotg(g2(x),x) == ((2-z(x))%P, (1-x[4])%P, (-x[5])%P) and quotg(g3(x),x) == ((2-z(x))%P, (1-x[4])%P, (1-x[5])%P) and
    quotg(g4(x),x) == ((3-z(x))%P, (2-x[4])%P, (1-x[5])%P) for x in ALL))
report("original family all start at Q=(2,0,1)", all((z(chart_to_x(1,0,lam,mu,0,1)), 0, 1) == (2,0,1) for lam,mu in product(range(P),repeat=2)))

print("== H. optional five-cell census (section 7)")
def A_G_of(Gm):
    m = len(Gm); Gm = mat(Gm); Im = ident(m)
    top = [Im[i] + Im[i] for i in range(m)]
    bot = [[-Gm[i][j] for j in range(m)] + [Im[i][j]-Gm[i][j] for j in range(m)] for i in range(m)]
    return top + bot
def order(A, cap=60):
    n = len(A); R = ident(n)
    for k in range(1, cap+1):
        R = matmul(R, A)
        if meq(R, ident(n)): return k
    return None
def form_matrix(Gm):
    m = len(Gm); Gm = mat(Gm); Im = ident(m)
    S = [[Fraction(0)]*(2*m) for _ in range(2*m)]
    for i in range(m):
        for j in range(m):
            S[i][j] = Gm[i][j]; S[i][m+j] = Gm[i][j]/2; S[m+i][j] = Gm[j][i]/2; S[m+i][m+j] = Im[i][j]
    return S
cells = [([[2]], [1,0,1], 4), ([[3]], [1,1,1], 3), ([[2,1],[1,2]], [1,0,1,0,1], 6), ([[2,1],[1,3]], [1,1,1,1,1], 5), ([[3,1],[1,3]], None, None)]
for Gm, cp, od in cells:
    A = A_G_of(Gm); c = charpoly(A)
    # formula det(X^2 I + (G-2I)X + I) : compare numerically at X=0..5 against charpoly
    m = len(Gm); Gq = mat(Gm)
    formula_ok = all(sum(c[i]*Fraction(X)**(len(c)-1-i) for i in range(len(c))) == det(madd(madd(scal(Fraction(X)**2, ident(m)), scal(Fraction(X), msub(Gq, scal(2, ident(m))))), ident(m))) for X in range(6))
    S = form_matrix(Gm); pd = minors_positive(S)
    o = order(A)
    if cp is not None:
        report(f"cell G={Gm}: charpoly {cp}, order {od}, positive definite", [int(x) for x in c] == cp and o == od and pd and formula_ok, f"got {[int(x) for x in c]} order={o} pd={pd}")
    else:
        # (X^2+1)(X+1)^2 = X^4+2X^3+2X^2+2X+1
        exp = polymul([1,0,1],[1,2,1])
        psd = all(det([r[:k] for r in S[:k]]) >= 0 for k in range(1, 5)) and det(S) == 0
        # nullity via rank of 2S (integer)
        M = [[2*x for x in r] for r in S]; rank = 0; Mm = [r[:] for r in M]; rows = len(Mm); cols = len(Mm[0]); rr = 0
        for cidx in range(cols):
            piv = next((r for r in range(rr, rows) if Mm[r][cidx] != 0), None)
            if piv is None: continue
            Mm[rr], Mm[piv] = Mm[piv], Mm[rr]
            for r in range(rows):
                if r != rr and Mm[r][cidx] != 0:
                    f = Mm[r][cidx]/Mm[rr][cidx]
                    Mm[r] = [x - f*y for x,y in zip(Mm[r], Mm[rr])]
            rr += 1
        report(f"cell G={Gm}: charpoly (X^2+1)(X+1)^2, infinite order (cap 60), psd nullity 1", [int(x) for x in c] == [int(x) for x in exp] and o is None and psd and (4-rr) == 1 and formula_ok, f"got {[int(x) for x in c]} order={o} rank={rr}")
        v = list(map(Fraction,(1,1,-2,-2))); w = list(map(Fraction,(0,0,1,1)))
        Ap = madd(A, ident(4))
        jc = matvec(Ap, v) == [0]*4 and matvec(Ap, w) == v
        pw = all(matvec(mpow(A, n), w) == [((-1)**n)*(wi - n*vi) for wi, vi in zip(w, v)] for n in range(0, 12))
        report("Jordan chain (A+I)v=0, (A+I)w=v, A^n w = (-1)^n (w - n v) for n<12", jc and pw)
report("mixed cell face reversal G=[[2,-1],[-1,3]] gives A_G = A_f", meq(A_G_of([[2,-1],[-1,3]]), A_f))

print()
print("FAILS:", FAILS if FAILS else "none")
