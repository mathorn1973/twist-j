#!/usr/bin/env python3
"""Prospective boost-completion audit. NON-CANONICAL, NEW_DECLARED L1.

Jet and matrix utilities adapted from P-RELATIONAL-MASS-INERTIAL-RESPONSE-1.
No runtime dependency on that probe. No floating point or ODE integration. Universal
claims and the limiting statement are proved in PROOF.md, not by this audit.
"""
from fractions import Fraction as F
from math import isqrt


class Failure(Exception):
    pass


def require(condition, code):
    if not condition:
        raise Failure(code)


class Jet:
    """Coefficients of 1,t,t^2, with exact rational square-root recursion."""
    def __init__(self, a=0, b=0, c=0):
        self.c = (F(a), F(b), F(c))

    def __add__(self, other):
        other = lift(other)
        return Jet(*(a + b for a, b in zip(self.c, other.c)))

    __radd__ = __add__

    def __neg__(self):
        return Jet(*(-a for a in self.c))

    def __sub__(self, other):
        return self + (-lift(other))

    def __rsub__(self, other):
        return lift(other) - self

    def __mul__(self, other):
        other = lift(other)
        return Jet(*(sum(self.c[j] * other.c[i-j] for j in range(i+1))
                     for i in range(3)))

    __rmul__ = __mul__

    def reciprocal(self):
        require(self.c[0] != 0, "ZERO_DENOMINATOR")
        b = [1 / self.c[0]]
        for n in (1, 2):
            b.append(-sum(self.c[k] * b[n-k] for k in range(1, n+1))
                     / self.c[0])
        return Jet(*b)

    def __truediv__(self, other):
        return self * lift(other).reciprocal()

    def __rtruediv__(self, other):
        return lift(other) * self.reciprocal()


def lift(x):
    return x if isinstance(x, Jet) else Jet(x)


def root(x):
    if not isinstance(x, Jet):
        q = F(x)
        a, b = isqrt(q.numerator), isqrt(q.denominator)
        require(a*a == q.numerator and b*b == q.denominator and a > 0,
                "NONRATIONAL_OR_ZERO_ROOT")
        return F(a, b)
    a = root(x.c[0])
    b = x.c[1] / (2*a)
    return Jet(a, b, (x.c[2] - b*b) / (2*a))


def trans(a):
    return tuple(zip(*a))


def mm(a, b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))


def mv(a, b):
    return tuple(sum(a[i][j]*b[j] for j in range(2)) for i in range(2))


def add(a, b):
    return tuple(tuple(a[i][j]+b[i][j] for j in range(2)) for i in range(2))


def scale(s, a):
    return tuple(tuple(s*x for x in row) for row in a)


def outer(a, b):
    return tuple(tuple(x*y for y in b) for x in a)


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def trace(a):
    return a[0][0]+a[1][1]


def det(a):
    return a[0][0]*a[1][1]-a[0][1]*a[1][0]


def inv(a):
    return scale(1/det(a), ((a[1][1], -a[0][1]), (-a[1][0], a[0][0])))


def pack(g, pi, x, p, r, rho):
    return tuple(map(F, (g[0][0], g[0][1], g[1][1], pi[0][0],
                         pi[0][1], pi[1][1], *x, *p, *r, *rho)))


def unpack(z):
    return (((z[0], z[1]), (z[1], z[2])),
            ((z[3], z[4]), (z[4], z[5])), z[6:8], z[8:10],
            z[10:12], z[12:14])


def internal(z):
    g, pi, _, _, r, rho = unpack(z)
    h = (trace(mm(mm(mm(g,pi),g),pi))/2
         + root(dot(rho,mv(g,rho))) + 3*dot(r,mv(inv(g),r)))
    j = add(scale(2,mm(g,pi)),outer(r,rho))
    return h, j, j[0][1]-j[1][0]


def observables(z, c=F(1), spin_sign=F(1), alpha=F(1)):
    h, j, s = internal(z)
    _, _, x, p, _, _ = unpack(z)
    big_h = root(h*h+alpha*c*c*dot(p,p))
    rp = (-p[1],p[0])
    k = tuple(big_h*x[i]/(c*c)-spin_sign*s*rp[i]/(big_h+h)
              for i in range(2))
    ell = x[0]*p[1]-x[1]*p[0]+s
    velocity = tuple(alpha*c*c*pi/big_h for pi in p)
    return dict(h=h,H=big_h,S=s,L=ell,K1=k[0],K2=k[1],
                P1=p[0],P2=p[1],V1=velocity[0],V2=velocity[1],
                J11=j[0][0],J12=j[0][1],J21=j[1][0],J22=j[1][1])


def gradients(z, c=F(1), spin_sign=F(1), alpha=F(1)):
    values = observables(z,c,spin_sign,alpha)
    result = {name: [] for name in values}
    for k in range(14):
        zz = tuple(Jet(v,int(i == k)) for i,v in enumerate(z))
        for name,value in observables(zz,c,spin_sign,alpha).items():
            result[name].append(value.c[1])
    return values, {name:tuple(v) for name,v in result.items()}


