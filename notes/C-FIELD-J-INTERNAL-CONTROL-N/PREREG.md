# Internal fetched-program control of the finite prepared instrument

**PUBLIC, NON-CANONICAL. Proposed conditional L1 theorem; no scientific
execution or earned verdict is asserted by this specification.**

Owner: A. M. Thorn / control_builder; coordinator: root. Original work,
Apache-2.0. Public reservation: issue #1333. Prepared 2 October 2026.
Author-side discussion with the coordinator is disclosed coauthorship,
not independent review. The known target, source proofs and proposed
controller are exposed. No blindness to the desired instrument is claimed.
The coordinator-authored [OCCURRENCE_INTERFACE.md](OCCURRENCE_INTERFACE.md),
with disclosed control_ownership assistance, is a specification annex
frozen alongside this file and available to the fresh reviewer. It is
not an author proof or an occurrence mechanism.

## 1. Authority, admitted inputs and the one new question

Authority remains Public Canon v96, public main and peeled tag
`44423153eee6259c7277eec5f5adbed9679f9146`, with declared content commit
`d63de7e7345cf5fa5ab344654aafb7238d6d8bca`. The coordinator has checked the
live authority, hashes, required checks and ownership before reservation.
These observations do not give this branch normative authority.

The scientific receiving pins are:

* Exact conditional Stage C, PR #1330:
  `024936502544c2ec45acc8890a052c7b3aca26be`, especially
  `notes/C-FIELD-J-LOCAL-INSTRUMENT-N/{PREREG,PROOF,RESULT}.md`
  and its independent review.
* Approximate preparation P, PR #1332:
  `1f88665ce8646cdf134cb4366958db0ca2d302d7`, especially
  `notes/C-FIELD-J-PREPARATION-MECHANISM-N/{PREREG,PROOF,RESULT,INTERFACE}.md`
  and `notes/C-FIELD-J-PREPARATION-MECHANISM-REVIEW-N/REVIEW.md`.
* The earlier local moving-head construction, issue #1294,
  `fd792d32b3efa90c15a46e065d6637ac8600cdcf`,
  `notes/C-J-LOCAL-RAMIFIED-MEMORY-N/PROOF.md`, section 8. It already
  supplies a fixed one-head controller for a chosen word of classical
  arithmetic passes. It is credited as background, not claimed as new.

The new question is whether an initialized **data program** can execute
the entire finite P loader and a supported nonadaptive C measurement
sequence under one fixed local update, with actual instruction fetch,
operand access, invocation storage, archive allocation and continuation.
No new writer, convergence rate, physical energy selection or sampler is
requested. Merely adding a clock to the external gate list is insufficient.

The work order `TWIST_J_after_1332_internal_control_work_order.md` is a
non-normative dispatch. Its stated ceiling is retained. Current public
POLICY/AGENTS procedures govern publication and execution. No scientific
program may execute or be imported until its complete public immutable
pin and readback. A fresh reviewer receives this publicly pinned
specification and admitted old sources, but not the new author proof,
implementation or output before its own proof/program freeze and first run.

## 2. State category, equality and parameters

The state category is **2: a vector/density operator on a declared complex
extension, with one total unitary update**. It is not identified with the
native integer state or with a realized single outcome. The full density
operator is the complete mathematical state of this candidate. Neither a
classical program basis value nor an orthogonal archive decomposition
supplies a rule selecting one actual LOW/HIGH word.

Fix integers N>=2, K>=0, L>=3 and m=K+1. The receiving application is
L=613 and M=2L=1226. Let T=2N-1. The C packet space is

```text
P = {0,1} x Z^4 x N_0,       packet x=(b,y,r).
```

The inherited complete C carrier consists of T packet registers, latch
ell in {0,1}, active pointer q_0 in Z_(2L), and K archive pairs
(q_(a+1),z_a) in Z_(2L) x {0,1}, 0<=a<K. At L=613 its receiver,
code c(y), support K5, four source labels, transport swaps, context
controls and flag/parity reader are exactly those of C. Smaller L below
is used only for the uniform P collision and labeled finite audit models;
it does not replace the physical comparison code by a smaller one.

Choose finite n_i>=0 and B=L sum_i n_i, allocate B retained bath qubits,
and choose h<=K nonadaptive contexts k_0,...,k_(h-1). A context catalogue
has c>=1 members and is an ordered collection (U_0,...,U_(c-1)) of specified unitaries
on C's four-source subspace, extended as in C by identity elsewhere and
identically at each reserve. It is fixed as part of the device law before
the program is loaded. It may be C's five U_k. An instruction selects a
catalogue index; no finite exact programmable processor for arbitrary
unknown unitaries is asserted. The finite audit uses a separately named
rational catalogue admitted by C's arbitrary-U(4) clause.

Only D=I source interventions are compiled in this first subclass. The
source is retained between rounds; it is never renewed by declaration.
Both repeated and changed contexts are included. Settings and their
initial independence/correlation assumptions are supplied initialization
data, not generated or selected from bath/record values.

