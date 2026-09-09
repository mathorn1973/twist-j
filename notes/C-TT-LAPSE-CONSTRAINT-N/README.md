# C-TT-LAPSE-CONSTRAINT-N: lapse and Hamiltonian constraint on the planar TT carrier

```text
STATUS:                 NON-CANONICAL INCUBATION
SCIENTIFIC STATUS:      candidate-D (construction and its declared choices)
                        candidate-T (the exact identities and arrays certified below)
ACTION LAYER:           L1 rational arrays; declared L2 role (lapse, spatial metric); no gate
AUTHORITY:              NO NORMATIVE AUTHORITY
FORMAL PUBLIC PROBE:    NONE
PREREGISTRATION:        PREREG.md, frozen before execution,
                        sha256 e0bb69848b442974ac6b69d32f1794547bdd982696bbb947e06077714e8f0af8
BASIS:                  Public Canon v81, main c6d90f148f6ea7295cb42c629b6cf735060ebfd4
OWNER ROWS (unchanged): TT-VECTOR-STATE-NORMALIZATION [O], FRW-INHOM [O], TT-SOURCE [O]
CANON / REGISTRY CHANGE: NONE
PROMOTION:              NONE
REVISION:               conclusions rescoped after the owner review of 2026-09-08;
                        PREREG.md and the two frozen verifiers are unchanged; a frozen
                        addendum certificate was added (section 11)
```

This note supplies one constrained geometric construction, decides what the
owner's six falsifiers do and do not establish for it, and records the exact
identities certified so far. It does not supply a complete constrained
gravitational model, a cosmological scalar power, a numerical `r_T(k)`, a
physical amplitude, or a Regge-Wheeler coefficient. It does not claim that
any of the five owner conditions is met in full. A fired falsifier is
archived as a result, not repaired.

## 1. Why this candidate exists

The predecessor `C-K1-DYNAMIC-METRIC-N` used the positive-definite pairing
`B_+(H,K) = tr(HK) + tr H tr K` as the common kinetic form of all six spatial
metric components. Its independent break-check found two structural facts:
the homogeneous trace mode then carries a positive kinetic sign, opposite to
`FRW-CANONICAL-FORM [T]`, and the trace is a radiative mode locked pointwise
to the TT component by `h_+ = -12 s`, so it cannot serve as a scalar
denominator. The owner recorded the predecessor as F for the `r_T` route and
took two program decisions: (A) `h = v^2` remains the registered TT decoder,
the square is not moved to the source side; (B) the scalar sector is a
constrained sector fixed by a lapse and a Hamiltonian constraint, not the
dynamical trace of the same radiative field.

The five conditions C1 to C5 and the six falsifiers F1 to F6 are frozen in
`PREREG.md`. This note builds the smallest construction that can be judged
against them, and the judgement is scoped.

## 2. The construction

Fields on the planar carrier `Z/5` (the K1 slot axis) at each counter `n`:
a lapse `nu = 1 + n` and a symmetric spatial metric `gamma = I + H`. The
shift is set to zero before variation; this is a declared restriction with a
consequence recorded in section 4. Discrete time difference
`Delta f_n = f_(n+1) - f_n`. Spatial operator: the exact planar reduction of
the public D3 stencil,

```text
(L f)_r = [188 f_r - 29 (f_(r-1) + f_(r+1)) - 65 (f_(r-2) + f_(r+2))] / 324,
```

with the planar rule fixed once: every product of two first differences along
the axis is the stencil form `<f, L g>`, every second difference is `-L`.

The gravitational action is the discrete linearized ADM action with the
standard indefinite DeWitt kinetic form and the prefactor `1/(2 lambda)`,
`lambda = 216 pi` from `FRW-CANONICAL-FORM [T]`:

```text
S_g = sum_n sum_r (1/(2 lambda)) [ (1/4)( tr (Delta H)^2 - (tr Delta H)^2 )
                                   + G_2(H) + n R_1(H) ],
G_2 = (1/2) d_i h_ij d_k h_kj - (1/2) d_i h_ij d_j h + (1/4) (d h)^2 - (1/4) d_k h_ij d_k h_ij,
R_1 = d_i d_j h_ij - d^2 h,           h = tr H,
```

`G_2` being the quadratic part of `sqrt(gamma) R(gamma)` (verified in the
standard way by the conformally flat check, `h_ij = 2 psi delta_ij` gives
`2 |grad psi|^2`), and `R_1` its linear part. The nonlinear homogeneous
sector is declared to be `FRW-CANONICAL-FORM` itself; only the linearized
coefficients are checked here.

Two readings of the fixed K1 are frozen:

