# PREREG. P-METRO-FORBIDDEN-WITNESSES-1

Preregistration frozen before any gate execution in this repository. Public
probe under `POLICY.md` and `AGENTS.md`, which govern over this file wherever
they differ.

Obligation B of `METRO-REDUCTION-CALCULUS [O]`: exact witnesses for the five
forbidden transformations named in `canon/CANON.md` section 15. The probe
supplies the witnesses and the census. It does not close the parent, which
stays `[O]` and `STOP` until obligations D and E also fall.

## Falsifier, first

```text
fires if the pinned evidence bundle or exact stdout differs, any of the twelve
frozen gates fails, any named witness fails to reproduce its stated pair of
positions, any exhibited obstruction is shown to be an admitted arrow under its
own exact precondition, any admitted arrow is shown to produce a functional
obstruction on either frozen box, any census count is shown to be over a domain
other than the declared 21987 tuples, or an output transport tau is exhibited
that intertwines any one of the five transformations on its own witness; a
different reading of a forbidden entry is outside this scope and is not a
counterexample
```

Operationally: any pinned gate FAIL on rerun kills the probe. A fired
falsifier is merged and archived, never hidden, and the threshold never moves
afterwards.

## Public identity, authority, and action layer

```text
probe:           P-METRO-FORBIDDEN-WITNESSES-1
probe owner:     A. M. Thorn / delegated session metro-probe-2026-08-20
branch:          probe/P-METRO-FORBIDDEN-WITNESSES-1
basis:           Public Canon v56, main 612806b, tag canon-v56,
                 CONTENT_COMMIT b36c93ed, CANON_SHA256 b284ed6e,
                 CANON_BYTES 288492, canon/SHA256SUMS 5 of 5 OK,
                 verified by fresh fetch on 2026-08-20
action layer:    L1 formal, on L5 stream objects. No L6, no cross-layer gate,
                 no layer lift, no physical or SI claim, no canon edit by this
                 probe.
lineage:         carries in the incubation promotion
                 PROMO-C-METRO-FORBIDDEN-WITNESSES-4 (2026-08-20). The
                 provenance of every file is declared below rather than
                 implied.
```

## The owner ruling this probe stands on

The five phrases section 15 names as forbidden are normative text whose
meaning was not fixed. The owner has ratified one reading per phrase as the
canonical meaning. That ruling is a decision about the meaning of existing
normative text, not a new scientific claim, and it is what makes obligation B
testable at all.

The decisive argument, recorded because it constrains every reading: section
15 fixes four admitted arrows and immediately names five forbidden
operations, and the parent carries a sharp negative falsifier, so a
transformation that were both admitted and forbidden would falsify
`METRO-REDUCTION-CALCULUS` negatively. Each phrase is therefore read
minimally and typewise, never rhetorically broadly.

```text
flattening the N^a geometry
    RATIFIED  loss of the named product structure N^a: several coordinates
              replaced by a single ordering without preserving their typed
              roles.
    OPERATIONAL  iota(n) = n_1 + ... + n_a; the stream must factor through the
              total-degree index.
    NOT FORBIDDEN  a faithful encoding that transports the whole coordinate
              structure.

erasing named coordinate digit-word actions
    RATIFIED  forgetting which coordinate a D_i(v_i) or delta_(i,u) belongs
              to.
    OPERATIONAL  the stream must be determined by the unordered multiset of
              digit maps, forgetting the (coordinate,digit) name of each.
    NOT FORBIDDEN  a permutation of coordinates that transports the names,
              input bases, maps and boxes with it. That permutation is
              admitted arrow 4 and is explicitly allowed.

arbitrary factor weights
    RATIFIED  introducing new arbitrary relative weights of the geometry
              factors or of the box reading.
    OPERATIONAL  the joint stream must be determined by the per-coordinate
              values ( w(delta_(1,n_1)(s)), w(delta_(2,n_2)(s)) ) ALONE, with
              the start state not in the key.
    NOT FORBIDDEN  general exact rational transport of the output, tau_R, or
              typed transport of w. Reading it more broadly would extend the
              prohibition past the definition of a reduction arrow.

output-dependent regrouping
    RATIFIED  changing the grouping of inputs, factors, boxes or trajectories
              according to output already obtained.
    OPERATIONAL  quotient of S by the level sets of w alone, with no
              delta-stability precondition.
    NOT FORBIDDEN  the Nerode quotient. It uses w(delta_v(s)) in its
              equivalence, but section 15 lists it as admitted arrow 3 under
              the congruence precondition. The broader reading would create
              exactly the forbidden allowed-and-forbidden contradiction.

replacing boxes by an unrelated ordering
    RATIFIED  discarding the canonical box geometry and substituting an
              independent ordering.
    OPERATIONAL  the coordinate acting first is chosen per input rather than
              by one fixed permutation transported with the digit maps; frozen
              as reversal of the order at every input.
    NOT FORBIDDEN  box transport induced by an admitted coordinate
              permutation. This entry does not address q^k blocking, which
              section 15 leaves as the separate open obligation D.
```

