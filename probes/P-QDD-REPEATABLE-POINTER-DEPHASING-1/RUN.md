# P-QDD-REPEATABLE-POINTER-DEPHASING-1 run record

Date: 2026-08-29

Status: local x86_64 formal audit passed, followed by byte-identical repository replay on GitHub-hosted x86_64 and aarch64. Canon and Registry remain unchanged.

The flat fields below are the machine-readable local record required by `tools/check_verifier.py`.

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

The local execution environment could not perform an outbound Git clone, so the execution root was reconstructed from the exact remote-pinned probe blobs at the canonical `probes/P-QDD-REPEATABLE-POINTER-DEPHASING-1/` path. The verifier is self-contained and opens no repository or external data file. The repository workflow then independently replayed it from a full public checkout on both required architectures.

## Sanitized local environment

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

## Accepted local verifier run

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

## Repository two-architecture reproduction

Pull request #672 triggered workflow run `33275989088` on evidence head
`115019e4fa6a2dfd3729cd00177a505c2086990a`; GitHub tested merge ref
`18355c01811e482855927a2bb749ca6a5032b497` against base
`842b43e2f258469712aedf121f879767d1bd072c`.

The two required architecture jobs independently checked out the public repository, ran policy, 142 tool tests, Canon v71 with 342 claims, ledger, gate contract, and the changed-probe verifier. Both returned the same verifier and stdout hashes as the pin and local record:

```text
x86_64:
  OS:             Ubuntu 24.04.4 LTS
  Python:         CPython 3.12.14 x64
  verifier sha:   c366b9e6bfcc2727fbcd2e49fde87d76f6867dfecea6f4e99bffaa7a572f77c5
  stdout sha:     d734fb338f315db08d69a6b8a80d555a45e57a7a531c492e037b502120f42240
  verdict:        VERIFY PASS

aarch64:
  OS:             Ubuntu 24.04.4 LTS
  Python:         CPython 3.12.14 arm64
  verifier sha:   c366b9e6bfcc2727fbcd2e49fde87d76f6867dfecea6f4e99bffaa7a572f77c5
  stdout sha:     d734fb338f315db08d69a6b8a80d555a45e57a7a531c492e037b502120f42240
  verdict:        VERIFY PASS

aggregate:        TWO-ARCHITECTURE CHECK PASS
workflow result:  success
```

This is repository reproduction of the one frozen proof carrier on two architectures. It is not independent mathematical confirmation. The theorem grade at the frozen L4 scope rests on the written proof in `PREREG.md`; the exact verifier and two-architecture replay audit that proof carrier.
