# C-ENTROPY-MACKEY-OBSTRUCTION-4-N independent breaker result

```text
STATUS:           NON-CANONICAL BREAKER RESULT
AUTHORITY:        none
SCIENTIFIC GRADE: UNEARNED
BREAKER:          22/22 PASS as reported by the M2 breaker session
RUN RECORD:       INCOMPLETE, pinned stdout not transferred
DECISION:         BREAKER GATE SATISFIED ON THE COUNTING AND TARGET-STRUCTURE
                  CONTENT; THE COMMON-COCYCLE PREMISE REMAINS SINGLE-ROUTE
PUBLIC BRIDGE:    ENTROPY-LAYER-BRIDGE remains O / STOP
```

This note records the breaker required by
`PREREG-C-ENTROPY-MACKEY-OBSTRUCTION-4-N.md` and by
`MACKEY4-PRIMARY-RESULT.md`, and the adjudication of that breaker against the
primary route. It is incubation material. It authorizes no public issue,
formal probe, registry row, frontier change, Canon patch, or status change.

## 1. Pins

```text
public basis:       Public Canon v28
main:               3161cbc764f547c95a80c3bd5028acf71c2ef524
tag:                canon-v28
content:            86a046007f89a64a696d013112a44f02e624dd2e
canon sha:          4b720846ccd42c7ec808ab2acb21793962390b074bb3799d28c0f16c00165d2c
recon base:         9b69881481dbcef91f3a772a13a8b7c98825ad31
breaker prereg:     PREREG-BREAKER-MACKEY4-1.md
breaker prereg sha: d02badef96706f4c1e3f88edf1430e4641e2276245873b875e56f399fafc8a51
breaker code:       mackey4_break.py
breaker code sha:   2bcb6ce2f009395e81f5904aef45475e8f165983003b6c4ca2d6aead86be6faa
breaker bytes:      29504
breaker stdout sha: 96475153... CLAIMED BY THE BREAKER SESSION, FILE NOT TRANSFERRED
platform:           Ubuntu 24.04.4, x86_64, Python 3.11.15, one platform
executions:         1 formal, plus one byte-identical repeat run
```

Both transferred files were verified byte for byte against the declared
SHA-256 before they were committed. Both are LF only. The committed Git blobs
reproduce the declared hashes exactly.

## 2. Independence provenance

The breaker was authored in a separate named session that declares it did not
read `mackey4_verify.py`, `mackey4_primary.stdout.txt`, or
`MACKEY4-PRIMARY-RUN.md`, and imported nothing from this branch.

`mackey4_verify.py` was read for the first time by the present adjudicating
session, after the breaker was frozen, pinned, and run. Reading a frozen
instrument after its run cannot contaminate it. No adjudication finding below
was fed back into either instrument; neither file was edited.

The adjudication used one additional synthetic instrument, described in
section 5. It touches no claim carrier: no `F_5^6`, no `Z[zeta_5]`, no canon
generator table. It does not import or execute either verifier.

## 3. What the breaker independently corroborates

The breaker reaches the primary's load-bearing values by genuinely different
routes:

