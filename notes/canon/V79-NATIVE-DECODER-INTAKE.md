# Native decoder: proposed seven-row intake

**NON-CANONICAL / review input for Public Canon v79.** This document
proposes six exact mathematical rows and one bounded implementation row.
It edits no sealed evidence, reports no new scientific execution or import,
and creates no physical obligation. Public Canon v78 remains the
authority until the separate reviewed fold is adopted.

The intake uses four unchanged public bundles:

| Bundle | Public pre-execution pin | Proof surface |
| --- | --- | --- |
| `P-QDD-U-NATIVE-READBACK-1` | `82da7e5aba4d22fe570e5d8432cbcc325077d451` | `PROOF.md` |
| `P-U-NATIVE-MEMORY-EVENT-1` | `1251e1d2853c913f7fc889418cc1f3d2ee8ba8dc` | `MEMORY-PROOF.md`, `CLOCK-PROOF.md`, `FREQUENCY-PROOF.md` |
| `P-U-FINITE-HISTORY-EVENT-1` | `f5ba76c60a8aac1a5d3dec80634fcf040be23496` | `CLOCK-PROOF.md`, `MEMORY-PROOF.md`, `PROOF.md` |
| `P-U-PREPARATION-EVENT-RECORD-1` | `19b69962ba0365d39546029a3f02dd7e05e38ba5` | `NATIVE-PROOF.md`, `INCIDENCE-PROOF.md`, `PROOF.md` |

Each bundle's `EXPECTED.txt`, `RUN.md`, and `RESULT.md` retain its finite
audit and custody. The universal results below rest on the written exact
proofs, not extrapolation from those finite comparisons. The retrospective
[preparation/record audit](../C-U-PREPARATION-RECORD-FALSIFIER-AUDIT-N.md)
corrects scope and layer presentation without changing a pinned file.

Finite native dynamics and symbolic state constraints are L1. All long-run
reader frequencies are L5, through the explicitly adopted mathematical
stream and named projection below. This supplies no physical apparatus
realization, exclusive occurrence, trial ensemble or L6 probability law.

## Proposed DEF-NATIVE-READER-STREAM: L5 definition

The complete source is a pointed origin-zero U-orbit ((n,x_n)) and a fixed
descriptor (kind,L,Sigma,f,parameters). Sigma is a named finite alphabet;
L is positive for window kinds. The kind specifies exactly one input:
checkpoint x_n in X14; decorated checkpoint (x_n,theta_n); the legal
past-and-current length-L TM word; or the legal length-L decorated
checkpoint word on the declared synchronized carrier. Checkpoint domains
contain every stated checkpoint; clock-word domains contain every legal
TM factor; native-word domains contain every legal factor of the declared
synchronized carrier. The fixed finite function f is total on that domain.

The descriptor and parameters remain unchanged throughout the orbit.
A rational constructor parameter or retained source vector is explicit
input; its acquisition is an additional premise, not performed by the
projection. The index n labels the stream but is not an argument supplied
to f. Descriptor equality is literal equality of all these data.

Output at every natural index has precisely (status,symbol):
(UNAVAILABLE,NONE) before warmup and (VALUE,f(input)) afterwards.
Checkpoint kinds begin at n=3, clock windows at n=L-1, and wholly
synchronized native windows at n=L+2. Output equality is literal
tag-and-symbol equality at every index. No shift quotient, fractional
symbol allocation, changing reader, or feedback to U is allowed.
Off-domain runtime calls return ERROR with no accepted symbol and are
outside the legal-orbit source domain. ERROR, UNAVAILABLE and SILENT are
distinct. Administrative tags are not accepted symbols. Cell/archive
state is a separate resource, not an implicit stream field.

Adopt GATE-L1-L5-NATIVE-READER-STREAM, owner DEF-NATIVE-READER-STREAM,
endpoints L1 to L5, kind DEFINITION_PROJECTION. This definition owns the
named L1 architecture, chart, invariant/recurrence, phase and conditional
incidence inputs. Their crossings occur through this gate. The L5
spectrum row depends on this L5 definition rather than adding ungated
direct L1 dependencies. It is a total mathematical projection, not a
physical realization gate or a new physical O owner.

