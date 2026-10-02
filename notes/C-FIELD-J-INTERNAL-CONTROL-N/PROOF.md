# Complete fetched control on the retained preparation carrier

**PUBLIC, NON-CANONICAL. Conditional L1 author-side proof. No independent
acceptance or scientific execution is asserted here.** Original work,
Apache-2.0. Owner: A. M. Thorn. The coordinator wrote this proof alongside
control_builder's separate author implementation. Coordinator design and
control_ownership's receiving-contract assistance are disclosed coauthorship,
not independent review. The known target and public construction are exposed.

The immutable specification and its occurrence-interface annex are at
`e5ff31fd7296df4bf740fd27c1ac3de14b5c8148`. Their SHA-256 values are
`ebc473f087158e382fbf4864b4f20676848b1c04821dbaafba53adfffd3ea40f` and
`64277d3cd9389584e8a32ec0d7d80589c9f83d46a2b466c2464a7ee83777ae91`.
The exact admitted C reference is
`024936502544c2ec45acc8890a052c7b3aca26be`; the admitted P reference is
`1f88665ce8646cdf134cb4366958db0ca2d302d7`. The earlier classical
moving-head result at `fd792d32b3efa90c15a46e065d6637ac8600cdcf`,
`notes/C-J-LOCAL-RAMIFIED-MEMORY-N/PROOF.md` section 8, is acknowledged.
The new claim concerns fetched data instructions, retained operand access
and this complete quantum preparation/measurement composition.

## 1. Carrier and meaning of the theorem

Fix N>=2, K>=0, L>=3, T=2N-1 and m=K+1. The receiving C application has
L=613. Choose finite loading counts n_i>=0, B=L sum_i n_i, h<=K supplied
contexts from a finite declared unitary catalogue, and W>=1. Put

```text
H = B + h(2T^2+5),       S = 2H+W,
g = 4N+4K+B+1,          d = 2S+2g+4.
```

The proof uses exactly the tensor factors and alphabets of PREREG sections
2-4: inherited C registers, B bath bits, K metadata words, S program words,
the immutable descriptor Theta, one head position in Z_d, the listed head
controls and all eight operand buses. The reference is arbitrary finite.
No factor is traced out in the control equality. Metadata is part of data;
the operand buses are separate retained quantum factors. Packet factors
have basis {0,1} x Z^4 x N_0. Finite words, counters and flags have their
literal stated alphabets, including invalid instruction bit patterns.

There is exactly one head by definition of the carrier. This is not an
acceptance test on an unspecified multihead system. For locality, embed its
position/internal tensor product into the direct sum of one-head sectors
on the rail: at position s the internal head state is located at s and all
other rail sites are vacant. This embedding moves the complete head cargo,
including quantum buses. It does not clone a common bus at every site.
No multihead dynamics or uniform finite local dimension is asserted.

Equality is equality of complete joint operator maps under the fixed
coordinate identification. The state description is category 2: a vector
or density on this complex extension. It is not a native integer-state
realization or a map choosing an actual LOW/HIGH word.

The programme/catalogue/graph and initialized control conditions are
hypotheses. For useful C semantics, source and geometry, even-supported
pointers, independent zero baths, zero flags and metadata, and the P/C
coupling assumptions are additional hypotheses. The local update below
nevertheless exists on every state of the declared Hilbert space.

## 2. Every station has an all-state inverse

We first establish unitarity independently of useful initialization.
For an unchanged classical-basis control register c and unitary blocks
V_c, the operator sum_c |c><c| tensor V_c is unitary: multiplying by
its adjoint removes cross terms and gives sum_c |c><c| tensor I. This
holds for coherent or entangled controls and does not measure them.

**Fetch.** At a program port t the map q -> q XOR A_t when pc=t is an
involution on every basis value. Both pc and A_t remain unchanged.
Consequently it is a unitary on coherent program/scratch states. The
UNFETCH operation is the same involution, with the same retained word.
ADVANCE-PC is a cyclic increment with the cyclic decrement as inverse.

**Operand access.** Every GET/PUT is a SWAP between equal typed factors,
controlled only by unchanged q,a,b. Its selector is a fixed function of
these local head registers and the adjacent port label. It is a direct
sum of identity and SWAP, hence an involution. No exchanged payload,
unknown readiness or quantum parity is used to select the port.

