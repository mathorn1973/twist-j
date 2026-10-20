# Polarizations of the Fixed CM5 Jacobian: Ideal Bijection and Hecke Series

```text
STATUS:                  NON-CANONICAL / PROOF-ONLY CLASSICAL DICTIONARY
AUTHORITY:               Public Canon v103 (dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d)
CANON / REGISTRY CHANGE: NONE
LICENSE:                 Apache-2.0 (A. M. Thorn)
```

This document proves the all-prime and all-norm polarization dictionary on the
benchmark complex abelian surface $B = \operatorname{Jac}(y^2 = x^5 - 1)$,
extending the public calibration notes
[`HODGE-AND-TATE-CM5-CALIBRATION-2026-09-11.md`](../HODGE-AND-TATE-CM5-CALIBRATION-2026-09-11.md)
and
[`HODGE-TATE-CM5-INTEGRAL-HOMOLOGY-CALIBRATION-2026-09-11.md`](../HODGE-TATE-CM5-INTEGRAL-HOMOLOGY-CALIBRATION-2026-09-11.md).
The results are unconditional classical consequences of the selected benchmark
and make no claim of novelty in the mathematical literature.

---

## 1. Fixed Benchmark and Exact Claims

Work over $\mathbb C$, or geometrically over $\overline{\mathbb Q}$ via a fixed
embedding into $\mathbb C$. Fix the smooth projective genus-two curve, its
Jacobian, and its canonical principal polarization:

$$
C:\ y^2 = x^5 - 1, \qquad B = \operatorname{Jac}(C), \qquad
\lambda_0 : B \xrightarrow{\sim} B^\vee.
$$

Let $\zeta = \exp(2\pi i/5)$. The curve automorphism $T : (x,y) \mapsto (\zeta x, y)$
fixes the chosen embedding

$$
\mathcal O_K = \mathbb Z[\zeta] \hookrightarrow \operatorname{End}_{\mathbb C}(B),
\qquad K = \mathbb Q(\zeta), \qquad
F = K^+ = \mathbb Q(\sqrt 5).
$$

Write $\phi = (1+\sqrt 5)/2$, $\mathcal O_F = \mathbb Z[\phi]$, and $L = \log\phi$.
Complex conjugation on $K$ is denoted by a bar. The two real embeddings of $F$
satisfy $\sigma_1(\phi) = \phi$ and $\sigma_2(\phi) = -\phi^{-1}$.

These are explicitly selected benchmark data. In agreement with the registered
theorem `CM-PERIOD-LATTICE-NONSELECTION [T]`, the bare algebraic carrier
$J = 1 + \zeta^2$ and its alternating pencil do not by themselves force a
unique complex torus, CM type, principal polarization, or integral homology
marking.

For each integer $n \ge 1$, let $\mathcal P_n^{\mathrm{all}}(B)$ denote the set
of all polarizations $D$ on $B$ with reduced self-intersection
$q(D) := D^2/2 = n$, modulo pullback by origin-preserving holomorphic
automorphisms $\operatorname{Aut}(B,0)$. Here a polarization means its
polarization isogeny, equivalently its ample Neron-Severi class in
$\operatorname{NS}(B)$, not an individual line bundle retaining its
$\operatorname{Pic}^0(B)$ translation parameter. For a rational prime $p$, let
$\mathcal P_p(B) = \mathcal P_p^{\mathrm{all}}(B)$ be the set of polarizations
of type $(1,p)$ modulo $\operatorname{Aut}(B,0)$.

We prove:

1. **All-norm ideal bijection:** for every integer $n \ge 1$,
   $$
   \boxed{\mathcal P_n^{\mathrm{all}}(B) \xrightarrow{\sim}
     \{\mathfrak a \subset \mathcal O_F : N\mathfrak a = n\},
     \qquad [D_\eta] \longmapsto (\eta).}
   \tag{P1}
   $$
2. **Exact prime count:** for every rational prime $p$, a polarization with
   $D^2/2 = p$ automatically has elementary-divisor type $(1,p)$, isogeny
   degree $p^2$, self-intersection $2p$, and orbit count
   $$
   \boxed{\#\mathcal P_p(B) =
   \begin{cases}
     2, & p \equiv 1,4 \pmod 5, \\
     1, & p = 5, \\
     0, & p \equiv 2,3 \pmod 5.
   \end{cases}}
   \tag{P2}
   $$
3. **Full circle of rapidity-weighted generating series:** pullback by
   $\operatorname{Aut}(B,0)$ shifts the hyperbolic rapidity
   $t(\eta) = \tfrac{1}{2}\log(\sigma_1\eta/\sigma_2\eta)$ by $2nL$, defining
   the polarization-orbit circle $\mathbb R/(2L\mathbb Z)$ and the unitary
   Hecke characters $\Xi_m$ ($m \in \mathbb Z$) of finite conductor $\mathcal O_F$.
   For $\Re s > 1$, the all-type and primitive type-$(1,n)$ generating series
   are
   $$
   \boxed{
   \sum_{[D_\eta] \in \mathcal P(B)} e^{\pi i m t(\eta)/L} \left(\frac{D_\eta^2}{2}\right)^{-s}
   = L_F(s,\Xi_m), \qquad
   \sum_{\substack{[D_\eta] \in \mathcal P(B) \\ D_\eta \text{ of type }(1,n)}}
   e^{\pi i m t(\eta)/L} n^{-s}
   = \frac{L_F(s,\Xi_m)}{\zeta(2s)}.}
   \tag{P3}
   $$
4. **Exact integer census, logarithm-free sector decision, and uniform sector
   asymptotics (Section 8):** every polarization class $[D] \in \mathcal P(B)$
   has a unique representative $\eta = x + y\phi \in \mathcal O_F$ modulo
   $\phi^{2\mathbb Z}$ in the integer cone $x \ge 1,\ 0 \le y < x$, for which
   $t(\eta) \in [0, 2L)$ and $x^2 \le q(\eta) = x^2 + xy - y^2 \le \tfrac{5}{4}x^2$.
   For $M \ge 1$ equal sectors on $\theta(\eta) = t(\eta)/(2L) \in [0,1)$, the
   sector $k \in \{0,\dots,M-1\}$ is decided strictly in $\mathbb Z[\phi]$ via
   $\phi^{4k}(\eta')^M \le \eta^M < \phi^{4(k+1)}(\eta')^M$ where
   $\eta' = \sigma_2(\eta) = (x+y) - y\phi > 0$. For every arc $I \subset \mathbb R/\mathbb Z$
   of Haar measure $|I| \in [0,1]$ (including arcs crossing $0 \bmod 1$), the
   all-class and primitive type-$(1,n)$ sector counts up to reduced norm $X \ge 1$
   satisfy
   $$
   \boxed{
   A(X,I) = \frac{2L}{\sqrt 5}\,|I|\,X + O(\sqrt X + 1), \qquad
   A_{\mathrm{prim}}(X,I) = \frac{2L}{\sqrt 5\,\zeta(2)}\,|I|\,X + O\bigl(\sqrt X\log(2X)\bigr),}
   \tag{P3a}
   $$
   with absolute implied constants independent of $I$ and $X$.

---

## 2. Classical Sources and Arithmetic Inputs

