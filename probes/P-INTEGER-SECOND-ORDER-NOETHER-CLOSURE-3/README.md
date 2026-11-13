# `P-INTEGER-SECOND-ORDER-NOETHER-CLOSURE-3`

- **Status:** `PASS`
- **Scope:** `NON-CANONICAL, NEW_DECLARED L1`
- **Ownership Issue:** [#1655](https://github.com/mathorn1973/twist-j/issues/1655)
- **Prospective Pin:** [`56437c4ef2c2e3a5aee679bb87b693395213f644`](https://github.com/mathorn1973/twist-j/commit/56437c4ef2c2e3a5aee679bb87b693395213f644) ([receipt](https://github.com/mathorn1973/twist-j/issues/1655#issuecomment-6276903848))

## Overview

Exact finite-horizon ($T = 5$, $133$ independent coordinates) verification of the second-order Barnich-Henneaux / Noether action extension $S_{\le 2}(\epsilon) = S_0 + \epsilon S_{\mathrm{int}} + \epsilon^2 S_2$ and multiplier-dressed second-order generator $\hat\delta_\psi = \delta_0^{(\psi)} + \epsilon \delta_1^{(\psi)} + \epsilon^2 \delta_2^{(\psi)}$ with $\delta_2^{(\psi)} x = G_{\Psi[M]} G_\psi x$ and prefix-sum multiplier dressing $\Psi_n[M] = \sum_{b=1}^n (\alpha_b \mathbf{1} + \lambda_b)$:

- **Off-shell second-order Noether identity:** $\delta_0^{(\psi)} S_2 + \delta_1^{(\psi)} S_{\mathrm{int}} + \delta_2^{(\psi)} S_0 = 0$ across all $126$ fixture-parameter pairs, cancelling the $115/324$ witness of `#1654` (`SECOND_ORDER_SPLIT=115/324,115/324,-115/162` on $\alpha_2 = \alpha_3 = 1$).
- **Pure-gauge field-redefinition completion:** $S_{\le 2}(x, \tau, p, \Gamma(\psi); \epsilon) = A_{\mathrm{aut}}(x - \epsilon G_\psi x)$ with zero defect across all $504$ checks (`PURE_GAUGE_S2_COMPLETION=115/648;0`).
- **Order-$\epsilon^2$ extended commutator cancellation:** $[\hat\delta_\psi, \hat\delta_\eta]_{\le 2} = 0$ across all $1140$ parameter pairs (`EXTENDED_COMMUTATOR_CANCELLATION=-1/4,1/4,0,0,0;1/4,-1/4,0,0,0;0,0,0,0,0`), with exact order-$\epsilon^3, \epsilon^4$ residual $\epsilon^3 C_3 + \epsilon^4 C_4$ (`THIRD_ORDER_COMMUTATOR_RESIDUAL=-1/8,1/8,0,0,0`).
- **Common-denominator integer lifts:** Exact integer second-order Noether identity at scale $16 m D^3 Q_\psi$ (`126` checks) and exact integer displaced state at denominator $D'' = 80 D^2 Q_\psi$ (`504` checks).

## Reproduction

```bash
python3 probes/P-INTEGER-SECOND-ORDER-NOETHER-CLOSURE-3/verify.py
```
