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
\eta(\alpha) = \frac{1}{2}\log\left|\frac{\sigma_1(\alpha)}{\sigma_2(\alpha)}\right|,
\qquad
\mu_m = \frac{\pi m}{2L},
\qquad
\epsilon = m \bmod 2 \in \{0,1\}.
\tag{A1}
$$

As established geometrically on the polarization circle $\mathbb R/(2L\mathbb Z)$
in [`CM5_POLARIZATIONS.md`](CM5_POLARIZATIONS.md), define on principal fractional
ideals $(\alpha)$:

$$
\boxed{
\Xi_m((\alpha))
= \operatorname{sgn}(N_{F/\mathbb Q}\alpha)^m
  \exp\left(\frac{\pi i m \eta(\alpha)}{L}\right)
= \operatorname{sgn}(N_{F/\mathbb Q}\alpha)^\epsilon
  \left|\frac{\sigma_1(\alpha)}{\sigma_2(\alpha)}\right|^{i\mu_m}.}
\tag{A2}
$$

When $m = 2h$ is even ($\epsilon = 0$), $\mu_{2h} = \tau_h := \pi h / L$, the
norm-sign factor is $+1$, and $\Xi_{2h}$ coincides with the registered
ideal-rapidity character lift

$$
\Psi_h((\alpha)) = \Xi_{2h}((\alpha))
= \exp\left(\frac{2\pi i h \eta(\alpha)}{L}\right)
= \left|\frac{\sigma_1(\alpha)}{\sigma_2(\alpha)}\right|^{i\tau_h}.
\tag{A3}
$$

### 1.1 Unit Invariance, Idelic Normalization, and Infinite Order

1. **Unit invariance for all $m \in \mathbb Z$:** every unit of $\mathcal O_F$
   has the form $u = \pm \phi^k$ ($k \in \mathbb Z$), with
   $N_{F/\mathbb Q}(u) = (-1)^k$ and $\eta(u) = kL$. Thus
   $$
   \operatorname{sgn}(N_{F/\mathbb Q}(u\alpha))^m
   = (-1)^{mk}\operatorname{sgn}(N_{F/\mathbb Q}\alpha)^m,
   \qquad
   e^{\pi i m \eta(u\alpha)/L} = e^{\pi i m k} e^{\pi i m \eta(\alpha)/L}
   = (-1)^{mk} e^{\pi i m \eta(\alpha)/L}.
   $$
   The two $(-1)^{mk}$ factors cancel for both even and odd $m$, so $\Xi_m$ is
   a well-defined unitary character on the group of fractional ideals of $F$.
2. **Global idelic Hecke character and conductor:** at each finite prime ideal
   $\mathfrak p$ of $\mathcal O_F$, define the unramified local character
   $\widetilde\Xi_{m,\mathfrak p}(x) = \Xi_m(\mathfrak p)^{v_{\mathfrak p}(x)}$,
   which is trivial on $\mathcal O_{F,\mathfrak p}^\times$. At the two real
   places $(x_1,x_2) \in \mathbb R^\times \times \mathbb R^\times$, define
   $$
   \boxed{
   \widetilde\Xi_{m,\infty}(x_1,x_2)
   = \operatorname{sgn}(x_1)^\epsilon \operatorname{sgn}(x_2)^\epsilon
     \left|\frac{x_1}{x_2}\right|^{-i\mu_m}
   = \operatorname{sgn}(x_1 x_2)^\epsilon \left|\frac{x_1}{x_2}\right|^{-i\mu_m}.}
   \tag{A4}
   $$
   For a principal idele $\alpha \in F^\times$,
   $\prod_{\mathfrak p}\widetilde\Xi_{m,\mathfrak p}(\alpha) = \Xi_m((\alpha)) = \widetilde\Xi_{m,\infty}(\sigma_1\alpha,\sigma_2\alpha)^{-1}$,
   so $\widetilde\Xi_m$ is trivial on $F^\times$ and defines a continuous
   unitary Hecke character of $\mathbb A_F^\times / F^\times$. Every finite
   local component is unramified, so the **finite conductor is $\mathfrak f = \mathcal O_F$**
   ($N\mathfrak f = 1$, $|\Delta_F| N\mathfrak f = 5$) for both even and odd
   $m$. For even $m$, the infinite modulus is trivial; for odd $m$, both real
   sign exponents equal $\epsilon = 1$, so the infinite part of the ray-class
   modulus is $\infty_1\infty_2$.
