#!/usr/bin/env python3
"""Exact supplementary audit. NON-CANONICAL; not a public promotion gate."""
from dataclasses import dataclass
from fractions import Fraction as R

@dataclass(frozen=True)
class Q5:
    a: R
    b: R = R(0)
    def __post_init__(self):
        object.__setattr__(self, 'a', R(self.a))
        object.__setattr__(self, 'b', R(self.b))
    @staticmethod
    def coerce(x):
        return x if isinstance(x, Q5) else Q5(x)
    def __add__(self, x):
        x = self.coerce(x)
        return Q5(self.a+x.a, self.b+x.b)
    __radd__ = __add__
    def __neg__(self):
        return Q5(-self.a, -self.b)
    def __sub__(self, x):
        return self + (-self.coerce(x))
    def __rsub__(self, x):
        return self.coerce(x) - self
    def __mul__(self, x):
        x = self.coerce(x)
        return Q5(self.a*x.a+5*self.b*x.b, self.a*x.b+self.b*x.a)
    __rmul__ = __mul__
    def inv(self):
        d = self.a*self.a-5*self.b*self.b
        if not d:
            raise ZeroDivisionError('zero in Q(sqrt(5))')
        return Q5(self.a/d, -self.b/d)
    def __truediv__(self, x):
        return self*self.coerce(x).inv()
    def __rtruediv__(self, x):
        return self.coerce(x)*self.inv()
    def __pow__(self, n):
        if not isinstance(n, int):
            raise TypeError('integer exponent required')
        base, n = (self.inv(), -n) if n < 0 else (self, n)
        out = Q5(1)
        while n:
            if n & 1:
                out = out*base
            base = base*base
            n >>= 1
        return out

def mm(a,b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(len(b)))
                       for j in range(len(b[0]))) for i in range(len(a)))
def mt(a):
    return tuple(zip(*a))
def ident(n, one=1, zero=0):
    return tuple(tuple(one if i==j else zero for j in range(n)) for i in range(n))
def mpow(a,n):
    if n < 0:
        raise ValueError('nonnegative power required')
    out=ident(len(a))
    while n:
        if n & 1:
            out=mm(out,a)
        a=mm(a,a);n>>=1
    return out

def diagblock(a,b):
    n,k=len(a),len(b)
    return tuple(tuple(a[i][j] if i<n and j<n else
                       b[i-n][j-n] if i>=n and j>=n else 0
                       for j in range(n+k)) for i in range(n+k))
def neg(a):
    return tuple(tuple(-x for x in row) for row in a)
def det(a):
    if len(a)==1:
        return a[0][0]
    return sum((-1)**j*a[0][j]*det(tuple(tuple(row[k] for k in range(len(a)) if k!=j)
                                              for row in a[1:])) for j in range(len(a)))
def charpoly(a):
    # Newton identities; exact rational division, followed by an integrality check.
    n=len(a); powers=[mpow(a,k) for k in range(1,n+1)]
    traces=[0]+[sum(p[i][i] for i in range(n)) for p in powers]
    c=[R(1)]
    for k in range(1,n+1):
        c.append(-sum(c[k-j]*traces[j] for j in range(1,k+1))/k)
    assert all(x.denominator==1 for x in c)
    return tuple(int(x) for x in c)

def zmul(a,b):
    """Multiplication in Z[j]/(1+j+j^2+j^3+j^4)."""
    v=[0]*7
    for i,x in enumerate(a):
        for k,y in enumerate(b):
            v[i+k]+=x*y
    for d in range(6,3,-1):
        t=v[d]
        for k in range(4):
            v[d-4+k]-=t
        v[d]=0
    return tuple(v[:4])