Symbol density is its count divided by available prefix length when the
limit exists. Acceptance for LOW/HIGH/SILENT is LOW or HIGH; an accepted
limit is asserted only at positive limiting acceptance density. Empty
acceptance is UNDEFINED. Conditioning on a bit uses the same orbit's
specified bit subsequence. Convergence and exact values are row 4 theorem
content, not part of the definition. Incorrect input slices, legal-domain
totality, warmup, equality, changing parameters or feedback violate this
contract. No first-outcome probability law is supplied.

## 1. U-NATIVE-CHART-AND-QDD-READBACK: proposed T, L1

**Scope and statement.** Let `F_n(x0)` be the checkpoint obtained from an
origin-zero head `x0 in F5^6` by the unchanged native update, including its
existing counter `n` and `theta_n=s_2(n) mod 2`. Put

```text
S(0)=0, S(m)=m-S(floor(m/2)),
t_n=(-1)^(n-3), h_n=(-1)^(n+theta_(n-1)),
N_n=S(floor((n-1)/2))-1.
```

For every `n>=3`, the reachable sheet is
`X_n={x:z(x)=4-3 theta_(n-1)}`. The following map is a bijection from
`X_n` to `F5^5` and is constant along each synchronized native trajectory:

```text
L(n,x)=(alpha,beta,gamma,delta,epsilon),
alpha=t_n(p1+p1p),       beta=t_n(p4+p4p),
gamma=h_n(p1-p1p-2),     delta=h_n(p4-p4p-1),
epsilon=t_n r-N_n.
```

Its inverse sets `A=t_n alpha`, `B=t_n beta`, `C=2+h_n gamma`,
`D=1+h_n delta` and then

```text
p1=3(A+C), p1p=3(A-C), p4=3(B+D), p4p=3(B-D),
r=t_n(epsilon+N_n), q=4-3 theta_(n-1)-A-B-r.
```

All these checkpoint operations are in `F5`. Encoding the same labels at
another clock gives the exact trajectory jump; the digit-sum and finite
alternating-sum calculations require logarithmically many integer
arithmetic steps in that clock, without speeding up physical time.

For every preparation subset `D0` and every required initial record
`rho:D0->Y`, recovery from the indexed current native state at any
`n>=3` exists if and only if `rho` is constant on every admitted `F_3`
fibre. The synchronized chart transports this criterion to every later
time. The full pointed orbit retains its head and is a different input.

For the inherited complete five-field QDD record, equality is piston
equality up to simultaneous sign. The supported heads
`(4,1,0,0,0,0)` and `(2,1,1,2,1,0)` both become
`(1,4,0,0,0,0)` after one tick but have original LOW values `0` and
`9/14`. Hence universal late readback fails. A separately added static
label of initial-phase classes `{0},{1,2},{3,4}` restores all five original
fields at every time; three distinguishable labels are necessary and
sufficient. Full-head recovery instead requires and is attained by five
labels. These are correctly initialized extensions, not new native
coordinates. Without added state, the maximum full-QDD-readable domain
has `125*4+3000*2=6500` of the 15625 heads, also attainable using supported
heads only; restricting the domain is an explicit change of preparation.

**Proof and dependencies.** The exact coordinate inverse, update identity,
merger criterion, fibre multiplicities and optimality witnesses are in
[native readback PROOF](../../probes/P-QDD-U-NATIVE-READBACK-1/PROOF.md),
sections 1–6. Dependencies are `DEF-ARCHITECTURE`,
`KERNEL-Z6-SYNCHRONIZATION`, the inherited QDD algebraic record and its
sign-equality lemma. No saved-label physical implementation is a dependency
or conclusion.

**Falsifier.** An exact failure of either chart inverse or its update law;
a nonconstant initial record recoverable on one merged fibre; a failed
specified merger or memory lower-bound witness; or an incorrect
three/five-label bound, fibre multiplicity, or 6500 maximum.

## 2. U-NATIVE-INVARIANT-AND-NOWRITE: proposed T, L1

**Scope and statement.** On `X14={x:z(x) in {1,4}}`, define

```text
V(x)=(p1+p1p, p4+p4p,
      chi(z)(p1-p1p-2), chi(z)(p4-p4p-1)),
chi(1)=1, chi(4)=-1, R(x)={V(x),-V(x)}.
```

For every one of the 6250 checkpoints and both control bits,
`V(next)=-V(x)`. The complete free-control graph has exactly the 313
`R` fibres as its strongly connected components: 312 of size 20 and one
of size 10. Every invariant fixed checkpoint reader factors uniquely
through `R`; this includes nonlinear readers. Conversely a fixed
correlated preparation encodes and reads each of the 313 labels. This is
static coding, not a derived write interaction or independent ready state.

