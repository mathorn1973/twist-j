#!/usr/bin/env python3
"""NON-CANONICAL exact L1 audit. Not a physical TT closure or formal gate."""
from __future__ import annotations
from fractions import Fraction as Q
from itertools import product

G = Q(1, 5)
WORDS = ('0010','0011','0100','0101','0110','1001','1010','1011','1100','1101')
CHECKS = 0


def require(ok: bool, name: str) -> None:
    global CHECKS
    CHECKS += 1
    if not ok:
        raise AssertionError(name)


class Poly:
    """Sparse commutative polynomials with exact rational coefficients."""
    def __init__(self, value=0):
        self.t = dict(value) if isinstance(value, dict) else ({(): Q(value)} if value else {})
        self.t = {m: Q(c) for m, c in self.t.items() if c}

    @staticmethod
    def var(i):
        return Poly({(i,): Q(1)})

    def __add__(self, other):
        other = other if isinstance(other, Poly) else Poly(other)
        out = dict(self.t)
        for m, c in other.t.items():
            out[m] = out.get(m, Q(0)) + c
        return Poly(out)

    __radd__ = __add__

    def __neg__(self):
        return Poly({m: -c for m, c in self.t.items()})

    def __sub__(self, other):
        return self + (-other if isinstance(other, Poly) else -Q(other))

    def __rsub__(self, other):
        return -self + other

    def __mul__(self, other):
        other = other if isinstance(other, Poly) else Poly(other)
        out = {}
        for m, c in self.t.items():
            for n, d in other.t.items():
                k = tuple(sorted(m + n))
                out[k] = out.get(k, Q(0)) + c * d
        return Poly(out)

    __rmul__ = __mul__

    def __pow__(self, n):
        if n < 0:
            raise ValueError('nonnegative polynomial exponent required')
        out = Poly(1)
        for _ in range(n):
            out = out * self
        return out

    def diff(self, i):
        out = {}
        for m, c in self.t.items():
            if i in m:
                n = list(m)
                count = n.count(i)
                n.remove(i)
                k = tuple(n)
                out[k] = out.get(k, Q(0)) + count * c
        return Poly(out)


def symbolic():
    a,b,c,d,e,f,l = (Poly.var(i) for i in range(7))
    require(not (Q(1,2)*((c-b)**2-(b-a)**2)-Q(1,2)*(c-a)*(c-2*b+a)).t, 'kinetic identity')
    for w in (Q(29,324), Q(65,324)):
        delta = w*Q(1,4)*(e-b)*((f-c)-(d-a))
        cur = w*Q(1,4)*(e-b)*((c-a)+(f-d))
        require(not (delta-cur-w*Q(1,2)*(c-a)*(b-e)).t, 'tail edge identity')
        require(not (delta+cur-w*Q(1,2)*(f-d)*(e-b)).t, 'head edge identity')
    delta_int = G*Q(1,2)*(b-e)*((c-f)-(a-d))
    require(not (G*Q(1,4)*(c-a)*(e-b)+G*Q(1,4)*(f-d)*(b-e)+delta_int*Q(1,2)).t, 'interaction cancellation')
    act = Q(1,4)*((b-a)**2+(c-b)**2+(e-d)**2+(f-e)**2-l*b*b-l*e*e-G*(b-e)**2)
    require(not (act.diff(1)+Q(1,2)*(c-2*b+a+l*b+G*(b-e))).t, 'x Euler equation')
    require(not (act.diff(4)+Q(1,2)*(f-2*e+d+l*e+G*(e-b))).t, 'y Euler equation')
    # At x=y, two copies with coefficient 1/4 recover one coefficient 1/2.
    sync = Q(1,4)*(2*(b-a)**2-2*l*a*a)
    require(not (sync-Q(1,2)*((b-a)**2-l*a*a)).t, 'synchronized action')
    print('SYMBOLIC local balance, reciprocal Euler equations, synchronized action PASS')


def add(a,b):
    return [x+y for x,y in zip(a,b)]


def sub(a,b):
    return [x-y for x,y in zip(a,b)]


def scale(c,a):
    return [c*x for x in a]


def dot(a,b):
    return sum((x*y for x,y in zip(a,b)), Q(0))


def mul_poly(a,b):
    out = [Q(0)]*(len(a)+len(b)-1)
    for i,c in enumerate(a):
        for j,d in enumerate(b):
            out[i+j] += c*d
    return out


