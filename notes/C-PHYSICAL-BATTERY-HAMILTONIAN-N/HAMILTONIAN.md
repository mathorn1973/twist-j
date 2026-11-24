# A local Hamiltonian with a physical battery and an additive bare energy

**Status: NON-CANONICAL, L1, candidate-T.** This is an analytical construction
in an explicitly added finite qubit model. It has no independent mathematical
acceptance and reports no new scientific execution. The target finite word
and its number-conserving compilation are specified in
[COMPILATION.md](COMPILATION.md); the initially supplied coherent fuel and
battery preparation are specified in [FUEL.md](FUEL.md).

The result is an exact endpoint implementation of that complete word by one
positive, time-independent, geometrically local Hamiltonian. Battery energy
is an actual positive onsite part of this same Hamiltonian. The coherent fuel
is an initial resource, and the localized clock is another nonstationary
resource. Neither is obtained by resetting an unknown state or by starting
all apparatus degrees of freedom in the ground state of the running law.

The endpoint does not provide an exact interval of physical storage. A
logical buffer of native steps in the target word is not a physical holding
time under this Hamiltonian. The finite physical reading window is bounded
separately below, using the variance of the complete physical Hamiltonian.

## 1. Target, encoding and actual elementary circuit

Let the finite target system have integer energy account \(N_S\) with
spectrum in \(\{0,\ldots,q_{\max}\}\). Choose

\[
Q=5^{2r}\geq q_{\max},\qquad \ell=2r+22,\qquad
L=5^\ell,\qquad B_{\max}=L+2Q-1.
\tag{H1}
\]

The battery has encoded levels \(0,\ldots,B_{\max}\). Its desired charged
state is

\[
|b_L\rangle=L^{-1/2}\sum_{n=0}^{L-1}|Q+n\rangle.
\tag{H2}
\]

The system encoding uses \(n_S\) dual-rail binary digits and a unary register
for \(N_S\). Every valid system codeword therefore has physical excitation
number \(n_S+q\) when its target energy is \(q\). The battery uses its
thermometer code. The fuel consists of \(Q\) charged qubits and \(L-1\)
donor qubits. The latter are grouped into the explicit coherent blocks in
FUEL.md, whose total excitation number is uniform on
\(0,\ldots,L-1\). These are blocks of identical-gap physical qubits; they
are not asserted to be independently prepared single-qubit superpositions.
The core width and clean compilation work space are

\[
P=2n_S+Q+B_{\max}+Q+(L-1),\qquad
A=P,\qquad S=P+2A=3P.
\tag{H3}
\]

Each of the \(A\) clean work pairs starts in its specified one-excitation
basis state and is restored at a completed macro boundary. Its energy cost
is \(A\epsilon\), rather than zero.

The preparation macro exchanges the disjoint equal-energy input and output
basis pairs defined in FUEL.md. It sends the stated coherent fuel,
with battery initially empty, exactly to (H2), with that fuel discharged.
The subsequent funded macros preserve the sum of the encoded system and
battery energy. Their extensions, compilation and all intermediate physical
gates preserve total excitation number on the entire raw qubit space.

Write the actual compiled circuit as

\[
C=U_{R_g}\cdots U_1.
\tag{H4}
\]

Here \(R_g\geq1\) is its actual elementary length, not a numerical claim
that the upper bound in COMPILATION.md is attained. Each \(U_t\) is unitary,
acts on at most four consecutive cells of a line of \(S\) qubits, and
commutes with their excitation-number sum on all raw input states.
Routing SWAPs and the clean-work computation are included in this list.
If the complete target has \(\nu=1+L_{\rm prog}+h\) macros, the conservative
compiler bound is

\[
R_g\leq128\nu P^3 4^P.
\tag{H5}
\]

The default choice is \(h=0\). A chosen finite suffix of \(h\) native
steps is part of the encoded target, not a subsequent physical release of
this hardware. The scheduler construction below depends only on (H4) and
its stated locality and number-conservation properties.

