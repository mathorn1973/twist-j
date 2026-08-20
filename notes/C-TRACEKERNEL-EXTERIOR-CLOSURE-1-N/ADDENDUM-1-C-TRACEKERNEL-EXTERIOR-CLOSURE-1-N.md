# ADDENDUM 1 to PREREG-C-TRACEKERNEL-EXTERIOR-CLOSURE-1-N

```text
AMENDS       PREREG-C-TRACEKERNEL-EXTERIOR-CLOSURE-1-N.md
             sha256 1c0b33b0f95c2260ae0f6ea3e3c3f03af0e2a763cccff91269621aa529fb1a2d
             16167 bytes. The amended file is RETAINED BYTE-IDENTICAL as
             the record. This addendum is additive and is hashed separately.
WHEN         2026-08-20, after the prereg was hashed, before any breaker
             exists and before any leg of this candidate is executed.
DIRECTION    Every change below either LOWERS a status ceiling or SHARPENS
             a falsifier. Nothing is raised, no threshold is moved, no
             scope is widened, no falsifier is retired.
WHY          An external review returned two corrections and two exact
             witnesses. Recorded here rather than quietly folded into the
             frozen file.
```

## A1. Status correction, mandatory

The closing block of the frozen prereg, headed "Standing conclusion of the
lane, at the labels earned", carries three rows labelled `[T]`. That is
grade inflation. In a non-canonical incubation lane a new result carries a
candidate label and never a bare canon label. The corrected accounting,
which supersedes that block:

```text
[candidate-T]
  The cyclotomic Galois Gram yields, for every prime p, the trace-kernel
  carrier W_p = rad(G_p mod p) of dimension p - 2 and the nondegenerate
  first-derived residual form g_p on it.

[candidate-T, conditional on EXACT-HODGE-HOME-CLOSURE]
  A nonzero home-carrier commutator closure exists only for p = 5.

[candidate-T, conditional on EXACT-HODGE-HOME-CLOSURE]
  At p = 5 the Hodge bracket yields sl_2(F_5) with the public Phi grading
  W_+ directsum W_- of dimensions 1 + 2.

[O]
  Public Canon v57 does not force EXACT-HODGE-HOME-CLOSURE. The decision is
  blocked by CURVATURE-OPERATOR-CANONICAL [O] and armed against full
  faithful GL_2(F_5) equivariance by F2 below.
```

The public source rows keep their public statuses unchanged and at their
own registered scopes: `ALPHA-SEED [T]` at p in {3,5,7,11,13} over Q,
`MEASURE-SPATIAL-ONLY [T]`, `QDD-PROJECTOR-PAIR-TR4 [T]`,
`COLOR-SPLIT-12 [D]`, `COLOR-KINEMATICAL-GL2 [D]`, `COLOR-CORE-2I [T]`,
`COLOR-INTEGRAL-LIFT [T]`, `CURVATURE-HISTORICAL-TRACE [T]`,
`CURVATURE-OPERATOR-CANONICAL [O]`. The candidate labels attach only to the
universal extension, the derived residual form, and the new bridge.

## A2. F2 sharpened from an order count to an exact witness

The frozen F2 argued from group orders, 480 against 120. That is correct
but weak. It is replaced, at the same falsifier and without widening it, by
a local exact witness.

Public reading, verbatim in scope: `rho(g) = (det g)^{-1} directsum g`
along `3 = 1 + 2`. Take the central element `g = 2 I_2` in `GL_2(F_5)`.
Then `det(2 I_2) = 4` and `4^{-1} = 4`, so `rho(2 I_2)` acts as `4` on
`W_+` and as `2` on `W_-`. With the frozen triple `h` in `W_+` and `e` in
`W_-` and `[h,e] = 2e`:

```text
[rho h, rho e] = [4h, 2e] = 8 [h,e] = 8 (2e) = 16 e = e
rho [h, e]     = rho(2e)  = 2 (2e)  = 4 e
e != 4 e,  so rho(2 I_2) is not in Aut(W_5, bracket).
```

General scalar: `rho(lambda I_2) = lambda^{-2} directsum lambda I_2`, and
compatibility with the mixed bracket `[W_+, W_-] -> W_-` requires
`lambda^{-1} = lambda`, that is `lambda^2 = 1`. Of the central `C_4` only
`lambda = +-1` survive; `lambda = 2` and `lambda = 3` break the bracket.
Verified exhaustively on all 125 states.

## A3. New quantitative finding, additive

Not in the frozen file and not supplied by the review. The overlap between
the public kinematical action and the automorphism group of the Hodge
bracket was counted exhaustively over all 480 elements of `GL_2(F_5)`:

