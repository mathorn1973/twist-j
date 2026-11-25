# Incubation audits and review record

NON-CANONICAL, no authority. Candidate-C finite checks; candidate-D written
deductions. This is not a public formal probe or a two-architecture receipt.

## Finite evidence

Environment: Linux, x86_64, Python 3.12.14. All three sources use only the
Python standard library and exact integers or Fraction. Each original helper
run completed successfully; its deterministic standard output is retained
as `RESULTS.txt`. There is no new run or independent confirmation implied by
copying the exact bytes into this directory.

| Audit | Source SHA-256 | Output SHA-256 | Output bytes |
|---|---|---|---:|
| kernel | `4c2b262c011561bc6d48ebef3315823d1d0dbcfcffcb4e3fbf3afe2b430b2bc1` | `649d40b8b17076b591f1508ac78216eed7679f77bf385df76acbdcd056aa628c` | 303 |
| rough | `290d975edcc6b38c47a3a685d2301b6d5d14176799948b1c505a2e387e261720` | `161efbdbbab5a2b96eaec363ce3993ea6532857290e7694cd7b9ec99c8dc4140` | 207 |
| returns | `1e3e70c740d25c2fe4a869ccfdbbe6241b0bcf3a400f4a3ff278a87efbcf1c78` | `9da793e860d84691f45d36d35642df91bdc6a9ab294de76e243d2774139516d4` | 446 |

Reproduction commands from the repository root:

```sh
python3 notes/C-RH-ARITHMETIC-KERNEL-N/audit/kernel/check.py
python3 notes/C-RH-ARITHMETIC-KERNEL-N/audit/rough/check_exact.py
python3 notes/C-RH-ARITHMETIC-KERNEL-N/audit/returns/verify.py
```

The kernel audit checks 29 scales, all 841 pair correlations, a full divisor
cube at primes 11 and 19, a finite aligned-prime mask, and 512 moving-tail
identities. Its prospective record describes the inquiry; it is not a
publicly pinned fixed-domain gate.

The rough audit checks an independent factorization/product census and both
direct and quotient formulas through 8192. The source, preregistration and
pre-run erratum were hashed before its first execution. Exit code was zero
and standard error empty. The erratum preserves an incorrectly calculated
initial boundary fixture, corrected before checker creation and execution.
The actual fired controls are omitted outer cutoff at `(N,d)=(114,19)` with
shift `-2`, and a nonstrict least-prime cutoff at `(1331,209)` with shift `+4`.
No mathematical threshold changed. The original frozen hash file is copied
unchanged, including its historical paths; each basename now resides under
`audit/rough/` with exactly the same bytes.

The returns audit checks 50 small squarefree moduli and the equal-order
prime witness, nine vertical moduli at three levels, and four quotient
multipliers for each of two return blocks. The public path translation is
only in the prose; its checker and preregistration are byte unchanged.

The general fixed-`u` asymptotic and the lifted `241` tail witness are written
derivations, not additional finite computations. Root did not execute the
optional finite audit mentioned in its prospective record, since the actual
quotient and cutoff risks had already been covered by the helper audits.

## Paper review

- Root read every mathematical file and all three executable audit sources.
- A separate Sol reviewed the complete kernel proof, including the split
  majorant and sharp finite-frequency sampling inequality; no remaining
  mathematical error was found. Its independent tent-kernel argument is
  also recorded in REVIEW-KERNEL.md.
- The second Astra reviewed the rough main term, exact quotient formula and
  same-window transfer. The requested wording explicitly distinguishes the
  prime-number-theorem input from the additional Mertens-rate input for the
  positive complementary term. See REVIEW-TAIL.md.
- The second Astra independently reconstructed the arbitrary-fixed-`u`
  prime-product integrals, their Dickman coefficient and the uniform
  character-quotient tail. See REVIEW-GENERAL.md.
- The retained analytic signed-window foundation was read by root, Astra
  and Sol in the immediately preceding work. Its T-only extraction keeps
  the lemma and coefficient unit and restates the rational criterion.
- Root checked the return-order proof, the Boolean versus numeric-input
  qualification, and the paper witness inside the actual long support.
- The late parallel PR #2088 was read at its immutable head. Sol read its
  actual six-unit proof; root checked the resulting exact gcd separation of
  the two long-tail rows. The scope qualification is appended explicitly.

