# Uniform control of sector cancellation by component orientations

**PUBLIC / NON-CANONICAL. Written proof candidate, candidate-T ceiling.**

- Item: C-PHOTON-SECTOR-ORIENTATION-CANCELLATION-N, #1241
- Author: A. M. Thorn
- Basis: Public Canon v92; public main
  `ad8a572128f594a3550cbf5e3adef2516fea3d88`
- Primary target: a positive thermodynamic lower bound for H_L is **NOT PROVED**.

This note controls the contribution omitted when the sector first moment is
restricted to a bounded number of components with nonzero measured residue.
All averages and sector denominators retain the original full measure.
Component sizes, diameters and winding lifts remain unrestricted.

Independent component reversals are an existing mechanism, including #1112
and the finer augmented decomposition in
`notes/C-PHOTON-BCHI-DIRECT-BOUND-N/CONNECTED-CURRENT.md`.
The complex-source modulus method also precedes this note; see
`notes/C-PHOTON-BCHI-DIRECT-BOUND-N/REPLICA-CAPS.md`, section 5,
where it is applied to the different integer-closed measure nu_0.
The mixed-current source comparisons in CONNECTED-CURRENT section 5 and
FULL-MEASURE section 10 are also inherited. Neither mechanism is claimed as new. They are derived directly here for the
stated full measure. The new conclusion is the uniform sector-projection
truncation error and its probability consequence.

## 1. Fixed measure and observables

For even L>=4, retain the periodic cubical complex K_L=(Z/LZ)^4 and

\[
\Omega_L=\{n\in\{-1,0,1\}^{P(K_L)}:\partial n=0\pmod5\},
\qquad
\mu_L(n)=\mathfrak Z_L^{-1}2^{-|\operatorname{supp}n|}.
\]

Let Sigma be the 01 seam at x_0=x_1=0, and set

\[
F=\langle n,\Sigma\rangle,\qquad A=F\bmod5,\qquad
G=L^{-2}\sum_{p\parallel01}n_p.
\]

For p_a=mu_L(A=a), define

\[
m_a=E_\mu[G\,1_{\{A=a\}}],\qquad
H_L=\sum_{a:p_a>0}\frac{m_a^2}{p_a}
=\|E_\mu[G\mid A]\|_2^2.
\]

All norms below are in L^2(mu_L). Reversal gives E_mu G=0.
The sector remains A, not a residue assigned to the generally noninteger G.

## 2. An inherited source method gives a uniform Gaussian bound

Put theta=2pi/5 and w(u)=2+2cos u. Character expansion of the link-field
sum gives, for any real face source h_p,

\[
\frac{\sum_{\alpha\in\mathbb F_5^E}
 \prod_p w(\theta(d\alpha)_p-i h_p)}
 {\sum_{\alpha\in\mathbb F_5^E}
 \prod_p w(\theta(d\alpha)_p)}
=E_\mu e^{\sum_p h_p n_p}.
\]

The constant and occupied Fourier coefficients are 2 and 1,1; their
common factor 2^{|P|} cancels. Every original w(theta f) is positive.
For real u,x the exact modulus identity is

\[
|w(u-ix)|=2(\cosh x+\cos u)
=w(u)+2(\cosh x-1).
\]

Take absolute values of the finite link-field sum and expand the resulting
nonnegative factors. This changes only the empty-face coefficient from
2 to 2cosh h_p; the occupied coefficients remain 1. Consequently

\[
E_\mu e^{\sum_p h_p n_p}
\le E_\mu\prod_{p:n_p=0}\cosh h_p
\le\prod_p\cosh h_p
\le \exp\!\left(\frac12\sum_p h_p^2\right).
\]

No independence or sector-conditioned empty-set estimate is used.
Choosing h_p=t/L^2 on the L^4 faces parallel to 01 and zero otherwise proves

\[
\boxed{E_\mu e^{tG}\le e^{t^2/2}\quad(t\in\mathbb R),\qquad EG^2\le1.}
\tag{1}
\]

The second assertion follows at zero from the second derivative of the
nonnegative difference, whose value and first derivative vanish there.
We do not compare arbitrary higher Taylor coefficients.

Chernoff's inequality gives mu_L(|G|>=s)<=2e^{-s^2/2}. If an event D
has probability p>0, the layer-cake formula therefore gives

