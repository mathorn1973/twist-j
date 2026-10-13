# C-QS-COUPLING-VARIANT-AB-DIAGNOSTIC-N: exact predefinition diagnostic of Variant B and Variant A (NON-CANONICAL)

~~~text
NOTE STATE:              DRAFT / NON-CANONICAL
DEFINITION DISPOSITION:  STOP-PREDEFINITION / CONDITIONAL WORKING BASELINE
SCIENTIFIC STATUS:       QUANT-SUBSTRATE [O] UNCHANGED
FORMAL SCIENTIFIC RUN:   NONE
FORMAL PROBE:            NONE
PROBE IDENTIFIER:        NONE RESERVED
PREREGISTRATION:         NONE
FORMAL VERIFIER:         NONE
SUPPORTING CHECKER:      NON-FORMAL / LIMITED COVERAGE (section 0.1)
COORDINATION LOCK:       NONE CLAIMED
RELATED ISSUE:           #689 (context only; its lock is not extended)
OWNER ROW:               QUANT-SUBSTRATE [O]
THIS NOTE ACTION LAYER:  NOT_APPLICABLE
PROPOSED GATE PATH:      L1 -> L5 -> L6
CANON CHANGE:            NONE
REGISTRY CHANGE:         NONE
NORMATIVE CHANGE:        NONE
GATE CHANGE:             NONE
STATUS MOVE:             NONE
~~~

## 0. Source authority and non-canonical disposition

~~~text
repository:                mathorn1973/twist-j
audit/main commit:         5f54015ed8361e3a64cb10894397020ddfadd104
Public Canon:              v101
Canon state:               ACTIVE
tag:                       canon-v101
content commit:            421a4ec1daf07c04d19022c1ee219607e83c09a8
Canon SHA-256:             b83a99feccac173bd3c9c5851c5874ca27cbd135f71d136d793b45f86c8a87f7
Canon bytes:               992352
owner:                     QUANT-SUBSTRATE [O]
related issue:             #689 (not a lock for these files)
predecessor note:          notes/canon/C-QS-COUPLING-REV4-TYPED-PREDEFINITION-N.md
predecessor commit:        64dc0ed8812074ca606413d2bf609c512203e061
predecessor SHA-256:       78127d08f31c6bf69145e47d4cd5a8713f7777df9f62b38b33b66044daa1697c
this file:                 notes/canon/C-QS-COUPLING-VARIANT-AB-DIAGNOSTIC-N.md
companion checker:         notes/canon/C-QS-COUPLING-VARIANT-AB-CHECKER.py
formal pin/run/result:     ABSENT / NOT AUTHORIZED / ABSENT
~~~

