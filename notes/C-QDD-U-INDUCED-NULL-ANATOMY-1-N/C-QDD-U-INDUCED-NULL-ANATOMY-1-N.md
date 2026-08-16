# C-QDD-U-INDUCED-NULL-ANATOMY-1-N

NON-CANONICAL. Incubation note, revision 2. No authority, no Canon change, no
`canon/` file touched, no registry row edited, no status moved. It records how
the negative half of `P-QDD-INSTRUMENT-U-INDUCED-1` should and should not be
read, and it fixes the candidate class that the null actually quantifies over.

```text
BASIS       Public Canon v49, STATE ACTIVE, AUTHORITY mathorn1973/twist-j main
TAG         canon-v49
CONTENT_COMMIT dc80228522a4ccb9495550dfbef8ba73b33b2157
CANON_SHA256   d456c42575375774200b08dafc3b4225643f526f5f1826292f1255f39d332f9e
CANON_BYTES    237233
SUBJECT     probe P-QDD-INSTRUMENT-U-INDUCED-1, claim lock issue #395,
            pull request #396, verifier pin 45cad3384c69d7f2e187d88e63c10ecbad965f0d,
            result commit 7df6a605fdff4b5b8a82981795e7d22168d0a081
DATE        2026-08-16
REVISION    2, after the owner STOP verdict on revision 1
```

Every count quoted below is quoted from the committed `EXPECTED.txt` of that
probe (path `probes/P-QDD-INSTRUMENT-U-INDUCED-1/EXPECTED.txt`, 3441 bytes,
SHA-256 `652baf70e75600fa80fb685c36435b19cdaae6e8f519e207e0d0a646bb7f5d5c`,
blob `46f7fd3fcaa223de342657e1aba7ec8dbc7f6ccc`) and is an audit input, not a
re-derivation.

## 0. What revision 1 got wrong

Revision 1 proposed a hypothesis H-ZT, that the entire null is carried by the
44 zero-target classes and that the 268-class positive sector was never tested.
The owner refuted it from the published counts. Revision 1 asserted three
things that are false and are withdrawn here:

```text
withdrawn  "H-ZT is consistent with every published count"
withdrawn  "the 268-class sector was never actually tested"
withdrawn  "the recorded output does not rank the two causes"
```

The refuting argument is section 5.2. It uses only `SEED-DEPENDENT-271350`, a
number that was printed in the output revision 1 was reading. The error was not
a missing measurement; it was a missing division.

## 1. Why this note exists

A null result is exactly as strong as the description of what was searched. The
sealed probe reports `POST-UNDEFINED-OR-ZERO-900` and three `NO-REALIZATION`
tags with count zero. Read without the class definition, that reads as "the
autonomous update cannot produce a QDD instrument". That reading is not
available from this evidence. What the evidence does support is stronger than
revision 1 allowed and narrower than the loose reading: the frozen construction
carries at least three separate sufficient obstructions, two of which are
settled by published counts plus static arithmetic and neither of which is the
zero-target sector.

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
windows        W  = [512, 2048)     all 15625 seeds        24000000 events
               W2 = [2048, 16384)   625 ready-fiber seeds   8960000 events
               census: the seed sum of the W counts, a control sharing W
target         the frozen (E_low, E_high) and occ = (w_low/m, w_high/m)
predicate      REAL = REAL-CLASS and REAL-ORIENT, exact equality in Q,
               universally quantified over seeds and over every nonzero class
               with a visit
post rules     the strict partition POST-PURE-STRICT / POST-MIXED /
               POST-UNDEFINED-OR-ZERO, undefined/zero taking precedence
```

The reads are two windows plus one aggregation, not three sampling regimes.

## 3. What the null does not quantify over

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
- any realization predicate weaker than exact rational equality per seed
```

`QDD-INSTRUMENT-APPARATUS [O]` closes negatively only "for a frozen complete
admissible physical class proved empty or proved unable to realize the effect
pair or event law". The class above is not that class, and the probe does not
claim it is.

## 4. Anatomy of the frozen target law, before any dynamics

Using only the Canon v49 formulas:

```text
w_low(v)  = (1/20) (sum v_i)^2        vanishes exactly when sum v_i = 0
w_high(v) = sum v_i^2 - (1/4)(sum v_i)^2  vanishes exactly when v is constant
m(v)      = sum v_i^2 - (1/5)(sum v_i)^2  is strictly positive off the ZERO class
```

Enumerating the 312 nonzero classes (`null_anatomy.py`, gates A3 and A8):

```text
 42 classes have w_low  = 0   prescribed LOW  rate exactly 0, occ = (0, 1)
  2 classes have w_high = 0   prescribed HIGH rate exactly 0, occ = (1, 0)
268 classes have both branches strictly positive
```

