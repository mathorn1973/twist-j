#!/usr/bin/env python3
# One question: WHY is the motor commutant empty? Exact, stdlib only.
from fractions import Fraction as F
import itertools, sys
def mat(r): return tuple(tuple(F(x) for x in row) for row in r)
def mmul(A,B): return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(len(B)))
                for j in range(len(B[0]))) for i in range(len(A)))
def msub(A,B): return tuple(tuple(A[i][j]-B[i][j] for j in range(4)) for i in range(4))
def eye(n): return tuple(tuple(F(1) if i==j else F(0) for j in range(n)) for i in range(n))
def zeros(): return tuple(tuple(F(0) for _ in range(4)) for _ in range(4))
def flat(A): return tuple(A[i][j] for i in range(4) for j in range(4))
def rank(rows):
    R=[list(r) for r in rows]; rk=0; row=0
    for col in range(len(R[0]) if R else 0):
        p=next((r for r in range(row,len(R)) if R[r][col]!=0),None)
        if p is None: continue
        R[row],R[p]=R[p],R[row]; pv=R[row][col]; R[row]=[x/pv for x in R[row]]
        for r in range(len(R)):
            if r!=row and R[r][col]!=0:
                f=R[r][col]; R[r]=[a-f*b for a,b in zip(R[r],R[row])]
        row+=1; rk+=1
    return rk

MJ=mat([[1,0,-1,1],[0,1,-1,0],[1,0,0,0],[0,1,-1,1]]); I4=eye(4); D=msub(MJ,I4)
D2=mmul(D,D); D3=mmul(D2,D)

# 1. min poly of D is Phi_5, so Q[D] = Q[x]/(Phi_5) = Q(zeta_5), a FIELD.
print("min poly degree 4 (I,D,D2,D3 independent):",
      rank([flat(I4),flat(D),flat(D2),flat(D3)])==4)
print("Phi_5(D) = 0:", msub(mmul(D3,D), msub(zeros(),
      tuple(tuple(I4[i][j]+D[i][j]+D2[i][j]+D3[i][j] for j in range(4))
            for i in range(4))))==zeros())

# 2. every nonzero element of Q[D] is invertible  -> exhaustive small test
noninv=0
for co in itertools.product(range(-3,4),repeat=4):
    if co==(0,0,0,0): continue
    A=tuple(tuple(co[0]*I4[i][j]+co[1]*D[i][j]+co[2]*D2[i][j]+co[3]*D3[i][j]
            for j in range(4)) for i in range(4))
    if rank([list(r) for r in A])!=4: noninv+=1
print("nonzero elements of Q[D] that are singular:", noninv, "of 2400")

# 3. therefore A M = 0 with A in Q[D] forces A = 0 for ANY nonzero M,
#    not merely for the stabilizer projector. Test many anchors.
bad=0
for trial in range(1,200):
    M=tuple(tuple(F(((trial*7+3*i+5*j)%11)-5) for j in range(4)) for i in range(4))
    if M==zeros(): continue
    rows=[]
    for B in (I4,D,D2,D3): rows.append(flat(mmul(B,M)))
    if 4-rank(rows)!=0: bad+=1
print("anchors M != 0 admitting a nonzero motor-equivariant law:", bad, "of 199")
print()
print("E4 mechanism: comm(D) = Q[D] = Q(zeta_5) is a FIELD because Phi_5 is")
print("irreducible, i.e. because 5 is prime. A field has no zero divisors, so")
print("no nonzero motor-equivariant operator can annihilate any nonzero record.")
