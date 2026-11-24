# A local source cursor, conserving Hamiltonian and accepted-output window

**NON-CANONICAL, L1, conditional candidate-T. Independent acceptance pending.**
Public reservation: [issue #1755](https://github.com/mathorn1973/twist-j/issues/1755).
This is an analytical construction; no new scientific execution is reported.

The inherited input is the finite sharp-energy circuit and accepted-channel
identity in [SHARP.md at 89f69e4][sharp], together with its
[local row layout at the same pin][layout]. Those candidate statements remain
conditional. This note replaces their supplied active domain-wall clock by
a physical source site coupled to an initially empty cursor line. It retains
all data histories, counts the new source and completion latch, and derives
its own reading times. [SOURCE.md](SOURCE.md) gives the source-resource
interpretation; the native-law audit is separate.

## 1. Inherited finite circuit and added completion latch

Use the pinned sharp circuit parameters

\[
Q_*=4259865,\qquad P_*=2n_*+3Q_*,\qquad A_*=P_*,\qquad S_*=3P_*.
\tag{H1}
\]

Here \(n_*\) is its registerwise binary information width, and \(A_*\)
is its count of clean dual-rail work pairs. Its actual elementary gate count
\(R_*\geq1\) obeys

\[
R_*\leq256P_*^3 4^{P_*}.
\tag{H2}
\]

The circuit includes sharp basis-fuel charging, the funded target, all work
and routing. Every elementary gate acts on at most four consecutive qubits
and preserves their total excitation number on the full raw space. Its
logical output is compared with the ideal accepted physical channel after
tracing the specified helpers and battery, not with an unchanged product
battery state.

The pinned layout uses \(R_*+1\) data rows and

\[
N=R_*(S_*+3)-1,\qquad N_{\rm data}=(R_*+1)S_*.
\tag{H3}
\]

Its instructions \(\widehat G_0,\ldots,\widehat G_{N-1}\) combine
transfers between rows with the elementary gates. They touch at most five
data qubits. The first instruction \(\widehat G_0=I\) is the initial
guard. Their complete product places the output on the fixed final row and
leaves previous rows empty. Those empty copies are physical hardware.

Add two fixed completion-latch qubits \(\lambda_0,\lambda_1\), initially
\(|10\rangle\), and prepend an idle preparation runway. Define

\[
A=N+1,\qquad L=2A,\qquad M=2L=4A,
\]
\[
G_j=I\ (0\leq j<A),\quad
G_{A+i-1}=\widehat G_{i-1}\ (1\leq i\leq N),\quad
G_{2A-1}=\operatorname{SWAP}_{\lambda_0,\lambda_1},\quad
G_j=I\ (L\leq j<M).
\tag{H4}
\]

The inherited instructions act as identity on this latch. Set
\(F_0=I\), \(F_j=G_{j-1}\cdots G_0\). Thus \(F_j=I\) for
\(0\leq j\leq A\). The latch is \(10\) for every prefix \(j<L\),
and \(01\) for every \(j\geq L\). Moreover \(F_j=F_L\) for
\(j\geq L\): the final identity tail makes no further data transfers.
The latch costs two qubits and one explicit initial excitation. The symbol
\(A\) is this runway length, distinct from the work-pair count \(A_*\).

## 2. Source, runway and cursor geometry

Keep the data sites \((x,2t)\), \(1\leq x\leq S_*\),
\(0\leq t\leq R_*\), and the pinned snake of N sites. Stage rails are
at \((x,2t+1)\), \(0\leq x\leq S_*+1\), with alternating directions
and one unit-step vertical connector between rails. Put the source and
runway sites at

\[
c_j=(-A-1+j,1),\qquad 0\leq j\leq A.
\]

The source is \(c_0\). Relabel pinned snake site i as \(c_{A+i}\), for
\(1\leq i\leq N\). Thus the runway ends at \((-1,1)\), next to the
initial guard \(c_{A+1}=(0,1)\). The last active site has index
\(A+N=2A-1\).

Let its final guard position be \((x_e,2R_*-1)\), with \(x_e=S_*+1\)
for a rightward final rail and \(x_e=0\) for a leftward rail. Write
\(s_e=1\) or \(-1\), respectively. Append \(2A+1\) cursor sites:

\[
c_{2A-1+r}=(x_e+r s_e,2R_*-1),\qquad 1\leq r\leq2A+1.
\tag{H5}
\]

Place the completion latch at \((x_e,2R_*)\) and
\((x_e+s_e,2R_*)\). These are outside the data columns, below the final
guard and first outward cursor site. A leftward final tail has \(R_*\)
even and at least two, so its height differs from the input runway. If
\(R_*=1\), the final rail and tail point right. Thus no new sites collide.
All cursor edges have unit lattice length. A conservative bounding rectangle
has width \(S_*+3A+4\) and height \(2R_*+1\), omitting unused sites.

Instruction \(G_j\) is attached to edge \(c_j\to c_{j+1}\). For the
inherited edges, its data operands belong to the pinned site
\(c_{j+1}\), hence remain within Manhattan radius four of that site.
The latch edge \(j=2A-1\) lies on the four-site plaquette at the final
guard. All runway and final-tail edges act on no data. In particular, the
source edge has \(G_0=I\) and touches only its two adjacent cursor qubits.

There are \(M+1\) physical cursor qubits, all with positive onsite gap.
The total physical qubit count is

\[
N_{\rm all}=N_{\rm data}+2+(M+1).
\tag{H6}
\]

The battery and basis-fuel banks each retain \((R_*+1)Q_*\) qubits across
the data rows. Their raw capacities are \(\epsilon(R_*+1)Q_*\), while
their single-active-row code capacities are \(\epsilon Q_*\). The added
cursor and latch do not replace or hide those copied banks.

## 3. A positive Hamiltonian on every raw state

For cursor site \(j\), let \(n_j=|1\rangle\langle1|_j\),
\(s_j^+=|1\rangle\langle0|_j\), and \(s_j^-=(s_j^+)^*\).
Define \(N_c=\sum_{j=0}^{M}n_j\), and let \(N_d\) count excitations
on all data and latch qubits. For any \(g,\epsilon>0\), set

\[
a_j=\frac{g}{M+1}\sqrt{(j+1)(M-j)},\quad 0\leq j<M,\qquad
 a_{-1}=a_M=0,\quad v_j=g-a_{j-1}-a_j.
\tag{H7}
\]

The full raw-space terms are

\[
h_j=a_j\left[(n_j+n_{j+1})\otimes I
 -s_{j+1}^+s_j^-\otimes G_j-s_j^+s_{j+1}^-\otimes G_j^*\right],
\]
\[
H_{\rm prop}=\sum_{j=0}^{M-1}h_j+\sum_{j=0}^{M}v_jn_j\otimes I
 =gN_c\otimes I-\sum_{j=0}^{M-1}a_j
 (s_{j+1}^+s_j^-\otimes G_j+s_j^+s_{j+1}^-\otimes G_j^*),
\]
\[
H_0=\epsilon(N_d+N_c),\qquad H_{\rm tot}=H_0+H_{\rm prop}.
\tag{H8}
\]

The cursor \(00\) block of \(h_j\) is zero, its \(11\) block is
\(2a_jI\), and its \(10,01\) block has diagonal entries \(a_jI\)
and unitary off-diagonal entries \(-a_jG_j,-a_jG_j^*\). That block is
positive with eigenvalues zero and \(2a_j\). Also \(a_j\leq g/2\)
and \(v_j\geq0\). Therefore

\[
0\leq h_j\leq2a_jI\leq gI,\quad 0\leq v_jn_j\leq gI,\qquad
0\leq H_{\rm prop}\leq(M+1)gI.
\tag{H9}
\]

The last bound follows from
\(2\sum_j a_j+\sum_jv_j=(M+1)g\). Every \(G_j\), including the
latch SWAP, preserves \(N_d\). Cursor hopping preserves \(N_c\).
Thus on the entire raw space, including multiple cursor excitations,

\[
[H_{\rm prop},N_d]=[H_{\rm prop},N_c]=[H_0,H_{\rm prop}]=0,
\qquad 0\leq H_{\rm tot}\leq
 [\epsilon N_{\rm all}+(M+1)g]I.
\tag{H10}
\]

Every propagating term has at most two cursor and five data operands, hence
at most seven qubits within Manhattan radius four. A cursor site belongs
to at most two edge terms, one potential and one onsite term. A data site
belongs to at most three edge terms and one onsite term; a latch site to
one edge and one onsite term. The term valence is at most four and the
co-support graph degree at most \(3(7-1)=18\). All local dimensions are
two. Each onsite term has norm \(\epsilon\), separately from the bound
\(g\) on each propagation or potential term.

Hermiticity includes the real reverse terms \(G_j^*\). The target remains
the declared chronological circuit; its microscopic implementation is not
a strictly one-way hopping law. No illegal-state projection, discarded
branch or negative cancellation of battery energy is used in (H8)-(H10).

## 4. Injection, exact history and initial physical energy

Initialize \(c_0=1\) and \(c_1=\cdots=c_M=0\). Write \(|j\rangle_c\)
for the state with exactly cursor site \(j\) occupied. The one-cursor
sector is invariant. Its history change of description
\(\mathcal W(|j\rangle\psi)=|j\rangle F_j\psi\) gives

\[
\mathcal W^*H_{\rm prop}\mathcal W
 =gI-\sum_{j=0}^{M-1}a_j(|j+1\rangle\langle j|+|j\rangle\langle j+1|)
 =gI-\frac{2g}{M+1}J_x.
\tag{H11}
\]

Here \(J_x\) is the dimensionless spin-\(M/2\) matrix. This analytical
conjugation is not an added physical operation. The initialized data has
sharp charge \(E_{\rm old}=n_*+A_*+Q_*\). The latch and source each
add one excitation, so the complete bare energy is exactly
\(E_0=\epsilon(E_{\rm old}+2)\). For any purified logical/reference input,

\[
|\Omega(t)\rangle=e^{-it(E_0+g)/\hbar}
 \sum_{j=0}^{M}\sqrt{\binom Mj}(i\sin\theta)^j
 (\cos\theta)^{M-j}|j\rangle_c F_j|\psi_0\rangle,
\qquad \theta=\frac{gt}{\hbar(M+1)}.
\tag{H12}
\]

This follows by expanding \(M\) identical two-state rotations in their
symmetric weight basis. At \(\tau_*=\pi\hbar(M+1)/(2g)\), only the
last term remains: the entire circuit, charging and latch are complete,
with every rejected history retained. The bare-energy phase is global at
all times on this sharp family. No relation \(\epsilon=4g\) is needed.

The initial and conserved physical moments are

\[
\langle H_{\rm tot}\rangle=\epsilon(E_{\rm old}+2)+g,\qquad
\operatorname{Var}(H_{\rm tot})=a_0^2=\frac{g^2M}{(M+1)^2}.
\tag{H13}
\]

The added cursor costs real bare energy \(\epsilon\), the latch another
\(\epsilon\), and the propagation mean \(g\) is counted. The empty
processor cursor is stationary for its isolated Hamiltonian; on the stated
sharp data even the full all-cursor-vacuum input is stationary. Replacing its
source bit by one gives a nonzero initial commutator only at the local
source edge: \([H_{\rm tot},\rho_0]_{1,0}=-a_0\rho_{\rm data}\), since
\(G_0=I\). This holds for mixed logical/reference inputs as well. The initial nonzero commutator is caused by this local bond; the global
energy-coherence distribution still depends on the full coupled Hamiltonian.

For example, the exact source occupation is \(\cos^{2M}\theta\).
The first processor-site probability is
\(M\sin^2\theta\cos^{2(M-1)}\theta\), whose maximum for \(M>1\) is
\((1-1/M)^{M-1}<1\). The prepared clock is instead a distributed packet
in the idle runway. For
\(1/16\leq p=\sin^2\theta\leq1/8\), the good positions \(1\leq j\leq A\)
have source empty and exactly unchanged data and latch. Their complement
has weight at most

\[
\delta_{\rm prep}=(15/16)^{4A}+(625/768)^A
 \leq2(5/6)^A.
\tag{H13a}
\]

The first term bounds remaining source occupation; the second bounds early
arrival past the runway. The normalized good component factors as a clock
packet times the original data/reference state. The actual unprojected
state has trace distance at most \(\sqrt{\delta_{\rm prep}}\) from that
product, without any physical conditioning. [PREPARATION.md](PREPARATION.md)
proves these claims, its nonzero time interval and the stronger reduced-data
bound. The concrete A is already at least 1024, giving
\(\delta_{\rm prep}<2^{-255}\). Loading and computation remain parts of
one continuous autonomous flow, not an exact stop between two stages.

## 5. A fixed-site read and a new continuous window

Let \(F_{\rm out}\) be the true-rail projector of the final-row acceptance
bit inherited from the pinned circuit. Define

\[
\Pi_{\rm read}=n_{\lambda_1}F_{\rm out},\qquad
w(t)=\sum_{j=L}^{M}\binom Mj\sin^{2j}\theta\cos^{2(M-j)}\theta.
\tag{H14}
\]

The latch excludes every unfinished prefix even if the primitive compiler
temporarily sets the acceptance bit. On all retained prefixes the data is
exactly \(F_L\psi_0\), in the same fixed output row. A single occupied
cursor bit would not provide this persistent completion test; the counted
latch is essential to this two-site observable.

Let \(\mathcal D\) trace the cursor, completion latch, empty rows, work,
fuel, battery, inner clock, system tally and auxiliary histories, then
remove the declared valid encoding of the retained object, carrier and
receiver information. The reference is retained. The pinned accepted-channel
identity and (H12) give the exact linear-map identity

\[
\mathcal D[\Pi_{\rm read}\rho(t)\Pi_{\rm read}]
 =w(t)\sigma_{\rm ideal},
\tag{H15}
\]

where \(\sigma_{\rm ideal}\) is the unnormalized ideal accepted physical
state, including arbitrary reference correlations. The clock trace removes
cross terms, and all surviving data vectors coincide. These are mathematical
read and reduction maps, not an implemented detector or physical erasure of
any history. The two read sites need not be adjacent.

For \(\pi\hbar(M+1)/(3g)\leq t\leq2\pi\hbar(M+1)/(3g)\), put
\(p=\sin^2\theta\geq3/4\). Binomial expansion and \(M=2L\) give

\[
1-w(t)\leq3^L(1-p+p/3)^{2L}\leq(3/4)^L=:\delta<10^{-30}.
\tag{H16}
\]

The first inequality applies the weight bound \(1_{j<L}\leq3^{L-j}\).
Here \(L\geq400\) already follows from (H1)-(H3), and
\((3/4)^4<1/2\) gives \(\delta<2^{-100}<10^{-30}\). This is a finite
norm-weight estimate, not a law of actual event frequencies. Using the
inherited candidate source bounds

\[
p_{\rm ideal}>p_0=\frac25\frac{1024}{15625}\frac{99}{50000},\quad
\frac{99}{100}p_0>\frac1{20000},\quad
r_{\rm ideal}<\frac{50000}{99\,2^{29}}<\frac1{10^6},
\]

(H15)-(H16) imply \(p_{\rm read}>1/20000\) and
\(r_{\rm read}=r_{\rm ideal}<1/10^6\) throughout this new interval.
These inherited spectral conclusions are conditional on the pinned source
proofs. The band observable is the same zero-extension readout, not a new
finite-box spectral projector. The accepted label/old-memory SWAP remains
exact; source label one gives receiver \(d_1\).

## 6. Conditional endpoint continuation and limits

At \(\tau_*\), mathematically project with \(\Pi_{\rm read}\), normalize
if its weight is nonzero, then evolve with the same \(H_{\rm tot}\).
The post-state has cursor exactly \(M\); the read commutes with \(H_0\)
and preserves the sharp energy sector. For source label one its receiver
is the correct \(d_1\) codeword on the fixed final row.

From cursor \(M\), the data at cursor position \(j\) is
\(F_jF_M^*\phi\) for any endpoint vector \(\phi\). It equals \(\phi\)
for every \(j\geq L\). For
\(0\leq u\leq\pi\hbar(M+1)/(6g)\), let
\(r=\sin^2(gu/[\hbar(M+1)])\leq1/4\). The weight of \(j<L\) is at most

\[
3^{-L}(1+2r)^{2L}\leq(3/4)^L=\delta.
\tag{H17}
\]

The wrong-receiver projector vanishes on the good tail and has norm at most
one elsewhere. Orthogonal cursor positions eliminate cross terms, proving
wrong-receiver weight at most \(\delta<10^{-30}\), including all retained
reference and battery correlations. Invalid or displaced receiver codes
count as wrong. This is a specified conditional continuation, not an
occurrence mechanism or a fresh preparation after measurement.

There is no permanent halt. The unmeasured sharp prepared flow returns to
its initial state up to phase at \(2\tau_*\), undoing the new records.
The finite tail buys a finite window and costs cursor sites and physical
time at bounded strength. It does not turn native flight-buffer estimates
into a physical duration, derive the qubit geometry from the original
particle coordinates, or prepare the supplied source from a state stationary
for this same full Hamiltonian. The latter obstruction and exact source
energy are treated in SOURCE.md. This note establishes a local autonomous
injection-and-computation law under those explicit initial resources.

[sharp]: https://github.com/mathorn1973/twist-j/blob/89f69e40f6ccfd950bf2e6c446ec38bc51f7f71b/notes/C-PHYSICAL-BATTERY-HAMILTONIAN-N/SHARP.md
[layout]: https://github.com/mathorn1973/twist-j/blob/89f69e40f6ccfd950bf2e6c446ec38bc51f7f71b/notes/C-PHYSICAL-BATTERY-HAMILTONIAN-N/HAMILTONIAN.md
