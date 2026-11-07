# Joint-preparation execution record

**NON-CANONICAL / L1. Author-side exact finite audit.**

Both recorded prospective executions passed at the same immutable source
pin [3c2b3529bb228fe9b95fe9217452c22c6a787aee](https://github.com/mathorn1973/twist-j/commit/3c2b3529bb228fe9b95fe9217452c22c6a787aee).

- Verifier: verify_joint_preparation.py, 19111 bytes.
- Source SHA-256: 5fb5dfb0b329e8d57ad14ecabcfe0fbba6ee8bbe6da91a4af2a157b89a70186d.
- Command on both architectures: python3 -I -B verify_joint_preparation.py.
- Working directory: notes/C-LOADED-CURRENT-WORK-PHASE-COMPATIBILITY-N.
- Fixed limits per process: 300 seconds wall time and 1073741824 bytes (1 GiB) memory.

## Runs and exact output

JOINT-RUNS.json contains the two supplied run receipts. Their timestamp
strings are preserved exactly, including precision and UTC offsets.

| Architecture | Platform | Python | started_utc | Elapsed seconds |
|---|---|---|---|---:|
| x86_64 | Ubuntu 22.04.5 LTS | 3.10.12 | 2026-11-07T12:23:07.216318+00:00 | 1.4203121780000005 |
| aarch64 | Debian GNU/Linux 12 (bookworm) | 3.11.2 | 2026-11-07T12:23:33.878744+00:00 | 3.7997759410063736 |

The coordinator performed the aarch64 execution in a clean clone of the
public source pin. Both executions used the same frozen verifier bytes.
Elapsed values are runtime metadata from the receipts, not mathematical
outputs.

Both processes exited zero, reported timeout false, and produced empty
stderr. Both scientific outputs contain 1243372 assertions and PASS.
No assertion, exception, timeout, or memory-limit failure occurred in
these two recorded scientific runs. No failed scientific run was repaired
or omitted under this pin.

The stdout files were compared directly and are byte-identical:

- Length: 1282 bytes.
- SHA-256: 66776cfa8b5bc9609c34806e1416aea559363b6a6e72034646a7038c32e4dbc3.
- Empty stderr SHA-256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.

JOINT-EXPECTED.txt is an exact byte copy of the recorded x86_64 stdout.
The aarch64 stdout was checked against those same bytes. Preparation of
this run record used receipt parsing, byte comparisons and hashing only.
It neither imported nor executed a scientific verifier.

## Source custody before execution

The supplied pre-execution public-readback receipt identifies the same
pin and records successful readback of all five public blobs below.
Each recorded Git blob identity matches the corresponding pinned bytes.

| File | Git blob |
|---|---|
| JOINT-CONSTRUCTION.md | 3a5cf037f20bc95d7a02d1330242e04ae4727d91 |
| JOINT-OBSTRUCTION.md | c5259b02c0c42e4c8a25f62a9b403c3475f0c3aa |
| JOINT-PREREG.md | 1322318f70a24a555792af7e6630348c9c94b890 |
| JOINT-SHA256SUMS | c6a80cd2237a14fac8f6516e7bd464cdf1b6b0de |
| verify_joint_preparation.py | 28925b88b52abd80bec49e92511d12ad22325c70 |

All four entries in JOINT-SHA256SUMS verify:

| Source file | SHA-256 |
|---|---|
| JOINT-CONSTRUCTION.md | ae5996409e2a9b2a239a996dbe2bd57b7176930d581aad542e60575a8de4d8a9 |
| JOINT-OBSTRUCTION.md | cc67b28d044e0ebf3c8b03b9586b11a41fdb088429936f3f2c9988f8cc8e77f5 |
| JOINT-PREREG.md | 025c8534487464e9c34421067fab69140c861c3de6ead2b210c3b413871c7c7c |
| verify_joint_preparation.py | 5fb5dfb0b329e8d57ad14ecabcfe0fbba6ee8bbe6da91a4af2a157b89a70186d |

The four predecessor manifests remain byte-identical to their versions
at fd6bf60bdcf19e6a4267c80353bfed7b60af12f5, the parent of this source pin.
Their existing entries all still verify: SOURCE-SHA256SUMS has eight,
FULLFIELD-SHA256SUMS five, RECEIVER-SHA256SUMS five, and STOCK-SHA256SUMS
four. No frozen source, proof, preregistration, or source manifest was
changed to package these results.

## Scope of the evidence

The analytical targets were exposed before this audit. These are
author-side executions and static reviews from the same working session,
not independent acceptance. They do not enlarge any older independent
review lock.

The new verifier is standalone. No predecessor verifier was imported or
replayed, and no native clock or field trajectory was rerun. The finite
scope is exactly JOINT-PREREG.md: the one-helper and four-helper prepared
protocols, their complete inverses and retained records, independent
donor-bank phases, the equal-length family, independent-helper permutation,
residue controls, frame covariance, and occupied-state controls.

The prepared fifth iterate is not asserted for arbitrary occupied states.
The source aligns to the initial donor/reference phase while the used donor
retains the old relative phase. The recorded construction does not create
a coherent bank from vacant resources, erase information, select an
attractor or physical phase law, compile a field-action controller, or
derive electromagnetic coupling. No scientific promotion is performed.