The two constant classes are `(-2,-2,-2,-2)` and `(-1,-1,-1,-1)`, identifiers 1
and 157 under the frozen lexicographic numbering. The 42 LOW-zero identifiers
are listed in the recorded stdout.

The 268 positive classes carry a second, separate piece of structure. Writing
the target rate in lowest terms `p_c / q_c`, the LOW and HIGH denominators
coincide, and the multiset of `q_c` over the positive sector is

```text
q:   6   7   8  14  16  17  26  32  46  56  64  96 104 136 176 224 256
n:  12  12  12   6  40  12  24   4  18  24  16  12  12  16  24  12  12
sum of q_c over the 268 positive classes = 19688
```

## 5. Three sufficient causes, and what the published counts already decide

### 5.1 Cause A, the zero-target sector. Open.

On a class with an exactly zero branch rate the frozen rules are absolute
rather than statistical: `REAL` demands the record read that cell exactly never
at that delay, and `POST-UNDEFINED-OR-ZERO` fires on a single event there. Each
`rho` is a fixed two-cell partition of the 25 fiber cells, and the fiber is a
refreshable register with no ready state and no reset, so every checkpoint
reads LOW or HIGH. Whether this alone kills all 900 pairs is decided exactly by
the reachable residue sets. For a fixed `(lambda, d)`, writing

```text
A = union of Reach(lambda, d, c) over c in Z_HIGH
B = union of Reach(lambda, d, c) over c in Z_LOW
```

a subset `S` avoids a zero-target event exactly when `A subset S` and
`S disjoint from B`, so admissible masks exist exactly when `A` and `B` are
disjoint, and they are then the masks with `A subset S subset F_5 \ B`,
intersected with the 30 nonempty proper subsets. This is the exact criterion.
Reach equal to all of `F_5` is sufficient for failure but not necessary, so a
count of full-reach triples is not a falsifier. The surviving question is

```text
Z-SUFFICIENT   is the zero-target sector by itself enough to eliminate all 900
               pairs, given that a second obstruction is already established?
```

### 5.2 Cause B, seed dependence inside the positive sector. Established.

`SEED-DEPENDENT-271350` counts triples `(rho, d, c)` over the 900 pairs and all
313 classes, including ZERO, for which two seeds visiting `c` in `W` have
different class-averaged `L/N`.

**Lemma.** If `(rho, d, c)` is seed dependent and `c` is a positive class, then
`(rho, d)` fails `REAL-POS-SINGLE`, because two seeds give different rates and
both would have to equal the same fixed target.

**Bound, complement form.** Total triples are `900 x 313 = 281700`, so exactly
`281700 - 271350 = 10350` triples are seed independent. A pair satisfying
`REAL-POS-SINGLE` needs all 268 of its positive triples seed independent, and
distinct pairs use disjoint triples, hence

```text
POS-REALIZED-SINGLE  <=  floor(10350 / 268)  =  38.
```

**Bound, the owner's pigeonhole form.** At most `(42 + 2 + 1) x 900 = 40500`
seed-dependent triples can lie off the positive sector, so at least
`271350 - 40500 = 230850` lie inside it; a pair carries at most 268, so at least
`ceil(230850 / 268) = 862` of the 900 pairs already fail there, giving the same
`900 - 862 = 38`. Gate A7 checks that the two derivations agree.

So at least 862 of the 900 pairs demonstrably fail inside the positive sector,
on window `W`, before any new computation. This is a genuine statement about
the registered `U`: the finite-window conditional rate on the positive sector
depends on the seed, and the frozen predicate quantifies over all 15625 seeds.

### 5.3 Cause C, denominator against window length. Necessary condition.

`REAL` requires `L_c / N_c = p_c / q_c` exactly, with `L_c` and `N_c` integers
and `gcd(p_c, q_c) = 1`, so `q_c` divides `N_c` and in particular
`N_c >= q_c` whenever the class is visited at all. Each step of the window lies
in exactly one class, so the visit counts sum to the window length. Therefore,
for every seed and every pair:

```text
sum of q_c over the VISITED positive classes  <=  |window|.
```

With `sum of q_c over all 268 positive classes = 19688`, this gives

```text
|W|  = 1536   at most 107 of the 268 positive classes may be visited
|W2| = 14336  at most 245 of the 268 positive classes may be visited
minimum window admitting the whole positive sector = 19688 steps
```

The practical form is sharper. A window of 1536 steps distributed over up to
313 classes gives an average of about five visits per class, while 224 of the
268 positive classes have `q_c >= 6`. Any visited positive class with
`0 < N_c < q_c` is an immediate exact failure. Confirming this needs no new
traversal design, only the per-seed visit histogram.

