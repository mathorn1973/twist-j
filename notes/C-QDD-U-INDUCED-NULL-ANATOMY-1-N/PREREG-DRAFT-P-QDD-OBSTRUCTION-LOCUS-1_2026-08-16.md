# PREREG DRAFT P-QDD-OBSTRUCTION-LOCUS-1

NON-CANONICAL DRAFT, revision 2, rebuilt after the owner STOP verdict on
revision 1. Incubation-lane preregistration. This file is not a public probe,
holds no probe identity, and earns nothing. No verifier exists and no formal
gate has run. Sealing requires, in this order: pull request #396 accepted so
that the result commit is on `main`, owner ANO on blocks B1 to B6 below, a fresh
public claim-lock issue, a fresh branch `probe/P-QDD-OBSTRUCTION-LOCUS-1`, and
the accepted `PREREG.md` plus the accepted `verify.py` pushed and read back from
the public remote before the first execution.

```text
CANDIDATE   P-QDD-OBSTRUCTION-LOCUS-1
DATE        2026-08-16
BASIS       Public Canon v49, STATE ACTIVE, AUTHORITY mathorn1973/twist-j main,
            TAG canon-v49,
            CONTENT_COMMIT dc80228522a4ccb9495550dfbef8ba73b33b2157,
            CANON_SHA256 d456c42575375774200b08dafc3b4225643f526f5f1826292f1255f39d332f9e,
            CANON_BYTES 237233
PRIOR       P-QDD-INSTRUMENT-U-INDUCED-1, claim lock #395, pull request #396
            preregistration commit 84888d086dff15b59c88fa69ff9a840761cfd082
            verifier pin commit    45cad3384c69d7f2e187d88e63c10ecbad965f0d
            RESULT COMMIT          7df6a605fdff4b5b8a82981795e7d22168d0a081
              path  probes/P-QDD-INSTRUMENT-U-INDUCED-1/EXPECTED.txt
              bytes 3441
              sha256 652baf70e75600fa80fb685c36435b19cdaae6e8f519e207e0d0a646bb7f5d5c
              blob  46f7fd3fcaa223de342657e1aba7ec8dbc7f6ccc
TARGET ROW  QDD-INSTRUMENT-APPARATUS [O], blockers O1 and O2
```

The verifier pin carries the verifier, not the result file. Gate D7 pins the
result commit above, not `45cad3...`.

## Mandatory result-exposure disclosure

This is a **result-exposed localization probe**. It is designed after the
complete published output of `P-QDD-INSTRUMENT-U-INDUCED-1`, it exists because
of that output, and it is not an independent confirmation of anything. It
cannot earn a discovery status and does not ask for one.

Exposure is declared exactly:

- every count and tag of the prior `EXPECTED.txt` is known to the author;
- the static class decomposition of D1 (42 LOW-zero, 2 HIGH-zero, 268
  both-positive) was computed before this draft by `null_anatomy.py` in this
  directory and is published in the companion note;
- the bound `POS-REALIZED-SINGLE <= 38`, and the pigeonhole statement that at
  least 862 of the 900 pairs already fail inside the positive sector on `W`,
  were derived before this draft from the published `SEED-DEPENDENT-271350` and
  are published in the companion note. D3 is therefore partly a confirmatory
  gate against a bound already known, and the bound is preregistered below as a
  hard ceiling whose violation is an implementation failure;
- the positive-sector denominator multiset and the sum 19688 were computed
  before this draft from the Canon target law and are published in the
  companion note;
- no reachable residue set, no visited-class multiset, no restricted count and
  no cause split has been computed by anyone at the time of writing;
- the formal execution count of the future accepted verifier is zero.

## Questions

Revision 1 asked whether the null is carried by the zero-target sector alone.
That hypothesis is refuted by the published `SEED-DEPENDENT-271350`. What
remains is a co-occurrence question and two localization questions:

```text
Q1  Z-SUFFICIENT   is the zero-target sector by itself enough to eliminate all
                   900 pairs, on W and on W2, even though at least 862 pairs
                   also fail inside the positive sector?
Q2  where exactly does the positive-sector failure live: which pairs, which
    classes, and is it seed dependence, an empty branch, a ZERO post, or the
    denominator arithmetic of Q3?
Q3  how much of the positive-sector failure is forced by the exact-rational
    predicate meeting the window length, independently of U?
```

