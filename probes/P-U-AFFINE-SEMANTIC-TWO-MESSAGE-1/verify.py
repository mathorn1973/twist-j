#!/usr/bin/env python3
# Copyright 2026 A. M. Thorn
# SPDX-License-Identifier: Apache-2.0
"""Frozen exact falsifiers for the alternate affine-preparation witness."""
from collections import Counter
from hashlib import sha256
from itertools import product
from pathlib import Path


def prepare(lam, mu):
    r = 3*(1+mu-lam) % 5
    return tuple(v % 5 for v in (3*mu,3,3*mu,2,2-mu-r,r))


def forms(x):
    a,b,c,d,q,r = x
    return tuple(v % 5 for v in (a+c,b+d,a-c-2,b-d-1,sum(x)))


def read(x):
    A,B,C,D,z = forms(x)
    return (A+D) % 5, (C+z) % 5


def decode(code):
    X,H = code
    return -1 if H == 0 else H*H*X % 5


def generator(x, k):
    a,b,c,d,q,r = x
    values = ((b,a,d,c,q,r),(-c,-d,-a,-b,-q,-r),
              (2-c,1-d+r,2-a,1-b-r,1-q,-r),
              (2-a,1-b,3-c,4-d,1-q,1-r),
              (2-a,1-b,3-c,4-d,2-q,1-r))[k]
    return tuple(v % 5 for v in values)


def step(x, bit):
    k = (sum(x)+2*bit) % 5
    return generator(x,k), k


def main():
    root = Path(__file__).resolve().parent
    for line in (root/'INPUTS.sha256').read_text().splitlines():
        digest,name = line.split('  ')
        assert sha256((root/name).read_bytes()).hexdigest() == digest, name

    # F1: Actual origin-zero dynamics and every message pair through n=8.
    blank,first,observed_tail,prepared = {},{},{},set()
    for lam,mu in product(range(5), repeat=2):
        x0 = prepare(lam,mu)
        assert x0 not in prepared
        prepared.add(x0)
        x = x0
        selectors = []
        for n in range(9):
            expected = -1 if n in (0,2) else lam if n == 1 else mu
            assert decode(read(x)) == expected, ('F1',lam,mu,n,x)
            if n == 0: blank[x] = -1
            if n == 1:
                first[x] = lam
                assert read(x) == ((-lam)%5,3)
            if n == 2: assert x == x0
            if n in (0,2): assert read(x) == (mu,0)
            if n in (3,4,7,8):
                assert observed_tail.setdefault(x,mu) == mu
            if n < 8:
                x,k = step(x,n.bit_count() % 2)
                selectors.append(k)
        assert selectors[:3] == [2,2,4]

    # F2: Full100-point tail, both control choices, and exact visitation.
    tail = {}
    for mu,C,z,r in product(range(5),(2,3),(1,4),range(5)):
        A = 2*C*z*mu % 5
        x = tuple(v % 5 for v in (3*(A+C+2),3,3*(A-C-2),2,z-A-r,r))
        assert x not in tail
        tail[x] = mu
        assert forms(x) == (A,0,C,0,z)
    assert len(tail) == 100 and observed_tail == tail
    for x,mu in tail.items():
        for bit in (0,1):
            nxt,k = step(x,bit)
            assert k in (1,3,4) and tail.get(nxt) == mu, ('F2',x,bit)

    # F3/F4: Exact domain, semantic law, and unrestricted-decoder criterion.
    assert len(blank) == len(first) == 25
    assert not (set(blank)&set(first) or set(blank)&set(tail) or set(first)&set(tail))
    domain = {**blank,**first,**tail}
    rows,code_labels = [],{}
    fibres = Counter()
    for x,label in sorted(domain.items()):
        code = read(x)
        assert decode(code) == label, ('F3',x,label,code)
        assert code_labels.setdefault(code,label) == label, ('F4',x)
        fibres[code] += 1
        rows.append(x+(label,)+code)
    assert len(rows) == 150 and len(code_labels) == 25
    assert Counter(row[6] for row in rows) == Counter({i:25 for i in range(-1,5)})
    assert Counter(fibres.values()) == Counter({5:20,10:5})
    assert Counter(code_labels.values()) == Counter({-1:5,0:4,1:4,2:4,3:4,4:4})
    cross = 0
    for i,left in enumerate(rows):
        for right in rows[i+1:]:
            if left[6] != right[6]:
                assert left[7:] != right[7:], ('F4',left,right)
                cross += 1
    assert cross == 9375

    # F5: Complete affine reader identity and affine injective preparation.
    matrix = ((1,1,1,4,0,0),(2,1,0,1,1,1))
    offset = (4,3)
    for x in product(range(5), repeat=6):
        linear = tuple((sum(a*b for a,b in zip(row,x))+t)%5 for row,t in zip(matrix,offset))
        assert linear == read(x), ('F5',x)
    assert (matrix[0][0]*matrix[1][4]-matrix[0][4]*matrix[1][0]) % 5 == 1
    base = prepare(0,0)
    vl,vm = (0,0,0,0,3,2),(3,0,3,0,1,3)
    for lam,mu in product(range(5),repeat=2):
        assert prepare(lam,mu) == tuple((b+lam*l+mu*m)%5 for b,l,m in zip(base,vl,vm))
    assert (vl[4]*vm[0]-vl[0]*vm[4]) % 5 != 0

    # F6: Independent affine-matrix dynamics and full native-state scan.
    from check_independent import run
    other,counts = run()
    assert rows == other, ('F6','row mismatch')
    assert counts['tail_edges'] == 200

    stream = ''.join(','.join(map(str,row))+'\n' for row in rows).encode('ascii')
    print('F1 PASS preparations=25 actual_checkpoints=225 updates=200 prefix=2,2,4')
    print('F2 PASS tail_states=100 control_edges=200 actual_cover_times=3,4,7,8')
    print('F3 PASS blank=25 first=25 tail=100 exact_domain=150 zero_messages=INCLUDED')
    print('F4 PASS cross_label_pairs=9375 conflicts=0 output_codes=25 fibres=20x5,5x10')
    print('F5 PASS reader_affine_rank=2 preparation_affine_rank=2 native_states=15625')
    print('F6 PASS independent_rows=150 matrix_dynamics=AGREE')
    print('ROWS_SHA256 '+sha256(stream).hexdigest())
    print('RESULT PASS alternate_preparation_affine=YES degree_minimum=1 coordinate_minimum=2')


if __name__ == '__main__':
    try:
        main()
    except AssertionError as exc:
        print('RESULT FAIL '+str(exc))
