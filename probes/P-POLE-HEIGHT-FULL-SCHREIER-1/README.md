# Full zero-Schreier family and nested collision transport

NON-CANONICAL / L1. Public reservation: issue #1905.

This is a new prospective construction after the preserved bounded miss
in P-POLE-HEIGHT-STABILIZER-CHAIN-1 (PR1904). It uses the same fixed
six-slot preparation I_t=(tB,-tB,u,u,X,2), complete target
G_t=(u+tB,u-tB,0,0,X,2), and64-direction public returning-loop bank.

The new search retains the complete zero-Schreier descriptor family.
It searches root images for a minus-input transporter and retains
star collision loops based at the minus target, then uses those loops
to transport the plus input. Paths are stored as explicit word expressions;
no root-action kernel is silently discarded. A found common word must
pass complete forward and inverse checks on all five original inputs.

Read PREREG.md for exact algorithm and limits, PROOF.md for the
transporter/collision lemmas, and PROVENANCE.md for exposed results and
copied scalar arithmetic. A finite root-image scan is not a complete
group orbit; any capped or exhausted construction miss is inconclusive.

Run from the repository root:

```text
python3 probes/P-POLE-HEIGHT-FULL-SCHREIER-1/verify.py
```

All sources are publicly pinned and read back before execution. Only
EXPECTED.txt, RUN.md and RESULT.md may be appended afterwards. Existing
x86_64 and aarch64 CI must reproduce the same exact output. No Canon,
workflow, physical normalization, merge or release is changed.