## Design principle

The construction does not change. `U`, the split, `beta`, `cls`, `R`, `D`, both
windows, both seed sets and the frozen target are reused verbatim from the
sealed preregistration. What changes is the granularity of the report and the
addition of two measurements the sealed probe did not take, the reachable
residue sets and the per-seed visited-class multiset. Any disagreement with an
overlapping sealed count is an ARCH-STOP, not a finding.

## Field 1: equation

Sections 1.1 to 1.7 of `P-QDD-INSTRUMENT-U-INDUCED-1` are imported unchanged and
are not restated. The following are added.

### 1a. Zero-target decomposition (block B1, owner ANO given)

```text
Z_LOW  = { nonzero c : w_low(c)  = 0 }     expected |Z_LOW|  = 42
Z_HIGH = { nonzero c : w_high(c) = 0 }     expected |Z_HIGH| = 2
POS    = { nonzero c : w_low(c) > 0 and w_high(c) > 0 }   expected |POS| = 268
Z = Z_LOW union Z_HIGH, disjoint, |Z| = 44, |Z| + |POS| = 312
```

Identifiers follow the frozen lexicographic numbering of the sealed section 1.2.
Complete identifier lists are printed. The decomposition is determined by the
frozen target alone and by no count.

### 1b. Cause split of the strict post tag, resolved by sector (block B2)

Revision 1 split the merged tag into three causes but left `U1` and `U2`
sector-blind, so a fired `U1` or `U2` could have come from the positive branch
of a zero-target class and would not have implied any positive-sector defect.
The split is therefore taken over sector as well:

```text
U1_Z(rho,d)    a visited positive-target branch of a class in Z has no event
U1_POS(rho,d)  a visited branch of a class in POS has no event
U2_Z(rho,d)    a visited positive-target branch of a class in Z has a ZERO post
U2_POS(rho,d)  a visited branch of a class in POS has a ZERO post
U3(rho,d)      some event occurs on a zero-target branch
```

On window `W` the disjunction
`U1_Z or U1_POS or U2_Z or U2_POS or U3` is audited equal, pair by pair, to the
sealed `POST-UNDEFINED-OR-ZERO`. The report gives the count of pairs for each
of the 31 nonempty subsets of the five indicators.

On window `W2` the same five indicators are computed and reported, but they are
labelled as a **new diagnostic output**. The sealed probe published no strict
post partition on `W2`, so no `W2` cause count may be compared with the sealed
tag and none may be presented as a re-derivation.

### 1c. Restriction to the positive sector (block B3)

```text
REAL-POS-CLASS   as REAL-CLASS but quantified only over c in POS
REAL-POS-ORIENT  as REAL-ORIENT but only over the pre-cells of POS
REAL-POS = REAL-POS-CLASS and REAL-POS-ORIENT, exact equality in Q
REAL-POS-SINGLE / REAL-POS-LONG / REAL-POS-CENSUS as in the sealed 1.7
FUNCTIONAL-POS       FUNCTIONAL with the pre-class domain restricted to POS
ORIENT-COHERENT-POS  orientation coherence restricted to POS
POST-PARTITION-POS   the strict partition restricted to POS
```

The four are reported separately; they are not collapsed into one verdict.

The restriction applies to the quantifier domain only. No count is re-weighted,
no class is merged, and no target value is touched. The restricting set is the
zero set of the frozen target law and is computable before any count, so it is
not selection by performance. It is nonetheless a result-informed restriction of
a sealed quantifier, which is why this carries a fresh probe identity.

Seed dependence is decomposed by sector, which is the measurement that says how
far the published aggregate is from the pigeonhole bound:

```text
SEED-DEP-ZERO-k   seed-dependent triples with c = ZERO
SEED-DEP-Z-k      seed-dependent triples with c in Z
SEED-DEP-POS-k    seed-dependent triples with c in POS
audit: the three sum to the sealed SEED-DEPENDENT-271350
```

**Preregistered ceiling.** From the sealed counts,
`281700 - 271350 = 10350` triples are seed independent, and a pair satisfying
`REAL-POS-SINGLE` needs all 268 of its positive triples seed independent, so