Equality means equality of **complete joint operator maps**, with the
program, controller, every memory/bus register, metadata and arbitrary
finite reference retained. At a named command boundary there is a fixed
coordinate identification to the external primitive program plus its
deterministic controller/metadata state. At intermediate microticks the
explicit partial routing unitary, not an inherited B step, is the
identification. Equality of parity weights alone is not acceptance.

## 3. Complete new storage and its ready domain

For an integer d>=1 let w(d)=max(1,ceil(log2 d)). Finite modular counters
below use their exact stated cyclic sets; XOR words use bit strings of
the displayed width. Unused bit patterns are not silently discarded.
Let ewidth=w(K+1), cwidth=w(c), pwidth=w(K+1), jwidth=w(L),
xwidth=w(T). A program word has fields

```text
(opcode:4 bits, inverse:1 bit, i:pwidth, j:jwidth,
 x:xwidth, y:xwidth, k:cwidth).
```

Its width is v=5+pwidth+jwidth+2*xwidth+cwidth. Opcode numbers are
0 NOP, 1 COLLIDE, 2 CTX_PLUS, 3 CTX_MINUS, 4 RECEIVER,
5 PACKET_SWAP, 6 OPEN, 7 CLOSE, 8 APPEND. Codes 9..15 decode to NOP.
Required argument ranges are checked only in the local decoder:
COLLIDE requires i<=K,j<L; PACKET_SWAP requires x,y<T and x!=y;
OPEN/CLOSE require k<c. Invalid required arguments also decode to NOP.
Unused arguments are ignored, not presumed zero. The inverse bit selects
the precisely specified inverse command. Invalid opcodes/arguments never
project the state or erase their stored word.

There are S immutable program-word registers A_0,...,A_(S-1), each v
bits. Immutable means no update targets these registers; coherent or
dirty values remain part of the all-state unitary, with no promise of a
classical instruction stream. An additional immutable descriptor word
Theta stores the finite binary encodings of (N,K,L,B,c,h,W,n_0,...,n_K,
k_0,...,k_(h-1),S,g,d), the catalogue identifier and either a requested
positive rational precision (numerator,denominator) or NONE. Its finite
bit width is declared before initialization and it is an isolated memory
vertex. Its consistency with the compiled tape and fixed device capacities
is an input promise, not a hidden runtime validator. The requested
precision does not replace the actual P bound or measure its fidelity.
Here is its exact encoding, so the descriptor is a retained register
rather than an implicit prose object. For n>=0 let b(n) be the ordinary
binary string for n+1, let ell(n) be its length, and put
gamma(n)=1^ell(n) 0 b(n). Concatenate gamma for N,K,L,B,c,h,W, then
the K+1 values n_i, then the h values k_t, then S,g,d, in those orders.
Append gamma of the catalogue identifier's UTF-8 byte length and the
literal eight-bit bytes of that identifier. Finally append 0 for NONE,
or 1 gamma(u) gamma(v) for the precision u/v in lowest terms, 1<=u<=v.
Choose the fixed device parameter theta_width at least this finite
length and pad on the right with zero bits to theta_width. The prefix
code and preceding counts give unique decoding of every consistent
descriptor and its final padding; equal canonical padded words mean
equal descriptor tuples at this fixed width. Arbitrary other words
remain valid raw quantum register states and are never run through a
hidden decoder or readiness test. The finite catalogue identifier names
the already fixed device catalogue; it cannot itself install an unknown
unitary. The width and identifier bytes are declared device parameters
before the program is initialized.
There are also K metadata words

```text
mu_a = (invocation:ewidth, context:cwidth, appended:1 bit).
```

Exactly one mobile head is part of the complete carrier, not a
postselected one-particle sector of an undeclared multihead model. Its
position is a vertex of a finite rail cycle Z_d. It carries:

```text
pc in Z_S; q in {0,1}^v;
a,e in Z_(K+1); b in Z_(B+1);
f_A,f_B in Z_(S+1);
I in {0,1}^ewidth; C in {0,1}^cwidth; run in {0,1};
two packet buses X,Y in P;
two pointer buses P0,P1 in Z_(2L);
latch bus l0, flag bus z0, bath bus beta in {0,1};
metadata bus mu0 in {0,1}^(ewidth+cwidth+1).
```

Here a is the next archive cursor, b the next bath cursor, e the epoch,
I/C the active invocation/context, and f_A/f_B count failed capacity
requests modulo S+1. The latter are retained reversible counters, not
readiness tests. There is no extra address oracle, branch selector,
unrecorded source label, random seed or desired-outcome tape.

The complete Hilbert space is the tensor product of all listed stationary
memory factors, all head internal factors and C^d for its position,
with an arbitrary finite reference R. Packet factors are countable;
all other factors are finite for a chosen device. This exact tensor
product, rather than its clean slice, is the all-state domain.

For the positive compiler theorem, program/descriptor memory is the
specified consistent basis data and is independent of the physical data;
head position, pc,q,a,b,e,f_A,f_B,
I,C,run are initially zero. Metadata mu_a is initially zero when the
claimed fresh invocation/provenance interpretation is used. The **buses
need not be pure or blank**: their full initial joint state can be
arbitrary and correlated with data/reference. They are restored at each
completed command, with all correlations, by the routing identity below.
A simple nonempty example uses basis-zero buses, which is an additional
available preparation, not a hidden E resource.

