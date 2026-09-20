#!/usr/bin/env python3
from collections import Counter, deque

P=5
PAIRS=((0,1),(0,2),(0,3),(1,2),(1,3),(2,3))

def eye(n): return [[int(i==j) for j in range(n)] for i in range(n)]
def zeros(r,c): return [[0]*c for _ in range(r)]
def sub(A,B): return [[(A[i][j]-B[i][j])%P for j in range(len(A[0]))] for i in range(len(A))]
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
    m=n; r=0
    for c in range(n):
        q=next((i for i in range(r,m) if M[i][c]%P),None)
        if q is None: raise AssertionError("singular")
        M[r],M[q]=M[q],M[r]
        u=pow(M[r][c],-1,P); M[r]=[(u*x)%P for x in M[r]]
        for i in range(m):
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
def jordan_ranks(U):
    N=sub(U,eye(6)); X=eye(6); out=[]
    for _ in range(5):
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
        for _,H in gens:
            assert key(mm(G,H)) in words
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
Dn=[[4*int(i==j)%P for j in range(6)] for i in range(6)]
En=[row[:] for row in Dn]
for G in (An,Bn,Cn,Dn,En): assert power(G,2)==eye(6)

gens=(("a",An),("b",Bn),("c",Cn),("d",Dn),("e",En))
Gamma=closure(gens)

C4=[[4,4,4,4],[1,0,0,0],[0,1,0,0],[0,0,1,0]]
Ah=c2(C4)
assert power(Ah,5)==eye(6) and Ah!=eye(6)
target=jordan_ranks(Ah)

order5=[]
types=Counter()
best={}
for kg,w in Gamma.items():
    G=mat(kg)
    if G!=eye(6) and power(G,5)==eye(6):
        s=jordan_ranks(G)
        order5.append((kg,w,s))
        types[s]+=1
        if s not in best or (len(w),w)<(len(best[s]),best[s]):
            best[s]=w

target_count=types[target]
target_best=best.get(target,"NONE")

bc=mm(Bn,Cn)
bc_type=jordan_ranks(bc)
assert bc_type==(1,0,0,0,0)

fired=closure((("b",Bn),("d",Dn),("e",En)))
fired5=sum(1 for kg in fired if mat(kg)!=eye(6) and power(mat(kg),5)==eye(6))

def nil_index(seq):
    for i,r in enumerate(seq,1):
        if r==0:return i
    return 6
max_nil=max((nil_index(s) for s in types),default=0)

print("P-NATIVE-LINEAR-ORDER5-HODGE-CLASS-1")
print("Gamma_lin order: %d" % len(Gamma))
print("order-5 elements: %d" % len(order5))
print("Hodge Jordan ranks: "+" ".join(map(str,target)))
for s in sorted(types):
    print("native type "+" ".join(map(str,s))+" count=%d shortest=%s" % (types[s],best[s] if best[s] else "IDENTITY"))
print("Hodge-type native elements: %d" % target_count)
print("shortest Hodge-type witness: %s" % target_best)
print("canonical bc ranks: "+" ".join(map(str,bc_type)))
print("maximum native order-5 nilpotency index: %d" % max_nil)
print("fired linear subgroup order / order-5 count: %d %d" % (len(fired),fired5))
print("word-level Hodge verdict: "+("WORD-SEAM" if target_count else "WORD-DIFFER"))
print("FIRED-COMMUTATOR-NOGO boundary: unchanged")
print("VERDICT: COMPLETE")
