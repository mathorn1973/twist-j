# Fixed total lapse and boundary ambiguity

Status: PASS
Scope: NON-CANONICAL, NEW_DECLARED L1, scalar normal form, force a=0
Theorem status: conditional candidate-T; no Canon promotion
Fired falsifiers: none
Ownership: https://github.com/mathorn1973/twist-j/issues/1668
Preregistration pin: 02ec973ecb77655e83d69b990ba22bef05df3424

## The variational distinction

For the unchanged action and real scalar normal-form carrier, varying every
lapse independently imposes H=0, as proved by predecessor #1666. Restricting
their sum before variation changes the admitted variations: stationarity
then requires equal bond energies, already implied by matched momenta.
It imposes no fixed numerical energy. All six frozen regular histories
have positive H and satisfy the constrained lapse equations; each fails
the free-lapse equation. Thus these are distinct variational problems.

Adding Efixed times the lapse sum is constant on the constrained domain
and cannot impose H=Efixed there. The audit uses Efixed=H+1 and observes
unchanged constrained stationarity despite the residual H-Efixed=-1.
Fixing endpoint data as well as total lapse can select an energy through
the boundary problem; that is a different statement from fixing the sum
alone. A chosen energy shell is an additional classification condition.

## Complete phase and boundary classification

For fixed integer T>=3, every stationary phase history has

    z_n=M0^n exp(a_n K)z0,  a_n=sum_(b<=n)s_b.

Under the declared finite phase equivalence, theta0=thetaT=0 and
s'_b=s_b+theta_b-theta_(b-1), the complete invariant is (z0,L), where
L=sum s_b. The dressed phases exp(-a_n K)z_n=M0^n z0 are invariant.
Every real L admits a regular bond representation. This finite relation
allows regular start and end representations whose connecting phase path
crosses a configuration caustic. Under the finer continuous regular-path
relation, ordered interval components of the bond-regularity domain are
additional complete labels. No finite count of those sectors is claimed.

Write the composite transfer as M0^T exp(LK), with blocks U_T,B_T.
For fixed configuration endpoints q,Q the initial momentum solves

    B_T p0=Q-U_T q.

If this is inconsistent there is no orbit. Otherwise let pstar be its
minimum-norm solution and k=dim ker B_T. All orbits are p0=pstar+w for
w in ker B_T. On an additional real shell H=Efixed, put

    rho^2=2Efixed-q^T Dq-||pstar||^2.

For k=0 there is exactly one orbit when rho^2=0 and none otherwise.
For k>0, negative rho^2 gives none, zero gives one, and positive rho^2
gives the sphere S^(k-1). This is a complete real classification for the
declared finite phase relation, not a count of rational points.

When B_T is invertible, the stationary sum of bond actions is its quadratic
generating function Ftot. Its parameter derivative at fixed q,Q is -H.
The unchanged endpoint term contributes Vq/2 and VQ/2 to the endpoint
gradients and leaves the mixed response -B_T^-1 unchanged. At T=3,L=0,
B3=(I-V)(3I-V) is invertible with five positive and one negative eigenvalue;
positivity of this boundary form is not assumed. The six regular fixtures
recover the unique initial momentum and actual stationary action exactly.

## A complete two-orbit example and its limits

At T=3,L=-3,q=Q=0,Efixed=5/2, the proof gives
ker B_3(-3)=span(v), v=(1,1,1,1,1,0). The real energy shell therefore
has exactly two finite phase orbits, with p0=+v and p0=-v. The three
lapse arrays (-3,0,0), (0,-3,0) and (0,0,-3) are individually regular.
Their six frozen rational histories have zero bond action and energy 5/2.
Redistributing the lapses relates the three histories of each sign;
opposite signs remain distinct because initial phase is invariant.

These examples require negative lapses and the uniform spatial mode.
They establish no two-orbit claim for positive lapses, for the mean-zero
sector, or for the finer continuous regular-path equivalence. The finite
audit evaluates only the exact uniform shear. The full kernel and global
completeness conclusions rest on the analytical proof, without numerical
evaluation of a finite nonuniform exponential.

## Exact finite audit

Both separately authored standard-library rational implementations produced
identical unmodified certificate bytes. The frozen audit completed:

| Audit | Count per implementation |
| --- | ---: |
| Normative authority files | 5 |
| Formal coefficients, degree 0 through 4 | 5 |
| Composition coefficient pairs | 15 |
| Regular endpoint cases | 6 |
| Constrained regular lapse variations | 18 |
| Nonzero free-lapse witnesses | 6 |
| Transformed phase series | 24 |
| Transformed bond and momentum series | 18 |
| Actual transformed action series | 6 |
| Uniform caustic histories | 6 |
| Distinct finite phase orbits in the caustic fixture | 2 |
| Deliberate defects detected | 8 |

Each series includes five exact coefficients. Actual transformed bond
actions and their momenta were calculated before comparison; predicted
zeros were not substituted. The payload has 189 records and SHA-256
`781e893677fc8a734e063c1be0af2776d7f56adfed80531e77f702ebde8a8c6c`.
EXPECTED.txt contains the 461-byte, 18-line stdout. RUN.md records the first
completed run. At this record the two required architecture replays remain
pending; the pull request records their outcome for the exact result head.

## Consequence for the gravity program

The scalar model admits positive-energy motion under the declared fixed-sum
boundary condition, and its residual endpoint ambiguity is classified.
Neither the equivalence relation nor a chosen energy shell supplies a
physical preparation or occurrence rule. Lapse redistribution still acts
on fixed linear phase dynamics. No nonlinear gravitational interaction,
physical clock, metric selection, native-U realization, continuum limit
or unnamed cross-layer lift follows.

The free-lapse result, earlier failures and abandoned pins remain intact;
separately owned #1659 is not resumed. Canon, registry, policy and workflows
are unchanged. A physical continuation needs a declared observable and
preparation or selection criterion beyond the scalar redistribution.
