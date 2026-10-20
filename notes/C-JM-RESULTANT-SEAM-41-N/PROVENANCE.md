# Source custody and publication audit

Status: NON-CANONICAL, publication-only packaging. Custody: issue #1670.
The source is the completed `PROMO-C-JM-RESULTANT-SEAM-41-N.zip` supplied in
this conversation, not an authority source for the public Canon.

Source ZIP SHA-256: `b0f68423977f1f30a196f4445de243097747a5f9543110fefa69cbe0ebd8e2f3`.
Source REPORT.md SHA-256: `c0a029bcc4fd2bdc24ee499c0493438418c0a9d290c571b3d504c752b25da520`.
All original manifest entries were verified before packaging; the separately
attached report matches the report inside the ZIP byte for byte.

## Source run and exposure

The source records Linux, x86_64, Python 3.13.5, SymPy 1.14.0, exit zero and
empty stderr for all three final scripts. The author exposed the product,
resultant and four counts before the audit. The local preregistrations were
not public Git pins; their original statements about no repository write refer
to that source execution, not to this subsequent archival PR.

This package makes no independent-agent, blind confirmation or scientific
two-architecture claim. Replaying the same source is reproduction only.

## Byte-identical imported evidence

| File | Original SHA-256 |
|---|---|
| `PREREG.md` | `10229e35ea439d892a6013f222b657b338301f23427a9c9c86dcf63c97e28916` |
| `SEAM-SUPPLEMENT-PREREG.md` | `3f25b721c4ee15584f2e5a525b1dc9536dd041015709a783eaf165d0ddd3257c` |
| `audit.py` | `d7ce8d35fee2aaf987ebffa617b272101321d4a677883627dbc763f6556b73c2` |
| `conjugation_audit.py` | `9cf12e50d8c6d85dabea220705b1e83c796d247b2ee84211a3bf2a0b4d8de272` |
| `supplement.py` | `8f6da638c616c889d971d5d92c5a45429dc678cd61eeeaeed7108488ab515925` |
| `ACTUAL.txt` | `135306f3d58f14de3ba0f82cdf68ddf234b095bfbb1770430a8a74311d377fa4` |
| `CONJUGATION-ACTUAL.txt` | `eca35a70e1053f7610e6acc450e44c1efa4697e5f898464d279bfadf5e414e55` |
| `SUPPLEMENT-ACTUAL.txt` | `cebbeb2f20a430f6ca0e8331a52c8feb613c422a904e438ef6f7218e1e57467f` |

## Publication-only changes and exclusions

REPORT.md sections 1 through 9 are unchanged. Its opening now distinguishes
the historical source run from this publication. Section 10 points to this
custody note and the replay wrapper instead of promising to publish intermediate
code/output. The mathematical claims, equations, counts and thresholds did not
change. README.md extracts the already completed statement and its boundaries;
PROMO records disposition only; replay.py only checks stored bytes and replays
the unchanged scripts. SHA256SUMS is regenerated for this published subset.

The binary ZIP, superseded `audit_initial.py`, intermediate `ACTUAL_initial.txt`,
empty stderr files and source implementation diary are not committed. Their
source integrity remains bound by the original ZIP hash. Source RUN.md is
summarized above rather than duplicated as a new formal run record.

The source correction is preserved here because it affects interpreting the
successful evidence: an initial report-only conversion used integer truncation
on a rational residue and printed 21 for conjugate M. Exact modular denominator
inversion gives 7, agreeing with the separate direct cyclotomic calculation.
No mathematical falsifier changed. The exploratory exponent 820 was replaced
by 1640 after determining the multiplier's order 40. The final archived scripts
and successful outputs already contain these corrections.

## Publication validation

Public comparison basis: `e7fe4e38048cdb6019df0599b47ad20a952475a9`.
Public Canon v103; content `01fb76f6b3b14a6a5ec05d0017ea922390ab6f66`.
Canon SHA-256 `d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b`,
1052518 bytes. No authority or normative file changed since the source analysis.
Both ancestor checks, five normative hashes and existing public architecture
and aggregate checks pass. POLICY, CANON, LEDGER and GATE CONTRACT checks pass.
The remote ref scan and tracked/current-candidate searches found no competing
claim; the distinct ramified-C40 note is identified in README.md.

Local publication replay uses the same Linux/x86_64, Python 3.13.5 and
SymPy 1.14.0 environment. The replay outcome is recorded below only after
execution. This is not another architecture or independent implementation.

## Public safety

Only the named English text, original mathematical code and successful
scientific outputs are included. No credentials, private addresses/hostnames,
user messages, private paths, machine names, compiled files, binaries,
third-party source code or erroneous intermediate output are published.
SymPy is a named replay dependency; no vendored library or paper text is
included. The repository's Apache-2.0 terms apply to this contributed material.
All files remain well below the 5 MiB limit.

## Completed publication replay

The unchanged three scripts exited zero with empty stderr. Each stdout
matched its archived counterpart byte for byte (2213, 1227 and 511 bytes).
The wrapper stdout was 207 bytes, SHA-256
`e77d5414bfdc5d7d417ccdc3c9faf1fc06158d3642c0685abfa20845aa3cddad`.
This same-environment replay is reproduction only. The manifest was
regenerated afterward solely to bind this added custody record.
