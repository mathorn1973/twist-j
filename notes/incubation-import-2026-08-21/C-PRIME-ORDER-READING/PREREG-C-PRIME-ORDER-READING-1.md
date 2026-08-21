# PREREG C-PRIME-ORDER-READING-1, stage A (PROP-1)

DATE 2026-08-11. One named session, this candidate only.
CANDIDATE: C-PRIME-ORDER-READING-1, definitional doc
claude/C-PRIME-ORDER-READING-1_2026-08-11.md. No authority.
OWNER ANO 2026-08-11: ANO-1 (b), ANO-2 (a), ANO-3 (a), ANO-4 (a), applying
to the hashed blocks
165ba2c67a216d24d933727edb4a054eb9dcb733105ad0f2f6779e7eed0b7bef (ANO-1),
e6513dd7374a097f03c676004c4c571ef73f990a4106a9be71a8ef2aa8e19a90 (ANO-2),
fec11408ff9532ba80f6f1ab698dec6f8b7cca01eaf583135b9cb99a3e8dfa19 (ANO-3),
0915e117c7678cc94660fffc20c7a010eaa7c8cfa67465d412ca92ae6ea923f8 (ANO-4).
TARGET LINE ON PROMOTION: public mathorn1973/twist-j, gated this session at
Public Canon v44, STATE ACTIVE, tag canon-v44, content commit 9da73b96,
SHA256SUMS 5 of 5 OK.
INCUBATION DISCIPLINE: corrected Field 5 of the C-ARITH-RAPIDITY-4 lane.
This preregistration freeze is absolute. Verifier development and debugging
before the accepted run are ordinary disclosed work. The accepted run is
declared once, by pinning verifier and stdout hashes; after that pin any
defect, any gate name exceeding its test, and any check beyond this
specification is an integrity STOP.

SCOPE SENTENCE. Stage A of the candidate: the arithmetic floor PROP-1
(injectivity and fixed-point avoidance of the unordered split-prime rapidity
class of SPLIT-PRIME-RAPIDITY-CLASS [T]), its written proof, and a finite
exact audit below 2000. Explicitly NOT claimed: anything about P_J itself,
the L5 reading, existence, uniqueness, order, or any physical statement.

## Field 1. EQUATION (frozen claims)

Notation. F = Q(sqrt5), O_F = Z[phi], phi^2 = phi + 1,
sigma(a + b phi) = (a + b) - b phi, N(a + b phi) = a^2 + ab - b^2,
Tr(a + b phi) = 2a + b. Split prime: rational prime p with p mod 5 in
{1, 4}. w_p denotes a generator of a prime ideal above p (N(w_p) = +-p;
class number one). R(p) is the unordered rapidity class on
(R/(log phi)Z)/{+-1}.

A1 REDUCTION LEMMA (candidate-T). For distinct split p, q and any choice of
   generators: R(p) = R(q) exactly if and only if pq divides y^2 in O_F for
   y = w_p sigma(w_q) (direct match) or y = w_p w_q (conjugate match).
   R(p) sits at a fixed point of the involution exactly if p divides w_p^2
   in O_F. Both tests are independent of the generator choices (changing a
   generator multiplies y by a unit and y^2 by a unit square).
   Proof route frozen: exact class equality gives an integer k with
   u = y^2 phi^(-2k) / n of absolute value 1 at both real places, where
   n = pq (respectively p, allowing also odd exponents phi^(-k) in the
   fixed-point case); u = a + b sqrt5 with equal absolute values at both
   places forces a b = 0, the branch a = 0 dies on norms, so u = +-1 and
   the divisibility follows. Conversely divisibility gives the unit
   quotient and the exact class equality.

A2 PROP-1 (candidate-T). The divisibility never holds: for all distinct
   split p, q and both y choices, pq does not divide y^2 in O_F; for every
   split p, p does not divide w_p^2 in O_F.
   Proof route frozen: a quotient z = y^2 / n in O_F has N(z) = +1, hence
   z = +-phi^(2j), hence (y phi^(-j))^2 = +-n; the rational numbers that
   are squares in Q(sqrt5) are exactly the rational squares and five times
   rational squares, and n in {pq, p} with p, q distinct primes different
   from 5 is neither, while -n < 0 is not a square in a real field. The
   odd-exponent fixed-point branch dies on the norm sign:
   N(w_p^2) = p^2 > 0 while N(+-p phi^(2j+1)) = -p^2 < 0.

A3 AUDIT (candidate-C). For all split p < 2000 (asserted count 146) and all
   unordered pairs, two structurally independent code paths agree that no
   collision and no fixed point occurs, and every negative control fires in
   both paths.

## Field 2. CODE

verify_prime_order_reading_1.py. Python standard library only. Exact
integer arithmetic on coefficient pairs (a, b) representing a + b phi. No
float in any assertion or printed field. Runtime under 120 s. Environment
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC. Two
architectures, byte-identical stdout required for the C grade of A3.

Path A: the divisibility test of A1 (coefficient divisibility of y^2 by n).
Path B: canonical unit reduction, structurally independent of path A:
reduce each generator by multiplication with phi^(+-1) to the representative
of minimal |Tr|, normalize sign and conjugation by a frozen deterministic
rule, and declare collision exactly when reduced tuples coincide.
Generator constructions: path 1, bounded Pell sweep on |a^2 + ab - b^2| = p;
path 2, Euclidean gcd(p, k - phi) in O_F where k^2 = k + 1 mod p, every
division step asserted norm-decreasing. Diagonal consistency gate: for each
p the two constructions must land on the same ideal pair, witnessed by
exactly one of the two match types firing on the mixed diagonal pair.
Negative controls, mandatory: for at least 10 split p, the synthetic pairs
(w_p, w_p), (w_p, phi w_p) and the rational witness y = N(w_p) MUST be
detected by both paths; a verifier whose detector cannot fire is not
acceptable and its run is not declarable.

## Field 3. CARRIER OR DATA

No external data. Split primes below 2000 from the residue condition alone.
Everything else is internal exact arithmetic.

## Field 4. SYSTEMATICS

Generator ambiguity is the object under test; A1 removes it and A1 is itself
a frozen claim whose written proof is stage-A work. Vacuous-PASS risk is
handled by the mandatory negative controls. Single-path logic errors are
guarded by the two structurally different paths. Overflow: none, Python
integers. The lesson of the dead C-ARITH-RAPIDITY-1 gate (a gate name
exceeding its test) is inherited: every printed gate name must name exactly
what its assertion checks.

## Field 5. FAILURE THRESHOLD

A certified collision or fixed-point hit at range: PROP-1 dies as F,
archived, the threshold does not move. Path A versus path B disagreement on
any pair: integrity STOP. A negative control that does not fire: integrity
STOP. Any defect found after the accepted run is pinned: integrity STOP.

## Field 6. ACTION LAYER

L1 (state arithmetic), per owner ANO-2 (a): the candidate lives at L5 with
L1 floors and this stage is an L1 floor. No lift is claimed. FALSIFIER,
explicit: an exhibited pair of distinct split primes below 2000 (or one
split prime for the fixed point) with the A1 divisibility certified in
exact integers by both paths.
