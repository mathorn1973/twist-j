# Finite-environment loading, retained failures and the accepted channel

**NON-CANONICAL, L1, conditional candidate-T. Independent acceptance
pending.** Public reservation:
[issue #1757](https://github.com/mathorn1973/twist-j/issues/1757).
This is an analytical construction, with no new scientific execution.

The old apparatus and its conditional accepted-channel interface are
[HAMILTONIAN.md of #1756 at 901c400](https://github.com/mathorn1973/twist-j/blob/901c400f85c427752e2e4367afb6cd00e59ac8c8/notes/C-LOCAL-CLOCK-SOURCE-N/HAMILTONIAN.md).
[HAMILTONIAN.md](HAMILTONIAN.md) specifies the new local environment,
loader, handoff and complete raw-space Hamiltonian. Its initially supplied
finite environment and its physical energy account are discussed in
[ENVIRONMENT.md](ENVIRONMENT.md). Here the old source is initially empty;
its excitation is created by the specified environment transition.

The preparation is not deterministic. The active environmental branch has
weight q=4/15, and every inactive branch remains in the complete state.
An explicit loading window prepares the actual old source state on that
branch, with a separate loader packet. It does not merely rename an initial
excitation at the old source site.

## 1. The finite input and active path

The environment has two qubits h,c with gaps 3 epsilon and epsilon and
independent initial excited populations 1/3 and 1/5. Their basis weights are

\[
p_{00}=8/15,\qquad p_{01}=2/15,\qquad
p_{10}=4/15=:q,\qquad p_{11}=1/15.
\tag{P1}
\]

The old source s starts in |0>. The loader t_0,...,t_(L-1) and all old
processor cursor sites start empty. The old data, charged data-battery
fuel, work and completion latch have their previously declared ready state,
with arbitrary admitted logical/reference correlations. Their readiness
is not derived from the two environmental qubits.

The first local exchange is

\[
|1_h0_c0_s0_{t_0}\rangle
\quad\longleftrightarrow\quad
|0_h1_c1_s1_{t_0}\rangle.
\tag{P2}
\]

Both words have bare energy 3 epsilon. The source and loader each acquire
one excitation while the cold qubit acquires one. The initially active
word is the h,c branch 10, with weight q. The other three environmental
branches have no accessible launch transition on the stated vacuum input.

Let the old completion threshold be L=2a and its old endpoint be 2L.
The new loader has L sites, and the old main cursor is extended from
2L to 3L by identity instructions. The total active history path has
K=4L edges and the following vertices:

- vertex 0: environment 10, source and all loader/main sites empty;
- vertices j=1,...,L: environment 01, source occupied, loader at t_(j-1),
  and every old main cursor site empty;
- vertices L+r, r=1,...,3L: environment 01, source empty, loader at its
  last site t_(L-1), and old or extended main cursor at site r.

The conditioned last loader edge and first main edge in HAMILTONIAN.md
make this one path invariant. The last loader excitation remains in place
while the main computation runs. Reverse hopping reverses the same path;
no branch is discarded or treated as an absorbing halt.

Write |nu_j> for these orthogonal physical basis configurations. The data
prefix F_j is identity for j<=L. At j=L+r it is the old prefix through
main site r, with the added identity tail when r>2L. In particular

\[
B=2L=K/2,\qquad F_j=F_B\quad(B\leq j\leq K).
\tag{P3}
\]

Thus the output is complete at global vertex B and stays on its fixed
final data row throughout the tail. The old completion latch is zero for
j<B and true for j>=B, on this prepared family.

## 2. Complete mixture and exact amplitudes

Let rho_z^fail denote the entire initialized state in each inactive branch
z=00,01,11, including the empty source/loader/main cursor and ready data.
Each is stationary under the new Hamiltonian on this input. Let rho_a(t)
be the normalized evolution of the active branch. The full state is

\[
\rho(t)=q\rho_a(t)+\sum_{z\in\{00,01,11\}}p_z\rho_z^{\rm fail}.
\tag{P4}
\]

This expression retains all four branches and their energy costs. It is
an identity of density operators, not an assertion about which outcome
occurs in an individual run.

On the active invariant path, the same constant-diagonal perfect-transfer
matrix gives, for a pure data/reference input psi_D,

\[
|\Omega_a(t)\rangle=e^{-it(E_a+g)/\hbar}
 \sum_{j=0}^{K}b_j(t)|\nu_j\rangle F_j|\psi_D\rangle,
\]
\[
b_j(t)=\sqrt{\binom Kj}(i\sin\theta)^j(\cos\theta)^{K-j},
\qquad \theta=\frac{gt}{\hbar(K+1)}.
\tag{P5}
\]

Here E_a is the fixed bare energy of that active branch, including the
old ready data and environmental charge. It is not the mean energy of
the full mixture. A mixed logical/reference input is handled by purification
or linearity. The inactive branches do not require the same bare-energy
value, and no replacement of their energy variance by the active-branch
variance is made.

For p=sin^2(theta), write X for the formal binomial weights

\[
\Pr(X=j)=\binom Kj p^j(1-p)^{K-j}.
\tag{P6}
\]

This notation abbreviates the exact expansion (P5). It does not supply an
occurrence law or a classical trajectory for the quantum cursor.

## 3. Loading before handoff

Use the first interval before theta=pi/2 with

\[
1/16\leq p\leq1/8,
\]

namely

\[
\frac{\hbar(K+1)}{g}\arcsin\frac14
 \leq t\leq
\frac{\hbar(K+1)}{g}\arcsin\frac1{\sqrt8}.
\tag{P7}
\]

Call vertices 1,...,L-1 good. They exclude the last loader site and hence
the handoff vertex L. On every good vertex:

- the environment is in 01;
- the actual old source is exactly |1>;
- all old main cursor sites are empty and all old data are unchanged;
- the loader has one excitation strictly before its last site;
- the completion latch retains its ready value.

The control n_(t_(L-1)) is zero on these states. The main handoff term
therefore annihilates this comparison subspace. This does not freeze the
loader itself or switch off its motion toward the handoff.

The active bad weight is

\[
\beta(t)=\Pr(X=0)+\Pr(X\geq L).
\tag{P8}
\]

The first term is a launch that has not occurred. The second includes the
handoff vertex and every later main history. Since K=4L,

\[
\Pr(X=0)=(1-p)^{4L}\leq(15/16)^{4L}.
\]

The generating polynomial E[z^X]=(1-p+pz)^K gives

\[
\Pr(X\geq L)\leq3^{-L}\mathbb E[3^X]
 =3^{-L}(1+2p)^{4L}\leq(625/768)^L.
\tag{P9}
\]

Consequently

\[
\boxed{\quad
\beta(t)\leq\delta_{\rm load}:=(15/16)^{4L}+(625/768)^L
 <2(5/6)^L.
\quad}
\tag{P10}
\]

Both comparisons are exact: (15/16)^4=50625/65536<5/6 and
625/768<5/6. The inherited finite construction already has L>=1024.
Using (5/6)^4=625/1296<1/2 therefore proves

\[
\delta_{\rm load}<2^{-255}<10^{-30}.
\tag{P11}
\]

In particular, both sqrt(delta_load) and sqrt(2 delta_load) are strictly
less than 2^-127, hence less than 10^-30. This bounds the full-state trace
and phase-aligned vector errors used below, not only the bad weight.

These are finite norm-weight inequalities, not empirical loading rates.

## 4. What is approximately and exactly prepared

Let w_load(t)=1-beta(t). Define the normalized loader packet

\[
|\chi(t)\rangle_t=\frac1{\sqrt{w_{\rm load}(t)}}
                  \sum_{j=1}^{L-1}b_j(t)|t_{j-1}\rangle.
\tag{P12}
\]

Let rho_old^ready be the old ready apparatus state with its source |1>,
its other old cursor sites empty, and its original data/latch preparation,
including the unknown logical input and reference. In the notation below,
rho_old^ready also tensors the vacuum of the added main-tail cells
r=2L+1,...,3L. These are physical factors, not omitted degrees of freedom.
The good comparison
state factors exactly as

\[
\sigma_a^{\rm load}(t)=|01\rangle\langle01|_{hc}
 \otimes|\chi(t)\rangle\langle\chi(t)|_t
 \otimes\rho_{\rm old}^{\rm ready}.
\tag{P13}
\]

For pure inputs its overlap with (P5), after choosing the common phase,
is sqrt(w_load). Thus, with trace distance D(rho,sigma)=||rho-sigma||_1/2,

\[
D(\rho_a(t),\sigma_a^{\rm load}(t))
 \leq\sqrt{\beta(t)}\leq\sqrt{\delta_{\rm load}}.
\tag{P14}
\]

Equality in the first bound holds for the purified pure states. Partial
trace gives the displayed reference-uniform inequality for mixed inputs.
The phase-aligned vector-norm bound is sqrt(2 beta), a different metric.

For the actual unconditioned experiment use the comparison mixture

\[
\sigma^{\rm load}(t)=q\sigma_a^{\rm load}(t)
                    +\sum_z p_z\rho_z^{\rm fail}.
\]

The inactive terms are identical on both sides, so

\[
\boxed{\quad D(\rho(t),\sigma^{\rm load}(t))
 \leq q\sqrt{\delta_{\rm load}}.\quad}
\tag{P15}
\]

This is an unconditional approximation to a retained mixture, not to a
pure loaded apparatus with unit weight. No projection or renormalization
is performed by the construction of the comparison state.

A local mathematical readiness observable is

\[
\Pi_{\rm ready}=n_s(1-n_{t_{L-1}}).
\tag{P16}
\]

The source and last loader site are neighbors in the specified layout.
On the reached configurations (P16) selects precisely vertices 1,...,L-1;
it vanishes on every inactive thermal branch. Its weight is exactly
q w_load(t)>=q(1-delta_load). If one mathematically projects with it and
normalizes, the reduced old apparatus is exactly rho_old^ready, for every
admitted logical/reference input. The remaining loader is (P12) and the
environment is 01. No physical implementation of that projection or an
occurrence rule is supplied by this observable.

This prepares the previous source vector as a tensor factor of a nearly
factorized loaded branch. It does not assert that the entire previous
Hamiltonian is already operating independently: its first edge is gated
by the loader endpoint, its clock coefficients are retuned for the larger
path, and the loader remains part of the same closed apparatus.

## 5. The source marginal and the retained environment

The source is excited at all loader vertices 1,...,L, including the handoff
vertex omitted from the good set. It is ground at vertex 0, on all main
vertices and on every inactive branch. Orthogonality of the remaining
environment/loader/cursor configurations removes source off-diagonal terms.
Hence its exact reduced state is

\[
\rho_s(t)=(1-p_s(t))|0\rangle\langle0|+p_s(t)|1\rangle\langle1|,
\qquad p_s(t)=q\Pr(1\leq X\leq L).
\tag{P17}
\]

Writing beta_s=Pr(X=0)+Pr(X>L)<=beta, one obtains

\[
D\bigl(\rho_s(t),(1-q)|0\rangle\langle0|+q|1\rangle\langle1|\bigr)
 =q\beta_s(t)\leq q\delta_{\rm load}.
\tag{P18}
\]

At every time, however, p_s(t)<=q. In particular,

\[
D(\rho_s(t),|1\rangle\langle1|)\geq1-q=11/15.
\tag{P19}
\]

This rules out a deterministic pure-source interpretation of this protocol.
It is not an optimality bound for every conceivable finite thermal machine.

Reading the spent environmental pattern 01 alone is insufficient: the
initial inactive branch 01 already has weight 2/15 and never loads the
source. The loader/source and later completion records distinguish it from
the successful branch. Entropy and correlations of the original mixed
environment are retained by the complete unitary, not removed by calling
that pattern a success.

## 6. Completed capture channel and the changed weight

The completion latch and final acceptance flag define the inherited
physical read projector Pi_read. On each inactive branch the completion
latch remains false. On the active path it excludes every vertex j<B,
even if a temporary primitive compiler flag is nonzero. On all retained
vertices the completed payload is the same F_B state on its fixed row.

Let D_out be the fixed mathematical output reduction: trace environment,
loader, main/source cursor, latch, work, battery, fuel, inner clock, tally
and auxiliary histories, retain the output information registers and the
reference, and apply their declared valid decoding. Let sigma_ideal be the
unnormalized ideal accepted physical/reference state of the inherited word.
Set

\[
w_{\rm out}(t)=\Pr(X\geq B)=
 \sum_{j=2L}^{4L}\binom{4L}{j}p^j(1-p)^{4L-j}.
\]

Then orthogonal history configurations and the pinned accepted-channel
identity prove

\[
\boxed{\quad
\mathcal D_{\rm out}[\Pi_{\rm read}\rho(t)\Pi_{\rm read}]
 =q\,w_{\rm out}(t)\,\sigma_{\rm ideal}.
\quad}
\tag{P20}
\]

The equality holds as a linear map on admitted logical input operators,
including arbitrary reference correlations. The traces are comparison maps;
no rejected branch is physically erased. Normalization, when the weight is
nonzero, leaves exactly the ideal accepted physical state.

For pi/3<=theta<=2pi/3, one has p>=3/4. Since K=2B,

\[
1-w_{\rm out}(t)\leq3^B(1-p+p/3)^{2B}
 \leq(3/4)^B=(3/4)^{2L}=:\delta_{\rm out}<10^{-30}.
\tag{P21}
\]

The inherited source bound is explicitly

\[
p_{\rm ideal}>p_0=\frac25\frac{1024}{15625}\frac{99}{50000},
\qquad\frac{99}{100}p_0>\frac1{20000}.
\]

Thus on this new read interval,

\[
\boxed{\quad p_{\rm read}(t)=q w_{\rm out}(t)p_{\rm ideal}
 >\frac{q}{20000}=\frac1{75000}.\quad}
\tag{P22}
\]

The earlier 1/20000 lower threshold is not carried over unchanged. The
normalized unwanted bound-band fraction remains below 1/10^6, and the
accepted incoming-label/old-memory SWAP, including arbitrary reference,
remains exact, conditional on the pinned source/filter premises. With
incoming label 1, the receiver is the correct d_1 codeword. No new physical
position identification or local implementation of the band observable
follows from this decoding identity.

## 7. Endpoint continuation and preparation limits

At tau=pi hbar(K+1)/(2g), the active path is exactly at K. A mathematical
accepted read with incoming label 1 selects only that active branch and
leaves the correct receiver state. Continue with the same fixed Hamiltonian
from the normalized projected state. For any endpoint data/reference vector
phi, reverse history j carries F_j F_K* phi. This is exactly phi for j>=B.

For delays 0<=u<=tau/3, the reverse-move weights have parameter
r=sin^2(gu/[hbar(K+1)])<=1/4. The weight outside the completed tail is at most

\[
3^{-B}(1+2r)^{2B}\leq(3/4)^B=\delta_{\rm out}.
\tag{P23}
\]

The wrong-receiver projector annihilates the good tail and has norm at
most one elsewhere. Orthogonal history configurations therefore bound its
weight by delta_out, including arbitrary retained battery/reference
correlations. The preparation factor q has disappeared through the stated
conditioning; no inverse q penalty is inserted into this exact tail argument.
This is a continuation contract, not a newly implemented instrument.

The comparison uses an actual old source excited from the finite environment,
but the source ground state, loader/main vacuum, ready data and contact law
are still initial resources. A ground state has no positive bare energy
cost here; its purity is not thereby derived for free. The particular
thermal populations fix q. The existence of a nonzero active branch under
these conditions does not prove that a temperature gradient is necessary
for every one-time loading protocol.

The initial environmental states are Gibbs states of their specified bare
single-qubit Hamiltonians. The complete product input is not a Gibbs state
of the interacting Hamiltonian that runs. A state stationary for that full
Hamiltonian stays stationary under its own evolution; the nonstationary
contact assumption is not removed by the word thermal.

Nor does this finite autonomous law produce a newly entered exact loading
plateau. Matrix elements of finite-Hamiltonian evolution are analytic in
time. Exact confinement to a fixed prepared subspace on an open interval
would extend to all times, contradicting an initial state outside it.
The quantitative window above avoids that false claim. There is no permanent
halt, reusable entropy-free reset, fresh infinite bath, or law of individual
outcomes in this candidate.
