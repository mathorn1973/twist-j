# C-QDD-U-INDUCED-NULL-ANATOMY-1-N

NON-CANONICAL. Incubation note, revision 3. No authority, no Canon change, no
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
REVISION    3, after two owner verdicts
```

Every count quoted below is quoted from the committed `EXPECTED.txt` of that
probe (path `probes/P-QDD-INSTRUMENT-U-INDUCED-1/EXPECTED.txt`, 3441 bytes,
SHA-256 `652baf70e75600fa80fb685c36435b19cdaae6e8f519e207e0d0a646bb7f5d5c`,
blob `46f7fd3fcaa223de342657e1aba7ec8dbc7f6ccc`) and is an audit input, not a
re-derivation.

## 0. Withdrawals

Revision 1 proposed H-ZT, that the whole null is carried by the 44 zero-target
classes and the 268-class positive sector was untested. The owner refuted it
from `SEED-DEPENDENT-271350`. Revision 2 withdrew:

```text
withdrawn (r2)  "H-ZT is consistent with every published count"
withdrawn (r2)  "the 268-class sector was never actually tested"
withdrawn (r2)  "the recorded output does not rank the two causes"
```

Revision 2 then overreached in the other direction on the denominator
arithmetic it introduced. The owner corrected that too. Revision 3 withdraws:

```text
withdrawn (r3)  "the whole positive sector is arithmetically unreachable on
                 either window whatever U does"
                 The bound says a realizing seed may VISIT at most 107
                 positive classes on W and 245 on W2. REAL-POS quantifies only
                 over visited classes, so nothing is thereby unreachable.
withdrawn (r3)  "224 of the 268 positive classes have q_c >= 6"
                 All 268 do; the smallest positive denominator is 6. The
                 threshold with 244 classes is q_c >= 8.
corrected (r3)  the complement form and the pigeonhole form of the seed bound
                 are algebraically equivalent readings of one published C8
                 number. They are a consistency check on the arithmetic, not
                 two independent pieces of evidence.
```

Both errors were of the same kind: a static count carried further than the
quantifier it belongs to.

## 1. Why this note exists

A null result is exactly as strong as the description of what was searched. The
sealed probe reports `POST-UNDEFINED-OR-ZERO-900` and three `NO-REALIZATION`
tags with count zero. Read without the class definition, that reads as "the
autonomous update cannot produce a QDD instrument". That reading is not
available from this evidence. What the evidence does support is that the frozen
construction carries more than one obstruction, and that the zero-target sector
is not the one that is settled.

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

The 268 positive classes carry a second piece of structure. Writing the target
rate in lowest terms `p_c / q_c`, the LOW and HIGH denominators coincide, and

```text
q:   6   7   8  14  16  17  26  32  46  56  64  96 104 136 176 224 256
n:  12  12  12   6  40  12  24   4  18  24  16  12  12  16  24  12  12

smallest positive denominator      q = 6, so all 268 have q_c >= 6
244 of the 268 have q_c >= 8
sum of q_c over the 268 classes    19688
the 44 zero-target classes all have denominator 1
```

## 5. Two sufficient causes, and one diagnostic gate

### 5.1 Cause A, the zero-target sector. Open.

On a class with an exactly zero branch rate the frozen rules are absolute
rather than statistical: `REAL` demands the record read that cell exactly never
at that delay, and `POST-UNDEFINED-OR-ZERO` fires on a single event there. Each
`rho` is a fixed two-cell partition of the 25 fiber cells, and the fiber is a
refreshable register with no ready state and no reset, so every checkpoint
reads LOW or HIGH. For a fixed `(lambda, d)`, writing

```text
A = union of Reach(lambda, d, c) over c in Z_HIGH
B = union of Reach(lambda, d, c) over c in Z_LOW
```

a subset `S` avoids a zero-target event exactly when `A subset S` and `S`
disjoint from `B`. Since `S` must additionally be one of the 30 nonempty proper
subsets, an admissible `S` exists only when `A` and `B` are disjoint, `A` is not
all of `F_5` and `B` is not all of `F_5`; the safe procedure is to enumerate the
30 masks and keep those satisfying both containments. Reach equal to `F_5` is
sufficient for failure but not necessary, so a count of full-reach triples is
not a falsifier. The surviving question is

```text
Z-SUFFICIENT   is the zero-target event indicator U3 by itself enough to
               eliminate all 900 pairs, on each window separately?
