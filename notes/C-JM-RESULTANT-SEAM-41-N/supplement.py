from contextlib import redirect_stdout
from io import StringIO
with redirect_stdout(StringIO()):
 import audit as t
s=t.s;x=t.x
from sympy.matrices.normalforms import hermite_normal_form
L40=s.cyclotomic_poly(40,x);difference=x**16-x**5-x**10
print('Phi40 =',L40)
print('N_K40(J-M) =',s.resultant(L40,difference,x))
common=[a for a in range(41) if L40.subs(x,a)%41==0 and difference.subs(x,a)%41==0]
print('common roots Phi40 and J-M mod41 =',common)
assert common==[6]
assert s.resultant(L40,difference,x)==41
print('faithful residue root orders =',s.n_order(10,41),s.n_order(27,41))
# The indexed extension has a column-coupling k e0 e3^T.
B1=t.D.copy();B1[0,7]=1
V=s.Matrix.hstack(*(t.coords(t.g*x**i,t.h) for i in range(4)),*(t.coords(x**i,t.h) for i in range(4)))
print('E1 to R power-basis determinant =',V.det())
assert V.det() in (-1,1)
assert t.H*V==V*B1
print('E1 companion equivalence = PASS')
print('Ext representative residue orbit =',[pow(19,n,41) for n in range(40)])
assert len({pow(19,n,41) for n in range(40)})==40
# Short modular binary powering, independent from the large integer powers.
def mpow(A,n,p):
 A=A.applyfunc(lambda v:int(v)%p);B=s.eye(A.rows)
 while n:
  if n&1:B=(B*A).applyfunc(lambda v:int(v)%p)
  A=(A*A).applyfunc(lambda v:int(v)%p);n//=2
 return B
for name,T,o in [('split',t.D,40),('glued',t.H,1640)]:
 assert mpow(T,o,41)==s.eye(8)
 for p in s.primefactors(o):assert mpow(T,o//p,41)!=s.eye(8)
 print('mod41 exact order',name,o)
# 41 annihilates the whole reduction-inclusion cokernel.
assert all(q.is_Integer for q in 41*t.C.inv())
assert t.C.inv()!=t.C.inv().applyfunc(lambda q:s.floor(q))
print('reduction inclusion cokernel exponent = 41')
print('new physical claims = NONE')
