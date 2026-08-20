# PREREG C-TRACEKERNEL-EXTERIOR-CLOSURE-1-N

```text
DATE            2026-08-20
OBJECT_KEY      NOTE:C-TRACEKERNEL-EXTERIOR-CLOSURE-1-N
CLAIM_KEY       C-TRACEKERNEL-EXTERIOR-CLOSURE-1-N
STATUS          NON-CANONICAL INCUBATION
RESULT_STATE    RESULT-EXPOSED
AUTHORITY       NONE
TARGET_LINE     public mathorn1973/twist-j, possible later promotion only
LAYER           L1 exact arithmetic only
SESSION         one named session, this candidate only
```

## Currency gate record

Run this session from a fresh full clone, not from a rendered page, an
attachment, or a project snapshot.

```text
repository      github.com/mathorn1973/twist-j
STATE           ACTIVE
CANON           Public Canon v57
AUTHORITY       mathorn1973/twist-j main
CUTOVER         2026-08-19
TAG             canon-v57 -> 4ef54f0c34f80897af0121a2d93b710e70a8377c
CONTENT_COMMIT  8e8b04abe4d3359942449533854ef1d142be70df
CANON_SHA256    c96a2ef52c78d68ef8f04b582e4a17328e6a863b49664f29b1bd324171d802a8
CANON_BYTES     295013            recomputed from the file, matches STATUS.md
main            d44645a239df764c630984765a9fdd458b090a31
SHA256SUMS      5 of 5 OK
ancestry        content commit is an ancestor of the tag and of main;
                the tag is an ancestor of main
registry        292 claims: 174 T, 43 D, 32 C, 24 O, 16 F, 3 H
```

## Scope sentence

For every prime `p`, the cyclotomic Galois trace Gram `G_p` on dimension
`p - 1`, its reduction modulo `p`, the radical of that reduction as a
canonical spatial carrier `W_p` of dimension `p - 2`, the first derived
residual form `g_p` on `W_p`, and the exact consequence of one named and
declared bridge premise, `EXACT-HODGE-HOME-CLOSURE`, for the admissible
dimension of a nonzero spatial commutator carrier. At `p = 5` the resulting
metric-volume Hodge bracket on `W_5` is identified as a Lie algebra and its
`Phi` grading is frozen.

Explicitly NOT claimed: that the public architecture forces
`EXACT-HODGE-HOME-CLOSURE`; that the bracket derives `COLOR-CORE-2I`,
`COLOR-INTEGRAL-LIFT`, the binary double cover, the spinor carrier, or the
marked integral lift over `Z[zeta_5]`; any physical, decoder, measure, or
metrology reading; any extension of the registered scope of `ALPHA-SEED`;
any identification with `KERNEL-WEDGE-COUPLING`; any lift to L2 through L6.

## RESULT EXPOSURE, mandatory, read before anything else

Freeze before execution was NOT observed. The equations, the expected
`p = 5` outcome, the Gram radical, the nondegenerate derived form, the
dimension classification, the Lie bracket, the Jacobi result, and an
explicit `sl_2` triple were all known before this preregistration was
written. This document is a freeze of statement and threshold, not a freeze
of ignorance.

The programs already run in this lane, with their environment
`LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC`, Linux
x86_64, CPython 3.12.3, one platform:

```text
recon_carry_cocycle_1.py        6d45a231ddf13802a9cb381598534443bf02ff878167150451cd8370c7cded7d
breaker_carry_cocycle_1.py      6bce7c6d7ba79ecabb7edbea55dd004b3046a053ad650f47f1bfc3c0f8c85caf
recon_two_factor_2.py           0bc10105b8601b40ed8b981c9d387dfe72cb0ab85597bf10f79e39915988f4bd
recon_three_differences_3.py    ec40fc543538f5d36dde6383b1cd9d4b66a22768b1b055886c4fadbf93038f80
recon_pure_channels_4.py        e7a43265a20a5dd8ac6897ba04519fab7e1361ed7ca8b8f139a285437f29e40d
audit_external_review_1.py      e4c77c5b0075b786c043ed81e5fdd2e88dfc0e8128fb7a4bf352b1d00607c4fb
recon_tracekernel_closure_5.py  38d8807befc4c3c15c5d4caddab04d4126dc4273ba83ba3a5c0914a16c2c652b
part_CD.py                      0ec79aff9f5dd44b5906588d67f2ce9b4131dd2ea539a8d7a5c4d5d8c1125b66
part_E.py                       2b44c63614de1a864525b2696e9f0a8cfd97d1c09b2c007d05f2397eb682cefd
audit_review3_1.py              4f9bf35b38dcb83c4e2cb32beca248e8e79f9e64b827a83559796ca4a19b5339
audit_review3_1 stdout          d0a9db2df4ac54cc4f837e8ac8076d4e19fa1e04be2653a6d06ea136a947a2c4
```