These reviews share the same conversation and files. They are internal
mathematical review, not blind independent confirmation or formal proof
checking. No external paper, private operational file or private machine
information is redistributed.

## Repository handoff

Only this candidate's notes directory is added to the verified public base.
The root uses the prescribed Git author A. M. Thorn <thorn@twistj.com>.
The public issue owns the result-exposed incubation scope. No formal
preregistration chronology is claimed for the later public transport.
Repository policy and whitespace checks are recorded in the pull request;
their success is distinct from proof of the mathematical statements.

## Signed continuation, 24 November 2026

The same candidate, owner, issue and draft continue from the published head
`59a41b28b9c6cedaf2fa3ef4a0a23e197a87d1cd`. Public main, the declared tag
and private operating-context revision were unchanged on fresh readback.
The declared content is an ancestor of main, the five normative hashes
match, and exact-main workflow `45388050270` has successful x86_64,
aarch64 and aggregate jobs. The declared annotated tag peels to main.

This continuation contains five paper derivations and four cross-reviews.
No new scientific checker, numerical experiment, finite audit, proof-assistant
build or two-architecture mathematical receipt was run. The earlier audit
sources, preregistrations, expected bytes and scientific thresholds remain
unchanged. Repository static checks establish delivery integrity only.

Root read all five derivations and all four reviews. A Sol checked the
signed Fourier inversion, exact smoothing normalization, short-window
energy, same-window quantifiers and localized pair formula. The second
Astra checked the smooth inverse, uniform growing-threshold bound, exact
positive-slice exponent, conditional transfer and two-coordinate moving
cut. The other Sol checked the exact large-prime partition, jump-aware
prime replacement, Mellin signs, reciprocal-unit constant and complement
cancellation. Root checked the later Mertens comparison and energy
asymptotic directly from the same proof. All review is internal to this
session, and no independent external confirmation is claimed.

Root then challenged the extra time tails in the positive close-pair
majorant. The second Astra proved its additional zero-free consequence for
`L(s,chi_5)` in real part above `2/3`. Root and the other Sol checked that
implication. The primary target was consequently stated using the exact
finite Dirichlet kernel on the original block. Its all-epsilon signed
cross-term condition is equivalent to RH; the all-time close-pair bound
is retained only as an optional sufficient target, with its additional
consequence. No logical separation or impossibility theorem is claimed.

One scope repair was made before publication: the Jordan norm formula
requires a conductor coprime to five. This holds for every conductor used
by the candidate. The reviewed statement now names it explicitly. The
frozen older files and finite thresholds were not changed.

The initial local Canon check could not resolve the content ancestor in a
shallow checkout. The GitHub ancestry comparison succeeded; fetching the
missing public history then made the unmodified local checker pass:
`CANON PASS v117 claims=639`. No evidence or checker rule was changed.

The new scope is in [round3/PREREG.md](round3/PREREG.md). The remaining
signed estimate stays O; the new paper deductions stay candidate-D.

## Finite-time continuation, 24 November 2026

The same owner, issue and draft continue from exact published candidate
`09ae5168191eed9cee484c08c5d65f58b31494d1`. STATUS, POLICY, AGENTS, CORE,
FRONTIER and the required private operating context were freshly read.
Public main remains `6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed`; the
annotated v117 tag peels to that commit and the declared content is its
ancestor. All five normative file hashes and the Canon byte count match.
The exact-main architecture pair and aggregate in workflow `45388050270`
are successful. Explicit remote branches and recent public claims were
checked; new neighboring #2090/#2092 and #2091/#2093 retain their owners.

Five paper files and four retained opposition records are added. Four
scope records describe the paper questions and exposed status. No new
scientific program, exact finite audit or numerical search ran. Root and
three collaborators, two Astra and two Sol in total, developed and read
the arguments within one session. Both Sol collaborators reconstructed
the finite-taper count; the retained full record is
[REVIEW-FINITE-TAPER](round4/REVIEW-FINITE-TAPER.md). The other Astra
reviewed the two-prime hierarchy, both local-correlation notes and the
critical-unit calculation. Root read all five proofs and their source
inputs. This is internal review, not external independent acceptance.

