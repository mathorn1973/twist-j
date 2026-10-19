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

By contrast, the ideal rapidity $\eta(\alpha) = \tfrac{1}{2}\log|\sigma_1(\alpha)/\sigma_2(\alpha)|$
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

### 6.1 Exact $(a,b)$ and $(x,y)$ Coordinates and the $J$-Pullback

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
is the greatest common divisor of its entries (Conrad, Section 3.2),

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
( equivalently $\Xi_m((c)) = 1$). Factoring out $\sum_{c\ge 1} (c^2)^{-s} = \zeta(2s)$
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
of type $(1,p^2)$. Note finally that $Z_{B,m}^{\mathrm{pol}}(s)$ and
$Z_{B,m}^{\mathrm{prim}}(s)$ are generating functions of polarization classes
on $B$ with respect to ideal multiplication (composition of commuting
Rosati-symmetric endomorphisms), not the Hasse-Weil $L$-function of $B$.
