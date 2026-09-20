# A selected bipartite measurement law

PUBLIC; candidate-T; NON-CANONICAL. Written proof for
P-QDD-SELECTED-BIPARTITE-LAW-1, lock
https://github.com/mathorn1973/twist-j/issues/1095.
A. M. Thorn; original text, Apache-2.0.

These are conditional mathematical statements about the selected effective
theory ETH-QDD-1 and the additional composition and preparation choices in
MODEL.md. Tensor composition, the physical preparation of the specified
entangled state, independent settings and the occurrence law are inputs.
They are not deductions from J or the deterministic native update U. The
channel arguments are finite-dimensional quantum mathematics. The exact
five-setting specialization and its complete comparison table are proved
below without a numerical approximation or an appeal to a finite run.

## 1. Source coordinates and the five existing measurements

On each wing use S=C^4 and the positive metric

\[
 G=I_4-\frac15\mathbf1\mathbf1^T,
 \qquad G^{-1}=I_4+\mathbf1\mathbf1^T,
 \qquad X^\sharp=G^{-1}X^*G.
\]

The eigenvalues of G are 1,1,1,1/5. A density is an endomorphism rho
with rho^sharp=rho, G rho positive semidefinite and ordinary trace one.
Changing coordinates by the real symmetric positive matrix F=G^(1/2)
sends rho to F rho F^(-1), an ordinary density. This identifies all the
positivity, trace and complete-positivity statements here with their usual
orthonormal-coordinate meanings. The joint metric is H=G tensor G;
the corresponding coordinate change is F tensor F. Finite local memories
can be adjoined with their declared positive metrics. All partial traces
below are partial traces of endomorphisms, or equivalently ordinary partial
traces after this coordinate change, not partial traces of an unconverted
covariance matrix.

Let

\[
 u_0=\frac{\sqrt5}{2}\mathbf1,
 \qquad u_k=-\frac{\sqrt5}{2}e_k\quad(1\le k\le4),
 \qquad P_k=u_ku_k^TG,
 \qquad Q_k=I-P_k.
\]

Here e_1,...,e_4 are the displayed source-coordinate vectors. Directly,

\[
 \langle u_k,u_l\rangle_G=
 \begin{cases}1&k=l,\\-1/4&k\ne l,\end{cases}
 \quad \sum_ku_k=0,
 \quad \sum_kP_k=\frac54I,
 \quad \operatorname{tr}(P_kP_l)=
 \begin{cases}1&k=l,\\1/16&k\ne l.\end{cases}             \tag{1}
\]

Thus P_k and Q_k are G-orthogonal projectors of ranks one and three.
They are precisely the five marked settings of ETH-QDD-1. No continuous
rotation, outcome splitting or additional setting is admitted to the
comparison below. LOW has effect P_k and HIGH has effect Q_k. Write
E_(k,L)=P_k, E_(k,H)=Q_k. The adopted local instrument is

\[
 \mathcal I_{k,o}(X)=E_{k,o}XE_{k,o}.                      \tag{2}
\]

Its branches are completely positive, their sum preserves trace, and
the branch following a positive-probability outcome is normalized by that
probability. The selection of (2), including its coarse HIGH post-state,
was the subject of P-QDD-SELECTED-MEASUREMENT-LAW-1; it remains an explicit
conditional input here. A fine measurement within HIGH is a different
instrument.

## 2. The selected aligned entangled preparation

Fix the same marked real source basis on both wings. For a matrix C define

\[
 \operatorname{vec}(C)=\sum_{i,j=1}^4 C_{ij}e_i\otimes e_j.
\]

Then (A tensor B)vec(C)=vec(A C B^T). Select

\[
 |\Phi\rangle=\frac12\operatorname{vec}(G^{-1}),
 \qquad \rho_\Phi=|\Phi\rangle\langle\Phi|_H,
 \qquad \langle\Phi|_H=\Phi^*H.                          \tag{3}
\]

Since F is real and symmetric,

\[
 (F\otimes F)|\Phi\rangle
 =\frac12\operatorname{vec}(FG^{-1}F^T)
 =\frac12\operatorname{vec}(I).
\]

