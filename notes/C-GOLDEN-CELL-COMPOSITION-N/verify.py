#!/usr/bin/env python3
"""Exact supplementary audit of the frozen same-carrier composition claims."""
from fractions import Fraction as Q
from functools import lru_cache
from hashlib import sha256
from itertools import product
from math import isqrt


def add(x, y):
    return x[0]+y[0], x[1]+y[1]


def scale(c, x):
    return c*x[0], c*x[1]


def mul(x, y):
    a, b = x
    c, d = y
    return a*c+b*d, a*d+b*c+b*d


def bar(x):
    return x[0]+x[1], -x[1]


def norm(x):
    a, b = x
    return a*a+a*b-b*b


def trace(x):
    return 2*x[0]+x[1]


def positive(x):
    return trace(x)>0 and norm(x)>0


def reduced(x):
    a, b = x
    return a+3*b>0 and a-2*b>=0


def eps(x):
    a, b = x
    return a+b, a+2*b


def epsinv(x):
    a, b = x
    return 2*a-b, b-a


@lru_cache(maxsize=None)
def unit(n):
    if not isinstance(n, int):
        raise TypeError('integer exponent required')
    base, count = ((1, 1), n) if n>=0 else ((2, -1), -n)
    ans = (1, 0)
    while count:
        if count & 1:
            ans = mul(ans, base)
        base = mul(base, base)
        count >>= 1
    return ans


@lru_cache(maxsize=None)
def encode(x):
    if not positive(x):
        raise ValueError('positive-sheet element required')
    n, r = 0, x
    while r[0]-2*r[1]<0:
        r = epsinv(r)
        n += 1
    while r[0]+3*r[1]<=0:
        r = eps(r)
        n -= 1
    assert reduced(r)
    return n, r


def decode(c):
    n, r = c
    if not reduced(r):
        raise ValueError('not in fundamental region')
    return mul(unit(n), r)


def combine(c1, c2):
    n, r = c1
    m, s = c2
    carry, t = encode(add(r, mul(unit(m-n), s)))
    return n+carry, t


@lru_cache(maxsize=None)
def trace_encode(x):
    # Separate coordinate recurrence, no call to encode or unit.
    t, b = trace(x), x[1]
    n = 0
    assert t>0 and t*t>5*b*b and (t-b)%2==0
    while 5*b>t:
        nt, nb = 3*t-5*b, -t+3*b
        assert nt%2==0 and nb%2==0
        t, b = nt//2, nb//2
        n += 1
    while 5*b<=-t:
        nt, nb = 3*t+5*b, t+3*b
        assert nt%2==0 and nb%2==0
        t, b = nt//2, nb//2
        n -= 1
    assert (t-b)%2==0 and -t<5*b<=t
    return n, ((t-b)//2, b)


def chart_signature(r):
    # Exact squares/sign suffice because normalized energy is positive.
    if not reduced(r):
        raise ValueError('reduced input required')
    b, N, t = r[1], norm(r), trace(r)
    sign = (b>0)-(b<0)
    return Q(t*t, N), Q(5*b*b, N), sign


def recover(N, signature):
    E2, p2, sign = signature
    t2, b2 = N*E2, N*p2/5
    assert t2.denominator==1 and b2.denominator==1
    t, b = isqrt(t2.numerator), isqrt(b2.numerator)
    assert t*t==t2 and b*b==b2
    b *= sign
    assert (t-b)%2==0
    return (t-b)//2, b


def box(size):
    return [(a, b) for a in range(1, size+1)
            for b in range(-size, size+1) if positive((a, b))]


def mm(A, B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))


def isprime(p):
    return p>=2 and all(p%d for d in range(2, isqrt(p)+1))


