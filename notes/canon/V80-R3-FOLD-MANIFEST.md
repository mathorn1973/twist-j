# Public Canon v80 r3 fold manifest

**NON-CANONICAL / SEALED FOLD INPUT / NO AUTHORITY.**

Issue: #881. Date: 2026-09-07. Author: A. M. Thorn.

This file freezes the complete intended delta for a fresh Public Canon v80
candidate. It does not itself change Canon, Registry, Frontier, status, tag or
release authority.

## 1. Basis and supersession

Public basis at freeze:

```text
main              1ea039d5a488042cbc4d722cc7dc7b1d3f8d841e
STATE             ACTIVE
Public Canon      v79
content commit    48ede94165472e2d77896a7c20ddb3c567f3bcc1
CANON sha256      025b07fe39ec4ab857a50adf467acc640334a1ea0cb87e8f9500b90948896764
CANON bytes       516701
```

The unpublished v80 candidate PR #874 is a source only. Its exact content
commit is

```text
79f09fb50530ec2f39dc4be8e972038a04ef746c
```

and its release head is

```text
5e09ae379acd833846e3186dae1915e0eec3344b
```

No tag or release was published. The r3 fold supersedes that candidate without
rewriting either commit or branch.

Between #874's old base `a51df34fe1f1f433062faeb18f5e03fd0a8082b2`
and the r3 basis above, public main added only the three probe directories
created by #876, #878 and #880. No Canon, Policy, Agent, workflow or repository
checker byte moved. Therefore the old v80 content is transported by exact Git
blob identity, not rewritten from an attachment or local snapshot.

## 2. Retained v80 content

Retain unchanged the three theorem-grade rows and their exact old-v80 statement,
ledger, dependency and evidence bytes:

```text
U-NATIVE-COMMON-READY-SOURCE-RETENTION          [T]
QDD-INCIDENCE-FIRST-HIT-CLASSIFICATION          [T]
QDD-MIXED-CHANNEL-ATTENUATION-RIGIDITY          [T]
```

Their evidence remains `P-QDD-V80-CLOSURE-BOUNDARIES-1`; their public probe
bundle and the old v80 reconciliation are not rewritten.

The old v80 content commit is the byte source for these paths before applying
the explicit r3 edits below:

```text
canon/CANON.md
canon/CHANGELOG.md
canon/DEPENDENCIES.tsv
canon/EVIDENCE.tsv
canon/FRONTIER_PROGRAMS.tsv
canon/HISTORY.tsv
canon/NORMATIVE.tsv
canon/REGISTRY.tsv
canon/SHA256SUMS
canon/STATUS_COUNTS.tsv
notes/canon/V80-DETERMINISTIC-PERMUTATION-PROFILE.md
reproduce/status-separation/EXPECTED.txt
reproduce/status-separation/README.md
reproduce/status-separation/verify.py
tools/test_architecture_map_report.py
```

`notes/canon/V80-RECONCILIATION.md` is replaced by the r3 reconciliation,
not copied as final text.

## 3. New registered theorem A

Claim id:

```text
A4-RATIONAL-FRAME-WEIGHT-NONUNIQUENESS
```

Status/layer/type:

```text
T / L4 / THEOREM
```

Registry scope, byte exact between the backticks:

```text
at L4 on rational rays of A4={v in Z^5:sum v_i=0} with q(v)=sum v_i^2 and complete rational orthogonal frames, the ternary norm-residue H([v])=h_3(q(v)) is projectively well defined and has sum H=0 on every complete frame; therefore w_t=1/4+tH is a normalized nonnegative frame weight for every rational |t|<=1/4 and uniformly strictly positive for |t|<1/4; all 30 inner Cl(4) rays retain 1/4 while the frozen equal-projector equilateral cover has defect D=3t, so every t!=0 member is nonquadratic; hence positivity plus noncontextual complete-frame additivity do not force the owner-adopted quadratic reading, without asserting a physical realization of the alternative weights or rejecting the chosen quadratic decoder
```

Scope SHA-256:

