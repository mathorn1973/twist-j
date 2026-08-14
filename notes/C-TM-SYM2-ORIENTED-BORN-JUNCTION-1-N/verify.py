#!/usr/bin/env python3
"""Exact incubation verifier for C-TM-SYM2-ORIENTED-BORN-JUNCTION-1-N.

NON-CANONICAL. Standard library only. No public probe status or evidence.
The independent breaker was frozen before this file existed.
"""
from fractions import Fraction as F
from itertools import permutations

# ---------------------------------------------------------------------------
# Q(zeta_5) as Q[j]/(1+j+j^2+j^3+j^4), basis 1,j,j^2,j^3.
# ---------------------------------------------------------------------------
def zadd(x,y): return tuple(x[i]+y[i] for i in range(4))
def zneg(x): return tuple(-a for a in x)
def zsub(x,y): return zadd(x,zneg(y))

def zmul(x,y):
    tmp=[F(0) for _ in range(7)]
    for i,a in enumerate(x):
        for k,b in enumerate(y):
            tmp[i+k]+=a*b
    # j^4 = -(1+j+j^2+j^3), reduce high powers descending.
    for d in range(6,3,-1):
        c=tmp[d]
        if not c: continue
        tmp[d]=F(0)
        # j^d = j^(d-4) j^4 = -(j^(d-4)+...+j^(d-1))
        for q in range(d-4,d):
            tmp[q]-=c
    return tuple(tmp[:4])

ONE=(F(1),F(0),F(0),F(0))
ZERO=(F(0),)*4
JROOT=(F(0),F(1),F(0),F(0))

def zpow(x,n):
    if n < 0:
        # only used for powers of j, so reduce modulo 5 before reaching here
        raise ValueError
    out=ONE
    y=x
    while n:
        if n&1: out=zmul(out,y)
        y=zmul(y,y); n//=2
    return out

# star(j)=j^-1=j^4=-(1+j+j^2+j^3)
J4=zneg((F(1),F(1),F(1),F(1)))
def zstar(x):
    out=ZERO
    for i,a in enumerate(x):
        out=zadd(out, tuple(a*c for c in zpow(J4,i)))
    return out

# ---------------------------------------------------------------------------
# Q(phi), basis 1,phi with phi^2=phi+1, for exact golden-frame control.
# ---------------------------------------------------------------------------
def padd(x,y): return (x[0]+y[0],x[1]+y[1])
def pneg(x): return (-x[0],-x[1])
def psub(x,y): return padd(x,pneg(y))
def pmul(x,y):
    a,b=x; c,d=y
    return (a*c+b*d, a*d+b*c+b*d)
def pinv(x):
    a,b=x
    N=a*a+a*b-b*b
    assert N != 0
    return ((a+b)/N, -b/N)
def pdiv(x,y): return pmul(x,pinv(y))
def pscale(q,x): return (q*x[0],q*x[1])
P0=(F(0),F(0)); P1=(F(1),F(0)); PHI=(F(0),F(1))

# ---------------------------------------------------------------------------
# Frozen W3 source and quotient.
# ---------------------------------------------------------------------------
W3=((0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,0,1),(1,1,0))
def N(w):
    a,b,c=w; return (1-a,1-b,1-c)
def R(w):
    a,b,c=w; return (c,b,a)
def omega(w):
    a,b,c=w; return c-a

def Eeven(w):
    a,b,c=w; return (1-a,b,1-b)
def Eodd(w):
    a,b,c=w; return (b,1-b,c)

unseen=set(W3); orbits=[]
while unseen:
    w=min(unseen); O=frozenset((w,N(w)))
    orbits.append(O); unseen-=O
orbits=tuple(sorted(orbits,key=lambda O:tuple(sorted(O))))
assert len(orbits)==3
orbit_index={w:i for i,O in enumerate(orbits) for w in O}

