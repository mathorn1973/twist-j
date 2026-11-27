"""NON-CANONICAL alternate exact replay of D-G (#2109).
Uses the independently implemented five-power ring and C/B maps in break.py.
Result-exposed; not a blind review. No import of the public verifier.
"""
from pathlib import Path
from itertools import product
from contextlib import redirect_stdout
from io import StringIO
import runpy,hashlib

root=Path(__file__).resolve().parent
captured=StringIO()
with redirect_stdout(captured):
    V=runpy.run_path(str(root/'break.py'))
assert captured.getvalue()==(root/'EXPECTED.txt').read_text()
Z,O,J=V['Z'],V['O'],V['J']
p,add,sub,sc,mul,h=V['p'],V['add'],V['sub'],V['sc'],V['mul'],V['h']
C,B=V['C'],V['B']
scalar=V['scalar']
P=tuple(p(k) for k in range(5))
def neg(z):return sc(-1,z)
def raw(z):return z[:4]
def ix(ny,x,y):return x*ny+y
def seed(ny,b,k,l=0):
    F=[]
    for x,y in product(range(8),range(ny)):
        d=sc((-1)**y,O)
        if x==0 and y==0:d=P[k]
        if x==0 and y==4 and ny==8:d=P[l]
        F.append((d,neg(d),Z,sc(2*(-1)**(x+b*y),J)))
    return tuple(F)
def transport(F,ny,bit,back=False):
    G=[list(c) for c in F]
    for x,y in product(range(8),range(bit,ny,2)):
        i,k=ix(ny,x,y),ix(ny,x,(y+1)%ny)
        for r in range(3):
            G[i][r],G[k][r]=C(F[i][r],F[k][r],back)
    for x,y in product(range(bit,8,2),range(ny)):
        i,k=ix(ny,x,y),ix(ny,(x+1)%8,y)
        G[i][3],G[k][3]=C(F[i][3],F[k][3],back)
    return tuple(tuple(c) for c in G)
def rsum(seq):return tuple(map(sum,zip(*seq)))
def account(F):
    return (rsum(z for c in F for z in c[:2]),rsum(z for c in F for z in c[2:]),
            rsum(h(z) for c in F for z in c))
def step(F,ny,bit,ac):
    G=transport(F,ny,bit)
    N=tuple(B(c)[0] for c in G)
    assert account(G)==account(N)==ac
    back=tuple(B(c)[0] for c in N)
    assert back==G and transport(back,ny,bit,True)==F
    return N,bit^1
def evolve(F,ny,n):
    ac=account(F);bit=0
    for _ in range(n):F,bit=step(F,ny,bit,ac)
    return F,bit
def shift(F,ny,a):
    return tuple(F[ix(ny,x,(y-a)%ny)] for x,y in product(range(8),range(ny)))
def digest(F,bit):
    t=str(bit)+';'+';'.join(','.join(map(str,raw(z))) for c in F for z in c)
    return hashlib.sha256(t.encode()).hexdigest()

