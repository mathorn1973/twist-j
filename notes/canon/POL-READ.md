# POL-READ. Exact square readout proposal

**NON-CANONICAL PROPOSAL.** This file has no authority and changes no claim
status. It proposes one later, separately reviewed and versioned Canon fold.

```text
public issue        #82
base                Public Canon v11 ACTIVE
base main           3d8c6307f20d01ad50fc90ae1c5777926b884881
claim               POL-READ
current status      O
proposed status     D
action layer        NOT_APPLICABLE
formal probe        none
```

The eventual fold must start from the then-current public `main`. The base
above is the currency stamp for this proposal only.

## 1. Falsifier first

The positive closure fails if any one of the following is true:

1. `h_+` and `h_x` are not the two real coordinate polynomials of the
   registered complex square;
2. an exact rotation of the input doublet does not induce the doubled-angle
   rotation of the output pair;
3. the readout requires a propagation law outside the registered family
   `c = 1 - s^2`;
4. the proposed reading claims a source map, quasinormal inference, action,
   normalization, numerical tensor ratio, or wider propagation theorem.

Items 1 to 3 do not fire. Item 4 is excluded by scope below.

## 2. Exact derivation

Freeze the registered decoder `TT-SQUARING-DECODER [D]`:

```text
v = v_1 + i v_2,
h = h_+ + i h_x = v^2.
```

Expansion in the polynomial ring gives

```text
h_+ = v_1^2 - v_2^2,
h_x = 2 v_1 v_2.
```

These are not two independent decoder choices. They are the two coordinates
of the one registered complex square.

Freeze an exact input-doublet rotation by elements `a,b` with
`a^2 + b^2 = 1`:

```text
v_1' = a v_1 - b v_2,
v_2' = b v_1 + a v_2.
```

Direct polynomial expansion gives

```text
h_+' = (a^2 - b^2) h_+ - 2ab h_x,
h_x' = 2ab h_+ + (a^2 - b^2) h_x.
```

This is the exact doubled-angle law. If `a = cos(alpha)` and
`b = sin(alpha)`, it may be abbreviated as `h -> exp(2 i alpha) h`, but the
polynomial identity above carries the result. Under conjugation
`v_2 -> -v_2`, `h_+` is fixed and `h_x` changes sign.

The output is therefore a spin-2 component pair under the declared input
frame convention. Calling the two coordinates plus and cross is a physical
decoder dictionary, so the result has status ceiling `D`, not `T`.

The component readout introduces no new propagation law. The only registered
propagation statement remains

```text
c = 1 - s^2.
```

The coordinate expansion does not add a componentwise amplitude evolution or
assert `h -> -3h`. It satisfies the positive decision condition of
`POL-READ [O]` without triggering its negative condition.

## 3. Existing evidence

The stable public reproduction `reproduce/coupling-metrology` already
constructs

```text
h_+ = v_1^2 - v_2^2,
h_x = 2 v_1 v_2,
```

checks their complex square, checks the `{+-1}` kernel and spin double cover,
and separately checks the registered values of `c(s)` at `s = 0, 1, 2`,
giving `c = +1, 0, -3`. It does not audit the doubled-angle covariance; that
identity is proved exactly above.

The later fold must retain `EV-POL-READ` as one `INLINE_CANON` evidence row,
re-pinned to the new Canon hash. It must not claim two evidence locations or
fabricate a two-architecture result for this dictionary derivation. The
existing reproduction remains the evidence of the required parent
`TT-SQUARING-DECODER [D]`.

## 4. Scope firewall

The proposed `D` row states only:

1. the component expansion of the registered complex square;
2. its exact doubled-angle frame law and conjugation parity;
3. that the readout introduces no independent propagation law.

It does not close or alter:

```text
TT-SOURCE                       O
QNM-LEAVER-MU                   O
TT-VECTOR-STATE-NORMALIZATION   O
TT-QUADRATIC-GERM               D
SCHWARZSCHILD-TT-ENDPOINT       T
```

It supplies no emission source, no shadow-to-mu inference rule, no vector
state or action normalization, no scalar comparison, no numerical `r_T(k)`,
no helicity selection, no detector response, and no uniqueness theorem beyond
the registered square.

## 5. Exact proposed registry row

The later fold may use this six-column TSV row exactly. The final dash records
an empty decision condition for the closed claim without trailing whitespace:

```tsv
POL-READ	D	the polarization readout of the registered TT square: h_+ = v1^2 - v2^2 and h_x = 2 v1 v2; for an exact input-doublet rotation v1' = a v1 - b v2, v2' = b v1 + a v2 with a^2 + b^2 = 1, the pair (h_+, h_x) transforms by ((a^2 - b^2, -2ab), (2ab, a^2 - b^2)), the doubled-angle spin-2 law, and conjugation fixes h_+ and negates h_x; a decoder dictionary derived from TT-SQUARING-DECODER, with no independent propagation law, source map, state normalization, helicity selection, detector response, or numerical observable claimed	14. The gravitational wave program	inline	-
```

The UTF-8 SHA-256 of the exact scope field in that row is

```text
c764fe8a00b4dd265563b14449a5cb53c7489dab77298c5761f4b8b6ae7b2bbc
```

Do not add a second `POL-SQUARE-READOUT [T]` row. The exact algebra belongs
inside the one dictionary claim whose physical component naming fixes the
status ceiling at `D`.

## 6. Proposed Canon text

In section 14, immediately after the sentence that declares
`TT-SQUARING-DECODER [D]`, add a paragraph equivalent in scope to:

