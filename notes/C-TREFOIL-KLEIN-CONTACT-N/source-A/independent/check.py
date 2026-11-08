#!/usr/bin/env python3
"""Independent exact checker, constructed only from the frozen PREREG.md.

No author source/results are read. All arithmetic uses stdlib Fraction.
Field inversion uses a rational 4-by-4 multiplication matrix, not symbolic CAS.
"""
from fractions import Fraction as Q
from math import comb
from pathlib import Path
import hashlib
import json
import platform
import sys
import time

PREREG = Path('/tmp/twistj-trefoil-coordinate-20261017/PREREG.md')
EXPECTED_HASH = 'd64ab46179bfe2acfaae3f61cbfdc9adc3c3c6a9e1048a92987d0e5bf7218053'
OUT = Path('/tmp/twistj-trefoil-coordinate-breaker-20261017')


def detq(m):
    m = [list(row) for row in m]
    value = Q(1)
    n = len(m)
    for k in range(n):
        pivot = next((i for i in range(k, n) if m[i][k]), None)
        if pivot is None:
            return Q(0)
        if pivot != k:
            m[pivot], m[k] = m[k], m[pivot]
            value = -value
        p = m[k][k]
        value *= p
        for i in range(k + 1, n):
            ratio = m[i][k] / p
            if ratio:
                for j in range(k + 1, n):
                    m[i][j] -= ratio * m[k][j]
    return value


class K:
    __slots__ = ('c',)

    def __init__(self, value=0):
        if isinstance(value, K):
            self.c = value.c
        elif isinstance(value, (list, tuple)):
            if len(value) != 4:
                raise ValueError('Field vectors require four coefficients')
            self.c = tuple(Q(x) for x in value)
        else:
            self.c = (Q(value), Q(0), Q(0), Q(0))

    def __bool__(self):
        return any(self.c)

    def __eq__(self, other):
        return self.c == K(other).c

    def __add__(self, other):
        other = K(other)
        return K(tuple(x+y for x,y in zip(self.c,other.c)))

    __radd__ = __add__

    def __neg__(self):
        return K(tuple(-x for x in self.c))

    def __sub__(self, other):
        return self + (-K(other))

    def __rsub__(self, other):
        return K(other) - self

    def __mul__(self, other):
        other = K(other)
        c = [Q(0)]*7
        for i,x in enumerate(self.c):
            if x:
                for j,y in enumerate(other.c):
                    if y:
                        c[i+j] += x*y
        for k in range(6,3,-1):
            if c[k]:
                for i in range(1,5):
                    c[k-i] -= c[k]
        return K(c[:4])

    __rmul__ = __mul__

    def inv(self):
        if not self:
            raise ZeroDivisionError('inverse of zero')
        columns = [(self * K(tuple(int(k==i) for k in range(4)))).c for i in range(4)]
        aug = [[columns[j][i] for j in range(4)]+[Q(i==0)] for i in range(4)]
        for k in range(4):
            pivot = next(i for i in range(k,4) if aug[i][k])
            aug[k],aug[pivot] = aug[pivot],aug[k]
            div = aug[k][k]
            aug[k] = [x/div for x in aug[k]]
            for i in range(4):
                if i != k and aug[i][k]:
                    ratio = aug[i][k]
                    aug[i] = [x-ratio*y for x,y in zip(aug[i],aug[k])]
        return K(tuple(aug[i][4] for i in range(4)))

    def __truediv__(self, other):
        return self * K(other).inv()

    def __rtruediv__(self, other):
        return K(other) / self

    def __pow__(self, n):
        if n < 0:
            return self.inv()**(-n)
        result,base = K(1),self
        while n:
            if n & 1:
                result = result*base
            base = base*base
            n //= 2
        return result

    def conjugate(self):
        return sum((self.c[k]*Z**(4*k) for k in range(4)),K())

    def norm(self):
        columns = [(self*Z**i).c for i in range(4)]
        return detq([[columns[j][i] for j in range(4)] for i in range(4)])

    def integral(self):
        return all(x.denominator == 1 for x in self.c)

    def mod_lambda(self):
        if not self.integral():
            raise ValueError('Nonintegral element in residue calculation')
        return sum(int(x) for x in self.c) % 5

    def valuation(self):
        if not self:
            return None
        n = self.norm()
        assert n != 0
        def ord5(x):
            x=abs(x)
            v=0
            while x % 5 == 0:
                x//=5
                v+=1
            return v
        return ord5(n.numerator)-ord5(n.denominator)

    def data(self):
        return [str(x) for x in self.c]