def main():
    inputs = box(16)
    digest = sha256()
    shifted = seams = 0
    for x in inputs:
        c = encode(x)
        n, r = c
        assert c==trace_encode(x)
        assert decode(c)==x and encode(r)==(0, r)
        assert norm(x)==norm(r) and positive(r)
        assert epsinv(eps(x))==eps(epsinv(x))==x
        assert eps(x)==mul((1, 1), x)
        assert epsinv(x)==mul((2, -1), x)
        E2, p2, sign = chart_signature(r)
        assert E2-p2==4 and 0<=p2<=1
        assert (p2==1)==(r[0]==2*r[1])
        assert recover(norm(r), (E2, p2, sign))==r
        if r[0]==2*r[1]:
            assert encode(bar(x))==(-n-1, r)
            seams += 1
        else:
            assert encode(bar(x))==(-n, bar(r))
        for j in range(-8, 9):
            y = mul(unit(j), x)
            assert encode(y)==trace_encode(y)==(n+j, r)
            assert norm(y)==norm(x)
            assert reduced(mul(unit(-(n+j)), x))==(j==0)
            shifted += 1
        digest.update(f'{x}|{n}|{r}\n'.encode('ascii'))
    print(f'G1 PASS positive_inputs={len(inputs)} shifted_cases={shifted} upper_seams={seams} exact_unique_reduction')
    print('NORMAL_FORM_LEDGER_SHA256 '+digest.hexdigest())

    pairs = closed_pairs = same_frame = 0
    for x, y in product(inputs, repeat=2):
        z = add(x, y)
        cx, cy = encode(x), encode(y)
        cz = combine(cx, cy)
        assert cz==encode(z)==trace_encode(z)
        assert combine(cy, cx)==cz and decode(cz)==z
        assert min(cx[0], cy[0])<=cz[0]<=max(cx[0], cy[0])
        cross = trace(mul(x, bar(y)))
        beta = x[1]*y[0]-x[0]*y[1]
        assert norm(z)==norm(x)+norm(y)+cross
        assert cross*cross-4*norm(x)*norm(y)==5*beta*beta
        # The weighted normalized coordinates are exactly (trace,b*sqrt5).
        assert trace(z)==trace(x)+trace(y) and z[1]==x[1]+y[1]
        if reduced(x) and reduced(y):
            assert reduced(z)
            closed_pairs += 1
        if cx[0]==cy[0]:
            assert cz==(cx[0], add(cx[1], cy[1]))
            same_frame += 1
        pairs += 1
    print(f'G2 PASS ordered_pairs={pairs} reduced_closed_pairs={closed_pairs} common_frame_no_carry={same_frame} norm_and_frame_transport')

    small = box(4)
    triples = 0
    for x, y, z in product(small, repeat=3):
        a, b, c = encode(x), encode(y), encode(z)
        lhs = combine(combine(a, b), c)
        rhs = combine(a, combine(b, c))
        assert lhs==rhs==trace_encode(add(add(x, y), z))
        triples += 1
    print(f'G3 PASS associativity_triples={triples} no_output_truncation')

    reps = sorted({encode(x)[1] for x in inputs})
    scales = 0
    for r in reps:
        H = chart_signature(r)
        for c in range(1, 9):
            cr = scale(c, r)
            assert reduced(cr) and norm(cr)==c*c*norm(r)
            assert chart_signature(cr)==H
            assert recover(norm(cr), H)==cr
            scales += 1
    # Exact positive weighted-composition witness.
    assert add((1, 0), (2, 1))==(3, 1)
    assert chart_signature((1, 0))==(Q(4), Q(0), 0)
    assert chart_signature((2, 1))==(Q(5), Q(1), 1)
    assert chart_signature((3, 1))==(Q(49, 11), Q(5, 11), 1)
    assert reduced((4, 2)) and norm((4, 2))==20 and trace((4, 2))==10
    print(f'G4 PASS distinct_reduced_inputs={len(reps)} scale_controls={scales} faithful_norm_reconstruction_and_weighted_composition')

    # Unit-orbit quotient: same reduced inputs, different total norms.
    assert encode((1, 0))[1]==encode((1, 1))[1]==(1, 0)
    assert norm(add((1, 0), (1, 0)))==4
    assert norm(add((1, 0), (1, 1)))==5
    Mphi=((0, 1), (1, 1)); Mphi_inv=((-1, 1), (1, 0)); I=((1, 0), (0, 1))
    assert mm(Mphi, Mphi_inv)==mm(Mphi_inv, Mphi)==I
    assert Mphi[0][0]*Mphi[1][1]-Mphi[0][1]*Mphi[1][0]==-1
    lucas=[2, 1]
    for _ in range(2, 129):
        lucas.append(lucas[-1]+lucas[-2])
    previous = 0
    for d in range(65):
        y = unit(d)
        assert norm(y)==1 and encode(y)==(d, (1, 0))
        val = norm(add((1, 0), y))
        assert val==2+lucas[2*d] and val>previous
        previous = val
    print('G5 PASS quotient_counterexample_norms=4,5 unit_difference_unimodular=1 relative_frame_family=65')

    # ANY Fourier folds of a rest input leave total sine square unchanged.
    assert add((1, 0), (4, 1))==add((2, 0), (3, 1))==(5, 1)
    p19=chart_signature((4, 1))[1]; p11=chart_signature((3, 1))[1]
    assert p19==Q(5, 19) and p11==Q(5, 11) and p19!=p11
    for x in [(1, 0), (2, 0)]:
        assert chart_signature(x)[1]==0

    # All-prime version: exact coefficients in Q(sqrt21), never floats.
    a,b,c,d=(3,1),(4,1),(2,1),(5,1)
    assert add(a,b)==add(c,d)==(7,2) and norm((7,2))==59
    assert tuple(map(norm,(a,b,c,d)))==(11,19,5,29)
    assert all(isprime(norm(x)) and reduced(x) for x in (a,b,c,d))
    p=chart_signature(a)[1]; q=chart_signature(b)[1]
    constant=p*(1-q)+(1-p)*q
    radical_square=4*p*(1-p)*q*(1-q)
    radical_coefficient=Q(20,209)
    assert constant==Q(100,209)
    assert radical_square==21*radical_coefficient*radical_coefficient
    target=1-chart_signature(d)[1]
    assert chart_signature(c)[1]==1 and target==Q(24,29)
    assert (target-constant)**2!=radical_square
    assert isqrt(21)**2!=21
    print('G6 PASS all_fold_torus_obstruction=5/19_vs_5/11 all_prime_total_norm=59')
    print('ALL_PRIME_TOTAL_SINE_SQUARES (100+/-20sqrt21)/209 != 24/29')
    print('DECISION rapidity_cell_addition=CLOSED quotient_addition=NOT_DEFINED nominated_total_W_factor=REJECTED')
    print('STATUS NON-CANONICAL finite exact audit; proofs separate; no independent review or dynamics bridge')


if __name__=='__main__':
    main()