**Collision.** In the pointer/bath space the specified vector nu_j is
normalized: d_j,s_j are orthonormal, as are the bath bits. Therefore
P_nu^2=P_nu=P_nu^*, and (I-2P_nu)^2=I. This is a total Hermitian
unitary, with identity action on odd pointers. The proof does not require
a fresh bath. Freshness is needed only for the P preparation theorem.

**Context.** Each catalogue member is unitary on the four H=1 source
labels and identity on the complementary labels, as specified by C.
Its extension acts separately at each reserve on present packets, and
as identity elsewhere. This orthogonal direct sum is unitary on the
whole packet bus. Invalid active context codes act as identity. CTX_MINUS
uses the adjoint; toggling a command's inverse bit takes its adjoint again.

**Receiver.** C proves G is a total basis permutation, including absent,
unsupported, underfunded and occupied-latch inputs. Explicitly, for a
supported packet with unchanged b,y and code c(y), its nontrivial branches
are (r,0,p)->(r-2,1,p+c) for r>=2 and (r,1,p)->(r+2,0,p).
For an output with latch one the inverse is (r+2,0,p-c); for latch zero
and r>=2 it is (r-2,1,p); underfunded latch-zero states are fixed.
Unsupported packets are fixed. These classes are exhaustive and disjoint.
Thus the complex basis lift is unitary. G is not substituted for G^-1.

PACKET_SWAP is an ordinary SWAP. OPEN and CLOSE each XOR I with binary(e),
C with binary(k), and run with one, leaving e,k unchanged at EXEC. Each is
an involution at fixed e,k. For a<K, APPEND is the commuting product of a
pointer SWAP, flag X, and metadata XOR by (I,C,1), with all its controls
unchanged. It is an involution at EXEC. At a=K its data gate is identity.
All invalid words decode to the explicitly prescribed identity operation.
Their actual stored bits remain; decoding is not an erasure of the word.

**Address and epoch changes.** For COLLIDE, on (b,f_B) the head-only map is

```text
(b,f) -> (b+1 mod(B+1), f+[b=B] mod(S+1)).
```

Given (b',f'), recover b=b'-1 modulo B+1 and f=f'-[b=B] modulo S+1.
This is a bijection, including B=0. The same argument applies to APPEND
with a,K,f_A. CLOSE is a cyclic epoch increment. Other commands leave
these registers unchanged. Opcode/arguments, the controls for these maps,
are not changed. Thus the opcode-controlled A_o and A_o^-1 are total
unitaries. Inverse commands apply A_o^-1 at PRE; forward commands apply
A_o at POST. There is no conditional one-sided append with an unproved
inverse and no sticky irreversible error bit.

This proves that every station J_s has the indicated adjoint on all
states, including arbitrary scratch, buses and program superpositions.
The immutable descriptor is tensored with identity throughout.

## 3. Fixed update, inverse and the claimed locality

Let U_J=sum_s |s><s| tensor J_s and let P_shift|s>=|s+1> on Z_d. Then
F=(P_shift tensor I)U_J. U_J is a unitary direct sum by section 2 and
P_shift is a permutation. Hence

```text
F^-1 = sum_s |s><s+1| tensor J_s^*.
```

Multiplying in either order gives identity. The formulas act on coherent
head positions without selecting one position. Packet factors may be
countable: a basis permutation is an isometry on finite sums and extends
to a surjective unitary, and the specified bounded unitary blocks/direct
sums have their ordinary Hilbert-space extensions. Operator identities
extend from finite-rank matrix units to trace-class operators by trace-norm
continuity, with arbitrary finite reference amplification.

At a port, J_s uses the head cargo at s and one adjacent memory vertex.
At a processor station it uses only cargo at s. Afterwards the head moves
along one rail edge, carrying its complete state. In the one-head embedding,
the port interaction has radius one and interaction plus motion has a
conservative radius two. The reverse motion followed by the inverse port
gate has the same bound. This is a statement about this explicit graph
and one-head carrier, not a full multihead QCA or native-U theorem.

