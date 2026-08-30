# Run record

Probe: `P-PHOTON-WILSON-VILLAIN-BRIDGE-1`

The flat fields below are the machine-readable record required by
`tools/check_verifier.py`.

```text
pin_commit: 05bc49339fb87aedef19ebb465251872c87265b5
verifier_sha256: 30af41ce20eb122405b130a8cb21bd4d55e1b0b53a749f57f655241179e19cc8
command: python3 probes/P-PHOTON-WILSON-VILLAIN-BRIDGE-1/verify.py
environment: LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
platform: Ubuntu 24.04 LTS
architecture: x86_64
python: CPython 3.12.3
exit_code: 0
stdout_sha256: 3f7e5bd8ce69cb9f01bfc1826c7e38ab3ab56a245b8d1b41b0907c71e4c5b01d
stdout_bytes: 798
stdout_lines: 17
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

## Pin audit

```text
prereg_sha256: 4c31988b985d7de2ee8b3805b0e258d69d9d8f36bc6f65639a17e9f861f417c1
prereg_bytes: 10851
verify_bytes: 7388
expected_sha256: 3f7e5bd8ce69cb9f01bfc1826c7e38ab3ab56a245b8d1b41b0907c71e4c5b01d
public_claim_lock: issue 692
formal_date: 2026-08-30
```

The formal execution occurred only after commit
`05bc49339fb87aedef19ebb465251872c87265b5` had prospectively pinned and
pushed both `PREREG.md` and the accepted `verify.py`, and their remote bytes
had been read back.

The accepted verifier was executed once from the clean repository checkout at
the pin, with stdout and stderr captured separately. `EXPECTED.txt` is the
complete raw stdout, 798 bytes, 17 LF-terminated lines. Standard error was
empty.

The local run is one x86_64 lane. It is not used to claim a two-architecture
computation gate. The proposed `T` status is proof-first from `PREREG.md`; the
verifier is an exact audit. The pull-request workflow must still reproduce the
exact committed stdout on its required x86_64 and aarch64 architectures.