Every actual synchronized chart trajectory visits its whole R fibre
arbitrarily late, by the primitive clock-word proof. Therefore a fixed
checkpoint reader eventually equal to one value already has that value
at every point of the fibre. It cannot change from a distinct synchronized
BLANK to a permanent WRITTEN value under unchanged U. This row asserts
recurrence, not long-run density. Finite retention is not ruled out.
Clock-dependent readings, outside memory, changed context and interventions
lie outside this fixed-checkpoint class.

R is not the QDD record despite the coincident cardinality 313: one R
fibre has different current LOW values 1/16 and 1/136. The separate
original-head merger obstructs universal late recovery of the original record.

**Proof and dependencies.**
[MEMORY-PROOF](../../probes/P-U-NATIVE-MEMORY-EVENT-1/MEMORY-PROOF.md),
[CLOCK-PROOF](../../probes/P-U-NATIVE-MEMORY-EVENT-1/CLOCK-PROOF.md), and
[FREQUENCY-PROOF](../../probes/P-U-NATIVE-MEMORY-EVENT-1/FREQUENCY-PROOF.md).
Use the preceding chart row and the inherited QDD record for the final
comparison. Graph connectivity proves the invariant classification;
primitive word containment proves actual repeated visits and the eventual-constancy obstruction.

**Falsifier.** A failed transition identity, component count or universal
factorization; failure of whole-fibre recurrence; or an admitted eventually constant fixed checkpoint reader differing at an earlier synchronized checkpoint.

## 3. U-FINITE-HISTORY-CLOCK-PHASE: proposed T, L1

**Scope and statement.** For fixed finite `L`, a causal clock reader sees
only the legal word `(theta_(n-L+1),...,theta_n)`, using the same function
at every occurrence. It receives no counter, future bits, growing memory,
or changing source parameter. For every `k>=1`, length
`L_k=5*2^(k-1)` suffices to reconstruct `n mod 2^k` at every eligible
endpoint. In particular 640 bits suffice for phase modulo 256; minimality
is not claimed. Empty-buffer acquisition returns UNAVAILABLE until full,
and the accepted interface rejects illegal complete words and nonbinary
input. The retained finite buffer is an admitted observer resource.


For M=2^k a length-3M word recognizes phase and three causal parent bits,
whose six legal triples give 6M labels. Their frequencies are L5 row 4.
The residue assignment LOW for r<a, HIGH for a<=r<b, SILENT otherwise is
a fixed finite construction for integers 0<=a<=b<=M, b>0. Native histories
supply theta_(n-1) through z_n=4-3 theta_(n-1), so phase decoding needs
the +1 correction; a 640-checkpoint window is wholly synchronized by n=642.
No limiting frequency is claimed in this L1 row.

**Scope and statement.** On each fixed synchronized chart trajectory,
every finite legal decorated-checkpoint word recurs with bounded gaps.
For every fixed finite `L` and every fixed reader of

```text
((x_(n-L+1),theta_(n-L+1)),...,(x_n,theta_n)),
```

eventual equality to one value implies equality to that value at every
fully synchronized window, including all earlier such windows. A window
is fully synchronized when `n>=L+2`. Therefore such a reader cannot move
from a distinct BLANK value at a fully synchronized window to a permanent
WRITTEN value under unchanged U. UNAVAILABLE during filling is not BLANK.
The statement allows arbitrary nonlinear fixed readers and every finite
length, but not a length growing with time, an external persistent label,
changed context or intervention. It excludes neither finite retention nor
a message already present in preparation.

The original-head merger in row 1 also survives any finite window once
the entire window lies at or after their common tick-one successor.
Equal subsequent inputs cannot
recover the two different original records. This is distinct from a full
pointed-orbit functional, which still sees the head.

**Proof and dependencies.**
[finite-history MEMORY-PROOF](../../probes/P-U-FINITE-HISTORY-EVENT-1/MEMORY-PROOF.md),
sections 2–5. The primitive 100-letter clock from row 2 maps through a
length-two morphism to each decorated native trajectory. Primitivity
places every legal word in all sufficiently large substitution blocks.
Recurrence then transports eventual constant readout back to every
earlier legal window. Single-point positive frequency alone would not
justify the finite-word recurrence step.

