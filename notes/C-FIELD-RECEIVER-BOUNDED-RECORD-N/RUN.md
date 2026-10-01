# Post-pin execution evidence

PUBLIC / NON-CANONICAL / candidate-T by conditional proof / L1.
Authority remains Public Canon v95. Date: 2026-10-01.
Reservation [#1313](https://github.com/mathorn1973/twist-j/issues/1313).
Draft [PR #1314](https://github.com/mathorn1973/twist-j/pull/1314).

## Immutable source and exposure

The source pin is
[`eb688ae9c172fdfa626c9eb2a26317362440a36c`](https://github.com/mathorn1973/twist-j/commit/eb688ae9c172fdfa626c9eb2a26317362440a36c),
with parent `04fa72ca2506398bf47a64fe33aa024625bd4f9b`, the exact #1312
candidate dependency. It adds ten text files: seven candidate files and
three reproduction files. This RUN and RESULT are later reporting-only
additions. All frozen source files and manifest entries remain unchanged.

The new construction was derived and reviewed analytically before the
pin. Its exact first times, reader interval, resources and finite suite
were frozen as known predictions. No new scientific module import or
execution occurred before commit, push and actual public readback. All ten
new files and six inherited source/proof inputs were fetched through the
GitHub Contents API at that exact commit; all sixteen public byte bodies
matched the local files, and the public branch ref matched the full pin.
Readback completed before the first scientific run and before opening PR.
This is prospective audit of exposed analytical predictions, not blind
independent discovery or a retrospective public preregistration.

SHA256SUMS binds nine source/protocol/reproduction files; its own bytes are
fixed by the source commit. The bridge independently checks ten explicit
source/dependency hashes before importing either adapter. The two adapters
reuse exposed predecessor local arithmetic; their composition and state
layouts are separately written, not a newly independent whole-law discovery.

| Frozen input | SHA-256 |
| --- | --- |
| PREREG.md | 51e9d854f94f7486dbd5034e548fecb5f9d52fc96a2b710e4fca3d83b48489c6 |
| PROOF.md | e410d85a0bba2980dd266a540f75ca436255141a9e038e5f4e42f35413c6e7e9 |
| audit.py | e18149ae8f5cfba1786511a6c44af458a792a1cbbfa06b28ce33cccba779ef67 |
| audit_challenger.py | 557e306b68114f159f189cbfc5f5ebb6293e10c0e6cc17640e6eb34b04bdd92a |
| Reproduction verify.py | 64a1f57cfceb085304ae2ac23645d86ba07cb66a365dfa694721602ef476a77e |
| Reproduction EXPECTED.txt | e7b9d8827cc627fd941c0b12bf834e8c60a54556f3c383ce9b5ad0036aa254f8 |

EXPECTED.txt is 592 ASCII bytes, eight LF-terminated lines, derived from
the frozen analytical targets before execution. The unchanged repository
runner requires exact byte equality, exit zero and empty scientific stderr.
A PASS receipt therefore reports execution of both complete-state adapters,
not just a hash check or a predecessor's old main routine.

## Actual clean local execution

A clean ordinary clone of the public-verified pin supplied Linux-compatible
Git metadata. Before execution HEAD equaled the exact pin and git status
was empty. All manifest hashes were verified before and after the run.

```text
python3 -B tools/check_reproduce.py --base 04fa72ca2506398bf47a64fe33aa024625bd4f9b
```

| Item | Actual value |
| --- | --- |
| Platform | Ubuntu 22.04, WSL2 |
| Architecture | x86_64 |
| Python | CPython 3.10.12 |
| Duration | 20.985 seconds |
| Exit code | 0 |
| stderr | 0 bytes |
| Runner stdout | 177 bytes, LF |
| Runner stdout SHA-256 | fe8b1cd191452d8caa6139d2643d303a669a40104b5fdb60df76fbfe75b682f4 |
| Frozen source hashes | unchanged before/after |

Exact runner stdout:

```text
REPRODUCE PASS field-receiver-bounded-record-n 64a1f57cfceb085304ae2ac23645d86ba07cb66a365dfa694721602ef476a77e e7b9d8827cc627fd941c0b12bf834e8c60a54556f3c383ce9b5ad0036aa254f8
```

The first scientific run completed successfully; there was no preceding
failed scientific run. Static source defects documented in REVIEW.md were
corrected before the immutable pin, without executing the programs.
The existing 120-second per-entry limit was not changed.

## Public architecture checks

[Workflow run 36844325408](https://github.com/mathorn1973/twist-j/actions/runs/36844325408)
completed successfully on source head
`eb688ae9c172fdfa626c9eb2a26317362440a36c` after public readback.

| Job | Actual result | Python | Evidence |
| --- | --- | --- | --- |
| [architecture-aarch64](https://github.com/mathorn1973/twist-j/actions/runs/36844325408/job/110310704725) | success | CPython 3.12.14 | identical exact receipt above |
| [architecture-x86_64](https://github.com/mathorn1973/twist-j/actions/runs/36844325408/job/110310705030) | success | CPython 3.12.14 | identical exact receipt above |
| [check](https://github.com/mathorn1973/twist-j/actions/runs/36844325408/job/110311153725) | success | not applicable | both architecture jobs passed |

Actual completed logs for both architecture jobs were read. Each contains
this reproduction's precise name, bridge hash and expected-output hash.
Both passed policy, 172 repository unit tests, Canon, ledger and gate
contract checks. The publication job was correctly skipped for a draft PR.
The existing workflow and runner are unchanged. These actual x86_64/aarch64
receipts satisfy the byte-identical computation gate for this candidate;
the aggregate green status alone was not used as the scientific receipt.
No completed scientific failure occurred in the local or public runs.


## Outcome and limits

The audit matches the predicted 20 H=1 seeds, 19 connected lengths and 7420
complete connected boundaries; 151 cut cases and 2956 cut boundaries;
19 matched K=identity controls; 2079 occupied-contact cases; and 918
fixed off-preparation background cases. It compares every stored coordinate
with the closed formula, both representations, layer accounts and inverse
identities. The all-N and all-time cut conclusions rest on PROOF.md.

The receiver first reads 1 at N, remains readable at N,N+1,N+2 and first
resets at N+3. It uses an explicit stored three-state phase mechanism,
with one new selected receiver gate and depth five. Initial energy 41 and
32N-1 stored coordinates are unchanged. The unchanged preparation under
any single cut never produces a record. No permanent, robust, minimal,
repeated-event, physical or J-derived memory claim is made.

Only a reviewed draft is handed off. No merge, Canon/registry edit, status
promotion, tag or release occurs; the #1312/#1310 dependencies remain
explicit and noncanonical. A final reporting-only PR head must also pass
its required checks before handoff. Its scientific sources remain the pin.
