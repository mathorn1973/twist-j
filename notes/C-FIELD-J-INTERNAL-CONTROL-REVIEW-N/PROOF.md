# Independent derivation of the internal fetched-program law

**PUBLIC, NON-CANONICAL. Independent paper review of the frozen specification;
no scientific execution or earned public status is asserted by this file.**
Original work, Apache-2.0. Prepared 2 October 2026 by `control_breaker`.
The precise public specification, admitted prior pins and exposure boundary
are recorded in the sibling PREREG. This proof was derived without reading
the new author's proof, implementation or output and before any scientific
execution. The model and desired comparison are known, not blinded.

## 1. Meaning of the statement and the inherited input

The complete state is a density/vector on the stated complex tensor product.
All stationary registers, including program and descriptor, the single head
position, ten control fields, eight bus roles, every fresh/spent bath,
invocation metadata and arbitrary finite reference belong to it. A packet
register is countable. The Hilbert space is separable; no finite truncation
of that register defines the all-state theorem.

The universal control conclusion has two different domains. Every station
and F must be unitary on the complete carrier, with arbitrary dirty or
coherent program, scratch and position. The specified primitive-program
interpretation additionally requires a classical initialized program,
head entry section and zero fetch scratch; P/C semantics impose their
separate ready-domain hypotheses. A coherent superposition of programs is
not assigned one classical chronology. It still has F's unitary evolution.

The receiving C proof at its admitted pin supplies the field chart and
positive definite H, support H<=5, exact code c, the total receiver and its
inverse, the packet permutation cycle, the four-label unitary extension and
the exact ready-bank ordered instrument. The receiving P proof at its
admitted pin supplies the local reflection, even-sector fidelity estimate
and joint comparison against the actual remainder. Those are mathematical
inputs, not code dependencies. The older moving-head proof already gave
autonomous mathematical scheduling for a selected classical macro word;
the present additional question is the actual finite fetched data program
and its addressed P/C implementation.

For completeness, C's receiver inverse is essential here. A supported
output with latch1 comes from `(r+2,0,p-c)`; one with latch0 and r>=2
comes from `(r-2,1,p)`; latch0 with r<2 and unsupported outputs are fixed.
These disjoint cases exhaust the carrier. In particular release is not a
negative translation, so G is not its own inverse. The code in this review
uses this distinction on every inverse RECEIVER.

## 2. All-state inverse, locality and energy: F1

At each program port, the word map `(q,A_t)->(q XOR A_t,A_t)` is an
involution, including dirty/coherent q and A_t. Conditioning it on a fixed
pc equality is an orthogonal block sum of involutions. Each data port is
a SWAP of equal spaces, controlled only on fields it does not change.
Thus it is also an orthogonal block sum of involutions; the control is not
measured. A flat invalid instruction decodes to identity without deleting
the stored bits, so all unused bit patterns remain in the carrier.

P's local vector nu has norm one: d and s each have norm one and bath0
and bath1 are orthogonal. Therefore `(I-2|nu><nu|)^2=I`; it is a total
unitary with identity odd sector. C's G is the basis permutation just
described. A context is the direct sum of its chosen U(4), repeated at
each reserve, and identity on all other packet basis labels. The catalogue
is fixed before the program is loaded; this does not program an arbitrary
unknown unitary with a finite instruction word.

OPEN/CLOSE XOR I by the retained e, XOR C by the fixed argument k and
flip run. They leave e unchanged at EXEC and are involutions there.
APPEND on a<K consists of a pointer SWAP, flag XOR and metadata XOR by
`(I,C,1)`, all on distinct targets with unchanged controls. Those commute
and are involutions. On a=K its data gate is identity. Every EXEC is
therefore unitary, including coherent counter controls.

For a capacity D with cursor t in Z_(D+1) and failure f in Z_(S+1), the
counter bijection is

```text
(t,f) -> (t+1 mod(D+1), f+[t=D] mod(S+1)).
```

