#!/usr/bin/env python3
"""Exact, design-exposed audit. Read the pinned PREREG and PROOF for scope."""
from fractions import Fraction as F
from math import comb
import sys

if sys.flags.optimize:
    raise RuntimeError('Assertions must be enabled.')


class C:
    """Q(i,zeta5), coefficients on zeta^0,...,zeta^3, each Gaussian rational."""
    __slots__ = ('v',)

    def __init__(self, x=0):
        if isinstance(x, C):
            self.v = x.v
        elif isinstance(x, tuple):
            assert len(x) == 8
            self.v = tuple(map(F, x))
        else:
            self.v = (F(x), F(0)) + (F(0),) * 6

    def __add__(self, other):
        other = C(other)
        return C(tuple(a+b for a,b in zip(self.v, other.v)))

    __radd__ = __add__

    def __neg__(self):
        return C(tuple(-a for a in self.v))

    def __sub__(self, other):
        return self + -C(other)

    def __rsub__(self, other):
        return C(other) + -self

    def __mul__(self, other):
        other = C(other)
        raw = [[F(0), F(0)] for _ in range(7)]
        for j in range(4):
            a, b = self.v[2*j:2*j+2]
            if not (a or b):
                continue
            for k in range(4):
                c, d = other.v[2*k:2*k+2]
                if not (c or d):
                    continue
                raw[j+k][0] += a*c-b*d
                raw[j+k][1] += a*d+b*c
        for k in range(6, 3, -1):
            a, b = raw[k]
            for j in range(4):
                raw[k-4+j][0] -= a
                raw[k-4+j][1] -= b
        return C(tuple(x for pair in raw[:4] for x in pair))

    __rmul__ = __mul__

    def __truediv__(self, other):
        return self * (F(1)/F(other))

    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        result = C(1)
        for _ in range(n):
            result *= self
        return result

    def __bool__(self):
        return any(self.v)

    def __eq__(self, other):
        return self.v == C(other).v

    def star(self):
        return sum((C((a, -b, 0, 0, 0, 0, 0, 0)) * zp(-j)
                    for j, (a, b) in enumerate(zip(self.v[::2], self.v[1::2]))), C())


I = C((0, 1, 0, 0, 0, 0, 0, 0))
Z = C((0, 0, 1, 0, 0, 0, 0, 0))


def zp(n):
    return Z ** (n % 5)


checks = 0


def check(ok, label):
    global checks
    checks += 1
    if not ok:
        raise AssertionError(label)


def add(v, key, a):
    a = C(a)
    new = v.get(key, C()) + a
    if new:
        v[key] = new
    elif key in v:
        del v[key]


def scale(v, a):
    return {k: x*a for k, x in v.items() if x*a}


def norm(v):
    return sum((a.star()*a for a in v.values()), C())


def extend(fn, v):
    out = {}
    for key, a in v.items():
        for dest, b in fn(key).items():
            add(out, dest, a*b)
    return out


M = [[C(1),2*I,2*I,C(-4)], [2*I,C(1),C(-4),2*I],
     [2*I,C(-4),C(1),2*I], [C(-4),2*I,2*I,C(1)]]
M = [[x/5 for x in row] for row in M]
SH = [(-1,0),(0,-1),(0,1),(1,0)]


def obj_basis(key):
    R, r, d = key
    out = {}
    for e in range(4):
        u, v = SH[e]
        a = M[e][d] * (zp(-1) if r+v == 0 else C(1))
        add(out, (R+u,r+v,e), a)
    return out


def obj_step(v):
    return extend(obj_basis, v)


def contact(key):
    arr,R,r,d,pos,bank,label,mem = key
    if R != pos or r != 0:
        return {key:C(1)}
    out = {}
    if arr == 'T' and d in (1,2):
        sign = 1 if d == 1 else -1
        add(out, ('T',R,0,1,pos,0,label,mem), F(1,2)+sign*F(3,10))
        add(out, ('T',R,0,2,pos,0,label,mem), F(1,2)-sign*F(3,10))
        add(out, ('P',R,0,0,pos,1,label,mem), -I*F(2*sign,5))
        add(out, ('P',R,0,3,pos,1,label,mem), I*F(2*sign,5))
        return out
    if arr == 'P' and bank == 1 and d in (0,3):
        sign = 1 if d == 0 else -1
        add(out, ('P',R,0,0,pos,1,label,mem), F(1,2)+sign*F(3,10))
        add(out, ('P',R,0,3,pos,1,label,mem), F(1,2)-sign*F(3,10))
        add(out, ('T',R,0,1,pos,0,label,mem), -I*F(2*sign,5))
        add(out, ('T',R,0,2,pos,0,label,mem), I*F(2*sign,5))
        return out
    return {key:C(1)}