3. **Infinite order and non-Galois invariance for $m \ne 0$:** let $\mathfrak p$
   be a prime ideal above a split rational prime $p$. By the registered theorem
   `SPLIT-PRIME-RAPIDITY-INDEPENDENCE [T]`, $[\eta(\mathfrak p)] \in \mathbb R/L\mathbb Z$
   is non-torsion. Since $\Xi_m(\mathfrak p)^2 = \Psi_m(\mathfrak p) = \exp(2\pi i m \eta(\mathfrak p)/L)$,
   $\Xi_m(\mathfrak p)$ has infinite multiplicative order whenever $m \ne 0$.
   Under the nontrivial Galois automorphism $\iota \in \operatorname{Gal}(F/\mathbb Q)$,
   $N_{F/\mathbb Q}(\iota\alpha) = N_{F/\mathbb Q}(\alpha)$ and
   $\eta(\iota\alpha) = -\eta(\alpha)$, so
   $$
   \Xi_m(\iota\mathfrak a) = \Xi_{-m}(\mathfrak a) = \overline{\Xi_m(\mathfrak a)},
   \qquad
   L_F(s,\Xi_m) = L_F(s,\Xi_{-m}).
   \tag{A5}
   $$
   In particular, $\Xi_m \circ \iota \ne \Xi_m$ for all $m \ne 0$.

---

## 2. Classical Maass Cusp-Form Identification (Molin-Page)

In P. Molin and A. Page, *Computing groups of Hecke characters* (ANTS XV, 2022,
`arXiv:2210.02716`, Sections 2.3-2.4 and Section 5.3.2, Proposition 39 and
Example 40 for $F = \mathbb Q(\sqrt 5)$), the unramified Hecke character
$\chi_m^{\mathrm{MP}}$ ($m \in \mathbb Z$) is normalized by the archimedean
component $\operatorname{sgn}(x_1 x_2)^\epsilon |x_1/x_2|^{i r_m}$ with
$r_m = \pi m/(2\log\phi) = \mu_m$ and $\epsilon \equiv m \pmod 2$. Because the
value on a principal ideal is the inverse of the archimedean component at a
generator, the exact dictionary between (A2)-(A4) and Molin-Page is

$$
\boxed{
\Xi_m = \chi_{-m}^{\mathrm{MP}}, \qquad
\Psi_h = \Xi_{2h} = \chi_{-2h}^{\mathrm{MP}}, \qquad
L_F(s,\Xi_m) = L(s,\chi_{-m}^{\mathrm{MP}}) = L(s,\chi_m^{\mathrm{MP}}).}
\tag{A6}
$$

By Proposition 39 and Example 40 of Molin-Page, for every integer $m \ne 0$,
quadratic automorphic induction from $F = \mathbb Q(\sqrt 5)$ to $\mathbb Q$
maps $\Xi_m$ to a Maass cusp form $f_m$ on $\Gamma_0(5)$ with:

- **Level and nebentypus:** level $N = |\Delta_F| N\mathfrak f = 5$ and
  quadratic character $\chi_5(\cdot) = \left(\frac{\cdot}{5}\right)$;
- **Parity:** $\epsilon = m \bmod 2 \in \{0,1\}$ under the reflection
  $x + iy \mapsto -x + iy$ (even Maass cusp forms for $m = 2h \ne 0$; odd
  Maass cusp forms for $m = 2h + 1$);
- **Hyperbolic Laplace eigenvalue:**
  $$
  \boxed{
  \lambda_m^{\mathrm{Maass}} = \frac{1}{4} + \mu_m^2
  = \frac{1}{4} + \left(\frac{\pi m}{2\log\phi}\right)^2,
  \qquad
  \lambda_{2h}^{\mathrm{Maass}} = \frac{1}{4} + \left(\frac{\pi h}{\log\phi}\right)^2;}
  \tag{A7}
  $$
- **Fourier-Whittaker expansion:** with $A_m(n) = \sum_{N\mathfrak a = n} \Xi_m(\mathfrak a) \in \mathbb R$,
  $$
  f_m(x+iy) = \sqrt y \sum_{n\ge 1} A_m(n) K_{i\mu_m}(2\pi n y)
  \begin{cases}
    \cos(2\pi n x), & m \text{ even } (\epsilon = 0), \\
    \sin(2\pi n x), & m \text{ odd } (\epsilon = 1);
  \end{cases}
  \tag{A8}
  $$
