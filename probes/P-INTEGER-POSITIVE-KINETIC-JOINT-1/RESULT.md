# Result: P-INTEGER-POSITIVE-KINETIC-JOINT-1

Status: `PASS` (`NON-CANONICAL`, `L1`).

## Summary

`P-INTEGER-POSITIVE-KINETIC-JOINT-1` establishes a positive-kinetic joint
variational integer model of the discrete linear TT metric sector coupled
to a scalar source, together with a positive-definite quadratic bond
energy for the two uncoupled homogeneous operators satisfying an exact
discrete work identity, and exact conservation of the canonical
symplectic Wronskian associated with the positive kinetic metric $I_6$ on
the homogeneous sector $a = 0$ (and on tangent variations for general
fixed $a$).

All 6 prospective frozen files (`PREREG.md`, `PROOF.md`, `SOURCE.md`,
`verify.py`, `breaker.py`, `FROZEN.sha256`) were pinned at commit
`bd7e1dada3a4869ecfae76c0aea03c0a88c9983f` and read back from GitHub
before the first execution (`https://github.com/mathorn1973/twist-j/issues/1647#issuecomment-6269491226`).
No post-pin edits were made to any frozen file. Following the public
review (`https://github.com/mathorn1973/twist-j/pull/1648#issuecomment-6270208985`),
this document narrows the post-run scope claims and records explicit
wording errata in the frozen text.

## Verified Mathematical and Computational Claims

1. **Positive-kinetic joint action and simultaneous stationarity:**
   With $m = 324$ and $\ell = (1,-1,0,0,0)$, the joint action on the
   gauge-invariant linearized 3+1 canonical functional $A_2$ is
   $$
   \begin{aligned}
   A_{\mathrm{pos}}[V_{\mathrm{metric}}, \ell_0, N, \chi]
   &= A_2[V_{\mathrm{metric}}, \ell_0, N]
   + \frac{1}{2}\sum_{n\ge 0}(\chi_{n+1} - \chi_n)^2
   - \sum_{n\ge 1}\left(\frac{1}{2}\chi_n^2 - a\chi_n\right) \\
   &\quad + \frac{1}{2}\sum_{n\ge 1}\frac{\chi_n}{m^n}
   \langle \ell, V_{\mathrm{metric},11,n} - V_{\mathrm{metric},22,n}\rangle,
   \qquad a\in\{-1,0,1\}.
   \end{aligned}
   $$
   In $A_{\mathrm{pos}}$, both the TT metric sector and the scalar source
   sector carry positive kinetic sign ($+\frac{1}{2}\|h_{n+1}-h_n\|_2^2$
   and $+\frac{1}{2}(\chi_{n+1}-\chi_n)^2$) and positive potential sign
   ($-\frac{1}{2}\langle h_n, L h_n\rangle$ and $-\frac{1}{2}\chi_n^2$).
   Varying all spatial metric components, lapse, shift, and scalar source
   before evaluating on the TT representative
   $V_{\mathrm{metric},n} = \operatorname{diag}(h_n, -h_n, 0)$ yields the
   coupled Euler-Lagrange equations
   $$
   (\Delta_c^2 + L)h_n = \frac{\chi_n}{m^n}\ell,
   \qquad
   (\Delta_c^2 + 1)\chi_n = a + \frac{\langle \ell, h_n\rangle}{m^n}.
   $$
   Because $A_{\mathrm{pos}}$ is a quadratic functional, centered unit
   finite differences equal the exact partial derivatives algebraically.
   Across all 30 ready histories ($10\text{ words}\times 3\text{ contexts}$)
   and steps $n=1,\dots,11$, both residuals vanish identically, and all
   `JOINT_VARIATIONS=720` on-shell central variations vanish (`0`), while
   `OFFSHELL_VARIATIONS=36` evaluates the 6 gradient components across 6
   off-shell configurations, matching the exact gradient formulas with at
   least one nonzero component per configuration (18 zero and 18 nonzero
   components).

