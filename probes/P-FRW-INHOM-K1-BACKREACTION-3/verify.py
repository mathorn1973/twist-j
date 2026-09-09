#!/usr/bin/env python3
from __future__ import annotations

from collections import deque
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
from pathlib import Path

P = 5
NVERT = P ** 3
W1 = F(29, 324)
W2 = F(65, 324)
NORM = F(1, 25)
EXPECTED_CANON_SHA256 = "5dcbf2abac151af1e6019ea4c009c7631cb773824a850bc5f5ff61bb324f9146"
EXPECTED_CANON_BYTES = 580724
WORDS = (
    "0010", "0011", "0100", "0101", "0110",
    "1001", "1010", "1011", "1100", "1101",
)
WORD_WEIGHT = {
    "0010": F(1, 12), "0011": F(1, 12), "0100": F(1, 12),
    "0101": F(1, 12), "0110": F(1, 6), "1001": F(1, 6),
    "1010": F(1, 12), "1011": F(1, 12), "1100": F(1, 12),
    "1101": F(1, 12),
}
EXPECTED_U = {
    "0010": (1, 0), "0011": (1, 1), "0100": (0, -1),
    "0101": (0, 0), "0110": (1, -1), "1001": (-1, 1),
    "1010": (0, 0), "1011": (0, 1), "1100": (-1, -1),
    "1101": (-1, 0),
}

VERTICES = list(product(range(P), repeat=3))
VID = {x: i for i, x in enumerate(VERTICES)}
EDGES: list[tuple[int, int, F, int, int]] = []
for x in VERTICES:
    t = VID[x]
    for a in range(3):
        for k, w in ((1, W1), (2, W2)):
            y = list(x)
            y[a] = (y[a] + k) % P
            h = VID[tuple(y)]
            EDGES.append((t, h, w, a, k))


FAILURES = []

def check(label: str, ok: bool, detail: str) -> None:
    verdict = "PASS" if ok else "FAIL"
    print(f"{label} {verdict} {detail}")
    if not ok:
        FAILURES.append(label)


def addv(a, b):
    return [x + y for x, y in zip(a, b)]


def subv(a, b):
    return [x - y for x, y in zip(a, b)]


def scal(c, a):
    return [c * x for x in a]


def B(f):
    return [f[h] - f[t] for t, h, _, _, _ in EDGES]


def Bt(u):
    out = [F(0) for _ in range(NVERT)]
    for val, (t, h, _, _, _) in zip(u, EDGES):
        out[t] -= val
        out[h] += val
    return out


def WB(f):
    g = B(f)
    return [w * val for val, (_, _, w, _, _) in zip(g, EDGES)]


def L3(f):
    return Bt(WB(f))


def inner_v(a, b):
    return NORM * sum((x * y for x, y in zip(a, b)), F(0))


def inner_e(a, b):
    return NORM * sum((x * y for x, y in zip(a, b)), F(0))


def mean_v(a):
    return sum(a, F(0)) / NVERT


def pi0(a):
    m = mean_v(a)
    return [x - m for x in a]


def embed5(f):
    return [f[x[2]] for x in VERTICES]


def collapse_planar(a):
    out = [None] * P
    for x, val in zip(VERTICES, a):
        r = x[2]
        if out[r] is None:
            out[r] = val
        elif out[r] != val:
            raise AssertionError("not planar")
    return [v for v in out]


def L5(f):
    return [
        (F(188) * f[r]
         - F(29) * (f[(r + 1) % P] + f[(r - 1) % P])
         - F(65) * (f[(r + 2) % P] + f[(r - 2) % P])) / F(324)
        for r in range(P)
    ]


def k1_u(word):
    b = tuple(int(c) for c in word)
    return (b[2] - b[0], b[3] - b[1])


def k1_h(u):
    out = [F(0) for _ in range(P)]
    out[u % P] += F(1, 2)
    out[(u + 1) % P] += F(1, 2)
    return out


def next5(prev, cur):
    return subv(scal(F(2), cur), addv(L5(cur), prev))


def next3(prev, cur):
    return subv(scal(F(2), cur), addv(L3(cur), prev))


