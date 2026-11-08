from contextlib import redirect_stdout
from io import StringIO
with redirect_stdout(StringIO()):
 import audit as t
s=t.s
from sympy.matrices.normalforms import hermite_normal_form,smith_normal_form
E=s.diag(t.BJ,t.BM)*t.C
bar=s.diag(t.bar5,t.bar8)
alpha=E[:,1];balpha=bar*alpha
v=E.inv()*balpha
print('integral product embedding determinant =',E.det())
print('bar alpha R-power coordinates =',list(v))
print('denominator lcm =',s.ilcm(*[s.denom(c) for c in v]))
print('123 bar alpha R-power coordinates =',list(123*v))
aug=hermite_normal_form(E.row_join(balpha))
print('R + Z bar alpha HNF =',aug.tolist())
print('R + Z bar alpha index in maximal product =',abs(aug.det()))
print('alpha bar alpha power coordinates =',list(E.inv()*s.diag(s.Matrix.hstack(*(t.coords(t.J*t.x**i,t.q5) for i in range(4))),s.Matrix.hstack(*(t.coords(t.M*t.x**i,t.q8) for i in range(4))))*balpha))
# Check the whole rational representation of the claimed three prime indices.
assert abs(E.det())==123
assert aug==s.eye(8)
assert s.ilcm(*[s.denom(c) for c in v])==123
# Sylvester determinant, independent of resultant() and of the reduction map.
f=t.s.Poly(t.f,t.x);g=t.s.Poly(t.g,t.x)
S=s.Matrix.hstack(*(t.coords(t.x**i*t.f,t.x**8) for i in range(4)),*(t.coords(t.x**i*t.g,t.x**8) for i in range(4)))
print('independent Sylvester determinant =',S.det())
# all common quotient roots, and primitive roots in the cyclotomic residue.
p=41
print('J residue',19,'barJ residue',17,'M residue',19,'barM residue',7)
print('common norm residues J,M =',19*17%41,19*7%41)
print('19 powers at exponents 8,20,40 =',[pow(19,n,41) for n in (8,20,40)])
print('16 split primes in compositum: roots Phi40 mod41 =',[a for a in range(p) if s.cyclotomic_poly(40,t.x).subs(t.x,a)%p==0])
# At 41 the two separate coordinate projectors are unavailable in R.
for e in (s.Matrix([1,0,0,0,0,0,0,0]),s.Matrix([0,0,0,0,1,0,0,0])):
 v=t.C.inv()*e
 print('separate idempotent power coordinates =',list(v))
# Star stable intersection has index [O:R]^2 since R+bar(R)=O.
print('index star-stable intersection in maximal product =',123**2)
# Two conditions after standard conjugation on the maximal factor product.
print('seam primes (j,m) =',(10,27),'conjugate =',(pow(10,-1,41),pow(27,-1,41)))