```text
POS-REALIZED-SINGLE <= floor(10350 / 268) = 38.
```

A measured `POS-REALIZED-SINGLE > 38` contradicts a published count and is an
implementation failure of this probe, not a discovery. It routes to ARCH-STOP.

### 1d. Exact zero-target avoidance and the U3 image (block B4)

Revision 1 used `Reach = F_5` as the obstruction test. That is sufficient but
not necessary, so it is withdrawn as a criterion and `REACH-FULL` is withdrawn
as a falsifier. The exact criterion is used instead. For each window, each
`lambda` in `Lambda_0` and each delay `d`, over the census of that window:

```text
Reach(lambda, d, c) = { lambda(f(x_(k+d))) : k in window, cls(x_k) = c }
A(lambda, d) = union of Reach(lambda, d, c) over c in Z_HIGH
B(lambda, d) = union of Reach(lambda, d, c) over c in Z_LOW
```

A subset `S` avoids every zero-target event exactly when

```text
A(lambda, d) subset S    and    S disjoint from B(lambda, d),
```

so admissible masks exist exactly when `A` and `B` are disjoint, and they are
then exactly the `S` with `A subset S subset F_5 \ B`, intersected with the 30
nonempty proper subsets. The verifier prints, per window and per `(lambda, d)`,
the sets `A` and `B`, the admissible mask list, and derives from them the exact
900-bit image of `U3`. On `W` that image is audited against the `U3` indicator
computed independently in 1b; a mismatch is ARCH-STOP.

This gate is mandatory on both `W` and `W2`. Both windows are already traversed
for D3 and D7, so retaining five bits of reachable residues per
`(window, lambda, d, c)` is neither a second pass nor a material cost.

### 1e. Static integrity items (block B5, demoted)

The information-locus vector is `(0, 0, 150, 0, 0, 0)` and is already determined
by the published pair list, so it is result-exposed and is not a decision gate.
The separate closure of the piston half `S` and the fiber half `s = q + r`, and
the recovery of the `KERNEL-Z6-SYNCHRONIZATION` sheet table from the two
one-dimensional maps, are static L1 structure belonging to the archive. Both are
retained only inside D0 and D7 as integrity checks and appear nowhere in the
routing of Field 5.

### 1f. Denominator feasibility (block B6, NEW, no owner ruling yet)

This block is not covered by the rulings on revision 1 and is proposed here for
a separate decision. It may be adopted, deferred or dropped without affecting
B1 to B5.

Write the frozen target rate of a positive class in lowest terms `p_c / q_c`.
Since `L_c` and `N_c` are integers with `gcd(p_c, q_c) = 1`, exact equality
forces `q_c | N_c`, hence `N_c >= q_c` whenever the class is visited. Each step
of a window lies in exactly one class, so for every seed and every pair:

```text
sum of q_c over the VISITED positive classes  <=  |window|.
```

Statically, `sum of q_c over all 268 positive classes = 19688`, while
`|W| = 1536` and `|W2| = 14336`, so at most 107 respectively 245 positive
classes can be visited by a realizing seed. The measurement is the per-seed
visited-class multiset:

```text
VISIT-INFEASIBLE-W-k   seeds whose visited positive denominators exceed 1536
VISIT-INFEASIBLE-W2-k  the same on W2 over the 625 ready-fiber seeds
UNDERVISITED-k         triples (seed, class) with 0 < N_c < q_c, c in POS
FEASIBLE-SEEDS-W       the complete list of seeds that pass the inequality
```

The visit histogram is already formed for the counts of the sealed 1.6, so this
block adds a comparison rather than a traversal.

## Field 2: code

One accepted verifier, `probes/P-QDD-OBSTRUCTION-LOCUS-1/verify.py`, to be
written and frozen with the accepted preregistration and pushed before any
execution.

```text
Python standard library only
integers and Fraction only; no float, no Decimal, no external dataset
deterministic enumeration order identical to the sealed probe
stdout: gate lines, every count of Field 5, and the same six labelled table
  hashes plus root hash as the sealed probe
```

