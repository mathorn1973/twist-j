# RECON pair-first, k4, after the fired third cut, 2026-08-11

NON-CANONICAL discovery, no claim, no freeze. Machinery imported from the
pinned cut-3 verifier (2bf4bf01...). Real neighborhoods explored here
deliberately; any successor candidate wanting real-anchored domains must
declare it in its own prereg. Script recon_pair_first_k4.py, log
recon1.log, both in the fleet handoff repo.

## R1, the G6 pair anatomy is an O(5) coincidence

All four isotypic COMPONENTS of the pair differ, including [22], and no
S_4 element maps the twin to the real. The equal gram22 data is
therefore equality of Gram matrices with genuinely different component
vectors: the pair is identified by the orthogonal-group quotient the
Gram construction takes, not by symmetry and not by component equality.
Consequence: the owner [H] cannot be saved at degree 2; if orientation
lives in [22] at all, it lives in degree >= 3 invariants of that
sector, OUTSIDE the frozen parent map.

## R2, gram22 twins are generic near the reals

E = D + all two-profile tables within Hamming 2 of the seventeen reals:
34312 tables (+1: 19552, -1: 14760). gram22 has 116 MIXED buckets on E.
The G6 twin was not a fluke; the flip-domain PASS of Q1 was a domain
artifact. gram22 sufficiency is dead on every real-anchored domain
tried.

## R3, fragility of small deciders

```text
d_min(D) witness, four sums          BROKEN on E
sums10, all ten sums                 BROKEN on E
gram22, the fifteen [22] Gram        BROKEN on E
eight sums + full gram211 (cost 14)  STILL DECIDES E
```

d_min trajectory: 4 on D, 7 on E (six sums + one [211] diagonal). Small
deciders keep existing and keep dying as the domain grows; the one
survivor so far leans on sums and [211], the opposite of the [H].

## R4, two would-be theorems killed before anyone froze them

full109 SEPARATES E by flow (34311 buckets on 34312 tables). But the
one duplicate-vector pair, 0x4d21ed2f85b5c190 and 0x6d21ef0f8595c190,
has equal 109-vector, SAME flow, and lies in DIFFERENT S_4 orbits (0 of
24 elements relate them). So: the 109 map does not separate orbits, and
any coverage theorem via orbit separation is refuted; the target must
be flow decision directly. And: no invariant-map counterexample to
"full109 decides" has appeared at any domain tried.

## What this arbitrates

Route 3 is complete; it did its job in one run. Route 2, a structural
sub-stratum without a completeness certificate, is now known to keep
manufacturing d_min artifacts; it is route 3 with extra steps. Route 1
is the only principled exit, with the target corrected by R4: not orbit
separation but flow decision over the true two-profile locus.

Concrete frozen questions the successor could carry, owner's pick:

```text
T-A  Does the full parent map decide the stratum: equal 109-vector and
     two-profile implies equal flow? The E-duplicate is consistent with
     it; unknown mechanism; this is the coverage anchor.
T-B  The surviving cost-14 object, eight sums + gram211: break it on
     harder domains, or freeze it as the candidate stable decider with
     its own falsifier.
T-C  The [H] retreat: construct the degree-3 invariant layer of the
     [22] sector (beyond the O(5) quotient), then re-pose sufficiency.
     New structural layer, outside the parent map, needs its own
     ambient accounting in the prereg.
```

Recommendation, one line: successor on route 1 with T-A as the central
frozen question and T-B as its finite break arm; T-C stays available as
the [H] retreat if the owner wants it posed at all.