2. **Positive-definite uncoupled quadratic bond energy, interaction
   account, and discrete work identity:**
   On each bond $(n-1,n)$ for $n\ge 1$, the quadratic bond energy of the
   two uncoupled homogeneous operators $\Delta_c^2 + L$ and
   $\Delta_c^2 + 1$ around the uncoupled equilibrium
   $(\bar h, \bar\chi) = (\frac{1}{5}\mathbf{1}, a)$ is
   $$
   \mathcal{H}_{\mathrm{phys},n}
   = \mathcal{H}_{h,n} + \mathcal{H}_{\chi,n},
   $$
   where
   $$
   \begin{aligned}
   \mathcal{H}_{h,n}
   &= \frac{1}{2}\|h_n - h_{n-1}\|_2^2 + \frac{1}{2}\langle h_{n-1}, L h_n\rangle
   = \frac{1}{2}\left\langle u_{h,n}, \left(I - \frac{1}{4}L\right)u_{h,n}\right\rangle
   + \frac{1}{2}\langle v_{h,n}, L v_{h,n}\rangle \\
   &\ge \frac{3}{8}\|u_{h,n}\|_2^2 + \frac{1}{4}\|v_{h,n}\|_2^2 \ge 0,
   \end{aligned}
   $$
   and
   $$
   \begin{aligned}
   \mathcal{H}_{\chi,n}
   &= \frac{1}{2}(\chi_n - \chi_{n-1})^2 + \frac{1}{2}(\chi_{n-1} - a)(\chi_n - a)
   = \frac{3}{8}u_{\chi,n}^2 + \frac{1}{2}v_{\chi,n}^2 \\
   &\ge \frac{1}{4}\left((\chi_n - a)^2 + (\chi_{n-1} - a)^2\right) \ge 0.
   \end{aligned}
   $$
   Across all 30 ready histories and bonds $n=1,\dots,12$,
   $\mathcal{H}_{\mathrm{phys},n} > 0$ strictly, and the one-step discrete
   work identity
   $$
   \mathcal{H}_{\mathrm{phys},n+1} - \mathcal{H}_{\mathrm{phys},n}
   = W_n
   = \frac{\chi_n}{m^n}\left\langle \ell, \frac{h_{n+1} - h_{n-1}}{2}\right\rangle
   + \frac{\langle \ell, h_n\rangle}{m^n}\left(\frac{\chi_{n+1} - \chi_{n-1}}{2}\right)
   $$
   holds identically (`HAMILTONIAN_CHECKS=720`). Putting $g_n = m^{-n}$,
   $l_n = \langle \ell, h_n\rangle$, and
   $$
   B_n = \frac{\chi_n l_{n-1} + \chi_{n-1} l_n}{2},
   $$
   one has $W_n = g_n(B_{n+1} - B_n)$, so the interaction-adjusted bond
   functional $J_n = \mathcal{H}_{\mathrm{phys},n} - g_{n-1} B_n$ satisfies
   $$
   J_{n+1} - J_n = (g_{n-1} - g_n) B_n.
   $$
   For word `0011` and $a=0$ at $n=1$, the field induces a strictly
   positive source-sector bond energy $\mathcal{H}_{\chi,2} = \frac{1}{839808} > 0$
   from $\mathcal{H}_{\chi,1} = 0$, while the uncoupled field-sector bond
   energy remains $\mathcal{H}_{h,1} = \mathcal{H}_{h,2} = \frac{53}{432}$;
   the gain $W_1 = \frac{1}{839808}$ (`ZERO_SOURCE_WORK1=1/839808`) is
   accounted for by the interaction term $g_1 B_2 = \frac{1}{324}\cdot\frac{1}{2592} = \frac{1}{839808}$
   ($B_1 = 0$, so $\mathcal{H}_{\mathrm{phys},2} - g_1 B_2 = \mathcal{H}_{\mathrm{phys},1}$).

