# C96-06 custody interface v1

NON-CANONICAL / SOFTWARE DEVELOPMENT / NOT A PHYSICAL GATE.

Source: #1318 `4756a3df650b91fb1d30806b0fb2aaac00e50cc2`, in particular
`notes/C-WORK-RECORD-CARTRIDGE-DEVICE-N/TEST_PLAN.md` sections 3, 5a and 6.
No source law, threshold, qualification requirement or public authority changes.
This is a reviewable schema version fixed before implementing real adapters;
it is not a claim that a prospective public campaign pin already exists.
The coordinator owns any integration change to this contract.

## Boundary and trust

Acquisition owns original independent observations, absolute time, specimen
identities, calibration mapping, acquisition order, all unsuccessful attempts
and assignment keys. It must run separately from the controller. Controller
commands and expected state tables cannot be substituted for observations.
`InstrumentAdapter` in `acquisition.py` is a protocol, not an instrument driver.
`SyntheticAdapter` permanently marks captures SYNTHETIC. A MEASURED string
alone does not authenticate a measurement: `confirm_acquisition` requires an
independent receipt verifier. No such production verifier is supplied here.

The external `ImmutableEvidenceStore` must retain original bytes by SHA-256,
authenticate immutable-storage receipts and permit hash-checked readback.
Source, version, license, size and hash are retained in manifests. Missing and
failed attempts remain in the complete 400-entry corpus roster. Data, serials,
raw ADC, secrets and receipts belong in the separately approved evidence
repository, not in this note or Canon. The code does not select or authorize
that repository. A local file timestamp or a read-only file bit is insufficient.

The reducer is independent of controller/model code. Its frozen input consists
of original raw bytes, complete calibration bytes, sampling/filter/settings
bytes and reducer source bytes. It returns `CALIBRATED_OBSERVATIONS` with
`origin`, SHA-256 for each of those four inputs and the actual target readings.
Expected tables have type `PUBLIC_PREDICTIONS`; a model trace cannot enter the
projector as a reduction. A trusted instrument reducer, authenticated origin
and externally held custody are still necessary to detect a forged type tag.
No generic software can establish physical provenance from caller-supplied
JSON alone.

## Exact packet schema

`schema.py` is the executable closed schema at every nested packet level.
Unknown fields are custody/blinding incidents when supplied to the evaluator.
The projector creates fresh dictionaries from the explicit allowlist; it never
copies arbitrary metadata. No free-form error strings, file links, calibration
references or persistent cartridge aliases enter packets.

All SI numbers use canonical exact rational strings (`1`, `-1/10`, `0`);
fractions are reduced. This avoids floating-point/NaN ambiguity and numeric
text used as a metadata channel. Coordinates and optical codes are JSON
integers (booleans do not qualify). An absent measurement is JSON `null`, not
zero. Arbitrary strings are not accepted in numeric fields. Quality flags are
the sorted unique subset of MISSING, SATURATION, TIMING, INVALID_POINTER,
SYNTHETIC. The evidence-class marker is a local validity flag and must be
uniformly applied across an entire test cohort. `packet_flags` collects all
packet, reading and port markers before any assessment return. The projector
lifts any nested SYNTHETIC marker to the packet flag; the locked verdict and
post-disclosure eligibility retain it even if frames are missing. An externally
supplied MEASURED label cannot override any of those markers.

| Field | Exact content |
| --- | --- |
| schema | `twist-j-c96-custody-1` |
| id | Fresh random 128-bit lowercase hex opaque ID; unrelated to order/identity |
| frames | Initial state and every G/A/B/F boundary, preserving all read samples |
| frame | step, layer, readings; INIT at 0, G/A/B/F for steps 1..10 |
| reading | relative t_s, original 31 target coordinates, physical p, raw 3-bit optical code, angle_deg, B_2/Z_2/r_2 energies/U/voltage, temperature_C, flags |
| ports | B_2/Z_2/r_2 signed simultaneous SI V/I segments with relative t0_s/t1_s and flags |
| uncertainty | time_s, first_work_J, whole_abs_J, ten slot_abs_J bounds |
| flags | Closed local validity vocabulary above |

The optical-code map, read-grid, SI conversion, reconstruction convention and
uncertainty method must be fixed with the reviewed physical gate before data.
No optical mask or sampling qualification is presumed to exist. Each read grid
includes the start and end of the original 100 ms fixed read window. Interior
sampling sufficient to qualify stability remains a physical-gate input; two
endpoint samples alone do not establish stability between samples. Missing
samples are retained as nulls/empty rows; shifted actual times remain shifted.

The common public predicate contract contains the entire positive prediction
family, one null table, the common read grid and the optical-code map. It is
the SAME contract for every packet, contains no actual run assignment, and
must be derived and reviewed against the pinned independent mathematical
reference before measurement. Runtime code checks its basic event order,
resource arrival at 2, first work at 3, old receiver reset at 4, HIT through 10
and constant null preparation. It does not prove a caller's prediction tables
implement the mathematical law. The development fixture deliberately uses
artificial tables; it is not the twenty-seed physical prediction corpus.

## Numerical decision

Both target predicates are always evaluated. Work is signed simultaneous
VI integrated over [20,22] s for the entire first receiving G operation,
including quiet/read interval and all back-transfers. Null work is the integral
of absolute VI on B_2 over each complete two-second G slot and all 100 s,
never the absolute value of net work. The other target port series remain in
the packet for independent balances. All three local V/I paths must cover
the complete 100 s horizon; an empty or gapped Z_2/r_2 path produces
LOCAL_PORTS_MISSING and an INDETERMINATE predicate, unless a known failure
already takes precedence. This coverage requirement does not add their
energies together; adding both ends of one transfer would double-count energy.
G-slot switching beyond its deadline is a timing fault.

