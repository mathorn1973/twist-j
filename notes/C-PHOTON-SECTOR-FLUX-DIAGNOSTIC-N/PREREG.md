# PREREG - C-PHOTON-SECTOR-FLUX-DIAGNOSTIC-N

**Status:** PUBLIC, NON-CANONICAL DIAGNOSTIC ONLY. ZERO evidential weight.
**Owner:** A. M. Thorn / photon-sector-flux-diagnostic-20260927
**Date:** 2026-09-27
**Issue:** #1210
**Authority:** Public Canon v92. No normative file changes.

## Purpose

This is a finite route-selection diagnostic for the candidate-T sector-Mazur
quantity from #1208. It is not a scientific finite-size scaling probe.

The exact target sampled by the inherited mobility kernel is

\[
\nu_L(n)\propto2^{-|\operatorname{supp}n|},
\qquad
n\in\{-1,0,1\}^{P_L},
\qquad
\partial n=0\pmod5.
\]

## Frozen sampler dependency

Import without editing

\`probes/P-PHOTON-Z5-DUAL-MOBILITY-QUALIFICATION-1/mobility_kernel.py\`.

That exact wrapper formally passed its own ZERO_ENGINEERING_ONLY L=3,4
mobility qualification. This diagnostic reuses only its stationary transition
law. It does not inherit a scientific phase status.

## Transfer-label reading

Freeze coordinate 0 as Euclidean time. For every saved four-dimensional
surface state and every time slice \(s=x_0\), define the spatial transfer
label

\[
r_s(x,i)
=
n_{0i}(s,x),
\qquad i\in\{1,2,3\},
\]

using the principal value in \(\{-1,0,1\}\).

The diagnostic must verify exactly for every saved state:

1. each \(r_s\) has spatial divergence zero modulo five;
2. for every direction \(i\), the cut flux
   \[
   w_i(s)
   =
   \sum_{x:x_i=0}r_s(x,i)\pmod5
   \]
   is independent of both the cut location and the time slice \(s\).

The common vector is the transfer winding label
\(w=(w_1,w_2,w_3)\in\mathbb F_5^3\).

For one configuration define the time-averaged integer flux

\[
\overline R_i
=
\frac1L
\sum_{s=0}^{L-1}
\sum_x r_s(x,i).
\]

Time averaging is used only as a variance-reduction reading. By cyclic time
translation it has the same ensemble mean as any fixed-slice \(R_i\).

## Frozen chains

Volumes:

\[
L\in\{3,4\}.
\]

For each L run four chains:

| label | start | seed |
|---|---|---|
| L3_cold_r1 | cold | 0xd1210030000000000000000000000101 |
| L3_cold_r2 | cold | 0xd1210030000000000000000000000102 |
| L3_witness_r1 | witness | 0xd1210030000000000000000000000201 |
| L3_minus_r1 | minus_witness | 0xd1210030000000000000000000000301 |
| L4_cold_r1 | cold | 0xd1210040000000000000000000000101 |
| L4_cold_r2 | cold | 0xd1210040000000000000000000000102 |
| L4_witness_r1 | witness | 0xd1210040000000000000000000000201 |
| L4_minus_r1 | minus_witness | 0xd1210040000000000000000000000301 |

Per chain:

- warmup: 4096 exact mobility transitions;
- saved samples: 512;
- transitions between saved samples: 64;
- exact state validation after warmup and after every 32nd saved sample.

No schedule extension or seed replacement after output is opened.

## Frozen saved observables

For every chain record:

- number of distinct winding vectors among saved samples;
- number of sample-to-sample winding changes;
- exact winding-sector counts \(N_w\);
- for each direction \(i\), exact integer numerator
  \[
  S_{w,i}
  =
  \sum_{\text{samples in }w}
  \sum_{s=0}^{L-1}R_i(s).
  \]

The empirical sector mean is

\[
\widehat{\mathbb E}_wR_i
=
\frac{S_{w,i}}{LN_w}.
\]

Pool the four chains at fixed L before evaluating the route statistic.

## Frozen empirical Mazur statistic

With \(N=2048\) pooled configurations,

\[
\widehat M_i(L)
=
\frac1{L^2}
\sum_{w:N_w>0}
\frac{N_w}{N}
\left(
\frac{S_{w,i}}{LN_w}
\right)^2.
\]

All decisions use exact \`Fraction\` arithmetic.

Also report:

\[
p_{\ne0}(L)
=
1-\frac{N_{(0,0,0)}}N.
\]

## Mobility guard

A chain passes iff:

- at least 16 distinct winding vectors occur;
- at least 32 saved-sample winding changes occur.

The guard is a diagnostic integrity check only.

## Frozen terminal

**NONCOLLAPSE-DIAGNOSTIC** if:

- all eight chains pass;
- every \(\widehat M_i(3)>0\);
- for every spatial direction,
  \[
  \widehat M_i(4)\ge\frac12\widehat M_i(3).
  \]

**COLLAPSE-DIAGNOSTIC** if:

- all eight chains pass;
- for every spatial direction,
  \[
  \widehat M_i(4)\le\frac14\widehat M_i(3).
  \]

**INCONCLUSIVE** otherwise.

These are engineering route-selection thresholds. None is an asymptotic
scientific claim.

## Firewall

No terminal proves or falsifies:

- \(\liminf P_L>0\);
- sector polarization at large L;
- the #1134 weighted bridge;
- P1;
- a massless phase or physical photon.

## Execution contract

After this preregistration and \`diagnostic.py\` are committed and publicly
read back, execute the frozen script once on JAS 2. A process error or missing
complete stdout gives STOP_EXECUTION and consumes the identifier. Do not
shorten or retry under this name.

## Repository boundary

Only \`notes/C-PHOTON-SECTOR-FLUX-DIAGNOSTIC-N/\` may be added.
