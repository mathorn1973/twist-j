# Typed Success-State and Retention Contract

**PUBLIC, NON-CANONICAL. Interface of `C-HOMOGENEOUS-RECORD-RETENTION-N` for
composition with a later preparation or joint-detector result.**

License: Apache-2.0.

Corrected after review (R1–R3); changes itemized in `CORRECTIONS.md`.

## 1. Fields

| Field | Value |
|---|---|
| Law | unchanged Public Canon v105 `HOMOGENEOUS-CAPTURE-CURRENT-RECORD` law, $U = U_0C$, $U_{\rm rec} = \mathcal T(U\otimes I)\mathcal T^*$ |
| Carrier and sector | one object pair, one carrier (standing token or moving pulse), one receiver at $z = 100$, coded memory $\mathcal D$ (26 labels), arbitrary reference $\mathcal H_{\rm ref}$ |
| Spatial cut | carrier position $c = y$ (token) or $x$ (pulse); record side $c\ge z$; current cut $\ell = z-1 = 99$ |
| Time | macrosteps $n$ between synchronized phase-zero slices; one macrostep = two microticks |
| Memory projection | $R_1 = I\otimes|d_1\rangle\langle d_1|\otimes I$ at $z$ |
| Old information | carrier label on $c\ge z$, memory on $c<z$ (exact, `PROOF.md` Theorem 1) |
| Charge and energy | active native charge $10$ unchanged; success family spectrally inside $I_E$; no extra resources |
| Admitted writers | only the receiver edge on $(z-1,z)$; leftward crossings un-write exactly; contacts at $s\ge z$ do not change the record |

## 2. Exact identity (any one-carrier state)

For a calibrated state $\chi\otimes e_1\otimes\Phi$ and every $n$:

$$
\Pr(\text{wrong memory at }n) = (1-\langle d_1,\sigma_{\mathcal D}d_1\rangle)\,
\|\mathbf 1_{c<z}U^n\chi\|^2 ,
$$

uniformly in the memory/reference input, with the per-step change equal to
$-\tfrac14$ of the carrier current through the cut $\ell = z-1$.

## 3. Retention input type

$$
\mathsf S_{\rm ret} := \Bigl\{\Psi_{\rm phys}(n_0) =
U_{\rm rec}^{n_0}\Omega_{{\rm rec},+}\mathcal T_+(\varphi\otimes\Phi)\ :\
\varphi\in\mathcal F,\ \Phi\in\mathcal D\otimes\mathcal H_{\rm ref},\
\|\Phi\| = 1\Bigr\},
$$

where $\mathcal F$ is the declared product family of `PROOF.md` §6.0
($N = 5$, $p_1 = w = 1/1000$, object shift $R_c\le0$, pulse shift
$x_c\ge0$) and $n_0$ is the elapsed time since the asymptotic reference slice
of $\varphi$.

## 4. Retention guarantee

For $\Psi\in\mathsf S_{\rm ret}$ with elapsed time $n_0$, every $m\ge0$ with
$n_0+m\ge T$:

$$
\|(I-R_1)U_{\rm rec}^m\Psi\|\le\varepsilon(T),\qquad
\|U_{\rm rec}^m\Psi-\Psi^{\rm ideal}_{n_0+m}\|\le\sqrt2\,\varepsilon(T),
$$

where $\varphi = \varphi_{\rm sp}\otimes p_1$ carries its label, $\eta_n\in
\mathcal H_{\rm sp}$ is defined by $U^n\Omega_+\varphi = \eta_n\otimes e_1$
(i.e. $\eta_n = U^n\Omega_+\varphi_{\rm sp}$), the ideal record is
$\Psi^{\rm ideal}_n = \sum_k\eta_n\otimes e_k\otimes d_1\otimes\phi_k$
(corrected, R2: the label is attached once), and $\varepsilon(T)$ is the exact
certified modulus of `RESULT.md` (frozen check at $T = 10^6$, tolerance
$1/100$).

## 5. Composition rule for a detector or preparation result

A later result composes with this contract only through an explicit inclusion
map and an error, in this form:

1. a physical post-state $\rho$ at a stated phase-zero slice, with the
   detection or preparation instrument and its outcome normalization declared,
   so that conditioning is explicit and leakage and failure outcomes are kept;
2. a certified $\Psi\in\mathsf S_{\rm ret}$ with elapsed time $n_0$ and a
   trace-norm error $\|\rho-|\Psi\rangle\langle\Psi|\|_1\le\epsilon_{\rm in}$;
3. after the slice the evolution is the unchanged $U_{\rm rec}$ (no further
   instrument acts on the receiver bond or the memory).

Then, for every $m$ with $n_0+m\ge T$,
$\operatorname{Tr}[(I-R_1)U_{\rm rec}^m\rho\,U_{\rm rec}^{-m}]\le
\varepsilon(T)^2+\epsilon_{\rm in}$, because $\|I-R_1\| = 1$. Without items 1–3
the ideal theorem says nothing about a measured state. An observation of $d_1$
alone is not an inclusion map: a pre-existing $d_1$ or a carrier that has not
crossed gives the same memory value.

## 6. Not supplied

- No inclusion of the normalized v105 selected component
  $Q_{\rm ch,full}\mathcal S\Psi_{\rm loc}/\sqrt{p(Q_{\rm full})}$ in
  $\mathsf S_{\rm ret}$; the minimal missing premise is stated in `PROOF.md` §7.
- No exact permanent retention of a captured record.
- No statement before $T$; the record may still be in transit.
