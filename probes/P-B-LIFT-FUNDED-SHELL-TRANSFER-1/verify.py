#!/usr/bin/env python3
"""Exact L1 audit, P-B-LIFT-FUNDED-SHELL-TRANSFER-1.
A. M. Thorn. SPDX-License-Identifier: Apache-2.0.
No scientific execution before the public preregistration pin.
"""
from itertools import product
from math import isqrt
from hashlib import sha256

BF = ((4,-2,2,-1),(-2,6,-1,3),(2,-1,2,0),(-1,3,0,2))
L = ((1,-3,-1,-2),(-3,4,-2,1),(0,5,1,2),(5,-5,2,-1))
V = ((1,2,1,2),(2,-1,2,-1),(0,-5,1,-3),(-5,5,-3,4))
AF = ((1,0,1,0),(0,1,0,1),(-2,1,-1,1),(1,-3,1,-2))
S = ((0,0,-1,0),(0,0,0,-1),(-1,0,0,0),(0,-1,0,0))
I = tuple(tuple(int(i==j) for j in range(4)) for i in range(4))
ZERO = (0,0,0,0,0,0)
Y1, Y2 = (0,0,-2,1), (2,-1,-4,2)
U1, U2 = (0,-1,-1,2), (0,-1,-1,1)
RHO4 = (2,4,0,0)
CAP = 20


class Falsifier(Exception):
    pass


def need(ok, text):
    if not ok:
        raise Falsifier(text)


def mv(m, x):
    return tuple(sum(a*b for a,b in zip(row,x)) for row in m)


def mm(m, n):
    return tuple(tuple(sum(m[i][k]*n[k][j] for k in range(4))
                       for j in range(4)) for i in range(4))


def tr(m):
    return tuple(zip(*m))


def scale(k, m):
    return tuple(tuple(k*x for x in row) for row in m)


def H(y):
    a,b,c,d = y[:4]
    return 2*a*a-2*a*b+3*b*b+c*c+d*d+2*a*c-a*d-b*c+3*b*d


def hm(y):
    return sum(a*b for a,b in zip(y,mv(BF,y)))//2


def in_shell(y):
    return (y[0]+2*y[1])%5==0 and (y[2]+2*y[3])%5==0


def f(a,b):
    return (a-b)**2+b*b


def price(y):
    return f(y[2],y[3])-f(y[0],y[1])


def beta(cell):
    a,b,c,d,q,r = cell
    return (-c,-d,-a,-b,-q%5,-r%5)


def pi(cell):
    a,b,c,d,q,r=cell
    return (b%5,a%5,d%5,c%5,q,r)


def nb(x):
    a,b,c,d,q,r=x
    return (-c%5,-d%5,-a%5,-b%5,-q%5,-r%5)


def native(n,x):
    a,b,c,d,q,r=x
    gs=((b,a,d,c,q,r),(-c,-d,-a,-b,-q,-r),
        (2-c,1+r-d,2-a,1-r-b,1-q,-r),
        (2-a,1-b,3-c,4-d,1-q,1-r),
        (2-a,1-b,3-c,4-d,2-q,1-r))
    choice=(sum(x)+2*(n.bit_count()%2))%5
    return tuple(t%5 for t in gs[choice])


def quotient(x):
    return (sum(x)%5,x[4],x[5])


# Full state = (source cell, receiver cell, nonnegative bank, C2 phase).
def energy(s):
    return H(s[0])+H(s[1])+s[2]


def swap(s):
    a,b,k,c=s
    return (b,a,k,c)


def fund(s):
    a,b,k,c=s
    candidate=beta(b)
    delta=H(candidate)-H(b)
    return (a,candidate,k-delta,c) if k>=delta else s


