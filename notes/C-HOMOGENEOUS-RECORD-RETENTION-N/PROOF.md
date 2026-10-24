# Quantitative Record Retention on the Homogeneous Capture-Current-Record Law

**PUBLIC, NON-CANONICAL. Analytical proofs for `C-HOMOGENEOUS-RECORD-RETENTION-N`.**

License: Apache-2.0.
Authority basis: `mathorn1973/twist-j` main `892a0b11089d34e241e1eb76d2c03247022d18e6`
(Public Canon v105, tag `canon-v105`, content commit
`b8cdfd6ea58ae798545bc6000c817147fa0f0dcc`).
All model inputs are the public law, preparation and certified constants of
`HOMOGENEOUS-CAPTURE-CURRENT-RECORD [T]` (`canon/CANON.md`) and its public
analytical package `notes/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/`. Exact
audits of the finite and rational statements below are in
`reproduce/C-HOMOGENEOUS-RECORD-RETENTION-N/verify.py`; the group in which a
statement is audited is named in brackets.

Corrected after review in separate, itemized commits (R1–R3); the changes and
the reviewed version's SHA-256 are listed in `CORRECTIONS.md`.

---

## 0. Setting and notation

The law is the declared v105 law: $U = U_0 C$ on the one-pair one-carrier
space $\mathcal H_T \oplus \mathcal H_P$, the receiver at $z = 100$ with coded
memory $\mathcal D = \operatorname{span}\{d_0,\dots,d_{25}\}$, the half-line
calibration $\mathcal T = \mathcal T_1 \oplus \mathcal T_2$ and
$U_{\rm rec} = \mathcal T (U \otimes I)\mathcal T^*$. Times $n \in \mathbb Z$
count macrosteps between synchronized phase-zero slices.

- $R_1 := I \otimes |d_1\rangle\langle d_1| \otimes I$ is the memory projection
  at $z$ onto the written value $d_1$.
- The **carrier position** is $c = y$ on tokens and $c = x$ on pulses.
  $\mathbf 1_< := \mathbf 1_{c<z}$ and $\mathbf 1_\ge := \mathbf 1_{c\ge z}$ act
  on positions only.
- $\mathcal H_{\rm sp}$ is the spatial/coin part of the one-carrier space
  (token arrangement $\ell^2(R,r,y)\otimes\mathbb C^4$, pulse arrangement
  $\ell^2(R,r,x)\otimes\mathbb C^4\otimes\mathbb C^2$). Because $C$, $U_0$,
  $U$ and $\Omega_\pm$ act identically on the 26 carrier labels (v105, 26
  identical label blocks), a calibrated state with carrier label index $1$ is
  written $\chi \otimes e_1$, where $e_k$ denotes $t_k$ on tokens and $p_k$ on
  pulses, and $U^n(\chi \otimes e_1) = \chi_n \otimes e_1$ with
  $\chi_n := U^n\chi$.
- **Label-stripping convention (R2).** Several vectors below are defined with
  their carrier label already attached: $\varphi = \varphi_{\rm sp}\otimes
  p_1$ in §6, and the v105 $\Psi_{\rm loc} = \psi_{\rm loc}\otimes t_1$.
  Spatial projections ($\mathbf 1_<$, $\mathbf 1_\ge$), the norms
  $\Lambda_n$, $\delta_n$ and the operators $U$, $U_0$, $\Omega_\pm$ are
  applied to the spatial/coin factor; norms do not change. Whenever a label
  $e_k$ is attached again, it is attached to the spatial factor only, e.g.
  $U^n\Omega_+\varphi = \eta_n\otimes e_1$ with $\eta_n :=
  U^n\Omega_+\varphi_{\rm sp}\in\mathcal H_{\rm sp}$.
- A memory/reference input is $\Phi = \sum_{k=0}^{25} d_k \otimes \phi_k \in
  \mathcal D \otimes \mathcal H_{\rm ref}$, $\|\Phi\| = 1$; mixed inputs are
  treated by purification into the reference.

---

## 1. Exact record-location identity

**Theorem 1.** For every $\chi \in \mathcal H_{\rm sp}$, every $\Phi$ and
every $n \in \mathbb Z$,

$$
U_{\rm rec}^n\,\mathcal T(\chi\otimes e_1\otimes\Phi)
 = \sum_{k=0}^{25}\Bigl[\mathbf 1_<\chi_n\otimes e_1\otimes d_k
 + \mathbf 1_\ge\chi_n\otimes e_k\otimes d_1\Bigr]\otimes\phi_k .
 \tag{1}
$$

Consequently, writing $\Psi_n$ for the left side and
$\Lambda_n(\chi) := \|\mathbf 1_<\chi_n\|$:

1. $\|(I - R_1)\Psi_n\|^2 = (1 - \|\phi_1\|^2)\,\Lambda_n(\chi)^2$ exactly.
2. The supremum over all memory/reference inputs is $\Lambda_n(\chi)^2$,
   attained exactly when $\phi_1 = 0$. For a mixed input $\sigma$ on
   $\mathcal D\otimes\mathcal H_{\rm ref}$ the wrong-memory probability is
   $(1 - \langle d_1,\sigma_{\mathcal D} d_1\rangle)\Lambda_n(\chi)^2$.
3. Full-record deviation:
   $\|\Psi_n - \sum_k \chi_n\otimes e_k\otimes d_1\otimes\phi_k\|^2
   = 2(1-\|\phi_1\|^2)\Lambda_n(\chi)^2$.
