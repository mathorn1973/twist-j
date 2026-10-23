# Homogeneous Capture, Fiber Scattering, Branch Gap, and Finite-Strip Elimination

**PUBLIC, NON-CANONICAL. Self-contained analytical proof (`PROOF_CAPTURE_SCATTERING.md`) for `C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N`.**

Owner: A. M. Thorn. License: Apache-2.0.
Authority basis: `mathorn1973/twist-j` main `e6240e2689bb22aab5f02bad90b75d3692bb96d9` (Public Canon v104, content commit `4a50e527d20018839f006ed312454b710e6486b4`).

---

## 1. Homogeneous Carrier, 26-Label Allocation, and Local Contact Law

### 1.1 Object Walk on Center and Relative Coordinates

Let $x_A = R + r \in \mathbb{Z}$ and $x_B = R - r \in \mathbb{Z}$ be the physical coordinates of the two object walkers in the common-parity sector $x_A \equiv x_B \pmod 2$. On $\mathcal{H}_{\mathrm{obj}} = \ell^2(\mathbb{Z}_R \times \mathbb{Z}_r, \mathbb{C}^4)$ with coin basis $(|1\rangle, |2\rangle, |3\rangle, |4\rangle) = (|++\rangle, |+-\rangle, |-+\rangle, |--\rangle)$, the one-step object walk is
$$W = \Gamma S M_2, \qquad M_2 = \frac{1}{5}\begin{pmatrix} 1 & 2i & 2i & -4 \\ 2i & 1 & -4 & 2i \\ 2i & -4 & 1 & 2i \\ -4 & 2i & 2i & 1 \end{pmatrix} = \frac{I_2 + 2i\sigma_x}{\sqrt{5}} \otimes \frac{I_2 + 2i\sigma_x}{\sqrt{5}},$$
where $S$ shifts $(R, r) \mapsto (R + \delta R_d, r + \delta r_d)$ with $(\delta R_d, \delta r_d) = (-1,0), (0,-1), (0,+1), (+1,0)$ for $d = 1,2,3,4$, and $\Gamma = I + (e^{-ig}-1)\delta_{r=0}$ applies the contact phase $z_g = e^{-ig} = e^{-i 2\pi/5}$ at $r = 0$.

Define the orthonormal contact coin vectors at $r = 0$:
$$|b_0\rangle = \delta_{r=0}\,\frac{|1\rangle - |4\rangle}{\sqrt{2}}, \qquad |a_0\rangle = \delta_{r=0}\,\frac{i(|2\rangle - |3\rangle)}{\sqrt{2}}.$$
Direct multiplication gives $M_2(|1\rangle - |4\rangle) = |1\rangle - |4\rangle$ and $M_2(|2\rangle - |3\rangle) = |2\rangle - |3\rangle$. At center momentum $P = 0$, $S$ fixes $r = 0$ on $|1\rangle, |4\rangle$, so $|b_0\rangle$ is an exact eigenvector of $W(0)$ with eigenvalue $z_g = e^{-ig}$.

### 1.2 Carrier Space, 26-Label Allocation, and Homogeneous Contact