```text
E1   SNF invariant factors (5,5,5,25), |Z^4/L| = 3125, type Z/25 + (Z/5)^3.
     Breaker: integer multiplication matrix plus own Smith normal form, with
     U A V = D and |det U| = |det V| = 1 verified.
     Primary: lambda-digit arithmetic.  DISTINCT PRESENTATION.        AGREE
E2   J cycle type 1^1 4^1 20^156, unique fixed class 0, order 20.
     Breaker: conjugated integer matrix W = U M_J U^-1 mod the invariant
     factors, well-definedness checked.                               AGREE
E3   Dyadic component law and c_src = 158, 315, then 629 for r >= 2.
     The primary hardcodes gcd(2^r,20) as min(2^r,4). The breaker verifies
     the gcd law itself by direct orbit count for m in {1,4,20}, r = 0..8.
     STRONGER THAN THE PRIMARY ON THIS POINT.                         AGREE
E4   Recurrent core |R| = 6250, halves 3125 + 3125, sheets z6 = 4 and 1.
     Breaker: image iteration plus a closure certificate F_t(H_s) = H_t,
     bijective for all four (s,t).
     Primary: a census warmup window.  DISTINCT METHOD, and the breaker's
     certificate removes the window heuristic.                        AGREE
E5   Mirror law.                                                      AGREE
E6   313 components, 312 x 20 + 1 x 10.                               AGREE
E7   All 312 generic halves regular dihedral of order 10, ord(s s') = 5,
     free action, multiplication table verified, both sides.          AGREE
E8   Singlet D_5/C_2, transitive on 5 points, five distinct reflection
     stabilizers.                                                     AGREE
E10  Menu by direct union-find on the 3125-state target half, all eight
     subgroups enumerated individually, both sides:
     D_5 313, C_5 625, each C_2 1563, trivial 3125.                   AGREE
E11  629 not in {313, 625, 1563, 3125}.                               AGREE
E12  Mixed control 312a + b = 629 has the unique solution (2,5).      AGREE
E13  Exact Fraction embedding arithmetic, transitive translation action,
     and the kernel relation gates: five involutions on all 15625 states,
     (bc)^5 = id, and the canon step (a,b,c,d) -> (a-c+d, b-c, a, b-c+d)
     reproduced as the columns of M_J.                                AGREE
```

No falsifier fired. The source additive type, the cycle type, the source
count at `r >= 2`, the target decomposition, and the whole Mackey menu are now
reached twice by exact routes that share no presentation.

`E9`, the common cocycle, is treated separately in section 5.

## 4. Adjudication finding 1: the basepoint census is a convention artifact

The frozen breaker preregistration classified the independent-basepoint
cross-edge census as diagnostic and explicitly non-falsifying, because the
breaker session could not know the primary's basepoint rule without reading
the forbidden file. It also recorded the condition under which the diagnostic
would become a real discrepancy: if the basepoint rules turned out to be
identical.

They are not identical. Three independent reasons, all read directly off the
two frozen instruments:

**Different state encodings.** Both sessions take the lexicographically
minimal element of a half as basepoint, but with respect to digit-reversed
encodings of `F_5^6`:

```text
digit weight    p1     p4    p1p   p4p     q      r
primary          1      5     25   125   625   3125
breaker       3125    625    125    25     5      1
```

Both are bijections onto `0..15624` and each is internally consistent, but
they induce different total orders on states, so "the lex-minimal point of
this half" denotes a different state.

**Different `D_5` markings.** The primary builds one global group from the
ambient generators, `rotation = d o (b e b)` with reflection `d`, and names
elements `rot0..rot4, ref0..ref4`. The breaker builds the group per component
and dynamics-natively, `s = F_0|H_0`, `s' = F_0 o F_1 o F_1`, `r = s o s'`,
and names elements `(e,k)`. Nothing forces `ref2` and `(1,2)` to denote the
same group element.

**Different measured quantity.** The primary records the right-translation
label of the cross map in globally-marked coordinates. The breaker records
the coordinate of the transported basepoint in an independently based `H_1`
frame. These are related but not the same functional.

Conclusion: the census values `157/155` and `156/156` are not comparable, and
the difference of one component is the convention artifact the preregistration
anticipated. The diagnostic is closed as non-falsifying, on its own frozen
terms. It is not a discrepancy and requires no investigation.

What is invariant, and does agree across both routes: the census takes exactly
two values over the 312 generic components; one is the identity; the other is
a single fixed reflection; the totals are 312 on both sides.

## 5. Adjudication finding 2: gate B13 has no discriminating power

This is the one finding that reduces what the breaker may be cited for.

