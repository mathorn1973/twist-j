# P-O5-SQUAREFREE-CORE-1 formal run

pin_commit: f80ff006c5be1793772addc636d328cfb073e407
verifier_sha256: 0df92255bc7b770b5e521e205b2ad10e0c56ac8577dffc61194f65c62f117c4c
command: python3 probes/P-O5-SQUAREFREE-CORE-1/verify.py
platform: Linux
architecture: x86_64
python: CPython 3.13.5
exit_code: 0
stdout_sha256: 830c1a1550c51c404d6c4a944c4108027b9fb795cf483306998c48f38ad69525
stdout_bytes: 476
stdout_lines: 10
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

## Public pin readback

The public connector readback established that the pin has exactly one parent, the declared Public Canon v67 basis, and exactly two added files in this probe directory. The preregistration is 14992 bytes with SHA-256 `26e57fc1986384b9680b43f3acac1bcef1da18b017b745cb2e769b1b0a7c21ee` and Git blob `1f20d71a19dc585f1e8f7d0e03c0b7f17a612662`. The verifier is 9955 bytes with the SHA-256 recorded above and Git blob `61da1b9dcf18121ab1064b1d01e2987108ff8e20`.

A direct network clone was unavailable in this runtime because public DNS resolution failed before checkout. That failed transport attempt executed no verifier. The accepted local formal surface was reconstructed only after its SHA-256 and Git blob identities matched the public pin readback. The verifier is self-contained and reads only its own pinned source.

## Frozen startup preflight

Immediately before the scientific command, the frozen clean-start preflight was executed with an empty environment except for `PATH=/usr/bin:/bin`, `LC_ALL=C`, `PYTHONHASHSEED=0`, and `TZ=UTC`, using `/usr/bin/python3`.

It exited zero, produced exactly `PYTHON_STARTUP_CLEAN` plus LF, produced 21 stdout bytes with SHA-256 `6a35d478a26afbc04957801fbb8b5470693d3ee1f2093354dc03ea48c484ac17`, and produced zero stderr bytes.

## Accepted formal invocation

The repository-standard scientific command recorded above was executed through the same frozen clean environment and resolved to `/usr/bin/python3`. It was invoked exactly once after the successful preflight.

`EXPECTED.txt` is its complete 476-byte stdout. The final line is `VERIFY RESULT 9/9 ALL PASS`. No threshold, pinned byte, mechanism, breaker witness, or source firewall changed after the pin.
