#!/usr/bin/env python3
"""Exact audit of one frozen direct-chart question, NON-CANONICAL."""
from fractions import Fraction as F
from math import isqrt

# Gaussian rationals, independently built raw walk matrices.
def ga(x,y): return (x[0]+y[0],x[1]+y[1])
def gn(x): return (-x[0],-x[1])
def gm(x,y): return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def gc(x): return (x[0],-x[1])
ONE,ZERO=(F(1),F(0)),(F(0),F(0))
def matmul(a,b):
    return tuple(tuple(ga(gm(a[i][0],b[0][j]),gm(a[i][1],b[1][j]))
                       for j in range(2)) for i in range(2))
def dagger(a): return tuple(tuple(gc(a[j][i]) for j in range(2)) for i in range(2))
def determinant(a): return ga(gm(a[0][0],a[1][1]),gn(gm(a[0][1],a[1][0])))
def walk(z):
    zi=gc(z)
    return ((z,gm((0,2),z)),(gm((0,2),zi),zi))

# a+b sqrt(5), exact rationals.
def qa(x,y):return (x[0]+y[0],x[1]+y[1])
def qneg(x):return (-x[0],-x[1])
def qm(x,y):return (x[0]*y[0]+5*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def qnorm(x):return x[0]*x[0]-5*x[1]*x[1]
def qb(x):return (x[0],-x[1])
def qp(x,n):
    if n<0:
        d=qnorm(x);x=(x[0]/d,-x[1]/d);n=-n
    r=(F(1),F(0))
    while n:
        if n&1:r=qm(r,x)
        x=qm(x,x);n//=2
    return r
def qsign(x):
    a,b=x
    if b==0:return (a>0)-(a<0)
    if a==0:return (b>0)-(b<0)
    if a>0 and b>0:return 1
    if a<0 and b<0:return -1
    d=a*a-5*b*b
    assert d!=0
    s=(d>0)-(d<0)
    return s if a>0 else -s
def rational_square(x):
    return x>=0 and isqrt(x.numerator)**2==x.numerator and isqrt(x.denominator)**2==x.denominator

def main():
    for j in range(-64,65):
        t=F(j,16);c=(1-t*t)/(1+t*t);p=2*t/(1+t*t)
        assert c*c+p*p==1
        a=walk((c,p));tr=ga(a[0][0],a[1][1]);det=determinant(a)
        assert matmul(dagger(a),a)==(((F(5),F(0)),ZERO),(ZERO,(F(5),F(0))))
        assert tr==(2*c,0) and det==(5,0)
        discriminant=ga(gm(tr,tr),(-20,0))
        e2=4+p*p
        assert discriminant==(-4*e2,0) and e2-p*p==4
    print('G1 PASS raw_walk_circle_fixtures=129 trace_det_unitarity_shell=exact')
    phi=(F(1,2),F(1,2));admitted=[]
    for n in range(-64,65):
        r,ri=qp(phi,n),qp(phi,-n)
        e,p=qa(r,ri),qa(r,qneg(ri))
        assert qa(qm(e,e),qneg(qm(p,p)))==(4,0)
        assert qm(r,ri)==(1,0)
        assert qb(r)==tuple((-1 if n%2 else 1)*a for a in ri)
        assert qnorm(r)==(-1 if n%2 else 1)
        is_admitted=qsign(qa((F(1),F(0)),qneg(qm(p,p))))>=0
        if is_admitted:admitted.append(n)
        assert is_admitted==(abs(n)<=1)
    assert admitted==[-1,0,1]
    e2=qa(qp(phi,2),qp(phi,-2));p2=qa(qp(phi,2),qneg(qp(phi,-2)))
    assert e2==(3,0) and p2==(0,1) and qm(p2,p2)==(5,0)
    print('G2 PASS rungs=-64..64 admitted=-1,0,1 full_chart_counterexample_n=2 p_squared=5')
    assert qnorm(tuple(2*a for a in phi))==-4
    assert all((a*a+a*b-b*b)%2!=0 for a,b in [(1,0),(0,1),(1,1)])
    common=[];norm4=0
    for a in range(1,33):
        for b in range(-64,65):
            if 2*a+b<=0 or a*a+a*b-b*b!=4:continue
            norm4+=1;assert a%2==b%2==0
            if 5*b*b<=4:common.append((a,b))
    assert common==[(2,0)]
    print(f'G3 PASS positive_norm4_box={norm4} common_O_plus_state=2 signed_odd_rungs=excluded')
    assert not rational_square(F(17)) and not rational_square(F(17,5))
    assert 7*7+7*16-16*16==-95
    assert qnorm((15,F(8)))==-95 # 16 phi+7=15+8 sqrt(5)
    a0,api=walk(ONE),walk((-1,0))
    assert ga(a0[0][0],a0[1][1])==(2,0)
    assert ga(api[0][0],api[1][1])==(-2,0)
    print('G4 PASS sqrt17_not_in_Qsqrt5 bound_curvature_radicand_norm=-95 phase_fold_distinct_traces=2,-2')
    print('DECISION FULL_DIRECT_CHART=REJECTED O_PLUS_MASS2_BRIDGE=REST_ONLY')
    print('DOWNSTREAM same_chart_W_selection_and_spectrum=NOT_REACHED')
    print('STATUS NON-CANONICAL exact audit; analytical proof separate; no independent review')

if __name__=='__main__':main()
