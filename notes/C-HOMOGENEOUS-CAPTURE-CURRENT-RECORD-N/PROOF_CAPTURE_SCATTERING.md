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
$$A = \frac{|1\rangle - |4\rangle}{\sqrt{2}}, \qquad B = \frac{|2\rangle - |3\rangle}{\sqrt{2}}, \qquad |b_0\rangle = \delta_{r=0}A, \qquad |a_0\rangle = \delta_{r=0}\,iB.$$
Direct multiplication gives $M_2(|1\rangle - |4\rangle) = |1\rangle - |4\rangle$ and $M_2(|2\rangle - |3\rangle) = |2\rangle - |3\rangle$. At center momentum $P = 0$, $S$ fixes $r = 0$ on $|1\rangle, |4\rangle$, so $|b_0\rangle = \delta_{r=0}A$ is an exact eigenvector of $W(0)$ with eigenvalue $z_g = e^{-ig}$.

### 1.2 Carrier Space, 26-Label Allocation, and Homogeneous Contact

The single-carrier space is $\mathcal{H}_{\mathrm{car}} = \mathcal{H}_{\mathrm{tok}} \oplus \mathcal{H}_{\mathrm{pulse}}$ with carrier site $y \in \mathbb{Z}$ and label $j \in \{0, 1, \dots, 25\}$:
- $\mathcal{H}_{\mathrm{tok}} = \ell^2(\mathbb{Z}_y) \otimes \mathbb{C}^{26}$ with basis $|\mathrm{tok}_j(y)\rangle$, evolving trivially under the unphased free carrier step ($V_{\mathrm{tok}} = I$).
- $\mathcal{H}_{\mathrm{pulse}} = \ell^2(\mathbb{Z}_x, \mathbb{C}^2) \otimes \mathbb{C}^{26}$ with basis $|p_{j,b}(x)\rangle$ ($b \in \{1,2\}$), evolving under $V = E Q$ where the on-site coin $Q$ and bond hop $E = D_{\mathrm{edge}}$ are
  $$Q\binom{\psi_1(x)}{\psi_2(x)} = \begin{pmatrix} c & -s \\ s & c \end{pmatrix}\binom{\psi_1(x)}{\psi_2(x)}, \qquad E\binom{v_1(x)}{v_2(x)} = \binom{c v_1(x) - s v_2(x+1)}{s v_1(x-1) + c v_2(x)}, \qquad c = \frac{1}{\sqrt{5}},\; s = \frac{2}{\sqrt{5}}.$$
  In Fourier momentum $k \in [-\pi, \pi)$ ($|x\rangle \mapsto e^{-ikx}$, so $(T_{-1}\psi)(x) = \psi(x+1)$ has multiplier $e^{ik}$ and $(T_{+1}\psi)(x) = \psi(x-1)$ has multiplier $e^{-ik}$), the factors and exact product symbol are
  $$E(k) = \frac{1}{\sqrt{5}}\begin{pmatrix} 1 & -2e^{ik} \\ 2e^{-ik} & 1 \end{pmatrix}, \qquad Q = \frac{1}{\sqrt{5}}\begin{pmatrix} 1 & -2 \\ 2 & 1 \end{pmatrix},$$
  $$V(k) = E(k)Q = \frac{1}{5}\begin{pmatrix} 1 - 4e^{ik} & -2(1 + e^{ik}) \\ 2(1 + e^{-ik}) & 1 - 4e^{-ik} \end{pmatrix}, \qquad \widetilde{V}(k) = e^{-i\beta}V(k).$$
  Direct computation gives $\det V(k) = \frac{1}{25}\bigl[(1-4e^{ik})(1-4e^{-ik}) + 4(1+e^{ik})(1+e^{-ik})\bigr] = 1$ and
  $$\frac{1}{2}\operatorname{tr} V(k) = \frac{1 - 4\cos k}{5} = \cos\varepsilon(k), \qquad \varepsilon(k) := \arccos\Bigl(\frac{1-4\cos k}{5}\Bigr) \in [\pi - b, b],$$
  where $b = \arccos(-3/5) = \pi - 2\arctan 2$ and $a := b - \pi/2 = 2\arctan 2 - \pi/2$ (note that the half-bandwidth of $\varepsilon$ around $\pi/2$ is $a$, while $2\arctan 2 = \pi - \arccos(-3/5) = b < 3\pi/4$). For $k \in (-\pi, 0)$, the branch with eigenvalue $e^{-i\varepsilon(k)}$ has positive group velocity
  $$v(k) = \varepsilon'(k) = -\frac{4\sin k}{5\sin\varepsilon(k)} > 0 \qquad (k \in (-\pi, 0)),$$
  and its normalized eigenvector $u_+(k) = (u_{+,1}(k), u_{+,2}(k))^T$ (projected onto by $P_+(k) = u_+(k)u_+(k)^*$) satisfies
  $$|u_{+,1}(k)|^2 = \frac{1 - v(k)}{2}.$$

The free macrostep on $\mathscr{H}_{\mathrm{ch}} = \mathcal{H}_{\mathrm{obj}} \otimes \mathcal{H}_{\mathrm{car}}$ is $U_0 = e^{-i\beta}(W \otimes V_{\mathrm{car}})$ with $\beta = 4\pi/5$.
The homogeneous contact unitary $C$ acts at coincidence $R = y = s, r = 0$ independently on each label $j \in \{0,\dots,25\}$ on the two orthonormal local vectors
$$\alpha_{s,j} = |R=s, r=0, iB\rangle \otimes |y=s, t_j\rangle, \qquad \beta_{s,j} = |R=s, r=0, A\rangle \otimes |x=s, \uparrow, p_j\rangle$$
via the core rotation $C_{\mathrm{core}} = \begin{pmatrix} c_* & -s_* \\ s_* & c_* \end{pmatrix} = \begin{pmatrix} 3/5 & -4/5 \\ 4/5 & 3/5 \end{pmatrix}$:
$$C\alpha_{s,j} = \frac{3}{5}\alpha_{s,j} + \frac{4}{5}\beta_{s,j}, \qquad C\beta_{s,j} = -\frac{4}{5}\alpha_{s,j} + \frac{3}{5}\beta_{s,j},$$
and as the identity on the orthogonal complement. The coupled macrostep is $U = U_0 C$.

