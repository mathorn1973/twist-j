# Synthesis note: F_2 | J | M as the three canonical faces of one ring

**NON-CANONICAL.** Incubation working note, no authority, no Canon change,
no file under `canon/` touched. Companion to `C-RECORD-CRT-IDEMPOTENT-1.md`
in this directory. Paths of the form `C:/j/twist-j-manifest/...` cited below
refer to the author's local working area and are not part of this repository.

**NON-CANONICAL working note, 2026-08-22.** Against Public Canon v60
(tag `canon-v60`). Grades in brackets follow canon conventions; nothing here
changes any status. Origin: owner's synthesis proposal (F_2 = descriptive
minimality, J = dynamic minimality, M = measurable event as the least
understood third object); this note verifies, grades, and extends it.

---

## 1. Verified identities (exact, in Z[x]/Phi_5, Fraction arithmetic)

- `zeta_5 = (J-1)^3`, hence **`Z[J] = Z[zeta_5]`** [T]
- `N(J) = 1` [T] — the step `x -> Jx` is a lattice bijection
- `J = zeta_5 * (zeta_5 + zeta_5^4)` [T] — i.e. `J = zeta_5 / phi` as an
  **exact ring identity** (`zeta*(zeta+zeta^4) = zeta^2 + 1`), not merely an
  archimedean statement
- `J^5 = phi^{-5} = -8 - 5 zeta^2 - 5 zeta^3 != 1` [T]; `J^{5n} = phi^{-5n}`
- local phase closure + global scale non-closure: `zeta_5^5 = 1`, `J^5 != 1`

**Sharpening [T]:** the unit group is `E(Z[zeta_5]) = mu_10 x phi^Z`
(Hasse index Q=1 for prime-power conductor), and since `J = zeta_5 phi^{-1}`
differs from `phi^{-1}` by torsion:

> **J is a fundamental unit of the ring it generates:**
> `Z[J] = Z[zeta_5]` and `E(Z[zeta_5]) = mu_10 x J^Z`.

One element supplies the ring, and generates its motion group modulo phase.
The two components of the owner's reading are exactly the two canonical
factors of E: phase = torsion `mu_10`, scale = free part of rank 1.

## 2. Grading the dynamic-minimality claim

Within the frozen class **prime cyclotomic fields** the claim is an immediate
Dirichlet corollary [T]: `r = (p-3)/2`, so p=3 gives r=0 (phase without
motion), **p=5 gives r=1** (first: nontrivial finite phase + exactly one
infinite unit direction), p>5 gives r>1.

**The relaxation is where it gets interesting.** Drop "prime" and ask for
*any* cyclotomic field with nontrivial phase and unit rank exactly 1:
`r = phi(n)/2 - 1 = 1  <=>  phi(n) = 4  <=>  n in {5, 8, 10, 12}`,
i.e. exactly three fields: **K_5 (= K_10), K_8, K_12** — the full quartic
cyclotomic fields. Then:

| extra condition | survivors | canon row already holding it |
|---|---|---|
| none (rank 1 + phase) | K_5, K_8, K_12 | — |
| totally ramified at one prime | **K_5 (at 5), K_8 (at 2)** | QUARTIC-CYCLOTOMIC-TOTAL-RAMIFICATION-CENSUS [T] |
| minimal absolute discriminant | **K_5** (125 < 144 < 256) | ABELIAN-CM-UNIQUE-EVEN-BIT-DISCRIMINANT-MINIMUM [T] |

So the owner's dynamic-minimality class does not merely re-derive "five": its
natural relaxation **regenerates the two-place structure**.

> **CORRECTED (Rev 3):** the original prose here called K_8 "the runner-up
> solution of the same minimality problem" — wrong. In the discriminant
> ordering of the rank-1 class the runner-up is **K_12** (144 < 256); K_8
> becomes the unique second survivor only inside the narrower
> totally-ramified subclass, exactly as the table above states. Also
> retired: the slogan "why five, thrice" — in the full cyclotomic class the
> rank-1 relaxation is *equivalent to quarticity* (phi(n) = 4), so it is a
> pleasant third reading, not a mathematically independent selector at the
> level of the discriminant minimum. Register modestly as
> CYCLOTOMIC-UNIT-RANK-MINIMALITY: prime case p=5 unique rank-1;
> all-cyclotomic relaxation {K_5, K_8, K_12}.