## 2. A fixed two-dimensional layout

For \(t=0,\ldots,R_g\) and \(j=1,\ldots,S\), put a data qubit
\(D_{t,j}\) at the square-lattice position \((j,2t)\). There are

\[
N_{\rm data}=(R_g+1)S
\tag{H6}
\]

data qubits. Row zero contains the entire initial circuit input, including
the charged work pairs and coherent fuel. All subsequent rows start in
\(|0\rangle^{\otimes S}\).

For stage \(t=0,\ldots,R_g-1\), put a horizontal clock rail at
\((j,2t+1)\), \(j=0,\ldots,S+1\). Traverse even stages from left to
right and odd stages from right to left. Join successive rails by one clock
site at the shared guard column and vertical coordinate \(2t+2\). The
result is a simple nearest-neighbor snake with

\[
K=R_g(S+2)+(R_g-1)=R_g(S+3)-1
\tag{H7}
\]

physical clock qubits, labeled \(c_1,\ldots,c_K\) along the snake. They
have zero bare splitting. Their propagation terms below are part of the
physical energy. The layout fits in a rectangle of width \(S+2\) and
height \(2R_g+1\) lattice sites, with unused positions omitted.

Assign one data instruction \(G_k\) to the clock site \(c_{k+1}\),
\(k=0,\ldots,K-1\). At a guard or connector site, let \(G_k=I\).
At active column \(j\) in stage \(t\), first SWAP \(D_{t,j}\) with
\(D_{t+1,j}\). At the last visited column in the support of \(U_{t+1}\),
apply \(U_{t+1}\) on its destination-row cells immediately after that
SWAP. By then all its operands have been transferred. No additional gate is
applied at the other active columns.

Each \(G_k\) touches at most five data qubits: four destination operands
and the source cell of the current transfer. Both its transfer and gate
commute with total physical data excitation number. Every stage implements
its prescribed gate while transferring the whole row. Consequently, if

\[
F_0=I,\qquad F_j=G_{j-1}\cdots G_0,
\tag{H8}
\]

then, for every initial row vector \(|\psi\rangle\),

\[
F_K\bigl(|\psi\rangle_0\otimes|0\rangle_{1,\ldots,R_g}\bigr)
 =|0\rangle_{0,\ldots,R_g-1}\otimes C|\psi\rangle_{R_g}.
\tag{H9}
\]

The SWAPs define full unitaries even if other rows are dirty. Equation (H9)
uses their stated fresh-row input. No dirty row or rejected history is traced
out to establish unitarity or the endpoint identity. Arbitrary passive
reference systems can be tensored through every equation.

## 3. Positive domain-wall propagation on the full raw space

Introduce fixed virtual boundary bits \(c_0=1\) and \(c_{K+1}=0\).
They are constants, not additional physical qubits. The legal clock basis is

\[
|j\rangle_c=|1\rangle^{\otimes j}|0\rangle^{\otimes(K-j)},
\qquad j=0,\ldots,K.
\tag{H10}
\]

Thus the initial clock is the actual product basis state with all physical
clock qubits zero. It needs no initially supplied one-excitation wave packet.
For \(k=0,\ldots,K-1\), define, with virtual factors replaced by their
fixed values,

\[
P_k=|1\rangle\langle1|_{c_k}\otimes I_{c_{k+1}}
       \otimes|0\rangle\langle0|_{c_{k+2}},\qquad
B_k=|110\rangle\langle100|_{c_kc_{k+1}c_{k+2}}.
\tag{H11}
\]

Choose an energy scale \(g>0\) and set

\[
a_k=\frac{g}{K+1}\sqrt{(k+1)(K-k)},\qquad
 a_{-1}=a_K=0,
\]
\[
b_j=|1\rangle\langle1|_{c_j}\otimes|0\rangle\langle0|_{c_{j+1}},
\qquad v_j=g-a_{j-1}-a_j\quad(0\leq j\leq K).
\tag{H12}
\]

