# P-SNAP-OCCURRENCE-IDENTITY-1 run record

pin_commit: 961356e7cd421898ec3e068df896c8ef6517a29a
verifier_sha256: 481d675877e957fe99853f6e8264dbb0490252f35e74bd47ca73313409398968
command: python3 probes/P-SNAP-OCCURRENCE-IDENTITY-1/verify.py
platform: Ubuntu 22.04 (Linux-compatible WSL)
architecture: x86_64
python: 3.10.12
exit_code: 0
stdout_sha256: c22a1fa224ada1389058ebd9ac770a7e7e88d236af3b50ea9a4c8aa655c008d8
stdout_bytes: 340
stdout_lines: 1
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

Status: first local formal execution completed, 2026-09-07.
Public lock: [#893](https://github.com/mathorn1973/twist-j/issues/893).

## Accepted public bytes

Before execution, all accepted sources were committed, pushed and read back
through the GitHub contents API at the full pin. SHA-256 and Git blob values:

| File | SHA-256 | Git blob |
| --- | --- | --- |
| PREREG.md | 431c2be5f62a39f6567302366f79a5a299894437f398fe90feffb3833f8a9c19 | b259d54cb61cd4daa0723ad2d4c70740f07c9e72 |
| PROOF.md | 81106a51b4b40da00f4f1eeff847159c9563d85288206275d2e2b841665b9a19 | b90f970637c2e7e903fbe9f6468e5b8e73617721 |
| verify.py | 481d675877e957fe99853f6e8264dbb0490252f35e74bd47ca73313409398968 | c3c80280e15d0d19e40713f6386a6dfc9e27d787 |

Their byte counts were respectively 8442, 14209 and 14901. Every public
digest matched the accepted local bytes. Preparation comprised proof review,
static code review and AST parsing only; no verifier execution or import
preceded the immutable pin and public readback.

## Execution custody

The launcher rechecked all three source hashes, used LC_ALL=C, LANG=C,
TZ=UTC, PYTHONHASHSEED=0 and PYTHONDONTWRITEBYTECODE=1, and applied the
preregistered 600-second ceiling. The completed process took approximately
0.754 seconds; elapsed time is neutral metadata, not a scientific target.

The raw stdout was copied byte-for-byte to EXPECTED.txt, without newline
normalization or edits. It is one LF-terminated JSON line reporting
PROOF_AUDIT_PASS, 2025435 exact checks and an empty failures list.
Accepted PREREG.md, PROOF.md and verify.py remain unchanged after pinning.

This record establishes the first local run only. Required x86_64 and
aarch64 CI must independently replay the reviewed head with Python 3.12,
empty stderr and identical EXPECTED.txt bytes. Their actual outcomes are
separate evidence attached to the review. Universal conclusions rest on
the proofs and their explicit inherited dependencies, not the check count.
