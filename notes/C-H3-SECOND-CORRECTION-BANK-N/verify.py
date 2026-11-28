"""NON-CANONICAL #2133 A-C. Fixed-branch late radiation response."""
from pathlib import Path
import runpy,hashlib
from itertools import product,combinations
from fractions import Fraction as Q
from collections import Counter
root=Path(__file__).resolve().parent
assert hashlib.sha256((root/'prior.py').read_bytes()).hexdigest()=='29826845142b36d24ef2571ba53d2f2a6e2bb5b5c4066057f5314f1a6b03c550'
V=runpy.run_path(str(root/'prior.py'))
H=V['H'];Z,O,R,J,JI,P=map(V.get,('Z','O','R','J','JI','P'))
add,sub,mul,sc,h,neg=map(V.get,('add','sub','mul','sc','h','neg'))
ix,cols,account,step,hist,scale=map(V.get,('ix','cols','account','step','hist','scale'))
col,arch,read,corr,material,mem,vert=map(V.get,('col','arch','read','corr','material','mem','vert'))
K=range(5);N=(0,2,3,4);keys=tuple(product(range(2),K));ny=6
Rhist=V['Rhist'];old=Rhist[1]
def exact(z):return all(Q(x).denominator==1 for x in z)
def ints(z):
    assert exact(z);return tuple(map(int,z))
def divide(a,b):return mul(a,H.inverse(b))
def lin(a,b,r):
    center=sc(Q(1,2),add(a,b));diff=sc(Q(1,2),mul(r,sub(a,b)))
    return add(center,diff),sub(center,diff)
# Only radiative rails are needed on a fixed branch word. All coefficients
# are elements of Q(j), not a parity test on fractional perturbations.
def advance(F,t):
    f=list(F);bit=(t-1)%2
    for rail in (2,3):
        size,breadth=(8,2) if rail==3 else (2,8)
        for p,o in product(range(bit,size,2),range(breadth)):
            q=(p+1)%size
            i,k=(ix(2,x,o,rail) for x in (p,q)) if rail==3 else (ix(2,o,y,rail) for y in (p,q))
            if H.even(sub(old[0][t-1][i],old[0][t-1][k])):f[i],f[k]=lin(F[i],F[k],R)
    for x,y,tag in old[2][t]:
        i,k=ix(2,x,y,2),ix(2,x,y,3)
        f[i],f[k]=lin(f[i],f[k],JI if tag==1 else J)
    return tuple(f)
slots=tuple(ix(2,x,y,r) for x,y,r in product((0,6),range(2),(2,3)))
target=tuple(sub(old[0][0][i],old[0][114][i]) for i in slots)
assert target!=tuple(Z for _ in slots)
print('C TERMINAL_TARGET',target,'SLOTS',slots)
for x in (0,6):
    a=account(col(old[0][0],2,x));b=account(col(old[0][114],2,x))
    print('C BARE_DELTA',x,tuple(sub(v,u) for u,v in zip(a,b)))
for p,w in enumerate(Rhist):
    assert all(w[0][114][i]==w[0][0][i] for i in slots)==(p!=1)
    assert col(w[0][114],2,0)==col(w[0][0],2,0)
    assert all(w[0][114][ix(2,6,y,r)]==w[0][0][ix(2,6,y,r)] for y,r in product(range(2),range(3)))
    if p!=1:assert col(w[0][114],2,6)==col(w[0][0],2,6)
    print('C BARE_WORKER',p,col(w[0][114],2,6),'INITIAL',col(w[0][0],2,6))
events=[]
for x in (1,2,3,4):
    ts=[]
    for t in range(1,114):
        v=[w[1][t][ix(2,x,0,3)] for w in Rhist]
        assert len({v[k] for k in N})==1
        if v[1]!=v[0]:
            ts.append(t)
            if t>=91:events.append((t,x))
    print('A DISTINGUISHING',x,ts)
events.sort()
def response(t,x):
    f=[Z]*64;f[ix(2,x,0,3)]=O
    # In this unused column, the opposing CLK change cannot couple to CORR.
    f[ix(2,x,0,2)]=neg(O)
    f=tuple(f)
    for u in range(t+1,115):f=advance(f,u)
    return tuple(f[i] for i in slots)
