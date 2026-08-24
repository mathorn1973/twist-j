# C-SPLIT-UNIT-1: the split unit (rev 2)

NON-CANONICAL candidate in the TWIST-J incubation lane. No authority. No
Canon change. One named session owns this candidate (Claude cloud session,
2026-08-01). Target on promotion: the public line mathorn1973/twist-j.
Basis: Public Canon v30 (tag canon-v30, content commit 857223fc..24ee0,
verified ACTIVE, hashes 5 of 5 OK). Rev 2 incorporates an accepted external
audit; see the revision history at the end and
AUDIT-C-SPLIT-UNIT-1_2026-08-01.md.

## 0. The owner's sentence

The whole is multiplicatively 1, additively 0, and internally carries a
nontrivial binary distinction.

This candidate freezes what in that sentence is theorem, what is dictionary,
and what is hypothesis, and it sharpens the sentence to its complete form.

Status split, declared up front:

```text
[candidate-T]   the algebraic block T1..T8 below, verified two-platform
                byte-identical (RESULT-C-SPLIT-UNIT-1_2026-08-01.md),
                with the scopes stated per item
[T, literature] Kronecker; Dirichlet; Kummer / Washington Thm 4.12,
                Cor 4.13; class number formula L(1, chi5) = 2 ln phi/sqrt 5
[D]             the ontological reading (section 5), the class premise of
                T4, the scale reading of T7, the unification of T8
[H]             the completeness claim (section 6), with its falsifier
```

## 1. The deflation, stated first

Honesty before elegance. Two facts that look J-specific are not:

```text
D1  sum_a log|sigma_a(u)| = 0 for EVERY unit u. Product formula. One line.
D2  log-size vector proportional to chi5 for EVERY unit of Z[zeta_5].
    Proof: complex conjugation gives |sigma_a(u)| = |sigma_(-a)(u)|, so the
    sizes are (t, s, s, t); |N(u)| = t^2 s^2 = 1 gives s = 1/t. Two lines.
    No unit theorem is needed for the line, only for its quantization.
```

So "navenek nula" at the size level is a property of the FIELD carried by
every unit. The owner's section 1, quoted alone, selects the field, not J.
What selects J, and under which premise, is T4 below.

## 2. The theorem block

Everything here is exact and pinned; proofs are short and written here; the
verifier is the witness, the breaker the second path, the external audit the
third reading.

**T1 (size character).** For all a in G = (Z/5Z)^x,

```text
|sigma_a(J)|^2 = phi^(-2 chi5(a))    exactly in Z[phi],
```

so the logarithmic image is log|sigma_a(J)| = -(ln phi) chi5(a). With
N(J) = 1 and Tr(J) = 3 this is the character form of the registered J-UNIT
[T] moduli (phi^-1, phi, phi, phi^-1). Proof: J = zeta phi^-1 (equivalent
to the Canon anchor J phi = j), |sigma_a(zeta)| = 1, sigma_a(phi) = phi for
a in {1,4} and -phi^-1 for a in {2,3}.

Purity lives at the logarithmic level and only there. The raw modulus
vector decomposes with a nonzero trivial part:

```text
(|sigma_a(J)|)_a = (sqrt5/2) . 1 - (1/2) . chi5,
```

trivial component sqrt5/2 (half the Gauss sum), chi5 component -1/2. Both
lines are one-step arithmetic over the frozen gates (C1..C4, D1, D2); no
new formal gate is claimed.

**T2 (quantization).** U(Z[zeta_5]) = mu_10 x <phi> [T, literature: Kummer;
Washington Thm 4.12, Cor 4.13; real subfield Q(sqrt 5), fundamental unit
phi]. Hence the size lattice of the whole unit group is

```text
{ log-size vectors } = Z . (ln phi) . chi5,
```

a rank-1 lattice on the chi5 line. Finite-range witness: all 78 units in
the [-4,4]^4 coefficient box lie on it (gate H1), and all 58 units in
[-2,2]^4 are literally +-zeta^k phi^m (gate K4).

**T3 (minimal quantum).** J = zeta phi^-1 carries m = -1: one negative
quantum of the unique bit, |m| = 1 minimal among non-torsion units. Across
the Galois orbit of J the size data are exactly {phi^-2 twice, phi^2 twice}
(gate K5): the sign of the quantum is Galois labeling, the magnitude 1 is
not. The minimal-quantum units form the torsor mu_10 . phi^{+-1}, twenty
elements; J does not sit there alone. What singles J out inside that torsor
is T4.