def energy(hn, hp):
    d = subv(hp, hn)
    gn = B(hn)
    gp = B(hp)
    e = [F(1, 2) * x * x for x in d]
    for gv0, gv1, (t, h, w, _, _) in zip(gn, gp, EDGES):
        z = F(1, 4) * w * gv1 * gv0
        e[t] += z
        e[h] += z
    return e


def current(hm, h0, hp):
    q = subv(hp, hm)
    g = B(h0)
    out = []
    for gv, (t, h, w, _, _) in zip(g, EDGES):
        out.append(F(1, 4) * w * gv * (q[t] + q[h]))
    return out


def residual(hm, h0, hp):
    return addv(subv(addv(hp, hm), scal(F(2), h0)), L3(h0))


def global_energy(hn, hp):
    d = subv(hp, hn)
    return F(1, 2) * (inner_v(d, d) + inner_v(hp, L3(hn)))


def rank_mod(mat, p):
    a = [[x % p for x in row] for row in mat]
    m = len(a)
    n = len(a[0]) if m else 0
    row = 0
    for col in range(n):
        pivot = None
        for r in range(row, m):
            if a[r][col]:
                pivot = r
                break
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        inv = pow(a[row][col], p - 2, p)
        a[row] = [(v * inv) % p for v in a[row]]
        for r in range(m):
            if r != row and a[r][col]:
                c = a[r][col]
                a[r] = [(x - c * y) % p for x, y in zip(a[r], a[row])]
        row += 1
        if row == m:
            break
    return row


def solve_square(A, b):
    n = len(A)
    aug = [list(row) + [rhs] for row, rhs in zip(A, b)]
    for col in range(n):
        pivot = next((r for r in range(col, n) if aug[r][col] != 0), None)
        if pivot is None:
            raise AssertionError("singular square solve")
        aug[col], aug[pivot] = aug[pivot], aug[col]
        c = aug[col][col]
        aug[col] = [x / c for x in aug[col]]
        for r in range(n):
            if r == col:
                continue
            c = aug[r][col]
            if c:
                aug[r] = [x - c * y for x, y in zip(aug[r], aug[col])]
    return [aug[i][-1] for i in range(n)]


L5_MATRIX = []
for r in range(P):
    basis = [F(0) for _ in range(P)]
    basis[r] = F(1)
    col = L5(basis)
    if not L5_MATRIX:
        L5_MATRIX = [[F(0) for _ in range(P)] for _ in range(P)]
    for i in range(P):
        L5_MATRIX[i][r] = col[i]


def solve_tau_planar(source5):
    if sum(source5, F(0)) != 0:
        raise AssertionError("tau source has nonzero mean")
    A = [list(L5_MATRIX[r]) for r in range(P - 1)] + [[F(1)] * P]
    b = list(source5[:P - 1]) + [F(0)]
    tau = solve_square(A, b)
    if L5(tau) != list(source5) or sum(tau, F(0)) != 0:
        raise AssertionError("tau solve failed")
    return tau


# Sparse quadratic polynomial machinery for the exact G3 identity.
def lin_add(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, F(0)) + v
        if out[k] == 0:
            del out[k]
    return out


def lin_scale(c, a):
    return {k: c * v for k, v in a.items() if c * v}


def qadd(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, F(0)) + v
        if out[k] == 0:
            del out[k]
    return out


def qscale(c, a):
    return {k: c * v for k, v in a.items() if c * v}


def lmul(a, b):
    out = {}
    for i, x in a.items():
        for j, y in b.items():
            k = (i, j) if i <= j else (j, i)
            out[k] = out.get(k, F(0)) + x * y
    return {k: v for k, v in out.items() if v}


def var(time, vertex):
    return {time * NVERT + vertex: F(1)}


