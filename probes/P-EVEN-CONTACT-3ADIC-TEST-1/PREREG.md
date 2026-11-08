# Six-field preregistration

PUBLIC / NON-CANONICAL / L1. P-EVEN-CONTACT-3ADIC-TEST-1.
Owner ChatGPT-20261018-even-contact-r3; A. M. Thorn, 2026-10-18.
SPDX-License-Identifier: Apache-2.0.

The finite R3 result is UNSEEN at this preregistration. Source definitions
and the conditional proof are exposed. No scientific import, execution,
rank computation or runtime benchmark has occurred. This is a new probe,
not a continuation or reuse of any sealed identifier.

Public claim: https://github.com/mathorn1973/twist-j/issues/1603#issuecomment-6248306355
Branch: probe/P-EVEN-CONTACT-3ADIC-TEST-1
Only changed path: probes/P-EVEN-CONTACT-3ADIC-TEST-1/

Authority checked before preparation: public main and peeled canon-v103
dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d; ACTIVE Public Canon v103,
content 01fb76f6b3b14a6a5ec05d0017ea922390ab6f66;
CANON.md SHA-256 d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b,
1052518 bytes. All five normative hashes, ancestry, required main checks,
issues, registry, probes and all remote heads were inspected.

## 1. Equation

The sole computed scientific proposition is

    R3: rank_F3(Bbar^705 Dbar_v)=2.

Use the literal 705-site rational wave apparatus at the public main above,
not a Fourier or infinite-lattice surrogate. Its exact definitions are
given in PROOF.md and source provenance in SOURCES.tsv. With P injecting
the four ports,

    Abar=81 H_w mod3,
    Kbar=I+PP^t mod3,
    Bbar=Kbar Abar.

H_w has diagonal 10/9 and stencil weights (6,1,15,1,1)/324 at squared
norms (2,4,8,10,16). Reduction leaves only norms 4,10,16, each with
coefficient one. Kbar multiplies the four output port rows by two.

In source order Y=((0,0,0),(1,1,0),(1,0,1),(0,1,1),(2,0,0)),
Dbar_v has rows (1,2),(2,1),(2,2),(2,2),(2,2) and zero elsewhere.
Only the first four Y sites are ports. Each source row is inserted
by coordinate, independently of its index in the sorted domain.

PROOF.md freezes the conditional consequence before this finite result:
R3 implies that every finite actual scheduled history starting in
H_pair=ker(F^2-I), and containing at least one nonzero accepted effective
impulse, ends outside H_pair at every subsequent finite cut. The proof
covers all words in the larger integer rectangle |alpha_1|<=2,
|alpha_2|<=3, with exactly two free steps between contact opportunities.
No cutoff on the number of contacts is used. Its proof and energy-account
consequence are written mathematics, not a finite history census.

## 2. Code

Accepted runtime files, all in this probe directory:

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| verify.py | 10025 | 6e7bbc45db3ada142466662836ec2a20c40c9d5232d7f92783a2a6030738f21c |
| check_independent.py | 4369 | e03c31b5d07294c8f1e4e35f186824ea6d1d38160d8e6d62965e3a48e2458f4d |
| DOMAIN.tsv | 5029 | 2e9b77cf8c507b9bc6675d9a07bf8e27ad88921c72c1efc22dcf5bdb41d8a7c0 |

The written conditional proof is also fixed:
PROOF.md SHA-256 7ab8edf5e3eb225ed984cfdf74116b7a4821d78dea1ca307587045de0c8f1184.

The primary implementation derives the full weighted stencil, reduces it
mod3, constructs finite neighbours by directed displacement and advances
the two columns together. It derives source rows from S_source[e1,e2]/2.
Its rank algorithm is Gaussian elimination on the transposed image.

The separately authored companion builds unordered edges from all pairs
of domain points and their squared distances, inserts the source rows
directly by coordinate, and advances the two columns separately.
Its rank algorithm tests determinants against the first nonzero row.
It shares only the byte-pinned domain with the primary implementation.
It does not import primary code or reuse its adjacency or intermediate
images. The primary verifier checks its hash before importing it.

Both complete 705-by-2 images and both exact ranks must agree.
verify.py is the single entry point. No runtime import of the source
apparatus, current Canon or another probe occurs. The closed runtime
bundle therefore needs no historical-context runner registration.

## 3. Carrier and complete finite inventory

Field F3, dimension 705, exponent exactly 705, both columns and every
domain row. DOMAIN.tsv is the unchanged canonical ASCII/LF, sorted,
duplicate-free copy of Y+B_zero+B_zero from the pinned source. B_zero
contains zero and all 60 even-parity stencil displacements. The verifier
checks exact file hash, byte count, integer syntax, parity, source sites,
the full geometric reconstruction, shell cardinalities, initial source
rank, and distinct finite neighbours. No smaller sampled carrier is used.

