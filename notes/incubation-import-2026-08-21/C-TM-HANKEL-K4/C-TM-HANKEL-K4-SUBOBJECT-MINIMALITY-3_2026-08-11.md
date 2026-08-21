# C-TM-HANKEL-K4-SUBOBJECT-MINIMALITY-3: FIRED, first-class, 2026-08-11

```text
STATUS:  incubation candidate, FIRED on Q2 and on the G6 extension break.
         Archived, not hidden. No integrity STOP: the verifier behaved,
         both firings carry independent in-run rechecks, and the whole
         stdout is byte-identical on two architectures.
PREREG   sha256 691763da2dd4ac40327e394c148ef65bc79a8c36ad60f8b04a16a658472dbc5e
VERIFIER verify_tm_hankel_k4_subobject_minimality_3.py
         sha256 2bf4bf0193868a7a04b4ae01a053cb53ab898cfa129409a35b97ae0c81e93242
         38061 B, assembled from the pinned parent verifier 88c07a22622e...
         (machinery unchanged) plus the frozen cut-3 gates
STDOUT   sha256 d55541c7c1ecd339b9e39372b06ae52a99373ff5b06e2d7b02ce17d0461f947d
         3598 B, exit 1 (fired), empty stderr
LEG 1    x86_64, formal run with separated streams
LEG 2    aarch64, byte-identical stdout, empty stderr
         (a first assembly run with merged streams produced the same
         bytes; determinism witnessed three times)
```

## Outcomes, in the frozen order

G1 [PASS] Domain D built exactly as frozen: base 3 (!), after single
flips 165, after double flips over the first 40: 19448 tables, flow +1:
9573, flow -1: 9875. The seventeen reals used in no construction step;
zero coincidental bit equalities.

G2 [PASS] Multiplicities (10, 12, 5, 3, 0); parent_coordinates 109;
atoms 30; ambient accounting 154 by both exact paths; the owner's
disclaimer statement printed: Q2 asserts minimality only among
subobjects of the parent map.

G3, Q1 [PASS, candidate-C on D] gram22 decides orientation on D: 2837
buckets, none mixed.

G4, Q2 [FIRED] The first maximal configuration tested already decides
D: B = eight orbit sums + the full gram211 block, cost 14, confirmed by
the independent direct pair loop. Parent-subobject minimality of gram22
is FALSE on D.

G5 [diagnostics] 1000 cost-15 deciders found before the print cap;
sums10 separates D (1441 buckets), gram31 separates, gram22 separates,
gram211 COLLIDES (consistent with the cut-2 kill), full109 separates.

G6 [FIRED, extension break] Among the seventeen held-out reals, exactly
one collides on gram22 with a D table of opposite flow. Q1 on D is
untouched; the EXTENSION of Q1 one step beyond D is dead.

## Post-run diagnostics (separate script, not the pinned verifier)

```text
d_min on D = 4.  Witness: FOUR orbit sums, B = {1, 2, 3, 5}, no Gram
                 block at all, independently rechecked by the direct
                 pair loop. Costs 1 to 3 have no decider.
G6 witness pair: real n = 1732991217 = 3.71.347.23447, flow +1,
                 against abstract table 0x2e439572cd318eda, flow -1,
                 equal on all 15 gram22 entries. The abstract twin sits
                 at Hamming distance 3 from the cut-1 witness
                 0x02e639472cd318ed2: it is a double-flip descendant of
                 the witness neighborhood.
Pair anatomy:    the two tables differ in 76 of 109 coordinates:
                 sums10 in 7 of 10, gram31 in 63 of 78, gram211 in 6 of
                 6, gram22 in 0 of 15. For the one genuinely hard pair
                 in hand, the orientation information lives everywhere
                 EXCEPT the [22] sector.
```

## Honest reading

The two firings are coherent and point at the same object: the domain.
D, though a hundred times the cut-2 pool, is the flip neighborhood of
three LCG tables and one witness; on such a correlated set, four orbit
sums suffice to decide orientation, so any minimality statement is
dominated by domain geometry, and gram22 sufficiency passes only
because D never manufactures a gram22 twin with opposite flow. The
first contact with an independent point, the held-out real 1732991217,
produces exactly such a twin. Both firings are findings about
flip-sampled domains, not yet about the stratum.

The owner hypothesis that orientation lives in [22] stays [H] by the
frozen prereg, but the one hard pair in evidence carries its
orientation entirely outside [22]. The pressure on the [H] is real and
is recorded as such.

## The fork this leaves for the owner

1. Coverage route: replace domain sampling by the agreement-pattern
   antichain over the true stratum, the A_opp(D) = A_opp(S) theorem
   named at the freeze. Hitting certificates make this the principled
   exit, and the G6 pair shows sampled domains will keep lying.
2. Structural domain: an exactly enumerable sub-stratum (a frozen coset
   or weight class swept completely) so that "on D" is a structural
   statement rather than a neighborhood artifact.
3. Pair-first recon: treat the G6 pair as the central object; find the
   minimal invariant set separating THIS pair and its orbit, before
   posing any new global question.

No new claim is made here. The candidate is dead under this id per its
own Field 5; a successor takes a new name after the owner picks the
fork.
