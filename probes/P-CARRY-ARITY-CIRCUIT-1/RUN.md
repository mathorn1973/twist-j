# RUN. P-CARRY-ARITY-CIRCUIT-1

## Immutable pin

```text
issue:           #314
pin commit:      4234d5ef9e9720aa29b355a9aef15b0e529f59f9
base main:       4d8558356f2f945b34e9f7fece323771d266585a
PREREG SHA-256:  d36f804b1a397d7bb5291ad48cbc9ba046f6bdaf27824e08bd8288d06c6e4ebf
PREREG bytes:    4888
verify SHA-256:  8c77db1e149c56c06452b7267ac0ab1e59e3c15a4d8ee29d8f597c8c31874073
verify bytes:    3250
```

Remote readback after the pin returned Git blob
`5bbf6141fb2e90a4845e3de733fe4943f9590ad0` for `PREREG.md` and
`8c904c25820ad3dabbb837e164deb6e3be26f11e` for `verify.py`, matching the
locally reconstructed blob identities and SHA-256 values above.

## Local x86_64 execution

```text
platform:       Linux
architecture:   x86_64
Python:         3.13.5
command:        LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC python3 probes/P-CARRY-ARITY-CIRCUIT-1/verify.py
exit code:      0
stderr bytes:   0
stdout bytes:   378
stdout SHA-256: 1f751aa0ce1773a218862eb47d6973884f9079fba9891d92778844207ceae329
result:         6/6 ALL PASS
```

The executed file was byte-checked before the run against the pinned
`verify.py` SHA-256.

A notebook-wrapper preflight was excluded from evidence because that wrapper
injected unrelated Python-startup instrumentation which wrote to stderr. The
pinned verifier was unchanged. The formal shell execution above used the
frozen neutral environment and produced empty stderr.

## Architecture gate

This record supplies one x86_64 leg only. It does not by itself satisfy the
public two-architecture computation gate. The pull-request workflow must run
the same pinned verifier on clean GitHub-hosted x86_64 and aarch64 jobs and
match the one committed `EXPECTED.txt` byte for byte before the computational
gate is closed. The all-n theorem claim remains proof-first and unregistered
pending review and fold.