These are provenance only. They are NOT blind discovery evidence and are
NOT accepted as a formal public verifier run. A future blind leg requires a
breaker written from this frozen text by an author who has not read the
positive verifier, with a new name and a new hash. No threshold below may
move after this file is hashed.

## Field 1. EQUATION

`G1` UNIVERSAL GRAM. For every prime `p`, indices `a, b` in `1..p-1`:

```text
(G_p)_{ab} = sum_{k=1}^{p-1} zeta_p^{k(a-b)} = p - 1 if a = b, else -1,
so G_p = p I - 1 1^T on dimension p - 1,
with rational spectrum {1 once, p with multiplicity p - 2},
normalized spectrum {1/p once, 1 with multiplicity p - 2},
the all-ones trace direction being the 1/p eigenvector.
```

`G2` CARRIER FROM THE RADICAL. `G_p mod p = -1 1^T`, of rank one, so

```text
W_p := rad(G_p mod p) = ker(sum : F_p^{p-1} -> F_p),   dim W_p = p - 2.
```

The carrier is derived from the Gram alone. No target prime enters.

`G3` FIRST DERIVED RESIDUAL FORM. `G_p mod p` restricted to `W_p` is
identically zero, since `W_p` is its radical. The correct object is one
level down. For `xbar, ybar` in `W_p` choose integer lifts `x, y` in
`Z^{p-1}` whose coordinate sums are divisible by `p`, and set

```text
g_p(xbar, ybar) := (x^T G_p y) / p   mod p.
```

Since `x^T G_p y = p (x . y) - (sum x)(sum y)` and both sums are divisible
by `p`, this equals `x . y mod p` and is independent of the lift. Because
`W_p^perp = <1>` for the dot product while `1` is not in `W_p`
(`sum 1 = p - 1 = -1 mod p`), `g_p` is nondegenerate on `W_p`, so
`W_p ~= W_p^*` canonically with no further choice.

`G4` BRIDGE PREMISE, DECLARED, NOT EARNED. Named
`EXACT-HODGE-HOME-CLOSURE`:

> The complete spatial commutator data are the two-forms on `W_p`. Their
> metric-volume Hodge image is totally and without remainder the same
> spatial carrier `W_p`: no projection, no quotient, no auxiliary carrier,
> and no unnamed change of degree. Concretely the bracket is the Hodge map
> `beta_omega` determined by `g_p` and a volume form `omega` through
> `g_p(beta_omega(x wedge y), z) = omega(x, y, z)`.

The naming of `beta_omega` is load bearing. A bare "some linear
isomorphism `Lambda^2 W -> W`" is strictly weaker and does not force a Lie
algebra: on `W_5` a sampled census of 4000 random alternating products
found 3013 invertible ones, of which only 20 satisfied Jacobi.

`G5` DIMENSION CLASSIFICATION, CONDITIONAL ON `G4`. Home closure requires
`dim Lambda^2 W_p = dim W_p`, that is `n(n-1)/2 = n` with `n = p - 2`,
whose only solutions are `n = 0` and `n = 3`, hence `p = 2` and `p = 5`.
At `p = 2` the carrier is `W_2 = 0` and the closure is empty. Therefore the
only nonzero solution is

```text
n = 3,   p = 5.
```

`G6` IDENTIFICATION AT `p = 5`, CONDITIONAL ON `G4`. With
`W_5 = ker(Tr_4)` inside `F_5^4`, `g_5` the derived form of `G3`, and any
volume form `omega`, the bracket `beta_omega` is alternating, satisfies the
Jacobi identity on all `5^9` triples, induces a bijection
`Lambda^2 W_5 -> W_5`, and

```text
(W_5, [ , ]) ~= sl_2(F_5).
```

Rescaling `omega` to `c omega` scales the bracket by `c`, and `x -> x/c` is
an isomorphism, so the algebra is unique up to isomorphism and only one
scalar is chosen.

`G7` PHI GRADING COMPATIBILITY. Let `Phi` be the coordinate permutation
`(x_0,x_1,x_2,x_3) -> (x_2,x_3,x_0,x_1)` and let

```text
W_+ = <(1,-1,1,-1)>,   dim 1,
W_- = {(u,v,-u,-v)},   dim 2
```

