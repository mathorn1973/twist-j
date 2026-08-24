# PROMO-C-FRONTIER-WELLPOSEDNESS-1

Promotion proposal for Public Canon v22. Self-contained: a fold can consume this
without reading anything else.

CANDIDATE OUTPUT, NO AUTHORITY. This proposal is not canon. It becomes canon only
after the public pipeline validates it: verifier reproduced on two architectures
byte-identical, public checks green, owner opens the fold PR.

```
Candidate id     C-FRONTIER-WELLPOSEDNESS-1 (rev2)
Proposed status  candidate-C -> C at the frozen finite range (the 25 live rows
                 of Public Canon v21). NOT T: the criteria are stipulated, not
                 derived, and the result is a census, not a theorem.
Action layer     L1 (state). The object is the ledger read as integer tables.
Basis            Public Canon v21, CONTENT_COMMIT 473fea34, CANON_SHA256
                 e82a314c49bf0c05ca103dd2c6845ca3b017845bee2edaf574c7ba98d54dbfda,
                 100166 bytes, SHA256SUMS 5 of 5 OK.
```

## 1. Exact statement proposed for registration

```
FRONTIER-WELLPOSEDNESS-CENSUS [C]

At Public Canon v21 (CONTENT_COMMIT 473fea34), of the 25 live H/O rows, exactly
4 satisfy at least one of two mechanically decidable ledger conditions, and
exactly 0 of the 106 T rows satisfy either:

  UNDEFINED-ROW    the claim_id has no ID-boundary occurrence in canon/CANON.md
                   outside section 18 (lines 2113 to 2215), AND EVIDENCE.tsv
                   gives evidence_kind INLINE_CANON with architecture_requirement
                   none, AND NORMATIVE.tsv gives layer NOT_APPLICABLE with empty
                   gate_ids, AND HISTORY.tsv records no SCOPE_CHANGE or
                   STATUS_CHANGE event.

  STOP-BRANCH-MISSING
                   FRONTIER_PROGRAMS.tsv gives work_state STOP while the
                   REGISTRY.tsv falsifier text contains no occurrence of "STOP".

The 4 are KC3-PLENUM-READOUT and OBSERVER-WRITE-PORT and PROTON-RESIDUAL-IS-QCD
(UNDEFINED-ROW) and COLOR-MEASURE-SELECTION (STOP-BRANCH-MISSING). A row meeting
either condition cannot be retired by any preregistered probe, because the probe
would have to supply the row's predicate or its stop rule before deciding it.
Scope: a census at one frozen commit. No claim that an unflagged row is easy,
that a flagged row is false, or that the conditions are exhaustive.
```

## 2. Falsifier proposed for registration

```
fires if, for any row the census flags UNDEFINED-ROW, a public normative
definition of that row's predicate is exhibited in canon/ outside section 18;
or if a recount at the pinned commit under the stated conditions returns a
number other than 4 of 25 and 0 of 106; or if either condition is shown to
select a T row at the pinned commit.
```

## 3. Verifier and pins

```
prereg rev2    PREREG-C-FRONTIER-WELLPOSEDNESS-1-REV2.md
               sha256 7ae986844119076fe95cf410fc27395b27fde400d3d864fd29caa39f20155e7b
verifier       verify_frontier_wellposedness_rev2.py
               sha256 0a56d1802d5e1522afb1d98e070b8951613cd80202635b69e70c72a5071707b2
stdout         sha256 bc0ff23e4501c984f142196fbe12bf53735614c5b3170827b6608622f24d4258
breaker        break_frontier_wellposedness_rev2.py
               sha256 4571beda53020858febf6e2206ce494177af0347b96863453c115cbb4abec6ed
recount        recount_post_break.py
               sha256 a59d32832d6b18068f802556ec54fe0249782ca8dd623fa2c7fac7b01fc1b039

archived rev1  prereg 6ebbc8e1731bf4659dc0e636b1ccf741214338c686db221cb56defc004216431
               verifier db75e877919c2cd26fb1fef7e49c0987d89c97cb7a722474c81eb4870541ee44
               outcome F-WP-PARSE FIRED, candidate-F, archived, threshold not moved

platform       x86_64, Python 3.11.15, LC_ALL=C LANG=C TZ=UTC,
               PYTHONDONTWRITEBYTECODE=1, PYTHONHASHSEED=0
```

**Blocking obligation before promotion.** Only one architecture was run. The
aarch64 leg with neutral public environment fields is owed, and byte identity is
required. Until then this is candidate-C on one leg and MUST NOT be folded.

**Second blocking obligation.** The verifier asserts the v21 basis pin, so at v22
it will abort. The fold must either pin it to the v21 commit as an archived
census or re-run it against the v22 bytes and register the v22 numbers. Pick one
explicitly; do not let it silently abort in CI.

## 4. Dependency edges proposed

