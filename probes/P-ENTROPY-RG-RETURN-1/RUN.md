# P-ENTROPY-RG-RETURN-1 run record

The preregistration and the verifier were committed and pushed as one
immutable pin, then read back from a fresh clone of the pushed remote branch
before any gate was executed. The first formal execution of the pinned
verifier is the local leg recorded below. Both hashes below were confirmed
equal in the readback clone before the run.

## Local leg

```text
pin_commit: db57f52eddaaba2529c22a072014ba6db0ac06b6
prereg_sha256: 35e2c199255511ee95fef471eda23f108be80ecb0765723d26c2156d55a5c19f
verifier_sha256: cb0e4a5b6dfed09b3d9c02ae68ce228f13ef5efdc4465a6b202eb00d44fd48b7
command: python3 probes/P-ENTROPY-RG-RETURN-1/verify.py
platform: Ubuntu 24.04
architecture: aarch64
python: 3.12.3
exit_code: 0
stdout_sha256: b86e083d8f852642c939574b439f097c12a1bf10e595e2d016c1dcb466cdb0d9
stdout_bytes: 6185
stdout_lines: 78
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

Environment, exported for the run exactly as frozen in `PREREG.md`:
`LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC`.
Working directory was the repository root of a fresh clone of the pinned
branch. Wall time was under one second, far inside the frozen 120 second
budget. Standard output was captured verbatim as `EXPECTED.txt`; standard
error was empty.

## Remote leg

The required check reruns the same pinned verifier on GitHub
`ubuntu-latest`, which `tools/check_verifier.py` asserts is x86_64, under the
same exported environment, and compares the full stdout byte for byte against
`EXPECTED.txt`.

```text
github_platform: ubuntu-latest
github_architecture: x86_64
github_expectation: stdout identical to EXPECTED.txt, exit 0, empty stderr
```

The two legs run on different architectures, so byte-identical output
satisfies the two-architecture computation gate of `AGENTS.md` section 6
item 6. The claim earned is nevertheless a finite computation and stays at
`C`; no independent proof is offered here and none is claimed.

## Disclosure

The exact file pinned as `verify.py` was executed once before the pin,
non-formally, on x86_64, as recorded in the pre-pin development disclosure of
`PREREG.md`. That run produced the same stdout hash as the local leg above.
It carries no public status, it is not evidence, and it is not the remote
leg: the remote leg is the independent rerun performed by the required check
on the pinned commit.
