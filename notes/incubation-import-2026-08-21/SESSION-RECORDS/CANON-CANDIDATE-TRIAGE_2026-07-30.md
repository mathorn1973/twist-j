# CANON CANDIDATE TRIAGE, session of 2026-07-30

NON-CANONICAL. Triage of everything this session produced against Public
Canon v27. Carries no authority, promotes nothing, edits no normative file.

```text
basis        Public Canon v27, ACTIVE, mathorn1973/twist-j main 9d17a1e7
             tag canon-v27, canon sha256 c7c4c7e6, 150959 bytes
             SHA256SUMS 5 of 5 OK, check_canon PASS, 214 claims, 28 live H/O
             currency re-checked at triage time: local main == origin/main
```

## Verdict first

Most of what this session computed is already registered, and the pretty parts
are the parts that are already registered. One candidate is worth opening. One
existing project candidate needs a scope correction. Nothing produced today
touches any open obligation that matters.

```text
WORTH A CANDIDATE     C-TWOLOGPHI-INVARIANTS-1, three exact arithmetic
                      characterisations of 2 log phi. The public canon
                      currently registers NO arithmetic identity for its own
                      central constant.
WORTH A CORRECTION    C-ENTROPY-RESIDUE-1 gate G12b states a window bound at
                      L = 20 that is false for every L <= 19. The conclusion
                      survives; the stated gate does not.
NOT WORTH A ROW       everything else, itemised in section 4 with reasons.
PRODUCED NOTHING      ENTROPY-LAYER-BRIDGE [O], CURVATURE-OPERATOR-CANONICAL
                      [O], OBSERVER-WRITE-PORT [H], MINIMAL-READ-DERIVATION
                      [O]. Untouched. Today was audit work, not frontier work.
```

## 1. The gap that justifies the candidate

Searched the whole normative bundle. These are absent, not merely
under-registered:

```text
term            canon/REGISTRY.tsv   canon/CANON.md
Mahler          0                    0
regulator       0                    0
Anosov          0                    0
log_phi         0                    0
Fix(            0                    0
```

So the canon states what `2 log phi` *is read as* and never what it *is*.
`BOOST-COUNT-LADDER [D]` reads `n log phi` as a rapidity count. The entropy
work sits at `[C]` on a frozen dyadic window with `ENTROPY-LAYER-BRIDGE [O]`
open above it. `LOG-AXES-INDEPENDENCE [T]` says `log phi` is independent of
`pi` over the algebraic numbers. Not one row says what number `2 log phi` is
in arithmetic terms.

That is a real hole, and it is the kind that lets prose drift: if the only
public anchor for the constant is a dictionary reading, every text that
mentions it has to borrow its authority from a reading. Three exact identities
close it, and none of them carries any physical content at all, which is
precisely why they are safe to register.

Already covered, and I checked rather than assumed:
`ELECTRON-G-RATIO [T]` already carries `N(J) = 1`, `Tr(J) = 3`,
`J Jbar = 2 - phi = phi^-2`, and `1 - J = zeta_10^9` of exact order 10. Those
four are not new. `J-LI-TORAL-HAAR-NOGO [T]` concerns a Koopman operator on a
torus but is a no-go about the Li norm ladder, a different statement from
anything here.

## 2. The candidate

`C-TWOLOGPHI-INVARIANTS-1`, full document in
`C-TWOLOGPHI-INVARIANTS-1.md`, verifier `verify_twologphi_1.py`, 21 gates,
21 of 21 PASS, exact arithmetic, no float anywhere in the file.

```text
I    log M(J) = 2 log phi. The minimal polynomial of J is
     x^4 - 3x^3 + 4x^2 - 2x + 1 = Phi_5(x - 1); exactly two of its roots lie
     outside the unit circle and both have modulus phi, so the Mahler measure
     is phi^2 exactly.                                       layer L1
II   Reg(Q(zeta_5)) = 2 log phi. Closed against the analytic class number
     formula with no decimal in the argument: the whole formula collapses to
     cot^2(pi/5) + cot^2(2 pi/5) = (5 + 2 sqrt5)/5 + (5 - 2 sqrt5)/5 = 2, an
     identity in Q(sqrt5). Class number one is proved here by the Minkowski
     bound rather than imported.                             layer L1
III  #Fix(T_J^n) = |N(J^n - 1)| in exact closed form for every n, equal to
     L_n^2 when n = 5 mod 10 and (L_n - 2)^2 when n = 0 mod 10, reproduced by
     an archimedean route that never forms the algebraic norm. The growth rate
     is 2 log phi.                                           layer L2
```

The load-bearing fence, and the reason this candidate is worth having rather
than dangerous: **the three are independent, none is derived from another, and
the coincidence of their values is a fact about the number and not a bridge
between the layers.** Anyone who reads I, II and III together as evidence that
the toral entropy is a rate of anything in the architecture has made exactly
the error the corrected bit note now fences in its section 3. Parts I and II
are L1 arithmetic about `J` and its field. Part III is L2, about the torus.
No lift between them is claimed, and the candidate would be worthless if it
implied one.

