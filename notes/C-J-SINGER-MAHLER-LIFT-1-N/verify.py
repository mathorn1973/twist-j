#!/usr/bin/env python3
"""Exact certificates for C-J-SINGER-MAHLER-LIFT-1-N.

No floating point is used.  The script proves the finite A2/A3 classification
used in the builder report and prints the short Routh/compound certificates
for the A0/A1 witnesses.  It is incubation code and has no public authority.
"""
from fractions import Fraction as F


def trim(p):
    p = [F(x) for x in p]
    while len(p) > 1 and p[0] == 0:
        p.pop(0)
    return p


def deriv(p):
    n = len(p) - 1
    return trim([p[i] * (n-i) for i in range(n)]) if n else [F(0)]


def divrem(a, b):
    a, b = trim(a), trim(b)
    if b == [0]:
        raise ZeroDivisionError
    q = [F(0)] * max(1, len(a)-len(b)+1)
    r = a[:]
    while r != [0] and len(r) >= len(b):
        k = len(r)-len(b)
        t = r[0]/b[0]
        q[len(q)-1-k] += t
        sub = [t*x for x in b] + [F(0)]*k
        r = trim([x-y for x,y in zip(r, sub)])
    return trim(q), trim(r)


def sturm(p):
    out = [trim(p), deriv(trim(p))]
    while out[-1] != [0]:
        _, r = divrem(out[-2], out[-1])
        if r == [0]:
            break
        out.append([-x for x in r])
    return out


def sgn(x):
    return (x > 0) - (x < 0)


def evalp(p, x):
    y = F(0)
    for a in p:
        y = y*x+a
    return y


def variation(signs):
    signs = [x for x in signs if x]
    return sum(signs[i] != signs[i-1] for i in range(1, len(signs)))


def var_at(seq, x=None, infinity=0):
    signs=[]
    for p in seq:
        if infinity:
            v=sgn(p[0])
            if infinity < 0 and (len(p)-1) % 2:
                v=-v
        else:
            v=sgn(evalp(p,F(x)))
        signs.append(v)
    return variation(signs)


def remove_linear(p, root):
    """Remove all copies of (x-root), returning polynomial and multiplicity."""
    p=trim(p); n=0
    fac=[F(1),-F(root)]
    while evalp(p,F(root)) == 0 and len(p)>1:
        q,r=divrem(p,fac)
        assert r == [0]
        p=q; n+=1
    return p,n


def q_outside_count(a,b,c):
    """Distinct real roots of compound cubic in (-inf,-3) U (3,inf)."""
    q=[1,-b,a*c-4,4*b-a*a-c*c]
    q,mminus=remove_linear(q,-3)
    q,mplus=remove_linear(q,3)
    seq=sturm(q)
    left=var_at(seq,infinity=-1)-var_at(seq,x=-3)
    right=var_at(seq,x=3)-var_at(seq,infinity=1)
    return left+right,mminus,mplus


def routh_quartic(a,b,c):
    """Exact RHP count after w=(z-1)/(z+1); nondegenerate cases only."""
    d4=F(2-a+b-c)       # f(-1)
    d3=F(-2*a+2*c)
    d2=F(12-2*b)
    d1=F(2*a-2*c)
    d0=F(2+a+b+c)       # f(1)
    assert d4 and d3
    e2=(d3*d2-d4*d1)/d3
    assert e2
    e3=(e2*d1-d3*d0)/e2
    assert e3 and d0
    col=[d4,d3,e2,e3,d0]
    changes=sum((col[i]>0)!=(col[i+1]>0) for i in range(4))
    return changes,col


def gf2_deg(x): return x.bit_length()-1


def gf2_mod(a,m):
    while a and gf2_deg(a)>=gf2_deg(m):
        a ^= m << (gf2_deg(a)-gf2_deg(m))
    return a


def gf2_mul(a,b,m):
    z=0
    while b:
        if b&1: z ^= a
        b >>= 1; a <<= 1
    return gf2_mod(z,m)


def gf2_pow(a,n,m):
    z=1
    while n:
        if n&1: z=gf2_mul(z,a,m)
        a=gf2_mul(a,a,m); n//=2
    return z


def gf2_gcd(a,b):
    while b: a,b=b,gf2_mod(a,b)
    return a


def primitive_quartic(m):
    x=0b10
    irreducible=(gf2_pow(x,16,m)==x and gf2_gcd(gf2_pow(x,4,m)^x,m)==1)
    order15=(gf2_pow(x,15,m)==1 and gf2_pow(x,5,m)!=1 and gf2_pow(x,3,m)!=1)
    return irreducible,order15


def fmt(q):
    return "/".join(map(str,(q.numerator,q.denominator))) if q.denominator!=1 else str(q.numerator)


