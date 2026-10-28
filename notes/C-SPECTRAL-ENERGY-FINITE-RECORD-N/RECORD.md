# An occupied archive with a prescribed finite retention window

**NON-CANONICAL, L1, conditional analytical candidate.** This note supplies
an additional finite coherent writer and its complete autonomous generator.
The construction uses an explicitly supplied clock and pointer readiness.
It is not a thermal preparation of those new resources, a spatially local
compiler, an event-selection law, or independently accepted mathematics.
No scientific executable or gate enumeration was run.

The fixed input is [PR #1766 at
`d978a455ef01506a9b8eb68c296e6ca89703710a`](https://github.com/mathorn1973/twist-j/tree/d978a455ef01506a9b8eb68c296e6ca89703710a/notes/C-COMMON-TEMPERATURE-PREPARATION-N).
Its complete Hamiltonian, actual input, endpoint time and read projector
are denoted by `H_66`, `rho_66`, `tau_66` and `Pi`, respectively. In this
note these are fixed mathematical inputs; the predecessor's continuous
Hamiltonian is not independently restarted after a handoff.

## 1. The physical registers and the energy contract

Write the predecessor's entire physical apparatus as `D=M tensor B`, where
`M` is its final receiver-memory block and `B` contains all other old
hardware. Use the complete raw physical memory block, including states
outside its logical code, rather than truncating it to successful outputs.
Let `d_M=dim M`. Add a fixed archive `A` isomorphic to this whole block and
with the identical onsite Hamiltonian `H_A=H_M` under that identification.
The archive need not be blank. Its admitted logical state may be occupied,
unknown and entangled with the original logical input and a passive
reference `R`.

Add a two-state pointer `P`, with bare Hamiltonian zero and a supplied
initial state `|0><0|`. Its zero means that this writer has not registered
an accepted output. It says nothing about whether the occupied archive
contains an older record. Add a clock `C` with basis `|j>`, `0<=j<=K`, bare
Hamiltonian zero, and a supplied initial state `|0><0|`. The nontrivial
clock energy is the interaction generator defined below. Degeneracy of
the pointer and clock does not prepare either pure state for free.

Let `Q_66` be the entire additive bare Hamiltonian called `H_0` in #1766,
including all its old information, work, donor, fuel, counter and cursor
factors. Define

\[
 Q=Q_{66}+H_A.                                           \tag{R1}
\]

The endpoint unitary and acceptance test satisfy

\[
 T=\exp(-i\tau_{66}H_{66}/\hbar),\qquad [T,Q_{66}]=0,
 \qquad [\Pi,Q_{66}]=0,\qquad \Pi=I_M\otimes\Pi_B.
                                                               \tag{R2}
\]

The first identity follows from #1766 H16. Its P16 retains the complete
outer-tail condition and the transported old-tail, completion-latch and
acceptance-flag conditions. These are computational-basis occupation/flag
projectors on hardware separate from the final memory, so they commute
with the additive diagonal energy and act trivially on `M`. This uses
the named memory block, not the entire final row containing both memory
and control. The predecessor's ultimate accepted logical map is uniform
over all admitted memory labels and references; see [#1746 PROOF.md,
Section 5](https://github.com/mathorn1973/twist-j/blob/01acc42b78f75095587765e9a5b91ee70dc28f37/notes/C-FORWARD-ONLY-CAPTURE-FILTER-N/PROOF.md).
Any alternative memory/control identification must prove (R2) again.

The initial joint data/reference density `rho_DAR` has the predecessor's
admitted input on `D`, with its thermal hardware independent of the
admitted logical/reference input. The passive reference `R` is disjoint
from `D,A,P,C`. The predecessor's input theorem may temporarily treat
`A` as part of its passive reference during `T`; the writer then acts on
`A`, so it is no longer a passive reference factor during the whole law.
Require

\[
 [Q\otimes I_R,\rho_{DAR}]=0.                            \tag{R3}
\]

For example, the archive's entire admitted logical code may occupy one
fixed energy, just as the inherited logical code does. Arbitrary
entanglement inside these fixed-charge logical spaces is allowed.
This condition prevents an unaccounted free rotation of the desired
archive state. Without (R3), a separate comparison with its free
`exp(-itQ/hbar)` evolution is needed. Such a broader promise is not used.

## 2. A reversible writer for an already occupied archive

Let `S=SWAP_(M,A)` on the two identical raw memory blocks. On all raw
apparatus, archive and pointer states, define

\[
 V=(I-\Pi)\otimes I_{AP}+\Pi\,S X_P.                    \tag{R4}
\]

Here and below untouched identities are implicit. The three factors
`Pi`, `S` and `X_P` commute. Thus `V^dagger=V` and `V^2=I` on the complete
raw space, including either initial pointer value and every failed or
defective old input. Identical memory spectra give

\[
 [S,H_M+H_A]=0,\qquad [V,Q]=0.                          \tag{R5}
\]

For a ready pointer the accepted sector is tagged by `P=1` and its
memory is moved into `A`; the old archive contents move into `M`.
The rejected sector is tagged by `P=0` and its archive is unchanged.
This exchanges unknown quantum states instead of copying them. It
preserves every correlation with `R` by an operator identity, without
assuming independence of old memory and archive.

Before any read, the joint state retains coherence between these pointer
sectors. The additional fixed pointer instrument, if one elects to apply
it, is

\[
 {\cal J}_b(\rho)=P_b\rho P_b,\qquad
 P_b=I_{DA}\otimes|b\rangle\langle b|_P,
 \qquad b=0,1.                                          \tag{R6}
\]

Its effects sum to the identity and it operates on the new physical
pointer alone. At the completed word, with a ready pointer, its data
Kraus operators are `S Pi T` and `(I-Pi)T`. No failure outcome is deleted.
Equation (R6) specifies a possible terminal read instrument. It is not
inserted into the autonomous evolution proved below, and it is not a
material detector or a rule selecting one outcome. In particular the
time of an external application of (R6) is not a hidden switching event
in the generator.

## 3. One complete positive autonomous Hamiltonian

Fix an integer `K>=2`. Put `U_0=T tensor I_AP`, `U_1=V`, and `U_j=I`
for `2<=j<K`. These are full raw-space unitaries. For `g>0` set

\[
 a_j={g\over K+1}\sqrt{(j+1)(K-j)},\qquad
 H_{\rm hist}=gI-
 \sum_{j=0}^{K-1}a_j\bigl(
 |j+1\rangle\langle j|_C\otimes U_j+
 |j\rangle\langle j+1|_C\otimes U_j^\dagger\bigr),
\]
\[
 H=Q+H_{\rm hist}.                                      \tag{R7}
\]

Let `F_0=I`, `F_j=U_(j-1)...U_0`, and
`G=sum_j |j><j| tensor F_j`. The exact unitary gauge gives

\[
 G^\dagger H_{\rm hist}G
   =gI-{2g\over K+1}J_x\otimes I,
\]
\[
 {g\over K+1}I\le H_{\rm hist}
       \le {g(2K+1)\over K+1}I,
 \qquad [Q,H_{\rm hist}]=0.                             \tag{R8}
\]

Hence the Hamiltonian is positive and time independent on its entire
declared finite Hilbert space. Both directions of every edge are present.
The gauge is a proof device; it does not identify the physical energy
with the original object's spectral energy. `Q` is precisely the
declared extended additive account (R1).

The edge containing `T` can act on the complete old apparatus, and the
writer uses the complete predicate `Pi`. No bound of seven sites,
Manhattan radius four, fixed degree, or efficient circuit complexity is
claimed for these two new edges. A spatially local implementation with
all its additional readiness and energy costs is a separate obligation.
The predecessor's locality result does not transfer merely because its
endpoint matrix appears in (R7).

The old interactions are encoded through `T`; `H_66` is not added a
second time to (R7). This construction implements the old endpoint and
the new writer. It does not preserve the old continuous trajectory.

## 4. The record alone, without a clock-gated read

For the supplied clean new seeds and (R3), let
`rho_in=|0><0|_C tensor |0><0|_P tensor rho_DAR`. The exact clock norm
weights under (R7) are

\[
 p_j(t)={K\choose j}\sin^{2j}\theta\cos^{2(K-j)}\theta,
 \qquad \theta={gt\over\hbar(K+1)}.                     \tag{R9}
\]

The free `Q` phases cancel in the density operator because of (R3) and
(R8). After tracing only `C`, the complete data/pointer/reference state
is the mixture of the unchanged input at `j=0`, the completed old
endpoint with pointer still zero at `j=1`, and the same completed
`VT` output at every `j>=2`. Define

\[
 w(t)=\sum_{j=2}^Kp_j(t),\qquad \beta(t)=1-w(t),\qquad
 \rho_{\rm fin}=VT(\rho_{DAR}\otimes|0\rangle\langle0|_P)T^\dagger V^\dagger.
                                                               \tag{R10}
\]

Consequently, for `D(rho,sigma)=||rho-sigma||_1/2`,

\[
 D(\rho_{DAPR}(t),\rho_{\rm fin})\le\beta(t),\qquad
 D(\rho_{APR}(t),\rho_{{\rm fin},APR})\le\beta(t).        \tag{R11}
\]

This is a bound on the new archive and pointer with its reference,
without reading, postselecting or including the new clock in the record.
The fixed sites `A,P` do not move along a row. No earlier prefix touches
them. In particular a dirty auxiliary row cannot masquerade as a ready
final pointer: such rows remain inside the old `D`, whereas `P` is an
explicitly new prepared factor.

There is a stronger exact statement for the accepted instrument. Let

\[
 \Sigma=S\Pi T\rho_{DAR}T^\dagger\Pi S^\dagger,
 \qquad p_{66}=\operatorname{tr}\Sigma.                 \tag{R12}
\]

Tracing the new clock and applying `P=1`, while retaining the full old
data, archive and reference, gives exactly

\[
 \sigma_{\rm rec,acc}(t)=w(t)\Sigma,
 \qquad p_{\rm rec}(t)=w(t)p_{66}.                       \tag{R13}
\]

Neither unfinished prefix can fire the new pointer. Thus, whenever
`w(t)>0`, the normalized accepted state is exactly `Sigma/p_66`.
The time-dependent factor cancels; it does not cause additional
conditional-state error. All old thermal defects and old false
acceptances remain inside `Sigma`, because `T` acts on the entire old
raw space. This is not an assertion that those old components are ideal.

## 5. A duration chosen before the evolution

Choose `K=64`. For `theta in [pi/3,2pi/3]` one has `p=sin^2 theta>=3/4`.
The binomial probability of fewer than two completed edges decreases
with `p`, so

\[
 \beta(t)=(1-p)^K+Kp(1-p)^{K-1}
 \le{1+3K\over4^K}
 ={193\over2^{128}}<2^{-120}=:\beta_* .                  \tag{R14}
\]

The monotonicity also follows by differentiating: the derivative is
`-K(K-1)p(1-p)^(K-2)<=0`. These are exact expressions and inequalities,
not a simulated clock or an estimate of experimental performance.

For any requested finite duration `T_h>0`, choose, before evolution,

\[
 g={\pi\hbar(K+1)\over3T_h}.                            \tag{R15}
\]

Then every time in the prescribed interval `[T_h,2T_h]` satisfies
(R11)-(R14). The exact completion peak is at
`tau=3T_h/2`. Increasing `T_h` at fixed `K` rescales the entire interaction
strength and the latency as well as the retention window. It is not
longer storage at unchanged couplings and unchanged acquisition time.
Physical calibration of `g`, `hbar` and laboratory time is an additional
implementation premise.

For the ideal new seeds the inherited conditioned channel error from
#1766 P22 is therefore unchanged on its declared reduced output. In
(R16) and (R20), apply that predecessor's output reduction after moving
its memory factor from `M` to `A`, and retain any desired subset of the
old output/reference factors. The previous archive contents, moved to
`M`, may be retained as the formerly passive archive factor. The object
is retained when its unwanted-band observable is evaluated. No ideal
product or channel approximation is asserted for the old donor, work
and row junk that the predecessor's comparison traces out. Equation
(R13), by contrast, is an exact identity on the whole raw `D,A,R`.
With this reduced-output convention:

\[
 D(\rho_{\rm rec,acc},\rho_{\rm rec,acc}^{\rm ideal})
       <75000\,2^{-78},\qquad
 u_{\rm rec,acc}<10^{-6}.                               \tag{R16}
\]

The ideal channel here has the additional `M,A` exchange. The complete
logical transformation is this exchange composed with the predecessor's
occupied-memory transfer, not a second identical copy of the input.
Reference-uniformity follows by treating `A` as part of the old passive
reference until the exchange.

Using only the black-box inequality `p_66>1/75000` would yield
`p_rec>(1-beta_*)/75000`, not the identical old strict threshold. The
source supplies the stronger margin in P19-P21: with

\[
 p_*={418176\over30517578125},\qquad
 p_*-{1\over75000}>{1\over3000000},\qquad
 p_{66}>p_*-2^{-78},                                    \tag{R17}
\]

one obtains `(1-beta_*)(p_*-2^-78)>1/75000`.
Thus the same numerical lower threshold survives the new finite window
by its explicit margin, not by ignoring the multiplier `w`.

## 6. Explicitly imperfect new readiness

The pure pointer and clock are additional inputs. The previous thermal
preparation does not cover them. If instead a complete supplied initial
state is within reference-uniform trace distance `zeta` of the declared
new-seed input, unitary evolution and the accepted-plus-reject instrument
give

\[
 |p_{\rm rec,actual}-w p_{66}|\le\zeta,\qquad
 D(\rho_{\rm rec,actual,acc},\Sigma/p_{66})
       \le{\zeta\over w p_{66}}.                       \tag{R18}
\]

The second bound applies when the actual accepted weight is nonzero;
it is ensured, for example, by `zeta<w p_66`. The denominator belongs
to the clean comparison output, and every false positive from a dirty
pointer or clock remains in the actual accepted state. Appending a
one-dimensional reject outcome proves the subnormalized contraction
bound needed before conditioning. No measurement filters out defects.
For an explicitly declared mixture
`rho_actual=(1-eta)rho_in+eta rho_bad`, one may use `zeta<=eta` and retain
the positive bad contribution directly; `rho_bad` evolves under the same
complete Hamiltonian.

For the optional promise `zeta<=2^-96`, a common accepted-instrument
comparison budget, including the original #1766 approximation and the
incomplete new histories, is

\[
 \varepsilon_{\rm rec}<2^{-78}+2^{-96}+2^{-120}<2^{-77}.
                                                               \tag{R19}
\]

The margin (R17) then gives throughout `[T_h,2T_h]`

\[
 p_{\rm rec,actual}>{1\over75000},\qquad
 D(\rho_{\rm rec,actual,acc},\rho_{\rm rec,acc}^{\rm ideal})
       <75000\,2^{-77},\qquad u_{\rm rec,actual,acc}<10^{-6}.
                                                               \tag{R20}
\]

For the last inequality use the inherited ideal unwanted fraction
`u_0<19/(20*10^6)` and
`75000*2^-77<1/(20*10^6)`. This is a conservative common budget; (R13)
shows why the clean conditional record does not actually pay `beta_*`.
The optional readiness accuracy is an explicit new resource promise,
not something established by (R19).

## 7. Inclusive finite resources and energy

Beyond the entire #1766 hardware, the construction adds a memory block
of raw dimension `d_M`, one two-state pointer and one clock of dimension
`K+1=65`. The complete apparatus dimension is

\[
 \dim\mathcal H_{\rm new}=130\,d_M\dim\mathcal H_{66}.
                                                               \tag{R21}
\]

It adds the whole archive energy capacity `||H_M||`, not merely its
successful logical state. All old failed inputs, old work and donors,
and every newly declared raw pointer and clock state belong to (R7).
The pointer's readiness and clock's localization are supplied entropy
and timing resources even though their bare Hamiltonians vanish.

For the clean ready clock, with `mu_Q=<Q>`, the exact full-generator
moments are

\[
 \langle H\rangle=\mu_Q+g,\qquad
 \operatorname{Var}(H)=\operatorname{Var}(Q)
                +{g^2K\over(K+1)^2}.                  \tag{R22}
\]

The variance of `Q` contains all old/archival covariances. The clock
diagonal is the constant `g`; the only edge leaving vertex zero has
`a_0^2=g^2K/(K+1)^2`. Its data unitary cancels on the return edge.
The cross covariance with `Q` vanishes in the ready clock input.
These facts prove (R22) without assuming a sharp old hardware energy.

For an imperfect input use its actual expectations of `H,H^2`. In the
explicit mixture above, with component means `mu_g,mu_b` and variances
`v_g,v_b`, the exact variance is

\[
 (1-\eta)v_g+\eta v_b+\eta(1-\eta)(\mu_g-\mu_b)^2.
                                                               \tag{R23}
\]

The finite capacity bound
`||H||<=||Q||+g(2K+1)/(K+1)` controls these terms; a small bad-input
probability is not a reason to discard its energy. For a trace-distance
readiness promise one may use
`|Delta<H>|<=2 zeta ||H||` and
`|Delta<H^2>|<=2 zeta ||H||^2`.

This energy is the declared apparatus account. The result does not
identify `Q_66` with the original object's spectral `H_W`, prove an
unchanged native law, or close the spectral-energy bridge discussed in
the companion energy analysis.

## 8. Reversal, recurrence and the precise remaining boundary

On the complete finite history, at `2tau=3T_h`,

\[
 U_{\rm hist}(2\tau)=
 e^{-i\pi(K+1)}e^{i2\pi J_x}=-I.
                                                               \tag{R24}
\]

Together with (R3), the clean initial density is exactly restored.
The pointer returns to zero, the new archive transfer is undone, and
the old archive contents return to their original location. A supplied
initial density within distance `zeta` of that clean state has pointer-one
weight at most `zeta` at this return. The ideal writer therefore gives
finite retention with a preset error bound, not a permanent archive.

This is consistent with two elementary restrictions. A fixed memory
projector commuting with the same Hamiltonian has constant expectation
and cannot be populated from an initially absent record. More generally,
finite-dimensional unitary recurrence excludes indefinite preservation
of a newly distinguishable record under a fixed read against an initial
absence preparation. The proposed writer explicitly does not commute
with the pointer: it can write and later undo it.

The finite-window theorem concerns uninterrupted closed evolution.
Applying the read instrument (R6), coupling an external detector, or
disconnecting an archive changes the experimental contract; no
postmeasurement retention theorem is silently imported. A future
material implementation must give that contact, its readiness and energy
account, and its own continuation bound if such an operation is used.

The positive partial result is a complete reversible inscription into an
occupied physical archive and a quantitative reference-uniform retention
window observable from the archive and pointer alone. Its new supplied
seeds and potentially global matrix couplings remain explicit. Coherent
registration does not select an observed event, and no reset, indefinite
halt, locality upgrade, thermal-origin claim or scientific promotion
follows.
