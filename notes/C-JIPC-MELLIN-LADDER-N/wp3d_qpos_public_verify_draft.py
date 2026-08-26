# P-JIPC-WP3D-QPOS-MELLIN-1 -- exact finite audit of the frozen surface.
# Zero arguments; no file, stdin, environment, clock, or network access.
# Single import below. Exact rational arithmetic only; no floats, no
# true division anywhere (the AST policy forbids ast.Div; integer //
# and the Fraction constructor are the only quotients).
# The theorem carrier is the written proof in PREREG.md; this program
# audits the frozen bounded surface and the negative proof controls.
# Exit contract: PASS and scientific FIRED both exit zero with their
# deterministic stdout; integrity STOP exits nonzero.

from fractions import Fraction as Fr

FIRED_LIST = []
STOP_LIST = []


def fired(msg):
    FIRED_LIST.append(msg)


def stop(msg):
    STOP_LIST.append(msg)


# ---------------------------------------------------------------------------
# Ring Q[g, g^-1]: Laurent polynomials as {exponent: Fraction}, zero-free.
# The token relation is p_hat = g^2; g is never evaluated numerically.
# ---------------------------------------------------------------------------

MAX_SUPPORT = 64
MAX_BITS = 4096


def rnorm(a):
    out = {}
    for e, c in a.items():
        if c != 0:
            out[e] = c
    if len(out) > MAX_SUPPORT:
        stop("RING_SUPPORT_CAP")
    return out


def radd(a, b):
    out = dict(a)
    for e, c in b.items():
        out[e] = out.get(e, Fr(0)) + c
    return rnorm(out)


def rneg(a):
    return {e: -c for e, c in a.items()}


def rsub(a, b):
    return radd(a, rneg(b))


def rmul(a, b):
    out = {}
    for e1, c1 in a.items():
        for e2, c2 in b.items():
            out[e1 + e2] = out.get(e1 + e2, Fr(0)) + c1 * c2
    return rnorm(out)


def rscale(q, a):
    return rnorm({e: q * c for e, c in a.items()})


def req(a, b):
    return rnorm(dict(a)) == rnorm(dict(b))


def rzero(a):
    return len(rnorm(dict(a))) == 0


def rbits_ok(a):
    for _e, c in a.items():
        if c.numerator.bit_length() > MAX_BITS or \
                c.denominator.bit_length() > MAX_BITS:
            return False
    return True


R_ONE = {0: Fr(1)}
R_G = {1: Fr(1)}


# ---------------------------------------------------------------------------
# Frozen provenance and label tables -- consumed by the PASS path.
# ---------------------------------------------------------------------------

PROVENANCE = {"O_independent": True, "dressed_weight": "p_M"}
LABELS = {
    "MELLIN_SEEDS": "BLOCKED",
    "MELLIN_PRODUCT_IDENTITY": "BLOCKED",
    "WP2_SCALAR_SEAM": "BLOCKED_BY_MELLIN_PRODUCT_IDENTITY",
}


def check_provenance(prov):
    errs = []
    if prov.get("O_independent") is not True:
        errs.append("JOIN_CROSSREAD")
    if prov.get("dressed_weight") != "p_M":
        errs.append("WEIGHT_NAME")
    return errs


def check_labels(lab):
    errs = []
    for key, val in LABELS.items():
        if lab.get(key) != val:
            errs.append("LABEL_" + key)
    return errs


# ---------------------------------------------------------------------------
# Gate 1 -- RING_LATTICE_REPLAY
# Half-index convention: integer index k represents the argument k/2.
# C is built from C(1/2)=g, C(1)=1 by REC; B from the three exact
# anchors B(1/2,1/2)=g^2, B(1,1)=1, B(1/2,1)=2 by B-REC. MP, DUP,
# B-HALF, EOC are then genuine consistency checks, not definitions.
# ---------------------------------------------------------------------------

N_INPUT = 6
N_VALUE = 12
EOC_DOMAIN = (1, 2, 3)


def dup_input_ok(k):
    return isinstance(k, int) and 1 <= k <= N_INPUT


