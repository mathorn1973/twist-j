# PREREG DRAFT P-QDD-OBSTRUCTION-LOCUS-1

NON-CANONICAL DRAFT. Incubation-lane preregistration. This file is not a public
probe, holds no probe identity, and earns nothing. No verifier exists yet and no
formal gate has run. Sealing requires, in this order: owner ANO on blocks B1 to
B5 below, a fresh public claim-lock issue, a fresh branch
`probe/P-QDD-OBSTRUCTION-LOCUS-1`, and the accepted `PREREG.md` plus the
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
PRIOR       P-QDD-INSTRUMENT-U-INDUCED-1, claim lock #395, pull request #396,
            pin 45cad3384c69d7f2e187d88e63c10ecbad965f0d,
            EXPECTED.txt 652baf70e75600fa80fb685c36435b19cdaae6e8f519e207e0d0a646bb7f5d5c
TARGET ROW  QDD-INSTRUMENT-APPARATUS [O], blockers O1 and O2
```

## Mandatory result-exposure disclosure

This is a **result-exposed confirmatory diagnostic**. It is designed after the
complete published output of `P-QDD-INSTRUMENT-U-INDUCED-1` and it exists
because of that output. It cannot earn a discovery status and does not ask for
one.

Exposure is declared exactly:

- every count and tag of the prior `EXPECTED.txt` is known to the author;
- the static class decomposition of gate D1 below (42 LOW-zero, 2 HIGH-zero,
  268 both-positive) was computed before this draft, in the incubation lane, by
  `null_anatomy.py` in this directory, and is published in the companion note.
  D1 is therefore a confirmatory transcription gate, not a discovery gate;
- no window count, joint tally, reachability set, or any dynamic quantity of
  the proposed measurement has been computed by anyone at the time of writing;
- the formal execution count of the future accepted verifier is zero.

## Question

The prior probe returned `POST-UNDEFINED-OR-ZERO-900` and three
`NO-REALIZATION` tags of count zero over the complete class `R x D`. Both
outcomes are single tags with no locus. The question here is where the
obstruction lives, and nothing else:

> Is the null of `P-QDD-INSTRUMENT-U-INDUCED-1` carried by the 44 nonzero
> classes on which the frozen occurrence law prescribes an exactly zero branch
> rate, or does it survive on the 268 classes where both branches are strictly
> positive?

Hypothesis under test, stated in the companion note:

```text
H-ZT  the entire observed null is carried by the 44 zero-target classes, and
      the 268-class sector was never tested
```

## Design principle

The construction does not change. `U`, the split, `beta`, `cls`, `R`, `D`, both
windows, both seed sets and the frozen target are all reused verbatim from the
sealed preregistration. Only the **granularity of the report** changes. The
diagnostic is therefore a re-derivation of the same computation with a finer
readout, and any disagreement with an overlapping sealed count is itself an
ARCH-STOP rather than a new finding.

## Field 1: equation

All definitions of `P-QDD-INSTRUMENT-U-INDUCED-1` sections 1.1 to 1.7 are
imported unchanged and are not restated here. The following are added.

### 1a. Zero-target decomposition (block B1)

```text
Z_LOW  = { nonzero classes c : w_low(c)  = 0 }   expected |Z_LOW|  = 42
Z_HIGH = { nonzero classes c : w_high(c) = 0 }   expected |Z_HIGH| = 2
POS    = { nonzero classes c : w_low(c) > 0 and w_high(c) > 0 }
                                                  expected |POS|    = 268
