# P-QDD-INSTRUMENT-NONSELECTION-1 local run record

Date: 2026-08-16

Status: local reproduction record only. This record does not satisfy the public
two-architecture gate by itself and changes no Canon status.

The flat fields below are the machine-readable record required by
`tools/check_verifier.py`.

```text
pin_commit: 063a62b36a3aa9f9e90ffdc085c61d977d62ea16
verifier_sha256: 0ed1cea59d049ca13ee34de082c2b625a6c0bed289bbed0e02e3202d2a41134c
command: python3 probes/P-QDD-INSTRUMENT-NONSELECTION-1/verify.py
platform: Linux 6.18.35
architecture: x86_64
python: 3.13.5
exit_code: 0
stdout_sha256: dc5ea636450ccb68f1c244654da8b48115342ee7b48012ca9ec34f280695a454
stdout_bytes: 725
stdout_lines: 11
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

## Pin audit

```text
PREREG sha256: 9575f297db404ceb7c10d7843351812d59ed1f8f655dc48130463b45a73c8d80
PREREG bytes:  17084
verify bytes:  12361
PREREG blob:   3df46dcf224f6f2da6f6fe6ecba51b4cfdb32da6
verify blob:   8b648368e78ee93595c43af33fd526c863df4cab
```

The verifier was executed from a local byte-identical copy of the public pinned
`verify.py`. Before execution, both its SHA-256 and its Git blob identity were
checked against the public remote. The canonical repository reproduction
command is the machine-readable `command` field above.

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
checks:   10/10 PASS
decision: NONSELECTION-PASS
```

`EXPECTED.txt` is the exact accepted stdout and has the same byte count, line
count and SHA-256 recorded above.

A post-pin smoke invocation of the same pinned bytes immediately before the
accepted clean-environment run produced the identical stdout. It is repetition
only; the clean-environment run above is the evidence-bearing local record.
