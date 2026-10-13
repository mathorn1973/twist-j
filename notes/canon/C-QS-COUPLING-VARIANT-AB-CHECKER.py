#!/usr/bin/env python3
"""
Selected Exact-Arithmetic Checks for C-QS-COUPLING-VARIANT-AB-DIAGNOSTIC-N.

Coverage markers below delimit the assertions actually executed:
- History automaton comparisons: all 24 couplings, B1/B2, N=2..9;
  separate N=1 normalization and N=3 interference witnesses.
- Symbolic initial-value and forward-difference identities: two scalar sums
  for all N>=1, not an all-N verification of the full automaton.
- Paired-vertex and opposite-branch evolution comparisons: N=2..6.
- Finite orbit, return-matrix, Fourier-determinant, and supplied first-jet
  coefficient checks; no derivation of physical A6 or AlphaMap.
- H-metric projection arithmetic on supplied vectors and scalar rate formulas;
  no full H-modified stream or projector-property verification.
- Rational consequences of the imported WALL-CIRCLE-LEMMA formulas, plus
  Galois index and J scalar-product identities; no analytic wall proof or
  J-dressed stream verification.

The companion note also contains imported Canon premises and prose derivations
outside this checker. Passing these assertions does not verify every claim in
the note or authorize a scientific status change.

Status: NON-CANONICAL / STOP-PREDEFINITION
Arithmetic: Exact Fraction over Q(i) and Q(zeta_5) only. Zero floats.
All checks use hard assertions.
"""

from fractions import Fraction
import sys

# ============================================================================
# 1. Exact Gaussian Rational Arithmetic Q(i)
# ============================================================================
class Qi:
    __slots__ = ("re", "im")
    def __init__(self, re=0, im=0):
        self.re = Fraction(re)
        self.im = Fraction(im)
    def __add__(self, o):
        o = o if isinstance(o, Qi) else Qi(o)
        return Qi(self.re + o.re, self.im + o.im)
    def __sub__(self, o):
        o = o if isinstance(o, Qi) else Qi(o)
        return Qi(self.re - o.re, self.im - o.im)
    def __mul__(self, o):
        o = o if isinstance(o, Qi) else Qi(o)
        return Qi(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)
    def __truediv__(self, o):
        o = o if isinstance(o, Qi) else Qi(o)
        d = o.re * o.re + o.im * o.im
        if d == 0:
            raise ZeroDivisionError("Division by zero in Qi")
        return Qi((self.re * o.re + self.im * o.im) / d, (self.im * o.re - self.re * o.im) / d)
    def __neg__(self):
        return Qi(-self.re, -self.im)
    def conj(self):
        return Qi(self.re, -self.im)
    def norm_sq(self):
        return self.re * self.re + self.im * self.im
    def __eq__(self, o):
        o = o if isinstance(o, Qi) else Qi(o)
        return self.re == o.re and self.im == o.im
    def __repr__(self):
        if self.im == 0:
            return f"{self.re}"
        return f"({self.re} + ({self.im})i)"

ZERO = Qi(0, 0)
ONE = Qi(1, 0)
LAM_P = Qi(1, 2)   # 1 + 2i
LAM_M = Qi(1, -2)  # 1 - 2i
Q_RATIO = LAM_M / LAM_P  # (1 - 2i)/(1 + 2i) = -3/5 - 4/5 i

assert LAM_P.norm_sq() == Fraction(5)
assert LAM_M.norm_sq() == Fraction(5)
assert Q_RATIO == Qi(Fraction(-3, 5), Fraction(-4, 5))
assert Q_RATIO.norm_sq() == Fraction(1)
assert Q_RATIO / (ONE - Q_RATIO) == Qi(Fraction(-1, 2), Fraction(-1, 4))
assert (Q_RATIO / (ONE - Q_RATIO)).norm_sq() == Fraction(5, 16)

# ============================================================================
# 2. Exact 10x10 Operators on M = M_D tensor R_5 in frozen basis {f_sigma tensor e_j}
# ============================================================================
def idx(sigma, j):
    return 5 * sigma + (j % 5)

def mat_zero(n=10):
    return [[ZERO for _ in range(n)] for _ in range(n)]

def mat_add(A, B):
    n = len(A)
    return [[A[r][c] + B[r][c] for c in range(n)] for r in range(n)]

def mat_sub(A, B):
    n = len(A)
    return [[A[r][c] - B[r][c] for c in range(n)] for r in range(n)]

def mat_scale(s, A):
    s = s if isinstance(s, Qi) else Qi(s)
    n = len(A)
    return [[s * A[r][c] for c in range(n)] for r in range(n)]

def mat_mul(A, B):
    n = len(A)
    C = mat_zero(n)
    for r in range(n):
        for k in range(n):
            if A[r][k] == ZERO:
                continue
            ark = A[r][k]
            for c in range(n):
                if B[k][c] != ZERO:
                    C[r][c] = C[r][c] + ark * B[k][c]
    return C

def mat_vec(A, v):
    n = len(A)
    out = [ZERO for _ in range(n)]
    for r in range(n):
        s = ZERO
        for c in range(n):
            if A[r][c] != ZERO and v[c] != ZERO:
                s = s + A[r][c] * v[c]
        out[r] = s
    return out

def vec_add(u, v):
    return [u[k] + v[k] for k in range(len(u))]

def vec_inner(u, v):
    return sum((u[k].conj() * v[k] for k in range(len(u))), ZERO)

def vec_norm_sq(u):
    return sum((u[k].norm_sq() for k in range(len(u))), Fraction(0))

D_REST = mat_zero(10)
Z_OP = mat_zero(10)
PI_E0 = mat_zero(10)
PI_NEQ0 = mat_zero(10)

for j in range(5):
    D_REST[idx(0, j)][idx(0, j)] = ONE
    D_REST[idx(1, j)][idx(1, j)] = ONE
    D_REST[idx(0, j)][idx(1, j)] = Qi(0, 2)
    D_REST[idx(1, j)][idx(0, j)] = Qi(0, 2)
    Z_OP[idx(0, j)][idx(0, j)] = ONE
    Z_OP[idx(1, j)][idx(1, j)] = -ONE
    if j == 0:
        PI_E0[idx(0, 0)][idx(0, 0)] = ONE
        PI_E0[idx(1, 0)][idx(1, 0)] = ONE
    else:
        PI_NEQ0[idx(0, j)][idx(0, j)] = ONE
        PI_NEQ0[idx(1, j)][idx(1, j)] = ONE

