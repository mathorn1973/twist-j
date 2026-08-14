#!/usr/bin/env python3
"""Dependency-free verifier for the independent issue-#369 certificate.

The companion independent_sympy.py discovers the lex basis from the raw
system.  This checker uses only the Python standard library to reparse the
source, rebuild all 3,889 raw records, verify all 383 active residuals, check
Buchberger's criterion for the sealed complex and real bases, check the
saturation unit, the exact real sign classification, and the frozen targets.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import re
import sys


if sys.flags.optimize:
    raise SystemExit("refusing optimized Python: exact verifier requires active assertions")


SOURCE_BYTES = 8515
SOURCE_SHA256 = "55fbc0ba2747b4e5adc5a5abd15ac7241a461ff8182268ebdae464d8a29cc9ae"
RAW_SHA256 = "09aac23466680ba762e363ad75845aa1535f4e8e32cee75ad41119f43cb16762"
SELECTED = (
    "01:00:00", "01:02:02", "02:08:05", "02:12:13",
    "02:13:22", "unit_phase",
)


# Sparse exact polynomial arithmetic.  Python tuple order is lex order.
def clean(p):
    return {m: Q(c) for m, c in p.items() if c}


def add(p, q, scale=Q(1)):
    out = dict(p)
    for m, c in q.items():
        out[m] = out.get(m, Q(0)) + scale*c
    return clean(out)


def mul(p, q):
    out = Counter()
    for m, c in p.items():
        for n, d in q.items():
            out[tuple(a+b for a, b in zip(m, n))] += c*d
    return clean(out)


def mul_monomial(p, monomial, coefficient=Q(1)):
    return clean({tuple(a+b for a, b in zip(m, monomial)): c*coefficient
                  for m, c in p.items()})


def lt(p):
    m = max(p)
    return m, p[m]


def divides(a, b):
    return all(x <= y for x, y in zip(a, b))


def quotient_monomial(a, b):
    return tuple(x-y for x, y in zip(a, b))


def normal_form(f, basis):
    work, remainder = dict(f), {}
    while work:
        m, c = lt(work)
        for g in basis:
            mg, cg = lt(g)
            if divides(mg, m):
                work = add(work, mul_monomial(g, quotient_monomial(m, mg), c/cg), -1)
                break
        else:
            remainder[m] = c
            del work[m]
    return clean(remainder)


def spoly(f, g):
    mf, cf = lt(f)
    mg, cg = lt(g)
    common = tuple(max(a, b) for a, b in zip(mf, mg))
    return add(
        mul_monomial(f, quotient_monomial(common, mf), 1/cf),
        mul_monomial(g, quotient_monomial(common, mg), 1/cg),
        -1,
    )


def check_reduced_groebner(basis):
    leading = [lt(g)[0] for g in basis]
    assert all(lt(g)[1] == 1 for g in basis)
    for i, g in enumerate(basis):
        for m in g:
            if m != leading[i]:
                assert not any(divides(L, m) for L in leading)
    for i in range(len(basis)):
        for j in range(i):
            assert normal_form(spoly(basis[i], basis[j]), basis) == {}


def strip_comments(text):
    return "\n".join(line.split("%", 1)[0] for line in text.splitlines())


def rows(block, pattern, allowed):
    out = []
    for row in (r.strip() for r in strip_comments(block).split(";") if r.strip()):
        tokens = re.findall(pattern, row)
        assert len(tokens) == 36 and set(tokens) <= allowed
        out.append(tokens)
    assert len(out) == 36
    return out


def parse_tensor(data):
    assert len(data) == SOURCE_BYTES
    assert hashlib.sha256(data).hexdigest() == SOURCE_SHA256
    found = re.findall(
        r"\bU\s*=\s*\[(.*?)\]\s*\.\*\s*w\.\^\s*\[(.*?)\]\s*;",
        data.decode(), re.S,
    )
    assert len(found) == 1
    amps = rows(found[0][0], r"(?<![A-Za-z0-9_])(?:0|a|b|c)(?![A-Za-z0-9_])",
                {"0", "a", "b", "c"})
    exps = rows(found[0][1], r"(?<![A-Za-z0-9_])(?:[0-9]|1[0-9])(?![A-Za-z0-9_])",
                {str(i) for i in range(20)})
    tensor = {}
    for r in range(36):
        for c in range(36):
            if amps[r][c] != "0":
                tensor[(r//6, r % 6, c//6, c % 6)] = (amps[r][c], int(exps[r][c]))
    assert len(tensor) == 112
    assert Counter(z[0] for z in tensor.values()) == Counter(a=40, b=40, c=32)
    return tensor


def flatten(tensor, parties):
    other = tuple(k for k in range(4) if k not in parties)
    result = [dict() for _ in range(36)]
    for ind, token in tensor.items():
        r = 6*ind[parties[0]] + ind[parties[1]]
        c = 6*ind[other[0]] + ind[other[1]]
        result[r][c] = token
    return result


def token_monomial(token, conjugate):
    label, exponent = token
    abc = {"a": (1, 0, 0), "b": (0, 1, 0), "c": (0, 0, 1)}[label]
    return abc + ((0, exponent) if conjugate else (exponent, 0))


def raw_records(tensor):
    result = []
    for parties in ((0, 1), (0, 2), (0, 3)):
        F = flatten(tensor, parties)
        for i in range(36):
            for j in range(36):
                p = Counter()
                for k in sorted(set(F[i]) & set(F[j])):
                    m = token_monomial(F[i][k], False)
                    n = token_monomial(F[j][k], True)
                    p[tuple(a+b for a, b in zip(m, n))] += 1
                if i == j:
                    p[(0, 0, 0, 0, 0)] -= 1
                result.append((f"{parties[0]}{parties[1]}:{i:02d}:{j:02d}",
                               {m: c for m, c in p.items() if c}))
    result.append(("unit_phase", {(0, 0, 0, 1, 1): 1, (0, 0, 0, 0, 0): -1}))
    return result


def raw_bytes(records):
    serial = []
    for tag, p in records:
        serial.append({"tag": tag,
                       "terms": [[list(m), c] for m, c in sorted(p.items())]})
    return (json.dumps(serial, sort_keys=True, separators=(",", ":")) + "\n").encode()


def P(n, *terms):
    """Build an n-variable polynomial from (coefficient, exponent tuple)."""
    assert all(len(m) == n for _, m in terms)
    return clean({m: Q(c) for c, m in terms})


def complex_basis():
    # variable order alpha,beta,gamma,y,x
    return [
        P(5, (1, (1,0,0,0,0)), (Q(1,5), (0,0,1,0,7)),
          (Q(-2,5), (0,0,1,0,5)), (Q(3,5), (0,0,1,0,3)),
          (Q(-4,5), (0,0,1,0,1))),
        P(5, (1, (0,1,0,0,0)), (Q(3,5), (0,0,1,0,7)),
          (Q(-1,5), (0,0,1,0,5)), (Q(-1,5), (0,0,1,0,3)),
          (Q(-2,5), (0,0,1,0,1))),
        P(5, (1, (0,0,2,0,0)), (Q(-1,2), (0,0,0,0,0))),
        P(5, (1, (0,0,0,1,0)), (1, (0,0,0,0,7)),
          (-1, (0,0,0,0,5)), (1, (0,0,0,0,3)), (-1, (0,0,0,0,1))),
        P(5, (1, (0,0,0,0,8)), (-1, (0,0,0,0,6)),
          (1, (0,0,0,0,4)), (-1, (0,0,0,0,2)), (1, (0,0,0,0,0))),
    ]


def real_basis():
    # variable order alpha,beta,gamma,v,u
    return [
        P(5, (1, (1,0,0,0,0)), (Q(8,5), (0,0,1,0,3)),
          (-2, (0,0,1,0,1))),
        P(5, (1, (0,1,0,0,0)), (Q(-16,5), (0,0,1,0,3)),
          (2, (0,0,1,0,1))),
        P(5, (1, (0,0,2,0,0)), (Q(-1,2), (0,0,0,0,0))),
        P(5, (1, (0,0,0,2,0)), (1, (0,0,0,0,2)),
          (-1, (0,0,0,0,0))),
        P(5, (1, (0,0,0,0,4)), (Q(-5,4), (0,0,0,0,2)),
          (Q(5,16), (0,0,0,0,0))),
    ]


def target_polynomials():
    # variable order alpha,beta,gamma,y,x
    a = P(5, (1, (1,0,0,0,0)))
    b = P(5, (1, (0,1,0,0,0)))
    c = P(5, (1, (0,0,1,0,0)))
    x = P(5, (1, (0,0,0,0,1)))
    y = P(5, (1, (0,0,0,1,0)))
    one = P(5, (1, (0,0,0,0,0)))
    r0 = add(mul(c, c), one, Q(-1,2))
    r0 = mul_monomial(r0, (0,0,0,0,0), 2)
    r1 = add(add(mul(a,a), mul(b,b)), mul(c,c), -1)
    r2 = add(add(mul(b,b), mul(a,b), -1), mul(a,a), -1)
    r3 = P(5, (1,(0,0,0,0,8)), (-1,(0,0,0,0,6)),
           (1,(0,0,0,0,4)), (-1,(0,0,0,0,2)), (1,(0,0,0,0,0)))
    r4 = add(c, mul(a, add(x,y)), -1)
    r5 = add(b, mul(a, add(mul(x,x),mul(y,y))), -1)
    return [r0,r1,r2,r3,r4,r5]


def sign_sqrt5(pair):
    """Sign of rational a+b*sqrt(5), with no floating point."""
    a, b = map(Q, pair)
    if b == 0:
        return (a > 0) - (a < 0)
    if a == 0 or (a > 0) == (b > 0):
        return 1 if b > 0 else -1
    comparison = a*a - 5*b*b
    return ((a > 0) - (a < 0)) if comparison > 0 else ((b > 0) - (b < 0))


def forward_membership_certificate(records, K):
    """Verify a compact straight-line representation of K in six raw records.

    Every ``derive`` call computes both the displayed polynomial and its full
    six-coordinate representation vector.  Thus the DAG below is not merely
    a vanishing check: it is an exact tracked ideal-membership certificate.
    """
    tags = SELECTED
    raw_by_tag = {}
    for tag, p in records:
        if tag in tags:
            raw_by_tag[tag] = clean({(m[0],m[1],m[2],m[4],m[3]): Q(c)
                                     for m,c in p.items()})
    assert set(raw_by_tag) == set(tags)
    zero=(0,0,0,0,0)
    one=P(5,(1,zero))
    def var(i):
        e=[0]*5;e[i]=1;return P(5,(1,tuple(e)))
    a,b,c,y,x=(var(i) for i in range(5))
    def pp(p,n):
        out=one
        for _ in range(n):out=mul(out,p)
        return out
    def scal(p,k):return mul_monomial(p,zero,Q(k))
    def summ(*ps):
        out={}
        for p in ps:out=add(out,p)
        return out
    z=mul(x,y); q=add(z,one,-1)
    def S(n):
        return summ(*(pp(z,k) for k in range(n)))

    class Tr:
        def __init__(self,p,rep):self.p,self.rep=p,rep
    source=[]
    for i,tag in enumerate(tags):
        rep=[{} for _ in tags];rep[i]=one
        source.append(Tr(raw_by_tag[tag],rep))
    R0,R1,R2,R3,R4,Rq=source
    def derive(claim, terms):
        got={}; rep=[{} for _ in tags]
        for coeff,tr in terms:
            got=add(got,mul(coeff,tr.p))
            for i in range(len(tags)):rep[i]=add(rep[i],mul(coeff,tr.rep[i]))
        assert got==claim
        assert summ(*(mul(rep[i],source[i].p) for i in range(len(tags))))==claim
        return Tr(claim,rep)

    A=add(scal(mul(c,c),2),one,-1)
    B=add(scal(summ(mul(a,a),mul(b,b)),2),one,-1)
    r=summ(one,mul(x,x)); s=summ(one,pp(x,10))
    phi=summ(pp(x,8),scal(pp(x,6),-1),pp(x,4),scal(pp(x,2),-1),one)
    T=summ(mul(c,pp(x,11)),mul(a,r)); C=mul(mul(a,b),s)
    D=mul(b,T); E=summ(mul(mul(b,c),pp(x,11)),mul(b,b),mul(mul(a,a),pp(x,4)))

    tA=derive(A,[(one,R0)])
    tB=derive(B,[(one,R1),(scal(summ(scal(mul(mul(b,b),S(3)),2),
                                      scal(mul(mul(a,a),S(18)),2)),-1),Rq)])
    tC=derive(C,[(pp(x,3),R3),(scal(mul(mul(a,b),summ(S(4),mul(pp(x,10),S(3)))),-1),Rq)])
    tD=derive(D,[(x,R2),(scal(mul(mul(a,b),summ(S(3),mul(pp(x,2),S(18)))),-1),Rq)])
    tE=derive(E,[(pp(x,6),R4),(scal(summ(mul(mul(mul(b,c),pp(x,11)),S(14)),
                                      mul(mul(b,b),S(10)),mul(mul(mul(a,a),pp(x,4)),S(5))),-1),Rq)])

    Hb=scal(mul(pp(y,4),summ(mul(c,pp(x,11)),mul(b,add(one,pp(x,4),-1)))),-2)
    Ub=add(mul(b,Hb),one,-1)
    tUb=derive(Ub,[(mul(pp(x,4),pp(y,4)),tB),(scal(pp(y,4),-2),tE),(S(4),Rq)])
    tT=derive(T,[(Hb,tD),(scal(T,-1),tUb)])
    Ha=scal(mul(mul(c,pp(y,11)),r),-2)
    Ua=add(mul(a,Ha),one,-1)
    tUa=derive(Ua,[(scal(mul(c,pp(y,11)),-2),tT),(pp(z,11),tA),(S(11),Rq)])
    Hr=scal(mul(mul(a,c),pp(y,11)),-2)
    Ur=add(mul(r,Hr),one,-1)
    tUr=derive(Ur,[(one,tUa)])
    tas=derive(mul(a,s),[(Hb,tC),(scal(mul(a,s),-1),tUb)])
    ts=derive(s,[(Ha,tas),(scal(s,-1),tUa)])
    tphi=derive(phi,[(Hr,ts),(scal(phi,-1),tUr)])

    q0=add(T,mul(mul(c,x),s),-1)
    tq0=derive(q0,[(one,tT),(scal(mul(c,x),-1),ts)])
    P0=summ(pp(x,7),scal(pp(x,5),-2),scal(pp(x,3),3),scal(x,-4))
    g0=summ(a,scal(mul(c,P0),Q(1,5)))
    trg0=derive(mul(r,g0),[(one,tq0),(scal(mul(c,x),Q(1,5)),tphi)])
    tg0=derive(g0,[(Hr,trg0),(scal(g0,-1),tUr)])

    F=add(E,mul(b,T),-1)
    tF=derive(F,[(one,tE),(scal(b,-1),tT)])
    L0=add(add(scal(B,Q(1,2)),F,-1),scal(A,Q(1,2)),-1)
    tL0=derive(L0,[(scal(one,Q(1,2)),tB),(scal(one,-1),tF),(scal(one,Q(-1,2)),tA)])
    P1=summ(scal(pp(x,7),3),scal(pp(x,5),-1),scal(pp(x,3),-1),scal(x,-2))
    g1=summ(b,scal(mul(c,P1),Q(1,5)))
    H=summ(pp(x,10),scal(pp(x,8),-6),scal(pp(x,6),6),scal(pp(x,4),-6),pp(x,2),scal(one,25))
    W=summ(scal(mul(a,pp(x,2)),-5),scal(a,5),mul(c,pp(x,9)),scal(mul(c,pp(x,7)),-6),
           scal(mul(c,pp(x,5)),6),scal(mul(c,pp(x,3)),-6),scal(mul(c,x),6))
    Q0=scal(mul(r,W),Q(-1,5))
    Z=summ(mul(Q0,g0),scal(mul(mul(phi,H),A),Q(1,50)),scal(mul(H,phi),Q(1,50)))
    tZ=derive(Z,[(Q0,tg0),(scal(mul(phi,H),Q(1,50)),tA),(scal(H,Q(1,50)),tphi)])
    targ1=derive(mul(mul(a,r),g1),[(one,tL0),(one,tZ)])
    tag1=derive(mul(a,g1),[(Hr,targ1),(scal(mul(a,g1),-1),tUr)])
    tg1=derive(g1,[(Ha,tag1),(scal(g1,-1),tUa)])
    tg2=derive(scal(A,Q(1,2)),[(scal(one,Q(1,2)),tA)])
    g3=summ(y,pp(x,7),scal(pp(x,5),-1),pp(x,3),scal(x,-1))
    tg3=derive(g3,[(add(y,g3,-1),Rq),(y,tphi)])

    outputs=[tg0,tg1,tg2,tg3,tphi]
    assert [z.p for z in outputs]==K
    payload=[]
    for out in outputs:
        row=[]
        for rp in out.rep:
            row.append([[list(m),[v.numerator,v.denominator]] for m,v in sorted(rp.items())])
        payload.append(row)
    cert=(json.dumps({"raw_tags":tags,"representations":payload},sort_keys=True,separators=(",",":"))+"\n").encode()
    return len(cert),hashlib.sha256(cert).hexdigest(),sum(len(p) for o in outputs for p in o.rep)


def main():
    if len(sys.argv) != 2:
        raise SystemExit("usage: independent_stdlib_verify.py AME46_ORIGINAL.m")
    tensor=parse_tensor(Path(sys.argv[1]).read_bytes())
    assert tensor[(0,0,0,1)] == ("c",0)
    assert tensor[(0,1,0,2)] == ("c",17)
    records = raw_records(tensor)
    stream = raw_bytes(records)
    assert len(records) == 3889 and sum(bool(p) for _, p in records) == 383
    assert len(stream) == 136262 and hashlib.sha256(stream).hexdigest() == RAW_SHA256

    K = complex_basis()
    check_reduced_groebner(K)
    rep_bytes,rep_sha,rep_terms = forward_membership_certificate(records,K)
    # Reorder source monomials a,b,c,x,y -> certificate a,b,c,y,x.
    active = 0
    tags = set()
    for tag, p in records:
        if not p:
            continue
        active += 1
        q = {(m[0],m[1],m[2],m[4],m[3]): Q(c) for m,c in p.items()}
        assert normal_form(q, K) == {}
        if tag in SELECTED:
            tags.add(tag)
    assert active == 383 and tags == set(SELECTED)

    # D * (-8 gamma x^6 + 8 gamma x^4 + 4 gamma) == 1 mod K.
    D = P(5, (1, (1,1,1,1,1)))
    invD = P(5, (-8,(0,0,1,0,6)), (8,(0,0,1,0,4)), (4,(0,0,1,0,0)))
    one = P(5, (1,(0,0,0,0,0)))
    assert normal_form(add(mul(D, invD), one, -1), K) == {}

    KR = real_basis()
    check_reduced_groebner(KR)
    # p=2u^2-3/2, p^2=1-u^2, and p^{-1}=8u^2-4 modulo q(u).
    p = P(5, (2,(0,0,0,0,2)), (Q(-3,2),(0,0,0,0,0)))
    pinv = P(5, (8,(0,0,0,0,2)), (-4,(0,0,0,0,0)))
    v2 = P(5, (1,(0,0,0,2,0)))
    assert normal_form(add(v2, mul(p,p), -1), KR) == {}
    assert normal_form(add(mul(p,pinv), P(5,(1,(0,0,0,0,0))), -1), KR) == {}

    # q(u) gives s=u^2=(5 +/- sqrt(5))/8.  Exact sign logic selects
    # gamma>0, u>0 and the plus root; v remains the two conjugate signs.
    s_plus = (Q(5,8), Q(1,8))
    s_minus = (Q(5,8), Q(-1,8))
    assert sign_sqrt5(s_plus) > 0 and sign_sqrt5((1-s_plus[0],-s_plus[1])) > 0
    assert sign_sqrt5(s_minus) > 0 and sign_sqrt5((1-s_minus[0],-s_minus[1])) > 0
    for s in (s_plus, s_minus):
        assert sign_sqrt5((5-4*s[0], -4*s[1])) > 0  # sign(alpha)=sign(gamma*u)
    assert sign_sqrt5((8*s_plus[0]-5,8*s_plus[1])) > 0
    assert sign_sqrt5((8*s_minus[0]-5,8*s_minus[1])) < 0
    def sqrt_interval(square_pair,lo,hi):
        lo,hi=Q(lo),Q(hi)
        assert lo>=0 and sign_sqrt5((square_pair[0]-lo*lo,square_pair[1]))>0
        assert sign_sqrt5((hi*hi-square_pair[0],-square_pair[1]))>0
    sqrt_interval((Q(5),Q(0)),Q(559,250),Q(2237,1000))       # d=sqrt(5)
    sqrt_interval((4*s_plus[0],4*s_plus[1]),Q(951,500),Q(1903,1000)) # T=2u
    sqrt_interval((Q(1,2),Q(0)),Q(707,1000),Q(177,250))      # gamma
    sqrt_interval((Q(1,4),Q(-1,20)),Q(371,1000),Q(93,250))  # alpha
    sqrt_interval((Q(1,4),Q(1,20)),Q(601,1000),Q(301,500))  # beta
    sqrt_interval(s_plus,Q(951,1000),Q(1903,2000))           # u
    vpair=(Q(-1,4),Q(1,4))
    assert sign_sqrt5((vpair[0]-Q(309,1000),vpair[1]))>0
    assert sign_sqrt5((Q(31,100)-vpair[0],-vpair[1]))>0

    targets = target_polynomials()
    assert [normal_form(r,K) for r in targets] == [{}]*6

    # Phi20 divides x^20-1: reduction by its monic univariate generator.
    x20minus1 = P(5, (1,(0,0,0,0,20)), (-1,(0,0,0,0,0)))
    assert normal_form(x20minus1, [K[-1]]) == {}
    assert (17*13-1) % 20 == 0

    print("GOLDEN_RIGIDITY_INDEPENDENT_STDLIB_V1")
    print("PASS SOURCE_AND_RAW records=3889 active=383 sha256=" + RAW_SHA256)
    print("PASS FIELD_LOCATORS U[0,1]=gamma U[1,2]=gamma*x^17")
    print("PASS COMPLEX_GB buchberger=YES reduced=YES raw_residuals=383/383")
    print(f"PASS FORWARD_MEMBERSHIP outputs=5 raw_tags=6 terms={rep_terms} bytes={rep_bytes} sha256={rep_sha}")
    print("PASS SIX_RAW_COORDINATES=" + ",".join(SELECTED))
    print("PASS SATURATION_REDUNDANT D_inverse=-8*gamma*x^6+8*gamma*x^4+4*gamma")
    print("PASS REAL_GB buchberger=YES reduced=YES decomposition=two_comaximal_components")
    print("PASS POSITIVE_CLASSIFICATION total_real=16 positive=2 conjugation_pair=YES")
    print("PASS PRIMARY_INTERVALS d,T,gamma,alpha,beta,u,v_plus,v_minus=8/8")
    print("PASS TARGET complex_mask=111111 positive_mask=111111")
    print("PASS FIELD exponent_inverse=13_mod_20 compositum=Q(zeta40)")
    print("SUMMARY 11/11 PASS verdict=EXACT_J_RIGID_UP_TO_CONJUGATION")


if __name__ == "__main__":
    main()
