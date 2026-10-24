# Exact local compilation with a physical excitation ledger

**Status: NON-CANONICAL, L1, candidate-T.** This is a finite algebraic
construction, not an executed coefficient table or an independent acceptance
of its source candidates. The reservation is
[issue #1753](https://github.com/mathorn1973/twist-j/issues/1753).

The input is the finite clock and complete-history program in
[CLOCK.md at ecb3460](https://github.com/mathorn1973/twist-j/blob/ecb3460977cd2ee8a120797ffa53ba88cbe14171/notes/C-FORWARD-AUTONOMOUS-CLOCK-N/CLOCK.md)
and its energy-conserving lift in
[ENERGY.md at the same pin](https://github.com/mathorn1973/twist-j/blob/ecb3460977cd2ee8a120797ffa53ba88cbe14171/notes/C-FORWARD-AUTONOMOUS-CLOCK-N/ENERGY.md).
Their underlying ideal source and filter are pinned in
[PROOF.md at 01acc42](https://github.com/mathorn1973/twist-j/blob/01acc42b78f75095587765e9a5b91ee70dc28f37/notes/C-FORWARD-ONLY-CAPTURE-FILTER-N/PROOF.md).
All inherited capture bounds remain conditional on those candidate proofs.

This construction realizes the finite target using qubits with identical
positive on-site gap and gates that conserve their total excitation number
on the entire physical Hilbert space. It does not preserve the original
particle geometry. Its enormous finite width and gate count are explicit.

## 1. Registers and integer energy

Let S be the finite clock and data system of the pinned construction. Write

\[
N_S=\sum_x q(x)|x\rangle\langle x|,\qquad 0\le q(x)\le q_{\max},
\]

in its declared configuration basis. Here x includes the internal clock,
coordinates, coin, carrier, logical labels, all pentit histories, and all
predicate bits. N_S is the selected integer ledger in the pinned ENERGY.md;
it is independent of the two logical labels. Choose an integer r>=0 with

\[
Q=5^{2r}\ge\max\{1,q_{\max}\},\qquad
\ell=2r+22,\qquad L=5^\ell=Q5^{22},\qquad B_{\max}=L+2Q-1.
\]

The logical battery has levels n=0,...,B_max. Its dimension is B_max+1,
whereas its physical unary encoding below uses B_max qubits.

For clarity, with the notation of pinned CLOCK.md,

\[
\begin{split}
d_S&=M\,12N_{\rm box}^3\,26^2\,5^{D+1}\,2^{B_{\rm work}},\\
n_S&=\lceil\log_2 12\rceil+3\lceil\log_2N_{\rm box}\rceil
 +2\lceil\log_2 26\rceil+3(D+1)+B_{\rm work}
 +\lceil\log_2M\rceil.
\end{split}
\]

Thus n_S is the registerwise binary width of S, excluding the battery.
Use the fixed registerwise enumeration of its valid basis states, written
z(x) in {0,1}^{n_S}; unused register codes are invalid. This is an encoding,
not a claim that S contains n_S originally physical qubits.

For a width w, define the thermometer word

\[
\theta_w(k)=1^k0^{w-k},\qquad 0\le k\le w.
\]

For one information bit use the dual-rail encoding 0 -> 10, 1 -> 01.
The physical encoding of S is

\[
\mathcal E_S|x\rangle
 =|\operatorname{dr}(z(x))\rangle
  |\theta_Q(q(x))\rangle.
\]

It uses 2n_S+Q qubits and has excitation number n_S+q(x). The logical
battery level n is encoded as theta_Bmax(n), with excitation number n.
All these physical qubits have the same Hamiltonian epsilon|1><1|,
with epsilon>0. Information in a degenerate dual-rail pair therefore
carries one explicitly counted excitation.

## 2. A fully specified conserving preparation permutation

The fuel consists of Q charged qubits and donor blocks F_j of widths
4*5^j, for j=0,...,ell-1. The total donor width is L-1. Its prescribed
initial state is

\[
|f\rangle=|1\rangle^{\otimes Q}\bigotimes_{j=0}^{\ell-1}|\eta_j\rangle,
\qquad
|\eta_j\rangle=\frac1{\sqrt5}\sum_{a=0}^{4}
 |\theta_{4\cdot5^j}(a5^j)\rangle.
\]

The coherent donor states are supplied input resources. The preparation
permutation below transfers their coherence and excitation energy; it does
not prepare them from energy-diagonal fuel. Their preparation obligation
and physical energy are discussed in [FUEL.md](FUEL.md).

For n=sum_j a_j5^j in {0,...,L-1}, define raw battery-and-fuel basis words

\[
\begin{split}
|a_n\rangle&=|\theta_{B_{\max}}(0)\rangle|1\rangle^{\otimes Q}
 \bigotimes_j|\theta_{4\cdot5^j}(a_j5^j)\rangle,\\
|b_n\rangle&=|\theta_{B_{\max}}(Q+n)\rangle|0\rangle^{\otimes Q}
 \bigotimes_j|0\rangle^{\otimes4\cdot5^j}.
\end{split}
\]

Every pair has the same excitation number Q+n. All a_n are distinct, all
b_n are distinct, and the two sets are disjoint because Q>=1 and their
battery words have respectively zero and positive weight. Let P_BF swap
a_n with b_n for each n, and fix every other raw battery-and-fuel basis
word. This defines one total unitary, including all invalid encodings.
It commutes with the sum of the physical excitation projectors. Since
product base-five expansion gives L orthogonal terms of amplitude 1/sqrt(L),

\[
P_{BF}(|\theta_{B_{\max}}(0)\rangle|f\rangle)
 =\left(\frac1{\sqrt L}\sum_{n=0}^{L-1}
 |\theta_{B_{\max}}(Q+n)\rangle\right)|0\rangle_F.
\]

This is exactly the battery state used by the pinned lift, with depleted
fuel. P_BF contains L disjoint transpositions; treating it as one named
macro does not make its implementation free.

## 3. The complete raw-space target word

Let U_clock be the pinned finite clock unitary, and let Gamma(U_clock)
be the pinned lift on S and the logical battery. In each complete total
energy sector t=Q,...,B_max it acts as J_t U_clock J_t*, where

\[
J_t|x\rangle=|x\rangle|t-q(x)\rangle.
\]

It is identity on incomplete edge sectors. Consequently it is a total
unitary commuting with N_S+N_B, including the finite battery boundaries.

Encode this unitary on the valid S-and-battery code. Extend it by identity
on the orthogonal complement of that code and by identity on the fuel.
Call the resulting physical unitary V. The code is spanned by physical
computational basis vectors; on it the excitation number equals
n_S+q(x)+n. Hence [V,N_phys]=0 on the entire raw physical space. Define
the preparation macro V_0=I_S tensor P_BF on that same raw space, where
I_S here means identity on all 2n_S+Q physical S qubits.

The core width is

\[
P=2n_S+Q+B_{\max}+Q+(L-1).
\]

It includes S, battery, charged fuel, and every donor qubit. For the pinned
program let L_prog=T+5D+8 and M=L_prog+H+1. For a chosen h in {0,...,H},
the target word, in rightmost-first convention, is

\[
\mathcal U_h=V^{L_{\rm prog}+h}V_0,\qquad
\nu=1+L_{\rm prog}+h.
\]

The default is h=0, the capture endpoint. The h>0 family includes h later
native release steps in the decoded target. It does not by itself prove
a continuous physical read window or preservation of bound-band purity
after further native contacts. All auxiliary histories remain present.

## 4. Exact sectorwise elimination

For each named macro separately, enumerate its 2^P physical basis vectors
first by total weight, then lexicographically. Its matrix is block diagonal
in weight. In each weight sector perform the following deterministic QR
elimination: process columns from left to right, and eliminate entries
from bottom to top using adjacent rows within that sector ordering.
For entries a,b use

\[
Z(a,b)=\frac1{\sqrt{|a|^2+|b|^2}}
 \begin{pmatrix}\bar a&\bar b\\-b&a\end{pmatrix}
\]

when (a,b) is nonzero, and skip a zero pair. The square root is the positive
one. This maps (a,b)^T to (sqrt(|a|^2+|b|^2),0)^T. A triangular unitary is
diagonal, so the inverse elimination sequence and the remaining diagonal
phases factor the macro into two-level unitaries and one-state phases.
Every two-level factor connects states of equal weight.

A sector of dimension d_w needs at most d_w(d_w-1)/2 two-level factors and
d_w phases. Thus the total number of factors per macro is bounded by

\[
\sum_w d_w^2\le\left(\sum_wd_w\right)^2=4^P.
\]

All coefficients of the source matrices, the lift, and the preparation
permutation are algebraic. The stated elimination uses only conjugation,
field operations, and positive square roots. It therefore defines finite
exact algebraic gate entries without rounding. The definition specifies an
algorithm for the coefficient table; no such enormous table has been
generated or executed here.

## 5. Equal-weight paths and local conserving primitives

Let x and y be distinct weight-w bit strings of length P. Match in ascending
order the positions where (x_i,y_i)=(1,0) with those where it equals (0,1).
Exchange the matched 10 pairs to 01 one pair at a time. This produces a
simple path x=v_0,...,v_k=y, with k<=P/2, entirely within weight w.
A transposition between consecutive path strings is an exchange of two
physical bits, conditioned on all P-2 other bits having their specified
values. Conjugating a two-level unitary on the final edge by the first
k-1 transpositions yields the desired two-level unitary on x,y. It uses
2k-1<=P-1 conditioned exchanges. A one-state phase is treated directly.

Reserve A=P work pairs, initialized to |10> each. They are physical qubits
with the same positive gap, and contribute A*epsilon to readiness energy.
For a predicate on m bits, an AND ladder uses at most m-1 work pairs.
Each ladder step is a rail swap conditioned on two physical control bits
having specified values. It has at most four operands. The controls are
unchanged, and the target rail swap conserves excitation number on all
four-qubit inputs, including rail words 00 and 11.

After computing the predicate, apply the desired two-level unitary on the
span of 01 and 10 of the two target bits, controlled by the true rail of
the last work pair. It fixes 00 and 11. This has at most three operands
and conserves excitation number on the entire raw space. Uncompute the
AND ladder. The predicate excludes the two changed data bits, so it is
unchanged during the central gate and uncomputation returns every work
pair exactly to |10>. Cases m=0 or 1 use the corresponding direct gate.

Zero-controls use the projector |0><0| directly. They are never implemented
by a physical excitation-changing X gate. For a one-state phase, compute
the full P-bit equality predicate, phase its true work rail, and uncompute.
No data bit changes, so the same clean-return argument applies.

A conditioned exchange or one-state phase needs at most 2P such constant
support primitives. Each primitive commutes with the physical excitation
sum as an operator identity, not only on encoded inputs. For all raw core
states and arbitrary reference systems, their product implements the
specified factor and returns the clean work state. Dirty work states have
a total unitary evolution but no promised logical interpretation.

## 6. One-dimensional routing and explicit bound

The core and work occupy S_line=P+2A=3P physical qubits on a line. For a
primitive on at most four selected sites, move its operands into four
consecutive sites by adjacent swaps, apply it there, then reverse those
swaps. At most 4*S_line swaps suffice in each direction. Including the
central gate, the routed cost is at most 8*S_line+1<=25P. Every routing
swap conserves excitation number because all qubits have the same gap.

A two-level factor requires at most (P-1)*2P primitives; a phase requires
at most 2P. Combining the elimination and routing bounds gives the safe
finite estimate

\[
\boxed{\quad S_{\rm line}=3P,\qquad
R_{\rm gates}\le128\,\nu P^3 4^P.\quad}
\]

Every gate acts on at most four consecutive physical qubits, has exact
algebraic matrix entries, and commutes with

\[
H_{0,\rm line}=\epsilon\sum_{i=1}^{3P}|1\rangle\langle1|_i.
\]

Every work pair returns exactly at every macro boundary, and the target
including its identity extension holds for every raw core input. This
includes preservation of arbitrary correlations with an external
reference. P_BF is compiled by the same bound, so all L preparation
transpositions and their controls are included.

## 7. What this energy statement means

At a valid S-and-battery checkpoint with clean work and depleted fuel,

\[
H_{0,\rm line}/\epsilon=n_S+A+q+n
\]

on each encoded basis state. Thus the old variable ledger q+n is realized
by actual on-site excitation energy, with the information and work baseline
n_S+A explicitly added. Before preparation, the same formula includes the
nonzero fuel excitations. Logical labels may be arbitrary and entangled
with a reference; dual-rail encoding gives them the same energy baseline
for every admitted label value.

During a primitive gate, thermometers and code conditions may be invalid.
The physical on-site sum remains defined and exactly conserved then too.
A subsystem's decoded logical energy need only agree with its assigned
physical qubit sum at the specified code checkpoints. No statement of
native particle locality or original W-query cost is made for the compiled
primitives. The forward program remains the target being simulated.

[HAMILTONIAN.md](HAMILTONIAN.md) embeds this conserving local circuit in one
autonomous Hamiltonian. Its history amplitudes contain circuit prefixes;
abstract macro checkpoints are not deterministic intermediate physical
times. The endpoint is the target above. Preparation, all rejected
histories, work energy, and routing are included in that target and its
resource bound. Neither the construction nor its exact finiteness is a
claim of practical scale, repeatable reset, or an occurrence rule.
