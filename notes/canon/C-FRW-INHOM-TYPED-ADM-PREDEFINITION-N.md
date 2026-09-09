# C-FRW-INHOM-TYPED-ADM-PREDEFINITION-N

**NON-CANONICAL / DEFINITION-ONLY / NO FORMAL SCIENTIFIC RUN**

```text
STATE:                 READY-DEFINITION
AUTHORITY BASIS:       Public Canon v82
BASE MAIN:              78186de105c1d79d51107c8e01520ee4bf0b6568
OWNER:                  FRW-INHOM [O], unchanged
CONNECTED:              TT-SOURCE [O], TT-VECTOR-STATE-NORMALIZATION [O], unchanged
ACTION SCOPE:           selected typed L1/L2 mathematical reading, local FRW tangent
FORMAL PROBE:           NONE
SCIENTIFIC STATUS MOVE: NONE
```

This note freezes one selected positive construction class. It does not claim
that the class exhausts all discrete gravity constructions. Exhaustiveness over
all inhomogeneous extensions is needed only for the universal negative route of
`FRW-INHOM`. Positive closure is tested on the selected class below.

The purpose is narrow. Keep the Public Canon v82 K1 packet and propagator
unchanged, solve its positive zero mode by a genuine homogeneous FRW component,
and derive the quadratic TT source and its time placement from one typed cubic
constraint action. The construction uses incidence maps rather than a
same-carrier nonlinear derivative.

No numerical target, measured cosmological value, `P_S`, `P_T`, or `r_T` is
used to choose any definition below.

## 1. Frozen tuple

The issue tuple is resolved as follows.

```text
S_inhom = (
  X_space                 = X = (Z/5)^3,
  X_time                  = integer counter n with half-slices n+1/2,
  translation_actions     = three commuting Z/5 translations on X,
  V_h                     = Q^X, selected plus TT amplitude,
  V_K                     = typed edge momentum P,
  V_n                     = homogeneous FRW lapse slot ell_0 plus mean-zero local lapse ell_perp,
  V_N                     = typed edge shift N,
  V_source                = derived TT Noether pair (e,j) and registered FRW matter source,
  inner_products           = normalized vertex and edge counting products,
  d                       = 3,
  delta                   = forward counter difference on h,
  W                       = diag(29/324,65/324) on hop lengths 1 and 2,
  L_public                = the v82 planar K1 operator,
  three_dimensional_extension = L3 = B^T W B,
  field_placements         = fixed in section 5,
  time_placements          = fixed in section 5,
  gauge_parameters         = mean-zero vertex xi_n,
  gauge_action             = fixed in section 9,
  action_domain            = finite-support variations of the displayed semidiscrete action,
  truncation_rule          = keep orders <= 3 in inhomogeneous perturbations,
  S2                      = Public K1 TT quadratic term plus typed scalar/vector constraints,
  S3                      = total-lapse/shift coupling to the derived quadratic TT Noether pair,
  homogeneous_embedding    = constant spatial mode carried by the public FRW background,
  FRW_restriction          = literal FRW-CANONICAL-FORM background action and constraint,
  EL_map                   = variations of S2+S3 and the public FRW background action,
  Hamiltonian_constraint   = section 10,
  momentum_constraints     = section 10,
  Noether_identities       = section 9,
  constraint_propagation   = section 10,
  TT_projector             = H = diag(h,-h,0), cross component zero in this selected class,
  TT_propagator            = Delta_c^2 h + L3 h = 0 at quadratic order,
  K1_input_map             = exact v82 h0,h1 embedding iota,
  source_reading           = rho_TT=e/(2 lambda), J_TT=j/(2 lambda),
  emission_map             = selected K1 packet -> initial TT pair (h0,h1),
  coefficient_domain       = Q with public lambda=216 pi carried formally,
  free_parameter_test      = section 12,
  Admissible               = section 13,
  ObjectEq                 = literal equality of all marked fields and labels,
  completeness_method      = syntactic exhaustion of the selected class, not all gravity,
  certificate_schema       = section 14,
  exact_checker            = future checker specified in section 14,
  decision_routing         = section 15
).
```

## 2. Why the spatial calculus is typed

Let `X=(Z/5)^3`. For each vertex `x`, direction `a in {1,2,3}`, and hop
`k in {1,2}`, introduce one oriented edge

