# Exact execution record

Candidate: C-INTEGRAL-GRAM-CONTACT-ARCHIVE-N.
Author: A. M. Thorn <thorn@twistj.com>.
SPDX-License-Identifier: Apache-2.0.
Status: NON-CANONICAL / L1 / completed exact finite audit on one architecture.
Reservation: [#1844](https://github.com/mathorn1973/twist-j/issues/1844).

## Public preregistration and source readback

Public source pin: `2670e0ef4deaea22d41eef588ea24aec5e68cb3d`.
Public basis: `a193e389fb1ddb0bdc89165b015c95a17eb1e425`, Public Canon v106.
Branch: `notes/c-integral-gram-contact-archive-n`.

The complete preregistration, analytical proof and both source programs were
published in this pin before either scientific execution. A fresh detached
Git checkout fetched the public pin. All eight published files matched their
prepublication byte counts, Git blob identifiers and SHA-256 values. HEAD
matched the public pin and the worktree was clean before execution. The same
complete checks passed after both runs and before adding these records.

The author explicitly approved the connected GitHub account's default commit
identity before publication. Source-file authorship remains A. M. Thorn.

The breaker was authored from PREREG.md alone before any output was seen.
Its stdout names local preparation commit
`c6e7eaef4741d7ec36bfb2e96d0e5831ea9295be` as its preregistration input.
That local authorship reference is not the public execution pin. The public
execution pin for both programs is the one stated above. PREREG.md is byte
identical to that local frozen input. The exact source and preregistration
hashes are in PREPARATION.md and SHA256SUMS.

## Commands and environment

Both commands ran from the repository root, concurrently in separate Python
processes, with independently captured stdout and stderr:

```sh
python3 -B notes/C-INTEGRAL-GRAM-CONTACT-ARCHIVE-N/verify.py
python3 -B notes/C-INTEGRAL-GRAM-CONTACT-ARCHIVE-N/break.py
```

Environment for both:

```text
PYTHONHASHSEED=0
PYTHONIOENCODING=utf-8
LC_ALL=C.UTF-8
PYTHONDONTWRITEBYTECODE=1
```

- Operating system: Linux.
- Architecture: x86_64.
- Python: 3.12.14 (cpython).
- Byte order: little.
- No floating point, tolerance, random sample or external data was used.
- Neither frozen source was edited after public pinning.

## Exact captured outputs

| Program | Started UTC | Finished UTC | Exit | Stdout bytes | Stderr bytes |
| --- | --- | --- | --- | --- | --- |
| verify.py | 2026-10-31T10:19:51+00:00 | 2026-10-31T10:19:53+00:00 | 0 | 681 | 0 |
| break.py | 2026-10-31T10:19:51+00:00 | 2026-10-31T10:20:02+00:00 | 0 | 1628 | 0 |

- EXPECTED.txt is the unmodified stdout of verify.py, SHA-256
  `79db6a2aa751b0362b5609e2293d33279510f59f7cbe5a51f5ac9ce0a09f1c12`.
- BREAK_EXPECTED.txt is the unmodified stdout of break.py, SHA-256
  `66a8d32d76aff04e579daecd9f4d7fa30dc65a7ba5df0ceb7d731144afdc8032`.
- Both stderr streams were empty, SHA-256
  `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

No synthetic expected stdout was substituted. Each file is the actual
captured output. The two programs intentionally have different diagnostic
formats; their complete stdout is not claimed to be mutually identical.

## Independent certificate comparison

The prescribed UTF-8 streams use the exact fixture and field order frozen
in PREREG.md. Both independently structured implementations produced:

| Certificate | Rows per implementation | Common SHA-256 |
| --- | --- | --- |
| Pair | 6561 | `813ea392db9eb4e42e6c2cc205f56b224699e37673d7a8c8fdef155513e3947b` |
| Program | 23040 | `ee8cdbe56ab01b745092d8fd700739f546120c35c3369b696b215101788f30e7` |

The pair stream covers every frozen F2 input and positive contact output.
The program stream covers the 1280 prepared cases followed by the 256
occupied cases, with all 15 boundaries per case. Equality was checked after
both completed runs. Source and output hashes were checked again before
writing this record. No mismatch, nonzero exit or stderr occurred.

## Evidential scope

This is one completed local execution of each of two separately authored
implementations on x86_64. It is not a two-architecture scientific replay.
The universal statements rely on PROOF.md, not these finite certificates.
The authored static proof review is not independent theorem acceptance.

Ordinary repository CI has x86_64 and aarch64 jobs, but its selectors execute
scientific verifiers under probes/ and reproduce/, not this notes/ directory.
It does not automatically execute either of these two programs. Green
repository CI must therefore be reported separately and cannot upgrade this
run to a two-architecture scientific computation gate. No workflow change,
Canon promotion or physical interpretation is implied by this record.
