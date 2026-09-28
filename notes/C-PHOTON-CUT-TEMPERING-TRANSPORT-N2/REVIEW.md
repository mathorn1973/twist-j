# Prospective static review of the fixture correction

**PUBLIC / NON-CANONICAL. Issue #1263. No N2 execution in this review.**

A separate delegated assistant reviewed this successor's source differences,
the predecessor's review and recorded outcome, and the unchanged controller's
failure handling. The reviewer did not author the analyzer or fixture
correction, but did author the unchanged predecessor sampler. Thus this is
an independent review of the correction, not an independently authored
sampler, a second human confirmation, or an executed reproduction.

The comparison baseline is the consumed first pin
`42efd804047ab89aa80e79d37276366d5cfa8596`, in
`notes/C-PHOTON-CUT-TEMPERING-TRANSPORT-N/`. Each predecessor source compared
locally was checked byte-for-byte against that Git object. The only changes
to the four executable sources are:

- `test_analyze.py`: the recursive forbidden-interval-name check calls
  `str(key).lower()` instead of `key.lower()`.
- `analyze.py`: the reported `ITEM` changes to this successor's identifier.
- `sample.cpp` and `run_pilot.py`: no byte changes.

The recorded failure occurred because `roundtrips_by_replica` has integer
keys in the in-memory report inspected by the synthetic fixture. Converting
a key to its string representation is appropriate for this name check.
For string keys the predicate remains exactly the same; for integer keys
it becomes defined and checks their decimal names. Traversal of every child
dictionary and list remains unchanged. No assertion, test case, recursion,
threshold, status rule or production calculation is removed or weakened.
The fix does not catch and suppress assertion failures. It addresses the
observed exception without claiming that all prospective tests will pass.

The analyzer rename changes only report identity. In particular its
precedence remains implementation failure, then mobility failure, then the
stationary identity checks. Means remain `NONINFERENTIAL_ESTIMATE`; the
analyzer still creates no signed confidence interval or squared-contrast
interval. `TRANSPORT_QUALIFIED` remains a finite engineering diagnostic,
without a proof of equilibrium, decorrelation or a mixing-time bound.

The unchanged controller first requires one sampler audit and one complete
fixture invocation, including their exact expected stdout, zero stderr and
zero return code. Failure stops the attempt before production. After both
pass it schedules the same twenty jobs, once each, then invokes the analyzer
once with separately recorded return code, stderr and hashes. It creates a
new output directory and has no retry path. The previous attempt's recorded
sampler-audit PASS is not substituted for the successor's declared audit.

The prior attempt is consumed and its test failure must stay recorded.
Reusing the original seeds and budgets for all twenty jobs does not reuse
or select lattice observations: none of those jobs ran in the predecessor.
A different identifier and complete public pin before execution distinguish
this corrected prospective attempt from an unrecorded retry.

The finite target and kernel arguments are inherited from the unchanged
predecessor `PROOF.md` at the stated first pin, SHA-256
`f6ca22bb038bb1f47c98acf6c1011a703178f1b8414fe5e9731b1a1aa6ecad55`.
They require no duplicate or changed proof. The source comparison also
confirmed these unchanged hashes:

- `sample.cpp`: `f629b60e71079b8e14623a1cadd9b7aaac303fb72e859679bba7a82eb08f43a3`.
- `run_pilot.py`: `3dbe211fdf85a221f6900d6a7b20f17bcfb4e1ca39633410f242ad86d8e89251`.

No sampler, audit, fixture, analyzer or production job was executed during
this review. All floating output continues to have ZERO scientific
evidential weight. The sector-polarization lower bound and P1 remain open;
Public Canon v92 receives no change.

The successor PREREG.md was also read before this review was completed.
Its immutable incorporation preserves the complete original protocol while
replacing the identifier and six-file source-pin list. Its explicit matrix
is lattice size L=4, two modes, two endpoint bases and five starts; any
reference to layer L6 is a hierarchy label, not a request for lattice L=6.
The public readback, fresh checkout/output directory, fixed first invocation
and failure preservation requirements are present. The optional reuse of a
hash-verified compiled binary does not substitute prior program output or
reuse a trajectory. The prospective static verdict is **READY TO FREEZE**
for this disclosed fixture correction and unchanged engineering protocol.
This verdict does not assert any future audit, fixture or production result.