class Graph:
    def __init__(self, dim):
        self.dim = dim
        self.vertices = list(product(range(5), repeat=dim))
        lookup = {v:i for i,v in enumerate(self.vertices)}
        self.size = len(self.vertices)
        self.factor = Q(1,5**(dim-1))
        self.edges = []
        for i,v in enumerate(self.vertices):
            for axis in range(dim):
                for k,w in ((1,Q(29,324)), (2,Q(65,324))):
                    u = list(v)
                    u[axis] = (u[axis]+k)%5
                    self.edges.append((i,lookup[tuple(u)],w))
        # Nonzero spectral annihilator: eigenvalues m*lambda_plus+n*lambda_minus.
        self.ann = [Q(1)]
        for m in range(dim+1):
            for n in range(dim+1-m):
                if m < n or m+n == 0:
                    continue
                center = Q(235*(m+n),324)
                if m == n:
                    factor = [-center,Q(1)]
                else:
                    gap = Q(18*(m-n),324)
                    factor = [center*center-5*gap*gap,-2*center,Q(1)]
                self.ann = mul_poly(self.ann,factor)

    def lap(self,a):
        out = [Q(0)]*self.size
        for i,j,w in self.edges:
            z = w*(a[i]-a[j])
            out[i] += z
            out[j] -= z
        return out

    def grad_w(self,a):
        return [w*(a[j]-a[i]) for i,j,w in self.edges]

    def div(self,a):
        out = [Q(0)]*self.size
        for (i,j,_),z in zip(self.edges,a):
            out[i] -= z
            out[j] += z
        return out

    def mean_zero(self,a):
        mean = sum(a,Q(0))/self.size
        return [x-mean for x in a]

    def inv_zero(self,a):
        rhs = self.mean_zero(a)
        out = [Q(0)]*self.size
        for c in reversed(self.ann[1:]):
            out = add(self.lap(out),scale(c,rhs))
        out = scale(-1/self.ann[0],out)
        require(self.lap(out) == rhs, 'exact Poisson inverse')
        require(sum(out,Q(0)) == 0, 'Poisson mean zero')
        return out

    def energy(self,a,b):
        out = [Q(1,2)*(y-x)**2 for x,y in zip(a,b)]
        for i,j,w in self.edges:
            term = w*Q(1,4)*(b[j]-b[i])*(a[j]-a[i])
            out[i] += term
            out[j] += term
        return out

    def current(self,a,b,c):
        q = sub(c,a)
        return [w*Q(1,4)*(b[j]-b[i])*(q[i]+q[j]) for i,j,w in self.edges]

    def next_pair(self,a,b,c,d):
        xn = sub(sub(scale(2,b),a),self.lap(b))
        yn = sub(sub(scale(2,d),c),self.lap(d))
        return add(xn,scale(G,sub(d,b))),add(yn,scale(G,sub(b,d)))

    def total_energy(self,x0,x1,y0,y1):
        ex,ey = self.energy(x0,x1),self.energy(y0,y1)
        cross = [G*Q(1,2)*(a-c)*(b-d) for a,b,c,d in zip(x0,x1,y0,y1)]
        return scale(Q(1,2),add(add(ex,ey),cross))

    def total_current(self,x0,x1,x2,y0,y1,y2):
        return scale(Q(1,2),add(self.current(x0,x1,x2),self.current(y0,y1,y2)))

    def total(self,a):
        return self.factor*sum(a,Q(0))


def evolution(graph,x0,x1,y0,y1,links):
    xs,ys = [x0,x1],[y0,y1]
    for _ in range(1,links):
        xn,yn = graph.next_pair(xs[-2],xs[-1],ys[-2],ys[-1])
        xs.append(xn)
        ys.append(yn)
    energies = [graph.total_energy(xs[n],xs[n+1],ys[n],ys[n+1]) for n in range(links)]
    taus = [scale(Q(1,2),graph.inv_zero(e)) for e in energies]
    energy = graph.total(energies[0])
    require(energy > 0, 'positive fixture energy')
    for n,e in enumerate(energies):
        require(graph.total(e) == energy, 'global energy')
        require(scale(2,graph.lap(taus[n])) == graph.mean_zero(e), 'scalar constraint')
    for n in range(1,links):
        cur = graph.total_current(xs[n-1],xs[n],xs[n+1],ys[n-1],ys[n],ys[n+1])
        require(add(sub(energies[n],energies[n-1]),graph.div(cur)) == [0]*graph.size, 'local conservation')
        grad = graph.grad_w(sub(taus[n],taus[n-1]))
        p = sub(scale(Q(-1,2),cur),grad)
        require(graph.div(p) == [0]*graph.size, 'co-closed momentum')
        require(add(scale(2,add(grad,p)),cur) == [0]*len(graph.edges), 'momentum constraint')
    return xs,ys,energy


