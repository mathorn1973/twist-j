# C-PRIME-ORDER-READING-1, definitional stage, 2026-08-11

```
CANDIDATE  C-PRIME-ORDER-READING-1. No authority. Incubation lane of the
           TWIST-J project. DEFINITIONAL STAGE: no preregistration is frozen,
           no verifier exists, no computation has been performed, no data
           opened. Owner ANO is required per decision block below before any
           prereg freeze.
SESSION    Claimed by one named session (Cowork dialog session of 2026-08-11,
           the session that wrote claude/NOTE-PRIMES-IN-J-DIALOG_2026-08-11.md).
           One session, one candidate.
TARGET     Public mathorn1973/twist-j on promotion.
GATE       Currency gate run 2026-08-11 against the live repository:
           STATE ACTIVE, Public Canon v44, AUTHORITY mathorn1973/twist-j main,
           tag canon-v44 = main HEAD 1417b533944e85106901079cc73ae7a0c3c42dc2,
           content commit 9da73b96613eb0d6f8d0ec17a5ada3ee6f511a4a, both
           ancestors of main; canon/CANON.md sha256
           c482aff6d0a01faab7fa8b92d2c485b39a8389f67ed99d79024a2878f35acd69,
           211566 bytes, equal to the STATUS declaration; canon/SHA256SUMS
           5 of 5 OK.
COLLISION  REGISTRY.tsv, canon/FRONTIER.md, probes/: no row, obligation or
           probe on prime enumeration order or on a plenum-to-primes map.
           Nearest rows, used as floors and context only:
           MOBIUS-TM-PRIME2-BRIDGE [T], TM-MULTIPLICATION-CARRY-DEFECT [T],
           SPLIT-PRIME-RAPIDITY-CLASS [T],
           SPLIT-PRIME-RAPIDITY-CONSTRUCTION-AGREEMENT [C],
           READ-REDUNDANCY-PRIME-SUPPORT [T], J-HARMONIC-SEAM [T],
           AXIOM-PROJECTION-DICTIONARY [D]. Project claude/: no prior
           candidate on this topic; the CLEANUP-RECORD lanes are disjoint.
ORIGIN     claude/NOTE-PRIMES-IN-J-DIALOG_2026-08-11.md, section 4, final [O]
           block. The six admissibility conditions of the external PUBLIC
           review are adopted, together with the two amendments recorded
           there (forcedness instead of bare existence; order semantics as
           the archimedean question).
```

## 0. Problem, one sentence

Does the ordered sequence of rational primes arise as a forced reading of the
J-plenum, or only as one compiled algorithm among many? Shorter: which machine
has the primes as its time.

## 1. Setting and notation

```
K = Q(zeta_5), O_K = Z[zeta_5], h_K = 1, O_K^x = mu_10 x <phi>.
F = Q(sqrt5), O_F = Z[phi], units +-phi^Z, N(phi) = -1, sqrt5 = 2 phi - 1.
J = 1 + zeta_5^2, N(J) = 1 (a unit, not a prime).
For a rational prime p split in F and a generator w of a prime ideal above p
(class number one), |w|_1 |w|_2 = p at the two real places; define t_w by
|w|_1 = sqrt(p) e^(t_w). Changing the generator by +-phi^j shifts t_w by
j log phi; conjugation negates it. The canonical object is the unordered
class R(p) = {t, -t} in (R/(log phi)Z)/{+-1}  (SPLIT-PRIME-RAPIDITY-CLASS [T]).
```

## 2. The map under definition

P_J : N -> (target fixed by ANO-4), n |-> the n-th prime the plenum calls.
The candidate must make "calls" exact. Admissibility, restating the six
review conditions as D1..D6:

```
D1 STRUCTURE   P_J is a term of the named structure S fixed by ANO-1, with no
               auxiliary constants, encodings, orderings or representative
               choices beyond those S names. The admitted logic frame for
               "term" is itself frozen at prereg time.
D2 NO ORACLE   S does not contain the set of primes, a primality primitive,
               or a predicate from which primality follows by naming alone.
               Deriving irreducibility from multiplication inside S is
               legitimate and expected.
D3 GAUGE       P_J is invariant under the gauge the program marks: Galois
               C_4, unit multiplication on generators, declared orientation
               and inversion. Element-level data enters only through gauge
               classes (equivalently through ideals).
D4 BIJECTION   P_J is a bijection onto the target prime set; each prime is
               called exactly once.
D5 TIME        The domain N is machine time (the counter). Three separate
               claims: EXIST (an admissible P_J exists), UNIQUE (it is
               unique), ORDER-MATCH (it is monotone for archimedean size,
               P_J(n) = p_n).
D6 READOUT     The same term emits Frob_{P_J(n)} in C_4 with the call,
               without re-reading the output.
```

