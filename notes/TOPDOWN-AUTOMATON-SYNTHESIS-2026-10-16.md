# Top-Down Integer Automaton Construction and Its Convergence with TWIST-J (Steps 1–7)

**NON-CANONICAL / structural synthesis note.**
Date: 2026-10-16
Author: A. M. Thorn `<thorn@twistj.com>`

## 0. Scope and Epistemic Guardrail

This note records a seven-step **top-down** ("odshora") construction of a
synchronous deterministic integer and finite-state automaton on a directed
graph and cell complex, starting strictly from:

1. directed graph / cell-complex incidence with entries in $\{-1, 0, +1\}$,
2. integer ($\mathbb{Z}$) and finite-field ($\mathbb{F}_p$) vertex, edge, and
   face states, and
3. strictly local synchronous transitions with bounded dependency radius,
   eliminating all reliance on continuous differential calculus.

At each step we identify the exact mathematical point where the top-down
automaton constraints meet the registered theorems and definitions of
**TWIST-J** (`canon/CANON.md`). In strict compliance with `POLICY.md` and
`DEF-FIELD-WORK-RECORD-CHAIN`, this note separates:
- **exact algebraic/topological necessities** (where minimal graph or
  spectral constraints force $p = 5$, $\mathbb{Z}[\zeta_5]$, $\Delta = 5$,
  $\operatorname{SL}_2(\mathbb{F}_{25})$, and mod-$5$ homology obstructions),
  and
- **selected architectural or dictionary choices** (such as the specific
  three-register endpoints $R, AM$, chronology `G; A; B; F`, and physical
  observable dictionaries `[D]`).

---

## Step 1: Minimal Irreducible Local Cycle Automaton ($p = 5$, $J$, and $F = JG$)

### 1.1 Top-down requirement
Seek the smallest directed cycle $C_p$ ($p$ prime) carrying an integer state
modulo the uniform background vector $(1,1,\dots,1)^T$ (so the state lattice
is $\mathbb{Z}^{p-1} \cong \mathbb{Z}[\zeta_p]$) such that the elementary
two-branch local shift rule ("stay at node $i$ or step along edge $i \to i+d$")
$$J = I + S^d \qquad (1 \le d < p)$$
is invertible up to norm, aperiodic (no root of unity), and generates a
nontrivial real quadratic energy scale $\mathbb{Q}(\sqrt{p})$:
- For $p = 2$: $\mathbb{Z}[\zeta_2] = \mathbb{Z}$ ($1 + \zeta_2 = 0$, singular).
- For $p = 3$: $\mathbb{Z}[\zeta_3]$ is Imaginary Quadratic; $1 + \zeta_3 = -\zeta_3^2$
  is a root of unity of finite order $6$ ($|1 + \zeta_3| = 1$, no real
  subring $\neq \mathbb{Z}$).
- For **$p = 5$**: $\mathbb{Z}[\zeta_5] \cong \mathbb{Z}^4$ has maximal real
  subring $\mathbb{Z}[\varphi]$ ($\varphi = \frac{1+\sqrt{5}}{2}$), and
  $$J = 1 + \zeta_5^2 \qquad (\text{claim } \texttt{J-STEP})$$
  has minimal polynomial $(X-1)^4 + (X-1)^3 + (X-1)^2 + (X-1) + 1 = 0$,
  norm $N_{\mathbb{Q}(\zeta_5)/\mathbb{Q}}(J) = 1$ (so $J \in \mathbb{Z}[\zeta_5]^\times$
  is a bijective unimodular integer update on $\mathbb{Z}^4$), and infinite
  multiplicative order (`J-TURING-COMPLETE`).

### 1.2 Pairing into the 4-periodic conservative carrier $F = JG$
Pairing $J$ with the companion matrix $G$ of `INTEGER-F-JG-INVARIANTS` in
$\operatorname{GL}_4(\mathbb{Z})$ gives $F = JG$ with:
$$F = \begin{pmatrix} 1 & 1 & -1 & 0 \\ 0 & 0 & -1 & 0 \\ 0 & 1 & 0 & 0 \\ 1 & 1 & 0 & -1 \end{pmatrix}, \qquad U_{\text{coord}} = \begin{pmatrix} 0 & 1 & 0 & 0 \\ 0 & -1 & 0 & 1 \\ 0 & 0 & -1 & 0 \\ -1 & 0 & 1 & 0 \end{pmatrix}, \qquad \det U_{\text{coord}} = 1.$$
In the unimodular coordinates $x = U_{\text{coord}}(a,b,c,d)^T = (b, d-b, -c, c-a)^T$,
the step $F$ is the **exact 4-cycle permutation** $S_4 = \operatorname{circ}(0,0,0,1)$
($F^4 = I_4$), which conserves:
- the linear charge $\chi(x) = \sum_{j=0}^3 x_j = d - a$, and
- every circulant quadratic form $Q(x) = x^T K x$ with
  $K = \operatorname{circ}(A, B, C, B)$ (in particular $(A,B,C) = (6,2,-1)$
  with eigenvalues $\{9, 7, 7, 1\}$, so $Q(x) \ge \|x\|^2$).