**T4 (the forced orbit, exact scope).** Theorem [candidate-T]: within the
class {1 + w : w in mu_10}, the units are exactly the four Galois
conjugates of J, one orbit. Enumeration: norms 16 (w = 1), 0 (w = -1),
1 (w = zeta^k), 5 (w = -zeta^k); second path by Sylvester resultants. By
Kronecker's theorem, "w in mu_10" is exactly "w a pure phase in every
archimedean reading".

What the field does not force: the class itself. Even exceptionality does
not select the orbit, because phi is itself an exceptional unit (1 - phi =
-phi^-1, both units). The selecting property is additive: u - 1 is pure
phase. Hence the honest grading:

```text
[candidate-T]  within the class 1 + mu_10, J is the unique Galois orbit of
               units, and it realizes the minimal quantum ln phi.
[D]            "being = identity plus a sizeless distinction", the premise
               that selects the class. "The field forces its first word"
               holds only relative to that premise.
```

**T5 (bit uniqueness, the kernel, and the p = 5 census).**

```text
(i)   G ~ C_4 has exactly one subgroup of index 2, {1,4}; exactly one real
      nontrivial character, chi5. The bit is unique.
(ii)  Conjugation and the bit, stated precisely. c = sigma_(-1) = sigma_4
      generates <c> = {1,4} = squares = ker chi5, and chi5(c) = +1. So the
      bit is NOT the conjugation involution: conjugation generates the
      KERNEL of the bit, and the bit is the unique nontrivial character of
      the quotient G/<c> ~ C_2. The p = 5 coincidence is subgroup-level:
      {1,4} is at once the squares, <conjugation>, and
      Gal(Q(zeta_5)/Q(sqrt 5)), since squares = {+-1} iff (p-1)/2 = 2 iff
      p = 5. Under translation by c the regular representation splits into
      the even block 1 + chi5 and the odd doublet; the phase pair is
      c-odd, and c-oddness alone forces its trivial and chi5 components to
      vanish. The c-grading algebra e+- = (1 +- c)/2 is gate I3; the bit
      is the quotient character, not c.
(iii) Sector census: the dual of G splits as {trivial, chi5, one conjugate
      doublet}. Among primes, exactly one doublet iff p = 5 (count
      (p-3)/2); at p = 3 the doublet count is zero. So p = 5 is the
      smallest prime whose Galois symmetry carries exactly one bit AND
      exactly one phase pair, and the 4-dimensional algebra splits
      4 = 1 + 1 + 2. This is character arithmetic [candidate-T]. It is
      NOT registered as a physical selection of p = 5, and this candidate
      registers no such reading; Canon section 16 is untouched.
(iv)  Two more faces of the same partition, already public: the unit-size
      character (T1), and the dilogarithm face of the registered Li_2 row
      after centering:
        (Re Li_2(sigma_a(J)))_a = (pi^2/20) . 1 - (pi^2/25) . chi5,
      trivial component pi^2/20 (the registered orbit sum pi^2/5 over 4),
      centered part pure chi5. The partition {1,4} | {2,3} is the same in
      all faces because C_4 admits only one.
```

**T6 (two sectors, no mixing, logarithmic reading).** Decompose the Galois
data of J in the regular representation of G:

```text
log-modulus datum  log|sigma_a(J)| = -(ln phi) chi5(a):
                   trivial component 0 (that is N(J) = 1, product
                   formula), pure chi5 sector, c-even.
argument datum     Arg sigma_a(J) = pi r_a, r = (2, -1, 1, -2)/5
                   principal: c-odd, hence trivial and chi5 components 0,
                   pure doublet sector; exactly r_a = Re[(2+i) chi(a)]/5
                   with chi(2) = i. Note |2 + i|^2 = 5, the Gaussian prime
                   above 5 of the registered Z2-PLACES-SPLIT [T].
```

The two archimedean projections of J (modulus and argument, the two force
channels of AXIOM-PROJECTION-DICTIONARY [D]) live, in this logarithmic and
principal-argument reading, in the two distinct nontrivial real sectors

```text
R[G] = 1 (+) chi5 (+) <Re chi, Im chi>,
```

with zero mixing and zero trivial part, and at p = 5 the sector list is
complete: there is no third nontrivial sector.

**T7 (the bit and the scale).** Gauss sum:

```text
sum_a chi5(a) zeta^a = 2 phi - 1,   (2 phi - 1)^2 = 5,
```

already registered publicly inside ALPHA-PREFACTOR-UNIFICATION [T] as
tau = 2 phi - 1 = sqrt 5. With the class number formula [T, literature]
L(1, chi5) = 2 ln phi / sqrt 5:

```text
ln phi = (sqrt 5 / 2) L(1, chi5).
```

The identity is classical [T, literature]. The reading "the bit generates
the scale" is [D]: the scale here is dimensionless arithmetic only, chi5 ->
sqrt 5 -> phi -> ln phi -> the size spectrum -> the kernel partition of
chi5. No metrological content; METRO-EDGE-SCALE [O] is untouched. The
entropy row 2 ln phi of the internal line reading as sqrt 5 L(1, chi5) is
likewise [D].

**T8 (three zeros: three theorems, one pattern).** Individually [T]:

```text
sum_a chi5(a) = 0                  trivial projection of a nontrivial
                                   character, C_4 module
sum_a log|sigma_a(u)| = 0          the same trivial projection in the same
                                   C_4 module (log|N(u)| = 0, augmentation)
Tr [P, Q] = 0                      trace cyclicity; equivalently
                                   End(V) = k I (+) sl(V) with commutators
                                   in sl(V); a DIFFERENT module
```

The first two are literally one statement in one module. The third is not:
no canonical morphism carries the C_4 datum to End(V). The unification
"navenek nula = zero scalar projection of a nontrivial object" is a [D]
reading pattern, useful prose, no theorem weight across the pair. "Celek
jedna" = the multiplicative trivial component, the norm, equals 1.

## 3. The completed sentence

The owner's sentence undercounts the interior and, in rev 1, overcounted
purity. The corrected complete form:

```text
The whole is multiplicatively 1 and, in the logarithmic reading,
additively 0. The logarithmic image carries exactly one bit and the
principal argument carries exactly one phase pair. The quantum of the bit
is ln phi, the special value of the bit's own L-function. Within the class
identity-plus-pure-phase, J is the unique Galois orbit of units and
realizes the minimal quantum of the bit.
```

## 4. Where the chain breaks, honestly

```text
1 -> bit          the bit is unique [candidate-T]; the carrier is unique
                  within the declared class 1 + mu_10 [candidate-T]; the
                  class itself is the ontological premise [D].
bit -> scale      the arithmetic identities are [candidate-T] and
                  [T, literature]; "generates the scale" is [D],
                  dimensionless only.
bit -> time       axiom, not derivation: time = counting powers of M_J is
                  A0's declared architecture. T4 forces WHICH unit up to
                  Galois relabeling GIVEN the class premise; the residual
                  axiom content is that premise plus "update = multiply".
                  Note also that "a sequence of resolutions" presupposes
                  an order: the counter is primitive in A0, not derived.
time -> space     OPEN [O]: space is read through commutators (CORE), the
                  fired kernel is spatially abelian (FIRED-COMMUTATOR-NOGO
                  [T]), the canonical curvature operator is open
                  (CURVATURE-OPERATOR-CANONICAL [O]). In the language of
                  this candidate the fired piston layer is the [P,Q] = 0
                  regime: bits and time, not yet space. The owner's own
                  grammar predicts exactly the brake the Canon keeps.
bit -> driver     OPEN: A0 states that checkpoint, five generators,
                  selector, decoder are not claimed to be uniquely forced
                  by J. Identifying the TM drive bit with chi5 is [H], and
                  MINIMAL-READ-DERIVATION [O] and QUADRATIC-DECODER-DATA
                  [O] stand between.
```

## 5. The ontological reading [D, NON-CANONICAL]

Reality is a closed unit. Its global invariant is 1, hence its total
logarithmic charge is 0. Inside, the unit resolves into character sectors:
one bit (index two, the smallest resolution of identity, epsilon^2 = 1 in
the quotient) and one oriented phase pair. Information does not begin with
existence; it begins with distinction inside existence (log2 1 = 0,
log2 2 = 1). Time is the order of resolutions (the counter, primitive).
Space, if the dictionary holds, is their noncommutativity (the
commutator), and observables are invariants of the action. "Navenek nula"
means: zero external distinguishability (A0) and zero total logarithmic
charge (T1). It does NOT mean E_total = 0; the public FRW row explicitly
makes no such claim, and neither does this candidate.

A symmetry-and-invariants reading alone underdetermines physics: the
quadruple (A, G, U, mu) is the minimal datum (algebra, symmetry, update,
measure). The open rows named in section 4 are exactly the U and mu gaps.

## 6. The completeness claim [H], with its falsifier

