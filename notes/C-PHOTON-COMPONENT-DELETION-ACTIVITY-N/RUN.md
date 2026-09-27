# RUN - C-PHOTON-COMPONENT-DELETION-ACTIVITY-N

**Status:** candidate-C audit only. Not a formal public probe.
**Owner:** #1200.

## Custody

- preregistration commit: \`318522229afbbf7f97d152ef8812ca74d8414d7a\`
- PREREG blob: \`8aa0ad88b56049d44947c416e1a6890a2bcb5390\`
- verifier commit before first execution: \`944b95a7d14ae6717f46ea37cef376f26bacab2b\`
- verifier blob: \`f7fa8010558434697cec63282aff13becb8954d8\`
- PREREG SHA-256:
  \`54c6ad4e358deee0b5a547e56661976156f383a092960f2866c17a5c2c483b1c\`
- verifier SHA-256:
  \`e32c0bda618e460a921b1e4881ab65f5e864f1aede32d3f80f065a6ffd35b97b\`

PREREG.md and verify.py were read back from GitHub before execution.

## Clean-clone execution

\`\`\`text
architecture: aarch64
python: Python 3.13.5
head: 52da9ff8c16a8502e87530464614d5beadb9475f
prereg_sha256: 54c6ad4e358deee0b5a547e56661976156f383a092960f2866c17a5c2c483b1c
verify_sha256: e32c0bda618e460a921b1e4881ab65f5e864f1aede32d3f80f065a6ffd35b97b
exit_code:0
stdout_bytes:497
stderr_bytes:0
\`\`\`

Exact stdout:

\`\`\`text
PASS G1 audit: factorial deletion inequality holds for all 0<=t<=r<=3 (10 cases).
PASS G4 motif: one defect has 21 faces; adjacent diagonal defects share exactly two equal 01 faces; separation >=2 is face-disjoint.
PASS G4 chain: N=1..64 gives A=17N+4, M=4N, ternary conserved unit current, neutral degree 2, charged degree 5, one connected component.
PASS G5 control: N=2 already has A/M=19/4 < 21/4; the family tends exactly to 17/4.
ALL PASS: component deletion/activity finite audit complete.
\`\`\`

The universal deletion theorem and all-N defect-chain statement rest on the
written proof. The execution is a finite exact audit only.
