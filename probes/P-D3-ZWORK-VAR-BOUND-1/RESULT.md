# Result of P-D3-ZWORK-VAR-BOUND-1

**Status: PASS in the first formal local run (two-architecture confirmation pending hosted x86_64 and aarch64 CI on this commit).**

The pinned zero-float standard-library verifier (`verify.py`, SHA-256
`faf10b8b933ce3975ec547c1d40fe5cd10320d17b421c568efb276073feeee09`) passed every
check F01–F06 and rejected all five deliberate negative controls, exiting `0`
with `0` stderr bytes and emitting the `1785` LF bytes committed in
`EXPECTED.txt` (SHA-256
`aa47b896720474f252f510dbe614add4676ea740376d7fad05a747c918448057`).

## Closed mathematical findings

1. **Cyclotomic Gram metric and sharp nonzero floor (F01 — PASS):**
   On \(\mathcal{O} = \mathbb{Z}[\zeta_5]\), \(Q_e(z) = 2q(z) = \operatorname{Tr}(z\bar{z}) = z^T G z\) has exact Gram matrix \(G = 5I_4 - J_4\), inverse \(G^{-1} = \frac{1}{5}(I_4 + J_4)\), \(\det G = 125\), \(\operatorname{spec}(G) = \{1, 5, 5, 5\}\), sharp nonzero floor \(q(z) \ge 2\) (\(2q(z) \ge 4\)) attained on exactly the `10` units \(\mu_{10}\), and low-energy shells \(2q \in \{0, 4, 6, 10, 14\} \mapsto \{1, 10, 20, 20, 60\}\).

2. **Exact vacuum and purely magnetic string lower bounds (F02 — PASS):**
   On \(D_3(L)\), edge-disjoint cuts enforce \(Q_E \ge 4d\) for a unit dipole at graph distance \(d\) (saturated at `4, 8, 12, 16` for \(d = 1..4\) on \(D_3(10)\)) and \(Q_E \ge 4L\) for a charge-free periodic unit \(x\)-flux configuration (saturated at `24, 32, 40, 48` for \(L = 6, 8, 10, 12\)). Over any purely magnetic stationary background \((0, 0, B_{\mathrm{bg}})\), the absence of an \(E\)-\(B\) cross-term preserves \(\Delta Q_{\mathrm{tot}} \ge 4L\), and over any fixed \(E_{\mathrm{bg}}\) the exact parallelogram identity holds.

3. **Sharp upper bound \(Z_{\mathrm{work,cont}}^{\mathrm{var}}(\beta, L) < 1/4\) (F03, F04 — PASS):**
   For the variance-based stiffness estimator
   \[
   Z_{\mathrm{work,cont}}^{\mathrm{var}}(\beta, L) := \frac{\beta\,\langle q(M_x)\rangle_\beta}{8L}
   = \frac{1}{4} - \frac{\pi^2}{16\beta L^3} \left\langle \left(\sum_{e \in E} \Delta x_e m_e\right)^T G^{-1} \left(\sum_{e \in E} \Delta x_e m_e\right) \right\rangle_{\mathrm{Villain}},
   \]
   the written 3D Villain \(XY^4\) duality proof establishes the strict inequality
   \(Z_{\mathrm{work,cont}}^{\mathrm{var}}(\beta, L) < 1/4\) across its exact domain:
   **all \(\beta > 0\), all finite even \(L \ge 2\), and the zero-divergence equilibrium ensemble over \(D_3(L)\) summing over all global flux sectors**.
   Strictness follows from \(G^{-1} \succ 0\) and strictly positive Boltzmann weight of configurations with nonzero dual current (explicit single-edge witness \(m_{e_0} = (1, 0, 0, 0)\) giving \(m_{e_0}^T G^{-1} m_{e_0} = 2/5 > 0\)).
   The finite audit confirms pointwise 4D Poisson summation to max relative error `1.286e-48` (`< 1e-40`) and exact spin-wave cancellation \(\max_v |(B\,\Delta x)_v| = 0\), \(\sum_e \Delta x_e (\theta_v - \theta_u) = 0\), and Gaussian limit \(1/4\) on \(D_3(2)\), \(D_3(4)\), and \(D_3(6)\).

4. **Finite-volume distinction from \(Z_{\mathrm{work}}^{\mathrm{disc}}\) and exact 3-edge crossover (F05 — PASS):**
   In 130-digit `Decimal` (primal/dual overlap errors `9.307e-47` on 2-edge and `1.925e-45` on 3-edge), \(Z_{\mathrm{work}}^{\mathrm{var}}(\beta) < 1/4\) holds strictly across all tested \(\beta \in \{0.01, 0.05, 0.10, 0.50, 1.00, 2.00\}\) on both complexes:
   - On the 2-edge complex (\(c = 1/4\)), \(Z_{\mathrm{work}}^{\mathrm{disc}}(\beta) = 1/4\) identically while \(Z_{\mathrm{work}}^{\mathrm{var}}(\beta) < 1/4\) strictly (deficits from `9.267768e-84` at \(\beta = 0.01\) to `2.499977e-1` at \(\beta = 2.00\)).
   - On the 3-edge complex (\(c = 1/3\)), both \(Z_{\mathrm{work}}^{\mathrm{var}}(\beta) < 1/4\) and \(Z_{\mathrm{work}}^{\mathrm{disc}}(\beta) < 1/4\) hold strictly, and their difference \(Z_{\mathrm{work}}^{\mathrm{var}}(\beta) - Z_{\mathrm{work}}^{\mathrm{disc}}(\beta)\) changes sign between \(\beta = 0.10\) (`+1.746870e-8`) and \(\beta = 0.50\) (`-7.709142e-2`). Exact bisection pins the crossover at **\(\beta_* \approx 0.242528416\)**, where both estimators coincide at approximately **`0.24920214`** (`< 1/4`, `abs_diff = 1.914e-43`).

5. **Deliberate negative controls (F06 — PASS):**
   All five controls (`corrupt_gram`, `zero_vortex_truncation`, `perturbed_edge_weight`, `broken_divergence_string`, `constant_sign_3edge`) were rejected as preregistered.

## Scope and open boundaries

- No falsifier fired. Action layer is `L1`; `canon/` is unchanged.
- No dynamical evolution law, Monte Carlo campaign, or coupling selection is included in this probe.
- The open obligation `Q9` remains strictly **`OPEN`**.
- Two-architecture reproduction (`POLICY.md` §4) will be confirmed only when both `architecture-x86_64` and `architecture-aarch64` (plus aggregate `check`) pass on this same pull-request commit against `EXPECTED.txt`.
