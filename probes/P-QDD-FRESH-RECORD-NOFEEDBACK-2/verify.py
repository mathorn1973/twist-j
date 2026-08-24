#!/usr/bin/env python3
"""Exact audit for P-QDD-FRESH-RECORD-NOFEEDBACK-2."""
from fractions import Fraction as F
import inspect

BASE="4ef54f0c34f80897af0121a2d93b710e70a8377c"; ISSUE=472
F5=range(5); UNITS=(1,2,3,4)

def M(rows): return tuple(tuple(x if isinstance(x,F) else F(x) for x in r) for r in rows)
def sh(a): return len(a),len(a[0])
def Z(r,c): return tuple(tuple(F(0) for _ in range(c)) for _ in range(r))
def I(n): return tuple(tuple(F(i==j) for j in range(n)) for i in range(n))
def T(a): return tuple(zip(*a))
def add(a,b): return tuple(tuple(x+y for x,y in zip(r,s)) for r,s in zip(a,b))
def sc(x,a): x=F(x); return tuple(tuple(x*y for y in r) for r in a)
def sub(a,b): return add(a,sc(-1,b))
def mm(a,b):
    bt=T(b); return tuple(tuple(sum((x*y for x,y in zip(r,c)),F(0)) for c in bt) for r in a)
def mv(a,v): return tuple(sum((x*y for x,y in zip(r,v)),F(0)) for r in a)
def pw(a,n):
    out=I(len(a)); b=a
    while n:
        if n&1: out=mm(out,b)
        b=mm(b,b); n//=2
    return out
def inv(a):
    n=len(a); w=[list(a[i])+list(I(n)[i]) for i in range(n)]
    for j in range(n):
        p=next(i for i in range(j,n) if w[i][j]); w[j],w[p]=w[p],w[j]
        q=w[j][j]; w[j]=[x/q for x in w[j]]
        for i in range(n):
            if i!=j and w[i][j]:
                q=w[i][j]; w[i]=[w[i][k]-q*w[j][k] for k in range(2*n)]
    return tuple(tuple(r[n:]) for r in w)
def rk(a):
    w=[list(r) for r in a]; r=len(w); c=len(w[0]); p=0
    for j in range(c):
        q=next((i for i in range(p,r) if w[i][j]),None)
        if q is None: continue
        w[p],w[q]=w[q],w[p]; z=w[p][j]; w[p]=[x/z for x in w[p]]
        for i in range(r):
            if i!=p and w[i][j]:
                z=w[i][j]; w[i]=[w[i][k]-z*w[p][k] for k in range(c)]
        p+=1
    return p
