#!/usr/bin/env python3
"""Exact audit for P-O5-WALSH-LINK-HOMOLOGY-1."""

from __future__ import annotations
import ast
from fractions import Fraction
from itertools import product
from pathlib import Path

def check(label, ok, detail=""):
    if not ok:
        raise AssertionError(f"{label} failed: {detail}")

def chi5(n):
    r=n%5
    return 0 if r==0 else (1 if r in (1,4) else -1)

def prime(n):
    if n<2: return False
    d=2
    while d*d<=n:
        if n%d==0: return False
        d+=1
    return True

def split_primes(N):
    return tuple(p for p in range(2,N+1) if prime(p) and chi5(p)==1)

def support_faces(N):
    ps=split_primes(N)
    out=[]
    def extend(i,chosen,norm):
        out.append(tuple(chosen))
        for k in range(i,len(ps)):
            p=ps[k]
            nxt=norm*p
            if nxt>N: break
            chosen.append(p)
            extend(k+1,chosen,nxt)
            chosen.pop()
    extend(0,[],1)
    return tuple(out)

def subsets(S):
    return tuple(tuple(p for i,p in enumerate(S) if mask>>i&1)
                 for mask in range(1<<len(S)))

def orientations(S):
    return tuple(product((-1,1),repeat=len(S)))

def oface(S,e):
    return tuple(zip(S,e))

def walsh(S,J):
    J=set(J); out={}
    for e in orientations(S):
        w=1
        for p,s in zip(S,e):
            if p in J: w*=s
        out[oface(S,e)]=w
    return out

def addscaled(dst,src,c):
    c=Fraction(c)
    for k,v in src.items():
        dst[k]=dst.get(k,Fraction(0))+c*Fraction(v)
        if dst[k]==0: del dst[k]

def bd_face(F):
    if not F:return {}
    return {F[:i]+F[i+1:]:(-1 if i%2 else 1) for i in range(len(F))}

def bd_direct(S,J):
    out={}
    for F,c in walsh(S,J).items(): addscaled(out,bd_face(F),c)
    return out