*Ornament [C]:* the fundamental unit of K_8's real subfield is the silver
ratio `1+sqrt2`; of K_12's, `2+sqrt3`. Golden scale at the write place,
silver scale at the read place.

## 3. F_2 is already inside the axiom's update law

The kernel `U(n, psi) = (n+1, g_(z_6(psi) + 2 theta_n mod 5)(psi))` couples
- `theta_n = s_2(n) mod 2` — binary digit sum, Thue-Morse: an **F_2 object**,
- `z_6(psi) = sum psi_k mod 5` — an **F_5 object**.

The update is literally minimal-description steering minimal-motion: the
owner's `F_2 | J` axis is the canon's `2 | 5` axis (v_2 read / v_5 write),
now with a synthesis name: **2 = distinction, 5 = motion.**

## 4. M: the three canonical faces of one ring

Every commutative ring R carries exactly three "free" structures:

1. **Units E(R)** — reversible motion. Here: `E = mu_10 x J^Z`; phase =
   torsion, scale = free part; r=1 = exactly one scale direction.
2. **Idempotents Idem(R)** — for *any* commutative R, Idem(R) is a Boolean
   algebra (`a AND b = ab`, `a XOR b = a+b-2ab`), i.e. an **F_2-object**, and
   every ring hom preserves it. `x^2 = x` is F_2's defining equation. The
   Boolean face of any record algebra is **functorial — forced, no decoder
   choice.**
3. **Residue/quotient morphisms** — the only maps that lose information.
   The minimal non-unit direction at the write place is `lambda = 1 - zeta_5`
   with `N(lambda) = 5`: minimal information price log 5 per event.
   (`3 - phi = |1 - zeta_5|^2` already sits inside GRAVITY-BRIDGE-LAW's g.
   Independent echo from the owner's PHIBIT emulator programme:
   D-PHIBIT-PROJ-LOCK measured exactly log2(5) bits destroyed per projective
   coupling fire.)

**Claim (synthesis):** F_2 | J | M are not three ad hoc objects; they are
Idem | E | residues — three canonical functors of the single ring Z[J].

> **CORRECTED (Rev 3):** "the three canonical faces of every ring" was
> false as stated — rings carry many other canonical constructions (Spec,
> ideals, modules, K-theory). Correct: three canonical functors *relevant
> to this synthesis*.

Consequences for M:

- > **CORRECTED (Rev 3) — main status error of this note.** The original
  > bullet here said "v60 already proved the Boolean skeleton of the
  > event". Too strong. The public theorem layer proves
  > `COMM-SAT(T) iff Xi_T = 0 iff T = +/-Q iff class(T)^2 = class(T)`
  > — i.e. **[T]: idempotence is the exact algebraic characterization of
  > the saturation class once COMM-SAT is posited.** But functional
  > terminality and read-only output provably do NOT imply COMM-SAT, and
  > **[O]: whether a physically completed event must land in that class is
  > exactly O2a** (whose fence forbids COMM-SAT/idempotence/+-Q/Lueders as
  > construction inputs). The same correction applies to the later
  > "M_when: mathematical answer (idempotence) is already [T]" — the [T]
  > is conditional on COMM-SAT; the physical membership is the open row.
- A **field has only trivial idempotents {0,1}**: a lone J-system carries
  exactly one bit. Nontrivial measurement therefore requires a **composite
  record ring**, whose idempotent decomposition = the context set. The
  22-context carry bank `C_bank = prod_p Z/b_p` is exactly such a product;
  O1's missing "physical context key" is, in this language, *which idempotent
  fires*.
- M therefore splits into three layers:
  - **M_bool** — which Boolean event: *forced* (Idem functor). Simple.
  - **M_when** — when is the event final: O2a. The mathematical answer
    (idempotence) is already [T] — and is *fenced as circular* for O2a's
    physical law.
  - **M_weight** — with what weight, sampled when: Born [D] + O1 + the
    measure rows. **All of v60's remaining openness is concentrated here.**

