# P-J-COINCIDENCE-RECORD-BOUNDARY-1 formal run record

```text
pin_commit:             998b18f359f3d45d4fe30425cff01393fa183a6f
pin_tree:               1159943ec67c96937fb8b9dc1a7e8cb18754e305
base_commit:            50d7c0fd230efc80a6ca7604ec1266aed8a5ff56
public_lock:            issue 809
public_readback_comment: https://github.com/mathorn1973/twist-j/issues/809#issuecomment-5542871614
command:                python3 probes/P-J-COINCIDENCE-RECORD-BOUNDARY-1/verify.py
formal_invocation:      one subprocess.run child under the exact lossless wrapper frozen in PREREG.md
child_argv:              python3 probes/P-J-COINCIDENCE-RECORD-BOUNDARY-1/verify.py
external_timeout_seconds: none
environment:            env -i PATH=/usr/bin:/bin LC_ALL=C PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 PYTHONNOUSERSITE=1 PYTHONSAFEPATH=1 TZ=UTC
platform:               Ubuntu 24.04
kernel:                 Linux 6.18.35
architecture:           x86_64
python:                 CPython 3.12.3
python_executable:      /usr/bin/python3
start_utc:              2026-09-04T15:38:36.178324Z
finish_utc:             2026-09-04T15:38:36.245562Z
formal_execution_count: 1
child_invocations:      1
capture_complete:       true
exit_code:              0
stdout_sha256:          d489a8786305d1d41b79dc8d63ba07283e6b796d5309a92303e3f06d72190c2b
stdout_bytes:           1768
stdout_lines:           23
stdout_line_endings:    LF-only
stdout_final_lf:        yes
stderr_sha256:          e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes:           0
stderr_lines:           0
prereg_blob:            41b161225992f086ca8a8816cef2b10f91704c18
prereg_sha256:          81b7575524f6e80fddb12f28f6f563935370fc55723eb36a4ef964398be35ecf
prereg_bytes:           25116
prereg_lines:           725
verifier_blob:          f229993693142beffe2a1003b3033577820a6195
verifier_sha256:        b2cf94f68bc6d6a2d4963827a27ff733537209a18ea37fd07f35f660d47e4eb5
verifier_bytes:         13762
verifier_lines:         507
verifier_pre_hash_match: yes
verifier_post_hash_match: yes
stdout_encoding:        ASCII (UTF-8 subset)
pinned_files_line_endings: LF-only
pinned_files_final_lf:  yes
expected_sha256:        d489a8786305d1d41b79dc8d63ba07283e6b796d5309a92303e3f06d72190c2b
expected_bytes:         1768
expected_lines:         23
public_readback:        PASS before execution
static_audit:           PASS before pin
frozen_stdout_byte_identity: PASS
pinned_files_unchanged_after_execution: yes
result:                 PASS, 16/16 gates and 2/2 mathematical claims
physical_hypothesis:    UNTESTED STOP
architecture_gate:      PENDING
```

The public branch pinned `PREREG.md` and `verify.py` together in one commit.
Both immutable Git blobs were read back byte for byte and recorded on issue
#809 before execution. Before that pin the verifier had been inspected and
parsed statically but had never been imported or executed.

The accepted verifier was invoked exactly once as the sole child of the
preregistered lossless evidence wrapper. The raw one-line hex envelope was
exposed in full before parsing. It records matching pre-call and post-call
verifier hashes, exit zero, empty stderr, and stdout byte-identical to
`EXPECTED.txt`. Neither pinned file changed.

All sixteen gates passed and both mathematical claims were confirmed at the
candidate-T/L1 ceiling. The sole physical row remained `UNTESTED STOP`, as
required. This is the sole local x86_64 formal leg. Public GitHub-hosted
x86_64 and aarch64 replay, aggregate validation, and post-result manual
security review are pending at the time of this immutable run record. No
hostname, machine nickname, private address, credential, token, or ambient
environment value is recorded.