def E_op(k):
    M = mat_zero(10)
    for s in (0, 1):
        for j in range(5):
            M[idx(s, j + k)][idx(s, j)] = ONE
    return M

def V_flip_op(a, b):
    """V_{a,b} = Z tensor (E_a - E_b)/2."""
    diff_E = mat_scale(Fraction(1, 2), mat_sub(E_op(a), E_op(b)))
    return mat_mul(Z_OP, diff_E)

# Pre-state u_0 = v_+ tensor e_0 = (f_0 + f_1) tensor e_0 in M_pre ~= M
U0_VEC = [ZERO for _ in range(10)]
U0_VEC[idx(0, 0)] = ONE
U0_VEC[idx(1, 0)] = ONE
assert vec_norm_sq(U0_VEC) == Fraction(2)

# Explicit canonical block identification tau_{post -> pre}: M_post -> M_pre
# Both M_pre and M_post are typed copies of M = M_D tensor R_5 ~= Q(i)^10 with frozen basis {f_sigma tensor e_j};
# tau_{post -> pre} is the basis-preserving Q(i)-linear isomorphism f_sigma^{(post)} tensor e_j -> f_sigma^{(pre)} tensor e_j.
def tau_post_to_pre(v_post):
    assert len(v_post) == 10
    return list(v_post)

# ============================================================================
# 3. Emission-Indexed History Automaton Producing h_N in H_N = (+)_{i=1}^{N-1} M_post
# ============================================================================
def run_history_automaton(a, b, mode, N):
    """
    Evolves the emission-indexed excursion automaton for N ticks from (u_0, (), ()):
      - psi_pre(n) in M_pre: evolves via D_e0 = (D_rest tensor 1) Pi_{e0}
      - At each tick n >= 1, emission from psi_pre(n-1) via Emit = Pi_{!=0} (D_rest tensor 1) V_{a,b}
        creates a new active excursion slot i = n in M_{exc, i}, while existing active slots i < n
        are reabsorbed into M_{post, i} via Reabs = Pi_{e0} (D_rest tensor 1) V_{a,b}
        and updated in M_{exc, i} via Mid (0 for B1, Pi_{!=0}(D_rest tensor 1)Pi_{!=0} for B2).
      - Completed slots in M_{post, i} evolve at subsequent ticks via D_e0.
    Returns:
      psi_pre(N) in M_pre,
      psi_exc_list(N) = [psi_{exc, 1}(N), ..., psi_{exc, N}(N)],
      h_N = [Psi_{1, 1}(N), ..., Psi_{1, N-1}(N)] in H_N = (+)_{i=1}^{N-1} M_post.
    """
    D_e0 = mat_mul(D_REST, PI_E0)
    V = V_flip_op(a, b)
    Emit = mat_mul(PI_NEQ0, mat_mul(D_REST, V))
    Reabs = mat_mul(PI_E0, mat_mul(D_REST, V))
    Mid = mat_zero(10) if mode == "B1" else mat_mul(PI_NEQ0, mat_mul(D_REST, PI_NEQ0))

    psi_pre = list(U0_VEC)
    exc_slots = []   # active excursion states indexed by emission tick i = 1..n
    post_slots = []  # completed excursion states in M_{post, i} indexed by i = 1..n-1

    for tick in range(1, N + 1):
        # 1. Existing post_slots (i = 1..tick-2) step with D_e0, plus reabsorption from exc_slots[i-1]:
        new_post_slots = []
        for idx_i in range(len(post_slots)):
            stepped_post = mat_vec(D_e0, post_slots[idx_i])
            reabs_from_exc = mat_vec(Reabs, exc_slots[idx_i])
            new_post_slots.append(vec_add(stepped_post, reabs_from_exc))
        # The slot emitted at tick - 1 has its first reabsorption opportunity at current tick:
        if len(exc_slots) == tick - 1 and tick >= 2:
            new_post_slots.append(mat_vec(Reabs, exc_slots[tick - 2]))

        # 2. Existing exc_slots step with Mid, and a new exc_slot is emitted at i = tick from psi_pre:
        new_exc_slots = [mat_vec(Mid, v_exc) for v_exc in exc_slots]
        new_exc_slots.append(mat_vec(Emit, psi_pre))

        # 3. psi_pre steps with D_e0:
        psi_pre = mat_vec(D_e0, psi_pre)

        exc_slots = new_exc_slots
        post_slots = new_post_slots

    assert len(post_slots) == max(0, N - 1)
    return psi_pre, exc_slots, post_slots

def S_N_map(h_N):
    """Coherent history summation S_N : H_N -> M_pre."""
    acc = [ZERO for _ in range(10)]
    for psi_1_i in h_N:
        acc = vec_add(acc, tau_post_to_pre(psi_1_i))
    return acc

def B_N_map(h_N, N):
    """Emission-resolved reference-normalized quadratic weight B_N : H_N -> Q."""
    denom = (Fraction(5) ** N) * vec_norm_sq(U0_VEC)
    num = sum((vec_norm_sq(psi_1_i) for psi_1_i in h_N), Fraction(0))
    return num / denom

def W_coh_map(h_N, N):
    """Coherent total post-state reference-normalized quadratic weight ||S_N(h_N)||^2 / (5^N ||u_0||^2)."""
    denom = (Fraction(5) ** N) * vec_norm_sq(U0_VEC)
    return vec_norm_sq(S_N_map(h_N)) / denom

# ============================================================================
# 4. Finite History-Automaton Comparisons and Named Witnesses
# COVERAGE-HISTORY-FINITE
# All 24 couplings and both modes at N=2..9 are compared with scalar formulas.
# N=1 normalization and the antipodal B2 N=3 interference witness are separate.
# No independent unindexed 30x30 matrix is constructed in this section.
# ============================================================================
I_nt = [(a, b) for a in range(5) for b in range(5) if (a, b) != (0, 0)]

