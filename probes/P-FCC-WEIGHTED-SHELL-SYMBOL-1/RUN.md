# Run record

Probe: `P-FCC-WEIGHTED-SHELL-SYMBOL-1`

The flat fields below are the machine-readable record required by
`tools/check_verifier.py`.

```text
pin_commit: f4cafb63b4534c8c0864b0935117f2539ad11b07
verifier_sha256: 7a853f0940a0c2794e40530270aebfe988a3b3596afb62d46db1bcd6413a1673
command: python3 probes/P-FCC-WEIGHTED-SHELL-SYMBOL-1/verify.py
environment: LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
platform: Ubuntu 24.04 LTS
architecture: x86_64
python: CPython 3.12.3
exit_code: 0
stdout_sha256: 3132f5185ac98f577b3931494c60b781fe381641f00ccd4c0be0574c698e42f6
stdout_bytes: 767
stdout_lines: 19
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

## Pin audit

```text
prereg_sha256: 3f75e0c9b76f9ba2fb1b21e4856afb6486ef2bde0da06761ba3a11e6c72e45bb
prereg_bytes: 9375
verify_bytes: 9978
expected_sha256: 3132f5185ac98f577b3931494c60b781fe381641f00ccd4c0be0574c698e42f6
public_claim_lock: issue 691
formal_date: 2026-08-30
```

The formal execution occurred only after commit
`f4cafb63b4534c8c0864b0935117f2539ad11b07` had prospectively pinned and
pushed both `PREREG.md` and the accepted `verify.py`, and their remote bytes
had been read back.

The accepted verifier was executed once from the clean repository checkout at
the pin, with stdout and stderr captured separately. `EXPECTED.txt` is the
complete raw stdout, 767 bytes, 19 LF-terminated lines. Standard error was
empty.

The local run is one x86_64 lane. It is not used to claim a two-architecture
computation gate. The proposed `T` status is proof-first from `PREREG.md`; the
verifier is an exact audit. The pull-request workflow must still reproduce the
exact committed stdout on its required x86_64 and aarch64 architectures.