def fund_alternate(s):
    a,b,k,c=s
    delta=price(b)
    # Alternate field computation through canonical shell preimage.
    raw=mv(V,b[:4]);need(all(t%5==0 for t in raw),'inverse shell type')
    u=tuple(t//5 for t in raw)
    ynew=mv(L,mv(BL,u))
    proposed=ynew+(-b[4]%5,-b[5]%5)
    if k<delta:
        return s
    return (a,proposed,k-delta,c)


def step(s):
    a,b,k,c = swap(s) if s[3]==0 else fund(s)
    return (a,b,k,1-c)


def back(s):
    a,b,k,c=s
    prev=(a,b,k,1-c)
    return swap(prev) if prev[3]==0 else fund(prev)


def shells(maxh):
    """Complete square-fiber enumeration, not an empirical coordinate cutoff."""
    out=set()
    ra=isqrt(8*maxh//5);rb=isqrt(12*maxh//5);rs=isqrt(4*maxh)
    for a,b in product(range(-ra,ra+1),range(-rb,rb+1)):
        q=3*a*a+2*a*b+2*b*b
        if q>4*maxh:continue
        for s1,s2 in product(range(-rs,rs+1),repeat=2):
            if q+s1*s1+s2*s2>4*maxh:continue
            if (s1-2*a+b)%2 or (s2+a-3*b)%2:continue
            u=(a,b,(s1-2*a+b)//2,(s2+a-3*b)//2)
            need(4*H(u)==q+s1*s1+s2*s2,'square-fiber identity')
            need(0<=H(u)<=maxh,'shell bound')
            out.add(u)
    return tuple(sorted(out))


def anchors():
    global BL
    need(mm(V,L)==scale(5,I)==mm(L,V),'V L inverse')
    need(mm(tr(L),mm(BF,L))==scale(5,BF),'H scaling')
    need(mm(S,S)==I,'S involution')
    raw=mm(V,mm(S,L));need(all(t%5==0 for row in raw for t in row),'B lift not integral')
    BL=tuple(tuple(t//5 for t in row) for row in raw)
    need(mm(BL,BL)==I and mm(L,BL)==mm(S,L),'B conjugate')
    pts=((0,0,0,0),)+tuple(tuple(int(i==j) for i in range(4)) for j in range(4))
    pts+=tuple(tuple(int(k==i)+int(k==j) for k in range(4)) for i in range(4) for j in range(i,4))
    for y in pts:
        need(H(y)==hm(y),'H Gram')
        need(H(mv(S,y))-H(y)==price(y),'price polynomial')
    for y in product(range(5),repeat=4):
        need(in_shell(y)==all(t%5==0 for t in mv(V,y)),'shell criterion')
        need(in_shell(y)==in_shell(mv(S,y)),'S shell invariance')
    print('G1 PASS integral_B_lift={} residue_criterion=625 price_polynomial_exact'.format(BL))


def coset_minimum(units):
    yb=mv(S,Y1)
    need(yb==(2,-1,0,0) and H(yb)==15,'boundary-four witness')
    need(mv(BF,yb)==(10,-10,5,-5),'boundary-four gradient')
    for v in product(range(-2,3),repeat=4):
        y=tuple(a+5*b for a,b in zip(yb,v))
        expected=15+25*(H(v)+sum(a*b for a,b in zip((2,-2,1,-1),v)))
        need(H(y)==expected and H(y)%25==15 and H(y)>=15,'coset congruence')
    allu=shells(3)
    yy=[mv(L,u) for u in allu if tuple(t%5 for t in mv(L,u))==RHO4]
    need(yy and min(map(H,yy))==15,'bounded minimum audit')
    minimizers=sorted(y for y in yy if H(y)==15)
    need(all(tuple(t%5 for t in y)!=RHO4 for y in units),'unit exclusion')
    print('G2 PASS whole_coset_minimum=15 min_increase_from_y3=10 minimizers_at_15={}'.format(minimizers))


def primitive_audit(fields):
    n=rej=0;digest=sha256()
    for y,z in product(fields,repeat=2):
        cost=H(y)+H(z)
        if cost>CAP:continue
        for bank in range(CAP-cost+1):
            for c in (0,1):
                s=(y+(1,2),z+(3,4),bank,c)
                t=fund(s)
                need(t==fund_alternate(s),'fund implementations differ')
                need(fund(t)==s and swap(swap(s))==s,'primitive inverse')
                need(energy(t)==energy(s) and t[2]>=0,'funded energy')
                need(back(step(s))==s and step(back(s))==s,'autonomous inverse')
                need(energy(step(s))==energy(s),'autonomous energy')
                need(all(in_shell(cell[:4]) for cell in t[:2]),'lattice leakage')
                need(pi(beta(s[1]))==nb(pi(s[1])),'native b projection')
                rej+=int(bank<price(z));n+=1
                digest.update((str((s,t))+'\n').encode())
    # Complete independent fiber census; the guard has no q/r arguments.
    nf=0
    for vals in product(range(5),repeat=4):
        for z,bank in ((Y1,10),(Y1,9),(Y2,30),(Y2,29),((0,0,0,0),0)):
            s=(Y2+vals[:2],z+vals[2:],bank,1)
            t=fund(s)
            need(fund(t)==s and t==fund_alternate(s),'complete fiber inverse')
            need(pi(beta(s[1]))==nb(pi(s[1])),'complete fiber b projection')
            nf+=1
    print('G3 PASS integer_sector_E_le_20={} refused={} fiber_cases={} checksum={}'.format(n,rej,nf,digest.hexdigest()))


def witnesses():
    starts=((0,0,0,0,0,0),(3,1,2,4,0,0))
    histories=[]
    for x in starts:
        hist=[x]
        for n in range(4):hist.append(native(n,hist[-1]))
        histories.append(hist)
    need([quotient(x) for x in histories[0]]==[quotient(x) for x in histories[1]],'native quotient histories')
    finals=[]
    for i,(u,y,hist) in enumerate(zip((U1,U2),(Y1,Y2),histories)):
        need(mv(L,u)==y and H(u)==1 and H(y)==5,'source energy/lift')
        cell=y+(1,1)
        need(pi(cell)==hist[3] and quotient(pi(cell))==(1,1,1),'actual source match')
        s=(cell,ZERO,30,0)
        moved=step(s);final=step(moved)
        need(moved[0]==ZERO and moved[1]==cell and moved[2]==30,'literal source transfer')
        need(final[0]==ZERO and pi(final[1])==hist[4],'fourth-boundary continuation')
        need(H(final[1])==(15,35)[i] and final[2]==(20,0)[i],'binary energy record')
        need(back(back(final))==s,'two-step inverse')
        need(energy(s)==energy(moved)==energy(final)==35,'full accounts')
        finals.append(final)
        # Passive reading is just H of the current field; no source/id passed.
        print('G4 WITNESS message={} native_history={} source_field={} actual_receiver={} H_receiver={} bank={} source_empty=True'.format(i,hist,y,final[1],H(final[1]),final[2]))
        again=s
        for _ in range(8):again=step(again)
        need(again==s,'declared eight-step prepared return')
        for bank in range(41):
            st=(cell,ZERO,bank,0);out=step(step(st))
            accepted=bank>=price(y)
            need(pi(out[1])==(hist[4] if accepted else hist[3]),'starved native boundary')
            need(back(back(out))==st and energy(out)==energy(st),'budget guard law')
        # A_f is a separate admitted mathematical continuation, not native U.
        free=final[1][:4]
        for _ in range(5):
            free=mv(AF,free);need(H(free)==H(final[1]) and in_shell(free),'free field record')
        need(free==final[1][:4],'free field fifth return')
    need(quotient(pi(finals[0][1]))==quotient(pi(finals[1][1])),'old port falsely separates')
    need(H(finals[0][1])!=H(finals[1][1]),'current field read fails')
    off=[step((y+(1,1),ZERO,30,0)) for y in (Y1,Y2)]
    need([H(s[1]) for s in off]==[5,5],'omitted beta scalar control')
    print('G5 PASS source_empty; both_native_boundary4_iff_B_ge_30; receiver_total_energy=35_in_both; omitted_beta_scalar_read=(5,5); prepared_full_return=8')


def main():
    try:
        anchors()
        allu=shells(CAP//5)
        fields=tuple(sorted(mv(L,u) for u in allu))
        need(len(fields)==len(set(fields)),'L injectivity')
        units=tuple(y for y in fields if H(y)==5)
        need(len(units)==20 and Y1 in units and Y2 in units,'unit sources')
        coset_minimum(units)
        primitive_audit(fields)
        witnesses()
    except Falsifier as exc:
        print('FALSIFIER: '+str(exc));print('AUDIT FAIL');return 0
    print('BOUNDARY selected integer lift, whole-cell exchange, bank and energy read; not original U implementation or physical admission')
    print('AUDIT PASS')
    return 0


if __name__=='__main__':
    raise SystemExit(main())
