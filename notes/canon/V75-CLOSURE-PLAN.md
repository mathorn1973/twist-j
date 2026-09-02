# V75 closure plan

**Status:** `NON-CANONICAL / PLANNING NOTE / NO AUTHORITY / NO STATUS CHANGE`

**Date:** 2026-09-02

This note proposes what a Public Canon v75 fold can close and what it must
leave open. It is not a probe, preregistration, result, promotion package,
evidence record, or release instruction. It creates no claim, status, scope,
dependency, gate, or evidence credit. Every item below moves only through the
ordinary reviewed fold procedure in `POLICY.md` and `AGENTS.md`.

## 1. Authority at writing

```text
STATE:           ACTIVE
CANON:           Public Canon v74
AUTHORITY:       mathorn1973/twist-j main
TAG:             canon-v74
CONTENT_COMMIT:  2561f7dcadcbbf683ce7b36219ea67378d879a5a
CANON_SHA256:    2db550cb68f6f4ee33b9194f1f6b3bc4d8fec19cd79e79a702c5357577a92c0e
CANON_BYTES:     389246
BASE_MAIN:       dfc21dfe97ed69ebe15ea9af1a7922bb666854f8
REGISTRY_ROWS:   352
LIVE_H_O:        31
CHECKERS:        check_canon PASS, check_ledger PASS, check_policy PASS
```

Updated 2026-09-02 after the merges of PR #779 (maintenance), PR #784
(`P-QDD-DIRECT-RECORD-E-NONCONGRUENCE-1`) and PR #785
(`P-TM-CHECKPOINT-HULL-STABLE-IMAGE-1`) into `main`. The v74 content
identity is unchanged; only the base `main` commit and the probe inventory
moved.

## 2. Verdict

Public `main` already carries five merged probes after v74 whose
`candidate-T` results were never registered. Together with the one headless
probe still in review, that is one honest "earned results" fold in which
statuses actually move.

The foundational wording package
`notes/canon/PROMO-FOUNDATIONAL-SPLIT-V75.md` cannot share that fold: it
requires byte-identical `REGISTRY.tsv`, `FRONTIER.md`, `NORMATIVE.tsv`,
`DEPENDENCIES.tsv`, and `GATES.tsv`. Proposed split:

```text
v75   earned-results fold: registered theorems and one gate disposition
v76   framework-wording fold: the already drafted A0 and CORE split,
      with its "v75" references renumbered to "v76"
```

## 3. Content of the v75 fold

### 3.1 Already merged on main, unregistered

