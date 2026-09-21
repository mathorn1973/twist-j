# A selected coherent measurement theory

Written proof for P-QDD-SELECTED-MEASUREMENT-LAW-1. PUBLIC,
candidate-T, NON-CANONICAL. A. M. Thorn; original text Apache-2.0.
The mathematical statements below are conditional on the declared selection
of a physical state, instrument class and occurrence law. They do not derive
those selections from J or the native deterministic update U. The generic
channel and sequential-measurement arguments are ordinary finite-dimensional
quantum theory; the specified trace metric, code, context orbit and exact
comparison numbers are the TWIST-J specialization.

## 1. State space, positivity and zero support

Let V=C^4 with

\[
 G=I_4-\frac15\mathbf1\mathbf1^T,
 \qquad \langle v,w\rangle_G=v^*Gw,
 \qquad X^\sharp=G^{-1}X^*G.
\]

The eigenvalues of G are 1,1,1,1/5, so this is a positive Hilbert metric.
A density is an endomorphism rho with rho^sharp=rho, G rho positive
semidefinite, and ordinary matrix trace tr(rho)=1. These are precisely
ordinary density operators after the coordinate change by G^(1/2):
rho maps to G^(1/2) rho G^(-1/2). In particular, positivity, trace,
complete positivity and all statements below are independent of the
nonorthonormal displayed basis.

A nonzero vector v prepares

\[
 \rho_v=\frac{vv^*G}{v^*Gv}.
\]

The zero vector is typed ZERO_SUPPORT: it supplies no normalized preparation
and no completed measurement outcome. More generally an unnormalized
positive input X of trace t>0 denotes the normalized preparation X/t
together with its declared weight t. If t=0, positivity implies X=0 and
normalization is undefined. Such an input is returned as ZERO_SUPPORT,
not as a random outcome with two zero probabilities. A zero-weight branch
of a supported preparation is retained as the zero operator and is never
divided by its trace.

The physical use of all these densities, including mixed and complex
preparations, is an explicit selection. The native finite checkpoint is
not itself this density operator.

## 2. Five fixed contexts and their simplex geometry

In the shifted source basis j,j^2,j^3,j^4, multiplication by j is

\[
 R=\begin{pmatrix}
 0&0&0&-1\\1&0&0&-1\\0&1&0&-1\\0&0&1&-1
 \end{pmatrix},\qquad R^5=I,\qquad R^*GR=G.
\]

Set P_0=ones_4/4, Q_0=I-P_0 and, for k in Z/5,

\[
 P_k=R^kP_0R^{-k},\qquad Q_k=I-P_k.
\]

These are G-orthogonal projectors of ranks one and three. They define
five selected apparatus settings. R is not asserted to be a native U step,
and setting changes are controlled choices, not time evolution forced by U.

An explicit unit vector for P_0 is u_0=(sqrt(5)/2) ones_4. The next four
vectors are u_k=-(sqrt(5)/2)e_k, k=1,2,3,4. Direct use of G gives

\[
 \langle u_k,u_l\rangle_G=
 \begin{cases}1&k=l,\\-1/4&k\ne l,\end{cases}
 \quad \sum_{k=0}^4u_k=0,
 \quad P_k=u_ku_k^*G,
 \quad \sum_{k=0}^4P_k=\frac54I.
\]

For example, R ones_4=-e_1 and R e_i=e_(i+1) for i<4, which supplies
the displayed orbit. The diagonal and off-diagonal Gram entries then follow
from G_(ii)=4/5, G_(ij)=-1/5 and G ones_4=ones_4/5. The frame sum follows
by summing the five displayed outer products. Consequently

\[
 \operatorname{tr}(P_kP_l)=
 \begin{cases}1&k=l,\\1/16&k\ne l.\end{cases}                 \tag{1}
\]

For context zero the selected LOW probability on a pure preparation is
|sum_i v_i|^2/(20 v^*Gv). This recovers the inherited algebraic quadratic
weight only after the occurrence law in section 5 is adopted.

## 3. Native code transport is a restricted isometry

Use the specified coherent code from
[P-U-GALOIS-FIBER-CODE-1](../P-U-GALOIS-FIBER-CODE-1/PROOF.md).
Its freely propagated map W_n obeys W_n^*W_n=G. From n=3 onwards its
range C_n is the four-dimensional span of the four synchronized moving
endpoints. Write W_n^sharp=G^(-1)W_n^*, the inverse on C_n. For m>=n>=3,
the restriction of the actual free native linear pushforward satisfies

