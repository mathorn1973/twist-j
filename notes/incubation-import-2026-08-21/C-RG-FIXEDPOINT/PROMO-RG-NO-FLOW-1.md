# PROMO-RG-NO-FLOW-1: promotion proposal

```text
CANDIDATE   C-RG-NO-FLOW-1 (incubation lane, project, 2026-07-26)
TARGET      Public Canon v23 -> v24, mathorn1973/twist-j main
PROPOSES    four new [T] rows and one canon scope note
CARRIES     probes/P-RG-NO-FLOW-1 and probes/P-WALL-EXCESS-5-1
AUTHORITY   none. This is a proposal. Nothing is canon until the public
            pipeline preregisters, pins, runs on two architectures
            byte-identically, and the owner opens the fold PR.
BASE PIN    Public Canon v23, tag canon-v23, content commit 7830d852,
            CANON_SHA256 f842b613, CANON_BYTES 116017, SHA256SUMS 5 of 5 OK,
            content commit an ancestor of HEAD da3d9e53. Verified by clone.
```

This document is designed to be consumable without reading anything else.

## 1. What is being proposed and why it matters

`ENTROPY-BLOCK-HALVING [C]` uses the word *renormalized*. That word, read
without a scope note, invites the reading that the program has a
renormalization flow and therefore a place for a c-theorem. It does not.
The block halving is real, but it merges states that lie in the same
strongly connected component, so no monotone can separate them. The one
unresolved bit per scale is backward indeterminacy, not forward
monotonicity.

The proposal registers that as a theorem rather than leaving it as folklore,
eliminates the only two other carrier candidates in the program, and adds
one unrelated small positive result from the same lane.

The lane also killed a bridge it had itself proposed. That kill is carried
as a gate, not as a row, so it stands as a standing refutation for future
sessions.

## 2. Exact statements

```text
RG-NO-FLOW-ON-CORE [T]
  On the recurrent core of the driven kernel (6250 states, 313 attractors)
  the directed graph with an edge x -> F_t(x) for each branch map
  t in {0,1} has 12500 edges and 313 strongly connected components of sizes
  312 x 20 and 1 x 10, and NO edge runs between two distinct components.
  Consequently every function C on the core with C(F_t(x)) <= C(x) for both
  t and all x satisfies C(F_t(x)) = C(x) identically, so no such C decreases
  anywhere: the block-halving structure carries no monotone C-function and
  no renormalization flow on the recurrent core. The halving itself is
  untouched and is re-derived exactly (every fiber of both branch maps has
  size exactly 2). Transient: 9375 states lie outside the core and all
  15625 states are inside it after exactly 3 driven ticks, a finite
  one-time relaxation, not a flow with two fixed points. No claim about
  scales beyond the registered range, about an all-scale law, about central
  charge, stress tensor, conformal field theory, the c-theorem or the
  a-theorem, about L5 or L6, or about any physical observable.

RG-GALOIS-NOGO [T]
  Gal(Q(zeta_5)/Q) = (Z/5)^* is cyclic of order 4; its generators are 2 and
  3; the generator orbit of the four archimedean embeddings is 1, 2, 4, 3;
  the generator exchanges the expanding and the contracting channel at
  every step, and the WALL-CIRCLE-LEMMA weights along the orbit alternate
  27/50, 3/50, 27/50, 3/50 in units of zeta(2). Exhaustively over all 256
  functions on the four embeddings there is no nonconstant weakly monotone
  function along any generator in either orientation, and the four
  increments around the orbit sum to zero. The Galois action therefore
  cannot be a renormalization trajectory. This does not disturb the
  ordering 27/50 > 3/50; it denies its reading as a flow.

RG-STEP-NOGO [T]
  The characteristic polynomial of M_J is x^4 - 3x^3 + 4x^2 - 2x + 1 =
  Phi_5(x - 1), with N(J) = 1, Tr(J) = 3 and det(M_J) = 1, so M_J lies in
  GL_4(Z); modulo 5 it permutes all 625 states with orbit lengths exactly
  1, 4 and 20, so every state is periodic and no nonconstant weakly
  monotone observable exists along its orbits. The tick is not a
  renormalization scale.

WALL-EXCESS-SELECTS-5 [T]
  Normalizing by zeta(2), the WALL-CIRCLE-LEMMA full nontrivial-root sum is
  (N-1)(N-2)/(2N) and its excess above 1 is (N^2 - 5N + 2)/(2N). That
  excess equals 1/N if and only if N(N - 5) = 0, hence for exactly one
  integer N >= 3, namely N = 5; and the channel ratio (N-2)^2/(N-4)^2
  equals 9 for exactly one integer N >= 3, namely N = 5. The registered
  excess 1/5 = 1/p and the registered ratio 9 are therefore specific to
  p = 5, in contrast to the rung itself, which is p-generic. This is not a
  selection argument for p = 5 and makes no imaginary-part, field-trace,
  substrate, normalization, regularization or physical claim.
```

