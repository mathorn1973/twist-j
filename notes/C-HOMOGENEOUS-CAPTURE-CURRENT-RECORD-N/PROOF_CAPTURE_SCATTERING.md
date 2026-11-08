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
  $$\frac{1}{2}\operatorname{tr} V(k) = \frac{1 - 4\cos k}{5} = \cos\varepsilon(k), \qquad \varepsilon(k) := \arccos\Bigl(\frac{1-4\cos k}{5}\Bigr) \in [0, a],$$
  where $a := 2\arctan 2 = \arccos(-3/5) < 3\pi/4$ (attaining $\varepsilon(\pm\pi) = 0$ and $\varepsilon(0) = a$, so $\varepsilon(\mathbb{T}) = [0, a]$). With the cut spectral logarithm $\operatorname{Log}_\pi(e^{-i\theta}) = -i\theta$ for $\theta \in (-\pi, \pi)$ (`homogeneous_source.md` (10)–(12)), the free pulse energy generator $H_E := \beta I + i\operatorname{Log}_\pi V$ ($\widetilde{V} = e^{-iH_E}$) has branches $\beta \pm \varepsilon(k)$ and exact spectrum $\sigma(H_E) = [\beta - a, \beta + a]$. For $k \in (-\pi, 0)$, the branch with eigenvalue $e^{-i\varepsilon(k)}$ of $V(k)$ (total pulse phase $e^{-i(\beta+\varepsilon(k))}$ of $\widetilde{V}(k)$) has positive group velocity
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
3. Define the fiberwise channel spaces (`homogeneous_source.md` (18))
   $$\mathscr{H}_{\mathrm{ch},0} := \int_{[-\pi,\pi)}^{\oplus} \mathscr{H}_{\mathrm{ac}}(U_0(K))\,\frac{dK}{2\pi}, \qquad \mathscr{H}_{\mathrm{ch}} := \int_{[-\pi,\pi)}^{\oplus} \mathscr{H}_{\mathrm{ac}}(U(K))\,\frac{dK}{2\pi},$$
   and let $P_{\mathrm{ch},0} = \int_{[-\pi,\pi)}^\oplus P_{\mathrm{ac}}(U_0(K))\,\frac{dK}{2\pi}$ and $P_{\mathrm{ch}} = \int_{[-\pi,\pi)}^\oplus P_{\mathrm{ac}}(U(K))\,\frac{dK}{2\pi}$ be the corresponding orthogonal projections (we work on $\mathscr{H}_{\mathrm{ch},0}$ and $\mathscr{H}_{\mathrm{ch}}$ directly and do not identify them with the global spaces $\mathscr{H}_{\mathrm{ac}}(U_0)$ or $\mathscr{H}_{\mathrm{ac}}(U)$). Because $U(K)$ and $U_0(K)$ depend analytically on $K \in [-\pi, \pi)$ and $\|\Omega_\pm(K)\| \le 1$, the direct-integral wave operators and scattering operator
   $$\Omega_\pm := \int_{[-\pi,\pi)}^{\oplus} \Omega_\pm(K)\,\frac{dK}{2\pi} = \operatorname*{s-lim}_{n\to\pm\infty} U^{-n} U_0^n P_{\mathrm{ch},0}, \qquad \mathcal{S} := \Omega_+^*\Omega_- = \int_{[-\pi,\pi)}^\oplus \mathcal{S}(K)\,\frac{dK}{2\pi}$$
   exist by dominated convergence of the bounded fiber norms, are partially isometric with initial space $\mathscr{H}_{\mathrm{ch},0}$ and final space $\mathscr{H}_{\mathrm{ch}}$, and satisfy $U\Omega_\pm = \Omega_\pm U_0$.

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
   We relate our conventions $U(K) = U_0(K)(I + J K_C J^*)$, $\Omega_\pm(K) = \operatorname{s-lim}_{n\to\pm\infty} U(K)^{-n}U_0(K)^n P_{\mathrm{ac}}(U_0(K))$, and $E$-spectral variable $U_0(K) = \int e^{-iE}\,dE_0(K, E)$ to the unitary stationary scattering formula of R. Tiedra de Aldecoa, *Stationary scattering theory for unitary operators with an application to quantum walks*, J. Funct. Anal. 279 (2020) 108704 (`arXiv:1912.04960v2`), Example 3.8 and Theorem 4.3 (`homogeneous_source.md` (31)–(36)). In Tiedra de Aldecoa's notation, $U = U_0(I + K)$ is written in multiplicative form with $K = J K_C J^*$, his wave operators $W_\pm(U, U_0) = \operatorname{s-lim}_{n\to\pm\infty} U^n U_0^{-n} P_{\mathrm{ac}}(U_0)$ correspond to our $\Omega_\mp(K)$ (reversing incoming/outgoing labels and replacing the scattering operator by its adjoint, which preserves transition probabilities $|S_{21}|^2 = |(S^*)_{12}|^2$), and our spectral parameter $e^{-iE}$ is the conjugate of $e^{i\theta}$: for $\zeta = r e^{-iE}$ ($r > 1$), $(U_0(K) - \zeta)^{-1}U_0(K) = -R_0(K, \zeta)U_0(K)$, so Tiedra de Aldecoa's port compression $J^*(U_0 - \zeta)^{-1}U_0 J = -m(K, \zeta)$ gives $I_2 + K_C(-m(K, \zeta)) = I_2 - K_Cm(K, \zeta)$; this and the push-through identity $(I_2-K_Cm)^{-1}K_C=K_C(I_2-mK_C)^{-1}$ give the identical transition matrix $T(K, \zeta) = K_C(I_2 - m(K, \zeta)K_C)^{-1}$. With $d\mu_{j,\mathrm{ac}}=\rho_j\,dE=\widehat\rho_j\,dE/(2\pi)$, the normalized-measure density is $\widehat\rho_j=2\pi\rho_j$; the stationary off-diagonal scattering matrix element between normalized boundary fibers carries the factor $2\pi\sqrt{\rho_{1,\mathrm{in}}(E)}\,T_{21}(K, E)\,\sqrt{\rho_{2,b,+}(K, E)}$. Taking the modulus squared yields the exact transition kernel at $(K, E)$ from the incoming token channel with density $\rho_{1,\mathrm{in}}(E)$ to the outgoing bound-pair + right-moving pulse channel with density $\rho_{2,b,+}(K, E)$:
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
Since $z = e^{-ig}$, setting $\widetilde{K} := e^{-ig/2}K$ yields $\widetilde{K}^* = e^{ig/2}K^* = e^{ig/2}e^{-ig}K = e^{-ig/2}K = \widetilde{K}$, so $\widetilde{K}$ is Hermitian. By Fourier transform $r \leftrightarrow q \in [0, 2\pi)$ on $\mathcal{H}_\perp = \ell^2(\mathbb{Z}_r) \otimes \operatorname{span}(S_{\mathrm{coin}}, T_{\mathrm{coin}}, B)$ (`canon/CANON.md`, `CONTACT-W-BOUND-PAIR-RESPONSE [T]`, equations (1)–(6)), the free walk symbol is
$$F_b(q) = \begin{pmatrix} d & ic & 0 \\ ic\cos q & d\cos q & i\sin q \\ -c\sin q & i d\sin q & \cos q \end{pmatrix}, \qquad d = -\frac{3}{5}, \quad c = \frac{4}{5}, \quad b_{\mathrm{can}} := 1 - d = \frac{8}{5}, \quad \ell := 1 + d = \frac{2}{5},$$
with characteristic polynomial $\det(\lambda I_3 - F_b(q)) = (\lambda - 1)\bigl(\lambda^2 + b_{\mathrm{can}}\lambda + 1 - \ell\lambda\cos q\bigr)$. At $\lambda = z = e^{-ig}$ ($\cos g = \frac{\sqrt{5}-1}{4}$), define the denominator polynomial
$$D(q) := z^2 + b_{\mathrm{can}} z + 1 - z\ell\cos q = z\bigl(2\cos g + b_{\mathrm{can}} - \ell\cos q\bigr).$$
Because $2\cos g + b_{\mathrm{can}} = \frac{\sqrt{5}-1}{2} + \frac{8}{5} > \frac{2}{5} = \ell > 0$, the real factor $2\cos g + b_{\mathrm{can}} - \ell\cos q \ge 2(\cos g - d) > 0$ never vanishes for $q \in [0, 2\pi)$. Evaluating the standard Poisson/residue integral on the unit circle gives the exact Canon resolvent integral (`CANON.md` (3)):
$$I_0 := \int_0^{2\pi} \frac{dq}{2\pi\,D(q)} = \frac{1}{2z\sqrt{(\cos g - d)(\cos g + 1)}}.$$
Since $(z + 1)^2 = z(2\cos g + 2) = 2z(\cos g + 1)$, this satisfies the exact identity
$$(z + 1)^2 I_0 = \sqrt{\frac{\cos g + 1}{\cos g - d}} = \frac{1}{s}, \qquad s = \sqrt{\frac{\cos g - d}{\cos g + 1}} = \sqrt{\frac{2\sqrt{5}-1}{5}} \in (0, 1).$$
In the basis $(S_{\mathrm{coin}}, T_{\mathrm{coin}}, B)$, the odd-in-$q$ entries $\sin q / D(q)$ integrate to zero, so $G_0 = \int_0^{2\pi} (z I_3 - F_b(q))^{-1}\,\frac{dq}{2\pi} = (G_0)_{ST} \oplus (G_0)_{BB}$ is block-diagonal. Using $\cos q\,D(q)^{-1} = \ell^{-1}z^{-1}\bigl[(z^2 + b_{\mathrm{can}}z + 1)D(q)^{-1} - 1\bigr]$ and $\sin^2 q = 1 - \cos^2 q$, the $2\times 2$ $(S_{\mathrm{coin}}, T_{\mathrm{coin}})$ block and $1\times 1$ $B$ block of $(z - 1)G_0$ are (`CANON.md` (4)):
$$(z - 1)(G_0)_{ST} = \begin{pmatrix} 1 - b_{\mathrm{can}}(z+1)I_0 & i c x \\ i c y & (z - d)x \end{pmatrix}, \qquad x := \frac{1 + (z+1)(d z - 1)I_0}{z\ell}, \quad y := \frac{(z+1)(z - d)I_0 - 1}{\ell},$$
and $(z - 1)(G_0)_{BB} = 1 - \frac{(z+1)(1-s)}{z\ell}$. Forming $K = I_3 - (z - 1)G_0 = K_{ST} \oplus K_{BB}$ and substituting $(z+1)^2 I_0 = 1/s$ and $c^2 = 1 - d^2 = b_{\mathrm{can}}\ell$ yields (`CANON.md` (5)):
$$K_{BB} = \frac{(z+1)(1-s)}{z\ell}, \qquad (K_{ST})_{11} = b_{\mathrm{can}}(z+1)I_0 = \frac{b_{\mathrm{can}}}{s(z+1)}, \qquad \det K_{ST} = \frac{b_{\mathrm{can}}(1-s)}{z\ell s}.$$
Multiplying by $e^{-ig/2}$ (where $z = e^{-ig}$ and $e^{-ig/2}(z+1)/z = e^{ig/2} + e^{-ig/2} = 2\cos(g/2) = 2c_0$) gives the exact entries of $\widetilde{K} = e^{-ig/2}K$:
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
Let $W(P) = \Gamma S_P M_\mu$ on $\ell^2(\mathbb{Z}_r, \mathbb{C}^4)$ with $\mu = 2$, $N = 1 + \mu^2 = 5$, $z = e^{-ig} = e^{-i 2\pi/5}$, Fourier variable $w := e^{iP}$ ($P \in [-\pi, \pi)$), and eigenvalue parameter $\lambda = e^{i\theta} \in \mathbb{T}$ (`finite_strip_complete.md` §§2–3, equations (2)–(15)). Define the unit-circle root
$$u_* := z\,\frac{Nz - 1}{N - z} \in \mathbb{T} \qquad \Bigl(|u_*| = 1 \text{ since } |Nz - 1| = |N - \bar{z}| = |N - z| \ne 0\Bigr),$$
and the finite exceptional momentum set
$$\mathcal{E}_{\mu,z} := \{0, \pi\} \cup \bigl\{P \in [-\pi, \pi) : e^{2iP} \in \{z, u_*, \bar{z}, \bar{u}_*\}\bigr\},$$
which contains at most $10$ points ($|\mathcal{E}_{\mu,z}| \le 10$) and therefore has Lebesgue measure zero.
1. **Stationary-channel elimination ($r \ne 0$) and the case $D = 0$:** On any site $r \ne 0$, the eigenvalue equation $S_P M_\mu \psi(r) = \lambda \psi(r)$ relates the stationary channels $(a_r, d_r) = (\psi_1(r), \psi_4(r))$ to the moving channels $(b_r, c_r) = (\psi_2(r), \psi_3(r))$ via the $2\times 2$ system (`finite_strip_complete.md` (2)–(3))
   $$\begin{pmatrix} N\lambda w^{-1} - 1 & \mu^2 \\ \mu^2 & N\lambda w - 1 \end{pmatrix}\binom{a_r}{d_r} = i\mu(b_r + c_r)\binom{1}{1},$$
   whose determinant is $N \cdot D(\lambda, w)$ with $D(\lambda, w) := N\lambda^2 - \lambda(w + w^{-1}) + 1 - \mu^2$. For $\lambda = e^{i\theta}$ and $w = e^{iP}$ on the unit circle,
   $$\frac{D(\lambda, w)}{\lambda} = N\lambda - (w + w^{-1}) + (1 - \mu^2)\lambda^{-1} = 2(\cos\theta - \cos P) + 2i\mu^2\sin\theta.$$
   Because $\mu > 0$, $\operatorname{Im}(D/\lambda) = 0 \implies \sin\theta = 0 \implies \lambda = \pm 1$, and then $\operatorname{Re}(D/\lambda) = 0 \implies \cos P = \pm 1$, so $D(\lambda, w) = 0$ on $\mathbb{T}^2$ occurs **only** at $(\lambda, P) = (1, 0)$ or $(-1, \pi)$, both of which have $P \in \{0, \pi\} \subset \mathcal{E}_{\mu,z}$ (indeed at $P = 0$, $\delta_r A$ for $r \ne 0$ are compactly supported eigenvectors of $W(0)$ with $\lambda = 1$).
   For all $P \notin \{0, \pi\}$, $D(\lambda, w) \ne 0$, and substituting $(a_r, d_r)$ into the moving rows at $r \ne 0$ gives (`finite_strip_complete.md` (4)–(6))
   $$\binom{(M_\mu\psi)_2(r)}{(M_\mu\psi)_3(r)} = \frac{1}{D(\lambda,w)}\begin{pmatrix} p(\lambda,w) & q(\lambda) \\ q(\lambda) & p(\lambda,w) \end{pmatrix}\binom{b_r}{c_r}, \qquad p(\lambda,w) := (\lambda-w)(\lambda-w^{-1}),\quad q(\lambda) := \mu^2(1-\lambda^2),$$
   with the exact polynomial identity $p(\lambda,w) - q(\lambda) = D(\lambda,w)$.
