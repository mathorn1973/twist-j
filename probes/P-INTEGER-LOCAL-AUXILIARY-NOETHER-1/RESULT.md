# Local auxiliary Noether completion

Status: PASS
Scope: NON-CANONICAL, NEW_DECLARED L1, a=0 and E_hom=0
Theorem status: conditional candidate-T; no Canon promotion
Fired falsifiers: none
Ownership: https://github.com/mathorn1973/twist-j/issues/1663
Preregistration pin: 45648ac0d495a55a6c76e90dfd0fe56e042bf224

## Result

Allowing the existing constrained auxiliary fields tau and p to transform
removes the predecessor's field-only locality obstruction at second order.
On the complete declared rational carrier, the frozen S2 is homogeneous
quadratic in multipliers, has temporal multiplier-pair radius at most one
independent of the horizon, and satisfies the off-shell second-order
Noether identity with the stated raw transformations. The skew
Euler-gradient correction preserves that identity and makes all
commutator coefficients through order two vanish off shell.

These are universal conditional identities proved in PROOF.md for every
T>=3, every rational endpoint pair held fixed under variation, every
admitted state and arbitrary endpoint-zero parameters. The fixed five-site
spatial inverse is permitted by the contract. No temporal prefix or inverse
of a horizon-sized matrix is used. No auxiliary coordinate is added.

## The raw obstruction remains explicit

The raw transformations preserve the action to the declared order but
generally fail to commute off shell. Their exact order-two field bracket is

    Craw_n=[(s_n t_(n+1)-t_n s_(n+1))R_(n+1)
           +(s_n t_(n-1)-t_n s_(n-1))R_(n-1)]/4.

It is an antisymmetric multiple of the Euler gradient, vanishing on shell.
At the frozen T=4 witness the slice1 coefficient is
(-1/4,0,1/4,0,0,0). The adjusted coefficient is zero; reversing the
adjustment gives twice the raw coefficient. At alpha=0 the adjustment
vector itself vanishes, but its multiplier derivative cancels the bracket.
The passing result does not erase this raw nonclosure.

## Exact finite audit

Two separately authored standard-library programs agree on the complete
canonical payload certificate without normalization. Their arithmetic
methods differ: exact central polynomial differences in the primary,
product-rule derivatives, dual arithmetic and an independently assembled
action Hessian in the breaker.

| Audit | Completed cases per implementation |
|---|---:|
| Dense off-shell states, horizons 3,4,5,7 | 12 |
| Lower-order identities | 237 |
| Scalar second-order Ward identity | 237 |
| Raw full second-order Ward identity | 237 |
| Adjusted full second-order Ward identity | 237 |
| Zero skew work and tangent admissibility | 237 each |
| Actual raw/adjusted commutator pairs | 237 |
| Distant multiplier polarizations | 900 |
| Denominator-cleared integer Ward identities | 237 |
| Deliberate defects detected | 8 |

Payload SHA-256:
`2d06df6788972c5bf4c9476036d81dea1c991d3822fa7b2e0ca2c176ba94e091`.
Exact scientific stdout is EXPECTED.txt; first-run custody is RUN.md.
The finite cases audit the universal derivation rather than replace it.
At this first-run record, cross-architecture acceptance is pending the
required x86_64 and aarch64 pull-request jobs on this unchanged verifier
and output.

## Interpretation and remaining question

The construction is formally equivalent through order two, on the same
carrier, to scalar-lapse autonomous mechanics plus algebraic auxiliary
pairs. The multiplier change is invertible as N=BZ+Q and lambda=l+Delta Z.
For y=(I-epsilon G_Z)x, the formal inverse is
x=(I+epsilon G_Z+epsilon^2 G_Z^2)y modulo epsilon^3; the auxiliary shifts
in PROOF.md are reversed algebraically. This uses the identity leading
term and does not assert invertibility at finite epsilon. The inverse's
stencil can grow with perturbative order.

Accordingly this result supplies a local consistency completion, not a new
gravitational bulk law. It does not establish orders three and higher,
exact symmetry at epsilon=1, physical trajectories or their preparation,
positive-energy or Lorentzian admissibility, a physical clock, metric
selection, native-U dynamics, or any cross-layer lift. Spatial locality on
an expanding lattice is also outside scope. Stationarity at E_hom=0 has
not been used to infer any nontrivial physical history.

The next scientific distinction is whether a proposed further completion
adds a physical invariant beyond this formal coordinate representation,
with explicit preparation and equivalence criteria. Higher-order algebra
alone cannot establish such physical novelty.

The predecessor #1662 remains valid in its field-only class. This probe
deliberately changes that premise; it repairs no frozen predecessor. The
separately owned prospective #1659 and the earlier failed/abandoned records
are unchanged. Canon, registry, policy and workflows are unchanged.
