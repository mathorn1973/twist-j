# Mixing and reconstruction for signed augmentation

**NON-CANONICAL. Authority none.** The deductions in this note are
**candidate-D**. The arithmetic estimate marked **O** is open here. The
setting is the actual rapidity span of [MOBIUS.md](MOBIUS.md) on the Public
Canon v117 basis of this candidate. The action layer is NOT_APPLICABLE.
The arguments are paper deductions. They use no scientific executable,
enumeration or numerical search.

Fix \(N\) and use orthonormal coordinates \(E_d/\sqrt{w(d)}\) for the
squarefree split supports \(d\le N\). Write \(b_d=\sqrt{w(d)}\beta_N(d)\)
for the coefficient vector of the actual sum \(B_N\), and
\(k_d=\sqrt{w(d)}\) for the augmentation vector. Put
\[
 D=\|k\|^2=D(N),\qquad m=k^*b=M(N),\qquad P=kk^*/D.
\]
The coordinates of \(b,k\) are real. The geometric statements allow complex
coordinates and use \(k^*b\) for the pairing that is linear in \(b\).
For the fourth-root product sampling with the trivial sample removed,
assume there is at least one split prime at most \(N\). Write \(A=A_N\),
\(q=4^{|P_N|}\) and \(\delta=D/q<1\), so that
\(A^*A=I-\delta P\) and \(z=A k/(1-\delta)\).

## 1. The best positive norm product at fixed condition number

For a positive definite Hermitian form \(G\), let
\[
 \mathcal P_G(b,k)=\bigl[(b^*Gb)(k^*G^{-1}k)\bigr]^{1/2}.
\]
To realize this exact allowance with the existing samples, set
\(U=A(A^*A)^{-1/2}\), an isometry into the sample space. The analysis
\(U G^{1/2}\) and readout \(U G^{-1/2}k\) have adjoint pairing \(k^*b\).
The readout is in the analysis range, so it has minimal norm among the
exact readouts. Their Euclidean norm product is \(\mathcal P_G\).

Suppose \(b,k\ne0\). Define the two angle parameters
\[
 \rho=\frac{|k^*b|}{\|k\|\|b\|},\qquad s=\sqrt{1-\rho^2}.
\]
For a condition number bound \(K\ge1\), put
\(C=(\sqrt K+1/\sqrt K)/2\) and \(S=(\sqrt K-1/\sqrt K)/2\). Then
\[
 \min_{\operatorname{cond}(G)\le K}
 \frac{\mathcal P_G(b,k)}{\|k\|\|b\|}
 =
 \begin{cases}
   C-Ss,&s>S/C,\\
   \rho,&s\le S/C .
 \end{cases}                                                     \tag{1}
\]
In particular the cost is \(K^{-1/2}\) for orthogonal unit vectors, and the
least condition number at which (1) equals \(\rho\) is
\((1+s)/(1-s)\) when \(\rho>0\). For parallel vectors the identity attains
the minimum. A zero vector gives product zero for every positive form.

To prove (1) for nonparallel vectors, compress \(G\) to the span of \(b,k\).
The inverse quadratic form on this span can only decrease. Indeed, for
\(y\) in the span, \(y^*G^{-1}y\) is the supremum of
\(2\Re(y^*x)-x^*Gx\), and restricting \(x\) gives the inverse of the
compression. The compression preserves the first quadratic form, and its
eigenvalues are between the extreme eigenvalues of \(G\).
Conversely, a form on the span extends by a scalar between its two
eigenvalues.

In two dimensions write \(u=b/\|b\|\) and take a unit \(w\perp k\) with
\(u^*w=s\). The two-dimensional inverse formula gives
\(k^*G^{-1}k/\|k\|^2=(w^*Gw)/\det G\). Normalize the determinant to one
and let \(L\le K\) be the condition number. The form is
\(C_L I+S_L H\), with \(C_L,S_L\) defined as \(C,S\) at \(L\), and with
\(H\) a traceless Hermitian involution when \(L>1\). For \(L=1\) take any
such \(H\). In the orthonormal bisector basis, \(u\) and \(w\) have
coordinates \((c,t)\) and \((c,-t)\), where
\(c^2-t^2=s\) and \(2ct=\rho\). If \(s=1\), use \(u=w\) as the first
basis vector. Write
\[
 H=\begin{pmatrix} h&x+iy\\x-iy&-h\end{pmatrix},\qquad
 h^2+x^2+y^2=1.
\]
The squared normalized product is
\[
 (C_L+S_L s h)^2-S_L^2\rho^2 x^2
 \ \ge\ \rho^2+(S_L h+C_L s)^2.
\]
For any \(h\in[-1,1]\) equality is attained with \(y=0\).
Minimizing in \(h\) leaves \(\rho^2+\max(0,C_L s-S_L)^2\).
Writing \(C_L=\cosh t_L\), \(S_L=\sinh t_L\) with
\(t_L=\tfrac12\log L\), the difference \(C_Ls-S_L\) decreases with \(L\).
Taking \(L=K\) proves the formula. The minimizing bisector form uses the
direction of \(b\) in its plane with \(k\) and its angle to \(k\).
Fitting this form to the actual pair uses the overlap \(|m|\) in (1).