2. **Case $P \notin \{0, \pi\}$ and $p(\lambda, w) \ne 0$:** Suppose $\chi$ is a nonzero compactly supported eigenvector of $W(P)$ with $P \notin \{0, \pi\}$ and $p(\lambda, w) \ne 0$. If $\operatorname{supp}\chi$ contains a maximal positive site $n > 0$, then $b_n = \lambda^{-1}(M_\mu\chi)_{2}(n+1) = 0$ and $(M_\mu\chi)_{3}(n) = \lambda c_{n+1} = 0$. The second row of the reduced moving system at $r = n \ne 0$ gives
   $$0 = (M_\mu\chi)_3(n) = \frac{q(\lambda)}{D(\lambda,w)}b_n + \frac{p(\lambda,w)}{D(\lambda,w)}c_n = \frac{p(\lambda,w)}{D(\lambda,w)}c_n \implies c_n = 0,$$
   and invertible elimination forces $a_n = d_n = 0$, contradicting $\chi(n) \ne 0$. Symmetric downward peeling from a minimal site $m < 0$ using $c_m = 0$ and $(M_\mu\chi)_2(m) = \frac{p}{D}b_m = 0$ eliminates $m < 0$. Finally, if $\operatorname{supp}\chi \subseteq \{0\}$, then $b_0 = c_0 = 0$ and $(M_\mu\chi)_2(0) = (M_\mu\chi)_3(0) = \frac{i\mu}{N}(a_0 + d_0) = 0 \implies d_0 = -a_0$, and the stationary equations at $r = 0$ read $z w(a_0 - \mu^2 d_0)/N = z w a_0 = \lambda a_0$ and $z w^{-1} d_0 = \lambda d_0 \implies w = w^{-1} \implies P \in \{0, \pi\}$, a contradiction.