```text
H-SPLIT-UNIT-COMPLETE: the specific resolution, bit, update, and decoder
of the public architecture are forced by J, not merely admissible.

Falsifier: exhibit at the same layer two inequivalent structures (a second
binary cut inequivalent to chi5 actually used by a registered reading, or
two inequivalent updates or decoders surviving every registered gate), or
a required choice provably external to <J> and Galois. A closure of
CURVATURE-OPERATOR-CANONICAL as NONUNIQUE or EMPTY, or of
MINIMAL-READ-DERIVATION negatively, fires the corresponding limb.
```

This H is live and is NOT strengthened by the T block above; the T block
only shrinks what remains to be forced (the bit is not free, and the
carrier is not free within the class; the class premise, the update
reading, and the decoder still are).

## 7. Dependency edges

```text
Canon v30 rows     J-UNIT [T]; J-PROJECTIONS [T]; PLENUM-POINT [T];
                   AXIOM-PROJECTION-DICTIONARY [D]; Z2-PLACES-SPLIT [T];
                   ALPHA-PREFACTOR-UNIFICATION [T] (tau = sqrt 5);
                   the Li_2 real-part rows; A0 and its disclaimer;
                   FIRED-COMMUTATOR-NOGO [T]; CARRY-PENTAD [T] (the
                   I + C^a family with charpoly Phi_5(X - 1));
                   CURVATURE-OPERATOR-CANONICAL [O];
                   MINIMAL-READ-DERIVATION [O]; QUADRATIC-DECODER-DATA [O].
Classical          Kronecker 1857; Dirichlet unit theorem; Kummer /
                   Washington Thm 4.12, Cor 4.13; Gauss sums; class number
                   formula for Q(sqrt 5).
Project witnesses  claude/verify_bit_note_1.py (regulator G-series,
                   Reg = 2 ln phi against the class number formula);
                   claude/PROMO-C-C8-BILINEAR-SHADOW-1.md (the distinct
                   Galois gauge bit of the shadow lane; different object,
                   do not conflate).
```

## 8. Verification record

See RESULT-C-SPLIT-UNIT-1_2026-08-01.md: prereg and both scripts frozen by
SHA-256 before first run; 38 + 8 gates, all PASS, exit 0, stdout
byte-identical on x86_64 and aarch64; no falsifier fired; no threshold
moved. Where labels in that record differ from rev 2, the audit record
AUDIT-C-SPLIT-UNIT-1_2026-08-01.md supersedes the prose; the pins and
gates themselves are unchanged.

## 9. Promotion sketch (not packaged, owner's call)

If wanted publicly, the natural cut is two small rows plus one note:

```text
J-ONE-PLUS-TORSION-UNIQUE   T   within {1 + w : w in mu_10} the units are
                                exactly one Galois orbit, the orbit of J,
                                at minimal quantum ln phi (T3, T4);
                                falsifier: a fifth such unit or a failed
                                orbit member
GALOIS-BIT-SECTORS          T   unique index-2 quotient; <c> = ker chi5
                                with chi5(c) = +1; census 1 + 1 + 2 at
                                p = 5; LOG-modulus on the chi5 line,
                                principal argument in the doublet plane
                                with the exact r table; raw modulus and
                                centered Li_2 decompositions (T1, T5, T6);
                                falsifier: enumeration counterexample or a
                                nonzero forbidden component
notes/ essay                    the completed sentence and the zero
                                pattern (T8), NON-CANONICAL
```

A PROMO-C-SPLIT-UNIT-1 package would follow the RG-FIXEDPOINT template.
Still not written: the working agreement wants the cross-family breaker
recorded before promotion; the external audit of rev 2 may already satisfy
it if the owner confirms the auditing seat's family.

## Revision history (disclosure)

```text
rev 1  2026-08-01. Initial candidate. Pins in
       RESULT-C-SPLIT-UNIT-1_2026-08-01.md.
rev 2  2026-08-01, same day, after an accepted external audit (relayed by
       the owner; AUDIT-C-SPLIT-UNIT-1_2026-08-01.md). Four prose-layer
       corrections: (1) conjugation generates ker chi5 and is not the
       bit; (2) purity restricted to log-modulus and centered vectors,
       raw modulus decomposition (sqrt5/2) 1 - (1/2) chi5 recorded;
       (3) T4 scoped to the class 1 + mu_10, "first word" gloss demoted
       to [D], the twenty-element minimal torsor recorded, the phi
       exceptional-unit counterpoint added; (4) the three-zeros
       unification demoted to a [D] pattern, instances staying T. The
       completed sentence rewritten in the logarithmic reading. No frozen
       gate, pin, or stdout changed; no falsifier fired; the 46 gates
       stand as run.
```
