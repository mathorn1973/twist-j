#!/usr/bin/env python3
"""Independent exact audit of the stated native fiber formulas.
Exploratory, not a preregistered public probe. Standard library only.
"""
from itertools import product
import json

I=((1,0,0),(0,1,0),(0,0,1))
A=((4,1,0),(0,1,0),(0,1,4))
P=((0,4,1),(0,4,0),(1,4,0))
STAR=(1,4,3)

def add(a,b): return tuple((x+y)%5 for x,y in zip(a,b))
def neg(a): return tuple(-x%5 for x in a)
def sub(a,b): return add(a,neg(b))
def scale(k,v): return tuple(k*x%5 for x in v)
def mv(a,v): return tuple(sum(x*y for x,y in zip(row,v))%5 for row in a)
def unpack(x):
    p=x[:4]; s=sum(p)%5;q,r=x[4:]
    w=tuple((v-4*s)%5 for v in p)
    return s,q,r,(w[0],sum(w[:2])%5,sum(w[:3])%5)
def pack(s,q,r,w):
    a,b,c=w
    return tuple((v+4*s)%5 for v in (a,b-a,c-b,-c))+(q,r)
def literal(g,x):
    a,b,c,d,q,r=x
    out=((b,a,d,c,q,r),(-c,-d,-a,-b,-q,-r),
         (-c+2,-d+1+r,-a+2,-b+1-r,1-q,-r),
         (2-a,1-b,3-c,4-d,1-q,1-r),
         (2-a,1-b,3-c,4-d,2-q,1-r))[g]
    return tuple(v%5 for v in out)
def fiber(g,s,q,r,w):
    if g==0: out=(s,q,r,mv(A,w))
    elif g==1: out=(-s,-q,-r,neg(mv(P,w)))
    elif g==2: out=(1-s,1-q,-r,add(neg(mv(P,w)),(3,r,3+r)))
    else: out=(-s,(1 if g==3 else 2)-q,1-r,add(neg(w),(2,3,1)))
    return tuple(v%5 for v in out[:3])+(out[3],)
def kernel(bit,x): return literal((sum(x)+2*bit)%5,x)
def theta(n): return n.bit_count()%2
def k_chart(n,s,q,r,w):
    tau=0
    while (s+q+r)%5 not in (1,4):
        g=(s+q+r+2*theta(n))%5
        s,q,r,w=fiber(g,s,q,r,w)
        n+=1; tau+=1
        assert tau<=9
    v=sub(w,STAR)
    if (s+q+r)%5==4: v=mv(P,v)
    return scale(-1 if n%2 else 1,v)
def phi_lambda(lam,x):
    s,q,r,w=unpack(x);z=(s+q+r)%5
    center=(4-r)%5 if z==0 else 4
    nw=add(w,scale((lam-1)*(w[1]-center),(3,1,3)))
    return pack(s,q,r,nw)

counts={'checkpoint_generator_decompositions':0,'checkpoint_extensions':0,
        'full_counter_chart_affine_basis_checks':0}
for x in product(range(5),repeat=6):
    args=unpack(x)
    assert pack(*args)==x
    for g in range(5):
        assert pack(*fiber(g,*args))==literal(g,x)
        counts['checkpoint_generator_decompositions']+=1
    for lam,bit in product(range(1,5),range(2)):
        assert phi_lambda(lam,kernel(bit,x))==kernel(bit,phi_lambda(lam,x))
        counts['checkpoint_extensions']+=1

for n,s,q,r,w in product(range(32),range(5),range(5),range(5),((0,0,0),)+I):
    nxt=fiber((s+q+r+2*theta(n))%5,s,q,r,w)
    assert k_chart(n,s,q,r,w)==k_chart(n+1,*nxt)
    counts['full_counter_chart_affine_basis_checks']+=1

def entrance(n,z):
    steps=0
    while z not in (1,4):
        z=((0,4,0,4,4),(2,1,1,3,1))[theta(n)][z]
        n+=1;steps+=1
        assert steps<=9
    return steps
assert entrance(14,0)==9
maximum=max(entrance(n,z) for n,z in product(range(4096),range(5)))
assert maximum==9
counts['bounded_entrance_cases']=4096*5
counts['maximum_entrance']=maximum
counts['sharp_witness']={'n':14,'z':0,'driver':'101001011'}
counts['status']='NON-CANONICAL exploratory exact audit; universal entrance bound proved separately'
print(json.dumps(counts,indent=2))
