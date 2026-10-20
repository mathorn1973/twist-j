# Result: conditional temporal-locality obstruction

Status: PASS
Scope: NON-CANONICAL, NEW_DECLARED L1
Analytical classification: conditional candidate-T, pending repository review.
Finite audit at packaging: completed on x86_64; the PR's exact-head checks
separately record the required x86_64/aarch64 replay.
Fired falsifiers: none.

## What was established

Within the precise class frozen in PREREG.md, no second-order correction
can have a temporal multiplier range bounded independently of the horizon.
The class keeps the inherited zeroth- and first-order transformations,
allows any homogeneous quadratic multiplier correction with arbitrary
field-dependent coefficients, and permits any everywhere-defined finite
second-order physical-field variation. That variation must leave the
auxiliary fields and multipliers unchanged. The identity must hold for
every admitted state, horizon and rational endpoint pair, with endpoints
fixed during variation.

The proof constructs an exact autonomous zero-mean history and a single
current multiplier. On it the physical-field gradient vanishes but the
first-order interaction variation is

    delta1 I=-(29/648)t_k.

The mixed alpha_b/N_(k,0) coefficients of any proposed correction must obey

    C_b-C_(b+1)=(29/648)delta_(b,k).

Every solution is a temporal step plus a common constant. At least one
entire tail reaches an endpoint. The sharp minimum radius for this
necessary coefficient system is min(k-1,T-k). It grows without bound for
interior k as the horizon increases. This is an analytic conclusion for
all horizons, not an extrapolation of the finite test cases. Sharpness of
this coefficient condition is not sufficiency for a full correction.

The actual inherited prefix correction realizes the left tail. Its long
range is thus required within this class, rather than being explained only
as an unfortunate choice of the particular prefix construction.

## Completed exact audit

The first formal execution followed public pin
`6c257b169054625aa608974c1c6a264fb56e5d02` and six-file byte readback.
Primary and separately written breaker agreed on the unmodified raw
certificate. The primary uses exact central polynomial differences and
affine tail propagation. The breaker uses exact dual differentiation,
an independently assembled action Hessian and full rational row reduction.

| Check | Count | Outcome |
|---|---:|---|
| Normative file hashes and sizes | 5 | PASS |
| Autonomous zero-mean histories | 22 | PASS |
| Residual components | 1200 | Exact zero |
| Independent action derivatives | 1200 | Equal negative residual |
| Current parameter variations | 244 | Exact predicted value |
| Actual prefix mixed coefficients | 222 | Required left tail |
| Locality-constrained linear systems | 222 | Exact predicted feasibility |
| Plateau contradictions | 22 | Detected |
| Positive auxiliary escapes | 22 | Exact cancellation |
| Integer residual components | 1200 | Exact zero |
| Integer Ward witnesses | 244 | Exact zero |
| Negative controls | 8 | All defects detected |

The stdout has 508 bytes and 19 lines, SHA-256
`d37addee43da071da1e4aa702b2408b9b5dd4b8fed38a5666a84bb3b8d3d825a`.
The underlying canonical payload digest is
`d6694aaf3c4191fabb4b11fd58fc530350ce647cb8eb3735c68727c67ed1f25a`.
The process exited zero with empty stderr. RUN.md and EXPECTED.txt preserve
the completed output. The frozen six files are unchanged.

## Boundary and next admissible question

The same witness admits a local cancellation if the restriction on the
auxiliary sector is relaxed: delta2 tau_k=ell/8 contributes +29/648.
That positive check is separate from the eight negative controls. It is
not an all-state transformation law, a closed algebra or a full completion.

The result neither excludes all local gauge theories nor contradicts the
separately owned local-parent construction in #1659. It establishes no
new nonlinear bulk law, selected metric, physical clock, native-U action,
Einstein dynamics or layer lift. The public Canon and registry are unchanged.

A meaningful successor would freeze a genuinely local auxiliary-transforming
law, test its Ward identity on the full off-shell domain, and then test
algebra closure and reduced bulk dynamics. It would have to distinguish a
change of coordinates or gauge packaging from new physical dynamics. This
result identifies that question without claiming its answer.
