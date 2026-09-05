# P-DECODER-RESERVOIR-COUPLING-1 preregistration

**FROZEN TARGET / NO FORMAL RUN AT PIN / PUBLIC STATUS NONE.**

Disclosure: **CHOICE-EXPLICIT / PROOF-FIRST / L1 ONLY**. The inherited source
was constructed with its QDD norm match exposed; no physical target
independence or Born selection is claimed.

```text
owner: A. M. Thorn
issue: https://github.com/mathorn1973/twist-j/issues/824
branch: probe/P-DECODER-RESERVOIR-COUPLING-1
base: a353b7e2aaec3e13f458f52e68c6464b9d718e67
authority: ACTIVE Public Canon v76
claim: DECODER-RESERVOIR-RECORD-ACCOUNTING
formal runs at pin: 0
public status: NONE
```

## 1. Equation and one conditional target

Use finite-support rational D3 pairs `(u,v)` and the fixed five-shell operator
L of the preceding transport result. For finite rational `gamma_x>=0`, incoming
reservoir amplitudes a supported on `R={gamma>0}`, and `p=(w-u)/2`, select

```text
f_x=gamma_x(2a_x-p_x),             b_x=a_x-p_x on R,
(1+gamma_x/2)w_x=2v_x-(Lv)_x-(1-gamma_x/2)u_x+2gamma_x a_x.
```

Outside R the update is free and there is no reservoir channel. The outgoing
port is b. Let `P_gamma(a)=sum_x gamma_x a_x^2`. The one proposed claim is
the conjunction of all following clauses under exactly these choices:

1. The complete `(wave,incoming)->(new wave,outgoing)` map is a rational
   bijection, including `gamma=2`, with the displayed inverse in PROOF.md.
   It preserves `E(wave)+P_gamma(port)` and obeys the exact local balance
   inherited from the forced wave law. Finite supports and local dependence
   remain finite at every finite step.
2. With a fresh zero incoming port at each step, the wave loses exactly the
   nonnegative deposit `d_x=gamma_x p_x^2=gamma_x b_x^2`. Accumulating
   `heat'_x=heat_x+d_x` preserves `E+sum heat`. Signed outgoing amplitudes
   are retained on a tape, and its weighted squared amplitudes equal heat.
3. For a fixed common rational threshold q>0, define per-channel
   `N_x=floor(heat_x/q)` and `r_x=heat_x-qN_x`. Every transition emits exactly
   the full interval of new lifetime ordinals at each channel, retains
   `0<=r_x<q`, and preserves `E+q sum N+sum r`. These are alternative
   representations of the same energy, not additional energy stores.
4. From initial zero heat, the generated finite histories are total, immutable
   and compatible under prefix restriction and continuation. Their signed
   reservoir tape reverses the full generated wave continuation. The total
   number of distinct threshold ordinals is at most `floor(E_initial/q)`.
   The initial state is the prior completed preparation `(0,S(source))`
   before the absorber acts, so `2E_initial=m_QDD(source)` on its defined
   rational source domain. No finite detection time or total absorption is
   guaranteed. No source, wave or U update takes a threshold record as input.

PROOF.md establishes the uniform conditional result; finite gates audit its
implementation. All clauses are required. This is one chosen mathematical
apparatus adapter, not the complete physical apparatus profile or decoder.

## 2. Accepted code and immutable inputs

The accepted program is verify.py, coupling.py and audit_coupling.py in this
directory. It additionally reads PROOF.md and CONTRACT.md for immutable hash
checking. All seven new source files are pinned together:

```text
PREREG.md  PROOF.md  CONTRACT.md  README.md
coupling.py  audit_coupling.py  verify.py
```

There is exactly one existing executable source dependency:

```text
path: probes/P-DECODER-RETARDED-ENERGY-TRANSPORT-1/transport.py
source_pin: 30ab237b4dcb339115517f67b883ca4cc3e00c32
sha256: 983d22690e061128d287f23ef4672fbd72954faa28f1a3fde9ce38b0d6660a60
bytes: 11353
```

