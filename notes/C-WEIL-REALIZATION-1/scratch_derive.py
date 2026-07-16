#!/usr/bin/env python3
# Scratch derivation pass for C-WEIL-REALIZATION-1. Prints, asserts nothing.
from fractions import Fraction
from itertools import combinations

# ---- Z[zeta_5] ----
def zmul(a, b):
    c = [0]*7
    for i in range(4):
        for k in range(4):
            c[i+k] += a[i]*b[k]
    r = [c[0]+c[5], c[1]+c[6], c[2], c[3]]
    k4 = c[4]
    return (r[0]-k4, r[1]-k4, r[2]-k4, r[3]-k4)

def zpow(a, n):
    r = (1,0,0,0)
    for _ in range(n):
        r = zmul(r, a)
    return r

def zsub(a,b): return tuple(x-y for x,y in zip(a,b))
def zadd(a,b): return tuple(x+y for x,y in zip(a,b))

J = (1,0,1,0)  # 1 + zeta^2
Z5 = (0,1,0,0)

# sigma_k: zeta -> zeta^k
def sigma(a, k):
    out = (a[0],0,0,0)
    for i in (1,2,3):
        t = zpow(Z5, (i*k) % 5)
        out = zadd(out, tuple(a[i]*x for x in t))
    return out

def norm(a):
    p = (1,0,0,0)
    for k in (1,2,3,4):
        p = zmul(p, sigma(a,k))
    return p

# ---- M_J two ways ----
cols = [zmul(J, zpow(Z5,i)) for i in range(4)]
M = [[cols[j][i] for j in range(4)] for i in range(4)]
print("M_J rows:", M)
def stepmap(v):
    a,b,c,d = v
    return (a-c+d, b-c, a, b-c+d)
import random
print("step map == M?", all(stepmap((a,b,c,d)) == tuple(sum(M[i][j]*[a,b,c,d][j] for j in range(4)) for i in range(4)) for a in range(-2,3) for b in range(-2,3) for c in range(-2,3) for d in range(-2,3)))

# ---- char poly (Faddeev-LeVerrier, exact) ----
def matmul(A,B):
    n=len(A); m=len(B[0]); K=len(B)
    return [[sum(A[i][k]*B[k][j] for k in range(K)) for j in range(m)] for i in range(n)]
def charpoly(A):
    n=len(A)
    I=[[1 if i==j else 0 for j in range(n)] for i in range(n)]
    c=[1]
    Mk=[row[:] for row in I]
    for k in range(1,n+1):
        Mk=matmul(A,Mk)
        ck=-sum(Mk[i][i] for i in range(n))
        assert ck % k == 0 or True
        ck=ck//k if sum(Mk[i][i] for i in range(n))%k==0 else Fraction(-sum(Mk[i][i] for i in range(n)),k)
        # redo cleanly with Fractions to be safe
        c.append(ck)
        for i in range(n):
            Mk[i][i]+=ck
    return c  # coefficients of z^n + c1 z^(n-1) + ... + cn

print("charpoly M:", charpoly(M))

# ---- N_m two paths ----
def matpow(A,m):
    n=len(A)
    R=[[1 if i==j else 0 for j in range(n)] for i in range(n)]
    for _ in range(m):
        R=matmul(R,A)
    return R
def det4(A):
    # cofactor, exact ints/fractions
    n=len(A)
    if n==1: return A[0][0]
    s=0
    for j in range(n):
        minor=[row[:j]+row[j+1:] for row in A[1:]]
        s += (-1)**j * A[0][j] * det4(minor)
    return s

print("m : det(M^m - I) : N(J^m - 1)")
for m in range(1,13):
    Mm = matpow(M,m)
    A = [[Mm[i][j]-(1 if i==j else 0) for j in range(4)] for i in range(4)]
    d = det4(A)
    nj = norm(zsub(zpow(J,m),(1,0,0,0)))
    print(m, d, nj)

# ---- exterior powers ----
def ext2(A):
    idx = list(combinations(range(4),2))
    B=[[0]*6 for _ in range(6)]
    for r,(i,j) in enumerate(idx):
        for c,(k,l) in enumerate(idx):
            B[r][c] = A[i][k]*A[j][l] - A[i][l]*A[j][k]
    return B
def ext3(A):
    idx = list(combinations(range(4),3))
    B=[[0]*4 for _ in range(4)]
    for r,rows in enumerate(idx):
        for c,colsx in enumerate(idx):
            sub=[[A[i][j] for j in colsx] for i in rows]
            B[r][c]=det4(sub)
    return B

L2 = ext2(M); L3 = ext3(M)
print("charpoly L2:", charpoly(L2))
print("charpoly L3:", charpoly(L3))
# target factorization check: (z^2-3z+1)*Phi_10 = z^6-4z^5+5z^4-5z^3+5z^2-4z+1
def polymul(p,q):
    r=[0]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):
            r[i+j]+=a*b
    return r