---

## Step 2: Causal Graph Localization of the Native Kernel $U$ on $\mathbb{F}_5^6$

### 2.1 Top-down requirement
On a 6-register node state $x = (p_1, p_4, p_1', p_4', q, r) \in \mathbb{F}_5^6$,
a general composition of five involutive updates $U = e \circ d \circ c \circ b \circ a$
driven by the Thue-Morse schedule $\theta_t \in \{0,1\}$ (`U-INVOLUTION`,
`U-THUE-MORSE`) could a priori create an all-to-all dependency graph
(in-degree $6$). For a local graph automaton, we ask whether there exists a
state coordinate with in-degree $1$.

### 2.2 Autonomous phase clock $z(x)$ and the 3-layer DAG
Define the total mod-5 sum $z(x) = \sum_{k=1}^6 x_k \bmod 5$. Under the five
canonical involutions of `reproduce/kernel-Execution/verify.py`:
$$z(a(x)) = z(x), \quad z(b(x)) = -z(x), \quad z(c(x)) = z(x), \quad z(d(x)) = 2 - z(x), \quad z(e(x)) = 3 - z(x) \pmod 5.$$
Hence over a full tick $U_{\theta_t}$:
$$z(x(t+1)) \equiv \begin{cases} 4 - z(x(t)) \pmod 5 & \text{if } \theta_t = 0, \\ 1 - z(x(t)) \pmod 5 & \text{if } \theta_t = 1. \end{cases}$$
This decomposes $U$ into a strictly feed-forward **3-layer directed acyclic
graph (DAG)** of strongly connected components:
$$\theta_t \longrightarrow z \longrightarrow (q, r) \longrightarrow (p_1, p_4, p_1', p_4'),$$
where the clock $z$ has internal in-degree $1$, the control pair $(q, r)$ has
in-degree $3$ ($z, q, r$), and the 4D piston $p = (p_1, p_4, p_1', p_4')$ is
driven by affine shifts parameterized solely by $(z, q, r)$.

---

## Step 3: Bridge Between Native Kernel $U$ and the Conservative Spatial Chain (`G; A; B; F`)

As proved in detail in `notes/U-FIELD-SHELL-GATE-BRIDGE-2026-10-16.md`:
1. In the conservative spatial chain (`DEF-FIELD-WORK-RECORD-CHAIN`,
   `FIELD-CONSERVATIVE-CHAIN-LAW`), the funded reaction gate $G$ accepts a
   local wave vector $y = (a, b, c, d) \in \mathbb{Z}^4$ for shell down-conversion
   $H(Lx) = 5H(x)$ if and only if $y \in L\mathbb{Z}^4$, which is decided
   purely modulo $5$ by the 25-state subspace:
   $$\mathcal{G}_L = \left\{ (a, b, c, d) \in \mathbb{F}_5^4 \;:\; a + 2b \equiv 0 \pmod 5,\; c + 2d \equiv 0 \pmod 5 \right\}.$$
2. Passing from the native piston $p = (p_1, p_4, p_1', p_4')$ to the
   $a$-swapped frame $\tilde{p} = a(p) = (p_4, p_1, p_4', p_1')$:
   - $\tilde{s} = a(\text{S\_VEC}) = (1, 2, 1, 2) \in \mathcal{G}_L$,
   - $\tilde{c}_d = a(\text{C\_D}[:4]) = (1, 2, 4, 3) \in \mathcal{G}_L$ with
     integer lift $(1, 2, -1, -2)^T = L(0, 0, -1, 0)^T \in L\mathbb{Z}^4$,
   - generators $b, d, e$ and $c|_{r=0}$ preserve $\mathcal{G}_L$ identically,
     while $c$ shifts the gate residuals $(g_1, g_2) = (u_0+2u_1, u_2+2u_3)$
     by $(r, -r) \pmod 5$.