Z      = Z_LOW union Z_HIGH,  disjoint,  |Z| = 44,  |Z| + |POS| = 312
```

Class identifiers follow the frozen lexicographic numbering of the sealed
preregistration section 1.2. The complete identifier lists are printed.

### 1b. Cause split of the strict post tag (block B2)

For each pair `(rho, d)` the three frozen causes are evaluated and reported
separately instead of merged:

```text
U1(rho,d)  some visited nonzero positive-target branch has no event
U2(rho,d)  some visited nonzero positive-target branch has a ZERO post
U3(rho,d)  some event occurs on a zero-target branch
```

`POST-UNDEFINED-OR-ZERO(rho,d)` is exactly `U1 or U2 or U3`, which is audited
against the sealed definition. The report gives the count of pairs for each of
the seven nonempty subsets of `{U1,U2,U3}`, and in particular the count of
pairs for which `U3` holds and neither `U1` nor `U2` holds.

### 1c. Restriction to the positive sector (block B3)

```text
REAL-POS-CLASS(rho,d;x_0,W*)   as REAL-CLASS but quantified only over c in POS
REAL-POS-ORIENT(rho,d;x_0,W*)  as REAL-ORIENT but only over pre-cells of POS
REAL-POS = REAL-POS-CLASS and REAL-POS-ORIENT, exact equality in Q
REAL-POS-SINGLE / REAL-POS-LONG / REAL-POS-CENSUS   as in the sealed 1.7
FUNCTIONAL-POS   as FUNCTIONAL but with the pre-class domain restricted to POS
```

The restriction is applied to the **quantifier domain only**. No count is
re-weighted, no class is merged, and the target values are untouched. The
restriction is defined by the zero set of the frozen target law, which is fixed
before any count is read; it is not a post hoc selection of classes by
performance.

### 1d. Reachability of the zero-target sector (block B4)

For each `lambda` in `Lambda_0`, each delay `d` in `D`, and each class `c` in
`Z`, over the census of window `W`:

```text
Reach(lambda, d, c) = { lambda(f(x_(k+d))) : k in W, cls(x_k) = c }  subset F_5
```

`Reach` is a set of residues, not a distribution. Its role is mechanical: a
subset `S` can avoid the forbidden cell for class `c` only if `Reach` is a
proper subset of `F_5` on the forbidden side. If `Reach(lambda,d,c) = F_5` then
no member of the 30 subsets can avoid it, and `U3` is forced for every subset
at that `(lambda, d)`.

### 1e. Information locus (block B5)

The sealed `INFO` predicate is reused verbatim and reported per `lambda`:

```text
INFO-BY-LAMBDA(lambda) = #{ (S,d) : INFO(rho_(lambda,S), d) }   six numbers
```

The exhaustive S2 audit is repeated, together with the statement that `s = q+r`
is the unique member of `Lambda_0` appearing in `sigma`, and with the separate
closure of the piston half `S` and the fiber half `s` under every generator.
The sheet table of `KERNEL-Z6-SYNCHRONIZATION` is reproduced from the two
one-dimensional maps as an integrity check.

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
`verify.py`, so that the cross-check of gate D7 is a genuine second
implementation of the shared quantities. Memory discipline, packed-lane layout,
and the 32-bit cell bounds of the sealed section on code are carried over
unchanged, since the traversal is the same size.

## Field 3: carrier or data

No external data.

```text
autonomous carrier   Omega = N_0 x F_5^6, U as registered in Canon v49
system carrier       V_eff subset (Q^4, G) via beta
pointer carrier      F_5^2, read only through R
target objects       E_low, E_high, m, w_low, w_high, dens, occ, unchanged
prior evidence       the committed EXPECTED.txt of P-QDD-INSTRUMENT-U-INDUCED-1,
                     used only as a cross-check target in D7
```

## Field 4: systematics and completeness

There is no measurement systematic. Gates:

```text
D0  generators, relations, sheet commutators, 313 classes, 25 ZERO checkpoints
    and 22 occurrence values reproduce exactly, as in the sealed C1 and C2
D1  the decomposition 42 / 2 / 268 reproduces; Z_LOW and Z_HIGH are disjoint;
    m > 0 on every nonzero class; complete identifier lists printed
D2  U1, U2, U3 evaluated for all 900 pairs; the seven subset counts printed;
    their union audited equal to the sealed strict tag for every pair
D3  REAL-POS-SINGLE, REAL-POS-LONG, REAL-POS-CENSUS and FUNCTIONAL-POS
    evaluated for all 900 pairs; counts and full pair lists printed
D4  the strict post partition recomputed with the pre-class domain restricted
    to POS, ZERO posts counted rather than tagging; counts printed
D5  Reach(lambda,d,c) computed for all 6 x 5 x 44 triples; the number of
    triples with Reach = F_5 printed, together with the complete list of
    triples whose Reach is a proper subset
D6  INFO-BY-LAMBDA printed; S2 audited exhaustively; the separate closure of
    S and s printed as five pairs of one-dimensional maps; the Canon sheet
    table reproduced from them
D7  every quantity overlapping the sealed EXPECTED.txt reproduces exactly:
    records=180, pairs=900, INFO true=150, the three NO-REALIZATION counts,
    functional=0, orient_coherent=0, pure_strict=0, mixed=0,
    undefined_or_zero=900, zero_input_multivalued=900,
    seed_triples=271350, orientation_triples=22500, both channel witnesses,
    the six labelled table hashes and the root hash
