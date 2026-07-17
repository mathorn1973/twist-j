# Horizon 2..6 preparation record

```text
STATUS:      NON-CANONICAL, PREPARATION GRADE. No claim status earned.
             The special block is closed exactly inside this prep module.
             The ordinary and coupled objects were outside its scope and
             are recorded separately by the subsequent closure in section 7.
MODULES:     horizon6_prep.py, test_horizon6_prep.py,
             test_marginal_2_4_to_2_5.py
BASELINES:   coupled_exact (2..4, optimum 417/1250, blocks {40:624, 60:1}),
             coupled_horizon5 (2..5, optimum 1459/2500, blocks {70:624, 90:1})
```

## 1. Scale correction (the truncation trap)

The `5 -> 6` refinement atoms carry exact edge weights `1/48`. The
horizon-5 integralization `int(weight * 24)` would therefore silently zero
sixteen level-6 edges. The correct scale for `2..6` is

```text
SCALE6 = 48 = lcm of all weight denominators,
OBJECTIVE_SCALE6 = 48 * 3125 = 150000.
```

In scale-48 units the closed baselines read: `2..4` scaled `50040`,
`2..5` scaled `87540`; per-block minima double to `{80:624, 120:1}` and
`{140:624, 180:1}`. Any horizon-6 code that reuses `SCALE = 24` is wrong
by construction; the prep module pins this as an assertion.

## 2. Structure of the 2..6 later graph (all machine-verified)

```text
nodes         44 = {level 3: 6, 4: 10, 5: 12, 6: 16}
              (equals the Thue-Morse factor complexity p(3..6) = 6,10,12,16,
              cross-checked independently in horizon6_prep)
pair edges    76 = 20 + 24 + 32 per transition
anchors       12, unchanged (they live at level 3); scaled weight 4
weights       scale-48 census {1: 16, 2: 56, 4: 4}
transports    all 76 are permutations of the 3125-state domain with the
              first-fibre F_5-shift form; shift census {0:50, 1:8, 3:16, 4:2}
gauge         43 tree edges, cycle rank 33, 25 nonidentity chord holonomies
orbits        exactly 625 orbits of size 5, five-fold canonical choice per
              orbit (the full-domain retraction EXTENDS to 2..6)
retraction    commutes on all 76 * 3125 = 237500 edge-state pairs and fixes
              all 60 anchor pins; the pin grid equals the horizon-5 grid
```

The retraction extension is the load-bearing prerequisite of the recon's
next-step 3 ("extend the exact coupled formulation to horizon 2..6,
preserving the full-domain retraction"). It is now machine-verified.

## 3. Special block CLOSED at 220 (scale 48)

Exact min-sum elimination with the deterministic min-fill order pinned in
`horizon6_prep.EXPECTED_MINFILL_ORDER` (maximum union scope 7, standard
induced width 6):

```text
coordinate optima   (44, 44, 44, 44, 44)   sum = 220 (lower bound)
reassembly          cyclic lift of the coordinate-0 assignment;
                    all-different at every node; replayed label-level cost
                    220 with 16 bad edges (ids pinned)
closure             lower = upper = 220; fathomed
```

## 4. Predict-then-test record: uniform marginal REFUTED

The frozen relation between the two closed baselines
(`test_marginal_2_4_to_2_5.py`):

```text
optimum(2..5) - optimum(2..4) = 1/4 exactly;
per-block marginal UNIFORM +30 (scale 24) for all 625 blocks;
first transition 209/2500 identical in both optima;
terminal transition of the 2..5 optimum exactly 0.
```

The uniform continuation to `2..6` predicted special `180 + 60 = 240`
(scale 48). The exact closure gives `220`: marginal `+40`, not `+60`.
The uniform-marginal hypothesis is refuted BEFORE freezing, by the cheap
block. Consequently no ordinary-block prediction is frozen here. The two
named candidate patterns, recorded for orientation only:

```text
ordinary marginal +60 (uniformity, now unsupported): block 200,
    total 624*200 + 220 = 125020, optimum 6251/7500
ordinary marginal +40 (special pattern):            block 180,
    total 624*180 + 220 = 112540, optimum 5627/7500
```

At preparation time the exact ordinary solve was left to decide; anything
between or outside those two diagnostics remained possible. Section 7 records
the later exact decision and the certificate method actually used.

## 5. Boundary of the preparation module

```text
1. Ordinary-block point bundle for 2..6 (the horizon-5 analogue lives in
   horizon5_ordinary.build_point_bundle): 220 variables, 380 pair
   equalities, 60 pins; chords 380 - 219 = 161.
2. Conditioned exact DP: the disjoint-copy base graph has standard induced
   width 6 (maximum union scope 7). The connected five-sheet ordinary lift
   must be measured rather than extrapolated from that floor (horizon-5
   needed width 8 with two conditioning variables). Peak-table feasibility
   must be checked before the run: at standard width 9 the union bag has
   `5^10` assignments and the outgoing message has `5^9`.
3. Structured coupled witness patch (the horizon-5 recipe: level-4 context
   patches propagated to level 5, plus the special cyclic offsets) and the
   block-cost census.
4. Zero-price dual assembly, root fathoming, certificate dataclass, and a
   neutral cross-platform readback under the frozen environment.
5. On closure, test the recorded transition-structure patterns: is the
   first transition still 209/2500; is the terminal transition still 0?
```

## 6. Reproduction

From the repository root, CPython 3.10+ without `-O`:

```text
python -m unittest discover -s notes/entropy_selection -p "test_horizon6*.py" -v
python -m unittest discover -s notes/entropy_selection -p "test_marginal*.py" -v
python -m notes.entropy_selection.horizon6_prep
```

The prep program writes no artifact and prints a NON-CANONICAL banner.

## 7. Subsequent exact closure

The later local closure does not change the preparation-grade authority of
this module. It builds the full ordinary `220/380/60` point bundle, verifies
the equivariant retraction on `1187500` edge-state pairs, and replaces the
infeasible dense-DP expectation by an exact integer local-polytope dual. The
dual has denominator 1, passes all 10600 feasibility inequalities, and has
objective 190. A matching assignment of cost 190 reassembles for all 624
ordinary blocks. Together with the independently closed special value 220,
one structured witness attains

```text
624*190 + 220 = 118780,
118780 / (48*3125) = 5939/7500.
```

The frozen witness has transition distances
`(313/1875, 573/1250, 1249/7500, 0)`: terminal zero survives, while the
earlier first-transition value does not. This remains NON-CANONICAL finite-
horizon analysis and earns no claim status.
