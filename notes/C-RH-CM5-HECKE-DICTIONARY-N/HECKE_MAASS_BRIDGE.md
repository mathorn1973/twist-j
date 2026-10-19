# Real-Quadratic Hecke-Maass Dictionary, Integral Mobius Quotient, and Sector Bounds

```text
STATUS:                  NON-CANONICAL / PROOF-ONLY CLASSICAL DICTIONARY
AUTHORITY:               Public Canon v103 (dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d)
CANON / REGISTRY CHANGE: NONE
LICENSE:                 Apache-2.0 (A. M. Thorn)
```

This document consolidates and proves the analytic and automorphic dictionary
for the real-quadratic carrier $F = \mathbb Q(\sqrt 5)$ attached to
$J = 1 + \zeta_5^2$, extending Section 7 of
[`notes/C-J-RAPIDITY-GALOIS-EQUIVARIANT-PRIME-SHELL-N/README.md`](../C-J-RAPIDITY-GALOIS-EQUIVARIANT-PRIME-SHELL-N/README.md)
and connecting directly to the polarization generating series in
[`CM5_POLARIZATIONS.md`](CM5_POLARIZATIONS.md).

---

## 1. Complete Hecke Character Family $\Xi_m$ (Even and Odd Modes)

Let

$$
F = \mathbb Q(\sqrt 5), \qquad \mathcal O_F = \mathbb Z[\phi], \qquad
\phi = \frac{1+\sqrt 5}{2}, \qquad L = \log\phi,
$$

with real embeddings $\sigma_1(\phi) = \phi$ and $\sigma_2(\phi) = -\phi^{-1}$.
For $\alpha \in F^\times$ and $m \in \mathbb Z$, set

$$
t(\alpha) = \frac{1}{2}\log\left|\frac{\sigma_1(\alpha)}{\sigma_2(\alpha)}\right|,
\qquad
\mu_m = \frac{\pi m}{2L},
\qquad
\epsilon_m = m \bmod 2 \in \{0,1\}.
\tag{A1}
$$

(Earlier ideal-rapidity notes write $\eta(\alpha)$ for $t(\alpha)$; here we write $t(\alpha)$ so that $\eta = x + y\phi \in \mathcal O_F$ is reserved unambiguously for Neron-Severi classes.) As established geometrically on the polarization circle $\mathbb R/(2L\mathbb Z)$ in [`CM5_POLARIZATIONS.md`](CM5_POLARIZATIONS.md), define on principal fractional ideals $(\alpha)$:

$$
\boxed{
\Xi_m((\alpha))
= \operatorname{sgn}(N_{F/\mathbb Q}\alpha)^{\epsilon_m}
  \exp\left(\frac{\pi i m t(\alpha)}{L}\right)
= \operatorname{sgn}(N_{F/\mathbb Q}\alpha)^{\epsilon_m}
  \left|\frac{\sigma_1(\alpha)}{\sigma_2(\alpha)}\right|^{i\mu_m}.}
\tag{A2}
$$

When $m = 2h$ is even ($\epsilon_{2h} = 0$), $\mu_{2h} = \tau_h := \pi h / L$, the
norm-sign factor is $+1$, and $\Xi_{2h}$ coincides with the registered
ideal-rapidity character lift

$$
\Psi_h((\alpha)) = \Xi_{2h}((\alpha))
= \exp\left(\frac{2\pi i h t(\alpha)}{L}\right)
= \left|\frac{\sigma_1(\alpha)}{\sigma_2(\alpha)}\right|^{i\tau_h}.
\tag{A3}
$$

### 1.1 Unit Invariance, Idelic Normalization, Completeness, and Infinite Order

1. **Unit invariance for all $m \in \mathbb Z$:** every unit of $\mathcal O_F$
   has the form $u = \pm \phi^k$ ($k \in \mathbb Z$), with
   $N_{F/\mathbb Q}(u) = (-1)^k$ and $t(u) = kL$. Thus
   $$
   \operatorname{sgn}(N_{F/\mathbb Q}(u\alpha))^{\epsilon_m}
   = (-1)^{mk}\operatorname{sgn}(N_{F/\mathbb Q}\alpha)^{\epsilon_m},
   \qquad
   e^{\pi i m t(u\alpha)/L} = e^{\pi i m k} e^{\pi i m t(\alpha)/L}
   = (-1)^{mk} e^{\pi i m t(\alpha)/L}.
   $$
   The two $(-1)^{mk}$ factors cancel for both even and odd $m$, so $\Xi_m$ is
   a well-defined unitary character on the group of fractional ideals of $F$.