Consequently Phi has H-norm one, rho_Phi is a rank-one density, and
both reduced densities are I_4/4. The four nonzero Schmidt coefficients
are 1/2. This is a maximally entangled state of the two selected
four-dimensional sources, not a product of native checkpoint points.

The real alignment matters. The identity used below pairs an operator on
one wing with a transpose on the other in the aligned orthonormal basis.
There is no unannounced assertion that the same formula holds after an
arbitrary independent complex change of physical setting on one wing.
The five displayed G-projectors become real symmetric projectors
\(\widetilde P_k=FP_kF^{-1}\), so their transpose is themselves.

For any real symmetric orthonormal-coordinate operators A,B,

\[
 \langle\operatorname{vec}(I)/2|
 A\otimes B|\operatorname{vec}(I)/2\rangle
 =\frac14\operatorname{tr}(AB^T).
\]

Applying this identity to the projectors gives

\[
 p_\Phi(L,L\mid x,y)
 =\operatorname{tr}[(P_x\otimes P_y)\rho_\Phi]
 =\frac14\operatorname{tr}(P_xP_y).                       \tag{4}
\]

Both LOW marginals are 1/4. Subtraction from the marginals and total mass
one yields the entire 5 by 5 table of binary distributions:

| Setting relation | LOW,LOW | LOW,HIGH | HIGH,LOW | HIGH,HIGH |
| --- | ---: | ---: | ---: | ---: |
| x=y | 1/4 | 0 | 0 | 3/4 |
| x differs from y | 1/64 | 15/64 | 15/64 | 33/64 |

Every entry is nonnegative and each row sums to one. There are five
diagonal setting pairs and twenty ordered off-diagonal pairs. In particular,

\[
 \sum_b p_\Phi(L,b\mid x,y)=\frac14,
 \qquad
 \sum_a p_\Phi(a,L\mid x,y)=\frac14                        \tag{5}
\]

for all settings. These are both operational no-signalling marginal
equalities; they are not yet a claim about a physical communication speed.

## 3. Normalized joint instruments and order independence

For a general joint density rho, define

\[
 K_{xy}^{ab}=E_{x,a}\otimes E_{y,b},\qquad
 \rho_{xy}^{ab}=K_{xy}^{ab}\rho K_{xy}^{ab},\qquad
 p_\rho(a,b\mid x,y)=\operatorname{tr}(\rho_{xy}^{ab}).     \tag{6}
\]

Each branch is positive. Completeness of the two local projectors gives
\(\sum_{a,b}(K_{xy}^{ab})^\sharp K_{xy}^{ab}=I\), hence
\(\sum_{a,b}p_\rho(a,b\mid x,y)=1\). At positive branch weight, the
normalized post-state is rho_(xy)^(ab)/p_rho(a,b|x,y). At zero weight,
positivity implies the branch operator is zero; it has no normalized
successor and is never selected. A zero raw preparation remains typed
ZERO_SUPPORT and is not a trial with a fabricated outcome.

The two local branch operations commute because they act on different
tensor factors. Their order therefore gives the same unnormalized joint
branch and the same record distribution. This is a tensor-product
statement, not the deduction of a spacetime ordering or a Lorentzian
separation from the native counter.

For a product preparation rho_A tensor rho_B, (6) factorizes exactly:

\[
 p(a,b\mid x,y)
 =\operatorname{tr}(E_{x,a}\rho_A)
  \operatorname{tr}(E_{y,b}\rho_B).                        \tag{7}
\]

For a fixed separable mixture, its mixture label gives a setting-independent
Bell-local decomposition. The entangled source (3) is not assigned such a
decomposition by this observation.

## 4. The complete Bell-local response class

Freeze setting spaces X=Y={0,1,2,3,4}, outcomes {L,H}, and a normalized
probability space (Lambda,mu). A Bell-local model in the comparison class
has measurable normalized local response kernels alpha(a|x,lambda) and
beta(b|y,lambda), and

\[
 p(a,b\mid x,y)=
 \int_\Lambda\alpha(a\mid x,\lambda)
                  \beta(b\mid y,\lambda)\,d\mu(\lambda),\qquad
 \mu(\cdot\mid x,y)=\mu(\cdot).                          \tag{8}
\]

