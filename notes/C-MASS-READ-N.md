# C-MASS-READ-N

**Status:** NON-CANONICAL INCUBATION NOTE  
**Authority:** none  
**Public basis:** Public Canon v39  
**Issue lock:** #297  
**Date:** 2026-08-07  
**Owner:** A. M. Thorn  

This Note opens a falsification-first research program around mass reading. It does not add a Canon claim, does not change any registry row, does not authorize a formal probe, and does not treat the present mass formulas as true premises.

The core question is narrower than "derive the proton mass" and broader than "fit the remaining proton residual":

> Does the registered TWIST-J architecture force a common physical reading mechanism for mass ratios, with species-dependent outputs but no target-dependent choices, and is any part of that mechanism tied specifically to the gravity channel rather than to phase reading?

A negative answer is a valid result. The current mass ladder may be partly right, wrongly interpreted, or wrong at its seed.

## 1. Public boundary at v39

The Note starts from the current public status separation, not from older internal Canon language.

The relevant public rows are:

```text
MASS-LADDER-FORMS          [D]
MU-TAU-COEFFICIENT         [T]
MU-EXCHANGE-IDENTITY       [T]
ALPHA-FORM                 [D]
ALPHA-VALUE-DIGITS         [C]
PROTON-RESIDUAL-IS-QCD     [O]
SCHEME-DICTIONARY          [O]
DRESS-CROSSCOUNT           [O]
METRO-EDGE-SCALE           [O]
QUADRATIC-DECODER-DATA     [O]
```

The distinction is binding.

`MASS-LADDER-FORMS [D]` is a committed physical reading and may be attacked. Its failure would not by itself falsify the exact mathematical statements `MU-TAU-COEFFICIENT [T]` or `MU-EXCHANGE-IDENTITY [T]`.

`PROTON-RESIDUAL-IS-QCD [O]` already owns the exact intrinsic/QCD derivation class. This program does not duplicate or redefine that row. It treats it as one competing origin branch.

`SCHEME-DICTIONARY [O]`, `DRESS-CROSSCOUNT [O]`, `METRO-EDGE-SCALE [O]`, and `QUADRATIC-DECODER-DATA [O]` own their current scopes. No branch below may silently close, narrow, or bypass them.

Issue #107 owns the typed quadratic `D_matter` completion lane. The Pauli program in #295 and its branch-A claim #296 own separate spin/statistics work. This Note does not compete with either lane.

## 2. Preparation exposure

This incubation is **RESULT-EXPOSED**.

Before this Note, the following numerical facts or candidate patterns were already discussed in preparation:

- the difference between the measured proton/electron mass ratio and `6 pi^5`;
- the current `alpha^2/3` proton dressing;
- the remaining ppm-scale witness after that dressing;
- the observation that the remaining witness lies near a rational multiple of `(alpha/pi)^2`, including the near-`1/5` comparison.

These are not blind discoveries and may not be used to choose a coefficient, sign, order, carrier, threshold, normalization, or functional form in a later formal probe.

Any promoted public probe descended from this Note must disclose the same exposure. A later match can be evidence only if the mechanism was frozen independently of the target value.

## 3. Program hypothesis space

The program deliberately keeps several mutually competing origins alive.

### A. C-MASS-READ-DIFFERENTIAL-N

**Status:** non-canonical candidate.  
**Expected layer:** L4 carrier to L5 read. Any L5 to L6 empirical lift requires a separate named gate.

Candidate statement:

There exists one exact mass-reading operator

```text
D_M(rho_a, public inputs) -> Delta_a
```

whose rule is common across particle species, while its output may depend on a pre-existing typed species/carrier label `rho_a`.

The operator must be constructed without using the measured mass residuals as inputs.

The target is not a common numerical correction. The target is a common **operator**.

A legitimate outcome may have

```text
Delta_p != Delta_mu != Delta_tau != Delta_e
```

provided the differences are forced by previously frozen carrier data and not by separately chosen coefficients.

A model with independent proton, muon, and tau correction formulas does not satisfy this branch.

### B. C-MASS-READ-SERIES-N

**Status:** non-canonical candidate.  
**Expected layer:** L5 algebraic/read structure only before any measured comparison.

If a mass-reading dressing exists, determine whether its perturbative or discrete expansion is forced by one construction. A schematic output may have the shape

```text
D_M(a) = c_(a,1) alpha^2
       + c_(a,2) (alpha/pi)^2
       + c_(a,3) alpha^4
       + ...
```

but this Note does not assert that this is the correct basis or order.