\[
E[G^2\,1_D]
\le\int_0^\infty\min\{p,2e^{-u/2}\}\,du
=2p\left(1+\log\frac2p\right)=:\Psi(p).
\tag{2}
\]

Set Psi(0)=0. This bound will control rare events in the full measure.

## 3. Exact orientation orbits

Join two occupied plaquettes whenever they share an edge. Write n_j for
the restrictions of n to the connected components of this graph.
No edge meets two different components. Hence each n_j separately satisfies
partial n_j=0 modulo five.

Reversing any selection of whole components preserves admissibility,
support and weight. These reversals partition Omega_L into finite orbits
O. An orbit records the support and the relative signs within each component,
up to reversal of that entire component; it does not identify all fields
having the same support. Choose a reference n_j on each component.
Conditional on O,

\[
n=\sum_j\varepsilon_j n_j,\qquad
\varepsilon_j\in\{-1,+1\}
\quad\hbox{independent and uniform}.
\tag{3}
\]

There are exactly 2^J distinct signings for J occupied components, all with
the same original weight. The orbit distribution is the one induced by mu_L.

Define reference quantities and reversal-invariant orbit quantities by

\[
q_j=\langle n_j,\Sigma\rangle\bmod5,\qquad
g_j=L^{-2}\sum_{p\parallel01}(n_j)_p,
\]
\[
M=\#\{j:q_j\ne0\},\qquad
V=\sum_{j:q_j\ne0}g_j^2,\qquad
S=\sum_jg_j^2.
\tag{4}
\]

M counts nonzero residues of the chosen 01 seam only. A component with
q_j=0 may have nonzero homology in another direction, nonzero G contribution,
or a nonzero integer current. No assertion excluding those possibilities
is made. Changing reference orientation changes q_j,g_j together and
does not change M,V,S.

Conditional on O, G=sum_j epsilon_j g_j and A=sum_j epsilon_j q_j modulo
five. Thus E[G^2|O]=S, and (1) gives

\[
EV\le ES=EG^2\le1.
\tag{5}
\]

Every q_j=0 sign is independent of A and has mean zero. It contributes
nothing to E[G|A,O]. In particular E[G 1_{\{M=0\}}|A]=0.

## 4. Cancellation when many measured residues are nonzero

Write zeta=e^{i theta} and rho=cos(pi/5)=(1+sqrt5)/4. For an orbit O let

\[
p_a^O=P(A=a\mid O),\quad
t_a^O=E[G1_{\{A=a\}}\mid O],\quad
H_O=\sum_{a:p_a^O>0}(t_a^O)^2/p_a^O.
\]

The independent signs give, for k=1,2,3,4,

\[
P_k^O:=E[\zeta^{kA}\mid O]
=\prod_{j:q_j\ne0}\cos(k\theta q_j),
\]
\[
C_k^O:=E[G\zeta^{kA}\mid O]
=i\sum_{j:q_j\ne0}g_j\sin(k\theta q_j)
 \prod_{\substack{\ell:q_\ell\ne0\\\ell\ne j}}
 \cos(k\theta q_\ell).
\tag{6}
\]

These formulae are invariant under changes of reference orientations.
For every nonzero q and k, |cos(k theta q)|<=rho<1. Therefore

\[
|P_k^O|\le\rho^M,\qquad
|C_k^O|^2\le M\rho^{2M-2}V\quad(M\ge1),
\]
\[
p_a^O\ge\frac{1-4\rho^M}{5}.
\tag{7}
\]

Since C_0^O=0 and C_{5-k}^O is the conjugate of C_k^O, Parseval gives

\[
\sum_a(t_a^O)^2
=\frac25\bigl(|C_1^O|^2+|C_2^O|^2\bigr).
\]

For M>=7 the lower denominator in (7) is positive:
4rho^7=(29+13sqrt5)/64<1. Consequently

\[
H_O\le\alpha_M V,\qquad
\alpha_m=\frac{4m\rho^{2m-2}}{1-4\rho^m}\quad(m\ge7).
\tag{8}
\]

Independently, projection of sum_{q_j!=0} epsilon_j g_j onto A gives
H_O<=V for all M. Define b_m=min{1,alpha_m} for integers m>=7.
It decreases to zero, because