---

## 2. Joint Momentum Fiber Decomposition and Wave Operators

### 2.1 Reduction to Total-Momentum Fibers $K = P + k$

Let $\mathsf{T}_m: (R, r, s) \mapsto (R+m, r, s+m)$ be the simultaneous lattice translation of the object center and the carrier ($s = y$ for a token or $s = x$ for a pulse) by $m \in \mathbb{Z}$. Both $U_0$ and $C$ commute with $\mathsf{T}_m$ and preserve each carrier label $j \in \{0,\dots,25\}$. Under the unitary change of variables $(R, s) \mapsto (s, u := R - s)$ and Fourier transform in $s \leftrightarrow K \in [-\pi, \pi)$:
$$\mathscr{H}_{\mathrm{ch}} \cong \int_{[-\pi,\pi)}^{\oplus} \bigl(\mathcal{H}_{\mathrm{tok},\mathrm{rel}} \oplus \mathcal{H}_{\mathrm{pulse},\mathrm{rel}}\bigr)\,\frac{dK}{2\pi} \otimes \mathbb{C}^{26},$$
where $\mathcal{H}_{\mathrm{tok},\mathrm{rel}} = \ell^2(\mathbb{Z}_u \times \mathbb{Z}_r, \mathbb{C}^4)$ and $\mathcal{H}_{\mathrm{pulse},\mathrm{rel}} = \ell^2(\mathbb{Z}_u \times \mathbb{Z}_r, \mathbb{C}^4) \otimes \mathbb{C}^2$.
In the dual momentum coordinates $(P, k)$ with $R \leftrightarrow P$ and $s \leftrightarrow k$, the conserved total fiber momentum is $K = P + k \pmod{2\pi}$:
- On the token arrangement, the token stands at $y$, so $u = R - y$ shifts only under $W$ and $P$ is conserved under $U_{0,1} = e^{-i\beta}W$: on fiber $P$, $U_{0,1}(P) = e^{-i\beta}W(P)$.
- On the pulse arrangement, a pulse hop $x \mapsto x \pm 1$ shifts $u = R - x \mapsto u \mp 1$ and multiplies fiber $K$ by $e^{\mp iK}$, so at object center momentum $P$ the pulse carries momentum $k = K - P$, and $U_{0,2}(K)$ acts at $P$ as $W(P) \otimes \widetilde{V}(K - P) = e^{-i\beta}W(P) \otimes V(K - P)$.
- On each fiber $K$ and each fixed label $j \in \{0,\dots,25\}$, the contact operator $C$ is independent of $K$ and differs from the identity only on the two-dimensional port subspace spanned by
  $$a_1 := \delta_{u=0, r=0}\,iB \oplus 0, \qquad a_2 := 0 \oplus \bigl(\delta_{u=0, r=0}\,A \otimes |\uparrow\rangle\bigr).$$

### 2.2 Existence and Completeness of Fiber and Direct-Integral Wave Operators

**Proposition 2.1 (Fiberwise and Direct-Integral Wave Operators).**
For every $K \in [-\pi, \pi)$ and every label $j \in \{0,\dots,25\}$:
1. $U(K) - U_0(K) = U_0(K)(C - I)$ has rank $2$ on each label sector ($52$ across all $26$ labels), hence is trace class.
2. By the Birman-Krein-Kato unitary trace-class scattering theorem, the fiber wave operators from the decoupled channel reference space $\mathscr{H}_{\mathrm{ch},0}(K) = \mathscr{H}_{\mathrm{ch},1}(K) \oplus \mathscr{H}_{\mathrm{ch},2}(K)$ to $\mathscr{H}_{\mathrm{ch}}(K)$,
   $$\Omega_\pm(K) := \operatorname*{s-lim}_{n\to\pm\infty} U(K)^{-n} U_0(K)^n P_{\mathrm{ac}}(U_0(K))$$
   ($\Omega_-(K)$ as $n \to -\infty$ incoming, $\Omega_+(K)$ as $n \to +\infty$ outgoing), exist, are partially isometric with initial space $\mathscr{H}_{\mathrm{ac}}(U_0(K))$ and common final space $\operatorname{Ran}\Omega_\pm(K) = \mathscr{H}_{\mathrm{ac}}(U(K))$ (asymptotic completeness), and satisfy $U(K)\Omega_\pm(K) = \Omega_\pm(K)U_0(K)$. The unitary fiber scattering operator on $\mathscr{H}_{\mathrm{ac}}(U_0(K))$ is $\mathcal{S}(K) := \Omega_+(K)^*\Omega_-(K)$.
3. Because $U(K)$ and $U_0(K)$ depend analytically on $K \in [-\pi, \pi)$, the direct-integral wave operators
   $$\Omega_\pm = \int_{[-\pi,\pi)}^{\oplus} \Omega_\pm(K)\,\frac{dK}{2\pi} = \operatorname*{s-lim}_{n\to\pm\infty} U^{-n} U_0^n P_{\mathrm{ac}}(U_0)$$
   and $\mathcal{S} = \Omega_+^*\Omega_- = \int_{[-\pi,\pi)}^\oplus \mathcal{S}(K)\,\frac{dK}{2\pi}$ exist on $\mathscr{H}_{\mathrm{ch}}$ by dominated convergence of the bounded fiber norms.

