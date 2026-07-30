# PREREG-C-ENTROPY-MACKEY-OBSTRUCTION-4-N

```text
STATUS:        NON-CANONICAL PREREGISTRATION
AUTHORITY:     NONE
TARGET LINE:   PUBLIC-REPOSITORY INCUBATION ONLY
CANDIDATE:     C-ENTROPY-MACKEY-OBSTRUCTION-4-N
OWNER:         A. M. Thorn / mathorn1973 / GPT-5.6 Thinking owner session
OPENED:        2026-07-30
PUBLIC BASIS:  Public Canon v28
MAIN:          3161cbc764f547c95a80c3bd5028acf71c2ef524
TAG:           canon-v28
CONTENT:       86a046007f89a64a696d013112a44f02e624dd2e
CANON SHA:     4b720846ccd42c7ec808ab2acb21793962390b074bb3799d28c0f16c00165d2c
RECON BASE:    39d9a88f3249310ed33df3f2a1172ef169456ead
DECLARED CLASS: fixed depth five, fiberwise bijective Route A sub-ansatz,
                substitution levels r >= 2
PROVISIONAL CEILING: candidate-C
COMPUTATION BEFORE THIS PREREGISTRATION: NONE FOR THIS CANDIDATE
```

This candidate is fresh. It does not import the missing primary verifier or the
result of `C-ENTROPY-MACKEY-OBSTRUCTION-3-N`. Earlier calculations are discovery
history only and are not evidence. No public issue, formal probe, registry row,
Canon patch, status change, or bridge closure is authorized here.

## Field 1. Equation and decision surface

### 1.1 Source system

Let

```text
Q_5 = O/lambda^5,
O   = Z[zeta_5],
lambda = 1-zeta_5,
J_5(q) = J q on Q_5,
J = 1+zeta_5^2.
```

Let `(K_TM,m_TM,S)` be the two-sided Thue-Morse substitution system with its
unique invariant probability. The depth-five source extension is

```text
T_src(kappa,q) = (S kappa, J_5 q).
```

The source permutation must be reconstructed exactly and must have cycle type

```text
1^1 4^1 20^156.
```

For a constant cycle `C_m`, the component count on the level-`r` dyadic factor
is

```text
gcd(2^r,m) = 2^min(r,v_2(m)).
```

The full Thue-Morse rational point spectrum is the dyadic root group. Fourier
analysis on `C_m` therefore gives the full product component count
`2^v_2(m)`. The finite dyadic factors stabilize once `r >= v_2(m)`.

Since the declared recon begins at `r=2` and

```text
max v_2(m) over m in {1,4,20} = 2,
```

the source count on the entire admitted range is

```text
c_src = 1 + 4 + 156*4 = 629.
```

The verifier must also print the out-of-scope controls

```text
c_src(0) = 158,
c_src(1) = 315,
c_src(r) = 629 for every tested r >= 2.
```

No statement omitting `r >= 2` passes this preregistration.

### 1.2 Target system

The target half has 312 generic blocks and one singlet block. The exact public
reading to be reconstructed is

```text
X_target = (disjoint union of 312 regular D_5-sets) disjoint union D_5/C_2,
|X_target| = 312*10 + 5 = 3125.
```

Each generic half is separately a free `D_5` torsor. The collection of 312
halves is not one torsor.

The decisive target gate is the existence of one measurable common cocycle

```text
alpha: K_TM -> D_5
```

whose action, after one fixed public reconstruction of coordinates, induces
all 312 regular actions and the singlet `D_5/C_2` action. Block-dependent
cocycles, block-dependent Mackey ranges, kappa-dependent relabelings, and
post-hoc target gauges are outside the candidate.

Let `M <= D_5` be the Mackey range of this one cocycle, defined up to
conjugacy. The number of target ergodic components must equal the number of
`M`-orbits on `X_target`.

All eight subgroups of `D_5` must be enumerated individually:

```text
D_5,
C_5,
five conjugate reflection subgroups C_2,
{1}.
```

Their orbit counts must be exactly

```text
M       regular D_5-set   D_5/C_2   total target components
D_5             1             1       313
C_5             2             1       625
C_2             5             3       1563
{1}            10             5       3125.
```

Thus the target menu is

```text
{313,625,1563,3125}.
```

The negative control is binding. Over the separate menus

