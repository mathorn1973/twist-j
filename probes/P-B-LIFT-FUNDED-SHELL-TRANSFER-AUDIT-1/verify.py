#!/usr/bin/env python3
"""Independent exact audit from PREREG only; no author implementation imported."""
from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import isqrt

Bf=((4,-2,2,-1),(-2,6,-1,3),(2,-1,2,0),(-1,3,0,2))
L=((1,-3,-1,-2),(-3,4,-2,1),(0,5,1,2),(5,-5,2,-1))
V=((1,2,1,2),(2,-1,2,-1),(0,-5,1,-3),(-5,5,-3,4))
A=((1,0,1,0),(0,1,0,1),(-2,1,-1,1),(1,-3,1,-2))
I=tuple(tuple(int(i==j) for j in range(4)) for i in range(4))
Y1=(0,0,-2,1); Y2=(2,-1,-4,2); ZERO=(0,0,0,0,0,0)

class ScientificFailure(Exception):
    pass

def require(value, label):
    if not value: raise ScientificFailure(label)

def transpose(m): return tuple(zip(*m))
def mv(m,v): return tuple(sum(a*b for a,b in zip(row,v)) for row in m)
def mm(m,n): return tuple(tuple(sum(a*b for a,b in zip(row,col)) for col in transpose(n)) for row in m)
def times(k,m): return tuple(tuple(k*v for v in row) for row in m)
def determinant(m):
    if not m: return 1
    return sum((-1)**j*m[0][j]*determinant(tuple(row[:j]+row[j+1:] for row in m[1:])) for j in range(len(m)))
def inverse(m):
    n=len(m); det=determinant(m)
    return tuple(tuple(Fraction((-1)**(i+j)*determinant(tuple(tuple(m[a][b] for b in range(n) if b!=i) for a in range(n) if a!=j)),det) for j in range(n)) for i in range(n))
def power(m,k):
    out=I
    for _ in range(k): out=mm(out,m)
    return out

def shell(y): return (y[0]+2*y[1])%5==0 and (y[2]+2*y[3])%5==0

def residue(y): return tuple(a%5 for a in y)

def S(y): return (-y[2],-y[3],-y[0],-y[1])

@lru_cache(maxsize=None)
def H(y):
    t=sum(a*b for a,b in zip(y,mv(Bf,y)))
    require(t%2==0,'F1 nonintegral H')
    return t//2

def hp(y):
    a,b,c,d=y
    return 2*a*a-2*a*b+3*b*b+c*c+d*d+2*a*c-a*d-b*c+3*b*d

def delta(y):
    a,b,c,d=y
    return (c-d)**2+d*d-(a-b)**2-b*b

def beta(cell): return S(cell[:4])+((-cell[4])%5,(-cell[5])%5)
def projection(cell):
    a,b,c,d,q,r=cell
    return residue((b,a,d,c,q,r))
def native_b(x):
    a,b,c,d,q,r=x
    return residue((-c,-d,-a,-b,-q,-r))
def native(x,n):
    a,b,c,d,q,r=x
    g=(sum(x)+2*(n.bit_count()%2))%5
    if g==0: y=(b,a,d,c,q,r)
    elif g==1: y=(-c,-d,-a,-b,-q,-r)
    elif g==2: y=(2-c,1-d+r,2-a,1-b-r,1-q,-r)
    elif g==3: y=(2-a,1-b,3-c,4-d,1-q,1-r)
    else: y=(2-a,1-b,3-c,4-d,2-q,1-r)
    return residue(y),g

# Complete state is (controller, bank, complete source, complete receiver).
def swap(state):
    c,b,s,r=state
    return c,b,r,s

def fund(state):
    c,b,s,r=state
    candidate=beta(r)
    available=b+H(r[:4])
    price=H(candidate[:4])
    if price>available: return state
    return c,available-price,s,candidate

def forward(state):
    c=state[0]
    t=swap(state) if c==0 else fund(state)
    return 1-c,t[1],t[2],t[3]

def backward(state):
    c,b,s,r=state
    t=(1-c,b,s,r)
    return swap(t) if t[0]==0 else fund(t)

def energy(state): return state[1]+H(state[2][:4])+H(state[3][:4])
def check_state(state):
    c,b,s,r=state
    require(c in (0,1) and b>=0,'F3 bad bank or phase')
    require(shell(s[:4]) and shell(r[:4]),'F3 lattice closure')
    require(all(0<=t<5 for t in s[4:]+r[4:]),'F3 fiber closure')