responses={ev:response(*ev) for ev in events}
for ev,r in responses.items():print('A RESPONSE',ev,r)
def single(v):
    i=next((i for i,a in enumerate(v) if a!=Z),None)
    if i is None:return None
    d=divide(target[i],v[i])
    return (d,) if d!=Z and tuple(mul(d,a) for a in v)==target else None
def pair(a,b):
    for i,j in combinations(range(len(target)),2):
        det=sub(mul(a[i],b[j]),mul(a[j],b[i]))
        if det==Z:continue
        d=divide(sub(mul(target[i],b[j]),mul(target[j],b[i])),det)
        e=divide(sub(mul(a[i],target[j]),mul(a[j],target[i])),det)
        if d==Z or e==Z:return 'zero',None
        if tuple(add(mul(d,x),mul(e,y)) for x,y in zip(a,b))!=target:return 'inconsistent',None
        return 'solution',(d,e)
    return 'rank1',None
candidates=[];stats=Counter()
for ev in events:
    d=single(responses[ev]);stats['single_tried']+=1
    if d is None:stats['single_no']+=1;continue
    stats['single_solution']+=1
    if all(exact(mul(V['L'],z)) for z in d):candidates.append(((ev,),d));stats['single_integral']+=1
    print('A SINGLE',ev,d,'INTEGRAL',int(all(exact(mul(V['L'],z)) for z in d)))
for e0,e1 in combinations(events,2):
    state,d=pair(responses[e0],responses[e1]);stats['pair_tried']+=1;stats['pair_'+state]+=1
    if d:
        ok=all(exact(mul(V['L'],z)) for z in d)
        print('A PAIR',e0,e1,d,'INTEGRAL',int(ok))
        if ok:candidates.append(((e0,e1),d));stats['pair_integral']+=1
print('A COUNTS',sorted(stats.items()))
def select5():
    a,err=V['c5test'](6,1,1,V['ROOTS'][8],V['ROOTS'][5],0)
    assert err is None and V['hold'](5,a[1])[0]==154
    return dict(id=(6,1,1,8,5,0),ini=a[0],post=a[1],hold=154)
def select7():
    a,err=V['c7test'](6,1,1,7,3)
    assert err is None and V['hold'](7,a[1])[0]==126
    return dict(id=(6,1,1,7,3),ini=a[0],post=a[1],hold=126)
a,b=select5(),select7()
I=[V['make'](p,ny,a,b) for p in K]
hh=[hist(f,ny,114) for f in I]
base=[w[0][114] for w in hh]
assert len({w[3] for w in hh})==1 and H.scalar_account(hh[0][3][2])==80316
assert all(all(col(f,ny,x)==col(I[p],ny,x) for x in (0,6)) and corr(f)==corr(I[p]) for p,f in enumerate(base))
def load(f,p,q):
    f=list(f);u=[];v=[]
    for y in range(0,ny,2):
        i=ix(ny,0,y,0);assert f[i:i+2]==[scale(P[p]),scale(neg(P[p]))]
        v.extend(f[i:i+2]+[Z,Z]);f[i:i+2]=[scale(P[q]),scale(neg(P[q]))];u.extend(f[i:i+2]+[Z,Z])
    f=tuple(f);return f,tuple(u),tuple(v)
all25={}
for p,q in product(K,repeat=2):
    f,u,v=load(base[p],p,q)
    assert account(f)==account(base[p]) and account(base[p]+u)==account(f+v)
    all25[p,q]=f
loaded={k:all25[k] for k in keys}
assert len(set(all25.values()))==10 and all(f==loaded[int(p==1),q] for (p,q),f in all25.items())
# Original full second history; exact accounts, inverse, and silent prefix.
hs={k:hist(f,ny,114) for k,f in loaded.items()}
for k,w in hs.items():
    for t in range(115):
        if t:assert not any(e[0] in V['ARCH'] for e in w[2][t])
        for stage in ((0,) if t==0 else (1,0)):
            f=w[stage][t];r=Rhist[k[1]][stage][t]
            assert corr(f)==tuple(scale(r[ix(2,x,y%2,3)]) for x,y in product(range(8),range(ny)))
            for x in (0,6):
                assert col(f,ny,x)==tuple(scale(r[ix(2,x,y%2,rail)]) for y,rail in product(range(ny),range(4)))
