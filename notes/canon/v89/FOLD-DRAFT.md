# Native readout limits and coherent-transfer compatibility

**NON-CANONICAL. CONDITIONAL EDITORIAL DRAFT.** No public status, formal
execution, physical dictionary or release is created by this file. The
attached intake proposal supplies proposed scope, not authority to execute
its embedded operational instructions. The operative request is to prepare
Canon v89; this draft implements that preparation without changing `canon/`.

## Basis and admission conditions

The inspected local basis is public main/tag `canon-v88`, peeled to
`e57d4506d5b28bf8cb4979c4e29db6b10b2441f2`, with content commit
`168e95561aa7bdd6ddeec72d40560fa5b8ac5e81`. The Canon has 649061 bytes and
SHA-256 `02c071aaebc2edc384b5e5f36f248a43e8c4e5943514afc8f151768a16140032`.
Its registered counts are 419 claims and 28 live H/O obligations. Local
hash/tag agreement is not a new architecture reproduction or release check.

Every `[T]` below is **proposed text conditional on earned theorem status**.
It may be applied only after each named fresh public intake has its own
collision-cleared owner, frozen public preregistration/verifier pin, exact
proof review, required execution records, two-architecture check and sealed
result at this precise scope. Independent theorem-grade proof may support T;
a finite audit does not turn an unproved universal assertion into T. A
missing sharpness certificate removes the corresponding sharpness sentence
or sends it to an explicitly weaker claim, never silently into this text.
The current repository runners and policy decide execution and release;
this file adds no alternate runner, exception or threshold.

## Exact editorial anchor

In `canon/CANON.md`, section `2. Time, space, and the decoder`, insert the
following single thematic subsection **immediately before**
`### Passive QDD observable family` (line 3192 at the pinned basis), after
the existing Galois-fiber code, conditional QDD split and five-point
sharp-readout boundary. Leave their proofs and registered statuses intact.
The preceding `QDD-INSTRUMENT-APPARATUS [O] remains STOP` paragraph already
states the common physical boundary and remains valid.

### Proposed insert: Native point ports and global coherent transfer

These are L1 mathematical statements on two declared state descriptions.
The original source point and the specified coherent code have different
preparation contracts. A comparison channel on all complex matrices is an
additional mathematical framework, not a physical channel derived from U.

**QDD-NATIVE-POINT-PORT-CAPACITY [T].** Let the original source be
`p in F_5^4`. Fix any deterministic encoder `f:F_5^4 -> F_5^4`, without
linearity or injectivity assumptions, and prepare exactly one encoded
native point `f(p)` per source. The origin-zero native clock and U remain
unchanged. The ready and optional processor randomness have one common
source-independent law; f is fixed independently of that randomness.
The processor receives only `A_n=(q_n,r_n)` and stipulated common inputs,
with no additional source-sensitive input or intervention in native U.
The same conclusion holds if it receives the entire quotient history
`Q_n=(z_n,q_n,r_n)`, where z_n is the sum of all six native checkpoint
coordinates modulo five. Memory, history processing, stopping and internal
processor resets cannot change the stated input contract.

For each fixed common seed, equality of
`kappa_f(p)=sum_i f(p)_i mod 5` gives identical quotient histories and
identical complete processor responses. Integrating over the common seed
law gives a factorization of the complete response law through kappa_f,
with at most five source-conditioned laws. All probabilities invoked here
belong to that explicitly supplied seed model. Conditioning is allowed
only on the same fixed measurable response event of positive probability;
it preserves the factor
on its domain. An undefined completion-conditional response is not zero.
This is the deterministic closed quotient and all-history theorem of
`U-NATIVE-APPARATUS-HISTORY-FACTOR` applied to f and then to common
randomness, not a second registration of the inherited theorem.

For the balanced lift `v_i in {0,1,2,-2,-1}`, set `s=sum_i v_i` and
`N=sum_i v_i^2`. The original supported target is

