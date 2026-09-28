# Averaged flux: sector estimates and the remaining polarization problem

**PUBLIC, NON-CANONICAL. Written proof candidate; review required.**

- Item: C-PHOTON-AVERAGED-SECTOR-POLARIZATION-N, #1233
- Author: A. M. Thorn
- Basis: Public Canon v92; public main
  `3bad0a50065418cde782ce9b3074bb691051d4f1`, the merge of #1231
- Status: candidate-T for the new mathematical consequences below
- Scope: the unchanged finite four-torus measure and its electric winding
  sectors
- Primary target: **a positive thermodynamic lower bound for H_L is NOT
  PROVED**

Two actual full-measure statements are established. First, the canonical
conditional-variance construction supplies its existing positive floor
inside the fluctuation left after projection onto the winding sector.
Second, deleting any set of spatial plaquette factors at one time slice
has an exact lower comparison in each electric sector. Neither result
establishes the required nonzero sector polarization.

The local charged insertion, its 21-face size, its packing density and its
variance constant are already in PHOTON-CONDITIONAL-VARIANCE-FLOOR [T].
They are not new claims here. The new refinement is identification of that
floor as variance **within** the sector. The zero-mode contact identity is
a specialization of the finite source identity, derived below for clarity.

## 1. Fixed observables and projections

For even L>=4, let K_L=(Z/LZ)^4 with positively oriented cubical cells.
The surface measure is

\[
\Omega_L=\{n\in\{-1,0,1\}^{P(K_L)}:\partial n=0\pmod5\},
\qquad \mu_L(n)=\mathfrak Z_L^{-1}2^{-|\operatorname{supp}n|}.
\tag{1}
\]

Let Sigma_(t,s) be the 01 seam at x_0=t,x_1=s and put

\[
F_{t,s}=\langle n,\Sigma_{t,s}\rangle,\qquad
F=F_{0,0},\qquad A=F\pmod5,\qquad
G=L^{-2}\sum_{t,s}F_{t,s}=L^{-2}\sum_{p\parallel01}n_p.
\tag{2}
\]

Summing the direction-1 boundary equations over a transverse plane gives
F_(t-1,s)-F_(t,s) in 5Z; summing the direction-0 equations gives
F_(t,s)-F_(t,s-1) in 5Z. The other terms telescope. Thus every F_(t,s)
has the same residue A. This uses only divisibility of the boundary by
five and also holds for arbitrary integer chains satisfying that condition.

Translation invariance, with this invariant sector label, gives
E[G|A]=E[F|A]. Global reversal gives E G=0. Write

\[
p_a=\mu_L(A=a),\qquad
H_L=\sum_{a:p_a>0}p_a\{E[G\mid A=a]\}^2,
\qquad R_L=E\operatorname{Var}(G\mid A).
\tag{3}
\]

The exact orthogonal decomposition is

\[
\operatorname{Var}(G)=H_L+R_L.
\tag{4}
\]

The sector label throughout is A=F mod 5. G need not be an integer and is
not assigned a new residue label. The full averaging and signed-part
inequalities are proved separately in
`notes/C-PHOTON-SECTOR-CANCELLATION-AUDIT-N/PROOF.md`, section 6.

## 2. The canonical insertion floor lies inside R_L

Use the canonical 01 charged insertion

\[
U(z)=-c_{012}(z)+c_{012}(z-e_2)
     -c_{013}(z)+c_{013}(z-e_3),\qquad
a_z=\partial U(z)-5p_{01}(z).
\tag{5}
\]

PHOTON-CONDITIONAL-VARIANCE-FLOOR [T] proves that a_z is ternary, has
exactly 21 occupied faces, and has boundary -5 partial p_01(z). Its five
01 coefficients are all -1. The same theorem supplies the disjoint packing

\[
z_0,z_1\in\{0,2,\ldots,L-2\},\qquad
z_2,z_3\in\{1+3r:0\le r<\lfloor L/3\rfloor\}.
\tag{6}
\]

