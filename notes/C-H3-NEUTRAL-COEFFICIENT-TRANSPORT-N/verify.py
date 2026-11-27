"""NON-CANONICAL proof-led branch and native audit, frozen issue #2109."""
import hashlib
import importlib.util
import sys
from itertools import product
from pathlib import Path
from collections import Counter
from functools import cache
from fractions import Fraction

source=Path(sys.argv[1] if len(sys.argv)>1 else 'reproduce/h3-referenced-record/verify.py')
raw=source.read_bytes()
assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()=='fd215e24fefbbebf83cf3985d8ebcedd590aa709'
spec=importlib.util.spec_from_file_location('pinned_h3',source)
H=importlib.util.module_from_spec(spec)
sys.modules[spec.name]=H
spec.loader.exec_module(H)
Z,O,J,JI,R,RI=H.ZERO,H.ONE,H.J,H.J_INV,H.RHO,H.RHO_INV
P=H.J_POWERS
add,sub=H.add,H.sub
mul=cache(H.mul); h=H.h
scale=H.scale
neg=lambda a:scale(-1,a)
rp=Fraction(1,2)
hs=lambda a:scale(rp,a)
JP={-1:JI,0:O,1:J}
C=cache(H.transport_pair); B=cache(H.collision)

def rank5(A):
    A=[list(row) for row in A]; n=len(A[0]); r=0
    for j in range(n):
        pos=next((i for i in range(r,len(A)) if A[i][j]%5),None)
        if pos is None:continue
        A[pos],A[r]=A[r],A[pos]
        k=pow(A[r][j]%5,-1,5); A[r]=[k*x%5 for x in A[r]]
        for i in range(r+1,len(A)):
            u=A[i][j]%5
            A[i]=[(a-u*b)%5 for a,b in zip(A[i],A[r])]
        r+=1
    return r

def A_gate():
    # A finite branch history can accumulate any nonzero residue, not only
    # a single B exponent. Check the full 4^4 possibilities as well.
    for e in (-1,0,1):
        m=pow(2,e,5); n=pow(2,-e,5)
        for a,b in product(range(5),repeat=2):
            c=(a+b)*3%5; d=(a-b)*3%5
            a1=(c+m*d)%5; b1=(c-m*d)%5
            assert (a1+b1)%5==(a+b)%5
            assert ((a1-b1)%5==0)==((a-b)%5==0)
            assert m*n%5==1
    hist=Counter()
    for u in product(range(1,5),repeat=4):
        for shift in (1,2,3):
            # Frozen cyclic order is +1; all cyclic start positions equivalent.
            if shift!=1:continue
            A=[[((u[j] if i==j else 0)-(1 if i==(j+1)%4 else 0))%5
                for j in range(4)] for i in range(4)]
            r=rank5(A); hist[r]+=1
            assert r>=3
            for k in range(4):
                M=[[row[(k+i)%4] for i in range(3)] for row in A]
                assert rank5(M)==3
    assert sum(hist.values())==256
    for es in product((-1,0,1),repeat=4):
        u=tuple(pow(2,e,5) for e in es)
        M=[[((u[j] if i==j else 0)-(1 if i==(j+1)%4 else 0))%5
            for j in range(4)] for i in range(4)]
        assert rank5(M)>=3
    print('A LOCAL_RESIDUE=PASS branch_assignments=81 accumulated_units=256 ranks='+str(sorted(hist.items())))

def eye(n):
    return tuple(tuple(O if i==j else Z for j in range(n)) for i in range(n))
def mm(A,B):
    return tuple(tuple(H.ring_sum(mul(a,b) for a,b in zip(row,col)) for col in zip(*B)) for row in A)
def minus(A,B):
    return tuple(tuple(sub(a,b) for a,b in zip(ar,br)) for ar,br in zip(A,B))
def diag(a):
    return tuple(tuple(v if i==j else Z for j in range(len(a))) for i,v in enumerate(a))
def mvec(A,v):
    return tuple(H.ring_sum(mul(a,b) for a,b in zip(row,v)) for row in A)
