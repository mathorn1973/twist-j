"""Alternate exact phase calculation, result-exposed, no H3 source import."""
from itertools import product,permutations
# Real quadratic ring a+b phi with phi^2=phi+1.
def mul(x,y):
    a,b=x;c,d=y
    return a*c+b*d,a*d+b*c+b*d
T=(2,-1)
def norm(i,a):
    if i<0:return (1,0)
    r=(i-a)%5
    return (0,0) if r==0 else (3,-1) if r in (1,4) else (2,1)
def q(x):
    a,b=x
    return 2*a+b
def coeff(n):
    return (0,0,0,1,-1)[n%5]
def val(n):
    return coeff(n)+coeff(n+2)
# independent integer determinant by Leibniz
M=[[val(i+k) for k in range(1,5)] for i in range(1,5)]
def d(A):
    if len(A)==1:return A[0][0]
    return sum((-1)**i*v*d([r[:i]+r[i+1:] for r in A[1:]]) for i,v in enumerate(A[0]))
assert abs(d(M))==1
for i,k in product(range(-1,5),repeat=2):
    flags=set()
    for a,b in product(range(5),repeat=2):
        A,B=norm(i,a),mul(T,norm(k,b))
        first=A!=(0,0) and B==mul(T,A)
        second=B!=(0,0) and A==mul(T,B)
        assert not second
        if first:
            flags.add((a,b))
    C=tuple(sum((a+b)%5==m for a,b in flags) for m in range(5))
    read=val(C.index(4)) if 4 in C else 0
    assert read==(0 if min(i,k)<0 else val(i+k))
    Q=12*sum(q(norm(i,a)) for a in range(5))+32*sum(q(mul(T,norm(k,b))) for b in range(5))
    print('READ',i,k,*C,'P',read,'Q',Q)
