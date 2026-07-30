# The metal trace: one integer between writing and reading

Date: 2026-07-19. Anchor: Public Canon v10, tag `canon-v10`. Companion to
`notes/ARCHITECTURE_MAP_2026-07-18.md`.

**NON-NORMATIVE SYNTHESIS.** Exploration, no authority. The algebraic
layer below is exact and twice witnessed; every physical reading is
explicitly hypothesis-grade. No Canon claim, status, scope, or evidence
record moves here. Registration, if wanted, follows the preregistration
procedure in POLICY.md.

CZ: Psani je petkove, cteni je dvojkove, a cely rozdil je jedno cele
cislo: stopa t v kovove rovnici x^2 = t x + 1. Zlato ma t = 1, stribro
t = 2. Diskriminant t^2 + 4 dava 5 a 8, tedy prave ta dve rozvetvena
prvocisla programu; stopa 1 sklada (Fibonacci, beh), stopa 2 kopiruje
(Pell, zaznam); atom zapisu je 1 + i = sqrt(2i); zapis nasobi sqrt2,
cteni deli sqrt2; zlata cista forma je jednotka (vratna), striborne pero
jednotka neni (nevratne). Algebra je [T-grade, dvakrat overeno], cteni
beh/zaznam je [H-grade] a je to kandidat na utazeni mezikusu
SILVER-SIBLING a TWO-PLACE-PHYSICS.

## 1. The observation (author: Marek)

Write both metallic equations as x^2 = t x + 1. Gold has t = 1, silver
has t = 2. The integer t is the field trace of the fundamental root, and
it is the whole difference between the program's two places:

```
trace t                  1                       2
disc t^2 + 4             5                       8
ramified prime           5 (5 | 5)               2 (2 | 8)
real floor               Q(sqrt5)                Q(sqrt2)
fundamental root         phi, N(phi) = -1        delta = 1 + sqrt2, N(delta) = -1
growth law               F_(n+1) = F_n + F_(n-1) P_(n+1) = 2 P_n + P_(n-1)
character                compose (run, verb)     copy (record, pen)
pure form                J = 1 + zeta_5^2        1 + i = sqrt(2i)
norm of pure form        N(J) = 1 (unit)         non-unit: 2 in Q(i), 4 in Q(zeta_8)
```

The two primes of the program, the 5 that writes and the 2 that reads,
are then not two postulates: they are the discriminants of the two
simplest metallic equations, and each metal's prime is the ramified
prime of its own definition. The write side grows by composing the last
two steps (minimal memory, dynamics); the read side grows by doubling
the present step, and doubling is copying, which is what a record does.
The stroke of the pen is 1 + i = sqrt2 x zeta_8 = sqrt(2i): amplitude
sqrt2 (one step of Q(sqrt2) irrationality, one bit), phase pi/4; two
strokes are (1 + i)^2 = 2i, doubling times a quarter turn. Reading is
the other side of the same coin: the Hadamard normalization is
1/sqrt2 = 1/(m + m^-1), so write times read is exactly 1, the same shape
as the golden selector. And the arrow: the golden pure form is a unit
(the run is reversible), the silver pen is not a unit (a write cannot be
un-written for free), with the uncatchable gap phi^2 - 2 = 1/phi.

## 2. The exact layer [T-grade, twice witnessed]

All algebraic rows above are exact and verified by two independent
implementations:

```
author's witness   verify_metals_deep.py, 19 checks, ALL OK
                   sha256 9779ccfdb38fe40b51657eae7a438933ac14995ddf89f1f439a1605ebd2475c7
                   x86_64, Python 3.11, LC_ALL=C LANG=C PYTHONHASHSEED=0 TZ=UTC
this note's witness notes/metal-trace/verify_metal_trace.py, 19 checks, ALL OK
                   sha256 6e742fb01b23d1209fe1369c297530257df024190028fd258a46923f71d4ebdd
                   x86_64, Python 3.11.15, same neutral field
```

Honest evidence-class note: the two witnesses are independent
implementations but the same architecture (both x86_64), so under the
repository's evidence classes this is implementation diversity, not yet
a two-architecture record. A genuine aarch64 leg is required before any
registered claim could cite the two-architecture bar.

Checks carried by this note's witness (exact arithmetic only: Fractions,
quadratic fields as pairs, cyclotomic fields modulo Phi_8 and Phi_5):
discriminants 5 and 8 with their ramification; trace and norm of phi and
delta (both fundamental units of norm -1); the growth laws
phi^n = F_n phi + F_(n-1) and delta^n = P_n delta + P_(n-1) for
n = 1..60; sqrt2 = m + m^-1 = m - m^3 and i = m^2 at zeta_8;
(1 + i)^2 = 2i and 1 + i = (m + m^-1) m; the norms of 1 + i (next
paragraph); the non-unit lock 2 = -i (1 + i)^2; the unit carrier
m/delta (N(m) = 1, N_{Q(zeta_8)/Q}(1 + sqrt2) = 1); phi^3 = 2 phi + 1,
i.e. phi^2 - 2 = 1/phi; N(J) = 1; and the write/read duality
sqrt2 x (1/sqrt2) = 1 with (1/sqrt2)^2 = 1/2.