2. **Global idelic Hecke character, conductor, and family completeness:** at each
   finite prime ideal $\mathfrak p$ of $\mathcal O_F$, define the unramified local
   character $\widetilde\Xi_{m,\mathfrak p}(x) = \Xi_m(\mathfrak p)^{v_{\mathfrak p}(x)}$,
   which is trivial on $\mathcal O_{F,\mathfrak p}^\times$. At the two real
   places $(x_1,x_2) \in \mathbb R^\times \times \mathbb R^\times$, set
   $\widetilde\Xi_{m,1}(x_1) = \operatorname{sgn}(x_1)^{\epsilon_m}|x_1|^{-i\mu_m}$
   and $\widetilde\Xi_{m,2}(x_2) = \operatorname{sgn}(x_2)^{\epsilon_m}|x_2|^{+i\mu_m}$,
   so that
   $$
   \boxed{
   \widetilde\Xi_{m,\infty}(x_1,x_2)
   = \operatorname{sgn}(x_1)^{\epsilon_m} \operatorname{sgn}(x_2)^{\epsilon_m}
     \left|\frac{x_1}{x_2}\right|^{-i\mu_m}
   = \operatorname{sgn}(x_1 x_2)^{\epsilon_m} \left|\frac{x_1}{x_2}\right|^{-i\mu_m}.}
   \tag{A4}
   $$
   For a principal idele $\alpha \in F^\times$,
   $\prod_{\mathfrak p}\widetilde\Xi_{m,\mathfrak p}(\alpha) = \Xi_m((\alpha)) = \widetilde\Xi_{m,\infty}(\sigma_1\alpha,\sigma_2\alpha)^{-1}$,
   so $\widetilde\Xi_m$ is trivial on $F^\times$ and defines a continuous
   unitary Hecke character of $\mathbb A_F^\times / F^\times$. Every finite
   local component is unramified, so the **finite conductor is $\mathfrak f_m = \mathcal O_F$**
   ($N\mathfrak f_m = 1$, arithmetic conductor $N_m = |\Delta_F| N\mathfrak f_m = 5$)
   for both even and odd $m$. The two real sign exponents are the pair
   $(\epsilon_m, \epsilon_m)$: for even $m$ the infinite modulus is empty, and
   for odd $m$ it is $\infty_1\infty_2$.
   Conversely, $\{\Xi_m\}_{m \in \mathbb Z}$ is the **complete** family of
   unitary Hecke characters of $F$ that are unramified at all finite places and
   trivial on the diagonal positive archimedean subgroup $\{(r,r) : r > 0\} \subset F_\infty^\times$:
   any such character has archimedean component $\operatorname{sgn}(x_1)^a\operatorname{sgn}(x_2)^b |x_1/x_2|^{i\mu}$;
   triviality on $-1 \in \mathcal O_F^\times$ forces $a \equiv b \equiv \epsilon \pmod 2$
   ($\epsilon \in \{0,1\}$), triviality on $\phi \in \mathcal O_F^\times$ forces
   $(-1)^\epsilon e^{2i\mu L} = 1 \implies \mu = -\pi m/(2L)$ with $m \equiv \epsilon \pmod 2$,
   and $h_F = 1$ uniquely determines all finite prime values.
3. **Infinite order and non-Galois invariance for $m \ne 0$:** directly on ideles
   with archimedean component $(e^r, 1)$ ($r \in \mathbb R$) and all finite
   components $1$, $\widetilde\Xi_m$ evaluates to $e^{-i\mu_m r}$; for $m \ne 0$
   this has infinite image and differs from its Galois conjugate $e^{+i\mu_m r}$.
   Equivalently on prime ideals, by `SPLIT-PRIME-RAPIDITY-INDEPENDENCE [T]`,
   $[t(\mathfrak p)] \in \mathbb R/L\mathbb Z$ is non-torsion at split primes, so
   $\Xi_m(\mathfrak p)^2 = \Psi_m(\mathfrak p) = \exp(2\pi i m t(\mathfrak p)/L)$
   has infinite multiplicative order whenever $m \ne 0$. Under the nontrivial
   Galois automorphism $\iota \in \operatorname{Gal}(F/\mathbb Q)$,
   $N_{F/\mathbb Q}(\iota\alpha) = N_{F/\mathbb Q}(\alpha)$ and
   $t(\iota\alpha) = -t(\alpha)$, so
   $$
   \Xi_m(\iota\mathfrak a) = \Xi_{-m}(\mathfrak a) = \overline{\Xi_m(\mathfrak a)},
   \qquad
   L_F(s,\Xi_m) = L_F(s,\Xi_{-m}).
   \tag{A5}
   $$
   In particular, $\Xi_m \circ \iota \ne \Xi_m$ for all $m \ne 0$, while the
   characters $\Xi_m$ and $\Xi_{-m}$ are distinct for $m \ne 0$ even though their
   $L$-functions coincide.

---

## 2. Classical Maass Cusp-Form Identification, Functional Equation, and Root Number

In P. Molin and A. Page, *Computing groups of Hecke characters* (ANTS XV, 2022,
`arXiv:2210.02716`, Sections 2.3-2.4 and Section 5.3.2, Proposition 39 and
Example 40 for $F = \mathbb Q(\sqrt 5)$), the unramified Hecke character
$\chi_m^{\mathrm{MP}}$ ($m \in \mathbb Z$) is normalized by the archimedean
component $\operatorname{sgn}(x_1 x_2)^{\epsilon_m} |x_1/x_2|^{i r_m}$ with
$r_m = \pi m/(2\log\phi) = \mu_m$ and $\epsilon_m = m \bmod 2$. Because the
value on a principal ideal is the inverse of the archimedean component at a
generator, the exact dictionary between (A2)-(A4) and Molin-Page is

$$
\boxed{
\Xi_m = \chi_{-m}^{\mathrm{MP}}, \qquad
\Psi_h = \Xi_{2h} = \chi_{-2h}^{\mathrm{MP}}, \qquad
L_F(s,\Xi_m) = L(s,\chi_{-m}^{\mathrm{MP}}) = L(s,\chi_m^{\mathrm{MP}}).}
\tag{A6}
$$

By Proposition 39 and Example 40 of Molin-Page, for every nonzero integer
$m \ne 0$, quadratic automorphic induction from $F = \mathbb Q(\sqrt 5)$ to
$\mathbb Q$ maps $\Xi_m$ to a Maass cusp form $f_m$ on $\Gamma_0(5)$ with:

- **Level and nebentypus:** level $N_m = |\Delta_F| N\mathfrak f_m = 5$ and
  central/nebentypus character $\chi_5(\cdot) = \left(\frac{\cdot}{5}\right)$;
- **Parity:** $\epsilon_m = m \bmod 2 \in \{0,1\}$ under the reflection
  $x + iy \mapsto -x + iy$ (even Maass cusp forms for $m = 2h \ne 0$; odd
  Maass cusp forms for $m = 2h + 1$);
- **Hyperbolic Laplace eigenvalue:**
  $$
  \boxed{
  \lambda_m^{\mathrm{Maass}} = \frac{1}{4} + \mu_m^2
  = \frac{1}{4} + \left(\frac{\pi m}{2\log\phi}\right)^2,
  \qquad
  \lambda_{2h}^{\mathrm{Maass}} = \frac{1}{4} + \left(\frac{\pi h}{\log\phi}\right)^2
  \qquad (m, h \ne 0);}
  \tag{A7}
  $$
- **Fourier-Whittaker expansion ($m \ne 0$):** with $A_m(n) = \sum_{N\mathfrak a = n} \Xi_m(\mathfrak a) = A_{-m}(n) \in \mathbb R$
  and $A_m(1) = 1$,
  $$
  f_m(x+iy) = \sqrt y \sum_{n\ge 1} A_m(n) K_{i\mu_m}(2\pi n y)
  \begin{cases}
    \cos(2\pi n x), & \epsilon_m = 0, \\
    \sin(2\pi n x), & \epsilon_m = 1
  \end{cases}
  \qquad (m \ne 0).
  \tag{A8}
  $$
  (In the exponential Fourier convention $f_m^{\mathrm{exp}}(x+iy) = \sqrt y \sum_{n\ne 0} \rho_m(n) K_{i\mu_m}(2\pi|n|y) e^{2\pi i n x}$
  normalized by $\rho_m(1) = 1$, one has $f_m^{\mathrm{exp}} = 2 f_m$ for
  $\epsilon_m = 0$ and $f_m^{\mathrm{exp}} = 2i f_m$ for $\epsilon_m = 1$, with
  $\rho_m(n) = A_m(n)$ and $\rho_m(-n) = (-1)^{\epsilon_m} A_m(n)$ for $n > 0$.)
- **Completed $L$-function and functional equation with global root number $+1$:**
  writing $\Gamma_{\mathbb R}(s) = \pi^{-s/2}\Gamma(s/2)$, both real places have
  sign exponent $\epsilon_m \in \{0,1\}$ and spectral shifts $\mp i\mu_m$, so
  $$
  \boxed{
  \Lambda(s,\Xi_m)
  = 5^{s/2} \Gamma_{\mathbb R}(s + \epsilon_m - i\mu_m)
            \Gamma_{\mathbb R}(s + \epsilon_m + i\mu_m) L_F(s,\Xi_m),}
  \tag{A9}
  $$
  and for **every** integer $m \in \mathbb Z$ (both even and odd), $\Lambda(s,\Xi_m)$
  satisfies the exact functional equation with global root number $W(\Xi_m) = +1$:
  $$
  \boxed{
  \Lambda(s,\Xi_m) = \Lambda(1-s,\Xi_{-m}) = \Lambda(1-s,\Xi_m),
  \qquad W(\Xi_m) = +1 \quad (m \in \mathbb Z).}
  \tag{A9a}
  $$

**Explicit proof of $W(\Xi_m) = +1$ (Tate local epsilon factors).** Following
B. Poonen, *Tate's thesis* (MIT 18.786 lecture notes, Sections 4.3, 4.7, 5.4,
Theorems 4.18 and 5.22), fix the standard additive character of $\mathbb A_{\mathbb Q}/\mathbb Q$
with $\psi_{\mathbb Q,\infty}(x) = e^{-2\pi i x}$ and $\psi_{\mathbb Q,p}(x) = e^{2\pi i \{x\}_p}$,
and set $\psi_F = \psi_{\mathbb Q} \circ \operatorname{Tr}_{F/\mathbb Q}$.
1. *Archimedean places $\infty_1, \infty_2$:* Using the Gaussian test function
   $f_{\epsilon_m}(x) = x^{\epsilon_m} e^{-\pi x^2}$ on $\mathbb R$, whose Fourier
   transform under $e^{-2\pi i x y}$ is $\widehat f_{\epsilon_m}(y) = (-i)^{\epsilon_m} f_{\epsilon_m}(y)$,
   Tate's local functional equation (Poonen, Lemma 4.20) gives
   $\varepsilon_{\infty_1}(s,\widetilde\Xi_{m,1},\psi_{F,1}) = (-i)^{\epsilon_m}$
   and $\varepsilon_{\infty_2}(s,\widetilde\Xi_{m,2},\psi_{F,2}) = (-i)^{\epsilon_m}$.
   Their archimedean product is
   $$\varepsilon_\infty(s,\Xi_m) = (-i)^{\epsilon_m}(-i)^{\epsilon_m} = (-1)^{\epsilon_m} = (-1)^m.$$
