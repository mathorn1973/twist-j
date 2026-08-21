# P-RG-NO-FLOW-1 preregistration

```text
PROBE       P-RG-NO-FLOW-1
LANE        the renormalization question
LAYER       L4 (support). No lift to L5 or L6 is claimed or attempted.
BASE        Public Canon v23, tag canon-v23, content commit 7830d852,
            CANON_SHA256 f842b613, CANON_BYTES 116017, SHA256SUMS 5 of 5 OK.
VERIFIER    verify.py in this directory,
            sha256 9db7cca18f2dfe4d0efacd8b7ab334ccf9f81b1360629260e943788c632a0377
ENV         LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
            Python standard library only, exact integer and rational
            arithmetic, no float in any assertion, run from repository root.
BUDGET      under 120 seconds. Local measurement in the originating lane:
            0.5 seconds.
OWNER       one owner; claim the public issue before executing.
```

## 0. Disclosure, read this first

This probe is CONFIRMATORY, not exploratory. The result was first derived in
the project incubation lane on 2026-07-26 (lane memo
`RG-STRUKTURA-NOSIC-A-DVA-NOGO_2026-07-26.md`), so the expected values are
known in advance and are stated below. That is the declared shape of the
contract: the incubation lane derives and freezes, the public pipeline
validates and gates. What this preregistration freezes is the statement, the
gate list and the falsifier, before the public verifier executes here.

The public verifier in this directory is fresh code, not the lane's
exploratory script. The lane's exploratory script and its two self-caught
errors are recorded in the memo and are not part of this probe.

## 1. The question

`ENTROPY-BLOCK-HALVING [C]` registers that the renormalized block maps are
exactly two-to-one on the recurrent core at every tested dyadic scale, one
unresolved bit per scale. A renormalization group is a semigroup, and the
two-to-one structure supplies the non-invertibility a semigroup needs. The
open question this probe settles is whether that structure additionally
carries a monotone: a function `C` on the core, nonincreasing along the
block maps, that strictly decreases somewhere. Without such a `C` there is
no renormalization flow and no c-theorem analogue, whatever the bit
bookkeeping says.

The probe also eliminates the only two other structures in the program that
have been proposed as scale carriers: the Galois action on the four
archimedean embeddings, and the step operator `M_J`.

## 2. The frozen statement

```text
S1  On the recurrent core of the driven kernel, the directed graph with an
    edge x -> F_t(x) for each branch map t in {0,1} has no edge between two
    distinct strongly connected components.
S2  Consequently every function C on the core with C(F_t(x)) <= C(x) for
    both t and all x satisfies C(F_t(x)) = C(x) for both t and all x.
    Delta C = 0 identically: no such C decreases anywhere.
S3  Therefore the block-halving structure carries NO monotone C-function and
    NO renormalization flow on the recurrent core. The one unresolved bit
    per scale is backward indeterminacy, not forward monotonicity.
S4  The Galois action on the four embeddings cannot carry a monotone: it is
    cyclic of order four and its generator exchanges the expanding and the
    contracting channel at every step.
S5  The step operator M_J cannot carry a monotone: det(M_J) = 1, so M_J is
    in GL_4(Z) and every orbit is periodic.
```

The lemma behind S2, stated so the gate is auditable and not a black box:
if the edge `x -> y` lies inside a strongly connected component there is a
path `y -> ... -> x`, so `C(x) >= C(y) >= ... >= C(x)` and every inequality
on that cycle is an equality. S1 says every edge is such an edge.

## 3. Carrier

The driven-kernel carrier (five generators, the encoding, the driver, the
census procedure) is taken identically from the pinned public probe
`P-ENTROPY-BRIDGE-3`, which is the canon evidence path for
`ENTROPY-BLOCK-HALVING` and `ENTROPY-LIVING-SET`. Reuse here is required
rather than optional: this probe asserts a property OF that carrier, so any
deviation in the carrier would make the result unfalsifiable against the
rows it addresses. Gates G01 to G03 re-derive the registered carrier
invariants before anything new is asserted, so a carrier drift fails loudly
instead of silently.