One stationary register is attached to each of its named access stations;
repeated visits are not multiple copies. Packets have two bus lanes with
GET and PUT, thus at most four incident port edges. Pointers likewise have
at most four; other accessed memories have at most two. Each rail station
has two rail neighbours and at most one memory edge. Theta is isolated.
The maximum degree is therefore four. Address comparisons and word XORs
act on the stated finite words; the packet alphabet is countable and
local dimensions grow with the selected capacities. No bit-level physical
implementation or fixed alphabet independent of those capacities is
inferred from graph radius.

The machine has actual sequential access cost: it visits S fetch ports
and g operand ports, then their reverse counterparts, with four processor
stations. It does not use a free nonlocal memory lookup or a map from a
whole initial state to the desired final history. For fixed capacities
and catalogue, changing the initialized tape changes data, not F.

## 4. Exact routing lemma, including arbitrary correlated buses

Fix one fetched basis word and fixed selector values. For each selected
role, the port table names one stationary operand and its corresponding
bus. Valid PACKET_SWAP targets are distinct; APPEND uses pointers 0 and
a+1 with a<K; other multiple operands have different types. Thus on the
useful address domain these exchanges pair distinct memory factors with
distinct buses. Each pair has the same Hilbert-space type.

Let R_o be their actual GET product in rail order. The reverse PUT order
is exactly R_o^-1. If V is a unitary on the selected buses, conjugating
by these SWAPs gives

```text
R_o^-1 V_buses R_o = V_named-memory tensor I_buses.
```

To prove this, act on an elementary tensor of all memory and bus basis
vectors: GET exchanges their positions, V acts on the transported memory
values, and PUT restores the original bus values and sends V's outputs to
the named memories. Multilinearity proves the vector identity, including
every coefficient and phase. Density-matrix or reference factorization
is not an assumption: operator equality implies its action on arbitrary
entangled, mixed and dirty inputs. In particular, it is false that these
reusable buses require a fresh pure state for each instruction.

APPEND's metadata gate also has unchanged I,C controls in the head; apply
the same tensor argument in each control block. OPEN/CLOSE have no GET
operands. Invalid words have none. For an exhausted COLLIDE or APPEND,
the declared partial extraction is followed by identity V, so PUT exactly
undoes GET. Their data action is identity even on arbitrary buses.

No conclusion here erases an old bath output. Routing exchanges an entire
retained quantum state; applying U_j to the transported selected bath and
then restoring it applies U_j to that one logical bath coordinate.

## 5. Command inverse and fetched-word equality

All GET selectors depend only on q,a,b. EXEC leaves a,b unchanged. OPEN
and CLOSE change I,C,run but have no routed operands. All other EXEC
gates leave the selector fields unchanged. PUT therefore applies the
inverse of the actual GET product, not a guessed recomputation from a
changed payload or target flag.

With composition read right to left, a positive command is

```text
M_(o,+) = A_o R_o^-1 V_o R_o.
```

Its actual inverse command first applies A_o^-1, thereby recovering the
old cursor/epoch values, and then performs GET, V_o^*, PUT at those
recovered values. As an operator this is

```text
M_(o,-) = R_o^-1 V_o^* R_o A_o^-1 = M_(o,+)^-1.
```

This proof does not commute A_o past a cursor-dependent R_o or an
epoch-dependent OPEN/CLOSE. In particular, moving inverse cursor recovery
to POST would generally use the wrong bath/archive cell. The specified
PRE placement is essential. The same reasoning holds when a forward
command is exhausted or has an invalid word: all its defined factors
are inverted, including cyclic cursors and modular failure updates.

At a command-entry section, take position zero, q=0, and a specified
basis program with current pc=t. During FETCH exactly one equality pc=t
is true, so q becomes the actual stored word A_t. Neither the program nor
pc changes before UNFETCH. None of PRE, GET, EXEC, PUT, POST changes q.
UNFETCH visits the same A_t and returns q to zero; ADVANCE-PC increments
pc once. A complete d-tick tour therefore implements M_(A_t) with all
controller fields retained. Fetching is a real reversible word operation,
not an assumption that an external agent supplies the instruction.

For a basis initialized program and classical head controls, the control
trajectory is independent of all data values. Every control update uses
only those controls and program values; no operand is copied into them.
This remains true for arbitrary entangled buses and metadata. The latter
are quantum data, not part of the asserted deterministic control factor.
Consequently, at every completed command there is a deterministic
classical control state gamma_j and an external logical data unitary E_j
such that, for every complete data/bus/reference operator X,

