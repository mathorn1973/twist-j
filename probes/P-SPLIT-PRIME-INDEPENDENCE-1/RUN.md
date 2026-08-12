# P-SPLIT-PRIME-INDEPENDENCE-1 run record

Date: 2026-08-12

Status: local reproduction record on two architectures. The GitHub x86_64
check at pull-request time is the public leg and is not represented here.
This record changes no Canon status.

The flat fields below are the machine-readable record required by
`tools/check_verifier.py`.

```text
pin_commit: 9aed10db8985a0d15569bffcfd2b8f4477102ce7
verifier_sha256: 2d45231d96de5d8e8a92c4d3462b1fa7f45189e3b3dafd48b55edfa1f45b28c7
command: python3 probes/P-SPLIT-PRIME-INDEPENDENCE-1/verify.py
platform: Debian GNU/Linux 13
architecture: aarch64
python: 3.11.2
exit_code: 0
stdout_sha256: 13c8a6f413655cefde8f72a81f6dbe818e4e57432a6b081f9620f9dbc4188399
stdout_bytes: 1159
stdout_lines: 23
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

Second architecture, byte-identical stdout, run from a fresh clone of the
pinned branch:

```text
pin_commit: 9aed10db8985a0d15569bffcfd2b8f4477102ce7
verifier_sha256: 2d45231d96de5d8e8a92c4d3462b1fa7f45189e3b3dafd48b55edfa1f45b28c7
command: python3 probes/P-SPLIT-PRIME-INDEPENDENCE-1/verify.py
platform: Ubuntu 24.04.4 LTS
architecture: x86_64
python: 3.11.15
exit_code: 0
stdout_sha256: 13c8a6f413655cefde8f72a81f6dbe818e4e57432a6b081f9620f9dbc4188399
stdout_bytes: 1159
stdout_lines: 23
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

Pinned bundle, recorded before first execution:

```text
PREREG sha256: ef2ad91e54f4c4e56821a4da194552f41f08a7e34c91ec4935ce923c943e406d
PREREG bytes:  16940
PREREG blob:   a4ebd9eba8b95b101f08a1ac01d09455fcb63b1c
verify bytes:  12883
verify blob:   26f38626bb4cc9123e9d59554559c28ea07f374f
```

Environment on both legs:

```text
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
```

Wall time 1.6 s and 1.4 s respectively, both far inside the 120 s bound.
Standard library only; no float, no logarithm and no inexact value appears
in any assertion or any printed field.

## Order of operations, for the audit trail

```text
1  currency gate on a fresh clone: STATE ACTIVE, canon-v44 and the declared
   content commit both ancestors of main, canon hash and byte count equal
   to the STATUS declaration, canon/SHA256SUMS 5 of 5 OK
2  collision scan: probes/, the public branch list and the registry claim
   column are clean for both claim ids; LOG-AXES-INDEPENDENCE was inspected
   and is disjoint in content, and is cited as adjacent in the PREREG
3  PREREG.md and verify.py written; static compilation check only
4  security audit of both staged files: no secrets, no keys, no private
   paths, no hostnames, no machine nicknames, ASCII text only
5  PIN: branch pushed with both files, commit 9aed10db, BEFORE any execution
6  leg 1 executed, leg 2 executed from a fresh clone of the pinned branch
7  EXPECTED.txt, RUN.md and RESULT.md written from the recorded output
```

The public claim issue required by POLICY step 2 could not be opened from
the executing session, which has push access by key but no GitHub API
credential. The disclosure stands in the PREREG under ISSUE and the pin
itself, pushed before first execution, is the operative public claim.
