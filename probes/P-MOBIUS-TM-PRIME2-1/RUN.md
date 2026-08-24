# P-MOBIUS-TM-PRIME2-1 local run record

Date: 2026-08-10

Status: local reproduction record only. This record does not satisfy the public
two-architecture gate by itself and changes no Canon status.

The flat fields below are the machine-readable record required by the public
probe tooling.

```text
pin_commit: bb7ee2d4cff05784cfcee75a9b8d191009c76fd2
verifier_sha256: 3c5c41adec750fdb11835b7eb0fb08654bea33e4fc2a0010fff0d2d443fc7389
command: python3 probes/P-MOBIUS-TM-PRIME2-1/verify.py
platform: Debian GNU/Linux 13
architecture: x86_64
python: 3.13.5
exit_code: 0
stdout_sha256: d8ef89267c4b284b77ce6298c268ce60d2c76ccb517cf0a9a33b972e3dc6f9bd
stdout_bytes: 984
stdout_lines: 23
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

## Pin audit

```text
PREREG sha256: bc6e0d05c1504d098870dd24a4f24ff4883a36594b3b8460e8c0fc2761ee868c
PREREG bytes:  10181
verify bytes:  7298
```

Both pinned files were read back from GitHub at the immutable pin before the
first verifier execution. Their Git blob identities matched local
`git hash-object`, and their SHA-256 values matched the frozen values above.

The execution sandbox cannot resolve `github.com` through its shell network,
so a direct `git clone` launcher was unavailable. That launcher failed before
`verify.py` executed and contributes no evidence. Authority and byte readback
were instead established through the GitHub connector before execution.

The accepted verifier was then executed from a local repository-shaped root
containing byte-identical copies of the two pinned files. The canonical public
reproduction command is the machine-readable `command` field above.

Environment for the accepted run:

```text
LC_ALL=C
LANG=C
PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0
TZ=UTC
```

No external data were opened.

## Accepted run

```text
checks:   18/18 PASS
decision: BRIDGE-PASS
```

`EXPECTED.txt` is the exact accepted stdout and has the byte count, line count,
and SHA-256 recorded above.

A second execution of the same pinned verifier bytes produced the same visible
stdout. That repetition is reproduction only, not independent confirmation.
