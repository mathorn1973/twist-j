# First pinned execution

```text
pin_commit: ed90ffd1826190b1fe04af0cf172d2886be21067
verifier_sha256: 461b29dc6d3282a00fcccfd0cc194b198f856b688f78841658c93e49ecccac8f
command: python3 probes/P-RELATIVE-CONTACT-FOUR-SLOT-MINIMUM-1/verify.py
platform: Ubuntu 24.04.3 LTS
architecture: x86_64
python: 3.12.14
exit_code: 0
stdout_sha256: 95ee2135ecb491ab7f0702d603ea94013d00beb28e70668a3c418c0f21478178
stdout_bytes: 1755
stdout_lines: 9
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

Started 2026-11-01T07:40:12.423368+00:00; completed 2026-11-01T07:40:18.805131+00:00.
The public pin was fetched into a clean detached checkout and all three
input files were read back byte for byte through the GitHub connector before
first execution. Only syntax compilation preceded the public pin.
The prescribed first local command used LC_ALL=C, LANG=C, TZ=UTC,
PYTHONHASHSEED=0, PYTHONDONTWRITEBYTECODE=1 and timeout600 seconds.
EXPECTED.txt is the unchanged complete stdout. Exit0; empty stderr.

## Input custody

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| PREREG.md | 5531 | `5baf144b63300113fdc83d0142ea5ae9f8792a97806e3af576f1cfc859b253e8` |
| PROOF.md | 7054 | `5952f685ced119c57b7e4ed57cf6acee4ddb46272e3efd4e42c0aaf06a3c5fff` |
| verify.py | 9251 | `461b29dc6d3282a00fcccfd0cc194b198f856b688f78841658c93e49ecccac8f` |

The scientific text is authored as A. M. Thorn. The public commit was
transported through the connected GitHub account, whose actual commit identity
is preserved. No local-only commit is represented as a public pin.

This record certifies the local x86_64 execution only. The unchanged required
GitHub workflow must replay this same source and stdout on both x86_64 and
aarch64. That is cross-architecture reproduction, not independent authorship.