For the positive P/C handoff additionally require the inherited promises:
even pointer support, fresh independent zero baths, C ready packet/latch
geometry, source code/state, zero archive flags and the chosen exact
couplings. All other initial pointer/source/reference/bus correlations
allowed by P remain allowed. Wrong parity, dirty baths, flags or head
scratch are not repaired or detected. They have the total raw unitary
evolution specified below and may fail the promised interpretation.
In particular, fresh pure bath inputs in the P claim are independent of
the buses too; the broader control theorem's dirty correlations cannot
override this preparation premise.

## 4. Local port graph and one fixed microscopic update

Stationary memory has one vertex per actual register. The head moves on
a finite cycle of named stations. The tour is, in this exact order:

```text
FETCH A_0,...,A_(S-1);
PRE;
GET: X-packet ports 0..T-1, Y-packet ports 0..T-1,
     P0-pointer ports 0..K, P1-pointer ports 0..K,
     latch port, z0-flag ports 0..K-1,
     mu0-metadata ports 0..K-1, beta-bath ports 0..B-1;
EXEC;
PUT: the same GET port list in reverse order;
POST;
UNFETCH A_(S-1),...,A_0;
ADVANCE-PC.
```

There are g=2T+2(K+1)+1+K+K+B=4N+4K+B+1 GET ports and

```text
d = 2S + 2g + 4
```

head microticks per complete command. Each FETCH/UNFETCH station is
attached to the **same** indicated program vertex. GET/PUT occurrences
and two bus lanes likewise attach to the same underlying data vertex;
there are no duplicate memories concealed in the graph. A memory vertex
has degree at most four, a rail station at most three, and processor
stations need no extra stationary operand. These counts ignore parallel
edges by treating the named ports as distinct rail vertices.

A port gate acts only on the head's internal registers and the one memory
vertex adjacent to its current station. Processor gates act entirely on
head registers. A head move goes to the next rail station. Thus the
interaction has graph radius one and the interaction-plus-shift and
its inverse have a conservative radius two in this selected port graph.
This is not C's spatial packet chain, nor a physical embedding of it.
The head alphabet, local word widths, packet alphabet and graph grow
with the declared capacities. No uniform finite-alphabet or fixed local
Hilbert-dimension theorem is claimed.

Let J_s be the total unitary station gate just specified below at rail
position s. Every J_s leaves the position unchanged. The **single fixed
update** is

```text
F = sum_(s in Z_d) |s+1><s| tensor J_s,
F^-1 = sum_(s in Z_d) |s><s+1| tensor J_s^*.
```

Both formulas apply to arbitrary superpositions of head position,
program, counters and dirty memory. The station law is unchanged at
runtime. For fixed capacities/catalogue the program contents are data:
changing them does not replace F by a new gate list. All-state unitarity
must be proved from the individual local factors and the position shift,
not inferred from successful initialized trajectories.

At FETCH/UNFETCH port t, J_s is

```text
if pc=t: q <- q XOR A_t; otherwise identity.
```

This is an involution for every program/scratch value. It is a local
word comparator and controlled addition, not an uncounted nonlocal RAM
lookup. At ADVANCE-PC, pc increments modulo S. FETCH therefore reads
one actual word into clean q, UNFETCH clears that same q by revisiting
the retained program, and only then is pc advanced. The program is
never copied into an unbounded command history.

## 5. Addressed extraction, decoded gates and counters

At a GET or PUT port, a controlled SWAP exchanges the indicated bus with
that stationary register iff the decoded command selects that bus/address.
There is no dependence on the value of the exchanged data. The selectors
use the current head q,a,b only; a and b are held fixed throughout GET,
EXEC and PUT. The selection table is complete:

| Opcode | Extracted operands |
|---|---|
| NOP, OPEN, CLOSE | none |
| COLLIDE(i,j) | P0 with pointer i; beta with bath b if b<B |
| CTX_PLUS, CTX_MINUS | X with source packet C_0 |
| RECEIVER | X with receiver packet C_(N-1); l0 with latch; P0 with active pointer 0 |
| PACKET_SWAP(x,y) | X with packet x; Y with distinct packet y |
| APPEND | P0 with active pointer 0; if a<K, P1 with pointer a+1, z0 with flag a, mu0 with metadata a |

The packet order used in addresses is
(C_0,...,C_(N-1),Q_(N-2),...,Q_0). Each listed valid operand has exactly
one matching memory port in its bus lane. Operand roles of the same
type are distinct for supported commands. Invalid encoded addresses
decode to NOP; exhausted cursors have the explicit partial selection in
the table. Every port is still an ordinary controlled SWAP on the full
carrier. Coherent selectors give controlled unitaries rather than a
measurement of the selector.

At EXEC, for a forward command use V_o below, and for an inverse command
use its adjoint. Conditions depend only on unchanged head controls:

| Opcode | V_o on the extracted buses/head |
|---|---|
| NOP | identity |
| COLLIDE(i,j) | if b<B, P's exact zero-phase edge-j reflection U_j on P0,beta; otherwise identity |
| CTX_PLUS | U_C on X if C<c; otherwise identity |
| CTX_MINUS | U_C^* on X if C<c; otherwise identity |
| RECEIVER | C's complete receiver G on X,l0,P0, including unsupported and underfunded branches |
| PACKET_SWAP | SWAP X,Y |
| OPEN(k), CLOSE(k) | I XOR= binary(e); C XOR= binary(k); run XOR=1 |
| APPEND | if a<K, SWAP P0,P1; z0 XOR=1; mu0 XOR=(I,C,1); otherwise identity |

For completeness P's reflection is U_j=I-2|nu_j><nu_j|, with
nu_j=(d_j|0>-s_j|1>)/sqrt(2), d_j=(|2j>-|2(j+1)>)/sqrt(2),
s_j=(|2j>+|2(j+1)>)/sqrt(2), cyclic j modulo L. It is the
identity on the odd pointer sector. No global E or Fourier preparation
gate has been added. C's G is the existing support-controlled, funded
pointer translation/release permutation; its supplied inverse, not G
again, is used for inverse RECEIVER.

Define a head-only bijection A_o as follows. All unmentioned registers
are unchanged, and the order of the simultaneous expression is explicit:

```text
COLLIDE: f_B <- f_B + [b=B] mod(S+1), then b <- b+1 mod(B+1).
APPEND:  f_A <- f_A + [a=K] mod(S+1), then a <- a+1 mod(K+1).
CLOSE:   e <- e+1 mod(K+1).
others:  identity.
```

Its inverse first decrements the cursor and then subtracts the indicator
of that recovered old cursor; CLOSE decrements e. At PRE apply A_o^-1
only for inverse commands. At POST apply A_o only for forward commands.
The other polarity uses identity at that station. This placement matters:
inverse commands recover the old addresses **before** extraction.

For valid addresses let R_o be the product of the actual GET swaps in
the displayed order. PUT is R_o^-1, including arbitrary dirty buses.
On a command-entry section with fixed fetched instruction the logical
maps are exactly

```text
M_(o,+) = A_o R_o^-1 V_o R_o,
M_(o,-) = R_o^-1 V_o^* R_o A_o^-1 = M_(o,+)^-1,
```

where R_o on the right of the inverse expression uses the recovered
counter values. OPEN/CLOSE change only I,C,run and have no extracted
operands; all other V_o leave selectors unchanged. This establishes the
needed control commutation rather than assuming it. With supported,
distinct targets, R_o^-1 V_o R_o is V_o on the named memory operands
and identity on all buses, even on correlated inputs. With exhausted
addresses it is the explicitly declared identity data action plus the
reversible cursor/failure update. No all-state gate conditionally erases
an occupied archive or creates a fresh bath.

The failed-request counters distinguish an attempted append at a=K or
collision at b=B from ordinary program completion using exactly the
available capacity. Their values count such attempts during a prefix
of at most S **forward-polarity** commands from zero before modular wrap
is possible. Inverse commands subtract their recovered forward indicator;
arbitrary mixed-polarity or dirty starts have raw modular values, not
nonnegative lifetime failure counts. They
are not irreversible sticky error flags, provenance certificates on
arbitrary dirty states or total classical readers of coherent programs.

## 6. Compiler, useful lifetime and all-step timing

The compiler is finite syntactic expansion, fixed before inspecting any
physical output. First emit COLLIDE(i,j), with forward polarity, for
i=0,...,K, sweep=0,...,n_i-1, j=0,...,L-1 in that order. It encodes no
bath address: the actual b cursor supplies addresses 0,...,B-1.

For round t=0,...,h-1 emit exactly:

```text
OPEN(k_t), CTX_PLUS,
2T copies of [RECEIVER, all A whole-packet swaps, all B whole-packet swaps],
CTX_MINUS, APPEND, CLOSE(k_t).
```

The A matching is (C_j,Q_j), j increasing 0..N-2; the B matching is
(Q_j,C_(j+1)), j increasing 0..N-2. Each matching has disjoint factors,
so the specified serialization equals the inherited parallel matching.
One inherited F_B=B A G step therefore costs T=2N-1 completed commands.
One C round uses 2T^2+5 commands; no duration for its source controls or
append is borrowed from a B step.

Let H=B+h(2T^2+5). Choose a finite integer W>=1. The stored program is:
the H forward commands, W NOPs, and the H forward commands in reverse
order with their inverse bits toggled. Its length is S=2H+W. For H=0
it consists entirely of NOPs. The initialized descriptors N,K,L,n_i,h,
contexts,W and derived capacities are explicit initial design data, not
an online stopping predicate or a desired parity sequence.

At each command boundary the head has returned to position zero and q
to zero; pc has advanced once. At every intermediate microtick the state
is the exact prefix of the fixed station word applied to the preceding
boundary state. This partial word gives an isometric embedding of the
retained logical state plus buses. The source or pointer may temporarily
reside on a bus. It is not claimed to stay at C's named packet location
through the extraction tour; it is restored at the specified boundaries.

Preparation ends at microtick B*d. Round t starts at
(B+t(2T^2+5))*d. Its OPEN completes after d more ticks, precontext after
2d more, and inherited B-step s (1<=s<=2T) completes at

```text
(B+t(2T^2+5)+2+s*T)*d.
```

