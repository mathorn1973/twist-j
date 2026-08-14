#!/usr/bin/env python3
"""Independent exact breaker, frozen before positive verifier."""
from fractions import Fraction as F
from itertools import permutations

W3=((0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,0,1),(1,1,0))
def N(w): a,b,c=w; return (1-a,1-b,1-c)
def R(w): a,b,c=w; return (c,b,a)
def omega(w): a,b,c=w; return c-a

unseen=set(W3); orbits=[]
while unseen:
    w=min(unseen); O=tuple(sorted((w,N(w)))); orbits.append(O); unseen-=set(O)
orbits=tuple(sorted(orbits))
assert len(orbits)==3

# A nonzero odd vector on an ordered chart of a two-point orbit is (x,-x).
# Swapping the chart multiplies the canonical representative (1,-1) by -1.
for O in orbits:
    x=F(7,3)
    a=(x,-x)
    swapped=(a[1],a[0])
    assert swapped==(-x,x)
    # Born law after proof of nonzero norm.
    norm=a[0]*a[0]+a[1]*a[1]
    assert norm>0
    p=(a[0]*a[0]/norm,a[1]*a[1]/norm)
    assert p[0]==p[1]
    # scale and sign controls
    for c in (F(-5,2),F(3,7)):
        b=(c*a[0],c*a[1]); q=b[0]*b[0]+b[1]*b[1]
        pb=(b[0]*b[0]/q,b[1]*b[1]/q)
        assert pb==p

# Source character is odd under N, but the palindrome orbit has zero
# instantaneous source vector. Keep carrier/state distinction exact.
zero_orbits=[]
for O in orbits:
    vals=tuple(omega(w) for w in O)
    assert vals[1]==-vals[0]
    if vals==(0,0): zero_orbits.append(O)
assert len(zero_orbits)==1

# Independent quotient composition, values evaluated only now.
T=((F(0),F(1),F(1)),(F(1),F(0),F(1)),(F(1),F(1),F(0)))
pQ=(F(1,3),)*3
for i in range(3): assert sum(T[i][j]*pQ[j] for j in range(3))==2*pQ[i]
half=(F(1,2),F(1,2))
mu={}
for i,O in enumerate(orbits):
    for k,w in enumerate(O): mu[w]=pQ[i]*half[k]
assert sum(mu.values())==1 and len(set(mu.values()))==1

# Strong coherence: every bijection to six line labels yields same measure.
common=None
for perm in permutations(range(6)):
    lm=[F(0)]*6
    for w,v in zip(W3,perm): lm[v]+=mu[w]
    lm=tuple(lm)
    if common is None: common=lm
    assert lm==common

print("B1 PASS odd projective line independent of sheet order")
print("B2 PASS Born law independent of representative, scale and sign")
print("B3 PASS carrier total on all three N-orbits")
print("B4 PASS palindrome instantaneous source remains exactly zero")
print("B5 PASS quotient composition normalized")
print("B6 PASS all 720 selector charts coherent")
print("B7 MANUAL current MEASURE-BORN-VERB scope must be decided separately")
print("BREAKER PASS")