```text
e=(x,a,k):  tail(e)=x,  head(e)=x+k e_a.
```

There are `125` vertices and `750` marked oriented edges. Define

```text
(B f)(e) = f(head(e)) - f(tail(e)),
w_1 = 29/324,
w_2 = 65/324,
(W u)(x,a,k) = w_k u(x,a,k),
L3 = B^T W B.
```

All arithmetic is rational. No square root of `L3` is used.

The nonlinear product remains the ordinary pointwise product on vertex
fields. `B` is not declared to satisfy a same-carrier Leibniz rule. This is
intentional. On a finite product of characteristic-zero fields every ordinary
same-carrier derivation is zero, so a nonzero nonlinear calculus cannot be
obtained by pretending that the public `L` has an ordinary Leibniz square
root. The typed vertex-to-edge incidence avoids that false requirement.

## 3. Exact recovery of the public planar operator

For a one-dimensional function `f:Z/5->Q`, define the planar embedding

```text
(iota f)(x1,x2,x3)=f(x3).
```

Use normalized counting products

```text
<f,g>_V = (1/25) sum_(x in X) f(x)g(x),
<u,v>_E = (1/25) sum_(e in E) u(e)v(e).
```

Then

```text
<iota f,iota g>_V = sum_(r in Z/5) f(r)g(r),
L3 iota = iota L_public,
```

where

```text
L_public = [188 I - 29(S+S^-1) - 65(S^2+S^-2)]/324.
```

The first equality fixes the transverse normalization `1/25`. It is not a
free amplitude. The second equality follows directly from
`B_k^T B_k = 2I-S^k-S^-k`; the two transverse directional contributions
vanish on `iota f`.

Thus the selected 3D carrier restricts literally to the Public Canon v82 K1
quadratic spatial operator with no rescaling.

## 4. K1 is unchanged

For every public K1 word `w`, retain exactly

```text
u_t = w_(t+2)-w_t,
h_t(r) = [delta_(r,u_t)+delta_(r,u_t+1)]/2,  t=0,1.
```

Set

```text
h_0^X = iota h_0,
h_1^X = iota h_1.
```

No word, source weight, amplitude, site, time label, or local order is
changed. The selected plus tensor is

```text
H_n(x)=diag(h_n(x),-h_n(x),0).
```

The cross component is zero because this construction attacks one selected
plus-polarized class. No statement about completeness of the polarization
family is made.

At quadratic order the TT equation is

```text
R_n := h_(n+1)-2 h_n+h_(n-1)+L3 h_n = 0.
```

On the embedded K1 sector this is exactly the v82 recurrence.

## 5. Time placement and lapse split

The placement is fixed by the local Noether identity below, not selected after
a source result.

```text
h_n                         vertex, integer slice n
d_n=h_(n+1)-h_n             vertex, half-slice n+1/2
e_(n+1/2)                   vertex, half-slice n+1/2
j_n                         edge, integer slice n
tau_(n+1/2)                 mean-zero vertex scalar, half-slice n+1/2
ell_perp_(n+1/2)            mean-zero local lapse, half-slice n+1/2
ell_0_(n+1/2)               homogeneous FRW lapse variation slot, half-slice n+1/2
P_n                         edge momentum, integer slice n
p_perp_n                    varied edge field in ker(B^T), integer slice n
N_n                         edge shift multiplier, integer slice n
xi_n                        mean-zero gauge parameter, integer slice n
```

The total lapse perturbation read by the TT source is

```text
ell_total_(n+1/2) = ell_0_(n+1/2) * 1 + ell_perp_(n+1/2).
```

`ell_0` is the perturbative variation slot of the public homogeneous FRW lapse.
It is not a second lapse or a new dynamical degree. `ell_perp` has zero spatial
mean. Therefore the constant and mean-zero Hamiltonian equations are both
retained and cannot be confused by projection.

The gauge parameter `xi_n` is mean-zero and acts only on the local split. The
homogeneous time reparametrization remains owned by the public FRW background.

## 6. The quadratic TT action

Before the common physical prefactor `1/(2 lambda)`, use

```text
A2_TT = (1/2) sum_n [ <d_n,d_n>_V - <h_n,L3 h_n>_V ].
```

Its Euler-Lagrange expression is `-R_n`. On the K1 embedding it is literally
the quadratic TT action of `DEF-K1-LINEAR-METRIC`.

The public value

