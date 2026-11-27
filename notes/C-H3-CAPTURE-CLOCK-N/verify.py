"""NON-CANONICAL #2119, exact clock census and early clocked capture."""
from pathlib import Path
import sys,hashlib,importlib.util,ast,re
from itertools import product
from functools import cache
from collections import Counter
root=Path(__file__).resolve().parent
source=Path(sys.argv[1] if len(sys.argv)>1 else 'reproduce/h3-referenced-record/verify.py')
prev=Path(sys.argv[2] if len(sys.argv)>2 else root/'B_PREV.txt')
raw=source.read_bytes()
assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()=='fd215e24fefbbebf83cf3985d8ebcedd590aa709'
assert hashlib.sha256(prev.read_bytes()).hexdigest()=='83a3879a57fa20e6975f2dad47294f357854ff0d7caf673081e14d55dc2c3488'
spec=importlib.util.spec_from_file_location('h3_pinned',source)
H=importlib.util.module_from_spec(spec);sys.modules[spec.name]=H;spec.loader.exec_module(H)
H.transport_pair=cache(H.transport_pair);H.collision=cache(H.collision)
Z,O,R,J,JI,P=H.ZERO,H.ONE,H.RHO,H.J,H.J_INV,H.J_POWERS
add,sub,mul,sc,h=H.add,H.sub,cache(H.mul),H.scale,H.h
neg=lambda x:sc(-1,x)
L=sub(O,R);m=sub(sc(2,O),R);gs=sc(2,mul(J,m));mR=mul(m,R)
ix=lambda x,y,q:H.index(2,x,y,q)
N=(0,2,3,4)
def rs(xs):return tuple(map(sum,zip(*xs)))
def account(F):
    return rs(z for i,z in enumerate(F) if i%4<2),rs(z for i,z in enumerate(F) if i%4>=2),rs(h(z) for z in F)
def sourcepart(F):return F[:8]
def reader(F):return F[8:]
def cell(F,x,y):
    i=ix(x,y,0);return F[i:i+4]
def matter(F,x):return F[ix(x,0,0)],F[ix(x,1,0)]
def cols(d,g,c):return d,neg(d),g,c
edges=[]
for bit in range(2):
    es=[(ix(x,bit,q),ix(x,1-bit,q)) for x,q in product(range(8),range(3))]
    es += [(ix(x,y,3),ix((x+1)%8,y,3)) for x,y in product(range(bit,8,2),range(2))]
    edges.append(tuple(es))
def trans(F,bit,back=False):
    G=list(F)
    for i,k in edges[bit]:G[i],G[k]=H.transport_pair(F[i],F[k],back)
    return tuple(G)
def collide(F):
    G=[];ts=[]
    for i in range(0,len(F),4):
        c,t=H.collision(F[i:i+4]);G.extend(c);ts.append(t)
    return tuple(G),tuple(ts)
def step(F,bit,ac):
    G=trans(F,bit);N0,ts=collide(G)
    assert account(G)==account(N0)==ac
    back,_=collide(N0)
    assert back==G and trans(back,bit,True)==F
    return G,N0,ts
def hist(F,n,literal=False):
    ac=account(F);cuts=[F];mids=[None];tags=[None]
    for t in range(n):
        G,N0,ts=step(F,t%2,ac)
        if literal:
            C0=H.transport(F,2,t%2);X,ev=H.collide(C0,2)
            assert G==C0 and X==N0
            assert tuple(dict(((x,y),k) for x,y,k in ev).get((x,y),0) for x,y in product(range(8),range(2)))==ts
        F=N0;cuts.append(F);mids.append(G);tags.append(ts)
    return cuts,mids,tags,ac
def word(hh,t):
    cuts,mids,_,_=hh
    return tuple(reader(F) for u in range(t+1) for F in ((cuts[u],) if u==0 else (mids[u],cuts[u])))
V=(Z,)+tuple(sc(s,P[k]) for s in (1,-1) for k in range(5))
def stock(n,l,vi):
    u=sc(n,P[l]);a=mul(L,u);v=V[vi];z=mul(L,v)
    b=sub(add(mR,mul(J,a)),sc(4,mul(J,u)));c2=add(mR,mul(L,a))
    if H.even(b) or (z!=Z and (H.even(z) or H.even(sub(z,c2)))):return None
    return Z,sc(2,v),sc(2,v),b,b,b,add(mR,sc(2,a))
def seed(p,st):
    F=[]
    for x,y in product(range(8),range(2)):
        d=(p if y==0 else sc(3,P[1])) if x==0 else Z
        g=gs if x==0 else Z
        c=(Z if x==0 else st[x-1]) if y==0 else gs
        F.extend(cols(d,g,c))
    return tuple(F)
