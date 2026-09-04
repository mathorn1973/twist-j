# P-J-PLENUM-POLAR-GAUSS-1 formal run record

```text
pin_commit:             501f0ef860af56e8c328e950f52f42623c507c09
pin_tree:               28ebdbf6c11b598c116238ca2ae55f0adeef9d41
base_commit:            36293614bbf4c961c4a027155293352a8abad55e
public_lock:            issue 804
public_readback_comment: https://github.com/mathorn1973/twist-j/issues/804#issuecomment-5542420814
command:                python3 probes/P-J-PLENUM-POLAR-GAUSS-1/verify.py
formal_invocation:      one subprocess.run child under the exact lossless wrapper frozen in PREREG.md
child_argv:              python3 probes/P-J-PLENUM-POLAR-GAUSS-1/verify.py
external_timeout_seconds: none
environment:            env -i PATH=/usr/bin:/bin LC_ALL=C PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 PYTHONNOUSERSITE=1 PYTHONSAFEPATH=1 TZ=UTC
platform:               Ubuntu 24.04
kernel:                 Linux 6.18.35
architecture:           x86_64
python:                 CPython 3.12.3
python_executable:      /usr/bin/python3
start_utc:              2026-09-04T15:06:16.411706Z
finish_utc:             2026-09-04T15:06:17.122415Z
formal_execution_count: 1
child_invocations:      1
capture_complete:       true
exit_code:              0
stdout_sha256:          34ec9a43130413fbb98c272af1b6d6f0fcd9ae487876c72b0d7b8c2914e71a61
stdout_bytes:           1469
stdout_lines:           22
stdout_line_endings:    LF-only
stdout_final_lf:        yes
stderr_sha256:          e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes:           0
stderr_lines:           0
prereg_blob:            0ff431b7aecba2de8d85eccf78439f9fbc45abd3
prereg_sha256:          11b5af1dcb617d53bf5d274307bc327214dbfff6fb1398814efa79416e3e076a
prereg_bytes:           20674
prereg_lines:           657
verifier_blob:          e2f4ae1ba02cfd15855cde03c493e474244b40d9
verifier_sha256:        7f7e0fddc72b8e282e77f56d11c6f1f28dff0ac2bac85c45d8beae2db06c8ebc
verifier_bytes:         22352
verifier_lines:         676
verifier_pre_hash_match: yes
verifier_post_hash_match: yes
stdout_encoding:        ASCII (UTF-8 subset)
pinned_files_line_endings: LF-only
pinned_files_final_lf:  yes
expected_sha256:        34ec9a43130413fbb98c272af1b6d6f0fcd9ae487876c72b0d7b8c2914e71a61
expected_bytes:         1469
expected_lines:         22
public_readback:        PASS before execution
static_audit:           PASS before pin
frozen_stdout_byte_identity: PASS
pinned_files_unchanged_after_execution: yes
result:                 SCIENTIFIC-FIRED, 15/16 gates and 1/2 claims confirmed
architecture_gate:      PENDING
```

The public branch pinned `PREREG.md` and `verify.py` together in one commit.
Both immutable remote blobs were read back byte for byte and recorded on issue
#804 before execution. Before that pin the verifier had been parsed and syntax
compiled statically but had never been imported or executed.

The accepted verifier was invoked exactly once as the sole child of the
preregistered lossless evidence wrapper. The raw one-line hex envelope was
exposed in full before parsing. It records matching pre-call and post-call
verifier hashes, exit zero, empty stderr, and the exact stdout preserved in
`EXPECTED.txt`. Neither pinned file changed.

Gate G02 returned `FAIL`. Every other gate returned `PASS`. Under the frozen
decision rule, claim A is `FIRED` and claim B is `CONFIRMED`. This is a
completed scientific result and may not be relabeled as `STOP` or
`ABANDONED`.

This is the sole local x86_64 formal leg. Public GitHub-hosted x86_64 and
aarch64 replay, aggregate validation, and post-result manual security review
are pending at the time of this immutable run record. No hostname, machine
nickname, private address, credential, token, or ambient environment value is
recorded.