print("(z^2-3z+1)*Phi_10:", polymul([1,-3,1],[1,-1,1,-1,1]))

# ---- Artin-Mazur series identity, order 12 ----
def poly_eval_series_inv(coeffs, order):
    # series of 1/det-poly ... we need series of exp(sum N_m z^m/m)
    pass
def series_log_of_poly(coeffs, order):
    # log(p(z)) as series, p(0)=1; coeffs ascending
    p = [Fraction(c) for c in coeffs] + [Fraction(0)]*(order+1-len(coeffs))
    # dlog = p'/p ; integrate
    dp = [p[i]*i for i in range(1,order+1)]
    inv = [Fraction(0)]*(order+1)
    inv[0] = 1/p[0]
    for n in range(1,order+1):
        s = Fraction(0)
        for k in range(1,n+1):
            s += p[k]*inv[n-k]
        inv[n] = -s/p[0]
    d = [Fraction(0)]*(order+1)
    for n in range(order+1):
        s=Fraction(0)
        for k in range(min(n,len(dp)-0)):
            if k < len(dp) and n-k <= order:
                s += (dp[k] if k < len(dp) else 0)*inv[n-k]
        d[n]=s
    out=[Fraction(0)]*(order+1)
    for n in range(1,order+1):
        out[n] = d[n-1]/n
    return out

def detpoly(A, order):
    # det(I - z A) ascending coefficients via charpoly: det(zI - A) = z^n + c1 z^(n-1)+...
    n=len(A)
    c = charpoly(A)  # z^n + c1 z^{n-1} + ... + cn
    # det(I - zA) = z^n * cp(1/z) with cp monic: = 1 + c1 z + c2 z^2 + ... cn z^n? check:
    # det(zI - A) = sum_k c_k z^{n-k}, c_0=1. det(I - zA) = z^n det((1/z)I - A) = sum_k c_k z^{k}. yes
    return [int(x) for x in c]

asc0 = [1,-1]  # det(I - z*1) for Lambda^0 (scalar 1)
asc4 = [1,-1]  # Lambda^4 = det = 1
asc1 = detpoly(M,12)
asc2 = detpoly(L2,12)
asc3 = detpoly(L3,12)
ORDER=12
# zeta_AM = det1 * det3 / (det0 * det2 * det4)?? signs: exp sum N_m z^m/m with N_m = sum_k (-1)^k tr Lambda^k M^m
# = prod_k det(I - z Lambda^k M)^{(-1)^{k+1}}
# k=0 term: (-1)^0 tr = 1 -> factor det(1 - z)^{-1}
# so zeta = [det(I-zL1) det(I-zL3)] / [(1-z)(1-z) det(I-zL2)]  (k=0 and k=4 in denominator)
lhs = [Fraction(0)]*(ORDER+1)
for m in range(1,ORDER+1):
    Mm=matpow(M,m)
    A=[[Mm[i][j]-(1 if i==j else 0) for j in range(4)] for i in range(4)]
    Nm = det4(A)
    lhs[m] = Fraction(Nm,m)
# exp series
expo=[Fraction(0)]*(ORDER+1); expo[0]=Fraction(1)
for n in range(1,ORDER+1):
    s=Fraction(0)
    for k in range(1,n+1):
        s += k*lhs[k]*expo[n-k]
    expo[n]=s/n
# rhs series: log-based
def series_from_polys(nums, dens, order):
    out=[Fraction(0)]*(order+1)
    for p in nums:
        lg = series_log_of_poly(p, order)
        out=[a+b for a,b in zip(out,lg)]
    for p in dens:
        lg = series_log_of_poly(p, order)
        out=[a-b for a,b in zip(out,lg)]
    # exp
    e=[Fraction(0)]*(order+1); e[0]=Fraction(1)
    for n in range(1,order+1):
        s=Fraction(0)
        for k in range(1,n+1):
            s += k*out[k]*e[n-k]
        e[n]=s/n
    return e
rhs = series_from_polys([asc1,asc3],[[1,-1],[1,-1],asc2], ORDER)
print("AM zeta series equal to order 12?", expo==rhs)
print("zeta_AM coefficients:", [str(x) for x in expo[:9]])

# ---- arithmetic layer: characters mod 5 in Z[i], convolution a_K ----
# chi(2)=i fixes the quartic character; residues: 1,2,3,4 -> chi values
# 2 is a generator: 2^1=2,2^2=4,2^3=3,2^4=1
chi_of = {1:(1,0), 2:(0,1), 4:(-1,0), 3:(0,-1)}  # (re,im) of chi(n mod 5)
def cxmul(a,b): return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])
def chi_pow(n, j):
    if n%5==0: return (0,0)
    v=(1,0)
    for _ in range(j): v=cxmul(v, chi_of[n%5])
    return v