The verifier reimplements the traversal rather than importing the sealed
`verify.py`, so the cross-check of D7 is a genuine second implementation. The
memory discipline, packed-lane layout and 32-bit cell bounds of the sealed code
section are carried over unchanged. The reachable-residue store is five bits per
`(window, lambda, d, c)` over `c in Z`, and the visited-class comparison of 1f
reads the existing histogram.

## Field 3: carrier or data

No external data.

```text
autonomous carrier   Omega = N_0 x F_5^6, U as registered in Canon v49
system carrier       V_eff subset (Q^4, G) via beta
pointer carrier      F_5^2, read only through R
target objects       E_low, E_high, m, w_low, w_high, dens, occ, unchanged
prior evidence       the EXPECTED.txt of the result commit pinned above,
                     used only as the cross-check target of D7
```

## Field 4: systematics and completeness

There is no measurement systematic. Gates:

```text
D0  generators, relations, sheet commutators, 313 classes, 25 ZERO checkpoints,
    22 occurrence values, the separate closure of S and s, and the recovery of
    the sheet table from the two one-dimensional maps, all reproduce exactly
D1  the decomposition 42 / 2 / 268 reproduces; Z_LOW and Z_HIGH disjoint; m > 0
    on every nonzero class; complete identifier lists printed
D2  the five sector-resolved causes of 1b evaluated for all 900 pairs on W and
    on W2; the 31 subset counts printed per window; on W the disjunction is
    audited equal to the sealed strict tag pair by pair; the W2 counts are
    labelled as new output and compared with nothing
D3  REAL-POS-SINGLE, REAL-POS-LONG, REAL-POS-CENSUS, FUNCTIONAL-POS,
    ORIENT-COHERENT-POS and POST-PARTITION-POS evaluated for all 900 pairs and
    reported separately with full pair lists; SEED-DEP-ZERO, SEED-DEP-Z and
    SEED-DEP-POS printed and audited to sum to 271350; the ceiling
    POS-REALIZED-SINGLE <= 38 checked
D5  A, B, the admissible mask lists and the exact 900-bit U3 image printed for
    every (window, lambda, d); on W the image audited against the independent
    U3 indicator of D2
D6  block B6 if adopted: VISIT-INFEASIBLE-W, VISIT-INFEASIBLE-W2,
    UNDERVISITED and the feasible-seed list printed
D7  every quantity overlapping the pinned result commit reproduces exactly:
    records=180, pairs=900, INFO true=150 with locus vector (0,0,150,0,0,0),
    the three NO-REALIZATION counts, functional=0, orient_coherent=0,
    pure_strict=0, mixed=0, undefined_or_zero=900, zero_input_multivalued=900,
    seed_triples=271350, orientation_triples=22500, both channel witnesses,
    the six labelled table hashes and the root hash
```

Any hidden input, floating tolerance, post hoc restriction of `R x D`, any
restriction of the class domain other than the one defined by the zero set of
the frozen target law in 1a, comparison of a `W2` cause count with the sealed
`W` tag, or an unnamed layer lift is STOP.

## Field 5: failure threshold and scientific routing

No tolerance exists.

```text
ARCH-STOP
  D0, D1 or D7 fails; or the D2 disjunction disagrees with the sealed tag on
  any pair on W; or the D5 image disagrees with the D2 indicator on W; or
  POS-REALIZED-SINGLE exceeds 38. Any of these voids the diagnostic entirely.
  None of them reopens the sealed probe and none becomes a finding.

U3-IMAGE-k               pairs with U3 true, per window
Z-SUFFICIENT-YES / NO    whether U3 holds for all 900 pairs, per window
U-CAUSE-<subset>-k       the 31 subset counts of D2, per window
POS-REALIZED-k           pairs satisfying REAL-POS-SINGLE
POS-LONG-REALIZED-k      pairs satisfying REAL-POS-LONG
POS-FUNCTIONAL-k         pairs satisfying FUNCTIONAL-POS
POS-ORIENT-COHERENT-k
POS-POST-<tag>-k         the restricted strict partition
SEED-DEP-ZERO/Z/POS-k    the sector decomposition of the sealed C8 count
ADMISSIBLE-MASKS         per (window, lambda, d), possibly empty
VISIT-INFEASIBLE-W/W2-k  block B6 if adopted
UNDERVISITED-k           block B6 if adopted
```

