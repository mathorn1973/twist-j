# PREREG DRAFT P-QDD-OBSTRUCTION-LOCUS-1

NON-CANONICAL DRAFT, revision 3, rebuilt after two owner verdicts. Incubation-lane
preregistration. This file is not a public probe, holds no probe identity, and
earns nothing. No verifier exists and no formal gate has run. Sealing requires,
in this order: pull request #396 accepted so the result commit is on `main`,
owner ANO on blocks B1 to B6 below, a fresh public claim-lock issue, a fresh
branch `probe/P-QDD-OBSTRUCTION-LOCUS-1`, and the accepted `PREREG.md` plus the
accepted `verify.py` pushed and read back from the public remote before the
first execution.

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
result commit above, not `45cad33...`.

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
- the bound `POS-REALIZED-SINGLE <= 38`, and the statement that at least 862 of
  the 900 pairs already fail inside the positive sector on `W`, were derived
  before this draft from the published `SEED-DEPENDENT-271350`. Its two
  derivations are algebraically equivalent readings of that one count and are
  not independent evidence. D3 is therefore partly a confirmatory gate against
  a bound already known, and the bound is preregistered below as a hard ceiling
  whose violation is an implementation failure;
- the positive-sector denominator multiset, the sum 19688, the minimum
  denominator 6 and the visit caps 107 / 245 / 138 / 401 were computed before
  this draft from the Canon target law and the two window lengths, and are
  published in the companion note;
- no reachable residue set, no visit count, no divisibility outcome, no
  restricted count and no cause split has been computed by anyone at the time
  of writing;
- the formal execution count of the future accepted verifier is zero.

## Questions

Revision 1 asked whether the null is carried by the zero-target sector alone.
That hypothesis is refuted by the published `SEED-DEPENDENT-271350`. What
remains:

```text
Q1  Z-SUFFICIENT   is the zero-target event indicator U3 by itself enough to
                   eliminate all 900 pairs, on each window separately?
Q2  where exactly does the positive-sector failure live: which pairs, which
    classes and orientations, and by which of the frozen causes?
Q3  is the U-induced visit histogram integer-compatible with exact REAL at all,
    per class and per orientation, on each window and on the census aggregate?
```

`Z-SUFFICIENT-NO` may be reported only as "`U3` alone does not suffice". It may
not be reported as "the `Z` sector does not suffice", because `Z` also obstructs
through the empty-branch and ZERO-post causes on its own positive-target
branches.

## Design principle

The construction does not change. `U`, the split, `beta`, `cls`, `R`, `D`, both
windows, both seed domains and the frozen target are reused verbatim from the
sealed preregistration. What changes is the granularity of the report and the
addition of two measurements the sealed probe did not take: the reachable
residue sets and the visit counts with their divisibility. Any disagreement with
an overlapping sealed count is an ARCH-STOP, not a finding.

## Window discipline

Two regimes are carried throughout and are never merged, never renamed into each
other, and never compared across:

```text
REGIME-W    window [512, 2048),   seed domain all 15625 seeds
REGIME-W2   window [2048, 16384), seed domain the 625 ready-fiber seeds S2
REGIME-CEN  the seed sum of the REGIME-W counts; a control sharing window W,
            with its own aggregate integers and therefore its own divisibility
```

Every tag in Field 5 carries its regime suffix. The sealed probe published a
strict post partition on `W` only, so only `REGIME-W` quantities may be compared
with sealed tags; `REGIME-W2` quantities are new output and are compared with
nothing external. Each regime gets its own `U3` cross-check, independently, and
the two cross-checks are reported separately.

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

```text
U1_Z    a visited positive-target branch of a class in Z has no event
U1_POS  a visited branch of a class in POS has no event
U2_Z    a visited positive-target branch of a class in Z has a ZERO post
U2_POS  a visited branch of a class in POS has a ZERO post
U3      some event occurs on a zero-target branch
```

The five indicators define a partition of the 900 pairs into **32 exact cells**,
the 31 nonempty subsets together with the cell `NONE` in which no indicator
fires. All 32 counts are printed per regime. `NONE` is expected empty on
`REGIME-W`, since the sealed strict tag fired on every pair there, and that
expectation is audited; `NONE` may be populated on `REGIME-W2` and its
population is a reportable result, not an error.