1. **Analytic model of the Jacobian:** C. McMullen, *Complex Analysis on Riemann
   Surfaces* (Harvard Math 213b course notes), Section 14, Theorem 14.3,
   identifies $B = \operatorname{Jac}(y^2 = x^5 - 1)$ analytically with
   $\mathbb C^2/\Phi(\mathbb Z[\zeta])$ for the CM type $\Phi = \{\sigma_1,\sigma_2\}$,
   where $\sigma_a(\zeta) = \zeta^a$.
2. **Abelian variety and CM machinery:** B. Conrad, *Abelian varieties:
   geometry, parameter spaces, and arithmetic* (2005), Theorem 1.2.1 (faithful
   homology representation of origin-preserving maps), Theorem 1.3.1 (maximal
   CM field), Example 2.4.6 (kernel $\operatorname{Pic}^0(B)$ of
   $\mathscr L \mapsto \lambda_{\mathscr L}$), Theorem 3.1.3 (Riemann
   positivity and ampleness), Section 3.2 (symplectic elementary divisors),
   Theorem 3.3.10 (primitive CM types and full endomorphism algebra),
   Theorem 5.1.4 and Corollary 5.1.5 (Neron-Severi group and symmetric
   homomorphisms), and Lemma 5.2.1 (Riemann-Roch and degree).
3. **Registered arithmetic carrier facts for $F = \mathbb Q(\sqrt 5)$:**
   $$
   h_F = 1, \qquad
   \mathcal O_F^\times = \{\pm \phi^n : n \in \mathbb Z\}, \qquad
   N_{F/\mathbb Q}(\phi) = -1, \qquad
   \Delta_F = 5.
   \tag{P4}
   $$

---

## 3. Full Endomorphism Ring and Rosati Involution

The holomorphic differentials $\omega_1 = dx/y$ and $\omega_2 = x\,dx/y$ on $C$
satisfy $T^*\omega_1 = \zeta\omega_1$ and $T^*\omega_2 = \zeta^2\omega_2$.
The CM type of $(B, \mathcal O_K)$ is therefore $\Phi = \{1,2\}$.

Because the cyclic quartic field $K = \mathbb Q(\zeta)$ has $F = \mathbb Q(\sqrt 5)$
as its unique quadratic subfield, $K$ contains no proper CM subfield. Hence the
CM type $\Phi = \{1,2\}$ is primitive. Explicitly, under
$\operatorname{Gal}(K/\mathbb Q) = (\mathbb Z/5\mathbb Z)^\times$, the four
translates of $\{1,2\}$ are $\{1,2\}$, $\{2,4\}$, $\{3,1\}$, and $\{4,3\}$, so
its stabilizer is trivial. Writing any $\mathbb Q$-linear endomorphism of the
rank-one $K$-module $H_1(B,\mathbb Q)$ as $\sum_{g \in \operatorname{Gal}(K/\mathbb Q)} a_g g$
with $a_g \in K$, preservation of the Hodge summands forces $a_g = 0$ for all
$g \ne 1$. By Conrad's Theorem 3.3.10, $B$ is simple and
$\operatorname{End}_{\mathbb C}^0(B) = K$. Since $\operatorname{End}_{\mathbb C}(B)$
is an order in $K$ containing the maximal order $\mathcal O_K = \mathbb Z[\zeta]$,

$$
\boxed{\operatorname{End}_{\mathbb C}(B) = \mathcal O_K.}
\tag{P5}
$$

Because $\lambda_0$ is the canonical principal polarization of $\operatorname{Jac}(C)$
and $T$ comes from an automorphism of $C$, $T^\vee \lambda_0 T = \lambda_0$.
For the Rosati involution $u^\dagger = \lambda_0^{-1} u^\vee \lambda_0$, this
yields $T^\dagger = T^{-1} = \bar T$. Since $T$ generates $K$, the Rosati
involution on $\operatorname{End}_{\mathbb C}(B) = \mathcal O_K$ is complex
conjugation, and the ring of Rosati-symmetric integral endomorphisms is

$$
\boxed{\operatorname{End}_{\mathbb C}(B)^{\dagger = 1} = \mathcal O_K \cap F = \mathcal O_F.}
\tag{P6}
$$

---

## 4. Neron-Severi Group, Ample Cone, and Intersection Form

For a line bundle $\mathscr L$ on $B$, let $\lambda_{\mathscr L} : B \to B^\vee$
be its symmetric polarization homomorphism. Over $\mathbb C$, the kernel of
$\mathscr L \mapsto \lambda_{\mathscr L}$ is $\operatorname{Pic}^0(B)$, and
because $\lambda_0$ is an isomorphism ($d_1 = d_2 = 1$), composing with
$\lambda_0^{-1}$ gives an isomorphism of abelian groups (Conrad, Theorem 5.1.4):

$$
\operatorname{NS}(B) \xrightarrow{\sim} \mathcal O_F, \qquad
[\mathscr L] \longmapsto \eta = \lambda_0^{-1}\lambda_{\mathscr L}.
\tag{P7}
$$

Write $D_\eta \in \operatorname{NS}(B)$ for the class corresponding to
$\eta \in \mathcal O_F$, so $D_1 = [\lambda_0]$ is the principal polarization
class.

On the two-dimensional complex tangent space $\operatorname{Lie}(B)$, the
Rosati-symmetric endomorphism $\eta \in \mathcal O_F$ acts diagonally with real
eigenvalues $\sigma_1(\eta)$ and $\sigma_2(\eta)$. The Riemann Hermitian form
of $D_\eta$ is obtained from the positive-definite Hermitian form of $D_1$ by
inserting $\eta$. By the Riemann positivity criterion (Conrad, Theorem 3.1.3),

$$
\boxed{D_\eta \text{ is ample} \quad \Longleftrightarrow \quad
\eta \gg 0 \quad (\sigma_1(\eta) > 0 \text{ and } \sigma_2(\eta) > 0).}
\tag{P8}
$$

For $\eta \in \mathcal O_F$, multiplication by $\eta$ on the rank-four lattice
$H_1(B,\mathbb Z) \simeq \mathcal O_K$ has degree

$$
\deg(\lambda_0 \eta) = N_{K/\mathbb Q}(\eta) = N_{F/\mathbb Q}(\eta)^2.
$$

By Riemann-Roch on the abelian surface $B$ (Conrad, Lemma 5.2.1),
$\deg(\lambda_{\mathscr L}) = \chi(\mathscr L)^2$ with $\chi(\mathscr L) = D_\eta^2/2$,
and for ample $D_\eta$ we have $\chi(\mathscr L) > 0$ and $N_{F/\mathbb Q}(\eta) > 0$.
Therefore

$$
\boxed{D_\eta^2 = 2 N_{F/\mathbb Q}(\eta), \qquad
q(D_\eta) := \frac{D_\eta^2}{2} = N_{F/\mathbb Q}(\eta).}
\tag{P9}
$$

Because $\eta + n \gg 0$ for all sufficiently large integers $n$, polynomial
identity in $n$ extends $D_\eta^2 = 2 N_{F/\mathbb Q}(\eta)$ to all
$\eta \in \mathcal O_F$.

---