**Falsifier.** A legal synchronized finite word without the proved
recurrence; an admitted fixed finite-window reader eventually constant
but different on an earlier fully synchronized window; or successful
original-record separation on the two identical late-window inputs.


Phase proof: P-U-FINITE-HISTORY-EVENT-1/CLOCK-PROOF.md, using five-bit
recognition and recursive decimation. Additional falsifiers are a legal
wrong-phase window, incorrect native +1 adapter, or wrong finite residue
allocation. Both phase and finite-window no-write have the single primary
evidence bundle P-U-FINITE-HISTORY-EVENT-1; their L1 dependencies are
native synchronization and the preceding chart/invariant rows.

## 4. U-NATIVE-READER-STREAM-SPECTRA: proposed T, L5

**Scope.** Exactly the L5 DEF-NATIVE-READER-STREAM domain and literal
equality above. Every limiting result is an all-prefix statement after
finite warmup. No physical occurrence is inferred.

For every origin-zero synchronized chart trajectory, every point of its
`R` fibre has positive all-prefix limiting density, uniformly `1/20` on
nonzero fibres and `1/10` on the zero fibre. The independent all-prefix
clock proof uses the primitive 100-letter substitution, not stationarity
alone. Let `F_D={a/b:0<=a<=b<=D}`, as a set of reduced rational values.
Complete per-orbit spectra for fixed present-state readings are:

| Read domain and statistic | Nonzero `V` | Zero `V` |
| --- | --- | --- |
| Binary checkpoint LOW density | `k/20`, `0<=k<=20` | `k/10`, `0<=k<=10` |
| `(checkpoint,driver bit)` LOW density | `k/60`, `0<=k<=60` | `k/30`, `0<=k<=30` |
| LOW density conditional on either bit | `k/30`, `0<=k<=30` | `k/15`, `0<=k<=15` |
| Absolute LOW density restricted to either bit | `k/60`, `0<=k<=30` | `k/30`, `0<=k<=15` |
| LOW fraction among positive-density accepted symbols | `F_60` | `F_30` |
| Accepted LOW fraction restricted to either bit | `F_30` | `F_15` |

Each atom receives one whole LOW/HIGH/SILENT assignment. Empty acceptance
is UNDEFINED. These are complete per-orbit spectra, not an assertion that
one global reader realizes independently prescribed targets on every
overlapping orbit. Eight of the 22 supported QDD LOW values lie outside
even `F_60`: `1/256,1/176,1/136,1/96,9/224,9/104,9/64,49/64`.
Thus the complete supported law is unavailable in this fixed-input class.
The equal cardinalities 313 do not identify `R` with the original QDD
record: one `R` fibre already contains current LOW values `1/16` and
`1/136`.


Every legal finite Thue–Morse factor has an exact all-prefix rational
frequency. For `M=2^k`, a length-`3M` word recognizes `6M` disjoint
classes of equal density `1/(6M)`, specified by phase and three causal
parent bits. Taking the union over all finite clock-word lengths gives
exactly

```text
unconditional LOW densities = {j/(3*2^k): k>=0, 0<=j<=3*2^k},
positive-acceptance LOW ratios = Q intersect [0,1].
```

This union is not the spectrum at each individual length and is not the
spectrum of all checkpoint-history readers. Given any rational `a/b` in
`[0,1]`, choose `M=2^k>=b`; from decoded residue `r` output LOW when
`r<a`, HIGH when `a<=r<b`, SILENT otherwise. Every `M` consecutive
available ticks contain `a`, `b-a`, and `M-b` symbols respectively.
The accepted ratio is `a/b`, with no supplied absolute counter.

On native synchronized histories `z_n=4-3 theta_(n-1)` gives the
preceding bit. Decoding that word requires a **+1** phase correction.
A length-640 checkpoint window is wholly synchronized by `n=642`.
The family contains all 22 supported QDD rational values as parameters;
this does not derive which parameter a preparation supplies.


For the fixed conditional incidence word e_v of row 6, capture/retention,
complete Cartesian incidence and its fixed slot convention are explicit
premises. The L5 reading is admitted through the same definition with the
captured source as a fixed parameter. With A,B,D,Delta as in row 6:
The source is fixed and natural ticks are observed consecutively after
valid warmup. For prefix length `n=qM+t`, and `T` the actual `t`
consecutive residual addresses from the chosen start, exact counts are

