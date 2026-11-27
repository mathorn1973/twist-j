"""NON-CANONICAL D diagnostic frozen in issue #2111 comment 7219919260."""
import verify as V
from itertools import product
from collections import Counter
from fractions import Fraction
H=V.H
Z,O,J,P=V.Z,V.O,V.J,V.P
add,sub,mul,h,scale,neg=V.add,V.sub,V.mul,V.h,V.scale,V.neg
idx,seed,shift,history,step,account=V.idx,V.seed,V.shift,V.history,V.step,V.account
s=40
b=1
a=-2
def fields(r,u,k=1,l=2,m=3,n=4):
    return seed(1,{(0,a*r%8):P[k],(0,(4+a*r)%8):P[l],
                   (1,a*u%8):P[m],(1,(4+a*u)%8):P[n]})
inputs=tuple(product(range(4),repeat=2))
hs={p:history(fields(*p),s+1) for p in inputs}
control=history(fields(0,0,0,0,0,0),s+1)
def radiation(F):
    return tuple(z for i,z in enumerate(F) if i%4>=2)
def radword(hist):
    cuts,mids,tags,ac=hist
    return tuple(radiation(F) for t in range(s+1)
                 for F in ((cuts[t],) if t==0 else (mids[t],cuts[t])))
def tagword(hist):
    return tuple(tuple(sorted(tags.items())) for tags in hist[2][1:s+1])
def maskword(hist):
    masks=[]
    for t in range(1,s+1):
        F=hist[0][t-1]; bit=(t-1)%2
        masks.append(tuple(H.even(sub(F[idx(x,y,0)],F[idx(x,(y+1)%8,0)]))
            for x,y in product(range(8),range(bit,8,2))))
    return tuple(masks)
def partition(label,words,cw):
    cnt=Counter(words)
    print('D1 TRANSCRIPT',label,'CLASSES',len(cnt),'SIZES',sorted(cnt.values()),
          'CONTROL_EQUALS',sum(w==cw for w in words))
for label,fun in (('radiation',radword),('Btags',tagword),('matter_C_masks',maskword)):
    partition(label,[fun(hs[p]) for p in inputs],fun(control))
for p,hist in hs.items():
    assert hist[0][s]==shift(fields(*p),a)
    assert hist[0][s]==fields((p[0]+1)%4,(p[1]+1)%4)
    assert H.scalar_account(hist[3][2])==1024
xs=[P[1]];fs=[P[2]]
for n in range(4):xs.append(V.K(xs[-1]));fs.append(V.W(fs[-1]))
assert xs[4]==xs[0] and fs[4]==fs[0]
targets=(tuple(xs[:4]),tuple(fs[:4]))

def aff(vals,target):
    A=mul(sub(target[1],target[0]),H.inverse(sub(vals[1],vals[0])))
    B=sub(target[0],mul(A,vals[0]))
    assert A!=Z
    return (A,B) if tuple(add(mul(A,x),B) for x in vals)==target else None
