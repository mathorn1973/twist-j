# P-FIELD-CELL-SHEAR-CENSUS-1 preregistration

PUBLIC / NON-CANONICAL / L1. Author session: Codex-v103-C-e359d425.
Public claim: [#1554](https://github.com/mathorn1973/twist-j/issues/1554).
Assignment: author C in [#1548](https://github.com/mathorn1973/twist-j/issues/1548),
body 13858 UTF-8 bytes, SHA-256
`c209686fede612501394f969d5052518d35c95be0523c9e22619cbd19984fd87`.

## 1. Equation

Fix the electric-first shear

```
T_C(E,M) = (E+CM, M-C^t(E+CM)),
G=C^t C, E=Cz,
A_G = [[I,I],[-G,I-G]],
H_G(z,M) = z^t G z + M^t M + z^t G M,
B_G = [[2G,G],[G,2I]], H_G(y)=y^t B_G y/2.
```

Exactly five positive-offdiagonal Gram types are admitted:
`(2)`, `(3)`, `[[2,1],[1,2]]`, `[[2,1],[1,3]]`,
`[[3,1],[1,3]]`. Their dimensions are respectively 1,1,2,2,2.
Their offdiagonal sign-reversed markings are included by reversing one
whole face, with all associated coordinates transformed. Arbitrary diagonal
edge/face orientation signs describe the same five fixed cells, not new cells.

Audit the exact characteristic polynomials, determinant one, inverse,
active embedding and metric pullback, invariant raw and active energy,
energy definiteness boundary, and minimal orders. The disclosed target
orders are 4,3,6,5,infinite; the disclosed last polynomial is
`(X^2+1)(X+1)^2`. These are exposed hypotheses, not new measurements or
blind predictions. Infinite order requires a nonzero Jordan chain and an
all-integer-time argument in the proof; no finite failed-return search can
establish it. Identify the canonical `A_f`, `B_f`, and coordinate convention
exactly, without changing the marked field law.

## 2. Code

The accepted source is the adjacent standard-library `verify.py`; the
immutable pin contains this PREREG, SOURCES.json, PROOF.md, LINEAGE.md,
README.md and verify.py. No author program, output or historical exploratory
program is imported. The independently authored checker uses exact integers
and rational elimination, direct polynomial determinant expansion, coefficient
matrix identities and the declared finite orientation family. No floating
point, external library, random choice or network access is used.

Before the first scientific run, commit and push the complete package and
read back the exact Git pin and file hashes. Static syntax checking is allowed
before that pin; importing or running this verifier, or an equivalent
exploratory calculation, is not. The first stdout is preserved unchanged,
including any scientific failure. The identifier and frozen inputs cannot
be repaired or reused after the pin.

## 3. Carrier and data

All matrices act on their complete declared integer lattices, with the
energy classification extended to their full real vector spaces. Active
coordinates are `(z_0,...,z_(k-1),M_0,...,M_(k-1))` and raw coordinates
are `(E_0,...,E_(m-1),M_0,...,M_(k-1))`. Literal equality is entrywise in
these ordered bases. Divergence uses +tail/-head.

The complete representatives below freeze ordered edges (parallel edges
are distinct) and rows of the edge-face boundary C. Faces are unweighted
oriented finite CW cells, so digons with two distinct parallel edges are
admitted; no claim that these are simple-graph triangles is made.

| Type | Vertices | Ordered edges | Rows of C |
|---|---|---|---|
| digon | 0,1 | 01,01 | (1),(-1) |
| triangle | 0,1,2 | 01,12,20 | (1),(1),(1) |
| digon-digon | 0,1 | 01,01,01 | (1,1),(-1,0),(0,-1) |
| digon-triangle | 0,1,2 | 01,01,02,21 | (1,1),(-1,0),(0,-1),(0,-1) |
| triangle-triangle | 0,1,2,3 | 01,12,20,13,30 | (1,1),(1,0),(1,0),(0,1),(0,1) |

For each case audit all `R=diag(+/-1)` on its m edges and all
`S=diag(+/-1)` on its k faces: `C'=RCS`, `D'=DR`, `G'=SGS`.
The complete orientation audit comprises 8+16+32+64+128=248 cases.
Reversing an edge alone leaves G unchanged. Offdiagonal reversal is a face
orientation change, not an isolated edit of one boundary coefficient.

The active embedding is `P_C=diag(C,I)`. The real/rational static complement
is `ker(C^t)` in the electric coordinates. This does not assert a direct
integral splitting of every raw integer state. No state enumeration or
empirical dataset is admitted or required. `SOURCES.json` binds all allowed
canonical files to the exact v102 basis and supplies the pre-pin reviewer
source boundary.

The manifest also stores the minimal canonical `C`, `A_f` and `B_f` matrix
excerpt used at runtime. Its SHA-256 is frozen in verify.py. Full canonical
file hashes are provenance of the immutable source commit and are checked
before pinning; replay reads only the frozen local manifest, never mutable
future Canon bytes. Audit-only notes listed separately in the manifest are
author lineage inputs, not admitted pre-pin scientific inputs for RC.

## 4. Systematics and provenance

The immutable mathematical basis is public `canon-v102`, peeled commit
`a632c6a162dc87e60104d7a478e7650a6d5c4a1b`, content commit
`b04e22dd3ed8e4240cff347364f24670d4183a4d`. The normative hashes, tag
and ancestry were read back. Main CI 38939750393, tag publication
38940217812 attempt 3 and release readback 38956254023 attempt 2 all
succeeded before this probe's first execution. The release gate is not
substituted by the local audit.

General shear invariance/positivity, the one-triangle order-three law,
the two-triangle zero-energy boundary and the chosen canonical order-five
field already occur in v102. LINEAGE.md records the bounded novelty audit;
no duplicate general theorem or physical selection claim is proposed.

The supplied analysis mentioned `v103_kontrola.py` but supplied neither that
program nor its run capture. It was not read or used. Exposed results from
the dispatch are declared above. Same-session helpers contribute proof and
static review; their work is not the distinct RC scientific audit.

Run from the repository root using exactly:

```
python3 probes/P-FIELD-CELL-SHEAR-CENSUS-1/verify.py
```

Environment: `LC_ALL=C`, `LANG=C`, `TZ=UTC`, `PYTHONHASHSEED=0`,
`PYTHONDONTWRITEBYTECODE=1`. Capture stdout/stderr separately outside the
checkout, with a 600-second limit. Use a clean exact-pin Linux or
Linux-compatible checkout. Record Python/platform/architecture, return code,
byte/line counts and SHA-256. GitHub must later replay the result on the
required x86_64 and aarch64 Python 3.12 jobs with byte-identical stdout.

## 5. Failure threshold and disposition

Zero tolerance: any incorrect boundary/Gram identity, inverse, determinant,
characteristic polynomial, metric identity, positivity claim, asserted minimal
order, nonzero Jordan-chain certificate, canonical-basis equality or
orientation conjugacy is a scientific failure at exactly that claim's scope.
No failed threshold is changed. Algebraic test failures print
`SCIENTIFIC_FAIL` and end with `FIELD_CELL_SHEAR_CENSUS_SCIENTIFIC_FAIL`,
with exit zero so the completed negative result is retained and replayed.
The failing case stops at its first failed assertion; other independent
cases continue, and the aggregate verdict retains every reported failure.

Mismatched source bytes/hashes are `INTEGRITY_STOP`, not a mathematical
counterexample. Unexpected exceptions, nonzero exit, stderr or timeout are
execution/integrity failures and receive the repository's applicable
disposition; they may not be relabeled as a successful scientific result.
Proof gaps or incorrect universal reasoning remain UNRESOLVED even if the
finite checker passes. A bounded orientation audit is not the proof for
arbitrary states or unbounded times. PASS does not establish independence,
physical implementation or Canon promotion.

## 6. Action layer and exclusions

Action layer: L1. All conclusions are conditional on the five fixed CW-cell
incidences, coordinate marking, integer carrier, metric and update order.
No L2-L6 lift is claimed. No classification of all two-face complexes,
longer faces, weights, extra shared edges, arbitrary graphs or other field
laws is attempted. No selection of p=5, physical apparatus, native-U lift,
source transport, contact, energy-selection law or Canon modification follows.

## Independent RC exposure contract

Before its own derivation/pin, RC may read this PREREG and SOURCES.json,
the released #1548 specification and the canonical files named as allowed
scientific inputs in SOURCES.json. It must not read this author's PROOF.md,
LINEAGE.md, verify.py, EXPECTED.txt, RUN.md, RESULT.md, or a diff exposing
them. README is only navigation and is not an additional scientific input.
RC's result is separate work with a different owner; this author does not
create or certify it. Shared #1548 receipts contain metadata only.
