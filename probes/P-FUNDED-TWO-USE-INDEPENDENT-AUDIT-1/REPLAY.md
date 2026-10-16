# Reproduction receipt for the negative geometry report

**NON-CANONICAL / L1 / scientific status remains PARTIAL / STOP.**

This receipt records actual replay of the 210-byte failure report in
EXPECTED.txt. Passing checks establish byte reproducibility of that negative
report. They do not establish completion or success of the planned audit.

Scientific pin: `1949d6c5c9712fc2c3aa10f0ac296afb9ea5e928`.
First result head: `2d6f2333aa519897e0fc328ef6b640c28733aba8`.
All seven pinned scientific/preregistration/custody files remain unchanged.

## Repository checker on Linux

From the clean first-result checkout on Ubuntu 24.04 / aarch64 / Python
3.12.3, the unmodified checks returned:

```text
POLICY PASS
CANON PASS v101 claims=514
LEDGER PASS claims=514 items=578 dependencies=1063 evidence=514 history=1061 gates=26 programs=7
GATE CONTRACT PASS gates=26 kinds=DEFINITION_PROJECTION:2,DICTIONARY_LIFT:13,FIRED_NEGATIVE:3,OPEN_DECISION:1,OPEN_LIFT:5,OPEN_SELECTION:2
VERIFY PASS P-FUNDED-TWO-USE-INDEPENDENT-AUDIT-1 4f8481297febd4a5d01b47bda050a5f30216b4474ff76de761fefbd0d5c87a0c 481062b8cbedafe06f14835e0ed1a3dee33380b48c92782a76478d616f747acf
REPRODUCE NOT APPLICABLE
```

Changed-probe checker command:
`python3 tools/check_verifier.py --base 8b91a935c426036e00ecb300019fd94734addeec`.
The existing 600-second limit, pin/hash checks, exit-zero, empty-stderr and
exact stdout requirements were not changed or bypassed.

## Required GitHub architectures

[Policy run 38717577560](https://github.com/mathorn1973/twist-j/actions/runs/38717577560)
records first result head `2d6f2333aa519897e0fc328ef6b640c28733aba8`.

| Required job | Actual result | Python | Evidence |
|---|---|---|---|
| architecture-aarch64 | success | CPython 3.12.15 | [job 116363917515](https://github.com/mathorn1973/twist-j/actions/runs/38717577560/job/116363917515) |
| architecture-x86_64 | success | CPython 3.12.15 | [job 116363919316](https://github.com/mathorn1973/twist-j/actions/runs/38717577560/job/116363919316) |
| check | success | aggregate | [job 116364250386](https://github.com/mathorn1973/twist-j/actions/runs/38717577560/job/116364250386) |

Both architecture job logs explicitly report the same VERIFY PASS line above,
including the same verifier SHA-256 and failure-stdout SHA-256. All policy,
unit, Canon, ledger, gate-contract and changed-probe steps passed. Publication
was skipped as appropriate for a draft PR. This is two-architecture replay
of one implementation, not two independent implementations and not a
successful two-use census. No comparison digest was executed.

This later receipt changes documentation only; its own PR-head checks must
also pass before handoff, with final head/job links reported on #1508.

## Review and remaining block

Lane R at `75b72a01974d76a68a649f2fe2092e5a8264472c` was reviewed statically
only after V's public code pin and public first-run record. Its conditional
contact factor, support, sharp fixed-linear rank and occupied-state refresh
counterexample were supported without an actionable finding. The detailed
source-exposed review is posted on issue #1508. Its proofs do not establish
the 869-site cardinality and do not resolve V's STOP.

The next scientific step needs an explicit source/implementation discrepancy
disposition and a new authorized identifier/pin. The current identifier is
not resumed or repaired. No merge or Canon promotion is requested.