From `(t',f')`, first recover `t=t'-1 mod(D+1)` and then recover
`f=f'-[t=D] mod(S+1)`. This proves both compositions exactly, also D=0.
CLOSE's epoch map is the cyclic increment with inverse decrement.
No finite counter implements an irreversible sticky failure or halt.

Consequently every station J_s has the stated adjoint. Since head
positions are orthogonal and every J_s fixes position, multiplication gives

```text
F*F = sum_s |s><s| tensor J_s*J_s = I,
FF* = sum_s |s+1><s+1| tensor J_s J_s* = I.
```

This is a proof on the full tensor product, not only on initialized
trajectories or a selected coherent branch. For packet permutations it
first holds on the dense span of basis vectors and extends continuously;
the direct-sum catalogue gates are already bounded unitaries. The same
argument includes arbitrary superpositions of position, words and counters.

Each port accesses only the head and its attached actual memory vertex;
processor gates use only head factors. The GET list has
`2T+2(K+1)+1+2K+B=4N+4K+B+1` stations. PUT revisits the same actual
vertices in reverse order. A packet or pointer memory has two bus lanes
and GET/PUT for each, hence degree4. A program, bit or metadata memory
has degree2. The isolated descriptor has degree0. A rail station has
two rail neighbours and at most one memory neighbour, hence degree<=3.
Gate radius1 plus the next-position shift gives the conservative radius2
for F and its inverse in this port graph. It is not a physical embedding
in C's original transport chain. Word sizes, packet alphabet and the graph
depend on capacities; no uniform finite-dimensional local law is proved.

The bare energy ledger is also an all-state claim. Packet SWAPs exchange
equal spectra, including inactive stored fields and dirty packet buses.
Latch SWAP exchanges weights 2l and 2l0. G exchanges exactly two reserve
units with latch energy. The selected contexts act within the H=1 shell
and preserve presence/reserve. All other affected factors have flat
spectra, so reflection, pointer SWAP, all XORs and counter maps commute
with that ledger, even on dirty states. The added constant counts B baths,
K metadata, S program words, ten finite head controls, five flat finite
bus factors, head position and descriptor: `C_fin=B+K+S+17`.
The packet buses and latch bus contribute their stated variable energies.
Thus every J_s and F commute with each energy spectral projector. This
also gives commutation with the unbounded diagonal energy on its domain.
At finite energy, positive definite H and nonnegative reserves bound all
packet coordinates; all other factors are finite. Finite energy subspaces
are finite dimensional, but arbitrary catalogue phases need not have
finite order. None of this counts physical pulse work or derives a clock.

## 3. Fetched command identity on the complete data: F2

Fix an entry boundary with pc=t, q=0 and a classical tape. During the
first S stations pc is unchanged, so exactly its t port XORs A_t into
q. All other program ports are literal identities, rather than a hidden
RAM lookup. The instruction remains in q through PRE, extraction,
EXEC, reinsertion and POST. The reverse program-port order encounters
the same unchanged A_t with the same pc and XORs q to zero; only after
that does pc increment. The final head position is zero.

Fix the controls after PRE. Write the ordered GET swaps as R. For valid
targets, every operand role reaches one actual register; different same-
type roles have different targets. During GET/EXEC/PUT the opcode and
address controls q,a,b are unchanged. EXEC can change I,C,run only for
OPEN/CLOSE, which select no external operands. Other EXEC gates do not
change the selectors. Thus PUT is literally R^-1 for the same recovered
controls, rather than a newly selected route.

Here is the dirty-bus point without a cleanliness shortcut. If registers
`D1,...,Dr` are paired with bus registers `B1,...,Br`, their product
SWAP R exchanges the two tensor collections. For any operator V on the
bus roles, conjugation gives `R^-1 V_B R=V_D tensor I_B`. This is
an operator identity, not a statement only on blank basis buses. It
therefore holds on a matrix unit whose ket and bra have different bus
values, and on any data/bus/reference entanglement. No discarded bus or
fresh bus marginal is introduced. APPEND at exhausted a and COLLIDE
at exhausted b may still extract P0, but V is identity on every extracted
role; R^-1 R is identity on all data and buses there as well.