2. *Finite places and the different $\mathfrak d_F = (\sqrt 5) = \mathfrak p_5$:*
   For each finite place $v$ of $F$, the inverse different has valuation
   $-d_v = -v(\mathfrak d_F)$, and the self-dual Haar measure gives
   $\operatorname{vol}(\mathcal O_{F,v}) = (N\mathfrak p_v)^{-d_v/2}$. Since
   $\widetilde\Xi_{m,v}$ is unramified at every finite place, its local epsilon
   factor is $\varepsilon_v(s,\widetilde\Xi_{m,v},\psi_{F,v}) = \Xi_m(\mathfrak p_v)^{d_v} (N\mathfrak p_v)^{d_v(1/2-s)}$.
   Because $\mathfrak d_F = (2\phi - 1) = (\sqrt 5) = \mathfrak p_5$ has
   $N\mathfrak d_F = 5$, every finite place $v \ne \mathfrak p_5$ has $d_v = 0$
   and $\varepsilon_v = 1$, while at $v = \mathfrak p_5$ ($d_{\mathfrak p_5} = 1$,
   $N_{F/\mathbb Q}(\sqrt 5) = -5$, $|\sigma_1(\sqrt 5)/\sigma_2(\sqrt 5)| = 1$):
   $$\Xi_m(\mathfrak p_5) = \operatorname{sgn}(-5)^{\epsilon_m}\cdot 1^{i\mu_m} = (-1)^m, \qquad \varepsilon_{\mathfrak p_5}(s,\widetilde\Xi_{m,\mathfrak p_5},\psi_{F,\mathfrak p_5}) = (-1)^m 5^{1/2-s}.$$
3. *Global sign cancellation:* Multiplying over all places gives the global
   epsilon factor $\varepsilon_F(s,\Xi_m) = (-1)^m \cdot (-1)^m 5^{1/2-s} = 5^{1/2-s}$,
   and evaluating at $s = 1/2$ yields $W(\Xi_m) = \varepsilon_F(1/2,\Xi_m) = +1$
   for every $m \in \mathbb Z$. Odd Maass parity ($\epsilon_m = 1$) does not
   produce a negative global root number because the product $-1$ of the two real
   local epsilon factors cancels the sign $\Xi_m(\mathfrak p_5) = -1$ at the
   different. $\square$

**Principal mode $m = 0$ and trivial zeros:**
- The mode $m = 0$ is explicitly excluded from the cusp-form assertion (A7)-(A8):
  $\Xi_0 = 1$ is Galois-invariant, its automorphic induction is the noncuspidal
  isobaric sum $1 \boxplus \chi_5$, and
  $$
  L_F(s,\Xi_0) = \zeta_F(s) = \zeta(s)L(s,\chi_5), \qquad
  \Lambda(s,\Xi_0) = \bigl[\Gamma_{\mathbb R}(s)\zeta(s)\bigr]\bigl[5^{s/2}\Gamma_{\mathbb R}(s)L(s,\chi_5)\bigr],
  \tag{A9b}
  $$
  which is meromorphic with simple poles at $s = 0$ and $s = 1$.
- For $m \ne 0$, both $L_F(s,\Xi_m)$ and $\Lambda(s,\Xi_m)$ are entire. Using
  $3 + 4\cos\theta + \cos(2\theta) = 2(1+\cos\theta)^2 \ge 0$ on the Euler
  logarithm gives $\zeta_F(\sigma)^3 |L_F(\sigma+it,\Xi_m)|^4 |L_F(\sigma+2it,\Xi_{2m})| \ge 1$
  for $\sigma > 1$; since $2m \ne 0$ makes $L_F(s,\Xi_{2m})$ entire, $L_F(1+it,\Xi_m) \ne 0$
  for all $t \in \mathbb R$. By (A9)-(A9a), the trivial zeros of $L_F(s,\Xi_m)$
  on $\Re s \le 0$ are simple and lie at $s = -\epsilon_m - 2k \pm i\mu_m$
  ($k = 0,1,2,\dots$). Any central zero at $s = 1/2$ has even order since
  $W(\Xi_m) = +1$. Note finally that $\lambda_m^{\mathrm{Maass}}$ is the
  hyperbolic Laplacian eigenvalue associated with the unit lattice of $F$, not a
  Riemann zeta zero ordinate.

---

## 3. Exact Integral-Lift Quotient and Local Euler Factors

Let $\mathfrak p$ be either prime ideal above a split rational prime $p$, and
put $z_{p,m} = \Xi_m(\mathfrak p)$, so $\Xi_m(\bar{\mathfrak p}) = z_{p,m}^{-1}$.
Define the ideal-Mobius character coefficients and their $\chi_5$-convolution:

$$
b^{(m)}(n) = \sum_{N\mathfrak a = n} \mu_F(\mathfrak a)\Xi_m(\mathfrak a),
\qquad
m^{(m)} = b^{(m)} * \chi_5,
\qquad
\mathcal D^{(m)}(s) = \sum_{n\ge 1} m^{(m)}(n) n^{-s}.
\tag{A10}
$$

For even modes $m = 2h$, $\Xi_{2h} = \Psi_h$, $m^{(2h)}(n) = m_h(n) = \operatorname{ev}_h\boldsymbol\mu(n)$
is the mode-$h$ evaluation of the registered integral ideal-rapidity character
lift (`J-IDEAL-RAPIDITY-CHARACTER-LIFT [T]`, PR `#584`), and
$\mathcal D^{(2h)}(s) = \mathcal D_h(s)$.

For $T = p^{-s}$, the complete Euler-factor table for all $m \in \mathbb Z$ is:

