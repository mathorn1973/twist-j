"""NON-CANONICAL exact active source interrogation, frozen issue #2115."""
from pathlib import Path
import importlib.util,sys,hashlib
from itertools import product
from fractions import Fraction as Q
from functools import cache
from collections import Counter

source=Path(sys.argv[1] if len(sys.argv)>1 else 'reproduce/h3-referenced-record/verify.py')
raw=source.read_bytes()
assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()=='fd215e24fefbbebf83cf3985d8ebcedd590aa709'
spec=importlib.util.spec_from_file_location('h3_pinned',source)
H=importlib.util.module_from_spec(spec);sys.modules[spec.name]=H
spec.loader.exec_module(H)
H.transport_pair=cache(H.transport_pair);H.collision=cache(H.collision)
Z,O,R,J,JI=H.ZERO,H.ONE,H.RHO,H.J,H.J_INV
P=H.J_POWERS
add,sub,mul,h,sc=H.add,H.sub,cache(H.mul),H.h,H.scale
neg=lambda x:sc(-1,x)
idx=lambda x,y,q:H.index(8,x,y,q)
def powr(a,n):
    t=O
    for _ in range(n):t=mul(t,a)
    return t
def rsum(seq):return tuple(map(sum,zip(*seq)))
def account(F):
    return rsum(z for i,z in enumerate(F) if i%4<2),rsum(z for i,z in enumerate(F) if i%4>=2),rsum(h(z) for z in F)
def step(F,bit,ac):
    G=H.transport(F,8,bit)
    N,ev=H.collide(G,8)
    back,_=H.collide(N,8)
    assert back==G and H.transport(back,8,bit,backward=True)==F
    assert account(G)==account(N)==ac
    return G,N,{(x,y):t for x,y,t in ev}
def hist(F,n):
    ac=account(F);cuts=[F];mids=[None];tags=[None]
    for t in range(n):
        G,F,E=step(F,t%2,ac)
        mids.append(G);cuts.append(F);tags.append(E)
    return cuts,mids,tags,ac
def marks(r,u=None):
    M={(0,-2*r%8):P[1],(0,(4-2*r)%8):P[2]}
    if u is not None:M.update({(1,-2*u%8):P[3],(1,(4-2*u)%8):P[4]})
    return M
def ref(r,u=None):
    M=marks(r,u)
    F=[]
    for x,y in product(range(8),repeat=2):
        d=M.get((x,y),sc((-1)**y,O))
        F.extend((d,neg(d),Z,sc(2*(-1)**(x+y),J)))
    return tuple(F)
def rad(F):return tuple(z for i,z in enumerate(F) if i%4>=2)
def src(F,mat=False):return tuple(F[idx(0,y,k)] for y in range(8) for k in (range(2) if mat else range(4)))
def reader(F):return F[32:]
def cell(F,x,y):
    i=idx(x,y,0);return F[i:i+4]
def radword(hh,n):
    cut,mid,tags,ac=hh
    return tuple(rad(F) for t in range(n+1) for F in ((cut[t],) if t==0 else (mid[t],cut[t])))
def tagword(hh,n):return tuple(tuple(sorted(tags.items())) for tags in hh[2][1:n+1])

# A: exact reference replay and radiation/tag classes.
R0={r:hist(ref(r),160) for r in range(4)}
for name,inputs in (('single',[(r,None) for r in range(4)]),('paired',list(product(range(4),repeat=2)))):
    hs=[R0[r] if u is None else hist(ref(r,u),160) for r,u in inputs]
    assert all(Hh[0][160]==Hh[0][0] and H.scalar_account(Hh[3][2])==1024 for Hh in hs)
    rr=len({radword(hh,160) for hh in hs});tt=len({tagword(hh,160) for hh in hs})
    assert rr==tt==1
    print('A REFERENCE',name,'INPUTS',len(hs),'RAD_CLASSES',rr,'B_CLASSES',tt,'RETURN',len(hs),'Q',1024)

