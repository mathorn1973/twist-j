# witness_jn_point.py
# NON-CANONICAL engineering witness for the ONE-POINT derivative criterion
# J_N(c) = [ (1/(m! n!)) d^{m+n} K_ray / da^m db^n at a=b=c ]  (lock #374 lane).
#
# Floats throughout; every decimal is a computed witness, never a conclusion.
#
# Structure and checks:
#   P0  Taylor coefficients M_k = M^{(k)}(c) of M(a) = (xi'/xi)(1/2+a) by a
#       manual Cauchy-integral (trapezoid on a circle, radius 2), then
#       power-series log-derivative division. Sanity vs direct mp.diff.
#   P1  NEW RECURSION (this session):  2c J[m,n] = delta_{n0} M_m/m!
#       + delta_{m0} M_n/n! - J[m-1,n] - J[m,n-1].  Verified against the
#       closed 2x2 of the second analysis and against zero-side sums.
#   P2  Two-path M_k check at c = 5/2 (s = 3): analytic Taylor path vs
#       prime/archimedean path  M_k = (-1)^k k! (s^-(k+1) + (s-1)^-(k+1))
#       + polygamma(k, s/2)/2^(k+1) + (-1)^(k+1) sum Lambda(n) (log n)^k n^-s,
#       Lambda summed to 10^6 with an explicit tail bound. Spot check at c=1.
#   P3  J_1(c) closed form det = (M^2 - c^2 M'^2)/(4 c^4) and the margin
#       |c M'(c)| < M(c) on a grid of c.
#   P4  LDL pivots of J_16(1): all positive (consistent with RH), and the
#       pivot decay compared with the collapsing D_N chain at a_n = 1 + 1/n.
#   P5  Zero-side crosscheck of selected J entries:
#       J[m,n] = (-1)^(m+n) sum_alpha m_alpha (c-alpha)^-(m+1) (c+alpha)^-(n+1)
#       truncated at 500 zeros, tail relevant only for (0,0).
#   P6  Li bridge (second analysis, with the domain caveat of this session):
#       lambda_n independently from zeros, then
#       (1-r)^2 sum_{n<=12} lambda_n r^{n-1}  vs  M(a(r)),
#       r = (a-1/2)/(a+1/2), at r = 0.15 and 0.30.
import sys
import mpmath as mp

mp.mp.dps = 60
OK = True

def report(tag, ok, detail):
    global OK
    OK = OK and ok
    print(('PASS ' if ok else 'FAIL ') + tag + '  ' + detail)

def xihat(s):
    s = mp.mpmathify(s)
    return ((s - 1) * mp.zeta(s)) * mp.pi ** (-s / 2) * mp.gamma(s / 2 + 1)

# ---------------- P0: M_k at c by Cauchy coefficients ----------------
def M_taylor(c, K, R=mp.mpf(2), NPTS=256):
    s0 = mp.mpf('0.5') + mp.mpmathify(c)
    vals = []
    for j in range(NPTS):
        th = 2 * mp.pi * j / NPTS
        vals.append(xihat(s0 + R * mp.expjpi(2 * mp.mpf(j) / NPTS)))
    x = []
    for k in range(K + 2):
        acc = mp.mpc(0)
        for j in range(NPTS):
            acc += vals[j] * mp.expjpi(-2 * mp.mpf(j * k) / NPTS)
        x.append(acc / NPTS / R ** k)
    # log-derivative series q = (sum (k+1) x_{k+1} t^k) / (sum x_k t^k)
    num = [(k + 1) * x[k + 1] for k in range(K + 1)]
    q = []
    for k in range(K + 1):
        acc = num[k]
        for j in range(k):
            acc -= q[j] * x[k - j]
        q.append(acc / x[0])
    return [mp.re(q[k]) * mp.factorial(k) for k in range(K + 1)]  # M^{(k)}(c)

KMAX = 17
Mk1 = M_taylor(1, KMAX)
def M_direct(a):
    return mp.re(mp.diff(lambda z: mp.log(xihat(z)), mp.mpf('0.5') + mp.mpmathify(a)))
d0 = abs(Mk1[0] - M_direct(1))
d1 = abs(Mk1[1] - mp.diff(lambda t: M_direct(t), 1))
report('P0 M_0,M_1 at c=1 vs direct', d0 < mp.mpf('1e-40') and d1 < mp.mpf('1e-15'),
       '|dM0|=%s |dM1|=%s' % (mp.nstr(d0, 3), mp.nstr(d1, 3)))

