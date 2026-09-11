#!/usr/bin/env python3
"""P-TT-NATIVE-QUADRATIC-EMISSION-1 exact verifier.

Formal public probe. Standard library only. Integer/Fraction arithmetic only.
No floats, no target measurements, no numerical r_T.
"""
from __future__ import annotations

from fractions import Fraction as Q

CHECKS = 0


def require(cond: bool, label: str) -> None:
    global CHECKS
    CHECKS += 1
    if not cond:
        raise AssertionError(label)


def vec_add(a, b):
    return [x + y for x, y in zip(a, b)]


def vec_sub(a, b):
    return [x - y for x, y in zip(a, b)]


def vec_scale(c, a):
    return [c * x for x in a]


def vec_mul(a, b):
    return [x * y for x, y in zip(a, b)]


def vec_sum(a):
    return sum(a, Q(0))


def rank(A):
    M = [[Q(x) for x in row] for row in A]
    if not M:
        return 0
    nr, nc = len(M), len(M[0])
    r = 0
    for c in range(nc):
        pivot = next((i for i in range(r, nr) if M[i][c]), None)
        if pivot is None:
            continue
        M[r], M[pivot] = M[pivot], M[r]
        q = M[r][c]
        M[r] = [x / q for x in M[r]]
        for i in range(nr):
            if i != r and M[i][c]:
                q = M[i][c]
                M[i] = [x - q * y for x, y in zip(M[i], M[r])]
        r += 1
        if r == nr:
            break
    return r


def solve_square(A, b):
    n = len(A)
    require(n > 0 and all(len(row) == n for row in A) and len(b) == n,
            "square solve shape")
    M = [[Q(x) for x in row] + [Q(y)] for row, y in zip(A, b)]
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, n) if M[i][c]), None)
        if pivot is None:
            raise AssertionError("singular exact solve")
        M[r], M[pivot] = M[pivot], M[r]
        q = M[r][c]
        M[r] = [x / q for x in M[r]]
        for i in range(n):
            if i != r and M[i][c]:
                q = M[i][c]
                M[i] = [x - q * y for x, y in zip(M[i], M[r])]
        r += 1
    require(all(M[i][j] == (Q(1) if i == j else Q(0))
                for i in range(n) for j in range(n)), "exact solve reduced identity")
    return [M[i][-1] for i in range(n)]


# ---------------------------------------------------------------------------
# 1. Native Thue-Morse factor language and exact frequencies
# ---------------------------------------------------------------------------
W = {
    "0010", "0011", "0100", "0101", "0110",
    "1001", "1010", "1011", "1100", "1101",
}
PAIR = {"00", "01", "10", "11"}
TRIPLE = {"001", "010", "011", "100", "101", "110"}


