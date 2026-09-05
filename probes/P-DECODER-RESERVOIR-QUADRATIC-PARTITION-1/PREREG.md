# P-DECODER-RESERVOIR-QUADRATIC-PARTITION-1 preregistration

**FROZEN TARGET / NO FORMAL RUN AT PIN / PUBLIC STATUS NONE.**

Disclosure: **CHOICE-EXPLICIT / PROOF-FIRST / L1 ONLY.** The old source
was designed with its QDD norm match exposed. The new target comparison
does not make that source or its coupling physically selected.

```text
owner: A. M. Thorn
issue: https://github.com/mathorn1973/twist-j/issues/827
branch: probe/P-DECODER-RESERVOIR-QUADRATIC-PARTITION-1
base: 4e794a01aec719a4536f2028ecbfd2f876a19e2b
authority: ACTIVE Public Canon v76
claim_A: DECODER-RESERVOIR-QUADRATIC-PARTITION
claim_B: DECODER-RESERVOIR-QDD-POSTPROCESSING-OBSTRUCTION
formal runs at pin: 0
public status: NONE
```

## 1. Equation and two conditional targets

Keep the finite-support rational D3 wave, fixed five-shell stencil, pair
energy `E` and centered five-site source `Bz=(0,Sz)` of the completed
transport result. Let `G=I_4-e e^T/5`, `e=(1,1,1,1)^T`, so
`2E(Bz)=z^T G z`. Source preparation finishes before coupling starts.
For fixed finite rational nonnegative conductance, extended by zero, use
the completed cold port law

```text
w_x=[2v_x-(Lv)_x-(1-gamma_x/2)u_x]/(1+gamma_x/2),
b_x=-(w_x-u_x)/2=[2u_x-((2I-L)v)_x]/(2+gamma_x),
E(v,w)+sum_(x in R) gamma_x b_x^2=E(u,v).
```

For every finite horizon n, each outgoing value is a linear row in z,
`b_(t,x)(z)=ell_(t,x) z`. Define from the actual port and final wave

```text
M_(t,x)=2 gamma_x ell_(t,x)^T ell_(t,x),
z^T R_n z=2E(P_n(z)).
```

Claim A is the conjunction:

1. All matrices are symmetric rational positive semidefinite and
   `sum_(t<n,x in R) M_(t,x)+R_n=G` for every admitted context and finite n.
   The residual is constructed independently from final-wave energy, not
   defined as the difference `G-sum M`.
2. Prefix rows agree, residuals obey the one-step accounting identity,
   and preselected disjoint complete grouping of port slots, retaining the
   residual, yields another positive partition of G.
3. On nonzero z, its normalized quadratic shares are nonnegative, sum to
   one and are invariant under nonzero rational source scaling. Zero has
   an explicit undefined-normalization disposition. With
   `F_j=G^(-1)M_j` and `rho_z=z z^T G/(z^T G z)`, positivity and
   self-adjointness are in the G metric, `sum F_j=I` and
   `tr(rho_z F_j)=z^T M_j z/(z^T G z)`. Ordinary Euclidean symmetry is not
   asserted. Threshold floors are a different, source-scale-dependent read.

Claim B assumes an active origin port, `gamma_0>0`, and `n>=1`. Its complete
postprocessing class consists exactly of one state-independent coefficient
`a_j in [0,1]` per fine port slot and the residual, with outputs
`sum a_j M_j` and `sum (1-a_j) M_j`. Coefficients may be real and depend
on fixed context/horizon but not on source or output. No outcome is omitted.
The claim states that no such processing agrees with both algebraic targets

```text
L_QDD=e e^T/20,            H_QDD=I_4-e e^T/4
```

on both balanced sources `(1,-1,0,0)` and `(1,1,1,1)`, hence none agrees on
all Q^4. The first origin row is

```text
h=(1421,-349,-349,-349)/1620,
ell_(0,0)=-h/(2+gamma_0),
M_(0,0)=2 gamma_0 h^T h/(2+gamma_0)^2.
```

