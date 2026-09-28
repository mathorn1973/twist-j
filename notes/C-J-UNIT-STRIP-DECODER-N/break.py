#!/usr/bin/env python3
"""Same-session adversarial checks for incubation #1269.

Not blind: the author had already seen verify.py. This is therefore a separate
implementation attack, not independent confirmation.
"""
from itertools import product
from math import comb, isqrt


def uv(x):
    a,b,c,d=x
    return (
        a*a-a*b+b*b-b*c+c*c-c*d+d*d,
        a*b-a*c-a*d+b*c-b*d+c*d,
    )


def nn(x):
    u,v=uv(x)
    return u*u+u*v-v*v


def reduced(x):
    if x==(0,0,0,0): return False
    u,v=uv(x)
    return v<=0 and u+2*v>0


def fourth_root_floor_ratio_256_25(X):
    return isqrt(isqrt((256*X)//25))


def ideal_counts(limit):
    a=[0]*(limit+1); a[1]=1
    for n in range(2,limit+1):
        m=n; val=1; p=2
        while p*p<=m:
            if m%p:
                p+=1
                continue
            e=0
            while m%p==0:
                m//=p; e+=1
            if p==5: local=1
            elif p%5==1: local=comb(e+3,3)
            elif p%5==4: local=(e//2+1) if e%2==0 else 0
            else: local=1 if e%4==0 else 0
            val*=local
            p+=1
        if m>1:
            p=m; e=1
            if p==5: local=1
            elif p%5==1: local=4
            elif p%5==4: local=0
            else: local=0
            val*=local
        a[n]=val
    return a


def count_box(X):
    B=fourth_root_floor_ratio_256_25(X)
    per=[0]*(X+1)
    for x in product(range(-B,B+1), repeat=4):
        if reduced(x):
            n=nn(x)
            if 0<n<=X: per[n]+=1
    return B,per


def main():
    print('NON-BLIND BREAKER; NON-CANONICAL incubation #1269')
    B,per=count_box(1000)
    ideals=ideal_counts(1000)
    assert B==10
    for n in range(1,1001):
        assert per[n]==10*ideals[n], (n,per[n],ideals[n])
    cum=[]; s=0
    for n in range(1,1001):
        s+=per[n]; cum.append(s)
    assert cum[939]==3110
    assert cum[940]==3150
    assert cum[999]==3410
    assert fourth_root_floor_ratio_256_25(941)==9
    bad=[]
    for x in product(range(-10,11), repeat=4):
        if max(map(abs,x))!=10: continue
        if reduced(x) and 0<nn(x)<=941: bad.append(x)
    assert not bad, bad[:1]
    print('PASS independent-factor count at every norm 1..1000')
    print('PASS cumulative strip counts: 3110 at 940; 3150 at 941; 3410 at 1000')
    print('PASS coefficient-bound attack: no norm<=941 reduced point on coordinate shell 10')
    print('RESULT BREAKER PASS; no frozen finite falsifier found')


if __name__=='__main__':
    main()