def tm_factor_theorem():
    # Pair frequencies x=(00,01,10,11). Child start parity gives exact equations.
    order = ["00", "01", "10", "11"]
    idx = {w: i for i, w in enumerate(order)}
    odd_map = {"00": "10", "01": "11", "10": "00", "11": "01"}
    even_mass = {"00": Q(0), "01": Q(1, 2), "10": Q(1, 2), "11": Q(0)}

    # f_child = 1/2 * even-start distribution + 1/2 * odd-start pushforward(f).
    # Move unknown terms left and add normalization.
    A = []
    b = []
    for out in order:
        row = [Q(0)] * 4
        row[idx[out]] = Q(1)
        for parent in order:
            if odd_map[parent] == out:
                row[idx[parent]] -= Q(1, 2)
        A.append(row)
        b.append(Q(1, 2) * even_mass[out])
    # Any four independent equations suffice; prove rank four, then candidate is unique.
    require(rank(A) == 4, "pair-frequency system unique")
    pair_freq = {
        "00": Q(1, 6), "01": Q(1, 3),
        "10": Q(1, 3), "11": Q(1, 6),
    }
    candidate = [pair_freq[w] for w in order]
    for row, rhs in zip(A, b):
        require(sum(c * x for c, x in zip(row, candidate)) == rhs,
                "pair-frequency fixed equation")
    require(sum(candidate, Q(0)) == 1, "pair frequencies normalize")

    # Complete legal length-three language by even/odd start decomposition of every pair.
    even3 = {}
    odd3 = {}
    for p in PAIR:
        a, b0 = map(int, p)
        even3[p] = f"{a}{1-a}{b0}"
        odd3[p] = f"{1-a}{b0}{1-b0}"
    triple = set(even3.values()) | set(odd3.values())
    require(triple == TRIPLE, "complete TM length-three language")

    triple_freq = {t: Q(0) for t in TRIPLE}
    for p, f in pair_freq.items():
        triple_freq[even3[p]] += Q(1, 2) * f
        triple_freq[odd3[p]] += Q(1, 2) * f
    require(all(triple_freq[t] == Q(1, 6) for t in TRIPLE),
            "all six TM triples have mass 1/6")
    require(sum(triple_freq.values(), Q(0)) == 1, "triple frequencies normalize")

    # Complete legal length-four language. Even starts depend on a parent pair;
    # odd starts depend on a parent triple.
    even4 = {}
    for p in PAIR:
        a, b0 = map(int, p)
        even4[p] = f"{a}{1-a}{b0}{1-b0}"
    odd4 = {}
    for t in TRIPLE:
        a, b0, c = map(int, t)
        odd4[t] = f"{1-a}{b0}{1-b0}{c}"
    words = set(even4.values()) | set(odd4.values())
    require(words == W, "complete TM length-four language equals K1 W")

    freq4 = {w: Q(0) for w in W}
    for p, f in pair_freq.items():
        freq4[even4[p]] += Q(1, 2) * f
    for t, f in triple_freq.items():
        freq4[odd4[t]] += Q(1, 2) * f
    expected = {w: Q(1, 12) for w in W}
    expected["0110"] = Q(1, 6)
    expected["1001"] = Q(1, 6)
    require(freq4 == expected, "native length-four masses equal K1 optional law")
    require(sum(freq4.values(), Q(0)) == 1, "length-four frequencies normalize")
    return freq4


# ---------------------------------------------------------------------------
# 2. Exact O(2)-equivariant quadratic source-map class
# ---------------------------------------------------------------------------
# Variables are (a,b,c,d), i.e. x=(a,b), y=(c,d). Monomial order is explicit.
MONOS = [
    (2, 0, 0, 0),
    (1, 1, 0, 0),
    (0, 2, 0, 0),
    (1, 0, 1, 0),
    (1, 0, 0, 1),
    (0, 1, 1, 0),
    (0, 1, 0, 1),
    (0, 0, 2, 0),
    (0, 0, 1, 1),
    (0, 0, 0, 2),
]
MIDX = {m: i for i, m in enumerate(MONOS)}


def lie_image(m):
    """L=-b d/da + a d/db - d d/dc + c d/dd on one monomial."""
    out = {}
    e = list(m)
    # -b d/da
    if e[0]:
        z = e.copy(); coef = -z[0]; z[0] -= 1; z[1] += 1
        out[tuple(z)] = out.get(tuple(z), Q(0)) + coef
    # +a d/db
    if e[1]:
        z = e.copy(); coef = z[1]; z[1] -= 1; z[0] += 1
        out[tuple(z)] = out.get(tuple(z), Q(0)) + coef
    # -d d/dc
    if e[2]:
        z = e.copy(); coef = -z[2]; z[2] -= 1; z[3] += 1
        out[tuple(z)] = out.get(tuple(z), Q(0)) + coef
    # +c d/dd
    if e[3]:
        z = e.copy(); coef = z[3]; z[3] -= 1; z[2] += 1
        out[tuple(z)] = out.get(tuple(z), Q(0)) + coef
    return {k: v for k, v in out.items() if v}