For a forward command POST applies A after reinsertion. Hence
`M+=A R^-1 V R`. For an inverse command PRE first applies A^-1. Its
old addresses are thereby recovered before the GET ports and remain
fixed until PUT. EXEC applies V*, and POST is identity. Therefore

```text
M- = (R^-1 V* R) A^-1 = (A R^-1 V R)^-1.
```

The notation R in this expression uses the controls after A^-1. It must
not be read as extraction at the original, uncorrected entry cursor.
In particular inverse exhaustion first recovers cursor D from cursor0,
subtracts the failure indicator, and performs identity data action.
Inverse successful APPEND recovers precisely the archived cell that
forward APPEND touched. Inverse CLOSE first restores the old e before
XORing I and toggling run. These are direct reasons the advertised
inverse formula works, not extrapolations from a clean run.

Induct over fetched commands. For an admitted classical start, all
classical head controls and the program are fixed by the instruction
sequence, independent of physical data. At every command boundary the
full map is exactly the literal external primitive program, its specified
metadata action, identity on all buses and the deterministic head/tape
factors. Metadata initially dirty are transformed by the prescribed XOR;
they need not be a deterministic output factor unless their initial
values are fixed. The fresh provenance conclusion below uses zero
metadata. Nothing in the control identity assumes pure data.

Apply the equality to ket and bra basis columns independently to obtain
every complete matrix unit `|s><t|`, including within-HIGH source units
and differing bus/reference values. Complex linearity handles imaginary
coherences too, although the audit catalogue is real. Finite rank
operators are dense in trace class and unitary conjugation is isometric
there, so continuity proves the asserted trace-class equality. Tensoring
any finite reference with identity preserves it. On the fixed full-output
identification the induced trace-distance control error is exactly zero.
This conclusion comes from the operator proof, not the finite verifier.

## 4. Compiler, actual timing and finite lifecycle: F3/F4

The loader contains exactly `B=L sum_i n_i` COLLIDEs. Induction on its
command rank gives b=j before its j-th command, 0<=j<B. Hence each
logical bath is extracted, collided and returned once, and b=B at its
end; none is reused as a fresh zero. The output of each bath occupies
its original memory vertex. The reused beta bus is restored, not a
second bath supply.

The A matching has N-1 disjoint packet swaps and the B matching has
N-1. Serializing them within their respective matchings gives exactly
their parallel product. One C transport step has `1+(N-1)+(N-1)=T`
completed commands, with its receiver first. A round is OPEN and
precontext, 2T such steps, then postcontext, APPEND and CLOSE. Its
length is `Q=2T^2+5`; no receiver or context duration is hidden in a
transport boundary. Thus H=B+hQ and S=2H+W. GET/PUT have 2g stations,
fetch/unfetch 2S and PRE/EXEC/POST/ADVANCE four, giving `d=2S+2g+4`.

Preparation finishes at B d, and round t starts at `(B+tQ)d`.
Its s-th completed transport step, 1<=s<=2T, is at
`(B+tQ+2+sT)d`. The receiver command in that step completes at
`(B+tQ+2+(s-1)T+1)d`. Its entry is one tour earlier and its actual
EXEC completes `S+1+g+1` microticks after that entry: S fetches,
PRE, g GET gates, then EXEC. This counts the actual gate, not the
location of a packet at a later command boundary.

C's geometric proof can also be recalled directly. One present packet
follows the cycle C0,...,C_(N-1),Q_(N-2),...,Q0 of length T. It first
reaches the receiver after N-1 completed steps; since G precedes the
swaps, the first funded reaction is step N. Its next visit is N+T and
releases. These are the only two reactions among the first 2T steps;
after them reserve2/latch0 and the packet position have returned. Its
pointer has received one translation, not a reset. Context conjugation
changes the retained source according to the complete post-state map.

