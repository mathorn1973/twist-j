# P-QDD-PASSIVE-READING-FAMILY-1

Owner: A. M. Thorn, assisted by the Codex passive-family session, 2026-09-15.
Public work reservation: [issue #1015](https://github.com/mathorn1973/twist-j/issues/1015).

This preregistration concerns the first passive-family result only.
`PROOF.md` contains an independent exact proof; `verify.py` is its arithmetic,
typing and finite-source audit. Reading selection is a declared input.

The baseline is Public Canon v86, authority `mathorn1973/twist-j main`,
tag `canon-v86`, activation commit
`d008270c9c979f457f73087e17672b1db85ee6ad`, content commit
`56068ba4423a2ca38ce5760f1e34e82e2597f99f`, with CANON.md SHA-256
`cfec639d2f952bc8d38f565b5ffc01851e53b39e764e10e95cfb6a1581b11b61`
and 626540 bytes. This authority baseline was confirmed for the isolated
probe checkout before preparing the pin. This file does not claim a
preregistration commit or completed run until the corresponding public
records exist.

## 1. Equation

With `G=I-uu^T/5`, `u=(1,1,1,1)^T`, and `chi=(1,-1,-1,1)^T`, freeze

```text
P_t=uu^T/4,
P_l=chi chi^T/4,
P_r=I-P_t-P_l,
P_S=sum_(a in S)P_a,  S subset {t,l,r}.
```

The proposed mathematical result is: these three rational G-self-adjoint
projectors have ranks 1,1,2, are pairwise orthogonal and sum to I; their
eight subset sums form the chosen Boolean algebra, with
`P_S P_T=P_(S intersection T)` and `I-P_S=P_(A minus S)`.
The complete family of partitions into nonzero disjoint blocks in this
algebra has the following literal IDs and block order:

```text
PI-ALL    ((t,l,r))
PI-TRACE  ((t),(l,r))
PI-LEG    ((t,r),(l))
PI-PAIR   ((t,l),(r))
PI-ATOMS  ((t),(l),(r)).
```

For `v=beta_QDD(kappa)`, `Q=v^T v`, `s=sum_i v_i`, and `ell=chi^T v`,
the atom weights are `s^2/20`, `ell^2/4`, and
`((v1-v4)^2+(v2-v3)^2)/2`. Their sum is `m=Q-s^2/5`.
Each block returns the sum of its atom weights and, only for m>0, the
normalized data obtained by division by m.

The record has exactly five fields:
`partition_id`, `support_state`, `total_weight`, `block_weights`, and
`normalized_weight_state`. Equality is literal, including IDs, tags, order,
lengths and rational entries. The zero record is
`(pi,ZERO_SUPPORT,0,(0,...,0),ZERO_DENOMINATOR)`.
The supported record is
`(pi,SUPPORTED,m,(w_B)_B,NORMALIZED((w_B/m)_B))`.

For each refinement sigma<=pi, the coarsening map has domain the coherent
records bearing literal ID sigma, as defined in PROOF.md. It sums raw and
normalized block entries into the displayed pi order and preserves the zero
rule. The frozen equalities are

```text
C_(sigma,pi) R_sigma = R_pi,
C_(pi,tau) C_(sigma,pi) = C_(sigma,tau)  for sigma<=pi<=tau.
```

PI-TRACE must agree with the existing algebraic QDD total and ordered
LOW/HIGH weight slots on the same beta input; no equality of different
record schemas is claimed.

## 2. Code

The accepted exact verifier is `probes/P-QDD-PASSIVE-READING-FAMILY-1/verify.py`.
It uses the Python standard library, exact `fractions.Fraction` arithmetic
and finite matrices. It imports no earlier scientific verifier. Its source
and this preregistration are committed and pushed before any formal gate
execution. Their exact file hashes and preregistration commit are recorded
with the subsequent run evidence.

The mathematical proof is `PROOF.md`. Deterministic scientific stdout uses
LF and does not include timing, platform identifiers or machine-dependent
values. From the repository root the formal command is
`python3 probes/P-QDD-PASSIVE-READING-FAMILY-1/verify.py`. The local formal
environment is Ubuntu 22.04 on x86_64 with CPython 3.10.12; the required
architecture jobs use their declared Python 3.12 environments.
Execution must use non-optimized Python; the verifier rejects an environment
that disables assertions. Successful execution has exit code 0 and empty stderr.
The same committed EXPECTED.txt must be
matched byte-for-byte on both required architecture jobs.

Only compilation and static checks may precede the formal pin. Earlier
non-canonical prototype audits are development evidence, not executions of
this public probe and not substitutes for its pin or run record.

## 3. Carrier or data

The adopted decoder domain remains the existing K_QDD of complete pointed
native histories. The only weight source is the existing balanced head
factorization beta_QDD. The displayed Q^4 formula is the proof extension;
it does not enlarge K_QDD or change the ALGEBRAIC-DMATTER binding.

The finite audit uses the exact existing digit map
`ell(0,1,2,3,4)=(0,1,2,-2,-1)` and all `5^6=15625` native heads. It also
checks the 625 balanced vectors directly. The q,r head coordinates are
unused by the reading maps. No external dataset is used.

The declared audit inventory is:

| Check | Exact inventory |
|---|---:|
| Atom projector matrices | 3, with ranks 1,1,2 |
| Boolean subset projectors | 8 |
| Boolean intersection-product identities | 64 |
| Boolean complement identities | 8 |
| Atom coefficient-matrix identities | 3 |
| Displayed partitions | 5 |
| Independently generated partitions of three atoms | 5 |
| Balanced vectors, including zero | 625 |
| Balanced vector/partition records | 3125 |
| Supported raw/normalized branch comparisons against matrix pairing | 6240 |
| Native heads | 15625 |
| Native head/partition records | 78125 |
| Explicit q,r-invariance comparisons | 78125 |
| Refinement pairs, including identities | 12 |
| Refinement chains, including repeated elements | 22 |
| Record coarsening equalities on balanced vectors | 7500 |
| Record composition equalities on balanced vectors | 13750 |
| Coherent-record refinement checks beyond the balanced source image | 12 |
| Coherent-record composition checks beyond the balanced source image | 22 |
| Incoherent-record rejection checks | 6 |
| Literal input-partition-ID mismatch check | 1 |
| Non-refinement rejection check | 1 |

The proof covers all rational vectors and all coherent records at the
stated mathematical scope; finite inventories are implementation audits.

## 4. Systematics and scope controls

- Keep the source operator P separate from its quadratic coefficient form GP.
  The weight comparison is `v^T G P v`, not an untyped Euclidean substitution.
- Preserve literal atom order, partition IDs and block order; in particular
  PI-LEG gives `(11/16,5/16)` on v=(1,0,0,0).
- Preserve exactly five record fields. Coarsening acts only on coherent
  records with the indicated input partition ID. Normalized and zero tags
  must never be inferred from coincident numbers in a different record.
- Keep zero-weight blocks on supported records. Normalize only by positive
  total m, never by a block weight or by the zero-source total.
- Keep R_pi factored through beta_QDD. Reading no later state is a source
  dependency restriction, not a uniqueness theorem about other decoders.
- Completeness is restricted to the declared three-atom algebra. No full
  address-reader classification or physical apparatus class is claimed.
- The existing algebraic binding and the three physical QDD O obligations
  are not discharged by these passive L1 identities.

## 5. Failure threshold and dispositions

One admitted exact failure of any frozen projector identity, rank, weight
formula, literal record equality, total/zero rule, source factorization or
refinement/composition identity is sufficient to fail the corresponding
mathematical assertion. One omitted or duplicate member relative to the
declared family and its proof is likewise a failure. The threshold is zero
tolerance; there is no numerical approximation or adjustable fit.

A mismatch between PI-TRACE and the specified existing algebraic weight
slots is an admitted scientific failure. A malformed record outside the
declared coherent-record domain is not a counterexample to coarsening
totality on that domain; expected rejection is a type check.

Authority, pin, file-integrity, runtime or output-custody failures are STOP
conditions and must not be relabelled as scientific success. A verifier
defect or incomplete run produces no completed gate and no mathematical
disposition by itself. Completed scientific failures are preserved and
reported under the repository policy; thresholds and scope do not move
after the pin.

## 6. Action layer and proposed consequence

All asserted maps, fields and equalities are L1 algebraic snapshots.
The independent proof may support the proposed theorem
`QDD-THREE-ATOM-PARTITION-COMPLETENESS` at its exact scope after normal review.
Owner adoption of the five named views is a separate dictionary decision
for `QDD-OBSERVABLE-READING-FAMILY`; the proof does not make that choice.

No event generation, post-state instrument, occurrence law, probability
resource, pointer, reset or physical realization is claimed by this probe.
No L1-to-L4/L5/L6 lift is performed. Normalized rational tuples remain data.
Any Canon fold occurs separately with its own reviewed, complete scope.
