# PREREG C-PRIME-BOOLE-1

DATE 2026-08-10. One named session, this candidate only.
CANDIDATE: C-PRIME-BOOLE-1. No authority. Incubation lane of the TWIST-J project.
TARGET LINE ON PROMOTION: public mathorn1973/twist-j (gated this session at
Public Canon v39, STATE ACTIVE, tag canon-v39, content commit ab17b104, 5/5
SHA256SUMS OK). Collision scan clean: no registry row or probe on the Boolean
skeleton of prime supports; nearest rows are FERMIONIZER [T] (the place-2 local
alternator), RAMIFIED-TM-LIFT [T] (carries the carry identity floor), and the
J-LI / LAMBDA-COCYCLE family (context only).
LAYER: L1 (state; arithmetic of the prime-support algebra). No lift to L2..L6
is claimed.

SCOPE SENTENCE. The Boolean skeleton of the positive integers under prime
support (AND = gcd, OR = lcm, XOR = squarefree kernel of the product), the
character theory of its two global alternators (mu on the squarefree layer,
lambda on all of N), the finite Euler-truncation dictionary tying that skeleton
to zeta, and one exact cosine anchor in the weighted-l2 geometry n^(-2 sigma).
Explicitly NOT claimed: any statement about the location of zeta zeros, any RH
progress, any J-coupling, any physical reading.

## Field 1. EQUATION (frozen claims)

Notation. For squarefree n, S(n) is the set of prime divisors; b_p(n) = 1 if
p divides n else 0; m o n := m n / gcd(m,n)^2 (the XOR product, defined on
squarefree pairs); mu is the Moebius function; lambda(n) = (-1)^Omega(n)
(Liouville); omega(n) = number of distinct prime divisors; x_p = p^(-t).

A1 SUPPORT MAPS. For squarefree m, n:
   S(gcd(m,n)) = S(m) AND S(n); S(lcm(m,n)) = S(m) OR S(n);
   z = m n / gcd(m,n)^2 is squarefree with S(z) = S(m) XOR S(n);
   and m n = z . gcd(m,n)^2 (the XOR part times the AND square).

A2 CARRY SPLITTER. For all integers a, b >= 0:
   a + b = (a XOR b) + 2 (a AND b) bitwise (the public floor sits inside
   RAMIFIED-TM-LIFT). Applied per prime exponent to squarefree m, n it is the
   factorization in A1: XOR is multiplication without overlap, AND is the
   birth of the square.

A3 MU IS THE XOR CHARACTER WITH AND ANNIHILATION.
   mu(n) = (-1)^omega(n) for squarefree n, and mu(n) = 0 iff p^2 divides n for
   some p. On the XOR product: mu(m o n) = mu(m) mu(n) for ALL squarefree
   m, n, coprime or not. On the ordinary product: gcd(m,n) = 1 implies
   mu(mn) = mu(m) mu(n); for squarefree m, n with gcd(m,n) > 1, mu(mn) = 0.
   Off the squarefree layer the character law fails (witness class m = 4,
   n = 2; the breaker documents it).

A4 LAMBDA IS THE TOTAL XOR CHARACTER. lambda(mn) = lambda(m) lambda(n) for all
   m, n (completely multiplicative); lambda = mu on squarefree n;
   mu = lambda . mu^2. lambda is the mod 2 reduction character of the free
   abelian monoid (N, .) = directsum over p of (Z>=0, +).

A5 EXACT INVERSE. sum over d dividing n of mu(d) = [n = 1]  (1 * mu = delta_1).

A6 XOR DECOMPOSITIONS. The number of ordered pairs (a, b) with a b = n and
   gcd(a, b) = 1 equals 2^omega(n). (Dirichlet series zeta(s)^2 / zeta(2s);
   dividing by zeta(2s) removes the AND channel.)

A7 EULER-TRUNCATION DICTIONARY (exact, finite). With x_p = p^(-t):
   (i)   sum over subsets Q of {primes <= 31} of prod_(p in Q) (-x_p)
         = prod_(p <= 31) (1 - x_p),   for t in {1, 2, 3, 4};
   (ii)  the same sum with +x_p equals prod (1 + x_p);
   (iii) prod (1 + x_p) = prod (1 - x_p^2) / prod (1 - x_p);
   (iv)  capped lambda block, primes p <= 13, exponents k_p in {0,1,2,3}:
         sum over exponent tuples of prod (-x_p)^(k_p)
         = prod_(p <= 13) sum_(k=0..3) (-x_p)^k,   for t in {2, 4};
         and per prime, sum_(k=0..3) (-x)^k = (1 - x^4)/(1 + x),
         sum_(k=0..3) x^k = (1 - x^4)/(1 - x).