The interval reconstruction is piecewise constant simultaneous V/I with exact
arithmetic. Its use is conditional on the frozen uncertainty covering timing,
filtering, interpolation, unresolved ripple, offsets and tails. It neither
averages V and I separately nor interpolates missing segments. Missing
uncertainty is INDETERMINATE. Measured threshold violation or known invalid
pointer/saturation/timing is FAILED. Both require zero FAILED/INDETERMINATE
trials for confirmation. A known failure takes precedence over incompleteness.

`expanded_uncertainty` accepts all eight named sensitivity-weighted covariance
components in J^2, tests positive semidefiniteness with rational arithmetic,
retains covariance, and rounds the square-root bound upward to 10^-12 J before
applying the supplied coverage factor. Effective degrees of freedom and a
hash-bound coverage justification are mandatory inputs. They are not earned
by merely providing a number or hash; physical review must inspect them.

## Commitments, timing and release

`framed_commitment` hashes domain `TWIST-J/C96/bundle/1` plus NUL,
u64-big-endian nonce byte length, a secret independently generated 32-byte
nonce, u64-big-endian member count, then for each member in lexicographic name
order: u64 name-byte length, UTF-8 name, u64 data-byte length, original bytes.
Generate nonce using `secrets.token_bytes(32)` independently for each bundle.
The public commitment conceals small assignment spaces; nonce and revealing
names/contents remain sealed. Randomness of externally supplied IDs/nonces
cannot be inferred from shape validation.

Preparation bundle binds keys, balanced order, physical mapping, calibrations,
law, firmware/build, predicates, converter/settings/source, full initial inputs,
all predicted tables, readiness/qualification and custody owner/receipt policy.
After acquisition, a second bundle binds every original raw file, all failures,
the complete roster and storage manifests. Neither manifest substitutes for
its original immutable data. Preparation must precede acquisition; raw sealing
must follow it and precede the complete assessor lock.

`lock_verdicts` accepts exactly 400 unique roster IDs, both tri-state outcomes,
packet hash, common predicate-contract hash and closed findings. It rejects
399, duplicates and roster mismatch. Lock all assessments together. Store
packets themselves with the lock so their hashes preserve measured trace and
quality findings. Hash and independently timestamp the complete lock before
ANY assignment key, original record or identifying inverse record is released.

`IndependentWitness.verify` must authenticate an independently held receipt
under the separately frozen trust policy. There is no default implementation;
a local timestamp is not accepted. `release_permit` checks all three public
commitment receipts, their chronology, the entire locked output and declared
blinding incidents. Its exact API is:

```text
release_permit(roster, locked, commitments, receipts, timestamp_provider,
               acquisition_receipts, acquisition_provider,
               incidents, inverse_records_still_sealed)
```

The acquisition receipt map has exactly ACQUISITION_START and ACQUISITION_END,
each containing authenticated receipt bytes. There are no caller-supplied
start/end time arguments. `IndependentAcquisitionWitness.verify` authenticates
the actual event time in each receipt and its exact shared `acquisition_binding`
digest. That digest binds the preparation commitment, final raw-corpus
commitment and hash of the complete sorted 400-ID roster. Replacing any of
those three objects invalidates both event bindings.

The acquisition provider must retain independently recorded session events
and authenticate their association with the finalized raw corpus. This can
be a later attestation linking already retained start/end records to the
completed manifest; it cannot be a claim that the final raw hash was known
before acquisition. The returned times are authenticated acquisition event
times, not the publication time of that later attestation. A TSA merely
signing caller-supplied historical times does not satisfy this interface.
The provider and its trust policy are still unavailable production inputs;
tests use an explicitly named mock and earn no real timestamp evidence.

The required chronology remains preparation publication < acquisition start
<= acquisition end < raw-corpus publication < complete verdict publication.
The permit includes its acquisition binding and authenticated event times.
The custodian must enforce the permit at the actual key-release boundary.
This in-process helper is not a replacement for separation of accounts/operators
or a tamper-proof access service.

Inverse-first and forward-first blocks have their own 81-boundary full tables,
not forward target predicates, and stay sealed through the 400-forward lock.
The exact inverse inventory and validated preparation roster are inputs still
required from the separately owned execution gate.

## Disclosure audit and remaining gates

First verify both original bundle commitments and original bytes. Next replay
the frozen independent reducer with the committed calibration/settings and
compare the projected packet byte-for-byte in canonical form. Any mismatch is
a custody failure; never rewrite the locked packet or verdict. Only then use
the revealed configuration to select its already locked target predicate.

The separate full-state routine compares all 96 coordinates and eleven banks
at all forward/inverse layer boundaries. `source_origin` bounds each non-path
contribution over source G_0 through target G_2 (0..22 s), subtracts it from
W_B-U_W and checks independent B_2/Z_2/r_2 balance residuals. Initial source
energy equality has a separate uncertainty-aware helper. The complete gate
must additionally authenticate those observations, compare all prepared inputs,
check continuous voltage/deadlines/reserves, swap losses, independent whole
apparatus balances/heat and all inverse criteria. These physical inputs and
integration are unavailable. No function returns physical CAMPAIGN_PASS.

The numerical CLI is explicitly a partial audit. Setting `--origin MEASURED`
does not authenticate evidence and returns PENDING_AUTHENTICATED_FULL_AUDIT.
SYNTHETIC flags survive projection, target lock and campaign selection and
always block confirmatory eligibility. Changing a file name cannot promote
them. A valid target result can coexist with FAILED source provenance.