The deterministic stdout is exactly one ASCII JSON line, keys sorted
and compact separators, followed by LF. It includes all 705 image rows,
their canonical TSV SHA-256, source/domain/companion identities, field,
dimension, exponent, retained-stencil count, finite nonzero-entry count,
port indices, both ranks, full-image agreement, the R3 verdict and its
conditional-proof interpretation. The canonical image TSV used for its
hash is header c0<TAB>c1<LF> and one a<TAB>b<LF> row per domain site.

At rank two, the certificate is the lexicographically first pair of
zero-based indices i<j with nonzero determinant, its two coordinates,
two rows and determinant in F3. Below rank two, it is the first kernel
direction in the fixed list (1,0),(0,1),(1,1),(1,2). These directions
exhaust the projective line over F3. The complete image and two algorithms
distinguish rank zero from rank one; a kernel direction alone only
certifies failure of R3. No expected rank, image, witness, image hash or
scientific stdout is supplied before execution.

## 4. Systematics

Integer arithmetic with explicit mod3 reduction only; no floating
approximation, random seed search, tolerance, network, third-party package,
subprocess, machine-derived scientific input or large integer growth.
The domain is finite and literal. Applying the port factor to output rows,
source order versus sorted domain order, and the non-port fifth site are
explicitly checked by static cross-review of the different constructions.

The source and proposed proof were available to both assistant contexts.
The companion was authored before seeing primary code; primary code was
finished before reading the companion. They were then cross-reviewed.
This is separate assistant authorship with exposed mathematical context,
not blind external peer review. REVIEW.md records actual review coverage.

Only source reads, AST parsing, byte comparisons, hashing and repository
metadata checks precede the public pin. Runtime complexity was inspected
statically: at most 248160 unordered distance checks in the companion,
36 neighbours per row, two columns and 705 iterations. The unchanged
per-verifier limit is 600 seconds; no timing benchmark has been performed.
Every accepted code, data and proof byte is publicly committed and read
back before the first scientific run. All later commits preserve the pin.

The owner-approved connector author address for this directly continuing
task is documented by issue #1603 comments 6241943562 and 6242247371.
That existing approval does not change repository authorship policy.
Actual commit identity and public byte readback will be recorded.

## 5. Failure threshold and execution

Tolerance is zero. The only scientific falsifier is exact image rank
below two: output R3_FALSIFIED, r3=FAILS and
conditional_word_obstruction=NOT_ESTABLISHED. This is a completed valid
negative result with exit code zero and empty stderr. It refutes R3;
it does not prove reachability, a native preparation or a returning word.

Exact image rank two outputs R3_CONFIRMED, r3=HOLDS and
conditional_word_obstruction=ESTABLISHED. That last flag invokes the
unchanged written proof; it is not a machine-checked universal proof.
Both outcomes explicitly print native_physical_admission=NOT_CLAIMED.

Fixture corruption, implementation disagreement, unexpected exceptions,
nonzero exit, nonempty stderr or timeout are execution failures. They do
not get relabelled as a negative scientific result or repaired under the
spent pin. Preserve the immutable sources and record the repository's
consumed/ABANDONED disposition; any corrected attack needs a new identifier.
No threshold, carrier, exponent, source, timing, alphabet or proof scope
may be changed after inspecting the finite result.

After public push and byte readback, from a clean Linux repository root:

    python3 probes/P-EVEN-CONTACT-3ADIC-TEST-1/verify.py

Use LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1.
Capture exact stdout and stderr separately with the 600-second limit.
Only a completed valid run supplies EXPECTED.txt, RUN.md and RESULT.md.
RUN.md records the public pin, accepted file hashes, actual environment,
command, exit, exact stream hashes and counts.

Then open one draft PR and use the existing required workflow for exact
x86_64 and aarch64 replay with Python 3.12. Local validation uses the
existing policy, unit, Canon, ledger, gate-contract and changed-path
verifier/reproduction checks with base
dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d.
No workflow, runner, timeout or old-probe edit is part of this task.
The draft PR is not merged or promoted into the Canon by this procedure.

## 6. Action layer

L1: exact finite linear algebra and its conditional rational dynamical
consequence for the declared source apparatus. No layer lift is made.
The contact is the supplied extension, not an admitted native TWIST U
contact. #1596 remains STOP_UNTYPED, with its existing ownership.
#1605 and #1610 retain their separate fixed content/review obligations.

This probe does not realize the Dirac onsite projector, settle
(0,pi)->(pi/2,pi/2), identify bank units with
2*sqrt(1+m^2)-2m, select a physical reading or prove an entropy law.
The exact ratio m/atan(m)>1 is unchanged. Pure-pair complementary energy,
if forced positive by R3, has no claimed uniform positive lower bound.
The prior Hilbert value 3/20 and seven-dimensional closure remain
separate analytical results, not propositions tested by this verifier.