def audit_state(state):
    e=energy(state)
    require(swap(swap(state))==state,'F3 swap inverse')
    require(fund(fund(state))==state,'F3 funded inverse')
    fwd=forward(state); rev=backward(state)
    require(backward(fwd)==state and forward(rev)==state,'F3 full inverse')
    for t in (swap(state),fund(state),fwd,rev):
        check_state(t); require(energy(t)==e,'F3 energy')

def coefficient_points():
    basis=[tuple(int(i==j) for j in range(4)) for i in range(4)]
    return [(0,)*4]+basis+[tuple(a+b for a,b in zip(basis[i],basis[j])) for i in range(4) for j in range(i+1,4)]

def bounded_preimages(cap):
    inv=inverse(Bf)
    require(mm(Bf,inv)==I,'F1 rational inverse')
    limits=[]
    for i in range(4):
        bound=2*cap*inv[i][i]
        limits.append(isqrt(bound.numerator//bound.denominator))
    pts=tuple(u for u in product(*(range(-a,a+1) for a in limits)) if H(u)<=cap)
    return tuple(limits),pts

def main():
    require(all(determinant(tuple(tuple(Bf[i][j] for j in range(k)) for i in range(k)))>0 for k in range(1,5)),'F1 positivity')
    require(mm(V,L)==times(5,I) and mm(L,V)==times(5,I),'F1 L inverse')
    require(mm(transpose(L),mm(Bf,L))==times(5,Bf),'F1 L energy')
    smat=transpose(tuple(S(tuple(int(i==j) for j in range(4))) for i in range(4)))
    require(mm(smat,smat)==I,'F1 S involution')
    nums=mm(V,mm(smat,L)); require(all(v%5==0 for row in nums for v in row),'F1 integral BL')
    bl=tuple(tuple(v//5 for v in row) for row in nums)
    require(mm(bl,bl)==I and mm(L,bl)==mm(smat,L),'F1 conjugate')
    require(power(A,5)==I and mm(transpose(A),mm(Bf,A))==Bf,'F1 free phase')
    for y in coefficient_points():
        require(H(y)==hp(y) and H(S(y))-H(y)==delta(y),'F1 cost polynomial')
    print('PASS G1 exact matrices, quadratic cost, conjugate and positivity')
    n=0; gate=0
    for y in product(range(5),repeat=4):
        require(shell(y)==all(a%5==0 for a in mv(V,y)),'F1 image criterion')
        require(shell(y)==shell(S(y)),'F1 S closure')
        gate+=int(shell(y))
        for q,r in product(range(5),repeat=2):
            cell=y+(q,r)
            require(projection(beta(cell))==native_b(projection(cell)),'F1 native diagram')
            n+=1
    require(gate==25 and n==15625,'F1 residue inventory')
    print('PASS G1 residue image625, gate25, full projection checks15625')
    yb=(2,-1,0,0); ell=(2,-2,1,-1)
    require(H(yb)==15 and mv(Bf,yb)==tuple(5*t for t in ell),'F2 coset coefficients')
    for v in product(range(-2,3),repeat=4):
        y=tuple(a+5*b for a,b in zip(yb,v))
        require(H(y)==15+25*(H(v)+sum(a*b for a,b in zip(ell,v))),'F2 coset identity')
    bounds,us=bounded_preimages(4)
    fields=tuple(sorted(mv(L,u) for u in us))
    require(len(fields)==len(set(fields)),'F2 L injection')
    units=[u for u in us if H(u)==1]
    require(len(units)==20 and len({residue(mv(L,u)) for u in units})==20,'F2 units')
    minimizers=tuple(y for y in fields if residue(y)==(2,4,0,0) and H(y)==15)
    require(yb in minimizers and not any(residue(y)==(2,4,0,0) and H(y)<15 for y in fields),'F2 minimum')
    print('PASS G2 inverse-Gram bounds='+str(bounds)+' preimages='+str(len(us)))
    print('PASS G2 complete rho4 minimum15; minimizers='+str(minimizers))
    count=0; accepted=0; refused=0
    for ys in fields:
        hs=H(ys)
        for yr in fields:
            hr=H(yr)
            for bank in range(21-hs-hr):
                for c in (0,1):
                    state=(c,bank,ys+(1,2),yr+(3,4))
                    audit_state(state); count+=1
                    if H(S(yr))<=bank+hr: accepted+=1
                    else: refused+=1
    require(count>0 and accepted>0 and refused>0,'F3 empty branches')
    print('PASS G3 complete bounded pair states='+str(count)+' funded='+str(accepted)+' refused='+str(refused))
    fiber_count=0
    for q1,r1,q2,r2 in product(range(5),repeat=4):
        for y,b in ((Y1,10),(Y1,9),(Y2,30),(Y2,29),((0,)*4,0)):
            for c in (0,1):
                audit_state((c,b,Y2+(q1,r1),y+(q2,r2))); fiber_count+=1
    require(fiber_count==6250,'F3 fiber inventory')
    print('PASS G3 occupied and refusal fiber states6250')
    starts=((0,)*6,(3,1,2,4,0,0)); histories=[]; quotients=[]; finals=[]
    for seed,y,price,out_h in zip(starts,(Y1,Y2),(10,30),(15,35)):
        x=seed; hist=[x]; gens=[]
        for n in range(4): x,g=native(x,n); hist.append(x); gens.append(g)
        histories.append(tuple(hist)); quotients.append(tuple((sum(t)%5,t[4],t[5]) for t in hist))
        require(gens==[0,2,4,1],'F4 actual selectors')
        cell=y+(1,1)
        require(hist[3]==projection(cell) and hist[4]==projection(beta(cell)),'F4 native actual endpoint')
        require(H(y)==5 and delta(y)==price,'F4 source cost')
        initial=(0,30,cell,ZERO)
        transfer=forward(initial); final=forward(transfer)
        require(transfer==(1,30,ZERO,cell),'F4 full depletion/exchange')
        require(final==(0,30-price,ZERO,beta(cell)),'F4 executed endpoint')
        require(energy(initial)==energy(final)==35 and H(final[3][:4])==out_h,'F4 current energy read')
        require(projection(final[3])==hist[4],'F4 exact native reading')
        state=initial
        for n in range(1,9):
            state=forward(state)
            require(energy(state)==35,'F5 continuing energy')
            require((state==initial)==(n==8),'F5 exact nominated return')
        field=final[3][:4]
        for _ in range(5):
            field=mv(A,field); require(H(field)==out_h,'F5 selected free continuation')
        require(field==final[3][:4],'F5 five phase return')
        finals.append(final)
    require(quotients[0]==quotients[1],'F4 common native quotient history')
    for bank in range(41):
        matched=[]
        for y,d in ((Y1,10),(Y2,30)):
            cell=y+(1,1); initial=(0,bank,cell,ZERO)
            out=forward(forward(initial))
            expected=(0,bank-d,ZERO,beta(cell)) if bank>=d else (0,bank,ZERO,cell)
            require(out==expected,'F5 bank case')
            matched.append(out[3]==beta(cell))
        require(all(matched)==(bank>=30),'F5 sharp common bank')
    print('PASS G4 native two-source transfer: field15/35 bank20/0 total35')
    print('PASS G5 banks0..40, threshold30, nominated period8, free-phase control')
    c1=Y1+(1,1); c2=Y2+(1,1)
    require(H(swap((0,30,c1,ZERO))[3][:4])==H(swap((0,30,c2,ZERO))[3][:4])==5,'F5 omitted F')
    dirty=(0,30,c1,c2); require(swap(dirty)[2]==c2,'F5 dirty receiver retained')
    a=(0,30,c1,c1); b=(0,30,c1,c2)
    overwrite=lambda t:(t[0],t[1],t[2],t[2])
    require(a!=b and overwrite(a)==overwrite(b),'F5 copy-negative control')
    wrong=(0,40,ZERO,beta(c1))
    require(energy(wrong)!=energy((0,30,ZERO,c1)),'F5 wrong-bank negative control')
    print('PASS negative controls: omitted F, occupied overwrite, wrong bank sign')
    print('AUDIT PASS G1-G5; independent specification-only implementation')

if __name__=='__main__':
    try:
        main()
    except ScientificFailure as exc:
        print('FALSIFIER '+str(exc))
        print('AUDIT FAIL; frozen target and source retained')