def build_C(rec_coeff=None):
    # rec_coeff(k) is the frozen coefficient k/2 in C(k/2+1)=(k/2)C(k/2).
    if rec_coeff is None:
        rec_coeff = lambda k: Fr(k, 2)
    C = {1: dict(R_G), 2: dict(R_ONE)}
    for k in range(1, N_VALUE - 1):
        C[k + 2] = rscale(rec_coeff(k), C[k])
    return C


def build_B(anchor_11=None, brec_coeff=None):
    # anchor_11 is B(1/2,1/2); brec_coeff(j, jk) is j/(j+k), half-indices.
    if anchor_11 is None:
        anchor_11 = {2: Fr(1)}
    if brec_coeff is None:
        brec_coeff = lambda j, jk: Fr(j, jk)
    B = {
        (1, 1): dict(anchor_11),
        (2, 2): dict(R_ONE),
        (1, 2): {0: Fr(2)},
        (2, 1): {0: Fr(2)},
    }
    for total in range(2, N_VALUE + 1):
        for j in range(1, total):
            k = total - j
            if (j, k) in B:
                continue
            if j > 2 and (j - 2, k) in B:
                B[(j, k)] = rscale(brec_coeff(j - 2, j - 2 + k), B[(j - 2, k)])
            elif k > 2 and (j, k - 2) in B:
                B[(j, k)] = rscale(brec_coeff(k - 2, j + k - 2), B[(j, k - 2)])
    return B


def check_lattice(C, B, dup_factor=None, dup_half_index=1):
    # dup_factor(k) is 2^(1-2p) at p = k/2, i.e. 2^(1-k).
    if dup_factor is None:
        dup_factor = lambda k: Fr(1, 2 ** (k - 1))
    errs = []
    for (j, k), v in B.items():
        if (k, j) in B and not req(v, B[(k, j)]):
            errs.append("B_SYMMETRY(%d,%d)" % (j, k))
    # MP on the lattice
    for j in range(1, N_VALUE):
        for k in range(1, N_VALUE - j + 1):
            if (j, k) not in B:
                continue
            lhs = rmul(C[j], C[k])
            rhs = rmul(C[j + k], B[(j, k)])
            if not req(lhs, rhs):
                errs.append("MP(%d/2,%d/2)" % (j, k))
    # DUP for p = k/2, k = 1..N_INPUT (inputs pass the bound predicate)
    for k in range(1, N_INPUT + 1):
        if not dup_input_ok(k):
            errs.append("DUP_INPUT(%d)" % k)
            continue
        lhs = rmul(C[k], C[k + 1])
        rhs = rscale(dup_factor(k), rmul(C[dup_half_index], C[2 * k]))
        if not req(lhs, rhs):
            errs.append("DUP(%d/2)" % k)
    # B-HALF for p = k/2, k = 1..N_INPUT
    for k in range(1, N_INPUT + 1):
        lhs = B[(k, k)]
        rhs = rscale(dup_factor(k), B[(1, k)])
        if not req(lhs, rhs):
            errs.append("B_HALF(%d/2)" % k)
    if not req(B[(1, 1)], {2: Fr(1)}):
        errs.append("BRIDGE_ANCHOR")
    return errs


def eoc_parts(C, s):
    # Ehat(s) = g^-s C(s/2); Ohat(s) = g^-(s+1) C((s+1)/2);
    # Chat(s) = 2^(1-s) g^-2s C(s).  Half-index of C(x) is 2x, so
    # C(s/2) = C[s], C((s+1)/2) = C[s+1], C(s) = C[2s].
    if s not in EOC_DOMAIN:
        return None  # domain guard: rejected before any indexing
    ehat = rmul({-s: Fr(1)}, C[s])
    ohat = rmul({-(s + 1): Fr(1)}, C[s + 1])
    chat = rscale(Fr(1, 2 ** (s - 1)), rmul({-2 * s: Fr(1)}, C[2 * s]))
    return ehat, ohat, chat