The checks emphasized total Fourier leakage after summing all pairs,
the full enlarged time range, the nonzero determinant count without an
extra endpoint term, and the exact numerator/gcd summation. In the prime
hierarchy, both split-density factors, the unordered-pair factor,
repeated-prime subtraction and the third-order sign were reconstructed.
The local smoothing review checked the index shift, the H^3 boundary,
and the macroscopic prime count behind the binning argument. The unit
review verified the positive leading products and the factor one half
in the logarithmic critical norm.

Assembly made two clarity changes: the finite-factor countermodel's
support means integers composed of its chosen primes, and the critical
table headings use words instead of Markdown separator characters.
The remaining finite-taper sum is named explicitly after the proved
large-gcd removal. None changes a mathematical threshold or previous
scientific evidence. Earlier proof files and all audit files remain
byte unchanged. The repository integrity and final remote readbacks are
reported at the exact new head in draft #2089; repository CI does not
promote these paper deductions or rerun the notes-only scientific audits.

The first local Canon integrity invocation in this continuation again
encountered a shallow candidate-history boundary. GitHub comparison
confirmed the declared content ancestor with zero commits behind;
deepening the same remote history made the unchanged checker report
`CANON PASS v117 claims=639`. Policy, changed-document links and math
delimiters, earlier-file byte preservation, whitespace and all 48 package
manifest entries also passed before the content commit. This was a local
history-resolution repair, not a changed authority or scientific result.

## Signed-estimate continuation, round five, 24 November 2026

The same owner and candidate continue from exact published head
`d26ca6caab5dda3875333f9d2ba73b74b55ba674`. Fresh STATUS-first readback
and the required private startup confirm the unchanged PUBLIC main,
declared v117 tag and content, all five normative hashes and content
ancestry. The exact-main architecture pair and aggregate in workflow
`45388050270` are successful. All 400 remote heads and current related
issues were inspected before the prospective scope was appended to
issue #2087. The neighboring #2093 update is read at
`853237620bc2be69026168f32bb0ad871f668950` and retains its owner.

This round adds five detailed paper notes, their report, four scope
records, five opposition records and a PROMO handoff. No new scientific
program, numerical enumeration, finite audit or proof-assistant build
was executed. No source computation in the external papers was rerun.
Root and the three helpers comprise two Astra and two Sol participants
within the same session. This is not external independent confirmation.

The numerator opposition checked the exact character-bearing sum before
conductor absolute values, the n plus/minus j divisor count including
the zero multiple, variable interval endpoints, three-rectangle coverage
of threshold-crossing pairs, and the actual absolute lower witness.
The short-sum opposition checked the primary theorem and exceptional
measure, exact real/integer grid identity, arithmetic progression
quotients, critical coefficient tail and lengths below one. It requested
an explicit distinction between a K-dependent gcd cutoff and a single
cutoff serving all fixed logarithmic exponents; the note now gives both.

The smooth-support review reconstructed the saddle expansion, the
positive endpoint coefficient, concentration and parameter-shift errors,
terminal residue slab and same-window transfer. The full-estimate review
checked the latest pinned source statement, exact rational rewritings
of its constants, the unit norm, preservation of the decay constant
and both sides of the signed bound. Root read every proof and source
statement, and a separate Sol reviewed the final combined cuts and
the first-harmonic prefix implication. That review verifies the norm
argument without assuming a bound on the deleted mixed pair term.

Assembly changes only links, local working-path references and review
wording where needed for the public package. Separate same-session
review is never described as external independent evidence. Earlier
mathematical files and all finite-audit bytes remain unchanged. Final
static and remote integrity results are recorded at the new exact head
in draft #2089. The required architecture workflow checks the notes
delivery and existing repository gates; it does not turn these paper
deductions into computation-grade mathematical evidence.

## Low-height continuation, round six, 24 November 2026

The same owner continues from candidate head
`f55cbcd1bf0eff6de99449c37ac8c03916b8acfe`. Fresh STATUS-first public
readback, private startup, all 400 public remote heads and current
claims were checked. Main remains
`6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed`, Public Canon v117; the
declared tag, content ancestry, five normative hashes and exact-main
architecture pair and aggregate were verified again. The prospective
continuation was appended to the existing issue before authoring new
repository material. No new claim owner or formal probe was created.