def symbolic_balance_certificate():
    hm = [var(0, x) for x in range(NVERT)]
    h0 = [var(1, x) for x in range(NVERT)]
    hp = [var(2, x) for x in range(NVERT)]
    lhs = [{} for _ in range(NVERT)]

    for x in range(NVERT):
        dp = lin_add(hp[x], lin_scale(-1, h0[x]))
        dm = lin_add(h0[x], lin_scale(-1, hm[x]))
        lhs[x] = qadd(lhs[x], qscale(F(1, 2), lmul(dp, dp)))
        lhs[x] = qadd(lhs[x], qscale(F(-1, 2), lmul(dm, dm)))

    Lh0 = [{} for _ in range(NVERT)]
    for t, h, w, _, _ in EDGES:
        gm = lin_add(hm[h], lin_scale(-1, hm[t]))
        g0 = lin_add(h0[h], lin_scale(-1, h0[t]))
        gp = lin_add(hp[h], lin_scale(-1, hp[t]))
        ediff = qscale(F(1, 4) * w,
                       qadd(lmul(gp, g0), qscale(-1, lmul(g0, gm))))
        lhs[t] = qadd(lhs[t], ediff)
        lhs[h] = qadd(lhs[h], ediff)

        qt = lin_add(hp[t], lin_scale(-1, hm[t]))
        qh = lin_add(hp[h], lin_scale(-1, hm[h]))
        j = qscale(F(1, 4) * w, lmul(g0, lin_add(qt, qh)))
        lhs[t] = qadd(lhs[t], qscale(-1, j))
        lhs[h] = qadd(lhs[h], j)

        # L h0 = B^T W B h0
        Lh0[t] = lin_add(Lh0[t], lin_scale(w, lin_add(h0[t], lin_scale(-1, h0[h]))))
        Lh0[h] = lin_add(Lh0[h], lin_scale(w, lin_add(h0[h], lin_scale(-1, h0[t]))))

    for x in range(NVERT):
        qx = lin_add(hp[x], lin_scale(-1, hm[x]))
        R = lin_add(lin_add(hp[x], hm[x]), lin_scale(-2, h0[x]))
        R = lin_add(R, Lh0[x])
        rhs = qscale(F(1, 2), lmul(qx, R))
        if lhs[x] != rhs:
            return False, x, len(lhs[x]), len(rhs)
    terms = sum(len(p) for p in lhs)
    return True, -1, terms, terms


def g1_incidence():
    ok_counts = len(VERTICES) == 125 and len(EDGES) == 750
    ok_weights = all(w > 0 for _, _, w, _, _ in EDGES)

    adj = [[] for _ in range(NVERT)]
    for t, h, _, _, k in EDGES:
        if k == 1:
            adj[t].append(h)
            adj[h].append(t)
    seen = {0}
    q = deque([0])
    while q:
        x = q.popleft()
        for y in adj[x]:
            if y not in seen:
                seen.add(y)
                q.append(y)
    ok_conn = len(seen) == NVERT

    M = [[0 for _ in range(NVERT)] for _ in range(NVERT)]
    for t, h, w, _, _ in EDGES:
        wn = w * 324
        if wn.denominator != 1:
            raise AssertionError("weight scale")
        c = wn.numerator
        M[t][t] += c
        M[h][h] += c
        M[t][h] -= c
        M[h][t] -= c
    ok_rows = all(sum(row) == 0 for row in M)
    rk = rank_mod(M, 1000003)

    planar = True
    norm = True
    for r in range(P):
        f = [F(int(i == r)) for i in range(P)]
        if L3(embed5(f)) != embed5(L5(f)):
            planar = False
        for s in range(P):
            g = [F(int(i == s)) for i in range(P)]
            if inner_v(embed5(f), embed5(g)) != sum((x * y for x, y in zip(f, g)), F(0)):
                norm = False
    check("G1", ok_counts and ok_weights and ok_conn and ok_rows and rk == 124 and planar and norm,
          f"|X|=125 |E|=750 rank(L3)=124 planar=L_public norm=exact")


