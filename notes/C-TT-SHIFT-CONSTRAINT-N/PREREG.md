# PREREG: C-TT-SHIFT-CONSTRAINT-N

```text
CANDIDATE:              C-TT-SHIFT-CONSTRAINT-N
STATUS:                 NON-CANONICAL INCUBATION, NO AUTHORITY
SCIENTIFIC STATUS:      candidate-D (construction), candidate-T (identities certified)
TARGET LINE:            public, mathorn1973/twist-j main
BASIS:                  Public Canon v81, main after merge of #908 (4fe37d3539ce4513d51e71e90f78e3ae0a607ad1)
OWNER ROWS (unchanged): TT-VECTOR-STATE-NORMALIZATION [O], FRW-INHOM [O], TT-SOURCE [O]
PREDECESSORS:           C-K1-DYNAMIC-METRIC-N (owner F for the r_T route),
                        C-TT-LAPSE-CONSTRAINT-N (PR #909, rescoped: shift set to zero
                        before variation, momentum constraints absent, witness
                        h_13 = n f(r) not excluded; second-order source by transcription)
ACTION LAYER:           L1 rational arrays with the declared L2 role of lapse, shift and
                        spatial metric; no L1-to-L2 gate is registered or executed
FORMAL PUBLIC PROBE:    NONE
CANON / REGISTRY EDIT:  NONE
DATA OPENED BEFORE FREEZE: NONE
AUTHOR:                 A. M. Thorn, 2026-09-08
```

## 0. The owner's acceptance object, frozen

From the review of PR #909: one common constrained variational system with
lapse and shift, from which at the same order the Hamiltonian constraint, the
momentum constraints and their preservation follow; the homogeneous component
part of the solution; the exact identity `L(h^2) = 2 h L h - 2 g(h)` used to
locate the disputed local lapse term; the two K1 windows preserved and any
extension explicitly delimited. The acceptance object is a complete compatible
initial-data and constraint-propagation construction, or an exact scoped
counterexample; not another covariance table and not a renamed scalar
denominator.

This candidate delivers the linear-order part of that object on the planar
carrier and states exactly which parts it does not deliver (section 4).

## 1. The six preregistration fields

**Equation.** Discrete linearized ADM action on the planar carrier `Z/5` with
lapse `nu = 1 + n`, shift `N = (N_1, N_2, N_3)` and spatial metric
`gamma = I + H`, prefactor `1/(2 lambda)`, `lambda = 216 pi` from
FRW-CANONICAL-FORM [T]. One antisymmetric first-difference operator `D`
(`D^T = -D`) and the Laplacian `L := -D^2 = D^T D`. Time staggering: `h_ij`
and `n` on integer slices, `N_i` and `K_ij` on half-integer slices,
`Delta f(n) = f(n+1) - f(n)`. With only the axis-3 difference present,

```text
K_11 = Delta h_11 / 2,   K_22 = Delta h_22 / 2,   K_12 = Delta h_12 / 2,
K_13 = (Delta h_13 - D N_1) / 2,   K_23 = (Delta h_23 - D N_2) / 2,
K_33 = (Delta h_33 - 2 D N_3) / 2,   K = K_11 + K_22 + K_33,

S = sum_n sum_r (1/(2 lambda)) [ K_ij K_ij - K^2 + G_2(h) + n R_1(h) ]
    + sum_n sum_r [ - n rho + N_i J_i + (1/2) h_ij S_ij ]          (prescribed source),

G_2 = (1/2) <D h_3j, D h_3j> - (1/2) <D h_33, D h> + (1/4) <D h, D h> - (1/4) <D h_ij, D h_ij>,
R_1 = D D h_33 - D D h = L (h_11 + h_22) = 2 L tau.
```

Gauge transformation to be tested (parameters `xi_0` on half-integer slices,
`xi_1, xi_2, xi_3` on integer slices):

```text
delta h_13 = D xi_1,   delta h_23 = D xi_2,   delta h_33 = 2 D xi_3,   other h_ij unchanged,
delta N_i  = Delta xi_i + delta_(i,3) D xi_0,
delta n    = -( xi_0(n + 1/2) - xi_0(n - 1/2) ).
```