The propagation Hamiltonian is

\[
h_k=a_k\left(P_k\otimes I-B_k\otimes G_k-B_k^*\otimes G_k^*\right),
\qquad
H_{\rm prop}=\sum_{k=0}^{K-1}h_k+\sum_{j=0}^{K}v_jb_j\otimes I.
\tag{H13}
\]

This formula is defined on every raw clock and data state. On the active
\(100,110\) clock block, \(h_k/a_k\) has diagonal blocks \(I,I\) and
unitary off-diagonal blocks \(-G_k,-G_k^*\); it is positive with eigenvalues
zero and two. It vanishes outside that block. Also
\(0\leq a_k\leq g/2\), so \(v_j\geq0\). Hence

\[
0\leq h_k\leq2a_kI\leq gI,\qquad
0\leq v_jb_j\leq gI,
\]
\[
0\leq H_{\rm prop}\leq
 \left(2\sum_k a_k+\sum_jv_j\right)I=(K+1)gI.
\tag{H14}
\]

No positivity or unitarity assertion silently discards illegal domain-wall
strings. The legal clock subspace is invariant: a legal string has just one
\(10\) boundary, and (H11) moves it one site forwards or backwards.

Each \(h_k\) acts on at most three clock and five data qubits. Every
participating site is at Manhattan distance at most four from its active
clock site. Each potential term has range one. A clock site belongs to at
most three propagation and two potential terms. A data site belongs to at
most its incoming and outgoing transfer terms and one separate gate term.
Thus the conservative term-valence bound is five before adding onsite
energies, and six afterwards. The graph joining sites that share a term has
degree at most \(5(8-1)=35\); onsite terms do not add neighbors. These
bounds are independent of \(S,R_g,Q,L\). All local dimensions are two.

The adjoint \(G_k^*\) in (H13) is a real reverse history hop required by
Hermiticity. This Hamiltonian is not a strictly one-way microscopic motion.
Its exact endpoint realizes the declared forward target word without an
inverse cleanup of the target state. Those are distinct statements.

## 4. The physical onsite energy and its commutation with propagation

Give every data qubit the same physical gap \(\epsilon>0\), and define

\[
N_{\rm data}^{\rm occ}=\sum_{t=0}^{R_g}\sum_{j=1}^{S}
 |1\rangle\langle1|_{D_{t,j}},\qquad
H_0=\epsilon N_{\rm data}^{\rm occ},\qquad
H_{\rm tot}=H_0+H_{\rm prop}.
\tag{H15}
\]

The superscript distinguishes the occupation operator from the number of
data sites in (H6). Bare clock energies are zero. Each onsite summand has
norm \(\epsilon\), and the propagation terms have norm at most \(g\).
There are no negative bare-energy or interaction counterterms.

Every \(G_k\) preserves \(N_{\rm data}^{\rm occ}\) on the full raw
space, while all clock operators commute with it. Therefore, term by term,

\[
[H_0,H_{\rm prop}]=0,\qquad
0\leq H_{\rm tot}\leq
 \bigl(\epsilon N_{\rm data}+(K+1)g\bigr)I.
\tag{H16}
\]

This gives a finite positive physical Hamiltonian with uniform local energy
bounds and geometrically local interactions. The total number of physical
qubits is \(N_{\rm data}+K\). It does not give a small apparatus or a
short physical duration. The exponential compiler bound and the large unary
reservoir are actual resources of this construction.

## 5. Exact endpoint of the same stationary Hamiltonian

On legal histories use the unitary change of description

\[
\mathcal W(|j\rangle_c\otimes|\psi\rangle)
 =|j\rangle_c\otimes F_j|\psi\rangle.
\tag{H17}
\]

It is used only to prove the evolution; it is not an extra operation. Since
all \(F_j\) preserve the data number,