def decode_matrix(vals,target):
    M=tuple(zip(*vals)); d=V.det(M)
    if abs(d)!=1:return None
    inv=tuple(tuple(((-1)**(i+j)*V.det(tuple(tuple(M[r][c] for c in range(4) if c!=i)
                    for r in range(4) if r!=j)))//d for j in range(4)) for i in range(4))
    D=tuple(tuple(sum(target[k][i]*inv[k][j] for k in range(4)) for j in range(4)) for i in range(4))
    assert tuple(V.applyD(D,x) for x in vals)==target
    return D
def local(p,x,y,t,n=1):
    hist=hs[p]
    z=[]
    for dt in range(n):
        F=hist[0][t+dt]
        i=idx(x,y,0)
        assert F[i+1]==neg(F[i])
        z.append(F[i])
    return z[0] if n==1 else tuple(z)
def ownvals(track,t,y,n):
    arr=[]
    for k in range(4):
        vals={local((k,l) if track==0 else (l,k),track,y,t,n) for l in range(4)}
        if len(vals)!=1:return None
        arr.append(next(iter(vals)))
    return tuple(arr)
for track in range(2):
    names=('independent','distinct','affine','integral_affine','unimodular','two_cut_independent','two_cut_distinct')
    first={};cnt=Counter()
    for t,y in product(range(s),range(8)):
        vals=ownvals(track,t,y,1);types=[];A=None;D=None
        if vals is not None:
            types.append('independent')
            if len(set(vals))==4:
                types.append('distinct')
                A=aff(vals,targets[track]);D=decode_matrix(vals,targets[track])
                if A:
                    types.append('affine')
                    if all(V.integral(v) for v in A):types.append('integral_affine')
                if D:types.append('unimodular')
            for name in types:
                cnt[name]+=1;first.setdefault(name,(t,y,vals,A,D))
        vv=ownvals(track,t,y,2)
        if vv is not None:
            cnt['two_cut_independent']+=1
            first.setdefault('two_cut_independent',(t,y,vv,None,None))
            if len(set(vv))==4:
                cnt['two_cut_distinct']+=1
                first.setdefault('two_cut_distinct',(t,y,vv,None,None))
    print('D2 COUNTS',track,[(k,cnt[k]) for k in names])
    for name in names:
        if name not in first:continue
        t,y,vals,A,D=first[name]
        print('D2 PORT',track,name,t,y,'VALUES',vals)
        if name in ('affine','integral_affine'):
            print('D2 AFFINE',track,name,tuple(tuple(str(z) for z in v) for v in A))
        if name=='unimodular':print('D2 MATRIX',track,D)
def weights(track,z,w):
    if track==0:return (z[1],w[2],z[2],w[1])
    def a(z):return z[3]-z[1]
    def b(z):return -z[1]
    return a(z),b(w),b(z),a(w)
def onehot(k):return tuple(int(i==k) for i in range(4))
def read(track,F):
    z,w=F[idx(track,0,0)],F[idx(track,2,0)]
    assert F[idx(track,0,1)]==neg(z) and F[idx(track,2,1)]==neg(w)
    ww=weights(track,z,w)
    if ww not in tuple(onehot(k) for k in range(4)):return ww,None
    out=rsum(scale(u,z) for u,z in zip(ww,targets[track]))
    return ww,out
print('D3 TARGETS',targets,'DETS',tuple(V.det(tuple(zip(*tar))) for tar in targets))
pairs=set();ell=Counter();cases=0
for r,u in inputs:
    F0=fields(r,u);hist=history(F0,160);cuts,mids,tags,ac=hist
    p0=None
    for n in range(5):
        F=cuts[s*n]
        assert F==fields((r+n)%4,(u+n)%4)
        w0,x=read(0,F);w1,f=read(1,F)
        assert w0==onehot((r+n)%4) and w1==onehot((u+n)%4)
        assert x==xs[(r+n)%4] and f==fs[(u+n)%4]
        p=mul(x,f)[3]
        if n==0:
            pairs.add((x,f));ell[p]+=1;p0=p
        else:assert p==p0 and V.K(xold)==x and V.W(fold)==f
        # The second port equals the same first port in the next stroke.
        if n<4:
            for track in range(2):
                assert F[idx(track,2,0)]==cuts[s*(n+1)][idx(track,0,0)]
        xold,fold=x,f;cases+=1
    print('D3 CASE',r,u,'ELL',p0,'Q',H.scalar_account(ac[2]))
assert len(pairs)==16
for k,l,m,n in ((0,0,3,4),(1,1,3,4),(2,2,3,4),(1,2,0,0),(1,2,3,3),(1,2,4,4)):
    # Literal strobe input controls, no claim of subsequent transport.
    vals=[read(0,fields(r,u,k,l,m,n))[1] is not None and
          read(1,fields(r,u,k,l,m,n))[1] is not None for r,u in inputs]
    print('D3 CONTROL',k,l,m,n,'ACCEPTED',sum(vals))
print('D3 PAIRS',len(pairs),'STROBE_CUTS',cases,'ELL_HISTOGRAM',sorted(ell.items()))
print('PASS D exact local material read and paired address continuation')
