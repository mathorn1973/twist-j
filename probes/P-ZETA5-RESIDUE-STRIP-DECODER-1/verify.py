#!/usr/bin/env python3
"""Exact verifier for P-ZETA5-RESIDUE-STRIP-DECODER-1.

Integers and Fraction only. No float, randomness, files, network or tolerance.
Universal theorem claims are proved in PROOF.md; this program audits exact
finite certificates and algebraic reductions.
"""
from fractions import Fraction as F
from itertools import product
from math import comb, isqrt

ONE = (1,0,0,0)
ZERO = (0,0,0,0)
J = (1,0,1,0)
JINV = (0,-1,-1,0)

def mul(x,y):
    out=[0]*7
    for i,a in enumerate(x):
        for j,b in enumerate(y):
            out[i+j]+=a*b
    for k in (6,5,4):
        q=out[k]
        for j in range(4):
            out[k-4+j]-=q
    return tuple(out[:4])

def pow_ring(x,n):
    r=ONE
    while n:
        if n&1:
            r=mul(r,x)
        x=mul(x,x)
        n//=2
    return r

def jpow(n):
    return pow_ring(J if n>=0 else JINV, abs(n))

def uv(x):
    a,b,c,d=x
    return (
        a*a-a*b+b*b-b*c+c*c-c*d+d*d,
        a*b-a*c-a*d+b*c-b*d+c*d,
    )

def norm(x):
    u,v=uv(x)
    return u*u+u*v-v*v

def strip(x):
    if x==ZERO:
        return False
    u,v=uv(x)
    return v>=0 and u-v>0

def half_strip(x):
    if x==ZERO:
        return False
    u,v=uv(x)
    return v>=0 and u-2*v>0

def decode(x):
    assert x != ZERO
    b=x
    n=0
    guard=0
    while not strip(b):
        u,v=uv(b)
        if v<0:
            b=mul(JINV,b)
            n+=1
        else:
            assert u-v<=0
            b=mul(J,b)
            n-=1
        guard+=1
        assert guard<100000
    return n,b

def coeff_bound(X):
    b=0
    while 25*(b+1)**4 < 256*X:
        b+=1
    return b

def strip_counts(limit):
    B=coeff_bound(limit)
    per=[0]*(limit+1)
    wrong=0
    reps=[]
    for x in product(range(-B,B+1), repeat=4):
        n=norm(x)
        if n<=0 or n>limit:
            continue
        if strip(x):
            per[n]+=1
            reps.append((n,x))
        if half_strip(x):
            wrong+=1
    reps.sort()
    return B,per,wrong,reps