3. **Case $P \notin \{0, \pi\}$ and $p(\lambda, w) = 0$:** Since $p(\lambda, w) = (\lambda - w)(\lambda - w^{-1}) = 0$ and $P \notin \{0, \pi\}$, we have $\lambda \in \{w, w^{-1}\}$ with $\lambda^2 \ne 1$, so $D(\lambda, w) = -q(\lambda) = -\mu^2(1 - \lambda^2) \ne 0$ and $q/D = -1$. On every exterior site $r \ne 0$, $(M_\mu\chi)_2(r) = -c_r$ and $(M_\mu\chi)_3(r) = -b_r$. Across any exterior bond $(r, r+1)$ with $r \ge 1$ or $r \le -2$, $\lambda b_r = (M_\mu\chi)_2(r+1) = -c_{r+1}$ and $\lambda c_{r+1} = (M_\mu\chi)_3(r) = -b_r$, whence $(\lambda^2 - 1)b_r = 0 \implies b_r = c_{r+1} = 0$. Thus $b_r = c_r = a_r = d_r = 0$ for all $|r| \ge 2$, and at $r = \pm 1$ only $c_1$ and $b_{-1}$ can be nonzero, determined by $r = 0$ via (`finite_strip_complete.md` (8)–(12))
   $$z M_\mu \chi(0) = T_{\lambda, w}\chi(0), \qquad T_{\lambda, w} := \begin{pmatrix} \lambda w^{-1} & 0 & 0 & 0 \\ 0 & 0 & -\lambda^2 & 0 \\ 0 & -\lambda^2 & 0 & 0 \\ 0 & 0 & 0 & \lambda w \end{pmatrix}.$$
   For $\lambda = w$ (setting $u := w^2 = e^{2iP}$) or $\lambda = w^{-1}$ (setting $u := w^{-2} = e^{-2iP}$), $T_{\lambda, w}$ is $T_+(u) = \begin{pmatrix}1&0&0&0\\0&0&-u&0\\0&-u&0&0\\0&0&0&u\end{pmatrix}$ or $T_-(u) = \begin{pmatrix}u&0&0&0\\0&0&-u&0\\0&-u&0&0\\0&0&0&1\end{pmatrix}$. Direct expansion over $\mathbb{Z}[i]$ (certified symbolically in all 16 Laurent polynomial identity groups of Group 6 in `verify.py`, `finite_strip_complete.md` (13)–(15)) gives the exact determinant factorization
   $$p_+(u) = p_-(u) := \det\bigl(z M_\mu - T_\pm(u)\bigr) = \frac{(z - u)^2}{N}\bigl[z(Nz - 1) - (N - z)u\bigr].$$
   Hence a nonzero solution on $r \in \{-1, 0, 1\}$ exists only if $u \in \{z, u_*\}$, i.e., $e^{2iP} \in \{z, u_*, \bar{z}, \bar{u}_*\}$, which places $P \in \mathcal{E}_{\mu,z}$. Thus for every $P \notin \mathcal{E}_{\mu,z}$, $W(P)$ has **no** nonzero compactly supported eigenvector.