\[
 N_{m,n}W_n=W_m.
\]

It is therefore an isometry from C_n to C_m. This is not a statement
that the pushforward on the full native checkpoint space is unitary or
even injective. Earlier native mergers remain present outside the
restricted four-dimensional coherent code.

Define on C_n only

\[
 D_{n,k,L}=W_nP_kW_n^\sharp,\qquad
 D_{n,k,H}=W_nQ_kW_n^\sharp,\qquad
 \Sigma_n=W_n\rho W_n^\sharp.
\]

These are orthogonal code projectors and a code density. They satisfy

\[
 D_{m,k,o}N_{m,n}=N_{m,n}D_{n,k,o}\quad\hbox{on }C_n.          \tag{2}
\]

This follows by composing each side with the surjection W_n and using
N_(m,n)W_n=W_m. The code projector D_(n,0,L) is the transported
distinguished endpoint read. For k other than zero the selected physical
implementation must supply the corresponding coherent context; a mere
renaming of native endpoints is not assumed to implement it.

Thus genuine free waiting, including waiting chosen from previous records,
acts as the identity on the displayed source coordinates. Equations (1)
and all sequential laws below survive any such waits when the read is
transported by (2). No inverse of global U is executed. The counter n
indexes the comparison; it does not supply laboratory energy or a clock.

## 4. Selected post-state principle and the complete CP branch class

The selected one-use instrument class consists of completely positive
linear branches Phi_(k,L), Phi_(k,H) whose sum preserves trace. In Kraus
notation a branch is sum_j L_j X L_j^sharp. The preparation and reset
contract supplies an apparatus ready state independent of the current
source and of earlier records. An uncontrolled correlated environment is
not silently represented by a state-independent source channel.

Three additional physical requirements are adopted in this class:

1. The effects are the displayed P_k,Q_k: branch traces are
   tr(P_k rho), tr(Q_k rho) for every density rho.
2. A repeated read in the same context is repeatable: the opposite
   outcome has zero weight after either branch.
3. The HIGH channel preserves the following three independently defined
   attenuation profiles for every HIGH-supported density.

To define the last condition, let E have columns e_1-e_4,e_2-e_4,e_3-e_4.
It maps C^3 onto Q_0V and has induced metric

\[
 H=E^*GE=I_3+\mathbf1_3\mathbf1_3^T,
 \quad
 A=\begin{pmatrix}-1&-1&-3/4\\0&0&1/4\\1&0&1/4\end{pmatrix},
 \quad B_t=(A^{\sharp_H})^tA^t,\quad t=1,2,3.
\]

Here sharp_H means H^(-1) X^* H. At context k use T_k=R^k E, an
isometry from the H metric onto Q_kV. The three HIGH tests are the
transports of B_t by T_k. The inherited A is the attenuation from the
previous independent algebraic construction; it is not defined here as
Q_0 R Q_0 and no such equality is claimed. Its transfer to this chosen
physical HIGH support and its preservation are explicit physical choices.
The tests are fixed before the unknown post-state channel is selected.

**Theorem 1 (complete reduced instrument selection).** In the class above,
the three requirements hold if and only if

\[
 \mathcal I_{k,L}(X)=P_kXP_k,\qquad
 \mathcal I_{k,H}(X)=Q_kXQ_k.                                \tag{3}
\]

**Proof.** Write P=P_k, Q=Q_k. The Q effect implies
sum_j L_j^sharp L_j=Q. For v in PV, summing squared norms shows
L_j P=0 for each j. Repeatability gives P L_j=0, again by a sum of
nonnegative squared norms. Thus L_j=Q L_j Q, and restriction to QV
is an arbitrary trace-preserving CP channel E_Q. Conversely every such
channel E_Q yields a repeatable Q branch E_Q(QXQ). This is the entire
finite-dimensional CP branch class, allowing arbitrary complex Kraus
entries and mixed outputs. The rank-one P branch is necessarily PXP,
because a trace-preserving channel on a one-dimensional operator algebra
is the identity.

For completeness the inherited three-pass argument is recorded here.
Under the T_k identification, trace preservation makes E_Q^* unital.
Preservation of the three profile weights for every density is equivalent
to E_Q^*(B_t)=B_t. Put

\[
 d_0=(-1,-1,3)^T,\quad d_1=(11,-5,-1)^T,
 \quad d_2=(-9,-25,-5)^T.
\]

The exact identities are