**One precision to carry forward.** "Each write multiplies the norm by
four" is field-dependent: N_{Q(i)/Q}(1 + i) = 2 at the Gaussian floor,
and N_{Q(zeta_8)/Q}(1 + i) = 4 = 2^2 in the degree-4 home that
TWO-PLACE-PHYSICS declares for the read place. Both are exact; any
registered row must name its field. The one-bit-per-stroke reading is
cleanest at the Gaussian floor (norm 2) or as the sqrt2 amplitude; the
factor 4 is its square in the full read home.

## 3. What is already registered

Individually, several rows of the table are Canon content already:
DEGREES-BY-PRIME [T] (sqrt5 at zeta_5, sqrt2 and i at zeta_8, disjoint
over Q), Z2-PLACES-SPLIT [T], J-UNIT [T] (N(J) = 1), SPINOR-FLOOR [T]
(N(phi) = -1 with the alternator), SILVER-RING-FACTS [C] and
SILVER-SIBLING [D] (the silver unit 1 + sqrt2 of norm -1 mirroring
tau = sqrt(J)), PENTIT-ROOT-FACTS [T] and MAGIC-PRIME-GATE [T],
BORN-HALF-ANGLE / SPIN-BISECTOR [T] (the sqrt2-normalized quadratic
step at the read place), TWO-PLACE-PHYSICS [D] (v_5 writes, v_2 reads,
as a dictionary with no uniqueness claim).

What is NOT in the Canon is the frame that binds them: the
single-parameter metallic family x^2 = t x + 1 with t the trace, in
which the two places are the t = 1 and t = 2 members, the two primes
are the two discriminant carriers, and the compose/copy split of the
growth laws is the candidate reason why one side runs and the other
records.

## 4. Where this lands in the architecture map

- **SILVER-SIBLING [D]**: the map's tightening path asks for "an exact
  structural correspondence theorem (a canonical map exchanging
  (5, tau, phi) and (2, m_8, 1 + sqrt2) data) rather than the current
  declared resemblance". The metallic trace family is a concrete
  candidate skeleton for exactly that theorem: one equation, one
  integer parameter, both fundamental roots of norm -1, both
  discriminants carrying their own ramified prime.
- **TWO-PLACE-PHYSICS [D]**: currently the write/read assignment is a
  pure dictionary. The compose/copy split of the recursions is a
  candidate derivation seed for WHY v_5 writes and v_2 reads. If it can
  be forced (not merely read), the dictionary's principal gap narrows.
- **Consonances, not claims**: ENTROPY-BLOCK-HALVING [C] (both block
  maps exactly two-to-one, one unresolved bit per scale: reading
  forgets one bit); BORN-ORDER-STAIRCASE [T] (each Born halving is one
  quadratic step at the prime 2); OBSERVER-WRITE-PORT [H] (the decoder
  is read-only: the record does not write back into the run).
- **Fence respected**: P5-ROOT-SELECTION [T] carries "no further
  coincidences are claimed as independent support for selecting
  p = 5". The discriminant story is therefore NOT glued onto that row.
  If it is to count as selection support, it must be registered as its
  own claim with its own falsifier.

## 5. Candidate registration path (sketches only)

If the author wants this in the Canon, the honest decomposition is:

1. `METAL-TRACE-FAMILY` [T candidate]: the exact family rows: trace,
   discriminant, ramification, unit norms, growth laws (checks 1-10,
   17-18 of the witness). Needs: preregistration, a reproduce/ bundle,
   two architectures. Pure algebra; should be uncontroversial.
2. `WRITE-ATOM-SQRT2I` [T candidate]: 1 + i = (m + m^-1) m,
   (1 + i)^2 = 2i, the field-named norms 2 and 4, the non-unit lock
   2 = -i (1 + i)^2, the unit carrier m/delta, and the write/read
   duality sqrt2 x (1/sqrt2) = 1 (checks 11-16, 19).
3. `RUN-RECORD-READING` [H candidate]: the reading "trace 1 composes =
   the run; trace 2 copies = the record; a write step carries amplitude
   factor sqrt2, a read step carries 1/sqrt2". Falsifier candidates:
   fires if a registered decoder write or read leg is exhibited whose
   exact amplitude factor differs from sqrt2 respectively 1/sqrt2, or
   if the completed decoder assigns the copy role to the t = 1 place.
4. `ARROW-NONUNIT` [H candidate]: irreversibility of the record carried
   by the non-unit write atom against the unit run (N(J) = 1 versus
   1 + i prime above 2). Falsifier candidate: fires if the completed
   decoder exhibits an admissible exact inverse of a registered write
   step (a unit realization of the write atom), or if the registered
   write atom is shown to be an element other than an associate of
   1 + i.

Order matters: 1 and 2 are registrable now (after prereg and a second
architecture); 3 and 4 only become decidable as the decoder closure
chain of the map (QUADRATIC-DECODER-DATA, METRO-ADMISSIBILITY) supplies
registered write and read legs to test against.

## 6. Witness

```
notes/metal-trace/verify_metal_trace.py   19 checks, ALL OK
sha256   6e742fb01b23d1209fe1369c297530257df024190028fd258a46923f71d4ebdd
platform x86_64, Python 3.11.15; one platform, exposure witness
field    LC_ALL=C LANG=C PYTHONHASHSEED=0 TZ=UTC
status   synthesis/exploration, no authority; algebra rows T-grade
         (twice implemented, one architecture), run/record reading H-grade
```
