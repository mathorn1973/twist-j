# The auxiliary test vector and the remaining global rank problem

**NON-CANONICAL. No authority. No Canon status change.**

**Candidate-D.** For each finite instance satisfying the genuine hypotheses of round 12, the common smooth test vector already evaluates the original period maps. The remaining question concerns how their global coefficients vary over the row space. The example below gives an exact obstruction to deducing the required inequality from injectivity and coordinate tests alone.

## Which space contains the test vector?

The finite-dimensional automorphic space $HH$ is the target of $P_u:C_u\to HH$. Write $\Sigma=\bigotimes_{v\mid\infty}\sigma_v$ for the archimedean representation, $\Sigma^\infty$ for its smooth vectors, and $w\in\Sigma^\infty$ for the prescribed unit vector in the minimal compact type. The row correspondence associates to each $f\in HH$ a unique intertwiner in the specified finite-level space,

$$
I_f:\Sigma\longrightarrow L^2_{\rm aut},\qquad I_f(w)=f.
$$

Thus $f$ specifies which automorphic realization is evaluated. A smooth vector $v$ specifies the input to $I_f$ in that realization. The expressions $v\in\Sigma^\infty$ and $I_f(v)\in L^2_{\rm aut}$ have different domains. Asking whether $v$ itself belongs to $HH$ would require an additional identification. Evaluation at $v$ is already defined for every original $f$.

Let $B_u:\Sigma^\infty\to V_u$ be the normalized archimedean Bessel map. The rational unitary transport $m_u$ gives $\widetilde B_u(v)=B_u(\Sigma(m_{u,\infty})v)$. The transported maps take values in pairwise inequivalent irreducible representations of the same compact group. Their combined image projects onto each summand. Complete reducibility therefore gives surjectivity onto $\bigoplus_u V_u$. Given unit vectors $\xi_u\in V_u$, choose $v_*\in\Sigma^\infty$ with $\widetilde B_u(v_*)=\xi_u$ for every word. For each $f$, the vector $I_f(\Sigma(m_{u,\infty})v_*)$ is a legitimate smooth automorphic input with the prescribed finite level. It can leave the minimal compact type. The matrix entry on the left of the period identity still uses $f\in HH$. [Round 12, §§2 and 8](../round12/PROOF.md)

## What the archimedean choice fixes

Use inner products linear in their second argument. For the actual positive quotient-measure factor $c_u$, set $\gamma_u(f,T)=\langle f,P_uT\rangle/c_u$. Round 12 proves the exact factorization

$$
L_{u,f,T}(v,\xi)=\gamma_u(f,T)\,\langle B_u(v),\xi\rangle .
$$

Here the bilinear Bessel period pairs the column $\operatorname{colForm}(T,\xi)$ with the conjugated row evaluated at $\iota_X(g)(1,x_u)$. In particular, $x_u$ remains the prescribed finite translate even when $v$ varies. Substitution of $v=\Sigma(m_{u,\infty})v_*$ and $\xi=\xi_u$ makes the last factor one for every word. The scalars $\gamma_u(f,T)$ retain the global period, its rational orbit and its finite tests. The choice of $v_*$ supplies no relation among them as $f$ and $T$ vary.

The normalization matters for this conclusion. Local multiplicity one makes the archimedean functional proportional to $B_u$. Writing $W_u(y)=B_u(\Sigma(y)w)$, the original integral then pairs $W_u(y)$ with itself. Its integral with respect to the specified quotient measure is $\int\|W_u(y)\|^2\,d\nu_{Q,u}(y)=1$. This identifies the proportion in the bilinear period with the original matrix entry divided by $c_u$.

The separate literal-translate result uses one $y\in G_\infty$ and $v=\Sigma(y)w$. It preserves all the ranks after multiplying each word map by its own nonzero scalar. Both deductions use analytic input, including absolute unfolding and smooth evaluation. The common-$y$ argument also uses real analyticity of the coefficient functions. The resulting equality of ranks is algebraic. [Round 12, §§3–7](../round12/PROOF.md)

