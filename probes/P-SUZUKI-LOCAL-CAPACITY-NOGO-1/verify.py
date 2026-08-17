# verify_suzuki_local_capacity_nogo_1.py
# Verifier for PREREG-C-SUZUKI-LOCAL-CAPACITY-NOGO-1 (frozen prereg sha256
# 37cc1a43238a4b076578a59b70009628d61b31f9da126b7e02662cdaad1d8218).
# Python 3 standard library only. Integers and Fractions only. No float
# object anywhere. Scaled-integer outward-rounded interval arithmetic at
# scale 2^-B, B = 192. Deterministic stdout, no timestamps.
import sys
from fractions import Fraction as F
from math import isqrt  # integer-only helper from stdlib (no floats)

B = 192
ONE = 1 << B

# ---------- directed helpers ----------
def fdiv(a, b):  # floor(a/b), b > 0
    return a // b
def cdiv(a, b):  # ceil(a/b), b > 0
    return -((-a) // b)

def from_frac(fr):
    n, d = fr.numerator, fr.denominator
    return (fdiv(n << B, d), cdiv(n << B, d))

def iv_int(n):
    return (n << B, n << B)

def iv_add(x, y): return (x[0] + y[0], x[1] + y[1])
def iv_sub(x, y): return (x[0] - y[1], x[1] - y[0])
def iv_neg(x):    return (-x[1], -x[0])

def iv_mul(x, y):
    ps = (x[0]*y[0], x[0]*y[1], x[1]*y[0], x[1]*y[1])
    return (fdiv(min(ps), ONE), cdiv(max(ps), ONE))

def iv_muli(x, n):  # multiply by exact integer n
    if n >= 0: return (x[0]*n, x[1]*n)
    return (x[1]*n, x[0]*n)

def iv_divi(x, n):  # divide by exact positive integer n
    return (fdiv(x[0], n), cdiv(x[1], n))

def iv_div(x, y):  # y strictly positive interval
    assert y[0] > 0
    lo = min(fdiv(x[0] << B, y[1]), fdiv(x[0] << B, y[0]))
    hi = max(cdiv(x[1] << B, y[0]), cdiv(x[1] << B, y[1]))
    return (lo, hi)

def iv_width_lt(x, bits):
    return (x[1] - x[0]) < (ONE >> bits)

def iv_intersects(x, y):
    return x[0] <= y[1] and y[0] <= x[1]

def dec(xs, digits=30):  # exact decimal string of scaled int xs/2^B
    neg = xs < 0
    v = -xs if neg else xs
    ip = v >> B
    fr = v - (ip << B)
    ds = []
    for _ in range(digits):
        fr *= 10
        ds.append(str(fr >> B))
        fr -= (fr >> B) << B
    return ('-' if neg else '') + str(ip) + '.' + ''.join(ds)

def iv_str(x):
    return '[' + dec(x[0]) + ', ' + dec(x[1]) + ']'

# ---------- exp of a scaled point, outward ----------
def exp_pt(xs):
    ax = -xs if xs < 0 else xs
    kmin = 2 * (cdiv(ax, ONE)) + 4
    term = (ONE, ONE)
    s = (ONE, ONE)
    x = (xs, xs)
    k = 0
    while True:
        k += 1
        term = iv_divi(iv_mul(term, x), k)
        s = iv_add(s, term)
        m = max(-term[0], term[1])
        if k >= kmin and m < 4:
            s = iv_add(s, (-2*m - 2, 2*m + 2))
            break
    return s

def exp_iv(x):
    return (exp_pt(x[0])[0], exp_pt(x[1])[1])

# ---------- log of a positive Fraction, outward ----------
def atanh_frac(u):  # |u| <= 1/4 guaranteed by caller; exact Fraction series
    s = F(0); p = u; u2 = u*u; k = 0
    while True:
        s += p / (2*k + 1)
        p *= u2
        k += 1
        if abs(p) / (2*k + 1) < F(1, 1 << (B + 16)):
            break
    tail = abs(p) / ((2*k + 1) * (1 - u2))
    return (from_frac(s - tail)[0], from_frac(s + tail)[1])

_LOG_CACHE = {}
def log_frac(fr):
    key = (fr.numerator, fr.denominator)
    if key in _LOG_CACHE: return _LOG_CACHE[key]
    assert fr > 0
    m = fr; e = 0
    while m >= F(4, 3): m = m / 2; e += 1
    while m < F(2, 3):  m = m * 2; e -= 1
    u = (m - 1) / (m + 1)
    at = atanh_frac(u)
    res = iv_add(iv_muli(LOG2, e), iv_muli(at, 2))
    _LOG_CACHE[key] = res
    return res

def atan_alt(u):  # alternating series brackets, u rational in (0,1)
    s = F(0); p = u; u2 = u*u; k = 0
    lo = hi = None
    while True:
        t = p / (2*k + 1)
        s = s + t if k % 2 == 0 else s - t
        p *= u2; k += 1
        nt = p / (2*k + 1)
        if nt < F(1, 1 << (B + 16)):
            if k % 2 == 1: lo, hi = s - nt, s
            else:          lo, hi = s, s + nt
            break
    return (from_frac(lo)[0], from_frac(hi)[1])

LOG2 = iv_muli(atanh_frac(F(1, 3)), 2)
PI = iv_sub(iv_muli(atan_alt(F(1, 5)), 16), iv_muli(atan_alt(F(1, 239)), 4))
LOGPI = (log_frac(F(PI[0], ONE))[0], log_frac(F(PI[1], ONE))[1])

# ---------- digamma and trigamma at 1/4, 3/4 ----------
BERN = {2: F(1,6), 4: F(-1,30), 6: F(1,42), 8: F(-1,30), 10: F(5,66),
        12: F(-691,2730), 14: F(7,6)}
B16 = F(-3617, 510)

def psi_asym(a):  # a Fraction >= 100; DLMF 5.11(ii) first-omitted-term bound
    fr = -1/(2*a)
    for j in range(1, 8):
        fr -= BERN[2*j] / (2*j * a**(2*j))
    err = abs(B16 / (16 * a**16))
    la = log_frac(a)
    return (iv_add(la, from_frac(fr - err))[0], iv_add(la, from_frac(fr + err))[1])

def psi1_asym(a):
    fr = 1/a + 1/(2*a*a)
    for j in range(1, 8):
        fr += BERN[2*j] / a**(2*j + 1)
    err = abs(B16 / a**17)
    return (from_frac(fr - err)[0], from_frac(fr + err)[1])

def psi_at(x):   # x in {1/4, 3/4}; recurrence N = 100
    N = 100
    s = sum(1/(x + k) for k in range(N))
    return iv_sub(psi_asym(x + N), from_frac(s))

def psi1_at(x):
    N = 100
    s = sum(1/(x + k)**2 for k in range(N))
    return iv_add(psi1_asym(x + N), from_frac(s))

PSI14 = psi_at(F(1, 4)); PSI34 = psi_at(F(3, 4))
PSI1_14 = psi1_at(F(1, 4)); PSI1_34 = psi1_at(F(3, 4))
ALPHA = iv_divi(iv_sub(LOGPI, PSI14), 2)
CCONST = iv_divi(PSI1_14, 4)

# ---------- S(z), capacity A, curvature A'' ----------
def S_pt(zs):  # scaled point z in (0,1), outward interval of sum z^k/(4k+1)^2
    z = (zs, zs)
    p = (ONE, ONE)
    s = iv_int(0)
    k = 0
    while True:
        term = iv_divi(p, (4*k + 1)**2)
        s = iv_add(s, term)
        p = iv_mul(p, z); k += 1
        if p[1] < (ONE >> 170):
            break
    # tail bound: sum_{j>=k} z^j/(4j+1)^2 <= p_hi/( (4k+1)^2 (1-z) )
    denom = (ONE - zs, ONE - zs)
    tail = iv_div(iv_divi((0, p[1]), (4*k + 1)**2), denom)
    return iv_add(s, (0, tail[1]))

def S_iv(z):
    return (S_pt(z[0])[0], S_pt(z[1])[1])

def A_iv(t):
    half = iv_divi(t, 2)
    eA = exp_iv(half)
    eB = exp_iv(iv_neg(half))
    pole = iv_sub(iv_muli(iv_add(eA, eB), 4), iv_int(8))
    lin = iv_neg(iv_mul(ALPHA, t))
    z = exp_iv(iv_neg(iv_muli(t, 2)))
    sterm = iv_neg(iv_muli(iv_mul(eB, S_iv(z)), 4))
    return iv_add(iv_add(iv_add(pole, lin), CCONST), sterm)

def A_pt(fr):
    return A_iv(from_frac(fr))

def App_iv(t):  # t.lo > 0 required
    half = iv_divi(t, 2)
    eA = exp_iv(half)
    eB = exp_iv(iv_neg(half))
    den = iv_sub(iv_int(1), exp_iv(iv_neg(iv_muli(t, 2))))
    assert den[0] > 0
    return iv_sub(iv_add(eA, eB), iv_div(eB, den))

# ---------- prime machinery ----------
def sieve(n):
    s = bytearray([1]) * 0
    s = bytearray([1]) * (n + 1)
    s[0:2] = b'\x00\x00'
    for i in range(2, isqrt(n) + 1):
        if s[i]:
            s[i*i::i] = bytearray(len(s[i*i::i]))
    return s

def primes_upto(n):
    s = sieve(n)
    return [i for i in range(2, n + 1) if s[i]]

def sqrt_int_iv(n):  # interval for sqrt(n)
    r = isqrt(n << (2 * B))
    return (r, r + 1)

def P_pt(tval, qmax):  # t exact integer value (3 or 6), events q <= qmax
    total = iv_int(0)
    for p in primes_upto(qmax):
        lp = log_frac(F(p))
        q = p; k = 1
        while q <= qmax:
            wt = iv_div(lp, sqrt_int_iv(q))
            ramp = iv_sub(iv_int(tval), iv_muli(lp, k))
            total = iv_add(total, iv_mul(wt, ramp))
            q *= p; k += 1
    return total

# ---------- gates ----------
fails = []
NGATES = [0]
def gate(name, ok, detail):
    NGATES[0] += 1
    print(('PASS ' if ok else 'FAIL ') + name + '  ' + detail)
    if not ok: fails.append(name)

# consistency gates for the constant machinery
d_psi = iv_sub(PSI34, PSI14)
gate('X1 psi(3/4)-psi(1/4) encloses pi',
     iv_intersects(d_psi, PI) and iv_width_lt(d_psi, 100) and iv_width_lt(PI, 100),
     'delta=' + iv_str(d_psi)[:46] + '...')
s_psi1 = iv_add(PSI1_14, PSI1_34)
two_pi2 = iv_muli(iv_mul(PI, PI), 2)
gate('X2 psi\'(1/4)+psi\'(3/4) encloses 2 pi^2',
     iv_intersects(s_psi1, two_pi2) and iv_width_lt(s_psi1, 100),
     'sum=' + iv_str(s_psi1)[:46] + '...')

# V1 surrogate prime-curve identities, exact Fractions
TAU = [F(1), F(3,2), F(2), F(7,3)]
OM  = [F(2), F(1,2), F(1), F(3,4)]
TIMES = [F(1,2), F(1), F(5,4), F(3,2), F(2), F(9,4), F(3)]
def ov(t, u, tau):
    m = min(t, u) - tau
    return m if m > 0 else F(0)
def Fsur(s):
    return sum(w*w*max(F(0), s - tau) for w, tau in zip(OM, TAU))
ok1 = True
for t in TIMES:
    ip = sum(w*w*ov(t, t, tau) for w, tau in zip(OM, TAU))
    if ip != Fsur(t): ok1 = False
for t in TIMES:
    for u in TIMES:
        ip = sum(w*w*ov(t, u, tau) for w, tau in zip(OM, TAU))
        if ip != Fsur(min(t, u)): ok1 = False
for u in TIMES:
    for t in TIMES:
        if u <= t:
            ip = sum(w*w*(ov(t, u, tau) - ov(u, u, tau)) for w, tau in zip(OM, TAU))
            if ip != 0: ok1 = False
            d = sum(w*w*(ov(t, t, tau) - 2*ov(t, u, tau) + ov(u, u, tau)) for w, tau in zip(OM, TAU))
            if d != Fsur(t) - Fsur(u): ok1 = False
# negative control: in the difference vector move component 2 start to 5/4
u0, t0 = F(3,2), F(2)
ipn = F(0)
for i, (w, tau) in enumerate(zip(OM, TAU)):
    taud = F(5,4) if i == 1 else tau
    ipn += w*w*(ov(t0, u0, taud) - ov(u0, u0, tau))
gate('V1 surrogate identities (i)-(iv) + negative control',
     ok1 and ipn != 0, 'negctrl=' + str(ipn))

# V2a geometric-series consistency of the Lerch derivative block
def v2a(fr):
    t = from_frac(fr)
    r = exp_iv(iv_neg(iv_muli(t, 2)))
    term = exp_iv(iv_neg(iv_divi(t, 2)))
    s = iv_int(0); k = 0
    while term[1] >= 4:
        s = iv_add(s, term)
        term = iv_mul(term, r); k += 1
        if k > 20000: return False
    den = iv_sub(iv_int(1), r)
    tail = iv_div((0, term[1]), den)
    lhs = iv_add(s, (0, tail[1]))
    rhs = iv_div(exp_iv(iv_neg(iv_divi(t, 2))), den)
    return iv_intersects(lhs, rhs) and iv_width_lt(lhs, 100) and iv_width_lt(rhs, 100)
gate('V2a geometric identity at t=1/4,1/2,1',
     v2a(F(1,4)) and v2a(F(1,2)) and v2a(F(1)), 'widths<2^-100, intervals intersect')

# V2r algebraic cross-check of A'' at log 2, log 3 (Mittermeier eq. 12)
a2l2 = App_iv(LOG2)
ref2 = iv_divi(iv_muli(sqrt_int_iv(2), 5), 6)
a2l3 = App_iv(log_frac(F(3)))
ref3 = iv_divi(iv_muli(sqrt_int_iv(3), 23), 24)
gate('V2r A\'\'(log q) matches sqrt(q)-1/(sqrt(q)(q^2-1)), q=2,3',
     iv_intersects(a2l2, ref2) and iv_intersects(a2l3, ref3),
     'A\'\'(log2)=' + dec(a2l2[0], 12) + '..')

# V2b plastic bracket and curvature signs
h_l = F(13,10)**3 - F(13,10) - 1
h_r = F(4,3)**3 - F(4,3) - 1
hp_l = 3*F(13,10)**2 - 1
app14 = App_iv(from_frac(F(1,4)))
app_log2 = a2l2
gate('V2b h(13/10)<0<h(4/3), h\'>0, A\'\'(1/4)<0, A\'\'(log2)>0',
     h_l == F(-103,1000) and h_l < 0 and h_r == F(1,27) and h_r > 0
     and hp_l > 0 and app14[1] < 0 and app_log2[0] > 0,
     'A\'\'(1/4) hi=' + dec(app14[1], 12))

# capacity values used by several gates
A_120 = A_pt(F(1,20)); A_14 = A_pt(F(1,4)); A_12 = A_pt(F(1,2))
A_45 = A_pt(F(4,5));   A_3 = A_pt(F(3));    A_6 = A_pt(F(6))
A_L2 = A_iv(LOG2)

# V3 convexity violation on (1/20, 1/4, 1/2)
lhs3 = iv_mul(iv_sub(A_14, A_120), from_frac(F(1,4)))
rhs3 = iv_mul(iv_sub(A_12, A_14), from_frac(F(1,5)))
gate('V3 convexity violation (ramp class EMPTY)', lhs3[0] > rhs3[1],
     'lhs>=' + dec(lhs3[0], 12) + ' rhs<=' + dec(rhs3[1], 12))

# V4a dA not nonnegative
gate('V4a A(1/4) > A(1/2)', A_14[0] > A_12[1],
     'A(1/4)>=' + dec(A_14[0], 12) + ' A(1/2)<=' + dec(A_12[1], 12))

# V4b increment domination fails at q = 2
dl = iv_sub(from_frac(F(4,5)), LOG2)
lhs4 = iv_div(iv_mul(LOG2, dl), sqrt_int_iv(2))
rhs4 = iv_sub(A_45, A_L2)
gate('V4b (log2/sqrt2)(4/5-log2) > A(4/5)-A(log2)', lhs4[0] > rhs4[1],
     'dP>=' + dec(lhs4[0], 12) + ' dA<=' + dec(rhs4[1], 12))

# V5 screw kernels indefinite at (3,6); event boundary guards
e3 = exp_pt(3 * ONE); e6 = exp_pt(6 * ONE)
g_ok = (e3[0] > 20 * ONE and e3[1] < 23 * ONE and
        e6[0] > 401 * ONE and e6[1] < 409 * ONE)
P_3 = P_pt(3, 20); P_6 = P_pt(6, 403)
dA5 = iv_sub(iv_muli(A_3, 4), A_6)
dP5 = iv_sub(iv_muli(P_3, 4), P_6)
gate('V5 4A(3)-A(6)<0, 4P(3)-P(6)<0, A(6)>0, P(6)>0, guards',
     g_ok and dA5[1] < 0 and dP5[1] < 0 and A_6[0] > 0 and P_6[0] > 0,
     '4A3-A6<=' + dec(dA5[1], 8) + ' 4P3-P6<=' + dec(dP5[1], 8))

# V6 adaptive positivity of A on [1/128, 45/64]
UNDEC = []
leaves = 0
stack = [(F(1,128), F(45,64), 0)]
while stack:
    a, b, d = stack.pop()
    tiv = (from_frac(a)[0], from_frac(b)[1])
    Av = A_iv(tiv)
    if Av[0] > 0:
        leaves += 1
        continue
    if d >= 24:
        UNDEC.append((a, b)); continue
    m = (a + b) / 2
    stack.append((a, m, d + 1)); stack.append((m, b, d + 1))
gate('V6 A>0 on [1/128,45/64] adaptive cover', len(UNDEC) == 0,
     'leaves=' + str(leaves) + ' undecided=' + str(len(UNDEC)))

# V7 event-count consistency at X = 10^6
X = 10**6
sv = sieve(X)
pi_pref = [0] * (X + 1)
c = 0
for i in range(X + 1):
    if sv[i]: c += 1
    pi_pref[i] = c
direct = pi_pref[X]
for p in primes_upto(1000):
    q = p * p
    while q <= X:
        direct += 1; q *= p
def iroot(n, k):
    if k == 1: return n
    lo, hi = 1, 2
    while hi**k <= n: hi *= 2
    while lo < hi - 1:
        mid = (lo + hi) // 2
        if mid**k <= n: lo = mid
        else: hi = mid
    return lo
formula = 0; k = 1
while True:
    r = iroot(X, k)
    if r < 2: break
    formula += pi_pref[r]; k += 1
gate('V7 event count two ways at 10^6', direct == formula,
     'N=' + str(direct))

print('CAPACITY WITNESS A(1/4)=' + dec(A_14[0], 20) + '..')
print('GATES PASSED ' + str(NGATES[0] - len(fails)) + '/' + str(NGATES[0]) +
      ('' if not fails else '  FAILED: ' + ','.join(fails)))
sys.exit(0 if not fails else 1)