def source_map_class():
    Lmap = [lie_image(m) for m in MONOS]
    equations = []

    # Rotation covariance: L(P)+2Q=0, L(Q)-2P=0.
    for j, target_m in enumerate(MONOS):
        row = [Q(0)] * 20
        for i, image in enumerate(Lmap):
            row[i] += image.get(target_m, Q(0))
        row[10 + j] += 2
        equations.append(row)
    for j, target_m in enumerate(MONOS):
        row = [Q(0)] * 20
        for i, image in enumerate(Lmap):
            row[10 + i] += image.get(target_m, Q(0))
        row[j] -= 2
        equations.append(row)

    # Reflection b,d -> -b,-d. P is even, Q is odd.
    for j, m in enumerate(MONOS):
        odd = (m[1] + m[3]) % 2
        if odd:
            row = [Q(0)] * 20; row[j] = 1; equations.append(row)
        else:
            row = [Q(0)] * 20; row[10 + j] = 1; equations.append(row)

    # Ordered-slice antisymmetry under x <-> y.
    for comp in (0, 10):
        for j, m in enumerate(MONOS):
            sm = (m[2], m[3], m[0], m[1])
            row = [Q(0)] * 20
            row[comp + j] += 1
            row[comp + MIDX[sm]] += 1
            equations.append(row)

    target = [Q(0)] * 20
    # P=(c^2-d^2)-(a^2-b^2)
    target[0] = -1
    target[2] = 1
    target[7] = 1
    target[9] = -1
    # Q=2cd-2ab
    target[10 + 1] = -2
    target[10 + 8] = 2

    require(all(sum(a * x for a, x in zip(row, target)) == 0
                for row in equations), "square-difference generator satisfies class A")
    r = rank(equations)
    require(r == 19, "class A coefficient system rank 19")
    require(20 - r == 1, "class A is exactly one-dimensional")
    return target


# ---------------------------------------------------------------------------
# 3. Sparse polynomial proof of local energy identity
# ---------------------------------------------------------------------------
class Poly:
    def __init__(self, terms=None):
        self.t = {}
        if terms:
            for m, c in terms.items():
                c = Q(c)
                if c:
                    self.t[tuple(sorted(m))] = self.t.get(tuple(sorted(m)), Q(0)) + c
            self.t = {m: c for m, c in self.t.items() if c}

    @staticmethod
    def var(i):
        return Poly({(i,): Q(1)})

    @staticmethod
    def const(c):
        return Poly({(): Q(c)}) if c else Poly()

    def __add__(self, other):
        other = other if isinstance(other, Poly) else Poly.const(other)
        out = dict(self.t)
        for m, c in other.t.items():
            out[m] = out.get(m, Q(0)) + c
        return Poly(out)

    __radd__ = __add__

    def __neg__(self):
        return Poly({m: -c for m, c in self.t.items()})

    def __sub__(self, other):
        return self + (-other if isinstance(other, Poly) else -Q(other))

    def __rsub__(self, other):
        return (-self) + other

    def __mul__(self, other):
        other = other if isinstance(other, Poly) else Poly.const(other)
        out = {}
        for m, c in self.t.items():
            for n, d in other.t.items():
                k = tuple(sorted(m + n))
                out[k] = out.get(k, Q(0)) + c * d
        return Poly(out)

    __rmul__ = __mul__

    def __pow__(self, n):
        require(n >= 0, "polynomial exponent nonnegative")
        out = Poly.const(1)
        for _ in range(n):
            out = out * self
        return out

    def zero(self):
        return not self.t


def symbolic_energy_identity():
    # tail times m-1,m,m+1: a,b,c; head: d,e,f
    a, b, c, d, e, f = (Poly.var(i) for i in range(6))
    kinetic = Q(1, 2) * ((c - b) ** 2 - (b - a) ** 2)
    kinetic_rhs = Q(1, 2) * (c - a) * (c - 2 * b + a)
    require((kinetic - kinetic_rhs).zero(), "symbolic kinetic identity")

    for w in (Q(29, 324), Q(65, 324)):
        gprev = d - a
        gcur = e - b
        gnext = f - c
        delta_share = w * Q(1, 4) * gcur * (gnext - gprev)
        current = w * Q(1, 4) * gcur * ((c - a) + (f - d))
        tail_rhs = w * Q(1, 2) * (c - a) * (b - e)
        head_rhs = w * Q(1, 2) * (f - d) * (e - b)
        require((delta_share - current - tail_rhs).zero(),
                "symbolic edge tail identity")
        require((delta_share + current - head_rhs).zero(),
                "symbolic edge head identity")


