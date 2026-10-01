# C96-06 executable custody and target assessment

NON-CANONICAL / SOFTWARE + SYNTHETIC development. No new formal scientific
gate, instrument run, sealed campaign, independent timestamp or qualification
is claimed. See [CONTRACT.md](CONTRACT.md) for the complete v1 interface and
explicit implementation boundaries. Source pin: #1318
`4756a3df650b91fb1d30806b0fb2aaac00e50cc2`.

The standard-library modules separate allowlist projection, dual forward
assessment, commitments/release ordering, and post-disclosure input replay,
96-coordinate comparison and source-origin checks. Acquisition, immutable
external storage and independently authenticated timestamps have explicit
provider interfaces and fail closed when no provider is configured. No model
code is imported into acquisition or projection.

From the repository root, with Python 3.12:

```text
python -B -m unittest discover -s notes/v96-custody -p test_custody.py -v
python -B notes/v96-custody/project_target.py REDUCTION.json OPAQUE_RANDOM_ID
python -B notes/v96-custody/assess_target.py PACKET.json PUBLIC_CONTRACT.json
python -B notes/v96-custody/audit_unblinded.py PACKET.json LOCKED_VERDICT.json LEDGER.json positive --origin SYNTHETIC
```

CLI inputs refer to the approved external evidence corpus, not files supplied
by this repository. No package installation or third-party runtime is needed.
The unit tests construct small artificial data in memory and write no raw data.

Development observation on 2026-10-01: Python 3.12.10, Windows x86_64, the above
unittest invocation completed with exit 0, 18 original tests. The subsequent
independent review and repair replay is recorded in [REVIEW.md](REVIEW.md).
Covered failure cases:
signed cancellation with excessive absolute work; gross/back-transfer error;
0.960 J target satisfying its lower limit while source lower bound is 0.940 J;
model trace masquerading as observation; changed byte/calibration/settings/code;
missing uncertainty, frames or samples; 399/duplicate verdicts; timing, invalid p
and ADC saturation; metadata/key leak and early disclosure; wrong witness
chronology or unavailable independent witness; persistent synthetic provenance;
covariance, gaps/overlaps, all 96 coordinates and separate inverse table lengths.
This development observation is not a preregistered scientific RUN/RESULT.

The reviewed API additionally retains nested synthetic provenance on early
returns and all eligibility paths, rejects missing local V/I paths, and requires
authenticated acquisition START/END event receipts bound to preparation, raw
corpus and roster. `release_permit` no longer accepts bare caller time integers.
Both timestamp and acquisition witness providers must be explicitly supplied;
there is no production implementation in this package. See CONTRACT.md for
the binding and chronology, including the distinction between acquisition
event time and a later attestation of its finalized corpus.

Next blocker: freeze and independently review the genuine prediction,
sampling and uncertainty inputs, then supply an authenticated raw instrument
reducer, an approved immutable evidence provider and an independent timestamp
provider before attempting the separately owned physical gate. C96-06 is a
tested software foundation, not a completed acquisition/confirmation system.
