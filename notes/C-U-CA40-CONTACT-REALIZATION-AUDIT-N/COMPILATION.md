# Compiling the contact from a Ca40 light-shift gate family

**PUBLIC / NON-CANONICAL / conditional analytical construction.**
Author: A. M. Thorn. Original text Apache-2.0.
Reservation: [#1444][reservation].
Public base: `408fc7a34cbd8113b4d5e1dac43793c7ad0270b0`, Public Canon v101.

This is a symbolic compilation and resource upper bound, not an experiment,
simulation, accepted verifier, or measured implementation. No scientific
program was run. The four-entangler SUM construction below was derived
during this audit after reading the published gate formula. The earlier
contact and its fourteen-SUM circuit were already exposed. The twenty-affine
profile symmetrization is existing work in [#1364][old-claim] and
[#1365][old-local], not a new method of this note.

## 1. Physical primitive and the exactness contract

The selected comparison code is the published Ca40+ optical ququint with
one S_(1/2), m=-1/2 level and four D_(5/2) Zeeman levels, connected by 729 nm
carrier transitions. It is not the separate all-D five-level encoding with
an additional ground state. [Hrmo et al.][hrmo] use closed light-shift
motional loops and cyclic echoes to obtain, up to a common phase,

```text
G(theta)|j,j> = |j,j>,
G(theta)|j,k> = exp(i theta)|j,k>,   j!=k.                (1)
```

Their Eq. (3) permits tuning theta through laser power or detuning and time.
The d=5 skeleton contains five closed LS loops. Its derivation neglects
differences between the small D-manifold light shifts; exact equality of
those shifts is not an experimental fact. The one-gate d=5 target has full
Schmidt rank but is not a maximally entangled Bell5 state. These distinctions
matter: this paper supplies a parameterized effective gate model, not a
measured exact SUM5 channel.

[Ringbauer et al.][ringbauer] supply the local two-level rotation and
phase-compensation framework, including single-ququint benchmarking and
multi-ion addressing. Here assume independently addressed, phase-calibrated
local star rotations on every data ion, including all spectator-level phases.
They compile the local unitaries below; no arbitrary U(5) pulse is primitive.
Their demonstrated MS addressing does not itself demonstrate pair-selective
Hrmo LS gates in a seven-ququint register.

For the first bound, explicitly assume that the normalized operator (1) is
available on each required ordered pair, with all other data ions unaffected,
at the specified angles. Actual precision, pair isolation, drift compensation,
motional closure, scattering, leakage, and stability remain device obligations.
The circuit identity is exact inside that gate contract. It is not an assertion
that a finite-precision physical channel equals its ideal matrix.

These controls are broader than #1364/#1365, which freeze common star pulses
and one fixed unequal LS profile. Individual addressing and a usable selected
pair must not be silently imported into that earlier class. No interaction
Hamiltonian proportional to a product of integer label operators is assumed.

## 2. Data encoding and the exposed contact compiler

Encode the seven physical basis labels directly as

```text
(x,u,y,w,q,r,s) in F5^7,
C:(x,u,y,w,q,r,s) -> (x,u-2s(y-x),y,w+2s(y-x),q,r,s).
```

Thus x,u,y,w are the centered coordinates themselves. No physical centering
operation is included in the main resource count. If one instead encodes raw
labels p1,p4,p1p,p4p, the conversion is

```text
K:(p1,p4,p1p,p4p) -> (p1-1,p4-3,p1p-4,p4p-2),
raw contact = K^-1 C K.
```

That version adds four local shifts and their four inverses.

The [previous control proof][previous-control] gives

```text
F|z> = 5^(-1/2) sum_m omega^(mz)|m>,   omega=exp(2 pi i/5),
C = F_uw^dagger D F_uw,
D = diag omega^[2s(y-x)(m_w-m_u)].
```

The reversible change `y<-y-x`, `m_w<-m_w-m_u` and its inverse use four
SUM-type gates. Put a=s, b=y-x, c=m_w-m_u in that chart. The identity

```text
(a+b+c)^3-(a+b)^3-(a+c)^3-(b+c)^3+a^3+b^3+c^3=6abc=abc
```

gives seven completed compute/phase/uncompute gadgets, with cubic phase
coefficients 2 on the triple and singletons and -2 on the three pairs.
Their computes and uncomputes use another ten SUM-type gates. Hence the
unoptimized centered circuit uses exactly fourteen SUM gates with gains
`k=+1` or `k=-1`, seven local `Q(k)=diag omega^(kz^3)`, and four local
Fourier transforms. All pivots may be occupied; their labels are restored.
This is an operation count of the displayed construction, not a minimum.

Fix the chronological gadget order as `abc, ab, ac, bc, a, b, c`.
Use c as the pivot for abc, ac and bc, and b as the pivot for ab.
Each gadget computes its sum onto that occupied pivot, applies its Q phase,
then uncomputes; the singleton gadgets need no SUM. Including the chart
change and its inverse, this fixes the required directed SUM pairs and
the corresponding two-ion entangler requirements:

| Logical control,target | SUM occurrences | G occurrences | Physical ion pair |
|---|---:|---:|---|
| x,y | 2 | 8 | (2,4) |
| u,w | 2 | 8 | (3,5) |
| s,w | 4 | 16 | (1,5) |
| y,w | 4 | 16 | (4,5) |
| s,y | 2 | 8 | (1,4) |

The physical indices use the CARRIER allocation
`s:1, x:2, u:3, y:4, w:5, q:6, r:7`.
Thus pair selection is required on exactly these five edges in this
unoptimized construction, with full spectator protection on each use.

## 3. Four light-shift gates implement a phase-exact normalized CZ5

For each c in F5 define the local reflection and a matching projector

```text
J_c|y> = |c-y>,
P_c = sum_(x+y=c) |x,y><x,y|.
```

J_c is its own inverse. Conjugation changes the equal-label test in (1):

```text
G_c(theta) = (I tensor J_c)^dagger G(theta)(I tensor J_c)
           = exp(i theta) exp(-i theta P_c).            (2)
```

The five projectors P_c are orthogonal and sum to identity. For nonzero
gain k in F5 choose

```text
theta_c = -(2 pi/5) 3k c^2    modulo 2 pi,   c=1,2,3,4,
A_k|x> = omega^(-3k x^2)|x>.
```

The omitted c=0 gate is identity. Since `1^2+2^2+3^2+4^2=30`, the common
phase from the four normalized G_c factors is

```text
exp(i sum_c theta_c)=omega^(-3k*30)=1.
```

On |x,y> their product consequently has phase `omega^[3k(x+y)^2]`.
The local correction gives the exact identity

```text
CZ_k := (A_k tensor A_k) product_(c=1)^4 G_c(theta_c),
CZ_k|x,y> = omega^[3k((x+y)^2-x^2-y^2)] |x,y>
          = omega^(kxy)|x,y>,                           (3)
```

because 6=1 in F5. The diagonal factors commute; each local conjugation
must still be completed. Formula (3) uses the measured family's ideal
matching-phase action, not a postulated N tensor N coupling.

With the stated positive-exponent Fourier convention,

```text
SUM_k = (I tensor F^dagger) CZ_k (I tensor F),
SUM_k|x,y> = |x,y+kx> .                                 (4)
```

Indeed its output coefficient is `5^(-1) sum_m omega^[m(y+kx-y')]`.
This fixes the Fourier sign and all input-dependent phases.
For k=+/-1, the four angles are two copies each of +4pi/5 and -4pi/5
(equivalently 6pi/5), with their assignments exchanged when k changes sign.
No negative physical duration is requested: gate parameters represent the
chosen angle modulo 2pi. Their availability must be calibrated at those angles.

## 4. Global phase, local determinants, and addressed pulse compilation

Each J_c has one fixed point and two transpositions, hence determinant one.
Also `det A_k=omega^(-3k*30)=1` and `det Q(k)=omega^(100k)=1`.
These local operations belong to SU(5) and can be compiled without an
unrecorded relative phase. A Fourier transform can be supplied with a
known scalar phase; its actual inverse cancels that scalar in a sandwich.

The normalized G of (1) fixes its common phase by convention. If the actual
implemented gate is `G_tilde(theta)=exp(i alpha(theta)) G(theta)`, equations
(3)-(4) acquire the scalar `exp(i sum_c alpha(theta_c))`. It is independent
of x,y and is not a hidden controlled phase on the source.
The fourteen-SUM contact then carries the sum of the 56 physical gate phases,
plus any explicitly retained local implementation phases. When the same two
angle implementations are reused, the G contribution is

```text
Phi_C = 28[alpha(+4pi/5)+alpha(-4pi/5)]  modulo 2pi.     (5)
```

Thus the normalized circuit is literally C, and the physical idealization
with these phases is `exp(i Phi_C) C`. Its isolated channel is exactly the
same. Literal operator equality requires accounting for that scalar; a
coherently controlled whole-circuit branch requires its correction or explicit
retention as a relative phase. No unmeasured global phase is certified here.

For a conservative local resource bound, use resonant star rotations

```text
R_(0,j)(beta,phi)=exp[-i beta(cos(phi)X_(0,j)+sin(phi)Y_(0,j))/2],
j=1,2,3,4,
```

with identity on the other three levels. Laser-phase conventions must be
translated to this mathematical convention and spectator phases compensated.
A rotation between two nonzero levels is a conjugated star rotation using
two star pi pulses and one variable rotation: at most three pulses.
Complex Givens elimination of a 5 by 5 unitary needs at most ten two-level
rotations, followed by four determinant-one relative phases. Each relative
phase on levels 0,j has a three-equatorial-pulse Euler decomposition.
Therefore at most `10*3+4*3=42` addressed star pulses suffice for each
SU(5) macro. Fourier matrices use an SU(5) representative with the paired
scalar convention above. This deliberately loose bound needs no extra level.

An exact X5 cycle needs only four star pi pulses. For the convention above,
apply R_(0,1), R_(0,2), R_(0,3), R_(0,4) chronologically with phases
`pi/2,-pi/2,pi/2,-pi/2`. Direct substitution gives |j> -> |j+1 mod5>
with coefficient one on every column. Inverses use reversed adjoint pulses.
This also verifies that the cyclic-echo pulse count below can include the
complete occupied amplitude space rather than population permutations alone.

## 5. Resource counts and physical-time sums

Count every local one-ion macro separately and perform operations serially
for an upper bound; do not claim an optimized parallel schedule.
One unoptimized SUM in (4) contains four G gates, eight J_c occurrences,
two A_k occurrences and two Fourier occurrences. Consequently:

| Centered-contact resource | Count |
|---|---:|
| Normalized G(+/-4pi/5) gates | 56 |
| J_c local reflection macros | 112 |
| A_k local quadratic phases | 28 |
| Fourier macros, including the four outer ones | 32 |
| Local cubic Q macros | 7 |
| Local macros outside the G implementations | 179 |

Using the published five-loop cyclic-echo skeleton for each G gives 280 LS
loop segments and 560 local X5 cycles (five on each of two ions per G).
The cycles use at most 2240 star pi pulses. The other 179 macros use at
most 7518 star pulses by the bound above: at most 9758 star pulses in total,
besides the 280 LS segments. These are conditional counts, not fitted device
performance. The raw-label version adds eight shift macros; a uniform
42-pulse bound gives at most 10094 star pulses instead.

For actual compiled pulse lists, the serial elapsed time is exactly the sum
of their durations plus their switching/waiting overheads. At macro level,

```text
T_C = sum_(56 occurrences) T_G(theta)
    + sum_(112 occurrences) T_J + sum_(28 occurrences) T_A
    + sum_(32 occurrences) T_F + sum_(7 occurrences) T_Q
    + T_overhead.                                     (6)
```

Each T_G includes its loops, cyclic echoes and internal overheads, so these
must not be added twice. In a completed one-mode loop model, a loop duration
is `2pi/|delta|`. A resonant carrier pulse of area beta at fixed calibrated
angular Rabi frequency Omega has duration `|beta|/Omega`. More generally the
area is the integral of the calibrated amplitude envelope. With maxima over
the actually chosen primitive list, a serial bound is

```text
T_C <= 280 t_LS,max + 9758 t_R,max + T_total-overhead.  (7)
```

All angle-dependent calibrations enter those maxima. No experimental gate
time, numerical runtime or common Rabi frequency for all transitions is
inferred by multiplying one representative number from a paper. State
preparation, cooling, subsequent native-step emulation and readout are outside
the contact-only sum and must be added when bounding a complete experiment.

No fresh blank data register is used. This does not remove the motional bus,
its preparation and admissible state domain, laser fields, phase references,
classical controller, switching, work and environmental outputs from the
physical resource account.

## 6. Unequal-profile qualification and the existing affine symmetrization

The 280-loop count uses the exact normalized family (1). The published
approximation that the four D shifts may be treated alike is not a proof
that a real device has that exact family. Calibration must either bound
the discrepancy or replace the idealization with a different declared model.

An existing exact effective-model option is the twenty-affine construction
of #1364/#1365. Its algebra also explains this issue transparently. Let one
completed, motional-closed LS loop have a fixed diagonal spin propagator

```text
L|j,k> = exp(i phi_jk)|j,k>.
```

For each a!=0 and b in F5, let `P_(a,b)|j>=|aj+b>` and conjugate L by the
same permutation on both ions. The twenty diagonal conjugates commute.
An odd permutation may be represented by a scalar-adjusted SU(5) matrix;
using its actual adjoint in each conjugation cancels that scalar exactly.
For j=k, each common output label occurs four times. For j!=k, the pair
of output labels visits each ordered unequal pair exactly once. Therefore
their product is

```text
exp(i A) G(B-A),
A = 4 sum_j phi_jj,
B = sum_(j!=k) phi_jk.                                (8)
```

This does not require equal D shifts. It requires a stable common loop
profile across the conjugates, exact modeled local permutations and closure
of the admitted motional dynamics. The attainable intensity/detuning range
must allow calibration of B-A to the required +/-4pi/5; a zero or inaccessible
entangling difference is a failure of that resource premise. The common
phase A is retained in the same way as Section 4.

For a simple unoptimized implementation of (8), each of the twenty loops
is surrounded by a permutation and inverse on each ion: at most eighty
one-ion permutation macros per synthesized G. Substitution into the present
contact gives 1120 LS loops, with those permutations in addition to the 179
external local macros. This is a derived substitution bound using the older
method, not a new experimental realization, an optimized count, or a claim
that the five-loop bound survives an arbitrary unequal profile.

Neither variant proves isolation of one selected pair among seven physical
ions. The different [#1369 model][old-global] supplies a conditional global
force/refocusing construction with a 500-loop isolation step and a larger
carrier. That model cannot be imported as already calibrated pair access
here; its assumptions, spectator protection and carrier would require a
separate reconciliation. No such expanded construction is claimed in this note.

## 7. Native time versus a compiled checkpoint emulator

The circuit is an externally scheduled finite pulse sequence. It does not
make C an endogenous operation of U or align its nonzero duration with one
native tick. Nor does restoration of labels at completed gadget boundaries
establish preservation of a physical source throughout each pulse.

A narrower digital-emulation contract is possible. Prepare the declared H0
family, encode its receiver coordinates in the seven-ion register, and keep
the logical counter in an explicit classical compiler/controller. On that
family the trace at each time is known independently of the source values:
`z0=z1=0`, `z2=2`, and `z_n=4+2 theta_(n-1)` for n>=3. The contact preserves z.
Thus the compiler can schedule the actual selected affine generator g_(i_n)
at each logical checkpoint without measuring the unknown receiver amplitudes.
Each fixed generator is itself a complete affine basis permutation and can
be compiled separately; the noninjective global selector map is not promoted
to a unitary on all possible initial sheets.

For a chosen finite horizon and fixed N, let E_n be the encoding at the
completed checkpoint and choose strictly increasing physical times tau_n.
The required ideal endpoint contract is

```text
Phi_n(E_n(v,s)) = E_(n+1)(G_n(v),s),          n!=N,
Phi_N(E_N(v,s)) = E_(N+1)(G_N(C_s(v)),s).
```

Here Phi_n is a separately compiled channel; at n=N its chronological order
is contact first, selected native generator second. Its duration includes
both complete pulse words and overheads. This emulates the prescribed finite
checkpoint history. The exposed host counter and schedule are resources,
not an autonomous realization of the original unbounded counter or selector.

During these gate sequences, physical drift must be suppressed, tracked or
included in the compilation. If a separate analog U is assumed to keep acting
while C is being driven, the product C-then-G does not follow from this proof.
Its joint time-dependent dynamics needs its own derivation. No finite pulse
count supplies indefinite error-free operation or an all-time experimental
record guarantee.

## 8. What would need to be validated on hardware

The analytic compiler supplies explicit angles and operations; it does not
derive an overall success probability from randomized benchmarking. Average
Clifford error rates, selected-state fidelity decay, coherent calibration
errors and worst-case channel error are different quantities. The Hrmo paper
itself qualifies its decay-fit interpretation in the presence of non-Markovian
noise. Powers or products of those reported averages are not a rigorous
failure bound for this long, structured, seven-ion circuit.

A compositional bound would need a declared error metric and compatible
certified bounds for the actual primitive channels, spectator behavior and
memory across the sequence. For example, an appropriate per-operation
diamond-distance bound in a justified memoryless channel model can be summed
by telescoping; that is a different input from the reported benchmarks.
Without such inputs, only the ideal operator identity and the explicit
resource requirements above are asserted.

No microscopic identification with J, native contact selection, quantum
source preservation beyond the previously proved channel boundary, physical
owner closure or Canon promotion follows. In particular, the paper-supported
S-plus-four-D carrier and separately driven controller must remain explicit.

[reservation]: https://github.com/mathorn1973/twist-j/issues/1444
[hrmo]: https://doi.org/10.1038/s41467-023-37375-2
[ringbauer]: https://doi.org/10.1038/s41567-022-01658-0
[previous-control]: https://github.com/mathorn1973/twist-j/blob/408fc7a34cbd8113b4d5e1dac43793c7ad0270b0/notes/C-U-CONTACT-FULL-SOURCE-ADMISSION-N/CONTROL-PROOF.md
[old-claim]: https://github.com/mathorn1973/twist-j/issues/1364
[old-local]: https://github.com/mathorn1973/twist-j/pull/1365
[old-global]: https://github.com/mathorn1973/twist-j/pull/1369
