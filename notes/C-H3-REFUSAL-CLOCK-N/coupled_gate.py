"""NON-CANONICAL #2135 H: two refusal wheels and exact delayed native gate."""
from pathlib import Path
import runpy
from itertools import product,combinations
from fractions import Fraction as Q
from collections import Counter
V=runpy.run_path(str(Path(__file__).resolve().parent/'verify.py'))
H=V['H'];Z,O,R,J,JI,P=map(V.get,('Z','O','R','J','JI','P'))
add,sub,mul,sc,h,neg=map(V.get,('add','sub','mul','sc','h','neg'))
vert=V['vert']
TARGETS=(114,90,89)
def families(n):
    for (y,z),(a,b) in product(combinations(range(2,n,2),2),product((-3,-2,-1,1,2,3),repeat=2)):
        d=[Z]*n;d[0]=O;d[1]=neg(O);d[y]=sc(a,O);d[z]=sc(b,O)
        yield ('G',y,z,a,b),tuple(d)
    if n==14:return
    for seed in [None]+list(product(range(2,n,2),range(5),(1,2))):
        d=[Z]*n;d[0]=O;d[1]=neg(O)
        if seed:
            y,k,m=seed;d[y]=sc(m,P[k])
        yield ('B',seed),tuple(d)
def traj(ini,nsteps):
    n=len(ini);v=ini;cuts=[v];words=[[] for y in range(n)]
    for t in range(1,nsteps+1):
        bit=(t-1)%2;nxt,mask=vert(v,bit)
        for y in range(n):
            k=(y+1)%n if y%2==bit else (y-1)%n
            words[y].append('R' if not H.even(sub(v[y],v[k])) else 'C' if nxt[y]!=v[y] else '=')
        v=nxt;cuts.append(v)
    return cuts,words
def masks():
    out={};counts=Counter();total=Counter()
    for n in (6,8,10,12,14):
        table={(T,y):{} for T,y in product(TARGETS,range(n))}
        for name,ini in families(n):
            total[n]+=1
            cuts,words=traj(ini,146)
            for y in range(n):
                vals={};rpre=[0];cpre=[0]
                for i,z in enumerate(cuts):vals[z[y]]=vals.get(z[y],0)|(1<<i)
                for w in words[y]:
                    rpre.append(rpre[-1]+(w=='R'));cpre.append(cpre[-1]+(w=='C'))
                for T,s in product(TARGETS,range(0,33,2)):
                    if rpre[s+T-1]==rpre[s] or cpre[s+T]==cpre[s]:continue
                    d=cuts[s+T][y]
                    # Bits 0..T-2 correspond to earlier cuts 1..T-1.
                    mask=(vals[d]>>(s+1))&((1<<(T-1))-1)
                    counts[T,n,y]+=1
                    table[T,y].setdefault(mask,(name,ini,s))
        for (T,y),d in table.items():out[T,n,y]=d
        print('H VECTORS',n,total[n],flush=True)
    for T in TARGETS:
        selected=None;tot=Counter()
        for n in (6,8,10,12,14):
            for y in range(n):
                d=out[T,n,y];items=list(d)
                pairs=0;first=None
                # Ordered insertion indices i<=j, unordered distinct masks,
                # with the empty-mask self-pair explicitly admitted.
                for i,a in enumerate(items):
                    for b in items[i:]:
                        if a&b or (a==b and a!=0):continue
                        pairs+=1
                        if first is None:first=(a,b)
                tot['wheels']+=counts[T,n,y];tot['masks']+=len(items);tot['disjoint_pairs']+=pairs
                if first is not None and selected is None:
                    a,b=first;selected=(n,y,a,b,d[a],d[b])
            print('H HEIGHT',T,n,'WHEELS',sum(counts[T,n,y] for y in range(n)),'MASKS',sum(len(out[T,n,y]) for y in range(n)))
        print('H CENSUS',T,sorted(tot.items()),'SELECT',selected,flush=True)
        if selected is not None:yield T,selected
