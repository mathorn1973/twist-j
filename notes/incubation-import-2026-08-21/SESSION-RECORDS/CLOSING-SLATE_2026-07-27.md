# CLOSING SLATE, 26 live rows ranked

NON-CANONICAL. A scheduling note. It creates no claim, moves no status, and
changes no scope. Every decision condition quoted is the registry's own.

    date       2026-07-27
    basis      Public Canon v25, mathorn1973/twist-j main, tag canon-v25
               CONTENT_COMMIT b914755b422bf79a8be637993b2edaa12a4333f8
               canon/SHA256SUMS 5 of 5 OK, clone head ef1d2d91
    inventory  3 H, 23 O, 26 live
    purpose    closing phase. Rank by what can actually be finished, not by
               what is interesting.

## Method

Three inputs, all taken from the repository, none invented here.

    Queue field    canon/FRONTIER.md already carries
                   <ROOT|FOLLOWUP>; <STOP|READY|BLOCKED>; <kind> per row.
    Leverage       computed from canon/DEPENDENCIES.tsv, REQUIRES edges only,
                   restricted to live rows.
    Partial work   probes/ (34 pinned probe directories, all with PREREG,
                   RESULT and EXPECTED), notes/, and the five stranded
                   candidate lanes recorded in claude/CLEANUP-RECORD_2026-07-27.

One distinction the Queue field does not draw, and which decides most of the
ranking:

    work-STOP    the row is STOP because a proof, a witness, or a
                 classification has not been written. A session can lift it.
    owner-STOP   the row is STOP because a definition has not been frozen by
                 the owner. No session can lift it, and no amount of
                 computation substitutes.

## The structural facts

The live set is almost entirely flat. Of 26 rows, 21 have no REQUIRES edge to
another live row in either direction. There is exactly one dependency subtree:

```
METRO-REDUCTION-CALCULUS [O]          zero live blockers
   |-> METRO-ADMISSIBILITY [O]           --+
   |-> METRO-ADMISSIBILITY-DIM [O]       --+--> OBSERVER-WRITE-PORT [H]
QUADRATIC-DECODER-DATA [O]              --+
```

METRO-REDUCTION-CALCULUS is the only live row with nonzero leverage. It
unblocks three rows directly and OBSERVER-WRITE-PORT through them: five of the
twenty six live rows, one fifth of the inventory, sit on one root.

OBSERVER-WRITE-PORT is the terminal sink, blocked by four. It is the last
closeable row in the program, not a candidate for this phase.

The three H rows deserve separate attention because an H is a standing public
exposure that can fire, while an O is only unfinished work. None of the three
can be closed now: NS-TILT waits on CMB-S4, OBSERVER-WRITE-PORT waits on four
rows, and LAMBDA-COCYCLE-ANGLES is discussed in tier 3.

## Tier 1, close these. Finite, internal, no new physics.

### 1. METRO-REDUCTION-CALCULUS [O]   ROOT; work-STOP; FORMAL

The highest-leverage row in the program and the only one that is leverage
positive. It is STOP for want of proofs and witnesses, not for want of an
owner decision, so a session can lift it today. CANON.md already states the
full type, so the closing checklist is enumerable and closed:

```
4  declared allowed arrows, each needing a complete frozen precondition
   and a transport proof
     1  state relabeling by a bijection phi: S -> S'
     2  restriction to S_reach(P)
     3  the multi-action Nerode quotient, with the congruence proviso
     4  coordinate permutation fixing the ordered output basis
5  forbidden entries, each needing ONE exact witness
     flattening the N^a geometry; erasing named coordinate digit-word
     actions; arbitrary factor weights; output-dependent regrouping;
     replacing boxes by an unrelated ordering
3  remaining obligations
     invariance proved; common q^k blocking decided; approx_red proved
     complete for the registered class
```

Twelve obligations, all finite and exact. Arrows 1, 2 and 4 are near
mechanical: relabeling, reachability restriction and coordinate permutation
have forced transports. Arrow 3 carries the only real content. The five
forbidden witnesses are the tractable and satisfying part: each needs one
explicit small protocol P on which the transformation changes the decision or
the terminal value, and those live at tiny (q, a, r, |S|) and fall out of an
exhaustive integer search. This is a single preregistered probe with an exact
verifier, well inside the 120 second budget.

    Recommended as the first move of the closing phase.