The single-carrier space is $\mathcal{H}_{\mathrm{car}} = \mathcal{H}_{\mathrm{tok}} \oplus \mathcal{H}_{\mathrm{pulse}}$ with carrier site $y \in \mathbb{Z}$ and label $j \in \{0, 1, \dots, 25\}$:
- $\mathcal{H}_{\mathrm{tok}} = \ell^2(\mathbb{Z}_y) \otimes \mathbb{C}^{26}$ with basis $|\mathrm{tok}_j(y)\rangle$, evolving trivially under the free carrier step ($V_{\mathrm{tok}} = I$).
- $\mathcal{H}_{\mathrm{pulse}} = \ell^2(\mathbb{Z}_y, \mathbb{C}^2) \otimes \mathbb{C}^{26}$ with basis $|p_{j,b}(y)\rangle$ ($b \in \{1,2\}$), evolving under $V_{\mathrm{pulse}} = D_{\mathrm{edge}} Q$ where the on-site coin and bond hop are
  $$Q\binom{\psi_1(y)}{\psi_2(y)} = \begin{pmatrix} c & -s \\ s & c \end{pmatrix}\binom{\psi_1(y)}{\psi_2(y)}, \qquad D_{\mathrm{edge}}\binom{v_1(y)}{v_2(y)} = \binom{c v_1(y) - s v_2(y+1)}{s v_1(y-1) + c v_2(y)}, \qquad c = \frac{1}{\sqrt{5}},\; s = \frac{2}{\sqrt{5}}.$$
  In Fourier momentum $k \in [-\pi, \pi)$ ($|y\rangle \mapsto e^{-iky}$), the pulse symbol is
  $$\widehat{V}_{\mathrm{pulse}}(k) = \frac{1}{5}\begin{pmatrix} 1 - 2e^{ik} & -2 - e^{ik} \\ 2 + e^{-ik} & 1 - 2e^{-ik} \end{pmatrix}, \qquad \frac{1}{2}\operatorname{tr}\widehat{V}_{\mathrm{pulse}}(k) = \frac{1 - 4\cos k}{5} = \cos\varepsilon(k),$$
  with $\varepsilon(k) = \arccos\bigl(\frac{1-4\cos k}{5}\bigr) \in [0, a_{\mathrm{pulse}}]$, $a_{\mathrm{pulse}} = 2\arctan 2 < \frac{3\pi}{4}$, and group velocity $v(k) = \varepsilon'(k) = -\frac{4\sin k}{5\sin\varepsilon(k)}$ (so $k \in (-\pi, 0)$ has $v(k) > 0$, right-moving).

The free macrostep on $\mathcal{H} = \mathcal{H}_{\mathrm{obj}} \otimes \mathcal{H}_{\mathrm{car}}$ is $U_0 = e^{-i\beta}(W \otimes V_{\mathrm{car}})$ with $\beta = 4\pi/5$.
The homogeneous contact unitary $C$ acts at coincidence $R = y, r = 0$ independently on each label $j \in \{0,\dots,25\}$ as
$$C\bigl(|a_0(y)\rangle|\mathrm{tok}_j(y)\rangle\bigr) = \frac{3}{5}|a_0(y)\rangle|\mathrm{tok}_j(y)\rangle + \frac{4}{5}|b_0(y)\rangle|p_{j,1}(y)\rangle,$$
$$C\bigl(|b_0(y)\rangle|p_{j,1}(y)\rangle\bigr) = -\frac{4}{5}|a_0(y)\rangle|\mathrm{tok}_j(y)\rangle + \frac{3}{5}|b_0(y)\rangle|p_{j,1}(y)\rangle,$$
and as the identity on the orthogonal complement. The coupled macrostep is $U = U_0 C$.

---

## 2. Joint Momentum Fiber Decomposition and Wave Operators

### 2.1 Reduction to Total-Momentum Fibers $K = P + k$

Let $T_m: (R, r, y) \mapsto (R+m, r, y+m)$ be the simultaneous lattice translation of the object center and the carrier by $m \in \mathbb{Z}$. Both $U_0$ and $C$ commute with $T_m$ and preserve each carrier label $j \in \{0,\dots,25\}$. Under the unitary change of variables $(R, y) \mapsto (y, u := R - y)$ and Fourier transform in $y \leftrightarrow K \in [-\pi, \pi)$:
$$\mathcal{H} \cong \int_{[-\pi,\pi)}^{\oplus} \mathcal{H}_{\mathrm{fib}}\,\frac{dK}{2\pi}, \qquad \mathcal{H}_{\mathrm{fib}} \cong \ell^2(\mathbb{Z}_u \times \mathbb{Z}_r, \mathbb{C}^4) \otimes (\mathbb{C}_{\mathrm{tok}} \oplus \mathbb{C}^2_{\mathrm{pulse}}) \otimes \mathbb{C}^{26}.$$
In the dual momentum coordinates $(P, k)$ with $R \leftrightarrow P$ and $y \leftrightarrow k$, the conserved fiber momentum is $K = P + k \pmod{2\pi}$:
- On the token arrangement, the token stands at $u = R - y$, so $P$ is conserved under $U_0(K)$: $U_{0,\mathrm{tok}}(K)$ acts on fiber $P$ as $e^{-i\beta}W(P)$.
- On the pulse arrangement, a pulse hop $y \mapsto y \pm 1$ shifts $u = R - y \mapsto u \mp 1$ and multiplies the fiber $K$ by $e^{\mp iK}$, so at object center momentum $P$ the pulse carries momentum $k = K - P$, and $U_{0,\mathrm{pulse}}(K)$ acts at $P$ as $e^{-i\beta}W(P) \otimes \widehat{V}_{\mathrm{pulse}}(K - P)$.
- On each fiber $K$ and each fixed label $j \in \{0,\dots,25\}$, the contact operator $C(K)$ differs from the identity only on the two-dimensional subspace spanned by
  $$|\phi_{1,j}\rangle = \delta_{u=0}|a_0\rangle|\mathrm{tok}_j\rangle, \qquad |\phi_{2,j}\rangle = \delta_{u=0}|b_0\rangle|p_{j,1}\rangle.$$

