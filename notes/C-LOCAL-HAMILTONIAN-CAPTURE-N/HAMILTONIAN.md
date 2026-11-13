# A positive local Hamiltonian for the compiled complete circuit

**NON-CANONICAL, L1, conditional candidate-T. Independent acceptance pending.**
This is a new two-dimensional qubit model. It is not a construction from the
original TWIST-J checkpoint or occupation dynamics. No scientific executable
or numerical simulation is used in this analytical derivation.

The Hamiltonian implements the complete circuit at one deterministic physical
endpoint time. At intermediate physical times it coherently superposes
logical circuit stages. In particular, the predecessor's H native release
steps and exact logical buffer are not an H-step interval of this hardware's
physical time. Section 6 instead supplies a rigorous approximate physical
read window around the endpoint.

## 1. Input circuit and the distinction between two geometries

Let the construction in [COMPILATION.md](COMPILATION.md) supply an exact
finite circuit of R_g >= 1 one-qubit or nearest-neighbour two-qubit gates
U_0,...,U_(R_g-1) on S >= 1 qubits. All battery preparation, finite register
encodings, initialized work, original branch histories and the logical clock
belong to those S qubits. No measurement or successful computational branch
is selected during the circuit. A passive reference is arbitrary.

Set R_g to the actual G_total gate-list length and S=w to the compiler's
line width. The bounds in COMPILATION.md apply to these actual values.
Here R_g is the number of compiled gates. It is not the predecessor's object
centre coordinate R. The qubit hardware lattice below is likewise distinct
from the native object/carrier coordinates encoded by the circuit. Routing
encoded data through this lattice does not itself prove a local intertwiner
from that lattice to native occupation sites.

The compiler's target equality applies on its stated encoded/initialized
input domain. The construction below implements the compiled qubit unitary
on every input of those S qubits. All other raw qubit states also have a
well-defined Hamiltonian evolution; no correctness promise on a ready domain
is used to infer Hermiticity or erase an off-domain input.

## 2. Explicit square-lattice layout and bounded interactions

Use data qubits D_(t,j) at integer lattice coordinates

    (j,2t),   0 <= t <= R_g,   1 <= j <= S.

There is a clock rail at height 2t+1 for each gate stage 0 <= t < R_g,
containing one clock qubit at each column 0,...,S+1. Traverse the first rail
left to right, the next right to left, and continue alternately. Between two
successive rails put one additional clock qubit at their common boundary
column and intermediate height 2t+2. Thus successive clock sites are nearest
neighbours of the square lattice, including turns. They form one simple
snake path. Number its actual clock qubits c_1,...,c_K in path order, where

    K = R_g(S+2) + (R_g-1) = R_g(S+3)-1.                     (H1)

The gate word associated with this clock has one instruction G_k for each
clock site c_(k+1), k=0,...,K-1. At the two boundary columns and at vertical
connector sites the instruction is identity. At the active site above data
column j in stage t, first SWAP D_(t,j) with D_(t+1,j).

The one circuit gate U_t is applied after this SWAP at the following site:
for a one-qubit gate on column j, use that column; for a gate on neighbouring
columns j,j+1, use the endpoint visited second by the sweep. At that moment
both operands have moved to row t+1. Apply U_t to them in that new row. All
other active instructions are just the transfer SWAP. Consequently each
G_k acts on at most three data qubits: the old and new sites of the current
column and, when needed, the already transferred neighbouring operand.

Induction through a row shows that its complete instruction product moves
all S input qubits from row t to row t+1 and applies exactly U_t. The
previous contents of row t+1 move into row t. This is a complete unitary
routing identity, including dirty or entangled destination rows. Taking all
extra rows initially zero makes the intended final state especially simple:
the last row contains U_(R_g-1)...U_0 applied to the initial row, and every
earlier row is zero. No data is cloned, measured or discarded.

