# Result — `P-INTEGER-SECOND-ORDER-NOETHER-CLOSURE-3`

Status: PASS
Scope: NON-CANONICAL, NEW_DECLARED L1
Fired falsifiers: none (`0` of `22` registered falsifiers fired)

## 1. Executive Summary

Following the public six-file prospective pin [`56437c4ef2c2e3a5aee679bb87b693395213f644`](https://github.com/mathorn1973/twist-j/commit/56437c4ef2c2e3a5aee679bb87b693395213f644) recorded on [Issue #1655](https://github.com/mathorn1973/twist-j/issues/1655#issuecomment-6276903848), the first formal execution of `python -I probes/P-INTEGER-SECOND-ORDER-NOETHER-CLOSURE-3/verify.py` passed with `exit_code = 0`, `stderr_bytes = 0`, and `1022` bytes (`27` lines, SHA-256 `16dd61af54d97da110bd5d01eaabb834d2b656e4c9bac69874dcca4a584075ee`) of exact ASCII/LF output, with byte-for-byte agreement between `verify.py` (incidence arrays, form `(3.7a)` of $S_2$, analytic polarized gradients, and four-point directional derivatives) and `breaker.py` (nested state arrays, form `(3.7b)` of $S_2$, nilpotent `Dual` automatic differentiation, and sparse $36\times 36$ generator matrices).

This probe resolves the three explicit second-order obligations exposed by `P-INTEGER-CUBIC-NOETHER-CLOSURE-1` ([#1653](https://github.com/mathorn1973/twist-j/issues/1653), [#1654](https://github.com/mathorn1973/twist-j/pull/1654)) while isolating the exact third- and fourth-order truncation remainders that govern the next step of the discrete gravitational construction:

1. **Exact Off-Shell Second-Order Noether Identity:**
   With the prefix-sum multiplier dressing $\Psi_n[M] = \sum_{b=1}^n \mu_b$ ($1 \le n \le T-1$, $\Psi_0[M] = \Psi_T[M] = 0$), residual multipliers $\widetilde M[M] = M - \Gamma(\Psi[M])$, second-order action term
   $$S_2[x, M] = -D_x S_{\mathrm{int}}[x, \widetilde M[M]][G_{\Psi[M]} x] + \frac{1}{2}\mathrm{Hess}_{A_{\mathrm{aut}}}(G_{\Psi[M]} x, G_{\Psi[M]} x)$$
   (equivalently form `(3.7b)` $-D_x S_{\mathrm{int}}[x, M][G_{\Psi[M]} x] - \frac{1}{2}\mathrm{Hess}_{A_{\mathrm{aut}}}(G_{\Psi[M]} x, G_{\Psi[M]} x) - D_x A_{\mathrm{aut}}(x)[G_{\Psi[M]}^2 x]$), and second-order field generator $\delta_2^{(\psi)} x = G_{\Psi[M]} G_\psi x$, the off-shell second-order Noether identity
   $$\boxed{\delta_0^{(\psi)} S_2 + \delta_1^{(\psi)} S_{\mathrm{int}} + \delta_2^{(\psi)} S_0 = 0}$$
   holds identically across all $126$ fixture-parameter pairs ($6$ fixtures $\times$ $21$ parameters).
   - On the witness state of `#1654` ($h_3 = (1,0,0,0,0)$, $\alpha_3 = 1$, $\psi_2 = \psi_3 = (1,0,0,0,0)$), where $\Psi_3[M] = (1,1,1,1,1)$, the `#1654` obstruction $\delta_1^{(\psi)} S_{\mathrm{int}} = 115/324$ is cancelled by $\delta_0^{(\psi)} S_2 = 0$ and $\delta_2^{(\psi)} S_0 = -115/324$.
   - On the nontrivial split witness ($\alpha_2 = \alpha_3 = 1$), where $\Psi_2[M] = (1,1,1,1,1)$ and $\Psi_3[M] = (2,2,2,2,2)$, all three terms are nonzero and sum to zero:
     $$\delta_0^{(\psi)} S_2 = \frac{115}{324}, \qquad \delta_1^{(\psi)} S_{\mathrm{int}} = \frac{115}{324}, \qquad \delta_2^{(\psi)} S_0 = -\frac{115}{162}, \qquad \text{sum} = 0$$
     (`SECOND_ORDER_SPLIT=115/324,115/324,-115/162`).
2. **Exact Pure-Gauge Field Redefinition Completion:**
   For any pure-gauge multiplier assignment $M = \Gamma(\psi)$, $\Psi_n[\Gamma(\psi)] = \psi_n$ and $\widetilde M[\Gamma(\psi)] = 0$, so $S_2[x, \Gamma(\psi)] = \frac{1}{2}\mathrm{Hess}_{A_{\mathrm{aut}}}(G_\psi x, G_\psi x)$ supplies the exact quadratic Taylor term of $A_{\mathrm{aut}}(x - \epsilon G_\psi x)$:
   $$\boxed{S_{\le 2}(x, \tau, p, \Gamma(\psi); \epsilon) = A_{\mathrm{aut}}(x - \epsilon G_\psi x)}$$
   with zero defect across all $504$ pure-gauge redefinition checks (`PURE_GAUGE_S2_COMPLETION=115/648;0`, cancelling the $-115/648$ remainder of `#1654`).
3. **Order-$\epsilon^2$ Extended Commutator Cancellation and Order-$\epsilon^3, \epsilon^4$ Residual:**
   For the multiplier-dependent vector fields $\hat\delta_\psi = \delta_0^{(\psi)} + \epsilon \delta_1^{(\psi)} + \epsilon^2 \delta_2^{(\psi)}$ on the full $133$-coordinate state space at $T = 5$, the multiplier variation $\delta_0^{(\psi)} \Psi_n[M] = \psi_n$ produces the order-$\epsilon^2$ cross-commutator
   $$(\delta_0^{(\psi)} \delta_2^{(\eta)} - \delta_0^{(\eta)} \delta_2^{(\psi)}) x = (G_\psi G_\eta - G_\eta G_\psi) x = -[\delta_1^{(\psi)}, \delta_1^{(\eta)}] x,$$
   so the bare order-$\epsilon^2$ commutator $(-1/4, 1/4, 0, 0, 0)$ of `#1654` is cancelled identically (`EXTENDED_COMMUTATOR_CANCELLATION=-1/4,1/4,0,0,0;1/4,-1/4,0,0,0;0,0,0,0,0`) across all $1140$ ordered parameter pairs ($6$ fixtures $\times$ $\binom{20}{2}$ pairs):
   $$\boxed{[\hat\delta_\psi, \hat\delta_\eta]_{\le 2} = 0.}$$
   The exact full state-space Lie bracket reduces purely to the third- and fourth-order physical-field residuals:
   $$[\hat\delta_\psi, \hat\delta_\eta] x = \epsilon^3 C_3(\psi, \eta; x, M) + \epsilon^4 C_4(\psi, \eta; x, M),$$
   with $C_3(\psi, \eta; x, M)_{h,1} = (-1/8, 1/8, 0, 0, 0)$ on the frozen nonclosure witness (`THIRD_ORDER_COMMUTATOR_RESIDUAL=-1/8,1/8,0,0,0`).
4. **Exact Truncation Remainders $W_3, W_4$ and Quartic Stencil Witness:**
   Along the joint deformation $\hat\delta_\psi z = \delta_0^{(\psi)} M + \epsilon \delta_1^{(\psi)} x + \epsilon^2 \delta_2^{(\psi)} x$, orders $\epsilon^0, \epsilon^1, \epsilon^2$ vanish identically off-shell, leaving
   $$\hat\delta_\psi S_{\le 2}(\epsilon) = \epsilon^3 W_3(\psi; x, M) + \epsilon^4 W_4(\psi; x, M), \qquad W_3 = \delta_1^{(\psi)} S_2 + \delta_2^{(\psi)} S_{\mathrm{int}}, \quad W_4 = \delta_2^{(\psi)} S_2.$$
   On the witness state ($\alpha_3 = 1$), $W_3 = -1/8 + 1/4 = 1/8$, $W_4 = -115/1296$, and $\hat\delta_\psi S_{\le 2}(1) = 47/1296$ (`THIRD_FOURTH_REMAINDERS=1/8,-115/1296,47/1296`). Because $S_2[x, M]$ is quadratic in $M$ and quadratic in $x$, the directional polynomial $p(\eta) = S_{\le 2}(z + \eta \hat\delta_\psi z; 1)$ is quartic in $\eta$; the four-point stencil gives the exact derivative $p'(0) = 47/1296$, whereas the two-point central difference $(p(1) - p(-1))/2 = 157/1296$ differs by the exact cubic coefficient $c_3 = 1/32$ (`QUARTIC_CENTRAL_DEFECT=1/32`).
5. **Exact Common-Denominator Integer Lifts:**
   - At integer scale $16 m D^3 Q_\psi$, the integer second-order Noether identity $\widehat\Delta_0^{(\psi)} + \widehat\Delta_1^{(\psi)} + \widehat\Delta_2^{(\psi)} = 0$ holds across all $126$ checks (`INTEGER_SECOND_ORDER_NOETHER=126`).
   - At common denominator $D'' = 80 D^2 Q_\psi$ ($288\,000$ for $Q_\psi = 1$ and $2\,016\,000$ for $Q_\psi = 7$ at $D = 60$), the second-order displaced state $z' = z + \delta_0^{(\psi)} M + \epsilon \delta_1^{(\psi)} x + \epsilon^2 \delta_2^{(\psi)} x$ is represented by exact integer numerators and preserves $\tau_b', \lambda_b' \in \mathbf{1}^\perp$ and $p_n' \in \ker B^\mathsf{T}$ across all $504$ checks (`INTEGER_SECOND_ORDER_TANGENT_CHECKS=504`).

## 2. Certified Output (`EXPECTED.txt`)

```text
CERTIFICATE=P-INTEGER-SECOND-ORDER-NOETHER-CLOSURE-3
AUTHORITY_FILES=5
GLOBAL_CONFIGURATIONS=6
GLOBAL_VARIATIONS=798
CONTINUITY_VERTICES=120
CONSTRAINT_PROPAGATION_VERTICES=120
INTEGER_CONTINUITY_VERTICES=120
FIRST_ORDER_NOETHER=126
SECOND_ORDER_NOETHER=126
INTEGER_SECOND_ORDER_NOETHER=126
DEFORMATION_CHECKS=504
PURE_GAUGE_REDEFINITION_CHECKS=504
INTEGER_SECOND_ORDER_TANGENT_CHECKS=504
EXTENDED_COMMUTATOR_CHECKS=1140
GLOBAL_S2_GRADIENT_SHA256=74a025a6de971360111126fa8e1ea1a24b26d5be0a28a64a52617f7ca24c4fba
SECOND_ORDER_PAYLOAD_SHA256=869bff9169debc3f8ed0196d52e0c0093ab91f7a9779c8241e6a858250e66bbc
GLOBAL_NEIGHBOR_GRADIENT=29/10368,29/10368,0,0,0;-17/51840
SECOND_ORDER_SPLIT=115/324,115/324,-115/162
THIRD_FOURTH_REMAINDERS=1/8,-115/1296,47/1296
QUARTIC_CENTRAL_DEFECT=1/32
PURE_GAUGE_S2_COMPLETION=115/648;0
EXTENDED_COMMUTATOR_CANCELLATION=-1/4,1/4,0,0,0;1/4,-1/4,0,0,0;0,0,0,0,0
THIRD_ORDER_COMMUTATOR_RESIDUAL=-1/8,1/8,0,0,0
NEGATIVE_CONTROLS=10
CERTIFICATE_RESULT=PASS
BREAKER_RAW_BYTES=IDENTICAL
RESULT=PASS
```

## 3. Explicit Scope Boundaries and Next Obligations

- **Earned Scope:** `PASS, NON-CANONICAL, NEW_DECLARED L1`.
- **What is established:** Exact off-shell second-order Noether invariance $\delta_0^{(\psi)} S_2 + \delta_1^{(\psi)} S_{\mathrm{int}} + \delta_2^{(\psi)} S_0 = 0$, exact pure-gauge quadratic Taylor completion $S_{\le 2}(\epsilon)|_{M=\Gamma(\psi)} = A_{\mathrm{aut}}(x - \epsilon G_\psi x)$, exact order-$\epsilon^2$ extended commutator cancellation $[\hat\delta_\psi, \hat\delta_\eta]_{\le 2} = 0$, and exact common-denominator integer lifts.
- **What remains open:**
  1. The second-order truncated action $S_{\le 2}(\epsilon)$ leaves the explicit third- and fourth-order variation remainders $W_3 = \delta_1^{(\psi)} S_2 + \delta_2^{(\psi)} S_{\mathrm{int}}$ and $W_4 = \delta_2^{(\psi)} S_2$ (`1/8` and `-115/1296` on the witness state).
  2. The second-order truncated generators $\hat\delta_\psi$ commute through $O(\epsilon^2)$ because $\delta_0^{(\psi)} \Psi_n[M] = \psi_n$ cancels the bare $[G_\psi, G_\eta]$ bracket, but leave the explicit third- and fourth-order Lie bracket residual $\epsilon^3 C_3 + \epsilon^4 C_4$ (`(-1/8, 1/8, 0, 0, 0)` at slice `1` on the witness state) because the central-difference operator $G_\psi$ does not satisfy a first-order Leibniz product rule across two time steps.
  3. The multiplier dressing $\Psi_n[M] = \sum_{b=1}^n \mu_b$ is temporally nonlocal (a prefix sum over bonds $1 \le b \le n$) on the finite horizon $\{0, \dots, T\}$. Replacing prefix-sum dressing by a local auxiliary-field or canonical phase-space formulation, and closing or trivializing the $O(\epsilon^3)$ action and commutator residuals, are the concrete next mathematical obligations.
