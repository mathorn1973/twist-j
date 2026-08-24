# C-PRIME-BOOLE-1. The Boolean skeleton of the primes and its zeta dictionary

```
CANDIDATE   C-PRIME-BOOLE-1, 2026-08-10. One named session. No authority.
TARGET      public mathorn1973/twist-j on promotion (notes/ or probe; owner decides).
GATE        public head at freeze: Public Canon v39, STATE ACTIVE, tag canon-v39,
            content commit ab17b104 (ancestor of main), canon/SHA256SUMS 5/5 OK,
            CANON.md sha256 698df221..., 187370 B. Internal line not reachable from
            this session and not used: this candidate builds on classical
            mathematics and public rows only.
LAYER       L1 (state). No lift claimed. No RH claim. No J-coupling claimed.
COLLISION   registry and probes/ scanned: no row or probe on this scope.
ORIGIN      owner message 2026-08-10 correcting the eta thread: the global XOR
            object inside zeta is mu, not eta. This document sharpens and pins it.
```

## 1. The correction, sharpened (candidate-T)

The public row FERMIONIZER [T] carries the LOCAL alternator of the place 2:
Phi_f(s) = 1 - 2^(1-s), the factor that turns zeta into eta. The owner's
correction stands: the GLOBAL alternator of the whole prime factorization is
not eta's factor. It is the parity character of the occupancy vector. Two
forms, and the distinction matters:

$$
\lambda(n) = (-1)^{\Omega(n)}, \qquad \mu(n) = \lambda(n)\,\mu(n)^2 .
$$

lambda is the total XOR character: the mod 2 reduction of the free abelian
monoid (N, .) = directsum_p (Z_{>=0}, +). It is completely multiplicative with
no exception. mu is lambda restricted to the Boolean layer (squarefree n) and
annihilated by AND overlap (mu = 0 as soon as some p^2 divides n). On the XOR
group law itself,

$$
m \circ n := \frac{mn}{\gcd(m,n)^2}, \qquad \mu(m \circ n) = \mu(m)\,\mu(n)
\quad \text{for ALL squarefree } m, n,
$$

coprime or not: mu is a genuine character of the group (squarefree, o) =
directsum_p F_2. Off the squarefree layer the law fails, and it fails exactly
where it should: witness (m, n) = (2, 4), z = 2, mu(z) = -1 against
mu(2) mu(4) = 0. The breaker's census on [1,60]^2 found 463 failures, every
single one involving a non-squarefree input. The boundary of the claim is the
claim.

So: eta is the place-2 local alternator; lambda is the global one; mu is the
global one wearing the Pauli constraint. That is the corrected sentence.

## 2. Frozen claims and their results

Preregistration frozen BEFORE any computation, then one verifier run per leg.

```
A1  support maps          S(gcd) = AND, S(lcm) = OR, S(mn/gcd^2) = XOR,
                          mn = XOR-part . AND-part^2          candidate-T + C
A2  carry splitter        a + b = (a XOR b) + 2 (a AND b); per prime bit:
                          XOR = multiplication without overlap, AND = the
                          square's birth (public floor: RAMIFIED-TM-LIFT)
                                                              candidate-T + C
A3  mu                    = (-1)^(XOR of bits) on squarefree, 0 on AND hit;
                          XOR-product character; ordinary-product law
                                                              candidate-T + C
A4  lambda                completely multiplicative total XOR character;
                          mu = lambda . mu^2                  candidate-T + C
A5  exact inverse         1 * mu = delta_1                    candidate-T + C
A6  XOR decompositions    #{(a,b) ordered, ab = n, gcd(a,b) = 1} = 2^omega(n)
                                                              candidate-T + C
A7  Euler truncations     subset sums = products, capped lambda blocks,
                          all exact Fractions                 candidate-C
A8  cosine anchor         see section 4                       candidate-T + C
```

Proof sketches (elementary, attached for review): A1 is v_p(gcd) = min,
v_p(lcm) = max, and on bits min = AND, max = OR, a + b - 2 min = XOR. A2 is
the binary full adder, per prime exponent. A3: (-1)^|S xor T| =
(-1)^(|S| + |T| - 2|S cap T|) = (-1)^|S| (-1)^|T|; annihilation is e >= 2.
A4: Omega(mn) = Omega(m) + Omega(n). A5: sum_k (-1)^k C(omega, k) = 0 for
omega >= 1. A6: each prime block goes wholly left or wholly right. A7: unique
factorization plus distributivity, verified as exact identities. A8: section 4.

