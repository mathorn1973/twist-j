# Frozen contract: `C-FUNDED-TWO-USE-EXECUTABLE-N`

**NON-CANONICAL / L1 executable mathematical and software contract / 2026-10-15.**
Original work Apache-2.0, A. M. Thorn.
Reservation: [#1507](https://github.com/mathorn1973/twist-j/issues/1507), under parent program [#1506](https://github.com/mathorn1973/twist-j/issues/1506).

---

## 1. Primary embedded geometry, stencil, and native dynamics

All definitions are embedded directly from the frozen sources in `SOURCES.json` without runtime sibling imports or precomputed response lookup tables:

1. **$D_3$ lattice and 60-offset stencil $B_{\mathrm{st}}$:**
   $$
   D_3 = \{x \in \mathbb{Z}^3 : x_1 + x_2 + x_3 \equiv 0 \pmod 2\}, \qquad
   B_{\mathrm{st}} = \{d \in D_3 : |d|^2 \in \{2, 4, 8, 10, 16\}\},
   $$
   with shell weights $(6, 1, 15, 1, 1)$ for $|d|^2 \in (2, 4, 8, 10, 16)$, stencil coefficients $c_d = \mathrm{weight}(|d|^2)/324$, full diagonal $\sum_{d \in B_{\mathrm{st}}} c_d = \frac{288}{324} = \frac{8}{9}$, and $B_{\mathrm{zero}} = B_{\mathrm{st}} \cup \{0\}$ ($|B_{\mathrm{zero}}| = 61$).
2. **Marked sites $Y$, ordered ports $R$, and 869-site causal domain $D$:**
   $$
   y_0 = (0,0,0), \quad y_1 = (1,1,0), \quad y_2 = (1,0,1), \quad y_3 = (0,1,1), \quad y_4 = (2,0,0) \in D_3,
   $$
   with $Y = (y_0, y_1, y_2, y_3, y_4)$, ordered port tuple $R = (y_0, y_1, y_2, y_3) \in D_3^4$, and finite causal domain
   $$
   D = Y + B_{\mathrm{zero}} + B_{\mathrm{zero}} \subset D_3 \qquad (|D| = 869),
   $$
   ordered lexicographically by integer coordinate triples $(x_1, x_2, x_3)$.
3. **Dirichlet operator $L_D$, wave operator $H$, coupler $K$, projection $J_0$, and five-site source $S$:**
   Let $P : \mathbb{Q}^4 \to \mathbb{Q}^D$ insert port values at $R$ ($P e_i = \delta_{y_i}$, $P^T P = I_4$). On $\mathbb{Q}^D$, the principal Dirichlet operator $L_D$ has $(L_D)_{x,x} = \frac{8}{9}$ and $(L_D)_{x,y} = -c_{x-y}$ for $x - y \in B_{\mathrm{st}}$ ($0$ otherwise), and
   $$
   H = 2I - L_D, \qquad K = (I + P P^T)^{-1} = I - \frac{1}{2}P P^T, \qquad J_0 = I - P P^T, \qquad T = K H.
   $$
   For $z = (z_0, z_1, z_2, z_3)^T \in \mathbb{Q}^4$ with sum $s = \mathbf{1}^T z = \sum_{i=0}^3 z_i$, the five-site zero-mean source map $S : \mathbb{Q}^4 \to \mathbb{Q}^D$ is
   $$
   S z = \sum_{i=0}^3 \left(z_i - \frac{s}{5}\right)\delta_{y_i} - \frac{s}{5}\delta_{y_4}, \qquad P^T S = I_4 - \frac{1}{5}\mathbf{1}\mathbf{1}^T = G_{\mathrm{source}}, \qquad \|S z\|^2 = z^T G_{\mathrm{source}} z.
   $$
4. **Balanced rational lift $\eta$:**
   With $\ell(0,1,2,3,4) = (0, 1, 2, -2, -1)$, for any receiver $r = (q, r_2) \in \mathbb{F}_5^2$,
   $$
   \eta(q, r_2) = \left(\frac{\ell(q)}{2},\, \frac{\ell(r_2) + 1}{2},\, 0,\, 0\right)^T \in \Pi_2 = \mathbb{Q}e_0 \oplus \mathbb{Q}e_1 \subset \mathbb{Q}^4, \qquad a(r) := S\eta(r) \in \mathbb{Q}^D.
   $$
5. **Two-head native tick $V$:**
   On $x = (a, b, c_0, d_0, q, r) \in \mathbb{F}_5^6$ with receiver $\operatorname{rec}(x) = (q, r) = (x_4, x_5) \in \mathbb{F}_5^2$, the five canonical involutions are
   $$
   \begin{aligned}
   g_0(x) &= (b, a, d_0, c_0, q, r), &
   g_1(x) &= (-c_0, -d_0, -a, -b, -q, -r) \bmod 5, \\
   g_2(x) &= (2-c_0, 1+r-d_0, 2-a, 1-r-b, 1-q, -r) \bmod 5, &
   g_3(x) &= (2-a, 1-b, 3-c_0, 4-d_0, 1-q, 1-r) \bmod 5, \\
   g_4(x) &= (2-a, 1-b, 3-c_0, 4-d_0, 2-q, 1-r) \bmod 5.
   \end{aligned}
   $$
   With $\theta_n = \operatorname{popcount}(n) \bmod 2$ and selector $j(n, x) = (\sum_{m=0}^5 x_m + 2\theta_n) \bmod 5$, the shared-counter two-head native tick is
   $$
   V(n, x_A, x_B) = \bigl(n + 1,\, g_{j(n, x_A)}(x_A),\, g_{j(n, x_B)}(x_B)\bigr).
   $$
   The residue sum $h(p) = \sum_{m=0}^3 p_m \bmod 5$ is **produced by the native trajectory** at $n = 1$ via $\operatorname{rec}(x_{1,i}) = C_1(h(p_i)) \in \{(0,4), (1,4), (1,0), (2,0), (0,1)\}$ from $x_{0,i} = (p_i, 0, 1)$, never preloaded into the apparatus.

---

## 2. Immutable typed carriers, primitives, and 8-phase autonomous schedule

### 2.1 Immutable typed state carriers and strict input validation

For any rational store capacity $B \in \mathbb{Q}_{\ge 0}$, the classical wave/tape carrier $\mathcal{X}$, static-source apparatus subcarrier $\mathcal{A}_B$, and composite state carrier $\mathcal{Z}_B$ are:
$$
\mathcal{X} = (\mathbb{Q}^D \times \mathbb{Q}^D) \times (\mathbb{Q}^4)^2 \times (\mathbb{Q}^4)^2 \times (\mathbb{Z}/2\mathbb{Z}), \qquad
X = \bigl((u, v),\, (A_0, A_1),\, (B_0, B_1),\, k\bigr),
$$
$$
\mathcal{A}_B = \mathcal{X} \times \mathbb{Q} \times ([0, B] \cap \mathbb{Q}) \times \{\pm 1\}^2 \times \mathbb{F}_5^2,
$$
$$
\mathcal{Z}_B = \mathbb{N}_0 \times \mathbb{F}_5^6 \times \mathbb{F}_5^6 \times \mathcal{X} \times \mathbb{Q} \times ([0, B] \cap \mathbb{Q}) \times \{\pm 1\}^2 \times \mathbb{F}_5^2 \times (\mathbb{Z}/8\mathbb{Z}),
$$
with state tuple $Z = (n, x_A, x_B, X, W, b, (\sigma_A, \sigma_B), d, c)$ and capacity $B$.
All state objects (`WaveTapeState`, `ApparatusSubstate`, `CompositeState`, `DirectPortReadout`, `ChronologicalCutEntry`) are `@dataclass(frozen=True)` structures with immutable tuple and `Fraction` fields. Every constructor and transition function enforces strict type and domain validation, rejecting `bool`, `float`, `str`, wrong vector lengths, out-of-range residues $\notin \{0,1,2,3,4\}$, invalid signs $\sigma_i \notin \{-1, +1\}$, invalid pointer $k \notin \{0, 1\}$, invalid phase $c \notin \{0,\dots,7\}$, negative counter $n < 0$, negative capacity $B < 0$, or out-of-bounds store $b \notin [0, B]$ rather than truncating or normalizing away disagreement.

### 2.2 Reversible classical wave/tape step $F$ and energy $E_{\mathrm{full}}$

On $\mathcal{X}$, the forward step `F_step` ($F$) and two-sided inverse `F_inverse` ($F^{-1}$) are:
$$
w_{\mathrm{next}} = K(H v - J_0 u + 4 P A_0), \qquad b_{\mathrm{out}} = A_0 - \frac{1}{2}P^T(w_{\mathrm{next}} - u),
$$
$$
F\bigl((u,v),(A_0,A_1),(B_0,B_1),k\bigr) = \bigl((v, w_{\mathrm{next}}),\, (A_1, B_1),\, (b_{\mathrm{out}}, B_0),\, (k+1)\bmod 2\bigr),
$$
$$
u = K(H v - J_0 w_{\mathrm{next}} + 4 P \beta_0), \qquad A_0 = \beta_0 + \frac{1}{2}P^T(w_{\mathrm{next}} - u),
$$
$$
F^{-1}\bigl((v, w_{\mathrm{next}}),\, (\alpha_0, \alpha_1),\, (\beta_0, \beta_1),\, k'\bigr) = \bigl((u, v),\, (A_0, \alpha_0),\, (\beta_1, \alpha_1),\, (k'-1)\bmod 2\bigr).
$$
The wave energy and full classical energy (counting stored tape energy once) are:
$$
E_D(u, v) = \frac{1}{2}\bigl(\|v - u\|^2 + u^T L_D v\bigr) = \frac{1}{2}\bigl(\|u\|^2 + \|v\|^2 - u^T H v\bigr), \qquad
E_{\mathrm{full}}(X) = E_D(u, v) + 2\bigl(\|A_0\|^2 + \|A_1\|^2 + \|B_0\|^2 + \|B_1\|^2\bigr).
$$

