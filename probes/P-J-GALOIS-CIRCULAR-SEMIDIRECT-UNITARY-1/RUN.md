# P-J-GALOIS-CIRCULAR-SEMIDIRECT-UNITARY-1 formal run record

```text
pin_commit:             a6400adf14a04e22d83341b69fa5a8c38ae73999
pin_tree:               7ffdc23af71b6b30d048187c31ec33c384c8fe87
base_commit:            a86dbf4a12a71422463d397733ca08ae8f117963
public_lock:            issue 797
public_readback_comment: https://github.com/mathorn1973/twist-j/issues/797#issuecomment-5536771802
command:                python3 probes/P-J-GALOIS-CIRCULAR-SEMIDIRECT-UNITARY-1/verify.py
formal_invocation:      /usr/bin/env -i PATH=/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin:/usr/local/bin:/usr/bin:/bin LC_ALL=C PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 TZ=UTC python3 probes/P-J-GALOIS-CIRCULAR-SEMIDIRECT-UNITARY-1/verify.py
external_timeout_seconds: none
environment:            env -i PATH=/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin:/usr/local/bin:/usr/bin:/bin LC_ALL=C PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 TZ=UTC
platform:               Ubuntu 24.04.3 LTS
kernel:                 Linux 6.18.35
architecture:           x86_64
python:                 CPython 3.12.13
python_executable:      /opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python3
start_utc:              2026-09-04T06:43:31Z
finish_utc:             2026-09-04T06:43:32Z
formal_execution_count: 1
exit_code:              0
stdout_sha256:          f9f873397fc41389084e2d6aa9873858909303b60c5b8a304235a46013de32f6
stdout_bytes:           1809
stdout_lines:           26
stdout_line_endings:    LF-only
stdout_final_lf:        yes
stderr_sha256:          e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes:           0
stderr_lines:           0
prereg_blob:            31a545937b762b596965e6ad175998c8d7049924
prereg_sha256:          ee222bd10b83387512718c7604e7523d479c9e4cfa13662b09e75d5e4c0a7eed
prereg_bytes:           17979
prereg_lines:           554
verifier_blob:          ddc764663424c5f50e290b6bda5ad7b575bc84ea
verifier_sha256:        c895c7cc8cf36bf3fba61e331cfa9b7a6d38188911538273cb58cb231a0b7207
verifier_bytes:         29759
verifier_lines:         949
encoding:               UTF-8 (ASCII subset)
line_endings:           LF-only
final_lf:               yes
expected_sha256:        f9f873397fc41389084e2d6aa9873858909303b60c5b8a304235a46013de32f6
expected_bytes:         1809
expected_lines:         26
public_readback:        PASS before execution
static_audit:           PASS, two independent reviews before pin
frozen_stdout_byte_identity: PASS
pinned_files_unchanged_after_execution: yes
result:                 PASS, 18/18 gates and 2/2 claims
architecture_gate:      PENDING
```

The public branch pinned `PREREG.md` and `verify.py` together in one commit.
Both immutable remote blobs were read back byte for byte and recorded on the
public claim issue before execution. The accepted verifier had not previously
been imported or executed.

No separate Python-startup preflight process was performed or claimed. Public
byte readback and the static mathematical, code, and security audits were the
pre-execution checks.

The pinned verifier was then executed exactly once with the formal invocation
above. It exited zero, wrote empty stderr, and its stdout is byte-identical to
`EXPECTED.txt`. The frozen `PREREG.md` and `verify.py` remained unchanged.

This is the sole local x86_64 formal leg. Public GitHub-hosted x86_64 and
aarch64 replay, aggregate policy validation, and post-result manual security
review are pending at the time of this record. No hostname, machine nickname,
private address, or fleet label is recorded.
