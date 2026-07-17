# Horizon 2..7 exact-closure lane

```text
STATUS:      NON-CANONICAL, NON-FORMAL, NO CLAIM STATUS.
LANE:        notes/entropy-selection-horizon7-exact
SCOPE:       the fixed-F_2, fixed-r=2 finite cell-sector ansatz only.
OBJECTIVE:   decide the ordinary horizon-7 block exactly and, only then,
             replay the full 625-block coupled horizon-7 construction.
```

This lane starts from the consolidated entropy recon. It does not open a
public probe and does not change Canon, the registry, the frontier, status,
release, or tag files.

## 1. Frozen inputs and unclosed observations

The repository-certified horizon-7 preparation closes the special block at
`260` in scale `48`. Its graph has `64` nodes, `116` base edges, and `12`
anchors. That result is an input to this lane and must not regress.

The current ordinary computation reports a rational LP value `192` and an
integer witness of cost `220`. These are development observations, not an
exact lower certificate and not a closed optimum. A floating-point solver's
zero reported gap is not evidence that rules out cost `219`.

## 2. Ordinary bundle to reconstruct

The formalized ordinary object must independently rebuild and verify:

```text
variables            320
pair records          580
anchor pins            60
spanning-tree edges   319
chords                261
pair-weight census    {1: 240, 2: 320, 4: 20}
pin-weight census     {4: 60}
commutation checks    580 * 3125 = 1812500
```

The horizon-7 holonomies, retraction, and pin hash must be computed from this
bundle. They may not be copied from the horizon-6 object.

## 3. Upper-bound gate

An exact assignment of cost `220` must be serialized and replayed without a
solver dependency. The replay must verify every constraint and lift the same
ordinary witness through all `624` ordinary fibres.

Finding any exact feasible assignment of cost at most `219` fires the target:
the value `220` is falsified, the counterexample is retained, and the threshold
is not moved silently.

## 4. Decisive lower-bound gate

Closure requires a standalone, exactly replayable certificate that cost at
most `219` is impossible. The intended certificate is a branch-and-bound
partition of the complete finite `F_5` domain:

1. branch children are disjoint and exhaustive inside their parent;
2. every leaf carries an exact rational LP dual bound strictly greater than
   `219`;
3. every dual inequality and objective value is checked with exact arithmetic;
4. the replayer reads a data-only certificate and has no solver dependency;
5. the certificate bytes and their digest are pinned by the tests.

Because the objective is integral, a verified leaf bound greater than `219`
proves a leaf lower bound of at least `220`. Floating-point bounds, an
unreplayed solver log, an incomplete partition, or an inexact leaf place the
lane on HOLD.

## 5. Coupled closure gate

Only after both ordinary gates pass may the lane combine the ordinary result
with the closed special block:

```text
624 * 220 + 260 = 137540,
137540 / 150000 = 6877 / 7500.
```

The joint replay must cover all `625` blocks, verify all-different constraints
at every node, and reproduce the exact total. Failure of the 624-fibre lift
blocks the coupled conclusion. Regression of the special value `260` is a base
inconsistency. The observed terminal `6 -> 7` cost `0` and marginal `30` are
witness diagnostics only, not closure gates.

## 6. Permitted conclusion and stop line

On success this lane may state only:

```text
ordinary optimum = 220,
coupled optimum  = 6877/7500,
```

inside the declared finite horizon `2..7`, fixed-`F_2`, fixed-`r=2` ansatz.
It may not claim an all-scale asymptotic, either branch of the summability
dichotomy, a summable, canonical, measurable, or regular selector, entropy or
measure transport, `C-ENTROPY-SELECTION-1`, `ENTROPY-LAYER-BRIDGE`, or any
Canon status.

## 7. Expected closure artifacts and validation

The minimal later artifact set is:

```text
horizon7_ordinary.py
horizon7_ordinary_solution.json
horizon7_ordinary_bnb.json
test_horizon7_ordinary.py
coupled_horizon7.py
test_coupled_horizon7.py
```

The data certificate must remain within repository policy limits. Closure
requires targeted horizon-7 tests, two byte-identical module reports, the full
entropy test suite, `git diff --check`, policy and repository unit tests,
Canon and ledger checks, and independent readback. One capable machine may
construct the certificate and a second ordinary machine may replay it. This is
not a formal two-architecture gate, and PIZE is not used.