def mulp(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]+=F(x)*F(y)
    return trim(out)


def parity_class(a,b,c):
    if a%2==0 and b%2==0 and c%2==1: return "p_L"
    if a%2==1 and b%2==0 and c%2==0: return "p_R"
    return None


def main():
    # R=(3+sqrt(5))/2.  The frozen coefficient theorem gives
    # |a|,|c| <= 4R and |b| <= 6R.  These two squared integer checks prove
    # 4R=6+2sqrt(5)<11 and 6R=9+3sqrt(5)<16.
    assert 20 < 25 and 45 < 49
    print("Window completeness: 4R<11 and 6R<16 by 20<25 and 45<49: PASS")

    pL=0b10011; pR=0b11001
    assert primitive_quartic(pL)==(True,True)
    assert primitive_quartic(pR)==(True,True)
    print("GF2 controls: p_L and p_R irreducible and order 15: PASS")

    named={
        "A0 lower":(-2,0,1),
        "A0 tie":(-2,4,-3),
        "A1 lower":(-1,0,0),
        "A1 tie":(3,4,2),
        "J":(-3,4,-2),
    }
    for name,(a,b,c) in named.items():
        assert parity_class(a,b,c) in ("p_L","p_R")
        n,col=routh_quartic(a,b,c)
        print(name,(a,b,c),"outside",n,"Routh",[fmt(x) for x in col],
              "Q",[1,-b,a*c-4,4*b-a*a-c*c])
        assert n==2

    assert parity_class(*named["A0 lower"])=="p_L"
    assert parity_class(*named["A0 tie"])=="p_L"
    assert parity_class(*named["A1 lower"])=="p_R"
    assert parity_class(*named["A1 tie"])=="p_R"
    assert parity_class(*named["J"])=="p_R"

    # Exact compound-cubic certificates for the strict witnesses and ties.
    # A0 lower: Q=(z+1)(z^2-z-5).  Its nontrivial roots are
    # (1+-sqrt(21))/2.  Since 4<sqrt(21)<5, one lies in (2,3) and
    # the other in (-2,-3/2); the last root is -1.
    assert mulp([1,1],[1,-1,-5])==[1,0,-6,-5]
    assert 16 < 21 < 25
    # A1 lower: Q=z^3-4z-1 has one root in each listed interval.
    q1=[1,0,-4,-1]
    q1_signs=[evalp(q1,F(x)) for x in (-2,-1,0,2,3)]
    assert q1_signs==[-1,2,-1,-1,14]
    # Every tie and J has Q=(z-3)(z^2-z-1).  The quadratic roots lie
    # strictly in (-2,2), while z=3 gives R and R^-1 exactly.
    assert mulp([1,-3],[1,-1,-1])==[1,-4,2,3]
    assert evalp([1,-1,-1],F(-2))==5
    assert evalp([1,-1,-1],F(-1))==1
    assert evalp([1,-1,-1],F(1))==-1
    assert evalp([1,-1,-1],F(2))==1
    print("Witness/tie compound comparisons against R: PASS")

    # Complete A2 finite window: a=-3, b,c even in the frozen bounds.
    no_q_out=[]; q_out=[]
    for b in range(-14,15,2):
        for c in range(-10,11,2):
            n,mm,mp=q_outside_count(-3,b,c)
            if n:
                q_out.append((b,c,n,mm,mp))
            else:
                outside,col=routh_quartic(-3,b,c)
                no_q_out.append((b,c,outside,col,mm,mp))
    assert len(q_out)==127 and len(no_q_out)==38
    survivors=[x for x in no_q_out if x[2]==2]
    assert [(x[0],x[1]) for x in survivors]==[(4,-2)]
    print("A2 exact split: total=165 Q-outside=127 residual=38")
    print("A2 residual Routh counts:",
          {k:sum(x[2]==k for x in no_q_out) for k in range(5)})
    print("A2 sole two-outside survivor:",(survivors[0][0],survivors[0][1]),
          [fmt(x) for x in survivors[0][3]],"Q endpoint multiplicities",survivors[0][4:])

    # Complete A3 finite window: c=2-b, with both frozen coefficient bounds.
    a3=[]
    for b in range(-14,15,2):
        c=2-b
        if -10<=c<=10:
            n,mm,mp=q_outside_count(-3,b,c)
            a3.append((b,c,n,mm,mp))
    assert len(a3)==11
    assert [(b,c) for b,c,n,mm,mp in a3 if n==0]==[(4,-2)]
    print("A3 exact split: total=11; only no-Q-outside pair=(4,-2)")
    print("A3 rows:",a3)
    print("ALL EXACT ASSERTIONS PASS")


if __name__=="__main__": main()