Z = K((0,1,0,0))
ONE = K(1)
ZERO = K()


def poly(terms):
    return {k:K(v) for k,v in terms.items() if K(v)}


def padd(*polynomials):
    result={}
    for p in polynomials:
        for monomial,c in p.items():
            result[monomial]=result.get(monomial,ZERO)+c
    return poly(result)


def pscale(p,c):
    c=K(c)
    return poly({k:v*c for k,v in p.items()})


def psub(p,q):
    return padd(p,pscale(q,-1))


def pmul(p,q):
    result={}
    for (i,j),c in p.items():
        for (k,l),d in q.items():
            m=(i+k,j+l)
            result[m]=result.get(m,ZERO)+c*d
    return poly(result)


def ppow(p,n):
    result={(0,0):ONE}
    while n:
        if n & 1:
            result=pmul(result,p)
        p=pmul(p,p)
        n//=2
    return result


def pdiff(p,axis):
    result={}
    for m,c in p.items():
        if m[axis]:
            n=list(m)
            n[axis]-=1
            result[tuple(n)]=c*m[axis]
    return poly(result)


def jac(p,q):
    return psub(pmul(pdiff(p,0),pdiff(q,1)),pmul(pdiff(p,1),pdiff(q,0)))


def hessian(p):
    return psub(pmul(pdiff(pdiff(p,0),0),pdiff(pdiff(p,1),1)),ppow(pdiff(pdiff(p,0),1),2))


def subst(p,A):
    """The column action: p(A00*u+A01*v, A10*u+A11*v)."""
    degree=max((max(i,j) for i,j in p),default=0)
    powers=[]
    for row in A:
        b=poly({(1,0):row[0],(0,1):row[1]})
        ps=[{(0,0):ONE}]
        for k in range(degree):
            ps.append(pmul(ps[-1],b))
        powers.append(ps)
    return padd(*(pscale(pmul(powers[0][i],powers[1][j]),c) for (i,j),c in p.items()))


def evalp(p,v):
    return sum((c*v[0]**i*v[1]**j for (i,j),c in p.items()),ZERO)


def pvaluation(p):
    return min(c.valuation() for c in p.values())


def residue(p):
    return {m:c.mod_lambda() for m,c in p.items() if c.mod_lambda()}


def pserial(p):
    return [{'u':i,'v':j,'coefficient':c.data()} for (i,j),c in sorted(p.items(),reverse=True)]


def mat(rows):
    return tuple(tuple(K(v) for v in row) for row in rows)


def mmul(A,B):
    return tuple(tuple(sum((a*b for a,b in zip(row,col)),ZERO) for col in zip(*B)) for row in A)


def mscale(A,c):
    return tuple(tuple(x*c for x in row) for row in A)


def mdet(A):
    return A[0][0]*A[1][1]-A[0][1]*A[1][0]


def minv(A):
    return mscale(mat([[A[1][1],-A[0][1]],[-A[1][0],A[0][0]]]),mdet(A).inv())


def dagger(A):
    return tuple(tuple(x.conjugate() for x in row) for row in zip(*A))


def mv(A,v):
    return tuple(sum((a*b for a,b in zip(row,v)),ZERO) for row in A)


def hermitian_value(M,v):
    return sum((x.conjugate()*y for x,y in zip(v,mv(M,v))),ZERO)


