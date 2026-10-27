# Exact finite-center source functions and a bounded U(1) flux reader

**PUBLIC-source, NON-CANONICAL; candidate-T written proof. No authority.**
Candidate C-PHOTON-U1-FINITE-CENTER-N, issue #1715.
Author: A. M. Thorn. Date: 2026-10-23. Apache-2.0.

The finite mathematical identities below concern an explicitly selected
bandlimited lattice action. They do not establish a phase or select this
action from the native TWIST-J evolution. The local incidence bound is
inherited from #1196; its extension to complete source functions, global
sharpness and the exact finite-center reader are the present scope.

## 1. Finite character integration, with no topological restriction

Let B be an integer matrix from face chains to edge chains on a finite cell
complex K. Write d=B^T. On every edge integrate normalized Haar measure,
either dA/(2pi) on U(1) or the uniform average over the N roots of unity.
All boundary edges are integrated too. Do not divide by gauge orbits.
For a real face source a and an integer edge insertion J, define

\[
 Z_G[a,J]=\mathbb E_{A\in G^E}
 e^{i\langle J,A\rangle}
 \prod_{p\in P}\{2+2\cos((dA)_p+a_p)\}.
\]

Angles represent group elements; integer J makes the insertion well-defined.
For N=2 the two Fourier modes +1 and -1 coincide on the group, but they are
still two terms of the displayed finite polynomial and must both be kept.
The argument does not require primal weights to be strictly positive.

Expand each factor as 2+e^{i((dA)_p+a_p)}+e^{-i((dA)_p+a_p)}.
An exponent choice n in {-1,0,1}^P has coefficient
2^{|P|-|supp n|}, source e^{i<n,a>}, and edge character Bn+J.
Orthogonality on each independent edge gives

\[
\begin{split}
Z_{U(1)}[a,J]&=\sum_n2^{|P|-|\operatorname{supp}n|}
 e^{i\langle n,a\rangle}\mathbf1_{Bn+J=0},\\
Z_{\mathbb Z_N}[a,J]&=\sum_n2^{|P|-|\operatorname{supp}n|}
 e^{i\langle n,a\rangle}\mathbf1_{Bn+J\equiv0\pmod N}.
\end{split}                                                    \tag{1}
\]

Both are finite identities. No limit interchange, gauge fixing, dual
potential or representation n=boundary of a three-chain is used. In
particular every nontrivial integer homology class present in K is retained.

If

\[
N>\max_e\left(\sum_p|B_{ep}|+|J_e|\right),                    \tag{2}
\]

then each integer (Bn+J)_e has absolute value strictly below N. Divisibility
by N is consequently equivalent to equality to zero. Equations (1) agree
term by term for every real a, not only at a=0.

More generally, a finite Fourier weight with face-dependent support
|n_p|<=M_p obeys the same argument with sum_p |B_ep| M_p in (2).
The coefficients need not be positive for this algebraic equality. Positive
probability interpretations require their own hypotheses.

## 2. The four-dimensional bridge and inherited input

For an ordinary D-dimensional cubical lattice each oriented edge has two
incident plaquettes in each transverse direction, at most 2(D-1) in all.
This is the local bound already proved in
[C-CURRENT-PRIME-GATE-N](../C-CURRENT-PRIME-GATE-N/PROOF.md), sections 1-2,
for the ternary current carrier. Applying it to (1) gives in D=4

\[
\boxed{Z_{\mathbb Z_N}[a,0]=Z_{U(1)}[a,0]\quad(N\ge7).}       \tag{3}
\]

It holds for finite free boxes with all edges summed, and for rectangular
periodic tori with every side length at least two and the usual cell
incidences. For open boundary links fixed to prescribed values the summed
edge constraints change; that is not the present boundary contract.

The proof covers composite N too. It gives equality of the finite source
functions and hence of their source derivatives, wherever a chosen quotient
or logarithm is defined. At zero source Z>0, so logarithmic derivatives
are well-defined in a neighborhood of zero. It does not give a bijection
between continuous and finite-group link fields or equality of arbitrary
link observables. For a nonzero insertion use (2) again.

