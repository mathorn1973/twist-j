# Local charge-five noise and sector cancellation

**PUBLIC, NON-CANONICAL. Written proof candidate; separate review required.**

- Claim: C-PHOTON-SECTOR-CANCELLATION-AUDIT-N
- Owner: #1226 / A. M. Thorn
- Basis: Public Canon v92; public main
  `f94868276c77332430c5b476adc9a7bcf6bb747c`
- Status: candidate-T
- Scope: the specified finite measures, an all-volume conditional
  counterfamily, and full-measure parallel-cut identities
- No claim: a thermodynamic lower bound, P1, P2, S7, a continuum limit,
  apparatus, PHOTON-MASSLESS-PHASE closure or a physical photon

The result is deliberately restricted. A fixed relative dominance of the
positive part of a raw cut flux over its negative part cannot hold uniformly
over every admissible exterior condition. Actual local charge-five
fluctuations provide a counterfamily, even while the conditional sector
polarization stays exactly positive. This does not decide the corresponding
inequality in the unconditioned torus measure.

There is also a positive full-measure statement: averaging over parallel
cuts preserves every sector mean and can only reduce the absolute first
moment. The original sector label is retained throughout.

## 1. Fixed model and sector quantities

Let L be even and L>=4, and use the positively oriented cells of
K_L=(Z/LZ)^4. The finite surface measure is

\[
\Omega_L=\{n\in\{-1,0,1\}^{P(K_L)}:\partial n=0\pmod5\},
\qquad
\mu_L(n)=\mathfrak Z_L^{-1}2^{-|\operatorname{supp}n|}.
\tag{1}
\]

For t,s in Z/LZ, the seam Sigma_(t,s) contains the 01 plaquettes whose
basepoints satisfy x_0=t and x_1=s. Put

\[
F_{t,s}=\langle n,\Sigma_{t,s}\rangle,
\qquad F=F_{0,0},\qquad A=F\pmod5.
\tag{2}
\]

The sector congruence can be checked directly from the boundary equations.
Sum (partial n)_e over all positively directed 1-edges whose basepoints
satisfy x_0=t and x_1=s, with x_2,x_3 unrestricted. The 01 terms give
F_(t-1,s)-F_(t,s); the 12 and 13 terms telescope in the two periodic
transverse coordinates. Each summed boundary coefficient is divisible by
five. Similarly, summing over positively directed 0-edges at x_0=t,x_1=s
gives F_(t,s)-F_(t,s-1), with the 02 and 03 terms telescoping. Moving one
coordinate at a time therefore proves

\[
F_{t,s}\equiv F\pmod5.
\tag{3}
\]

For a probability law nu on this carrier, let p_a=nu(A=a) and
m_a=E_nu[F 1_(A=a)]. Omit empty sectors in

\[
\mathscr H(\nu)=\sum_{a:p_a>0}\frac{m_a^2}{p_a}.
\tag{4}
\]

For a reversal-invariant law, E_nu F=0 and (4) is the sector-polarization
quantity H=Var(E[F|A]) used by the existing sufficient P1 route. For a
non-centered law it is the uncentered second moment of the conditional
mean; we will not confuse the two quantities.

Write x_+=max(x,0), x_-=max(-x,0), and define the sector-1 parts

\[
u(\nu)=E_\nu[F_+1_{A=1}],\qquad
v(\nu)=E_\nu[F_-1_{A=1}].
\tag{5}
\]

Multiplying both by any common partition normalization gives the
unnormalized U,V and leaves v/u=V/U unchanged. The counterexample below
concerns the ratio, so no normalization convention is hidden in it.

## 2. All fillings of one four-cup support

Use the cubical convention

\[
\partial c_{abc}(x)=p_{bc}(x+e_a)-p_{bc}(x)
-p_{ac}(x+e_b)+p_{ac}(x)
+p_{ab}(x+e_c)-p_{ab}(x).
\tag{6}
\]

Fix x_0=x_1=0 and write p=p_01(x). Set

\[
u_1=-c_{012}(x),\quad u_2=c_{012}(x-e_2),\quad
u_3=-c_{013}(x),\quad u_4=c_{013}(x-e_3),
\qquad q_j=\partial u_j-p.
\tag{7}
\]

Each boundary in (7) has central-face coefficient +1. Thus q_j is the
five-face cube boundary with that central face removed, and

\[
\partial q_j=-\partial p.
\tag{8}
\]

The four q_j have disjoint face supports. Together with p they form the
21-face support S_x. The ternary field

