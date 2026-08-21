# breaker_offcritical_detection.py
# NON-CANONICAL synthetic breaker for the ray/one-point criteria (lock #374 lane).
#
# SYNTHETIC MODEL, labeled: a finite zero multiset Z = {first 120 true ordinates
# on the critical line, both signs} U {injected off-critical quadruples (x,y)},
# alpha-coordinates, quadruple {(+-x, +-y)}. Nothing here is a statement about
# zeta; the model tests the MECHANISM (off-critical orbit => negative direction)
# and measures the detection cost of three instruments:
#
#   I1  ray chain      a_n = 1 + 1/n, N <= 24      (ill conditioned, per warning)
#   I2  spread chain   a_i = 0.6 + 0.4 (i-1)       (same theorem, spread nodes)
#   I3  one-point      J_N(1), N <= 48             (derivative matrices)
#
# K(a,b) = sum_alpha 1/((a-alpha)(b+alpha));
# J[m,n] = (-1)^(m+n) sum_alpha (c-alpha)^-(m+1) (c+alpha)^-(n+1), c = 1.
# Detection: sequential LDL pivots (= leading-minor ratios); first pivot
# < -NOISE declares N*. Signs of LDL pivots give inertia (Sylvester).
# Chains run at dps 300 (their pivots collapse ~1e-6N); J at dps 60.
#
# Also: the Li/Abel radius mechanism made quantitative: R = min |1 - 1/rho|
# over the symmetric multiset; at a synthetic LOW quadruple the partial sums
# of the bridge series diverge for r > R while the kernel value stays finite.
import sys
import mpmath as mp

def load_zeros():
    try:
        with open('zeros_500.txt') as f:
            return [mp.mpf(line.strip()) for line in f][:120]
    except OSError:
        with mp.workdps(15):
            return [mp.mpf(mp.zetazero(n).imag) for n in range(1, 121)]

with mp.workdps(60):
    BASE = load_zeros()

def zero_set(quads):
    Z = []
    for g in BASE:
        Z.append(mp.mpc(0, g)); Z.append(mp.mpc(0, -g))
    for (x, y) in quads:
        x = mp.mpf(x); y = mp.mpf(y)
        for al in (mp.mpc(x, y), mp.mpc(-x, y), mp.mpc(x, -y), mp.mpc(-x, -y)):
            Z.append(al)
    return Z

def chain_matrix(Z, pts):
    N = len(pts)
    A = [[mp.mpf(0)] * N for _ in range(N)]
    for i in range(N):
        for j in range(i, N):
            v = mp.re(mp.fsum(1 / ((pts[i] - al) * (pts[j] + al)) for al in Z))
            A[i][j] = v; A[j][i] = v
    return A

def J_matrix(Z, c, N):
    c = mp.mpf(c)
    w1 = []; w2 = []
    for al in Z:
        p1 = [mp.mpc(1)]; p2 = [mp.mpc(1)]
        i1 = 1 / (c - al); i2 = 1 / (c + al)
        for _ in range(N + 1):
            p1.append(p1[-1] * i1); p2.append(p2[-1] * i2)
        w1.append(p1); w2.append(p2)
    A = [[mp.mpf(0)] * (N + 1) for _ in range(N + 1)]
    for m in range(N + 1):
        for n in range(m, N + 1):
            acc = mp.fsum((w1[idx][m + 1] * w2[idx][n + 1]).real for idx in range(len(Z)))
            v = acc * (-1) ** (m + n)
            A[m][n] = v; A[n][m] = v
    return A

def ldl_pivots_simple(A):
    N = len(A)
    B = [row[:] for row in A]
    piv = []
    for k in range(N):
        p = B[k][k]
        piv.append(p)
        if p == 0:
            break
        for i in range(k + 1, N):
            f = B[i][k] / p
            for j in range(k + 1, N):
                B[i][j] -= f * B[k][j]
    return piv

def analyze(piv, noise):
    first = None
    negs = 0
    for k, p in enumerate(piv):
        if p < -noise:
            negs += 1
            if first is None:
                first = k + 1
    return first, negs, min(piv)

print('SYNTHETIC MODEL: 120 on-line ordinates + injected quadruples, c = 1.')
print('All numbers are computed witnesses on the model, not statements about zeta.')
print()

CONFIGS = [
    ('single x=0.10 y=14.1347', [('0.10', '14.1347')]),
    ('single x=0.25 y=14.1347', [('0.25', '14.1347')]),
    ('single x=0.40 y=14.1347', [('0.40', '14.1347')]),
    ('single x=0.25 y=30',      [('0.25', '30')]),
    ('single x=0.25 y=60',      [('0.25', '60')]),
    ('double (0.25,14.1347)+(0.25,60)', [('0.25', '14.1347'), ('0.25', '60')]),
]
NCH = 24
NJ = 48

