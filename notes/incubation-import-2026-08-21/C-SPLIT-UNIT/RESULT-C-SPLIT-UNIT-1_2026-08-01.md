# RESULT C-SPLIT-UNIT-1

NON-CANONICAL. Incubation-lane candidate result. No authority, no Canon change.

```text
CANDIDATE   C-SPLIT-UNIT-1
DATE        2026-08-01
BASIS       Public Canon v30, tag canon-v30,
            content commit 857223fcd5e7bc8c8e68f1df768d6e8222b24ee0,
            CANON_SHA256 2a32dcbd..., 157167 bytes, SHA256SUMS 5 of 5 OK,
            tag and content commit verified ancestors of main (fresh clone)
```

## Pins

Frozen before first execution (FREEZE.sha256, recorded pre-run):

```text
PREREG-C-SPLIT-UNIT-1_2026-08-01.md
  f1278995449b1023c2e47589ad80e11ec003dbd78a0317d46e7bb09723ecdca5
verify_split_unit_1.py
  5094d5fb15e1369dea760959c89fc4b6a5b050363427151142d88a56e275b913
break_split_unit_1.py
  601661172325e5335d88f66f443f9cb0737f33dde89b368d130f2cfecb30b782
```

Runs, both under LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0
TZ=UTC, script hashes verified identical on both machines before running:

```text
leg 1  x86_64, Linux cloud sandbox, Python 3.11.15
leg 2  aarch64, Ubuntu 24.04, Python 3.12.3 (internal relay runner)

verify_split_unit_1.py    exit 0 both legs, 38 gates, 38 PASS, 0 FAIL
  stdout 2326 bytes
  sha256 0855c66111d26a72968f1a3823f357c2f2a5ed3e86048836b402849756ebd5b3
  byte-identical across the two architectures
break_split_unit_1.py     exit 0 both legs, 8 gates, 8 PASS, 0 FAIL
  stdout 903 bytes
  sha256 d346745d1793d4e1642fa774aefe681724787dfa0fbd339e7e2316b63363fd9b
  byte-identical across the two architectures
```

No falsifier fired. No threshold moved. The two-architecture byte-identity
condition of public POLICY section 4 is met by these two legs; the pins above
are incubation pins, not a public probe, so every label below stays a
candidate label.

## Outcomes by claim