## 2. A rank-one mixer specified by the target

The choice \(G_K=I+(K-1)P\) uses \(k,D\) and the prescribed \(K\).
Its exact allowance is
\[
 \mathcal P_{G_K}(b,k)^2
   = |m|^2+\frac{D\|b\|^2-|m|^2}{K}.                             \tag{2}
\]
This choice is minimax at every prescribed \(\rho\) if all unit signals
with that angle are allowed and \(\dim\mathcal H_N\ge2\). To see this,
write \(e=k/\|k\|\) and rescale a competitor \(G\) to
\(e^*G^{-1}e=1\). Cauchy gives \(e^*Ge\ge1\). The condition number bound
then gives \(v^*Gv\ge1/K\) for every unit \(v\perp e\). Averaging the
allowances squared for \(\rho e+s v\) and \(\rho e-s v\) gives at least
\(\rho^2+s^2/K\). Formula (2) attains that value for every such signal.
For a single pair the normalized optimum is at least
\(\max(\rho,K^{-1/2})\), by Cauchy and the eigenvalue bounds. Thus (2) is
within a factor \(\sqrt2\) of even the pair-dependent optimal product.

There is a direct implementation on the fourth-root samples. Since
\(AP=P_{Ak}A\), where \(P_{Ak}\) projects onto \(Ak\), define
\[
 T_K=I+(\sqrt K-1)P_{Ak},\qquad
 \widetilde A=T_K A=A G_K^{1/2},\qquad
 \widetilde z=z/\sqrt K .
\]
Then \(\widetilde A^*\widetilde z=k\), and \(\widetilde z\) is the
minimal-norm readout. The eigenvalues of \(\widetilde A^*\widetilde A\)
are \(K(1-\delta)\) on \(k\) and \(1\) on its orthogonal complement. Hence
\[
 \|\widetilde z\|^2=\frac{D}{K(1-\delta)},\qquad
 \|\widetilde A b\|^2\|\widetilde z\|^2
  =|m|^2+\frac{D\|(I-P)b\|^2}{K(1-\delta)}.                      \tag{3}
\]
The mixer amplifies the measured component in \(Ak\) by \(\sqrt K\)
and divides its readout by the same factor.

The coefficient norm of the actual sum has the sharp order
\(\|b\|^2\asymp N\). For the upper bound, section 4 of MOBIUS.md gives
\[
 |\beta_N(d)|\ll (N/d)^{1/3}
                  \prod_{p\mid d}(1-p^{-2/3})^{-1}.
\]
Put \(g_2(d)=w(d)\prod_{p\mid d}(1-p^{-2/3})^{-2}\) on the squarefree
split supports and zero elsewhere. Then \(\sum_{d\le x}g_2(d)\ll x\).
In fact \(g_2\le w*v_2\), where \(v_2\) is nonnegative and
multiplicative, supported on squarefree split supports and given at
split primes by \(v_2(p)=2[(1-p^{-2/3})^{-2}-1]\). Equality holds on
squarefree split supports. The absolute sum \(\sum_d v_2(d)/d\)
converges by its Euler product because \(v_2(p)=O(p^{-2/3})\).
The claim follows from \(\sum_{d\le x}w(d)\ll x\) by convolution.
Partial summation now gives
\[
 \|b\|^2\ll N^{2/3}\sum_{d\le N}g_2(d)d^{-2/3}\ll N.
\]
The top band \(N/2<d\le N\) supplies the lower bound. In (3) take
\(K=(1+\lfloor\sqrt N\rfloor)^2\), which is comparable to \(N\) and
makes the sampling multiplier \(\sqrt K\) integral. The readout norm
is bounded, the term transverse to \(P\) is \(O(N)\), and the other term
is exactly \(M(N)^2\). An estimate of the full squared norm product at
the square-root scale still requires this arithmetic term.

## 3. Exact cost of removing a specified source subspace