For each active instruction, the associated clock site and its preceding
and following clock sites are on the same horizontal rail: the two boundary
clock sites supply a guard at each end of the active columns. All data
operands are at vertical displacement one and horizontal displacement at
most one from the active clock site. At an inactive turn the instruction
is identity. Therefore each propagation term in Section 3 is supported on
at most six physical qubits, all within Manhattan radius two of its central
clock site. A conservative support diameter is four. The two-clock potential
terms have radius one.

Each clock qubit occurs in at most three propagation terms and two potential
terms. Each data qubit occurs in one incoming and one outgoing transfer and
at most the neighbouring gate contributions; four propagation terms are a
conservative upper bound. Hence every site is in at most five local terms.
The graph joining sites that occur in a common term has degree at most 25.
These constants do not grow with R_g or S. This is bounded-range geometry,
not merely a finite many-body locality order with unbounded interaction
valence. It still permits up to six-body interactions; no two-body hardware
reduction is asserted.

All occupied lattice sites have dimension two. There are (R_g+1)S data
qubits and K clock qubits. The entire layout fits in the rectangle with
columns 0,...,S+1 and heights 0,...,2R_g. Unused sites need not be present;
if included as qubits they are identity spectators. The circuit-dependent
couplings and gate matrices are hardwired model data, with a finite
classical description.

## 3. Full-space positive Hamiltonian

Use the fixed boundary values c_0=1 and c_(K+1)=0. These are constants in
the first and last interaction definitions, not additional dynamic qubits.
For 0 <= k < K, let

    P_k = |1><1|_(c_k) tensor I_(c_(k+1)) tensor |0><0|_(c_(k+2)),
    B_k = |110><100|_(c_k,c_(k+1),c_(k+2)).

At a virtual boundary remove the fixed one-dimensional factor. The operator
B_k flips the middle clock bit from zero to one, conditioned on its two
neighbours. Let g>0 have units of energy and define

    a_k = [g/(K+1)] sqrt((k+1)(K-k)),
    a_(-1) = a_K = 0.

For 0 <= j <= K let b_j be the projector onto c_j=1,c_(j+1)=0,
with the same fixed-boundary convention, and set

    v_j = g-a_(j-1)-a_j.

The time-independent hardware Hamiltonian is

    H = sum_(k=0)^(K-1) h_k + sum_(j=0)^K v_j b_j,
    h_k = a_k [P_k tensor I - B_k tensor G_k - B_k* tensor G_k*].   (H2)

All unspecified factors in each term are identities. This is a complete
operator on every clock pattern and every data input, including invalid
clock patterns and dirty registers.

On P_k=0 the term h_k vanishes. On P_k=1 its middle-clock/data block has the
form a_k times a two-by-two operator matrix with diagonal I and off-diagonal
-G_k and -G_k*. Since G_k is unitary, that matrix has eigenvalues zero and
two. Thus h_k is positive and ||h_k||=2a_k. The elementary inequality

    (k+1)(K-k) <= (K+1)^2/4

gives 2a_k<=g. It follows that 0<=v_j<=g. Every term in (H2) is positive,
and each has operator norm at most g. Moreover,

    0 <= H <= [sum_k 2a_k + sum_j v_j] I = (K+1)g I.          (H3)

The last equality uses that every a_k occurs twice in the sum of v_j.
In particular H is finite-dimensional, self-adjoint and globally bounded.
Its continuous-time evolution exp(-itH/hbar) is unitary on the entire raw
Hilbert space, irrespective of preparation. No acceptance projection is
part of that evolution.

The reverse terms B_k* tensor G_k* are necessary for Hermiticity. They are
explicit, not omitted costs. The compiled target word uses the desired
forward operations, but this Hamiltonian is not a microscopic law whose
clock can hop only forward. It is a coherent propagation Hamiltonian with
both directions and an exact forward-word endpoint.

## 4. Legal histories and exact endpoint transfer

