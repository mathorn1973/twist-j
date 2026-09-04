# P-J-CIRCULAR-QDD-DUAL-SIMPLEX-BRIDGE-2 formal run record

```text
pin_commit:             2d33ad06044b78f5e204fe28d966e8f66e043953
pin_tree:               37e3eb7b358ef24012b86228713b0a5ac3500c4f
base_commit:            3b15217d28575726da1ff3af4de71cba4544637d
public_lock:            issue 801
public_readback_comment: https://github.com/mathorn1973/twist-j/issues/801#issuecomment-5538706591
command:                python3 probes/P-J-CIRCULAR-QDD-DUAL-SIMPLEX-BRIDGE-2/verify.py
formal_invocation:      one subprocess.run child under the exact lossless wrapper frozen in PREREG.md
child_argv:              python3 probes/P-J-CIRCULAR-QDD-DUAL-SIMPLEX-BRIDGE-2/verify.py
external_timeout_seconds: none
environment:            env -i PATH=/usr/bin:/bin LC_ALL=C PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 PYTHONNOUSERSITE=1 PYTHONSAFEPATH=1 TZ=UTC
platform:               Ubuntu 24.04
kernel:                 Linux 6.18.35
architecture:           x86_64
python:                 CPython 3.12.3
python_executable:      /usr/bin/python3
start_utc:              2026-09-04T09:47:53.906523Z
finish_utc:             2026-09-04T09:47:54.196271Z
start_unix_ns:          1788515273906502920
end_unix_ns:            1788515274196303528
capture_interval_ns:    289800608, exact end_unix_ns-start_unix_ns
timestamp_capture_order: start_unix_ns, start_utc, child, finish_utc, end_unix_ns
formal_execution_count: 1
child_invocations:      1
capture_complete:       true
exit_code:              0
stdout_sha256:          6d512d1efe4f93505f69fc3cfe21182f02b7fd40cb052a59a7eb5095013f7e5a
stdout_bytes:           1858
stdout_lines:           26
stdout_line_endings:    LF-only
stdout_final_lf:        yes
stderr_sha256:          e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes:           0
stderr_lines:           0
capture_envelope_sha256: a215f7a8f8d7e1ace60a638f477c501d1c79b9d406ca0f0d58a5e1a51ea3578a
capture_envelope_bytes: 4836
capture_envelope_lines: 1
prereg_blob:            032a7528af340747c6e1b9ff7a59e36e387a0801
prereg_sha256:          8ad1e9cafd5cc6a9b18e2f83252c404bb6965c0240a118a858461bb04c459542
prereg_bytes:           27381
prereg_lines:           770
verifier_blob:          e748cf31d1c781bbd7249aefc11936123cd5011d
verifier_sha256:        bc7ab7565cc21c387485487fb23ce2d9cee0cf35a8a10869376de61874da9318
verifier_bytes:         43469
verifier_lines:         1200
verifier_pre_hash_match: yes
verifier_post_hash_match: yes
stdout_encoding:        ASCII (UTF-8 subset)
pinned_files_line_endings: LF-only
pinned_files_final_lf:  yes
expected_sha256:        6d512d1efe4f93505f69fc3cfe21182f02b7fd40cb052a59a7eb5095013f7e5a
expected_bytes:         1858
expected_lines:         26
public_readback:        PASS before execution
static_audit:           PASS, four independent reviews before pin
frozen_stdout_byte_identity: PASS
pinned_files_unchanged_after_execution: yes
predecessor_execution_leg: none; P-J-CIRCULAR-QDD-DUAL-SIMPLEX-BRIDGE-1 remains ABANDONED
result:                 PASS, 15/15 gates and 2/2 claims
architecture_gate:      PENDING
```

The public successor branch pinned `PREREG.md` and `verify.py` together in
one commit. Both immutable remote blobs were read back byte for byte and
recorded on issue #801 before execution. The successor verifier had not
previously been imported or executed.

The accepted verifier was invoked exactly once as the sole child of the
preregistered lossless evidence wrapper. The raw one-line hex envelope was
exposed and retained before parsing. It records matching pre/post verifier
hashes, exit zero, empty stderr, and stdout byte-identical to `EXPECTED.txt`.
Neither pinned file changed.

The abandoned predecessor is not an execution leg and contributes no
transcript, decision, or evidence. This is the sole local x86_64 formal leg.
Public GitHub-hosted x86_64 and aarch64 replay, aggregate validation, and
post-result manual security review are pending at the time of this immutable
record. No hostname, machine nickname, private address, credential, token, or
ambient environment value is recorded.