3. Consequently, the all-zero integer trajectory $U^t(0,0)$ remains inside
   $L\mathbb{Z}^4$ in the $a$-frame for all $t \ge 0$, and at the first
   synchronization tick $t = 3$ produces the exact unit-energy wave seed:
   $$\tilde{y}(3) = (0, 0, -2, 1)^T = L(0, -1, -1, 2)^T, \qquad H(0, -1, -1, 2) = 1, \quad H(\tilde{y}(3)) = 5.$$

---

## Step 4: Emergence of Spatial Shift (Translation) Without Continuous Calculus

In a discrete graph automaton without derivatives, spatial motion arises from
**composing non-commuting local involutions**:
1. **Dihedral translation from reflection pairs (`U-HEX-PROJECTION`, `U-CUBIC-SUM`):**
   Lifting the involutions $a, b, c, d, e$ to $\mathbb{Z}^6$:
   - $(e \circ d)(x) = x + (0, 0, 0, 0, 1, 0)$ (pure unit translation in $q$),
   - $(c \circ b)(x) = x + (2, 1-r, 2, 1+r, 1, 0)$,
   - fired commutators $t_1 = [d, e] = (0, 0, 0, 0, -2, 0)$ and
     $t_2 = [b, d] = (-5, -5, -5, -5, -2, -2)$ span a 2D lattice whose
     3-generator projection $e_1 = t_1, e_2 = t_2, e_3 = -(t_1 + t_2)$
     produces hexagonal shells of size $H_R = 3R(R+1) + 1 = (R+1)^3 - R^3$ and
     cumulative cubic ball volume $\sum_{r=0}^R H_r = (R+1)^3$.
2. **Spatial propagation on a chain (`INTEGER-SEPARATED-FACTOR-CERTIFICATE`):**
   Alternating non-commuting local port swaps $A$ (internal cell swap) and
   $B$ (inter-cell channel swap) in the schedule `G; A; B; F` produces a
   ballistic shift of $1$ cell per macrostep ($x \mapsto x + 1$) with
   dependency radius at most $2$ stored-block edges.
3. **Charged transport and bridge flux memory (`FIELD-GAUSS-CONTACT-MEMORY`, `FIELD-CHARGED-SEPARATION-BOUND`):**
   To preserve Gauss's law $DE = \rho$ locally when a charge $+q$ hops across
   an oriented bridge edge $e = (u \to v)$, the local transition must update
   the edge electric flux by $E_e' = E_e - q$. Separating $+q$ and $-q$ across
   $L$ bridge edges therefore leaves a flux string of energy at least
   $$H_f \ge q^2 L.$$

---

## Step 5: Multidimensional Cell Complex, Defeating the Two-Triangle Zero Mode, and the Maxwell Chain Complex

### 5.1 Spectral wall $\|C\| < 2$ and why 2D cell pasting jumps from $p = 3$ to $p = 5$
On any 2-complex with vertex-edge divergence $D$ and edge-face incidence $C$
($DC = 0$), the symplectic shear
$$E' = E + CM, \qquad M' = M - C^T E'$$
preserves $DE$ and the quadratic form (`FIELD-SHEAR-ENERGY-BOUNDARY`):
$$H_f(E, M) = \|E\|^2 + \|M\|^2 + E^T C M, \qquad 4H_f(E, M) = \|2E + CM\|^2 + M^T(4I - C^T C)M.$$
Positive definiteness holds iff $\lambda_{\max}(C^T C) < 4$:
- **One triangle (length 3, `FIELD-EISENSTEIN-RESONANCE`):** $c^T c = 3 \implies 4 - c^T c = 1 > 0$.
  On the cycle sector $E = zc$, the step is $T(z, m) = (z+m, -3z-2m)$ with
  period **$T^3 = I$** ($\mathbb{Z}[\zeta_3]$, norm factor $p = 3$).
- **Two triangles sharing an edge ($3 + 3$):**
  $$C^T C = \begin{pmatrix} 3 & 1 \\ 1 & 3 \end{pmatrix}, \qquad 4I - C^T C = \begin{pmatrix} 1 & -1 \\ -1 & 1 \end{pmatrix}, \qquad \det(4I - C^T C) = 0.$$
  Because $\lambda_{\max}(C^T C) = 4$, the nonzero divergence-free integer state
  $M = (2, 2),\, E = (-2, -1, -1, -1, -1)$ has **$DE = 0$ and $H_f = 0$** (a zero-energy mode).
