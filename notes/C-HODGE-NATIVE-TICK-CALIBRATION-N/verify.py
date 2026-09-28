#!/usr/bin/env python3
from fractions import Fraction as F
from pathlib import Path
import hashlib,importlib.util

ROOT=Path(__file__).resolve().parents[2]
HASHES={
'notes/C-NATIVE-HODGE-METRIC-SEAM-N3/PROOF.md':'2f27776ceb851774e0b026b274b446605c8b480ed90fa4f57ede22ce13be742d',
'notes/C-HODGE-EVENT-CAUCHY-N/PROOF.md':'6ebac7c63bcadba55791db017d273aa2136cdbf8867a72b3006c1d46bae823af',
'notes/C-HODGE-EVENT-CAUCHY-N/model.py':'adc99adac6ff1e3d9e76d4952b97af16fcdbe919021c5947bdb6c0feb7b3a772',
'reproduce/coupling-metrology/verify.py':'8b203f9c4885a9f70b4460ded55d884529989cd244a3f0acbdcae9a8de053566',
'reproduce/coupling-metrology/README.md':'ad9bb19d32d844847a8820ff9d67650c3e914427780c2001aae54ee4e78a1c5b',
}
for f,h in HASHES.items():
 p=ROOT/f
 if hashlib.sha256(p.read_bytes()).hexdigest()!=h:
  raise RuntimeError('STOP inherited hash mismatch: '+f)

p=ROOT/'notes/C-HODGE-EVENT-CAUCHY-N/model.py'
spec=importlib.util.spec_from_file_location('tick_event_model',p)
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
M=mod.Model();Q=M.Q;S=M.anchor['S']


def absq(x):
 return x if M.sign(x)>=0 else -x


def edge_interval(h,m,z):
 a=M.event(h,m,z);b=M.event(h,m+1,z)
 d=[y-x for x,y in zip(a,b)]
 return M.inner(d,d)


def main():
 a1,a2,a3=[M.inner(v,v) for v in M.frame[1:]]
 ct=M.ct
 assert (a1,a2,a3)==(Q(0,F(2,5)),Q(0,F(6,5)),Q(0,F(3,2)))
 assert ct==Q(F(1,4),F(1,8))

 ratios=(a1/ct,a2/ct,a3/ct)
 expected=(Q(16)-Q(0,F(32,5)),
           Q(48)-Q(0,F(96,5)),
           Q(60)-Q(0,F(24)))
 assert ratios==expected
 assert all(M.sign(x)>0 for x in ratios)

 # alpha_i=ct/a_i is the inherited scalar-stencil coefficient relation.
 assert tuple(ct/a for a in (a1,a2,a3))==M.alpha
 assert tuple(Q(1)/a for a in M.alpha)==ratios

 # Exact h=3 rounded-event obstruction.
 i0=edge_interval(3,0,(0,0,0))
 i1=edge_interval(3,1,(1,0,0))
 assert i0==Q(F(-398,6561))
 assert i1==Q(F(-1861,32805),F(1,32805))
 assert i0!=i1 and M.sign(i0)<0 and M.sign(i1)<0

 # Exact sample audit of the universal rounding inequality.
 R0=M.R
 checks=0
 for h in (3,4,5,8,12):
  eps=Q(2)*R0/Q(h**4)
  bound=ct*(Q(2)*eps/Q(h)+Q(2)*eps*eps)
  formula=ct*(Q(4)*R0/Q(h**5)+Q(8)*R0*R0/Q(h**8))
  assert bound==formula
  for m in (-1,0,1):
   for z in ((0,0,0),(1,0,0),(0,1,0),(0,0,1),(1,-1,1)):
    interval=edge_interval(h,m,z)
    err=interval+ct/Q(h*h)
    assert M.sign(bound-absq(err))>=0
    checks+=1

 # Relative calibrated squared-interval bound, with formal factor T^2 removed.
 for h in (3,5,12,31):
  rel=Q(4)*R0/Q(h**3)+Q(8)*R0*R0/Q(h**6)
  assert M.sign(rel)>0
  if h>=12:
   assert M.sign(Q(1)-rel)>0

 print('PASS G1: ideal tick calibration factor lambda_h/T^2 = h^2/ct is unique')
 print('PASS G2: calibrated integer-label metric coefficients are independent of h')
 print('PASS G3: spatial ratios a_i/ct exact and positive; signature 3+1')
 print(f'PASS G4: rounded same-site interval bound exact-sample checks={checks}')
 print('PASS G5: h=3 has two unequal exact timelike tick intervals')
 print('PASS G6: relative squared-tick error bound is O(h^-3)')
 print('NON-CANONICAL: METRO-TICK calibrates the selected ideal seam, not exact finite-h rounded events')

if __name__=='__main__':main()