Denote the corresponding supports by S_i, their union by B, and their
number and canonical density by

\[
k_L=(L/2)^2\lfloor L/3\rfloor^2,
\qquad c_L=2^{-41}k_L/L^4.
\tag{7}
\]

No edge is incident to faces from two different supports. The canonical
proof establishes this including periodic seams; it also establishes the
unconditional empty-set estimate mu_L(n|S_i=0)>=2^-21. Neither statement
is strengthened here to arbitrary sector-conditioned emptiness.

Let E_B be the information consisting of all face values outside B.
The new observation is

\[
\boxed{A\text{ is determined by }E_B.}
\tag{8}
\]

To prove (8), take any two admissible configurations with the same outside
values and decompose their difference as sum_i d_i, where d_i is supported
on S_i. An edge meets at most one S_i. The global boundary condition
therefore implies partial d_i=0 mod 5 separately for each i. The d_i need
not be ternary; the integer-chain seam congruence after (2) still applies.
All 01 faces of S_i have x_0=z_0 and x_1=z_1. A seam with t different from
z_0 has zero pairing with d_i. The congruence forces its pairing with
Sigma_(0,0) to be zero modulo five as well. Summing over i proves (8).

The conditioning stage of the canonical variance proof, applied to
g_p=L^-2 on 01 faces and zero elsewhere, gives

\[
E\operatorname{Var}(G\mid E_B)
\ge\sum_i 2^{1-2\cdot21}|G(a_i)|^2
=\frac{25k_L}{2^{41}L^4}=25c_L,
\tag{9}
\]

because G(a_i)=-5/L^2. Specifically, before its final total-variance step,
that proof conditions on E_B, uses the three allowed fillings 0,+a_i,-a_i
whenever zero is allowed, and averages their conditional zero probabilities
using the *unconditional* empty-set estimate. This is exactly the quantity
on the left of (9), not a per-sector empty-set comparison.

By (8), conditional total variance now gives

\[
R_L
=E\operatorname{Var}(G\mid E_B)
 +E\operatorname{Var}(E[G\mid E_B]\mid A)
\ge25c_L.
\tag{10}
\]

Consequently

\[
\boxed{R_L\ge\frac{25k_L}{2^{41}L^4}.}
\tag{11}
\]

For even L>=4, floor(L/3)>=L/4, so R_L>=25/2^47 at every admitted
volume. The canonical density tends to rho=1/(36*2^41), hence

\[
\boxed{\liminf_{L\to\infty,\ L\ \mathrm{even}}R_L\ge25\rho.}
\tag{12}
\]

The constant 25rho is the existing canonical zero-mode variance floor.
Equations (8)-(12) show that the same construction survives subtraction of
the projection onto A. Therefore G does not become a function of A in
mean square with a vanishing residual. This does not force H_L to vanish
and does not rule out a positive H_L alongside R_L.

## 3. Known contact identity at zero momentum

For completeness, use the strictly positive link measure pi_L with
W(f)=2+2 cos(theta f), theta=2pi/5, f=(da)_p in F_5. Let
X_p=tan(theta f_p/2) and use the finite source function

\[
\mathcal Z(B)=\sum_a\prod_p w(\theta(da)_p+B_p),
\qquad w(u)=2+2\cos u.
\tag{13}
\]

Character expansion gives
\(\mathcal Z(B)/\mathcal Z(0)=E_\mu\exp(i\sum_p n_pB_p)\).
At B=0, all W are positive and

