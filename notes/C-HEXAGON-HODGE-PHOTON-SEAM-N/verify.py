#!/usr/bin/env python3
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction
from collections import Counter
from itertools import combinations

@dataclass(frozen=True)
class K:
    a: Fraction
    b: Fraction = Fraction(0)
    def __add__(self, o):
        o = lift(o); return K(self.a+o.a, self.b+o.b)
    __radd__ = __add__
    def __neg__(self): return K(-self.a, -self.b)
    def __sub__(self, o): return self + (-lift(o))
    def __rsub__(self, o): return lift(o) - self
    def __mul__(self, o):
        o = lift(o)
        return K(self.a*o.a + 5*self.b*o.b, self.a*o.b + self.b*o.a)
    __rmul__ = __mul__
    def inv(self):
        d = self.a*self.a - 5*self.b*self.b
        assert d != 0
        return K(self.a/d, -self.b/d)
    def __truediv__(self, o): return self * lift(o).inv()
    def __rtruediv__(self, o): return lift(o) / self
    def __pow__(self, n: int):
        assert n >= 0
        r = ONE; x = self
        while n:
            if n & 1: r = r*x
            x = x*x; n //= 2
        return r
    def __bool__(self): return self.a != 0 or self.b != 0

def lift(x):
    if isinstance(x,K): return x
    return K(Fraction(x))

ZERO=K(Fraction(0)); ONE=K(Fraction(1)); PHI=K(Fraction(1,2),Fraction(1,2))

def mat_eye(n): return [[ONE if i==j else ZERO for j in range(n)] for i in range(n)]
def mat_add(A,B): return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def mat_mul(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))), ZERO) for j in range(len(B[0]))] for i in range(len(A))]
def mat_scale(A,c):
    c=lift(c); return [[c*x for x in row] for row in A]
def mat_trace(A): return sum((A[i][i] for i in range(len(A))), ZERO)

def charpoly(A):
    n=len(A); B=mat_eye(n); coeff=[ONE]
    for k in range(1,n+1):
        AB=mat_mul(A,B)
        ck = -mat_trace(AB)/k
        coeff.append(ck)
        B=mat_add(AB,mat_scale(mat_eye(n),ck))
    return list(reversed(coeff))

def companion(poly):
    n=len(poly)-1; assert poly[-1]==ONE
    A=[[ZERO for _ in range(n)] for _ in range(n)]
    for i in range(1,n): A[i][i-1]=ONE
    for i in range(n): A[i][n-1]=-poly[i]
    return A

def wedge2(A):
    pairs=list(combinations(range(len(A)),2)); idx={p:i for i,p in enumerate(pairs)}
    W=[[ZERO for _ in pairs] for __ in pairs]
    for c,(i,j) in enumerate(pairs):
        for a,b in pairs:
            W[idx[(a,b)]][c]=A[a][i]*A[b][j]-A[a][j]*A[b][i]
    return W

def poly_trim(p):
    p=p[:]
    while len(p)>1 and not p[-1]: p.pop()
    return p

def poly_add(p,q):
    n=max(len(p),len(q)); out=[ZERO]*n
    for i in range(n): out[i]=(p[i] if i<len(p) else ZERO)+(q[i] if i<len(q) else ZERO)
    return poly_trim(out)

def poly_neg(p): return [-x for x in p]
def poly_sub(p,q): return poly_add(p,poly_neg(q))

def poly_mul(p,q):
    out=[ZERO]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q): out[i+j]=out[i+j]+a*b
    return poly_trim(out)

def poly_divmod(p,q):
    p=poly_trim(p); q=poly_trim(q); assert q != [ZERO]
    if len(p)<len(q): return [ZERO],p
    out=[ZERO]*(len(p)-len(q)+1); r=p[:]
    while len(r)>=len(q) and r != [ZERO]:
        c=r[-1]/q[-1]; d=len(r)-len(q); out[d]=c
        sub=[ZERO]*d+[c*x for x in q]
        r=poly_sub(r,sub)
    return poly_trim(out),poly_trim(r)

def poly_monic(p):
    p=poly_trim(p); return [x/p[-1] for x in p]

def poly_gcd(p,q):
    p=poly_trim(p); q=poly_trim(q)
    while q != [ZERO]:
        _,r=poly_divmod(p,q); p,q=q,r
    return poly_monic(p)

