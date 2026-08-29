# P-QDD-REPEATABLE-POINTER-DEPHASING-1 local run record

Date: 2026-08-29

Status: local x86_64 formal audit passed. This record does not satisfy the repository two-architecture gate by itself and changes no Canon or Registry status.

The flat fields below are the machine-readable record required by `tools/check_verifier.py`.

```text
pin_commit: 254127da12f4570c16e80293244fd3770a604cd3
verifier_sha256: c366b9e6bfcc2727fbcd2e49fde87d76f6867dfecea6f4e99bffaa7a572f77c5
command: python3 probes/P-QDD-REPEATABLE-POINTER-DEPHASING-1/verify.py
platform: Linux 6.18.35
architecture: x86_64
python: 3.13.5
exit_code: 0
stdout_sha256: d734fb338f315db08d69a6b8a80d555a45e57a7a531c492e037b502120f42240
stdout_bytes: 1133
stdout_lines: 19
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

## Pin audit

```text
base commit:      842b43e2f258469712aedf121f879767d1bd072c
pin commit:       254127da12f4570c16e80293244fd3770a604cd3
PREREG sha256:    2866bfa490257afccf32a2370dda6ade69a123f894353ca2726b0e598e41fe60
PREREG bytes:     10370
PREREG Git blob:  1de199ea21551220072abd9cfebcd53c68b02bb6
verify sha256:    c366b9e6bfcc2727fbcd2e49fde87d76f6867dfecea6f4e99bffaa7a572f77c5
verify bytes:     8489
verify Git blob:  c358908754c2de9ab80e3d72e8476eecb688177d
```

Both pinned files were read back from the public branch before execution. Their calculated Git blob identities matched the remote Git blob identities exactly. No accepted verifier execution occurred before the pin.

The local execution environment cannot perform an outbound Git clone, so the execution root was reconstructed from the exact remote-pinned probe blobs at the canonical `probes/P-QDD-REPEATABLE-POINTER-DEPHASING-1/` path. The verifier is self-contained and opens no repository or external data file. The required GitHub workflow will independently replay it from a full public checkout on both repository architectures.

## Sanitized environment

```text
LC_ALL=C
LANG=C
PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0
TZ=UTC
PATH=/opt/pyvenv/bin:/usr/bin:/bin
```

Formal command as executed from the local execution root:

```text
env -i PATH=/opt/pyvenv/bin:/usr/bin:/bin LC_ALL=C LANG=C \
  PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
  /opt/pyvenv/bin/python3 \
  probes/P-QDD-REPEATABLE-POINTER-DEPHASING-1/verify.py
```

No external data were opened.

## Accepted verifier run

The first accepted post-pin execution returned:

```text
exit code:       0
stdout bytes:    1133
stdout lines:    19
stdout sha256:   d734fb338f315db08d69a6b8a80d555a45e57a7a531c492e037b502120f42240
stderr bytes:    0
stderr sha256:   e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
result:          9/9 ALL PASS
```

`EXPECTED.txt` is the exact accepted stdout.

## Public replay state

Pending pull-request replay on GitHub-hosted x86_64 and aarch64. Until that replay completes, the local run is one architecture only. The candidate theorem grade rests on the written proof in `PREREG.md`; the verifier is an audit.
