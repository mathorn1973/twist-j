"""NON-CANONICAL #2123, result-exposed alternate ring/update audit.
Uses the separately implemented cyclic-five-coefficient engine of #2121,
pinned by its exact source hash. Does not import H3 or verify.py.
"""
from pathlib import Path
from fractions import Fraction as Q
import hashlib,runpy
from itertools import product
from collections import Counter
root=Path(__file__).resolve().parent
engine=root/'alternate_predecessor.py'
assert hashlib.sha256(engine.read_bytes()).hexdigest()=='48262b6e7bb600c069952412015385721c894210eec50da11314df792c2ac27e'
E=runpy.run_path(str(engine))
p=E['p'];O,Z,R,J,JI,P=map(E.get,('O','Z','R','J','JI','P'))
add,sub,mul,sc,h,even=map(E.get,('add','sub','mul','sc','h','even'))
raw,flat,cell,ix,rs=map(E.get,('raw','flat','cell','ix','rs'))
C,B,trans,hist,acc,scalar=map(E.get,('C','B','trans','hist','acc','scalar'))
seed,src,worker,store,archive,reader,ret,two=map(E.get,('seed','source','worker','store','archive','reader','ret','two'))
K=range(5);N=(0,2,3,4)
neg=lambda x:sc(-1,x)
def integral(x):
    return all(Q(a).denominator==1 for a in x)
def ints(x):
    assert integral(x)
    return tuple(map(int,x))
alpha=sc(Q(1,2),J)
beta=sc(Q(1,2),sub(O,R))
# Geometric derivative of the fifth-root relation, not the primary inverse routine.
bi=sc(Q(2,5),rs((sc(4,O),sc(3,R),sc(2,P[4]),P[1])))
assert mul(beta,bi)==O
old=[hist(seed(k,'static'),790) for k in K]
I=[w[0][0] for w in old]
assert all(w[3]==old[0][3] for w in old) and scalar(old[0][3][2])==2630
corrections={}
for t in (114,384,758):
    x=old[1][0][t-1][ix(6,0)][3]
    y=old[1][0][t-1][ix(5,0)][3]
    u=I[1][ix(6,0)][3]
    ystar=ints(add(x,mul(bi,sub(u,x))))
    delta=sub(ystar,y)
    assert even(sub(ystar,x)) and C(x,ystar)[0]==u and delta!=Z
    assert all(src(old[k][0][t])==src(I[k]) and worker(old[k][0][t])==worker(I[k]) for k in N)
    assert src(old[1][0][t])==src(I[1]) and store(old[1][1][t])==store(I[1])
    v=list(old[1][0][t-1]);c=v[ix(5,0)];v[ix(5,0)]=c[:3]+(ystar,)
    G=trans(tuple(v),1);F=tuple(B(c)[0] for c in G)
    assert src(F)==src(I[1]) and worker(F)==worker(I[1])
    alias=next(((s,k) for s,k in product(range(1,t-1),K) if (t-1-s)%5==0 and old[k][1][s][ix(5,0)][3]==y),None)
    assert raw(delta)=={114:(12,0,6,6),384:(0,-6,6,-6),758:(12,0,12,0)}[t]
    assert alias=={114:None,384:(3,0),758:(142,1)}[t]
    corrections[t]=(delta,ystar,x,y)
    print('ALT A',t,'DELTA',raw(delta),'YSTAR',raw(ystar),'ALIAS',alias)
# Check all 620 initial candidates' local branch guards and final archive pairs.
delta,ystar,x,rp=corrections[114]
t=113
ws=(Z,)+tuple(sc(n*s,P[k]) for n,s,k in product((1,3,5),(1,-1),range(5)))
def rot(d,n,back=False):
    for _ in range(n%5):d=C(*d,back)
    return d
selected=None
for tag in (1,2):
    # 1-JI=rho/J, 1-J=-rho.
    f=mul(delta,mul(J,P[3]) if tag==1 else neg(P[3]))
    assert mul(sub(O,JI if tag==1 else J),f)==delta
    g=add(rp,sc(2,f));base=mul(JI if tag==1 else J,f)
    goal=ints(sub(g,mul(alpha,delta))),ints(sub(g,mul(beta,delta)))
    counts=Counter()
    for sign,k,w in product((1,-1),range(5),ws):
        d0=mul(base,sc(sign,P[k]));d1=add(d0,sc(2,w))
        ini=rot((d0,d1),t,True);cur=ini;ok=True
        for s in range(1,t+1):
            cur=C(*cur)
            if any(B(cell(cur[y],g,old[k0][1][s][ix(5,y)][3]))[1]!=(tag if s==t and k0==1 and y==0 else 0)
                   for k0,y in product(K,range(2))):
                ok=False;break
        counts['tried']+=1
        if not ok:
            counts['guard_reject']+=1;continue
        assert cur==(d0,d1)
        for k0 in K:
            c0,e0=B(cell(d0,g,old[k0][1][t][ix(5,0)][3]))
            c1,e1=B(cell(d1,g,old[k0][1][t][ix(5,1)][3]))
            assert (e0,e1)==(tag if k0==1 else 0,0)
            if k0==1:assert c0[3]==ystar and c0[2]==sub(g,delta)
            dd=C(c0[0],c1[0]);gg=C(c0[2],c1[2])
            cc=(C(ystar,x)[0] if k0==1 else old[k0][1][114][ix(5,0)][3],old[k0][1][114][ix(5,1)][3])
            c,e=B(cell(dd[0],gg[0],cc[0]));d,e1=B(cell(dd[1],gg[1],cc[1]))
            assert (e,e1)==(0,0)
            assert (c[2],d[2])==(goal if k0==1 else (g,g))
        assert goal[0]!=g and goal[1]!=g
        counts['relative_target']+=1
        if tag==1 and selected is None:selected=f,g,ini,goal
    assert counts=={'tried':310,'guard_reject':10,'relative_target':300}
    print('ALT LOCAL',tag,sorted(counts.items()))
