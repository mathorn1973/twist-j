# Decoder through an external apparatus and open measurement records

NON-CANONICAL. Definition and source-qualification proposal.
Public claims UNREGISTERED / CANON UNCHANGED. No experimental payload has
been downloaded, opened or analyzed for this proposal. No physical certificate
or formal probe result is issued.

Owner lane: [issue #834](https://github.com/mathorn1973/twist-j/issues/834),
under the physical apparatus obligations of
[issue #539](https://github.com/mathorn1973/twist-j/issues/539).
Authority checked against ACTIVE Public Canon v76 at public main
`50d11b2818883fd5f9a5178d56a5c12162a95cb3`.
The [source-candidate manifest](DECODER-OPEN-DATA-BRIDGE-1.sources.json)
records discovery evidence and outstanding admission fields. It is not an
accepted scientific input manifest.

## 1. The work that can proceed without a laboratory

The current resource constraint is publicly accessible experimental data only:
no new laboratory acquisition, hardware purchase or dependence on privately
supplied data. An existing experiment supplies an external apparatus instance.
Its documentation, archived calibration evidence and records can support a
bounded reconstruction of what that apparatus observed.

There are two distinct maps to build:

```text
archived bytes + apparatus metadata + calibration
    -- fixed observation adapter --> ordered observed records

U source + independently chosen physical dictionary + apparatus law
    -- physical prediction --> records of the same declared type.
```

The first map is implementable without deriving the second. Agreement can test
the second only after its source, context, parameters and observation map are
independently specified. Selecting a U head, detector law or interpretation to
encode already observed outcomes would create no predictive bridge.

This route does not substitute a Bell apparatus for the circuit in
[DECODER-PASSIVE-REALIZATION-BRIDGE-1](DECODER-PASSIVE-REALIZATION-BRIDGE-1.md).
That circuit remains an unbuilt realization proposal. External detector data
do not certify its matrix, energy normalization, buffer or preparation map.

## 2. Source choice made from documentation

The first qualification target is the **NIST 2015 Bell-test archive**, because
its documentation describes settings, detection and synchronization records
and preprocessing provenance. The official landing page supplies reuse terms;
it also identifies the archive as mutable and metadata as potentially
incomplete. Preserve its notice and attribution when reusing data or code.
[NIST repository and terms](https://www.nist.gov/pml/applied-physics-division/bell-test-research-software-and-data).

Its raw format is a sequence of channel, time and transfer-counter words.
Compressed and processed representations have different schemas. The `cw45`
files lack self-contained window metadata, and some spreadsheets have a known
zero-count caveat. These representations cannot silently replace original
records for this audit.
[Format documentation](https://www.nist.gov/document/bell-test-data-file-folder-descriptions).

The 2017 addendum released previously withheld runs after further analysis.
The word `blind` in a filename does not make our reanalysis blind.
[Addendum](https://s3.amazonaws.com/nist-belltestdata/belldata/File_Folder_Descriptions_Addendum_2017_02.pdf).

Object names must be preserved literally: the two stations' `nolightconeshift`
run names differ, and the raw-server listing itself includes some compressed
objects. Pairing runs or choosing a decoder from directory name alone is
inadmissible. No particular pair is admitted yet.
[Original-object catalogue](https://www.nist.gov/pml/applied-physics-division/bell-test-research-software-and-data/repository-bell-test-research-3).

Two secondary sources are listed, without opening their data. Hensen's 2016
second Bell experiment provides a compact versioned archive but needs its full
reuse terms and record semantics resolved. BrightEyes-TTM provides a distinct
time-tagging source candidate; it is relevant to instrument-record handling,
not an adopted Bell or QDD realization. Neither is a replacement selected
according to which outcome fits TWIST-J.

The choice above is a priority for **qualification**, not a selection of a
favorable scientific result. Published Bell conclusions and some aggregate
summaries were already encountered in discovery. This is retrospective work.
No unseen file is claimed statistically independent merely because this agent
has not opened it.

## 3. A proposed observation adapter with explicit domains

All identifiers in this section are local proposal identifiers. They create no
Canon definitions, cross-layer gates or physical effect identifiers.

`OD-CONTEXT` contains the source release, run/station identities, apparatus
configuration, channel dictionary, clock model, preparation and setting
semantics, record-coverage evidence, applicable calibration references and
the frozen selection rule. References distinguish an author's declaration,
an available calibration record, a measured bound and an assumption. A paper
description is not automatically an independently audited calibration.

`OD-RAW` is an immutable ordered byte source with object hashes and source
offsets. `OD-EVENT` retains station, channel, integer local timestamp, transfer
counter where present, original record index and raw-byte locator. Conversion
retains a dictionary of original codes. Unknown channels and ties remain
explicit; the importer must not sort away acquisition order or infer a global
event order from unaligned local clocks.

`OD-ATTEMPT` is proposed as:

```text
source_id, run_id, context_id, attempt_id,
local_sync_ids, local_windows, alignment_model_id,
settings_and_validity, all_detection_records,
coverage_status, selection_status, invalid_reasons,
calibration_ids, provenance_locators.
```

An attempt is defined by the documented trial clock, herald or other frozen
rule, not by the existence of a detection. A detection-only list cannot supply
its own missing trial denominator. A heralded source requires the documented
herald eligibility and its causal position; it is not interchangeable with
an unconditional pulse stream.

`OD-READOUT` is a tagged value:

```text
OBSERVED(pattern, multiplicities)
NO_DETECTION(valid_window, coverage_certificate)
INVALID(reason, retained_attempt)
UNRESOLVED(reason, retained_evidence)
```

No detection means an empty declared observation window **with adequate
coverage**, not zero source support or absence of a physical particle. An
unknown interval does not become a no-detection outcome. Invalid or missing
settings do not default to one setting. Multiple detections remain multiple
unless an independently justified, preregistered coarsening defines otherwise.
Instrument symbols such as click/no-click are not QDD LOW/HIGH labels.

The proposed maps have the following obligations:

| Map | Required behavior |
|---|---|
| `OD-PARSE: OD-RAW x OD-CONTEXT -> events or typed error` | Freeze per-object word widths, byte order, counter rules and archive/member identity. Byte errors stop the affected reconstruction. |
| `OD-SEGMENT: events x OD-CONTEXT -> attempts plus coverage gaps` | Use fixed timing and eligibility rules. Retain all constructed attempts and separately represent gaps whose trial count is not known. |
| `OD-OBSERVE: attempts -> readouts` | Preserve multiplicities, invalidity and provenance; resolve no-detection only with its coverage premise. |
| `OD-REDUCE: readouts -> declared summary` | Publish the denominator, retained and excluded categories and the exact coarsening. Do not infer a physical probability law from a normalized count. |

This is a specification; no source parser is implemented or executed here.
The conservation audit is at the level of record provenance: every imported
event must have a documented role or an explicit retained exclusion reason.
A record can support more than one derived field, so this is not a claim that
every byte maps bijectively to exactly one physical outcome.

## 4. Timing, selection and calibration are part of the measurement

Before any comparison, fix units, relative clock offsets and uncertainties,
window endpoints and tie rules, pulse/group indexing, station pairing,
multiple-hit policy, acquisition gaps, live intervals and run boundaries.
If timing must be estimated, predefine its algorithm and calibration-only
source segments. Preserve the estimate's uncertainty and correlations.
Do not maximize a coincidence count or model agreement on evaluation records.

Keep calibration, apparatus identification and evaluation roles distinct.
Shared references retain their covariance. Dataset partitions chosen after
looking at their outcomes do not become held-out evidence by renaming them.
Historical author choices remain historical choices in the exposure record.

The first empirical question should be narrow: **can the archived acquisition
be translated into complete, auditable attempts and observed outcomes under
its published apparatus contract?** A negative qualification can establish
missing evidence for this source; it does not falsify the physical experiment,
its published Bell result or TWIST-J.

Only a subsequent independently specified model comparison can test predicted
responses or occurrence laws. It must include detector inefficiency,
background, dead time, afterpulsing, timing uncertainty and memory wherever
relevant to the claim. If the archive cannot bound a needed nuisance parameter,
restrict the claim or leave it unresolved. Never fit an efficiency or threshold
on evaluation data solely to make the desired weights appear.

## 5. Pre-access custody and the formal pin

[POLICY](../POLICY.md) requires the accepted verifier and preregistration to be
public before formal gates. [AGENTS](../AGENTS.md) names opening formal data
before the pin as a stop condition. The procedure below distinguishes opaque
custody from semantic opening; it is not permission to explore results early.
The current note authorizes neither acquisition nor a scientific run.

1. Complete source qualification from catalogues, licenses, methods and schema
   documentation. Resolve run pairing, file inventory, variants and reuse
   obligations. Record prior exposure. Do not preview data archives or embedded
   outcome tables as if they were catalogue metadata.
2. Prefer a complete formal pin with externally supplied source hashes. If
   those are unavailable, first publish a separate **nonformal pre-access
   custody lock**: exact URLs/version and object IDs, available provider
   checksums, size bounds, allowed HTTP headers, transfer script, acquisition limits
   and no-substitution rule. This is not a `P-*` scientific pin.
3. Only under that custody lock, fetch opaque bytes into an untracked external
   store and compute SHA-256 and byte counts without parsing, previews,
   decompression or outcome inspection. Preserve the object identity and
   retrieval receipt. A provider MD5, ETag or filename is not a SHA-256. Missing
   strong provider identity must be recorded as weaker initial custody, not
   described as an immutable release. Unexpected identity/size aborts custody.
4. Create one new named public probe with all six preregistration fields,
   accepted exact verifier, completed custody manifest and an explicit replay
   path. Commit, push and read back the complete pin before the first semantic
   opening, including member inspection/decompression when needed. Do not edit
   a prior formal pin to insert the newly computed hash.
5. Execute only the pinned analysis and retain its complete result. Changes to
   the estimator, source set, window or threshold require their own disposition
   and new probe; a failed scientific result remains a result.

Large raw archives stay outside Git under a public manifest. The existing
5 MiB tracked-file limit and workflow rules are unchanged. The probe cannot be
declared ready until deterministic retrieval or another policy-compliant
replay path supplies every required input to both architecture jobs. A small
derived table may support a downstream calculation, but cannot substitute for
raw-record reproducibility of the adapter that produced it.

## 6. What each completed stage would earn

| Stage | Concrete deliverable | Supported conclusion |
|---|---|---|
| Source qualification | Complete version/license/inventory/schema/exposure map | This archive is admissible for the specified question. |
| Record reconstruction | Pinned parser, exact custody, attempt and exclusion audit | These archived bytes yield these declared observations. |
| Apparatus comparison | Independent calibration premises, fixed model and error/statistical rule | Agreement or rejection for this external apparatus and tested context. |
| Post-state/persistence | Sequential preparations and readouts with relevant controls | Only the post-state distinctions actually identified by those interventions. |
| TWIST-J prediction | Independently supplied U-to-physical-source/context dictionary and compatible apparatus law | A bounded empirical test of that candidate dictionary. |

An ordinary click archive does not identify an unobserved post-state, physical
reset or all future responses. A sequential dataset could constrain these
features if its interventions distinguish the competing models. With fixed
available data, restrict the proposed apparatus family to the distinctions
actually identifiable and leave other families open. Observational equivalence
on an archive is not equality of complete physical instruments.

For a Born comparison, state preparation and measurement calibration must
declare every external quantum assumption. If tomography or detector modeling
already assumes the Born rule, reusing it can test consistency under that
assumption but cannot independently derive the assumption. A single archive
does not identify a whole occurrence law without a fixed family and statistical
premises; stationarity, independence or a memory bound must be justified or
explicitly conditional.

The existing
[quadratic-partition result](../probes/P-DECODER-RESERVOIR-QUADRATIC-PARTITION-1/RESULT.md)
still obstructs the specified fixed nonnegative energy postprocessing into both
sharp QDD targets. Data reuse does not remove that mathematical boundary.
The [DQRC preregistration](../probes/P-DQRC-ARITHMETIC-RECONSTRUCTION-1/PREREG.md)
already lists the D0-D6 empirical-interface obligations; this proposal is a new
external-apparatus preparation lane, not a resumption of that probe.

`QDD-INSTRUMENT-APPARATUS` remains O and STOP. Its physical terminality and
whole-family completeness obligations remain open. `COINCIDENCE-RECORD-FREQUENCY`
remains candidate-H / UNTESTED / STOP outside the registry: laboratory
coincidence processing is not the Canon's simultaneous incidence population.
The photon gates and physical U/SI identification are unchanged.

The immediate next deliverable is a **NIST source qualification and custody
specification**, including exact object pairing, parser schema and a feasible
replay budget. It requires no laboratory. It precedes any empirical comparison
and is not a claim that a complete physical decoder has already been built.
