# Pair-local incidence: breaker audit and signed-reduction boundary (NON-CANONICAL)

```text
IDENTIFIER:          C-J-PAIR-LOCAL-INCIDENCE-BREAKER-AUDIT-1
DATE:                2026-09-04
SCOPE:               L1 mathematics and finite model consistency
STATUS:              POST-EXPOSURE INCUBATION AUDIT / NON-CANONICAL
PUBLIC FORMAL PROBE: NONE
PUBLIC BASE:         fbf33fa1116d9e3526ac4ae057356cf2d2bddb6e
CANON:               Public Canon v75, unchanged
```

The supplied B1–B4 numerical witnesses reproduce through a second code path.
They exclude autonomous evolution from unsigned populations alone, direct
raw-arrival pair counting as the reduced census, and A as an automorphism of
the entire fixed integer lattice. The frozen model instead evolves signed
coefficients before preparing reduced fibres. It returns **0**, not 16, in
the challenged dark cell. Its conditional census construction survives these
witnesses; a physical implementation of signed reduction remains absent.

`COINCIDENCE-RECORD-FREQUENCY` remains `candidate-H / UNTESTED / STOP` and
`QDD-INSTRUMENT-APPARATUS` remains `O / STOP`. Candidate labels in this note
describe proposal-local conclusions, not registered public statuses. No
physical occurrence law, frequency law, self-location rule, or cross-layer
closure is adopted.

## 1. Audited specification and provenance

The attached [candidate specification](C-J-PAIR-LOCAL-INCIDENCE-BREAKER-AUDIT-1/source/C-J-PAIR-LOCAL-INCIDENCE-CENSUS-N.md)
and [candidate model](C-J-PAIR-LOCAL-INCIDENCE-BREAKER-AUDIT-1/source/candidate_model.py)
are byte-identical snapshots frozen before this audit. Their original
wording "unexecuted" describes the snapshot at that time. The model was
subsequently exercised in the local incubation run recorded in section 7;
no formal public probe was executed.

The external review supplied the B1–B4 witnesses in text. Its original
breaker script was not available. The two documents it named,
`NAVRH-APARATU-RETEZ-AXIOM-BORN_2026-09-04_CZ.md` and
`NOTE-KUDY-K-BORNOVU-CTENI_2026-09-04_CZ.md`, were also unavailable to this
audit. This note therefore evaluates the attached model and the explicitly
stated objections; it does not assume that the external review had inspected
this exact package or assess the complete contents of those two documents.

The [audit code](C-J-PAIR-LOCAL-INCIDENCE-BREAKER-AUDIT-1/verify_incubation.py)
first computes convolution by distributing source columns and computes the
determinant by Gaussian elimination over `Fraction`. Only then does it import
the frozen model, whose update uses row shifts, and compare results. This is
a second implementation with disclosed, already known witnesses. It is not
a blind prediction or an independent discovery of the counterexamples.
Earlier static reviews by multiple agents were not independent executable
reproductions.

## 2. B1: absolute populations do not determine the next state

Use `A=1+g²−g³−g⁴`, with `g e_k=e_(k+1 mod 5)`. The supplied inputs give:

```text
d  = (-3, 0,-1, 1, 3)     A d  = (-1,3,-8, 1,5)
d' = (-3, 0, 1,-1, 3)     A d' = (-5,3,-4,-1,7)
```

Equal `|d|` and unequal `|Ad|` exclude a map G on unsigned populations with
`G(|d|)=|Ad|` for all such inputs. The original pair lies outside the model's
carrier `L_D={d∈Z⁵: Σd_k=0, d_i≡d_j (mod 5)}`. This does not remove the
obstruction: multiplication by five gives witnesses inside L_D:

```text
D  = (-15,0,-5, 5,15)     A D  = ( -5,15,-40, 5,25)
D' = (-15,0, 5,-5,15)     A D' = (-25,15,-20,-5,35)
```

The frozen model retains both the signed preparation and the signed
coefficients at the read cut. Its record census does not replace that state
and cannot be the sole input to the next A step. B1 correctly excludes such
an extension.

## 3. B2 and B3: reduction precedes the bank

For the seed `a₀=(4,−1,−1,−1,−1)`, exact arithmetic gives the following table.
Each row counts one-step arrivals from the already reduced preceding state;
it does not count the entire unreduced history tree from the original seed.

| Step | New signed state | Sum of squared raw arrival counts | Sum of squared reduced coefficients | Ratio |
|---|---|---:|---:|---:|
| 0→1 | (5,0,5,−5,−5) | 212 | 100 | 53/25 |
| 1→2 | (−5,−5,20,−5,−5) | 1300 | 500 | 13/5 |
| 2→3 | (−25,−25,25,0,25) | 5300 | 2500 | 53/25 |
| 3→4 | (−25,−25,−25,−25,100) | 32500 | 12500 | 13/5 |