## 3. The dictionary (candidate-T; each line is one Euler product)

```
growth (all occupancies)          zeta(s)
AND channel (the squares)         zeta(2s)
XOR selector, unsigned            zeta(s)/zeta(2s)     sum over squarefree n^-s
XOR character, Pauli (mu)         1/zeta(s)            sum mu(n) n^-s
XOR character, total (lambda)     zeta(2s)/zeta(s)     sum lambda(n) n^-s
XOR decomposition count           zeta(s)^2/zeta(2s)   sum 2^omega(n) n^-s
carry removal                     divide by zeta(2s)
```

In binary addition AND makes the carry. In prime multiplication AND makes the
square, the square lives in zeta(2s), and every carry-free (coprime) structure
is a division by zeta(2s). The owner's boxed sentences are exact.

## 4. The cosine anchor (the new pin)

Weighted geometry <f, g> = sum f(n) g(n) n^(-2 sigma): the prime axes are
independent, the axis of p has length log p, exactly the space the owner
proposed. Two frozen geometries: G1 (squarefree ambient, vectors 1 and mu) and
G2 (all-n ambient, vectors 1 and lambda). In both, norms of the two vectors
are equal, and the angle between growth and the XOR character is

$$
\cos\theta(\sigma) = \frac{\zeta(4\sigma)}{\zeta(2\sigma)^2},
\qquad \sigma > \tfrac{1}{2},
$$

the same formula in both geometries; per prime the factor is
(1 - p^(-2 sigma))/(1 + p^(-2 sigma)). Three exact facts hang on it:

1. Boundary orthogonality, unconditional (candidate-T; imports Mertens):
   as sigma -> 1/2+ the cosine goes to 0 at rate

$$
\cos\theta(\sigma) = \frac{\pi^2}{6}\,(2\sigma - 1)^2\,(1 + o(1)).
$$

   The mechanism is the pole of zeta at s = 1: the growth singularity is what
   forces the XOR character orthogonal exactly at the critical boundary. The
   truncated form at sigma = 1/2 is prod_(p <= P) (p-1)/(p+1), verified
   strictly decreasing through p <= 500 (readout 0.013205 at P = 500).

2. Rational witness (candidate-T): at sigma = 1,

$$
\cos\theta(1) = \frac{\zeta(4)}{\zeta(2)^2} = \frac{36}{90} = \frac{2}{5},
$$

   exactly. Truncation prod_(p <= 500) (p^2-1)/(p^2+1) decreasing with floor
   > 2/5 (readout 0.400218). Remark, not a claim: 2/5 = 2/p at p = 5.

3. Scope honesty (breaker, exact): the value 2/5 is geometry-specific. Moving
   mu into the all-n ambient shifts cos^2 by exactly prod 1/(1 + p^(-4)),
   computed and pinned. The boundary vanishing does NOT depend on the ambient
   (the growth norm diverges at the boundary in every version).

WHAT THIS IS NOT. The boundary orthogonality is unconditional and says nothing
about the location of zeta zeros. RH lives one floor higher, in completeness,
not in one inner product. The classical hard forms of the owner's sentence
(literature imports, none claimed here): RH iff M(x) = O(x^(1/2 + eps)); RH
iff sum mu(n) n^(-s) converges for every sigma > 1/2 (the XOR series reaches
the critical line); the Nyman-Beurling criterion with the Baez-Duarte
strengthening to integer dilations (arXiv math/0202141); Weil positivity; the
Connes school scaling reading. The honest open question this lane feeds: state
the Baez-Duarte completeness in Boolean coordinates (candidate follow-up
C-PRIME-BOOLE-2, unopened).

## 5. Prior art (priority honesty)

The skeleton is established mathematics and the candidate claims framing, not
priority. Known: the divisor lattice of a squarefree number is the Boolean
lattice (textbook); the statistical-mechanics reading of zeta as the partition
function of the free Riemann gas over primes (Julia 1990, the primon gas);
mu(n) = (-1)^F with squarefree = Pauli exclusion and 1/zeta as the
supersymmetric partition function (Spector 1990, Comm. Math. Phys.); the
Bost-Connes C*-dynamical system (1995). AND creating the square IS double
occupancy being forbidden for fermions; the program's Pauli lane
(C-PAULI-CAR-FORCING-N, P-PAULI-CARRIER-CAR-1) speaks the same language from
the J side. What we did not find stated in this exact form is the cosine
normalization of section 4; treat it as folklore-adjacent until a source
appears. Bibliographic ids get pinned at fold time.