## 3. The correction to an existing project candidate

`C-ENTROPY-RESIDUE-1` states, as gate G12b of its `STATE-DESCRIPTION-RATE`
argument, that `15625 * 60 = 937500 < 2^20` at `L = 20`. That is true at
`L = 20` and false below it. Scanned:

```text
L    p_TM(L)   15625 p_TM(L)      2^L      bound holds
16   46            718750       65536      no
17   48            750000      131072      no
18   52            812500      262144      no
19   56            875000      524288      no
20   60            937500     1048576      yes
21   64           1000000     2097152      yes
...  linear         linear   exponential   yes for all L in 20..30 checked
```

The candidate's conclusion is unaffected: the window count is linear in `L` and
`2^L` is exponential, so the asymptotic rate is zero regardless. But the gate
as written reads like a general bound and is a single point, and the first `L`
at which it bites is `20`. The doc should say `L >= 20`, or better, state the
linear-versus-exponential argument and use `L = 20` only as a witness. A gate
that is false at `L = 19` and quoted without its threshold is the kind of thing
this programme fires rows over.

Not a canon matter. An incubation-lane correction, and cheap.

## 4. Not worth a row, with reasons

```text
already registered, verified against the head, not new:
  N(J) = 1, Tr(J) = 3, J Jbar = phi^-2      ELECTRON-G-RATIO [T]
  M_J and the canon step, char poly          J-STEP [T], CODEC-TR4 [T]
  |J| = 1/phi, arg J = 2 pi/5                J-PROJECTIONS [T]
  J phi = zeta_5, (J-1)^3 = zeta_5           J-GOLDEN-BRIDGE [T]
  1 - J a primitive tenth root               J-TENTH-ROOT [T], ELECTRON-G-RATIO
  pi = -5 i Li_1(J)                          PI-FROM-J [T]
  Re Li_2(sigma_a(J)) channels, sum pi^2/5,
    ratio 9 on the expanding channel         WALL-LI2-RUNG [T],
                                             WALL-CIRCLE-LEMMA [T]
  the general-N dilogarithm sum
    pi^2 (N-1)(N-2)/(12N)                    WALL-CIRCLE-LEMMA [T] already
                                             states it for all N >= 3
  pi and log phi independent over the
    algebraic numbers                        LOG-AXES-INDEPENDENCE [T]
  script-Q phi^2 = 2 pi, xi phi^2 = 5,
    script-Q/xi = arg J, delta != 0          BRIDGE-DEFECT [T]
  2 pi/5 per tick, five ticks close          METRO-TICK [T]
  gold and silver as two place-attached
    involutions, Klein four at zeta_8        LADDER-SPIN-PLACES [T],
                                             Z2-PLACES-SPLIT [T]
  gold and silver as units of norm -1,
    discriminants 5 and 8                    METAL-TRACE-CASCADE [T]
  Fibonacci/Lucas rigidity for the coins     COIN-SELECTION-CONDITIONAL [T]

true, exact, and too small to earn a row of its own:
  1 < log_phi 2 < 2, from phi < 2 < phi^2 with phi^2 - 2 = 1/phi. A remark
  inside the candidate, not a claim. It is one line from J-PROJECTIONS.
  phi^p = F_p phi + F_(p-1). Standard, and COIN-SELECTION-CONDITIONAL already
  rests on the same rigidity.

a corollary of the candidate, not a separate claim:
  the convergence phase law for (1/n) log #Fix, order 2 phi^-2n / n on
  n = 5 mod 10 and 4 phi^-n / n on n = 0 mod 10, with exact asymptotic ties
  whenever the slow index is twice the fast one. It follows from the closed
  forms of Part III. Belongs in the reproduction README as a warning against
  extrapolating from a single n, not in the registry.

not canon at all:
  the fix ledgers, the deposit sheet, the channel policy, the corrigendum
  draft. Working records and outward documents. The channel policy is a
  decision record and should stay one.
```

## 5. The honest negative

Two things this session did not do, stated because a triage that only lists
findings is a sales document.

First, **no open obligation moved.** `ENTROPY-LAYER-BRIDGE [O]` is exactly
where it was. If anything, the candidate makes the gap more visible rather than
smaller: it pins the number three ways in arithmetic and thereby isolates the
one step that is missing, which is the step from arithmetic to the
architecture's own tick. That is progress in clarity and not in the ledger.

Second, **the candidate breaks the lane's own ordering.** Every computation
here was run before any preregistration existed, because the session began as
a document repair and the arithmetic was a by-product. The candidate document
discloses that in full. A clean freeze-then-run, on a second architecture, is
required before any of it is promotable, and nothing here claims otherwise.

Two of the session's own conjectures fired and are kept: monotone convergence
of the periodic-point rate is false, and the window bound of section 3 is false
below `L = 20`. Three gates in the first draft of the candidate verifier were
also defective, found by re-reading rather than by the gates themselves: a
garbled bound statement, a tautology written as a gate, and a float inside an
assertion. All three were fixed before the run that is pinned. A verifier that
can contain a tautology is a reminder that gate count is not evidence.