The hidden variable can contain any setting-independent shared preparation
information, common randomness, earlier records, or refinement of those
data. No finite bound on Lambda is assumed. Conditions (8) are the named
factorization and measurement-independence premises. The actual effective
quantum preparation is fixed independently of the chosen settings in this
comparison; its physical preparation and setting-selection mechanism are
separate declared choices, not consequences of a marginal calculation.

There are exactly 2^5 deterministic response strings on each wing and
2^10=1024 deterministic joint vertices. These vertices generate the whole
class (8), not merely its finite-lambda part. To see this directly, for
strings s=(s_0,...,s_4), t=(t_0,...,t_4), set

\[
 w(s,t)=\int_\Lambda
       \prod_{x=0}^4\alpha(s_x\mid x,\lambda)
       \prod_{y=0}^4\beta(t_y\mid y,\lambda)\,d\mu(\lambda).
\]

These weights are nonnegative, sum to one, and their marginal at a fixed
x,y reproduces (8). This is a mathematical refinement of stochastic
responses, not an assertion that unperformed measurements have quantum
outcomes. Conversely any convex combination of the vertices is a model
(8). Thus a linear bound on all 1024 vertices is a bound on every model
in the declared complete response class.

Define the five-setting Bell functional

\[
 \mathcal B(p)=2\sum_{k=0}^4p(L,L\mid k,k)
              -\sum_{k\ne l}p(L,L\mid k,l).              \tag{9}
\]

The second sum contains all twenty ordered pairs. At a deterministic
vertex let A and B be the subsets of settings assigned LOW, and put
a=|A|, b=|B|, c=|A intersection B|. The diagonal sum is c and the
off-diagonal sum is ab-c, so

\[
 \mathcal B=3c-ab.
\]

Interchanging the wings if necessary, assume a<=b. Since c<=a,
\(3c-ab\le a(3-b)\). For b=0 this is zero; for b=1 it is at most
2; for b=2 it is at most 2; and for b>=3 it is nonpositive. Therefore

\[
 \boxed{\mathcal B(p)\le2\quad\hbox{for every model (8).}} \tag{10}
\]

The bound is attained when both LOW sets are the same singleton or the
same two-element subset. It does not assume perfect synchrony, fair
sampling, equal marginals, or any additional symmetry of p.

For (4),

\[
 \boxed{\mathcal B(p_\Phi)=\frac52-\frac{20}{64}
                            =\frac{35}{16}>2.}           \tag{11}
\]

The excess is 3/16. Thus the entire table has no representation (8), even
with arbitrary setting-independent stochastic refinements. One may retain
measurement independence in the chosen quantum model, in which case the
Bell-local factorization cannot be imposed. This does not identify a
physical influence, a preferred time order, or a signalling mechanism.

There is a useful independent exact contradiction on the ideal table.
Perfect equal-setting agreement forces equal predetermined responses in
any deterministic refinement. If N is their number of LOW settings, then
EN=5/4 and E[N(N-1)]=20/64=5/16. Hence Var(N)=0 while EN=5/4 is not an
integer. Inequality (10) is stronger as an operational witness because it
requires no perfect-agreement premise.

## 5. Exact optimum for the five frozen local measurements

Let v_k=u_k tensor u_k. In metric H these are unit vectors and
\(\langle v_k,v_l\rangle_H=1/16\) for k different from l. Define

\[
 T=\sum_kP_k\otimes P_k=\sum_k|v_k\rangle\langle v_k|_H.
\]

The five-column Gram matrix is

\[
 \frac{15}{16}I_5+\frac1{16}\mathbf1\mathbf1^T.
\]

It has eigenvalues 5/4 once and 15/16 four times. Its positive eigenvalues
are precisely the nonzero eigenvalues of T, since for a column map V the
operators V^sharp V and V V^sharp have the same nonzero eigenvalues.
The remaining eleven eigenvalues of T are zero.

Using the frame sum in (1), the Bell operator for (9) is

\[
 \widehat{\mathcal B}
 =3T-\left(\sum_kP_k\right)\otimes\left(\sum_lP_l\right)
 =3T-\frac{25}{16}I_{16}.
\]

Therefore its spectrum, with multiplicities, is

