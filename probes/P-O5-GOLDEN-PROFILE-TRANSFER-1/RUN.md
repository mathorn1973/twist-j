# P-O5-GOLDEN-PROFILE-TRANSFER-1 formal run record

Status: local accepted formal record. Public two-architecture replay pending.

The flat fields below are the machine-readable local execution record.

```text
pin_commit: 07d017ccec9ea533a8643b1f20283023f41774a3
verifier_sha256: c3bae78f402be52deb583cf7ac94db9c34f8e3a0bb3a750b7eb4283037d70963
command: python3 probes/P-O5-GOLDEN-PROFILE-TRANSFER-1/verify.py
formal_invocation: env -i PATH=/usr/bin:/bin LC_ALL=C PYTHONHASHSEED=0 TZ=UTC /usr/bin/python3 probes/P-O5-GOLDEN-PROFILE-TRANSFER-1/verify.py
platform: Linux
architecture: x86_64
python: CPython 3.12.3
exit_code: 0
stdout_sha256: 8bee1581eb97ee521108e124ae354aafe8292442574d04ac96f84ffeb783f46a
stdout_bytes: 419
stdout_lines: 9
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

The `command` field uses the repository-required replay spelling. The
`formal_invocation` field records the exact clean-environment process accepted
for the local formal leg.

## Pin readback before execution

The accepted runtime surface was used only after public readback showed that
the pin is exactly one commit above basis
`66a3e68fed5988a72cd56fe411b1ed633253194f`, changes exactly `PREREG.md`
and `verify.py`, and carries:

```text
PREREG blob:      4bd1b0b163880b20010d1222a2f71a077c1fe2bd
PREREG SHA256:    e0e6ce95dcc9fea273d58300c38305a82c1c8673168929ca93a95d5ad1c15410
PREREG bytes:     23703
verifier blob:    1c2dacad9c88f151aab4b165ade5a0e2c1a70304
verifier SHA256:  c3bae78f402be52deb583cf7ac94db9c34f8e3a0bb3a750b7eb4283037d70963
verifier bytes:   20470
```

Both Git blob identities and SHA-256 values matched the local frozen copies.

## Clean startup preflight

Immediately before the scientific invocation, the frozen `/usr/bin/python3`
preflight returned zero, wrote exactly `PYTHON_STARTUP_CLEAN` plus LF, and
wrote zero stderr bytes.

```text
preflight_stdout_sha256: 6a35d478a26afbc04957801fbb8b5470693d3ee1f2093354dc03ea48c484ac17
preflight_stdout_bytes: 21
preflight_stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
preflight_stderr_bytes: 0
```

The one scientific invocation then completed once. `EXPECTED.txt` is its
complete LF stdout. No theorem, threshold, breaker witness, carrier,
`PREREG.md`, or verifier byte moved after the pin.