---

## 3. Two-Port Lippmann-Schwinger Inversion and the $64\pi^2$ Normalization

Fix a total momentum fiber $K \in [-\pi, \pi)$ and a carrier label $j$. Let $J: \mathbb{C}^2 \to \mathcal{H}_{\mathrm{tok},\mathrm{rel}} \oplus \mathcal{H}_{\mathrm{pulse},\mathrm{rel}}$ be the isometric port injection $J(c_1, c_2)^T = c_1 a_1 + c_2 a_2$ ($J^* J = I_2$). In the basis $\{a_1, a_2\}$, the core contact unitary and its rank-two perturbation matrix are
$$C_{\mathrm{core}} = \begin{pmatrix} c_* & -s_* \\ s_* & c_* \end{pmatrix} = \begin{pmatrix} 3/5 & -4/5 \\ 4/5 & 3/5 \end{pmatrix}, \qquad K_C := C_{\mathrm{core}} - I_2 = \begin{pmatrix} c_* - 1 & -s_* \\ s_* & c_* - 1 \end{pmatrix} = \frac{1}{5}\begin{pmatrix} -2 & -4 \\ 4 & -2 \end{pmatrix},$$
so $C = I + J K_C J^*$ and $U(K) = U_0(K)C = U_0(K)(I + J K_C J^*)$.

For $|\zeta| > 1$, let $R_0(K, \zeta) = (\zeta - U_0(K))^{-1}$ and $R(K, \zeta) = (\zeta - U(K))^{-1}$. Because $U_0(K) = U_{0,1} \oplus U_{0,2}(K)$ is block-diagonal between the token and pulse arrangements, the $2\times 2$ port compression
$$m(K, \zeta) := J^* R_0(K, \zeta) U_0(K) J = \operatorname{diag}\bigl(m_1(\zeta), m_2(K, \zeta)\bigr)$$
is diagonal, with entries
$$m_j(K, \zeta) = \bigl\langle a_j, (\zeta - U_{0,j}(K))^{-1}U_{0,j}(K) a_j\bigr\rangle = \frac{F_j(K, \zeta) - 1}{2} \qquad (j = 1, 2),$$
where the port Carathéodory functions are defined for $|\zeta| > 1$ by
$$F_j(K, \zeta) := \bigl\langle a_j, (\zeta + U_{0,j}(K))(\zeta - U_{0,j}(K))^{-1}a_j\bigr\rangle = 1 + 2m_j(K, \zeta) = \int_{-\pi}^{\pi} \frac{\zeta + e^{-iE}}{\zeta - e^{-iE}}\,d\mu_j(K, E),$$
satisfying $\operatorname{Re} F_j(K, \zeta) > 0$ on $|\zeta| > 1$ and $F_j(K, \infty) = \|a_j\|^2 = 1$ (note that $F_1(\zeta)$ is independent of $K$).

**Theorem 3.1 ($2\times 2$ Port Inversion and $64\pi^2$ Transition Kernel).**
1. Factoring $\zeta - U(K) = (\zeta - U_0(K))\bigl(I - R_0(K, \zeta)U_0(K) J K_C J^*\bigr)$ yields the exact rank-two Krein-Lippmann-Schwinger resolvent identity for $|\zeta| > 1$:
   $$R(K, \zeta) - R_0(K, \zeta) = R_0(K, \zeta) U_0(K) J\, T(K, \zeta)\, J^* R_0(K, \zeta), \qquad T(K, \zeta) := K_C\bigl(I_2 - m(K, \zeta)K_C\bigr)^{-1}.$$
2. Explicitly,
   $$I_2 - m(K, \zeta)K_C = \begin{pmatrix} 1 - (c_* - 1)m_1 & s_* m_1 \\ -s_* m_2 & 1 - (c_* - 1)m_2 \end{pmatrix}.$$
   Since $(c_* - 1)^2 + s_*^2 = 2(1 - c_*)$ and $(1 + 2m_1)(1 + 2m_2) = F_1 F_2$, its determinant is
   $$\det\bigl(I_2 - m(K, \zeta)K_C\bigr) = 1 + (1 - c_*)(m_1 + m_2 + 2m_1 m_2) = \frac{1 + c_*}{2} + \frac{1 - c_*}{2}F_1 F_2 = \frac{4 + F_1(\zeta)F_2(K, \zeta)}{5}.$$
   Multiplying $K_C = \begin{pmatrix} c_*-1 & -s_* \\ s_* & c_*-1 \end{pmatrix}$ by $\operatorname{adj}(I_2 - m K_C) = \begin{pmatrix} 1-(c_*-1)m_2 & -s_* m_1 \\ s_* m_2 & 1-(c_*-1)m_1 \end{pmatrix}$ gives the $(2,1)$ numerator $s_*(1 - (c_*-1)m_2) + (c_*-1)s_* m_2 = s_* = 4/5$ and $(1,2)$ numerator $-s_* = -4/5$, so the off-diagonal transition matrix entries are
   $$T_{21}(K, \zeta) = -T_{12}(K, \zeta) = \frac{s_*}{\det(I_2 - m(K, \zeta)K_C)} = \frac{4}{4 + F_1(\zeta)F_2(K, \zeta)}.$$
