# Localizing a five-level QDD register with four pair interventions

**NON-CANONICAL.** This is an analytic result in a specified intervention model. The identification of an apparatus with this model is a separate physical question.

## Model and exact statement

Let the input be $\mathbb C^5$, with basis $e_0,\ldots,e_4$. The physical subsystem $P$ has corresponding orthonormal levels and may have additional levels. Write $I_P$ for the inclusion of the logical levels into $P$. An isometry $V:\mathbb C^5\to P\otimes E$ represents preparation up to the intervention, including fixed stocks and a purification of any discarded information. A single isometry $W:P\otimes E\to R\otimes F$ represents the subsequent process, with receiver $R$ and discarded output $F$. A dilation on an inaccessible reference acts trivially on that reference.

Let $L_k:\mathbb C^2\to\mathbb C^5$ include the ordered pair $0,k$, $k=1,\ldots,4$. Let $Q_k$ be the projector in $P$ onto those two levels. The intervention $G_k$ acts as $U=cI+isX$ on $Q_k$ and as identity on its complement, where $c=4/5$, $s=3/5$, and $X$ exchanges the two coordinates. In each separate trial the intervention acts only on $P$, with a common $V,W$ and a common output isometry $J:\mathbb C^5\to R$. Let $V_k=VL_k$, and let $G_k$ and $Q_k$ on $P\otimes E$ denote their tensor extensions. The idle channel is $\operatorname{Tr}_F(WV\,\cdot\, V^*W^*)$. The $k$-th channel is the reduced channel of $WG_kV_k$ on the two-dimensional input.

Suppose the idle channel equals the isometric channel of $J$ and each pair channel equals that of $JL_kU$, including relative coherences and all output levels. Then $V=I_P\otimes\eta$ for a single unit vector $\eta\in E$. This certifies the encoded state at the common intervention cut, including for inputs entangled with a passive reference.

For the proof, the normalized Choi vector of each branch, including its environment, purifies a pure ideal Choi state. Therefore $WV=J\otimes z_0$ and $WG_kV_k=JL_kU\otimes z_k$ for unit vectors $z_0,z_k$. Taking the cross Gram matrix for the two branches gives
$$
M_k=V_k^*G_kV_k=\lambda_k U,\qquad \lambda_k=\langle z_0,z_k\rangle .
$$
The real part of $G_k$ is $cI+(1-c)(I-Q_k)$. Hence
$$
2c+(1-c)\|(I-Q_k)V_k\|_{\mathrm{HS}}^2
   =\operatorname{Re}\operatorname{Tr}M_k=2c\operatorname{Re}\lambda_k .
$$
Since $0<c<1$ and $\operatorname{Re}\lambda_k\le 1$, the leakage term vanishes and $\lambda_k=1$. Consequently $z_k=z_0$, and injectivity of $W$ gives $G_kV_k=V_k U$. The input $e_0$ lies in the intersection of the four physical pairs, so $Ve_0=e_0\otimes\eta$. Applying the intertwining identity to the first pair coordinate yields $is\,Ve_k=is\,e_k\otimes\eta$ for every $k>0$, proving the statement.

## Quantitative statement

For each of the five settings, bound the half trace distance of its normalized receiver Choi state from the ideal by $t$. The input dimension is five in the idle setting and two in each pair setting. If each output matrix unit on an $n$-dimensional input has trace-norm error at most $e_n$, expanding in matrix units gives a sufficient Choi bound $ne_n/2$. The output used for the bound includes leakage and any loss flags. The hypothesis concerns the specified interventions. In an application, an independently justified pulse error must be propagated into the Choi bound for comparison with those interventions.

For $0\le t\le 1/16000$, there is a unit vector $\eta\in E$ with
$$
\|V-I_P\otimes\eta\|_{\mathrm{op}}
 \le \sqrt{14160t}+1-\sqrt{1-(2360/3)t}.
$$
Tensoring with identity on a passive reference preserves the operator norm.

### Extracting aligned Kraus components

For a branch isometry $A:\mathbb C^n\to R\otimes F$, vectorize $A$ with a normalized maximally entangled input. Let $p$ be the ideal normalized Choi vector, $\tau$ the received Choi state, and $f=\langle p,\tau p\rangle\ge 1-t$. The normalized projection of the vectorized $A$ along $p$ fixes a unit environment direction $z$. Write $A=C_z\otimes z+C_\perp$ with $C_\perp$ supported on $z^\perp$.

The off-diagonal block $(I-|p\rangle\langle p|)\tau p$ has norm at most $t$. Indeed, if the block is nonzero, the Hermitian operator exchanging $p$ with the normalized block vector has operator norm one, and its trace pairing with $\tau-|p\rangle\langle p|$ is twice the block norm. The vectorized $C_z$ has component $\sqrt f$ along $p$ and transverse norm at most $t/\sqrt f$. The squared norm of the vectorized $C_\perp$ is at most $1-f$, since the aligned component has squared norm at least $f$. If $J_A$ is the ideal isometry, then
$$
\|C_z-J_A\|_{\mathrm{op}}\le 1-\sqrt f+\sqrt n\,t/\sqrt f,\qquad
\|C_\perp\|_{\mathrm{op}}\le\sqrt{nt}.
$$
Here normalized vectorization divides the Hilbert–Schmidt norm by $\sqrt n$, and the contribution parallel to $p$ uses $\|J_A\|_{\mathrm{op}}=1$.