```text
Source reading   e = (a b_r(t), 0, 0) is a prescribed stress source with
                 S_m = - sum (1 + n) sqrt(det gamma) eps_gamma(e),
                 eps_gamma(e) = (1/2) e^T gamma^-1 e, covector fixed under
                 variation. Linear terms: -(n/2)|e|^2 + (1/2) tr(H S(e)),
                 S(e) = e e^T - (|e|^2/2) I. This is the predecessor's coupling
                 with the lapse added. The owner already confined this reading
                 to TT-SOURCE; it is kept only to decide whether constrained
                 dynamics admits it at all.
Decoder reading  h_+(r,t) = v^2 = iota_t(r) = a^2 b_r(t)^2 is the TT strain
                 itself (TT-SQUARING-DECODER [D], POL-READ [D]); no matter
                 source; a second-order scalar source is supplied by a declared
                 transcription, not by variation of the quadratic action
                 (section 8).
```

Declared choices of this candidate, all visible:

| Choice | Position |
|---|---|
| Planar carrier `Z/5` with the planar rule | The three-dimensional carrier needs a discrete gradient to write `d_i d_j H_ij`; none is introduced. |
| Shift set to zero before variation | The momentum constraints are therefore absent from the system; the vector sector is not shown to be gauge (section 4). |
| Indefinite DeWitt form, prefactor `1/(2 lambda)`, `lambda = 216 pi` | Chosen so that the homogeneous quadratic coefficient matches FRW-CANONICAL-FORM; it is a selection, not a derivation of the FRW branch. |
| Nonlinear homogeneous sector = `FRW-CANONICAL-FORM` | Declared; the `e^(3 Phi)` factors, the full lapse dependence and the Friedmann identities are not derived here. |
| Second-order lattice density for `R_2(h)` in the decoder reading | Two transcriptions declared; their exact difference is now known (section 8); neither is derived from a common cubic lattice action. |
| `k != 0` equations are the flat static linearization | The homogeneous component is not solved; FRW-background equations are not derived. |

## 3. Sector decomposition [candidate-T]

Write `h_+ = (h_11 - h_22)/2`, `h_x = h_12` (TT), `tau = (h_11 + h_22)/2`
(transverse trace), `ell = h_33` (longitudinal), `h_13, h_23` (vector).
With only the axis-3 difference nonzero, exact polynomial identities give

```text
kinetic   (1/4)[ tr (Delta H)^2 - (tr Delta H)^2 ]
        = (1/2)[ (Delta h_+)^2 + (Delta h_x)^2 + (Delta h_13)^2 + (Delta h_23)^2 - (Delta tau)^2 ]
          - Delta tau Delta ell,
gradient  G_2 = (1/2) <tau, L tau> - (1/2) <h_+, L h_+> - (1/2) <h_x, L h_x>,
lapse     R_1 = 2 L tau.
```

`ell` and the vector components have no gradient energy; the lapse
multiplies only `tau`; the TT pair carries the wave form with the sign of a
physical field; `tau` carries the opposite gradient sign and a kinetic term
only through its coupling to `ell`. This is the conformal-factor structure of
the Einstein action on the lattice, and it is what the positive-definite
predecessor erased. Absence of gradient energy by itself does not prove that
`ell` and the vector components are pure gauge in this system; see section 4.

## 4. Equations [candidate-T as polynomial identities]

The seven sector equations below are certified as polynomial identities in
all 105 field variables, 15 source variables and the formal `1/lambda`
(addendum check A4), not merely at sampled configurations:

```text
(a) lapse        (1/lambda) L tau = iota/2                        [source reading]
(b) longitudinal (1/(2 lambda)) Delta^2 tau = iota/4
(c) trace        Delta^2 tau + Delta^2 ell + L tau + 2 L n = 0
(d) TT           Delta^2 h_+ + L h_+ = lambda iota,   Delta^2 h_x + L h_x = 0
(e) vector       Delta^2 h_13 = Delta^2 h_23 = 0
```

The lapse occurs only linearly in the action and its equation contains no
lapse variable (addendum A5): in the displayed quadratic action the lapse
does not propagate. That is the full content of the F2 record.

With `ell` gauge-fixed to zero, (a) fixes the nonzero modes of `tau`
instantaneously from the source, (c) fixes `n` (on nonzero modes, whenever
(a) and (b) both hold, `n = -tau`), and (b) is the consistency condition.
In the displayed system no pure-trace radiative mode survives. This is the
F3 record, and it is conditional: the system contains no momentum
constraints, because the shift was set to zero before variation. The
source-free configuration

```text
h_13(n, r) = n f(r),   f nonconstant with zero mean,   all other perturbations zero,
```