| Rational prime $p$ | Local factor of $L_F(s,\Xi_m)^{-1}$ | Local factor of $L(s,\chi_5)$ | Local factor of $\mathcal D^{(m)}(s)$ |
|---|---|---|---|
| Split, $\chi_5(p) = +1$ | $(1 - z_{p,m}T)(1 - z_{p,m}^{-1}T)$ | $(1 - T)^{-1}$ | $(1 - z_{p,m}T)(1 - z_{p,m}^{-1}T)/(1 - T)$ |
| Inert, $\chi_5(p) = -1$ | $1 - T^2$ (since $\mathfrak p = (p)$, $N\mathfrak p = p^2$, $\Xi_m((p)) = 1$) | $(1 + T)^{-1}$ | $(1 - T^2)/(1 + T) = 1 - T$ |
| Ramified, $p = 5$ | $1 - (-1)^m T$ (since $\mathfrak p_5 = (\sqrt 5) = (2+\phi)$, $\Xi_m(\mathfrak p_5) = (-1)^m$) | $1$ | $1 - (-1)^m T$ |

At the ramified prime $\mathfrak p_5 = (\sqrt 5) = (2+\phi)$, both generators
yield the same value $\Xi_m(\mathfrak p_5) = (-1)^m$: at $\alpha = \sqrt 5$ one
has $N_{F/\mathbb Q}(\sqrt 5) = -5$ and $t(\sqrt 5) = 0$, giving
$(-1)^{\epsilon_m}\cdot 1 = (-1)^m$, while at the totally positive generator
$\eta_5 = 2 + \phi = \phi\sqrt 5 \gg 0$ one has $N_{F/\mathbb Q}(2+\phi) = +5$
and $t(2+\phi) = L$, giving $(+1)^{\epsilon_m} e^{\pi i m L/L} = (-1)^m$.

Expanding the split local factor $(1 - (z_{p,m}+z_{p,m}^{-1})T + T^2)(1 + T + T^2 + \cdots)$
shows that at every split prime $p$,

$$
m^{(m)}(p) = 1 - z_{p,m} - z_{p,m}^{-1}, \qquad
m^{(m)}(p^k) = 2 - z_{p,m} - z_{p,m}^{-1} \quad (k \ge 2).
\tag{A11}
$$

All split prime-power tails $k \ge 2$ are nonzero and essential for the exact
cancellation of $(1 - T)^{-1}$. By contrast, the squarefree rational Reynolds
lift (`PR #579`) has local factor $1 - \tfrac{1}{2}(z_p + z_p^{-1})T$ and
leads to a square-root Euler quotient with a correction product rather than a
pure ratio of $L$-functions.

Because $|b^{(m)}(n)| \le a_F(n)$, both $\sum_{n\ge 1} b^{(m)}(n) n^{-s} = L_F(s,\Xi_m)^{-1}$
and $L(s,\chi_5)$ converge absolutely on $\Re s > 1$, proving:

$$
\boxed{
\mathcal D^{(m)}(s) = \sum_{n\ge 1} m^{(m)}(n) n^{-s}
= \frac{L(s,\chi_5)}{L_F(s,\Xi_m)} \qquad (\Re s > 1),}
\tag{A12}
$$

and in particular for the even modes $m = 2h$ and the principal mode $m = 0$:

$$
\boxed{
\mathcal D_h(s) = \sum_{n\ge 1} m_h(n) n^{-s}
= \frac{L(s,\chi_5)}{L_F(s,\Psi_h)} \quad (\Re s > 1),
\qquad
\mathcal D_0(s) = \frac{L(s,\chi_5)}{\zeta(s)L(s,\chi_5)} = \frac{1}{\zeta(s)}.}
\tag{A13}
$$

Notice that at the ramified prime $p = 5$, even modes $m = 2h$ have local
factor $1 - 5^{-s}$, whereas odd modes $m = 2h+1$ have local factor
$1 + 5^{-s}$ because the ramified polarization class $[D_{2+\phi}]$ sits at
the half-period $t(2+\phi) = L \in \mathbb R/(2L\mathbb Z)$.

---

## 4. Exact Meromorphic Order and Non-Cancellation Conditions

For every $m \ne 0$, both $L(s,\chi_5)$ and the cuspidal Hecke $L$-function
$L_F(s,\Xi_m)$ extend to entire functions on $\mathbb C$. Therefore $\mathcal D^{(m)}(s)$
is meromorphic on $\mathbb C$, and at every point $\rho \in \mathbb C$ its
exact order is

$$
\boxed{
\operatorname{ord}_{s=\rho}\mathcal D^{(m)}(s)
= \operatorname{ord}_{s=\rho} L(s,\chi_5) - \operatorname{ord}_{s=\rho} L_F(s,\Xi_m).}
\tag{A14}
$$

Accordingly:

1. **Holomorphy from denominator GRH:** if $\mathrm{GRH}$ holds for $L_F(s,\Xi_m)$
   ($m \ne 0$), then $\operatorname{ord}_\rho L_F(s,\Xi_m) = 0$ on $\Re s > 1/2$,
   so $\mathcal D^{(m)}(s)$ is holomorphic on $\Re s > 1/2$ without any further
   hypothesis.
2. **Converse requires non-cancellation:** holomorphy of $\mathcal D^{(m)}(s)$
   on $\Re s > 1/2$ implies $\operatorname{ord}_\rho L_F(s,\Xi_m) \le \operatorname{ord}_\rho L(s,\chi_5)$
   there. Assuming $\mathrm{GRH}$ for the fixed numerator $L(s,\chi_5)$ gives
   $\operatorname{ord}_\rho L(s,\chi_5) = 0$ on $\Re s > 1/2$, yielding the
   exact conditional biconditional:
   $$
   \boxed{
   \text{Assuming }\mathrm{GRH}\text{ for }L(s,\chi_5):\quad
   \mathcal D^{(m)}(s)\text{ is holomorphic on }\Re s > \tfrac{1}{2}
   \ \Longleftrightarrow\ 
   \mathrm{GRH}\text{ holds for }L_F(s,\Xi_m) \quad (m \ne 0).}
   \tag{A14a}
   $$
   Even under both $\mathrm{GRH}$ premises, asserting on the critical line
   $\Re s = 1/2$ that every critical-line zero of $L_F(s,\Xi_m)$ is an
   uncancelled pole of $\mathcal D^{(m)}(s)$ requires linear independence /
   non-coincidence of the critical-line zeros of $L(s,\chi_5)$ and $L_F(s,\Xi_m)$.