def nz(row,basis):
    return any(H.ring_sum(mul(a,b) for a,b in zip(row,v))!=Z for v in basis)
def rdiff(a,b):
    return tuple(sub(u,v) for u,v in zip(a,b))
@cache
def null(A):
    A=[list(row) for row in A]
    n=len(A[0]); r=0;piv=[]
    for j in range(n):
        k=next((i for i in range(r,len(A)) if A[i][j]!=Z),None)
        if k is None:continue
        A[k],A[r]=A[r],A[k]
        inv=H.inverse(A[r][j])
        A[r]=[mul(a,inv) for a in A[r]]
        assert A[r][j]==O
        for i in range(len(A)):
            if i==r:continue
            u=A[i][j]
            if u!=Z:A[i]=[sub(a,mul(u,b)) for a,b in zip(A[i],A[r])]
        piv.append(j);r+=1
    result=[]
    for j in range(n):
        if j in piv:continue
        v=[Z]*n;v[j]=O
        for i,k in enumerate(piv):v[k]=neg(A[i][j])
        result.append(tuple(v))
    return tuple(result)
alpha=hs(add(O,R));beta=hs(sub(O,R))
MC=((alpha,beta),(beta,alpha))
RC=((alpha,Z,beta,Z),(Z,O,Z,Z),(beta,Z,alpha,Z),(Z,Z,Z,O))
def RB(e):
    G=JP[-e]
    a,b=hs(add(O,G)),hs(sub(O,G))
    return ((a,b),(b,a))
@cache
def B_rad(e):
    A,D=RB(e[0]),RB(e[1])
    return ((A[0][0],A[0][1],Z,Z),(A[1][0],A[1][1],Z,Z),
            (Z,Z,D[0][0],D[0][1]),(Z,Z,D[1][0],D[1][1]))
@cache
def sector(word,rad):
    c1,c2,e1,e2=word
    n=4 if rad else 2
    Id=eye(n)
    C1=(RC if rad else MC) if c1 else Id
    C2=(RC if rad else MC) if c2 else Id
    B1=B_rad(e1) if rad else diag(tuple(JP[e] for e in e1))
    B2=B_rad(e2) if rad else diag(tuple(JP[e] for e in e2))
    F1=mm(B1,C1); F2=mm(B2,C2)
    M=minus(mm(F2,F1),Id)
    K=null(M)
    assert all(mvec(M,v)==(Z,)*n for v in K)
    pre2=mm(C2,F1)
    if rad:
        active=all(nz(rdiff(P0[2*i],P0[2*i+1]),K)
                   for P0,e in ((C1,e1),(pre2,e2)) for i in range(2) if e[i])
        change=(c1 and nz(rdiff(Id[0],Id[2]),K)) or (c2 and nz(rdiff(F1[0],F1[2]),K))
    else:
        active=all(nz(P0[i],K) for P0,e in ((C1,e1),(pre2,e2)) for i in range(2) if e[i])
        change=(c1 and nz(rdiff(Id[0],Id[1]),K)) or (c2 and nz(rdiff(F1[0],F1[1]),K))
    return active,bool(change),len(K)

def B_gate():
    es=tuple(product((-1,0,1),repeat=2));hist=Counter();survivors=[]
    for m1,m2,g1,g2,e1,e2 in product((0,1),(0,1),(0,1),(0,1),es,es):
        ma,mc,md=sector((m1,m2,e1,e2),False)
        ra,rc,rd=sector((g1,g2,e1,e2),True)
        if not ma:hist['zero_pre_d']+=1
        elif not ra:hist['zero_pre_f']+=1
        elif not (mc or rc):hist['C_idle']+=1
        else:
            hist['survivors']+=1
            survivors.append((m1,m2,g1,g2,e1,e2,md,rd,mc,rc))
    assert sum(hist.values())==1296
    print('B WORDS',sorted(hist.items()))
    print('B SURVIVORS',len(survivors))
    for w in survivors:print('B WORD',w)

if __name__=='__main__':
    A_gate()
    B_gate()
