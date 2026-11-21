# First-run custody

Author: A. M. Thorn <thorn@twistj.com>.
SPDX-License-Identifier: Apache-2.0.

The first accepted execution completed with the predeclared scientific
status **CERTIFIED**. This record preserves that execution; preparing the
record did not rerun the scientific entry point.

```text
pin_commit: 173ca05aab8fac006a5e4d54d640f8a9eff35d18
verifier_sha256: 0f4c0ca43024aeeb93d41acb35e41f52d5d1dfd9fe960067172a918e33d74a67
command: python3 probes/P-BOUND-PAIR-ABSOLUTE-CAPTURE-1/verify.py
platform: Ubuntu 24.04.3 LTS
architecture: x86_64
python: 3.12.14
exit_code: 0
stdout_sha256: 8927eb5c1fe3314094189aa5a9f34bf64710c242f1f06e01e3b6e394d7c2c989
stdout_bytes: 1387
stdout_lines: 16
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

## Public pin and execution order

The reserved branch `probe/P-BOUND-PAIR-ABSOLUTE-CAPTURE-1` was created at
the stated pin. Its ref and all six input files were then read back through
the public GitHub interface. Every file matched the local UTF-8 bytes,
SHA-256 and Git blob stated below before execution.

```text
public_readback_utc: 2026-10-28 08:13:10 UTC
execution_started_utc: 2026-10-28T08:13:27.713355+00:00
execution_finished_utc: 2026-10-28T08:13:38.313713+00:00
elapsed_seconds: 10.600333417000002
outer_timeout_seconds: 600
timed_out: false
```

The six pinned files were materialized with their repository-relative
paths in the local run directory. No full local Git checkout is claimed.
The verifier reads only its two pinned Python helpers and the standard
library; it does not read ambient files, call Git or access the network.
The public pin's parent is the unchanged v106 main
`a193e389fb1ddb0bdc89165b015c95a17eb1e425`.

The execution environment fixed `LC_ALL=C`, `LANG=C`,
`PYTHONDONTWRITEBYTECODE=1`, `PYTHONHASHSEED=0` and `TZ=UTC`.
The actual stdout was captured as bytes and copied unchanged to
`EXPECTED.txt`. Actual stderr was empty. The process completed within the
outer timeout; elapsed time is administrative metadata, not a scientific
classification condition.

## Complete pinned input custody

| Input | Bytes | SHA-256 | Git blob |
|---|---:|---|---|
| `probes/P-BOUND-PAIR-ABSOLUTE-CAPTURE-1/verify.py` | 17081 | `0f4c0ca43024aeeb93d41acb35e41f52d5d1dfd9fe960067172a918e33d74a67` | `f8896dab5a934313ca6e14c78c92ef45416d3f37` |
| `probes/P-BOUND-PAIR-ABSOLUTE-CAPTURE-1/interval_core.py` | 22802 | `cbf3259297b47c3fcd13e122e747f8c140b27c97917b6f242e5bb16811208ae1` | `6102b3c13732b79904a0a726595a47f8d926c096` |
| `probes/P-BOUND-PAIR-ABSOLUTE-CAPTURE-1/model.py` | 15753 | `6984302b20df4154dad6c2afd9d2becb82df4a01b03c4a0390041d0ebba8fdce` | `809f1021c99a43627262f75785a313240880760b` |
| `probes/P-BOUND-PAIR-ABSOLUTE-CAPTURE-1/PREREG.md` | 17892 | `f8badc05e43a42d90fb5d58b97b9a5543888cf83752102f71f57768878b083fd` | `6e3d6317830b1f82d221d0c38b23e34ea120f8e8` |
| `notes/C-BOUND-PAIR-ABSOLUTE-CAPTURE-N/PROOF.md` | 31450 | `0cd1955901fcf98a27a7171b0f94611bf358cc2cf6eea029e9a9dc8c1f6d3954` | `2ce2e37f042491e6653b1af415becbaf49989ac3` |
| `notes/C-BOUND-PAIR-ABSOLUTE-CAPTURE-N/SOURCES.md` | 8179 | `6ebf2d426e82f7f00a36a41853aeedfab0e0e925c6db8662243980c8c294a34f` | `675de1aefe23ecb2658cee25f21f9529398f6d1b` |

All six input files were checked again against these hashes when this
record was prepared. None was changed after the pin. Compilation and
static authoring review preceded the pin; neither imported or executed
the scientific calculation.

## Contributor identity and reproduction scope

Before branch publication and execution, the author explicitly approved
using the connected account's commit identity
`A. M. Thorn <221838986+mathorn1973@users.noreply.github.com>` for this
probe. The approval is recorded in reservation #1814. The pinned source
author/license notices and repository-wide default remain unchanged.

This is the first local x86_64 execution record. Required byte-identical
x86_64/aarch64 reproduction is supplied by the unchanged pull-request
workflow and must be assessed on the actual final PR head. This local
record does not invent later workflow outcomes or independent theorem
acceptance.