port=ix(6,0,2);ref=ix(6,1,2);corr=ix(6,0,3)
def A():
    hist_all=Counter();hist_first=Counter();stocks=0;total=0
    for line in prev.read_text().splitlines():
        mat=re.match(r'^B STOCK (-?\d+) (\d+) (\d+) .* MATCHES (\[.*?\]) NEGATIVE_SPLIT ',line)
        if not mat:continue
        n,l,vi=map(int,mat.groups()[:3]);times=ast.literal_eval(mat[4])
        if not times:continue
        st=stock(n,l,vi);assert st is not None
        hh=[hist(seed(p,st),max(times)) for p in P];stocks+=1
        assert len({w[3] for w in hh})==1
        for k,T in enumerate(times):
            assert all(sourcepart(w[0][T])==sourcepart(w[0][0]) for w in hh)
            assert len({word(w,T) for w in hh})==2 and len({word(hh[i],T) for i in N})==1
            r=hh[1][1][T][corr]
            assert hh[1][0][T][corr]==r and all(hh[i][0][T][corr]!=r for i in N)
            old=[(t,i) for t,i in product(range(1,T),range(5)) if hh[i][1][t][corr]==r]
            same=[(t,i) for t,i in old if (T-t)%5==0]
            key=(bool(old),bool(same));hist_all[key]+=1;total+=1
            if k==0:hist_first[key]+=1
            print('A WITNESS',n,l,vi,T,'EARLIEST',old[0] if old else None,'SAME_MOD5',same[0] if same else None)
    assert (stocks,total)==(143,202)
    print('A ALL',total,sorted(hist_all.items()))
    print('A FIRST',stocks,sorted(hist_first.items()))

def Cpow(pair,t,back=False):
    for _ in range(t):pair=H.transport_pair(*pair,back)
    return pair
def make_clock(f,w,t):
    d0=mul(JI,f);ready=(d0,add(d0,sc(2,w)))
    initial=Cpow(ready,t,True)
    assert Cpow(initial,t)==ready
    assert Cpow(initial,5)==initial and H.even(sub(*initial))
    assert all(Cpow(initial,i)!=initial for i in range(1,5))
    return initial,ready
def setup(F,initial,g):
    N0=list(F)
    for y,d in enumerate(initial):
        N0[ix(6,y,0):ix(6,y,0)+3]=(d,neg(d),g)
    return tuple(N0)
def pretest(old,t,f,w):
    Rpos=old[1][1][t][corr];g=add(Rpos,sc(2,f))
    initial,ready=make_clock(f,w,t)
    static_early=any(H.collision(cols(ready[0],g,old[k][1][u][corr]))[1]
                     for u,k in product(range(1,t),range(5)))
    ds=initial
    for u in range(1,t+1):
        ds=Cpow(ds,1)
        for k,y in product(range(5),range(2)):
            z=old[k][1][u][ix(6,y,3)]
            tag=H.collision(cols(ds[y],g,z))[1]
            if tag!=int(u==t and k==1 and y==0):return None
    return initial,ready,g,add(g,mul(sub(JI,O),f)),static_early
def trial(old,t,initial,ready,g,mark,ks,through=160,collect=False):
    F={k:setup(old[k][0][0],initial,g) for k in ks}
    ini=F.copy();acs={k:account(ff) for k,ff in F.items()}
    assert len(set(acs.values()))==1
    assert all(reader(ff)==reader(ini[ks[0]]) for ff in ini.values())
    heads=[];matches=[];active=True;neg_same=True;pos_seen=False;loss=None
    for u in range(1,through+1):
        MM={};TT={};NN={}
        for k,ff in F.items():
            G,N0,ts=step(ff,(u-1)%2,acs[k])
            MM[k]=G;NN[k]=N0;TT[k]=ts
            if u<t:
                if sourcepart(N0)!=sourcepart(old[k][0][u]) or any(N0[i]!=old[k][0][u][i] for i in range(3,len(N0),4)) or any(ts[12:14]):
                    return 'EARLY_CONTINUATION',[],None
            elif u==t:
                if matter(G,6)!=ready or any(G[ix(6,y,2)]!=g or G[ix(6,y,3)]!=old[k][1][u][ix(6,y,3)] for y in range(2)) or ts[12:14]!=(int(k==1),0):
                    return 'CAPTURE_GUARD',[],None
                if N0[port]!=(mark if k==1 else g) or N0[ref]!=g:
                    return 'CAPTURE_OUTPUT',[],None
        for stage,states in ((1,MM),(0,NN)):
            neg_same &= len({reader(ff) for k,ff in states.items() if k!=1})==1
            pos_seen |= reader(states[1])!=reader(states[ks[0] if ks[0]!=1 else ks[1]])
            if u>t and active and any(ff[port]!=(mark if k==1 else g) or ff[ref]!=g for k,ff in states.items()):
                active=False;loss=(u,stage)
        F=NN
        if collect:heads.append((u,MM,NN,TT,neg_same,pos_seen,active))
        if u>=t and u%2==0 and active and neg_same and pos_seen and all(sourcepart(F[k])==sourcepart(ini[k]) for k in ks):
            matches.append(u)
        if not collect and not active:break
        if not collect and not neg_same:break
    return ('PASS' if matches else 'NO_HELD_RETURN'),matches,(ini,acs,heads,loss)
