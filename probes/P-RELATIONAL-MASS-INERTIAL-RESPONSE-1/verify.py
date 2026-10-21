#!/usr/bin/env python3
"""Exact prospective audit. NON-CANONICAL, L1; standard library only.

No differential-equation integration or floating point is used. Universal
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


def energy(z, kappa=F(3)):
    g, pi, _, p, r, rho = unpack(z)
    plus = tuple(a+b for a, b in zip(rho, p))
    minus = tuple(a-b for a, b in zip(rho, p))
    return (trace(mm(mm(mm(g, pi), g), pi))/2
            + (root(dot(plus, mv(g, plus)))
               + root(dot(minus, mv(g, minus))))/2
            + kappa*dot(r, mv(inv(g), r)))


def charge(z, full=True):
    g, pi, x, p, r, rho = unpack(z)
    j = add(scale(2, mm(g, pi)), outer(r, rho))
    return add(j, outer(x, p)) if full else j


def gradient(z):
    return tuple(energy(tuple(Jet(v, int(i == k)) for i, v in enumerate(z)))
                 .c[1] for k in range(14))


def canonical(grad):
    return (grad[3], grad[4]/2, grad[5], -grad[0], -grad[1]/2,
            -grad[2], grad[8], grad[9], -grad[6], -grad[7],
            grad[12], grad[13], -grad[10], -grad[11])


def explicit(z):
    g, pi, _, p, r, rho = unpack(z)
    plus = tuple(a+b for a, b in zip(rho, p))
    minus = tuple(a-b for a, b in zip(rho, p))
    ep = root(dot(plus, mv(g, plus)))
    em = root(dot(minus, mv(g, minus)))
    vp, vm = mv(g, plus), mv(g, minus)
    force = mv(inv(g), r)
    gd = mm(mm(g, pi), g)
    pid = add(scale(-1, mm(mm(pi, g), pi)),
              add(scale(F(-1, 4), add(scale(1/ep, outer(plus, plus)),
                                     scale(1/em, outer(minus, minus)))),
                  scale(3, outer(force, force))))
    return pack(gd, pid, tuple((a/ep-b/em)/2 for a,b in zip(vp,vm)),
                (0,0), tuple((a/ep+b/em)/2 for a,b in zip(vp,vm)),
                tuple(-6*a for a in force))


IDENTITY = ((F(1), F(0)), (F(0), F(1)))
ZERO = ((F(0), F(0)), (F(0), F(0)))
L_LIST = (((1,0),(0,1)), ((2,0),(0,1)), ((1,1),(0,1)),
          ((1,0),(1,1)), ((0,-1),(1,0)), ((2,1),(1,1)))
L_LIST = tuple(tuple(tuple(map(F,row)) for row in a) for a in L_LIST)
STREAMS = (((3,4),(5,12)), ((5,0),(-3,4)), ((0,2),(0,-3)),
           ((3,4),(-3,-4)))


def main():
    field_cases = hessian_cases = 0
    changed_internal = False
    for l in L_LIST:
        il = inv(l)
        g = mm(l, trans(l))
        pi = mm(mm(trans(il), ((F(1),F(-1)),(F(-1),F(2)))), il)
        r, x = mv(l, (F(2),F(-1))), mv(l, (F(1),F(3)))
        for q1, q2 in STREAMS:
            p1, p2 = mv(trans(il),q1), mv(trans(il),q2)
            p = tuple(a+b for a,b in zip(p1,p2))
            rho = tuple(a-b for a,b in zip(p1,p2))
            z = pack(g,pi,x,p,r,rho)
            require(g[0][0] > 0 and det(g) > 0, "DOMAIN")
            grad = gradient(z)
            flow = canonical(grad)
            require(flow == explicit(z), "HAMILTON_EQUATIONS")
            require(flow[8:10] == (0,0), "MOMENTUM")
            require(dot(grad,flow) == 0, "ENERGY")
            zj = tuple(Jet(v,d) for v,d in zip(z,flow))
            jdot = tuple(tuple(v.c[1] for v in row) for row in charge(zj))
            idot = tuple(tuple(v.c[1] for v in row) for row in charge(zj,False))
            require(jdot == ZERO, "FULL_CHARGE")
            require(idot == scale(-1,outer(flow[6:8],p)), "INTERNAL_CHARGE")
            changed_internal |= idot != ZERO
            field_cases += 1
        for q in ((3,4),(0,6),(5,12)):
            rho = mv(trans(il), q)
            z = pack(g,pi,x,(0,0),r,rho)
            e = root(dot(rho,mv(g,rho)))
            v = mv(g,rho)
            a = add(scale(1/e,g),scale(-1/(e*e*e),outer(v,v)))
            require(det(a) == 0 and trace(a) > 0, "HESSIAN_RANK")
            require(mv(a,rho) == (0,0), "HESSIAN_KERNEL")
            for direction in ((1,0),(0,1),(1,1)):
                dz = (0,)*8 + direction + (0,)*4
                ej = energy(tuple(Jet(v,d) for v,d in zip(z,dz)))
                require(ej.c[1] == 0, "ODD_P_TERM")
                require(2*ej.c[2] == dot(direction,mv(a,direction)),
                        "HESSIAN_COEFFICIENT")
                hessian_cases += 1

    jstar = ((F(0),F(4)),(F(-2),F(0)))
    pistar = ((F(0),F(-1)),(F(-1),F(0)))
    witness = pack(IDENTITY,pistar,(0,0),(0,0),(1,0),(0,6))
    require(energy(witness) == 10 and charge(witness) == jstar, "REST_DATA")
    for s in (F(1),F(2),F(3),F(-3)):
        z = pack(IDENTITY,pistar,(0,0),(0,s),(1,0),(0,6))
        require(energy(z) == 10 and charge(z) == jstar, "PARALLEL_FLAT")
    perpendicular = pack(IDENTITY,pistar,(0,0),(F(9,2),0),(1,0),(0,6))
    require(energy(perpendicular) == F(23,2), "TRANSVERSE_ENERGY")
    require(charge(perpendicular) == jstar, "TRANSVERSE_CHARGE")
    curvatures = []
    for direction in ((1,0),(0,1)):
        dz = (0,)*8 + direction + (0,)*4
        curvatures.append(2*energy(tuple(Jet(v,d) for v,d in zip(witness,dz))).c[2])
    require(curvatures == [F(1,6),F(0)], "WITNESS_HESSIAN")

    section_coefficients = []
    for c in (F(-1),F(0),F(1)):
        # Every coordinate is a full polynomial in the same parameter.
        z = (Jet(1),Jet(0),Jet(1),Jet(0),Jet(-1,0,-c/2),Jet(0),
             Jet(0),Jet(0,c),Jet(0,1),Jet(0),Jet(1),Jet(0),
             Jet(0),Jet(6,0,c))
        jj = charge(z)
        require(all(jj[i][j].c == (jstar[i][j],0,0)
                    for i in range(2) for j in range(2)), "SECTION_CHARGE")
        hj = energy(z)
        require(hj.c[:2] == (10,0) and hj.c[2] == 2*c+F(1,12),
                "SECTION_CURVATURE")
        section_coefficients.append(hj.c[2])
    require(section_coefficients == [F(-23,12),F(1,12),F(25,12)],
            "SECTION_DISTINCT")

    omega = ((F(0),F(-2)),(F(1),F(0)))
    require(mm(omega,omega) == scale(-2,IDENTITY), "GENERATOR_SQUARE")
    astar = ((F(1,6),F(0)),(F(0),F(0)))
    abar = scale(F(1,2),add(astar,
                 scale(F(1,2),mm(mm(omega,astar),trans(omega)))))
    gbar = scale(F(1,2),add(IDENTITY,
                 scale(F(1,2),mm(omega,trans(omega)))))
    require(abar == ((F(1,12),0),(0,F(1,24))), "MEAN_RESPONSE")
    require(gbar == ((F(3,2),0),(0,F(3,4)))
            and abar == scale(F(1,18),gbar), "MEAN_NORMALIZATION")
    cayley = scale(F(1,3),add(scale(-1,IDENTITY),scale(2,omega)))
    require(mm(mm(cayley,astar),trans(cayley))
            == scale(F(1,54),((F(1),F(-2)),(F(-2),F(4)))), "PHASE_RESPONSE")

    collapse_cases = 0
    last = None
    for eps in (F(3),F(-3),F(16,3),F(-16,3)):
        last = None
        for s in (F(1),F(1,2),F(1,4)):
            g = ((s*s,F(0)),(F(0),s**6))
            z = pack(g,ZERO,(0,-2/eps),(eps,0),(s*s,0),(0,4/(s*s)))
            h = energy(z)
            require(charge(z) == jstar, "COLLAPSE_CHARGE")
            require(h == s*root(eps*eps+16)+3*s*s, "COLLAPSE_ENERGY")
            require(h > 0 and (last is None or h < last), "COLLAPSE_ORDER")
            last = h
            collapse_cases += 1

    # Negative controls: each assertion rejects one explicitly false inference.
    require(changed_internal, "NC_FROZEN_INTERNAL_CHARGE")
    require(curvatures[0] != curvatures[1], "NC_SCALAR_HESSIAN")
    require(curvatures[1] == 0, "NC_POSITIVE_DEFINITE_HESSIAN")
    require(last < 10, "NC_OLD_MINIMUM")
    collapse = pack(((F(1,16),0),(0,F(1,4096))),ZERO,
                    (0,F(-2,3)),(3,0),(F(1,16),0),(0,64))
    require(charge(collapse,False) != jstar, "NC_OMITTED_CENTER_CHARGE")
    require(det(omega) == 2 and mv(trans(omega),(1,0)) != (0,0),
            "NC_MOVING_OLD_GENERATOR")
    require(len(set(section_coefficients)) == 3, "NC_UNIQUE_PREPARATION")
    print("FIELD_CASES=" + str(field_cases))
    print("HESSIAN_DIRECTIONS=" + str(hessian_cases))
    print("FIXED_CHARGE_WITNESSES=6")
    print("PREPARATION_SECTIONS=3")
    print("MEAN_AND_PHASE_CHECKS=4")
    print("COLLAPSE_CASES=" + str(collapse_cases))
    print("NEGATIVE_CONTROLS=7")
    print("REST_HESSIAN=1/6,0")
    print("RESULT=PASS")


if __name__ == "__main__":
    try:
        main()
    except Failure as exc:
        print("FALSIFIER=" + str(exc))
        print("RESULT=FAIL")
    except Exception as exc:
        print("FALSIFIER=UNEXPECTED_" + type(exc).__name__)
        print("RESULT=FAIL")