**Why O2a is hard — the synthesis reading:** the obvious answer ("events are
idempotents") is forced mathematics, and forced mathematics carries no
physical information; the O2a fence (no COMM-SAT / idempotence / Lueders as
construction input) exists precisely because the target theorem already
proved it. So the independent physical law O2a asks for will most likely be
a statement about **weight dynamics** (M_weight), not about the record
algebra (M_bool). In backlog terms: O1 is upstream of O2a not just formally
but semantically.

Measurement is simple in two of its three layers. That is the precise sense
of "the layers under it must be simple": they are — and the entire
difficulty of v60's frontier is the third layer.

## 5. Concrete next moves

1. Freeze the dynamic-minimality class (prime cyclotomic; conditions 1-5)
   and register the Dirichlet corollary as an L1 theorem-row candidate —
   "why five, thrice", alongside the census and the discriminant minimum.
   Standard, cheap, two-architecture verifiable.
2. Register the relaxation table of §2 as the connective tissue between the
   new row and the existing two [T] rows (three separate frozen classes; no
   physical-selection chain claimed, per canon discipline).
3. For the manifest: the Idem language gives `physics_manifest.detector_id`
   and O1's "context key" a typed candidate shape (idempotent decomposition
   of a declared record ring) — a candidate declaration, not a closure; O2a's
   fence must be respected (no idempotence as construction input for the
   physical law).

## 6. The typed signature (owner's formulation) and its consequences

```
F_2   |   (R = Z[J], J in R^x)   |   rho : R -> A_record
                                     M = (ker rho, Idem(A_record), mu)
```

Of the three data of M, only mu is free:

1. **ker rho is classified, not chosen.** Kernels range over Spec Z[J].
   Two are distinguished without choice: (a) minimal norm — the norm ladder
   is 5 < 11 < 16 < ... (only 5 ramifies, disc 125), so the globally
   cheapest kernel is lambda = (1 - zeta_5), N = 5, record F_5 (write side,
   price log 5); (b) the unique F_2-algebra record — 2 is inert
   (ord_5(2) = 4), so (2) is the only prime of residue characteristic 2,
   record F_16 = F_2^4 (read side; J-STEP Z^4 mod 2). The two places of
   TWO-PLACE-PHYSICS drop out as the two canonical solutions of "minimal
   record".
2. **Each minimal record reads exactly one component of J** (verified
   exactly): mod lambda the phase dies (zeta == 1) and J == 2 cycles
   {2,4,3,1} in F_5^x (pure scale, order 4); mod 2 the phase survives
   exactly (ord(zeta) = 5), the scale folds to order 3, and J has order
   15 — **J is a primitive root of F_16^x**. The archimedean projection
   dictionary (modulus -> gravity, argument -> EM) has non-archimedean
   twins: two minimal kernels, one projection each.
3. **The record closes what the motion does not.** J^15 == 1 mod 2: the
   non-closing helix closes in every single finite record; global scale
   non-closure is invisible to any one record and appears only in event
   counts over time — which is why D_clock / ObservableHistory must be
   separate types and why mu cannot be a property of one record but a
   measure over events.
4. **Nontrivial Idem requires a composite modulus.** A one-prime record is
   a field (one bit). Apparatus: rho : R -> R/m = prod R/p_i^{e_i} (CRT),
   Idem = F_2^k, contexts = the prime decomposition of the record modulus.
   An event is a localization at one factor; O1's missing "context key" =
   which prime the dynamics selects; mu is typed as a measure on Spec Z[J]
   (Born square as its registered candidate density [D]). The 22-context
   carry bank prod Z/b_p has exactly this shape.

Consequence for the forced-decoder question: the decoder has no freedom at
rho or Idem (classified/functorial); the entire decision is concentrated
in mu. The owner's formula is the type signature of
physics_manifest + measure_manifest.

> **SUPERSEDED (see section 7):** "only mu is free" was an overclaim — the
> free data are four (which I, tau, orientation bit, mu); "mod lambda reads
> the scale" was wrong wording (both finite positions are torsion; scale is
> archimedean-only); "event = localization" should be "projection onto one
> CRT factor via a primitive idempotent"; "(2) = the K_8 read place" is a
> conflation of two distinct binary objects pending a bridge; "non-closure
> visible only in event counts" ignores quotient towers (TIME-QUANTUM-TOWER
> [C]). Section 7 is the settled form.