\[
a_x=-p+\sum_{j=1}^4q_j
      =\partial\left(\sum_{j=1}^4u_j\right)-5p
\tag{9}
\]

has boundary -5 partial p. Its five 01 faces all have coefficient -1;
the other sixteen faces are cup side walls.

We now classify *every* filling of S_x when all incident outside
contributions are zero. At each noncentral edge of a cup, precisely two
support faces meet. Their mod-five boundary equation is an integer zero
equation, since its value lies between -2 and 2. These equations propagate
one common coefficient, relative to q_j, across its connected five-face
support. The central face has its independent ternary coefficient. Every
admissible filling therefore has the unique form

\[
n=-z p+\sum_{j=1}^4 b_jq_j,
\qquad z,b_1,b_2,b_3,b_4\in\{-1,0,1\}.
\tag{10}
\]

Conversely, (8) shows that the only remaining condition is

\[
s:=z+b_1+b_2+b_3+b_4\equiv0\pmod5.
\tag{11}
\]

The possible integer sums in (11) are 0,+5,-5. There are exactly

\[
1+\binom52\binom21+\binom54\binom42=51
\tag{12}
\]

tuples with sum zero: zero, two nonzero entries with opposite signs, or
four nonzero entries with two of each sign. The two other tuples are all
+1 and all -1. Hence the complete local law has 53 states. No local filling
has been discarded or fixed by an extra condition.

Each q_j contributes -1 to F, as does the central term with coefficient
z. Thus the local cut flux is

\[
X=-s\in\{0,+5,-5\}.
\tag{13}
\]

The local weight of (10) is

\[
2^{-|z|}t^{\sum_j|b_j|},\qquad t=2^{-5}.
\tag{14}
\]

The zero-sum coefficient of
(1+(y+y^-1)/2)(1+t(y+y^-1))^4 is

\[
Q_0=1+4t+12t^2+12t^3+6t^4
    =\frac{596163}{524288}.
\tag{15}
\]

For example, the four-cup polynomial has zero coefficient
1+12t^2+6t^4 and each first coefficient 4t+12t^3; the central coefficients
give (15). The two charged states each have weight
(1/2)t^4=2^-21. Therefore

\[
Z_{\rm cup}=Q_0+2\cdot2^{-21}
            =\frac{1192327}{2^{20}},
\qquad
\boxed{\Pr(X=+5)=\Pr(X=-5)=\frac1{2\cdot1192327}.}
\tag{16}
\]

These are analytical coefficient identities, not an executed enumeration.

## 3. Admissible exterior conditions and independent packing

Let P be the positive 01 coordinate plane at x_2=x_3=0. It is an integer
closed chain with L^2 faces and F(P)=1. Put

\[
h=\left\lfloor\frac{L-1}{3}\right\rfloor,
\qquad m=h^2,
\qquad x_{ij}=(0,0,2+3i,2+3j),\quad 0\le i,j<h.
\tag{17}
\]

The vertex box of S_(x_ij) is

\[
[0,1]\times[0,1]\times[1+3i,3+3i]\times[1+3j,3+3j].
\tag{18}
\]

All listed coordinates lie between 0 and L-1. Different boxes have
disjoint vertex sets; none meets P, whose transverse coordinates are both
zero. Thus no edge is incident to support faces from two different patches,
or to support faces from a patch and P. Periodicity creates no new vertex
identification because the boxes avoid transverse coordinate zero.

Let B_L be the union of the m patch supports. Define E_+ by fixing *only*
the faces outside B_L to the restriction of P; define E_- using -P instead.
Both events have positive probability in (1), since all patches can be
filled with zero. On E_+, each patch has precisely the zero-incident-exterior
constraints classified in section 2. The same is true on E_-.

The face weights factor, and each edge constraint contains remaining
variables from at most one patch. Consequently, under either conditional
law all m complete local laws (16) are independent and identical. If

\[
Y_i=X_i/5,\qquad T=\sum_{i=1}^mY_i,\qquad
v_0=E Y_i^2=\frac1{1192327},
\tag{19}
\]

then

\[
F=1+5T\quad\hbox{on }E_+,
\qquad F=-1+5T\quad\hbox{on }E_-.
\tag{20}
\]

In particular the respective sectors are exactly A=1 and A=4. These are
actual Gibbs conditional laws on the original torus carrier and weight,
not probabilities assigned to a few selected configurations. All 53
fillings of every patch remain present.

## 4. Exact moment growth and failure of uniform relative dominance

The variables Y_i are independent, centered, symmetric and in {0,+1,-1}.
Since E Y_i^4=E Y_i^2=v_0, expanding finite sums gives

