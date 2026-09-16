# P-QDD-U-NATIVE-READBACK-1 preregistration

Status: FORMAL PREREGISTRATION / RESULT-EXPOSED / PROOF-FIRST / L1 ONLY

Owner: A. M. Thorn. Date: 2026-09-06.
Public claim: [issue #859](https://github.com/mathorn1973/twist-j/issues/859).
Branch: `probe/P-QDD-U-NATIVE-READBACK-1`.
Directory: `probes/P-QDD-U-NATIVE-READBACK-1/`.

The formulas, witnesses and predicted finite counts were obtained in private
work before this preregistration. Earlier private scripts were executed and
their outputs were inspected. This is a formal replication and independent
proof audit of exposed results, not a blind prediction. The newly authored
accepted verifier has not been executed or imported before this pin. Only
static reading, source comparison, syntax parsing and written algebra review
precede it. The private implementation and its logs are not dependencies or
public evidence of this probe.

The complete `PREREG.md`, `PROOF.md` and `verify.py` are frozen together in
one commit, pushed and read back before the first formal execution. Candidate
theorem status depends on the written proof and review; no public Canon status
is earned by the preregistration or automatically promoted by its test output.

## Authority and inherited results

```text
STATE: ACTIVE
CANON: Public Canon v78
AUTHORITY: mathorn1973/twist-j main
BASE_COMMIT: a6e5e0fa21fbdb34213b035b889de12d9923a828
TAG: canon-v78
TAG_OBJECT: 89d026633a295520bfa8b27d4a5d40f115cacb0b
TAG_TARGET: a6e5e0fa21fbdb34213b035b889de12d9923a828
CONTENT_COMMIT: 767b136713ae12f5f30869642852dcb8a3f671b0
CANON_SHA256: 82b29c75eb007c71d73dc33e63270d0e0895fdf41886499fcf79b928826855b5
CANON_BYTES: 473631
```

The five normative files matched the public hash manifest. Both architecture
jobs and aggregate `check` passed at this base in
[run 34019197885](https://github.com/mathorn1973/twist-j/actions/runs/34019197885).
Publication succeeded in run 34019253710. The collision audit covered all
114 live remote heads explicitly, 27 open issues, 11 open PRs, the full pinned
tree and registry. It found no matching identifier or direct new-target lock.

The following public T results are inherited, not new discoveries here:

- `KERNEL-Z6-SYNCHRONIZATION`, evidence
  `P-KERNEL-Z6-SYNCHRONIZATION-1`, issue #160: origin-zero synchronization at
  tick three and exactly five preimages, one from each initial phase sheet.
- `TM-SHEET-SYNCHRONIZING-GRAPH`, issue #417, and
  `TM-CHECKPOINT-HULL-STABLE-IMAGE`, issue #780: synchronizing language and
  sharp length-nine stability on their stated carriers. No new or sharper
  arbitrary-start synchronization bound is proposed here.
- `QDD-DIRECT-RECORD-E-NONCONGRUENCE`: complete QDD record equality exactly
  up to common piston sign, giving 313 records. Its current-record question
  differs from the old-record recovery question below.
- `CARRY-J-CHECKPOINT` and `FIRED-COMMUTATOR-NOGO`: the existing clock and
  tail-generator restrictions remain in force.

The sealed `P-QDD-INSTRUMENT-U-INDUCED-1`, issue #395, pin
`45cad3384c69d7f2e187d88e63c10ecbad965f0d`, already establishes native
coupling in its distinct finite instrument audit. Its 180 record maps and
five delays are not used to infer the universal statement in this probe.
The reserved U-INDUCED-2 lane is not reused. No sealed probe is resumed.

## Field 1: equation

All equations and their proofs are part of the simultaneously frozen
[PROOF.md](PROOF.md). The conjunction has separately reported components.

**A. Native chart.** For `n>=3` on
`X_n={x in F5^6: sum(x)=4-3 theta_(n-1)}`, define

```text
theta_n = popcount(n) mod 2
S(M) = M-floor(M/2)+floor(M/4)-...
t_n = (-1)^(n-3), h_n = (-1)^(n+theta_(n-1))
N_n = S(floor((n-1)/2))-1
L(n,x) = (t_n(p1+p1p), t_n(p4+p4p),
          h_n(p1-p1p-2), h_n(p4-p4p-1), t_n*r-N_n) mod 5.
```

The displayed inverse in PROOF is a bijection `F5^5 -> X_n`, and
`L(U(n,x))=L(n,x)`. Thus a synchronized jump to any `m>=n` is
`encode(m,L(n,x))`. Evaluating the clock formula takes `O(log m)` integer
arithmetic steps; this does not assert constant-cost arithmetic or faster
physical time. The universal identity is proved, not inferred from samples.

**B. Native readback obstruction.** For an initial record `rho` on a
preparation set `A subset F5^6`, a decoder of the current native checkpoint
and clock recovers `rho(x0)` at any fixed `n>=3` iff `rho` is constant on
every `F3` fiber intersected with A. The actual complete registered QDD head
record violates this condition on the full set of supported heads: the one-tick merged
heads `(4,1,0,0,0,0)` and `(2,1,1,2,1,0)` have normalized LOW values
`0` and `9/14`. The registered decoder whose input retains the entire orbit
head is unaffected.

**C. Minimal additional state.** The conditional extension
`U'(n,x,c)=(U(n,x),c)`, initialized with c according to initial-phase classes
`{0},{1,2},{3,4}`, recovers all five original QDD fields at every time.
Three distinguishable additional states are necessary, as the common
tick-three checkpoint `(0,0,0,1,0,0)` has three supported predecessors with
LOW values `1/16,1/256,3/8`. A five-state saved initial phase instead recovers
the complete head. Its five-state lower bound is a direct corollary of the
inherited five-to-one theorem, not a new fiber theorem. Bijectivity applies
only to correctly initialized reachable full-head slices; neither extension
is claimed globally injective on the unrestricted Cartesian carrier.

**D. Exact preparation bound.** Among 3125 F3 fibers, complete-QDD record
multiplicities are `(4,1)` in 125 fibers and `(2,2,1)` in 3000 fibers.
Consequently the maximum unaugmented preparation set admitting exact
complete-record readback has `125*4+3000*2=6500` heads. The same maximum
is attainable using only supported heads. PROOF derives these counts by
two independent affine constraints, as well as the general factor criterion.

## Field 2: code

One newly authored standard-library `verify.py` uses integers and exact
`Fraction` arithmetic, with no private imports, runtime network, file writes,
floating tolerances or downloaded data. Its independent checks compare
coordinate generators against separately stated affine matrices, scalar
QDD formulas against matrix contractions, and the chart against direct ticks.
Caching the 625 piston records changes no equality or domain.

The accepted finite audit is frozen as follows:

1. All 15625 heads and all five generators: coordinate/matrix equality and
   involutions; both phase tables.
2. All 625 piston tuples: scalar/matrix equality of all five QDD fields,
   sign equivalence, zero support and the inherited 313 distinct records.
3. The switch-count formula at every integer M from 0 through 10000,
   compared with literal adjacent Thue-Morse bit changes.
4. All 3125 labels at each of these 28 times: every integer from 3 through
   18; `31,32,33,63,64,65,255,256,257,2**127,2**127+1,10**80+7`.
   Check both chart inverses, phase and one native transition.
5. All 15625 origin-zero heads at every snapshot n from 0 through 17:
   direct evolution, closed-form tail, saved-phase full-head recovery and
   saved-class complete-QDD recovery, including transient n=0,1,2.
6. All 3125 F3 fibers and all five phase candidates: exact preimage
   structure, complete-record class multiplicities, affine equality
   classification, and construction/count of a supported 6500-head domain.
7. The explicit supported two-head collision and three-record lower-bound
   witness stated in B and C, with all fields compared exactly.
8. At `10**1000+123`, a fixed deterministic representative label set defined
   in the accepted code: inverse, one-step invariance and jump composition.

The finite clock samples audit the all-clock proof. They do not exhaust the
infinite counter. Arbitrary-start transient optimization, malformed-input API
behavior and physical memory implementation are not claims of this verifier.

Audit item 1 supplies the first two code groups; items 2 through 8 each
supply one further group, for nine required groups. The loop bounds predict
1533811 exact comparisons in total before execution. This is an audit count,
not a count of independent experiments.

Scientific stdout is a deterministic ASCII JSON object with a final LF.
It names each completed component, check and failure counts, exact first
counterexamples when present, and aggregate PASS or FALSIFIED. A completed
audit exits zero even when it reports a mathematical falsifier; exit zero
means completed execution, not mathematical success. JSON FALSIFIED names a
failed frozen computational conjunction; a reference or implementation
disagreement is not itself a theorem counterexample. The scientific RESULT
must apply the independent mathematical/integrity classification below.
Unexpected exceptions
or failure to complete every component are execution defects, not PASS.

## Field 3: carrier or data

Native carrier: `Omega=N0 x F5^6`, coordinate order
`(p1,p4,p1p,p4p,q,r)`, phase `z=sum(x) mod 5`, generator selection
`(z+2 theta_n) mod 5` in the order `(a,b,c,d,e)`. The five full affine
formulas are in PROOF. All native equalities are exact modulo five.

The QDD carrier is the registered family of origin-zero forward orbits with
the initial head retained. Let `v=ell(p)` with `ell=(0,1,2,-2,-1)`,
`s=sum(v)`, `G=I-11^T/5`. The complete record contains support, mass
`v^T G v`, ordered weights `(s*s/20, v^T v-s*s/4)`, density
`v v^T G / mass` and their normalized ordered weight pair. At zero support
both denominator-bearing fields have `ZERO_DENOMINATOR`; otherwise use the
registered `DENSITY` and `NORMALIZED` tags. Equality is equality of the full
five-field record, not only of the normalized LOW value. The domain contains
15625 heads, 15600 supported. No probability-of-occurrence interpretation
is added to these algebraic weights.

Readback takes the later checkpoint, its actual clock, and only the declared
finite auxiliary label if present. It is not allowed the original head as an
unreported input. The conditional label is initialized from that head and
adds state; it is not a new native coordinate or an independently writable
history. The 6500 optimum is over preparation subsets, not a physically
preferred preparation selection.

Public source identity is frozen at BASE_COMMIT above:

| Path | Bytes | SHA-256 |
| --- | ---: | --- |
| `canon/CANON.md` | 473631 | `82b29c75eb007c71d73dc33e63270d0e0895fdf41886499fcf79b928826855b5` |
| `reproduce/census/verify.py` | 8127 | `1df13ba2218acaa9cf48dab2480e6472b107691aac868618dc7f91d511718a5c` |
| `reproduce/qdd-route-a/verify.py` | 12498 | `fbd1da8b9945033ad03794c9960341a457640d636929c9b3a030e0898b0fb464` |
| `probes/P-QDD-DIRECT-RECORD-E-NONCONGRUENCE-1/PREREG.md` | 12860 | `22f6203938d56819bd175af4ce3458d7f51f13ec5180d3f0fc88ec4c7f8401bf` |
| `probes/P-QDD-DIRECT-RECORD-E-NONCONGRUENCE-1/verify.py` | 9403 | `00bef39293ce531f3e9e72ea4389ab1e47a9a4ca8565347f1d1f1ac227a35a90` |

The Canon fixes U, the QDD head map, its accepted direct/factor equivalence
and the inherited theorems; census provides a second public U transcription.
The qdd-route-a reproduction grounds `QDD-ALGEBRAIC-FACTORIZATION`;
the noncongruence probe grounds inherited complete-record sign equality.
The verifier is self-contained and does not execute these source files.

## Field 4: systematics and frozen procedure

Source formulas and exact record typing are reviewed against the pinned
public text. Proof review is independent of implementation review. The main
risks are wrong generator ordering, clock shifts, omitted density or mass,
mixing a head-retaining orbit with a late checkpoint, and silently treating an
initialized extension as native memory. The separate reference formulas,
exhaustive head/fiber census, explicit transient and collision cases, and
written carrier restrictions address these risks.

Private result exposure, public prior art and the stronger known
synchronization bounds remain disclosed regardless of outcome. The proposed
new mathematical scope is the explicit chart and the target-specific old-QDD
memory/preparation results. Even their success supplies no occurrence law.

After static review, commit and push only PREREG, PROOF and verify.py; record
the immutable commit, parent, hashes and public readback. Then use a separate
clean Linux checkout fetched from that exact public pin, working from its
repository root, with `LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0
PYTHONDONTWRITEBYTECODE=1`, and run:

```text
python3 probes/P-QDD-U-NATIVE-READBACK-1/verify.py
```

Capture stdout and stderr separately. Record neutral OS, architecture,
Python version, exit code, byte counts and SHA-256 in RUN; add exact stdout
as EXPECTED and the scientific disposition as RESULT. Check cleanliness
and unchanged pinned bytes before and after execution. The required PR
workflow independently reruns the same accepted code on x86_64 and aarch64
with Python 3.12 and compares byte-identical output to the single EXPECTED.

The pin is never amended, rebased, squashed or force-pushed. Later commits
add the records; they do not adjust equations, test domains or thresholds.
Source/hash drift or an incomplete/defective execution is an integrity STOP.
If no valid gate completed, preserve the original pinned files and close the
consumed identifier as ABANDONED under POLICY; any corrected experiment
requires a fresh identifier and pin. A completed mathematical falsifier is
preserved with its exact output and scientific result, never abandoned or
removed to recover a passing result.

## Field 5: failure threshold

Zero mathematical mismatches are tolerated. The following exact
counterexamples falsify the named component:

- An admitted chart inverse, phase or invariance identity fails (A).
- A conflicting initial record factors through the native F3 map, or the
  displayed collision does not have the stated merged image and distinct
  records (B).
- A correctly initialized three-class readback returns a different original
  complete record; fewer than three records occur in the lower-bound
  witness; or saved-phase recovery fails on its admitted domain (C).
- The derived fiber multiplicities are false, a factor-compatible preparation
  set exceeds 6500, or the supported construction fails to attain it (D).

Every component must complete and pass for aggregate PASS. An implementation
mismatch must be checked against the written mathematics before it is called
a theorem counterexample. Source drift, code changes, skipped groups,
exceptions or a hidden cross-layer premise are integrity/protocol failures;
they cannot earn PASS or be relabelled as a mathematical discovery.

## Field 6: action layer

L1 only. A successful proof audit supports a native mathematical chart, a
negative universal current-state readback result, and a positive conditional
extension with exact memory cost and preparation bound. The conditional
positive does not reverse the native negative.

No realized event, independent occurrence measure, physical pointer,
protected working-memory interaction, Born frequency, consciousness claim,
O1/O2a/O2b closure, or completion of the matter/geometry/clock decoder is
asserted. No L1-to-L5/L6 bridge or public Canon promotion is performed by
this probe. Those obligations retain their registered scope and status.