```text
230c7563ab84a21fec0bc0b51584463dc52251094709c206cb0c9472ca7814b6
```

Canon section:

```text
2. Time, space, and the decoder
```

Falsifier, byte exact:

```text
fires on an exact rational A4 ray whose H value changes under rational rescaling, an exact complete rational orthogonal frame with nonzero H-sum, failure of positivity or normalization in the stated t range, failure of the frozen equal-projector cover or D=3t, or a single symmetric quadratic form representing a nonzero-t member; physical realization of a different reading is outside this mathematical claim
```

Normative row:

```text
A4-RATIONAL-FRAME-WEIGHT-NONUNIQUENESS	THEOREM	A4-RATIONAL-FRAME-WEIGHT-NONUNIQUENESS	T	L4		canon/CANON.md::A4-RATIONAL-FRAME-WEIGHT-NONUNIQUENESS
```

Registry row:

```text
A4-RATIONAL-FRAME-WEIGHT-NONUNIQUENESS	T	at L4 on rational rays of A4={v in Z^5:sum v_i=0} with q(v)=sum v_i^2 and complete rational orthogonal frames, the ternary norm-residue H([v])=h_3(q(v)) is projectively well defined and has sum H=0 on every complete frame; therefore w_t=1/4+tH is a normalized nonnegative frame weight for every rational |t|<=1/4 and uniformly strictly positive for |t|<1/4; all 30 inner Cl(4) rays retain 1/4 while the frozen equal-projector equilateral cover has defect D=3t, so every t!=0 member is nonquadratic; hence positivity plus noncontextual complete-frame additivity do not force the owner-adopted quadratic reading, without asserting a physical realization of the alternative weights or rejecting the chosen quadratic decoder	2. Time, space, and the decoder	inline	fires on an exact rational A4 ray whose H value changes under rational rescaling, an exact complete rational orthogonal frame with nonzero H-sum, failure of positivity or normalization in the stated t range, failure of the frozen equal-projector cover or D=3t, or a single symmetric quadratic form representing a nonzero-t member; physical realization of a different reading is outside this mathematical claim
```

Evidence row:

```text
A4-RATIONAL-FRAME-WEIGHT-NONUNIQUENESS	EV-A4-RATIONAL-FRAME-WEIGHT-NONUNIQUENESS	INLINE_CANON	inline	230c7563ab84a21fec0bc0b51584463dc52251094709c206cb0c9472ca7814b6	registry-scope-sha256-v1	none
```

History row:

```text
CANON80-DECLARE-A4-RATIONAL-FRAME-WEIGHT-NONUNIQUENESS	1	2026-09-07	canon-v80-candidate	A4-RATIONAL-FRAME-WEIGHT-NONUNIQUENESS	DECLARE		T	230c7563ab84a21fec0bc0b51584463dc52251094709c206cb0c9472ca7814b6	EV-A4-RATIONAL-FRAME-WEIGHT-NONUNIQUENESS	inline	230c7563ab84a21fec0bc0b51584463dc52251094709c206cb0c9472ca7814b6	Declare the exact global rational A4 frame-weight counterexample: positive complete-frame additivity does not force quadratic reading; no physical alternative reading is adopted.
```

No dependency or gate row is added.

Public theorem source retained for audit and provenance: merged probe
`probes/P-A4-RATIONAL-FRAME-WEIGHT-NONUNIQUENESS-1/`, PR #876. The Canon proof,
not the finite verifier, is the normative theorem evidence.

## 4. New registered theorem B

Claim id:

```text
QDD-SIMPLEX-PAIR-INCIDENCE
```

Status/layer/type:

```text
T / L4 / THEOREM
```

Registry scope, byte exact:

```text
at L4 for every regular simplex V_N={x in Q^N:sum x=0}, N>=2, integer source z in Z^(N-1), setting k and bijection beta to all vertices except k, with x=sum z_i u_beta(i), U=N(N-1), A=(sum z_i)^2, B=N sum_(i<j)(z_i-z_j)^2 and D=A+B: U is the least universal integer clearing both x and P_kx, X=Ux and its P/Q branches are integral, X recovers z exactly, a_k=N e_k-1 is the primitive LOW generator with q(a_k)=U, and q(P_kx)=A/U, q(Q_kx)=B/U, q(x)=D/U; A and B are literal ordered Cartesian-pair cardinalities, so the chosen quadratic read equals a second-order integer pair-incidence census; at N=p=5, U=20 and the public QDD identities A=s^2, B=5(4S2-s^2), D=4(5S2-s^2) are recovered; no uniqueness, physical apparatus, occurrence, sampling or L6 measure is claimed
```

Scope SHA-256:

```text
d39e676eaf7ec15b9f1e36ba0afa561d0674c4e4650df79ec998933b8ab6d8f0
```

Canon section:

```text
2. Time, space, and the decoder
```

Falsifier, byte exact:

```text
fires on any exact admitted N>=2 source or setting violating minimal lift U=N(N-1), integrality, source recovery, primitive LOW scale, Cartesian-pair cardinalities, P/Q norm identities, the nonzero-source ratios or the N=5 public specialization; a different decoder family or absence of physical realization is outside this L4 theorem
```

Normative row:

```text
QDD-SIMPLEX-PAIR-INCIDENCE	THEOREM	QDD-SIMPLEX-PAIR-INCIDENCE	T	L4		canon/CANON.md::QDD-SIMPLEX-PAIR-INCIDENCE
```

Registry row:

```text
QDD-SIMPLEX-PAIR-INCIDENCE	T	at L4 for every regular simplex V_N={x in Q^N:sum x=0}, N>=2, integer source z in Z^(N-1), setting k and bijection beta to all vertices except k, with x=sum z_i u_beta(i), U=N(N-1), A=(sum z_i)^2, B=N sum_(i<j)(z_i-z_j)^2 and D=A+B: U is the least universal integer clearing both x and P_kx, X=Ux and its P/Q branches are integral, X recovers z exactly, a_k=N e_k-1 is the primitive LOW generator with q(a_k)=U, and q(P_kx)=A/U, q(Q_kx)=B/U, q(x)=D/U; A and B are literal ordered Cartesian-pair cardinalities, so the chosen quadratic read equals a second-order integer pair-incidence census; at N=p=5, U=20 and the public QDD identities A=s^2, B=5(4S2-s^2), D=4(5S2-s^2) are recovered; no uniqueness, physical apparatus, occurrence, sampling or L6 measure is claimed	2. Time, space, and the decoder	inline	fires on any exact admitted N>=2 source or setting violating minimal lift U=N(N-1), integrality, source recovery, primitive LOW scale, Cartesian-pair cardinalities, P/Q norm identities, the nonzero-source ratios or the N=5 public specialization; a different decoder family or absence of physical realization is outside this L4 theorem
```

Evidence row:

```text
QDD-SIMPLEX-PAIR-INCIDENCE	EV-QDD-SIMPLEX-PAIR-INCIDENCE	INLINE_CANON	inline	d39e676eaf7ec15b9f1e36ba0afa561d0674c4e4650df79ec998933b8ab6d8f0	registry-scope-sha256-v1	none
```

History row:

```text
CANON80-DECLARE-QDD-SIMPLEX-PAIR-INCIDENCE	1	2026-09-07	canon-v80-candidate	QDD-SIMPLEX-PAIR-INCIDENCE	DECLARE		T	d39e676eaf7ec15b9f1e36ba0afa561d0674c4e4650df79ec998933b8ab6d8f0	EV-QDD-SIMPLEX-PAIR-INCIDENCE	inline	d39e676eaf7ec15b9f1e36ba0afa561d0674c4e4650df79ec998933b8ab6d8f0	Declare the uniform regular-simplex theorem identifying the chosen quadratic P/Q read with an exact second-order integer pair-incidence census and fixing U=20 at p=5 by integral simplex scale.
```

No dependency or gate row is added.

Public theorem source retained for audit and provenance: merged successor probe
`probes/P-QDD-SIMPLEX-PAIR-INCIDENCE-2/`, PR #880. Abandoned predecessor
`P-QDD-SIMPLEX-PAIR-INCIDENCE-1` carries no evidence and no status.