\[
\frac{w'}w=-X,\qquad \frac{w''}w=\frac{X^2-1}{2}.
\tag{14}
\]

Taking a second derivative at one face gives the local identity

\[
E_\mu n_p^2=\frac{1-E_\pi X_p^2}{2}.
\tag{15}
\]

For the uniform 01 source B=s 1_(01), expanding the second derivative of
the product gives

\[
\operatorname{Var}_\mu\left(\sum_{p\parallel01}n_p\right)
=\frac12\sum_{p\parallel01}(1+E_\pi X_p^2)
 -E_\pi\left(\sum_{p\parallel01}X_p\right)^2.
\tag{16}
\]

Both means vanish by reversal. There are L^4 faces of this orientation,
and translation invariance identifies their local expectations. Combining
(15)-(16) with the normalization of G proves, for any 01 face p,

\[
\boxed{
\operatorname{Var}_\mu(G)+E_\mu n_p^2
+L^{-4}E_\pi\left(\sum_{q\parallel01}X_q\right)^2=1.}
\tag{17}
\]

This is the zero-momentum specialization of the source contact identity,
not a new phase theorem. In particular Var(G)<=1. Equations (4) and (11)
give the uniform checks

\[
0\le H_L\le1-25c_L,\qquad
H_L+R_L\le1.
\tag{18}
\]

They are upper bounds for the target; they supply no positive lower bound.

## 4. A positive empty-set bound within each electric sector

There is a sector-conditioned comparison that does follow from positivity,
with a restricted geometry. Choose coordinate 0 as transfer time. Let B_s
be any set of purely spatial plaquettes, with directions in {1,2,3}, at
one time slice. Then for every nonempty electric winding sector A=a,

\[
\boxed{\mu_L(n|_{B_s}=0\mid A=a)\ge2^{-|B_s|}.}
\tag{19}
\]

Here is a finite operator proof with all relevant positivity specified.
On one spatial slice, use orthonormal link-field characters labelled by r
in F_5^(spatial edges), and restrict to gauge-invariant labels partial r=0
mod 5. Choose the normalized temporal-link convolution, with exact Fourier
coefficients

\[
(c_0,c_1,c_2,c_3,c_4)=(2,1,0,0,1),\qquad
D_{rr}=\prod_l c_{r_l}.
\]

The positive support of D has r_l in {0,+1,-1}.

Let M be multiplication, in spatial link coordinates, by

\[
h(a)=\prod_{p\ \mathrm{spatial}}W((d_sa)_p)>0.
\]

The unnormalized transfer on the positive character support is

\[
T=D^{1/2}MD^{1/2}.
\tag{20}
\]

Expanding each spatial W as 2+zeta^f+zeta^-f gives the exact character
matrix entries

\[
M_{r,r'}=\sum_{\substack{m\in\{-1,0,1\}^{P_s}\\
                          \partial_s m=r-r'\pmod5}}
                   \prod_{p\in P_s}c_{m_p}.
\]

Thus M changes r only by a spatial plaquette boundary, and T preserves
the electric winding
a=sum_(x:x_1=0) r_(x,1) mod 5. Denote its orthogonal projector by P_a;
P_a commutes with T. The same preservation holds after any spatial
plaquette factors are removed.

Expanding a cyclic product of (20), the D factors supply the temporal
plaquette labels and the M factors supply the spatial labels. The
intermediate character constraints are precisely partial n=0 mod 5.
Inserting P_a selects A=a, giving the exact identity

\[
\operatorname{tr}(P_aT^L)=Q_a
:=\sum_{\substack{n\in\Omega_L\\A(n)=a}}\prod_{p\in P(K_L)}c_{n_p}
=2^{|P(K_L)|}\sum_{\substack{n\in\Omega_L\\A(n)=a}}
                      2^{-|\operatorname{supp}n|}.
\]

The common factor 2^(|P(K_L)|) cancels in conditional probability ratios.
This also directly identifies the chosen sector without assuming a
physical transfer interpretation.

An empty spatial plaquette keeps just the constant Fourier coefficient 2
of its W factor. Replace M by multiplication M_B with

\[
h_B(a)=h(a)\prod_{p\in B_s}\frac2{W((d_sa)_p)}.
\]

Since 0<W<=4,

\[
M_B\ge2^{-|B_s|}M,
\qquad T_B:=D^{1/2}M_BD^{1/2}\ge2^{-|B_s|}T
\tag{21}
\]

in the positive-operator order. Deleting the factors at that single slice
changes the sector trace to tr(P_a T_B T^(L-1)). Since
P_a T^(L-1) is positive semidefinite, tracing (21) against it gives

\[
\operatorname{tr}(P_aT_BT^{L-1})
\ge2^{-|B_s|}\operatorname{tr}(P_aT^L),
\]

which proves (19). No operator commutativity between T_B and T was used.

The scope restrictions matter. For a temporal plaquette, keeping only its
zero surface label replaces the diagonal factor (2,1,0,0,1) by
(2,0,0,0,0). On a character with label +1 or -1, the old diagonal entry is
positive and the new one is zero. There is therefore no positive constant
c for a direct operator inequality D_empty>=cD of this form. This breaks
that comparison method for the temporal faces of a charged 01 insertion;
it does not prove that their sector-conditioned empty probability has no
other lower bound. Nor is a product-order argument for deletions at several
different time slices asserted.

An unrestricted version of (19) for every plaquette set is actually false:
take B=Sigma_(0,0). Its emptiness forces A=0, so for a!=0 its conditional
empty probability is zero, whereas 2^(-|B|)=2^(-L^2)>0. This is a counterexample
inside the actual full measure. It does not decide an empty-set bound for
the particular contractible 21-face cup support.

One cannot obtain the unrestricted sector-conditioned empty-set estimate
merely by Fourier-projecting the canonical pointwise source comparison.
The projection onto A=a uses coefficients zeta^(-ka), whose real paired
coefficients can be negative. A pointwise positive comparison between the
twisted source sums does not preserve order under that projection. Equation
(19) works because it instead retains a positive sector projector in a
single-slice operator comparison.

## 5. A generic cosine-correlation shortcut fails

The following control concerns a different, explicitly specified carrier,
not the four-torus measure. Let a,b be independent F_5 variables with
probability W(f)/10, and set

\[
u=\cos(\theta(a+b)),\qquad v=\cos(\theta(a-b)).
\]

Character orthogonality gives
E exp(i theta a)=1/2 and E exp(2i theta a)=0, and the same for b.
Consequently

\[
E u=E v=\frac14,\qquad
E(uv)=\frac12E\{\cos(2\theta a)+\cos(2\theta b)\}=0,
\qquad
\boxed{\operatorname{Cov}(u,v)=-\frac1{16}.}
\tag{22}
\]

Thus positive local W and nonnegative local Fourier coefficients do not
alone imply a generic nonnegative covariance for these cosine forms.
The exact identity

\[
W(x+y)W(x-y)=4(\cos x+\cos y)^2
\]

with the continuous notation W(x)=2+2 cos x does not supply that missing
inequality. Equation (22) rejects this generic auxiliary lemma; it does
not disprove a separately specified correlation inequality for the actual
four-dimensional gauge model, or the desired lower bound for H_L.

## 6. Exact disposition of the primary target

**candidate-T:** the conditional-projection refinement (11) is a new
consequence of the existing canonical local theorem. The constant,
insertion and packing are inherited. The fluctuation that it certifies
lies within winding sectors, so it cannot be counted as a floor for H_L.

**candidate-T:** (19) is a genuine positive bound in each electric sector
for a spatial plaquette set at one time slice. The proved operator order
does not include the temporal plaquettes needed to insert 01 winding flux.

**Primary target NOT PROVED:** no lower bound for a nonzero sector's
probability together with its squared conditional mean, or for their sum
H_L, has been obtained. In particular, no nonvanishing sector-polarization
floor is inferred from positivity of partition sums, total variance,
convexity, or local fluctuations. A full-measure estimate preventing
cancellation between positive and negative integer lifts within the
relevant sector is still missing; neither the spatial deletion bound nor
the failed generic correlation lemma supplies it.

The result neither closes nor falsifies P1. P2, S7,
PHOTON-MASSLESS-PHASE, the continuum limit and the physical photon retain
their prior scopes. No scientific computation, numerical enumeration,
simulation, or extrapolation is part of this proof.
