# A geometric identity tail and a continuous accepted-output window

**NON-CANONICAL, L1, conditional candidate-T. Independent acceptance pending.**
This is an analytical extension of the number-conserving local apparatus in
[SHARP.md](SHARP.md), using the physical Hamiltonian construction in
[HAMILTONIAN.md](HAMILTONIAN.md). No scientific execution is reported here.

The input reduced-channel result is
[PROOF.md in PR #1752 at e19b071](https://github.com/mathorn1973/twist-j/blob/e19b07183c3e4841e18c8913de7c4c83429b94f3/notes/C-FINITE-HAMILTONIAN-READOUT-N/PROOF.md).
That candidate supplies a sharp-energy interface with an exact accepted
physical reduced channel. It does not supply the geometric compiler used
here. Its numerical clock length and physical reading times are not imported:
this note derives a new window after the entire spatial compilation, including
basis-fuel charging and routing.

The added tail consists of physical clock qubits with identity instructions.
There are no subsequent row transfers on that tail. The completed output
therefore remains on a fixed final data row. The read predicate also requires
a physical clock bit certifying that the whole compiled circuit is finished;
an early value of a temporary compiler flag is never accepted.

## 1. The sharp input and the completed local word

SHARP.md uses the explicitly changed account of #1752. Its inner target
clock has endpoint \(M_*=3276820\), its auxiliary account has maximum
\(R_{\rm aux}=983045\), and

\[
Q_*=M_*+R_{\rm aux}=4259865.
\tag{P1}
\]

Its two macros first move a basis charge of \(Q_*\) from the fuel to the
battery, then implement the declared finite-sector mirror unitary. This
retains every rejected history and gives the accepted physical reduced
channel of #1752. The comparison is not equality to a product of the ideal
complete state and an unchanged battery. In general the sharp battery
retains correlations with the inner clock and auxiliary energy.

Use the actual number-conserving line circuit of SHARP.md, with width and
clean work count

\[
P_*=2n_*+3Q_*,\qquad A_*=P_*,\qquad
S_*=3P_*.
\tag{P2}
\]

Here \(n_*\) is that note's registerwise binary width. It is not the
coherent-fuel construction's width. The physical core has the encoded
system, unary tally, battery and basis fuel; there are no broad coherent
donor blocks in this variant. Let \(R_*\geq1\) be the actual elementary
line-gate count, including charging, all work and routing. Every elementary
gate acts on at most four consecutive qubits and preserves excitation number
on the whole raw space. Its stated conservative bound is

\[
R_*\leq256P_*^3 4^{P_*}.
\tag{P3}
\]

The row-and-snake construction of HAMILTONIAN.md transfers the data through
\(R_*+1\) rows. The number of active clock instructions is

\[
K_0=R_*(S_*+3)-1,\qquad N_{\rm data}=(R_*+1)S_*.
\tag{P4}
\]

Call those instructions \(G_0,\ldots,G_{K_0-1}\), and let
\(F_j=G_{j-1}\cdots G_0\), with \(F_0=I\). On the stated fresh-row
input, \(F_{K_0}\) leaves all earlier data rows empty and places the
complete output on row \(R_*\). All work is in its restored state there.
The equalities hold with arbitrary admitted logical/reference input.

Let \(F_{\rm out}\) be the computational-basis projector on the true rail
of the encoded final acceptance bit on that final row. At a valid final
codeword it is the intended flag projector. It is defined on all raw inputs,
and it commutes with the physical excitation sum. A generic primitive
compilation does not guarantee that this rail is zero at earlier prefixes.
No such guarantee is assumed below.

The complete initialized data has one sharp physical onsite energy

\[
E_*=\epsilon(n_*+A_*+Q_*).
\tag{P5}
\]

The initially empty battery is charged within the word. The input charge
comes from the declared basis fuel, and all information and clean-work
excitations are counted. Because every instruction preserves excitation
number, every compiled prefix remains in this same energy eigenspace.
Unknown logical messages and their reference correlations do not change
(P5). Neither a coherent battery nor an initial cross-energy fuel
superposition is needed for this reduced-output interface.

## 2. A physical identity tail with unchanged data storage

Keep every data row in (P4). Append exactly \(K_0\) physical clock qubits
after the terminal active clock site. The total number of physical clock
qubits and transitions becomes

\[
M_{\rm out}=2K_0,
\tag{P6}
\]

and there are \(M_{\rm out}+1\) legal domain-wall clock states. In the
SHARP.md and README.md notation, \(k=K_0\) and \(K_*=M_{\rm out}\).
Set

\[
G_j=I\quad(K_0\leq j<M_{\rm out}),\qquad
F_j=F_{K_0}\quad(K_0\leq j\leq M_{\rm out}).
\tag{P7}
\]

This is physical clock padding, not additional identity line gates followed
by more row transfers.

For the geometric embedding, the last active stage rail is at vertical
coordinate \(2R_*-1\). Its endpoint is the guard column \(S_*+1\) when
that rail was traversed to the right, and guard column zero when traversed
to the left. Continue horizontally outward from that guard for \(K_0\)
unit lattice steps. The new sites lie outside every previous data row and
clock rail, so there are no collisions. Consecutive clock sites stay one
lattice step apart, including the junction. The apparatus fits in a rectangle
of width \(S_*+K_0+2\) and height \(2R_*+1\), omitting unused positions.

No extra data or battery rows are introduced. The fixed physical battery
bank still consists of its columns in all existing data rows. In this
sharp variant it has \((R_*+1)Q_*\) qubits and raw capacity
\(\epsilon(R_*+1)Q_*\), whereas the one-active-row logical ladder has
capacity \(\epsilon Q_*\). The basis-fuel bank has the same copied
width. Empty rows remain counted hardware.

## 3. Positive local Hamiltonian on all clock strings

For brevity write \(M=M_{\rm out}\). Use actual clock bits
\(c_1,\ldots,c_M\), fixed virtual boundaries \(c_0=1,c_{M+1}=0\),
and legal states

\[
|j\rangle_c=|1\rangle^{\otimes j}|0\rangle^{\otimes(M-j)},
\qquad 0\leq j\leq M.
\tag{P8}
\]

All physical clock bits are initially zero and have zero bare onsite gap.
For \(0\leq j<M\), define

\[
P_j=|1\rangle\langle1|_{c_j}\otimes I_{c_{j+1}}
              \otimes|0\rangle\langle0|_{c_{j+2}},\qquad
B_j=|110\rangle\langle100|_{c_jc_{j+1}c_{j+2}},
\]
\[
a_j=\frac{g}{M+1}\sqrt{(j+1)(M-j)},\qquad a_{-1}=a_M=0,
\]
\[
b_j=|1\rangle\langle1|_{c_j}\otimes|0\rangle\langle0|_{c_{j+1}},
\qquad v_j=g-a_{j-1}-a_j\quad(0\leq j\leq M).
\tag{P9}
\]

Virtual boundary factors in these formulas are replaced by their fixed
values. With \(g>0\), set

\[
H_{\rm pad}=\sum_{j=0}^{M-1}
 a_j(P_j\otimes I-B_j\otimes G_j-B_j^*\otimes G_j^*)
 +\sum_{j=0}^{M}v_jb_j\otimes I,
\]
\[
H_0=\epsilon\sum_{\text{all data sites }i}|1\rangle\langle1|_i,
\qquad H_{\rm tot}^{\rm pad}=H_0+H_{\rm pad},\qquad\epsilon>0.
\tag{P10}
\]

The same two-clock-word block proof as HAMILTONIAN.md gives, on the entire
raw clock/data space,

\[
H_{\rm pad}\geq0,\quad [H_0,H_{\rm pad}]=0,\quad
0\leq H_{\rm tot}^{\rm pad}
 \leq\bigl(\epsilon N_{\rm data}+(M+1)g\bigr)I.
\tag{P11}
\]

Each propagation summand is positive with norm at most \(g\); each
potential summand is positive with norm at most \(g\). Each onsite term
has norm \(\epsilon\). Illegal clock strings have a fully defined
Hermitian evolution and are not discarded to obtain these inequalities.

Active propagation terms still involve at most five data and three clock
qubits within Manhattan radius four of the active clock site. New tail
terms act only on at most three consecutive clock qubits. The junction has
the same bounds. Term valence is at most six including onsite terms, and
the graph joining sites that share a term has degree at most 35. Every
local dimension is two. The total physical qubit count is

\[
(R_*+1)S_*+2K_0.
\tag{P12}
\]

Adjoint reverse edges remain present in (P10). The completed chronological
target is forward, while the microscopic clock Hamiltonian is Hermitian and
permits reverse history motion.

## 4. Exact history weights and the completion-qualified read

Define the legal-history unitary change of description

\[
\mathcal W(|j\rangle_c\otimes|\psi\rangle)
 =|j\rangle_c\otimes F_j|\psi\rangle.
\tag{P13}
\]

It is an analytical identity, not an added implementation step. The legal
restriction of \(\mathcal W^*H_{\rm pad}\mathcal W\) is
\(gI-[2g/(M+1)]J_x\), with spin \(M/2\). For the initialized sharp data
and arbitrary reference, the full evolution is therefore

\[
|\Omega(t)\rangle=e^{-it(E_*+g)/\hbar}
 \sum_{j=0}^{M}\sqrt{\binom Mj}
 (i\sin\theta)^j(\cos\theta)^{M-j}
 |j\rangle_c\otimes F_j|\psi_0\rangle,
\qquad \theta=\frac{gt}{\hbar(M+1)}.
\tag{P14}
\]

Expanding \(M\) identical two-state rotations in the normalized symmetric
weight basis proves the formula, including its normalization. Since the
whole initialized orbit has sharp \(H_0=E_*I\), its free onsite phase
is global at every time. The ratio \(\epsilon/g\) need not be calibrated
to make a bare-energy endpoint phase vanish. This is a consequence of the
sharp-input family, not an identity on energy-superposed raw inputs.

At

\[
\tau_* =\frac{\pi\hbar(M+1)}{2g}
\tag{P15}
\]

the clock is exactly \(M\), and the complete final data is exactly
\(F_{K_0}\psi_0\), up to a common phase. The physical completed output
is fixed on the final row throughout all histories \(j\geq K_0\).

For a physical read define

\[
\Pi_{\rm read}=|1\rangle\langle1|_{c_{K_0}}\otimes F_{\rm out}.
\tag{P16}
\]

On legal domain-wall states, \(c_{K_0}=1\) if and only if
\(j\geq K_0\). Thus (P16) rejects every incomplete compiled prefix,
regardless of temporary values of the flag rail. It is a product of two
fixed-site projectors and commutes with \(H_0\). The sites need not be
neighbors. The expression specifies a mathematical joint read observable;
this note does not construct an additional physical readout device or its
couplings.

Let \(\mathcal D_{\rm out}\) be the final accepted-output reduction in
SHARP.md: trace the unused data rows, work, fuel, battery, system tally, inner-clock and
auxiliary registers, remove the declared valid encoding, and retain the
object, carrier, receiver and reference. All its uses below are on valid
completed accepted output, so no interpretation of a dirty intermediate
code is needed. Write \(\sigma_{\rm ideal}\) for the unnormalized
ideal accepted physical state, including the reference.

Set

\[
w(t)=\sum_{j=K_0}^{M}\binom Mj
       \sin^{2j}\theta\,\cos^{2(M-j)}\theta.
\tag{P17}
\]

For the actual complete density operator \(\rho(t)\),

\[
\boxed{\quad
\mathcal D_{\rm out}\left(\operatorname{Tr}_{\rm outer\ clock}
 [\Pi_{\rm read}\rho(t)\Pi_{\rm read}]\right)
 =w(t)\sigma_{\rm ideal}.
\quad}
\tag{P18}
\]

Indeed, the clock trace removes cross terms with different \(j\), (P16)
keeps only \(j\geq K_0\), and every retained data vector is the same
\(F_{K_0}\psi_0\). Applying the exact final reduced-channel identity of
SHARP.md gives (P18). The proof extends to all logical/reference matrix
units by linearity, so it preserves arbitrary admitted reference
correlations. The traces are observational reductions; no branch or
correlation is physically deleted from the closed evolution.

Whenever \(w(t)>0\), normalization of (P18) gives exactly the ideal
accepted physical state. No inverse small-acceptance penalty appears in
this identity.

## 5. A new continuous read window after the full spatial compilation

For

\[
\frac{\pi\hbar(M+1)}{3g}\leq t\leq
\frac{2\pi\hbar(M+1)}{3g},
\tag{P19}
\]

one has \(p=\sin^2\theta\geq3/4\). The coefficients in (P17) are a
binomial expansion with \(M=2K_0\). Using a formal binomial variable
\(X\) to abbreviate its finite polynomial weights,

\[
1-w(t)=\Pr(X<K_0)
 \leq3^{K_0}\mathbb E(3^{-X})
 =3^{K_0}(1-p+p/3)^{2K_0}
 \leq(3/4)^{K_0}=:\delta.
\tag{P20}
\]

This is a finite algebraic weight bound, not a law of realized outcomes.
The interval width is \(\pi\hbar(M+1)/(3g)\), with the exact endpoint
\(\tau_*\) in its center. It scales with the complete compiled clock
length at the fixed local interaction strength \(g\).

Here \(K_0\geq400\) follows already from (P1)-(P4) and \(R_*\geq1\).
For a smaller abstract circuit, one may first append enough identity line
gates to reach that condition, counting their extra data rows and clock
sites before defining (P6). Since \((3/4)^4=81/256<1/2\),

\[
\delta\leq(3/4)^{400}<2^{-100}<10^{-30}.
\tag{P21}
\]

The explicit source bound inherited conditionally through #1752 is

\[
p_{\rm ideal}>p_0:=\frac25\frac{1024}{15625}\frac{99}{50000},
\qquad\frac{99}{100}p_0>\frac1{20000},
\]
\[
r_{\rm ideal}<\frac{50000}{99\,2^{29}}<\frac1{10^6}.
\tag{P22}
\]

Consequently (P18)-(P21) give on the whole interval (P19)

\[
p_{\rm read}(t)=w(t)p_{\rm ideal}>\frac1{20000},\qquad
r_{\rm read}(t)=r_{\rm ideal}<\frac1{10^6}.
\tag{P23}
\]

These numerical source and spectral conclusions depend on the still
candidate source/filter proofs of #1746. The bound-band observable is the
same one evaluated on that physical output, not a newly identified finite
periodic-box spectral projector. The normalized accepted logical channel
is the same exact incoming-label/old-memory SWAP, including arbitrary
reference. With incoming label one, the receiver is exactly \(d_1\) on
this accepted state. No probabilities of actual individual events have
been derived.

## 6. Continuation after an endpoint mathematical read

Equations (P18)-(P23) describe separate reads of the unmeasured evolution.
The following is a different continuation contract. At \(t=\tau_*\),
apply \(\Pi_{\rm read}\) as a mathematical projection and normalize when
its weight is nonzero. Continue with the same fixed Hamiltonian
\(H_{\rm tot}^{\rm pad}\). This does not claim an implemented collapse
mechanism, a detector apparatus, or a physical occurrence law.

The post-state has outer clock exactly \(M\). Since (P16) commutes with
\(H_0\), it remains in the same sharp physical onsite-energy sector (P5).
For incoming label one, its receiver on the fixed final row is exactly
\(d_1\). Let \(P_{d_1}^{\rm out}\) be the projector onto that valid
receiver codeword on the final-row information qubits, acting as identity
on every other degree of freedom. Invalid or displaced receiver codes are
included in \(I-P_{d_1}^{\rm out}\).

For any endpoint data/reference vector \(\phi\), the history identity
(P13) gives the backward-from-endpoint data at clock \(j\) as
\(F_jF_M^*\phi\). Whenever \(j\geq K_0\), (P7) makes this exactly
\(\phi\). The wrong-receiver projection therefore annihilates that
whole tail portion. Orthogonal clock states remove cross terms in its
expectation, and its norm is at most one on the remaining portion.

For a delay \(u\) satisfying

\[
0\leq u\leq\frac{\pi\hbar(M+1)}{6g},
\tag{P24}
\]

put \(r=\sin^2(gu/[\hbar(M+1)])\leq1/4\). Motion from clock \(M\)
has binomial weights for the number \(Y=M-j\) of downward moves. The
bad portion \(j<K_0\) has \(Y>K_0\), so

\[
\Pr(j<K_0)\leq3^{-K_0}\mathbb E(3^Y)
 =3^{-K_0}(1+2r)^{2K_0}\leq(3/4)^{K_0}=\delta.
\]
\[
\boxed{\quad
\operatorname{Tr}\bigl[(I-P_{d_1}^{\rm out})\rho_{\rm post}(u)\bigr]
 \leq\delta<10^{-30}.
\quad}
\tag{P25}
\]

The bound is linear in the bad history weight and applies to arbitrary
retained history, battery and reference correlations. It does not use a
fresh preparation after the read, and it does not divide by the earlier
small acceptance weight: the good tail preserves every normalized endpoint
post-state meeting the stated receiver condition.

This is finite approximate physical retention in the added apparatus.
It is not the native-flight buffer of #1746, and it does not prove continued
binding during any reverse excursion into the active circuit. Such excursions
have small nonzero amplitude at generic positive delays. The finite clock
has no absorbing halt or permanent protected record.

## 7. Total energy, readiness and limitations

At the stated initialized sharp input, (P10) has exact physical moments

\[
\boxed{\langle H_{\rm tot}^{\rm pad}\rangle
 =\epsilon(n_*+A_*+Q_*)+g,}
\qquad
\boxed{\operatorname{Var}(H_{\rm tot}^{\rm pad})
 =\frac{g^2M}{(M+1)^2}.}
\tag{P26}
\]

The first follows from sharp \(H_0\) and propagation diagonal \(g\).
The only initial off-diagonal clock transition has squared norm
\(a_0^2=g^2M/(M+1)^2\), proving the variance. The interaction contribution
is included in the physical energy. The sharp fuel simplifies the bare
energy preparation, but the total initial state is nonstationary for the
running Hamiltonian. Indeed the initially localized clock gives a nonzero
commutator block \([H_{\rm tot}^{\rm pad},\rho]_{1,0}=-a_0G_0\rho_{\rm data}\) for every
nonzero data density operator. For a pure preparation this is also witnessed
by the strictly positive variance in (P26).

A state stationary for the full \(H_{\rm tot}^{\rm pad}\) stays
stationary under every unitary commuting with that generator. Consequently
this construction does not prepare its working clock from a completely
stationary free apparatus. The supplied basis fuel, clean work, empty data
rows, clock boundary, exact fixed couplings and chosen energy interpretation
remain additional physical premises. It has no cross-\(H_0\)-energy donor
requirement because its reduced-output target is different from a coherent
battery/product-state interface, not because such coherence was created
from stationary resources.

The padded clock returns the initially unmeasured legal computation to its
initial state up to a common phase at \(2\tau_*\). This is a reversal of
its new records, not a useful reset preserving them. A post-read trajectory
is governed by its projected state and is not silently identified with that
unmeasured recurrence.

All locality statements concern the added qubit lattice. Original particle
coordinates are encoded values. The sharp account, its energy degeneracies,
local interactions and continuous-time law are selected model data, not a
derivation from the original TWIST-J update. The exact accepted-output
identity and the new compiled read window are L1 mathematical statements;
their independent acceptance, material realization and physical measurement
implementation remain open.