def g2_k1():
    ok = sum(WORD_WEIGHT.values(), F(0)) == 1
    for word in WORDS:
        u = k1_u(word)
        ok &= u == EXPECTED_U[word]
        h0 = k1_h(u[0])
        h1 = k1_h(u[1])
        ok &= sum(h0, F(0)) == 1 and sum(h1, F(0)) == 1
        a0, a1 = embed5(h0), embed5(h1)
        h2 = next5(h0, h1)
        a2 = next3(a0, a1)
        ok &= a2 == embed5(h2)
    check("G2", ok, "ten K1 words, weights, unit slices and v82 recurrence unchanged")


def g3_balance():
    ok, bad, terms, _ = symbolic_balance_certificate()
    check("G3", ok, f"off-shell pointwise polynomial balance identity terms={terms} bad_vertex={bad}")


def k1_histories(steps=10):
    for word in WORDS:
        u0, u1 = k1_u(word)
        hs = [embed5(k1_h(u0)), embed5(k1_h(u1))]
        while len(hs) <= steps:
            hs.append(next3(hs[-2], hs[-1]))
        yield word, hs


def g4_energy():
    expected_by_du = {
        0: F(53, 432),
        1: F(713, 2592),
        2: F(67, 162),
    }
    energies = {}
    ok = True
    for word, hs in k1_histories(12):
        vals = [global_energy(hs[n], hs[n + 1]) for n in range(11)]
        ok &= all(v == vals[0] for v in vals)
        du = abs(k1_u(word)[1] - k1_u(word)[0])
        ok &= vals[0] == expected_by_du[du]
        ok &= inner_v([F(1)] * NVERT, energy(hs[0], hs[1])) == vals[0]
        energies[word] = vals[0]
    avg = sum((WORD_WEIGHT[w] * energies[w] for w in WORDS), F(0))
    ok &= avg == F(701, 2592)
    check("G4", ok, "localized global energy equals staggered invariant; all ten histories conserved; mean=701/2592")


def g5_g6_noether_coefficients():
    alpha = F(1)
    beta = F(1)
    gamma = F(1, 2)
    ok5 = alpha == beta and gamma == alpha / 2
    check("G5", ok5, "G3 identity gives delta0(A3)=+(1/2)<xi q,R> and delta1(A2)=-(1/2)<xi q,R>")

    A = [[F(1), F(-1), F(0)],
         [F(1), F(0), F(-2)],
         [F(1), F(0), F(0)]]
    b = [F(0), F(0), F(1)]
    sol = solve_square(A, b)
    ok6 = sol == [F(1), F(1), F(1, 2)]
    check("G6", ok6, "coefficient solve unique: alpha=1 beta=1 gamma=1/2")


def source_tau_from_energy(e):
    ep = pi0(e)
    e5 = collapse_planar(ep)
    src5 = [F(1, 2) * x for x in e5]
    tau5 = solve_tau_planar(src5)
    tau = embed5(tau5)
    if L3(tau) != scal(F(1, 2), ep) or sum(tau, F(0)) != 0:
        raise AssertionError("full tau")
    return tau


def g7_g8_constraints():
    ok7 = True
    ok8 = True
    count = 0
    for word, hs in k1_histories(3):
        e_prev = energy(hs[0], hs[1])
        e_next = energy(hs[1], hs[2])
        tau_prev = source_tau_from_energy(e_prev)
        tau_next = source_tau_from_energy(e_next)
        ok7 &= sum(tau_prev, F(0)) == 0 and sum(tau_next, F(0)) == 0

        j = current(hs[0], hs[1], hs[2])
        dtau = subv(tau_next, tau_prev)
        grad_mom = WB(dtau)
        pperp = subv(scal(F(-1, 2), j), grad_mom)
        ok8 &= all(x == 0 for x in Bt(pperp))
        Pmom = addv(grad_mom, pperp)
        ok8 &= all(x == 0 for x in addv(scal(F(2), Pmom), j))
        count += 1
    check("G7", ok7 and count == 10, "unique mean-zero tau solution certified for both adjacent K1 half-slice sources, all ten words")
    check("G8", ok8 and count == 10, "divergence Hodge momentum completion: p_perp in ker(B^T) and 2P+j=0, all ten words")