\[
 \boxed{\operatorname{spec}(\widehat{\mathcal B})
   =\{(35/16)^{[1]},(5/4)^{[4]},(-25/16)^{[11]}\}.}       \tag{12}
\]

Moreover \(\sum_ku_ku_k^T=(5/4)G^{-1}\), so

\[
 \sum_kv_k=\frac54\operatorname{vec}(G^{-1})
         =\frac52|\Phi\rangle.
\]

This spans the largest eigenspace. For every joint density rho,
\(\operatorname{tr}(\widehat{\mathcal B}\rho)\le35/16\).
Equality forces rho to be supported on that one-dimensional eigenspace,
hence rho=rho_Phi. The optimum is over all states with these five fixed
effects on each wing. This is not an optimization over arbitrary physical
measurement families, nor a self-testing or device-independent uniqueness
claim.

## 6. All CHSH restrictions have absolute value at most two

Assign LOW the sign +1 and HIGH the sign -1. The correlations of (4) are

\[
 E(x,y)=p(LL)+p(HH)-p(LH)-p(HL)
       =\frac1{16}+\frac{15}{16}\delta_{xy}.              \tag{13}
\]

Take any x_0,x_1,y_0,y_1, including repeated choices, and any four signs
s_(ij) in {+1,-1} whose product is -1. These are all eight CHSH sign
variants. Set \(S=\sum_{i,j=0}^1s_{ij}E(x_i,y_j)\).

If either wing repeats its setting, one column sum or row sum of the sign
matrix is zero and the other is +2 or -2. Therefore S reduces to
\(\pm2E(x,y)\), whose absolute value is at most two.

Otherwise both wings use distinct settings. The equality entries
\(\delta_{x_i y_j}\) form a partial matching with m=0,1 or 2 edges.
Write e=1/16.

- If m=0, \(S=e\sum s_{ij}=\pm2e\), so |S|=1/8.
- If m=1, adding its contribution (1-e)s to the first term gives
  |S| equal to 1+e=17/16 or 1-3e=13/16.
- If m=2, the two edges occupy different rows and columns. If their
  signs agree, the other two signs are opposite; S is +2 or -2. If their
  signs disagree, their correction cancels and |S|=2e=1/8.

Thus

\[
 \boxed{\max|S|=2.}                                     \tag{14}
\]

For example x=(0,1), y=(1,0), with coefficient signs (+,+,+,-), attains
2. Equations (11) and (14) concern the same state and the same five
settings. Testing every two-setting CHSH restriction is not a test of the
complete five-setting Bell-local polytope. No implication from CHSH
nonviolation to full locality is used or available here.

## 7. A specified noise family

For 0<=v<=1 select the white-noise mixture

\[
 \rho_v=v\rho_\Phi+(1-v)I_{16}/16.
\]

The fully mixed state is (I_4/4) tensor (I_4/4). Its binary table is
(LL,LH,HL,HH)=(1,3,3,9)/16 for every pair of settings. In particular,
every LL entry is 1/16 and its Bell value is
\(2\cdot5/16-20/16=-5/8\). By linearity,

\[
 \boxed{\mathcal B(\rho_v)=\frac{45v-10}{16},\qquad
 \mathcal B(\rho_v)>2\ \Longleftrightarrow\ v>14/15.}      \tag{15}
\]

The parameter v is the declared mixture weight, not an inferred detector
efficiency or a laboratory error model. At or below 14/15 this particular
witness does not exclude locality; no local decomposition or other-witness
impossibility is concluded. The threshold is an exact consequence of this
chosen family, not a measured tolerance.

## 8. Steering is conditional; unconditional control is not signalling

The conditional Bob density after Alice obtains LOW at setting x on Phi
is P_x; after HIGH it is Q_x/3. This follows from the same aligned transpose
identity used in (4), or directly by partially tracing the two branches of
the standard maximally entangled vector. The probabilities are 1/4 and
3/4, respectively, so the density without Alice's result is

\[
 \frac14P_x+\frac34\frac{Q_x}{3}=I_4/4.                  \tag{16}
\]