# B: rowwise synthesis on O localized away from 2.
A=sc(Q(1,2),add(O,R));B=sc(Q(1,2),sub(O,R))
Binv=H.inverse(B)
assert mul(B,Binv)==O
eta=powr(sub(O,R),4)
def ints(z):
    assert all(Q(v).denominator==1 for v in z),z
    return tuple(int(v) for v in z)
eta=ints(eta)
assert not H.even(eta)
def oddden(z):return all(Q(t).denominator%2 for t in z)
def evenloc(z):
    assert oddden(z),z
    return all(Q(t).numerator%2==0 for t in z)
def rational_C(a,b,back=False):
    dif=sub(a,b)
    if not evenloc(dif):return a,b
    u=mul(H.RHO_INV if back else R,dif)
    ans=(sc(Q(1,2),add(add(a,b),u)),sc(Q(1,2),sub(add(a,b),u)))
    assert all(oddden(v) for v in ans)
    return ans
def partner(c,w):
    out=add(c,mul(Binv,sub(w,c)))
    assert evenloc(sub(out,c))
    assert rational_C(c,out)[0]==w
    return out
def vert(g,bit):
    out=list(g)
    for y in range(bit,8,2):
        z=(y+1)%8
        out[y],out[z]=H.transport_pair(g[y],g[z],False)
    return tuple(out)
def post(g,f,e):
    c=sub(g,sc(2,f))
    w=JI if e==1 else J if e==-1 else O
    delta=mul(sub(w,O),f)
    return add(g,delta),sub(c,delta)
g1=tuple(sc((-1)**y,mul(R,R)) for y in range(8))
c1=tuple(sc((-1)**y,mul(add(J,O),R)) for y in range(8))
f2=tuple(powr(J,2) if y==0 else sc(-(-1)**y,O) for y in range(8))
f3=tuple(powr(J,3) if y==0 else Z for y in range(8))
f4=tuple(powr(J,2) if y==0 else Z for y in range(8))
f1=tuple(sc(-(-1)**y,mul(J,R)) for y in range(8))
g2m=vert(g1,1)
p2=tuple(post(g2m[y],f2[y],1 if y==0 else -1) for y in range(8))
g2,c2=tuple(zip(*p2))
g3m=vert(g2,0)
p3=tuple(post(g3m[y],f3[y],1 if y==0 else 0) for y in range(8))
g3,c3=tuple(zip(*p3))
g4m=vert(g3,1)
cm={t:tuple(sub(g,sc(2,f)) for g,f in zip(gs,fs)) for t,gs,fs in ((2,g2m,f2),(3,g3m,f3),(4,g4m,f4))}
cp=tuple(sub(cm[4][y],mul(R,f4[y])) for y in range(8))
target=tuple(add(c,sc(2,O)) for c in cp)
# Separate reader initial stock, computed without phase index.
stock={}
for y in range(8):
    s=(-1)**y
    c11=sc(-2*s,mul(J,R))
    c71=partner(c1[y],cm[2][y]);c61=c71
    c72=sub(add(c1[y],c71),cm[2][y])
    c12=partner(c2[y],cm[3][y])
    c21=partner(c11,c12);c31=c21
    c22=sub(add(c11,c21),c12);c13=sub(add(c2[y],c12),cm[3][y])
    c73=partner(c3[y],cm[4][y]);c62=partner(c72,c73);c51=partner(c61,c62)
    c23=partner(c13,target[y]);c32=partner(c22,c23);c41=partner(c31,c32)
    c40,c50=rational_C(c41,c51,True)
    assert rational_C(c40,c50)==(c41,c51)
    row=(sc(-2*s,J),c21,c31,c40,c50,c61,c71)
    for x,z in enumerate(row,1):
        assert oddden(z)
        stock[x,y]=ints(mul(eta,z))
def scale_eta(z):return ints(mul(eta,z))
def prepare(l,r):
    F=[]
    for x,y in product(range(8),repeat=2):
        if x==0:F.extend(scale_eta(z) for z in cell(ref(r),0,y))
        else:F.extend((Z,Z,Z,stock[x,(y+2*l)%8]))
    return tuple(F)