The HIGH witness forces its LOW coefficient zero; the LOW witness forces
the same coefficient one. Nonnegativity forbids cancellation. PROOF.md
proves both claims uniformly; finite exact gates audit the implementation.
The obstruction includes deterministic coarse-graining and pre-grouping,
but not nonlinear/source-dependent rules, coherent processing before
squaring, changed interactions, postselection with renormalization or all
physical apparatuses. No physical F result is targeted.

## 2. Accepted code and immutable sources

The six new source files are frozen together:

```text
PREREG.md  PROOF.md  README.md
partition.py  audit_partition.py  verify.py
```

There are exactly two existing executable source dependencies:

| Path | Original source pin | SHA-256 | Bytes |
|---|---|---|---:|
| `probes/P-DECODER-RESERVOIR-COUPLING-1/coupling.py` | `550420d188a45c4929e300ca6aabcde812f4d65a` | `54f8b03762639e2573f02210b07e0d19b28935c2bc68c7f5988b15efbe26d403` | 7966 |
| `probes/P-DECODER-RETARDED-ENERGY-TRANSPORT-1/transport.py` | `30ab237b4dcb339115517f67b883ca4cc3e00c32` | `983d22690e061128d287f23ef4672fbd72954faa28f1a3fde9ce38b0d6660a60` | 11353 |

The source loader enforces immutable dependencies and imported origins.
The accepted verifier additionally pins its own implementation/audit and
proof bytes. PREREG and README are bound by the complete candidate commit
and public readback. No previous probe is changed, copied wholesale,
renamed, resumed or used outside its earned conditional scope.

Before any scientific execution or import, commit and push the complete
candidate and read back all eight source files byte for byte. Static
inspection and compilation are allowed first. The sole initial formal
command, from a clean Linux repository root, is

```text
python3 probes/P-DECODER-RESERVOIR-QUADRATIC-PARTITION-1/verify.py
```

Only standard-library exact integers, Fractions, tuples, byte hashing and
local immutable sources are used. There is no external dataset, physical
measurement, network, subprocess, random seed, floating tolerance or fitted
input in the scientific program. Administrative pin/readback/run capture
tools are outside it.

## 3. Carrier, equality and frozen finite audit

The uniform domain is `z in Q^4`, finite positive rational Gamma on D3
ports, and `n in N_0`; empty Gamma is admitted. Canonical finite fields omit
zero entries. Pair order, source sites, operator weights and energy density
are precisely those of the unchanged inherited modules. All matrix and
port-slot equalities are literal. No phase or physical-record quotient is
introduced. Gamma, horizon and grouping are fixed before reading sources
or comparing their output. Threshold q is positive rational and is inert
for partition construction.

Generated partitions retain every site/time slot, including zero rows.
The residual is a separately labelled component. Grouping indices must
give a disjoint exhaustive partition of the port slots; they never swallow
or discard the residual. The claim concerns generated partitions, not
unvalidated forged dataclass contents.

The finite audit uses a maximal horizon of three with every prefix 0..3
for these four contexts, where o=(0,0,0), p=(1,1,0):

```text
Gamma empty;
Gamma={o:2};
Gamma={o:1};
Gamma={o:2,p:1/2}.
```

The independent reference builds the five-shell stencil and centered source
itself, applies a separately written pointwise recurrence to the four basis
sources and their six pair sums, and reconstructs quadratic forms by energy
polarization. It does not call production propagation or define its residual
by conservation. This compares two constructions, not two wrappers around
the same energy difference. Exact principal-minor checks audit positivity
of the four-dimensional matrices; finite sample positivity is insufficient.

The eight frozen gates are:

```text
G01_TYPES_ZERO                   exact domain rejection and zero normalization;
G02_INDEPENDENT_PROPAGATION       independent source/stencil/port row agreement;
G03_RESIDUAL_PARTITION_PSD        direct residual energy, positivity and sum G;
G04_PREFIX_GROUPING              earlier slots, residual identity and grouping;
G05_G_METRIC_TRACE               metric, normalization and exact trace formulas;
G06_FIRST_PORT_ROW               h row, conductance factor and both witnesses;
G07_POSTPROCESSING_OBSTRUCTION   positivity and contradictory coefficients;
G08_THRESHOLD_BOUNDARY          exact floor boundary versus invariant shares.
```