Write |j>_C for the clock basis string containing j leading ones and K-j
zeros, for j=0,...,K. The initial clock |0>_C is the all-zero product state.
Set F_0=I and F_j=G_(j-1)...G_0. Define the history identification

    W_hist (|j> tensor psi) = |j>_C tensor F_j psi.

Orthogonal clock strings make W_hist an isometry, for all complete data
vectors psi. The image is an invariant subspace of (H2). On a legal string,
exactly b_j is one, the propagation diagonal contributes a_(j-1)+a_j, and
the two possible propagation edges carry the appropriate G or G*. Therefore

    W_hist* H W_hist = (g I-A) tensor I_data,
    A = sum_(j=0)^(K-1) a_j (|j+1><j|+|j><j+1|).             (H4)

This is a full operator identity, so it also holds with any reference
included. The isometry is a proof device; the physical preparation is just
the stated product clock with the data input, not a prepared history state.

Let J_x be the spin-K/2 x-component in the basis labelled j=0,...,K. Its
nearest-neighbour matrix entries are sqrt((j+1)(K-j))/2, whence

    A = [2g/(K+1)] J_x.

One elementary proof of the transfer identity identifies this matrix with
J_x=(1/2)sum_(r=1)^K X_r on the symmetric subspace of K mathematical spins.
The endpoint states correspond to all zeros and all ones. At rotation angle
pi, each exp(i pi X_r/2)=i X_r, so

    exp(i pi J_x)|0> = i^K |K>.

These mathematical spins are only a proof of the matrix exponential and
add no hardware beyond the K clock qubits already counted. Define

    t_* = pi hbar (K+1)/(2g).                                (H5)

Combining (H4) with the scalar phase exp(-ig t_*/hbar) gives, exactly,

    exp(-it_* H/hbar)(|0>_C tensor psi)
       = -i |K>_C tensor F_K psi.                            (H6)

The phase is -i because exp[-i pi(K+1)/2] i^K=-i. Equation (H6) holds for
all data inputs and arbitrary reference entanglement. With the compiler's
initialized data domain it therefore produces its complete intended output,
including the prepared battery and all accepted and rejected branches,
without postselecting a successful history-clock outcome.

The engineered path-transfer method is established prior art; see
[Christandl et al., Perfect state transfer in quantum spin networks][pst].
The calculation here specifies the full positive Hamiltonian and the
geometric routing used in this candidate, without claiming invention of
perfect state transfer or of history-state computation.

## 5. Clock initialization and the physical energy of this model

The physical history clock starts with every actual bit zero. There is no
supplied delocalized wave packet or one-excitation clock preparation. The
logical source, logical battery seed and compiler work are also prepared as
specified product basis states before the preparation gates begin. Those
gates, including the coherent battery loader, belong to the compiled word
and hence to the single evolution in (H6).

Product-basis readiness is an explicit initial-condition resource. For the
factors required to be zero it can be described by the local preparation
target Hamiltonian H_ready=Delta sum_i |1><1|_i, Delta>0, whose ground space
fixes those factors. Arbitrary logical inputs and their reference are not
included in this sum. This description neither proves a cooling protocol
nor makes H_ready identical to H. No switching between H_ready and H is part
of the autonomous mathematical evolution being claimed: the model begins
in its prescribed ready state with H fixed. Acquiring that initial state
from an arbitrary dirty or thermal apparatus remains a separate preparation
and entropy-account question. It is not an arbitrary-state unitary reset.

For every normalized initial data/reference vector on the all-zero physical
clock, (H4) gives

    <H> = g,
    Var(H) = a_0^2 = g^2 K/(K+1)^2.                          (H7)

Indeed (H-g)|0,psi> has exactly the one adjacent history component with norm
a_0. Both the mean and variance are conserved under the autonomous evolution.
The energy g is therefore not inferred to be zero merely because the
required clock is a simple product state. In the legal history sector the
spectrum lies in

    [g/(K+1), g(2K+1)/(K+1)],