`E9` is the common-cocycle premise. It is load bearing: candidate gate `S7`
requires that one `alpha` acts through both target representations with
**no block-dependent Mackey range hidden in the gauge**, and `F6` falsifies
the route if no single common cocycle exists. The whole obstruction argument
needs one Mackey subgroup `M` for the entire target, not one per block.

Gate `B13` of `mackey4_break.py` reports this premise as verified. It is not.
All four of its edge checks are forced by earlier gates plus its own
definitions:

```text
edge (0,1)   true by the definition of coord1t, which is built as the
             transport of the H_0 coordinates through F_1
edge (1,0)   follows from B08, since F_0 o F_1 = id on H_0
edge (0,0)   follows from B10, since perms[(1,0)] is s by construction and
             the multiplication table was verified
edge (1,1)   follows from B10 and r := s o s', since perms[(1,1)] = s o r = s'
```

`B13` cannot fail if `B08` and `B10` pass. Worse, the breaker's marking is
built per component from that component's own dynamics and its own basepoint,
which is precisely the block-dependent gauge `S7` warns against.

This was confirmed, not merely argued. A synthetic target was built with four
components carrying four deliberately **different** cocycles:

```text
component 0   sigma=(1,0)  tau=(1,1)  cross g=(0,0)
component 1   sigma=(1,2)  tau=(1,4)  cross g=(0,3)
component 2   sigma=(1,3)  tau=(1,0)  cross g=(1,2)
component 3   sigma=(1,1)  tau=(1,3)  cross g=(0,1)
```

Running the `B08`, `B10`, and `B13` logic verbatim on it gives:

```text
B08  PASS
B10  PASS
B13  PASS, reporting one uniform cocycle (0,0)->s, (0,1)->id,
     (1,0)->id, (1,1)->s r on every component
```

`B13` reports a common cocycle on a target constructed to have none.

The primary's `T02` does not have this defect. It marks every component with
**one global group** taken from the ambient generators, permits only a
per-component gauge drawn from a two-element set, and then demands the same
four specific labels `(ref4, id, id, ref0)` on all 312 components and the
singlet. That is a genuine block-independence statement and it can fail.

Consequence, stated exactly:

```text
E1-E8 and E10-E13   corroborated by two independent exact routes.
E9                  corroborated by the primary route only.
                    The breaker's 22/22 does not add evidence here.
```

The candidate's decision rule asks that "both exact routes agree" and that
"the common-cocycle reconstruction is explicit". The routes do agree on every
value both instruments actually test, and the primary's reconstruction is
explicit. But the premise that carries the most weight in the obstruction has
exactly one witness: one implementation, one platform, one run.

## 6. Lane decision

```text
The gate STOP PENDING INDEPENDENT BREAKER is satisfied on the counting and
target-structure content. It is not satisfied on the common-cocycle premise.
```

What this does not do, unchanged from the primary result and restated so no
successor summary can drift:

- it is not `A_A = empty`;
- it does not close `ENTROPY-LAYER-BRIDGE [O]`;
- it earns no public status, no registry row, and no frontier change;
- every `629` statement remains scoped to `r >= 2`;
- one platform, incubation lane, so `candidate-C` is the ceiling in any case.

Recommended next step, in order of cost:

1. Supply the pinned breaker stdout so the run record in section 1 is
   complete. Until then this record is incomplete by its own preregistration,
   whose execution policy requires every execution to be recorded.
2. Commission `PREREG-BREAKER-MACKEY4-2` scoped to `E9` alone: an independent
   reconstruction that builds one global `D_5` from the public generators,
   allows only a per-component gauge, and tests block independence. This is a
   single gate and it is the premise the entire obstruction rests on.
3. Only then decide whether to record the `candidate-C` negative subclass
   result for the fixed depth-five, fiberwise-bijective, `r >= 2` class.

Recording `candidate-C` before step 2 is defensible under the literal decision
rule, but it would rest the load-bearing common-cocycle premise on a single
route while the `22/22 ALL PASS` headline suggests otherwise. That gap is the
reason this note does not itself declare the candidate result.