The same bridge can be seen in the binary pair representation from #1111.
Write n=S-T with S,T in {0,1}^P. Each nonzero coordinate has one lift and
each zero coordinate two. Thus the multiplicity is exactly
2^{|P|-|supp n|}, and the partition counts ordered pairs with equal boundary
in the corresponding group. This is attribution of the inherited pair
identity, not a new Born-law or quantum-measure derivation.

## 3. Seven is globally sharp on even four-tori

Fix an even L>=4 and x in (Z/LZ)^4. Set

\[
s(x)=(-1)^{x_1+x_2+x_3},\qquad
j_0(x)=s(x),\qquad j_1=j_2=j_3=0.
\]

This integer current is nonzero and conserved, since s is independent of
x_0. For any N in {2,3,4,5,6}, choose integers a_1,a_2,a_3 in {0,1,2}
with sum N. Define

\[
 f_0(s)=0,\qquad f_1(s)=(1+s)/2,\qquad f_2(s)=s,
 \qquad n_{0\nu}(x)=f_{a_\nu}(s(x)),
\]

and set the other three plaquette orientations to zero. All n are ternary.
At a direction-zero edge,

\[
(Bn)_0(x)=\sum_{\nu=1}^3
 [n_{0\nu}(x)-n_{0\nu}(x-e_\nu)]
=\sum_{\nu=1}^3 a_\nu s(x)=N j_0(x).
\]

At a transverse edge the two contributions differing by an x_0 translation
cancel. Therefore Bn=N j on every edge. Half the sites have either parity,
so a coefficient a_nu=1 occupies L^4/2 faces, while a_nu=2 occupies L^4.
Hence

\[
|\operatorname{supp}n|=N L^4/2.                            \tag{4}
\]

Every U(1) term at a=0 is also a Z_N term. The exhibited additional term
has positive integer weight. Consequently

\[
\boxed{Z_{\mathbb Z_N}[0,0]>Z_{U(1)}[0,0]\quad(2\le N\le6).} \tag{5}
\]

Thus (3)'s threshold is sharp for the full stated lattice class, not only
for an unconstrained local edge star. No corresponding claim that every
individual smaller finite box distinguishes these models is made.

For the N=6 configuration, Bn=6j. Set the inserted current J=j. Then
Bn+J=7j, so this term is admitted in the Z7 inserted numerator and excluded
in U(1). All U(1) terms are still admitted and all coefficients at a=0
are positive. The inserted numerators differ strictly; their denominators
agree by (3). This shows that N>=8 is sharp for the full insertion class
||J||_infinity<=1. The insertion is a product of signed winding loops,
not one simple contractible Wilson loop. More generally, J=M j gives the
same obstruction at N=6+M for the full bounded-current class M>=1.

These witnesses were derived analytically and disclosed in the frozen
preregistration before any finite execution. They are not blind discoveries.

## 4. Exact topology of the flux source

On a rectangular periodic torus fix mu<nu. Let S_(u,v) be the two-cochain
equal to one on mu,nu plaquettes with x_mu=u, x_nu=v, and zero elsewhere.
For an integer-closed n define

\[
 W_{\mu\nu}(n)=\langle n,S_{(0,0)}\rangle.
\]

This is integer. To prove independence of stack position, sum the
direction-nu boundary equation Bn=0 over all coordinates transverse to
mu,nu. All differences in transverse directions telescope. The remaining
identity equates the sums at adjacent x_mu. The direction-mu equation
similarly equates adjacent x_nu. Thus all L_mu L_nu stacks have the same
pairing. Summing them gives

\[
\sum_x n_{\mu\nu}(x)=L_\mu L_\nu W_{\mu\nu}(n).             \tag{6}
\]

A fundamental mu,nu sheet wrapping both directions with other coordinates
fixed is an allowed ternary integer cycle and pairs to one. An elementary
cube boundary pairs to zero. W is a surface winding number. It is not the
principal-lift magnetic-flux diagnostic of a primal Z7 configuration.