```text
a in {1,2,5,10},
b in {1,3,5},
```

the equation

```text
312*a + b = 629
```

must have the unique solution `(a,b)=(2,5)`. This means `C_5` on the generic
blocks and the trivial group on the singlet. If the implementation cannot
realize this mixed control when the common-cocycle requirement is deliberately
removed, the test does not demonstrate that the common cocycle is load bearing.

### 1.3 Claimed obstruction

A measurable fiberwise bijective conjugacy between the source and target
extensions preserves the invariant sigma-algebra and therefore the number of
ergodic components. The candidate claim is

```text
629 not in {313,625,1563,3125}.
```

Hence no measurable depth-five fiberwise-bijective conjugacy exists, provided
all source, target, common-cocycle, and subgroup gates pass.

Provisional conclusion on success:

```text
The fixed-depth-five fiberwise-bijective Route A subclass is empty.
```

This is not `A_A = empty` and does not close `ENTROPY-LAYER-BRIDGE [O]`.

### 1.4 Conditional embedding into Route A

The obstruction becomes a Route A subclass result only after the following
embedding lemma is proved.

Let

```text
pi_5: O_(K,lambda) -> Q_5
```

be reduction modulo `lambda^5`. Normalized additive Haar probability must push
to the uniform measure on the 3125 cosets. This must be proved from translation
invariance and transitivity of coset translations, not assumed from cardinality.

If a measurable family

```text
B_kappa: Q_5 -> H_(kappa_-1)
```

is bijective almost everywhere and satisfies the cocycle equation, define

```text
P(kappa,y) = B_kappa(pi_5(y)).
```

Using the one-letter Thue-Morse masses `1/2,1/2`, the proof must derive

```text
P_*mu({psi}) = (1/2)(1/3125) = 1/6250
```

for every recurrent state. Uniform pushforward is conditional on both Haar
quotient uniformity and fiberwise bijectivity. Exact equivariance alone does
not imply it.

## Field 2. Code and independence plan

No code is accepted or executed by this preregistration commit.

The intended primary implementation is

```text
notes/entropy_selection/mackey4_verify.py
```

and must use Python standard library only, exact integers and `Fraction`, no
float in any assertion, no network, no subprocess, and no imported old Mackey
candidate.

The primary route must reconstruct:

1. `Q_5` from the cyclotomic integer presentation and independently verify its
   additive type and cardinality;
2. multiplication by `J` and the full cycle type `1^1 4^1 20^156`;
3. the dyadic Thue-Morse eigenvalue intersection and source counts at
   `r=0,1,2,...`;
4. all 6250 recurrent target states and one-tick target maps from the public
   generator definitions, not from a spectrum-only table;
5. the decomposition into 312 separate regular `D_5` torsors and the singlet
   `D_5/C_2`;
6. one common `D_5` cocycle, or an exact counterexample showing that no common
   coordinate reconstruction exists;
7. all eight subgroups and every orbit count;
8. the Haar quotient lemma and the conditional Route A embedding.

An independent breaker is required before any promotion package:

```text
notes/entropy_selection/mackey4_break.py
```

It must be authored in a separate named session from this frozen
preregistration without reading `mackey4_verify.py`, must not import it, and
must be frozen before comparison. Its source route must use a distinct
presentation, for example the integer multiplication matrix plus Smith normal
form rather than the primary lambda-digit arithmetic. Its target route must
rebuild the subgroup menu and mixed negative control independently.

A second run of the primary verifier is reproduction only. A breaker that merely
runs the primary verifier is reproduction only.

## Field 3. Carrier and data

No external data.

Exact public or repository carriers:

```text
K_TM with m_TM and S,
O_(K,lambda),
Q_5 = O/lambda^5,
F_5^6 recurrent target,
D_5 of order 10,
312 regular D_5-sets,
D_5/C_2 singlet set.
```

Public status ceiling inputs include `ENTROPY-LIVING-SET [C]`,
`ENTROPY-MIRROR-LAW [C]`, `ENTROPY-COUNT-MATCH [C]`, and
`COLOR-TORSOR-HOLONOMY [T]`. Unless the new reconstruction independently
raises every load-bearing finite input by proof, the candidate ceiling is C.

