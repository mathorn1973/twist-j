"""NON-CANONICAL exact local reader / paired motor audit, frozen issue #2111."""
import sys,hashlib,importlib.util
from pathlib import Path
from itertools import product,permutations
from functools import cache
from collections import Counter
from fractions import Fraction

source=Path(sys.argv[1] if len(sys.argv)>1 else 'reproduce/h3-referenced-record/verify.py')
raw=source.read_bytes()
assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()=='fd215e24fefbbebf83cf3985d8ebcedd590aa709'
spec=importlib.util.spec_from_file_location('h3_pinned',source)
H=importlib.util.module_from_spec(spec);sys.modules[spec.name]=H
spec.loader.exec_module(H)
H.transport_pair=cache(H.transport_pair);H.collision=cache(H.collision)
Z,O,J,P=H.ZERO,H.ONE,H.J,H.J_POWERS
add,sub,mul,h,scale=H.add,H.sub,cache(H.mul),H.h,H.scale
neg=lambda x:scale(-1,x)
v=add(P[2],P[3]); W=lambda f:mul(P[4],H.sigma(f,2)); K=lambda x:mul(v,H.sigma(x,2))
ROOTS=tuple(P[pow(2,r,5)] for r in range(4))
NY=8;NX=8
SPECS=((0,120,2),(1,40,-2))
idx=lambda x,y,rail: H.index(NY,x,y,rail)

def rsum(xs):return tuple(map(sum,zip(*xs)))
def account(F):
    return rsum(z for i,z in enumerate(F) if i%4<2),rsum(z for i,z in enumerate(F) if i%4>=2),rsum(h(z) for z in F)
def seed(b,markers):
    F=[]
    for x,y in product(range(NX),range(NY)):
        d=markers.get((x,y),scale((-1)**y,O))
        F.extend((d,neg(d),Z,scale(2*(-1)**(x+b*y),J)))
    return tuple(F)
def single(b,k=1,l=2,r=0,a=None):
    if a is None:a=SPECS[b][2]
    return seed(b,{(0,a*r%8):P[k],(0,(4+a*r)%8):P[l]})
def shift(F,a):
    return tuple(F[idx(x,(y-a)%NY,q)] for x,y,q in product(range(NX),range(NY),range(4)))
def step(F,bit,ac):
    G=H.transport(F,NY,bit)
    N,ev=H.collide(G,NY)
    back,_=H.collide(N,NY)
    assert back==G and H.transport(back,NY,bit,backward=True)==F
    assert account(G)==account(N)==ac
    return G,N,{(x,y):t for x,y,t in ev}
def history(F0,n):
    ac=account(F0);F=F0;bit=0
    cuts=[F0];mids=[None];tags=[None]
    for _ in range(n):
        G,F,E=step(F,bit,ac);bit^=1
        mids.append(G);cuts.append(F);tags.append(E)
    return cuts,mids,tags,ac