4. **No nonzero $W$-invariant subspace in $\operatorname{Ran} P_B$:** For any $P \notin \mathcal{E}_{\mu,z}$, the finite-dimensional subspace $\bigcap_{n\in\mathbb{Z}} W(P)^{-n}\operatorname{Ran} P_B \subset \ell^2(\mathbb{Z}_r, \mathbb{C}^4)$ is $W(P)$-invariant; if it were nonzero, it would contain a compactly supported eigenvector of $W(P)$, contradicting (2)–(3). Hence $\bigcap_{n\in\mathbb{Z}} W(P)^{-n}\operatorname{Ran} P_B = \{0\}$ for all $P \notin \mathcal{E}_{\mu,z}$. Since $\mathcal{E}_{\mu,z}$ is finite (measure zero) and $W = \int_{[-\pi,\pi)}^\oplus W(P)\,\frac{dP}{2\pi}$, any $\psi \in \bigcap_{n\in\mathbb{Z}} W^{-n}\operatorname{Ran} P_B$ has $\psi(P) \in \bigcap_{n\in\mathbb{Z}} W(P)^{-n}\operatorname{Ran} P_B = \{0\}$ for a.e. $P$, so
   $$\bigcap_{n\in\mathbb{Z}} W^{-n}\operatorname{Ran} P_B = \{0\}.$$
