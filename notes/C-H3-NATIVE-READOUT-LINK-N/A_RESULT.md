# A result: one exact endpoint admits original-start preparation

NON-CANONICAL incubation. NO AUTHORITY. L1. Claim #2141.
Status: candidate-C, finite exact primary computation; PROTOCOL_DEVIATION
recorded below. No public promotion or completed joint blind confirmation.

## Verdict

Exactly one of the six frozen targets passes the strict original-start gate:
`(s,y,tag)=(107,3,1)`. It has a common four-slot radiation preparation at the
original absolute full cut 0, with all 25 prescribed incoming source reserves
recovered exactly. Unchanged native H3, together with the original source SWAP
at absolute full 114, attains the exact active-field target at relative full
107, absolute full 221. This is a preinstalled waiting probe. The calculation
does not establish spatial travel of the probe or a complete successor cycle.

The frozen contract is [PREREG-A.md](PREREG-A.md), with the pre-execution
[CLARIFICATION-A.md](CLARIFICATION-A.md). The exact primary evidence is
[DELIVERY.txt](DELIVERY.txt), especially its six `ORIGINAL_START_VERDICT`,
`SOURCE_BOUNDARY`, `LATER_SUMMARY`, and final `COMPLETE` records.

| Target `(s,y,tag)` | Strict original-start gate | Correct recovered source reserves | Later common-preparation full cuts | Earliest lead `s-t` |
|---|---|---:|---|---:|
| `(107,3,2)` | FAIL | 20/25 | 91 through 107 | 16 |
| `(107,3,1)` | PASS | 25/25 | 0 through 107 | 107 |
| `(93,0,2)` | FAIL | 20/25 | 93 only | 0 |
| `(93,0,1)` | FAIL | 20/25 | 93 only | 0 |
| `(89,0,2)` | FAIL | 20/25 | 89 only | 0 |
| `(89,0,1)` | FAIL | 20/25 | 89 only | 0 |

The later cuts in this table use second-run relative time, where absolute
time is `114+t`. Relative full 0 is therefore a separate diagnostic from
original absolute full 0. Every one of the 129 passing later preparations
also preserves bank and old-archive material along its stipulated suffix.
Later feasibility never changes a failed original-start verdict.

## Passing preparation and complete resource account

Coefficients are in the basis `(1,j,j^2,j^3)`. For the passing tag1 target,
`f=(3,2,1,1)`. At original absolute full 0, replace the following radiation
slots by whole-slot SWAP and retain every outgoing slot:

| Slot | Incoming value |
|---|---|
| `CORR(3,3)` | `(-3,-2,-1,-1)` |
| `CLK(4,3)` | `(3,2,1,1)` |
| `CORR(4,3)` | `(-3,-2,-1,-1)` |
| `CLK(4,4)` | `(3,2,1,1)` |

The minimal support has exactly four slots, with raw indices
`(87,110,111,114)`. The incoming stock is the same for every `(p,q)`.
Its full account `(Sm,Sr,H,Q)` is

```text
((0,0,0,0), (0,0,0,0), (24,0,-4,-4), 52).
```

The complete account of the field, prescribed source reserve, and probe stock
is

```text
((-12,24,42,18), (762,588,792,429), (54080,0,17894,17894), 90266).
```

In particular, `Q=90184+30+52=90266`: the unchanged field, incoming source
reserve, and incoming probe stock. The retained outgoing radiation has
`Q=3150`; it remains part of the compound state after replacement. These
complete totals must not be confused with the account of the active field
alone or with a mathematical pullback from which probe stock is omitted.

All 12 source material slots agree with the unchanged reference immediately
before and after the absolute full-114 exchange. The named strict archive
and bank windows pass. The stronger diagnostic also finds no material
disagreement at any full or post-C cut throughout the entire first and second
prefixes through the endpoint. Equality here is to the unchanged predecessor
at the same cut, not to a reset or constant material state.

