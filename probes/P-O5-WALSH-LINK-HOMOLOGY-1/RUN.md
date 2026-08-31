# P-O5-WALSH-LINK-HOMOLOGY-1 formal run record

Date: 2026-08-27

Status: local accepted formal record. The public two-architecture gate is
pending the pull-request workflow, which must rerun the unchanged pinned
verifier on x86_64 and aarch64 and compare stdout byte for byte with the one
committed EXPECTED.txt.

The flat fields below are the machine-readable execution record.

```text
pin_commit: 662a5b57fcc6d1e65466e7404b0e47287467bab9
verifier_sha256: 41a08bc9d0711ae9a91cda8975248c4e59626c121bc657e37222e7a1e892259e
command: python3 probes/P-O5-WALSH-LINK-HOMOLOGY-1/verify.py
platform: Linux
architecture: x86_64
python: CPython 3.13.5
exit_code: 0
stdout_sha256: 40e978e31dacd7b1491af4178f275d2aaef0d62b6f23c376ed70253bd1b0c001
stdout_bytes: 292
stdout_lines: 8
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

## Pin readback before execution

```text
basis_main:       d14a8fa3b4e5dd15d1294c4b2022e8dc6c649a11
pin_tree:         b24dc33f0fff8954fbb0e2a2a674043f6d650385
prereg_blob:      163b11f35c597939b430f49fd3e9d092918a842e
prereg_bytes:     7105
verifier_blob:    75d87d94d6aece257a16f078358bdf5a648060b7
verifier_bytes:   7792
```

Remote compare reported exactly one commit ahead of the declared basis and
exactly two added files under this probe directory. The local verifier copy
matched the public Git blob exactly before execution. Neither pinned file
changed after the pin.

## Clean startup preflight

```text
preflight_command: env -i PATH=/usr/bin:/bin LC_ALL=C PYTHONHASHSEED=0 TZ=UTC /usr/bin/python3 -c "print('PYTHON_STARTUP_CLEAN')"
preflight_exit_code: 0
preflight_stdout_sha256: 6a35d478a26afbc04957801fbb8b5470693d3ee1f2093354dc03ea48c484ac17
preflight_stdout_bytes: 21
preflight_stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
preflight_stderr_bytes: 0
```

The preflight passed immediately before the single accepted scientific
execution. `EXPECTED.txt` is its complete 292-byte LF stdout. No theorem,
threshold, witness, pinned byte, carrier, or source firewall changed after the
pin.