5. **Corollary 5.2 (No Non-Identity Translation-Invariant Finite-Strip Contact Commuting with $W \otimes V$).** If a bounded operator $C$ on $\mathcal{H}_{\mathrm{obj}} \otimes \mathcal{H}_{\mathrm{pulse}}$ satisfies $[C, W \otimes V] = 0$ and $(P_B \otimes I)(C - I) = C - I$, then for every $n \in \mathbb{Z}$, $(W^{-n}P_B W^n \otimes I)(C - I) = (W \otimes V)^{-n}(P_B \otimes I)(C - I)(W \otimes V)^n = C - I$, so $\operatorname{Ran}(C - I) \subset \bigl(\bigcap_{n\in\mathbb{Z}} W^{-n}\operatorname{Ran} P_B\bigr) \otimes \mathcal{H}_{\mathrm{pulse}} = \{0\}$, forcing $C = I$.

### 5.2 One-Carrier Safe-Window Theorem vs. Two-Pulse Alias Obstruction

We keep strictly distinct the one-carrier safe-window spectral-energy theorem and the two-pulse periodic-window alias obstruction (`homogeneous_source.md` §3, `finite_strip_complete.md` §6 (19)–(26)). Fix the exact constants
$$\alpha := \frac{3\pi}{10}, \qquad \beta := \frac{4\pi}{5}, \qquad a := 2\arctan 2 = \arccos\Bigl(-\frac{3}{5}\Bigr) < \frac{3\pi}{4}, \qquad b := \pi - a = 2\arctan\Bigl(\frac{1}{2}\Bigr) = \arccos\Bigl(\frac{3}{5}\Bigr),$$
which satisfy $0 < b < \alpha < \pi/2 < a < 3\pi/4 < \beta < \pi$.

