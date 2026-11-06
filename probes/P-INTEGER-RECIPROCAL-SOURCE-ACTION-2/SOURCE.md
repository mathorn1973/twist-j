# Source and choice manifest

Status: NON-CANONICAL  
Action layer: L1  
Probe: P-INTEGER-RECIPROCAL-SOURCE-ACTION-2  
Ownership: https://github.com/mathorn1973/twist-j/issues/1642

## Normative authority actually read

Public Canon v103, active main and peeled tag canon-v103:
dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d.
Declared content commit: 01fb76f6b3b14a6a5ec05d0017ea922390ab6f66.
The content commit is an ancestor of the active base.

The following bytes were read and independently hashed before preparation.
Both verifiers check this exact five-file manifest during execution.

| Path | Bytes | SHA-256 |
| --- | ---: | --- |
| canon/CANON.md | 1052518 | d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b |
| canon/CORE.md | 30714 | 9d5617a163bc7a4e1964d41861ff7f2f44009117c61debe08a4e1547c88be728 |
| canon/FRONTIER.md | 27382 | 8574c3d4b0cc70278dec7d64e2a51022718cc54497c64025d9e6021775fcbaf0 |
| canon/REGISTRY.tsv | 532811 | 5cd008147435bf1facfe93b2e05d9d7e41554d73f647ad09659aac002195890d |
| canon/CHANGELOG.md | 207770 | 79f6bd8f30b1f845ae918b7374049f4bf8e0a2270e89b4c5223469a93855f078 |

The active-base POLICY.md hash is
da5d2cf5a021f4d069c471725e02b6d2c201e3acadd5ecfd4213a361184b7a5d;
AGENTS.md is
7363b83ca6d822ec35e8465fe64c1aa8cd0007bf8b99ae599c265cc49fcee6e1.
The current authority check runs inspected were main push 39022927713,
tag 39022952253, and release 39033710211, with successful required checks.
These are authority receipts, not this probe's computational evidence.

Canonical input:

- [DEF-K1-LINEAR-METRIC and K1-LINEAR-METRIC-COMPLETION](https://github.com/mathorn1973/twist-j/blob/dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d/canon/CANON.md):
  the ten words, their two initial slices, rational L, the marked plus-TT
  metric reader, the full quadratic comparison action, its derivative
  branch, and the all-counter free bound -59/100<h<99/100.
- The same authority defines the cyclotomic arithmetic used here.
  All source gates, coupling-selection properties, reciprocal backreaction
  laws, and joint-action identities are restated and proved self-contained
  in this probe; no foreign branch is a runtime dependency.

The canonical completion theorem is used only at its selected free-K1
scope. It is not cited as a theorem for the new reciprocal forced
recurrence. PROOF.md derives the additional all-counter bound needed for
the reciprocally forced recurrence.

## Non-canonical companion provenance and consumed predecessor

1. [P-INTEGER-SOURCE-HOLONOMY-1, PR #1633](https://github.com/mathorn1973/twist-j/pull/1633):
   ownership #1632, pin b3de2d7886a00bc7d6b2f5fe470516424be8b046, head
   1ffe24aab9f4bbe070dfbb23b914244c9b68aa02. Source: six-phase integer
   Hermitian holonomy, occupied detector, and funded reflection theorem.
   Its [independent review](https://github.com/mathorn1973/twist-j/issues/1632#issuecomment-6262097998)
   accepted its declared NON-CANONICAL L1 scope.

2. [P-INTEGER-K1-SCALED-BRIDGE-4, PR #1639](https://github.com/mathorn1973/twist-j/pull/1639):
   ownership #1635, pin fda020d27b2ea57eafe143a2bc7a3b59a52ef6ce, head
   78fa5a663632e2b0733c6bafe0a6cda7f8bb5379.
   Its completed PASS and immutable files are left intact. The
   [review receipt](https://github.com/mathorn1973/twist-j/pull/1639#issuecomment-6263553901)
   distinguishes its valid declared scaled arithmetic from a wrong frozen
   source manifest, summary defects, and a shared-bank interaction that
   does not change the field at fixed counter.

3. [P-INTEGER-PRIMITIVE-SOURCE-METRIC-1, PR #1641](https://github.com/mathorn1973/twist-j/pull/1641):
   ownership #1640, pin 7ffee4939346221e2d43ed386f33bdfa47cd509f, head
   af88c702baf6c31bf4bb51c9768a07bc261c3dc6. Source: primitive-carrier
   one-way source-to-metric forcing, all-counter denominator theorem,
   uniform Lorentz signature on the twenty ready histories, and
   prescribed-source quadratic metric action. Its
   [independent review](https://github.com/mathorn1973/twist-j/issues/1640#issuecomment-6265271658)
   accepted its declared NON-CANONICAL L1 scope and recorded the remaining
   obligations addressed here: structural justification of the coupling
   choices and reciprocal source-metric dynamics from a joint action.

4. Consumed predecessor [P-INTEGER-RECIPROCAL-SOURCE-ACTION-1, PR #1643](https://github.com/mathorn1973/twist-j/pull/1643):
   ownership #1642, pin a369fbf85feb79a2a10716b8bd7efd9ff8da5814, closure
   commit 511ad2f1. On its first post-pin invocation, verify.py completed
   with exit code 0, empty stderr, and stdout FALSIFIER=INITIAL_DATA /
   RESULT=FAIL (SHA-256
   31e352459901a944bccf26ddae6b75408a9a986f2c66ce770080c823f634444a)
   because the literal beta(w) table column transcribed 0 instead of +1
   for word 0100 and 0 instead of -1 for word 1101. Per POLICY.md Section
   3, that completed FAIL is preserved on its own branch with its exact
   EXPECTED.txt, RUN.md, and RESULT.md, and the corrected table is
   retargeted here under the fresh identifier
   P-INTEGER-RECIPROCAL-SOURCE-ACTION-2 with its own prospective pin.

The earlier scaled-bridge identifiers -1, -2 and -3 are consumed abandoned
pins on their own branches (pins
632f59e97c169abe937e00a6d92642f32378d767,
fd4e5a2734fd99d94480b6bef30d2c657f6debc3, and
989c4ba195d1e6a5ecce9baed437ae2fa1372543, disposition PRs #1636, #1637,
and #1638). None of those foreign branches is modified or used as runtime
evidence.

## Choice ledger

| Item | Origin and scope |
| --- | --- |
| Five labelled sites, ten words, initial slices, free C and marked TT reader | Selected canonical L1 inputs, with their stated restrictions |
| Hermitian source, reference and detector registers | NEW_DECLARED apparatus, inherited as non-canonical context from #1633 and #1641 |
| Primitive P,Q,k carrier and special first divisor | NEW_DECLARED encoding from #1641; extended here to reciprocal phase-6 coupling |
| Structural classification of chi, ell, factor 2, and 324^n attenuation | New L1 theorem (B2) within the declared apparatus class; marked site pair {0,1} and sign orientation remain explicit context choices |
| Reciprocal phase-6 update s' = s + lambda Phi(P,Q) | NEW_DECLARED modulo-2 scale-invariant backreaction gate; exact inverse proved on the full integer carrier |
| Secular-resonance no-go for unattenuated numerator feedback | New L1 proof explaining why scale-compatible modulo-2 reduction is required for all-counter Lorentz stability |
| Joint quadratic action A_joint[V,ell_0,N,chi] | NEW_DECLARED joint metric-and-source action; exact metric stationarity and O(324^-(2n-1)) integer-lattice source stationarity proved |
| lambda=0, a=0, and one-way prescribed-source controls | Frozen negative and comparison controls; no post-result selection |
| E, nonnegative bank, direction, phase, reflection | NEW_DECLARED arithmetic cost and admission dynamics |
| Bound for all 30 ready reciprocally coupled histories | New L1 proof (-299/500<h<499/500); finite replay is its audit |

No external measurements, parameter fits, random seeds, native-U
modifications, physical units, or physical acquisition clock are used.
The register R is an apparatus reference, not a Riemann tensor. The field
counter k is an exact precision/history index. Metric equality is literal
at the declared sites, polarization, source context and counter.

## Implementation independence and metadata

The primary verifier uses a four-coefficient polynomial quotient, conjugate
matrix multiplication, and rational recurrence. The breaker verifier uses
direct eight-coordinate source gates, explicit five-by-five C and L
matrices, and separate check routines without importing the primary
verifier or PROOF.md. Both were authored in the same assisted session from
the common mathematical specification PREREG.md; this shared session
context is disclosed transparently rather than presented as a separate
human laboratory. Neither imports the other.

Static review and compilation precede the pin; execution follows remote
pin readback. The primary compares the breaker's raw subprocess stdout
bytes without normalization.
