# P-J-PLENUM-CENTERING-INDEX-1 formal run record

```text
pin_commit:             89047f3921959457f635687bd120e323ea9df05a
pin_tree:               a615b0ff9fa651ee57a25886917978bb56145f73
base_commit:            fbf33fa1116d9e3526ac4ae057356cf2d2bddb6e
public_lock:            issue 814
public_readback_comment: https://github.com/mathorn1973/twist-j/issues/814#issuecomment-5546492828
command:                python3 probes/P-J-PLENUM-CENTERING-INDEX-1/verify.py
platform:               Ubuntu 24.04.3 LTS
architecture:           x86_64
python:                 3.12.3
start_utc:              2026-09-04T21:12:26.955871Z
finish_utc:             2026-09-04T21:12:26.991043Z
formal_execution_count: 1
exit_code:              0
stdout_sha256:          a48a88c3545f9d355b89b125e873882968ddad4771502c9462e1a9dd489d983c
stdout_bytes:           328
stdout_lines:           10
stdout_line_endings:    LF-only
stdout_final_lf:        yes
stdout_encoding:        ASCII (UTF-8 subset)
stderr_sha256:          e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes:           0
stderr_lines:           0
prereg_blob:            11344d8d76de28d24a6be52543bb22be6d8eeab7
prereg_sha256:          9af0e477fea192603550e72f624398ac1f43ff6bac09b4a86040848d9d2cc494
prereg_bytes:           11268
verifier_blob:          d2c6b0dea1ecb161fdbea73666c463a33c107706
verifier_sha256:        e5ef4861a42004d709cec63dfcf299be6dcc4186e89a7d5ba5a9243cc6f5a900
verifier_bytes:         4510
verifier_pre_sha256:    e5ef4861a42004d709cec63dfcf299be6dcc4186e89a7d5ba5a9243cc6f5a900
verifier_post_sha256:   e5ef4861a42004d709cec63dfcf299be6dcc4186e89a7d5ba5a9243cc6f5a900
verifier_pre_hash_match: yes
verifier_post_hash_match: yes
expected_sha256:        a48a88c3545f9d355b89b125e873882968ddad4771502c9462e1a9dd489d983c
expected_bytes:         328
expected_lines:         10
public_readback:        PASS before execution
captured_stdout_hex_hash_and_count: PASS
captured_stderr_hex_hash_and_count: PASS
expected_byte_identity_with_capture: PASS
pinned_files_unchanged_after_execution: yes
result:                 LOCAL CONFIRMED, 6/6 gates and 1/1 mathematical claim
architecture_gate:      PENDING
post_result_security_review: PENDING
```

The public readback binds both pinned files to the recorded Git blobs,
SHA-256 values and byte counts. The captured execution identifies the same
pin and has identical pre-execution and post-execution verifier hashes.
It reports exit zero, 328 stdout bytes in ten lines, and empty stderr.

The captured raw stdout and stderr hex were decoded after execution and
checked against their recorded SHA-256 values and byte counts. The stdout
was checked for ASCII, LF-only line endings and its final LF, then written
unchanged as `EXPECTED.txt`. All six scientific gates report `PASS`, and
the recorded terminal is `CONFIRMED`. The pinned source files still match
their public readback and their immutable commit.

The timestamps above are the UTC equivalents of the capture's explicit
`+02:00` timestamps. No additional environment settings or implementation
metadata are inferred from the output.

This is the sole local formal execution. Required public x86_64 and aarch64
replay, aggregate validation and post-result manual security review remain
pending at the time of this run record. The local mathematical result does
not register a public claim or change Canon.