3. Under the spectral measure normalization $\langle a_j, U_{0,j}(K)^n a_j\rangle = \int_{-\pi}^{\pi} e^{-inE}\,d\mu_j(K, E)$ with $d\mu_j(K, E) = \rho_j(K, E)\,dE + d\mu_{j,\mathrm{sing}}(K, E)$, the radial boundary values $F_j(K, E) := \lim_{r\downarrow 1} F_j(K, r e^{-iE})$ satisfy
   $$\operatorname{Re} F_j(K, E) = 2\pi\,\rho_j(K, E) \qquad \text{for Lebesgue-a.e. } E \in [-\pi, \pi).$$
   By the Birman-Krein-Kato stationary representation of the unitary scattering operator $\mathcal{S}(K) = \Omega_+(K)^*\Omega_-(K)$, the modulus-squared transition kernel at $(K, E)$ from the incoming token channel with density $\rho_{1,\mathrm{in}}(E)$ to the outgoing bound-pair + right-moving pulse channel with density $\rho_{2,b,+}(K, E)$ is
   $$\mathcal{P}(K, E) = 4\pi^2\,\bigl|T_{21}(K, E)\bigr|^2\,\rho_{1,\mathrm{in}}(E)\,\rho_{2,b,+}(K, E) = \frac{64\pi^2\,\rho_{1,\mathrm{in}}(E)\,\rho_{2,b,+}(K, E)}{\bigl|4 + F_1(E)F_2(K, E)\bigr|^2}.$$
   In `reproduce/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/verify.py`, Group 2 takes this analytically derived transition kernel $\mathcal{P}(K, E)$ as input and certifies its rational interval lower bound across $(K, E) \in I_K \times I_E$.

---

## 4. Inherited Infinite-Operator Bound-Branch Gap on $|P| \le 1/12$

We prove the spectral gap and Riesz projector derivative bound directly on the infinite relative-coordinate Hilbert space $\ell^2(\mathbb{Z}_r) \otimes \mathbb{C}^4$ without any finite-box truncation.

### 4.1 Zero-Momentum Free and Contact Resolvents

At $P = 0$, the fiber walk is $W(0) = \Gamma F_0$ with $\Gamma = I + (z - 1)\delta_{r=0}$ and $z = e^{-ig} = e^{-i 2\pi/5}$.
In the orthonormal coin basis
$$A = \frac{|1\rangle - |4\rangle}{\sqrt{2}}, \quad S_{\mathrm{coin}} = \frac{|1\rangle + |4\rangle}{\sqrt{2}}, \quad T_{\mathrm{coin}} = \frac{|2\rangle + |3\rangle}{\sqrt{2}}, \quad B = \frac{|2\rangle - |3\rangle}{\sqrt{2}},$$
the entire channel $\ell^2(\mathbb{Z}_r)\otimes \operatorname{span}(A)$ is fixed by $F_0 = S M_2(0)$, so $\chi_0 = |b_0\rangle = \delta_{r=0} A$ has $W(0)\chi_0 = z \chi_0$ and every site $r \ne 0$ in the $A$ channel has eigenvalue $1$ at distance $|z - 1| = 2\sin(\pi/5) > 1$ from $z$.

On the three-channel orthogonal complement $\mathcal{H}_\perp = \ell^2(\mathbb{Z}_r) \otimes \operatorname{span}(S_{\mathrm{coin}}, T_{\mathrm{coin}}, B)$, the free walk $F_b = F_0|_{\mathcal{H}_\perp}$ has spectrum
$$\operatorname{spec}(F_b) = \{1\} \cup \bigl\{e^{\pm i\theta} : 2\arctan 2 \le \theta \le \pi\bigr\}.$$
Define the exact constants
$$c_0 = \cos\Bigl(\frac{\pi}{5}\Bigr) = \frac{1+\sqrt{5}}{4}, \quad s_0 = \sin\Bigl(\frac{\pi}{5}\Bigr) = \sqrt{\frac{5-\sqrt{5}}{8}}, \quad d = \cos(2\arctan 2) = -\frac{3}{5}, \quad b = \frac{8}{5}, \quad \ell = \frac{2}{5}, \quad s = \sqrt{\frac{2\sqrt{5}-1}{5}}.$$
The distance from $z = e^{-i 2\pi/5}$ to $\operatorname{spec}(F_b)$ is achieved at $e^{-i 2\arctan 2}$:
$$\delta_f = \operatorname{dist}(z, \operatorname{spec}(F_b)) = 2\sin(\arctan 2 - \pi/5) = \frac{4c_0 - 2s_0}{\sqrt{5}}.$$
Since $\frac{111}{50} < \sqrt{5} < \frac{9}{4}$ (as $111^2 = 12321 < 12500$ and $9^2 = 81 > 80$), we have $c_0 > \frac{161}{200}$, $s_0 < \frac{59}{100}$ (as $\frac{5 - 111/50}{8} = \frac{139}{400} < \frac{3481}{10000} = (59/100)^2$), and $1 < |z - 1| = 2s_0 < \frac{6}{5}$. Therefore
$$\delta_f > \frac{4(161/200) - 2(59/100)}{9/4} = \frac{68}{75} > \frac{9}{10} \implies \|R_0\| = \|(z - F_b)^{-1}\| < \frac{10}{9}.$$

### 4.2 Woodbury Factorization, Adjoint Identity, and Hermitian Positivity of $\widetilde{K}$

