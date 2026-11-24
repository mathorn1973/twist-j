#!/usr/bin/env python3
"""Exact source-exposed audit, NON-CANONICAL L1. A. M. Thorn, Apache-2.0.
No imports of predecessor scientific programs. Freeze before execution.
"""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
from hashlib import sha256
from dataclasses import dataclass
import json

Y = ((0,0,0),(1,1,0),(1,0,1),(0,1,1),(2,0,0))
WEIGHTS = {2:6,4:1,8:15,10:1,16:1}
DOMAIN_SHA = '2e9b77cf8c507b9bc6675d9a07bf8e27ad88921c72c1efc22dcf5bdb41d8a7c0'


def lin(*terms):
    out = {}
    for scale, row in terms:
        for i, x in row.items():
            out[i] = out.get(i,Q(0)) + scale*x
    return {i:x for i,x in out.items() if x}


def unit(i):
    return {i:Q(1)}


def pull(row, matrix):
    return lin(*((c,matrix[i]) for i,c in row.items()))


def dot(x,y):
    return sum((c*y.get(i,Q(0)) for i,c in x.items()),Q(0))


def determinant(matrix):
    a = [list(row) for row in matrix]
    d = Q(1)
    for j in range(len(a)):
        k = next((k for k in range(j,len(a)) if a[k][j]),None)
        if k is None:
            return Q(0)
        if k != j:
            a[j],a[k]=a[k],a[j]
            d = -d
        pivot = a[j][j]
        d *= pivot
        for k in range(j+1,len(a)):
            scale = a[k][j]/pivot
            for c in range(j,len(a)):
                a[k][c] -= scale*a[j][c]
    return d


@dataclass(frozen=True)
class State:
    u: dict
    v: dict
    tapes: tuple
    k: int = 0