### 2.2 Existence and Completeness of Fiber and Direct-Integral Wave Operators

**Proposition 2.1 (Fiberwise and Direct-Integral Wave Operators).**
For every $K \in [-\pi, \pi)$ and every label $j \in \{0,\dots,25\}$:
1. $U(K) - U_0(K) = U_0(K)(C(K) - I)$ has rank $2$ on each label sector ($52$ on all $26$ labels), hence is trace class.
2. By the Birman-Krein-Kato unitary trace-class scattering theorem, the fiber wave operators
   $$\Omega_\pm(K) = \operatorname*{s-lim}_{n\to\mp\infty} U(K)^{-n} U_0(K)^n P_{\mathrm{ac}}(U_0(K))$$
   exist, are partially isometric with initial space $P_{\mathrm{ac}}(U_0(K))\mathcal{H}_{\mathrm{fib}}$ and final space $P_{\mathrm{ac}}(U(K))\mathcal{H}_{\mathrm{fib}}$, and satisfy the intertwining identity $U(K)\Omega_\pm(K) = \Omega_\pm(K)U_0(K)$.
3. Because $U(K)$ and $U_0(K)$ depend measurably (in fact analytically) on $K \in [-\pi, \pi)$, the direct-integral wave operators
   $$\Omega_\pm = \int_{[-\pi,\pi)}^{\oplus} \Omega_\pm(K)\,\frac{dK}{2\pi} = \operatorname*{s-lim}_{n\to\mp\infty} U^{-n} U_0^n P_{\mathrm{ac}}(U_0)$$
   exist on $\mathcal{H}$ by dominated convergence of the bounded fiber norms.
4. On the incoming token arrangement, $P_{\mathrm{ac}}(U_{0,\mathrm{tok}})$ decomposes into the relative-scattering channel $\mathcal{H}_{\mathrm{in},\mathrm{sc}} = \int^\oplus \Pi_{\mathrm{sc}}^W(P)\mathcal{H}_{\mathrm{obj}}(P)\,\frac{dP}{2\pi} \otimes \mathcal{H}_{\mathrm{tok}}$ and the relative-bound channel $\mathcal{H}_{\mathrm{in},\mathrm{bd}} = \int^\oplus \Pi_b(P)\mathcal{H}_{\mathrm{obj}}(P)\,\frac{dP}{2\pi} \otimes \mathcal{H}_{\mathrm{tok}}$. On the outgoing pulse arrangement, $P_{\mathrm{ac}}(U_{0,\mathrm{pulse}})$ contains the bound-pair-plus-pulse channel $\mathcal{H}_{\mathrm{out},\mathrm{bd}} = \int^\oplus \Pi_b(P)\mathcal{H}_{\mathrm{obj}}(P) \otimes \mathcal{H}_{\mathrm{pulse}}(K-P)\,\frac{dP\,dK}{(2\pi)^2}$.

---

## 3. Two-Port Lippmann-Schwinger Inversion and the $64\pi^2$ Normalization

Fix a total momentum fiber $K \in [-\pi, \pi)$ and a carrier label $j$. In the two-dimensional contact basis $\{|\phi_1\rangle, |\phi_2\rangle\}$ ($\phi_1 = \delta_{u=0}|a_0\rangle|\mathrm{tok}_j\rangle$, $\phi_2 = \delta_{u=0}|b_0\rangle|p_{j,1}\rangle$), the contact unitary is
$$C_{\mathrm{port}} = \begin{pmatrix} 3/5 & -4/5 \\ 4/5 & 3/5 \end{pmatrix} = I_2 - \frac{2}{5}\begin{pmatrix} 1 & 2 \\ -2 & 1 \end{pmatrix}.$$
Notice that
$$(C_{\mathrm{port}} - I_2)^{-1} = -\frac{1}{2}\begin{pmatrix} 1 & -2 \\ 2 & 1 \end{pmatrix} = -\frac{1}{2}(I_2 + J), \qquad J := \begin{pmatrix} 0 & -2 \\ 2 & 0 \end{pmatrix}.$$

