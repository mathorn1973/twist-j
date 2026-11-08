# First pinned Linux replay

NON-CANONICAL / L1 / exposure-disclosed prospective composition.

pin_commit: 6f6570bbbddfc496131dd31c5fdacaaa9e1cd9e5
verifier_sha256: 645ac0808feedcfd111cd54b80e1496202be36a142b5c317236496b8dda93bfb
command: python3 probes/P-RELATIVE-CONTACT-WORKBANK-REUSE-1/verify.py
platform: Ubuntu 24.04.1 LTS, Linux WSL2
architecture: x86_64
python: 3.12.3
exit_code: 0
stdout_sha256: 78d928c9303732b501bfab0b52c159c2fed4fcb0857c24cac59341aad3ec36e3
stdout_bytes: 2083
stdout_lines: 1
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

All seven scientific sources were publicly fetched at the exact commit and
matched by SHA-256 before the first execution. The Linux checkout fetched
that public pin, checked a clean worktree and rechecked the verifier hash
before execution. The checkout remained clean afterward. No source or
threshold changed after the pin. This was the first scientific execution of
this composition, with no failed attempt or scientific retry.

Assertions were enabled. The environment set LC_ALL=C, LANG=C,
PYTHONDONTWRITEBYTECODE=1, PYTHONHASHSEED=0 and TZ=UTC, and removed inherited
PYTHONIOENCODING, PYTHONUNBUFFERED and TWISTJ_EVIDENCE_DIR. The unchanged limit
was 600 seconds. Measured wall duration was approximately 36.55 seconds;
this is operational metadata, not physical time or a scientific threshold.

## Pinned source custody

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| PREREG.md | 9821 | `edd43e722ca7c407a904a6d9cc2c70fcc215c10830b0fa8de92a8f59fc9687e7` |
| PROOF.md | 25373 | `7345b699f2f6f3dc2059318d0a526d15c32b05b72b3f36c6ffdae2b6ffc4c8f8` |
| PROVENANCE.md | 3337 | `65788bd17f31b98285e4d519e4a5a3d463d1caa80c6eb4cd9234aa939cda6bf8` |
| README.md | 3494 | `5363b41d734fb842a27d5818d8289d727fc02c36c0e8fb6ea34e0010144643ec` |
| SOURCES.tsv | 1906 | `27c5dea66524af0316ed66b94edd7f28dc7f97d824bc1a02651f2bb7a44e5fd7` |
| verify.py | 30973 | `645ac0808feedcfd111cd54b80e1496202be36a142b5c317236496b8dda93bfb` |
| WORD535.txt | 4877 | `ca6bdd7a9b43e329cbc3630f26e32125b1d16a9872b9563e57733f5c408c916b` |

This record describes the first Linux x86_64 execution only. Required GitHub
x86_64 and aarch64 jobs must replay these exact EXPECTED.txt bytes. Their
actual results and head are reported on the PR, not claimed here in advance.
The two internal arithmetic representations and authoring-session checks do
not constitute an independent mathematical verdict.
