# Delivery checks and self-review

NON-CANONICAL. Administrative checks are not scientific promotion.

## Executed local repository checks

The following checks passed on the isolated candidate tree:

```text
python3 tools/check_policy.py                         POLICY PASS
python3 -m unittest discover -s tools -p 'test_*.py'    189 tests, OK
python3 tools/check_canon.py                          CANON PASS v103 claims=530
python3 tools/check_ledger.py                         LEDGER PASS
python3 tools/check_gate_contract.py                  GATE CONTRACT PASS
python3 tools/check_verifier.py --base BASE           VERIFY NOT APPLICABLE
python3 tools/check_reproduce.py --base BASE          REPRODUCE NOT APPLICABLE
git diff --check                                     PASS
```

BASE is dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d. The unit-test output
includes expected negative-fixture diagnostic text; the actual suite
completed with all 189 tests successful. The changed-path checks correctly
select no formal probe or minimal reproduction for this notes-only change.
The separate actual scientific execution is described in RUN.md.

## Author self-review, not independent review

- The alphabet table is complete for the declared old chain. Its contacts
  swap neutral resources only. No field swap, source impulse or basis
  change was silently admitted.
- Every accepted field inverse is integral; rejected G leaves the entire
  input fixed. The depth proof does not treat an inadmissible rational
  intermediate as an actual state.
- Nonzero G_L residues have depth one for every integer representative,
  since L^2 Z^4=5 Z^4. Higher initial energy does not change this fact.
- The Q1 proof admits more schedules than the old fixed chronology. The
  negative result therefore remains valid for that chronology, but says
  nothing about extending the primitive set.
- Q2 requires identical source norm and the displayed initial R/PLu
  family. Its permitted controller cannot inspect the differing field.
  Source-dependent scheduling is allowed in Q1 but not confused with Q2.
- The true inverse of Ghat subtracts the event on the recovered input;
  Ghat itself is not called involutive. Occupied C5 states are retained.
- H=15 for the outside-alphabet target vector is only an attained witness,
  not a claim of the complete boundary-four minimum or a funded contact.
- A single aarch64 code execution is a finite self-audit. Notes-only CI
  does not automatically rerun it on two scientific architectures.

All frozen source, contract, preregistration and expected-output bytes
remain identical to the preregistration commit. The proof and results
were added in a descendant, not amended into that pin.

## Publication boundary

Only notes/C-U-FIELD-CHAIN-WORD-OBSTRUCTION-N/ is changed. The files were
reviewed for private paths, hostnames, credentials, personal data, binary
content, unreviewed external material and out-of-scope status claims.
No Canon, policy, workflow, existing note or probe is edited. Authorship
is A. M. Thorn <thorn@twistj.com>, under the repository Apache-2.0 policy.
The draft pull-request job receipt is recorded on issue #1590, not assumed
here before its execution. No merge, tag, release or promotion is requested.