The four new proof files contain low-height marked-prime cancellation,
the cube-root conductor transfer, compact-spectrum short-sum estimates,
and the signed cubic unit with a balanced comparison. Their initial
paper scope records are preserved. The narrower transposition record
honestly identifies its result-exposed timing. There was no scientific
computation, numerical sum, finite audit, external-source execution or
formal verifier in this continuation.

An Astra derived the actual conductor identities and low-height
estimates; two Sol participants developed the short-spectral and
balanced-unit arguments. A Sol reviewed the marked-prime proof, another
Sol reviewed the cube-root transfer including the final three-prime
consequence, the Astra reviewed the signed unit and balanced carrier,
and root reviewed all four proofs and the other opposition records.
Root supplied the further deletion through D^(2/3). Root's short-scale
review required clarification that its compact frequency cap is wider
than the existing star cap. The corrected paper makes only the proved
improvement to the smoothing error. No threshold or computed outcome
changed. Root's final scope review covers the report and handoff.

The neighboring draft #2093 was read at
`2147cba363d90d2772c3d5f883d79c326260d9c9`. Its balanced Mertens
construction and covariance are credited. The current package proves
the separate transfer to t, includes the cubic correction, and keeps
the distinct carriers and window conventions explicit. Root reread
the primary fixed-modulus prime-count input and the exact published
short-interval statement used through round five.

Assembly changes only the package indexes and the new round-six files.
Public-copy adjustments concern working-path references, links and
same-session review wording. Earlier proofs, finite evidence and
preregistration bytes remain unchanged. All new deductions are
candidate-D; the final Q_core positive-part estimate is O. CI and
repository integrity checks are not mathematical promotion or external
independent confirmation. Exact delivery and required workflow results
are recorded on the same draft PR.

## Core continuation, round seven, 24 November 2026

The same owner continues from exact published candidate
4e098f9742a72a128bfb61a10c429bced78fe17e. STATUS was freshly read
first. Public main remains 6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed,
Canon v117. The declared annotated tag and content ancestry, all five
normative hashes and successful exact-main architecture jobs and aggregate
in workflow 45388050270 were verified. The current private startup
instructions were read separately. All 400 remote heads, open related
claims and the relevant registry, evidence, gate and probe sources were
inspected before the prospective continuation was appended to issue 2087
and read back exactly.

The related draft 2093 had advanced to
eac05e3cde56d0fb3e429b91aa7129087e5da4db. Its current balanced
low-frequency papers were read and attributed. The context lookup supplied
no newer authoritative arithmetic evidence than the pinned Git work.
The neighboring owner and the original public authority remain separate.

This round adds three paper proofs, four prospective scope records, a
report and promotion handoff. An Astra derived the smooth-divisor deletion
and actual unsigned obstruction. A Sol derived the exact cube-root
pushforward, its signed main terms and integer finite-moment obstruction.
Another Sol derived the compact balanced spectrum and improved joint slow
observation. Root reconstructed the proofs, fixed the two-family successor
in the report, proposed the longer compact carrier without a unit tail,
and supplied the second family's additional nonzero-conductor example.
Both additions are proved in the author files.

The separate same-session proof reviews checked the two density counts
and all numerator sums, primitive discrepancy coefficient and original
gcd pruning, prime-count endpoints and repeated-prime weight, integer
dilation supports and moments, signed-unit bounds and the failure of an
all-epsilon pointwise bound for its absolute majorant, both masked affine
terms, the longer cutoff and the complete buffered time convolution.
The prime review also supplied the exceptional-derivative extension of
the generic power obstruction; the public proof states the changed
logarithmic exponent explicitly. This remains one research session, with
no external independent or blind confirmation.

Root read the primary fixed-modulus prime-count statement, the exact
published maximal short-sum hypotheses and Lee--Leong version 5,
Theorem 1.1 equation (12). No numerical constant is inferred from a table
outside its stated scope. No scientific executable, numerical enumeration,
finite audit, external-source computation or formal proof build was run.
All earlier mathematical and finite-audit files remain unchanged.

Public-copy adjustments concern the corresponding scope link, source
precision and the nonzero-cofactor wording. All new deductions are
candidate-D. The target (Q_7)_+ at the all-epsilon power scale remains O.
The repository checks and exact remote delivery are recorded on the same
draft and do not promote these mathematical statuses.

