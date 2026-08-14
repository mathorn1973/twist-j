# RUN. P-TM-SYM2-BORN-HALVING-1

```text
pin_commit:              0e930978878453800fa078f75b9a0e25c2963787
PREREG_sha256:           7e512890fa486cd3b37410d813b0b6becfc1694bbe2f5dae691ebfa17cfec36e
verifier_sha256:         a9dbe6d5549aa3e0bb5f21cc4d8e26586cbcf95141df141432b710e8fdb0f6f7
platform:                Debian GNU/Linux 13 (trixie)
architecture:            x86_64
python:                  Python 3.13.5
start_utc:               2026-08-14T15:07:50Z
finish_utc:              2026-08-14T15:07:51Z
command:                 python3 probes/P-TM-SYM2-BORN-HALVING-1/verify.py
environment:             LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
exit_code:               0
stdout_bytes:            741
stdout_lines:            30
stdout_sha256:           52ee81ddd10c7af5e00ff1a2a1b6ea2fed9905b1f235349b73c0732fb2ead51d
stderr_bytes:            0
stderr_sha256:           e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
deterministic_executions: 1

github_platform:         Ubuntu 24.04.4 LTS
github_architecture:     aarch64
github_python:           CPython 3.12.13
github_verifier_sha256:  a9dbe6d5549aa3e0bb5f21cc4d8e26586cbcf95141df141432b710e8fdb0f6f7
github_stdout_sha256:    52ee81ddd10c7af5e00ff1a2a1b6ea2fed9905b1f235349b73c0732fb2ead51d
github_exit_code:        0
github_stderr_bytes:     0
github_status:           PASS
github_byte_identity:    PASS
```

## Source materialization record

The execution environment could not resolve `github.com` for a direct `git clone`.
No verifier execution was attempted during that failed clone.

After the public pin was pushed and the exact remote bytes of `PREREG.md` and
`verify.py` were read back through the GitHub connector, those two pinned files
were materialized byte-for-byte under a local repository-root-shaped directory
with the frozen probe path and the verifier was executed there once. The
verifier is self-contained and reads no repository file.

This is not described as a clean Git checkout. The scientific identity of the
executed file is the exact remote pin byte identity above. The public GitHub
pull-request workflow is the clean repository replay.

The formal stderr file was empty. Terminal-control text emitted by the hosting
container after the command was not part of the redirected verifier stderr and
is not part of the scientific transcript.

## Scientific return

`EXPECTED.txt` is the exact 741-byte stdout of this single local execution.
The decision printed by the pinned verifier is `BORN-HALVING-PASS`.
No post-pin verifier edit, retry, threshold move, or local scientific rerun occurred.

## First pull-request workflow preflight

Workflow `31813175546` stopped on both GitHub architectures before any
changed-probe verifier replay. `check_policy.py` passed. The repository unit
test that parses all RUN records then reported:

```text
RUN.md lacks fields: stdout_lines, verifier_sha256
```

This was an evidence-metadata schema defect only. It was corrected by adding
the required field names and the missing line count. No `PREREG.md`, verifier,
`EXPECTED.txt`, scientific threshold, route, or output byte changed, and no
additional local scientific execution was made. The failed workflow carries no
cross-architecture scientific verdict.

## Successful clean GitHub replay

The corrected evidence head `b7d86f655921aceabee140e44d4e93d5f7c678fb`
was tested by policy workflow `31813296463` on the clean pull-request merge
checkout `55858de4921c9edd9b530e07a29db383a136f5c1`.

```text
x86_64 job:      94808833870   success
architecture:    x86_64
platform:        Ubuntu 24.04.4 LTS
python:          CPython 3.12.13
verifier sha256: a9dbe6d5549aa3e0bb5f21cc4d8e26586cbcf95141df141432b710e8fdb0f6f7
stdout sha256:   52ee81ddd10c7af5e00ff1a2a1b6ea2fed9905b1f235349b73c0732fb2ead51d

aarch64 job:     94808834014   success
architecture:    aarch64
platform:        Ubuntu 24.04.4 LTS
python:          CPython 3.12.13
verifier sha256: a9dbe6d5549aa3e0bb5f21cc4d8e26586cbcf95141df141432b710e8fdb0f6f7
stdout sha256:   52ee81ddd10c7af5e00ff1a2a1b6ea2fed9905b1f235349b73c0732fb2ead51d

aggregate check: 94808891578   success
terminal line:   TWO-ARCHITECTURE CHECK PASS
```

Both architecture jobs also passed policy, all 99 repository unit tests,
Canon and ledger checks, and `tools/check_verifier.py --base` reproduced the
changed probe byte-for-byte. The x86_64 and aarch64 clean replays therefore
satisfy the public two-architecture computation gate for the pinned verifier.
