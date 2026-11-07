# Mathematical review of the fixed receiver, root clock and stock census

Status: NON-CANONICAL / L1. This is a review record, not a Canon fold. It
was written before review.py was pinned or executed. Nothing in it relies
on output from any code.

**Target.** PR #1930 at head 3d8d364cb981bb5d53bbede432fb5a4ac4181709,
directory `notes/C-LOADED-CURRENT-WORK-PHASE-COMPATIBILITY-N`. The reviewed
texts are RECEIVER-CONTACT.md, RECEIVER-DYNAMICS.md, RECEIVER-OBSTRUCTION.md,
RECEIVER-RESULT.md, STOCK-BOUND.md, STOCK-RESULT.md and REVIEW-RESPONSE.md.
TARGET-SHA256SUMS binds them. The comparison authority is Public Canon
v109, `canon/CANON.md`, RELATIVE-CONTACT-INTEGRAL-LAW, SHA-256
035408ec79219cc72a7d3613cf1568154cca185137d2a2daa43b896aae0c6383.

## How this review was made

There were eight code-free reviewers, each in its own fresh context. One
reviewer took each scope S1 to S7 of PREREG.md. An eighth, S8, checked
consistency across documents and the status labels.

Each reviewer read only:
- PREREG.md;
- the target Markdown files above, by `git show` at the head;
- the Canon contact-law section.

No reviewer read any `*.py`, EXPECTED, RUN, INFORMAL, PR, issue or CI
material, and no reviewer ran code. Every derivation was redone by hand.
In total the reviewers checked 212 claims and filed 83 findings.

The findings are of four kinds. Each finding of kind error, gap or
overstatement went to two further skeptics, in fresh contexts, who were
asked to refute it. A finding survived if at least one skeptic failed to
refute it. Of the 14 findings tested, 13 survived. S5-F4 was refuted by
both skeptics and is withdrawn. Findings of kind wording or note were not
sent to skeptics. The coordinator checked the substantive ones by hand.
Among them are the swap counterexample, the holonomy sign, the j^3 S
response and the mod-5 bound.

**Exposure.** None of the reviewers was blind. RECEIVER-RESULT.md,
STOCK-RESULT.md and PREREG.md, all of which they read, state the target's
results and the frozen expected values. The coordinator, who compiled this
text, is exposed as recorded in PREREG.md section 2. This review is
independent of the target's code. It is not independent of the origin of
the hypotheses. The reviewers' working records stay in the session and are
summarized here. They are not part of the repository.

## Verdict

No mathematical error was found in the target. Every finite and infinite
statement in scope that the reviewers could reach by hand is correct within
its declared domain. The defects are of three kinds:
- missing proof steps, each one or two lines long;
- a few sentences that, read literally, state more than is proved;
- wording, notation and provenance phrasing.

One false equality was found, in this review's own PREREG.md (R7). The
target does not contain it. It is handled by PREREG-AMENDMENT-1.md.

| Scope | Content | Verdict |
| --- | --- | --- |
| S1 | Operational distinction: names versus re-encodings | Accept with stated corrections E1-E3 |
| S2 | Fixed receiver R, response, backreaction, inverse, accounts | Accept with stated corrections E4-E7 |
| S3 | Root clock V_m, period 25, padded calendar, minimum account | Accept with stated corrections E8-E13 |
| S4 | Relative phase, unit covariance, D_m gauge | Accept with stated corrections E14-E19 |
| S5 | Linear obstruction over K=Q(j) | Accept with stated corrections E20-E24 |
| S6 | Positive H_m family | Accept with stated corrections E25-E28 |
| S7 | Stock census, minimum 22, B1, T and S, B4 | Accept with stated corrections E29-E33 |

E34 and E35 apply across documents. None of the corrections changes a
conclusion. A Canon text built from this target should include them.

Each correction carries one of three marks:
- **R (required restriction).** As written, the statement is false or
  reads as false. It must be narrowed.
- **G (proof gap).** The statement is true, but a step is missing.
- **W (wording).** Notation, vocabulary or provenance. Recommended.

## S1 Operational distinction

