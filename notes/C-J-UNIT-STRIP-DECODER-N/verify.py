#!/usr/bin/env python3
"""Exact finite audit for result-exposed NON-CANONICAL incubation #1269."""
from itertools import product
from math import comb, isqrt

ONE=(1,0,0,0); ZERO=(0,0,0,0); J=(1,0,1,0); JI=(0,-1,-1,0)

def mul(x,y):
    o=[0]*7
    for i,a in enumerate(x):
        for j,b in enumerate(y): o[i+j]+=a*b
    for k in (6,5,4):
        q=o[k]
        for j in range(4): o[k-4+j]-=q
    return tuple(o[:4])

def pw(x,n):
    r=ONE
    while n:
        if n&1:r=mul(r,x)
        x=mul(x,x);n//=2
    return r

def jp(n): return pw(J if n>=0 else JI,abs(n))

def uv(x):
    a,b,c,d=x
    return (a*a-a*b+b*b-b*c+c*c-c*d+d*d,
            a*b-a*c-a*d+b*c-b*d+c*d)

def norm(x):
    u,v=uv(x);return u*u+u*v-v*v

def red(x):
    if x==ZERO:return False
    u,v=uv(x);return v<=0 and u+2*v>0

def fmul(x,y):
    u,v=x;a,b=y
    return u*a+v*b,u*b+v*a+v*b

def ph2(n):
    x=(1,1) if n>=0 else (2,-1); r=(1,0); n=abs(n)
    while n:
        if n&1:r=fmul(r,x)
        x=fmul(x,x);n//=2
    return r

def decode(x):
    a=uv(x)
    def below(m):return fmul(a,ph2(m))[1]<=0
    if below(0):
        lo,hi=0,1
        while below(hi):lo,hi=hi,2*hi
    else:
        lo,hi=-1,0
        while not below(lo):lo,hi=2*lo,lo
    while hi-lo>1:
        m=(lo+hi)//2
        if below(m):lo=m
        else:hi=m
    b=mul(jp(-lo),x)
    assert red(b)
    return lo,b

def coeff_bound(X):return isqrt(isqrt((256*X)//25))

def strip_counts(X):
    B=coeff_bound(X); per=[0]*(X+1)
    for x in product(range(-B,B+1),repeat=4):
        if red(x):
            n=norm(x)
            if 0<n<=X:per[n]+=1
    return B,per

def ideal_counts(limit):
    spf=list(range(limit+1))
    for p in range(2,isqrt(limit)+1):
        if spf[p]==p:
            for q in range(p*p,limit+1,p):
                if spf[q]==q:spf[q]=p
    a=[0]*(limit+1);a[1]=1
    for n in range(2,limit+1):
        p=spf[n];m=n;e=0
        while m%p==0:m//=p;e+=1
        if p==5:loc=1
        elif p%5==1:loc=comb(e+3,3)
        elif p%5==4:loc=e//2+1 if e%2==0 else 0
        else:loc=1 if e%4==0 else 0
        a[n]=a[m]*loc
    return a

def main():
    print('NON-CANONICAL EXACT REGRESSION; result-exposed incubation #1269')
    assert mul(J,JI)==ONE
    z=(0,1,0,0); pi=(1,-1,0,0); ms5=(1,0,2,2)
    assert pw(z,5)==ONE
    assert mul(pi,pi)==mul(ms5,J)
    assert pw(pi,4)==mul((5,0,0,0),jp(2))
    samples=[x for x in product(range(-2,3),repeat=4) if x!=ZERO]
    for x in samples:
        n,b=decode(x);assert mul(jp(n),b)==x;assert norm(b)==norm(x)
        for k in (-50,-5,-1,0,1,5,50):assert decode(mul(jp(k),x))==(n+k,b)
    print('PASS strip normal form and signed J shifts: 624 inputs, 4368 shifts')
    for n in (-10000,-257,-1,0,1,257,10000):assert decode(jp(n))==(n,ONE)
    print('PASS exact half-open boundary powers through +/-10000')
    B,per=strip_counts(1000); ideals=ideal_counts(1000)
    assert B==10
    for n in range(1,1001):assert per[n]==10*ideals[n],(n,per[n],ideals[n])
    s=0; c={}
    for n in range(1,1001):
        s+=per[n]
        if n in (940,941,1000):c[n]=s
    assert c=={940:3110,941:3150,1000:3410}
    print('PASS normwise strip count = 10 * Euler ideal count for norms 1..1000')
    print('PASS cumulative capacities: B_940=3110; B_941=3150; B_1000=3410')
    assert coeff_bound(941)==9
    vals=[]
    for x in product(range(-9,10),repeat=4):
        if red(x) and 0<norm(x)<=941:vals.append((norm(x),x))
    vals.sort();assert len(vals)==3150 and len({x for _,x in vals[:3125]})==3125
    print('PASS explicit ordered 3125-entry integral codebook at norm bound 941')
    print('RESULT PASS; finite capacity evidence remains candidate-C in this notes-only lane')

if __name__=='__main__':main()
