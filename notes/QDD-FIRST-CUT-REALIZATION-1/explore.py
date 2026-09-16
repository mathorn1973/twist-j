#!/usr/bin/env python3
"""NON-CANONICAL exploration of a fixed first-cut passive completion.

Not a formal verifier; prior public proofs fix the source and port rows.
Exact assertions use standard-library rational arithmetic. No sealed probe
is imported, modified, or executed. The radical construction is specified
by rational LDL data, whose defining Gram identities are checked exactly.
"""
from fractions import Fraction as F
from itertools import product, permutations
import json

H = (
    (-354,1416,-354,-354),(-354,-354,1416,-354),
    (-348,-348,-348,1422),(-368,-343,-343,-373),
    (8,53,-22,-22),(8,-22,53,-22),(16,-14,-9,16),
    (1421,-349,-349,-349),
)
PORTS=((1,1,0),(1,0,1),(0,1,1),(2,0,0),
       (-1,-1,0),(-1,0,-1),(-1,0,1),(0,0,0))
Y=((0,0,0),(1,1,0),(1,0,1),(0,1,1),(2,0,0))
SCALE=4860**2

def transpose(a): return tuple(zip(*a))
def mul(a,b): return tuple(tuple(sum((x*y for x,y in zip(row,col)),F(0))
                                for col in transpose(b)) for row in a)
def sub(a,b): return tuple(tuple(x-y for x,y in zip(ar,br)) for ar,br in zip(a,b))
def scale(c,a): return tuple(tuple(c*x for x in row) for row in a)
def identity(n): return tuple(tuple(F(i==j) for j in range(n)) for i in range(n))

def ldl(a, require_positive=True):
    n=len(a); lower=[[F(i==j) for j in range(n)] for i in range(n)]; diagonal=[]
    for j in range(n):
        pivot=a[j][j]-sum(lower[j][k]**2*diagonal[k] for k in range(j))
        if require_positive:
            assert pivot>0
        if not pivot:
            return None,None
        diagonal.append(pivot)
        for i in range(j+1,n):
            lower[i][j]=(a[i][j]-sum(lower[i][k]*lower[j][k]*diagonal[k]
                                    for k in range(j)))/pivot
    lower=tuple(tuple(row) for row in lower); diagonal=tuple(diagonal)
    diag=tuple(tuple(diagonal[i] if i==j else F(0) for j in range(n)) for i in range(n))
    assert mul(mul(lower,diag),transpose(lower))==a
    return lower,diagonal

def inverse(a):
    n=len(a); t=[list(row)+list(irow) for row,irow in zip(a,identity(n))]
    for j in range(n):
        k=next(i for i in range(j,n) if t[i][j])
        t[j],t[k]=t[k],t[j]
        pivot=t[j][j];t[j]=[x/pivot for x in t[j]]
        for i in range(n):
            if i==j:continue
            q=t[i][j];t[i]=[x-q*y for x,y in zip(t[i],t[j])]
    answer=tuple(tuple(row[n:]) for row in t)
    assert mul(a,answer)==identity(n)
    return answer

def stencil():
    out={}
    for shell,w in (((1,1,0),6),((2,0,0),1),((2,2,0),15),((3,1,0),1),((4,0,0),1)):
        for perm in permutations(shell):
            for signs in product((-1,1),repeat=3):
                out[tuple(a*b for a,b in zip(perm,signs))]=F(w,324)
    return out

def hrow(x,st):
    out=[F(0)]*4
    for j,y in enumerate(Y):
        d=tuple(a-b for a,b in zip(y,x))
        k=F(10,9) if x==y else st.get(d,F(0))
        for i in range(4):out[i]+=k*(F(i==j)-F(1,5))
    return tuple(out)

