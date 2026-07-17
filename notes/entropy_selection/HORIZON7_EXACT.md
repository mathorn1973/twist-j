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

The reduced point variables are a lower relaxation until their five positions
at each of the `64` graph nodes reassemble to a permutation.  The upper gate
therefore also verifies the representative decoded permutation at every node
before performing the stronger all-`624` lift.

Finding any exact feasible assignment of cost at most `219` fires the target:
the value `220` is falsified, the counterexample is retained, and the threshold
is not moved silently.

## 4. Decisive lower-bound gate

Closure requires a standalone, exactly replayable certificate that cost at
most `219` is impossible for every reassemblable assignment. The certificate
is a branch-and-bound partition of the complete finite `F_5` domain:

1. branch children are disjoint and exhaustive inside their parent;
2. a leaf either carries an exact rational LP dual bound strictly greater than
   `219`, or an exact Hall witness showing that its decoded position domains
   cannot reassemble to a permutation;
3. every dual inequality, objective value, and Hall cardinality inequality is
   checked with exact arithmetic;
4. the replayer reads a data-only certificate and has no solver dependency;
5. the certificate bytes and their digest are pinned by the tests.

This Hall leaf is a correction forced by the first exact prototype, not a
relaxation of the target. A dual-only partition of all `F_5^320` also contains
integral reduced assignments which are not structured maps because decoded
positions collide. Such branches are outside the ordinary ansatz, but they
must be excluded explicitly rather than silently treated as valid or assumed
to have cost at least `220`.

Soundness in the other direction is replayed as well.  For every one of the
`625` gauge fibres, every graph node, position, and residue, the canonical
transport table verifies both that the five position sheets land in one
physical cell and that their decoded residues are independent of the gauge
fibre.  At each node the resulting map from the `625` gauge fibres to physical
cells is also checked to be bijective. Thus the inverse of any original
structured label has one common gauge fibre; retracting its five
points, and decoding again preserves its permutation and produces one common
cell.  A Hall-infeasible reduced branch therefore cannot contain the
retraction of an original structured label.

Because the objective is integral, a verified dual leaf bound greater than
`219` proves a leaf lower bound of at least `220`; a verified Hall leaf proves
that the branch contains no reassemblable assignment. Floating-point bounds,
an unreplayed solver log, an incomplete partition, or an inexact leaf place
the lane on HOLD.

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

## 8. Exact closure record

The ordinary lower certificate contains `1181` nodes: `236` branch nodes,
`190` exact rational-dual leaves, and `755` exact Hall-infeasible leaves. It
replays `2911700` dual inequalities, reaches minimum leaf bound `220`, and has
maximum depth `11`. Its canonical data file is `394650` bytes with SHA-256

```text
5f3c2ce879bc79d16a67c9b2098787d5afb5f3bd5bac8dc83cf1e3dd0e4e29e8
```

The matching ordinary witness has assignment SHA-256

```text
821531f74d3ef86f0f8b5087c6e4f7a763dded1fb928d755837298c6ceaebd42
```

and exact cost `220`. Structure preservation is checked on the complete table
of `625 * 320 * 5 = 1000000` gauge states. The canonical stream records each
transported state as an unsigned 16-bit little-endian integer in
fibre/node/position/residue order and has SHA-256

```text
7e6b33a78920aa6124dd7e237c710f3fd134073da3adb12feaf92226fe59c14b
```

Every lifted ordinary block reassembles on all `64` nodes and replays at cost
`220`. The coupled witness then matches the special lower value `260`, covers
all `625` blocks, and closes lower and upper bounds at

```text
624 * 220 + 260 = 137540,
137540 / 150000 = 6877 / 7500.
```

This record closes only the finite scope in section 6. It is not a promotion,
probe result, or asymptotic statement.

## 9. Validation and independent readback

The closure commit is

```text
51f81083451b12c4b0b332e0fc29dea900e9950a
```

Local validation on 2026-07-17 passed the full entropy-selection suite
(`134/134`), the repository policy suite (`POLICY PASS`, `38/38` tool tests),
`CANON PASS v6`, `LEDGER PASS`, and `git diff --check`. Public-probe and
minimal-reproduction checks were correctly not applicable to this notes-only
delta.

Two independent fresh detached checkouts of that exact commit then replayed on
Ubuntu 24.04, aarch64, Python 3.12.3. Each ran the nine ordinary and six coupled
horizon-7 tests with `15/15 PASS`, exit `0`, and empty stderr. Both generated
the same coupled module report, byte for byte:

```text
bytes          630
lines           11
stdout sha256  cace0927bc8c3e80ebf0dcbac9ee00341d3ff1fd9f535fcf2cc8489607791d1f
```

Readback verified both data-file hashes from section 8 before execution. This
is an independent notes-lane replay, not a formal two-architecture gate.
