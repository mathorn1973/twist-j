# P-J-FIBONACCI-BRAID-1 formal run record

```text
pin_commit:             84376b4b0a53e16c91822d4c5293649f70d9ad5a
pin_tree:               f86e00187a654cb101824a8935521d506ef9061e
base_commit:            01b861c8e36cb56f9b4b24681018beec27d521eb
public_lock:            issue 795
public_readback_comment: https://github.com/mathorn1973/twist-j/issues/795#issuecomment-5530529073
command:                python3 probes/P-J-FIBONACCI-BRAID-1/verify.py
formal_invocation:      /usr/bin/timeout --signal=TERM 600s /usr/bin/env -i PATH=/usr/bin:/bin LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC /usr/bin/python3 probes/P-J-FIBONACCI-BRAID-1/verify.py
external_timeout_seconds: 600
environment:            env -i PATH=/usr/bin:/bin LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
platform:               Ubuntu 24.04.3 LTS
kernel:                 Linux 6.18.35
architecture:           x86_64
python:                 CPython 3.12.3
start_utc:              2026-09-03T18:49:22Z
finish_utc:             2026-09-03T18:49:22Z
elapsed_wall_nanoseconds: 65870483
formal_execution_count: 1
exit_code:              0
stdout_sha256:          09886942e87b9962b85f9823eeac8b4fb36b9f41489ecae3731dac9a30240999
stdout_bytes:           1391
stdout_lines:           23
stdout_line_endings:    LF-only
stdout_final_lf:        yes
stderr_sha256:          e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes:           0
stderr_lines:           0
prereg_blob:            da476b6c0a6d5645cf9077c474161f77bcf8ed13
prereg_sha256:          a444acb8890c1f34348fb922bd7fccfc13b6f30e34a1400a423db58c95f29061
prereg_bytes:           18421
prereg_lines:           557
verifier_blob:          45f2ba84ad1298fba926b801a712feafa4d8746c
verifier_sha256:        d30193d720e57a8e35c0ee40161406f50150ff024d96d240c44c699b869b1b77
verifier_bytes:         25315
verifier_lines:         843
encoding:               UTF-8 (ASCII subset)
line_endings:           LF-only
final_lf:               yes
expected_sha256:        09886942e87b9962b85f9823eeac8b4fb36b9f41489ecae3731dac9a30240999
expected_bytes:         1391
expected_lines:         23
public_readback:        PASS before execution
static_audit:           PASS, two independent reviews before pin
frozen_stdout_byte_identity: PASS
pinned_files_unchanged_after_execution: yes
result:                 PASS, 17/17 gates and 2/2 claims
architecture_gate:      PENDING
```

The public branch pinned `PREREG.md` and `verify.py` together in one commit.
Both immutable remote blobs were read back byte for byte and recorded on the
public claim issue before execution. The accepted verifier had not previously
been imported or executed.

No separate Python-startup preflight process was performed or claimed. Public
byte readback and the static audits were the pre-execution checks.

The pinned verifier was then executed exactly once with the formal invocation
above. It exited zero, wrote empty stderr, and its stdout is byte-identical to
`EXPECTED.txt`. The frozen `PREREG.md` and `verify.py` remained unchanged.

This is the sole local x86_64 formal leg. Public GitHub-hosted x86_64 and
aarch64 replay, aggregate policy validation, and manual security review are
pending at the time of this record. No hostname, machine nickname, private
address, or fleet label is recorded.