- **Digon + triangle sharing an edge ($2 + 3$, `DEF-FIELD-WORK-RECORD-CHAIN`):**
  Pairing a 2-edge face $f_0 = e_0 - e_1$ with a 3-edge face $f_1 = -e_0 + e_2 + e_3$ gives:
  $$C^T C = \begin{pmatrix} 2 & -1 \\ -1 & 3 \end{pmatrix}, \qquad 4I - C^T C = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}, \qquad \det(4I - C^T C) = 1 > 0.$$
  Here $4H_{\text{raw}}(E,M) = \|2E + CM\|^2 + M_0^2 + (M_0 + M_1)^2$ is strictly
  positive definite, the characteristic polynomial of $C^T C$ is
  $\lambda^2 - 5\lambda + 5 = 0$ with **discriminant $\Delta = 5$** (eigenvalues
  $\frac{5 \pm \sqrt{5}}{2} < 4$), and the induced wave operator $A_f$ on
  $P\mathbb{Z}^4$ satisfies the 5th cyclotomic equation:
  $$\Phi_5(A_f) = I + A_f + A_f^2 + A_f^3 + A_f^4 = 0 \qquad (A_f^5 = I,\; L^* L = 5I_4).$$
  Thus avoiding the two-triangle zero mode automatically transitions the cell
  dynamics from $p = 3$ ($\mathbb{Z}[\zeta_3]$) to **$p = 5$ ($\mathbb{Z}[\zeta_5]$)**.

### 5.2 Escaping the 1D bridge string on the closed $2 \times 2 \times 2$ torus (`MAXWELL-GAUSS-CHAIN`)
On the closed 3D torus $(\mathbb{Z}/2\mathbb{Z})^3$ ($V = 8, E = 24$), the
boundary matrix $\partial_1: \mathbb{Z}^{24} \to \mathbb{Z}^8$ has all $7$
Smith elementary divisors equal to $1$ (no torsion) and cycle space dimension
$E - V + 1 = 17$. A separated dipole $\rho = \delta_{(1,1,0)} - \delta_{(0,0,0)}$
is solved by a 2-edge path with $\|E\|^2 = 2$, and the integrated Gauss law
holds identically on all $2^8 = 256$ vertex regions.

### 5.3 The 3+1D tesseract, $2^4$ torus, and mod-$5$ homology obstructions (`MAXWELL-BIANCHI`, `MAXWELL-AMPERE-CHAIN`, `MAXWELL-OBSTRUCTION-P`)
- On the 3+1D tesseract $(V, E, F, C) = (16, 32, 24, 8)$, gauge invariance
  $F[A + d\Lambda] = F[A]$ on all 24 faces and Bianchi's identity
  $dF = d(dA) = 0$ on all 8 cubes hold identically in the 32 edge and 16
  vertex symbols (`MAXWELL-BIANCHI`).
- On the closed 4D torus $(\mathbb{Z}/2\mathbb{Z})^4$ $(V_4, E_4, F_4) = (16, 64, 96)$,
  continuity $\partial_1 \partial_2 = 0$ holds identically in all 96 face
  symbols, all $45$ Smith elementary divisors of $\partial_2$ over $\mathbb{Z}$
  equal $1$, $\operatorname{rank}(\partial_1) = 15$, and the first homology
  group is $H_1(\mathbb{T}^4; \mathbb{Z}) \cong \mathbb{Z}^{49 - 45} = \mathbb{Z}^4$,
  detected by four explicit winding cocycles $f_\mu(J)$ ($\mu = 0,1,2,3$).
- Reduced to a finite automaton over $\mathbb{F}_5$ (`MAXWELL-OBSTRUCTION-P`):
  - Gauss $\partial_1 E \equiv \rho \pmod 5$ is solvable $\Longleftrightarrow \sum_v \rho_v \equiv 0 \pmod 5$.
  - Ampère $\partial_2 G \equiv J \pmod 5$ has $\operatorname{rank}_{\mathbb{F}_5}(\partial_2) = 45 = 64 - (15 + 4)$
    and is solvable $\Longleftrightarrow \partial_1 J \equiv 0 \pmod 5$ and
    $f_\mu(J) \equiv 0 \pmod 5$ for all $\mu \in \{0,1,2,3\}$. A single
    winding current is obstructed over $\mathbb{F}_5$, whereas a bundle of $5$
    parallel windings $5J_w$ becomes unknotted and solvable modulo $5$.

