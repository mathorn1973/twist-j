# Round 19. A spectral certificate for arbitrary test subspaces

**NON-CANONICAL. No authority. Candidate-D (finite-dimensional deductions).**
The actual uniform period estimate remains **O**. All arguments below are on paper.

## 1. What an incidence costs

Let a finite tuple of complex linear maps be given by $A_u:E_u\to F$,
with $D=\dim F>0$, $R=\sum_u\dim E_u>0$. Use any positive definite
Hermitian inner product on the target. Write $I_u=\operatorname{im} A_u$,
$H_u$ for its orthogonal projector, $S=\sum_u H_u$, and
$\kappa=R^{-1}\sum_u\dim\ker A_u$. The concentration defect is exactly

$$
 \epsilon=\kappa+\max_{W\le F}
 \left(\frac{1}{R}\sum_u\dim(W\cap I_u)-\frac{\dim W}{D}\right).
 \tag{19.1}
$$

For the orthogonal projector $X$ onto $W$, the compression $XH_uX|_W$
is a positive contraction. Its eigenvalue-one space equals $W\cap I_u$,
since equality in the norm contraction of an orthogonal projection forces
membership in its range. Write $t_i$ for the compression eigenvalues,
counted with multiplicity. Block multiplication relative to $W\oplus W^\perp$
gives

$$
 \tfrac12\|[X,H_u]\|_{\rm HS}^2
 =\operatorname{tr}_W(XH_uX-(XH_uX)^2)
 =\sum_i t_i(1-t_i).
$$

The exact principal-angle loss is consequently

$$
 \operatorname{tr}(XH_u)-\dim(W\cap I_u)
 =\tfrac12\|[X,H_u]\|_{\rm HS}^2+\sum_{0<t_i<1}t_i^2 .
 \tag{19.2}
$$

Here $t_i$ are squared principal cosines, with zeros added if necessary.
The last term is nonnegative. A large centered frame trace by itself does
not account for this loss.

## 2. An inequality between two finite matrices

For the moment work on a single target of dimension $d>0$ with projections
$H_u$. Use the unnormalized Hilbert--Schmidt inner product. On its matrix
space define the self-adjoint positive operator

$$
 \mathcal L(Y)=\tfrac12\sum_u[H_u,[H_u,Y]]
 =\tfrac12(SY+YS)-\sum_u H_uYH_u .
 \tag{19.3}
$$

Its quadratic form is $\tfrac12\sum_u\|[H_u,Y]\|_{\rm HS}^2$. Suppose it
is at least $\gamma\|Y\|_{\rm HS}^2$ on traceless Hermitian matrices, for
some $\gamma\ge0$. For a projection $X$ of relative rank $x$, put
$Y=X-xI$, $h=\operatorname{tr}(S)/d$, $T=S-hI$ and
$\Delta=\lambda_{\max}(S)-\lambda_{\min}(S)$. Directly from the two
eigenvalues of $Y$,

$$
 \|Y\|_{\rm HS}^2=dx(1-x),\qquad \|Y\|_1=2dx(1-x).
$$

Subtract the spectral midpoint of $S$ inside $\operatorname{tr}(YS)$.
Trace duality gives $\operatorname{tr}(YS)\le\Delta dx(1-x)$. Applying
(19.2) to all words now gives the incidence bound

$$
 \sum_u\dim(\operatorname{ran}X\cap I_u)
 \le hdx+(\Delta-\gamma)dx(1-x).
 \tag{19.4}
$$

**Candidate-D.** If $\gamma\ge\Delta$, every subspace receives at most its
proportional share of the total image rank, including when $S$ has unequal
eigenvalues. A sufficient test uses real scalars $a,b$ and finite
positive-semidefinite inequalities

$$
 aI\preceq S\preceq bI,\qquad
 \mathcal L|_{\operatorname{tr}=0}\succeq (b-a)I .
 \tag{19.5}
