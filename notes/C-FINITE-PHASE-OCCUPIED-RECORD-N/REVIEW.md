# Same-session analytical challenge and disposition

**PUBLIC / NON-CANONICAL / L1. Conditional analytical candidate-T.**
Author: A. M. Thorn. Date: 2026-10-25. Apache-2.0.
Reservation: [#1775](https://github.com/mathorn1973/twist-j/issues/1775).

This is a separately reasoned analytical contribution within the same
authoring session. It is not independent external acceptance, an additional
formal review, a computational reproduction or a Canon promotion. The
reviewer reconstructed the primary symmetry, complete one- and two-step
channels, and active-contact second moments from the pinned source
definitions before reading the finished derivations. The accompanying
CONTRACT, EXPERIMENT, SPECTRAL, CONTACT and RESOURCES texts were then read
and compared with those reconstructions. No scientific executable,
simulation, expanded circuit or numerical spectral evaluation was run.

The source is Public Canon v105 at
`892a0b11089d34e241e1eb76d2c03247022d18e6`, content
`b8cdfd6ea58ae798545bc6000c817147fa0f0dcc`. The actual object coin,
streaming order, contact ports, pulse symbol and receiver calibration were
read in the pinned `C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N` source
proofs. The common numerator and Borel-energy definitions are scoped
inputs from #1741 and #1772, not new theorems of this review.

**Disposition:** no blocking mathematical correction remains in the
checked statements below. The primary receiver experiment agrees with
the reserved label, ready-subspace and readout contract. The stronger
equal-spectrum statement for the active-contact phase pair fails, and
CONTACT correctly retains an exact witness of that failure. External
acceptance remains pending.

## 1. Reducing sector and full spectral symmetry

The object exchange sends `r` to `-r` and exchanges coins 2 and 3. It
commutes with the identical tensor-factor object coin, the streaming
displacements and the contact phase at `r=0`. Thus it commutes with
the complete object walk `W` in both time directions.

The relevant reducing space is specifically the **object-odd pulse
space**. Its vectors are orthogonal to the exchange-even object vector
`A` in every pulse contact port, and to every token port by arrangement
type. Both `C` and `C*` are identity there. The free operator and its
adjoint preserve this space, and the receiver calibration acts trivially
on object parity. This establishes a reducing space of the full
`U_rec`. Global object exchange alone need not commute with `C`: its
token port is odd and its pulse port is even. The proof does not make
that stronger, invalid assertion.

For the exact pulse symbol, direct two-by-two multiplication gives

\[
J_cV(-k)=V(k)J_c,\qquad
J_c=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\]

Reflection about 99 supplies the momentum reversal and the scalar
Fourier factor. The resulting pulse unitary commutes with `V`. Extending
it by identity on the **reducing** complement is therefore a valid
unitary symmetry of the complete uncalibrated law. Conjugating that
symmetry by the same fixed receiver calibration gives an exact symmetry
of `U_rec`, including its token, even-pulse and occupied-memory sectors.
It is a proof device, not an implemented additional gate.

At the input site 99 the calibration is identity for every old memory.
The reflection fixes that site and `J_c v_+ = -v_-`. The full symmetry
therefore maps the two admitted inputs to one another up to one global
sign while keeping the old memory/reference factor unchanged. Since it
commutes with the full unitary, it commutes with all its spectral
projections. Equality follows for every Borel spectral event, and hence
for the entire distribution of the same prescribed `H_*=f(U_rec)`.

This checks the full spectral claim rather than an equality of a free
energy, occupation charge, first moment or finite sequence of moments.
No limiting interchange through a discontinuous Borel logarithm is used.
The energy scale and its physical identification are not established.

SPECTRAL's additional real-coin statement also checks: compression of a
spectral projection to a fixed odd object state and one pulse site gives
a Hermitian matrix commuting with `J_c`. It has form `a I+b J_c`.
Every real normalized coin has expectation `a`, because its real
skew-symmetric quadratic form vanishes. The argument does not extend
that conclusion to every complex coin.

## 2. First readout, correlations and the reserved label

Applying the on-site pulse coin and then the edge operator gives the
four amplitudes in EXPERIMENT. For `v_+` they are, in the order
`(98,1),(99,1),(99,2),(100,2)`,

\[
\frac{1}{5\sqrt2}(-6,-1,3,-2),
\]

and for `v_-` they are

\[
\frac{1}{5\sqrt2}(-2,3,1,6).
\]

The corresponding spatial weights are `18/25,1/5,2/25` and
`2/25,1/5,18/25`, where the two on-site banks have been grouped only
for this norm check. The relative bank phase changes an amplitude in
one common outgoing configuration. It is not a global-phase effect.

On the rightmost output, the original receiver operation exchanges
`p_0` with the old receiver state. For arbitrary reference vectors it
maps

\[
 |p_0\rangle\sum_{j=1}^{25}|d_j\rangle|\phi_j\rangle
 \longmapsto
 \sum_{j=1}^{25}|p_j\rangle|d_0\rangle|\phi_j\rangle.
\]

The other three spatial components leave the old state in the receiver.
These identities retain nonorthogonal reference vectors, their
coherences and mixed states by purification. The complete output retains
the off-diagonal terms between spatial branches until a specified
instrument or partial trace removes them.

The contracted readout is the original receiver-only projector onto
`d_0`. It agrees with the auxiliary right-arrival projector **on this
output family**, because the unchanged old state belongs to
`K=span(d_1,...,d_25)`. The two projectors are not equal on the whole
Hilbert space. The exact receiver weights are consequently

\[
p_1(\theta)=\frac{10-8\cos\theta}{25},\qquad
p_1(0)=\frac2{25},\quad p_1(\pi)=\frac{18}{25}.
\]

The derived source effect has eigenvalues `4/5,0`, and its phase-only
contrast at fixed populations is `32|a||b|/25 <=16/25`. The stated
sharpness has the declared one-site, two-bank, one-step scope.

The full-26-state flag obstruction is also valid. Positivity forces
any effect with zero false indications on every unchanged old state to
annihilate the old-state subspace. Unit indication on `d_0` then
requires that subspace to be orthogonal to `d_0`, so its dimension is
at most 25. The selected subspace saturates the bound. Admitting every
old receiver state would force the effect to vanish. This says nothing
against coherent SWAP on all 26 states or a detector with separately
declared history resources.

## 3. Two-time distinction, inverse and current

The eight amplitudes of `V^2` in EXPERIMENT were reconstructed by
convolving its on-site, left and right two-by-two coefficient matrices.
The two column norms are one and their scalar product is zero. The
right-half effect is

\[
\frac1{625}\begin{pmatrix}96&-112\\-112&464\end{pmatrix},
\]

which gives the uninterrupted final weights

\[
p_{2,\mathrm{unread}}(\theta)
 =\frac{280-112\cos\theta}{625}.
\]

If the declared receiver Lueders instrument is applied after the first
step, the second final weight is instead

\[
p_{2,\mathrm{read}}(\theta)
 =\frac{260-120\cos\theta}{625}.
\]

The difference `(20+8 cos(theta))/625` is the omitted interference
term between the two first-time alternatives. The complete four-entry
joint tables in EXPERIMENT agree with this reconstruction and sum to
one. Neither table is used as the other experiment's prediction.

From a first-written state at `(100,2)`, the return coefficient to
`(99,1)` is `-2/5`. Thus the conditional second-time no-write weight
is `4/25`; the complementary weight is `21/25`. On return, the same
unitary swap restores the entire old memory/reference state and the
carrier label `p_0`. These are conditional/sequential statements, not
an attribution of unmeasured classical histories. The displayed full
inverse correctly reverses the unmeasured joint state; it does not
reverse a discarded measurement record or provide resource renewal.

The claimed native current across cut 99 is also correct for the
primary input. Both object constituents remain left of that cut for
the first step; the receiver charge stays two. Only the pulse charge
four crosses. Consequently

\[
\langle J_{99}\rangle_+=\frac8{25},\qquad
\langle J_{99}\rangle_-=\frac{72}{25}.
\]

This is the inherited occupation-charge current, with no asserted
identification as a local current of `H_*`.

## 4. Active-contact result and the failed equal-spectrum extension

For the separate source `(3 alpha+4 eta gamma)/5`, the actual contact
rotation gives

\[
a_C=\frac{9-16\eta}{25},\qquad
b_C=\frac{12(1+\eta)}{25}.
\]

The complete subsequent pulse front has coefficient `2 b_C/5`.
The reserved-label receiver effect therefore has weight
`1152(1+Re eta)/15625`, giving `2304/15625` and zero for the two
settings. The token complement, all pulse outputs, their distinct
object factors and the old-memory/reference transfer are retained in
CONTACT. The counterfactual removal of `C` is explicitly only an
analytical control and does not change the implemented experiment.

The zero is a statement about the first conversion and readout. It
does not establish an invariant dark source: the token object has a
nonzero two-step return to its contact port, as CONTACT's own return
amplitude demonstrates. The active-contact source also already includes
a pulse component and tests no bound-state projector.

The second-moment witness was checked independently. The object return
amplitudes are `4 zeta^(-1)/5` on `iB` and `4 zeta^(-2)/5` on `A`;
the pulse return is `-7/25`. The only possible intervening contact
correction is at 98. Its token remains there, and its right-moving
pulse reaches bank 2, so neither can return to the tested original
ports in one more step. The global factor `zeta^(-4)` is retained.
It cancels the first object return phase and leaves `zeta^(-1)` in
the second. This gives precisely

\[
\langle\psi_-,U_{\rm rec}^2\psi_-\rangle=\frac{12}{25},
\qquad
\langle\psi_+,U_{\rm rec}^2\psi_+\rangle
 =-\frac{84}{625}-\frac{2688\zeta^{-1}}{15625}.
\]

They are unequal. Thus the full spectral laws of this active-contact
pair differ, despite equal occupation charge and equal initial basis
probabilities. The primary equal-spectrum conclusion is not
transferable. This witness does not by itself decide equality or
inequality of a particular Hamiltonian mean.

## 5. Finite resources, error bounds and limits

The four-port nominal source block in EXPERIMENT is unitary on every
one of its four columns and identity on its complement. Its full
coefficients are rational half-integers at the two declared phases.
Its inverse is explicit. This supplies a mathematical preparation and
does not derive a local or original-six-pentit preparation mechanism.

The primary causal coordinate bounds and
`16(2n+1)^3 26^2` basis-state bound in RESOURCES are conservative finite
upper bounds. The corresponding contact count
`12(2n+1)^3 26^2` includes both arrangements and both pulse banks.
The passive reference is an unchanged factor; no finite classical
description of that arbitrary unknown state is assumed.

For a fixed basis old memory, the primary source has four raw
coefficients `+/-1` and common Hilbert normalization two. The inherited
recurrence therefore reads `a_n=A^n a_0` and
`psi_n=iota(a_n)/(2*25^n)`. The text correctly restricts a finite
integer description of a whole state to inputs with the corresponding
arithmetic promise. Arbitrary complex memory/reference amplitudes are
covered by operator linearity, not converted into finite integer data.
Finite support and finite exact specifications do not bound material
carry latency or all-time precision cost.

Trace-distance preparation bounds, half-diamond step bounds and the
operator-norm effect bound compose as stated. In particular their
primary contrast lower bound subtracts both preparations, both copies
of the common step error and both effect errors. The `1/100` parameter
example gives `29/50`. The spectral-distribution error statement
compares perturbed initial states against the same fixed `H_*`; it
does not claim stability of a discontinuous logarithm under arbitrary
operator perturbations or conservation under a different channel.

The final reading is a declared mathematical instrument. The results
are its L1 weights and coherent channel identities. They do not derive
individual occurrences, empirical frequencies, physical energy units,
an autonomous preparation/read clock, a persistent record, renewed
stock or the selected spatial model from the original six-pentit rule.
The primary experiment leaves conversion inactive; the secondary
experiment exercises conversion but supplies its coherent contact
source. These limitations are part of the checked conclusion.

## 6. Separately marked active equal-spectrum supplement

`ACTIVE_EQUAL_SPECTRUM.md` was subsequently reviewed as a separately
marked, result-exposed analytical extension. It leaves the frozen primary
input and its proof unchanged. This contribution checked its conceptual
spectral, support, preparation and reference arguments from the source
definitions, then read the actual supplement. It did not independently
reconstruct every fifth-step path coefficient. The finite cross-term and
fourth-moment derivations have their own analytical checks; the numerical
inequalities below are conditional on those displayed exact coefficients.
No scientific executable was run for this extension either.

### 6.1 Exact spectral identity and one common normalization

For any unitary `U`, the operator
`D_theta=exp(i theta)U^2-exp(-i theta)U^(-2)` is skew-adjoint. The
norms of `(I+D_theta)chi` and `(I-D_theta)chi` therefore coincide
and equal `Z=1+||D_theta chi||^2`. On the unit circle its scalar
value is purely imaginary, so the two full spectral measures are
exactly the same measure

\[
\frac{1+|d_\theta(z)|^2}{Z}\,d\mu_\chi(z).
\]

The bounds `1<=Z<=5` follow directly from `||D_theta||<=2`.
For `theta=0`, `Z=3-2 Re<chi,U^4 chi>`. This proof applies to
the actual complete `U_rec`; it needs neither a free-spectrum
substitution nor continuity of a Borel logarithm. Equality therefore
holds for every fixed Borel reading of that same unitary.

The normalized polynomial formula specifies two states for the fixed
source. It is not a claim that `(I+/-D)/sqrt(Z)` is a unitary gate
on every input, and it does not authorize inserting a backward physical
evolution between the declared forward macrosteps.

### 6.2 Equal coordinate populations and a genuinely active contact

For `chi=alpha_97`, the combined involution in the supplement is
object exchange times `+1` on tokens and `-1` on pulses. Both
contact ports have its eigenvalue `-1`, so it commutes with `C`,
the free operator and the receiver calibration. At the initial token
fiber `(R,r,y)=(97,0,97)`, its negative sector contains only the
coin line spanned by `B`. This is a symmetry of the full active
contact problem, unlike object exchange by itself.

The second return moment is `12/25`, as follows from the retained
token coefficient `3/5`, the object return `4h/5`, and the common
phase `k^2 h=1`. An initially emitted pulse cannot contribute to
the source token coordinate at that time. Consequently
`<chi,D chi>=0`. The symmetry then forces the entire projection of
`D chi` onto the two actual coordinate ports of `chi` to vanish.
This is the componentwise statement needed for equal configuration
probabilities; scalar orthogonality alone would not suffice.

The two inputs thus agree on those two ports and differ by a sign on
every other nonzero source coordinate. The difference is a relative
phase, not a global phase or a population change. Each retains the
contact-port coefficient `1/sqrt(Z)`. Since the contact rotation has
no eigenvalue one on a port pair, it changes each complete input at the
first step. Contact activity is established, without claiming that the
input is a pure token or that binding has been demonstrated.

Both forward and inverse complete steps have carrier propagation radius
one. Thus the two-step source tables have carrier coordinates in
`[95,99]`. They are wholly left of the receiver, so their common
old-memory/reference state remains untouched and the initial flag is
zero. In particular this preparation does not depend on the unknown
old memory or hide an initially written target label.

For a complete nominal preparation, the finite-dimensional extension
must be defined on the **source** space and tensored with the identity
on old memory/reference. Let `U_s` be the uncalibrated source step and
write `d_s=(U_s^2-U_s^(-2))alpha_97`,
`r=||d_s||`, and `e=d_s/r` when `r>0`. On the orthonormal source
basis `(alpha_97,e)`, the complete block

\[
G_\pm=\frac1{\sqrt Z}
\begin{pmatrix}1&\mp r\\\pm r&1\end{pmatrix}
\]

is unitary, has the explicit adjoint inverse and sends `alpha_97` to
the required source state. Extend it by identity on the orthogonal
complement; if `r=0`, use identity. Defining this block on a span
containing one particular unknown full reference vector would not give
a common preparation for all admitted references. The source-only
construction avoids that problem. Its finite specification supplies
no native, local or economical realization of the preparation.

### 6.3 Full receiver event and conditional contrast check

After three forward steps the polynomial expression is
`(U^3 +/- U^5 -/+ U)chi/sqrt(Z)`. The receiver projector kills
`U chi`, because its carrier cannot yet reach 100. Thus the stated
readout reduction and `4 Re(c)/Z` contrast identity are exact.

The only right-side component at time three is the extreme pulse front
at `(100,2)`, so the cross term may project the time-five state onto
that same front. Individual weights and the complete channel must
instead use the full right-side carrier projector, retaining both
arrangements and all right-side components. The supplement explicitly
maintains this distinction in (A5a) and (A11).

Equation (A11) is precisely the original half-line label calibration
on the entire uncalibrated evolved state. It retains coherences between
arrival and nonarrival, transfers every old-memory/reference component
on arrival, and remains an isometry for arbitrary input reference
dimension. Only the label-transfer isometry is common to the two
phases; their conditional spatial wave packets need not coincide.

Given the displayed cross term

\[
c=\frac{65536}{5^{15}}(9387-10985h)
\]

and fourth moment

\[
m_4=\frac{3600-2100h^{-1}+1792h}{15625},
\qquad h=e^{-2\pi i/5},
\]

the subsequent normalization and inequality algebra check exactly:

\[
Z=\frac{39521+154\sqrt5}{15625},\qquad
\Delta p=
\frac{65536(48533-10985\sqrt5)}
 {5^9(39521+154\sqrt5)}.
\]

Using `sqrt(5)<9/4` bounds the numerator from below and the
denominator from above. The lower bound is
`3121709056/155732421875 > 1/50`, with integer comparison
`156085452800 > 155732421875`. This final rational check does not
substitute for the separately derived finite-path inputs `c` and
`m_4`.

The raw-vector identity with `A=25 U_rec` also checks:
`625 chi_0 +/- A^2 chi_0 -/+ (A*)^2 chi_0` has the common
normalization `625 sqrt(2Z)` and finite cyclotomic coordinates.
The arbitrary-complex-memory statement remains an operator extension,
not a claim that every input has finitely many classical integer data.

No blocking conceptual correction remains in this supplement. Its
preparations are deliberately supplied coherent history combinations;
the subsequent law is unchanged. This establishes a different finite
calibration from CONTACT's two-port pair, whose equal-spectrum
extension still fails. It does not establish an incoming-unbound
capture experiment, native source manufacture, a physical energy
identification, an occurrence law, persistent retention or renewal.
The same-session status and pending external acceptance remain in force.

## 7. Separate reconstruction of the supplementary finite paths

A second analytical reviewer separately reconstructed all finite-path
coefficients and then read the complete ACTIVE_EQUAL_SPECTRUM text.
The coordinating author also reconstructed the same coefficients by
direct object-coin multiplication and pulse Laurent-polynomial
identities. These are separately reasoned checks within this authoring
session, not external acceptance or computational reproductions.

The checks covered the following concrete failure risks:

- Contact completeness: the bank-1 displacement bound and object
  parity force the four contact sites at steps2,3,4,5. Every remaining
  move must be right-moving to contribute to the tested fifth-step
  front. Repeated relevant contacts and pulse-token-pulse excursions
  cannot reach that front in time.
- Free pulse amplitudes: Cayley--Hamilton gives the fifth-step
  coefficient \(-608/3125\), and the two near-front bank-1
  coefficients \(4/25\) and \(-48/625\).
- Object coefficients: direct multiplication gives
  \(12h^3/25\) and \((20h^4+16h^3)/125\), including both contact
  phases and relative excursions.
- All six cross-term contributions and the common phase \(k^2\)
  give exactly (A8); none is replaced by an incoherent probability.
- The object fourth moment is \((80h^2-28h)/125\). The free
  retained-token contribution, the token self-contact correction
  and the returning pulse conversion exhaust the full fourth
  return moment. They give the displayed \(m_4\) and \(Z\).
- Substitution gives the exact positive contrast in (A9)--(A10) and the
  strict bound \(>1/50\).

No blocking mathematical correction was found. Two clarity corrections
were incorporated: the generic unitary is denoted separately from
the uncalibrated source operator, and moments of arbitrary Borel
readings are asserted equal only when they exist. The nominated bounded
\(H_*\) has every nonnegative integer moment.

The complete source-only preparation and two-coordinate sign selector
retain identity on unknown memory/reference and every complement.
The input still contains coherent token and pulse parts and does not
constitute incoming-unbound capture. The analytical supplement does not
repair or erase the simple CONTACT pair's unequal-spectrum result.
