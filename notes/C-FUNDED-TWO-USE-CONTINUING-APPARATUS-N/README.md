# `C-FUNDED-TWO-USE-CONTINUING-APPARATUS-N`

**NON-CANONICAL / L1 analytical incubation note / 2026-10-15.**
Original work Apache-2.0, A. M. Thorn.
Reservation: [#1504](https://github.com/mathorn1973/twist-j/issues/1504), following the completed three-lane review in [#1497#issuecomment-6179898943](https://github.com/mathorn1973/twist-j/issues/1497#issuecomment-6179898943).

---

## 1. Frozen research question

How can one completely specified conditional L1 device perform two positive source uses on the same continuing wave/tape apparatus with a single bounded rational energy store $b \in [0, B] \cap \mathbb{Q}$, signed work ledger $W \in \mathbb{Q}$, and full two-sided $H_B$ store guards while retaining all four chronological signed port cuts $(b_0, b_1, b_2, b_3)$, both native heads $(x_A, x_B)$, the delayed second-source receiver label $d = C_{1,B} \in \mathbb{F}_5^2$, and explicit contact direction/acceptance indicators $(\sigma_A, \sigma_B) \in \{\pm 1\}^2$, and what exact input-independent capacity $(B, b_{\mathrm{init}})$, occupied-wave work correction $\Delta_B(z_A, z_B)$, dual inverse theorems, conditioned two-use prediction laws, and matched-comparator boundaries govern this continuing apparatus?

---

## 2. Six ordered obligations

1. **Obligation 1 (Carrier, preserved classical geometry, and delayed-label separation):**
   Preserve the inherited $D_3$ stencil $B$, marked sites $Y = (y_0, y_1, y_2, y_3, y_4)$ with ordered ports $R = ((0,0,0), (1,1,0), (1,0,1), (0,1,1)) \in D_3^4$ and fifth zero-mean reference site $y_4 = (2,0,0) \in D_3$, finite causal domain $D = Y + B_{\mathrm{zero}} + B_{\mathrm{zero}}$ ($|D| = 869$), five-site source map $S$, and two-tape wave update $F$. Use the live first-tick receiver $C_{1,A} = \operatorname{rec}(x_{1,A})$ at $n=1$ ($c=1$) and the retained delayed label $d = C_{1,B} = \operatorname{rec}(x_{1,B}) \in \mathbb{F}_5^2$ at actual $n=3$ ($c=4$). Specify one complete carrier $\mathcal{Z}_B$ and keep the discrete $\mathbb{F}_5^2$ delayed label $d$ strictly distinct from any rational ancillary registers.
2. **Obligation 2 (Conditional label-adapter and two-bit direction-control primitives with global invertibility):**
   Admit the reversible buffer addition $L_{\mathrm{buf}}(x_B, d) = (x_B, d + \operatorname{rec}(x_B) \pmod 5)$ and two separately retained direction bits $(\sigma_A, \sigma_B) \in \{\pm 1\}^2$, both initialized to $+1$, one for each contact ($H_{B,A}$ at $c=1$ acting on $\sigma_A$ and reading $\operatorname{rec}(x_A)$; $H_{B,B}$ at $c=4$ acting on $\sigma_B$ and reading $d$), as explicit conditional L1 primitives (not compiled from native $U$ and not claimed minimal). Prove that every primitive ($L_{\mathrm{buf}}, H_{B,A}, H_{B,B}, F$) is globally well-defined and invertible on its declared carrier, with $H_{B,A}^2 = \mathrm{id}$ and $H_{B,B}^2 = \mathrm{id}$ on all of $\mathcal{Z}_B$.
3. **Obligation 3 (Single bounded store $b \in [0,B]$, signed work accounting, and exact occupied-state $\Delta_B$):**
   Use a single stock $b \in [0, B] \cap \mathbb{Q}$, signed work ledger $W \in \mathbb{Q}$, and the complete two-sided $H_B$ guard at each contact ($0 \le b - \Delta_A \le B$ at $c=1$; $0 \le b - \Delta_B \le B$ at $c=4$). Derive the exact closed-form occupied-wave energy increment $\Delta_B(z_A, z_B) = E_0(z_B) + g^T(w_2 - \frac{1}{2}H w_1) = E_0(z_B) - \frac{s_B (\mu^T z_A)}{10497600}$ with $\mu = (145483, 173653, 173653, 142153)^T$ from the frozen `#1485` stencil values, and prove both $0 \le b_{\mathrm{init}} - E_A \le B$ and $0 \le b_{\mathrm{init}} - E_A - \Delta_B \le B$ along the positive ready trajectory.
4. **Obligation 4 (Input-independent $(B, b_{\mathrm{init}})$ for all $25$ ordered source pairs and complete off-ready/refused behavior):**
   Starting from blank wave/tapes and fixed source-independent readiness, prove the exact 25-pair rational work table on $Z_5 \times Z_5$, establishing $0 \le E_A(z_A) \le \frac{2}{5}$, $0 \le \Delta_B(z_A, z_B) \le \frac{2}{5}$, and $\max_{(z_A,z_B)\in Z_5^2}(E_A + \Delta_B) = \frac{8224427}{10497600} < \frac{4}{5}$, so that any input-independent $(B, b_{\mathrm{init}})$ satisfying $\frac{8224427}{10497600} \le b_{\mathrm{init}} \le B$ (in particular $b_{\mathrm{init}} = B = \frac{4}{5}$) succeeds for all $25$ ordered source-label pairs. Define the complete transition and inverse behavior across all four acceptance/refusal branches `(ACC,ACC)`, `(ACC,REF)`, `(REF,ACC)`, `(REF,REF)` and arbitrary occupied states, with explicit partial-funding refusal witnesses at $B = \frac{2}{5}$ and $B = \frac{1}{5}$.
5. **Obligation 5 (Four-cut retention, acceptance/refusal discrimination, and dual inverse theorems):**
   Retain all four chronological cuts $(b_0, b_1, b_2, b_3)$, both native heads $(x_A, x_B)$, delayed label $d \in \mathbb{F}_5^2$, and direction pair $(\sigma_A, \sigma_B) \in \{\pm 1\}^2$. Prove continued direct reading of the first record $(b_0, b_1)$, exact reading and archive-independent source decoding of $(z_A, z_B)$ from $(b_0, b_2)$, discrimination of accepted zero ($h_i = 0$, flipping $\sigma_i \mapsto -1$) from refusal (preserving $\sigma_i = +1$), the complete-apparatus two-sided permutation inverse on the full apparatus carrier, and the native prepared-image left inverse and exact image recognizer across all $625^2 = 390{,}625$ native input pairs $(p_A, p_B) \in \mathbb{F}_5^4 \times \mathbb{F}_5^4$.
6. **Obligation 6 (Joint energy invariant, conditioned two-use prediction, and matched-comparator boundary):**
   Prove the joint invariants $E_{\mathrm{full}}(X) - W = 2(\|c_0\|^2 + \|c_1\|^2)$, $E_{\mathrm{full}}(X) + b = 2(\|c_0\|^2 + \|c_1\|^2) + b_{\mathrm{init}}$, and $W + b = b_{\mathrm{init}}$ (counting stored tape energy once inside $E_{\mathrm{full}}(X)$), the conditioned two-use calibration-to-prediction theorem on $Z_5 \times Z_5 \subset \Pi_2 \times \Pi_2$ within the linear/quadratic model hierarchy $\mathcal{A}_{\mathrm{lin}}^{(2)} \subset \mathcal{A}_{\mathrm{aff}}^{(2)} \subset \mathcal{A}_{\mathrm{nl}}^{(2)}$, and the exact comparator theorem separating restricted comparators while preserving byte-for-byte indistinguishability against any classical comparator implementing the same full law.

---

## 3. Immutable inputs and non-duplication boundary

- **Public authority:** Public Canon v101 at `main` (`8b91a935c426036e00ecb300019fd94734addeec`, `canon-v101`, content commit `421a4ec1daf07c04d19022c1ee219607e83c09a8`).
- **Accepted three-lane inputs (preserved untouched):**
  - A1 (`#1498` / PR `#1502`): `7b4d55502be44b2f2aed4005c909d7dcb50dbc55` (`notes/C-HB-NATIVE-ADMISSION-BOUNDARY-N/`)
  - A2 (`#1499` / PR `#1501`): `c34baa826cb846260b96373ae6d8f10c3a189a5a` (`notes/C-TWO-USE-CONTROL-ARCHIVE-N/`)
  - A3 (`#1500` / PR `#1503`): `f341b04f737827d9033e60f452fab77231f7b04a` (`notes/C-FIVE-SOURCE-PREDICTIVE-SEPARATION-N/`)
- **Historical inputs:** `#1484`/`#1485` (`1b69563af4018b08d7dc75781b12e9553a8c19c3`), `#1486`/`#1489` (`ea924e214ec3c29009fd4590f294954d3e5ad43f`), `#1491`/`#1492` (`8b91a935c426036e00ecb300019fd94734addeec`), and `#1495`/`#1496` (`b7636a334b09fcc68422bcd6cc6e15334d416c59`).
- **Public owners untouched:** `QUADRATIC-MEMORY-NATIVE-CONTACT` `[O]` and `QDD-INSTRUMENT-APPARATUS` `[O]` remain untouched. No Canon, registry, frontier, or workflow file is modified.