---

## Step 6: Face Readout, Spinor Half-Step in $\operatorname{SL}_2(\mathbb{F}_{25})$, and the $A_8$ Born Staircase

### 6.1 Verb readout Gram matrix and Born face weights (`SUBSTRATE-KNIT`, `BORN-FACE-WEIGHTS`)
On the 5-cycle $\mathbb{Z}/5\mathbb{Z}$, the local step verb $C_+ = I_5 + S$
and its conjugate readout $C_- = C_+^T = I_5 + S^{-1}$ satisfy:
$$C_+ C_+^T = \operatorname{circ}(2, 1, 0, 0, 1).$$
In the Fourier basis of the finite Weyl pair $Z X Z^{-1} X^{-1} = \zeta_5 I_5$,
its eigenvalues in $\mathbb{Z}[\zeta_5]$ are the Born face weights:
$$w(k) = |1 + \zeta_5^k|^2 \implies w(0) = 4,\quad 2w(1) = 2w(4) = 3 + \sqrt{5},\quad 2w(2) = 2w(3) = 3 - \sqrt{5},$$
where $\sqrt{5} = 1 + 2(\zeta_5 + \zeta_5^4)$ ($\tau^2 = 5$). The spectral mass
is $\sum_{k=0}^4 w(k) = 10$ against coefficient mass $1^2 + 1^2 = 2$
(Plancherel ratio $10 / 2 = 5 = p$), Galois $\sigma_2$ swaps $w(1) \leftrightarrow w(2)$
because $\left(\frac{2}{5}\right) = -1$, and the unnormalized tilt is $2\sqrt{5}$.

### 6.2 Spinor bisector of the quarter-turn in $\operatorname{SL}_2(\mathbb{F}_{25})$ (`SPIN-BISECTOR`)
The 4-periodic carrier quarter-turn $B = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$
($B^2 = -I_2, B^4 = I_2$) has integer bisector $S = I_2 - B$ satisfying
$\det(I_2 - B) = 2$ and $(I_2 - B)^2 = -2B$. Because $\left(\frac{2}{5}\right) = -1$,
normalizing $I_2 - B$ to determinant $1$ forces the quadratic field extension
$\mathbb{F}_{25} = \mathbb{F}_5[x]/(x^2 + 2)$, where $s = 2x$ satisfies
$s^2 \equiv 2 \pmod 5$ and $s^{-1} = 3s$. Then
$$R = s^{-1}(I_2 - B) \in \operatorname{SL}_2(\mathbb{F}_{25}) \quad \text{satisfies} \quad \det R = 1,\; R^2 = -B,\; R^4 = -I_2,\; R^8 = I_2,$$
realizing the exact finite shadow of the spinor double cover.

### 6.3 Residual algebra $A_8 = \mathbb{Z}[\zeta_8]/5$ and order staircase (`BORN-QUARTET`)
In $A_8 = \mathbb{F}_5[X]/(X^4 + 1)$ with involution $X^* = X^7 = -X^3$ and
Born norm $N_B(a) = a a^*$:
- $X^4 + 1 \equiv (X^2 + 2)(X^2 + 3) \pmod 5$ splits $A_8 \cong \mathbb{F}_{25} \times \mathbb{F}_{25}$
  into two factors swapped by $*$ (`BORN-RESIDUAL-SPLIT`).
- The Born unit group $U_B(A_8) = \{u \in A_8 : N_B(u) = 1\}$ is cyclic of
  order $24$, and every unit obeys the half-angle identity
  $(1 + u)^2 = u N_B(1 + u)$ (`BORN-HALF-ANGLE`).
- The bisector norm $N_B(1 + u)$ has a $*$-fixed square root iff $u$ lies in
  the 12-element square subgroup of $U_B(A_8)$, yielding $11$ invertible unit
  bisectors ($H^2 = u, N_B(H) = 1$) and $1$ vanishing antipode $u = -1$.
- Because $\zeta_8 = X$ is ungated (not a square), each phase halving
  $4 \to 8 \to 16$ requires an irreducible quadratic extension step
  $\mathbb{F}_5 \to \mathbb{F}_{25} \to \mathbb{F}_{625}$ (`BORN-ORDER-STAIRCASE`).

---

## Step 7: Dimensionless Coupling Seeds, Weinberg Tree $3/13$, and Mass Ladder Invariants