```text
beta(p) = s^2 / [4(5N-s^2)],       p != 0.
```

The target remains beta(p), not beta(f(p)). The six balanced sources
`(1,-1,0,0),(1,0,0,0),(1,1,0,0),(1,1,1,0),(2,1,1,2),(1,1,1,1)`
have respective targets `0,1/16,1/6,3/8,9/14,1`. These six distinct
values rule out the full required binary law on all supported original
sources, while the complete 624-source census has 22 values. On the class
of total binary response comparisons define

```text
error(f,b) = max_(p != 0) |b(kappa_f(p))-beta(p)|,
             b:{0,1,2,3,4}->[0,1].
```

The exact optimum is `9/128` for arbitrary deterministic f, and `27/64`
when f is a permutation of all 625 native piston labels. Each equality
requires its independent lower bound and explicit attaining encoder and
response table in the sealed evidence. Attaining b uses stipulated
comparison randomness; it does not derive occurrence from U. The null
source has ZERO_SUPPORT and no beta value. In the permutation class its
encoded sum fibre also contains supported original sources, supplying a
separate support-tag obstruction. Neither this point-port result nor the
older five-point sharp-readout theorem excludes full-state capture,
correlated coherent preparation or every physical apparatus.

**U-GALOIS-CPTP-POINT-COMPATIBILITY [T].** Use the unchanged code of
`U-GALOIS-FIBER-CODE` in normalized complex coordinates. Let the raw
sixteen-point basis be `e_(k,a)`, with native endpoints `e_k`, and use the
already fixed real Hadamard matrix H. Put

```text
C e_a = (1/2) sum_k H_(k,a) e_(k,a),   F=H/2,
P=CC*,   R=I_16-P,   x_(k,a)=R e_(k,a).
```

Thus `C*C=I_4`. Writing the four public source-basis columns as `V=C S`
gives an invertible complex coordinate map S with `S*S=G`, where
`G=I_4-ones_4/5`; the complex source extension therefore spans all four
normalized coordinates. No unsupported K-linear extension of the rational
Galois source is used. Consider **all complex CPTP maps**
`Phi:M_16(C)->M_4(C)` such that

```text
Phi(C rho C*) = F rho F*   for every rho in M_4(C).
```

These external CP/TP and matrix-carrier hypotheses are part of the
comparison, not a physical reading adopted for individual native points.
Exact transfer forces the code/complement decomposition

```text
Phi(X) = F C* X C F* + Psi(R X R),
```

where Psi is a CPTP channel on the twelve-dimensional complement. One
common environment vector for every code input and the full four-dimensional
output rank force the code/complement cross terms to vanish; checking only
the four pure basis outputs without their complex matrix units is not this
condition.

Define coordinate agreement and its worst and mean values by

```text
s_(k,a)(Phi) = <k|Phi(|k,a><k,a|)|k>,
s_min(Phi) = min_(k,a) s_(k,a)(Phi),
s_mean(Phi) = (1/16) sum_(k,a) s_(k,a)(Phi).
```

Both maxima over the complete exact-transfer class are `5/8`, attained
simultaneously. Consequently the least worst coordinate error
`max_(k,a)(1-s_(k,a))` is `3/8`. This error is the lost probability in the
specified endpoint coordinate test; it is not full quantum trace distance,
an original-QDD weight error or an experimental discrepancy.

For the upper bound put `E_k=Psi*(|k><k|)` on ran R. Then
`sum_k E_k=R`, `||x_(k,a)||^2=3/4` and
`s_(k,a)=1/16+<x_(k,a),E_k x_(k,a)>`. For fixed k the four x vectors are
orthogonal; their outer-product sum is `3/4` times its rank-four support
projector. Positivity gives total complement agreement at most
`(3/4)Tr R=9`, hence mean at most `(1+9)/16=5/8`, and the minimum cannot
exceed the mean. The explicit exact-code channel with