The coefficients, basis functions, truncation rule, and signs must be generated upstream. They may not be selected by minimizing the proton, muon, or tau residual.

`DRESS-CROSSCOUNT [O]` remains the owner of the integer crossing count per observable. If a later series construction requires that count, it must consume the registered result rather than reinvent it under a new name.

### C. C-MASS-READ-GRAVITY-N

**Status:** non-canonical candidate.  
**Expected layer:** compound. The source/readout object must be typed first; environmental L6 comparison is a later gate.

Candidate statement:

Mass reading has a dependence on a registered gravity-channel quantity `Gamma` that phase reading does not share.

The word `Gamma` is deliberately unresolved here. It may not be chosen after looking at environmental constraints. A later preregistration must first decide exactly what the public architecture supplies as the admissible gravity-side input, for example a lapse, commutator invariant, curvature-derived quantity, counter-derived quantity, or another already registered object.

Only after `Gamma` and the functional dependence are frozen may a branch compare environments.

A valid gravity branch must predict, before opening environmental target data, at least the sign and exact functional form or exact discrete law corresponding to

```text
d log(mu) / d Gamma
```

or its typed discrete analogue.

`METRO-EDGE-SCALE [O]` continues to own the SI selector and scale clause. A dimensionless gravity construction does not authorize an SI claim by itself.

### D. C-MASS-SEED-AUDIT-N

**Status:** non-canonical candidate.

This branch keeps open the possibility that the present seed itself is wrong.

In particular, none of the following is protected by this program:

```text
mu_(p,0) = 6 pi^5
mu_p     = 6 pi^5 (1 + alpha^2/3)
```

The first expression may be the wrong physical seed, a useful asymptotic structure, or a numerical coincidence. The second may be a true first correction, a partial reading, or an accidental improvement.

A permitted terminal outcome is

```text
SEED_FALSE
```

A program that cannot return `SEED_FALSE` is only a rescue attempt and is outside this Note.

### E. Existing intrinsic branch

`PROTON-RESIDUAL-IS-QCD [O]` is retained as the intrinsic/QCD competitor.

This Note creates no substitute `C-MASS-QCD-*` candidate. If the QCD row closes, that result enters the origin classification at its earned scope.

## 4. Common gates

The following gates apply to every later branch unless a narrower preregistration explicitly strengthens them.

### G0. Layer declaration

Every branch declares its action layer before computation. No unnamed lift between L1 state, L2 manifold, L3 boundary, L4 support, L5 stream, and L6 measure is allowed.

### G1. No target leakage

Measured mass ratios, their residuals, or an equivalent derived target may not select:

```text
coefficient
sign
series order
basis
carrier label
normalization
branch
threshold
functional form
```

A target may be opened only after the relevant structure is frozen, except where prior exposure is explicitly disclosed and the target is excluded from construction evidence.

### G2. No new free dimensionless input

Any new free dimensionless coefficient introduced to repair a residual is a negative result for the zero-free-input branch.

A rational number is not exempt merely because it is simple.

### G3. Common operator

Proton, muon, tau, and electron must be outputs of one operator or one formally classified operator family whose admissibility is fixed independently of those target masses.

Three unrelated formulas are not a common mechanism.

### G4. Universal multiplicative cancellation

**candidate-T lemma.** If one proposes

```text
m_a^read = F m_a^0
m_e^read = F m_e^0
```

with exactly the same nonzero factor `F`, then

```text
m_a^read / m_e^read = m_a^0 / m_e^0.
```

Therefore a species-independent common multiplicative factor cannot explain a residual in a mass ratio.

This does not rule out species-dependent factors, additive structures, relational read maps, or another typed mechanism. It kills only the common multiplicative route.

### G5. Phase control

If the program claims that the extra cost belongs to mass reading rather than to reading in general, the same mechanism must provide a structural control on a registered phase observable.

The desired control is not "set the phase coefficient to zero". The zero or absence must follow from the operator and the phase carrier.

Failure to distinguish the two reading classes weakens or kills the claimed interpretation.

### G6. Cross-mass holdout

No observable may be used both to construct and to validate the same coefficient.

The strongest design is preferred: derive the operator and every coefficient without proton, muon, or tau target masses, then use all three as external tests.

If that is impossible, the preregistration must freeze which targets are construction data and which are holdouts.

### G7. Method covariance

Metrological agreement must be represented with its shared inputs and correlations. Different apparatus does not automatically imply statistically independent determination.

Any later L6 evidence package must name the measurement method, source, shared theoretical inputs, shared constants, and known correlation structure to the extent required by the claim.

