"""Author-code-blind exact check from the exposed formal preregistration.

Original code by A. M. Thorn / independent Codex scope-review session.
Apache-2.0. Universal CPTP claims require the accompanying written proof.
No scientific execution before the public joint pin.
"""

from fractions import Fraction as R


def mat(n, m, f):
    return [[R(f(i, j)) for j in range(m)] for i in range(n)]


def eye(n):
    return mat(n, n, lambda i, j: int(i == j))


def tr(a):
    return [list(c) for c in zip(*a)]


def mul(a, b):
    assert len(a[0]) == len(b)
    return [[sum(x*y for x, y in zip(row, col)) for col in zip(*b)]
            for row in a]


def plus(a, b):
    return [[x+y for x, y in zip(u, v)] for u, v in zip(a, b)]


def scaled(c, a):
    return [[c*x for x in row] for row in a]


def column(a, j):
    return [row[j] for row in a]


def outer(u, v):
    return [[x*y for y in v] for x in u]


def total(matrices, n, m):
    result = mat(n, m, lambda i, j: 0)
    for a in matrices:
        result = plus(result, a)
    return result


def rank(a):
    work = [row[:] for row in a]
    pivot_row = 0
    for j in range(len(work[0])):
        pivot = next((i for i in range(pivot_row, len(work)) if work[i][j]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        denominator = work[pivot_row][j]
        work[pivot_row] = [x/denominator for x in work[pivot_row]]
        for i in range(len(work)):
            if i != pivot_row and work[i][j]:
                coefficient = work[i][j]
                work[i] = [x-coefficient*y
                           for x, y in zip(work[i], work[pivot_row])]
        pivot_row += 1
        if pivot_row == len(work):
            break
    return pivot_row


def kraus_rank(kraus):
    # Choi rank equals rank of vectorized Kraus operators over C;
    # the concrete matrices here are rational, so exact Q rank is the same.
    return rank([[x for row in k for x in row] for k in kraus])


def density(kraus, vector):
    outputs = [[sum(x*y for x,y in zip(row, vector)) for row in k]
               for k in kraus]
    return total((outer(v, v) for v in outputs), 4, 4)


def block(a, b):
    n, m = len(a), len(b)
    return mat(n+m, n+m, lambda i,j:
               a[i][j] if i < n and j < n else
               b[i-n][j-n] if i >= n and j >= n else 0)


def check():
    h = ((1,1,1,1),(1,-1,1,-1),(1,1,-1,-1),(1,-1,-1,1))
    f = mat(4,4,lambda i,j: R(h[i][j],2))
    c = mat(16,4,lambda i,j: R(h[i//4][j],2) if i%4 == j else 0)
    identity = eye(16)
    p = mul(c, tr(c))
    q = plus(identity, scaled(-1,p))
    d = mul(f,tr(c))
    zero4x16 = mat(4,16,lambda i,j: 0)
    zero4 = mat(4,4,lambda i,j: 0)
    native = mat(4,16,lambda k,j: int(j//4 == k))
    assert mul(tr(c),c) == mul(tr(f),f) == eye(4)
    assert mul(native,c) == f and mul(tr(native),native) != identity
    assert mul(q,q) == q and rank(q) == 12
    assert mul(d,c) == f and mul(d,q) == zero4x16

    five = [d] + [mat(4,16,lambda k,j,a=a: q[4*k+a][j]) for a in range(4)]
    seventeen = [d] + [mat(4,16,lambda row,j,k=k,a=a:
                         q[4*k+a][j] if row == k else 0)
                       for k in range(4) for a in range(4)]
    assert kraus_rank(five) == 5 and kraus_rank(seventeen) == 17
    for ks in (five,seventeen):
        assert total((mul(tr(k),k) for k in ks),16,16) == identity
        kc = [mul(k,c) for k in ks]
        kq = [mul(k,q) for k in ks]
        assert kc[0] == f and kq[0] == zero4x16
        assert all(a == zero4 for a in kc[1:])
        for i in range(4):
            for j in range(4):
                transported = total((outer(column(a,i),column(a,j)) for a in kc),4,4)
                assert transported == outer(column(f,i),column(f,j))
            for j in range(16):
                cross = total((outer(column(a,i),column(b,j))
                               for a,b in zip(kc,kq)),4,4)
                assert cross == zero4 and tr(cross) == zero4
        for j in range(16):
            output = total((outer(column(k,j),column(k,j)) for k in ks),4,4)
            assert [output[i][i] for i in range(4)] == [
                R(5,8) if i == j//4 else R(1,8) for i in range(4)]
        for k in range(4):
            complement_effect = total((outer(operator[k],operator[k])
                                       for operator in ks[1:]),16,16)
            expected_effect = total((outer(column(q,4*k+a),column(q,4*k+a))
                                     for a in range(4)),16,16)
            assert complement_effect == expected_effect
            assert rank(complement_effect) == 4
            assert mul(complement_effect,complement_effect) == scaled(R(3,4),complement_effect)

    raw0 = column(identity,0)
    assert density(five,raw0)[0][1] == -R(1,8)
    assert density(seventeen,raw0)[0][1] == R(1,16)
    effects = [total((outer(column(q,4*k+a),column(q,4*k+a))
                     for a in range(4)),16,16) for k in range(4)]
    assert total(effects,16,16) == q
    assert (R(1)+R(3,4)*sum(q[i][i] for i in range(16)))/16 == R(5,8)
    # Complex off-block effect uniqueness reduces to these four independent
    # real outer products. Real linear independence also gives complex one.
    simplex = mat(4,4,lambda i,j: R(int(i == j))-R(1,4))
    products = [outer(column(simplex,k),column(simplex,k)) for k in range(4)]
    diagonal_minor = mat(4,4,lambda i,j: products[j][i][i])
    assert diagonal_minor == mat(4,4,lambda i,j:R(int(i == j),2)+R(1,16))
    assert rank(diagonal_minor) == 4

    point_exact = [mat(4,16,lambda k,j,a=a:
                       int(j//4 == k and j%4 == a)) for a in range(4)]
    assert total((mul(tr(k),k) for k in point_exact),16,16) == identity
    for j in range(16):
        out = density(point_exact,column(identity,j))
        assert out == mat(4,4,lambda i,k:int(i == k == j//4))
    alpha = [R(1,2)]*4
    code_alpha = [sum(x*y for x,y in zip(row,alpha)) for row in c]
    assert density(point_exact,code_alpha) == scaled(R(1,4),eye(4))

    v4 = mat(16,16,lambda i,j: f[i//4][j%4]*f[i%4][j//4]*h[j//4][j%4])
    assert mul(tr(v4),v4) == identity
    control = [mat(4,16,lambda k,j,mu=mu: v4[4*k+mu][j]) for mu in range(4)]
    assert kraus_rank(control) == 4
    assert mul(control[0],c) == f
    assert all(mul(k,c) == zero4 for k in control[1:])
    for j in range(16):
        out = density(control,column(identity,j))
        assert [out[i][i] for i in range(4)] == [R(1,4)]*4

    u20 = mat(20,20,lambda i,j:
               q[i][j] if i < 16 and j < 16 else
               c[i][j-16] if i < 16 and j >= 16 else
               d[i-16][j] if i >= 16 and j < 16 else 0)
    assert mul(tr(u20),u20) == mul(u20,tr(u20)) == eye(20)
    b = mat(16,16,lambda i,j: f[i//4][j//4] if i%4 == j%4 else 0)
    loader = mat(16,16,lambda i,j: h[i//4][i%4]*b[i][j])
    entrance = mat(16,4,lambda i,j:int(i == j))
    assert mul(loader,entrance) == c
    assert mul(tr(loader),loader) == identity
    permutation = list(range(20))
    for a in range(4):
        permutation[a],permutation[16+a] = permutation[16+a],permutation[a]
    swap = mat(20,20,lambda i,j:int(j == permutation[i]))
    factors = (block(identity,f),block(loader,eye(4)),swap,block(tr(loader),eye(4)))
    assembled = eye(20)
    for factor in factors:
        assembled = mul(assembled,factor)
    assert assembled == u20
    loaded = mat(20,4,lambda i,j:c[i][j] if i < 16 else 0)
    desired = mat(20,4,lambda i,j:0 if i < 16 else f[i-16][j])
    assert mul(u20,loaded) == desired
    assert mul(block(tr(loader),eye(4)),loaded) == mat(20,4,lambda i,j:int(i == j))

    return ('INDEPENDENT_BREAKER_B PASS bound=5/8 auxiliary=5 '
            'choi_ranks=5,17 raw=16 matrix_units=16')


if __name__ == '__main__':
    print(check())
