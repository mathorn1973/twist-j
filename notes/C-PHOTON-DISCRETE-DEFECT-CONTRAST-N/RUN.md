# Run record

**PUBLIC, NON-CANONICAL. Candidate-C audit only.**

- Claim: C-PHOTON-DISCRETE-DEFECT-CONTRAST-N
- Issue: #1220
- Immutable executed commit: \`f030586d0fd729f421e0f7e7c0540784d2527c09\`
- Execution lane: JAS 2 clean Git checkout
- Platform: Linux
- Architecture: aarch64
- Python: 3.12.3
- Process timeout: 45 seconds
- Exit code: 0
- stdout bytes: 371
- stderr bytes: 0
- Committed stdout match: YES

## Frozen file identities

- \`audit.py\` Git blob: \`e44cee20f08598f4b795e9bfa50e5c51fc6b0f1e\`
- \`EXPECTED.txt\` Git blob: \`917ac6afeb98404ee61bc6b8f428d05499ee7a02\`
- \`audit.py\` SHA-256: \`a0dd3621b4a68ed7f2ff27e27511fa8cada5270c8d373301851a11c2953108df\`
- \`EXPECTED.txt\` SHA-256: \`d3a3443b6717a1c8cd02ee1406c9ca78db90cf81c59aa8f6803935472c470564\`
- stdout SHA-256: \`d3a3443b6717a1c8cd02ee1406c9ca78db90cf81c59aa8f6803935472c470564\`
- stderr SHA-256: \`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855\`

## Exact stdout

\`\`\`text
LOCAL_DIFF PASS checks=10
GRAM PASS sources=125 link_fields=25 binary_chains=8
GALOIS PASS checks=500
REAL_SUBFIELD PASS checks=125 normalization_integer=YES
DEFECT_GALOIS PASS checks=375
INTEGER_COLLAPSE PASS controls=625 defects=375
AUDIT PASS; discrete_defect_identity=EXACT; binary_pair_gram=EXACT; integer_two_mode_reduction=EXACT; thermodynamic_floor=OPEN; P1=OPEN
\`\`\`

stderr was empty.

## Infrastructure attempts before evidence

Two earlier execution-tool invocations failed at the connector/transport layer before any process result, filesystem readback, exit code, stdout or stderr was returned. They are recorded in issue #1220 and supply no scientific evidence. They were not interpreted as PASS, FAIL or a completed scientific run.

The aarch64 run above is the first execution for which a scientific process result is established.

## Status ceiling

This run is one-architecture candidate-C evidence for the frozen algebra audit. It is not a two-architecture public gate and does not promote the written proof. The all-volume theorem remains candidate-T pending separate mathematical review. The thermodynamic floor and P1 remain open.
