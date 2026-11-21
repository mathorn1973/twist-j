#!/usr/bin/env python3
"""Independent blind verifier for PR #1862 finite contact Collatz contract.

Written from the markdown contract only (see PREREG.md in this directory).
Exact integer arithmetic only. Prints PASS/FAIL per frozen check C0..C12
and exits 0 only on complete PASS.
"""
import hashlib
import sys

# ---------------------------------------------------------------- ring O
# Element: tuple (a0,a1,a2,a3) = a0 + a1*t + a2*t^2 + a3*t^3,
# t satisfies 1 + t + t^2 + t^3 + t^4 = 0 (t is the text's j).

ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
T = (0, 1, 0, 0)


def add(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2], a[3] + b[3])


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2], a[3] - b[3])


def neg(a):
    return (-a[0], -a[1], -a[2], -a[3])


def mul(a, b):
    # Generic convolution, then reduce degrees >= 4 by t^5 = 1 and
    # t^4 = -1 - t - t^2 - t^3, from high degree downwards.
    c = [0] * 7
    for i in range(4):
        if a[i]:
            for k in range(4):
                c[i + k] += a[i] * b[k]
    for d in range(6, 3, -1):
        coef = c[d]
        if coef:
            if d >= 5:
                c[d - 5] += coef
            else:  # d == 4
                for i in range(4):
                    c[i] -= coef
    return (c[0], c[1], c[2], c[3])


def pow_elem(a, e):
    r = ONE
    for _ in range(e):
        r = mul(r, a)
    return r


def int_elem(n):
    return (n, 0, 0, 0)


RHO = mul(T, T)               # rho = j^2
U = sub(ONE, RHO)             # u = 1 - rho
W = add(ONE, RHO)             # w = 1 + rho (= J in the text)


def q_account(z):
    s = z[0] + z[1] + z[2] + z[3]
    num = 5 * (z[0] * z[0] + z[1] * z[1] + z[2] * z[2] + z[3] * z[3]) - s * s
    assert num % 2 == 0
    return num // 2


def eps(z):
    return (z[0] + z[1] + z[2] + z[3]) % 5


