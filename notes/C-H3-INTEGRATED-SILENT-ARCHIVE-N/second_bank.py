"""NON-CANONICAL #2131 D. A new bank one contact earlier than the old archive."""
from pathlib import Path
import runpy
from itertools import product,combinations
from collections import Counter
V=runpy.run_path(str(Path(__file__).resolve().parent/'verify.py'))
H=V['H'];Z,O,R,J,JI,P=map(V.get,('Z','O','R','J','JI','P'))
add,sub,mul,sc,h,neg=map(V.get,('add','sub','mul','sc','h','neg'))
ix,cols,account,step,hist,scale=map(V.get,('ix','cols','account','step','hist','scale'))
col,arch,read,corr,material,mem,vert,back=map(V.get,('col','arch','read','corr','material','mem','vert','back'))
parts,disj,clean,ratio,dm=map(V.get,('parts','disj','clean','ratio','dm'))
K=range(5);N=(0,2,3,4);ny=6;ARCH=V['ARCH'];keys=tuple(product(range(2),K))
d4=sc(2,V['delta'])
assert mul(sc(V['Q'](1,2),V['L']),d4)==scale(V['delta'])
def choice5():
    a,err=V['c5test'](6,1,1,V['ROOTS'][8],V['ROOTS'][5],0)
    assert err is None and V['hold'](5,a[1])[0]==154
    return dict(id=(6,1,1,8,5,0),ini=a[0],post=a[1],hold=154)
def choice7():
    a,err=V['c7test'](6,1,1,7,3)
    assert err is None and V['hold'](7,a[1])[0]==126
    return dict(id=(6,1,1,7,3),ini=a[0],post=a[1],hold=126)
a,b=choice5(),choice7()
I=[V['make'](p,ny,a,b) for p in K]
old=[hist(f,ny,114) for f in I]
F=[w[0][114] for w in old]
assert all(all(col(F[p],ny,x)==col(I[p],ny,x) for x in (0,6)) and corr(F[p])==corr(I[p]) for p in K)
assert H.scalar_account(old[0][3][2])==80316
def exchange(f,p,q):
    f=list(f);reserve=[];outgoing=[]
    for y in range(0,ny,2):
        i=ix(ny,0,y,0)
        assert f[i:i+2]==[scale(P[p]),scale(neg(P[p]))]
        outgoing.extend(f[i:i+2]+[Z,Z])
        new=[scale(P[q]),scale(neg(P[q]))];reserve.extend(new+[Z,Z]);f[i:i+2]=new
    return tuple(f),tuple(reserve),tuple(outgoing)
def load(f,p,q):
    z,u,v=exchange(f,p,q)
    assert account(z)==account(f) and account(f+u)==account(z+v)
    return z
all25={(p,q):load(F[p],p,q) for p,q in product(K,repeat=2)}
loaded={k:all25[k] for k in keys}
assert len(set(all25.values()))==10 and all(f==loaded[int(p==1),q] for (p,q),f in all25.items())
sec={k:hist(f,ny,114) for k,f in loaded.items()}
r4=sec[0,1][1][112][ix(ny,4,0,3)]
pos={w[1][112][ix(ny,4,y,3)] for (a0,q),w in sec.items() for y in range(0,ny,2) if q==1}
negative={w[1][112][ix(ny,4,y,3)] for (a0,q),w in sec.items() for y in range(0,ny,2) if q!=1}
print('D TARGET226','POS',sorted(pos),'NEG',sorted(negative),'DELTA4',d4)
if pos!={r4} or len(negative)!=1 or r4 in negative:
    print('D STOP target radiation unavailable')
    raise SystemExit(0)
# Pre-B radiation transcripts for the earlier-idle condition, deduplicated
# only by literal equality of the local CORR values.
def inputs(t,y):
    if t<=114:return tuple(dict.fromkeys(w[1][t][ix(ny,4,y,3)] for w in old))
    return tuple(dict.fromkeys(w[1][t-114][ix(ny,4,y,3)] for w in sec.values()))