```text
elements of GL_2(F_5) whose public image rho(g) preserves the bracket:  8
structure: 4 diagonal with det 1, 4 antidiagonal with det -1
that is exactly the normalizer of the maximal torus
incompatible: 472 of 480, which is 98.3 percent
```

So the incompatibility is not a boundary effect of the two group orders. It
is generic. The frozen F2 stands, and its consequence is stronger than it
was written.

Also recorded: the review's alternative three-dimensional representation
`(det g)^{-1} Sym^2(g)` was checked. Its image has order exactly 120, it
kills every scalar matrix, and it factors through `PGL_2(F_5)`. It is a
different carrier datum from the public `(det g)^{-1} directsum g`, whose
image has order exactly 480 and is faithful. Substituting the first for the
second would be a new named bridge, not a reinterpretation of
`COLOR-KINEMATICAL-GL2 [D]`. No such bridge is claimed here.

## A4. Systematics item S6 upgraded from sampling to an exact counterexample

The frozen S6 reports a seeded census: of 4000 random alternating products
on `W_5`, 3013 were invertible and 20 satisfied Jacobi. That evidence is
retained. It is now supplemented, at the same claim, by one exact
counterexample which is characteristic-free.

On a basis `e_1, e_2, e_3` set

```text
[e_2, e_3] = e_1,   [e_3, e_1] = e_1 + e_2,   [e_1, e_2] = e_3.
```

In the bases `(e_2 wedge e_3, e_3 wedge e_1, e_1 wedge e_2)` and
`(e_1, e_2, e_3)` the map `beta` has matrix

```text
A = [[1,1,0],[0,1,0],[0,0,1]],   det A = 1,
```

so `beta : Lambda^2 W -> W` is an isomorphism. Yet

```text
[e_1,[e_2,e_3]] + [e_2,[e_3,e_1]] + [e_3,[e_1,e_2]]
  = [e_1,e_1] + [e_2, e_1 + e_2] + [e_3,e_3]
  = -[e_1,e_2]
  = -e_3  !=  0.
```

The Jacobi sum is `-e_3` over `Z` and over every field, so an invertible
`beta` does not force a Lie algebra. This is the exact reason the premise
must name `beta_omega` and not merely "some isomorphism". Verified.

## A5. Provenance, so no later leg can misclaim it

```text
The rho(2 I_2) witness of A2 and the Jacobi counterexample of A4 were
SUPPLIED BY EXTERNAL REVIEW, in text, before any breaker for this
candidate existed. They were then verified independently here. A later
breaker MUST NOT report either of them as a blind find.

The counting of A3 (8 of 480, the torus normalizer) was not supplied and
was found in this session. It is nonetheless result-exposed like the rest
of the lane.

This conversational session has seen the construction, the expected
outcome, the explicit sl_2 triple, F2, and both witnesses. It is therefore
DISQUALIFIED as the blind breaker leg. It may audit; it may not certify
independence.
```

## A6. Verifier pins for the addendum

```text
audit_review3_1.py   4f9bf35b38dcb83c4e2cb32beca248e8e79f9e64b827a83559796ca4a19b5339
                     10757 B, 34 of 34 PASS
audit_review4_1.py   83a7a940d980d660a366dee6685293089ecae1a7f44c24604b4fdd051eb8204d
                     16 of 16 PASS: X1 the rho(2I) witness, X2 the 8 of 480
                     count and the two representations, X3 the exact Jacobi
                     counterexample
environment          LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1
                     PYTHONHASHSEED=0 TZ=UTC
                     Linux x86_64, CPython 3.12.3, ONE platform
```

One platform is an exposition witness. It is not a two-architecture leg and
nothing here is promoted on it.

## A7. Handoff conditions for the blind leg, binding

```text
1  The prereg and this addendum are committed and pushed before any
   breaker is written. Git is the only handover surface; a local hash is
   not a shared freeze.
2  The second author reads the frozen prereg and this addendum. The second
   author does NOT read recon_tracekernel_closure_5.py, part_CD.py,
   part_E.py, audit_review3_1.py, audit_review4_1.py, or any transcript of
   this session.
3  break.py is written, committed and hashed BEFORE it is executed.
4  Only then is it run.
5  Conclusions are compared only after the breaker leg is frozen.
6  A leg that merely reruns the positive verifier is reproduction, not
   independent confirmation, and is labelled as such.
7  Any output is packaged as PROMO-C-TRACEKERNEL-EXTERIOR-CLOSURE-1 and
   still promotes nothing until a separate sealed public fold consumes it.
```