This cause is independent of A and of B. It is stated here as a necessary
condition plus a static count; the visited-class multiset is the one dynamical
input still missing, and it is cheap.

## 6. What the two windows and the census do and do not acquit

Two disjoint windows and two different seed sets are evidence against a window
artifact and against a start transient. The census adds nothing independent: it
is the aggregation of the `S-single` counts over the same window `W`.

Cause C explains why widening the window is not a route out either. `W2` is
still shorter than 19688, so the whole positive sector remains arithmetically
unreachable on it as well.

## 7. The positive residue

Two things in the sealed output are informative, and neither is a null. Both
survive revision 2 unchanged.

**The channel is internal.** `CHANNEL-PASS` with exhaustive S1 and S2 audits
and two exhibited feedback witnesses says that coupling, backreaction and
record formation are inside `U`, with no external observer, no inserted draw and
no collapse instruction. It is claimable independently of every other tag.

**The information locus is exactly the selector-coupled functional.**
`RECORD-INFORMATION count=150` is one functional, all 30 subsets, all 5 delays.
On the frozen zero-based enumeration of `verify.py` that is
`Lambda_0[2] = (1,1)`, the functional `q + r`, which is exactly the fiber
combination entering

```text
sigma(n, x) = (p1 + p4 + p1p + p4p) + (q + r) + 2 theta_n  mod 5.
```

`KERNEL-Z6-SYNCHRONIZATION [T]` establishes that `z_6` closes under every
generator. Gate A4 shows that this one-dimensional closure splits: the piston
half `S = p1+p4+p1p+p4p` and the fiber half `s = q+r` close separately, with

```text
      S           s
a     S           s
b    -S          -s
c   1-S         1-s
d    -S         2-s
e    -S         3-s
```

so `z_6 = S + s` is the sum of two closed one-dimensional systems and the Canon
sheet table is recovered from them (gate A5). All six fiber functionals are
autonomous, because every generator acts on the fiber with linear part `+-1`
(gate A6); what singles out `s` is not autonomy but that `s` is the unique fiber
functional entering `sigma`. Since the piston reaches the fiber only through the
selector, per S2, `s` is the only pointer direction the selector can write on.
The conditional uninformativeness of the complementary directions is the
probe's measurement, not a theorem here.

The information-locus vector `(0, 0, 150, 0, 0, 0)` is already determined by the
published pair list. It is archive structure, not a live decision.

## 8. Consequences for the next construction

Revision 1 listed three exits and treated them as if fixing the zero-target
sector would rescue the construction. That is wrong: cause B is established and
cause C is arithmetic, so neither is touched by any of them. The exits are
necessary at best.

```text
E1  admit a ready state or a reset, so a zero-target branch can be honoured
E2  enlarge the record beyond two cells, or beyond one checkpoint
E3  restrict the pre-observable so zero-target classes are not visited
E4  weaken the realization predicate, which is currently exact rational
    equality per seed on a finite window; cause C says this predicate is
    arithmetically unreachable on the whole positive sector below 19688 steps,
    and cause B says the per-seed universal quantifier fails on at least 862
    pairs at 1536 steps
E5  change nothing and accept that this split and this record class are a
    negative result about the construction rather than about U
```

`E3` remains the dangerous one: choosing the coarse-graining after seeing which
classes obstruct is exactly the circularity `QDD-INSTRUMENT-NONSELECTION [T]`
warns about. `E4` is the one the arithmetic points at, and it is also the one
that touches program commitments directly, since the frozen stance is
`SAMPLING NOT PROVIDED` with no limit asserted. Naming that tension is the
honest output here; resolving it is not authorized by anything in this note.

None of E1 to E5 is adopted. They are named so a later preregistration can
freeze one before comparison with the effects.

## 9. Scope firewall

This note does not:

- change any Canon status, registry row, frontier entry or definition;
- advance or retire `QDD-INSTRUMENT-APPARATUS [O]` or its blockers O1 and O2;
- assert `Z-SUFFICIENT` in either direction;
- re-derive, replace or reinterpret any count of the sealed probe; sections 5.2
  and 5.3 derive consequences of published counts and of the Canon target law
  and introduce no new measurement;
- claim a limit, an L6 measure, or any sampling statement beyond
  `SAMPLING NOT PROVIDED`;
- select a record map, a delay or a coarse-graining;
- adopt any of E1 to E5;
- claim the two-architecture computation gate for `null_anatomy.py`.

The companion draft
`PREREG-DRAFT-P-QDD-OBSTRUCTION-LOCUS-1_2026-08-16.md` states the measurement
that would settle `Z-SUFFICIENT` and locate causes B and C exactly. It is a
draft awaiting owner ANO and carries no probe identity.