4. Old-information location (corrected, R2): by (1), on the component
   $\mathbf 1_\ge\chi_n$ the old memory/reference state appears as
   $\sum_ke_k\otimes\phi_k$, i.e. in the carrier label, with the memory in
   $d_1$; on the component $\mathbf 1_<\chi_n$ it appears as
   $\sum_kd_k\otimes\phi_k$, i.e. still in the memory, with the carrier label
   $e_1$. The spatial/coin vector multiplying these label states is
   $\mathbf 1_\ge\chi_n$ or $\mathbf 1_<\chi_n$ and does not depend on $k$.
   Correlations of the reference with position therefore occur only through
   this left/right split, which is kept exactly; nothing is traced out.
5. One-step balance: with $J^{\rm car}_\ell := C^* D_c^*\, j_{E,\ell}\, D_c C$
   the carrier (pulse-bond) part of the v105 cut current at $\ell = z-1$,
   $$
   \Lambda_{n+1}(\chi)^2 - \Lambda_n(\chi)^2
   = -\tfrac14\,\langle\Psi_n, J^{\rm car}_{z-1}\Psi_n\rangle
   \qquad(\|\Phi\| = 1). \tag{2}
   $$

*Proof.* $\mathcal T$ is a unitary involution, so
$U_{\rm rec}^n = \mathcal T(U^n\otimes I)\mathcal T^*$ and
$U_{\rm rec}^n\mathcal T = \mathcal T(U^n\otimes I)$. The label identity gives
$(U^n\otimes I)(\chi\otimes e_1\otimes\Phi) = \chi_n\otimes e_1\otimes\Phi$.
$\mathcal T$ is the identity on $c<z$ and applies the exchange
$\mathsf J(e_1\otimes d_k) = e_k\otimes d_1$ on $c\ge z$; this is (1).
$(I-R_1)$ annihilates every $d_1$ term; the remaining vectors
$\mathbf 1_<\chi_n\otimes e_1\otimes d_k\otimes\phi_k$, $k\ne1$, are
orthogonal because the $d_k$ are, which gives item 1; item 2 follows by
linearity in the purification. In item 3 the difference is
$\sum_{k\ne1}\mathbf 1_<\chi_n\otimes(e_1\otimes d_k - e_k\otimes d_1)\otimes\phi_k$
with orthogonal summands of squared norm $2\|\mathbf 1_<\chi_n\|^2\|\phi_k\|^2$.
Item 4 is read off (1). For item 5 let
$N^{\rm car}_{R,\ell} := 4\cdot\mathbf 1_{c>\ell}$, the carrier part of the
v105 right-half native charge; for $\ell = z-1$,
$\mathbf 1_< = I - N^{\rm car}_{R,\ell}/4$. Since $N^{\rm car}$ is diagonal in
position it commutes with $\mathcal T$, and $U\otimes I = \mathcal T^*U_{\rm
rec}\mathcal T$, so
$\Lambda_{n+1}^2-\Lambda_n^2 = -\frac14\langle\Psi_n,(U_{\rm rec}^*N^{\rm
car}U_{\rm rec}-N^{\rm car})\Psi_n\rangle$. In the v105 factorization
$U_{\rm rec} = e^{-i\beta}\Gamma S_{\rm obj}D_{\rm edge,rec}D_cC$ the
contact, the coins, $\Gamma$ and the object streaming leave every carrier
position fixed and tokens never move; only the pulse bond hop across $\ell$
changes $N^{\rm car}$, and on the bond pair $(v_1(\ell), v_2(\ell+1))$ the
change of $4\|v_2(\ell+1)\|^2$ under
$\left(\begin{smallmatrix}c&-s\mathsf S\\ s\mathsf S&c\end{smallmatrix}\right)$
is the quadratic form of
$j_{E,\ell} = 4\left(\begin{smallmatrix}s^2&sc\,\mathsf S\\ sc\,\mathsf S&-s^2\end{smallmatrix}\right)$
evaluated after $D_cC$ (as in the proof of v105 Theorem 4.1). $\square$

*Audit.* [Group 1] the label algebra on all 26 labels and items 1, 3, 4 on an
entangled two-site example. [Group 2] the complete local physical law (contact,
both coins, receiver edge with $\mathsf J$ at $(z-1,z)$, streaming, $\Gamma$)
evolved exactly in $\mathbb Z[i][\zeta_5]$ agrees with
$\mathcal T(U^n\otimes I)\mathcal T^*$ at every step on a state with tokens and
pulses on both sides of the receiver, writing and un-writing contacts and an
entangled reference; item 1 and the balance (2) hold exactly at every step;
unitarity holds; two negative controls (free edge, edge shifted by one bond)
fail as they must.

**Remark 1.1.** Theorem 1 replaces the v105 triangle bound
$\Pr(\text{wrong}\mid\Psi_+)\le\min\{\eta_n^2,(\delta_n+\widetilde\eta_n)^2\}$
(`PROOF_CURRENT_RECORD_INTERFACE.md` §1.1(4)) by an equality: for the
selected outgoing branch $\chi = \Omega_+(\psi_{{\rm out},+})$,
the wrong-memory probability is exactly $(1-\|\phi_1\|^2)\Lambda_n^2$ with
$\Lambda_n \le \delta_n + \widetilde\eta_n$, where
$\delta_n = \|\mathbf 1_{x<z}U_0^n\psi_{{\rm out},+}\|$ and
$\widetilde\eta_n = \|(U^n\Omega_+ - U_0^n)\psi_{{\rm out},+}\|$.

