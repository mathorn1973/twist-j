# Independent implementation and analytical review

NON-CANONICAL / L1. This record describes source independence and local
execution. It does not substitute for the required two-architecture replay.

## Independent breaker custody

The separate breaker agent received the frozen PREREG.md at commit
25a9034379fccb29d1408d505fa5dfd6319b6e6d. It read that exact file through
the GitHub connector and verified 12715 bytes and SHA-256
9c6cc1cbbfcd50779f52dcdf1e77b4d6cc8b068b69996ff19807cf6ab7d47a1a.

Its complete source-reading provenance was:

1. The delegated task and two coordination messages, containing the frozen
   source locator, independence constraints and procedural status.
2. That frozen PREREG.md as its sole scientific input.
3. Its own newly written break.py for static syntax, literal and hash checks.

It did not read verify.py, PROOF.md, predecessor executable sources,
another agent's source or scientific outputs. No scientific program was
executed or imported before the breaker source freeze. No new numerical
classification result was seen by its author. The analytical witness and
centered formulas were deliberately exposed in PREREG; this is not a claim
of blind discovery of those preregistered predictions.

The breaker independently assembled the five affine generator matrices.
It enumerated unordered pairs inside each initial reading fibre, propagated
distinguishability backwards, and recovered the class-count sequence from
shortest distinguishing depths. Surviving pairs were checked for exact
equivalence, including transitivity. Both quotient transitions and the sharp
extra-label construction were checked on every checkpoint. This differs
from the builder's iterative signature splitting.

breaker_pin: bd2d5658d32837a3d8113d751cae0960d97b0807
breaker_parent: 25a9034379fccb29d1408d505fa5dfd6319b6e6d
breaker_sha256: 09593386ba0fbdad7c294dc957ce9c424282313d6dbd576ced58f1a05d533383
breaker_bytes: 27306
breaker_git_blob: 296c2debb8e13acc8b8c3ed6c17032c522fefdea

This commit added break.py only. The coordinator read it back from GitHub
and compared its complete contents with the source before either program
ran. The accepted verifier and preregistration remained byte-identical to
their earlier pin. Both source pins and the provenance were recorded on
issue #1949 before execution.

## First independent execution

command: python3 probes/P-U-PISTON-GRAM-DESCENT-1/break.py
execution_commit: bd2d5658d32837a3d8113d751cae0960d97b0807
environment: LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
platform: Debian GNU/Linux 13 (trixie)
architecture: x86_64
python: 3.12.14
run_started_utc: 2026-11-07T21:22:42.155998+00:00
run_finished_utc: 2026-11-07T21:22:43.117651+00:00
pre_run_clean: yes
post_run_clean: yes
deterministic_executions: 1
exit_code: 0
stdout_sha256: 1efb8cfdc2c2c6c157c77913a847476c4790f44ecfae23f0d08b9fbf325a5599
stdout_bytes: 2303
stdout_lines: 1
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
direct_stdout_byte_comparison: PASS

The two first executions ran concurrently after both source freezes. Their
outputs were compared only after both completed. Direct byte comparison,
not just matching digests, passed. EXPECTED.txt contains the single shared
stdout; it is not duplicated in a second output artifact. This is independent
implementation agreement on one architecture. The public workflow replays
the accepted verify.py on both required architectures; it does not execute
break.py, and no such claim is made.

## Pre-execution analytical review

A third agent independently read only PREREG.md and PROOF.md at the first
pin, blobs 449b73b6f7675c277de79145f4dac08b1c6fe1f0 and
5b780fc4d6c55d1c7b663e308711ff878a98f58c. It read neither scientific
program, did not communicate with the breaker author, and performed no
scientific execution or unknown census.

Its review was PASS for the actual native witness selector, the full-counter
factor criterion, coarsest common refinement, sharp tag capacity, stable
center, determinant sign, cone action, flat frame, relation to the displayed
V, and the stated scope. It did not independently reassess historical
priority in the registry. The coordinator published this limited review on
issue #1949 before execution. The review does not certify program correctness
or replace finite evidence.

## Authorship exception

The author explicitly approved the GitHub connector's automatic address for
this probe. Commits use A. M. Thorn with the account's GitHub noreply address.
The source candidate was not accepted as the execution pin until that
approval and its attachment to the reserved public branch. The exception
affected author metadata only; no scientific source or scope changed.