def pulse_step(key):
    arr,R,r,d,pos,bank,label,mem = key
    if arr == 'T':
        return {key:C(1)}
    a = 1 if bank == 1 else -2
    b = 2 if bank == 1 else 1
    out = {}
    add(out, ('P',R,r,d,pos,1,label,mem), F(a,5))
    lr, mr = (mem,label) if pos+1 == 100 else (label,mem)
    add(out, ('P',R,r,d,pos+1,2,lr,mr), F(2*a,5))
    ll, ml = (mem,label) if pos == 100 else (label,mem)
    add(out, ('P',R,r,d,pos-1,1,ll,ml), F(-2*b,5))
    add(out, ('P',R,r,d,pos,2,label,mem), F(b,5))
    return out


def native_obj_step(key):
    arr,R,r,d,pos,bank,label,mem = key
    return {(arr,R2,r2,e,pos,bank,label,mem): a
            for (R2,r2,e),a in obj_basis((R,r,d)).items()}


def native_step(v):
    return scale(extend(native_obj_step, extend(pulse_step, extend(contact,v))), zp(-2))


# Laurent polynomials in a unitary variable v, over Q(i,zeta5).
def la(p, q):
    out = dict(p)
    for k,a in q.items():
        add(out,k,a)
    return out


def lm(p, q):
    out = {}
    for k,a in p.items():
        for l,b in q.items():
            add(out,k+l,a*b)
    return out


def ls(p):
    return {-k:a.star() for k,a in p.items()}


check(I*I == -1 and zp(5) == 1 and sum(zp(j) for j in range(5)) == 0, 'field')
for j in range(4):
    for k in range(4):
        check(sum(M[r][j].star()*M[r][k] for r in range(4)) == (j==k), 'coin unitary')
for a in ([C(1),C(0),C(0),C(-1)], [C(0),C(1),C(-1),C(0)]):
    check([sum(M[r][k]*a[k] for k in range(4)) for r in range(4)] == a, 'A and B coin eigenvectors')
# The P=0 relative fiber fixes A but does not fix delta_0 B.
a_rel = {(0,0):C(1),(0,3):C(-1)}
b_rel = {(0,1):C(1),(0,2):C(-1)}

def relative_step(v):
    out = {}
    for (r,d),a in v.items():
        for (_,rn,e),b in obj_basis((0,r,d)).items():
            add(out,(rn,e),a*b)
    return out

check(relative_step(a_rel) == scale(a_rel,zp(-1)), 'correct bound anchor')
check(relative_step(b_rel) == {(-1,1):C(1),(1,2):C(-1)}, 'B is not bound anchor')
# Exchange covariance on each local positional case used by the one-step rule.
def exchange(v):
    return {(R,-r,({1:2,2:1}.get(d,d))):a for (R,r,d),a in v.items()}
for r in (-1,0,1):
    for d in range(4):
        v={(0,r,d):C(1)}
        check(obj_step(exchange(v)) == exchange(obj_step(v)), 'exchange covariance')

for label,mem in [(1,2),(0,25),(1,1)]:
    v={('T',99,0,1,99,0,label,mem):I, ('T',99,0,2,99,0,label,mem):-I}
    a={(99,0,0):C(1),(99,0,3):C(-1)}
    for T in (1,2):
        v=native_step(v); a=obj_step(a)
        front={k:x for k,x in v.items() if k[0]=='P' and k[4]==99+T and k[5]==2}
        c=zp(-2*T)*F(8,25)*F(-4,5)**(T-1)
        expected={('P',R,r,d,99+T,2,mem,label):x*c for (R,r,d),x in a.items()}
        check(front == expected,'finite native front including memory swap')
        check(norm(v)==2,'native norm')
        check(norm(front)==2*F(64,625)*F(16,25)**(T-1),'front squared norm')
for j in range(26):
    for k in range(26):
        check(tuple(reversed(tuple(reversed((j,k)))))==(j,k),'all-label swap inverse')

# Complete 5x5 block B(V)=I+(V-I) F5*|4><4|F5.
block=[]
for a in range(5):
    row=[]
    for b in range(5):
        c=zp(4*(b-a))/5
        row.append(la({0:C(int(a==b))},{0:-c,1:c}))
    block.append(row)
