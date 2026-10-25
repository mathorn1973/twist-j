# A finite phase-to-record experiment at equal full spectral energy

**PUBLIC / NON-CANONICAL / L1. Conditional analytical candidate-T.**
Author: A. M. Thorn. Date: 2026-10-25. Apache-2.0.
Reservation: [#1775](https://github.com/mathorn1973/twist-j/issues/1775).
Independent acceptance remains pending.

The unchanged complete spatial step \(U_{\rm rec}\) admits finite
phase comparisons with identical complete spectral-energy distributions
and different receiver outputs. The frozen one-step calibration has
write weights \(2/25\) and \(18/25\). A separately declared analytical
supplement activates the actual contact and proves a receiver contrast
strictly greater than \(1/50\) after three uninterrupted steps, again
with identical full spectral laws and initial configuration probabilities.

In the simpler frozen calibration, two finite
inputs with the same positions, basis populations, occupied receiver and
reference, and the same **entire full-step spectral-energy distribution**,
give the one-step receiver write weights:

\[
\boxed{p_+=\frac2{25},\qquad p_-=\frac{18}{25},\qquad
       p_--p_+=\frac{16}{25}.}
\]

Only the relative phase between the two pulse banks changes. The output
is read at the original receiver after one original macrostep. Every
complementary branch and the displaced old-memory/reference information
are retained in the derivation.

This is a conditional finite experiment inside the prescribed spatial
model. The source preparation and final reading are explicitly supplied.
It does not derive the geometry, the coherent preparation or an individual
actual outcome from the original six-pentit TWIST transition.

## 1. The frozen primary experiment

The receiver remains at \(z=100\). A pulse with label zero starts at
\(x=99\), with bank vector

\[
v_\pm=(1,\pm1)^{\mathsf T}/\sqrt2.
\]

The common object state is

\[
\chi_-=
\bigl(|R=0,r=3,e_1\rangle-|R=0,r=-3,e_1\rangle\bigr)/\sqrt2.
\]

The original 26-dimensional receiver contains arbitrary old data in

\[
K=\operatorname{span}\{d_1,\ldots,d_{25}\},
\]

including correlations with an arbitrary passive reference. One label
\(d_0\) is reserved to indicate a new write. The source is initially a
product with the same receiver/reference input in both preparations.

A supplied complete four-port unitary prepares each source from a
marked basis input. The subsequent evolution contains only the original
\(U_{\rm rec}\). The final effect is the receiver-only
\(P_W=|d_0\rangle\langle d_0|\), with its complementary effect retained.

## 2. The resulting physics within this model

### Phase changes transport and recording without changing spectral energy

The object-odd pulse sector is reducing. Its actual contact is inactive
at all times; this is proved from the operator, not inferred from a
short causal separation. A reflected pulse together with the real
bank rotation \(J_c\), conjugated by the original receiver calibration,
defines a symmetry of the full operator and exchanges the two inputs.

Thus, for every Borel spectral set \(B\),

\[
\langle\Psi_+,E_{U_{\rm rec}}(B)\Psi_+\rangle
=
\langle\Psi_-,E_{U_{\rm rec}}(B)\Psi_-\rangle.
\]

In particular the complete distributions of the nominated
\(H_*=f(U_{\rm rec})\), where \(f(e^{-iE})=E\bmod2\pi\in[0,2\pi)\),
coincide. This includes all moments and every spectral interval, and
each distribution is conserved by the same evolution.

The exact pulse update nevertheless has different right-going
interference amplitudes. More generally,

\[
p_1(\theta)=\frac{10-8\cos\theta}{25}.
\]

The contrast \(16/25\) is sharp among phase-only changes at fixed bank
populations, for a pulse at this one site and this one-step reading.
This does not optimize over arbitrary apparatuses or waiting times.

The Canon's occupation-charge current across the actual cut \(99\)
also differs:

\[
\langle J_{99}\rangle_+=8/25,\qquad
\langle J_{99}\rangle_-=72/25.
\]

Only carrier charge crosses this cut on the first step. This is a
native occupation-current result; it is not a derived local current of
the nominated spectral energy.

### Occupied memory works coherently, with a sharp indication cost

In the written branch,

\[
|p_0\rangle\sum_{j=1}^{25}|d_j\rangle|\phi_j\rangle
\longmapsto
\sum_{j=1}^{25}|p_j\rangle|d_0\rangle|\phi_j\rangle.
\]

The pulse takes the old contents and all their reference correlations.
The nonwritten branch leaves them in the receiver. This occupied
exchange is inherited; the new result is its exact phase-dependent
finite-time weight under this unchanged apparatus law.

A perfect receiver-only fresh-write flag cannot work for every state
of the full 26-dimensional old memory: an old \(d_0\) is
indistinguishable from a newly written \(d_0\). Excluding one direction
is necessary and sufficient, so the 25-dimensional ready space is
sharp. Coherent exchange itself remains valid for all 26 old labels.

### A current record is reversible and depends on the reading protocol

| Final reading protocol | Phase \(+\) | Phase \(-\) |
| --- | ---: | ---: |
| Read after one step | \(2/25\) | \(18/25\) |
| Two uninterrupted steps, then one reading | \(168/625\) | \(392/625\) |
| Read after each step, ignore the first result | \(140/625\) | \(380/625\) |

After a nonzero first written outcome, the next step retains the
new flag with conditional weight \(21/25\), and returns the old
memory/reference state with weight \(4/25\). This is an exact
sequential-instrument statement, not a classical history assigned to
an unmeasured coherent state.

The uninterrupted and measured protocols have different second-step
statistics because the first reading removes a specific interference
term. The files give both complete states/instruments.

## 3. Active-contact calibrations

### 3.1 A simple first-step contrast with different spectral laws

At the actual contact site \(99\), let \(\alpha\) be the standing-token
port and \(\gamma\) the pulse port of the Canon. Use the two admitted
coherent inputs

\[
\psi_\pm=(3\alpha\pm4\gamma)/5.
\]

The contact, free streaming and the same occupied receiver give

\[
p_W(\psi_+)=2304/15625,\qquad p_W(\psi_-)=0.
\]

This shows phase-sensitive conversion at the actual contact followed by
transport and a local occupied-memory record, with no added operation
between spatial steps. Its dark setting concerns this first conversion
and reading, not an invariant dark state.

These inputs **do not have the same complete spectral distribution**.
The exact witnesses are

\[
\langle\psi_-,U_{\rm rec}^2\psi_-\rangle=12/25,
\]

\[
\langle\psi_+,U_{\rm rec}^2\psi_+\rangle
=-84/625-(2688/15625)e^{-2\pi i/5}.
\]

The primary equal-energy proof is therefore not transferred to this
different family. Equal occupation charge and equal norm alone would
not justify that transfer.

The active calibration begins with an admitted coherent token/pulse
source already at contact. It does not prove incoming-unbound-to-bound
capture or supply the Canon's asymptotic capture preparation in a
finite device.

### 3.2 A finite active-contact pair with equal full spectral laws

A separate
[result-exposed analytical supplement](https://github.com/mathorn1973/twist-j/issues/1775#issuecomment-6399077081)
uses the same law and receiver. Let \(\chi_s=\alpha_{97}\) be the
original standing-token contact vector. On the source space define
\(d_s=(U^2-U^{-2})\chi_s\), with \(U=U_0C\), and prepare

\[
\psi_\pm=\frac{\chi_s\pm d_s}{\sqrt Z},\qquad
Z=\frac{39521+154\sqrt5}{15625}.
\]

Both source supports lie to the left of the receiver, with carrier
coordinates in \(95,\ldots,99\). Hence they are products with the same
arbitrary old memory/reference, and their source definition agrees with
the corresponding calibrated full-operator polynomial on these inputs.
It specifies a supplied finite preparation; it does not command a
physical execution of inverse time steps.

The skew-adjoint polynomial \(U_{\rm rec}^2-U_{\rm rec}^{-2}\) gives
identical full spectral densities to the two inputs. An exact return
moment and a combined object/arrangement symmetry additionally show that
the finite source tables have identical configuration probabilities:
they agree on the two original \(\chi_s\) coordinates and have opposite
signs elsewhere. The actual contact is active on both inputs.

After three uninterrupted forward macrosteps, the original receiver-only
write effect gives

\[
\boxed{
p_W(\psi_+)-p_W(\psi_-)
=\frac{65536(48533-10985\sqrt5)}
{5^9(39521+154\sqrt5)}
>\frac1{50}.
}
\]

The proof evaluates the complete relevant interference term, including
the first emission, late token emission and all four possible
pulse-contact corrections. The exact separate probabilities are specified
by the complete finite output vectors; the displayed closed value is
their difference. No branch is selected during the evolution.

This result combines active contact, equal full spectral energy, a
relative-sign change and a finite original-memory output in one
experiment. Its more structured coherent source is still supplied. It
is not a token-only preparation and does not test a bound-pair projector.
The simpler \(3{:}4\) contact pair's unequal-spectrum result remains
unchanged.

## 4. Scope and verification

| Question | Result |
| --- | --- |
| Finite phase dependence under one unchanged spatial law | Exact one-step receiver effect and full two-step continuation |
| Same full spectral energy in the primary phase comparison | Exact full-operator symmetry proof |
| Active contact in that primary comparison | Inactive reducing sector; a separate active calibration is supplied |
| Active contact with equal full spectrum in the finite supplementary pair | Exact three-step contrast greater than \(1/50\), with a supplied structured source |
| Active contact with equal full spectrum for the simple \(3{:}4\) pair | Refuted by unequal second moments |
| Arbitrary occupied old data and passive reference | Exact on the 25-dimensional flag-ready subspace; full-label SWAP remains valid |
| Arbitrary full26 old data with a perfect local fresh-write flag | Impossible without additional readiness or indication resources |
| Exact finite arithmetic | Four raw integer source coefficients and inherited \(\mathcal A=25U_{\rm rec}\) |
| Perturbations | Uniform state/channel/effect bounds, including a primary contrast guarantee |
| Original six-pentit generation, physical energy selection and outcome occurrence | Not established |
| Scientific acceptance | Same-session analytical checks only; separate acceptance pending |

No scientific executable, simulation or numerical parameter search was
run. Repository integrity checks do not serve as scientific acceptance.
The public issue was reserved before new note commits; exposed hand
predictions are explicitly recorded as such in the contract.

## 5. Files

| File | Contents |
| --- | --- |
| [CONTRACT.md](CONTRACT.md) | Frozen public scope, input family, analytical tests and execution boundary |
| [EXPERIMENT.md](EXPERIMENT.md) | Complete loader, joint outputs, readout effects, continuation and flag capacity |
| [SPECTRAL.md](SPECTRAL.md) | Reducing sector, full symmetry, entire energy-law equality and occupation current |
| [CONTACT.md](CONTACT.md) | Active-contact phase calibration and the failed equal-spectrum extension |
| [ACTIVE_EQUAL_SPECTRUM.md](ACTIVE_EQUAL_SPECTRUM.md) | Finite active-contact phase pair with equal full spectral laws and an exact three-step contrast |
| [RESOURCES.md](RESOURCES.md) | Finite support, exact arithmetic quantifiers, tolerance bounds and native implementation debts |
| [SOURCES.md](SOURCES.md) | Authority, exact source pins and prior-result boundaries |
| [REVIEW.md](REVIEW.md) | Separately reasoned same-session analytical review |
| [VALIDATION.md](VALIDATION.md) | Integrity checks, authorship and delivery status |
| SHA256SUMS | Exact authored-file inventory and hashes |