## 6. Pins

```
PREREG   PREREG-C-PRIME-BOOLE-1.md
         sha256 eb859b1c0079d133afa6808a6198e55c34542aed69d095249b9b871642b45612
         8051 B, frozen 2026-08-10T09:57:23Z, before any computation
VERIFIER verify_prime_boole_1.py
         sha256 5f7af8ea8e267f12c69dc0d37108d181a9c6421d46e1a5d40ffeb6f569b598ee
         10462 B, pinned 2026-08-10T09:59:32Z, stdlib only, exact, no float in
         any assertion, env LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1
         PYTHONHASHSEED=0 TZ=UTC
LEG A    Linux x86_64, CPython 3.11.15 (cloud container), exit 0, 1.03 s
LEG B    Linux aarch64, CPython 3.13.5 (fleet device), exit 0
STDOUT   sha256 3c1be837b03b6463cfe22361a3420fff902a4b51e624eb2c771e6cbf52ac000b
         2920 B, 39/39 PASS, empty stderr, BYTE-IDENTICAL across the two
         architectures (incubation grade; a public probe re-pins fresh)
BREAKER  break_prime_boole_1.py
         sha256 7929248e13c0aa7022a37c5bac25d527038a6ef4a86cf08301d9f4287c274575
         stdout sha256 40386940e3ebfd849ffed56c8b0ab37c6d7ca5c800fcf96884989fc7bf0c93a0
         7/7, independent code paths (trial division, fresh window [601,900],
         off-layer census, exact ambient-shift factor, out-of-freeze t = 5, 6):
         no counterexample; failures land exactly on the claimed boundary
```

## 7. Relation to the public rows (gated at v39)

```
FERMIONIZER [T]            the local place-2 alternator; this candidate names the
                           global object it is the local shadow of.
RAMIFIED-TM-LIFT [T]       already carries the carry identity a+b = XOR + 2 AND
                           with 2 the unique universal coefficient; A2 cites it
                           as the public floor.
PENTAGON-NORMALIZATION [T] normalization identity only, no RH content; confirmed
                           in the row text. Untouched.
LAMBDA-COCYCLE-ANGLES [H]  the cocycle vector exists iff RH AND every Cayley
 + GRID-EQUIVALENCE [T]    angle lies on the 5-adic grid 2 pi (1/4) Z[1/5]. That
 + BRANCH-COLLAPSE [T]     conjunction is strictly stronger than RH. This
                           candidate deliberately decouples: the Boolean
                           skeleton is universal over ALL primes and J-free by
                           construction. J re-entry (a metric or cocycle on this
                           space) needs its own named gate.
J-LI-* nogo family [T]     the carrier hunt has killed Haar-Koopman, E8-shell,
                           Hilbert-Schmidt and shift routes; consistent with
                           moving the search to the Boolean substrate first.
PENTAGON-ONLY-DILATIONS    unfolded incubation PROMO in this project: NB clock
 (project lane, no fold)   functions have Gram gcd(m,n)^2/(12 m n), an AND
                           coupling, and the pure 5-tower misses every
                           cross-prime direction by an exact constant. The same
                           decoupling lesson from the NB side.
```

## 8. Landing options (the fold consumes, the owner decides)

```
(a) notes/ NON-CANONICAL note on the public line: cheap, immediate, no
    registry row; anchors the language.
(b) public probe P-PRIME-BOOLE-1: fresh PREREG.md + verify.py under probes/,
    two-architecture check at PR time, registry claim PRIME-BOOLE [T] with
    scope = sections 1-4 (limit corollaries as named classical imports) and
    the prereg falsifier verbatim.
(c) stay incubated. Speaks against it: open decision 3 already lists five
    unfolded lanes; this one is cheap to fold and should move or die.
```

Recommendation of this session: (b), with (a) as the fallback if the owner
wants zero registry motion before a second independent read.

## 9. Dependency edges

Classical imports only: Euler products and values zeta(2) = pi^2/6,
zeta(4) = pi^4/90; Laurent expansion of zeta at s = 1; Mertens third theorem.
No internal-line dependency. No public row edited. Public rows cited as
context only.