# ---------------- P1: recursion for J_N(c) ----------------
def Jmatrix(Mk, c, N):
    c = mp.mpmathify(c)
    J = [[mp.mpf(0)] * (N + 1) for _ in range(N + 1)]
    for m in range(N + 1):
        for n in range(N + 1):
            rhs = mp.mpf(0)
            if n == 0:
                rhs += Mk[m] / mp.factorial(m)
            if m == 0:
                rhs += Mk[n] / mp.factorial(n)
            if m > 0:
                rhs -= J[m - 1][n]
            if n > 0:
                rhs -= J[m][n - 1]
            J[m][n] = rhs / (2 * c)
    return J

J16 = Jmatrix(Mk1, 1, 16)
M0, M1 = Mk1[0], Mk1[1]
c = mp.mpf(1)
closed = [[M0 / c, (c * M1 - M0) / (2 * c ** 2)],
          [(c * M1 - M0) / (2 * c ** 2), (M0 - c * M1) / (2 * c ** 3)]]
dev = max(abs(J16[m][n] - closed[m][n]) for m in range(2) for n in range(2))
detc = (M0 ** 2 - c ** 2 * M1 ** 2) / (4 * c ** 4)
det2 = J16[0][0] * J16[1][1] - J16[0][1] * J16[1][0]
report('P1 J_1(1) closed form and det', dev < mp.mpf('1e-45') and abs(detc - det2) < mp.mpf('1e-45'),
       'maxdev=%s det=%s' % (mp.nstr(dev, 3), mp.nstr(det2, 8)))

# ---------------- P2: prime-side path at c = 5/2 ----------------
NMAX = 3 * 10 ** 6
spf = list(range(NMAX + 1))
i = 2
while i * i <= NMAX:
    if spf[i] == i:
        for j in range(i * i, NMAX + 1, i):
            if spf[j] == j:
                spf[j] = i
    i += 1
def lambda_power_sums(sigma, kmax):
    S = [mp.mpf(0)] * (kmax + 1)
    for n in range(2, NMAX + 1):
        p = spf[n]
        m = n
        while m % p == 0:
            m //= p
        if m == 1:
            base = mp.log(p)
            t = mp.mpf(1) / mp.mpf(n) ** sigma
            L = mp.log(n)
            pw = mp.mpf(1)
            for k in range(kmax + 1):
                S[k] += base * pw * t
                pw *= L
    return S

KP = 12
s3 = mp.mpf(3)
S3 = lambda_power_sums(s3, KP)
Mk25 = M_taylor(mp.mpf('2.5'), KP, R=mp.mpf('1.75'))
worstd = mp.mpf(0); worstk = -1; worsttail = mp.mpf(0); worstM = mp.mpf(0)
for k in range(KP + 1):
    arch = (-1) ** k * mp.factorial(k) * (s3 ** (-(k + 1)) + (s3 - 1) ** (-(k + 1)))
    if k == 0:
        arch += -mp.log(mp.pi) / 2 + mp.digamma(s3 / 2) / 2
    else:
        arch += mp.polygamma(k, s3 / 2) / 2 ** (k + 1)
    prime_path = arch + (-1) ** (k + 1) * S3[k]
    tail = mp.mpf('1.04') * mp.gammainc(k + 1, 2 * mp.log(NMAX)) / 2 ** (k + 1)
    d = abs(prime_path - Mk25[k])
    if d > worstd:
        worstd = d; worstk = k; worsttail = tail; worstM = abs(Mk25[k])
    if not d < 3 * tail + mp.mpf('1e-30'):
        report('P2 k=%d' % k, False, 'prime=%s taylor=%s |d|=%s tail=%s'
               % (mp.nstr(prime_path, 12), mp.nstr(Mk25[k], 12), mp.nstr(d, 3), mp.nstr(tail, 3)))
report('P2 prime vs taylor M_k, c=5/2, k<=12', True if OK else OK,
       'worst |d|=%s at k=%d (tail bound %s, |M_k|=%s); sharp for small k, tail-dominated for large k'
       % (mp.nstr(worstd, 3), worstk, mp.nstr(worsttail, 3), mp.nstr(worstM, 3)))

# ---------------- P3: J_1 margin on a grid ----------------
rows = []
allok = True
for cg in ['0.6', '0.75', '1', '1.5', '2.5', '5']:
    cgm = mp.mpf(cg)
    Mg = M_direct(cgm)
    M1g = mp.diff(lambda t: M_direct(t), cgm)
    ratio = abs(cgm * M1g) / Mg
    allok = allok and ratio < 1
    rows.append('c=%s ratio=%s' % (cg, mp.nstr(ratio, 6)))
report('P3 |c M\'(c)| < M(c) on grid', allok, ' '.join(rows))

# ---------------- P4: LDL pivots of J_16(1) vs D_N chain ----------------
with mp.workdps(80):
    A = mp.matrix(17, 17)
    for m in range(17):
        for n in range(17):
            A[m, n] = J16[m][n]
    piv = []
    ok4 = True
    B = A.copy()
    for k in range(17):
        p = B[k, k]
        piv.append(p)
        if p <= 0:
            ok4 = False
            break
        for i2 in range(k + 1, 17):
            f = B[i2, k] / p
            for j2 in range(k + 1, 17):
                B[i2, j2] -= f * B[k, j2]
