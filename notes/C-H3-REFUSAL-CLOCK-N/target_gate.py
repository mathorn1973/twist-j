"""NON-CANONICAL #2135 G: separately frozen 114-tick refusal clock search."""
from pathlib import Path
import runpy
from itertools import product,combinations
from fractions import Fraction as Q
from collections import Counter
V=runpy.run_path(str(Path(__file__).resolve().parent/'verify.py'))
H=V['H'];Z,O,R,J,JI,P=map(V.get,('Z','O','R','J','JI','P'))
add,sub,mul,sc,h,neg=map(V.get,('add','sub','mul','sc','h','neg'))
vert=V['vert']
roots=tuple(sc(s,P[k]) for s,k in product((1,-1),range(5)))
def trajectory(ini,limit):
    n=len(ini);v=ini;cuts=[v];words=[[] for y in range(n)]
    for t in range(1,limit+1):
        bit=(t-1)%2;nxt,mask=vert(v,bit)
        for y in range(n):
            j=(y+1)%n if y%2==bit else (y-1)%n
            words[y].append('R' if not H.even(sub(v[y],v[j])) else 'C' if nxt[y]!=v[y] else '=')
        v=nxt;cuts.append(v)
    return cuts,words
def search():
    stats=Counter()
    for n in (6,8,10,12,14):
        local=Counter()
        for (y,z),(a,b) in product(combinations(range(2,n,2),2),product((-3,-2,-1,1,2,3),repeat=2)):
            d=[Z]*n;d[0]=O;d[1]=neg(O);d[y]=sc(a,O);d[z]=sc(b,O);ini=tuple(d)
            cuts,words=trajectory(ini,146)
            local['vectors']+=1
            for s,k in product(range(0,33,2),range(n)):
                local['row_phase']+=1
                dstar=cuts[s+114][k]
                if any(cuts[s+u][k]==dstar for u in range(1,114)):
                    local['repeated']+=1;continue
                word=''.join(words[k][s:s+114])
                if 'R' not in word[:-1] or 'C' not in word:
                    local['no_refusal_change']+=1;continue
                local['rare']+=1
                for w,tag in product(roots,(1,2)):
                    local['gates']+=1
                    v=add(dstar,sc(2,w));f=mul(J if tag==1 else JI,neg(w))
                    G=sc(2,f)
                    hit=next((u,H.collision((cuts[s+u][k],v,G,Z))[1]) for u in range(1,115) if H.collision((cuts[s+u][k],v,G,Z))[1])
                    if hit!=(114,tag):local['earlier']+=1;continue
                    local['pass']+=1
                    stats.update(local)
                    print('G HEIGHT',n,sorted(local.items()))
                    print('G COUNTS',sorted(stats.items()))
                    return (n,y,z,a,b,s,k,w,tag,ini,cuts[s],dstar,v,f,word)
        stats.update(local)
        print('G HEIGHT',n,sorted(local.items()),flush=True)
    assert stats['vectors']==1260
    print('G COUNTS',sorted(stats.items()))
    return None
def account(F):
    return H.ring_sum(z for i,z in enumerate(F) if i%4<2),H.ring_sum(z for i,z in enumerate(F) if i%4>=2),H.ring_sum(h(z) for z in F)
def replay(best):
    n,y,z,a,b,s,k,w,tag,ini,d0,dstar,v,f,word=best
    print('G SELECT',best)
    F=[]
    G0=sc(2,f)
    for x,yy in product(range(8),range(n)):
        F.extend((d0[yy] if x==0 else Z,v if x==0 else Z,G0 if x==0 else Z,Z if yy==k else G0))
    F0=F=tuple(F);ac=account(F);i=H.index(n,0,k,0);mark=None;hold=0;active=True
    for t in range(1,147):
        G=H.transport(F,n,(t-1)%2);N,ev=H.collide(G,n)
        assert H.collide(N,n)[0]==G and H.transport(G,n,(t-1)%2,True)==F and account(G)==account(N)==ac
        if t<114:assert not ev
        if t<=114:
            assert G[i+1:i+4]==(v,G0,Z)
            assert G[2::4]==F0[2::4] and G[3::4]==F0[3::4]
        if t==114:
            assert ev==((0,k,tag),) and G[i]==dstar
            mark=N[i+2];assert mark!=G0
            print('G WRITE','PRE',G[i:i+4],'POST',N[i:i+4],'ACCOUNT',ac,'Q',H.scalar_account(ac[2]))
        if t>114 and active:
            if G[i+2]==N[i+2]==mark:hold+=1
            else:active=False
        F=N
    print('G HOLD',hold)
    vv=ini;period=None
    for t in range(1,4097):
        vv,_=vert(vv,(t-1)%2)
        if t%2==0 and vv==ini:period=t;break
    print('G FREE_PERIOD',period)
    def lin(a,b):
        center=sc(Q(1,2),add(a,b));delta=sc(Q(1,2),mul(R,sub(a,b)))
        return add(center,delta),sub(center,delta)
    vv=d0;first=None
    for t in range(1,115):
        out=list(vv);bit=(t-1)%2
        for y in range(bit,n,2):
            z=(y+1)%n;out[y],out[z]=lin(vv[y],vv[z])
        vv=tuple(out)
        d=sc(Q(1,2),sub(vv[k],v))
        b0=1 if d!=Z and h(f)==mul(H.T,h(d)) else 2 if f!=Z and h(d)==mul(H.T,h(f)) else 0
        if b0 and first is None:first=t,b0
    print('G FORCED_LINEAR','FIRST_BALANCE',first,'SAME_READY',int(vv[k]==dstar),'TARGET_R0',vv[k])
    print('G PASS native first write at114')
if __name__=='__main__':
    best=search()
    if best is None:print('G NO EXACT114')
    else:replay(best)
