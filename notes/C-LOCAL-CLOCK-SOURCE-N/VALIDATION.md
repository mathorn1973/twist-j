# Validation, custody and falsifiers

**NON-CANONICAL, L1, conditional analytical candidate-T.**
Independent mathematical acceptance is pending. Public reservation:
[#1755](https://github.com/mathorn1973/twist-j/issues/1755).

## Authority and fixed input

The branch starts from freshly fetched main/canon-v105
`892a0b11089d34e241e1eb76d2c03247022d18e6`, with declared Canon content
`b8cdfd6ea58ae798545bc6000c817147fa0f0dcc`. Current STATUS, POLICY and AGENTS
were consulted and live branches, public issues and active work were checked
for overlap before the public reservation. The normative Canon is 1295029
bytes, SHA-256
`73894f331dac3226fe30c86f1ccd893bc2761b0220557e0bfb374d049aa2fa31`.

The fixed direct candidate input is PR #1754 at
`89f69e40f6ccfd950bf2e6c446ec38bc51f7f71b`, in particular its SHARP.md,
COMPILATION.md, HAMILTONIAN.md and NATIVE.md. Its source and accepted-channel
premises come from:

- #1746: `01acc42b78f75095587765e9a5b91ee70dc28f37`;
- #1748: `ecb3460977cd2ee8a120797ffa53ba88cbe14171`;
- #1752: `e19b07183c3e4841e18c8913de7c4c83429b94f3`.

These inputs are not changed or independently accepted by this note.
The conditional margins remain the ones proved for the selected source and
physical output, not new spectral assertions about the finite box. The
Hamiltonian and loading lemmas are analytical statements about the specified
finite circuit even if a separate inherited spectral premise later fails.

The public claim described the source-cursor route before the first commit.
The finalized construction includes a counted idle loading runway, a local
completion latch and an idle output tail. There was no scientific executable,
simulation, coefficient-table generation or new verifier run. This is notes
work under POLICY section 5. A future computational audit must have its own
prospective public code/protocol pin before execution.

## Proven claims and review boundary

The proof supplies a particular finite local Hamiltonian, an explicit
initial source state, full-space positivity and conserved excitation counts.
It derives an approximate loading interval, an exact computation endpoint,
a conditional accepted reduced channel and finite conditional retention.
It does not prepare the exact previous domain-wall clock as an independently
usable output, or produce a nonstationary closed state from a stationary one.

The general engineered state-transfer and history-clock methods are prior
art; see [Christandl et al.](https://arxiv.org/abs/quant-ph/0309131v2) and
[Breuckmann and Terhal](https://arxiv.org/abs/1311.6101v3). The present
construction explicitly proves its own source, geometry, energy partition
and preparation interfaces. It does not claim a new general clock method or
import a material realization from those references.

Delegated derivations and cross-reading, followed by the root session's
assembled review, are all part of the same working session. They are not
independent scientific acceptance. Review targets include:

- The n_j+n_(j+1) positive edge formula on 00, 01, 10 and 11 sectors;
  no positivity argument is restricted silently to one cursor.
- Exact source/runway/active/latch/tail indices, physical site coordinates,
  collision-free embedding, seven-site support and bounded valence.
- Separate conservation of cursor and data/latch charge, with two extra
  initial excitations and all existing data fuel/work still counted.
- The source's complete epsilon+g energy, positive launch/rest partition,
  and the distinction between an actual fixed H and comparison H_sep.
- The mixed-input commutator, global binomial energy distribution, and why
  nonzero variance alone would not certify a nonstationary resource.
- Full-state loading trace distance sqrt(delta), distinct vector-norm
  bound sqrt(2 delta), and the sharper reduced-data error bound.
- The physical latch's exclusion of unfinished compiler prefixes, exact
  reduced accepted channel, rederived time scale and post-read continuation.
- The limited native-law conclusions and the openly supplied source/contact
  initial condition. The old initially noncommuting term was already local.

## Reviewed proof bytes

SHA-256 of the UTF-8/LF proof files in this candidate, after same-session review. This manifest does not hash itself; Git identifies all six published files.

| File | SHA-256 |
| --- | --- |
| HAMILTONIAN.md | 25998d9cb0085922335ecc716a47e49b61b61dba8177bb237d54790ccebcb554 |
| SOURCE.md | 5772097d155d2041e2771a5b182a6bff76937308e83b3759954d7ddb09622852 |
| PREPARATION.md | f8e90f26f6a510f7a864111f73d1ce365cfcc2ed1ffc785ac82247ba5cddd8e1 |
| NATIVE.md | 8ccdcc80b99c3d5dd17652bd48fc89838c659116b692a1bd1c5d16df34ad37a1 |
| README.md | a71364707b2b36c2357f4d979bf960d4e84ba077cd0d4296ab85fc06ebc31850 |

## Repository checks

Existing repository checks are recorded here and on the final PR. They
are integrity checks, not verification of the new analytical proof:

- `python -B tools/check_policy.py`: POLICY PASS.
- `python -B tools/check_canon.py`: CANON PASS v105, 577 claims.
- `python -B tools/check_ledger.py`: LEDGER PASS, 577 claims, 641 items,
  1160 dependencies, 577 evidence entries, 1124 history entries, 26 gates,
  7 programs.
- `python -B tools/check_gate_contract.py`: GATE CONTRACT PASS, 26 gates.

The published PR reports the required architecture jobs and aggregate check,
actual log readback and exact published-file custody. No new scientific
VERIFY or REPRODUCE result is claimed for this notes-only contribution.

## Falsification and residual obligations

Any invalid raw-space positive block, charge-changing primitive, incorrect
geometric support, failed one-cursor invariant sector or failed gauge identity
would invalidate the constructed Hamiltonian at its stated scope. The source
claim fails if the empty device runs without a source under the specified
initial data, the first bond is not the complete initial commutator, the
launch/rest partition is not positive, or the counted source/interface
energy does not vanish at the endpoint.

The loading claim fails if the specified runway interval violates its
binomial-weight bound or the complete-state metric is confused with the bad
weight. The output claim fails if unfinished prefixes can pass the latch,
if any retained physical degree of freedom changes the traced auxiliary
energy label, or if the stated normalized post-read continuation exceeds its
bound. A physical measurement mechanism is not silently substituted for the
mathematical conditioning in that claim.

The preparation boundary is deliberately not eliminated: clean empty
hardware, the occupied source, charged data and latch, exact couplings and
continuous-time evolution are supplied. Acquisition of the source/contact
state from a specified environment, cooling, precision/material implementation,
noise robustness, native observable/dynamics intertwiners, useful reset and
individual outcome occurrence remain open. These are not asserted outputs
of the present construction.

All tracked files are new authored English scientific notes with public
citations. No Canon, registry, policy, workflow, predecessor or threshold is
edited. The staged paths and text were checked for private infrastructure,
credentials, transcripts and third-party code. No merge or promotion is
part of this candidate.
