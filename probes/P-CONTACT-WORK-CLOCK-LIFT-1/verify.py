#!/usr/bin/env python3
"""Exact finite audit of the declared work/clock suspension. Apache-2.0.

NON-CANONICAL / L1. A. M. Thorn, 2026-11-05.
Universal continuous assertions are proved in PROOF.md, not sampled here.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
import json


def add(a, b):
    return tuple(x+y for x,y in zip(a,b))


def neg(a):
    return tuple(-x for x in a)


def scale(n, a):
    return tuple(n*x for x in a)


def mul(a, b):
    c=[0]*7
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j]+=x*y
    for k in range(6,3,-1):
        for i in range(4):
            c[k-4+i]-=c[k]
    return tuple(c[:4])


ZERO=(0,0,0,0)
ONE=(1,0,0,0)
J=(0,1,0,0)
RHO=(0,0,1,0)
U=(1,-1,0,0)
OMEGA=((0,1,0,0),(-1,0,1,0),(0,-1,0,1),(0,0,-1,0))
GRAM=tuple(tuple(5*int(i==j)-1 for j in range(4)) for i in range(4))


@lru_cache(maxsize=None)
def q(a):
    v=5*sum(x*x for x in a)-sum(a)**2
    assert v%2==0
    return v//2


@lru_cache(maxsize=None)
def contact(a,b):
    difference=add(a,neg(b))
    if any(x%2 for x in difference):
        return a,b
    s=tuple((x+y)//2 for x,y in zip(a,b))
    d=tuple(x//2 for x in difference)
    rd=mul(RHO,d)
    return add(s,rd),add(s,neg(rd))


def energy(w,lam):
    return sum(q(x) for x in w)+lam*q(add(w[1],neg(w[2])))


def tags(w,b,lam):
    r=sum(q(x) for x in w)
    epsilon=not any(x%2 for x in add(w[0],neg(w[1])))
    delta=energy(w,lam)+b >= (1+2*lam)*r
    return epsilon,delta


def endpoint(w,b,c,lam,inverse=False):
    eps,delta=tags(w,b,lam)
    old=energy(w,lam)
    if eps and delta:
        x,y=w[:2]
        for _ in range(4 if inverse else 1):
            x,y=contact(x,y)
        new=(x,y,w[2])
    else:
        new=w
    result=(new,b+old-energy(new,lam),(c+(-1 if inverse else 1))%5)
    assert tags(result[0],result[1],lam)==(eps,delta)
    return result


def transpose(a):
    return tuple(zip(*a))


def mm(a,b):
    return tuple(tuple(sum(x*y for x,y in zip(row,col)) for col in zip(*b)) for row in a)


def eye(n):
    return tuple(tuple(F(i==j) for j in range(n)) for i in range(n))


def inverse(a):
    n=len(a)
    rows=[list(map(F,row))+list(eye(n)[i]) for i,row in enumerate(a)]
    for k in range(n):
        pivot=next(i for i in range(k,n) if rows[i][k])
        rows[k],rows[pivot]=rows[pivot],rows[k]
        factor=rows[k][k]
        rows[k]=[x/factor for x in rows[k]]
        for i in range(n):
            if i!=k:
                factor=rows[i][k]
                rows[i]=[x-factor*y for x,y in zip(rows[i],rows[k])]
    return tuple(tuple(row[n:]) for row in rows)


def power(a,n):
    b=eye(len(a))
    for _ in range(n):
        b=mm(b,a)
    return b


def block_diag(blocks):
    n=sum(len(b) for b in blocks)
    out=[[F(0)]*n for _ in range(n)]
    offset=0
    for b in blocks:
        for i,row in enumerate(b):
            for j,x in enumerate(row):
                out[offset+i][offset+j]=F(x)
        offset+=len(b)
    return tuple(map(tuple,out))


def matrix_from_multiplier(multiplier):
    cols=[mul(multiplier,tuple(int(i==j) for i in range(4))) for j in range(4)]
    return transpose(cols)


def pair_matrix(m):
    out=[list(row) for row in eye(12)]
    for i in range(4):
        for j in range(4):
            a=F(int(i==j)+m[i][j],2)
            b=F(int(i==j)-m[i][j],2)
            out[i][j]=out[4+i][4+j]=a
            out[i][4+j]=out[4+i][j]=b
    return tuple(map(tuple,out))


# Sparse polynomials in 24 independent formal gradient variables.
def pc(v):
    return {():F(v)} if v else {}


def pv(i):
    return {(i,):F(1)}


def pa(a,b):
    out=dict(a)
    for term,v in b.items():
        out[term]=out.get(term,F(0))+v
        if not out[term]:
            del out[term]
    return out


def pn(a):
    return {t:-v for t,v in a.items()}


def pm(a,b):
    out={}
    for t,x in a.items():
        for u,y in b.items():
            term=tuple(sorted(t+u))
            out[term]=out.get(term,F(0))+x*y
            if not out[term]:
                del out[term]
    return out


def ps(values):
    out={}
    for a in values:
        out=pa(out,a)
    return out


def pmm(a,b):
    return tuple(tuple(ps(pm(x,y) for x,y in zip(row,col)) for col in zip(*b)) for row in a)


def formal_clock_audit():
    base=block_diag([OMEGA]*3)
    inv=inverse(base)
    product_form=block_diag([base,((0,1),(-1,0))])
    grad_e=[pv(i) for i in range(12)]
    grad_h=[pv(12+i) for i in range(12)]
    mixed=[pa(a,pn(b)) for a,b in zip(grad_e,grad_h)]
    jac=[[pc(v) for v in row] for row in eye(14)]
    for i in range(12):
        jac[13][i]=mixed[i]
    pulled=pmm(pmm(transpose(jac),tuple(tuple(pc(v) for v in row) for row in product_form)),jac)
    expected=[[pc(v) for v in row] for row in product_form]
    for i in range(12):
        expected[i][12]=pn(mixed[i])
        expected[12][i]=mixed[i]
    assert pulled==tuple(map(tuple,expected))
    field=[pn(ps(pm(pc(inv[i][j]),grad_h[j]) for j in range(12))) for i in range(12)]
    velocity=field+[pc(1),pn(ps(pm(grad_e[i],field[i]) for i in range(12)))]
    product=pmm(pulled,tuple((v,) for v in velocity))
    target=[pn(x) for x in grad_e]+[{},pc(-1)]
    assert [row[0] for row in product]==target
    assert not ps(pm(grad_h[i],field[i]) for i in range(12))
    print('PASS FORMAL_CLOCK pullback=14x14 Hamilton_equation=all_polynomial_coefficients variables=24')


def matrix_audit():
    rho=matrix_from_multiplier(RHO)
    half=matrix_from_multiplier(neg(J))
    assert mm(mm(transpose(rho),OMEGA),rho)==OMEGA
    assert power(rho,5)==eye(4)
    assert mm(half,half)==rho
    assert power(half,5)==tuple(tuple(-x for x in row) for row in eye(4))
    assert power(half,10)==eye(4)
    assert all(half!=power(rho,k) for k in range(5))
    contact_matrix=pair_matrix(rho)
    half_matrix=pair_matrix(half)
    omega=block_diag([OMEGA]*3)
    assert mm(mm(transpose(contact_matrix),omega),contact_matrix)==omega
    assert mm(mm(transpose(half_matrix),omega),half_matrix)==omega
    assert mm(half_matrix,half_matrix)==contact_matrix
    assert power(contact_matrix,5)==eye(12)
    assert mm(mm(transpose(rho),GRAM),rho)==GRAM
    base=block_diag([GRAM]*3)
    interaction=[[F(0)]*12 for _ in range(12)]
    for i in range(4):
        for j in range(4):
            for a,b,sign in ((4,4,1),(8,8,1),(4,8,-1),(8,4,-1)):
                interaction[a+i][b+j]=sign*GRAM[i][j]
    dimensions=[]
    for lam in (0,1,2,7):
        hessian=tuple(tuple(base[i][j]+lam*interaction[i][j] for j in range(12)) for i in range(12))
        changed=mm(mm(transpose(contact_matrix),hessian),contact_matrix)
        diff=tuple(tuple(changed[i][j]-hessian[i][j] for j in range(12)) for i in range(12))
        assert any(v for row in diff for v in row)==bool(lam)
        # Full symbolic Jacobian pullback of the naive lift.
        gradient=[ps(pm(pc(diff[i][j]),pv(j)) for j in range(12)) for i in range(12)]
        product_form=block_diag([omega,((0,1),(-1,0))])
        jac=[[pc(0) for _ in range(14)] for _ in range(14)]
        for i in range(12):
            for j in range(12):
                jac[i][j]=pc(contact_matrix[i][j])
        jac[12][12]=pc(1); jac[13][13]=pc(1)
        for j in range(12):
            jac[13][j]=pn(gradient[j])
        pulled=pmm(pmm(transpose(jac),tuple(tuple(pc(v) for v in row) for row in product_form)),jac)
        expected=[[pc(v) for v in row] for row in product_form]
        for j in range(12):
            expected[12][j]=pn(gradient[j]); expected[j][12]=gradient[j]
        assert pulled==tuple(map(tuple,expected))
        dimensions.append(lam)
    print('PASS MATRICES primitive_form=preserved contact_order=5 half_order=10 half_square=contact')
    print('PASS PRODUCT_DEFECT lambda='+','.join(map(str,dimensions))+' zero_iff_lambda_zero=True')


def finite_audit():
    values={ZERO,ONE,scale(2,ONE)}
    value=U
    for _ in range(5):
        values.update((value,neg(value)))
        value=mul(RHO,value)
    assert len(values)==13
    counts={'cases':0,'active':0,'parity_hold':0,'funding_hold':0,'cycle_checks':0}
    for w in product(sorted(values),repeat=3):
        r=sum(q(x) for x in w)
        interaction=q(add(w[1],neg(w[2])))
        assert 0<=interaction<=2*r
        for lam in (0,1,2,7):
            threshold=max(0,lam*(2*r-interaction))
            for b in sorted({0,1,5,10,20,60,120,400,threshold}):
                eps,delta=tags(w,b,lam)
                assert delta==(b>=threshold)
                result=endpoint(w,b,0,lam)
                nw,nb,nc=result
                assert nb>=0 and nc==1
                assert energy(nw,lam)+nb==energy(w,lam)+b
                assert sum(q(x) for x in nw)==r
                assert endpoint(nw,nb,nc,lam,True)==(w,b,0)
                if eps and delta:
                    x,y=contact(w[0],w[1])
                    assert nw==(x,y,w[2])
                    counts['active']+=1
                else:
                    assert nw==w and nb==b
                    counts['parity_hold' if not eps else 'funding_hold']+=1
                state=(w,b,0)
                for _ in range(5):
                    state=endpoint(*state,lam)
                assert state==(w,b,0)
                counts['cases']+=1; counts['cycle_checks']+=1
    print('PASS FINITE '+json.dumps(counts,sort_keys=True,separators=(',',':')))


def witnesses():
    minus_ju=neg(mul(J,U))
    state=(U,neg(U),minus_ju)
    # Selected half snapshot, not a native isolated contact power.
    half=(minus_ju,neg(minus_ju),minus_ju)
    x,y=contact(state[0],state[1]); end=(x,y,state[2])
    accounts=[q(add(w[1],neg(w[2]))) for w in (state,half,end)]
    assert accounts==[15,20,15]
    assert [sum(q(v) for v in w) for w in (state,half,end)]==[15,15,15]
    for lam in (0,1,2,7):
        e=[energy(w,lam) for w in (state,half,end)]
        assert [e[0]-v for v in e]==[0,-5*lam,0]
        assert [5*lam+e[0]-v for v in e]==[5*lam,0,5*lam]
        # Original endpoint guard sees zero cost but this chosen path may fail.
        assert e[0]==e[2]
        for c in range(5):
            active_bank=max(0,lam*(30-15))
            nw,nb,nc=endpoint(state,active_bank,c,lam)
            assert endpoint(nw,nb,nc,lam,True)==(state,active_bank,c)
    work_state=(U,neg(U),U)
    after=[]
    for lam in (1,2):
        assert tags(work_state,60,lam)==(True,True)
        result=endpoint(work_state,60,0,lam)
        assert result[1]-60==10*lam
        for c in range(5):
            clock_result=endpoint(work_state,60,c,lam)
            assert clock_result[1]-60==10*lam
            assert endpoint(*clock_result,lam,inverse=True)==(work_state,60,c)
        after.append(result)
    assert after[0][0]==after[1][0] and after[0][2]==after[1][2]
    print('PASS RESERVE R=15 interaction=15,20,15 sharp_path_reserve=5lambda endpoint_payment=0')
    print('PASS FREE_COEFFICIENT lambda=1,2 common_bank=60 same_contact_clock=True bank_gains=10,20')


def main():
    if not __debug__:
        raise RuntimeError('Assertions must be enabled')
    print('P-CONTACT-WORK-CLOCK-LIFT-1 NON-CANONICAL L1 EXACT')
    matrix_audit()
    formal_clock_audit()
    finite_audit()
    witnesses()
    print('RESULT PASS; continuous claims require PROOF.md; no native or physical alpha claim')


if __name__=='__main__':
    main()