def det(M):
    n=len(M)
    return sum((-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
               *prodint(M[i][p[i]] for i in range(n)) for p in permutations(range(n)))
def prodint(a):
    t=1
    for z in a:t*=z
    return t
def decoder(vals):
    M=tuple(zip(*vals)); d=det(M)
    if abs(d)!=1:return None
    # Inverse of the column matrix, followed by multiplication by root columns.
    inv=tuple(tuple(((-1)**(i+j)*det(tuple(tuple(M[r][c] for c in range(4) if c!=i)
                    for r in range(4) if r!=j)))//d for j in range(4)) for i in range(4))
    D=tuple(tuple(sum(ROOTS[k][i]*inv[k][j] for k in range(4)) for j in range(4)) for i in range(4))
    assert tuple(applyD(D,x) for x in vals)==ROOTS
    return D
def applyD(D,x):
    return tuple(sum(a*b for a,b in zip(row,x)) for row in D)
def aff(vals):
    A=mul(sub(ROOTS[1],ROOTS[0]),H.inverse(sub(vals[1],vals[0])))
    B=sub(ROOTS[0],mul(A,vals[0]))
    assert A!=Z
    return (A,B) if tuple(add(mul(A,x),B) for x in vals)==ROOTS else None
def integral(x):
    return all(Fraction(t).denominator==1 for t in x)
def text_ring(z):
    return ','.join(str(t) for t in z)
def repr_mat(M):
    return ';'.join(text_ring(r) for r in M)
def rec_at(Hist,a,t,x,y):
    cuts,mids,tags,ac=Hist
    out=[]
    for r in range(4):
        yy=(y-a*r)%8
        pos=idx(x,yy,0)
        out.append((cuts[t-1][pos+2:pos+4],mids[t][pos+2:pos+4],
                    cuts[t][pos+2:pos+4],tags[t].get((x,yy),0)))
    return tuple(out)
def holds(Hist,a,t,x,y):
    # Number of subsequent consecutive substeps at which CLK has exactly its
    # post-B value; first actual change ends the hold. Cap at one full cycle.
    cuts,mids,tags,ac=Hist
    period=(len(cuts)-1)//4
    out=[]
    for r in range(4):
        yy=(y-a*r)%8;pos=idx(x,yy,2)
        val=cuts[t][pos];n=0
        for dt in range(1,period+1):
            u=(t+dt-1)%period+1
            if mids[u][pos]!=val:break
            n+=1
            if cuts[u][pos]!=val:break
            n+=1
        out.append(n)
    return tuple(out)

def A_gate():
    names=('distinct','allwrite','ready','affine','integral_affine','unimodular')
    first={}; allhist={}; hs={}
    for b,s,a in SPECS:
        F0=single(b); Hist=history(F0,4*s);hs[b]=Hist
        cuts,mids,tags,ac=Hist
        assert H.scalar_account(ac[2])==1024
        for r in range(5):assert cuts[r*s]==shift(F0,r*a)
        hist=Counter()
        for t,x,y in product(range(1,s+1),range(8),range(8)):
            rec=rec_at(Hist,a,t,x,y)
            vals=tuple(e[2][0] for e in rec)
            if len(set(vals))!=4:continue
            local=['distinct'];A=None;D=None
            if all(e[1][0]!=e[2][0] for e in rec):
                assert all(e[3] in (1,2) for e in rec)
                local.append('allwrite')
                if len({e[1][0] for e in rec})==1:local.append('ready')
                A=aff(vals)
                if A:
                    local.append('affine')
                    if all(integral(v) for v in A):local.append('integral_affine')
                D=decoder(vals)
                if D:local.append('unimodular')
            for name in local:
                hist[name]+=1
                first.setdefault(name,(b,t,x,y,rec,A,D))
        allhist[b]=hist
        print('A COUNTS',b,[(k,hist[k]) for k in names])
    for name in names:
        if name not in first:
            print('A EMPTY',name);continue
        b,t,x,y,rec,A,D=first[name]
        _,s,a=SPECS[b]; Hist=hs[b]
        vals=tuple(e[2][0] for e in rec)
        print('A PORT',name,b,t,x,y,'HOLD_SUBSTEPS',holds(Hist,a,t,x,y),'DET',det(tuple(zip(*vals))))
        for r,e in enumerate(rec):
            print('A LOCAL',name,r,'PRE',repr_mat(e[0]),'POST_C',repr_mat(e[1]),'POST_B',repr_mat(e[2]),'TAG',e[3])
        if name in ('affine','integral_affine'):
            assert A
            print('A AFFINE',name,text_ring(A[0]),text_ring(A[1]))
            read=lambda val: add(mul(A[0],val),A[1])
        elif name=='unimodular':
            assert D
            print('A MATRIX',name,repr_mat(D))
            read=lambda val:applyD(D,val)
        else:
            # Membership test of four actual raw values, not an arithmetic read.
            read=lambda val: ROOTS[vals.index(val)] if val in vals else None
        # The four preparations are even translates of the same full orbit.
        # Audit literally from all four rotations across four complete cycles.
        for r in range(4):
            F=single(b,r=r);F0=F;ac=account(F);bit=0
            for n in range(1,16*s+1):
                G,N,E=step(F,bit,ac);bit^=1
                if (n-1)%s+1==t:
                    phase=(r+(n-1)//s)%4;pos=idx(x,y,0)
                    assert (F[pos+2:pos+4],G[pos+2:pos+4],N[pos+2:pos+4],E.get((x,y),0))==rec[phase]
                    assert read(N[pos+2])==ROOTS[phase]
                F=N
            assert F==F0 and bit==0
        for k,l in ((0,0),(1,1),(2,2)):
            Hist0=history(single(b,k,l),t)
            aliases=[]
            for r in range(4):
                val=Hist0[0][t][idx(x,(y-a*r)%8,2)]
                z=read(val)
                aliases.append(ROOTS.index(z) if z in ROOTS else -1)
            print('A CONTROL',name,k,l,aliases)
    print('A DONE fixed native writes and local observations')

def B_gate():
    wins=[];total=0
    for b,s,a in SPECS:
        for c in range(1,8):
            matched=[]
            for r,u in product(range(4),repeat=2):
                marks={(0,a*r%8):P[1],(0,(4+a*r)%8):P[2],
                       (c,a*u%8):P[3],(c,(4+a*u)%8):P[4]}
                F0=seed(b,marks);F=F0;ac=account(F);bit=0
                assert H.scalar_account(ac[2])==1024
                for _ in range(s):
                    _,F,_=step(F,bit,ac);bit^=1
                if F==shift(F0,a) and bit==0:matched.append((r,u))
                total+=1
            print('B TRACKS',b,c,'COUNT',len(matched),'MATCHES',matched)
            if len(matched)==16:
                wins.append((b,c))
                for r,u in matched:
                    marks={(0,a*r%8):P[1],(0,(4+a*r)%8):P[2],
                           (c,a*u%8):P[3],(c,(4+a*u)%8):P[4]}
                    F0=seed(b,marks);cuts,_,_,_=history(F0,4*s)
                    assert all(cuts[s*i]==shift(F0,a*i) for i in range(5))
                    assert len({cuts[s*i] for i in range(4)})==4
    assert total==224
    print('B WINS',wins,'PREPARATIONS',total)

def C_gate():
    tags=((1,2),(1,3),(1,4),(2,3))
    xs=[P[1]];fs=[P[2]]
    for i in range(4):xs.append(K(xs[-1]));fs.append(W(fs[-1]))
    assert xs[4]==xs[0] and fs[4]==fs[0]
    assert len(set(xs[:4]))==len(set(fs[:4]))==4
    for x,f in product((O,P[1],P[2],P[3]),repeat=2):
        assert mul(K(x),W(f))[3]==mul(x,f)[3]
    assert len({(x,f) for x,f in product(xs[:4],fs[:4])})==16
    words={};fields=set();pairs=set();invariants={}
    for d,(k,l) in enumerate(tags):
        F0=single(1,k,l);Hist=history(F0,160);cuts=Hist[0]
        assert all(cuts[40*n]==shift(F0,-2*n) for n in range(5))
        for r in range(4):
            F=single(1,k,l,r); assert F==shift(F0,-2*r)
            assert F not in fields;fields.add(F)
            word=tuple(P.index(cuts[40*((r+n)%4)][idx(0,0,0)]) for n in range(4))
            assert word.count(k)==word.count(l)==1 and word.count(0)==2
            # Actual temporal record at the same fixed material port.
            observed=tuple(sorted(x for x in word if x))
            rd=tags.index(observed);rr=(-word.index(observed[0]))%4
            assert (rd,rr)==(d,r)
            x,f=xs[rr],fs[(rr+rd)%4]
            assert (x,f) not in pairs;pairs.add((x,f));words[(d,r)]=word
            p=mul(x,f)[3]
            assert mul(K(x),W(f))[3]==p
            assert K(x)==xs[(r+1)%4] and W(f)==fs[(r+d+1)%4]
            invariants.setdefault(d,p);assert invariants[d]==p
            print('C PAIR',d,r,'WORD',word,'X',text_ring(x),'F',text_ring(f),'ELL',p)
    assert len(fields)==len(pairs)==16
    for n in range(1,5):
        h0=Counter(w[:n] for w in words.values())
        print('C PREFIX',n,'DISTINCT',len(h0),'FIBRES',sorted(Counter(h0.values()).items()))
    print('C ELL',sorted(invariants.items()))
    print('C PASS 16/16 encoded independent target pairs; one local temporal port; no raw K/W actuation')

if __name__=='__main__':
    A_gate()
    B_gate()
    C_gate()
