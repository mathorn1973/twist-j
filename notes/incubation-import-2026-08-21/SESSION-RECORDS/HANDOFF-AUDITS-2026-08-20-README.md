# HANDOFF-AUDITS-2026-08-20

```text
STATUS:      NON-CANONICAL handoff bundle. No authority.
AUTHORITY:   none. This directory creates no claim, no Registry row, no
             evidence entry, no probe permission and no status change. It
             edits no normative file. RH remains O. QDD-INSTRUMENT-APPARATUS
             remains O with both blockers open. SAMPLING NOT PROVIDED.
CONTENTS:    two independent audits carried out in one Cowork session on
             2026-08-20, each with its own preregistration frozen and hashed
             before execution, its own exact verifier, its own recorded
             stdout, and its own findings; plus the correction leg opened by
             the owner review of the second audit.
LAYER:       L6 measure and spectral for the first audit; L4
             apparatus/support for the second. Neither lifts.
DISCLOSURE:  RESULT-EXPOSED / IMPLEMENTATION-INDEPENDENT / NOT BLIND. Both
             audits are independent in implementation and derivation. Neither
             is blind: the sealed results and their expected structure were
             known in advance.
```

## 1. Authority now, and the basis the audits used

Current public authority at the time this branch was written:

```text
STATE:          ACTIVE
CANON:          Public Canon v57
AUTHORITY:      mathorn1973/twist-j main
TAG:            canon-v57
CONTENT_COMMIT: 8e8b04abe4d3359942449533854ef1d142be70df
CANON_SHA256:   c96a2ef52c78d68ef8f04b582e4a17328e6a863b49664f29b1bd324171d802a8
CANON_BYTES:    295013
MAIN_AT_WRITE:  4ef54f0c34f80897af0121a2d93b710e70a8377c
```

Both audits were performed earlier the same day, against Public Canon v56,
which was `ACTIVE` then:

```text
CANON:          Public Canon v56
TAG:            canon-v56
CONTENT_COMMIT: b36c93ed8ce24a9cbd771168094db04f5a5ac06c
CANON_SHA256:   b284ed6e78341aa6e3a74652d6f1f8f4079c270461f28bf32f2d95a6bd8b6645
CANON_BYTES:    288492
main at audit:  4ed6cb72ab1110b68ed0574115e9dacbaf65e954
```

The currency gate was run at the start of the session: `STATE ACTIVE`,
`canon/SHA256SUMS` five of five OK, tag and content commit both verified as
ancestors of `main`.

The basis relation is stated as a pair, so that neither half can be quoted
alone:

```text
the audited probe directories are byte-identical between the v56 state the
audits used and current main;
canon/ is NOT byte-identical, because Public Canon v57 has since activated;
the audited rows are unchanged in status and text.
```

Checked explicitly, and machine-checked in the correction leg:

```text
canon/REGISTRY.tsv rows LAMBDA-COCYCLE-ANGLES, LAMBDA-COCYCLE-BRANCH-COLLAPSE,
  LAMBDA-COCYCLE-GRID-EQUIVALENCE, QDD-INSTRUMENT-APPARATUS and
  QDD-INSTRUMENT-NONSELECTION            identical at v56 and v57
probes/P-LAMBDA-COCYCLE-ANGLES-1         identical
probes/P-LAMBDA-COCYCLE-ANGLES-2         identical
probes/P-QDD-J-CENTRALIZER-TERMINALITY-1 identical
canon/CANON.md                           DIFFERS (v57 activation)
```

What v57 changed: five closed rows added (`J-MAHLER-MEASURE`,
`REGULATOR-TWO-LOG-PHI`, `CYCLOTOMIC-CLASS-NUMBER-ONE` at T,
`J-TORAL-PERIODIC-POINTS`, `METRO-FORBIDDEN-WITNESSES` at C) and the scope
text of one existing row, `METRO-REDUCTION-CALCULUS`, which stays at O. No
live row moved.

Nothing in either audit depends on Canon prose, and every sealed object they
check is unchanged, so the basis move changes no result. A reader who wants
the audits re-run against v57 should re-run them.