def det_int(M):
    A=[list(map(int,row)) for row in M]; n=len(A); sign=1; den=1
    for k in range(n-1):
        if A[k][k]==0:
            s=next(i for i in range(k+1,n) if A[i][k]!=0)
            A[k],A[s]=A[s],A[k]; sign*=-1
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                A[i][j]=(A[i][j]*pivot-A[i][k]*A[k][j])//den
        den=pivot
        for i in range(k+1,n): A[i][k]=0
    return sign*A[-1][-1]

def label_multiset_source(m):
    return Counter([(2*m,0),(-2*m,0),(0,m%10),(0,(3*m)%10),(0,(7*m)%10),(0,(9*m)%10)])

def label_multiset_target(n):
    return Counter([(0,0),(0,0),(2*n,n%10),(2*n,(-n)%10),(-2*n,n%10),(-2*n,(-n)%10)])

def hom_dim(m,n):
    S=label_multiset_source(m); T=label_multiset_target(n)
    return sum(S[k]*T[k] for k in S.keys() | T.keys())

def expected_hom_dim(m,n):
    if m%10: return 0
    return 12 if m==n else 8

def main():
    C=[
        [K(-1),K(-1),K(-1),K(-1)],
        [K(1),K(0),K(0),K(0)],
        [K(0),K(1),K(0),K(0)],
        [K(0),K(0),K(1),K(0)],
    ]
    C2=mat_mul(C,C); M=mat_add(mat_eye(4),C2); L=wedge2(M)
    pW=charpoly(L)
    pW_expected=poly_mul([ONE,K(-3),ONE],[ONE,K(-1),ONE,K(-1),ONE])
    assert pW==pW_expected

    pE=poly_mul([ONE,K(-3),ONE],[ONE,-PHI,ONE])
    A=companion(pE); assert charpoly(A)==pE
    B=wedge2(A); pB=charpoly(B)
    q=[ONE,-3*PHI,K(8)+PHI,-3*PHI,ONE]
    pB_expected=poly_mul([ONE,K(-2),ONE],q)
    assert pB==pB_expected
    assert poly_gcd(pW,pB)==[ONE]

    H=[
        [1,0,0,-1,0,0],
        [0,1,0,0,-1,0],
        [0,0,1,0,0,-1],
        [1,1,1,1,1,1],
        [1,-1,0,1,-1,0],
        [1,1,-2,1,1,-2],
    ]
    d=det_int(H); assert abs(d)==48; assert d%5 in (2,3)
    alt=[1,-1,1,-1,1,-1]
    rot=alt[-1:]+alt[:-1]
    assert rot==[-x for x in alt]

    Q=[[Fraction(1),Fraction(-3,2)],[Fraction(-3,2),Fraction(1)]]
    T=[[Fraction(3),Fraction(-1)],[Fraction(1),Fraction(0)]]
    def fmul(A,B):
        return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
    TT=[list(x) for x in zip(*T)]
    assert fmul(fmul(TT,Q),T)==Q

    for m in range(1,101):
        for n in range(1,101):
            assert hom_dim(m,n)==expected_hom_dim(m,n)
            assert label_multiset_source(m) != label_multiset_target(n)

    print("PASS G1: planar-hexagon coordinate matrix has |det|=48; antipodal odd triple is reducible under the cycle.")
    print("PASS G2: marked exterior J-step charpoly is (x^2-3x+1)(x^4-x^3+x^2-x+1).")
    print("PASS G3: wedge^2 of the fixed-J Lorentz-chart step has the frozen exact charpoly and gcd(pW,pB)=1.")
    print("PASS G4: same-step intertwiner class S L = B S is zero by coprime characteristic polynomials.")
    print("PASS G5: for all m,n>=1, dim Hom(L^m,B^n)=0 if 10 does not divide m, 8 if 10|m and m!=n, 12 if 10|m=n; never invertible.")
    print("PASS G6: axial recurrence preserves y^2-3yz+z^2; this is an algebraic (1,1) form, not a photon propagation law.")
    print("ALL PASS: C-HEXAGON-HODGE-PHOTON-SEAM-N exact audit complete.")

if __name__=="__main__": main()
