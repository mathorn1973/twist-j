from __future__ import annotations
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
x=s.Symbol('x')
f=x**4-3*x**3+4*x**2-2*x+1
h=x**8-7*x**7+24*x**6-46*x**5+54*x**4-39*x**3+20*x**2-6*x+1
g,rem=s.div(h,f); assert rem==0
print('f =',f);print('g =',g);print('h =',h)
def coords(p,q):
 n=s.degree(q,x); r=s.Poly(s.rem(p,q,x),x)
 return s.Matrix([r.nth(i) for i in range(n)])
def cp(q):
 n=s.degree(q,x)
 return s.Matrix.hstack(*(coords(x**(i+1),q) for i in range(n)))
F,G,H=cp(f),cp(g),cp(h)
D=s.diag(F,G)
C=s.Matrix.hstack(*(coords(x**i,f).col_join(coords(x**i,g)) for i in range(8)))
assert D*C==C*H
print('C =',C.tolist())
print('det C =',C.det())
print('SNF C =', [abs(int(t)) for t in smith_normal_form(C,domain=s.ZZ).diagonal()])
print('resultant =',s.resultant(f,g,x))
print('disc f,g,h =',*[s.discriminant(q,x) for q in (f,g,h)])
print('trace determinant D =',s.trace(D),D.det())
period={}
for n in range(1,5):
 a=abs((F**n-s.eye(4)).det());b=abs((G**n-s.eye(4)).det());v=abs((H**n-s.eye(8)).det())
 assert v==a*b
 period[n]=v-sum(period[d] for d in s.divisors(n) if d<n)
 print('period',n,'fixedJ',a,'fixedM',b,'fixedProduct',v,'leastPeriodPoints',period[n],'orbits',period[n]//n)
print('mod41 gcd =',s.Poly(s.gcd(s.Poly(f,x,modulus=41),s.Poly(g,x,modulus=41)),x,modulus=41))
roots_f=[i for i in range(41) if f.subs(x,i)%41==0]
roots_g=[i for i in range(41) if g.subs(x,i)%41==0]
r=next(iter(set(roots_f)&set(roots_g)))
print('mod41 roots f,g,common =',roots_f,roots_g,r)
print('order common =',s.n_order(r,41))
a,b,c=s.gcdex(f,g,x)
print('Bezout 41 coefficients =',s.expand(41*a),s.expand(41*b),s.expand(41*c))
q5=x**4+x**3+x**2+x+1;q8=x**4+1
J=1+x*x;M=1+x+x*x
BJ=s.Matrix.hstack(*(coords(J**i,q5) for i in range(4)))
BM=s.Matrix.hstack(*(coords(M**i,q8) for i in range(4)))
assert s.rem(f.subs(x,J),q5,x)==0
assert s.rem(g.subs(x,M),q8,x)==0
print('J power basis =',BJ.tolist(),'det',BJ.det())
print('M power basis =',BM.tolist(),'det',BM.det())
print('M index =',abs(BM.det()),'SNF',list(smith_normal_form(BM,domain=s.ZZ).diagonal()))
print('maximal product index =',abs(C.det()*BJ.det()*BM.det()))
print('m from M =',list(BM.inv()*coords(x,q8)))
# Conjugation in power bases. x^-1 is expressed by the cyclotomic relation.
bar5=s.Matrix.hstack(*(coords(x**((-i)%5),q5) for i in range(4)))
bar8=s.Matrix.hstack(*(coords(x**((-i)%8),q8) for i in range(4)))
cbJ=BJ.inv()*bar5*BJ;cbM=BM.inv()*bar8*BM
print('conjugation on A =',cbJ.tolist())
print('conjugation on B =',cbM.tolist())
print('barJ power coords =',list(cbJ[:,1]))
print('barM power coords =',list(cbM[:,1]))
red=lambda v: sum(int(s.numer(v[i]))*pow(int(s.denom(v[i])),-1,41)*pow(r,i,41) for i in range(4))%41
print('conjugate generator residues =',red(cbJ[:,1]),red(cbM[:,1]))
print('j residue =',pow(r-1,3,41))
# Evaluation of m uses inverse of 3 modulo 41.
v=BM.inv()*coords(x,q8)
def modrat(v,p):
 return int(s.numer(v)) * pow(int(s.denom(v)),-1,p)%p
mres=sum(modrat(v[i],41)*pow(r,i,41) for i in range(4))%41
print('m residue =',mres)
print('conjugation roots check =',(1+pow(pow(r-1,3,41),-2,41))%41,(1+pow(mres,-1,41)+pow(mres,-2,41))%41)
# minimal polynomial ranks over F_p via explicit exact elimination

def rankmod(A,p):
 z=[[int(t)%p for t in row] for row in A.tolist()];m=len(z);n=len(z[0]);i=0
 for j in range(n):
  pivot=next((k for k in range(i,m) if z[k][j]),None)
  if pivot is None:continue
  z[i],z[pivot]=z[pivot],z[i];iv=pow(z[i][j],-1,p);z[i]=[t*iv%p for t in z[i]]
  for k in range(m):
   if k!=i:
    t=z[k][j];z[k]=[(z[k][l]-t*z[i][l])%p for l in range(n)]
  i+=1
  if i==m:break
 return i
for n in (1,20,40,41,1640):
 print('mod41 fixed dimensions',n, 'glued',8-rankmod(H**n-s.eye(8),41),'split',8-rankmod(D**n-s.eye(8),41))
print('rank C mod41 =',rankmod(C,41))
# periodic integer point group: all Smith invariants, truncated to nontrivial ones
for n in (1,2,3,4,20):
 out=[]
 for T in (D,H):
  sn=smith_normal_form(T**n-s.eye(8),domain=s.ZZ)
  out.append([abs(int(t)) for t in sn.diagonal() if abs(t)!=1])
 print('fixed group SNF',n,'split',out[0],'glued',out[1])
print('resultant controls M orientation =',s.resultant(f,g.subs(x,-x),x))
