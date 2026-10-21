#!/usr/bin/env python3
"""Exact, source-exposed finite audit. This is not a public TWIST-J gate."""
from fractions import Fraction as F
from collections import Counter

class Field:
    def __init__(self, order):
        self.order = order
        self.low = (1,1,1,1) if order == 5 else (1,0,0,0)
    def el(self, value):
        if isinstance(value, E):
            assert value.k is self
            return value
        if isinstance(value, (int, F)):
            value = (value,0,0,0)
        return E(self, tuple(F(x) for x in value))
    @property
    def root(self): return self.el((0,1,0,0))

class E:
    def __init__(self, k, c): self.k, self.c = k, c
    def __add__(self, other):
        other = self.k.el(other)
        return self.k.el(tuple(a+b for a,b in zip(self.c,other.c)))
    __radd__ = __add__
    def __neg__(self): return self.k.el(tuple(-a for a in self.c))
    def __sub__(self, other): return self + (-self.k.el(other))
    def __rsub__(self, other): return self.k.el(other) - self
    def __mul__(self, other):
        other = self.k.el(other)
        p = [F(0)]*7
        for i,a in enumerate(self.c):
            for j,b in enumerate(other.c): p[i+j] += a*b
        for n in range(6,3,-1):
            for i,t in enumerate(self.k.low): p[n-4+i] -= p[n]*t
        return self.k.el(tuple(p[:4]))
    __rmul__ = __mul__
    def __pow__(self, n):
        if n < 0: return self.inv() ** (-n)
        ans, base = self.k.el(1), self
        while n:
            if n & 1: ans = ans*base
            base = base*base
            n >>= 1
        return ans
    def inv(self):
        if not any(self.c): raise ZeroDivisionError()
        cols = [(self * self.k.el(tuple(int(i==j) for i in range(4)))).c for j in range(4)]
        A = [[cols[j][i] for j in range(4)] + [F(i==0)] for i in range(4)]
        for j in range(4):
            p = next(i for i in range(j,4) if A[i][j])
            A[j], A[p] = A[p], A[j]
            q = A[j][j]
            A[j] = [x/q for x in A[j]]
            for i in range(4):
                if i != j:
                    q = A[i][j]
                    A[i] = [a-q*b for a,b in zip(A[i],A[j])]
        ans = self.k.el(tuple(A[i][-1] for i in range(4)))
        assert self*ans == 1
        return ans
    def __truediv__(self, other): return self * self.k.el(other).inv()
    def __rtruediv__(self, other): return self.k.el(other) / self
    def __eq__(self, other):
        other = self.k.el(other)
        return self.c == other.c
    def __hash__(self): return hash((id(self.k), self.c))
    def conj(self): return sum((a*self.k.root**((-i)%self.k.order) for i,a in enumerate(self.c)), self.k.el(0))
    def __repr__(self): return str(self.c)

def h(v): return sum(x*x.conj() for x in v)
def inner(v,w): return sum(x.conj()*y for x,y in zip(v,w))
def P(v,w):
    a = inner(v,w)
    return a*a.conj()/(h(v)*h(w))
def perp(v): return (-v[1].conj(),v[0].conj())
def rho(v):
    hv = h(v)
    return [[a*b.conj()/hv for b in v] for a in v]
def pair_trace(R,S): return sum(R[i][j]*S[j][i] for i in range(2) for j in range(2))

def run(order):
    K = Field(order)
    j, one, zero = K.root, K.el(1), K.el(0)
    poles = [(one,zero),(zero,one)]
    phases = [s*j**k for s in (1,-1) for k in range(5)] if order==5 else [j**k for k in range(8)]
    rays = poles + [(one,z) for z in phases]
    for v in rays:
        R = rho(v)
        assert R[0][0]+R[1][1] == 1
        for a in range(2):
            for b in range(2):
                assert sum(R[a][k]*R[k][b] for k in range(2)) == R[a][b]
    for v in rays:
        for w in rays:
            a = inner(v,w)
            d = v[0]*w[1]-v[1]*w[0]
            assert h(v)*h(w) == a*a.conj()+d*d.conj()
            assert P(v,w)+P(v,perp(w)) == 1
            assert P(v,w) == pair_trace(rho(v),rho(w))
    frame = [[sum(rho(v)[a][b] for v in rays) for b in range(2)] for a in range(2)]
    assert frame == [[K.el(len(rays)//2),zero],[zero,K.el(len(rays)//2)]]
    counts = Counter(P(v,w) for v in rays for w in rays)
    if order == 5:
        phi = -j**2-j**3
        expected = {K.el(0):12, K.el(1):12, K.el(F(1,2)):40,
                    (phi+1)/4:20,(2-phi)/4:20,(3-phi)/4:20,(2+phi)/4:20}
        assert counts == expected
        high,low = (phi+1)/4,(2-phi)/4
        assert [P((one,one),(one,j**(2**k))) for k in range(4)] == [high,low,high,low]
        assert high+low == F(3,4) and high*low == F(1,16)
        assert P((one,j),(one,-j)) == 0
        for v in rays:
            R = rho(v)
            u = 2*pair_trace(R,rho((one,one)))-1
            t = 2*pair_trace(R,rho((one,j)))-1
            c = (t-j.conj()*u)/(j-j.conj())
            assert c == R[0][1]
        print('K5 PASS: 12 declared rays; 144 exact pair checks; 7 overlap values.')
        print('K5 multiplicities: 0:12, 1:12, 1/2:40, each remaining value:20.')
        print('K5 PASS: cycle HIGH,LOW,HIGH,LOW; three-context reconstruction.')
    else:
        rt2 = j-j**3
        high,low = (2+rt2)/4,(2-rt2)/4
        assert counts == {K.el(0):10,K.el(1):10,K.el(F(1,2)):48,high:16,low:16}
        assert [P((one,one),(one,j**(1+2*k))) for k in range(4)] == [high,low,low,high]
        assert P((one,one),(one,j)) == high and high != 0
        print('K8 PASS: 10 declared rays; 100 exact pair checks; 5 overlap values.')
        print('K8 multiplicities: 0:10, 1:10, 1/2:48, each remaining value:16.')
        print('K8 PASS: cycle HIGH,LOW,LOW,HIGH; proposed bridge breaks orthogonality.')
    print('PASS: trace-one idempotents, frame sum, Lagrange identity and binary complements.')

if __name__ == '__main__':
    print('NON-CANONICAL / L1 / bounded source-exposed local audit / candidate-C')
    run(5)
    run(8)
    print('No height-exhaustiveness, Born derivation, physical bridge or sampling conclusion.')