**Corollary 1.2 (unpostselected v105 input).** For the v105 preparation
$\Psi_{\rm phys} = \Omega_{{\rm rec},-}(\Psi_{\rm loc}\otimes\Phi)$ with
$\Psi_{\rm loc} = \psi_{\rm loc}\otimes t_1$ (token at $y = 0 < z$),
$\mathcal T_-^*$ acts as the identity on the input, so
$\Psi_{\rm phys} = \mathcal T(\Omega_-\psi_{\rm loc}\otimes e_1\otimes\Phi)$
and, by Theorem 1,

$$
\Pr(\text{wrong memory at }n)
 = (1-\|\phi_1\|^2)\bigl(1 - p_R(n)\bigr),\qquad
 p_R(n) := \|\mathbf 1_\ge U^n\Omega_-\psi_{\rm loc}\|^2 .
$$

$p_R(n)$ counts every carrier right of the receiver, including right-moving
pulses accompanied by unbound object outcomes; its limit is not computed here.
Only $p(Q_{\rm full}) > 2/10^{28}$ is certified (v105). Nothing is
conditioned away: on the full input the transferred record exists only on the
carrier-right fraction.

---

## 2. Writers, eraser and admitted overwrites

**Theorem 2.** On the declared one-carrier sector with memory in $\mathcal D$:

1. The memory label changes only through the receiver edge $D_{\rm rec}$ on the
   bond $(z-1,z)$; contact, coins, streaming, $\Gamma$ and the token step act
   as the identity on the memory.
2. A carrier crossing the bond to the right writes (exchanges) and a carrier
   crossing it to the left un-writes exactly: by (1) the memory content on
   $\operatorname{Ran}\mathbf 1_<$ is the original memory, with no third value.
   A record held at time $n$ is lost at a later time exactly to the extent
   that carrier weight has returned to $c<z$, and (2) states that this loss is
   one quarter of the carrier flux through the receiver cut.
3. A contact at $s\ge z$ converts pulse and token at the same site and leaves
   the record unchanged ($[\mathcal T, C\otimes I] = 0$, both sides on
   $\operatorname{Ran}\mathbf 1_\ge$).
4. Not covered by the declared law (statements about other laws, not claims):
   a second carrier crossing the bond would apply $\mathsf J$ again and move
   the $d_1$ record into that carrier (overwrite); memory contents in
   $\mathcal D^\perp$ are never written (free edge $E\otimes I$ on
   $\mathcal D^\perp$); active helpers, other receivers, locks or archives are
   not part of the law.

*Proof.* Item 1 is the v105 local realization
(`PROOF_CURRENT_RECORD_INTERFACE.md` Theorem 1.1(2)); items 2 and 3 follow
from (1) and (2). $\square$

---

## 3. No retention modulus uniform over the success sector

**Theorem 3.** Let $Q_{\rm ch,full}$ be the v105 outgoing channel projector
(label $p_1$). For every $n\in\mathbb Z$ and $\epsilon>0$ there is a unit
$\varphi\in\operatorname{Ran}Q_{\rm ch,full}$ with
$\Lambda_n(\Omega_+\varphi)\ge 1-\epsilon$. Hence, with $\phi_1 = 0$, the
supremum of the wrong-memory amplitude at time $n$ over the normalized
success sector equals $1$, for every $n$.

*Proof.* The joint translations $\tau_m:(R,c)\mapsto(R+m,c+m)$ commute with
$U$, $U_0$, $C$, $\Omega_+$, and with $Q_{\rm ch,full}$, which is a function of
the momenta $(P,k)$ and of fiber projectors. Fix a unit
$\varphi_0\in\operatorname{Ran}Q_{\rm ch,full}$ (nonempty by v105, or by
Theorem 6). Then $\varphi_m := \tau_{-m}\varphi_0\in\operatorname{Ran}Q_{\rm
ch,full}$ and $\|\mathbf 1_{c<z}U^n\Omega_+\varphi_m\| =
\|\mathbf 1_{c<z+m}U^n\Omega_+\varphi_0\|\to\|U^n\Omega_+\varphi_0\| = 1$ as
$m\to\infty$, since $\mathbf 1_{c<z+m}\to I$ strongly. $\square$

The asymptotic success event carries no time stamp and no position. Any
finite-interval or future-uniform statement therefore needs declared
localization data, and the write time of a success state can be arbitrarily
late. One successful capture is not a retention guarantee.

---

## 4. Free no-parking: no exact permanent retention for the free surrogate

Let $V$ be the free pulse step on $\ell^2(\mathbb Z)\otimes\mathbb C^2$ with
symbol $V(k)$, and put $w = e^{-ik}$. In this variable
$V_{11} = (1-4w^{-1})/5$, $V_{12} = -2(1+w^{-1})/5$, $V_{21} = 2(1+w)/5$,
$V_{22} = (1-4w)/5$, $\det V = 1$ and
$$
25w^2\bigl((\operatorname{tr}V)^2-4\bigr) = 16(w+1)^2(w^2-3w+1). \tag{3}
$$
The factor $w^2-3w+1$ has the simple root $w_0 = (3-\sqrt5)/2\in(0,1)$.
[Group 3 audits these identities.]

**Theorem 4.**