**Proposition 5.3 (One-Carrier Safe-Window Intertwining Theorem).**
On the one-carrier reference space $\mathscr{H}_1 \oplus \mathscr{H}_2$, define $H_W := i\operatorname{Log}_\alpha W$ ($\sigma(H_W) \subset [-\alpha, 2\pi - \alpha]$ since $e^{i\alpha}$ lies in the canonical spectral gap of $W$) and $H_E := \beta I + i\operatorname{Log}_\pi V$ ($\sigma(H_E) = [\beta - a, \beta + a]$ since $\varepsilon(\mathbb{T}) = [0, a]$). The additive channel reference energy generator $H_0 := H_{0,1} \oplus H_{0,2}$ ($U_0 = e^{-iH_0}$) has components (`homogeneous_source.md` (12)–(16)):
$$H_{0,1} := (H_W + \beta I) \otimes I_{\mathrm{tok}}, \qquad H_{0,2} := H_W \otimes I_{\mathrm{pulse}} + I_{\mathrm{obj}} \otimes H_E.$$
1. Since $\beta - \alpha = \pi/2$ and $2\pi - \alpha + \beta = 5\pi/2$, the spectra satisfy
   $$\sigma(H_{0,1}) \subset \Bigl[\frac{\pi}{2}, \frac{5\pi}{2}\Bigr], \qquad \sigma(H_{0,2}) \subset \Bigl[\frac{\pi}{2} - a, \frac{5\pi}{2} + a\Bigr] \implies \sigma(H_0) \subset \Bigl[\frac{\pi}{2} - a, \frac{5\pi}{2} + a\Bigr].$$
   Because $a < 3\pi/4$, we have $\pi/2 + a < 5\pi/4$ and $5\pi/2 - a > 7\pi/4$. Thus the open safe window
   $$J_{\mathrm{safe}} := \Bigl(\frac{5\pi}{4}, \frac{7\pi}{4}\Bigr) \subset \Bigl(\frac{\pi}{2} + a, \frac{5\pi}{2} - a\Bigr)$$
   satisfies $(J_{\mathrm{safe}} + 2\pi m) \cap \sigma(H_0) = \varnothing$ for every nonzero integer $m \in \mathbb{Z}\setminus\{0\}$ (`verify.py` Group 2).
2. Consequently, on $P_J := \mathbf{1}_{J_{\mathrm{safe}}}(H_0)P_{\mathrm{ch},0}$ (and in particular on the closed safe window $J_0 = [3\pi/2, 17\pi/10] \subset J_{\mathrm{safe}}$ containing our packet window $I_E = [8\pi/5 - 1/1000, 8\pi/5 + 1/1000]$), any $2\pi$-periodic Borel function $\widetilde{f}$ agreeing with a Borel function $f$ on $J_{\mathrm{safe}}$ satisfies $\widetilde{f}(H_0)P_J = f(H_0)P_J$, so $\mathcal{S} f(H_0) P_J = f(H_0) \mathcal{S} P_J$, $\Omega_\pm f(H_0) P_J = U^{\pm}_{\mathrm{eff}}(f)\Omega_\pm P_J$, and the receiver-conjugated scattering operator $\mathcal{S}_{\mathrm{rec}}$ commutes with $H_0 \otimes I_{\mathrm{rec}}$ on $\operatorname{Ran}(P_J \otimes I_{\mathrm{rec}})$.

