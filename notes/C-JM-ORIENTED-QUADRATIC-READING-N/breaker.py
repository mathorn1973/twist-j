#!/usr/bin/env python3
"""Result-exposed separate stdlib arithmetic check; not a blind review."""
from itertools import product
from math import gcd

F=[1,-2,4,-3,1]; G=[1,-4,8,-4,1]
P5=[1,1,1,1,1]; P8=[1,0,0,0,1]

def trim(a):
    a=list(a)
    while len(a)>1 and a[-1]==0: a.pop()
    return a

def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b):c[i+j]+=u*v
    return trim(c)

def rem(a,f):
    a=trim(a); d=len(f)-1
    while len(a)>d:
        k=len(a)-1-d; t=a[-1]
        for i,c in enumerate(f):a[k+i]-=t*c
        a=trim(a)
    return a+[0]*(d-len(a))

def powring(a,n,f):
    r=[1]
    while n:
        if n&1:r=rem(mul(r,a),f)
        a=rem(mul(a,a),f);n//=2
    return rem(r,f)

def conjugate(a,f):
    generator=[0,0,0,-1] if f==P8 else rem([0,0,0,0,1],f)
    out=[0]*4
    for i,t in enumerate(a):
        power=powring(generator,i,f)
        out=[u+t*v for u,v in zip(out,power)]
    return out

def trace(a,f):return 4*a[0] if f==P8 else 4*a[0]-sum(a[1:])

def mm(a,b,mod=None):
    bt=list(zip(*b))
    out=[[sum(u*v for u,v in zip(row,col)) for col in bt] for row in a]
    return [[z%mod for z in row] for row in out] if mod else out

def transpose(a):return [list(row) for row in zip(*a)]
def eye(n):return [[int(i==j) for j in range(n)] for i in range(n)]

def det(a):
    a=[row[:] for row in a]; n=len(a); sign=1; last=1
    for k in range(n-1):
        if a[k][k]==0:
            l=next(i for i in range(k+1,n) if a[i][k])
            a[k],a[l]=a[l],a[k];sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator=a[i][j]*pivot-a[i][k]*a[k][j]
                assert numerator%last==0
                a[i][j]=numerator//last
            a[i][k]=0
        last=pivot
    return sign*a[-1][-1]

def companion(f):
    n=len(f)-1
    return transpose([rem([0]*(i+1)+[1],f) for i in range(n)])

def power(a,n):
    out=eye(len(a))
    while n:
        if n&1:out=mm(out,a,41)
        a=mm(a,a,41);n//=2
    return out

def scalar_sign(a):
    n=len(a)
    return a==eye(n) or a==[[(-z)%41 for z in row] for row in eye(n)]

Hpoly=mul(F,G)
C=transpose([rem([0]*i+[1],F)+rem([0]*i+[1],G) for i in range(8)])
assert det(C)==41
H=companion(Hpoly)
D=[r+[0]*4 for r in companion(F)]+[[0]*4+r for r in companion(G)]
assert mm(D,C)==mm(C,H)
J=[1,0,1,0]; M=[1,1,1,0]
Jp=[powring(J,n,P5) for n in range(8)]
Mp=[powring(M,n,P8) for n in range(8)]
GR=[[trace(rem(mul(Jp[i],conjugate(Jp[j],P5)),P5),P5)+
     trace(rem(mul(Mp[i],conjugate(Mp[j],P8)),P8),P8)
     for j in range(8)] for i in range(8)]
assert GR==transpose(GR) and det(GR)==484128000
positive=0
for z in product((-1,0,1),repeat=8):
    q=sum(z[i]*GR[i][j]*z[j] for i in range(8) for j in range(8))
    assert (q>0)==any(z)
    positive+=q>0
assert positive==6560
for n,A,divisors in [(20,D,(10,4)),(820,H,(410,164,20))]:
    assert scalar_sign(power(A,n))
    assert all(not scalar_sign(power(A,m)) for m in divisors)
# Constant sign-flip witness, in componentwise multiplication.
one=[1,0,0,0]; minus=[-1,0,0,0]
assert rem(mul(one,conjugate(one,P8)),P8)==rem(mul(minus,conjugate(minus,P8)),P8)
assert (1-1)%41==0 and (1-(-1))%41!=0
for a,b in product(range(41),repeat=2):
    assert ((a*a-2*a*b+b*b)%41==0)==(a==b)
# Synthetic quotient of h by x-19, reduced mod41.
a=list(reversed(Hpoly)); quotient=[a[0]]
for t in a[1:-1]:quotient.append((t+19*quotient[-1])%41)
assert (a[-1]+19*quotient[-1])%41==0
k=list(reversed(quotient)); k=[t%41 for t in k]
assert k==[28,32,33,34,27,6,12,1]
assert all(sum(row[i]*k[i] for i in range(8))%41==0 for row in C)
assert all(t%41==0 for t in rem(mul(k,k),Hpoly)) and k[-1]**2%41==1
print('RESULT-EXPOSED STDLIB CHECK')
print('CRT inclusion, direct cyclotomic conjugation and trace Gram = PASS')
print('positive nonzero ternary vectors checked = 6560')
print('quadratic action exact orders by scalar-kernel test = 20/820')
print('norm-equal seam/anti-seam witness and 1681 residue tests = PASS')
print('nilpotent multiplication/outer-square contrast = PASS')
print('ALL STDLIB CHECKS PASS; no blind-agent or architecture promotion')