```text
Ad(F^(jd)) ( |gamma_0><gamma_0| tensor X )
 = |gamma_j><gamma_j| tensor
   (E_j tensor I_buses,R) X (E_j^* tensor I_buses,R).
```

Here gamma includes the fixed program/descriptor, rail position, pc,
scratch and classical head controls; metadata remains in X. E_j is the
chronological product of the explicitly addressed external primitives
and the stated metadata XORs at their actual counter values. This is an
all-matrix-unit equality, not a reduced pointer-population identity.

For intermediate tick jd+r, 0<=r<d, use the actual ordered prefix of the
next r station gates and shifts. Its classical controls are still
deterministic. Its data/bus part is a known unitary R_(j,r), giving the
same formula with R_(j,r)(E_j tensor I) in place of E_j tensor I.
This supplies every microscopic step and its inverse. A transported
source/pointer is on its bus during that prefix, not silently left at
its old inherited coordinate.

## 6. Compiler correctness and exact timing

The initial loader emits exactly B COLLIDE commands in the stated order
(pointer, sweep, edge). With b=0 initially, its t-th command has b=t,
for 0<=t<B, and selects the unique bath address t. Its postincrement
gives t+1 without wrap. Thus it applies exactly P's ordered full unitary
W_P to the bank and its B retained baths. Metadata, source and other
data are untouched at these command boundaries. Arbitrary bus correlations
are restored by section 4. After loading b=B and f_B=0; no failed
request is inferred from the bank being completely consumed.

One C transport step is receiver G followed by N-1 disjoint A swaps
and N-1 disjoint B swaps. Serializing each matching in the specified
order leaves its operator unchanged because disjoint-factor swaps
commute. This uses 1+2(N-1)=T commands. Exactly 2T inherited steps cost
2T^2 commands and implement the entire C unitary U_F^(2T), on dirty
as well as clean data. The pre/post source controls add two commands;
OPEN, APPEND and CLOSE add three. Each round therefore has exactly
2T^2+5 commands and the full useful word has H as stated.

Let a_t=B+t(2T^2+5) be the command index at the start of round t.
OPEN ends at (a_t+1)d and CTX_PLUS at (a_t+2)d. Transport step s ends
at (a_t+2+sT)d, for 1<=s<=2T. Its receiver command ends at
(a_t+2+(s-1)T+1)d, preceding its step boundary by T-1 commands.
Inside that receiver command, the G transition itself completes at
the command-entry tick plus S+g+2: S FETCH ticks, one PRE, g GET ticks
and one EXEC. These equations account for the actual head transitions.
They do not assign a physical duration or identify a routed microtick
with an inherited B macrostep.

The admitted C timing theorem applies at the corresponding logical
transport boundaries. On its clean source/geometry domain WRITE is
the funded receiver reaction at s=N, and RELEASE at s=N+T. All source
components have the same geometry/funding timing. Their field labels
and coherent amplitudes are not an extra controller input. After 2T
steps the operative geometry is restored, as required for the next
round. The source state is retained with its actual post-state and
correlations; a geometry return is not source renewal.

## 7. Actual cursor allocation and metadata provenance

Initially a=e=0 and I=C=run=0. Induct on the round number t<h<=K.
Assume a=e=t at its start, earlier flags and metadata have the values
already written, and untouched later flags/metadata are zero.
OPEN(k_t) uses the current epoch to produce I=t,C=k_t,run=1. These
values stay unchanged through source controls and transport. APPEND
uses the **current a=t** to fetch archive pointer t+1, flag t and
metadata t. No archive-address argument on the tape replaces this
cursor selection.

Because the loader does not alter flags/metadata and earlier appends
addressed only u<t, this selected flag is actually zero on the supported
domain. The append swaps the complete active pointer with that stored
pointer, sets its flag to one and writes (t,k_t,1) by XOR into zero
metadata. The old pointer and all its correlations are retained. The
archive postincrement gives a=t+1. CLOSE at the still-current e=t
XORs the same invocation/context fields away, sets run back to zero
and then gives e=t+1. The induction is proved.

