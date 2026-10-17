# P-FIELD-CELL-SHEAR-CENSUS-AUDIT-1 preregistration

PUBLIC / NON-CANONICAL / L1. Reviewer: Codex-v103-RC-62183bc2.
Claim: [#1567](https://github.com/mathorn1973/twist-j/issues/1567).
This is the independent RC lane in released program #1548, reviewing C's
specification at 423c6f7488b35399ff40fcc30be01df526aba795 and later PR #1556.
It does not modify the author's package. The known targets are exposed;
independence concerns derivation and code, not blindness to the assignment.

## 1. Equation

Freeze the electric-first raw shear E'=E+CM, M'=M-C^t E', its active
restriction E=Cz with A_G(z,M)=(z+M,M-G(z+M)), and G=C^t C. Use exactly
G=(2), (3), [[2,1],[1,2]], [[2,1],[1,3]], [[3,1],[1,3]], together with
whole-edge and whole-face sign reorientations. The corresponding raw energy
is Hraw=E^t E+M^t M+E^t CM; active H_G=z^t Gz+M^t M+z^t GM.

Audit: characteristic polynomial det(X^2 I+(G-2I)X+I), determinant one,
integer inverse, energy invariance and exact definiteness boundary, raw and
active orders, incidence representatives, canonical basis identification,
and orientation conjugacies. Targets for minimal order are 4,3,6,5,infinite.
The last polynomial is (X^2+1)(X+1)^2. PROOF.md supplies the complete
recurrence-based derivation and explicit Jordan chain, including all integer
powers; a repeated root or failed finite-return search is not sufficient.

## 2. Code

The accepted exact verifier is the adjacent verify.py, independently written
from the allowed specification and canonical mathematics. It constructs
update matrices from coordinate basis images, obtains energy matrices by
polarization, and computes characteristic coefficients by Newton power-trace
identities. Rational Schur complements audit positive/semidefinite forms.
There is no imported author or historical verifier, random source, network,
float or external dependency. The verifier reads no external files; SOURCE
hashes document immutable provenance, not a runtime input dependency.

The complete PREREG, PROOF, SOURCES, README, EXPOSURE and verifier are committed
and pushed before execution. A new fetch and exact commit/file readback must
confirm the pin. Compilation/static inspection is allowed; import, dry run,
equivalent exploratory calculation and any scientific execution before that
pin are forbidden. Neither frozen code nor thresholds may be repaired after
running. The first stdout is retained, including scientific negatives.

## 3. Carrier or data

Coordinates are ordered (E0,...,E_(m-1),M0,...,M_(k-1)) for raw integer states
and (z0,...,z_(k-1),M0,...,M_(k-1)) for active integer states. Equality is
literal in these markings; the energy classification extends to the full
real vector spaces. The five finite unweighted CW representatives, with
+tail/-head divergence and distinct parallel edges, are:

| Type | Vertices | Ordered edges | Rows of C |
|---|---|---|---|
| digon | 0,1 | 01,01 | (1),(-1) |
| triangle | 0,1,2 | 01,12,20 | (1),(1),(1) |
| digon-digon | 0,1 | 01,01,01 | (1,1),(-1,0),(0,-1) |
| digon-triangle | 0,1,2 | 01,01,02,21 | (1,1),(-1,0),(0,-1),(0,-1) |
| triangle-triangle | 0,1,2,3 | 01,12,20,13,30 | (1,1),(1,0),(1,0),(0,1),(0,1) |

The complete orientation family is C'=RCS, D'=DR with independent diagonal
edge/face signs; G'=SGS. There are exactly 248 marked cases. Sign-reversed
shared-edge Grams arise by reversing a whole face, not one coefficient.
Raw/static splitting is claimed only over Q or R, not as a direct integral
splitting. PROOF.md fixes the canonical mixed-cell basis and its transformed
metric explicitly. No empirical dataset or integer-state truncation is used.

Negative controls are fixed before execution: a one-coefficient boundary
flip must violate DC=0; the reversed shear order must fail the fixed
original metric; the parabolic case must not satisfy A^2=I and must have
the nonzero Jordan chain v=(1,1,-2,-2), w=(0,0,1,1). The written all-time
Jordan argument, separately from the A^2 test, decides infinite order.

## 4. Systematics

Basis: canon-v102 and main a632c6a162dc87e60104d7a478e7650a6d5c4a1b;
content b04e22dd3ed8e4240cff347364f24670d4183a4d. SOURCES.json binds the
five admitted Canon files and author specification hashes. Dispatch body
has 13858 bytes and SHA-256 c209686fede612501394f969d5052518d35c95be0523c9e22619cbd19984fd87.
All were checked before this pin. Main CI 38939750393 passed both required
architectures and check; release readback 38956254023 attempt 2 passed and
the release is published immutable. Fresh remote branches/issues and current
probe/note/registry metadata were checked before the public claim.

The general shear theorem, triangle order three, canonical order five and
two-triangle zero-energy boundary are inherited. The proof clearly separates
those premises from the bounded comparison. No author-lineage-only source
is read before the exposure barrier. Same-session analytic and static helpers
are part of this single RC audit, not additional independent implementations.

First formal command, from a clean exact-pin Linux checkout:

    python3 probes/P-FIELD-CELL-SHEAR-CENSUS-AUDIT-1/verify.py

Use LC_ALL=C, LANG=C, TZ=UTC, PYTHONHASHSEED=0 and
PYTHONDONTWRITEBYTECODE=1, with a 600-second timeout. Capture exact stdout,
stderr, exit status and UTC start/end, plus neutral OS, architecture and
Python version. Preserve output outside the checkout before copying exact
stdout to EXPECTED.txt and recording RUN.md. Record and publicly commit
that first run before opening the author results. Required PR CI must replay
the same head on x86_64 and aarch64 with Python 3.12, zero exit, empty stderr,
the pinned verifier hash and byte-identical EXPECTED.txt.

## 5. Failure threshold and disposition

Zero tolerance for any failed exact identity, Gram, characteristic, inverse,
metric, minimal order, Jordan certificate, boundary, canonical marking or
orientation assertion. The checker prints SCIENTIFIC_FAIL with case and
ends RC_FIELD_CELL_SHEAR_AUDIT_SCIENTIFIC_FAIL while exiting zero, retaining
a completed negative result for replay. Independent cases continue after
the first assertion failure in a case. A failed total orientation count is
also recorded. Expected positive completion ends RC_FIELD_CELL_SHEAR_AUDIT_PASS.

A nonzero exit, exception, timeout, stderr or failed provenance check is an
execution/integrity STOP, not a mathematical refutation. Apply the repository
abandoned-pin rule if no completed formal record exists; never reuse the
identifier or silently fix the pin. Proof gaps remain UNRESOLVED even if
finite checks pass. After the barrier, classify each author claim as AGREE,
DIFFER with exact counterexample, UNRESOLVED or STOP. Preserve author pins;
NO_NEW_CLAIM is valid for wholly inherited content. Required CI success is
replay evidence and does not itself establish independence or a universal proof.

## 6. Action layer

L1 only, conditional on the five selected incidences, complete ordered
integer carriers, equality, energy and electric-first update. No L2-L6 lift,
classification of all two-complexes, extra edges, longer faces, weights,
p=5 selection, physical energy/preparation, native-U lift or apparatus follows.
No Canon, registry, frontier, gate, policy, workflow, sealed probe, merge,
tag or release change is part of this audit.