More generally, let `C=|A|=N−g`, where N is the all-ones matrix, and let
`q(a)=Σa_k²`, `L(a)=Σ|a_k|`. Then `CᵀC=I+3N`, so

```text
q(C|a|)=q(a)+3L(a)²,          q(Aa)=5q(a) when Σa_k=0.
```

At cell 1 of the first step, the contributions are `(-1,-1,+1,+1)`:

| Quantity | Value |
|---|---:|
| Unsigned raw pair count | (2+2)² = 16 |
| Signed pair sum | (2−2)² = 0 |
| Actual attached-model output at cell 1 | 0 |

The attached model uses this order:

```text
signed d → signed arithmetic A^n d
         → fresh reduced fibres of sizes |(A^n d)_k|
         → complete two-role pair bank
         → one same-cell XOR activation → census.
```

The XOR gate does not perform interference. Signed arithmetic evaluates the
cancellation before the bank is prepared. Thus the **unsigned raw-arrival
extension** is refuted (`candidate-F`), and the bank alone does not supply a
physical derivation of interference. B3 does not refute the literal model
with reduced inputs: that model never creates those sixteen same-cell
addresses in the dark cell. The gate does not read a numerical Born target,
but the complete census still depends on the strong fibre-preparation
premise. Not reading the target ratio is insufficient to establish a physical
derivation.

## 4. No-go for a nonnegative separately additive raw-pair recorder

Consider a finite nonnegative record rule separately additive under disjoint
addition of raw units in each input role. Denote the elementary sign-pair
responses by nonnegative integers `w₊₊, w₊₋, w₋₊, w₋₋`. Decomposition into
singletons gives, for two identical inputs containing p positive and m
negative units,

```text
R(p,m)=w₊₊ p²+(w₊₋+w₋₊)pm+w₋₋ m².
```

Unit response to each pure sign requires `w₊₊=w₋₋=1`. Factoring the response
through the reduced coefficient's square would require `R(p,m)=(p−m)²`.
However,

```text
R(1,1)=2+w₊₋+w₋₊ ≥ 2,          (1−1)²=0.
```

Here `p=m=1` is a local null input in the explicitly enlarged class of raw
ports, not an admitted nonzero global preparation of the frozen model. For
the actual B3 cell, `p=m=2`, the same argument gives at least 8 against the
required zero; complete unsigned incidence gives 16. Physical availability
of the singleton calibrations is a premise of this no-go, not its conclusion.

Hence **nonnegativity, separate additivity on raw inputs, unit calibration,
and null output after cancellation are incompatible**. This is a conditional
finite-set theorem (`candidate-T` at the proof level), not a registered
status or a refutation of every possible physical apparatus.

Signed summation itself is linear. Conversion to nonnegative reduced counts
`|p−m|` is not additive under raw disjoint union. The candidate's product
theorem therefore applies **after reduction**; its additivity cannot be
transported through cancellation. Signed weights give an algebraic
difference, not a positive cardinality of physical events. Another positive
construction would have to change the premises, for example by allowing
cancellation of records or context-dependent selection.

## 5. B4: coefficient evolution, presentation loss, and bank reversibility

On the root lattice `A₄={d∈Z⁵:Σd_k=0}`, in the basis `e_i−e_4`, A has matrix

```text
 1 -1 -1  1
-1  0 -2 -2
 2  1  2  0
 0  2  1  2
```

and determinant 25. Its image has index 25, so A is not an automorphism of
the entire fixed lattice. The same holds on the invariant full-rank
sublattice L_D. On the augmentation-zero sector, however, `AᵀA=5I`; A is
injective and `A⁻¹=Aᵀ/5`. Every point in the lattice image has one integral
predecessor. An arbitrary lattice target need not: the preimage of `e₀−e₄`
is `(2/5,0,−2/5,1/5,−1/5)`.

This does not prove many-to-one loss of signed coefficient states. A
different map, from arbitrarily labelled raw arrivals to their net
coefficient, forgets presentation and ancestry. A reversible physical
realization of that reduction would have to retain the discarded information
in its complete state or environment.

The claimed bank involution fixes a and changes only b:
`(a,b)↦(a,b XOR h_a)`. It does not advance a by A. B4 does not refute this
involution, and the involution does not prove reversibility of preparation
or autonomous dynamics. For example, `(a,z)↦(a,z+Aa)` has the integer inverse
`(a,z)↦(a,z−Aa)` while retaining a. This is a computational extension with
memory, not a supplied physical mechanism. The determinant alone therefore
does not force physical annihilation.

