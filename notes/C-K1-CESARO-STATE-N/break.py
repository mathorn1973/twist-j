#!/usr/bin/env python3
"""Same-agent cross-check by rational Krylov projection, no spectral code imported.

This is NOT blind two-agent confirmation. It uses only Fraction and derives
its own annihilating polynomial from the exact 8-dimensional recurrence.
"""
from fractions import Fraction as F
import json

def transpose(a): return list(map(list,zip(*a)))
def product(a,b):
    bt=transpose(b)
    return [[sum((x*y for x,y in zip(row,col)),F(0)) for col in bt] for row in a]
def zeros(n,m): return [[F(0) for _ in range(m)] for _ in range(n)]
def flat(a): return [x for row in a for x in row]
def lincomb(coeff, mats):
    return [[sum((c*a[i][j] for c,a in zip(coeff,mats)),F(0))
             for j in range(len(mats[0][0]))] for i in range(len(mats[0]))]
def linear_solve(columns,b):
    """Return a solution to independent-column A x=b, or None if inconsistent."""
    m=len(columns)
    rows=[[columns[j][i] for j in range(m)]+[b[i]] for i in range(len(b))]
    pivotrow=0; pivots=[]
    for col in range(m):
        found=next((i for i in range(pivotrow,len(rows)) if rows[i][col]),None)
        if found is None: raise AssertionError('Krylov columns ceased to be independent')
        rows[pivotrow],rows[found]=rows[found],rows[pivotrow]
        p=rows[pivotrow][col]
        rows[pivotrow]=[x/p for x in rows[pivotrow]]
        for i in range(len(rows)):
            if i!=pivotrow and rows[i][col]:
                f=rows[i][col]
                rows[i]=[x-f*y for x,y in zip(rows[i],rows[pivotrow])]
        pivots.append((pivotrow,col));pivotrow+=1
    if any(all(x==0 for x in row[:m]) and row[m]!=0 for row in rows): return None
    out=[F(0)]*m
    for r,c in pivots: out[c]=rows[r][m]
    return out

L=[[F(188 if i==j else -29 if (j-i)%5 in (1,4) else -65,324)
    for j in range(5)] for i in range(5)]
# E identifies Q^4 with the zero-sum subspace of Q^5.
E=[[F(i==j) for j in range(4)] for i in range(4)]+[[-F(1)]*4]
Lr=[[L[i][j]-L[i][4] for j in range(4)] for i in range(4)]
T=zeros(8,8)
for i in range(4):
    for j in range(4):
        T[i][j]=2*F(i==j)-Lr[i][j]
        T[i][j+4]=-F(i==j)
        T[i+4][j]=F(i==j)
W=('0010','0011','0100','0101','0110','1001','1010','1011','1100','1101')
K0=zeros(8,8)
for word in W:
    weight=F(1,6 if word in ('0110','1001') else 12)
    pair=[]
    for t in (1,0):
        u=int(word[t+2])-int(word[t])
        pair += [F(int(i==u%5)+int(i==(u+1)%5),2)-F(1,5) for i in range(4)]
    for i in range(8):
        for j in range(8): K0[i][j]+=weight*pair[i]*pair[j]
Krylov=[K0]; columns=[flat(K0)]
for degree in range(1,21):
    nxt=product(product(T,Krylov[-1]),transpose(T))
    relation=linear_solve(columns,flat(nxt))
    if relation is not None: break
    Krylov.append(nxt);columns.append(flat(nxt))
else: raise AssertionError('no annihilator found within the audit bound')
# First exact relation p(A) K0 = 0. It propagates to all subsequent powers.
p=[-x for x in relation]+[F(1)]
assert sum(p)==0
q=[F(0)]*degree;q[-1]=p[-1]
for i in range(degree-2,-1,-1):q[i]=p[i+1]+q[i+1]
assert p[0]==-q[0]
q1=sum(q);assert q1!=0
Kstar=lincomb([x/q1 for x in q],Krylov)
assert product(product(T,Kstar),transpose(T))==Kstar
C0=product(product(E,[row[:4] for row in Kstar[:4]]),transpose(E))
C1=product(product(E,[row[4:] for row in Kstar[:4]]),transpose(E))
assert C0==transpose(C0) and C1==transpose(C1)
LC1=product(L,C1)
energy=sum((C0[i][i]-C1[i][i]+LC1[i][i]/2 for i in range(5)),F(0))
assert energy==F(701,2592)
print(json.dumps({
 'method':'exact rational Krylov Cesaro projector; same-agent cross-check',
 'annihilator_degree':degree,
 'annihilator_coefficients_low_to_high':[str(x) for x in p],
 'q_at_one':str(q1),
 'stationary_covariance':[[str(x) for x in row] for row in C0],
 'lag1_covariance':[[str(x) for x in row] for row in C1],
 'mean_energy':str(energy),
 'mean_site_variance':str(sum(C0[i][i] for i in range(5))/5),
 'stationarity_identity':True,
},sort_keys=True,indent=2))