def B():
    counts=Counter();wins=0
    vecs=tuple(v for v in product(range(2),repeat=4) if any(v))
    ws=tuple(sc(s,P[k]) for s in (1,-1) for k in range(5))
    for n,l in product((-3,-1,1,3),range(5)):
        st=stock(n,l,0)
        if st is None:
            print('B STOCK_REJECT',n,l);continue
        old=[hist(seed(p,st),160) for p in P]
        for t in range(3,13):
            rpos=old[1][1][t][corr];rn={old[k][1][t][corr] for k in N}
            if len(rn)!=1 or rpos in rn:
                print('B CUT_REJECT',n,l,t);continue
            local=Counter()
            for v,N0,w in product(vecs,(1,3,5),ws):
                f=sc(N0,v)
                counts['tried']+=1;local['tried']+=1
                pre=pretest(old,t,f,w)
                if pre is None:
                    counts['guard_rejected']+=1;local['guard_rejected']+=1;continue
                ini,ready,g,mark,static=pre
                counts['pretest_pass']+=1;local['pretest_pass']+=1
                status,mm,_=trial(old,t,ini,ready,g,mark,(0,1))
                if not mm:
                    counts['screen_'+status]+=1;local['screen_'+status]+=1;continue
                status,mm,info=trial(old,t,ini,ready,g,mark,tuple(range(5)),collect=True)
                if not mm:
                    counts['full_'+status]+=1;local['full_'+status]+=1;continue
                wins+=1;counts['success']+=1;local['success']+=1
                initial,acs,heads,loss=info;T=mm[0]
                print('B CUT',n,l,t,sorted(local.items()))
                print('B COUNTS',sorted(counts.items()))
                print('B SELECT',n,l,t,'F',f,'W',w,'INITIAL_D',ini,'READY_D',ready,'G',g,'MARK',mark,'STATIC_EARLY',int(static),'RETURNS',mm,'FIRST_LOSS',loss)
                print('B ACCOUNT',acs[0],'Q',H.scalar_account(acs[0][2]))
                allh=[hist(initial[k],160,True) for k in range(5)]
                for k,hh in enumerate(allh):
                    assert sourcepart(hh[0][T])==sourcepart(hh[0][0]) and hh[0][T][port]==(mark if k==1 else g) and hh[0][T][ref]==g
                    print('B WITNESS',k,'SOURCE',sourcepart(hh[0][T]),'OUT',hh[0][T][port],'REF',hh[0][T][ref])
                for u,MM,NN,TT,ns,ps,ac in heads:
                    if u<=max(T,t+1):
                        print('B WINDOW',u,'CLOCK_PRE',matter(MM[1],6),'CLOCK_POST',matter(NN[1],6),'TAGS',tuple(TT[k][12:14] for k in range(5)),'PORTS',tuple(NN[k][port] for k in range(5)),'SOURCE_MATCH',sum(sourcepart(NN[k])==sourcepart(initial[k]) for k in range(5)),'CLASSES',len({word(h,u) for h in allh}),'HOLD',int(ac))
                print('B PASS 5/5 clocked early capture, full source restored with held record')
                return
            print('B CUT',n,l,t,sorted(local.items()))
    print('B COUNTS',sorted(counts.items()))
    print('B NO QUALIFYING CLOCKED ECHO')
def C():
    initial,ready=make_clock(O,P[1],3)
    F=[]
    for x,y in product(range(8),range(2)):
        F.extend(cols(initial[y] if x==6 else Z,sc(2,O) if x==6 else Z,Z if y==0 else sc(2,O)))
    # Preregistration says both CLK=2 in column6, other columns zero.
    F=tuple(F);hh=hist(F,12,True);cut,mid,tags,ac=hh
    first=next((t for t in range(1,13) if any(tags[t])),None)
    print('C CLOCK_INITIAL',initial,'READY',ready,'FREE_PERIOD',5,'Q',H.scalar_account(ac[2]))
    print('C FIRST',first)
    for t in range(1,13):
        print('C TICK',t,'PRE',matter(mid[t],6),'POST',matter(cut[t],6),'TAGS',tags[t][12:14],'CLK',cut[t][port],'REF',cut[t][ref])
    ok=first==3 and tags[3][12:14]==(1,0)
    print('C RESULT',int(ok))
if __name__=='__main__':
    A();B();C()