A separate Sol synthesis review checked the fixed two-family union, both
nonzero-conductor examples, the unchanged prime correction, transfers to
G_7, the generic probe at input scale sqrt(X), and the final status
ceiling. Its four-part conclusion is retained in round7/REVIEW-SYNTHESIS.md.

Before the content commit, POLICY PASS and CANON PASS v117 claims=639
were observed. All 91 package manifest entries, changed relative links
and anchors, paired math delimiters, whitespace, file sizes and public
content checks pass. All 75 earlier non-index files match the previous
candidate byte for byte. Main and the preceding draft head were freshly
read back unchanged before committing. Final exact-head workflow and
remote-file custody are recorded in the draft after publication.

## Complete-power continuation, round eight, 24 November 2026

The same owner continues from exact candidate
`6649670532e4d69858bc92994a55a54682f5d619`. STATUS was read first
through the GitHub connector. Public main remains
`6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed`, Canon v117. The annotated
tag `63ff3d2f7edc0c921a6c8ddd033badb59b632436` peels to that main;
content `d65e32c4b8e9a14496d3b7aba46fc384f51f81dc` is its ancestor.
All five normative hashes and the declared 1624192-byte Canon matched.
Exact-main workflow 45388050270 has successful aarch64 job 138424069994,
x86_64 job 138424070625 and aggregate 138424717642. Required public and
private startup instructions were read before delegation; private
operational details are not part of this paper package.

The explicit remote scan contained 400 branch heads. Its captured text
has SHA-256
`e7cd82046a91e82f99693047c6613ae98889c52d95d28781c13abeea9641239d`.
Related open issues, registry, evidence, gates and probe paths were
checked for collisions. No sealed probe is reopened. The prospective
round-eight scope was appended to the same issue 2087 and read back
exactly before research authoring. This is continued non-canonical
incubation under the same owner and draft 2089.

The neighboring draft 2093 was read at
`ceb77e3632ec4617c54d8e1fd504d3b1c99dd106`. Its complete thirty-file
package and twenty-nine manifest entries matched the fetched Git bytes.
The new full-coupled, full-level and lowest-mode papers were examined
for arithmetic transfer and its limits. That candidate keeps its own
owner and coefficient sequence. Personal-context lookup was used only
for discovery; it did not establish authority.

An Astra derived proper-divisor transfer, the actual upper and interior
three-prime comparisons, and the normalized determinant deletion. One
Sol derived the actual all-prime regroup, the repeated-pair contraction
and the inverse-weight negative-square formula. Another Sol derived
moving residue-zero bounds, exact smooth proper-frequency annihilation
and then the full sharp-cap common-window extension. The latter is a
separate frozen proof; its earlier reviewed source was not replaced.
Root reconstructed the decisive arguments and fixed one complete Q8.
There are four proof files, four prospective scope records, seven review
records, the report and the promotion handoff in round8.

The same-session opposition checked primitive means, reflection
symmetry, both periodic endpoints, denominator coincidences, resonant
terms, sharp-cap sums on all original shells, fixed-time versus frozen
moving masks, actual nonzero cofactor examples, signed determinant
progressions, repeated-prime multiplicity, dilation constants, critical
and positive-epsilon quantifiers, signed short-rectangle errors and both
negative squares. The root's single successor received a separate Astra
review. Each lane then checked its new report sections. Final scope
clarifications distinguish the specified large interior family from the
union of all triples and distinguish the sufficient one-sided route
from the equivalent complete criterion. The four author proofs retain
their reviewed bytes.

Root reopened the primary fixed-modulus prime-count statement and the
already attributed maximal short-sum and Lee--Leong version 5 sources.
No scientific executable, numerical enumeration, symbolic computation,
external-source computation or formal proof build ran in this round.
All new deductions are candidate-D. The complete all-epsilon bound for
Q8, equivalently Q7, remains O. The reviews are in one research session
with the proofs visible, not blind or independent external confirmation.
Repository delivery checks do not promote this mathematical status.