## 2. `lambda-grid/`, the angular clause of `LAMBDA-COCYCLE-ANGLES [H]`

Question asked: not RH, but the placement of the Cayley angles into
`2 pi (1/4) Z[1/5]`.

Result: the lattice is not a free parameter. It is re-derived as forced by
four routes that coincide, the fourth of which is new in this audit:

```text
(a) the point spectrum of U_J, orbit lengths {1} union {4 . 5^a};
(b) the arithmetic set of reduced fractions with denominator 2^e 5^f, e <= 2;
(c) NEW: the roots of unity of the lambda-adic cyclotomic tower are exactly
    mu_4 x mu_(5^infinity), with mu_3 and mu_8 blocked at the residue field
    and total ramification certified by Eisenstein at x + 1; hence the grid
    is maximal for every lambda-adic torsion transport, not only for U_J;
(d) the annihilation reading dist(4 . 5^A x, Z) -> 0.
```

The factor `1/4` is `ord(J mod lambda) = ord(2 in F_5^x)` and is already
forced by the uniformizer itself: `(1 - zeta^4)(-zeta) = 1 - zeta` gives the
turn of `lambda` as `17/20`, on the grid and not in `(1/2) Z[1/5]`.

Weight of the clause, unchanged in status: the hypothesis is exactly the
statement that every ordinate is `(1/2) cot(pi m/(4 . 5^a))`, an explicit
abelian algebraic number. It is strictly stronger than RH; it is not decidable
by any finite computation, since the grid ordinates are dense; the honest
attack surface is the tail clause family, not the pointwise clause. The row is
correct as registered and its `H` is the right label.

Two local falsifiers of the audit fired, both on the audit's own material and
neither against a public row. They are archived in section 6 of the audit
record together with the corrected values, and the correction leg
`verify_lambda_grid_audit_1b.py` is included.

## 3. `qdd-terminality/`, the bifurcation of `P-QDD-J-CENTRALIZER-TERMINALITY-1`

An independent audit of the sealed probe merged by pull request 462, rebuilt
from the axiom step map by fresh code with no import from the probe directory
and with the target effects compared last. Thirty-two exact gates, all pass,
zero findings. The sealed pin hashes match and the sealed verifier reproduces
byte-identically.

The reduction it adds, in the corrected wording of section 4 below:

```text
PROJECTIVE-TERMINALITY-REDUCTION.
Inside the frozen class the sign equivalence T ~ -T is a congruence for
composition, so the post-state quotient is a group with identity [Q_k].
Fresh-pointer ray terminality is equivalent, inside this class, to

    [T]^2 = [T],

and since every [T] is invertible the only idempotent is the identity.
Equivalently T^2 = +T or T^2 = -T iff T = +Q_k or T = -Q_k. Weaker than
strict representative idempotence, physically equivalent to the unique
Lueders class. It compresses the terminality selector inside the frozen
class; it does not derive terminality, prove the class globally exhaustive,
or close O2.                                              [candidate-T]
```

The negative-route survivor `[R - C]` is exactly a non-terminal involution:
`(R - C)^2 = Q` while `Q` is not `+/- (R - C)`, and on `w = w_R + w_C` it
moves `w` off its own line and back. Repeatability of the outcome is not
terminality of the post-state.

## 4. `qdd-terminality/` correction leg, from the owner review

The owner reviewed the QDD audit and returned a `PRE-RUN / STOP` verdict with
four required corrections. It arrived after the audit had been frozen,
executed and published, so the corrections are applied by addendum, in the way
POLICY treats a sealed object: nothing pinned is edited.