### 2.3 Conditional L1 primitives ($L_{\mathrm{buf}}, H_{B,A}, H_{B,B}$)

1. **Buffer capture (`buffer_capture` / `buffer_capture_inverse`):**
   $$
   L_{\mathrm{buf}}(x_B, d) = \bigl(x_B,\, (d + \operatorname{rec}(x_B)) \bmod 5\bigr), \qquad
   L_{\mathrm{buf}}^{-1}(x_B, d') = \bigl(x_B,\, (d' - \operatorname{rec}(x_B)) \bmod 5\bigr).
   $$
2. **First funded contact (`funded_contact_A`, $H_{B,A}$):** Reads $r_A = \operatorname{rec}(x_A) \in \mathbb{F}_5^2$ (or static $r_A$ on $\mathcal{A}_B$) and $\sigma_A \in \{\pm 1\}$, sets $a_A = S\eta(r_A)$ and $\Delta_A = E_D(u, v + \sigma_A a_A) - E_D(u, v) = \frac{1}{2}\|a_A\|^2 + \sigma_A a_A^T(v - \frac{1}{2}H u)$:
   - If $0 \le b - \Delta_A \le B$ (`ACC`): $(v, W, b, (\sigma_A, \sigma_B)) \mapsto (v + \sigma_A a_A, W + \Delta_A, b - \Delta_A, (-\sigma_A, \sigma_B))$.
   - If $b - \Delta_A < 0$ or $b - \Delta_A > B$ (`REF`): identity.
