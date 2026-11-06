#!/usr/bin/env python3
"""Frozen exact audit of the existing W at P=0. No floating point."""
from fractions import Fraction as Q
from functools import lru_cache
from math import isqrt


def trim(p):
    p = list(p)
    while p and p[-1] == 0:
        p.pop()
    return p


def padd(a, b):
    p = [Q(0)] * max(len(a), len(b))
    for j, v in enumerate(a):
        p[j] += v
    for j, v in enumerate(b):
        p[j] += v
    return trim(p)


def pneg(a):
    return [-x for x in a]


def pmul(a, b):
    if not a or not b:
        return []
    p = [Q(0)] * (len(a)+len(b)-1)
    for j, x in enumerate(a):
        for k, y in enumerate(b):
            p[j+k] += x*y
    return trim(p)


def pdiv(a, b):
    a, b = trim(a), trim(b)
    if not b:
        raise ZeroDivisionError('zero polynomial')
    q = [Q(0)] * max(0, len(a)-len(b)+1)
    while a and len(a) >= len(b):
        d = len(a)-len(b)
        c = a[-1]/b[-1]
        q[d] += c
        for j, t in enumerate(b):
            a[d+j] -= c*t
        a = trim(a)
    return trim(q), a


MOD = tuple(map(Q, (1, 0, -1, 0, 1, 0, -1, 0, 1)))


class K:
    """Q[zeta20], coefficient basis modulo Phi20; exact rational coefficients."""
    __slots__ = ('c',)

    def __init__(self, value=0):
        if isinstance(value, K):
            self.c = value.c
            return
        p = list(map(Q, value)) if isinstance(value, (tuple, list)) else [Q(value)]
        for d in range(len(p)-1, 7, -1):
            t = p[d]
            if t:
                for j, sign in ((0, -1), (2, 1), (4, -1), (6, 1)):
                    p[d-8+j] += sign*t
        p = p[:8]
        p += [Q(0)]*(8-len(p))
        self.c = tuple(p)

    def __hash__(self):
        return hash(self.c)

    def __eq__(self, other):
        return self.c == K(other).c

    def __bool__(self):
        return any(self.c)

    def __add__(self, other):
        o = K(other)
        return K(tuple(a+b for a, b in zip(self.c, o.c)))
    __radd__ = __add__

    def __neg__(self):
        return K(tuple(-v for v in self.c))

    def __sub__(self, other):
        return self + (-K(other))

    def __rsub__(self, other):
        return K(other) - self

    def __mul__(self, other):
        return K(pmul(self.c, K(other).c))
    __rmul__ = __mul__

    def __truediv__(self, other):
        return self * inverse(K(other))

    def __rtruediv__(self, other):
        return K(other) / self

    def __pow__(self, n):
        if not isinstance(n, int):
            raise TypeError('integer exponent required')
        base = self
        if n < 0:
            base, n = inverse(base), -n
        out = K(1)
        while n:
            if n & 1:
                out = out*base
            base = base*base
            n >>= 1
        return out

    def __repr__(self):
        return 'K'+repr(self.c)


@lru_cache(maxsize=None)
def inverse(x):
    if not x:
        raise ZeroDivisionError('zero field element')
    r0, r1 = list(MOD), trim(x.c)
    s0, s1 = [], [Q(1)]
    while r1:
        q, r = pdiv(r0, r1)
        r0, r1 = r1, r
        s0, s1 = s1, padd(s0, pneg(pmul(q, s1)))
    assert len(r0) == 1 and r0[0] != 0
    return K([v/r0[0] for v in s0])


Z20 = K((0, 1))
I = Z20**5
J5 = Z20**4
GAMMA = J5**4
SQ5 = 1+2*(J5+J5**4)
PHI = (1+SQ5)/2
BAR_Z = Z20**19


@lru_cache(maxsize=None)
def bar(x):
    out = K(0)
    for c in reversed(x.c):
        out = out*BAR_Z+c
    return out


def re(x):
    return (x+bar(x))/2


def abs2(x):
    return x*bar(x)


def mm(a, b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(len(b)))
                       for j in range(len(b[0]))) for i in range(len(a)))


def mv(a, x):
    return tuple(sum(t*v for t, v in zip(row, x)) for row in a)


def adj(a):
    return tuple(tuple(bar(K(a[j][i])) for j in range(len(a)))
                 for i in range(len(a[0])))


def eye(n):
    return tuple(tuple(K(i == j) for j in range(n)) for i in range(n))


def det2(a):
    return a[0][0]*a[1][1]-a[0][1]*a[1][0]


def inv2(a):
    d = det2(a)
    return ((a[1][1]/d, -a[0][1]/d), (-a[1][0]/d, a[0][0]/d))


def transfer(rho):
    return ((rho*(5*rho+3)/(rho-1), 4*(rho+1)/(rho-1)),
            (-4*(rho+1)/(rho-1), (-3*rho-5)/(rho*(rho-1))))