```text
lambda = 216 pi
```

is carried formally. No evaluation of `pi` is needed.

## 7. The derived local TT source

For an edge `e`, put

```text
g_n(e) = (B h_n)(e),
q_n(x) = h_(n+1)(x)-h_(n-1)(x).
```

Define the half-slice vertex energy record

```text
e_(n+1/2)(x)
  = (1/2) d_n(x)^2
    + (1/4) sum_(e incident to x) w_e g_(n+1)(e) g_n(e),
```

where an edge is incident to both its tail and head and `w_e=w_k`.
Define the integer-slice oriented edge current

```text
j_n(e)
  = (1/4) w_e g_n(e)
      [ q_n(tail(e)) + q_n(head(e)) ].
```

These are definitions derived by edgewise polarization of `A2_TT`. They are
not an assumed stress tensor and contain no adjustable coefficient.

Their global sum is

```text
E_(n+1/2) = <1,e_(n+1/2)>_V
          = (1/2)[ <d_n,d_n>_V + <h_(n+1),L3 h_n>_V ].
```

This is the staggered quadratic invariant already isolated by the K1
incubation. The present definition additionally localizes it on the typed 3D
carrier.

## 8. Exact off-shell balance identity

The future checker must certify the pointwise polynomial identity

```text
e_(n+1/2) - e_(n-1/2) + B^T j_n
  = (1/2) q_n * R_n,
```

where `*` is pointwise vertex multiplication.

This identity has a direct edgewise proof. The kinetic difference gives
`(1/2) q_n [h_(n+1)-2h_n+h_(n-1)]`. Splitting the change of the edge term
equally between its two endpoints leaves exactly the oriented divergence
`B^T j_n` and `(1/2) q_n L3 h_n`.

Consequently, on every solution of the quadratic K1 equation,

```text
e_(n+1/2)-e_(n-1/2)+B^T j_n=0
```

exactly. Summing over the closed torus gives
`E_(n+1/2)=E_(n-1/2)`.

No statistical averaging, continuum limit, or Gaussian closure enters this
identity.

## 9. Constraint action and cubic Noether completion

Let `V_0` be the mean-zero vertex subspace and write `Pi_0` for subtraction of
the spatial mean. Let the typed edge momentum be

```text
p_perp_n in ker(B^T),
P_n = W B [tau_(n+1/2)-tau_(n-1/2)] + p_perp_n.
```

Here `p_perp_n` is an auxiliary geometric field varied inside `ker(B^T)`. It is
not selected after inspecting the source. Its equation and the shift equation
together determine the co-closed part of the momentum constraint.

Before the common factor `1/(2 lambda)`, freeze the local constraint terms

```text
A2_constraint
  = sum_n [
      2 <ell_perp_(n+1/2), L3 tau_(n+1/2)>_V
    + 2 <N_n, P_n>_E
    ].
```

The full cubic TT source coupling is one total-lapse plus shift pairing:

```text
A3_source
  = sum_n [
      - V0 * ell_0_(n+1/2) * bar_e_(n+1/2)
      - <ell_perp_(n+1/2), e_(n+1/2)>_V
      + <N_n, j_n>_E
    ],
```

where

```text
V0 = <1,1>_V = 5,
bar_e = <1,e>_V / V0.
```

Equivalently the two lapse terms are exactly

```text
- <ell_total_(n+1/2), e_(n+1/2)>_V.
```

Thus no source component is dropped: `ell_0` sees the exact spatial mean and
`ell_perp` sees the exact mean-zero component.

The coefficient `1` in both cubic source couplings is frozen by the existing
public prescribed-source convention: lapse couples as `-n rho` and shift as
`+N.J`. With the common gravitational prefactor, this defines

```text
rho_TT = e/(2 lambda),
J_TT   = j/(2 lambda).
```

No target observable is used in this normalization.

The local gauge transformation through the required order is

```text
delta_0 ell_perp_(n+1/2) = xi_(n+1)-xi_n,
delta_0 N_n               = B xi_n,
delta_0 tau                = 0,
delta_0 p_perp             = 0,
delta_0 h                  = 0,

delta_1 h_n                = (1/2) xi_n q_n.
```

`ell_0` is inert under this mean-zero local gauge family because homogeneous
time reparametrization belongs to the public FRW background.

The coefficient `1/2` is not chosen. For a general local ansatz