def contact_raw(a, b):
    d = sub(a, b)
    if d[0] % 2 or d[1] % 2 or d[2] % 2 or d[3] % 2:
        return (a, b)
    ssum = add(a, b)
    s = (ssum[0] // 2, ssum[1] // 2, ssum[2] // 2, ssum[3] // 2)
    t = (d[0] // 2, d[1] // 2, d[2] // 2, d[3] // 2)
    rt = mul(RHO, t)
    return (add(s, rt), sub(s, rt))


# Pair memoisation (convention K8): a fresh ordered pair is computed by
# contact_raw and audited once (check C2); later uses reuse the result.
PAIR_CACHE = {}
PAIR_FAILURES = []


def _audit_pair(a, b, out):
    x, y = a, b
    for _ in range(5):
        x, y = contact_raw(x, y)
    if (x, y) != (a, b):
        PAIR_FAILURES.append(("C^5!=id", a, b))
    x, y = out
    for _ in range(4):
        x, y = contact_raw(x, y)
    if (x, y) != (a, b):
        PAIR_FAILURES.append(("C^4 o C != id", a, b))
    if add(out[0], out[1]) != add(a, b):
        PAIR_FAILURES.append(("pair sum", a, b))
    if q_account(out[0]) + q_account(out[1]) != q_account(a) + q_account(b):
        PAIR_FAILURES.append(("Q sum", a, b))
    if eps(out[0]) != eps(a) or eps(out[1]) != eps(b):
        PAIR_FAILURES.append(("eps per slot", a, b))


def contact(a, b):
    key = (a, b)
    out = PAIR_CACHE.get(key)
    if out is None:
        out = contact_raw(a, b)
        PAIR_CACHE[key] = out
        _audit_pair(a, b, out)
    return out


def apply_word(state, edges):
    cache = PAIR_CACHE
    for i, j in edges:
        a = state[i]
        b = state[j]
        out = cache.get((a, b))
        if out is None:
            out = contact(a, b)
        state[i], state[j] = out


def apply_inverse_word(state, edges):
    # Reversed edges, four literal contacts per reversed edge.
    for i, j in reversed(edges):
        for _ in range(4):
            state[i], state[j] = contact(state[i], state[j])


# ------------------------------------------------------- Collatz from def.

D_DOMAIN = (1, 3, 5, 7, 9, 11, 13, 15, 17, 23)
I_INPUTS = (1, 3, 5, 7, 9, 11, 13, 15)

# Text table (PROOF.md:174-185), used ONLY as the C3 comparison target.
TEXT_TABLE = {
    1: (1, 2), 3: (5, 1), 5: (1, 4), 7: (11, 1), 9: (7, 2),
    11: (17, 1), 13: (5, 3), 15: (23, 1), 17: (13, 2), 23: (35, 1),
}


def collatz(n):
    x = 3 * n + 1
    v = 0
    while x % 2 == 0:
        x //= 2
        v += 1
    return x, v


TABLE = {n: collatz(n) for n in D_DOMAIN}

# ---------------------------------------------------------------- compiler

X0, Y0, A0, B0 = 0, 12, 24, 30
SCR0 = 36
SEL_A, SEL_B, SEL_S = 45, 46, 47
HELPER = 48
NSLOTS = 49


def rail(base, k, bitvalue):
    return base + 2 * k + (1 if bitvalue else 0)


def bit_pair(base, k):
    return (base + 2 * k, base + 2 * k + 1)


def d_edges(h, c, d):
    return [(h, c)] * 3 + [(h, d)] * 3 + [(h, c), (h, d), (h, c)]


def v_edges(g, h, c, d):
    de = d_edges(h, c, d)
    return [(g, h)] + de + [(g, h)] * 4 + de


MACROS = []  # ('V', g, c, d) or ('D', c, d); helper is always slot 48


def emit_v(g, c, d):
    MACROS.append(('V', g, c, d))


def emit_d(c, d):
    MACROS.append(('D', c, d))


def emit_minterm(controls, target_pairs):
    if not target_pairs:
        return
    k = len(controls)
    if k == 1:
        for (c, d) in target_pairs:
            emit_v(controls[0], c, d)
        return
    borrows = [(controls[0], controls[1], SCR0)]
    for r in range(1, k - 1):
        borrows.append((SCR0 + r - 1, controls[r + 1], SCR0 + r))
    for (g, c, d) in borrows:
        emit_v(g, c, d)
    last = SCR0 + k - 2
    for (c, d) in target_pairs:
        emit_v(last, c, d)
    for (g, c, d) in reversed(borrows):
        emit_v(g, c, d)


def build_module(sel_slot, arch_base):
    # Stage 1: X-minterm for n -> XOR m into Y, v into archive.
    for n in D_DOMAIN:
        m, v = TABLE[n]
        controls = [sel_slot] + [rail(X0, k, (n >> k) & 1) for k in range(6)]
        targets = [bit_pair(Y0, k) for k in range(6) if (m >> k) & 1]
        targets += [bit_pair(arch_base, k) for k in range(3) if (v >> k) & 1]
        emit_minterm(controls, targets)
    # Stage 2: (Y, archive)-minterm for (m, v) -> XOR n into X.
    for n in D_DOMAIN:
        m, v = TABLE[n]
        controls = [sel_slot]
        controls += [rail(Y0, k, (m >> k) & 1) for k in range(6)]
        controls += [rail(arch_base, k, (v >> k) & 1) for k in range(3)]
        targets = [bit_pair(X0, k) for k in range(6) if (n >> k) & 1]
        emit_minterm(controls, targets)
    # Stage 3: per bit, Y -> X then X -> Y, both selector-controlled.
    for k in range(6):
        emit_minterm([sel_slot, rail(Y0, k, 1)], [bit_pair(X0, k)])
        emit_minterm([sel_slot, rail(X0, k, 1)], [bit_pair(Y0, k)])


def build_word():
    global MACROS
    MACROS = []
    build_module(SEL_A, A0)
    build_module(SEL_B, B0)
    emit_d(SEL_B, SEL_S)
    emit_d(SEL_A, SEL_B)
    edges = []
    for mac in MACROS:
        if mac[0] == 'V':
            edges += v_edges(mac[1], HELPER, mac[2], mac[3])
        else:
            edges += d_edges(HELPER, mac[1], mac[2])
    return list(MACROS), edges


# ------------------------------------------------------------------- states

class Fail(Exception):
    pass


def encode_reg(state, base, nbits, value):
    for k in range(nbits):
        if (value >> k) & 1:
            state[base + 2 * k] = ZERO
            state[base + 2 * k + 1] = U
        else:
            state[base + 2 * k] = U
            state[base + 2 * k + 1] = ZERO


def decode_reg(state, base, nbits):
    val = 0
    for k in range(nbits):
        lo = state[base + 2 * k]
        hi = state[base + 2 * k + 1]
        if lo == U and hi == ZERO:
            pass
        elif lo == ZERO and hi == U:
            val |= (1 << k)
        else:
            raise Fail(f"non-binary rails at base {base} bit {k}: {lo} {hi}")
    return val


def make_state(x_val, a_val, b_val, sel_slot):
    st = [ZERO] * NSLOTS
    encode_reg(st, X0, 6, x_val)
    encode_reg(st, Y0, 6, 0)
    encode_reg(st, A0, 3, a_val)
    encode_reg(st, B0, 3, b_val)
    st[sel_slot] = U
    st[HELPER] = W
    return st


def selector_of(state):
    toks = [s for s in (SEL_A, SEL_B, SEL_S) if state[s] == U]
    others = [s for s in (SEL_A, SEL_B, SEL_S) if state[s] not in (U, ZERO)]
    if len(toks) != 1 or others:
        raise Fail(f"selector not a single token: "
                   f"{[state[s] for s in (SEL_A, SEL_B, SEL_S)]}")
    return toks[0]


def check_boundary(state, want_x, want_a, want_b, want_sel):
    if decode_reg(state, X0, 6) != want_x:
        raise Fail(f"X={decode_reg(state, X0, 6)} != {want_x}")
    if decode_reg(state, A0, 3) != want_a:
        raise Fail(f"A={decode_reg(state, A0, 3)} != {want_a}")
    if decode_reg(state, B0, 3) != want_b:
        raise Fail(f"B={decode_reg(state, B0, 3)} != {want_b}")
    if decode_reg(state, Y0, 6) != 0:
        raise Fail("Y not blank at boundary")
    if any(state[i] != ZERO for i in range(SCR0, SCR0 + 9)):
        raise Fail("scratch not blank at boundary")
    if state[HELPER] != W:
        raise Fail("helper != w at boundary")
    if selector_of(state) != want_sel:
        raise Fail(f"selector {selector_of(state)} != {want_sel}")
    total = ZERO
    for z in state:
        total = add(total, z)
    want_sum = ZERO
    for _ in range(19):
        want_sum = add(want_sum, U)
    want_sum = add(want_sum, W)
    if total != want_sum:
        raise Fail(f"total sum {total} != 19u+w {want_sum}")
    if sum(q_account(z) for z in state) != 98:
        raise Fail("total Q != 98 at boundary")


# -------------------------------------------------------------------- checks

RESULTS = {}


def record(cid, ok, detail):
    RESULTS[cid] = (bool(ok), detail)


def guard(cid, fn):
    try:
        detail = fn()
        record(cid, True, detail)
    except Fail as e:
        record(cid, False, str(e))
    except Exception as e:  # any exception is a failed check, never a pass
        record(cid, False, f"exception {type(e).__name__}: {e}")


def check_c0():
    if add(add(add(add(ONE, T), mul(T, T)), pow_elem(T, 3)), pow_elem(T, 4)) != ZERO:
        raise Fail("1+t+t^2+t^3+t^4 != 0")
    if pow_elem(RHO, 5) != ONE or RHO == ONE:
        raise Fail("rho order is not 5")
    if q_account(U) != 5 or q_account(W) != 3:
        raise Fail(f"Q(u)={q_account(U)} Q(w)={q_account(W)}")
    if eps(RHO) != 1 or eps(U) != 0:
        raise Fail(f"eps(rho)={eps(RHO)} eps(u)={eps(U)}")
    return "ring identities, Q(u)=5, Q(w)=3, eps(rho)=1, eps(u)=0"


def _local_macro(edges, init4):
    # slots 0=g,1=h,2=c,3=d (for D alone slot 0 is unused padding)
    st = list(init4)
    apply_word(st, edges)
    final = list(st)
    apply_inverse_word(st, edges)
    if st != list(init4):
        raise Fail(f"native inverse did not restore {init4}, got {st}")
    return final


def check_c1():
    w2 = add(ONE, pow_elem(RHO, 2))  # 1 + rho^2
    targets = [(ZERO, ZERO), (U, ZERO), (ZERO, U)]
    # D rows: helper w swaps, helper w2 is identity (PROOF.md:61-68).
    for h in (W, w2):
        for (c, d) in targets:
            fin = _local_macro(d_edges(1, 2, 3), [ZERO, h, c, d])
            want_cd = (d, c) if h == W else (c, d)
            if fin[1] != h or (fin[2], fin[3]) != want_cd:
                raise Fail(f"D row h={h} target=({c},{d}) -> {fin[1:]}")
    # V rows: swap exactly when g = u (PROOF.md:95-102).
    for g in (ZERO, U):
        for (c, d) in targets:
            fin = _local_macro(v_edges(0, 1, 2, 3), [g, W, c, d])
            want_cd = (d, c) if g == U else (c, d)
            if fin[0] != g or fin[1] != W or (fin[2], fin[3]) != want_cd:
                raise Fail(f"V row g={g} target=({c},{d}) -> {fin}")
    if len(v_edges(0, 1, 2, 3)) != 23 or len(d_edges(1, 2, 3)) != 9:
        raise Fail("V/D contact counts are not 23/9")
    return "6 D rows + 6 V rows by literal contacts, each with native inverse"


def check_c3():
    seen = set()
    for n in D_DOMAIN:
        m, v = TABLE[n]
        if (m, v) != TEXT_TABLE[n]:
            raise Fail(f"n={n}: computed ({m},{v}) != text {TEXT_TABLE[n]}")
        if (m, v) in seen:
            raise Fail(f"(m,v)=({m},{v}) not injective")
        seen.add((m, v))
        if (2 ** v * m - 1) % 3 != 0 or (2 ** v * m - 1) // 3 != n:
            raise Fail(f"inverse formula fails for n={n}")
        if m >= 64 or v >= 8:
            raise Fail(f"n={n}: (m,v) does not fit 6/3 bits")
    return "10 rows from 3n+1 definition match text table; (m,v) injective"


MACROS_W, EDGES_W = build_word()


def check_c4():
    nv = sum(1 for mac in MACROS_W if mac[0] == 'V')
    nd = sum(1 for mac in MACROS_W if mac[0] == 'D')
    if nv != 794 or nd != 2:
        raise Fail(f"V macros={nv}, D macros={nd}, want 794/2")
    if len(EDGES_W) != 18280 or len(EDGES_W) != 23 * nv + 9 * nd:
        raise Fail(f"contacts={len(EDGES_W)}, want 18280")
    for (i, j) in EDGES_W:
        if not (0 <= i < NSLOTS and 0 <= j < NSLOTS and i != j):
            raise Fail(f"bad edge {(i, j)}")
    blob = bytearray()
    for (i, j) in EDGES_W:
        blob.append(i)
        blob.append(j)
    digest = hashlib.sha256(bytes(blob)).hexdigest()
    return f"794 V + 2 D, 18280 contacts; my edge SHA256 (K6)={digest}"


TRAJ = {}  # n -> dict with boundaries and decoded first/final data


def check_c5():
    for n in I_INPUTS:
        st = make_state(n, 0, 0, SEL_A)
        check_boundary(st, n, 0, 0, SEL_A)
    return "8 prepared states: sum 19u+w, Q=98, work ready, selector A"


def check_c6():
    lines = []
    for n in I_INPUTS:
        m1, v1 = TABLE[n]
        if n not in D_DOMAIN or m1 not in D_DOMAIN:
            raise Fail(f"active input outside D for n={n} (m1={m1})")
        m2, v2 = TABLE[m1]
        st = make_state(n, 0, 0, SEL_A)
        wants = [(m1, v1, 0, SEL_B), (m2, v1, v2, SEL_S), (m2, v1, v2, SEL_A)]
        bounds = []
        for wi, (wx, wa, wb, wsel) in enumerate(wants, start=1):
            apply_word(st, EDGES_W)
            try:
                check_boundary(st, wx, wa, wb, wsel)
            except Fail as e:
                raise Fail(f"n={n} after W{wi}: {e}")
            bounds.append(list(st))
            ser = ";".join(",".join(str(c) for c in slot) for slot in st)
            lines.append(f"{n}|{wi}|{ser}\n")
        TRAJ[n] = {"m1": m1, "v1": v1, "m2": m2, "v2": v2, "bounds": bounds}
    digest = hashlib.sha256("".join(lines).encode("ascii")).hexdigest()
    return ("8 trajectories x 3 boundaries exact; "
            f"my boundary SHA256 (K7)={digest}")


def check_c7():
    for n in I_INPUTS:
        init = make_state(n, 0, 0, SEL_A)
        st = list(init)
        for _ in range(3):
            apply_word(st, EDGES_W)
        for _ in range(3):
            apply_inverse_word(st, EDGES_W)
        if st != init:
            raise Fail(f"n={n}: 3W inverse did not restore initial state")
    return "full primitive inverse of 3W restores all 8 initial states"


def check_c8():
    count = 0
    for n in D_DOMAIN:
        m, v = TABLE[n]
        for prior_a in range(8):
            init = make_state(n, prior_a, 0, SEL_B)
            st = list(init)
            apply_word(st, EDGES_W)
            try:
                check_boundary(st, m, prior_a, v, SEL_S)
            except Fail as e:
                raise Fail(f"n={n} priorA={prior_a}: {e}")
            apply_inverse_word(st, EDGES_W)
            if st != init:
                raise Fail(f"n={n} priorA={prior_a}: inverse mismatch")
            count += 1
    if count != 80:
        raise Fail(f"ran {count} cases, want 80")
    return "80 occupied-A continuations exact, each with full inverse"


def check_c9():
    # Abstract token semantics validated in C1: values 0=no token, 1=u, 2=w.
    tape = []
    for mac in MACROS_W:
        if mac[0] == 'V':
            tape.append((0, mac[1], mac[2], mac[3]))
        else:
            tape.append((1, 0, mac[1], mac[2]))
    cases = 0
    for x in range(64):
        for a in range(8):
            for b in range(8):
                st = [0] * NSLOTS
                for base, nbits, val in ((X0, 6, x), (Y0, 6, 0),
                                         (A0, 3, a), (B0, 3, b)):
                    for k in range(nbits):
                        bit = (val >> k) & 1
                        st[base + 2 * k] = 0 if bit else 1
                        st[base + 2 * k + 1] = 1 if bit else 0
                st[SEL_S] = 1
                st[HELPER] = 2
                for (kind, g, c, d) in tape:
                    if st[c] not in (0, 1) or st[d] not in (0, 1) \
                            or st[c] + st[d] > 1:
                        raise Fail("macro target precondition violated")
                    if kind == 0:
                        if st[g] not in (0, 1):
                            raise Fail("macro control precondition violated")
                        if st[g] == 1:
                            st[c], st[d] = st[d], st[c]
                    else:
                        st[c], st[d] = st[d], st[c]
                # decode abstractly
                def dec(base, nbits):
                    val = 0
                    for k in range(nbits):
                        lo, hi = st[base + 2 * k], st[base + 2 * k + 1]
                        if (lo, hi) == (0, 1):
                            val |= (1 << k)
                        elif (lo, hi) != (1, 0):
                            raise Fail("abstract rails corrupted")
                    return val
                if dec(X0, 6) != x or dec(A0, 3) != a or dec(B0, 3) != b \
                        or dec(Y0, 6) != 0:
                    raise Fail(f"skip changed registers x={x} a={a} b={b}")
                if any(st[i] != 0 for i in range(SCR0, SCR0 + 9)):
                    raise Fail("skip left scratch dirty")
                if st[SEL_A] != 1 or st[SEL_B] != 0 or st[SEL_S] != 0:
                    raise Fail("skip did not advance selector S->A")
                if st[HELPER] != 2:
                    raise Fail("skip touched helper")
                cases += 1
    if cases != 4096:
        raise Fail(f"ran {cases} cases, want 4096")
    return "4096 skip cases unchanged at MACRO level (not primitive replay)"


def check_c10():
    for n in I_INPUTS:
        t = TRAJ.get(n)
        if t is None:
            raise Fail(f"trajectory for n={n} missing (C6 failed?)")
        x = t["m2"]
        for v in (t["v2"], t["v1"]):  # reverse archive order: B, then A
            if (2 ** v * x - 1) % 3 != 0:
                raise Fail(f"n={n}: inexact inverse division")
            x = (2 ** v * x - 1) // 3
        if x != n:
            raise Fail(f"n={n}: recovered {x}")
    return "final X + ordered depths recover all 8 inputs exactly"


def check_c11():
    by_m = {}
    for n in D_DOMAIN:
        m, v = TABLE[n]
        by_m.setdefault(m, []).append((n, v))
    found = [(m, rows) for m, rows in by_m.items()
             if len({v for _, v in rows}) > 1]
    if not found:
        raise Fail("no common first output with distinct depths")
    for (n1, n2, m, v1, v2) in ((1, 5, 1, 2, 4), (3, 13, 5, 1, 3)):
        if TABLE[n1] != (m, v1) or TABLE[n2] != (m, v2):
            raise Fail(f"text pair {n1},{n2} not reproduced")
        # also confirm in the actual trajectories where available
        for n, vv in ((n1, v1), (n2, v2)):
            if n in TRAJ and (TRAJ[n]["m1"], TRAJ[n]["v1"]) != (m, vv):
                raise Fail(f"trajectory first step mismatch for n={n}")
    return "pairs (1,5)->m=1 depths 2,4 and (3,13)->m=5 depths 1,3"


def check_c12():
    jinv = neg(add(RHO, pow_elem(RHO, 3)))  # -rho - rho^3
    if mul(W, jinv) != ONE:
        raise Fail("J * (-rho-rho^3) != 1")
    slots = 6  # active + D+1 = 5 zero slots, D = 4
    for n in D_DOMAIN:
        m, v = TABLE[n]
        if v > 4:
            raise Fail(f"n={n}: v={v} exceeds cascade depth 4")
        st = [int_elem(3 * n + 1)] + [ZERO] * (slots - 1)
        for s in range(1, slots):
            st[0], st[s] = contact(st[0], st[s])
        prefix = 0
        while prefix < slots - 1 and st[1 + prefix] != ZERO:
            prefix += 1
        if any(st[1 + i] != ZERO for i in range(prefix, slots - 1)):
            raise Fail(f"n={n}: stored slots not a nonzero prefix")
        if prefix != v:
            raise Fail(f"n={n}: nonzero prefix {prefix} != v={v}")
        if mul(pow_elem(jinv, v), st[0]) != int_elem(m):
            raise Fail(f"n={n}: J^-v * active != m")
    for n in D_DOMAIN:  # odd x is refused by C(x, 0)
        x = int_elem(n)
        if contact(x, ZERO) != (x, ZERO):
            raise Fail(f"odd x={n} not left fixed by C(x,0)")
    return "finite instances only: J inverse, halving cascade for 3n+1 (n in D)"


def main():
    guard("C0", check_c0)
    guard("C1", check_c1)
    guard("C3", check_c3)
    guard("C4", check_c4)
    guard("C5", check_c5)
    guard("C6", check_c6)
    guard("C7", check_c7)
    guard("C8", check_c8)
    guard("C9", check_c9)
    guard("C10", check_c10)
    guard("C11", check_c11)
    guard("C12", check_c12)
    # C2 is finalised only after every primitive replay above has run.
    if PAIR_FAILURES:
        record("C2", False,
               f"{len(PAIR_FAILURES)} pair failures, first {PAIR_FAILURES[0]}")
    else:
        record("C2", True,
               f"{len(PAIR_CACHE)} distinct ordered primitive pairs audited "
               "(C^5, C^4 inverse, sum, Q, eps per slot)")
    all_ok = True
    for i in range(13):
        cid = f"C{i}"
        ok, detail = RESULTS.get(cid, (False, "not run"))
        all_ok = all_ok and ok
        print(f"{cid} {'PASS' if ok else 'FAIL'} {detail}")
    if all(n in TRAJ for n in I_INPUTS):
        print("trajectories (n -> after W1, after W2, depths):")
        for n in I_INPUTS:
            t = TRAJ[n]
            print(f"  {n} -> {t['m1']}, {t['m2']}, ({t['v1']},{t['v2']})")
    print("OVERALL " + ("PASS" if all_ok else "FAIL"))
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