3. **Canonical symplectic Wronskian associated with the positive kinetic
   metric $I_6$ (`SYMPLECTIC`):**
   Because the current-slice coupling operator
   $$
   A_n^+ = \begin{pmatrix} m^{n-1}C & \ell \\ \ell^{\mathsf{T}} & m^n \end{pmatrix}
   $$
   is symmetric in the positive-definite kinetic metric $I_6 \succ 0$, any
   two solutions $(h^{(1)},\chi^{(1)})$ and $(h^{(2)},\chi^{(2)})$ of the
   **homogeneous system $a = 0$** (or any two tangent variations /
   differences from a common particular solution at fixed $a$) conserve
   the canonical symplectic Wronskian associated with $I_6$:
   $$
   \Omega_n^+ = \Omega_{h,n} + \Omega_{\chi,n}
   = \left(\langle h_{n-1}^{(1)}, h_n^{(2)}\rangle - \langle h_n^{(1)}, h_{n-1}^{(2)}\rangle\right)
   + \left(\chi_{n-1}^{(1)}\chi_n^{(2)} - \chi_n^{(1)}\chi_{n-1}^{(2)}\right)
   = \Omega_1^+
   $$
   for all $n\ge 1$ (`SYMPLECTIC_CHECKS=540` across all 45 unordered word
   pairs in homogeneous context $a=0$ for $n=1,\dots,12$). On arbitrary
   uncentered affine solutions at $a \ne 0$, direct substitution gives
   $\Omega_{n+1}^+ - \Omega_n^+ = a(\chi_n^{(1)} - \chi_n^{(2)})$ (for
   example, at `(0010, 0011)` and $a = +1$, $\Omega_1^+ = \Omega_2^+ = \frac{1}{4}$
   while $\Omega_3^+ = \frac{163}{648} \ne \frac{1}{4}$). For the
   homogeneous pair `(0010, 0011)` with $a=0$ at $n=3$, the metric and
   source sectors exchange equal and opposite symplectic flux:
   $$
   \Omega_{h,3} - \Omega_{h,2} = -\frac{1}{136048896},
   \qquad
   \Omega_{\chi,3} - \Omega_{\chi,2} = +\frac{1}{136048896},
   \qquad
   \Omega_3^+ = \Omega_1^+ = \frac{1}{4}
   $$
   (`SYMPLECTIC_EXCHANGE3=-1/136048896,1/136048896,1/4`), whereas the
   indefinite form $\Omega_{h,n} - \Omega_{\chi,n}$ of `#1646` fails to be
   conserved by $-\frac{1}{68024448} \ne 0$.

4. **Exact integer carrier, congruence inversion, reversible funded
   bijection, and Lorentzian signature:**
   With $D_n = 2m^{n(n-1)/2}$ and $r_n = m^{2n-1}$, the 21-integer core
   $x = (P, W, Y, V, H, k)\in \mathcal{C}_0$ advances by
   $$
   P' = m^{k-1}C P - r_k W + Y\ell,
   \qquad
   Y' = m^k Y - r_k V + a D_{k+1} + \langle \ell, P\rangle,
   \qquad
   H' = \rho(M_{\mathrm{loop}}(Y' - Y))(H),
   $$
   invertible via exact modulo-$r_{k-1}$ congruence (`CORE_FIXTURES=172`,
   `FUNDED_CASES=4128`, `IMAGE_DEFECTS=684`), and the 23-coordinate funded
   map $F$ is a reversible bijection satisfying $F^{-1} = \mathrm{Rev}\,F\,\mathrm{Rev}$.
   Across all 390 history records
   (`HISTORY_SHA256=9a6f40a91833a8827e87885901dafa8f7eddce8bf3c4043b5b04f0175c537365`),
   $$
   |\chi_n - \chi_n^{\mathrm{auto}}| < \frac{2}{323},
   \qquad
   |\chi_n| < \frac{648}{323} < 3,
   \qquad
   \|h_n - h_n^{\mathrm{free}}\|_\infty < \frac{1630}{209304} < \frac{1}{125},
   $$
   and $-\frac{299}{500} < h_n(r) < \frac{499}{500}$, so
   $\det g_n(r) = -(1 - h_n(r)^2) < -\frac{999}{250000} < 0$.

5. **Concrete witnesses:**
   - Fixed-counter source contrast (`0010`, $n=2$):
     $P_2^{(-)} = (487,167,-230,130,94)$, $Y_2^{(-)} = -1296$;
     $P_2^{(+)} = (491,163,-230,130,94)$, $Y_2^{(+)} = 1296$;
     $h_2^{(+)} - h_2^{(-)} = (\frac{1}{162}, -\frac{1}{162}, 0, 0, 0)$
     (`DIRECT_CONTRAST=1/162,-1/162,0,0,0`).
   - Zero-source reciprocal witness (`0011`, $a=0$):
     At $n=2$, $P_2 = (94,165,165,94,130)$, $Y_2 = -1$, $D_2 = 648$, so
     $\chi_2 = -\frac{1}{648}$ (`ZERO_SOURCE_CHI2=-1/648`), and the sharp
     first-step bank threshold is `ZERO_SOURCE_FIRST_BANK=89368`.
     At $n=3$, $P_3 = (22236119,-2269619,-2269620,22236120,28091448)$,
     $Y_3 = -105047$, $D_3 = 68024448$, giving
     $h_3 - h_3^{\mathrm{free}} = (-\frac{1}{68024448}, \frac{1}{68024448}, 0, 0, 0)$
     (`RECIPROCAL_CONTRAST=-1/68024448,1/68024448,0,0,0`) and continued
     feedback contrast $\chi_3 - \chi_3^{\mathrm{first}} = -\frac{71}{68024448}$
     (`CONTINUED_SOURCE_CONTRAST=-71/68024448`).

