#!/usr/bin/env python3
"""Independent arithmetic audit of a NON-CANONICAL L1 Hodge first-order note.

Only Python standard library, exact integers, Fraction, and F5 arithmetic.
The statements were known before this script: it is NOT a blind breaker and
NOT a formally pinned public probe. No external files or system effects.
"""
from fractions import Fraction as Q
from itertools import product

P = 5
PAIRS = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))


def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def mv(a, v):
    return [sum(x * v[k] for k, x in enumerate(row)) for row in a]


def tr(a):
    return [list(row) for row in zip(*a)]


def ident(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def residues(a):
    return [[x % P for x in row] for row in a]


def rref(a):
    a = residues(a)
    row = 0
    pivots = []
    for j in range(len(a[0]) if a else 0):
        k = next((i for i in range(row, len(a)) if a[i][j]), None)
        if k is None:
            continue
        a[row], a[k] = a[k], a[row]
        inv = pow(a[row][j], -1, P)
        a[row] = [(x * inv) % P for x in a[row]]
        for i in range(len(a)):
            if i != row:
                c = a[i][j]
                a[i] = [(a[i][t] - c * a[row][t]) % P
                        for t in range(len(a[0]))]
        pivots.append(j)
        row += 1
        if row == len(a):
            break
    return a, pivots


def rank(a):
    return len(rref(a)[1])


def null_basis(a):
    r, pivots = rref(a)
    out = []
    for f in (j for j in range(len(a[0])) if j not in pivots):
        v = [0] * len(a[0])
        v[f] = 1
        for i, j in enumerate(pivots):
            v[j] = -r[i][f] % P
        out.append(v)
    return out


def solve(a, b):
    r, pivots = rref([row + [b[i]] for i, row in enumerate(a)])
    n = len(a[0])
    assert all(j < n for j in pivots), 'not in column space'
    out = [0] * n
    for i, j in enumerate(pivots):
        out[j] = r[i][n]
    assert [x % P for x in mv(a, out)] == [x % P for x in b]
    return out


def inv(a):
    return tr([solve(a, e) for e in ident(len(a))])


def det3(a):
    return (a[0][0] * (a[1][1]*a[2][2] - a[1][2]*a[2][1])
          - a[0][1] * (a[1][0]*a[2][2] - a[1][2]*a[2][0])
          + a[0][2] * (a[1][0]*a[2][1] - a[1][1]*a[2][0])) % P


def wedge(a, b):
    return [(a[i]*b[j] - a[j]*b[i]) % P for i, j in PAIRS]


def qcoords(v):
    return [(v[i] - v[3]) % P for i in range(3)]


def perm_a4(perm):
    a = [[0]*4 for _ in range(4)]
    for col, j in enumerate(range(1, 5)):
        if perm[j]:
            a[perm[j] - 1][col] += 1
        if perm[0]:
            a[perm[0] - 1][col] -= 1
    return a


def compound2(a):
    return [[a[k][i]*a[l][j] - a[l][i]*a[k][j]
             for i, j in PAIRS] for k, l in PAIRS]


def signq(x):
    return (x > 0) - (x < 0)


class F:
    """Exact a+b sqrt(5) in Q(sqrt5)."""
    def __init__(self, a=0, b=0):
        if isinstance(a, F):
            self.a, self.b = a.a, a.b
        else:
            self.a, self.b = Q(a), Q(b)

    def __add__(self, rhs):
        rhs = F(rhs)
        return F(self.a + rhs.a, self.b + rhs.b)
    __radd__ = __add__

    def __neg__(self):
        return F(-self.a, -self.b)

    def __sub__(self, rhs):
        return self + (-F(rhs))

    def __rsub__(self, rhs):
        return F(rhs) - self

    def __mul__(self, rhs):
        rhs = F(rhs)
        return F(self.a*rhs.a + 5*self.b*rhs.b,
                 self.a*rhs.b + self.b*rhs.a)
    __rmul__ = __mul__

    def conj(self):
        return F(self.a, -self.b)

    def inverse(self):
        n = self.a*self.a - 5*self.b*self.b
        assert n != 0
        return F(self.a/n, -self.b/n)

    def __truediv__(self, rhs):
        return self*F(rhs).inverse()

    def __pow__(self, n):
        if n < 0:
            return self.inverse() ** (-n)
        ans, val = F(1), self
        while n:
            if n & 1:
                ans = ans*val
            val = val*val
            n //= 2
        return ans

    def __eq__(self, rhs):
        rhs = F(rhs)
        return (self.a, self.b) == (rhs.a, rhs.b)

    def sign(self):
        a, b = self.a, self.b
        if a == 0:
            return signq(b)
        if b == 0 or signq(a) == signq(b):
            return signq(a)
        comp = a*a - 5*b*b
        assert comp != 0  # 5 is nonsquare in Q
        return signq(a) if comp > 0 else signq(b)

    def residue(self):
        assert self.a.denominator % P != 0 and self.b.denominator % P != 0
        return (self.a.numerator * pow(self.a.denominator, -1, P)) % P


def det_f(a):
    assert len(a) == 3
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
            - a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
            + a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))


