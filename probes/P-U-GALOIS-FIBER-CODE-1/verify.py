#!/usr/bin/env python3
"""Exact audit of the specified L1 code; no physical read is executed."""

from fractions import Fraction as Q
from itertools import product


def scalar(x):
    return (Q(x), Q(0), Q(0), Q(0))


Z, O = scalar(0), scalar(1)
J = (Q(0), Q(1), Q(0), Q(0))


def add(*xs):
    return tuple(sum(t, Q(0)) for t in zip(*xs)) if xs else Z


def scale(x, q):
    return tuple(q * a for a in x)


def mul(x, y):
    a = [Q(0)] * 7
    for i in range(4):
        for k in range(4):
            a[i + k] += x[i] * y[k]
    for i in range(6, 3, -1):
        for k in range(i - 4, i):
            a[k] -= a[i]
    return tuple(a[:4])


def power(x, n):
    r = O
    for _ in range(n):
        r = mul(r, x)
    return r


def sigma(x, a):
    return add(*(scale(power(J, a * i), x[i]) for i in range(4)))


def star(m):
    return [[sigma(x, 4) for x in col] for col in zip(*m)]


def mm(a, b):
    return [[add(*(mul(x, y) for x, y in zip(row, col)))
             for col in zip(*b)] for row in a]


def gram(a):
    return mm(star(a), a)


def native(x, index):
    a, b, c, d, q, r = x
    ys = ((b, a, d, c, q, r),
          (-c, -d, -a, -b, -q, -r),
          (2-c, 1-d+r, 2-a, 1-b-r, 1-q, -r),
          (2-a, 1-b, 3-c, 4-d, 1-q, 1-r),
          (2-a, 1-b, 3-c, 4-d, 2-q, 1-r))
    return tuple(t % 5 for t in ys[index])


def tick(x, bit):
    return native(x, (sum(x) + 2 * bit) % 5)


def antecedent(s, h):
    xs = {1: (2-h, 1, 3, 4, h, 1),
          2: (2-h, 1, 3, 4, h+1, 1),
          3: (0, 0, -h, 0, h+1, 2),
          4: (0, 0, -h, 0, h+2, 2)}
    return tuple(t % 5 for t in xs[s])


def aggregate(points, rows):
    out = {}
    for p, row in zip(points, rows):
        out[p] = [add(x, y) for x, y in zip(out.get(p, [Z]*4), row)]
    return out


