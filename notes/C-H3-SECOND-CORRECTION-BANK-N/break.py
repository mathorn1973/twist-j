"""NON-CANONICAL #2133 alternate A-E. Independent predecessor ring/update."""
import runpy,hashlib
from pathlib import Path
from itertools import product,combinations
from fractions import Fraction as Q
from collections import Counter
root=Path(__file__).resolve().parent
engine=root/'alternate_prior.py'
assert hashlib.sha256(engine.read_bytes()).hexdigest()=='d92e1d6b859efe5a2c49f9bc65959a51202c8cb32d4a015594c50603086bb99b'
V=runpy.run_path(str(engine))
Z,O,R,J,JI,P,L=map(V.get,('Z','O','R','J','JI','P','L'))
add,sub,mul,sc,h,neg=map(V.get,('add','sub','mul','sc','h','neg'))
ix,cell,account,hist,col,arch,corr,vert,C,B,transport=map(V.get,('ix','cell','account','hist','col','arch','corr','vert','C','B','transport'))
scale=V['scale'];scalar=V['scalar']
K=range(5);N=(0,2,3,4);old=V['Rhist'][1];target=(6,3,0,6);delta=V['delta']
def fieldinv(z):
    # Galois conjugates in the cyclic-five representation, unlike the
    # primary's reduction-polynomial inverse.
    assert z!=Z
    def sigma(a):return V['rs'](sc(v,P[k*a%5]) for k,v in enumerate(z))
    p=mul(mul(sigma(2),sigma(3)),sigma(4));n=mul(z,p)
    assert n[1:]==(0,0,0) and n[0]!=0
    return sc(Q(1,n[0]),p)
slots=tuple((ix(2,x,y),r) for x,y,r in product((0,6),range(2),(2,3)))
targetvec=tuple(sub(old[0][0][i][r],old[0][114][i][r]) for i,r in slots)
assert targetvec==tuple(target if k==5 else Z for k in range(8))
for p,w in enumerate(V['Rhist']):
    assert col(w[0][114],2,0)==col(w[0][0],2,0)
    assert (col(w[0][114],2,6)==col(w[0][0],2,6))==(p!=1)
    if p==1:
        f=col(w[0][114],2,6);i=col(w[0][0],2,6)
        assert tuple(sub(v,u) for u,v in zip(account(i),account(f)))==(Z,neg(target),(132,0,69,69))
print('ALT C TARGET',targetvec)
events=[]
for x in (1,2,3,4):
    ts=[]
    for t in range(1,114):
        w=[hh[1][t][ix(2,x,0)][3] for hh in V['Rhist']]
        assert len({w[p] for p in N})==1
        if w[1]!=w[0]:ts.append(t)
    events.extend((t,x) for t in ts if t>=91)
    assert ts==({1:[],2:[],3:list(range(52,60)),4:list(range(15,103))}[x])
    print('ALT A DISTINGUISHING',x,ts)
events.sort()
alpha=sc(Q(1,2),J);beta=sc(Q(1,2),L)
def mix(a,b,r):
    A=sc(Q(1,2),add(O,r));D=sc(Q(1,2),sub(O,r))
    return add(mul(A,a),mul(D,b)),add(mul(D,a),mul(A,b))
def response(t,x):
    F=[(Z,Z) for _ in range(16)];F[ix(2,x,0)]=(neg(O),O)
    for u in range(t+1,115):
        # Apply the fixed actual linear branch, in an independent
        # cell-vector representation with explicit two-axis pairs.
        ff=[list(v) for v in F];prev=old[0][u-1];bit=(u-1)%2
        for rail in range(2):
            for a,b in ([(ix(2,k,bit),ix(2,k,1-bit)) for k in range(8)] if rail==0 else [(ix(2,k,y),ix(2,(k+1)%8,y)) for k,y in product(range(bit,8,2),range(2))]):
                if V['even'](sub(prev[a][rail+2],prev[b][rail+2])):
                    ff[a][rail],ff[b][rail]=mix(F[a][rail],F[b][rail],R)
        for k,y,tag in old[2][u]:
            i=ix(2,k,y);ff[i][:]=mix(*ff[i],JI if tag==1 else J)
        F=tuple(tuple(v) for v in ff)
    return tuple(F[i][r-2] for i,r in slots)
