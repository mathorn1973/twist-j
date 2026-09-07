# P-BINARY-RECORD-QUADRATIC-SELECTION-1 run record

pin_commit: c157fa9258ed01fb71320feba5a2c223daeb749e
verifier_sha256: 186923ad40daa7732b6fb6755c94ede6ef3b80da1197bd9ec62e6e096511d035
command: python3 probes/P-BINARY-RECORD-QUADRATIC-SELECTION-1/verify.py
platform: Ubuntu 22.04 (Linux-compatible WSL)
architecture: x86_64
python: 3.10.12
exit_code: 0
stdout_sha256: e2c90fa59e6ccf7f200ddfc13b3a1898e2d5293aa4defa091e4bd193101f3c9b
stdout_bytes: 415
stdout_lines: 8
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

Status: completed first local formal run, 2026-09-07.
Public lock: [#885](https://github.com/mathorn1973/twist-j/issues/885).

## Public pin custody

The pin contains PREREG.md, PROOF.md and verify.py. It was pushed and all three
files were fetched through the GitHub contents API at the full pin commit
before execution. Their SHA-256 values matched the local bytes exactly:

```text
PREREG.md 971bd955b8f6c63b3994d75e4be11572bf11cca882bc5a44b0c64ca6208f886c
PROOF.md  ce735905b568f6d9594fcb1fc7649ceecc0318eacfd6006af1df0de033a8c31b
verify.py 186923ad40daa7732b6fb6755c94ede6ef3b80da1197bd9ec62e6e096511d035
```

The corresponding public Git blob SHAs were

```text
PREREG.md f778f2b6987beae4756e026c44b027a89cd88c32
PROOF.md  0257c685bbc1763ab39716b20de283df864d3207
verify.py 99e6158d75cdc34924ef7ae9204f46ed1e0c5006
```

The Linux launcher checked the verifier hash again before executing it. Before
the pin, only AST parsing was performed; no scientific gate was executed.
The proofs and explicit witnesses were already known, as declared in PREREG.

## Execution

The process ran from the repository root with LC_ALL=C, LANG=C, TZ=UTC,
PYTHONHASHSEED=0 and PYTHONDONTWRITEBYTECODE=1, with a 600-second timeout.
The actual local Python was 3.10.12, within the preregistered >=3.10 class.
CI uses 3.12. The measured local duration was approximately 0.193 seconds;
timing is metadata, not a scientific threshold or output.

The complete stdout contains 109538 passed exact assertions. EXPECTED.txt is
the unchanged 415-byte stdout, not a retyped or normalized transcript. The
empty stderr was hashed independently. The accepted verifier remains exactly
the pinned file.

This is one local x86_64 run. The required GitHub x86_64 and aarch64 jobs must
independently replay the pinned verifier and match the same EXPECTED.txt.
Their exact-head results are recorded on the review; the all-domain claims
rest on PROOF.md, not on extrapolation from the finite audit.

## Additional maintenance replay

A subsequent native-Windows invocation of check_verifier.py reported stdout
hash `3b805b403d6021b9709b2f9c21641745582788a81335f084a46659dd1cfe1646`.
Replacing each LF in the saved Linux stdout by CRLF reproduces that hash
exactly: it is the Windows text-stream newline conversion. The prescribed
Linux checker then replayed the unchanged verifier and returned VERIFY PASS
with the original `e2c90fa5...` stdout digest. The Windows worktree metadata
paths were supplied to Linux Git through explicit GIT_DIR and GIT_WORK_TREE;
this adapts checkout access and changes no tracked file or verifier behavior.
Neither EXPECTED.txt nor any pinned file was normalized or altered.