On `REGIME-W` the disjunction of the five indicators is audited equal, pair by
pair, to the sealed `POST-UNDEFINED-OR-ZERO`.

### 1c. Restriction to the positive sector (block B3)

```text
REAL-POS-CLASS   as REAL-CLASS but quantified only over c in POS
REAL-POS-ORIENT  as REAL-ORIENT but only over the pre-cells of POS
REAL-POS = REAL-POS-CLASS and REAL-POS-ORIENT, exact equality in Q
FUNCTIONAL-POS       FUNCTIONAL with the pre-class domain restricted to POS
ORIENT-COHERENT-POS  orientation coherence restricted to POS
POST-PARTITION-POS   the strict partition restricted to POS
```

The four are reported separately per regime; they are not collapsed into one
verdict. The restriction applies to the quantifier domain only. No count is
re-weighted, no class is merged, and no target value is touched. The restricting
set is the zero set of the frozen target law, computable before any count, so it
is not selection by performance; it is nonetheless a result-informed restriction
of a sealed quantifier, which is why this carries a fresh probe identity.

Seed dependence is decomposed by sector:

```text
SEED-DEP-ZERO-k   seed-dependent triples with c = ZERO
SEED-DEP-Z-k      seed-dependent triples with c in Z
SEED-DEP-POS-k    seed-dependent triples with c in POS
audit: the three sum to the sealed SEED-DEPENDENT-271350
```

**Preregistered ceiling.** `281700 - 271350 = 10350` triples are seed
independent, and a pair satisfying `REAL-POS-SINGLE` needs all 268 of its
positive triples seed independent, so `POS-REALIZED-SINGLE-W <= 38`. A measured
value above 38 contradicts a published count and is an implementation failure,
routed to ARCH-STOP.

### 1d. Exact zero-target avoidance and the U3 image (block B4)

`Reach = F_5` is sufficient for failure but not necessary, so it is withdrawn as
a criterion and `REACH-FULL` is withdrawn as a falsifier. For each regime, each
`lambda` in `Lambda_0` and each delay `d`, over that regime's census:

```text
Reach(lambda, d, c) = { lambda(f(x_(k+d))) : k in window, cls(x_k) = c }
A(lambda, d) = union of Reach(lambda, d, c) over c in Z_HIGH
B(lambda, d) = union of Reach(lambda, d, c) over c in Z_LOW
```

A subset `S` avoids every zero-target event exactly when `A subset S` and `S`
disjoint from `B`. Since `S` must also be one of the 30 nonempty proper subsets,
an admissible `S` exists only when

```text
A disjoint from B,   A != F_5,   B != F_5
```

and these three conditions are printed explicitly. The verifier does **not**
reason from the conditions: it normatively enumerates the 30 masks `1..30` and
keeps exactly those satisfying both containments, so the empty, full and
degenerate cases are handled by construction rather than by argument. The
printed admissible mask list, possibly empty, and the sets `A` and `B` are the
gate output; from them the exact 900-bit image of `U3` is derived and printed.

Per regime, that derived image is audited against the `U3` indicator computed
independently in 1b. The two cross-checks, one per regime, are separate gates
and are reported separately.

### 1e. Static integrity items (block B5, demoted)

The information-locus vector is `(0, 0, 150, 0, 0, 0)`, already determined by the
published pair list, so it is result-exposed and is not a decision gate. The
separate closure of the piston half `S` and the fiber half `s = q + r`, and the
recovery of the `KERNEL-Z6-SYNCHRONIZATION` sheet table from the two
one-dimensional maps, are static L1 structure. All three are retained only
inside D0 and D7 as integrity checks and appear nowhere in the routing.

### 1f. Divisibility of the visit counts (block B6, NEW, no owner ruling yet)

Write the frozen target rate of a positive class in lowest terms `p_c / q_c`.
`REAL` requires `L / N = p_c / q_c` with `L`, `N` integers and
`gcd(p_c, q_c) = 1`, so `q_c` divides `N`. `REAL-ORIENT` carries the same
equality per orientation, so the requirement holds for oriented pre-cells as
well as for classes.

**Normative gate.**

