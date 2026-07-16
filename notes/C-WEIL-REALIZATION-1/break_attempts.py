#!/usr/bin/env python3
# Break attempts against C-WEIL-REALIZATION-1 (independent scrutiny; this
# file is the breaker, not the pinned verifier).
from fractions import Fraction

# --- shared minimal machinery (independent re-implementation where cheap) ---
def cxmul(a, b): return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])

def build_aK(chi2, NMAX=2500):
    chi_of = {1:(1,0), 2:chi2, 4:cxmul(chi2,chi2), 3:cxmul(cxmul(chi2,chi2),chi2)}
    def chp(n, j):
        if n % 5 == 0: return (0,0)
        v = (1,0)
        for _ in range(j): v = cxmul(v, chi_of[n%5])
        return v
    b = [(0,0)]*(NMAX+1)
    for d in range(1, NMAX+1):
        for n in range(d, NMAX+1, d):
            t = chp(n//d, 1); b[n] = (b[n][0]+t[0], b[n][1]+t[1])
    c2 = [(0,0)]*(NMAX+1)
    for d in range(1, NMAX+1):
        if b[d] != (0,0):
            for n in range(d, NMAX+1, d):
                t = cxmul(b[d], chp(n//d, 2)); c2[n] = (c2[n][0]+t[0], c2[n][1]+t[1])
    c3 = [(0,0)]*(NMAX+1)
    for d in range(1, NMAX+1):
        if c2[d] != (0,0):
            for n in range(d, NMAX+1, d):
                t = cxmul(c2[d], chp(n//d, 3)); c3[n] = (c3[n][0]+t[0], c3[n][1]+t[1])
    return c3

# BR1: character-choice independence. chi(2) = i vs chi(2) = -i must give the
# same a_K (the triple product runs over all nontrivial characters either way).
A = build_aK((0,1)); B = build_aK((0,-1))
print("BR1 chi-choice independence: a_K identical for chi(2)=i and chi(2)=-i:", A == B)

# BR2: independent poke at an untabled prime power: 7 has order 4 mod 5, so
# a_K(7)=a_K(49)=a_K(343)=0 and a_K(2401)=1.
print("BR2 f=4 tower at p=7: a_K(7,49,343,2401) =",
      A[7][0], A[49][0], A[343][0], A[2401][0], "expected 0 0 0 1")

# BR3: sensitivity control. Corrupt one Lambda_K rule (p=4 mod 5 at odd m)
# and confirm the log-symbol identity FAILS at the first affected n (19^1=19
# has a_K(19)=0 so first visible failure is n=19*k with a_K(k)>0: n=19*1? lhs
# gets Lambda_K(19)*a_K(1) = {19:4} vs rhs a_K(19)*log19 = {} -> fail at 19).
def factor(n):
    f={}; d=2
    while d*d<=n:
        while n%d==0: f[d]=f.get(d,0)+1; n//=d
        d+=1
    if n>1: f[n]=f.get(n,0)+1
    return f
def lamK(n, corrupt=False):
    f=factor(n)
    if len(f)!=1: return {}
    (p,m), = f.items()
    if p==5: return {5:1}
    r=p%5
    if r==1: return {p:4}
    if r==4: return {p:4} if (m%2==0 or corrupt) else {}
    return {p:4} if m%4==0 else {}
def identity_holds(n, corrupt):
    lhs={}
    for d in range(1,n+1):
        if n%d==0:
            lk=lamK(d,corrupt)
            a=A[n//d][0]
            if lk and a:
                for pp,c in lk.items(): lhs[pp]=lhs.get(pp,0)+c*a
    rhs={}
    if A[n][0]:
        for pp,m in factor(n).items(): rhs[pp]=A[n][0]*m
    return {k:v for k,v in lhs.items() if v} == {k:v for k,v in rhs.items() if v}
print("BR3 corrupted Lambda_K rule detected at n=19:", (not identity_holds(19, True)), "; clean rule holds:", identity_holds(19, False))

# BR4: negative control on the dynamical pillar: a one-entry corruption of
# M_J must break the charpoly assertion (the asserts are not tautological).
def matmul(Aa,Bb):
    n=len(Aa); K=len(Bb); m=len(Bb[0])
    return [[sum(Aa[i][k]*Bb[k][j] for k in range(K)) for j in range(m)] for i in range(n)]
def charpoly(Aa):
    n=len(Aa); c=[1]
    Mk=[[1 if i==j else 0 for j in range(n)] for i in range(n)]
    for k in range(1,n+1):
        Mk=matmul(Aa,Mk)
        t=sum(Mk[i][i] for i in range(n))
        c.append(Fraction(-t,k))
        for i in range(n): Mk[i][i]+=c[-1]
    return c
M=[[1,0,-1,1],[0,1,-1,0],[1,0,0,0],[0,1,-1,1]]
Mbad=[row[:] for row in M]; Mbad[0][0]=2
print("BR4 corrupted M detected:", charpoly(Mbad) != [1,-3,4,-2,1], "; true M gives target:", [int(x) for x in charpoly(M)] == [1,-3,4,-2,1])

# BR5: gamma bracket direction, small-N float witness (not an assertion of
# the pinned verifier; here as an independent sanity check of the imported
# inequality 1/(2(N+1)) < H_N - ln N - gamma < 1/(2N)).
import math
for N in (10, 100, 1000):
    H=sum(1.0/k for k in range(1,N+1))
    lo=H-math.log(N)-1/(2*N); hi=H-math.log(N)-1/(2*(N+1))
    print("BR5 N=%d bracket (%.10f, %.10f) contains gamma 0.5772156649: %s"
          % (N, lo, hi, lo < 0.5772156649015329 < hi))

# BR6: lambda_1 cross-check against a float evaluation (witness only).
lam1_float = 1 + 0.5772156649015329/2 - math.log(4*math.pi)/2
print("BR6 float lambda_1 = %.15f inside pinned interval [0.023095708964233559, 0.023095708972138893]: %s"
      % (lam1_float, 0.023095708964233559 < lam1_float < 0.023095708972138893))