be its eigenspaces inside `W_5`, which is the public split `3 = 1 + 2` of
`COLOR-SPLIT-12 [D]`. Then `Phi` preserves the coordinate sum, the dot
product and the volume, `det(Phi restricted to W_5) = 1`, hence
`Phi[x,y] = [Phi x, Phi y]`, and

```text
[W_+, W_+] = 0,   [W_+, W_-] = W_- onto,   [W_-, W_-] = W_+ onto.
```

The public `1 + 2` split is therefore the Cartan grading of the bracket:
the line is the Cartan part, the plane is the root part, and the bracket of
two plane directions returns to the line. A `Phi` adapted triple is
`h = (1,0,1)` in `W_+`, `e = (1,4,3)` and `f = (3,4,1)` in `W_-`, in the
basis `b_1 = (1,-1,0,0)`, `b_2 = (0,1,-1,0)`, `b_3 = (0,0,1,-1)`, with
`[h,e] = 2e`, `[h,f] = -2f`, `[e,f] = h` and determinant `4`.

## Field 2. CODE

The programs listed under RESULT EXPOSURE are `EXPOSED_PROVENANCE` and
carry no gate status. Any future checker or breaker for this candidate must
be a new file with a new name and a new SHA-256, written from this frozen
text. Python standard library only, exact integer and Fraction arithmetic,
no float in any assertion, deterministic output with every set iteration
sorted, under 120 seconds, run under
`LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC`.

## Field 3. CARRIER AND DATA

```text
general prime p                 G1, G2 exhaustive in a and b, p to 23
G_p over Z                      exact integer matrices, no reduction first
W_p over F_p                    basis (e_i - e_{i+1}), i = 1..p-2
integer lifts                   for the derived form g_p, lift independence
                                tested by adding p e_t for every t
full W_5                        all 125 elements for the bracket audit,
                                all 5^6 pairs, all 5^9 triples for Jacobi
Phi eigenspaces                 all 5 and all 25 elements enumerated
volume rescaling                c in {1,2,3,4}
random alternating products     seeded census, seed recorded in the file
No decimal appears anywhere. Every assertion is an integer or a Fraction
equality.
```

## Field 4. SYSTEMATICS AND COMPLETENESS, frozen

Each must be reported, pass or fail:

```text
S1  independence of g_p from the choice of integer lift
S2  the empty case p = 2: W_2 = 0, closure holds vacuously and is NOT the
    bit case; CARRY-PENTAD lives on a nonzero F_2^4 and the two are
    different objects, characteristic of the carrier against cyclotomic
    parameter
S3  volume rescaling omega -> c omega and the induced isomorphism
S4  plane-only negative control: dim Lambda^2 W_- = 1 is not 2, so no exact
    home closure exists on the color plane alone
S5  Phi grading, all three brackets, surjectivity of the last two
S6  the weakness of the unnamed premise: the sampled invertible-but-not-
    Jacobi census, with its seed
S7  automorphism count: |Aut(W_5, bracket)| = 120, against
    |GL_2(F_5)| = 480 of COLOR-KINEMATICAL-GL2 [D]
S8  no derivation of 2I, the spinor carrier, or the integral lift is
    attempted or reported
```

## Field 5. FAILURE THRESHOLD AND ROUTING

```text
CONDITIONAL-PASS
  G1, G2, G3, G7 hold exactly, and G5 and G6 hold exactly under the frozen
  EXACT-HODGE-HOME-CLOSURE premise, with every S1 to S8 item reported.

MISMATCH
  Any exact defect in the Gram identity, the radical, the derived form or
  its lift independence, the dimension classification, the Hodge bracket,
  the Jacobi identity, the sl_2 identification, or the Phi grading.
  A mismatch is archived, never deleted, and no threshold is moved.

STOP
  Any claim that Public Canon v57 forces EXACT-HODGE-HOME-CLOSURE;
  any use of CURVATURE-OPERATOR-CANONICAL [O] as if closed;
  any L1 to L2 lift;
  any claim that the bracket derives COLOR-CORE-2I or COLOR-INTEGRAL-LIFT;
  any extension of the registered five-prime scope of ALPHA-SEED [T].
```

## Field 6. LAYER AND ACTION

```text
LAYER   L1 only. Every statement is exact arithmetic on finite carriers.
ACTION  L1. No lift is claimed. Any lift needs its own named gate.
```

## Falsifiers of the premise, stated before any further work

