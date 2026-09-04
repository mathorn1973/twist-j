# Result

Status: `ABANDONED`.

```text
probe                         P-J-CIRCULAR-QDD-DUAL-SIMPLEX-BRIDGE-1
public lock                   issue #799
public pin                    19bc56ef1f476f3f64ed03a7ce22b7b6b7c49554
accepted-verifier attempts    1
completed formal records      0
scientific result             none
recorded                      2026-09-04, Public Canon v75
```

## Why no completed gate record exists

The two-file preregistration pin was public and its remote bytes had passed
byte-for-byte readback before the accepted verifier was invoked.  The child
process returned to an in-memory capture harness, which had collected its
stdout, stderr, exit code and UTC timestamps as Base64 fields in JSON.  The
orchestration layer then called an unavailable JavaScript `atob` decoder and
raised `ReferenceError` before those captured fields were retained or exposed.

No exact stdout, stderr or child exit-code record remains available.  The
accepted verifier was not rerun, and its output is not reconstructed from the
source or from the predicted result.  This is a technical evidence-custody
failure, not a fired mathematical falsifier and not evidence for either frozen
claim.

Under `POLICY.md`, the pin is therefore abandoned: it produced no auditable
completed gate transcript.  `EXPECTED.txt` and `RUN.md` are intentionally
absent.

## Immutable pin

```text
branch:             probe/P-J-CIRCULAR-QDD-DUAL-SIMPLEX-BRIDGE-1
base:               6a312ea988e885ff63f3bfeebf4c6c58f70bbef4
pin commit:         19bc56ef1f476f3f64ed03a7ce22b7b6b7c49554
pin tree:           6aa25a67b98d7728ee220645fec48e2c103ce41c
PREREG blob:        4b7cf75621fc9403c6c8c03d2f8ed7395897721f
PREREG SHA-256:     3a4aaa4cf370e2f9bfa1105354b06f69e3ce439d4e3357de7034d86f8b08973b
verify blob:        85c4c2f18c137ab4fff4426d100aaca74184ee34
verify SHA-256:     0fb23c9b869f1c98852dcd036d2bd31d623dc85bc584cedefb88b651fa0d812f
```

The frozen `PREREG.md` and `verify.py` remain exactly as publicly pinned.

## The identifier is consumed

`P-J-CIRCULAR-QDD-DUAL-SIMPLEX-BRIDGE-1` is spent.  It must not be reused,
renamed, repaired, rerun or resumed, and no part of this lane may be cited as
scientific evidence.  Any retargeted attack requires a new identifier, a new
public claim lock, a new preregistration and a new immutable pin.  Its
preregistration must name this predecessor and disclose the failed transcript
capture before its own execution.

## Canon effect

None.  Neither frozen claim is confirmed or fired.  No claim is registered,
promoted, lowered or retired; no Registry, Frontier, gate, dependency,
dictionary, `STATUS.md` or Canon text changes.