Checked by hand:
- the Proposition of RECEIVER-OBSTRUCTION section 1 and its induction;
- the re-encoding rule (1+5t)r mod 25, which keeps r mod 5;
- high digits that are all distinct exactly when r mod 5 != 0;
- the witness r=13: labels (13,3,18,8,23), high digits (2,0,3,1,4), and
  readings (2,32,7,17,27) against a single reading 2 for five names on the
  unchanged state.

The distinction is correct. Five names attached to one unchanged state are
one preparation. Actual re-encodings are different preparations.

- **E1 (W).** The headline of RECEIVER-RESULT.md drops the relative-frame
  qualifier, and its "phase" is interpretive. Suggested wording: "A single
  fixed ordinary-contact receiver distinguishes, relative to its fixed
  stock frame, five actual unit-amplitude input preparations (j^b,-j^b) and
  five explicitly implemented clock laws applied to one common preparation,
  by an integer quadratic-account response. It does not select which law
  occurs." [S1-F1, S8-F13]
- **E2 (W).** The proof of RECEIVER-OBSTRUCTION section 1 speaks of "the
  fixed joint transition". The receiver alternates C(p,R) and C(p,q), so
  the transition depends on the step. Write "the fixed, possibly
  step-dependent transitions F_n", or include the program counter in the
  state. [S1-F2]
- **E3 (W).** "zeta^5=j" does not fix zeta, since there are five such
  roots. State zeta=exp(2 pi i/25) at the marked embedding. Write the
  witness digits as (r_0,r_1)=(3,2). [S1-F3, S6-W2]

Notes:
- The Proposition is a tautology once its hypothesis holds. Its content
  is checking that hypothesis for the old construction, and the text does
  that correctly. The executed name control therefore carries no
  independent evidential weight, and review.py marks it as an identity
  control. [S1-N2]
- On the two-pair register, E_t is (r_0,r_1) -> (r_0, r_1+t r_0 mod 5).
  It is not a product of single-pair maps. This supports the point that
  the receiver frame must be fixed independently. [S1-N4]

## S2 Fixed receiver

Checked by hand:
- Q(R)=32, Q(a)=7, Q(1+a)=10;
- (1+a) abar = (7,4,1,2,6), with sum 20;
- the admission pattern and the first hit at block k=2b mod 5;
- R_n = 1+a+rho^n a for n=1..5: (1,1,1,1), (3,2,0,-1), (2,3,3,1), (1,0,-1,-1),
  (3,4,2,0), with Q (2,27,17,7,32);
- readings (32,17,2,7,27) and work (0,15,30,25,5);
- accounts 36 and 68;
- the 40-contact literal inverse.

A compact closed form also holds: reading(b) = 5c_b - 3 with
c=(7,4,1,2,6), because 2n = b mod 5 at the hit.

- **E4 (G).** The refusal argument uses two facts mod 2 without proof:
  O/2O is a field, and j^c = 1 mod 2 only when 5 divides c. Insert: "2 has
  order 4 modulo 5, so Phi_5 is irreducible over F_2 and O/2O=F_16. For 5
  not dividing c, N(1-j^c)=5 is odd, so j^c is not 1 mod 2. Hence 1-rho^n
  is nonzero in F_16 for n=1..4." [S2-F1, S8-F6(iii)]
- **E5 (G).** The text never says why every stock contact after the first
  hit admits, which (R9) needs. The reason is that p_n-R_n = -2 rho^n a
  lies in 2O, and the balanced contact refuses for n<=4 and leaves p
  unchanged. [S2-F2, S8-F6(ii)]
- **E6 (W).** "calorimetric receiver", "terminal energies", "receiver-work"
  and "the record has backreaction" use physical words for the arithmetic
  account. The Canon contact-law section explicitly excludes that
  identification. Use "loaded stock receiver", "terminal account Q" and
  "account transferred". The backreaction acts on the pointer, not on the
  record. [S2-F3, S2-F4, S8-F13]
- **E7 (W).** In (R10), w_(2n mod 5) is undefined and clashes with the
  eigenvectors w_t of section 4. In (R8), "R" names both the stock slot and
  its initial value. Name the coefficients c, and write the word as
  [C(p,X), C(p,q)]^5 with slot X initialized to R. [S2-F5]

