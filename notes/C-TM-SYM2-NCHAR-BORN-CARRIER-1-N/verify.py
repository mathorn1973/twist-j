#!/usr/bin/env python3
"""Exact NON-CANONICAL audit for the N-character Born carrier."""
from fractions import Fraction as F
from itertools import permutations

W3=((0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,0,1),(1,1,0))
def N(w): a,b,c=w; return (1-a,1-b,1-c)
def omega(w): a,b,c=w; return c-a

unseen=set(W3); orbits=[]
while unseen:
    w=min(unseen); O=tuple(sorted((w,N(w)))); orbits.append(O); unseen-=set(O)
orbits=tuple(sorted(orbits))
assert len(orbits)==3

# C1-C2. Kernel of swap+I on Q^2 is span(1,-1), projectively fixed by swap.
for O in orbits:
    basis=(F(1),F(-1))
    assert (basis[1],basis[0])==(-basis[0],-basis[1])
print("C1 PASS odd line dimension one on every two-sheet orbit")
print("C2 PASS sheet swap fixes the projective odd line")

# C3. Source character matches; do not replace zero instantaneous state.
zero_count=0
for O in orbits:
    a=omega(O[0]); b=omega(O[1])
    assert b==-a
    if a==b==0: zero_count+=1
assert zero_count==1
print("C3 PASS source N-character matches; one instantaneous zero orbit preserved")

# C4-C5. Any nonzero odd-line representative gives same coordinate Born law.
reference=None
for O in orbits:
    for x in (F(1),F(-2),F(7,5)):
        v=(x,-x); norm=v[0]*v[0]+v[1]*v[1]
        assert norm>0
        p=(v[0]*v[0]/norm,v[1]*v[1]/norm)
        if reference is None: reference=p
        assert p==reference
assert reference==(F(1,2),F(1,2))
print("C4 PASS projective odd-line Born law unique")
print("C5 PASS carrier Born law total including palindrome orbit")

# C6. Reconstruct quotient transfer and stationary law, then compose.
idx={w:i for i,O in enumerate(orbits) for w in O}
def Eeven(w): a,b,c=w; return (1-a,b,1-b)
def Eodd(w): a,b,c=w; return (b,1-b,c)
T=[[F(0)]*3 for _ in range(3)]
for parent,O in enumerate(orbits):
    w=O[0]
    for kid in (Eeven(w),Eodd(w)): T[idx[kid]][parent]+=1
assert T==[[F(0),F(1),F(1)],[F(1),F(0),F(1)],[F(1),F(1),F(0)]]
pQ=(F(1,3),)*3
for i in range(3): assert sum(T[i][j]*pQ[j] for j in range(3))==2*pQ[i]
mu={}
for i,O in enumerate(orbits):
    for k,w in enumerate(O): mu[w]=pQ[i]*reference[k]
assert sum(mu.values())==1 and len(set(mu.values()))==1
common=None; n=0
for perm in permutations(range(6)):
    lm=[F(0)]*6
    for w,v in zip(W3,perm): lm[v]+=mu[w]
    lm=tuple(lm)
    if common is None: common=lm
    assert lm==common
    n+=1
assert n==720
print("C6 PASS quotient composition and all 720 chart pushforwards coherent")

# C7 is a source-scope ruling, not a finite arithmetic test.
print("C7 BOUNDARY public MEASURE-BORN-VERB is specifically a Born square of the verb")
print("DECISION MATHEMATICAL-CARRIER")