\[
E T^2=mv_0,\qquad
E T^4=mv_0+3m(m-1)v_0^2.
\tag{21}
\]

Holder's inequality applied to |T|^(2/3)|T|^(4/3) gives
E T^2 <= (E|T|)^(2/3)(E T^4)^(1/3). Therefore

\[
\boxed{
E|T|\ge
\frac{(E T^2)^{3/2}}{(E T^4)^{1/2}}
=\frac{mv_0}{\sqrt{1+3(m-1)v_0}}.}
\tag{22}
\]

No limiting distribution or central limit theorem is used. For the
symmetric integer T, pairing its values t and -t also gives

\[
R_m:=E|1+5T|=5E|T|+\Pr(T=0)
\ge\frac{5mv_0}{\sqrt{1+3(m-1)v_0}}\longrightarrow\infty.
\tag{23}
\]

Under nu_+=mu_L(.|E_+), all mass is in sector 1 and E F=1. Equations
(5) and (23) imply

\[
u(\nu_+)=\frac{R_m+1}{2},\qquad
v(\nu_+)=\frac{R_m-1}{2},\qquad
\boxed{\frac{v(\nu_+)}{u(\nu_+)}
=\frac{R_m-1}{R_m+1}\longrightarrow1.}
\tag{24}
\]

Since m tends to infinity with the even torus size, (24) proves the
following restricted negative statement:

> There is no constant kappa<1 and no finite volume threshold for which
> v(nu)<=kappa u(nu) holds for every sufficiently large even torus and
> every admissible exterior-conditioned sector-1 law nu. The explicit
> exterior conditions E_+ already violate that assertion.

For any fixed kappa<1, the exact criterion
R_m>(1+kappa)/(1-kappa), together with (23), supplies a finite violating
size. This is not a failure of a measured finite-size trend.

The result does **not** prove that v(mu_L)/u(mu_L) tends to one. No lower
bound on mu_L(E_+) is supplied. A full-measure inequality may exploit the
relative weights of exterior conditions, and that question remains open.

## 5. The conditional polarization can remain exactly one

Now let nu_*=mu_L(.|E_+ union E_-). Global reversal preserves (1), exchanges
the two events, and preserves each cup law. Thus their weights are exactly
equal, and nu_* has the representation

\[
F=\varepsilon+5T,
\qquad \Pr(\varepsilon=+1)=\Pr(\varepsilon=-1)=\frac12,
\qquad \varepsilon\ \hbox{independent of }T.
\tag{25}
\]

Here E F=0, p_1=p_4=1/2, the two conditional means are +1,-1, and

\[
\boxed{\mathscr H(\nu_*)=H(\nu_*)=1.}
\tag{26}
\]

Both sector-1 parts in (24) are halved under nu_*, so their ratio still
tends to one. Fixed relative sign dominance is therefore stronger than
positive sector polarization even within these actual conditioned Gibbs
ensembles.

There is no conflict with a sector cap obtained from the *unconditioned*
binary-pair Gram representation. That representation first chooses a
boundary fiber and then draws the two binary surfaces independently with
the same uniform law. Conditioning on the exterior **difference** being
+P or -P restricts the pair jointly. The conditional pair law is no longer
that mixture of independent identical fiber draws. A cap such as
p_1,p_2<=1/4, or a consequence such as H>=(8/5)D derived from that full-fiber
law, cannot be transported to nu_*. Equation (25) explicitly gives p_1=1/2.
No such full-measure cap or prefactor is promoted by this note. The separate
cap argument is in
`notes/C-PHOTON-BINARY-FIBER-SECTOR-CAP-N/PROOF.md`, section 2, published
through #1225 and PR #1227 at merge
`5daf8df697dc480227d7db5fe2c678f48c14040d`. That note remains NON-CANONICAL;
its publication does not enlarge the conditional law considered here.

## 6. Parallel-cut averaging in the full measure

Return now to the unconditioned measure mu_L and define

\[
G=\frac1{L^2}\sum_{t,s}F_{t,s}
 =\frac1{L^2}\sum_{p\parallel01}n_p.
\tag{27}
\]

There are L^2 seams, each with L^2 plaquettes. This explains both the
normalization and the fact that G need not be an integer. In everything
below the sector variable is still A=F mod 5, never G mod 5.

Translations preserve mu_L and, by (3), preserve the event A=a. They send
any one of the seams to any other. Consequently, for every nonempty sector,

\[
E[F_{t,s}\mid A=a]=E[F\mid A=a],
\qquad E[|F_{t,s}|\mid A=a]=E[|F|\mid A=a].
\tag{28}
\]

