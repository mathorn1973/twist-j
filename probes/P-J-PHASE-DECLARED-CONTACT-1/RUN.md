# First exact pinned run

PUBLIC / NON-CANONICAL / L1. A. M. Thorn. Apache-2.0.

```text
pin_commit: f48e0ce8ca86d707a5b2db458affb065419445df
verifier_sha256: ec04b1cbc9fcf842571209798613d832bcf94ebcb86be421a1e7741f5b30018f
command: python3 probes/P-J-PHASE-DECLARED-CONTACT-1/verify.py
platform: Linux
architecture: aarch64
python: 3.11.2
exit_code: 0
stdout_sha256: 4a74d8ce680d8b7cebc389105b699b85054afcb23630835adea5a3c5f0457cbc
stdout_bytes: 4371
stdout_lines: 11
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

Public pre-run pin/readback receipt:
https://github.com/mathorn1973/twist-j/issues/1578#issuecomment-6235504053

Start UTC: 2026-10-17T15:08:41.149242+00:00
End UTC: 2026-10-17T15:08:47.222080+00:00
Elapsed: 6.072357 seconds, within the unchanged 600-second limit.

This was the first scientific import/execution of the new verifier, from
the clean public pin. The environment was LC_ALL=C, LANG=C, TZ=UTC,
PYTHONHASHSEED=0 and PYTHONDONTWRITEBYTECODE=1. PREREG.md, verify.py,
PROOF.md and SOURCES.tsv had identical before/after bytes; HEAD and the
clean worktree state were unchanged. The verifier itself checked its three
unchanged runtime dependencies before import and after the audit.

EXPECTED.txt is the exact captured stdout, with no reconstruction or
normalization. Integers and rational pairs are exact; stdout contains
eleven lines. No falsifier fired. Empty stderr and exit 0 are execution
facts; the explicit AUDIT PASS is the scientific result.

The frozen inventory covers 2500 complete contact cases, 500 ready cases,
75000 continuation boundaries, affine/quotient certificates, four actual
joined funded trajectories and one downstream replay after four fixed
omitted-W prefixes. The unchanged record reader also constructs its own
four basis-derived response operators; that inherited computation is not
an independent experiment or a new source interface.

This initial aarch64 execution does not by itself satisfy the required
two-architecture gate. The public PR jobs must replay the same verifier
against the same exact EXPECTED.txt on x86_64 and aarch64. Their observed
results and immutable job links are recorded in the public completion
receipt. Same-session review remains authored/self-reviewed.