vecs=[response(*v) for v in events]
assert len(vecs)==12
# Exact rank-one certificate without solving the same pair systems:
# all columns are multiples of a nonzero first column. The target
# is not in this span because a nonzero worker CLK coefficient is
# present whereas the target has only a worker CORR component.
p=next(i for i,v in enumerate(vecs[0]) if v!=Z)
assert targetvec[p]==Z
factor=[mul(v[p],fieldinv(vecs[0][p])) for v in vecs]
assert all(a!=Z and tuple(mul(a,u) for u in vecs[0])==v for a,v in zip(factor,vecs))
assert all(v[p]!=Z for v in vecs)
print('ALT A RANK',1,'EVENTS',len(vecs),'SINGLES_NO',12,'PAIRS_RANK1',66,'PIVOT',p,'FACTORS',factor)
r5=[];r7=[]
for a,b,s,t,e in product((1,2),(1,2),range(10),range(10),(0,2)):
    res,err=V['check5'](6,a,b,V['roots'][s],V['roots'][t],e)
    if err:continue
    hold,why=V['hold'](5,res[1])
    if hold>=114:r5.append(((a,b,s,t,e),res,hold))
for tag,k,u,v in product((1,2),K,range(11),range(11)):
    res,err=V['check7'](6,tag,k,V['WS'][u],V['WS'][v])
    if err:continue
    hold,why=V['hold'](7,res[1])
    if hold>=114:r7.append(((tag,k,u,v),hold))
assert len(r5)==8 and len(r7)==3
want=scale(delta);r=V['inc'](V['Rhist'],5,113,1,0)
allowed=tuple(add(r,sc(2,V['f_for'](want,tag))) for tag in (1,2))
for ident,res,hold in r5:
    for bit,(d,g) in enumerate(res[1]):
        for t in range(113):d,g=vert(d,t%2),vert(g,t%2)
        assert all(g[y] not in allowed and B(cell(d[y],g[y],r))[1]==0 for y in range(0,6,2))
        print('ALT B CLK',ident,bit,tuple(g[y] for y in range(0,6,2)))
print('ALT B PAIRED',len(r5)*len(r7),'DIRECT',0)
# Replay the selected integrated field with fresh input and no new bank.
a=next(res for ident,res,hold in r5 if ident==(1,1,8,5,0))
b,err=V['check7'](6,1,1,V['WS'][7],V['WS'][3]);assert err is None
a=dict(ini=a[0]);b=dict(ini=b[0])
I=[V['make'](p,6,a,b) for p in K];hh=[hist(f,6,114) for f in I]
assert all(scalar(w[3][2])==80316 for w in hh)
F=[w[0][114] for w in hh]
assert all(col(f,6,0)==col(I[p],6,0) and col(f,6,6)==col(I[p],6,6) and corr(f)==corr(I[p]) for p,f in enumerate(F))
def load(f,p,q):
    f=list(f);u=[];v=[]
    for y in range(0,6,2):
        i=ix(6,0,y);assert f[i][:2]==(scale(P[p]),scale(neg(P[p])))
        v.append(cell(scale(P[p]),Z,Z));u.append(cell(scale(P[q]),Z,Z))
        f[i]=cell(scale(P[q]),f[i][2],f[i][3])
    return tuple(f),tuple(u),tuple(v)
all25={}
for p,q in product(K,repeat=2):
    f,u,v=load(F[p],p,q)
    assert account(F[p])==account(f) and account(F[p]+u)==account(f+v)
    all25[p,q]=f
assert len(set(all25.values()))==10 and all(f==all25[int(p==1),q] for (p,q),f in all25.items())
for k in product(range(2),K):
    w=hist(all25[k],6,114)
    for t in range(115):
        if t:assert not any(x in V['ARCH'] for x,y,k0 in w[2][t])
        for stage in ((0,) if t==0 else (1,0)):
            G=w[stage][t];R0=V['Rhist'][k[1]][stage][t]
            assert corr(G)==tuple(scale(R0[ix(2,x,y%2)][3]) for x,y in product(range(8),range(6)))
            for x in (0,6):assert col(G,6,x)==tuple(tuple(scale(z) for z in R0[ix(2,x,y%2)]) for y in range(6))
    f=w[0][114];assert col(f,6,0)==col(I[k[1]],6,0)
    dif=tuple(sub(v,u) for u,v in zip(account(col(I[k[1]],6,6)),account(col(f,6,6))))
    assert dif==( (Z,(0,-9,18,-9),(585,0,225,225)) if k[1]==1 else (Z,Z,Z))
