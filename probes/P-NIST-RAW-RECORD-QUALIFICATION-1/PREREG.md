# P-NIST-RAW-RECORD-QUALIFICATION-1 preregistration

FROZEN TARGET / NO SEMANTIC DATA OPENING AT PIN / PUBLIC STATUS NONE.
Retrospective external-data qualification. Published summaries and apparatus
documentation are known; no blind or independent-new-experiment claim.

```text
owner: A. M. Thorn
issue: https://github.com/mathorn1973/twist-j/issues/836
branch: probe/P-NIST-RAW-RECORD-QUALIFICATION-1
base: af2240d0a2c4807fc6a01c0c5c3132a22ace6015
authority: ACTIVE Public Canon v76
action layer: L5, archived observation stream only
claim_A: NIST-RAW-PREFIX-CODEC-QUALIFICATION
claim_B: NIST-RUN3-RECORD-INTERVAL-ONEHOT
formal runs at pin: 0
semantic openings of experimental payloads at pin: 0
public status: NONE
```

## 1. Equation and targets

For each named compressed archive, verify its complete byte count and SHA-256
before reading ZIP metadata or decompressing. Select the unique member with
the literal expected basename in SOURCE.json. Interpret the first
`min(1048576, member_size/24)` complete rows using **little-endian `<QQQ`**.
This codec is an explicit hypothesis motivated by published Windows/native
NumPy acquisition code, not a certified exact acquisition-version identity.
Never try another byte order or source after seeing the output.

Rows have original zero-based indices and three unsigned integer words.
Codes 0,2,4,5,6 are the documented detection, setting-0, setting-1, PPS and
sync channels. Code 64 is calendar metadata of the documented logger variant;
its second word is a 14-digit Gregorian calendar value, not a timetag or an
independently calibrated UTC clock. Other codes remain visible as violations
of this candidate dictionary. The nominal tick `625/8 ps` is an external
documented scale, not a new metrological certificate or TWIST-J SI bridge.

Claim A is the conjunction, on all four selected prefixes:

- admissible archive/member structure under the frozen limits;
- member size divisible by 24, complete reading of the nominated prefix;
- all decoded channel codes belong to `{0,2,4,5,6,64}`;
- every calendar-64 field has the frozen Gregorian format.

Exact row-accounting for the decomposition below is an implementation
invariant checked on every run. An internal bookkeeping failure invalidates
the execution; it is not an empirical counterexample to A.

This is a finite data-qualification claim conditional on the explicit codec.
It does not assert ordered timetags, absence of loss, correct experiment timing,
complete physical coverage or semantic correctness of every channel label.

Let `j_0<...<j_(K-1)` be original row indices with channel 6. Closed
**record-order intervals** are

```text
I_k = {i : j_k < i < j_(k+1)},        0 <= k < K-1.
N = prefix_rows + K + sum_k |I_k| + suffix_rows.
```

Prefix and suffix rows remain visible; with no sync all rows form an unanchored
fragment. Metadata rows participate in bookkeeping. No sorting, station-clock
alignment, coincidence-window search or deletion is performed. An interval is
not automatically a physical trial. For each interval count every setting-0,
setting-1 and detector row as `(n_2,n_4,n_0)`.

Claim B concerns only the two RUN objects: each has at least one closed
interval, and every such interval has `(n_2,n_4)` equal to `(1,0)` or `(0,1)`.
No settings, repeated settings and both settings are separately retained.
The threshold is **zero exceptional closed intervals**. This tests one exact
necessary syntactic condition for a naive binary reading of these intervals;
even success would not establish their physical trial semantics.

`n_0=0` is labeled `NO_RECORDED_DETECTOR_ROW`, never certified no-click, absence
of a photon, QDD ZERO_SUPPORT or source failure. Detections outside a historical
Bell window are not removed. No expected Born, CHSH or Bell statistic is tested.

## 2. Accepted code and immutable dependencies

The sole executable scientific source is `verify.py`. Its complete bytes and
this preregistration are publicly committed before first execution. Its
literal `MANIFEST_SHA256` binds SOURCE.json; that manifest binds the four opaque
archives and the inherited NIST source-notice note. No third-party code is
imported, executed or copied into this probe.

The source manifest records the separate nonformal custody commit
`92433f0f77a954e4c210255ecbdb6a41d99a5f39`. Only opaque download, size and SHA-256
computation occurred under that custody lock. No archive preview, member
inspection, decompression, parsing or outcome extraction preceded this final
analytical pin. The earlier preparation commit was not used for acquisition.

Use exactly:

```text
python3 probes/P-NIST-RAW-RECORD-QUALIFICATION-1/verify.py
```

The standard-library verifier uses a temporary directory outside the checkout
for cold retrieval and refuses redirects. The optional
`TWISTJ_NIST_CACHE_DIR` is a performance hint only: `<id>.zip` files are checked
against the same complete size/SHA-256 before any semantic access. It changes
neither source selection nor stdout. Cold retrieval must work in unchanged
GitHub architecture jobs within the existing 600-second verifier limit.
Source notice accompanies copied archives. No raw archive is tracked in Git.

## 3. Carrier and selected data

SOURCE.json names exactly four original-server objects: Alice and Bob run3,
and their separate 00_03 synchronization archives. Literal local-start-time
filenames differ across run3 stations and are preserved. No physical-time
pairing between their rows is asserted. In particular, the 00_03 files do not
certify an unchanged offset for run3.