\[
\frac{\alpha_{m+1}}{\alpha_m}
=\frac{m+1}{m}\rho^2
 \frac{1-4\rho^m}{1-4\rho^{m+1}}
<\frac87\rho^2=\frac{3+\sqrt5}{7}<1.
\tag{9}
\]

These are orbit calculations, not yet replacements for the full measure.
The next step retains the original orbit weights and sector probabilities.

## 5. Uniform two-sided control of the omitted first moment

Fix an integer r>=7. Define the retained quantity by

\[
\boxed{
H_L^{<r}
=\sum_{a:p_a>0}
\frac{\bigl(E_\mu[G\,1_{\{A=a\}}1_{\{1\le M<r\}}]\bigr)^2}{p_a}.}
\tag{10}
\]

The p_a are those of the FULL mu_L. Formula (10) is not a sector mean
computed in a renormalized restricted measure.

Let U=E[G|A], U_< = E[G1_{1<=M<r}|A] and
U_>= = E[G1_{M>=r}|A]. The M=0 contribution vanishes by section 3,
so U=U_<+U_>=. Conditioning first on (A,O), followed by Jensen, gives

\[
\begin{aligned}
\|U_{\ge}\|_2^2
&\le E\!\left[1_{\{M\ge r\}}\{E[G\mid A,O]\}^2\right]\\
&=E[1_{\{M\ge r\}}H_O]
\le b_r E[V1_{\{M\ge r\}}]\le b_r.
\end{aligned}
\tag{11}
\]

The same original measure is used in every line. Since
||U||_2=sqrt(H_L) and ||U_<||_2=sqrt(H_L^{<r}), the triangle inequality proves

\[
\boxed{\left|\sqrt{H_L}-\sqrt{H_L^{<r}}\right|\le\sqrt{b_r}}
\quad\hbox{uniformly in even }L\ge4.
\tag{12}
\]

In particular,

\[
\boxed{
\bigl(\sqrt{H_L^{<r}}-\sqrt{b_r}\bigr)_+^2
\le H_L
\le\bigl(\sqrt{H_L^{<r}}+\sqrt{b_r}\bigr)^2.}
\tag{13}
\]

Thus all omitted sector cancellation has a stated, arbitrarily small norm
budget as r increases. This does not bound the size of the retained
components or establish the sign of their combined first moment.

## 6. A necessary full-measure probability condition

Put p_{L,r}=mu_L(1<=M<r). Direct projection onto (A,O), rather than
squaring (12), gives the additive estimate

\[
\begin{aligned}
H_L
&\le E H_O\\
&\le E[V1_{\{1\le M<r\}}]+b_r E[V1_{\{M\ge r\}}]\\
&\le E[G^2 1_{\{1\le M<r\}}]+b_r\\
&\le \boxed{\Psi(p_{L,r})+b_r}.
\end{aligned}
\tag{14}
\]

The event is orbit-measurable, so E[V;D]<=E[S;D]=E[G^2;D];
equation (2) justifies the final line. No lower bound on any event weight
has been assumed.

If p_{L,r}->0 for every fixed integer r>=7 along even volumes, then
(14), followed by r->infinity, proves H_L->0. This hypothesis allows both
M=0 and arbitrarily large M. Conversely, liminf H_L>0 requires some fixed
finite r with liminf p_{L,r}>0. Indeed choose b_r below a positive eventual
lower bound for H_L; Psi is continuous, increasing on [0,1], and vanishes
at zero.

This is a necessary condition, not a sufficient one. A nonvanishing
probability of bounded M alone does not rule out cancellation among the
retained signed means.

## 7. Remaining lower-bound obligation

The contribution with many nonzero measured component residues is now
uniformly controlled in the original full measure. To obtain a positive
thermodynamic H_L floor from (13), it remains to prove, for at least one
fixed r>=7,

\[
\liminf_{L\to\infty,\ L\ {\rm even}}\sqrt{H_L^{<r}}>\sqrt{b_r}.
\tag{15}
\]

No such estimate is proved here. It is not enough to show a sign on a
selected support, positivity of a variance, or a large event probability.
The retained components may be macroscopic and their contributions must
still be summed with their actual original weights.

The partial statements are candidate-T. The primary positive lower bound
is NOT PROVED; P1 and PHOTON-MASSLESS-PHASE remain open. There is no
scientific execution, phase verdict, Canon promotion or physical photon
identification in this note.