def main():
    st=stencil()
    assert len(st)==60 and sum(st.values())==F(8,9)
    assert tuple(hrow(x,st) for x in PORTS)==scale(F(1,1620),H)
    B=scale(F(-1,4860),H)
    P=tuple(tuple(F(i==j,2)-F(1,10) for j in range(4)) for i in range(4))
    Bgram=mul(transpose(B),B)
    R=sub(P,Bgram)
    integer_R=scale(SCALE,R)
    assert all(v.denominator==1 for row in integer_R for v in row)
    L,d=ldl(integer_R)
    leading=[];value=F(1)
    for pivot in d:
        value*=pivot;leading.append(value)
    assert all(v>0 for v in leading)
    # C=diag(sqrt(d_i))/4860 * L^T, hence C^T C=R exactly.
    certified_margins=[]
    for margin in (F(1,2),F(2,3),F(7,10),F(3,4),F(4,5)):
        _,dd=ldl(sub(R,scale(margin,P)),require_positive=False)
        certified_margins.append((margin,dd is not None and all(v>0 for v in dd)))
    margin_integer=scale(SCALE,sub(scale(10,R),scale(7,P)))
    _,margin_diagonal=ldl(margin_integer)
    margin_leading=[];value=F(1)
    for pivot in margin_diagonal:
        value*=pivot;margin_leading.append(value)
    Pinverse=inverse(P)
    gram_normalized_trace=sum(mul(Pinverse,Bgram)[i][i] for i in range(4))
    # Four independent real input directions are retained already by B.
    _,bd=ldl(Bgram)
    assert all(v>0 for v in bd)
    # Independent matrix-metric check of the separate sensitivity derivation.
    origin_first=(B[-1],)+B[:-1]
    alpha_squared=tuple(mul(mul((row,),Pinverse),transpose((row,)))[0][0]
                        for row in origin_first)
    alpha_expected=tuple(map(F,('63113/295245','6962/32805','6962/32805',
        '2341/10935','127309/590490','413/1180980','413/1180980','29/393660')))
    assert alpha_squared==alpha_expected
    upper=tuple(F(v,10**6) for v in (462348,460678,460678,462692,464327,18701,18701,8583))
    assert all(a*a>=q and (a-F(1,10**6))**2<q for a,q in zip(upper,alpha_squared))
    weights=(F(1),)+tuple(abs(F(v)) for v in ('-111027113/111030330',
        '-111027113/111030330','-9409883/9409350','1556538/1568225',
        '-11092/313645','-11092/313645','0'))
    sensitivity_linear=2*sum(w*a for w,a in zip(weights,upper))
    sensitivity_quadratic=sum(weights)
    assert sensitivity_linear==F(320403677788237,69393956250000)
    assert sensitivity_quadratic==F(936962003,185050550)
    buffer={tuple(a+b for a,b in zip(x,s)) for x in set(Y)|set(PORTS)
            for s in set(st)|{(0,0,0)}}
    # General first-cut residual law at all balanced native heads.
    for z in product(range(-2,3),repeat=4):
        quadratic=lambda m:sum(F(z[i])*m[i][j]*z[j] for i in range(4) for j in range(4))
        assert quadratic(P)==quadratic(Bgram)+quadratic(R)
        assert quadratic(R)>0 or z==(0,0,0,0)
    report={
      'status':'NON-CANONICAL EXPLORATION; no formal gate or physical measurement',
      'signed_output_order':PORTS,
      'B_definition':'B=-H/4860; outgoing b=B z, gamma=1, first cut only',
      'H_integer_rows':H,
      'input_energy_metric_P_G_over_2':P,
      'residual_integer_matrix_23619600_R':integer_R,
      'positive_leading_principal_minors_integer_matrix':leading,
      'LDL_lower_unit_L':L,'LDL_positive_diagonal_d':d,
      'exact_radical_residual_factor':'C=diag(sqrt(d_i))/4860 times transpose(L); C^T C=R',
      'B_rank':4,'residual_rank':4,
      'minimum_residual_real_channels_fixed_metric':4,
      'total_separate_output_channels_fixed_metric':12,
      'normalized_energy_fraction_trace':gram_normalized_trace,
      'certified_strict_margins_R_minus_margin_P':certified_margins,
      'strict_seven_tenths_margin_integer_23619600_times_10R_minus_7P':margin_integer,
      'strict_seven_tenths_margin_positive_leading_minors':margin_leading,
      'full_first_cut_Dirichlet_buffer_site_count':len(buffer),
      'full_wave_plus_port_scattering_mode_count_2n_plus_8':2*len(buffer)+8,
      'balanced_source_energy_checks':625,
      'independent_sensitivity_metric_norm_check':'PASS',
      'origin_first_alpha_squared':alpha_squared,
      'sensitivity_uniform_linear_gain_upper':sensitivity_linear,
      'sensitivity_uniform_quadratic_gain':sensitivity_quadratic,
      'source_reference':'P-QDD-PASSIVE-QUADRATIC-CALIBRATION-1 proof at 757492055ab5a0a39e14a4089650f3f76ed9cf47',
    }
    print(json.dumps(report,indent=2,default=str))

if __name__=='__main__':main()
