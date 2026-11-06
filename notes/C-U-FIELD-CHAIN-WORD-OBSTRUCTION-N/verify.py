#!/usr/bin/env python3
"""Exact finite self-audit. NON-CANONICAL; universal claims need PROOF.md."""
from itertools import product

A = ((1,0,1,0),(0,1,0,1),(-2,1,-1,1),(1,-3,1,-2))
L = ((1,-3,-1,-2),(-3,4,-2,1),(0,5,1,2),(5,-5,2,-1))
V = ((1,2,1,2),(2,-1,2,-1),(0,-5,1,-3),(-5,5,-3,4))
BF = ((4,-2,2,-1),(-2,6,-1,3),(2,-1,2,0),(-1,3,0,2))
K = ((6,2,-1,2),(2,6,2,-1),(-1,2,6,2),(2,-1,2,6))
C = ((1,-1),(-1,0),(0,1),(0,1))
D = ((1,1,1,0),(-1,-1,0,-1),(0,0,-1,1))
I = tuple(tuple(int(i == j) for j in range(4)) for i in range(4))
R = (1,-2,1,0)+(0,)*8
AM = (1,0,0,0)+(0,-1,0,0)+(0,-1,1,0)
ZM = (0,)*12

def tr(m): return tuple(zip(*m))
def mv(m,v): return tuple(sum(a*b for a,b in zip(row,v)) for row in m)
def mm(m,n): return tuple(tuple(sum(a*b for a,b in zip(row,col)) for col in tr(n)) for row in m)
def scale(k,m): return tuple(tuple(k*a for a in row) for row in m)
def add(u,v): return tuple(a+b for a,b in zip(u,v))
def sub(u,v): return tuple(a-b for a,b in zip(u,v))
def pw(m,n):
    out=I
    for _ in range(n): out=mm(out,m)
    return out

def H(y):
    a,b,c,d=y
    return 2*a*a-2*a*b+3*b*b+c*c+d*d+2*a*c-a*d-b*c+3*b*d

def Q(y): return sum(a*b for a,b in zip(y,mv(K,y)))
def residue(y): return tuple(a%5 for a in y)
def raw(y,sigma=(0,0)):
    a,b,c,d=y; u,v=sigma
    return (a-b+u,-a+u,b+v,b+u-v,c,d)