satisfies every displayed equation (addendum A7). A momentum constraint
would normally exclude an inhomogeneous vector velocity; this system does
not. The vector sector is therefore not shown to be gauge, and "TT is the
only radiative sector" is not established. Whether `ell` may be frozen is
also not established; freezing it after a failed consistency identity would
define a new candidate, not repair this one.

The coefficient census is computed (addendum A6): the action polynomial has
370 monomials and every coefficient is a rational multiple of `lambda^0` or
`lambda^(-1)`. The relative source-to-geometry coefficient that the
predecessor set by hand (`rho = 1`) is here `lambda`, by the selection of a
common prefactor. This records the selected normalization; it does not
establish a physical scalar comparison or an amplitude normalization (F5
record: no new coefficient in the selected action; physical normalization
open).

## 5. Homogeneous limit [candidate-T at quadratic scope]

For `H = 2 Phi I` constant in space (`tau = ell = 2 Phi`, TT zero, source
zero) the action equals, per site,

```text
-(3/lambda) (Delta Phi)^2,
```

the kinetic coefficient and sign of `FRW-CANONICAL-FORM`,
`S = V_0 sum nu e^(3 Phi) [ -(3/lambda)(Delta Phi / nu)^2 - rho(Phi) ]`, at
`nu = 1`, `e^(3 Phi) -> 1`. The lapse coupling at zero wave number is
`-n rho` with `rho = |e|^2/2`. The predecessor's pairing gives
`+24 (Delta Phi)^2` per site at the same place. F1 record: the quadratic
homogeneous coefficient agrees; the full nonlinear discrete FRW reduction
(`e^(3 Phi)`, full lapse dependence, Friedmann identities) is declared, not
established by this check.

## 6. The zero mode: the static flat carrier is incompatible with K1 [candidate-T]

On the compact carrier `1^T L = 0`, so the `k = 0` component of the lapse
equation (a) reads `0 = iota_hat_0 / 2`. For every K1 word and both cuts,
`sum_r iota_t(r) = a^2 > 0`. Hence the complete constraint `L tau = sigma`
has no solution on the static flat compact carrier for any K1 word in the
source reading, and likewise in the decoder reading, where the second-order
source has zero mode

```text
sum_r sigma = 53/864  (u_0 = u_1),   161/864  (|u_0 - u_1| = 1),   269/864  (|u_0 - u_1| = 2),
```

at unit `a^2`, identical for the two lattice transcriptions.

The correct statement is narrower than "C1 is forced by C2": the selected
static flat compact background is incompatible with a positive constraint
source. In the intended FRW-compatible continuation the homogeneous
contribution must be included and solved, not discarded by a projection.
The arrays of section 8 solve the projected equation and satisfy

```text
L tau - sigma = -mean(sigma) 1 != 0
```

(addendum A3); they are not solutions of the full constraint and not
initial data on a dynamic background, because that background and its
nonzero-mode constraint have not been supplied. Lapse variation alone does
not derive the nonlinear FRW branch. The obstruction is nevertheless exact
and is the concrete reason the scalar denominator of the TT program cannot
be built on this static carrier: its zero mode belongs to the homogeneous
sector that `FRW-INHOM` owns.

## 7. Source reading: conservation, and F6 fires at its tested scope

Equations (a) and (b) together imply, on every nonzero mode,

```text
Delta^2 iota = L iota,
```

the linearized conservation law of the prescribed stress in this flat sector
(energy density `iota/2`, longitudinal stress `-iota/2`). The fixed K1 word
law supplies two cuts. The continuation the law demands at either cut,

```text
iota_(-1) = 2 iota_0 - iota_1 + L iota_0,      iota_2 = 2 iota_1 - iota_0 + L iota_1,
```

is not a K1 intensity (two cyclically adjacent sites at `a^2/2`) for any of
the ten words, twenty of twenty cases; for word `0010`,
`iota_(-1) = (-209/324, 161/216, 269/216, -47/324, -65/324)`. The four
words with `iota_0 = iota_1` fail as well. Together with the zero mode of
section 6: the fixed K1 cannot be the prescribed stress source of this
flat-sector constrained system without being changed. **F6 fires for the
source reading at this scope.** The record concerns the specified flat
sector equations and the tested fixed-shape continuation; it is not a theorem
about every conserved source or about an FRW-background extension. As a
child of `TT-SOURCE` the dynamic map remains a conditional emission map; it
cannot be a constrained gravity source without a conservation law for K1,
the predecessor's own backreaction debt.

## 8. Decoder reading: the projected constrained scalar [candidate-T for the exact arrays]