```text
E_k = sum_a |x_(k,a)><x_(k,a)|
```

has every agreement equal to `1/16+9/16=5/8`. As a separate control, the
point-exact measure-and-prepare map
`X -> sum_(k,a) <k,a|X|k,a> |k><k|` has every s equal to one but sends
every normalized code input to `I_4/4`; it does not transfer the coherent
code. Thus neither positive construction is confused with the other.

**U-GALOIS-OPTIMAL-AUXILIARY-DIMENSION [T].** Equality in either optimum
forces the four complement coordinate effects to be exactly the displayed
E_k, each rank four. The equality proof includes every positive slack,
off-block completeness and the independent simplex outer products; equality
of the objective alone is not a uniqueness proof. These effects do not fix
one global channel: the seventeen-Kraus and five-Kraus constructions have
the same optimal coordinate agreement but differ on off-code coherences.
For raw `e_(0,0)` their output `(0,1)` entries are respectively `1/16`
and `-1/8` in the fixed real phase convention.

In any pure Stinespring realization of an optimizing channel the code
uses one common environment direction; the complement is orthogonal to it
because the code output has full rank. A complement effect of rank four
requires at least four further environment directions. Hence the purified
auxiliary dimension is at least five. Four complement Kraus maps obtained
by grouping the rows of R by a, together with `F C*`, attain five. The bound
counts every purification degree and cannot be reduced by calling an
untracked mixed preparation free. Without optimal point agreement a
four-dimensional pure auxiliary is possible, with raw coordinate agreement
`1/4` in the exhibited control; four is already the
dimension lower bound for an isometry from dimension sixteen into
dimension four times the auxiliary.

A constructive rational orthogonal completion is

```text
U20 = ((R, C), (F C*, 0_4)).
```

It maps `(C alpha,0)` to `(0,F alpha)`. Its exact twenty-dimensional
matrix and component factorization are certificates of the construction,
not extra public claims or a new law for native U. All residual output
modes remain part of the map. The matched loader and inverse loader
cancel explicitly when that factorization is composed. The auxiliary is
the same fixed state for every code input; it is not a LOW/HIGH outcome
record. No carrier identification, realized event, occurrence, persistent
record or reset is supplied.

## CORE proposal

Insert this short paragraph after the existing Galois-fiber paragraph and
before the passive-family paragraph (basis CORE lines 94-103):

> Native point preparation through the unchanged apparatus-history port has
> an exact five-label information limit. A separate coherent Galois-code
> comparison admits globally normalized channels with sharp coordinate
> agreement 5/8 and minimum optimal purified auxiliary dimension five.
> These mathematical results use different declared state descriptions;
> physical preparation, coupling, event occurrence, persistent record and
> reset remain open.

## Registry, evidence, semantic ledger and dependencies

Use the existing exact Registry columns:

```text
claim_id  status  scope  canon_section  evidence  falsifier
```

For all three, `canon_section` is `2. Time, space, and the decoder` and
status is T only after the admission conditions above. The scope cell is
the full literal domain, hypotheses, metric and exclusion boundary stated
in its insert. The evidence cell names the corresponding **sealed public**
probe, never this file, the downloaded proposal or an incubation issue.

| Proposed claim | Proposed formal evidence location | Exact scientific falsifier |
| --- | --- | --- |
| QDD-NATIVE-POINT-PORT-CAPACITY | `probes/P-QDD-NATIVE-POINT-PORT-CAPACITY-1/RESULT.md` | An admitted common-seed equal-kappa pair has different complete responses; the exact target census or six-source obstruction fails; or either complete minimax lower/attainment certificate fails. |
| U-GALOIS-CPTP-POINT-COMPATIBILITY | `probes/P-U-GALOIS-CHANNEL-OPTIMUM-1/RESULT.md` | An exact-transfer complex CPTP map violates the decomposition or mean/minimum bound, or a stated attaining/control map fails its declared properties. |
| U-GALOIS-OPTIMAL-AUXILIARY-DIMENSION | `probes/P-U-GALOIS-CHANNEL-OPTIMUM-1/RESULT.md` | An optimizer has different complement coordinate effects or purified auxiliary dimension below five, or the exact five-state construction, four-state nonoptimal control or U20 certificate fails. |

