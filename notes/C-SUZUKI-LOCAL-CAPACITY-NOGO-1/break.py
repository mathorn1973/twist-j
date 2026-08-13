# breaker_suzuki_local_capacity_nogo_1.py
# Independent adversarial path for C-SUZUKI-LOCAL-CAPACITY-NOGO-1.
# DIFFERENT code path by design: mpmath special functions (lerchphi,
# digamma, catalan, pi, gamma constant) instead of the verifier's
# psi-recurrence + S-series scaled-integer machinery. Floats/mpf allowed
# HERE (breaker, engineering grade); nothing the verifier depends on is
# asserted from this file. Exit 1 on any discrepancy or successful break.
import sys
from mpmath import (mp, mpf, exp, log, cos, cosh, sqrt, pi, catalan, euler,
                    digamma, lerchphi, polyroots)
mp.dps = 50

# --- capacity via the ORIGINAL Suzuki-form (independent of verifier form) ---
PSI14 = digamma(mpf(1)/4)
LINC = (PSI14 - log(pi))/2                    # = -alpha
CS = pi**2 + 8*catalan                        # Suzuki C = psi'(1/4)
def A(t):
    t = mpf(t)
    return (4*(exp(t/2) + exp(-t/2) - 2) + LINC*t
            + (CS - exp(-t/2)*lerchphi(exp(-2*t), 2, mpf(1)/4))/4)
def App(t):
    t = mpf(t)
    return exp(t/2) + exp(-t/2) - exp(-t/2)/(1 - exp(-2*t))

def sieve(n):
    s = [True]*(n+1); s[0] = s[1] = False
    for i in range(2, int(n**0.5)+1):
        if s[i]:
            for j in range(i*i, n+1, i): s[j] = False
    return [i for i in range(2, n+1) if s[i]]
def P(t, qmax):
    t = mpf(t); tot = mpf(0)
    for p in sieve(qmax):
        q = p; k = 1
        while q <= qmax:
            tot += log(p)/sqrt(q)*(t - k*log(p))
            q *= p; k += 1
    return tot

bad = []
def chk(name, val, ref, tol):
    ok = abs(val - ref) < tol
    print(('OK  ' if ok else 'BAD ') + name + ' ' + mp.nstr(val, 20) +
          (' vs ' + mp.nstr(ref, 20) if ref is not None else ''))
    if not ok: bad.append(name)

# cross-check against Mittermeier v5 printed constants (42),(43)
alpha = -LINC
chk('1-alpha vs M-5 (42)', 1 - alpha, mpf('-1.6860917096128327911'), mpf('1e-15'))
chk('C-4 vs M-5 (43)', CS/4 - 4, mpf('0.2993322886267776848'), mpf('1e-15'))
# alpha via the second route (log 8pi + gamma + pi/2)/2
chk('alpha two routes', alpha, (log(8*pi) + euler + pi/2)/2, mpf('1e-40'))

# gate-quantity recomputation vs verifier printed leading digits
chk('A(1/4)', A(mpf(1)/4), mpf('0.05123349628233368698'), mpf('1e-18'))
chk('A(1/2)', A(mpf(1)/2), mpf('0.040162580382'), mpf('1e-11'))
chk('App(1/4)', App(mpf(1)/4), mpf('-0.227215300124'), mpf('1e-11'))
chk('App(log2) vs 5 sqrt2/6', App(log(2)), 5*sqrt(2)/6, mpf('1e-40'))
chk('App(log3) vs 23 sqrt3/24', App(log(3)), 23*sqrt(3)/24, mpf('1e-40'))
lhs3 = (A(mpf(1)/4) - A(mpf(1)/20))*mpf(1)/4
rhs3 = (A(mpf(1)/2) - A(mpf(1)/4))*mpf(1)/5
chk('V3 lhs', lhs3, mpf('0.002382356805'), mpf('1e-10'))
chk('V3 rhs', rhs3, mpf('-0.002214183180'), mpf('1e-10'))
dP = log(2)/sqrt(2)*(mpf(4)/5 - log(2)); dA = A(mpf(4)/5) - A(log(2))
chk('V4b dP', dP, mpf('0.052371673204'), mpf('1e-11'))
chk('V4b dA', dA, mpf('0.031050793500'), mpf('1e-11'))
chk('4A(3)-A(6)', 4*A(3) - A(6), mpf('-35.85403015'), mpf('1e-7'))
chk('4P(3)-P(6)', 4*P(3, 20) - P(6, 403), mpf('-35.96474408'), mpf('1e-7'))