## 5. Canon insertion

Insert the exact text from `V80-R3-CANON-INSERT.md` immediately before

```text
## 3. The kernel and the census
```

in the old-v80 `canon/CANON.md` byte source. No existing old-v80 theorem text is
edited or paraphrased.

## 6. Ledger mechanics

Relative to old v80 content, prepend the two rows above to `REGISTRY.tsv`,
`NORMATIVE.tsv`, `EVIDENCE.tsv` and `HISTORY.tsv` after their headers, preserving
all old-v80 rows byte for byte. Do not add `DEPENDENCIES.tsv`, `GATES.tsv`,
`CORE_SELECTION.tsv` or `FRONTIER_PROGRAMS.tsv` rows for these claims.

The target exact ledger counts are:

```text
claims             398
normative items    447
dependencies       744
evidence           398
history            931
gates              15
frontier programs  8
```

The target `STATUS_COUNTS.tsv` is:

```text
METRIC	VALUE
claims	398
T-LOCK	0
T	266
D	45
C	39
H	2
O	28
F	18
live_H_O	30
reproductions	24
evidence_none	50
one-architecture	9
recorded-audit	31
two-architecture	308
```

The evidence architecture counts sum to 398. Both new theorem rows use
`architecture_requirement=none` because their normative evidence is the
self-contained Canon proof. The successful public two-architecture probe runs
are audit/provenance support and are named in reconciliation.

Because neither new theorem has a dependency edge, retain the old-v80
architecture-map expected sets and counts:

```text
direct_architecture_requires        182
transitive_architecture_dependents  258
dependency_terminals                 61
```

## 7. Changelog meaning

The v80 changelog entry must retain the old three-result content and append this
reading-boundary paragraph, without changing any old result status:

> Two later L4 theorems delimit the quadratic decoder without selecting a
> physical apparatus. A4-RATIONAL-FRAME-WEIGHT-NONUNIQUENESS proves that
> positivity and complete rational-frame additivity do not make quadratic
> reading globally unique. QDD-SIMPLEX-PAIR-INCIDENCE proves, independently,
> that the owner-adopted quadratic P/Q branch is exactly a second-order integer
> Cartesian-pair census on the regular-simplex relation, with the minimal
> integral scale U=N(N-1) and U=20 at p=5. Thus v80 records both plurality and
> a structural reason for the chosen reading. No physical QDD O owner moves.

## 8. Frontier and physical firewall

All old v80 live H/O rows retain status, scope, evidence, falsifier, scheduler
metadata and decision condition. In particular these stay O / STOP:

```text
QDD-INSTRUMENT-APPARATUS
QDD-INSTRUMENT-CLASS-COMPLETENESS
QDD-TERMINAL-EVENT-SEMANTICS
```

Neither new theorem supplies a physical effect, selected apparatus, ready
state, coupling, pointer, exclusive occurrence, onset law, sampling law,
post-state selection, reset, L1-to-L5 lift or L6 measure. The pair sets are
mathematical relations, not detector clicks. The nonquadratic frame weights are
mathematical alternatives, not adopted physical readings.

The public reading-family discipline remains unchanged: global decoder
uniqueness is not required; a reading may not be selected after inspecting the
target result.

## 9. Reconciliation and release shape

`V80-R3-RECONCILIATION.md` is the r3 review input and names #874, #876, #878,
#880 and #881 explicitly. The abandoned #877 lane earns nothing.

After the complete content tree passes policy, Canon, ledger, gate, generated
view, architecture-map, status-separation and full probe/reproduction sweeps,
freeze exactly one content commit based on current public main. Then create one
release-form commit changing exactly:

```text
STATUS.md
README.md
CITATION.cff
```

The release-form values must be generated from that exact content commit and
its final `canon/CANON.md` SHA-256 and byte count. Do not reuse the old #874
content hash, byte count, STATUS commit or release head.

This issue and manifest authorize a release candidate PR only. They do not
authorize tagging, publishing a release or changing twistj.com.