coupling.py checks that file's hash before import and checks the imported
module's exact origin. It adds its directory temporarily to Python's import
path and removes it immediately after importing. No prior probe is copied,
changed or resumed. The mathematical dependency and its public result are
identified in PROOF.md; no unregistered result is relabelled Canon.

Only standard-library exact integers, Fractions, finite tuples, dataclasses,
AST and byte hashing are used. No external data, network, subprocess, random
seed, float tolerance, physical measurement or environment-dependent target
enters the scientific program. Runtime file reads are limited to the pinned
code/proof/contract bytes. The verifier prints only deterministic stdout.

Before the first formal run, commit and push all seven source files and
read back their exact bytes together with the inherited dependency. Static
inspection and compilation are allowed beforehand; scientific execution and
imports are not. The first formal command in a clean Linux checkout is:

```text
python3 probes/P-DECODER-RESERVOIR-COUPLING-1/verify.py
```

## 3. Carrier and frozen finite audit

The full wave carrier is `C_c(D3,Q)^2`. Gamma is a canonical finite field
with positive rational entries; zero coefficients are omitted and the empty
context is allowed. The threshold is a positive rational. Incoming/outgoing
ports and heat are finite fields on the same fixed channel sites. Heat is
nonnegative. Equality is literal, without phase or apparatus quotients.

Single State transitions allow any nonnegative initial heat and nonnegative
tick; their budget is initial E plus initial heat. The stronger history bound
in clause 4 is explicitly for ready zero heat and tick zero. The tape and
threshold addresses live in one fixed history context. Python record types
and all equality/overlap/readiness conventions are fixed in CONTRACT.md.

The accepted code freezes these gates and their exact literal cases:

```text
G01_COUPLING          independent pointwise solve, warm and cold ports,
                      zero/empty controls, weighted energy, both inverse directions
G02_COLD_BALANCE      nonnegative deposit, forced local/aperture balance,
                      exact wave plus reservoir accounting
G03_MEMORY           exact boundaries, positive subthreshold deposits,
                      multiple crossings, residuals and no repeated ordinals
G04_BOUNDARIES        inversion-odd dark state, instantaneous blind port and
                      complete one-step absorption at gamma=2
G05_PREFIX_TAPE       zero, unit and (1/2,-2,1,-1/3) sources; steps0..3;
                      continuation, tape reversal, budget, complete lifetime ranges
G06_TYPES            invalid coefficients/thresholds, off-channel ports/heat,
                      ticks, ranges, lengths and inconsistent histories
G07_LOCALITY_CHOICES  distant changes outside the stencil; amplitude scaling;
                      threshold changes affect records but not wave/deposits;
                      per-channel versus pooled counts and input-dependency audit
```

G05 uses gamma=2 at `(0,0,0)`, gamma=1/2 at `(1,1,0)`, and q=1/100.
G07 uses the pair `(delta_o/3,2delta_p/5)`, the same gamma, and q=1;
remote perturbations at `(40,0,0)`; amplitude factor -3/2; threshold
comparison 1/1000 versus1000; and heat 3/5 at each of o,p for the pooling
boundary. G01--G04 cases are specified literally by audit_coupling.py,
including exact gamma=2 and zero/empty controls. No gate is selected by a
measured or fitted outcome. The infinite wave is not truncated to a box.

For complete case identification, G01 crosses the pairs zero, `(0,delta_o)`
and `(delta_o/2-delta_p/3,-2delta_o/5+3delta_p/7)` with gamma profiles
empty, `{o:1/2}`, `{o:2}`, `{o:4}`, `{o:1/2,p:4}`, `{o:2,p:1/2}`.
Nonempty contexts have cold and warm ports (2/3 at o, -3/5 at p, restricted
to present channels), giving 33 cases, each checked in both directions by
also treating the same pair/port as an arbitrary output. G02 uses the same three pairs with
`{o:1/2,p:2}`, q=2/3 and every singleton in the active halo, plus empty,
two-site, whole-halo and far aperture controls.

