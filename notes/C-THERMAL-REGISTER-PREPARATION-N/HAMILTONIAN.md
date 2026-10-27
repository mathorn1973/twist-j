# One static Hamiltonian for thermal preparation and the capture channel

**Status: NON-CANONICAL, L1, candidate-T.** This is an analytical construction,
not an executed compiler, independent mathematical acceptance, or a derivation
from the native transfer law. All physical Hilbert spaces below are finite.
The work cells are genuine multilevel sites; their dimension grows with the
payload. The previous all-qubit local-dimension bound is not retained.

The input contract is the finite apparatus of [PR #1758](https://github.com/mathorn1973/twist-j/pull/1758)
at commit `243379459e3c7493368473cbae1a17eb99ee8316`, specifically its
`C-ENVIRONMENT-SOURCE-PREPARATION-N` construction. Its complete accepted
channel is retained, including its environmental weight `4/15`. This note
replaces its preparation and continuous trajectory by a new physical model.
The preparation permutation and its error are specified in [PREPARATION.md](PREPARATION.md);
all thermal and work resources are accounted for in [RESOURCES.md](RESOURCES.md).

## 1. Payload, physical work cells, and the buffered lift

There are `n` payload qubits in one line, including the old apparatus,
compression donors, the two environmental donors, and retained garbage.
Their physical bare Hamiltonian is

\[
 H_P=\epsilon\sum_{i=1}^n w_i n_i,
 \qquad w_i\in\{1,2,3\},\qquad Q=\sum_i w_i,\qquad R=2Q.
 \tag{H1}
\]

The unknown logical input, with any reference, is restricted to the stated
fixed-charge code. Other initial payload factors are diagonal in their
physical energy bases. In particular the common-temperature donor state has
`beta*epsilon=ln(2)`: gap-`epsilon` donors have excited population `1/3`, and
gap-`2 epsilon` donors have excited population `1/5`. No arbitrary coherence
between different initial bare energies is included in this input contract.

Each payload position has a separate work site of physical dimension
`2R+1`, with

\[
 H_B=\epsilon\sum_{b=0}^{2R}b|b\rangle\langle b|.
 \tag{H2}
\]

This is its whole physical space, not a code inside a larger qubit bank.
The distinguished work site starts in

\[
 \omega_B=(1-\eta_B)|R\rangle\langle R|
       +\frac{\eta_B}{2R}\sum_{b\ne R}|b\rangle\langle b|,
 \qquad \eta_B=\frac{2^{-80}}{Q+1}.
 \tag{H3}
\]

It is full rank, has mean energy `epsilon R`, and remains an explicitly
supplied nonthermal resource. The other work sites may start in arbitrary
diagonal Gibbs states. Their energy is included, not set to zero.

For a gate `U` on payload subset `A`, put `q_A=sum_(i in A) w_i`.
On every complete local total-charge sector `q_A <= t <= 2R`, define

\[
 J_{A,t}|x\rangle=|x\rangle|t-e_A(x)\rangle,
 \qquad \Gamma_A(U)|_{t}=J_{A,t}UJ_{A,t}^{\dagger}.
 \tag{H4}
\]

On each remaining local sector use the identity. This specifies a unitary
on the entire physical payload/work space and exactly preserves
`H_(P,A)+H_B`. It does not assume that a square root already is an apparatus.

For the complete payload, sectors `Q <= t <= 2R` contain every payload
basis state. If the work input is the central state `|R>`, its total charge
is `R+e(x)`, which lies in this interval. During any local gate,

\[
 q_A\le t-e_{A^c}(x)\le 2R.
\]

Consequently every local lift agrees there with the common global lift.
For any finite word the shifts telescope:

\[
 \Gamma(U_s)\cdots\Gamma(U_1)=\Gamma(U_s\cdots U_1),
 \qquad b_{\rm out}=R+e_{\rm in}-e_{\rm out}.
 \tag{H5}
\]

The charge excursion is at most `Q`, independently of the number of gates.
The uniformly weighted noncentral part of (H3) is retained. Outside the
complete global sectors a product of locally completed gates need not be
the identity. No identity-on-that-tail claim is used.

The preparation is a classical reversible permutation: the three-bit
compression `100 <-> 011`, routing swaps, needed complements, target swaps,
and the two environmental swaps. On the admitted diagonal input its central
work branch gives exactly the intended classical preparation distribution,
with all discarded information retained in donors and work. The logical
fixed-charge input and its reference are left intact.

## 2. The endpoint operator and a finite compiler without clean scratch

Let `K_old` be the path length in the pinned #1758 model and let `J_old`
identify its active legal histories with a path register and the admitted
logical input. Its bare charge is constant along this legal path. Write

\[
 \mathcal R|j\rangle=|K_{\rm old}-j\rangle,\qquad
 T=-iJ_{\rm old}(\mathcal R\otimes I)J_{\rm old}^{\dagger}
        +(I-J_{\rm old}J_{\rm old}^{\dagger}).
 \tag{H6}
\]

This is a full-space unitary. It commutes with the old apparatus bare
Hamiltonian, sends its active initial boundary to its completed boundary,
and is the identity on the inactive environmental input sectors. Its phase
on the active sector agrees with the usual engineered-chain reflection
phase. Other free phases have no effect on the stated initially diagonal
environmental mixture. Tensor (H6) with the identity on new donors and
retained garbage. Thus `[T,H_P]=0`.

This definition fixes the endpoint extension used here. It does not assert
that the new dynamics equals `exp(-it H_old/hbar)` at intermediate times or
on every dirty raw input. Its equivalence to the old experiment is the
specified input-to-reduced-output channel.

On the buffered sectors (H5) gives the stronger identity

\[
 \Gamma(T)=T\otimes I_B.
 \tag{H7}
\]

It holds even when the work site is already correlated with the prepared
environment and garbage. Tracing those systems therefore cannot change the
subsequent reduced action of `T`.

An exact finite compiler for (H6) can be fixed without a clean ancilla.
Here is a deliberately loose constructive bound, using arbitrary exact
one- and two-qubit gates rather than a finite approximate gate alphabet.
QR elimination uses fewer than `4^n` two-level rotations and basis phases.
A Gray path of length at most `n` expresses each two-level rotation using
at most `2n-1` fully controlled one-qubit gates. Diagonalize the target
`2 x 2` unitary of such a gate. Its two controlled phases have the form

\[
 e^{i\phi |x\rangle\langle x|},\qquad
 |x\rangle\langle x|=2^{-n}\prod_i(I+(-1)^{x_i}Z_i).
 \tag{H8}
\]

Expand the product. The resulting at most `2^n` commuting Pauli-string
rotations are implemented with a parity CNOT chain, one one-qubit rotation,
and the reverse parity chain. This uses the existing qubits as temporary
parity carriers and restores them; no clean scratch state is needed.
Including the two target basis changes, a controlled one-qubit gate needs
at most `4n 2^n+2` one-/two-qubit gates. A safe resulting bound is
`16 n^2 8^n`. Move each pair together and back with at most `2(n-1)` payload
swaps to obtain at most `64 n^3 8^n` nearest-neighbor gates.

These gates need not preserve payload energy. Each is implemented through
(H4). To bring the distinguished work factor to a gate at payload cell `i`,
swap work factors along the line from cell 1 to `i`, apply the funded gate,
and undo those work swaps. The other work factors have equal spectra, so
the swaps preserve physical energy. Conjugating this way acts on the
original distinguished work factor and is the identity on all original
other work factors, even when they are dirty or correlated. The overhead
is at most `2n+1`, giving the safe bound

\[
 J_T\le256n^4 8^n.
 \tag{H9}
\]

The explicit three-bit preparation may use its direct, smaller construction;
the same generic bound also suffices for its full permutation. Let `J_p`
and `J_T` denote the actual primitive lengths produced by the fixed
algorithm, and put `J=J_p+J_T`. These are mathematical counts of the defined
finite algorithm. They have not been enumerated by a scientific execution.
This is the standard exact universal-compilation setting of
[Barenco et al.](https://arxiv.org/abs/quant-ph/9503016), with the elementary
bound above supplied to make the resource claim explicit.

## 3. Local geometry with arbitrary row contents

A line has `W=2n` separate physical sites: payload qubits at odd columns and
work qudits at even columns. There are `J+1` data rows at heights `2t`,
`0 <= t <= J`. Every row repeats the same column dimensions and onsite
spectra. Only row 0 contains the payload to be processed. Every other row
may contain arbitrary diagonal Gibbs junk. No fresh zero row is required.

A primitive uses at most three neighboring payload qubits and one work
site, within five consecutive physical columns. A head-transport swap uses
two work sites separated by one payload column. Route payload operands
before the primitive and undo the routing when prescribed; these swaps are
also included in `J` and funded when their spectra differ.

For one primitive, transfer a whole row to the next by single-site swaps.
Apply the primitive on the destination row immediately after its last
operand has arrived. The order alternates left to right and right to left.
The resulting stage equals a complete-row SWAP followed by the primitive
on the destination row. Induction gives the exact operator identity:

- final row: the original row-0 state acted on by the complete word;
- earlier rows: the original remaining rows permuted backwards.

This identity holds for arbitrary correlations between row contents. It is
not a statement that junk rows happen to be nearly empty. At the preparation
checkpoint the same statement holds for the preparation prefix. The hold
interval then applies the identity, including to the row positions.

Put cursor sites on the horizontal rails `y=2t+1`, at columns `0,...,W+1`,
with one guard connector between successive rails. A block of `j >= 1`
primitive stages has an outward initial source, an identity guard edge, and

\[
 b(j)=j(W+3)-1
 \tag{H10}
\]

edges. Each row-transfer instruction, possibly followed by the primitive,
uses at most five data sites. Including its two cursor endpoints, each
propagation term uses at most seven physical sites in a Manhattan-radius-4
ball. The large onsite dimension of the work cells remains explicit.

Choose the integer padding scale

\[
 B\ge\max\{b(J_p),b(J_T),8192\},\qquad K=8B.
 \tag{H11}
\]

The preparation starts with the identity guard and finishes by vertex `B`.
An identity-only cursor detour joins its final guard to the outward source
of the `T` block at vertex `3B`. Thus the prepared payload stays in a fixed
row at every vertex from `B` through `3B`. The `T` block finishes by `4B`.
All remaining edges through vertex `K` are identity edges, without further
data transfers. The final output remains in a fixed final row.

For an explicit detour, let its start guard have local coordinates `(0,0)`
and its destination source `(1,2)`, with the positive horizontal direction
pointing outside the data strip. Travel to `(d,0)`, then to `(d,2)`, then
back to `(1,2)`. Use two unit vertical edges or one length-two vertical edge.
Its length is respectively `2d+1` or `2d`, realizing the required length
`3B-b(J_p)`. The detour is outside the data strip and its rails are disjoint.
The `T` block starts toward the data strip; its final outward identity tail
is disjoint from this detour. The occasional length-two identity edge does
not enlarge the stated radius. A conservative enclosing rectangle has width
`W+8B+6` and height `2J+1` lattice units.

The full hardware count is

\[
 N_{\rm payload}=(J+1)n,\quad N_{\rm work}=(J+1)n,\quad
 N_{\rm cursor}=K+1,
\]
\[
 \dim\mathcal H=2^{(J+1)n+K+1}(2R+1)^{(J+1)n}.
 \tag{H12}
\]

In particular the full work bank has capacity
`epsilon (2R)(J+1)n`, not the capacity of one distinguished work site.
A data site occurs in at most two transfer terms and one primitive term.
A cursor site occurs in at most two edge terms, one potential, and one bare
onsite term. A conservative interaction degree is 24 other physical sites;
no degree bound hides the growing work-site dimension.

## 4. One positive, time-independent Hamiltonian on every raw state

Let `H_D` be the sum of all payload and work onsite Hamiltonians over every
row in (H12), including junk. Let `n_j` be the occupation of cursor site `j`
and `s_j^+` its raising operator. Define the scheduled data instructions
`G_j`, `0 <= j < K`, by the geometry above; identity instructions fill all
padding. Every `G_j` is a full-space unitary and commutes with `H_D`.

For `g>0`, put

\[
 a_j={g\over K+1}\sqrt{(j+1)(K-j)},\quad
 a_{-1}=a_K=0,\quad v_j=g-a_{j-1}-a_j\ge0.
 \tag{H13}
\]

The last inequality follows from `a_j <= g/2`. Set

\[
 h_j=a_j\left[(n_j+n_{j+1})I
 -s_{j+1}^+s_j^-G_j-s_j^+s_{j+1}^-G_j^{\dagger}\right],
\]
\[
 H_{\rm prop}=\sum_{j=0}^{K-1}h_j+\sum_{j=0}^{K}v_jn_j,
 \qquad
 H_0=H_D+\epsilon\sum_j n_j,\qquad
 H_{\rm tot}=H_0+H_{\rm prop}.
 \tag{H14}
\]

On cursor blocks `00`, `11`, and `span{10,01}`, an edge term is respectively
zero, `2a_j I`, and `a_j [[I,-G_j^dagger],[-G_j,I]]`. It is positive on all
raw states and has norm `2a_j <= g`. Therefore

\[
 H_{\rm tot}\ge0,\qquad [H_0,H_{\rm prop}]=0,
 \qquad [H_{\rm tot},N_c]=0,\quad N_c=\sum_jn_j.
 \tag{H15}
\]

The commutator in (H15) follows from conservation of `H_D` by every
instruction and conservation of cursor number by every hop. The interaction
energy is a real summand, not a negative cancellation of the bare battery.
Since `2 sum a_j+sum v_j=(K+1)g`, the full-space bound is

\[
 0\le H_{\rm tot}\le
 \left\{\epsilon[(J+1)(Q+2Rn)+K+1]+(K+1)g\right\}I.
 \tag{H16}
\]

Every rejected work component, dirty row, and zero- or multi-cursor
configuration evolves under this same Hermitian operator. Reverse hopping
contains `G_j^dagger`; the microscopic Hamiltonian is not strictly one-way.
Forward gates specify the ordered completed program.

## 5. Exact ideal history and two finite windows

For the comparison state with exactly one cursor at site 0, define
`F_0=I` and `F_j=G_(j-1)...G_0`. The history isometry maps
`|j> tensor |psi>` to `|j> tensor F_j|psi>`. On this sector,

\[
 H_{\rm prop}\simeq gI-{2g\over K+1}J_x.
\]

Thus, with `theta=g t/[hbar(K+1)]`, its clock probabilities are exactly

\[
 p_j(t)={K\choose j}\sin^{2j}\theta\cos^{2(K-j)}\theta.
 \tag{H17}
\]

This is the engineered perfect-transfer method of
[Christandl et al.](https://arxiv.org/abs/quant-ph/0309131v2), applied to a
unitary-labelled path. At `tau=pi hbar(K+1)/(2g)`, the cursor is exactly at
`K` and the complete word has acted, with propagation phase `-i`.

All admitted actual initial densities commute with `H_0`: the baths and work
seeds are diagonal, the logical code has fixed charge, and the cursor seed
below is diagonal. Hence the free factor generated by `H_0` cancels at the
density-operator level for all times. This remains true with the admitted
reference. No relation `epsilon=4g` and no sharp total bare energy are needed
for this family. An arbitrary cross-energy coherent input is outside this
claim and would retain its free phases.

For the preparation window choose `sin^2 theta in [3/16,1/4]` on the first
rising traversal. If `X` has the law in (H17), elementary exponential Markov
bounds give

\[
 \Pr(X<B)\le[2(29/32)^8]^B<(31/32)^B,
\]
\[
 \Pr(X>3B)\le[(5/4)^8/8]^B<(3/4)^B.
\]

For the first bound use `E 2^(-X)=(1-p/2)^(8B)`; for the second use
`E 2^X=(1+p)^(8B)`. Also `(29/32)^2<5/6` and
`2(5/6)^4=625/648<31/32`. Therefore

\[
 \delta_{\rm prep}<2(31/32)^B<2^{-255}.
 \tag{H18}
\]

Within every good history in this window the prepared original apparatus
is in the same fixed row, the old endpoint word has not begun, and all
entropy-bearing donor and work systems remain present. After tracing the
cursor, the reduced preparation error from premature or late histories is
at most `delta_prep`. A full pure-state comparison to a normalized window
packet instead costs the square root of the excluded probability; the two
statements must not be interchanged.

For the output window choose `theta in [pi/3,2pi/3]`, equivalently

\[
 {\pi\hbar(K+1)\over3g}\le t\le
 {2\pi\hbar(K+1)\over3g}.
\]

The completed tail begins at `4B=K/2`. Its weight `w(t)` obeys

\[
 w(t)=\Pr(X\ge4B),\qquad 1-w(t)\le(3/4)^{4B}=:\delta_{\rm out}.
 \tag{H19}
\]

Indeed for `p>=3/4`, Markov's inequality applied to `3^(-X)` gives the
bound in (H19). This is a new continuous window of this Hamiltonian. It is
not an inherited native-memory time interval.

## 6. Full-rank controller, output observable, and errors

The physical cursor starts in the product state with

\[
 \Pr(n_0=1)=1-r,\qquad\Pr(n_j=1)=r\ (j>0),\qquad
 r={2^{-80}\over K+1}.
 \tag{H20}
\]

Every physical cursor bit is full rank. This includes vacuum and every
multi-excitation string, not only a mixture within the one-excitation code.
The desired basis string has weight `(1-r)^(K+1)`, so its excluded weight
`eta_C'=1-(1-r)^(K+1) <= 2^(-80)`. The polarization in (H20) is supplied;
it is not prepared by the compression word whose timing it enables.
Likewise (H3) remains a supplied work resource. No exact reset is claimed.

Let `xi` be the reduced readiness error of [PREPARATION.md](PREPARATION.md).
For the central work and ideal cursor branches, (H5)-(H7) give the intended
prepared apparatus channel followed by `T`. The work tail contributes at
most `eta_B`, and the cursor tail at most `eta_C'`, by linearity and trace
norm contraction. Thus the unconditional reduced preparation window has
error at most `xi+eta_B+eta_C'+delta_prep`; the completed output has error at
most `xi+eta_B+eta_C'+delta_out`. Here trace distance means half the trace
norm. These bounds do not discard the bad branches from the physical state.

A full-space mathematical completion projector is

\[
 P_{\rm tail}=I-\prod_{j=4B}^{K}(I-n_j).
 \tag{H21}
\]

On the one-cursor history it selects precisely the completed tail. Let
`F_final` be the transported complete old read projector `Pi_read` in the
fixed final data row: the old completion latch AND the old final acceptance
flag, as defined in Section 6 of the pinned #1758 `PREPARATION.md`. In
particular the old completion latch rejects the inactive environmental
branches. The new read projector is `P_tail F_final`. The additional master
tail condition rejects an accidental read predicate in the unfinished
compiler. On the central-work, ideal-cursor component,
tracing clock, garbage, donors, work, and unretained old auxiliaries gives
exactly `w(t)` times the accepted output of the actually prepared old
apparatus. Comparing that preparation with the old ideal input introduces
`xi`. The physical bad components remain bounded as above; the exact old
selectivity ratio must not be copied without the corresponding error and
acceptance-denominator correction.

For example, if a subnormalized ideal accepted state has trace at least
`p_min` and the trace-norm distance of the actual accepted state from it is
at most `e<p_min`, normalization gives the safe bound
`2e/(p_min-e)`. One may take `e=2(xi+eta_B+eta_C'+delta_out)` from the above
trace-distance bounds. The sharper bounds in the preparation note may be
used when their hypotheses are retained.

(H21) and the final flag are specified observables, not an engineered read
instrument, a detector coupling, or a rule for realized events. The finite
window eventually closes; the positive finite Hamiltonian has no absorbing
halt or permanent storage theorem. A preparation-only word or a later
readout-and-reuse mechanism has to be specified separately if needed.

## 7. Complete initial energy and the remaining nonstationarity

Let `mu_D=Tr(H_D rho_D)` and `nu_D=Var_(rho_D)(H_D)` refer to all initial
rows, heads, donors, dirty targets, and the logical input. They include the
distinguished seed contribution

\[
 \langle H_B\rangle=\epsilon R,\qquad
 \operatorname{Var}(H_B)=\epsilon^2\eta_B{(R+1)(2R+1)\over6}.
 \tag{H22}
\]

For independent initial data and cursor, the whole-Hamiltonian moments are

\[
 \langle H_{\rm tot}\rangle
 =\mu_D+(\epsilon+g)[1+(K-1)r],
 \tag{H23}
\]
\[
 \begin{split}
 \operatorname{Var}(H_{\rm tot})={}&\nu_D
 +(\epsilon+g)^2(K+1)r(1-r)\\
 &+{g^2K\over(K+1)^2}(1-2r)^2
 +{g^2K(K+2)\over3(K+1)}r(1-r).
 \end{split}
 \tag{H24}
\]

To verify these identities, write `H_prop=g N_c-T_hop`. The initial clock
is diagonal, so every hopping expectation and its cross term with the
bare diagonal part vanishes. In `T_hop^2` only a hop and its return on the
same edge have a diagonal matrix element, and `G_j^dagger G_j=I`. Its
expectation is
`sum a_j^2[p_j(1-p_(j+1))+(1-p_j)p_(j+1)]`. Finally
`sum a_j^2=g^2 K(K+2)/[6(K+1)]`. This proves (H23)-(H24) on the full product
seed, including its multiple-cursor strings. No small tail probability is
used to erase a potentially large energy contribution.

There is still initial nonstationarity relative to the coupled Hamiltonian.
The first instruction is `G_0=I`. Partial trace of `[H_tot,rho_initial]`
over all data and all cursor sites except `0,1` has off-diagonal magnitude
`a_0(1-2r)`. Therefore

\[
 \|[H_{\rm tot},\rho_{\rm initial}]\|_1
 \ge2a_0(1-2r)>0.
 \tag{H25}
\]

For Hermitian multiples of this commutator the partial trace is trace-norm
contractive, which justifies the bound. The formula proves nonstationarity
also for mixed logical inputs with references. The full-rank tails can
produce additional commutators on later gate bonds; there is no assertion
that all nonstationarity is confined to the first bond.

All components of `H_0` and `H_prop` have their physical energy included,
and their total expectations are separately conserved by (H15). The
compression transfers entropy and energy into retained garbage and work.
The construction prepares the old apparatus approximately from the stated
moderate-temperature donors while explicitly consuming the supplied work
and controller resources. It does not prepare those remaining resources
from a stationary state of the full interacting Hamiltonian, and it does
not derive this added hardware from the native TWIST-J law.