1. No nonzero $\pi$ supported in $\{x\ge z\}$ has $\hat\pi(k)$ in a single
   eigenline of $V(k)$ for almost every $k$ (for any measurable choice of the
   eigenvalue). In particular no nonzero right-moving state
   ($\Pi_{v<0}\pi = 0$) is supported in $\{x\ge z\}$.
2. If $\pi\ne0$ is right-moving, then $\mathbf 1_{x<z}V^m\pi\ne0$ for every
   $m\in\mathbb Z$. If $\Pi_{v<0}\pi\ne0$, then
   $\lim_{m\to\infty}\|\mathbf 1_{x<z}V^m\pi\| = \|\Pi_{v<0}\pi\|>0$.
   Hence $\bigcap_{m\ge0}V^{-m}\operatorname{Ran}\mathbf 1_{x\ge z} = \{0\}$.
3. For every nonzero selected outgoing branch $\psi_{{\rm out},+}$ (bound
   object, right-moving plus-band pulse, possibly entangled), the v105 free
   tail satisfies $\delta_n>0$ for every $n$: the free-surrogate record is
   never complete at any finite time.
4. Exact witness that one exact retention instant is not durability: the
   pulse $\pi = e_2$ at $x = z+2$ has
   $\|\mathbf 1_{x<z}V^m\pi\|^2 = 0$ for $m = 0,1,2$ and $= 1024/15625$ for
   $m = 3$ (unique light-cone path, amplitude $-32/125$). With any object at
   distance greater than $6$ from the pulse the coupled evolution coincides
   with the free one for these three steps (contacts need $R = x$ and the
   relative coordinate moves by at most $2$ per step), so by Theorem 1 the
   wrong-memory probability is exactly $0$ at $n = 0,1,2$ and
   $(1-\|\phi_1\|^2)\cdot1024/15625$ at $n = 3$. [Group 3]

*Proof of 1.* If $\pi$ is supported in $x\ge z$, then
$\hat\pi = (f,g)$ with $f,g\in w^zH^2(\mathbb D)$. Suppose
$(V(k)-\mu(k))\hat\pi(k) = 0$ a.e. If $f\equiv0$, the first row gives
$V_{12}g = 0$ a.e.; $V_{12}$ vanishes on $|w| = 1$ only at $w = -1$, so
$g = 0$ and $\pi = 0$. Otherwise $f\ne0$ a.e. on the circle (a nonzero Hardy
function has nonzero boundary values a.e.), and
$\mu = (V_{11}f+V_{12}g)/f$ a.e. Because $\mu^2-(\operatorname{tr}V)\mu+1 = 0$,
the function
$\widetilde Q := w^{2-2z}\bigl[(V_{11}f+V_{12}g)^2-\operatorname{tr}V\,(V_{11}f+V_{12}g)f+f^2\bigr]$
belongs to $H^1(\mathbb D)$ (products of $H^2$ functions times polynomials,
since $wV_{11}$, $wV_{12}$, $w\operatorname{tr}V$ are polynomials) and has zero
boundary values a.e.; hence $\widetilde Q\equiv0$. The meromorphic function
$m := (V_{11}f+V_{12}g)/f$ on $\mathbb D$ therefore satisfies
$m^2-(\operatorname{tr}V)m+1 = 0$, and $h := 2m-\operatorname{tr}V$ is
meromorphic on $\mathbb D$ with $h^2 = (\operatorname{tr}V)^2-4$. By (3) the
right side has a simple zero at $w_0\in\mathbb D$, whereas
$\operatorname{ord}_{w_0}(h^2) = 2\operatorname{ord}_{w_0}(h)$ is even, a
contradiction. A right-moving state has $\hat\pi(k)\in\operatorname{Ran}
\Pi_{v>0}(k)$, a line for a.e. $k$. $\square$

*Proof of 2.* $\Pi_{v<0}$ commutes with $V$, so $V^m\pi$ is nonzero and
right-moving and, by item 1, not supported in $x\ge z$. For the second
statement let $\psi\in\operatorname{Ran}\Pi_{v<0}$ have
$\hat\psi = h(k)u(k)$ with $h\in C_c^\infty(I)$, $u$ the analytic
left-moving eigenvector on an open interval $I\subset(0,\pi)$ or
$(-\pi,0)$ on which the group velocity is $\le -v_0<0$. Two integrations by
parts in $k$ (the phase derivative is $x - mv(k)\ge x+mv_0$) give
$|(V^m\psi)(x)|\le C_\psi(x+mv_0)^{-2}$ for $x\ge z$ and $m$ large, so
$\|\mathbf 1_{x\ge z}V^m\psi\|\to0$. Such $\psi$ are dense in
$\operatorname{Ran}\Pi_{v<0}$ and $V$ is unitary, so
$\|\mathbf 1_{x\ge z}V^m\pi_-\|\to0$ for every $\pi_-\in\operatorname{Ran}
\Pi_{v<0}$, and likewise $\|\mathbf 1_{x<z}V^m\pi_+\|\to0$ for every
right-moving $\pi_+$. With $\pi = \pi_-+\pi_+$ this gives the limit. $\square$