This non-canonical note records the exact predefinition diagnostic and conditional working baseline for **Variant B** (paired excursion automaton) and **Variant A** (the original wall-based Rev 3 proposal) following [C-QS-COUPLING-REV4-TYPED-PREDEFINITION-N.md](https://github.com/mathorn1973/twist-j/blob/64dc0ed8812074ca606413d2bf609c512203e061/notes/canon/C-QS-COUPLING-REV4-TYPED-PREDEFINITION-N.md). The accompanying [checker](C-QS-COUPLING-VARIANT-AB-CHECKER.py) audits selected exact identities over $\mathbb{Q}(i)$ and $\mathbb{Q}(\zeta_5)$ using `Fraction`, together with the explicitly bounded finite-step comparisons listed below. Imported Canon theorems and mathematical arguments in this note are separate evidence; the checker is not a complete proof of the note. Its present definition disposition remains `STOP-PREDEFINITION`.


The Canon tuple above identifies the source snapshot, not approval or a formal
pin of these two files. [Issue #689](https://github.com/mathorn1973/twist-j/issues/689)
is related context only. Its [owner disposition](https://github.com/mathorn1973/twist-j/issues/689#issuecomment-5468979652)
locks exactly the original Rev 4 branch and note path, with definition-only
scope; this diagnostic neither inherits nor extends that lock. The checker is
a non-formal supporting calculation and claims no verifier or evaluation
authority under that issue. No probe, gate, owner adoption, or scientific status is created.

### 0.1 Evidence and checker coverage

The section numbers and `COVERAGE-*` comments below refer to the companion
checker. A successful run establishes only its executed assertions.

| Evidence | What is checked | Boundary |
|---|---|---|
| Sections 1–4, `COVERAGE-HISTORY-FINITE` | Exact matrix arithmetic and history/read comparisons for all 24 nontrivial couplings, $N=2,\ldots,9$, with separate $N=1$ and $N=3$ witnesses | These finite checks do not alone prove all-$N$ operator identities. |
| Section 5, `COVERAGE-SCALAR-SUMS-ALL-N` | Initial values and symbolic forward differences for the two B2 scalar sum formulas | This is an all-$N$ induction for the sums; their identification with the automaton and the limits also use the derivation in section 4 below. |
| Sections 6–7 | Exact orbit, Fourier, determinant and closed return-coefficient checks | These do not select a physically admissible orbit or an AlphaMap. |
| Section 8, `COVERAGE-PAIRED-FINITE-JETS` | Paired-vertex comparisons for $N=2,\ldots,6$ and rational first-jet composition | The physical response and alpha dictionaries remain premises. |
| Section 9, `COVERAGE-RETURN-OPPOSITE-FINITE` and `COVERAGE-SUPPLIED-QUOTIENT` | Return/skew-Hermitian matrix identities; opposite-branch comparisons for $N=2,\ldots,6$; quotient arithmetic for supplied $(v,s)$ | No canonical pair of angle readings is derived. The general symbolic $\Pi$ formula is the written quotient derivation in section 8.2. |
| Section 10, `COVERAGE-H-PROJECTION-ARITHMETIC` | Selected $H$-metric evaluations and projection of a supplied closed return vector | Projector idempotence, $H$-self-adjointness and all-step evolution with the modified projector are not independently tested by this section. |
| Section 11, `COVERAGE-WALL-IMPORTED-COEFFICIENTS` | Galois/root index map and rational consequences of the imported wall formula | The analytic wall and principal-branch theorems are Canon premises, not re-proved here. |
| Section 11, `COVERAGE-J-SCALAR-PRODUCTS` | Exact scalar products $J\bar J$, $J^2$ and their conjugations | Cancellation in a dressed stream and the adjoint vertex rule follow from the written algebra; no dressed automaton is run. |

The germ-order obstruction, nonuniform normalization limit, finite-propagator
limitation and physical interpretation boundaries are mathematical arguments
or scope statements in the note, not additional executed checker tests.
`tools/check_gate_contract.py` validates `canon/NORMATIVE.tsv` and
`canon/GATES.tsv`; its success does not validate this note or extend issue #689.

---

## 1. Module, Step Operator, and Return Matrix Elements

Let $M = M_D \otimes_{\mathbb{Q}(i)} R_5 \cong \mathbb{Q}(i)^{10}$ with frozen basis $\{f_\sigma \otimes e_j\}_{\sigma\in\{0,1\},\,j\in\mathbb{Z}_5}$, free step $D_{\rm rest} \otimes 1$ ($D_{\rm rest} = I_2 + 2i X$, $D_{\rm rest} v_\pm = (1\pm 2i)v_\pm$), and chiral shift coupling
\[
W^{(Z)}_{a,b} = Q_0 \otimes E_a + Q_1 \otimes E_b = I_2 \otimes \frac{E_a + E_b}{2} + V_{a,b},
\qquad
V_{a,b} = Z \otimes \frac{E_a - E_b}{2},
\qquad (a,b) \in I_{\rm nt} = \mathbb{Z}_5^2 \setminus \{(0,0)\}.
\]
With reference pre-state $u_0 = v_+ \otimes e_0$ ($\|u_0\|^2 = 2$) and register projectors $\Pi_{e_0} = I_2 \otimes |e_0\rangle\langle e_0|$, $\Pi_{\neq 0} = I_{10} - \Pi_{e_0}$:

1. **Bilinear two-vertex return matrix element:**
   On all of $\mathbb{Z}_5^2$,
   \[
   s_{\rm bilin}(a,b)
   = \frac{\langle u_0,\, \Pi_{e_0} V_{a,b} \Pi_{\neq 0} V_{a,b} u_0\rangle}{\|u_0\|^2}
   = -\frac{1}{2}\bigl(\delta_{a+b,0} - \delta_{a,0}\delta_{b,0}\bigr).
   \]
   On $I_{\rm nt} = \mathbb{Z}_5^2 \setminus \{(0,0)\}$, this simplifies to
   \[
   \boxed{s_{\rm bilin}(a,b) = -\frac{1}{2}\,\delta_{a+b,0}.}
   \]
2. **Hermitian one-vertex intermediate weight:**
   On $I_{\rm nt}$,
   \[
   s_{\rm herm}(a,b)
   = \frac{\|\Pi_{\neq 0} V_{a,b} u_0\|^2}{\|u_0\|^2}
   = \frac{1}{4}\bigl(2 - \delta_{a,0} - \delta_{b,0} - 2\delta_{a,b}\bigr).
   \]

---

## 2. Typed Block Isomorphism and Emission-Indexed History Space $H_N$

Let $M_{\rm pre}, M_{\rm exc}, M_{\rm post}$ be typed copies of $M = \mathbb{Q}(i)^{10}$, equipped with the explicit basis-preserving **$\mathbb{Q}(i)$-linear isomorphism**
\[
\tau_{\rm post\to pre}: M_{\rm post} \xrightarrow{\;\sim\;} M_{\rm pre},
\qquad
f_\sigma^{\rm (post)} \otimes e_j \longmapsto f_\sigma^{\rm (pre)} \otimes e_j.
\]
Define $D_{e_0} = (D_{\rm rest}\otimes 1)\Pi_{e_0}$, $D_{\neq 0} = \Pi_{\neq 0}(D_{\rm rest}\otimes 1)\Pi_{\neq 0}$, $\operatorname{Emit}_{a,b} = \Pi_{\neq 0}(D_{\rm rest}\otimes 1)V_{a,b}$, and $\operatorname{Reabs}_{a,b} = \Pi_{e_0}(D_{\rm rest}\otimes 1)V_{a,b}$.

At tick $N \ge 1$, the completed-excursion history space is
\[
H_N = \bigoplus_{i=1}^{N-1} M_{{\rm post},i},
\qquad
h_N = \bigl(\Psi_{1,i}(N)\bigr)_{i=1}^{N-1} \in H_N,
\]
where $i \in \{1,\dots,N-1\}$ indexes the emission tick from $M_{\rm pre}$ into $M_{{\rm exc},i}$:
\[
\Psi_{1,i}(N) =
\begin{cases}
(D_{e_0})^{N-i-1}\,\operatorname{Reabs}_{a,b}\,\operatorname{Emit}_{a,b}\,(D_{e_0})^{i-1} u_0 & \text{(mode B1: }\ell=1\text{)},\\[4pt]
\displaystyle\sum_{\ell=1}^{N-i} (D_{e_0})^{N-i-\ell}\,\operatorname{Reabs}_{a,b}\,(D_{\neq 0})^{\ell-1}\,\operatorname{Emit}_{a,b}\,(D_{e_0})^{i-1} u_0 & \text{(mode B2: all }\ell\ge 1\text{)}.
\end{cases}
\]
*(Whether the emission index $i$ is a mathematical history grading or a physical record remains an explicit open choice under `STOP-PREDEFINITION`.)*

---

## 3. Two Declared History Readings ($S_N, B_N$) and Reference-Branch Normalization

Given $\Psi_0(N) = (D_{e_0})^N u_0 = (1+2i)^N u_0$ with $\|\Psi_0(N)\|^2 = 5^N \|u_0\|^2$, define two explicit maps on $H_N$:
1. **Coherent summation map $S_N: H_N \to M_{\rm pre}$:**
   \[
   S_N(h_N) = \sum_{i=1}^{N-1} \tau_{\rm post\to pre}\bigl(\Psi_{1,i}(N)\bigr),
   \qquad
   A_N = \frac{\langle \Psi_0(N),\, S_N(h_N)\rangle}{\|\Psi_0(N)\|^2}.
   \]
2. **Emission-resolved quadratic weight normalized by the reference branch $B_N: H_N \to \mathbb{Q}$:**
   \[
   B_N(h_N) = \frac{\sum_{i=1}^{N-1} \|\Psi_{1,i}(N)\|^2}{5^N \|u_0\|^2}.
   \]

- **Distinction between $W_{\rm coh}(N)$ and $B_N(h_N)$:** The unindexed post-block stores only $S_N(h_N)$. Define
  \[
  W_{\rm coh}(N) = \frac{\|S_N(h_N)\|^2}{5^N \|u_0\|^2}.
  \]
  These readings are not generally equal. At $N=2$ on the antipodal orbit, both equal $1/4$ in either mode. At $N=3$ on $\mathcal{O}_{u,-u}$ in mode B2, $W_{\rm coh}(3) = \frac{13}{20} \neq B_3(h_3) = \frac{9}{20}$.
- **Reference-branch vs total-state normalization:** Already at $N=1$,
  \[
  \frac{\|\Psi_0(1)\|^2 + \|\Psi_{\rm exc}(1)\|^2}{5\|u_0\|^2} = 1 + s_{\rm herm}(a,b) = \frac{3}{2}
  \quad\text{on }\mathcal{O}_{u,-u}.
  \]
  Hence $B_N(h_N)$ and $c_w = \lim_{N\to\infty} \frac{B_N(h_N)}{N}$ are strictly **quadratic weights normalized by the reference branch**, not total-state probabilities.

---

## 4. Exact All-$N$ Identities and Conditional Ratios on $\mathcal{O}_{u,-u}$

With $q = \frac{1-2i}{1+2i} = -\frac{3}{5}-\frac{4}{5}i$ ($\frac{q}{1-q} = -\frac{1}{2}-\frac{1}{4}i$, $\left|\frac{q}{1-q}\right|^2 = \frac{5}{16}$), exact induction in $\mathbb{Q}(i)[N, q^N, \bar{q}^N]$ holds for all $N \ge 1$:
- **B1:** $A_N^{\rm (B1)} = (N-1)\,s_{\rm bilin}(a,b)\,q$, $B_N^{\rm (B1)}(h_N) = (N-1)\,s_{\rm bilin}(a,b)^2$.
- **B2:** $A_N^{\rm (B2)} = s_{\rm bilin}(a,b)\left[\frac{q}{1-q}\,N - \frac{q(1-q^N)}{(1-q)^2}\right]$, $B_N^{\rm (B2)}(h_N) = \frac{5}{16}\,s_{\rm bilin}(a,b)^2\left[2(N-1) - 2\operatorname{Re}\frac{q(1-q^{N-1})}{1-q}\right]$.

The all-$N$ reduction uses the specified recurrence: for each completed path
with $j-i=\ell$, the two coin flips give
$(1+2i)^{N-\ell}(1-2i)^\ell s_{\rm bilin}u_0$.
Summing these paths gives $A_N$; summing their coherent amplitudes within each
emission slot before taking its norm gives the displayed $B_N$.
The scalar induction in checker section 5 audits the resulting B2 sums.
The bounds $|q|=1$ and $|1-q^N|\le2$, with $q\ne1$, make their remainders
bounded, proving the following limits after division by $N$.

Setting $\rho_1 = \lim_{N\to\infty} \frac{A_N}{N}$, $x = +\operatorname{Im}\rho_1$, and $c_w = \lim_{N\to\infty} \frac{B_N(h_N)}{N}$:

| Antipodal Orbit $\mathcal{O}_{u,-u}$ ($s_{\rm bilin}=-1/2$) | $\rho_1$ | $x = \operatorname{Im}\rho_1$ | $c_w = \lim_{N\to\infty} B_N/N$ | Conditional Ratio $5x/c_w$ |
|---|---:|---:|---:|---:|
| **B1** ($\ell=1$) | $\frac{3}{10}+\frac{2}{5}i$ | $\frac{2}{5}$ | $\frac{1}{4}$ | **$8$** |
| **B2** (all $\ell\ge 1$) | $\frac{1}{4}+\frac{1}{8}i$ | $\frac{1}{8}$ | $\frac{5}{32}$ | **$4$** |

---

## 5. Sharply Delimited Obstruction for the Natural `AlphaMap`

Suppose the completed excursion history enters with perturbation parameter $t$ as $h_N(t) = t h_N$. Under the A6 conversion and the natural identification of $\alpha(t)$ with the reference-normalized quadratic weight rate of $h_N(t)$:
\[
\alpha(t) = \lim_{N\to\infty} \frac{B_N(t h_N)}{N} = c_w t^2,
\qquad
a_e(t) - a_e(0) = \frac{5x}{2\Pi}\,t + O(t^2).
\]
On the antipodal orbit ($c_w > 0$, $x \neq 0$), eliminating $t$ yields
\[
\boxed{a_e(\alpha) - a_e(0) = \pm \frac{5x}{2\Pi\sqrt{c_w}}\sqrt{\alpha} + O(\alpha).}
\]
- Restricting to $t \ge 0$ removes the $\pm$ sign ambiguity, but **does not remove the non-analytic $\sqrt{\alpha}$ term**, failing to produce the required regular Schwinger germ $a_e(\alpha) = a_e(0) + K\alpha + O(\alpha^2)$.
- Because $(a_e(t)-a_e(0), \alpha(t)) = (\text{const}\cdot t^1 + O(t^2),\, c_w t^2)$ has unequal leading jet orders ($1$ vs $2$), this obstruction is invariant under any regular invertible reparametrization $t = \phi(u)$ ($\phi(0)=0, \phi'(0)\neq 0$) and under multiplication of either branch by any non-zero constant ($J\bar{J}$, $\pi$, or normalization factors).
- Setting $\alpha(t) = c_w t$ would require adopting a new, separate `AlphaMap` postulate rather than deriving $\alpha$ as the quadratic weight $B_N(t h_N)$.
- Achieving a common perturbative order without an ad-hoc linear `AlphaMap` is not automatic: one possible repair is matching a **two-vertex virtual return phase of order $\varepsilon^2$** against a **one-vertex emission weight of order $\varepsilon^2$**, which alters the channel definition and requires its own independent justification (detailed in Section 6 below).

---

## 6. Paired Vertex-Parametrized Variant (`NON-CANONICAL` / `STOP-PREDEFINITION`)

### 6.1 Single Automaton with Real Vertex Parameter $\varepsilon$

Let $\varepsilon$ be a formal real parameter ($\bar{\varepsilon} = \varepsilon$) placed on every vertex insertion:
\[
\operatorname{Emit}_{a,b} \longmapsto \varepsilon\operatorname{Emit}_{a,b},
\qquad
\operatorname{Reabs}_{a,b} \longmapsto \varepsilon\operatorname{Reabs}_{a,b}.
\]
Denoting the reference state by $r_n \in M_{\rm pre}$, the active excursion slots by $e_{n,i} \in M_{{\rm exc},i}$ ($1 \le i \le n$), and the completed excursion slots by $p_{n,i} \in M_{{\rm post},i}$ ($1 \le i < n$), the recurrence from $r_0 = u_0$ (with missing components zero) is:
\[
\begin{aligned}
r_n &= D_{e_0} r_{n-1},\\
e_{n,n}(\varepsilon) &= \varepsilon\operatorname{Emit}_{a,b}\,r_{n-1},\\
e_{n,i}(\varepsilon) &= M_{\rm mid}\,e_{n-1,i}(\varepsilon) \qquad (1 \le i < n),\\
p_{n,i}(\varepsilon) &= D_{e_0}\,p_{n-1,i}(\varepsilon) + \varepsilon\operatorname{Reabs}_{a,b}\,e_{n-1,i}(\varepsilon) \qquad (1 \le i < n),
\end{aligned}
\]
where $M_{\rm mid} = 0$ for **B1** and $M_{\rm mid} = D_{\neq 0}$ for **B2**.

- The reference branch $r_N = \Psi_0(N)$ is independent of $\varepsilon$ ($O(\varepsilon^0)$), with $\|r_N\|^2 = 5^N \|u_0\|^2$.
- Each active component $e_{n,i}(\varepsilon) = \varepsilon e_{n,i}(1)$ is homogeneous of order $\varepsilon^1$.
- The completed excursion history $h_N(\varepsilon) = (p_{N,i}(\varepsilon))_{i=1}^{N-1} = \varepsilon^2 h_N(1)$ is homogeneous of order $\varepsilon^2$.

### 6.2 Declared Reading of Emissions at Creation ($\chi_i, F_N, \alpha_N$)

Define the amplitude newly emitted at tick $i \in \{1,\dots,N\}$:
\[
\chi_i(\varepsilon) := e_{i,i}(\varepsilon) = \varepsilon\operatorname{Emit}_{a,b}\,r_{i-1}.
\]
Since both eigenvalues $1 \pm 2i$ of $D_{\rm rest}$ have squared modulus $5$,
\[
\frac{\|\chi_i(\varepsilon)\|^2}{5^i \|u_0\|^2} = \varepsilon^2 s_{\rm herm}(a,b) \qquad \forall i \ge 1.
\]
The cumulative reference-normalized emission weight and its per-tick average are:
\[
F_N(\varepsilon) := \sum_{i=1}^N \frac{\|\chi_i(\varepsilon)\|^2}{5^i \|u_0\|^2} = N \varepsilon^2 s_{\rm herm}(a,b),
\qquad
\alpha_N(\varepsilon) := \frac{F_N(\varepsilon)}{N} = s_{\rm herm}(a,b)\,\varepsilon^2.
\]
- **Distinction from final intermediate occupancy:** $F_N(\varepsilon)$ is a newly declared reading of emissions at their creation tick $i$, whereas $\sum_{i=1}^N \|e_{N,i}(\varepsilon)\|^2 / (5^N \|u_0\|^2)$ measures the final-step intermediate occupancy at tick $N$. These two readings are **not generally identical**: in **B2**, their values coincide:
  \[
  \frac{\sum_{i=1}^N \|e_{N,i}(\varepsilon)\|^2}{5^N \|u_0\|^2} = N \varepsilon^2 s_{\rm herm}(a,b) = F_N(\varepsilon),
  \]
  whereas in **B1** ($M_{\rm mid} = 0$), only the last slot $e_{N,N}$ survives at tick $N$, so they differ for all $N \ge 2$ and $\varepsilon^2 s_{\rm herm}(a,b) \neq 0$ (giving $s_{\rm herm}\varepsilon^2$ instead of $N s_{\rm herm}\varepsilon^2$). Nor is $F_N(\varepsilon)$ a total-state normalized probability.

### 6.3 Common First Jet in $\tau = \varepsilon^2$, Coefficient Ring, and Algebraic Chain Rule

Set $\tau = \varepsilon^2$. First perform reference normalization and first-jet extraction in $\mathbb{Q}[\tau]/(\tau^2)$ at finite $N$, and only then take the $N \to \infty$ limit of the jet coefficients:
\[
\theta_N(\tau) := \frac{1}{N}\operatorname{Im}\log\bigl(1 + \tau A_N\bigr) \equiv \tau\,\frac{\operatorname{Im} A_N}{N} \pmod{\tau^2},
\qquad
\alpha_N(\tau) = s_{\rm herm}(a,b)\,\tau.
\]
Taking $N \to \infty$ on the $\tau^1$ coefficients yields first jets over $\mathbb{Q}$:
\[
\theta(\tau) = x\,\tau \pmod{\tau^2} \in \mathbb{Q}[\tau]/(\tau^2),
\qquad
\alpha(\tau) = s_{\rm herm}(a,b)\,\tau \pmod{\tau^2} \in \mathbb{Q}[\tau]/(\tau^2).
\]
For any coupling with $s_{\rm herm}(a,b) > 0$, eliminating $\tau = s_{\rm herm}(a,b)^{-1}\alpha \pmod{\alpha^2}$ and applying the Phase B A6 conversion gives the rational first-jet identity in $\mathbb{Q}[\alpha]/(\alpha^2)$ (verified by `Jet1` in [C-QS-COUPLING-VARIANT-AB-CHECKER.py](C-QS-COUPLING-VARIANT-AB-CHECKER.py)):
\[
\Pi\bigl[a_e(\alpha) - a_e(0)\bigr] \equiv \frac{5x}{2 s_{\rm herm}(a,b)}\,\alpha \pmod{\alpha^2} \in \mathbb{Q}[\alpha]/(\alpha^2),
\]
and the full first-jet chain rule in $F_\Pi[\alpha]/(\alpha^2)$:
\[
\boxed{a_e(\alpha) - a_e(0) \equiv \frac{5x}{2\Pi s_{\rm herm}(a,b)}\,\alpha \pmod{\alpha^2} \in F_\Pi[\alpha]/(\alpha^2).}
\]

### 6.4 Non-Commutativity of Limits (Part of the Definition)

On the antipodal orbit, $A_N = N\rho_1 + O(1)$ with $\rho_1 \neq 0$. At fixed $\tau > 0$:
\[
\lim_{N\to\infty} \frac{\arg(1 + \tau A_N)}{N} = 0,
\qquad\text{whereas}\qquad
\lim_{N\to\infty} \left.\frac{\partial}{\partial\tau}\frac{\arg(1 + \tau A_N)}{N}\right|_{\tau=0} = x \neq 0.
\]
Thus $\left.\frac{\partial}{\partial\tau}\right|_{\tau=0}$ and $\lim_{N\to\infty}$ do not commute; the automaton defines the stationary first-order perturbative coefficient, not a full finite-coupling stationary response.

### 6.5 Complete Classification of the Paired Reading Across $I_{\rm nt}$

| Orbit | Size | $s_{\rm bilin}$ | $s_{\rm herm}$ | $5x_{\rm B1}/s_{\rm herm}$ | $5x_{\rm B2}/s_{\rm herm}$ |
|---|---:|---:|---:|---:|---:|
| $\mathcal{O}_{0,u}$ | $4$ | $0$ | $1/4$ | $0$ | $0$ |
| $\mathcal{O}_{u,0}$ | $4$ | $0$ | $1/4$ | $0$ | $0$ |
| $\mathcal{O}_{u,u}$ | $4$ | $0$ | $0$ | undefined (`STOP`) | undefined (`STOP`) |
| $\mathcal{O}_{u,2u}$ | $4$ | $0$ | $1/2$ | $0$ | $0$ |
| $\mathcal{O}_{u,3u}$ | $4$ | $0$ | $1/2$ | $0$ | $0$ |
| $\mathcal{O}_{u,-u}$ | $4$ | $-1/2$ | $1/2$ | **$4$** | **$5/4$** |

- **All 24 couplings in $I_{\rm nt}$:** $4$ couplings ($\mathcal{O}_{u,u}$) have a zero denominator $s_{\rm herm} = 0$ (`STOP`).
- **20 off-diagonal couplings ($a \neq b$):** $2$ distinct coefficient values remain in each mode ($\{0, 4\}$ in B1; $\{0, 5/4\}$ in B2 — `NONUNIQUE` without an additional selector).
- **Antipodal restriction ($\mathcal{O}_{u,-u}$):** Conditional singletons **$4$** (B1) and **$5/4$** (B2).

---

## 7. Interim Delimitation on Variant B's Paired Automaton (`STOP-PREDEFINITION`)

> Dokončená exkurzní váha při přirozeném `AlphaMap` vykazuje nesoulad vedoucích řádů. Spárování dvouvrcholové fáze s jednovrcholovou emisní vahou tento nesoulad odstraňuje a při deklarované limitě koeficientů dává podmíněné antipodální poměry $4$ a $5/4$. Fyzická identifikace emisního čtení s $\alpha$, převod A6 a výběr přípustné třídy nejsou tímto výpočtem odvozeny.

- The unequal values $4 \neq 1$ and $5/4 \neq 1$ do **not** imply the necessity of any specific additional canonical structure; they establish only that the stated models with the stated readings do not produce the target ratio. Any additional or alternative structure must be justified by an independent principle — the mere need to obtain a factor of $4/5$ (or $1/4$) is not such a principle.

---

## 8. Exact Analysis of `ResponseLaw` A6 and Canonical Reference Audit (`STOP-PREDEFINITION`)

### 8.1 Corrected Public Canon v101 Reference Map

- **Tree electron moment (`ELECTRON-G-*`):**
  - `ELECTRON-G-TREE [D]`, supported by `ELECTRON-G-RATIO [T]` and `ELECTRON-G-DOUBLE-COVER [T]` ([canon/CANON.md](https://github.com/mathorn1973/twist-j/blob/5f54015ed8361e3a64cb10894397020ddfadd104/canon/CANON.md#L15681-L15688), [reproduce/photon-electron/verify.py](https://github.com/mathorn1973/twist-j/blob/5f54015ed8361e3a64cb10894397020ddfadd104/reproduce/photon-electron/verify.py#L506-L647)): defines the tree reading as the ratio of the vertex flux to the spinor half-angle on the $(5,10)$ double-cover pair ($X^5 = 1$ on the fiber, $R^5 = -I, R^{10} = I$ on the spinor, pivot $1 - J = e^{-i\pi/5}$):
    \[
    g_e(0) = \frac{2\pi/5}{\pi/5} = 2,
    \]
    and explicitly leaves the first-order correction open.
  - `QUANT-SCHWINGER-TARGET [T]` ([canon/CANON.md](https://github.com/mathorn1973/twist-j/blob/5f54015ed8361e3a64cb10894397020ddfadd104/canon/CANON.md#L15689-L15696)): proves $J\bar{J}/\mathcal{Q} = 1/(2\pi)$ from `J-MODULUS-CHORD [T]` and `BRIDGE-DEFECT [T]`, fixing only the target scalar without identifying it with $[\alpha^1]((g_e(\alpha)-2)/2)$.
- **Dirac step and Gaussian rest coin (`DIRAC-*`):**
  - `DIRAC-STEP [D]` on `DIRAC-STEP-THEOREMS [T]` ([canon/CANON.md](https://github.com/mathorn1973/twist-j/blob/5f54015ed8361e3a64cb10894397020ddfadd104/canon/CANON.md#L15722-L15727), [reproduce/dirac-ladder/verify.py](https://github.com/mathorn1973/twist-j/blob/5f54015ed8361e3a64cb10894397020ddfadd104/reproduce/dirac-ladder/verify.py#L453-L530)): $D_J(m_D) = S(I + i m_D X)$ with $\det = 1 + m_D^2 = 5$ for the electron; the unitarized rest coin $D_{\rm rest}/\sqrt{5}$ has **infinite order**, distinct from the order-$10$ spinor rotation $R$ of `ELECTRON-G-DOUBLE-COVER [T]`.
  - `CHECKERBOARD-GAUSS-TOWER [T]` ([canon/CANON.md](https://github.com/mathorn1973/twist-j/blob/5f54015ed8361e3a64cb10894397020ddfadd104/canon/CANON.md#L15732-L15738)): $(1+2i)^n$ recursion with norm $5^n$.
- **Born dictionary and $\alpha$ register (`MEASURE-*`, `ALPHA-*`):**
  - `MEASURE-BORN-VERB [D]`, `KERNEL-CELL-DICTIONARY [D]`, `BORN-FACE-WEIGHTS [T]`.
  - `ALPHA-FORM [D]`, `ALPHA-VALUE-DIGITS [C]`, `ALPHA-SEED [T]`, `ALPHA-PREFACTOR-UNIFICATION [T]` ([canon/CANON.md](https://github.com/mathorn1973/twist-j/blob/5f54015ed8361e3a64cb10894397020ddfadd104/canon/CANON.md#L14243-L14276)): `ALPHA-SEED [T]` establishes the dimensionless trace seed $\alpha_* = 1/p$ on the cyclotomic Galois-trace Gram $G = pI - \mathbf{1}\mathbf{1}^T$ (not physical $\alpha^{-1} = 137$).
  - *(Note: `PARTICLE-MOMENTS`, `ALPHA-INV-0`, and `PHOTON-ELECTRON` are not claim identifiers in `canon/REGISTRY.tsv`.)*

### 8.2 First-Order Differential Law of the Ratio Reading $g_e(\tau) = \theta_v(\tau)/\theta_s(\tau)$

Let $\theta_v(\tau)$ and $\theta_s(\tau)$ denote the perturbed per-tick vertex flux angle and spinor half-angle in $F_\Pi[\tau]/(\tau^2)$:
\[
\theta_v(\tau) = \frac{2\Pi}{5} + v\tau \pmod{\tau^2},
\qquad
\theta_s(\tau) = \frac{\Pi}{5} + s\tau \pmod{\tau^2}.
\]
If the tree ratio reading `ELECTRON-G-TREE [D]` continues to first order as $g_e(\tau) = \theta_v(\tau)/\theta_s(\tau)$, then in $F_\Pi[\tau]/(\tau^2)$:
\[
g_e(\tau)
= \frac{\frac{2\Pi}{5} + v\tau}{\frac{\Pi}{5} + s\tau}
\equiv 2 + \frac{5}{\Pi}(v - 2s)\,\tau \pmod{\tau^2},
\qquad
a_e(\tau) = \frac{g_e(\tau) - 2}{2} \equiv \frac{5}{2\Pi}(v - 2s)\,\tau \pmod{\tau^2},
\]
so that
\[
\boxed{a_e'(0) = \frac{5}{2\Pi}(v - 2s) = \frac{5}{2\Pi}\bigl(\theta_v'(0) - 2\theta_s'(0)\bigr).}
\]
Consequently, the proposed law $\operatorname{ResponseLaw}_{A6}(x) = \frac{5x}{2\Pi}$ holds **if and only if**
\[
\boxed{x = \theta_v'(0) - 2\theta_s'(0) = v - 2s.}
\]

- **Branch 1 ($v = x,\, s = 0$):** Perturbation shifts only the vertex angle while the spinor half-angle remains locked at $\Pi/5$; this yields $a_e'(0) = \frac{5x}{2\Pi}$ (the proposed A6).
- **Branch 2 ($v = x,\, s = x/2$):** Perturbation preserves the double-cover ratio $\theta_v(\tau) = 2\theta_s(\tau)$ at first order; this yields $a_e'(0) = 0$.
- Both branches share the exact same tree value $g_e(0) = 2$; the tree value and the 5-tick period alone do not decide between them.

### 8.3 Register Return Operator, Auxiliary Coin Tangent, and Conditional Diagnosis of A6

1. **Register return operator vs projected return channel:**
   For an antipodal coupling $(u,-u)$ ($u \in \mathbb{Z}_5^\times$), let
   \[
   T = \frac{E_u - E_{-u}}{2}, \qquad P_0 = |e_0\rangle\langle e_0|, \qquad Q = I_5 - P_0.
   \]
   Then on $R_5$:
   \[
   T Q T\,e_0 = \frac{e_{2u} + e_{-2u} - 2e_0}{4},
   \qquad
   P_0 T Q T P_0 = -\frac{1}{2} P_0.
   \]
   The two mixed products $E_u E_{-u} + E_{-u} E_u = 2 I_5$ produce $-2e_0/4 = -\frac{1}{2}e_0$, while the unmixed shifts $(e_{2u} + e_{-2u})/4$ are removed only by the final projection $P_0$. Thus the completed channel projected back to $e_0$ returns with the real register coefficient $-1/2$; this does **not** make $T Q T$ the identity on $R_5$ and does **not** imply $\theta_v'(0) = 0$. Furthermore, $e_0$ is not an eigenvector of $E_1$ and $[P_0, E_1] \neq 0$, so replacing the static register projection by a free shift $E_1$ alters the dynamics and does not preserve the original formulas for $x_B$.

2. **Auxiliary coin return jet and half-difference tangent:**
   When the initial coin branch is $v_- = f_0 - f_1$ instead of $v_+ = f_0 + f_1$, the eigenvalue ratio $q = \frac{1-2i}{1+2i}$ is replaced by $\bar{q} = \frac{1+2i}{1-2i}$, so that
   \[
   A_{N,-} = \overline{A_{N,+}}.
   \]
   On the 2-dimensional coin space $M_D = \operatorname{span}\{v_+, v_-\}$ (with $X v_\pm = \pm v_\pm$), the relative return first-jet operator is therefore
   \[
   I_2 + \tau\bigl(\operatorname{Re} A_{N,+}\,I_2 + i\operatorname{Im} A_{N,+}\,X\bigr) \pmod{\tau^2}.
   \]
   Under the declared order of operations (first-jet extraction at finite $N$, division of the phase tangent by $N$, followed by $N \to \infty$), the two coin eigenphases have tangents $+x_B$ and $-x_B$, and the **tangent of their half-difference is $x_B$**. Identifying this auxiliary coin half-difference tangent (on the infinite-order rest coin $D_{\rm rest}$) with a canonical angle reading of the $(5,10)$ double cover requires an independent justification.

3. **Closed conditional diagnosis of A6:**
   > Při přijatém pokračování $g_e = \theta_v/\theta_s$ platí A6 právě tehdy, když $x_B = \theta_v'(0) - 2\theta_s'(0)$. Varianta B vypočítává pomocný mincovní tangent $x_B$, ale dosud neurčuje dvě kanonická úhlová čtení ani tuto identitu. Možnost III je kandidátní realizace, nikoli její nezávislé odvození.

---

## 9. Analysis of `AlphaMap`, Skew-Hermitian Cancelation, and Calibration Factor $\lambda$ (`STOP-PREDEFINITION`)

### 9.1 Separation of the Proved Emission Functional from Physical Calibration

Separate the proved per-tick creation-time emission functional of the paired automaton from its physical calibration into `AlphaCarrier` $= F_\Pi[\alpha]/(\alpha^2)$:
\[
\alpha_{\rm em}(\tau) = s_{\rm herm}(a,b)\,\tau,
\qquad
\alpha(\tau) = \lambda\,s_{\rm herm}(a,b)\,\tau + O(\tau^2),
\]
where $\lambda \in F_\Pi^\times$ is the calibration factor of `AlphaMap`: $\alpha = \lambda\,\alpha_{\rm em} \pmod{\tau^2}$. Conditionally on A6 ($a_e'(0) = \frac{5x_B}{2\Pi}$) and $s_{\rm herm}(a,b) > 0$, the first-order Schwinger coefficient is:
\[
\boxed{K(\lambda) = \frac{5 x_B}{2\Pi\,\lambda s_{\rm herm}(a,b)}.}
\]

### 9.2 Exact Skew-Hermitian Identity $s_{\rm bilin} = -s_{\rm herm}$ on the Antipodal Orbit

On the antipodal orbit $(u,-u)$ ($u \in \mathbb{Z}_5^\times$), the chiral shift vertex
\[
V_{u,-u} = Z \otimes \frac{E_u - E_{-u}}{2}
\]
satisfies $Z^\dagger = Z$ and $E_u^\dagger = E_{-u}$, and is therefore **skew-Hermitian**:
\[
V_{u,-u}^\dagger = -V_{u,-u}.
\]
Consequently, for any nonzero reference state $u_0 \in M_{e_0} \setminus \{0\}$ (so that $\Pi_{e_0} u_0 = u_0$ and $\|u_0\|^2 \neq 0$):
\[
\langle u_0,\, \Pi_{e_0} V_{u,-u} \Pi_{\neq 0} V_{u,-u} u_0\rangle
= -\langle u_0,\, V_{u,-u}^\dagger \Pi_{\neq 0} V_{u,-u} u_0\rangle
= -\|\Pi_{\neq 0} V_{u,-u} u_0\|^2,
\]
which implies the exact one-step identity across all $u_0 \in M_{e_0} \setminus \{0\}$:
\[
\boxed{s_{\rm bilin}(u,-u) = -s_{\rm herm}(u,-u) = -\frac{1}{2} \qquad \forall u \in \mathbb{Z}_5^\times.}
\]
Because $s_{\rm bilin}(u,-u) / s_{\rm herm}(u,-u) = -1$ identically on $\mathcal{O}_{u,-u}$, for any reference state $u_0 = c(v_+ \otimes e_0)$ ($c \in \mathbb{Q}(i)^\times$) on the positive coin branch $v_+$, the uncalibrated asymptotic ratio $\frac{x_B}{s_{\rm herm}}$ is **invariant** under any common real rescaling of the vertex $V_{u,-u} \mapsto c_V V_{u,-u}$ ($c_V \in \mathbb{R}^\times$) and independent of $\|u_0\|^2$ (with opposite sign on the negative coin branch $v_-$):
\[
\frac{x_{\rm B1}}{s_{\rm herm}} = -\operatorname{Im}(q) = \frac{4}{5},
\qquad
\frac{x_{\rm B2}}{s_{\rm herm}} = -\operatorname{Im}\left(\frac{q}{1-q}\right) = \frac{1}{4}.
\]

### 9.3 Three Exact Delimitations on `AlphaMap` and $\lambda$

1. **`ALPHA-SEED [T]` ($4\times 4$ Gram $G_5$) vs $5\times 5$ degenerate Gram $H$ and quotient projection $P_H$:**
   - For $p=5$, the canonical proof of `ALPHA-SEED [T]` ([reproduce/alpha-exact-lemma/verify.py](https://github.com/mathorn1973/twist-j/blob/5f54015ed8361e3a64cb10894397020ddfadd104/reproduce/alpha-exact-lemma/verify.py#L5)) works on the $(p-1)=4$-dimensional basis with
     \[
     G_5 = 5 I_4 - \mathbf{1}_4\mathbf{1}_4^T,
     \qquad
     \operatorname{spec}(G_5/5) = \{1/5, 1, 1, 1\}.
     \]
     By contrast, the $5\times 5$ matrix $H = I_5 - \frac{1}{5}\mathbf{1}_5\mathbf{1}_5^T$ on $R_5$ has $\operatorname{spec}(H) = \{0, 1, 1, 1, 1\}$ (eigenvalue $0$ on $\mathbf{1}_5$, not $1/5$).
   - Under $\eta(c) = \sum_{j=0}^4 c_j \zeta_5^j$ for rational register coordinates $c \in \mathbb{Q}^5$,
     \[
     \frac{1}{5}\operatorname{Tr}\!\bigl(\eta(c)\overline{\eta(c)}\bigr)
     = \sum_{j=0}^4 c_j^2 - \frac{1}{5}\left(\sum_{j=0}^4 c_j\right)^2 = c^T H c.
     \]
     `AFFINE-QUADRATIC-FORM-UNIQUENESS [T]` ([canon/CANON.md](https://github.com/mathorn1973/twist-j/blob/5f54015ed8361e3a64cb10894397020ddfadd104/canon/CANON.md#L10925-L10944)) explicitly distinguishes the sizes $J_5$ and $J_4$ and derives no Born reading or normalization from this identity.
   - While the antipodal emission vector $T e_0 = \frac{e_u - e_{-u}}{2}$ retains quadratic weight $\|T e_0\|_H^2 = \frac{1}{2}$, the reference vector has $\|e_0\|_H^2 = \frac{4}{5} \neq 1$, and $P_0 = |e_0\rangle\langle e_0|$ does not descend to the quotient by $\ker H = \langle \mathbf{1}_5\rangle$ ($P_0 \mathbf{1}_5 = e_0 \neq 0$).
   - Replacing $P_0$ by the $H$-consistent quotient projector
     \[
     P_H c = e_0\,\frac{5c_0 - \sum_{j=0}^4 c_j}{4}, \qquad Q_H = I_5 - P_H,
     \]
     yields simultaneously on the antipodal orbit (the coefficient arithmetic is checked in Section 10 of [C-QS-COUPLING-VARIANT-AB-CHECKER.py](C-QS-COUPLING-VARIANT-AB-CHECKER.py)):
     \[
     s_{\rm herm}^H = \frac{5}{8}, \qquad s_{\rm bilin}^H = -\frac{5}{8}, \qquad x_{\rm B1}^H = \frac{1}{2}, \qquad x_{\rm B2}^H = \frac{5}{32},
     \]
     so the ratios $\frac{5x^H}{s_{\rm herm}^H}$ remain **$4$** (in B1) and **$5/4$** (in B2). Changing the metric and projector consistently alters both the emission weight and the return phase by the same factor $5/4$, leaving their ratio unchanged.

2. **Denominator correction preserves the formal first jet, not physical $\lambda = 1$:**
   - For each finite tick $i$, $\frac{\tau h}{1 + c_i\tau + O_i(\tau^2)} = h\tau + O_i(\tau^2)$ ($h = s_{\rm herm}$), so this normalization change does not alter the first-jet coefficient under the declared order "first derivative at finite $N$, then limit $N \to \infty$".
   - The remainder is not uniform in $i$: in B2, the total norm of the orthogonal historical state relative to the reference has the form $D_i(\tau) = 1 + i h\tau + \tau^2 B_i$, so for fixed $\tau > 0$ and $h > 0$:
     \[
     0 \le \frac{1}{N}\sum_{i=1}^N \frac{\tau h}{D_i(\tau)} \le \frac{1}{N}\sum_{i=1}^N \frac{1}{i} \xrightarrow{N\to\infty} 0,
     \]
     whereas differentiating at finite $N$ and then taking $N \to \infty$ gives $h$. Thus the formal emission tangent is preserved, but its identification with a stationary physical coupling at finite $\tau$ is not proved by this argument.

3. **5-tick cycle does not by itself determine $\lambda = 5$:**
   - A common change of time unit from 1 tick to 1 five-tick cycle multiplies both the phase rate and the emission rate by $5$, leaving their ratio invariant. Multiplying only the emission reading by $5$ is a new relative calibration requiring its own justification; moreover, the factor $5$ in A6 comes from the tree denominator $\theta_s(0) = \Pi/5$, not from a derived count of emission opportunities.

---

## 10. Audit of the Original Wall-Based Variant A (Rev 3) and Future $J$-Model Dichotomy (`STOP-PREDEFINITION`)

### 10.1 Separation of Root Index $k$ and Galois Branch Index $a$

For $N=5$, let the root circle elements and principal angles of `WALL-CIRCLE-LEMMA [T]` and `WALL-LI2-RUNG [T]` ([canon/CANON.md](https://github.com/mathorn1973/twist-j/blob/5f54015ed8361e3a64cb10894397020ddfadd104/canon/CANON.md#L21652-L21766)) be indexed by $k \in \{1, 2, 3, 4\}$:
\[
z_k = 1 + \zeta_5^k,
\qquad
\psi_k = \frac{\pi(5 - 2k)}{5},
\qquad
\operatorname{Li}_1(z_k) = i\psi_k,
\qquad
\operatorname{Re}\operatorname{Li}_2(z_k) = \frac{\psi_k^2}{4}.
\]
Since $J = 1 + \zeta_5^2 = z_2$, the Galois automorphism $\sigma_a(\zeta_5) = \zeta_5^a$ ($a \in \{1, 2, 3, 4\}$) maps $J$ to root index $k_a = 2a \bmod 5$:
\[
\sigma_a(J) = z_{\,2a \bmod 5}.
\]
Ordering by Galois branch index $a = 1, 2, 3, 4$ (which corresponds to $k_a = 2, 4, 1, 3$) yields (the rational consequences of the imported wall identity are checked in Section 11 of [C-QS-COUPLING-VARIANT-AB-CHECKER.py](C-QS-COUPLING-VARIANT-AB-CHECKER.py)):
\[
\operatorname{Im}\operatorname{Li}_1\bigl(\sigma_a(J)\bigr)
= \frac{\pi}{5}\bigl(1, -3, 3, -1\bigr),
\qquad
\operatorname{Re}\operatorname{Li}_2\bigl(\sigma_a(J)\bigr)
= \frac{\pi^2}{100}\bigl(1, 9, 9, 1\bigr).
\]

- On this logarithmic $\operatorname{Li}_1$ rung, the imaginary parts are $\pm\frac{\pi}{5}$ and $\pm\frac{3\pi}{5}$ (whereas $\frac{2\pi}{5}$ belongs, for example, to $\arg J = \frac{2\pi}{5}$).
- The contracting Galois branches ($|\sigma_a(J)| = \phi^{-1} < 1$) are $a = 1, 4$ ($k = 2, 3$); the expanding Galois branches ($|\sigma_a(J)| = \phi > 1$) are $a = 2, 3$ ($k = 4, 1$).
- The same-branch quadratic ratio $\frac{\operatorname{Re}\operatorname{Li}_2(\sigma_a(J))}{[\operatorname{Im}\operatorname{Li}_1(\sigma_a(J))]^2} = \frac{1}{4}$ and the normalized Galois-orbit branch weights $\left(\frac{1}{20}, \frac{9}{20}, \frac{9}{20}, \frac{1}{20}\right)$ (contracting sum $\frac{1}{10}$, expanding sum $\frac{9}{10}$) are exact static identities, but **none of these identities by itself selects a dynamical phase functional**.

### 10.2 Narrowly Scoped Obstruction for $1/\ell^2$ and Expanding-Branch Series

- **Rational generating function of a fixed finite-dimensional propagator:** For a fixed finite-dimensional propagator $M$ and a fixed linear readout, the excursion sequence $f_\ell = u^\dagger M^\ell v$ has a rational generating function
  \[
  \sum_{\ell \ge 0} f_\ell t^\ell = u^\dagger(I - tM)^{-1}v,
  \]
  which cannot directly generate a nonzero polylogarithmic sequence $z^\ell/\ell^2$ for all $\ell \ge 1$.
- **Scope delimitation:** This proves only that a fixed finite-dimensional time-homogeneous step with fixed linear readout does not produce $z^\ell/\ell^2$. It does **not** prove that only a non-local history is possible: time-dependent steps, an extended carrier, or a different integral reading could be proposed, provided they are given an independent definition.
- **Expanding branches and analytic continuation:** On the expanding Galois branches $a = 2, 3$ ($|\sigma_a(J)| = \phi > 1$), the power series $\sum_{\ell=1}^\infty \frac{\sigma_a(J)^\ell}{\ell^2}$ diverges. This does **not** call into question the canonical analytic continuation identity `WALL-LI2-RUNG [T]`; what is missing in Variant A is a proof that this analytic continuation equals the required dynamical excursion sum.

### 10.3 Firewall Violation in Rev 3 and Classification as `STOP-PREDEFINITION`

- In the unratified Rev 3 draft ([P-QS-COUPLING-1-OWNER-DEFINITION-REV3.md](https://github.com/mathorn1973/twist-j/blob/5f54015ed8361e3a64cb10894397020ddfadd104/notes/incubation-import-2026-08-21/C-QS-COUPLING/P-QS-COUPLING-1-OWNER-DEFINITION-REV3.md)), the exponent relation $n_p = 2n_w$ is derived from the target $\pi$-degree ($1/\pi^1$), which cannot independently select a Phase A response. Separately, the assignment $x_A:=c_w/5$ forces $5x_A/c_w=1$ for every nonzero $c_w$ by elementary cancellation. This is an illustrative assignment, not an operator derivation or evidence from an unpublished exploratory script.
- Per [C-QS-COUPLING-REV4-TYPED-PREDEFINITION-N.md](https://github.com/mathorn1973/twist-j/blob/64dc0ed8812074ca606413d2bf609c512203e061/notes/canon/C-QS-COUPLING-REV4-TYPED-PREDEFINITION-N.md#L924-L975) (§9), unresolved admissibility of the wall closure in Phase A leaves the definition in **`STOP-PREDEFINITION`**. (`STOP-INTEGRITY` would apply only to a formal execution that violated the Phase A / Phase B firewall; no such formal run was executed.)

### 10.4 Vertex-Pair Dichotomy for Any Future $J$-Model

Inserting $J$ into the vertex does not by itself determine a unique dynamics; any future $J$-weighted dynamical model must first freeze the vertex-pair rule (only the scalar product identities are checked in Section 11 of [C-QS-COUPLING-VARIANT-AB-CHECKER.py](C-QS-COUPLING-VARIANT-AB-CHECKER.py)):

1. **Emission $J V_{u,-u}$, reabsorption $\bar{J} V_{u,-u}$:** Both the two-vertex return amplitude and the one-vertex Hermitian emission weight acquire the common real factor $J\bar{J} = 2 + \zeta_5^2 + \zeta_5^3 = 2 - \phi = \phi^{-2} \in \mathbb{Q}(\zeta_5)^+$. This factor cancels identically in the quotient, leaving Variant B's conditional antipodal ratios **$4$** (B1) and **$5/4$** (B2) unchanged.
2. **Emission $J V_{u,-u}$, reabsorption $J V_{u,-u}$:** The two-vertex return amplitude acquires the complex factor $J^2 = 1 + 2\zeta_5^2 + \zeta_5^4 \neq J\bar{J}$, whereas the one-vertex Hermitian emission weight acquires $J\bar{J}$, altering the phase response. Moreover, because $V_{u,-u}^\dagger = -V_{u,-u}$ is skew-Hermitian,
   \[
   (J V_{u,-u})^\dagger = -\bar{J} V_{u,-u},
   \]
   so requiring a genuinely adjoint emission/reabsorption vertex pair also requires freezing the sign convention.

---

## 11. Final Summary and Joint Comparison (`NON-CANONICAL` / `STOP-PREDEFINITION`)

> Varianta B poskytuje přesné podmíněné výsledky pro deklarovaný automat, čtení a pořadí limit. Neurčuje fyzickou kalibraci `AlphaMap`, diferenciální identifikaci A6 ani výběr antipodální třídy. Změna společného reálného měřítka vrcholu, společné časové jednotky ani uvedená konzistentní kvocientová konstrukce poměry $4$ a $5/4$ nemění. Původní stěnová Varianta A nevyhovuje navrženému firewallu Phase A / Phase B a zůstává uzavřena v `STOP-PREDEFINITION`. Ilustrativní předpis $x_A=c_w/5$ by poměr $1$ vložil konstrukcí, nikoli odvodil z dynamiky.

| Varianta | Doložený výsledek | Neuzavřená podmínka |
|---|---|---|
| **B, spárovaný automat** | Při deklarovaných čteních poměry $4$, $5/4$ | A6, fyzický `AlphaMap`, přípustná třída |
| **A, původní stěnový návrh** | Přesné stěnové identity; ilustrativní předpis $x_A=c_w/5$ není odvozením odezvy z dynamiky | Přípustná provenience Phase A a odvození odezev z dynamiky |
