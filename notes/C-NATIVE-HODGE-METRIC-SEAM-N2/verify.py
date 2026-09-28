#!/usr/bin/env python3
from fractions import Fraction as F
from pathlib import Path
import contextlib,hashlib,importlib.util,io,runpy

ROOT=Path(__file__).resolve().parents[2]
HASHES={
'notes/C-OMEGA-GENERATIVE-GEOMETRY-N2/PROOF.md':'a6be9bd44df63655e2a42ec88c9f4cbb853b9ba15f5f5a869ec89e1ca5775c60',
'notes/C-HODGE-EVENT-CAUCHY-N/PROOF.md':'6ebac7c63bcadba55791db017d273aa2136cdbf8867a72b3006c1d46bae823af',
'notes/C-HODGE-EVENT-CAUCHY-N/model.py':'adc99adac6ff1e3d9e76d4952b97af16fcdbe919021c5947bdb6c0feb7b3a772',
'probes/P-J-HODGE-HERM2-LOXODROME-1/verify.py':'02f33f1de4174ee4d4aeb45202d838897e68c3bd205df23f9b208cc669f489d9',
'notes/C-NATIVE-HODGE-METRIC-SEAM-N/RESULT.md':'d346d41fcff7a9ba62434e55242475fc05926ef3ab62746c838bc4324e4b571e',
}
for f,h in HASHES.items():
 p=ROOT/f
 if hashlib.sha256(p.read_bytes()).hexdigest()!=h: raise RuntimeError('STOP hash '+f)

p=ROOT/'notes/C-HODGE-EVENT-CAUCHY-N/model.py'
spec=importlib.util.spec_from_file_location('ev',p);ev=importlib.util.module_from_spec(spec);spec.loader.exec_module(ev)
M=ev.Model();Q=M.Q
with contextlib.redirect_stdout(io.StringIO()):
 H=runpy.run_path(str(ROOT/'probes/P-J-HODGE-HERM2-LOXODROME-1/verify.py'))

def lincomb(coeffs):
 out=[Q(0)]*6
 for c,v in zip(coeffs,M.frame[1:]):
  out=[a+Q(c)*b for a,b in zip(out,v)]
 return out

def q(coeffs):
 v=lincomb(coeffs);return M.inner(v,v)

def main():
 a1,a2,a3=[M.inner(v,v) for v in M.frame[1:]]
 assert (a1,a2,a3)==(Q(0,F(2,5)),Q(0,F(6,5)),Q(0,F(3,2)))
 p10=(F(2,3),F(-1,3),F(-1,3))
 p01=(F(-1,3),F(2,3),F(-1,3))
 p11=(F(1,3),F(1,3),F(-2,3))
 qs=[q(v) for v in (p10,p01,p11)]
 assert qs==[Q(0,F(43,90)),Q(0,F(67,90)),Q(0,F(38,45))]
 assert len(set(map(str,qs)))==3
 qd=q((1,1,1));assert qd==Q(0,F(31,10))
 # Explicit permutation failure in the actual frame metric.
 assert q((1,0,0))!=q((0,1,0))!=q((0,0,1))
 # Predecessor hypothetical control in ORIGINAL E coordinates.
 Bp=H['Bp']
 def qorig(v):
  return sum((Q(v[i])*Bp[i][j]*Q(v[j]) for i in range(3) for j in range(3)),Q(0))
 u=qorig(p10);d=qorig((1,1,1))
 assert u==Q(0,F(2,15)) and d==Q(0,F(3,2)) and d/u==Q(F(45,4))
 assert H['B'][3][3]==Q(F(-1,4),F(-1,8))
 print('PASS G1: N2 sites are coefficients of the orthogonal s1,s2,s3 Hodge frame')
 print('PASS G2: cover-direction squares = sqrt5*(43,67,76)/90; all distinct')
 print('PASS G3: tagged diagonal square = 31sqrt5/10; cover hexagon symmetry is not a Hodge-frame isometry')
 print('PASS G4: rho=45/4 reproduced only in the predecessor hypothetical original-coordinate identification')
 print('PASS G5: correctly typed flat frame = diag(2sqrt5/5,6sqrt5/5,3sqrt5/2,-(2+sqrt5)/8)')
 print('NON-CANONICAL CORRECTION: #1252 is superseded for the actual N2 pipeline')

if __name__=='__main__':main()
