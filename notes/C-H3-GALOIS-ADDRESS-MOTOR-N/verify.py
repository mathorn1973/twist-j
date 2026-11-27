"""Non-canonical proof-led audit, issue #2106. Pinned H3 law, unchanged."""
import hashlib
import importlib.util
import sys
from itertools import product
from pathlib import Path
from collections import Counter

source=Path(sys.argv[1] if len(sys.argv)>1 else 'reproduce/h3-referenced-record/verify.py')
raw=source.read_bytes()
assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()=='fd215e24fefbbebf83cf3985d8ebcedd590aa709'
spec=importlib.util.spec_from_file_location('pinned_h3',source)
H=importlib.util.module_from_spec(spec)
sys.modules[spec.name]=H
spec.loader.exec_module(H)
Z,O,J,JI,R,RI=H.ZERO,H.ONE,H.J,H.J_INV,H.RHO,H.RHO_INV
P=H.J_POWERS
add,sub,mul,h,scale=H.add,H.sub,H.mul,H.h,H.scale
neg=lambda a:scale(-1,a)
phi=neg(add(P[2],P[3]))
v=neg(phi)
w=add(scale(2,O),P[1])
c=add(O,P[1])
ci=neg(mul(J,P[1]))
assert mul(c,ci)==O
q=lambda z:H.scalar_account(h(z))
S=(Z,)+tuple(scale(s,P[k]) for s in (1,-1) for k in range(5))
A=tuple((scale(s,P[b]),scale(s,P[3*b%5])) for s in (1,-1) for b in range(5))
pos=((1,1),(4,0),(5,3),(4,5),(6,1))
minus=((7,3),(4,4),(3,1),(4,-1),(2,3))
real=lambda a,b:add(scale(a,O),scale(b,phi))
assert tuple(h(sub(z,w)) for z in S[1:])==tuple(real(*ab) for ab in pos+minus)
assert h(w)==real(3,2) and H.T==real(2,-1)
assert [z for z in S if h(sub(z,w))==h(c)]==[O]
assert not any(h(sub(z,w))==H.T for z in S)
mod2=lambda a:tuple(t%2 for t in a)
roots={mod2(a) for a in P}
assert len(roots)==5 and mod2(mul(add(O,P[4]),P[4])) not in roots
def d(x,m,r):
    return mul(mul(m,ci),sub(x,mul(r,w)))
def cell(x,m,a):
    z,r=A[a]
    D=d(x,m,r)
    f=neg(mul(mul(J,RI),mul(m,z)))
    return (D,neg(D),Z,scale(-2,f))
def block(x,m):
    return tuple(cell(x,m,a) for a in range(10) for repeat in range(2))
def residues(m,a):
    r=A[a][1]
    result={mod2(mul(J,d(x,m,r)) if x==r else d(x,m,r)) for x in S}
    assert len(result)<=7
    return result
def guard(m1,a1,m2,a2):
    forbidden=residues(m1,a1)|residues(m2,a2)
    assert len(forbidden)<=14
    return next(g for g in product(range(2),repeat=4) if g not in forbidden)
g1=guard(v,9,P[4],0)
g2=guard(P[4],9,v,0)
def pad(g):
    return ((g,neg(g),Z,Z),)*2
def field(rows):
    return tuple(z for a in range(8) for cell in rows for z in cell)
def account(F):
    return (H.ring_sum(z for i,z in enumerate(F) if i%4<2),
            H.ring_sum(z for i,z in enumerate(F) if i%4>=2),
            H.ring_sum(h(z) for z in F),sum(q(z) for z in F))
def first_output(F,ny,start,x,m):
    strip=tuple(F[H.index(ny,0,start+2*a,2)] for a in range(10))
    nz=[(a,z) for a,z in enumerate(strip) if z!=Z]
    if x==Z:
        assert nz==[]
        return -1,Z
    address=next(a for a,(_,r) in enumerate(A) if r==x)
    target=mul(m,H.sigma(x,2))
    assert nz==[(address,target)]
    sign,k=divmod(S.index(x)-1,5)
    assert address==5*sign+2*k%5
    return address,nz[0][1]
def audit(rows,blocks,expected_q):
    ny=len(rows)
    F=field(rows)
    initial=account(F)
    assert initial[:2]==(Z,Z) and initial[3]==expected_q
    C=H.transport(F,ny,0)
    assert C==F
    N,ev=H.collide(C,ny)
    expected={(a,start+2*i+dup,1)
              for start,x,m in blocks if x!=Z
              for i,(_,r) in enumerate(A) if r==x
              for a in range(8) for dup in range(2)}
    assert set(ev)==expected and len(ev)==len(expected)
    assert all((z!=Z)==((a,b,1) in expected)
               for a,b in product(range(8),range(ny))
               for z in (N[H.index(ny,a,b,2)],))
    assert account(N)==initial
    outs=tuple(first_output(N,ny,*b) for b in blocks)
    C2=H.transport(N,ny,1)
    assert C2==N
    NN,ev2=H.collide(C2,ny)
    assert set(ev2)=={(a,b,2) for a,b,t in expected}
    assert len(ev2)==len(expected) and NN==F
    assert account(NN)==initial
    for bit,U,V in ((0,F,N),(1,N,NN)):
        before,_=H.collide(V,ny)
        assert H.transport(before,ny,bit,backward=True)==U
    # Canonical row representation used only for reproducibility.
    text=';'.join(','.join(map(str,z)) for z in F+N+NN)
    digest=hashlib.sha256(text.encode()).hexdigest()
    return outs,len(ev),digest
def line(label,ix,iy,outs,n,Q,digest):
    print(label,ix,iy,';'.join(str(a)+':'+','.join(map(str,z)) for a,z in outs),
          n,Q,digest)
print('NORMS 11/11; B1 unique; B2 excluded; residue root set 5')
print('GUARDS',','.join(map(str,g1)),','.join(map(str,g2)),'Q',32*(q(g1)+q(g2)))
for ix,x in enumerate(S):
    Q=4160 if x==Z else 5120
    out,n,digest=audit(block(x,O),((0,x,O),),Q)
    line('A',ix,-1,out,n,Q,digest)
for (ix,x),(iy,y) in product(enumerate(S),repeat=2):
    Q=(3840 if x==Z else 4480)+(4160 if y==Z else 5120)+32*(q(g1)+q(g2))
    rows=block(x,v)+pad(g1)+block(y,P[4])+pad(g2)
    out,n,digest=audit(rows,((0,x,v),(22,y,P[4])),Q)
    assert mul(out[0][1],out[1][1])[3]==mul(x,y)[3]
    line('B',ix,iy,out,n,Q,digest)
print('PASS A=11/11 B=121/121 return=132/132 pairing=121/121')