def bd_formula(S,J,keepJ=False,omit2=False):
    out={}; Js=set(J); fac=1 if omit2 else 2
    for i,p in enumerate(S):
        if p in Js and not keepJ: continue
        L=S[:i]+S[i+1:]
        LJ=tuple(q for q in J if q!=p)
        addscaled(out,walsh(L,LJ),fac*(-1 if i%2 else fac//fac))
    return out

def link(delta,J):
    D=set(delta); Js=set(J)
    vs=tuple(sorted({p for F in delta for p in F if p not in Js}))
    out=[]
    def extend(i,chosen):
        T=tuple(chosen)
        if tuple(sorted(J+T)) in D: out.append(T)
        else: return
        for k in range(i,len(vs)):
            chosen.append(vs[k]); extend(k+1,chosen); chosen.pop()
    extend(0,[])
    return tuple(out)

def nu(J,T):
    return sum(j<t for j in J for t in T)

def psi(J,T,omit_sign=False):
    S=tuple(sorted(J+T))
    s=1 if omit_sign or nu(J,T)%2==0 else -1
    out={}
    addscaled(out,walsh(S,J),Fraction(s,2**len(T)))
    return out

def bd_support(T):
    if not T:return {}
    return {T[:i]+T[i+1:]:(-1 if i%2 else 1) for i in range(len(T))}

def kfaces(N):
    out=[()]
    for S in support_faces(N):
        if S: out.extend(oface(S,e) for e in orientations(S))
    return tuple(out)

def grouped(faces):
    g={}
    for F in faces:g.setdefault(len(F)-1,[]).append(F)
    return g

def rankQ(M):
    if not M:return 0
    A=[[Fraction(x) for x in row] for row in M]
    nr=len(A); nc=len(A[0]); r=c=0
    while r<nr and c<nc:
        piv=next((i for i in range(r,nr) if A[i][c]),None)
        if piv is None:c+=1;continue
        A[r],A[piv]=A[piv],A[r]
        q=A[r][c]; A[r]=[x/q for x in A[r]]
        for i in range(nr):
            if i!=r and A[i][c]:
                q=A[i][c]
                A[i]=[A[i][j]-q*A[r][j] for j in range(nc)]
        r+=1;c+=1
    return r

def brank(g,d):
    src=g.get(d,[]); dst=g.get(d-1,[])
    if not src or not dst:return 0
    row={F:i for i,F in enumerate(dst)}
    M=[[0]*len(src) for _ in dst]
    for j,F in enumerate(src):
        for i in range(len(F)):
            M[row[F[:i]+F[i+1:]]][j]+=(-1 if i%2 else 1)
    return rankQ(M)

def betti(faces):
    g=grouped(faces); mx=max(g)
    ranks={d:brank(g,d) for d in range(-1,mx+1)}
    out={}
    for d in range(-1,mx+1):
        v=len(g.get(d,[]))-ranks.get(d,0)-ranks.get(d+1,0)
        if v:out[d]=v
    return out

def red_euler(faces):
    return sum(-1 if (len(F)-1)%2 else 1 for F in faces)

def rank2(M):
    A=[[x&1 for x in row] for row in M]; r=c=0
    while A and r<len(A) and c<len(A[0]):
        piv=next((i for i in range(r,len(A)) if A[i][c]),None)
        if piv is None:c+=1;continue
        A[r],A[piv]=A[piv],A[r]
        for i in range(len(A)):
            if i!=r and A[i][c]:A[i]=[x^y for x,y in zip(A[i],A[r])]
        r+=1;c+=1
    return r

def G01():
    for n in range(6):
        S=tuple(range(n)); rows=[]
        for J in subsets(S):
            Js=set(J); row=[]
            for e in orientations(S):
                w=1
                for i in Js: w*=e[i]
                row.append(w)
            rows.append(row)
        target=1<<n
        for i,a in enumerate(rows):
            for j,b in enumerate(rows):
                check("Walsh orthogonality",sum(x*y for x,y in zip(a,b))==(target if i==j else 0),(n,i,j))

def G02():
    for N in (11,121,209,500):
        for S in support_faces(N):
            for J in subsets(S):
                check("boundary",bd_direct(S,J)==bd_formula(S,J),(N,S,J))

def G03():
    for N in (11,121,209,500):
        D=support_faces(N)
        for J in D:
            for T in link(D,J):
                L={}
                for F,c in psi(J,T).items():addscaled(L,bd_face(F),c)
                R={}
                for U,c in bd_support(T).items():addscaled(R,psi(J,U),c)
                check("chain map",L==R,(N,J,T))

def G04():
    for N in (1,11,121,209,500):
        D=support_faces(N); full=betti(kfaces(N)); rhs={}
        for J in D:
            for d,v in betti(link(D,J)).items():
                q=d+len(J); rhs[q]=rhs.get(q,0)+v
        rhs={d:v for d,v in rhs.items() if v}
        check("Betti",full==rhs,(N,full,rhs))

def G05():
    for N in (1,11,121,209,500,1000):
        D=support_faces(N)
        rhs=sum(((-1)**len(J))*red_euler(link(D,J)) for J in D)
        check("Euler",red_euler(kfaces(N))==rhs,N)

def G06():
    check("B1",rankQ([[1,1],[1,1]])==1)
    S=(11,)
    check("B2",bd_direct(S,S)!=bd_formula(S,S,keepJ=True))
    check("B3",bd_direct(S,())!=bd_formula(S,(),omit2=True))
    J=(11,);T=(19,);L={};R={}
    for F,c in psi(J,T,omit_sign=True).items():addscaled(L,bd_face(F),c)
    for U,c in bd_support(T).items():addscaled(R,psi(J,U,omit_sign=True),c)
    check("B4",L!=R)
    check("B5",rank2([[1,1],[1,-1]])==1)

def G07():
    raw=Path(__file__).read_bytes()
    check("LF",raw.endswith(b"\n") and b"\r" not in raw)
    tree=ast.parse(raw.decode(),filename=__file__)
    allowed={"__future__","ast","fractions","itertools","pathlib"}
    roots=[]; calls=[]
    for n in ast.walk(tree):
        if isinstance(n,ast.Import):roots.extend(x.name.split(".")[0] for x in n.names)
        if isinstance(n,ast.ImportFrom):roots.append((n.module or "").split(".")[0])
        if isinstance(n,ast.Constant):check("literal",not isinstance(n.value,(float,complex)))
        if isinstance(n,ast.Call):
            if isinstance(n.func,ast.Name):calls.append(n.func.id)
    check("imports",set(roots)<=allowed,roots)
    check("dynamic",not(set(calls)&{"compile","complex","eval","exec","float","input","open"}))

def main():
    G01();print("G01 PASS Walsh Q-bases")
    G02();print("G02 PASS exact character boundary")
    G03();print("G03 PASS shifted link chain isomorphisms")
    G04();print("G04 PASS rational Betti direct sum")
    G05();print("G05 PASS reduced Euler link sum")
    G06();print("G06 PASS breakers B1=11 B2=11 B3=11 B4=(209;11,19) B5=char2")
    G07();print("G07 PASS exact-rational stdlib firewall")
    print("VERIFY RESULT 7/7 ALL PASS")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