### 2. TT-VECTOR-STATE-NORMALIZATION [O]   ROOT; READY; FORMAL

The most independent row in the inventory: no REQUIRES edge to any live row,
nothing bounded by it except POL-READ. Single deliverable, stated by the
registry itself as "the only gate yielding a numerical r_T(k)". Closes
positively by a public vector-doublet normalization producing that number, or
negatively if every admissible normalization violates a registered TT identity
or needs an extra free dimensionless input. Both branches are decidable by
work already scoped.

### 3. PHOTON-WINDOW-PROOF [O]   ROOT; READY; FORMAL, half closeable

Two obligations, and they are not of the same kind.

    (i)   every closed charge 5 worldline of length L satisfies
          F_occ >= kappa L, for admissible kappa with 2^(4 kappa) > 2401.
          Since 2401 = 7^4 this is exactly kappa > log_2 7. A finite
          combinatorial bound on an integer worldline family: the program's
          home ground, attackable now by exhaustive search plus a bound proof.
    (ii)  an electric face roughening certificate sufficient for the declared
          Froehlich-Spencer class import. An external import, not internal work.

    Recommendation: split the row so (i) can close on its own evidence.
    Carrying both under one id means finishing the tractable half buys no
    visible movement, which is how rows sit still for a year.

## Tier 2, re-target. The closing move is not the one being attempted.

### 4. ENTROPY-LAYER-BRIDGE [O]   ROOT; work-STOP; FORMAL

The most heavily worked row in the inventory and the clearest case of pushing
on a door marked pull. Ten dependency rows and six pinned probes
(P-ENTROPY-BRIDGE-1 through 4, P-ENTROPY-CURSOR-CLOSURE-1, P-ENTROPY-MIRROR-1).
Read the DEPENDENCIES basis column: ENTROPY-AFFINE-COCYCLE, ENTROPY-BLOCK-HALVING,
ENTROPY-COUNT-MATCH, ENTROPY-MIRROR-LAW, ENTROPY-PENTAGON-QUOTIENT and
ENTROPY-UNIQUE-PAST each say, in the canon's own words, that they constrain but
do NOT construct an element of A_A. ENTROPY-CYLINDER-NOGO-CURSOR excludes every
cursor for L = 4..32 at every finite lambda-depth.

Six honest attempts to construct, six results that constrain and none that
constructs, is evidence. The decision condition already licenses the other
direction: "closes negatively only by a complete theorem A_A = empty".

    Recommendation: stop attempting construction. Preregister an attempt at
    the negative theorem. A fired falsifier is first-class progress in this
    program and closes the row exactly as a construction would.

### 5. METRO-ADMISSIBILITY [O]   FOLLOWUP; work-STOP; FORMAL

Its own decision condition says it closes "only when all eight children close",
and that METRO-FINITE-STATE-RATIONALITY proves conditional rationality inside
only part of R1. One monolithic row standing for eight separate obligations
cannot show progress and cannot be partially closed.

    Recommendation: split R1 through R8 into eight registered children with
    their own decision conditions. This is bookkeeping, not science, and it
    converts an immovable row into eight movable ones. It raises the row count,
    which argues against it in a closing phase; it is listed here so the
    trade is explicit rather than accidental.

### 6. SCHEME-DICTIONARY, GENERATIONS-L3, QUANT-SUBSTRATE [O]   ROOT; READY

All three are READY with no live blockers, and all three are genuine
derivations rather than bookkeeping. No partial work exists for any of them in
probes/ or notes/. They belong on the slate and should not be expected to
close quickly. GENERATIONS-L3 is the crispest of the three: a single integer,
with the negative branch armed if the derived count differs from three.

## Tier 3, parked. Cannot be closed by any internal work.

Naming these matters. Carried in the same list as tier 1 they read as backlog;
named as parked they stop distorting the count.

