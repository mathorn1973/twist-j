# Run record

Probe: `P-SO3-FINITE-ANISOTROPY-DEPTH-1`

The flat fields below are the machine-readable record required by
`tools/check_verifier.py`.

```text
pin_commit: 4448ad11a8026740962d06585c06b8e7d11ad6b2
verifier_sha256: f9cb216c006aa98a83ff99619955d8221d53b00484eabbffafbcba651e39cd55
command: python3 probes/P-SO3-FINITE-ANISOTROPY-DEPTH-1/verify.py
platform: Debian GNU/Linux 13
architecture: x86_64
python: CPython 3.13.5
exit_code: 0
stdout_sha256: c5f29046913ca024427be3fc1213fc15af672ca2e51917a260788e792606ccbc
stdout_bytes: 470
stdout_lines: 13
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

## Pin audit

```text
prereg_sha256: 45f3076ce730205ee7896a1b7f82f6fd0d5b9388bd4423da440eb5cee247cc34
prereg_bytes: 8864
verify_bytes: 9329
expected_sha256: c5f29046913ca024427be3fc1213fc15af672ca2e51917a260788e792606ccbc
public_claim_lock: issue 615
formal_date: 2026-08-28
```

The formal execution occurred only after commit `4448ad11a8026740962d06585c06b8e7d11ad6b2` had prospectively pinned and pushed both `PREREG.md` and the accepted `verify.py`.

The accepted verifier was executed from a repository-root-compatible directory with stdout and stderr captured separately. `EXPECTED.txt` is the complete raw stdout, 470 bytes, 13 LF-terminated lines. Standard error was empty.

The local run is one x86_64 lane. It is not used to claim a two-architecture computation gate. The proposed `T` status is proof-first from `PREREG.md`; the verifier is an exact audit. The pull-request workflow must still reproduce the exact committed stdout on its required architectures.
