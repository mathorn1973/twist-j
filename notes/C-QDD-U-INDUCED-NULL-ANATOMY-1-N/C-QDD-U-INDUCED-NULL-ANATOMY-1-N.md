# C-QDD-U-INDUCED-NULL-ANATOMY-1-N

NON-CANONICAL. Incubation note. No authority, no Canon change, no `canon/`
file touched, no registry row edited, no status moved. It records how the
negative half of `P-QDD-INSTRUMENT-U-INDUCED-1` should and should not be read,
and it fixes the candidate class that the null actually quantifies over.

```text
BASIS       Public Canon v49, STATE ACTIVE, AUTHORITY mathorn1973/twist-j main
TAG         canon-v49
CONTENT_COMMIT dc80228522a4ccb9495550dfbef8ba73b33b2157
CANON_SHA256   d456c42575375774200b08dafc3b4225643f526f5f1826292f1255f39d332f9e
CANON_BYTES    237233
SUBJECT     probe P-QDD-INSTRUMENT-U-INDUCED-1, claim lock issue #395,
            pull request #396, pin 45cad3384c69d7f2e187d88e63c10ecbad965f0d
DATE        2026-08-16
```

At the time of writing, pull request #396 is open and unmerged. Every count
quoted below is quoted from its committed `EXPECTED.txt`
(SHA-256 `652baf70e75600fa80fb685c36435b19cdaae6e8f519e207e0d0a646bb7f5d5c`)
and is an audit input to this note, not a re-derivation.

## 1. Why this note exists

A null result is exactly as strong as the description of what was searched. The
sealed probe reports `POST-UNDEFINED-OR-ZERO-900` and three
`NO-REALIZATION` tags with count zero. Read without the class definition, that
reads as "the autonomous update cannot produce a QDD instrument". That reading
is not available from this evidence. This note states the class, states the
mechanical anatomy of the target law inside that class, and separates the part
of the null that is informative from the part that is forced by a definitional
corner.

## 2. The class the null quantifies over

Everything below was frozen before execution and none of it was selected after
seeing counts.

```text
law            the registered autonomous update U of Canon v49 sections 2 and 3,
               unchanged; no coupling was chosen for the probe
split          system = piston (p1,p4,p1p,p4p);  pointer = fiber (q,r)
pre-observable beta = DEF-QDD-BALANCED-PISTON at the head checkpoint,
               cls(x) = {beta(x), -beta(x)}
               313 classes, 625 oriented pre-cells, 25 ZERO checkpoints
record class   R = { rho_(lambda,S) },  rho = LOW iff lambda(q,r) in S
               lambda over Lambda_0 = ((1,0),(0,1),(1,1),(1,2),(1,3),(1,4))
               S over the 30 nonempty proper subsets of F_5
               |R| = 180 two-cell maps, every one a function of ONE checkpoint
delays         D = {1,2,3,4,5}
pairs          |R x D| = 900, complete enumeration, none selected post hoc
windows        S-single  all 15625 seeds, W  = [512, 2048)
               S-long    625 ready-fiber seeds, W2 = [2048, 16384)
               S-census  the S-single counts summed over seeds (control)
target         the frozen (E_low, E_high) and occ = (w_low/m, w_high/m)
predicate      REAL = REAL-CLASS and REAL-ORIENT, exact equality in Q,
               universally quantified over seeds and over every nonzero class
               with a visit
post rules     the strict partition POST-PURE-STRICT / POST-MIXED /
               POST-UNDEFINED-OR-ZERO, undefined/zero taking precedence
```

So the object that came back empty is:

> a two-cell record read off a single checkpoint of the two-coordinate fiber,
> at a delay of at most five, with no ready state and no reset, required to
> reproduce the frozen occurrence law exactly, simultaneously on every visited
> nonzero class and on both orientations, for every seed.

## 3. What the null does not quantify over

None of the following was varied, so none of it is constrained by the result:

```text
- any other split of the six coordinates into system and pointer
- record maps with more than two cells
- record maps reading more than one checkpoint, or a time-averaged register
- a ready state, a reset, or any readiness condition
- delays greater than five
- coarse-grainings of the piston other than cls
- any window other than the two frozen ones, and any limit
- composition, a second copy, or an environment factor
- any effect pair other than the frozen (E_low, E_high)
```