No JSON integer occurrence is accepted as evidence for an optimum or component
count. Every result must be recomputed from the typed carrier or replayed from
a separately hashed exact certificate whose semantics are checked.

## Field 4. Systematics

The result must survive all of the following.

```text
S1  Authority: Public Canon v28 tuple and the recon merge are exact.
S2  Level: every 629 statement explicitly assumes r >= 2.
S3  Source: the global dyadic point-spectrum argument and finite-r formula agree.
S4  Source independence: two distinct exact presentations give the same J cycle type.
S5  Target language: 312 separate ten-point torsors, never one 312-point torsor.
S6  Target reconstruction: all 6250 states and all required one-tick maps agree
    with the public generator definitions.
S7  Common cocycle: one alpha acts through both target representations; no
    block-dependent Mackey range is hidden in the gauge.
S8  Subgroup completeness: all eight subgroups are enumerated, including all
    five reflections individually.
S9  Burnside: the C_2 action on D_5/C_2 has exactly 3 orbits, not a fractional
    or representative-only count.
S10 Mixed control: removing common M produces the unique pair (2,5) and total 629.
S11 Haar: pi_5 pushes normalized Haar to uniform probability by a proved lemma.
S12 Route A: uniform pushforward uses Haar uniformity plus fiberwise bijectivity,
    not equivariance alone.
S13 Equivalence: measurable conjugacy preserves the invariant sigma-algebra and
    component count under the exact almost-everywhere convention.
S14 Layer: only the existing L2-to-L5 Route A subclass is addressed; no L6
    physical measure or entropy rate is introduced.
S15 Scope: no conclusion about deeper lambda digits, nonbijective maps, variable
    depth, r>2 collar classes, or all of A_A.
S16 Provenance: no file or result from the incomplete 3-N bundle is used as evidence.
```

## Field 5. Failure thresholds

The candidate is falsified, blocked, or reduced as follows.

```text
F1  The exact source orbit type differs from 1^1 4^1 20^156.
F2  The full Thue-Morse rational point spectrum contains a non-dyadic root of
    unity relevant to the finite cycles.
F3  The source count at any admitted r >= 2 differs from 629.
F4  Normalized Haar does not push uniformly to Q_5.
F5  The target is not exactly 312 regular D_5-sets plus D_5/C_2.
F6  No single common D_5 cocycle exists under the frozen target coordinates.
    This falsifies this Mackey route rather than proving the bridge.
F7  The complete subgroup enumeration yields an additional target count or 629.
F8  A common subgroup M produces 629 target components.
F9  The mixed negative control (2,5) does not produce 629 after the common-M
    restriction is removed.
F10 A measurable conjugacy in the declared class fails to preserve the component
    invariant under the stated equality convention.
F11 Primary and independent routes disagree on any load-bearing object.
F12 The proof requires block-dependent gauge, moving thresholds, a new layer,
    or an unregistered public premise.
```

Decision rule:

```text
candidate-C NEGATIVE SUBCLASS RESULT
    only if every S gate passes, no F gate fires, both exact routes agree,
    and the common-cocycle reconstruction is explicit.

FALSIFIED ROUTE
    if F1-F10 fires with an exact witness.

STOP
    if the target common cocycle, source spectral theorem, Haar lemma,
    independence, or equality convention remains incomplete.
```

Thresholds and scope may not move after the first computation. A defect in this
preregistration before computation may be corrected only by retiring `4-N` and
opening a fresh candidate identifier.

## Field 6. Action layer and corollary fence

```text
FROM: L2 measurable dynamical source
TO:   L5 finite recurrent readout
DEPTH: lambda^5 only
NEW LIFT: none
L6 physical measure: excluded
SI: excluded
```

Optional asymptotic corollary, not part of the primary decision:

Only if a separate exact audit proves that the summable-limit theorem and the
prefix-tree dichotomy apply to the identical fixed-`F_2`, fixed-`r=2`
cell-sector class encoded by this candidate may the no-go imply

```text
o_H -> infinity
```

inside that class. The corollary decides no `r>2` collar family and no general
Route A map. It must be recorded under its own dependency gate and cannot be
inferred merely from the number 629.

## Freeze record

At this preregistration commit:

```text
mackey4_verify.py: absent
mackey4_break.py:  absent
formal or informal computation under candidate 4-N: none
threshold movement: forbidden after the first computation
```
