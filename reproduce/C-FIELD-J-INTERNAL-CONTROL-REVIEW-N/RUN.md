# First independent internal-control run

**PUBLIC, NON-CANONICAL. Actual first execution of the frozen independent audit.**
Original work, Apache-2.0. Owner: A. M. Thorn.

Specification pin: `e5ff31fd7296df4bf740fd27c1ac3de14b5c8148`.
Complete independent proof/program pin: `d674bf1bc0b9c69b9dcd623ddb13afbf0c93b3ae`.
All four public source blobs were read back and matched to local raw bytes
before execution. The Linux checkout was clean at this exact full pin.
The coordinator executed this independent audit first, before releasing
new author proof, program or output to the reviewer. No scientific source
was edited after freeze and no local rerun occurred.

```text
python3 -I reproduce/C-FIELD-J-INTERNAL-CONTROL-REVIEW-N/verify.py
```

Date (UTC): 2026-10-02. Ubuntu 22.04.5 LTS; x86_64; Python 3.10.12.
Environment supplied: `LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1`.
The registered `-I` uses Python isolated mode; the program imports only
standard-library modules and its ordered arithmetic is deterministic.
External timeout: 120 seconds. Elapsed: 14.427 seconds. Exit: 0.
Stderr: 0 bytes, SHA-256
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

| Source or output | Bytes | SHA-256 |
|---|---:|---|
| notes/C-FIELD-J-INTERNAL-CONTROL-REVIEW-N/PREREG.md | 12020 | `abc075c2ab50e210ddf1b2a977afe429e10ce1efdd848a8f1aa97f1be8fce36d` |
| notes/C-FIELD-J-INTERNAL-CONTROL-REVIEW-N/PROOF.md | 26328 | `d35393266d924686527ad6f28047a1f451bb84efaeeed747745fb8502329610b` |
| reproduce/C-FIELD-J-INTERNAL-CONTROL-REVIEW-N/verify.py | 30678 | `9645e3d2bd021df1a5a6d29af096b1a316c3150ab0f56a30b31c06813a963676` |
| reproduce/C-FIELD-J-INTERNAL-CONTROL-REVIEW-N/README.md | 1786 | `9af04c7361b7819320b3460d035423e521abbb1a3fb39e18adafca17b50be821` |
| EXPECTED.txt (actual stdout) | 392 | `77edd7406a395dadf6e170de5802beb14c0a7ca7f7b8ef99897c3d428e7da816` |

All registered finite groups completed. The exact output records 56
compiler descriptors, 41184 single-step inverse cases, 234 complete
command cases, 60 complete program cases, 336 ideal-history matrix units,
8 finite-loader columns and 96 typed-boundary cases. Positive-domain
nonconstant repeated-context weight is zero; the separately retained
unnormalized off-domain vector gives weight 13/9, not a probability above
one. No branch was sampled or selected.

This run is x86_64 evidence, not yet the two-architecture gate. The unchanged
stock `tools/check_reproduce.py` must run the same source without source
rewriting and compare actual stdout to this exact EXPECTED on both CI
architectures. That runner uses its ordinary Python invocation without
`-I`; this distinction does not change the scientific code and the actual
byte comparison, not an assumption, decides reproducibility. RESULT and
REVIEW must cite completed jobs before claiming that gate.

The independent paper proof, finite checker and later author comparison
are distinct evidence. No actual occurrence law, physical pulse/tick/work
realization, new source preparation or Canon promotion follows.