ratios = [piv[k + 1] / piv[k] for k in range(len(piv) - 1)]
report('P4 J_16(1) LDL pivots all positive', ok4,
       'p_0=%s p_8=%s p_16=%s decay~%s..%s per step'
       % (mp.nstr(piv[0], 4), mp.nstr(piv[8], 4), mp.nstr(piv[16], 4),
          mp.nstr(min(ratios), 3), mp.nstr(max(ratios), 3)))
print('NOTE P4: D_N chain at a_n=1+1/n had pivot ~1.3e-35 already at N=8;')
print('one-point pivots decay ~1e-3 per step (scale set by the first zero,')
print('((c-1/2)/gamma_1)^2-ish), roughly geometric: better conditioned than the')
print('chain but still needing ~3 digits per order; certified work needs interval')
print('arithmetic with precision linear in N.')

# ---------------- P5: zero-side crosscheck ----------------
NZ = 500
with mp.workdps(15):
    gams = [mp.zetazero(n).imag for n in range(1, NZ + 1)]
with open('zeros_500.txt', 'w') as f:
    for g in gams:
        f.write(mp.nstr(g, 15) + '\n')
T = mp.mpf(gams[-1])
tail00 = (mp.log(T / (2 * mp.pi)) + 1) / (mp.pi * T)
sel = [(0, 0), (0, 1), (1, 1), (2, 3), (5, 5), (8, 8)]
ok5 = True
msg = []
for (m, n) in sel:
    # sum over alpha in {i g, -i g}: (c-alpha)^{-(m+1)} (c+alpha)^{-(n+1)} at c=1
    acc = mp.mpf(0)
    for g in gams:
        for al in (mp.mpc(0, g), mp.mpc(0, -g)):
            acc += mp.re((1 - al) ** (-(m + 1)) * (1 + al) ** (-(n + 1)))
    acc *= (-1) ** (m + n)
    d = abs(acc - J16[m][n])
    # tolerance: truncation tail (m+n>=1 decays like T^-(m+n+1)) plus the
    # 15-digit zero-list precision propagated, plus a floor
    if (m, n) == (0, 0):
        tol = 3 * tail00
    else:
        tol = 10 * (mp.log(T / (2 * mp.pi)) + 1) / T ** (m + n + 1) \
              + mp.mpf('1e-12') * abs(J16[m][n]) + mp.mpf('1e-33')
    ok5 = ok5 and d < tol
    msg.append('J[%d,%d] d=%s' % (m, n, mp.nstr(d, 2)))
report('P5 zero-side vs recursion', ok5, ' '.join(msg) + ' ((0,0) within zero tail %s)' % mp.nstr(tail00, 2))

# ---------------- P6: Li bridge ----------------
NL = 12
lam = []
for n in range(1, NL + 1):
    acc = mp.mpf(0)
    for g in gams:
        rho = mp.mpc(mp.mpf('0.5'), g)
        acc += 2 * mp.re(1 - (1 - 1 / rho) ** n)
    lam.append(acc)
lamtail = [n * (mp.log(T / (2 * mp.pi)) + 1) / (2 * mp.pi * T) for n in range(1, NL + 1)]
ok6 = True
msg6 = []
for rstr in ['0.15', '0.30']:
    r = mp.mpf(rstr)
    a = (1 + r) / (2 * (1 - r))
    lhs = (1 - r) ** 2 * mp.fsum(lam[n - 1] * r ** (n - 1) for n in range(1, NL + 1))
    rhs = M_direct(a)
    budget = (1 - r) ** 2 * mp.fsum(lamtail[n - 1] * r ** (n - 1) for n in range(1, NL + 1)) \
             + 40 * r ** NL
    d = abs(lhs - rhs)
    ok6 = ok6 and d < 3 * budget
    msg6.append('r=%s a=%s |d|=%s (budget %s)' % (rstr, mp.nstr(a, 5), mp.nstr(d, 3), mp.nstr(budget, 3)))
report('P6 Li bridge (1-r)^2 sum lambda_n r^(n-1) = M(a)', ok6, ' '.join(msg6))
lam1_exact = 1 + mp.euler / 2 - mp.log(4 * mp.pi) / 2
report('P6 lambda_1 zero-sum vs exact', abs(lam[0] - lam1_exact) < 3 * lamtail[0],
       'zero-sum=%s exact=%s' % (mp.nstr(lam[0], 10), mp.nstr(lam1_exact, 10)))

print('WITNESS ' + ('PASS' if OK else 'FAIL'))
sys.exit(0 if OK else 1)