\[
 \begin{split}
 H-A^*HA&=\operatorname{diag}(0,0,5/4),\\
 I-A^{\sharp_H}A&=(15/16)\operatorname{Proj}_H(d_0),\\
 A^{\sharp_H}d_0&=d_1/4,\qquad A^{\sharp_H}d_1=d_2/4,\\
 \det[d_0,d_1,d_2]&=-1024,\\
 \langle d_0,d_1\rangle_H&=-4,\qquad
 \langle d_0,d_2\rangle_H=-20.
 \end{split}
\]

Therefore the three differences B_t-B_(t+1), t=0,1,2 with B_0=I,
are positive multiples of the three rank-one projectors onto d_t.
Their traces are 15/16, 215/256 and 2815/4096. E_Q^* fixes all three
projectors.

If a unital Kraus adjoint fixes an orthogonal projector F, positivity
on ker F gives F K_j(ker F)=0. Trace preservation together with the
same fixed-projector equality on im F gives
(I-F) K_j(im F)=0. Hence every K_j commutes with F. Applied to the
three projectors above, each K_j has all d_t as eigenvectors. Commutation
with the d_0 projector and its two nonzero inner products forces all
three eigenvalues to agree. The nonzero determinant gives K_j=c_j I,
and sum_j |c_j|^2=1 gives E_Q=id. This proves (3). Conversely (3)
immediately has the required effects, repeatability and profile preservation.

The restriction to complete positivity is essential; mere positive maps
include transpose in a real orthonormal basis, which fixes the real tests
but changes complex states. The full proof and explicit nonselection
witnesses are in
[MIXED-PROOF.md](../P-QDD-V80-CLOSURE-BOUNDARIES-1/MIXED-PROOF.md).
The theorem identifies reduced instruments within the declared class;
it does not classify all physical couplings or hidden apparatus memories.

## 5. Occurrence is a selected law, not a unitary consequence

For a normalized preparation rho and a chosen setting k, adopt a completed
event with exactly one outcome o in {L,H}, probability

\[
 p(o\mid k,\rho)=\operatorname{tr}\mathcal I_{k,o}(\rho),
 \qquad
 \rho_o=\frac{\mathcal I_{k,o}(\rho)}{p(o\mid k,\rho)}
 \quad\hbox{when }p(o\mid k,\rho)>0.                         \tag{4}
\]

This is an adopted Born occurrence and conditioning law. Theorem 1 selects
its reduced post-state instruments given the stated requirements; it does
not derive the physical occurrence of one branch. A physical terminal
event is the completion of a faithful record of this selected outcome,
under the admitted apparatus and persistence assumptions. ZERO_SUPPORT
produces no event. Incomplete physical writes or apparatus faults are outside
this ideal model and cannot be relabeled as one of its completed outcomes.

The law is compatible with arbitrary untouched finite-dimensional ancillary
systems through I_(k,o) tensor id. This is one reason for selecting complete
positivity. It does not impose a Born law on deterministic native points,
nor identify the probability ensemble with one finite-window native orbit.

## 6. Reversible writing, decoherence and the selected event

Let one fresh record cell have orthonormal states |blank>, |L>, |H>.
Let tau_L exchange blank and L while fixing H, and tau_H exchange blank
and H while fixing L. Define

\[
 C_k=P_k\otimes\tau_L+Q_k\otimes\tau_H.
\]

Orthogonality of P_k,Q_k gives C_k^sharp C_k=I and C_k^2=I on the
entire source-cell space. In particular

\[
 C_k(v\otimes|\mathrm{blank}\rangle)
 =P_kv\otimes|L\rangle+Q_kv\otimes|H\rangle.                 \tag{5}
\]

All HIGH amplitudes acquire the same record. This preserves their mutual
coherence. For a density input, the joint output contains not only the
diagonal terms P_k rho P_k tensor |L><L| and Q_k rho Q_k tensor |H><H|,
but also the off-diagonal terms P_k rho Q_k tensor |L><H| and its adjoint.

Record-basis dephasing removes those last two terms, producing the
classical-record/quantum-source state

\[
 \mathcal I_{k,L}(\rho)\otimes|L\rangle\langle L|
 +\mathcal I_{k,H}(\rho)\otimes|H\rangle\langle H|.           \tag{6}
\]

Equation (6) has the branch weights and conditional states of (4).
Neither (5) nor dephasing proves that precisely one event happens.
That identification is made by the selected event law (4). Nor does
dephasing restore the original uncorrelated source state. The reduced
source is generally P_k rho P_k+Q_k rho Q_k.

