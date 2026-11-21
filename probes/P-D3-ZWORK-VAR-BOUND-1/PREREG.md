# P-D3-ZWORK-VAR-BOUND-1 preregistration

**Status: FORMAL PREREGISTRATION / RESULT-EXPOSED / PROOF-FIRST**

Owner: A. M. Thorn, coordinating the exact proof and audit
Branch: `probe/P-D3-ZWORK-VAR-BOUND-1`
Directory: `probes/P-D3-ZWORK-VAR-BOUND-1/`

This probe states and machine-audits the exact cyclotomic metric, vacuum string lower bounds, and the sharp variance-stiffness upper bound \(Z_{\mathrm{work,cont}}^{\mathrm{var}}(\beta, L) < 1/4\) on the periodic 12-edge FCC lattice \(D_3(L)\) over \(\mathcal{O} = \mathbb{Z}[\zeta_5]\). The written derivation and exploratory arithmetic had been exposed before the immutable pin. The first formal verifier invocation takes place only after public readback of the pin.

### Public authority

```text
STATE: ACTIVE
CANON: Public Canon v113
MAIN AT CLAIM: c089e7ec7ecc82f4838c27663d94c040f5cc4ea3
TAG: canon-v113
TAG OBJECT: 3a91e2bee83a3045b17f3aa2895f69deef62d89c
CONTENT_COMMIT: 50d0e94d81e4954b7351bff755ed1889290bb7b8
CANON_SHA256: 47114cb616069242cff36bb499e5fe9b11266a92c744ba3f15a9085c11956b34
CANON_BYTES: 1555510
```

## Field 1: equation and decision

### 1.1 Cyclotomic quadratic form and sharp nonzero floor

Let \(\mathcal{O} = \mathbb{Z}[\zeta_5] \cong \mathbb{Z}^4\) in the power basis \((1, j, j^2, j^3)\) with \(j^4 = -(1 + j + j^2 + j^3)\). For \(z = (a_0, a_1, a_2, a_3) \in \mathbb{Z}^4\), define the local quadratic energy
\[
Q_e(z) := 2q(z) := \operatorname{Tr}_{\mathbb{Q}(\zeta_5)/\mathbb{Q}}(z\bar{z}) = z^T G z,
\qquad
G = 5I_4 - J_4,
\qquad
G^{-1} = \frac{1}{5}(I_4 + J_4),
\]
where \(J_4\) is the \(4 \times 4\) all-ones matrix, \(\det G = 125\), \(\operatorname{spec}(G) = \{1, 5, 5, 5\}\), and \(\operatorname{spec}(G^{-1}) = \{1, 1/5, 1/5, 1/5\}\). Because \(q(z) = |\sigma_1(z)|^2 + |\sigma_2(z)|^2\) is the sum of two positive real numbers whose product is the positive integer algebraic norm \(N_{\mathbb{Q}(\zeta_5)/\mathbb{Q}}(z) \ge 1\) for \(z \neq 0\), AM-GM yields the sharp floor
\[
q(z) \ge 2 \qquad \bigl(2q(z) \ge 4\bigr) \qquad \forall z \in \mathcal{O} \setminus \{0\},
\]
attained precisely on the ten roots of unity \(\mu_{10} = \{\pm j^k : 0 \le k \le 4\}\).

### 1.2 Vacuum and purely magnetic string lower bounds on \(D_3(L)\)

For every even \(L \ge 2\), the periodic 12-edge FCC lattice
\[
D_3(L) = \{(x, y, z) \in \{0, \dots, L-1\}^3 : x + y + z \equiv 0 \pmod 2\}
\]
has \(|V| = L^3/2\) vertices and \(|E| = 6|V| = 3L^3\) positive directed edges \(e = (u \to v)\) along \(\mathrm{DIRS} = \{(1,1,0),(1,-1,0),(1,0,1),(1,0,-1),(0,1,1),(0,1,-1)\}\). Each edge \(e\) carries \(E_e \in \mathcal{O}\), with electric energy \(Q_E[E] = \sum_{e \in E} 2q(E_e) = \sum_{e \in E} E_e^T G E_e\).