**Proposition 5.4 (Two-Pulse Periodic-Window Alias Obstruction).**
On the two-pulse reference sector $\mathcal{H}_{\mathrm{obj}} \otimes \mathcal{H}_{\mathrm{pulse}} \otimes \mathcal{H}_{\mathrm{pulse}}$ with additive generator $H^{(2)} = H_W \otimes I \otimes I + I \otimes H_E \otimes I + I \otimes I \otimes H_E$ ($U_0^{(2)} = e^{-iH^{(2)}}$, `finite_strip_complete.md` §6 (19)–(26)):
1. **Exterior Weyl sequences for $H_W$:** Truncating plane waves of the free walk $S M_2$ to the exterior shell $2L \le |r| \le 3L$ (where $\Gamma = I$ since $r \ne 0$) yields Weyl sequences at quasi-energies $\theta_\pm(P, q) \in [-b, b] \cup [a, \pi + b]$, proving the spectral inclusion
   $$[-b, b] \cup [a, \pi + b] \subseteq \sigma(H_W) \subseteq [-\alpha, 2\pi - \alpha].$$
2. **Contiguous inner interval $J_*$ of length $> 4\pi$:** Since $H_W$ and the two copies of $H_E$ act on independent tensor factors and $\sigma(H_E) = [\beta - a, \beta + a]$, the Minkowski sum $\sigma(H^{(2)}) = \sigma(H_W) + \sigma(H_E) + \sigma(H_E)$ contains
   $$\bigl([-b, b] \cup [a, \pi + b]\bigr) + [2\beta - 2a, 2\beta + 2a] = [2\beta - 2a - b, 2\beta + 2a + b] \cup [2\beta - a, 2\beta + 2a + \pi + b].$$
   Because $2\beta - a \le 2\beta + 2a + b$ (as $3a + b > 0$), these two intervals overlap and form the single contiguous interval (`finite_strip_complete.md` (24)–(25))
   $$J_* := [L_*, U_*] := [2\beta - 2a - b,\; 2\beta + 2a + \pi + b] \subseteq \sigma(H^{(2)}),$$
   whose length is $|J_*| = 4a + \pi + 2b = 3\pi + 2a > 4\pi$ (since $a + b = \pi$ and $a = 2\arctan 2 > \pi/2$).
3. **Complete outer enclosure and aliases for all $E \in \sigma(H^{(2)})$:** From $\sigma(H_W) \subseteq [-\alpha, 2\pi - \alpha]$, the entire spectrum is enclosed in
   $$\sigma(H^{(2)}) \subseteq [L_o, U_o] := [2\beta - 2a - \alpha,\; 2\beta + 2a + 2\pi - \alpha].$$
   The two outer strips $[L_o, L_*)$ and $(U_*, U_o]$ have widths $L_* - L_o = \alpha - b \in (0, 2\pi)$ and $U_o - U_* = \pi - \alpha - b = a - \alpha \in (0, 2\pi)$:
   - For every $E \in J_*$, since $|J_*| = 3\pi + 2a > 4\pi$, at least one of $E \pm 2\pi$ lies in $J_* \subseteq \sigma(H^{(2)})$.
   - For every $E \in [L_o, L_*)$, $E + 2\pi \in [L_o + 2\pi, L_* + 2\pi) \subset [L_*, U_*] = J_* \subseteq \sigma(H^{(2)})$ (since $L_o + 2\pi - L_* = 2\pi - (\alpha - b) > 0$ and $U_* - (L_* + 2\pi) = |J_*| - 2\pi = \pi + 2a > 0$).
   - For every $E \in (U_*, U_o]$, $E - 2\pi \in (U_* - 2\pi, U_o - 2\pi] \subset [L_*, U_*] = J_* \subseteq \sigma(H^{(2)})$ (since $(U_* - 2\pi) - L_* = |J_*| - 2\pi > 0$ and $U_* - (U_o - 2\pi) = 2\pi - (a - \alpha) > 0$).
   Hence **every** point $E \in \sigma(H^{(2)})$ has at least one $2\pi$-alias in $\sigma(H^{(2)})$ (`finite_strip_complete.md` (26)):
   $$\forall E \in \sigma(H^{(2)}), \qquad \{E - 2\pi, E + 2\pi\} \cap \sigma(H^{(2)}) \ne \varnothing.$$
   Therefore, no periodic spectral window of $U_0^{(2)}$ is alias-free on the two-pulse sector; in the present one-carrier package, outgoing binding is selected explicitly by the bound-branch projector $\Pi_b(P)$ in $Q_{\mathrm{full}}$ and $Q_{\mathrm{win}}$, not inferred from pulse energy or receiver memory $|d_1\rangle$ alone.

