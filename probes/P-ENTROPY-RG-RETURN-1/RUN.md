# P-ENTROPY-RG-RETURN-1 run record

The preregistration and the verifier were committed and pushed as one
immutable pin, then read back from a fresh clone of the pushed remote branch
before any gate was executed. The first formal execution of the pinned
verifier is the local leg below. The required check then reran the same
pinned verifier on GitHub and compared the full standard output byte for
byte.

```text
pin_commit: db57f52eddaaba2529c22a072014ba6db0ac06b6
command: python3 probes/P-ENTROPY-RG-RETURN-1/verify.py
verifier_sha256: cb0e4a5b6dfed09b3d9c02ae68ce228f13ef5efdc4465a6b202eb00d44fd48b7
prereg_sha256: 35e2c199255511ee95fef471eda23f108be80ecb0765723d26c2156d55a5c19f
```

Both hashes were confirmed equal in the readback clone before the run. The
environment exported for every execution below is exactly the one frozen in
`PREREG.md`:
`LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC`, from the
repository root.

## Local formal leg

```text
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

Wall time was under one second against the frozen 120 second budget. Standard
output was captured verbatim as `EXPECTED.txt`; standard error was empty.

## Required GitHub leg

```text
platform: ubuntu-latest
architecture: x86_64
python: 3.12
verifier_sha256: cb0e4a5b6dfed09b3d9c02ae68ce228f13ef5efdc4465a6b202eb00d44fd48b7
stdout_sha256: b86e083d8f852642c939574b439f097c12a1bf10e595e2d016c1dcb466cdb0d9
exit_code: 0
stderr_bytes: 0
status: PASS
verdict: VERIFY PASS
byte_identity: PASS
replay: PASS
```

The two legs ran on different architectures, so byte-identical output
satisfies the two-architecture computation gate of `AGENTS.md` section 6
item 6. The claim earned is nevertheless a finite computation and stays at
`C`; no independent proof is offered here and none is claimed.

## Provenance of the GitHub leg fields

The evidence is the workflow run recorded against this branch head, run id
`30619202693`, job id `91119445513`, whose conclusion is success. The job log
text itself was not read: GitHub requires authentication to serve it, and the
session that authored this probe held no credential for it.

The recorded values therefore have this standing, and any reader can check
each one against the pinned sources. Architecture, exit code, empty standard
error, the verifier hash and the standard-output hash are asserted by
`tools/check_verifier.py` at the pinned commit: that tool fails the job unless
the runner reports `x86_64`, unless the verifier bytes match their pin, unless
the process exits zero with no standard error, and unless its standard output
equals `EXPECTED.txt` byte for byte. A successful conclusion of that job
entails every one of those. The runner image is the one named in
`.github/workflows/policy.yml`, and the interpreter series `3.12` is the one
that workflow pins; the patch level was not read, for the reason above.

Nothing in this section is a separate measurement, and none of it is offered
as one.

## Auxiliary reproduction, not the required check

An additional reproduction was run from a fresh clone of this pushed branch
in a third environment, on a different machine from the local leg and under a
different interpreter, with the same exported environment.

```text
aux_role: auxiliary reproduction, no gate weight, not a leg of the record
aux_architecture: x86_64
aux_python: 3.11.15
aux_exit: 0
aux_stderr_bytes: 0
aux_stdout_sha256: b86e083d8f852642c939574b439f097c12a1bf10e595e2d016c1dcb466cdb0d9
aux_tool_line: VERIFY PASS P-ENTROPY-RG-RETURN-1 cb0e4a5b6dfed09b3d9c02ae68ce228f13ef5efdc4465a6b202eb00d44fd48b7 b86e083d8f852642c939574b439f097c12a1bf10e595e2d016c1dcb466cdb0d9
```

It reproduces the pinned output exactly under an interpreter two minor
versions apart from the local leg, which is evidence that the determinism
claimed in `PREREG.md` does not depend on the interpreter minor version. It
carries no gate weight and does not substitute for the required check.

## Disclosure

The exact file pinned as `verify.py` was executed once before the pin,
non-formally, on x86_64, as recorded in the pre-pin development disclosure of
`PREREG.md`. That run produced the same standard-output hash as the local leg
above. It carries no public status, it is not evidence, and it is not the
GitHub leg.
