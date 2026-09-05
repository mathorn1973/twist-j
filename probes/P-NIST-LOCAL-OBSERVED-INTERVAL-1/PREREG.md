# P-NIST-LOCAL-OBSERVED-INTERVAL-1 preregistration

FROZEN TARGET / PRIOR PREFIX EXPOSURE DECLARED / PUBLIC STATUS NONE.

```text
owner: A. M. Thorn
issue: https://github.com/mathorn1973/twist-j/issues/838
branch: probe/P-NIST-LOCAL-OBSERVED-INTERVAL-1
base: 11556f685f0c51c06fec6da32118a1d1e63d7fa4
authority: ACTIVE Public Canon v76
action layer: L5 archived record transformation; no physical lift
claim_A: NIST-LOCAL-OBSERVATION-LOSSLESS
claim_B: NIST-LOCAL-OBSERVATION-PREFIX-CAUSALITY
new formal executions at pin: 0
public status: NONE
```

## 1. Equation and targets

For a finite sequence `r_i=(i,c_i,t_i,x_i)`, indices are consecutive from zero
and each raw word `(c_i,t_i,x_i)` is an unsigned 64-bit integer. The letter
`t_i` denotes only the second raw word; at channel 64 it is calendar metadata,
not an event timetag. No ordering of these words is assumed.

Let `j_0<...<j_(K-1)` be the indices of channel-6 rows. Define the exact
ownership partition of `[0,N)`:

```text
if K=0:  UNANCHORED owns [0,N), including N=0;
if K>0:  PREFIX owns [0,j_0), omitted if empty;
         CLOSED_INTERVAL(k) owns [j_k,j_(k+1)), 0<=k<K-1;
         PENDING_SUFFIX owns [j_(K-1),N).
```

A closed packet also references the complete right sync row `r_(j_(k+1))`.
That reference is explicitly nonowning. It supplies lookahead and can appear
again as the next packet's owned left boundary without duplicating row ownership.
The prefix emits when the first sync arrives. A closed interval emits only
when its right sync arrives, with that row's original index as `emitted_at`.
UNANCHORED and PENDING_SUFFIX are nonmutating snapshots, with no event emission.
End of the inspected prefix is not a physical terminal event or a reset.

Claim A: on the four inherited selected data portions, packet ownership
reconstructs every original `<QQQ` row exactly once in original order; the
derived field views agree with their named raw rows and preserve multiplicity.
The independent batch decomposition and streaming output also agree on the
complete frozen synthetic family. Every equality is exact, with zero tolerance.

Claim B: on the same data, the emitted packet sequence and pending state are
independent of the frozen input chunking, snapshots do not mutate the state,
all tested input prefixes agree with the corresponding streaming state, and
emission requires exactly the named causal right boundary. Existing emitted
packets persist under extension. All synthetic prefix comparisons must agree.

PROOF.md supplies the elementary partition and causal invariant argument.
The formal computational result is restricted to the exact declared audit;
no physical completeness or statistical generalization follows from a census.

## 2. Accepted code and dependency identity

The accepted implementation is `adapter.py`, and the sole scientific entry
point is `verify.py`. The verifier's literal `MANIFEST_SHA256` binds
DEPENDENCIES.json, which binds the adapter and each inherited executable/data
dependency by full SHA-256 and byte count. All scientific imports occur only
after those dependency identities are checked in the pinned run.

The inherited qualification probe is complete and unchanged. Its source
manifest and acquisition/hash routines are reused as immutable dependencies,
not resumed as a new scientific gate. All new source files and this complete
preregistration are committed, pushed and read back before the first new
execution. Only static source reading and parsing occur before that pin.

Run from a clean Linux checkout at the repository root:

```text
python3 probes/P-NIST-LOCAL-OBSERVED-INTERVAL-1/verify.py
```

Python 3.12 standard library suffices. As before, optional
`TWISTJ_NIST_CACHE_DIR` is only a transport hint. Every complete compressed
archive is counted and SHA-256 checked before ZIP access; cold replay retrieves
the same four literal NIST URLs with the preserved notice. No redirects,
different source selection, changed member or alternate endian trial is allowed.
The existing per-verifier timeout remains 600 seconds, with no workflow change.

## 3. Carrier and exact data scope

Use exactly the four objects and nominated member basenames from
`P-NIST-RAW-RECORD-QUALIFICATION-1/SOURCE.json`: Alice/Bob 00_03 sync and
Alice/Bob run3. Decode exactly the same first
`min(1048576, member_size/24)` rows. The two sync members are known to fit
entirely; run3 tails remain outside scope. Complete compressed hash verification
does not claim that an unread uncompressed tail has been interpreted.

The prior published audit decoded 3,071,884 total rows and found one setting
row in every closed run3 interval. This exposure is declared. Its timing and
channel summaries are known. This successor is not blind, a new experiment or
independent physical replication. It computes new packet and delay descriptions
only after its own pin; the earlier probe is neither edited nor relabeled.