## 6. Surviving result and remaining physical contract

Separate additivity under the original specification's assumptions gives a
product of fibres. **Selecting equal cells is an additional premise.** In
the multicolour version,
`F(X,Y) ≅ ⨿ᵢⱼ X_i×Y_j×W_ij`; the diagonal follows only after calibrating one
record for an equal-cell pair and none for a different-cell pair. The product
theorem supplies neither that calibration nor its physical justification.

Further work must supply a physical carrier of sign and reduction,
independently of the target ratio. Its contract must specify:

1. The complete state and signed update, with census outputs not replacing
   the dynamical state.
2. Why different raw presentations of one coefficient produce the same
   readable output, and why cancelled contributions are not independently
   counted as records.
3. Where presentation information is retained if physical reversibility is
   required.
4. Preparation of reduced fibres, two input roles, full capacity, a blank
   bank, one activation, and retention at a fixed read cut.
5. Independent justification of the diagonal response, and the separate
   boundary between a population census and one reader's self-location.

The mathematical unit definition already exists in
[C-J-RESIDUAL-INTEGER-UNIT-1-N](https://github.com/mathorn1973/twist-j/blob/fbf33fa1116d9e3526ac4ae057356cf2d2bddb6e/notes/canon/C-J-RESIDUAL-INTEGER-UNIT-1-N.md).
It does not establish physical realization. The objection that no unit
definition exists therefore does not apply directly to the attached package.
The [adopted A/U5 split with a separate open B channel](https://github.com/mathorn1973/twist-j/blob/fbf33fa1116d9e3526ac4ae057356cf2d2bddb6e/notes/canon/C-J-A-U5-COINCIDENCE-OWNER-FREEZE.md)
also remains in force. The breaker does not override that ruling or admit
raw J or B to the integer count port. The design predecessor
[PR #803](https://github.com/mathorn1973/twist-j/pull/803) was merged as
`a7ef8ba676a7a26ebac4b0d5a0b31c47bc41cc9c`.

## 7. Incubation protocol and reproducibility

This audit followed an authorized local incubation procedure: freeze the
[six-field PREREG](C-J-PAIR-LOCAL-INCIDENCE-BREAKER-AUDIT-1/PREREG.md) and its
SHA-256 before execution. A separately sealed
[pre-execution erratum](C-J-PAIR-LOCAL-INCIDENCE-BREAKER-AUDIT-1/PREREG-ADDENDUM-1.md)
corrected a phrase that interchanged the cell index and its zero count.
Inputs, code, and failure threshold did not change. This procedure does not
replace the repository's public formal-probe protocol. A local pin is not a
pre-execution public timestamp, and publication through this notes pull
request does not retroactively confer formal-probe status.

The local run completed on 2026-09-04 at 16:35:12 UTC using Python 3.12.10
on Windows AMD64, with `LC_ALL=C`, `PYTHONHASHSEED=0`, `TZ=UTC`, and
`PYTHONDONTWRITEBYTECODE=1`. Exit code was 0, stdout was 3138 bytes, and
stderr was empty. Exact checks covered signed states and census for n=0…4,
B1–B4, and the fixed-input involution. The general statements above rest on
their proofs, not on the size of this finite sample.

The public package contains the minimal specification, code, PREREG,
erratum, and [SHA-256 provenance](C-J-PAIR-LOCAL-INCIDENCE-BREAKER-AUDIT-1/PROVENANCE.json).
The original local organizational README, execution wrapper, and raw run
outputs are omitted; relevant hashes are recorded. This is a selective
scientific package, not a byte-identical copy of the entire local directory.
The two scientific source snapshots, audit code, PREREG, and erratum retain
their original bytes. The English exposition and its current manifest entry
are publication documents written after the run; they are not frozen inputs.

For a fresh incubation replay, from the directory containing this note run
`python C-J-PAIR-LOCAL-INCIDENCE-BREAKER-AUDIT-1/verify_incubation.py` with the
same environment. The script uses only the standard library and the attached
model. A new run is the recipient's own reproduction, not the original
recorded run or automatically a formal public probe. Repository CI checks
for this notes-only change do not execute this incubation script or establish
two-architecture scientific reproduction of its output.

This identifier names an audit and reserves no public claim or formal probe;
it does not take over `C-J-COINCIDENCE-RECORD-1` from another line. An external
`BREAKER-RECORD-C-J-COINCIDENCE-RECORD-1` should independently identify its
exact script, inputs, output, and challenged source version. The attached
second implementation does not substitute for that unavailable original
breaker record.