print("=== 1. HISTORY AUTOMATON: ALL 24 COUPLINGS, B1/B2, N=2..9 AND NAMED WITNESSES ===")
for mode in ("B1", "B2"):
    for (a, b) in I_nt:
        V = V_flip_op(a, b)
        mid_v = mat_vec(PI_NEQ0, mat_vec(V, U0_VEC))
        ret_v = mat_vec(PI_E0, mat_vec(V, mid_v))
        sb_qi = vec_inner(U0_VEC, ret_v) / Qi(2, 0)
        assert sb_qi.im == 0
        sb = sb_qi.re
        sh = vec_norm_sq(mid_v) / vec_norm_sq(U0_VEC)

        # Check N=1 reference normalization vs total 3-block norm:
        psi0_1, exc_1, h_1 = run_history_automaton(a, b, mode, 1)
        assert len(h_1) == 0
        tot_norm_1 = (vec_norm_sq(psi0_1) + sum(vec_norm_sq(x) for x in exc_1)) / (Fraction(5) * vec_norm_sq(U0_VEC))
        assert tot_norm_1 == Fraction(1) + sh
        if (a + b) % 5 == 0 and a != 0:
            assert tot_norm_1 == Fraction(3, 2)

        for N in range(2, 10):
            psi0_N, exc_N, h_N = run_history_automaton(a, b, mode, N)
            psi1_tot = S_N_map(h_N)

            # Relative amplitude A_N from S_N(h_N):
            A_N = vec_inner(psi0_N, psi1_tot) / Qi(vec_norm_sq(psi0_N), 0)
            B_N = B_N_map(h_N, N)
            W_coh = W_coh_map(h_N, N)

            if mode == "B1":
                expected_A_N = Qi(N - 1, 0) * Qi(sb, 0) * Q_RATIO
                expected_B_N = Fraction(N - 1) * (sb * sb)
            else:
                q_sum = ZERO
                q_pow = ONE
                for L in range(1, N):
                    q_pow = q_pow * Q_RATIO
                    q_sum = q_sum + Qi(N - L, 0) * q_pow
                expected_A_N = Qi(sb, 0) * q_sum

                # Closed-form identity for B_N(h_N):
                q_pow_Nm1 = ONE
                for _ in range(N - 1):
                    q_pow_Nm1 = q_pow_Nm1 * Q_RATIO
                q_geom = Q_RATIO * (ONE - q_pow_Nm1) / (ONE - Q_RATIO)
                expected_B_N = Fraction(5, 16) * (sb * sb) * (Fraction(2 * (N - 1)) - Fraction(2) * q_geom.re)

            assert A_N == expected_A_N, f"Mismatch in A_N for {(a,b)} mode={mode} N={N}"
            assert B_N == expected_B_N, f"Mismatch in B_N for {(a,b)} mode={mode} N={N}"
            assert W_coh == A_N.norm_sq(), f"Mismatch in W_coh for {(a,b)} mode={mode} N={N}"

            # Check explicit N=3 witness on antipodal orbit in B2:
            if mode == "B2" and (a + b) % 5 == 0 and a != 0 and N == 3:
                assert W_coh == Fraction(13, 20)
                assert B_N == Fraction(9, 20)
                assert W_coh != B_N

print("  [PASS] History comparisons hold for all 24 couplings in B1/B2 at N=2..9; N=1 normalization and antipodal B2 N=3 witness (13/20 != 9/20) hold.")

# ============================================================================
# 5. Symbolic All-N Proof of Two Scalar Telescoping Identities
# COVERAGE-SCALAR-SUMS-ALL-N
# F(N) represents sum_{L=1}^{N-1} (N-L)*q^L; its increment is
# q*(1-q^N)/(1-q). G(N) represents sum_{M=1}^{N-1}
# |q*(1-q^M)/(1-q)|^2; its increment is (5/16)*(2-q^N-conj(q)^N).
# The exact initial values and coefficientwise forward differences prove these
# scalar identities for every N>=1. The all-N reduction of the automaton to
# these sums and the subsequent limiting arguments are prose derivations.
# ============================================================================
class SymSeq:
    """Exact sequence f(N) = c0 + c1*N + cq * q^N + cqb * conj(q)^N over Q(i)."""
    __slots__ = ("c0", "c1", "cq", "cqb")
    def __init__(self, c0=ZERO, c1=ZERO, cq=ZERO, cqb=ZERO):
        self.c0 = c0 if isinstance(c0, Qi) else Qi(c0)
        self.c1 = c1 if isinstance(c1, Qi) else Qi(c1)
        self.cq = cq if isinstance(cq, Qi) else Qi(cq)
        self.cqb = cqb if isinstance(cqb, Qi) else Qi(cqb)

    def eval_at(self, N):
        qN = ONE
        qbN = ONE
        q_conj = Q_RATIO.conj()
        for _ in range(N):
            qN = qN * Q_RATIO
            qbN = qbN * q_conj
        return self.c0 + Qi(N, 0) * self.c1 + self.cq * qN + self.cqb * qbN

    def shift_plus_one(self):
        """Returns f(N+1) in the canonical basis {1, N, q^N, conj(q)^N}."""
        return SymSeq(
            c0=self.c0 + self.c1,
            c1=self.c1,
            cq=self.cq * Q_RATIO,
            cqb=self.cqb * Q_RATIO.conj(),
        )

    def __sub__(self, o):
        return SymSeq(self.c0 - o.c0, self.c1 - o.c1, self.cq - o.cq, self.cqb - o.cqb)

    def __eq__(self, o):
        return (self.c0 == o.c0 and self.c1 == o.c1
                and self.cq == o.cq and self.cqb == o.cqb)

print("\n=== 2. SYMBOLIC INITIAL VALUES AND DIFFERENCES FOR TWO SCALAR SUMS, ALL N >= 1 ===")
r_q = Q_RATIO / (ONE - Q_RATIO)            # -1/2 - 1/4 i
r_q2 = Q_RATIO / ((ONE - Q_RATIO) * (ONE - Q_RATIO))  # -q / (1-q)^2 = 5/16

F_sym = SymSeq(c0=-r_q2, c1=r_q, cq=r_q2, cqb=ZERO)
assert F_sym.eval_at(1) == ZERO
diff_F = F_sym.shift_plus_one() - F_sym
expected_step_F = SymSeq(c0=r_q, c1=ZERO, cq=-r_q, cqb=ZERO)
assert diff_F == expected_step_F