for name, quads in CONFIGS:
    with mp.workdps(300):
        Z = zero_set(quads)
        ray = [1 + mp.mpf(1) / n for n in range(1, NCH + 1)]
        spread = [mp.mpf('0.6') + mp.mpf('0.4') * i for i in range(NCH)]
        p1 = ldl_pivots_simple(chain_matrix(Z, ray))
        p2 = ldl_pivots_simple(chain_matrix(Z, spread))
        f1, n1, m1 = analyze(p1, mp.mpf('1e-250'))
        f2, n2, m2 = analyze(p2, mp.mpf('1e-250'))
    with mp.workdps(300):
        Z = zero_set(quads)
        p3 = ldl_pivots_simple(J_matrix(Z, 1, NJ))
        f3, n3, m3 = analyze(p3, mp.mpf('1e-250'))
    print(name)
    print('  I1 ray 1+1/n   (N<=%d): first neg pivot N* = %s, negs %d, min pivot %s'
          % (NCH, f1, n1, mp.nstr(m1, 3)))
    print('  I2 spread      (N<=%d): first neg pivot N* = %s, negs %d, min pivot %s'
          % (NCH, f2, n2, mp.nstr(m2, 3)))
    print('  I3 J_N(1)      (N<=%d): first neg pivot N* = %s, negs %d (expect up to %d), min pivot %s'
          % (NJ, f3, n3, 2 * len(quads), mp.nstr(m3, 3)))
    print()

with mp.workdps(300):
    Z0 = zero_set([])
    pc1 = ldl_pivots_simple(chain_matrix(Z0, [1 + mp.mpf(1) / n for n in range(1, NCH + 1)]))
    fc1, nc1, mc1 = analyze(pc1, mp.mpf('1e-250'))
with mp.workdps(300):
    Z0 = zero_set([])
    pc3 = ldl_pivots_simple(J_matrix(Z0, 1, NJ))
    fc3, nc3, mc3 = analyze(pc3, mp.mpf('1e-250'))
print('control (no injection): ray negs %d (min pivot %s), J_%d(1) negs %d (min pivot %s)'
      % (nc1, mp.nstr(mc1, 3), NJ, nc3, mp.nstr(mc3, 3)))
print()

# Li/Abel radius mechanism, quantitative
print('Li/Abel radius R = min |1 - 1/rho| over the symmetric multiset:')
with mp.workdps(60):
    for (x, y) in [('0.25', '14.1347'), ('0.40', '14.1347'), ('0.40', '2')]:
        xm, ym = mp.mpf(x), mp.mpf(y)
        rho = mp.mpc(mp.mpf('0.5') + xm, ym)
        R = abs(1 - 1 / rho)   # the |u|<1 member; radius = min(|u|) = this
        print('  x=%s y=%s: R = %s (deficit 1-R = %s)' % (x, y, mp.nstr(R, 8), mp.nstr(1 - R, 3)))
    # divergence demo at the aggressive low quadruple x=0.40, y=2
    Zq = zero_set([('0.40', '2')])
    def Msyn(a):
        return mp.re(mp.fsum(1 / (a - al) for al in Zq))
    lam = []
    NLAM = 220
    us = [1 - 1 / (mp.mpf('0.5') + al) for al in Zq]
    pw = [mp.mpc(1) for _ in us]
    for n in range(1, NLAM + 1):
        for i in range(len(us)):
            pw[i] *= us[i]
        lam.append(mp.re(mp.fsum(1 - p for p in pw)))
    for rstr in ['0.80', '0.95']:
        r = mp.mpf(rstr)
        a = (1 + r) / (2 * (1 - r))
        target = Msyn(a)
        partial120 = (1 - r) ** 2 * mp.fsum(lam[n - 1] * r ** (n - 1) for n in range(1, 121))
        partial220 = (1 - r) ** 2 * mp.fsum(lam[n - 1] * r ** (n - 1) for n in range(1, 221))
        print('  r=%s (R=0.913...): M_syn=%s  partial_120=%s  partial_220=%s  %s'
              % (rstr, mp.nstr(target, 6), mp.nstr(partial120, 6), mp.nstr(partial220, 6),
                 'CONVERGING' if abs(partial220 - target) < abs(partial120 - target) else 'DIVERGING'))

print()
print('BREAKER DONE')
sys.exit(0)