1. **Dipole bound:** For any two fixed unit charges \(+1, -1\) at graph distance \(d\) and no other charges, the \(d\) BFS boundary cuts \(\partial B_k\) (\(0 \le k < d\)) are pairwise edge-disjoint and each carries total flux \(\mathbf{1}\), so each contains at least one nonzero edge of cost \(\ge 4\), yielding \(Q_E \ge 4d\) (saturated by a unit shortest-path string).
2. **Periodic unit \(x\)-flux bound:** For any charge-free configuration (\(\operatorname{div}_{D_3} E = 0\)) with unit global \(x\)-flux \(M_x(E) = \mathbf{1}\), the \(L\) transverse \(x\)-slices \(\Sigma_x\) (\(0 \le x < L\), each of \(2L^2\) edges with \(\Delta x_e = +1\)) are pairwise edge-disjoint and each carries flux \(\mathbf{1}\), yielding \(Q_E \ge 4L\) (saturated by a unit \(x\)-string of length \(L\)). Over any purely magnetic stationary background \((0, 0, B_{\mathrm{bg}})\) in \(Q_{\mathrm{tot}} = Q_E + Q_B\), the absence of an \(E\)-\(B\) cross-term gives \(\Delta Q_{\mathrm{tot}} \ge 4L\) identically; over any fixed electric background \(E_{\mathrm{bg}}\), the parallelogram identity gives \(\frac{1}{2}[\Delta Q_E(+\Delta E) + \Delta Q_E(-\Delta E)] = Q_E(\Delta E)\).

### 1.3 Sharp variance-stiffness theorem \(Z_{\mathrm{work,cont}}^{\mathrm{var}}(\beta, L) < 1/4\)

**Scope of the theorem:** The theorem holds for **all \(\beta > 0\)**, **all finite even \(L \ge 2\)**, and the **zero-divergence equilibrium ensemble over \(D_3(L)\) summing over all global flux sectors** \(M(E) \in (\mathbb{Z}^4)^3\).

For a divergence-free configuration \(E \in (\mathbb{Z}^4)^{|E|}\) (\(\operatorname{div}_{D_3} E = 0\)), the global \(x\)-flux is
\[
M_x(E) := \frac{1}{L} \sum_{e \in E} \Delta x_e E_e \in \mathbb{Z}^4,
\]
and the twisted equilibrium partition function is
\[
Z_L(\beta; \phi_x) := \sum_{\operatorname{div}_{D_3} E = 0} \exp\!\left(-\beta \sum_{e \in E} E_e^T G E_e + i\,\phi_x^T M_x(E)\right), \qquad \phi_x \in \mathbb{R}^4.
\]
Define the variance-based continuum stiffness estimator directly by
\[
Z_{\mathrm{work,cont}}^{\mathrm{var}}(\beta, L) := \frac{\beta\,\langle q(M_x)\rangle_\beta}{8L} = \frac{\beta\,\langle M_x^T G M_x\rangle_\beta}{16L}.
\]

**Proof (exact 3D Villain \(XY^4\) duality and spin-wave cancellation):**

1. Enforce \((\operatorname{div}_{D_3} E)_v = 0\) at every vertex \(v \in V\) by integrating over compact dual angles \(\theta_v \in [-\pi, \pi)^4\):
   \[
   Z_L(\beta; \phi_x) = \int_{[-\pi,\pi)^{4|V|}} \left(\prod_{v \in V} \frac{d^4\theta_v}{(2\pi)^4}\right) \prod_{e=(u\to v)} \sum_{E_e \in \mathbb{Z}^4} \exp\!\left(-\beta E_e^T G E_e + i\left(\theta_v - \theta_u + \frac{\Delta x_e}{L}\phi_x\right)^T E_e\right).
   \]
