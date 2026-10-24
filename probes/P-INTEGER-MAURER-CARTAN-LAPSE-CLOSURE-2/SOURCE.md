# P-INTEGER-MAURER-CARTAN-LAPSE-CLOSURE-2 — Source Provenance and Algorithmic Independence

## 1. Provenance and Upstream Chain

This probe builds directly on the merged integer-gravity sequence on `main`:
- `P-INTEGER-AUTONOMOUS-JOINT-ENERGY-1` (`#1650`, issue `#1649`): six-component autonomous K1 metric-source system with source drive $a \in \{-1, 0, 1\}$ and equilibrium energy shift $E_* = \frac{4342005}{8683757}(a/4)^2$.
- `P-INTEGER-LOCAL-NOETHER-OBSTRUCTION-1` (`#1662`, issue `#1661`): temporal locality obstruction in the field-only class and local multiplier relaxation.
- `P-INTEGER-LOCAL-AUXILIARY-NOETHER-1` (`#1664`, issue `#1663`): horizon-uniform local auxiliary completion and degree-2 skew-adjusted commuting closure.
- `P-INTEGER-SCALAR-LAPSE-RIGIDITY-1` (`#1666`, issue `#1665`): all-order scalar-lapse completion $M(s) = M_0 \exp(s K)$, Ward rigidity $M' = K M$, free-lapse stationary collapse at $a = 0$, and the degree-3 off-shell commutator witness $-\frac{1}{8} C u$.
- `P-INTEGER-FIXED-DURATION-BOUNDARY-1` (`#1668`): fixed-total-lapse stationary phase quotient, boundary/energy classification, and $T = 3, \Lambda = -3$ caustic.

## 2. Two Independent Implementations

Both `verify.py` and `breaker.py` are standalone Python 3 scripts using only the Python standard library (`fractions.Fraction`, `hashlib.sha256`, `math`, `pathlib`, `subprocess`, `sys`) and outputting pure ASCII with `\n` (LF) line endings via `sys.stdout.buffer.write`. Neither script imports or reads the other's source code.

### 2.1 Primary Verifier (`verify.py`)
1. **Carrier Construction:** Builds the $5 \times 5$ circulant Laplacian $L$ by directed graph edge incidence over jumps $1$ (`29/324`) and $2$ (`65/324`), assembles $V, C, D, K, M_0$, and computes the matrix series $R(s) = \sum_{k=0}^4 \frac{s^k}{k!} K^k$, $M(s) = M_0 R(s)$, $E(s) = B(s)^{-1}$, and $A(s) = E(s) U(s)$ by explicit $12 \times 12$ and $6 \times 6$ `Fraction` matrix power series inversion and convolution.
2. **Gauge Commutator Evaluation:** Evaluates the adjusted gauge generator $\tilde V_t^{\le m}(q, s)$ ($m \in \{1, 2, 3, 4\}$) directly on field histories $q = (q_0, \dots, q_T) \in (\mathbb{Q}^6)^{T+1}$ by summing the directional lapse derivative $\partial_t \tilde V_r(q, s) - \partial_r \tilde V_t(q, s)$ and the field-space Jacobian convolution $\sum_{j=1}^{d-1} \bigl(\tilde V_r^{(d-j)}(\tilde V_t^{(j)}(q, s), s) - \tilde V_t^{(d-j)}(\tilde V_r^{(j)}(q, s), s)\bigr)$, and compares the resulting field vector against the Maurer–Cartan curvature formula $\mathcal{F}_{t,r}(s) \nabla_q S(q, s)$.
3. **Forced Equilibrium and Cold-Start Dynamics:** Computes $x_* = V^+ f_*$ by Gauss–Jordan elimination on the zero-sum-constrained $6 \times 6$ matrix, verifies the square-completion identity for $S^{(a)}(q, s)$, and propagates the vacuum cold-start trajectory $q_{-1} = q_0 = 0$ via the $12 \times 12$ transfer matrix $M_0$.

### 2.2 Independent Breaker (`breaker.py`)
1. **Carrier Construction & Polynomial Ring Algebra:** Constructs $L$ from its explicit symmetric circulant entries, represents every $6 \times 6$ block of $U_k, B_k, E_k, A_k$ as a polynomial in the single symmetric matrix $C$ reduced modulo its minimal polynomial (or direct polynomial ring convolution in $\mathbb{Q}[C]$ evaluated on $C$), and verifies the closed-form polynomial formulas for $E_0, \dots, E_4$ and $A_0, \dots, A_4$:
   $$E_0 = I_6,\; E_1 = -C,\; E_2 = \frac{1}{2}(I_6 + C^2),\; E_3 = -\frac{1}{6}(2 C + C^3),\; E_4 = \frac{1}{24}(I_6 + 6 C^2 + C^4),$$
   $$A_0 = C,\; A_1 = -I_6,\; A_2 = \frac{1}{2} C,\; A_3 = -\frac{1}{6}(I_6 + 2 C^2),\; A_4 = \frac{1}{24}(5 C + C^3).$$
2. **Operator-Matrix Maurer–Cartan Assembly:** Assembles the global $6(T-1) \times 6(T-1)$ interior block matrices $H_k(s)$, $L_t^{(k)}(s)$, $\Omega_{t,r}^{(k)}(s)$, and $A_t^{(m)}(s)$, computes the commutator matrix $\partial_t \tilde L_r - \partial_r \tilde L_t + [\tilde L_r, \tilde L_t]$ directly in the matrix algebra $\mathbb{Q}^{6(T-1) \times 6(T-1)}$, and verifies that it equals $\mathcal{F}_{t,r}(s) H(s)$ and vanishes through degree 4.
3. **Forced Equilibrium and Second-Order Recurrence:** Solves $V x_* = f_*$ via $LDL^\mathsf{T}$ factorization on the reduced 5D basis of $\mathbf{1}_5^\perp \oplus \mathbb{Q}$, verifies $D x_* = f_* - \frac{1}{4} V f_*$ and $E_{\mathrm{cold}} = E_* - \frac{1}{8}\|f_*\|^2$, and generates the cold-start trajectory $q_{-1} = q_0 = 0$ directly from the inhomogeneous second-order recurrence $q_{n+1} = 2 C q_n - q_{n-1} + f_*$.

## 3. Deterministic Fixtures

Both scripts use the identical deterministic rational fixture
$$\operatorname{fixture}(\mathrm{seed}, n, r) = \frac{((\mathrm{seed} + 2)(n + 1)(r + 3) + (n - r)^2) \bmod 17 - 8}{\mathrm{seed} + 2}$$
for off-shell field histories, bond lapses, and Dirichlet gauge parameters.
