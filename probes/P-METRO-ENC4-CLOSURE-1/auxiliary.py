"""Exact finite observable-module and primary certificate data, standard library only."""
from fractions import Fraction as Q
from itertools import product
from math import gcd,lcm
from common import dump, require
import polynomial as poly

class M:
    """Rational matrices with explicit empty dimensions."""
    def __init__(self, rows, cols=None):
        self.v=tuple(tuple(Q(x) for x in row) for row in rows)
        self.n=len(self.v); self.m=len(self.v[0]) if self.n else (cols or 0)
        require(all(len(row)==self.m for row in self.v),'ragged matrix')
    def __eq__(self,other):
        return isinstance(other,M) and (self.n,self.m,self.v)==(other.n,other.m,other.v)
    def __add__(self,b):
        require((self.n,self.m)==(b.n,b.m),'matrix sum shape')
        return M([[self.v[i][j]+b.v[i][j] for j in range(self.m)] for i in range(self.n)],self.m)
    def __sub__(self,b): return self+b.scale(-1)
    def scale(self,c): return M([[c*x for x in row] for row in self.v],self.m)
    def __matmul__(self,b):
        require(self.m==b.n,'matrix product shape')
        return M([[sum((self.v[i][k]*b.v[k][j] for k in range(self.m)),Q(0))
                   for j in range(b.m)] for i in range(self.n)],b.m)
    def trans(self): return M([[self.v[i][j] for i in range(self.n)] for j in range(self.m)],self.n)
    def take(self,rows,cols):
        rows,cols=tuple(rows),tuple(cols)
        return M([[self.v[i][j] for j in cols] for i in rows],len(cols))
    def rref(self):
        rows=[list(row) for row in self.v]; pivots=[]; r=0
        for col in range(self.m):
            pivot=next((i for i in range(r,self.n) if rows[i][col]),None)
            if pivot is None: continue
            rows[r],rows[pivot]=rows[pivot],rows[r]
            x=rows[r][col]; rows[r]=[v/x for v in rows[r]]
            for i in range(self.n):
                if i!=r and rows[i][col]:
                    x=rows[i][col];rows[i]=[a-x*b for a,b in zip(rows[i],rows[r])]
            pivots.append(col);r+=1
            if r==self.n: break
        return M(rows,self.m),tuple(pivots)
    def rank(self): return len(self.rref()[1])
    def inv(self):
        require(self.n==self.m,'inverse shape')
        reduced,_=hcat(self,identity(self.n)).rref()
        require(reduced.take(range(self.n),range(self.n))==identity(self.n),'singular matrix')
        return reduced.take(range(self.n),range(self.n,2*self.n))
    def kernel(self):
        reduced,pivots=self.rref(); free=[j for j in range(self.m) if j not in pivots]
        out=[[Q(0) for _ in free] for _ in range(self.m)]
        for k,j in enumerate(free):
            out[j][k]=Q(1)
            for i,pivot in enumerate(pivots):out[pivot][k]=-reduced.v[i][j]
        return M(out,len(free))
    def serial(self):
        return {'rows':self.n,'cols':self.m,'data':[[str(x) for x in row] for row in self.v]}

def zeros(n,m=None):
    m=n if m is None else m
    return M([[0]*m for _ in range(n)],m)
def identity(n): return M([[int(i==j) for j in range(n)] for i in range(n)],n)
def hcat(*matrices):
    n=matrices[0].n
    require(all(m.n==n for m in matrices),'column join shape')
    return M([sum((list(m.v[i]) for m in matrices),[]) for i in range(n)],sum(m.m for m in matrices))
def basis(m):
    reduced,pivots=m.trans().rref()
    return reduced.take(range(len(pivots)),range(m.n)).trans()
def coordinates(b,v):
    if b.m==0:
        require(v==zeros(b.n,v.m),'vector outside zero module')
        return zeros(0,v.m)
    rows=b.trans().rref()[1]
    answer=b.take(rows,range(b.m)).inv() @ v.take(rows,range(v.m))
    require(b@answer==v,'vector outside module')
    return answer