2. Apply the exact 4D Poisson summation identity on every edge \(e\),
   \[
   \sum_{n \in \mathbb{Z}^4} e^{-\beta n^T G n + i u^T n}
   = \frac{\pi^2}{\beta^2 \sqrt{125}} \sum_{m \in \mathbb{Z}^4} \exp\!\left(-\frac{1}{4\beta}(u - 2\pi m)^T G^{-1}(u - 2\pi m)\right),
   \]
   yielding the exact dual 3D Villain \(XY^4\) representation
   \[
   Z_L(\beta; \phi_x) = \left(\frac{\pi^2}{\beta^2 \sqrt{125}}\right)^{|E|} \sum_{\{m_e \in \mathbb{Z}^4\}} \int_{[-\pi,\pi)^{4|V|}} \left(\prod_{v \in V} \frac{d^4\theta_v}{(2\pi)^4}\right) \exp\!\bigl(-S_{\mathrm{Villain}}(\theta, m; \phi_x)\bigr),
   \]
   with
   \[
   S_{\mathrm{Villain}}(\theta, m; \phi_x) = \frac{1}{4\beta} \sum_{e=(u\to v)} \left(\theta_v - \theta_u - 2\pi m_e + \frac{\Delta x_e}{L}\phi_x\right)^T G^{-1} \left(\theta_v - \theta_u - 2\pi m_e + \frac{\Delta x_e}{L}\phi_x\right).
   \]
3. Expand \(S_{\mathrm{Villain}}(\theta, m; \phi_x)\) in powers of \(\phi_x\) around \(\phi_x = 0\):
   - **Quadratic term:** Exactly four of the six positive directions in \(\mathrm{DIRS}\) have \(\Delta x_e = +1\) (and two have \(\Delta x_e = 0\)), so \(\sum_{e \in E} (\Delta x_e)^2 = 4|V| = 2L^3\). Hence
     \[
     \nabla_{\phi_x}\nabla_{\phi_x}^T S_{\mathrm{Villain}}\Big|_{\phi_x = 0} = \frac{\sum_e (\Delta x_e)^2}{2\beta L^2}\, G^{-1} = \frac{L}{\beta}\, G^{-1},
     \]
     independent of \((\theta, m)\).
   - **Identical spin-wave cancellation:** At every vertex \(v \in D_3(L)\), four outgoing edges and four incoming edges have \(\Delta x_e = +1\), so \((B\,\Delta x)_v = 4 - 4 = 0\). Therefore, for **every** \(\theta \in \mathbb{R}^{4|V|}\),
     \[
     \sum_{e=(u\to v)} \Delta x_e (\theta_v - \theta_u) = -\sum_{v \in V} \theta_v (B\,\Delta x)_v \equiv 0.
     \]
     The linear coupling to \(\phi_x\) is therefore purely a function of the integer dual variables \(m\):
     \[
     J_x(m) := \nabla_{\phi_x} S_{\mathrm{Villain}}\Big|_{\phi_x = 0} = -\frac{\pi}{\beta L} \sum_{e \in E} \Delta x_e G^{-1} m_e.
     \]
4. Equating \(-\nabla_{\phi_x}\nabla_{\phi_x}^T \ln Z_L(\beta; \phi_x)\big|_{\phi_x=0}\) in the primal and Villain representations (with \(\langle M_x \rangle_\beta = 0\) and \(\langle J_x \rangle_{\mathrm{Villain}} = 0\) by sign symmetry) yields the exact matrix helicity-modulus identity
   \[
   \langle M_x M_x^T \rangle_\beta = \frac{L}{\beta}\, G^{-1} - \operatorname{Cov}_{\mathrm{Villain}}(J_x) \preceq \frac{L}{\beta}\, G^{-1}.
   \]
5. Contracting with \(\frac{1}{2}\operatorname{Tr}(G \cdot (\cdots))\) (using \(\operatorname{Tr}(I_4) = 4\) and \(G^{-1} G G^{-1} = G^{-1}\)) gives
   \[
   \langle q(M_x) \rangle_\beta = \frac{2L}{\beta} - \frac{\pi^2}{2\beta^2 L^2} \left\langle \left(\sum_{e \in E} \Delta x_e m_e\right)^T G^{-1} \left(\sum_{e \in E} \Delta x_e m_e\right) \right\rangle_{\mathrm{Villain}},
   \]
   and dividing by \(8L/\beta\) gives the exact representation
   \[
   Z_{\mathrm{work,cont}}^{\mathrm{var}}(\beta, L) = \frac{\beta\,\langle q(M_x)\rangle_\beta}{8L} = \frac{1}{4} - \frac{\pi^2}{16\beta L^3} \left\langle \left(\sum_{e \in E} \Delta x_e m_e\right)^T G^{-1} \left(\sum_{e \in E} \Delta x_e m_e\right) \right\rangle_{\mathrm{Villain}}.
   \]