In the source-free quadratic action, lapse variation gives only `L tau = 0`.
A source quadratic in `h` requires cubic terms in the action (lapse times
quadratic tensor expressions), which the displayed action does not contain.
The candidate therefore supplies the second-order constraint by a declared
transcription of `2 L tau = (K_ij K^ij - K^2)_2 - R_2(h_+)` with
`K = (1/2) Delta h`:

```text
(i)   L tau = sigma_i  = (1/4)(Delta h)^2 + (1/4) g(h),
(ii)  L tau = sigma_ii = (1/4)(Delta h)^2 - (3/4) g(h) + h L h,
g(h)(r) = (1/2) sum_k m_k (h(r) - h(r+k))^2,   sum_r g = <h, L h>.
```

Neither is derived from one common cubic lattice action; both are candidate
definitions with exact array consequences. `lambda` cancels in both.

**Exact relation between the two transcriptions** (owner review, certified as
addendum A1, A2). For this `L` and `g` the discrete product identity

```text
L(h^2) = 2 h (L h) - 2 g(h)
```

holds as a polynomial identity in the five site values. Consequently

```text
sigma_ii - sigma_i = (1/2) L(h^2),        tau_ii - tau_i = (1/2) Pi(h^2),
```

`Pi = I - 1 1^T/5`. The zero modes agree, and the full nonzero-mode
difference is known in closed form. At cut 0, unit `a^2`, it is `+3/40` at
each occupied site and `-1/20` at each empty site, for every word. The fork
is thus reduced to one specific local term. It is not thereby resolved: with
a variable lapse, `<nu, sigma_ii - sigma_i> = (1/2) <L nu, h^2>`, which is
not zero in general, so a term that sums to zero at constant lapse cannot be
dropped before local lapse variation. A fixed definition of the physical
metric and the full lapse-dependent action must decide it.

**Time placement.** The same-time sum `Z_n = sum_r sigma_i(n,r)
= (1/4)(||h_(n+1) - h_n||^2 + <h_n, L h_n>)` is not conserved by the free TT
equation: for `h_0 = h_1 = f` with `L f != 0`, `Z_1 - Z_0 = (1/4)||L f||^2
> 0` (addendum A8; for word `0101`, `14189/279936`). The conserved
staggered form uses the cross-slice term `<h_n, L h_(n+1)>`, as in the
predecessor's energy theorem. `sigma_i` is therefore not "the same
conserved discrete energy"; the constraint derivation must fix the time
placement rather than borrow the same-time continuum expression.

With those limits stated, the projected arrays are exact. On the nonzero
modes, `tau = L^+ (sigma_i - mean sigma_i)` with `L^+` the pseudo-inverse of
`L` on the mean-zero subspace, a rational symmetric circulant. At cut 0,
unit `a^2`, indices `r = 0..4`, by class `(u_0, u_1)`:

```text
(-1,-1)  ( 6951/1715360, -845/171536, 1499/857680, -845/171536, 6951/1715360)
(-1, 0)  (-77289/1715360, 47291/857680, -28957/857680, -34681/857680, 109983/1715360)
(-1, 1)  ( 25743/1715360, 5171/857680, 22559/857680, -65137/857680, 49071/1715360)
( 0,-1)  (-77289/1715360, 109983/1715360, -34681/857680, -28957/857680, 47291/857680)
( 0, 0)  ( 6951/1715360, 6951/1715360, -845/171536, 1499/857680, -845/171536)
( 0, 1)  ( 109983/1715360, -77289/1715360, 47291/857680, -28957/857680, -34681/857680)
( 1,-1)  ( 5171/857680, 25743/1715360, 49071/1715360, -65137/857680, 22559/857680)
( 1, 0)  ( 47291/857680, -77289/1715360, 109983/1715360, -34681/857680, -28957/857680)
( 1, 1)  (-845/171536, 6951/1715360, 6951/1715360, -845/171536, 1499/857680)
```

`1715360 = 32 . 5 . 71 . 151`. The arrays are translation covariant under
`u -> u + 1`. Under `a^2 -> c a^2` they scale by `c^2`.

**Moments and amplitude.** `h = Q(v)` is quadratic in the doublet, `sigma` is
quadratic in `h`, and `tau` is linear in `sigma`; so `tau` is quartic in the
doublet. For a general source family `E[tau]` uses joint moments through
degree four, `Cov(tau, tau)` through degree eight, `Cov(h, tau)` through
degree six. The complete ten-word K1 law fixes all of these on its two-window
domain, so no new probability law is needed for K1; but a general
fourth-moment specification does not by itself determine the power of a
quantity quadratic in `h`. Scaling: `h ~ a^2`, `tau ~ a^4`, `Cov(h,h) ~ a^4`,
`Cov(tau,tau) ~ a^8`; a formal ratio of these powers would scale as
`a^(-4)`. Cancellation of `lambda` is not cancellation of the physical
amplitude. No ratio is formed here, and `tau` is not a cosmological
perturbation or a `P_S(k)`.