c_5_16 = Qi(Fraction(5, 16), 0)
inv_1_minus_q = ONE + r_q
G_sym = SymSeq(
    c0=c_5_16 * (Qi(-2, 0) - inv_1_minus_q * Q_RATIO - (inv_1_minus_q * Q_RATIO).conj()),
    c1=c_5_16 * Qi(2, 0),
    cq=c_5_16 * inv_1_minus_q,
    cqb=c_5_16 * inv_1_minus_q.conj(),
)
assert G_sym.eval_at(1) == ZERO
diff_G = G_sym.shift_plus_one() - G_sym
expected_step_G = SymSeq(
    c0=c_5_16 * Qi(2, 0),
    c1=ZERO,
    cq=-c_5_16,
    cqb=-c_5_16,
)
assert diff_G == expected_step_G
assert G_sym.c1 == Qi(Fraction(5, 8), 0)
print("  [PASS] Exact initial values and forward differences prove the two scalar sum identities F(N) and G(N) for all integers N>=1.")

# ============================================================================
# 6. Exact Orbit Classification and Conditional Ratios Over I_nt
# COVERAGE-ORBIT-CLASSIFICATION
# The finite partition and ratios use the scalar rate formulas stated above.
# ============================================================================
print("\n=== 3. EXACT ORBIT CLASSIFICATION AND CONDITIONAL RATIOS ON ANTIPODAL ORBIT ===")
rho_B1_unit = Q_RATIO                             # -3/5 - 4/5 i
rho_B2_unit = Q_RATIO / (ONE - Q_RATIO)           # -1/2 - 1/4 i

orbit_defs = [
    ("O_{u,0}",    [(u, 0) for u in range(1, 5)]),
    ("O_{0,u}",    [(0, u) for u in range(1, 5)]),
    ("O_{u,u}",    [(u, u) for u in range(1, 5)]),
    ("O_{u,2u}",   [(u, (2 * u) % 5) for u in range(1, 5)]),
    ("O_{u,3u}",   [(u, (3 * u) % 5) for u in range(1, 5)]),
    ("O_{u,-u}",   [(u, (4 * u) % 5) for u in range(1, 5)]),
]

seen_pairs = set()
print(f"{'Orbit':<10} | {'size':<4} | {'s_bilin':<8} | {'s_herm':<8} | {'B1: (x, c_w, 5x/c_w)':<26} | {'B2: (x, c_w, 5x/c_w)':<26}")
print("-" * 96)

for orb_name, pairs in orbit_defs:
    assert len(pairs) == 4
    sb_set = set()
    sh_set = set()
    for (a, b) in pairs:
        seen_pairs.add((a, b))
        V = V_flip_op(a, b)
        mid_v = mat_vec(PI_NEQ0, mat_vec(V, U0_VEC))
        ret_v = mat_vec(PI_E0, mat_vec(V, mid_v))
        sb_val = (vec_inner(U0_VEC, ret_v) / Qi(2, 0)).re
        sh_val = vec_norm_sq(mid_v) / vec_norm_sq(U0_VEC)
        sb_set.add(sb_val)
        sh_set.add(sh_val)
    assert len(sb_set) == 1 and len(sh_set) == 1
    sb = sb_set.pop()
    sh = sh_set.pop()

    rho_B1 = Qi(sb, 0) * rho_B1_unit
    rho_B2 = Qi(sb, 0) * rho_B2_unit
    x_B1 = rho_B1.im
    cw_B1 = sb * sb
    x_B2 = rho_B2.im
    cw_B2 = Fraction(5, 8) * (sb * sb)

    if cw_B1 == 0:
        b1_str = f"({x_B1}, {cw_B1}, STOP:0/0)"
        b2_str = f"({x_B2}, {cw_B2}, STOP:0/0)"
        assert orb_name != "O_{u,-u}"
    else:
        rat_B1 = Fraction(5) * x_B1 / cw_B1
        rat_B2 = Fraction(5) * x_B2 / cw_B2
        b1_str = f"({x_B1}, {cw_B1}, {rat_B1})"
        b2_str = f"({x_B2}, {cw_B2}, {rat_B2})"
        assert orb_name == "O_{u,-u}"
        assert sb == Fraction(-1, 2)
        assert sh == Fraction(1, 2)
        assert rho_B1 == Qi(Fraction(3, 10), Fraction(2, 5))
        assert rho_B2 == Qi(Fraction(1, 4), Fraction(1, 8))
        assert (x_B1, cw_B1, rat_B1) == (Fraction(2, 5), Fraction(1, 4), Fraction(8))
        assert (x_B2, cw_B2, rat_B2) == (Fraction(1, 8), Fraction(5, 32), Fraction(4))

    print(f"{orb_name:<10} | {len(pairs):<4} | {str(sb):<8} | {str(sh):<8} | {b1_str:<26} | {b2_str:<26}")

assert len(seen_pairs) == 24

# ============================================================================
# 7. Exact Return-Coefficient and Fourier-Determinant Identities
# COVERAGE-RETURN-AND-FOURIER
# Exhaustive checks cover the return coefficient on all 25 pairs and the
# determinant products and antipodal membership on the 24 nontrivial pairs.
# The AlphaMap order obstruction is a prose derivation, not a check here.
# ============================================================================
class QZeta5:
    """Exact element in Q(zeta_5) in basis {1, z, z^2, z^3} with 1+z+z^2+z^3+z^4 = 0."""
    __slots__ = ("c",)
    def __init__(self, c=(0, 0, 0, 0)):
        self.c = tuple(Fraction(x) for x in c)
    @staticmethod
    def from_powers(p):
        """p is dict or 5-tuple of coefficients of z^0..z^4."""
        c4 = Fraction(p[4])
        return QZeta5(tuple(Fraction(p[k]) - c4 for k in range(4)))
    def __add__(self, o):
        return QZeta5(tuple(self.c[k] + o.c[k] for k in range(4)))
    def __sub__(self, o):
        return QZeta5(tuple(self.c[k] - o.c[k] for k in range(4)))
    def __mul__(self, o):
        acc = [Fraction(0)] * 5
        for i in range(4):
            for j in range(4):
                acc[(i + j) % 5] += self.c[i] * o.c[j]
        return QZeta5.from_powers(acc)
    def conj(self):
        # conj(z^k) = z^{-k mod 5}
        acc = [Fraction(0)] * 5
        for k in range(4):
            acc[(-k) % 5] += self.c[k]
        return QZeta5.from_powers(acc)
    def galois(self, a):
        # sigma_a(z^k) = z^{a*k mod 5} for a in {1,2,3,4}
        assert a in (1, 2, 3, 4)
        acc = [Fraction(0)] * 5
        for k in range(4):
            acc[(a * k) % 5] += self.c[k]
        return QZeta5.from_powers(acc)
    def __eq__(self, o):
        return self.c == o.c