## 5. Automorphism Orbits and the Ideal Bijection

By (P5), origin-preserving holomorphic automorphisms of $B$ are

$$
\operatorname{Aut}(B,0) = \mathcal O_K^\times.
$$

For $u \in \mathcal O_K^\times$, functoriality $\lambda_{u^*\mathscr L} = u^\vee \lambda_{\mathscr L} u$
and $\lambda_0^{-1} u^\vee \lambda_0 = u^\dagger = \bar u$ give the pullback
action on $\operatorname{NS}(B)$:

$$
u^* D_\eta = D_{u\bar u \eta}.
\tag{P10}
$$

Here $u\bar u = N_{K/F}(u)$ lies in the group of totally positive units
$\mathcal O_F^{\times,+} = \{\phi^{2n} : n \in \mathbb Z\}$. Conversely, since
$\phi \in \mathcal O_F^\times \subset \mathcal O_K^\times$ satisfies
$N_{K/F}(\phi^n) = \phi^n \overline{\phi^n} = \phi^{2n}$ for every $n \in \mathbb Z$,

$$
\boxed{N_{K/F}(\mathcal O_K^\times) = \mathcal O_F^{\times,+} = \{\phi^{2n} : n \in \mathbb Z\}.}
\tag{P11}
$$

Now fix any integer $n \ge 1$ and consider the map

$$
\mathcal P_n^{\mathrm{all}}(B) \longrightarrow \{\mathfrak a \subset \mathcal O_F : N\mathfrak a = n\},
\qquad [D_\eta] \longmapsto (\eta).
\tag{P12}
$$

- **Well-defined and norm-preserving:** if $\eta \gg 0$ has $q(D_\eta) = n$,
  then $N_{F/\mathbb Q}(\eta) = n > 0$, so $N(\eta) = |N_{F/\mathbb Q}(\eta)| = n$.
  Pullback replaces $\eta$ by $u\bar u\eta$, which generates the same ideal $(\eta)$.
