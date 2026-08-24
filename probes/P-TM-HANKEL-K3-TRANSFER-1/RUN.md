# P-TM-HANKEL-K3-TRANSFER-1 local run record

Date: 2026-08-11

Status: local reproduction record only. This record does not satisfy the public
two-architecture gate by itself and changes no Canon status.

The flat fields below are the machine-readable record required by
`tools/check_verifier.py`.

```text
pin_commit: ab8a9db324c36564bfbbb06835b106f151b49f7b
verifier_sha256: e9a9ee71919a46f7e193f8c53489b49cab6248d826f6300660da0c35951155e6
command: python3 probes/P-TM-HANKEL-K3-TRANSFER-1/verify.py
platform: Debian GNU/Linux 13
architecture: aarch64
python: 3.13.5
exit_code: 0
stdout_sha256: 88ba526bb0ddc10248d41d873b76fa96369253f875a4c8b8b7d3fc27d3762d9d
stdout_bytes: 1808
stdout_lines: 44
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

## Pin audit

```text
PREREG sha256: ef25c31ef5835fb6a755916f31e795b979d3bd15452507cafb996a0286dc0044
PREREG bytes:  8935
PREREG blob:   99bc9b48d003b311d974db61fedefc880cb4a46d
verify bytes:  32003
verify blob:   f010736ac532f9da49b5079c4b736494e2583cb2
```

The verifier was executed from a fresh clone of the public repository at the
pushed pin commit, from the repository root. Before execution, the SHA-256 of
both pinned files was read back from the public remote clone and matched the
values recorded at the pin. The canonical repository reproduction command is
the machine-readable `command` field above.

Environment for the accepted run:

```text
LC_ALL=C
LANG=C
PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0
TZ=UTC
```

No external data were opened. Wall time 27 seconds, within the 120 second
budget declared in PREREG.md.

## Accepted run

```text
checks:   31/31 PASS
decision: TRANSFER-K3-PASS
```

`EXPECTED.txt` is the exact accepted stdout and has the same byte count, line
count, and SHA-256 recorded above. The run was executed twice on the local
platform with byte-identical stdout, and reproduced byte-identically on a
second architecture (Ubuntu 22.04, x86_64, Python 3.10.12) before this record
was committed. The repository-required GitHub x86_64 and aarch64 jobs at
pull-request time complete the public two-architecture gate.

The written proofs cited in `PREREG.md`, not this finite audit, carry the
universal quantifiers of the companion note sections 1 to 4.