G03 uses `{o:2,p:1/2}`. Direct threshold cases at q=3/5 are heat empty,
`{o:2/5,p:3/5}`, `{o:9/5,p:21/10}` and `{o:17/5,p:3/35}`. Cold transitions
at q=1 start with pair `(A delta_o,0)` and `(A,heat,tick)` equal to
`(1,empty,0)`, `(1,{o:1/2,p:1/3},7)`, `(2,empty,0)`, `(3,{o:3/4},2)`,
`(3,{o:11/4},2)` and `(0,{o:2},9)`. Each is followed by another transition
checking that existing ordinals are not emitted again. G04 uses gamma=2
only at o, q=1: the inversion-odd pair `(0,delta_p-delta_-p)` for three
steps, the completely absorbed pair `(2delta_o,0)` followed by two steps,
and instantaneous blind pair `(5delta_o/9,delta_o)` for one step. The
uniform dark-mode conclusion is proved independently in PROOF.md.

## 4. Systematics and choices

Pair order is previous/current. The original source kick completes before
the first coupled transition; batch tick0 denotes that first transition, not
the source preparation. All subsequent gamma and q values are fixed. Fresh
incoming zeros represent new reservoir slots, not reset or erased old ones.
The signed outgoing tape retains information that scalar heat alone can lose.
The available supply of fresh ports and persistent memory is an explicit
unbounded apparatus idealization with finite use at every finite horizon.

The coupling, gamma profile, threshold, channel decomposition, fresh-port
readiness, lifetime ordinals and atomic batch are choices, not consequences
of J or physically calibrated constants. Heat and threshold records do not
feed the coupling; the wave is affected by the chosen coupling itself, not
by passively reading its record. This differs from the prior energy reader.

Positive aperture energy is not equivalent to a deposit: the midpoint port
can vanish. The model neither guarantees reflection-free or complete
absorption nor forbids complete absorption in special states. Record queries
on overlapping site sets refer to one ledger, with inclusion-exclusion. The
threshold is applied per fixed elementary channel; re-pooling heat before
flooring is a different chosen read. Multiple distinct couplers are not
silently combined or credited twice on overlapping sites. No reset or
erasure operation is provided. History constructor consistency does not by
itself certify reachability of an arbitrary forged final wave pair; the
claim concerns the explicitly generated histories.

## 5. Failure threshold and disposition

Threshold: **zero exceptions and exact equality**. Any failed required clause
or gate fires the sole claim. Assertion failures produce a completed record
with SCIENTIFIC-FIRED, exit zero and exact stdout, and must be retained and
merged. An unexpected execution/integrity failure without a completed record
consumes this identifier under the abandoned-pin rule. Never edit frozen
code, choices, scope, cases or thresholds to rescue this pin. Any correction
requires a new identifier and preregistration.

After execution, write exact stdout to EXPECTED.txt; record neutral Linux
environment, pin, dependency hashes, exit code, byte counts and line endings
in RUN.md; state earned scope and fired falsifiers in RESULT.md. The required
GitHub workflow independently compares exact bytes on aarch64 and x86_64.
One probe per PR; preserve the pin through a merge commit. Registration is
deferred to a separate earned Canon fold.

## 6. Action layer and physical boundary

**L1 encoded mathematical coupling, memory and records only.** This does not
claim the L4 support/L5 history physical profile required by #539. Physical
source/detector realization, quantum effects and post-state instruments,
apparatus-family completeness, target independence, SI calibration, physical
event completion, occurrence/sampling, Born frequency, COMM-SAT and Bell
accounting remain unresolved. Threshold ordinals are not photon counts or
Born outcomes; no one-click rule follows. No physical or L6 bridge passes.
The #744 pole/polarization obligations and #756 F3 NOT_SATISFIED remain;
production #742 stays FORBIDDEN. COINCIDENCE-RECORD-FREQUENCY is UNTESTED/STOP.

**PUBLIC CLAIMS UNREGISTERED / CANON UNCHANGED.**
