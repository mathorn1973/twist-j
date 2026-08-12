# P-SPLIT-PRIME-INDEPENDENCE-1 run record

Date: 2026-08-12

Status: local reproduction record. The required GitHub x86_64 check is the
public second leg of the two-architecture gate and is not represented here;
its structured record is added once that check has run, before the fold is
requested. This record changes no Canon status.

## Pin audit

The preregistration and the verifier were pushed to the probe branch before
any execution, and the public readback matched the pin commit, both byte
streams, both SHA-256 values and both Git blob identities.

```text
pin_commit: 9aed10db8985a0d15569bffcfd2b8f4477102ce7
prereg_sha256: ef2ad91e54f4c4e56821a4da194552f41f08a7e34c91ec4935ce923c943e406d
prereg_bytes: 16940
prereg_blob: a4ebd9eba8b95b101f08a1ac01d09455fcb63b1c
verifier_sha256: 2d45231d96de5d8e8a92c4d3462b1fa7f45189e3b3dafd48b55edfa1f45b28c7
verifier_bytes: 12883
verifier_blob: 26f38626bb4cc9123e9d59554559c28ea07f374f
```

## Accepted run

The flat fields below are the machine-readable record required by
`tools/check_verifier.py`.

```text
command: python3 probes/P-SPLIT-PRIME-INDEPENDENCE-1/verify.py
platform: Debian GNU/Linux 12 (bookworm)
architecture: aarch64
python: Python 3.11.2
start_utc: 2026-08-12T08:26:13.020076233Z
finish_utc: 2026-08-12T08:26:14.639764646Z
wall_seconds: 1.619688000
deterministic_executions: 1
exit_code: 0
stdout_sha256: 13c8a6f413655cefde8f72a81f6dbe818e4e57432a6b081f9620f9dbc4188399
stdout_bytes: 1159
stdout_lines: 23
stdout_cr: 0
stdout_final_byte: 10
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
groups: 13 of 13 PASS
checks: 13
verdict: SURVIVED
```

Full environment on every leg:

```text
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
```

The checkout was clean immediately before and after the execution.
`EXPECTED.txt` is the exact raw stdout, LF line endings, final LF present, no
carriage return anywhere. Stderr was empty. The leg ran on a user-controlled
connected runner and its private machine nickname is intentionally omitted
from the public record.

## Additional local reproductions, recorded in prose

Two further reproductions were run from a fresh clone of the pinned branch
rather than from a working tree, and both matched the accepted stdout
SHA-256 exactly, with the same 1159 bytes and 23 lines, exit code zero and an
empty stderr.

```text
x86_64, Ubuntu 24.04.4 LTS, CPython 3.11.15
aarch64, Debian GNU/Linux 13 (trixie), CPython 3.13.5
```

The second of those exercises a different CPython minor series from the
accepted run, which is the series the public check uses, so the recorded
output is known not to depend on the interpreter version. Together with the
accepted aarch64 leg this gives two architectures and three interpreters
locally. None of that replaces the required GitHub check.

## Order of operations, for the audit trail

```text
1  currency gate on a fresh clone: STATE ACTIVE, canon-v44 and the declared
   content commit both ancestors of main, canon hash and byte count equal to
   the STATUS declaration, canon/SHA256SUMS 5 of 5 OK
2  collision scan: probes/, the public branch list and the registry claim
   column are clean for both claim ids; LOG-AXES-INDEPENDENCE was inspected,
   is disjoint in content, and is cited as adjacent in the preregistration
3  PREREG.md and verify.py written; static compilation check only, no gate
4  security audit of both staged files: no secrets, no keys, no private
   paths, no hostnames, no machine nicknames, ASCII text only
5  PIN: branch pushed with both files, BEFORE any execution
6  accepted leg executed; two further architectures and interpreters
   reproduced from fresh clones of the pinned branch
7  EXPECTED.txt, RUN.md and RESULT.md written from the recorded output
```

## Record corrections, disclosed rather than repaired in silence

```text
1  the first draft of this file carried two flat field blocks, one per
   architecture, which repeats the singleton fields pin_commit and command;
   the house checker rejected it and it was rewritten to a single accepted
   leg with the further reproductions in prose. No measured value changed.
2  that draft named the accepted leg's platform as Debian 13. It ran on
   Debian 12; the field above is the corrected value, and Debian 13 appears
   only where it belongs, among the additional reproductions.
3  a second draft used the structured leg headings. Those headings require a
   completed GitHub leg, which cannot exist before the public check has run,
   so the flat form is used until that record exists.
```

Neither correction touches the pinned bundle, which is unchanged since the
pin commit.

The public claim issue required by POLICY step 2 could not be opened from the
executing session, which had push access by key but no API credential. The
disclosure stands in the preregistration under ISSUE and the pin itself,
pushed before first execution, is the operative public claim.