f,g,ini,goal=selected
assert raw(f)==(18,6,6,18) and tuple(map(raw,ini))==((8,7,1,13),(6,5,-1,11))
def setup(k):
    F=list(I[k])
    for y in range(2):
        i=ix(5,y);F[i]=cell(ini[y],g,F[i][3])
    return tuple(F)
hh=[hist(setup(k),370) for k in K];I1=[w[0][0] for w in hh]
assert len({w[3] for w in hh})==1 and scalar(hh[0][3][2])==7752
assert len({reader(f) for f in I1})==1
def pair(F):return F[ix(5,0)][2],F[ix(5,1)][2]
def relation(F):return sub(*pair(F))
for k in K:
    W=hh[k]
    for s in range(1,113):
        F=W[0][s];prev=old[k][0][s]
        assert src(F)==src(prev) and worker(F)==worker(prev)
        assert tuple(c[3] for c in F)==tuple(c[3] for c in prev) and W[2][s][10:12]==(0,0)
    assert W[2][113][10:12]==(int(k==1),0) and W[2][114][10:12]==(0,0)
    assert W[0][113][ix(5,0)][3]==(ystar if k==1 else old[k][0][113][ix(5,0)][3])
    F=W[0][114]
    assert src(F)==src(I1[k]) and worker(F)==worker(I1[k]) and acc(archive(F))==acc(archive(I1[k]))
    assert pair(F)==(goal if k==1 else (g,g))
    assert relation(F)==(neg(mul(R,delta)) if k==1 else Z)
    print('ALT WITNESS',k,'SOURCE',flat(src(F)),'WORKER',flat(worker(F)),'ARCHIVE5',flat(F[10:12]))
assert two([w[0][114] for w in hh],archive)
pl=rl=bl=split=None;negok=True;seen=False;resets=[];records=[];pairresets=[];relresets=[];joint=[]
for s in range(371):
    for stage in ((0,) if s==0 else (1,0)):
        FF=[w[stage][s] for w in hh]
        negok &= all(reader(FF[k])==reader(FF[0]) for k in N);seen |= reader(FF[1])!=reader(FF[0])
        if not negok and split is None:split=(s,stage)
        if s==114 and stage==0:assert negok and seen
        if s>114:
            if pl is None and any(pair(FF[k])!=(goal if k==1 else (g,g)) for k in K):pl=(s,stage)
            if rl is None and any(relation(FF[k])!=(sub(*goal) if k==1 else Z) for k in K):rl=(s,stage)
            if bl is None and any((relation(FF[k])!=Z)!=(k==1) for k in K):bl=(s,stage)
        if stage==0 and s>=114 and s%2==0 and ret(FF,I1,src) and ret(FF,I1,worker):
            resets.append(s)
            if two(FF,archive) and negok and seen:records.append(s)
            if all(pair(FF[k])==(goal if k==1 else (g,g)) for k in K):pairresets.append(s)
            if all(relation(FF[k])==(sub(*goal) if k==1 else Z) for k in K):relresets.append(s)
        if stage==0 and s>0 and s%2==0 and FF==I1:joint.append(s)
assert (pl,rl,bl,split)==((115,1),(115,1),(158,0),None)
assert resets==records==[114,198,244] and pairresets==relresets==[114,244] and not joint
print('ALT SUMMARY','Q',scalar(hh[0][3][2]),'H',raw(hh[0][3][2]),'PAIR',tuple(map(raw,goal)),'REL',raw(sub(*goal)),
      'LOSS',pl,rl,bl,'NEG_SPLIT',split,'RESETS',resets,'RECORDS',records,'PAIR_RESETS',pairresets,'REL_RESETS',relresets,'JOINT',joint)
assert C(O,neg(O))==(R,neg(R)) and add(h(O),h(neg(O)))==add(h(R),h(neg(R)))
print('PASS alternate independent ring, A corrections, B guard/relative local census, selected D full replay')
