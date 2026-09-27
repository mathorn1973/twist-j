#!/usr/bin/env python3
"""Prospective exact audit; universal classification is in PROOF.md."""
from __future__ import annotations
import contextlib
import hashlib
import io
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[2]
ANCHOR = ROOT / 'probes/P-J-HODGE-HERM2-LOXODROME-1/verify.py'
DIGEST = '02f33f1de4174ee4d4aeb45202d838897e68c3bd205df23f9b208cc669f489d9'

def main():
    if hashlib.sha256(ANCHOR.read_bytes()).hexdigest() != DIGEST:
        raise RuntimeError('STOP: inherited anchor hash differs')
    anchor_out = io.StringIO()
    with contextlib.redirect_stdout(anchor_out):
        m = runpy.run_path(str(ANCHOR))
    Q5, phi = m['Q5'], m['phi']
    mm, tr, add, sub, scale = (m[s] for s in ('mm','tr','add','sub','scale'))
    power, rank, solve, cb, wedge = (m[s] for s in ('power','rank','solve','colbasis','compound2'))
    z, one = Q5(0), Q5(1)
    def mat(a): return [[Q5(x) for x in row] for row in a]
    def eye(n): return [[one if i==j else z for j in range(n)] for i in range(n)]
    def zero(r,c): return [[z for _ in range(c)] for __ in range(r)]
    def cols(a): return tr(a)
    def cat(*arrays): return tr([v for a in arrays for v in tr(a)])
    def inv(a): return tr([solve(a,v) for v in tr(eye(len(a)))])
    def null(a):
        a=[row[:] for row in a]; n=len(a[0]); r=0; piv=[]
        for c in range(n):
            p=next((i for i in range(r,len(a)) if a[i][c]),None)
            if p is None: continue
            a[r],a[p]=a[p],a[r]; u=one/a[r][c]
            a[r]=[u*x for x in a[r]]
            for i in range(len(a)):
                if i!=r and a[i][c]:
                    f=a[i][c]; a[i]=[a[i][j]-f*a[r][j] for j in range(n)]
            piv.append(c); r+=1
        out=[]
        for c in range(n):
            if c in piv: continue
            v=[z]*n; v[c]=one
            for i,p in enumerate(piv): v[p]=-a[i][c]
            out.append(v)
        return tr(out) if out else [[] for _ in range(n)]
    def sign(x):
        a,b=x.a,x.b
        if not b: return (a>0)-(a<0)
        if not a: return (b>0)-(b<0)
        if a*b>0: return (a>0)-(a<0)
        c=a*a-5*b*b
        assert c
        t=a if c>0 else b
        return (t>0)-(t<0)
    def det2(a): return a[0][0]*a[1][1]-a[0][1]*a[1][0]
    def restrict(a,b): return mm(mm(tr(b),a),b)
    def eqs(x,y):
        out=[]
        for i in range(6):
            for j in range(6):
                r=[z]*36
                for k in range(6):
                    r[6*i+k]=r[6*i+k]+x[k][j]
                    r[6*k+j]=r[6*k+j]-y[i][k]
                out.append(r)
        return out
    L,K,beta,E,A,g=(m[s] for s in ('LQ','KQ','WQ','E','A','B'))
    Q=mat(wedge(m['C']))
    R=tr([solve(E,v) for v in tr(mm(Q,E))])
    D,B=wedge(R),wedge(A)
    assert mm(Q,E)==mm(E,R)
    assert power(Q,5)==eye(6) and power(R,5)==eye(4)
    assert mm(Q,K)==mm(K,Q) and mm(Q,L)==mm(L,Q)
    assert restrict(beta,Q)==beta and restrict(g,R)==g
    assert restrict(g,A)==g
    L10,B10=power(L,10),power(B,10)
    P=null(sub(L10,eye(6)))
    Pp=tr(cb(mm(m['Pp'],P)))
    Pm=tr(cb(mm(m['Pm'],P)))
    hp=null(sub(L,scale(eye(6),phi*phi)))
    hm=null(sub(L,scale(eye(6),one/(phi*phi))))
    assert [rank(a) for a in (P,Pp,Pm,hp,hm)]==[4,2,2,1,1]
    U=cat(Pp,Pm,hp,hm); assert rank(U)==6
    ef=tr([solve(E,v) for v in tr(cat(hp,hm,Pp))])
    wf=wedge(ef); V=tr([tr(wf)[j] for j in (0,5,1,2,3,4)])
    Ui,Vi=inv(U),inv(V)
    l=mm(mm(Ui,L10),U); b=mm(mm(Vi,B10),V)
    q=mm(mm(Ui,Q),U); d=mm(mm(Vi,D),V)
    rr=one
    for _ in range(20): rr=rr*phi
    sl=[one]*4+[rr,one/rr]; tl=[one,one,rr,rr,one/rr,one/rr]
    assert l==[[sl[i] if i==j else z for j in range(6)] for i in range(6)]
    assert b==[[tl[i] if i==j else z for j in range(6)] for i in range(6)]
    homdim=36-rank(eqs(l,b))
    jointdim=36-rank(eqs(l,b)+eqs(q,d))
    assert homdim==12 and jointdim==0
    rp=[row[:2] for row in q[:2]]
    rm=[row[2:4] for row in q[2:4]]
    assert rp[0][0]+rp[1][1]==-phi and det2(rp)==one
    assert rm[0][0]+rm[1][1]==phi-one and det2(rm)==one
    assert sign(phi*phi-4)<0 and sign((phi-one)*(phi-one)-4)<0
    assert d==[([one,z,z,z,z,z] if i==0 else [z,one,z,z,z,z] if i==1
        else [z,z]+rp[i-2]+[z,z] if i<4 else [z,z,z,z]+rp[i-4]) for i in range(6)]
    assert mm(K,Pp)==scale(Pp,m['S']) and mm(K,Pm)==scale(Pm,-m['S'])
    # All rank-four matrices have exactly the 2x4,2x1,2x1 block pattern.
    # These independent 12 unit coefficients span the complete solved Hom.
    allowed=[(i,j) for i in range(2) for j in range(4)]+[(2,4),(3,4),(4,5),(5,5)]
    for i,j in allowed:
        s=zero(6,6); s[i][j]=one
        assert mm(s,l)==mm(b,s)
    gf=restrict(g,ef); a=gf[0][1]
    gp=[row[2:] for row in gf[2:]]
    assert gf[0][0]==gf[1][1]==z and a
    assert all(gf[i][j]==z for i in (0,1) for j in (2,3))
    assert sign(gp[0][0])>0 and sign(det2(gp))>0
    h=wedge(g); gamma=beta  # same combinatorial wedge matrix in E coordinates
    hf=restrict(h,V); cf=restrict(gamma,V)
    vol=cf[0][1]; assert vol
    expected_h=zero(6,6); expected_h[0][0]=-a*a; expected_h[1][1]=det2(gp)
    expected_c=zero(6,6); expected_c[0][1]=expected_c[1][0]=vol
    for i in range(2):
        for j in range(2):
            expected_h[2+i][4+j]=expected_h[4+j][2+i]=a*gp[i][j]
            eps=one if (i,j)==(0,1) else -one if (i,j)==(1,0) else z
            expected_c[2+i][4+j]=expected_c[4+j][2+i]=-vol*eps
    assert hf==expected_h and cf==expected_c
    # Two rank-four maps with the same negative-Hodge periodic kernel.
    # Their natural h restrictions have different rank: no target h-isometry equates them.
    images=[]; maps=[]
    for y in ([one,z],[-gp[0][1],gp[0][0]]):
        s=zero(6,6); s[0][0]=s[1][1]=s[2][4]=one
        s[4][5],s[5][5]=y
        assert rank(s)==4 and mm(s,l)==mm(b,s)
        im=tr(cb(s)); images.append(im); maps.append(mm(mm(V,s),Ui))
        assert rank(cat(im,mm(d,im)))>4
    assert [rank(restrict(hf,v)) for v in images]==[4,2]
    assert [rank(restrict(cf,v)) for v in images]==[2,4]
    # Orthogonal source quotient is not target-form restriction.
    Pi=mm(mm(mm(E,inv(g)),tr(E)),beta)
    assert rank(Pi)==4 and mm(Pi,Pi)==Pi and mm(Pi,E)==E
    assert mm(Pi,L)==mm(L,Pi) and mm(Pi,Q)==mm(Q,Pi)
    assert mm(Pi,Pm)==zero(6,2)
    assert rank(restrict(beta,Pm))==2 and sign(restrict(beta,Pm)[0][0])<0
    conj=lambda x: Q5(x.a,-x.b)
    Pi2=[[conj(x) for x in row] for row in Pi]
    assert rank(mm(Pi,Pi2))==2 and rank(add(Pi,Pi2))==6 and Pi!=Pi2
    print('PASS anchors: exact hash-pinned marked A4/J-Hodge reproduction')
    print('PASS blocked class: dim_F Hom(L^10,B^10)=12; maximum rank 4')
    print('PASS C5 map test: joint blocked/C5 Hom dimension 0')
    print('PASS C5 image test: two real-irreducible rotating target planes; no invariant rank-four image')
    print('PASS kernel test: periodic source splits into two inequivalent C5/Hodge planes')
    print('PASS target forms: exact block matrices; nondegenerate pencil restriction is (2,2), otherwise (1,1,2 zero)')
    print('PASS witnesses: same Hodge kernel, different images, h ranks 4/2 and wedge ranks 2/4')
    print('PASS direct quotient: rank-four orthogonal J/C5 projection onto E survives; Galois changes chart')
    print('NON-CANONICAL L1: no physical spacetime or photon conclusion')

if __name__=='__main__': main()