### 5.3 No-Uniform-Shutoff Identity

**Proposition 5.5 (No Uniform Finite-Time Shutoff on the Incoming Packet Family vs. Per-State Dispersion).**
Let $D: L^2(I_E) \to \mathscr{H}_{\mathrm{ch},0}$ be the isometric incoming packet family $D f := \mathcal{F}_{P,E}^{-1}\bigl(f(E)\xi_{\mathrm{in}}(P, E)\bigr) \otimes |y=0, t_1\rangle$, where $\psi_{\mathrm{in}} = D(\ell_E^{-1/2}\mathbf{1}_{I_E})$.
1. **Uniform operator norm over the translated packet family:** For every $n \in \mathbb{Z}$ and every $f \in L^2(I_E)$, the intertwining identity $U\Omega_- = \Omega_- U_0$ gives $U^n \Omega_- D f = \Omega_- U_0^n D f = \Omega_- D(e^{-inE}f)$. Since multiplication by $e^{-inE}$ is a unitary bijection of $L^2(I_E)$ onto itself,
   $$\sup_{\|f\|_{L^2(I_E)} = 1} \bigl\|(C - I) U^n \Omega_- D f\bigr\| = \sup_{\|g\|_{L^2(I_E)} = 1} \bigl\|(C - I)\Omega_- D g\bigr\| = \bigl\|(C - I)\Omega_- D\bigr\| > 0 \qquad (\forall n \in \mathbb{Z}),$$
   where $\|(C-I)\Omega_- D\| > 0$ because if $(C-I)\Omega_- D = 0$, then $U^n\Omega_- D = U_0^n\Omega_- D$ for all $n \in \mathbb{Z}$, forcing $\mathcal{S} D = \Omega_+^*\Omega_- D = D$ and zero capture probability onto $\mathscr{H}_2$, contradicting $p(Q_{\mathrm{win}}) > 2/10^{28} > 0$. Thus the contact coupling $(C - I)$ never shuts off uniformly on the spectral family $\Omega_- D(L^2(I_E))$.
2. **Per-state asymptotic decay on $\mathscr{H}_{\mathrm{ch}}$ (`homogeneous_source.md` §12 (55)):** For each fixed state $\phi \in \mathscr{H}_{\mathrm{ch}}$, write $\psi_\pm := \Omega_\pm^*\phi \in \mathscr{H}_{\mathrm{ch},0}$, so $\|U^n\phi - U_0^n\psi_\pm\| \to 0$ as $n \to \pm\infty$. On each fiber $K \in [-\pi, \pi)$, $\psi_\pm(K) \in \mathscr{H}_{\mathrm{ac}}(U_0(K))$, so by the Riemann-Lebesgue lemma for absolutely continuous spectral measures, $U_0(K)^n\psi_\pm(K) \rightharpoonup 0$ weakly as $n \to \pm\infty$. Because $C(K) - I$ has finite rank ($\le 52$) on each fiber $K$, it is compact and converts weak convergence into norm convergence: $\lim_{n\to\pm\infty}\|(C(K) - I)U_0(K)^n\psi_\pm(K)\| = 0$ for a.e. $K$. Since $\|(C(K) - I)U_0(K)^n\psi_\pm(K)\|^2 \le 4\|\psi_\pm(K)\|^2 \in L^1(\mathbb{T})$, dominated convergence gives $\lim_{n\to\pm\infty}\|(C - I)U_0^n\psi_\pm\| = 0$, and therefore
   $$\lim_{n\to\pm\infty}\bigl\|(C - I)U^n\phi\bigr\| = 0 \qquad (\forall \phi \in \mathscr{H}_{\mathrm{ch}}),$$
   whereas the supremum over the time-translated packet family $\Omega_- D(L^2(I_E))$ remains constant and strictly positive for all $n \in \mathbb{Z}$.