6. **Strict inequality (\(<\, 1/4\)):** Because \(G^{-1}\) is strictly positive definite (\(\operatorname{spec}(G^{-1}) = \{1, 1/5, 1/5, 1/5\}\)) and finite-volume configurations with nonzero dual current carry strictly positive Boltzmann weight for all \(\beta > 0\) and finite even \(L \ge 2\) (explicit witness: \(m_{e_0} = (1, 0, 0, 0)\) on one edge with \(\Delta x_{e_0} = +1\) and \(m_e = 0\) elsewhere gives \(m_{e_0}^T G^{-1} m_{e_0} = 2/5 > 0\) and finite Villain action uniformly on \([-\pi, \pi)^{4|V|}\)), the Villain expectation is strictly positive. Hence
   \[
   Z_{\mathrm{work,cont}}^{\mathrm{var}}(\beta, L) < \frac{1}{4}
   \qquad \forall \beta > 0,\;\; \forall \text{ finite even } L \ge 2.
   \]

### 1.4 Distinction from the finite-volume discrete free-energy estimator and exact 3-edge crossover

On any finite graph with divergence-free flux \(M \in \mathbb{Z}^4\) whose Gaussian covariance is \(\langle M M^T\rangle_\beta^{\mathrm{Gauss}} = \frac{c}{\beta} G^{-1}\), the variance estimator \(Z_{\mathrm{work}}^{\mathrm{var}}(\beta) := \frac{\beta\langle q(M)\rangle_\beta}{8c}\) and the discrete free-energy estimator \(Z_{\mathrm{work}}^{\mathrm{disc}}(\beta) := \frac{\beta}{2c\,\Delta F(\mathbf{1})}\) (where \(\Delta F(\mathbf{1}) := -\ln(Z(\beta; \mathbf{1})/Z(\beta; 0))\)) are distinct definitions at finite volume:

- On the 2-edge cyclotomic complex (\(k = 2\) parallel edges between two vertices, \(c = 1/4\)), \(\Delta F(\mathbf{1}) = 8\beta\), so \(Z_{\mathrm{work}}^{\mathrm{disc}}(\beta) = 1/4\) identically for all \(\beta > 0\), while \(Z_{\mathrm{work}}^{\mathrm{var}}(\beta) < 1/4\) strictly for all \(\beta > 0\).
- On the 3-edge cyclotomic complex (\(k = 3\) parallel edges between two vertices, \(c = 1/3\)), both \(Z_{\mathrm{work}}^{\mathrm{var}}(\beta) < 1/4\) and \(Z_{\mathrm{work}}^{\mathrm{disc}}(\beta) < 1/4\) hold strictly for all \(\beta > 0\), and their difference \(Z_{\mathrm{work}}^{\mathrm{var}}(\beta) - Z_{\mathrm{work}}^{\mathrm{disc}}(\beta)\) changes sign between \(\beta = 0.10\) (positive) and \(\beta = 0.50\) (negative). Direct high-precision bisection locates the exact crossover at \(\beta_* \approx 0.242528416\), where both estimators coincide at approximately \(0.24920214 < 1/4\).

## Field 2: accepted code

```text
file: probes/P-D3-ZWORK-VAR-BOUND-1/verify.py
sha256: faf10b8b933ce3975ec547c1d40fe5cd10320d17b421c568efb276073feeee09
bytes: 37915
command: python3 probes/P-D3-ZWORK-VAR-BOUND-1/verify.py
dependencies: Python standard library
arithmetic: exact integers, rational Fraction, and 130-digit Decimal (zero float, zero complex)
input: fixed mathematical constants and lattice definitions inside verify.py
timeout_seconds: 600
```

## Field 3: carrier and data

