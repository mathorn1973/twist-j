# Independent derivation and attempted breaks

**NON-CANONICAL. Written before exposure to author Stage-C proof/code/output.
Prospective proof review; no execution or final acceptance is asserted.**
Inputs, exposure and finite audit scope are fixed in PREREG.md.

## 1. Start with complete states, not a clean effective qubit

Order the physical path slots as C0,Q0,C1,Q1,...,C(N-1). At the rightmost
slot the support predicate depends only on b,y and is unchanged by G. In
the supported sector the output sets are disjoint: latch one comes from
funded latch zero, latch zero with reserve at least two comes from latch
one, and latch zero with smaller reserve is fixed. The stated inverse
therefore has exactly one nonnegative-reserve preimage at every output.
Unsupported sectors are fixed. Each matching swaps complete six-coordinate
packets. Reversing the order of the matchings and then G proves the full
inverse, with or without a fixed cut. Dirty fields and old channel contents
are not removed from this argument.

The receiver preserves r+2l and b,y; each matching preserves the multiset of
complete packet accounts. Thus the full diagonal E_B is invariant. From B,
`2H(Ca)=a2^2+(a2-a0)^2+(a0-a3)^2+(a3-a1)^2+a1^2`, so bounded H bounds all
integer coefficients. At fixed finite energy there are finitely many basis
states. A bijection of a countable orthonormal basis extends by norm
completion to a unitary of ell^2, and its inverse is the extension of the
classical inverse. It permutes each energy eigenspace, hence strongly
commutes with the diagonal energy operator on its domain. This establishes
the lift on the entire carrier, not just on a single-packet slice.

The K finite archive registers add exactly 2K to the stipulated energy.
Their dimension is finite. Shell source unitaries are direct sums over
presence, reserve and energy and preserve the same operator; the identity
completes every unassigned block. The Fourier and append controls preserve
flat pointer/flag energy. Periodicity follows for the classical finite-shell
permutation only. A unitary with an irrational eigenphase on a finite shell
already defeats an attempted periodicity claim for arbitrary added controls;
the specification correctly excludes that inference.

## 2. Derive the clean joint state from actual path motion

The two path matchings send Cj to C(j+1), the rightmost cell to the last
channel, each channel to its predecessor, and Q0 to C0. This is one cycle
of length T=2N-1. The receiver is first occupied at boundary N-1 and is
reacted on at step N. Its successive visits are T steps apart. Reserve
two/latch zero and reserve zero/latch one alternate, so writes occur at
N+2mT and releases at N+(2m+1)T. Induction gives the stated e(n), w(n),
packet position, reserve, latch and pointer p0+w(n)c(y) at every boundary.
At 2T the operative geometry is initial and exactly one translation remains.

Consequently the clean isometry is a controlled shift, without replacing
the B law: `|y;0>|p> -> |y;n>S_(w(n)c(y))|p>`. Applying this identity to
both legs of a matrix unit yields the full correlated-input formula.
Sandwich with a read projector and trace only the pointer to obtain the
displayed partial-trace expression. With a product pointer density sigma,
each source block is multiplied by gamma_o(a,b). Necessity of equality of
all coefficients follows by testing matrix units; sufficiency follows by
linearity. Density inputs span the operator algebra by polarization, so the
criterion does not depend on allowing nonphysical operator tests as inputs.
Tensoring with arbitrary finite references preserves the identity termwise.
Initial source-pointer correlations cannot in general be reduced to a map
of the source marginal; the joint formula correctly retains them.

## 3. Coherent readiness and a uniqueness argument on the promised interface

Translation permutes the two uniform parity sums E,O, with action X^(c mod2).
After E readiness, all labels of one code parity have exactly the same
pointer vector. The parity projector keeps that vector or annihilates it.
Thus gamma is one when both source labels belong to the selected parity and
zero otherwise. O exchanges read names. With a diagonal pointer density,
translation of the ket and bra can have nonzero trace only if their distinct
codes are equal modulo M. The code is injective and has values 1,...,1225,
so every distinct-label off-diagonal is destroyed for blank and diagonal-even
preparations. This supplies an exact negative boundary, not an empirical
preference for coherent readiness. The entangled HIGH state
`(f1|0>+f2|1>)/sqrt(2)` makes this difference persist with an untouched
reference.