The receiver reaction in B-step s precedes that step's completed boundary
by its remaining T-1 swap commands: the receiver command boundary is

```text
(B+t(2T^2+5)+2+(s-1)*T+1)*d.
```

On C's clean sector WRITE occurs at s=N and RELEASE at s=N+T, using the
inherited local funded predicate. The actual processor G action occurs
at its EXEC station inside that command; its precise microtick is the
command-entry tick plus S+1+g+1. The +1 counts PRE and the final +1 the
EXEC gate's completed transition; FETCH occupies the first S ticks.

After 2T B steps the operative packet/reserve/latch geometry returns,
the postcontext completes, APPEND completes, and CLOSE completes the
round. The source itself has not been reset. OPEN sets I=t,C=k_t,run=1
on the admitted initial registers. APPEND uses a=t to choose the actual
archive address and deposits (t,k_t,1) in mu_t. CLOSE clears I,C,run and
increments e. Consequently after t completed rounds a=e=t; all earlier
cells have flag one and metadata (u,k_u,1), and later cells have their
initial zero flag/metadata. This is the scoped proof of unused-cell
selection and invocation association, not an inference from a flag alone.

The data read window is the interval H*d <= tau < (H+W)*d. During it
every data-memory GET/PUT and EXEC gate is identity, although the head,
pc and program fetch scratch move. Earlier records are also untouched
by later forward rounds, since their actual cursor addresses differ.
Exactly h<=K records are promised. Completion at h=K is PROGRAM_COMPLETE,
not a capacity failure. An additional APPEND requested with a=K has
identity data action, increments f_A and advances the cyclic cursor;
it is a counted CAPACITY_EXHAUSTED request, not a new valid record.

After the read window, the inverse tail undoes the entire command word.
At time S*d the correct initialized program/controller returns to its
start and all data/buses/metadata return exactly to their input state.
The head continues cyclically; no absorbing halt exists. This return is
for unmeasured coherent evolution. An external parity measurement that
discards its apparatus is not automatically reversed. The inverse tail
is outside the passive-record/bath-isolation comparison interval.

## 7. Bath isolation, coherence and energy/resource ledger

The initialized b cursor is the rank of the next COLLIDE in the loader.
Induction gives each of the B allocated logical bath inputs exactly one
forward collision, with its output restored to that same memory vertex.
GET and PUT are transports of that one state through a reusable bus,
not fresh bath copies. Already used and not-yet-used bath ports have
identity coupling whenever their address does not match b. During
**every microtick** from preparation completion through the read window,
all commands have a non-COLLIDE opcode. Their beta selectors and bath
gates are identity. Spent baths are therefore a dynamically isolated
reference throughout the inherited comparison. No control, context or
stopping rule depends on their values. They are intentionally revisited
only in the later inverse tail.

No primitive copies source label y, pointer parity, archive flag or bath
value into the classical head-control fields or invocation metadata.
Source packets are relocated to a bus and
returned, not copied. On the admitted program, head/metadata evolution
depends only on initialized commands and counters; it is identical for
all four source labels and their matrix units. The required equality
retains the resulting within-HIGH off-diagonal terms and all bus
correlations. A claim based only on final pointer populations fails.

Resources of this model are finite but need not be practical:

| Item | Exact count or scope |
|---|---|
| Inherited C registers | T packets, one latch, m pointers, K flags |
| P baths | B=L sum_i n_i independent pure zero inputs; all B outputs retained |
| Metadata | K words of ewidth+cwidth+1 bits |
| Program/descriptor | S words of v bits plus the declared finite descriptor word Theta, initialized basis data |
| Mobile head | one rail position, listed finite control registers and eight bus roles (X,Y,P0,P1,l0,z0,beta,mu0) |
| Address mechanism | g actual GET ports and their reverse PUT ports; S actual fetch/unfetch pairs |
| Graph | d rail stations and one vertex per actual stationary memory register; degree at most four |
| Useful time | H*d abstract microticks, followed by W*d data-read ticks |
| Full return | S*d abstract microticks under unmeasured coherent continuation |
| Controller/bus purity | listed classical program/control/metadata initialization; arbitrary bus joint state is allowed |
| Context/pulse/phase | specified exact local gate catalogue and P/C couplings; implementation remains supplied |

For the bare energy extension give every added finite register a fixed
unit level independent of its value, except the latch bus has energy
2*l0. Give each packet bus energy b+H(y)+r as in C. The constant sum of
the finite-register levels is denoted C_fin and explicitly counts all
B baths, K metadata words, S program words, head position and the
finite head registers other than l0. With one unit per finite word
register (not per bit), the ten finite head control registers are
pc,q,a,e,b,f_A,f_B,I,C,run; the five other flat head registers are
P0,P1,z0,beta,mu0. Including head position and Theta therefore gives
C_fin=B+K+S+17. The descriptor's isolated vertex is included in storage.
Then

```text
E_ext = E_C + E_packet(X)+E_packet(Y)+2*l0 + C_fin.
```

Pointer/latch/packet swaps exchange equal assigned spectra; receiver G
preserves packet reserve plus latch energy; shell context gates preserve
H; all other affected levels are flat. The proposed proof must establish
commutation on the whole carrier, including dirty buses. This selected
ledger is not measured drive work, an SI dictionary or a justification
of high-dimensional port hardware. For fixed capacities its finite-energy
subspaces are finite, but no finite order of arbitrary context gates is
deduced from that fact.