A8 COSINE ANCHOR. Inner product <f, g> = sum f(n) g(n) n^(-2 sigma), t = 2 sigma.
   G1 = squarefree ambient, vectors 1 and mu, truncated to subsets of
   primes <= 31. G2 = all-n ambient, vectors 1 and lambda, truncated to
   primes <= 13 with exponents capped at 3.
   (i)   Norms are equal: ||mu||^2 = ||1||^2 in G1 and ||lambda||^2 = ||1||^2
         in G2 exactly, so cos = <1, .> / ||1||^2 with no square root.
   (ii)  Both truncated cosines reduce exactly to the SAME per-prime factor:
         cos = prod over the leg's prime set of (1 - x_p)/(1 + x_p)
         = [prod (1 - x_p)]^2 / prod (1 - x_p^2);
         G1 at t in {1, 2, 3, 4}, G2 at t in {2, 4} (the cap K = 3 cancels
         exactly by A7(iv)).
   (iii) Boundary t = 1 (sigma = 1/2): cos_P(1/2) = prod_(p <= P) (p-1)/(p+1),
         strictly decreasing as P runs through the primes up to 500. Classical
         import (Mertens): the limit is 0. The growth vector and the XOR
         character become orthogonal exactly at the critical boundary,
         unconditionally.
   (iv)  sigma = 1 witness: with the Euler values zeta(2) = pi^2/6 and
         zeta(4) = pi^4/90 as rational coefficients, the limit cosine is
         (1/90)/(1/6)^2 = 2/5 exactly; and the truncation
         prod_(p <= 500) (p^2 - 1)/(p^2 + 1) is strictly decreasing and stays
         > 2/5 at every prime step.
   Limit statements (P to infinity, sigma > 1/2: cos theta(sigma)
   = zeta(4 sigma)/zeta(2 sigma)^2; boundary asymptotic
   cos theta = (pi^2/6)(2 sigma - 1)^2 (1 + o(1))) are classical-import
   corollaries (absolute convergence of Euler products for Re s > 1, Laurent
   expansion of zeta at s = 1, Mertens third theorem), cited, not asserted by
   computation.

## Field 2. CODE

verify_prime_boole_1.py. Python standard library only (fractions, math,
itertools, sys). Exact arithmetic; no float in any assertion; decimal readouts
are labeled readouts computed by integer scaling and are not assertions.
Environment: LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC.
Runtime target under 120 s per leg, hard stop 300 s. Static compilation checks
are allowed before the pin; no formal gate runs before the freeze.
Two legs: leg A this cloud container (Linux, CPython 3.x), leg B one fleet
device (Linux, different CPU architecture, CPython 3.x); byte-identical stdout
across the two legs is required for the computation grade candidate-C. If leg
B is unreachable the run is single-leg and says so plainly.

## Field 3. CARRIER OR DATA

None. Self-generated integer ranges only. Frozen bounds: A1 squarefree pairs
m <= n <= 600; A2 a, b in [0, 512]; A3 mu two-path agreement and parity on
[1, 20000], XOR-character pairs on squarefree m <= n <= 300; A4 complete
multiplicativity on m <= n <= 300, layer agreements on [1, 20000];
A5 n <= 20000; A6 n <= 5000; A7 and A8 exactly as displayed in Field 1.

## Field 4. SYSTEMATICS

Finite truncation everywhere; every exact assertion is an identity instance at
the frozen ranges, so there is no threshold to tune. The witness 2/5 is
specific to the frozen geometries G1 and G2: changing the ambient (for example
the vector mu inside the all-n ambient) changes the cosine value, which the
breaker documents as a scope note; the boundary vanishing at sigma = 1/2 does
not depend on that choice. Classical imports are named in Field 1 and are not
recomputed.

## Field 5. FAILURE THRESHOLD

Zero tolerance. Any single exact assertion failing at any frozen instance
fires the falsifier of the corresponding claim and the transcript records
FALSIFIED. A fired falsifier is a first-class outcome: archived, not deleted;
no bound moves after the fact.

## Field 6. ACTION LAYER

L1. Any physical reading or any lift to another layer needs its own named gate
and is not part of this candidate.

## FALSIFIER (explicit)

A concrete instance violating any of A1..A8 at the frozen ranges: a squarefree
pair breaking a support map or the XOR-character law, an integer pair breaking
the carry splitter, an n breaking the mu/lambda/delta_1/2^omega identities, a
subset or exponent tuple breaking an Euler-truncation identity, a prime step
breaking monotonicity or the > 2/5 floor, or the rational identity
(1/90)/(1/6)^2 = 2/5 failing. For the candidate-T proofs attached in the
candidate document: an identified gap on review.