3. **Second funded contact (`funded_contact_B`, $H_{B,B}$):** Reads retained $d \in \mathbb{F}_5^2$ and $\sigma_B \in \{\pm 1\}$, sets $a_B = S\eta(d)$ and $\Delta_B = E_D(u, v + \sigma_B a_B) - E_D(u, v) = \frac{1}{2}\|a_B\|^2 + \sigma_B a_B^T(v - \frac{1}{2}H u)$:
   - If $0 \le b - \Delta_B \le B$ (`ACC`): $(v, W, b, (\sigma_A, \sigma_B)) \mapsto (v + \sigma_B a_B, W + \Delta_B, b - \Delta_B, (\sigma_A, -\sigma_B))$.
   - If $b - \Delta_B < 0$ or $b - \Delta_B > B$ (`REF`): identity.

### 2.4 Eight-phase autonomous schedule (`coupled_step`, `run_seven_steps`, `run_eight_steps`)

At phase $c \in \mathbb{Z}/8\mathbb{Z}$, `coupled_step` ($\mathcal{G}_B$) applies the row operation before advancing $c \mapsto (c+1)\bmod 8$:
- $c = 0$: `native_tick` ($V$) on $(n, x_A, x_B)$; apparatus coordinates held.
- $c = 1$: `buffer_capture` ($L_{\mathrm{buf}}$) on $(x_B, d)$ and `funded_contact_A` ($H_{B,A}$) on $(x_A, X, W, b, \sigma_A)$.
- $c = 2$: `native_tick` ($V$) on $(n, x_A, x_B)$ and `F_step` ($F$) on $X$ (cut 0).
- $c = 3$: `native_tick` ($V$) on $(n, x_A, x_B)$ and `F_step` ($F$) on $X$ (cut 1).
- $c = 4$: `funded_contact_B` ($H_{B,B}$) on $(d, X, W, b, \sigma_B)$; $(n, x_A, x_B, d)$ held.
- $c = 5$: `native_tick` ($V$) on $(n, x_A, x_B)$ and `F_step` ($F$) on $X$ (cut 2).
- $c = 6$: `native_tick` ($V$) on $(n, x_A, x_B)$ and `F_step` ($F$) on $X$ (cut 3).
- $c = 7$: hold all data coordinates $(n, x_A, x_B, X, W, b, (\sigma_A, \sigma_B), d)$; advance $c: 7 \mapsto 0$.