```text
-alpha <ell_perp,e> + beta <N,j>,
delta_1 h = gamma xi q,
```

the off-shell balance identity forces `alpha=beta` and
`gamma=alpha/2`. The public source normalization fixes `alpha=1`, hence
`beta=1` and `gamma=1/2`.

The quadratic constraint term is exactly invariant under `delta_0` because

```text
B^T P_n = L3[tau_(n+1/2)-tau_(n-1/2)]
```

by `B^T p_perp=0`. The local source term varies as the balance identity.
Therefore

```text
delta_0(A2_constraint+A3_source)
  = +(1/2) sum_n <xi_n q_n,R_n>_V,

delta_1 A2_TT
  = -(1/2) sum_n <xi_n q_n,R_n>_V,
```

and hence

```text
delta_0 A3 + delta_1 A2 = 0
```

through cubic order, off shell, exactly, for the declared local gauge family.
This is the frozen nonlinear gauge gate for the selected scalar backreaction
class.

## 10. Hamiltonian and momentum constraints

Variation with respect to the mean-zero local lapse gives

```text
2 L3 tau_(n+1/2) - Pi_0 e_(n+1/2) = 0,
```

or

```text
L3 tau_(n+1/2) = (1/2) Pi_0 e_(n+1/2).
```

Since `L3=B^T W B` is positive semidefinite and its kernel on the connected
three-torus is exactly the constants, this equation has one and only one
mean-zero solution for every source record.

Variation with respect to the typed shift gives

```text
2 P_n + j_n = 0.
```

Variation of `p_perp` within `ker(B^T)` gives the co-closed projection of
`N_n` equal to zero. The remaining longitudinal shift is a local gauge
multiplier, as intended.

On the TT equation `R_n=0`, the source balance identity and the two adjacent
Hamiltonian constraints imply

```text
B^T[-j_n/2 - W B(tau_(n+1/2)-tau_(n-1/2))] = 0.
```

Therefore the shift equation determines

```text
p_perp_n = -j_n/2 - W B(tau_(n+1/2)-tau_(n-1/2))
```

inside `ker(B^T)` exactly. This is an Euler-Lagrange solution for the varied
auxiliary field, not a post-result selector. No longitudinality assumption on
the K1 current is made. Harmonic and coexact current are carried by `p_perp`
rather than discarded.

The two constraint expressions obey the exact Bianchi relation, with the
quadratic TT equation as the off-shell remainder. On shell, Hamiltonian
constraint propagation and momentum solvability are the same local balance
identity.

## 11. Homogeneous FRW mode

The zero spatial mode is not put through `L3` and is not projected away. It is
owned by the public rank-1 FRW background and is coupled by the explicit
`ell_0` term in `A3_source`.

For the normalized 3D carrier

```text
V0 = <1,1>_V = 5,
bar_e_(n+1/2) = E_(n+1/2)/V0.
```

The homogeneous TT source read from the same total-lapse coupling is

```text
bar_rho_TT = bar_e/(2 lambda).
```

Vary the total action with respect to the public homogeneous FRW lapse at the
selected local FRW tangent. The public matter term contributes `rho_matter` and
the explicit cubic TT term contributes `bar_e/(2 lambda)`. The homogeneous
lapse equation is therefore

```text
3 H^2 = lambda [rho_matter + bar_rho_TT]
      = lambda rho_matter + bar_e/2.
```

This is not a new value of `lambda`. It is the public canonical constraint with
the derived TT contribution added under the same lapse variation.

When the inhomogeneous field is removed, `h=0` gives `e=j=0`, so the complete
homogeneous restriction is literally

```text
3 H^2 = lambda rho_matter,
lambda = 216 pi,
H^2 = 72 pi rho_matter,
```

with the public `FRW-CANONICAL-FORM` action, continuity clause, second
Friedmann equation, canonical Hamiltonian form, and forced fiber multiplier
unchanged. This construction does not alter or rederive those public inputs.
It extends their source side.

The present selected class is a local FRW tangent construction. It does not
claim an all-epoch transfer law for K1 wave numbers or a nonlinear strong-field
solution.

## 12. Free-parameter test

The selected class has no adjustable dimensionless coefficient.