```text
C_LOW=qA+|O_LOW intersect T|,
C_HIGH=qB+|O_HIGH intersect T|,
C_ACC=qD+|(O_LOW union O_HIGH) intersect T|.
```

Bounded remainders give the formal-word densities `A/M,B/M,D/M`, and,
for `v!=0`, accepted ratio
`A/D=s^2/[4(5Q-s^2)]`, agreeing with the inherited QDD LOW value.
For complete cycles, with LOW/accepted counts `L,N`, exactly
`4 L Delta=N s^2`. This equality is **not** an arbitrary-prefix identity:
for source `1000` at first address zero, `L=N=1`, `Delta=4`, and
`16!=1`. When `s=0,v!=0`, no address emits LOW and some emit HIGH;
when `v=0`, there is no accepted symbol and the ratio is UNDEFINED.
Neither `kappa=0` nor a centered five-vector's zero sum replaces `s=0`.


**Primary evidence:** P-U-FINITE-HISTORY-EVENT-1 for complete causal clock
spectra. Its CLOCK-PROOF supplies pair-word frequencies, the 6M equal-mass
classes and the all-prefix extension. The inherited instantaneous
classification and primitive 100-state clock proof remain explicitly
evidenced by P-U-NATIVE-MEMORY-EVENT-1/CLOCK-PROOF.md and
FREQUENCY-PROOF.md. The conditional periodic-word corollary is
P-U-PREPARATION-EVENT-RECORD-1/INCIDENCE-PROOF.md section 6.
A single primary EVIDENCE entry must not conceal those proof sources.

**Dependency:** DEF-NATIVE-READER-STREAM at L5. Its owned projection gate
transports the named L1 chart/invariant, phase and incidence inputs.
**Falsifier:** a wrong all-prefix atom/factor limit, an exact member or
nonmember error in either complete spectrum, a whole-atom allocation
failure, or failure of the fixed-source consecutive-tick count/remainder
identity. Arbitrary invocation schedules are outside that corollary;
empty acceptance stays UNDEFINED. First-hit ordering is separate from
every limiting law here.

## 5. U-NATIVE-APPARATUS-HISTORY-FACTOR: proposed T, L1

**Scope and statement.** Split the native source as four pistons `p` and
the observed port `A=(q,r)`. A ready `a in F5^2` is common and independent
of `p`; all runs have the same binary driver `b`. Put
`kappa=sum(p) mod 5`, `z=kappa+q+r`, and `pi(x)=(z,q,r)`. The native
generators close exactly on this quotient:

| Generator | New `(z,q,r)` |
| --- | --- |
| `a` | `(z,q,r)` |
| `b` | `(-z,-q,-r)` |
| `c` | `(2-z,1-q,-r)` |
| `d` | `(2-z,1-q,1-r)` |
| `e` | `(3-z,2-q,1-r)` |

The selector also depends only on `z,b`. Thus the commuting identity and
induction prove the following complete, all-time quantifier:

```text
for every common ready a, common infinite driver b,
p,p' with equal kappa, every set Y, and every
F:image(H_(a,b))->Y,
F(H_(a,b)(p))=F(H_(a,b)(p')),
where H_(a,b)(p)=(A0,A1,...).
```

No linearity, computability, causality or finite-memory restriction is
needed for this functional statement. An arbitrary deterministic causal
processor with common source-independent initial memory and other common
inputs likewise has identical reader choices, symbols, records, stopping
decisions on equal histories. Its
memory may be unbounded. Additional source access and feedback are outside
the contract.

For the fixed-origin TM driver the maximal label is `kappa` at 24 readies;
at ready `(3,0)` it identifies just `2~4`. Complete histories are already
classified by `(A0,A1,A2)`. Minimum recognition horizons are tick 1 for
21 generic readies, tick 2 for `(0,0),(3,3),(1,3)`, and tick 1 for the
four observable classes at `(3,0)`; five-class recovery at the latter
ready is impossible. For every source subset and source quantity, exact
readback exists if and only if that quantity is constant on these classes.

Late tails have four classes at `(0,0),(3,0),(3,3),(1,3)` and five at
the other 21 readies. At the first and last of those four the late
identification is `0~1`; at the middle two it is `2~4`. At `(0,0),(3,3),
(1,3)` the missing distinction occurs at tick 2 and is absent from every
tick-three-and-later tail. Full-history storage can retain it.

