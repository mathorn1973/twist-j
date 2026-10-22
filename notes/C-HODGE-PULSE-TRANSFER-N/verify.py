#!/usr/bin/env python3
"""Result-exposed, exact local algebra audit; NOT a public TWIST-J gate."""
from itertools import product
import sympy as S

r = S.sqrt(5)
phi = (1+r)/2
c, s = 1/r, 2/r
I2 = S.eye(2)
Z = S.diag(1,-1)
X = S.Matrix([[0,1],[1,0]])
Q = S.Matrix([[c,-s],[s,c]])
T = S.Matrix([[1,-c],[c,-1]])/s
B = S.Matrix([[1,-c],[-c,1]])/s

def eq(a,b):
    d=a-b
    if isinstance(d,S.MatrixBase):
        assert all(S.simplify(x)==0 for x in d), d
    else:
        assert S.simplify(d)==0, d

ain,bin = S.symbols('a b')
aout,bout = Q*S.Matrix([ain,bin])
eq(Q.T*Q,I2)
eq(T*S.Matrix([ain,aout]),S.Matrix([bout,bin]))
print('01 pulse unitarity and frozen boundary regrouping: PASS')
eq(T.det(),-1)
eq(T*T,I2)
eq(T.T*Z*T,Z)
print('02 full boundary transfer is flux-preserving and involutory: PASS')
eq(T,Z*B)
eq(T.T*T,B*B)
eq(B.det(),1)
eq(B*S.Matrix([1,-1]),phi*S.Matrix([1,-1]))
eq(B*S.Matrix([1,1]),(phi-1)*S.Matrix([1,1]))
assert phi.is_positive and (phi-1).is_positive
print('03 positive polar factor eigenvalues: phi, phi^-1')

t,x,y,z=S.symbols('t x y z',real=True)
H=S.Matrix([[t+z,x-S.I*y],[x+S.I*y,t-z]])
coords=(t,x,y,z)
def herm_action(A):
    Y=S.simplify(A*H*A.conjugate().T)
    out=S.Matrix([(Y[0,0]+Y[1,1])/2,(Y[0,1]+Y[1,0])/2,
                  (Y[1,0]-Y[0,1])/(2*S.I),(Y[0,0]-Y[1,1])/2])
    return S.simplify(out.jacobian(coords))
L=herm_action(B)
Lt=herm_action(T)
expected=S.Matrix([[S.Rational(3,2),-r/2,0,0],[-r/2,S.Rational(3,2),0,0],
                   [0,0,1,0],[0,0,0,1]])
eq(L,expected)
eta=S.diag(1,-1,-1,-1)
eq(L.T*eta*L,eta)
v=S.symbols('v')
eq(L.charpoly(v).as_expr(),(v*v-3*v+1)*(v-1)**2)
eq(H.det(),t*t-x*x-y*y-z*z)
print('04 Hermitian polar action: (v^2-3v+1)(v-1)^2; signature 1,3')
eq(Lt*Lt,S.eye(4))
assert S.simplify(Lt.charpoly(v).as_expr()-(v*v-3*v+1)*(v*v-phi*v+1))!=0
print('05 full transfer is NOT the Hodge loxodrome: PASS')
cc,ss=S.Rational(3,5),S.Rational(4,5)
Bc=S.Matrix([[1,-cc],[-cc,1]])/ss
eq(Bc*S.Matrix([1,-1]),2*S.Matrix([1,-1]))
eq(Bc*S.Matrix([1,1]),S.Rational(1,2)*S.Matrix([1,1]))
Lc=herm_action(Bc)
eq(Lc.charpoly(v).as_expr(),(v*v-S.Rational(17,4)*v+1)*(v-1)**2)
print('06 capture contact has polar eigenvalues 2,1/2, not phi,phi^-1')
Balt=S.Matrix([[1,-s],[-s,1]])/c
eq(Balt*S.Matrix([1,-1]),phi**3*S.Matrix([1,-1]))
eq(Balt*S.Matrix([1,1]),phi**-3*S.Matrix([1,1]))
print('07 alternative port grouping yields phi^3,phi^-3: nonuniqueness retained')

def mod(A):
    return A.applyfunc(lambda a: int(a)%5)

def reduce_f(a):
    a=S.expand(a)
    a0,a1=a.coeff(r,0),a.coeff(r,1)
    assert S.simplify(a-a0-r*a1)==0
    a0=S.Rational(a0)
    assert a0.q%5
    return (int(a0.p)*pow(int(a0.q),-1,5))%5

Bb=B.applyfunc(reduce_f)
eq(Bb,S.Matrix([[0,2],[2,0]]))
eq(mod(Bb*Bb),4*I2)
assert int(Bb.det())%5==1
hh=S.diag(1,-1); ee=S.Matrix([[0,1],[0,0]]); ff=ee.T
sl_basis=(hh,ee,ff)
def sl_coords(A):
    return mod(S.Matrix([A[0,0],A[0,1],A[1,0]]))
Ad=S.Matrix.hstack(*[sl_coords(Bb*a*Bb.inv_mod(5)) for a in sl_basis])
eq(mod(Ad*Ad),S.eye(3))
def rankmod(A):
    A=[list(map(lambda x:int(x)%5,row)) for row in A.tolist()]
    n=len(A);m=len(A[0]);row=0
    for col in range(m):
        p=next((i for i in range(row,n) if A[i][col]),None)
        if p is None: continue
        A[row],A[p]=A[p],A[row]
        inv=pow(A[row][col],-1,5)
        A[row]=[(a*inv)%5 for a in A[row]]
        for i in range(n):
            if i!=row:
                q=A[i][col]
                A[i]=[(a-q*b)%5 for a,b in zip(A[i],A[row])]
        row+=1
        if row==n:break
    return row
assert 3-rankmod(Ad-S.eye(3))==1
assert 3-rankmod(Ad+S.eye(3))==2
print('08 reduction at sqrt5: Bbar=2X; adjoint splits 1+2')
# Public marked W5 chart: h,e,f from P-TRACEKERNEL-EXTERIOR-CLOSURE-1.
Gh=S.Matrix([[2,4,0],[4,2,4],[0,4,2]])
h=S.Matrix([1,0,1]);e=S.Matrix([1,4,3]);f=S.Matrix([3,4,1])
M=S.Matrix.hstack(h,e,f)
def bracket(a,b):
    return mod(Gh.inv_mod(5)*a.cross(b))
eq(bracket(h,e),mod(2*e))
eq(bracket(h,f),mod(-2*f))
eq(bracket(e,f),h)
Phi=mod(M*S.diag(1,4,4)*M.inv_mod(5))
eq(Phi,S.Matrix([[0,4,1],[0,4,0],[1,4,0]]))
P=S.Matrix([[1,1],[1,-1]])
eq(mod(P.inv_mod(5)*Bb*P),S.diag(2,3))
def psi(w):
    h_,e_,f_=mod(M.inv_mod(5)*w)
    return mod(P*(h_*hh+e_*ee+f_*ff)*P.inv_mod(5))
for w in S.eye(3).columnspace():
    eq(mod(Bb*psi(w)*Bb.inv_mod(5)),psi(Phi*w))
print('09 explicit W5/sl2 conjugacy gives the published Phi grading, NOT D')
print('ALL 9 EXACT CHECK GROUPS PASS')
print('NON-CANONICAL; one local lane; no physical or canonical bridge asserted')
