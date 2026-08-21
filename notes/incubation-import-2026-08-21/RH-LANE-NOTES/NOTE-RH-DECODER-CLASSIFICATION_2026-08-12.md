# NOTE: RH as a decoder classification problem, REV2

```
Status     NON-CANONICAL working note. No authority. Opens no lane, edits no
           row, proposes no fold. Framing and gate design only.
Date       2026-08-12, revision 2 (same day; revision 1 superseded in place)
Origin     owner strategy statement of 2026-08-12, operationalized in rev 1;
           rev 2 applies the owner review of the same day.
REV2 delta G0 added (domain freeze). G2 relaxed from bare locality to one
           frozen functorial assembly. G5 given its exact coherence
           equation. G7 retyped as a total BRIGHT/DARK constructor. G8
           split into G8a type rejection with a named obstruction and G8b
           false-positive rejection. Verdicts split into two independent
           axes. The rev 1 lattice-falsifiability sentence corrected. The
           headline sentence moved under the reframing. ANO-7 disposition
           changed to deferred pending these gates.
```

## 0. Provenance and basis

Public gate rerun in this session from a fresh clone of mathorn1973/twist-j:

```
STATE ACTIVE, CANON Public Canon v45, TAG canon-v45
CONTENT_COMMIT cbd248274d67a861611787ba6e7be3e6a13b29f1   ancestor of main
tag canon-v45 = 84e7a81faaffa70d04398b4e535cf7b456624dc2  ancestor of main
CANON_SHA256 f3f8954bda620836e604d08d9088587ea84429ecdadfc27737e83b0f8031128b
CANON_BYTES 214608, both confirmed against canon/CANON.md
canon/SHA256SUMS 5 of 5 OK
```

Rows read at v45: PENTAGON-NORMALIZATION [T], SPLIT-PRIME-RAPIDITY-
INDEPENDENCE [T], REDUCED-SPLIT-GENERATOR-HEIGHT [T], LAMBDA-COCYCLE-ANGLES
[H] with its grid equivalence, MINIMAL-READ-DERIVATION [O]. Verified for
rev 2: DEF-DECODER-COMPLETION-CONTRACT is present at v45 as a normative
DEFINITION (canon/CANON.md, section 2, Time, space, and the decoder;
NORMATIVE.tsv row; the text states it supplies only the finite typed
manifest and refines the declared partial decoder chain without asserting a
completed decoder). No Beurling row exists at v45 (REGISTRY and canon texts
checked), so the G8b lead in this note is new to the program and unpinned.

Project sources read: MILESTONE-2026-08-12_CZ.md, NOTE-WEIL-TOWER-RANK-
DIAGNOSIS_2026-08-12.md, REVIEW-NIGHT-ENGINE_2026-08-12.md,
STAGE-B-NOTE-C-PRIME-ORDER-READING-1_2026-08-11.md,
C-PRIME-ORDER-READING-1_2026-08-11.md, NOTE-PRIMES-IN-J-DIALOG_2026-08-11.md,
CANON-v28-CTENARSKA-VERZE_2026-07-30.md (J-LI carrier no-go family).

Cited as owner-reported and NOT verified in this session: the matrix Hecke
corner P_0(X) = (Tr X / 2) I with P_0 Q P_0 = Q_zeta, and the [F] on the
hoped projector-to-form positivity transfer.

## 1. The reframing [owner statement, restated]

Stop treating the lane as an attack on RH. Treat it as the classification of
admissible RH decoders: constructors that read a positive geometry out of
Euler data, with zeros entering only as the spectrum of the reading, never
as input. The public line already runs this verdict logic for the physics
decoder: DEF-DECODER-COMPLETION-CONTRACT freezes the finite typed manifest
first, and MINIMAL-READ-DERIVATION [O] closes only against the complete
admissible class, positively on unique forcing, negatively on a proved
nonempty class with inequivalent members, STOP while the class is
incomplete. The reframing imports that logic into the Weil lane.

The headline, and the rank diagnosis is its proof of relevance:

```
A finite PSD readout is not a result.
The result is the uniform arithmetic square root.
```

Rank of a finite cut tracks visible zeros, so the only known square root of
a finite cut is zero-indexed, and PSD at finite cut is exactly what
classical zero verification already guarantees.

## 2. Criterion versus constructor [D]

Positivity criteria equivalent to RH are plentiful: the Weil form, Li
coefficients, Nyman-Beurling density. A criterion restates the target. A
decoder is a constructor: input a point of the frozen Euler class, output a
typed verdict whose BRIGHT branch carries a Gram root A with Q = A* A.
Criteria we have; constructors we do not. The classification is of
constructors up to the equivalence frozen in G0; without that quotient
UNIQUE versus NONUNIQUE is ill posed, because coordinate changes masquerade
as new decoders.