def is_positive_definite(a):
    p1 = a[0][0]
    p2 = a[0][0]*a[1][1] - a[0][1]*a[1][0]
    p3 = det_f(a)
    return p1.sign() > 0 and p2.sign() > 0 and p3.sign() > 0


# Canonical marked A4 forms, not copied target matrices.
H = [[1 + int(i == j) for j in range(4)] for i in range(4)]
C = [[-1, -1, -1, -1], [1, 0, 0, 0],
     [0, 1, 0, 0], [0, 0, 1, 0]]
C2 = mm(C, C)
M = [[int(i == j) + C2[i][j] for j in range(4)] for i in range(4)]
G2 = [[H[i][k]*H[j][l]-H[i][l]*H[j][k]
       for k, l in PAIRS] for i, j in PAIRS]
W = [[0]*6 for _ in range(6)]
for a, ij in enumerate(PAIRS):
    for b, kl in enumerate(PAIRS):
        ix = ij + kl
        if len(set(ix)) == 4:
            W[a][b] = (-1)**sum(ix[i] > ix[j]
                                   for i in range(4) for j in range(i+1, 4))
K = mm(W, G2)
assert mm(K, K) == [[5*x for x in row] for row in ident(6)]
assert all(W[i][j] == W[j][i] for i in range(6) for j in range(6))
L = compound2(M)
assert mm(mm(tr(L), W), L) == W
print('01 PASS: marked A4, integral K^2=5I, L preserves unimodular wedge pairing')

Kb = residues(K)
assert rank(Kb) == 3 and rank(residues(mm(Kb, Kb))) == 0
ell = [1]*4
E = tr([wedge(ell, e) for e in ident(4)])
assert rank(E) == 3
assert residues(mm(Kb, E)) == [[0]*4 for _ in range(6)]
Bmat = [[1, 0, 0], [4, 1, 0], [0, 4, 1], [0, 0, 4]]
Bpub = residues(mm(tr(Bmat), Bmat))
assert Bpub == [[2, 4, 0], [4, 2, 4], [0, 4, 2]]
assert det3(Bpub) == 4
Hb = residues(H)
Qcols = [[int(i == j) for i in range(4)] for j in range(3)]
T = tr([solve(Bmat, mv(Hb, col)) for col in Qcols])
assert det3(T) != 0
Gq = residues(mm(mm(tr(tr(Qcols)), Hb), tr(Qcols)))
assert residues(mm(mm(tr(T), Bpub), T)) == Gq
print('02 PASS: ramified Hodge image and exact quotient isometry to W5')

# Select the first independent columns of the *reconstructed* Kbar.
_, src = rref(Kb)
assert len(src) == 3
coords = []
for i in src:
    v = solve(E, [Kb[row][i] for row in range(6)])
    coords.append(mv(T, qcoords(v)))
coord = residues(tr(coords))
assert det3(coord) != 0
Bpull = residues(mm(mm(tr(coord), Bpub), coord))
hp = residues([[2*G2[i][j] for j in src] for i in src])
hm = residues([[-2*G2[i][j] for j in src] for i in src])
assert hp == residues([[3*x for x in row] for row in Bpull])
assert hm == residues([[-3*x for x in row] for row in Bpull])
assert det3(Bpull) == 4 and det3(hp) == 3
print('03 PASS: first-order restriction h_plus=3*g5, h_minus=-3*g5, square classes differ')

s = F(0, 1)
# Full field identity, not a formula copied into a comment.
for eta in (1, -1):
    A = [[F(K[i][j]) + eta*s*int(i == j) for j in range(6)]
         for i in range(6)]
    left = mm(mm(tr(A), [[F(x) for x in row] for row in W]), A)
    right = [[eta*2*s*(F(G2[i][j]) + eta*s*W[i][j])
              for j in range(6)] for i in range(6)]
    assert left == right
# Real + Hodge eigenlattice Gram after division by sqrt5.
Bfirst = [[2*(F(G2[i][j]) + s*W[i][j]) for j in src] for i in src]
assert is_positive_definite(Bfirst)
assert is_positive_definite([[x.conj() for x in row] for row in Bfirst])
print('04 PASS: exact six-by-six Hodge identity and definite base form at both real places')

# Orientation reversal changes (W,K) to (-W,-K). The plus-first-order
# expression still reduces to 2*G2 on the new plus eigenlattice.
Wrev = [[-x for x in row] for row in W]
Krev = mm(Wrev, G2)
assert Krev == [[-x for x in row] for row in K]
Arev = [[F(Krev[i][j]) + s*int(i == j) for j in range(6)]
        for i in range(6)]
