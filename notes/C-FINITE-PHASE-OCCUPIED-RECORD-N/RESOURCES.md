# Finite support, exact coefficients and operational boundaries

**PUBLIC / NON-CANONICAL / L1. Conditional analytical candidate-T.**
Author: A. M. Thorn. Date: 2026-10-25. Apache-2.0.
Reservation: [#1775](https://github.com/mathorn1973/twist-j/issues/1775).

The finite experiment is specified in [EXPERIMENT.md](EXPERIMENT.md).
Its full spectral statement is in [SPECTRAL.md](SPECTRAL.md). This file
counts the admitted resources and proves uniform stability bounds. It
does not turn a mathematical state specification into a preparation by
the original six-pentit transition.

## 1. What is finite

At the initial cut the controlled source uses four orthogonal basis ports:

\[
(R,r,d;x,b,j)=(0,\pm3,1;99,1,0),\quad
(0,\pm3,1;99,2,0).
\]

The receiver has its original 26 label states. The old data can occupy the
entire 25-dimensional ready subspace

\[
K=\operatorname{span}\{d_1,\ldots,d_{25}\},
\]

including arbitrary correlations with a passive reference. One original
receiver label, \(d_0\), is reserved to distinguish a new write. The
dimension-25 bound for a perfect receiver-only flag is proved in
EXPERIMENT, not treated as a free blank-memory assumption.

The primary experiment reads the receiver after exactly one original
macrostep. The uninterrupted continuation is followed for two macrosteps.
In the admitted native spatial realization one macrostep occupies two
autonomous microticks between synchronized phase-zero cuts; this is an
inherited property of that realization, not a derivation of its spatial
gates from the original six-pentit kernel.

The initial source, the setting of its phase, and the choice to read at
that cut are supplied. An autonomous physical clock for the preparation
and observation is not constructed here.

### 1.1 A causal support bound

The primary sector remains a pulse sector and its contact is inactive
for all time. After \(n\) macrosteps its active spatial support is contained
in

\[
|R|\le n,\qquad
r\in[3-n,3+n]\cup[-3-n,-3+n],\qquad
x\in[99-n,99+n].
\]

The intervals denote integer sites. There are four object coin states,
two pulse banks and 26 labels each for carrier and receiver. Thus a
conservative bound on the number of active coordinate-basis states is

\[
D_n\le
2(2n+1)^2\cdot4\cdot(2n+1)\cdot2\cdot26^2
=16(2n+1)^3\,26^2.
\]

This overcounts intersections of the two relative-coordinate intervals,
unreachable coin-position combinations and unused label combinations.
It suffices to prove finite support without introducing a truncated
operator. The full operator remains the original infinite-space unitary;
only the finite causal support of these chosen finite prefixes is used.

The formula is uniform over all old data in \(K\). The passive reference
is left as an identity factor and is not asserted to have finite
dimension. For a pure old-memory/reference vector its receiver Schmidt
rank is at most 25. No classical description of an arbitrary unknown
reference state is needed to apply the fixed channel.

The active-contact calibration in [CONTACT.md](CONTACT.md) also starts
on four coordinate ports. After \(n\) steps its object satisfies

\[
|R-99|\le n,\qquad |r|\le n,
\]

and the standing-token or pulse coordinate lies in
\([99-n,99+n]\). With one token arrangement and two pulse banks, a
conservative corresponding active-coordinate bound is
\(12(2n+1)^3\,26^2\). These bounds describe finite prefixes; they do not
supply a finite box reproducing all later evolution.

### 1.2 The finite supplementary source

The source in [ACTIVE_EQUAL_SPECTRUM.md](ACTIVE_EQUAL_SPECTRUM.md) is
specified by
\(\chi_s\pm(U^2-U^{-2})\chi_s\), with \(\chi_s=\alpha_{97}\) and
the original source operator \(U=U_0C\). Both inverse and forward steps
have range at most one in each configuration coordinate. Thus its
initial support obeys

\[
|R-97|\le2,\qquad |r|\le2,\qquad |c-97|\le2,
\]

where \(c\) is the token or pulse coordinate. In particular \(c\le99\),
so this preparation acts as a source-only operation tensored with the
identity on the arbitrary old memory/reference.

After \(n\) subsequent forward steps the three bounds become
\(n+2\). A conservative active-coordinate count is
\(12(2n+5)^3\,26^2\). The actual reading uses \(n=3\), and no
intervening instrument or postselection. A complete supplied source
unitary is given in the supplement on the span of \(\chi_s\) and
\((U^2-U^{-2})\chi_s\), with the identity on its complement.
It is independent of the unknown old receiver/reference state.

The negative powers specify finite amplitudes. Their use in the
mathematical source definition is not a claim that the native apparatus
can execute inverse steps to prepare the source, or that doing so has
no cost.

## 2. Exact arithmetic and its scope

Let \(\mathcal O=\mathbb Z[\zeta_{20}]\) with the same complex embedding
\(\iota\) as the whole-step arithmetic construction. In the fixed
occupation basis,

\[
\mathcal A=25U_{\rm rec},\qquad
\mathcal A^\dagger\mathcal A=625I.
\]

This numerator and its minimal denominator are inherited from
[#1741](https://github.com/mathorn1973/twist-j/issues/1741#issuecomment-6385322548)
and [#1772](https://github.com/mathorn1973/twist-j/pull/1772).
They are not new results of the finite phase experiment.

For either primary phase \(0,\pi\), and a fixed basis state of the old
receiver, the four source coefficients are \(\pm1/2\). The raw source
vector \(a_0\) therefore has four coefficients \(\pm1\) and
\(\|\iota(a_0)\|=2\). The exact complete sequence is

\[
a_n=\mathcal A^n a_0,\qquad
\psi_n=\frac{\iota(a_n)}{2\,25^n}.
\]

Every \(\mathcal O\)-coefficient has eight integer coordinates in the
fixed cyclotomic basis. This is one common normalization of the entire
state. No accepted branch is renormalized during the evolution.

The supplied complete source preparation can be written as one
four-by-four block with entries \(\pm1/2\) for the two exact phase
settings, and the identity on its orthogonal complement. Its two
Hadamard factors contain \(1/\sqrt2\), but the entries of this joint
four-port block are rational. The preparation is explicitly separate
from the unchanged subsequent \(U_{\rm rec}\).

For the active-contact phase settings
\(\eta\in\{1,-1,i,-i\}\), the raw source coefficients are

\[
(3i,-3i,4\eta,-4\eta)
\]

with common normalization \(\sqrt{50}\). They belong to \(\mathcal O\).
The resulting exact write weights are derived directly in CONTACT.

For the supplementary source, put \(\mathcal A_s=25U\) on the source
space and let \(v=\sqrt2\chi_s\), whose two coordinate coefficients
are \(i,-i\). Its raw source tables are exactly

\[
a_\pm=
\bigl[625I\pm(\mathcal A_s^2-(\mathcal A_s^\dagger)^2)\bigr]v.
\]

They have finite support and coefficients in \(\mathcal O\). Their common
norm is \(625\sqrt{2Z}\), since their decoded vectors are
\(625\sqrt2(\chi_s\pm d_s)\). This includes the full preparation
table with a single shared normalization; it requires neither an
integer encoding of the unknown receiver nor an executed inverse
native tick.

### 2.1 Arbitrary old data are a quantum input, not an integer promise

The complete channel identities hold with an arbitrary old receiver and
reference by complex linearity, tensoring with the reference identity,
and extension to density operators. An arbitrary complex input need not
have coefficients in \(\iota(\mathcal O)\) up to a common scale.

Consequently, the finite integer specification applies to the fixed
source and the operator columns, or to an entire input additionally
promised to have such coefficients. It does not encode every unknown
complex receiver/reference amplitude as a finite integer tuple. The
linear channel theorem is stronger in its input generality than the
classical exact-register representation.

The numerator may grow under repeated multiplication. Finite time gives
finite integer data for algebraic inputs; it does not make arbitrary
precision multiplication a constant-cost material operation. The
scale, divisibility, inverse and all-time precision distinctions of
[#1772](https://github.com/mathorn1973/twist-j/blob/3abf054e435e31c51e6e50528b09fe3cf7cffe13/notes/C-FULL-RECORD-SCALE-LIFT-N/PROOF.md)
remain in force.

## 3. Uniform readout tolerance

Use trace distance

\[
D(\rho,\sigma)=\tfrac12\|\rho-\sigma\|_1.
\]

Let \(\rho_\pm\) be the ideal complete input states, including receiver
and reference, and \(\widetilde\rho_\pm\) their actual preparations with

\[
D(\widetilde\rho_\pm,\rho_\pm)\le\delta_\pm.
\]

For the same ideal evolution and receiver effect, trace-distance
contractivity and \(0\le P_0\le I\) give

\[
|\widetilde p_\pm-p_\pm|\le\delta_\pm.
\]

Since the ideal difference is \(p_- -p_+=16/25\),

\[
\boxed{
\widetilde p_- -\widetilde p_+
\ge \frac{16}{25}-\delta_--\delta_+ .
}
\]

This is uniform over every admitted old memory/reference state. It is a
state-distance guarantee, not a demonstrated manufacturing tolerance.

### 3.1 Imperfect steps and an imperfect effect

For a prefix of \(N\) steps, let \(\mathcal U\) be the ideal full unitary
channel, and let the actual step channels satisfy

\[
\tfrac12\|\widetilde{\mathcal U}_j-\mathcal U\|_\diamond
\le\varepsilon_j.
\]

The diamond bound is understood on the declared full input domain with
all passive references. A telescoping expansion and channel
contractivity imply that each final output is within

\[
\delta_\pm+\sum_{j=1}^{N}\varepsilon_j
\]

of its ideal output. If the actual final effect obeys
\(0\le\widetilde P_0\le I\) and
\(\|\widetilde P_0-P_0\|\le\eta\), then

\[
|\widetilde p_\pm-p_\pm|
\le\delta_\pm+\sum_{j=1}^{N}\varepsilon_j+\eta.
\]

For the primary \(N=1\) experiment this gives

\[
\widetilde p_- -\widetilde p_+
\ge\frac{16}{25}
-\delta_--\delta_+-2\varepsilon_1-2\eta.
\]

For the unmeasured \(N=2\) experiment, replace the ideal contrast by
\(224/625\) and use the sum of its two step errors.

For the supplementary active-contact experiment, \(N=3\) and the
positive ideal contrast is the exact value in ACTIVE_EQUAL_SPECTRUM,
strictly greater than \(1/50\). Subtract the same preparation, step and
effect error terms. For example, if each of its two preparation
distances, its three half-diamond step errors and its effect error
is at most \(1/1000\), the resulting contrast is strictly greater than
\(1/100\). These are conditional mathematical budgets, not certified
material tolerances.

As a parameter example only, the inequalities
\(\delta_\pm,\varepsilon_1,\eta\le1/100\) guarantee a primary contrast
at least \(29/50\). These error levels have not been realized or
measured in a material device. The same framework also bounds the
active-contact calibration, using its ideal contrast
\(2304/15625\).

If two unitary steps obey an operator-norm bound
\(\|\widetilde U-U_{\rm rec}\|\le\varepsilon\), their half diamond
distance is at most \(\varepsilon\): expand the difference of the two
conjugations, use the trace-norm ideal property and tensor the same
operator-norm estimate with an arbitrary reference. This provides one
sufficient route to the channel assumption; no such implementation
error is certified here.

## 4. Stability of the equal-energy comparison

The exact primary inputs have the same distribution for every spectral
effect of the full \(U_{\rm rec}\), hence for the nominated

\[
H_*=f(U_{\rm rec}),\qquad
f(e^{-iE})=E\bmod2\pi\in[0,2\pi).
\]

Let \(E_0>0\) be a supplied common unit conversion. The total-variation
distance between the \(E_0H_*\) distributions of the perturbed initial
states is at most \(\delta_++\delta_-\). Indeed each spectral measurement
contracts trace distance and the two ideal distributions coincide.

Because \(0\le H_*\le2\pi I\),

\[
\left|
\operatorname{Tr}(E_0H_*\widetilde\rho_+)
-\operatorname{Tr}(E_0H_*\widetilde\rho_-)
\right|
\le2\pi E_0(\delta_++\delta_-).
\]

This is a comparison with the same prescribed \(H_*\). It neither
selects a physical energy scale nor proves conservation of this energy
under an arbitrary perturbed channel. A supplied preparation apparatus
and its work/phase-reference ledger are not included in the nominated
closed spatial step.

The equal-distribution statement is exact for the primary pair. It
does not apply to the active-contact dark/bright pair: CONTACT gives
different second \(U_{\rm rec}\) moments and thereby disproves equality
of their full spectral laws.

The different finite pair in ACTIVE_EQUAL_SPECTRUM does have exact
equal full spectral laws, by a skew-adjoint polynomial identity.
The same fixed-\(H_*\) preparation bounds above therefore apply to that
pair as well. They do not identify the costs of its larger supplied
source preparation.

## 5. What is still supplied

| Interface | Established in this note | Remaining physical input |
| --- | --- | --- |
| Source | Four-port input, exact phase pair and a complete preparation block | Native production of that coherent state and its phase reference |
| Evolution | The unchanged full \(U_{\rm rec}\), including its complements and inverse | Selection of the spatial geometry and contacts from the original six-pentit rule |
| Receiver | Exact coherent exchange and a sharp 25-state ready capacity | Funding the reserved flag and preparation of the admitted receiver subspace |
| Reading | A specified finite receiver effect and its L1 weights | A material detector and any law of individual outcome occurrence |
| Continuation | Exact one-step return probability and uninterrupted two-step output | Long retention, archive, reset and renewed resources |
| Energy | Exact full spectral equality for the primary pair | Physical selection, units, local energy density and preparation cost |
| Arithmetic | Finite exact specification for the fixed algebraic source and operator | Local finite-digit update, clock rate and precision-resource renewal |

The primary experiment does not exercise capture: its pulse/object sector
is reducing and the contact is identically inactive there. The secondary
calibration exercises the actual contact, but starts from an admitted
coherent contact input rather than an incoming state with certified zero
bound weight. Neither construction is a new finite witness of the
Canon's incoming-unbound-to-bound scattering result.

The finite-prefix compilation and occupied archive of
[#1774](https://github.com/mathorn1973/twist-j/pull/1774), and the
separate thermal/reuse constructions in
[#1768](https://github.com/mathorn1973/twist-j/pull/1768) and
[#1770](https://github.com/mathorn1973/twist-j/pull/1770), retain their
own hypotheses and laws. This note does not silently insert their
controls or resources into \(U_{\rm rec}\).
