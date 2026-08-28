# Run record

Probe: `P-SO3-FINITE-ANISOTROPY-DEPTH-1`

```text
preregistration_pin: 4448ad11a8026740962d06585c06b8e7d11ad6b2
prereg_sha256:       45f3076ce730205ee7896a1b7f82f6fd0d5b9388bd4423da440eb5cee247cc34
prereg_bytes:        8864
verifier_sha256:     f9cb216c006aa98a83ff99619955d8221d53b00484eabbffafbcba651e39cd55
verifier_bytes:      9329
expected_sha256:     c5f29046913ca024427be3fc1213fc15af672ca2e51917a260788e792606ccbc
stdout_sha256:       c5f29046913ca024427be3fc1213fc15af672ca2e51917a260788e792606ccbc
stdout_bytes:        470
stderr_sha256:       e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes:        0
exit_code:           0
platform:            Debian GNU/Linux 13
architecture:        x86_64
python:              3.13.5
formal_date:         2026-08-28
```

Command, from a repository-root-compatible directory:

```text
python3 probes/P-SO3-FINITE-ANISOTROPY-DEPTH-1/verify.py
```

The formal execution occurred only after commit `4448ad11a8026740962d06585c06b8e7d11ad6b2` had prospectively pinned and pushed both `PREREG.md` and the accepted `verify.py`.

The local run is one x86_64 lane. It is not used to claim a two-architecture computation gate. The proposed `T` status is proof-first from `PREREG.md`; the verifier is an exact audit. The pull-request workflow must still reproduce the exact committed stdout on its required architectures.