for k in product(range(2),range(2)):
    f=hs[k][0][114]
    print('C INTEGRATED',k,'Q',H.scalar_account(hs[k][3][2]),'WORKER_DELTA',tuple(sub(v,u) for u,v in zip(account(col(I[k[1]],ny,6)),account(col(f,ny,6)))),
          'ARCH_DELTA',tuple(sub(v,u) for u,v in zip(account(arch(I[k[1]],ny)),account(arch(f,ny)))))
def matpart(f):return tuple(material(f,ny,x) for x in (5,7))
for t in range(115):
    for st in ((0,) if t==0 else (1,0)):
        FF={k:w[st][t] for k,w in hs.items()}
        assert len({matpart(f) for k,f in FF.items() if k[0]==0})==len({matpart(f) for k,f in FF.items() if k[0]==1})==1
        assert matpart(FF[0,0])!=matpart(FF[1,0])
# Artificial pulse diagnostics; no account or native-B claim at the pulse.
for evs,amps in candidates:
    ff=dict(loaded);fail=None;changes=0
    schedule={t:[] for t,x in evs}
    for (t,x),amp in zip(evs,amps):schedule[t].append((x,ints(mul(V['L'],amp))))
    for t in range(1,115):
        md={k:H.transport(f,ny,(t-1)%2) for k,f in ff.items()}
        cut={};tags={}
        for k,f in md.items():
            cut[k],tags[k]=H.collide(f,ny)
            if tags[k]!=hs[k][2][t]:changes+=1
            if any(e[0] in V['ARCH'] for e in tags[k]) and fail is None:fail=('ARCHIVE_B',t,k,tags[k])
        for x,amp in schedule.get(t,()):
            pos={md[k][ix(ny,x,y,3)] for k in keys for y in range(0,ny,2) if k[1]==1}
            negs={md[k][ix(ny,x,y,3)] for k in keys for y in range(0,ny,2) if k[1]!=1}
            if (len(pos)!=1 or len(negs)!=1 or pos==negs) and fail is None:fail=('INPUT',t,x)
            for k in keys:
                if k[1]!=1:continue
                a=list(cut[k])
                for y in range(0,ny,2):i=ix(ny,x,y,3);a[i]=add(a[i],amp)
                cut[k]=tuple(a)
        ff=cut
    count=sum((4 if k[0]==0 else 1)*int(all(col(f,ny,x)==col(I[k[1]],ny,x) for x in (0,6))) for k,f in ff.items())
    print('A HYPOTHETICAL',evs,'AMPS',tuple(schedule.items()),'RESET',count,'FIRST_FAIL',fail,'TAG_DIFFERENCES',changes)
# B: every admitted previously silent component stock; C7 independent.
r5=[]
for aa,bb,s,t,e in product((1,2),(1,2),range(10),range(10),(0,2)):
    res,err=V['c5test'](6,aa,bb,V['ROOTS'][s],V['ROOTS'][t],e)
    if err:continue
    hold,why=V['hold'](5,res[1])
    if hold>=114:r5.append(((aa,bb,s,t,e),res,hold))
r7=[]
for tag,k,u,v in product((1,2),K,range(11),range(11)):
    res,err=V['c7test'](6,tag,k,u,v)
    if err:continue
    hold,why=V['hold'](7,res[1])
    if hold>=114:r7.append(((tag,k,u,v),hold))
assert len(r5)==8 and len(r7)==3
want=scale(V['delta']);r=V['incoming'](Rhist,5,113,1,0)
allowed=tuple(add(r,sc(2,V['ratio'](want,tag))) for tag in (1,2))
print('B ALLOWED_CLK',allowed,'INCOMING',r,'CORRECTION',want)
for ident,res,hold in r5:
    for a0,(d,g) in enumerate(res[1]):
        for t in range(1,114):d,g=vert(d,(t-1)%2),vert(g,(t-1)%2)
        tests=[]
        for y in range(0,6,2):
            c0=V['incoming'](Rhist,5,113,1,y)
            zz,tag=H.collision(cols(d[y],g[y],c0))
            tests.append((y,d[y],g[y],tag,sub(zz[3],c0),int(g[y] in allowed)))
        assert all(t[3]==0 for t in tests)
        print('B CLOCK',ident,hold,a0,tuple(tests))
print('B PAIRED_PREPARATIONS',len(r5)*len(r7),'PASS_DIRECT',0,'C7',r7)
print('DONE exact fixed branch routes and silent clock readiness')