Falsifiers:

```text
F1  Z-SUFFICIENT-NO on W
      the zero-target sector alone does not eliminate all 900 pairs, so the
      published null strictly requires the positive-sector obstruction as well.
F2  POS-REALIZED-0 with POS-FUNCTIONAL-0
      the positive sector is obstructed on every pair. Together with the
      established bound this is the expected outcome and is not news by itself;
      what it earns is the exact locus printed alongside it.
F3  POS-REALIZED-k with 0 < k <= 38
      at least one pair reproduces the occurrence law on the whole positive
      sector. This earns nothing by itself, since the zero-target sector remains
      unrealized and the pair is still not an instrument, but it is a materially
      different reading of the sealed null and routes to a separate owner
      decision.
F4  SEED-DEP-POS below the pigeonhole minimum 230850
      arithmetic contradiction with the sealed count; ARCH-STOP, not a finding.
F5  block B6 adopted and VISIT-INFEASIBLE-W-15625
      every seed violates the denominator inequality on W, so REAL-POS-SINGLE
      was arithmetically unreachable on that window independently of U. This is
      the strongest available statement that the frozen construction, not the
      registered update, carries the null.
```

Scientific routing, fixed before any pin:

- No outcome closes `QDD-INSTRUMENT-APPARATUS [O]` in either direction, and no
  outcome moves O1 or O2. `SAMPLING NOT PROVIDED` remains the only sampling
  statement.
- `Z-SUFFICIENT-YES` on both windows plus `F2` records that the frozen
  construction carries at least two independent sufficient obstructions. That is
  an argument about the construction, not about `U`, and its only consequence is
  that a further search inside this class is unjustified until a frozen choice
  changes.
- `F1` records that the zero-target sector is not independently sufficient, so
  the positive-sector obstruction is load bearing. Combined with the published
  seed dependence this is the first constraint this lane produces on the
  registered coupling at the frozen split, and it earns at most a finite-window
  classification statement, candidate grade C at a later reviewed fold.
- `F5`, if B6 is adopted and fires, subordinates both of the above: it says the
  realization predicate is unreachable on the frozen window for arithmetic
  reasons, and the correct next owner decision is about the predicate, not about
  the record class.
- Every routing above is a statement about a frozen finite construction. None is
  a limit theorem and none is an L6 claim.

The threshold and scope may not move after the pin.

## Field 6: action layer

```text
L1  exact autonomous dynamics, the split closure, and the static arithmetic of
    the target law including the denominator multiset
L4  induced apparatus classification on the frozen split, restricted and
    unrestricted
L5  finite-window realized-event stream, exact counts, reachable residue sets
    and visit histograms, both windows
L6  none: no normalized measure, no limit, no SI statement
```

## Scope firewall

This diagnostic does not:

- close `QDD-INSTRUMENT-APPARATUS [O]` in either direction, or move O1 or O2;
- modify `QUADRATIC-DECODER-DATA [O]` or any `DEF-QDD-*` definition;
- choose or alter a coupling: `U` is the registered update, unchanged;
- alter the record class, the delays, the windows, the seeds or the target;
- select any `(rho, d)` before the complete enumeration is reported;
- reopen, amend, rename or resume the sealed probe;
- present any `W2` quantity as a re-derivation of a sealed `W` quantity;
- assert a limit, an L6 measure, or a sampling construction;
- adopt or recommend any exit E1 to E5 of the companion note;
- fill any field of the decoder completion contract;
- introduce a new free dimensionless input.

## Blocks awaiting owner ANO

```text
B1  zero-target decomposition and its use as the restriction domain   ANO given
B2  sector-resolved cause split, W2 causes as new output              rebuilt
B3  restricted predicates, seed-dependence decomposition, ceiling 38  rebuilt
B4  exact avoidance criterion, admissible masks, U3 image, W and W2   rebuilt
B5  static integrity items demoted into D0 and D7                     demoted
B6  denominator feasibility against window length                     NEW
```

B6 is the only block with no ruling. It is the cheapest gate in the draft and,
if it fires, the most consequential, because it would move the open question
from the record class to the realization predicate. It is written so that
dropping it leaves B1 to B5 intact.