The mathematical adapter accepts every correctly indexed raw-word sequence,
including unknown channels and repeated/missing settings. Its synthetic audit
exhausts channel words of length zero through four over
`{0,2,4,5,6,64,99}`: exactly 2,801 sequences, with the deterministic word and
transfer assignments fixed in the accepted verifier. Channel 99 explicitly
tests preservation of unknown rows. These are declared algorithmic fixtures,
not experimental data or physical controls.

## 4. Observations, systematics and decision independence

Each packet retains complete raw owned rows and separately typed references
to setting, detector, PPS, calendar and unknown rows. Setting classes are
`ONEHOT_0`, `ONEHOT_1`, `MISSING`, `REPEATED_0`, `REPEATED_1`, and `BOTH`.
Detector classes are `NO_RECORDED_DETECTOR_ROW`, `SINGLE_RECORDED_DETECTOR_ROW`
and `MULTIPLE_RECORDED_DETECTOR_ROWS`. A closed interval's derived views concern
its interior; neither sync boundary is an observed detector or setting row.

Detector deltas from the left sync are signed integer raw-tick differences.
A delta from a setting is reported only when there is exactly one setting row;
otherwise its reference is explicitly missing or ambiguous. Calendar-64 words
are never used as event timetags. No pulse window, coincidence window, clock
offset, Alice/Bob pairing, timestamp sorting or physical outcome is inferred.

The fixed actual-prefix checkpoints are the distinct lengths in
`{0,1,2,3,7,31,127,1023,8191,65535,262143,N}` that lie within `[0,N]`.
Continuous and chunked traversals of the same authenticated member must agree;
the exact positive chunk cycle is frozen in code. All synthetic prefixes are
checked against a batch implementation built from sync-index slices. A pending
snapshot never consumes, resets or closes the stream. New right boundaries may
turn previously pending rows into a closed packet; they never rewrite a packet
that was already emitted.

Canonical compact JSON plus one LF per packet defines packet-stream hashes.
Reconstruction hashes use the concatenated owned original `<QQQ` bytes, omitting
all nonowning references. Bounded deterministic summaries and witnesses preserve
exact provenance; no full raw packet stream is tracked in Git. Public output
contains complete audit counts and digests, not sampled favorable intervals.
Any displayed first witnesses and histogram summaries have their caps and order
fixed in code before inspection.

## 5. Gates, failure thresholds and disposition

The four exact zero-tolerance gates are:

```text
G01_SYNTHETIC_REFERENCE       streaming, batch and every synthetic prefix agree
G02_ACTUAL_LOSSLESS          original indexed rows reconstruct exactly
G03_ACTUAL_PREFIX_CHUNKING   causal snapshots and chunk-independent prefixes
G04_ACTUAL_DERIVED_REFERENCE all derived views match independent row references
```

A claim is CONFIRMED only when every gate assigned to it in the frozen verifier
passes. G01 and G04 support both claims; G02 supports A and G03 supports B.
A completed exact violation must remain in deterministic stdout with its fired
gate and result; exit zero and empty stderr distinguish a completed scientific
audit from an integrity failure. Captured authenticated ZIP/format faults are
retained as qualification failures, not silently repaired or substituted.

Network/retrieval/hash/dependency failures and unexpected program or environment
errors exit nonzero. They provide no completed valid gate; POLICY's abandoned-pin
rule applies when required. No pinned source is patched to rescue such a run.
No threshold, carrier, prefix or scientific scope may move after the pin.

EXPECTED.txt is exact first-run stdout. RUN.md records pin, command, neutral
environment and byte hashes. RESULT.md records each claim and any fired
condition. Independent public aarch64/x86_64 replay must reproduce the same
bytes. Such replay audits the same archive, not independent experiments.

## 6. Layer and physical boundary

This is an L5 archive-to-record transformation. A packet's closure means that
the required next raw sync row has arrived. It does not establish physical
measurement completion, post-state saturation or COMM-SAT. The transducer's
software state is not an identified physical apparatus state or reset law.

No setting row is identified with a QDD target or a detector outcome. Missing
detector rows are not certified no-clicks, ZERO_SUPPORT, absent photons or a
source failure. The count does not supply coverage, efficiency, dead time,
prepare/reset, independent trials, a normalized probability kernel or a Born
occurrence law. No output feeds U. No L1-to-L5 or L5-to-L6 gate is passed.

`QDD-INSTRUMENT-APPARATUS` remains O / STOP. Both O2 children, Bell causal
accounting and photon obligations remain unchanged.
`COINCIDENCE-RECORD-FREQUENCY` remains candidate-H / UNTESTED / STOP outside the
registry. Public claims are unregistered and Canon v76 is unchanged.