There are five distinct original-full-0 evolving fields for this preparation,
ten distinct endpoint fields, and 25 distinct field-plus-source compound
states. Sharing equal field trajectories does not identify the 25 source
reserves. The exact local read condition at relative 108, absolute 222, was
checked separately as the known endpoint premise; the delivery comparison
itself ends at full 107. This passing tag1 amplitude is distinct from the tag2
probe used in the separately preregistered B lane. A supplies no composition
claim with B.

## Preserved failures

All five failed targets require a material change already at original full 0,
have at least one noncommon radiation coordinate, and fail both source
material boundary comparisons. Each recovers the wrong incoming source
reserve for all five inputs with `q=1`, and the correct reserve for the other
20 inputs. Their mathematical preimages and all failed clauses are retained
in the transcript.

For every failed target the first material counterexample is input
`(p,q)=(0,1)`, slot `(0,1,r0)`, at original full 0:

```text
expected (0,3,0,-3)
actual   (-1,0,-1,-3).
```

All six targets preserve the old archive in its strict comparison window.
The bank window fails for the five negative targets except `(89,0,2)`, which
still fails the initial-preparation and source-boundary gates. Thus a bank
window pass alone is insufficient. These negatives exclude only the five
specified exact targets under this preparation contract, not all possible
native readers or probe-delivery constructions.

## Execution and custody

This primary run used the publicly frozen source tree
`a3b3a735280be83cb27880ccb7b46cdd0c86af8a`; `delivery.py` was integrated without
byte changes in `65f27230f2cbb177f2a122261f04ddb860f7393b`.
The execution command, from the repository root, was

```sh
PYTHONHASHSEED=0 LC_ALL=C TZ=UTC python3 -B -u notes/C-H3-NATIVE-READOUT-LINK-N/delivery.py
```

The interpreter was Python 3.12.14 on Linux 6.18.57 x86_64. Exit was 0;
stderr was empty. Measured wall time was 21.988904 seconds, user CPU time
21.854631 seconds, system CPU time 0.091701 seconds, and maximum resident
memory 39024 KiB. These decimal values are runtime measurements, not
scientific approximations. `DELIVERY.txt` is the unchanged 154628-byte stdout.

| Artifact | SHA256 |
|---|---|
| `DELIVERY.txt` | `c2a04cc1f8d9f1dae34af73951fe5d2ac039de69a135956b990b350f2fed2dd3` |
| `delivery.py` | `5adf6a71eff327c794c4e2721303507b0b420fc9e2737c77d4ab0ef92b70c23b` |
| `model.py` | `7b2f12553efe075e97a3814e68b6402690d1f66c389e1a6c45694aeccd91365d` |
| `PREREG-A.md` | `31baa223b9bc63c97a72d229f0f40f08b474565a89d4d38746de7847785f8370` |
| `CLARIFICATION-A.md` | `4f37002bc0285a4e50123645f0597003e9b0ec121844c021eb55f9e09f4a69f5` |
| Native `reproduce/h3-referenced-record/verify.py` | `4553945d3bf32574ffd55de917859497e9644394f506aaf01ff9492adb8eeedd` |

The primary audit includes 1780 unchanged-prefix ticks, 22880 inverse ticks
with both native compositions checked, 45760 inverse-cut account checks,
150 source SWAP account/inverse checks, 3310 radiation SWAP account/inverse
checks, and all 25 strict delivery compound checks for the passing target.
The transcript retains all ordered field and compound hashes and the
remaining counters. Source and thresholds were not changed after execution.

## Protocol deviation and remaining scope

`PREREG-A.md` requires freezing both `delivery.py` and the standalone
`break.py` before execution. The primary run occurred after its own public
source freeze but before the standalone checker freeze. This ordering did
not satisfy that requirement. The output is preserved without relabeling
the chronology. Any later separately written checker run is recorded as
reproduction, not as completed joint blind confirmation. The owner records
the package-wide chronology separately.

This local x86_64 execution alone satisfies neither a two-architecture gate
nor a promotion gate. The result is a bounded candidate-C compatibility
witness for 25 actual inputs. It does not supply an autonomous source loader,
the 50 crossed donor/background successor test, restoration of source and
worker to a reusable ready state, unlimited reuse, or physical occurrence.
The predecessor's failed restoration and continuation claims remain intact.