The ruling was given against Public Canon v55. The five phrases are unchanged
at v56, byte for byte, and this probe checks that before it computes: the
sentence naming them occurs once in `canon/CANON.md` at the pinned basis.

## The six fields

```text
EQUATION     for the typed L5 U_RF tuple P = (q,a,r,S,A0,{delta_(i,u)},enc_q,w)
             at q = 2, a = 2, r = 1, A0 = S, single-digit inputs, and
             coordinate 1 acting first, so that
                 Stream_P(s,n) = w( delta_(2,n_2)( delta_(1,n_1)(s) ) ),
             a transformation T with declared start transport sigma and index
             transport iota is ADMISSIBLE only if some map tau on output
             values satisfies
                 Stream_(T(P))(sigma(s), iota(n)) = tau( Stream_P(s,n) )
             for every s in A0 and every n, and a FUNCTIONAL OBSTRUCTION for T
             on P is an explicit pair of positions
                 (s,n), (t,m)  with  Stream_P(s,n) = Stream_P(t,m)
                     and Stream_(T(P))(sigma(s),iota(n))
                         != Stream_(T(P))(sigma(t),iota(m)).
             Such a pair excludes every tau at once, linear or otherwise; it is
             the non-descent idiom the Canon already uses in
             QPAIR-HERM-INTEGER-NONDESCENT. CLAIM: each of the five forbidden
             entries named in section 15, under the ratified readings above,
             admits an exact functional obstruction, so none of the five is an
             admissible arrow.
CODE         probes/P-METRO-FORBIDDEN-WITNESSES-1/verify.py, Python standard
             library only, integers and Fraction, no float in any assertion,
             deterministic, no randomness, no file access, no network, no
             clock, no seed, working-directory free, under 120 s, run from
             repository root with LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1
             PYTHONHASHSEED=0 TZ=UTC.
CARRIER      the section 15 U_RF typing and the coordinate-1-first composition
             convention, verbatim; METRO-REDUCTION-ARROWS [C] for the four
             admitted arrows and their exact preconditions, used only as a
             control. Two frozen boxes, declared in full below.
SYSTEMATICS  the five witnesses, the census counts, the commuting-tuple count
             and the T3b subset count were computed in the incubation lane and
             are declared here in advance; they bind this run. The two boxes
             are declared exhaustively below and every reported count is over
             the same 21987 tuples, which gate G10 enforces. The verifier is
             carried in from the incubation lane rather than rewritten, and
             the independent code path is supplied by the breaker instead; see
             Provenance. Witnesses W1 to W5 need not lie in either box: they
             are hand-checkable exhibits, the boxes are the census domain.
THRESHOLD    any gate FAIL kills the probe. Exact equality only, no tolerance,
             no float comparison anywhere.
LAYER        L1 formal on L5 stream objects. No L6. No cross-layer gate. No
             lift. The parent stays O and STOP.
```

## The two frozen boxes, declared exhaustively

```text
BOX-2   |S| = 2, A0 = S, all four digit maps free, output alphabet {0,1,2}:
        delta_(1,0), delta_(1,1), delta_(2,0), delta_(2,1) range over all
        4 maps S -> S, and w ranges over all 9 maps S -> {0,1,2}.
        4^4 x 3^2 = 2304 tuples.
BOX-3   |S| = 3, A0 = S, zero-digit maps fixed to the identity, output
        alphabet {0,1,2}: delta_(1,0) = delta_(2,0) = id, delta_(1,1) and
        delta_(2,1) range over all 27 maps S -> S, and w ranges over all 27
        maps S -> {0,1,2}.
        27 x 27 x 27 = 19683 tuples.
TOTAL   2304 + 19683 = 21987 tuples. Every census count is over this domain.
```

## Declared expected values, frozen before execution

