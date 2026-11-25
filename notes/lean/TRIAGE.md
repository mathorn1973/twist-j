# Triage of the L1 T rows of Public Canon v117 for Lean

NON-CANONICAL. Working triage, no authority. Changes no status, scope or evidence.

Source: mathorn1973/twist-j @ 6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed, canon/REGISTRY.tsv, rows with status T whose scope names L1: 255 of 483 T rows.

## Method

Two axes, assigned by a keyword script on the positive part of each scope (text before the first exclusion clause such as "no decoder ..."), then spot-read.

1. Vocabulary: which definitions must exist in Lean before the statement can even be written. First matching cluster wins, from V8 down to V0. Keyword-based as well, but far more stable than the difficulty axis.

2. Difficulty: E explicit finite object or ring identity, S universal statement on standard Mathlib infrastructure, H analytic, conditional, classification or model-dependent. This axis is a first machine pass and misjudges single rows; it must be read before a row is scheduled.

## Counts

```
cluster     E    S    H  total  vocabulary
V0         13    1    3     17  general mathematics, no TWIST vocabulary
V1         14    3    3     20  J kernel identities, Z[j] contact algebra
V2         16    4    5     25  Z[zeta_5]-modules, CM pencil, Galois, Hodge, F5 linear algebra
V3          7    3    2     12  Q(sqrt5), Z[phi], ideals, quadratic characters
V4          3    7    1     11  Thue-Morse, carry, arithmetic functions
V5          3    1    0      4  five-cell register Q^5 / Z^5
V6          3    1    0      4  QDD lattice Z^4 with G=I-uu^T/5
V7         31    8    6     45  native update U on N0 x F5^6
V8         66   18   33    117  model vocabulary: decoder, record, energy, QDD apparatus
all       156   46   53    255
```

## Reading

- 162 of 255 rows (V7 and V8) cannot be stated until the TWIST vocabulary exists in Lean: the native update on N0 x F5^6, its counter and checkpoint, readouts, records, ports and energy accounts. Writing those definitions is the statement surface; it is where a wrong formalization would silently prove the wrong thing, so it needs owner review before any proof work.
- 93 rows (V0 to V6) need only Mathlib plus a small kernel: Z[zeta_5], Q(sqrt5), F_5 linear algebra, arithmetic functions. These are the first proof wave.
- Section 1 of the Canon (the axiom and the two projections) is partly covered by the layer-0 kernel: J-GOLDEN-BRIDGE fully (J phi = j, (J-1)^3 = j, J^5 phi^5 = 1); the ring-level parts of J-STEP (step formula, characteristic polynomial), J-MODULUS-CHORD (J Jbar = 2 - phi, (2 - phi) phi^2 = 1) and J-TENTH-ROOT ((1-J)^5 = -1). Open there, each a separate obligation:
  1. det M_J = 1 and trace M_J = 3 for the 4 x 4 integer matrix (J-STEP);
  2. Algebra.norm J = 1 and Algebra.trace J = 3 in Q(zeta_5) (J-UNIT, J-STEP);
  3. the tie det M_J = Algebra.norm J, which the Canon states in one line but which joins two different objects and must not absorb either of them;
  4. 1 - J has exact order ten, i.e. primitivity, not only (1 - J)^10 = 1 (J-TENTH-ROOT);
  5. the archimedean statements of J-PROJECTIONS;
  6. O_K^x = mu_10 x phi^Z.
- Not in this triage: the 228 T rows whose scope does not name L1. Most carry a physical dictionary or a higher layer and are outside a first Lean wave.

## Files

`TRIAGE-L1-T.tsv`: one row per claim, columns vocabulary, difficulty, claim_id, canon_section, evidence, full scope.