## 3. Floors, what is already known

```
F1 [T-lit]     The set of primes in any positional base is not a regular
               language. No admissible P_J factors through a fixed
               finite-state window over a digit stream; the reading must
               consume unbounded state, and the counter is the only named
               unbounded object.
F2 [T-lit]     Ideal-level data is choice-free: a nonzero prime ideal
               determines p (the characteristic of its residue field) and f.
               Recovering the prime below a given prime object is not the
               problem. The problem is the stream: which prime objects the
               machine visits, in which machine time.
F3 [T, v44]    Element-level scale data is canonical only as the unordered
               class R(p) on the circle. The winding number (the integer
               part of the rapidity) is NOT canonical: it moves under phi
               multiplication of the generator. Any order built through
               generators needs a canonical section of the unit action;
               none is registered.
F4 [analysis]  The plenum architecture is computation-universal for every
               purpose relevant here. If ANO-1 admits free encodings, EXIST
               is trivial (a sieve compiles) and UNIQUE is false (many
               sieves compile). The entire content of the candidate lives in
               the strength of D1. This is the central design risk and the
               reason for the kill condition in section 6.
F5 [T-lit]     Any generating mechanism must carry multiplicative structure
               (the Euler product). Functional-equation-grade symmetry alone
               admits Davenport-Heilbronn type counterfeits.
```

## 4. PROP-1, one new arithmetic statement, found while writing this document

Status: candidate-T, proof sketch only, NOT verified, no computation run.
Enters no registry and no canon. First stage-A target after a prereg freeze.

```
CLAIM      The unordered rapidity class is injective on split primes, and no
           split class sits at a fixed point of the involution: for distinct
           rational primes p != q, both split in F, R(p) != R(q); and for
           every split p, R(p) avoids the classes of 0 and (log phi)/2.

SKETCH     Suppose two classes coincide exactly. Unwinding section 1, there
           is y in O_F, a product of two generators (y = w_p sigma(w_q) for
           the direct match, y = w_p w_q for the conjugate match, y = w_p
           alone for a fixed-point case) and an integer m with
                y^2 = +- phi^m N,
           where N = pq (respectively p). Write w = y^2 phi^(-m) / N. Then
           |w|_1 = |w|_2 and w = a + b sqrt5 in F forces a b = 0; the case
           a = 0 dies on norms, so w = +-1 and y^2 = +- phi^m N exactly.
           If m = 2j: (y phi^(-j))^2 = +- N, so +- N is a square in F. The
           rationals that are squares in Q(sqrt5) are exactly the rational
           squares and 5 times rational squares; N in {pq, p} with p, q
           distinct primes different from 5 is neither, and -N < 0 is not a
           square in a real field. If m = 2j + 1: taking norms,
           N(y^2) = N(y)^2 >= 0 while N(+- phi^(2j+1) N) = -N^2 < 0.
           All cases are impossible.

CONSEQUENCE  If PROP-1 survives verification: the v44 circle classes
           SEPARATE split primes completely. The canonical J-side data
           distinguishes every split prime individually; what it provably
           cannot do, by F3, is ORDER them. The entire order deficit of the
           J-language is exactly the winding number, that is, the unit
           ambiguity. P_J is precisely the problem of a canonical section of
           the unit action, or of a machine time that supplies the winding.

FALSIFIER  An exhibited pair of distinct split primes with a certified class
           collision, or a split prime certified at a fixed point. Exact
           integer arithmetic in Z[phi]; verifier design frozen at prereg.
```

## 5. Decision blocks for the owner

Answer ANO per block with the option letter. Each block is hashed from its
BEGIN line through its END line inclusive, LF endings; hashes in section 9.

