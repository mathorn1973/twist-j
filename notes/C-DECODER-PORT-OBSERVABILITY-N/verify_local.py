"""NON-CANONICAL exact local audit. One x86_64 lane; no formal gate."""
from fractions import Fraction as F
from itertools import product, permutations
from collections import defaultdict
from hashlib import sha256
from pathlib import Path

ROOT=Path(__file__).resolve().parent
assert sha256((ROOT/'PREREG.md').read_bytes()).hexdigest()=='020ce31d809e6b6c29b502d3bd5623f82a7be25eefb53ab231058093655608e1'
O=(0,0,0)
Y=(O,(1,1,0),(1,0,1),(0,1,1),(2,0,0))
weights={2:6,4:1,8:15,10:1,16:1}
add=lambda x,y: tuple(a+b for a,b in zip(x,y))
sub=lambda x,y: tuple(a-b for a,b in zip(x,y))
# Direct norm-enumeration construction.
C={x:F(weights[sum(a*a for a in x)],324) for x in product(range(-4,5),repeat=3) if sum(a*a for a in x) in weights}
assert len(C)==60 and sum(C.values())==F(8,9)
H=dict(C);H[O]=F(10,9)
H2={}
for y in Y:
    H2[y]=sum((h*H.get(sub(y,x),F(0)) for x,h in H.items()),F(0))
center=lambda a: tuple(a[j]-sum(a,F(0))/5 for j in range(4))
M=tuple(center(tuple(H.get(sub(x,y),F(0)) for y in Y)) for x in Y[:4])
a=M[0]
b=center(tuple(H2[y]-2*(y==O) for y in Y))
assert a[1]==a[2]==a[3] and b[1]==b[2]==b[3]
minor=a[0]*b[1]-a[1]*b[0]
assert minor!=0
v=(349,354,354,348)
N=tuple(tuple(F(1770*(i==j)-v[i]) for j in range(4)) for i in range(4))
assert M==tuple(tuple(x/1620 for x in row) for row in N)
Minv=tuple(tuple(F(54,59)*(F(i==j)+F(v[i],365)) for j in range(4)) for i in range(4))
def mv(A,x): return tuple(sum((a*b for a,b in zip(row,x)),F(0)) for row in A)
assert tuple(tuple(sum((M[i][k]*Minv[k][j] for k in range(4)),F(0)) for j in range(4)) for i in range(4))==tuple(tuple(F(i==j) for j in range(4)) for i in range(4))
# Second construction: signed-permutation shells and sparse full update.
C_alt={}
for rep,weight in (((1,1,0),6),((2,0,0),1),((2,2,0),15),((3,1,0),1),((4,0,0),1)):
    for p in set(permutations(rep)):
        for signs in product((-1,1),repeat=3):
            C_alt[tuple(a*s for a,s in zip(p,signs))]=F(weight,324)
assert C_alt==C

def prepare(z):
    mean=sum(z,F(0))/5
    return {y:t-mean for y,t in zip(Y,tuple(z)+(F(0),)) if t-mean}

def step(u,v,ports):
    w=defaultdict(F)
    for x,c in u.items():w[x]-=c
    for x,c in v.items():
        w[x]+=2*c
        for d,k in C_alt.items():
            w[x]-=k*c
            w[add(x,d)]+=k*c
    outgoing={}
    for x,g in ports.items():
        w[x]=(w[x]+g*u.get(x,F(0))/2)/(1+g/2)
        outgoing[x]=-(w[x]-u.get(x,F(0)))/2
    return dict(v),{x:c for x,c in w.items() if c},outgoing

grid=(F(1,2),F(2),F(5))
for g in grid:
    for j in range(4):
        z=tuple(F(i==j) for i in range(4))
        u0={};v0=prepare(z)
        u1,v1,out1=step(u0,v0,{O:g})
        _,_,out2=step(u1,v1,{O:g})
        assert out1[O]==-a[j]/(2+g)
        assert out2[O]==-(b[j]-g/(2+g)*F(10,9)*a[j])/(2+g)
        _,_,out4=step(u0,v0,{y:g for y in Y[:4]})
        assert tuple(out4[y] for y in Y[:4])==tuple(-M[i][j]/(2+g) for i in range(4))
        assert mv(Minv,tuple(-(2+g)*out4[y] for y in Y[:4]))==z

# Bounded checks audit the all-time symmetry proof, not its quantifiers.
for dark in ((0,1,-1,0),(0,1,0,-1)):
    u={};v0=prepare(tuple(map(F,dark))); vv=v0
    for _ in range(3):
        u,vv,out=step(u,vv,{O:F(2)})
        assert out[O]==0

q=(F(1),F(1),F(0),F(0)); q2=(F(1),F(-1),F(0),F(0))
z=mv(Minv,q);z2=mv(Minv,q2)
assert tuple(x*x for x in mv(M,z))==tuple(x*x for x in mv(M,z2))
def mass(z): return sum(x*x for x in z)-sum(z)**2/5
def low(z): return sum(z)**2/(20*mass(z))
assert low(z)>0 and low(z2)==0
print('NON-CANONICAL LOCAL AUDIT; no physical or two-architecture result')
print('source: Public Canon v77 at 8ea01cd36ade943af10718593b0e1348d6837a3b')
print('single-origin first row a =',a)
print('single-origin independent row b =',b)
print('two-row (z0,z1+z2+z3) determinant =',minor)
print('single-origin invisible source plane: z0=0, z1+z2+z3=0')
print('four-port matrix: M=(1770 I-v 1^T)/1620; v=',v)
print('det M =',F(1770**3*365,1620**4))
print('M^-1 = (54/59)(I+v 1^T/365)')
print('signed basis tests: g=1/2,2,5; first two origin transitions and first four-port transition PASS')
print('two source-dark witnesses through three steps: PASS; all-time conclusion relies on symmetry proof')
print('heat-only equal first-step outputs; rational source low weights:',low(z),low(z2))
print('ALL LOCAL AUDIT CHECKS PASS')
