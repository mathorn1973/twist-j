"""Result-exposed alternate matrix audit of issue #2102; not a blind reviewer."""
from itertools import combinations, product
from sympy import Matrix, eye, zeros
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

B = [list(combinations(range(4), k)) for k in range(5)]
C = {}
for k in range(4):
    for i in range(4):
        A = zeros(len(B[k+1]), len(B[k]))
        for t, J in enumerate(B[k]):
            if i not in J:
                I = tuple(sorted((i,)+J))
                A[B[k+1].index(I), t] = (-1)**sum(x<i for x in J)
        C[k,i] = A

def snf(A):
    S = smith_normal_form(A, domain=ZZ)
    return tuple(abs(S[i,i]) for i in range(min(S.shape)) if S[i,i])

G = 5*eye(4)-Matrix.ones(4,4)
assert snf(G)==(1,5,5,5)
for name,H,pred in [('SELF',G,(1,1,1,5)),('DUAL',eye(4),(1,1,1,1))]:
    a = {(k,i):sum((H[i,j]*C[k-1,j].T for j in range(4)),zeros(len(B[k-1]),len(B[k]))) for k in (2,3) for i in range(4)}
    A = Matrix.vstack(*(Matrix.hstack(*(a[3,i]*C[2,j] for j in range(4))) for i in range(4)))
    D = Matrix.vstack(*(Matrix.hstack(*(C[1,j]*a[2,i] for i in range(4))) for j in range(4)))
    for i,j in product(range(4),repeat=2):
        assert A[6*i:6*i+6,6*j:6*j+6]+D[6*j:6*j+6,6*i:6*i+6] == H[i,j]*eye(6)
    assert snf(A)==snf(D)==pred
    print(name, 'all-block identity; Smith', pred)
R=Matrix([[1,1,1,1],[1,0,0,-1],[0,1,0,-1],[0,0,1,-1]])
assert abs(R.det())==4
for x in product(range(5),repeat=4):
    v=Matrix(x); z=G*v
    y=Matrix([(-z[0])%5]+[((z[i]-z[3])//5)%5 for i in range(3)])
    assert all((u-w)%5==0 for u,w in zip(R*v,y))
assert len({tuple(int(t)%5 for t in R*Matrix(x)) for x in product(range(5),repeat=4)})==625
print('READER det_abs=4 bijection=625')
from sympy import symbols, rem, invert
j=symbols('j'); P=j**4+j**3+j**2+j+1
red=lambda f: rem(f,P,j).expand()
vec=lambda f: Matrix([red(f).coeff(j,i) for i in range(4)])
sigma=lambda f: red(f.subs(j,j**2))
J=1+j**2
inv=invert(1-j,P,j)
D=Matrix.hstack(*(vec(inv*(sigma(j**k)-j**k)) for k in range(4)))
assert all(x.q==1 for x in D)
M=Matrix.hstack(*(vec(J*j**k) for k in range(4)))
K=M*D-D*M
u=j**2+j**3
assert K==Matrix.hstack(*(vec(u*sigma(j**k)) for k in range(4)))
assert K*K==Matrix.hstack(*(vec(-j**(4*k)) for k in range(4))) and K**4==eye(4)
Kv=Matrix.hstack(*(vec(-(j+j**4)*sigma(j**k)) for k in range(4)))
assert K.T*G*Kv==G and K.det() in (-1,1)
print('COMMUTATOR polynomial quotient: K^2=-conjugation; dual covariance')