*Proof of 3 (corrected, R2).* On the pulse arrangement $U_0 =
W\otimes\widetilde V$ commutes with the velocity spectral projection
$I\otimes\Pi_{v>0}$, so $U_0^n\psi$ is right-moving. ($U_0$ does not commute
with $I\otimes\mathbf 1_{x<z}$: the pulse hops across the cut; this is not
used.) If $\mathbf 1_{x<z}U_0^n\psi = 0$, expand $U_0^n\psi = \sum_i
e_i\otimes\pi_i$ in an orthonormal object basis. The partial inner products
$\langle e_i|\otimes I$ commute with $I\otimes\Pi_{v>0}$ and
$I\otimes\mathbf 1_{x<z}$, so every $\pi_i$ is right-moving and supported in
$x\ge z$, hence zero by item 1; so $\psi = 0$. $\square$

---

## 5. Eternal parked records

**Proposition 5.** Let $d$ be the v105 dark object state at token site $n_0$
(`PROOF_CURRENT_RECORD_INTERFACE.md` §6.2) and let $n_0\ge z$. The physical
state $\Psi = \mathcal T(d\otimes|y=n_0\rangle\otimes e_1\otimes\Phi)$ satisfies
$(I-R_1)U_{\rm rec}^m\Psi = 0$ for every $m\in\mathbb Z$.

*Proof.* The inversion $\mathcal R_{n_0}|R,r,d\rangle = |2n_0-R,-r,5-d\rangle$
commutes with $W$, $\mathcal R_{n_0}\alpha_{n_0} = -\alpha_{n_0}$ and
$\mathcal R_{n_0}d = d$, so $\langle\alpha_{n_0},W^md\rangle = 0$ for all $m$;
the contact never fires, the token stays at $n_0\ge z$, $\mathbf 1_<\chi_m = 0$,
and Theorem 1 applies. $\square$ [Group 4: the inversion relations, the
commutation on every basis state of a $5\times5$ box around the contact, zero
contact overlap for $m = 0,\dots,8$, and the exact physical evolution with
memory $d_1$ for $m = 0,\dots,5$.]

Exact permanent, indeed eternal, retention therefore occurs on the declared law
without any lock. The example is a configuration whose record is held at all
past and future times: there is no write event, no capture, no bound-pair or
outgoing-pulse herald, and the state lies outside $\operatorname{Ran}Q_{\rm
full}$. Proposition 5 is an existence statement; it does not classify eternal
records (corrected wording, R2). "$R_1$ holds for all future times" neither requires a lock nor
certifies that a capture happened. Whether the invariant subspace
$\bigcap_{m\ge0}U^{-m}\operatorname{Ran}\mathbf 1_\ge$ meets
$\Omega_+\operatorname{Ran}Q_{\rm ch,full}$ (exact permanent retention of a
captured record without a lock) is **not decided** here; Theorem 4 excludes it
for the free surrogate.

---

## 6. Future-uniform retention for a declared success family

### 6.0 Family and statement

Let $b(t) = (1-t^2)^N\mathbf 1_{|t|\le1}$, $\chi_0 = \delta_{r=0}A$
($= b_0$ of v105), $k_0 = -\arccos((9-5\sqrt5)/16)$ and $e_2$ the second pulse
bank. The declared family $\mathcal F$ consists of the product outgoing states

$$
\varphi = \chi\otimes\pi\otimes p_1 =: \varphi_{\rm sp}\otimes p_1,\qquad
\hat\chi(P) = A_g\theta_g\,b(P/p_1)\,\Pi_b(P)\chi_0,\qquad
\hat\pi(k) = A_h\theta_h\,b\bigl((k-k_0)/w\bigr)P_+(k)e_2,
$$

with unimodular constants $\theta_g,\theta_h$, normalizing $A_g,A_h>0$
($\|\chi\| = \|\pi\| = 1$), and their joint translates with the object moved
by $R_c\le0$ and the pulse by $x_c\ge0$. Frozen parameters: $N = 5$,
$p_1 = w = 1/1000$, $z = 100$, $h = 1/1000$, $\rho_P = 1/10$,
$\rho_k = 3/10$. Fourier conventions are those of v105:
$\hat\chi(P) = \sum_R\chi(R)e^{-iPR}$ with fiber walk $W(P)$ on
$\ell^2(\mathbb Z_r)\otimes\mathbb C^4$, and $\hat\pi(k) = \sum_x\pi(x)e^{-ikx}$.

The success state is $\Psi_+ := \mathcal T_+(\varphi\otimes\Phi) =
\chi\otimes\pi\otimes\sum_kp_k\otimes d_1\otimes\phi_k\in\operatorname{Ran}
Q_{\rm full}$ and its physical evolution is
$\Psi_{\rm phys}(n) := U_{\rm rec}^n\Omega_{{\rm rec},+}\Psi_+$, a unit vector.

**Theorem 6.** For every $\varphi\in\mathcal F$, every memory/reference input
$\Phi$ and every $n\ge T$,
$$
\|(I-R_1)\Psi_{\rm phys}(n)\| \le \varepsilon(T) := \bar\delta(T)+\bar\eta(T),
$$
with $\bar\delta,\bar\eta$ the explicit decreasing functions of §§6.8–6.9.
The exact rational certificate [Group 6] evaluates $\varepsilon(10^6)$ against
the frozen tolerance $1/100$ and tabulates $\varepsilon(T)$ for
$T\in\{2\cdot10^5,5\cdot10^5,10^6,10^7\}$.

### 6.1 Membership in the success sector

