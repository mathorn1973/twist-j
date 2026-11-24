# Validation and scientific scope

**NON-CANONICAL. L1. Analytical candidate-T; independent acceptance pending.**
Public claim: [#1749](https://github.com/mathorn1973/twist-j/issues/1749).

## Authority and prospective scope

Work began from freshly fetched public main and canon-v105
`892a0b11089d34e241e1eb76d2c03247022d18e6`, with declared content
`b8cdfd6ea58ae798545bc6000c817147fa0f0dcc`. Both ancestry relations were
checked. All five canon/SHA256SUMS entries match. In particular the Canon
has SHA-256
`73894f331dac3226fe30c86f1ccd893bc2761b0220557e0bfb374d049aa2fa31`
and the declared 1295029 bytes. The live baseline checks include successful
architecture-x86_64, architecture-aarch64 and aggregate check results.
The public STATUS, POLICY, AGENTS, CORE and FRONTIER were consulted; relevant
current claims, remote heads and the registry/probe inventory were scanned.

The public issue specified the local-Hamiltonian and preparation scope before
this branch's first commit. This is analytical notes work. No new verifier,
numerical experiment, synthesis execution, gate table, first-run record or
scientific replay was produced. The enormous finite gate catalogue is defined
by an exact algorithm, not claimed to have been physically built or generated.
A future executable validation requires its own prospective public pin.

Input candidate snapshots remain unchanged and unaccepted by this note:

- #1746: `01acc42b78f75095587765e9a5b91ee70dc28f37`.
- #1748: `ecb3460977cd2ee8a120797ffa53ba88cbe14171`.

Their successful checks, architecture replays or claimed numerical thresholds
are not new runs or independent acceptance of this construction. The positive
Hamiltonian theorem applies to the specified finite matrix word even if a
separate inherited source/spectral premise later fails; the physical capture
interpretation and inherited thresholds remain conditional on those premises.

The general history-computation and engineered state-transfer methods are
prior art. The proof supplies the particular geometry, positive full-space
operator and preparation/scope audit. See
[Christandl et al.](https://arxiv.org/abs/quant-ph/0309131v2) for engineered
perfect state transfer and
[Barenco et al.](https://arxiv.org/abs/quant-ph/9503016) for exact elementary
gate synthesis. The required identities and bounds are derived explicitly
in the companion files; no experimental implementation is imported from
these citations.

## Same-session mathematical review

Three delegated analytical contributions and cross-reads, followed by the
main session's assembled review, are part of this one working session.
They are not independent scientific review or authority to promote a claim.

Checks of the written derivation covered:

- Finite target dimension, integer energy-sector law, and the explicit
  reservoir preparation from a basis level with no discarded output.
- Registerwise binary encoding, exact QR/Gray-path synthesis, clean AND
  ancillas, wire restoration, invalid-code extensions and finite gate bound.
- The concrete fresh-row geometry, local clock guards, six-site support,
  bounded range and interaction valence; no distant shared clock wiring.
- Full-space positivity, the diagonal clock correction, the legal history
  gauge, the exact endpoint phase and time, reference uniformity, and the
  distinct global and legal-sector spectral bounds.
- Initial generator energy and variance, the physical timing bound, and the
  obstruction to coherent reservoir preparation from stationary resources
  under the old additive account.
- The default h=0 selectivity endpoint, restricted h>0 memory statements,
  and the distinction between logical checkpoints and physical-time storage.

Review identified a mismatch between two extensions of P_B on invalid
composite codes. The final convention is identity for every invalid target
code, as in COMPILATION.md; PREPARATION.md now distinguishes that convention
from its battery-only formula on the valid target carrier. Review also
clarified that the initializer leaves all ten raw label qubits free, with
the valid 676-dimensional source domain a separate promise, and made the
interface R_g=G_total and S=w explicit. These corrections do not change the
prepared valid-source target. No blocking defect remained in the reviewed
mathematical scope.

Final proof-file SHA-256 values after those clarifications:

| File | SHA-256 |
| --- | --- |
| COMPILATION.md | `f6cab1425c2ce8c1c838489a47471d1614b78dfac863f562ab234b0e4baddd92` |
| HAMILTONIAN.md | `294541642714f0c619195f175e71b06d8d6668c02b4214af6b78d9052000c851` |
| PREPARATION.md | `303b5439326ba2e63e1b845d56af4d512579ef84ba8f75a20adf8fbb1a72401f` |
| README.md | `d9a3e5e78ff18494d95e23d977c0b620bcb41d8db446e2e68a89df2a90914429` |

The main session applied and checked the final convention/ground-space
clarifications after the delegated cross-read; the file hashes distinguish
that final wording from earlier review snapshots.

## Repository checks and falsifiers

Existing repository-integrity commands completed with exit zero:

- `python -B tools/check_policy.py`: POLICY PASS.
- `python -B tools/check_canon.py`: CANON PASS v105, 577 claims.
- `python -B tools/check_ledger.py`: LEDGER PASS, 577 claims, 641 items,
  1160 dependencies, 577 evidence entries, 1124 history entries, 26 gates.
- `python -B tools/check_gate_contract.py`: GATE CONTRACT PASS, 26 gates.

These are repository checks, not verification of the new Hamiltonian proof.
Required CI and public readback of the published head are reported on its PR.
No new scientific computation is claimed by the notes-only change.

The local execution claim fails if its matrix factorization or source
encoding is wrong, a term exceeds the stated fixed geometric support or
valence, a raw-space Hamiltonian block is non-Hermitian/nonpositive, the
legal history space is not invariant, or the advertised endpoint, time,
energy or stability identity fails on an admitted data/reference input.
The preparation obstruction is restricted to stationary initial resources
and exact conservation of the stated additive account; a coherent source
outside those hypotheses does not falsify it.

Exact local coefficients, six-body interactions, ready-state resources and
the chosen continuous-time law are declared additions. Noise tolerance,
coefficient calibration cost, two-body reduction, autonomous preparation
from a specified thermal or dirty source, useful reset, a native spatial
encoding and identification of a physical battery energy remain open. The
logical release buffer is not promoted into physical-time permanent memory.

Only authored English scientific notes and public citations are included.
No Canon, registry, policy, workflow, predecessor branch or threshold is
changed. No merge, scientific promotion, experimental realization or law of
individual outcomes is claimed.