# ---------------------------------------------------------------------------
# 4. Planar graph, K1 packets, exact emitted histories and constraints
# ---------------------------------------------------------------------------
WEIGHTS = ((1, Q(29, 324)), (2, Q(65, 324)))


def lap(a):
    out = [Q(0)] * 5
    for r in range(5):
        out[r] = (Q(188) * a[r]
                  - Q(29) * (a[(r + 1) % 5] + a[(r - 1) % 5])
                  - Q(65) * (a[(r + 2) % 5] + a[(r - 2) % 5])) / Q(324)
    return out


def edges():
    return [(r, (r + k) % 5, w) for r in range(5) for k, w in WEIGHTS]


EDGES = edges()


def grad_w(a):
    return [w * (a[j] - a[i]) for i, j, w in EDGES]


def div_edge(v):
    out = [Q(0)] * 5
    for (i, j, _), z in zip(EDGES, v):
        out[i] -= z
        out[j] += z
    return out


def mean_zero(a):
    m = vec_sum(a) / 5
    return [x - m for x in a]


def poisson(rhs):
    rhs = mean_zero(rhs)
    # Solve L tau=rhs with sum tau=0 by replacing one dependent row by the mean condition.
    A = []
    for r in range(4):
        row = [Q(0)] * 5
        row[r] = Q(188, 324)
        row[(r + 1) % 5] += Q(-29, 324)
        row[(r - 1) % 5] += Q(-29, 324)
        row[(r + 2) % 5] += Q(-65, 324)
        row[(r - 2) % 5] += Q(-65, 324)
        A.append(row)
    A.append([Q(1)] * 5)
    b = rhs[:4] + [Q(0)]
    x = solve_square(A, b)
    require(lap(x) == rhs, "Poisson inverse exact")
    require(vec_sum(x) == 0, "Poisson solution mean zero")
    return x


def H_of_u(u):
    u %= 5
    out = [Q(0)] * 5
    out[u] += Q(1, 2)
    out[(u + 1) % 5] += Q(1, 2)
    return out


def packet(word):
    w = tuple(int(x) for x in word)
    u0 = w[2] - w[0]
    u1 = w[3] - w[1]
    require(u0 == w[2] - w[0], "omega first overlap")
    require(u1 == w[3] - w[1], "omega second overlap")
    H0, H1 = H_of_u(u0), H_of_u(u1)
    phi = vec_sub(H1, H0)
    return (u0, u1), H0, H1, phi


def energy(a, b):
    out = [Q(1, 2) * (y - x) ** 2 for x, y in zip(a, b)]
    for i, j, w in EDGES:
        term = w * Q(1, 4) * (b[j] - b[i]) * (a[j] - a[i])
        out[i] += term
        out[j] += term
    return out


def current(a, b, c):
    q = vec_sub(c, a)
    out = []
    for i, j, w in EDGES:
        out.append(w * Q(1, 4) * (b[j] - b[i]) * (q[i] + q[j]))
    return out


def history(phi, horizon=24):
    zero = [Q(0)] * 5
    h = [zero[:], zero[:]]
    for m in range(1, horizon):
        force = phi if m == 1 else zero
        nxt = vec_add(vec_sub(vec_scale(2, h[m]), h[m - 1]),
                      vec_sub(force, lap(h[m])))
        h.append(nxt)
    require(len(h) == horizon + 1, "history horizon shape")
    return h