Let $j: \mathbb{C}^3 \hookrightarrow \mathcal{H}_\perp$ insert a coin vector in $\operatorname{span}(S_{\mathrm{coin}}, T_{\mathrm{coin}}, B)$ at $r = 0$, and put $P_0 = j j^*$. On $\mathcal{H}_\perp$, $W_b = \Gamma F_b$ satisfies $\Gamma^{-1}(z - W_b) = (z - F_b) - (z - 1)P_0$, so by the Woodbury identity:
$$(z - W_b)^{-1} = \bigl[R_0 + (z - 1)R_0 j K^{-1} j^* R_0\bigr]\Gamma^{-1}, \qquad G_0 = j^* R_0 j, \quad K = I_3 - (z - 1)G_0.$$
Because $F_b$ is unitary and $|z| = 1$ ($z^* = \bar{z} = z^{-1}$), the free resolvent $R_0 = (z - F_b)^{-1}$ satisfies the exact adjoint identity
$$R_0^* = \bigl((z - F_b)^{-1}\bigr)^* = (z^{-1} - F_b^{-1})^{-1} = -z F_b(z - F_b)^{-1} = z I - z^2 R_0.$$
Compressing by $j$ gives $G_0^* = j^* R_0^* j = z I_3 - z^2 G_0$, and therefore
$$K^* = I_3 - (z^{-1} - 1)(z I_3 - z^2 G_0) = I_3 - (1 - z)I_3 + z(1 - z)G_0 = z\bigl(I_3 - (z - 1)G_0\bigr) = z K.$$
Since $z = e^{-ig}$, setting $\widetilde{K} := e^{-ig/2}K$ yields $\widetilde{K}^* = e^{ig/2}K^* = e^{ig/2}e^{-ig}K = e^{-ig/2}K = \widetilde{K}$, so $\widetilde{K}$ is Hermitian. By Fourier transform on $\ell^2(\mathbb{Z}_r)$ (`CONTACT-W-BOUND-PAIR-RESPONSE [T]`), the Toeplitz integral $I_0 = \int_{-\pi}^{\pi}\frac{dk}{2\pi}\frac{1}{(z+1)^2 - 4z(\frac{1+4\cos k}{5})^2}$ satisfies $(z+1)^2 I_0 = \frac{1}{s}$, and $\widetilde{K}$ splits by parity into a $2\times 2$ $(S,T)$ block and a $1\times 1$ $B$ block with exact entries:
$$\widetilde{K}_{BB} = 5c_0(1-s), \quad (\widetilde{K}_{ST})_{11} = \frac{4}{5s c_0}, \quad \det(\widetilde{K}_{ST}) = \frac{4(1-s)}{s}, \quad \operatorname{tr}(\widetilde{K}_{ST}) = -3c_0 + \frac{1 + 3c_0^2}{s c_0}.$$
Using $\frac{223}{100} < \sqrt{5} < \frac{161}{72}$ ($223^2 = 49729 < 50000$ and $5\cdot 72^2 = 25920 < 25921 = 161^2$), we obtain $\frac{4}{5} < c_0 < 1$ and $\frac{83}{100} < s < \frac{5}{6}$. Consequently:
$$\widetilde{K}_{BB} > 5\cdot\frac{4}{5}\cdot\frac{1}{6} = \frac{2}{3} > \frac{1}{2}, \qquad (\widetilde{K}_{ST})_{11} > \frac{4}{5\cdot(5/6)\cdot 1} = \frac{24}{25} > \frac{1}{2}, \qquad \det(\widetilde{K}_{ST}) > \frac{4(1/6)}{5/6} = \frac{4}{5}.$$
Since $f(c, s) = \frac{1}{sc} + 3c(\frac{1}{s}-1)$ decreases strictly in both $c \in (4/5, 1)$ and $s \in (83/100, 5/6)$ (as $\partial_c f = \frac{3(1-s) - 1/c^2}{s} < \frac{3(17/100) - 1}{s} < 0$ and $\partial_s f < 0$), we have
$$\operatorname{tr}(\widetilde{K}_{ST}) < f\Bigl(\frac{4}{5}, \frac{83}{100}\Bigr) = \frac{829}{415} < 2,$$
$$\det\bigl(\widetilde{K}_{ST} - \tfrac{1}{2}I_2\bigr) = \det(\widetilde{K}_{ST}) - \frac{1}{2}\operatorname{tr}(\widetilde{K}_{ST}) + \frac{1}{4} > \frac{4}{5} - \frac{829}{830} + \frac{1}{4} = \frac{17}{332} > 0.$$
By Sylvester's criterion, $\widetilde{K} > \frac{1}{2}I_3$, so $\|K^{-1}\| < 2$. Hence
$$\|(z - W_b)^{-1}\| < \frac{10}{9} + \frac{6}{5}\Bigl(\frac{10}{9}\Bigr)^2 \cdot 2 = \frac{110}{27} \implies \operatorname{dist}(z, \operatorname{spec}(W(0))\setminus\{z\}) > \delta_0 := \frac{27}{110}.$$

### 4.3 Uniform Branch Gap and Projector Derivative Bound on $|P| \le 1/12$