def canonical(a):
    return (a[3],a[4]/2,a[5],-a[0],-a[1]/2,-a[2],
            a[8],a[9],-a[6],-a[7],a[12],a[13],-a[10],-a[11])


def bracket(a,b):
    return dot(a,canonical(b))


def scalar_gradient(function,z):
    return tuple(function(tuple(Jet(v,int(i == k)) for i,v in enumerate(z)))
                 .c[1] for k in range(14))


def old_energy(z):
    g,pi,_,p,r,rho = unpack(z)
    plus = tuple(a+b for a,b in zip(rho,p))
    minus = tuple(a-b for a,b in zip(rho,p))
    e = (root(dot(plus,mv(g,plus)))+root(dot(minus,mv(g,minus))))/2
    return trace(mm(mm(mm(g,pi),g),pi))/2+e+3*dot(r,mv(inv(g),r))


I = ((F(1),F(0)),(F(0),F(1)))
Z = ((F(0),F(0)),(F(0),F(0)))
PISTAR = ((F(0),F(-1)),(F(-1),F(0)))


def initial_states():
    a = pack(I,PISTAR,(0,0),(0,0),(1,0),(0,6))
    b = pack(I,((1,-1),(-1,0)),(0,0),(0,0),(1,1),(3,4))
    l = ((F(1),F(1)),(F(0),F(1)))
    il = inv(l)
    c = pack(mm(l,trans(l)),mm(mm(trans(il),PISTAR),il),
             (0,0),(0,0),mv(l,(1,0)),mv(trans(il),(0,6)))
    return a,b,c