```text
E1 SIZE      candidate-T   sigma_a(J) sigma_(5-a)(J) = phi^(-2 chi5(a)) exact
                           in Z[phi]; gates C1..C5; independent charpoly path
                           K1 gives (x^2 - 3x + 1)^2. Consistent with J-UNIT
                           [T] and J-PROJECTIONS [T]; adds the character form.
E2 GAUSS     candidate-T   sum chi5(a) zeta^a = 2 phi - 1, square 5, twist
                           identity for all b (D1..D3). The value tau =
                           2 phi - 1 = sqrt 5 is already registered publicly
                           inside ALPHA-PREFACTOR-UNIFICATION [T]; this lane
                           adds nothing to that row and cites it.
E3 ORBIT     candidate-T   the units of the form 1 + torsion are exactly the
                           four Galois conjugates of J (E1..E3 gates, full
                           enumeration of mu_10 = a proof at L1; second path
                           by Sylvester resultants, K2a..K2b). With
                           Kronecker's theorem: up to Galois relabeling, J is
                           the unique unit of Z[zeta_5] equal to 1 plus a
                           pure phase. The axiom's additive shape is forced.
E4 BIT       candidate-T   one subgroup of index 2; one real nontrivial
                           character; {1,4} = squares = {+-1} (three faces of
                           one bit, a p = 5 coincidence: squares = {+-1} iff
                           (p-1)/2 = 2 iff p = 5); sector census: exactly one
                           complex doublet iff p = 5, zero at p = 3
                           (F1..F4, K3, K3b, K3c; enumeration = proof).
E5 ARG       candidate-T   arg sigma_a(J) = pi (2, -1, 1, -2)/5 principal;
                           trivial and chi5 components exactly zero;
                           conjugation-odd; 5 r_a = Re[(2+i) chi(a)]
                           (G1..G7). The modulus datum is pure chi5 sector,
                           the argument datum is pure doublet sector. Note
                           |2 + i|^2 = 5, the Gaussian prime above 5 of the
                           registered Z2-PLACES-SPLIT [T].
E6 LATTICE   candidate-C at range, resting on classical [T, literature]:
                           all 78 units with coefficients in [-4,4]^4 lie on
                           the chi5 size line in even phi powers with inverse
                           pair product (H1, H2); all 58 units in [-2,2]^4
                           are literally +-zeta^k phi^m (K4). Classical
                           structure U = <-zeta> x <phi> (Kummer; Washington
                           Thm 4.12, Cor 4.13) makes the all-units statement
                           [T, literature]: the size lattice is Z ln(phi)
                           chi5 and J sits at quantum m = -1, minimal |m| = 1
                           (H4, K5).
E7 ZERO      candidate-T   witnesses of the skeleton: sum chi5 = 0; a
                           projector pair with [P,Q] != 0, Tr[P,Q] = 0;
                           conjugation projectors e+- with epsilon^2 = 1
                           (I1..I3). The unifying one-line theorem (the
                           trivial isotypic projection of any nontrivial
                           sector object is zero) is stated with proof in the
                           candidate doc.
E8 ANCHORS   candidate-T   N(J) = 1, Tr(J) = 3, J phi = j, (J-1)^3 = j,
                           J^5 = phi^-5 (B1..B6), matching the Canon anchors.
```

## The break attempt (what was tried)

Independent second paths, not reruns: Faddeev-LeVerrier characteristic
polynomial against the direct conjugate product; Sylvester resultants against
the product-of-conjugates norm; brute force over all 16 sign maps against the
subgroup enumeration; direct membership in {+-zeta^k phi^m} against the
modulus-only test. Constructed counterexample attempts: the non-unit
1 - zeta against the size gate (rejected, as it must be); the partition map
(+, +, -, -) as a fake bit (not multiplicative); {1,2}, {1,3}, {1,2,3} as
fake index-2 subgroups (not closed). Nothing broke.

## Honest deflation, recorded

Two of the owner's headline facts do not single out J and must never be
quoted as if they did:

```text
1  sum_a log|sigma_a(u)| = 0 holds for EVERY unit u (product formula).
2  the log-size vector proportional to chi5 holds for EVERY unit of
   Z[zeta_5]: conjugation forces |sigma_a(u)| = |sigma_(-a)(u)|, and
   |N(u)| = 1 forces the second pair to be the inverse of the first.
   Two lines, no unit theorem needed.
```

What does single out J: E3 (unique unit of shape 1 + pure phase, up to
Galois) and E6 with H4 (minimal quantum |m| = 1 of the unique bit). The
grammar belongs to the field; J is its forced minimal carrier.

## What this run does NOT establish

No physical dictionary, no driver, selector, or decoder derivation, no
curvature operator, no measure, no E_total statement, no change to any Canon
row. The [D] ontology reading and the [H] completeness claim of the candidate
doc are ungraded by these runs. A0's explicit non-uniqueness disclaimer
stands untouched.

## Files

```text
claude/C-SPLIT-UNIT-1.md                      candidate claim and scope
claude/PREREG-C-SPLIT-UNIT-1_2026-08-01.md    frozen prereg
claude/verify_split_unit_1.py                 pinned verifier
claude/break_split_unit_1.py                  pinned break attempt
claude/split_unit_1.stdout.txt                verifier stdout (both legs)
claude/split_unit_1_break.stdout.txt          breaker stdout (both legs)
claude/RESULT-C-SPLIT-UNIT-1_2026-08-01.md    this record
```
