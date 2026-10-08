# Package validation

**NON-CANONICAL / NO AUTHORITY.**

The exact mathematical first runs are recorded in [RUN.md](RUN.md). This
file concerns repository checks and final report review; it supplies no
additional scientific execution or architecture result.

## Repository checks

The complete reporting package at
`c38621793736cbc50367468f468cf9474cb9f404` passed the following local checks
on 2026-10-08. They use the repository's existing unchanged check programs.

| Command | Observed result |
|---|---|
| `python3 tools/check_policy.py` | POLICY PASS |
| `python3 tools/check_canon.py` | CANON PASS v100 claims=510 |
| `python3 tools/check_ledger.py` | LEDGER PASS claims=510 items=574 dependencies=1050 evidence=510 history=1057 gates=26 programs=7 |
| `python3 tools/check_gate_contract.py` | GATE CONTRACT PASS gates=26 |
| `python3 tools/check_verifier.py --base 7d7f588c42422c2cf37b04d76ebc13ca55eb96dc` | VERIFY NOT APPLICABLE |
| `python3 tools/check_reproduce.py --base 7d7f588c42422c2cf37b04d76ebc13ca55eb96dc` | REPRODUCE NOT APPLICABLE |
| `python3 -m unittest discover -s tools -p 'test_*.py'` | 183 tests, OK, exit 0 |
| `git diff --cached --check` | No whitespace errors |

The two NOT APPLICABLE outcomes are expected: this note changes no public
probe or minimal reproduction. They must not be described as scientific
reruns of this note. The unit suite's intentionally failing fixtures print
negative-case labels; all 183 unit tests passed.

## Final exposed report review

After both first outputs were available, a separate assistant context
checked README, RESULT, RUN, CUSTODY, PROMO and EXPECTED against the pinned
proof and exact output. It accepted the reported tables, small-size cases,
distinct torus kernels, execution counts, custody exclusion and scope.
It read no candidate program and ran no scientific code. This is a later
exposed document review, not an extension of its earlier proof-author
independence or another computational confirmation.

One wording issue was corrected in an ordinary follow-up commit: the
future native **state family** must be invariant under the original U;
the complete reader must be specified and satisfy the appropriate
intertwining relation. The reader's values need not be constant in time.
This clarifies the native-admission paragraph of PROMO and changes no
proof, scientific source, output, falsifier or scope.

Final packaging includes this record and an SHA-256 manifest of every
other note file. The manifest excludes itself. The original code/proof
pins and source bytes remain unchanged. All new tracked files are within
the single reserved note directory. No Canon, policy, workflow, existing
probe, existing reproduction or third-party dependency is modified.

No remote PR check or public scientific two-architecture gate is claimed.
The exact local Git history and pre-execution public comment readbacks
remain the custody evidence described in CUSTODY and RUN.