The conditional ensembles depend on x. Their average does not. Sorting
Bob's records by Alice's setting and result requires those records to be
communicated or otherwise jointly available. It is not an operation on
Bob's marginal data alone. Formula (16) is an exact steering-versus-average
distinction and does not assume that a realized remote outcome is already
known locally.

The more general no-message statement is given next. It is stronger than
checking only the one-shot marginal table.

## 9. Local histories, explicit memory and bounded local stopping

Adjoin arbitrary finite local memories M_A,M_B, and let rho be any joint
complex density on (S_A tensor M_A) tensor (S_B tensor M_B). Initial
correlations and entanglement between any of these declared factors are
allowed. There is no replacement of their dynamics by a guessed reduced
source channel. Work in orthonormal coordinates for the proof; changing
back to the declared metrics leaves it unchanged.

An admitted finite protocol on each wing is a finite-depth tree of local
completely positive branch maps. At each node, the sum of the outgoing
maps is trace preserving. The next local setting and operation can depend
on the wing's own past record, local control and local finite memory, but
not on a remote record or an undeclared interwing operation. A predeclared
finite upper bound on the depth permits local stopping at earlier nodes.
Include every local leaf in the outcome space, including a declared
no-event or resource disposition if such a branch is part of the protocol.
Discarding inconvenient leaves is not the total instrument used here.

For local leaves h,g, denote the compositions along their paths by
\(\mathcal A_h\) and \(\mathcal B_g\). Each is completely positive.
Induction from the leaves towards the root gives

\[
 \mathcal A_{\rm tot}=\sum_h\mathcal A_h,
 \qquad \mathcal B_{\rm tot}=\sum_g\mathcal B_g
 \quad\hbox{trace preserving}.                           \tag{17}
\]

Indeed, replacing a stopped leaf by its continuation preserves total trace
because the outgoing sum is trace preserving. A stop itself is the identity
continuation on that leaf. Repeated use proves (17) for every bounded
stopping tree, without an assumption of a fixed stopping depth.

The unnormalized joint history operator and weight are

\[
 \rho_{h,g}=(\mathcal A_h\otimes\mathcal B_g)(\rho),
 \qquad p(h,g)=\operatorname{tr}(\rho_{h,g}).               \tag{18}
\]

Positivity follows from complete positivity; summing (18) gives one by
(17). Summing all continuations of a prefix gives its prefix weight.
Every positive-weight history has its normalized joint successor. These
facts prove the finite complex-state ordered law, including local adaptive
choices, explicit operative memory and bounded local stopping. They do
not infer a single realized event without the separately adopted occurrence
law. Passive rereading of an existing archive entry is not another trial.

Maps on different wings commute, so every interleaving compatible with the
two local orders has the same expression (18). This statement ceases to
apply if an operation acts jointly across the wings or a local choice
depends on a newly received remote outcome. Such communicated protocols
can be represented explicitly, but are not the no-message class here.

The finite proof does not establish almost-sure termination of an
unbounded stopping rule, infinite physical archive capacity, or a free
reset. A fresh-pair product law across repeated trials additionally requires
replacement of the entire declared source and operative memories, as in
ETH-QDD-1. Resetting only a pointer does not supply independent trials.

## 10. Controllable-message test on all local records

Let m label a message Bob is free to encode in a local protocol
\(\{\mathcal B_g^{(m)}\}_g\). Each total map
\(\mathcal B_{\rm tot}^{(m)}\) is trace preserving by (17). The full
initial joint density rho is the same for every message. Alice's protocol,
including her setting-selection rule and any later decision function of
her local records, is also the same for every message. This freezes the
absence of a source-message correlation or a separately transmitted
message in Alice's control input.

Using the adjoint map and
\((\mathcal B_{\rm tot}^{(m)})^*(I)=I\), for every Alice leaf h,

\[
\begin{aligned}
 p_m(h)
 &=\sum_g\operatorname{tr}[
       (\mathcal A_h\otimes\mathcal B_g^{(m)})(\rho)]\\
 &=\operatorname{tr}[
       (\mathcal A_h\otimes\mathcal B_{\rm tot}^{(m)})(\rho)]\\
 &=\operatorname{tr}[(\mathcal A_h\otimes\operatorname{id})(\rho)].
\end{aligned}                                           \tag{19}
\]