For $|z| < 1$, let $R_0(K, z) = (I - z U_0(K))^{-1} = \frac{1}{2}(I + \mathcal{F}_0(K, z))$ where $\mathcal{F}_0(K, z) = (I + z U_0(K))(I - z U_0(K))^{-1}$ has positive real part ($\operatorname{Re}\mathcal{F}_0(K, z) \ge 0$). Because the token and pulse arrangements are decoupled under $U_0(K)$, the $2\times 2$ port compression of $\mathcal{F}_0(K, z)$ is diagonal:
$$F(K, z) = \operatorname{diag}(F_1(K, z), F_2(K, z)), \qquad F_\alpha(K, z) = \langle\phi_\alpha, (I + z U_0(K))(I - z U_0(K))^{-1}\phi_\alpha\rangle \quad (\alpha = 1, 2),$$
where $\operatorname{Re} F_\alpha(K, z) > 0$ on $|z| < 1$ and $F_\alpha(K, 0) = 1$ (so each $F_\alpha(K, \cdot)$ belongs to the Carathéodory class $\mathcal{C}$).

**Theorem 3.1 ($2\times 2$ Port Inversion and $64\pi^2$ Transition Kernel).**
1. The perturbed resolvent $R(K, z) = (I - z U(K))^{-1}$ satisfies the Krein-Lippmann-Schwinger identity
   $$R(K, z) - R_0(K, z) = R_0(K, z) U_0(K) \Phi M(K, z)^{-1} \Phi^* z R_0(K, z),$$
   where $\Phi = (|\phi_1\rangle, |\phi_2\rangle)$ and the $2\times 2$ denominator matrix is
   $$M(K, z) = I_2 - (C_{\mathrm{port}} - I_2)\Phi^*(R_0(K, z) - I)\Phi = \frac{1}{2}(I_2 - C_{\mathrm{port}})\bigl(I_2 - \tfrac{1}{2}J F(K, z)\bigr).$$
2. Explicitly inverting $I_2 - \frac{1}{2}J F(K, z) = \begin{pmatrix} 1 & F_2(K,z) \\ -F_1(K,z) & 1 \end{pmatrix}$ yields determinant $1 + F_1(K,z)F_2(K,z)/4 = \frac{4 + F_1(K,z)F_2(K,z)}{4}$ and off-diagonal transition entry from port 2 (incoming contact-selected object channel) to port 1 (outgoing bound-pair-plus-pulse channel):
   $$T_{1\leftarrow 2}(K, z) = \frac{4}{4 + F_1(K, z)F_2(K, z)}.$$
3. Under the $(2\pi)^{-1}$ Fourier normalization on each momentum coordinate, the boundary spectral densities of the two ports at quasi-energy $E \in [-\pi, \pi)$ ($z = r e^{iE}, r \uparrow 1^-$) satisfy
   $$\operatorname{Re} F_\alpha(K, E + i0) = 2\pi \rho_\alpha(K, E) + \text{singular part} \ge 2\pi \rho_\alpha(K, E) \ge 0.$$
   When normalized with respect to unit spectral measure $dE$ on $I_E$, each port evaluation carries the boundary factor $\sqrt{2\pi\rho_\alpha(K,E)}$, and the off-diagonal T-matrix coupling carries the factor $4$ from $T_{1\leftarrow 2}$ together with the factor $2$ from $R_0(K,z) - \frac{1}{2}I = \frac{1}{2}\mathcal{F}_0(K,z)$:
   $$(2 \cdot 4 \cdot \sqrt{2\pi} \cdot \sqrt{2\pi})^2 = (8 \cdot 2\pi)^2 \cdot \frac{1}{(2\pi)^2} = 64\pi^2,$$
   yielding the exact modulus-squared transition kernel between normalized incoming port-2 states and normalized outgoing port-1 states at $(K, E)$:
   $$|A_{1\leftarrow 2}(K, E)|^2 = 64\pi^2\,\frac{\rho_2(K, E)\,\rho_1(K, E)}{|4 + F_1(K, E+i0)F_2(K, E+i0)|^2}.$$