```text
basis          corrected to v57 with the pair statement of section 1; the
               published sentence claiming canon/ byte-identity was true only
               for the pre-v57 pair it was written about, and is withdrawn.
freeze         gap admitted: the first leg froze the preregistration but bound
               the program only by description. The correction leg freezes
               preregistration and program together, ast-parse only before the
               pin, with byte, LF, CR and final-LF counts in AUDIT_PIN-CORRECTION.txt.
custody        chain of custody added, CH1 to CH8, all pass: pin ancestry,
               blob identity at four commits, absence of result files at the
               pin, no post-pin change, current-main equality, clean worktree,
               and HEAD exactly at the audited merge.
proofs         QA2 and QA3 now carry written universal proofs rather than
               samples: the rational-circle injection t = s/(1 + r) with
               1 + r = 2/(1 + t^2) nonzero, the sharp-coordinate identity
               T^sharp = eR + rC - sJ forcing s = 0, and the three-line scalar
               lemma for line-preserving maps.
QA6            restated as projective idempotence in the named quotient, with
               the universal proof T^sharp T^2 = (T^sharp T) T = Q T = T
               against T^sharp(eps T) = eps Q, hence T = eps Q. The earlier
               phrase "one post-state-class equation for O2" is withdrawn as
               too suggestive.
grammar        fixed-order gates, no fail-fast, decision word and return codes
               0 AUDIT-PASS, 1 AUDIT-INTEGRITY-STOP, 2 AUDIT-DISAGREEMENT.
```

Correction leg decision: `AUDIT-PASS`, 8/8 chain gates, 5/5 proof inputs.

## 5. What a reader may and may not take from this bundle

```text
MAY   the exact identities, the certificates, the recorded stdout, the fired
      falsifiers, the reduction of section 3, and the reading of the weight
      of the angular clause in section 2.
MAY NOT  any status change. Every earned label is a candidate label. Nothing
      here is public T, nothing here is evidence for a Registry row, and no
      summary of this bundle may exceed the status or scope of the sealed
      rows it audits. Neither O1 nor O2 is moved.
```

## 6. Reproduction

Every program is Python standard library only, exact integer and `Fraction`
arithmetic, with no floating-point value formed in any assertion. Frozen
command:

```text
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC python3 <file>
```

Three programs, `breaker_lambda_grid_audit_1.py`,
`audit_qdd_centralizer_1.py` and `audit_qdd_chain_1.py`, read a repository
checkout by absolute path and therefore carry the audit sandbox path in one
assignment each. The files are shipped exactly as executed, because their
hashes are part of the run record; a reproducer must edit that one line to
point at a local checkout, which changes the file hash by design and is
expected. `SECOND-LEG.md` records a byte-identical replay of all four
first-audit programs on a second architecture.

`SHA256SUMS` covers every file in this directory except itself.

## 7. Inventory

```text
lambda-grid/PREREG-AUDIT-LAMBDA-GRID-1.md          frozen before execution
lambda-grid/AUDIT-LAMBDA-COCYCLE-GRID_2026-08-20.md the audit record
lambda-grid/verify_lambda_grid_audit_1.py          primary verifier
lambda-grid/verify_lambda_grid_audit_1.stdout.txt  51/52 PASS, one CONJ fired
lambda-grid/verify_lambda_grid_audit_1b.py         correction leg
lambda-grid/verify_lambda_grid_audit_1b.stdout.txt 12/12 PASS
lambda-grid/breaker_lambda_grid_audit_1.py         attack pass and reproduction
lambda-grid/breaker_lambda_grid_audit_1.stdout.txt FINDINGS 0 of 15
qdd-terminality/PREREG-AUDIT-QDD-TERMINALITY-1.md  frozen before execution
qdd-terminality/AUDIT-QDD-CENTRALIZER-TERMINALITY_2026-08-20.md the audit record
qdd-terminality/audit_qdd_centralizer_1.py         independent audit program
qdd-terminality/audit_qdd_centralizer_1.stdout.txt 32/32 PASS
qdd-terminality/PREREG-AUDIT-QDD-TERMINALITY-1-CORRECTION.md  correction prereg
qdd-terminality/AUDIT_PIN-CORRECTION.txt           pin of prereg and program
qdd-terminality/audit_qdd_chain_1.py               chain and proof-input gates
qdd-terminality/audit_qdd_chain_1.stdout.txt       8/8 and 5/5, AUDIT-PASS
qdd-terminality/CORRECTION-AUDIT-QDD-TERMINALITY-1_2026-08-20.md the correction
SECOND-LEG.md                                      arm64 replay record
```