Seven updates (`run_seven_steps`, $\mathcal{G}_B^7$) from $c = 0, n = 0$ reach the completion boundary $c = 7, n = 5$. The eighth update (`run_eight_steps`, $\mathcal{G}_B^8$) executes row $c = 7$, holding all data coordinates and rolling $c$ to $0$.

---

## 3. Reader interfaces, API access restrictions, and endpoint recognizer

### 3.1 Direct chronological archive reader (`direct_chronological_cut_reader`)

On the first initialized period ($(c, n) \in \{(0,0), (1,1), (2,1), (3,2), (4,3), (5,3), (6,4), (7,5)\}$), `direct_chronological_cut_reader(state)` inspects only `(n, c, A0, A1, B0, B1)` and returns the four chronological cut slots with status `UNWRITTEN` or `PRESENT(use, cut, vector)`:
- $c \in \{0, 1, 2\}$: all four cuts `UNWRITTEN`.
- $c = 3$: cut $0$ (`use=1, cut=0`) is `PRESENT` at $B_0 = b_0$; cuts $1, 2, 3$ `UNWRITTEN`.
- $c \in \{4, 5\}$: cuts $0, 1$ are `PRESENT` at $(B_1, B_0) = (b_0, b_1)$; cuts $2, 3$ `UNWRITTEN`.
- $c = 6$: cuts $0, 1, 2$ are `PRESENT` at $(A_1, B_1, B_0) = (b_0, b_1, b_2)$; cut $3$ `UNWRITTEN`.
- $c = 7$: all four cuts $0, 1, 2, 3$ are `PRESENT` at $(A_0, A_1, B_1, B_0) = (b_0, b_1, b_2, b_3)$.

### 3.2 Direct source reader (`direct_source_reader`) and testable API access restrictions

`direct_source_reader(b0, b2, *, sigma_A=-1, sigma_B=-1, d=None)` takes **only** the port vectors $b_0, b_2 \in \mathbb{Q}^4$ and declared acceptance/context information (`sigma_A, sigma_B` or delayed label `d`), never native heads $x_A, x_B$, piston inputs $p_A, p_B$, precomputed sums $h_A, h_B$, old archives $c_0, c_1$, or wave vectors $u, v$:
- **API guard:** Passing a `CompositeState`, `ApparatusSubstate`, `WaveTapeState`, or 6-tuple native checkpoint to `direct_source_reader` raises `TypeError`. `extract_direct_port_readout(state, include_d=False)` constructs a restricted `DirectPortReadout(b0, b2, sigma_A, sigma_B, d)` object that strips all native, wave, work, store, and old-archive fields.
- **Decoding law:** Using $R_0 = -\frac{1}{2}P^T T S$, $R_0^{-1} = -\frac{216}{59}(I_4 + \frac{v\mathbf{1}^T}{365})$ ($v = (349, 354, 354, 348)^T$), and $D_2 = \frac{1}{2}P^T(T - T^3 + T J_0)S$ derived directly from the primary operators:
  - First acceptance is $\alpha_A = \frac{1 - \sigma_A}{2} \in \{0, 1\}$. If $\alpha_A = 1$, $z_A = R_0^{-1} b_0$; if $\alpha_A = 0$, $b_0$ must be $0$ and $z_A$ is reported as `REFUSED`.
  - Second acceptance $\alpha_B \in \{0, 1\}$ can be supplied via $\sigma_B$ ($\alpha_B = \frac{1 - \sigma_B}{2}$) **or**, on the common-ready family when `d` is provided (`Clarification (ii)`), read directly from $(d, b_0, b_2)$ without $\sigma_B$: let $z_A^{\mathrm{eff}} = R_0^{-1} b_0$ and $r_{\mathrm{res}} = b_2 - D_2 z_A^{\mathrm{eff}}$; if $d = (0, 4)$ ($\eta(d) = 0$), $\alpha_B = 1$ and $z_B = 0$ whenever $r_{\mathrm{res}} = 0$; if $d \ne (0, 4)$ ($\eta(d) \ne 0$), $\alpha_B = 1$ with $z_B = R_0^{-1} r_{\mathrm{res}} = \eta(d)$ if $r_{\mathrm{res}} = R_0 \eta(d)$, and $\alpha_B = 0$ (`REFUSED`) if $r_{\mathrm{res}} = 0$.

