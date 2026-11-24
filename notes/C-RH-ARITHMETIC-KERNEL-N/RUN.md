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
