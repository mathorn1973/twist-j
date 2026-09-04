# P-J-SIMPLEX-TIGHT-FRAME-DILATION-BOUNDARY-1 formal run record

```text
pin_commit:             3194c6f6dcd24b9e1c552be34ed6b103b2b4ade6
pin_tree:               a35c84cd689192f9666d0f842b187943965514fd
base_commit:            ba728ffb6eea65c3c652ab4ec3a853889e6e590b
public_lock:            issue 806
public_readback_comment: https://github.com/mathorn1973/twist-j/issues/806#issuecomment-5542617872
command:                python3 probes/P-J-SIMPLEX-TIGHT-FRAME-DILATION-BOUNDARY-1/verify.py
formal_invocation:      one subprocess.run child under the exact lossless wrapper frozen in PREREG.md
child_argv:              python3 probes/P-J-SIMPLEX-TIGHT-FRAME-DILATION-BOUNDARY-1/verify.py
external_timeout_seconds: none
environment:            env -i PATH=/usr/bin:/bin LC_ALL=C PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 PYTHONNOUSERSITE=1 PYTHONSAFEPATH=1 TZ=UTC
platform:               Ubuntu 24.04
kernel:                 Linux 6.18.35
architecture:           x86_64
python:                 CPython 3.12.3
python_executable:      /usr/bin/python3
start_utc:              2026-09-04T15:19:31.547842Z
finish_utc:             2026-09-04T15:19:32.239288Z
formal_execution_count: 1
child_invocations:      1
capture_complete:       true
exit_code:              0
stdout_sha256:          5366e476df3c4c3e4f6b9219b334919b398932e725759008f956738e9da9aae7
stdout_bytes:           1550
stdout_lines:           21
stdout_line_endings:    LF-only
stdout_final_lf:        yes
stderr_sha256:          e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes:           0
stderr_lines:           0
prereg_blob:            e93e2c1b12db8ad0815f14ee284761c33d57b74a
prereg_sha256:          f381849efeff78b810adc8e64a354d80d37df7e3b78d717cca6477d61a15cabb
prereg_bytes:           20646
prereg_lines:           590
verifier_blob:          40179727473d7c250fe25206d2d50768e86b1768
verifier_sha256:        f964e45237315095221dd26f3e331c1e2f01b41920daf2b35e0399e4dbc4dc64
verifier_bytes:         19930
verifier_lines:         579
verifier_pre_hash_match: yes
verifier_post_hash_match: yes
stdout_encoding:        ASCII (UTF-8 subset)
pinned_files_line_endings: LF-only
pinned_files_final_lf:  yes
expected_sha256:        5366e476df3c4c3e4f6b9219b334919b398932e725759008f956738e9da9aae7
expected_bytes:         1550
expected_lines:         21
public_readback:        PASS before execution
static_audit:           PASS before pin
frozen_stdout_byte_identity: PASS
pinned_files_unchanged_after_execution: yes
result:                 PASS, 15/15 gates and 2/2 claims
architecture_gate:      PENDING
```

The public branch pinned `PREREG.md` and `verify.py` together in one commit.
Both immutable remote blobs were read back byte for byte and recorded on issue
#806 before execution. Before that pin the verifier had been parsed and syntax
compiled statically but had never been imported or executed.

The accepted verifier was invoked exactly once as the sole child of the
preregistered lossless evidence wrapper. The raw one-line hex envelope was
exposed in full before parsing. It records matching pre-call and post-call
verifier hashes, exit zero, empty stderr, and stdout byte-identical to
`EXPECTED.txt`. Neither pinned file changed.

All fifteen gates passed and both frozen claims were confirmed at the
candidate-T/L1 ceiling. This is the sole local x86_64 formal leg. Public
GitHub-hosted x86_64 and aarch64 replay, aggregate validation, and post-result
manual security review are pending at the time of this immutable run record.
No hostname, machine nickname, private address, credential, token, or ambient
environment value is recorded.