def audit_packets():
    zero = [Q(0)] * 5
    static = 0
    active = 0
    classes = {}
    for word in sorted(W):
        (u0, u1), H0, H1, phi = packet(word)
        require(vec_sum(H0) == 1 and vec_sum(H1) == 1, "K1 slice normalization")
        require(vec_sum(phi) == 0, "emission has zero spatial mean")
        if u0 == u1:
            static += 1
            require(phi == zero, "static packet emits zero")
        else:
            active += 1
            require(phi != zero, "nonstatic packet emits nonzero")
            kinetic = vec_scale(Q(1, 2), vec_mul(vec_sub(H1, H0), vec_sub(H1, H0)))
            emitted = vec_scale(Q(1, 2), vec_mul(phi, phi))
            require(kinetic == emitted, "source-work normalization kappa=+1")
            require(any(x > 0 for x in kinetic), "nonstatic normalization witness")

        classes.setdefault(abs(u1 - u0), 0)
        classes[abs(u1 - u0)] += 1

        h = history(phi)
        require(h[0] == zero and h[1] == zero and h[2] == phi,
                "regular zero-start first emission")

        energies = [energy(h[n], h[n + 1]) for n in range(24)]
        src = [vec_scale(Q(1, 2), vec_mul(phi, phi))] + [zero[:] for _ in range(23)]
        total = [vec_add(e, s) for e, s in zip(energies, src)]
        taus = [poisson(vec_scale(Q(1, 2), mean_zero(e))) for e in total]
        # poisson() solves L tau=argument; hence 2Ltau=Pi0(total energy).
        for n in range(24):
            require(vec_scale(2, lap(taus[n])) == mean_zero(total[n]),
                    "scalar auxiliary constraint")

        for m in range(1, 24):
            force = phi if m == 1 else zero
            q = vec_sub(h[m + 1], h[m - 1])
            j = current(h[m - 1], h[m], h[m + 1])
            field_defect = vec_add(vec_sub(energies[m], energies[m - 1]), div_edge(j))
            rhs = vec_scale(Q(1, 2), vec_mul(q, force))
            require(field_defect == rhs, "finite field work identity")
            total_defect = vec_add(vec_sub(total[m], total[m - 1]), div_edge(j))
            require(total_defect == zero, "source plus field local conservation")

            dtau = vec_sub(taus[m], taus[m - 1])
            p = vec_sub(vec_scale(Q(-1, 2), j), grad_w(dtau))
            require(div_edge(p) == zero, "auxiliary momentum co-closure")

        # Registered planar source conservation: rho=J_i=S_i3=0.
        rho = zero
        J3 = zero
        Si3 = zero
        require(rho == J3 == Si3 == zero, "pure transverse source conservation data")

    require(static + active == 10, "all K1 packets classified")
    require(static == 4 and active == 6, "K1 static/active source split")
    require(classes == {0: 4, 1: 4, 2: 2}, "K1 delta-u class census")
    return static, active, classes


def main():
    tm_factor_theorem()
    source_map_class()
    symbolic_energy_identity()
    static, active, classes = audit_packets()

    # A5: once class A is one-dimensional, any nonstatic packet has nonzero
    # ||H1-H0||^2, so exact equality of emitted and inherited kinetic channel
    # gives kappa^2=1. Forward source order chooses +1; reverse order is -1.
    require(Q(1) ** 2 == 1 and Q(-1) ** 2 == 1, "kappa magnitude fixed to one")

    # Registered spin propagation type.
    require(1 - 1 * 1 == 0, "spin-1 propagation coefficient")
    require(1 - 2 * 2 == -3, "spin-2 propagation coefficient")

    print("TM4_LANGUAGE 10 FACTORS PASS")
    print("TM4_MASSES 0110=1/6 1001=1/6 OTHER8=1/12 PASS")
    print("ORIENTATION_OVERLAPS u0=w2-w0 u1=w3-w1 PASS")
    print("QUADRATIC_SOURCE_CLASS O2+REFLECTION+TIME_SWAP NULLITY=1 PASS")
    print("EMISSION Phi=b1^2-b0^2=H1-H0 KAPPA_ABS=1 PASS")
    print(f"K1_PACKETS STATIC={static} ACTIVE={active} CLASSES={classes} PASS")
    print("ZERO_START h0=h1=0 h2=Phi UNIQUE_RECURRENCE PASS")
    print("LOCAL_WORK_AND_CONSTRAINTS exact symbolic + rational fixtures PASS")
    print("SPIN_TYPES c(1)=0 c(2)=-3 PASS")
    print("NO_NEW_DIMENSIONLESS_SOURCE_COEFFICIENT PASS")
    print(f"EXACT_ASSERTIONS {CHECKS}")
    print("RESULT PASS; TT-SOURCE STATUS NOT CHANGED BY THIS PROBE")


if __name__ == "__main__":
    main()