```
ANO-1 BEGIN
STRUCTURE S. What "the named structure" means. Decides the fate of F4.
(a) ring-strict: two-sorted structure (the counter N; the ring O_K with +,
    x, J, the Galois action). No ideal-set primitive, no encodings. The
    strongest reading; EXIST is genuinely open and may be provably empty.
(b) architecture: option (a) plus the declared discrete architecture of the
    active canon (Omega = N_0 x F_5^6, five generators, selector), with P_J
    required to be a reading in the sense of the registered decoder calculus
    (METRO family). Ties the candidate to the decoder programme.
(c) ideal-canonical: option (a) plus the ideal monoid of O_K with norm
    counting admitted as the counter applied to residue classes. Under (c)
    enumeration of prime ideals by norm becomes admissible, EXIST is cheap,
    and all content moves to UNIQUE and ORDER-MATCH.
CONSEQUENCE  (a) hard existence, clean uniqueness; (b) decoder-coupled,
    slowest, most physical; (c) fast existence, uniqueness fight.
ANO-1 END

ANO-2 BEGIN
LAYER. (a) L5 stream for the candidate, with L1 floors for the arithmetic
statements (PROP-1 at L1). (b) L1 only, deferring the stream reading. Any
later lift to L6 (a measure over histories) needs its own named gate.
ANO-2 END

ANO-3 BEGIN
FORCEDNESS. What "forced reading" asserts.
(a) uniqueness form: the future row asserts EXIST and UNIQUE within D1..D6;
    falsifier: two admissible P_J differing at some n. Mirrors the
    architecture-universality falsifier pattern already used in the program.
(b) minimality form: P_J minimal in a named cost order. Requires naming a
    new order; collides with the no-new-free-input discipline; not
    recommended unless a canonical cost is already in canon.
(c) equivariance form: P_J the unique Galois- and unit-equivariant map with
    a named property X; X must be supplied by the owner.
ANO-3 END

ANO-4 BEGIN
TARGET AND ORDER SEMANTICS.
(a) target = rational primes; ORDER-MATCH = agreement with the archimedean
    size order, stated as its own separately falsifiable claim. The physics
    sits in ORDER-MATCH: order by size is itself the archimedean projection,
    so ORDER-MATCH asks whether J-time order and archimedean order coincide.
(b) target = nonzero prime ideals of O_K in norm order; ORDER becomes
    internal and trivial; all content moves to TIME (which ideals, when).
ANO-4 END
```

Recommendations, one line: ANO-1 (b), ANO-2 (a), ANO-3 (a), ANO-4 (a).
Recommendations are not decisions; every block is a real fork.

## 6. Kill condition for the definitional stage itself

This stage closes as F (ill posed) if for every ANO-1 option either the
admitted structure compiles a sieve (EXIST trivial and UNIQUE false), or
nothing satisfies D1..D6. STOP while the logic frame of D1 is unfixed.
A fired kill is archived as a first-class outcome, not deleted.

## 7. What this document does not do

No preregistration is frozen. No verifier exists. No computation was run;
PROP-1 is a pencil sketch. No registry, frontier or canon line moves. Public
probe machinery is untouched. The six POLICY preregistration fields are
written only after the owner ANO on blocks 1 to 4, in
PREREG-C-PRIME-ORDER-READING-1.md, and frozen before any compute.

## 8. Dependency edges

```
uses as floors, does not modify:
  SPLIT-PRIME-RAPIDITY-CLASS [T], SPLIT-PRIME-RAPIDITY-CONSTRUCTION-
  AGREEMENT [C], MOBIUS-TM-PRIME2-BRIDGE [T], TM-MULTIPLICATION-CARRY-
  DEFECT [T], J-HARMONIC-SEAM [T], AXIOM-PROJECTION-DICTIONARY [D]
kept-out interface, referenced only:
  PRIME-RAPIDITY-WEIL-BRIDGE (outside canon per FOLD-V44 record)
adjacent open rows, not touched:
  METRO-REDUCTION-CALCULUS [O], QUADRATIC-DECODER-DATA [O]
```

## 9. Block hashes

```
ANO-1  sha256 165ba2c67a216d24d933727edb4a054eb9dcb733105ad0f2f6779e7eed0b7bef
ANO-2  sha256 e6513dd7374a097f03c676004c4c571ef73f990a4106a9be71a8ef2aa8e19a90
ANO-3  sha256 fec11408ff9532ba80f6f1ab698dec6f8b7cca01eaf583135b9cb99a3e8dfa19
ANO-4  sha256 0915e117c7678cc94660fffc20c7a010eaa7c8cfa67465d412ca92ae6ea923f8
```