def main():
    counts = dict(algebra=0,hessian=0,force=0,old=0)
    nontrivial_clocks = 0
    force = (F(1),F(2))
    centers = ((F(1),F(-2)),(F(-2),F(1)))
    directions = ((F(1),F(0)),(F(3,5),F(4,5)))
    for initial in initial_states():
        g,pi,_,_,r,rho = unpack(initial)
        h0,_,_ = internal(initial)
        require(g[0][0] > 0 and det(g) > 0 and h0 > 0,"DOMAIN")
        for c in (F(1),F(2)):
            for t in (F(0),F(1,4),F(1,2)):
                for direction,center in zip(directions,centers):
                    p = tuple(h0/c*2*t/(1-t*t)*d for d in direction)
                    z = pack(g,pi,center,p,r,rho)
                    value,grad = gradients(z,c)
                    require(value['H'] == h0*(1+t*t)/(1-t*t),"MOMENTUM_PARAM")
                    require(value['H']**2-c*c*dot(p,p) == h0*h0,
                            "MASS_CASIMIR")
                    require(value['H']*value['L']-c*c*(value['K1']*p[1]
                            -value['K2']*p[0]) == h0*value['S'],"SPIN_CASIMIR")
                    require(bracket(grad['P1'],grad['P2']) == 0,
                            "MOMENTUM_COMMUTATOR")
                    for i in (1,2):
                        for j in (1,2):
                            require(bracket(grad['K'+str(i)],grad['P'+str(j)])
                                    == (value['H']/(c*c) if i == j else 0),
                                    "BOOST_MOMENTUM")
                        require(bracket(grad['K'+str(i)],grad['H'])
                                == p[i-1],"BOOST_ENERGY")
                        require(bracket(grad['h'],grad['K'+str(i)]) == 0,
                                "INTERNAL_BOOST")
                        require(bracket(grad['S'],grad['K'+str(i)]) == 0,
                                "SPIN_BOOST")
                    require(bracket(grad['K1'],grad['K2']) == -value['L']/(c*c),
                            "BOOST_BOOST")
                    for name in ('P','K'):
                        require(bracket(grad['L'],grad[name+'1']) == value[name+'2']
                                and bracket(grad['L'],grad[name+'2'])
                                == -value[name+'1'],"ROTATION_"+name)
                    for name in ('P1','P2','L','h','J11','J12','J21','J22'):
                        require(bracket(grad[name],grad['H']) == 0,"CONSERVED_"+name)
                    fh,fi = canonical(grad['H']),canonical(grad['h'])
                    for k in (0,1,2,3,4,5,10,11,12,13):
                        require(fh[k] == h0/value['H']*fi[k],"INTERNAL_CLOCK")
                    require(fh[6:8] == tuple(c*c*a/value['H'] for a in p)
                            and fh[8:10] == (0,0),"CENTER_FLOW")
                    if t:
                        require(fh[10:12] != fi[10:12],"NC_FROZEN_CLOCK")
                        nontrivial_clocks += 1
                    # W=-f.X is a new explicit uniform-force comparison.
                    gw = (F(0),)*6+tuple(-a for a in force)+(F(0),)*6
                    gt = tuple(a+b for a,b in zip(grad['H'],gw))
                    require(tuple(bracket(grad['P'+str(i)],gt) for i in (1,2))
                            == force,"FORCE_MOMENTUM")
                    require(bracket(grad['h'],gt) == 0,"FORCE_INTERNAL")
                    pf = dot(p,force)
                    for i in (1,2):
                        target = c*c/value['H']*force[i-1]
                        target -= c**4*p[i-1]*pf/(value['H']**3)
                        require(bracket(grad['V'+str(i)],gt) == target,
                                "FORCE_ACCELERATION")
                    counts['algebra'] += 1
                    counts['force'] += 1
            z = pack(g,pi,(0,0),(0,0),r,rho)
            for direction in ((1,0),(0,1),(1,1)):
                dz = (0,)*8+direction+(0,)*4
                hj = observables(tuple(Jet(v,d) for v,d in zip(z,dz)),c)['H']
                require(hj.c[1] == 0 and 2*hj.c[2]
                        == c*c/h0*dot(direction,direction),"REST_HESSIAN")
                counts['hessian'] += 1

    # Concrete new-model witness, independent of the fixture parametrization.
    w = pack(I,PISTAR,(0,0),(F(15,2),0),(1,0),(0,6))
    v,g = gradients(w)
    require((v['h'],v['H'],v['V1'],v['V2']) == (10,F(25,2),F(3,5),0),
            "MOVING_WITNESS")
    require(v['h']/v['H'] == F(4,5),"WITNESS_CLOCK")
    require(g['V1'][8] == F(32,625) and g['V2'][9] == F(2,25)
            and g['V1'][9] == 0 and g['V2'][8] == 0,"WITNESS_ACCELERATION")
    # Controls differentiate S from the actual internal canonical variables.
    wrong = []
    for sign in (F(0),F(-1)):
        wrong_v,wrong_g = gradients(w,spin_sign=sign)
        defect = bracket(wrong_g['K1'],wrong_g['K2'])+wrong_v['L']
        require(defect != 0,"NC_SPIN_OMITTED" if sign == 0 else "NC_SPIN_SIGN")
        wrong.append(defect)
    # For alpha=4 use a rational-root momentum, and the explicitly naive boost.
    wa = pack(I,PISTAR,(1,-2),(F(15,4),0),(1,0),(0,6))
    av,ag = gradients(wa,spin_sign=F(0),alpha=F(4))
    require(bracket(ag['K1'],ag['H']) == 4*av['P1']
            and bracket(ag['K1'],ag['H']) != av['P1'],"NC_UNSELECTED_ALPHA")

    # Old model: exact finite transport and internal-charge loss at the old rest data.
    for t in (F(1,10),F(1,4),F(1,2),F(1,5)):
        p = F(12)*t/(1-t*t)
        z = pack(I,PISTAR,(0,0),(p,0),(1,0),(0,6))
        oh = old_energy(z)
        oe = F(6)*(1+t*t)/(1-t*t)
        flow = canonical(scalar_gradient(old_energy,z))
        velocity = F(2)*t/(1+t*t)
        d = p*velocity
        require(oh == 4+oe and flow[6:8] == (velocity,0),"OLD_TRANSPORT")
        require(d > 0 and d == oe*velocity*velocity,"OLD_POSITIVE_D")
        zj = tuple(Jet(a,b) for a,b in zip(z,flow))
        _,jj,_ = internal(zj)
        jd = tuple(tuple(a.c[1] for a in row) for row in jj)
        require(jd == ((-d,0),(0,0)),"OLD_INTERNAL_LOSS")
        require(trace(jd) == -d,"OLD_TRACE_IDENTITY")
        require(trace(jd) != 0,"NC_OLD_FROZEN_TRACE")
        if t == F(1,5):
            require((p,oe,oh,velocity,d)
                    == (F(5,2),F(13,2),F(21,2),F(5,13),F(25,26)),
                    "OLD_RATIONAL_WITNESS")
        counts['old'] += 1
    require(nontrivial_clocks == 24,"NC_CLOCK_COUNT")
    print('ALGEBRA_CASES='+str(counts['algebra']))
    print('FORCE_CASES='+str(counts['force']))
    print('REST_HESSIAN_DIRECTIONS='+str(counts['hessian']))
    print('OLD_TRANSPORT_CASES='+str(counts['old']))
    print('NEGATIVE_CONTROLS=5')
    print('MOVING_WITNESS=10,25/2,3/5,4/5')
    print('ACCELERATION_WITNESS=32/625,2/25')
    print('RESULT=PASS')


if __name__ == '__main__':
    try:
        main()
    except Failure as exc:
        print('FALSIFIER='+str(exc))
        print('RESULT=FAIL')
        raise SystemExit(1)
    except Exception as exc:
        print('FALSIFIER=UNEXPECTED_'+type(exc).__name__)
        print('RESULT=FAIL')
        raise SystemExit(1)

