# P-QDD-PASSIVE-QUADRATIC-CALIBRATION-1

Owner: A. M. Thorn, assisted by the Codex passive-quadratic session,
2026-09-16. Public reservation:
[issue #1023](https://github.com/mathorn1973/twist-j/issues/1023).

The baseline is Public Canon v87, authority `mathorn1973/twist-j main`,
at public main commit `fd512f50d90382124e7c00afa926c8083fd56e06`.
The declared Canon content commit is
`41c8d4229b71437f09957d959975dc1772e95806`, tag `canon-v87`, with
CANON.md SHA-256
`a2517c6d8efb1969a7258f94d9874cca3b5b9beb1aecdfd2e39b56f33961a917`
and 634207 bytes. The coordinating session confirmed public authority and
the work reservation before preparing this package.

This fresh public probe follows disclosed non-canonical exact explorations
of the same source class, response rows, determinant and error formula.
These earlier calculations informed the proposed formulas and design;
they are not blind or empirical preregistration, executions of this probe,
or substitutes for its public pin. There is no empirical dataset here.
The proposed origin prediction omits the origin from its algebraic input
list; the term held-out does not claim unseen experimental validation.

## 1. Equation

For `u=(1,1,1,1)^T`, `chi=(1,-1,-1,1)^T`, `G=I-uu^T/5`, fix
`P_t=uu^T/4`, `P_l=chi chi^T/4`, `P_r=I-P_t-P_l`. Write
`T=GP_t`, `L=GP_l`, `R=GP_r` and their atom weights as

```
t=(sum z_i)^2/20,
l=(z0-z1-z2+z3)^2/4,
r=((z0-z3)^2+(z1-z2)^2)/2.
```

The proposed single theorem `QDD-PASSIVE-QUADRATIC-CALIBRATION` has these
explicitly bounded clauses:

- A rational symmetric homogeneous quadratic `z^T A z` factors through
  the existing finest coherent PI-ATOMS record on Q^4 if and only if
  `A in span_Q(T,L,R)`. The same equivalence holds on the actual balanced
  head grid Z. The proof gives seven necessary coefficient constraints
  using coordinate vectors and pair sums, and their exact converse.
- For arbitrary preparation probability vectors on Z, knowledge of the
  entire passive-record law requires at least seven additional fixed
  rational scalar expectations to identify every homogeneous quadratic
  mean. Seven suffice. The lower bound includes arbitrary scalar functions
  and is explicitly about universal ensemble expectation prediction, not
  deterministic decoding or a single target.
- In the stated five-site centered source and sixty-displacement cold
  reservoir model, gamma=1 first-step deposits at the seven frozen sites
  in PROOF.md complete the three atom forms to rank ten. The scaled integer
  determinant is exactly
  `-176542678173169038600000000000000000`.
- The unscaled held-out origin deposit obeys the exact ten-coefficient
  identity in PROOF.md. Its sharp unrestricted additive error gains are
  `A=84944136907/246938981400` for the atom group and
  `B=751911453/185050550` for the deposit group. A held-out comparison adds
  its own error allowance. The last deposit coefficient is zero, so the
  universal seven-reading minimum must not be attributed to this one target.
- Sources e0,e1 have identical finest records but the exact origin deposits
  `2019241/23619600` and `121801/23619600`, giving first-step counts one
  and zero at q=1/16. This audits persistence of the inherited source
  collision under the newly selected finest reading.

PROOF.md freezes the complete matrices, source sites, shell weights,
coefficient order, ten rational prediction coefficients, record equality
and source/zero conventions. No fitted coefficient or adjustable tolerance
is used. All seven verifier checks belong to this one proposed theorem.

## 2. Code

The accepted exact verifier is
`probes/P-QDD-PASSIVE-QUADRATIC-CALIBRATION-1/verify.py`. It is standalone:
Python standard library only, exact integers and `fractions.Fraction`, no
external package, imported scientific module, runtime Canon parsing,
external fixture, cached result, network access or file mutation. Its
mathematical input is the explicit public code and proof, not a local path.

PREREG.md, PROOF.md and verify.py are committed and pushed before the first
formal gate execution. The subsequent run record names the pin and exact
file hashes; this file does not invent a completed pin or run in advance.
Compilation and static review are allowed beforehand. No execution of this
new verifier or its gate functions is allowed before that pin.

Formal command from the repository root:

```
python3 probes/P-QDD-PASSIVE-QUADRATIC-CALIBRATION-1/verify.py
```

The verifier rejects optimized Python, emits deterministic LF scientific
stdout and includes no timestamps or machine-dependent values. A complete
successful run exits zero with empty stderr. Both required architecture
jobs must match the same committed EXPECTED.txt byte for byte. Actual run
environment, hashes, byte counts and exit status are recorded only after
execution. The independent proof supplies the universal statements; finite
execution audits their implementations and exact certificates.

## 3. Carrier or data

The inherited decoder domain stays K_QDD with its existing balanced head
map, whose image is `Z={-2,-1,0,1,2}^4`. The Q^4 theorem is an algebraic
extension for proof, not a new decoder-domain adoption. All 625 balanced
vectors, including zero, are audited; the unused head coordinates add no
argument to this reading. Ensemble probability vectors are stipulated
mathematical inputs, not inferred occurrence laws or physical measures.

The fixed source sites are `(000),(110),(101),(011),(200)`. Its centered
coefficients are `(z,0)_j-sum(z)/5`. The full stencil shells have squared
norms `(2,4,8,10,16)` and per-displacement weights `(6,1,15,1,1)/324`.
The seven calibration sites are
`(110),(101),(011),(200),(-1,-1,0),(-1,0,-1),(-1,0,1)`; the separate
validation site is the origin. All use first-step cold gamma=1 response.

| Gate | Frozen inventory and target |
|---|---|
| G01_FACTORABLE_QUADRATICS | Three atom forms; coordinate and pair-sum record equalities; three coefficient-basis identities for the d,a,b converse |
| G02_FULL_PASSIVE_LAW_DIMENSION | All 625 finest records; every equal-record monomial difference; constraint rank 7, quadratic rank 10, constant-plus-quadratic rank 11 |
| G03_INDEPENDENT_SPATIAL_RESPONSE | Two independent constructions of the 60 stencil displacements; 8 response rows; 4 basis preparations at 8 sites, each with signed amplitude and deposit comparison |
| G04_SEVEN_PORT_BASIS | Seven distinct off-origin ports; exact integer determinant and independent rational rank 10 |
| G05_HELD_OUT_IDENTITY | Exact solved coefficients; all 10 polynomial coefficients; all 625 balanced sources |
| G06_ADDITIVE_ERROR_CERTIFICATE | Exact two-group and common coefficient gains; unrestricted-box sign attainment, including zero group radii |
| G07_FINEST_RECORD_COLLISION | Identical five-field records at e0,e1; exact unequal deposits and threshold counts |

No empirical or external dataset is used. No distribution is chosen by
matching a measured target. The identity for all ensembles follows from
pointwise polynomial identities and the separate finite-function-space proof.

## 4. Systematics

- Keep source projectors P separate from quadratic coefficient forms GP.
- Keep all five coherent record fields and literal PI-ATOMS ID; normalize
  only by positive total and preserve the exact zero branch.
- Full passive-law calibration means the probabilities of all record
  fibres, including zero. It is stronger than merely three atom means.
  The dimension proof includes constants and hence normalization.
- Seven is the minimum for every quadratic mean under arbitrary ensembles.
  This is not a lower bound for one deterministic head or one omitted port.
- Extra calibration functions remain separate functions; no sixth passive
  record field, source argument or feedback into U is introduced.
- The source injection, stencil, conductance, cold inputs, first-step age
  and stipulated preparation law remain choices. Later contexts require
  their own evolution forms. First-step inter-port coexistence does not
  establish a later context equivalence.
- The prediction coefficients multiply unscaled physical-model weights,
  not the scaled determinant rows. The exact scaling is stated explicitly.
- Sharp error gain concerns an unrestricted additive error box only.
  Geometry, conductance, source calibration, finite sampling and correlated
  errors are not controlled by that coefficient sum.
- The old e0,e1 collision is not presented as newly discovered. Its retention
  under the now selected finest record is the bounded new comparison.
- Quadratic expectation sufficiency supplies neither full distribution
  identification nor a general threshold-count or frequency law.
- Prior non-canonical exploration is disclosed. No empirical blinding,
  preregistered experimental design or physical measurement is claimed.

## 5. Failure threshold and dispositions

One admitted exact failure of a frozen factorization identity, finite-grid
dimension, response coefficient, determinant, reconstruction coefficient,
error-gain equality or source distinction fires the corresponding clause.
An exact ensemble counterexample to the proved universal calibration bound
at the frozen scope likewise fires it. The threshold is zero tolerance.
There is no floating-point approximation, fitted parameter, post-execution
threshold adjustment or scope relaxation.

The verifier records all completed scientific assertions as PASS or FIRED,
then emits the corresponding aggregate disposition. A completed scientific
failure is retained and reported. Authority, missing pin, code custody,
disabled assertions, unexpected runtime failure or incomplete execution are
STOP conditions, not scientific success. A code defect producing no complete
gate output yields no completed scientific conclusion; disposition follows
the repository's abandoned-pin policy when applicable.

## 6. Action layer

All asserted objects and equalities are L1 conditional algebra and finite
ensemble identifiability. The proof may support the proposed single T row
`QDD-PASSIVE-QUADRATIC-CALIBRATION` after ordinary review. A separate public
fold would be needed for any Canon change; this probe makes none itself.

The existing passive-family D selection, K_QDD domain and ALGEBRAIC-DMATTER
binding remain unchanged. The source/coupling remains a conditional encoded
model. No physical preparation, port, clock, effect, instrument, pointer,
event semantics, reset, occurrence law, independence, empirical frequency
or cross-layer L1-to-L4/L5/L6 bridge is supplied. The three physical QDD
obligations remain open, with no claimed partial closure.