**Code.** `verify.py`, Python standard library, exact arithmetic. Two
representations: (P1) a commutative symbol algebra `Q[L, D, E, E^-1]/(D^2 + L)`
with transpose `D -> -D`, `E -> E^-1`, in which the action is a quadratic form
with operator coefficients and all identities are checked as operator
identities valid for every antisymmetric circulant `D` with `L = -D^2`; (P2)
an explicit polynomial action on `Z/5 x Z/4` (time periodic) with the rational
centered difference `D_c f(r) = (f(r+1) - f(r-1))/2` and `L_c = -D_c^2`, in
which gauge invariance and the Euler-Lagrange equations are checked as
polynomial identities in all field and gauge variables.

**Carrier or data.** Planar `Z/5`; the ten K1 words and weights unchanged from
`notes/V81-TT-K1-SOURCE-MAP-1.md`; the public planar stencil
`(L f)_r = [188 f_r - 29(f_(r-1)+f_(r+1)) - 65(f_(r-2)+f_(r+2))]/324` as the
target of the square-root question.

**Systematics.** (i) Linear order only: no second-order TT self-source, so the
decoder-reading scalar of the predecessor is not reproduced here; the
transcriptions (i)/(ii) are outside this candidate. (ii) Flat static
background: the homogeneous `k = 0` sector is analysed exactly but not solved
on an FRW background. (iii) Planar carrier only. (iv) The public stencil `L`
may or may not admit a rational antisymmetric `D` with `-D^2 = L`; this is
decided exactly, and the consequence for which `D` the theory uses is recorded
as a fork, not decided here.

**Failure threshold.** Each check is an exact identity or an exact
counterexample; no tolerance. A fired falsifier is recorded, not repaired.

**Action layer.** L1; intended L2 role declared; no gate.

## 2. Falsifiers of this candidate

```text
FA  the discrete action is not exactly invariant under the stated gauge
    transformation (linear part or quadratic part fails)
FB  the Noether identities do not give preservation of the Hamiltonian and
    momentum constraints by the evolution equations
FC  in the zero-shift gauge the momentum constraint does not exclude the
    witness h_13 = n f(r), or the witness is not the pure-gauge configuration
    generated by xi_1 = n D^-1 f
FD  after constraints and gauge fixing, a non-TT radiative sector survives on
    nonzero modes in vacuum
FE  the fixed K1 intensities admit no conserved completion at all (as opposed
    to the covector stress S_33 = -iota/2, J = 0 being non-conserved)
```

Recorded facts that are not falsifiers: whether the public planar `L` has a
rational antisymmetric square root; the exact form of the `k = 0` obstruction.

## 3. Checks

```text
P1  operator algebra: Euler-Lagrange expressions for n, N_1, N_2, N_3 and the
    six h_ij; Noether identities for xi_0, xi_1, xi_2, xi_3 vanish identically
    (vacuum); the same with the prescribed source gives the exact discrete
    conservation laws the source must satisfy
P2  the quadratic form vanishes on pure-gauge configurations (operator level)
P3  explicit D_c model, time-periodic: S(phi + G xi) - S(phi) = 0 as a
    polynomial identity in all variables; Euler-Lagrange equations at interior
    slices agree with P1; witness h_13 = n f with N = 0 violates the momentum
    constraint; with N_1 = D_c^-1 f all equations hold (pure gauge)
P4  no rational antisymmetric circulant D on Z/5 satisfies -D^2 = L_public:
    the reduced quadratic has discriminant 4 . 71 . 151, not a square
P5  K1 source: D iota != 0 for all ten words (any D invertible on nonzero
    modes), so the covector stress with J = 0 violates the conservation law;
    a conserved completion (J_3, S_33) exists and is computed for D_c
P6  zero mode: the k = 0 Hamiltonian constraint reads -rho_hat_0 = 0 on the
    static flat background; recorded exactly
P7  sector reduction in vacuum on nonzero modes, gauge N = 0, ell = 0: tau = 0,
    K_13 = K_23 = 0, h_13, h_23 constant and gaugeable to zero; h_+, h_x satisfy
    Delta^2 h + L h = 0; lapse n = 0
```

## 4. What this candidate does not claim

No second-order source, no TT self-sourcing, no decision of the (i)/(ii)
transcriptions, no FRW background, no solution of the homogeneous component
beyond its exact obstruction, no three-dimensional carrier, no Regge-Wheeler
coefficient, no `P_S`, no `r_T`, no change to any registered row, no
promotion.