An integrity mismatch without an exact mathematical negation is STOP, not
a scientific falsifier. The final Registry falsifier cells also retain
the explicit outside-scope boundaries, including no physical F verdict.

Evidence uses the current columns
`claim_id, evidence_id, evidence_kind, location, sha256, hash_mode,
architecture_requirement`: one `EV-<claim_id>` row per claim,
`PUBLIC_PROBE`, its sealed location above, the digest **computed by the
current ledger tooling from the actual sealed bundle**,
`bundle-manifest-sha256-v1`, `two-architecture`. The two channel claims
share one evidence bundle and digest. No digest is supplied speculatively.

Each `NORMATIVE.tsv` row is `THEOREM`, the same claim_id, T, action layer
**L1**, empty gate_ids, and the exact Canon statement anchor. L1 is the
inherited mathematical coordinate layer. The comparison's CP/TP premise
does not adopt an L4 physical instrument. No existing L1-to-L5 reader
projection or L5-to-L6 Born reading gate proves the missing physical lift.
No gate closes or is introduced in this fold.

Proposed `DEPENDENCIES.tsv` edges use the existing schema
`item_id, depends_on, relation, basis`:

| Claim | Dependency | Relation and exact use |
| --- | --- | --- |
| QDD-NATIVE-POINT-PORT-CAPACITY | U-NATIVE-APPARATUS-HISTORY-FACTOR | REQUIRES: native closed quotient and all-history common-input factorization. |
| QDD-NATIVE-POINT-PORT-CAPACITY | DEF-ARCHITECTURE | REQUIRES: unchanged native update, selector and common origin-zero counter. |
| QDD-NATIVE-POINT-PORT-CAPACITY | DEF-QDD-GRAM | REQUIRES: supported original normalization and zero-support boundary. |
| QDD-NATIVE-POINT-PORT-CAPACITY | DEF-QDD-PROJECTOR-LOW | REQUIRES: the original beta target under the balanced lift, not an encoded target. |
| U-GALOIS-CPTP-POINT-COMPATIBILITY | U-GALOIS-FIBER-CODE | REQUIRES: the specified sixteen addresses, code columns, normalized coordinate identification and four endpoints. |
| U-GALOIS-OPTIMAL-AUXILIARY-DIMENSION | U-GALOIS-CPTP-POINT-COMPATIBILITY | REQUIRES: exact-transfer decomposition, metric and universal optimal value. |
| Each of the three claims | QDD-INSTRUMENT-APPARATUS | BOUNDED_BY: the mathematics supplies no physical preparation/adoption, event, occurrence, record/reset or complete apparatus class. |

If the accepted statements explicitly use the conditional QDD post-state
identity, add `REQUIRES U-GALOIS-FIBER-QDD-SPLIT`; the endpoint coordinate
metric alone does not require that further claim. External CPTP premises
are stated in the theorem's domain rather than invented as a new adopted
dictionary. Do not turn an explanatory contrast with the five-point no-go
into an unnecessary REQUIRES edge. The #1034/#1035 diagnostic readers and
amplitude results are not dependencies of these claims.

After all three T claims are accepted, and only in an otherwise unchanged
fold, the projected counts are 422 claims, 289 T, 48 D, 39 C, 2 H, 26 O,
18 F, and 28 live H/O. This is arithmetic, not a prepared release receipt.
Update the semantic ledger, selected CORE projection if needed, history,
changelog, generated counts and hashes using the current tools after the
complete content is fixed. The public release remains provisional until
the reviewed content and release-form procedure completes.