In (1), the stack source alpha S_(0,0) and the uniform source alpha/(L_mu
L_nu) on all mu,nu faces have identical pairing with every allowed n.
Their entire source functions therefore agree in U(1) and, by (3), in Z_N
for N>=7. This is a complete nonlinear source identity. It must not be
transferred to Z5, where Bn=5j may be nonzero and (6) need not hold.

At zero source the positive dual measure is proportional to
2^{-|supp n|} on all integer-closed ternary n. Reversal n->-n gives E W=0.
Hence

\[
\frac{Z(\alpha S)}{Z(0)}=\mathbb E e^{i\alpha W},\qquad
F(\alpha)=-\log\frac{Z(\alpha S)}{Z(0)},\qquad
\boxed{F''(0)=\operatorname{Var}(W).}                       \tag{7}
\]

At every finite torus this variance is strictly positive: zero and both
oriented fundamental sheets have positive weights. It may tend to zero
as the torus grows. Strict finite positivity is not a massless-phase proof.
The explicit two-dimensional example in section 7 makes that distinction
quantitative.

## 5. An exact bounded reader on positive Z7 configurations

Let x=2cos(2pi/7). Its minimal polynomial is x^3+x^2-2x-1=0; the desired
root lies in (6/5,5/4), since the polynomial has opposite signs there and
strictly positive derivative on this interval. Consequently all four weights

\[
w_0=4,\quad w_{\pm1}=2+x,\quad w_{\pm2}=x^2,\quad
w_{\pm3}=3-x-x^2                                             \tag{8}
\]

are strictly positive. For the last one the interval gives w_3>3/16.
All arithmetic can be carried out in Q(x) using rational triples.

For a real angle theta write

\[
 X(\theta)=\frac{\sin\theta}{1+\cos\theta}=\tan(\theta/2),
 \qquad s(\theta)=-\log(2+2\cos\theta).
\]

At the seven group values there is no theta=pi. Thus s'=X and
s''=(1+X^2)/2 are finite on the entire discrete carrier. Put

\[
r=\frac{2-x}{2+x}=\tan^2(\pi/7),\quad
G=(0,1,(2+x)/x,(1+x)/(x-1),-(1+x)/(x-1),-(2+x)/x,-1).
\]

Tangent addition, or direct substitution in the minimal polynomial, gives
X(2pi k/7)=sqrt(r)G(k) for all residues k. No square root is needed for
the quadratic reader.

Let V be the number of vertices and A=L_mu L_nu. Under the uniform source
alpha/A the derivative of the complete action is sum_x X(f_x)/A.
The normalized measure at alpha=0 is invariant under charge conjugation,
so this derivative has expectation zero. Differentiating the finite
partition sum twice yields

\[
\boxed{
 h_{\mu\nu}=F''(0)=\mathbb E_{\mu_7}
 \frac{V/2+(r/2)\sum_x G(f_x)^2-r(\sum_xG(f_x))^2}{A^2}.
}                                                            \tag{9}
\]

Here f=dA modulo seven is the actual primal curl. Formula (3) identifies
this mean with the U(1) flux response in (7). The reader is a finite
Q(x)-valued function of each finite Z7 configuration. It can be negative
on individual configurations; only its full expectation is the variance.
On an isotropic four-torus A^2=V. This simplification does not apply in
two dimensions. Averaging the six orientations uses fixed equal weights.

The stack-source reader similarly uses the number of faces in that stack,
its score sum and its score-square sum, with no A^-2 prefactor. Its full
expectation agrees with (9), but the two configuration-wise readers need
not agree. In particular the source identity is not a coupling between
individual primal configurations and individual dual windings.

Seven discrete twist samples determine W modulo seven and do not generally
determine Var(W). Formula (9) avoids that aliasing: it is an exact analytic
source derivative, not a reconstruction from seven sampled twist values.

## 6. Exact local transitions are possible, but do not solve mixing