- **Completed $L$-function:** writing $\Gamma_{\mathbb R}(s) = \pi^{-s/2}\Gamma(s/2)$,
  both real places have sign exponent $\epsilon \in \{0,1\}$ and spectral shifts
  $\pm i\mu_m$, so Section 2.4 of Molin-Page gives
  $$
  \boxed{
  \Lambda(s,\Xi_m)
  = 5^{s/2} \Gamma_{\mathbb R}(s + \epsilon + i\mu_m)
            \Gamma_{\mathbb R}(s + \epsilon - i\mu_m) L_F(s,\Xi_m).}
  \tag{A9}
  $$

For $m = 0$, $L_F(s,\Xi_0) = \zeta_F(s) = \zeta(s)L(s,\chi_5)$ has a simple
pole at $s = 1$ and belongs to the noncuspidal Eisenstein spectrum. Note also
that $\lambda_m^{\mathrm{Maass}}$ is the eigenvalue of the hyperbolic Laplacian
$-y^2(\partial_x^2 + \partial_y^2)$ associated with the periodic lattice of
units, not a Riemann zeta zero ordinate.

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
   there. To deduce that $L_F(s,\Xi_m)$ is zero-free on $\Re s > 1/2$, one needs
   that $L(s,\chi_5)$ has no zeros there (for example, by assuming $\mathrm{GRH}$
   for $L(s,\chi_5)$). Even under both $\mathrm{GRH}$ premises, asserting that
   every critical-line zero of $L_F(s,\Xi_m)$ is an uncancelled pole of
   $\mathcal D^{(m)}(s)$ requires linear independence / non-coincidence of the
   critical-line zeros of $L(s,\chi_5)$ and $L_F(s,\Xi_m)$.

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

By the functional equation and Phragmen-Lindelof convexity on $-1/2 \le \sigma \le 5/2$,
there is an absolute constant $C_0 > 0$ such that

$$
|L_F(\sigma + it, \Xi_m)| \ll Q_m(t)^{C_0} \qquad (-1/2 \le \sigma \le 5/2).
\tag{A16}
$$

Fix $0 < \delta < 1/2$. Under $\mathrm{GRH}$ for $L_F(s,\Xi_m)$, $L_F(z,\Xi_m)$
has no zeros in $\Re z > 1/2$, so $\log L_F(z,\Xi_m)$ is analytic on the disk
$|z - (2 + it)| \le R := \tfrac{3}{2} - \tfrac{\delta}{2}$, with its branch fixed
at the center $2 + it$ by the absolutely convergent Euler sum
$|\log L_F(2 + it, \Xi_m)| \le \log\zeta_F(2) = O(1)$. On this disk, (A16)
gives $\Re\log L_F(z,\Xi_m) \le C_0 \log Q_m(t) + O(1)$. Applying the
Borel-Caratheodory theorem on the concentric disk of smaller radius
$r := \tfrac{3}{2} - \delta$ (where $\frac{2r}{R-r} = \frac{6-4\delta}{\delta} \le \frac{6}{\delta}$)
yields

$$
\bigl|\log L_F(\sigma + it, \Xi_m)\bigr|
\le \frac{6}{\delta}\bigl(C_0 \log Q_m(t) + O(1)\bigr) + O(\delta^{-1})
\qquad (\tfrac{1}{2} + \delta \le \sigma \le 2),
$$

and therefore the explicit reciprocal polynomial bound

$$
\boxed{
\bigl|L_F(\sigma + it, \Xi_m)^{-1}\bigr|
\ll_\delta Q_m(t)^{6 C_0 / \delta}
\ll_\delta \bigl(1 + |t| + |\mu_m|\bigr)^{12 C_0 / \delta}
\qquad (\tfrac{1}{2} + \delta \le \sigma \le 2).}
\tag{A17}
$$

*(Remark on the conditional Littlewood / Lindelof refinement: using the standard
conditional bound $\Re\log L_F(z,\Xi_m) \ll (\log Q_m(t))^{2-2\Re z}/\log\log Q_m(t)$
under $\mathrm{GRH}$ improves the exponent $12 C_0 / \delta$ in (A17) to any
$\varepsilon > 0$, giving $|L_F(\sigma+it,\Xi_m)^{-1}| \ll_{\delta,\varepsilon} Q_m(t)^\varepsilon \ll_{\delta,\varepsilon} (1 + |t| + |m|)^\varepsilon$
for $\sigma \ge \tfrac{1}{2} + \delta$.)*

### 5.2 Mellin Contour Shift and Mode-Growing Regime

