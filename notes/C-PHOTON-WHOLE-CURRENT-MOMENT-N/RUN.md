# RUN — C-PHOTON-WHOLE-CURRENT-MOMENT-N

**Status:** candidate-C audit only. Not a formal public probe and not a two-architecture scientific gate.
**Owner:** #1198.

## Frozen custody

- preregistration commit:
  \`769a55d44ff71b7cacc4bebbeedf300b3982ec8b\`
- verifier commit before first run:
  \`a290193b6352d60eb28b5072d5394888f5a52336\`
- verifier blob:
  \`a789f85c530ff776653b8f92e747f99bb54efe8a\`
- verifier SHA-256:
  \`c59f428666e8a9c8edc47347468661f48b73ca4821280c0a1c1520df51bdf6ac\`

Both PREREG.md and verify.py were read back from GitHub before execution.

## First clean-clone execution

\`\`\`text
architecture: arm64
python: Python 3.9.6
head: a290193b6352d60eb28b5072d5394888f5a52336
verify_sha256: c59f428666e8a9c8edc47347468661f48b73ca4821280c0a1c1520df51bdf6ac
exit_code:0
stdout_bytes:378
stderr_bytes:0
\`\`\`

Exact stdout:

\`\`\`text
PASS G3: exhaustive cyclic zero-sum sources L=2..7, entries -2..2 (10376 sources) satisfy 4 ell <= L ||B||_1.
PASS G6: opposite winding-loop source saturates ell=M^2/8 for every even L=4..20.
PASS G8: M^3 tail identity verified exactly for M=1..1000.
PASS G10: among odd primes p<=101, D=p-1 and p=2D-3 intersect only at p=5, D=4.
ALL PASS: whole-current moment audit complete.
\`\`\`

A second clean-clone ARM execution after the written proof was committed used
the same verifier SHA-256 and produced the same 378 stdout bytes with empty
stderr. This is same-architecture reproduction only.

## Audit scope

The finite audit checks examples and exhaustive finite instances of G3, G6,
G8 and G10. The all-size mathematical force of G1-G8 and G10 rests on the
written proof, not on this execution.

No uniform probabilistic bound on R3(L) is audited or claimed.
