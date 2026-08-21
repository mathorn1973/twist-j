# C-DMATTER-DIRECT-1 RUN RECORD, 2026-07-21

Candidate run record, incubation lane. NO AUTHORITY. Nothing here is canon,
nothing launches a probe, nothing edits PR #113. Consumer: the
P-DMATTER-TOTAL-1 definition pass ("NEXT DEFINITION-ONLY PASS: independent
D_direct").

## Order of operations (discipline)

The candidate doc with the preregistration was written and hashed BEFORE the
verifier was written or executed. Freeze first, compute second. One
implementation-only amendment after a first-run catch, disclosed below with
both pins retained.

## Pins

```
prereg     C-DMATTER-DIRECT-1.md
           sha256 13ab9a03be33a7fdc29e5206e45b9e5d4711a0ab45b063b48d767e7515faf835
           16694 bytes, frozen 2026-07-21T11:53:32Z, before any computation
verifier   verify_dmatter_direct_1.py
           first pin  7272530ecf78702a030a3aa92698671fd2187f50d430cce95454c165a637fa54
                      (run 1: exit 1; three gate fails, all traced to two
                      implementation defects: a dropped window argument in
                      jmul_matrix, and a wrong rational-value extraction in
                      znorm; no gate semantics touched; retained as evidence)
           Amendment 1 (implementation only), accepted verifier
                      0630d82fc45982d64c41dd0403ea3dc5fd5caecd8272606b5881cf9126240ebd
stdout     sha256 bc16079ee7c5f8d5ff72047271186304b742d13ea35ca3ee81d13ec43b723d43
           5998 bytes; three runs, byte identical (runs 2, 3, 4 same hash);
           28 of 29 gates PASS, all 27 core gates PASS, exit 0; runtime
           about 30 s (labeled engineering readout), inside the public
           120 s rule
breaker    break_dmatter_direct_1.py (independent path: trace table only,
           no fractions import, no polynomial multiplication, no matrices)
           sha256 9c23a2919d484f4370260d4190e21c6168e8989f8612c0b78fd77dc861944764
           stdout sha256 cb6b7248e359f1e428f8cbe1c1b66632d451b427871c6b6d6d7aa00d13bfcb2e
           six kill attempts, zero kills
env        LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
platform   TWO ARCHITECTURES, byte identical:
             x86_64  sandbox, Python 3.11.15
             aarch64 second platform, Python 3.12.3
           Both the verifier source and its stdout, and the breaker source
           and its stdout, hash identically on both architectures:
             verifier src    0630d82fc45982d64c41dd0403ea3dc5fd5caecd8272606b5881cf9126240ebd
             verifier stdout bc16079ee7c5f8d5ff72047271186304b742d13ea35ca3ee81d13ec43b723d43
             breaker  src    9c23a2919d484f4370260d4190e21c6168e8989f8612c0b78fd77dc861944764
             breaker  stdout cb6b7248e359f1e428f8cbe1c1b66632d451b427871c6b6d6d7aa00d13bfcb2e
           The two-platform byte identity is met here in the incubation lane
           for candidate strengthening. The PUBLIC two-platform gate still
           stands as the promotion requirement: a pinned public probe branch
           reproduced on the GitHub x86_64 check at PR time, with neutral
           public environment fields (the second-architecture nickname above
           MUST be scrubbed to a neutral descriptor, e.g. Ubuntu aarch64,
           before any public commit).
public     STATUS.md at read time: Public Canon v14 ACTIVE, tag canon-v14,
           CONTENT_COMMIT ab4ea07d15ab1cfa0c403d3c2a74164011ffa0e7, main
           27a68d6, canon/SHA256SUMS 5 of 5 OK
internal   twistj-jam v184 project snapshot, cited at its grades
```

## Result

The #113 STOP item "independent D_direct: publish an independent registered
readout" is ANSWERED at candidate grade. The readout exists, needs zero new
dictionary atoms, and its factorization through the frozen Gram-spectral
candidate is exact on the full carrier.

```
D_direct = the cyclotomic Galois-trace readout of the piston:
  w          = v1 zeta + v2 zeta^2 + v3 zeta^3 + v4 zeta^4 in Z[zeta_5]
               (balanced digits, public CODEC-TR4 power basis, F_5^* window)
  support    = [w = 0]
  total      = (1/5) Tr(w wbar)                  wbar = sigma_4(w)
  branch     = ((4/5) c^2, total - (4/5) c^2)    c = Tr(w)/4, the rational
                                                 component of w in Q + ker(Tr)
  density    = trace-pairing rank-one x -> w (1/5) Tr(x wbar), normalized
```

Defined by field arithmetic only. Not defined through Qcan, N_G, F_Gram, or
any shared factorization helper (#113 Section 5 prohibition respected; the
two implementations share no quadratic code).

## Gates by block (canonical frame unless stated)

```
[A] axiom and frame     N(J) = 1, Tr(J) = 3 by field arithmetic; the axiom
                        step matrix IS multiplication by J; char =
                        Phi_5(x - 1); det(2I - M_J) = 5; the CODEC identity
                        Tr_4(M_J x) = 2 Tr_4(x) - 5 x_c on the basis.
                        Frame scan over all 120 injections: exactly 5
                        verb-compatible (the consecutive cyclic windows);
                        verb-compatibility AND trace alignment (all
                        exponents in F_5^*) select (zeta, zeta^2, zeta^3,
                        zeta^4) UNIQUELY.
[B] carrier and fibers  independent re-derivation of the #113 counts:
                        |image Qcan| = 313 = 1 + 312 sign pairs, zero fiber
                        25, nonzero fibers 50; the balanced section is odd,
                        so checkpoint negation realizes the sign pair.
                        R-echo, no weight: (p^4 - 1)/2 + 1 = 313 = 13^2 +
                        12^2, the CENSUS-313 shape.
[C] factorization       E1 total, E2 branch pair, E3 density (field
                        rank-one == A G entrywise), E4 trace alignment
                        (Tr(w) = -(v1+v2+v3+v4) over Z), split hygiene and
                        tagged-union predicates: ALL EXACT on all 625
                        pistons, hence all 15625 anchored checkpoints.
                        Gram-side identities reproduced on the way:
                        (A G)^2 = m (A G); G (I + 11^T) = I; sharp fixes
                        E_low, E_high; G-spectrum {1/5, 1, 1, 1} with the
                        all-ones trace eigenvector (ALPHA-SEED shape).
[D] injection scan      E1 holds for ALL 120 injections (any four distinct
                        powers carry the same trace Gram 5I - 11^T); E2
                        holds for EXACTLY the 24 F_5^* orderings and fails
                        on all 96 zero-windows; the 24 orderings give
                        identical scalar MatterData (exponent relabeling is
                        exact gauge, the CARRY-PENTAD shape).
[E] controls            WRONG-FACTOR-OMIT-G fires (1/16 vs 1/4 on e_1, the
                        #113 Section 6 pair); the unbalanced section breaks
                        the sign merge (fiber sizes collapse to [25]); the
                        Euclidean total Tr(A) also factors yet differs
                        (fiber constancy alone does not select the Gram;
                        exact normalization does); the sign-sensitive
                        readout does not factor (the fiber test has teeth).
[F] cross-anchors       spectral pair: 4 alpha = v^T G0 v (the sealed v167
                        sum, Gram (5I - 11^T)/2) and alpha^2 - 5 beta^2 =
                        N(w) (the sealed product), exact in Q(sqrt5) on all
                        pistons; ramified collapse v^T G0 v = -(sum v)^2
                        mod 5 with sum v = Tr_4 mod 5 (the CODEC shadow).
[G] completeness        MatterData is constant on Qcan fibers AND separates
                        the 312 nonzero classes (density times total
                        recovers A G; G invertible). The negative-closure
                        clause "two states distinguished by the typed
                        D_matter action have equal Q" is unreachable for
                        this schema.
```

## Fired paths, first class (archived, thresholds not moved)

```
P1b / F-DMATTER-DIRECT-FRAME as frozen: FIRED. The prereg predicted the
CODEC -5-on-slot-3 fingerprint selects one window among the five
verb-compatible ones. False: the fingerprint is a property of the shared
matrix and is window invariant (5 of 5 carry it). By its letter the frozen
frame falsifier fires. The frame selection SURVIVES on the corrected pair
of public clauses, both already in the frozen equation block: verb
compatibility (5 windows) plus trace alignment E4 (all exponents in F_5^*,
so that the piston character Tr_4 equals minus the field trace), unique
intersection (zeta, zeta^2, zeta^3, zeta^4). Recorded, not hidden.

Verifier run 1 (first pin): exit 1 on three gates, all implementation
defects of the fresh code (window argument, rational extraction), caught by
the gates themselves; Amendment 1 changed implementation only; both pins
and the failing run are retained above.
```

## Break attempt (independent code path, zero kills)

```
K1  full 15625 hunt for an E1/E2 counterexample, x20 integer scale,
    trace-table arithmetic: none exists.
K2  hunt for a zero-window injection passing E2 everywhere: all 96 fail
    somewhere; the F_5^* clause is load-bearing, not decorative.
K3  unbalanced section 0..4: the sign merge breaks as predicted; oddness
    ell(-t) = -ell(t) is the load-bearing property of the section.
K4  subset-projector attack: within the combinatorial family of slot
    subsets, only the full slot set reproduces the direct low branch: the
    split is not one of many.
K7  wrong-involution attack: the sigma_2 pairing differs AND goes negative
    (witness v = (0, 0, 0, 1), value -1). Positivity of the Born square
    forces the sigma_4 conjugation, the modulus involution. The dagger
    choice in D_direct is forced, not conventional.
K6  gauge recheck of all 24 orderings by the table path: identical scalar
    data.
```

## Statements earned, candidate grade (public validation pending)

```
candidate-T  FACTORIZATION. D_direct = F_Gram o Qcan o beta exactly, every
             frozen field, all 15625 anchored checkpoints, exact
             normalization included. Core identity: the #113 coordinate
             Gram G0 = 5I - 11^T IS the cyclotomic Galois-trace Gram of
             the piston power basis (Tr(zeta^(a-b)) = 5 delta - 1). This
             closes, at effects level and candidate grade, the identity
             that v184 T-QD-GRAM-PISTON (v172) and Part XXXIX (v177)
             explicitly kept open.
candidate-T  FRAME FORCED. Verb compatibility plus trace alignment select
             the window (zeta, zeta^2, zeta^3, zeta^4) uniquely; exponent
             relabeling is exact gauge (CARRY-PENTAD shape); positivity
             forces the conjugation sigma_4.
candidate-D  PEDIGREE. Every ingredient is published, publicly, for other
             sectors: CODEC-TR4 [T] (power basis, M_J = multiplication by
             J), ALPHA-SEED [T] (the cyclotomic Galois-trace Gram and its
             {1/p, 1, 1, 1} spectrum), MEASURE-SPATIAL-ONLY [T] (trace vs
             spatial split, weights 1/p vs 1), READING-SPLIT [D] (the
             quadratic leg is the Born square), MEASURE-BORN-VERB [D] on
             BORN-FACE-WEIGHTS [T], COUPLINGS-DETERMINE [T] (the Galois
             Gram density), CARRY-PENTAD [T] (exponent gauge). Zero new
             dictionary atoms. Internal seals cited: T-A17-SPECTRAL-PAIR
             (v167; the direct total is (2/5)(m+ + m-)), T-QD-GRAM-PISTON
             (v172), the v177 Gram coupling layer, the sealed signed
             representatives.
candidate-D  FENCE. Matter schema carries modulus-side quadratic fields
             only (polar split: mass is a modulus; phases are
             argument-side, EM); this is what makes Q-fiber constancy
             achievable, and with the density field the schema determines
             Qcan exactly.
```

## Proposed #113 addendum (text offered to the lane, not pushed)

For the residual definition ledger of
notes/canon/P-DMATTER-TOTAL-1-DEFINITION-CANDIDATE.md:

```
| D_direct | PROPOSED: CAND-DIRECT-CYCLOTOMIC-READOUT | adopt public IDs |
```

with the definition block of this candidate's Section 0, the frame clause
(CODEC-TR4 power basis, F_5^* window, verb + trace-alignment selection,
g_a relabeling exact gauge), the measure fence (modulus-side fields only),
and two proposed dependency edges:

```
QUADRATIC-DECODER-DATA -> MEASURE-SPATIAL-ONLY
QUADRATIC-DECODER-DATA -> ALPHA-SEED
```

The future probe P-DMATTER-TOTAL-1 positive route then carries real
content: the factorization equality with exact normalization on all 15625,
two platforms byte identical, closing the registered open identity
"coordinate Gram = cyclotomic Galois-trace Gram" at the effects level.
Still open for READY, untouched by this candidate: the physical measure
dictionary ruling, stage and leg wording, the completion-contract manifests,
and the remaining identifier slots. STOP stands until the lane owner adopts
a definition pass.

## Files

```
claude/C-DMATTER-DIRECT-1.md              prereg (frozen first)
claude/verify_dmatter_direct_1.py         accepted verifier (Amendment 1)
claude/break_dmatter_direct_1.py          breaker (independent path)
claude/C-DMATTER-DIRECT-1_RUN_2026-07-21.md  this record
```

## Public git (a definition note, not a probe)

A concise public definition note was pushed at the author's direction, on a
fresh branch off origin/main, nicknames scrubbed to neutral descriptors,
security audited (no secrets, no private paths, no machine names). It is
non-normative: it answers the #113 routing item "independent D_direct",
changes no Canon object, authorizes no probe, and STOP stands.

```
repo     mathorn1973/twist-j
branch   notes/p-dmatter-total-1-direct-readout
base     origin/main 27a68d6 (Public Canon v14 ACTIVE)
commit   aa28f6dfdb2cd904f5744ef6fc13c28740f2f021
author   A. M. Thorn <thorn@twistj.com> (per POLICY commit identity;
         agent co-author/session trailers omitted to keep the public
         canon surface clean, matching the program's no-internal-fold-
         language rule)
file     notes/canon/P-DMATTER-TOTAL-1-DIRECT-READOUT.md (206 lines)
PR       not opened; the lane owner opens it
         (github.com/mathorn1973/twist-j/pull/new/notes/p-dmatter-total-1-direct-readout)
```

The verifier, breaker, prereg, and run record stay in the incubation lane
(this project and the aarch64 workspace); they enter the public repo only
through the future probe P-DMATTER-TOTAL-1, freshly pinned before execution.
The two-architecture reproduction here is candidate strengthening; the public
two-platform gate (pinned public probe branch reproduced on GitHub x86_64 at
PR time) remains the promotion requirement.

## Disposition after the owner audit (PR #113 commit 50f9189, 2026-07-21)

The owner integrated the usable core of the aa28f6d note into PR #113 as
P-DMATTER-TOTAL-1-CYCLOTOMIC-REALIZATION.md (ALGEBRAIC-LEMMA-ONLY, basis
B0 = (1, zeta, zeta^2, zeta^3), low line = the missing-power line
Q lambda_B, lambda_B = -zeta^4) and audited this candidate's claims. The
disposition, accepted here:

```
STANDS (absorbed)   the candidate-T algebra: trace-Gram identity, branch
                    weights, [T_w] = A G, tags, fibers. Re-audited this
                    session against 50f9189's own B0 formulation:
                    audit_cyclotomic_realization_50f9189.py, sha256
                    8bd9389da73583c8b3ac2aa48b38ad4287b513c855f6274a84d75fbb3205d5e0,
                    8 of 8 exact checks PASS.
DOWNGRADED (agreed) the candidate-D pedigree claims "zero new dictionary
                    atoms" and "independently published readout": the
                    ingredients are public rows, the COMPOSITE
                    checkpoint-to-field-to-record map is not published.
                    The CARRY-PENTAD gauge sourcing is likewise rejected
                    as authority (the computed 24-ordering invariance
                    stands as a computed fact only). R_cyc is a second
                    realization of F_Gram, not a prior D_direct.
RULED (accepted)    the incubation hashes are private exploratory
                    provenance, not public evidence; a future public
                    verifier is a conformance certificate, never an
                    independent selection.
NEW FACT (this      the record R_cyc is WINDOW INVARIANT: all five
session's audit)    verb-compatible readings give identical numbers on
                    every checkpoint, so no finite computation can decide
                    among them; and exactly ONE of the five candidate
                    splits is Galois stable, the rational-line split
                    (missing power 0). The B0 split (low line Q zeta^4)
                    is not Galois equivariant (witness computed). The
                    Route A dictionary therefore has a minimal one-clause
                    form: "the branch split commutes with the cyclotomic
                    Galois action", which selects the rational line
                    uniquely with no basis or window choice.
```

C-DMATTER-DIRECT-1 status after disposition: candidate-T (algebra,
absorbed into #113 at 50f9189); the independence claim reduced to the
owner's Route A / Route B decision; D_direct UNRESOLVED; STOP stands.
