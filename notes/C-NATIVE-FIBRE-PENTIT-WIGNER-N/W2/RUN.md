# W2 independent breaker run

[PASS: LOCAL AUDIT] NON-CANONICAL. Session CODEX-W2-INDEPENDENT-20261002. Action layer L1. No status promotion.

## Custody

Pin recorded before first execution: 2026-10-02T17:34:57.7209910Z.

| Pinned file | SHA-256 |
| --- | --- |
| PREREG-W2.md | 49fc22c516553ac8825dcf7ff0af52e47ae34cc2693ddd418576a1d96bca95e6 |
| independent_breaker.py | a1f673e436d4628bd4592d1e4a36dd2b659a80c260aea9a82cf3cc0228181cc0 |
| PROOF-AUDIT.md | db41abf9dd55472435eaf1e473bf80e0a1add74555f11eefd4ce9906aee306c4 |

[PASS] All three pinned files were checked before both executions and after the second execution. All hashes are unchanged. No prior scientific execution, failed version, repair, or successor pin exists. Static Python AST parsing, compilation and float-literal inspection preceded the pin without executing the audit.

## Command and environment

From the W2 directory:

```text
python independent_breaker.py
LC_ALL=C
LANG=C
PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0
TZ=UTC
```

The runner used subprocess.run with the current Python executable, capture_output=True and the listed environment. It wrote stdout and stderr bytes directly from the child process. No shell text pipeline transformed child stdout.

| Neutral field | Value |
| --- | --- |
| Platform | Windows 11 |
| Architecture reported by Python | AMD64 |
| Architecture class | x86_64 |
| Python | CPython 3.12.10 |

## Executions

| Field | First | Repeat |
| --- | --- | --- |
| Started UTC | 2026-10-02T17:35:09.738119+00:00 | 2026-10-02T17:35:33.621640+00:00 |
| Finished UTC | 2026-10-02T17:35:11.438004+00:00 | 2026-10-02T17:35:35.345040+00:00 |
| Exit code | 0 | 0 |
| Stdout bytes | 1335 | 1335 |
| Stderr bytes | 0 | 0 |
| Stdout SHA-256 | 187016c69990aaa276e7f3a49281c6deff9efe20b6b012659471f5275e5a9ff1 | 187016c69990aaa276e7f3a49281c6deff9efe20b6b012659471f5275e5a9ff1 |
| Stderr SHA-256 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |

[PASS] Repeat stdout is byte-identical to FIRST.stdout. This is same-architecture reproduction only. The raw transcript contains the native Windows CRLF produced by Python stdout. No cross-platform normalization or Linux byte-identity claim is made. W1 concerns the four original frozen programs and is independent of this W2 transcript.

Exact transcripts and machine-readable metadata are FIRST.stdout, FIRST.stderr, FIRST.json, REPEAT.stdout, REPEAT.stderr and REPEAT.json. The independent census table's canonical serialization is ASCII with LF and is separate from the native stdout line endings. Its digest is a2f76d45a0d42ae42906238833f90231ab55546ec4a9a3290bf2d6ed60c11491 for 9544 bytes. The table serialization is specified in PREREG-W2.md and the code; it is not the original package's unspecified table serialization.

[UNCHANGED] C-OCCURRENCE-CYCLE-COUNT-N remains STOP_APPLICABILITY / H_NOT_TESTED. The QDD reading remains conditional.
