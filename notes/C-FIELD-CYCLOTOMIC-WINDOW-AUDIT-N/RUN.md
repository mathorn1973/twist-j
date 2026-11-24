# Successor execution and custody

PUBLIC / NON-CANONICAL, L1. Local scientific outcome: PASS.
Public two-architecture scientific gate: PASS, run 36784255529.

## Immutable sequence

- Base public main: b8ba1a07ad776cdd8d878fe0a407e07312c0e263.
- Preregistration pin: 08e8acbc0390256571263f211e023391f2eaee93.
- Joint source/proof/bridge/EXPECTED pin:
  dc086b78c3f17e0a2c605bf95ee5f854088bd2de.

Both pins were pushed and publicly read back before execution. No new
scientific program ran during drafting or static review. The primary is
an attributed public-source adaptation; the challenge author read only
this frozen PREREG as scientific source before the joint pin. A separate
reviewer read the challenge without reading the new primary. The root
read the challenge only after the public joint pin, for security review.
No frozen scientific source or target output was changed after execution.

The old #1302 partial audit remains unchanged at
ff603881d1c297a6bbb63f88df455a4b4bf3ea74. It is not an execution input
and was not rerun. This success does not relabel its primary failure.

## First scientific run

From a clean checkout of the joint pin and the repository root:

```text
python3 tools/check_reproduce.py --base b8ba1a07ad776cdd8d878fe0a407e07312c0e263
```

```text
platform: Ubuntu 22.04.5 LTS (Linux-compatible WSL)
architecture: x86_64
Python: 3.10.12, standard library
start UTC: 2026-09-30T22:09:13Z
outer elapsed seconds: 0.462
runner exit code: 0
runner stdout bytes: 177
runner stderr bytes: 0
runner stdout SHA-256: 6a7d6309e9e93d6808d0f19bc87a3e5adf65b58178aa90c1692faa9837a3f1f2
runner stderr SHA-256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

The current unmodified runner selected the committed reproduction path,
set LC_ALL=C, LANG=C, TZ=UTC, PYTHONHASHSEED=0 and
PYTHONDONTWRITEBYTECODE=1, and enforced its combined 120-second limit.
It observed bridge exit 0, empty scientific stderr and exactly 311 stdout
bytes equal to the single committed EXPECTED.txt. The bridge reached both
implementations' success lines and its own final line. RUNNER.txt stores
the exact checker stdout. The checker owns comparison and process rules;
the bridge only binds source bytes and invokes the two implementations.

EXPECTED was a prospective literal success target at the code pin. Only
this observed run established its equality to actual scientific stdout.
Its SHA-256 is
1f85ba3a5f31ee600a68de0dac5eed4205b4ed848d4cc4e5416ba319a6e57280.
No direct ad-hoc scientific launch, assertion repair or retry occurred.

## Code-pin byte identities

| file | bytes | SHA-256 |
| --- | ---: | --- |
| notes PREREG.md | 13013 | c1d6585c03c703948d7ebafd98af4fddff8d456a2947d95b8e5c252d0c4b893c |
| notes verify.py | 15660 | 18917c54c4a21b7b2010757e3657ba761e532ac2fb3d3b9cb48aed833d2aa782 |
| notes break.py | 28176 | cfa213376ac715ca8d634ae950a5cd3e30bc7fe15ce70d5703f424b4ca95a85c |
| notes PROOF.md | 28539 | d9cde5b2182fbd8526865c1117730099b91d2fa1a0d78e059b3707abacffeb78 |
| reproduction verify.py | 1007 | 509263a3d180182d5be2861a6e9b048504af1592995f5a142884dcbd9f316bea |
| reproduction EXPECTED.txt | 311 | 1f85ba3a5f31ee600a68de0dac5eed4205b4ed848d4cc4e5416ba319a6e57280 |
| reproduction README.md | 3493 | 64cdfb4dbcbe08fb06941c685b3004ceeb6a49fb11779c6579c60f4bbdaef82f |

All bytes matched the committed blobs immediately before execution. The
bridge additionally guards PREREG and both implementation hashes on every
run. The package SHA256SUMS binds final public records as well as code.

## Repository validation and public gate

Unchanged local repository checks passed with Python 3.12:
policy; 172 unit tests (one platform-specific skip); Canon v95 /484 claims;
ledger /543 items /991 dependencies /484 evidence /1031 history /25 gates;
explicit gate contracts /25 gates. Unit-test fixture messages containing
FAIL are deliberate negative fixtures; the suite exit was 0 and overall OK.

The public gate was read back from BOTH architecture jobs of
[PR #1304 run 36784255529](https://github.com/mathorn1973/twist-j/actions/runs/36784255529),
event pull_request, source head b546b7cbf99263e731d842583eb9afdd8fe9b281.
Both jobs set up CPython 3.12.14 and actually executed the unchanged
minimal-reproduction runner with these exact scientific source guards.

| job | runner architecture | completion UTC | result |
| --- | --- | --- | --- |
| [110121731336](https://github.com/mathorn1973/twist-j/actions/runs/36784255529/job/110121731336) | x86_64, ubuntu-latest | 2026-09-30T22:13:25Z | PASS |
| [110121731434](https://github.com/mathorn1973/twist-j/actions/runs/36784255529/job/110121731434) | aarch64, ubuntu-24.04-arm | 2026-09-30T22:13:23Z | PASS |
| aggregate check 110121871835 | requires both jobs | 2026-09-30T22:13:33Z | PASS |

Both architecture logs contain this identical line:

```text
REPRODUCE PASS FIELD-CYCLOTOMIC-WINDOW-AUDIT-N 509263a3d180182d5be2861a6e9b048504af1592995f5a142884dcbd9f316bea 1f85ba3a5f31ee600a68de0dac5eed4205b4ed848d4cc4e5416ba319a6e57280
```

This establishes the same guarded implementations, exit zero, empty stderr
and the same 311-byte scientific stdout on two different architectures.
It supplies the public computation gate for this audit. The local run and
static reviews remain separately identified evidence, not substitutes for
the two jobs. Publication was correctly skipped on this ordinary PR event;
no release action was attempted. Subsequent record-only commits do not
alter the pinned scientific files and remain subject to normal PR checks.