FLUX = ((K(-1), K(0)), (K(0), K(1)))
COIN = tuple(tuple(K(x)/5 for x in row) for row in
             ((1, 2*I, 2*I, -4), (2*I, 1, -4, 2*I),
              (2*I, -4, 1, 2*I), (-4, 2*I, 2*I, 1)))


def flux(v):
    return abs2(v[1])-abs2(v[0])


def direct_states(lam, kap, ze, V, sig, S):
    """Substitute stationary states in the ORIGINAL four-channel recurrence."""
    checks = 0
    for incidence in (0, 1):
        if incidence == 0:
            cl, cr = (K(1), S[0][0]), (S[1][0], K(0))
        else:
            cl, cr = (K(0), S[0][1]), (S[1][1], K(1))

        @lru_cache(maxsize=None)
        def bond(r):
            c = cl if r <= 0 else cr
            return mv(V, (ze**(-sig*r)*c[0], ze**(sig*r)*c[1]))

        @lru_cache(maxsize=None)
        def original(r):
            k = kap if r == 0 else K(1)
            L, R = bond(r+1)[0], bond(r)[1]
            u = 2*I*k*(L+R)/(5*lam+3*k)
            return tuple(k*v for v in (u, L, R, u))

        for r in range(-2, 3):
            k = kap if r == 0 else K(1)
            out = []
            for row, src in enumerate((r, r+1, r-1, r)):
                out.append(k*mv(COIN, original(src))[row])
            assert tuple(out) == tuple(lam*v for v in original(r)), ('original recurrence', incidence, r)
            checks += 4
    return checks


def finite_walk(v, kap):
    out = {}
    for (r, col), amp in v.items():
        for row, shift in enumerate((0, -1, 1, 0)):
            site = r+shift
            k = kap if site == 0 else K(1)
            term = k*COIN[row][col]*amp
            key = (site, row)
            out[key] = out.get(key, K(0))+term
    return {k: v for k, v in out.items() if v}


def compact_projection(v):
    u = (v.get((0, 0), K(0))-v.get((0, 3), K(0)))/2
    return {(0, 0): u, (0, 3): -u} if u else {}