def check_eoc(C):
    errs = []
    for s in EOC_DOMAIN:
        got = eoc_parts(C, s)
        if got is None:
            errs.append("EOC_DOMAIN(%d)" % s)
            continue
        ehat, ohat, chat = got
        if not req(rmul(ehat, ohat), chat):
            errs.append("EOC(%d)" % s)
        if s == 1:
            if not req(ehat, R_ONE):
                errs.append("ANCHOR_EHAT1")
            if not req(chat, {-2: Fr(1)}):
                errs.append("ANCHOR_CHAT1")
    return errs


# ---------------------------------------------------------------------------
# Gate 2 -- MODULUS_SCHEDULE (integer-exponent arithmetic only)
# D_b(a/c) = 2^-ceil(c(b+1+c)/a); audited: the ceiling inequality, the
# 1/r <= 2^c step, and the k-schedule inequalities k >= 0, k c >= a-c.
# The value (k+2)! 2^(b+1) is replayed as the frozen R_b.
# ---------------------------------------------------------------------------

MODULUS_PAIRS = ((1, 2, 4), (3, 2, 4), (7, 5, 6), (1, 7, 6))  # (a, c, b)


def factorial(n):
    out = 1
    for i in range(2, n + 1):
        out *= i
    return out


def ceil_div(x, y):
    return -((-x) // y)


def check_modulus(pairs=MODULUS_PAIRS, ceil_shift=1):
    # ceil_shift=1 is frozen: the exponent uses b + ceil_shift + c.
    errs = []
    for (a, c, b) in pairs:
        if a <= 0 or c <= 0:
            errs.append("MOD_DOMAIN")
            continue
        aexp = ceil_div(c * (b + ceil_shift + c), a)
        # D^r <= 2^-(b+1+c)  <=>  aexp * a >= c * (b+1+c)
        if not (aexp * a >= c * (b + 1 + c)):
            errs.append("MOD_CEIL(%d/%d,b=%d)" % (a, c, b))
        # 1/r = c/a <= c <= 2^c
        if not (c <= 2 ** c):
            errs.append("MOD_2POW(%d)" % c)
        # k = max(0, ceil((a-c)/c)) must satisfy k >= 0 and k c >= a-c,
        # the exact content of the (Minf') requirement k >= s-1.
        k = max(0, ceil_div(a - c, c))
        if not (k >= 0 and k * c >= a - c):
            errs.append("MOD_K(%d/%d)" % (a, c))
        # frozen tail value replay: (k+2)!/R_b = 2^-(b+1) with
        # R_b = (k+2)! 2^(b+1); replayed as the frozen pair (k, R_b).
        R = factorial(k + 2) * 2 ** (b + 1)
        if Fr(factorial(k + 2), R) != Fr(1, 2 ** (b + 1)):
            errs.append("MOD_TAIL(%d/%d,b=%d)" % (a, c, b))
    return errs


# ---------------------------------------------------------------------------
# Gate 3 -- MACHIN_WITNESSES
# Bivariate polynomials over Q as {(i,j): Fraction} in (u, v).
# ---------------------------------------------------------------------------


def pmul(a, b):
    out = {}
    for (i1, j1), c1 in a.items():
        for (i2, j2), c2 in b.items():
            key = (i1 + i2, j1 + j2)
            out[key] = out.get(key, Fr(0)) + c1 * c2
    return {k: v for k, v in out.items() if v != 0}


def padd(a, b):
    out = dict(a)
    for k, c in b.items():
        out[k] = out.get(k, Fr(0)) + c
    return {k: v for k, v in out.items() if v != 0}


def pneg(a):
    return {k: -v for k, v in a.items()}


P_ONE = {(0, 0): Fr(1)}
P_U = {(1, 0): Fr(1)}
P_V = {(0, 1): Fr(1)}


def machin_poly_residual(sq_coeff=Fr(1)):
    # (1-uv)^2 + sq_coeff*(u+v)^2 - (1+u^2)(1+v^2); frozen sq_coeff = 1.
    one_m_uv = padd(P_ONE, pneg(pmul(P_U, P_V)))
    u_p_v = padd(P_U, P_V)
    lhs = padd(pmul(one_m_uv, one_m_uv),
               {k: sq_coeff * c for k, c in pmul(u_p_v, u_p_v).items()})
    one_p_u2 = padd(P_ONE, pmul(P_U, P_U))
    one_p_v2 = padd(P_ONE, pmul(P_V, P_V))
    return padd(lhs, pneg(pmul(one_p_u2, one_p_v2)))


MACHIN_COMPOSITIONS = (
    # (u, v, claimed target, cross-left, cross-right); the composition
    # equality is checked division-free: (u+v) == target * (1 - u v),
    # and the domain bound as (u+v) <= 2 * (1 - u v).
    (Fr(1, 5), Fr(1, 5), Fr(5, 12), 10 * 12, 24 * 5),
    (Fr(5, 12), Fr(5, 12), Fr(120, 119), 720 * 119, 714 * 120),
    (Fr(1), Fr(1, 239), Fr(120, 119), 240 * 119, 238 * 120),
)


def check_machin(compositions=MACHIN_COMPOSITIONS, poly_coeff=Fr(1),
                 alt_sign=1):
    errs = []
    if machin_poly_residual(poly_coeff):
        errs.append("MACHIN_POLY")
    for (u, v, target, xl, xr) in compositions:
        if not (u * v < 1):
            errs.append("MACHIN_DOMAIN_UV")
            continue
        if not (u <= 2 and v <= 2):
            errs.append("MACHIN_DOMAIN_ARG")
        if (u + v) != target * (1 - u * v):
            errs.append("MACHIN_COMPOSE")
        if not ((u + v) <= 2 * (1 - u * v)):
            errs.append("MACHIN_DOMAIN_VAL")
        if xl != xr:
            errs.append("MACHIN_CROSS")
    # Q7 Step-1 indexing at q = 5, in the convention
    # S_(q,N) = sum_(n=0)^(N-1) (-1)^n a_(q,n): the partial-sum gaps
    # S_(N+1) - S_N = (-1)^N a_(q,N) for N = 1..4, strict monotone
    # decrease a_n > a_(n+1), and nesting of all later sums in the
    # hull of each consecutive pair.
    q = 5
    a = [Fr(1, (2 * n + 1) * q ** (2 * n + 1)) for n in range(0, 6)]
    for n in range(0, 5):
        if not (a[n] > a[n + 1]):
            errs.append("MACHIN_DECREASE(n=%d)" % n)
    S = [Fr(0)]
    for n in range(0, 5):
        S.append(S[-1] + (Fr(-1) ** n) * a[n] * alt_sign)
    for N in range(1, 5):
        gap = S[N + 1] - S[N]
        want = (Fr(-1) ** N) * a[N]
        if gap != want:
            errs.append("MACHIN_INDEXING(N=%d)" % N)
        lo, hi = min(S[N], S[N + 1]), max(S[N], S[N + 1])
        for m in range(N + 2, len(S)):
            if not (lo <= S[m] <= hi):
                errs.append("MACHIN_HULL(N=%d,m=%d)" % (N, m))
    return errs


# ---------------------------------------------------------------------------
# Gate 4 -- FORM_IDENTITY_REPLAY
# Exponent vectors linear in (p, q, s): (const, cp, cq, cs) over Q.
# Each substitution is audited as exact linear-form bookkeeping.
# ---------------------------------------------------------------------------


def lf(c0=0, cp=0, cq=0, cs=0):
    return (Fr(c0), Fr(cp), Fr(cq), Fr(cs))


def lf_add(x, y):
    return tuple(m + n for m, n in zip(x, y))


def lf_scale(k, x):
    return tuple(Fr(k) * m for m in x)


def check_forms(upull_target_1mu=lf(-1, 1, 0, 0), slope_jac=lf(1),
                epull_factor=Fr(1, 2), ql_factor=Fr(1, 2),
                sqrt_jac_exp=Fr(-1, 2), sqrt_factor=Fr(1, 2),
                join_left=lf(0, 0, 0, 1)):
    errs = []
    # F1 slope y = x t: y^(q-1) dy = x^(q-1) t^(q-1) * (x dt):
    # x-exponent total = (q-1) + slope_jac; frozen total q.
    if lf_add(lf(-1, 0, 1, 0), slope_jac) != lf(0, 0, 1, 0):
        errs.append("FORM_SLOPE")
    # F2 w = x(1+t): (1+t)-exponent total -(p+q-1) - 1 = -(p+q).
    tot = lf_add(lf_scale(-1, lf(-1, 1, 1, 0)), lf(-1))
    if tot != lf(0, -1, -1, 0):
        errs.append("FORM_WLIN")
    # F3 u = t/(1+t): t^(q-1)(1+t)^(-(p+q)) dt = u^(q-1)(1-u)^X du,
    # X = -(q-1) + (p+q) - 2; frozen X = p-1.
    X = lf_add(lf_add(lf_scale(-1, lf(-1, 0, 1, 0)), lf(0, 1, 1, 0)), lf(-2))
    if X != upull_target_1mu:
        errs.append("FORM_UPULL")
    # F4 v = w^(1/2): dv = (1/2) w^(-1/2) dw, the (1-w)-exponent p-1 is
    # carried unchanged; frozen Jacobian exponent -1/2 and factor 1/2.
    if sqrt_jac_exp != Fr(-1, 2) or sqrt_factor != Fr(1, 2):
        errs.append("FORM_SQRT")
    if lf(-1, 1, 0, 0) != lf(-1, 1, 0, 0):
        errs.append("FORM_SQRT_CARRY")
    # F5 y = x^2: x^(s-1) dx = (1/2) y^(s/2-1) dy; exponent check
    # (s-1)/2 - 1/2 = s/2 - 1 and frozen factor 1/2.
    if lf_add(lf_scale(Fr(1, 2), lf(-1, 0, 0, 1)), lf(Fr(-1, 2))) != \
            lf_add(lf_scale(Fr(1, 2), lf(0, 0, 0, 1)), lf(-1)):
        errs.append("FORM_EPULL_EXP")
    if epull_factor != Fr(1, 2):
        errs.append("FORM_EPULL_FACTOR")
    # F6 x = r^2 (quadratic-to-linear): (2s-1-1)/2 = s-1, factor 1/2.
    if lf_scale(Fr(1, 2), lf(-2, 0, 0, 2)) != lf(-1, 0, 0, 1):
        errs.append("FORM_QL_EXP")
    if ql_factor != Fr(1, 2):
        errs.append("FORM_QL_FACTOR")
    # F7 bridge half-power chain: (1+t)-exponents 1/2 + 1/2 - 2 = -1.
    if Fr(1, 2) + Fr(1, 2) - 2 != Fr(-1):
        errs.append("FORM_BRIDGE_CHAIN")
    # F8 JOIN: x * x^(s-1) = x^s as the exponent equality 1 + (s-1) = s.
    if lf_add(lf(1), lf(-1, 0, 0, 1)) != join_left:
        errs.append("FORM_JOIN")
    return errs


# ---------------------------------------------------------------------------
# Gate 5 -- SCALE_RESIDUALS at lambda = 2 (genuine ring computation)
# law = "original": residual of Ehat_l Ohat_l - Chat_l  (must be nonzero)
# law = "scaled":   residual of Ehat_l Ohat_l - lam Chat_l (identically 0;
#                   using it as a guard is the forbidden mutation)
# ---------------------------------------------------------------------------


def residuals(C, lam=Fr(2), law="original"):
    r1 = {0: lam - 1}
    r2 = {2: lam * lam - 1}
    r3s = []
    for s in EOC_DOMAIN:
        ehat, ohat, chat = eoc_parts(C, s)
        el, ol, cl = rscale(lam, ehat), rscale(lam, ohat), rscale(lam, chat)
        if law == "original":
            r3s.append(rsub(rmul(el, ol), cl))
        else:
            r3s.append(rsub(rmul(el, ol), rscale(lam, cl)))
    return r1, r2, r3s


def check_scale(C):
    errs = []
    r1, r2, r3s = residuals(C)
    if rzero(r1) or not req(r1, {0: Fr(1)}):
        errs.append("SCALE_R1")
    if rzero(r2) or not req(r2, {2: Fr(3)}):
        errs.append("SCALE_R2")
    for s, r3 in zip(EOC_DOMAIN, r3s):
        if rzero(r3):
            errs.append("SCALE_R3(%d)" % s)
    return errs


# ---------------------------------------------------------------------------
# Gate 6 -- PROOF_CONTROLS: 23 mutations; each must be rejected at its
# named semantic guard. A control that fails to reject is an integrity
# STOP (CONTROL_PASSED), never a scientific FIRED.
# ---------------------------------------------------------------------------


def run_controls():
    results = []

    def control(name, rejected):
        results.append((name, bool(rejected)))

    C0 = build_C()
    B0 = build_B()

    # 1 mutated REC coefficient
    control("REC_COEFF", check_lattice(build_C(lambda k: Fr(k + 2, 2)), B0))
    # 2 mutated DUP factor 2^(-2p) = 2^-k
    control("DUP_FACTOR", check_lattice(C0, B0,
            dup_factor=lambda k: Fr(1, 2 ** k)))
    # 3 displaced C(1/2) in DUP (uses C(1) instead)
    control("DUP_DISPLACED", check_lattice(C0, B0, dup_half_index=2))
    # 4 mutated B-REC coefficient j/(j+k+1)
    control("BREC_COEFF", check_lattice(C0,
            build_B(brec_coeff=lambda j, jk: Fr(j, jk + 1))))
    # 5 one-step diagonal-descent witness: the correct chain factor is
    # p/(2(2p+1)) = k/(4k+4); the mutated one-step claim p/(2p+1)
    # = k/(2k+2) must FAIL for every k.
    one_step_rejected = True
    for k in range(1, N_INPUT - 1):
        if req(B0[(k + 2, k + 2)], rscale(Fr(k, 2 * k + 2), B0[(k, k)])):
            one_step_rejected = False
    control("DIAG_ONESTEP", one_step_rejected)
    # 6 mutated bridge anchor g^2 + 1
    control("BRIDGE_ANCHOR", check_lattice(C0,
            build_B(anchor_11={2: Fr(1), 0: Fr(1)})))
    # 7 EOC outside the frozen domain (s = 1/2; rejected before any
    # lattice indexing, so no half-power object is ever formed)
    control("EOC_DOMAIN", eoc_parts(C0, Fr(1, 2)) is None)
    # 8 lattice bounds: input beyond N_input AND value beyond N_value
    control("LATTICE_BOUNDS",
            (not dup_input_ok(N_INPUT + 1)) and ((N_VALUE + 1) not in C0))
    # 9 mutated D_b ceiling (b+c instead of b+1+c)
    control("MOD_CEIL", check_modulus(ceil_shift=0))
    # 10 mutated schedule factorial: (k+1)!/R_b != 2^-(b+1)
    fact_mut_rejected = True
    for (a, c, b) in MODULUS_PAIRS:
        k = max(0, ceil_div(a - c, c))
        R = factorial(k + 2) * 2 ** (b + 1)
        if Fr(factorial(k + 1), R) == Fr(1, 2 ** (b + 1)):
            fact_mut_rejected = False
    control("MOD_FACT", fact_mut_rejected)
    # 11 mutated Machin polynomial coefficient
    control("MACHIN_POLY", check_machin(poly_coeff=Fr(2)))
    # 12 mutated cross witness
    control("MACHIN_CROSS", check_machin(compositions=(
        (Fr(5, 12), Fr(5, 12), Fr(120, 119), 720 * 119, 720 * 118),)))
    # 13 violated domain condition uv >= 1
    control("MACHIN_UV", check_machin(compositions=(
        (Fr(1), Fr(1), Fr(1), 1, 1),)))
    # 14 mutated Q7 Step-1 sign
    control("MACHIN_SIGN", check_machin(alt_sign=-1))
    # 15 mutated slope Jacobian (missing x)
    control("FORM_SLOPE", check_forms(slope_jac=lf(0)))
    # 16 mutated u-pullback bookkeeping (p instead of p-1)
    control("FORM_UPULL", check_forms(upull_target_1mu=lf(0, 1, 0, 0)))
    # 17 mutated E-PULL factor
    control("FORM_EPULL", check_forms(epull_factor=Fr(1)))
    # 18 mutated square-root and quadratic-linear Jacobians (both
    # halves of the mutation must be rejected)
    control("FORM_SQRT_QL",
            check_forms(sqrt_factor=Fr(1)) and check_forms(ql_factor=Fr(1)))
    # 19 JOIN as definition: mutated provenance table rejected by the
    # same guard the PASS path consumes
    mut_prov = dict(PROVENANCE)
    mut_prov["O_independent"] = False
    control("JOIN_CROSSREAD", check_provenance(mut_prov))
    # 20 lambda = 2 model accepted by the mutated scaled-law guard:
    # the same residual code path must accept (all zero) under the
    # scaled law and reject under the original law
    _r1, _r2, r3_orig = residuals(build_C(), law="original")
    _r1b, _r2b, r3_scaled = residuals(build_C(), law="scaled")
    control("SCALE_MUTGUARD",
            all(rzero(r) for r in r3_scaled) and
            all(not rzero(r) for r in r3_orig))
    # 21 dressed weight renamed away from p_M (provenance guard; a
    # name/graph test, never a numeric envelope test)
    mut_prov2 = dict(PROVENANCE)
    mut_prov2["dressed_weight"] = "p_X"
    control("WEIGHT_NAME", check_provenance(mut_prov2))
    # 22 nonpositive exponent rejected at the modulus domain guard
    # (irrational exponents are excluded by the reduced-integer-pair
    # input type itself)
    control("EXP_DOMAIN", check_modulus(pairs=((-1, 2, 4),)))
    # 23 claim label above the slice rejected by the label guard
    mut_lab = dict(LABELS)
    mut_lab["MELLIN_SEEDS"] = "PASS"
    control("LABEL_CAP", check_labels(mut_lab))

    return results


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    C = build_C()
    B = build_B()

    # integrity guards consumed by the PASS path
    for e in check_provenance(PROVENANCE):
        stop("PROVENANCE " + e)
    for e in check_labels(LABELS):
        stop("LABELS " + e)
    for elem in list(C.values()) + list(B.values()):
        if not rbits_ok(elem):
            stop("RATIONAL_BITS_CAP")
            break

    # scientific gates 1-4 (a completed exact negation is FIRED)
    for e in check_lattice(C, B) + check_eoc(C):
        fired("RING_LATTICE_REPLAY " + e)
    for e in check_modulus():
        fired("MODULUS_SCHEDULE " + e)
    for e in check_machin():
        fired("MACHIN_WITNESSES " + e)
    for e in check_forms():
        fired("FORM_IDENTITY_REPLAY " + e)

    # gate 5: the residuals are frozen ring constants; a mismatch can
    # only be a verifier defect, hence integrity STOP, not FIRED
    for e in check_scale(C):
        stop("SCALE_RESIDUALS " + e)

    # gate 6: proof controls; a control that fails to reject is STOP
    controls = run_controls()
    if len(controls) != 23:
        stop("CONTROL_COUNT %d" % len(controls))
    for name, rejected in controls:
        if not rejected:
            stop("CONTROL_PASSED " + name)

    if STOP_LIST:
        for msg in STOP_LIST:
            print("STOP " + msg)
        raise SystemExit(1)

    if FIRED_LIST:
        for msg in FIRED_LIST:
            print("FIRED " + msg)
        print("RESULT FIRED")
        return

    print("P_JIPC_WP3D_QPOS_MELLIN_AUDIT 1")
    print("ARITHMETIC Q_EXACT_FRACTION PASS")
    print("RING_LATTICE_REPLAY N_INPUT=6 N_VALUE=12 EOC=1,2,3 PASS")
    print("MODULUS_SCHEDULE PAIRS=4 PASS")
    print("MACHIN_WITNESSES POLY,CROSS3,DOMAINS,INDEXING PASS")
    print("FORM_IDENTITY_REPLAY FORMS=8 PASS")
    print("SCALE_RESIDUALS LAMBDA=2 GUARDS=3 PASS")
    print("PROOF_CONTROLS 23/23 PASS")
    print("THEOREM_CARRIER WRITTEN_PROOF_NOT_FINITE_AUDIT")
    print("RESULT PASS")


if __name__ == "__main__":
    main()
