# TWIST-J, the Riemann Hypothesis, CM5 Polarizations, and Hecke-Maass Series

```text
STATUS:                  NON-CANONICAL / SYNTHESIS AND CLASSICAL DICTIONARY
AUTHORITY:               Public Canon v103 remains unchanged
PUBLIC BASE:             dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d (tag canon-v103)
PUBLIC CONTENT COMMIT:   8e1f6538a09c8ef012a0a9971d501119f13d52ee
PUBLIC CANON SHA-256:    d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b
PUBLIC CANON BYTES:      1052518
DATE:                    2026-10-20
FORMAL RUN FOR THIS DIR: NONE (proof-first classical synthesis)
CANON / REGISTRY CHANGE: NONE
LICENSE:                 Apache-2.0 (A. M. Thorn)
```

## 1. Scope and Executive Summary

This package provides a compact, self-contained reference for how the TWIST-J
program interacts with the Riemann Hypothesis (RH), real-quadratic analytic
number theory, and the arithmetic geometry of the cyclotomic fivefold field.
It changes no file under `canon/`, registers no claim in `canon/REGISTRY.tsv`,
and promotes no claim status.

From the primitive algebraic axiom

$$
J = 1 + \zeta_5^2, \qquad K = \mathbb Q(\zeta_5), \qquad
F = K^+ = \mathbb Q(\sqrt 5), \qquad
\phi = \frac{1+\sqrt 5}{2}, \qquad L = \log\phi,
$$

three exact mathematical threads meet:

1. **Unconditional geometry, integer census, and sector asymptotics of
   polarizations on the selected $\mathrm{CM}_5$ Jacobian**
   ([`CM5_POLARIZATIONS.md`](CM5_POLARIZATIONS.md)): on the fixed abelian
   surface $B = \operatorname{Jac}(y^2 = x^5 - 1)$ with canonical principal
   polarization $\lambda_0$, origin-preserving automorphisms are
   $\operatorname{Aut}(B,0) = \mathcal O_K^\times$, the Neron-Severi group is
   $\operatorname{NS}(B) \simeq \mathcal O_F = \mathbb Z[\phi]$, the ample cone
   is the totally positive cone $\eta \gg 0$, and $D_\eta^2 = 2 N_{F/\mathbb Q}(\eta)$.
   Because $h_F = h_F^+ = 1$ and $N_{K/F}(\mathcal O_K^\times) = \mathcal O_F^{\times,+} = \{\phi^{2n}\}$,
   there is an exact bijection for every $n \ge 1$ between
   $\operatorname{Aut}(B,0)$-orbits of polarizations with $D^2/2 = n$ and
   integral ideals $\mathfrak a \subset \mathcal O_F$ of norm $n$.
   For every rational prime $p$, the number of type-$(1,p)$ polarization orbits
   is $2$ if $p \equiv 1,4 \pmod 5$, $1$ if $p = 5$ (represented by
   $\eta_5 = 2 + \phi$), and $0$ if $p \equiv 2,3 \pmod 5$.
   Every polarization orbit has a unique representative $\eta = x + y\phi$
   modulo $\phi^{2\mathbb Z}$ in the integer cone $x \ge 1,\ 0 \le y < x$, with
   rapidity $t(\eta) = \tfrac{1}{2}\log(\sigma_1\eta/\sigma_2\eta) \in [0,2L)$,
   norm sandwich $x^2 \le q(x,y) = x^2 + xy - y^2 \le \tfrac{5}{4}x^2$, and
   elementary divisors $(d_1,d_2) = (\gcd(x,y), q(x,y)/\gcd(x,y))$. For $M$
   equal sectors on $\theta(\eta) = t(\eta)/(2L) \in [0,1)$, the sector index
   $k \in \{0,\dots,M-1\}$ is decided purely in $\mathbb Z[\phi]$ via
   $\phi^{4k}(\eta')^M \le \eta^M < \phi^{4(k+1)}(\eta')^M$
   ($\eta' = \sigma_2\eta = (x+y) - y\phi > 0$). Across all norms $q \le X$ and
   any arc $I \subset \mathbb R/\mathbb Z$ of Haar measure $|I|$, the all-class
   and primitive type-$(1,n)$ counts satisfy uniformly in $I$:
   $$
   A(X,I) = \frac{2L}{\sqrt 5}\,|I|\,X + O(\sqrt X + 1), \qquad
   A_{\mathrm{prim}}(X,I) = \frac{2L}{\sqrt 5\,\zeta(2)}\,|I|\,X + O\bigl(\sqrt X\log(2X)\bigr).
   $$
2. **Polarization rapidity, the full Hecke character family $\Xi_m$, Maass
   cusp forms, root numbers, and the integral Mobius quotient**
   ([`HECKE_MAASS_BRIDGE.md`](HECKE_MAASS_BRIDGE.md)):
   pullback by $\operatorname{Aut}(B,0)$ shifts the hyperbolic rapidity
   $t(\eta) = \tfrac{1}{2}\log(\sigma_1\eta/\sigma_2\eta)$ by $2nL$, making
   $\mathbb R/(2L\mathbb Z)$ the natural polarization-orbit circle and a
   degree-two cover of the ideal-rapidity circle $\mathbb R/(L\mathbb Z)$.
   Its Fourier modes define the complete family of unitary Hecke characters of
   finite conductor $\mathcal O_F$ that are trivial on the positive diagonal of
   $F_\infty^\times$:
   $$
   \Xi_m((\alpha))
   = \operatorname{sgn}(N_{F/\mathbb Q}\alpha)^{\epsilon_m}
     \left|\frac{\sigma_1\alpha}{\sigma_2\alpha}\right|^{i\pi m/(2L)},
   \qquad \epsilon_m = m \bmod 2 \in \{0,1\}, \quad m \in \mathbb Z,
   $$
   whose even subfamily $\Psi_h = \Xi_{2h}$ is the registered ideal-rapidity
   character lift. The unweighted, mode-$m$ weighted, and primitive type-$(1,n)$
   polarization generating series on $\Re s > 1$ are respectively
   $$
   Z_B^{\mathrm{pol}}(s) = \zeta_F(s) = \zeta(s)L(s,\chi_5), \qquad
   Z_{B,m}^{\mathrm{pol}}(s) = L_F(s,\Xi_m), \qquad
   Z_{B,m}^{\mathrm{prim}}(s) = \frac{L_F(s,\Xi_m)}{\zeta(2s)}.
   $$
   Under quadratic automorphic induction (Molin-Page, Proposition 39 and
   Example 40), each $\Xi_m$ with $m \ne 0$ corresponds to a Maass cusp form on
   $\Gamma_0(5)$ of nebentypus $\chi_5$, parity $\epsilon_m = m \bmod 2 \in \{0,1\}$,
   and Laplace eigenvalue $\lambda_m^{\mathrm{Maass}} = \tfrac{1}{4} + (\pi m/(2L))^2$.
   Every mode $m \in \mathbb Z$ (both even and odd) satisfies the functional
   equation $\Lambda(s,\Xi_m) = \Lambda(1-s,\Xi_{-m}) = \Lambda(1-s,\Xi_m)$ with
   global root number $W(\Xi_m) = +1$, because the archimedean epsilon factor
   $(-i)^{\epsilon_m}(-i)^{\epsilon_m} = (-1)^m$ cancels the local epsilon factor
   $\Xi_m(\mathfrak p_5) = (-1)^m$ at the different $\mathfrak d_F = (\sqrt 5) = \mathfrak p_5$.
   Convolving the ideal-Mobius character coefficients $b^{(m)}(n)$ with $\chi_5$
   yields the exact Dirichlet series quotient
   $$
   \mathcal D^{(m)}(s) = \sum_{n\ge 1} m^{(m)}(n) n^{-s}
   = \frac{L(s,\chi_5)}{L_F(s,\Xi_m)} \qquad (\Re s > 1),
   $$
   with $\mathcal D_{2h}(s) = \mathcal D_h(s) = L(s,\chi_5)/L_F(s,\Psi_h)$ and
   $\mathcal D_0(s) = 1/\zeta(s)$.
3. **Unconditional narrow rapidity sectors and conditional GRH bounds with
   explicit analytic conductor** ([`HECKE_MAASS_BRIDGE.md`](HECKE_MAASS_BRIDGE.md)):
   specializing the theorem of Baier and Roy (`arXiv:2307.03513v2`, Theorems 1
   and 3, eq. (6)) to $F = \mathbb Q(\sqrt 5)$ gives, without any RH or GRH
   assumption, at least $\gg \delta X / \log X$ oriented split prime ideals
   (and hence prime polarization orbits) in $[X/2, X]$ inside every projected
   rapidity sector of width $\delta \ge (2\pi)^{-1} X^{-0.235}$ on
   $\mathbb R/(L\mathbb Z)$ (equivalently on the symmetric pair of sheets
   $J \cup (J+L) \subset \mathbb R/(2L\mathbb Z)$).
   Separately, when GRH is permitted as an explicit premise for $L_F(s,\Xi_m)$,
   Borel-Caratheodory and Mellin inversion prove a self-contained smooth
   summatory estimate with explicit dependence $(1+|m|)^{12 C_0/\delta} X^{1/2+\delta}$
   on the analytic conductor $Q_m(t) = 5(1 + |t + \mu_m|)(1 + |t - \mu_m|)$,
   sharpened to $(1+|m|)^\varepsilon X^{1/2+\delta}$ when the conditional
   Littlewood bound is imported.

---

## 2. Public TWIST-J Map of RH and Number-Theory Work (v7 to v103)

The public record separates proven algebraic/geometric structure (`T`),
computational benchmarks (`C`), candidate dictionaries (`D` / `notes/`),
live hypotheses (`H`), live open obligations (`O`), and closed no-go routes (`F`).

| Public stage | Primary public refs | Established mathematical content | Scope boundary |
|---|---|---|---|
| Pentagon filter and normalization | [PR #42](https://github.com/mathorn1973/twist-j/pull/42), [PR #48](https://github.com/mathorn1973/twist-j/pull/48), [PR #53](https://github.com/mathorn1973/twist-j/pull/53) | $c(n) = 5[5\mid n] - 1$ gives $P_0(s) = (5^{1-s}-1)\zeta(s)$; dividing out the filter and importing classical completion gives $Z_J = \zeta$ and $\xi_J = \xi$. | `PENTAGON-NORMALIZATION [T]`. Normalizes the target as $\zeta(s)$; supplies no Weil positivity proof. |
| Conditional Li / Fredholm realizations | [PR #44](https://github.com/mathorn1973/twist-j/pull/44), [`notes/C-LI-COCYCLE-1`](../C-LI-COCYCLE-1/C-LI-COCYCLE-1.md), [`notes/C-LI-S2-RELATIVE-DETERMINANT-1`](../C-LI-S2-RELATIVE-DETERMINANT-1/C-LI-S2-RELATIVE-DETERMINANT-1.md) | Li-Schoenberg-Toeplitz cocycle normal forms, $S_2$ relative determinant, and Stieltjes-Hankel reformulations. | `NON-CANONICAL` notes. Constructing a positive operator from assumed critical-line zeros is already recorded here and is not a new unconditional bridge. |
| Carrier no-go theorems | [PR #55](https://github.com/mathorn1973/twist-j/pull/55), [PR #60](https://github.com/mathorn1973/twist-j/pull/60), [PR #61](https://github.com/mathorn1973/twist-j/pull/61), [PR #62](https://github.com/mathorn1973/twist-j/pull/62), [PR #63](https://github.com/mathorn1973/twist-j/pull/63), [PR #400](https://github.com/mathorn1973/twist-j/pull/400), [PR #446](https://github.com/mathorn1973/twist-j/pull/446), [PR #448](https://github.com/mathorn1973/twist-j/pull/448), [PR #457](https://github.com/mathorn1973/twist-j/pull/457) | Excludes toral Haar spectrum, $E_8$ shell multiplicities, compact $\lambda$-adic Hilbert-Schmidt operators, noncompact bilateral shifts, local ramp/filtration capacity routes, and pentagon-only dilation towers. | Registered `T` no-go rows and paired `F` carrier rows (`SUZUKI-LOCAL-CAPACITY-NOGO [T]`, `PENTAGON-ONLY-DILATIONS [F]`). Excludes only the frozen carrier classes. |
| Compact $\lambda$-adic cocycle grid | [PR #286](https://github.com/mathorn1973/twist-j/pull/286), [PR #288](https://github.com/mathorn1973/twist-j/pull/288), [PR #290](https://github.com/mathorn1973/twist-j/pull/290), [PR #294](https://github.com/mathorn1973/twist-j/pull/294) | Point-spectrum angle set is $2\pi(1/4)\mathbb Z[1/5]$; a cocycle vector exists in $L^2(\mathcal O_\lambda,\mathrm{Haar})$ iff RH holds and every Cayley angle lies in that grid. | `LAMBDA-COCYCLE-GRID-EQUIVALENCE [T]`, `LAMBDA-COCYCLE-BRANCH-COLLAPSE [T]`, `LAMBDA-COCYCLE-ANGLES [H]`. Assuming RH removes only the radial condition, not the angular grid requirement. |
| Real-quadratic rapidity and Fejer Gram control | [PR #343](https://github.com/mathorn1973/twist-j/pull/343), [PR #351](https://github.com/mathorn1973/twist-j/pull/351) | Unordered split-prime rapidity classes $\{r_p,-r_p\}$ in $\mathbb R/L\mathbb Z$, $\mathbb Z$-linear independence of oriented split-prime rapidities, reduced generator bounds, and Fejer Gram control. | `SPLIT-PRIME-RAPIDITY-CLASS [T]`, `SPLIT-PRIME-RAPIDITY-INDEPENDENCE [T]`. Linear independence of a finite prime set is algebraic and distinct from sector density. |
| Galois-equivariant shells and ideal Mobius descent | [PR #579](https://github.com/mathorn1973/twist-j/pull/579), [PR #580](https://github.com/mathorn1973/twist-j/pull/580), [PR #582](https://github.com/mathorn1973/twist-j/pull/582), [PR #584](https://github.com/mathorn1973/twist-j/pull/584), [`notes/C-J-RAPIDITY-GALOIS-EQUIVARIANT-PRIME-SHELL-N`](../C-J-RAPIDITY-GALOIS-EQUIVARIANT-PRIME-SHELL-N/README.md) | $a_F = 1 * \chi_5$, ideal Mobius pushforward $b$, exact descent $\mu = b * \chi_5$, squarefree Reynolds shell ($2^a$ branches) vs. integral character lift $\boldsymbol\mu$ ($3^a$ squarefree branches and split prime-power tails), and $C_0 O_5 = 1/\zeta$. | Eight registered `T` rows and live open obligation `TRIVIAL-RAPIDITY-EVALUATION-BRIDGE [O]`. Exact algebraic identities do not by themselves supply summatory cancellation at augmentation. |
| Nine-probe $O_5(s)$ split-channel chain | [PR #588](https://github.com/mathorn1973/twist-j/pull/588), [PR #592](https://github.com/mathorn1973/twist-j/pull/592), [PR #593](https://github.com/mathorn1973/twist-j/pull/593), [PR #598](https://github.com/mathorn1973/twist-j/pull/598), [PR #602](https://github.com/mathorn1973/twist-j/pull/602), [PR #605](https://github.com/mathorn1973/twist-j/pull/605), [PR #607](https://github.com/mathorn1973/twist-j/pull/607), [PR #609](https://github.com/mathorn1973/twist-j/pull/609), [PR #611](https://github.com/mathorn1973/twist-j/pull/611), [PR #614](https://github.com/mathorn1973/twist-j/pull/614) | Factorizes $H_5 \widehat O_5 = 1/\zeta_F$ on $\Re s > 1/2$, $O_5 = A_5 S_5$, threshold complex Euler characteristic, Walsh link homology, ratio-11 annulus reduction, bilinear transfer, and golden $\phi^2$/Lucas five-antidiagonal reduction. | Merged proof-first probes; all 9 pass `x86_64` and `aarch64` CI (Section 2.1). Preserves power bounds above $1/3$ (or $1/2$) but does not bound the residual signed shell. |
| Golden ladder and full-shell Fourier contract | [PR #792](https://github.com/mathorn1973/twist-j/pull/792), [PR #818](https://github.com/mathorn1973/twist-j/pull/818), [PR #819](https://github.com/mathorn1973/twist-j/pull/819), [`notes/RH-FULL-SHELL-FOURIER-CONTRACT-2026-09-05.md`](../RH-FULL-SHELL-FOURIER-CONTRACT-2026-09-05.md) | Golden/Lucas integrality ladder and exact finite-support reconstruction of augmentation from nonzero modes $1 \le h \le 4N-1$ with coefficient norm $< \sqrt{3N/2}$; unconditional PNT-AP forces an unsigned source-energy floor $\gtrsim \sqrt{N/\log N}$. | `RAPIDITY-GOLDEN-LADDER [T]`, `RAPIDITY-TARGET-RECONSTRUCTION [T]`. Rules out unsigned $O(N^\varepsilon)$ source bounds ($\varepsilon < 1/2$) on that frame; signed cancellation across modes remains open. |
| $\mathrm{CM}_5$ Jacobian and integral homology calibration | [`notes/HODGE-AND-TATE-CM5-CALIBRATION-2026-09-11.md`](../HODGE-AND-TATE-CM5-CALIBRATION-2026-09-11.md), [`notes/HODGE-TATE-CM5-INTEGRAL-HOMOLOGY-CALIBRATION-2026-09-11.md`](../HODGE-TATE-CM5-INTEGRAL-HOMOLOGY-CALIBRATION-2026-09-11.md) | Calibrates $B = \operatorname{Jac}(y^2=x^5-1)$ with CM type $\{1,2\}$ and integral $\mathbb Z[j]$ homology against the registered alternating CM pencil $\Omega_{(a,b)}$ after the explicit $P = J^{-1}$ basis change. | `CM-ALTERNATING-PENCIL [T]`, `CM-ALTERNATING-PRIMARY-LATTICE-SEAM [T]`, `CM-PERIOD-LATTICE-NONSELECTION [T]`. Choosing $B$ and $\lambda_0$ is explicit benchmark data, not forced by the bare $J$ carrier. |
| Cyclotomic Dedekind residue and unit-strip counting | [PR #1274](https://github.com/mathorn1973/twist-j/pull/1274) | Exact $\zeta_{\mathbb Q(\zeta_5)}$ residue, $J$-unit-strip fundamental domain, ideal-count identity, and finite code capacity alongside the imported Landau exponent $3/5$. | Five registered `T` rows in v93. Unconditional number-theoretic bridge; independent of RH. |

### 2.1 Verified Two-Architecture CI Ledger for the Nine $O_5$ Probes

Earlier secondary summaries cited stale `pending` text from initial `RESULT.md`
templates. All nine merged $O_5$ probe heads completed with `SUCCESS` across
`architecture-x86_64`, `architecture-aarch64`, and the aggregate `check` gate:

| PR | Probe directory | Verified GitHub Actions run (`x86_64` + `aarch64` + `check` PASS) |
|---:|---|---|
| [#592](https://github.com/mathorn1973/twist-j/pull/592) | `probes/P-O5-SQUAREFREE-TRANSFER-1` | <https://github.com/mathorn1973/twist-j/actions/runs/33083182628> |
| [#593](https://github.com/mathorn1973/twist-j/pull/593) | `probes/P-O5-DEDEKIND-FACTORIZATION-1` | <https://github.com/mathorn1973/twist-j/actions/runs/33090790803> |
| [#598](https://github.com/mathorn1973/twist-j/pull/598) | `probes/P-S5-THRESHOLD-COMPLEX-1` | <https://github.com/mathorn1973/twist-j/actions/runs/33098370669> |
| [#602](https://github.com/mathorn1973/twist-j/pull/602) | `probes/P-S5-WALSH-LINK-DECOMPOSITION-1` | <https://github.com/mathorn1973/twist-j/actions/runs/33101110965> |
| [#605](https://github.com/mathorn1973/twist-j/pull/605) | `probes/P-S5-LINK-HOMOLOGY-BASIS-1` | <https://github.com/mathorn1973/twist-j/actions/runs/33103407912> |
| [#607](https://github.com/mathorn1973/twist-j/pull/607) | `probes/P-S5-DYADIC-ANNULUS-EQUIVALENCE-1` | <https://github.com/mathorn1973/twist-j/actions/runs/33106974732> |
| [#609](https://github.com/mathorn1973/twist-j/pull/609) | `probes/P-S5-BILINEAR-ANNULUS-REDUCTION-1` | <https://github.com/mathorn1973/twist-j/actions/runs/33110355849> |
| [#611](https://github.com/mathorn1973/twist-j/pull/611) | `probes/P-S5-GOLDEN-CUTOFF-BAND-1` | <https://github.com/mathorn1973/twist-j/actions/runs/33114387017> |
| [#614](https://github.com/mathorn1973/twist-j/pull/614) | `probes/P-S5-GOLDEN-SHELL-PROFILE-KERNEL-1` | <https://github.com/mathorn1973/twist-j/actions/runs/33154186875> |

---

## 3. Exact Hypothesis Ledger for Conditional and Unconditional Statements

Because $\zeta_F(s) = \zeta(s)L(s,\chi_5)$ and $\zeta_K(s) = \zeta(s)L(s,\chi_5)L(s,\chi)\overline{L(\bar s,\chi)}$
factorize into distinct primitive $L$-functions, analytic hypotheses must be
named at the exact family where they are invoked:

| Premise or external theorem | Exact scope in the $\mathbb Q(\sqrt 5)$ / $\mathrm{CM}_5$ dictionary | What it does NOT cover |
|---|---|---|
| **Unconditional** | All $\mathrm{CM}_5$ polarization bijections, the integer cone $x \ge 1,\ 0 \le y < x$, the logarithm-free sector decision in $\mathbb Z[\phi]$, uniform all-class and primitive sector asymptotics $A(X,I)$ and $A_{\mathrm{prim}}(X,I)$, the $\mathbb R/(2L\mathbb Z) \to \mathbb R/(L\mathbb Z)$ cover, Euler products for $L_F(s,\Xi_m)$, $L_F(s,\Xi_m)/\zeta(2s)$, and $\mathcal D^{(m)}(s)$ on $\Re s > 1$, the Maass cusp-form correspondence (Molin-Page), the global root number $W(\Xi_m) = +1$, the regulator identity $L'(0,\chi_5) = \log\phi$, and the Baier-Roy narrow-sector prime lower bound on $\mathbb R/(L\mathbb Z)$. | Prime-norm sector equidistribution on a single sheet of $\mathbb R/(2L\mathbb Z)$ without odd-mode sieve control, zero-free regions beyond classical de la Vallee Poussin / Vinogradov-Korobov bounds, or square-root summatory cancellation. |
| **External Quasi-RH preprints** (OpenAI, Sept 30 and Oct 5, 2026, `openai/math` commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a`) | Declares zero-freeness in $\Re s > 7/8$ (Sept 30; formalized in Lean 4.34.1 for `DirichletSevenEighths`) and $\Re s > 11/12$ (Oct 5, via Poisson summation, sextic-to-cubic Gauss-Jacobi identities, Kubota metaplectic theta series, and quadratic large sieve) for all Dirichlet $L$-functions and finite-order Hecke $L$-functions over $\mathbb Q(\sqrt{-3})$. By Dedekind factorization this covers $\zeta(s)$, $L(s,\chi_5)$, $\zeta_F(s)$, and $\zeta_K(s)$ in $\Re s > 7/8$. | Does not establish $\Re s > 1/2$ (full RH/GRH), and does not cover the infinite-order Hecke family $L_F(s,\Xi_m)$ ($m \ne 0$) over the real quadratic field $F = \mathbb Q(\sqrt 5)$. |
| **Ordinary $\mathrm{RH}$ for $\zeta(s)$** | Zero-freeness of $\zeta(s)$ in $\Re s > 1/2$; controls the principal scalar channel $\mathcal D_0(s) = 1/\zeta(s)$ ($m_0 = \mu$). | Does not imply $\mathrm{GRH}$ for $L(s,\chi_5)$ or for any nonzero mode $L_F(s,\Xi_m)$, and does not discharge `TRIVIAL-RAPIDITY-EVALUATION-BRIDGE [O]` (which requires a non-circular derivation without a zeta-zero premise). |
| **$\mathrm{GRH}$ for $\zeta_F(s) = \zeta(s)L(s,\chi_5)$** | Combines ordinary $\mathrm{RH}$ for $\zeta(s)$ and $\mathrm{GRH}$ for $L(s,\chi_5)$; ensures the numerator $L(s,\chi_5)$ of $\mathcal D^{(m)}(s)$ has no zeros in $\Re s > 1/2$, making holomorphy of $\mathcal D^{(m)}(s)$ on $\Re s > 1/2$ equivalent to $\mathrm{GRH}$ for $L_F(s,\Xi_m)$. | Does not imply zero-freeness of $L_F(s,\Xi_m)$ for $m \ne 0$. |
| **$\mathrm{GRH}$ for a fixed mode $L_F(s,\Xi_m)$ ($m \ne 0$)** | Ensures $\mathcal D^{(m)}(s) = L(s,\chi_5)/L_F(s,\Xi_m)$ is holomorphic on $\Re s > 1/2$ and gives the fixed-mode smooth summatory bound $\sum_{n\ge 1} m^{(m)}(n) w(n/X) = O_{m,w,\delta}(X^{1/2+\delta})$. | Does not control uniformity as $|m| \to \infty$ or sharp-cutoff sums without explicit conductor tracking. |
| **$\mathrm{GRH}$ for $\{L_F(s,\Xi_m)\}_{m\ne 0}$ with conductor control** | Retains the analytic conductor $Q_m(t) = 5(1 + |t + \mu_m|)(1 + |t - \mu_m|)$ ($\mu_m = \pi m/(2L)$), yielding the proved Borel-Caratheodory smooth bound $(1 + |m|)^{12 C_0/\delta} X^{1/2+\delta}$ (and the imported Littlewood refinement $(1 + |m|)^\varepsilon X^{1/2+\delta}$) across growing mode ranges $|m| \le H(X)$. | Sharp-cutoff summation still requires separate Perron truncation and vertical mean-value control. |

---

## 4. The Regulator Identity as Exact Shared Constant

The fundamental rapidity period $L = \log\phi$ of $F = \mathbb Q(\sqrt 5)$
simultaneously governs the unit lattice shift, the polarization-orbit period
$2L$, the archimedean Hecke spacing $\mu_m = \pi m/(2L)$, the sector density
constant $2L/\sqrt 5$, and the special value of the quadratic Dirichlet
$L$-function at $s = 0$:

$$
\boxed{L'(0,\chi_5) = \log\phi = -2\zeta_F'(0).}
$$

**Exact analytic proof (no numerical evaluation).** The primitive quadratic
character $\chi_5$ modulo $5$ has values $\chi_5(1)=\chi_5(4)=1$,
$\chi_5(2)=\chi_5(3)=-1$, and $\chi_5(0)=0$. Expanding $L(s,\chi_5)$ in
Hurwitz zeta functions $\zeta(s,a) = \sum_{n\ge 0}(n+a)^{-s}$ gives

$$
L(s,\chi_5) = 5^{-s}\Bigl(\zeta(s,\tfrac{1}{5}) - \zeta(s,\tfrac{2}{5})
  - \zeta(s,\tfrac{3}{5}) + \zeta(s,\tfrac{4}{5})\Bigr).
$$

Since $\sum_{a=1}^4 \chi_5(a) = 0$ and $\zeta(0,a) = \tfrac{1}{2} - a$ satisfies
$(1/2 - 1/5) - (1/2 - 2/5) - (1/2 - 3/5) + (1/2 - 4/5) = 0$, we have
$L(0,\chi_5) = 0$. Differentiating at $s = 0$ and applying Lerch's identity
$\zeta'(0,a) = \log\Gamma(a) - \tfrac{1}{2}\log(2\pi)$ (NIST DLMF 25.11.18)
eliminates the $5^{-s}\log 5$ term and the $\tfrac{1}{2}\log(2\pi)$ constants:

$$
L'(0,\chi_5)
= \log\frac{\Gamma(1/5)\Gamma(4/5)}{\Gamma(2/5)\Gamma(3/5)}.
$$

By Euler's reflection formula $\Gamma(z)\Gamma(1-z) = \pi/\sin(\pi z)$ (NIST
DLMF 5.5.3),

$$
L'(0,\chi_5)
= \log\frac{\sin(2\pi/5)}{\sin(\pi/5)}
= \log\bigl(2\cos(\pi/5)\bigr)
= \log\phi = L.
$$

Finally, differentiating $\zeta_F(s) = \zeta(s)L(s,\chi_5)$ at $s = 0$ and
using $L(0,\chi_5) = 0$ together with $\zeta(0) = -1/2$ gives
$\zeta_F'(0) = \zeta(0)L'(0,\chi_5) = -\tfrac{1}{2}\log\phi$. $\square$

---

## 5. Package Contents and Primary Sources

- [`CM5_POLARIZATIONS.md`](CM5_POLARIZATIONS.md): complete proof of the
  polarization-ideal bijection on $B = \operatorname{Jac}(y^2=x^5-1)$, the
  all-prime type-$(1,p)$ count, the $\mathbb R/(2L\mathbb Z)$ rapidity circle,
  the $(a,b)$ and $(x,y)$ Gram and $J$-pullback matrices, the weighted
  generating series $L_F(s,\Xi_m)$, the primitive series $L_F(s,\Xi_m)/\zeta(2s)$,
  the unique integer-cone representative $x \ge 1,\ 0 \le y < x$, the exact
  logarithm-free sector decision in $\mathbb Z[\phi]$, and the uniform sector
  asymptotics $A(X,I)$ and $A_{\mathrm{prim}}(X,I)$.
- [`HECKE_MAASS_BRIDGE.md`](HECKE_MAASS_BRIDGE.md): complete proof of the
  real-quadratic Hecke character normalization and completeness for all
  $m \in \mathbb Z$ (both even $\Psi_h = \Xi_{2h}$ and odd $\Xi_{2h+1}$), the
  Molin-Page Maass cusp-form dictionary on $\Gamma_0(5)$, the global root
  number $W(\Xi_m) = +1$ via Tate local epsilon factors, the exact integral-lift
  quotient $\mathcal D^{(m)}(s) = L(s,\chi_5)/L_F(s,\Xi_m)$, the meromorphic
  pole-order identity, the conditional GRH smooth summatory bound with explicit
  analytic conductor $Q_m(t)$, and the unconditional Baier-Roy narrow-sector
  prime bound on $\mathbb R/(L\mathbb Z)$ and $\mathbb R/(2L\mathbb Z)$.
- [`SHA256SUMS`](SHA256SUMS): SHA-256 digests of the package documents.

### External Primary References

1. C. McMullen, *Complex Analysis on Riemann Surfaces*, Harvard Math 213b lecture
   notes, Section 14, Theorem 14.3:
   <https://people.math.harvard.edu/~ctm/home/text/class/harvard/213b/19/html/home/course/course.pdf>
2. B. Conrad, *Abelian varieties: geometry, parameter spaces, and arithmetic*,
   July 8, 2005, Theorems 1.2.1, 1.3.1, 3.1.3, 3.3.10, 5.1.4, and Section 5.2:
   <https://math.stanford.edu/~conrad/papers/cmchina.pdf>
3. P. Molin and A. Page, *Computing groups of Hecke characters*, ANTS XV (2022),
   `arXiv:2210.02716`, Sections 2.3-2.4 and Section 5.3.2, Proposition 39 and
   Example 40:
   <https://antsmath.org/ANTSXV/papers/ANTS-XV_molin-page.pdf>
4. B. Poonen, *Tate's thesis*, MIT 18.786 lecture notes, Sections 4.3, 4.7, 5.4,
   Theorems 4.18 and 5.22:
   <https://math.mit.edu/~poonen/786/tate.pdf>
5. S. Baier and S. Roy, *A note on the distribution of prime ideals in real
   quadratic fields*, `arXiv:2307.03513v2`, Theorems 1 and 3, equation (6):
   <https://arxiv.org/abs/2307.03513>
6. H. Davenport, *On a principle of Lipschitz*, J. London Math. Soc. 26 (1951),
   179-183.
7. A. V. Sutherland, MIT 18.785 *Number Theory I*, Lecture 20 (Dedekind zeta
   function factorization):
   <https://math.mit.edu/classes/18.785/2019fa/LectureNotes20.pdf>
8. NIST Digital Library of Mathematical Functions, eqs. 25.11.18 and 5.5.3:
   <https://dlmf.nist.gov/25.11>, <https://dlmf.nist.gov/5.5>
9. OpenAI, *The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane $\Re s > 7/8$*
   (Sept 30, 2026) and *The Quasi-Riemann Hypothesis* (Oct 5, 2026), repository
   `openai/math` at `1581d4cbdd69a0faf34b2089614fe2a814316a6a`:
   <https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a>

