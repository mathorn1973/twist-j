# C-TM-HANKEL-K4-SPECTRAL-FLOW-2: freeze, run, break, pin

```text
STATUS:  incubation candidate, NO AUTHORITY, promotes nothing
DATE:    2026-08-11 (UTC)
BASIS:   Public Canon v43, main 981aa1b (re-read at freeze)
PARENT:  C-TM-HANKEL-K4-SUBSTRATE-1 (frozen substrate and canonical
         109-entry S_4-invariant map consumed unchanged)
PREREG   sha256 5a70438e9fd0ed858079e612e72034ede45487caf3ca9d239db27090a1e507c7  8213 B
VERIFIER sha256 88c07a22622e8dddc966a79b20c0c274eb3791823560e8dcf879b7640af41d0c  30725 B
STDOUT   sha256 dbef15d9379ce72a7e8bf197d1f511c11a05ec2bc5758ba5f09766bf8513044f  2957 B
         7 of 7 gates PASS, exit 0, empty stderr
LEG 1    Ubuntu 24.04 x86_64 Python 3.11.15
LEG 2    Debian 13 aarch64 Python 3.13.5, verifier reassembled from the
         local pinned substrate machinery plus SHA-checked tail chunks,
         byte-identical file hash confirmed before execution, stdout
         byte-identical
```

Frozen question (owner directive): which minimal S_4-invariant
information distinguishes the endpoint inertias NEG 7 ZERO 0 POS 9 and
NEG 9 ZERO 0 POS 7 on the frozen k = 4 substrate. Flow convention frozen:
upward crossing counts +1, SF = (sigma(1) - sigma(0))/2, so profile 709
forces SF = +1 and 907 forces SF = -1.

Two assembly defects were caught at first execution attempts, before any
gate produced a result: a missing Fraction import and a missing
det_bareiss splice. Crash-on-start build fixes, recorded, no gate logic
touched; superseded hashes 33632e00..., 80b858d1....

## Results

G1/G2 [candidate-C]. Every one of the 17 frozen real failures (n <= 4e9,
re-verified extremal, endpoints by three independent exact paths) has
EXACTLY ONE crossing of det(Kxor + sR) in (0,1), no multiple roots, and
the oriented walk realizes the endpoint flow exactly: orientation +1 for
all twelve 709 cases, -1 for all five 907 cases. At this range the real
k = 4 failure is always a single transversal event with a definite
orientation.

G3 [candidate-T; reproduces the sealed skeleton with an in-verifier
derivation]. Q[X_4] = 10[4] + 12[31] + 5[22] + 3[211], multiplicities by
exact character inner products, ranks of the five unnormalized isotypic
operators (10, 36, 10, 9, 0) by exact integer elimination. The [1111]
sector is absent: no pure sign channel exists on this substrate.

G5 [candidate-C, the discriminating find]. Pool of 182 two-profile
tables (97 flow +1, 85 flow -1; 4000 fresh LCG tables, one declared flip
round, the 17 reals):

```text
gram211 (6 entries)   COLLISION: tables 0x04d01ef3f8595c190 and
                      0x18a766e2734d2e754 have equal [211] Gram data and
                      OPPOSITE flow. The [211] sector alone does not
                      carry the orientation. First exact sector kill.
sums10  (10 entries)  separates on the pool (82 buckets)
gram31  (78 entries)  separates (173 buckets)
gram22  (15 entries)  separates (101 buckets)   <- owner H candidate, alive
full109               separates (182 buckets)
```

G4: on the 17 reals alone every layer separates; the reals are too few
to discriminate sectors by themselves.

Break attempt (independent code, sha 875e20a7...): B1 grid sign-change
count reconfirms one crossing per real failure with no shared isolation
machinery; B2 the [211] collision is genuine (profiles opposite by the
congruence path, [211] slices equal, sums differ, so the collision is
invisible to [211] but visible to the trivial sector); B3 a 25x wider
deterministic pool (4519 tables, 2604 vs 1915) still has NO
opposite-flow collision in sums10, gram22, or full109. All survived,
broken = 0.

## Reading, no claim beyond the searched domains

The orientation lower bound now stands as: [211] insufficient alone;
sums10, gram31, gram22 unfalsified as carriers on 4519 tables. The owner
hypothesis that the orientation lives in the [22] sector is alive and
untouched; the cheaper surprise is that the ten linear orbit sums also
survived as an orientation carrier on the searched domains, even though
the same sums provably fail to decide the balanced/nonbalanced CLASS
(parent candidate, exact collision). Orientation and class are therefore
separated by the linear layer differently, and the next kill shot should
target sums10 first: one opposite-flow sums collision would leave the
quadratic sectors as the frontier exactly as the owner wagered. G6
sufficiency stays unreachable by freeze; nothing here is a sufficiency
statement.

## Non-claims

No sufficiency of any layer at any search size; no irrelevance of [211]
inside larger layers; no census over 2^65; no RH, Weil, decoder,
physical, or L2-L6 statement; no registry row. The two owner hypotheses
(orientation in a new irreducible component with [22] first; decoder
positivity as prohibition of a flow orientation) are recorded as [H] in
the prereg Field 6 and were not evaluated as claims.