def split(z):
    e0,e1,e2,e3,c,d=z
    nums=(2*e0-3*e1+e2+e3,-e0-e1+2*e2+2*e3,
          5*c,5*d,2*e0+2*e1+e2+e3,e0+e1+3*e2-2*e3)
    if any(v%5 for v in nums): return None
    vals=tuple(v//5 for v in nums)
    return vals[:4],vals[4:]

def Hraw(z):
    e,m=z[:4],z[4:]
    return sum(v*v for v in z)+sum(a*b for a,b in zip(e,mv(C,m)))

def free(c,reverse=False):
    e,m=c[24:28],c[28:30]
    if reverse:
        m=add(m,mv(tr(C),e)); e=sub(e,mv(C,m))
    else:
        e=add(e,mv(C,m)); m=sub(m,mv(tr(C),e))
    return c[:24]+e+m+(c[30],)

def gate(c):
    """Literal funded G. Returns complete cell and actual forward R event."""
    m=c[:12]
    if m not in (R,AM): return c,0
    parts=split(c[24:30])
    if parts is None: return c,0
    y,sigma=parts
    if m==R:
        nums=mv(V,y)
        if any(v%5 for v in nums): return c,0
        x=tuple(v//5 for v in nums); h=H(x)
        funds=c[30]+4*h-2
        if funds<0: return c,0
        return AM+c[12:24]+raw(x,sigma)+(funds,),1
    h=H(y); funds=c[30]+2-4*h
    if funds<0: return c,0
    return R+c[12:24]+raw(mv(L,y),sigma)+(funds,),0

def fund(c,r): return c[:30]+(r,)

def step(state,cut=None,reverse=False):
    old,qs,p=state; cells=list(old); qs=list(qs); n=len(cells)
    if reverse:
        cells=[free(c,True) for c in cells]
        for j in reversed(range(n-1)):
            if j!=cut: cells[j+1],qs[j]=fund(cells[j+1],qs[j]),cells[j+1][30]
        for j in reversed(range(n-1)):
            if j!=cut: cells[j],qs[j]=fund(cells[j],qs[j]),cells[j][30]
        for i in reversed(range(n)):
            current=cells[i]; recovered,_=gate(current)
            if i==n-1 and recovered[:12]==R and current[:12]==AM: p=(p-1)%5
            cells[i]=recovered
    else:
        for i in range(n):
            cells[i],event=gate(cells[i])
            if i==n-1: p=(p+event)%5
        for j in range(n-1):
            if j!=cut: cells[j],qs[j]=fund(cells[j],qs[j]),cells[j][30]
        for j in range(n-1):
            if j!=cut: cells[j+1],qs[j]=fund(cells[j+1],qs[j]),cells[j+1][30]
        cells=[free(c) for c in cells]
    return tuple(cells),tuple(qs),p

def energy(state):
    cells,qs,p=state
    assert 0<=p<5 and all(q>=0 for q in qs)
    out=1+sum(qs)
    for c in cells:
        assert len(c)==31 and c[30]>=0
        out+=sum(Q(c[j:j+4]) for j in range(0,24,4))+Hraw(c[24:30])+c[30]
    return out

def accounts(state):
    out=[]
    for c in state[0]:
        sums=tuple(sum(c[4*j+i] for j in range(3)) for i in range(4))
        rho=(sum(c[:12])+sum(c[12:16]),sum(c[16:20]),sum(c[20:24]))
        div=mv(D,c[24:28])
        out.append((c[12:24],sums,rho,div,sub(div,rho)))
    return tuple(out)

def visible(state):
    """Everything except source active y; its static component stays included."""
    cells,qs,p=state
    parts=split(cells[0][24:30]); assert parts is not None
    return (cells[0][:24],parts[1],cells[0][30],cells[1:],qs,p)

def units():
    out=[]
    for a,b,s,t in product(range(-1,2),range(-1,2),range(-2,3),range(-2,3)):
        if 3*a*a+2*a*b+2*b*b+s*s+t*t!=4: continue
        if (s-2*a+b)%2 or (t+a-3*b)%2: continue
        out.append((a,b,(s-2*a+b)//2,(t+a-3*b)//2))
    return tuple(sorted(out))

def initial(w,n,mode):
    cells=[]
    source_funds=(0,3,100)[mode]
    for i in range(n):
        if i==0:
            m=R; z=raw(mv(L,w),(mode,-mode)); r=source_funds
        elif mode==0:
            m=R if i==n-1 else ZM; z=(0,)*6; r=0
        elif mode==1:
            m=AM if i==n-1 else R
            z=(1,0,0,0,1,-1) if i==n-1 else raw((0,0,1,0),(1,-1))
            r=7+i
        else:
            m=R if i==n-1 else ZM
            z=raw(mv(L,(0,0,i,1)),(i,-1)); r=30+i
        b=tuple((j+i)%3-1 for j in range(12)) if mode else (0,)*12
        cells.append(m+b+z+(r,))
    return tuple(cells),tuple(mode*(j+2) for j in range(n-1)),(4 if mode else 0)

def native(x,n):
    a,b,c,d,q,r=x; g=(sum(x)+2*(n.bit_count()%2))%5
    ys=((b,a,d,c,q,r),(-c,-d,-a,-b,-q,-r),
        (2-c,1-d+r,2-a,1-b-r,1-q,-r),
        (2-a,1-b,3-c,4-d,1-q,1-r),(2-a,1-b,3-c,4-d,2-q,1-r))
    return residue(ys[g])

def main():
    assert pw(A,5)==I and mm(A,L)==mm(L,A)
    assert mm(L,L)==scale(5,pw(A,3)) and mm(V,L)==scale(5,I) and mm(L,V)==scale(5,I)
    assert mm(tr(A),mm(BF,A))==BF and mm(tr(L),mm(BF,L))==scale(5,BF)
    assert mm(D,C)==((0,0),)*3
    print('PASS exact field algebra and energy certificates')
    x=(0,)*6; trajectory=[x]
    for n in range(4): x=native(x,n); trajectory.append(x)
    assert trajectory[3]==(0,0,1,3,1,1) and trajectory[4]==(4,2,0,0,4,4)
    for s,t in product(range(5),repeat=2):
        y=(3*s%5,s,3*t%5,t)
        orb={residue(mv(pw(A,k),y)) for k in range(5)}
        expect={(3*((s+k*t)%5)%5,(s+k*t)%5,3*t%5,t) for k in range(5)}
        assert orb==expect and len(orb)==(5 if t else 1)
    rho3=(0,0,3,1); rho4=(2,4,0,0)
    assert rho4 not in {residue(mv(pw(A,k),rho3)) for k in range(5)}
    print('PASS native boundary and all 25 residue orbits')
    y=(0,0,-2,1); illegal=(-y[2],-y[3],-y[0],-y[1])
    assert residue(illegal)==rho4 and H(y)==5 and H(illegal)==15
    assert residue(mv(A,y))==(3,1,3,1)
    print('PASS legal phase control and outside-alphabet boundary control')
    us=units(); assert len(us)==20 and all(H(w)==1 for w in us)
    assert len({residue(mv(L,w)) for w in us})==20
    steps=0; contexts=0
    for n,mode,cut in product((2,3),range(3),(None,0)):
        contexts+=1; reference=None
        for w in us:
            state=initial(w,n,mode); e=energy(state); acc=accounts(state)
            records=[visible(state)]
            for _ in range(24):
                nxt=step(state,cut)
                assert step(nxt,cut,True)==state
                assert energy(nxt)==e and accounts(nxt)==acc
                state=nxt; records.append(visible(state)); steps+=1
            if reference is None: reference=records
            else: assert records==reference
    assert contexts==12 and steps==5760
    print('PASS complete occupied chains: 20 seeds, 12 contexts, 5760 steps')
    print('PASS equal-energy source histories and full inverse/account checks')
    w=(0,0,1,0)
    low=step(initial(w,2,0)); high=step(initial(tuple(2*v for v in w),2,0))
    assert low[0][1][30]==2 and high[0][1][30]==14
    print('PASS different-energy receiver control: 2 versus 14')

if __name__=='__main__': main()