## 3. Admissibility gates (REV2)

Each gate names the check that fails it. A candidate enters the table with
its failed gates listed, or with none.

```
G0 DOMAIN FREEZE     before any candidate is tested, freeze: the input
                     category E (objects: axiomatized Euler data; morphisms
                     Mor(E)), the directed family of test spaces V_R with
                     inclusions j_RS for R <= S, the equality notion, the
                     decoder equivalence relation, and the counterfeit
                     battery. Changing any of these after seeing a
                     candidate restarts the classification. House anchor:
                     DEF-DECODER-COMPLETION-CONTRACT, the typed manifest
                     before any completion claim.
G1 INPUT PURITY      the constructor is a computable functional of the
                     frozen Euler data, defined on all of E; no zeros in
                     the definition, the normalization, or a closure chosen
                     to make the target work.
G2 EULER             each local Euler datum enters under its own place
   FUNCTORIALITY     label. The constructor may combine places only through
                     one frozen assembly rule, fixed classwide before any
                     candidate run and natural in E (commutes with Mor(E),
                     which makes the no-post-hoc requirement checkable
                     rather than stylistic). No cross-place pairing, sign,
                     weight or normalization selected after inspecting the
                     target form or its spectrum. NOT required: that the
                     square root of a sum of local forms be a sum of local
                     square roots. The freeze is on the rule, not on
                     locality of the output.
G3 ARCH COMPLETION   the constructor produces the full gamma term; assuming
                     the completed xi as given is a G3 failure.
G4 EXACT NORM        global normalization is part of the constructor,
                     exact, with no constants fitted after the fact.
G5 UNIFORMITY        one constructor for all cuts, with the coherence
                     equation. For R <= S, with A_R : V_R -> H_R and
                     isometries U_RS : H_R -> H_S, all classwide data:

                         A_S j_RS = U_RS A_R,     U_ST U_RS = U_RT.

                     Then Q_R = A_R* A_R is one object seen in growing
                     windows, not a series of unrelated Cholesky
                     factorizations (a PSD matrix of rank r is the Gram
                     matrix of r vectors; per-cut factorization certifies
                     nothing). Built-in consistency check: the target side
                     satisfies Q_S(j x, j y) = Q_R(x, y) automatically,
                     Weil forms restrict along test-space inclusions, so
                     the equation constrains A and U, never Q. The diagram
                     is natural in E; per-input tuning of U is excluded
                     because U is classwide. Decoder equivalence: a
                     coherent family of intertwiners between the H systems
                     commuting with the Euler action. UNIQUE means the
                     groupoid of readings is contractible.
G6 GRAM OUTPUT       in the BRIGHT branch, Q = A* A holds as a term-level
                     identity against the prime side of the explicit
                     formula, provable without the zero side. The main
                     prize.
G7 TYPED READOUT     the constructor is TOTAL on the frozen class:

                         D(E) in { BRIGHT(A), DARK(w) }

                     with BRIGHT(A) if and only if Q_E >= 0, the BRIGHT
                     branch proved on the prime side (G6), and DARK(w)
                     carrying an exact certified witness w with
                     Q_E(w) < 0. Bare nonexistence of a reading is not a
                     verdict. Asymmetry, stated so it is not rediscovered:
                     DARK is semidecidable, a finite witness certifies it;
                     BRIGHT is where the mathematics lives; at finite
                     computational stage the honest state is UNDECIDED,
                     reported, never pushed (this is exactly U2 of the rank
                     diagnosis, certified inertia, lifted to the
                     constructor level). Totality on the ideal class is a
                     theorem obligation on the candidate, not an
                     algorithmic promise per finite stage. Surplus rigidity
                     stays disqualifying: a candidate whose BRIGHT branch
                     requires conditions beyond Q_E >= 0 has an image too
                     small to be canonical. Correction against rev 1: the
                     lambda-adic grid condition is NOT logically
                     unfalsifiable; it is falsifiable by an exact algebraic
                     or transcendence exclusion of an ordinate, and the
                     public row carries exactly that falsifier with a
                     one-sided finite channel. What the density of Z[1/5]
                     blocks is deciding membership by numerical refinement
                     alone. Rev 1 overstated this; the row was always
                     honest.
G8a COUNTERFEIT      a non-Euler fake such as DH must be rejected for one
    TYPE REJECTION   exact named Euler-local obstruction, not merely
                     declared out of domain. For DH the witness has the
                     shape of a single certified multiplicativity violation
                     in the coefficient field Q(kappa), for instance
                     c(2) c(3) != c(6); behind it the finite lemma that a
                     real nonzero 5-periodic completely multiplicative
                     sequence is a Dirichlet character mod 5, and the DH
                     mix is not one. Candidate-grade until pinned by a
                     prereg; cheap; belongs in every prereg of this frame
                     as the typed guard.
G8b FALSE-POSITIVE   any admitted member of the frozen comparison class
    REJECTION [O]    with certified failure of Weil positivity must return
                     DARK. Honest difficulty: a known genuinely Euler
                     counterfeit of RH is not obvious, and the gate must
                     not pretend to a control we do not have. One lead,
                     literature grade, to be pinned before any use [H-lit]:
                     Beurling generalized-prime systems keep Euler
                     multiplicativity and provably violate the RH analogue
                     for constructed systems; whether they enter the class
                     depends on whether the class demands the exact
                     functional equation. If the class excludes them, G8b
                     currently has no known inhabitant and must say so.
                     Epstein control: freeze ONE object, its normalization,
                     and a citable off-line witness before public use;
                     house-natural candidate is the binary form
                     x^2 + 5 y^2, discriminant -20, class number 2, pending
                     the literature pin; until pinned this stays [O].
```

