#!/usr/bin/env python3
"""Exact exploratory audit of the signed A4 / bracket / binary pentad bridge.

Independent implementation, Python standard library, no source execution.
This is not a preregistered public probe and earns no Canon status.
"""
from itertools import permutations, combinations, product
import json

P = 5
B = ((2,4,0),(4,2,4),(0,4,2))
BI = ((2,3,4),(3,1,3),(4,3,2))
I = ((1,0,0),(0,1,0),(0,0,1))
A = ((4,1,0),(0,1,0),(0,1,4))
PHI = ((0,4,1),(0,4,0),(1,4,0))

def mv(a,v): return tuple(sum(x*y for x,y in zip(row,v))%5 for row in a)
def mm(a,b): return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(len(b)))%5 for j in range(len(b[0]))) for i in range(len(a)))
def tr(a): return tuple(zip(*a))
def scale(k,a): return tuple(tuple(k*x%5 for x in row) for row in a)
def det(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])-a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])+a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))%5
def dot(u,v): return sum(x*y for x,y in zip(u,v))%5
def norm(v): return dot(v,mv(B,v))
def beta(v,w):
    cross=(v[1]*w[2]-v[2]*w[1],v[2]*w[0]-v[0]*w[2],v[0]*w[1]-v[1]*w[0])
    return mv(BI,cross)
def normline(v):
    a=next(t for t in v if t%5)
    return tuple(x*pow(a,-1,5)%5 for x in v)
def embed(v):
    a,b,c=v
    return (0,a,(-a+b)%5,(-b+c)%5,-c%5)
def quotient(x):
    p=tuple((x[i]-x[0])%5 for i in range(1,5))
    assert sum(p)%5==0
    return (p[0],(p[0]+p[1])%5,(p[0]+p[1]+p[2])%5)
def act(sig,v):
    out=[0]*5
    for i,j in enumerate(sig): out[j]=v[i]
    return tuple(out)
def sign(sig): return -1 if sum(sig[i]>sig[j] for i in range(5) for j in range(i+1,5))%2 else 1
def matrix(sig):
    cols=[quotient(act(sig,embed(v))) for v in I]
    return scale(sign(sig),tuple(zip(*cols)))
def pcompose(sig,tau): return tuple(sig[tau[i]] for i in range(5))
def generated(gens):
    got={I}; queue=[I]
    while queue:
        a=queue.pop()
        for g in gens:
            b=mm(g,a)
            if b not in got: got.add(b);queue.append(b)
    return got
def frame(i):
    others=[j for j in range(5) if j!=i]
    lines=set()
    for pair in combinations(others,2):
        v=tuple(0 if j==i else 1 if j in pair else -1 for j in range(5))
        lines.add(normline(quotient(v)))
    assert len(lines)==3
    return frozenset(lines)

SIGS=list(permutations(range(5)))
FRAMES=tuple(frame(i) for i in range(5))
MATS={s:matrix(s) for s in SIGS}
assert len(set(MATS.values()))==120
assert mm(B,BI)==I
for c in MATS.values():
    assert det(c)==1 and mm(mm(tr(c),B),c)==B
    for v,w in product(I,repeat=2): assert beta(mv(c,v),mv(c,w))==mv(c,beta(v,w))
for s,t in product(SIGS,repeat=2): assert mm(MATS[s],MATS[t])==MATS[pcompose(s,t)]

lines={normline(v) for v in product(range(5),repeat=3) if any(v)}
square={v for v in lines if norm(v) in (1,4)}
assert len(lines)==31 and len(square)==15
assert len(set().union(*FRAMES))==15 and set().union(*FRAMES)==square
for f in FRAMES:
    for v,w in combinations(f,2): assert dot(v,mv(B,w))==0
    for v in f: assert {w for w in square if dot(v,mv(B,w))==0}==set(f)-{v}
for s,c in MATS.items():
    for i,f in enumerate(FRAMES): assert frozenset(normline(mv(c,v)) for v in f)==FRAMES[s[i]]

EVEN=[m for m in range(32) if m.bit_count()%2==0]
v=[31^(1<<i) for i in range(5)]
def q2(m): return (m.bit_count()//2)%2
def b2(m,n): return (m&n).bit_count()%2
def xor_sum(values):
    out=0
    for value in values: out^=value
    return out
assert {m for m in EVEN if m and q2(m)==0}==set(v)
assert all(any(b2(m,n) for n in EVEN) for m in EVEN if m)
def combine(mask): return xor_sum(v[i+1] for i in range(4) if mask>>i&1)
CB={combine(m):m for m in range(16)}
assert len(CB)==16 and xor_sum(v)==0
for m in range(16):
    assert q2(combine(m))==((m.bit_count()*(m.bit_count()-1)//2)%2)
    root=(combine(m)>>1)&15
    tau=root^(15 if root.bit_count()%2 else 0)
    assert tau==m
def actbits(s,m): return sum(1<<s[i] for i in range(5) if m>>i&1)
binary_actions=[]
for s in SIGS:
    binary_actions.append(tuple(CB[actbits(s,combine(m))] for m in range(16)))
    for m in EVEN: assert q2(actbits(s,m))==q2(m)
assert len(set(binary_actions))==120

sigma_a=(0,2,1,4,3)
sigma_phi=(0,3,4,1,2)
tau=(1,0,2,3,4)
assert MATS[sigma_a]==A and MATS[sigma_phi]==PHI
T=MATS[tau]
assert T==((1,0,0),(3,4,0),(4,0,4)) and mm(T,T)==I
native=generated([A,PHI,scale(-1,I)])
native_so={g for g in native if det(g)==1}
assert len(native)==8 and len(native_so)==4
assert len(generated([A,PHI,T]))==120
assert T not in native
assert len(generated([PHI,T]))==12

# All order-five maps on the common five labels form a single 24-element class.
fivecycles=[]
for s in SIGS:
    seen=set();j=0
    while j not in seen: seen.add(j);j=s[j]
    if len(seen)==5: fivecycles.append(s)
assert len(fivecycles)==24
assert not set(MATS[s] for s in fivecycles)&native

out={
  'status':'NON-CANONICAL exploratory exact audit; proofs carry universal claims',
  'signed_s5_matrices':len(MATS),'homomorphism_pairs':len(SIGS)**2,
  'projective_directions':len(lines),'square_directions':len(square),
  'intrinsic_frames':[[list(v) for v in sorted(f)] for f in FRAMES],
  'frame_permutations':120,'binary_states':len(EVEN),'binary_isometries':120,
  'carry_basis_matches_registered_tau15':True,
  'native_tangent_group':len(native),'native_bracket_group':len(native_so),
  'missing_transposition_matrix':T,'native_plus_T_group':120,
  'active_phi_plus_T_group':12,'fivecycles':len(fivecycles)
}
print(json.dumps(out,indent=2))
