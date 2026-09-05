# NIST measurement contract 1

**NON-CANONICAL / CONDITIONAL CONTRACT / PHYSICAL STOP-DEFINITION.**
Public claims UNREGISTERED; Canon v76 and all existing claim scopes are unchanged.
Owner: [issue #839](https://github.com/mathorn1973/twist-j/issues/839), under
[#539](https://github.com/mathorn1973/twist-j/issues/539). Basis: public main
`11556f685f0c51c06fec6da32118a1d1e63d7fa4`. The companion
[JSON](NIST-MEASUREMENT-CONTRACT-1.json) owns stable local identifiers, dependencies,
field types, choices and decision rules. These are proposal identifiers, not new Canon gates.

## 1. What this contract defines

This contract gives a complete, deterministic specification of an **external
archival observation adapter**, followed by a total decision interface for
conditional physical interpretation. Missing physical evidence produces a typed
STOP retaining the observation. It does not produce an invented trial, no-click,
post-state, clock calibration or probability. A well-formed certificate is not
automatically accepted physical evidence.

The two interfaces are:

```text
authenticated source rows -> archival state machine -> LocalObservedInterval
LocalObservedInterval x pre-admitted evidence bundle
    -> CONDITIONAL_PHYSICAL_READOUT | INVALID_PHYSICAL_ATTEMPT | STOP_PHYSICAL
```

The [qualification result](../probes/P-NIST-RAW-RECORD-QUALIFICATION-1/RESULT.md)
has already established its two finite predicates under the declared codec.
The separate [adapter probe #838](https://github.com/mathorn1973/twist-j/issues/838)
now supplies the conditional kernel evidence recorded below in
[PR #841](https://github.com/mathorn1973/twist-j/pull/841). Its result is an external
dependency of this note; adoption through the complete NMC interface remains prospective.
That Python core defines rows, packets, a streaming machine, tuple-valued emissions
and `ValueError` validation. The Source/Context, `OK`/`STOP`, immutable transition
and history wrappers below are a semantic specification, not implemented API
claims about #838. Its Python machine named `LocalObservedInterval` is distinct
from this contract's enriched, immutable interval view of the same descriptive name.
There is no map here from a TWIST-J orbit to this apparatus. Its carrier is
`FOREIGN_NIST`, distinct from the chosen reservoir and U4 prototypes. `feeds_U=false`.

## 2. Source identity, existing evidence and exposure

The byte identities are inherited from
[SOURCE.json](../probes/P-NIST-RAW-RECORD-QUALIFICATION-1/SOURCE.json), SHA-256
`653e5dd17b041ecf38244bcd8312fa724863eb681f940795e38974182f7bbe8a`.
The qualification scientific pin is `dc8abb7e8e5ccaad4ff561776b747801a4d4a373`.
That manifest binds the four complete ZIP objects, their exact basenames and reuse notice.
SHA-256 identifies the acquired objects; it does not identify an immutable provider release.

| Source ID | Member basename | Qualified decoded extent | Closed intervals | Evidence status |
|---|---|---:|---:|---|
| alice-sync | 00_03_find_sync.T1.dat | 485503 rows, full member/CRC | 194914 | Existing finite result |
| bob-sync | 00_03_find_sync.T2.dat | 489229 rows, full member/CRC | 197214 | Existing finite result |
| alice-run3 | 00_44_CH_pockel_100kHz.run3.alice.dat | first 1048576 rows | 512047 | Existing finite result |
| bob-run3 | 00_43_CH_pockel_100kHz.run3.bob.dat | first 1048576 rows | 514203 | Existing finite result |

The run3 interval settings were exactly one-hot in that scope. Detector multiplicity
was retained: Alice had 488341 zero-row, 22960 one-row and 746 multiple-row intervals;
Bob had 494432, 19392 and 379. These are already known source-order observations.
Run3 tails and their full-member CRC remain outside those decoded claims.
Equal prefix lengths do not establish common physical time or paired trials.

Existing catalogue, source-code, publication and qualification exposure is disclosed.
This design is informed by the completed qualification and is not blind.
No experimental payload is opened for authoring this note, and no new outcome
statistic or scientific execution is performed. A successor uses its own public
preregistration/readback; this note does not authorize extra inspection.

### Existing adapter kernel evidence

The [commit-pinned adapter RESULT](https://github.com/mathorn1973/twist-j/blob/0630ab38a07ecb9d57d2097aa76ac26f00a5815e/probes/P-NIST-LOCAL-OBSERVED-INTERVAL-1/RESULT.md)
records **A CONFIRMED / B CONFIRMED**, with G01_SYNTHETIC_REFERENCE,
G02_ACTUAL_LOSSLESS, G03_ACTUAL_PREFIX_CHUNKING and G04_ACTUAL_DERIVED_REFERENCE
all PASS. Claim A uses G01/G02/G04; claim B uses G01/G03/G04. The source pin is
`0ddc026fa5f2eefcfbc122d38585f475bd6418cc`; the original result commit is
`f37cb6b803ccab9c8adb4c7f310f7392cfe6494c`, and the architecture-evidence commit is
`0630ab38a07ecb9d57d2097aa76ac26f00a5815e`. All six new source files remain byte
identical to that source pin. The [pinned RUN inventory](https://github.com/mathorn1973/twist-j/blob/0630ab38a07ecb9d57d2097aa76ac26f00a5815e/probes/P-NIST-LOCAL-OBSERVED-INTERVAL-1/RUN.md)
records the first x86_64 Linux execution, exit zero, empty stderr and exact stdout:
58096 bytes, SHA-256 `c10825ec57fd5672e7a05d9caba1d1946cbea420d9cbf10968b596c7cb847836`.
Independent public aarch64/x86_64 cold replay is **PASS** in
[workflow 33962156745](https://github.com/mathorn1973/twist-j/actions/runs/33962156745)
on the original result commit: [aarch64 job 101295794608](https://github.com/mathorn1973/twist-j/actions/runs/33962156745/job/101295794608)
and [x86_64 job 101295794350](https://github.com/mathorn1973/twist-j/actions/runs/33962156745/job/101295794350)
reported identical verifier and stdout hashes. The evidence commit records those
receipts; it is not the commit on which that workflow ran.

This evidence tests one pinned Python kernel on the same four nominated member
portions and the frozen finite synthetic fixtures. It supports lossless row
ownership, derived references, causal packet emission and the specified prefix/chunk
checks. The separate general induction proof concerns the defined mathematical
state relation; finite testing does not prove all Python executions. This is
known, exposed archive evidence, not a blind or independent experiment.

`NMC1-G-ADAPTER` therefore has **CONDITIONAL_EXACT_KERNEL_PASS / WRAPPER_STOP**:
the complete NMC Source/Context, OK/STOP, history, persistence and physical-decision
wrappers are **NOT_IMPLEMENTED / UNTESTED**. Their prospective composition with
this kernel has not passed an implementation gate. No physical certificate is
added; the physical bundle remains EMPTY and physical interpretation remains STOP.

## 3. Primary evidence and adopted choices

| ID | Evidence or choice | Exact use and limit |
|---|---|---|
| E-FORMAT | [NIST format documentation](https://www.nist.gov/document/bell-test-data-file-folder-descriptions), 2015-12-23, pp.1-4 | Three uint64 words; tick 625/8 ps; stored channels 0/2/4/5/6. This supplies a documented nominal dictionary. |
| E-CLOCK | Same document, p.1 | Shared 10 MHz reference, different origins; PPS jitter about 10 ns and possible 100 ns jumps. These approximate statements are not hard uncertainty bounds. |
| E-STROBE | Same document, p.1 | Sync follows QRNG sampling through 18 feet of coax. Cable length alone supplies no propagation-delay value. |
| E-WINDOW | Same document, pp.3-4 | Processed format has 16 pulse slots. Window delays/radii and initial alignment skips reside in processing metadata; cw45 alone is insufficient. |
| E-RUN3 | Same document, p.2 | Run3 delay correction was unsuccessful. Qualification does not remove this warning. |
| E-PROCESS | [NIST processing description](https://s3.amazonaws.com/nist-belltestdata/belldata/code/analysis/DataProcessingDescription.pdf), 2015-12-23 | Historical analysis starts at a sync after a common PPS, retains the first bad sync, and maps simultaneous settings to zero. Those analysis choices are not adopted here. |
| E-DAQ | [NIST acquisition source archive](https://s3.amazonaws.com/nist-belltestdata/belldata/code/daq/bell_server.zip), hashes in JSON | Native NumPy words; channel 64 is calendar metadata. Transfer IDs count nonempty writes; no complete loss ledger follows. Source version identity for the run is unproved. |
| C-CODEC | Accepted explicit choice, inherited qualification | Little-endian `<QQQ`; never infer another decoder by choosing favorable outcomes. |
| C-PARTITION | Accepted explicit choice | Original row order and consecutive recorded sync anchors; no clock sorting or detector-based selection. |
| C-POINTER | Accepted explicit choice | Retain every detector/setting row and multiplicity. No binary detector coarsening. |
| C-WINDOW | Accepted explicit choice | No numerical physical window is supplied by this contract. Conditional windows must be evidence-bound finite disjoint half-open intervals. |

The inherited NIST notice accompanies reuse. No source archive or external code
is copied into these artifacts. The documentation describes possible metadata
in processed files; no such file or its alleged calibration is admitted by a mention.
Likewise, the separate 00_03 objects do not certify a run3 clock map.

## 4. Exact archival carriers and equalities

All integers below are mathematical integers. `u64` means `0 <= x < 2^64`.
`stream_id=(source_manifest_sha256, object_id)` and `RowRef=(stream_id,index)`.
The pinned adapter kernel uses a wire `stream_id` string equal to
`object_id`. `NMC1-WIRE-IDENTITY` explicitly maps that string, under the fixed
inherited SOURCE hash, to this semantic pair, and inversely projects the object
ID after checking the same hash. It is a bijection on the four admitted IDs,
not literal equality of the two types. Packet conversion preserves every row,
borrowed reference and emission index; a wrong hash/unknown ID returns STOP_INPUT.
A row reference resolves to the immutable named member at uncompressed byte
offset `24*index`, length 24, under the bound archive hash. It is not a
compressed-file offset or an independent physical event identifier.

```text
RawRow(index: nonnegative integer, channel:u64, word2:u64, transfer:u64)
Packet(stream_id, kind, owned_rows:tuple[RawRow],
       right_sync_reference: RawRow | NONE, emitted_at: integer | NONE)
kind = PREFIX | CLOSED_INTERVAL | PENDING_SUFFIX | UNANCHORED
Source = (stream_id, archive_hash, member_basename, codec, nominated_extent)
Context = (profile_version, Source, record_rules, certificate_bundle_id)
Ready = (Source, Context, cursor=0, pending=(), emitted=())
ArchiveState = (Source, Context, next_index, phase, pending, emitted_packets)
phase = UNANCHORED | ANCHORED
History = (emitted_packets, current_nonemitting_snapshot)
RecordDelta = (before_state, accepted_row, emitted_packet | NO_EMISSION, after_state)
```

`right_sync_reference` is a borrowed complete row value identified by the packet's
stream and that row's index. It never owns that row. `emitted_at` is a source
record index, not physical occurrence time. The JSON spelling of `NONE` is null.
Source, context, ready, state, row, packet, delta and history equalities are
componentwise exact equality of their respective complete fields; order matters.
No equality quotients out signs, phases, timestamps, source identity or provenance.

`SupportedSource` is exactly one of the four inherited manifest objects with the
specified codec/extent and successful integrity checks. It is not selected by
click presence. The abstract row-state machine also has an explicitly separate
finite-row test domain, including empty input and anomalous codes; those tests
cannot enlarge the empirical source claim.

## 5. Total state machine and row ownership

`prepare(Source,Context)` checks literal source/context agreement and returns Ready.
All operations return `OK(value)` or `STOP_INPUT(sorted_reason_ids, unchanged_state,
retained_input)` on ill-typed, mismatched or out-of-order requests. No repair occurs.
These envelopes belong to the specified NMC wrapper. A Python implementation must
validate Source/Context and translate core results or exceptions explicitly; #838
does not itself implement these envelopes, stored emitted history or RecordDelta.
The unchanged-state promise is for one rejected semantic operation. It does not
claim rollback of earlier rows accepted by a Python `feed_many` invocation.
A valid `step` consumes exactly the next row `r` with `r.index=next_index`
within the nominated extent. Prefix consistency is restricted to that same
source/context and extent; it does not authorize reading an extra raw row.
Unknown channel codes remain raw rows; they are flagged in derived views.

```text
If r.channel != 6:
    pending' = pending ++ (r); emit NO_EMISSION.
If r.channel == 6 and phase == UNANCHORED:
    if pending is nonempty, emit Packet(PREFIX, pending, borrowed r,
                                        emitted_at=r.index);
    otherwise emit NO_EMISSION;
    pending'=(r); phase'=ANCHORED.
If r.channel == 6 and phase == ANCHORED:
    emit Packet(CLOSED_INTERVAL, pending, borrowed r, emitted_at=r.index);
    pending'=(r).
In every accepted step: next_index'=next_index+1.
Emitted packets are appended once, in that same step.
```

A PREFIX packet is emitted at the first sync only when its owned tuple is nonempty.
Empty emitted packets are excluded; a first-row sync is retained as the pending anchor.
For sync indices `j_0<...<j_(K-1)`, CLOSED_INTERVAL packet k owns exactly
`r[j_k:j_(k+1)]`: the left sync and all strict interior rows. Its right boundary
`r[j_(k+1)]` is only a reference and becomes the next pending left anchor.
The prefix owns `r[0:j_0]`. No boundary is silently dropped or owned twice.

`finish/passive_read` returns a nonemitting snapshot: PENDING_SUFFIX owns the
pending last anchor and tail if anchored; otherwise UNANCHORED owns all rows,
including the empty tuple for empty input. Both snapshots have `emitted_at=NONE`
and `right_sync_reference=NONE`. They are not appended as events. A snapshot
is replaced when the inspected prefix extends; already emitted packets do not change.

Concatenating the owned rows of emitted packets and the current snapshot
reconstructs exactly `r[0:n]`. For prefixes of lengths n<=m, emitted(n) is a
prefix of emitted(m). A closed packet is emitted only upon consuming its right
boundary, so its content needs no future row. These identities follow by
induction over the three update cases; the implementation audit belongs to #838.

`emit(delta)` returns its already determined packet or NO_EMISSION without another
append. `append` validates the before-history and expected unique next packet;
duplicate/out-of-sequence appends STOP_INPUT. `persist(after,packet,delta)` verifies
the complete delta and returns exactly after, never replays a transition.
`passive_read` changes no cursor, state or history. `archival_complete(packet)`
means an emitted PREFIX/CLOSED_INTERVAL frame is fixed, not physical terminality.
An empty source prefix yields an empty UNANCHORED snapshot, not physical zero support.

Replay from cursor zero is a new invocation of prepare retaining the prior history.
Physical reset, preparation, ready-state selection and terminality have no archive
implementation. `physical_reset` returns STOP_PHYSICAL and leaves the archived state
unchanged. This tagged reset is **not** the #539 reset signature, whose codomain
has no rejection tag: a separately reviewed adapter/amendment is required.
This external L5 contract does not claim #539 L4-to-L5 conformance or READY-DEFINITION.

## 6. Derived local observed interval and outcome

`NMC1-LOCAL-OBSERVED-INTERVAL` is the deterministic view of a CLOSED_INTERVAL packet:
source/context and packet identity; left/right row references and their raw timetags;
the entire raw interior; ordered setting/detector/PPS/calendar/other references;
transfer references; setting and detector tags; diagnostics; and provenance.
No derived view acquires ownership of another raw row.
`NMC1-VIEW(packet,context)` checks the context's Source against the packet through
the explicit wire-identity adapter before constructing this view. The semantic
view is not the mutable Python streaming machine named `LocalObservedInterval`;
the latter's state and tuple outputs require the separately specified wrapper.

For counts n2,n4 over strict interior rows, the setting tag is
ONEHOT_0 for (1,0), ONEHOT_1 for (0,1), MISSING for (0,0),
REPEATED_0 for (n2>1,0), REPEATED_1 for (0,n4>1), and BOTH otherwise.
Exactly one setting row permits a unique observed setting timestamp; otherwise
its value is `MISSING` or `AMBIGUOUS`, with all supporting rows retained.
No setting is physically attributed to a pulse merely by this count.

The detector tag is NO_RECORDED_DETECTOR_ROW, SINGLE_RECORDED_DETECTOR_ROW,
or MULTIPLE_RECORDED_DETECTOR_ROWS according to the number of channel-0 interior rows.
Each detector row retains `word2-left_sync.word2` and, only for a unique setting
row, `word2-setting.word2`. These signed integer differences are descriptors,
not acceptance windows, time-of-flight measurements or occurrence probabilities.
Channel 64 is never included in timetag differences.

Unknown codes, invalid calendar fields, nonpositive boundary differences and
other timing anomalies remain explicit diagnostic reasons with raw references.
The observation can still be reconstructed. They do not silently become a
physical INVALID trial unless the separately admitted trial contract says so.
PREFIX, PENDING_SUFFIX and UNANCHORED have no fabricated complete-interval readout.

## 7. Conditional physical interpretation with a complete STOP path

A certificate bundle is a finite, ordered set of immutable evidence records.
Each record owns an ID, bytes/hash or immutable source locator, issuer/procedure,
same-run object/station scope, quantity, units, calibration inputs, uncertainty
set and correlations, validity interval, exposure/selection rule, and an external
admission receipt. Numerical endpoints are rational with explicit units.
Missing, contradictory, out-of-scope or merely self-declared certificates do not pass.
Admitted assumptions are listed separately from measured bounds. The empty
bundle is the current bundle; its physical decisions always STOP_PHYSICAL.

`physical_interpret(interval_view,bundle)` takes a valid
`NMC1-LOCAL-OBSERVED-INTERVAL`. Every physical decision retains that complete view,
its Source, Context and owning packet; the bundle identity must equal the identity
bound by Context. A malformed view/request returns STOP_INPUT retaining the input,
without inventing a Source or Context. On a valid view it performs these finite checks:

1. Validate Source/Context/packet identity, complete interval, row references and
   evidence receipts. Unsupported physical premises return STOP_PHYSICAL with the
   unchanged interval view, Source, Context, packet and reasons.
2. Require a same-run trial/eligibility certificate assigning the sync and setting
   references to one physical trial and explaining the physical preparation/pulse
   convention. Invalid eligibility returns INVALID_PHYSICAL_ATTEMPT, retained in
   the denominator audit; ambiguity returns STOP_PHYSICAL.
3. Require clock/setting/window/pointer and recording-coverage certificates applicable
   to that trial. In particular, prove candidate completeness: every relevant
   registration for each physical window lies in this packet's owned strict interior
   and the pinned inspected extent, under the admitted uncertainty, record-order and
   registration-latency bounds. Otherwise STOP_PHYSICAL; no adjacent packet is
   implicitly consulted. Only then classify the supplied rows as below. Never
   optimize a window or discard an ambiguous row.
4. Any unresolved required classification, activity state or gap returns STOP_PHYSICAL.
   A documented invalid apparatus condition returns INVALID_PHYSICAL_ATTEMPT.
5. Otherwise return CONDITIONAL_PHYSICAL_READOUT with all certificate IDs, assumptions,
   trial/setting label, definite-in detections and multiplicity, retained definite-out
   rows with reasons, and the complete original view, Source, Context and packet.
   Zero in-window registered
   detections gives NO_DETECTION_WITH_COVERAGE; one gives SINGLE_REGISTRATION;
   more gives MULTIPLE_REGISTRATIONS. These are registration outcomes, not photon
   number, QDD LOW/HIGH, source vacuum or quantum post-state.

Distinct STOP reasons accumulate in sorted ID order; a missing premise never defaults
to a favorable value. A STOP/INVALID is retained, not removed from a tally. This
conditional readout does not supply a complete physical instrument/post-state.

### Clock, pairing and window choice

The admitted clock family is affine on each independently certified validity segment:
`T_s(q)=a_s*q+b_s`, with `a_s>0`. Its parameters and shared-reference correlations
belong to a nonempty bounded rational polytope supplied by the certificate.
No offset, slope, segment boundary or hard uncertainty bound is fitted to setting
or detector outcomes. The documented common reference motivates this family;
its validity on run3 still needs evidence. Known clock faults STOP the affected
scope rather than trigger a search for a better mapping.

A same-run PPS-association certificate must identify which recorded PPS/metadata
references denote the same physical second, with latency/jitter and possible-jump
dispositions. Calendar-64 values alone and the separate 00_03 files cannot provide
that certificate. Only after it passes may the documented first-sync-after-common-PPS
convention be adopted with explicit pulse indexing and uniqueness evidence.
Cross-station pairing uses unique certified physical trial labels on the common
validity domain. It preserves every unmatched/ambiguous local packet; no nearest-click
or favorable-coincidence matching is permitted.

Window certificates provide finite disjoint half-open pulse windows `[L_j,U_j)`
relative to the certified trial reference, their pulse/group indexing, setting
association, units and endpoint convention. In the fixed-endpoint branch, each
`L_j,U_j` is an exact, fixed rational value with `L_j<U_j`. No run3 numerical endpoints, 16-slot
index conversion, coax velocity factor or nominal-100-kHz equality is assumed here.
Multiple accepted pulse slots remain separately referenced and may be grouped only
by a predeclared union preserving raw multiplicity.

For a row's possible relative times `[A,B]` obtained by exact extrema over the
certificate's uncertainty polytope, membership in `[L,U)` is definite-in when
`A>=L and B<U`, definite-out when `B<L or A>=U`, and ambiguous otherwise.
These formulas apply only to fixed exact `L,U`. If endpoints are uncertain, the
allowed extension supplies affine `t(theta), L(theta), U(theta)` on the same
nonempty bounded rational polytope P, including their joint correlations, and
certifies ordered disjoint windows throughout P. Set `dL=t-L`, `dU=t-U` and use
joint extrema: definite-in iff `min_P dL>=0 and max_P dU<0`; definite-out iff
`max_P dL<0 or min_P dU>=0`; otherwise ambiguous. Unsupported endpoint dependence
or missing joint bounds returns STOP_PHYSICAL. Separate marginal endpoint ranges
are not substituted for these correlated differences.
Test each disjoint slot; ambiguous slot/group attribution STOPs that claimed
classification. This conservative rule is a chosen decision procedure, not an
inferred physical tolerance. Nonempty polytope and extrema are finite rational
linear-feasibility/optimization obligations; a missing bound is not infinity by default.

### Coverage, loss, multiple pulses and dead time

Recording coverage requires independently supported acquisition/live boundaries,
buffer-loss and gap disposition, channel registration semantics, and applicability
through every declared observation window. It also requires a candidate-completeness
certificate connecting physical times, possible registration latency, record order
and the submitted packet's interior. Precisely, for every admitted parameter
`theta` and each declared window `W_j(theta)`, let `Reg(W_j,theta)` denote all
relevant recorded registrations attributed to that window under the certified
registration model. The certificate must establish

```text
Reg(W_j,theta) subseteq
    { RowRef(Source.stream_id,i) : j_left < i < j_right and 0 <= i < N_pinned }.
```

Every reference on the right must resolve inside the submitted packet's owned
interior. Together with the recording/loss certificate, this rules out unaccounted
relevant registrations outside the candidate set. It is required for zero, single
and multiple registration results alike; a closed archival packet alone proves
none of this physical containment. A borrowed right sync does not supply adjacent
interior rows. Possible outside-window ownership, incomplete latency/order bounds,
or a window extending beyond the inspected extent returns STOP_PHYSICAL. A broader
multi-packet collector would require a separately specified ownership/coverage
contract and inspection scope; this contract never searches neighboring packets.

Consecutive transfer IDs or a narrow
observed sync-spacing histogram do not certify it. An unknown number of missing
trials is represented as a gap with UNKNOWN count, not zero attempts.

Dead time, recovery, saturation, afterpulsing, dark/background events and multi-pulse
emission are not inferred absent. A supplied activity model may classify a window
as active, known-inactive/invalid, or unresolved; the latter two remain visible.
NO_DETECTION_WITH_COVERAGE means no registered event under that specified apparatus
condition. It does not require ideal efficiency and does not assert no incoming
photon. Efficiency/background bounds and a response/memory model become mandatory
for any quantitative source-to-outcome or Born comparison, beyond this limited
registration statement. No multiple-hit rule selects a first click or invents
an exclusive two-valued outcome in the present contract.

## 8. Readiness gates, physical family and Born boundary

| Gate ID | Premise / owner | Present status | Evidence or decision |
|---|---|---|---|
| NMC1-G-ARCHIVE | Source identity and inherited prefix codec | EXISTING_FINITE_RESULT | Qualification RESULT/SOURCE; four fixed objects only |
| NMC1-G-ADAPTER | Exact archival kernel; prospective NMC wrapper composition | CONDITIONAL_EXACT_KERNEL_PASS / WRAPPER_STOP | Commit-pinned #838 RESULT: A/B CONFIRMED, 4 gates PASS; aarch64/x86_64 replay PASS; NMC wrappers NOT_IMPLEMENTED / UNTESTED |
| NMC1-G-TRIAL | Same-run trial/setting/preparation attribution | UNRESOLVED | No admitted physical trial certificate |
| NMC1-G-CLOCK | Same-run clock, PPS association and unique pairing | UNRESOLVED | E-CLOCK/E-PROCESS are narrative evidence, not run3 certificates |
| NMC1-G-WINDOW | Pulse indexing, delays, windows and uncertainty | UNRESOLVED | E-STROBE/E-WINDOW; no numerical certificate admitted |
| NMC1-G-COVERAGE | Recording/live coverage, loss/gap disposition, registration latency/order and complete window candidates inside the owned interior and pinned extent | UNRESOLVED | E-DAQ provides neither a complete loss ledger nor the required containment certificate |
| NMC1-G-POINTER | Registration meaning, activity and multiplicity | UNRESOLVED | Observed tags defined; physical evidence required |
| NMC1-G-INSTRUMENT | Physical ready/post-state/memory/persistence/reset | UNRESOLVED | Archive replay is not apparatus dynamics |
| NMC1-G-RESPONSE | Efficiency/background/recovery/memory response law | UNRESOLVED | Required for source-dependent predictions |
| NMC1-G-SOURCE | Independently selected U-to-physical source/context dictionary | UNRESOLVED | No such map or U4/reservoir identity adopted |
| NMC1-G-OCCURRENCE | Law on complete preparations and realized outcomes | UNRESOLVED | No measure, ensemble or selection law inferred |
| NMC1-G-BORN | Independent state/effect identification and declared statistical test | UNRESOLVED | No physical Born derivation or comparison executed |

These local gates are bookkeeping identifiers. They are not registered scientific
gates or substitute authority for their owners. All are non-writing decisions.

The archival family consists of the four fixed sources under this one observation
algorithm, indexed by explicit certificate bundles. Its equality is exact source,
context, packet and history equality. Different certified physical contexts remain
different contexts. Equality of observed finite archives does not imply equality
of all admissible instruments, post-states, effects or future laws. No exhaustive
classification of physical alternatives is asserted.

An optional quantum benchmark must separately supply its state/preparation map,
effects or complete instrument, loss/no-registration/multiple-registration alphabet,
memory assumptions, calibration exposure and finite statistical decision rule.
If it uses `p(y|rho,c)=tr(rho E_(c,y))`, Born is **an explicit benchmark assumption**.
Tomography/efficiency inference that uses this equation must be listed as Born-dependent;
it cannot then serve as an independent derivation. No such quantum-calibration source
is admitted here. E-FORMAT, E-PROCESS and E-DAQ are used only for record/timing
documentation, not quantum state or probability identification; the published Bell
result is not reused as a Born premise.

For an occurrence claim one must independently fix the preparation/context/ready-state
schedule and either its measure, an ordered deterministic frequency theorem, or an
explicit occurrence postulate. A finite census and one-hot settings supply none
of these. Counts do not acquire an L6 meaning by normalization. The existing
reservoir postprocessing obstruction and QDD/physical owners remain unchanged.

## 9. Field ownership and implementation boundary

The JSON carrier registry owns every stored field; derived local views cite their
owning packet and raw references. Source identity owns byte/row coordinates;
Context owns all admitted choices and certificate references; ArchiveState owns
the cursor, pending tuple and emitted history; Packet owns only `owned_rows`;
RecordDelta owns the complete transition witness. Certificates own physical
quantities, uncertainty and scope; no derived count owns them by inference.
PhysicalDecision retains the complete submitted semantic interval view, Source,
Context and packet on every physical branch. These are specified wrapper fields,
not additional fields already implemented in the #838 Packet or Python machine.

Every public map has an explicit input-validation STOP branch. No mutation, network
retrieval or new scientific execution is authorized by evaluating this document.
No reset, zero, support, terminal, post-state or probability slot is silently filled
by the archival machine. A later physical implementation must publish the needed
evidence and any #539 schema amendment separately. This contract makes those
conditional decisions precise without claiming that the physical decoder is complete.