Breversed = mm(mm(tr(Arev), [[F(x) for x in row] for row in Wrev]), Arev)
assert Breversed == [[2*s*(F(G2[i][j]) - s*W[i][j])
                       for j in range(6)] for i in range(6)]
assert residues([[2*G2[i][j] for j in src] for i in src]) == hp
# Non-unimodular pairing beta/2 DOES change the square class.
assert (3*pow(2, -1, 5)) % P in {1, 4}
print('05 PASS: orientation reversal stable, but non-unimodular beta/2 changes square class')

pC, pR = (1, 2, 3, 4, 0), (1, 2, 0, 3, 4)
AW = []
for perm in (pC, pR):
    Aq = tr([qcoords(mv(residues(perm_a4(perm)), e)) for e in Qcols])
    a = residues(mm(mm(T, Aq), inv(T)))
    assert residues(mm(mm(tr(a), Bpub), a)) == Bpub
    AW.append(a)
relations = []
for a in AW:
    for i in range(3):
        for j in range(3):
            row = [0]*9
            for k in range(3):
                row[3*i + k] += a[k][j]
                row[3*k + j] -= a[i][k]
            relations.append(row)
centralizer = null_basis(relations)
assert len(centralizer) == 1
assert centralizer[0] == [x*centralizer[0][0] % P for x in sum(ident(3), [])]
assert centralizer[0][0] != 0
assert all((3*a*a) % P in {2, 3} for a in range(1, 5))
print('06 PASS: End_A5(W5)=F5; marked A5-equivariant square class is fixed')

phi = F(Q(1, 2), Q(1, 2))
assert phi*phi == phi + 1 and phi*phi.conj() == F(-1)
assert phi.residue() == 3
samples = 0
for eps, n in product((1, -1), range(-7, 8)):
    u = eps*(phi**n)
    norm = u*u.conj()
    assert norm == F((-1)**n)
    r = u.residue()
    assert r*r % P == norm.residue()
    srel = 3*pow(r, -1, P) % P
    predicted = eps*pow(3, 1-n, P) % P
    assert srel == predicted
    assert (srel in {1, 4}) == (norm == F(-1))
    g = [[x/u for x in row] for row in Bfirst]
    for emb in (False, True):
        gg = [[x.conj() if emb else x for x in row] for row in g]
        sign = u.conj().sign() if emb else u.sign()
        assert sign in (-1, 1)
        assert is_positive_definite([[sign*x for x in row] for row in gg])
    assert (u.sign() == u.conj().sign()) == (n % 2 == 0)
    samples += 1
assert samples == 30
assert (phi*s).conj()*(phi*s) == F(5)
print('07 PASS: 30 uniformizers exact (n=-7..7, both signs), real-place definiteness')
print('08 PASS: square residual multiplier iff Norm(unit)=-1; isometry vs sign tradeoff')

# A5 + J: no common fixed symmetric form. Compute the entire linear
# constraint system, not a citation of the 744000-element group census.
AqM = tr([qcoords(mv(residues(M), e)) for e in Qcols])
Lb = residues(L)
# L acts on ell wedge Vbar.  The quotient action has an EXTRA scalar 2,
# since M ell = 2 ell mod 5.  Confusing it with the M action is a type error.
assert [x % P for x in mv(residues(M), ell)] == [2, 2, 2, 2]
Lcols = []
for e in Qcols:
    image = mv(Lb, wedge(ell, e))
    Lcols.append(qcoords(solve(E, image)))
DL = residues(tr(Lcols))
assert DL == residues([[2*x for x in row] for row in AqM])
D = residues(mm(mm(T, DL), inv(T)))
assert det3(D) == P-1
assert residues(mm(mm(mm(mm(D, D), D), D), D)) == [[-x % P for x in row] for row in ident(3)]
bases = []
for i in range(3):
    for j in range(i, 3):
        b = [[0]*3 for _ in range(3)]
        b[i][j] = 1
        b[j][i] = 1
        bases.append(b)
form_eqns = []
for gen in AW + [D]:
    changed = [residues(mm(mm(tr(gen), b), gen)) for b in bases]
    for i in range(3):
        for j in range(i, 3):
            form_eqns.append([(x[i][j] - b[i][j]) % P for x, b in zip(changed, bases)])
assert rank(form_eqns[:12]) == 5
assert rank(form_eqns) == 6
print('09 PASS: A5 preserves one metric line; adding J leaves no nonzero fixed symmetric form')

# Generic total ramification control for odd primes: Phi_p(1+p*t) == p mod p^2.
for prime in (3, 5, 7, 11, 13):
    for t in range(prime):
        x = 1 + prime*t
        assert sum(pow(x, k, prime*prime) for k in range(prime)) % (prime*prime) == prime
print('10 PASS: Phi_p(1+p*t)=p mod p^2 on p=3,5,7,11,13, all t')
print('ALL 10 EXACT LOCAL CHECKS PASS; NON-CANONICAL L1, no independent gate')
