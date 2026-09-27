# Proof - C-PHOTON-SLOW-MODE-SECTOR-MAZUR-N

**Status:** candidate-T, PUBLIC NON-CANONICAL.
**Owner:** #1208.
**Author:** A. M. Thorn <thorn@twistj.com>.
**Date:** 2026-09-27.
**Frozen preregistration commit:** \`138f7d346ed11932068b169f5c9e150ad816d619\`.

No Canon status is asserted here.

## 1. Finite transfer and winding blocks

Use the finite transfer construction of PR #1104. On its positive support,
the common unitary \(\mathcal U\) identifies the carrier with

\[
S_L
=
\operatorname{span}
\{\chi_r:
r\in\{0,+1,-1\}^{E_L},
\ \partial r=0\pmod5\}.
\]

The normalized transfer \(T\) is positive and self-adjoint.

For each spatial direction \(i\), define the mod-five cut flux

\[
w_i(r)
=
\sum_{x:x_i=0}r(x,i)\pmod5.
\]

The finite dynamics note proves

\[
S_L
=
\bigoplus_{w\in\mathbb F_5^3}S_w,
\qquad
TS_w\subseteq S_w.                                    \tag{1}
\]

All 125 sectors are nonzero.

For a positive spatial link \(\ell\), the electric insertion is

\[
\kappa E_\ell
=
\mathcal U^*Q_\ell\mathcal U,
\qquad
Q_\ell\chi_r=-r_\ell\chi_r.                            \tag{2}
\]

Every \(Q_\ell\) is diagonal in the same character basis as the winding
projectors. Hence it commutes with every winding projector. The
plane-normalized sum

\[
\overline E_i
=
L^{-3/2}\sum_xE_{(x,i)}
\]

also preserves every sector:

\[
\boxed{
\overline E_iS_w\subseteq S_w.
}                                                       \tag{3}
\]

This is G1.

## 2. The sector thermal means

For temporal period \(L\), define

\[
Z=\operatorname{tr}T^L,
\qquad
Z_w=\operatorname{tr}_{S_w}T^L,
\qquad
p_w=Z_w/Z.
\]

Because \(T>0\) on the finite positive support and \(S_w\ne0\),

\[
Z_w>0,\qquad p_w>0,\qquad \sum_wp_w=1.
\]

Put

\[
m_w
=
Z_w^{-1}
\operatorname{tr}_{S_w}(\overline E_iT^L).             \tag{4}
\]

On the character side define the integer total direction-\(i\) flux

\[
R_i(r)
=
\sum_x r(x,i).                                         \tag{5}
\]

Summing (2) over all \(L^3\) spatial links of direction \(i\) gives

\[
\boxed{
\kappa\overline E_i
=
-L^{-3/2}\mathcal U^*R_i\mathcal U.
}                                                       \tag{6}
\]

Consequently

\[
\boxed{
m_w
=
-\frac1{\kappa L^{3/2}}\mathbb E_wR_i,
}                                                       \tag{7}
\]

where \(\mathbb E_w\) is the normalized trace state with density
\(T^L/Z_w\) in sector \(w\).

## 3. Exact sector-Mazur inequality

Fix \(1\le t<L\). Since both \(T\) and \(\overline E_i\) preserve the sectors,

\[
C_{E,L}(t)
=
\frac1Z
\sum_w
\operatorname{tr}_{S_w}
(\overline E_iT^t\overline E_iT^{L-t}).                 \tag{8}
\]

Diagonalize \(T\) separately in each \(S_w\):

\[
T|_{S_w}|a,w\rangle
=
\lambda_{a,w}|a,w\rangle,
\qquad
\lambda_{a,w}>0.
\]

Since \(\overline E_i\) is Hermitian,

\[
\begin{aligned}
ZC_{E,L}(t)
&=
\sum_w\sum_{a,b}
|\langle a,w|\overline E_i|b,w\rangle|^2
\lambda_{b,w}^t\lambda_{a,w}^{L-t}\\
&\ge
\sum_w\sum_a
|\langle a,w|\overline E_i|a,w\rangle|^2
\lambda_{a,w}^L.
\end{aligned}                                          \tag{9}
\]

All discarded terms are nonnegative. The right side is independent of
\(t\).

For one sector, weighted Cauchy gives

\[
\begin{aligned}
\sum_a
|E_{aa}^{(w)}|^2\lambda_{a,w}^L
&\ge
\frac{
\left|
\sum_aE_{aa}^{(w)}\lambda_{a,w}^L
\right|^2
}{
\sum_a\lambda_{a,w}^L
}\\
&=
Z_wm_w^2.
\end{aligned}                                          \tag{10}
\]

Divide (9) by \(Z\). Therefore, for every \(1\le t<L\),

\[
\boxed{
C_{E,L}(t)
\ge
\sum_{w\in\mathbb F_5^3}p_wm_w^2.
}                                                       \tag{11}
\]

This is an exact finite-dimensional Mazur-type bound. It needs no gap,
thermodynamic limit, clustering or assumption on the distribution of
transfer rates.

## 4. Midpoint mass

The sign bookkeeping of #1133 gives the positive finite sequence

\[
b_L(t)
=
\kappa^2\left[c_{B,L}(t)+C_{E,L}(t)\right],
\]

where both terms on the right are nonnegative. Hence

\[
b_L(t)\ge\kappa^2C_{E,L}(t).                            \tag{12}
\]

At the midpoint,

\[
P_L
=
Lb_L(L/2)
\ge
\kappa^2L\sum_wp_wm_w^2.
\]

Using (7),

\[
\kappa^2L\,m_w^2
=
\frac{(\mathbb E_wR_i)^2}{L^2}.
\]

Therefore

\[
\boxed{
P_L
\ge
\frac1{L^2}
\sum_{w\in\mathbb F_5^3}
p_w\left(\mathbb E_wR_i\right)^2.
}                                                       \tag{13}
\]

This is the primary theorem.

It moves the slow-mode question from the full transfer spectrum to 125 exact
sector weights and sector-polarization means.

## 5. Immediate sufficient criterion

Let \(W_L\subseteq\mathbb F_5^3\). If

\[
\sum_{w\in W_L}p_w\ge p_0>0
\]

and

\[
|\mathbb E_wR_i|\ge cL
\qquad
(w\in W_L),
\]

then (13) gives

\[
P_L
\ge
\frac1{L^2}
\sum_{w\in W_L}p_w c^2L^2
\ge
\boxed{p_0c^2}.                                        \tag{14}
\]

The problem of proving a nondegenerating midpoint has therefore been reduced
to a sector free-energy/polarization estimate.

Neither premise of (14) is asserted here for the fixed model.

## 6. Exact topological congruence

For an integer slice coordinate \(s\), define

\[
F_i(s)
=
\sum_{x:x_i=s}r(x,i).
\]

Summing the mod-five conservation law \(\partial r=0\pmod5\) over the slab
between two adjacent cuts gives

\[
F_i(s+1)\equiv F_i(s)\pmod5.
\]

By definition the common residue is \(w_i\). Summing all \(L\) cut fluxes,

\[
R_i(r)
=
\sum_{s=0}^{L-1}F_i(s),
\]

so

\[
\boxed{
R_i(r)\equiv Lw_i\pmod5.
}                                                       \tag{15}
\]

This is the entire purely topological input to the sector polarization.

## 7. Why topology alone cannot close the bound

Equation (15) does not fix the sign or mean of \(R_i\).

There is an explicit control inside the actual ternary carrier. Assume
\(L\ge2\), so at least five parallel coordinate loops are available whenever
needed below. In sector \(w_i=1\):

- one positive coordinate winding loop has
  \[
  R_i=L,\qquad w_i=1;
  \]
- four disjoint negative coordinate winding loops have
  \[
  R_i=-4L,\qquad w_i=-4\equiv1\pmod5.
  \]

Both fields are ternary and integer-divergence-free, hence belong to the same
allowed mod-five sector.

More generally, sector \(w_i=a\in\{1,2,3,4\}\) contains representatives on
both sides of zero once enough parallel loops are available: use \(a\)
positive loops or \(5-a\) negative loops.

Thus even the actual sector support straddles zero. The positive lower bound
needed in (14) must arise from the **transfer weights**, not from the sector
label.

This does not show that the thermal sector mean is zero. The transfer strongly
need not weight the two representatives equally.

## 8. Charge conjugation

Charge conjugation

\[
C\chi_r=\chi_{-r}
\]

commutes with \(T\), maps \(S_w\) unitarily to \(S_{-w}\), and sends

\[
R_i\mapsto-R_i.
\]

Therefore

\[
\boxed{
Z_w=Z_{-w},\quad
p_w=p_{-w},\quad
\mathbb E_{-w}R_i=-\mathbb E_wR_i.
}                    \tag{16}
\]

The squares in (13) are therefore naturally paired. This symmetry does not
force the nonzero-sector means to vanish because \(w\) and \(-w\) are distinct
for every nonzero \(w\in\mathbb F_5^3\).

## 9. Relation to a full path expansion

The sector thermal weight may also be written in the character basis.
For a periodic sequence \(r_0,\ldots,r_{L-1}\in S_w\),

\[
\operatorname{tr}_{S_w}T^L
=
\Lambda^{-L}
\sum_{\{r_t\}\subset S_w}
\prod_{t=0}^{L-1}
\ell(r_t)\,
b(r_{t+1}-r_t),
\qquad r_L=r_0.                                        \tag{17}
\]

Here

\[
\ell(r)=10^{|E_L|}2^{-|\operatorname{supp}r|}
\]

on the ternary carrier, and \(b(\delta)\ge0\) is the exact spatial surface
coefficient from PR #1104.

Equation (17) makes the remaining problem concrete: prove that this positive
path measure in nonzero winding sectors polarizes \(R_i\) strongly enough,
and that enough such sectors retain nonvanishing weight.

No independent-loop or dilute-surface assumption appears in this formulation.

## 10. P1 boundary

The midpoint quantity is not by itself the ordered local coefficient.

#1134 supplies the exact conditional comparison

\[
|P_L-\Delta|
\le
|a_L-a|+\rho_L/24,                                    \tag{18}
\]

when the target limit moment and full-space weighted error \(\rho_L\) are
defined at the declared scope.

Thus a future proof based on (13) needs two distinct ingredients:

1. a nonzero sector response giving \(P_L\ge c_*>0\);
2. the full-space weighted bridge making the error in (18) vanish.

The present note supplies only the exact reduction for the first ingredient.

## 11. Status

- sector preservation, sector-Mazur inequality, midpoint reduction,
  winding congruence and charge-conjugation identities: **candidate-T**;
- exact rational and winding-loop audit: **candidate-C**;
- nonzero fixed-model sector polarization: **OPEN**;
- nonvanishing sector weight in the required limit: **OPEN**;
- full-space weighted bridge: **OPEN**;
- P1, massless phase and physical photon: **OPEN**.