| Probe | Local status | Proposed rows | Effect |
| --- | --- | --- | --- |
| `P-JIPC-WP3D-QPOS-MELLIN-1` (PR #778) | candidate-T / L1 | 1 T | pure addition |
| `P-MATTER-SCALAR-TEMPORAL-CHARACTERISTIC-1` | candidate-T | `MATTER-SCALAR-TEMPORAL-CHARACTERISTIC`, `MATTER-SCALAR-BRANCH-CLASSIFICATION`, `MATTER-SCALAR-MASSIVE-GERM` | opens the massive-kinematics lane as a separate lane |
| `P-PHOTON-HERM2-GERM-AND-GLOBAL-OBSTRUCTION-1` | candidate-T | `PHOTON-HERM2-TANGENT-GERM`, `PHOTON-HERM2-SEPARATED-GLOBAL-OBSTRUCTION`; `PHOTON-MASSIVE-SCALAR-GERM` duplicates the matter row | the only gate disposition available |
| `P-TM-CHECKPOINT-HULL-STABLE-IMAGE-1` (PR #785, issue #780, merged 2026-09-02) | candidate-T / L1, two-architecture PASS | 1 T / L1 | pure addition; no gate, no measure, no physical carrier |
| `P-QDD-DIRECT-RECORD-E-NONCONGRUENCE-1` (PR #784, issue #782, merged 2026-09-02) | candidate-T / L1, two-architecture PASS | 1 T / L1 | negative boundary for pointwise record transformation only |

### 3.2 In review, fold only after merge

| Probe | Public state | Proposed row |
| --- | --- | --- |
| `P-TM-FOURPHASE-HULL-NONDESCENT-1` (PR #783, issue #781) | two-architecture PASS, unmerged | 1 T / L5 |
| `P-TM-CORR-ZEROS-1` (PR #696, issue #694) | two-architecture PASS since 2026-08-31, unmerged | optional 1 T / L5; promotion note already in `notes/canon/PROMO-C-TM-CORR-ZEROS-1.md` |

Neither of these moves a gate or an `O` row. The dynamic reversor corollary
built on the now public stable-image result stays outside v75.

### 3.3 The one gate disposition

`GATE-L4-L5-PHOTON-CONE-IDENTIFICATION` does not close as written: the
Herm2 probe proves exact agreement of the quadratic germ, while the natural
global separated equivariant class is empty and the arbitrary total class is
unclassified. Following `notes/canon/PHOTON-PROGRAM-CLOSURE-V74.md`, the fold
may replace the gate by two gates:

```text
GATE-L4-L5-PHOTON-CONE-GERM             closes AGREE on PHOTON-HERM2-TANGENT-GERM
GATE-L4-L5-PHOTON-GLOBAL-CARRIER        remains OPEN_LIFT, research lane
```

`PHOTON-CONE-CONVERGENCE [O]` then receives a `SCOPE_CHANGE` narrowing it to
the global carrier question and stays `O / ROOT / STOP`. This is an owner
governance decision recorded in `HISTORY.tsv`, not an automatic closure.

### 3.4 Indicative count movement

```text
claims   352 -> 361 or 362
T        225 -> 234 or 235
gates     14 -> 15
```

## 4. Deliberately left open by v75

- `PHOTON-MASSLESS-PHASE [O]`: the production preregistration at `t=1` is
  frozen, but the F1 through F3 execution firewall does not yet hold and no
  production output exists. Nothing enters v75.
- Dynamic QDD reversor corollary, invariant measures, and any physical
  reading: a separate later fold, and the corollary depends on `X_stab`
  first becoming public.
- `GENERATIONS-L3`, `QUANT-SUBSTRATE`, `TT-VECTOR-STATE-NORMALIZATION`:
  `READY` roots with predefinition notes only and no probe; PRs #693 and
  #695 are far behind `main`.
- `ENTROPY-LAYER-BRIDGE [O]` and the QDD apparatus block: no new input.
- `PHOTON-KAPPA-LEMMA [F]`, `PHOTON-WINDOW-PROOF [F]`: terminal, not
  reopened.

## 5. Order of operations

1. PR #779 (maintenance: status-separation reproduction count 23 to 24),
   PR #784 and PR #785 are merged as of 2026-09-02.
2. Merge PR #786 (legacy disposition) and PR #787 (intake notes) with no
   status movement.
3. Review and merge PR #783; decide PR #696. Each requires its own manual
   scope and security review.
4. Open `synthesis/canon-v75` from `main` after those merges. Exactly two
   frozen commits: the complete content fold, then a release-form commit
   changing only `STATUS.md`, `README.md`, and `CITATION.cff`.
5. Content fold: new rows in `REGISTRY.tsv`, `EVIDENCE.tsv`,
   `DEPENDENCIES.tsv`, `HISTORY.tsv`; the gate split in `GATES.tsv`;
   Canon text; regenerated `FRONTIER.md`, `STATUS_COUNTS.tsv`,
   `SHA256SUMS`; extended `reproduce/status-separation`.
6. Tag `canon-v75` only after public readback; publish assets only after tag
   readback passes.
7. Open v76 immediately afterwards with the framework wording and a
   byte-identical Registry.

## 6. Decisions reserved to the owner

- **Massive-germ duplicate.** `MATTER-SCALAR-MASSIVE-GERM` and
  `PHOTON-MASSIVE-SCALAR-GERM` prove the same statement from two probes.
  Proposed: one registered row, both probes cited as evidence.
- **Gate split.** Replacing the cone gate changes a decision condition; it
  does not satisfy the existing one. It must be an explicit owner
  disposition.
- **TM-CORR-ZEROS registration.** The probe states `CANON UNCHANGED` and
  claims no priority. Registration is legitimate but optional.

## 7. Breadth housekeeping with no scientific cost

- Rebase or close stale PRs #693, #695, #650, and #595 with a pointer.
- Close claim-lock issues whose probes are merged and folded in v73
  (#716, #721, #724, #731) after verification; #780 and #782 once their
  merged probes are folded; #694 after the PR #696 decision.
- Nine registry rows carry one-architecture evidence only
  (`ALPHA-VALUE-DIGITS`, `HYPERPLANE-BOUNDARY-REALIZATION`,
  `KERNEL-CELL-COMPONENTS`, `TIME-QUANTUM-TOWER`, `SILVER-RING-FACTS`,
  `COULOMB-GREEN-COMPUTATION`, `MONOPOLE-COST`, `KAPPA-SHAPES`,
  `METRO-REDUCTION-ARROWS`). Replaying them through the two-architecture
  workflow is the cheapest ledger-debt reduction. Not for v75.

## 8. Stop conditions

STOP if public authority or any normative input moves before the fold; if
any probe in section 3.2 is folded before its merge; if the foundational
wording and the scientific rows are combined in one fold; if a candidate row
is registered above the status its probe earned; or if the gate split is
presented as satisfying the existing decision condition.
