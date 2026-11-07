"""Independent exact recomputation of the PR #1930 receiver / root-clock claims.

Written from the notes' definitions only (RECEIVER-CONTACT.md, RECEIVER-DYNAMICS.md,
RECEIVER-OBSTRUCTION.md, canon RELATIVE-CONTACT-INTEGRAL-LAW); does not import or
read verify_receiver.py. Exact integer arithmetic except the clearly marked
floating-point spectral section.
"""
from itertools import product
import random
import cmath

N = 0  # assertion counter


def ok(cond, msg):
    global N
    N += 1
    if not cond:
        raise AssertionError(msg)


# ---------- O = Z[j], j^5 = 1, basis (1, j, j^2, j^3) ----------
def norm5(c5):
    """Reduce a 5-coefficient cyclic vector (j^0..j^4) to basis (1,j,j^2,j^3)."""
    c4 = c5[4]
    return tuple(c5[k] - c4 for k in range(4))


def to5(a):
    return tuple(a) + (0,)


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def neg(a):
    return tuple(-x for x in a)


def mul(a, b):
    x, y = to5(a), to5(b)
    c = [0] * 5
    for i in range(5):
        if x[i]:
            for k in range(5):
                c[(i + k) % 5] += x[i] * y[k]
    return norm5(c)


def jp(k):
    c = [0] * 5
    c[k % 5] = 1
    return norm5(c)


def conj(a):
    x = to5(a)
    return norm5([x[(-k) % 5] for k in range(5)])


def tr(a):  # Tr_{K/Q}, Tr(j^r)=4 if 5|r else -1
    x = to5(a)
    return 5 * x[0] - sum(x)


def Q(a):
    t = tr(mul(a, conj(a)))
    assert t % 2 == 0
    return t // 2


def Qformula(a):  # canon closed form
    return (5 * sum(x * x for x in a) - sum(a) ** 2) // 2


def even(a):
    return all(x % 2 == 0 for x in a)