```
NS-TILT [H]             waits on CMB-S4. The falsifier is already written and
                        the program does not control the data. Expect it to
                        decide against the tilt.
QNM-LEAVER-MU [O]       waits on an external shadow measurement plus a public
                        inference rule.
ALPHA-S-RUNNING [O]     the derivation is internal but the close needs a
                        measured comparison at a named scale.
NEUTRON-DELTA-EM [O]    same shape: closes negatively against a measured tier
                        window.
LAMBDA-COCYCLE-ANGLES [H]  marked READY, and it is not. Its falsifier fires
                        if a single ordinate Cayley angle 2 arctan(1/(2 gamma))
                        is PROVED outside 2 pi (1/4) Z[1/5]. That hypothesis
                        forces 1/(2 gamma) = tan(pi r) for an explicit rational
                        r, hence forces gamma algebraic. No transcendence or
                        irrationality result of that strength is available for
                        zeta ordinates, so the clause is not provable with
                        current mathematics. The second clause, on the Li
                        second differences along n = 4 . 5^A, is the only
                        clause with a real attack surface.
```

Recommendation: mark the four empirical rows PARKED-EMPIRICAL in the scheduler
label, and re-read LAMBDA-COCYCLE-ANGLES from READY to BLOCKED, or narrow its
falsifier to the second clause. That is a scheduler correction, not a claim
change, and it makes the READY list honest.

## Tier 4, free. Reduces open lanes without touching a live row.

None of these close a live H or O. All of them reduce standing exposure or
finish work that is already done, at low cost, which is exactly what a closing
phase is for.

```
1  P-C8-BILINEAR-SHADOW-2. RESULT.md reads "6/6 ALL PASS", proof-first
   theorem candidate at T, L1 scope, no local falsifier fired, and only the
   required GitHub x86_64 leg pending. There is NO registry row for it at
   v25 (grep count zero). Completed, verified, pinned science with one CI run
   and one fold left. The single cheapest piece of unfinished business in the
   repository.
2  The four PROMO-J-LI-* proposals. They target a v6 to v7 fold that never
   happened and their three verifiers exist in no repo file. Retire or record
   an F. Do not carry them further.
3  C-ENTROPY-RESIDUE-1. Six proposed rows targeting Canon v2, zero hits
   anywhere in the repository. Retire.
4  C-COLOR-MEASURE-DIM-1. Targets Canon v5; v22 retyped the parent
   COLOR-MEASURE-SELECTION to a much stricter STOP surface. Rebase before any
   fold, or retire.
5  C-KERNEL-SUBSET-LANDSCAPE-1. Carries a first-class fired falsifier and its
   rider row appears in no repo file. Archive as F.
6  canon/CANON.md section 11 carries an unlabelled claim, "The Fibonacci
   category with central charge c = 14/5 is mathematical background", with no
   backing registry row, inside a hashed normative file. Delete the clause.
   Carry it as a rider on the next fold; do not spend a fold on it.
```

## One owner decision that unblocks a row

TM-SYM2-PHYSICAL-MEASURE [O] is the one owner-STOP in the inventory. Its own
scope says "no successor L5 source is presently frozen" and requires a
"separately owner-approved successor L5 source". No session can lift it and no
computation substitutes. It is either approved, or it is retired. Leaving it
STOP is the only option that costs something every time the list is read.

## Summary ranking

```
rank  row                            why
  1   METRO-REDUCTION-CALCULUS       only leverage-positive row; unblocks 5 of
                                     26; 12 finite exact obligations; work-STOP
  2   TT-VECTOR-STATE-NORMALIZATION  READY, zero live dependencies, one number
  3   PHOTON-WINDOW-PROOF (i)        READY, finite combinatorial bound,
                                     kappa > log_2 7; split the row first
  4   ENTROPY-LAYER-BRIDGE           re-target to the negative theorem
  5   GENERATIONS-L3                 READY, crisp, but a real derivation
  6   SCHEME-DICTIONARY              READY, real derivation
  7   QUANT-SUBSTRATE                READY, real derivation
  8   METRO-ADMISSIBILITY            split into eight children, or leave
 ...  the remaining STOP rows        each needs its own definitions frozen
 --   4 empirical + LAMBDA-COCYCLE   parked, not closeable internally
 --   OBSERVER-WRITE-PORT [H]        last, blocked by four
```

## Falsifier for this note

Wrong if any Queue field, REQUIRES edge, probe RESULT status or registry row
count quoted above differs from mathorn1973/twist-j at the stated commit; if
METRO-REDUCTION-CALCULUS is shown to have a live REQUIRES blocker; if any row
called parked has an internal closing route; or if the twelve METRO obligations
are not the complete set stated by CANON.md.
