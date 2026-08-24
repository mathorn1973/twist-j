# P-TM-HANKEL-K3-TRANSFER-1 result

Date: 2026-08-11

## Decision

```text
TRANSFER-K3-PASS
```

All 31 preregistered gates passed with exit code 0 and empty stderr on the
local aarch64 formal leg, and the identical 1808-byte stdout was reproduced on
a second architecture (x86_64) before this record was committed. The
repository-required GitHub x86_64 and aarch64 jobs rerun the pinned verifier at
pull-request time; the probe evidence gate is complete when they reproduce the
committed `EXPECTED.txt` byte for byte. **Canon status: unchanged.** This probe
PR creates no Registry or Canon claim.

## Frozen scope decided

Within the preregistered L1 scope, at computation grade (C):

```text
G1  Squareful-defect parity. On 246 prime sets, extremal and not: the
    defect R has zero empty row and column, its nonempty block is I
    modulo 2 with odd determinant, every intersection-layer operator is
    I modulo 2 with odd determinant, and the layer inversion
    K(S,T) = sum over V subset (S AND T) of d_V(S XOR T) holds
    entrywise. No low-rank compression of the squareful defect exists
    at this scope.
G2  Integral Witt form. On all 1109 extremal sets tested (1103 pairs
    with p < q <= 1000, four triples, two chains at k = 4, 5):
    W^T Kxor W = diag((-1)^(|S|+1) 3^(|S|)) exactly, and W^T R W keeps
    the empty split and the parity form.
G3  The k = 2 pencil. The 4 by 4 W-basis collapse and the corner bound
    |3D + 3E + F| <= 7 hold on all 1103 pairs; exact root isolation on
    the first 128 pairs finds zero pencil roots in (0,1) and balanced
    inertia NEG 2 ZERO 0 POS 2 at s = 0, 1/2, 1.
G4  The k = 3 falsification. The witnesses 147965 = 5.101.293,
    1942781 = 83.89.263, 11743733 = 149.269.293 are extremal with K
    inertia NEG 5 ZERO 0 POS 3 by two independent exact paths,
    determinants -3840, -768, -9856, pencil constant term 3^12, and
    exactly one pencil root in (0,1) each. Among all 157 extremal
    triples with n <= 200000 exactly one is nonbalanced; among the 99
    triples with p < q < r <= 300 exactly three fail.
G5  The abstract k = 3 classification. Local rigidity bounds (32 and 16
    cases); pair-Schur principal minors nonnegative on the whole 2^15
    substrate with the unique all-minors-zero configuration of inertia
    NEG 2 ZERO 0 POS 1; determinant trichotomy of G_6 with census
    32398 / 110 / 260 and its exact 16x lift 518368 / 1760 / 4160;
    det K classes 522462 / 51 / 1775; the inertia refinement
    det K > 0 iff NEG 4 ZERO 0 POS 4, det K = 0 iff NEG 4 ZERO 1 POS 3,
    det K < 0 iff NEG 5 ZERO 0 POS 3 over the full 2^19 sweep; the
    two-scalar law FAIL iff det G_6 < 0 and det K <= 0.
G6  Invariant layers. Linear orbit sums are insufficient (3584 buckets,
    58 mixed); the canonical 28 quadratic invariants are sufficient
    (88352 buckets, zero mixed); Burnside count 89472 by formula and by
    direct enumeration; proper quotient gap 1120.
G7  Real-witness consistency by a second construction. The abstract
    linear form reproduces the witness determinants -3840, -768, -9856
    exactly and places all three witnesses in det G_6 < 0
    (values -1536, -1536, -4864); the five known non-rigid real
    triples satisfy det G_6 >= 0 and det K > 0.
```

## What this result means

The Hankel divisor block of c = mu * t splits as an XOR circulant plus a
two-adically unimodular squareful defect. On the extremal locus the skeleton
carries the exact integral Witt form diag((-1)^(|S|+1) 3^(|S|)). At k = 2 the
balanced transfer is universal. At k = 3 universality fails, the failure locus
is decided by the two scalars det G_6 and det K, the failure inertia is
exactly NEG 5 ZERO 0 POS 3, and the decision factors through the canonical
quadratic S_3-invariant map, strictly below the orbit space.

## What this result does not mean

No layer lift occurred. This result asserts nothing about zeta zeros, the
Riemann hypothesis, Weil positivity, or explicit formulae; nothing about the
infinite operator beyond the finite compressions; no J-coupling, no physical
reading, no L2-L6 lift. The universal quantifiers of the companion note
sections 1 to 4 are carried by the written proofs there, not by this finite
audit. No Registry row moves and no Canon file changes with this probe.

## Reproducibility state

```text
pin:             ab8a9db324c36564bfbbb06835b106f151b49f7b
PREREG sha256:   ef25c31ef5835fb6a755916f31e795b979d3bd15452507cafb996a0286dc0044
verifier sha256: e9a9ee71919a46f7e193f8c53489b49cab6248d826f6300660da0c35951155e6
stdout sha256:   88ba526bb0ddc10248d41d873b76fa96369253f875a4c8b8b7d3fc27d3762d9d
local aarch64:   PASS, Debian GNU/Linux 13, Python 3.13.5, empty stderr, 27 s
cross x86_64:    PASS, Ubuntu 22.04, Python 3.10.12, byte-identical stdout
GitHub x86_64:   pending, runs at pull-request time
GitHub aarch64:  pending, runs at pull-request time
Canon fold:      not started
```

The next boundary is the owner's pull request for this one-probe branch and
its review and merge without squash or rebase. Any Registry or Canon movement
is a later, separate reviewed action, bounded by the companion note
`notes/C-TM-HANKEL-XOR-DEFECT-1.md` (itself pending review on its own branch).