The originating lane additionally reproduced `P-ENTROPY-BRIDGE-3` itself in
full, stdout byte-identical to its recorded pin
`a4600f241d499bef6eda8d1efa8fad082b054dcf7bbb5e10746c594401e4d32d`,
1612 bytes, 10 of 10 PASS.

## 4. Gates, frozen before execution

```text
G01 CARRIER        recurrent core 6250 on 313 attractors, 6250 = 2 x 5^5
G02 HALVES         the two branch images partition the core, 3125 + 3125
G03 FIBERS         exact fiber census: every fiber of both branch maps on
                   the core has size exactly 2
G04 FLOWGRAPH      6250 nodes and 12500 directed edges
G05 SCC-CENSUS     313 strongly connected components, sizes 312 x 20 and
                   1 x 10, matching the 313 attractors
G06 NO-INTER-EDGE  zero of the 12500 edges runs between components
G07 PERMUTATION    the same conclusion by an independent algebraic route
                   with no graph search: F_0 permutes half 0, F_1 permutes
                   half 1, both cross maps are bijections, both two-step
                   maps permute their half
G08 TRANSIENT      9375 states outside the core; all 15625 states are inside
                   the core after exactly 3 driven ticks
G09 GALOIS-NOGO    exhaustively over all 256 functions on the four
                   embeddings, no nonconstant weakly monotone function along
                   any generator in either orientation
G10 STEP-NOGO      char poly Phi_5(x-1), det 1, orbit lengths 1, 4, 20
                   modulo 5, every state periodic
```

G06 and G07 are two independent routes to the same conclusion. G07 exists
precisely so that the result does not rest on one graph algorithm.

## 5. Failure threshold and falsifier

```text
FIRE if any of G01 to G03 fails: the carrier has drifted from the registered
     one and nothing downstream may be read.
FIRE if G06 finds one or more inter-component edges. One such edge is a
     candidate site for a genuine strict decrease and S1 to S3 are refuted.
FIRE if G06 and G07 disagree.
FIRE if G09 exhibits a nonconstant weakly monotone function along a Galois
     generator.
FIRE if G10 finds det(M_J) != 1 or a non-periodic orbit modulo 5.
FIRE if the aarch64 and x86_64 transcripts differ in any byte.
```

A fired falsifier is a first-class outcome and is archived, not deleted. The
threshold is not moved after the fact.

## 6. Systematics

```text
The census procedure inherits the warm-up 400 and window 300 of the source
probe. A different window could in principle name a different core; the
probe therefore pins the core cardinality and the attractor count as gates
rather than assuming them.
The Tarjan implementation is iterative to avoid a recursion limit
dependency. G07 is the systematics control on G06.
The wall weights in G09 are computed from the WALL-CIRCLE-LEMMA closed form
as exact rationals. No polylogarithm is evaluated, so no numerical tolerance
enters anywhere in this probe.
The two no-go gates G09 and G10 are finite and exhaustive over their whole
domains (256 functions, 625 states), not sampled.
```

## 7. Scope: what this probe does NOT claim

```text
It says nothing about the transient. The relaxation into the core IS
  irreversible; the probe measures it as three ticks and calls it a
  one-time relaxation, not a flow with two fixed points.
It says nothing about scales beyond the registered [C] range of
  ENTROPY-BLOCK-HALVING, and it does not prove an all-scale law.
It says nothing about central charge, stress tensor, conformal field
  theory, the c-theorem, the a-theorem, or any physical observable.
It says nothing about the L5 or L6 layers, about ENTROPY-LAYER-BRIDGE, or
  about the private line.
It does not touch section 16 of the canon. The Galois gate uses the wall
  closed form only as an input.
It does not weaken ENTROPY-BLOCK-HALVING. The halving is real and G03
  re-derives it exactly. What the probe denies is that the halving is a
  monotone, not that it is a halving.
```

## 8. Reconciliation obligation, flagged for the owner

`AGENTS.md` requires every public claim to map to an internal claim of equal
or stronger status. The originating lane could not confirm the private head
in its session and does not know whether the sealed v184 line carries a
basis for S1 to S3. This is an owner decision before the fold, not something
the probe can settle: either an internal basis is named, or the public row
is registered at the status the reconciliation supports.
