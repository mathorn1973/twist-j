# C-FIELD-J-PREPARATION-MECHANISM-N — proof

**PUBLIC, NON-CANONICAL. Conditional L1 mathematics only. Approximate
finite pointer preparation; actual occurrence is not derived.**

This proof implements the immutable PREREG at public specification pin
`7809098069d4c4ff9f362048cf92c3e8b4714493`. The exact inherited Stage-C
reference is `024936502544c2ec45acc8890a052c7b3aca26be`, with Stage B admitted
through that reference. Nothing below changes its carrier, transport,
conditional instrument, archive operation or source/context controls.

Authorship and exposure: the coordinator and algebra_builder supplied the
design and bounds disclosed in PREREG. The author-side `preparation_proof`
coauthor wrote this derivation from that frozen specification. This is
disclosed author assistance, not independent review. No reviewer source,
reviewer output, scientific execution or numerical observation was used
to derive this proof. Finite audit results, if obtained, belong in the
separate execution and result records; this document does not anticipate
their success.

## 1. Statement, domain and notation

For the application let \(L=613\), \(M=2L=1226\), and \(m=K+1\). Pointer
0 is C's active pointer; pointers 1 through K are its existing archive
pointers. Write their Hilbert spaces as \(A_i=\mathbb C^{2L}\), and let

\[
 A_i^{\rm e}=\operatorname{span}\{|p=2j\rangle:0\le j<L\}.
\]

We abbreviate the embedded even mode \(|p=2j\rangle\) by \(|j\rangle\).
The graph joining j to j+1 modulo L is a new internal mode graph. It is
not B's spatial chain, and no physical placement is inferred from this
notation. All other inherited coordinates, including source, archive
flags and any reference, are denoted Z. Only the new pointer and bath
factors are used in the calculations below; no truncation or alteration
of the inherited dirty-state carrier is implicit.

Choose finite nonnegative integers \(n_i\). Allocate exactly

\[
 B=L\sum_{i=0}^{K}n_i
\]

distinct qubits, with addresses (i, sweep, edge). On pointer i a sweep
visits edges 0 through L-1 in that order. Each collision uses its own
qubit, initially \(|0\rangle\), independent of all other coordinates. A
fixed external classical script specifies the ordering, addresses,
coupling phases and pulse durations. It never inspects a bath output or
postselects a history. Every bath output remains in the carrier.

The positive preparation theorem admits any density operator

\[
 \Omega\text{ on }\Big(\bigotimes_{i=0}^{K}A_i^{\rm e}\Big)\otimes Z.
\]

It may contain arbitrary mixed pointer states and arbitrary correlations
among pointers and Z. In particular it includes the clean product
\(|0\rangle\langle0|^{\otimes m}\otimes\rho_Z\). Source preparation
and archive flags are not prepared by this operation. The total unitary
will also be defined on odd pointers and dirty baths, but the convergence
promise does not cover those inputs.

For any integer L>=3 define

\[
 |E_L\rangle=L^{-1/2}\sum_{j=0}^{L-1}|j\rangle,
 \qquad P_E=|E_L\rangle\langle E_L|,
 \qquad r_L=1-\frac4{L^3}.
\]

Let \(F_{i,0}\) be the initial expectation of \(P_E\) on pointer i. The
claim proved below is