Taking the mean in (27), and then using the pointwise triangle inequality,
proves

\[
\boxed{E[G\mid A]=E[F\mid A],\qquad
E[|G|\mid A]\le E[|F|\mid A].}
\tag{29}
\]

In particular the full-measure H is exactly preserved if its conditional
mean observable is written using G and the same A. For each sector define

\[
u_{X,a}=E[X_+1_{A=a}],\quad
v_{X,a}=E[X_-1_{A=a}],\qquad X\in\{F,G\}.
\tag{30}
\]

Using X_+=(|X|+X)/2 and X_-=(|X|-X)/2 in (29) yields

\[
u_{G,a}\le u_{F,a},\qquad v_{G,a}\le v_{F,a},\qquad
u_{G,a}-v_{G,a}=u_{F,a}-v_{F,a}=m_a.
\tag{31}
\]

If m_a>0, then u_(G,a)>0 and the function (r-m_a)/(r+m_a) increases with
r>=m_a. Applying it to r=E[|X|1_(A=a)] gives

\[
\boxed{\frac{v_{G,a}}{u_{G,a}}
\le\frac{v_{F,a}}{u_{F,a}}\quad(m_a>0).}
\tag{32}
\]

No assertion of strict improvement, a positive m_a, or a volume-uniform
bound below one is part of (32). For negative m_a the displayed direction
must not be used. These are full-measure identities and inequalities;
they do not assume the special exterior conditions of sections 3-5.

## 7. Exact removal of the sign problem in the counterfamily

The conditioned ensembles are not translation invariant, so (29) is not
invoked for them. Their G can instead be calculated directly. The plane
contributes epsilon L^2 to the total 01 sum. Every cup contributes its cut
flux 5Y_i to that same total sum. Thus on nu_*

\[
G=\varepsilon+\frac{5T}{L^2}.
\tag{33}
\]

Since |T|<=m and m=floor((L-1)/3)^2<L^2/9,

\[
\left|\frac{5T}{L^2}\right|<\frac59.
\tag{34}
\]

Therefore G has sign epsilon for every allowed filling, not only with high
probability. In sector 1, exactly

\[
u_{G,1}(\nu_*)=\frac12,\qquad
v_{G,1}(\nu_*)=0,
\tag{35}
\]

whereas v_(F,1)/u_(F,1) tends to one. The sector means and H remain the
same in this particular example. Also

\[
\operatorname{Var}(G\mid\varepsilon)
=\frac{25mv_0}{L^4}\longrightarrow0,
\tag{36}
\]

which separately quantifies the suppression of this local fluctuation.
Neither (34), (35), nor (36) is asserted for the full torus measure.

## 8. Disposition and remaining target

**candidate-T:** the universal claim across all exterior conditions is
false by (24), including a reversal-symmetric conditional family with H=1.
This is a restricted mathematical obstruction, not a negative disposition
of P1 or of either proposed full-measure bound.

**candidate-T:** (29)-(32) give an exact full-measure replacement of the
raw cut observable by the parallel-cut average, preserving the sector
means while decreasing both signed-part magnitudes. The original sector
label must remain in the statement.

**O:** a positive thermodynamic floor for

\[
H_L=\sum_{a:p_a>0}p_a\{E_{\mu_L}[G\mid A=a]\}^2
\tag{37}
\]

still needs a model-specific estimate. No lower bound for p_a or these
conditional means follows from the averaging identity. In particular the
second proposed counting estimate U_L^2>=c N_L Q_(L,1) has neither been
proved nor disproved. A future sign-dominance attack should concern G with
the same sector variable and should not assume uniformity over arbitrary
exteriors without a new argument.

## Source and review boundary

All new conclusions above rest on the written arguments. At the declared
main pin, the four-cup boundary convention is also present in
`notes/C-PHOTON-COMPONENT-DELETION-ACTIVITY-N/PROOF.md`, section 4.
The general factorization for edge-separated conditional patches is
discussed in `notes/C-PHOTON-BCHI-DIRECT-BOUND-N/NEUTRAL-SUM.md`, section C.
Those notes have their own NON-CANONICAL scopes. Their historical finite
audits are not new runs or independent confirmations of this item.

Review must check the completeness of (10), all 53 weights, the packing
including periodic seams, the exact exterior conditioning, the moment
interpolation, and the distinction between the full law and conditioned
laws. It must separately check the normalization of G and preservation of
the original sector event under translations. No scientific execution,
finite extrapolation, or blind-verifier claim accompanies this proof.
