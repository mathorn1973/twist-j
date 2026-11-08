# First local formal run

pin_commit: 7ffee4939346221e2d43ed386f33bdfa47cd509f
command: python3 probes/P-INTEGER-PRIMITIVE-SOURCE-METRIC-1/verify.py
verifier_sha256: a77e599eda0f5a5ba938ab884ea577c58185bb85b210acbee59eb6a441c47413
platform: Ubuntu 24.04.3 LTS
architecture: x86_64
python: 3.12.14
exit_code: 0
stdout_sha256: 855d38e01e6defbcabf2a109ffe9b37f88656e2c69884de774ae2af72fa59b3c
stdout_bytes: 612
stdout_lines: 21
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

started_utc: 2026-10-19T09:55:34.286101+00:00
completed_utc: 2026-10-19T09:55:37.686362+00:00
prereg_sha256: 445eedb7d6c66c141d52ae45afcc2b43255b0d29dc465191059dfd73edffbe15
proof_sha256: 44285281a42061073c2da33880d3175f8f1ed1ee44e5f6dbcf501f44a2a1ec4e
source_sha256: 94cdace90965626cd21f01b6309f5c2b6a4621454fb89dfb1d4467786e58de91
breaker_sha256: 7f556dcf88d2d1b7632fbe425e4e84f2b66a3c3f955fe05692a5eadc746852cd
frozen_manifest_sha256: 5c6f1213c3eb59659b07f498f6a9c224e66f6229dc65d70172bf2b0000f93929

## Execution custody

This was the first scientific execution of either pinned implementation.
Before execution, all six frozen files were public and were fetched back
from the immutable pin with byte-identical contents. The local index tree
equalled the remote tree ed6ce8ac08e893f023b78d47d251be7e2b7c63ce; the
checkout was clean at that exact pin. All manifest hashes were checked
again immediately before launching the primary.

The public prospective receipt, posted and read back before execution, is
https://github.com/mathorn1973/twist-j/issues/1640#issuecomment-6264519495.
The metadata limitation of the GitHub commit connector was disclosed in
the ownership issue before the pin. Its actual privacy-address author and
committer metadata were read back; no history was rewritten.

Environment: LC_ALL=C, LANG=C, PYTHONDONTWRITEBYTECODE=1,
PYTHONHASHSEED=0, TZ=UTC. The primary launched breaker.py with the same
Python executable and -I in a separate process. Both completed. The child
had exit zero, empty stderr, and exactly the same 19-line certificate as
the primary, including every final LF. The primary appended its two
success lines. No stripping or newline normalization was used.

EXPECTED.txt is the unmodified 612-byte first stdout. The separate initial
capture was hashed before being copied to this file. Stderr was empty.
No frozen definition, source, proof, fixture, or implementation changed
after the pin.

## Required architecture gate

This record states the observed local run only. The draft PR's unchanged
workflow must replay this exact verifier and breaker on x86_64 and aarch64
with Python 3.12 and compare to the same EXPECTED.txt. The actual workflow
and job receipts will be recorded in the PR and its public comments after
their results are observed. Local x86_64 agreement alone does not assert
that two architectures have already passed.