Notes:
- All five inputs carry the same account 4.
- For b=0 the disturbance is a phase rotation only. [S2-F7]
- The disclaimer that the account-32 stock is not minimal is borne out by
  STOCK-BOUND.md. A pointer to it beside the disclaimer would help.
  [S2-F8]

## S3 Root clock

Checked by hand:
- the compressed and padded words;
- V_m(z) = (j^(m+1) z_4, j^m z_0, ..., j^m z_3) on neutral states;
- V_m^5 = jI on the neutral carrier;
- C^3 on every pair after five ticks off the neutral carrier;
- least period 25 on nonzero neutral states;
- the inverse word;
- 23 attempts with 8 swaps;
- the minimum neutral account 4.

The texts make no claim about calendars or physical duration beyond what is
proved.

- **E8 (G).** The minimum-account argument asserts Q(a)^2 - 5B^2 = 4N(a) >= 4
  without derivation. It also leaves phi, A and B undefined. Either add
  the derivation, with phi = 1+j+j^4, Q = 2A+B, N = A^2+AB-B^2 and N >= 1, or
  use the shorter argument. Since 2Q = 5 sum c_i^2 - (sum c_i)^2, which is
  -(sum c_i)^2 mod 5, Q=1 would need (sum c_i)^2 = 3 mod 5. That is
  impossible, so every nonzero a has Q >= 2, with equality exactly on
  U10. [S3-G1, S4-F1, S8-F16]
- **E9 (G).** Off the neutral carrier, "five ticks apply C^3 to every pair"
  needs its counting step. In five ticks each pair occupies every position
  once and receives C^(3(m+1)+4*3m) = C^(15m+3) = C^3. A stronger form
  also holds: the V_m word equals T^(1+5m) on all of O^10, where T is the
  V_0 word. [S3-G2, S3-N1]
- **E10 (W).** "Reverses the contact powers" should say that each C^p is
  replaced by C^((5-p) mod 5), followed by the swaps in reverse order. Each
  pair swap exchanges first slot with first slot and second with second,
  so neutral orientation is kept. [S3-W1, S3-W2]
- **E11 (R).** "Identity padding ... does not ... preserve an unspecified
  path-action register" asserts a negative that is not proved. Write: "The
  C^5 padding blocks compose to the identity and preserve endpoints. They
  derive no physical duration, and they are not shown to leave any
  separately added path-action register unchanged." [S3-W3]
- **E12 (R).** "A 25-period root clock" holds on nonzero neutral states.
  Single occupied states off that carrier can have period 1 or 5. Write
  "least period 25 on every nonzero neutral state (order exactly 25 on
  O^10)". [S3-W4]
- **E13 (W).** Spaces are missing between words and numerals throughout
  RECEIVER-DYNAMICS.md and STOCK-BOUND.md: "period25", "account4",
  "minimum22", "modulo2 is1" and others. [S3-W5, S7-F8]

Note: the number 23 comes from the chosen padding layout. It is not a
forced or minimal common calendar. [S3-N2]

## S4 Relative phase and gauge

Checked by hand:
- C(up,uq) = uC(p,q) on both branches, for every unit u of O;
- Q(ua) = Q(a) exactly for u in U10, with Q(phi) = 3 as the counterexample
  for other units;
- q_n(m,X) = q_n(0, j^(-nm) X) for n=1 and n=13, where j^(-13m) = j^(2m);
- D_m V D_m^-1 = j^m V;
- H_m = D_m H_0 D_m^-1.

The relational conclusion is correct. The reading depends on the
preparation, the law m and the stock only through their relative element.

- **E14 (G).** STOCK-BOUND section 3 states the rotation rule B4 without
  its one-line derivation, which is unit covariance with u=j^s applied to
  the stock alone, plus input relabeling. STOCK-RESULT section 3 states
  q_n(m,T) = q_n(0, j^(-nm) T) without proof or a pointer to
  REVIEW-RESPONSE section 1. [S4-F7, S7-F3]
