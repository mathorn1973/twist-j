# First local formal run

pin_commit: fe5456f1aac8adcc3fdb0222df81f7e2fc773977
command: python3 probes/P-INTEGER-JOINT-VARIATION-1/verify.py
verifier_sha256: bf0c7a1df9315534236602356f142d9f762e348ff36fe5560d57964d22d0ee70
platform: Linux-6.18.55-x86_64-with-glibc2.39
architecture: x86_64
python: 3.12.14
exit_code: 0
stdout_sha256: a8b2315bf4a69ed4a9bd8490868dd9224b3e973c967bf2db4b90bc9efee3f7f7
stdout_bytes: 589
stdout_lines: 21
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

started_utc: 2026-10-19T13:32:44.499899+00:00
completed_utc: 2026-10-19T13:32:48.342585+00:00
prereg_sha256: 83430002a51a71790eed29b3fb51dcdaf8aa89761f74f616711b284e052344f3
proof_sha256: e56252742dcf6120afd8ba18eda5cd711762fa1fd85ffda3ff9c5779ece8206e
source_sha256: 7e4e61ff9b25b3f1f6422ebca1f3a6f1d60079d7b0488dca3cf9bb3faf4f5917
breaker_sha256: 197deeed1042108d287ebd6f5bad6f22a0e29793653e0169987043ba2b3dd601
frozen_manifest_sha256: 6499fc4771240a5396c67aacf6063844247c858d5629cff777a0c1a1f9234daa

## Execution custody

This was the first scientific execution of either pinned implementation.
All six frozen files had been published and read back from GitHub at
fe5456f1aac8adcc3fdb0222df81f7e2fc773977 with byte-identical contents.
The synchronized local index and commit tree both equalled
45fda3323996486b07731955716baf84dd196105; the checkout was clean at the
exact pin before execution. No prospective result file was invented.

The public pin receipt was posted and read back before execution:
https://github.com/mathorn1973/twist-j/issues/1645#issuecomment-6268456972.
The GitHub connector recorded the previously disclosed account privacy
email for author and committer. That metadata was read back; the pin
was preserved without history rewriting.

Environment: LC_ALL=C, LANG=C, PYTHONDONTWRITEBYTECODE=1,
PYTHONHASHSEED=0, TZ=UTC. The primary launched breaker.py with the same
Python executable and -I in a separate process. The child completed
with exit zero, empty stderr, and exactly the same 19-line certificate
bytes as the primary, including every final LF. The primary appended
its two terminal success lines. No stripping or newline normalization
was used to obtain the agreement.

EXPECTED.txt is the unmodified 589-byte first stdout. The separate
first-run capture was hashed before being copied to this file. Stderr
was empty. No frozen definition, proof, source, fixture or implementation
changed after the prospective pin.

## Required architecture gate

This record states the observed first local run only. The draft PR's
unchanged workflow must replay the exact verifier and breaker on x86_64
and aarch64 with Python 3.12 and compare to the same EXPECTED.txt.
Actual workflow and job receipts will be recorded in the PR and its
public comments after observation. This local x86_64 result does not
claim that the two-architecture gate has already passed.