Let \(S_0\) be an orthogonally marked source subspace and
\(T_0=S_0^\perp\). Use subscripts \(S_0,T_0\) for projections, put
\(D_{T_0}=\|k_{T_0}\|^2\), and write \(m_{S_0}=k_{S_0}^*b_{S_0}\),
\(m_{T_0}=k_{T_0}^*b_{T_0}\). On the clean projected data \(Ab_{T_0}\)
the minimal readout for \(m_{T_0}\) is
\[
 z_{T_0}=\frac{A k_{T_0}}{1-D_{T_0}/q},\qquad
 \|z_{T_0}\|^2=\frac{D_{T_0}}{1-D_{T_0}/q}.                     \tag{4}
\]
Indeed the compressed Gram on \(T_0\) is
\(I_{T_0}-k_{T_0}k_{T_0}^*/q\). With the original data \(Ab\), the
same readout satisfies
\[
 A^*z_{T_0}=k_{T_0}-\frac{D_{T_0}}{q-D_{T_0}}\,k_{S_0},\qquad
 m=z_{T_0}^*Ab+\frac{q}{q-D_{T_0}}m_{S_0}.                       \tag{5}
\]
This follows by applying \(A^*A=I-kk^*/q\) to \(k_{T_0}\).
Replacing \(m_{S_0}\) by \(a\) produces an error of magnitude
\(\frac{q}{q-D_{T_0}}|a-m_{S_0}|\) on raw data, or \(|a-m_{S_0}|\)
on the projected data. The raw factor is at most
\((1-\delta)^{-1}\le4\). If \(k_{S_0}=0\), this subspace already has
zero contribution. On projected data, discarding a general
\(m_{S_0}\) has sharp uniform cost \(\|k_{S_0}\| B\) over
\(\|b_{S_0}\|\le B\). Replacing the functional by \(g^*b_{S_0}\)
for \(g\in S_0\) changes that cost to \(\|k_{S_0}-g\|B\), by
the same sharp Cauchy equality.

If \(S_0\) lies in the directions \(d\le L\), then
\(\|k_{S_0}\|^2\ll L\). For \(1\le L\le N\) the above coefficient
bound gives
\[
 \|b_{S_0}\|^2\ll N^{2/3}L^{1/3},\qquad
 |m_{S_0}|\ll N^{1/3}L^{2/3}.
\]
The first estimate uses the \(g_2\) mean bound and partial summation,
and the second follows by Cauchy. This includes any fixed finite span
of specified source rows for sufficiently large \(N\), because every
direction in a row at index \(n\) divides \(n\). The neutral direction
\(E_1\) has \(\|k_{S_0}\|^2=1\) and \(m_{S_0}=C_0(N)=O(N^{1/3})\).
At \(L=N^{1/4}\) the bounds are \(O(N^{3/4})\) on deleted coefficient
energy and \(O(N^{1/2})\) on its contribution to augmentation. For
\(L\le N/2\) the top band remains in the complementary data, so the
unweighted complementary Cauchy product is still of order \(N\).
Formula (2) applies on \(T_0\) with the projected target and signal
when \(k_{T_0}\ne0\).

## 4. Prime-support blocks and an explicit arithmetic estimate

For a chosen subset of the split primes at most \(N\), let \(R\) be
their squarefree product. Partition the directions into blocks indexed
by the part \(h\) of \(d\) coprime to \(R\), so \(d=ha\) with \(a\mid R\).
For each nonempty block set
\[
 D_h=\sum_{\substack{a\mid R\\ha\le N}}w(ha),\qquad
 m_h=\sum_{\substack{a\mid R\\ha\le N}}w(ha)\beta_N(ha).
\]
Let \(P_h\) project onto \(k\) restricted to block \(h\), as a
one-dimensional subspace of the whole coordinate space. The form
\(G_{K,R}=I+(K-1)\sum_h P_h\) uses only the partition and the target.
It has the exact product
\[
 \mathcal P_{G_{K,R}}(b,k)^2
   =\mathcal E_R(N)+\frac{D\|b\|^2-\mathcal E_R(N)}{K},
 \qquad
 \mathcal E_R(N)=D\sum_h\frac{|m_h|^2}{D_h}.                       \tag{6}
\]
The projector ranges are orthogonal and their sum contains \(k\), so
the sum of the projectors commutes with the fourth-root Gram.
The raw-sample realization is \(A G_{K,R}^{1/2}\), with readout
\(z/\sqrt K\). Its squared allowance is
\[
 |m|^2+\frac{\mathcal E_R(N)-|m|^2}{1-\delta}
       +\frac{D\|b\|^2-\mathcal E_R(N)}{K(1-\delta)}.              \tag{7}
\]
For this formula, decompose \(b\) into its \(k\) component, the rest of
the sum of the projector ranges, and the orthogonal complement. The
squared norms of the three components are respectively
\(|m|^2/D\), \((\mathcal E_R(N)-|m|^2)/D\) and
\(\|b\|^2-\mathcal E_R(N)/D\). These components have fourth-root Gram
eigenvalues \(1-\delta,1,1\), and the first two acquire the factor
\(K\) from the squared mixer. Both (6) and (7) preserve the exact signed
pairing.

