# Public two-architecture acceptance

Status: **PASS; candidate-T; L1; NON-CANONICAL**.
This accepts the mathematical proof audit. It is not an experimental
measurement, a physical-origin theorem or a Canon registry change.

scientific_pin: 8acb9c3379ca6ff2335684715fb07ec89e868509
tested_result_head: 3fa8541bd2d8c8ed937069b045bc215ddd50dd5b
base_main: b61e3801725bc22c98bfeb33460fa738f0b4eff7
pull_request: https://github.com/mathorn1973/twist-j/pull/1090
workflow_run: https://github.com/mathorn1973/twist-j/actions/runs/35518809194

| Required job | Result | Public evidence |
| --- | --- | --- |
| architecture-x86_64 | success | https://github.com/mathorn1973/twist-j/actions/runs/35518809194/job/106099201156 |
| architecture-aarch64 | success | https://github.com/mathorn1973/twist-j/actions/runs/35518809194/job/106099201182 |
| check | success | https://github.com/mathorn1973/twist-j/actions/runs/35518809194/job/106099251737 |

Both architecture logs explicitly report the same verifier and exact
stdout hashes, matching RUN.md and EXPECTED.txt:

verifier_sha256: a1015c9c79f0c72c69c314cd854c9e2174253af3bac214e5e9f4c15a7580385b
stdout_sha256: be6be3a22da1bc518c2557c729c3bd28d6eb646d44497caffdaaa60e7cd379d4

The independent reviewer completed REVIEW.md without reading verify.py
or running a scientific program. The separate post-run review of RESULT,
RUN and EXPECTED also passed after two summary clarifications: equal
positive port gaps, and energy-eigenstate inputs and outputs. Those
clarifications change no scientific pin, target, proof or threshold.

All six scientific files remain byte identical to the public pin.
This acceptance-only commit changes none of them. Its final PR head
must pass both architecture jobs and aggregate check again before merge.
The PR retains the final-head evidence and merge/readback identity.

The full environment conclusion rests on the written proof. The code
obstruction assumes the declared energy encoding and LOW--HIGH coherence;
the stronger global B obstruction requires all checkpoint inputs.
The pulse construction admits externally supplied quantum control and
does not identify a native carrier or a physical time law. No apparatus
owner or L1-to-L5 gate is closed. Canon v90 and the entire canon/ tree
remain unchanged.
