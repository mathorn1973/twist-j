#!/usr/bin/env python3
"""Prospective closed-recoil audit. NON-CANONICAL, NEW_DECLARED L1.

Jet and matrix utilities adapted from P-RELATIONAL-MASS-BOOST-COMPLETION-1.
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
    """Coefficients through t^4, with exact rational formal arithmetic."""
    def __init__(self, a=0, b=0, c=0, d=0, e=0):
        self.c = (F(a), F(b), F(c), F(d), F(e))

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
                     for i in range(5)))

    __rmul__ = __mul__

    def reciprocal(self):
        require(self.c[0] != 0, "ZERO_DENOMINATOR")
        b = [1 / self.c[0]]
        for n in range(1, 5):
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
    b = [root(x.c[0])]
    for n in range(1,5):
        b.append((x.c[n]-sum(b[k]*b[n-k] for k in range(1,n)))/(2*b[0]))
    return Jet(*b)


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
    g,pi,_,_,r,rho = unpack(z)
    h = (trace(mm(mm(mm(g,pi),g),pi))/2
         + root(dot(rho,mv(g,rho)))+3*dot(r,mv(inv(g),r)))
    j = add(scale(2,mm(g,pi)),outer(r,rho))
    return h,j,j[0][1]-j[1][0]


def free(z,c=F(1),newton=False):
    h,j,s = internal(z)
    _,_,x,p,_,_ = unpack(z)
    big_h = h+c*c*dot(p,p)/(2*h) if newton else root(h*h+c*c*dot(p,p))
    rp = (-p[1],p[0])
    y = tuple(x[i]+c*c*s*rp[i]/(h*(big_h+h)) for i in range(2))
    k = tuple(big_h*x[i]/(c*c)-s*rp[i]/(big_h+h) for i in range(2))
    ell = x[0]*p[1]-x[1]*p[0]+s
    return dict(h=h,H=big_h,S=s,L=ell,K1=k[0],K2=k[1],
                Y1=y[0],Y2=y[1],X1=x[0],X2=x[1],P1=p[0],P2=p[1])


def rival(z,c=F(1)):
    h,_,_ = internal(z)
    _,_,_,p,_,_ = unpack(z)
    difference = h-10
    a = 1+difference*difference*difference/F(12250)
    return dict(h=h,H=root(h*h+c*c*a*dot(p,p)))


def gradients(function,z):
    values = function(z)
    result = {name:[] for name in values}
    for k in range(len(z)):
        zz = tuple(Jet(v,int(i == k)) for i,v in enumerate(z))
        for name,value in function(zz).items():
            result[name].append(lift(value).c[1])
    return values,{name:tuple(v) for name,v in result.items()}


def canonical14(a):
    return (a[3],a[4]/2,a[5],-a[0],-a[1]/2,-a[2],
            a[8],a[9],-a[6],-a[7],a[12],a[13],-a[10],-a[11])


def canonical(a):
    require(len(a) in (14,28),"CANONICAL_DIMENSION")
    return canonical14(a[:14])+(canonical14(a[14:]) if len(a) == 28 else ())


def pb(a,b):
    return dot(a,canonical(b))


def value0(x):
    return x.c[0] if isinstance(x,Jet) else F(x)


def exp_zero(x):
    """Exact formal exponential, admitted only when its constant is zero."""
    if not isinstance(x,Jet):
        require(x == 0,"EXP_CONSTANT")
        return F(1)
    require(x.c[0] == 0,"EXP_CONSTANT")
    b = [F(1)]
    for n in range(1,5):
        b.append(sum(k*x.c[k]*b[n-k] for k in range(1,n+1))/n)
    return Jet(*b)


def potential(displacement):
    q = dot(displacement,displacement)
    if value0(q) >= 1:
        return F(0)
    return 22*exp_zero(F(1,3)-q/(1-q))


def joint(z,c):
    a,b = z[:14],z[14:]
    ha,ja,_ = internal(a)
    hb,jb,_ = internal(b)
    _,_,xa,pa,_,_ = unpack(a)
    _,_,xb,pb_,_,_ = unpack(b)
    ea,eb = root(ha*ha+c*c*dot(pa,pa)),root(hb*hb+c*c*dot(pb_,pb_))
    v = potential(tuple(x-y for x,y in zip(xa,xb)))
    out = dict(H=ea+eb+v,HA=ha,HB=hb,EA=ea,EB=eb,V=v,
               P1=pa[0]+pb_[0],P2=pa[1]+pb_[1],
               VA1=c*c*pa[0]/ea,VA2=c*c*pa[1]/ea,
               VB1=c*c*pb_[0]/eb,VB2=c*c*pb_[1]/eb)
    for label,j in (('A',ja),('B',jb)):
        for i in range(2):
            for k in range(2):
                out['J'+label+str(i)+str(k)] = j[i][k]
    return out


I = ((F(1),F(0)),(F(0),F(1)))
PIA = ((F(0),F(-1)),(F(-1),F(0)))
PIB = ((F(0),F(-3)),(F(-3),F(0)))
ZA = pack(I,PIA,(0,0),(0,0),(1,0),(0,6))
ZB = pack(I,PIB,(0,0),(0,0),(2,0),(0,24))


def internal_states():
    l = ((F(1),F(1)),(F(0),F(1)))
    il = inv(l)
    transformed = pack(mm(l,trans(l)),mm(mm(trans(il),PIA),il),
                       (0,0),(0,0),mv(l,(1,0)),mv(trans(il),(0,6)))
    return ZA,ZB,transformed


def replace_center(z,x,p):
    g,pi,_,_,r,rho = unpack(z)
    return pack(g,pi,x,p,r,rho)


def main():
    directions = ((F(1),F(0)),(F(3,5),F(4,5)))
    centers = ((F(1),F(-2)),(F(-2),F(1)))
    free_cases = discriminator_cases = 0
    for initial in internal_states():
        h,_,_ = internal(initial)
        for c in (F(1),F(2)):
            for t in (F(0),F(1,4),F(1,2)):
                for direction,center in zip(directions,centers):
                    p = tuple(h/c*2*t/(1-t*t)*d for d in direction)
                    z = replace_center(initial,center,p)
                    value,grad = gradients(lambda z:free(z,c),z)
                    for i in (1,2):
                        for j in (1,2):
                            require(pb(grad['Y'+str(j)],grad['K'+str(i)])
                                    == value['Y'+str(i)]*p[j-1]/value['H'],
                                    "Y_BOOST_COVARIANCE")
                            require(pb(grad['Y'+str(i)],grad['P'+str(j)])
                                    == int(i == j),"Y_MOMENTUM")
                        require(pb(grad['Y'+str(i)],grad['H'])
                                == c*c*p[i-1]/value['H'],"Y_VELOCITY")
                    require(pb(grad['Y1'],grad['Y2'])
                            == c*c*value['S']/(h*value['H']),"Y_NONCANONICAL")
                    rp = (-p[1],p[0])
                    for i in (1,2):
                        require(value['K'+str(i)] == value['H']*value['Y'+str(i)]/(c*c)
                                -value['S']/h*rp[i-1],"Y_BOOST_REWRITE")
                    require(value['L'] == value['Y1']*p[1]-value['Y2']*p[0]
                            +value['H']/h*value['S'],"Y_ROTATION_REWRITE")
                    free_cases += 1
            z = replace_center(initial,(0,0),(0,0))
            dz = (0,)*8+(1,0)+(0,)*4
            zz = tuple(Jet(v,d) for v,d in zip(z,dz))
            er,en = free(zz,c)['H'],free(zz,c,True)['H']
            ar,an = 2*er.c[2],2*en.c[2]
            require(ar == an and ar == c*c/h,"SAME_REST_HESSIAN")
            require(h*24*er.c[4]/(3*ar*ar) == -1
                    and h*24*en.c[4]/(3*an*an) == 0,"FOURTH_DISCRIMINATOR")
            discriminator_cases += 1

    # One-point verification of the new second bound preparation.
    h,j,s = internal(ZB)
    require(h == 45 and j == ((0,42),(-6,0)) and s == 48,"BOUND_B_DATA")
    require(det(j)-trace(j)**2/4 == 252,"BOUND_B_CHARGE")
    a,b,u = F(24),F(18),F(3,4)
    cube_root = F(1,2)
    require(cube_root**3 == F(3)/a and b*b == a*a-252 and u == b/a,
            "BOUND_B_MINIMUM_PARAMETERS")
    require(2*cube_root+(a-b)*(1-a/b)/2 == 0,"BOUND_B_MINIMUM_DERIVATIVE")
    _,gb = gradients(lambda z:free(z),ZB)
    flow = canonical(gb['h'])
    omega = ((F(0),F(-7,2)),(F(1,2),F(0)))
    require(mm(omega,omega) == scale(F(-7,4),I),"BOUND_B_GENERATOR")
    g,pi,_,_,r,rho = unpack(ZB)
    expected = pack(add(mm(omega,g),mm(g,trans(omega))),
                    scale(-1,add(mm(trans(omega),pi),mm(pi,omega))),
                    (0,0),(0,0),mv(omega,r),tuple(-v for v in mv(trans(omega),rho)))
    require(flow == expected,"BOUND_B_RELATIVE_EQUILIBRIUM")

    contact_cases = outgoing_cases = rest_ratios = 0
    for c in (F(1),F(2)):
        for direction in directions:
            for moving in (False,True):
                momentum = F(24)/c if moving else F(0)
                pa = tuple(momentum*d for d in direction)
                pb_ = tuple(-v for v in pa)
                a = replace_center(ZA,tuple(d/4 for d in direction),pa)
                b = replace_center(ZB,tuple(-d/4 for d in direction),pb_)
                z = a+b
                value,grad = gradients(lambda z:joint(z,c),z)
                flow = canonical(grad['H'])
                fa = tuple(F(352,9)*d for d in direction)
                require(value['V'] == 22,"CONTACT_POTENTIAL")
                require(flow[8:10] == fa and flow[22:24] == tuple(-f for f in fa),
                        "CONTACT_EQUAL_OPPOSITE_FORCE")
                require(pb(grad['P1'],grad['H']) == 0
                        and pb(grad['P2'],grad['H']) == 0,"CONTACT_TOTAL_MOMENTUM")
                require(pb(grad['H'],grad['H']) == 0,"CONTACT_TOTAL_ENERGY")
                for name in ('HA','HB','JA00','JA01','JA10','JA11',
                             'JB00','JB01','JB10','JB11'):
                    require(pb(grad[name],grad['H']) == 0,"CONTACT_CONSERVED_"+name)
                for offset,label in ((0,'A'),(14,'B')):
                    ihflow = canonical(grad['H'+label])
                    clock = value['H'+label]/value['E'+label]
                    for index in (0,1,2,3,4,5,10,11,12,13):
                        require(flow[offset+index] == clock*ihflow[offset+index],
                                "CONTACT_INTERNAL_CLOCK")
                    velocity = tuple(value['V'+label+str(i)] for i in (1,2))
                    require(flow[offset+6:offset+8] == velocity,"CONTACT_CENTER_FLOW")
                if not moving:
                    aa = tuple(pb(grad['VA'+str(i)],grad['H']) for i in (1,2))
                    ab = tuple(pb(grad['VB'+str(i)],grad['H']) for i in (1,2))
                    require(aa == tuple(c*c/10*f for f in fa)
                            and ab == tuple(-c*c/45*f for f in fa),"REST_FORCE_ACCELERATION")
                    require(dot(direction,aa)/(-dot(direction,ab)) == F(9,2),
                            "REST_ACCELERATION_RATIO")
                    require(value['H'] == 77,"INITIAL_CLOSED_ENERGY")
                    rest_ratios += 1
                contact_cases += 1

            pa = tuple(F(24)/c*d for d in direction)
            a = replace_center(ZA,direction,pa)
            b = replace_center(ZB,tuple(-d for d in direction),tuple(-p for p in pa))
            value,grad = gradients(lambda z:joint(z,c),a+b)
            flow = canonical(grad['H'])
            require(value['V'] == 0 and value['EA'] == 26 and value['EB'] == 51
                    and value['H'] == 77,"OUTGOING_CLOSED_ENERGY")
            va = tuple(F(12,13)*c*d for d in direction)
            vb = tuple(F(-8,17)*c*d for d in direction)
            require(flow[6:8] == va and flow[20:22] == vb
                    and flow[8:10] == (0,0) and flow[22:24] == (0,0),"OUTGOING_FLOW")
            clocka,clockb = value['HA']/value['EA'],value['HB']/value['EB']
            require(clocka == F(5,13) and clockb == F(15,17),"OUTGOING_CLOCKS")
            speeda,speedb = dot(direction,va),-dot(direction,vb)
            require(speedb*clocka/(speeda*clockb) == F(2,9),"RECOIL_MASS_RATIO")
            require(speedb/speeda == F(26,51)
                    and speedb/speeda != F(2,9),"NC_RAW_SPEED_RATIO")
            outgoing_cases += 1

    value,grad = gradients(free,ZA)
    require(pb(grad['X2'],grad['K1']) == F(3,10)
            and value['X1']*value['P2']/value['H'] == 0,"NC_X_NOT_COVARIANT")
    require(pb(grad['Y1'],grad['Y2']) == F(3,50),"NC_Y_NOT_CANONICAL")
    moving = replace_center(ZA,(0,0),(F(15,2),0))
    vr,gr = gradients(free,moving)
    vn,gn = gradients(lambda z:free(z,newton=True),moving)
    require(vr['H'] == F(25,2) and vn['H'] == F(205,16)
            and gr['H'][8] == F(3,5) and gn['H'][8] == F(3,4),"NEWTON_COMPARISON")
    require(pb(gn['K1'],gn['H']) != vn['P1'],"NC_NEWTON_BOOST")
    require(vr['h']/vr['H'] == F(4,5)
            and canonical(gr['H'])[10:12] != canonical(gr['h'])[10:12],
            "NC_OMITTED_CLOCK")
    # One complete reference shell does not select the h-dependence of transport.
    rival_curvatures,original_curvatures = [],[]
    for initial in (ZA,ZB):
        dz = (0,)*8+(1,0)+(0,)*4
        zz = tuple(Jet(v,d) for v,d in zip(initial,dz))
        rival_curvatures.append(2*rival(zz)['H'].c[2])
        original_curvatures.append(2*free(zz)['H'].c[2])
    require(rival_curvatures == [F(1,10),F(1,10)]
            and original_curvatures == [F(1,10),F(1,45)],"REFERENCE_CURVATURES")
    vb,gb = gradients(rival,moving)
    require(vb['H'] == vr['H'] == F(25,2) and gb['H'] == gr['H'],
            "REFERENCE_FULL_FLOW")
    require(rival_curvatures[0]/rival_curvatures[1] == 1
            and original_curvatures[0]/original_curvatures[1] == F(9,2),
            "REFERENCE_RECOIL_DISCRIMINATOR")
    print('FREE_COVARIANT_CASES='+str(free_cases))
    print('FOURTH_DISCRIMINATORS='+str(discriminator_cases))
    print('BOUND_B_WITNESSES=1')
    print('CONTACT_CASES='+str(contact_cases))
    print('REST_ACCELERATION_RATIOS='+str(rest_ratios))
    print('OUTGOING_CASES='+str(outgoing_cases))
    print('REFERENCE_CALIBRATION_CASES=3')
    print('NEGATIVE_CONTROLS=5')
    print('RECOIL_MASS_RATIO_A_OVER_B=2/9')
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

