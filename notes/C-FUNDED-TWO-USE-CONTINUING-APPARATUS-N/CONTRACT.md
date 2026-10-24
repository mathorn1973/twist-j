# Frozen contract: `C-FUNDED-TWO-USE-CONTINUING-APPARATUS-N`

**NON-CANONICAL / L1 mathematical contract / conditional two-use funded continuing apparatus.**
Original work Apache-2.0, A. M. Thorn, 2026-10-15.
Reservation: [#1504](https://github.com/mathorn1973/twist-j/issues/1504), following [#1497#issuecomment-6179898943](https://github.com/mathorn1973/twist-j/issues/1497#issuecomment-6179898943).
This contract is frozen at its first public pin commit (`README.md`, `CONTRACT.md`, `PREREG.md`, `SOURCES.json`) before `PROOF.md`, `RESULT.md`, `INTERFACE.json`, and `PROMO-C-FUNDED-TWO-USE-CONTINUING-APPARATUS-N.md` are authored.

---

## 1. Preserved classical wave/tape geometry and native two-head dynamics

### 1.1 Inherited $D_3$ stencil, five-site source $S$, and two-tape transition $F$

All classical definitions are inherited without change from `notes/C-CLASSICAL-SIGNED-PORT-CONTRACT-N/CONTRACT.md` (`4302c31f07823b2a843e3702ca14620c1917b853`) and `notes/C-CLASSICAL-SIGNED-PORT-CONTRACT-N/OBSERVABILITY_CALIBRATION.md` (`1b69563af4018b08d7dc75781b12e9553a8c19c3`):

1. **Lattice and stencil:** Let $D_3 = \{x \in \mathbb{Z}^3 : x_1 + x_2 + x_3 \equiv 0 \pmod 2\}$. The symmetric stencil $B_{\mathrm{st}} = \{d \in D_3 : |d|^2 \in \{2, 4, 8, 10, 16\}\}$ has shell weights $(6, 1, 15, 1, 1)$ and coefficients $c_d = \mathrm{weight}(|d|^2)/324$, with full diagonal $\sum_{d \in B_{\mathrm{st}}} c_d = \frac{8}{9}$. Put $B_{\mathrm{zero}} = B_{\mathrm{st}} \cup \{0\}$.
2. **Marked sites, ordered ports, and finite causal domain:** Mark, in exact order,
   $$
   y_0 = (0,0,0), \quad y_1 = (1,1,0), \quad y_2 = (1,0,1), \quad y_3 = (0,1,1), \quad y_4 = (2,0,0) \in D_3,
   $$
   with $Y = \{y_0, y_1, y_2, y_3, y_4\}$, ordered four-port tuple $R = (y_0, y_1, y_2, y_3) \in D_3^4$, and finite causal domain $D = Y + B_{\mathrm{zero}} + B_{\mathrm{zero}}$ ($|D| = 869$), ordered lexicographically.
3. **Operators and five-site zero-mean source:** Let $P : \mathbb{Q}^4 \to \mathbb{Q}^D$ insert the four port values at $R = (y_0, y_1, y_2, y_3)$ ($P e_i = \delta_{y_i}$ for $i \in \{0,1,2,3\}$, $P^T P = I_4$). Let $L_D = P_D L P_D^T$ be the principal Dirichlet restriction (retaining boundary diagonal $\frac{8}{9}$), and set
   $$
   H = 2I - L_D, \qquad K = (I + P P^T)^{-1} = I - \frac{1}{2}P P^T, \qquad J_0 = I - P P^T, \qquad T = K H.
   $$
   For any $z = (z_0, z_1, z_2, z_3)^T \in \mathbb{Q}^4$ with sum $s = \mathbf{1}^T z = \sum_{i=0}^3 z_i$, the five-site zero-mean source insertion $S : \mathbb{Q}^4 \to \mathbb{Q}^D$ is
   $$
   S z = \sum_{i=0}^3 \left(z_i - \frac{s}{5}\right)\delta_{y_i} - \frac{s}{5}\delta_{y_4},
   $$
   with $P^T S = I_4 - \frac{1}{5}\mathbf{1}\mathbf{1}^T = G_{\mathrm{source}}$ and $\|S z\|^2 = z^T G_{\mathrm{source}} z$.
4. **Classical wave/tape state, transition $F$, and full energy:** The classical wave/tape carrier is
   $$
   \mathcal{X} = (\mathbb{Q}^D \times \mathbb{Q}^D) \times (\mathbb{Q}^4)^2 \times (\mathbb{Q}^4)^2 \times (\mathbb{Z}/2\mathbb{Z}), \qquad X = \bigl((u, v),\, (A_0, A_1),\, (B_0, B_1),\, k\bigr).
   $$
   The reversible two-tape wave update $F : \mathcal{X} \to \mathcal{X}$ is
   $$
   w_{\mathrm{next}} = K(H v - J_0 u + 4 P A_0), \qquad b_{\mathrm{out}} = A_0 - \frac{1}{2}P^T(w_{\mathrm{next}} - u), \qquad
   F\bigl((u,v),(A_0,A_1),(B_0,B_1),k\bigr) = \bigl((v, w_{\mathrm{next}}),\, (A_1, B_1),\, (b_{\mathrm{out}}, B_0),\, k+1 \bmod 2\bigr).
   $$
   The wave energy and full classical energy (counting stored tape energy once) are
   $$
   E_D(u, v) = \frac{1}{2}\bigl(\|v - u\|^2 + u^T L_D v\bigr) = \frac{1}{2}\bigl(\|u\|^2 + \|v\|^2 - u^T H v\bigr), \qquad
   E_{\mathrm{full}}(X) = E_D(u, v) + 2\bigl(\|A_0\|^2 + \|A_1\|^2 + \|B_0\|^2 + \|B_1\|^2\bigr).
   $$
5. **Balanced rational lift $\eta$:** For any receiver pair $r = (q, r_2) \in \mathbb{F}_5^2$, use the balanced residue lift $\ell(0,1,2,3,4) = (0,1,2,-2,-1)$ and
   $$
   \eta(q, r_2) = \left(\frac{\ell(q)}{2},\, \frac{\ell(r_2) + 1}{2},\, 0,\, 0\right) \in \Pi_2 = \mathbb{Q}e_0 \oplus \mathbb{Q}e_1 \subset \mathbb{Q}^4, \qquad a(r) := S\eta(r) \in \mathbb{Q}^D.
   $$

### 1.2 Shared-counter two-head native evolution $V$

On $\mathbb{N}_0 \times \mathbb{F}_5^6 \times \mathbb{F}_5^6$ with state $(n, x_A, x_B)$, where $\operatorname{rec}(x) = (x_4, x_5) \in \mathbb{F}_5^2$ denotes the last two coordinates of $x = (x_0, x_1, x_2, x_3, x_4, x_5) \in \mathbb{F}_5^6$, the native tick $V$ applies the five canonical involutions $g_0, g_1, g_2, g_3, g_4$ from Public Canon v101 (`8b91a935c426036e00ecb300019fd94734addeec`) independently to each head with the shared counter $n$:
$$
V(n, x_A, x_B) = \bigl(n+1,\, g_{j(n, x_A)}(x_A),\, g_{j(n, x_B)}(x_B)\bigr), \qquad j(n, x) = \left(\sum_{m=0}^5 x_m + 2\theta_n\right) \bmod 5, \qquad \theta_n = \operatorname{popcount}(n) \bmod 2.
$$
For any native preparation $p \in \mathbb{F}_5^4$ with $x_0(p) = (p, 0, 1)$ and residue sum $h(p) = \sum_{m=0}^3 p_m \bmod 5$, the first-tick receiver at $n=1$ is $C_1(h) \in \{(0,4), (1,4), (1,0), (2,0), (0,1)\}$, inducing the five source vectors $Z_5 = \{z^{(0)}, z^{(1)}, z^{(2)}, z^{(3)}, z^{(4)}\} = \{(0,0,0,0), (\frac{1}{2},0,0,0), (\frac{1}{2},\frac{1}{2},0,0), (1,\frac{1}{2},0,0), (0,1,0,0)\} \subset \Pi_2$ with cold injection energies $E_0(z^{(h)}) = \frac{1}{2}\|S z^{(h)}\|^2 \in \{0, \frac{1}{10}, \frac{3}{20}, \frac{2}{5}, \frac{2}{5}\}$.

---

## 2. Full composite carrier, conditional primitives, and 8-phase autonomous law

### 2.1 Complete composite carrier $\mathcal{Z}_B$ and literal equality

Fix a rational store capacity $B \in \mathbb{Q}_{\ge 0}$ (with $B$ unsubscripted denoting the store capacity, distinct from the output tape pair $B_{\mathrm{out}} = (B_0, B_1) \in (\mathbb{Q}^4)^2$). The complete composite state carrier is
$$
\mathcal{Z}_B = \mathbb{N}_0 \times \mathbb{F}_5^6 \times \mathbb{F}_5^6 \times \mathcal{X} \times \mathbb{Q} \times ([0, B] \cap \mathbb{Q}) \times \{\pm 1\}^2 \times \mathbb{F}_5^2 \times (\mathbb{Z}/8\mathbb{Z}),
$$
with state tuple
$$
Z = \bigl(n,\, x_A,\, x_B,\, X,\, W,\, b,\, (\sigma_A, \sigma_B),\, d,\, c\bigr),
$$
where:
- $n \in \mathbb{N}_0$ is the shared native counter;
- $x_A, x_B \in \mathbb{F}_5^6$ are the two native checkpoint registers;
- $X = ((u,v), (A_0,A_1), (B_0,B_1), k) \in \mathcal{X}$ is the complete classical wave and four-slot tape state;
- $W \in \mathbb{Q}$ is the signed work ledger;
- $b \in [0, B] \cap \mathbb{Q}$ is the single bounded nonnegative rational energy store;
- $(\sigma_A, \sigma_B) \in \{\pm 1\}^2$ is the ordered pair of separately retained contact direction bits, one for Contact A and one for Contact B;
- $d \in \mathbb{F}_5^2$ is the discrete 25-state delayed receiver buffer (kept strictly distinct from any rational ancillary registers such as A1's $(d_{\mathrm{rat}}, \beta) \in \mathbb{Q} \times \{0,1\}$);
- $c \in \mathbb{Z}/8\mathbb{Z}$ is the 8-phase controller clock.

The static-source apparatus subcarrier (holding supplied receiver labels $(r_A, r_B) \in (\mathbb{F}_5^2)^2$ fixed in place of $(\operatorname{rec}(x_A), \operatorname{rec}(x_B))$) is
$$
\mathcal{A}_B = \mathcal{X} \times \mathbb{Q} \times ([0, B] \cap \mathbb{Q}) \times \{\pm 1\}^2 \times \mathbb{F}_5^2.
$$
**Literal equality:** Equality everywhere is exact coordinatewise equality in $\mathbb{N}_0$, $\mathbb{F}_5^6$, $\mathbb{Q}^D$, $\mathbb{Q}^4$, $\mathbb{Q}$, $[0,B]\cap\mathbb{Q}$, $\{\pm 1\}^2$, $\mathbb{F}_5^2$, and $\mathbb{Z}/8\mathbb{Z}$ with tolerance $0$, without sign quotient, normalization, or projectivization.

### 2.2 Explicitly admitted conditional primitives ($L_{\mathrm{buf}}, H_{B,A}, H_{B,B}$)

In addition to the inherited native $V$ and classical $F$, the following three operations are admitted explicitly as **conditional L1 mathematical primitives** (not compiled from native $U$, not derived from $J$, and not claimed minimal):

1. **Delayed-label buffer capture $L_{\mathrm{buf}}$:** On $\mathbb{F}_5^6 \times \mathbb{F}_5^2$ (acting on $(x_B, d)$ and fixing all other coordinates),
   $$
   L_{\mathrm{buf}}(x_B, d) = \bigl(x_B,\, (d + \operatorname{rec}(x_B)) \bmod 5\bigr), \qquad
   L_{\mathrm{buf}}^{-1}(x_B, d') = \bigl(x_B,\, (d' - \operatorname{rec}(x_B)) \bmod 5\bigr).
   $$
2. **First bounded-store contact involution $H_{B,A}$ (acting on label $r_A = \operatorname{rec}(x_A)$ and direction slot $\sigma_A$):**
   For any state $Z \in \mathcal{Z}_B$ (or $(X, W, b, (\sigma_A, \sigma_B), d) \in \mathcal{A}_B$ with static label $r_A \in \mathbb{F}_5^2$), let $a_A = S\eta(r_A)$ and define the exact wave energy increment
   $$
   \Delta_A(u, v, \sigma_A, r_A) := E_D(u, v + \sigma_A a_A) - E_D(u, v) = \frac{1}{2}\|a_A\|^2 + \sigma_A a_A^T\left(v - \frac{1}{2}H u\right).
   $$
   The complete two-sided store guard is $0 \le b - \Delta_A \le B$:
   - If $0 \le b - \Delta_A \le B$ (**accepted branch**):
     $$
     H_{B,A} : \bigl(v,\, W,\, b,\, (\sigma_A, \sigma_B)\bigr) \mapsto \bigl(v + \sigma_A a_A,\, W + \Delta_A,\, b - \Delta_A,\, (-\sigma_A, \sigma_B)\bigr),
     $$
     leaving $n, x_A, x_B, u, (A_0,A_1), (B_0,B_1), k, \sigma_B, d, c$ unchanged.
   - If $b - \Delta_A < 0$ or $b - \Delta_A > B$ (**refused branch**):
     $$
     H_{B,A} = \mathrm{id}.
     $$
3. **Second bounded-store contact involution $H_{B,B}$ (acting on retained delayed label $d \in \mathbb{F}_5^2$ and direction slot $\sigma_B$):**
   For any state $Z \in \mathcal{Z}_B$ (or $\mathcal{A}_B$), let $a_B = S\eta(d)$ and define the exact wave energy increment
   $$
   \Delta_B(u, v, \sigma_B, d) := E_D(u, v + \sigma_B a_B) - E_D(u, v) = \frac{1}{2}\|a_B\|^2 + \sigma_B a_B^T\left(v - \frac{1}{2}H u\right).
   $$
   The complete two-sided store guard is $0 \le b - \Delta_B \le B$:
   - If $0 \le b - \Delta_B \le B$ (**accepted branch**):
     $$
     H_{B,B} : \bigl(v,\, W,\, b,\, (\sigma_A, \sigma_B)\bigr) \mapsto \bigl(v + \sigma_B a_B,\, W + \Delta_B,\, b - \Delta_B,\, (\sigma_A, -\sigma_B)\bigr),
     $$
     leaving $n, x_A, x_B, u, (A_0,A_1), (B_0,B_1), k, \sigma_A, d, c$ unchanged.
   - If $b - \Delta_B < 0$ or $b - \Delta_B > B$ (**refused branch**):
     $$
     H_{B,B} = \mathrm{id}.
     $$

### 2.3 Eight-phase autonomous schedule $\mathcal{G}_B$

All operations in row $c \in \mathbb{Z}/8\mathbb{Z}$ are applied before advancing $c \mapsto (c + 1) \bmod 8$:

| Phase $c$ | Operation on complete state $Z \in \mathcal{Z}_B$ | Static-source apparatus row map $T_c$ on $\mathcal{A}_B$ |
| :---: | :--- | :--- |
| `0` | $V$ on $(n, x_A, x_B)$; all apparatus coordinates in $\mathcal{A}_B$ held | $\mathrm{id}_{\mathcal{A}_B}$ |
| `1` | $L_{\mathrm{buf}}$ ($d \leftarrow d + \operatorname{rec}(x_B) \pmod 5$) and $H_{B,A}$ (reading $\operatorname{rec}(x_A)$ with $\sigma_A$) | $H_{B,A}^{(r_A)} \circ L_{\mathrm{buf}}^{(r_B)} = L_{\mathrm{buf}}^{(r_B)} \circ H_{B,A}^{(r_A)}$ |
| `2` | $V$ on $(n, x_A, x_B)$ and $F$ on $X$; $(W, b, (\sigma_A, \sigma_B), d)$ held | $F \times \mathrm{id}$ |
| `3` | $V$ on $(n, x_A, x_B)$ and $F$ on $X$; $(W, b, (\sigma_A, \sigma_B), d)$ held | $F \times \mathrm{id}$ |
| `4` | $H_{B,B}$ (reading retained $d \in \mathbb{F}_5^2$ with $\sigma_B$); $(n, x_A, x_B, d)$ held | $H_{B,B}$ |
| `5` | $V$ on $(n, x_A, x_B)$ and $F$ on $X$; $(W, b, (\sigma_A, \sigma_B), d)$ held | $F \times \mathrm{id}$ |
| `6` | $V$ on $(n, x_A, x_B)$ and $F$ on $X$; $(W, b, (\sigma_A, \sigma_B), d)$ held | $F \times \mathrm{id}$ |
| `7` | Hold all coordinates in $(n, x_A, x_B, \mathcal{A}_B)$; advance $c: 7 \mapsto 0$ | $\mathrm{id}_{\mathcal{A}_B}$ |

Completion of the first two-use period is the boundary $n = 5, c = 7$ (after four $F$ transitions at $c = 2, 3, 5, 6$).

---

## 3. Common readiness, target theorems, and comparator families

### 3.1 Common-ready family $\mathcal{R}_{(c_0, c_1, b_{\mathrm{init}}, B)}$ and blank-ready subfamily $\mathcal{R}_{\mathrm{blank}}(b_{\mathrm{init}}, B)$

For any fixed old archive pair $(c_0, c_1) \in (\mathbb{Q}^4)^2$ and any fixed rational store parameters $0 \le b_{\mathrm{init}} \le B$, each independent native input pair $(p_A, p_B) \in \mathbb{F}_5^4 \times \mathbb{F}_5^4$ ($625^2 = 390{,}625$ pairs) is prepared at $c = 0$ as
$$
n = 0, \quad x_A = (p_A, 0, 1), \quad x_B = (p_B, 0, 1), \quad u = v = 0, \quad A = (0, 0), \quad B_{\mathrm{out}} = (c_0, c_1), \quad k = 0, \quad W = 0, \quad b = b_{\mathrm{init}}, \quad (\sigma_A, \sigma_B) = (+1, +1), \quad d = (0, 0), \quad c = 0.
$$
The **blank-ready subfamily** $\mathcal{R}_{\mathrm{blank}}(b_{\mathrm{init}}, B)$ has $c_0 = c_1 = 0$. On any ready trajectory, the retained acceptance indicators after $c=1$ and $c=4$ are
$$
\alpha_A := \frac{1 - \sigma_{A,\mathrm{final}}}{2} \in \{0, 1\}, \qquad \alpha_B := \frac{1 - \sigma_{B,\mathrm{final}}}{2} \in \{0, 1\},
$$
where $\alpha_i = 1$ ($\sigma_{i,\mathrm{final}} = -1$) certifies an **accepted** contact $i$ and $\alpha_i = 0$ ($\sigma_{i,\mathrm{final}} = +1$) certifies a **refused** contact $i$.

### 3.2 Target obligations and model/comparator families

1. **Global invertibility (`Obligation 1–2`):** Prove that $L_{\mathrm{buf}}, H_{B,A}, H_{B,B}, F$ are global bijections on their carriers, $H_{B,A}^2 = H_{B,B}^2 = \mathrm{id}$, and $G_B(a, c) = (T_c(a), (c+1)\bmod 8)$ is a two-sided permutation on $\mathcal{A}_B \times (\mathbb{Z}/8\mathbb{Z})$ across all accepted, refused, and occupied states.
2. **Exact occupied-state work $\Delta_B(z_A, z_B)$ and input-independent two-use funding (`Obligation 3–4`):**
   Derive the exact bilinear identity $g^T(w_2 - \frac{1}{2}H w_1) = -\frac{s_B(\mu^T z_A)}{10497600}$ with $\mu = (145483, 173653, 173653, 142153)^T$, evaluate the exact 25-pair rational table of $(E_A, \Delta_B, W_{\mathrm{final}})$ on $Z_5 \times Z_5$, prove that $0 \le E_A \le \frac{2}{5}$, $0 \le \Delta_B \le \frac{2}{5}$, and $\max_{Z_5^2}(E_A + \Delta_B) = \frac{8224427}{10497600} < \frac{4}{5}$, and prove that any $(B, b_{\mathrm{init}})$ with $\frac{8224427}{10497600} \le b_{\mathrm{init}} \le B$ (in particular $b_{\mathrm{init}} = B = \frac{4}{5}$) satisfies both $0 \le b_{\mathrm{init}} - E_A \le B$ and $0 \le b_{\mathrm{init}} - E_A - \Delta_B \le B$ for all $25$ ordered source-label pairs. Provide explicit refusal witnesses at $b_{\mathrm{init}} = B = \frac{2}{5}$ and $b_{\mathrm{init}} = B = \frac{1}{5}$.
3. **Four-cut record retention, acceptance/refusal discrimination, and native prepared-image inverse (`Obligation 5`):**
   Derive the unified four-cut output equations $b_0 = \alpha_A R_0 z_A$, $b_1 = \alpha_A R_1 z_A$, $b_2 = \alpha_A D_2(z_A) + \alpha_B R_0 z_B$, $b_3 = \alpha_A D_3(z_A) + \alpha_B R_1 z_B - \frac{1}{2}J_p c_1$, prove continued reading of $(b_0, b_1)$ at every boundary and archive-independent source recovery $z_A = R_0^{-1} b_0, z_B = R_0^{-1}(b_2 - D_2(z_A))$ when $(\alpha_A, \alpha_B) = (1, 1)$, prove discrimination of accepted zero ($h_i = 0$) from refusal via $(\sigma_A, \sigma_B)$, and prove the exact left inverse and image recognizer on $\mathcal{R}_{(c_0, c_1, b_{\mathrm{init}}, B)}$ for all $625^2 = 390{,}625$ native input pairs $(p_A, p_B) \in \mathbb{F}_5^4 \times \mathbb{F}_5^4$.
4. **Joint energy invariant, conditioned two-use prediction, and comparator boundary (`Obligation 6`):**
   Prove conservation of $E_{\mathrm{full}}(X) - W$, $E_{\mathrm{full}}(X) + b$, and $W + b$ across all 8 phases (counting stored tape energy once), prove the conditioned two-use calibration-to-prediction theorem on $Z_5 \times Z_5 \subset \Pi_2 \times \Pi_2$ within the two-use linear/quadratic model class $\mathcal{A}_{\mathrm{lin}}^{(2)} = \{(A_0, A_1, D_2, D_3, G_0, \Omega)\}$ (and its affine/nonlinear extensions $\mathcal{A}_{\mathrm{aff}}^{(2)} \subset \mathcal{A}_{\mathrm{nl}}^{(2)}$), and prove byte-for-byte indistinguishability against a full matched classical comparator alongside explicit separation witnesses against restricted comparators.