print('ALT C INTEGRATED','Q',80316,'WORKER_DELTA_POS',945,'RESET',20)
# D: exact same frozen amplitude set, independent order-free set generation.
def power(u,e):
    if e<0:assert u==J;u,e=JI,-e
    z=O
    for _ in range(e):z=mul(z,u)
    return z
units={sc(s,mul(P[k],power(J,e))) for s,k,e in product((1,-1),K,range(-3,4))}
zs={sc(n,mul(u,d)) for n,u,d in product((1,2,3,4,6,8,12,16),units,(target,delta))}
zs|={sc(2**h0,mul(mul(power(L,ell),u),d)) for h0,ell,u,d in product(range(4),(1,2),units,(target,delta))}
assert len(zs)==1750
stats=Counter()
for t in range(91,103):
    local=Counter()
    for z in sorted(zs):
        f=list(old[0][t]);i=ix(2,4,0);f[i]=f[i][:3]+(add(f[i][3],z),);f=tuple(f)
        changed=False
        for u in range(t+1,115):
            g=transport(f,2,(u-1)%2);b0=tuple(B(c0) for c0 in g);f=tuple(v[0] for v in b0)
            tags=tuple((x,y,b0[ix(2,x,y)][1]) for x,y in product(range(8),range(2)) if b0[ix(2,x,y)][1])
            changed |= tags!=old[2][u]
        a=col(f,2,0)==col(old[0][0],2,0);b=col(f,2,6)==col(old[0][0],2,6)
        c=f[ix(2,6,0)][3]==old[0][0][ix(2,6,0)][3]
        local[(int(a),int(b),int(c),int(changed))]+=1
    stats.update(local)
    assert local=={(0,0,0,1):(100 if t<93 else 80),(1,0,0,1):(1650 if t<93 else 1670)}
    print('ALT D',t,sorted(local.items()))
assert stats=={(0,0,0,1):1000,(1,0,0,1):20000}
print('ALT D TOTAL',sorted(stats.items()))
# E: derive the coefficient matrix by the exact C^4 closed expression,
# not the primary's iterative pair propagation / RREF method.
g1=tuple(scale(add(V['r'],sc(2,V['f_for'](delta,k)))) for k in (1,2))
g2=tuple(scale(add(V['c'],sc(2,V['f_for'](V['delta5'],k)))) for k in (1,2))
a4=sc(Q(1,2),add(O,P[3]));b4=sc(Q(1,2),sub(O,P[3]))
def residual(a,b,c):
    E=add(g1[0],sc(a,sub(g1[1],g1[0])));G=add(g2[0],sc(b,sub(g2[1],g2[0])))
    Odd=mul(V['BI'],sub(G,mul(alpha,sub(E,want))))
    return sub(add(mul(a4,E),mul(b4,Odd)),add(g1[0],sc(c,sub(g1[1],g1[0]))))
zero=residual(0,0,0);columns=[sub(residual(*z),zero) for z in ((1,0,0),(0,1,0),(0,0,1))]
assert zero==(-39,3,-36,-33)
assert columns==[(60,-48,60,-12),(12,0,36,12),(0,36,-24,48)]
# Integer left-annihilator, with independent determinant certificate for rank.
u=(-16,-26,-1,19)
dot=lambda a,b:sum(x*y for x,y in zip(a,b))
assert all(dot(u,v)==0 for v in columns) and dot(u,zero)==-45
M=tuple(tuple(v[i] for v in columns) for i in range(3))
det=sum((1 if (i,j,k) in ((0,1,2),(1,2,0),(2,0,1)) else -1)*M[0][i]*M[1][j]*M[2][k] for i,j,k in ((0,1,2),(0,2,1),(1,0,2),(1,2,0),(2,0,1),(2,1,0)))
assert det!=0
print('ALT E',zero,columns,'ANNIHILATOR',u,'DOT_CONSTANT',dot(u,zero),'RANK_MINOR',det,'RANK',3,'AUG',4)
print('PASS independent ring/update A-E; no native second bank')