- **E15 (R).** V_m = j^m V_0 and D_m V_0 D_m^-1 = V_m are identities of
  amplitude maps on the neutral carrier O^5. They do not hold slot by slot
  for the ten-slot words on all of O^10. Add "as linear maps on the neutral
  amplitude carrier" wherever they are stated. If gauge equivalence of the
  total words is wanted, the contact word G_m = prod_k C_(pair k)^(3km mod 5)
  conjugates them exactly on O^10. [S4-F2, S8-F4, S4-N1]
- **E16 (W).** REVIEW-RESPONSE section 1 mixes two transformations:
  - global multiplication by u in U10, an exact symmetry of every word and
    account;
  - the gauge D_m, which relates (V_0, e0, X) to (V_m, e0, j^(km) X) for a
    receiver at site k.

  State both. Replace "no character in isolation has been measured" by the
  relative-element statement, and "energies" by "accounts". [S4-F3, S4-F5,
  S4-F6]
- **E17 (W).** S names both a generic stock (q_n(m,S), "Q(S)=22") and the
  specific stock 2-2j+j^2. Use X for the generic stock. [S4-F4, S7-F7,
  S8-F12]
- **E18 (W).** STOCK-BOUND section 3 should say "torsion unit
  u = +-j^s". Contact covariance holds for every unit; Q invariance holds
  only for these ten. [S4-F8]
- **E19 (R).** "Their connection product around the cycle is the same j"
  does not say which coefficients it multiplies. The hopping coefficients
  of V_m multiply to j^(4m) * j^(m+1) = j. The forward off-diagonal entries
  of H_m multiply to (-j^m)^5 * j = -j. Write "the hopping coefficients of
  V_m multiply to j around the cycle for every m". [S4-F9, S6-W1, S8-F3]

Note: the compensating stock rotation depends on the attachment site. It is
j^(km) at site k. If the n=1 and n=13 experiments share one stock frame, no
single rotation j^s reproduces both V_m readings from V_0 when m != 0 mod 5.
For example, V_1 with R gives (17,32). V_0 with j^s R, s=0..4, gives (32,2),
(27,17), (7,32), (2,27) and (17,7). A receiver frame shared across sites is
therefore itself a supplied identification. [S4-N3]

## S5 Linear obstruction over K=Q(j)

Checked by hand:
- Eisenstein at 5 for Phi_25(X+1);
- [L:K] = 5 and the irreducibility of X^5 - j over K;
- the twenty-element basis zeta^(5i+k);
- nonzero projection of every nonzero K^5 vector on every mode;
- the commutant K[V], a field;
- no nontrivial idempotent;
- the dimension of every K-space with K-linear W^5 = jI is a multiple of 5.

All S5 claims are true.

- **E20 (R).** "It does not exclude ... nonlinear controllers" can be read
  as allowing a nonlinear controller to prepare an exact pure mode in K^5.
  That is false: no nonzero state of K^5 is a pure mode, however it is
  produced. Write: "No nonzero state of the K^5 carrier is an exact pure
  mode, however it is produced. The filter statement concerns commuting
  K-linear maps only. Approximation, limits, nonlinear or
  embedding-dependent selection records, added references and extended
  coefficient fields are not excluded." [S5-F1]
- **E21 (R).** "This excludes exact commuting linear filters", read
  literally, excludes V itself. What is excluded is nonzero non-invertible
  commuting K-linear filters, in particular nontrivial projectors, and
  exact pure-mode states. [S5-F7]
- **E22 (G).** The passage from "minimal polynomial X^5 - j" to "dimension a
  multiple of 5" needs one line. U is a vector space over the field
  K[W] = L, so dim_K U = 5 dim_L U. "Finite K-vector space" should read
  "finite-dimensional". [S5-F3]
- **E23 (G).** (R11) is derived from the diagonal pairing alone. It also
  needs three facts: l_t is a left eigenvector, l_t.w_t' = 5 delta_(t,t'),
  and the w_t form a basis. RECEIVER-OBSTRUCTION should cite
  c_t(e_0) = 1/5 rather than only assert it. [S5-F5]
