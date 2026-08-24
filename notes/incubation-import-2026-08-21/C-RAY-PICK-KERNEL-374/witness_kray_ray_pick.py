# witness_kray_ray_pick.py
# NON-CANONICAL engineering witness for the ray Pick kernel note under
# junction lock mathorn1973/twist-j#374 (C-RH-WEIL-NORM-JUNCTION-1-N).
#
# Floating point throughout, every decimal below is a computed witness,
# not an assertion of canon grade. No zero table enters any claim; the
# zero list is used only to smoke-test an identity that is proved by hand.
#
# Objects. X(z) = xi(1/2+z), M(a) = X'(a)/X(a) = (xi'/xi)(1/2+a),
# K_ray(a,b) = (M(a)+M(b))/(a+b) for a,b > 1/2.
#
# W1  Hadamard identity K_ray(a,b) = sum_alpha m_alpha/((a-alpha)(b+alpha))
#     against the first NZ zeros on the line, with an engineering tail
#     estimate (1/pi)(log(T/2pi)+1)/T.
# W2  D_N = det[K_ray(a_i,a_j)]_{i,j<=N} > 0 for N=1..8, a_n = 1+1/n,
#     entries computed from xi'/xi directly (no zeros involved).
# W3  M(1/2) = lambda_1 = 1 + euler/2 - log(4 pi)/2  (Li lambda_1).
# W4  Unconditional diagonal positivity: M(a) > 0 on a grid a > 1/2.
# W5  Prime/archimedean split at sigma = a+1/2 in {2,3}:
#     M(a) = 1/sigma + 1/(sigma-1) - (1/2)log pi + (1/2)psi(sigma/2)
#            - sum_{n>=2} Lambda(n)/n^sigma   (Lambda summed to 10^6).
import sys
import mpmath as mp

mp.mp.dps = 40
OK = True

def xihat(s):
    s = mp.mpmathify(s)
    return ((s - 1) * mp.zeta(s)) * mp.pi ** (-s / 2) * mp.gamma(s / 2 + 1)

def M(a):
    a = mp.mpmathify(a)
    return mp.re(mp.diff(lambda z: mp.log(xihat(z)), mp.mpf('0.5') + a))

def K(a, b):
    return (M(a) + M(b)) / (mp.mpmathify(a) + mp.mpmathify(b))

def report(tag, ok, detail):
    global OK
    OK = OK and ok
    print(('PASS ' if ok else 'FAIL ') + tag + '  ' + detail)

# ---------------- W1 Hadamard identity ----------------
NZ = 500
with mp.workdps(15):
    gams = [mp.zetazero(n).imag for n in range(1, NZ + 1)]
T = mp.mpf(gams[-1])
tail = (mp.log(T / (2 * mp.pi)) + 1) / (mp.pi * T)
print('W1 zeros used NZ=%d, T=%s, engineering tail estimate %s'
      % (NZ, mp.nstr(T, 8), mp.nstr(tail, 3)))
for (a, b) in [('0.7', '1.3'), ('0.6', '0.9'), ('1.0', '2.0')]:
    a_, b_ = mp.mpf(a), mp.mpf(b)
    s = mp.mpf(0)
    for g in gams:
        g_ = mp.mpf(g)
        s += 2 * mp.re(1 / ((a_ - 1j * g_) * (b_ + 1j * g_)))
    direct = K(a_, b_)
    diff = abs(direct - s)
    report('W1(%s,%s)' % (a, b), diff < 3 * tail,
           'K_ray=%s  zerosum=%s  |diff|=%s  (tail~%s)'
           % (mp.nstr(direct, 12), mp.nstr(s, 12), mp.nstr(diff, 3), mp.nstr(tail, 3)))

# ---------------- W2 determinant chain ----------------
N = 8
avals = [1 + mp.mpf(1) / n for n in range(1, N + 1)]
Mvals = [M(a) for a in avals]
Kmat = mp.matrix(N, N)
for i in range(N):
    for j in range(N):
        Kmat[i, j] = (Mvals[i] + Mvals[j]) / (avals[i] + avals[j])
dets = []
for n in range(1, N + 1):
    sub = mp.matrix(n, n)
    for i in range(n):
        for j in range(n):
            sub[i, j] = Kmat[i, j]
    dets.append(mp.det(sub))
allpos = all(d > 0 for d in dets)
report('W2 D_1..D_%d > 0' % N, allpos,
       ' '.join('D_%d=%s' % (n + 1, mp.nstr(d, 6)) for n, d in enumerate(dets)))
ev = mp.eigsy(Kmat, eigvals_only=True)
report('W2 min eigenvalue > 0', min(ev) > 0, 'lambda_min=%s' % mp.nstr(min(ev), 6))

# ---------------- W3 M(1/2) = lambda_1 ----------------
lam1 = 1 + mp.euler / 2 - mp.log(4 * mp.pi) / 2
m_half = M('0.5')
report('W3 M(1/2)=lambda_1', abs(m_half - lam1) < mp.mpf(10) ** (-25),
       'M(1/2)=%s  lambda_1=%s  |diff|=%s'
       % (mp.nstr(m_half, 25), mp.nstr(lam1, 25), mp.nstr(abs(m_half - lam1), 3)))

# ---------------- W4 diagonal positivity ----------------
grid = ['0.5001', '0.51', '0.6', '0.75', '1', '1.5', '2', '3', '5', '10']
vals = [(g, M(g)) for g in grid]
report('W4 M(a)>0 on grid', all(v > 0 for _, v in vals),
       ' '.join('M(%s)=%s' % (g, mp.nstr(v, 8)) for g, v in vals[:4]) + ' ...')

# ---------------- W5 prime/archimedean split ----------------
NMAX = 10 ** 6
lam = [mp.mpf(0)] * 0
# smallest-prime-factor sieve for Lambda(n), n <= NMAX
spf = list(range(NMAX + 1))
i = 2
while i * i <= NMAX:
    if spf[i] == i:
        for j in range(i * i, NMAX + 1, i):
            if spf[j] == j:
                spf[j] = i
    i += 1
def lambda_sum(sigma):
    s = mp.mpf(0)
    for n in range(2, NMAX + 1):
        p = spf[n]
        m = n
        while m % p == 0:
            m //= p
        if m == 1:
            s += mp.log(p) / mp.mpf(n) ** sigma
    return s
for sigma in [mp.mpf(2), mp.mpf(3)]:
    arch = 1 / sigma + 1 / (sigma - 1) - mp.log(mp.pi) / 2 + mp.digamma(sigma / 2) / 2
    formula = arch - lambda_sum(sigma)
    direct = M(sigma - mp.mpf('0.5'))
    tailb = mp.mpf('1.04') * sigma / (sigma - 1) * mp.mpf(NMAX) ** (1 - sigma)
    diff = abs(formula - direct)
    report('W5 sigma=%s' % mp.nstr(sigma, 2), diff < 3 * tailb,
           'formula=%s  direct=%s  |diff|=%s  (Lambda tail<=%s)'
           % (mp.nstr(formula, 15), mp.nstr(direct, 15), mp.nstr(diff, 3), mp.nstr(tailb, 3)))

print('WITNESS ' + ('PASS' if OK else 'FAIL'))
sys.exit(0 if OK else 1)