Before the content commit, local POLICY PASS and CANON PASS v117
claims=639 were observed. The complete package has 108 manifest entries;
all match. All 88 earlier non-index files match the preceding candidate
byte for byte. The 21 changed files comprise 17 new round-eight files
and the four package indices. Relative links and anchors, paired math
delimiters, whitespace and public content checks pass. All four frozen
author proofs retain their reviewed SHA-256 values. The exact remote
content readback, head-specific workflow and final unchanged-main check
are recorded in the existing draft after delivery.


## Round nine: the full joint cancellation, 25 November 2026

PUBLIC main was freshly checked as
`6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed`, declared Canon v117.
STATUS was read first, followed by the required policy, agent, core,
frontier, registry/evidence/gate/probe material and private startup
instructions. The declared content is
`d65e32c4b8e9a14496d3b7aba46fc384f51f81dc`; the annotated tag object
`63ff3d2f7edc0c921a6c8ddd033badb59b632436` peels to the declared
activation/main commit. Content ancestry, all five normative hashes,
and the 1624192-byte Canon match. Exact-main workflow 45388050270
has successful x86_64, aarch64 and aggregate jobs as recorded above.
No private operating details are included in this paper package.

The explicit branch scan captured 402 remote heads with SHA-256
`fa13e9cefd9a95d2faa2d3382809e440b6097f1207c8105e9160bf52b63655fe`.
Open issues and relevant candidates, registry, evidence, gates and
probe paths were checked for collisions. The prospective continuation
was appended to issue 2087 and its 30988-character body read back
exactly before authoring. The existing candidate, branch and draft
2089 were retained, incoming head
`6a91ef48f6454743797614503aa5863dde54befb`.

The neighboring public package at
`ceb77e3632ec4617c54d8e1fd504d3b1c99dd106` has thirty files and
29 matching manifest entries. The newly relevant Huang arithmetic
bridge at `fd6232aa10da26a374e421d6d46538b36b41aafb` has fifteen
files and 14 matching manifest entries. Their complete-window,
signed-interval, prime-filter and reconstruction scopes were read.
Their carriers and owners remain distinct. Discovery context and
historical project uploads did not establish current authority.

An Astra derived the full rough completion, sharp critical correction
norm, logarithmic smooth-prefix removal and actual log-share obstruction.
A Sol derived the resolved inverse mean, longer two-square factor cut
and actual penalty-omission lower bounds. The other Sol derived the
whole arithmetic-gcd recursion and direct common-taper covariance
projection. Root reconstructed the arguments and derived the integer
cubic-moment cut and its complete-window corollaries. The seven
proof files retain their reviewed versions with four prospective
question records. Further same-session reviewers checked the inputs,
endpoints, multiplicities, floors, signed squares, critical versus
supercritical quantifiers, source scopes and final synthesis.

All new scientific work was paper algebra and analytic estimates.
No new scientific numerical or symbolic execution, finite audit or
formal proof build was performed. The earlier candidate-C evidence
is unchanged. Reviewers could see the author proofs; this is neither
blind independent confirmation nor external mathematical review.
New deductions remain candidate-D and the full Q8 bound remains O.
The old sufficient positive-linear-term shortcut is now ruled out
at its unchanged cutoff; the old implication itself is not altered.

Root reopened the primary Hardy, fixed-modulus prime-count,
finite discrepancy and second-derivative sources. The finite-table
scope of Yamada and all-fixed-order scope of Thorner--Zaman are
kept distinct. Small final wording clarifications concerned the
common H-block partition, the affine a versus long b coefficients,
and the direction requiring lower-block induction. No threshold,
fired falsifier, sealed probe or prior mathematical result changed.

Main and the draft's incoming head were read back unchanged again
before packaging. The exact delivered commit, remote byte readback,
head-specific workflow and final main comparison are recorded in
the existing issue and draft after delivery. Repository checks
provide custody of the paper package, not promotion of its results.

Before the content commit, local POLICY PASS and CANON PASS v117
claims=639 were observed. The package has 129 manifest entries;
all match. All 105 earlier non-index files match the incoming
candidate byte for byte. The 25 changed files comprise 21 new
round-nine files and the four package indices. The seven author
proofs retain their final reviewed bytes. Relative links, paired
math delimiters, whitespace and the public-content scan pass.
No private archive files or operating details are part of the diff.
The final report received a separate Astra paper review after its
scope clarifications. Remote byte and workflow receipts follow
in the draft and owner issue, rather than being predicted here.