The fixed F removes external **runtime instruction/address scheduling**
in this discrete model. It does not derive a physical tick, autonomous
continuous-time Hamiltonian, phase reference, pulse generator or the
initial program. Realizing the port/reflection/context gates by externally
shaped pulses would retain those physical pulse controls as boundary
inputs. Their numbers stored in a program are not a drive derivation.

## 8. Exact control and composed preparation theorem to prove

For each admitted classical program/control start and every complete
data/bus/reference operator X, the command-boundary internal map must
equal the corresponding external primitive program on the data, the
specified metadata extension, and identity on buses, with deterministic
classical head-control/program factors retained. Here 'head-control'
excludes the eight bus factors: their possibly correlated state is
retained inside X and is not replaced by a deterministic factor.
This includes dirty data/buses and all
matrix units; P/C's positive semantics add their separate ready-domain
conditions. The equality extends to trace-class operators by continuity
and to finite reference amplifications. The inverse and partial-station
identities supply the all-step statement, not an endpoint simulation.

The resulting **control error is exactly zero** in the metric of the
complete trace-distance output comparison, uniformly over admitted
inputs and finite references, if and only if this operator equality is
proved. A successful finite test alone cannot set the error to zero.

At B*d the original P theorem, enlarged with the restored buses and
deterministic controller as retained factors, gives

```text
r_L=1-4/L^3;
delta=min(1, sum_i r_L^(n_i)*(1-F_(i,0)));
epsilon_prep=min(1, sqrt(delta)+delta/2);
D(rho_QZ', P_E^(tensor m) tensor rho_Z') <= epsilon_prep.
```

Z' is the **actual** output remainder, including every spent bath,
source/reference, buses and controller/metadata. Its internal correlations
are retained. The proof of the internal measurement implementation must
show that its extension of C is one common CPTP map on these two inputs,
identity on baths, with deterministic outcome-independent controller
metadata and no hidden fine-label record. This places it within P's
contract after an explicit new controller-extension argument.

Hence at the final read window, and at every named completed-round prefix,
the complete actual finite-device/ideal-C output distance is at most
epsilon_prep. It is not multiplied by h. The same bound holds after a
complete declared parity read of all records, retaining every branch,
all flags/metadata and any unused cells. Thus formal finite-device versus
ideal-C trace distributions have TV<=epsilon_prep and prefix errors
<=epsilon_prep. For p_w,q_w>0 the admitted sufficient normalized-branch
bound is min(1,2*epsilon_prep/min(p_w,q_w)); for q_w=0 retain the actual
branch of weight at most epsilon_prep, without inventing a normalized
ideal branch. Source/context approximations are not included: all their
primitives here are exact hypotheses.

For repeated contexts the ideal C projector products allow only constant
LOW/HIGH words. Approximate finite preparation can give other words;
they remain in the compared output. Changed contexts use the ordered
complete post-state maps, not independent scalar draws. Keeping the
same source is essential. There is no claim of independent fresh trials.

No actual-history law is defined in this candidate. In particular
epsilon_occurrence is **undefined, not zero**. The above two formal
operator laws cannot be identified with an actual-history measure by
definition. A separate occurrence proposal would have to provide its
own actual-state/record map and independent measure or frequency theorem.
No L1-to-L5 or L5-to-L6 physical gate is claimed or modified here.

## 9. Finite exact audit domain and execution envelope

The author audit will be newly written standard-library Python with
integer/Fraction arithmetic; no imports of predecessor/reviewer code,
randomness, floating point, network, runtime source files or target-fit
search. Its purpose is to audit the following frozen finite domains.
The universal theorem is a separate proof obligation, not extrapolation.
An independent reviewer chooses and freezes its own exact audit from
this same public specification before exposure to author sources.

1. **Compiler/resource audit at the actual L=613.** N in {2,3,4}, K in
   {0,1,2,3}, h in {0,...,K}, n_i one of all zero, all one, or i mod2,
   W in {1,2}, contexts k_t=t mod2. These are 180 labeled descriptors,
   including coincident small descriptors. Verify the literal emitted
   words, inverse tail, unique ordered bath addresses, cursor-selected
   archive cells, all timing/resource formulas and empty/capacity cases.
   This is finite symbolic compilation, not a trajectory of a sufficient
   large preparation bound.
2. **Local update/inverse audit.** Device parameter tuples (N,K,B,S,L)
   are (2,0,0,1,3), (2,1,2,2,3), (3,2,3,3,5), and (2,2,3,3,613),
   with the two-entry rational catalogue in item 4. Use every rail
   station, every pc, every fixture f=0,...,4 from the explicit rule
   below, both polarities and the twelve-word inventory O:
   NOP, OPEN(0), CLOSE(1), CTX_PLUS, CTX_MINUS, RECEIVER,
   PACKET_SWAP(0,T-1), COLLIDE(0,0), COLLIDE(K,L-1), APPEND,
   opcode 15, and invalid PACKET_SWAP(0,0). All unmentioned instruction
   arguments are zero. Set q to the selected word/polarity. Program
   word A_t is O_((t+f) mod12), with inverse bit (t+f) mod2.
   Check F^-1 F and F F^-1 on the full basis state with exact sparse
   amplitudes. Exhausted cursors, dirty scratch/data/buses and invalid
   fields are included, not filtered. This is not exhaustive enumeration
   of the countable packet carrier.