def main():
    here = Path(__file__).resolve().parent
    for line in (here/'CODE_SHA256SUMS').read_text().splitlines():
        digest,name = line.split('  ',1)
        assert sha256((here/name).read_bytes()).hexdigest()==digest, name
    stencil = [x for x in product(range(-4,5),repeat=3)
               if sum(x)%2==0 and sum(t*t for t in x) in WEIGHTS]
    bzero = stencil+[(0,0,0)]
    domain = sorted({tuple(y[i]+a[i]+b[i] for i in range(3))
                     for y in Y for a in bzero for b in bzero})
    raw=('x\ty\tz\n'+''.join('%d\t%d\t%d\n'%x for x in domain)).encode()
    assert len(stencil)==60 and len(domain)==705 and sha256(raw).hexdigest()==DOMAIN_SHA
    n=len(domain); dim=2*n+16; index={x:i for i,x in enumerate(domain)}
    ports=[index[x] for x in Y[:4]]; pset=set(ports); e4=index[Y[4]]
    near=index[(6,0,0)]; far=index[(10,0,0)]
    H=[]
    for i,x in enumerate(domain):
        row={i:Q(10,9)}
        for d in stencil:
            y=tuple(x[k]+d[k] for k in range(3))
            if y in index:
                row[index[y]]=Q(WEIGHTS[sum(t*t for t in d)],324)
        H.append(row)
    for i,row in enumerate(H):
        for j,x in row.items():
            assert H[j].get(i,Q(0))==x
    A=[lin((Q(1),unit(ports[k])),(Q(-1,5),{index[y]:Q(1) for y in Y})) for k in (0,1)]
    G=[[dot(a,b) for b in A] for a in A]
    assert G==[[Q(4,5),Q(-1,5)],[Q(-1,5),Q(4,5)]]
    M=[[a.get(p,Q(0)) for p in ports] for a in A]
    h=[H[e4].get(p,Q(0)) for p in ports]
    assert h==[Q(1,324),Q(1,54),Q(1,54),Q(0)]
    def lift(row,offset): return {i+offset:x for i,x in row.items()}
    rho=[lin((Q(1),lift(a,n)),(Q(-1,2),pull(a,H))) for a in A]
    gamma=lin((Q(1,5),unit(e4)),(Q(-1,10),lift(H[e4],n)))
    hkh=pull({j:c*(Q(1,2) if j in pset else Q(1)) for j,c in H[e4].items()},H)
    hj={j:c for j,c in H[e4].items() if j not in pset}
    delta=lin((Q(1,5),unit(n+e4)),(Q(-1,10),lift(hkh,n)),(Q(1,10),hj))
    # Full F rows, independently assembled from its full wave/tape equations.
    a0=2*n; a1=a0+4; b0=a1+4; b1=b0+4
    wrows=[]
    for i in range(n):
        k=Q(1,2) if i in pset else Q(1)
        row=lin((k,lift(H[i],n)),(Q(0) if i in pset else -k,unit(i)))
        if i in pset:
            row=lin((Q(1),row),(4*k,unit(a0+ports.index(i))))
        wrows.append(row)
    Frows=[unit(n+i) for i in range(n)]+wrows
    Frows += [unit(a1+i) for i in range(4)]
    Frows += [unit(b1+i) for i in range(4)]
    Frows += [lin((Q(1),unit(a0+i)),(Q(-1,2),wrows[p]),(Q(1,2),unit(p))) for i,p in enumerate(ports)]
    Frows += [unit(b0+i) for i in range(4)]
    assert len(Frows)==dim
    identities=[]
    for i,r in enumerate(rho):
        expect=lin((Q(1),gamma),(Q(2),{a0+j:M[i][j] for j in range(4)}))
        identities.append((pull(r,Frows),expect))
    identities.append((pull(gamma,Frows),lin((Q(1),delta),(Q(-1,5),{a0+j:h[j] for j in range(4)}))))
    for i,r in enumerate(rho):
        expect=lin((Q(1),delta),(Q(-1,5),{a0+j:h[j] for j in range(4)}),(Q(2),{a1+j:M[i][j] for j in range(4)}))
        identities.append((pull(pull(r,Frows),Frows),expect))
    for actual,expect in identities:
        assert all(actual.get(i,Q(0))==expect.get(i,Q(0)) for i in range(dim))
    kappa=[dot(delta,lift(a,n)) for a in A]
    assert kappa==[Q(-145483,10497600),Q(-173653,10497600)]
    columns3=[lift(A[0],n),lift(A[1],n),unit(n+far)]
    columns4=[lift(A[0],n),lift(A[1],n),unit(n+near),unit(n+far)]
    d3=determinant([[dot(r,c) for c in columns3] for r in rho+[delta]])
    d4=determinant([[dot(r,c) for c in columns4] for r in rho+[gamma,delta]])
    assert d3==Q(3,5)*Q(-1,10*324**2)
    assert d4==Q(3,5)*Q(-1,10*324)*Q(-1,10*324**2)

    def h_apply(vec):
        # Symmetry lets the literal stencil act by sparse columns.
        return lin(*((value,H[j]) for j,value in vec.items()))
    def vector(x):
        out=lin((Q(1),x.u),(Q(1),lift(x.v,n)))
        for slot,values in enumerate(x.tapes):
            for j,val in enumerate(values):
                if val: out[2*n+4*slot+j]=Q(val)
        return out
    def read_rho(x): return tuple(dot(r,vector(x)) for r in rho)
    def read_delta(x): return dot(delta,vector(x))
    def f(x):
        aa,aa1,bb0,bb1=x.tapes
        unprojected={i:v for i,v in x.u.items() if i not in pset}
        inserted={ports[i]:4*aa[i] for i in range(4) if aa[i]}
        tmp=lin((Q(1),h_apply(x.v)),(Q(-1),unprojected),(Q(1),inserted))
        w={i:v*(Q(1,2) if i in pset else Q(1)) for i,v in tmp.items()}
        bout=tuple(aa[i]-(w.get(p,Q(0))-x.u.get(p,Q(0)))/2 for i,p in enumerate(ports))
        return State(dict(x.v),w,(aa1,bb1,bout,bb0),(x.k+1)%2)
    def energy(x):
        return (dot(x.u,x.u)+dot(x.v,x.v)-dot(x.u,h_apply(x.v)))/2+2*sum((t*t for slot in x.tapes for t in slot),Q(0))
    def eta(label):
        balanced=(0,1,2,-2,-1)
        return (Q(balanced[label[0]],2),Q(balanced[label[1]]+1,2))
    def source(et): return lin(*((et[i],A[i]) for i in range(2)))
    def cold(et): return sum((et[i]*G[i][j]*et[j] for i in range(2) for j in range(2)),Q(0))/2
    def proposed_cost(et,sg,r): return cold(et)+sg*sum((et[i]*r[i] for i in range(2)),Q(0))
    def contact(x,et,sg,B,b,W):
        proposed=State(dict(x.u),lin((Q(1),x.v),(Q(sg),source(et))),x.tapes,x.k)
        cost=energy(proposed)-energy(x)
        accepted=0<=b-cost<=B
        return (proposed if accepted else x, b-cost if accepted else b,
                W+cost if accepted else W,-sg if accepted else sg,cost,accepted)
    zeros=(Q(0),)*4; blank=(zeros,)*4
    witnesses=[]
    for sign in (1,-1):
        x=State({}, {far:Q(sign)},blank)
        assert read_rho(x)==(0,0) and dot(gamma,vector(x))==0 and energy(x)==Q(1,2)
        x1=f(x); x2=f(x1)
        assert x1.tapes==x2.tapes==blank
        assert energy(x1)==energy(x2)==Q(1,2)
        value=Q(-sign,10*324**2)
        assert read_delta(x)==value and read_rho(x2)==(value,value)
        result=contact(x2,(Q(1),Q(0)),1,Q(1),Q(1,2),Q(0))
        assert result[-1] and result[-2]==Q(2,5)+value
        witnesses.append(str(result[-2]))
    tape2=((Q(1,3),Q(-1,5),Q(0),Q(2,7)),(Q(0),Q(1,2),Q(-2,9),Q(0)),
           (Q(1),Q(-1),Q(0),Q(1,4)),(Q(-1,3),Q(0),Q(1,5),Q(0)))
    waves=[({},{}),({}, {far:Q(1)}),({}, {far:Q(-1)}),
           ({ports[0]:Q(2,3),near:Q(-1,7)},{ports[1]:Q(-3,5),far:Q(5,11)}),
           ({},{ports[0]:Q(-2)})]
    family=[State(dict(u),dict(v),tape) for u,v in waves for tape in (blank,tape2)]
    labels=list(product(range(5),repeat=2))
    stocks=[(Q(0),Q(0)),(Q(1),Q(1,2)),(Q(1),Q(1)),(Q(1,2),Q(1,4))]
    single=0
    for x,label,sg,stock in product(family,labels,(1,-1),stocks):
        B,b=stock; et=eta(label); r=read_rho(x); d=read_delta(x)
        y,bnew,wnew,sgnew,cost,yes=contact(x,et,sg,B,b,Q(2,7))
        assert cost==proposed_cost(et,sg,r)
        expected_r=tuple(r[i]+(sg*sum((G[i][j]*et[j] for j in range(2)),Q(0)) if yes else 0) for i in range(2))
        expected_d=d+(sg*sum((kappa[j]*et[j] for j in range(2)),Q(0)) if yes else 0)
        assert read_rho(y)==expected_r and read_delta(y)==expected_d
        single+=1
    pairs=[((0,4),(0,4)),((0,4),(2,4)),((2,4),(0,1)),((1,4),(4,1))]
    twouse=0; branch_counts={}
    for x,pair,sgs,stock in product(family,pairs,product((1,-1),repeat=2),stocks[:3]):
        B,b=stock; sa,sb=sgs; ea,eb=map(eta,pair); W=Q(2,7)
        r=read_rho(x); d=read_delta(x); ca=proposed_cost(ea,sa,r)
        ya=0<=b-ca<=B; bp=b-ca if ya else b; wp=W+ca if ya else W
        dp=d+(sa*sum((kappa[j]*ea[j] for j in range(2)),Q(0)) if ya else 0)
        g2=dp-sum((h[j]*x.tapes[0][j] for j in range(4)),Q(0))/5
        rb=tuple(g2+2*sum((M[i][j]*x.tapes[1][j] for j in range(4)),Q(0)) for i in range(2))
        cb=proposed_cost(eb,sb,rb); yb=0<=bp-cb<=B
        xp,bd,wd,sad,cad,yad=contact(x,ea,sa,B,b,W)
        assert cad==ca and yad==ya
        xp1=f(xp); xp2=f(xp1)
        assert energy(xp)==energy(xp1)==energy(xp2)
        assert read_rho(xp2)==rb
        xf,bd,wd,sbd,cbd,ybd=contact(xp2,eb,sb,B,bd,wd)
        assert cbd==cb and ybd==yb
        assert bd==(bp-cb if yb else bp) and wd==(wp+cb if yb else wp)
        assert sad==(-sa if ya else sa) and sbd==(-sb if yb else sb)
        assert energy(xf)+bd==energy(x)+b
        assert read_rho(xf)==tuple(rb[i]+(sb*sum((G[i][j]*eb[j] for j in range(2)),Q(0)) if yb else 0) for i in range(2))
        key=f'{int(ya)}{int(yb)}'; branch_counts[key]=branch_counts.get(key,0)+1
        twouse+=1
    assert single==2000 and twouse==480
    report={'status':'PASS / NON-CANONICAL / candidate-C / L1','domain':n,'full_linear_dimension':dim,
            'coefficient_equalities':len(identities)*dim,'rank_horizon_0_2':3,'rank_horizon_0_1_2':4,
            'minor3':str(d3),'minor4':str(d4),'kappa':[str(t) for t in kappa],
            'equal_energy_far_witness_work':witnesses,'one_contact_cases':single,
            'two_contact_cases':twouse,'branches':branch_counts,
            'scope':'fixed linear wave summaries; tapes known separately; two F steps, not autonomous all-time closure'}
    print(json.dumps(report,sort_keys=True,separators=(',',':')))


if __name__=='__main__':
    main()