This is a provenance theorem on the initialized supported protocol,
not a universal interpretation of a flag or metadata word. Dirty flags
are toggled, dirty metadata is XORed, and unknown pointers are exchanged
by exactly the same total map. None is projected to a fresh state.
For first invocation t=0 and context zero, the appended metadata bit
still distinguishes the written header from its zero initialization.

There are at most K supported appended records. At h=K the last
successful append leaves a=K and f_A=0. Completion is not a capacity
error. A further forward APPEND at that cursor performs identity on
data, adds one to f_A and cycles a to zero. Its exact inverse recovers
the prior cursor and subtracts that increment. COLLIDE behaves analogously
at b=B. Subsequent arbitrary raw commands can revisit used resources;
the once-only guarantee belongs to the compiled useful word, not every
possible tape. The failure fields are modular values, not permanent
overflow protection. On a forward-polarity prefix from zero of length
at most S, they equal nonnegative failure counts because their modulus
is S+1. No such count interpretation is made for mixed/inverse programs.

The receiving annex therefore separates formal-history applicability
from raw capacity diagnosis. Missing purity/coherence promises are not
detected by this machine. A coherent control state has its total unitary
evolution without being assigned a hidden single classical chronology.

## 8. Read window, lifetime and complete continuation

The useful word is followed by W encoded NOPs and then the same useful
word in reverse order with every inverse bit toggled. The NOPs have
identity data/counter operations. During every tick of

```text
H*d <= tau < (H+W)*d
```

no data-memory GET/PUT or EXEC changes memory. Fetch/clock motion still
occurs. Thus the promised finite read window has W*d abstract ticks;
the controller has not entered an absorbing halt. Earlier archives
were also untouched by later useful rounds, because their addresses
were never selected again.

Section 5 proves each inverted word is the inverse of its original
complete command, with counter recovery in the right order. Induction
through the inverse tail cancels the H command maps in reverse order.
At S*d the data, buses and metadata are exactly their initial joint
state, all classical controls are restored, pc has completed its cyclic
traversal and position/scratch are zero. The stationary program and
descriptor never changed. This return holds for arbitrary data/bus
operators at the admitted controller start; it does not require that
the data were in the positive preparation slice.

The useful programme repeats under continued F iteration after that
return. Its finite invocation fields do not remember an unbounded
number of cycles. The return theorem concerns the unmeasured coherent
closed state. If an external read apparatus is coupled and then omitted,
the displayed inverse need not restore that altered state. In particular,
formal parity dephasing is not quietly inserted into the unitary lifecycle.

## 9. Bath isolation and absence of a fine-label controller record

By section 6, each declared fresh logical bath participates once in the
loader, with its entire output returned to its memory vertex. Already
spent cells and future cells have identity gates whenever their address
does not match. This is a statement about individual addressed gates,
not only a coincidence of final bath marginals.

Every command after preparation and through the read window is a
non-COLLIDE word. At all its GET/PUT ports the beta/bath selector is
false, and its EXEC gate does not act on bath memory or beta. Therefore
every individual microtick acts as identity on all stationary spent
bath factors. Neither context nor a cursor/clock transition reads their
values. The inverse tail intentionally revisits them only after the
comparison interval ends.

Payloads can temporarily occupy the quantum buses. They are not copied
into pc,q,a,b,e,I,C,run or failure counters. Program contents alone
determine these classical fields. APPEND's header contains invocation,
context and its appended marker; it contains no source label, pointer
position or parity. At each command boundary all bus factors are
restored jointly. Thus there is no hidden fine-label control record.

In particular, section 5 applies to |f_j><f_k| for every j,k in the
four-source code and to its arbitrary pointer/reference/bus blocks.
For j,k within HIGH the same exact external C block is retained, not
just the same diagonal population. Approximate readiness can still
alter the finite device's coherence as P quantifies; the controller
adds no extra such change at the stated comparison boundaries.

## 10. Complete preparation/error comparison

At the B*d boundary the logical map is exactly W_P on bank/baths and
identity on every other data/bus coordinate, together with deterministic
classical controller values. Hence P's joint preparation theorem applies
with all restored buses, source/reference and controller/metadata
included in the remainder Z'. For the selected finite bank Q,