For the fixed LOW=odd reader, a sharp HIGH effect for any of the three even
codes forces the positive density sigma to have no odd support. In detail,
trace against the odd projector vanishes, so its product with sigma^(1/2)
has zero Hilbert-Schmidt norm. Hence sigma is supported on even positions.
Preservation of f2,f3 coherence then requires `tr(sigma S_28)=1` (the inverse
shift convention gives the same fixed space). For any unitary U,
`tr[sigma (I-U)^*(I-U)]=2-2Re tr(sigma U)`. Equality to zero implies
`(I-U)sigma^(1/2)=0`. Thus sigma is supported in Fix(S_28). The additive
subgroup generated by 28 mod1226 consists of every even residue because
gcd(28,1226)=2. A fixed vector has constant coordinates on each parity orbit.
The even fixed space is the single line E. A positive trace-one operator
on that line is exactly |E><E|. Sufficiency was already proved. With fixed
parity relabeling the identical argument gives unique O. This is selection
by a specified target instrument, not independent physical preparation.

The optional Fourier control is unitary because the inner product of its
j and k columns is `L^-1 sum_t exp(2pi i(j-k)t/L)`, one for j=k and zero
otherwise by the finite geometric sum. It maps basis zero to E but is not
erasure: a dirty density is transformed unitarily and need not become ready.
Diagonal mixtures remain diagonal under basis permutations; no B-only
mixture of such operations creates the off-diagonals of |E><E|.

## 4. A rational chart for the four-label comparison

Let B have columns v0=(1,1,1,1), v1=(1,-1,0,0), v2=(1,1,-2,0),
v3=(1,1,1,-3). Then `B^*GB=W=diag(4/5,2,6,12)`. The normalized columns
`v_j/sqrt(W_jj)` are precisely the advertised u0,q1,q2,q3. Define T=B^-1
as a logical chart. Physical coefficient f_j and chart coefficient g_j are
related by the fixed scaling f_j=sqrt(W_jj)g_j, so the chart metric is W.
For endomorphisms the chart map is `X -> T X B`; the adjoint is
`A^sharp=W^-1 A^* W`. This avoids radicals in audit arithmetic without
changing the Hilbert-space map V. In particular `V=B^-1` followed by the
positive diagonal scaling, so `V^*V=G` and `V^sharp V=I`.

The actual four packet labels all have H=1. Their writer parity projector
is L=diag(1,0,0,0), with H=I-L. Because R is G-unitary, its chart matrix
`Rhat=T R B` is W-unitary. Source precontrol is Rhat^-k and postcontrol is
Rhat^k at C0. Composing them around the controlled parity writer gives
branch matrices `Rhat^k L Rhat^-k` and `Rhat^k H Rhat^-k`, exactly
`T Pk B` and `T Qk B`. Checking every matrix unit proves complete branch
equality and its finite-reference extension. Arbitrary admitted source
unitaries use the same argument with U^sharp L U and U^sharp H U. No
scalar classical field label is identified with a coherent amplitude.

## 5. Archives, dirty states and supported histories

Append sends `(p,p_i,z_i)` to `(p_i,p,1-z_i)`. Applying it twice restores
every input. It preserves the selected constant energies, and it exchanges
quantum correlations as well as basis values. For a fresh E,0 archive cell,
the old active phase moves to the archive, active becomes E and the flag
becomes one. For an occupied cell active receives the old archived phase and
the flag becomes zero. A dirty E/O phase or other pointer state at a zero
flag is still dirty readiness. Appending after an absent/underfunded trial
creates syntactic flag one without a WRITE. These counterexamples invalidate
universal event detection, automatic erasure and source-provenance readings;
the specification explicitly disclaims all three.

