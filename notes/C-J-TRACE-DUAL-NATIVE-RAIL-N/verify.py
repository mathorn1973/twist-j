"""NON-CANONICAL proof-led native H3 witness, issue #2104.
Usage: python3 verify.py [path-to-pinned-H3-verifier].
"""
from itertools import product, permutations
from pathlib import Path
import hashlib, importlib.util, sys

p=Path(sys.argv[1] if len(sys.argv)>1 else 'reproduce/h3-referenced-record/verify.py')
b=p.read_bytes()
assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()=='fd215e24fefbbebf83cf3985d8ebcedd590aa709'
s=importlib.util.spec_from_file_location('pinned_h3',p)
H=importlib.util.module_from_spec(s)
sys.modules[s.name]=H
s.loader.exec_module(H)
Z,O,J,JI=H.ZERO,H.ONE,H.J,H.J_INV
P=H.J_POWERS
add,sub,mul,scale,h=H.add,H.sub,H.mul,H.scale,H.h
neg=lambda x:scale(-1,x)
trace=lambda x:4*x[0]-sum(x[1:])
q=lambda x:H.scalar_account(h(x))
table=(0,1,-1,1,-1)
def pair(d,f):
    w=mul(d,f)
    assert trace(mul(w,sub(P[2],P[1])))==5*w[3]
    return w[3]
def det(A):
    return sum((-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))*prodint(A[i][p[i]] for i in range(len(p))) for p in permutations(range(len(A))))
def prodint(a):
    t=1
    for x in a:t*=x
    return t
def acct(F):
    return (H.ring_sum(v for n,v in enumerate(F) if n%4<2),
            H.ring_sum(v for n,v in enumerate(F) if n%4>=2),
            H.ring_sum(h(v) for v in F),sum(q(v) for v in F))
def cell(F,ny,a,b):
    t=4*(a*ny+b)
    return F[t:t+4]
def diffs(C):
    return H.half(sub(C[0],C[1])),H.half(sub(C[2],C[3]))
def field(ny,fn):
    return tuple(v for a in range(8) for b in range(ny) for v in fn(a,b))
def tick(F,ny,bit):
    C=H.transport(F,ny,bit)
    assert C==F
    N,ev=H.collide(C,ny)
    back,_=H.collide(N,ny)
    assert back==C
    assert H.transport(back,ny,bit,backward=True)==F
    assert acct(N)==acct(F)
    return N,ev
G=[[pair(P[i],mul(J,P[k])) for k in range(1,5)] for i in range(1,5)]
assert abs(det(G))==1
for i,k in product(range(5),repeat=2):
    x,u=P[i],P[k]; f=mul(J,u)
    F=field(4,lambda a,b:(x,neg(x),f,neg(f)))
    assert acct(F)[0:2]==(Z,Z) and acct(F)[3]==320
    N,e=tick(F,4,0)
    assert len(e)==32 and all(t==1 for a,b,t in e)
    assert all(diffs(cell(N,4,a,b))==(mul(J,x),u) for a,b in product(range(8),range(4)))
    assert pair(x,f)==pair(mul(J,x),u)==table[(i+k)%5]
    assert mul(x,f)==mul(mul(J,x),u)
    NN,e2=tick(N,4,1)
    assert NN==F and len(e2)==32 and all(t==2 for a,b,t in e2)
print('A uniform=25/25 cells=32 q=320 return=2 determinant_abs=1')
S=(Z,)+tuple(scale(t,P[i]) for i in range(4) for t in (1,-1))
for x,f in product(S,repeat=2):
    def initial(a,b):
        d,g=(x,mul(J,x)) if a<4 else (mul(JI,f),f)
        return d,neg(d),g,neg(g)
    F=field(4,initial)
    N,e=tick(F,4,0)
    assert set(e)=={(a,b,1) for a,b in product(range(8),range(4)) if (x if a<4 else f)!=Z}
    for a,b in product(range(8),range(4)):
        assert diffs(cell(N,4,a,b))==((mul(J,x),x) if a<4 else (f,mul(JI,f)))
    assert pair(diffs(cell(N,4,0,0))[0],diffs(cell(N,4,4,0))[1])==pair(x,f)
print('B independent=81/81 complete_inverse=YES dependent_payers=YES')
hist={}
for i,k in product(range(-1,5),repeat=2):
    x=Z if i<0 else P[i]
    u=Z if k<0 else P[k]
    def initial(a,b):
        d=sub(x,P[a]) if a<5 else Z
        g=mul(J,sub(u,P[b])) if b<5 else Z
        return d,neg(d),Z,scale(-2,g)
    F=field(6,initial)
    Q=(240 if i>=0 else 120)+(960 if k>=0 else 480)
    assert acct(F)[3]==Q
    N,e=tick(F,6,0)
    assert all(t==1 and a<5 and b<5 for a,b,t in e)
    flags={(a,b) for a,b in product(range(8),range(6)) if cell(N,6,a,b)[2]!=Z}
    assert flags=={(a,b) for a,b,t in e}
    assert all(a<5 and b<5 for a,b in flags)
    counts=tuple(sum((a+b)%5==m for a,b in flags) for m in range(5))
    expect=(5,)*5 if i==k==-1 else (0,)*5 if min(i,k)<0 else tuple(4 if m==(i+k)%5 else 1 for m in range(5))
    assert counts==expect
    read=table[counts.index(4)] if 4 in counts else 0
    assert read==pair(x,mul(J,u))
    hist[read]=hist.get(read,0)+1
    print('READ',i,k,*counts,'P',read,'Q',Q)
assert hist=={-1:10,0:16,1:10}
print('C reader=36/36 native_CLK_flags=YES B2=0 outputs=-1:10,0:16,+1:10')
print('PASS NON-CANONICAL L1; no native preparer, one-port reducer or physical lift')