def z_pow(k):
    p = [0] * 5
    p[k % 5] = 1
    return QZeta5.from_powers(p)

print("\n=== 4. EXACT RETURN COEFFICIENTS AND CYCLOTOMIC FOURIER-DETERMINANT CHECKS ===")
for a in range(5):
    for b in range(5):
        V = V_flip_op(a, b)
        mid_v = mat_vec(PI_NEQ0, mat_vec(V, U0_VEC))
        ret_v = mat_vec(PI_E0, mat_vec(V, mid_v))
        sb_val = (vec_inner(U0_VEC, ret_v) / Qi(2, 0)).re
        d_apb = 1 if (a + b) % 5 == 0 else 0
        d_a0 = 1 if a == 0 else 0
        d_b0 = 1 if b == 0 else 0
        expected_sb_Z5 = Fraction(-1, 2) * (d_apb - d_a0 * d_b0)
        assert sb_val == expected_sb_Z5
        if (a, b) != (0, 0):
            expected_sb_Int = Fraction(-1, 2) * d_apb
            assert sb_val == expected_sb_Int

antipodal_fourier = []
for (a, b) in I_nt:
    prod_det = z_pow(0)
    for m in range(5):
        prod_det = prod_det * z_pow(m * (a + b))
    assert prod_det == z_pow(0)
    if z_pow(a + b) == z_pow(0) and a != 0 and b != 0:
        antipodal_fourier.append((a, b))
assert antipodal_fourier == [(1, 4), (2, 3), (3, 2), (4, 1)]
print("  [PASS] General s_bilin formula holds on all 25 pairs; its -1/2 * delta_{a+b,0} restriction holds on I_nt.")
print("  [PASS] Exact Q(zeta_5) Fourier check verified: antipodal set {(1,4),(2,3),(3,2),(4,1)}.")
print("  [NOTE] The completed-history AlphaMap order obstruction is derived in the companion note; it is not an additional machine check here.")

# ============================================================================
# 8. Paired Vertex-Parametrized Automaton (Emit -> eps*Emit, Reabs -> eps*Reabs),
#    Creation-Time Emission Reading chi_i(eps), and First-Jet Chain Rule in Q[tau]/(tau^2)
# COVERAGE-PAIRED-FINITE-JETS
# Evolution, grading, creation weights, and occupancy comparisons use N=2..6
# for all 24 couplings in B1/B2. Jet1 checks the supplied rational rate
# coefficients after factoring out Pi; physical A6 and AlphaMap remain open.
# ============================================================================
class Jet1:
    """Exact element c0 + c1 * t in the first-jet ring Q[t]/(t^2)."""
    __slots__ = ("c0", "c1")
    def __init__(self, c0=0, c1=0):
        self.c0 = Fraction(c0)
        self.c1 = Fraction(c1)
    def compose(self, other):
        """Given self(t) = c0 + c1*t and other(u) = 0 + d1*u (with other.c0 == 0), return self(other(u)) mod u^2."""
        assert other.c0 == 0, "Formal jet composition requires zero constant term"
        return Jet1(self.c0, self.c1 * other.c1)
    def inverse_Composition(self):
        """Return formal compositional inverse in Q[u]/(u^2) when c0 == 0 and c1 != 0."""
        assert self.c0 == 0 and self.c1 != 0
        return Jet1(0, Fraction(1) / self.c1)
    def __eq__(self, o):
        return self.c0 == o.c0 and self.c1 == o.c1

def run_paired_eps_automaton(a, b, mode, N):
    D_e0 = mat_mul(D_REST, PI_E0)
    V = V_flip_op(a, b)
    Emit = mat_mul(PI_NEQ0, mat_mul(D_REST, V))
    Reabs = mat_mul(PI_E0, mat_mul(D_REST, V))
    Mid = mat_zero(10) if mode == "B1" else mat_mul(PI_NEQ0, mat_mul(D_REST, PI_NEQ0))
    z10 = [ZERO for _ in range(10)]

    r_curr = (list(U0_VEC), list(z10), list(z10))  # purely eps^0
    e_slots = []   # list of (deg0, deg1, deg2)
    p_slots = []   # list of (deg0, deg1, deg2)
    chi_history = []  # chi_i = e_{i,i} recorded at creation tick i = 1..N

    for n in range(1, N + 1):
        new_p_slots = []
        for i_idx in range(len(p_slots)):
            p_prev = p_slots[i_idx]
            e_prev = e_slots[i_idx]
            assert p_prev[0] == z10 and p_prev[1] == z10
            assert e_prev[0] == z10 and e_prev[2] == z10
            p_deg2 = vec_add(mat_vec(D_e0, p_prev[2]), mat_vec(Reabs, e_prev[1]))
            new_p_slots.append((list(z10), list(z10), p_deg2))
        if len(e_slots) == n - 1 and n >= 2:
            e_last = e_slots[n - 2]
            assert e_last[0] == z10 and e_last[2] == z10
            p_deg2 = mat_vec(Reabs, e_last[1])
            new_p_slots.append((list(z10), list(z10), p_deg2))

        new_e_slots = []
        for e_prev in e_slots:
            assert e_prev[0] == z10 and e_prev[2] == z10
            new_e_slots.append((list(z10), mat_vec(Mid, e_prev[1]), list(z10)))

        assert r_curr[1] == z10 and r_curr[2] == z10
        chi_n_deg1 = mat_vec(Emit, r_curr[0])
        e_nn = (list(z10), chi_n_deg1, list(z10))
        new_e_slots.append(e_nn)
        chi_history.append(e_nn)

        r_curr = (mat_vec(D_e0, r_curr[0]), list(z10), list(z10))

        e_slots = new_e_slots
        p_slots = new_p_slots

    return r_curr, e_slots, p_slots, chi_history

print("\n=== 5. PAIRED AUTOMATON N=2..6 AND SUPPLIED RATIONAL FIRST-JET COEFFICIENTS ===")
print(f"{'Orbit':<10} | {'s_herm':<8} | {'5*x_B1 / s_herm':<18} | {'5*x_B2 / s_herm':<18}")
print("-" * 64)