`QDD-INSTRUMENT-APPARATUS [O]` closes negatively only "for a frozen complete
admissible physical class proved empty or proved unable to realize the effect
pair or event law". The class of section 2 is not that class, and the probe
does not claim it is. This note exists so that the distinction survives the
result being quoted.

## 4. Anatomy of the frozen target law, before any dynamics

The occurrence law has a zero set, and the zero set is large. Writing `v` for a
balanced piston vector and using only the Canon v49 formulas:

```text
w_low(v)  = (1/20) (sum v_i)^2        vanishes exactly when sum v_i = 0
w_high(v) = sum v_i^2 - (1/4)(sum v_i)^2  vanishes exactly when v is constant
m(v)      = sum v_i^2 - (1/5)(sum v_i)^2  is strictly positive off the ZERO class
```

Enumerating the 312 nonzero classes (`null_anatomy.py`, gate A3):

```text
 42 classes have w_low  = 0   prescribed LOW  rate exactly 0, occ = (0, 1)
  2 classes have w_high = 0   prescribed HIGH rate exactly 0, occ = (1, 0)
268 classes have both branches strictly positive
```

The two constant classes are the representatives `(-2,-2,-2,-2)` and
`(-1,-1,-1,-1)`, class identifiers 1 and 157 under the frozen lexicographic
numbering. The 42 LOW-zero identifiers are listed in the recorded stdout.

So 44 of the 312 nonzero classes carry a branch whose prescribed rate is not
small but exactly zero. On such a class the frozen rules are absolute rather
than statistical:

- `REAL` demands that the record read the zero-target cell exactly never at
  that delay, over every window and every seed;
- `POST-UNDEFINED-OR-ZERO` fires on a single event on a zero-target branch.

Now recall the shape of the record class. Each `rho` is a fixed two-cell
partition of the 25 fiber cells; the fiber is a refreshable register with no
ready state and no reset, so every checkpoint reads LOW or HIGH. A pair
`(rho, d)` therefore survives only if, simultaneously for all 44 zero-target
classes, the delay-`d` reachable `lambda`-residue set avoids the forbidden
cell. One event anywhere in that 44-class sector, out of 24000000 single-window
events, is sufficient to produce both `NO-REALIZATION-W` and
`POST-UNDEFINED-OR-ZERO` for that pair.

## 5. Hypothesis H-ZT, and why the published tags cannot decide it

```text
H-ZT  The entire observed null is carried by the 44 zero-target classes.
      On the 268 classes with both branches strictly positive, the frozen
      construction was never actually tested.
```

H-ZT is consistent with every published count, and the published counts cannot
refute it, for two structural reasons.

**The realization predicate is quantified over all nonzero classes at once.**
`REAL-CLASS` requires the equality "for every nonzero `c` with `N_c > 0`". A
single failure on class 25 and a uniform failure across all 312 produce the
same tag `NO-REALIZATION-W count=0`. The tag has no locus.

**The strict post tag merges three disjoint causes.** By the frozen definition,
`POST-UNDEFINED-OR-ZERO` fires when any one of the following holds:

```text
U1  a visited nonzero positive-target branch has no event
U2  a visited nonzero positive-target branch has a ZERO post
U3  any event occurs on a zero-target branch
```

`POST-UNDEFINED-OR-ZERO-900` reports the union. U3 is a statement about the
target law meeting the record class; U1 and U2 are statements about the
dynamics. They are not the same finding and they are not separated anywhere in
the committed output.

This is not a defect of the sealed probe. Its enumeration and its refusal to
restrict `R x D` after the fact are correct discipline, and the merged tag was
frozen before execution. It is a limit on what the recorded evidence can be
asked afterwards, and it is repairable only by a new measurement.

## 6. What the three regimes do and do not acquit

The probe reports `NO-REALIZATION-W`, `LONG-NO-REALIZATION-W2` and
`CENSUS-NO-REALIZATION-W`, all zero. This is weaker than three independent
readings. `S-census` is the aggregation of the `S-single` counts over seeds, so
it shares the window `W = [512, 2048)`. The genuinely distinct reads are two:

```text
W  = [512, 2048)     all 15625 seeds        24000000 events
W2 = [2048, 16384)   625 ready-fiber seeds   8960000 events
```

Two disjoint windows, two different seed sets, one aggregation. That is
evidence against a window artifact and against a start-transient artifact. It
is not evidence about the choice of sampling semantics in general, and it is
consistent with H-ZT, under which no window could have helped.