### Comparing idle with the pair setting

For a fixed pair, let $\lambda=\langle z_0,z_k\rangle$, $h=1-\operatorname{Re}\lambda$. Expand
$$
M_k=(WV_k)^*(WG_kV_k)
$$
using the aligned and perpendicular components. The aligned product differs from $\lambda U$ by at most the sum of the aligned component errors, since the aligned components and both ideal isometries are contractions. Each aligned-perpendicular cross term carries at most $\sqrt{1-|\lambda|^2}\le\sqrt{2h}$ by orthogonality to its own environment direction. The perpendicular-perpendicular term is at most $\sqrt{10}\,t$. For $t\le 1/4$, the estimates for $n=5,2$, with $\sqrt5+\sqrt2<4$, therefore give
$$
\|M_k-\lambda U\|_{\mathrm{op}}\le 10t+4\sqrt{2th}.
$$
In particular the coefficient $10$ bounds $2+4/\sqrt{3/4}+\sqrt{10}$.

Put $\ell_k=\|(I-Q_k)V_k\|_{\mathrm{HS}}^2$. The exact real trace identity gives
$$
ch+(1-c)\ell_k/2 \le 10t+4\sqrt{2th}.
$$
The inequality $4\sqrt{2th}\le (2/5)h+20t$ gives $h\le75t$. Since $10+4\sqrt{150}<59$, set $a=59t$ to obtain $\|M_k-\lambda U\|_{\mathrm{op}}\le a$, $\ell_k\le10a$, and $ch\le a$. For $D_k=G_kV_k-V_kU$ this implies
$$
\|D_k\|_{\mathrm{HS}}^2=4-2\operatorname{Re}\operatorname{Tr}(U^*M_k)
   \le 4h+4a\le 9a.
$$

### Recovering the common environment

Write $v_{rj}=(\langle e_r|\otimes I_E)Ve_j$ in a physical basis extending the logical levels, and set
$$
v=v_{00},\quad A_0=\sum_{r\ne 0}\|v_{r0}\|^2,\quad
B=\sum_{k>0,\ r\notin\{0,k\}}\|v_{rk}\|^2 .
$$
Each wrong logical row of column zero counts in three leakage sums. Each extra row counts in all four. Therefore $3A_0+B\le 40a$. The rows $k$ and $0$ of the first column of $D_k$ are $is(v-v_{kk})$ and $is(v_{k0}-v_{0k})$, respectively. Thus
$$
\sum_{k>0}(\|v_{kk}-v\|^2+\|v_{0k}\|^2)
   \le 2A_0+(2/s^2)\sum_k\|D_k\|_{\mathrm{HS}}^2
   \le 2A_0+200a.
$$
Adding $A_0+B$ bounds the squared Hilbert–Schmidt error of $V-I_P\otimes v$ by $240a$. Since $\|v\|^2=1-A_0\ge1-40a/3>0$ in the stated range, the operator-norm cost of replacing $v$ by $\eta=v/\|v\|$ is at most $1-\sqrt{1-40a/3}$. This gives the stated bound.

## Real rotations, minimality, and checks of applicability

The real pair rotation with columns $(c,s)^{\mathsf T}$ and $(-s,c)^{\mathsf T}$ is $D^*G_kD$ on the pair, where $D=\operatorname{diag}(1,i,i,i,i)$ on the logical levels and identity on the extra levels. Use $V'=(D\otimes I_E)VD^*$ and $W'=(D_R\otimes I_F)W(D^*\otimes I_E)$, where $D_R J=JD$ and $D_R$ fixes the orthogonal complement of the range of $J$. Here each occurrence of $D$ acts on its indicated space. These coordinate changes convert the real comparison to the complex one and preserve the Choi distances and final norm.

Four distinct pair interventions are necessary among single-coordinate-pair interventions in this model, even with full tomography and idle. Any collection of at most three edges on five vertices has a disconnected pair graph. Encode $Ve_j=e_j\otimes f_{C(j)}$, where $C(j)$ is the connected component of $j$ and the component flags $f_C$ are orthonormal. A fixed controlled operation in $W$ clears the flag on each populated branch. Every permitted pair unitary and idle commute with the component-controlled encoding, so the received channels agree exactly with their ideals. Before clearing, $E$ retains a component record and the common-vector conclusion fails. This bound allows arbitrary unitaries within each selected pair and repeated interventions.

For a proposed apparatus, independent checks must establish physical addressing, the signed action in a shared coordinate frame, and the common preparation and receiver process. A pulse choice reaching the decoder through a separate channel, or uncontrolled storage motion during the intervention, takes the apparatus outside the stated model. Channel comparisons can reject the exact premises by detecting a nonzero Choi discrepancy and can reject a claimed tolerance by establishing a discrepancy above it. Point populations alone do not test relative phases. The theorem leaves the physical site identification, carrier history outside the cut, and hardware performance open.