Notation hygiene, one line: P_0 currently names the pentagon filter series
(public row), the trace projector of the matrix Hecke lane, and a projector
in the F_5^6 paper. Any public text of this frame renames the projectors
before the collision propagates.

## 4. The candidate table as of 2026-08-12

```
CANDIDATE                      GATES FAILED        READING OF THE FAILURE
pentagon filter P_0(s)         G6 by absence       channel recovery [T]; the
  (public row)                                     probe's own closing line:
                                                   no test space, no positive
                                                   form, no operator emerged.
matrix Hecke corner            G6 by absence       canonical channel selector:
  (working branch,             (transfer [F])      P_0 Q P_0 = Q_zeta selects
  owner-reported)                                  exactly the form whose
                                                   positivity is the target;
                                                   projector positivity does
                                                   not transfer; no A built.
lambda-adic cocycle route      G7 surplus          a genuine reading whose
  (LAMBDA-COCYCLE-ANGLES [H]                       BRIGHT branch requires RH
  + grid equivalence [T])                          AND every Cayley angle in
                                                   2 pi (1/4) Z[1/5]. Image
                                                   too small to be canonical.
                                                   Type specimen of a G7
                                                   failure; the row itself is
                                                   honest and stands as H.
night engine Gram tower        G5, G6 open;        first execution of the G8
  (recon lane, DRAFT-PREREG    G8 executed once    battery: one frame PSD on
  C-WEIL-GRAM-TOWER-1,         at float grade      the zeta/chi_5/xi tower,
  ANO-7 deferred, see D-A)                         indefinite on DH with dh+
                                                   inertia (3, 148, 179).
                                                   Note the engine did NOT
                                                   reject DH by type: it
                                                   computed DH's own -f'/f by
                                                   divisor recursion and let
                                                   it fire negative. That is
                                                   a numerical DARK verdict
                                                   on an admitted fake,
                                                   stronger than the G8a
                                                   minimum; R2 (interval
                                                   LDL^T) upgrades it to
                                                   certified.
J-LI carrier no-go family      terminal for        E8 shells, Haar-Koopman HS
  ([T] no-gos, [F] rows)       their carriers      route, scaling shift:
                                                   three carrier classes
                                                   closed negatively. EMPTY
                                                   verdicts at fixed carrier,
                                                   correctly recorded.
external context (literature)  unread against      Connes trace positivity on
  Connes, Deninger             the gate list       the adele class space;
                                                   Deninger regularized
                                                   determinant cohomology.
                                                   Decoder attempts in this
                                                   exact sense, neither with
                                                   number-field positivity
                                                   landed. To be read against
                                                   the gates once, carefully.
```

Three house candidates fail three different named gates, and one lane has
already executed the battery once. The gate list discriminates today. That
is the argument that the classification is a program and not a taxonomy of
essays.

## 5. What the frame does not do

No gate lowers the difficulty. The dividing line the gates enforce, Euler
multiplicativity against bare functional-equation symmetry, is exactly the
classical hard line, and the frame localizes the difficulty there instead
of hiding it. With G0 frozen, admissibility can no longer drift toward what
a candidate happens to manage, which is the failure mode that turns
classifications into taxonomies. And PSD at finite cut stops being
reportable as progress, because the readout is certified rank and inertia
(U2), and because of the headline sentence of section 1.

## 6. Verdicts: two independent axes

```
CLASSIFICATION   property of the frozen class:
                 UNIQUE / NONUNIQUE / EMPTY / STOP
READOUT ON ZETA  property of the input, delivered by the constructor:
                 BRIGHT / DARK / UNDECIDED
```

