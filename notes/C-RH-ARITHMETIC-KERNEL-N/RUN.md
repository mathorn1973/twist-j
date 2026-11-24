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
