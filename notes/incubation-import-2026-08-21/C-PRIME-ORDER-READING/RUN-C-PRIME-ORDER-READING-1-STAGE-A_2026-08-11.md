# RUN C-PRIME-ORDER-READING-1, stage A accepted run, 2026-08-11

Candidate, no authority. Accepted run declared by the pins below, per the
corrected incubation discipline. Sequence of the day, in order: owner ANO
(blocks 1b, 2a, 3a, 4a) -> prereg frozen -> Field 2 path B defect discovered
at specification review, disclosed and corrected by ADDENDUM 1, still before
any code -> verifier written -> leg 1 run -> leg 2 run. No threshold moved
at any point.

## Pins

```
prereg    PREREG-C-PRIME-ORDER-READING-1.md
          sha256 6f90df5d23c8900c80a08c69a06eb70279a8692f18cb53365566320e58cfee21
          6440 bytes, frozen before any code
addendum  PREREG-C-PRIME-ORDER-READING-1-ADDENDUM-1.md
          sha256 ecc770bf9387834f2d5b98707b355b3aaced51efe83e6d7425694d169268f735
          1974 bytes, Field 2 path B correction (vacuity on cross-prime
          pairs, the id-1 class of defect caught at spec time), frozen
          before any code
verifier  verify_prime_order_reading_1.py
          sha256 307dd0c17f922b46566f12ebf6af93b120f151004534d527c7cecae765a28b4c
          7460 bytes
stdout    por1.out
          sha256 f7b40278da52c642dd1ed1e2f4d77d505d44d9fdfd106b03b1e27575accddac5
          455 bytes, SUMMARY PASS=8 FAIL=0, exit 0
leg 1     x86_64, glibc 2.39 cloud container, CPython 3.11.15, wall 0.13 s
leg 2     aarch64, Debian GNU/Linux 13, CPython 3.13.5
          verifier hash identical and stdout byte-identical on both legs
env       LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
```

## Results, candidate labels only

```
candidate-T  A1 REDUCTION LEMMA. Class equality on the rapidity circle is
             equivalent to the exact divisibility n | y^2 in Z[phi]
             (y = w_p sigma(w_q) direct, w_p w_q conjugate, w_p alone for
             fixed points), independent of generator choice. Written sketch
             frozen in the prereg; NOT yet independently reviewed. The
             three-way agreements (G4, G7, G8) are consistency evidence,
             not proof.
candidate-T  A2 PROP-1. The divisibility never holds: the unordered
             rapidity class is injective on split primes and avoids the
             involution fixed points. Universal statement rests on the
             written sketch (squares of Q(sqrt5) meeting Q, norm signs);
             the verifier is an audit at finite scope.
candidate-C  A3 AUDIT below 2000. 146 split primes; 21170 cross-prime
             collision tests, 0 collisions, path A and path B agree
             21170/21170; 146 fixed-point tests, 0 hits, three-way
             agreement 146/146; 30/30 negative controls fired in both
             paths; construction diagonal exactly-one-match 146/146.
```

## Interpretation inside the candidate

The canonical v44 circle data separates all 146 split primes below 2000,
and, if the sketch holds, all split primes. Combined with floor F3 of the
definitional doc, the order deficit of the J-language is exactly the
winding number, the unit ambiguity. The P_J problem sharpens to: a
canonical section of the unit action, or a machine time that supplies the
winding.

## Open before any promotion talk

```
1  Independent review of the A1/A2 written proofs (they are sketches).
2  Breaker, step 4 of the lane: an independent attempt to construct a
   collision or to break the reduction lemma by a second reading.
3  Stage B under owner ANO-1 (b): formalize D1 against the METRO U_RF
   protocol class; evaluate the definitional kill condition under (b).
```

No registry, frontier or canon line moves. No public probe opened.