Combining (A17) (or its $\varepsilon$-refinement) with the standard convexity
bound $|L(\sigma + it, \chi_5)| \ll (1 + |t|)^{1/2}$ on $\tfrac{1}{2} + \delta \le \sigma \le 2$
gives

$$
\bigl|\mathcal D^{(m)}(\sigma + it)\bigr|
\ll_{\delta,\varepsilon} (1 + |t|)^{1/2 + \varepsilon} (1 + |m|)^\varepsilon
\qquad (\tfrac{1}{2} + \delta \le \sigma \le 2).
\tag{A18}
$$

Integration by parts $K$ times shows $|\widehat w(\sigma + it)| \ll_{w,K} (1 + |t|)^{-K}$
uniformly on $1/2 \le \sigma \le 2$. Shifting the Mellin inversion contour

$$
\sum_{n\ge 1} m^{(m)}(n) w(n/X)
= \frac{1}{2\pi i}\int_{(2)} \mathcal D^{(m)}(s)\widehat w(s) X^s\,ds
$$

to the line $\Re s = \tfrac{1}{2} + \delta$ encounters no poles and yields both
the fixed-mode estimate and its explicit mode dependence:

$$
\boxed{
\sum_{n\ge 1} m^{(m)}(n) w(n/X)
= O_{w,\delta,\varepsilon}\Bigl((1 + |m|)^\varepsilon X^{1/2 + \delta}\Bigr)
\qquad (X \ge 1, \ m \ne 0).}
\tag{A19}
$$

In particular, when summing a smooth linear combination $\sum_{1 \le |m| \le H(X)} c_m \sum_{n\ge 1} m^{(m)}(n) w(n/X)$
under $\mathrm{GRH}$ for all modes $1 \le |m| \le H(X)$, the individual mode
bounds contribute $(1 + H(X))^\varepsilon X^{1/2+\delta} \sum_{|m|\le H(X)} |c_m|$.
Passing from smooth weights $w(n/X)$ to a sharp cutoff $\mathbf 1_{n\le X}$
replaces rapid Mellin decay by the Perron kernel $X^s/s$, which requires a
separate truncation height $T$ and vertical mean-value control of
$\mathcal D^{(m)}(\tfrac{1}{2} + \delta + it)$ over $|t| \le T$.

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
= \frac{2\pi \eta(\alpha)}{L} \pmod{2\pi}.
\tag{A20}
$$

Applying Theorem 3 of Baier-Roy (with the exponents of Theorem 1: norm window
$Y \ge X^{0.765}$ and angular width $\omega \ge X^{-0.235}$) to the dyadic
interval $[X/2, X]$ ($Y = X/2$) and any arc $I \subset \mathbb R/\mathbb Z$ of
length $\delta \in [(2\pi)^{-1} X^{-0.235}, 1)$ gives unconditionally for all
sufficiently large $X$:

$$
\#\bigl\{\mathfrak p \subset \mathcal O_F \text{ prime} :
  X/2 \le N\mathfrak p \le X,\ \eta(\mathfrak p)/L \in I \pmod 1\bigr\}
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

- the **sum of counts** on the two opposite sheets $J$ and $J + L$ of
  $\mathbb R/(2L\mathbb Z)$ depends only on the even modes $\Psi_h = \Xi_{2h}$
  and is unconditionally bounded below by $\gg \delta X / \log X$ for
  $\delta \ge (2\pi)^{-1} X^{-0.235}$ directly by (A21);
- isolating a **single sheet** $J \subset \mathbb R/(2L\mathbb Z)$ requires
  controlling the odd-mode sum $\sum_{k} c_{2k+1}(J) \sum_{X/2 \le N\mathfrak p \le X} \Xi_{2k+1}(\mathfrak p)$
  for $|2k+1| \ll \delta^{-1} X^\varepsilon$. Because the odd modes $\Xi_{2k+1}$
  analyzed in Sections 1-2 have the same trivial finite conductor $\mathfrak f = \mathcal O_F$
  and level $5$ as the even modes $\Psi_h$ (differing only by the archimedean
  parity shift $\epsilon = 1$ in (A9)), the same zero-free region and
  zero-density estimates over $F = \mathbb Q(\sqrt 5)$ apply to the full
  narrow-class Hecke family $\{\Xi_m\}_{m \in \mathbb Z}$ when extending
  sector theorems from $\mathbb R/(L\mathbb Z)$ to $\mathbb R/(2L\mathbb Z)$.
