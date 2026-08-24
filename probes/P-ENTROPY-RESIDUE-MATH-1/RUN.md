# P-ENTROPY-RESIDUE-MATH-1 formal run record

Date: 2026-08-20

Status: local formal record. The public two-architecture gate is completed
by the repository pull-request workflow, which reruns the pinned verifier on
x86_64 and aarch64 and compares stdout byte for byte against `EXPECTED.txt`.

The flat fields below are the machine-readable record required by
`tools/check_verifier.py`.

```text
pin_commit: 740dd83f20e1d07ec018075891dce9af091e16ac
verifier_sha256: 73b54e235048fd803a0b696483729d48638e6c5988d6df7ecc6ab3b8b8996b86
command: python3 probes/P-ENTROPY-RESIDUE-MATH-1/verify.py
platform: Ubuntu 24.04.4 LTS
architecture: x86_64
python: CPython 3.11.15
exit_code: 0
stdout_sha256: 7793bc5e8abea7facfdf2221dd8295c08c6141e5a516be1e4223c028a41a7344
stdout_bytes: 2082
stdout_lines: 28
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

## Pin audit

```text
PREREG sha256: 26871e561cee8a45fe3ff5a944ead4534a868030ab3b2ebc4e5ef2edcc1995fa
PREREG bytes:  8965
PREREG blob:   261e899bc3cd42db7bae809fb6642bd02709dd19
verify bytes:  9806
verify blob:   204973b3290c1e16a671d0530ad0437ad40f70af
public pin comment: issue #451, comment 5353488828
```

The verifier was executed once, formally, from a clean checkout of the
public repository at the pushed pin commit, from the repository root.
Before execution the SHA-256 of both pinned files was read back from that
checkout and matched the values recorded at the pin and in the public pin
comment. `EXPECTED.txt` is the exact raw stdout of that one execution, LF
line endings, final LF. The process exited zero and wrote no stderr.

Environment for the accepted run:

```text
LC_ALL=C
LANG=C
PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0
TZ=UTC
```

No external data exist in this probe. Wall time under one second, within
the 120 second budget declared in `PREREG.md`. As disclosed in `PREREG.md`,
the probe is result-exposed; the candidate file was smoke-executed before
the pin, outside the repository, revealing nothing not declared.

## Accepted run

```text
checks:   8/8 PASS
decision: the exact skeleton of the three entropy rows holds; universal
          statements carried by the written proofs with imports labeled
```
