#!/usr/bin/env python3
from collections import Counter, deque

P=5
PAIRS=((0,1),(0,2),(0,3),(1,2),(1,3),(2,3))

def eye(n): return [[int(i==j) for j in range(n)] for i in range(n)]
def zeros(r,c): return [[0]*c for _ in range(r)]
def add(A,B): return [[(A[i][j]+B[i][j])%P for j in range(len(A[0]))] for i in range(len(A))]
def sub(A,B): return [[(A[i][j]-B[i][j])%P for j in range(len(A[0]))] for i in range(len(A))]
def scale(A,c): return [[(c*x)%P for x in row] for row in A]
def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))%P
             for j in range(len(B[0]))] for i in range(len(A))]
def power(A,n):
    R=eye(len(A))
    while n:
        if n&1:R=mm(R,A)
        A=mm(A,A); n//=2
    return R
def rank(A):
    A=[[x%P for x in row] for row in A]
    m=len(A); n=len(A[0]) if m else 0; r=0
    for c in range(n):
        q=next((i for i in range(r,m) if A[i][c]%P),None)
        if q is None: continue
        A[r],A[q]=A[q],A[r]
        u=pow(A[r][c],-1,P); A[r]=[(u*x)%P for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]%P:
                u=A[i][c]%P
                A[i]=[(A[i][j]-u*A[r][j])%P for j in range(n)]
        r+=1
        if r==m: break
    return r
def inverse(A):
    n=len(A); M=[[(A[i][j]%P) for j in range(n)]+eye(n)[i] for i in range(n)]
    r=0
    for c in range(n):
        q=next((i for i in range(r,n) if M[i][c]%P),None)
        if q is None: raise AssertionError("singular")
        M[r],M[q]=M[q],M[r]
        u=pow(M[r][c],-1,P); M[r]=[(u*x)%P for x in M[r]]
        for i in range(n):
            if i!=r and M[i][c]%P:
                u=M[i][c]%P
                M[i]=[(M[i][j]-u*M[r][j])%P for j in range(2*n)]
        r+=1
    return [row[n:] for row in M]
def c2(A):
    out=zeros(6,6)
    for col,(i,j) in enumerate(PAIRS):
        for row,(k,l) in enumerate(PAIRS):
            out[row][col]=(A[k][i]*A[l][j]-A[k][j]*A[l][i])%P
    return out
def key(A): return tuple(x%P for row in A for x in row)
def mat(k,n=6): return [list(k[i*n:(i+1)*n]) for i in range(n)]
def order(A,limit=500):
    R=eye(len(A))
    for n in range(1,limit+1):
        R=mm(R,A)
        if R==eye(len(A)): return n
    return None
def ranks_about(A,scalar):
    N=sub(A,scale(eye(6),scalar)); X=eye(6); out=[]
    for _ in range(6):
        X=mm(X,N); out.append(rank(X))
    return tuple(out)
def closure(gens):
    I=eye(6); ki=key(I)
    words={ki:""}; q=deque([ki])
    while q:
        kg=q.popleft(); G=mat(kg)
        for name,H in gens:
            kh=key(mm(G,H))
            if kh not in words:
                words[kh]=words[kg]+name
                q.append(kh)
    for kg in tuple(words):
        G=mat(kg)
        assert key(inverse(G)) in words
        for _,H in gens: assert key(mm(G,H)) in words
    return words

An=[
[0,1,0,0,0,0],
[1,0,0,0,0,0],
[0,0,0,1,0,0],
[0,0,1,0,0,0],
[0,0,0,0,1,0],
[0,0,0,0,0,1],
]
Bn=[
[0,0,4,0,0,0],
[0,0,0,4,0,0],
[4,0,0,0,0,0],
[0,4,0,0,0,0],
[0,0,0,0,4,0],
[0,0,0,0,0,4],
]
Cn=[
[0,0,4,0,0,0],
[0,0,0,4,0,1],
[4,0,0,0,0,0],
[0,4,0,0,0,4],
[0,0,0,0,4,0],
[0,0,0,0,0,4],
]
Dn=scale(eye(6),4)
En=[row[:] for row in Dn]
for G in (An,Bn,Cn,Dn,En): assert power(G,2)==eye(6)

gens=(("a",An),("b",Bn),("c",Cn),("d",Dn),("e",En))
Gamma=closure(gens)

C4=[[4,4,4,4],[1,0,0,0],[0,1,0,0],[0,0,1,0]]
M4=add(eye(4),power(C4,2))
Lh=c2(M4)
Ah=c2(C4)
assert rank(Lh)==6
target_order=order(Lh)
target=ranks_about(Lh,4)
assert target[-1]==0
cycle_control=ranks_about(Ah,1)

types=Counter(); best={}; candidates=[]
for kg,w in Gamma.items():
    G=mat(kg)
    seq=ranks_about(G,4)
    if seq[-1]==0:
        types[seq]+=1
        if seq not in best or (len(w),w)<(len(best[seq]),best[seq]):
            best[seq]=w
        if seq==target:
            candidates.append((kg,w))

candidates.sort(key=lambda item:(len(item[1]),item[1]))
shortest=candidates[0][1] if candidates else "NONE"

minus_bc=mm(Dn,mm(Bn,Cn))
minus_cb=mm(Dn,mm(Cn,Bn))
mbc=(order(minus_bc),ranks_about(minus_bc,4))
mcb=(order(minus_cb),ranks_about(minus_cb,4))

fired=closure((("b",Bn),("d",Dn),("e",En)))
fired_candidates=0
for kg in fired:
    G=mat(kg)
    if ranks_about(G,4)==target:
        fired_candidates+=1

print("P-NATIVE-LINEAR-JHODGE-STEP-CLASS-1")
print("Gamma_lin order: %d" % len(Gamma))
print("actual Hodge step order: %d" % target_order)
print("actual Hodge step (-1)-ranks: "+" ".join(map(str,target)))
print("marked cycle (+1)-ranks: "+" ".join(map(str,cycle_control)))
print("step/cycle rank-sequence match: "+("YES" if target==cycle_control else "NO"))
for s in sorted(types):
    print("native (-1)-type "+" ".join(map(str,s))+" count=%d shortest=%s" %
          (types[s],best[s] if best[s] else "IDENTITY"))
print("actual-step native candidates: %d" % len(candidates))
print("shortest actual-step witness: %s" % shortest)
print("-bc order / ranks: %d %s" % (mbc[0]," ".join(map(str,mbc[1]))))
print("-cb order / ranks: %d %s" % (mcb[0]," ".join(map(str,mcb[1]))))
print("fired subgroup order / actual-step candidates: %d %d" % (len(fired),fired_candidates))
print("actual-step verdict: "+("STEP-SEAM" if candidates else "STEP-DIFFER"))
print("VERDICT: COMPLETE")