```

Any hidden input, floating tolerance, post hoc restriction of `R x D`, any
restriction of the class domain other than the one defined by the zero set of
the frozen target law in 1a, or an unnamed layer lift is STOP.

## Field 5: failure threshold and scientific routing

No tolerance exists.

```text
ARCH-STOP
  D0, D1 or D7 fails. In particular any disagreement with the sealed
  EXPECTED.txt voids this diagnostic entirely; it does not reopen the sealed
  probe and it does not become a finding.

ZERO-TARGET-ONLY-k     number of pairs where U3 holds and U1, U2 both fail
U-CAUSE-<subset>-k     the seven subset counts of D2
POS-REALIZED-k         number of pairs satisfying REAL-POS-SINGLE
POS-LONG-REALIZED-k    number satisfying REAL-POS-LONG
POS-CENSUS-REALIZED-k  control
POS-FUNCTIONAL-k       number satisfying FUNCTIONAL-POS
POS-UNDEFINED-OR-ZERO-k  the restricted strict partition of D4
REACH-FULL-k           number of (lambda,d,c) triples with Reach = F_5
INFO-BY-LAMBDA         six numbers summing to 150
```

Falsifiers:

```text
F1  ZERO-TARGET-ONLY-k with k < 900
      H-ZT is refuted as a complete explanation. At least one pair fails for a
      reason interior to the positive sector.
F2  POS-REALIZED-0 together with POS-FUNCTIONAL-0
      the obstruction survives on the well-conditioned sector. The frozen
      split and record class, not the zero set of the target, are then the
      load-bearing choices, and the sealed null carries genuine information
      about U.
F3  POS-REALIZED-k with k > 0
      at least one (rho,d) reproduces the occurrence law exactly on the entire
      positive sector. This earns nothing by itself: the zero-target sector
      remains unrealized and the pair is still not an instrument. It is
      reported as a materially different reading of the sealed null and is
      routed to a separate owner decision.
F4  REACH-FULL-0
      the reachability mechanism proposed in the companion note is wrong. The
      zero-target failures are then dynamical selections rather than a
      partition impossibility, even if F1 does not fire.
F5  the union audit of D2 disagrees with the sealed strict tag on any pair
      transcription error; ARCH-STOP.
```

Scientific routing, fixed before any pin:

- `ZERO-TARGET-ONLY-900` with `REACH-FULL-k`, `k > 0`, is the H-ZT outcome. It
  records that the sealed null measured the zero set of the frozen target law
  meeting a two-cell record class, and that the 268-class sector is untested.
  It changes no status. It authorizes nothing about `U`. Its only consequence
  is that the next construction must change a frozen choice, from the exits
  E1 to E3 named in the companion note, before any further search.
- `F2` is the opposite outcome and is the stronger scientific result: it would
  be the first constraint this lane has produced on the registered coupling
  itself, at the frozen split. Even then it earns at most a finite-window
  classification statement, candidate grade C at a later reviewed fold, and it
  does not close `QDD-INSTRUMENT-APPARATUS [O]` negatively, because the class
  of section 2 of the companion note is not the complete admissible physical
  class of that row.
- Every outcome leaves O1 and O2 at STOP. `SAMPLING NOT PROVIDED` remains the
  only sampling statement.

The threshold and scope may not move after the pin.

## Field 6: action layer

```text
L1  exact autonomous dynamics, the split closure, and the static arithmetic
    of the target law
L4  induced apparatus classification on the frozen split, restricted and
    unrestricted
L5  finite-window realized-event stream and exact counts, both windows
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
- assert a limit, an L6 measure, or a sampling construction;
- fill any field of the decoder completion contract;
- introduce a new free dimensionless input.

## Open drafting questions for owner ANO

```text
B1  the zero-target decomposition and its use as the restriction domain
B2  the three-cause split of the strict post tag
B3  the restricted realization and functional predicates
B4  the reachability report and its 6 x 5 x 44 scope
B5  the information-locus report and the split-closure integrity check
```

Two points deserve an explicit ruling rather than a default:

1. **Is the POS restriction admissible at all?** It restricts a quantifier
   after a null has been seen. The defence is that the restricting set is the
   zero set of the frozen target law, computable before any count and published
   in the companion note, so it is not selection by performance. The owner may
   still hold that any post-result restriction of a sealed quantifier must
   carry a fresh probe identity with no reference to the sealed one, in which
   case D7 must be dropped and the diagnostic becomes a standalone measurement.
2. **Scope of D5.** Reach over the census of `W` is the cheap version. Reach
   over `W2` as well would double the traversal cost for a mechanism check that
   is already decided by the first window. The draft proposes `W` only, and the
   owner may widen it.
