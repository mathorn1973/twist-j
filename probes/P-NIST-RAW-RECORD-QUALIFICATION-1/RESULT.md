# NIST archived record qualification: result

Status: **CONFIRMED**, two conditional claims about specified archived records.

**PUBLIC CLAIMS UNREGISTERED / CANON UNCHANGED / PHYSICAL COMPLETION UNRESOLVED.**

## A. NIST-RAW-PREFIX-CODEC-QUALIFICATION

All four authenticated archives pass the frozen structure, member-size,
prefix-reading, channel-dictionary and calendar-format predicates under the
declared little-endian `<QQQ` interpretation. No unknown channel, invalid
calendar field or captured archive-structure violation occurs. Every row is
accounted for by the unchanged record-order partition. This qualifies the
specific interpretation of the specified bytes; it does not independently
identify an exact acquisition-software version or certify channel physics.

The audit decoded **3,071,884 rows**. The two synchronization members were
fully read and CRC-verified. Each run3 member was limited to its first
1,048,576 records; their unread tails are outside all record claims below.
The complete compressed bytes of all four objects were SHA-256 verified.

| Object | Decoded rows | Scope | Closed record intervals | Detector rows | Calendar-64 rows |
|---|---:|---|---:|---:|---:|
| Alice 00_03 sync | 485,503 | full member | 194,914 | 95,669 | 2 |
| Bob 00_03 sync | 489,229 | full member | 197,214 | 94,795 | 2 |
| Alice run3 | 1,048,576 | prefix | 512,047 | 24,469 | 6 |
| Bob run3 | 1,048,576 | prefix | 514,203 | 20,159 | 5 |

No equal or decreasing physical-channel timetag occurs in the selected
source order after separating calendar-64 rows. This is a diagnostic of these
decoded portions, not a new monotonicity, missing-data or clock-calibration
claim. Transfer-counter comparisons also have no reversal; the audit does not
equate counter transitions with complete data delivery. The known historical
timing caveat for run3 is not erased by successful byte decoding.

## B. NIST-RUN3-RECORD-INTERVAL-ONEHOT

Both selected run3 prefixes contain closed sync-bracket intervals, and every
such interval contains exactly one setting row. The frozen zero-exception
predicate passes on **1,026,250 station-local intervals** in total.

| Run3 station | `(n_2,n_4)=(1,0)` | `(n_2,n_4)=(0,1)` | Missing, repeated or both |
|---|---:|---:|---:|
| Alice | 258,392 | 253,655 | 0 |
| Bob | 256,820 | 257,383 | 0 |

No cross-station pairing is part of this count. The distinct totals and file
start names are preserved. The synchronization files also show one setting
per closed record interval, as a reported diagnostic; B was preregistered
only for the two run3 objects. No threshold, member, prefix or dictionary was
changed after inspecting the data.

Detector multiplicity remains explicit:

| Run3 station | No detector row | Exactly one | At least two |
|---|---:|---:|---:|
| Alice | 488,341 | 22,960 | 746 |
| Bob | 494,432 | 19,392 | 379 |

These columns count closed record intervals. A zero means only
`NO_RECORDED_DETECTOR_ROW`; multiple rows are not collapsed into an invented
exclusive outcome. No historical Bell detection window has been applied.
The observed one-setting property supplies a concrete input for a later
event reconstruction, while leaving detection-window and multi-record rules
to a separate explicit contract.

## Evidence and falsifiers

The sole initial formal execution used public pin
`dc8abb7e8e5ccaad4ff561776b747801a4d4a373`, after public readback of every frozen
source and inherited notice. It exited zero with empty stderr. EXPECTED.txt
is its exact 32,414-byte, 1,324-line JSON stdout, SHA-256
`ac5edf54c34e40613fc22a55c2423169ac3f8c719ff9472d5c2532b75b135439`.
RUN.md binds the command, environment, source hashes and custody provenance.

Neither frozen scientific falsifier fired. Exact row-accounting invariants
passed. All four nominated members were found uniquely; all use DEFLATED
compression. Agreement with the chosen codec is a conditional qualification,
not an independent proof of the apparatus interpretation. Independent cold
replay on **aarch64 and x86_64 passed** in
[workflow 33960329681](https://github.com/mathorn1973/twist-j/actions/runs/33960329681),
with the same exact verifier and stdout hashes. The aggregate required check,
all 155 tool tests and repository checks passed. Independent post-result
scope, integrity, security and license review passed; RUN.md gives the evidence.
These are reproducible audits of the same archive, not independent experiments.

## Physical boundary and next decision

The available result is an authenticated archived stream, a tested record
codec and an exact station-local partition with settings and detector-row
multiplicity. It is not yet a complete physical event stream. A successor
needs a preregistered mapping from record indices to physical trial labels,
clock-offset evidence for the same run, fixed observation windows, acquisition
coverage and explicit handling of absent/multiple records. The separate 00_03
files alone do not supply a run3 offset certificate.

No trial pairing, detection efficiency, dead time, calibrated no-click,
physical reset, complete instrument family, source distribution, photon
identity, TWIST-J realization bridge or Born occurrence law is established.
The external apparatus is not identified with the proposed U4 circuit.
Any successor must disclose this now-known prefix and its analysis as prior
exposure; a fresh pin cannot make it blind again.

`QDD-INSTRUMENT-APPARATUS` remains O / STOP.
`COINCIDENCE-RECORD-FREQUENCY` remains candidate-H / UNTESTED / STOP outside
the registry. Public Canon v76 and every public claim status are unchanged.