This is independent of m. Consequently every decision whose distribution
is obtained solely from Alice's local record and a fixed local decision
kernel has a message-independent distribution. In particular Bob cannot
encode a controllable distinguishable message into those records by any
operation in this class. Interchanging the wings gives the same theorem in
the opposite direction. This covers arbitrary finite local ancillas,
arbitrary fixed initial correlations, adaptive local instruments and
bounded local stopping, not just the five one-shot projective reads.

Postselection on a Bob event replaces the trace-preserving sum by one
branch and does not satisfy the premise of (19). Recognizing or selecting
those trials on Alice's side needs remote information. A stop rule chosen
using a remote record, a joint interwing operation, an initial state varying
with m, or a message-dependent Alice control is likewise outside the
specified test. The proof does not exclude ordinary communication through
an explicitly added channel.

The conclusion is operational no-message transmission in a selected tensor
model. To call any physical separation spacelike or any transmitted signal
superluminal requires an additional spacetime and clock dictionary. Neither
that dictionary nor a microscopic mechanism is derived here.

## 11. A complete setting-dependent separable negative control

For each setting k define the two normalized local densities

\[
 \tau_{k,L}=P_k,\qquad \tau_{k,H}=Q_k/3.
\]

They yield their indicated outcome with probability one when measured at
k. For each pair of settings x,y choose the separable state

\[
 \sigma_{xy}=
 \sum_{a,b}p_\Phi(a,b\mid x,y)\,
                 \tau_{x,a}\otimes\tau_{y,b}.             \tag{20}
\]

It is normalized and positive. Measuring precisely x,y on this state
reproduces every entry of (4), since the cross-effect traces vanish and
the indicated-effect traces equal one. Moreover its local marginals are

\[
 \operatorname{tr}_B\sigma_{xy}
 =\frac14P_x+\frac34\frac{Q_x}{3}=I/4,
 \qquad \operatorname{tr}_A\sigma_{xy}=I/4.               \tag{21}
\]

Thus both no-signalling equalities and the same reduced source densities
can coexist with this dependence of the preparation on the settings.
Equation (20) supplies a family of setting-dependent preparations, not one
fixed separable preparation. A single fixed separable preparation would
have decomposition (8), contradicting (11).

An equivalent response-level example takes lambda=(a,b), local deterministic
responses returning the two components, and
\(\mu_{xy}(a,b)=p_\Phi(a,b\mid x,y)\). It preserves conditional local
factorization but violates measurement independence. The contradiction in
(11) excludes the conjunction in (8); it cannot by itself select among
all possible replacements for the premises. Construction (20) is an exact
negative control demonstrating that point, not the source selected by this
theory and not a superdeterministic physical proposal.

## 12. Native-code comparison and the remaining physical boundary

For each wing, the inherited code has an isometry W_n with
\(W_n^*W_n=G\), at n>=3, and actual restricted free pushforward
\(N_{m,n}W_n=W_m\). Select two marked code copies and their tensor map

\[
 \mathcal W_{n_A,n_B}=W_{n_A}\otimes W_{n_B}.
\]

It has Gram H and transports every joint density, branch and projector in
this proof to the tensor code. On this domain,

\[
 (N_{m_A,n_A}\otimes N_{m_B,n_B})\mathcal W_{n_A,n_B}
 =\mathcal W_{m_A,m_B}.                                  \tag{22}
\]

Thus independently chosen genuine free waits change neither the logical
joint state nor any probability when the reads are transported with the
code. The tensor restriction is an isometry. This does not assert that the
global native update is unitary, that one Omega=N_0 times F_5^6 decomposes
into the two wing systems, or that U itself prepares their entanglement.
The two comparison counters do not define a physical simultaneity,
separation, clock rate, preparation energy or coupling strength.

The formal apparatus needs the declared entangled preparation, both local
context controls, local records, independent setting selection, complete
local system boundaries and the adopted event law. Those are additional
physical choices. The joint law, Bell exclusion, unique optimum for the
fixed effects and no-message theorem are exact consequences conditional on
those choices. They neither close the entire physical apparatus class nor
promote an unperformed experiment to evidence. The existing native,
apparatus and cross-layer owners keep their broader scopes.