def period(axis):
    n=len(axis[0]); adj=[set(f[i] for f in axis) for i in range(n)]
    reach=[]
    for i in range(n):
        found={i}; queue=[i]
        for u in queue:
            for v in sorted(adj[u]-found): found.add(v);queue.append(v)
        reach.append(found)
    todo=set(range(n)); classes=[]
    while todo:
        u=min(todo);component={v for v in todo if v in reach[u] and u in reach[v]}
        todo-=component
        if all(adj[v]<=component for v in component):classes.append(component)
    h=1
    for component in classes:
        root=min(component);depth={root:0};queue=[root]
        for u in queue:
            for v in sorted(adj[u]):
                if v not in depth:depth[v]=depth[u]+1;queue.append(v)
        g=0
        for u in component:
            for v in adj[u]:g=gcd(g,depth[u]+1-depth[v])
        require(g>0,'invalid recurrent period');h=lcm(h,g)
    return h

def charpoly(a):
    require(a.n==a.m,'characteristic shape')
    b=identity(a.n); coefficients=[Q(1)]
    for k in range(1,a.n+1):
        ab=a@b; coefficient=-sum((ab.v[i][i] for i in range(a.n)),Q(0))/k
        coefficients.append(coefficient);b=ab+identity(a.n).scale(coefficient)
    if a.n:require(b==zeros(a.n),'Cayley-Hamilton failure')
    return tuple(reversed(coefficients))
def evaluate(f,a):
    out=zeros(a.n)
    for c in reversed(f):out=(out@a)+identity(a.n).scale(c)
    return out

def modpower_x(k,f):
    result=poly.mod(poly.ONE,f);x=poly.mod((Q(0),Q(1)),f)
    while k:
        if k&1:result=poly.mod(poly.mul(result,x),f)
        k//=2
        if k:x=poly.mod(poly.mul(x,x),f)
    return result