From the integer ring $\mathbb{Z}[\zeta_5]$ ($p = 5$, rank $p - 1 = 4$) established in Step 1:

1. **Galois-trace Gram matrix and $\alpha_* = 1/5$ (`ALPHA-SEED`, `MEASURE-SPATIAL-ONLY`):**
   On $\mathbb{Z}^4$, the Galois-trace Gram matrix $G = 5I_4 - \mathbf{1}\mathbf{1}^T$
   has eigenvector $\mathbf{1} = (1,1,1,1)^T$ with eigenvalue $1$ and a 3D
   orthogonal trace-kernel complement with eigenvalue $5$ ($\det G = 5^3 = 125$).
   Normalized by $p = 5$, the spectrum is $\{1/5, 1, 1, 1\}$, yielding the
   dimensionless trace seed $\alpha_* = 1/p = 1/5$ and spatial weight
   $d/(d+1) = 3/4$ (ratio $15 : 4$, $w = -14/15$).
2. **Trace of the axiom $\operatorname{Tr}(J) = 3$, trace kernel, and Weinberg tree $3/13$ (`WEINBERG-TREE`, `HYPERCHARGE-LAW`):**
   On the power basis $\{1, \zeta_5, \zeta_5^2, \zeta_5^3\}$ of $\mathbb{Z}[\zeta_5]$,
   $\operatorname{Tr}(1) = 4$ and $\operatorname{Tr}(\zeta_5^m) = -1$ ($m=1..4$), so:
   $$d = \operatorname{deg}_f = \operatorname{Tr}(J) = \operatorname{Tr}(1 + \zeta_5^2) = 4 - 1 = 3.$$
   The trace functional $\operatorname{Tr}(v) = 4v_0 - v_1 - v_2 - v_3$ has a
   3D kernel over $\mathbb{Q}$ and $5^3 = 125$ points over $\mathbb{F}_5$,
   giving $B_{\text{quark}} = 1/\dim\ker(\operatorname{Tr}) = 1/3$ and all
   seven Standard Model hypercharges via $Y_F = (B - L) + 2T_3^R$. With
   $V = d(d+1) = 12$, the tree-level Weinberg angle is:
   $$\sin^2\theta_W\big|_{\text{tree}} = \frac{\operatorname{deg}_f}{V + 1} = \frac{3}{13},$$
   and with $\varphi^{-4} = 5 - 3\varphi = \frac{7 - 3\sqrt{5}}{2} > 0$, the
   committed form is $\sin^2\theta_W = \frac{3}{13} + \frac{1}{32\pi^2 \varphi^4}$ (`WEINBERG-FORM`).
3. **Shared lepton coefficient $C_{\mu\tau} = 89/5$, exchange identity, and bridges (`MU-TAU-COEFFICIENT`, `MU-EXCHANGE-IDENTITY`, `BRIDGE-DEFECT`, `PARITY-LAW`):**
   Combining the spatial matter number $18 = \frac{1}{2} V d = \frac{1}{2}(12)(3)$
   (which also equals the reactant rest energy $Q(R) = 18$ in Step 3) with the
   trace seed $1/p = 1/5$ gives:
   $$C_{\mu\tau} = 18 - \frac{1}{5} = \frac{89}{5}, \qquad 240\, C_{\mu\tau} = 4272 \in \mathbb{Z}, \qquad \delta\mu_\tau + 240\,\delta\mu_\mu = 0.$$
   In $\mathbb{Q}(\sqrt{5})$, the exact bridges $\xi = 5\varphi^{-2}$ and
   $\mathcal{Q} = 2\pi\varphi^{-2}$ satisfy $\xi\varphi^2 = 5 = p$,
   $\mathcal{Q}\varphi^2 = 2\pi$, and $\mathcal{Q}/\xi = \frac{2\pi}{5} = \arg J$,
   while $6\varphi^2 = 9 + 3\sqrt{5}$ is a root of the irreducible polynomial
   $x^2 - 18x + 36 = 0$ ($\Delta = 180$), certifying $\delta = 6\varphi^2 - 5\pi \neq 0$
   by Lindemann-Weierstrass. Under the formal grading involution $\iota_\pi(\pi) = -\pi$,
   the 13 even observables, 3 odd carriers at $\pi^1, \pi^3, \pi^5$, and the
   mixed neutron composite ($\{0, 5\}$) partition the observable register (`PARITY-LAW`).