For a fixed link all other links give six staple offsets. If the link value
is a in Z7, its conditional unnormalized mass is a product of six weights
from (8), with orientation signs absorbed using w_k=w_-k. Every mass is
strictly positive. The 924 possible offset-count vectors cover all local
backgrounds up to permutation. Their seven candidate masses lie in Z[x].

A cubic-field sign can be decided exactly by refining a rational isolating
interval for x. A nonzero rational polynomial of degree below three cannot
vanish at x. An exact lazy categorical draw can compare dyadic bounds on
an ideal uniform number with the exact cumulative probability intervals.
It terminates almost surely; equality with a cut has probability zero.
This supplies exact transition probabilities without floating-point cuts.

Each single-link heat bath satisfies detailed balance and leaves the full
finite measure invariant. A fixed systematic sweep preserves that measure
by composition, but is not claimed reversible. Because every local value
has positive probability, successive sweeps can reach any link configuration
and have positive self-loop probability. Hence the finite chain is
irreducible and aperiodic. No quantitative or volume-uniform mixing time
follows. Seeded pseudorandom execution is engineering evidence, not a proof
of an ideal independent-random-bit source.

In the closed-surface representation, adding only cube boundaries preserves
all W. In the primal representation, adding flat holonomies preserves every
plaquette and therefore is not a magnetic-sector transport test. These
facts must be built into any later measurement qualification. A frozen
sector or too-short trajectory may return a wrong equilibrium mean even
when every individual arithmetic decision is exact.

## 7. Exact small-volume controls and a vanishing-response counterexample

For a single plaquette disk, integrating any boundary edge forces n=0,
so the normalized Haar partition is 2. For the six-face boundary of one
three-cube, each edge condition equates the two oriented neighboring face
values. Connectedness leaves n=0 or either oriented full boundary, giving
Z=2^6+2=66. These are normalization and contractible-cycle controls.

On a connected periodic two-dimensional torus with A=L_1 L_2 plaquettes,
integer closure forces every n_p to have the same value. The only three
states are n=0 and the two fundamental wrapping sheets. Consequently

\[
 Z(\alpha)=2^A+2\cos\alpha,\qquad
 h=\frac{2}{2^A+2}.                                         \tag{10}
\]

The two-dimensional edge degree is two, so Z_N reproduces this source
function for every N>=3. In particular Z7 must pass it exactly. If the
dual sum is restricted to boundaries, the two winding states disappear,
producing the false h=0. For the real full measure h>0 at every finite
size yet h tends to zero as A grows. Thus finite positivity alone is a
demonstrably insufficient phase criterion.

For an independent primal check, every Z7 plaquette assignment with
sum_p f_p=0 modulo seven is realized by the same number of periodic link
assignments. One may prove surjectivity by solving successively along rows
and columns; alternatively the image of d in the cellular torus complex
has codimension one, with its sole condition the total two-cycle pairing.
All fibers have equal size because d is a homomorphism. Thus the normalized
link integral is exactly the uniform average over 7^(A-1) constrained
plaquette assignments. This retains the Haar factor, not a new independent-
plaquette approximation.

Enumeration at A=4 and 6 can therefore check the partition, both readers
and a shifted single plaquette at alpha=2pi/7. The shifted partition must
be 2^A+x. These exact finite tests audit implementation, not the universal
proof or the four-dimensional thermodynamic limit by enumeration.

## 8. What has been reduced, and what remains open

For this exact bandlimited weight the selected finite-source U(1) problem
can be studied without an angular discretization error using positive Z7
link weights and the reader (9). This is a finite-source and observable
bridge, not a theorem importing another Z7 action's phase diagram.

The following remain separate obligations: practical sampling of the full
measure at growing volume; the selected thermodynamic limit and uncertainty
control; a nonvanishing long-wavelength/flux-response theorem with its
correct observable consequences; stability or comparison back to Z5; the
TWIST-J action-carrier and physical-photon bridges. Neither (3), (7), (9)
nor exact transition arithmetic discharges those obligations.
