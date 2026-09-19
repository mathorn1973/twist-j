#!/usr/bin/env python3
from fractions import Fraction as F
class Q5:
    __slots__=("a","b")
    def __init__(self,a=0,b=0): self.a=F(a); self.b=F(b)
    def __add__(self,o): o=q(o); return Q5(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return Q5(-self.a,-self.b)
    def __sub__(self,o): return self+(-q(o))
    def __mul__(self,o): o=q(o); return Q5(self.a*o.a+5*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def __truediv__(self,o):
        o=q(o); d=o.a*o.a-5*o.b*o.b
        if not d: raise ZeroDivisionError
        return self*Q5(o.a/d,-o.b/d)
    def __eq__(self,o): o=q(o); return self.a==o.a and self.b==o.b
    def __bool__(self): return bool(self.a or self.b)
    def sig(self): return Q5(self.a,-self.b)
def q(x): return x if isinstance(x,Q5) else Q5(x)
P=((0,1),(0,2),(0,3),(1,2),(1,3),(2,3))
def eye(n,f=F): return [[f(int(i==j)) for j in range(n)] for i in range(n)]
def z(r,c,f=F): return [[f(0) for _ in range(c)] for __ in range(r)]
def add(A,B): return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def sub(A,B): return [[A[i][j]-B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def sc(A,c): return [[c*x for x in r] for r in A]
def mm(A,B): return [[sum((A[i][k]*B[k][j] for k in range(len(B))),start=0) for j in range(len(B[0]))] for i in range(len(A))]
def pw(A,n):
    f=Q5 if isinstance(A[0][0],Q5) else F if isinstance(A[0][0],F) else int
    R=eye(len(A),f)
    while n:
        if n&1:R=mm(R,A)
        A=mm(A,A);n//=2
    return R
def rk(A):
    A=[r[:] for r in A];m=len(A);n=len(A[0]);r=0
    for c in range(n):
        p=next((i for i in range(r,m) if A[i][c]),None)
        if p is None: continue
        A[r],A[p]=A[p],A[r]; v=A[r][c]; A[r]=[x/v for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                v=A[i][c]; A[i]=[A[i][j]-v*A[r][j] for j in range(n)]
        r+=1
    return r
def c2(A):
    f=Q5 if isinstance(A[0][0],Q5) else F if isinstance(A[0][0],F) else int
    R=z(6,6,f)
    for j,(a,b) in enumerate(P):
        for i,(c,d) in enumerate(P): R[i][j]=A[c][a]*A[d][b]-A[c][b]*A[d][a]
    return R
def cols(A):
    out=[]
    for j in range(len(A[0])):
        v=[A[i][j] for i in range(len(A))]
        M=[list(x) for x in zip(*(out+[v]))]
        if rk(M)>len(out): out.append(v)
    return out
def mat(C): return [list(x) for x in zip(*C)]
def cat(A,B): return [a+b for a,b in zip(A,B)]
def sm(ms):
    R=z(len(ms[0]),len(ms[0][0]),F)
    for A in ms:R=add(R,A)
    return R
H=[[F(2 if i==j else 1) for j in range(4)] for i in range(4)]
C=[[-1,-1,-1,-1],[1,0,0,0],[0,1,0,0],[0,0,1,0]]
M=add(eye(4,int),pw(C,2)); A=c2(C); L=c2(M); G=c2(H)
B=z(6,6,F)
for i,p in enumerate(P):
    for j,s in enumerate(P):
        u=p+s
        if len(set(u))==4:
            inv=sum(u[a]>u[b] for a in range(4) for b in range(a+1,4))
            B[i][j]=F(-1 if inv%2 else 1)
K=mm(B,G); assert mm(K,K)==sc(eye(6,F),F(5))
IQ=eye(6,Q5); KQ=[[Q5(x) for x in r] for r in K]; LQ=[[Q5(x) for x in r] for r in L]
Pp=add(sc(IQ,Q5(F(1,2))),sc(KQ,Q5(0,F(1,10))))
Pm=sub(sc(IQ,Q5(F(1,2))),sc(KQ,Q5(0,F(1,10))))
bp,bm=cols(Pp),cols(Pm)
X=mm(mm(Pm,LQ),Pp); Y=mm(mm(Pp,LQ),Pm)
xp=next(v for v in ([X[i][j] for i in range(6)] for j in range(6)) if any(v))
xm=next(v for v in ([Y[i][j] for i in range(6)] for j in range(6)) if any(v))
Ep,Em=mat(bp+[xp]),mat(bm+[xm])
assert rk(Ep)==rk(Em)==4 and rk(cat(Ep,Em))==6
sEp=[[x.sig() for x in r] for r in Ep]
assert rk(cat(sEp,Em))==4
T=sc(sm([pw(A,j) for j in range(5)]),F(1,5)); R=sub(eye(6,F),T)
TQ=[[Q5(x) for x in r] for r in T]; RQ=[[Q5(x) for x in r] for r in R]
assert rk(T)==2 and rk(R)==4 and mm(T,R)==z(6,6,F)
assert rk(cat(Ep,TQ))==4 and rk(cat(Em,TQ))==4
assert 4+4-rk(cat(Ep,Em))==2
RE=mm(RQ,Ep); assert rk(RE)==2 and rk(cat(TQ,RE))==4
assert all(x.denominator==1 for r in L for x in r)
assert all(x.denominator==1 for r in K for x in r)
K5=[[int(x)%5 for x in r] for r in K]
def r5(A):
    A=[r[:] for r in A];m=len(A);n=len(A[0]);r=0
    for c in range(n):
        p=next((i for i in range(r,m) if A[i][c]%5),None)
        if p is None:continue
        A[r],A[p]=A[p],A[r];u=pow(A[r][c],-1,5);A[r]=[(u*x)%5 for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]%5:
                u=A[i][c]%5;A[i]=[(A[i][j]-u*A[r][j])%5 for j in range(n)]
        r+=1
    return r
assert r5(K5)==3
assert [[sum(K5[i][k]*K5[k][j] for k in range(6))%5 for j in range(6)] for i in range(6)]==[[0]*6 for _ in range(6)]
print("P-J-HODGE-INTEGRAL-LIFT-1")
print("chart dimensions over Q(sqrt5): 4 4")
print("Galois conjugate chart: PASS")
print("sum / intersection dimensions: 6 2")
print("common rational primary plane rank: 2")
print("visible periodic plane dimension: 2")
print("minimum Q-defined carrier dimension: 6")
print("integral lift rank: 6")
print("mod-5 Hodge rank / square: 3 0")
print("universal rational-point and minimality clauses: PROOF.md")
print("VERDICT: PASS")
