# P-U-AFFINE-RECEIVER-INDEPENDENT-AUDIT-2: Result

Status: PASS (NON-CANONICAL / L1 independent adversarial audit of `#1519` / PR `#1520`, assigned in `#1521`)

- **Owner session:** `Antigravity-20261015-abdf12b3`
- **Author:** A. M. Thorn `<thorn@twistj.com>`
- **Predecessor disposition:** `P-U-AFFINE-RECEIVER-INDEPENDENT-AUDIT-1` (`8d6112604793dfbd6fbf4f229ba74d80d3c07a41`) exited nonzero on an auxiliary sharpness witness tuple and is closed with `Status: ABANDONED` at `c29b072fc35f95bc68db0bfbcdf19b7b0e4c855d` on `probe/P-U-AFFINE-RECEIVER-INDEPENDENT-AUDIT-1`. That identifier is permanently consumed.
- **Successor immutable pin:** `725b519cb49de7ccf8de5086ec6543c625e68f1c`
- **First formal run commit (before primary code/result inspection):** `8df07b09001d4b36b1e7a96dc2e57e5d337dde76`
- **Action layer:** `L1` (no Canon promotion, registry edit, or merge of `#1520` is performed by this review)

## 1. Audited Conclusions and Earned Scope

1. **All-affine origin-zero immediate-retention obstruction (confirmed, candidate-T):**
   For any input preparation map $E: \mathbb{F}_5^2 \to \mathbb{F}_5^6$, any fixed affine receiver $R(x) = L x + h$ of arbitrary coordinate count $k \ge 0$, and any fixed total reader $G$, origin-zero evolution under unchanged $U$ forces $z(x_2) \in \{1, 2\}$ and $x_3 \in \{-x_2 + t_3,\; -x_2 + t_4\}$. Any common receiver state $R(x_2(\lambda, \mu)) = r_{\mathrm{ready}}$ yields at most **two** receiver states at $n = 3$:
   $$R(x_3(\lambda, \mu)) \in \left\{\, -r_{\mathrm{ready}} + 2h + L t_3,\;\; -r_{\mathrm{ready}} + 2h + L t_4 \,\right\}.$$
   Hence no fixed reader can produce five distinct second messages at $n = 3$. This bound ($\le 2$) is constructively sharp.
2. **All-affine origin-zero eventual-retention obstruction (confirmed, candidate-T via `U-NATIVE-INVARIANT-AND-NOWRITE`):**
   If $R(x_2) = r_{\mathrm{ready}}$, $G(r_{\mathrm{ready}}) = \mathrm{BLANK}$, and each prepared trajectory eventually retains a permanent nonblank output $\mathrm{PRESENT}(\mu)$ from some finite onset $N(\lambda, \mu) \ge 3$, then every preparation with $z(x_2) = 1$ has $x_2 \in X_1 \subset X_{14}$ in the exact recurrent $X_{14}$ sign fibre $\{V(x_3), -V(x_3)\}$ of $x_3 = g_3(x_2)$ and is excluded by `U-NATIVE-INVARIANT-AND-NOWRITE`, while all remaining preparations have $z(x_2) = 2$ and share the single state $R(x_3) = -r_{\mathrm{ready}} + 2h + L t_4$. By `U-NATIVE-INVARIANT-AND-NOWRITE` at $x_3 \in X_{14}$, at most **one** nonblank second message can ever be permanently retained. This bound ($\le 1$) is also constructively sharp.
3. **Late construction from $n = 5$ and preparation boundary (confirmed, candidate-T / candidate-C):**
   - Both global coordinate splits $(\bar{R}, \bar{S})$ ($3+3$) and $(\tilde{R}, \tilde{S})$ ($2+4$) are exact bijections on $\mathbb{F}_5^6$ ($62,500$ inverse checks).
   - For all $25$ pairs $(\lambda, \mu) \in \mathbb{F}_5^2$, $x_5(\lambda, \mu)$ yields $\mathrm{BLANK}, \mathrm{PRESENT}(\lambda), \mathrm{BLANK}, \mathrm{PRESENT}(\mu)$ at $n = 5, 6, 7, 8$, full checkpoint and receiver return $x_7(\lambda, \mu) = x_5(\lambda, \mu)$ at $n = 7$ (where $g_2$ subsequently acts and mixes coordinates, unlike $g_3/g_4$ at $n = 2$), and permanent retention in the $500$-state closed continuation carrier $\mathcal{C}_{500}$ ($1,000$ transitions, $25,500$ trajectory checks through $n = 1024$).
   - Two $\mathbb{F}_5$ coordinates are necessary and sufficient in the affine-repartition class ($5^1 < 6 \le 5^2$), while bare $(u, v)$ merges recurrent supports into $\{0, 3\}, \{1, 2\}, \{4\}$.
   - Every $0011$ launch window starts at $n = 2m + 1$ with $(\theta_m, \theta_{m+1}, \theta_{m+2}) = (1, 0, 1)$ (including the infinite family $n_k = 3 \cdot 2^k + 5$ for $k \ge 4$), so $\theta_{n-1} = 1$ and $T_1^{-1}(X_0) = \emptyset$: no trace-zero launch $(n, x_n)$ has an immediate predecessor under $U$.

## 2. Explicit Boundaries and Limitations Preserved

- The two-coordinate receiver $\tilde{R} = (D, H)$ uses the source sum $A = a + c$ inside $H = \Sigma + 3(A - B)$ and does not belong to the raw $(u, v, q, r)$ access class of $\bar{R} = (u, v, \Sigma)$.
- First-message persistence ($2 - A(2A + H)C = \lambda$ for $n \ge 9$) shares the reference $H$, and the second source is not emptied ($w_8 = 1 + 2\mu, w_9 = 3\mu \bmod 5$).
- Late $0011$ launches on $X_0$ are stipulated initial states with no $U$-predecessor, not internally reached resets of an origin-zero run.
- The origin-zero negative theorem does not exclude nonlinear receiver coordinates, hidden non-equal receiver states behind a shared $\mathrm{BLANK}$ label at $n = 2$, finite-horizon (non-permanent) retention, added context/clock input, or modified dynamics.
- No Fired Falsifiers: `NONE`.