zero_denom_count = 0
offdiag_vals_B1 = set()
offdiag_vals_B2 = set()

for orb_name, pairs in orbit_defs:
    for (a, b) in pairs:
        V = V_flip_op(a, b)
        mid_v = mat_vec(PI_NEQ0, mat_vec(V, U0_VEC))
        sh = vec_norm_sq(mid_v) / vec_norm_sq(U0_VEC)
        sb = Fraction(-1, 2) if (a + b) % 5 == 0 else Fraction(0)

        for mode in ("B1", "B2"):
            for N in range(2, 7):
                r_N, e_N, p_N, chi_hist = run_paired_eps_automaton(a, b, mode, N)
                psi0_1, exc_1, h_1 = run_history_automaton(a, b, mode, N)
                assert r_N[0] == psi0_1
                assert [slot[1] for slot in e_N] == exc_1
                assert [slot[2] for slot in p_N] == h_1
                F_N_coeff = Fraction(0)
                for i_tick, chi_slot in enumerate(chi_hist, start=1):
                    w_i = vec_norm_sq(chi_slot[1]) / ((Fraction(5) ** i_tick) * vec_norm_sq(U0_VEC))
                    assert w_i == sh
                    F_N_coeff += w_i
                assert F_N_coeff == Fraction(N) * sh
                alpha_N_coeff = F_N_coeff / Fraction(N)
                assert alpha_N_coeff == sh

                final_occ_total = sum(vec_norm_sq(slot[1]) for slot in e_N) / (
                    (Fraction(5) ** N) * vec_norm_sq(U0_VEC)
                )
                if mode == "B2":
                    assert final_occ_total == F_N_coeff
                else:
                    assert final_occ_total == sh
                    if sh > 0 and N >= 2:
                        assert final_occ_total != F_N_coeff

        if sh == 0:
            zero_denom_count += 1

    a0, b0 = pairs[0]
    V0 = V_flip_op(a0, b0)
    sh = vec_norm_sq(mat_vec(PI_NEQ0, mat_vec(V0, U0_VEC))) / vec_norm_sq(U0_VEC)
    sb = Fraction(-1, 2) if (a0 + b0) % 5 == 0 else Fraction(0)
    x_B1 = (Qi(sb, 0) * rho_B1_unit).im
    x_B2 = (Qi(sb, 0) * rho_B2_unit).im

    if sh == 0:
        assert orb_name == "O_{u,u}"
        s_b1 = "undefined (STOP)"
        s_b2 = "undefined (STOP)"
    else:
        alpha_jet = Jet1(0, sh)
        tau_of_alpha = alpha_jet.inverse_Composition()
        pi_ae_B1_jet = Jet1(0, Fraction(5) * x_B1 / Fraction(2)).compose(tau_of_alpha)
        pi_ae_B2_jet = Jet1(0, Fraction(5) * x_B2 / Fraction(2)).compose(tau_of_alpha)

        ratio_B1 = Fraction(5) * x_B1 / sh
        ratio_B2 = Fraction(5) * x_B2 / sh
        assert pi_ae_B1_jet.c1 == ratio_B1 / Fraction(2)
        assert pi_ae_B2_jet.c1 == ratio_B2 / Fraction(2)

        offdiag_vals_B1.add(ratio_B1)
        offdiag_vals_B2.add(ratio_B2)
        s_b1 = str(ratio_B1)
        s_b2 = str(ratio_B2)
        if orb_name == "O_{u,-u}":
            assert ratio_B1 == Fraction(4)
            assert ratio_B2 == Fraction(5, 4)
        else:
            assert ratio_B1 == Fraction(0)
            assert ratio_B2 == Fraction(0)

    print(f"{orb_name:<10} | {str(sh):<8} | {s_b1:<18} | {s_b2:<18}")

assert zero_denom_count == 4
assert offdiag_vals_B1 == {Fraction(0), Fraction(4)}
assert offdiag_vals_B2 == {Fraction(0), Fraction(5, 4)}
print("  [PASS] For all 24 couplings in B1/B2 at N=2..6, paired grading, h_N(eps)=eps^2*h_N, creation weights, and final occupancy comparisons hold.")
print("  [PASS] Supplied rational first-jet coefficients give 4 zero denominators; off-diagonal sets {0, 4} (B1), {0, 5/4} (B2); no physical A6 or AlphaMap is derived.")

# ============================================================================
# 9. Register Return Identities, Finite Opposite-Branch Comparisons,
#    and Quotient Algebra for Supplied Pairs (v, s)
# COVERAGE-RETURN-OPPOSITE-FINITE
# Matrix identities cover all four antipodal couplings. Opposite-branch
# evolution is compared only at N=2..6 in B1/B2. Its all-N extension and the
# coin phase-generator interpretation are mathematical derivations in the note.
# ============================================================================
def mat_dag(A):
    n = len(A)
    return [[A[c][r].conj() for c in range(n)] for r in range(n)]

E1_10 = E_op(1)
assert mat_mul(PI_E0, E1_10) != mat_mul(E1_10, PI_E0)

U0_MINUS_VEC = [ZERO for _ in range(10)]
U0_MINUS_VEC[idx(0, 0)] = ONE
U0_MINUS_VEC[idx(1, 0)] = -ONE