for y in range(8):
    print('B STOCK',y,*[stock[x,y] for x in range(1,8)])
print('B ETA',eta,'Q_ETA',H.scalar_account(h(eta)))
pos=scale_eta(add(target[0],sub(R,O)));negative=scale_eta(target[0])
assert pos!=negative
qvals=set()
H0={}
for l,r in product(range(4),repeat=2):
    F0=prepare(l,r)
    assert src(F0)==tuple(scale_eta(z) for z in src(ref(r)))
    assert reader(F0)==reader(prepare(l,0))
    n=160 if l==0 else 12
    hh=hist(F0,n);cuts,mids,tags,ac=hh
    if l==0:H0[r]=hh
    qvals.add(H.scalar_account(ac[2]))
    localr=(r-l)%4
    positive=localr==2
    for t in range(1,5):
        for y in range(8):
            yy=(y+2*l)%8
            f=(f1,f2,f3,f4)[t-1][yy]
            c=cell(mids[t],0,y)
            assert H.even(sub(c[2],c[3]))
            assert H.half(sub(c[2],c[3]))==scale_eta(f)
            tag=1 if t==1 else (1 if yy==0 else 2) if t==2 else (1 if yy==0 else 0) if t==3 else (2 if yy==0 and positive else 0)
            assert tags[t].get((0,y),0)==tag,(l,r,t,y,tags[t].get((0,y),0),tag)
        assert not any(x!=0 for x,y in tags[t])
    yy=(-2*l)%8;prev=(yy-1)%8
    dv=sub(cell(cuts[3],0,prev)[0],cell(cuts[3],0,yy)[0])
    assert H.even(dv)==(not positive)
    if positive:assert cell(mids[4],0,yy)[0]==cell(cuts[3],0,yy)[0]
    else:assert cell(mids[4],0,yy)[0]!=cell(cuts[3],0,yy)[0]
    port=idx(1,yy,3)
    assert cuts[4][port]==negative
    assert cuts[5][port]==(pos if positive else negative)
    assert (cuts[5][port]!=cuts[4][port])==positive
    assert not any(x!=0 for t in range(1,n+1) for x,y in tags[t])
    print('B CASE',l,r,'T4_C_ADMIT',int(not positive),'T4_TAG',2*int(positive),'REMOTE5',cuts[5][port])
    print('B SOURCE4',l,r,'PRE_D',cell(mids[4],0,yy)[0],'POST_D',cell(cuts[4],0,yy)[0])
assert len(qvals)==1
print('B PASS',16,'POSITIVE',4,'Q',next(iter(qvals)),'R_POS',pos,'R_NEG',negative)

def reader_words(hh,n):
    cut,mid,_,_=hh
    return tuple(reader(F) for t in range(n+1) for F in ((cut[t],) if t==0 else (mid[t],cut[t])))
for t in range(1,13):
    p=len({reader_words(H0[r],t) for r in range(4)})
    print('B READER_PREFIX',t,p)
for t in range(5,13):
    ix=idx(1,0,3)
    out=[(pos if r==2 else negative) for r in range(4)]
    print('B HOLD',t,'POST_C',sum(H0[r][1][t][ix]==out[r] for r in range(4)),'FULL',sum(H0[r][0][t][ix]==out[r] for r in range(4)))

# C: material and complete-column recovery against the actual reference history.
def compare(t,r,mat,initial):
    target_t=0 if initial else t
    raw=src(R0[r][0][target_t],mat)
    return src(H0[r][0][t],mat)==tuple(scale_eta(z) for z in raw)
for name,mat,initial in (('material_ref',True,False),('full_ref',False,False),('material_initial',True,True)):
    counts=[sum(compare(t,r,mat,initial) for r in range(4)) for t in range(1,161)]
    print('C COMMON',name,[t for t,n in enumerate(counts,1) if n==4])
    print('C HIST',name,sorted(Counter(counts).items()))
    print('C CUTS',name,[(t,counts[t-1]) for t in (5,40,80,120,160)])
print('DONE exact separated-source active interrogation and recovery boundary')
