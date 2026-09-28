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

# Actual N2/event pipeline.
p=ROOT/'notes/C-HODGE-EVENT-CAUCHY-N/model.py'
spec=importlib.util.spec_from_file_location('evn3',p)
ev=importlib.util.module_from_spec(spec);spec.loader.exec_module(ev)
M=ev.Model();Q=M.Q

# Hypothetical N1 control in its own single Hodge-Q5 runtime.
with contextlib.redirect_stdout(io.StringIO()):
 H=runpy.run_path(str(ROOT/'probes/P-J-HODGE-HERM2-LOXODROME-1/verify.py'))
HQ=H['Q5']

def lincomb(coeffs):
 out=[Q(0)]*6
 for c,v in zip(coeffs,M.frame[1:]):
  out=[a+Q(c)*b for a,b in zip(out,v)]
 return out

def qframe(coeffs):
 v=lincomb(coeffs);return M.inner(v,v)

def qorig(v):
 Bp=H['Bp']
 vv=[HQ(x) for x in v]
 return sum((vv[i]*Bp[i][j]*vv[j] for i in range(3) for j in range(3)),HQ(0))

def main():
 a1,a2,a3=[M.inner(v,v) for v in M.frame[1:]]
 assert (a1,a2,a3)==(Q(0,F(2,5)),Q(0,F(6,5)),Q(0,F(3,2)))

 p10=(F(2,3),F(-1,3),F(-1,3))
 p01=(F(-1,3),F(2,3),F(-1,3))
 p11=(F(1,3),F(1,3),F(-2,3))
 qs=[qframe(v) for v in (p10,p01,p11)]
 assert qs==[Q(0,F(43,90)),Q(0,F(67,90)),Q(0,F(38,45))]
 assert qs[0]!=qs[1] and qs[0]!=qs[2] and qs[1]!=qs[2]

 qd=qframe((1,1,1))
 assert qd==Q(0,F(31,10))
 assert qframe((1,0,0))==a1 and qframe((0,1,0))==a2 and qframe((0,0,1))==a3
 assert len({str(a1),str(a2),str(a3)})==3

 # N1 hypothetical original-coordinate control, now in one HQ class.
 u=qorig(p10);d=qorig((1,1,1))
 assert u==HQ(0,F(2,15))
 assert d==HQ(0,F(3,2))
 assert d/u==HQ(F(45,4))

 b33=H['B'][3][3]
 assert b33==HQ(F(-1,4),F(-1,8))

 print('PASS G1: actual N2 site coordinates use orthogonal frame s1,s2,s3')
 print('PASS G2: cover-direction squares = sqrt5*(43,67,76)/90; pairwise distinct')
 print('PASS G3: tagged diagonal square = 31sqrt5/10')
 print('PASS G4: abstract hexagon symmetry is not an isometry of the actual N2 Hodge frame')
 print('PASS G5: rho=45/4 reproduced only in the hypothetical original-coordinate N1 control')
 print('PASS G6: typed flat frame = diag(2sqrt5/5,6sqrt5/5,3sqrt5/2,-(2+sqrt5)/8)')
 print('NON-CANONICAL CORRECTION: N1 is superseded for the actual N2 pipeline')

if __name__=='__main__':main()
