# First formal execution of the compressed native step

NON-CANONICAL. This is an exact audit of the conditional ideal model, not
a laboratory execution, calibration or physical inverse demonstration.

The [immutable ten-file candidate](https://github.com/mathorn1973/twist-j/tree/308eaf9be2358d2ad2bbcae5d44698de6b0cd680/probes/P-U-ION-NATIVE-COMPRESSION-1)
was committed and pushed before execution. At
`2026-10-04T18:15:42.200997+00:00`, all ten public GitHub file contents were
read back and compared byte for byte with both local working files and
pinned Git objects. The branch pointed to the pin and its worktree was clean.
The support manifest SHA-256 was
`3163b277d88b641328f74783b10e820504f17cf65a01c3a8c4948fc145b3b8e8`.

Machine-readable record, with command relative to the repository root:

```text
pin_commit: 308eaf9be2358d2ad2bbcae5d44698de6b0cd680
verifier_sha256: a8d1f95ad89995ebc287b3fbf6b0839100b00f0888786206661658ac4e4d3b95
command: python3 probes/P-U-ION-NATIVE-COMPRESSION-1/verify.py
platform: Ubuntu 22.04.5 LTS
architecture: x86_64
python: CPython 3.10.12
exit_code: 0
stdout_sha256: a53dc82cdf385144b47eb556c92e7a791339243a05f91226ae2918cfc3e2c9db
stdout_bytes: 906
stdout_lines: 11
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

| Field | Observed value |
| --- | --- |
| Start UTC | 2026-10-04T18:16:59.413342+00:00 |
| Finish UTC | 2026-10-04T18:17:01.764314+00:00 |
| Elapsed seconds | 2.3488464300025953 |
| Whole execution timeout seconds | 600 |
| Independent subprocess timeout seconds | 300 |
| Timeout reached | No |

The run fixed `LC_ALL=C`, `LANG=C`, `TZ=UTC`, `PYTHONHASHSEED=0` and
`PYTHONDONTWRITEBYTECODE=1`. The primary invoked the separately authored
independent verifier in its own process. That subprocess exited zero,
wrote no stderr, reported PASS and agreed on all twelve shared audit fields. Its
actual JSON stdout SHA-256, recorded by the primary, is
`2da764ca2ecf7b3e6241d99986782467066dd9daf3ca9e3653214fc978d67241`.

An earlier administrative wrapper invocation stopped while resolving the
Windows-created Git worktree path under Linux, before either verifier was
invoked. Only the wrapper's path handling outside the repository was fixed.
The first scientific invocation is the completed run above; no scientific
file, threshold or support input changed after public pinning.

The wrapper captured exact stdout and stderr before copying the successful
stdout bytes to EXPECTED.txt. Pre-pin activity was analytical derivation,
source review and syntax/JSON parsing, as disclosed in REVIEW-PREREG.md.
The exact carrier count and angle are outputs of this first run; the larger
prospective bounds remain frozen and are not replaced in the preregistration.

This record establishes one local architecture run. The required public CI
jobs separately reproduce the final PR head on x86_64 and aarch64. Their
results belong to that head and do not certify physical device accuracy.