Claim A requires G01..G05 and G08. Claim B conservatively requires all eight
gates, including the underlying partition controls. Literal finite cases
and exact additional type/scaling/threshold controls are fixed in the
accepted audit source. Their frozen values cannot be changed after the pin.
All four propagation contexts use q=1. G05 evaluates the unit source,
the two balanced LOW/HIGH witnesses, and `(1/2,-2,1,-1/3)`. G08 uses the
one-step origin-gamma-2 partition with `z=(1,-1,0,0)`, its scaled source
`3z`, exact heat `3481/23328`, q=1 floor counts zero and one respectively,
and an independent threshold change to q=7 that leaves the partition
unchanged. G04 compares singleton, pooled and site-grouped slot partitions.
No finite gate is represented as an exhaustive enumeration of all rational
contexts, horizons or real postprocessing coefficients; the proof supplies
those quantifiers.

## 4. Systematics and exposed choices

The five source sites and norm match, rational scalar wave, conductance
coupling and fresh cold slots are inherited choices. The sampled contexts
do not establish physical target independence or physical parameter values.
Different Gamma values are different mathematical contexts, not free
selectors to be adjusted after inspecting a target.

The matrix convention includes the factor two from `2E_initial=m`; a port
deposit is `gamma b^2` while its matrix is `2 gamma ell^T ell`. Energy
shares therefore divide heat by E_initial. The residual is measured on the
whole final finite-support wave and its energy halo, not only at the port
sites. No finite spatial box or boundary wrap is substituted.

Both matrix routes retain exact zeros and all sites needed by the stencil.
Positivity is checked algebraically, never by decimal eigenvalues. The
G-metric operators need not be ordinary symmetric matrices. A zero source
does not have a normalized Born vector. No-deposit or no-crossing is not
identified with zero source, complete absorption or physical nonexistence.

The current proof does not erase residual energy, sum two representations
of the same energy, or transfer signed tape labels to A/U5 residual tokens.
No wave, source or U update depends on heat, threshold counts or target
LOW/HIGH weights. This probe supplies no occurrence or ensemble law.

## 5. Failure thresholds and disposition

Every threshold is **zero exceptions / exact equality** at the frozen
scope. A scientific assertion failure emits the named gate FIRED, the
affected claim outcome and terminal SCIENTIFIC-FIRED with exit zero and
deterministic exact stdout. All gates are attempted, and a fired result
must be preserved and merged. The claim-gate routing above is fixed.

An unexpected execution or integrity error is not a scientific result.
If the formal gate cannot complete its record, this identifier is consumed
under the abandoned-pin rule; it must not be resumed, renamed or repaired.
Any replacement requires a new ID and new preregistration. A completed
scientific failure is never relabelled abandonment.

After execution, preserve exact stdout as EXPECTED.txt and record the pin,
all source hashes, neutral platform/architecture, command, exit, stdout and
stderr bytes/hashes and line endings in RUN.md. RESULT.md states exactly
the earned claim scopes. The ordinary required workflow independently
replays the one changed probe on x86_64 and aarch64. No source file is
changed after the pin. One probe per PR; no squash, rebase, amend or force
push. Public registration is a separate earned Canon fold.

## 6. Action layer and physical firewall

The complete attack is **L1 encoded rational mathematics**. The
Born-shaped trace identity is not a physical effect, instrument or
probability claim. The negative theorem concerns only the specified
postprocessing class, not physical apparatus-family completeness or the
Born rule. Warm reservoirs, adaptive horizons, nonlinear/source-dependent
processing and altered source/coupling families remain outside scope.

The physical-profile proposal under #539, source/clock and context
determination, pointer and event equality, terminality/COMM-SAT, complete
physical apparatus classes, post-state instruments, occurrence/sampling,
Bell accounting and all new L1-to-L5/L6 lifts remain unresolved.
COINCIDENCE-RECORD-FREQUENCY stays candidate-H / UNTESTED / STOP.
The photon #744 pole/polarization contract and #756 F3 NOT_SATISFIED remain;
production #742 stays FORBIDDEN.

**PUBLIC CLAIMS UNREGISTERED / CANON UNCHANGED.**
