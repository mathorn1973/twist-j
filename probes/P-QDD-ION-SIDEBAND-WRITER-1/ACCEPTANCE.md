# Public two-architecture acceptance

Status: **PASS; candidate-T; L1; NON-CANONICAL**.
Hardware apparatus: **NOT_RUN**. This accepts a conditional mathematical
pulse theorem and its exact audit, not a laboratory measurement or a
physical L1-to-L5 bridge.

scientific_pin: d928961aea0c939d0abe057fa2149dffa82c5056
tested_result_head: 2d983a6e11632e6a9d6cd6a43527bddc129b7f00
base_main: 1511a2e56e302c415a8879ebfdca079c2190323a
pull_request: https://github.com/mathorn1973/twist-j/pull/1092
workflow_run: https://github.com/mathorn1973/twist-j/actions/runs/35521944696

| Required job | Result | Public evidence |
| --- | --- | --- |
| architecture-x86_64 | success | https://github.com/mathorn1973/twist-j/actions/runs/35521944696/job/106107424701 |
| architecture-aarch64 | success | https://github.com/mathorn1973/twist-j/actions/runs/35521944696/job/106107424629 |
| check | success | https://github.com/mathorn1973/twist-j/actions/runs/35521944696/job/106107468049 |

Both architecture logs explicitly report the same verifier and exact
stdout hashes, matching RUN.md and EXPECTED.txt:

verifier_sha256: 9fd0067e97b91f4a49de7eeadcb8569464ab927df4c2d4d905301c90e9d3fad9
stdout_sha256: 6a82b3d9e8e4a8a7a96352ae34fef62bf95faccfda7c74b214e1b2c693f7dfea

All seven scientific files remain byte identical to the public pin.
The independent reviewer completed REVIEW.md without reading verify.py
or running scientific code. A separate post-run review found RESULT,
RUN and EXPECTED consistent with the frozen proof and scope. It did
not claim another execution or independent runtime-hash verification.

This acceptance-only commit changes no scientific file. Its final PR
head must pass both architecture jobs and aggregate check before merge;
final-head and merged-main evidence are retained in the PR readback.

The physical mechanism is a driven ion sideband with externally supplied
lasers, clocks, cooling and electronics. Continuous-pulse vacuum-domain
invariance and arbitrary-input coherence follow from the written proof
under the stated ideal Hamiltonian. No actual device calibration,
measured fidelity, complete-sequence feasibility, native physical U,
autonomous controller, event law or apparatus-family closure is earned.
The moving native chart remains restricted, and the input coupling is
an intervention. Canon v90 and the entire canon/ tree are unchanged.
