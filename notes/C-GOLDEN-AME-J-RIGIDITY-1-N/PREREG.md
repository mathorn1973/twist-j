# C-GOLDEN-AME-J-RIGIDITY-1-N — public preregistration

Status: **NON-CANONICAL INCUBATION**
Target line: **PUBLIC**
Layer: **L1 exact algebra only**
Public lock: [issue #369](https://github.com/mathorn1973/twist-j/issues/369)
Branch: `notes/c-golden-ame-j-rigidity-1-n`
Canon writes: **forbidden**
Registry writes: **forbidden**
`PROMO.md`: **forbidden**

Before this public lock no target Gröbner basis, saturation, radical,
elimination, factorization aimed at solution branches, positive-branch
classification, or expected-relation membership test was computed.  The
permitted pre-lock work was limited to source pins, two exact token
constructions, structural counts, stable unsolved-equation serialization,
artificial CAS self-tests, and exact back-substitution of the already
published golden point.

After the public commit/hash, the family, variables, involution, generator
order, sole saturation, real locus, target order, controls, gates, and verdict
grammar below are immutable.  A result-dependent change requires a new claim
key and a new public preregistration.

## 1. Question and deliberately narrow family

The pinned golden AME(4,6) source consists of a `36 x 36` amplitude-label
matrix with labels `0,a,b,c`, multiplied entrywise by a printed integer
exponent matrix.  Its active support has 112 entries: 40 labelled `a`, 40
labelled `b`, and 32 labelled `c`.

This experiment does **not** vary an arbitrary tensor with that zero support.
It freezes:

1. all 112 active positions;
2. the assignment of each active position to one of the three common
   amplitude labels;
3. every literal integer exponent at each active position; and
4. the three published `2|2` flattening conventions.

Only four quantities vary: three common positive real amplitudes and one unit
complex phase.  The question is whether three-way unitarity inside this tied
printed-gauge family forces the golden amplitudes, twentieth cyclotomy, and
their amplitude/phase seam, up to complex conjugation.

The word **skeleton** below means this complete support/label/exponent
skeleton.  It never means the zero support alone.  The `9 x 4` description
from the explanatory source fixes a useful second construction, but it adds
no projector, Bell basis, local factorization, or target equation.

## 2. Authority, sources, and prior independent replay

`SOURCE_PINS.json` and `SOURCE.md` are normative.

| Item | Frozen value |
|---|---|
| Canon | Public Canon v46 |
| Authority | `mathorn1973/twist-j` `main` |
| Activation commit | `6545c1d0de61ff4696eb3de1a258139e8891f436` |
| Content commit | `62628ca4da2d938e4e3a122d35c0d93a6debc27f` |
| `canon/CANON.md` bytes | `222760` |
| `canon/CANON.md` SHA-256 | `6c57e714c441bd679b9f6c673352cfae44ac993433d7c4624cd9c3c93df291ff` |

The sole tensor-value authority is `AME46_ORIGINAL.m` from
`matrix-toolbox/AME_4_6` commit
`1fa4a4d4d2b9a3c6d3b6c8d802116415fb679fe8`: 8515 bytes, SHA-256
`55fbc0ba2747b4e5adc5a5abd15ac7241a461ff8182268ebdae464d8a29cc9ae`,
Git blob `e0d0e171d58b3360c39595d677ffc401a466112d`.

At the same upstream commit, `block944.m` is pinned as auxiliary permutation
provenance: 8234 bytes, SHA-256
`af0aac863f54beb2c8396368fd87102e75192a38ec77efee0605210123540649`,
Git blob `caab29cb76e60e3165abf70931cf35e387b6e3b1`.

The already public independent review commit
`c5da90c091995e398f2379c9437234754d4e3d3a` supplies a prior, separate
two-architecture replay of the source, support, exact three-way unitarity,
and minimal entry field of the known specialization.  Its byte-identical
certificate hashes are:

```text
CERT-G0-G1-INDEPENDENT.txt  5afb8eb1c188536de7de175eec3fe1340ea47fa449471540d67f5f6a3c3c1f7d
CERT-G3-G4-REVIEW.txt       48f469f53ffc3803647b0708a590954f356f8f991dbfff4262343d1e533755f9
```

These prior facts certify the imported golden point.  They do not answer the
new parametric rigidity question.

Post-lock software rejects a source pin mismatch before parsing.  A source or
parser mismatch is `INVALID`, never evidence for or against rigidity.

## 3. Opaque-token parse and parametric tensor

After byte checks, the raw-family builder may parse only the two `36 x 36`
literals in

```text
U = [ amplitude labels ] .* w.^[ integer exponents ];
```

The definitions of `a`, `b`, `c`, and `w` above those literals must not be
parsed, evaluated, imported, or called by the raw builder.  Here those four
source names are opaque tokens.

All indices are zero-based.  For `i,j,k,l in {0,...,5}`, set

```text
row = 6*i + j
col = 6*k + l.
```

Let `L[row,col]` be the pinned amplitude token and `E[row,col]` the pinned
integer exponent.  Work in

$$
R=\mathbb Q[\alpha,\beta,\gamma,x,y]
$$

with formal involution

$$
\alpha^*=\alpha,\quad \beta^*=\beta,\quad \gamma^*=\gamma,
\quad x^*=y,\quad y^*=x.
$$

Map the source tokens by

$$
0\mapsto0,\qquad a\mapsto\alpha,\qquad
b\mapsto\beta,\qquad c\mapsto\gamma
$$

and define

$$
\widehat U_{rc}=\begin{cases}
0,&L_{rc}=0,\\
\lambda(L_{rc})x^{E_{rc}},&L_{rc}\ne0,
\end{cases}
\qquad
\widehat A_{ijkl}=\widehat U_{6i+j,,6k+l}.
$$

Every exponent is the literal non-negative integer printed in the source.
Exponents are **not** reduced modulo 20.  Neither `x^20=1` nor any other
root-of-unity relation is assumed.

The three flattenings are frozen as

$$
\begin{aligned}
F_{01}[6i+j,6k+l]&=\widehat A_{ijkl},\\
F_{02}[6i+k,6j+l]&=\widehat A_{ijkl},\\
F_{03}[6i+l,6k+j]&=\widehat A_{ijkl}.
\end{aligned}
$$

No transpose, partial transpose, party permutation, local unitary, local
rephasing, row/column reordering, or alternate representative may be chosen
after seeing a result.  Requiring
`alpha,beta,gamma > 0` fixes the printed global-phase gauge.  A free global
phase is tested separately as a negative control.

## 4. Two frozen constructions and pre-lock structural certificate

Construction A parses the pinned source literals directly.  Construction B
uses the independently pinned `block944.m` permutations: after the frozen
row and column maps, the `F_03` flattening has nine `4 x 4` blocks with active
counts

```text
12, 14, 14, 8, 16, 8, 14, 14, 12.
```

Construction B fills those blocks and reverses both frozen permutations and
the flattening.  It imports no support, label, exponent, or serialized
polynomial from construction A.  The two exact token tensors must agree
entry by entry before any ideal operation.

The frozen pre-lock serializer produced 3,889 coordinate records, of which
383 are nonzero, including `xy-1`.  Its exact byte stream has SHA-256

```text
09aac23466680ba762e363ad75845aa1535f4e8e32cee75ad41119f43cb16762
```

and length 136262 bytes.  This is structural precomputation only: the
equations were serialized but not solved, saturated, reduced, factored, or
tested against any expected relation.

## 5. Primary raw ideal and exact serialization order

Write `dagger` for transpose followed by the formal involution.  The primary
raw ideal uses only the three ordered **row-Gram** systems:

$$
I_{\rm raw}=\left\langle
\{(F_{01}F_{01}^\dagger-I)_{rc}\}_{r,c},
\{(F_{02}F_{02}^\dagger-I)_{rc}\}_{r,c},
\{(F_{03}F_{03}^\dagger-I)_{rc}\}_{r,c},
xy-1
\right\rangle\subset R. \tag{1}
$$

The exact serializer order is immutable and matches the frozen hash:

1. all 1,296 coordinates of `01`, row-major;
2. all 1,296 coordinates of `02`, row-major;
3. all 1,296 coordinates of `03`, row-major; and
4. `xy-1` as the final record.

All 3,889 records remain in the raw byte stream, including identically zero
and duplicate coordinates.  Exactly 383 coordinate records are nonzero,
including `xy-1`; this count does not quotient duplicate nonzero records.

The three column-Gram systems

$$
F_{01}^\dagger F_{01}-I,
\quad F_{02}^\dagger F_{02}-I,
\quad F_{03}^\dagger F_{03}-I \tag{2}
$$

are mandatory redundant audits, not primary generators.  For square matrices
over every field specialization, a one-sided inverse is two-sided.  The
audit must construct (2) independently and certify exact reduction to zero
under the accepted primary ideal/certificate.  Failure is `INVALID`; adding
(2) to repair a primary failure is forbidden.

Raw construction performs no reduction by `xy-1`, factor cancellation,
radicalization, Gröbner reduction, or cyclotomic lookup.  Its only
non-source domain equation is exactly `xy-1`.  Every raw record carries a
derivation trace to a row-Gram coordinate or that one domain equation.

## 6. Sole saturation and target-blind algebraic outputs

The intended family keeps all three source amplitude labels nonzero.  Put

$$
D=\alpha\beta\gamma xy
$$

and freeze the sole saturation

$$
I^\circ=(I_{\rm raw}:D^\infty). \tag{3}
$$

It is computed by

$$
I^\circ=
\bigl(\langle I_{\rm raw},1-tD\rangle
\cap\mathbb Q[\alpha,\beta,\gamma,x,y]\bigr).
$$

No saturation by `alpha-beta`, `x-y`, a discriminant, a cyclotomic
polynomial, an expected seam relation, or a factor discovered during the run
is allowed.  Degenerate full-support solutions with equal amplitude labels
or real phases remain in scope.

The target-blind stage reports:

1. replay of the frozen 3,889-record serialization hash and nonzero count;
2. a canonical reduced exact basis and hash for `I^circ`;
3. `dim(R/I^circ)`;
4. `sqrt(I^circ)` and whether `I^circ` is radical;
5. an exact equidimensional or primary decomposition when the frozen exact
   engine completes it; and
6. the elimination data needed for the exact real classification.

The saturation elimination order is lexicographic

```text
t > alpha > beta > gamma > y > x.
```

The univariate phase-elimination order is lexicographic

```text
alpha > beta > gamma > y > x.
```

Additional orders or modular reconnaissance are accelerators only.  They
must reproduce the canonical exact characteristic-zero artifacts.  Any
declared CAS wall-time, memory, process, or certificate-size ceiling is hard:
exceeding it gives `NO_VERDICT`, never permission to change (1), (3), the
order, the target, or the family.

The frozen resource envelope for each mandatory exact stage is 24 hours of
wall time, at most eight worker processes, and at most 16 GiB resident memory.
The cumulative envelope for G4--G7 is 72 hours per implementation.  A public
repository artifact may not exceed the policy limit of 5 MiB; a larger exact
certificate must be stored externally with an immutable byte count and
SHA-256, while a small standalone checker and its expected output remain in
the notes package.  Reaching any one of these ceilings yields `NO_VERDICT`.

## 7. Exact positive unit-circle locus

The question concerns positive real amplitudes and a unit complex phase, not
all complex points of `I^circ`.  Introduce real variables `u,v` by

$$
x=u+iv,\qquad y=u-iv,
$$

reduce in `Q[i]/(i^2+1)`, and split every canonical generator of `I^circ`
into real and imaginary parts.  Let `I_R` be the resulting rational ideal,
including `u^2+v^2-1`.

The exact semialgebraic locus is

$$
Z_+=\{(\alpha,\beta,\gamma,u,v):
I_R=0,\ \alpha>0,\ \beta>0,\ \gamma>0\}. \tag{4}
$$

Floating-point roots, tolerance clustering, plots, or numerical singular
values are not certificates.  Finiteness, cardinality, universal relations,
and counterbranches require exact real-root isolation, a rational univariate
representation, or exact quantifier elimination.  Every counterbranch must
include defining polynomials and rational isolating intervals.

A positive-dimensional complex component does not by itself prove a real
positive deformation.  `EXACT_POSITIVE_DEFORMATION` requires an exact
certificate that (4) contains infinitely many points.

## 8. Target relations loaded only after the blind seal

The target evaluator is a separate program with read-only access to the
sealed raw and saturated artifacts.  It cannot create, add, remove, saturate,
or replace an ideal generator.

The ordered relation vector is

$$
\begin{aligned}
r_0&=2\gamma^2-1,\\
r_1&=\alpha^2+\beta^2-\gamma^2,\\
r_2&=\beta^2-\alpha\beta-\alpha^2,\\
r_3&=x^8-x^6+x^4-x^2+1,\\
r_4&=\gamma-\alpha(x+y),\\
r_5&=\beta-\alpha(x^2+y^2).
\end{aligned} \tag{5}
$$

For each relation, report separately:

- **complex support:** membership in `sqrt(I^circ)`; and
- **positive-real support:** whether (4) together with `r_k != 0` has an
  exact witness.

For complex-valued relations after the `u,v` substitution, `r_k != 0` means
that at least one of its real and imaginary parts is nonzero.  The primary
question uses the positive-real result.  Complex-radical membership is
reported but is not required for a positive-real rigidity verdict.

The hard rigidity gate requires all six positive-real relations and exactly
two reduced points in (4), exchanged by `v -> -v`, with the same positive
amplitude triple.  No sign of `v` is preferred.

Only after that gate passes may one interpret

$$
\frac{\beta}{\alpha}=x^2+x^{-2},\qquad
\gamma=\alpha(x+x^{-1}),\qquad
\Phi_{20}(x)=0,
$$

and hence, inside this frozen family,

$$
\zeta_5=x^4,\qquad J(x)=1+x^8
$$

up to complex conjugation.  The experiment cannot select the Canon
orientation of `J` over its conjugate.

### Entry-field readback

The field conclusion is a mandatory consequence test, not an assumption.
The pinned literal gives

```text
Uhat[0,1] = gamma
Uhat[1,2] = gamma*x^17.
```

On a rigid branch, `x^20=1`, and `17*13 = 1 (mod 20)`, so

```text
x = (Uhat[1,2] / Uhat[0,1])^13.
```

Using the seam relations and positive `2*gamma^2=1`, prove both inclusions in

$$
\mathbb Q(\text{nonzero entries})
=\mathbb Q(x,\gamma)
=\mathbb Q(\zeta_{20},\sqrt2)
=\mathbb Q(\zeta_{40}). \tag{6}
$$

Containment in a preselected cyclotomic field is insufficient.

## 9. Mandatory negative controls

All controls run before a target verdict is accepted.

### NC0 — domain-only leak control

Use only `<xy-1>`, with the same saturation by `D`.  It must have complex
dimension four and an infinite positive real locus.  None of `r_0,...,r_5`,
`x^20-1`, or a nonzero polynomial in `x` alone may be reported as forced.
Failure is `INVALID_TARGET_LEAK`.

### NC1 — global-phase freedom

Introduce `g,h` with `g*=h`, `h*=g`, and `gh-1`.  Replace every matrix entry
by `g` times that entry and its adjoint by `h` times the adjoint.  Unitarity
must leave one unit-phase parameter free.  The saturated control ideal is the
extension of (3) by `gh-1`; its dimension is one larger whenever the main
dimension is known.  Forced cyclotomy for `g` is `INVALID_TARGET_LEAK`.

### NC2 — conjugation symmetry

Applying the formal involution to every primary generator must reproduce the
same ideal.  The exact real output must be invariant under `v -> -v`.  A lone
non-real branch or preferred sign of `v` is `INVALID`.

### NC3 — literal-exponent control

On a synthetic token, `x^20` must remain `x^20`; it may not become `1`.  In
NC0 the normal form of `x^20-1` must remain nonzero.  Any modular reduction
of source exponents is `INVALID_TARGET_LEAK`.

### NC4 — independent construction replay

Construction B must reproduce construction A's exact token tensor and the
frozen 3,889-record serialization hash without importing construction A's
support, label, exponent, or serialized polynomial tables.  Disagreement is
`INVALID`.

### NC5 — column-Gram audit

Construct all coordinates in (2) independently and certify them as redundant
consequences of the accepted primary system.  Any nonzero residual is
`INVALID`; it cannot be repaired by enlarging the primary ideal.

## 10. Code-separation firewall

The public package separates these roles:

```text
source pin and opaque-token construction
raw row-Gram serialization
target-blind saturation and classification
post-seal known-point replay
read-only target evaluation
negative controls and column-Gram audit
```

The raw constructor and every module it imports are forbidden to contain or
call:

- numeric definitions of source `a,b,c,w`;
- `sqrt(5)`, the golden ratio, `J`, `zeta_5`, `zeta_20`, or `zeta_40`;
- a cyclotomic-polynomial or root-of-unity constructor;
- `x^20-1`, `Phi_20`, or the coefficient list of `r_3`;
- any of `r_0,r_1,r_2,r_4,r_5`;
- a locator selected from the known golden point; or
- a precomputed target basis, eliminant, factor, or solution.

The raw constructor may use only verified literal token data, rational
integer arithmetic, the five formal variables, the stated involution, sparse
row-Gram multiplication, Kronecker deltas, and `xy-1`.  An AST/import audit,
derivation trace, and construction-B replay are mandatory.

The known-point verifier may know the published constants only after the raw
serialization has been sealed.  It cannot be imported by, or write artifacts
used by, the raw constructor.

## 11. Post-lock gate order

**G0 — authority and source integrity.** Verify issue #369, Canon authority,
both upstream file pins, literal shapes, support 112, label counts `40/40/32`,
active exponent range `0..19`, the nine block counts, and the prior replay
commit/certificates.

**G1 — blind construction equality.** Build constructions A and B and require
entrywise equality.  Emit no target relation.

**G2 — raw ideal seal.** Reproduce exactly 3,889 records, 383 nonzero
coordinate records, 136262 serialization bytes, and SHA-256
`09aac23466680ba762e363ad75845aa1535f4e8e32cee75ad41119f43cb16762`.
Close raw write handles before any downstream target stage.

**G3 — controls and known point.** Run NC0--NC5.  Independently substitute the
known source point in exact `Q(zeta_40)` arithmetic, reproduce left and right
unitarity of all three flattenings, and evaluate every sealed primary
generator to zero.  This is an integrity witness, not a target test.

**G4 — target-blind algebraic classification.** Compute (3), dimension,
radical, decomposition, and elimination data.  Hash all exact artifacts.

**G5 — exact real classification.** Construct (4), certify nonemptiness,
finiteness/cardinality or a positive deformation, and isolate every positive
branch exactly.

**G6 — frozen target evaluation.** Evaluate (5) in order, produce the complex
and positive-real six-bit masks, and print the first failed relation with an
exact positive counterbranch.  If the strong mask survives, prove (6).

**G7 — independent replay.** Reproduce source parsing, construction equality,
raw hash, column audit, saturation, real branch count, masks, and every
published witness with an independent exact implementation or architecture.

**G8 — scoped result.** Publish scripts, exact stdout, canonical JSON,
manifests, resource use, and notes-only `RESULT.md`.  No Canon, Registry,
pull-request, release, evidence, or promotion action is authorized.

## 12. Hard verdict grammar

Every valid run emits

```text
(complex_dimension,
 positive_cardinality = integer | INFINITE | UNKNOWN,
 complex_radical_mask[6],
 positive_universal_mask[6],
 conjugation_pairing,
 field_readback,
 independent_replay)
```

The human verdict is deterministic:

- `EXACT_J_RIGID_UP_TO_CONJUGATION` iff G0--G7 pass, the positive mask is
  `111111`, (4) has exactly two reduced points, conjugation exchanges them
  while fixing their positive amplitude triple, and (6) passes.
- `EXACT_GOLDEN_AND_PHASE_BUT_NO_SEAM` iff the positive mask begins `1111`
  and at least one of bits 4--5 is zero, with an exact counterbranch.
- `EXACT_GOLDEN_AMPLITUDES_ONLY` iff bits 0--2 are `111` and bit 3 is zero.
- `EXACT_PHASE_ONLY` iff bit 3 is one and at least one of bits 0--2 is zero.
- `EXACT_POSITIVE_DEFORMATION` iff an exact certificate proves (4) infinite
  and the strongest verdict does not apply; the full mask is still reported.
- `EXACT_FINITE_COUNTERBRANCH(mask=......)` iff (4) is finite and nonempty
  but the strongest verdict fails.  The first failed relation and an exact
  positive witness are mandatory.
- `INVALID_TARGET_LEAK` iff a negative control detects a forbidden inserted
  relation.
- `INVALID` iff an authority, source, parser, construction, serialization,
  involution, column audit, exact-arithmetic, or independent-replay gate
  fails.
- `NO_VERDICT` iff an exact mandatory computation reaches its declared CAS
  resource ceiling or otherwise does not finish within that frozen envelope.

The known golden specialization supplies at least one point of (4).  An
exactly certified empty positive locus is therefore a construction or
convention failure and is `INVALID`, not a negative mathematical result.

## 13. Scope firewall

A positive result is a rigidity theorem only for the frozen
three-amplitude/one-phase tied family in the printed gauge.  It does not prove:

- uniqueness of AME(4,6);
- rigidity under arbitrary support-preserving deformations;
- local-unitary uniqueness of the golden tensor;
- equivalence to or separation from other AME constructions;
- that the zero support alone forces `J`;
- a decoder, Born rule, error-correction mechanism, physical write/read
  operation, or fault-tolerant computer; or
- a preferred orientation between `J` and its conjugate.

A negative result refutes only this proposed rigidity mechanism.  It does not
alter the already proved entry-field identity of the pinned specialization.
No outcome under this lock changes Public Canon v46.