For a clean head/metadata start, induction over rounds gives e=a=t,
I=C=run=0 at entry. OPEN(k_t) makes `(I,C,run)=(t,k_t,1)` without
changing e or a. APPEND extracts archive cell a=t, deposits the active
pointer there, flags it and XORs `(t,k_t,1)` into its initial zero
metadata. Since t<h<=K, it never requests a=K. POST advances a;
CLOSE clears I,C,run with the unchanged old e and increments e. Earlier
archive cells are never selected again in the forward round word.
This proves fresh-cell selection and provenance from initialized
chronology. A raw flag on a dirty input has no such implication.

At h=K, a=K is ordinary completion, with no failed request. A separate
forward APPEND at a=K has identity data action, increases f_A and wraps
the cursor. The same holds for COLLIDE at b=B. During at most S forward
commands from zero there are at most S failures, so mod(S+1) equals
the nonnegative count. Mixed polarities or dirty starts only have the
raw modular interpretation. The inverse recovers failures reversibly.

For every partial tour of r stations, let W_r be the literal prefix
product of those station maps together with head shifts. Then the state
at its microtick is W_r applied to the preceding boundary output, and
W_r has its explicit reversed adjoint. This supplies a fixed unitary
coordinate identification at intermediate ticks. Extracted source or
pointer data can reside on buses there, so naming the stationary C
location throughout a tour would be false. A coalesced audit is valid
only for station factors already proved identity; it must count their
head shifts and preserve their endpoints, as this verifier does.

The W NOP tours after H leave all data memories, metadata and buses
unchanged; program fetch scratch, head position and pc still move.
The promised read interval is `[Hd,(H+W)d)`. The inverse tail executes
the adjoints in reverse command order, so at S d all data, buses,
metadata and the initialized controller return, including pc=0 and
q=0. The unchanged program/descriptor were retained all along. The
head continues afterward: there is no absorbing halt. This return
holds only for unmeasured coherent continuation. An external parity
measurement whose apparatus is discarded is an additional map whose
inverse is not supplied by this tape. Source renewal likewise is not
created by a repeated head cycle.

## 5. Coherence, controller leakage and an exact repeated-context invariant: F5

On the admitted basis program, no control field is updated from a
source, pointer, flag or bath value. Metadata stores only I,C and a
constant append bit. The only physical transfers to the head are SWAPs
into buses, followed by exact conjugation back to memory. Thus no
fine source label is left in a classical head register or in metadata.
This statement is stronger than equality of output parity weights; it
is the tensor identity proved in section3. Entanglement may remain in
physical pointers/baths, as the device requires, and intermediate buses
may carry the source. Neither is a hidden classical label record.

At ideal readiness each even translation fixes E and each odd translation
takes E to the orthogonal O. With `P_LOW=|f0><f0|` and
`P_HIGH=I-P_LOW`, round k has branch operator
`P_(o,k)=U_k* P_o U_k` on the retained source. After a context word,
the complete branch is its ordered product, last round on the left,
on both sides of the initial source/reference density. All words,
including zero operators, remain in the instrument. Arbitrary
within-HIGH off-diagonal units survive ideal readiness. Changed
contexts cannot be replaced by independent scalar draws.

There is a useful sharper invariant in this particular positive
subclass. Let Pi_e be projection onto even pointer support. P's
reflection preserves it exactly. A supported receiver translation
by c(f_j) sends that support into parity beta_j, and the subsequent
release adds no translation. Hence for any pointer vector in the
even sector, including an entangled bank, the first round's archive
parity equals its source bin in the measured basis. Reading a bin
restricts that source to the corresponding coarse eigenspace; failure
of E coherence can dephase fine labels inside it but cannot move
support to the other bin. The next same context cancels the preceding
postcontext, its fresh active pointer is again even-supported, and
the next archive bin is identical. Induction gives only constant
LOW/HIGH words for every repeated-context sequence on the positive
even-bank domain, even at zero sweeps.