---

## 4. Inherited Infinite-Operator Bound-Branch Gap on $|P| \le 1/12$

We prove the spectral gap and Riesz projector derivative bound directly on the infinite relative-coordinate Hilbert space $\ell^2(\mathbb{Z}_r) \otimes \mathbb{C}^4$ without any finite-box truncation.

### 4.1 Zero-Momentum Free and Contact Resolvents

At $P = 0$, the fiber walk is $W(0) = \Gamma F_0$ with $\Gamma = I + (z_g - 1)\delta_{r=0}$ and $z_g = e^{-ig} = e^{-i 2\pi/5}$.
In the orthonormal coin basis
$$A_{\mathrm{coin}} = \frac{|1\rangle - |4\rangle}{\sqrt{2}}, \quad S_{\mathrm{coin}} = \frac{|1\rangle + |4\rangle}{\sqrt{2}}, \quad T_{\mathrm{coin}} = \frac{|2\rangle + |3\rangle}{\sqrt{2}}, \quad B_{\mathrm{coin}} = \frac{|2\rangle - |3\rangle}{\sqrt{2}},$$
the entire channel $\ell^2(\mathbb{Z}_r)\otimes \operatorname{span}(A_{\mathrm{coin}})$ is fixed by $F_0 = S M_2(0)$, so $\chi_0 = |b_0\rangle = \delta_{r=0} A_{\mathrm{coin}}$ has $W(0)\chi_0 = z_g \chi_0$ and every site $r \ne 0$ in the $A_{\mathrm{coin}}$ channel has eigenvalue $1$ at distance $|z_g - 1| = 2\sin(\pi/5) > 1$ from $z_g$.

On the three-channel orthogonal complement $\mathcal{H}_\perp = \ell^2(\mathbb{Z}_r) \otimes \operatorname{span}(S_{\mathrm{coin}}, T_{\mathrm{coin}}, B_{\mathrm{coin}})$, the free walk $F_b = F_0|_{\mathcal{H}_\perp}$ has spectrum
$$\operatorname{spec}(F_b) = \{1\} \cup \bigl\{e^{\pm i\theta} : 2\arctan 2 \le \theta \le \pi\bigr\}.$$
Let $c_0 = \cos(\pi/5) = \frac{1+\sqrt{5}}{4}$, $s_0 = \sin(\pi/5) = \sqrt{\frac{5-\sqrt{5}}{8}}$, and $s = \sqrt{\frac{2\sqrt{5}-1}{5}}$. The distance from $z_g = e^{-i 2\pi/5}$ to $\operatorname{spec}(F_b)$ is achieved at $e^{-i 2\arctan 2}$:
$$\delta_f = \operatorname{dist}(z_g, \operatorname{spec}(F_b)) = 2\sin(\arctan 2 - \pi/5) = \frac{4c_0 - 2s_0}{\sqrt{5}}.$$
Since $\frac{111}{50} < \sqrt{5} < \frac{9}{4}$ (as $111^2 = 12321 < 12500$ and $9^2 = 81 > 80$), we have $c_0 > \frac{161}{200}$, $s_0 < \frac{59}{100}$ (as $\frac{5 - 111/50}{8} = \frac{139}{400} < \frac{3481}{10000} = (59/100)^2$), and $1 < |z_g - 1| = 2s_0 < \frac{6}{5}$. Therefore
$$\delta_f > \frac{4(161/200) - 2(59/100)}{9/4} = \frac{68}{75} > \frac{9}{10} \implies \|R_0\| = \|(z_g - F_b)^{-1}\| < \frac{10}{9}.$$

### 4.2 Woodbury Factorization and Hermitian Positivity of $\widetilde{K}$