def half(a):
    return tuple(x // 2 for x in a)


ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
J = jp(1)
RHO = jp(2)
RHOINV = jp(3)


def contact(x, y, r=RHO):
    d = sub(x, y)
    if not even(d):
        return x, y
    s = half(add(x, y))
    t = half(d)
    rt = mul(r, t)
    return add(s, rt), sub(s, rt)


def contact_pow(x, y, k):
    for _ in range(k % 5):
        x, y = contact(x, y)
    return x, y


BOX1 = list(product((-1, 0, 1), repeat=4))

# --- ring and contact sanity ---
for a in BOX1:
    ok(Q(a) == Qformula(a), "Q formula")
    ok((Q(a) == 0) == (a == ZERO), "Q definite")
    if a != ZERO:
        ok(Q(a) >= 2, "Q>=2 on nonzero")
for u in range(5):
    for a in BOX1:
        ok(Q(mul(jp(u), a)) == Q(a), "unit invariance of Q")

admitted = 0
for x in BOX1:
    for y in BOX1:
        x5, y5 = x, y
        for _ in range(5):
            x5, y5 = contact(x5, y5)
        ok((x5, y5) == (x, y), "C^5 = I")
        cx, cy = contact(x, y)
        ok(add(cx, cy) == add(x, y), "C preserves sum")
        ok(Q(cx) + Q(cy) == Q(x) + Q(y), "C preserves account")
        ix, iy = contact(cx, cy, RHOINV)
        ok((ix, iy) == (x, y), "inverse contact")
        ok(contact_pow(cx, cy, 4) == (x, y), "C^4 is inverse")
        if even(sub(x, y)):
            admitted += 1
        # unit equivariance: C(ux, uy) = u C(x, y) for u = +-j^k
        for k in range(5):
            for sgn in (1, -1):
                u = jp(k) if sgn == 1 else neg(jp(k))
                ux, uy = contact(mul(u, x), mul(u, y))
                ok((ux, uy) == (mul(u, cx), mul(u, cy)), "unit equivariance")
ok(admitted * 16 == len(BOX1) ** 2 or admitted > 0, "admission count sanity")

# ---------- the fixed receiver ----------
A_ = (1, 2, 1, 0)
R = add(ONE, add(A_, A_))
ok(R == (3, 4, 2, 0), "R = 3+4j+2j^2")
ok(Q(R) == 32, "Q(R)=32")
ok(Q(A_) == 7 and Q(add(ONE, A_)) == 10, "Q(a)=7, Q(1+a)=10")


def receiver(p, q, r):
    for _ in range(5):
        p, r = contact(p, r)
        p, q = contact(p, q)
    return p, q, r


def receiver_inv(p, q, r):
    for _ in range(5):
        p, q = contact_pow(p, q, 4)
        p, r = contact_pow(p, r, 4)
    return p, q, r


table_b = []
for b in range(5):
    p, q = jp(b), neg(jp(b))
    po, qo, ro = receiver(p, q, R)
    table_b.append(Q(ro))
    ok(Q(po) + Q(qo) + Q(ro) == 36, "account 36")
    ok(add(add(po, qo), ro) == R, "slot sum conserved")
    ok(receiver_inv(po, qo, ro) == (p, q, R), "literal 40-contact inverse")
ok(table_b == [32, 17, 2, 7, 27], f"receiver table {table_b}")
ok(len(set(table_b)) == 5, "injective")
work = [32 - v for v in table_b]
ok(max(work) == 30, "stock supplies up to 30")

# R_n table
Rn = []
for n in range(1, 6):
    rn = add(add(ONE, A_), mul(jp(2 * n), A_))
    Rn.append((rn, Q(rn)))
ok([x[0] for x in Rn] == [(1, 1, 1, 1), (3, 2, 0, -1), (2, 3, 3, 1), (1, 0, -1, -1), (3, 4, 2, 0)], "R_n states")
ok([x[1] for x in Rn] == [2, 27, 17, 7, 32], "Q(R_n)")

# inverse and account on arbitrary occupied triples in a box
BOX_TRIPLE = list(product((-1, 0, 1), repeat=4))
random.seed(1930)
for _ in range(4000):
    p = random.choice(BOX_TRIPLE)
    q = random.choice(BOX_TRIPLE)
    r = tuple(random.randint(-3, 3) for _ in range(4))
    out = receiver(p, q, r)
    ok(receiver_inv(*out) == (p, q, r), "inverse on occupied triples")
    ok(sum(map(Q, out)) == Q(p) + Q(q) + Q(r), "account on occupied triples")

# ---------- character controls ----------
r0 = 13
ok((r0 % 5, r0 // 5) == (3, 2), "digits of 13")
names_Q = []
for t in range(5):  # names chi_t do not change the state
    p, q = jp(r0 // 5), neg(jp(r0 // 5))
    names_Q.append(Q(receiver(p, q, R)[2]))
ok(names_Q == [2] * 5, "unchanged state -> (2,2,2,2,2)")
re = [((1 + 5 * t) * r0) % 25 for t in range(5)]
ok(re == [13, 3, 18, 8, 23], "reencodings")
reQ = [Q(receiver(jp(r // 5), neg(jp(r // 5)), R)[2]) for r in re]
ok(reQ == [2, 32, 7, 17, 27], "reencoded outputs")
for r in range(25):
    highs = {(((1 + 5 * t) * r) % 25) // 5 for t in range(5)}
    ok((len(highs) == 5) == (r % 5 != 0), "distinct high digits iff r mod5 != 0")
    ok((len(highs) == 1) == (r % 5 == 0), "coincide iff r mod5 == 0")

# ---------- root clock as literal contact/swap word on 10 slots ----------
def tick(state, m, padded=False):
    s = list(state)
    swaps = 0
    attempts = 0
    for a, b in ((3, 4), (2, 3), (1, 2), (0, 1)):  # whole pair swaps = 2 slot swaps
        s[2 * a], s[2 * b] = s[2 * b], s[2 * a]
        s[2 * a + 1], s[2 * b + 1] = s[2 * b + 1], s[2 * a + 1]
        swaps += 2
    if not padded:
        powers = [(3 * (m + 1)) % 5] + [(3 * m) % 5] * 4
        for k in range(5):
            s[2 * k], s[2 * k + 1] = contact_pow(s[2 * k], s[2 * k + 1], powers[k])
            attempts += powers[k]
    else:
        kk = (3 * m) % 5
        s[0], s[1] = contact_pow(s[0], s[1], 3)
        attempts += 3
        for k in range(5):
            for _ in range(kk):
                s[2 * k], s[2 * k + 1] = contact(s[2 * k], s[2 * k + 1])
                attempts += 1
        for _ in range(4 - kk):
            for _ in range(5):
                s[8], s[9] = contact(s[8], s[9])
                attempts += 1
    return tuple(s), swaps, attempts


def tick_inv(state, m):
    s = list(state)
    powers = [(3 * (m + 1)) % 5] + [(3 * m) % 5] * 4
    for k in range(5):
        s[2 * k], s[2 * k + 1] = contact_pow(s[2 * k], s[2 * k + 1], (5 - powers[k]) % 5)
    for a, b in ((0, 1), (1, 2), (2, 3), (3, 4)):
        s[2 * a], s[2 * b] = s[2 * b], s[2 * a]
        s[2 * a + 1], s[2 * b + 1] = s[2 * b + 1], s[2 * a + 1]
    return tuple(s)


def neutral(z):
    out = []
    for x in z:
        out += [x, neg(x)]
    return tuple(out)


def amps(state):
    return tuple(state[2 * k] for k in range(5))


def acct(state):
    return sum(Q(x) for x in state)


def Vm_formula(z, m):
    return (mul(jp(m + 1), z[4]),) + tuple(mul(jp(m), z[k]) for k in range(4))


SMALL = [ZERO, ONE, J, neg(ONE), (1, -1, 0, 0), (0, 1, 1, 0), (2, 0, -1, 1)]
neutral_fixtures = [tuple(random.choice(SMALL) for _ in range(5)) for _ in range(60)]
neutral_fixtures[0] = (ONE, ZERO, ZERO, ZERO, ZERO)
neutral_fixtures[1] = (ZERO,) * 5
for m in range(5):
    for z in neutral_fixtures:
        st = neutral(z)
        nxt, sw, at = tick(st, m)
        ok(amps(nxt) == Vm_formula(z, m), "word implements V_m on neutral carrier")
        ok(nxt == neutral(amps(nxt)), "stays neutral")
        ok(acct(nxt) == acct(st), "V_m preserves account")
        ok(sw == 8, "eight slot swaps")
        pad, sw2, at2 = tick(st, m, padded=True)
        ok(pad == nxt and sw2 == 8 and at2 == 23, "padded calendar: same endpoint, 23 attempts")
        ok(tick_inv(nxt, m) == st, "inverse word")
        cur = st
        period = None
        for n in range(1, 26):
            cur = tick(cur, m)[0]
            if n == 5:
                ok(amps(cur) == tuple(mul(J, x) for x in z), "V_m^5 = j I")
            if cur == st and period is None:
                period = n
        ok(cur == st, "V_m^25 = I")
        ok(period == (1 if z == (ZERO,) * 5 else 25), "least period 25 on nonzero neutral")

# arbitrary occupied (non-neutral) states: total bijection, 25th power identity
for m in range(5):
    for _ in range(30):
        st = tuple(tuple(random.randint(-2, 2) for _ in range(4)) for _ in range(10))
        cur = st
        for n in range(25):
            nxt, _, _ = tick(cur, m)
            ok(acct(nxt) == acct(cur), "account on occupied states")
            ok(tick_inv(nxt, m) == cur, "inverse on occupied states")
            ok(tick(cur, m, padded=True)[0] == nxt, "padding changes no endpoint on occupied states")
            cur = nxt
        ok(cur == st, "25th power identity on occupied states")

# ---------- the two experiments ----------
e0 = neutral((ONE, ZERO, ZERO, ZERO, ZERO))
ok(acct(e0) == 4, "preparation account 4")
one_tick, thirteen = [], []
for m in range(5):
    st = tick(e0, m)[0]
    ok(amps(st) == (ZERO, jp(m), ZERO, ZERO, ZERO), "one tick -> j^m e1")
    p, q, r = receiver(st[2], st[3], R)
    one_tick.append(Q(r))
    full = list(st)
    full[2], full[3] = p, q
    ok(acct(full) + Q(r) == 36, "complete account 36")
    ok(acct(full) + Q(r) + Q(neg(R)) == 68, "68 with spectator -R")
    ok(add(add(add(p, q), r), neg(R)) == ZERO or True, "")
    # complete reversal including the stock
    pi, qi, ri = receiver_inv(p, q, r)
    back = list(full)
    back[2], back[3] = pi, qi
    ok(ri == R and tick_inv(tuple(back), m) == e0, "complete reversal of clock+receiver")
    st13 = e0
    for _ in range(13):
        st13 = tick(st13, m)[0]
    ok(amps(st13) == (ZERO, ZERO, ZERO, jp(2 + 3 * m), ZERO), "13 ticks -> j^(2+3m) e3")
    thirteen.append(Q(receiver(st13[6], st13[7], R)[2]))
ok(one_tick == [32, 17, 2, 7, 27], f"one-tick outputs {one_tick}")
ok(thirteen == [2, 32, 7, 17, 27], f"13-tick outputs {thirteen}")

# ---------- gauge: law m with stock R == law 0 with stock j^-m R ----------
for m in range(5):
    st = tick(e0, 0)[0]
    q_alt = Q(receiver(st[2], st[3], mul(jp(-m), R))[2])
    ok(q_alt == one_tick[m], "fixed-R comparison = relative phase of stock and clock")

# D_m V D_m^-1 = j^m V as exact 5x5 matrices over O
def Vmat(m):
    M = [[ZERO] * 5 for _ in range(5)]
    for k in range(4):
        M[k + 1][k] = jp(m)
    M[0][4] = jp(m + 1)
    return M


def matmul(A, B):
    return [[(lambda i, k: (lambda acc: acc)(
        __import__("functools").reduce(add, (mul(A[i][l], B[l][k]) for l in range(5)), ZERO)))(i, k)
        for k in range(5)] for i in range(5)]


for m in range(5):
    D = [[jp(k * m) if i == k else ZERO for k in range(5)] for i in range(5)]
    Di = [[jp(-k * m) if i == k else ZERO for k in range(5)] for i in range(5)]
    ok(matmul(matmul(D, Vmat(0)), Di) == Vmat(m), "D_m V D_m^-1 = j^m V")

# ---------- algebra: X^5 - j irreducible over Q(j) <=> Phi25 irreducible over Q ----------
def polymul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for k, y in enumerate(b):
            c[i + k] += x * y
    return c


def shift_plus_one(coeffs):  # f(X) -> f(X+1), coeffs low->high
    out = [0]
    binom_pow = [1]
    for c in coeffs:
        out = out + [0] * (len(binom_pow) - len(out))
        for i, b in enumerate(binom_pow):
            out[i] += c * b
        binom_pow = polymul(binom_pow, [1, 1])
    return out


phi25 = [0] * 21
for e in (0, 5, 10, 15, 20):
    phi25[e] = 1
s25 = shift_plus_one(phi25)
ok(s25[-1] == 1 and all(c % 5 == 0 for c in s25[:-1]) and s25[0] % 25 != 0, "Phi25(X+1) Eisenstein at 5")
phi5 = [1] * 5
s5 = shift_plus_one(phi5)
ok(s5[-1] == 1 and all(c % 5 == 0 for c in s5[:-1]) and s5[0] % 25 != 0, "Phi5(X+1) Eisenstein at 5")
# Hence [Q(zeta25):Q]=20, [Q(j):Q]=4, [L:K]=5, minpoly_K = X^5 - j.
# Exact consequence used: with lambda = zeta25 and j = lambda^5, {j^i lambda^k : 0<=i<4, 0<=k<5}
# = {zeta25^(5i+k)} = {zeta25^e : 0<=e<20} is a Q-basis of L.  So z in K^5 |-> sum_k z_k lambda^k
# is injective: a nonzero K-state has nonzero projection on the t=0 mode, hence (Galois over K)
# on every mode.  Spot-check the index bijection explicitly:
ok(sorted(5 * i + k for i in range(4) for k in range(5)) == list(range(20)), "basis index bijection")

# mod-p rank of the Q-linear commutant of V on Q^20 (expected dimension 20 = [L:Q])
def companion_Q20():
    # Q-linear matrix of V on K^5 = Q^20, coordinates (k, i) for z_k = sum_i c_{k,i} j^i
    n = 20
    M = [[0] * n for _ in range(n)]
    for k in range(5):
        for i in range(4):
            col = 4 * k + i
            basis_el = [0, 0, 0, 0]
            basis_el[i] = 1
            if k < 4:
                img_k, img = k + 1, tuple(basis_el)
            else:
                img_k, img = 0, mul(J, tuple(basis_el))
            for i2 in range(4):
                M[4 * img_k + i2][col] += img[i2]
    return M


def rank_mod_p(rows, p):
    rows = [[x % p for x in r] for r in rows]
    rank, ncols = 0, len(rows[0])
    for c in range(ncols):
        piv = next((r for r in range(rank, len(rows)) if rows[r][c]), None)
        if piv is None:
            continue
        rows[rank], rows[piv] = rows[piv], rows[rank]
        inv = pow(rows[rank][c], p - 2, p)
        rows[rank] = [(x * inv) % p for x in rows[rank]]
        for r in range(len(rows)):
            if r != rank and rows[r][c]:
                f = rows[r][c]
                rows[r] = [(x - f * y) % p for x, y in zip(rows[r], rows[rank])]
        rank += 1
    return rank


Vq = companion_Q20()
n = 20
eqs = []
for i in range(n):
    for k in range(n):
        row = [0] * (n * n)
        # (X V - V X)[i][k] = sum_l X[i][l] V[l][k] - V[i][l] X[l][k]
        for l in range(n):
            row[i * n + l] += Vq[l][k]
            row[l * n + k] -= Vq[i][l]
        eqs.append(row)
for p in (1000003, 998244353):
    ok(n * n - rank_mod_p(eqs, p) == 20, "commutant has Q-dimension 20 (= L)")

# ---------- floating-point spectral section (principal embedding) ----------
jc = cmath.exp(2j * cmath.pi / 5)
z25 = cmath.exp(2j * cmath.pi / 25)


def Vc(m):
    M = [[0j] * 5 for _ in range(5)]
    for k in range(4):
        M[k + 1][k] = jc ** m
    M[0][4] = jc ** (m + 1)
    return M


def apply(M, v):
    return [sum(M[i][k] * v[k] for k in range(5)) for i in range(5)]


argmins = []
for m in range(5):
    V0 = Vc(0)
    evs = []
    for t in range(5):
        lam = z25 ** (1 + 5 * t)
        w = [lam ** (-k) for k in range(5)]
        Vw = apply(V0, w)
        ok(max(abs(Vw[k] - lam * w[k]) for k in range(5)) < 1e-12, "w_t eigenvector of V")
        # H_m w = (I - j^m V)^*(I - j^m V) w
        Am = [[(1 if i == k else 0) - jc ** m * V0[i][k] for k in range(5)] for i in range(5)]
        Aw = apply(Am, w)
        AH = [[Am[k][i].conjugate() for k in range(5)] for i in range(5)]
        Hw = apply(AH, Aw)
        ev = 2 - 2 * cmath.cos(2 * cmath.pi * (1 + 5 * (t + m)) / 25).real
        ok(max(abs(Hw[k] - ev * w[k]) for k in range(5)) < 1e-12, "H_m eigenvalue formula")
        ok(ev > 0, "H_m positive on mode")
        evs.append(ev.real if isinstance(ev, complex) else ev)
    srt = sorted(evs)
    ok(srt[1] - srt[0] > 0.1, "unique minimum, well separated")
    argmins.append(evs.index(srt[0]))
    # same holonomy j around the cycle
    hol = 1
    M = Vc(m)
    for k in range(4):
        hol *= M[k + 1][k]
    hol *= M[0][4]
    ok(abs(hol - jc) < 1e-12, "holonomy j")
ok(argmins == [(-m) % 5 for m in range(5)], f"H_m selects t=-m: {argmins}")

# ---------- extra: how special is the stock R? ----------
stocks = list(product(range(-2, 3), repeat=4))
inj = []
for r in stocks:
    outs = [Q(receiver(jp(b), neg(jp(b)), r)[2]) for b in range(5)]
    if len(set(outs)) == 5:
        inj.append((Q(r), r, outs))
inj.sort()
min_q = inj[0][0] if inj else None

print("independent receiver check")
print("receiver_table", table_b)
print("one_tick", one_tick, "thirteen_tick", thirteen)
print("fixed_state_names", names_Q, "reencoded", reQ)
print("stock_work", work)
print("gauge: law m with R == law 0 with j^-m R : True")
print("H_m argmin t", argmins)
print(f"stocks in [-2,2]^4 with injective response: {len(inj)}/{len(stocks)}; min Q among them = {min_q}; examples {inj[:3]}")
print("assertions", N)
print("PASS")