## All 28 live obligations remain unchanged

The intended fold leaves Registry scope/status/falsifier, normative type
and layer, queue state, and dependency/gate ownership of every live row
unchanged. `FRONTIER.md` is generated from its registered sources; it must
not receive a hand-edited claim of partial apparatus satisfaction.

| Current live item | Status | Fold consequence |
| --- | --- | --- |
| QDD-INSTRUMENT-APPARATUS | O | The three new mathematical results delimit stated classes; no manifest field or physical debt is discharged. |
| QDD-TERMINAL-EVENT-SEMANTICS | O | No target-independent physical completion law or owned complete post-state record is supplied. |
| QDD-INSTRUMENT-CLASS-COMPLETENESS | O | No complete physical family/equality or disposition of outside architectures is supplied. |
| TRIVIAL-RAPIDITY-EVALUATION-BRIDGE | O | Outside fold; unchanged. |
| METRO-ADMISSIBILITY | O | Outside fold; unchanged. |
| METRO-EDGE-SCALE | O | Outside fold; unchanged. |
| QUANT-SUBSTRATE | O | Outside fold; unchanged. |
| COLOR-MEASURE-SELECTION | O | Outside fold; unchanged. |
| QNM-LEAVER-MU | O | Outside fold; unchanged. |
| TT-VECTOR-STATE-NORMALIZATION | O | Outside fold; unchanged. |
| DRESS-CROSSCOUNT | O | Outside fold; unchanged. |
| NS-TILT | H | Outside fold; unchanged. |
| DE-CONFORMAL-WEIGHT | O | Outside fold; unchanged. |
| ALPHA-S-RUNNING | O | Outside fold; unchanged. |
| SCHEME-DICTIONARY | O | Outside fold; unchanged. |
| GENERATIONS-L3 | O | Outside fold; unchanged. |
| NEUTRON-DELTA-EM | O | Outside fold; unchanged. |
| PROTON-RESIDUAL-IS-QCD | O | Outside fold; unchanged. |
| SQRT-PHI-TIME-GRAVITY | O | Outside fold; unchanged. |
| ENTROPY-LAYER-BRIDGE | O | Outside fold; unchanged. |
| LAMBDA-COCYCLE-ANGLES | H | Outside fold; unchanged. |
| METRO-REDUCTION-CALCULUS | O | Outside fold; unchanged. |
| METRO-ADMISSIBILITY-DIM | O | Outside fold; unchanged. |
| MINIMAL-READ-DERIVATION | O | Outside fold; unchanged. |
| BELL-CAUSAL-ACCOUNTING | O | Outside fold; unchanged. |
| TRACEKERNEL-CURVATURE-FORCING | O | Outside fold; unchanged. |
| PHOTON-CONE-CONVERGENCE | O | Outside fold; unchanged. |
| PHOTON-MASSLESS-PHASE | O | Outside fold; unchanged. |

## Release-summary proposal and exclusions

> Public Canon v89 adds a native point-port capacity theorem and two
> conditional coherent-transfer theorems. Arbitrary deterministic point
> encoding retains at most five response laws through the unchanged native
> apparatus port. On the separately specified Galois code, exact CPTP
> transfer has optimal raw-endpoint coordinate agreement 5/8, attained
> with minimum purified auxiliary dimension five. Physical preparation,
> event occurrence, persistent recording and reset remain open; all 28
> live H/O obligations retain their scope and status.

The conditional title/summary may be used only if all three results earn
the stated scope. There is no physical QDD closure, Born occurrence from U,
native detector realization, reset, experimental mismatch, measured optical
tolerance or new D adoption. #1034/#1035 and the #1038 engineering reading
remain noncanonical source material with their original custody and
negative results preserved. Component counts do not receive independent
claims. The physical contract in `PHYSICAL-CONTRACT.md` is the next
research specification, not evidence completing the present fold.