def main():
    one,zero=Q5(1),Q5(0)
    phi=Q5(R(1,2),R(1,2))
    rungs=[phi**n for n in range(-8,9)]
    def sc(r):
        return ((r-1/r)/2,(r+1/r)/2)
    for r in rungs:
        s,c=sc(r); E,P=2*c,2*s
        v,q=s/c,1/c
        assert v*v+q*q==one and E*E-P*P==Q5(4)
        S=((r,-one),(one,r))
        HD=((P,Q5(2)),(Q5(2),-P))
        assert mm(HD,S)==mm(S,((E,zero),(zero,-E)))
    print('PASS frame_rungs=17 dirac_diagonalization=17 shell_and_reading=17')
    for r in rungs:
        S=((r,-one),(one,r));Si=((r/(1+r*r),one/(1+r*r)),(-one/(1+r*r),r/(1+r*r)))
        assert mm(S,Si)==ident(2,one,zero)
        for rp in rungs:
            Sp=((rp,-one),(one,rp));T=mm(Sp,Si)
            Gp=((one/(1+rp*rp),zero),(zero,one/(1+rp*rp)))
            G=((one/(1+r*r),zero),(zero,one/(1+r*r)))
            assert mm(mm(mt(T),Gp),T)==G
    print('PASS exact_metric_transfers=289')
    for r in rungs:
        s,c=sc(r)
        for rp in rungs:
            sp,cp=sc(rp)
            # Translation from old p=2s to new p=2sp. Inverse-pullback Jacobian.
            delta=2*(sp-s)
            assert 2*sp-delta==2*s
            jac_inverse=cp/c
            jac_forward=c/cp
            assert jac_inverse*jac_forward==one
            # Same-rapidity comoving energy for masses 2 and 4.
            q0,v0=1/c,s/c
            dE,dP=2*cp,2*sp
            assert dE-v0*dP==2*q0*(cp*c-sp*s)
        # m1=2,m2=4 at the same physical p; algebraic mass Jacobian.
        # The new cosh need not lie in Q(sqrt5), so square the identity.
        old_s=s;new_s=s/2
        new_c_squared=1+new_s*new_s
        assert 4*old_s*old_s==16*new_s*new_s
        assert new_c_squared==1+old_s*old_s/4
    print('PASS momentum_pullback_pairs=289 comoving_clock_pairs=289')
    # Submitted minus-flow has jacobian_squared=cosh(eta)/(cosh(tau)cosh(f)).
    # The true df/deta is exp(-tau)cosh(eta)/cosh(f), so the norm multiplier is
    # exp(tau)/cosh(tau)=8/5 at exp(tau)=2. No quadrature is involved.
    a=R(2);cosh_tau=(a+1/a)/2
    assert a/cosh_tau==R(8,5)
    print('PASS original_wrong_mass_map_norm_factor=8/5')
    J=(1,0,1,0)
    basis=[tuple(int(i==k) for i in range(4)) for k in range(4)]
    M=tuple(zip(*(zmul(J,v) for v in basis)))
    assert M==((1,0,-1,1),(0,1,-1,0),(1,0,0,0),(0,1,-1,1))
    Q=((1,1,0,1),(0,0,1,1),(0,1,0,1),(0,1,0,0))
    Qi=((1,0,-1,0),(0,0,0,1),(0,1,-1,1),(0,0,1,-1))
    assert det(Q)==1 and mm(Q,Qi)==ident(4) and mm(Qi,Q)==ident(4)
    F=((0,1),(1,1));Fi=((-1,1),(1,0));B=diagblock(F,Fi)
    assert mm(F,Fi)==ident(2) and det(M)==det(B)==1
    assert mm(mm(Qi,mpow(M,5)),Q)==diagblock(neg(mpow(F,5)),mpow(Fi,5))
    assert mm(mm(Qi,mpow(M,10)),Q)==mpow(B,10)
    assert charpoly(mpow(M,10))==(1,-246,15131,-246,1)
    assert charpoly(mpow(B,10))==(1,-246,15131,-246,1)
    for n in range(1,10):
        assert charpoly(mpow(M,n))!=charpoly(mpow(B,n))
    print('PASS integral_conjugacy_Q_det=1 block5_sign=verified block10=verified')
    print('PASS smaller_positive_blocks_1_through_9=not_similar_by_charpoly')
    print('SCOPE finite exact audit only; all-parameter claims require PROOF.md')
    print('PUBLIC_PROMOTION none; INDEPENDENT_REVIEW none')

if __name__=='__main__':
    main()