K1's two windows are untouched. The strain beyond them is extended, where
needed, by the free TT equation (d) with zero source; this is a declared
extension, and the existence of a complete constrained continuation
compatible with it is not proved. F6 record for the decoder reading: the two
prescribed K1 windows are preserved; completion is open.

## 9. Spin structure (C4)

At the flat level the sectors are not propagated by one operator: TT pair
`Delta^2 + L`, scalar `tau` by the elliptic constraint `L`, lapse algebraic,
longitudinal and vector without gradient energy. This is a description of
the flat sector decomposition. The registered coefficient `c = 1 - s^2`
(`-3` at `s = 2`) is a Regge-Wheeler coefficient on a mass background, a
cubic-order, background-dependent statement that a quadratic flat action
cannot exhibit. F4 record: flat sector behaviour described; the registered
mass-background coefficient is untested, so the strong condition is open.

## 10. Scoped record and open obligations

```text
F1  quadratic homogeneous sign and coefficient agree; full nonlinear discrete
    FRW reduction declared, not established
F2  no lapse propagation in the displayed quadratic action (polynomial statement)
F3  nonzero-mode projected trace fixed conditionally; complete constraint
    reduction (shift, momentum constraints, global solvability) not established
F4  flat sector decomposition described; mass-background coefficient untested
F5  selected common prefactor and source normalization recorded (computed
    census); physical scalar comparison and amplitude normalization open
F6  source reading: the tested continuation leaves the K1 class (fires at
    that scope); decoder reading: two K1 windows preserved, complete
    constrained continuation not proved
```

"Does not fire in the executed check" is not "condition met". No owner
condition C1 to C5 is claimed complete. No original O/H closes. No status
moves.

Open obligations, in the order the next construction must meet them:

1. Momentum constraints. Retain the shift through variation, or supply the
   omitted constraints and prove equivalence to the gauge-fixed system. The
   witness of section 4 shows the present system does not exclude an
   inhomogeneous vector velocity.
2. One common constrained variational system through the required order,
   from which the Hamiltonian constraint, the momentum constraints, the
   longitudinal equation, the time placement of the second-order source and
   their preservation all follow. The declared transcriptions (i) and (ii)
   are replaced by whatever that action gives; the exact difference
   `(1/2) L(h^2)` and its lapse-weighted form `(1/2) <L nu, h^2>` locate the
   disputed term.
3. The homogeneous component solved as part of the initial data, not
   projected away; nonzero-mode equations on that same background.
4. Three-dimensional carrier: a discrete gradient compatible with `L`.
5. Regge-Wheeler coefficient `1 - s^2` on a mass background.

The acceptance object for the next step is a complete compatible initial-data
and constraint-propagation construction, or an exact scoped counterexample;
not another covariance table and not a renamed scalar denominator.

## 11. Reproducibility

`verify.py` was frozen and run once; its first run failed one fixture, an
expected class count written as 8 where the joint law has 9 pairs
`(u_0, u_1)`. The failed output and the unchanged source are retained
(`RUN-verify-first.txt`). The successor `verify_fixture_corrected.py`
changes only that expected count, was frozen before execution, and passed
24 of 24 exact checks. Both were rerun from the same frozen bytes on a
second architecture with byte-identical stdout.

What those 24 checks are, by kind: the sector decompositions are exact
polynomial identities; the constraint arrays are exact finite-array
equations with the assertions inside `solve_tau`; the variation check there
audits random exact configurations at two values of `lambda`, which decides
identities linear in `1/lambda` at those configurations but is not a
universal certificate; the K7/F5 line is `check(..., True)`, a declaration;
the F4 line counts distinct strings in a hand-written sector table. The
frozen files are not edited to hide this. Instead a third file,
`verify_review_addendum.py`, was frozen and run after the review; it
supplies the universal certificates the report now relies on: the symbolic
Euler-Lagrange identities in all variables (A4), the linear lapse
statement (A5), a computed coefficient census (A6), the product identity
and transcription difference (A1, A2), the projected residual (A3), the
vector witness (A7) and the time-placement result (A8). 10 of 10, two
architectures, byte-identical stdout. Hashes and environments are in
`RESULT.md`. One author, one code path; a local two-architecture record, not
the public gate.