- **Primary lattice carrier:** Periodic 12-edge FCC lattice \(D_3(L)\) for even \(L \ge 2\) with edge variables \(E_e \in \mathcal{O} = \mathbb{Z}[\zeta_5] \cong \mathbb{Z}^4\), local energy \(Q_e(z) = 2q(z) = z^T G z\), and the zero-divergence equilibrium ensemble summing over all global flux sectors \(M(E) \in (\mathbb{Z}^4)^3\).
- **Finite audit instances in `verify.py`:**
  - Exact integer enumeration of \([-3, 3]^4\) certifying \(q(z) \ge 2\), \(\mu_{10}\), and all shells \(2q \le 14\) (outside \([-3, 3]^4\), \(z^T G z \ge \|z\|_2^2 \ge 16\)).
  - Exact dipole cuts on \(D_3(10)\) (\(d = 1, 2, 3, 4\)) and periodic \(x\)-cuts on \(D_3(L)\) (\(L = 6, 8, 10, 12\)).
  - Pointwise 4D Poisson summation at \(u = (0.37, -0.81, 1.19, 0.53)\) and \(\beta \in \{0.50, 1.00, 2.00\}\) in 130-digit `Decimal`.
  - Exact \(D_3(L)\) spin-wave cancellation and Gaussian twist coefficient on \(L \in \{2, 4, 6\}\), plus exact `Fraction` strictness witness \(m_{e_0} = (1, 0, 0, 0)\).
  - Exact 130-digit `Decimal` primal and dual evaluations on the 2-edge (\(c = 1/4\)) and 3-edge (\(c = 1/3\)) cyclotomic complexes across \(\beta \in \{0.01, 0.05, 0.10, 0.50, 1.00, 2.00\}\), plus 130-step bisection of the 3-edge crossover on \([0.20, 0.30]\).

## Field 4: systematics

The proof and audit govern strictly the stated equilibrium statistical-mechanical bound for \(Z_{\mathrm{work,cont}}^{\mathrm{var}}(\beta, L) = \beta\langle q(M_x)\rangle_\beta / (8L)\) on \(D_3(L)\) over \(\mathbb{Z}[\zeta_5]\).

- The theorem retains the superscript \(\mathrm{var}\) explicitly and does not conflate \(Z_{\mathrm{work,cont}}^{\mathrm{var}}\) with the finite-volume discrete difference \(Z_{\mathrm{work}}^{\mathrm{disc}}\).
- No deterministic dynamical evolution law, no Monte Carlo campaign, no continuum renormalization claim, and no coupling or \(\alpha\) selection is included or claimed.
- The open obligation `Q9` (selection of a dimensionless electromagnetic coupling) remains strictly `OPEN`.
- Because `verify.py` uses zero IEEE-754 `float` or `complex` arithmetic and relies exclusively on Python `int`, `Fraction`, and deterministic 130-digit `Decimal` (`libmpdec`), output bytes are architecture-independent.

## Field 5: failure thresholds and controls

Every mathematical identity and strict inequality must hold exactly (or within the stated exact `Decimal(130)` truncation tolerance for infinite lattice sums). Any exact violation fires its falsifier:

- **F01.** \(G G^{-1} \neq I_4\), \(\det G \neq 125\), \(\operatorname{spec}(G) \neq \{1, 5, 5, 5\}\), \(\operatorname{spec}(G^{-1}) \neq \{1, 1/5, 1/5, 1/5\}\), any mismatch between \(z^T G z\), \(\operatorname{Tr}(z\bar{z})\), and \(\sum_{r<s}(c_r - c_s)^2\) on \([-3, 3]^4\), or violation of \(\min_{z\neq 0} q(z) = 2\), \(|\mu_{10}| = 10\), or shells \(\{1, 10, 20, 20, 60\}\).
- **F02.** Any failure of edge-disjoint cuts, unit cut flux, \(\operatorname{div}_{D_3} E = 0\), \(Q_E = 4d\) (\(d = 1..4\)), \(Q_E = 4L\) (\(L = 6, 8, 10, 12\)), purely magnetic increment \(\Delta Q_{\mathrm{tot}} = 4L\), or the parallelogram identity on \(D_3(6)\).
- **F03.** Pointwise 4D Poisson summation relative error \(\ge 10^{-40}\) at any \(\beta \in \{0.50, 1.00, 2.00\}\).
- **F04.** On any \(L \in \{2, 4, 6\}\): \(\sum_e (\Delta x_e)^2 \neq 2L^3\), \(\max_v |(B\,\Delta x)_v| \neq 0\), nonzero spin-wave sum \(\sum_e \Delta x_e(\theta_v - \theta_u)\), \(K \neq (L/\beta)G^{-1}\), Gaussian limit \(\neq 1/4\), or failure of the strictness witness \(m_{e_0}^T G^{-1} m_{e_0} = 2/5 > 0\).
- **F05.** On the 2-edge or 3-edge cyclotomic complexes: primal/dual overlap error \(\ge 10^{-40}\), violation of strict \(Z_{\mathrm{work}}^{\mathrm{var}}(\beta) < 1/4\) at any tested \(\beta\), violation of \(Z_{\mathrm{work}}^{\mathrm{var}} < Z_{\mathrm{work}}^{\mathrm{disc}} = 1/4\) on the 2-edge complex, violation of \(Z_{\mathrm{work}}^{\mathrm{disc}} < 1/4\) on the 3-edge complex, or failure to certify the 3-edge sign change and crossover \(|\beta_* - 0.242528416| < 10^{-9}\), \(|Z(\beta_*) - 0.24920214| < 10^{-8}\), \(|Z_{\mathrm{work}}^{\mathrm{var}}(\beta_*) - Z_{\mathrm{work}}^{\mathrm{disc}}(\beta_*)| < 10^{-35}\).
- **F06.** Failure to reject any of the five deliberate negative controls:
  - `C01` (`corrupt_gram`): replacing \(G\) by \(5I_4\) breaks \(\operatorname{Tr}(z\bar{z}) = z^T G z\) at \(z = (1, 1, 0, 0)\).
  - `C02` (`zero_vortex_truncation`): truncating \(m \equiv 0\) yields zero deficit (\(Z = 1/4\)), contradicting the exact 2-edge deficit at \(\beta = 1.00\).
  - `C03` (`perturbed_edge_weight`): changing one \(\Delta x_{e_0}: 1 \to 2\) on \(D_3(4)\) produces \(\max_v |(B\,\Delta x)_v| = 1\) and nonzero spin-wave sum.
  - `C04` (`broken_divergence_string`): deleting one edge of the \(D_3(6)\) unit \(x\)-string lowers \(Q_E\) to \(20 < 24\) while triggering \(\mathrm{div\_err} = 2\) and cut flux failure.
  - `C05` (`constant_sign_3edge`): opposite signs of \(Z_{\mathrm{work}}^{\mathrm{var}} - Z_{\mathrm{work}}^{\mathrm{disc}}\) at \(\beta = 0.10\) and \(\beta = 0.50\) refute any claim of constant sign or non-crossing at finite \(\beta\).

PASS requires the universal written proof, exact passing of F01–F06 with all five negative controls rejected, matching verifier SHA-256, exit code 0, empty stderr, and byte-identical stdout in both required architecture jobs (`architecture-x86_64` and `architecture-aarch64`) against the same committed `EXPECTED.txt`. A verified mathematical counterexample yields BREAK. A pin mismatch, runtime error, or incomplete run without a counterexample is STOP.

## Field 6: action layers

Action layer: **L1** (exact algebraic and equilibrium lattice-bound theorem with finite exact audit). No cross-layer lift is proposed, `canon/` is untouched, `Q9` remains `OPEN`, and this probe changes strictly one directory (`probes/P-D3-ZWORK-VAR-BOUND-1/`).

## Execution and custody

Commit and push `PREREG.md` and `verify.py` first. Fetch and read back the pushed `pin_commit` SHA and both file SHA-256 digests before executing the formal verifier command. Run the pinned verifier from the repository root with `LC_ALL=C LANG=C PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 TZ=UTC`. Record exact stdout in `EXPECTED.txt`, neutral execution metadata in `RUN.md`, and the scientific outcome in `RESULT.md`. Two-architecture reproduction is confirmed only once both `architecture-x86_64` and `architecture-aarch64` pass on the same PR commit against the same `EXPECTED.txt`.
