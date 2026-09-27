# PREREG - C-PHOTON-SLOW-MODE-SECTOR-MAZUR-N

**Status:** PUBLIC, NON-CANONICAL incubation. No Canon authority.
**Owner:** A. M. Thorn / photon-slow-mode-sector-mazur-20260927
**Date:** 2026-09-27
**Issue:** #1208
**Action layer:** L6 finite positive-transfer mathematics.
**Authority:** Public Canon v92. Normative files remain unchanged.

## Frozen inputs at their own scope

### Finite transfer

From PR #1104, head
\`87ccd4b80575143ba1d3418171a7171c6e7d82e4\`, use the finite spatial
transfer on the positive support and its character carrier

\[
S_L
=
\{r\in\{0,+1,-1\}^{E_L}:\partial r=0\pmod5\}.
\]

The normalized transfer \(T\) is positive, self-adjoint and has spectrum in
\((0,1]\) on its positive support.

For every spatial link \(\ell\), the common unitary \(\mathcal U\) gives

\[
\kappa E_\ell
=
\mathcal U^*Q_\ell\mathcal U,
\qquad
Q_\ell\chi_r=-r_\ell\chi_r.
\]

### Winding sectors

The same finite transfer decomposes exactly as

\[
S_L
=
\bigoplus_{w\in\mathbb F_5^3} S_w,
\]

where

\[
w_i(r)
=
\sum_{x:x_i=0}r(x,i)\pmod5.
\]

Every \(S_w\) is nonzero and invariant under \(T\).

### Positive midpoint sequence

From #1133 use the plane-normalized Hermitian electric insertion

\[
\overline E_i
=
L^{-3/2}\sum_x E_{(x,i)}
\]

and the positive sequence

\[
b_L(t)
=
\kappa^2[c_{B,L}(t)+C_{E,L}(t)],
\qquad
C_{E,L}(t)
=
Z^{-1}\operatorname{tr}
(\overline E_i T^t\overline E_i T^{L-t})
\ge0,
\]

where \(c_{B,L}(t)\ge0\) and the sign convention converts the raw Euclidean
electric covariance into the positive Hermitian quantity \(C_{E,L}(t)\).

The exact midpoint quantity is

\[
P_L=L\,b_L(L/2).
\]

### Limit boundary

#1134 proves that a positive lower bound on \(P_L\) does not by itself imply
the ordered local P1 coefficient without a separate full-space weighted-error
or weighted-tail bridge. This boundary is frozen into the present result.

## Frozen notation

For one spatial direction \(i\), define on the character carrier

\[
R_i(r)=\sum_x r(x,i).
\]

Then

\[
\boxed{
\kappa\overline E_i
=
-L^{-3/2}R_i
}
\]

under the common unitary.

For inverse temporal size \(L\), put

\[
Z=\operatorname{tr}T^L,
\qquad
Z_w=\operatorname{tr}_{S_w}T^L,
\qquad
p_w=Z_w/Z.
\]

Since every \(S_w\) is nonzero and \(T>0\) on the positive support,
\(Z_w>0\) and \(p_w>0\).

Define

\[
m_w
=
Z_w^{-1}
\operatorname{tr}_{S_w}(\overline E_iT^L).
\]

Equivalently,

\[
m_w
=
-\frac1{\kappa L^{3/2}}
\mathbb E_w R_i,
\]

where \(\mathbb E_w\) is the exact sector thermal expectation.

## G1. Sector preservation

Prove that \(\overline E_i\) preserves each \(S_w\).

On the character side, every \(Q_\ell\) is diagonal in \(r\), hence commutes
with every winding projector. The common unitary transports this statement to
the physical positive support.

## G2. Exact sector-Mazur inequality

For every integer \(1\le t<L\), prove

\[
\boxed{
C_{E,L}(t)
\ge
\sum_w p_wm_w^2.
}
\]

Required proof:

1. diagonalize \(T\) separately in every invariant sector;
2. write the exact nonnegative spectral sum
   \[
   Z\,C_{E,L}(t)
   =
   \sum_w\sum_{a,b\in w}
   |E^{(w)}_{ab}|^2
   \lambda_b^t\lambda_a^{L-t};
   \]
3. discard all \(a\ne b\) terms;
4. obtain
   \[
   Z\,C_{E,L}(t)
   \ge
   \sum_w\sum_a
   |E^{(w)}_{aa}|^2\lambda_a^L;
   \]
5. apply weighted Cauchy within each sector:
   \[
   \sum_a |E_{aa}|^2\lambda_a^L
   \ge
   \frac{|\sum_aE_{aa}\lambda_a^L|^2}
        {\sum_a\lambda_a^L}
   =
   Z_wm_w^2.
   \]

No time-separation or spectral-gap estimate is used.

## G3. Exact midpoint lower bound

Since \(c_{B,L}(t)\ge0\),

\[
b_L(t)
\ge
\kappa^2C_{E,L}(t).
\]

At \(t=L/2\),

\[
P_L
=
Lb_L(L/2)
\ge
\kappa^2L\sum_wp_wm_w^2.
\]

Substitute the exact \(R_i\) normalization to obtain

\[
\boxed{
P_L
\ge
\frac1{L^2}
\sum_{w\in\mathbb F_5^3}
p_w\left(\mathbb E_wR_i\right)^2.
}
\]

This is the primary theorem.

## G4. Sufficient sector response criterion

For any sector set \(W_L\), if

\[
\sum_{w\in W_L}p_w\ge p_0>0
\]

and

\[
|\mathbb E_wR_i|\ge cL
\qquad
(w\in W_L),
\]

then

\[
\boxed{P_L\ge p_0c^2.}
\]

This is a sufficient theorem, not a proved property of the fixed model.

## G5. Exact winding congruence

For \(r\in S_w\), let

\[
F_i(s)
=
\sum_{x:x_i=s}r(x,i).
\]

Modulo five, \(\partial r=0\) implies

\[
F_i(s+1)=F_i(s)=w_i.
\]

Therefore

\[
R_i(r)
=
\sum_{s=0}^{L-1}F_i(s)
\equiv
Lw_i
\pmod5.
\]

This is the complete topological information used here.

## G6. Topology-only firewall

The congruence in G5 does not imply a lower bound on

\[
|\mathbb E_wR_i|.
\]

For a fixed nonzero residue class modulo five, integers in that class occur on
both sides of zero once the allowed interval is large enough. A convex
combination of such values can have mean zero.

No claim is made that the actual sector law realizes such a cancellation.
The point is logical: sector conservation alone is insufficient. Any positive
bound in G4 must use model-specific sector weights or a further monotonicity,
injection, free-energy or switching theorem.

## G7. Charge-conjugation control

Charge conjugation maps \(S_w\) to \(S_{-w}\), preserves the transfer
spectrum, sends \(R_i\) to \(-R_i\), and therefore gives

\[
p_w=p_{-w},
\qquad
\mathbb E_{-w}R_i=-\mathbb E_wR_i.
\]

This is compatible with the square in G3 but does not supply its positivity
away from zero.

## G8. P1 boundary

Even a uniform positive lower bound on \(P_L\) is not by itself a P1 closure.

To identify it with the ordered local coefficient one still needs the
full-space bridge of #1134, for example

\[
|P_L-\Delta|
\le
|a_L-a|+\rho_L/24
\]

with the relevant weighted error \(\rho_L\to0\).

The present theorem isolates the slow-mode lower-bound problem only.

## Exact finite audit

Only after this preregistration and the audit source are committed and publicly
read back, a standard-library exact audit may test:

1. G2 on a fixed list of rational block-diagonal positive transfer matrices
   and sector-preserving Hermitian insertions;
2. exact equality of the final \(L\)- and \(\kappa\)-powers under the symbolic
   substitution \(m_w=-\mathbb E_wR_i/(\kappa L^{3/2})\);
3. G5 on explicit ternary divergence-free winding-loop fixtures for
   \(L\in\{3,4,6\}\);
4. the charge-conjugation pairing of those fixtures.

The audit is candidate-C corroboration only. The theorem is the written
finite-dimensional proof.

## Falsifiers

Any exact failure of G1-G5 or G7 fires the corresponding candidate.
Failure to establish the model-specific criterion G4 leaves the slow-mode
program open and does not falsify G1-G3.

## Repository boundary

Only \`notes/C-PHOTON-SLOW-MODE-SECTOR-MAZUR-N/\` may be added.

No Canon, Registry, Frontier, formal probe, gate, tool, workflow, release or
existing note may be changed.
