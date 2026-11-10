# First pinned execution

NON-CANONICAL / L1. One author, two arithmetic representations.

pin_commit: 787bce2ed8fddf89c4812f8bc2aee2eee3b2b930
verifier_sha256: 77a243645ffdabe503a1f567ae3d0f02c876b3eb0becb9f5fb98471a276a13b0
command: python3 probes/P-J-FUNDED-PAIR-NETWORK-1/verify.py
platform: Ubuntu 24.04.1 LTS
architecture: x86_64
python: 3.12.3
exit_code: 0
stdout_sha256: b2975a7d25474ba4019fddb51951842bc977e68e97b1f8f162be31ed05dfd569
stdout_bytes: 781
stdout_lines: 1
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

started_utc: 2026-11-09T00:14:32.773462+00:00
completed_utc: 2026-11-09T00:14:35.596543+00:00

## Source custody and execution

Reservation #1969 and its pre-execution analytical comment fixed the network,
fixed-pair obstruction, transport family and four-cell re-pairing cycles.
The complete source set was committed locally before execution, transported
as a Git bundle, then published unchanged through the authorized connector.
The shell's read-only transport did not publish a commit; its local commit
is not used as the execution pin. No credentials or permissions were changed.
The user expressly authorized the connected account's default author address.

The public pin contains the three scientific sources in one commit on the
verified public main. Both documents were read back through the connector.
All three exact files were also fetched at the public SHA and compared byte
for byte with a clean checkout, with the hashes below, BEFORE execution.
Only static parsing and source inspection occurred before that readback.

| Source | SHA-256 | Bytes |
| --- | --- | ---: |
| PREREG.md | e857aa76a43fd8835b896fd29a42ff556cbad31ba734d2fc05c1b48fec2a85dc | 8004 |
| PROOF.md | f106138801d0017927a067e430f1835b76197cae87af379297f34423db5a20d0 | 11784 |
| verify.py | 77a243645ffdabe503a1f567ae3d0f02c876b3eb0becb9f5fb98471a276a13b0 | 11985 |

The command ran from the repository root with assertions enabled. Inherited
PYTHON* and TWISTJ* variables were removed; PYTHONDONTWRITEBYTECODE=1,
PYTHONHASHSEED=0, LC_ALL=C, LANG=C and TZ=UTC were set. Timeout: 600 seconds.
The observed wall time was approximately 2.823 seconds, operational metadata,
not a scientific quantity or threshold. Exact stdout was retained unchanged
as EXPECTED.txt after observing exit zero and empty stderr. No scientific
source, inventory, reader, prediction or threshold was edited after the pin.

## Independence and architecture boundary

Polynomial reduction and five-term cyclic arithmetic were written by the same
author and share gate logic. Their agreement is NOT independent authorship.
Direct shift and complete-cycle formulas additionally audit that shared logic.
The analytic proofs remain author proofs pending independent review.

This file records the first x86_64 execution only. Public x86_64/aarch64
reproduction must compare the unchanged verifier to these same expected bytes;
actual workflow receipts are recorded on the pull request after completion.
A repeated same-architecture run is reproduction, not a second architecture.
No Canon, existing gate, registry, workflow, primitive-owner source or release
is changed by this result.