```text
Writing v = v_1 + i v_2 and h = h_+ + i h_x, the same square gives
h_+ = v_1^2 - v_2^2 and h_x = 2 v_1 v_2. For the exact input-frame rotation
v_1' = a v_1 - b v_2, v_2' = b v_1 + a v_2 with a^2 + b^2 = 1, the pair
transforms by the matrix ((a^2-b^2,-2ab),(2ab,a^2-b^2)), the doubled-angle
spin-2 law; conjugation fixes h_+ and negates h_x. The two coordinates are
read as plus and cross (POL-READ [D]). This readout introduces no independent
propagation law, source map, detector convention, action normalization, or
numerical tensor ratio.
```

Remove `POL-READ` from the sentence that lists live section 14 obligations.
Resolve that sentence's grammar without strengthening the scope of
`QNM-LEAVER-MU`.

## 7. Companion-ledger edits in the later fold

`canon/NORMATIVE.tsv`:

```tsv
POL-READ	DICTIONARY	POL-READ	D	NOT_APPLICABLE		canon/CANON.md::14. The gravitational wave program
```

Retain the existing architecture dependency and add to
`canon/DEPENDENCIES.tsv`:

```tsv
POL-READ	TT-SQUARING-DECODER	REQUIRES	the plus/cross components, conjugation parity, and doubled-angle covariance are exact polynomial consequences of the registered complex square; no independent propagation law is introduced
POL-READ	TT-SOURCE	BOUNDED_BY	the component readout does not construct the still-open emission map
POL-READ	TT-VECTOR-STATE-NORMALIZATION	BOUNDED_BY	the component readout does not select a state normalization or produce a numerical r_T(k)
```

`canon/EVIDENCE.tsv` must retain one evidence row:

```tsv
POL-READ	EV-POL-READ	INLINE_CANON	inline	<V12_CANON_SHA256>	file-sha256	none
```

`canon/HISTORY.tsv` must append the next contiguous `POL-READ` event:

```tsv
CANON12-POL-READ	12	<FOLD-DATE>	canon-v12	POL-READ	STATUS_CHANGE	O	D	c764fe8a00b4dd265563b14449a5cb53c7489dab77298c5761f4b8b6ae7b2bbc	EV-POL-READ	inline	<V12_CANON_SHA256>	Exact polynomial expansion of the registered TT square yields the plus/cross components, conjugation parity, and doubled-angle covariance; the physical naming remains a decoder dictionary and no second propagation law is introduced
```

Do not write this event before the v12 content fold exists. Because inline
evidence hashes the whole Canon, every other `INLINE_CANON` row must also be
re-pinned to the v12 Canon hash, with its next contiguous `EVIDENCE_CHANGE`
history event. At v11 there are 39 such other claims. Their usual next event
sequence is 12, with these exceptions:

```text
CURVATURE-OPERATOR-CANONICAL   11
O-R2-K-JUNCTION-PIN             4
CARRY-J-CHECKPOINT              2
```

The expected v12 status partition after this one status change is

```text
claims       190
T             93
D             39
C             21
H              6
O             22
F              9
live H/O       28
```

Update only the expected partition in
`reproduce/status-separation/verify.py` from `D=38, O=23` to `D=39, O=22`.
Its stdout is status-invariant and `EXPECTED.txt` should remain unchanged.

Regenerate `canon/FRONTIER.md`; `POL-READ` must disappear from the live
frontier. Regenerate `canon/CORE.md` only through the repository generator and
do not add `POL-READ` to `CORE_SELECTION.tsv` without separate justification.

## 8. Version and activation boundary

Public Canon v11 remains authoritative while this proposal is reviewed. The
proposal branch must not edit `canon/CANON.md`, `canon/REGISTRY.tsv`, companion
ledgers, `STATUS.md`, or `canon/SHA256SUMS`.

The later content fold must start from the then-current public `main` and
produce the normal integer-versioned Canon bundle. Its expected file surface
is:

```text
canon/CANON.md
canon/REGISTRY.tsv
canon/NORMATIVE.tsv
canon/DEPENDENCIES.tsv
canon/EVIDENCE.tsv
canon/HISTORY.tsv
canon/FRONTIER.md
canon/CORE.md
canon/CHANGELOG.md
canon/STATUS_COUNTS.tsv
canon/SHA256SUMS
reproduce/status-separation/verify.py
```

The separate release-form commit changes only:

```text
STATUS.md
README.md
CITATION.cff
```

It records the actual v12 content commit, Canon SHA-256, byte count, version,
and release date. The v11 activation tuple remains authoritative until that
release-form commit is merged, tagged `canon-v12`, and passes public readback.
No frontier decrement is counted before activation.

## 9. Validation checklist for the later fold

The later fold must run and pass, at minimum:

```text
python tools/generate_canon_views.py --apply
python tools/generate_canon_views.py --check-dir canon
python tools/check_policy.py
python -m unittest discover -s tools -p "test_*.py"
python tools/check_canon.py
python tools/check_ledger.py
python tools/check_verifier.py --base <ACTUAL_FOLD_BASE_COMMIT>
python tools/check_reproduce.py --base <ACTUAL_FOLD_BASE_COMMIT>
python tools/check_activation.py --full --content-commit <V12_CONTENT_COMMIT>
git diff --check
```

It must also perform a named-file security review. This proposal contains no
secret, credential, private hostname, private log, personal data, binary
model, or third-party material.