Old archive cells are passive by assumption. Each subsequent write acts
on the source and a new blank cell and as identity on old cells. Thus their
record values persist under the admitted dynamics. Supplying these cells,
their physical retention and controlled couplings is a physical resource
assumption. No unbounded material archive is inferred from the availability
of an arbitrary finite mathematical record string.

## 7. Complete finite histories and causal adaptive contexts

Fix a causal protocol before the run: at a history word w in {L,H}^*,
it specifies the next context k(w) and any free waiting time. More generally
it may specify a trace-preserving preparation or intervening channel T_w
on the current source, subject to the explicit memory/reset contract.
Taking T_w=id covers free waiting in the moving code coordinates. No
distribution over settings is needed for a fixed such protocol; an external
randomized setting rule requires its own supplied probability law.

Starting from rho_empty=rho_0, recursively set

\[
 \rho_{wo}=\mathcal I_{k(w),o}(\mathcal T_w(\rho_w)),
 \qquad p(w)=\operatorname{tr}\rho_w.                        \tag{7}
\]

Each rho_w is positive and unnormalized. The two branch maps sum to a
trace-preserving map, so

\[
 p(wL)+p(wH)=p(w),\qquad
 \sum_{|w|=N}p(w)=1.                                        \tag{8}
\]

These identities follow by positivity and trace preservation at one node
and induction down the tree. They cover every finite adaptive context tree,
not only the finite words used in a verifier. Conditional branch states and
probabilities are obtained only at nodes with p(w)>0. Unreachable branches
remain zero, independently of how the protocol labels their descendants.
A protocol may also stop at a node according to its recorded past. For a
finite tree whose leaves include every such terminating branch, repeated
use of (8) gives total leaf weight one. No assertion of almost-sure
termination is made for an unbounded stopping rule.

If a finite-dimensional quantum memory M is explicitly retained, use a
joint state omega_w on V tensor M, a declared joint CPTP intervening map
T_w, and the recursion

\[
 \omega_{wo}=(\mathcal I_{k(w),o}\otimes\mathrm{id}_M)
                 (\mathcal T_w(\omega_w)),\qquad
 p(w)=\operatorname{tr}\omega_w.                             \tag{7a}
\]

The same proof gives (8). This specifies a local selected instrument with
its own independently ready apparatus; it does not classify every joint
interaction with M. A correlated source-memory state need not induce a
state-independent reduced source channel, and no such channel is presumed.
The complete joint state, rather than only its source marginal, determines
later probabilities when T_w couples the two. Resetting that retained
memory for fresh trials requires the stronger replacement in (12).

With no nontrivial intervening channels, let P_(k,L)=P_k and
P_(k,H)=Q_k. Then for w=o_1...o_N,

\[
 K_w=P_{k(o_1...o_{N-1}),o_N}\cdots P_{k(\varnothing),o_1},
 \quad \rho_w=K_w\rho_0K_w^\sharp,
 \quad p(w)=\operatorname{tr}(K_w\rho_0K_w^\sharp).           \tag{9}
\]

The complete finite archive state is sum_(|w|=N) rho_w tensor |w><w|.
Its trace is one, and tracing its newest record reproduces the correctly
updated earlier-history weights. Old records themselves are not rewritten.

For a fixed infinite causal protocol, the compatible finite-cylinder
probabilities (8) define a unique probability measure on {L,H}^N with its
product sigma-algebra. One may use the ordinary finite-alphabet extension
theorem: each level is a probability distribution, every longer cylinder
marginal agrees by (8), and finite cylinder events generate the sigma-algebra.
This is a probability-space completion of the selected law. It is not a
construction of an infinite material archive, an all-order native sampling
theorem or a derivation of independent trials.

## 8. Repetition, fresh preparation and memory accounting

For a fixed context with free waits only and no intervening source-memory
interaction, P_k Q_k=0 and both projectors are idempotent. The retained
memory, if present, is untouched. Thus every history containing both
symbols has zero weight:

\[
 p(L^N)=\operatorname{tr}(P_k\rho_0),\qquad
 p(H^N)=\operatorname{tr}(Q_k\rho_0).                         \tag{10}
\]

Repeated reads of the same preparation are perfectly correlated in this
ideal model. The archive records one retained branch repeatedly, not N
independent draws.

A supplied fresh-preparation channel is instead

\[
 \mathcal R_\sigma(X)=\sigma\operatorname{tr}X.              \tag{11}
\]

