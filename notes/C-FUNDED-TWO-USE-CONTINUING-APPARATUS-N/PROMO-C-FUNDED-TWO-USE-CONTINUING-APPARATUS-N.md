# Promotion Dossier: `C-FUNDED-TWO-USE-CONTINUING-APPARATUS-N`

**NON-CANONICAL / L1 analytical promotion dossier / 2026-10-15.**
Original work Apache-2.0, A. M. Thorn.
Reservation: [#1504](https://github.com/mathorn1973/twist-j/issues/1504), following [#1497#issuecomment-6179898943](https://github.com/mathorn1973/twist-j/issues/1497#issuecomment-6179898943).

```text
candidate_id:               C-FUNDED-TWO-USE-CONTINUING-APPARATUS-N
branch:                     incubation/C-FUNDED-TWO-USE-CONTINUING-APPARATUS-N
base_commit:                8b91a935c426036e00ecb300019fd94734addeec
preregistration_commit:     d4b67e44d14a2f224a0ed77eb8dd08b217711cfb
canon_tag:                  canon-v101
content_commit:             421a4ec1daf07c04d19022c1ee219607e83c09a8
canon_sha256:               b83a99feccac173bd3c9c5851c5874ca27cbd135f71d136d793b45f86c8a87f7
canon_bytes:                992352
action_layer:               L1 (symbolic mathematical proof over F_5 and Q)
scientific_code_status:     NONE / NOT_RUN
physical_status:            NOT_READY
recommendation:             DO NOT PROMOTE (keep as NON-CANONICAL note under notes/C-FUNDED-TWO-USE-CONTINUING-APPARATUS-N/)
```

---

## 1. Candidate statement-to-proof mapping

| Subclaim ID | Statement summary | Exact `PROOF.md` section & theorem | Domain of validity | Boundary / refusal / separation witness | Upstream frontier owner (untouched) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `S1` | Global bijectivity of $L_{\mathrm{buf}}, F, H_{B,A}, H_{B,B}$, global involutivity $H_{B,A}^2 = H_{B,B}^2 = \mathrm{id}$, and two-sided permutation $G_B$ on $\mathcal{A}_B \times (\mathbb{Z}/8\mathbb{Z})$ | Section 1, `Theorem 1` & `Theorem 2` | All states in $\mathcal{Z}_B$ and $\mathcal{A}_B \times (\mathbb{Z}/8\mathbb{Z})$ for any $B \in \mathbb{Q}_{\ge 0}$ | Single shared $\sigma \in \{\pm 1\}$ fails on $(p_A, p_B) = ((0,0,0,0), (1,0,0,0))$ at $c=4$ ($b_2 = -R_0 z^{(1)} \ne +R_0 z^{(1)}$) | `QUADRATIC-MEMORY-NATIVE-CONTACT` `[O]` |
| `S2` | Closed-form occupied-wave energy increment $\Delta_B(z_A, z_B) = E_0(z_B) - \frac{s_B(\mu^T z_A)}{10497600}$ with $\mu = (145483, 173653, 173653, 142153)^T$ and complete 25-pair rational census | Section 2, `Theorem 3` | All $(z_A, z_B) \in \mathbb{Q}^4 \times \mathbb{Q}^4$ on accepted-A common-ready states $\mathcal{R}_{(c_0, c_1, b_{\mathrm{init}}, B)}$ | Cold formula $\Delta_B^{\mathrm{cold}} = E_0(z_B)$ errs by $-\frac{s_B(\mu^T z_A)}{10497600} \ne 0$ on all $16$ pairs with $h_A, h_B \in \{1,2,3,4\}$ | `QUADRATIC-MEMORY-NATIVE-CONTACT` `[O]` |
| `S3` | Sharp input-independent two-use funding condition $B_* = \frac{8224427}{10497600} \le b_{\mathrm{init}} \le B$ (canonical store $b_{\mathrm{init}} = B = \frac{4}{5}$) and exact four-branch classifications | Section 2, `Theorem 4` | All $25$ pairs in $Z_5 \times Z_5$ and all $390{,}625$ native pairs $(p_A, p_B) \in \mathbb{F}_5^4 \times \mathbb{F}_5^4$ on $\mathcal{R}_{(c_0, c_1, b_{\mathrm{init}}, B)}$ | $B = \frac{2}{5}$ refuses Contact B on $12$ pairs (e.g. $(3,3)$); $B = \frac{1}{5}$ partitions $Z_5^2$ into $6$ `(ACC,ACC)`, $9$ `(ACC,REF)`, $6$ `(REF,ACC)`, $4$ `(REF,REF)`; warm active tape $A_{\mathrm{init}}=(0,e_0)$ shifts $\Delta_B$ to $\frac{9}{10}$ | `QUADRATIC-MEMORY-NATIVE-CONTACT` `[O]` |
| `S4` | Unified four-cut retention $b_0, b_1, b_2, b_3$ in $(A_0, A_1, B_1, B_0)$ at $c=7$, archive-independent source decoder on `(ACC, ACC)`, accepted-zero vs. refusal discrimination, and exact native left inverse $V^{-5}$ | Section 3, `Theorem 5` | All $390{,}625$ native input pairs on $\mathcal{R}_{(c_0, c_1, b_{\mathrm{init}}, B)}$ | At $b_{\mathrm{init}} = B = \frac{1}{5}$ and $c_1 = 0$, $(h_A, h_B) \in \{(0,0), (0,3), (3,0), (3,3)\}$ all give $(b_0, b_1, b_2, b_3) = (0,0,0,0)$ and $(W_{\mathrm{final}}, b_{\mathrm{final}}) = (0, \frac{1}{5})$, separated only by $(\sigma_A, \sigma_B)_{\mathrm{final}}$ | `QDD-INSTRUMENT-APPARATUS` `[O]` |
| `S5` | Joint energy-work-store invariants $E_{\mathrm{full}}(X) - W = \mathrm{const}$, $E_{\mathrm{full}}(X) + b = \mathrm{const}$, $W + b = \mathrm{const}$ across all 8 phases (counting stored tape energy once) | Section 4, `Theorem 6` | All trajectories in $\mathcal{Z}_B$ | Double-counting tape energy breaks invariance at $F$-steps $c \in \{2,3,5,6\}$ | `QUADRATIC-MEMORY-NATIVE-CONTACT` `[O]` |
| `S6` | Conditioned two-use calibration-to-prediction theorem in $\mathcal{A}_{\mathrm{lin}}^{(2)}$ on $Z_5 \times Z_5 \subset \Pi_2 \times \Pi_2$ ($7$ calibration runs $\to 18$ out-of-sample pairs, or $5 \to 20$ under rank-one $\Omega$) and non-identifiability boundaries | Section 4, `Theorem 7` | $\mathcal{A}_{\mathrm{lin}}^{(2)}|_{\Pi_2}$ ($\dim_{\mathbb{Q}} = 39$, or $37$ under rank-one $\Omega$) on `(ACC, ACC)` Blank-Ready states | $51$-dimensional out-of-plane kernel $\mathcal{K}_\perp^{(2)}$ on $\Pi_\perp = \mathbb{Q}e_2 \oplus \mathbb{Q}e_3$ and cubic separator $q_3(z_0, z_1) = z_0 z_1(2z_0 - 1)$ vanishing on $\{z^{(0)}, z^{(1)}, z^{(2)}, z^{(4)}\}$ with $q_3(z^{(3)}) = \frac{1}{2}$ | `QDD-INSTRUMENT-APPARATUS` `[O]` |
| `S7` | Byte-for-byte indistinguishability from full matched classical comparator $\mathcal{M}_{\mathrm{matched}}^{(2)}$ and five restricted-comparator separation witnesses | Section 4, `Theorem 8` | All $390{,}625$ native input pairs on $\mathcal{R}_{(c_0, c_1, b_{\mathrm{init}}, B)}$ | Explicit rational witnesses separating $\mathcal{M}_{\mathrm{single}}$, $\mathcal{M}_{\mathrm{cold}}$, $\mathcal{M}_{2\text{-slot}}$, $\mathcal{M}_{1\sigma}$, and $\mathcal{M}_{\text{no-}\sigma}$ | `QDD-INSTRUMENT-APPARATUS` `[O]` |

---

## 2. Recommendation: **DO NOT PROMOTE**

1. **L1 incubation scope (`NON-CANONICAL`):** All results in `C-FUNDED-TWO-USE-CONTINUING-APPARATUS-N` are symbolic L1 mathematical theorems over $\mathbb{F}_5$ and $\mathbb{Q}$ under `notes/C-FUNDED-TWO-USE-CONTINUING-APPARATUS-N/` (`scientific_code_status: NONE / NOT_RUN`, `physical_status: NOT_READY`).
2. **Conditional L1 primitives:** The delayed-label buffer capture $L_{\mathrm{buf}}$ and the two bounded-store contact involutions $H_{B,A}, H_{B,B}$ are admitted as explicit conditional L1 primitives and are not compiled from native $U$ or derived from $J$.
3. **No public Canon or registry promotion:** No changes are proposed or permitted to `canon/CANON.md`, `canon/CORE.md`, `canon/FRONTIER.md`, `canon/REGISTRY.tsv`, `canon/CHANGELOG.md`, or `canon/SHA256SUMS`. Both `QUADRATIC-MEMORY-NATIVE-CONTACT` `[O]` and `QDD-INSTRUMENT-APPARATUS` `[O]` remain open at their current canonical scope.
