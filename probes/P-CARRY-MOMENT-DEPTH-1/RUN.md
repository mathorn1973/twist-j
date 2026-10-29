# First formal run: P-CARRY-MOMENT-DEPTH-1

This records the first exact local execution after the public source pin.
Status: completed, exit zero, empty stderr. NON-CANONICAL.

```text
pin_commit: 65d2ae96d55fce7f527b2807e0e1f1fb2b5cdf38
verifier_sha256: 8d264e779a9db78a078f5bb611a290cd464d474033e6d27e3954766482c03c51
prereg_sha256: 574f2bd65198c5db2d561258e976a32fef4f4707117fd3ba6b953ff90f331d3c
command: python3 probes/P-CARRY-MOMENT-DEPTH-1/verify.py
platform: Debian GNU/Linux 13 (trixie)
architecture: x86_64
python: 3.13.5
exit_code: 0
stdout_sha256: 0d42d526a8b4649cc6a48879b6086e45f02427929185ff98cc7325be6123a595
stdout_bytes: 8576
stdout_lines: 426
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
proof_sha256: 5d83e6cd072b84c1cd045f6efc57d4463813774a3f1b41909eebd8743e7f8cec
base_commit: a193e389fb1ddb0bdc89165b015c95a17eb1e425
source_tree: 94ba3586a2de5a1476a3a869e47d74bab4d3a40b
source_readback_utc: 2026-10-29T07:34:48.408098+00:00
started_utc: 2026-10-29T07:34:59.012745+00:00
finished_utc: 2026-10-29T07:35:31.128881+00:00
elapsed_seconds: 32.114132
environment: LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
```

Reservation: [#1820](https://github.com/mathorn1973/twist-j/issues/1820).
The five source files were pushed and read back through the public repository
API before execution; their bytes and Git blob identities matched the local
pin. The checkout was clean before and after the verifier. No code, threshold
or scientific source changed after the pin.

EXPECTED.txt is the unmodified scientific stdout. No elapsed time, machine
identity or other variable metadata is embedded in that stdout. The elapsed
seconds above are an engineering observation, not a scientific predicate.

This record establishes one x86_64 execution. The required GitHub x86_64 and
aarch64 runs use Python 3.12 and compare against the same committed stdout;
their separate workflow evidence must not be inferred from this local record.
