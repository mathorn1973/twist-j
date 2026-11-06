# An absolute upper bound for the frozen joint event

**NON-CANONICAL / L1 / post-run analytical addendum.**
Author: A. M. Thorn. SPDX-License-Identifier: Apache-2.0.

This deduction was made after the first relative-profile execution. It is
not represented as part of that prospective numerical audit. It uses the
same frozen source, complete scattering functions and output event. The
pinned proofs, verifier, preregistration and captured output are unchanged;
no additional scientific executable was run for this addendum.

## 1. The full denominator gives a universal overlap bound

Use the almost-everywhere Caratheodory boundary values from the inherited
`PROOF_CAPTURE_SCATTERING.md`, section 3. Write

\[
\rho_{1,\mathrm{tot}}(E)=\frac{\operatorname{Re}F_1(E)}{2\pi},
\qquad
\rho_{2,\mathrm{tot}}(K,E)=\frac{\operatorname{Re}F_2(K,E)}{2\pi}.
\tag{AB-1}
\]

These are the full port densities, including every open contribution.
The selected outgoing density satisfies
`0<rho_(2,b,+)<=rho_(2,tot)` almost everywhere in the frozen output
rectangle. The selected channel projector commutes with `U0` and lies
between zero and the identity. Its positive port spectral measure is
therefore dominated by the full measure, and the same inequality holds
almost everywhere for their absolutely continuous densities. Relative
binding does not make the full bound-pair-plus-moving-pulse channel a
point measure in total energy. The incoming density `rho_p` is a selected contribution to
`rho_(1,tot)`. In particular the latter includes the full positive
contribution of `|P|<=1` established in (CP-9).

For any two complex numbers the exact identity

\[
|4+F_1F_2|^2-16\operatorname{Re}F_1\operatorname{Re}F_2
=|4-F_1\overline{F_2}|^2\ge0
\tag{AB-2}
\]

holds. Therefore the complete transition kernel in (CP-13) obeys

\[
\frac{64\pi^2\rho_p\rho_{2,b,+}}{|4+F_1F_2|^2}
\le
\frac{\rho_p}{\rho_{1,\mathrm{tot}}}
\frac{\rho_{2,b,+}}{\rho_{2,\mathrm{tot}}}
\le\frac{\rho_p}{\rho_{1,\mathrm{tot}}}.
\tag{AB-3}
\]

No complete resolvent has been replaced by a selected channel. Positivity
on this rectangle makes the displayed ratios well-defined almost
everywhere; null exceptional boundary sets do not change the integral.

## 2. The incoming and outgoing windows

For every `omega in I_omega`, (CP-15) and the ratio bound in section 8
of the profile proof give

\[
\rho_0(E)\le\frac{\delta}{\pi}\rho(0,\omega),\qquad
\rho(P,\omega)>\frac58\rho(0,\omega)\quad (|P|\le1).
\tag{AB-4}
\]

Consequently

\[
\rho_{1,\mathrm{tot}}(E)
\ge\int_{-1}^{1}\rho(P,\omega)\frac{dP}{2\pi}
>\frac{5}{8\pi}\rho(0,\omega),
\qquad
\frac{\rho_0(E)}{\rho_{1,\mathrm{tot}}(E)}<\frac{8\delta}{5}.
\tag{AB-5}
\]

The inherited `PROOF_PACKET_CERTIFICATE.md`, section 3, fixes

\[
I_K=[k_0-\delta_K,k_0+\delta_K],\quad
k_0=-\arccos\frac{9-5\sqrt5}{16},\quad \delta_K=1/1000.
\tag{AB-6}
\]

The localized standing token gives uniform total-momentum weight
`dK/(2*pi)`, so the weight of this selected output interval is
`delta_K/pi`. The incident energy distribution has total weight one.
Integrating (AB-3) and (AB-5) therefore proves

\[
\boxed{
\frac{2}{10^{28}}<\mathsf P(0)
<\frac{8\delta\delta_K}{5\pi}
=\frac{8}{5\pi\,10^6}
<\frac{8}{15\,10^6}.
}
\tag{AB-7}
\]

The lower bound is inherited. For the entire frozen family, strict
momentum decline and (CP-28) imply

\[
\frac1{10^{28}}<\mathsf P(p)<\frac{8}{5\pi\,10^6}
\qquad (|p|\le999/1000).
\tag{AB-8}
\]

## 3. Meaning and remaining absolute calculation

These absolute bounds are very wide. They do not estimate the actual
magnitude of the capture rate. The small upper bound is for the particular
joint event with its narrow outgoing total-momentum window and the
specified contact-selected input. It is not an upper bound on arbitrary
capture, on a differently conditioned source, or on a plane-wave cross
section. In particular the window-conditioned source `Psi_win` in the
inherited packet proof has a different total-momentum normalization and
does not inherit (AB-7) as written.

To determine the magnitude, the smallest remaining calculation is one
absolute base point `P_win(0)` on the same `I_K x I_E`. This requires the
complete `F2`, with all relative spectral contributions and pulse branches,
including the pole and threshold contributions in its full momentum
integral. The selected outgoing bound-branch density alone cannot replace
it. Once `P_win(0) in [a,b]` is certified, each existing relative enclosure
`[L(p),U(p)]` immediately gives `[a L(p),b U(p)]`; no repeated momentum
scan or changed source definition is needed.

All inherited source versions and hashes are listed in [SOURCES.md](SOURCES.md).
