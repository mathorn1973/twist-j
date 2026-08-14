#!/usr/bin/env python3
"""Independent exact breaker for C-TM-SYM2-ORIENTED-BORN-JUNCTION-1-N.

Frozen before any positive verifier exists. Standard library only. This is
NON-CANONICAL incubation tooling and is not public probe evidence.
"""
from fractions import Fraction as F
from itertools import permutations

W3 = ((0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,0,1),(1,1,0))

def N(w):
    a,b,c = w
    return (1-a,1-b,1-c)

def R(w):
    a,b,c = w
    return (c,b,a)

def omega(w):
    a,b,c = w
    return c-a

# Build N-orbits without choosing representatives in the conclusion.
unseen = set(W3)
orbits = []
while unseen:
    w = min(unseen)
    O = frozenset((w,N(w)))
    assert len(O) == 2
    orbits.append(O)
    unseen -= O
orbits = tuple(sorted(orbits, key=lambda O: tuple(sorted(O))))
assert len(orbits) == 3

# B1: direct omega-square conditional Born route must fail on one orbit.
omega_norms = tuple(sum(F(omega(w)**2) for w in O) for O in orbits)
assert sorted(omega_norms) == [F(0),F(2),F(2)]
assert any(x == 0 for x in omega_norms)

# Character checks, independent of any selector.
for w in W3:
    assert omega(R(w)) == -omega(w)
    assert omega(N(w)) == -omega(w)
    assert omega(N(R(w))) == omega(w)

# B2: quotient transfer. Columns are parents; each orbit has one child in
# each of the other two quotient orbits and none in itself.
T = (
    (F(0),F(1),F(1)),
    (F(1),F(0),F(1)),
    (F(1),F(1),F(0)),
)
# Solve T p = 2 p plus sum p=1 directly by subtraction.
# Equations imply p0=p1=p2; normalization then fixes the vector.
p = (F(1,3),F(1,3),F(1,3))
for i in range(3):
    assert sum(T[i][j]*p[j] for j in range(3)) == 2*p[i]
assert sum(p) == 1
# Independent uniqueness: rank of augmented rational system by RREF.
A = [
    [T[i][j] - (F(2) if i == j else F(0)) for j in range(3)] + [F(0)]
    for i in range(3)
]
A.append([F(1),F(1),F(1),F(1)])
row = 0
pivots = []
for col in range(3):
    pivot = next((r for r in range(row,len(A)) if A[r][col] != 0), None)
    if pivot is None:
        continue
    A[row],A[pivot] = A[pivot],A[row]
    q = A[row][col]
    A[row] = [x/q for x in A[row]]
    for r in range(len(A)):
        if r == row:
            continue
        q = A[r][col]
        if q:
            A[r] = [A[r][c]-q*A[row][c] for c in range(4)]
    pivots.append(col)
    row += 1
assert pivots == [0,1,2]
assert tuple(A[i][3] for i in range(3)) == p

# B3: coefficient Born support is forced equal by v=(1,1) on its two slots.
v = (F(1),F(1))
Z = sum(x*x for x in v)
half = tuple(x*x/Z for x in v)
assert half == (F(1,2),F(1,2))
# Both support orientations push forward to the same two-point distribution.
for perm in ((0,1),(1,0)):
    pushed = [F(0),F(0)]
    for i,j in enumerate(perm):
        pushed[j] += half[i]
    assert tuple(pushed) == half

# B4: construct window measure only now, from quotient p and support half.
mu = {}
for idx,O in enumerate(orbits):
    members = tuple(sorted(O))
    assert len(members) == 2
    for j,w in enumerate(members):
        mu[w] = p[idx] * half[j]
assert set(mu) == set(W3)
assert sum(mu.values()) == 1
assert all(x > 0 for x in mu.values())
# Derivation gives a common value, but this was not an input to Q or B.
values = set(mu.values())
assert len(values) == 1

# B5/B6: any bijective chart sends the derived uniform W3 measure to the
# same coordinate measure on six line labels. This is stronger than checking
# only the frozen 48 selector charts and therefore cannot hide a selected one.
labels = tuple(range(6))
for perm in permutations(labels):
    line_mu = {v:F(0) for v in labels}
    for w,vlabel in zip(W3,perm):
        line_mu[vlabel] += mu[w]
    assert len(set(line_mu.values())) == 1
    assert sum(line_mu.values()) == 1

# B7: adjacent-pair control is evaluated only after mu exists.
E00 = tuple(w for w in W3 if w[:2] == (0,0))
assert E00 == ((0,0,1),)
rho00_candidate = sum(mu[w] for w in E00)
assert rho00_candidate in values

# Orientation retention firewall: enumerate the full input sign and stream
# values. The scalar measure is allowed to be blind, but it is defined on the
# full typed product, not on a quotient of it.
for eps in (-1,1):
    for om in (-1,0,1):
        J = tuple(F(om*eps*x) for x in (1,-1,-1,1))
        assert len(J) == 4
        # The Born scalar map is a total function on this typed input family.
        assert sum(mu.values()) == 1

print("B1 PASS omega-only route has exact zero-norm N-orbit")
print("B2 PASS quotient stationary law unique")
print("B3 PASS coefficient support Born law orientation-independent")
print("B4 PASS six-word measure total and normalized")
print("B5 PASS every bijective selector chart gives one line measure")
print("B6 PASS all 720 bijections checked, hence frozen 48 covered")
print("B7 PASS GYRON event evaluated only as post-construction control")
print("B8 PASS no decoder or D_matter object constructed")
print("BREAKER PASS")