class Interval:
    __slots__ = ('lo', 'hi')

    def __init__(self, lo, hi=None):
        if isinstance(lo, Interval):
            self.lo, self.hi = lo.lo, lo.hi
        else:
            self.lo, self.hi = Q(lo), Q(lo if hi is None else hi)
        assert self.lo <= self.hi

    def __add__(self, other):
        b = Interval(other)
        return Interval(self.lo+b.lo, self.hi+b.hi)
    __radd__ = __add__

    def __neg__(self):
        return Interval(-self.hi, -self.lo)

    def __sub__(self, other):
        return self+(-Interval(other))

    def __rsub__(self, other):
        return Interval(other)-self

    def __mul__(self, other):
        b = Interval(other)
        corners = (self.lo*b.lo, self.lo*b.hi, self.hi*b.lo, self.hi*b.hi)
        return Interval(min(corners), max(corners))
    __rmul__ = __mul__

    def __truediv__(self, other):
        b = Interval(other)
        assert b.lo > 0 or b.hi < 0
        return self*Interval(1/b.hi, 1/b.lo)

    def square(self):
        low = 0 if self.lo <= 0 <= self.hi else min(self.lo*self.lo, self.hi*self.hi)
        return Interval(low, max(self.lo*self.lo, self.hi*self.hi))

    def root(self):
        assert self.lo >= 0
        scale = 1 << 80
        a = isqrt((self.lo.numerator*scale*scale)//self.lo.denominator)
        b = isqrt((self.hi.numerator*scale*scale)//self.hi.denominator)+1
        assert Q(a*a, scale*scale) <= self.lo
        assert Q(b*b, scale*scale) >= self.hi
        return Interval(Q(a, scale), Q(b, scale))


def interval_reflection(cq, sig):
    root5 = Interval(5).root()
    cg = (root5-1)/4
    sg = (10+2*root5).root()/4
    c = (cq-4)/5
    st = (1-c.square()).root()
    d = c*cg-sig*st*sg
    n = 80*(1+d)*(d-c).square()
    m = (1-c)*(1-d)*(-5*c-3)
    assert n.lo >= 0 and m.lo > 0
    R = n/(n+m)
    assert 0 <= R.lo <= R.hi <= 1
    return R


def print_interval(label, R):
    scale = 10**9
    lo = (R.lo.numerator*scale)//R.lo.denominator
    hi = -((-R.hi.numerator*scale)//R.hi.denominator)
    assert 0 <= hi-lo <= 2
    print(label+' '+str(lo)+'/'+str(scale)+' <= R <= '+str(hi)+'/'+str(scale))


def main():
    assert Z20**20 == 1 and I*I == -1 and J5**5 == 1
    assert SQ5*SQ5 == 5 and PHI*PHI == PHI+1
    assert bar(GAMMA)*GAMMA == 1 and bar(I) == -I
    assert mm(adj(COIN), COIN) == eye(4)
    cases = residuals = 0
    for j in range(5, 21):
        aa = Q(j, 4)
        t, u = aa+1/aa, aa-1/aa
        assert t*t-u*u == 4
        lp = (1+I*t)/(1-I*t)
        cq = K((9-t*t)/(1+t*t))
        sq = 2*SQ5*u/(1+t*t)
        ze = cq+I*sq
        assert abs2(ze) == 1 and abs2(lp) == 1
        b0 = K(4/t)
        a0 = b0*(1-5*re(lp))/4
        assert a0*a0-b0*b0 == sq*sq
        H = a0+sq
        V = ((b0, H), (H, b0))
        normal = 2*sq*H
        assert mm(mm(adj(V), FLUX), V) == ((normal, K(0)), (K(0), -normal))
        for sig in (1, -1):
            lam = lp if sig == 1 else bar(lp)
            free = transfer(lam)
            D = ((ze**(-sig), K(0)), (K(0), ze**sig))
            assert mm(free, V) == mm(V, D)
            for kap in (K(1), GAMMA):
                a = kap*(lam-kap)/(5*lam+3*kap)
                b = -4*kap*(lam+kap)/(5*lam+3*kap)
                direct = ((lam/a, -b/a), (b/a, (a*a-b*b)/(lam*a)))
                defect = transfer(lam/kap)
                assert direct == defect and det2(defect) == 1
                assert mm(mm(adj(defect), FLUX), defect) == FLUX
                M = mm(mm(inv2(V), defect), V)
                Kmat = mm(inv2(D), M)
                assert det2(Kmat) == 1
                denom = Kmat[1][1]
                S = ((-Kmat[1][0]/denom, 1/denom),
                     (1/denom, Kmat[0][1]/denom))
                assert mm(adj(S), S) == eye(2)
                r, tr = abs2(S[0][0]), abs2(S[1][0])
                assert r+tr == 1 and r == abs2(S[1][1])
                c, d = re(lam), re(lam/kap)
                n = 80*(1+d)*(d-c)**2
                m = (1-c)*(1-d)*(-5*c-3)
                assert r == n/(n+m), ('scalar formula', j, sig)
                if kap == 1:
                    assert S == ((K(0), K(1)), (K(1), K(0)))
                if sig == 1:
                    rho = lam/kap
                    b1 = 4*I*(rho+1)/(rho-1)
                    a1 = b1*(1-5*d)/4
                    Y, ZZ = a0*b1-b0*a1, a0*a1-b0*b1
                    den = sq*(5*d+4)+I*ZZ
                    closed = ((I*Y/den, ze*sq/den),
                              (ze*sq/den, I*ze*ze*Y/den))
                    assert S == closed, ('phase formula', j)
                residuals += direct_states(lam, kap, ze, V, sig, S)
                cases += 1
    print('G1 PASS exact_field_cases='+str(cases)+' transfer_flux_S_unitarity_free_limit_scalar_and_phase_formulas')
    print('G2 PASS original_four_channel_stationary_equations='+str(residuals)+' left_and_right_incidence_no_truncation')
    special = J5**2
    assert special*special == GAMMA
    assert mm(transfer(special/GAMMA), transfer(special)) == eye(2)
    assert re(special) == -PHI/2
    assert 5*re(special)+4 == 4-5*PHI/2
    assert re(special/GAMMA) == re(special)
    print('G3 PASS exact_transparency_lambda=j^2 lambda_squared=gamma cos_q=4-5phi/2 defect_inverse_free')
    dark = 0
    for r in (-1, 0, 1):
        for coin in range(4):
            v = {(r, coin): K(1)}
            projection = compact_projection(v)
            expect = {key: GAMMA*x for key, x in projection.items()}
            assert compact_projection(finite_walk(v, GAMMA)) == expect
            assert finite_walk(projection, GAMMA) == expect
            dark += 1
    print('G4 PASS compact_A_commutator_basis_controls='+str(dark)+' zero_capture_from_orthogonal_input')
    root3 = Interval(3).root()
    for label, cq in (('pi/6', root3/2), ('pi/3', Interval(Q(1, 2))),
                      ('pi/2', Interval(0)), ('5pi/6', -root3/2)):
        for sig in (1, -1):
            R = interval_reflection(cq, sig)
            print_interval('INTERVAL q='+label+' eigenphase='+('+' if sig == 1 else '-'), R)
    print('G5 PASS eight_stationary_reflection_enclosures sqrt_bits=80 width_at_most=2/1000000000')
    assert (-1+3*PHI)*(-1+3*(1-PHI)) == -11
    assert (-1+4*PHI)*(-1+4*(1-PHI)) == -19
    assert Q(1, 11) != Q(4, 19)
    print('G6 PASS prime_addresses_use_norm_minus_11_minus_19_and_mass_normalization_not_literal_O_plus')
    print('STATUS NON-CANONICAL same-session exact audit; no independent review, occurrence or native-U claim')


if __name__ == '__main__':
    main()