$|P|\le p_1\le1/100$; $\hat\chi(P)\in\operatorname{Ran}\Pi_b(P)$;
$\hat\pi(k)\in\operatorname{Ran}P_+(k)$ with $k\in[k_0-w,k_0+w]\subset
(-\pi,0)$, where $\varepsilon'>0$; the label is $p_1$. For the energy window,
$\varepsilon(k_0) = g$ and $\Omega(0) = g$, so with §§6.4–6.5,
$|\Omega(P)+\beta+\varepsilon(k)-8\pi/5|\le E^o_2p_1^2/2+v_{\max}w\le h$
[Group 5]. On each fiber $K$ the eigenvalue phase
$P\mapsto\Omega(P)+\varepsilon(K-P)$ has derivative
$\Omega'-\varepsilon'\le v_b-v_{\min}<0$, so the fiber components lie in the
absolutely continuous channel space of $U_0(K)$. Hence
$\varphi\in\operatorname{Ran}Q_{\rm ch,full}$ and $\Psi_+\in
\operatorname{Ran}Q_{\rm full}$. Translations commute with $Q_{\rm ch,full}$.

### 6.2 Analytic bound branch

v105 gives $W(P) = e^{iPQ}W(0)$ with $Q = \operatorname{diag}(1,0,0,-1)$, and
$\|(w-W(0))^{-1}\|\le M_0 = 440/53$ on $C = \{|w-z| = 1/8\}$, $z = e^{-ig}$.
For complex $|P|\le\rho_P$, $\|W(P)-W(0)\|\le e^{|P|}-1$, so a Neumann series
gives $\|(w-W(P))^{-1}\|\le M_R := M_0/(1-M_0(e^{\rho_P}-1))$ on $C$
(the product is below one [Group 5]). The Riesz projector
$\Pi(P) = \frac1{2\pi i}\oint_C(w-W(P))^{-1}dw$ is analytic, of rank one, with
$\|\Pi(P)\|\le M_R/8$; its eigenvalue $\lambda(P)$ lies in $|w-z|<1/8$, so
$\Omega(P) := g+i\operatorname{Log}(\lambda(P)/z)$ is analytic with
$|\Omega(P)-g|\le\log(8/7)\le1/7$, and agrees with the v105 dispersion on the
real axis. $N(P) := \langle\chi_0,\Pi(P)\chi_0\rangle$ is analytic with
$|N|\le M_R/8$, and for real $|P|\le1/12$,
$N(P) = |\langle\chi_0,\chi_b(P)\rangle|^2\in[8424/11449,1]$ (v105).

### 6.3 Symmetry

With $\widetilde{\mathcal R}|r,d\rangle = |-r,5-d\rangle$:
$\widetilde{\mathcal R}W(0)\widetilde{\mathcal R} = W(0)$ (the coin matrix is
invariant under $d\mapsto5-d$, displacements reverse, $\Gamma$ is even) and
$\widetilde{\mathcal R}Q\widetilde{\mathcal R} = -Q$, so
$W(-P) = \widetilde{\mathcal R}W(P)\widetilde{\mathcal R}$ and $\lambda(-P) =
\lambda(P)$: $\Omega$ is even and $\Omega'(0) = 0$. Since
$\widetilde{\mathcal R}\chi_0 = -\chi_0$, $N$ is even. [Group 4]

### 6.4 Object constants (Cauchy)

For real $|P|\le p_1$ and $r_P := \rho_P-p_1$:
$|\Omega^{(b)}(P)|\le E^o_b := b!/(7r_P^b)$ for $b\ge1$,
$|N^{(j)}(P)|\le j!M_R/(8r_P^j)$ for $j\ge1$, $|N|\le1$;
$|\Omega'(P)|\le p_1E^o_2 =: v_b$ and $|\Omega(P)-g|\le E^o_2p_1^2/2$.

### 6.5 Pulse constants

$\gamma(k) = (1-4\cos k)/5$, $\varepsilon = \arccos\gamma$,
$\gamma_0 = \cos g$. For $|k-k_c|\le\rho_k$ with $k_c$ in the window,
$|\cos k-\cos k_0|\le(w+\rho_k)\cosh\rho_k$, hence
$|\gamma-\gamma_0|\le r_\gamma := \frac45(w+\rho_k)\cosh\rho_k<1-\gamma_0$.
On that disk $\sin\varepsilon = \sqrt{1-\gamma^2}$ is analytic with
$|\sin\varepsilon|\ge\sigma_{\min} := \sqrt{(1-r_\gamma)^2-\gamma_0^2}$ and
$|\varepsilon-g|\le r_\varepsilon := r_\gamma/\sigma_{\min}$. The plus
projector $P_+ = (V-e^{i\varepsilon})/(-2i\sin\varepsilon)$ is analytic; using
$V_{22}-\gamma = \frac{4i}5\sin k$, $e^{i\varepsilon} = \gamma+i\sin\varepsilon$,
$|\sin k|\le\cosh\rho_k$ and $|\sin\varepsilon|^2\le1+|\gamma|^2$:
$$
|p_{12}|\le\frac{1+e^{\rho_k}}{5\sigma_{\min}},\qquad
|p_{22}|\le\frac{\frac45\cosh\rho_k+\sqrt{1+(\gamma_0+r_\gamma)^2}}{2\sigma_{\min}} .
$$
On the real window $|p_{12}|\le1/2$ and $p_{22} = (1+v)/2$ with
$v^2 = 2(1-\cos k)/(3-2\cos k)$, decreasing in $\cos k$, so
$v\in[v_{\min},v_{\max}]$ from $|\cos k-\cos k_0|\le w$. Cauchy:
$|\varepsilon^{(b)}|\le E^p_b := b!\,r_\varepsilon/\rho_k^b$ and
$|p_{i2}^{(j)}|\le j!M_{p,i}/\rho_k^j$.