The same conclusion follows coherently, without an intermediate read:
expand all controlled translations in the common measured source basis.
Consecutive U_k U_k* cancel. Every occurrence of a fixed basis label
adds a pointer translation of the same parity, and the archive parity
word has that constant value. Summing those components cannot create
support in a nonconstant word.

Consequently the sentence in frozen specification section8 saying that
approximate finite preparation "can give other words" must not be
understood as an existential claim within this exact even-bank, D=I,
repeated-context subclass. The general comparison still retains all
ideal-zero branches and remains correct, but here such nonconstant
branches have actual weight zero as well. An initially odd active
pointer is an explicit off-domain example giving opposite first parity
and subsequent even-pointer parity. The review audits both domains
separately. This is an analytic wording/scope finding, not a counterexample
to F's inverse, command equality or the stated error inequality, and it
does not silently amend the frozen specification.

## 6. Extension of P with the actual remainder: F6

During preparation, the command identity says that each local collision
acts on its selected stationary pointer and fresh bath, with identity
on all buses and other physical data at the boundary. Fresh pure baths
must be independent of the buses too. Arbitrary prior pointer/source/
bus/reference correlations are allowed. The deterministic controller
extension is independent of these data. Thus the receiving P estimate
applies at time B d with buses, controller and metadata included in Z'.

Write `r=1-4/L^3`,
`delta=min(1,sum_i r^n_i(1-F_(i,0)))` and
`epsilon=min(1,sqrt(delta)+delta/2)`. The inherited even-sector rate
and union bound for commuting pointer projections give loss <=delta
for `R=P_E^(tensor m)`. To make the crucial comparator explicit, with
Pi=R tensor I one has

```text
Pi rho Pi = R tensor sigma,
rho_Z' = sigma + tau,  tau>=0, Tr(tau)=eta<=delta.
```

The off-diagonal R/complement blocks vanish under pointer partial
trace; no source/bath independence is inserted. Purification and the
rank-one trace norm give `||rho-Pi rho Pi||_1<=2 sqrt(eta)`, and
`||Pi rho Pi-R tensor rho_Z'||_1=eta`. Hence
`D(rho,R tensor rho_Z')<=epsilon`. The marginal is the actual output
remainder, with all its internal source/bath/reference/bus correlations.

The new obligation is that the internal C extension is one common map
on these two inputs. At every microtick after preparation and before
the end of the read window, the fetched opcode is non-COLLIDE. At
beta-bath ports the selector is identically false, and no processor
gate acts on beta as a bath operand. Every stationary spent-bath
factor is therefore untouched at each such microtick, not merely
restored at the endpoint. No decision is based on its contents.
Archive/control evolution depends only on the same classical program
and initialized counters; section5 excludes an extra fine-label record.
Thus the full internal measurement segment is a common unitary on
the other factors tensored with bath identity. Its partial-tour
versions have the same property. Complete parity read, when requested,
adds a CPTP instrument with all outcome records retained.

Trace-distance contraction under this one common CPTP map bounds its
complete actual/ideal outputs by epsilon at every named completed prefix
and final read. Preparation is charged once for the bank; h is not a
factor. A further classical history read contracts to TV<=epsilon.
Taking a prefix marginal preserves the same bound. For a branch w,
complete block-diagonal output comparison bounds its subnormalized
trace norm and its weight discrepancy. If both p_w and q_w are
positive, adding and subtracting one equally scaled branch gives the
safe bound

```text
D(rho_w/p_w, sigma_w/q_w)
  <= min(1, 2 epsilon/min(p_w,q_w)).
```

It is deliberately sufficient rather than optimized. If q_w=0, the
actual weight is at most epsilon; a normalized ideal state is undefined.
No branch is removed to improve this bound. In the repeated positive
subclass section5 proves an additional exact zero for nonconstant words;
the general error inequality does not require them to be positive.