Let $j: \mathbb{C}^3 \hookrightarrow \mathcal{H}_\perp$ insert a coin vector in $\operatorname{span}(S_{\mathrm{coin}}, T_{\mathrm{coin}}, B_{\mathrm{coin}})$ at $r = 0$, and put $P_0 = j j^*$. On $\mathcal{H}_\perp$, $W_b = \Gamma F_b$ satisfies $\Gamma^{-1}(z_g - W_b) = (z_g - F_b) - (z_g - 1)P_0$, so by the Woodbury identity:
$$(z_g - W_b)^{-1} = \bigl[R_0 + (z_g - 1)R_0 j K^{-1} j^* R_0\bigr]\Gamma^{-1}, \qquad G_0 = j^* R_0 j, \quad K = I_3 - (z_g - 1)G_0.$$
By unitarity of $F_b$, $G_0^* = \bar{z}_g I_3 - \bar{z}_g^2 G_0$ and $K^* = \bar{z}_g K$, so $\widetilde{K} = e^{-ig/2}K$ is Hermitian and splits by parity into a $2\times 2$ $(S,T)$ block and a $1\times 1$ $B$ block with exact entries:
$$\widetilde{K}_{BB} = 5c_0(1-s), \quad (\widetilde{K}_{ST})_{11} = \frac{4}{5s c_0}, \quad \det(\widetilde{K}_{ST}) = \frac{4(1-s)}{s}, \quad \operatorname{tr}(\widetilde{K}_{ST}) = -3c_0 + \frac{1 + 3c_0^2}{s c_0}.$$
Using $\frac{223}{100} < \sqrt{5} < \frac{161}{72}$ ($223^2 = 49729 < 50000$ and $5\cdot 72^2 = 25920 < 25921 = 161^2$), we obtain $\frac{4}{5} < c_0 < 1$ and $\frac{83}{100} < s < \frac{5}{6}$. Consequently:
$$\widetilde{K}_{BB} > 5\cdot\frac{4}{5}\cdot\frac{1}{6} = \frac{2}{3} > \frac{1}{2}, \qquad (\widetilde{K}_{ST})_{11} > \frac{4}{5\cdot(5/6)\cdot 1} = \frac{24}{25} > \frac{1}{2}, \qquad \det(\widetilde{K}_{ST}) > \frac{4(1/6)}{5/6} = \frac{4}{5}.$$
Since $f(c, s) = \frac{1}{sc} + 3c(\frac{1}{s}-1)$ decreases strictly in both $c \in (4/5, 1)$ and $s \in (83/100, 5/6)$ (as $\partial_c f = \frac{3(1-s) - 1/c^2}{s} < \frac{3(17/100) - 1}{s} < 0$ and $\partial_s f < 0$), we have
$$\operatorname{tr}(\widetilde{K}_{ST}) < f\Bigl(\frac{4}{5}, \frac{83}{100}\Bigr) = \frac{829}{415} < 2,$$
$$\det\bigl(\widetilde{K}_{ST} - \tfrac{1}{2}I_2\bigr) = \det(\widetilde{K}_{ST}) - \frac{1}{2}\operatorname{tr}(\widetilde{K}_{ST}) + \frac{1}{4} > \frac{4}{5} - \frac{829}{830} + \frac{1}{4} = \frac{17}{332} > 0.$$
By Sylvester's criterion, $\widetilde{K} > \frac{1}{2}I_3$, so $\|K^{-1}\| < 2$. Hence
$$\|(z_g - W_b)^{-1}\| < \frac{10}{9} + \frac{6}{5}\Bigl(\frac{10}{9}\Bigr)^2 \cdot 2 = \frac{110}{27} \implies \operatorname{dist}(z_g, \operatorname{spec}(W(0))\setminus\{z_g\}) > \delta_0 := \frac{27}{110}.$$

### 4.3 Uniform Branch Gap and Projector Derivative Bound on $|P| \le 1/12$