### 6.6 Non-stationary phase with explicit constant

**Lemma 6.6.** Let $F\in C^N[a,b]$ with $F^{(j)}(a) = F^{(j)}(b) = 0$ for
$j<N$, and $\Phi$ real with $|\Phi'|\ge D>0$, $|\Phi^{(b)}|\le mE_b$ for
$b\ge2$, and $m/D\le1/\kappa$. Define $\mathcal LF := (F/\Phi')'$ and expand
$\mathcal L^NF = \sum_tc_tF^{(a_t)}\prod_b(\Phi^{(b)})^{e_{t,b}}
\Phi'^{-(N+\sum_be_{t,b})}$. Then
$$
\Bigl|\int_a^bFe^{i\Phi}\frac{dk}{2\pi}\Bigr|\le\frac{K}{D^N},\qquad
K := \frac1{2\pi}\sum_t|c_t|\,\|F^{(a_t)}\|_{L^1}\prod_b(E_b/\kappa)^{e_{t,b}}.
$$

*Proof.* $e^{i\Phi} = (i\Phi')^{-1}(e^{i\Phi})'$; $N$ integrations by parts
have vanishing boundary terms because $\mathcal L^jF$ is a combination of
$F^{(a)}$, $a\le j<N$. Each application of $\mathcal L$ raises
$q-\sum_be_b$ by one, so $q = N+\sum_be_b$ and
$m^{\sum e}/D^q\le\kappa^{-\sum e}D^{-N}$. $\square$

The bump gives $\|F^{(a)}\|_{L^1}\le A\sum_c\binom ac w^{1-c}\|b^{(c)}\|_{L^1[-1,1]}
\sup|p^{(a-c)}|$ (and the same with $p_1$, $N$ for the object), with
$\|b^{(c)}\|_{L^1}\le\sum_i|\beta^{(c)}_i|\frac2{i+1}$ for the coefficients
$\beta^{(c)}_i$ of $b^{(c)}$, $A_g^2\le2\pi/(N_{\min}p_1I_b)$,
$A_h^2\le2\pi/(\frac{1+v_{\min}}2wI_b)$ and $I_b = \int_{-1}^1b^2$ exact.

### 6.7 Amplitudes

The object contact amplitude is
$a_s(m) := \langle R=s,r=0,A|W^m\chi\rangle = \theta_g\int G(P)e^{i(Ps-m\Omega(P))}
\frac{dP}{2\pi}$ with $G = A_gb(P/p_1)N(P)$, because
$W(P)^m\Pi(P)\chi_0 = \lambda(P)^m\Pi(P)\chi_0$. For $s>mv_b$ Lemma 6.6 gives
$|a_s(m)|\le K_o/(s-mv_b)^N$. The pulse amplitudes are
$\pi_m(x)_i = e^{-im\beta}\theta_h\int A_hb\,p_{i2}\,e^{i(kx-m\varepsilon(k))}
\frac{dk}{2\pi}$; for $x<mv_{\min}$, $|\pi_m(x)_i|\le K_{p,i}/(mv_{\min}-x)^N$.

### 6.8 Free tail

$\delta_n := \|\mathbf 1_{x<z}U_0^n\varphi\| = \|\mathbf 1_{x<z}V^n\pi\|$. With
$D_0 := nv_{\min}-z+1$, $S(D) := D^{-2N}+D^{1-2N}/(2N-1)$ and
$\kappa_\delta := v_{\min}-(z-1)/T$,
$$
\delta_n^2\le(K_{d,1}^2+K_{d,2}^2)\,S(D_0) =: \bar\delta(n)^2
\qquad(n\ge T),
$$
where $K_{d,i}$ uses the ratio bound $n/(nv_{\min}-x)\le1/\kappa_\delta$
($x\le z-1$), and $\sum_{j\ge0}(D_0+j)^{-2N}\le S(D_0)$.

### 6.9 Cook bound for the interaction

For $\psi = U_0^n\varphi$ in the channel space,
$\Omega_+\psi-\psi = \sum_{m\ge0}U^{-m-1}U_0(I-C)U_0^m\psi$ whenever the norms
are summable, so
$\widetilde\eta_n := \|(U^n\Omega_+-U_0^n)\varphi\|\le\sum_{m\ge n}
\|(I-C)U_0^m\varphi\|$. On the pulse arrangement
$\|(I-C)\xi\|^2 = \frac45\sum_{s,j}|\langle\gamma_{s,j},\xi\rangle|^2$, and for
$\varphi$ the only port amplitudes are
$\langle\gamma_{s,1},U_0^m\varphi\rangle = a_s(m)\,\pi_m(s)_1$ up to a phase.
Split at $\sigma_m = m(v_b+v_{\min})/2$ and put $\kappa_c := (v_{\min}-v_b)/2$,
$A_\infty := \|G\|_{L^1}/2\pi\ge\sup_s|a_s|$,
$B_\infty := \|A_hb\,p_{12}\|_{L^1}/2\pi\ge\sup_x|\pi_m(x)_1|$:
$$
\sum_s|a_s\pi_m(s)_1|^2\le B_\infty^2\sum_{s>\sigma_m}|a_s|^2
+A_\infty^2\sum_{s\le\sigma_m}|\pi_m(s)_1|^2\le C_{\rm sum}^2S(\kappa_cm),
$$
$C_{\rm sum}^2 := B_\infty^2K_o^2+A_\infty^2K_{p,1}^2$ (ratio $\kappa_c$). Using
$\sqrt{S(D)} = D^{1/2-N}\sqrt{1/D+1/(2N-1)}$ and
$\sum_{m\ge n}m^{1/2-N}\le n^{1/2-N}+n^{3/2-N}/(N-3/2)$:
$$
\widetilde\eta_n\le\bar\eta(n) := \frac2{\sqrt5}C_{\rm sum}
\sqrt{\frac1{\kappa_cn}+\frac1{2N-1}}\;\kappa_c^{1/2-N}
\Bigl(n^{1/2-N}+\frac{n^{3/2-N}}{N-3/2}\Bigr).
$$

### 6.10 Assembly

$\Omega_{{\rm rec},+} = \mathcal T(\Omega_+\otimes I)\mathcal T_+^*$ (v105) and
$\mathcal T_+^*\Psi_+ = \varphi\otimes\Phi$ give
$\Psi_{\rm phys}(n) = \mathcal T(U^n\Omega_+\varphi\otimes\Phi)$. Theorem 1 and
$\Lambda_n\le\delta_n+\widetilde\eta_n$ give
$\|(I-R_1)\Psi_{\rm phys}(n)\| = \sqrt{1-\|\phi_1\|^2}\Lambda_n\le
\bar\delta(n)+\bar\eta(n)\le\varepsilon(T)$ for $n\ge T$, since both bounds
decrease in $n$. $\square$

**Corollary 6.1.** Wrong-memory probability $\le\varepsilon(T)^2$. With
$\eta_n := U^n\Omega_+\varphi_{\rm sp}$ (label-stripping convention, R2), the
full-record deviation obeys
$\|\Psi_{\rm phys}(n)-\sum_k\eta_n\otimes e_k\otimes d_1\otimes\phi_k\|
\le\sqrt2\,\varepsilon(T)$, so the old memory/reference state is carried by
the carrier label within $\sqrt2\,\varepsilon(T)$ for all $n\ge T$,
uniformly over $\Phi$.

**Corollary 6.2 (translates).** For the object moved by $R_c\le0$ and the
pulse by $x_c\ge0$, $a_s\mapsto a_{s-R_c}$ and $\pi_m(x)\mapsto\pi_m(x-x_c)$;
the tail sums over $s>\sigma_m$, $s\le\sigma_m$ and $x<z$ only shrink, so the
same $\varepsilon(T)$ holds.

**Remark 6.3.** The constants are conservative: Cauchy estimates on complex
disks, $L^1$ bounds through coefficient sums, and Cook's sum, which ignores all
cancellation. No claim is made that the true error is small earlier; the theorem
asserts only the stated upper bound.

---

## 7. The actual v105 selected component

For $\hat\varphi := Q_{\rm ch,full}\mathcal S\Psi_{\rm loc}/\sqrt{p(Q_{\rm
full})}$, Theorem 1 gives the exact wrong-memory amplitude
$\sqrt{1-\|\phi_1\|^2}\,\Lambda_n(\Omega_+\hat\varphi)$. The proof of
Theorem 6 applies verbatim to any $\varphi\in\operatorname{Ran}Q_{\rm
ch,full}$ for which (i) a free-tail bound on $\mathbf 1_{x<z}U_0^n\varphi$ and
(ii) a summable bound on $\|(I-C)U_0^m\varphi\|$ are certified. The v105
certificates do not supply either for $\hat\varphi$: they bound $p(Q_{\rm
full})$ from below through Carathéodory functions, with control of
$|4+F_1F_2|$ only on a subset of large measure, and give no pointwise bound
on energy derivatives of $\mathcal S(K,E)$, hence no Wigner time delay and no
position moment of $\hat\varphi$; moreover $\hat\varphi$ has jump
discontinuities at the sharp edges of $I_E$ and $|P|\le1/100$, where the
integration by parts of Lemma 6.6 is unavailable. **Minimal missing premise:** a
certified bound on a position moment
$\|(1+|X_{\rm pulse}-X_{\rm obj}|)^s\hat\varphi\|$ for some $s>0$ together with
a summable contact-decay bound, or a smoothed preparation whose outgoing
component lies in a family of the type of $\mathcal F$. The receiver itself
imposes no time limit: by Theorem 1 every retention error is carrier transport.

---

## 8. Status of the requested targets

| Target | Status here |
|---|---|
| Exact identity, uniform over coded memory/reference inputs | Proved (Theorem 1) |
| Recrossing, eraser and overwrite classification | Proved on the declared law (Theorem 2) |
| Uniform modulus over the whole success sector | Impossible (Theorem 3) |
| Exact permanent retention of a captured record | Not claimed; impossible for the free surrogate at every time (Theorem 4); eternal parked records exist outside the success sector (Proposition 5); interacting captured case open |
| Finite interval $[T,T+L]$ | Subsumed by the future-uniform bound for $\mathcal F$ |
| Future-uniform approximate retention, declared family $\mathcal F$ | Theorem 6; frozen tolerance checked by the exact certificate |
| Future-uniform retention of the actual normalized v105 component | Not achieved; missing premise in §7 |
| Lock, archive or reset | None added; the law is the unchanged v105 law |