def field_rank(rows):
    a=[list(row) for row in rows]
    if not a:
        return 0
    pivotrow=0
    for col in range(len(a[0])):
        pivot=next((i for i in range(pivotrow,len(a)) if a[i][col]),None)
        if pivot is None:
            continue
        a[pivot],a[pivotrow]=a[pivotrow],a[pivot]
        d=a[pivotrow][col].inv()
        a[pivotrow]=[x*d for x in a[pivotrow]]
        for i in range(pivotrow+1,len(a)):
            if a[i][col]:
                factor=a[i][col]
                a[i]=[x-factor*y for x,y in zip(a[i],a[pivotrow])]
        pivotrow+=1
        if pivotrow==len(a):
            break
    return pivotrow


REPORT={
    'scope':'Independent NON-CANONICAL auxiliary exact verification; no public P-probe, no Canon changes',
    'implementation':{
        'field':'Q[z]/(1+z+z^2+z^3+z^4)',
        'basis':['1','z','z^2','z^3'],
        'arithmetic':'Python standard library fractions.Fraction; no floating point or CAS',
        'field_inverse':'4x4 rational multiplication-matrix Gaussian elimination',
        'valuation':'ord_5 of the exact field norm determinant',
        'polynomials':'sparse bivariate dictionaries; column action substitution',
        'independence':'Only frozen PREREG.md read; no author source or results accessed',
    },
    'environment':{'python':sys.version,'implementation':platform.python_implementation(),'machine':platform.machine(),'platform':platform.platform()},
    'checks':[],
}


def check(name,actual,expected,category):
    ok=actual==expected
    def serial(x):
        if isinstance(x,K): return x.data()
        if isinstance(x,tuple): return [serial(a) for a in x]
        if isinstance(x,list): return [serial(a) for a in x]
        if isinstance(x,dict):
            if any(isinstance(k,tuple) for k in x):
                return [{'monomial':list(k),'coefficient':serial(v)} for k,v in sorted(x.items())]
            return {k:serial(v) for k,v in x.items()}
        return x
    record={'name':name,'category':category,'pass':ok}
    if not ok or isinstance(actual,(int,str,list)):
        record.update(actual=serial(actual),expected=serial(expected))
    REPORT['checks'].append(record)
    if not ok:
        print('FAIL '+name,flush=True)
    return ok