\[
 D\!\left(\Omega_{\rm out},P_E^{\otimes m}\otimes
             \Omega_{Z',\rm out}\right)
 \le \min\{1,\sqrt\delta+\delta/2\},
 \quad
 \delta=\min\left\{1,\sum_i r_L^{n_i}(1-F_{i,0})\right\},       \tag{1}
\]

where \(Z'=Z\otimes(\mathbb C^2)^{\otimes B}\) includes **all actual output
baths**, \(D(X,Y)=\frac12\|X-Y\|_1\), and the marginal in (1) is the
actual marginal. It need not be fresh, independent internally, or devoid
of the old pointer information. The original Z marginal is unchanged.

The proof is uniform in L>=3; L=613 is a substitution into the proved
bound. It does not rely on a finite dimensional census of selected L's,
a fitted gap, or a simulation of the sufficient large bath budget.

## 2. The total collision and its supplied Hamiltonian

For an edge j let

\[
 d_j=\frac{|j\rangle-|j+1\rangle}{\sqrt2},\qquad
 s_j=\frac{|j\rangle+|j+1\rangle}{\sqrt2},\qquad
 P_j=|d_j\rangle\langle d_j|,
 \quad Q_j=I-P_j,
 \quad J_j=|s_j\rangle\langle d_j|.                       \tag{2}
\]

Here I is the full pointer identity until an explicit even restriction is
made. The vectors d_j and s_j are orthonormal. Set

\[
 \nu_j=\frac{d_j\otimes|0\rangle-s_j\otimes|1\rangle}{\sqrt2},
 \qquad U_j=I-2|\nu_j\rangle\langle\nu_j|.                    \tag{3}
\]

Since \(|\nu_j\rangle\) is normalized, its rank-one projector squares to
itself. Thus \(U_j^*=U_j\) and \(U_j^2=I\). In particular

\[
 U_j(d_j\otimes|0\rangle)=s_j\otimes|1\rangle,
 \quad
 U_j(s_j\otimes|1\rangle)=d_j\otimes|0\rangle,               \tag{4}
\]

and U_j fixes the orthogonal complement of their span. These identities
prove the inverse on the whole pointer/bath space, not merely on the
fresh-bath input slice. Tensoring with identities proves the same claim
in the presence of arbitrary correlations with other coordinates. The
odd pointer sector is orthogonal to both d_j and s_j, so U_j is the
identity on that sector tensored with either bath state.

With \(P_{s,j}=|s_j\rangle\langle s_j|\), the bath-block form is

\[
 U_j=Q_j\otimes|0\rangle\langle0|
   +(I-P_{s,j})\otimes|1\rangle\langle1|
   +J_j\otimes|1\rangle\langle0|
   +J_j^*\otimes|0\rangle\langle1|.                       \tag{5}
\]

Consequently, for every pointer vector, not only an even one,

\[
 U_j(\psi\otimes|0\rangle)
      =Q_j\psi\otimes|0\rangle+J_j\psi\otimes|1\rangle.     \tag{6}
\]

The specified effective Hamiltonian is

\[
 H_j(t)=\hbar g_j(t)|\nu_j\rangle\langle\nu_j|,
 \qquad \int g_j(t)\,dt=\pi.
\]

Its values at different times commute. Its propagator is therefore

\[
 \exp\!\left(-i\pi|\nu_j\rangle\langle\nu_j|\right)
   =I+(e^{-i\pi}-1)|\nu_j\rangle\langle\nu_j|=U_j.         \tag{7}
\]

Equation (7) specifies the relative signs and exact pulse area. It is not
the different exchange Hamiltonian with a pi/2 pulse and minus-i swap
phases. The primitive contains only the two named internal modes and the
fresh qubit; it contains no global E projector, Fourier operation, C
context projector, or source-dependent switch. Its phase-aligned coherent
coupling and classical drive are nevertheless supplied effective controls,
not derived physical resources.

Tracing the bath of (6), with all other coordinates retained, yields

\[
 \Phi_j(X)=Q_jXQ_j+J_jXJ_j^*,\qquad
 Q_j^*Q_j+J_j^*J_j=Q_j+P_j=I.                              \tag{8}
\]

Thus the reduced map is completely positive and trace preserving (CPTP).
The trace here is a mathematical reduction of a retained state. It is
neither a bath measurement nor a conditional normalization.

## 3. Full joint state, inverse and resource account

Number the B collisions in script order. Let \(V_t\) be the corresponding
U_j on its addressed pointer and qubit, extended by identity elsewhere,
and let \(W=V_B\cdots V_1\). Then

\[
 W^{-1}=V_1\cdots V_B.                                    \tag{9}
\]

The identity holds on all states, including dirty, entangled baths. On
the specified fresh inputs, iteration of (6) gives the isometry

\[
 W(\psi\otimes|0^B\rangle)
      =\sum_{u\in\{0,1\}^B}K_u\psi\otimes|u\rangle,
 \qquad
 K_u=T_{B,u_B}\cdots T_{1,u_1},                            \tag{10}
\]

where \(T_{t,0}=Q_{j_t}\) and \(T_{t,1}=J_{j_t}\) act on the named pointer.
Every T also acts identically on Z and the other pointers. By linearity,
for an arbitrary admitted joint density,

\[
 \Omega_{\rm out}
 =W[\Omega\otimes|0^B\rangle\langle0^B|]W^*
 =\sum_{u,v}K_u\Omega K_v^*\otimes|u\rangle\langle v|.     \tag{11}
\]

All ket/bra cross terms remain in (11). It determines correlations with
the source and reference as well as with every bath. The corresponding
reduced pointer/Z map is the ordered composition of (8). Since channels
on distinct pointers commute, it is also

\[
 \left(\bigotimes_i\Phi^{n_i}\right)\otimes\operatorname{id}_Z,
 \qquad \Phi=\Phi_{L-1}\cdots\Phi_0.                       \tag{12}
\]

Because W acts on no Z coordinate, local-unitary invariance of the partial
trace gives

\[
 \Omega_{Z,\rm out}=\Omega_{Z,\rm in}.                     \tag{13}
\]

This does not assert that Z stays uncorrelated with the bath. For example,
initial source/pointer correlations may become source/bath correlations.

The resource ledger is exactly B qubits, each supplied pure and retained
after use, with input and output being the same physical coordinates.
There is no second supply concealed in the notation. For equal n_i=n
this is mLn cells. The n_i=0 case has no collisions on pointer i; B=0
gives W=I. A request beyond the allocated addresses has no promised next
loading pulse. The external finite script returns RESOURCE_EXHAUSTED and
retains the state; it does not install a new absorbing quantum state.

The operation acts identically on all C packet fields, reserves, latch,
and archive flags. In particular a used flag is not erased. Initial zero
flags remain a separate premise for a fresh Stage-C run. Running W in
reverse restores the old joint state; it cannot both restore the bath
purity and keep information that was changed by the forward operation.
Loading a used archive pointer changes that record and is not passive
record retention.

In the selected bare energy ledger, C's pointer and flag energies are
flat at one, and both levels of each bath qubit have energy one. Hence

\[
 E_{\rm extended}=E_C+B.                                  \tag{14}
\]

Every affected pointer/bath state has the same bare energy and all other
coordinates are fixed by U_j. Thus \([U_j,E_{\rm extended}]=0\) on the
entire carrier; the supplied H_j also commutes with this bare ledger.
Neither this commutation nor (7) accounts for the physical work of the
external drive. The consumed resource is fresh purity and available
storage. E is not selected as a lower-energy state by a flat spectrum.
The graph operator in the next section is a mathematical defect
diagnostic, not a derived physical Hamiltonian or an SI energy dictionary.

## 4. Exact one-edge fidelity gain

From this section through the contraction theorem, every operator is
restricted to the even space \(A^{\rm e}\), and I means \(I_{\rm e}\).
The odd sector must not be included in a positive gap or uniqueness claim.

Directly,

\[
 \langle d_j,E_L\rangle=0,\qquad
 \langle s_j,E_L\rangle=\sqrt{2/L}.
\]

It follows that \(Q_jE_L=E_L\), \(J_jE_L=0\), and

\[
 \Phi_j(P_E)=P_E,
 \quad
 \Phi_j^*(P_E)=Q_jP_EQ_j+J_j^*P_EJ_j
             =P_E+\frac2L P_j.                           \tag{15}
\]

For any density rho on the even space,

\[
 \operatorname{Tr}(P_E\Phi_j(\rho))-
 \operatorname{Tr}(P_E\rho)=\frac2L\operatorname{Tr}(P_j\rho).\tag{16}
\]

No independence of rho from a retained reference is needed: rho can be
the marginal at that time of an arbitrary joint state. Every new bath is
still a fresh independent zero because no earlier collision addressed it.

## 5. No-jump lower bound for a complete sweep

Write the prefix channel and its no-jump operator as

\[
 \mathcal T_j=\Phi_{j-1}\cdots\Phi_0,\qquad
 A_j=Q_{j-1}\cdots Q_0,\qquad
 \mathcal T_0=\operatorname{id},\quad A_0=I,
\]

and let \(A=A_L\). Telescoping (15) through the channel prefixes gives

\[
 \Phi^*(P_E)-P_E=\frac2L\sum_{j=0}^{L-1}\mathcal T_j^*(P_j).
                                                                    \tag{17}
\]

The Kraus expansion of a prefix contains the all-Q history A_j. Since
P_j is positive, every other Kraus contribution to
\(\mathcal T_j^*(P_j)\) is positive. Consequently

\[
 \mathcal T_j^*(P_j)\succeq A_j^*P_jA_j.
\]

Moreover \(A_{j+1}=Q_jA_j\) and \(Q_j^2=Q_j\), so

\[
 A_j^*A_j-A_{j+1}^*A_{j+1}=A_j^*P_jA_j.
\]

Summing these identities proves the exact telescoping loss and its
channel consequence:

\[
 \sum_j A_j^*P_jA_j=I-A^*A,
 \qquad
 \Phi^*(P_E)-P_E\succeq\frac2L(I-A^*A).                   \tag{18}
\]

The positive terms omitted in this lower bound are still retained in
the full state (11). Taking a lower bound does not remove histories from
the mechanism.

## 6. Sequential overlap estimate, including the closing edge

Let \(\psi\perp E_L\), \(x_0=\psi\), and

\[
 x_{j+1}=Q_jx_j=x_j-a_jd_j,\qquad
 a_j=\langle d_j,x_j\rangle,
 \quad b_j=\langle d_j,\psi\rangle.
\]

Orthogonal projection loses exactly \(|a_j|^2\) of squared norm, whence

\[
 D_\psi:=\|\psi\|^2-\|A\psi\|^2
     =\sum_{j=0}^{L-1}|a_j|^2.                          \tag{19}
\]

Also \(x_j=\psi-\sum_{k<j}a_kd_k\), so

\[
 b_j=a_j+\sum_{k<j}a_k\langle d_j,d_k\rangle.              \tag{20}
\]

For a cycle of length at least three, distinct neighboring edge
differences have overlap -1/2 and disjoint edge differences have overlap
zero. For L=3 every pair of distinct edges is neighboring; (20) still
has exactly the following form:

\[
 \begin{aligned}
 b_0&=a_0,\\
 b_j&=a_j-a_{j-1}/2 &&(1\le j\le L-2),\\
 b_{L-1}&=a_{L-1}-(a_{L-2}+a_0)/2. &&
 \end{aligned}                                             \tag{21}
\]

The final a_0 term is the closing-edge overlap and cannot be dropped.
Let T be the matrix \(b=Ta\). Each diagonal entry is 1, each nonzero
off-diagonal entry is -1/2, and every row and column has absolute sum at
most 2. In particular the first column contains its diagonal and the
contributions to rows 1 and L-1; its sum is exactly 2, also for L=3.

For completeness, weighted Cauchy-Schwarz proves the required matrix
norm estimate without finding singular values:

\[
 \begin{aligned}
 \sum_j|(Ta)_j|^2
 &\le\sum_j\left(\sum_k|T_{jk}|\right)
                  \left(\sum_k|T_{jk}||a_k|^2\right)\\
 &\le2\sum_k|a_k|^2\sum_j|T_{jk}|
 \le4\sum_k|a_k|^2.
 \end{aligned}                                             \tag{22}
\]

Combining (19)-(22),

\[
 \langle\psi,(\sum_jP_j)\psi\rangle
       =\sum_j|b_j|^2\le4D_\psi.                        \tag{23}
\]

## 7. Cycle gap and uniform rational contraction

Let \(G=\sum_jP_j\). In the even position basis its action is

\[
 (Gv)_j=v_j-\tfrac12(v_{j-1}+v_{j+1}).
\]

The orthonormal Fourier vectors with components
\(L^{-1/2}\exp(2\pi i k j/L)\), k=0,...,L-1, therefore have eigenvalues

\[
 \mu_k=1-\cos(2\pi k/L).
\]

This use of Fourier vectors proves a graph inequality; it does not add
a Fourier gate to the loader. The k=0 vector is E_L. Symmetry and
monotonicity of cosine on [0,pi] show that the smallest nonzero
eigenvalue is

\[
 \lambda_L=1-\cos(2\pi/L)=2\sin^2(\pi/L).
\]

On [0,pi/2], concavity of sine places it above the chord between its
endpoints: \(\sin x\ge2x/\pi\). Since L>=3 places pi/L in this interval,

\[
 \lambda_L\ge\frac8{L^2},\qquad
 G\succeq\lambda_L(I-P_E)\succeq\frac8{L^2}(I-P_E).       \tag{24}
\]

Applying (24) to (23) gives, for every \(\psi\perp E_L\),

\[
 \langle\psi,(I-A^*A)\psi\rangle
       \ge\frac{\lambda_L}{4}\|\psi\|^2
       \ge\frac2{L^2}\|\psi\|^2.                         \tag{25}
\]

Each Q_j fixes E_L, and its adjoint is itself. Thus both A and A^* fix
E_L; \(I-A^*A\) annihilates E_L and has zero cross terms with that line.
The quadratic-form estimate extends to the operator inequality on the
whole even space:

\[
 I-A^*A\succeq\frac{\lambda_L}{4}(I-P_E)
          \succeq\frac2{L^2}(I-P_E).                     \tag{26}
\]

Together, (18) and (26) prove

\[
 \Phi^*(P_E)-P_E\succeq
 \frac{\lambda_L}{2L}(I-P_E)
 \succeq\frac4{L^3}(I-P_E).                              \tag{27}
\]

Taking the expectation in any even-supported density rho, with
\(F=\operatorname{Tr}(P_E\rho)\), proves

\[
 1-\operatorname{Tr}(P_E\Phi(\rho))\le r_L(1-F).
\]

Induction, including the n=0 identity case, yields

\[
 1-\operatorname{Tr}(P_E\Phi^n(\rho))
      \le r_L^n(1-F).                                    \tag{28}
\]

The same derivation permits the sharper factor
\(1-\lambda_L/(2L)\). The rational factor r_L is a conservative bound,
not a claimed optimum. Since \(0<r_L<1\) for L>=3, the fidelity converges
to one. The projection estimate proved in sections 8-9, with no
nontrivial remainder system, also gives trace-distance convergence.

If an even-supported density is stationary, (27) forces F=1. Positivity
then confines its support to the rank-one P_E space, and trace one makes
it P_E. Equation (15) proves existence, so P_E is the unique stationary
density **on the even sector**. Odd states are unaffected and refute a
full-carrier uniqueness claim. The proof does not require the ordered
sweep channel to be translation covariant; its chosen starting edge is
part of the script.

## 8. Correlated bank fidelity and exact marginal decomposition

Take the complete output (11). Because the reduced map is (12), the
marginal of pointer i evolves by exactly \(\Phi^{n_i}\), even when its
input is correlated with every other factor. Trace preservation on the
other pointers is sufficient for this marginal assertion. Thus (28)
gives the individual losses

\[
 1-F_{i,\rm out}\le r_L^{n_i}(1-F_{i,0}).                  \tag{29}
\]

Write \(R=P_E^{\otimes m}\) and \(\Pi=R\otimes I_{Z'}\). The commuting
pointer projections obey

\[
 I-\prod_iP_{E,i}\preceq\sum_i(I-P_{E,i}).                 \tag{30}
\]

Indeed their joint eigenvalues are zero or one and the inequality
reduces to \(1-\prod_i t_i\le\sum_i(1-t_i)\). In the two-pointer case the
positive difference is exactly
\((I-P_{E,1})(I-P_{E,2})\). Therefore, with

\[
 \eta=1-\operatorname{Tr}(\Pi\Omega_{\rm out}),
\]

equations (29)-(30) imply \(0\le\eta\le\delta\le1\), for delta defined
in (1). No tensor-product hypothesis on the actual pointer bank was used.

We now prove the required full-state estimate for any density omega on
A tensor Z' and any rank-one ready projection R on A. Because R has rank
one, there is a positive subnormalized operator sigma on Z' such that

\[
 \Pi\omega\Pi=R\otimes\sigma,\qquad
 \operatorname{Tr}\sigma=1-\eta.                          \tag{31}
\]

Partial trace over A kills the off-diagonal blocks between R and its
orthogonal complement. One way to see this is to choose an A basis
whose first vector spans R: each diagonal A matrix element of a cross
block vanishes. It follows that

\[
 \omega_{Z'}=\sigma+\tau,
 \quad
 \tau=\operatorname{Tr}_A[(I-\Pi)\omega(I-\Pi)]\succeq0,
 \quad \operatorname{Tr}\tau=\eta.                       \tag{32}
\]

In particular the comparator uses the actual marginal \(\sigma+\tau\).
No independence or purity of that marginal is inferred.

## 9. Gentle estimate and full joint decoupling

Here is a direct proof of the unnormalized projection bound used with
(31). Purify omega as a unit vector \(\Psi\) on a larger space. Put
\(\phi=(\Pi\otimes I)\Psi\) and \(\chi=\Psi-\phi\). Then
\(\|\phi\|^2=1-\eta\), \(\|\chi\|^2=\eta\), and

\[
 |\Psi\rangle\langle\Psi|-|\phi\rangle\langle\phi|
    =|\chi\rangle\langle\Psi|+|\phi\rangle\langle\chi|.
\]

The trace norm of a rank-one outer product \(|u\rangle\langle v|\) is
\(\|u\|\|v\|\). The triangle inequality bounds this difference by
\(\sqrt\eta+\sqrt{1-\eta}\sqrt\eta\le2\sqrt\eta\). Partial trace
contracts the trace norm of a Hermitian operator: in the dual formula
\(\|Y\|_1=\max_{-I\preceq H\preceq I}\operatorname{Tr}(HY)\), an effect
H on the retained space is lifted to \(H\otimes I\) with the same order
bounds on the full space. Thus

\[
 \|\omega-\Pi\omega\Pi\|_1\le2\sqrt\eta.                 \tag{33}
\]

This derivation includes eta=0 and eta=1 and never normalizes a projected
branch. Equations (31)-(32) also give the exact second norm

\[
 \|\Pi\omega\Pi-R\otimes\omega_{Z'}\|_1
      =\|R\otimes\tau\|_1=\eta.                         \tag{34}
\]

The triangle inequality, (33)-(34), and the bound D<=1 for density
operators prove

\[
 D(\omega,R\otimes\omega_{Z'})
     \le\min\{1,\sqrt\eta+\eta/2\}
     \le\min\{1,\sqrt\delta+\delta/2\}.                  \tag{35}
\]

Applying this to \(\omega=\Omega_{\rm out}\) proves (1). It controls
coherences and every pointer/remainder correlation, including correlations
with all retained baths. Matching position populations alone would not
imply (35).

For a basis blank \(F_{i,0}=1/L\); for an arbitrary admitted density the
conservative inequality \(F_{i,0}\ge0\) suffices. Given
\(0<\epsilon_{\rm target}\le1\), if the un-clipped sum in (1) is at most
\(4\epsilon_{\rm target}^2/9\), then

\[
 \sqrt\delta+\delta/2
 \le\frac23\epsilon_{\rm target}
      +\frac29\epsilon_{\rm target}^2
 \le\frac89\epsilon_{\rm target}
 \le\epsilon_{\rm target}.                              \tag{36}
\]

This is sufficient, not an optimized resource formula. For equal n,
the declared exact conditions are respectively

\[
 m r_L^n\le4\epsilon_{\rm target}^2/9,
 \qquad
 m(1-1/L)r_L^n\le4\epsilon_{\rm target}^2/9.              \tag{37}
\]

Because \(0<r_L<1\), for every finite m and positive target there exists
a finite integer n satisfying either condition. Equations (36)-(37)
and B=mLn specify a finite budget without executing n collisions to
demonstrate the bound. A budget can be extremely conservative; no claim
of practical efficiency follows.

## 10. Handoff to any admitted finite Stage-C protocol

After loading, compare the actual state \(\Omega_{\rm out}\) with the
ideal comparator

\[
 \widetilde\Omega_{\rm in}=R\otimes\Omega_{Z',\rm out}.
\]

The comparator supplies the exact ready pointer bank while preserving
the **same actual** joint state of source, other C coordinates, reference
and bath outputs. It does not replace a correlated source/bath state by
the product of its marginals. Original Z is unchanged by (13), so
separately supplied C source/flag conditions are not repaired or weakened
by this comparison.

Fix an admitted C finite causal protocol of horizon h<=K, with identical
context choices and control descriptor in the two comparisons. Baths
are an untouched reference: the protocol neither reuses nor couples to
them and does not choose controls from their unrecorded contents. At each
conditional read retain the explicit outcome register and both branches.
At every bounded stopping leaf or declared status retain its output as
well. The resulting complete map \(\Lambda\), including the archive,
source, registers, reference and bath identities, is CPTP. To see why
adaptive finite control does not change this, sum all instrument
branches to obtain the trace-preserving map at the last node, and
work back to the root. Terminal leaves carry identity continuation.
No trace is lost by deleting zero or inconvenient leaves.

Any coherent program or setting register already admitted by C remains
part of this complete map. Its controlled unitaries and prescribed read
maps are CPTP; no extra dephasing of a coherent program is introduced
by the comparison. The decision-tree argument describes the explicitly
conditional read part. The distance argument itself applies to the
whole specified map, including retained coherent cross terms.

For completeness, CPTP trace-distance contraction follows from the
variational formula for a Hermitian trace-zero X:

\[
 \tfrac12\|X\|_1=\max_{0\preceq M\preceq I}
                         |\operatorname{Tr}(MX)|.
\]

The dual of a CPTP map is positive and unital, so it sends every output
effect M to an input effect between zero and I. Applying this formula
to \(X=\Omega_{\rm out}-\widetilde\Omega_{\rm in}\) gives

\[
 D(\Lambda(\Omega_{\rm out}),\Lambda(\widetilde\Omega_{\rm in}))
     \le\epsilon,\qquad
 \epsilon=\min\{1,\sqrt\delta+\delta/2\}.                 \tag{38}
\]

Equation (38) is a single comparison of complete protocol outputs. It
does not incur an additional factor h: the finite bank was loaded once
and the entire h-step protocol is one CPTP map applied to that comparison.
Tracing unused cells or all baths is another CPTP map and preserves the
same bound. This does not cover replacing consumed bath cells by
unregistered fresh ones or silently discarding the correlated remainder.

When the prescribed read instrument produces an explicit final outcome
register with blocks \(\tau_w\) and
\(\widetilde\tau_w\), contraction and the trace norm of a direct sum give

\[
 \sum_w\|\tau_w-\widetilde\tau_w\|_1\le2\epsilon.         \tag{39}
\]

Let \(p_w=\operatorname{Tr}\tau_w\) and
\(q_w=\operatorname{Tr}\widetilde\tau_w\). Since absolute trace is
bounded by trace norm,

\[
 \tfrac12\sum_w|p_w-q_w|\le\epsilon.                   \tag{40}
\]

Any complete prefix event is a union of retained final leaves, so its
weight differs by at most epsilon. These are formal quantum operator
traces. No actual outcome, actual record sequence or sampling measure
has been selected by this argument.

For a single branch, (39) implies
\(\|\tau-\widetilde\tau\|_1\le2\epsilon\). If its two weights p,q
are positive, writing

\[
 \frac\tau p-\frac{\widetilde\tau}q
     =\frac{\tau-\widetilde\tau}p
       +\widetilde\tau\left(\frac1p-\frac1q\right)
\]

and using \(|p-q|\le\|\tau-\widetilde\tau\|_1\) proves the stated
sufficient bound

\[
 D(\tau/p,\widetilde\tau/q)
      \le\min\left\{1,\frac{2\epsilon}{\min(p,q)}\right\}.\tag{41}
\]

This bound can become vacuous on rare branches. If q=0, there is no
normalized ideal branch to compare, and (40) only guarantees p<=epsilon.
Such a newly positive branch remains in the actual complete output.
No uniform small normalized-state error on arbitrarily rare prefixes
is claimed. A controller that accesses the baths lies outside the
declared Stage-C handoff and requires its own explicit comparison law.

## 11. Retained bath marks and the equal-population control

For collision t the incoming qubit is an independent zero. Equation (6)
shows that the expectation of its outgoing mark projector
\(|1\rangle\langle1|\) is

\[
 q_t=\operatorname{Tr}(J_j\rho_{t-1}J_j^*)
        =\operatorname{Tr}(P_j\rho_{t-1}).                 \tag{42}
\]

Later collisions do not touch that qubit, so its marginal expectation
is unchanged. From (16),

\[
 F_t-F_{t-1}=\frac2L q_t,
 \qquad
 \sum_{t=1}^{T}q_t=\frac L2(F_T-F_0).                    \tag{43}
\]

The sum on the left is exactly the expectation of the sum of the T
retained mark projectors, including when the baths are correlated. It
is not a claim that an actual observed number equals its expectation.
The flat ledger assigns no extra energy to mark one, so this is not an
emitted-energy count either.

For a basis blank \(F_0=1/L\). Since fidelity is at most one, every finite
sum in (43) is at most \((L-1)/2\). Along complete sweeps (28) makes
F_T tend to one, so the increasing finite sums have supremum and limit
\((L-1)/2\), which is 306 for L=613. This limiting statement describes
a sequence of larger finite scripts; it does not add an infinite bath
to any one execution.

The ready density P_E is fixed by every edge and gives q_t=0. In contrast,
for \(\rho_{\rm diag}=I_{\rm e}/L\), the first edge has q=1/L and

\[
 \Phi_j(I/L)=\frac{I-P_j+|s_j\rangle\langle s_j|}{L}
     =\frac IL+
       \frac{|j\rangle\langle j+1|+|j+1\rangle\langle j|}{L}.
                                                                    \tag{44}
\]

Both neighbor off-diagonal entries become 1/L; every position population
remains 1/L. Thus equal position populations do not identify the two
inputs. Both P_E and I/L are invariant under conjugation by a cyclic
translation, but only P_E is supported on the invariant-vector line.
The bath mark and newly generated coherence in (44) are independent
operator consequences of the local loader, not fitted C LOW/HIGH
probabilities or an actual-occurrence model.

## 12. Exact finite dyadic limitation

Let \(\mathcal D=\{a/2^b:a\in\mathbb Z,\ b\ge0\}\). It is closed
under addition and multiplication. At zero edge phases, the entries of
P_j, Q_j and J_j in the position basis are dyadic rational. The nonzero
entries of nu_j are plus or minus 1/2, so the entries of
\(U_j=I-2|\nu_j\rangle\langle\nu_j|\) are dyadic as well.

Finite products, multiplication of a dyadic density by U and U^*, and
finite partial traces all preserve dyadic entries. The same fact follows
from the finite Kraus expression (8). Hence every finite unconditional
reduced pointer density produced from a dyadic pointer density and the
basis baths is dyadic. The assertion also holds with real and imaginary
parts in \(\mathcal D\) if that more general convention is used.

The clean product basis input has a dyadic pointer density. Its supplied
\(\rho_Z\) need not be dyadic: W acts only on pointers and baths, so the reduced
pointer calculation is independent of \(\rho_Z\). It is therefore within the
obstruction even for an arbitrary separately prepared source/reference.

For L=613 every even position matrix entry of P_E is 1/613. If that number
were a/2^b, then \(2^b=613a\), impossible because the odd integer 613>1
cannot divide a power of two. Thus no finite unconditional loading script
with these exact zero-phase gates produces P_E from the basis blanks.
An exactly ready bank would have exactly ready single-pointer marginals,
so the same obstruction rules out an exact finite bank from those blanks.

This statement concerns the specified dyadic initial class and primitive.
It does not exclude preexisting E, arbitrary nondyadic correlated inputs,
I_even/613, normalized postselection, other phase primitives, or a
different preparation mechanism. Nor does it conflict with convergence:
dyadic entries may approach nondyadic values. The finite guarantee (1)
is deliberately approximate and does not literally discharge C's exact
ready premise without its separate error interface.

## 13. Phase holonomy, dirty baths and odd inputs

Put \(z_j=e^{i\theta_j}\), and replace the edge vectors by

\[
 d_j(\theta)=\frac{|j\rangle-z_j|j+1\rangle}{\sqrt2},\qquad
 s_j(\theta)=\frac{|j\rangle+z_j|j+1\rangle}{\sqrt2}.
\]

They remain orthonormal and the corresponding reflection is still an
all-state unitary. A common dark vector psi must satisfy

\[
 \langle d_j(\theta),\psi\rangle=0
 \quad\Longleftrightarrow\quad
 \psi_{j+1}=z_j\psi_j.                                    \tag{45}
\]

Iteration determines all components from psi_0. Closing the cycle gives
\((1-\prod_jz_j)\psi_0=0\). If the product is not one, all components
are zero and the difference matrix has rank L. If the product is one,
the kernel is one dimensional and the rank is L-1. Its normalized
generator has components

\[
 \psi_j=L^{-1/2}\prod_{k=0}^{j-1}z_k,
\]

with empty product one. All magnitudes are equal. Every local Q fixes
this vector and every local J annihilates it, so every corresponding
local channel fixes its pure density. This line equals the E_L line
exactly when all z_j=1. In particular a consistent nonconstant sign or
phase pattern changes the dark line. Nontrivial holonomy proves absence
of a common dark vector, not absence of every stationary density of a
phase-mismatched channel. The positive rate and Stage-C error theorem
were proved only for the zero-phase contract.

For a dirty incoming bath \(|1\rangle\), (5) instead gives

\[
 U_j(\psi\otimes|1\rangle)
     =J_j^*\psi\otimes|0\rangle
       +(I-|s_j\rangle\langle s_j|)\psi\otimes|1\rangle.\tag{46}
\]

Taking psi=E_L and alpha=\(\sqrt{2/L}\), the output is
\(\alpha d_j\otimes|0\rangle+(E_L-\alpha s_j)\otimes|1\rangle\).
Its E_L fidelity is exactly

\[
 |\alpha\langle E_L,d_j\rangle|^2
 +|1-\alpha\langle E_L,s_j\rangle|^2
       =(1-2/L)^2.                                      \tag{47}
\]

Thus a reused dirty bath can spoil even an already ready pointer. The
total inverse still exists, but the fresh-bath channel and convergence
guarantee do not apply. There is no hidden bath-freshness test.

Finally U_j is identity on the odd pointer subspace for either bath
state. Odd weight is invariant, and a purely odd input never becomes
E_L. No odd-sector leakage, dirty flag, or failed preparation condition
is removed by postselection. The total state remains defined on those
inputs, with no claimed positive loading guarantee.

## 14. Scope of the mathematical discharge

The construction supplies an explicitly counted finite unitary dilation
of an approximate pointer loader. It proves a uniform analytic rate,
the joint metric (1) against the actual retained remainder, finite
resource conditions, a complete finite Stage-C comparison without an
h multiplier, and separate bath/coherence diagnostics. The finite audit
domains in PREREG test exact instances of these identities; they do not
replace the universal proofs or certify L=613 by extrapolation.

The independent ideal E bank is replaced only in this approximate sense.
Remaining premises are the even-mode graph and its embedding, supplied
phase-sensitive local reflection and pulse area, external address/clock
script, fresh pure basis baths and storage, C source-code loading and
context controls, initial zero archive flags, and the complex quantum
state/channel formalism with the selected flat bare energy. A microscopic
realization of these controls and its physical work cost remains open.

Every bath is retained; no E pointer, global Fourier preparation,
postselection, implicit bath reset or outcome-based tuning is supplied
as a replacement premise. Formal instrument traces remain formal traces.
This proof derives neither actual parity occurrence nor a realized record
history nor its sampling law. It makes no native-U, Born-origin, hardware,
empirical, Canon-promotion or physical-closure claim, and it does not
change the registered scope of QDD-INSTRUMENT-APPARATUS,
QDD-TERMINAL-EVENT-SEMANTICS or QDD-INSTRUMENT-CLASS-COMPLETENESS.