for u in range(1, 5):
    b_ant = (-u) % 5
    T_op = mat_scale(Fraction(1, 2), mat_sub(E_op(u), E_op(b_ant)))
    TQT = mat_mul(T_op, mat_mul(PI_NEQ0, T_op))
    e0_vec = [ZERO for _ in range(10)]
    e0_vec[idx(0, 0)] = ONE
    tqt_e0 = mat_vec(TQT, e0_vec)
    expected_tqt_e0 = [ZERO for _ in range(10)]
    expected_tqt_e0[idx(0, (2 * u) % 5)] = expected_tqt_e0[idx(0, (2 * u) % 5)] + Qi(Fraction(1, 4), 0)
    expected_tqt_e0[idx(0, (-2 * u) % 5)] = expected_tqt_e0[idx(0, (-2 * u) % 5)] + Qi(Fraction(1, 4), 0)
    expected_tqt_e0[idx(0, 0)] = expected_tqt_e0[idx(0, 0)] + Qi(Fraction(-1, 2), 0)
    assert tqt_e0 == expected_tqt_e0
    assert mat_mul(PI_E0, mat_mul(TQT, PI_E0)) == mat_scale(Fraction(-1, 2), PI_E0)

    V_u = V_flip_op(u, b_ant)
    assert mat_dag(V_u) == mat_scale(Fraction(-1), V_u)

    D_e0 = mat_mul(D_REST, PI_E0)
    Emit = mat_mul(PI_NEQ0, mat_mul(D_REST, V_u))
    Reabs = mat_mul(PI_E0, mat_mul(D_REST, V_u))
    for mode in ("B1", "B2"):
        Mid = mat_zero(10) if mode == "B1" else mat_mul(PI_NEQ0, mat_mul(D_REST, PI_NEQ0))
        for N in range(2, 7):
            psi0_plus, _, h_plus = run_history_automaton(u, b_ant, mode, N)
            A_N_plus = vec_inner(psi0_plus, S_N_map(h_plus)) / Qi(vec_norm_sq(psi0_plus), 0)
            psi_pre_m = list(U0_MINUS_VEC)
            exc_m = []
            post_m = []
            for tick in range(1, N + 1):
                new_post_m = [
                    vec_add(mat_vec(D_e0, post_m[k]), mat_vec(Reabs, exc_m[k]))
                    for k in range(len(post_m))
                ]
                if len(exc_m) == tick - 1 and tick >= 2:
                    new_post_m.append(mat_vec(Reabs, exc_m[tick - 2]))
                new_exc_m = [mat_vec(Mid, v_e) for v_e in exc_m]
                new_exc_m.append(mat_vec(Emit, psi_pre_m))
                psi_pre_m = mat_vec(D_e0, psi_pre_m)
                exc_m, post_m = new_exc_m, new_post_m
            A_N_minus = vec_inner(psi_pre_m, S_N_map(post_m)) / Qi(vec_norm_sq(psi_pre_m), 0)
            assert A_N_minus == A_N_plus.conj()

# COVERAGE-SUPPLIED-QUOTIENT
# Six supplied rational (v,s) pairs are checked with Pi factored out. The
# general F_Pi quotient identity follows from the prose quotient derivation;
# the physical meanings or selection of v and s are not established here.
def jet_div(num: Jet1, den: Jet1) -> Jet1:
    assert den.c0 != 0
    c0 = num.c0 / den.c0
    c1 = (num.c1 * den.c0 - num.c0 * den.c1) / (den.c0 * den.c0)
    return Jet1(c0, c1)

def ae_prime_times_Pi_from_vs(v_rate: Fraction, s_rate: Fraction) -> Fraction:
    theta_v_jet = Jet1(Fraction(2, 5), v_rate)
    theta_s_jet = Jet1(Fraction(1, 5), s_rate)
    g_jet = jet_div(theta_v_jet, theta_s_jet)
    assert g_jet.c0 == Fraction(2)
    ae_jet = Jet1((g_jet.c0 - Fraction(2)) / Fraction(2), g_jet.c1 / Fraction(2))
    assert ae_jet.c0 == Fraction(0)
    assert ae_jet.c1 == Fraction(5, 2) * (v_rate - Fraction(2) * s_rate)
    return ae_jet.c1

print("\n=== 6. RETURN MATRICES, OPPOSITE-BRANCH COMPARISONS N=2..6, AND SIX SUPPLIED QUOTIENT PAIRS ===")
for mode_label, x_val in (("B1", Fraction(2, 5)), ("B2", Fraction(1, 8))):
    b1_res = ae_prime_times_Pi_from_vs(x_val, Fraction(0))
    assert b1_res == Fraction(5, 2) * x_val
    b2_res = ae_prime_times_Pi_from_vs(x_val, x_val / Fraction(2))
    assert b2_res == Fraction(0)
    b3_res = ae_prime_times_Pi_from_vs(Fraction(0), x_val)
    assert b3_res == -Fraction(5) * x_val
    print(f"  Mode {mode_label} (x_B = {x_val}): supplied (v=x, s=0) => {b1_res}; (v=x, s=x/2) => {b2_res}; (v=0, s=x) => {b3_res}")
print("  [PASS] TQT e_0 = (e_{2u}+e_{-2u}-2e_0)/4, P_0 TQT P_0 = -1/2 P_0, [P_0, E_1] != 0 verified.")
print("  [PASS] V_{u,-u}^dag=-V_{u,-u} holds for all four antipodal couplings; A_{N,-}=conj(A_{N,+}) holds in B1/B2 at tested N=2..6.")
print("  [PASS] Six supplied rational (v,s) pairs satisfy the scaled quotient coefficient (5/2)*(v-2*s); no operator-to-angle identification is checked.")

# ============================================================================
# 10. H-Metric and Projection Arithmetic on Supplied Register Vectors
# COVERAGE-H-PROJECTION-ARITHMETIC
# Checks below cover annihilation of ones, reference/emission quadratic
# values, P_H applied to a supplied return vector, and supplied scalar rate
# formulas. They do not independently verify P_H idempotence, H-self-adjointness,
# a trace-pullback theorem, or the full H-modified propagation.
# ============================================================================
print("\n=== 7. H-METRIC PROJECTION ARITHMETIC ON SUPPLIED VECTORS AND RATE FORMULAS ===")
H_5 = [[Fraction(1 if r == c else 0) - Fraction(1, 5) for c in range(5)] for r in range(5)]
P_H_5 = [[Fraction(0) for _ in range(5)] for _ in range(5)]
for c in range(5):
    P_H_5[0][c] = Fraction(4, 4) if c == 0 else Fraction(-1, 4)
Q_H_5 = [[(Fraction(1 if r == c else 0) - P_H_5[r][c]) for c in range(5)] for r in range(5)]

def h_inner_5(u5, v5):
    s = Fraction(0)
    for r in range(5):
        for c in range(5):
            s += u5[r] * H_5[r][c] * v5[c]
    return s

def mat5_vec(M5, v5):
    return [sum(M5[r][c] * v5[c] for c in range(5)) for r in range(5)]

e0_5 = [Fraction(1 if j == 0 else 0) for j in range(5)]
ones_5 = [Fraction(1) for _ in range(5)]
assert mat5_vec(H_5, ones_5) == [Fraction(0)] * 5
assert mat5_vec(P_H_5, ones_5) == [Fraction(0)] * 5
assert h_inner_5(e0_5, e0_5) == Fraction(4, 5)