Let $\Gamma_u:C_u\to HH$ be defined by $\langle f,\Gamma_uT\rangle=\gamma_u(f,T)$. Then $P_u=c_u\Gamma_u$. For $D=\dim HH>0$ and $R=\sum_u\dim C_u>0$, the remaining inequality at tolerance $\epsilon_*$ is

$$
\sum_u\operatorname{rank}(\Gamma_u^*|_V)
\ \geq\ R\left(\frac{\dim V}{D}-\epsilon_*\right)
\qquad\text{for every subspace } V\leq HH .
$$

## An exact four-column example

**Candidate-D, abstract linear algebra.** Take $HH=\mathbb C^3$ with its standard Hermitian inner product and four one-dimensional column spaces. Let $\Gamma_j(t)=t a_j$, where

$$
a_1=(1,1,1),\qquad a_2=(1,1,2),\qquad
a_3=(2,2,1),\qquad a_4=(1,2,1).
$$

All entries are strictly positive integers and the four image lines are distinct. The independent vectors $a_1,a_2$ span the plane $x_1=x_2$, which contains $a_3$. The fourth vector lies outside that plane. Thus the columns span $\mathbb C^3$, and the joint map $f\mapsto(\Gamma_j^*f)_{j=1}^4$ is injective.

For a subspace $V$, write $s(V)=\sum_j\operatorname{rank}(\Gamma_j^*|_V)$. This counts the columns outside $V^\perp$. The deficit is $\dim V/3-s(V)/4$. On every nonzero coordinate subspace $s(V)=4$, because each column has a nonzero entry in each coordinate. Every coordinate subspace consequently meets the inequality at zero tolerance.

For the line $V=\mathbb C(1,-1,0)$ the first three adjoints vanish and the fourth is nonzero. Its deficit is $1/3-1/4=1/12$. This is the exact maximum over all complex subspaces. Injectivity forces $s(V)\geq1$ on any line. For a plane, $V^\perp$ is a line and contains at most one of the four distinct image lines, so $s(V)\geq3$ and the deficit is at most $2/3-3/4<0$. The zero subspace and the whole space each have deficit zero. The example shows why a common kernel check and even all coordinate subspace checks can miss the controlling direction. It makes no assertion that these columns occur as automorphic period maps.

One can attach simultaneous test vectors to this example directly. Take an auxiliary space $\mathbb C^4$ and let $B_j$ be its four coordinate projections. Their combined map is onto, and the auxiliary vector $(1,1,1,1)$ realizes a unit in every output. Define the abstract periods by multiplying $\gamma_j(f,t)=\langle f,t a_j\rangle$ by $\langle B_j(v),\xi\rangle$. They now have the displayed factorization and the common-vector property, while the four row adjoints still have deficit $1/12$. The construction isolates the implication being tested at the level of linear maps.

One may label the three coordinate lines by distinct characters of a diagonal circle action, each with multiplicity one. This does not make the four column maps equivariant under that action: their image lines are not invariant. Such labels supply no valid reduction of the subspaces in the rank test. The example therefore does not contradict any reduction that separately proves invariance under the actual Hecke algebra.

## The separate rational norm test

For a quadratic extension $E=F(\sqrt d)$ of number fields, two coefficients in $F^\times$ have the same global norm class exactly when their ratio $a$ is a norm at every completion. Indeed the conic $X^2-dY^2=aZ^2$ then has a point everywhere locally, hence over $F$ by Hasse–Minkowski. A global point has $Z\ne0$ since $d$ is nonsquare in $F$, giving $a=N_{E/F}((X+Y\sqrt d)/Z)$. The converse follows by localization. This criterion tests a *given* pair of rational coefficients. Global occurrence of a Fourier coefficient on the specified orbit and the rank inequality above remain **O** for the positive-index problem. [Milne, *Class Field Theory*, VIII §3, Theorems 3.1 and 3.5](https://www.jmilne.org/math/CourseNotes/CFTc.pdf#page=243)