\[
\mathcal W^*H_0\mathcal W=I_c\otimes H_0,
\]
\[
\mathcal W^*H_{\rm prop}\mathcal W
 =\left(gI_c-A_K\right)\otimes I,\qquad
A_K=\sum_{k=0}^{K-1}a_k(|k+1\rangle\langle k|+|k\rangle\langle k+1|).
\tag{H18}
\]

The diagonal is exactly \(g\), since the two adjacent propagation
diagonals and \(v_j\) add to \(g\). The matrix \(A_K\) is
\(2g/(K+1)\) times the spin-\(K/2\) matrix \(J_x\), in units where
its matrix entries are dimensionless. A rotation by \(\pi\) takes one
extreme-weight vector to the other with phase \(i^K\). Thus at

\[
\tau=\frac{\pi\hbar(K+1)}{2g}
\tag{H19}
\]

one has

\[
e^{-i\tau H_{\rm prop}/\hbar}
  (|0\rangle_c\otimes|\psi\rangle)
 =-i|K\rangle_c\otimes F_K|\psi\rangle.
\tag{H20}
\]

Here \(|\psi\rangle\) can include all data rows and an arbitrary
reference, and the reference is unaffected. Equation (H20) does not measure
or postselect the clock. Perfect transfer by engineered fixed couplings is a
known construction; see Christandl, Datta, Ekert and Landahl,
[Perfect state transfer in quantum spin networks](https://arxiv.org/abs/quant-ph/0309131v2).
The present proof states the required clock matrix and phases explicitly.

To include the bare physical energy without unwanted endpoint phases, fix

\[
\epsilon=4g.
\tag{H21}
\]

Then \(\epsilon\tau/\hbar=2\pi(K+1)\), and the integer spectrum of
\(N_{\rm data}^{\rm occ}\) gives

\[
e^{-i\tau H_0/\hbar}=I
\tag{H22}
\]

on the entire raw space, including coherent superpositions of different
energies. Commutation (H16) now proves the full physical endpoint identity

\[
\boxed{
 e^{-i\tau H_{\rm tot}/\hbar}
 \bigl(|0\rangle_c\otimes|\psi\rangle_0\otimes|0\rangle_{1,\ldots,R_g}\bigr)
 =-i|K\rangle_c\otimes|0\rangle_{0,\ldots,R_g-1}
       \otimes C|\psi\rangle_{R_g}.}
\tag{H23}
\]

The equality includes battery charging, all compiled target operations, all
auxiliary histories and all passive references. It contains no stochastic
law for realized events. For any other choice of \(\epsilon/g\), the
known free evolution \(e^{-i\tau H_0/\hbar}\) must be retained; it cannot
be omitted when the fuel is energy-coherent.

A Hamiltonian compiled for the preparation macro alone yields the exactly
charged state (H2) at its endpoint. A Hamiltonian compiled for preparation
followed by the funded experiment yields the final joint state of that
whole word at its endpoint. Its intermediate physical evolution is a
superposition of circuit histories. It does not first reach a unique,
fully charged physical time and then begin a separate clocked experiment.

## 6. Battery energy is a fixed positive part of the physical law

Let \(J_B\subset\{1,\ldots,S\}\) be the columns assigned to the
\(B_{\max}\) physical battery code qubits at circuit macro boundaries.
Define the battery bank to include these columns in every data row:

\[
H_B=\epsilon\sum_{t=0}^{R_g}\sum_{j\in J_B}
 |1\rangle\langle1|_{D_{t,j}},\qquad H_{\rm rest}=H_0-H_B\geq0.
\tag{H24}
\]

The full physical battery bank has \((R_g+1)B_{\max}\) qubits and raw
capacity \(\epsilon(R_g+1)B_{\max}\). The smaller capacity
\(\epsilon B_{\max}\) describes its valid code with only one active data
row. Empty battery copies in the other rows remain physical hardware and
are counted in (H6) and (H16). Similarly, the physical fuel columns occupy
\((R_g+1)(Q+L-1)\) qubits across all rows, although only the initial row
contains fuel at readiness. Their raw onsite capacity is
\(\epsilon(R_g+1)(Q+L-1)\).

This is a fixed physical subsystem and a positive onsite summand of
\(H_{\rm tot}\), not a state-dependent observable or a fitted ledger.
At a valid macro boundary, the line routing is restored, the previous rows
are empty, and the battery thermometer code has exactly \(n\)
excitations. The physical observable (H24) then equals its intended encoded
value \(\epsilon n\).

During routing, some logical labels can occupy columns outside their
assigned bank. Equation (H24) still defines the energy of the same physical
cells, but its identification with an abstract battery register is only
asserted at the restored code boundaries. Those boundaries are circuit
checkpoints; the autonomous evolution does not deterministically occupy
each at a separate physical time. At the final endpoint (H23) the
identification is exact.

For all physical times, commutation gives

\[
\Delta\langle H_0\rangle=0,\qquad
\Delta\langle H_{\rm prop}\rangle=0,\qquad
\Delta\langle H_B\rangle+\Delta\langle H_{\rm rest}\rangle=0.
\tag{H25}
\]

The preparation-only endpoint raises the initially empty battery's mean
energy by

\[
\epsilon\left(Q+\frac{L-1}{2}\right).
\tag{H26}
\]

The initially supplied fuel loses precisely that energy; its target output
is the all-zero state. The work pairs return with their initial excitation
count. Subsequent funded target operations redistribute energy between the
physical encoded system and battery. All gate and routing operations are
included in the conserved physical account (H25).

The interaction energy is not being silently set to zero. For the stated
initial clock it has mean \(g\), remains \(g\), and contributes to the
physical total energy below. It is not the source of the mean energy in
(H26), because it is separately conserved in this particular model.

## 7. Actual initial energy, coherence and reading tolerance

Consider the complete input specified in FUEL.md: the target system
has \(q=0\), its \(n_S\) dual-rail code pairs have one excitation each,
the \(A\) work pairs have one excitation each, the battery is empty, and
the fuel has excitation number \(Q+n\) with uniform amplitude for
\(n=0,\ldots,L-1\). Unknown label and reference states are allowed where
the target account is the identity. All other data rows and the physical
clock start at zero. Denote the complete initial vector by \(|\Omega\rangle\).

The exact bare-energy moments are

\[
\mu_0=\langle H_0\rangle
 =\epsilon\left(n_S+A+Q+\frac{L-1}{2}\right),\qquad
\operatorname{Var}(H_0)=\epsilon^2\frac{L^2-1}{12}.
\tag{H27}
\]

On a legal initial clock,

\[
H_{\rm prop}|\Omega\rangle
 =g|\Omega\rangle-a_0|1\rangle_c\otimes G_0|\psi\rangle,
\qquad a_0^2=\frac{g^2K}{(K+1)^2}.
\tag{H28}
\]

The second term is orthogonal in the clock to the first, even with arbitrary
reference entanglement. Therefore
\(\langle H_{\rm prop}\rangle=g\),
\(\operatorname{Var}(H_{\rm prop})=a_0^2\), and the covariance of
\(H_0\) with \(H_{\rm prop}\) on this initial state is zero. Hence

\[
\boxed{\mu=\langle H_{\rm tot}\rangle
 =\epsilon\left(n_S+A+Q+\frac{L-1}{2}\right)+g,}
\]
\[
\boxed{\sigma^2=\operatorname{Var}(H_{\rm tot})
 =\epsilon^2\frac{L^2-1}{12}+\frac{g^2K}{(K+1)^2}.}
\tag{H29}
\]

Both moments are conserved during the closed evolution. The localized
clock is not stationary for \(H_{\rm prop}\), and the supplied donor
blocks are not stationary for \(H_0\). In particular, making the physical
clock bare-degenerate does not create the donor coherence for free. Its
initial temporal variance for \(H_{\rm prop}\) supplies no nonzero
\(H_0\)-coherence mode: every physical clock vector has the same bare
energy zero, and \([H_{\rm prop},H_0]=0\). Thus the clock cannot silently
replace the specified donor in this additive energy account.

Indeed, if the complete initial state commuted with \(H_0\), (H16) would
preserve that symmetry. Since \(H_0\) is the sum of the battery and rest
onsite energies, the reduced battery would then commute with its own
\(H_B\). It could not become the pure state (H2) for \(L>1\). The
initial donor coherence is the explicit symmetry-breaking resource used by
the battery preparation. Preparing that resource from stationary inputs
requires another resource or a changed premise; no such preparation is
claimed here. The all-zero physical clock is a specified basis preparation,
not a unitary reset of an arbitrary clock state.

Let \(|\Omega(t)\rangle=e^{-itH_{\rm tot}/\hbar}|\Omega\rangle\).
The spectral theorem and \(|e^{-ix}-1|\leq|x|\) imply the complete-state
endpoint stability estimate

\[
\left\|e^{i\mu\delta t/\hbar}|\Omega(\tau+\delta t)\rangle
       -|\Omega(\tau)\rangle\right\|
 \leq\min\left\{2,\frac{|\delta t|\sigma}{\hbar}\right\}.
\tag{H30}
\]

The corresponding trace-distance error is at most
\(\min\{1,|\delta t|\sigma/\hbar\}\), also after partial trace.
This is an unconditional state bound; rare-outcome conditioning needs its
own error propagation.

For the clock endpoint probability alone, the spin matrix gives

\[
\Pr(c=K\text{ at }\tau+\delta t)
 =\cos^{2K}\left(\frac{g\delta t}{\hbar(K+1)}\right).
\tag{H31}
\]

The bare data evolution does not change this clock probability. A clock-only
bound therefore uses \(a_0\), but the coherent full output in (H30) uses
\(\sigma\). Replacing \(\sigma\) with \(a_0\) would omit the fuel's
physical energy variance and would be incorrect.

The path endpoint is not an absorbing halt. At \(2\tau\), the prepared
legal history returns to its initial state up to phase, including reversal
of the charging and computation. This recurrence is not reusable operation
with the new records retained. No exact physical storage interval after
\(\tau\), no switching mechanism, and no repeat-cycle reset are supplied
by (H23).

## 8. Scope relative to the original transfer law

The forward filter and finite source are the target of
[PR #1746](https://github.com/mathorn1973/twist-j/pull/1746). Its forward
controlled steps and complete histories remain the logical specification.
The finite account and funded lift in
[PR #1748](https://github.com/mathorn1973/twist-j/pull/1748) supply the target
energy-preserving macros. The local clock architecture in
[PR #1751](https://github.com/mathorn1973/twist-j/pull/1751) motivates the
scheduler used here, but its former physical-energy interpretation is not
silently inherited: (H15) explicitly adds the positive bare onsite energy,
and (H16), (H21)-(H23), and (H29) prove its consequences.

The geometry in this note is the geometry of the added qubit apparatus.
A target position coordinate is encoded information in that apparatus. A
controlled original step is compiled into an elementary circuit; it is not
asserted to be the original native spatial motion occurring without the
encoding. The assignment of \(N_S\) to a physical excitation code is a
chosen added dictionary, not a derivation of microscopic energies from the
original transfer law. The local tensor factors, fixed interactions,
identical onsite gaps, exact coupling values and prepared coherent donor
blocks are all additional model specifications.

Within that stated model, battery charging and the complete target word have
one closed positive Hamiltonian, an exact conserved additive bare energy,
and an exact reference-uniform endpoint. The construction establishes no
native-law implementation, independent mathematical acceptance, occurrence
rule, efficient resource scale, or permanent record protection.
