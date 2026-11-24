# Round 10 custody

**NON-CANONICAL. No authority. One x86_64 architecture.**

## Basis and immutable pins

- Candidate: C-RH-SEMISTABLE-FRAME-N; alias C-RH-BK-CONCENTRATION-N.
- Owner: A. M. Thorn; session ChatGPT-Astra-Sol-20261123-R10.
- Public claim: issue #2070; existing draft PR #2071.
- Public authority basis: 93c36089db57032a6cbca482ff62c95884567d0f.
- Prior round 9 delivery: f35ccbafa4089260e0e2225908ebac33cb6893e0.
- External mathematical source pin: 40e56bab026552e089d7afcfeff08d2defb9c005.
- Local contract commit: 7e19b11c9fc7669265081bac807cf68a684fa375.
- Public contract commit: 4c3ff7a6c3003b8c102ce44eac6e1891b5a8c728.
- Identical contract-stage tree: c614ce5486fe9dda3f245a1dd325b12e7a4b7c4b.
- Combined local code commit: 846fd7cd19b4a875b24de191c1ccf311f44f1164.
- Public execution pin: e4b7ee04b10e227fa7362b6578c9046dd1613b22.
- Identical execution-stage tree: 819ee0b50e7bf29806f44cab2217e6dac4b1fe02.

The declared Public Canon v116 tag/content ancestry, five normative
hashes and byte counts, exact-main architecture jobs and aggregate check
were read back at bootstrap. These establish the authority basis only.
They do not validate or promote round 10.

## Prospective order

1. Paper development, opposition and actual-source reading fixed the
   mathematical statements and finite audit domains.
2. PREREG.md was committed, published and read back.
3. Separate Sol authors wrote standalone verifier and breaker from that
   frozen contract. Neither scientific program was run or imported
   during authorship. The breaker did not read the verifier or its output.
4. Both programs were frozen, combined without modification, committed,
   published and read back at the immutable execution pin.
5. The coordinator compared SHA-256, byte counts and Git blob contents
   for all three frozen files before starting either program.
6. The first executions ran once each in separate clean detached
   worktrees at the execution pin. The worktrees stayed clean.
7. Actual stdout, stderr and JSON receipts were preserved. Paper review
   wording and final documentation were completed afterwards.

The frozen Git blobs are:

| File | Git blob | SHA-256 |
|---|---|---|
| PREREG.md | 4a79b1a9ff36663806feb38e7a4334eebd397064 | 7f8190d05f4269f8c9d43c6138a1812a5b82b1fae6a742f9ff777b67b3f8b5c9 |
| verify_r10.py | ee923718b60caec4c02f6f24801e132ed70fdc8c | 4dd909dfcd5dbe7715a1c20e0b49a7e57873248f894b371e771643870eb87dbe |
| break_r10.py | 5ce821f8893fcb71e821c603ff4fcb37141bffe5 | 4506a754044c81234e4ddd732d95bc326494d2068419b8aa91cff6e759ce6353 |

## First executions

Both used standard-library Python 3.12.14 on Debian GNU/Linux 13,
x86_64, with PYTHONHASHSEED=0, LC_ALL=C.UTF-8,
PYTHONDONTWRITEBYTECODE=1 and a 240-second subprocess limit.
The command, precise timestamps, elapsed nanoseconds, status and output
hashes are in verify.run.json and break.run.json.

Both runs exited zero with empty stderr and no timeout. There was no
failed scientific run, driver preflight correction or retry in round 10.
The differing stdout layouts of the independently authored programs are
preserved. Their counts and assertions agree.

The fixed contract, both programs and all first-run output bytes remain
unchanged. Earlier round 8 and round 9 contracts, programs and first-run
evidence also remain unchanged. Any subsequent rerun is reproduction.

## Authorship, delivery and evidence boundary

Local commits use A. M. Thorn <thorn@twistj.com>. The authenticated
GitHub connector exposes no author-email override and transports the
exact trees with the connected account's no-reply identity. As in the
previous deliveries, local and public commit objects are recorded
separately. Tree equality and file readback, not equality of commit IDs,
establish content custody.

Only round10/ and the parent index/handoff are changed. No Canon, registry,
workflow, release, neighboring claim or branch history is rewritten.
The proof, programs and review record are newly authored; third-party
sources are cited by links rather than imported.

Paper and code opposition took place within this session. It is not an
external independent referee report. Both runs are one architecture,
not the repository's public two-architecture gate. The work remains
candidate-D/candidate-C, and the actual intrinsic period-rank improvement
remains open.

## Repository validation

The repository's own tools returned POLICY PASS and
CANON PASS v116 claims=634. These are repository-integrity checks,
not additional scientific executions or a second architecture.

Before final packaging, public main and the PR base were freshly read
and remained 93c36089db57032a6cbca482ff62c95884567d0f. The PR was open
and draft, and its head was the expected execution pin
e4b7ee04b10e227fa7362b6578c9046dd1613b22. The three frozen round 10
files and all round 9 evidence match that pin without modification.

The final staged delivery delta passed git diff --cached --check.
Paper review of the final index, results and handoff found matching counts;
its wording corrections were applied before delivery.