def main():
    tau = ((0, 4, 0, 4, 4), (2, 1, 1, 3, 1))
    sheet_images = [[set() for _ in range(5)] for _ in range(2)]
    final_images = [set() for _ in range(5)]
    for x in product(range(5), repeat=6):
        s = sum(x) % 5
        for i in range(5):
            assert native(native(x, i), i) == x
        for b in (0, 1):
            y = tick(x, b)
            assert sum(y) % 5 == tau[b][s]
            sheet_images[b][s].add(y)
        y = x
        for b in (0, 1, 1):
            y = tick(y, b)
        assert sum(y) % 5 == 1
        final_images[s].add(y)
    assert all(len(z) == 3125 for row in sheet_images for z in row)
    assert all(len(z) == 3125 and z == final_images[0] for z in final_images)

    marks = (1, 2, 4, 3)
    hmat = ((1, 1, 1, 1), (1, -1, 1, -1),
            (1, 1, -1, -1), (1, -1, -1, 1))
    assert all(sum(hmat[k][a]*hmat[k][b] for k in range(4))
               == 4*int(a == b) for a in range(4) for b in range(4))
    g = add(O, scale(J, 2), scale(power(J, 4), 2))
    assert mul(g, g) == scalar(5) and sigma(g, 4) == g
    c = scale(g, Q(1, 10))
    embeddings = [[power(J, a*i) for i in range(1, 5)] for a in marks]
    source_gram = [[scalar(int(i == k)-Q(1, 5)) for k in range(4)]
                   for i in range(4)]
    ids = [(k, a) for k in range(4) for a in range(4)]
    points = [antecedent(marks[a], marks[k]) for k, a in ids]
    assert len(set(points)) == 16
    assert all(sum(p) % 5 == marks[a] for p, (_, a) in zip(points, ids))
    v = [[mul(scale(c, hmat[k][a]), t) for t in embeddings[a]] for k, a in ids]
    histories = [points]
    prefixes = []
    for n in range(4):
        pts = histories[n]
        out = aggregate(pts, v)
        assert len(out) == (16, 8, 8, 4)[n]
        assert gram(list(out.values())) == source_gram
        for i, (k, a) in enumerate(ids):
            for j, (l, b) in enumerate(ids):
                same = (a == b if n == 0 else
                        (a == 1) == (b == 1) if n < 3 else True)
                assert (pts[i] == pts[j]) == (k == l and same)
        prefixes.append(out)
        if n < 3:
            histories.append([tick(p, (0, 1, 1)[n]) for p in pts])
    endpoints = [(h, 0, 0, 0, (1-h) % 5, 0) for h in marks]
    w = [prefixes[3][p] for p in endpoints]
    assert w == [[add(*(mul(scale(c, hmat[k][a]), embeddings[a][i])
                       for a in range(4))) for i in range(4)] for k in range(4)]
    low = [[scalar(Q(1, 4)) for _ in range(4)] for _ in range(4)]
    high = [[scalar(int(i == k)-Q(1, 4)) for k in range(4)] for i in range(4)]
    inverse = mm([[scalar(int(i == k)+1) for k in range(4)] for i in range(4)], star(w))
    identity = [[scalar(int(i == k)) for k in range(4)] for i in range(4)]
    assert mm(inverse, w) == identity and mm(w, inverse) == identity
    for o, p in enumerate((low, high)):
        dw = [row if (k == 0) == (o == 0) else [Z]*4 for k, row in enumerate(w)]
        assert dw == mm(w, p)
        assert mm(star(w), dw) == mm(source_gram, p)
        d = [[scalar(int(i == k and ((i == 0) == (o == 0))))
              for k in range(4)] for i in range(4)]
        for i in range(4):
            for j in range(4):
                rho = [[scalar(int(a == i and b == j)) for b in range(4)]
                       for a in range(4)]
                assert mm(mm(d, mm(mm(w, rho), inverse)), d) == mm(
                    mm(w, mm(mm(p, rho), p)), inverse)
    assert w[0] == [scale(c, -1)]*4
    # Alternative orthogonal identity template: same prefix Grams, other output.
    vi = [[mul(scale(g, Q(int(k == a), 5)), t) for t in embeddings[a]]
          for k, a in ids]
    assert all(gram(list(aggregate(pts, vi).values())) == source_gram for pts in histories)
    assert [aggregate(points, vi)[p] for p in points] != v
    # A=1 has shifted coordinates (-1,-1,-1,-1).
    ones = [[scalar(-1)] for _ in range(4)]
    final = mm(w, ones)
    assert final == [[scale(g, Q(2, 5))], [Z], [Z], [Z]]
    assert gram(final) == [[scalar(Q(4, 5))]]
    dephased = {p: Z for p in endpoints}
    for p, row in zip(histories[3], mm(v, ones)):
        dephased[p] = add(dephased[p], mul(sigma(row[0], 4), row[0]))
    assert [dephased[p] for p in endpoints] == [scalar(Q(1, 5))]*4
    assert mm(low, [[Z] for _ in range(4)]) == [[Z] for _ in range(4)]
    print('NATIVE sheets=5 size=3125 complete_state_domain=15625 PASS')
    print('NATIVE support=16,8,8,4 common_partitions=discrete;134|2;134|2;1234 PASS')
    print('GRAM every_prefix=I4-ones4/5 all_later_times=sheet_bijection_induction PASS')
    print('LOW/HIGH shifted_chart=j*iota_B0 effects=ones4/4,I4-ones4/4 PASS')
    print('POST_STATE ideal_coarse_read operator_basis=16 per_branch PASS')
    print('PREPARATION alternative_orthogonal_template=isometric selection=NOT_DERIVED PASS')
    print('PHYSICAL preparation,event,occurrence,record,reset,family,layer_gate=NOT_SUPPLIED')


if __name__ == '__main__':
    main()