# plastic root independent
rts = [r.real for r in polyroots([1, 0, -1, -1]) if abs(r.imag) < mpf('1e-40')]
rho = rts[0]
chk('rho^3-rho-1', rho**3 - rho - 1, mpf(0), mpf('1e-45'))
print('INFO log rho =', mp.nstr(log(rho), 20), ' < log 2 =', mp.nstr(log(2), 20))

# BREAK ATTEMPT 1: scan for a failure of the convexity violation
# (is the V3 margin knife-edge? find the widest slope-decrease region)
worst = None
tgrid = [mpf(1)/1000*k for k in range(5, 700, 5)]
prev = None
dec_regions = 0
for i in range(1, len(tgrid) - 1):
    a, b, c = tgrid[i-1], tgrid[i], tgrid[i+1]
    s1 = (A(b) - A(a))/(b - a); s2 = (A(c) - A(b))/(c - b)
    if s2 < s1:
        dec_regions += 1
        gap = s1 - s2
        if worst is None or gap > worst[0]: worst = (gap, b)
print('INFO slope-decrease grid points:', dec_regions, 'of', len(tgrid)-2,
      ' max gap', mp.nstr(worst[0], 10), 'near t =', mp.nstr(worst[1], 10))
if dec_regions == 0: bad.append('convexity violation vanished')

# BREAK ATTEMPT 2: nonnegative-ramp least squares fit of A on [1/50, 3/5]
# model: c0 + c1 t + sum_j w_j (t - a_j)_+, w_j >= 0, c0 c1 free.
knots = [mpf(k)/50 for k in range(0, 30)]
ts = [mpf(1)/50 + mpf(29)/50*mpf(k)/120 for k in range(121)]
ys = [A(t) for t in ts]
import random
random.seed(0)
w = [mpf(0)]*len(knots); c0 = ys[0]; c1 = mpf(0)
def model(t):
    v = c0 + c1*t
    for wj, aj in zip(w, knots):
        if t > aj: v += wj*(t - aj)
    return v
lr = mpf('0.05')
for it in range(4000):
    g0 = mpf(0); g1 = mpf(0); gw = [mpf(0)]*len(knots)
    for t, y in zip(ts, ys):
        r = model(t) - y
        g0 += r; g1 += r*t
        for j, aj in enumerate(knots):
            if t > aj: gw[j] += r*(t - aj)
    n = mpf(len(ts))
    c0 -= lr*g0/n; c1 -= lr*g1/n
    for j in range(len(knots)):
        w[j] = max(mpf(0), w[j] - lr*gw[j]/n)
resid = max(abs(model(t) - y) for t, y in zip(ts, ys))
print('INFO best nonneg-ramp fit max residual on [1/50,3/5]:', mp.nstr(resid, 10))
if resid < mpf('1e-6'):
    bad.append('ramp fit succeeded (EMPTY in doubt)')

# BREAK ATTEMPT 3: positivity floor scan on [1/128, 45/64]
mn = None
for k in range(3000):
    t = mpf(1)/128 + (mpf(45)/64 - mpf(1)/128)*mpf(k)/2999
    v = A(t)
    if mn is None or v < mn[0]: mn = (v, t)
print('INFO min A on window grid:', mp.nstr(mn[0], 12), 'at t =', mp.nstr(mn[1], 8))
if mn[0] <= 0: bad.append('window positivity broken')

print('BREAKER RESULT: ' + ('0 breaks, ' if not bad else str(len(bad)) + ' hits: ')
      + ('all independent recomputations agree' if not bad else ','.join(bad)))
sys.exit(1 if bad else 0)