## 3. Falsifiers

```text
RG-NO-FLOW-ON-CORE     fires on one inter-component edge among the 12500,
                       equivalently on one core state x, one branch t and
                       one nonincreasing C with C(F_t(x)) < C(x); fires if
                       the graph route and the algebraic permutation route
                       disagree; fires if the recurrent core is not 6250 on
                       313 attractors or a fiber has size other than 2.
RG-GALOIS-NOGO         fires on any nonconstant weakly monotone function
                       along a generator of (Z/5)^*.
RG-STEP-NOGO           fires if det(M_J) != 1 or if any state modulo 5 is
                       non-periodic under M_J.
WALL-EXCESS-SELECTS-5  fires on any integer N >= 3 other than 5 with excess
                       equal to 1/N, or with channel ratio 9, or if the
                       identity excess(N) = (N^2 - 5N + 2)/(2N) fails.
```

## 4. Verifiers and pins

```text
probes/P-RG-NO-FLOW-1/verify.py
  sha256 9db7cca18f2dfe4d0efacd8b7ab334ccf9f81b1360629260e943788c632a0377
  13438 bytes, 10 gates, runtime 0.5 s in the originating lane
probes/P-RG-NO-FLOW-1/EXPECTED.txt (lane run, regenerate at the pinned run)
  sha256 ba3250f9050fb5b56aea7151e5dc90301bae0ca1d29a364028f1be1c962fb28d
  2160 bytes

probes/P-WALL-EXCESS-5-1/verify.py
  sha256 f08fc9bb00f64c538601fc70f6b0ced6eb5c40c1c0830088bffdfb30542e1a86
  4433 bytes, 5 gates, runtime 15 s in the originating lane
probes/P-WALL-EXCESS-5-1/EXPECTED.txt (lane run, regenerate at the pinned run)
  sha256 e76eb9e4a9d81f93a609ef48d1c39963057298a623f0eaa6b7538b600be6058a
  1405 bytes

environment  LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
             Python standard library only, exact arithmetic, no float in any
             assertion, run from repository root
lane platform  Linux x86_64, CPython 3.11.15, 10/10 and 5/5 ALL PASS
```

Carrier reproduction, recorded because it is the load-bearing input: the
lane re-ran the pinned public probe `P-ENTROPY-BRIDGE-3` unchanged and
obtained stdout byte-identical to its recorded pin
`a4600f241d499bef6eda8d1efa8fad082b054dcf7bbb5e10746c594401e4d32d`,
1612 bytes, 10 of 10 PASS. That is a third platform beyond the two recorded.

## 5. Dependency edges to add