The inverse tail is excluded from bath isolation: it intentionally
revisits baths to recover the complete coherent input. Finite exact E
from the forbidden dyadic basis-blank slice is not claimed. P remains
approximate, and source/context/coupling errors are absent only because
the present theorem assumes those primitives exactly. Any approximate
successor needs its own uniform complete-map control bound.

## 7. Occurrence interface, resource diagnosis and remaining premises: F7

The annex's report is a mathematical function of declared admission,
classical chronology, boundary and capacity information. Its first
ordered case is INVALID_PROMISE for missing/contradicted admission,
unsupported descriptor, absent classical chronology or a boundary outside
the retained forward/read interval. This is not a finding that every
unverified physical input is bad. Under admitted chronology, zero
completed rounds yields NO_COMPLETED_ROUND with empty prefix weight1;
j>=1 yields FORMAL_RECORD_AVAILABLE(j) with all 2^j branch maps,
including zero maps. K=0 therefore has the empty-prefix case. The
applicability label keeps conditional-on-declared, unestablished and
known-violated hypotheses distinct.

Resource diagnosis is independent: absent a request gives NO_REQUEST;
a specified forward COLLIDE/APPEND at a cursor below capacity gives
WITHIN_CAPACITY; at capacity it gives CAPACITY_EXHAUSTED, with the
actual reversible counter update retained. Inverse commands recover
resources and are not fresh requests. Without one specified classical
chronology, NO_CLASSICAL_CHRONOLOGY retains the raw coherent state.
One cannot infer such a chronology from a dirty counter. Full supported
completion has NO_REQUEST, even when h=K. An unsupported extra-append
tape can have INVALID_PROMISE and CAPACITY_EXHAUSTED simultaneously.
Reports of earlier valid prefixes remain statements about their earlier
boundaries; arbitrary later raw commands need not preserve the archive.

These ordered cases are exhaustive on the typed inputs. They use supplied
hypotheses, not a measurement of unknown quantum purity/coherence. No
unready input is projected, normalized into a successful trial or erased.
The complete raw joint state is retained for every case. Every realized
record field is NOT_DERIVED. Funded WRITE, append flag, formal parity
projector and actual realized outcome remain four different objects.

There are likewise three separate laws. P_dev consists of the traces
of the actual finite prepared/controller device; P_idealC consists of
the exact ready-bank comparison with the actual remainder; P_actual
would require an independently supplied actual preparation measure
and actual record map. Neither exists here, so epsilon_occurrence is
undefined, not zero. A future proof on a common complete history space
could combine epsilon_occurrence, epsilon_control and epsilon_prep by
the triangle inequality, retaining all branches. The present theorem
only supplies the middle term zero and the formal preparation comparison.
It does not compare actual conditional post-states on rare prefixes.

The supplied program, descriptor, single-head preparation, capacities,
graph, finite catalogue, exact phases/pulses, pure fresh bath bank,
source code/state, contexts, C geometry and flags remain premises.
Internal fetch/address scheduling is proved in a discrete added law;
it does not derive the native U, a physical tick or drive Hamiltonian,
continuous-time control, measured work, independent renewed trials,
actual outcome selection or an initial measure/frequency law. No
physical apparatus-family completeness or Canon promotion follows.
The QDD physical owners and their named cross-layer gates remain open
with their existing scope.

## 8. Review disposition before execution and author comparison

The all-state inverse, complete fetched-command equality, archive/bath
cursor semantics, all-step/compiler lifecycle, coherence and leakage
argument, and the enlarged actual-remainder comparison are independently
derived above. No counterexample to those mathematical claims has been
found by this paper review. The explicit repeated-history scope finding
in section5 must remain visible; a positive statement that finite even
preparation creates nonconstant repeated words would be unsupported.

The frozen finite verifier is an independent routing and composition
audit with the common-mode primitive-catalogue limitation disclosed in
PREREG. It has not been executed at this source freeze. Its eventual
first-run result, two-architecture replay and later author-source
comparison are separate evidence and are not anticipated here.