```
FRONTIER-WELLPOSEDNESS-CENSUS  DEF-ARCHITECTURE  REQUIRES  canon definition boundary
KC3-PLENUM-READOUT         FRONTIER-WELLPOSEDNESS-CENSUS  BOUNDED_BY  flagged UNDEFINED-ROW
OBSERVER-WRITE-PORT        FRONTIER-WELLPOSEDNESS-CENSUS  BOUNDED_BY  flagged UNDEFINED-ROW
PROTON-RESIDUAL-IS-QCD     FRONTIER-WELLPOSEDNESS-CENSUS  BOUNDED_BY  flagged UNDEFINED-ROW
COLOR-MEASURE-SELECTION    FRONTIER-WELLPOSEDNESS-CENSUS  BOUNDED_BY  flagged STOP-BRANCH-MISSING
```

## 5. The four owner actions, in order of cheapness

These are the actions the census licenses. Each is a normative edit and belongs
to the owner, not to a probe.

### 5.1 RETIRE KC3-PLENUM-READOUT. Live count 25 -> 24.

The strongest case, and the only one that moves the count.

The row asserts "the ramified place acquires the archimedean readout s" and fires
"if the residue class readout of the ramified place disagrees with the
archimedean value s = abs(1 - zeta_5)". The predicate cannot be typed:

```
s = abs(1 - zeta_5) = 2 sin(pi/5) = sqrt(3 - phi).
Q(zeta_5) intersect R = Q(sqrt5). Solving (a + b sqrt5)^2 = (5 - sqrt5)/2
forces 16 a^4 - 40 a^2 + 5 = 0, discriminant 1280, not a square, so no rational
a exists. Hence s is not in Q(zeta_5); it lies in Q(zeta_20)^+.
Only s^2 = 3 - phi lies in Q(zeta_5).
```

Reduction modulo lambda = 1 - zeta_5 is defined on O = Z[zeta_5]. Since s is not
in that ring, s has no residue class, so "the residue class readout ... disagrees
with s" compares an element of F_5 against an object that has no image in F_5.
Neither branch is reachable. Additionally the row is a leaf: `DEPENDENCIES.tsv`
has it only as `KC3-PLENUM-READOUT DEF-ARCHITECTURE REQUIRES`, and nothing in the
ledger depends on it. Retiring it breaks nothing.

Registry action: HISTORY.tsv event RETIRE with rationale "predicate untypeable at
the declared carrier: s is not in Q(zeta_5) and has no residue class"; remove the
row from the live set; STATUS_COUNTS live_H_O 25 -> 24, status_H 4 -> 3.

If the owner prefers to keep the question, the alternative is a SCOPE_CHANGE that
states both readouts as typed maps into one codomain with a declared
normalization. The one public bridge between the two places is the four-embedding
product `N(1 - zeta_5) = 5`, exactly `(3 - phi)(2 + phi) = 5`, which does not by
itself supply that codomain.

### 5.2 Give OBSERVER-WRITE-PORT a STOP branch. No count change.

Do not retire this one. Its predicate is absent from the canon body, but it
carries three real REQUIRES edges (`QUADRATIC-DECODER-DATA`, `DEF-DECODER-CLOCK`,
`METRO-ADMISSIBILITY`) and its own falsifier already says positive closure needs
"the completed decoder dependency graph". That is a STOP condition stated in
prose but not in the decision grammar. Give it the form
`QUADRATIC-DECODER-DATA` already uses:

```
STOP until the typed observer output schema, the write channel type, the
autonomous state codomain, and the completed decoder dependency graph are
public; fires when a typed public decoder construction supplies a nontrivial
write channel into U; closes positively when the completed graph proves every
output is terminal.
```

Also assign a layer. `NORMATIVE.tsv` currently gives `NOT_APPLICABLE` with no
gate for a row whose whole content is a cross-stage claim about the decoder.

### 5.3 Rescope PROTON-RESIDUAL-IS-QCD. No count change.

Its negative branch reads "closes negatively if the derived residual is
incompatible with the measured proton moment within its comparison window".
There is no measured proton moment in `data/EXTERNAL_SOURCES.tsv`, and "the
proton residual" is defined nowhere. The canon body mentions the proton only as
`6 pi^5` at `canon/CANON.md:1124` and as a stationary density at `:1539`, neither
of which is a residual.

Either register the measured datum with a named source and window, or restate
the branch so it does not quantify over a dataset the public line does not carry.
As written the negative branch cannot be evaluated.

### 5.4 Add the STOP branch to COLOR-MEASURE-SELECTION. No count change.

`FRONTIER_PROGRAMS.tsv` schedules it `ROOT / STOP / FORMAL`, but its decision
condition has only a positive and a negative branch. `canon/FRONTIER.md` lines 4
to 7 state that `REGISTRY.tsv` alone supplies every decision condition and that
the program table "creates no claim, status, scope, dependency, layer, gate,
evidence, or verifier permission". So a reader working from the registry sees a
closable row, and the STOP label cannot supply the missing branch.

