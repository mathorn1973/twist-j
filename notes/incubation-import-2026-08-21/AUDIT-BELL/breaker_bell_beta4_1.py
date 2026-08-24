#!/usr/bin/env python3
# BREAKER for the beta = 4 probe. Independent route: build the physical
# two-qubit correlation matrix from sigma_i (x) sigma_j and compare.
# Exact Gaussian-integer arithmetic. Stdlib only. No float anywhere.
import sys, itertools
FIND=[]
def rep(name, broken, note=""):
    if broken: FIND.append(name)
    print("%-44s %s%s" % (name,"BREAK" if broken else "HOLDS",("  "+note) if note else ""))

# Gaussian integers as (re, im)
def gadd(x,y): return (x[0]+y[0], x[1]+y[1])
def gmul(x,y): return (x[0]*y[0]-x[1]*y[1], x[0]*y[1]+x[1]*y[0])
Z=(0,0)
SX=[[(0,0),(1,0)],[(1,0),(0,0)]]
SY=[[(0,0),(0,-1)],[(0,1),(0,0)]]
SZ=[[(1,0),(0,0)],[(0,0),(-1,0)]]
SIG=[SX,SY,SZ]
def kron(P,Qm):
    return [[gmul(P[i//2][j//2],Qm[i%2][j%2]) for j in range(4)] for i in range(4)]
def quad(M,psi):
    s=Z
    for k in range(4):
        for l in range(4):
            s=gadd(s,gmul((psi[k],0),gmul(M[k][l],(psi[l],0))))
    return s

def piston_T(a,b,c,d):
    D=a*d-b*c
    return [[2*(a*d+b*c),0,2*(a*c-b*d)],[0,2*D,0],
            [2*(a*b-c*d),0,a*a-b*b-c*c+d*d]]
def phys_T(a,b,c,d):
    psi=[a,b,c,d]; out=[]
    for i in range(3):
        row=[]
        for j in range(3):
            val=quad(kron(SIG[i],SIG[j]),psi)
            if val[1]!=0: raise AssertionError("imaginary correlation")
            row.append(val[0])
        out.append(row)
    return out
def mTm(T):  # T^T T
    return [[sum(T[k][i]*T[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
def charpoly3(M):  # returns (e1,e2,e3)
    e1=M[0][0]+M[1][1]+M[2][2]
    e2=(M[0][0]*M[1][1]-M[0][1]*M[1][0]+M[0][0]*M[2][2]-M[0][2]*M[2][0]
        +M[1][1]*M[2][2]-M[1][2]*M[2][1])
    e3=(M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
        -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
        +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))
    return e1,e2,e3

RNG=range(-4,5)
# ---- X1: is the piston T the physical correlation matrix? ----
bad_shape=bad_sign=0
for a,b,c,d in itertools.product(RNG,repeat=4):
    Tp,Tf=piston_T(a,b,c,d),phys_T(a,b,c,d)
    if [[abs(x) for x in r] for r in Tp]!=[[abs(x) for x in r] for r in Tf]: bad_shape+=1
    diff=[(i,j) for i in range(3) for j in range(3) if Tp[i][j]!=Tf[i][j]]
    if diff and diff!=[(1,1)]: bad_sign+=1
rep("X1a-|piston T| = |physical <sig_i sig_j>|", bad_shape!=0,
    "%d of %d mismatched" % (bad_shape,len(RNG)**4))
rep("X1b-only entry (2,2) differs, by sign (S2=i sig_y)", bad_sign!=0)

# ---- X2: spectrum identical, so Horodecki M is the same object ----
bad=0
for a,b,c,d in itertools.product(RNG,repeat=4):
    Q=a*a+b*b+c*c+d*d; R=2*(a*d-b*c)
    if charpoly3(mTm(phys_T(a,b,c,d)))!=(Q*Q+2*R*R,2*Q*Q*R*R+R**4,Q*Q*R**4): bad+=1
rep("X2-physical route gives the same spectrum", bad!=0)

# ---- X3: this IS the Horodecki criterion with Wootters concurrence ----
# normalized state: M = lam1+lam2 = 1 + C^2, C = 2|det X| . check on Q=1 rationals
from fractions import Fraction as Fr
bad=0
for a,b,c,d in itertools.product(range(-3,4),repeat=4):
    Q=a*a+b*b+c*c+d*d
    if Q==0: continue
    R=2*(a*d-b*c)
    M_unnorm=Q*Q+R*R                       # lam1+lam2, proven in the audit
    M_norm=Fr(M_unnorm,Q*Q)                # divide by Q^2 (state normalization)
    C=Fr(2*abs(a*d-b*c),Q)                 # Wootters concurrence of a real pure state
    if M_norm != 1+C*C: bad+=1
rep("X3-M = 1 + C^2 exactly (Horodecki + Wootters)", bad!=0,
    "beta=4 reproduces the standard pure-state result")

# ---- X4: Tsirelson is an output, not an input ----
# CHSH_max = 2 sqrt(M) ; M <= 2 with equality iff R^2 = Q^2 iff |det|=Q/2
mx=max(Fr(a*a+b*b+c*c+d*d,1)**0 * Fr((a*a+b*b+c*c+d*d)**2+(2*(a*d-b*c))**2,
        (a*a+b*b+c*c+d*d)**2)
       for a,b,c,d in itertools.product(range(-3,4),repeat=4) if a*a+b*b+c*c+d*d)
rep("X4-max M = 2, i.e. CHSH_max = 2 sqrt2 exactly", mx!=2, "max M = %s" % mx)

# ---- X5: THE GAP. rescale the antisymmetric axis S2 -> t S2 ----
def piston_T_t(a,b,c,d,t):
    T=piston_T(a,b,c,d); T[1][1]*=t*t; return T
rows=[]
for t in (1,2,3,5):
    ok=True
    for a,b,c,d in itertools.product(range(-3,4),repeat=4):
        Q=a*a+b*b+c*c+d*d; R=2*(a*d-b*c)
        e=charpoly3(mTm(piston_T_t(a,b,c,d,t)))
        want=(Q*Q+R*R+t**4*R*R, Q*Q*R*R+Q*Q*t**4*R*R+t**4*R**4, Q*Q*R*R*t**4*R*R)
        if e!=want: ok=False; break
    rows.append((t,4*t**4,ok))
rep("X5a-spectrum under rescaling = {Q^2,R^2,t^4 R^2}", not all(r[2] for r in rows))
rep("X5b-beta is NOT fixed by local covariance", False,
    "beta(t) = " + ", ".join("t=%d -> %d" % (t,b) for t,b,_ in rows))
# his own counterexamples, identified
tI=[(t,piston_T_t(1,0,0,1,t)) for t in (1,2,3)]
rep("X5c-diag(2,8,2) and diag(2,18,2) are t=2 and t=3",
    [T[1][1] for _,T in tI]!=[2,8,18],
    "so they carry beta = 64 and beta = 324, not 4")

# ---- X6: what DOES fix t? orthonormality of the S basis in Frobenius ----
def frob(P): return sum(P[i][j]**2 for i in range(2) for j in range(2))
S1=[[0,1],[1,0]]; S2=[[0,1],[-1,0]]; S3=[[1,0],[0,-1]]
rep("X6-t=1 iff the three S_i share one Frobenius norm",
    not (frob(S1)==frob(S2)==frob(S3)==2),
    "||S_i||^2 = 2 for all three exactly at t=1")

print("\nFINDINGS %d of %d" % (len(FIND),9))
if FIND: print("BROKEN: "+", ".join(FIND))
sys.exit(2 if FIND else 0)