for u in range(1, 5):
    b_ant = (-u) % 5
    Te0_5 = [Fraction(0)] * 5
    Te0_5[u] += Fraction(1, 2)
    Te0_5[b_ant] -= Fraction(1, 2)
    QTe0_5 = mat5_vec(Q_H_5, Te0_5)
    assert QTe0_5 == Te0_5
    assert h_inner_5(QTe0_5, QTe0_5) == Fraction(1, 2)
    s_herm_H = h_inner_5(QTe0_5, QTe0_5) / h_inner_5(e0_5, e0_5)
    assert s_herm_H == Fraction(5, 8)

    # Supplied closed return vector; not recomputed from an H-modified stream.
    TQTe0_5 = [Fraction(0)] * 5
    TQTe0_5[(2 * u) % 5] += Fraction(1, 4)
    TQTe0_5[(-2 * u) % 5] += Fraction(1, 4)
    TQTe0_5[0] -= Fraction(1, 2)
    PTQTe0_5 = mat5_vec(P_H_5, TQTe0_5)
    assert PTQTe0_5 == [Fraction(-5, 8) if j == 0 else Fraction(0) for j in range(5)]
    s_bilin_H = h_inner_5(e0_5, PTQTe0_5) / h_inner_5(e0_5, e0_5)
    assert s_bilin_H == Fraction(-5, 8)

    x_B1_H = (Qi(s_bilin_H, 0) * rho_B1_unit).im
    x_B2_H = (Qi(s_bilin_H, 0) * rho_B2_unit).im
    assert x_B1_H == Fraction(1, 2)
    assert x_B2_H == Fraction(5, 32)
    assert Fraction(5) * x_B1_H / s_herm_H == Fraction(4)
    assert Fraction(5) * x_B2_H / s_herm_H == Fraction(5, 4)

print("  [PASS] Supplied-vector H-projection arithmetic and scalar rate formulas give s_herm^H=5/8, s_bilin^H=-5/8, x_B1^H=1/2, x_B2^H=5/32, and ratios 4, 5/4; full H-modified propagation is not checked.")

# ============================================================================
# 11. Galois Indices, Imported Wall-Coefficient Consequences, and J Products
# COVERAGE-WALL-IMPORTED-COEFFICIENTS
# WALL-CIRCLE-LEMMA is an imported Canon premise. Its principal-logarithm and
# principal-dilogarithm identities are not reproved or evaluated here. This
# section checks the Galois index map and rational coefficient consequences.
# ============================================================================
print("\n=== 8. GALOIS INDICES, RATIONAL CONSEQUENCES OF IMPORTED WALL FORMULAS, AND J PRODUCTS ===")
# Root elements z_k = 1 + zeta_5^k for k in {1,2,3,4}; J = 1 + zeta_5^2 = z_2.
z_roots = {k: z_pow(0) + z_pow(k) for k in (1, 2, 3, 4)}
J_elem = z_pow(0) + z_pow(2)
Jbar_elem = J_elem.conj()
assert J_elem == z_roots[2]
assert Jbar_elem == z_roots[3]

# Check sigma_a(J) = z_{2a mod 5} for a = 1, 2, 3, 4:
galois_root_indices = []
im_li1_pi_coeffs = []
re_li2_pi2_coeffs = []
for a in (1, 2, 3, 4):
    k_a = (2 * a) % 5
    assert J_elem.galois(a) == z_roots[k_a]
    galois_root_indices.append(k_a)
    # Imported premise from WALL-CIRCLE-LEMMA [T], not an independent wall proof:
    # psi_k/pi=(5-2*k)/5 and Re Li_2(z_k)/pi^2=(psi_k/pi)^2/4.
    psi_coeff = Fraction(5 - 2 * k_a, 5)
    li2_coeff = (psi_coeff * psi_coeff) / Fraction(4)
    assert li2_coeff / (psi_coeff * psi_coeff) == Fraction(1, 4)
    im_li1_pi_coeffs.append(psi_coeff)
    re_li2_pi2_coeffs.append(li2_coeff)

assert galois_root_indices == [2, 4, 1, 3]
assert im_li1_pi_coeffs == [Fraction(1, 5), Fraction(-3, 5), Fraction(3, 5), Fraction(-1, 5)]
assert re_li2_pi2_coeffs == [Fraction(1, 100), Fraction(9, 100), Fraction(9, 100), Fraction(1, 100)]

# Orbit sum and normalized branch weights:
orbit_li2_sum = sum(re_li2_pi2_coeffs, Fraction(0))
assert orbit_li2_sum == Fraction(1, 5)
orbit_weights = [c / orbit_li2_sum for c in re_li2_pi2_coeffs]
assert orbit_weights == [Fraction(1, 20), Fraction(9, 20), Fraction(9, 20), Fraction(1, 20)]
# Contracting Galois branches a = 1, 4 vs expanding Galois branches a = 2, 3:
assert orbit_weights[0] + orbit_weights[3] == Fraction(1, 10)
assert orbit_weights[1] + orbit_weights[2] == Fraction(9, 10)

# COVERAGE-J-SCALAR-PRODUCTS
# Only scalar products in Q(zeta_5) are checked here: J*Jbar is real and
# J^2 is distinct and nonreal. Their assignment to emission/reabsorption
# factors and the resulting ratio cancellation are prose derivations in the
# note. No J-weighted operator evolution or phase/weight ratio is tested here.
JJbar = J_elem * Jbar_elem
J_sq = J_elem * J_elem
assert JJbar == QZeta5.from_powers([2, 0, 1, 1, 0])
assert JJbar.conj() == JJbar
assert J_sq == QZeta5.from_powers([1, 0, 2, 0, 1])
assert J_sq != JJbar
assert J_sq.conj() != J_sq

print("  [PASS] Galois branch map sigma_a(J) = z_{2a mod 5} verified: a=(1,2,3,4) -> k=(2,4,1,3).")
print("  [PASS] Rational consequences of imported wall formulas give coefficient lists (1/5,-3/5,3/5,-1/5), (1/100,9/100,9/100,1/100), orbit sum 1/5, and stated normalized weights.")
print("  [PASS] Scalar products J*Jbar and J^2 have the stated cyclotomic coefficients; J*Jbar is real and J^2 is distinct and nonreal. No J-dressed stream is checked.")