The row is not closable as written for a second, independent reason: its negative
branch quantifies over "every named constraint", and no constraint is named
anywhere in the public line. The scope numbers "24 carrier orbits, 16 observable
types" occur in exactly one authored sentence propagated to four generated views,
with evidence `inline`, and section 12 of the canon never mentions them. The
public color verifier `reproduce/color-ladder/verify.py` passes 12 of 12 and
never touches `SL_3(F_5)`, never enumerates orbits of any carrier, and never
prints 24 or 16. Proposed replacement, matching the sibling STOP rows:

```
STOP until the carrier set, the acting group, the orbit decomposition, the
observable-type enumeration, and the constraint list are public; closes
positively by a derivation selecting the weight vector over the published orbits
under the published constraints; closes negatively if that constraint set is
exhausted with no surviving weight vector, or if two inequivalent vectors survive
every published constraint.
```

## 6. Reported for the same fold, not part of the census

Each of these is a separate finding with no status attached. They are cheap to
fold and each removes a false affordance or a hazard.

1. **Three claim_id substring collisions** among 203 ids, none live:
   `DIRAC-STEP` inside `DIRAC-STEP-THEOREMS`, `READING-SPLIT` inside
   `BOOST-READING-SPLIT`, `ELECTRON-SIGN` inside `ELECTRON-SIGN-LAWS`. Any ledger
   tool matching claim_ids by plain substring is exposed. Recommend the
   ID-boundary rule used by this candidate's verifier in `tools/`.

2. **KAPPA-SHAPES library minimum 31/8 is not the minimum of the registered
   greedy bound.** At L = 8 the 3-cube Gray Hamiltonian cycle gives
   30/8 = 15/4 < 31/8. No public claim is violated, because KAPPA-SHAPES says
   "no statement about arbitrary shapes", but 31/8 therefore cannot serve as an
   admissible kappa for PHOTON-WINDOW-PROOF and the disclaimer is carrying the
   whole load. Recommend one scope sentence saying so.

3. **PHOTON-WINDOW-PROOF route (i) is not a finite search.** The threshold
   reduction is exact and integer: for rational kappa = p/q, `2^(4 kappa) > 2401`
   is `2^p > 7^q`. But `F_occ` is a minimum-support integer 2-chain quantity, not
   an arc-additive weight, so minimum-mean-cycle does not apply, and the greedy
   surrogate is not walk-local. Enumerated greedy-LB minima over closed
   edge-simple loops in Z^4 are 17/4, 4, 15/4, 7/2 at L = 4, 6, 8, 10: strictly
   decreasing with no stabilization above log_2 7 = 2.807. Also the Z^4 plaquette
   lattice these rows live on is code-only and absent from the architecture
   inventory at `canon/CANON.md:86-92`, and the Froehlich-Spencer roughening
   import of obligation (ii) has no public criterion, citation, or scope at all.

4. **SCHEME-DICTIONARY quantifier, as a reading only.** Its negative branch says
   "if any dictionary requires a new free dimensionless parameter" for a row whose
   subject is an existence question, which makes the branches non-exclusive. This
   is NOT registered as a defect: the mechanical indicator that flagged it was
   withdrawn in the break round because "if any" is the house idiom, used in nine
   rows including both v21 theorems. Owner judgment, not machine-checked.

## 7. What the census does not license

It licenses no status change to any scientific row beyond the four owner actions
above, no new physics, and no closure of any scientific obligation.

Retiring an undefined row shortens the frontier without advancing the program.
The available v22 reduction is one row, 25 to 24, and it is bookkeeping. The
other 21 live rows are real and none of the five audited in depth this session
(CURVATURE-OPERATOR-CANONICAL, COLOR-MEASURE-SELECTION, PHOTON-WINDOW-PROOF,
KC3-PLENUM-READOUT, SCHEME-DICTIONARY) can be closed on the science today.

## 8. The best actual science target for v22, for the record

Not part of this candidate, offered as scheduling input. `METRO-ADMISSIBILITY`
has the most leverage of the 21 workable rows, because v21 just supplied
`METRO-FINITE-STATE-RATIONALITY [T]` and the higher-dimensional residual class
appears to need no new mathematics: for a d-dimensional digit alphabet the
transition-count matrix has constant row sum q^d, so `P = B/q^d` is row
stochastic, `q^d` is semisimple by the same boundedness argument, and the same
rational Bezout projector gives conditional rationality. That would classify one
named residual class ("higher dimensional supports") and, with an invariance
proof under declared reductions, satisfies the row's positive branch for that
class.

It would NARROW the row, not close it: the residual also contains non-finite-state
streams, unbounded-memory adaptive protocols, stochastic protocols without an
exact finite reduction, irrational carriers with cross-layer normalization, and
physical units. Narrowing does not move the live count. Say so in the fold rather
than letting a narrowed row read as a closed one.