### G8. Gravity prediction before environmental comparison

A gravity branch must freeze its source object and predicted environmental response before comparison with white-dwarf, absorber, clock, or other environmental constraints.

Choosing the gravity variable because it evades the opened data is target leakage.

### G9. Negative results survive

A fired branch falsifier is preserved. It may not be repaired by moving a threshold, changing the carrier under the same identifier, or redefining the failed mechanism as a different layer after the result.

A new mechanism requires a new named candidate.

## 5. Origin classification

The program should eventually classify rather than merely fit.

Proposed terminal vocabulary:

```text
READ_ONLY
INTRINSIC_ONLY
MIXED
SEED_FALSE
NONUNIQUE
EMPTY
STOP
```

Meaning:

- `READ_ONLY`: a complete admitted read-origin class survives and the frozen intrinsic class is empty at the declared scope.
- `INTRINSIC_ONLY`: the intrinsic class survives and the read-origin class is empty at the declared scope.
- `MIXED`: independently derived nonzero intrinsic and read components both survive, with no free split coefficient.
- `SEED_FALSE`: the registered seed required by the tested branch fails before a residual decomposition is meaningful.
- `NONUNIQUE`: at least two inequivalent admitted mechanisms survive all frozen gates, so the architecture does not select a unique reading at the declared scope.
- `EMPTY`: the complete frozen admitted class is empty.
- `STOP`: typing, completeness, authority, evidence, or layer requirements are insufficient for a scientific decision.

`MIXED` is not a fallback bucket. A free decomposition of one measured number into two terms is not a result.

## 6. Why the first attack is differential reading, not gravity

The gravity route contains too many possible source objects to be a clean first attack.

The first scientific candidate should therefore be `C-MASS-READ-DIFFERENTIAL-N`.

The initial question is:

> Does the current public architecture contain an exact, target-independent operator that distinguishes the registered electron, proton, muon, and tau carrier/read labels in a way capable of producing different mass-reading corrections?

The first pass should end before measured residuals.

Possible outcomes at that stage include:

```text
candidate-T     an exact differential operator or classification is forced
candidate-D     a unique dictionary reading exists conditional on registered carrier data
candidate-C     only a finite exact census has been obtained
EMPTY           no admitted differential operator exists in the frozen class
NONUNIQUE       several inequivalent operators survive
STOP            the public carriers or typed decoder data are insufficient
```

If the branch is `EMPTY`, the proposed universal mass-reading interpretation dies in that frozen architecture before metrology.

If it is `NONUNIQUE`, numerical agreement of one selected operator does not establish the theory.

Only a sufficiently constrained survivor should be exposed to mass data.

## 7. Relation to the current Canon

This program is adversarial to the current physical mass reading, not to exact mathematics merely because that mathematics currently appears in the mass section.

A later result may therefore produce a split such as:

```text
MU-TAU-COEFFICIENT        survives as exact mathematics
MU-EXCHANGE-IDENTITY      survives as exact mathematics
MASS-LADDER-FORMS         requires revision or is falsified as a physical dictionary
```

That is a legitimate scientific outcome.

Likewise, failure of `6 pi^5` as a physical proton seed would not falsify the arithmetic identity represented by the expression itself. It would falsify or revise the physical reading that assigns it to the proton ratio.

## 8. Formalization path

This Note authorizes no formal execution.

A later branch begins only after its own public collision lock and, where computation or formal gating is intended, a prospectively pinned preregistration.

For the first branch the future public work should freeze at least:

```text
candidate id
source carrier(s)
output type
equality/equivalence
allowed public dependencies
common-operator predicate
species-label admissibility
no-target-leakage procedure
complete candidate class or completeness theorem
scientific falsifiers
action layer and every required lift gate
```

No `EXPECTED.txt`, formal transcript, fitted coefficient, or target-derived threshold belongs before that pin.

## 9. Promotion boundary

This Note carries no scientific status and creates no public frontier row.

A future incubation result, if any, must be recorded only as `candidate-T`, `candidate-D`, or `candidate-C` at its exact scope, independently attacked, and packaged for promotion only after the required protocol is satisfied.

Promotion must not imply that the Canon was right. The purpose of the program is to determine which parts of the current mass reading, if any, survive a clean adversarial reconstruction.

## 10. Immediate next step

Do not fit the residual.

Define the admissible carrier labels and the candidate operator class for `C-MASS-READ-DIFFERENTIAL-N`, then try to prove one of three things before opening target masses:

```text
UNIQUE
NONUNIQUE
EMPTY
```

That classification is the first real scientific result this program needs.