$$

These inequalities are linear in $a,b$ for a given tuple. The restriction
may be made on the real space of traceless Hermitian matrices in a
Hilbert--Schmidt orthonormal basis. With a nonorthonormal basis the right
side uses its metric matrix. A one-dimensional block has no traceless test.

**Candidate-D.** There is also a variance bound. With $V=d^{-1}\operatorname{tr}(T^2)$,
Cauchy--Schwarz bounds the centered incidence per target dimension by
$\sqrt{Vx(1-x)}-\gamma x(1-x)\le V/(4\gamma)$ if $\gamma>0$.
For example, for isometries with $d=D$, put
$Q=(D/R)S$, $v=D^{-1}\operatorname{tr}((Q-I)^2)$, and
$g=(D/R)\gamma>0$. Formula (19.1) then gives
$\epsilon\le v/(4g)$. For arbitrary kernels, use (19.1) with the
actual ranks and retain the kernel and block-mass terms below.

## 3. Common reducing subspaces and the exact central term

Let $\mathcal A=\operatorname{alg}^*(I,H_u:u)$. In (19.1) the objective
is supermodular on subspaces. Indeed for each image, the sum of its
intersections with two test spaces is contained in its intersection with
their sum, while the intersection term is exact. The target dimension is
modular. Hence the sum and intersection of any two maximizers are also
maximizers. There is a unique largest maximizer, obtained by choosing one
of maximal dimension. Existence follows from the finite set of possible
dimension tuples.

Every unitary of $\mathcal A'$ preserves all the images. It fixes the
largest maximizing space and commutes with its orthogonal projection.
Unitaries span a finite-dimensional star algebra, so this projection
belongs to $\mathcal A''=\mathcal A$. Write its ordinary finite-dimensional
star-algebra decomposition as

$$
 F=\bigoplus_j\mathbb C^{d_j}\otimes\mathbb C^{m_j},\qquad
 \mathcal A=\bigoplus_j M_{d_j}(\mathbb C)\otimes I_{m_j},\qquad
 H_u=\bigoplus_j H_{uj}\otimes I_{m_j}.
$$

The largest maximizing projection thus has the form
$\bigoplus_j X_j\otimes I_{m_j}$. Maximization separates in these blocks.
Equivalently the Hilbert--Schmidt conditional expectation onto $\mathcal A'$
sends this projection to $\bigoplus_j x_j I_{d_j}\otimes I_{m_j}$. Its
restriction to $\mathcal A$ averages onto the center. No gap between two
different simple blocks, or on maps between equivalent copies, is required.

For $S_j=\sum_uH_{uj}$ set $h_j=\operatorname{tr}(S_j)/d_j$, and let
$\Delta_j,\gamma_j$ be the diameter and a lower gap bound as in Section 2.
Write $t_+=\max(t,0)$. Whole-block selection gives the lower bound, and
(19.4) with $x_j(1-x_j)\le1/4$ gives the upper bound

$$
 \begin{aligned}
 B&=\kappa+\sum_j m_jd_j(h_j/R-1/D)_+,\\
 B&\le\epsilon\le B+\frac1{4R}\sum_j m_jd_j(\Delta_j-\gamma_j)_+ .
 \end{aligned}\tag{19.6}
$$

The variance argument independently bounds each additive error by
$m_jd_j V_j/(4R\gamma_j)$ when $\gamma_j>0$. If every test (19.5)
passes, the lower bound $B$ is the **exact** defect. In particular,
proportional central image masses and zero kernels imply semistability.

Every simple block of dimension greater than one has a strictly positive
gap for each fixed tuple: a zero-energy matrix commutes with all its image
projectors, and these generate the entire simple matrix algebra. This
argument gives no family-uniform ratio of gap to diameter. The center here
is that of the algebra *generated by the image projectors*. Its masses do
not inherit the round 17 estimates for the separately constructed Hecke
and determinant algebra. In a commuting incidence model the present blocks
all have dimension one. The tests then pass vacuously and the whole defect
is already $B$. Applying the tests inside a pre-existing reduction instead
requires keeping its source and target normalizations.

