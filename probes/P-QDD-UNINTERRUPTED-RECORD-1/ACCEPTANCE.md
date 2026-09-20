# Public two-architecture acceptance

Status: **PASS; candidate-T; L1; NON-CANONICAL**.
This is acceptance of the formal proof audit, not physical apparatus
realization or a Canon registry change.

scientific_pin: a6c66f3b5ae9c75f35980816a2b00007f366bdc2
tested_result_head: 2538e67bb6203ea4e79efb09c85f878a73f8a465
base_main: 963cb34d6a68a09d93b611f32211d9a3bdc547b7
pull_request: https://github.com/mathorn1973/twist-j/pull/1086
workflow_run: https://github.com/mathorn1973/twist-j/actions/runs/35508007129

| Required job | Result | Public evidence |
| --- | --- | --- |
| architecture-x86_64 | success | https://github.com/mathorn1973/twist-j/actions/runs/35508007129/job/106070964983 |
| architecture-aarch64 | success | https://github.com/mathorn1973/twist-j/actions/runs/35508007129/job/106070964855 |
| check | success | https://github.com/mathorn1973/twist-j/actions/runs/35508007129/job/106071012393 |

Both architecture logs explicitly report the same pinned verifier and
byte-identical stdout:

verifier_sha256: 2f4ee7d4fdb86c69082ecdd31eeb1c20c8c59940dddb215a031e01b391c34136
stdout_sha256: 876bb254aa77fe5be6ec4a79ec4905bc71ec3ac17176b0fda5750e89cd471347

These match the first local execution recorded in RUN.md and EXPECTED.txt.
The independent breaker passed its separately recorded local execution in
BREAKER-RUN.md. It is an independent implementation, not a second
architecture run.

All seven scientific files remain byte identical to the public pin.
This acceptance-only commit changes none of them and supplies no new
scientific result. Its final pull-request head must pass both architecture
jobs and aggregate check again before merge. The public PR retains those
final-head checks and the merge identity.

The written inductions in PROOF.md establish the all-duration statements;
the finite programs audit their exact premises. Physical entrance and exit
interactions, archive realization, single events and occurrence remain
open under QDD-INSTRUMENT-APPARATUS. Canon v90 and the entire canon/
directory remain unchanged.
