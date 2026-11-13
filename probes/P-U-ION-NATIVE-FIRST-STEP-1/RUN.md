# First formal execution

NON-CANONICAL. Exact audit of a frozen conditional ideal first-step
construction; this is not a laboratory execution or physical calibration.

- Public preregistration pin: `9e4978073604f4dcb69d1ab024bdeadc12d75d40`.
- [Immutable nine-file candidate](https://github.com/mathorn1973/twist-j/tree/9e4978073604f4dcb69d1ab024bdeadc12d75d40/probes/P-U-ION-NATIVE-FIRST-STEP-1).
- Public byte readback: `2026-10-04T16:57:48.846579+00:00`. All nine files matched
  the public Git blobs, local bytes and pinned objects; the tree was clean.
- Primary SHA-256: `e217dea56c67d0e7628cefe33885938c8b0023ba6b53a26d57b5e80a9c6b457b`.
- INPUTS.json SHA-256: `831106e859554394d3595745f83713cdeb8fbce265b0b1d3a8c42817f7a9a6f6`.

Machine-readable record; the command runs from the repository root:

```text
pin_commit: 9e4978073604f4dcb69d1ab024bdeadc12d75d40
verifier_sha256: e217dea56c67d0e7628cefe33885938c8b0023ba6b53a26d57b5e80a9c6b457b
command: python3 probes/P-U-ION-NATIVE-FIRST-STEP-1/verify.py
platform: Ubuntu 22.04.5 LTS
architecture: x86_64
python: CPython 3.10.12
exit_code: 0
stdout_sha256: b8b71baf5255bbba5842bb16abf1d2f61602c168cc62bdc806589a557ba15f9e
stdout_bytes: 755
stdout_lines: 10
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

| Field | Observed value |
| --- | --- |
| Start UTC | 2026-10-04T16:58:03.772312+00:00 |
| Finish UTC | 2026-10-04T16:58:07.257417+00:00 |
| Elapsed seconds | 3.4866058860061457 |
| Outer timeout seconds | 600 |
| Independent subprocess timeout seconds | 300 |
| Timeout reached | No |
| Exit code | 0 |
| stdout | 755 bytes, 10 LF-terminated lines |
| stderr | 0 bytes |

The environment fixed `LC_ALL=C`, `LANG=C`, `PYTHONHASHSEED=0`,
`PYTHONDONTWRITEBYTECODE=1` and `TZ=UTC`. The independent implementation
ran in a separate Python process; its successful exact JSON stdout has
SHA-256 `84d31a7aa605314ca20c303e6abe2223cea472a3b06464910efdf3d86cc0f723`,
as recorded in the primary's actual output.

The wrapper captured the first execution's exact stdout before copying it
to [EXPECTED.txt](EXPECTED.txt). No accepted scientific file changed after
the public pin, and no failed scientific execution preceded this run.
Pre-pin work was analytical derivation, static review, AST parsing and
administrative/source inspection, disclosed in REVIEW-PREREG.md.

This local record covers one architecture. Required public jobs separately
replay the same bytes on the final PR head. Neither kind of execution
certifies a real-device error, input preparation or a full history.