N=3000
aK=[None]*(N+1)
# iterated Dirichlet convolution 1 * chi * chi^2 * chi^3
b=[(0,0)]*(N+1)
for d in range(1,N+1):
    for n in range(d,N+1,d):
        b[n]=(b[n][0]+chi_pow(n//d,1)[0], b[n][1]+chi_pow(n//d,1)[1])  # (1*chi)(n)=sum_{d|n} chi(n/d)
c2=[(0,0)]*(N+1)
for d in range(1,N+1):
    for n in range(d,N+1,d):
        t=cxmul(b[d], chi_pow(n//d,2))
        c2[n]=(c2[n][0]+t[0], c2[n][1]+t[1])
c3=[(0,0)]*(N+1)
for d in range(1,N+1):
    for n in range(d,N+1,d):
        t=cxmul(c2[d], chi_pow(n//d,3))
        c3[n]=(c3[n][0]+t[0], c3[n][1]+t[1])
bad=[n for n in range(1,N+1) if c3[n][1]!=0 or c3[n][0]<0]
print("a_K imaginary/negative anomalies:", bad[:5], "count", len(bad))
spot={1:None,2:None,3:None,4:None,5:None,11:None,16:None,25:None,31:None,41:None,55:None,61:None,81:None,121:None,256:None,361:None,605:None}
for n in spot:
    if n<=N: spot[n]=c3[n][0]
print("a_K spot:", spot)

# roots of Phi_5 mod p vs a_K(p)
def nroots(p):
    return sum(1 for x in range(p) if (1+x+x*x+x**3+x**4)%p==0)
prs=[p for p in range(2,200) if all(p%q for q in range(2,p))]
mism=[(p,nroots(p),c3[p][0]) for p in prs if p<=N and nroots(p)!=c3[p][0]]
print("hyperplane-count mismatches (should be empty):", mism)

# ---- Gauss sums in Z[zeta_20] ----
# Phi_20(x) = x^8 - x^6 + x^4 - x^2 + 1; basis z^0..z^7, z = zeta_20
PHI20=[1,0,-1,0,1,0,-1,0,1]  # ascending: 1 - x^2 + x^4 - x^6 + x^8 -> careful sign order
# Phi_20 = x^8 - x^6 + x^4 - x^2 + 1 (ascending: [1,0,-1,0,1,0,-1,0,1])
def z20mul(a,b):
    c=[0]*15
    for i in range(8):
        for j in range(8):
            c[i+j]+=a[i]*b[j]
    # reduce degree >=8 using x^8 = x^6 - x^4 + x^2 - 1
    for d in range(14,7,-1):
        k=c[d]
        if k:
            c[d]=0
            c[d-2]+=k
            c[d-4]-=k
            c[d-6]+=k
            c[d-8]-=k
    return tuple(c[:8])
def z20pow(a,n):
    r=(1,0,0,0,0,0,0,0)
    for _ in range(n): r=z20mul(r,a)
    return r
Z20=(0,1,0,0,0,0,0,0)
zeta5_20 = z20pow(Z20,4)
i_20 = z20pow(Z20,5)
def z20add(a,b): return tuple(x+y for x,y in zip(a,b))
def z20scale(a,s): return tuple(s*x for x in a)
def z20conj(a):
    # z -> z^-1 = z^19
    out=(0,)*8
    for e in range(8):
        if a[e]:
            out=z20add(out, z20scale(z20pow(Z20,(19*e)%20), a[e]))
    return out
def gauss(j):
    g=(0,)*8
    for a in range(1,5):
        chv = chi_pow(a,j)  # in Z[i]
        term = z20add(z20scale(z20pow(zeta5_20,a), chv[0]), z20scale(z20mul(i_20, z20pow(zeta5_20,a)), chv[1]))
        g=z20add(g,term)
    return g
for j in (1,2,3):
    g=gauss(j)
    print("g(chi^%d) ="%j, g, " g*conj(g) =", z20mul(g, z20conj(g)))
# Fourier bridge: 4*zeta5^n = sum_j chibar^j(n) g(chi^j), j=0..3, g(chi^0) = sum_a zeta^a = -1
g0=(0,)*8
for a in range(1,5): g0=z20add(g0, z20pow(zeta5_20,a))
print("g(chi^0) =", g0)
for n in (1,2,3,4):
    tot=(0,)*8
    for j in range(4):
        g = g0 if j==0 else gauss(j)
        ch = chi_pow(n,j)
        chbar = (ch[0],-ch[1])
        tot=z20add(tot, z20add(z20scale(g,chbar[0]), z20scale(z20mul(i_20,g),chbar[1])))
    lhs = z20scale(z20pow(zeta5_20,n),4)
    print("bridge n=%d ok?"%n, tot==lhs)

# ---- disc(Phi_5) via prod (zeta^i - zeta^j)^2 ----
p=(1,0,0,0)
for i in range(1,5):
    for j in range(i+1,5):
        d = zsub(zpow(Z5,i), zpow(Z5,j))
        p = zmul(p, zmul(d,d))
print("disc(Phi_5) =", p)
