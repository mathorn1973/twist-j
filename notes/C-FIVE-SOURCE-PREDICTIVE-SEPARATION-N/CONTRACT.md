# Predictive separation and calibration-to-prediction contract

**NON-CANONICAL / L1 mathematical identifiability and prospective measurement contract / 2026-10-14.**
Original work Apache-2.0, A. M. Thorn.
Reservation: [#1500](https://github.com/mathorn1973/twist-j/issues/1500), dispatched under [#1497](https://github.com/mathorn1973/twist-j/issues/1497).
Identifier: `C-FIVE-SOURCE-PREDICTIVE-SEPARATION-N`.
Authority basis: Public Canon v101, public `main` `8b91a935c426036e00ecb300019fd94734addeec`.

This contract freezes the mathematical domains, literal equality relations, preparation families, retained states, primitive permissions, target-independent model/comparator classes, quantifiers, positive and negative decision criteria, failure witnesses, exported interface slots, and exclusions before deriving any new result.

---

## 1. Mathematical domains, fixed inherited objects, and literal equality

### 1.1 Native autonomous substrate (inherited from Public Canon v101)

The autonomous state carrier is $\Omega = \mathbb{N}_0 \times \mathbb{F}_5^6$ with checkpoints $x = (p_0, p_1, p_2, p_3, q, r) \in \mathbb{F}_5^6$, piston vector $p = (p_0, p_1, p_2, p_3) \in \mathbb{F}_5^4$, receiver pair $C = (q, r) \in \mathbb{F}_5^2$, residue sum $h(p) = \sum_{i=0}^3 p_i \pmod 5$, total checkpoint sum $z_6(x) = h(p) + q + r \pmod 5$, driver bit $\theta_n = s_2(n) \bmod 2$, and update

$$
U(n, x) = \bigl(n+1, g_{z_6(x) + 2\theta_n \bmod 5}(x)\bigr),
$$

where $(g_0, g_1, g_2, g_3, g_4)$ are the five canonical involutions on $\mathbb{F}_5^6$ frozen in Public Canon v101 (`canon/CANON.md`) and audited in `probes/P-NATIVE-CLASSICAL-CONTACT-CENSUS-1`.

- **Native preparation domain:** $\mathcal{P}_{\mathrm{nat}} = \mathbb{F}_5^4$ ($625$ preparations), embedded at $n=0$ as $x_0(p) = (p_0, p_1, p_2, p_3, 0, 1)$ with common ready receiver $C_0 = (0, 1)$.
- **Literal native equality:** $p = p'$ in $\mathcal{P}_{\mathrm{nat}}$ if and only if $p_i = p'_i$ in $\mathbb{F}_5$ for all $i \in \{0, 1, 2, 3\}$. Equality of checkpoint trajectories is literal coordinate equality in $\mathbb{N}_0 \times \mathbb{F}_5^6$. A present zero piston tuple $p = (0,0,0,0)$ or zero sum $h(p) = 0$ is an occupied preparation, not absence of a trial.

### 1.2 Classical signed-port wave and tape substrate (inherited from `#1484`/`#1485`)

The classical source space is $\mathbb{Q}^4$ with standard basis $e_0, e_1, e_2, e_3$ and operational box

$$
Z_{\mathrm{op}} = \bigl\{ z = (z_0, z_1, z_2, z_3) \in \mathbb{Q}^4 : \max_{0 \le i \le 3} |z_i| \le 1 \bigr\}.
$$

The lattice $D_3 = \{x \in \mathbb{Z}^3 : x_1 + x_2 + x_3 \equiv 0 \pmod 2\}$, symmetric stencil $B = \{d \in D_3 : |d|^2 \in \{2, 4, 8, 10, 16\}\}$ with weights $(6, 1, 15, 1, 1)/324$, marked sites $Y = \{y_0, y_1, y_2, y_3, y_4\}$, ordered port tuple $R = (y_0, y_1, y_2, y_3)$, finite causal domain $D = Y + B_{\mathrm{zero}} + B_{\mathrm{zero}}$, port insertion $P : \mathbb{Q}^4 \to \mathbb{Q}^D$, principal Dirichlet operator $L_D = P_D L P_D^T$, $H_D = 2I - L_D$, five-site zero-mean source insertion

$$
S(z) = \sum_{i=0}^3 \left(z_i - \frac{s}{5}\right)\delta_{y_i} - \frac{s}{5}\delta_{y_4}, \qquad s = \sum_{i=0}^3 z_i,
$$

source Gram matrix $G_{\mathrm{source}} = I_4 - \frac{1}{5}\mathbf{1}\mathbf{1}^T$, fixed port conductances $g_j = 2$ ($G = 2I_4$, $C_{\mathrm{port}} = 2PP^T$, $D_g = I + PP^T$), single-cut coupler $\operatorname{Couple}((u,v), a) = ((v,w), b)$, two-slot tape carrier

$$
X = (\mathbb{Q}^D \times \mathbb{Q}^D) \times (\mathbb{Q}^4)^2 \times (\mathbb{Q}^4)^2 \times (\mathbb{Z}/2\mathbb{Z}),
$$

two-cut transition $F : X \to X$, pair energy $E_D(u,v) = \frac{1}{2}(\|v-u\|^2 + u^T L_D v)$, port deposit $q_g(a) = 2\|a\|^2$, and full conserved amplitude energy

$$
E_{\mathrm{full}}\bigl((u,v), (A_0, A_1), (B_0, B_1), k\bigr) = E_D(u,v) + q_g(A_0) + q_g(A_1) + q_g(B_0) + q_g(B_1)
$$

are frozen exactly as in `notes/C-CLASSICAL-SIGNED-PORT-CONTRACT-N/CONTRACT.md` (`4302c31f07823b2a843e3702ca14620c1917b853`).

- **Literal classical equality:** Equality of sources $z \in \mathbb{Q}^4$, outputs $b_t \in \mathbb{Q}^4$, chronological two-cut records $Y_2 = (b_0, b_1) \in (\mathbb{Q}^4)^2$, energies $E \in \mathbb{Q}$, and full states $X$ is exact componentwise rational equality with tolerance $0$, without sign quotient, projectivization, normalization, or post-hoc rescaling.

### 1.3 Fixed mixed-carrier contact and source families (inherited from `#1486`/`#1489`)

With balanced lift $\ell(0,1,2,3,4) = (0, 1, 2, -2, -1)$ and receiver-to-source map

$$
\eta(q, r) = \left(\frac{\ell(q)}{2},\, \frac{\ell(r)+1}{2},\, 0,\, 0\right) \in \mathbb{Q}^4,
$$

the conditional contact $C_*$ at native boundary $n=1$ acts on $((n,x), X, w, (\text{program}, \text{stage}))$ with $X = ((u,v), A, B_{\mathrm{tape}}, k)$ by holding $(n,x)$, $A$, $B_{\mathrm{tape}}$, and $k$ fixed and updating

$$
C_* : (u, v, w) \mapsto \bigl(u,\, v + S\eta(q, r),\, w + E_D(u, v + S\eta(q,r)) - E_D(u, v)\bigr).
$$

Starting from $X_{\mathrm{blank}} = ((0,0), (0,0), (0,0), 0)$ and $w=0$, the five native residue classes $h \in \{0,1,2,3,4\}$ induce at $n=1$ the ordered five-point source set

$$
Z_5 = \bigl\{ z^{(0)}, z^{(1)}, z^{(2)}, z^{(3)}, z^{(4)} \bigr\} = \left\{
(0,0,0,0),\;
\left(\tfrac{1}{2},0,0,0\right),\;
\left(\tfrac{1}{2},\tfrac{1}{2},0,0\right),\;
\left(1,\tfrac{1}{2},0,0\right),\;
(0,1,0,0)
\right\} \subset Z_{\mathrm{op}} \subset \mathbb{Q}^4.
$$

The classical identification and validation source sets from `#1484`/`#1485` are

$$
Z_I = \{0\} \cup \{\pm e_i : 0 \le i < 4\} \quad (|Z_I| = 9), \qquad
Z_V = \{\sigma e_i + \rho e_j : 0 \le i < j < 4,\; \sigma, \rho \in \{-1, +1\}\} \quad (|Z_V| = 24).
$$

---

## 2. Target-independent model and comparator hierarchy

To test calibration-to-prediction transport and mechanism separation without circularity, we freeze three nested model classes and one explicit comparator class before deriving any prediction.

### 2.1 Cold two-cut response and energy model classes on a source domain $\mathcal{Z} \subseteq \mathbb{Q}^4$

A cold two-cut response-and-energy model $m$ over $\mathbb{Q}^4$ specifies a map

$$
\mathcal{O}_m : \mathbb{Q}^4 \to \mathbb{Q}^4 \times \mathbb{Q}^4 \times \mathbb{Q}^3, \qquad
z \mapsto \bigl(b_{0,m}(z),\, b_{1,m}(z),\, (E_{0,m}(z), E_{1,m}(z), E_{2,m}(z))\bigr),
$$

together with an initial work ledger value $w_m(z) = E_{0,m}(z)$ satisfying the two-cut conservation relation

$$
E_{1,m}(z) = E_{0,m}(z) - 2\|b_{0,m}(z)\|^2, \qquad
E_{2,m}(z) = E_{0,m}(z) - 2\|b_{0,m}(z)\|^2 - 2\|b_{1,m}(z)\|^2.
$$

Literal equality of models $m_1, m_2$ on a subset $S \subseteq \mathbb{Q}^4$ is exact pointwise equality $\mathcal{O}_{m_1}(z) = \mathcal{O}_{m_2}(z)$ for all $z \in S$.

1. **Linear/quadratic physical-form class $\mathcal{A}_{\mathrm{lin}}$:** Models $m = (A_0, A_1, G_0)$ parameterized by arbitrary rational matrices $A_0, A_1 \in \mathbb{Q}^{4 \times 4}$ and a symmetric matrix $G_0 \in \mathbb{Q}^{4 \times 4}_{\mathrm{sym}}$, where
   $$
   b_{0,m}(z) = A_0 z, \qquad b_{1,m}(z) = A_1 z, \qquad E_{0,m}(z) = \tfrac{1}{2} z^T G_0 z,
   $$
   and $E_{1,m}(z), E_{2,m}(z)$ are determined by the two-cut conservation equation above. The reference model $m_* = (R_0, R_1, G_{\mathrm{source}}) \in \mathcal{A}_{\mathrm{lin}}$ is the frozen `#1484`/`#1485` law with $R_0 = -\frac{1}{4}M$ and $R_1 = \frac{1}{2}Q - \frac{1}{4}K + \frac{1}{8}JM$.
2. **Affine response class $\mathcal{A}_{\mathrm{aff}}$:** Models $m = (c_0, A_0, c_1, A_1, e_0, \ell_0, G_0)$ with offsets $c_0, c_1 \in \mathbb{Q}^4$, matrices $A_0, A_1 \in \mathbb{Q}^{4 \times 4}$, scalar $e_0 \in \mathbb{Q}$, linear functional $\ell_0 \in \mathbb{Q}^4$, and symmetric matrix $G_0 \in \mathbb{Q}^{4 \times 4}_{\mathrm{sym}}$, where
   $$
   b_{0,m}(z) = c_0 + A_0 z, \qquad b_{1,m}(z) = c_1 + A_1 z, \qquad E_{0,m}(z) = e_0 + \ell_0^T z + \tfrac{1}{2} z^T G_0 z.
   $$
3. **General deterministic source-dependent class $\mathcal{A}_{\mathrm{nl}}$:** Arbitrary total functions $b_{0,m}, b_{1,m} : \mathbb{Q}^4 \to \mathbb{Q}^4$ and $E_{0,m} : \mathbb{Q}^4 \to \mathbb{Q}$ (including higher-degree polynomial or piecewise-rational source-dependent models) with $E_{1,m}, E_{2,m}$ given by the two-cut ledger equation.

### 2.2 Complete dynamical / mechanism comparator class $\mathcal{M}_{\mathrm{dyn}}$

A complete single-trial dynamical device $D \in \mathcal{M}_{\mathrm{dyn}}$ on preparation domain $\mathcal{P}_{\mathrm{in}}$ with observable map $\Pi_{\mathrm{obs}}$ consists of:

$$
D = \bigl(\mathcal{S}_{\mathrm{int}},\, \sigma_{\mathrm{ready}},\, \Phi_{\mathrm{prep}} : \mathcal{P}_{\mathrm{in}} \to \mathcal{S}_{\mathrm{int}},\, \mathcal{T}_{\mathrm{run}} : \mathcal{S}_{\mathrm{int}} \to \mathcal{S}_{\mathrm{int}},\, \Pi_{\mathrm{obs}} : \mathcal{S}_{\mathrm{int}} \to \mathcal{Y}\bigr).
$$

Two special instances are frozen:

- **Native-contact composite device $D_{\mathrm{NC}}$:** Input $p \in \mathbb{F}_5^4$, internal carrier $\Omega \times X \times \mathbb{Q} \times \mathcal{C}_{\mathrm{ctrl}}$, ready state $((0,(0,0,0,0,0,1)), X_{\mathrm{blank}}, 0, (\text{program},0))$, preparation $\Phi_{\mathrm{prep}}(p) = ((0,(p,0,1)), X_{\mathrm{blank}}, 0, (\text{program},0))$, four-stage run map $\mathcal{T}_{\mathrm{run}}$ executing $U \to C_* \to (U \times F) \to (U \times F) \to \mathrm{STOP}$, and classical port-and-ledger projection
  $$
  \Pi_{\mathrm{port}}\bigl((3,x_3), ((v_1,v_2),(0,0),(b_1,b_0),0), w, (\text{program},4)\bigr) = \bigl((b_0, b_1), (E_0, E_1, E_2), w\bigr).
  $$
- **Ordinary rational classical wave/port comparator $D_{\mathrm{cl}}$:** A classical lookup/encoder and rational wave device with no $\mathbb{F}_5^6$ generator dynamics $g_0,\dots,g_4$ and no Thue-Morse parity evaluation $\theta_n$, whose input front-end maps $p \in \mathbb{F}_5^4$ (or any supplied $z \in \mathcal{Z} \subseteq \mathbb{Q}^4$) to the same classical source vector $z = \eta(C_1(p)) \in Z_5$ (or $z \in \mathcal{Z}$), initializes the same cold classical state $X_0(z) = ((0, S(z)), (0,0), (0,0), 0)$ and work ledger $w = E_D(0, S(z))$, runs two steps of the identical rational operator $F$, and outputs $\Pi_{\mathrm{port}}(X_2(z), w)$.

---

## 3. Calibration-to-prediction interface and quantifiers

For any declared model class $\mathcal{A}$, any calibration source protocol $I_{\mathrm{set}} \subseteq \mathbb{Q}^4$, and any held-out validation source protocol $V_{\mathrm{set}} \subseteq \mathbb{Q}^4$:

- **Calibrated record:** $I(m) = \bigl(\mathcal{O}_m(z)\bigr)_{z \in I_{\mathrm{set}}}$.
- **Withheld prediction:** For $s \in V_{\mathrm{set}}$, $V(m; s) = \mathcal{O}_m(s)$.
- **Predictive determination predicate $\mathrm{Det}(\mathcal{A}, I_{\mathrm{set}}, V_{\mathrm{set}})$:**
  $$
  \forall m_1, m_2 \in \mathcal{A},\; \forall s \in V_{\mathrm{set}} : \quad I(m_1) = I(m_2) \implies V(m_1; s) = V(m_2; s).
  $$

### 3.1 Positive and negative outcome rules

- **Positive determination (`DETERMINED`):** Requires an exact symbolic proof that $\mathrm{Det}(\mathcal{A}, I_{\mathrm{set}}, V_{\mathrm{set}})$ holds for every $m_1, m_2 \in \mathcal{A}$ and every $s \in V_{\mathrm{set}}$, together with the explicit reconstruction formula expressing $V(m; s)$ in terms of $I(m)$.
- **Negative determination (`UNDERDETERMINED`):** Requires an explicit pair of complete admitted models $m_1, m_2 \in \mathcal{A}$ and an explicit held-out input $s \in V_{\mathrm{set}}$ such that $I(m_1) = I(m_2)$ byte-for-byte on all of $I_{\mathrm{set}}$ while $V(m_1; s) \ne V(m_2; s)$, together with the exact kernel/ambiguity subspace classification.

---

## 4. Prospective test contract and qualification boundary

1. **Strict separation of test gates:** Signed response validation ($r_{y,tj}$), full energy balance ($r_E$), independent source/sensor/clock/units qualification (Stage S), and mechanism attribution ($D_{\mathrm{NC}}$ versus $D_{\mathrm{cl}}$) are four distinct gates. Passing signed response or mathematical energy identities never discharges Stage S qualification or mechanism attribution.
2. **Legacy protocol preservation:** The `#1484`/`#1485` 9-source $Z_I$ / 24-source $Z_V$ protocol and its engineering tolerances $\varepsilon_y = \varepsilon_E = 1/10000$ remain unchanged on their declared domain. A $Z_5$-restricted test is a separate explicitly scoped protocol on $\operatorname{span}_{\mathbb{Q}}(Z_5)$, not a replacement for $Z_I/Z_V$.
3. **Second-cut independence:** In every protocol, $b_1$ must be acquired from the continuing state after the second transition $F$, never synthesized from $b_0$ via $-4R_1 M^{-1} b_0$.
4. **Energy accounting:** Retained outgoing tape deposits $q_g(b_0) + q_g(b_1)$ are internal tape energy inside $E_{\mathrm{full}}$ and must not be double-counted as external heat flux. Unmeasured controller, native-substrate, sensor, or reset energies may not be set to zero.

---

## 5. Evidence mode and exclusions

- **Evidence mode:** Purely analytical L1 mathematical proofs and exact rational witness constructions (`AUTHORED_PROOF`, `SELF_REVIEWED`, `NOT_INDEPENDENTLY_REVIEWED`). No scientific verifier execution, numerical solver, or laboratory measurement is authorized or run under this contract.
- **Exclusions:** No claim of global decoder uniqueness; no Born rule or probabilistic trial law from deterministic responses; no assertion that five residue classes span $\mathbb{Q}^4$; no SI constant or apparatus qualification derived from arithmetic; no identification of DP5 ion records with the classical port; no promotion of any claim to canonical status or closure of any `[O]` frontier row.
