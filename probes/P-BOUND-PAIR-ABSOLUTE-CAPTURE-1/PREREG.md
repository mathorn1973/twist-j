# P-BOUND-PAIR-ABSOLUTE-CAPTURE-1 prospective contract

**NON-CANONICAL / L1. Prospective execution contract.**

Author: A. M. Thorn <thorn@twistj.com>.
SPDX-License-Identifier: Apache-2.0.
Reservation: [#1814](https://github.com/mathorn1973/twist-j/issues/1814).
Owner: the single continuing session recorded in that reservation.

This is the prospective contract for the complete three-file verifier.
The three input digests are fixed below and static review is complete.
The entire package must be committed, pushed and publicly read back before
the first scientific execution. This preregistration reports no run or
numerical result.

## 1. Authority and conditional dependency

```text
PUBLIC authority:       mathorn1973/twist-j main
Public Canon:           v106
main / peeled tag:      a193e389fb1ddb0bdc89165b015c95a17eb1e425
content commit:         9242db4f040d67d9417eacd06612230b74248cff
Canon SHA-256:          52302c640033dd15d4a7a075cad16fa48b1473b7396d1f7413536a9ec45422e7
Canon bytes:            1370107
conditional source:    PR1813 at 8298af04f7385ec24f61a1b7c84d861cae017529
branch:                 probe/P-BOUND-PAIR-ABSOLUTE-CAPTURE-1
probe path:             probes/P-BOUND-PAIR-ABSOLUTE-CAPTURE-1/
analytical path:        notes/C-BOUND-PAIR-ABSOLUTE-CAPTURE-N/
action layer:           L1 only
```

The root owns authority, normative-hash and collision readbacks. The
branch starts at this public main. The open, unmerged predecessor remains
a pinned NON-CANONICAL analytical dependency; no predecessor probe is
imported or executed. The final `PROOF.md` and `SOURCES.md` under the
analytical path identify all premises and their exact public bytes.

## 2. Original absolute target and full denominator

The sole target is the original absolute reference probability
`P0 = P_win(0)`:

\[
 P_0=\int_{I_K}\frac{dK}{2\pi}\int_{I_E}\frac{dE}{2h}
 \frac{64\pi^2\rho_{\rm in}(E)\rho_{2,b,+}(K,E)}
 {|4+F_1(E)F_2(K,E)|^2}.
\]

Keep the full port functions with the inherited exterior radial boundary
convention:

\[
 F_1(E)=\int_{-\pi}^{\pi}f_B(P,E-\beta)\frac{dP}{2\pi},
 \qquad
 F_2(K,E)=\int_{-\pi}^{\pi}\sum_{\sigma=\pm1}
 h_\sigma(k)f_A(K-k,E-\beta-\sigma\varepsilon(k))\frac{dk}{2\pi}.
\]

The full F2 boundary contains the continuum, every physical relative
bound pole after pulse convolution, and the principal-value imaginary
part. The numerator selects the original outgoing branch. Both pulse
signs and every admitted denominator channel remain present.

The contact has `mu=2`, `g=2*pi/5`, `beta=4*pi/5` and capture core
`((3/5,-4/5),(4/5,3/5))`. The carrier, both arrangements, all 26 labels,
receiver and admitted old-memory/reference states remain those of the
inherited homogeneous capture-and-record theorem.

## 3. Frozen source, windows and event

Use exactly

\[
 \delta=h=\delta_K=1/1000,\qquad E_*=8\pi/5,\qquad
 k_0=-\arccos\frac{9-5\sqrt5}{16},
\]
\[
 I_E=[E_*-h,E_*+h],\quad I_{\rm in}=[-\delta,\delta],\quad
 I_K=[k_0-\delta_K,k_0+\delta_K],\quad
 I_{\rm out}=[-1/100,1/100].
\]

The incoming contact-selected relative AC packet, standing token at
`y=0` with label 1, receiver at `z=100`, and flat energy density
`1/(2h)` on `I_E` are unchanged. Localizing the token gives uniform total
momentum measure `dK/(2*pi)`, without conditioning the input on `I_K`.
The joint event includes the bound-pair projector, the right-moving
positive pulse branch, outgoing pair momentum in `I_out`, the stated K/E
windows, and the record with all admitted memory/reference correlations.

The incoming density is

\[
 \rho_{\rm in}(E)=\int_{-\delta}^{\delta}
 \rho(P,E-\beta)\frac{dP}{2\pi},\qquad
 \rho(P,\omega)=
 \frac{\sqrt{(\cos P-5\cos\omega)^2-16}}
 {2\pi[\cos P-5\cos\omega+4\cos(\omega-g)]}.
\]

The executable uses the conditional CP-24 finite-width enclosure
`(delta/pi)*rho(0,E-beta)*(1+[-delta^2,delta^2])` uniformly on the
original energy window. It does not substitute an exact zero-width
source. All constants are exact integers, ratios or specified algebraic
and trigonometric expressions; there are no measured or fitted inputs.

## 4. Complete pinned input inventory

The sole scientific entry point, run from the repository root, is

```text
python3 probes/P-BOUND-PAIR-ABSOLUTE-CAPTURE-1/verify.py
```

It accepts no numerical command-line override or interactive input, uses
only the Python standard library and these local files, and performs no
network access.

| Pinned executable input | SHA-256 |
|---|---|
| `probes/P-BOUND-PAIR-ABSOLUTE-CAPTURE-1/verify.py` | `0f4c0ca43024aeeb93d41acb35e41f52d5d1dfd9fe960067172a918e33d74a67` |
| `probes/P-BOUND-PAIR-ABSOLUTE-CAPTURE-1/interval_core.py` | `cbf3259297b47c3fcd13e122e747f8c140b27c97917b6f242e5bb16811208ae1` |
| `probes/P-BOUND-PAIR-ABSOLUTE-CAPTURE-1/model.py` | `6984302b20df4154dad6c2afd9d2becb82df4a01b03c4a0390041d0ebba8fdce` |

Runtime fixtures: **NONE**. External constant tables: **NONE**.
No scientific constants, root census, quadrature or probability
calculation is evaluated by importing these modules.

The analytical input is the single
`notes/C-BOUND-PAIR-ABSOLUTE-CAPTURE-N/PROOF.md`, with the inherited
source inventory in its sibling `SOURCES.md`. Those documents and this
preregistration are in the same public pin as the executable. The public
readback records exact bytes and hashes for all six files; no file is
required to contain its own hash.

## 5. Exact arithmetic and complete scalar reductions

All scientific arithmetic uses outward fixed-point intervals on
`Z/2^96` with integer endpoints. Rational conversion, multiplication,
division and elementary functions round outward. Square-root endpoints
use integer square roots and exact endpoint inequalities. No binary
floating-point value decides a scientific assertion.

The pi enclosure uses
`pi=16*atan(1/5)-4*atan(1/239)`. Each arctangent uses exactly 40
alternating rational terms and an explicit next-term remainder bounded
by `1/(81*q^81)`. Sine and cosine use 24 coefficients, degrees 47 and
46, respectively. On the reduced range `|r|<=1` their remainder bounds
are `1/49!` and `1/48!`. Quadrant reduction uses the pi enclosure,
includes all possible interval extrema, and returns the safe range
`[-1,1]` if reduced uncertainty exceeds the Taylor domain.

The negative root defining k0 is isolated from
`cos(k0)=(7-5*phi)/8`, `phi=(1+sqrt(5))/2`, starting with the enclosing
bracket `[-pi.hi/2^96,0]`. There are at most 128 midpoint steps, with
an interval-Newton contraction when the target and midpoint cosine
enclosures overlap. Required final width is at most `10^-20`, rounded
down in raw units. Initialization occurs before the controlled audit
block; an initialization failure is not a completed INCONCLUSIVE result.

The model uses the complete scalar fA/fB formulas in `PROOF.md` and
the physical sheet fixed by exterior continuation. It retains both
`sigma=-1,+1` and weights `h_sigma=(1-sigma*epsilon')/2`. Strict gap,
continuum and threshold enclosures are distinguished. A removable
factor or threshold that the actual interval predicates cannot certify
is left unresolved; no sampled sheet or denominator replacement is used.

## 6. Uniform geometry and pole accounting

There is exactly **one uniform external K/E box**, covering all of
`I_K x I_E`. There is no outer subdivision, outer exceptional box or
excision in this executable. All model enclosures retain the entire
external variation.

For each pulse sign, in order `-1,+1`, the census begins with 64 equal
panels in `u=k/pi in [-1,1]`. Initial processing is left to right;
a subdivided left child is processed before its right sibling. Each
panel must be excluded by the one-sided complete no-pole predicate,
excluded by a nonzero gap denominator H, or covered by a certified
simple-root neighborhood. No unresolved inner region is discarded.

A candidate root requires separated H_k' and opposite endpoint signs
uniformly over K,E. Up to nine clipped dyadic neighborhoods are attempted.
After sign certification, at most 16 interval-Newton steps refine the
root tube; refinement stops if its raw width improves by at most four
units. Overlapping tubes are identified only after derivative separation
on the union of their certified covers. Root-tube intersections must
remain valid.

A still unresolved panel with normalized width at most `2^-40` raises
controlled uncertainty. A complete census must identify exactly one
selected `sigma=+1` root whose entire outgoing momentum tube is inside
`I_out` and whose absolute residue has a positive lower bound. No pole
count is assumed or prescribed. Final roots are sorted by
`(sigma,lower_u)`.

For each root r use the signed cotangent coefficient

\[
 c_r=\frac{B(r)}{2H_k'(r)}.
\]

All real coarea contributions `|c_r|` are added to F2. The imaginary
boundary is regularized with the periodic cotangent whose full-circle
principal value is zero. Near a root, the complete segment between the
panel and its root tube must stay in the certified smooth monotone gap
cover, and its maximum momentum distance must be at most `1/8`. The
local quotient uses first and second derivative enclosures on that whole
segment, with the correction
`|cot(d/2)-2/d|<=|d|/5`. The exact root is retained as an implicit root
family; its midpoint does not replace it. Outside such a certified
segment the full boundary formula and every cotangent term are retained.

## 7. Range quadrature and fixed budgets

Each quadrature panel contributes its exact normalized length times an
enclosure of the integrand on the entire panel. F1 uses evenness to
integrate over `u in [0,1]` with unit factor; F2 integrates the
regularized full sum over `u in [-1,1]` with factor `1/2`, then adds
all real coarea contributions.

Both quadratures start with 64 equal panels. The next split is the
panel with the largest sum of real and imaginary enclosure widths;
an unresolved panel receives priority score `2^300`. Insertion order
breaks equal-score ties. Each split replaces one panel with its left
and right halves. Running endpoint totals use exact integers.

The budgets and stopping rules are fixed before execution:

| Quantity | Frozen limit or rule |
|---|---|
| Geometry model evaluations | 4096 actual uncached census calls |
| F1 live leaf panels | 1024 |
| F2 live leaf panels | 4096 |
| Initial panels in each census sign and each quadrature | 64 |
| Root neighborhood attempts | 9 |
| Interval-Newton refinements per certified root attempt | 16 |
| Unresolved geometry minimum normalized width | `2^-40` |
| F1 early-stop maximum component width | `1/100` |
| F2 early-stop maximum component width | `1/20` |
| Final certification comparison | `L>0` and `U<=10*L` |

The geometry counter charges actual uncached calls to either
`model.no_pole` or `model.pole_data` through the census. The budget is
checked **before** increment and invocation. The two method caches have
separate keys `(u.lo,u.hi,sigma)`; cache hits cost nothing. Cached
uncertainty in pole data is re-raised without another model invocation.
The shared geometry budget is never reset between signs or root
refinements. Each quadrature counter charges one interval-integrand
evaluation per panel; that evaluation may contain multiple direct model
calls. Those direct calls do not consume the geometry budget.

Quadrature budgets count current leaf panels, not total evaluations.
With 64 initial evaluations and two evaluations per split, the maximum
evaluation counts are `2*1024-64` and `2*4096-64`. Width tolerances
provide early stopping only. A complete range sum at its panel budget
remains usable even when that tolerance was not certified. An unresolved
range at the limit or exhausted grid raises controlled uncertainty.
The printed target-width flags report early-stop acceptance; a zero
flag records exit at the panel limit and alone asserts no width inequality.

After complete F1/F2 enclosures with positive real lower bounds, the
denominator is enclosed directly and its lower endpoint strengthened by

\[
 |4+F_1F_2|^2\ge16\operatorname{Re}F_1\operatorname{Re}F_2.
\]

The selected numerator and whole-window normalization give
`(h/pi)*64*pi^2*rho_in*|c_selected|/(2*pi)/denominator`.
This encloses the entire original double integral because the E measure
has total mass one and the K measure has total mass `h/pi`.
The final interval is intersected with the inherited full-event bounds

\[
 2/10^{28}<P_0<8/(5\pi\,10^6).
\]

All intersections are consistency obligations. A contradictory
intersection is an uncaught programming/enclosure error, not uncertainty.
No finite spatial box, radial extrapolation, changed source, omitted
inner region or selected-channel denominator is admitted. No decision
depends on wall-clock timing.

## 8. Exact stdout schema and predetermined dispositions

After successful initialization stdout begins exactly with

```text
P-BOUND-PAIR-ABSOLUTE-CAPTURE-1
arithmetic: outward fixed-point 2^96; full boundary resolvents
source: delta=h=delta_K=1/1000; selected |P_out|<=1/100
```

A complete census then prints, in this order,

```text
geometry: COMPLETE; evaluations=<integer>
pole <index> sigma=<-1 or 1> k=[<lower>,<upper>] residue=[<lower>,<upper>] selected=<yes or no>
```

There is one pole line per actual certified root, indexed from zero.
Pole endpoints and F1/F2 endpoints below use outward decimal formatting
with 18 fractional places. A complete probability enclosure then prints

```text
F1 Re=[<lower>,<upper>] Im=[<lower>,<upper>]
F2 Re=[<lower>,<upper>] Im=[<lower>,<upper>]
quadrature panels=<F1 integer>,<F2 integer> evaluations=<F1 integer>,<F2 integer> target_width=<0 or 1>,<0 or 1>
P_win(0)=[<lower>,<upper>]
P_win(0) raw=[<lower integer>,<upper integer>]/2^96
```

The probability decimal endpoints use 32 fractional places. The raw
line gives the exact dyadic interval; both representations are printed.
There is no predicted pole count or target magnitude.

The final line is exactly one of

```text
status: CERTIFIED; upper/lower<=10
status: INCONCLUSIVE; certified enclosure wider than factor10
```

CERTIFIED is permitted **if and only if** the actual complete interval
has positive raw lower endpoint and `upper_raw<=10*lower_raw`.
A complete but wider interval is printed in full and classified
INCONCLUSIVE. The early-stop tolerances do not decide this status.

If an intended `Uncertain` escapes geometry or boundary integration
inside the audit block, the following lines are printed instead of an
unavailable complete probability calculation:

```text
geometry evaluations=<integer>
status: INCONCLUSIVE; <actual uncertainty reason>
retained bound: 2/10^28 < P_win(0) < 8/(5*pi*10^6)
retained outward interval=[<lower>,<upper>]
retained raw=[<lower integer>,<upper integer>]/2^96
```

The retained interval always encloses the **entire original event**:
its endpoints are the outward `2/10^28` lower endpoint and the outward
`8/(5*pi*10^6)` upper endpoint. The decimal line again uses 32 fractional
places. It is explicitly inherited conditional information, not a new
absolute magnitude estimate. If the census completed before later
integration failed, its already printed census and pole lines remain
in stdout ahead of these fallback lines. A partial inner sum is never
presented as complete F2.

Both controlled statuses finish normally with exit code zero and empty
stderr. Only the intended `Uncertain` exception is controlled. TypeError,
ValueError, AssertionError, arithmetic programming errors and unexpected
exceptions remain uncaught and exit nonzero. This executable has no
separate negative-witness output branch; no such branch is invented
after execution.

## 9. First-run custody and technical failure

The accepted package is publicly pinned and all six input files read back
before any scientific execution. Static parse/compile review before that
pin does not execute the scientific path. The root then executes the
entry point once from the pinned tree in the repository environment:

```text
LC_ALL=C
LANG=C
PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0
TZ=UTC
```

Preserve the exact first stdout, stderr and exit disposition. No silent
retry, changed tolerance, enlarged budget, window revision or post-pin
repair is allowed. The repository's 600-second replay limit is unchanged;
an external timeout is a technical failure, not a controlled budget result.

A completed CERTIFIED or INCONCLUSIVE run is closed with its actual
`EXPECTED.txt`, `RUN.md` and `RESULT.md` in a later commit, preserving
every pinned input byte. RUN records full pin_commit, verifier_sha256,
exact command, neutral platform, architecture, Python version, exit_code,
stdout_sha256/bytes/lines and stderr_sha256/bytes. A technical failure
that never completed the gate receives the policy's ABANDONED record
without fabricated EXPECTED.txt or RUN.md; its pin is consumed.

The unchanged runner checks the run fields, verifier pin and ancestry,
clean exit/stderr and exact stdout identity. The custody manifest and
public readback also bind both helpers and analytical sources.
Required x86_64 and aarch64 replay must be read from the actual final-head
workflow logs before that evidence is claimed. No workflow or gate is
modified by this package.

## 10. Scope and review limits

The proposal and all new conclusions remain NON-CANONICAL, L1 and
conditional on the stated model and analytical premises.
Component-separated static cross-review within this one continuing
session is authoring review, not independent external theorem acceptance.

The numerical scope is the original asymptotic joint event on its
original normalized state. No native preparation, physical occurrence
law, finite detector result, renewal, particle identification, spin,
charge, statistics, polarization, SI scale, general capture rate or
plane-wave cross section is inferred. No merge, Canon promotion,
registry/frontier change or release is part of this preregistration.