def D():
    wins=[]
    for b,period in ((0,240),(1,80)):
        E={k:seed(4,b,k) for k in range(1,5)}; results={}
        for k in range(1,5):
            F=E[k];bit=0;ac=account(F);hits=[(0,k)];quarter=[raw(F[0][0])]
            for t in range(1,period+1):
                F,bit=step(F,4,bit,ac)
                if bit==0:
                    for l,E0 in E.items():
                        if F==E0:hits.append((t,l))
                assert all(c[1]==neg(c[0]) for c in F)
                if t%(period//4)==0:quarter.append(raw(F[0][0]))
            assert F==E[k] and bit==0
            results[k]=hits
            print('D CASE',b,k,'PERIOD',period,'HITS',hits)
            print('D PORT',b,k,quarter)
        for s in (period//4,3*period//4):
            ok=all((s,2*k%5) in results[k] for k in range(1,5))
            if ok:wins.append((b,s))
            print('D STRIDE',b,s,'MATCHES',sum((s,2*k%5) in results[k] for k in range(1,5)),'WIN',int(ok))
    print('D WINS',wins)
    print('DONE exact fixed-port phase diagnostic')

def E():
    for b,t in ((0,120),(1,40)):
        Fs=[evolve(seed(4,b,k),4,t)[0] for k in range(5)]
        assert len(set(Fs))==5
        sources=[F[0][:2] for F in Fs]
        print('E SOURCE',b,t,[tuple(map(raw,c)) for c in sources])
        varying=[(i,r) for i,r in product(range(32),range(4))
                 if len({F[i][r] for F in Fs})>1]
        sites={i for i,r in varying};vpairs=sorted({2*i+r//2 for i,r in varying})
        injective=[divmod(i,4) for i in range(32) if len({F[i] for F in Fs})==5]
        print('E SUPPORT',b,'SLOTS',len(varying),'SITES',len(sites),'PAIRS',len(vpairs),'LOCAL_INJECTIVE',injective)
        matches=[]
        for c,role in product(range(32),range(2)):
            vals=[(add(F[c][2*role],F[c][2*role+1]),sub(F[c][2*role],F[c][2*role+1])) for F in Fs]
            if len(set(vals))==1:continue
            centers=[u for u,v in vals];diffs=[v for u,v in vals]
            print('E PAIR',b,divmod(c,4),role,'CENTERS',list(map(raw,centers)),'DIFFS',list(map(raw,diffs)),'INJECTIVE',int(len(set(vals))==5))
            if len(set(centers))==1 and diffs[0]!=Z:
                for e in range(1,5):
                    if all(diffs[k]==mul(diffs[0],P[e*k%5]) for k in range(5)):
                        matches.append((c,role,e,diffs[0]))
        strong=[m for m in matches if m[0]!=0 and vpairs==[2*m[0]+m[1]] and all(v==(O,neg(O)) for v in sources)]
        print('E LOCAL_PHASE_RECORDS',b,[(divmod(c,4),r,e,raw(d)) for c,r,e,d in matches])
        print('E STRONG_RELOCATION',b,[(divmod(c,4),r,e,raw(d)) for c,r,e,d in strong])
    print('DONE exact five-input half-period record diagnostic')

def four(b,k,l,s,a):
    F0=seed(8,b,k,l);F=F0;bit=0;ac=account(F);states=[F0]
    for t in range(1,4*s+1):
        F,bit=step(F,8,bit,ac)
        if t%s==0:
            assert bit==0 and F==shift(F0,8,(t//s)*a)
            states.append(F)
    assert F==F0 and bit==0
    return len(set(states[:-1]))

def F_gate():
    for b,s in ((0,120),(1,40)):
        result=[]
        for k in range(5):
            F0=seed(4,b,k);F,bit=evolve(F0,4,s)
            result.append(int(bit==0 and F==shift(F0,4,2)))
        print('F SHUTTLE',b,s,'COMPLETE_TRANSLATION',result)
    wins=[]
    for b,s0 in ((0,120),(1,40)):
        common=None
        for k in range(5):
            F0=seed(8,b,k);F=F0;bit=0;ac=account(F)
            targets={a:shift(F0,8,a) for a in (2,-2)}
            matches=[];period=0
            for t in range(1,257):
                F,bit=step(F,8,bit,ac)
                if bit==0:
                    for a,target in targets.items():
                        if F==target:matches.append((t,a))
                    if not period and F==F0:period=t
            print('F HEIGHT8',b,k,'PERIOD',period,'MATCHES',matches)
            common=set(matches) if common is None else common.intersection(matches)
        common=sorted(common)
        print('F COMMON',b,common)
        for s,a in common:
            counts=[four(b,k,0,s,a) for k in range(5)]
            assert counts==[1,4,4,4,4]
            wins.append((b,s,a))
            print('F FOUR_STROKES',b,s,a,counts)
        for s in sorted({s0}|{s for s,a in common}):
            fam={a:[] for a in (2,-2)}
            for k,l in product(range(5),repeat=2):
                F0=seed(8,b,k,l);F,bit=evolve(F0,8,s)
                for a in fam:
                    if bit==0 and F==shift(F0,8,a):fam[a].append((k,l))
            for a,match in fam.items():
                print('F TWO_PHASE',b,s,a,'MATCHES',match)
                if len(match)==25:
                    counts=[four(b,k,l,s,a) for k,l in product(range(5),repeat=2)]
                    assert all(n in (1,2,4) for n in counts)
                    print('F TWO_PHASE_FOUR',b,s,a,'ORBIT_SIZES',counts)
    print('F WINS',wins)
    print('DONE exact height-8 prolongation')

def G():
    wins=0
    for b,s,a in ((0,120,2),(1,40,-2)):
        hist={2:0,4:0};periods={};bg=seed(8,b,0,0)
        for k,l in product(range(1,5),repeat=2):
            F0=seed(8,b,k,l);F=F0;bit=0;ac=account(F)
            assert scalar(ac[2])==1024
            def values(F):
                v=[]
                for y in (0,2,4,6):
                    c=F[ix(8,0,y)]
                    assert c[1]==neg(c[0])
                    v.append(P.index(c[0]))
                return tuple(v)
            states=[F0];vals=[values(F0)];ds=[digest(F0,bit)];first=0
            for t in range(1,4*s+1):
                F,bit=step(F,8,bit,ac)
                if not first and F==F0 and bit==0:first=t
                if t%s==0:
                    r=t//s
                    assert F==shift(F0,8,r*a) and bit==0
                    expected=list(bg)
                    for y,q in ((r*a%8,k),((4+r*a)%8,l)):
                        i=ix(8,0,y);expected[i]=(P[q],neg(P[q]),*bg[i][2:])
                    assert F==tuple(expected)
                    states.append(F);vals.append(values(F));ds.append(digest(F,bit))
            assert F==F0 and bit==0
            n=len(set(states[:-1]))
            assert n==(2 if k==l else 4)
            assert all(states[i]!=F0 for i in range(1,n)) and states[n]==F0
            hist[n]+=1;periods[first]=periods.get(first,0)+1;wins+=1
            print('G CASE',b,k,l,'STRIDE',s,'SHIFT',a,'PERIOD',first,'STROBE_ORDER',n,'Q',1024)
            print('G PORTS',b,k,l,*vals)
            print('G DIGESTS',b,k,l,*ds)
        assert hist=={2:4,4:12}
        print('G GROUP',b,'STROBE_ORDERS',sorted(hist.items()),'PERIODS',sorted(periods.items()))
    assert wins==32
    print('G PASS 32/32 pairs; 24 exact order-four orbits, 8 exact order-two controls')
    print('DONE exact two-phase four-stroke native transport')
D();E();F_gate();G()