## Explicit Wording Errata in the Frozen `PREREG.md` and `PROOF.md`

The following terminology clarifications apply to the frozen prose without
affecting any formula, bound, or executable test:
1. **Unxentered vs homogeneous/tangent Wronskian:** `PREREG.md` §4.3 and
   `PROOF.md` §4.3 correctly state the uncentered Wronskian conservation
   theorem for $a = 0$; any general-$a$ reading requires tangent variations
   or centering around a common particular solution because
   $\Omega_{n+1}^+ - \Omega_n^+ = a(\chi_n^{(1)} - \chi_n^{(2)})$ on
   uncentered affine solutions.
2. **Uncoupled bond energy vs interaction energy:** $\mathcal{H}_{\mathrm{phys},n}$
   is the positive quadratic bond energy of the two uncoupled homogeneous
   operators around the uncoupled equilibrium $(\frac{1}{5}\mathbf{1}, a)$
   (which is not the coupled equilibrium for $a \ne 0$). The interaction
   contribution is tracked through $W_n = g_n(B_{n+1} - B_n)$ and
   $J_n = \mathcal{H}_{\mathrm{phys},n} - g_{n-1}B_n$.
3. **Symplectic terminology:** The positive-definite object is the kinetic
   metric $I_6 \succ 0$; $\Omega_n^+$ is the canonical alternating
   symplectic Wronskian associated with $I_6$, rather than a quadratic
   form with signature.
4. **Reversible funded bijection vs involution:** In `PREREG.md` / `PROOF.md`,
   "funded involution" means the $\mathrm{Rev}$-reversible bijection
   $F^{-1} = \mathrm{Rev}\,F\,\mathrm{Rev}$ ($\mathrm{Rev}$ is the
   involution; $F$ has orbits of periods $2, 4, 6$).
5. **Centered finite differences:** Centered unit differences of
   $A_{\mathrm{pos}}$ equal exact partial derivatives because $A_{\mathrm{pos}}$
   is quadratic; positive definiteness is not required for this identity.

## Scope and Open Limits

- Scope is `NON-CANONICAL`, `L1`. No canonical file in `canon/` is modified.
- Because the interaction term $\frac{\chi_n}{m^n}\langle \ell, h_n\rangle$
  is explicitly step-dependent via $g_n = m^{-n}$, $J_{n+1} - J_n = (g_{n-1} - g_n)B_n$
  is non-zero in general. An autonomous constant-coupling formulation with
  an exactly conserved interaction-inclusive total Hamiltonian and discrete
  Legendre map is established in the successor probe
  `P-INTEGER-AUTONOMOUS-JOINT-ENERGY-1` (Draft PR #1650, issue #1649).
- The model remains within the linear 3+1 TT metric sector coupled to a
  scalar source on the 5-site ring; full nonlinear discrete gravitational
  dynamics and constraint propagation remain open.

## Exact Output (`EXPECTED.txt`, 720 bytes, SHA-256 `5b050c5aab38db6bb8865fe00ca5b023a1a73f36b25c9ba3d37c863f3ac8ff0a`)

```text
CERTIFICATE=P-INTEGER-POSITIVE-KINETIC-JOINT-1
AUTHORITY_FILES=5
TRANSPORT_CHECKS=133
HOLONOMY_CHECKS=95
CORE_FIXTURES=172
FUNDED_CASES=4128
IMAGE_DEFECTS=684
HISTORY_RECORDS=390
HISTORY_SHA256=9a6f40a91833a8827e87885901dafa8f7eddce8bf3c4043b5b04f0175c537365
JOINT_VARIATIONS=720
OFFSHELL_VARIATIONS=36
HAMILTONIAN_CHECKS=720
SYMPLECTIC_CHECKS=540
DIRECT_CONTRAST=1/162,-1/162,0,0,0
ZERO_SOURCE_CHI2=-1/648
RECIPROCAL_CONTRAST=-1/68024448,1/68024448,0,0,0
CONTINUED_SOURCE_CONTRAST=-71/68024448
ZERO_SOURCE_WORK1=1/839808
SYMPLECTIC_EXCHANGE3=-1/136048896,1/136048896,1/4
ZERO_SOURCE_FIRST_BANK=89368
CYCLE_PERIODS=2,4,6,2,4,6,2,4,6
NEGATIVE_CONTROLS=PASS
CERTIFICATE_RESULT=PASS
BREAKER_RAW_BYTES=IDENTICAL
RESULT=PASS
```