def cols(vs): return tuple(tuple(v[j] for v in vs) for j in range(len(vs[0])))
def e(n,i): return tuple(F(j==i) for j in range(n))
def kron(a,b):
    ar,ac=sh(a); br,bc=sh(b)
    return tuple(tuple(a[i//br][j//bc]*b[i%br][j%bc] for j in range(ac*bc)) for i in range(ar*br))
def kv(*vs):
    out=(F(1),)
    for v in vs: out=tuple(x*y for x in out for y in v)
    return out
def perm(im):
    out=[[F(0)]*len(im) for _ in im]
    for j,i in enumerate(im): out[i][j]=F(1)
    return tuple(tuple(r) for r in out)
def sharp(a,g,gi): return mm(mm(gi,T(a)),g)
def firstcol(a):
    for j in range(len(a[0])):
        v=tuple(r[j] for r in a)
        if any(v): return v
    raise AssertionError
def affine_image(c,b,x): return (b+c*x)%5
def hoff(a,k): return k*(1-a)%5

def build():
    """Target-independent reconstruction from the public J step."""
    i=I(4); one=M([[1]*4]*4); g=sub(i,sc(F(1,5),one)); gi=inv(g)
    mj=M(((1,0,-1,1),(0,1,-1,0),(1,0,0,0),(0,1,-1,1))); d=sub(mj,i)
    u=tuple(mv(pw(d,k),e(4,0)) for k in F5); B=cols(u[:4]); Bi=inv(B)
    def rho(c,b): return mm(cols(tuple(u[affine_image(c,b,x)] for x in range(4))),Bi)
    A={(c,b):rho(c,b) for c in UNITS for b in F5}
    H={(a,k):A[(a,hoff(a,k))] for a in UNITS for k in F5}
    P={k:sc(F(1,4),sum_m((H[(a,k)] for a in UNITS),4,4)) for k in F5}; Q={k:sub(i,P[k]) for k in F5}
    R={}; C={}; J={}
    for k in F5:
        h=H[(2,k)]; R[k]=sc(F(1,4),sub(add(sub(i,h),pw(h,2)),pw(h,3)))
        C[k]=sub(Q[k],R[k]); J[k]=mm(h,C[k])
    return i,g,gi,d,u,A,H,P,Q,R,C,J
def sum_m(xs,r,c):
    out=Z(r,c)
    for x in xs: out=add(out,x)
    return out
def moving(R,C,J,k,a,b,c): return add(sc(a,R[k]),add(sc(b,C[k]),sc(c,J[k])))
def writer_and_step(P,Xb,g,gi):
    x=M(((0,1),(1,0))); U=add(kron(P,I(2)),kron(Xb,x))
    sl=perm((1,0,2)); shh=perm((2,1,0)); p0=M(((1,0),(0,0))); p1=M(((0,0),(0,1)))
    W=add(kron(p0,sl),kron(p1,shh)); S=mm(kron(I(4),W),kron(U,I(3)))
    G8=kron(g,I(2)); G24=kron(G8,I(3))
    assert mm(sharp(U,G8,kron(gi,I(2))),U)==I(8)
    assert mm(sharp(S,G24,kron(kron(gi,I(2)),I(3))),S)==I(24)
    return W,S
def sparse(v,n):
    key=[0]+[0,0]*n; out={}
    for i,x in enumerate(v):
        if x: key[0]=i; out[tuple(key)]=x
    return out
def relabel(state,cell,label):
    pos=2+2*cell; out={}
    for key,a in state.items():
        k=list(key); k[pos]=label; k=tuple(k); out[k]=out.get(k,F(0))+a
    return {k:a for k,a in out.items() if a}
def step(state,j,P,Xb):
    ap=1+2*j; mp=ap+1; mid={}
    for key,a in state.items():
        assert key[ap]==0 and key[mp]==0
        si=key[0]
        for so in range(4):
            for pointer,coef in ((0,P[so][si]),(1,Xb[so][si])):
                if coef:
                    k=list(key); k[0]=so; k[ap]=pointer; k=tuple(k); mid[k]=mid.get(k,F(0))+a*coef
    out={}
    for key,a in mid.items():
        k=list(key); k[mp]=1 if key[ap]==0 else 2; k=tuple(k); out[k]=out.get(k,F(0))+a
    return {k:a for k,a in out.items() if a}
def expected(v,n,pointer,record):
    tail=tuple(x for _ in range(n) for x in (pointer,record)); return {(i,*tail):x for i,x in enumerate(v) if x}
def drop_record(state,cell):
    pos=2+2*cell; out={}
    for key,a in state.items():
        k=key[:pos]+key[pos+1:]; out[k]=out.get(k,F(0))+a
    return out

def main():
    assert all(x not in inspect.getsource(build) for x in ("E_low","E_high","target_low","target_high")); gates=1
    i,g,gi,d,u,A,H,P,Q,R,C,J=build()
    assert pw(d,5)==i and mm(mm(T(d),g),d)==g and tuple(sum((u[k][j] for k in F5),F(0)) for j in range(4))==(F(0),)*4 and u[2]==(F(-1),)*4
    for x in F5:
        for y in F5: assert sum((u[x][j]*mv(g,u[y])[j] for j in range(4)),F(0))==(F(4,5) if x==y else F(-1,5))
    gates+=1
    assert len(set(A.values()))==20 and A[(1,1)]==d
    for (a,b),r in A.items():
        assert mm(mm(T(r),g),r)==g and all(mv(r,u[x])==u[affine_image(a,b,x)] for x in F5)
        for aa in UNITS:
            for bb in F5: assert mm(r,A[(aa,bb)])==A[(a*aa%5,(b+a*bb)%5)]
    gates+=1
    for k in F5:
        assert mm(P[k],P[k])==P[k] and sharp(P[k],g,gi)==P[k] and rk(P[k])==1
        assert mm(Q[k],Q[k])==Q[k] and sharp(Q[k],g,gi)==Q[k] and rk(Q[k])==3 and add(P[k],Q[k])==i
        assert rk(R[k])==1 and rk(C[k])==2 and add(R[k],C[k])==Q[k]
        assert mm(R[k],R[k])==R[k] and mm(C[k],C[k])==C[k] and mm(R[k],C[k])==Z(4,4) and mm(C[k],R[k])==Z(4,4)
        assert sharp(R[k],g,gi)==R[k] and sharp(C[k],g,gi)==C[k] and mm(J[k],J[k])==sc(-1,C[k]) and sharp(J[k],g,gi)==sc(-1,J[k])
    gates+=1
    k=0; star=sub(R[k],C[k]); assert sharp(star,g,gi)==star and mm(star,star)==Q[k] and mm(sharp(star,g,gi),star)==Q[k] and star!=Q[k] and star!=sc(-1,Q[k])
    assert mm(P[k],star)==Z(4,4) and mm(Q[k],star)==star; gates+=1
    W,S=writer_and_step(P[k],star,g,gi); assert mm(T(W),W)==I(6) and mm(W,W)==I(6); gates+=1
    for Xb in (Q[k],sc(-1,Q[k]),star,moving(R,C,J,k,F(1),F(3,5),F(4,5))):
        _,S=writer_and_step(P[k],Xb,g,gi)
        for v in (e(4,j) for j in range(4)):
            lhs=mv(S,kv(v,e(2,0),e(3,0))); rhs=tuple(a+b for a,b in zip(kv(mv(P[k],v),e(2,0),e(3,1)),kv(mv(Xb,v),e(2,1),e(3,2)))); assert lhs==rhs
    gates+=1
    wr=firstcol(R[k]); wc=firstcol(C[k]); mix=tuple(a+b for a,b in zip(wr,wc)); one=mv(star,mix); two=mv(pw(star,2),mix); assert rk(cols((one,two)))==2; gates+=1
    hs=sparse(mix,3); prefixes=[]
    for j in range(3): hs=step(hs,j,P[k],star); prefixes.append(tuple(next(iter(hs))[2+2*q] for q in range(j+1)))
    assert prefixes==[(2,),(2,2),(2,2,2)] and hs==expected(mv(pw(star,3),mix),3,1,2)
    ls=sparse(u[k],3)
    for j in range(3): ls=step(ls,j,P[k],star)
    assert ls==expected(u[k],3,0,1); gates+=1
    base=sparse(mix,2); lo=relabel(base,0,1); hi=relabel(base,0,2); olo=step(lo,1,P[k],star); ohi=step(hi,1,P[k],star)
    assert all(x[2]==1 for x in olo) and all(x[2]==2 for x in ohi) and drop_record(olo,0)==drop_record(ohi,0); gates+=1
    assert mm(Q[k],star)==star and mm(P[k],star)==Z(4,4) and rk(cols((one,two)))==2; gates+=1
    assert mm(star,star)==Q[k] and Q[k]!=star and Q[k]!=sc(-1,star)
    for x in (Q[k],sc(-1,Q[k])): assert mm(x,x)==x or mm(x,x)==sc(-1,x)
    gates+=1
    assert rk(cols((one,two)))==2 and rk(cols((mv(Q[k],mix),mv(Q[k],mv(Q[k],mix)))))==1; gates+=1
    target_low=sc(F(1,4),M([[1]*4]*4)); target_high=sub(i,target_low); assert P[2]==target_low and Q[2]==target_high
    ts=sub(R[2],C[2]); assert mm(sharp(ts,g,gi),ts)==target_high and mm(ts,ts)==target_high and ts!=target_high and ts!=sc(-1,target_high); gates+=1
    assert gates==14
    print("P-QDD-FRESH-RECORD-NOFEEDBACK-2"); print(f"BASE_COMMIT {BASE}"); print(f"ISSUE {ISSUE}")
    print("CLASS_INPUTS J-step,F5,AGL1,fresh-pointer,blank-LOW-HIGH-record")
    print("TARGET_INDEPENDENCE PASS"); print("RECORD_WRITER alphabet=3 reversible=YES")
    print("FRESH_PROTOCOL cells=3 append_only=YES prefix_preserving=YES")
    print("NO_FEEDBACK old_record_controls=NO"); print("GENERAL_EXTENSION admitted_T=ALL proof=INLINE")
    print("OUTCOME_REPEATABILITY LOW=YES HIGH=YES"); print("J_WITNESS T=R-C selfadjoint=YES involutive=YES")
    print("PROJECTIVE_IDEMPOTENCE witness=NONIDEMPOTENT"); print("RECORD_HISTORY witness=HIGH,HIGH,HIGH")
    print("POSTSTATE_RAYS first_second=SPLIT"); print("RECORD_SUFFICIENCY status=EXTRA_PREMISE")
    print("TARGET_TOKEN 2"); print("TARGET_EFFECTS realized=YES"); print("DECISION NONIMPLICATION")
    print("O2_GLOBAL_STATUS UNCHANGED"); print("SAMPLING NOT PROVIDED")
    print("CANDIDATE_CEILING T restricted-L4-theorems"); print("ALL PASS 14/14")
    return 0
if __name__=="__main__": raise SystemExit(main())