def word_pair(word):
    w = tuple(map(int,word))
    u = (w[2]-w[0],w[3]-w[1])
    pair = [[Q(int(r == v%5)+int(r == (v+1)%5),2) for r in range(5)] for v in u]
    return u,pair


def audits():
    graph = Graph(1)
    zero = [Q(0)]*5
    source_energies = {}
    for word in WORDS:
        u,(a,b) = word_pair(word)
        xs,ys,E = evolution(graph,zero,zero,a,b,32)
        require(xs[2] == scale(G,b), 'first emission')
        require(any(xs[2]), 'nonzero first emission')
        require(all(sum(add(x,y),Q(0)) == 1 for x,y in zip(xs,ys)), 'common zero mode')
        # Independent normal coordinates have operators L and L+2gI.
        for n in range(1,32):
            s0,s1,s2 = (add(xs[t],ys[t]) for t in (n-1,n,n+1))
            d0,d1,d2 = (sub(xs[t],ys[t]) for t in (n-1,n,n+1))
            require(add(add(sub(s2,scale(2,s1)),s0),graph.lap(s1)) == zero, 'normal plus mode')
            require(add(add(add(sub(d2,scale(2,d1)),d0),graph.lap(d1)),scale(2*G,d1)) == zero, 'normal minus mode')
        eK = graph.total(graph.energy(a,b))
        require(E == eK/2+G*dot(a,b)/4, 'initial energy formula')
        source_energies[abs(u[1]-u[0])] = E
        sx,sy,_ = evolution(graph,a,b,a,b,4)
        require(sx == sy, 'synchronized invariant subspace')
        require(graph.total_energy(a,b,a,b) == graph.energy(a,b), 'synchronized energy')
    print('WORDS 10; LINKS_PER_WORD 32; FIRST_EMISSION 10/10 PASS')
    print('SOURCE_ENERGIES '+','.join(str(k)+':'+str(source_energies[k]) for k in sorted(source_energies)))

    g3 = Graph(3)
    x0 = [Q((v[0]+2*v[1]+3*v[2])%7-3,7) for v in g3.vertices]
    y0 = [Q((2*v[0]+v[1]+v[2])%5-2,5) for v in g3.vertices]
    evolution(g3,x0,x0,y0,y0,4)
    print('NONPLANAR VERTICES 125 EDGES 750 LINKS 4; ALL CONSTRAINTS PASS')

    # sqrt(5)<9/4, since 5<81/16; all eigenvalues of L3+2gI are below 4.
    upper = 3*(Q(235)+18*Q(9,4))/324+2*G
    require(Q(5) < Q(81,16) and upper < 4, 'exact spectral stability bound')
    print('SPECTRAL_UPPER_BOUND '+str(upper)+' < 4 PASS')

    a,b = word_pair('0101')[1]
    xs,ys,_ = evolution(graph,zero,zero,a,b,3)
    m = 1
    cur = graph.total_current(xs[0],xs[1],xs[2],ys[0],ys[1],ys[2])
    bare0 = scale(Q(1,2),add(graph.energy(xs[0],xs[1]),graph.energy(ys[0],ys[1])))
    bare1 = scale(Q(1,2),add(graph.energy(xs[1],xs[2]),graph.energy(ys[1],ys[2])))
    defect = add(sub(bare1,bare0),graph.div(cur))
    require(any(defect), 'NC1 omitted interaction must fail')
    print('NC1_OMITTED_INTERACTION_DEFECT '+','.join(map(str,defect)))

    _,new_y = graph.next_pair(a,b,zero,zero)
    require(new_y == scale(G,b) and any(new_y), 'NC2 reservoir-zero not invariant')
    print('NC2_RESERVOIR_ZERO NOT_INVARIANT; synchronization is distinct')

    # One-way forcing violates the reciprocal y Euler equation on this same input.
    forced_x = scale(G,b)
    frozen_y_next = sub(scale(2,b),a)
    frozen_y_next = sub(frozen_y_next,graph.lap(b))
    residual_y = add(add(sub(frozen_y_next,scale(2,b)),a),graph.lap(b))
    residual_y = sub(residual_y,scale(G,sub(zero,b)))
    require(any(residual_y), 'NC3 one-way forcing breaks joint Euler equation')
    print('NC3_ONE_WAY_SOURCE JOINT_EULER_FAIL')
    print('NC4_PHYSICAL_TT_BRIDGES NOT_SUPPLIED; TT-SOURCE remains O')


def main():
    symbolic()
    audits()
    print('EXACT_ASSERTIONS '+str(CHECKS))
    print('INCUBATION_MATHEMATICAL_AUDIT PASS; NO_PUBLIC_STATUS_CHANGE')


if __name__ == '__main__':
    main()