incoming={t:tuple(inputs(t,y) for y in range(ny)) for t in range(1,226)}
def patch(f,x,d,g):
    f=list(f)
    for y in range(ny):
        i=ix(ny,x,y,0);f[i:i+3]=(d[y],neg(d[y]),g[y])
    return tuple(f)
def advance(v,n):
    for t in range(1,n+1):v=vert(v,(t-1)%2)
    return v
def candidate(tag,k,ui,vi):
    f=ratio(d4,tag);g0=add(r4,sc(2,f));d0=dm(f,tag)
    u,v=V['WS'][ui],V['WS'][vi]
    goal=tuple((mul(d0,P[k]) if y==0 else d0) if y%2==0 else add(d0,sc(2,v if y==1 else u)) for y in range(ny))
    ini=back(goal,226);d=ini;g=tuple(g0 for _ in range(ny))
    for t in range(1,227):
        d=vert(d,(t-1)%2)
        if t==226:break
        for y in range(ny):
            if any(H.collision(cols(d[y],g0,z))[1] for z in incoming[t][y]):
                return 'EARLY_'+str(t),None
    assert d==goal
    for (a0,q),w in sec.items():
        for y in range(ny):
            c=w[1][112][ix(ny,4,y,3)]
            n,t=H.collision(cols(d[y],g0,c))
            expected=tag if q==1 and y%2==0 else 0
            if t!=expected:return 'TARGET_TAG',None
            assert n[3]==add(c,d4 if expected else Z)
    return 'ADMIT',(ini,g,goal)
def local_end(tag,ini,g,goal):
    # All earlier x4 B are idle, so adding its independent actual vertical
    # state to the old pre-B226 cut is exactly the proved prehistory.
    # No externally altered native trajectory is asserted as the final result.
    before={k:patch(w[1][112],4,goal,g) for k,w in sec.items()}
    final={};mid={};stage={};ac={}
    for k,f in before.items():
        ac[k]=account(patch(I[k[1]],4,ini,g))
        assert account(f)==ac[k]
        N0,ev=H.collide(f,ny);assert H.collide(N0,ny)[0]==f and account(N0)==ac[k]
        assert tuple(e for e in ev if e[0] in ARCH)==tuple((4,y,tag) for y in range(0,ny,2) if k[1]==1)
        G1,N1,E1=step(N0,ny,0,ac[k])
        if any(e[0] in ARCH for e in E1):return 'ARCHIVE_B227',None
        # The intended correction has actually crossed the x4,x5 edge.
        for y in range(ny):
            i=ix(ny,5,y,3);v=sec[k][1][113][i]
            want=add(v,scale(V['delta']) if k[1]==1 and y%2==0 else Z)
            if G1[i]!=want:return 'DELIVERY227',None
        G2,N2,E2=step(N1,ny,1,ac[k])
        if any(e[0] in ARCH for e in E2):return 'ARCHIVE_B228',None
        if not all(col(N2,ny,x)==col(I[k[1]],ny,x) for x in (0,6)):return 'RESET228',None
        assert account(arch(N2,ny))==account(arch(patch(I[k[1]],4,ini,g),ny))
        final[k]=N2
    first=lambda f:tuple(mem(f,ny,x) for x in (5,7))
    second=lambda f:mem(f,ny,4)
    if not clean(parts(final,first,lambda k:k[0])):return 'OLD_RECORD',None
    if not clean(parts(final,second,lambda k:int(k[1]==1))):return 'NEW_RECORD',None
    if not clean(parts(final,lambda f:tuple(material(f,ny,x) for x in ARCH),lambda k:(k[0],int(k[1]==1)))):return 'MATERIAL4',None
    return 'PASS',final
stats=Counter();chosen=None
for tag in (1,2):
    local=Counter()
    for k,ui,vi in product(K,range(11),range(11)):
        result,c=candidate(tag,k,ui,vi)
        local[result]+=1
        if c is None:continue
        status,end=local_end(tag,*c)
        local[status]+=1
        if status=='PASS' and chosen is None:chosen=(tag,k,ui,vi,c,end)
    stats.update(local)
    print('D TAG',tag,sorted(local.items()))
print('D TOTAL',sorted(stats.items()))
if chosen is None:
    print('D NO SECOND BANK')
    raise SystemExit(0)
