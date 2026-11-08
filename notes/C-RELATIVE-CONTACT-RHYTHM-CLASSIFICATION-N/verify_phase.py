#!/usr/bin/env python3
"""Integer checks of the depth marker and sharp account bounds.

NON-CANONICAL / L1. Adapted from the already exposed 2026-11-02 review audit.
No imports from other verifiers; this is not a new independent review.
Computational statements and stdout are unchanged from that source.
"""
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
Z=(0,0,0,0)
ONE=(1,0,0,0)
RHO=(0,0,1,0)

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def scale(n,a): return tuple(n*x for x in a)
def mul(a,b):
    c=[0]*7
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    for i in range(6,3,-1):
        z=c[i]
        c[i]=0
        for k in range(1,5): c[i-k]-=z
    return tuple(c[:4])
def Q(a):
    numerator=5*sum(x*x for x in a)-sum(a)**2
    assert numerator%2==0
    return numerator//2
def valuation(a):
    if not any(a): return None  # infinity, kept nonnumeric
    v=[]
    for x in a:
        if x:
            n=0
            while x%2==0:
                n+=1
                x//=2
            v.append(n)
    return min(v)
def h(x):
    values=[valuation(sub(x[0],x[1])),valuation(sub(x[1],x[2]))]
    finite=[v for v in values if v is not None]
    return min(finite) if finite else None
def contact(a,b):
    delta=sub(a,b)
    if any(x%2 for x in delta): return a,b
    center=tuple((x+y)//2 for x,y in zip(a,b))
    rel=mul(RHO,tuple(x//2 for x in delta))
    return add(center,rel),sub(center,rel)
def F(x):
    a,b,c=x
    a,b=contact(a,b)
    b,c=contact(b,c)
    return a,b,c
def S(x): return add(add(x[0],x[1]),x[2])
def E(x): return sum(Q(a) for a in x)
def M(x): return Q(sub(x[0],x[1]))+Q(sub(x[1],x[2]))+Q(sub(x[0],x[2]))
def pi(a): return sum(a)%5
def A(d): return (4**(d+1)-1)//3

def orbit(initial,limit=40000):
    history=[]
    seen=set()
    x=initial
    while x not in seen:
        seen.add(x)
        history.append(x)
        assert S(x)==S(initial) and E(x)==E(initial) and M(x)==M(initial)
        assert M(x)==3*E(x)-Q(S(x))
        x=F(x)
        if len(history)>limit: raise AssertionError('declared finite check limit exceeded')
    assert x==initial
    markers=[h(x) for x in history]
    if markers==[None]: return {'P':1,'d':None,'h':markers,'M':0},history
    assert all(value is not None for value in markers)
    d=max(markers)
    maxima=[n for n,v in enumerate(markers) if v==d]
    gaps=[(maxima[(i+1)%len(maxima)]-n)%len(history) or len(history)
          for i,n in enumerate(maxima)]
    return {'P':len(history),'d':d,'h':markers,'maximal_phases':maxima,
            'cyclic_maximal_phase_gaps':gaps,'M':M(initial),'E':E(initial),
            'S':S(initial),'pi_slots':[pi(a) for a in initial]},history

def main():
    failures=[]
    checks=[]
    def check(name,passed):
        checks.append({'name':name,'passed':bool(passed)})
        if not passed: failures.append(name)
    witness,wh=orbit((scale(4,ONE),Z,scale(2,ONE)))
    check('integer_4_0_2_P25_d1_M48',witness['P']==25 and witness['d']==1 and witness['M']==48)
    check('integer_4_0_2_h_iff_5_divides_n',witness['h']==[int(n%5==0) for n in range(25)])
    w=(1,-1,0,0)
    v=(2,-1,-1,0)
    X=(scale(6,w),Z,Z)
    Y=(add(scale(2,w),scale(2,v)),sub(scale(2,w),scale(2,v)),scale(2,w))
    xr,xhist=orbit(X)
    yr,yhist=orbit(Y)
    check('Qw5_Qv15',Q(w)==5 and Q(v)==15)
    check('same_E180_S6w_M360',E(X)==E(Y)==180 and S(X)==S(Y)==scale(6,w) and M(X)==M(Y)==360)
    check('different_P5_P25_same_d1',xr['P']==5 and yr['P']==25 and xr['d']==yr['d']==1)
    check('same_full_depth_history_period5',all(xr['h'][n%5]==yr['h'][n%25]==int(n%5==0) for n in range(25)))
    check('same_zero_pi_every_slot_every_phase',all([pi(a) for a in state]==[0,0,0] for state in xhist+yhist))
    coefficient_mod5_X=[[c%5 for c in a] for a in X]
    coefficient_mod5_Y=[[c%5 for c in a] for a in Y]
    check('coefficient_mod5_readings_are_distinct',coefficient_mod5_X!=coefficient_mod5_Y)
    families=[]
    for d in range(6):
        factor=2**d
        for family,initial,expected_p,expected_m in (
            ('I',(scale(factor,ONE),Z,Z),A(d),4**(d+1)),
            ('II',(Z,scale(factor,ONE),Z),2*A(d)-1,4**(d+1)),
            ('III',(scale(factor,ONE),scale(-factor,ONE),Z),5*A(d),12*4**d)):
            row,history=orbit(initial)
            check(f'{family}_d{d}_sharp_M_P',row['d']==d and row['M']==expected_m and row['P']==expected_p)
            check(f'{family}_d{d}_3P_bound',3*row['P']<=2*row['M']-5)
            if family=='III':
                check(f'III_d{d}_five_equally_spaced_maxima',
                      len(row['maximal_phases'])==5 and row['cyclic_maximal_phase_gaps']==[A(d)]*5)
            families.append({'family':family,'d_input':d,'initial':initial,'result':row})
    diagonal,dh=orbit((ONE,ONE,ONE))
    check('diagonal_excluded_from_bound',diagonal['M']==0 and diagonal['P']==1 and not(3<=-5))
    result={
        'scope':'exposed-source finite exact replay; analytical argument in PROOF.md',
        'definitions':{'h':'min(v2(a-b),v2(b-c)), v2(0)=infinity',
                       'd':'maximum h over the full least orbit',
                       'A_d':'(4^(d+1)-1)/3','pi':'sum coefficients modulo5, i.e. O/(1-j)'},
        'integer_witness':witness,
        'hidden_phase':{'w':w,'v':v,'X':X,'Y':Y,'X_result':xr,'Y_result':yr,
                        'coefficient_mod5_X':coefficient_mod5_X,'coefficient_mod5_Y':coefficient_mod5_Y,
                        'individual_Q_X':[Q(a) for a in X],'individual_Q_Y':[Q(a) for a in Y]},
        'sharp_family_checks':families,
        'checks':checks,'failures':failures,'limited_inputs':[]
    }
    (HERE/'results.json').write_text(json.dumps(result,indent=2)+'\n')
    print('integer witness P,d,M:',witness['P'],witness['d'],witness['M'])
    print('X/Y P:',xr['P'],yr['P'],'E:',E(X),E(Y),'M:',M(X),M(Y),'same depth history:PASS')
    print('X coefficient residues mod5:',coefficient_mod5_X)
    print('Y coefficient residues mod5:',coefficient_mod5_Y)
    print('sharp family checks:',len(families),'d=0..5')
    print('RESULT',len(checks),'checks;',len(failures),'failures;0 limited inputs')
    if failures: raise AssertionError(failures)

if __name__=='__main__': main()