## 7. Settled form (owner's recon 2026-08-22, 19/19 + 23/23 PASS) + the pentad lock

Owner's corrections, all accepted and independently re-verified here
(ord_5(3)=4 so 3 is inert; Phi_7 mod 2 = two cubics so Z[zeta_7]/2 = F_8 x F_8;
(1+i)^2 = 2i = 0 in Z[i]/2 so nilpotent; |sigma_{1,4}(J)| = phi^-1,
|sigma_{2,3}(J)| = phi — modulus constant on conjugate pairs; Frobenius is a
single 4-orbit on the roots in F_16; |R/(6)| = 1296 with r=2;
|R/(10)| = 10^4):

**Three positions, not two.** lambda reads the modulus projection *as torsion
of order 4* (J-bar = 2, the CARRY-PENTAD carry token) and kills the phase;
(2) reads the phase exactly (order 5) and folds the scale to order 3
(J-bar primitive, order 15); **scale, positivity, contraction |J| = phi^-1
and entropy 2 log phi live only at the archimedean position.** Both finite
positions are torsion — provable, not merely tested: every finite quotient
has a finite unit group, so falsifier F1 can never fire and row 2d can be
retired to a proof. Likewise F4: R/(2) is a field iff ord_5(2)=4 — proof,
not test.

**Four free data, not one.**

```
which I     the apparatus (classification != selection; Spec is a catalog)
tau         event-completion law (M_when; [H] candidate: nilpotent
            filtration sqrt(I)/I — write has thickness, read has none)
orientation C_2 torsor {sigma_2, sigma_3}; invisible at lambda (GAUGE
            residue collapse (X-2)^4) and at (2) (single Frobenius orbit),
            free archimedean (trivialized only by the choice of i)
mu          measure on the atomic outputs of the CHOSEN apparatus
            (mu_I on Supp(I) first; a global measure on Spec R would need
            a compatible family {mu_I} — extra step, not automatic)
```

Forced once I is chosen: Supp(I) = atomic channels, Idem(R/I) = F_2^r
(= Idem(R/sqrt I)), thicknesses (e_i). Settled headline (owner's):
**algebra freely determines the structure of outcomes once physics
determines what is read; physics must still supply what is lost (I),
when the event completes (tau), and with what weight (mu).**
Signature M = (I, tau, mu), B_I forced. Atomic event = projection onto one
CRT factor via a primitive idempotent (NOT "localization").

**Reading-position paradox (theorem):** both minimal kernels give fields —
one channel, zero Boolean resolution. Neither is an apparatus; they are
extreme points of the catalog. An apparatus needs a composite modulus.
In the rational-conductor class: smallest two-channel record m = 6
(F_16 x F_81); smallest carrying both distinguished positions m = 10
(F_16 x R/lambda^4, |.| = 10^4). Sharpening in the ideal class: the
two-channel minimum is lambda p_11 (norm 55), and lambda(2) (norm 80,
F_5 x F_16) carries both distinguished positions with zero thickness —
thickness is part of the freedom in I, not forced by carrying both places.

**The C-CARRY-PENTAD-1 lock** (frozen 2026-07-19, a8585761 in the internal
line = C:\j\jam; read 2026-08-22; rev2, 18 gates OK, one platform, guards
G1-G4). The freeze already contains, from the other direction:

- (PIN) det(2I - M_J) = N(2 - J) = 5 — i.e. lambda | (2 - J): **J == 2 mod
  lambda is pinned there as the exact ramification witness.** The owner's
  identification "write position = carry position" (J-bar = 2 = the carry
  token) is a registered join, not an analogy.
- (GAUGE)+G1 is the provenance of the orientation bit: the power in I + c^k
  is a gauge class under the isometries of the carry geometry; the mod-5
  channel is blind ((X-2)^4) — the same lambda-blindness as row 2 of the
  position table; the archimedean modulus cuts the four powers into the
  conjugate pairs {1,4} | {2,3}; the residual choice within a pair is the
  C_2 torsor. Falsifier F2 overlaps the freeze's own falsifier list
  ("a residue-channel invariant distinguishing two powers").
- The chain carry bit -> pentad -> S_5 -> Phi_5 -> I + c^2 ~ M_J gives the
  **derivation arrow F_2 -> J** (up to gauge, conditional on the width gate
  G2, with the +1 step form by hand, O-STEP-FORM): the description side
  generates the motion side's characteristic packet. Neither prior note had
  this arrow. Its guards also bound the synthesis: no unconditional p=5
  derivation, no physics lift (G4).
- G3's remark (the +1 buys infinite order, hyperbolic 2+2 split, entropy
  2 ln phi) is the archimedean row of the position table, sealed earlier.