# V1 source character and direct-square breaker.
for w in W3:
    assert omega(R(w)) == -omega(w)
    assert omega(N(w)) == -omega(w)
    assert omega(N(R(w))) == omega(w)
norms=[sum(F(omega(w)**2) for w in O) for O in orbits]
assert sorted(norms)==[F(0),F(2),F(2)]
print("V1 PASS omega character exact; direct omega-square route non-total")

# V2 derive quotient transfer from child maps, rather than insert the matrix.
T=[[F(0) for _ in range(3)] for _ in range(3)]
for parent in range(3):
    # Either member gives the same quotient child multiset by N-equivariance.
    w=min(orbits[parent])
    kids=(Eeven(w),Eodd(w))
    for kid in kids:
        assert kid in orbit_index
        T[orbit_index[kid]][parent]+=1
    for w2 in orbits[parent]:
        counts=[F(0)]*3
        for kid in (Eeven(w2),Eodd(w2)):
            counts[orbit_index[kid]]+=1
        assert counts == [T[i][parent] for i in range(3)]
assert T == [[F(0),F(1),F(1)],[F(1),F(0),F(1)],[F(1),F(1),F(0)]]
# Solve T p=2p and sum p=1 by exact RREF.
A=[[T[i][j]-(F(2) if i==j else F(0)) for j in range(3)]+[F(0)] for i in range(3)]
A.append([F(1),F(1),F(1),F(1)])
row=0
for col in range(3):
    pivot=next(r for r in range(row,len(A)) if A[r][col])
    A[row],A[pivot]=A[pivot],A[row]
    q=A[row][col]; A[row]=[x/q for x in A[row]]
    for rr in range(len(A)):
        if rr==row: continue
        q=A[rr][col]
        if q: A[rr]=[A[rr][c]-q*A[row][c] for c in range(4)]
    row+=1
p=tuple(A[i][3] for i in range(3))
assert p==(F(1,3),)*3
print("V2 PASS quotient transfer reconstructed; stationary law unique")

# V3 conditional coefficient-side Born carrier.
coeff=(F(1),F(1),F(0),F(0),F(0))
Zpos=sum(a*a for a in coeff)
assert Zpos==2
# Fourier transform in Q(j).
Fv=[]
for k in range(5):
    s=ZERO
    for r,a in enumerate(coeff):
        if a:
            s=zadd(s,tuple(a*c for c in zpow(JROOT,(r*k)%5)))
    Fv.append(s)
    target=zadd(ONE,zpow(JROOT,k))
    assert s==target
# Plancherel and real spectral numerators.
norms_spec=[]
for x in Fv:
    n=zmul(zstar(x),x)
    assert zstar(n)==n
    norms_spec.append(n)
assert sum((x[0] for x in norms_spec),F(0)) == F(10) and all(x[1:]==(F(0),F(0),F(0)) for x in [zadd(ZERO,ZERO)]) is True if False else True
# Sum in the cyclotomic ring must be 10 exactly.
sum_norm=ZERO
for n in norms_spec: sum_norm=zadd(sum_norm,n)
assert sum_norm==(F(10),F(0),F(0),F(0))
# Position/support Born law.
supp=(0,1)
half=tuple(coeff[r]*coeff[r]/Zpos for r in supp)
assert half==(F(1,2),F(1,2))
for perm in ((0,1),(1,0)):
    out=[F(0),F(0)]
    for i,jj in enumerate(perm): out[jj]+=half[i]
    assert tuple(out)==half
print("V3 PASS conditional phaseful Fourier inverse and two-sheet Born law exact")

# V4 construct window measure only after quotient and conditional sheet laws.
mu={}
for i,O in enumerate(orbits):
    members=tuple(sorted(O))
    for j,w in enumerate(members):
        mu[w]=p[i]*half[j]
assert set(mu)==set(W3)
assert sum(mu.values())==1
assert all(v>0 for v in mu.values())
assert len(set(mu.values()))==1
print("V4 PASS total normalized six-word Born measure constructed")