def jordan(a,e,f,exponent):
    dim=e.rank();fa=evaluate(f,a);op=e;nullities=[0]
    for _ in range(exponent):
        op=fa@op;nullities.append(dim-op.rank())
    require(nullities[-1]==dim,'primary annihilator failure')
    degree=len(f)-1
    require(all((nullities[k]-nullities[k-1])%degree==0 for k in range(1,len(nullities))),
            'irreducible nullity divisibility')
    at_least=[(nullities[k]-nullities[k-1])//degree for k in range(1,len(nullities))]+[0]
    blocks=[{'size':k+1,'count_per_root':at_least[k]-at_least[k+1]}
            for k in range(exponent) if at_least[k]!=at_least[k+1]]
    require(all(x['count_per_root']>0 for x in blocks),'invalid Jordan partition')
    return {'nullities':nullities,'blocks':blocks}

def primary(a,h):
    if not a.n:return [],[]
    chi=charpoly(a); records=[];inside=[]
    for f,exponent in poly.factor(chi):
        modulus=poly.power(f,exponent);other,rem=poly.divmod_poly(chi,modulus)
        require(rem==poly.ZERO,'characteristic factor division')
        g,s,_=poly.xgcd(other,modulus)
        require(g==poly.ONE,'primary factors not coprime')
        e=evaluate(poly.mod(poly.mul(s,other),chi),a)
        require(e@e==e and e@a==a@e,'invalid primary projector')
        peripheral=poly.sub(modpower_x(h,f),poly.mod(poly.ONE,f))==poly.ZERO
        j=jordan(a,e,f,exponent)
        if peripheral:require(all(b['size']==1 for b in j['blocks']),'peripheral Jordan block')
        records.append({'factor':[str(c) for c in reversed(f)],'char_exponent':exponent,
                        'dimension':e.rank(),'projector':e.serial(),'peripheral':peripheral,**j})
        inside.append((f,exponent,e,peripheral))
    total=zeros(a.n)
    for i,(_,_,e,_) in enumerate(inside):
        total=total+e
        for _,_,other,_ in inside[:i]:require(e@other==zeros(a.n),'overlapping primary sectors')
    require(total==identity(a.n),'primary decomposition incomplete')
    return records,inside

def auxiliary(s):
    full=[]
    for axis in s.digits:
        full.append([M([[int(target==j) for j in range(s.n)] for target in mapping]) for mapping in axis])
    w=M(s.weights); b=basis(w)
    while True:
        extended=basis(hcat(b,*(m@b for axis in full for m in axis)))
        if extended.m==b.m:b=extended;break
        b=extended
    module_digits=[[coordinates(b,m@b) for m in axis] for axis in full]
    output_coordinates=coordinates(b,w)
    reachable=set(s.starts);queue=list(sorted(reachable))
    for state in queue:
        for axis in s.digits:
            for mapping in axis:
                target=mapping[state]
                if target not in reachable:reachable.add(target);queue.append(target)
    reachable=sorted(reachable)
    evaluation=b.take(reachable,range(b.m));kernel=basis(evaluation.kernel())
    d=b.m;k=kernel.m;change=kernel
    for j in range(d):
        column=identity(d).take(range(d),(j,))
        if hcat(change,column).rank()>change.m:change=hcat(change,column)
    require(change.m==d,'quotient complement incomplete')
    inv=change.inv();quotient_digits=[]
    for axis in module_digits:
        out=[]
        for m in axis:
            new=inv@m@change
            require(new.take(range(k,d),range(k))==zeros(d-k,k),'observable kernel not invariant')
            out.append(new.take(range(k,d),range(k,d)))
        quotient_digits.append(out)
    averages=[]
    for axis in quotient_digits:
        total=zeros(d-k)
        for m in axis:total=total+m
        averages.append(total.scale(Q(1,s.q)))
    for i,a in enumerate(averages):
        for other in averages[:i]:require(a@other==other@a,'quotient averages do not commute')
    axes=[];internals=[]
    for i,a in enumerate(averages):
        h=period(s.digits[i]);records,inside=primary(a,h)
        axes.append({'period_multiple':h,'average':a.serial(),'primary':records});internals.append(inside)
    sectors=[];total=zeros(d-k)
    if d-k:
        for indices in product(*(range(len(axis)) for axis in internals)):
            e=identity(d-k)
            for i,index in enumerate(indices):e=e@internals[i][index][2]
            dimension=e.rank()
            if not dimension:continue
            require(e@e==e,'joint projector invalid');total=total+e
            sector_axes=[]
            for i,index in enumerate(indices):
                f,exponent,_,_=internals[i][index]
                require(e@averages[i]==averages[i]@e,'joint sector not invariant')
                sector_axes.append(jordan(averages[i],e,f,exponent))
            sectors.append({'primary_indices':list(indices),'dimension':dimension,'projector':e.serial(),
                            'axes':sector_axes,'joint_peripheral':all(internals[i][j][3] for i,j in enumerate(indices))})
        require(total==identity(d-k),'joint decomposition incomplete')
    return {'schema':'metro-observable-primary-stdlib-v1','reachable':reachable,
            'module_dimension':d,'module_basis':b.serial(),'output_coordinates':output_coordinates.serial(),
            'module_digits':[[m.serial() for m in axis] for axis in module_digits],
            'kernel_dimension':k,'kernel_basis':kernel.serial(),'quotient_dimension':d-k,
            'basis_change':change.serial(),'quotient_output':(inv@output_coordinates).take(range(k,d),range(s.r)).serial(),
            'quotient_digits':[[m.serial() for m in axis] for axis in quotient_digits],
            'axes':axes,'joint_sectors':sectors}

def verify_auxiliary(s,record):
    require(dump(record)==dump(auxiliary(s)),'auxiliary module/spectral data mismatch')