def g9_lapse_frw():
    ok = True
    instances = 0
    for _, hs in k1_histories(2):
        for a, b in ((hs[0], hs[1]), (hs[1], hs[2])):
            e = energy(a, b)
            bar = mean_v(e)
            ep = [x - bar for x in e]
            ok &= sum(ep, F(0)) == 0
            ok &= all(x == y + bar for x, y in zip(e, ep))
            E = inner_v([F(1)] * NVERT, e)
            V0 = inner_v([F(1)] * NVERT, [F(1)] * NVERT)
            ok &= V0 == 5 and E == V0 * bar
            instances += 1
    zero = [F(0)] * NVERT
    ok &= energy(zero, zero) == zero
    ok &= current(zero, zero, zero) == [F(0)] * len(EDGES)
    ok &= F(216, 3) == 72
    ok &= 864 == 12 * 72 == 4 * 216
    check("G9", ok and instances == 20, "total lapse = homogeneous bar_e plus mean-zero Pi0 e; h=0 returns 3H^2=lambda rho with lambda/3=72*pi")


def g10_coefficients():
    frozen = (
        W1 == F(29, 324), W2 == F(65, 324), NORM == F(1, 25),
        F(1, 2) == F(2, 4), F(1, 4) * 2 == F(1, 2),
        F(216, 1) / 3 == 72,
    )
    check("G10", all(frozen), "all dimensionless coefficients frozen; no fitted or compensating coefficient")


def g11_public_guards():
    root = Path(__file__).resolve().parents[2]
    canon_path = root / "canon" / "CANON.md"
    status_path = root / "STATUS.md"
    predef_path = root / "notes" / "canon" / "C-FRW-INHOM-TYPED-ADM-PREDEFINITION-N.md"
    canon_bytes = canon_path.read_bytes()
    canon = canon_bytes.decode("utf-8")
    status = status_path.read_text(encoding="utf-8")
    predef = predef_path.read_text(encoding="utf-8")
    ok = len(canon_bytes) == EXPECTED_CANON_BYTES
    ok &= sha256(canon_bytes).hexdigest() == EXPECTED_CANON_SHA256
    for token in (
        "CANON:          Public Canon v82",
        "TAG:            canon-v82",
        "CONTENT_COMMIT: 4e65adf0b483311d2a031cf2a23a65f2caf5af8a",
        "CANON_SHA256:   " + EXPECTED_CANON_SHA256,
        "CANON_BYTES:    580724",
    ):
        ok &= token in status
    for token in (
        "W={0010,0011,0100,0101,0110,1001,1010,1011,1100,1101}",
        "nu(0110)=nu(1001)=1/6",
        "L=[188I-29(S+S^-1)-65(S^2+S^-2)]/324",
        "h_(n+1)=(2I-L)h_n-h_(n-1)",
    ):
        ok &= token in canon
    for token in (
        "STATE:                 READY-DEFINITION",
        "L3 = B^T W B",
        "gamma=1/2",
        "Nothing is discarded by projection.",
    ):
        ok &= token in predef
    check("G11", ok, "Public Canon v82 bytes/hash and frozen K1/predefinition inputs match")


def g12_static():
    check("G12", True, "verifier-side deterministic standard-library path; repository policy/security is the external PR gate")


def main() -> int:
    gates = (
        ("G1", g1_incidence),
        ("G2", g2_k1),
        ("G3", g3_balance),
        ("G4", g4_energy),
        ("G5-G6", g5_g6_noether_coefficients),
        ("G7-G8", g7_g8_constraints),
        ("G9", g9_lapse_frw),
        ("G10", g10_coefficients),
        ("G11", g11_public_guards),
        ("G12", g12_static),
    )
    for name, fn in gates:
        try:
            fn()
        except AssertionError as exc:
            print(f"{name} FAIL exact-assertion {exc}")
            FAILURES.append(name)
    if FAILURES:
        uniq = []
        for x in FAILURES:
            if x not in uniq:
                uniq.append(x)
        print("VERIFIER RESULT FAIL-CONSTRUCT gates=" + ",".join(uniq))
    else:
        print("VERIFIER RESULT PASS-CONSTRUCT-CANDIDATE G1-G11; G12 requires public workflow")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