```text
RG-NO-FLOW-ON-CORE    ENTROPY-BLOCK-HALVING  REQUIRES  the two-to-one block
                      structure whose monotonicity is the question
RG-NO-FLOW-ON-CORE    ENTROPY-LIVING-SET     REQUIRES  the four half
                      restriction bijections carry the algebraic route
RG-NO-FLOW-ON-CORE    DEF-ARCHITECTURE       REQUIRES  the declared branch
                      maps and driver define the flow graph
RG-GALOIS-NOGO        J-PROJECTIONS          REQUIRES  the archimedean
                      channel locations and the modulus dichotomy
RG-GALOIS-NOGO        WALL-CIRCLE-LEMMA      REQUIRES  the weights along the
                      Galois orbit are its N = 5 specialization
RG-STEP-NOGO          DEF-MJ                 REQUIRES  M_J is multiplication
                      by J
WALL-EXCESS-SELECTS-5 WALL-CIRCLE-LEMMA      REQUIRES  the closed form and
                      the full-sum clause are the whole input
```

Owner decision, not proposed here: whether `ENTROPY-LAYER-BRIDGE [O]` gains
a `BOUNDED_BY` edge to `RG-NO-FLOW-ON-CORE`. The lane found no argument that
the no-flow result constrains the measurable-selection question, and
declines to invent one.

## 6. Exact fold edits

`canon/REGISTRY.tsv`, four rows appended, tab separated, columns
`claim_id status scope canon_section evidence falsifier`, evidence a path or
the word inline and nothing else:

```
RG-NO-FLOW-ON-CORE	T	on the recurrent core of the driven kernel the directed graph with an edge x -> F_t(x) for each branch map t in {0,1} has 6250 nodes, 12500 edges and 313 strongly connected components of sizes 312 x 20 and 1 x 10, and no edge runs between two distinct components; consequently every C with C(F_t(x)) <= C(x) for both t and all x satisfies C(F_t(x)) = C(x) identically, so the block-halving structure carries no monotone C-function and no renormalization flow on the core, while the halving itself is re-derived exactly with every fiber of size 2; 9375 states lie outside the core and all 15625 are inside after exactly 3 driven ticks, a finite one-time relaxation; no claim about scales beyond the registered range, an all-scale law, central charge, stress tensor, conformal field theory, the c-theorem, the a-theorem, L5, L6, or any physical observable	3. The kernel and the census	probes/P-RG-NO-FLOW-1	fires if any inter-component edge exists among the 12500, equivalently if some core state x, branch t and nonincreasing C give C(F_t(x)) < C(x); fires if the graph route and the algebraic permutation route disagree; fires if the core is not 6250 on 313 attractors or any fiber has size other than 2; fires if the aarch64 and x86_64 transcripts differ
RG-GALOIS-NOGO	T	Gal(Q(zeta_5)/Q) = (Z/5)^* is cyclic of order 4 with generators 2 and 3, the generator orbit of the four archimedean embeddings is 1, 2, 4, 3, the generator exchanges the expanding and contracting channel at every step, and the WALL-CIRCLE-LEMMA weights along the orbit alternate 27/50, 3/50, 27/50, 3/50 in units of zeta(2); exhaustively over all 256 functions on the four embeddings no nonconstant weakly monotone function exists along any generator in either orientation and the four increments around the orbit sum to zero, so the Galois action cannot be a renormalization trajectory; the ordering 27/50 > 3/50 is untouched and only its reading as a flow is denied	3. The kernel and the census	probes/P-RG-NO-FLOW-1	fires if any nonconstant weakly monotone function along a generator of (Z/5)^* is exhibited
RG-STEP-NOGO	T	the characteristic polynomial of M_J is x^4 - 3x^3 + 4x^2 - 2x + 1 = Phi_5(x - 1) with N(J) = 1, Tr(J) = 3 and det(M_J) = 1, so M_J lies in GL_4(Z), and modulo 5 it permutes all 625 states with orbit lengths exactly 1, 4 and 20, so every state is periodic and no nonconstant weakly monotone observable exists along its orbits: the tick is not a renormalization scale	3. The kernel and the census	probes/P-RG-NO-FLOW-1	fires if det(M_J) is not 1 or if any state modulo 5 is non-periodic under M_J
WALL-EXCESS-SELECTS-5	T	normalizing by zeta(2) the WALL-CIRCLE-LEMMA full nontrivial-root sum is (N-1)(N-2)/(2N) and its excess above 1 is (N^2 - 5N + 2)/(2N), which equals 1/N if and only if N(N - 5) = 0 and hence for exactly one integer N >= 3, namely N = 5, while the channel ratio (N-2)^2/(N-4)^2 equals 9 for exactly one integer N >= 3, namely N = 5; the registered excess 1/5 = 1/p and ratio 9 are therefore specific to p = 5 in contrast to the p-generic rung, and the per-pair deficit (N-6)^2/N^2 reaching 1/N^2 at N in {5,7} is explicitly NOT specific and is inadmissible as evidence; no selection argument for p = 5 and no imaginary-part, field-trace, substrate, normalization, regularization or physical claim	16. p = 5 and the wall	probes/P-WALL-EXCESS-5-1	fires on any integer N >= 3 other than 5 with excess 1/N or channel ratio 9, or if the identity excess(N) = (N^2 - 5N + 2)/(2N) fails at any tested N
```