```

A negative answer means only that `U3` alone does not suffice. It does not mean
the `Z` sector is insufficient, since `Z` also obstructs through the empty-branch
and ZERO-post causes on its own positive-target branches.

### 5.2 Cause B, seed dependence inside the positive sector. Established.

`SEED-DEPENDENT-271350` counts triples `(rho, d, c)` over the 900 pairs and all
313 classes, including ZERO, for which two seeds visiting `c` in `W` have
different class-averaged `L/N`.

**Lemma.** If `(rho, d, c)` is seed dependent and `c` is a positive class, then
`(rho, d)` fails `REAL-POS-SINGLE`, because two seeds give different rates and
both would have to equal the same fixed target.

**Bound.** Total triples are `900 x 313 = 281700`, so exactly
`281700 - 271350 = 10350` are seed independent. A pair satisfying
`REAL-POS-SINGLE` needs all 268 of its positive triples seed independent, and
distinct pairs use disjoint triples, hence

```text
POS-REALIZED-SINGLE  <=  floor(10350 / 268)  =  38.
```

The owner's pigeonhole form reaches the same 38 from the complement: at most
`45 x 900 = 40500` seed-dependent triples lie off the positive sector, so at
least `230850` lie inside it, and at least `ceil(230850 / 268) = 862` pairs fail
there. The two forms are algebraically equivalent readings of the one published
C8 number. Gate A7 checks they agree, which is an arithmetic self-check, not
corroboration by a second source.

At least 862 of the 900 pairs demonstrably fail inside the positive sector on
window `W`, before any new computation. This is a statement about the registered
`U`: the finite-window conditional rate on the positive sector depends on the
seed, and the frozen predicate quantifies over all 15625 seeds.

### 5.3 A divisibility gate. Cheap, decisive when it fires, one-sided.

`REAL` requires `L / N = p_c / q_c` exactly with `L` and `N` integers and
`gcd(p_c, q_c) = 1`, so

```text
q_c divides N     for every visited positive class,
q_c divides N     for every visited positive ORIENTED pre-cell as well,
                  since REAL-ORIENT carries the same equality per orientation.
```

The decisive test is therefore a divisibility test on the visit counts, not a
budget:

```text
GATE   there exists a visited positive class or oriented pre-cell with
       N > 0 and N mod q_c != 0
```

evaluated separately on `W`, on `W2`, and on the census aggregate, whose summed
counts must satisfy their own divisibility independently.

What makes this sharp is that `N` depends on the seed and the window only, never
on the record map or the delay. So **one defective seed nullifies all 900 pairs
of that regime at once**: if some seed has a visited positive class with
`q_c` not dividing `N`, then no integer `L` can produce the target rate for that
seed, and `REAL-POS-SINGLE`, being universally quantified over seeds, fails for
every `(rho, d)`. The gate does not need every seed to be defective, and a
falsifier that demanded all 15625 would be the wrong shape.

The correct conclusion, if the gate fires, is not "independently of `U`". The
visit histogram is produced by `U`. It is:

> the `U`-induced visit histogram is integer-incompatible with exact `REAL`
> already before the record map and the delay are chosen.

Two weaker certificates come from the same arithmetic and are kept only as
such, because they bound visits rather than deciding realizability:

```text
N < q_c on a visited positive class is an immediate failure of that class
sum of q_c over the visited positive classes <= |window|, hence a realizing
  seed may visit at most 107 of the 268 positive classes on W and at most 245
  on W2; resolved by orientation, at most 138 respectively 401 of the 536
  positive oriented pre-cells
```

Neither certificate makes `REAL-POS` unreachable, because `REAL` quantifies only
over visited classes and does not require the sector to be covered. And the gate
is one-sided: finding no indivisibility licenses no positive conclusion about
realizability whatsoever.

## 6. What the two windows and the census do and do not acquit

Two disjoint windows and two different seed sets are evidence against a window
artifact and against a start transient. The census adds nothing independent: it
is the aggregation of the `S-single` counts over the same window `W`. Its
divisibility, however, is a separate test on separate integers and must be run
separately.

## 7. The positive residue

Two things in the sealed output are informative, and neither is a null. Both
survive unchanged through revisions 2 and 3.

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

Cause B is established, so no exit that only repairs the zero-target sector can
rescue the construction. The exits are necessary at best.

```text
E1  admit a ready state or a reset, so a zero-target branch can be honoured
E2  enlarge the record beyond two cells, or beyond one checkpoint
E3  restrict the pre-observable so zero-target classes are not visited
E4  weaken the realization predicate, which is currently exact rational
    equality per seed on a finite window; cause B says the per-seed universal
    quantifier already fails on at least 862 pairs at 1536 steps, and the
    divisibility gate of 5.3 may show the visit histogram cannot carry exact
    equality at all
E5  change nothing and accept that this split and this record class are a
    negative result about the construction rather than about U
```

`E3` remains the dangerous one: choosing the coarse-graining after seeing which
classes obstruct is exactly the circularity `QDD-INSTRUMENT-NONSELECTION [T]`
warns about. `E4` is the one both settled causes point at, and it also touches
program commitments directly, since the frozen stance is `SAMPLING NOT PROVIDED`
with no limit asserted. Naming that tension is the honest output here; resolving
it is not authorized by anything in this note.

None of E1 to E5 is adopted.

## 9. Scope firewall

This note does not:

- change any Canon status, registry row, frontier entry or definition;
- advance or retire `QDD-INSTRUMENT-APPARATUS [O]` or its blockers O1 and O2;
- assert `Z-SUFFICIENT` in either direction;
- assert that any divisibility failure occurs; 5.3 defines a gate and states
  what would follow if it fires, and nothing is measured here;
- re-derive, replace or reinterpret any count of the sealed probe; sections 5.2
  and 5.3 derive consequences of published counts and of the Canon target law;
- claim a limit, an L6 measure, or any sampling statement beyond
  `SAMPLING NOT PROVIDED`;
- select a record map, a delay or a coarse-graining;
- adopt any of E1 to E5;
- claim the two-architecture computation gate for `null_anatomy.py`.

The companion draft
`PREREG-DRAFT-P-QDD-OBSTRUCTION-LOCUS-1_2026-08-16.md` states the measurement
that would settle `Z-SUFFICIENT` and run the divisibility gate. It is a draft
awaiting owner ANO and carries no probe identity.