**Status labels (owner's):** candidate-T: position table, r(m), r(2)=1,
thicknesses, Arf-1 transfer. candidate-D: write/read/scale as three
positions. [H]: tau in the nilpotent filtration. [O]: which I per
apparatus; mu. Falsifiers F1-F4 hold (F1, F4 retire-able to proofs).
Sober note stands: filtration length 4 (e = 4, total ramification) and
ord_5(2) = 4 (2 primitive root mod 5) are both four for different reasons —
coincidence until a proof joins them. Before any candidate is drafted,
C-CARRY-PENTAD-1 must be cited as the frozen predecessor (its scope
overlaps P2/S5/BRIDGE/PIN); the synthesis adds the three-position table,
the M = (I, tau, mu) type, r(m)/thickness structure, the J-specificity
comparisons (Z[i]/2, Z[zeta_7]/2), and the Dirichlet rank-1 minimality
with its relaxation table.

## 8. Coarse-graining addendum (owner's closing remark, 2026-08-22)

Owner: measurement = finding invariants; the coarse-graining rule is
fundamental — the same mathematics as magnetism and the phases of water,
over three-dimensional space.

Three anchors:

1. **The ledger already agrees on where this lives.** In the manifest
   draft, `coarse_graining_id` is the ONE unresolved top-level scalar, and
   its owner is METRO-REDUCTION-CALCULUS [O] — independently identified in
   R4 as the single deepest formal choke point (rows 4, 7, 8 and the NEG
   branch of MINIMAL-READ-DERIVATION all quantify over the equivalence it
   must define). The physical intuition and the formal backlog point at the
   same slot.
2. **Ising is the existence proof for the whole strategy.** The 3D Ising
   model is literally an F_2 theory over three-dimensional space, and its
   coarse-graining flow produces continuum critical physics shared by
   uniaxial magnets and the liquid-gas transition of water — one fixed
   point, one universality class, determined by (symmetry, dimension)
   alone, with every microscopic detail irrelevant. Discrete substrate ->
   continuum reading is therefore not a category error; it is the
   best-understood mechanism in statistical physics. J already carries the
   RG skeleton: the hyperbolic 2+2 eigenvalue split (phi expanding,
   phi^-1 contracting; entropy 2 ln phi) is a relevant/irrelevant
   decomposition, and "measurement = invariants" = what survives the
   quotient tower (TIME-QUANTUM-TOWER [C] is such a tower statement).
3. **The forced-decoder question in RG language.** METRO-REDUCTION-CALCULUS
   defines the arrows (admissible reductions); decoder classes are basins;
   FORCED / SEVERAL / EMPTY = exactly one / several / no fixed point of the
   coarse-graining flow in the frozen class. Same trichotomy, physical
   dress.

Fence: the canon has no continuum limit anywhere and ENTROPY-RG-RETURN
explicitly disclaims a scaling theorem — this section is strategy [H], not
result. Where d=3 is already registered: 3 = C(3,2) spatial 2-planes
(FRW-CANONICAL-FORM), G_nat = 27 = d^3, w = -1 + 1/(dp) with d=3, and
color su(3) on the three-dimensional trace kernel.

## 9. Rev 3 — owner's authority-checked revision applied (2026-08-22)

Owner re-verified the public basis (STATUS.md ACTIVE, canon-v60, content
commit ancestor of main, SHA matches SHA256SUMS, PR #520 two-architecture
PASS) and revised this note without writing to the repo. All corrections
accepted; the marked blocks in sections 2 and 4 carry the two hard errors
(K_12 vs K_8 runner-up; the O2a status error). Settled state:

**Theorem-grade center of the synthesis (owner's priority 2, freeze first):**
RECORD-CRT-IDEMPOTENT-STRUCTURE [T-candidate]. For R = Z[zeta_5] and
I = prod p_i^{e_i} with r = |Supp(I)|:

```
R/I ~= prod R/p_i^{e_i}            (each factor LOCAL, not nec. a field)
Idem(R/I) ~= F_2^r ~= Idem(R/sqrt I)
```

Sharp split: **Supp(I) forces the Boolean algebra of outcomes; the
exponents (e_i) carry the thickness and are invisible to the Boolean
layer** — which is exactly where the tau hypothesis (nilpotent filtration)
can live without touching B_I. Corrected local statement: |Supp(I)| = 1
implies |Idem| = 2 even when R/p^e is not a field. Minima (all verified):
rational conductor m = 6 (F_16 x F_81, |R/(6)| = 6^4 = 1296); ideal-class
two-channel support lambda p_11, N = 55; smallest square-free ideal
carrying both distinguished finite positions lambda(2), N = 80,
R/I ~= F_5 x F_16. Precision: B_I determines the SPACE of possible Boolean
events, not which event occurs — atom selection remains dynamical.

**Type M, inconsistency resolved:** the orientation bit is moved OUT of M
into the reading convention — the public manifest already carries
`read_convention_id` as a separate top-level slot, and the {sigma_2,
sigma_3} choice is a property of the archimedean embedding convention
unless an apparatus is shown to select it. Settled signature:

```
M = (I, tau, mu_I),        B_I = Idem(R/I) forced.
```

**Position names de-physicalized (candidate-D stays separate):** ramified
residue position lambda / binary residue position (2) / archimedean
position. Only the dictionary may later name them write/read/scale.

**Public predecessor authority corrected:** for PUBLIC work the
predecessors are the v60 rows CARRY-PENTAD [T] (REGISTRY row 232: pentad,
O(q) = S_5, I+C^2 integrally conjugate to M_J, all I+C^a read as 2, "with
order five fixed, four is..."), J-BINARY-NORM-DESCENT [T] (row 16:
O_5/(2) ~= F_16, q_2 = q_+ mod 2 = Tr_(F_4/F_2) o N_(F_16/F_4), singular
locus mu_5, A4/2A4 ~= O_5/2O_5 isometry, transport to the pentad form) and
CARRY-QUADRATIC-SYMMETRY [T] (row 15). The internal freeze C-CARRY-PENTAD-1
(a8585761) remains origin-of-idea only, not predecessor authority; and
section 7's claim that the F_2 -> J arrow "was not there" is too strong
against v60 — the public theorem rows already contain its substantial part.
Standing guard: CARRY-PENTAD [T] itself does not unconditionally select
the prime 5, the cycle, the exponent, or a physical reading; the synthesis
must not route around that.

**Coarse-graining downgraded to precise [H]:** METRO-REDUCTION-CALCULUS is
a system of admissible reduction arrows, transports, and an intended
equivalence — not yet an RG flow; RG relevant/irrelevant directions are
eigenvalues of the linearized RG transformation at a fixed point in
interaction space, so the 2+2 spectral split of M_J may not yet be labeled
RG directions (structural analogy [H]). Ising phrasing corrected: not
"literally an F_2 theory" (Gibbs weights and RG are not F_2 arithmetic)
but: a binary discrete microstate can have a universal continuous
macroscopic critical reading; Ising universality does cover simple liquids
at the liquid-gas critical point.

**Owner's priority order:**
1. CYCLOTOMIC-UNIT-RANK-MINIMALITY [T-candidate], modest form.
2. RECORD-CRT-IDEMPOTENT-STRUCTURE [T-candidate] — **priority; the
   biggest new advance of this note** — plus the purely arithmetic
   three-position table as candidate-T, the write/read/scale reading as
   candidate-D.
3. tau from the nilpotent filtration + RG/METRO reading [H, NON-CANONICAL]
   — valuable precisely because it uses neither COMM-SAT nor idempotence
   as input; must predict something independent and attach to a physically
   chosen I, else it does not cross the O2a fence.

**Settled headline (replaces "three faces"):**

> J determines reversible arithmetic motion; I determines the loss;
> Supp(I) forces the Boolean algebra of outcomes; (e_i) carry the
> thickness; mu_I remains physics.

Less poetic, harder, and it localizes exactly what is already theorem and
where the physics still lies.
