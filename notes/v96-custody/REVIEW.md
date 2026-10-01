# Adversarial custody review and repairs

NON-CANONICAL / SOFTWARE and SYNTHETIC development only. Date: 2026-10-01.
No acquisition run, authentic witness receipt, blinded campaign or physical
PASS occurred. Public authority and the #1318 acceptance limits are unchanged.

The reviewer was separate from the initial package author. It read every
module, schema, test and contract against pinned #1318 TEST_PLAN sections 3,
5a and 6. It first reviewed without modifying source and replayed the original
18 tests successfully. It then constructed four small synthetic adversarial
witnesses, reported their concrete failures to the coordinator, and implemented
the authorized repairs below. Consequently this is independent discovery of
implementation defects followed by reviewer-authored fixes; the repairs are
subject to the coordinator's final review, not asserted to be independently
reviewed merely because the same reviewer wrote this record.

## Findings and exact disposition

| Initial defect | Synthetic witness | Repair and regression |
| --- | --- | --- |
| Post-disclosure eligibility looked only at top-level SYNTHETIC | A nested reading marker appeared in assessor findings, but an external MEASURED label yielded PENDING_AUTHENTICATED_FULL_AUDIT | `packet_flags` validates and collects every schema-defined nested marker; projector lifts SYNTHETIC; eligibility checks both all packet markers and locked findings |
| Missing-frame early return erased provenance and known failures | A top-level SYNTHETIC packet missing its last frame produced only FRAME_ROSTER | Marker collection and quality decisions precede every early return; a known SATURATION remains FAILED even with a missing frame |
| Missing non-B local paths did not invalidate the positive predicate | Empty Z_2 and r_2 V/I series still yielded positive SATISFIED | All three local paths require complete 0..100 s coverage; missing paths give LOCAL_PORTS_MISSING and INDETERMINATE, without summing or double-counting path energies |
| Acquisition times were bare caller integers | Realistically shaped commitment receipts plus invented start/end integers were enough for RELEASE_PERMIT | Separate authenticated acquisition START/END receipts are required; their independently returned event times and shared binding cover preparation, final raw corpus and exact roster |

The first three repaired paths are covered for reading and port markers,
missing frames, immutable locked findings, all three empty/gapped series and
known-failure precedence. The fourth is covered for unavailable providers,
ordinary local time text or integers in place of receipt bytes, missing event
receipts, changed preparation commitment, changed raw commitment, changed
roster, invalid chronology, early disclosure and declared incidents.

The acquisition binding is not a claim that a final raw hash existed before
the capture started. A production acquisition provider must authenticate an
independently retained session's actual start/end events and their association
with the finalized raw corpus. A later attestation may link those existing
events to the final manifest. A generic timestamp authority merely signing
caller-asserted historical times is insufficient. CONTRACT.md now states this
trust requirement and the new API explicitly. No production provider exists
in this package; TestOnlyAcquisitionWitness is a test mock, not time evidence.

## Other reviewed behavior

The closed nested packet schema rejects explicit serials, persistent aliases,
configuration/route/cut fields, absolute-timestamp fields, calibration references,
free-form errors and extra keys. The projector constructs fresh allowlisted
dictionaries. Exact rational encodings forbid alternative numeric spellings,
booleans and nonfinite numbers. This does not authenticate the physical truth
of allowed values or make genuine target behavior statistically indistinguishable.
Correct relative-time reduction, sampling qualification and metadata-free raw
conversion still require the trusted instrument reducer.

Both target predicates are evaluated for each packet against one common
public prediction contract. They are not chosen using a revealed label.
The first-work integral is signed over the complete [20,22] s operation;
null work uses integral abs(VI) over each G slot and the complete horizon.
Gaps are not interpolated and missing uncertainties are not zero. The
0.960 J example remains a target pass with a failed 0.940 J source lower
bound under its stated uncertainties and non-path energy. Source attribution
is separate from target assessment and uses the full 0..22 s causal interval.

Exact covariance validation checks symmetry and positive semidefiniteness,
retains correlations, and rounds the square-root upper bound conservatively.
Coverage factors, degrees of freedom, physical calibration and uncertainty
justification remain explicit external inputs; the function does not establish
their measured validity. Full-state comparison covers 96 coordinates and
eleven banks with separate forward/inverse table sizes, but authentic frozen
prediction tables and observed raw records are still required.

Commitments bind domain, secret 32-byte nonce, member count, names and byte
lengths. The complete roster and lock require exactly 400 unique IDs and both
tri-state verdicts; 399 or duplicate entries fail. Disclosure still requires
all locked verdicts, independently witnessed commitment chronology, authenticated
acquisition events, no blinding incident and sealed identifying inverse records.
The helper supplies a permit to a separate custodian; it does not control
real keys or instantiate a tamper-proof evidence service.

Post-disclosure replay checks original raw/calibration/settings/reducer bytes,
requires a separately supplied frozen reducer, and compares the reconstructed
projection to the locked packet. It never silently replaces a packet or a
verdict. Genuine prediction generation, independent raw acquisition, trusted
code identity, complete readiness and full-campaign orchestration are outside
the implemented foundation and must not be inferred from shape/hash checks.

## Actual development replay

After the repairs, from the repository root:

```text
python -B -m unittest discover -s notes/v96-custody -p test_custody.py -v
```

Actual environment: Windows x86_64, CPython 3.12.10. Result: exit 0,
22 tests, unittest reported 0.405 seconds. All fixtures were constructed in
memory, explicitly synthetic; no instrument was accessed, no original corpus
was invented, and no evidence provider or real timestamp authority was used.
`git diff --check` also passed. This is a development test replay, not a
prospectively preregistered scientific RUN/RESULT or architecture gate.

The coordinator separately inspected the repaired provenance collection,
source audit and acquisition-event binding, then replayed the same 22 tests
on CPython 3.12.10 / Windows x86_64 (exit 0, 0.399 seconds). No further
blocking defect was found in those reviewed changes. Trusted provider truth
and the full physical audit remain external obligations; passing these
tests does not authenticate caller-supplied MEASURED labels or mock receipts.

## Disposition

The four observed defects are repaired and covered by executable regressions.
The numerical/custody foundation is reviewable. It remains ineligible to
declare an actual confirmation campaign complete: authentic instrument
adapters/reducers, independent acquisition and timestamp providers, approved
immutable storage, frozen genuine prediction/roster inputs, qualified
calibrations, and full physical audit integration are still absent. The partial
audit continues to return `campaign_pass: false`; no function awards physical
CAMPAIGN_PASS. A synthetic numerical SATISFIED result always retains its
non-confirmatory provenance.