Sources `1000` and `2400` have the same `kappa` and original LOW
`1/16` versus `1/96`; `0000` and `1400` have the same `kappa` but
different support tags. They cannot be separated by this port or any of
its history processors, for any common ready/driver. Their full states
nevertheless never merge, since equal quotients select common bijective
generators forever. The augmented port `(z,A)` reveals `kappa` at tick
zero but still fails both same-sum witnesses. The full pointed orbit can
read its original source directly. None of these observations implies a
no-go for every apparatus split or a physically selected capture axiom.

**Proof and dependencies.**
[NATIVE-PROOF](../../probes/P-U-PREPARATION-EVENT-RECORD-1/NATIVE-PROOF.md),
sections 2–9, the native generator definitions and inherited QDD record.
This all-time induction extends beyond the earlier finite U-induced
reader/delay census and does not reinterpret its system-side conditioning.

**Falsifier.** Failure of the commuting identity, complete TM class or
minimum-horizon/tail classification; a source quantity recovered despite
being nonconstant on an observable fibre; divergence of any stipulated
common-input processor on equal port histories; or failure of either
exact QDD/support or full-state nonmerger witness.

## 6. QDD-CONDITIONAL-INCIDENCE-AND-SYMBOLIC-RECORD: proposed T, L1

**Scope and statement.** This is an explicit conditional extension. Capture
and retain before tick one the **four-coordinate** balanced source
`v in V={-2,-1,0,1,2}^4`, with `ell=(0,1,2,-2,-1)`. Use ordinary
integer sums `s=sum_(i=0)^3 v_i`, `Q=sum_(i=0)^3 v_i^2` and
`Delta=5Q-s^2`, not a field sum or a 31-coordinate source. Admit one LOW
channel of signed amplitude `s` and five copies of each of the six pair
differences. An integer amplitude `a` occupies the complete Cartesian
square `{0,...,|a|-1}^2`, retaining its sign. These choices were made with
the QDD target known; they are not independently derived detector laws.

For every real four-vector the exact quadratic identities are

```text
sum_(i<j)(v_i-v_j)^2=4Q-s^2,
A=s^2, B=5(4Q-s^2), D=A+B=4Delta,
Delta>=Q, with Delta=0 iff v=0.
```

For integer sources the declared complete Cartesian fibres have those
cardinalities. Their fixed 544-slot embedding applies only to `V`: 64
LOW slots `r=8a+b`, 480 HIGH slots
`r=64+16(5j+c)+4a+b`, and 480 empty padding slots give `M=1024`.
The ordered pairs at indices `j=0,...,5` are
`(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)`, and copies have `c=0,...,4`.
LOW row and column indices `a,b` range from 0 through 7; HIGH indices
range from 0 through 3. LOW occupancy requires `a,b<|s|`; HIGH occupancy
requires `a,b<|v_i-v_k|` for the pair `(i,k)` at index `j` and copy `c`.
The bounds `|s|<=8` and
`|v_i-v_j|<=4` prevent truncation. The label word `e_v(r)` is
single-valued LOW/HIGH/SILENT, not a physical exclusive occurrence.

Given ordered direct TM-bit acquisition and the row-3 phase reader with
`k=10`, 2560 past-and-current bits address `n mod 1024`. The proved
native `z` adapter has the separate +1 correction. The executable record
wrapper uses direct bits; a separate end-to-end `z` wrapper is not claimed.
The resulting e_v is a finite single-valued residue word. Its limiting
count interpretation belongs exclusively to L5 row 4 through the declared
projection. At integer s=0, v!=0 there are no LOW slots and some HIGH
slots; at v=0 no accepted slot and no accepted ratio. Neither kappa=0 nor
a centered five-vector's zero sum is the hypothesis s=0. The static
cardinality ratio A/D equals the inherited QDD LOW expression on v!=0.

The four-coordinate common shift is not a symmetry: `1000` to `2111`
changes LOW from `1/16` to `5/8`. Indeed
`s'=s+4c`, `Q'=Q+2cs+4c^2`, `Delta'=Delta+2cs+4c^2`.
The balanced lift and reference choice are part of the input contract.
The 31 channel outputs cannot be substituted back as the source dimension.

