# PREREG-AUDIT-QDD-TERMINALITY-1-CORRECTION

```text
KIND:       correction leg for the already-executed audit
            AUDIT-QDD-CENTRALIZER-TERMINALITY, opened in response to the
            owner review of 2026-08-20.
ORDER NOTE: the review is written as a PRE-RUN verdict. The audit had already
            been executed and published when the review arrived. This leg
            therefore corrects by addendum. No pinned artifact of the first
            leg is altered, no threshold is moved, and the first leg's
            recorded stdout stands as recorded.
AUTHORITY:  none. NON-CANONICAL. No repo normative edit, no registry motion,
            no probe, no fold. O1 and O2 stay open. SAMPLING NOT PROVIDED.
LAYER:      L4 apparatus/support only.
DATE:       2026-08-20
DISCLOSURE: RESULT-EXPOSED / IMPLEMENTATION-INDEPENDENT / NOT BLIND.
            The audit is independent in implementation and derivation. It is
            not blind: the sealed result and its expected structure were known
            in advance.
```

## Current authority

```text
CURRENT_AUTHORITY:
  STATE:          ACTIVE
  CANON:          Public Canon v57
  AUTHORITY:      mathorn1973/twist-j main
  TAG:            canon-v57
  CONTENT_COMMIT: 8e8b04abe4d3359942449533854ef1d142be70df
  CANON_SHA256:   c96a2ef52c78d68ef8f04b582e4a17328e6a863b49664f29b1bd324171d802a8
  CANON_BYTES:    295013
  MAIN_AT_AUDIT:  4ef54f0c34f80897af0121a2d93b710e70a8377c

AUDITED_OBJECT:
  PROBE:          P-QDD-J-CENTRALIZER-TERMINALITY-1
  ISSUE:          459
  PR:             462
  PIN_COMMIT:     e1cf7394279d07318571f99d1c81762919a761f9
  RESULT_COMMIT:  936a396d57a659e45c8e5c3923aaa19896306662
  FINAL_PR_HEAD:  aef78f6815fc874eb2d759b025789d16b95cb6fe
  MERGE_COMMIT:   4ed6cb72ab1110b68ed0574115e9dacbaf65e954

BASIS_RELATION:
  the audited probe directory is byte-identical between its sealed merge and
  current main;
  canon/ is NOT byte-identical, because Public Canon v57 has since activated;
  the relevant QDD-INSTRUMENT-APPARATUS row remains O and unchanged in its
  selection and sampling boundary.
```

The first leg executed from a clean checkout whose HEAD was exactly
`4ed6cb72`, the audited merge. That is recorded here and machine-checked
below rather than asserted.

## Gates of this leg

Chain of custody, replacing the file-hash-only QF1 of the first leg:

```text
CH1 (QF1a)  pin commit is an ancestor of result commit, final PR head and
            merge commit.
CH2 (QF1b)  the three pinned blobs are byte-identical at all four commits.
CH3 (QF1c)  EXPECTED.txt, RUN.md and RESULT.md do not exist at the pin.
CH4 (QF1d)  no pinned file changes after the pin.
CH5 (QF1e)  current-main copies of all six sealed files equal the
            merge-commit copies.
CH6 (QF1f)  the audit checkout worktree is clean.
CH7 (QF1g)  the audit checkout HEAD is exactly the audited merge commit,
            not a moving main.
CH8         basis disclosure: canon/ differs between the audited merge and
            current main, and the QDD registry row is unchanged. Both facts
            are asserted as a pair, so neither can be quoted alone.
```

Machine complements to the written proofs supplied by the owner review. The
proofs are the load-bearing objects; these gates certify their finitely many
matrix inputs:

```text
PR1  sharp coordinates: R and C are self-sharp and J^sharp = -J, hence by
     linearity T(e,r,s)^sharp = e R + r C - s J for every rational e, r, s.
     Self-adjointness therefore forces s = 0 at once, with no sampling.
PR2  effect coordinates: the multiplication table gives
     T^sharp T = e^2 R + (r^2 + s^2) C by linearity, so the effect equation
     is exactly e^2 = 1 and r^2 + s^2 = 1.
PR3  projective idempotence, the universal step in representatives:
     from T^sharp T = Q_k and T^2 = eps T with eps in {+1, -1},
     left multiplication by T^sharp gives T^sharp T^2 = (T^sharp T) T =
     Q_k T = T and also T^sharp (eps T) = eps Q_k, hence T = eps Q_k.
     The converse is immediate. The gate certifies Q_k T = T for the class
     and the associativity inputs; the three-line argument is written, not
     sampled.
PR4  quotient well-definedness: (+/-A)(+/-B) = +/-(AB), so T ~ -T is a
     congruence for composition and the post-state quotient is a group with
     identity [Q_k]; the only idempotent of a group is its identity.
PR5  non-terminal involution witness: for T = R_k - C_k and w = w_R + w_C
     with w_R, w_C nonzero in the two summands, T w = w_R - w_C and
     T^2 w = w_R + w_C are not on one rational line, while T^2 = Q_k.
     Involutivity is therefore not terminality.
```

Falsifiers of this leg:

```text
QF3a  the universal projective-idempotence reduction fails;
QF3b  the explicit R - C non-terminal involution witness fails;
QF3c  quotient multiplication is not well defined under T ~ -T;
QF1x  any chain-of-custody gate CH1 to CH8 fails.
```

## Decision vocabulary and return codes

```text
AUDIT-PASS
  no gate fires; the corrected claims stand at their declared ceilings.
AUDIT-DISAGREEMENT
  a mathematical gate fires with an exact witness; a finding against at
  least one sealed statement, subject to chain-of-custody diagnosis.
AUDIT-INTEGRITY-STOP
  a chain-of-custody gate fires, the basis is wrong, or the leg is
  incomplete. No scientific finding is stated.

return codes   0 AUDIT-PASS, 1 AUDIT-INTEGRITY-STOP, 2 AUDIT-DISAGREEMENT
```

The program does not fail fast. It collects every gate in fixed order,
prints every available exact witness, and returns the code at the end.
Output carries no time, path, host, or other variable datum.

## Freeze

This file and `audit_qdd_chain_1.py` are frozen together, before any
execution of the program, and their pin is recorded in
`AUDIT_PIN-CORRECTION.txt` with sha256, byte count, LF count, CR count and
final-LF flag for each. Static compile check only before the freeze, with no
import and no execution. Exactly one run follows the pin. Timeout for any
subprocess is 120 seconds; exceeding it is AUDIT-INTEGRITY-STOP without
retry.

## What this leg does not do

It does not re-run the first leg, does not alter its files, does not change
any earned label except by supplying the written proofs the owner review
requires, and does not move O2. Deriving projective idempotence from the
typed composition of fresh apparatus, irreversible record and the
no-feedback rule remains the open question.