3. **Addressed command equality.** Use actual L=613, N=3,K=2,B=3,S=1,
   the same catalogue, q=0,pc=0,head position zero and program A_0
   equal to the chosen command. The forty command/cursor instances are:
   NOP; OPEN(k),CLOSE(k) for k=0,1; CTX_PLUS,CTX_MINUS; RECEIVER;
   every PACKET_SWAP(x,y) with 0<=x<y<5; every COLLIDE(i,j) with
   i=0,1,2, j=0,612 and initial b=0,1,2; APPEND with initial a=0,1;
   exhausted COLLIDE(0,0) at b=3; and exhausted APPEND at a=2.
   Their Cartesian products with both polarities, source labels
   f_0,...,f_3, pointer values p=0,1,2,1224,1225, bath bits u=0,1
   and dirty fixtures f=0,1 give 6400 cases. The explicit overrides
   following the fixture rule fix all otherwise ambiguous coordinates.
   Compare the complete fetched-tour result against a separately
   expressed logical target gate and retained head state, including
   restored buses and command adjoints. No data coordinate is dropped.
   For each of the forty forward command/cursor instances also compare
   the correlated vector v_1+(2/3)v_2: v_1 has source f_1, reference 0
   and X-bus packet (0,0,0), while v_2 has source f_2, reference 1 and
   X-bus packet (1,f_3,3); all other coordinates use the same f=0
   command-entry fixture with p=0,u=0. This unnormalized vector and its
   exact outer-product units test retained data/bus/reference coherence;
   there is no irrational normalization or measured sampling step.
4. **Complete finite measurement/control programs.** Rational catalogue
   U_0=I_4 and U_1=H_4/2, where H_4 has rows (1,1,1,1), (1,-1,1,-1),
   (1,1,-1,-1), (1,-1,-1,1). Take N=2,K=2,L=613,n_i=0,W=1 and
   context words empty, (0), (1), (0,0), (1,1), (0,1), (1,0).
   Compare complete internal/external output columns for all four
   source basis states and their sixteen matrix units, using declared
   basis pointer/bus fixtures. Verify metadata, read window, complete
   inverse return and repeated/changed-context order. An additional
   ideal-C calculation on the four-dimensional source and orthogonal
   E/O record symbols checks all formal history branch maps; it is
   explicitly an inherited exact-readiness comparison, not the finite
   n_i=0 device's actual preparation.
5. **Retained finite loader composition.** The labeled toy models use
   N=2,L=3 and a four-source controlled-translation comparison with
   shifts (1,0,2,4) modulo 6, the same rational catalogue, K=1 with
   n=(1,0) and contexts (0),(1), and K=2 with n=(1,0,0) and contexts
   (0,0),(0,1). B=3 throughout. Retain all baths and every amplitude;
   compare the internally executed loader/round maps with the
   separately composed external maps and their inverse. Test a source
   superposition/reference correlation and an initially odd pointer,
   dirty bath and dirty archive flag as negative-domain controls.
   These are finite audits of routing/composition; they do not replace
   the L=613 C receiver or prove P's rate by small-L extrapolation.

The fixed dirty fixture rule for items 2 and 3 is as follows. In C's
field-coordinate chart let Y=(0,f_0,f_1,f_2,f_3,y_bad), where zero is the
stored field tuple (0,0,0,0), the four fields are exactly C's source
labels, and y_bad=(0,0,4,0) has H=16. Packet address v contains
((v+f) mod2, Y_((v+f) mod6), (v+2f) mod4). The stationary latch is
f mod2, pointer i is (2i+f) mod(2L), flag t is (t+f) mod2, bath u
is (u+f) mod2, and metadata t has binary fields
((t+f) mod2^ewidth, (t+2f) mod2^cwidth, (t+f) mod2).
The buses are

```text
X=(f mod2,Y_(f mod6),f mod4),
Ybus=((f+1) mod2,Y_((f+3) mod6),(f+2) mod4),
P0=f mod(2L), P1=(2L-1-f) mod(2L),
l0=(f+1) mod2, z0=f mod2, beta=(f+1) mod2,
mu0=all-one bits for odd f, all-zero bits for even f.
```

Head a=f mod(K+1), b=f mod(B+1), e=(f+1) mod(K+1),
f_A=f mod(S+1), f_B=(f+2) mod(S+1), I=f mod2^ewidth,
C=f mod2^cwidth and run=f mod2. The descriptor word is an unchanged
all-zero test value. Items 2 and 3 replace position/pc/q/program by
their explicitly stated values. Item 3 additionally overrides any
listed command cursor; puts the selected source field with b=1,r=2
in the receiver for RECEIVER, packet x for PACKET_SWAP, and C_0
otherwise; replaces pointer i for COLLIDE or active pointer otherwise
by its selected p; and sets bath b to its selected u when b<B, or bath
0 when b=B. All unspecified coordinates follow the rule. At L=3,5
the item-2 receiver uses C's same support/funding/code formula with
pointer addition modulo 2L solely as a labeled inverse audit model;
no small-L C classification is inferred.