---

## 5. Conditional Smooth Summatory Estimate and Explicit Conductor Dependence

Assume $\mathrm{GRH}$ for a given cuspidal mode $L_F(s,\Xi_m)$ ($m \ne 0$). Let
$w \in C_c^\infty((0,\infty))$ be a smooth compactly supported test function,
with Mellin transform $\widehat w(s) = \int_0^\infty w(u) u^{s-1}\,du$.

### 5.1 Analytic Conductor and Reciprocal Bound via Borel-Caratheodory

From the completed $L$-function (A9), the height- and mode-dependent analytic
conductor of $L_F(s,\Xi_m)$ on vertical lines $s = \sigma + it$ is

$$
\boxed{
Q_m(t) := 5\bigl(1 + |t + \mu_m|\bigr)\bigl(1 + |t - \mu_m|\bigr),
\qquad \mu_m = \frac{\pi m}{2L}.}
\tag{A15}
$$

We first prove an explicit vertical polynomial bound valid on the entire
half-plane $\sigma \ge -1/2$ (including $\sigma \ge 2$):

- **Right half-plane $\sigma \ge 3/2$ (Euler product / Dirichlet series region):**
  for all $\sigma \ge 3/2$ and $y \in \mathbb R$, the Dirichlet series and Euler
  product of $L_F(\sigma + iy, \Xi_m)$ converge absolutely with
  $$
  \bigl|L_F(\sigma + iy, \Xi_m)\bigr| \le \zeta_F(\sigma) \le \zeta_F(3/2)
  \le \zeta_F(3/2)\,Q_m(y) \qquad (\sigma \ge 3/2).
  $$
- **Vertical line $\sigma = -1/2$ via the exact gamma shift $\Gamma_{\mathbb R}(w+2) = \frac{w}{2\pi}\Gamma_{\mathbb R}(w)$:**
  for $s = -\tfrac{1}{2} + iy$, one has $1 - s = \tfrac{3}{2} - iy$, so
  $\Re(1 - s) = \tfrac{3}{2} = \Re s + 2$. Because $|\Gamma_{\mathbb R}(\sigma - iu)| = |\Gamma_{\mathbb R}(\sigma + iu)|$
  and $(2\epsilon_m - 1)^2 = 1$ for both $\epsilon_m \in \{0,1\}$, the identity
  $\Gamma_{\mathbb R}(w+2) = \frac{w}{2\pi}\Gamma_{\mathbb R}(w)$ gives for
  $u = y \mp \mu_m$:
  $$
  \left|\frac{\Gamma_{\mathbb R}(1 - s + \epsilon_m \mp i\mu_m)}{\Gamma_{\mathbb R}(s + \epsilon_m \mp i\mu_m)}\right|_{\Re s = -1/2}
  = \left|\frac{-\tfrac{1}{2} + \epsilon_m + iu}{2\pi}\right|
  = \frac{\sqrt{1 + 4u^2}}{4\pi}
  \le \frac{1 + |u|}{2\pi}.
  $$
  Combining the two archimedean places with $\bigl|5^{(1-s)/2}/5^{s/2}\bigr| = 5$
  and $|L_F(\tfrac{3}{2} - iy, \Xi_m)| \le \zeta_F(3/2)$, the functional
  equation (A9a) yields on $\Re s = -1/2$:
  $$
  \bigl|L_F(-\tfrac{1}{2} + iy, \Xi_m)\bigr|
  \le \frac{5\,\zeta_F(3/2)}{4\pi^2}\bigl(1 + |y - \mu_m|\bigr)\bigl(1 + |y + \mu_m|\bigr)
  = \frac{\zeta_F(3/2)}{4\pi^2}\,Q_m(y)
  \le \zeta_F(3/2)\,Q_m(y).
  $$
- **Phragmen-Lindelof on the strip $-1/2 \le \sigma \le 3/2$:** for $m \ne 0$,
  $L_F(z,\Xi_m)$ is entire of finite order, so applying the Phragmen-Lindelof
  maximum principle on $-1/2 \le \sigma \le 3/2$ between the boundary bounds at
  $\sigma = -1/2$ and $\sigma = 3/2$ establishes on the entire half-plane
  $\sigma \ge -1/2$ the explicit bound with $C_0 = 1$:

$$
\boxed{
\bigl|L_F(\sigma + iy, \Xi_m)\bigr|
\le \zeta_F(3/2)\,Q_m(y)^{C_0} \qquad (\sigma \ge -1/2,\ C_0 := 1).}
\tag{A16}
$$

