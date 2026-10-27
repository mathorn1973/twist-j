# An autonomous preparation window before the data program

**NON-CANONICAL, L1, conditional candidate-T. Independent acceptance
pending.** Public reservation:
[issue #1755](https://github.com/mathorn1973/twist-j/issues/1755).
This is an analytical finite construction; no scientific program or
coefficient table has been executed.

The inherited data circuit is the sharp-source construction in
[SHARP.md at 89f69e4](https://github.com/mathorn1973/twist-j/blob/89f69e40f6ccfd950bf2e6c446ec38bc51f7f71b/notes/C-PHYSICAL-BATTERY-HAMILTONIAN-N/SHARP.md).
[HAMILTONIAN.md](HAMILTONIAN.md) adds a charged source site, an initially
empty cursor line, a completion latch and physical identity intervals.
This note proves a preparation interval in that same stationary law.
[SOURCE.md](SOURCE.md) accounts for the supplied source and its interaction
energy; no source preparation from a stationary global state is assumed.

## 1. Schedule and initialized family

Let R_* be the actual elementary line-gate count of the inherited circuit,
S_* its line width, and

\[
N=R_*(S_*+3)-1,\qquad A=N+1,\qquad L=2A,\qquad M=4A.
\tag{P1}
\]

Here A is a runway length, distinct from the inherited work-pair count A_*.
There are cursor sites c_0,...,c_M. The source is c_0; all other cursor
sites are initially in their vacuum state. The initial cursor has exactly
one excitation, at c_0.

Index edges by j=0,...,M-1. Their data instructions are:

- identity for j=0,...,A-1;
- the N inherited row-transfer instructions for j=A,...,A+N-1;
- a swap of the two completion-latch rails on j=A+N=2A-1;
- identity for j=L,...,M-1.

Thus the first A edges form a physical runway before any data instruction.
The last 2A edges form the later reading tail. These are different intervals.

Write W_j for the instruction on edge j and

\[
F_0=I,\qquad F_j=W_{j-1}\cdots W_0.
\tag{P2}
\]

In particular F_j=I for 0<=j<=A. All data rows, the fuel for charging the data battery,
work pairs, the initially empty battery and the completion latch are
included in the data input. The completion latch starts in |10>.
The source's initial cursor excitation is the additional charged resource
specified in SOURCE.md.

Let psi_0 denote this data input with arbitrary admitted logical messages
and reference correlations. It has sharp physical bare energy after
including the one cursor excitation. Call that energy E_0. This is
sharpness for H_0, not stationarity for the complete coupled Hamiltonian.
All instructions preserve H_0 on the full raw space.

## 2. Exact cursor amplitudes in the complete law

On the one-cursor sector, HAMILTONIAN.md uses edge weights

\[
a_j=\frac{g}{M+1}\sqrt{(j+1)(M-j)},\qquad g>0,
\]

and a positive diagonal completion such that its propagation Hamiltonian
is gauge-equivalent to gI-[2g/(M+1)]J_x, with spin M/2. The physical
Hamiltonian is H_0+H_prop. Its full-space edge definition, including the
11 cursor block, is the one in HAMILTONIAN.md; no sector is discarded in
defining that operator.

On the stated input its exact state is

\[
|\Omega(t)\rangle=e^{-it(E_0+g)/\hbar}
 \sum_{j=0}^{M}b_j(t)|j\rangle_c\otimes F_j|\psi_0\rangle,
\]
\[
b_j(t)=\sqrt{\binom Mj}(i\sin\theta)^j(\cos\theta)^{M-j},
\qquad \theta=\frac{gt}{\hbar(M+1)}.
\tag{P3}
\]

Here |j>_c is the physical one-excitation basis vector at site c_j.
The formula follows by expanding M identical two-state rotations in their
symmetric weight basis, followed by the history gauge. In particular,

\[
|b_j(t)|^2=\binom Mj p^j(1-p)^{M-j},\qquad p=\sin^2\theta.
\tag{P4}
\]

The complete state retains every cursor history, including premature data
histories and the amplitude still on the source. The following binomial
notation abbreviates these exact polynomial weights and asserts no law
of physical outcome occurrence.

## 3. A finite preparation interval

Use the first interval before theta=pi/2 satisfying

\[
\frac1{16}\leq p\leq\frac18.
\]

Equivalently,

\[
\frac{\hbar(M+1)}{g}\arcsin\frac14
 \leq t\leq
\frac{\hbar(M+1)}{g}\arcsin\frac1{\sqrt8}.
\tag{P5}
\]

Its width is strictly positive and scales with the full cursor length at
fixed local strength g. This is an interval of the autonomous evolution,
not a time at which a coupling is switched or the state is projected.

Call cursor positions 1<=j<=A good. On them the source site is empty,
the excitation is on the runway, and every data degree of freedom is
unchanged. This includes the empty battery, its still-charged basis fuel,
all initial work and empty rows, and the latch |10>. The inherited
battery-charging macro has not yet begun on these histories.

The bad weight is exactly the sum of source survival and premature exit:

\[
\beta(t)=|b_0(t)|^2+\sum_{j>A}|b_j(t)|^2.
\tag{P6}
\]

For the source term, (P5) gives

\[
|b_0(t)|^2=(1-p)^M\leq(15/16)^{4A}
                 =\left(\frac{50625}{65536}\right)^A.
\tag{P7}
\]

For the second term, use a formal binomial variable X with the weights
(P4). Its generating polynomial is E[z^X]=(1-p+pz)^M. Thus

\[
\begin{split}
\Pr(X>A)&\leq3^{-A}\,\mathbb E[3^X]
 =3^{-A}(1+2p)^{4A}\\
&\leq3^{-A}(5/4)^{4A}
 =\left(\frac{625}{768}\right)^A.
\end{split}
\tag{P8}
\]

Combining the two terms,

\[
\boxed{\quad
\beta(t)\leq\delta_{\rm prep}:=
 \left(\frac{50625}{65536}\right)^A+
 \left(\frac{625}{768}\right)^A
 <2(5/6)^A.
\quad}
\tag{P9}
\]

The comparisons are exact: 6*50625<5*65536 and 6*625<5*768.
For this construction A>=1024 already follows from R_*>=1,
S_*=3P_*, P_*>=3Q_* and Q_*=4259865. Since

\[
(5/6)^4=625/1296<1/2,
\]

one obtains

\[
\delta_{\rm prep}<2^{-255}<10^{-30}.
\tag{P10}
\]

This is a conservative analytical bound, not a simulated success rate.

## 4. Approximate preparation without a physical postselection

Put w(t)=1-beta(t)>0 and define a normalized runway wavepacket

\[
|\chi(t)\rangle_c=
 \frac1{\sqrt{w(t)}}\sum_{j=1}^{A}b_j(t)|j\rangle_c.
\tag{P11}
\]

It has the source site c_0 exactly empty, and every cursor site beyond the
runway exactly empty. Its one excitation is coherently distributed over
sites 1,...,A. It is independent of the unknown logical messages and their
reference. It is not a single-site prepared cursor.

For a pure data/reference input, compare the actual complete state with

\[
|\Xi(t)\rangle=e^{-it(E_0+g)/\hbar}
                 |\chi(t)\rangle_c\otimes|\psi_0\rangle.
\tag{P12}
\]

Because F_j=I on the runway and different cursor sites are orthogonal,

\[
\langle\Xi(t)|\Omega(t)\rangle=\sqrt{w(t)}.
\]

With trace distance D(rho,sigma)=||rho-sigma||_1/2, this proves

\[
\boxed{\quad
D\bigl(|\Omega(t)\rangle\langle\Omega(t)|,
       |\Xi(t)\rangle\langle\Xi(t)|\bigr)
 =\sqrt{\beta(t)}\leq\sqrt{\delta_{\rm prep}}<2^{-127}<10^{-30}.
\quad}
\tag{P13}
\]

For clarity, the phase-aligned vector norm is a different metric:

\[
\|\Omega(t)-\Xi(t)\|^2=2(1-\sqrt{1-\beta(t)})
                     \leq2\beta(t).
\tag{P14}
\]

Its bound is sqrt(2 delta_prep), not sqrt(delta_prep). It too is less than
2^-127 under (P10). For a mixed logical/reference input, purify it, apply
(P13), and trace only the purifying system. This gives the same uniform
upper bound on the complete physical state, without discarding any
physical cursor history.

The normalization in (P11) defines the comparison state used to prove an
approximation. No projection, renormalization operation, or successful
outcome is required in the actual apparatus. The actual state remains
(P3), with its complete bad component. Thus (P13) is an unconditional
preparation statement, not a postselected preparation protocol.

There is also a stronger bound on disturbance of the data itself. Trace
the physical cursor, retaining all data and the passive reference. The
result is the mixture with weights (P4). Every term j<=A, including the
source-survival term j=0, has exactly the initial data state. Convexity of
trace distance therefore yields

\[
\boxed{\quad
D(\rho_{\rm data}(t),\rho_{\rm data}(0))
 \leq\Pr(X>A)\leq(625/768)^A.
\quad}
\tag{P15}
\]

Consequently failure to leave the source does not itself disturb the
battery, fuel, messages or work. Only premature data histories contribute
to this disturbance bound.

## 5. Energy and the boundary of the preparation claim

The source occupation is exactly cos^(2M)(theta), so its bare energy is
its specified onsite gap times that occupation. Emptying c_0 does not
turn off its coupling to c_1. Nor does an empty c_0 imply exactly zero
source/interface energy, because the launch-edge energy also acts on c_1.
SOURCE.md gives the positive launch-region account and its exact evolution.
The specified initial energies and subsequent transfers of the source, data,
latch and computation are counted in the same physical model; acquiring those
ready inputs remains supplied.

The source starts in a specified excited basis state for its bare onsite
energy. Relative to the complete coupled Hamiltonian, the input is already
nonstationary. The device cursor would remain in its stationary vacuum
without that source excitation. This construction transfers a supplied
local resource into a propagating controller; it does not generate full
Hamiltonian nonstationarity from a stationary global input.

There is no exact intermediate single-site preparation or exact holding
plateau. For example, under the constant-diagonal one-cursor Hamiltonian,
the initial source state has propagation variance a_0^2. A state with the
cursor exactly at site 1 would have variance a_0^2+a_1^2, independently of
its data/reference vector. Since a_1>0 and unitary evolution conserves
variance, that exact first-site state cannot be reached from the source.

More generally, for a fixed finite Hamiltonian H and a fixed projector P,
the vector (I-P)exp(-itH/ħ)psi is analytic in t. If it vanished throughout
an open interval, it would vanish for all times. A state initially outside
an exact prepared subspace cannot therefore enter it and remain exactly
there throughout a later open interval under this same law. The analogous
statement follows for a density matrix by purification, or entrywise
analyticity. It does not prohibit the quantitative approximate interval
(P13), or a stated conditional read of a complete history.

During (P5), the comparison clock wavepacket changes with t; it is not a
clock frozen at one fixed ready state. Later evolution, without any new
switch, continues into the data program and the final reading tail.
HAMILTONIAN.md proves the completed accepted-output interface and its own
later read interval. Neither interval is permanent storage, a reusable
reset, a native-law derivation or a law of individual outcomes.