```text
BOX-2 tuples                 2304
BOX-3 tuples                 19683
obstructing tuples of 21987  T1 flattening        16140
                             T2 erasing names     18666
                             T3a factor weights   12702
                             T3b anchored variant  9288  (disclosed subset)
                             T4 output regrouping  9072
                             T5 box reordering    13116
admitted arrows              relabel 0, restrict 0, Nerode 0 with 21987
                             applicable, coordinate permutation 0 on the 4329
                             commuting tuples
report R1                    13320 non-commuting tuples on which a transported
                             coordinate swap breaks the pointwise stream;
                             reported, not gated, and not a claim about the
                             closed row METRO-REDUCTION-ARROWS [C]
named witnesses              W1 (0,(0,1)) and (0,(1,0)) 2 vs 1;
                             W2 redistribution (0,1,3,2) at (1,(0,0)) 1 vs 0;
                             W3 (0,(1,1)) and (1,(0,0)) 2 vs 1;
                             W4 (0,(1,0)) and (1,(1,0)) 0 vs 1;
                             W5 (0,(0,1)) and (0,(1,1)) 0 vs 1
RESULT                       12/12 ALL PASS, exit 0, empty stderr
```

## Provenance, declared rather than implied

```text
verify.py     carried in from the incubation lane verifier of
              PROMO-C-METRO-FORBIDDEN-WITNESSES-4, with exactly two
              non-semantic edits: the two header lines now name this probe and
              the owner ratification, and stdout is written through an
              explicit LF reconfiguration. No gate, box, reading, witness or
              count was changed. This is deliberate: the census numbers the
              proposed row carries are the numbers this code produces, so
              rewriting it would replace the package rather than validate it.
breaker       written fresh for this probe, sharing no routine with verify.py:
              a different tuple encoding, a different obstruction search, an
              independent re-implementation of both boxes and of all six
              census counts, and an exhaustive tau search. That is where the
              independent code path lives, and it is reported in RESULT.md
              whether it agrees or not.
PREREG.md     written fresh for this probe.
```

## Proposed fold edits (a later sealed fold, not this probe)

The owner has ratified the five readings, so the CANONICAL branch applies.
Exact texts are frozen in `FOLD-ROWS.tsv` and `FOLD-EDITS.md` beside this
file. Ledger delta: claims +1, C +1. Frontier: no list item is added, because
a C row is not live and `tools/check_canon.py` rejects a closed claim at the
head of a frontier list item.

```text
new row       METRO-FORBIDDEN-WITNESSES [C], canon section 15, evidence
              probes/P-METRO-FORBIDDEN-WITNESSES-1
parent row    METRO-REDUCTION-CALCULUS [O] keeps its status, its STOP state
              and its falsifier. Only the obligation B clause of its scope
              changes, in REGISTRY.tsv and in FRONTIER.md identically, to
              record that the five readings are the ratified meaning of the
              five phrases and that B is discharged for those five entries
              while any further entry stays open.
canon prose   one new paragraph in section 15 between the
              METRO-REDUCTION-ARROWS paragraph and the
              METRO-REDUCTION-CALCULUS paragraph, plus the matching clause
              replacement in the parent paragraph.
```

Traps verified against the pinned basis, all three anchors present exactly
once: the section string, the parent clause in `REGISTRY.tsv` and
`FRONTIER.md`, and the parent paragraph clause in `CANON.md`. The candidate id
of the incubation lane is never written into any hashed canon file, because
`tools/check_canon.py` would read it as a status-C token for an unregistered
claim.

## Non-claims

```text
The parent is not closed. Obligations D and E are untouched and
METRO-REDUCTION-CALCULUS stays O and STOP. Discharging B for five entries is
not closing the row and no summary may say otherwise.

No completeness claim is made about the forbidden catalogue itself. The five
entries are the five the Canon names. Whether that list is complete is not
addressed.

No claim is made at |S| > 4, q > 2, a > 2, r > 1, or for multi-digit words.
No blocking, normalization, decision, terminal-value, L6, cross-layer,
physical or SI claim is made. Common q^k blocking is obligation D and is not
touched.

METRO-REDUCTION-ARROWS [C] is used only as a control and does not move. The
R1 report about a transported coordinate swap on non-commuting tuples is
recorded and deliberately not gated: it is a question about a closed row and
this probe will not move a closed row by a side effect. If it needs settling,
that is its own probe with its own preregistration.

The status is C, not T. The five named obstructions are individually
hand-checkable and would carry T on their own, but the row also carries a
census over a finite box, which is computation at a declared finite range. A
later fold may lift the existential clause alone under its own named gate.
```