For item 4, both full-program fixtures use C's clean single-packet
geometry, zero flags and metadata, the admitted initialized controller,
and no baths. The first has pointer tuple (0,0,0) and all bus fields
zero/empty. The second has pointer tuple (0,2,4) and the f=1 bus values
above. Every source basis label is used in both. The ideal-C symbolic
history calculation uses these same context words with the exact E
bank as a **separate** comparison input, checks all 16 source units and
all 2^h parity histories, and retains ordered source post-state blocks.

For item 5 the positive toy input has every pointer/bus blank, zero
flags/metadata, three zero baths and clean transport geometry. Use all
four source basis columns and the reference vector
|f_1,0_R>+(2/3)|f_2,1_R>. The three negative-domain variants, each
with the same reference vector, change respectively the active pointer
to |1>, bath 0 to |1>, or archive flag 0 to one. Other fields remain
the same. For this toy only the supported four labels are translated
by the stated shifts (1,0,2,4) modulo 6; their same funded WRITE and
RELEASE branches and inverse are used with the unchanged packet route.
These variants must retain and invert the full output; no positive
readiness or exact-repeatability promise is imposed on them.

The implementation may coalesce a sequence of **proved identity station
gates** for sparse trajectory efficiency only if it explicitly computes
the traversed head positions/tick count and checks that no selected port,
processor or counter update is skipped. The station/inverse audit and
paper all-step proof remain mandatory. No endpoint oracle may stand in
for executing the addressed swaps and decoded primitive.

The full source pin may spell out encoding functions and exact output
counts but may not change the domains or claims above after this
specification is publicly frozen. Predicted success,
stdout, fitted tolerances or performance observations are not inputs.
The local first run envelope is 120 seconds under a deterministic
environment (LC_ALL=C, LANG=C, TZ=UTC, PYTHONHASHSEED=0,
PYTHONDONTWRITEBYTECODE=1). Actual exit, stderr, stdout byte count/hash
and environment are recorded afterward, with no post-pin source repair
or unreported rerun. Existing unchanged repository runners must replay
the exact frozen verifier against its own captured EXPECTED on x86_64
and aarch64 before that computation gate is claimed.

## 10. Falsifiers, acceptance and surviving assumptions

F1 fires for a failure of the total local inverse, an unlisted register,
nonlocal operand access at the declared graph scope, unretained workspace,
or a physical/local-alphabet assertion stronger than the model.

F2 fires if fetch/unfetch, operand routing, inverse address recovery or
counter arithmetic fails the complete command operator equality; or if
the program is really a desired-output lookup rather than operation data.

F3 fires if a supported bath input is reused, a spent bath is touched or
consulted during any forward C microtick/read window, an archive address
is not selected by retained state, or invocation/context provenance is
claimed from a dirty flag outside the proved domain.

F4 fires for an incorrect compiler/timing/resource formula, an omitted
microstep, an absorbing reversible halt, false full return after an
unretained external measurement, or a hidden source renewal.

F5 fires if any source/reference/bus matrix unit, within-HIGH coherence,
changed-context continuation or outcome-dependent controller remainder
breaks the claimed complete-map equality.

F6 fires if the new controller extension fails P's untouched-bath joint
contract, if the actual remainder is replaced by fresh independent data,
if epsilon is multiplied per trial without cause or omitted, or if
rare/ideal-zero branches are dropped or overclaimed.

F7 fires for a claimed native realization, physical clock/work closure,
exact finite E from the forbidden dyadic slice, actual outcome/measure,
empirical result, physical apparatus completeness or Canon promotion
without its separate evidence and named gates.

Acceptance requires independent theorem-grade review of F1-F7, exact
finite audits with immutable public custody and actual two-architecture
replay. A failed local model receives its precise scoped disposition;
it is not a general impossibility theorem about autonomous control or
deterministic measurement.

The intended one-page accounting summary is:

| Runtime input removed at this conditional scope | Retained premise |
|---|---|
| Per-command external fetch and dispatch | initialized finite program, graph and head entry state |
| External choice of next pointer/bath address | encoded pointer/edge arguments, actual retained bath cursor, supplied fresh pure bath bank |
| External next archive selection | actual retained archive cursor and initial zero flags/metadata |
| External invocation/context bookkeeping | supplied context sequence, initialized epoch and scratch; actual reversible OPEN/APPEND/CLOSE storage |
| Runtime round/tour scheduling and finite read-window placement | fixed discrete F, exact local gates and a supplied physical realization/tick if one is requested |
| Exact external orchestration of the P/C composition | existing complex formalism, exact catalogue/phase/pulses, source preparation and C/P positive domain |
| None for realized single outcomes | occurrence map and independent measure/frequency law remain open |

This candidate is a complete finite conditional internal-control law if
proved. It does not change the decision conditions of
QDD-INSTRUMENT-APPARATUS, QDD-TERMINAL-EVENT-SEMANTICS or
QDD-INSTRUMENT-CLASS-COMPLETENESS.
