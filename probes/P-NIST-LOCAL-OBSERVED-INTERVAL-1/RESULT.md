# NIST causal lossless interval adapter: result

Status: **CONFIRMED**, two conditional results for the frozen archived-record audit.

**PUBLIC CLAIMS UNREGISTERED / CANON UNCHANGED / PHYSICAL COMPLETION UNRESOLVED.**

## A. Lossless ownership and exact derived references

The pinned adapter reconstructs every original indexed row in the four declared
member portions exactly once through owned packet rows and the pending suffix.
Reconstruction was compared directly with an independent original-row buffer;
matching digests are a compact record of that audit, not an injectivity premise.
The nonowning right sync reference is excluded from reconstruction and retained
as the next interval's owned left sync. Derived setting, detector, metadata and
signed-delay views match the independently calculated row references.

| Object | Selected rows | Closed intervals | Emitted packets |
|---|---:|---:|---:|
| Alice 00_03 sync | 485,503 | 194,914 | 194,914 |
| Bob 00_03 sync | 489,229 | 197,214 | 197,215 |
| Alice run3 | 1,048,576 | 512,047 | 512,047 |
| Bob run3 | 1,048,576 | 514,203 | 514,203 |

There are **3,071,884 selected rows**, **1,418,378 closed intervals** and
**1,418,379 emitted packets**. The additional packet is Bob sync's one-row
PREFIX, which contains a detector row preceding the first sync. It remains
preserved; it is not assigned to an invented earlier interval. Every object's
final PENDING_SUFFIX remains a snapshot and is not closed by end of input.
Alice sync starts directly with a sync, so no empty PREFIX is emitted.

Both sync members were fully read with CRC verification on each traversal.
The run3 members were limited to their first 1,048,576 rows. Their tails were
not interpreted. Complete compressed archive identities were checked before
ZIP access; byte authentication does not qualify unread tails semantically.

## B. Causal emission, immutable snapshots and chunk-independent audit

Every actual packet is emitted only when its required right sync row arrives.
Previously emitted packets are unchanged as later rows are consumed. Pending
snapshots neither consume rows nor invent a boundary. Continuous input and
the frozen 31-row chunking agree at every declared prefix checkpoint and at
the final selected extent, including packet, pending and reconstruction views.

The separate synthetic audit covers all **2,801 channel sequences** of lengths
zero through four over the frozen seven-channel alphabet, with the specified
numeric timetag and transfer assignments. It checks all 13,539 prefixes and
13,539 two-chunk splits. Unknown channels, absent/repeated/both settings,
calendar rows, nonmonotone words and empty input are algorithmic fixtures,
not experimental observations. This finite enumeration does not exhaust all
possible uint64 assignments. PROOF.md supplies the general induction argument
for the defined mathematical state relation; the finite audit alone does not
prove universal correctness of arbitrary Python executions.

## Frozen gates and exact evidence

| Gate | Checked conditions | Failed conditions | Result |
|---|---:|---:|---|
| G01_SYNTHETIC_REFERENCE | 91,973 | 0 | PASS |
| G02_ACTUAL_LOSSLESS | 8,510,562 | 0 | PASS |
| G03_ACTUAL_PREFIX_CHUNKING | 4,255,473 | 0 | PASS |
| G04_ACTUAL_DERIVED_REFERENCE | 3,307,036 | 0 | PASS |

Claim A uses G01/G02/G04; claim B uses G01/G03/G04. Neither falsifier fired.
The exact first formal execution followed public pin
`0ddc026fa5f2eefcfbc122d38585f475bd6418cc` and public byte readback of all six
new source files and the inherited dependencies. It exited zero with empty
stderr, unchanged source hashes and a clean checkout. EXPECTED.txt is the
exact **58,096-byte, 1,419-line** JSON stdout with SHA-256
`c10825ec57fd5672e7a05d9caba1d1946cbea420d9cbf10968b596c7cb847836`.
RUN.md records the complete pin and execution inventory.

Independent public cold replay on **aarch64 and x86_64 passed** in
[workflow 33962156745](https://github.com/mathorn1973/twist-j/actions/runs/33962156745), with identical verifier and stdout hashes.
The required aggregate check, all 155 tool tests, repository checks and
independent post-result scope/integrity/license review passed. RUN.md gives
the job references and exact evidence. The two-architecture computation gate
is satisfied for this conditional audit; claims remain unregistered and
no public status is changed.

## Signed-delay diagnostics and physical boundary

The frozen diagnostics preserve signed raw-tick differences. For closed run3
intervals, Alice's 24,469 detector rows have detector-minus-left-sync range
7 through 129,038 and detector-minus-unique-setting range -43 through 128,986.
Bob's 20,159 rows have the corresponding ranges 125 through 129,070 and
-240 through 128,720. These are record differences with their exact reference
rows. Negative detector-minus-setting values are retained; they do not fire
an unregistered ordering predicate or authorize changing a detection window.
Full histogram digests and the preregistered bounded summaries are in stdout.

This result is an L5 archived-record adapter. It supplies neither a physical
trial partition nor cross-station pairing, calibrated timing/window membership,
registration coverage, no-click, efficiency, dead time, post-state or reset.
Zero and multiple detector-row cases remain distinct without coarsening into
exclusive QDD outcomes. Packet closure is arrival of a raw boundary record,
not terminal measurement semantics or COMM-SAT. The separate NIST measurement
contract's physical interpretation and OK/STOP/history wrappers are not tested
implementations of this adapter kernel.

The previous qualification census was disclosed before this new pin. These
are reproducible computations on the same archive, not blind data or independent
experiments. No new source, member, tail, time window or threshold was selected.
No output feeds U. No TWIST-J/NIST apparatus identification, L1-to-L5 or L5-to-L6
bridge, photon completion or Born occurrence law follows.

`QDD-INSTRUMENT-APPARATUS` remains O / STOP. Both O2 children and Bell causal
accounting are unchanged. `COINCIDENCE-RECORD-FREQUENCY` remains candidate-H /
UNTESTED / STOP outside the registry. Public Canon v76 is unchanged.