with width 2gK/(K+1)<2g. This restricted spectral bound is distinct from the
full raw-space bound (H3).

H is the physical time generator of this declared qubit model. It is not
identified with the predecessor's separate diagonal clock/data/battery
account E_total. General circuit decomposition and rail transport do not
by themselves prove [H,E_total]=0 at intermediate hardware times, even
when the decoded completed target unitary conserves E_total. Thus preparing
and executing the encoded finite battery is established at the circuit
level; identifying its logical energy ladder with a compatible local
hardware energy requires an additional construction. The two accounts must
not be substituted for one another. The energy scale g and the lattice
spacing are supplied model parameters, not derived TWIST-J calibrations.

## 6. A physical read window and the retention boundary

The endpoint is not an absorbing state. At intermediate times the legal
history-clock amplitudes generally occupy several j values, with the
corresponding data states F_j psi. The record's native H-step buffer in the
logical target consequently supplies no exact interval of physical clock
time in this Hamiltonian. The hardware qubits also physically move encoded
carrier and receiver information between rows. Native-coordinate holding
and fixed-location hardware storage are different assertions.

There is, however, a uniform physical-time stability bound near the exact
endpoint. Let Psi_* be the normalized right side of (H6), including every
reference. Remove the irrelevant phase exp(-ig delta_t/hbar). The integral
form of the unitary evolution and conservation of ||(H-g)Psi_*||=a_0 give

    || exp[-i(H-g)delta_t/hbar] Psi_* - Psi_* ||
       <= min(2, |delta_t| a_0/hbar).                         (H8)

Thus the complete state at t_*+delta_t, modulo that common phase, is within
eta_time=|delta_t|g sqrt(K)/[(K+1)hbar] of the exact endpoint, capped by two.
The bound is uniform over data and reference inputs. Every fixed physical
output effect has weight error at most min(1,eta_time), and partial tracing
cannot enlarge the trace distance. Conditional comparisons after a rare
acceptance still require their appropriate normalization bound; the time
error has not inherited the source-specific diagonal-energy exception of
the preceding battery proof.

For any required whole-state tolerance eta>0, the sufficient read window is

    |delta_t| <= eta hbar (K+1)/(g sqrt(K)).                  (H9)

This is a physical-time statement in the declared generator model, using
its chosen g. It is an approximate finite window, not permanent memory or
native empirical occurrence. Exact endpoint timing is unnecessary if this
window and its error budget are acceptable.

The same spin rotation gives complete return up to phase at 2t_*. The
coherent circuit can then be traversed again; this is not a useful detector
reset that preserves a newly copied external history. No irreversible halt,
unlimited archive, independently renewed trial or selected realized event
is supplied by the Hamiltonian.

## 7. What is constructed and what remains open

The positive result is an exact endpoint implementation of the complete
compiled target by a time-independent, positive, bounded-strength Hamiltonian
on a finite two-dimensional lattice of qubits, with bounded interaction
range and valence. All raw states have a Hermitian law; all reference
correlations and branch histories are retained. The initial clock is a
basis product, the coherent logical battery preparation is in the word,
and a quantitative physical endpoint window is given.

The construction explicitly adds the qubit lattice, its ready resources,
its hardwired gate interactions and spatially varying engineered couplings.
It uses up to six-body interactions with exact prescribed coefficients.
It does not derive those interactions from original occupation cells,
compile a finite fixed universal interaction alphabet without further
approximation, calibrate g or distance, prove arbitrary dirty-state renewal,
or identify the logical battery account with the physical generator.
A two-body implementation, coupling-error budget, resource preparation from
a specified physical source and an exact native spatial encoding need their
own proofs. Logical forward sufficiency survives in the endpoint word;
strictly forward microscopic clock hopping does not.

[pst]: https://arxiv.org/abs/quant-ph/0309131v2
