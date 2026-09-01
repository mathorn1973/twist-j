# RUN

## Immutable pin

```text
pin_commit: 38ef6a4a528689b45a1b8694d69d8aae9554570c
verifier_sha256: 37da04c1f44759f079c1eb233b84460ad7896bcb3cee72caae689a39b590387a
prereg_sha256: eef75e3d6164de5ee9f7cdbc39936dcb45fdaf2153b9930821e7c01df136a2c2
```

## Command

```text
command: python3 probes/P-MATTER-SCALAR-TEMPORAL-CHARACTERISTIC-1/verify.py
```

## Local execution record

```text
platform: Linux
architecture: x86_64
python: Python 3.13.5
exit_code: 0
stdout_sha256: aff791912f217684a9a7622f820a20d6f7325e1224acf1e7a8605f0436e10be1
stdout_bytes: 608
stdout_lines: 15
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

Environment:

```text
env -i PATH=/usr/local/bin:/usr/bin:/bin LC_ALL=C LANG=C
PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
```

The accepted verifier was executed only after the immutable pin. The local
run matched `EXPECTED.txt` byte for byte. The pull-request workflow must rerun
the same pinned verifier on clean `x86_64` and `aarch64` jobs and compare both
outputs to the one committed `EXPECTED.txt`.