```text
r_L = 1-4/L^3,
delta = min(1, sum_i r_L^(n_i)(1-F_(i,0))),
epsilon_prep = min(1, sqrt(delta)+delta/2),
D(rho_QZ', P_E^(tensor m) tensor rho_Z') <= epsilon_prep.
```

The remainder is the actual marginal of this output. It can contain
source/bath/bus correlations and information originally in the pointers.
It is not replaced by independently refreshed data. P's argument uses
finite bank projections and trace-norm inequalities and is stable under
adjoining untouched reference factors. If new countable packet-bus factors
are not included in a finite-reference formulation, apply its uniform
bound on finite-dimensional approximations and pass to the trace-class
limit. Partial trace, unitary conjugation and the finite bank projections
are continuous in that norm. This gives the same inequality without an
unannounced bus-independence or bus-purity assumption.

Apply the same subsequent internal unitary to the actual and comparison
states. It preserves their trace distance exactly. Section 9 shows that
its spent-bath factors remain spectators at every microtick. At completed
round boundaries, section 5 identifies it with the same admitted
nonadaptive C protocol, tensored with identity on buses and the specified
outcome-independent metadata/controller extension. On the ideal E bank
this is precisely C's complete coherent history operator, with arbitrary
retained reference including Z' correlations. This proves the new
controller-extension obligation instead of assuming its admission.

Consequently the complete internal finite-device output and its identified
ideal-C output differ by at most epsilon_prep at every completed-round
boundary and the final read window. Intermediate ticks can be compared
under their explicit partial-routing embedding with the same bound. No
factor proportional to the number of rounds occurs: one common channel
acts on one already bounded pair of joint states.

The control comparison itself has error exactly zero because section 5
is an operator identity on the complete initialized-controller domain,
including arbitrary finite references. Finite tests do not establish
that zero; they audit the independent analytic identity. Exactness of
the local primitive/catalogue gates remains a premise. Extra approximate
pulses, wrong phases, impurity, source/context errors or bath feedback
are not covered by declaring a larger sweep count.

For a formal complete record read, take the direct-sum CP map of the
archive projectors. It retains every branch, flag, metadata field and
unused cell. This is a mathematical reading instrument, not an added
physical selector or an uncounted dynamical apparatus. Trace distance
contracts under that map, and its classical branch traces therefore
have total variation at most epsilon_prep. Each prefix-weight difference
has the same bound. No zero-weight or unfavoured branch is omitted.

For branch operators A,B with positive traces p,q, normalize only when
both are positive. The inherited sufficient estimate is
min(1,2 epsilon_prep/min(p,q)). Its denominators preclude a uniform
rare-branch guarantee without a lower-weight condition. If q=0, the
actual formal weight is at most epsilon_prep but there is no normalized
ideal branch. This error estimate alone does not establish every exact ideal zero.

For reference, with D=I the ideal source branch maps are the ordered
projector products Q_(k_t,o_t)...Q_(k_0,o_0). A repeated context gives
orthogonal complementary projectors, so a change of label makes the
product zero and a constant word leaves its original projector. Different
contexts in general do not commute, so their order and the retained
post-state matter. The same compiler implements both cases; it does
not redraw an independent outcome or replace the source.

### 10a. Pre-execution scope correction: repeated-context parity

The frozen PREREG section 8 says that approximate preparation can give
nonconstant words under a repeated context. For the positive even-supported
D=I subclass actually declared here, that sentence is too broad. A fresh
reviewer's paper pass identified this before either new verifier ran. This
paragraph records the correction; the immutable specification, operational
law, finite audit domains and error threshold are unchanged.

Every preparation collision preserves each pointer's even subspace. In a
clean C round the controlled pointer shift has odd parity exactly on LOW
and even parity on HIGH. Therefore its branch map sends the source into
the corresponding context projector range, even when the pointer and
retained remainder are correlated and the pointer is not E. Translation
operators may still differ between fine labels within HIGH, so this
statement does not give the ideal within-HIGH joint state or its coherence.
After source unrotation, the state is supported in Q_(k,o). With D=I and
the same next context, the next pre-rotation stays in the same bin. Its
fresh logical archive cell supplies another even-supported active pointer;
the second recorded parity is again o. Iteration proves that every
nonconstant word in a run of identical contexts has exactly zero formal
weight in this supported finite device as well as in ideal C.