For storage, additionally supply fresh cells `{BLANK,LOW,HIGH}` and an
archive. The control LOW or HIGH swaps that symbol with BLANK and fixes
the third; SILENT acts as identity and appends nothing. Accepted writes
require a fresh BLANK cell. Append the exact tuple
`(source_before,source_after,phase,fine_slot,sign,event,old_cell,written_cell)`;
the retained source does not change, and every earlier record is preserved.
A passive reread does not step or append. These are conditional
permutation and induction theorems, not physical allocation/reset or
reversibility of the whole growing-buffer/archive protocol.

The archived first symbol is not selected by the count limit. Source
`1000` with onsets 3072 and 3136 has first LOW and first HIGH respectively,
while the corresponding L5 limits are recorded only in row 4. Phase-zero-only and
phase-64-only invocation schedules give all LOW and all HIGH. Thus neither
arbitrary calendars nor a probability law for fresh preparations follows.
Storage supplies persistence; the algebraic count ratio does not require
that archive. No controlled comparison of old `0/900` instrument cases
against `624/624` source vectors was performed.

**Proof and dependencies.**
[INCIDENCE-PROOF](../../probes/P-U-PREPARATION-EVENT-RECORD-1/INCIDENCE-PROOF.md),
sections 1–7; row 3 for phase addressing; inherited QDD factorization for
the final algebraic comparison; the retrospective audit for the explicit
four-dimensional, shift, prefix and layer distinctions. Row 5 explains
why the extra captured source is not supplied by the natural port alone.

**Falsifier.** A wrong four-dimensional identity or support decision; a
truncated incidence fibre inside `V`; an addressed LOW at integer `s=0`;
failure of the controlled-cell inverse, fresh-cell
precondition, unchanged captured source, or preservation/passive reread of
an older record. No physical realization is claimed for this falsifier.


No retained source, buffer, archive or selected symbol feeds back to U.
## 7. QDD-CONDITIONAL-INCIDENCE-FINITE-AUDIT: proposed C, finite L1 implementation audit

**Scope and statement.** The sealed implementation agrees exactly with
the specified four-dimensional incidence counts and supported QDD ratios
on all 624 nonzero sources of `V`, with the zero source separately typed.
Its complete source/address check covers `625*1024=640000` pairs. The
causal record audit covers seven frozen sources at two frozen onsets,
14336 stream updates, including complete payload and every-prefix checks.
The corresponding phase audit covers 16384 generating contexts for 8188
legal length-2560 words. The complete run has 1082026 exact comparisons;
that total is not a count of independent experiments.

The implementation claim assumes captured and retained `v`, complete
Cartesian incidence, fixed slot order, correct ordered bit acquisition and
consecutive observation. Fresh cells and an archive are additional
premises for its record checks. It says nothing about all integer sources,
all finite streams or a physically available apparatus. Universal
identities and processor invariance belong to their L1 proof rows, and
all long-run word frequencies to L5 row 4, not to extrapolation from this C row.

**Evidence and dependencies.** The unchanged
[verify.py](../../probes/P-U-PREPARATION-EVENT-RECORD-1/verify.py),
[EXPECTED](../../probes/P-U-PREPARATION-EVENT-RECORD-1/EXPECTED.txt),
[RUN](../../probes/P-U-PREPARATION-EVENT-RECORD-1/RUN.md), and
[RESULT](../../probes/P-U-PREPARATION-EVENT-RECORD-1/RESULT.md).
EXPECTED is 8352 bytes, SHA-256
`5d56f69ce88fff71c433903cfa95305c2c5c7e51c1db16fb7064715f7338d7ef`.
The finite comparison depends on the frozen implementation contract and
inherited QDD formula; the independently stated mathematics is row 6.

**Falsifier.** An exact admitted source/address discrepancy, wrong zero
disposition, or failed frozen record/phase case. A byte or source mismatch
without mathematical negation is integrity STOP. This bounded C status
does not weaken the independently proved universal mathematics.

## Intake boundary

The seven rows classify native readback, invariant storage, mathematical
frequency capacity, fixed-window permanence, the natural apparatus port,
and one conditional source-to-symbol/archive construction. The adopted L5 projection is mathematical. These rows do not
select a physical reader, source capture, coupling, occurrence mechanism,
post-measurement instrument, storage supply or reset. They do not close or create a QDD physical O owner or physical realization gate. The existing owners retain
their exact obligations. No new retrospective hand example is passed off
as a comparison in an earlier frozen run.