```text
w_1,w_2         public K1 stencil, fixed
1/25            forced by exact planar norm preservation
1/2 in e,j      fixed by symmetric endpoint polarization
ell_total split identity + mean-zero decomposition, fixed
alpha=beta=1    fixed by the public lapse/shift source convention
gamma=1/2       forced by cubic Noether cancellation
lambda=216 pi   public FRW value
K1 amplitude    unchanged v82 unit amplitude
```

A future checker must treat any additional coefficient multiplying
`e`, `j`, `tau`, `P`, the planar embedding, either lapse component, or the FRW
source as a fired free-parameter falsifier.

## 13. Selected admissible class and equality

`Admissible` contains exactly the constructions obtained by the displayed
recipe from:

1. one public K1 word `w`,
2. one public FRW background satisfying `FRW-CANONICAL-FORM`, and
3. an integer counter interval with compactly supported variations.

There is no structural branch inside the class. `tau` is the unique mean-zero
solution of the Hamiltonian constraint. `p_perp` is a varied auxiliary field
whose on-shell value is fixed by the momentum equation. The lapse split is the
unique constant plus mean-zero decomposition. Translations of `X` are
symmetries but are not quotiented by `ObjectEq`.

`ObjectEq` is literal equality of the marked background, word, counter,
vertex fields, edge fields, and source records.

Completeness means syntactic completeness of this selected positive class:
every admitted input has exactly the outputs specified above. It does not mean
that every possible discrete gravity theory lies in this class.

## 14. Future exact checker and certificate schema

No result-bearing formal checker is run in this definition lane. A successor
probe, if separately collision-checked and preregistered, must freeze one
standard-library exact checker with the following certificate blocks before
execution.

```text
G1  3D incidence: L3=B^T W B, kernel(constants), planar restriction exactly L_public.
G2  K1 embedding: both initial slices and v82 recurrence unchanged for all ten words.
G3  Off-shell local balance identity as a polynomial identity on the declared carrier.
G4  Global energy identity and all-time conservation conditional on R_n=0.
G5  Cubic Noether identity delta_0 A3 + delta_1 A2 = 0 exactly.
G6  Coefficient solve: alpha=beta, gamma=alpha/2; source convention fixes alpha=1.
G7  Hamiltonian constraint has a unique mean-zero tau solution for every admitted source.
G8  Momentum solution p_perp exists in ker(B^T), with its on-shell value fixed by the shift equation.
G9  Total-lapse split is exact: local source is Pi_0 e, homogeneous source is bar_e, no zero mode is discarded, and h=0 returns every registered FRW identity unchanged.
G10 No new free dimensionless coefficient appears.
G11 K1 source law, amplitudes, words, and ordering remain byte-identical to the public definition inputs consumed.
G12 Security, policy, action-layer and dependency checks pass.
```

The formal verifier may use symbolic polynomial coefficients or exact finite
rational arrays. Floating point is forbidden in the decision path.

## 15. Decision routing

```text
READY-DEFINITION
  This note. All structural choices needed for the selected positive class are frozen.

PASS-CONSTRUCT
  A separately preregistered checker certifies G1 through G12 on both required
  architectures, with no fired falsifier. This earns a promotion package for
  the selected inhomogeneous source construction. It does not automatically
  move the owner row until the public fold verifies that the earned scope
  literally satisfies the current FRW-INHOM positive clause.

FAIL-CONSTRUCT
  Any exact failure of G1 through G11 rejects this selected construction and
  is preserved. It does not prove the universal negative FRW-INHOM clause.

STOP
  Authority drift, hash mismatch, changed K1 input, changed threshold,
  undeclared coefficient, unnamed layer lift, or source/equality ambiguity.
```

## 16. Explicit non-claims

This predefinition does not claim:

- that the selected construction is uniquely forced by `J`;
- that all nonlinear gravity is classified;
- a physical occurrence law for K1 words;
- a detector response;
- a scalar fluctuation spectrum `P_S`;
- a numerical tensor ratio `r_T`;
- a Schwarzschild or Regge-Wheeler pullback;
- QCD or matter-source closure;
- an all-epoch cosmological transfer function;
- a status move for `FRW-INHOM`, `TT-SOURCE`, or
  `TT-VECTOR-STATE-NORMALIZATION`.

The construction is designed to answer one prior obstruction exactly: the
positive K1 zero mode is carried by the homogeneous FRW lapse equation, while
the mean-zero spatial source is solved by the typed three-dimensional
constraint. Nothing is discarded by projection.