### 3.3 Full-input endpoint inverse (`recover_prepared_inputs`) and ready-image recognizer (`recognize_ready_image`)

Full native input recovery is explicitly a separate endpoint function with native-head access (`recognize_ready_image(state, *, c0=None, c1=None, b_init=None)` and `recover_prepared_inputs(state, *, c0=None, c1=None, b_init=None)`), enforcing all four necessary and sufficient conditions on $Z \in \mathcal{Z}_B$:
1. $n = 5$, $c = 7$, and $\operatorname{rec}(x_i) \in \{C_3(0), \dots, C_3(4)\} = \{(1,0), (2,0), (2,1), (3,1), (1,2)\}$ for $i \in \{A, B\}$, uniquely decoding $(h_A, h_B)$.
2. Reconstruct $\hat{x}_{0,i} = g_{j_0(h_i)} g_{j_1(h_i)} g_{j_2(h_i)} x_i$ and require both $\operatorname{rec}(\hat{x}_{0,i}) = (0, 1)$ **and** piston-sum selector consistency $\sum_{m=0}^3 \hat{x}_{0,i,m} \bmod 5 = h_i$ for $i \in \{A, B\}$.
3. Reconstruct $\hat{x}_{1,i} = g_{j_0(h_i)} \hat{x}_{0,i}$ and require $d = \operatorname{rec}(\hat{x}_{1,B}) = C_1(h_B)$.
4. Apply the two-sided apparatus inverse $(M_{7,B}^{(r_A, r_B)})^{-1}$ with $r_i = \operatorname{rec}(\hat{x}_{1,i})$ to $(X, W, b, (\sigma_A, \sigma_B), d)$ and require $u_0 = v_0 = 0$, $A_0 = A_1 = 0$, $k_0 = 0$, $W_0 = 0$, $(\sigma_{A,0}, \sigma_{B,0}) = (+1, +1)$, $d_0 = (0, 0)$, and (when $c_0, c_1, b_{\mathrm{init}}$ are prescribed) $B_{\mathrm{out},0} = (c_0, c_1)$ and $b_0^{\mathrm{store}} = b_{\mathrm{init}}$.

---

## 4. Shared cross-implementation comparison mode (`TWOUSE-COMPARE-v1`)

In comparison mode (`--compare`, separate from ordinary scientific stdout), the program iterates over:
1. `B` in `[0, 1/10, 1/5, 2/5, 8224427/10497600, 4/5]` (in exact order);
2. `h_A` in `0..4`, then `h_B` in `0..4`, with representative $p_i = (h_i, 0, 0, 0)$, blank waves $u = v = 0$, blank tapes $A_0 = A_1 = B_0 = B_1 = 0$, and $b_{\mathrm{init}} = B$;
3. boundaries `c` in `0..7` in order ($6 \times 5 \times 5 \times 8 = 1200$ records).

Each record is serialized as the 18-element JSON array:
```text
[B,h_A,h_B,c,n,x_A,x_B,u,v,A0,A1,B0,B1,k,W,b,[sigma_A,sigma_B],d]
```
where every rational in `B, u, v, A0, A1, B0, B1, W, b` is encoded as `[numerator, positive_denominator]` (with zero as `[0, 1]`), `u` and `v` have all 869 entries ordered lexicographically by $(x_1, x_2, x_3) \in D$, and each record is encoded via `json.dumps(record, separators=(',', ':'), ensure_ascii=True) + "\n"` in ASCII bytes and fed into an incremental SHA-256 hasher. Comparison mode outputs the single line:
```text
TWOUSE-COMPARE-v1 records=1200 sha256=<64 lowercase hex>
```
Per `#1507`, this comparison output is withheld from Lane V until V's pin and first-run receipt.