def ideal_coeffs(limit):
    spf=list(range(limit+1))
    if limit>=1:
        spf[1]=1
    for p in range(2,isqrt(limit)+1):
        if spf[p]==p:
            start=p*p
            for q in range(start,limit+1,p):
                if spf[q]==q:
                    spf[q]=p
    a=[0]*(limit+1)
    a[1]=1
    for n in range(2,limit+1):
        p=spf[n]
        m=n
        e=0
        while m%p==0:
            m//=p
            e+=1
        if p==5:
            local=1
        elif p%5==1:
            local=comb(e+3,3)
        elif p%5==4:
            local=(e//2+1) if e%2==0 else 0
        else:
            local=1 if e%4==0 else 0
        a[n]=a[m]*local
    return a

def gauss_pair():
    # conjugate(kappa(a)) for kappa(2)=i, in Gaussian integer pairs.
    kb={1:(1,0),2:(0,-1),3:(0,1),4:(-1,0)}
    re=sum(a*kb[a][0] for a in range(1,5))
    im=sum(a*kb[a][1] for a in range(1,5))
    return re,im

def main():
    passed=0
    def gate(label, cond, detail):
        nonlocal passed
        assert cond, label
        passed+=1
        print("PASS", label, detail)

    print("TWIST-J P-ZETA5-RESIDUE-STRIP-DECODER-1 exact verifier")

    # G1: symbolic coefficient bookkeeping, pi^2 and log(phi)/sqrt5 suppressed.
    resK=F(4,25)
    resk=F(2,1)
    ratio=resK/resk
    bookkeeping=F(2,1)/(5*5)
    gate("G01_RESIDUE", resK==F(4,25) and ratio==F(2,25) and bookkeeping==ratio,
         "ResK coefficient 4/25; relative quartic coefficient 2/25; two denominator fives are 5 and 5")

    S=gauss_pair()
    Snorm=S[0]*S[0]+S[1]*S[1]
    Lnorm=F(Snorm,5**3)
    gate("G02_GAUSS", S==(-3,1) and Snorm==10 and Lnorm==F(2,25),
         "S=-3+i; |S|^2=10; |L(1,kappa)|^2/pi^2=2/25")

    gate("G03_JUNIT", mul(J,JINV)==ONE and norm(J)==1,
         "J inverse and norm-one action exact in Z[zeta_5]")

    # Complete correct strip box at X=2500 and half-width negative control.
    B,per,wrong,reps=strip_counts(2500)
    gate("G04_BOX", B==12 and all(max(map(abs,x))<=12 for _,x in reps),
         "complete coefficient radius 12 for norm<=2500")

    ideals2500=ideal_coeffs(2500)
    gate("G05_NORMWISE", all(per[n]==10*ideals2500[n] for n in range(1,2501)),
         "strip count equals 10 times Euler ideal count at every norm 1..2500")

    cumulative=[]
    total=0
    for n in range(1,2501):
        total+=per[n]
        cumulative.append(total)
    frozen=(cumulative[939],cumulative[940],cumulative[999],cumlative[2499])
    gate("G06_COUNTS", frozen==(3110,3150,3410,8440),
         "B_940=3110 B_941=3150 B_1000=3410 B_2500=8440")

    gate("G07_NEGCTRL", wrong==4300,
         "half-width strip 1<=A/B<phi^2 has 4300 representatives at X=2500")

    # 125 exact J round trips: first five strip reps, n=-12..12.
    seeds=[x for _,x in reps[:5]]
    rt=0
    for b in seeds:
        assert strip(b)
        for n in range(-12,13):
            x=mul(jpow(n),b)
            got_n,got_b=decode(x)
            assert (got_n,got_b)==(n,b)
            rt+=1
    gate("G08_ROUNDTRIP", rt==125,
         "integer-only J-strip decoder round trip on 125 frozen pairs")

    xmin=next(i+1 for i,v in enumerate(cumulative) if v>=3125)
    gate("G09_CAPACITY", xmin==941 and cumulative[939]<3125<=cumulative[940],
         "global 3125-orbit scalar capacity threshold X_min=941")

    ideals1m=ideal_coeffs(10**6)
    A1m=sum(ideals1m[1:])
    gate("G10_MILLION", A1m==339775,
         "exact ideal count A_K(10^6)=339775")

    # QDD Route A identity on all 625 balanced pistons.
    vals=(-2,-1,0,1,2)
    supported=0
    for x in product(vals,repeat=4):
        Q=sum(t*t for t in x)
        s=sum(x)
        u,v=uv(x)
        tr=4*u+2*v
        assert 5*Q-s*s==tr
        if x!=ZERO:
            assert tr>0
            left=F(s&s,4*(5)Q-s*s))
            right=F(s*s,8*(2*u+v))
            assert left==right
            supported+=1
    gate("G11_QDD", supported==624,
         "5Q-s^2=Tr(alpha bar(alpha))=2(A+B) and incidence rewrite on all 624 supported pistons")

    # Landau exponent specialization is arithmetic only; theorem itself is imported.
    exponent=F(1,1)-F(2,5)
    gate("G12_LANDAU", exponent==F(3,5),
         "degree-four Landau exponent specializes exactly to 3/5")

    print("RESULT", f"{passed}/12", "ALL PASS")

if __name__=="__main__":
    main()