`F1` WITHDRAWN. The earlier falsifier, that `COLOR-SPLIT-12 [D]` confines
the spatial commutator to the two-dimensional plane, is FALSE. The row is a
dictionary split into eigenspaces of `Phi` and carries no dependency on the
spatial commutator. `G7` shows the split is compatible with the full
bracket rather than a restriction of it. Recorded as fired against its
author, not deleted.

`F2` LIVE, NEW. `COLOR-KINEMATICAL-GL2 [D]` reads the kinematical image as
`GL_2(F_5)` of order 480 on the antisymmetric plane, embedded along
`3 = 1 + 2` by `g -> (det g)^{-1} directsum g`. The automorphism group of
the Hodge bracket on `W_5` has order 120, counted exhaustively, and equals
`PGL_2(F_5) = SO_3(F_5) = Aut(sl_2(F_5))`. If the public architecture
requires the spatial commutator to be equivariant under the order 480
kinematical group, then it is not the Hodge bracket and
`EXACT-HODGE-HOME-CLOSURE` is false. Exhibiting that requirement from the
public rows fires this candidate.

`F3` LIVE. Any public derivation showing the spatial commutator data are a
proper subspace of `Lambda^2 W_p`, or that the return map to `W_p` may be a
projection or a quotient rather than a bijection, fires the premise and the
dimension classification with it.

## Collision scan against Public Canon v57

Registry and canon read this session. No row carries the modulo `p`
radical of the Gram, the derived residual form, or the exterior closure.

```text
ALPHA-SEED [T]              same Gram G = pI - 11^T with normalized
                            spectrum {1/p, 1^(p-2)}, over Q, registered
                            scope p in {3,5,7,11,13}. This candidate does
                            not extend that scope and does not restate it
                            as new.
MEASURE-SPATIAL-ONLY [T]    trace and conformal weight 1/p, spatial base
                            ker(Tr) weight 1, d/(d+1) = 3/4 at d = 3.
                            G3 is the modulo p reading of the same weight.
QDD-PROJECTOR-PAIR-TR4 [T]  the rational-side projector pair for
                            G = I_4 - (1/5) 1 1^T. Different field,
                            different object.
COLOR-SPLIT-12 [D]          the Phi split 3 = 1 + 2. G7 refines it and
                            does not promote it.
COLOR-KINEMATICAL-GL2 [D]   order 480 on the plane. Falsifier F2.
COLOR-CORE-2I [T]           the finite group SL_2(F_5) = 2I of order 120
                            with center {I,-I}. NOT derived here. The
                            bracket gives the three-dimensional Lie algebra
                            sl_2(F_5); adjoint action of the group has
                            kernel {I,-I} and image PSL_2(F_5) = A_5, so
                            the double cover and the integral lift are not
                            recovered.
COLOR-INTEGRAL-LIFT [T]     the marked two-generator lift over Z[zeta_5].
                            NOT derived here.
QPAIR-SYM2-2I-IRREDUCIBLE [T]  owns a three-dimensional module Sym^2(2a).
                            No intertwiner with W_5 is claimed; a dimension
                            match is not an intertwiner.
KERNEL-WEDGE-COUPLING [T]   fifteen wedges of a cell pair in (F_5^6)^2 under
                            a diagonal SL_2(F_5). Different object, not the
                            Hodge map Lambda^2 W_5 -> W_5.
CURVATURE-OPERATOR-CANONICAL [O]  ROOT, STOP, FORMAL. This row, not
                            COLOR-SPLIT-12, is what blocks any claim that
                            the architecture forces G4.
CURVATURE-HISTORICAL-TRACE [T]  dim V = 818, Tr(K^2) = -881/8, frozen
                            historical operator scope only. Untouched.
```

## Successor obligation, not opened here

```text
C-TRACEKERNEL-CURVATURE-FORCING-1-N   [O]
  whether the public architecture forces EXACT-HODGE-HOME-CLOSURE.
  Blocked in the present public state by CURVATURE-OPERATOR-CANONICAL [O],
  which must first decide UNIQUE, NONUNIQUE, EMPTY or STOP after its
  carrier, measure, projection group, and ambient versus intrinsic
  commutator choice are fixed publicly. This is an L1 to L2 question and
  requires its own named gate. Nothing in the present candidate touches it.
```

## Standing conclusion of the lane, at the labels earned

```text
[T]   the cyclotomic Gram gives a canonical spatial carrier and a canonical
      metric on it, for every prime, with no target number as input
[T]   exact metric-volume home closure of the commutator is possible on a
      nonzero carrier only at p = 5
[T]   at p = 5 the closure produces sl_2(F_5) with the public 1 + 2 grading
[O]   the public architecture does not yet force the closure
```