The source was chosen from catalogue/documentation before payload inspection:
run3 is an early, finite named acquisition useful for a record audit, with an
already documented unsuccessful experimental delay correction. That warning
does not imply corrupt bytes or invalidate other runs. These records are not
a newly selected experiment for a physics significance claim.

The prefix bound is fixed before inspection for reproducible resource use:
at most 4194304 decoded rows across the four objects. Each complete compressed
archive is hashed, but an uninspected member tail is not claimed decoded or
CRC-verified. Output distinguishes a complete member from a truncated prefix.
No property is extended from the prefix to its unread tail.

Archive admissibility requires at most 100 ZIP entries and a unique,
unencrypted nominated member of at most 16 GiB, using STORED or DEFLATED
compression. Other compression methods and malformed ZIP structure, names,
or compressed-prefix content are explicit qualification failures. No member
is extracted by its archive pathname.
The entry-count condition is an acceptance limit checked after Python reads
the ZIP central directory; it is not a preallocation memory bound.

## 4. Systematics, diagnostics and prior exposure

The verifier reports calendar rows separately from timetag comparisons.
Documented acquisition code may use GPS-derived calendar values or computer
UTC; the field is not an independent event clock. Physical-channel timestamp
differences, ties/reversals and transfer-counter differences are diagnostics,
not zero-tolerance claims A or B. A counter jump is not automatically data loss;
absence of gaps is not proof of complete acquisition coverage.

For record-order sync intervals, retain settings multiplicity and timing
diagnostics in the frozen code. Histograms have exact integer counts and
deterministic summaries; hashes of complete canonical histogram encodings
make omitted display bins reproducible. Witness lists have a fixed finite cap
and preserve original row indices. They do not select favorable events.
The channel list prints only the six allowed codes that occur. A complete
channel-histogram digest, support/count/range, top eight bins and the total
unknown count retain a bounded diagnostic even if the codec is incompatible.

No efficiency, dead time, afterpulsing, uncertainty, independence, stationarity,
source distribution or detector model is inferred from a zero count. Such
physical conclusions need separately supplied calibration and apparatus laws.
Archived time tags are external L5 observation records, not a derived L1-to-L5
TWIST-J stream. No layer lift or L6 measure is adopted.

Known exposure consists of catalogue identities and sizes, documented channel
formats and acquisition source, published processing caveats and published
Bell summaries. Raw files and calibration payloads were not semantically
opened before the final pin. This does not retroactively make the historical
dataset or its design choices blind or independent of published results.

## 5. Failure thresholds and disposition

Claim A returns `QUALIFIED` only if every conjunct in Section 1 holds for all
four nominated prefixes. Any listed structural/data counterexample returns
`QUALIFICATION_FAILED` with a deterministic reason or witness. Such a completed
qualification is a scientific data result: exit zero, empty stderr, retained
EXPECTED.txt and a result disposition; it is not discarded as an abandoned pin.

For parsed RUN prefixes, B returns `ONEHOT` exactly under its Section 1
predicate and `NOT_ONEHOT` otherwise. When a RUN prefix cannot be parsed,
B is `NOT_EVALUATED`; a parser failure is not fabricated as a onehot
counterexample. The exact implemented distinction is part of the frozen code.

No rejection limit is chosen from the later census. Structural archive faults
captured by the verifier are data failures. Retrieval failure, size/SHA
mismatch, a changed dependency, environment failure or unexpected program
error is an integrity failure with no completed valid gate. Apply POLICY's
abandoned-pin rule when required; never repair and rerun the same formal pin.

Agreement across architectures reproduces the integer audit. It does not
make four archived inputs independent physical replications or earn a physical
T result. The conservative result remains an unregistered external-data
qualification; any later Canon treatment is a separate reviewed fold.

## 6. Action layer and exclusions

Action is confined to L5 archived record reconstruction. Integer arithmetic
implements the audit; it does not supply a physical decoder or a sampling law.
The chosen experimental apparatus is not the PR #833 U4 circuit and is not
identified with a TWIST-J U source. No QDD effect, instrument, post-state,
physical reset, complete family, photon identification, Born occurrence,
Bell causal explanation or SI calibration is established.

`QDD-INSTRUMENT-APPARATUS` remains O and STOP.
`COINCIDENCE-RECORD-FREQUENCY` remains candidate-H / UNTESTED / STOP outside
the registry. This probe does not resume or modify any earlier probe.

## 7. Primary documentation

- [Original data catalogue](https://www.nist.gov/pml/applied-physics-division/bell-test-research-software-and-data/repository-bell-test-research-3).
- [Format and acquisition caveats](https://www.nist.gov/document/bell-test-data-file-folder-descriptions).
- [Processing description](https://s3.amazonaws.com/nist-belltestdata/belldata/code/analysis/DataProcessingDescription.pdf).
- [DAQ code archive, read only as documentation](https://s3.amazonaws.com/nist-belltestdata/belldata/code/daq/bell_server.zip): 17507 bytes, SHA-256 `858c7bfdb2eaabdb4dec5ecd12a7f974428d5fe2c846634a4e1ff52b36c348c7`; member `bell_server/ttag_stream.py`, 5097 bytes, SHA-256 `f4458333fc010f71d991f524f9c384971bd5c1a2deb59c9337c561acce149ce5`.
- [NIST source notice](../../notes/NIST-RAW-CUSTODY-1.md).