On the promised ready slice the full round is, chronologically, D, U,
actual 2T B steps, U^sharp, append. Reverse the factors to obtain the stated
all-state inverse. At the macro boundary the source is at C0, reserve two,
latch zero and active E, with the new source-record correlations retained.
The source is not replaced. The records `(E,1),(O,1),(E,0)` distinguish
HIGH, LOW and unused. An external program supplies context, epoch and index;
the two archive coordinates alone do not contain the canonical physical
record tuple. K fresh cells permit at most K promised appends. Exhaustion
is a descriptor-level stop retaining state, not a reversible absorbing halt.

Expand one ready round as the isometry
`v -> (U^sharp L U D)v |L_i> + (U^sharp H U D)v |H_i>`.
Inducting over a supplied causal program yields K_w and every retained
history term. Parity reads delete exactly the cross terms with different
read labels. Without those reads a fixed-depth coherently controlled
program retains `K_w rho K_v^sharp |record(w)><record(v)|`. The record
basis also includes flags and ordered unused cells. The construction is
linear on the source and identity on any finite untouched reference.

At each node `sum_o M_(w,o)^sharp M_(w,o)=I`, so summing the next traces
returns the prefix trace. Induction gives normalization over every complete
bounded stopping tree. Positive trace permits normalization; zero branches
remain zero. At a repeated fixed context with D=I, projector orthogonality
kills mixed words and idempotence preserves the two constant words. These
are dependent rereads. A second unarchived round acts twice on the same
phase, cancelling for a repeated writer instead of retaining a second fresh
record. Source replacement would be a different supplied operation.

For passive retention, partial tracing a trace-preserving operation on the
complement fixes the archive marginal by its adjoint fixing identity. After
parity dephasing, later parity-controlled source channels preserve each old
diagonal block trace. Before dephasing their different left/right actions
can alter cross-block overlaps; there is no entire-quantum-archive retention
theorem for coherent feedback. Direct archive Fourier operations, reuse,
unappend and inverses likewise lie outside the passive promise.

## 6. What whole-family equality does and does not say

After a fixed output identification, different retained preparations can
already differ at the empty protocol. Equality of a reduced first-use
instrument cannot identify E and O as full retained states. A phase change
is a legitimate descriptor equivalence only when one fixed coordinate
unitary intertwines preparation, all labeled operations and reads and the
output interface; it is not inferred from matching one effect.

On a finite invariant energy sector, vectorize the two retained operator
spaces and pair their branch maps. The span W of all reachable paired
matrix-unit preparations is the least invariant linear subspace containing
the seeds. The iterative construction must stabilize because dimension is
bounded by d1^2+d2^2. If the output difference vanishes on W it vanishes
on every reachable word and linear combination. Conversely, if every word
output agrees then every spanning reachable vector is in its kernel. This
proves necessity and sufficiency. Finite causal tree branches are words;
the same result applies branchwise with zero padding for absent labels.
Exact effective coefficients make Gaussian elimination an algorithm. The
proof supplies no algorithm over unspecified complex constants, no finite
classification over unbounded energy, and no replacement of an uncountable
operation family by one finite alphabet.

## 7. Scope verdict before runs and author comparison

No mathematical counterexample has been found by this independent paper
derivation. The natural attempted breaks instead show why the stated
restrictions matter: dirty append can falsely mark validity; a fine or
diagonal pointer loses HIGH coherence; a second unarchived round is not
fresh; a source-pointer correlation prevents a source-marginal channel;
and equality of effects does not erase retained phase or future memory.

The accepted predecessor supplies a classical reversible carrier. Complex
extension, coherent readiness, selected shell controls, pointer degeneracy,
finite archive and externally scheduled conditional reads are additional
choices. WRITE is a deterministic branch on complete classical basis states,
but a parity branch trace is not a mechanism selecting one realized outcome.
This review cannot infer the physical selected QDD dictionary, terminal
saturation law, complete physical apparatus class, Born occurrence or native
preparation from the formulas. The corresponding Canon owners remain open.
Final acceptance still requires comparison against the independently frozen
author proof/code and exact pinned execution with retained falsifiers.