The block contribution has a finite signed formula in restricted source
rows. Define \(\beta^{(R)}(h;x)\) as the \(E_h\) coefficient of
\(\sum_{n\le x,\ (n,R)=1}\boldsymbol\mu(n)\). Then
\[
 m_h=w(h)\sum_{\substack{a\mid R\\a\le N/h}}
                      (-1)^{\omega(a)}\beta^{(R)}(h;N/a).        \tag{8}
\]
Indeed, evaluating \(X_p=1\) for \(p\mid R\) multiplies a direction
\(E_{ha}\) by \(w(a)\) and leaves \(E_h\). Factor each index \(n\)
into its part coprime to \(R\) and its part supported on primes of
\(R\). The specialized local rows at those primes have coefficients
\(1,-1,0,\ldots\) in the successive prime powers. Thus the supported
part runs only over \(a\mid R\) with sign \((-1)^{\omega(a)}\).
Finally augment the remaining direction \(E_h\) by \(w(h)\).

Adding one split prime \(p\) to \(R\) merges any pair of old blocks
with indices \(h\) and \(ph\). If the old weights and contributions
are \(D_1,D_2,m_1,m_2\), the decrease in \(\mathcal E_R(N)/D\) from
that pair is exactly
\[
 \frac{D_1D_2}{D_1+D_2}\left|\frac{m_1}{D_1}
                                  -\frac{m_2}{D_2}\right|^2.
\]
A sole block retains its contribution. The decrease follows by
expanding the two old terms and the merged term. The endpoints of
coarsening are \(D\|b\|^2\) for \(R=1\) and \(|m|^2\) when \(R\)
includes all the split primes up to \(N\). In intermediate cases (8)
exposes the signed differences inside each block that must be
controlled before summing its square.

For every \(R\), each \(h>N/2\) coprime to \(R\) is the only direction
in its block and satisfies \(|m_h|=D_h=w(h)\). Therefore
\[
 \mathcal E_R(N)\ \ge\
 D(N)\sum_{\substack{N/2<h\le N\\(h,R)=1}}w(h).                   \tag{9}
\]
More generally any positive form preserving these blocks gives a
norm product at least \(\sum_h|m_h|\), by Cauchy within blocks and
then across them. If \(R\) is fixed, the sum in (9) is
\(\asymp_R N\). To obtain this from section 1 of MOBIUS.md, replace the
local quotient \(h_p(t)=(1+2t)(1-t)^2\) at the finitely many primes of
\(R\) by \((1-t)^2\). The same absolute convergence and convolution
argument gives main coefficient
\(\kappa_5\prod_{p\mid R}(1+2/p)^{-1}>0\) for the coprime cumulative
weight, with error \(O_{R,\epsilon}(x^{1/2+\epsilon})\).
Consequently every fixed prime choice retains a linear norm allowance.
The exact test (9) applies also to moving prime sets.

**O.** For an explicit moving choice \(R=R_N\) made from the support,
the arithmetic input sufficient for this block method on
\(I_{3/2}(Y)=[Y,Y^{3/2})\cap\mathbf Z\) is the following. For every
\(\eta>0\), arbitrarily late complete windows should satisfy
\[
 \sum_{N\in I_{3/2}(Y)}
          \frac{\mathcal E_{R_N}(N)}{N(N+1)}\ll_\eta Y^\eta .     \tag{10}
\]
Here each block contribution is specified by (8). With \(K\asymp N\),
the transverse remainder in (6) has weighted sum \(O(\log Y)\), and
(7) differs only by uniformly bounded factors. The positive-part
criterion of MOBIUS.md follows by using (10) at smaller exponents
and absorbing the constants on sufficiently late windows.
Condition (10) asks for squared cancellation within the blocks and
also controls the negative part of \(M\). It can be stronger than
the signed positive-part criterion. At the single-block endpoint
it is the whole-target square estimate. No estimate of (10) for an
intermediate moving partition is proved here. The geometric optimum
and the exact reconstruction leave the arithmetic estimate open.