Fix $0 < \delta < 1/2$. Under $\mathrm{GRH}$ for $L_F(s,\Xi_m)$, $L_F(z,\Xi_m)$
has no zeros in $\Re z > 1/2$, so $\log L_F(z,\Xi_m)$ is analytic on the disk
$|z - (2 + it)| \le R := \tfrac{3}{2} - \tfrac{\delta}{2}$ (which spans real
parts $\Re z \in [\tfrac{1}{2} + \tfrac{\delta}{2},\, \tfrac{7}{2} - \tfrac{\delta}{2}] \subset [-1/2, \infty)$),
with its branch fixed at the center $2 + it$ by the absolutely convergent Euler
sum $|\log L_F(2 + it, \Xi_m)| \le \log\zeta_F(2) = O(1)$. On this disk,
$|\Im z - t| \le R < 3/2$ implies $1 + |\Im z \pm \mu_m| \le \tfrac{5}{2}(1 + |t \pm \mu_m|)$
and $Q_m(\Im z) \le \tfrac{25}{4}Q_m(t)$, so (A16) gives
$\Re\log L_F(z,\Xi_m) \le C_0 \log Q_m(t) + \log(\tfrac{25}{4}\zeta_F(3/2))$.
Applying the Borel-Caratheodory theorem on the concentric disk of smaller
radius $r := \tfrac{3}{2} - \delta$ (where $\frac{2r}{R-r} = \frac{6-4\delta}{\delta} \le \frac{6}{\delta}$)
yields both upper and lower control of $\Re\log L_F$:

$$
\bigl|\log L_F(\sigma + it, \Xi_m)\bigr|
\le \frac{6}{\delta}\bigl(C_0 \log Q_m(t) + O(1)\bigr) + O(\delta^{-1})
\qquad (\tfrac{1}{2} + \delta \le \sigma \le 2),
$$

and therefore the self-contained polynomial reciprocal bound with explicit
exponent $B_\delta := 12 C_0 / \delta = 12 / \delta$:

$$
\boxed{
\bigl|L_F(\sigma + it, \Xi_m)^{-1}\bigr|
\ll_\delta Q_m(t)^{6 C_0 / \delta}
\ll_\delta \bigl(1 + |t| + |\mu_m|\bigr)^{B_\delta},
\qquad B_\delta := \frac{12 C_0}{\delta} = \frac{12}{\delta}
\qquad (\tfrac{1}{2} + \delta \le \sigma \le 2).}
\tag{A17}
$$

### 5.2 Mellin Contour Shift and Mode Dependence

Combining the proved Borel-Caratheodory bound (A17) with the standard convexity
bound $|L(\sigma + it, \chi_5)| \ll (1 + |t|)^{1/2}$ on $\tfrac{1}{2} + \delta \le \sigma \le 2$
gives

$$
\bigl|\mathcal D^{(m)}(\sigma + it)\bigr|
\ll_\delta (1 + |t|)^{1/2 + B_\delta} (1 + |m|)^{B_\delta}
\qquad (\tfrac{1}{2} + \delta \le \sigma \le 2,\ B_\delta = 12/\delta).
\tag{A18}
$$

Integration by parts $K = \lceil B_\delta \rceil + 3$ times shows
$|\widehat w(\sigma + it)| \ll_{w,\delta} (1 + |t|)^{-K}$ uniformly on
$1/2 \le \sigma \le 2$. Shifting the Mellin inversion contour

$$
\sum_{n\ge 1} m^{(m)}(n) w(n/X)
= \frac{1}{2\pi i}\int_{(2)} \mathcal D^{(m)}(s)\widehat w(s) X^s\,ds
$$

to the line $\Re s = \tfrac{1}{2} + \delta$ encounters no poles and proves the
conditional smooth summatory estimate with explicit polynomial conductor
exponent $B_\delta = 12/\delta$:

$$
\boxed{
\sum_{n\ge 1} m^{(m)}(n) w(n/X)
= O_{w,\delta}\Bigl((1 + |m|)^{B_\delta} X^{1/2 + \delta}\Bigr),
\qquad B_\delta = \frac{12 C_0}{\delta} = \frac{12}{\delta}
\qquad (X \ge 1, \ m \ne 0).}
\tag{A19}
$$

**Scope boundary (`[OPEN]` for $\varepsilon$-exponent and growing-mode / sharp-cutoff sums):**
1. *From $B_\delta = 12/\delta$ to $\varepsilon > 0$ (`[OPEN / NOT CLAIMED]`):*
   Replacing the proved exponent $B_\delta = 12/\delta$ in (A17)-(A19) by an
   arbitrary $\varepsilon > 0$ is **not** claimed here. Doing so requires first
   establishing a conditional Littlewood upper bound
   $\Re\log L_F(z,\Xi_m) \ll_\delta (\log Q_m(\Im z))^{2-2\Re z}/\log\log Q_m(\Im z)$
   uniformly in the spectral parameter $\mu_m$ on $\Re z \ge \tfrac{1}{2} + \tfrac{\delta}{2}$,
   and second applying Borel-Caratheodory on a disk inside $\Re z \ge \tfrac{1}{2} + \tfrac{\delta}{2}$
   to turn that upper bound on $\Re\log L_F$ into a lower bound on $\Re\log L_F$
   (since an upper bound on $\Re\log L_F$ alone bounds $|L_F|$ above, not
   $|L_F^{-1}|$).
2. *Growing mode ranges $|m| \le H(X)$ and sharp cutoffs (`[OPEN]`):*
   Under (A19), summing a linear combination over $1 \le |m| \le H(X)$ carries
   the polynomial factor $(1 + H(X))^{B_\delta} \sum_{|m|\le H(X)} |c_m|$.
   Uniform subpolynomial control in $H(X)$ and passage from smooth weights
   $w(n/X)$ to the sharp cutoff $\mathbf 1_{n\le X}$ (which replaces rapid
   Mellin decay by the Perron kernel $X^s/s$ and requires vertical mean-value
   control over $|t| \le T$) remain **`[OPEN]`**.

---

## 6. Unconditional Prime Ideals in Narrow Rapidity Sectors