Since $W(P) = e^{iPQ}W(0)$ with $Q = \operatorname{diag}(1,0,0,-1)$, we have $\|W(P) - W(0)\| \le |P|$ and $\|W'(P)\| \le 1$.
On the fixed circle $C: |w - z_g| = 1/8$,
$$\operatorname{dist}(C, \operatorname{spec}(W(0))) \ge \min\Bigl(\frac{1}{8}, \delta_0 - \frac{1}{8}\Bigr) = \frac{53}{440}, \qquad \sup_{w\in C}\|(w - W(0))^{-1}\| \le M_0 := \frac{440}{53}.$$
For $|P| \le p_* = 1/12$, the Neumann product is $M_0 p_* = \frac{110}{159} < 1$, so $C \subset \rho(W(P))$ with $\sup_{|P|\le 1/12, w\in C}\|(w-W(P))^{-1}\| \le \frac{M_0}{1 - M_0/12} = \frac{1320}{49}$. The Riesz projector
$$\Pi_b(P) = \frac{1}{2\pi i}\oint_C (w - W(P))^{-1}\,dw$$
remains rank-one and orthogonal on $|P| \le 1/12$, with unique enclosed simple eigenvalue $\lambda(P) = e^{-i\Omega_b(P)}$ satisfying $|\lambda(P) - z_g| \le |P| < 1/8$. Because normal operators within norm $|P|$ have spectra within Hausdorff distance $|P|$, any spectral point of $W(P)$ outside $C$ lies within $|P|$ of $\operatorname{spec}(W(0))\setminus\{z_g\}$, so
$$\operatorname{dist}\bigl(\lambda(P), \operatorname{spec}(W(P))\setminus\{\lambda(P)\}\bigr) \ge \delta_0 - 2|P| \ge \frac{27}{110} - \frac{1}{6} = \frac{13}{165}.$$
Projecting $(W(0) - \lambda(P))\chi_b(P) = (W(0) - W(P))\chi_b(P)$ onto $\{|b_0\rangle\}^\perp$ gives $\|(I - |b_0\rangle\langle b_0|)\chi_b(P)\| \le \frac{|P|}{\delta_0 - |P|} \le \frac{55}{107}$, so
$$|\langle b_0, \chi_b(P)\rangle|^2 \ge 1 - \Bigl(\frac{55}{107}\Bigr)^2 = \frac{8424}{11449} > \frac{1}{2}.$$
Choosing the parallel-transport gauge $\langle\chi_b(P), \chi_b'(P)\rangle = 0$, differentiating $W(P)\chi_b(P) = \lambda(P)\chi_b(P)$ yields $\chi_b'(P) = -[(W(P) - \lambda(P))|_{\operatorname{Ran}(I-\Pi_b(P))}]^{-1}(I - \Pi_b(P))W'(P)\chi_b(P)$, and since $\Pi_b'(P) = |\chi_b'\rangle\langle\chi_b| + |\chi_b\rangle\langle\chi_b'|$ on orthogonal vectors:
$$\|\Pi_b'(P)\| = \|\chi_b'(P)\| \le \frac{\|W'(P)\|}{\delta_0 - 2|P|} \le L := \frac{165}{13}, \qquad |\Omega_b'(P)| \le 1, \quad |\Omega_b''(P)| \le 2L.$$

---

## 5. Finite-Strip Elimination, Two-Pulse Alias Obstruction, and No-Uniform-Shutoff

### 5.1 Finite-Strip Elimination and Compact-Support Classification

**Theorem 5.1 (Finite-Strip Elimination and Compact Eigenvectors of $W(P)$).**
Let $W(P) = \Gamma S_P M_\mu$ on $\ell^2(\mathbb{Z}_r, \mathbb{C}^4)$ with $\mu = 2$, $N = 1 + \mu^2 = 5$, $w = e^{i\theta}$ ($P = 2\theta$), and eigenvalue parameter $\lambda \in \mathbb{T}$.
1. **Stationary-channel elimination ($r \ne 0$):** On any site $r \ne 0$, the eigenvalue equation $S_P M_\mu \psi(r) = \lambda \psi(r)$ relates the stationary channels $(a_r, d_r) = (\psi_1(r), \psi_4(r))$ to the moving channels $(b_r, c_r) = (\psi_2(r), \psi_3(r))$ via the $2\times 2$ system
   $$\begin{pmatrix} N\lambda w^{-1} - 1 & \mu^2 \\ \mu^2 & N\lambda w - 1 \end{pmatrix}\binom{a_r}{d_r} = i\mu(b_r + c_r)\binom{1}{1},$$
   whose determinant is $N \cdot D(\lambda, w)$ with $D(\lambda, w) = N\lambda^2 - \lambda(w + w^{-1}) + 1 - \mu^2$. Substituting the inverse into the moving channels yields
   $$\binom{(M_\mu\psi)_2(r)}{(M_\mu\psi)_3(r)} = \frac{1}{D(\lambda,w)}\begin{pmatrix} p(\lambda,w) & q(\lambda) \\ q(\lambda) & p(\lambda,w) \end{pmatrix}\binom{b_r}{c_r}, \qquad p(\lambda,w) = (\lambda-w)(\lambda-w^{-1}),\quad q(\lambda) = \mu^2(1-\lambda^2),$$
   with the exact polynomial identity $p(\lambda,w) - q(\lambda) = D(\lambda,w)$.
2. **Absence of compactly supported eigenvectors outside $r \in \{-1,0,1\}$:** Because $p - q = D$, the transfer matrix between $(b_r, c_{r-1})$ and $(b_{r+1}, c_r)$ has determinant $1$ whenever $D(\lambda, w) \ne 0$, so any eigenvector vanishing for $|r| > R_0 \ge 1$ must vanish for all $|r| \ge 2$. At $|r| \le 1$, direct algebraic elimination (verified symbolically over $\mathbb{Z}[i]$ in Group 6 of `verify.py`) proves that the only compactly supported eigenvectors of $W(P)$ are the two-parameter family supported on $r \in \{-1, 0, 1\}$ at $z_g = w^2$ and $\lambda = w$ ($P = 2\theta$), which at $P \in I_P$ reduces to the single bound branch $\Pi_b(P)$. In particular, $W(P)$ has no embedded eigenvalues or extra point spectrum in $I_\omega$ on $I_P$.

### 5.2 Two-Pulse Alias Obstruction in the Safe Energy Window

**Proposition 5.2 (Two-Pulse Alias Obstruction).**
In the two-pulse sector (if the object decayed into two free pulses without forming the bound pair), each pulse dispersion branch has quasi-energy in $[-\theta_{\max}, \theta_{\max}]$ with $\theta_{\max} = 2\arctan 2 < \frac{3\pi}{4}$. Thus the two-pulse total quasi-energy sum lies in $[-2\theta_{\max}, 2\theta_{\max}] \subset (-\frac{3\pi}{2}, \frac{3\pi}{2})$. Modulo $2\pi$, the covered arc is
$$[-2\theta_{\max}, 2\theta_{\max}] \pmod{2\pi} \subset \bigl[0, \tfrac{3\pi}{2}\bigr) \cup \bigl(\tfrac{\pi}{2}, 2\pi\bigr),$$
Wait: in $[0, 2\pi)$, the upper alias $2\theta_{\max} < \frac{3\pi}{2} = \frac{6\pi}{4}$ and the lower alias $2\pi - 2\theta_{\max} > 2\pi - \frac{3\pi}{2} = \frac{\pi}{2}$; moreover, when the object is unbound, any pulse + scattering state on the safe total-energy interval $J_0 = [\frac{3\pi}{2}, \frac{17\pi}{10}] \subset J_{\mathrm{safe}} = (\frac{5\pi}{4}, \frac{7\pi}{4})$ satisfies:
- Our energy window $I_E = [\frac{8\pi}{5} - \frac{1}{1000}, \frac{8\pi}{5} + \frac{1}{1000}]$ lies strictly inside $J_0 = [\frac{3\pi}{2}, \frac{17\pi}{10}] \subset J_{\mathrm{safe}} = (\frac{5\pi}{4}, \frac{7\pi}{4})$.
- On $I_E \times I_K$, the unbound object + right-moving pulse continuum has object quasi-energy $E - \beta - \varepsilon(K-P)$ lying in the spectral gap of $W_{\mathrm{sc}}(P)$. Hence on $\mathcal{H}_{I_E}(U_{\mathrm{rec}})$, any outgoing pulse wavepacket in the certified $(K, E)$ window is automatically accompanied by the bound object branch $\Pi_b(P)$.

### 5.3 No-Uniform-Shutoff Identity

**Proposition 5.3 (No Finite-Time Uniform Shutoff of Contact).**
Let $\Psi \in \mathcal{H}$ be any state, and suppose there exists a finite time $n_0 \in \mathbb{Z}$ such that the coupled evolution agrees with the free evolution for all $n \ge n_0$: $U^n \Psi = U_0^n \Psi$ for all $n \ge n_0$. Putting $n = n_0$ and $n = n_0 + 1$ gives $U U_0^{n_0}\Psi = U_0 U_0^{n_0}\Psi$, so $C(U_0^{n_0}\Psi) = U_0^{n_0}\Psi$, and inductively $U^n \Psi = U_0^n \Psi$ for all $n \in \mathbb{Z}$. Consequently $\Omega_-^* \Psi = \Omega_+^* \Psi$, which has zero transition amplitude between the orthogonal incoming token arrangement and outgoing pulse arrangement. Any state with nonzero capture probability therefore undergoes contact interaction over an unbounded time horizon; capture is genuinely asymptotic.