```text
DIV-FAIL(seed, regime)  there exists a positive class c, or a positive oriented
                        pre-cell (c, eps), with N > 0 and N mod q_c != 0
```

evaluated over classes and over orientations, separately in `REGIME-W`,
`REGIME-W2` and `REGIME-CEN`; the census aggregate has its own summed integers
and its divisibility is tested on those, never inherited.

**Why one seed is enough.** `N` depends on the seed and the window only, never
on the record map or the delay. If `DIV-FAIL` holds for one seed of a regime,
then no integer `L` can produce the target rate for that seed, and
`REAL-POS-SINGLE`, being universally quantified over seeds, fails for every one
of the 900 pairs of that regime. The falsifier below is therefore existential;
it must not demand all 15625 seeds.

**Reported quantities.**

```text
DIV-FAIL-SEEDS-<regime>-k       seeds exhibiting at least one indivisibility
DIV-FAIL-FIRST-<regime>         the lexicographically first witness, printed as
                                (seed, class, orientation, N, q_c)
DIV-FAIL-CELLS-<regime>-k       distinct (class, orientation) cells implicated
UNDERVISITED-<regime>-k         cells with 0 < N < q_c, a weaker certificate
VISIT-BUDGET-<regime>-k         seeds whose visited positive denominators sum
                                above the window length, a weaker certificate
```

**Reading.** If the gate fires, the conclusion is not "independently of `U`":
the visit histogram is produced by `U`. It is that the `U`-induced visit
histogram is integer-incompatible with exact `REAL` already before the record
map and the delay are chosen. If the gate does not fire, nothing positive
follows: absence of an indivisibility licenses no conclusion about
realizability. The gate is one-sided by construction.

The weaker certificates are retained for reporting only. `sum of q_c over the
visited positive classes <= |window|` bounds how many positive classes a
realizing seed may visit, at most 107 of 268 on `W` and 245 on `W2`, and at most
138 respectively 401 of the 536 positive oriented pre-cells. It does not make
`REAL-POS` unreachable, because `REAL` quantifies only over visited classes and
does not require the sector to be covered.

The visit histogram is already formed for the counts of the sealed 1.6, so this
block adds comparisons rather than a traversal.

## Field 2: code

One accepted verifier, `probes/P-QDD-OBSTRUCTION-LOCUS-1/verify.py`, to be
written and frozen with the accepted preregistration and pushed before any
execution.

```text
Python standard library only
integers and Fraction only; no float, no Decimal, no external dataset
deterministic enumeration order identical to the sealed probe
stdout: gate lines, every count of Field 5 with its regime suffix, and the same
  six labelled table hashes plus root hash as the sealed probe
```

The verifier reimplements the traversal rather than importing the sealed
`verify.py`, so the cross-check of D7 is a genuine second implementation. The
memory discipline, packed-lane layout and 32-bit cell bounds of the sealed code
section are carried over unchanged. The reachable-residue store is five bits per
`(regime, lambda, d, c)` over `c in Z`; the divisibility test reads the existing
visit histogram.

## Field 3: carrier or data

No external data.

```text
autonomous carrier   Omega = N_0 x F_5^6, U as registered in Canon v49
system carrier       V_eff subset (Q^4, G) via beta
pointer carrier      F_5^2, read only through R
target objects       E_low, E_high, m, w_low, w_high, dens, occ, unchanged
prior evidence       the EXPECTED.txt of the result commit pinned above,
                     read as specified in D7 and used only as a cross-check
```

## Field 4: systematics and completeness

There is no measurement systematic. Gates:

```text
D0  generators, relations, sheet commutators, 313 classes, 25 ZERO checkpoints,
    22 occurrence values, the separate closure of S and s, and the recovery of
    the sheet table from the two one-dimensional maps, all reproduce exactly
D1  the decomposition 42 / 2 / 268 reproduces; Z_LOW and Z_HIGH disjoint; m > 0
    on every nonzero class; complete identifier lists and the per-class
    denominators q_c printed
D2  the five sector-resolved causes evaluated for all 900 pairs in each regime;
    all 32 cell counts printed per regime, NONE included; on REGIME-W the
    disjunction audited equal to the sealed strict tag pair by pair, and NONE
    audited empty there
D3  REAL-POS, FUNCTIONAL-POS, ORIENT-COHERENT-POS and POST-PARTITION-POS
    evaluated for all 900 pairs in each regime and reported separately with
    full pair lists; SEED-DEP-ZERO, SEED-DEP-Z, SEED-DEP-POS printed and
    audited to sum to 271350; the ceiling POS-REALIZED-SINGLE-W <= 38 checked
D4  block B6: DIV-FAIL evaluated over classes and orientations in REGIME-W,
    REGIME-W2 and REGIME-CEN; seed counts, first witness, implicated cells,
    UNDERVISITED and VISIT-BUDGET printed per regime
D5  A, B, the three existence conditions, the enumerated admissible mask list
    over masks 1..30, and the exact 900-bit U3 image printed per regime; the
    image audited against the independent U3 indicator of D2, once per regime,
    as two separately reported cross-checks
D7  the pinned result commit is read as an immutable blob: the verifier resolves
    the recorded blob id 46f7fd3f..., confirms its SHA-256 and 3441 bytes,
    confirms the result commit is an ancestor of the branch under test, and
    parses the file under an exact frozen grammar (one record per line, ASCII,
    LF terminated, fields split on single spaces, tags matched literally, no
    regular expression accepting a superset). Comparison is on the canonical
    serialization of the parsed records, not on formatted text. Every
    overlapping quantity reproduces exactly: records=180, pairs=900,
    INFO true=150 with locus vector (0,0,150,0,0,0), the three NO-REALIZATION
    counts, functional=0, orient_coherent=0, pure_strict=0, mixed=0,
    undefined_or_zero=900, zero_input_multivalued=900, seed_triples=271350,
    orientation_triples=22500, both channel witnesses, the six labelled table
    hashes and the root hash
```

Any hidden input, floating tolerance, post hoc restriction of `R x D`, any
restriction of the class domain other than the one defined by the zero set of
the frozen target law in 1a, any comparison of a `REGIME-W2` quantity with a
sealed `W` quantity, any inheritance of a divisibility verdict between regimes,
or an unnamed layer lift is STOP.

## Field 5: failure threshold and scientific routing

No tolerance exists. Every tag below carries its regime suffix.

```text
ARCH-STOP
  D0, D1 or D7 fails; or the D2 disjunction disagrees with the sealed tag on
  any pair in REGIME-W; or NONE is nonempty in REGIME-W; or a D5 image
  disagrees with its regime's D2 indicator; or POS-REALIZED-SINGLE-W exceeds
  38; or SEED-DEP-POS falls below 230850. Any of these voids the diagnostic
  entirely. None reopens the sealed probe and none becomes a finding.

U3-IMAGE-<regime>-k
Z-SUFFICIENT-<regime>-YES/NO   whether U3 holds for all 900 pairs of that regime
U-CAUSE-<regime>-<cell>-k      the 32 cell counts
POS-REALIZED-<regime>-k
POS-FUNCTIONAL-<regime>-k
POS-ORIENT-COHERENT-<regime>-k
POS-POST-<regime>-<tag>-k
SEED-DEP-ZERO/Z/POS-k
ADMISSIBLE-MASKS-<regime>      per (lambda, d), possibly empty
DIV-FAIL-SEEDS-<regime>-k      block B6
DIV-FAIL-FIRST-<regime>        block B6
UNDERVISITED-<regime>-k        block B6, weak certificate
VISIT-BUDGET-<regime>-k        block B6, weak certificate
```

Falsifiers:

```text
F1  Z-SUFFICIENT-<regime>-NO
      the zero-target event indicator alone does not eliminate all 900 pairs of
      that regime. It says nothing about whether the Z sector as a whole
      suffices, since Z also obstructs through U1_Z and U2_Z.
F2  POS-REALIZED-<regime>-0 with POS-FUNCTIONAL-<regime>-0
      the positive sector is obstructed on every pair of that regime. On
      REGIME-W this is the expected outcome given the established bound; what
      it earns is the exact locus printed alongside it.
F3  POS-REALIZED-W-k with 0 < k <= 38
      at least one pair reproduces the occurrence law on the whole positive
      sector. It earns nothing by itself, since the zero-target sector remains
      unrealized, but it is a materially different reading and routes to a
      separate owner decision.
F4  SEED-DEP-POS below 230850, or the three sector counts not summing to
      271350
      arithmetic contradiction with the sealed count; ARCH-STOP, not a finding.
F5  block B6 adopted and DIV-FAIL-SEEDS-<regime>-k with k >= 1
      at least one seed of that regime has a visited positive class or oriented
      pre-cell whose visit count is not divisible by its target denominator.
      Then REAL-POS-SINGLE fails for every one of the 900 pairs of that regime,
      and the statement earned is: the U-induced visit histogram of that regime
      is integer-incompatible with exact REAL before the record map and the
      delay are chosen. F5 is existential and must not be written to require
      all seeds.
F6  block B6 adopted and DIV-FAIL-SEEDS-<regime>-0
      no indivisibility found in that regime. Nothing positive follows; the
      gate is one-sided and this outcome licenses no claim of realizability.
```

Scientific routing, fixed before any pin:

- No outcome closes `QDD-INSTRUMENT-APPARATUS [O]` in either direction, and no
  outcome moves O1 or O2. `SAMPLING NOT PROVIDED` remains the only sampling
  statement.
- `Z-SUFFICIENT-YES` in both regimes together with `F2` records that the frozen
  construction carries at least two independent sufficient obstructions. That is
  an argument about the construction, not about `U`, and its consequence is that
  a further search inside this class is unjustified until a frozen choice
  changes.
- `F1` records that `U3` alone is not sufficient in that regime, so the
  positive-sector obstruction is load bearing there. Combined with the published
  seed dependence this is the first constraint this lane produces on the
  registered coupling at the frozen split, and it earns at most a finite-window
  classification statement, candidate grade C at a later reviewed fold.
- `F5`, if B6 is adopted and fires, subordinates the record-class question in
  that regime: the correct next owner decision is then about the realization
  predicate, not about the record map. It is regime-local; firing in `REGIME-W`
  says nothing about `REGIME-W2` and vice versa.
- Every routing above is a statement about a frozen finite construction. None is
  a limit theorem and none is an L6 claim.

The threshold and scope may not move after the pin.

## Field 6: action layer

```text
L1  exact autonomous dynamics, the split closure, and the static arithmetic of
    the target law including the denominator multiset
L4  induced apparatus classification on the frozen split, restricted and
    unrestricted
L5  finite-window realized-event stream, exact counts, reachable residue sets,
    visit histograms and their divisibility, both regimes and the census
L6  none: no normalized measure, no limit, no SI statement
```

## Scope firewall

This diagnostic does not:

- close `QDD-INSTRUMENT-APPARATUS [O]` in either direction, or move O1 or O2;
- modify `QUADRATIC-DECODER-DATA [O]` or any `DEF-QDD-*` definition;
- choose or alter a coupling: `U` is the registered update, unchanged;
- alter the record class, the delays, the windows, the seed domains or the
  target;
- select any `(rho, d)` before the complete enumeration is reported;
- reopen, amend, rename or resume the sealed probe;
- present any `REGIME-W2` quantity as a re-derivation of a sealed `W` quantity,
  or inherit any verdict between regimes;
- read a positive realizability conclusion out of an absent divisibility
  failure;
- assert a limit, an L6 measure, or a sampling construction;
- adopt or recommend any exit E1 to E5 of the companion note;
- fill any field of the decoder completion contract;
- introduce a new free dimensionless input.

## Blocks awaiting owner ANO

```text
B1  zero-target decomposition as the restriction domain           ANO given
B2  sector-resolved cause split, 32 cells with NONE, per regime   rebuilt r3
B3  restricted predicates, seed-dependence decomposition, ceiling rebuilt r2
B4  existence conditions plus normative enumeration of masks 1-30 rebuilt r3
B5  static items demoted into D0 and D7                           demoted r2
B6  divisibility gate on the visit counts, existential falsifier  rebuilt r3
```

B6 is the only block never ruled on. Revision 2 stated it as an unreachability
claim, which was wrong: the visit budget bounds how many positive classes a
realizing seed may visit, and `REAL` does not require the sector to be covered.
Revision 3 replaces that with the divisibility gate above, which is decisive
when it fires, silent when it does not, and regime-local. It is written so that
dropping it leaves B1 to B5 intact.