## 4. A nontight rational certificate

Take the four complex lines through $(4,1),(0,1),(1,1),(1,-1)$ in
$\mathbb C^2$, with the standard metric. Their image projectors have
rational entries. Start with the same lines but with $(1,0)$ in the
first slot. The two orthogonal bases then give $S_0=2I$. In the usual
traceless Hermitian basis of Pauli matrices, the pair of coordinate-line
projections kills the diagonal direction in (19.3) and acts as identity
on the other two. The pair of diagonal-line projections kills the real
off-diagonal Pauli direction and acts as identity on the other two.
Thus the eigenvalues of the original form are $1,2,1$.

The change of the first projector is the traceless matrix
$17^{-1}\left(\begin{smallmatrix}-1&4\\4&1\end{smallmatrix}\right)$
with eigenvalues $\pm t$, $t=1/\sqrt{17}$. The new $S$ has diameter
$2t>0$. For a projector $H$, the commutator map $Y\mapsto[H,Y]$ has
Hilbert--Schmidt operator norm at most one, by diagonalizing $H$.
Changing $H$ by this matrix changes the commutator map in norm by at
most $2t$. Factoring the difference of its squares as
$A^2-B^2=A(A-B)+(A-B)B$ bounds the change in (19.3) by $2t$. Therefore
$\gamma\ge1-2t>2t=\Delta$, since $17>16$. The certificate proves
semistability with strict margin. Taking $m>1$ equal copies as
$H_u\otimes I_m$ makes the gap on all traceless target matrices zero,
while the reduced certificate still passes.

## 5. Construction from a Gram matrix alone

Let $A$ be the joint column matrix and let $G=A^*A$ include its word
partition. Given $D$ as well, this determines the arrangement up to
target unitary equivalence. Choose independent columns indexed by $J$
spanning its image, so $K=G_{J,J}$ is positive definite. In that basis
the coordinate matrix of all columns is $C=K^{-1}G_{J,:}$, with target
metric $K$. Select independent columns $V_u$ from the $u$-part of
$C$ spanning that word. Its projector in these coordinates is exactly

$$
 H_u=V_u(V_u^*KV_u)^{-1}V_u^*K.
$$

An empty image gives the zero projector. Include $D-\operatorname{rank}G$
orthogonal blind dimensions on which all projectors vanish. If $G=0$,
all maps vanish and (19.1) gives $\epsilon=1$ directly. In the coordinate
space with metric $K$, the adjoint of $Y$ is $K^{-1}Y^*K$. This
gives the matrix-space metric for (19.5) with no positive square root of
$G$ or polar inverse. Ordinary linear systems give the commutant and
center, and finite-dimensional spectral decompositions separate their
blocks. Exact coefficient matrices over a specified number field and
embedding permit algebraic operations after adjoining conjugates and any
required algebraic eigenvalues. The convergent actual-period Gram
expansion is a mathematical input, not an assertion that these entries
are supplied in such an exact format.

Any common invertible target transformation $L$ preserves (19.1), by
$W\leftrightarrow LW$; source changes of basis also preserve it. One may
therefore apply the certificate to images $LI_u$ after recomputing their
orthogonal projectors. A gap or diagonal Gram estimate proved in an earlier
metric does not automatically transfer to a new one.

Spectral gaps and near balance have also been used to study operator
scaling, including convergence in Theorem 1.5 and capacity in Theorem 1.8 of
[Kwok, Lau and Ramachandran](https://cs.uwaterloo.ca/~lapchi/papers/spectral-scaling.pdf).
The elementary incidence deductions above invoke no scaling convergence
theorem and make no priority claim. No estimate on the missing actual
period gap-to-diameter comparison has been proved here.
