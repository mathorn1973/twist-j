# PROMO-C-READ-REDUNDANCY-1

Promotion proposal. One doc a fold can consume without reading anything
else. Candidate carries no authority; validation is public, not here.

```text
CANDIDATE    C-READ-REDUNDANCY-1
              prereg sha256 334cb3bf9ef6feaccaa7e48c809e0f2f880c6686c025eee96474fb31c743d0d2
TARGET       public line, mathorn1973/twist-j main, as a new probe
             P-READ-REDUNDANCY-1 plus one T row and frontier prose under
             the existing MINIMAL-READ-DERIVATION [O]. Additive; no
             existing row changes status or scope.
PROPOSED BY  incubation lane session, 2026-07-29 (workstream A of
             claude/PLAN-DECODER-SECTOR-POST-V27_2026-07-29.md)
CONTEXT      route precondition 5 of
             notes/canon/ADOPT-COIN-MINIMAL-READ-2026-07-29.md section 5
```

## Exact statement (proposed status T after the public probe)

Let S be a set of primes, Z_S the localization of Z at S, and m >= 1.
Call an accumulator anonymous and total when it is a polynomial map in
R[x_1..x_m] invariant under every permutation of its m inputs; this is
equivalent to an arbitrary feedback-free acyclic circuit over
{+, x, constants of R} with permutation-invariant output.

```text
T (proposed)  READ-REDUNDANCY-PRIME-SUPPORT, layer L5 over the L1 coin
              carrier, no lift.
  (i)   An anonymous total accumulator over Z_S returning the common
        input value identically at multiplicity m exists iff every prime
        factor of m lies in S. Necessity: in the monomial symmetric
        basis the diagonal identity forces, on its weight-1 stratum, the
        single equation m c = 1 in Z_S, because (1) is the only weight-1
        partition and diagonal degree equals weight. Sufficiency:
        (x_1 + .. + x_m)/m.
  (ii)  Without anonymity the bound is void: a typed projection funnel
        (wire from one typed port to the output, zero arithmetic)
        carries every m over Z, in particular m = 6 with translation
        invariant offset types.
  (iii) Without totality the bound is void: the partial common-value
        map on the diagonal carries every m.
  (iv)  Corollary on the registered coin pair (generic multiplicities 2
        and 6, rung multiplicities 1 and 5, per
        COIN-SELECTION-CONDITIONAL): for any S with 3 not in S,
        multiplicity 6 is obstructed while 2 carries whenever 2 in S,
        1 is free over Z, and 5 carries iff 5 in S. In particular over
        the registered places {2} and {2,5} the anonymous total sixfold
        read does not exist and the twofold read does.
```

## Falsifier (for the T row, inline)

A symmetric total polynomial accumulator over Z_S returning the common
value identically at a multiplicity m with a prime factor outside S; or
failure of the typed projection or diagonal common-value witnesses on
their stated domains; or a weight-1 partition other than (1); or a
monomial symmetric function whose diagonal degree differs from its
weight.

## What the row does for the frontier (prose, no status change)

The no-feedback route to MINIMAL-READ-DERIVATION [O] is refined, not
closed. Refinement: absence of feedback alone tolerates arbitrary
finite read multiplicity (clause (ii) is exactly the tolerance
statement anticipated by the route note, which declares that such a
proof kills the route only). The surviving route runs through two
decoder definitions the O row already lists as missing, now reduced to
named bits with known prices: whether the cover-to-output map presents
sheets anonymously (anonymity), and whether the accumulator is total
rather than diagonal-partial (totality). Given both, the redundancy
bound is the prime-support condition of (i), and among the registered
pair the sixfold read costs the prime 3, which the constant ring does
not carry. The O row stays O and STOP per its own decision text;
COIN-MINIMAL-READ stays H.

## Verifier and pins

```text
verify_read_redundancy_1.py  sha256 3febde99b4f0c328452bf435406b689a24343c576959f58368b96107b6e5fdcf
                             stdout 05d567dc19a3705e7de6fcae4a91cc85964c1b2207d7c2da4fead959d901f3ef
                             exit 0, 13/13 PASS
break_read_redundancy_1.py   sha256 ac22ddb164d3d835d0f7bac32ea9e33f62f9b2bbc0ec49ce0aec49f347229482
                             stdout 4e4aa7b5b1f7ac0fac1f8df754ec68774d4ac55176103cbd655e35dd54b3f2da
                             exit 0, NO FALSIFIER FIRED
Independent legs: 390625 integer symmetric candidates at m = 2, zero
diagonal identities; 2 x 1922375 dyadic candidates at m = 6 in two
families, zero; witness survived 50 exact values (Q and Q(sqrt5)) under
8 port orders. ONE platform so far: the public probe must rerun the
merged verifier on two architectures with byte-identical stdout; until
then computation rows are at most C and every label is a candidate
label. The symbolic proof of (i) is four lines and checkable by hand.
```

## Dependency edges

```text
Uses      COIN-SELECTION-CONDITIONAL [T] (the pair and its generic and
          rung multiplicities 2, 6, 1, 5); DRIFT-IS-THE-READ [T] (read
          semantics and coherent range, used only to motivate the
          identity normalization); Z2-PLACES-SPLIT [T] and
          TWO-PLACE-PHYSICS [D] (the registered places motivating
          S = {2} and S = {2,5}).
Declared  the arithmetic-circuit model, the anonymity and totality
          clauses, and the ring identification are auxiliary hypotheses
          of the row, stated in its scope; they are the decision points
          of the O row, not theorems.
No edits  to any existing row's status or scope. Additive only.
```

## Exact edits the fold would make

```text
1  probes/P-READ-REDUNDANCY-1/: PREREG.md (six fields, public wording,
   from the candidate prereg), verify.py (merge of the candidate
   verifier and breaker legs into one file), EXPECTED.txt, RUN.md,
   RESULT.md after the two-platform run.
2  REGISTRY.tsv: add the T row above with its inline falsifier
   (schema: claim_id status scope canon_section evidence falsifier;
   evidence probes/P-READ-REDUNDANCY-1).
3  canon/FRONTIER.md: the MINIMAL-READ-DERIVATION entry gains the route
   refinement paragraph above. No decision condition changes.
4  canon/CANON.md: fold owner's call; registry plus frontier suffice.
   Integer-versioned sealed fold, new hashes, no squash.
```

## Claim check before folding

Check issues, branches, probes/ and the registry for collisions first.
As of 2026-07-29: 13 open issues, none touching redundancy, funnel,
accumulator, or MINIMAL-READ; no probe directory or branch named
P-READ-REDUNDANCY-*; no registry row on read redundancy.
