#!/usr/bin/env python3
"""Exact field-subset classification for MatterData_QDD."""
from fractions import Fraction as F
from itertools import combinations, product

BASIS=tuple(tuple(F(int(i==j)) for i in range(4)) for j in range(4)); POW=BASIS+((F(-1),)*4,)
ZERO=(F(0),)*4; LAMBDA=(F(1),)*4; L=(-2,-1,0,1,2)
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def scale(c,a): return tuple(c*x for x in a)
def mul(a,b):
    o=[F(0)]*4
    for i,x in enumerate(a):
      for j,y in enumerate(b):
       if x and y:
        p=POW[(i+j)%5]
        for k in range(4): o[k]+=x*y*p[k]
    return tuple(o)
def conj(a):
    o=[F(0)]*4
    for i,x in enumerate(a):
      p=POW[(-i)%5]
      for k in range(4): o[k]+=x*p[k]
    return tuple(o)
def tr(a):
    c=[mul(a,e) for e in BASIS]; return sum(c[j][j] for j in range(4))
def pair(a,b): return tr(mul(a,conj(b)))/5
LN=pair(LAMBDA,LAMBDA)
def matrix_T(w):
    cols=[scale(pair(BASIS[j],w),w) for j in range(4)]
    return tuple(tuple(cols[j][i] for j in range(4)) for i in range(4))
def mscale(c,a): return tuple(tuple(c*x for x in row) for row in a)
def record(v):
    v=tuple(F(x) for x in v)
    if v==ZERO: return ("ZERO_SUPPORT",F(0),(F(0),F(0)),"ZERO_DENOMINATOR","ZERO_DENOMINATOR")
    m=pair(v,v); c=pair(v,LAMBDA)/LN; lo=scale(c,LAMBDA); hi=sub(v,lo)
    wl=pair(lo,lo); wh=pair(hi,hi); rho=mscale(1/m,matrix_T(v))
    return ("SUPPORTED",m,(wl,wh),("DENSITY",rho),("NORMALIZED",(wl/m,wh/m)))

FIELDS=("S","M","B","R","N")
records=[record(v) for v in product(L,repeat=4)]
full_count=len(set(records)); assert full_count==313
complete=[]
for mask in range(32):
    idx=tuple(i for i in range(5) if mask>>i&1)
    vals={tuple(r[i] for i in idx) for r in records}
    if len(vals)==full_count: complete.append(tuple(FIELDS[i] for i in idx))
expected=[]
for mask in range(32):
    s={FIELDS[i] for i in range(5) if mask>>i&1}
    if "R" in s and ("M" in s or "B" in s): expected.append(tuple(FIELDS[i] for i in range(5) if mask>>i&1))
assert complete==expected and len(complete)==12
minimal=[s for s in complete if not any(set(t)<set(s) for t in complete)]
assert minimal==[("M","R"),("B","R")]

v=(1,0,0,1); w=(1,1,0,0); rv=record(v); rw=record(w)
assert tuple(rv[i] for i in (0,1,2,4))==tuple(rw[i] for i in (0,1,2,4)) and rv[3]!=rw[3]
a=(1,0,0,0); b=(2,0,0,0); ra=record(a); rb=record(b)
assert tuple(ra[i] for i in (0,3,4))==tuple(rb[i] for i in (0,3,4)) and ra[1]!=rb[1]

print("C-QDD-MATTERDATA-MINIMAL-SCHEMA-1-N")
print("STATUS NON-CANONICAL INCUBATION")
print(f"S1 COMPLETE_SUBSETS {len(complete)} PASS")
print("S2 RULE contains_R_and_(M_or_B) PASS")
print("S3 MINIMAL {M,R} {B,R} PASS")
print("S4 SUFFICIENCY M+R_reconstructs_Q; B+R_recovers_M_then_Q PASS")
print("S5 NECESSITY no_R_wedge_witness=PASS R_without_scale_e0_2e0=PASS")
print("S6 REDUNDANCY support_and_normalized_never_required PASS")
print("COMPLETE " + " ".join("{"+",".join(s)+"}" for s in complete))
print("GUARD equality classification only; no schema deletion or Born/measure/decoder-completion claim")
print("RESULT candidate-T")
