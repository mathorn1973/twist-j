# RESULT. C-QDD-ERASURE-LATTICE-1

Date: 2026-08-21. Candidate lane, NO AUTHORITY. Basis: Public Canon v58
(tag canon-v58, content commit 05a0749e, CANON_SHA256 647822f5..., 304010 B,
SHA256SUMS 5 of 5 OK, tag and content commit ancestors of main).

Decision per the frozen preregistration: **ERASURE-LADDER**.

## Frozen artifacts and hashes

```text
frozen before execution (FREEZE-C-QDD-ERASURE-LATTICE-1.txt, 08:08:58Z):
  PREREG-C-QDD-ERASURE-LATTICE-1.md
    6ba0d1e947e310e1c8952e83bdb59bdac8642eff72b28a1d9504aa402adbb921  11433 B
  verify_qdd_erasure_lattice_1.py
    e482ed41ffa7471a7307ee0cf02d1d2d7bd3f6cab2be39318b2c7978a471c9b8  18550 B
  breaker_qdd_erasure_lattice_1.py
    c1223b967bfdf864ef9f8a38bf11515bfbc2f5d28171a68234079cfb5eb6f89b  11792 B

single formal executions, exit codes 0 / 2, both stderr empty:
  verify stdout   45 gates, 45 PASS, 0 FAIL, DECISION: ERASURE-LADDER
    eaa53d32a8f2eace3d4d2e993993588fea9afd309d38d1def07a1ba4fd36a140
  breaker stdout  10 attacks, 9 HOLDS, 1 BREAK (B4b), FINDINGS 1 of 10
    9c3ef3ae4e0996bd1aa0ac2a9c4ec597ba9c19bfb9ba72e38e4998b9edec263a

diagnosis leg (post-run, own identity, frozen files untouched):
  diag_qdd_erasure_lattice_1.py
    3fa07d6eb1b9b279756bb4b6908c426407c050a962169057578fce0ecf81fb28
  diag stdout, exit 0
    e85f5203614797555743e4bba2f6a5718fd8de0fa1716ed74d9886787523517b
```

## The fired breaker line, archived, and its exact diagnosis

Breaker attack B4b filtered the 48-member normalizer family
`{+-rho(h) Q_k : h in S_k}` by admittedness and D_k-covariance and carried
the auxiliary expectation "exactly {+-Q_k} survives". Four algebraic members
survived. The diagnosis leg identifies them exactly:

```text
+-Q_k               at h = identity
+-(R_k - C_k)       at h = g^2 = (x -> 2k - x), the double transposition
                    (0 4)(1 3) fixing k = 2, the central involution of D_k
```

with the exact identity `rho(g^2) Q_k = R_k - C_k`. The survivor set equals
the E3 member list, so the finding is a defect of the breaker's auxiliary
expectation, not of the candidate: E3 is CONFIRMED by the independent route.
No prereg falsifier (LATTICE-F, CENTRALIZER-F, CLASS-F, MOTOR-F,
TRANSPORT-F) fires. The fired line stays archived as recorded; nothing
frozen was edited and no threshold moved.

## Earned statements

All within the frozen public J simplex class of the sealed record lane
(`(Q^4, G)`, vertices `u_x = D^x e_0`, motor `D = M_J - I = rho((01234))`,
record token k, admitted laws `T P_k = P_k T = 0`, `T^sharp T = Q_k`,
registered sign equality `T ~ -T`; effects compared last, and
`P_2 = E_low`, `Q_2 = E_high` re-verified).

```text
L1 [candidate-T]  LATTICE. The subgroups between the architecture residual
    H_k = AGL_1(F_5) cap S_k ~= C_4 and the record stabilizer S_k ~= S_4
    are exactly H_k < D_k < S_k, with D_k the unique dihedral group of
    order 8 over H_k. Proof by 20 + 16 exhaustive closures; independently
    by the full 30-subgroup census of S_k (breadth-first closure lattice).

L2 [candidate-T]  CENTRALIZERS. Moving-space centralizer dimensions
    3 / 2 / 1 with exact bases {R_k, C_k, J_k}, {R_k, C_k}, {Q_k}; the
    full End(V) commutant dimensions are 4 / 3 / 2. Two independent
    methods agree (nullspace of the joint linear system; rank of the exact
    group-averaging projector).

L3 [candidate-T]  RUNG CLASSES, target-independent.
    H_k rung: T = eR + rC + sJ with e^2 = 1, r^2 + s^2 = 1; an injective
      rational family of physical classes (the sealed rational circle,
      re-derived by fresh code). NONSELECTION, infinitely many classes.
    D_k rung: exactly four algebraic members {+-Q_k, +-(R_k - C_k)},
      exactly two physical classes: the Lueders class [Q_k] and the
      nonterminal involution class [R_k - C_k]. The sealed terminality
      bifurcation lives exactly on this rung.
    S_k rung: exactly one physical class [Q_k]; strict representative
      idempotence selects +Q_k.

L4 [candidate-T]  MOTOR EMPTINESS. The commutant of the motor is Q[D],
    spanned by {I, D, D^2, D^3}; no nonzero member annihilates the
    recorded line, so no admitted law commutes with the motor; by
    commutant containment the admitted class is EMPTY for every subgroup
    of S_5 containing the motor cycle (machine witnesses: C_5, AGL_1(F_5),
    A_5, S_5). A reading law cannot be equivariant under the flow.

L5 [candidate-T]  TRANSPORT. Conjugation by the motor carries the complete
    ladder of token k to token k+1 (stabilizer, residual, dihedral rung,
    projectors), and the dimensions 3-2-1 hold at all five tokens. The
    motor that admits no reading transports the reading ladder.

L6 [candidate-T]  CENTER IDENTITY (from the diagnosis leg). The second
    D_k-rung class is the central involution acting after Lueders:
    R_k - C_k = rho(x -> 2k - x) Q_k, and x -> 2k - x is the multiplier
    a = -1, the involution of the residual C_4 itself. Z(S_k) is trivial;
    Z(D_k) = {1, a = -1} on the moving space.
```

Reading, [candidate-D], exactly as frozen plus the center identity:

```text
Within this frozen class the reading interface has exactly one minimal
selecting premise: full record-partition erasure S_k. There is no third
rung. Retaining even one bit of residual label, the orientation sign
x - k versus k - x among the unrecorded vertices, retains exactly the
known nonterminal class rho(-1) Q. The architecture residual alone leaves
a continuum. No reading is equivariant under the motor, so the selecting
symmetry cannot come from the flow; it can only come from what the record
erases. The O2 selection gap is, in this class, exactly one bit wide.
```

## What this does and does not move

Extends the sealed lane P-QDD-J-CENTRALIZER-TERMINALITY-1,
P-QDD-RECORD-COMPLETE-STABILIZER-1, P-QDD-RECORD-NATURALITY-FORK-1,
P-QDD-FRESH-RECORD-NOFEEDBACK-2, P-QDD-J-AFFINE-APPARATUS-1 by closing the
premise lattice between their endpoints and by the motor no-go below it.
Combined with the sealed record-sufficiency equivalence, the open O2
question sharpens from "what physical principle supplies record
sufficiency" to "what erases the central involution x -> 2k - x of the
retained labels", one bit.

No status changes. QDD-INSTRUMENT-APPARATUS stays O with O1 and O2 open.
SAMPLING NOT PROVIDED untouched. L4 only, no L5/L6 lift, apparatus records
are not public D_clock records. The lattice quantifies only over premises
containing the architecture residual H_k; the naturality-versus-normalizer
axis is separate and sealed. Candidate labels throughout; validation is
public, not here.