def main():
    start=time.monotonic()
    prereg_hash=hashlib.sha256(PREREG.read_bytes()).hexdigest()
    REPORT['prereg_sha256']=prereg_hash
    REPORT['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    check('frozen prereg SHA-256',prereg_hash,EXPECTED_HASH,'input')
    if prereg_hash != EXPECTED_HASH:
        raise RuntimeError('Frozen prereg hash mismatch')
    # Independent arithmetic checks precede use for the target identities.
    check('Phi_5(z)=0',sum((Z**k for k in range(5)),ZERO),ZERO,'implementation self-check')
    check('z^5=1',Z**5,ONE,'implementation self-check')
    samples=[K(2)+Z,K((1,-3,2,5)),Z-Z**4,1-Z]
    for i,x in enumerate(samples):
        check(f'inverse multiplication {i}',x*x.inv(),ONE,'implementation self-check')
        check(f'conjugation involution {i}',x.conjugate().conjugate(),x,'implementation self-check')
        check(f'norm determinant versus conjugate product {i}',K(x.norm()),
              eval_field_product(x),'implementation self-check')
    print('Exact arithmetic self-checks complete',flush=True)

    a=Z+Z**4
    s=Z**2-Z**3
    r=Z-Z**4
    lam=1-Z
    J=1+Z**2
    scalar_targets=[('a^2+a=1',a**2+a,1),('s^2=a-2',s**2,a-2),('s^4=5a^2',s**4,5*a**2),
                    ('r=s/a',r,s/a),('a^2+s^2=-1',a**2+s**2,-1),('c(a)=a',a.conjugate(),a),
                    ('c(s)=-s',s.conjugate(),-s),('s=z^2 lambda',s,Z**2*lam),('J=a z',J,a*Z)]
    for name,x,y in scalar_targets:
        check(name,x,K(y),'F1')
    for name,x,target in [('lambda',lam,1),('s',s,1),('5',K(5),4)]:
        check(f'valuation({name})',x.valuation(),target,'F1')

    S=mat([[0,-1],[1,0]])
    T=mat([[Z,1],[0,Z**4]])
    P=mat([[1,-a],[0,s]])
    B=mat([[s,a],[0,1]])
    D=mat([[Z,0],[0,Z**4]])
    E=mat([[1/r,1/s],[1/s,-1/r]])
    I=mat([[1,0],[0,1]])
    Pinv=minv(P)
    for name,x,y in [
        ('det(P)=s',mdet(P),s),('det(B)=s',mdet(B),s),('B=s P^-1',B,mscale(Pinv,s)),
        ('P^-1 T P=D',mmul(mmul(Pinv,T),P),D),('P^-1 S P=E',mmul(mmul(Pinv,S),P),E),
        ('B T=D B',mmul(B,T),mmul(D,B)),('B S=E B',mmul(B,S),mmul(E,B)),
        ('det(D)=1',mdet(D),ONE),('det(E)=1',mdet(E),ONE),('E^2=-I',mmul(E,E),mscale(I,-1)),
        ('D dagger D=I',mmul(dagger(D),D),I),('E dagger E=I',mmul(dagger(E),E),I),
        ('P Pinv=I',mmul(P,Pinv),I),('Pinv P=I',mmul(Pinv,P),I),
    ]:
        check(name,x,y,'F1')

    f0=poly({(11,1):1,(6,6):11,(1,11):-1})
    H0=poly({(20,0):-1,(0,20):-1,(15,5):228,(5,15):-228,(10,10):-494})
    W0=poly({(30,0):1,(0,30):1,(25,5):522,(5,25):-522,(20,10):-10005,(10,20):-10005})
    check('standard Klein relation residual',psub(padd(ppow(W0,2),ppow(H0,3)),pscale(ppow(f0,5),1728)),{},'F3')
    check('standard Hessian residual',psub(hessian(f0),pscale(H0,121)),{},'F3')
    check('standard Jacobian residual',psub(jac(f0,H0),pscale(W0,20)),{},'F3')
    for name,p in [('f0',f0),('H0',H0),('W0',W0)]:
        for gen,A in [('D',D),('E',E)]:
            check(f'{name} invariant under {gen}',psub(subst(p,A),p),{},'F2')
    print('Scalar, matrix, standard-form identities complete',flush=True)

    fhat,Hhat,What=(subst(p,B) for p in (f0,H0,W0))
    F,H,W=(pscale(p,s**(-k)) for p,k in [(fhat,10),(Hhat,20),(What,25)])
    allforms={'fhat':fhat,'Hhat':Hhat,'What':What,'F':F,'H':H,'W':W}
    vals=[]
    for name,p in allforms.items():
        check(f'{name} has globally integral coefficients',all(c.integral() for c in p.values()),True,'F2')
        for gen,A in [('S',S),('T',T)]:
            check(f'{name} invariant under column {gen}',psub(subst(p,A),p),{},'F2')
        vals.append(pvaluation(p))
    check('all six exact coefficient valuations',vals,[10,20,25,0,0,0],'F4')
    check('unscaled marked Klein residual',psub(padd(ppow(What,2),ppow(Hhat,3)),pscale(ppow(fhat,5),1728)),{},'F3')
    check('primitive marked Klein residual',psub(padd(ppow(W,2),pscale(ppow(H,3),s**10)),pscale(ppow(F,5),1728)),{},'F3')
    check('primitive marked Jacobian residual',psub(W,pscale(jac(F,H),a*a/4)),{},'F3')
    E6=poly({(5,1):1,(1,5):-1})
    D20=padd(ppow(poly({(5,0):1,(1,4):-1}),4),poly({(0,20):1}))
    for name,p,q in [('F',F,pscale(ppow(E6,2),2)),('H',H,pscale(D20,4)),('W',W,pscale(ppow(E6,5),4))]:
        check(f'{name} exact reduction',residue(p),residue(q),'F4')

    fK,HK,WK=pscale(F,s**-2),H,pscale(W,s**-5)
    for name,p,q in [('fK',fK,f0),('HK',HK,H0),('WK',WK,W0)]:
        check(f'{name} equals pullback by Pinv',psub(p,subst(q,Pinv)),{},'F3')
    check('normalized K-valued relation residual',psub(padd(ppow(WK,2),ppow(HK,3)),pscale(ppow(fK,5),1728)),{},'F3')
    check('K-valued coefficient valuations',[pvaluation(p) for p in (fK,HK,WK)],[-2,0,-5],'F4')
    print('Marked invariance, integrality, exact valuations and reductions complete',flush=True)

    v0=(-a,Z**2)
    M=mat([[1,a/s],[-a/s,1]])
    for name,x,y in [
        ('B v0=z^2 (J,1)',mv(B,v0),(Z**2*J,Z**2)),('f0(J,1)=0',evalp(f0,(J,ONE)),ZERO),
        ('F(v0)=0',evalp(F,v0),ZERO),('M=Pinv dagger Pinv',M,mmul(dagger(Pinv),Pinv)),
        ('M dagger=M',dagger(M),M),('det(M)=-1/s^2',mdet(M),-s**-2),
        ('trace(M)=2',M[0][0]+M[1][1],K(2)),('S dagger M S=M',mmul(mmul(dagger(S),M),S),M),
        ('T dagger M T=M',mmul(mmul(dagger(T),M),T),M),('v0 dagger M v0=1',hermitian_value(M,v0),ONE),
    ]:
        check(name,x,y,'F5')

    # Verify dimensions without enumerating the group: D invariance leaves at
    # most seven monomials; exact ranks enforce E invariance on those columns.
    dimensions={}
    for degree in (12,20,30):
        exponents=[i for i in range(degree+1) if (2*i-degree)%5==0]
        columns=[psub(subst(poly({(i,degree-i):1}),E),poly({(i,degree-i):1})) for i in exponents]
        rows=[[col.get((i,degree-i),ZERO) for col in columns] for i in range(degree+1)]
        rank=field_rank(rows)
        dim=len(columns)-rank
        dimensions[str(degree)]={'D_allowed_x_exponents':exponents,'E_constraint_rank':rank,'dimension':dim}
        check(f'invariant space dimension degree {degree}',dim,1,'F6')

    # Explicit independence witness needed by the normalization obstruction.
    h3at10=evalp(H0,(ONE,ZERO))**3
    w2at10=evalp(W0,(ONE,ZERO))**2
    h3at11=evalp(H0,(ONE,ONE))**3
    w2at11=evalp(W0,(ONE,ONE))**2
    witness=h3at10*w2at11-h3at11*w2at10
    check('H0^3 and W0^2 independent witness nonzero',bool(witness),True,'F6')

    REPORT['constants']={name:x.data() for name,x in [('z',Z),('lambda',lam),('a',a),('s',s),('r',r),('J',J)]}
    REPORT['polynomials']={name:pserial(p) for name,p in {**allforms,'fK':fK,'HK':HK,'WK':WK}.items()}
    REPORT['reductions']={name:[{'u':i,'v':j,'coefficient_mod_5':c} for (i,j),c in sorted(residue(p).items(),reverse=True)] for name,p in [('F',F),('H',H),('W',W)]}
    REPORT['coefficient_valuations']={name:[{'u':i,'v':j,'valuation':c.valuation()} for (i,j),c in sorted(p.items(),reverse=True)] for name,p in allforms.items()}
    REPORT['invariant_space_dimensions']=dimensions
    REPORT['independence_witness']={'points':['(1,0)','(1,1)'],'determinant':witness.data()}
    REPORT['failures']=[c['name'] for c in REPORT['checks'] if not c['pass']]
    REPORT['pass']=not REPORT['failures']
    REPORT['exit_status']=0 if REPORT['pass'] else 1
    (OUT/'report.json').write_text(json.dumps(REPORT,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'pass':REPORT['pass'],'checks':len(REPORT['checks']),'failures':REPORT['failures'],'source_sha256':REPORT['source_sha256']},sort_keys=True),flush=True)
    return REPORT['exit_status']


def eval_field_product(x):
    """Second norm route: product over the four embeddings z -> z^i."""
    product=ONE
    for i in (1,2,3,4):
        product*=sum((x.c[k]*Z**(i*k) for k in range(4)),ZERO)
    return product


if __name__=='__main__':
    sys.exit(main())