It is CPTP. For example in orthonormal coordinates, if
sigma=sum_a s_a |a><a|, its Kraus maps sqrt(s_a)|a><i| for all a,i
give (11) and have Kraus squares summing to identity. In the source-only
protocol, a new source drawn from this fixed preparation before each read
gives product probabilities for a fixed, nonadaptive sequence of settings
and fixed replacements. With retained apparatus memory this conclusion
instead requires its stated independent readiness, or the joint replacement
in (12), before each trial.
For adaptive settings the same reset removes source memory, but the
conditional outcome law still depends on the context selected from history;
unconditional independence need not hold.

Where M is an admitted apparatus memory and A the retained archive,
the stronger joint replacement required for a genuinely ready independent
apparatus is

\[
 (\mathcal R_{\sigma\otimes\eta}\otimes\mathrm{id}_A)(X_{SMA})
 =\sigma\otimes\eta\otimes\operatorname{tr}_{SM}X_{SMA}.    \tag{12}
\]

It leaves the archive's reduced state intact and removes correlations of
source and apparatus memory with that archive. A microscopic implementation
must put discarded correlations and state information into a supplied
reservoir or replaced carrier. Equation (12) does not assert their global
destruction, free reset or a specific thermodynamic cost. Resetting only a
pointer or port is not equivalent to (11) or (12), and cannot be used to
claim fresh trials.

## 9. Exact consequences that constrain the selected theory

These are deductions after selection, not adjusted target values.

**Context transition.** Preparing the normalized LOW state P_k and reading
context l gives LOW probability one for l=k and 1/16 otherwise, by (1).
For every density rho, sum_k tr(P_k rho)=5/4. A separately supplied
uniform setting lottery would therefore have average LOW probability 1/4;
the lottery itself is not derived.

**Order and disturbance.** Start in rho_0=P_0. Read context 1 and then
context 0, retaining both outcomes. The exact table is

| First outcome, context 1 | Second LOW, context 0 | Second HIGH, context 0 |
| --- | ---: | ---: |
| LOW | 1/256 | 15/256 |
| HIGH | 225/256 | 15/256 |

Indeed the first LOW has weight 1/16 and leaves P_1. The HIGH-to-LOW
joint weight is ||P_0 Q_1 u_0||_G^2=(1-1/16)^2=225/256.
The remaining entries follow by normalization. When the intermediate
record is ignored the final LOW probability is 113/128, whereas omitting
the context-1 read gives one. This is an exact consequence of the
noncommuting projectors, not an experimental observation.

**HIGH coherence is observable.** In Q_0V take the orthonormal vectors

\[
 a=(1,-1,1,-1)^T/2,\quad b=(1,1,-1,-1)^T/2,
 \quad c=(1,-1,-1,1)^T/2,
 \quad \psi=(a+b)/\sqrt2.
\]

The selected coarse HIGH branch leaves |psi><psi| unchanged. A fine
measurement in the basis a,b,c followed by erasure of its fine label gives
one half of |a><a|+|b><b| instead. Inner products with
u_1=-(sqrt(5)/2)e_1 give next-context LOW probabilities 5/8 and 5/16,
respectively. Thus fine discrimination followed by forgetting is not the
selected coarse instrument. All displayed ket-bra operators in this section
use the G inner product.

## 10. Exact closure and outstanding physical attribution

Within the selected model there is now one consistent specification of
preparation, five contexts, reduced post-states, single-event probabilities,
all finite ordered histories, record writing, passive archive persistence,
fresh preparation and ZERO_SUPPORT. Complete positivity and the three-pass
condition select (3) within the full stated reduced-channel class. Native
free code transport is compatible with every such source-coordinate
history through (2).

The physical selections are not proved by this compatibility: adoption and
preparation of the coherent code; identification and controllability of the
five contexts; the CP apparatus type with its ready-state independence;
three-profile preservation; occurrence according to (4); supplied memory,
passive retention and replacement resources. The finite-dimensional writer
proves mathematical realizability in that type, not physical completeness
over nonlinear, correlated-memory or differently typed architectures.

The ion proposal supplies one external controlled realization candidate;
its postulated laboratory interactions are not deduced from J or unchanged
U, and their empirical accuracy has not been established for this program.
No new experiment is reported here. The algebraic identities are L1; channel
and record constructions provide mathematical objects for the declared
L4/L5 comparisons; the selected probability law is an explicit adopted
measure premise. None of those labels certifies that the registered
physical L1-to-L5 or separate L6 gate has passed. Canon promotion, any
redefinition of the broader apparatus obligations, and experimental
validation remain distinct acts.