The independence is structural, not prudential: BRIGHT versus DARK is
determined by Q_E alone (G7), hence decoder-independent; decoders differ in
the witness A they carry. The cells that matter:

```
UNIQUE + BRIGHT(zeta)  the wager: positivity not inserted but read off the
                       single admissible reading, prime side. RH with a
                       mechanism on the carrier.
UNIQUE + DARK(zeta)    a certified witness: RH disproved. First-class
                       outcome; the frame is symmetric and does not presume
                       the sign of the answer.
UNIQUE + UNDECIDED     the expected long middle; report, never push.
NONUNIQUE              canonicity dies; G7 readouts stay valid, the
                       mechanism story does not; record and re-aim. The
                       physics analogy of one forced reading takes real
                       damage.
EMPTY                  proved: no constructor satisfies the gates even
                       assuming RH. First-class major result; the substrate
                       admits no arithmetic square root on this carrier,
                       bounding the physics decoder analogy from above.
                       Already locally inhabited: the J-LI no-gos are this
                       verdict at fixed carriers.
STOP                   authority or basis unclear, per contract.
META                   an all-gates BRIGHT on a battery fake breaks G8
                       soundness and kills the frame in one shot.
```

## 7. Dispositions instead of new lanes

Owner decision 3 already lists five packaged lanes with no public movement.
This note opens nothing and proposes consuming the frame through what is
already pending:

```
D-A  ANO-7 DEFERRED (owner decision 2026-08-12): DRAFT-PREREG-C-WEIL-GRAM-
     TOWER-1 is not to be frozen under the rev 1 gates. Pre-freeze
     checklist, verbatim: (1) G0 domain freeze, (2) the exact G5 coherence
     equation, (3) G7 as BRIGHT/DARK, (4) G8 split into type rejection and
     false-positive test. After these, the draft's current content sits at
     the G8 practical test plus part of G5, with R1 + R2 and the rank rules
     U1..U3 as already stated, and G6 remains the main prize.
D-B  the four PROMO-J-LI-* proposals belong to the lambda-adic and Li
     complex: re-target them as entries of the candidate table (G7 surplus
     and carrier no-gos) or fold them as they stand. Either move closes
     open decision 3 for that group.
D-C  the cheap calibration of G5 (exhibit, Fraction-only on small nested
     cuts, that per-cut factorizations do not cohere under refinement
     without arithmetic input) fits inside the same prereg as a readout,
     not as a lane.
D-D  pin the G8a witness for DH (one page, exact, the multiplicativity
     violation in Q(kappa)) and freeze the Epstein object with its
     citation. Both belong to the same pre-freeze pass as D-A.
```

## 8. A direction, not a lane [H]

The addresses carry no order; the counter does. v45 holds independence of
split-prime rapidity classes [T], so the compact coordinate is a real
infinite-rank address book, and the milestone names the deficit exactly:
the addresses do not carry the order. In this frame the missing operation
has a classical analytic shape: positive equals square of causal is
spectral factorization, so the arithmetic square root would be a kernel A
triangular with respect to the counter (norm order), with A* A equal to the
prime side plus the boundary term, and the coherence isometries U_RS of G5
would be the window extensions of one causal filter. The gamma term then
sits where the program already puts boundaries. Declared layers if this
ever becomes a lane: addresses L4, stream L5, reading L6, two named lifts,
each with its own gate. Where it will fight: the archimedean and boundary
terms, and a Szego-type condition on the arithmetic side. Where it
connects: C-PRIME-ORDER-READING-1 is the order question asked from the
other end; its F4 risk (over a computation-universal substrate bare
existence is trivial and uniqueness is false; all content lives in how
tightly admissibility is defined) is the house-internal statement of why
G0 must exist and the gates must be tight; and its answering stage already
declares a dependency on open decoder rows. The two lanes are one lane read
from both ends.

## 9. Relation to the physics decoder lane

Same verdict logic as MINIMAL-READ-DERIVATION [O], now with the same
completion discipline (G0 against DEF-DECODER-COMPLETION-CONTRACT). One
structural asymmetry stays visible: physics has an empirical leg, observed
reality constrains the reading; arithmetic has only finite verified cuts
[C] and the fake battery, so all discriminating power on the arithmetic
side lives in the gates and the fakes. Expand the battery accordingly, and
read every surplus-rigidity candidate as a diagnosis of the candidate,
never as a claim about the world.

The shared question of the RH branch and the TWIST-J decoder, after this
revision, is one sentence:

```
Is the admissible class complete, and does it contain exactly one
equivalence class of readings?
```

Existence of some reading is cheap on a computation-universal substrate.
Completeness of the class plus uniqueness up to equivalence is the entire
content, on both sides.