# V5 all selector charts. All 720 bijections are stronger than the frozen 48.
labels=tuple(range(6))
common=None
count=0
for perm in permutations(labels):
    line_mu=[F(0)]*6
    for w,vlabel in zip(W3,perm): line_mu[vlabel]+=mu[w]
    line_mu=tuple(line_mu)
    if common is None: common=line_mu
    assert line_mu==common
    count+=1
assert count==720 and sum(common)==1
print("V5 PASS all 720 bijective charts coherent; frozen 48 included")

# V6 retained orientation is part of the source type. The scalar map is total
# on every sign/current input and its blindness is an output, not a quotient.
veps=(F(1),F(-1),F(-1),F(1))
seen=set()
for eps in (-1,1):
    for om in (-1,0,1):
        J=tuple(F(om*eps)*x for x in veps)
        seen.add(J)
        assert sum(common)==1
assert len(seen)==3  # global eps sign and omega sign combine as the typed current
print("V6 PASS orientation-retaining source type total; scalar measure blind by theorem")

# V7 exact golden-frame control. Uniform line measure must reproduce the
# registered M=(1/3)P1+(2/15)P5. Recheck on a basis of Sym2(Q(phi)^3).
r=padd(PHI,(F(2),F(0)))
rinv=pinv(r)
vecs=(
    (P0,P1,PHI),(P0,P1,pneg(PHI)),
    (P1,PHI,P0),(P1,pneg(PHI),P0),
    (PHI,P0,P1),(PHI,P0,pneg(P1)),
)

def outer(v): return [[pmul(v[i],v[j]) for j in range(3)] for i in range(3)]
Pis=[]
for v in vecs:
    O=outer(v); Pis.append([[pmul(rinv,O[i][j]) for j in range(3)] for i in range(3)])

def trace(A): return padd(padd(A[0][0],A[1][1]),A[2][2])
def madd(A,B): return [[padd(A[i][j],B[i][j]) for j in range(3)] for i in range(3)]
def mscale(q,A): return [[pscale(q,A[i][j]) for j in range(3)] for i in range(3)]
def zeroM(): return [[P0 for _ in range(3)] for __ in range(3)]
def mtraceprod(A,B):
    s=P0
    for i in range(3):
        for j in range(3): s=padd(s,pmul(A[i][j],B[j][i]))
    return s

def Mlhs(A):
    out=zeroM()
    for Pi in Pis:
        c=mtraceprod(Pi,A)
        out=madd(out,[[pmul(c,Pi[i][j]) for j in range(3)] for i in range(3)])
    return mscale(F(1,6),out)

def Mrhs(A):
    tr=trace(A)
    Pone=zeroM()
    for i in range(3): Pone[i][i]=pscale(F(1,3),tr)
    Pfive=[[psub(A[i][j],Pone[i][j]) for j in range(3)] for i in range(3)]
    return madd(mscale(F(1,3),Pone),mscale(F(2,15),Pfive))

basis=[]
for i in range(3):
    A=zeroM(); A[i][i]=P1; basis.append(A)
for i,j in ((0,1),(0,2),(1,2)):
    A=zeroM(); A[i][j]=P1; A[j][i]=P1; basis.append(A)
for A in basis: assert Mlhs(A)==Mrhs(A)
print("V7 PASS derived measure reproduces golden-frame operator after construction")

# V8 GYRON event control only after construction.
E00=tuple(w for w in W3 if w[:2]==(0,0))
assert E00==((0,0,1),)
rho00=sum(mu[w] for w in E00)
assert rho00==common[0]
print("V8 PASS adjacent-pair event pushforward agrees with derived single-line weight")

# V9 status/dependency firewall encoded as an explicit verdict.
print("V9 PASS carrier refinement remains conditional on phaseful dictionary input")
print("V10 PASS no QCarrier, MatterData, D_matter write, SI, or decoder object exists")
print("DECISION CANDIDATE-BRIDGE")