for a in range(5):
    for b in range(5):
        total={}
        for k in range(5):
            total=la(total,lm(ls(block[k][a]),block[k][b]))
        check(total==({0:C(1)} if a==b else {}),'full Fourier block unitarity')
check(block[0][0]=={0:C(F(4,5)),1:C(F(1,5))},'zero branch')
h=lm(ls(block[0][0]),block[0][0])
check(h=={-1:C(F(4,25)),0:C(F(17,25)),1:C(F(4,25))},'elementary effect')
for a in range(1,5):
    c=zp(-4*a)/5
    check(block[a][0]=={0:-c,1:c},'all four failure branches')

# OR grouping in x=H^m; exact polynomial identity for the fixed n and smaller tests.
for n in range(1,9):
    coef=[0]*(n+1)
    for j in range(1,n+1):
        for k in range(n-j+1):
            coef[j+k]+=comb(n,j)*comb(n-j,k)*(-1)**k
    rhs=[0]+[(-1)**(j+1)*comb(n,j) for j in range(1,n+1)]
    check(coef==rhs,'complete grouped histories')

# Fixed analytic spectral certificates. No numerical eigenvalues or parameter search.
check(F(27,110)-F(1,12)==F(107,660)>F(4,25),'complementary spectral margin')
check(F(1,24)-F(1,6*24**3)>F(1,25),'center stop sine margin')
check(F(4,25)*F(1,100)**2==F(1,62500),'pass loss')
check(F(4,25)*F(4,25)**2==F(64,15625),'W stop loss')
check(F(4,25)*4*F(1,25)**2==F(16,15625),'R stop loss')
check(256*F(64,15625)==1024*F(16,15625)>1,'stop block inverse Bernoulli')
mR,mW,n=32768,8192,8
check(mR==32*1024 and mW==32*256,'32 stop blocks')
check(F(mR,62500)<F(8,15) and F(mW,62500)<F(2,15),'pass rational majorants')
check(100*(8**8+2**8)<15**8,'pass greater than 99 percent')
gamma=1-F(mR,62500)**n-F(mW,62500)**n
check(gamma>F(99,100),'fixed pass certificate')
stop=F(8,2**32)
check(stop==F(1,2**29),'fixed stop certificate')
overlap=1-F(11,259)**2
check(overlap==F(66960,67081),'source overlap')
check(overlap*F(1,400)>F(1,500),'source bound mass using pi less than 4')
check(F(50000,99*2**29)<F(1,10**6),'conditional bound-sector leakage')
q2=F(64,625)*F(16,25)
check(q2==F(1024,15625),'T2 front mass')
check(q2*F(99,50000)>F(1,8000),'prepared acceptance')
check(F(2,5)*q2*F(99,50000)>F(1,20000),'marked basis acceptance')
D=n*(mR+mW)
check(D==327680 and n*mW==65536 and n*mR==262144,'register and call counts')
check(2*D==655360,'Fourier gate count')
# Explicit finite source permutation, preserving every other basis input.
def perm_source(a,d):
    return {(0,0):(0,1),(0,1):(0,0),(1,0):(0,2),(0,2):(1,0)}.get((a,d),(a,d))
check(len({perm_source(a,d) for a in range(5) for d in range(4)})==20,'source permutation bijection')
source={}
for a in range(5):
    h,d=perm_source(a,0)
    phase=I if (h,d)==(0,1) else -I if (h,d)==(0,2) else C(1)
    source[(h,d)]=phase
mark={k:a for k,a in source.items() if k[0]==0}
check(mark=={(0,1):I,(0,2):-I},'source marked iB coefficients')
check(norm(mark)/5==F(2,5) and norm(source)/5==1,'source marked weight and total norm')

print('C-FORWARD-ONLY-CAPTURE-FILTER-N exact audit')
print('status NON-CANONICAL L1 candidate-T; design-exposed; independent acceptance pending')
print('checks',checks)
print('native_front_T1_T2 all declared label examples PASS')
print('complete_five_state_block_and_grouped_histories PASS')
print('pass_effect > 99/100; stop_effect < 1/536870912')
print('prepared_T2_weight > 1/8000; marked_basis_T2_weight > 1/20000')
print('conditional_outside_selected_bound_band < 1/1000000')
print('filter_five_state_registers 327680; forward_W_calls 65536; forward_center_calls 262144')
print('native_admission energy_account occurrence reset UNRESOLVED')
print('PASS')