- **E24 (W).** Three wording fixes:
  - "prime-power degrees" should be "prime-power orders" (25 and 5); the
    degrees are 20 and 4;
  - "faithful twenty-fifth-root eigenvalue" should be "an eigenvalue that
    is a primitive 25th root of unity";
  - REVIEW-RESPONSE section 3 should say that the map K^5 -> L,
    P(V)e_0 -> P(lambda), carries the basis j^i V^k e_0 to the power basis,
    and should replace "Equivalently" with "Hence, by the tower law".

  [S5-F6, S5-F11]

S5-F4, which claimed that two links of the irreducibility chain were
missing, was refuted by both skeptics and is withdrawn.

Notes:
- The obstruction holds in every K-space with a K-linear W^5 = jI, not
  only in K^5. Enlarging the representation does not escape it without new
  scalars or non-commuting structure. [S5-F2]
- Gal(L/K) permutes the five projections cyclically. So the set of
  vanishing projections is empty or everything, which is a second proof of
  nonzero projection. [S5-F9]
- At the principal embedding, approximation of any eigenline by O^5 states
  is available, with unbounded account. [S5-F10]

## S6 Positive H_m family

Checked by hand:
- H_m = 2I - j^m V - j^-m V* = (I - j^m V)*(I - j^m V);
- eigenvalues |1 - zeta^e|^2 with e = 1+5(t+m) mod 25, all positive;
- det H_m = (1-j)(1-j^-1);
- the ground mode t = -m at the principal embedding, with d values
  (1,6,11,9,4) for m=0;
- equal support and holonomy against unequal coefficients;
- the argument that positivity does not select H_0.