- **Injectivity:** if $(\eta') = (\eta)$ with $\eta, \eta' \gg 0$, then
  $\eta' = v\eta$ for a unit $v \in \mathcal O_F^\times$. Since both $\eta$ and
  $\eta'$ are totally positive, $v \in \mathcal O_F^{\times,+} = \{\phi^{2k}\}$.
  By (P11), $v = u\bar u$ for $u = \phi^k \in \mathcal O_K^\times$, so
  $D_{\eta'} = u^* D_\eta$.
- **Surjectivity:** let $\mathfrak a \subset \mathcal O_F$ be an integral ideal
  with $N\mathfrak a = n$. Because $h_F = 1$, $\mathfrak a = (\alpha)$ for some
  $\alpha \in \mathcal O_F \setminus \{0\}$. Since $\sigma_1(\phi) = \phi > 0$
  and $\sigma_2(\phi) = -\phi^{-1} < 0$, the four units $\{1, -1, \phi, -\phi\}$
  realize all four sign pairs $(\pm, \pm)$ under $(\sigma_1, \sigma_2)$. Thus
  there is a unit $w \in \{1, -1, \phi, -\phi\}$ such that $\eta = w\alpha \gg 0$
  (giving an explicit proof that the narrow class number is $h_F^+ = 1$). Then
  $(\eta) = \mathfrak a$ and $N_{F/\mathbb Q}(\eta) = |N_{F/\mathbb Q}(\eta)| = N\mathfrak a = n$,
  so $[D_\eta] \in \mathcal P_n^{\mathrm{all}}(B)$ maps to $\mathfrak a$.

This proves the bijection (P1) for every $n \ge 1$. When $n = p$ is a rational
prime, the elementary divisors $(d_1,d_2)$ satisfy $1 \le d_1 \mid d_2$ and
$d_1 d_2 = p$, forcing $(d_1,d_2) = (1,p)$. By the quadratic splitting law in
$F = \mathbb Q(\sqrt 5)$ ($\Delta_F = 5$), the number of integral ideals of norm
$p$ is $2$ when $\left(\frac{p}{5}\right) = +1$ ($p \equiv 1,4 \pmod 5$), $1$
when $p = 5$, and $0$ when $\left(\frac{p}{5}\right) = -1$ ($p \equiv 2,3 \pmod 5$).
At $p = 5$, the unique ramified prime ideal $(\sqrt 5)$ has the explicit totally
positive generator

$$
\eta_5 = \phi\sqrt 5 = 2 + \phi \gg 0, \qquad N_{F/\mathbb Q}(2+\phi) = 5.
\tag{P13}
$$

This completes the proof of (P2).

---

## 6. Polarization Rapidity Circle $\mathbb R/(2L\mathbb Z)$ and Coordinates

For $\eta \gg 0$ with $N_{F/\mathbb Q}(\eta) = n$, define its hyperbolic rapidity

$$
t(\eta) = \frac{1}{2}\log\frac{\sigma_1(\eta)}{\sigma_2(\eta)},
\qquad
(\sigma_1(\eta), \sigma_2(\eta)) = \bigl(\sqrt n\,e^{t(\eta)}, \sqrt n\,e^{-t(\eta)}\bigr).
$$

Under the pullback action $\eta \mapsto \phi^{2k}\eta$ of $\operatorname{Aut}(B,0)$,
$t(\phi^{2k}\eta) = t(\eta) + 2kL$. Therefore the natural circle indexing
polarization orbits is

$$
\mathbb R/(2L\mathbb Z).
\tag{P14}
$$

By contrast, the ideal rapidity $t(\alpha) = \tfrac{1}{2}\log|\sigma_1(\alpha)/\sigma_2(\alpha)|$
admits generators of either norm sign, including multiplication by $\phi$
(which has $N_{F/\mathbb Q}(\phi) = -1$ and shifts rapidity by $L$), and lives
on $\mathbb R/(L\mathbb Z)$. The two circles are linked by the degree-two
covering projection

$$
\pi : \mathbb R/(2L\mathbb Z) \longrightarrow \mathbb R/(L\mathbb Z), \qquad
[t]_{2L} \longmapsto [t]_L.
\tag{P15}
$$

Multiplication by $\phi$ reverses the sign of the norm form $N_{F/\mathbb Q}$
and maps the ample cone $\eta \gg 0$ outside itself; it is an anti-isometry of
the Neron-Severi Lorentz lattice, not a holomorphic automorphism pullback. At
the ramified prime $p = 5$, the totally positive generator $\eta_5 = 2 + \phi = \phi\sqrt 5$
has $\sigma_1(\eta_5)/\sigma_2(\eta_5) = \phi^2$, so

$$
t(\eta_5) = L \in \mathbb R/(2L\mathbb Z), \qquad
\pi(t(\eta_5)) = 0 \in \mathbb R/(L\mathbb Z).
$$

### 6.1 Exact $(a,b)$ and $(x,y)$ Coordinates, the Inverse-Different Seam, and the $J$-Pullback

In the public alternating pencil $\Omega_{(a,b)} = a\Omega_1 + b\Omega_2$ with
Pfaffian $a^2 - ab - b^2$, the Neron-Severi parameter is

$$
\eta = (a - b) + b\phi = x + y\phi, \qquad x = a - b, \quad y = b,
\tag{P16}
$$

so that

$$
N_{F/\mathbb Q}(\eta) = a^2 - ab - b^2 = x^2 + xy - y^2.
$$

**Comparison with the integral-homology calibration (`CM-ALTERNATING-PENCIL [T]`):**
On the rank-four lattice $\mathcal O_K = \mathbb Z[\zeta]$, with
$\lambda_1 = \zeta - \zeta^{-1},\ \lambda_2 = \zeta^2 - \zeta^{-2}$, and the
anti-real rank-one $\mathbb Z[\phi]$-lattice
$L = \{\lambda \in \mathcal O_K : \bar\lambda = -\lambda\} = \lambda_1\mathbb Z[\phi]$,
the divided trace pairing $\Omega_\lambda(u,v) = \frac{1}{5}\operatorname{Tr}_{K/\mathbb Q}(\lambda u\bar v)$
is already integral and alternating on $\mathcal O_K \times \mathcal O_K$, has
Pfaffian $\operatorname{Pf}(\Omega_{(a,b)}) = a^2 - ab - b^2 = N_{F/\mathbb Q}((a-b)+b\phi)$
for $\lambda = a\lambda_1 + b\lambda_2$, and is unimodular precisely on the Pell
unit orbit $(\lambda) = (\lambda_1)$ (`CM-ALTERNATING-PENCIL [T]`, where dividing
by $5$ cancels the inverse-different denominator of $\mathfrak d_{K/\mathbb Q}$).
In [`HODGE-TATE-CM5-INTEGRAL-HOMOLOGY-CALIBRATION-2026-09-11.md`](../HODGE-TATE-CM5-INTEGRAL-HOMOLOGY-CALIBRATION-2026-09-11.md),
the double-pentagon edge basis $(c_0,c_1,c_2,c_3)$ of $H_1(B,\mathbb Z) \simeq \mathcal O_K$
realizes the order-five automorphism $T_*$ as the companion matrix $M$ of
multiplication by $\zeta$ and the topological intersection pairing as
$W_c = \Omega_1 - \Omega_2 = \Omega_{(1,-1)} = J^*\Omega_1$ ($\operatorname{Pf}(W_c) = +1$).
Indeed, $1^2-1(-1)-(-1)^2=1$; the negative sign printed in the cited
calibration is a typographical error.
Passing to the unimodular integral basis $d_k = J^{-1}c_k$ via
$P = -(M + M^2) = J^{-1} \in \operatorname{GL}_4(\mathbb Z)$ ($\det P = 1$,
$P^{-1}MP = M$) removes the $J$-pullback and transforms the intersection pairing
into $P^\mathsf{T} W_c P = \Omega_1 = E_0$ (the unimodular principal polarization
$D_1 = [\lambda_0]$ of type $(1,1)$), while the general polarization form is
$E_\eta(u,v) = \Omega_1(\eta u,v) = \Omega_{(a,b)}(u,v)$ of Pfaffian
$N_{F/\mathbb Q}(\eta) = a^2 - ab - b^2 = x^2 + xy - y^2$. (By contrast, the
index-$5$ primary-lattice seam of `CM-ALTERNATING-PRIMARY-LATTICE-SEAM [T]` and
`CM-REAL-DIFFERENT-PRIMARY-SEAM [T]` lives inside the rank-six exterior square
$E_{\mathbb Z} = \operatorname{Alt}^2(\mathbb Z^4)$, where the direct sum
$H_{\mathbb Z} \oplus C_{\mathbb Z}$ of the rank-two CM pencil $H_{\mathbb Z}$
and the rank-four circular sector $C_{\mathbb Z}$ has index $5$ with quotient
$Q_{\mathrm{seam}} \simeq \mathfrak d_F^{-1}H_{\mathbb Z}/H_{\mathbb Z} \simeq \mathbb Z/5\mathbb Z$.)

The intersection Gram matrices of $D_\eta^2 = 2 N_{F/\mathbb Q}(\eta)$ in the
two integral bases are

$$
G_{a,b} = \begin{pmatrix} 2 & -1 \\ -1 & -2 \end{pmatrix}, \qquad
G_{x,y} = \begin{pmatrix} 2 & 1 \\ 1 & -2 \end{pmatrix}, \qquad
\det G_{a,b} = \det G_{x,y} = -5,
\tag{P17}
$$

of signature $(1,1)$. Since $J = 1 + \zeta^2 \in \mathcal O_K^\times$ has
relative norm $J\bar J = 2 - \phi = \phi^{-2}$, its pullback $J^* D_\eta = D_{(2-\phi)\eta}$
acts on the two coordinate systems by

$$
\begin{pmatrix} a' \\ b' \end{pmatrix}
= \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix}
  \begin{pmatrix} a \\ b \end{pmatrix},
\qquad
\begin{pmatrix} x' \\ y' \end{pmatrix}
= \begin{pmatrix} 2 & -1 \\ -1 & 1 \end{pmatrix}
  \begin{pmatrix} x \\ y \end{pmatrix},
\tag{P18}
$$

with characteristic polynomial $z^2 - 3z + 1$, eigenvalues $\phi^2, \phi^{-2}$,
and rapidity shift $t \mapsto t - 2L$ (hence trivial on $\mathbb R/(2L\mathbb Z)$).

---

## 7. Full Circle of Hecke Characters and Primitive Generating Series

For each $m \in \mathbb Z$, the character $\omega_m([D_\eta]) = \exp(\pi i m t(\eta)/L)$
on $\mathbb R/(2L\mathbb Z)$ transfers via (P1) to the unitary ideal character

$$
\boxed{
\Xi_m((\alpha))
= \operatorname{sgn}(N_{F/\mathbb Q}\alpha)^m
  \left|\frac{\sigma_1\alpha}{\sigma_2\alpha}\right|^{i\pi m/(2L)}
\qquad (\alpha \in F^\times).}
\tag{P19}
$$

Generator independence is immediate: replacing $\alpha$ by $\pm \phi^k \alpha$
multiplies $\operatorname{sgn}(N_{F/\mathbb Q}\alpha)^m$ by $(-1)^{mk}$ and
shifts $\tfrac{1}{2}\log|\sigma_1\alpha/\sigma_2\alpha|$ by $kL$, which also
multiplies $|\sigma_1\alpha/\sigma_2\alpha|^{i\pi m/(2L)}$ by $e^{\pi i m k} = (-1)^{mk}$;
their product is invariant. For $\eta \gg 0$, $\operatorname{sgn}(N_F\eta) = +1$
and $\Xi_m((\eta)) = e^{\pi i m t(\eta)/L}$. The even modes recover the
registered ideal-rapidity characters $\Xi_{2h} = \Psi_h$, while the odd modes
resolve the two sheets of $\mathbb R/(2L\mathbb Z) \to \mathbb R/(L\mathbb Z)$
and satisfy $\Xi_m((\sqrt 5)) = (-1)^m$.

Summing over all polarization orbits $[D] \in \mathcal P(B) = \bigsqcup_{n\ge 1}\mathcal P_n^{\mathrm{all}}(B)$
for $\Re s > 1$ gives the absolute-convergence identity

$$
Z_{B,m}^{\mathrm{pol}}(s)
:= \sum_{[D] \in \mathcal P(B)} \omega_m([D]) q(D)^{-s}
= \sum_{\mathfrak a \subset \mathcal O_F} \Xi_m(\mathfrak a) (N\mathfrak a)^{-s}
= L_F(s,\Xi_m),
\tag{P20}
$$

with $Z_{B,0}^{\mathrm{pol}}(s) = \zeta_F(s) = \zeta(s)L(s,\chi_5)$.

### 7.1 Primitive Classes and Type $(1,n)$ Polarizations

For $\eta = x + y\phi \in \mathcal O_F \setminus \{0\}$, define its positive
integral content $c(\eta) = \gcd(x,y) = \gcd(a,b) \ge 1$. In any integral
homology basis of $H_1(B,\mathbb Z)$, the alternating Riemann matrix of $D_1$
is unimodular ($E_0 \in \operatorname{GL}_4(\mathbb Z)$), and the alternating
matrix of $D_\eta$ is $E_\eta = E_0 M_\eta$, where $M_\eta$ is the integral
matrix of multiplication by $\eta$. Because $E_0$ is unimodular, an integer
$c \ge 1$ divides $E_\eta$ in $M_4(\mathbb Z)$ if and only if $c$ divides
$M_\eta$, which by (P5)-(P6) holds if and only if $\eta/c \in \mathcal O_F$.
Since the first elementary divisor $d_1(D_\eta)$ of $E_\eta$ (with $d_1 \mid d_2$)
is the greatest common divisor of its entries (Conrad, Section 3.2) and
$\operatorname{Pf}(E_\eta) = d_1(D_\eta)d_2(D_\eta) = q(D_\eta) = N_{F/\mathbb Q}(\eta)$,

$$
\boxed{d_1(D_\eta) = c(\eta) = \gcd(x,y), \qquad
(d_1(D_\eta), d_2(D_\eta)) = \bigl(c(\eta),\, N_{F/\mathbb Q}(\eta)/c(\eta)\bigr).}
\tag{P21}
$$

In particular, $D_\eta$ has type $(1,n)$ if and only if $\eta \gg 0$ is
primitive ($c(\eta) = 1$) with $N_{F/\mathbb Q}(\eta) = n$. Every ample class
decomposes uniquely as $D_\eta = c D_{\eta_0}$ with $c = c(\eta) \ge 1$ and
$\eta_0 = \eta/c$ primitive and totally positive; under this decomposition
$q(D_\eta) = c^2 q(D_{\eta_0})$ and $\omega_m([D_\eta]) = \omega_m([D_{\eta_0}])$
(equivalently $\Xi_m((c)) = 1$). Factoring out $\sum_{c\ge 1} (c^2)^{-s} = \zeta(2s)$
on $\Re s > 1$ proves the second identity in (P3):

$$
Z_{B,m}^{\mathrm{prim}}(s)
:= \sum_{\substack{[D] \in \mathcal P(B) \\ D \text{ primitive}}} \omega_m([D]) q(D)^{-s}
= \frac{L_F(s,\Xi_m)}{\zeta(2s)}.
\tag{P22}
$$

Comparing local Euler factors of $L_F(s,\Xi_m)/\zeta(2s)$ at $T = p^{-s}$ and
$z_p = \Xi_m(\mathfrak p)$ gives:

| Rational prime $p$ | Mode-$m$ factor of $L_F(s,\Xi_m)$ | Mode-$m$ primitive factor of $L_F(s,\Xi_m)/\zeta(2s)$ | Unweighted count $\rho_F(p^k)$ of type $(1,p^k)$ |
|---|---|---|---|
| Split, $\chi_5(p) = +1$ | $[(1 - z_p T)(1 - z_p^{-1}T)]^{-1}$ | $(1 - T^2)/[(1 - z_p T)(1 - z_p^{-1}T)] = 1 + \sum_{k\ge 1}(z_p^k + z_p^{-k})T^k$ | $2$ for all $k \ge 1$ |
| Inert, $\chi_5(p) = -1$ | $(1 - T^2)^{-1}$ | $1$ | $0$ for all $k \ge 1$ |
| Ramified, $p = 5$ | $(1 - (-1)^m T)^{-1}$ | $1 + (-1)^m T$ | $1$ for $k = 1$, and $0$ for $k \ge 2$ |

By multiplicativity, the number $\rho_F(n)$ of type-$(1,n)$ polarization orbits
on $B$ is

$$
\boxed{
\rho_F(n) = \sum_{c^2 \mid n} \mu(c) a_F(n/c^2)
= \begin{cases}
  2^{\omega_{\mathrm{split}}(n)}, & \text{if } v_5(n) \le 1 \text{ and every prime } p \mid n \text{ with } p \ne 5 \text{ splits in } F, \\
  0, & \text{otherwise.}
\end{cases}}
\tag{P23}
$$

In particular, at an inert prime $p$, the unique polarization orbit of reduced
self-intersection $p^2$ is $[p D_1]$ of type $(p,p)$; there is no polarization
of type $(1,p^2)$.

---

## 8. Exact Integer Census, Logarithm-Free Sector Decision, and Uniform Sector Asymptotics

This section establishes the explicit integer coordinate census of all
polarization classes $[D_\eta] \in \mathcal P(B)$ up to any norm bound $X \ge 1$,
an exact logarithm-free algorithm for sector classification on
$\mathbb R/(2L\mathbb Z)$, and uniform asymptotics for all-class and primitive
type-$(1,n)$ polarizations in arbitrary arcs $I \subset \mathbb R/\mathbb Z$.

### 8.1 Unique Fundamental-Cone Representative and Excluded Boundary $y = x$

Write every element of $\mathcal O_F = \mathbb Z[\phi]$ uniquely as
$\eta = x + y\phi$ with $x,y \in \mathbb Z$, and denote its Galois conjugate by
$\eta' = \sigma_2(\eta) = x - y\phi^{-1} = (x+y) - y\phi$.

**Theorem 8.1 (Unique reduced representative in the integer cone).**
*Every $\operatorname{Aut}(B,0)$-orbit in $\mathcal O_F^+ / \phi^{2\mathbb Z}$
contains a unique representative $\eta = x + y\phi$ in the integer cone*

$$
\boxed{
\mathcal C := \bigl\{\eta = x + y\phi \in \mathbb Z[\phi] : x \in \mathbb Z,\ y \in \mathbb Z,\ x > 0,\ 0 \le y < x\bigr\},}
\tag{P24}
$$

*and for $\eta = x + y\phi \in \mathbb Z[\phi]$ one has the exact equivalence*

$$
\bigl(\eta \gg 0 \text{ and } t(\eta) \in [0,2L)\bigr)
\quad \Longleftrightarrow \quad
\bigl(x > 0 \text{ and } 0 \le y < x\bigr).
\tag{P25}
$$

*Proof.* Multiplication by $\phi^{2k}$ ($k \in \mathbb Z$) preserves total
positivity and shifts $t(\eta) = \tfrac{1}{2}\log(\sigma_1\eta/\sigma_2\eta)$
by $t(\phi^{2k}\eta) = t(\eta) + 2kL$. Hence every orbit in
$\mathcal O_F^+/\phi^{2\mathbb Z}$ has a unique representative $\eta \gg 0$
with $t(\eta) \in [0,2L)$, namely for $k = -\lfloor t(\eta_0)/(2L)\rfloor$.
Since $\eta' = \sigma_2(\eta) > 0$ for $\eta \gg 0$ and $\log$ is strictly
increasing on $(0,\infty)$,

$$
0 \le t(\eta) < 2L
\iff 1 \le \frac{\sigma_1(\eta)}{\sigma_2(\eta)} < e^{4L} = \phi^4
\iff \eta' \le \eta < \phi^4 \eta'.
$$

In $\mathbb Z[\phi]$, $\phi - (-\phi^{-1}) = \sqrt 5$, while
$\phi^4 = 3\phi + 2$ and $\phi^4(-\phi^{-1}) = -\phi^3 = -(2\phi + 1)$ give
$\phi^4 - 1 = 3\phi + 1 = \phi^3 + \phi$ and
$\phi^4(-\phi^{-1}) - \phi = -3\phi - 1 = -(\phi^3 + \phi)$. Therefore we
obtain the two exact algebraic factorizations

$$
\boxed{
\eta - \eta' = (\phi + \phi^{-1})y = \sqrt 5\,y, \qquad
\phi^4\eta' - \eta = (\phi^3 + \phi)(x - y) = \phi^2\sqrt 5\,(x - y).}
\tag{P26}
$$

If $\eta \gg 0$ and $0 \le t(\eta) < 2L$, then $\eta - \eta' \ge 0$ forces
$y \ge 0$, $\phi^4\eta' - \eta > 0$ forces $x - y > 0$, and thus
$x > y \ge 0$, so $x \ge 1$. Conversely, if $x > 0$ and $0 \le y < x$, then
$\sigma_1(\eta) = x + y\phi \ge x > 0$, $\sigma_2(\eta) = (x - y) + y(1 - \phi^{-1}) \ge 1 > 0$,
and (P26) gives $\eta - \eta' \ge 0$ and $\phi^4\eta' - \eta > 0$, so
$\eta \gg 0$ and $t(\eta) \in [0,2L)$.

**Why the upper boundary $y = x$ is excluded:** at $y = x > 0$, the identity
$1 + \phi = \phi^2$ yields

$$
\eta\big|_{y=x} = x(1 + \phi) = x\phi^2 = \phi^2(x + 0\cdot\phi),
\qquad t(x\phi^2) = 2L \equiv 0 \pmod{2L}.
\tag{P27}
$$

Thus $(x,x)$ lies in the same $\operatorname{Aut}(B,0)$-orbit as the lower
boundary point $(x,0)$ (pullback by $(J^{-1})^*$) and sits at the upper endpoint
$2L$ of $[0,2L)$. Including $y = x$ would list every scalar class $[x D_1]$
twice. $\square$

### 8.2 Norm Form Bounds and Finite Exhaustive Box up to Norm $X$

**Theorem 8.2 (Norm sandwich and finite census box).**
*For every $\eta = x + y\phi \in \mathcal C$ ($x \ge 1,\ 0 \le y < x$), the
reduced polarization norm $q(\eta) = N_{F/\mathbb Q}(\eta)$ satisfies*

$$
\boxed{
q(x,y) = x^2 + xy - y^2 = \frac{5}{4}x^2 - \left(y - \frac{x}{2}\right)^2,
\qquad x^2 \le q(x,y) \le \frac{5}{4}x^2.}
\tag{P28}
$$

*Consequently, for any real $X \ge 1$, the set of all polarization orbits with
$q(D) \le X$ is enumerated without omission or duplication by the finite box*

$$
\boxed{
\mathcal C(X)
= \bigl\{(x,y) \in \mathbb Z^2 : 1 \le x \le \lfloor\sqrt X\rfloor,\ 0 \le y < x,\ x^2 + xy - y^2 \le X\bigr\}.}
\tag{P29}
$$

*Proof.* Since $\phi^2 = \phi + 1$, we have $\operatorname{Tr}_{F/\mathbb Q}(\phi) = 1$
and $N_{F/\mathbb Q}(\phi) = -1$, so $q(x,y) = (x+y\phi)(x+y\sigma_2\phi) = x^2 + xy - y^2$.
For $0 \le y < x$, $y(x - y) \ge 0$ gives $q(x,y) = x^2 + y(x - y) \ge x^2$
(with equality if and only if $y = 0$), and completing the square gives
$q(x,y) = \tfrac{5}{4}x^2 - (y - x/2)^2 \le \tfrac{5}{4}x^2$ (attained when
$2\mid x$ and $y = x/2$, where $q(2m,m) = 5m^2$). If $(x,y) \in \mathcal C$
has $q(x,y) \le X$, then $x^2 \le q(x,y) \le X$ forces $1 \le x \le \lfloor\sqrt X\rfloor$.
By Theorem 8.1 and the bijection (P1), $\mathcal C(X)$ lists every polarization
class of reduced norm $\le X$ once and only once. $\square$

### 8.3 Exact Logarithm-Free Sector Decision and Galois Mirror Involution

Normalize the polarization circle $\mathbb R/(2L\mathbb Z)$ to unit Haar
measure via $\theta(\eta) := t(\eta)/(2L) \in [0,1)$ for $\eta \in \mathcal C$.
For an integer $M \ge 1$, partition $[0,1)$ into $M$ equal half-open sectors
$S_k = [k/M, (k+1)/M)$ ($k = 0,1,\dots,M-1$).

**Theorem 8.3 (Exact sector decision in $\mathbb Z[\phi]$).**
*For $\eta = x + y\phi \in \mathcal C$, let $\eta' = \sigma_2(\eta) = (x+y) - y\phi > 0$.
For each $k \in \{0,1,\dots,M-1\}$,*

$$
\boxed{
\theta(\eta) \in \left[\frac{k}{M}, \frac{k+1}{M}\right)
\quad \Longleftrightarrow \quad
\phi^{4k}(\eta')^M \le \eta^M < \phi^{4(k+1)}(\eta')^M.}
\tag{P30}
$$

*Every comparison in (P30) is decided purely in $\mathbb Z^2$ with zero
floating-point or logarithm evaluation: writing any difference in $\mathbb Z[\phi]$
as $\delta = A + B\phi$ ($A,B \in \mathbb Z$), one has $2\sigma_1(\delta) = (2A+B) + B\sqrt 5$,
so*

$$
\boxed{
A + B\phi \ge 0 \iff
\begin{cases}
  2A + B \ge 0, & \text{if } (2A+B)^2 \ge 5B^2, \\
  B > 0, & \text{if } (2A+B)^2 < 5B^2.
\end{cases}}
\tag{P31}
$$

*Moreover, for every $n \ge 0$, $\phi^n = F_{n-1} + F_n\phi$ ($F_0 = 0, F_1 = 1$),
and multiplication in $\mathbb Z[\phi]$ obeys $(a_1 + b_1\phi)(a_2 + b_2\phi) = (a_1 a_2 + b_1 b_2) + (a_1 b_2 + b_1 a_2 + b_1 b_2)\phi$.*

*Proof.* Since $\eta > 0$ and $\eta' > 0$, $\theta(\eta) = \frac{1}{4L}\log(\eta/\eta')$.
Multiplying $k/M \le \theta(\eta) < (k+1)/M$ by $4ML > 0$, exponentiating with
$e^{4L} = \phi^4$, and multiplying by $(\eta')^M > 0$ gives (P30). Because
$5$ is not a rational square, $(2A+B)^2 = 5B^2$ holds only at $A = B = 0$, so
comparing $(2A+B)^2$ against $5B^2$ in $\mathbb Z$ determines the exact sign of
$(2A+B) + B\sqrt 5$. $\square$

**Proposition 8.4 (Exact Galois mirror involution on the interior of $\mathcal C$).**
*For $\eta = x + y\phi \in \mathcal C$ with $0 < y < x$, its Galois conjugate
$\sigma_2(\eta) = (x+y) - y\phi \gg 0$ has reduced representative*

$$
\boxed{
\widetilde\eta := \phi^2\sigma_2(\eta) = x + (x - y)\phi \in \mathcal C,
\qquad q(x, x-y) = q(x,y), \qquad
\gcd(x, x-y) = \gcd(x,y), \qquad
\theta(\widetilde\eta) = 1 - \theta(\eta).}
\tag{P32}
$$

*Its fixed locus in $0 < y < x$ is the ray $x = 2y$ ($y \ge 1$), where
$\eta = y(2+\phi) = y\phi\sqrt 5$, $q(2y,y) = 5y^2$, and $\theta(2y,y) = 1/2$
($t = L$). Consequently, for any even sector count $M \ge 4$, the involution
$(x,y) \leftrightarrow (x,x-y)$ pairs $S_k$ bijectively with $S_{M-1-k}$ for
$1 \le k \le M/2 - 2$, while accounting for the ray $y = 0$ ($\theta = 0 \in S_0$)
and the ramified ray $x = 2y$ ($\theta = 1/2 \in S_{M/2}$) gives for every $X \ge 1$
the exact finite-X identities:*

$$
\boxed{
\begin{aligned}
A(X, S_k) &= A(X, S_{M-1-k}), &
A_{\mathrm{prim}}(X, S_k) &= A_{\mathrm{prim}}(X, S_{M-1-k})
\quad (1 \le k \le M/2 - 2), \\
A(X, S_0) - A(X, S_{M-1}) &= \lfloor\sqrt X\rfloor, &
A_{\mathrm{prim}}(X, S_0) - A_{\mathrm{prim}}(X, S_{M-1}) &= 1, \\
A(X, S_{M/2}) - A(X, S_{M/2-1}) &= \lfloor\sqrt{X/5}\rfloor, &
A_{\mathrm{prim}}(X, S_{M/2}) - A_{\mathrm{prim}}(X, S_{M/2-1}) &= \mathbf 1_{X \ge 5}.
\end{aligned}}
\tag{P33}
$$

### 8.4 Uniform Sector Asymptotics for All Classes and Primitive Classes

Let $I \subset \mathbb R/\mathbb Z$ be any arc (connected interval on the circle,
open, half-open, or closed, including wrap-around arcs crossing $0 \bmod 1$) of
normalized Haar measure $|I| \in [0,1]$, corresponding to an arc of length
$2L\,|I|$ on $\mathbb R/(2L\mathbb Z)$. Define

$$
A(X,I) := \#\bigl\{(x,y) \in \mathcal C(X) : \theta(x,y) \in I \pmod 1\bigr\},
\qquad
A_{\mathrm{prim}}(X,I) := \#\bigl\{(x,y) \in \mathcal C(X) : \gcd(x,y) = 1,\ \theta(x,y) \in I \pmod 1\bigr\}.
$$

**Theorem 8.5 (Uniform sector asymptotics across all norms and primitive norms).**
*For every real $X \ge 1$ and every arc $I \subset \mathbb R/\mathbb Z$ of Haar
measure $|I| \in [0,1]$,*

$$
\boxed{
A(X,I) = \frac{2L}{\sqrt 5}\,|I|\,X + O(\sqrt X + 1),
\qquad
A_{\mathrm{prim}}(X,I)
= \frac{2L}{\sqrt 5\,\zeta(2)}\,|I|\,X + O\bigl(\sqrt X\log(2X)\bigr),}
\tag{P34}
$$

*where $\zeta(2) = \pi^2/6$, $\frac{2L}{\sqrt 5} = \frac{2\log\phi}{\sqrt 5} \approx 0.43040894$,
$\frac{2L}{\sqrt 5\,\zeta(2)} = \frac{12\log\phi}{\pi^2\sqrt 5} \approx 0.26165734$,
and the implied $O$-constants are absolute (independent of both $X$ and $I$).*

*Proof.*
1. **Wrap-around reduction to subintervals of $[0,1)$:** If $I \subset \mathbb R/\mathbb Z$
   does not cross $0 \bmod 1$, it lifts to a single subinterval $I_1 \subset [0,1)$
   with $|I_1| = |I|$. If $I$ crosses $0 \bmod 1$, it splits into two disjoint
   subintervals $I_1 = [\alpha, 1)$ and $I_2 = [0, \beta)$ of $[0,1)$ with
   $|I_1| + |I_2| = |I|$. By additivity of $A(X,\cdot)$, $A_{\mathrm{prim}}(X,\cdot)$,
   and $|\cdot|$ (at the cost of doubling the absolute implied error constant),
   it suffices to prove (P34) for a single interval $I \subset [0,1)$ with
   endpoints $0 \le \alpha \le \beta \le 1$ and $|I| = \beta - \alpha$.
2. **Volume and Jacobian in $(x,y)$-coordinates:** Embed $\mathcal O_F$ into
   $\mathbb R^2$ by $(u,v) = (\sigma_1\eta, \sigma_2\eta) = (x + y\phi, x - y\phi^{-1})$.
   The transformation determinant is
   $$
   \det\frac{\partial(u,v)}{\partial(x,y)}
   = \det\begin{pmatrix} 1 & \phi \\ 1 & -\phi^{-1} \end{pmatrix}
   = -(\phi + \phi^{-1}) = -\sqrt 5,
   $$
   so $\mathbb Z^2$ in $(x,y)$-coordinates has covolume $1$ while the image
   lattice $\Lambda = (\sigma_1,\sigma_2)(\mathcal O_F)$ has covolume $\sqrt 5$.
   In hyperbolic polar coordinates $u = \sqrt q\,e^{2L\theta},\ v = \sqrt q\,e^{-2L\theta}$
   ($0 < q \le X,\ \alpha \le \theta \le \beta$), the Jacobian with respect to
   $(q,\theta)$ is
   $$
   \det\frac{\partial(u,v)}{\partial(q,\theta)}
   = \det\begin{pmatrix}
       \frac{1}{2\sqrt q} e^{2L\theta} & 2L\sqrt q\,e^{2L\theta} \\
       \frac{1}{2\sqrt q} e^{-2L\theta} & -2L\sqrt q\,e^{-2L\theta}
     \end{pmatrix}
   = -2L.
   $$
   Therefore the Euclidean area of $\Omega(X,I) := \{(x,y) \in \mathbb R^2 : x > 0,\ 0 \le y < x,\ q(x,y) \le X,\ \theta(x,y) \in I\}$
   in the $(x,y)$-plane is
   $$
   \operatorname{Area}_{x,y}(\Omega(X,I))
   = \frac{1}{\sqrt 5}\operatorname{Area}_{u,v}(\Omega(X,I))
   = \frac{1}{\sqrt 5}\int_{\alpha}^{\beta}\int_0^X 2L\,dq\,d\theta
   = \frac{2L}{\sqrt 5}\,|I|\,X.
   \tag{P35}
   $$
3. **Uniform Davenport boundary estimate:** Because $\Omega(X,I) = \sqrt X\,\Omega(1,I)$
   is homothetic to $\Omega(1,I) \subset [0,1] \times [0,1]$, along the upper
   hyperbolic arc $q(x,y) = 1$ parametrized by $\theta \in [0,1]$ one has
   $$
   x(\theta) = \frac{e^{2L\theta}\phi^{-1} + e^{-2L\theta}\phi}{\sqrt 5}
   = \frac{2}{\sqrt 5}\cosh(2L\theta - L), \qquad
   y(\theta) = \frac{e^{2L\theta} - e^{-2L\theta}}{\sqrt 5}
   = \frac{2}{\sqrt 5}\sinh(2L\theta).
   $$
   Each coordinate is monotone on $[0, 1/2]$ and on $[1/2, 1]$, so splitting $I$
   at $1/2$ expresses $\Omega(X,I)$ as the union of at most two regions whose
   boundaries consist of two straight segments through the origin and one
   monotone hyperbolic arc inside $[0,\sqrt X]^2$. Every horizontal or vertical
   line meets each piece in at most one interval, and the projections on both
   axes have length $\le \sqrt X$. By Davenport's lattice-point theorem (1951),
   $$
   \bigl|A(X,I) - \operatorname{Area}_{x,y}(\Omega(X,I))\bigr|
   \le 4\sqrt X + 2 = O(\sqrt X + 1)
   \tag{P36}
   $$
   uniformly in $I \subset [0,1)$ (with the same $O(\sqrt X + 1)$ bound whether
    the endpoints $\alpha,\beta$ are open or closed, since any ray $x\sin\psi = y\cos\psi$
   in $[0,\sqrt X]^2$ contains at most $\lfloor\sqrt X\rfloor$ integer points).
4. **Complete Mobius inversion and tail bound for $A_{\mathrm{prim}}(X,I)$:**
   For every integer $c \ge 1$, scaling $(x,y) = c(x_0,y_0)$ satisfies
   $q(cx_0,cy_0) = c^2 q(x_0,y_0)$ and $\theta(cx_0,cy_0) = \theta(x_0,y_0)$.
   Since $q(x,y) \ge x^2 \ge c^2$ whenever $c \mid \gcd(x,y)$, only
   $1 \le c \le C := \lfloor\sqrt X\rfloor$ can contribute, and Mobius inversion
   $\mathbf 1_{\gcd(x,y)=1} = \sum_{c\mid\gcd(x,y)}\mu(c)$ is a finite exact identity:
   $$
   A_{\mathrm{prim}}(X,I) = \sum_{c=1}^{\lfloor\sqrt X\rfloor} \mu(c)\,A(X/c^2, I).
   \tag{P37}
   $$
   Substituting $A(X/c^2,I) = \frac{2L}{\sqrt 5}|I|\frac{X}{c^2} + R(X/c^2,I)$
   with $|R(Y,I)| \le K_0(\sqrt Y + 1)$ for $Y \ge 1$ gives
   $$
   A_{\mathrm{prim}}(X,I)
   = \frac{2L}{\sqrt 5}\,|I|\,X \sum_{c=1}^{\lfloor\sqrt X\rfloor} \frac{\mu(c)}{c^2}
     + \sum_{c=1}^{\lfloor\sqrt X\rfloor} \mu(c)\,R(X/c^2, I).
   $$
   The infinite Mobius tail is bounded uniformly in $I$ by
   $$
   \left|\sum_{c > \lfloor\sqrt X\rfloor} \frac{\mu(c)}{c^2}\right|
   \le \sum_{c = \lfloor\sqrt X\rfloor + 1}^{\infty} \frac{1}{c(c-1)}
   = \frac{1}{\lfloor\sqrt X\rfloor} \le \frac{2}{\sqrt X},
   \qquad
   \frac{2L}{\sqrt 5}\,|I|\,X \left|\sum_{c > \lfloor\sqrt X\rfloor} \frac{\mu(c)}{c^2}\right|
   \le \frac{4L}{\sqrt 5}\sqrt X,
   \tag{P38}
   $$
   and the summed error term is bounded uniformly in $I$ by
   $$
   \sum_{c=1}^{\lfloor\sqrt X\rfloor} \bigl|R(X/c^2, I)\bigr|
   \le K_0 \sum_{c=1}^{\lfloor\sqrt X\rfloor} \left(\frac{\sqrt X}{c} + 1\right)
   \le K_0\Bigl(\sqrt X\bigl(1 + \log\sqrt X\bigr) + \sqrt X\Bigr)
   \ll \sqrt X\log(2X).
   \tag{P39}
   $$
   Since $\sum_{c=1}^\infty \mu(c)c^{-2} = 1/\zeta(2) = 6/\pi^2$, combining
   (P37)-(P39) proves (P34). $\square$

### 8.5 Explicit Scope Boundaries and Non-Claims

1. **All-norm and primitive-norm geometry vs. prime-norm sector counts:**
   Theorems 8.1-8.5 are unconditional geometry-of-numbers statements for all
   integral polarization classes ($A(X,I)$) and primitive type-$(1,n)$ classes
   ($A_{\mathrm{prim}}(X,I)$). They do **not** by themselves establish a prime
   number theorem in sectors; prime-norm sector estimates require the Hecke
   $L$-functions $L_F(s,\Xi_m)$ and the analytic machinery of
   [`HECKE_MAASS_BRIDGE.md`](HECKE_MAASS_BRIDGE.md).
2. **Full Neron-Severi cone vs. endomorphism-pullback reachability $f^*\lambda_0$:**
   Every totally positive $\eta \in \mathcal O_F^+$ defines an ample polarization
   isogeny $\lambda_\eta = \lambda_0\eta : B \to B^\vee$ of reduced norm
   $q(\eta) = N_{F/\mathbb Q}(\eta)$. Whether $\lambda_\eta$ is further
   realizable as an endomorphism pullback $f^*\lambda_0 = f^\vee\lambda_0 f = \lambda_0(f\bar f)$
   for some $f \in \mathcal O_K$ is equivalent to $\eta \in N_{K/F}(\mathcal O_K)$,
   a distinct relative-norm condition not claimed in Theorem 8.2 or Theorem 8.5.
3. **No operator or Markov transition claim:** The polarization census and
   sector asymptotics do not define transition probabilities between sectors or
   derive the native operator $U$. Also, $Z_{B,m}^{\mathrm{pol}}(s)$ and
   $Z_{B,m}^{\mathrm{prim}}(s)$ are generating functions of polarization classes
   on $B$ with respect to ideal multiplication, not the Hasse-Weil $L$-function
   of $B$.

