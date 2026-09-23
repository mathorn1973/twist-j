# Review addendum: thermodynamic Polyakov decay and finite-fit reachability

- **Reviewed item:** C-PHOTON-PRODUCTION-REACHABILITY-N
- **Author:** A. M. Thorn, drafted with an AI agent session
- **Date:** 22 September 2026
- **Scope:** PUBLIC, NON-CANONICAL review addendum; no public probe pin and no authority.
- **Scientific ceiling:** candidate-T for the elementary bound below, subject to independent review. The regression witness is exact arithmetic on rounded engineering input data, not an exact evaluation of Maxwell expectations.

The original incubation PREREG, code, transcript and terminal must be retained unchanged. This addendum distinguishes its restricted numerical terminal from stronger claims in the accompanying prose.

## 1. An exact thermodynamic bound

Consider precisely the Gaussian control used in the supplied audit: a free Maxwell field on the isotropic periodic torus of side L, with fixed finite beta > 0. Let L >= 3 and let G_L be the mean-zero inverse of the three-dimensional nearest-neighbour Laplacian. The audit's exact identity is

    E |Pbar|^2 = L^(-3) sum_r exp[-(L/beta)(G_L(0)-G_L(r))].

Then

    R_L = E |Pbar|
        <= [L^(-3) + (1-L^(-3)) exp(-L(1-L^(-3))/(6 beta))]^(1/2)
        -> 0.

This holds for every fixed finite beta > 0, not merely the scanned couplings. It does not address beta growing with L, fixed temporal extent, a compact interacting measure, or the value of the renormalized coupling of the TWIST weight.

### Proof

With the nonnegative Laplacian convention of the audit,

    (Delta G_L)(r) = 1{r=0} - L^(-3).

Let M be the maximum of G_L on the complement of the origin. A maximizing vertex not adjacent to the origin would have all six neighbours in that complement, so

    6 M - sum_neighbours G_L >= 0.

This contradicts Delta G_L = -L^(-3) there. Thus the maximum on the complement is attained at a neighbour of the origin. All six such neighbours have the same value by cubic and reflection symmetry. Evaluating the Laplacian at the origin gives

    6 (G_L(0)-G_L(e_1)) = 1-L^(-3).

Consequently, for every r != 0,

    G_L(0)-G_L(r) >= (1-L^(-3))/6.

Separate the r=0 term in the second-moment identity and bound all other terms by this inequality. Finally, Cauchy-Schwarz gives E|Pbar| <= (E|Pbar|^2)^(1/2). This proves the displayed bound and limit.

The proof, rather than a finite-volume check or the heuristic perimeter/noise interpolation, establishes the limit. The supplied review reports additional numerical checks of the Green-function inequalities at L=6,8,12,16,24,32 and the second-moment bound at beta=1/4,1/2,1,2,5. Those checks are not needed for the proof and are not claimed as a new publication replay.

## 2. Why this does not prove a finite fit unreachable

A vanishing true limit and a positive intercept in a misspecified finite-size fit are compatible. The original incubation terminal is explicitly restricted to

    B* = {1/2, 3/4, 1, 3/2, 2},
    SE_L = r R_L,

with the same relative precision r at every L. It does not quantify over arbitrary positive uncertainty profiles or all real beta <= 2. The public #757 protocol instead obtains its errors from chain-preserving data analysis.

A concrete sensitivity witness uses the original stdout's rounded beta=2 first-moment estimates:

    L    12         16         24         32
    R    0.4957806  0.3853003  0.2326458  0.1403118
    SE   0.001      0.001      0.05       0.05

Apply precisely the audit's WLS formula to y = b0 + a/L^p. The fitted intercept and inverse-information standard error are approximately

    p=1:  b0 = 0.0532175373,  SE(b0) = 0.00498680365
    p=2:  b0 = 0.2427957303,  SE(b0) = 0.00261823145.

Both intercepts are more than ten standard errors above zero. The included stdlib script `verification/review_exact_wls.py` treats the displayed means and errors as rational input and proves, with no floating-point arithmetic,

    b0 > 0 and b0^2 > 100 Var(b0)

for both fits. Hence even the conservative multiplier 10 leaves both lower bounds positive in this WLS convention.

This is NOT a public production run, NOT a full PHOTON_EVIDENCE result, NOT a demonstration that these errors would arise in a particular production chain, and NOT a fired falsifier of the original restricted incubation protocol. It shows why the prose must not upgrade that restricted result to an unconditional finite-fit impossibility statement.

The supplied table itself already disproves the sentence that both fitted intercepts are negative throughout the stated examples: at beta=2 its original M2 intercept is positive while M1 is negative. Also, its tabulated first moments are sampled estimates. The exact formula evaluates the second moment, not the first moment or the fitted intercepts.

## 3. Publication wording

Retain DESIGN_POLYAKOV_UNREACHABLE as the original protocol's terminal, explicitly scoped to its finite coupling set and constant-relative-error WLS family. State the exact thermodynamic bound separately. Remove claims of finite-size impossibility for every beta <= 2, universal transfer to every Coulomb phase, safety against all false confinement outcomes, or a guaranteed full-production terminal.

The correlator computation establishes target-shape bias in the declared Gaussian control. The supplied review reports a reproduction of max |D| = 0.18426 at L=24, n=3; the unchanged original transcript records the same value. Turning that deterministic discrepancy into a production classification still requires the frozen covariance, fit, resolution and integrity gates.

Nothing in this review edits, reopens, re-scores or authorizes #757. A changed production protocol remains a successor experiment.