This is a parity/support invariant, not an assumption that the finite bank
has the ideal E coherence. It needs the declared even support, clean C
geometry and preserved source, exact context operations and D=I. Odd or
otherwise off-domain inputs retain their total reversible evolution but
not this positive statement. Other ideal zero branches, changed-context
continuation and normalized branch-state errors still require the stated
comparison; the general zero-weight error allowance is not replaced by
an unproved equality of full instruments. No realized outcome is selected.

## 11. Exact storage and bare energy account

There are T inherited packet registers, one latch, m pointers and K
archive flags; B stationary baths; K metadata words; S programme words;
one descriptor; and the complete head factors listed in PREREG. Its
eight bus roles are X,Y,P0,P1,l0,z0,beta,mu0. The graph has d rail
vertices and one per actual stationary memory register, including the
isolated descriptor. Every fetch/access port is an edge/visit, not a
new copy of the addressed register. The encoded width of Theta and all
word/counter alphabets are part of the selected finite device.

The number of useful commands, head ticks and full return ticks is H,
H*d and S*d respectively. This includes S-word scans, all operand-port
visits, inverse-address changes and idle turn/processor steps. It is
finite for every finite descriptor. The conservative preparation rate
can require enormous n_i and consequently enormous B, tape and time;
neither laboratory feasibility nor complexity optimality follows.

For the specified bare ledger, assign packet bus energy b+H(y)+r,
latch bus energy 2l0, and fixed unit energy to every other added finite
factor. The fifteen finite head factors excluding position/latch are
pc,q,a,e,b,f_A,f_B,I,C,run,P0,P1,z0,beta,mu0. With position and descriptor
this gives

```text
C_fin = B+K+S+17,
E_ext = E_C + E_packet(X)+E_packet(Y)+2*l0+C_fin.
```

GET/PUT exchange equal energy spectra. Receiver G preserves its reserve
plus twice its latch; contexts preserve H and presence/reserve; collisions,
pointer swaps, word/counter changes and head motion act on flat levels.
Each station and its inverse commute with every spectral projector of
E_ext. Thus F preserves its finite or extended nonnegative expectation.
For fixed capacities, a finite energy bound bounds every reserve and,
by positive definiteness of H, every field coordinate. All other alphabets
are finite, giving finite energy subspaces. Finite dimensionality alone
does not give finite order for arbitrary coherent catalogue gates.

This is a selected mathematical ledger. It accounts for all named
registers under its convention, not for measured drive work, material
hardware cost or an SI realization. The fixed abstract tick and the
exact local couplings are supplied; storing an instruction for a
time-dependent physical pulse does not derive its pulse generator.

## 12. Discharged premise and retained boundary

The proved improvement is internal runtime fetch, operand addressing,
bath/archive allocation, invocation bookkeeping and finite programme
timing on the declared port graph. No external agent chooses the next
instruction after the admitted launch. The initializing programme,
descriptor, catalogue, graph and entry state are still inputs. Source
preparation, phase alignment, bath purity and physical realization of
the primitive interactions/tick remain inputs. Only the declared finite
nonadaptive D=I subclass is claimed; adaptive choices, source replacement
and coherent stopping need their own law and proof.

The one-page removed/retained-premise table in PREREG section 10 applies
without strengthening any entry. The occurrence annex gives a total
typed formal report with raw resource diagnostics, not a realized-event
transducer. At K=0 its report is NO_COMPLETED_ROUND. A ready-domain
promise is never converted into a quantum readiness measurement.

The complete formal state, funded WRITE, archive occupancy and formal
parity projectors do not define one selected actual history. In this
candidate no actual-state preparation measure or frequency theorem is
provided; epsilon_occurrence is undefined. A future independent actual
record law must be compared first with the finite implemented device,
then with the ideal C reference using the present preparation allowance.
The prospective triangle bound in the annex does not fill that missing
law by definition. Failure to supply it here is not a general no-go
theorem for deterministic measurement models.

All statements remain conditional L1 results on the complex extension.
No native-U derivation, physical clock/work conclusion, exact finite E
from the frozen dyadic preparation class, empirical result, physical
apparatus completeness, layer-gate passage or Canon promotion is asserted.