def acct(F):
    return H.ring_sum(z for i,z in enumerate(F) if i%4<2),H.ring_sum(z for i,z in enumerate(F) if i%4>=2),H.ring_sum(h(z) for z in F)
def solve(T,sel):
    n,y,ma,mb,(nameu,iu,su),(namev,iv,sv)=sel
    U,wu=traj(iu,146);Vv,wv=traj(iv,146)
    u=tuple(z[y] for z in U[su:su+T+1]);v=tuple(z[y] for z in Vv[sv:sv+T+1])
    assert ma==sum(1<<(t-1) for t in range(1,T) if u[t]==u[T])
    assert mb==sum(1<<(t-1) for t in range(1,T) if v[t]==v[T])
    assert not ma&mb
    assert H.scalar_account(h(mul(J,J)))!=H.scalar_account(h(O))
    T2=mul(H.T,H.T);bound=4*(T-1)+1
    def balance(d,w):return h(d) in (h(w),mul(T2,h(w)))
    for N in range(1,bound+1):
        w=sc(N,O)
        if all(not balance(sub(sc(Q(1,2),sub(u[t],u[T])),w),w) for t in range(1,T) if v[t]==v[T]):break
    else:raise AssertionError('root bound N')
    for M in range(1,2*bound,2):
        if all(not balance(sub(sc(Q(1,2),sub(sub(u[t],u[T]),sc(M,sub(v[t],v[T])))),w),w) for t in range(1,T) if v[t]!=v[T]):break
    else:raise AssertionError('root bound M')
    c0=add(sub(u[T],sc(M,v[T])),sc(2,w));f=neg(mul(J,w))
    for t in range(1,T):
        d=sc(Q(1,2),sub(u[t],add(sc(M,v[t]),c0)))
        assert not balance(d,w)
    assert sc(Q(1,2),sub(u[T],add(sc(M,v[T]),c0)))==neg(w)
    initu=U[su];initv=tuple(add(sc(M,z),c0) for z in Vv[sv])
    print('H DESIGN',T,'HEIGHT',n,'ROW',y,'U',nameu,su,'V',namev,sv,'N',N,'M',M,'TRANSLATION',c0,'F',f,'INIT_U',initu,'INIT_V',initv)
    print('H WORDS',T,''.join(wu[y][su:su+T]),''.join(wv[y][sv:sv+T]))
    F=[]
    G0=sc(2,f)
    for x,k in product(range(8),range(n)):
        F.extend((initu[k] if x==0 else Z,initv[k] if x==0 else Z,G0 if x==0 else Z,Z if k==y else G0))
    I=F=tuple(F);ac=acct(F);i=H.index(n,0,y,0);mark=None;hold=0;active=True
    for t in range(1,T+33):
        G=H.transport(F,n,(t-1)%2);N0,ev=H.collide(G,n)
        assert acct(G)==acct(N0)==ac and H.collide(N0,n)[0]==G and H.transport(G,n,(t-1)%2,True)==F
        if t<T:assert not ev
        if t<=T:
            assert G[2::4]==I[2::4] and G[3::4]==I[3::4]
            for k in range(n):
                z=H.index(n,0,k,0)
                assert G[z:z+2]==(U[su+t][k],add(sc(M,Vv[sv+t][k]),c0))
        if t==T:
            assert ev==((0,y,1),);mark=N0[i+2];assert mark!=G0
            print('H WRITE',T,'PRE',G[i:i+4],'POST',N0[i:i+4],'ACCOUNT',ac,'Q',H.scalar_account(ac[2]))
        if t>T and active:
            if G[i+2]==N0[i+2]==mark:hold+=1
            else:active=False
        F=N0
    print('H HOLD',T,hold,'OF',32)
    print('H PASS',T,'literal first write and conserved accounts')
if __name__=='__main__':
    wins=list(masks())
    print('H TARGETS_WITH_PAIR',tuple(T for T,s in wins))
    for T,s in wins:solve(T,s)
    print('DONE paired refusal clocks')