`SEED-DEPENDENT-271350` should be read alongside this. The conditional rates
are strongly seed dependent, which is the F4 shape and which by itself blocks
the universal quantifier in `REAL-SINGLE` independently of any target value.
Seed dependence and zero-target dominance are two separate sufficient causes of
the same null, and the recorded output does not rank them.

## 7. The positive residue

Two things in the sealed output are informative, and neither is a null.

**The channel is internal.** `CHANNEL-PASS` with exhaustive S1 and S2 audits
and two exhibited feedback witnesses says that coupling, backreaction and
record formation are inside `U`, with no external observer, no inserted draw
and no collapse instruction. This is claimable independently of every other
tag, and it is the part of the result that survives everything in this note.

**The information locus is exactly the selector-coupled functional.**
`RECORD-INFORMATION count=150` is not a scattered 150 out of 900. The
enumerated pairs are exactly `L2:S01:D1` through `L2:S30:D5`, that is one
functional, all 30 subsets, all 5 delays. On the frozen enumeration convention
of `verify.py` the index is zero based, so `L2 = Lambda_0[2] = (1,1)`, the
functional `q + r`. Every other fiber functional, including `q` alone and `r`
alone, is uninformative about the piston class at every delay and for every
subset.

That is exactly the functional that appears in the selector:

```text
sigma(n, x) = (p1 + p4 + p1p + p4p) + (q + r) + 2 theta_n  mod 5
```

The refinement worth recording is that this is not a coincidence of the
enumeration. `KERNEL-Z6-SYNCHRONIZATION [T]` already establishes that
`z_6 = Tr_6` closes under every generator. Gate A4 of `null_anatomy.py` shows
that this one-dimensional closure splits: the piston half `S = p1+p4+p1p+p4p`
and the fiber half `s = q + r` close *separately*, with induced maps

```text
      S           s
a     S           s
b    -S          -s
c   1-S         1-s
d    -S         2-s
e    -S         3-s
```

so `z_6 = S + s` is recovered as the sum of two closed one-dimensional systems,
and the Canon sheet table is reproduced from them (gate A5). All six fiber
functionals are autonomous, because every generator acts on the fiber with
linear part `+-1` (gate A6); what singles out `s` is not autonomy but that `s`
is the unique fiber functional entering `sigma`. The natural reading is that
piston-class information reaches the pointer only through the selector, per S2,
and `s` is the only pointer direction the selector can write on. The
complementary directions are driven by the same generator word but are
conditionally uninformative, which is what the measured 150 says.

This is stated as a structural reading, not as a theorem. The closure and the
selector-coupling are exact and audited here; the conditional uninformativeness
of the complementary directions is the probe's measurement.

## 8. Consequences for the next construction

If H-ZT holds, then no amount of searching inside the frozen class helps,
because the obstruction is not in `U`. Three exits follow directly from
section 4, and each is a construction change, not a search:

```text
E1  admit a ready state or a reset, so a zero-target branch can be honoured
    by the register never being read there rather than by a partition accident
E2  enlarge the record beyond two cells, or beyond one checkpoint, so the
    record can resolve the zero-target sector separately
E3  restrict the pre-observable so the zero-target classes are not visited,
    which is a coarse-graining change and must be justified independently of
    the target, not chosen to make the target fit
```

`E3` is the dangerous one: choosing the coarse-graining after seeing which
classes obstruct is exactly the circularity that
`QDD-INSTRUMENT-NONSELECTION [T]` warns about, and it would not be independent
selection evidence. It is listed for completeness, not recommended.

None of E1 to E3 is authorized here. They are named so that the next
preregistration can freeze one of them before comparison with the effects.

## 9. Scope firewall

This note does not:

- change any Canon status, registry row, frontier entry or definition;
- advance or retire `QDD-INSTRUMENT-APPARATUS [O]` or its blockers O1 and O2;
- assert that H-ZT is true; H-ZT is a hypothesis with a stated measurement;
- re-derive, replace or reinterpret any count of the sealed probe;
- claim a limit, an L6 measure, or any sampling statement beyond
  `SAMPLING NOT PROVIDED`;
- select a record map, a delay or a coarse-graining;
- claim the two-architecture computation gate for `null_anatomy.py`.

The companion draft
`PREREG-DRAFT-P-QDD-OBSTRUCTION-LOCUS-1_2026-08-16.md` states the measurement
that would decide H-ZT. It is a draft awaiting owner ANO and carries no probe
identity.