- **E25 (R).** "Reversible unitary evolution preserves eigenmode weights. It
  does not cool into the selected ground mode." This sentence, its
  REVIEW-RESPONSE section 2 counterpart and its RECEIVER-RESULT echo are
  proved only for unitaries that commute with V. For a general reversible
  map they are false. Inside the native repertoire, the pair swap (1,2)
  sends e0+e2 to e0+e1 and halves the normalized H_0 energy, from 2 to 1.
  Write:

  > "Unitary evolution that commutes with V, in particular the clocks V_m
  > and every exp(-is H_m'), multiplies each mode coefficient by a phase.
  > It therefore preserves every eigenmode weight and <H_m>. A general
  > reversible map can lower the energy of particular inputs. No reversible
  > linear map cools all inputs, because it is injective and
  > Tr(U* H_m U) = Tr H_m = 10. Within K^5 no linear map, and no contact or
  > swap word on the native carrier, produces a state on the exact ground
  > ray, by (R11)."

  [S6-O1]
- **E26 (G).** The text does not say that V is unitary (V* = V^-1 = j^-1 V^4).
  Hence V* w_t = lambda_t^-1 w_t and H_m w_t = |1 - j^m lambda_t|^2 w_t, so
  "positive" means positive definite. One line covers all three. [S6-G1]
- **E27 (W).** The ground-mode statement needs the marked embedding
  zeta -> exp(2 pi i/25). zeta^1 is strictly nearest to 1 among zeta^1,
  zeta^6, zeta^11, zeta^16 and zeta^21, with chord lengths 2 sin(pi d/25),
  d = 1,6,11,9,4. RECEIVER-RESULT should add "at the principal complex
  embedding" to its ground-state sentence. [S6-W2, S8-F2]
- **E28 (W).** Two phrases in RECEIVER-DYNAMICS section 5 need fixing.
  "Every normalized complex eigenmode has the same norm" is a tautology.
  "The same nearest-neighbor cyclic support and positive quadratic form"
  can be read as "the same form", which is false, since the forms differ
  with m. Write "a positive definite quadratic form; the forms differ with
  m". [S6-W3]

Notes:
- **The selection depends on the embedding.** Fix the principal embedding
  of K and let the embedding of L run over its five extensions,
  zeta -> zeta^a with a = 1,6,11,16,21. The abstract root that H_0 selects
  then runs over t = 0,4,3,2,1. H_0 alone therefore singles out no root of
  X^5 - j. [S6-N1]
- **Positivity moves the selection problem.** The ground mode of H_m is
  always the V_m eigenvector with eigenvalue zeta. Choosing H is choosing
  the clock. The native integral energy E_m(z) = sum_k Q(((I-V_m)z)_k)
  satisfies E_m(D_m z) = E_0(z), so replacing the Hermitian norm by the
  trace account does not break the tie either. [S6-N2]
- **Imaginary-time evolution.** Normalized imaginary-time evolution always
  converges on K^5. Approaching the ground ray within a given error needs
  states of growing account. [S6-N3]

## S7 Stock census

Checked by hand:
- **B1.** 5 c_i^2 <= 4Q, from G^-1 = 2(I + 11^T)/5, whose diagonal is 4/5.
  So [-5,5]^4 is complete for Q <= 32 (and for Q <= 44).
- **T.** T = 1+2a with a = j-j^3; Q(a) = 5, Q(1+a) = 7; w = (2,0,-2,-1,1)
  with sum 0; Q(R_n) = 12 + 5w_(2n mod 5). Readings (22,12,2,7,17), work
  (0,10,20,15,5).
- **S.** Readings (12,7,22,2,17).
- **j^3 S.** j^3 S = 1+2a' with a' = j^3-j^4; Q(a') = 5, Q(1+a') = 7;
  w' = (2,-2,1,0,-1); (Q(R'_1),...,Q(R'_5)) = (17,7,2,12,22). Readings
  (22,2,17,12,7).
- **Accounts.** 26/48 and 30/52.
- **B4.** The rotation rule, by unit covariance.
- **No selection.** Minimizing Q selects no frame.

- **E29 (G).** STOCK-BOUND section 2 leaves out several steps:
  - the formula Q(R_n) = Q(1+a) + Q(a) + Tr((1+a) abar rho^-n);
  - the whole derivation for j^3 S above;
  - B4, which is used before it is stated in section 3; move it ahead of
    (B3) with its one-line proof;
  - that a zero stock never admits, since p stays a unit, so all its
    readings are 0;
  - "undoing that common frame rotation" should read "undoing this
    stock-only rotation by B4".

  The claim that 1+a is nonzero mod 2 plays no role and can be dropped.
  [S7-F3, S7-F5, S8-F6(i,iv,v), S8-F7]
- **E30 (R).** "Equality ... for example (5,2,2,2) has Q=32" presents
  (5,2,2,2) as an equality case. It is not one: 5*25 = 125 < 128 = 4*32.
  Write: "Equality holds at real points with the other coordinates equal
  to c_i/2. The integral near-equality point (5,2,2,2) has Q=32, so the
  cutoff 5 is necessary." [S7-F4, S8-F14]
- **E31 (R).** "A separator constructed by hand before enumeration" and
  "not outputs from an unrecorded search" are stronger than the disclosed
  history. The value 22 and the counts 40/40/40 were first exposed by this
  reviewer's informal enumeration. The derivations are valid whatever their
  origin. State uniformly: "derived by hand before the author's pinned
  census; the value 22 and the level counts were first exposed by an
  informal enumeration (see STOCK-RESULT section 4)". REVIEW-RESPONSE
  section 4 is in a stale tense ("is being specified separately"). Use
  dated, tense-neutral statements. [S7-F6, S7-F7, S8-F10, S8-F11]
- **E32 (W).** "The minimum lexicographic tuple is (-4,-2,-2,-3)" should
  state its key: "the first record in the (Q, stock-tuple) lexicographic
  order". [S8-F8]
- **E33 (W).** The key sentence of STOCK-RESULT section 2 carries no inline
  status marker. Suggested changes:
  - tag it "[C: finite census, complete by the hand bound B1; existence T]";
  - replace "bounded candidate-C" with "finite-decision candidate-C";
  - retitle STOCK-BOUND as a completeness bound plus an exact account-22
    separator.

  [S8-F9]

Note: an independent hand argument confirms the minimum and the level
table. Reviewer S7 derived, without code, that no stock with Q < 22
succeeds, and reproduced {22:40, 28:40, 32:40} and the box table
{22:16, 28:8, 32:8}. The outline:

1. A success must be congruent to some j^c mod 2. Otherwise the stock
   never admits.
2. By B4, X = 1+2a. If a is not in 2O, X succeeds exactly when the five
   cyclic coefficients of (1+a) abar are pairwise distinct. That property
   is Galois-invariant.
3. Q(X) = 2+10F with F in (1/5)Z, so every candidate has Q = 0, 2 or 8 mod 10.
4. Q < 22 leaves 46 values of a, all failing.
5. At Q = 22, exactly the Galois orbits of T and of -1+2j-2j^2 succeed,
   8 per coset, 40 in all.

This is a confirmation of exposed values, not a blind prediction: S7 had
read the target's counts. It removes the minimum's sole dependence on
computation. The owner may add it to STOCK-BOUND. [S7-F2, S8-F15]

## Across documents

- **E34 (W).** The open obligation "prove the complete predictions gauge
  invariant" is ambiguous. Inside the model, invariance under the joint
  transformation is already proved, and fixed-stock predictions are
  provably not invariant. Use the STOCK-RESULT section 3 formulation
  everywhere. That means either an independent law for the relative
  preparation and coupling, or a physical argument that the jointly
  transformed descriptions are equivalent. [S8-F5]
- **E35 (W).** Several symbols are overloaded, and a combined Canon text
  must resolve them:
  - q is a slot, the Canon account and a reading;
  - S is the Canon slot sum, a generic stock and a specific stock;
  - a is redefined for each stock, and a_t = 1+5t also appears;
  - the eigenvalues are lambda_t in one file and alpha_t in another;
  - the target writes Q where the Canon writes q;
  - the equation labels (R1)-(R10) collide with this review's check labels
    R1-R10;
  - RECEIVER-RESULT reports a negative stock Q change, while STOCK-RESULT
    reports positive work released.

  Fix one notation set and one sign convention. [S8-F12]

## What the run can and cannot confirm

review.py re-derives the finite statements frozen in PREREG section 6. It
was written from definitions alone and does not use the target's code. A
pass confirms only those finite statements. The following rest on this
hand review alone:
- Q >= 2 on all of O (E8);
- the obstruction for every nonzero K^5 vector and every W with W^5 = jI
  (S5);
- the dimension-20 commutant as a deduction from the finite rank and
  nullity premises;
- the strict increase of 4 sin^2(pi d/25) on d = 0..12, behind the ground
  mode;
- all interpretive statements.

## Non-binding expectations for the exploratory outputs

PREREG section 7 marks X1 and X2 as exploratory. They are not predicted
there and do not judge the target. The hand argument of S7 nevertheless
gives expectations. They are recorded here, before the run, so that the
comparison is honest. Neither this review nor any in-scope target document
contains computed values of X1 or X2.

- **X1.** Successes occur only at levels Q = 0, 2 or 8 mod 10. So up to
  Q <= 44 the possible levels are 22, 28, 32, 38, 40 and 42. There is none at
  30.
- **X2.** The 120 successes are closed under negation, complex conjugation
  and both Galois maps. They form 12 orbits under U10.

A mismatch here would expose an error in the hand argument, not in the
target. It would be reported as such.

## Relation to the earlier informal check

The coordinator's informal check raised six points earlier. The target
revision at 3d8d364 already addresses four of them:
- **The relative identity.** REVIEW-RESPONSE section 1 now covers it. S4
  confirms it, with E15 and E16.
- **R is not minimal.** STOCK-BOUND and STOCK-RESULT now cover it.
- **The basis argument.** REVIEW-RESPONSE section 3 now covers it. S5
  confirms it, with E24.
- **The "same coupling" wording.** REVIEW-RESPONSE section 2 now stresses
  that the coefficients differ. E28 fixes the remaining phrase in
  RECEIVER-DYNAMICS section 5.

Two points remain partly open. The code-free reviewers raised them again.
They had read REVIEW-RESPONSE.md, which answers the informal comments, so
this is not an independent rediscovery.
- **Embedding dependence.** See E3, E27 and the S6 notes.
- **The 13-tick horizon.** See the S4 note.