tag,k,ui,vi,(d,g,goal),pred=chosen
print('D SELECT',tag,k,ui,vi,'INI',d,'CLK',g,'READY',goal)
II=[patch(f,4,d,g) for f in I];hh=[hist(f,ny,114) for f in II]
assert len({w[3] for w in hh})==1
for p,w in enumerate(hh):
    for t in range(115):
        for st in ((0,) if t==0 else (1,0)):
            G=w[st][t];R0=old[p][st][t]
            assert all(col(G,ny,x)==col(R0,ny,x) for x in range(8) if x!=4)
            assert corr(G)==corr(R0)
        if t:assert not any(e[0]==4 for e in w[2][t])
    G=w[0][114]
    assert all(col(G,ny,x)==col(II[p],ny,x) for x in (0,6))
    assert corr(G)==corr(II[p]) and account(arch(G,ny))==account(arch(II[p],ny))
all25={(p,q):load(hh[p][0][114],p,q) for p,q in product(K,repeat=2)}
assert len(set(all25.values()))==10 and all(v==all25[int(p==1),q] for (p,q),v in all25.items())
hs={k:hist(all25[k],ny,256) for k in keys}
for key,w in hs.items():
    for t in range(112):
        for st in ((0,) if t==0 else (1,0)):
            G=w[st][t];R0=sec[key][st][t]
            assert all(col(G,ny,x)==col(R0,ny,x) for x in range(8) if x!=4)
            assert corr(G)==corr(R0)
        if t:assert not any(e[0] in ARCH for e in w[2][t])
    assert tuple(e for e in w[2][112] if e[0] in ARCH)==tuple((4,y,tag) for y in range(0,ny,2) if key[1]==1)
    assert not any(e[0] in ARCH for t in (113,114) for e in w[2][t])
    assert w[0][114]==pred[key]
    assert all(col(w[0][114],ny,x)==col(II[key[1]],ny,x) for x in (0,6))
    assert all(w[0][6][ix(ny,6,y,2)]==scale(V['mark'] if key[1]==1 and y%2==0 else V['gworker']) for y in range(ny))
    assert account(arch(w[0][114],ny))==account(arch(II[key[1]],ny))
end={k:w[0][114] for k,w in hs.items()}
first=lambda f:tuple(mem(f,ny,x) for x in (5,7))
second=lambda f:mem(f,ny,4)
assert clean(parts(end,first,lambda k:k[0])) and clean(parts(end,second,lambda k:int(k[1]==1)))
print('D FULL_RETURN','Q',H.scalar_account(hh[0][3][2]),'H',hh[0][3][2],'SOURCE_WORKER',25,'MATERIAL4',len({tuple(material(f,ny,x) for x in ARCH) for f in end.values()}))
for key in ((0,0),(0,1),(1,0),(1,1)):
    f=end[key]
    print('D END',key,'CORR_INITIAL_DIFF',sum(a!=b for a,b in zip(corr(f),corr(II[key[1]]))),
          'MATERIAL4_COLUMN',material(f,ny,4),'MATERIAL5',material(f,ny,5),'MATERIAL7',material(f,ny,7))
print('D CORR_CLASSES',len({corr(f) for f in end.values()}))
firstloss=secondloss=None;nextB=None
for t in range(115,257):
    if nextB is None:
        hit=next(((key,tuple(e for e in w[2][t] if e[0] in ARCH)) for key,w in hs.items() if any(e[0] in ARCH for e in w[2][t])),None)
        if hit:nextB=t,hit
    for st in (1,0):
        ff={key:w[st][t] for key,w in hs.items()}
        if firstloss is None and not disj(parts(ff,lambda f:tuple(material(f,ny,x) for x in (5,7)),lambda k:k[0])):firstloss=t,st
        if secondloss is None and not disj(parts(ff,lambda f:material(f,ny,4),lambda k:int(k[1]==1))):secondloss=t,st
print('D FUTURE','FIRST_LOSS',firstloss,'SECOND_LOSS',secondloss,'NEXT_ARCHIVE_B',nextB)
print('D PASS two full source/worker returns and separated material records')
