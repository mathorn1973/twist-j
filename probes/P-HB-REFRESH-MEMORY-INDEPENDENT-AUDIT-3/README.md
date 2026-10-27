# P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-3

**PUBLIC / NON-CANONICAL / L1 — Independent Audit of Two-Contact Wave-Summary Memory Ranks and Refresh Laws on the 705-Site $D_3$ Carrier**

- **Issue:** [#1528](https://github.com/mathorn1973/twist-j/issues/1528)
- **Primary Lane:** [#1525](https://github.com/mathorn1973/twist-j/issues/1525) (`notes/C-HB-REFRESH-MEMORY-BOUNDARY-N`)
- **Program:** [#1506](https://github.com/mathorn1973/twist-j/issues/1506) / [#1548](https://github.com/mathorn1973/twist-j/issues/1548)
- **Preserved Predecessors:** `P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-1` (pin `bda14aabb495be1db5790c86b6a68d6721cb1fab`, negative report `475a033091db921b28fb409707353ef49870050e`, `PARTIAL / STOP`, NOT `ABANDONED`) and `P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-2` (pin `453e4404bf987f7b5747b5bb59351ee459dade7f`, negative report `c8d4fd675490feeeeab06a15a8b1ff5fa06bdd29`, `PARTIAL / STOP`, NOT `ABANDONED`)
- **Audit Owner:** `Antigravity-20261017-v103-hb-refresh-memory-audit`
- **Author:** A. M. Thorn `<thorn@twistj.com>`, Apache-2.0
- **Action Layer:** `L1`

## Overview

This directory is the fresh successor to `P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-1` (where `det4` matched the factored target $\frac{1}{5668704000}$ and then halted on a hand-multiplied denominator typo `Q(3, 1698693120000)` instead of `Q(3, 17006112000)`) and `P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-2` (where Stages 1–5 and all $2000$ single-contact and $480$ two-contact cases in Stage 6 passed, and the post-loop regime-coverage assertion `missing-two-kind-zero_cost_accept` halted because the first source pair was written as `((0, 3), (2, 4))` instead of the zero-source pair `((0, 4), (2, 4))`). It contains the independent mathematical proof (`PROOF.md`) and standalone, zero-dependency exact rational/integer audit verifier (`break.py`, invoked through `verify.py`) testing the four targets of [#1528](https://github.com/mathorn1973/twist-j/issues/1528) on the canonical $705$-site finite Dirichlet domain $D = Y + B_0 + B_0 \subset \mathbb{Z}^3$ ($1426$ full wave/tape coordinates):

1. **Exact Refresh Identities on All $1426$ Full Wave/Tape Basis Inputs ($5 \times 1426 = 7130$ Exact Coefficients):**
   $$\rho(FX) = \gamma(X)\mathbf{1}_2 + 2 M a_0, \qquad \gamma(FX) = \delta(X) - \frac{1}{5} h^T a_0, \qquad \rho(F^2 X) = \left(\delta(X) - \frac{1}{5} h^T a_0\right)\mathbf{1}_2 + 2 M a_1.$$
2. **Fixed Linear Wave-Summary Kernel Criteria and Exact Minors:**
   - Prediction at horizon $n \in \{0, 2\}$ (both for exact pre-guard work and for Boolean guard decisions across admissible $(b, B)$) holds iff $\ker L \subseteq \ker(\rho, \delta)$, with sharp minimum rank $3$ certified by the $3 \times 3$ minor on $((0, s_0), (0, s_1), (0, \delta_{(10,0,0)}))$ of determinant $\frac{3}{5} \cdot \left(-\frac{1}{10 \cdot 324^2}\right) = -\frac{3}{5248800} = -\frac{1}{1749600}$.
   - Prediction at horizon $n \in \{0, 1, 2\}$ holds iff $\ker L \subseteq \ker(\rho, \gamma, \delta)$, with sharp minimum rank $4$ certified by inserting $(0, \delta_{(6,0,0)})$ as the third column, determinant $\frac{3}{5} \cdot \left(-\frac{1}{10 \cdot 324}\right) \cdot \left(-\frac{1}{10 \cdot 324^2}\right) = \frac{3}{17006112000} = \frac{1}{5668704000}$.
3. **Equal-Energy, Equal-Tape Opposite-Velocity Counterexample to $(\rho, \gamma)$ Closure:**
   - $X_\pm = (u = 0, v = \pm \delta_{(10,0,0)}, 0, 0, 0, 0)$ share $\rho = (0, 0)^T$, $\gamma = 0$, $E_{\mathrm{full}} = 1/2$, and zero tapes through $n = 0, 1, 2$, yet have $\delta(X_\pm) = \mp \frac{1}{1049760}$ and $\rho(F^2 X_\pm) = \mp \frac{1}{1049760}\mathbf{1}_2$, yielding distinct accepted work $\frac{419903}{1049760} \ne \frac{419905}{1049760}$ under second contact $A(1, 0)^T$ ($\sigma = +1, B = 1, b = 1/2$).
4. **Finite Two-Contact Reduced Predictor $\xi = (\rho, \delta)$:**
   - With $\kappa^T = \frac{1}{5} e_4^T(A - \frac{1}{2} H K H A) = -\frac{(145483, 173653)}{10497600}$, a guarded first contact updates $\rho \mapsto \rho + \tilde{\sigma}_1 G \eta_2(q_1, r_1)$ and $\delta \mapsto \delta + \tilde{\sigma}_1 \kappa^T \eta_2(q_1, r_1)$, predicting the post-$F^2$ second contact from $(\xi(u, v), a_0, a_1)$ and spectators across all $2000$ single-contact and $480$ two-contact guarded cases.

## Reproduction

```bash
python3 probes/P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-3/verify.py
```