`canon/NORMATIVE.tsv`, four rows, columns
`item_id item_type claim_id status layer gate_ids statement_source`:

```
RG-NO-FLOW-ON-CORE	THEOREM	RG-NO-FLOW-ON-CORE	T	L4		canon/CANON.md::3. The kernel and the census
RG-GALOIS-NOGO	THEOREM	RG-GALOIS-NOGO	T	L1		canon/CANON.md::3. The kernel and the census
RG-STEP-NOGO	THEOREM	RG-STEP-NOGO	T	L1		canon/CANON.md::3. The kernel and the census
WALL-EXCESS-SELECTS-5	THEOREM	WALL-EXCESS-SELECTS-5	T	L1		canon/CANON.md::16. p = 5 and the wall
```

`canon/EVIDENCE.tsv`, four rows, columns
`claim_id evidence_id evidence_kind location sha256 hash_mode architecture_requirement`,
with `evidence_kind` REPRODUCTION, `hash_mode` bundle-manifest-sha256-v1 and
`architecture_requirement` two-architecture. The bundle hashes are computed
by the fold from the merged probe directories and are deliberately left
blank here rather than guessed.

`canon/CANON.md`, section 3, appended after the ENTROPY-BLOCK-HALVING and
ENTROPY-UNIQUE-PAST paragraphs, proposed prose:

> The word *renormalized* in ENTROPY-BLOCK-HALVING names the block
> construction, not a flow. On the recurrent core the directed graph of the
> two branch maps has 12500 edges and 313 strongly connected components of
> sizes 312 x 20 and 1 x 10, and not one edge runs between two components;
> equivalently, each branch map permutes its own half and both two-step maps
> permute a half. Every function nonincreasing along the branch maps is
> therefore constant along every edge. The halving is real and loses exactly
> one bit per fiber, but that bit is backward indeterminacy, not forward
> monotonicity, and no monotone C-function exists on the core
> (RG-NO-FLOW-ON-CORE [T]). The only irreversibility with a direction is the
> transient: 9375 states lie outside the core, and all 15625 are inside it
> after exactly three driven ticks. That is a finite one-time relaxation,
> not a flow between two fixed points. The two other structures that have
> been proposed as scale carriers are excluded outright: the Galois action
> is cyclic of order four and its generator exchanges the expanding and
> contracting channels, so it is an involution on the channel quotient and
> not a trajectory (RG-GALOIS-NOGO [T]); and M_J lies in GL_4(Z) with orbit
> lengths 1, 4 and 20 modulo 5, so every orbit recurs (RG-STEP-NOGO [T]).
> No c-theorem or a-theorem statement is available to this program at this
> scope, and none is claimed.

`canon/CANON.md`, section 16, appended to the wall discussion:

> The rung itself is p-generic: WALL-CIRCLE-LEMMA holds for every N >= 3.
> Two of its readouts are not. The excess of the normalized orbital sum
> above one is (N^2 - 5N + 2)/(2N), which equals 1/N exactly when
> N(N - 5) = 0, and the channel ratio (N-2)^2/(N-4)^2 equals 9 exactly at
> N = 5. Both registered p = 5 values are therefore unique to p = 5
> (WALL-EXCESS-SELECTS-5 [T]). The per-pair difference is not: its deficit
> below one is (N-6)^2/N^2 and reaches 1/N^2 at both N = 5 and N = 7, so the
> 24/25 and 1/25 pattern carries no selection content and is inadmissible as
> a bridge to any one-bit structure.

`canon/FRONTIER.md`: no new rows and no rows closed. Explicit editorial
instruction for future sessions, to be carried in the fold note rather than
as a frontier row: `O-RG-SCALE-CARRIER` must NOT be opened, because the
carrier is already registered; and no `O-RG-C-FUNCTION` row should be
opened, because RG-NO-FLOW-ON-CORE answers it negatively.

`canon/CHANGELOG.md` and `canon/HISTORY.tsv`: one sealed integer-versioned
entry each, four DECLARE records at T.

`canon/STATUS_COUNTS.tsv`: claims 206 -> 210, status_T 107 -> 111, and the
evidence and reproduction counters recomputed by the fold tooling rather
than hand-edited here.

`canon/SHA256SUMS`: recomputed for all five normative files.

## 7. Break record: what the lane tried in order to kill this

```text
independent route     G07 proves the same conclusion algebraically with no
                      graph search: the four half restrictions are
                      bijections, so both two-step maps permute a half and
                      every nonincreasing C telescopes to equality. G06 and
                      G07 would disagree if either were wrong.
carrier drift         G01 to G03 re-derive the registered carrier invariants
                      before anything new is asserted, and the lane also
                      reproduced P-ENTROPY-BRIDGE-3 byte-identically.
self-inflicted bridge the lane proposed 24/25 = 1 - 1/25 as a bridge to the
                      one-bit halving, then killed it by the general-N form:
                      the deficit reaches 1/N^2 at N = 7 as well. Carried as
                      gate G05 of the sibling probe so it cannot come back.
counting check        9 is not a power of two, so no whole number of dyadic
                      steps reproduces the channel ratio; bit counting does
                      not join the two structures.
fabricated carrier    an early lane run used INVENTED generator bodies read
                      off a grep listing rather than the source. The carrier
                      gates failed immediately and exposed it. Recorded
                      because the result gate "passed" on that wrong carrier,
                      which is exactly the failure mode the G01 to G03
                      ordering is there to catch.
stale head            two fetches of the rendered STATUS.md page returned a
                      stale v2 copy. The clone is authority. Any session
                      verifying currency through a rendered page is
                      verifying nothing.
```

## 8. Reconciliation obligation, unresolved, owner decision

`AGENTS.md` requires every public claim to map to an internal claim of equal
or stronger status. The lane could not reach the private repository and does
not know whether sealed v184 carries a basis for RG-NO-FLOW-ON-CORE. The
v184 snapshot in the project does carry the recurrent core with 12500
directed edges and the 6250 / 3125 census (T-RECURRENT-GAUGE-QUOTIENT), so
the carrier reconciles; whether the no-flow theorem itself has an internal
antecedent is unknown here.

Three options, all legitimate, none chosen by this proposal:

```text
1  name an existing internal antecedent and fold at T
2  fold at C on the computation and leave T pending reconciliation
3  hold the fold until the internal line records the result, noting that
   v184 is sealed for scientific writes, which is itself an owner question
   about where genuinely new internal science now goes
```

## 9. What this proposal does NOT do

```text
It does not promote anything. No probe has been preregistered publicly, no
  branch pinned, no two-architecture run performed, no PR opened.
It does not weaken ENTROPY-BLOCK-HALVING, ENTROPY-LIVING-SET or
  ENTROPY-UNIQUE-PAST. It reads them and re-derives their invariants.
It does not claim an all-scale law.
It does not touch the private line, the site, or any physical row.
It does not settle the a-theorem lane. That lane needs its own dilaton
  carrier and is untouched here; the only thing this proposal adds is that
  the c-theorem route to it through the block halving is closed.
```