Since $W(P) = e^{iPQ}W(0)$ with $Q = \operatorname{diag}(1,0,0,-1)$, we have $\|W(P) - W(0)\| \le |P|$ and $\|W'(P)\| \le 1$.
On the fixed circle $C: |w - z| = 1/8$,
$$\operatorname{dist}(C, \operatorname{spec}(W(0))) \ge \min\Bigl(\frac{1}{8}, \delta_0 - \frac{1}{8}\Bigr) = \frac{53}{440}, \qquad \sup_{w\in C}\|(w - W(0))^{-1}\| \le M_0 := \frac{440}{53}.$$
For $|P| \le p_* = 1/12$, the Neumann product is $M_0 p_* = \frac{110}{159} < 1$, so $C \subset \rho(W(P))$ with $\sup_{|P|\le 1/12, w\in C}\|(w-W(P))^{-1}\| \le \frac{M_0}{1 - M_0/12} = \frac{1320}{49}$. The Riesz projector
$$\Pi_b(P) = \frac{1}{2\pi i}\oint_C (w - W(P))^{-1}\,dw$$
remains rank-one and orthogonal on $|P| \le 1/12$, with unique enclosed simple eigenvalue $\lambda(P) = e^{-i\Omega(P)}$ satisfying $|\lambda(P) - z| \le |P| < 1/8$. Because normal operators within norm $|P|$ have spectra within Hausdorff distance $|P|$, any spectral point of $W(P)$ outside $C$ lies within $|P|$ of $\operatorname{spec}(W(0))\setminus\{z\}$, so
$$\operatorname{dist}\bigl(\lambda(P), \operatorname{spec}(W(P))\setminus\{\lambda(P)\}\bigr) \ge \delta_0 - 2|P| \ge \frac{27}{110} - \frac{1}{6} = \frac{13}{165}.$$
Projecting $(W(0) - \lambda(P))\chi_b(P) = (W(0) - W(P))\chi_b(P)$ onto $\{|b_0\rangle\}^\perp$ gives $\|(I - |b_0\rangle\langle b_0|)\chi_b(P)\| \le \frac{|P|}{\delta_0 - |P|} \le \frac{55}{107}$, so
$$|\langle b_0, \chi_b(P)\rangle|^2 \ge 1 - \Bigl(\frac{55}{107}\Bigr)^2 = \frac{8424}{11449} > \frac{1}{2}.$$
Choosing the parallel-transport gauge $\langle\chi_b(P), \chi_b'(P)\rangle = 0$, differentiating $W(P)\chi_b(P) = \lambda(P)\chi_b(P)$ yields $\chi_b'(P) = -[(W(P) - \lambda(P))|_{\operatorname{Ran}(I-\Pi_b(P))}]^{-1}(I - \Pi_b(P))W'(P)\chi_b(P)$, and since $\Pi_b'(P) = |\chi_b'\rangle\langle\chi_b| + |\chi_b\rangle\langle\chi_b'|$ on orthogonal vectors:
$$\|\Pi_b'(P)\| = \|\chi_b'(P)\| \le \frac{\|W'(P)\|}{\delta_0 - 2|P|} \le L := \frac{165}{13}, \qquad |\Omega'(P)| \le 1, \quad |\Omega''(P)| \le 2L.$$

---

## 5. Finite-Strip Elimination, Safe Window vs. Two-Pulse Alias, and No-Uniform-Shutoff

### 5.1 Finite-Strip Elimination, Exceptional Set $\mathcal{E}_{\mu,z}$, and Absence of Finite-Strip Invariant Subspaces

Let $P_B = \mathbf{1}_{|r| \le R_0}$ be the spatial projector onto any finite relative strip $|r| \le R_0$ ($R_0 \ge 0$).

**Theorem 5.1 (Finite-Strip Elimination and Compact-Support Classification for $W(P)$).**
Let $W(P) = \Gamma S_P M_\mu$ on $\ell^2(\mathbb{Z}_r, \mathbb{C}^4)$ with $\mu = 2$, $N = 1 + \mu^2 = 5$, $z = e^{-ig} = e^{-i 2\pi/5}$, $w = e^{i\theta}$ ($P = 2\theta \in [-\pi, \pi)$), and eigenvalue parameter $\lambda \in \mathbb{T}$. Define the finite exceptional momentum set
$$\mathcal{E}_{\mu,z} := \{0, \pi\} \cup \bigl\{P \in [-\pi, \pi) : e^{2iP} \in \{z, u_*, \bar{z}, \bar{u}_*\}\bigr\}, \qquad u_* := \frac{1 - \mu^2 + i\mu\sqrt{N - 2}}{N - 1} = \frac{-3 + 2i\sqrt{3}}{4},$$
which contains at most $10$ points ($|\mathcal{E}_{\mu,z}| \le 10$) and therefore has Lebesgue measure zero.
1. **Stationary-channel elimination ($r \ne 0$):** On any site $r \ne 0$, the eigenvalue equation $S_P M_\mu \psi(r) = \lambda \psi(r)$ relates the stationary channels $(a_r, d_r) = (\psi_1(r), \psi_4(r))$ to the moving channels $(b_r, c_r) = (\psi_2(r), \psi_3(r))$ via the $2\times 2$ system
   $$\begin{pmatrix} N\lambda w^{-1} - 1 & \mu^2 \\ \mu^2 & N\lambda w - 1 \end{pmatrix}\binom{a_r}{d_r} = i\mu(b_r + c_r)\binom{1}{1},$$
   whose determinant is $N \cdot D(\lambda, w)$ with $D(\lambda, w) = N\lambda^2 - \lambda(w + w^{-1}) + 1 - \mu^2$. Substituting the inverse into the moving channels yields
   $$\binom{(M_\mu\psi)_2(r)}{(M_\mu\psi)_3(r)} = \frac{1}{D(\lambda,w)}\begin{pmatrix} p(\lambda,w) & q(\lambda) \\ q(\lambda) & p(\lambda,w) \end{pmatrix}\binom{b_r}{c_r}, \qquad p(\lambda,w) = (\lambda-w)(\lambda-w^{-1}),\quad q(\lambda) = \mu^2(1-\lambda^2),$$
   with the exact polynomial identity $p(\lambda,w) - q(\lambda) = D(\lambda,w)$.
2. **Absence of compactly supported eigenvectors for $P \notin \mathcal{E}_{\mu,z}$:** Note first that at the special point $P = 0 \in \mathcal{E}_{\mu,z}$ ($w = 1$), $\delta_r A$ for $r \ne 0$ are compactly supported eigenvectors of $W(0)$ with eigenvalue $\lambda = 1$ (and $\delta_0 A$ has eigenvalue $z$). For $P \notin \mathcal{E}_{\mu,z}$, $w \ne \pm 1$; if $D(\lambda, w) = 0$, the moving recurrence decouples and forces vanishing outside $r = 0$, while if $D(\lambda, w) \ne 0$, the exterior transfer matrix has determinant $1$ (since $p - q = D$) and forces any compactly supported eigenvector to vanish for all $|r| \ge 2$. On $|r| \le 1$, direct algebraic elimination over $\mathbb{Z}[i]$ (verified symbolically in all 16 Laurent polynomial identity groups of Group 6 in `verify.py`) proves that a nonzero solution on $r \in \{-1, 0, 1\}$ exists only when $e^{2iP} = w^4 \in \{z, u_*, \bar{z}, \bar{u}_*\}$. Hence for every $P \notin \mathcal{E}_{\mu,z}$, $W(P)$ has **no** nonzero compactly supported eigenvector.
3. **No nonzero $W$-invariant subspace in $\operatorname{Ran} P_B$:** For any $P \notin \mathcal{E}_{\mu,z}$, the finite-dimensional subspace $\bigcap_{n\in\mathbb{Z}} W(P)^{-n}\operatorname{Ran} P_B \subset \ell^2(\mathbb{Z}_r, \mathbb{C}^4)$ is $W(P)$-invariant; if it were nonzero, it would contain a compactly supported eigenvector of $W(P)$, contradicting (2). Hence $\bigcap_{n\in\mathbb{Z}} W(P)^{-n}\operatorname{Ran} P_B = \{0\}$ for all $P \notin \mathcal{E}_{\mu,z}$. Since $\mathcal{E}_{\mu,z}$ is finite (measure zero) and $W = \int_{[-\pi,\pi)}^\oplus W(P)\,\frac{dP}{2\pi}$, any $\psi \in \bigcap_{n\in\mathbb{Z}} W^{-n}\operatorname{Ran} P_B$ has $\psi(P) \in \bigcap_{n\in\mathbb{Z}} W(P)^{-n}\operatorname{Ran} P_B = \{0\}$ for a.e. $P$, so
   $$\bigcap_{n\in\mathbb{Z}} W^{-n}\operatorname{Ran} P_B = \{0\}.$$
4. **Corollary 5.2 (No Non-Identity Translation-Invariant Finite-Strip Contact Commuting with $W \otimes V$).** If a bounded operator $C$ on $\mathcal{H}_{\mathrm{obj}} \otimes \mathcal{H}_{\mathrm{pulse}}$ satisfies $[C, W \otimes V] = 0$ and $(P_B \otimes I)(C - I) = C - I$, then for every $n \in \mathbb{Z}$, $(W^{-n}P_B W^n \otimes I)(C - I) = (W \otimes V)^{-n}(P_B \otimes I)(C - I)(W \otimes V)^n = C - I$, so $\operatorname{Ran}(C - I) \subset \bigl(\bigcap_{n\in\mathbb{Z}} W^{-n}\operatorname{Ran} P_B\bigr) \otimes \mathcal{H}_{\mathrm{pulse}} = \{0\}$, forcing $C = I$.

### 5.2 One-Carrier Safe-Window Theorem vs. Two-Pulse Alias Obstruction

We keep strictly distinct the one-carrier safe-window spectral-energy theorem and the two-pulse periodic-window alias obstruction.

**Proposition 5.3 (One-Carrier Safe-Window Intertwining Theorem).**
On the one-carrier reference space $\mathscr{H}_{\mathrm{ch},0} = \mathscr{H}_{\mathrm{ch},1} \oplus \mathscr{H}_{\mathrm{ch},2}$, let $H_0 = H_{0,1} \oplus H_{0,2}$ be the additive channel reference energy generator ($U_0 = e^{-iH_0}$) with $H_{0,1} = H_W \otimes I_{\mathrm{tok}}$ ($\sigma(H_{0,1}) \subset [\pi/2 - a, 3\pi/2 + b]$) and $H_{0,2} = H_W \otimes I_{\mathrm{pulse}} + I_{\mathrm{obj}} \otimes H_E$ ($\sigma(H_{0,2}) \subset [3\pi/2 - a - b, 3\pi/2 + 2b] = [\pi/2 - a, 5\pi/2 + a]$, where $b = \arccos(-3/5) = \pi - 2\arctan 2$ and $a = b - \pi/2 = \pi/2 - \arccos(-3/5) = 2\arctan 2 - \pi/2 < \pi/4$).
1. Since $a < \pi/4$, we have $\pi/2 + a < 3\pi/4 < 5\pi/4$ and $5\pi/2 - a > 9\pi/4$, so for every $E \in J_{\mathrm{safe}} := (5\pi/4, 7\pi/4)$ and every nonzero integer $m \in \mathbb{Z}\setminus\{0\}$, $E + 2\pi m \notin [\pi/2 - a, 5\pi/2 + a] \supset \sigma(H_0)$.
2. Consequently, on the closed safe window $J_0 = [3\pi/2, 17\pi/10] \subset J_{\mathrm{safe}}$ containing our packet window $I_E = [8\pi/5 - 1/1000, 8\pi/5 + 1/1000]$, modular quasi-energy $e^{-iE}$ uniquely determines the additive reference energy $E \in \sigma(H_0)$, so $P_{J_0}(U_0) = \mathbf{1}_{J_0}(H_0)$ and the receiver-conjugated scattering operator $\mathcal{S}_{\mathrm{rec}}$ commutes with $H_0 \otimes I_{\mathrm{rec}}$ on $\operatorname{Ran}(\mathbf{1}_{J_0}(H_0) \otimes I_{\mathrm{rec}})$:
   $$(H_0 \otimes I_{\mathrm{rec}})\,\mathcal{S}_{\mathrm{rec}}\,\mathbf{1}_{J_0}(H_0 \otimes I_{\mathrm{rec}}) = \mathcal{S}_{\mathrm{rec}}\,(H_0 \otimes I_{\mathrm{rec}})\,\mathbf{1}_{J_0}(H_0 \otimes I_{\mathrm{rec}}).$$

**Proposition 5.4 (Two-Pulse Periodic-Window Alias Obstruction).**
On the two-pulse reference sector $\mathcal{H}_{\mathrm{obj}} \otimes \mathcal{H}_{\mathrm{pulse}} \otimes \mathcal{H}_{\mathrm{pulse}}$ with additive generator $H^{(2)} = H_W + H_E + H_E$ ($U_0^{(2)} = e^{-iH^{(2)}}$), where $\sigma(H_E) = [\pi - b, b]$ has width $2b - \pi = 2a = 4\arctan 2 - \pi > 0$ and $\sigma(H_W) \supset [\beta - a, \beta + a] \cup [\beta + \pi - b, \beta + b]$:
1. The sumset $\sigma(H^{(2)}) = \sigma(H_W) + \sigma(H_E) + \sigma(H_E)$ contains the contiguous interval
   $$J_* := [2\beta - 2a - b,\; 2\beta + 2a + \pi + b],$$
   whose length is $|J_*| = \pi + 4a + 2b = 3\pi + 6a = 3\pi + 3(4\arctan 2 - \pi) = 12\arctan 2 > 4\pi$ (in fact $3\pi + 2a > 4\pi$ since $2a = 4\arctan 2 - \pi > \pi \iff \arctan 2 > \pi/2$ — more directly, $2b - \pi = 2a > \pi/3$, so $\pi + 4a + 2b = 2\pi + 6a > 4\pi$).
2. Because $J_* \subset \sigma(H^{(2)})$ is an interval of length strictly exceeding $4\pi$, **every** point $E \in \sigma(H^{(2)})$ has at least one $2\pi$-alias in $\sigma(H^{(2)})$:
   $$\forall E \in \sigma(H^{(2)}), \qquad \{E - 2\pi, E + 2\pi\} \cap \sigma(H^{(2)}) \ne \varnothing.$$
   Therefore, no periodic spectral window of $U_0^{(2)}$ is alias-free on the two-pulse sector; in the present one-carrier package, outgoing binding is selected explicitly by the bound-branch projector $\Pi_b(P)$ in $Q_{\mathrm{full}}$ and $Q_{\mathrm{win}}$, not inferred from pulse energy or receiver memory $|d_1\rangle$ alone.

### 5.3 No-Uniform-Shutoff Identity

**Proposition 5.5 (No Uniform Finite-Time Shutoff on the Incoming Packet Family vs. Per-State Dispersion).**
Let $D: L^2(I_E) \to \mathscr{H}_{\mathrm{ch},1}$ be the isometric incoming packet family $D f := \mathcal{F}_{P,E}^{-1}\bigl(f(E)\xi_{\mathrm{in}}(P, E)\bigr) \otimes |y=0, t_1\rangle$, where $\psi_{\mathrm{in}} = D(\ell_E^{-1/2}\mathbf{1}_{I_E})$.
1. **Uniform operator norm over the translated packet family:** For every $n \in \mathbb{Z}$ and every $f \in L^2(I_E)$, the intertwining identity $U\Omega_- = \Omega_- U_0$ gives $U^n \Omega_- D f = \Omega_- U_0^n D f = \Omega_- D(e^{-inE}f)$. Since multiplication by $e^{-inE}$ is a unitary bijection of $L^2(I_E)$ onto itself,
   $$\sup_{\|f\|_{L^2(I_E)} = 1} \bigl\|(C - I) U^n \Omega_- D f\bigr\| = \sup_{\|g\|_{L^2(I_E)} = 1} \bigl\|(C - I)\Omega_- D g\bigr\| = \bigl\|(C - I)\Omega_- D\bigr\| > 0 \qquad (\forall n \in \mathbb{Z}),$$
   where $\|(C-I)\Omega_- D\| > 0$ because if $(C-I)\Omega_- D = 0$, then $U^n\Omega_- D = U_0^n\Omega_- D$ for all $n \in \mathbb{Z}$, forcing $\mathcal{S} D = \Omega_+^*\Omega_- D = D$ and zero capture probability onto $\mathscr{H}_{\mathrm{ch},2}$, contradicting $p(Q_{\mathrm{win}}) > 2/10^{28} > 0$. Thus the contact coupling $(C - I)$ never shuts off uniformly on the spectral family $\Omega_- D(L^2(I_E))$.
2. **Per-state asymptotic decay:** For each fixed state $\phi \in \mathscr{H}_{\mathrm{ac}}(U)$, $U^n\phi - U_0^n\Omega_+^*\phi \to 0$ as $n \to +\infty$ and $U^n\phi - U_0^n\Omega_-^*\phi \to 0$ as $n \to -\infty$, while $\|(C - I)U_0^n\psi\| \to 0$ as $n \to \pm\infty$ for every $\psi \in \mathscr{H}_{\mathrm{ac}}(U_0)$ by local dispersion of $U_0^n$ at the compact contact port. Hence $\lim_{n\to\pm\infty}\|(C-I)U^n\phi\| = 0$ for each fixed $\phi$, whereas the supremum over the time-translated packet family $D(L^2(I_E))$ remains constant and strictly positive for all $n \in \mathbb{Z}$.