S. Baier and S. Roy, *A note on the distribution of prime ideals in real
quadratic fields* (`arXiv:2307.03513v2`, Theorems 1 and 3, equation (6)), prove
an unconditional lower bound for the number of prime ideals of a real quadratic
field lying simultaneously in a short norm interval $[X, X+Y]$ and a narrow
sector of the archimedean torus.

### 6.1 Projected Sectors on the Ideal Circle $\mathbb R/(L\mathbb Z)$

In equation (6) of Baier-Roy, the angular coordinate of a principal ideal
$\mathfrak a = (\alpha) \subset \mathcal O_F$ is defined modulo $2\pi$ using
the fundamental unit $\phi$ by

$$
\theta(\mathfrak a)
= \frac{\pi}{\log\phi}\log\left|\frac{\sigma_1(\alpha)}{\sigma_2(\alpha)}\right|
= \frac{2\pi t(\alpha)}{L} \pmod{2\pi}.
\tag{A20}
$$

Applying Theorem 3 of Baier-Roy (with the exponents of Theorem 1: norm window
$Y \ge X^{0.765}$ and angular width $\omega \ge X^{-0.235}$) to the dyadic
interval $[X/2, X]$ ($Y = X/2$) and any arc $I \subset \mathbb R/\mathbb Z$ of
length $\delta \in [(2\pi)^{-1} X^{-0.235}, 1)$ gives unconditionally for all
sufficiently large $X$:

$$
\#\bigl\{\mathfrak p \subset \mathcal O_F \text{ prime} :
  X/2 \le N\mathfrak p \le X,\ t(\mathfrak p)/L \in I \pmod 1\bigr\}
\gg \frac{\delta X}{\log X}.
\tag{A21}
$$

Since inert prime ideals $(p)$ have norm $p^2 \in [X/2, X]$ and contribute at
most $O(\sqrt X) = o(X^{0.765}/\log X)$, and the single ramified prime ideal
$(\sqrt 5)$ has norm $5$, (A21) remains valid when restricted to **split prime
ideals** $\mathfrak p$ of prime norm $N\mathfrak p = p$. Under the polarization
bijection (P1)-(P2) of [`CM5_POLARIZATIONS.md`](CM5_POLARIZATIONS.md), this
gives unconditionally at least $\gg \delta X / \log X$ type-$(1,p)$ prime
polarization orbits $[D_\eta] \in \mathcal P_p(B)$ with $p \in [X/2, X]$ whose
projected rapidity $\pi(t(\eta))/L$ lies in $I$.

### 6.2 Single-Sheet Sectors on the Polarization Circle $\mathbb R/(2L\mathbb Z)$

Under the degree-two cover $\pi : \mathbb R/(2L\mathbb Z) \to \mathbb R/(L\mathbb Z)$,
an arc $J \subset \mathbb R/(2L\mathbb Z)$ of length $\delta L$ ($0 < \delta < 1$)
has a disjoint partner $J + L = \{t + L : t \in J\}$ above the same base arc
$I = \pi(J)$ of length $\delta L$. For any totally positive generator $\eta \gg 0$
of an ideal $\mathfrak a$, the indicator of $J$ versus $J + L$ is separated by
the parity character $\operatorname{sgn}_{\mathrm{sheet}}([t]_{2L})$:

$$
\mathbf 1_J([t]_{2L}) + \mathbf 1_{J+L}([t]_{2L}) = \mathbf 1_{\pi(J)}([t]_L),
\qquad
\mathbf 1_J([t]_{2L}) - \mathbf 1_{J+L}([t]_{2L})
= \sum_{k \in \mathbb Z} c_{2k+1}(J)\, e^{\pi i (2k+1) t / L}
= \sum_{k \in \mathbb Z} c_{2k+1}(J)\, \Xi_{2k+1}((\eta)).
\tag{A22}
$$

Thus:

- **Proved unconditional consequence of Baier-Roy on $\mathbb R/(L\mathbb Z)$
  (and on $\mathbb R/(2L\mathbb Z)$ for the two-sheet union $J \cup (J+L)$):**
  the **sum of counts** on the two opposite sheets $J$ and $J + L$ of
  $\mathbb R/(2L\mathbb Z)$ depends only on the even modes $\Psi_h = \Xi_{2h}$
  and is unconditionally bounded below by $\gg \delta X / \log X$ for
  $\delta \ge (2\pi)^{-1} X^{-0.235}$ directly by (A21).
- **Single-sheet arcs on $\mathbb R/(2L\mathbb Z)$ (`[OPEN]`):**
  Equations (6)-(7) and Theorem 3 of Baier-Roy work exclusively on the
  ideal-class circle $\mathbb R/(L\mathbb Z)$ with the even characters
  $\Psi_h = \Xi_{2h}$ (which have empty infinite modulus). Isolating a **single
  sheet** $J \subset \mathbb R/(2L\mathbb Z)$ requires controlling the odd-mode
  sum $\sum_{k} c_{2k+1}(J) \sum_{X/2 \le N\mathfrak p \le X} \Xi_{2k+1}(\mathfrak p)$,
  where $\Xi_{2k+1}$ carries the archimedean sign modulus $\infty_1\infty_2$
  ($\epsilon_{2k+1} = 1$ in (A9)). Having the same finite conductor
  $\mathfrak f = \mathcal O_F$ does not by itself transfer Baier-Roy's theorem
  without verifying the zero-free region, zero-density estimate, and Harman
  sieve inputs for the odd subfamily $\Xi_{2k+1}$; single-sheet prime bounds on
  $\mathbb R/(2L\mathbb Z)$ therefore remain **`[OPEN]`** in this note.


