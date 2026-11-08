# A counted, driven local realization on the occupation ports

**NON-CANONICAL, L1. Conditional analytical candidate-T. Independent
acceptance pending.** Author: A. M. Thorn. Apache-2.0.

This is an existence construction in an explicitly added gate model. It
preserves the original finite source and receiver occupation reading at
the output. It does not derive quantum gates from the six-pentit rule,
select the physical energy, or construct a self-starting autonomous clock.
Its deliberately large bounds are upper bounds, not a practical design.
No expanded circuit or scientific program was executed.

## 1. Finite occupation encoding without a receiver-state oracle

Use the period-15 coordinate closure in [SOURCE_CIRCUIT](SOURCE_CIRCUIT.md),
with R and c represented by 90,...,104 and r by -7,...,7. Its complete
unitary agrees with every prefix of the preparation on the admitted seed
family: three SELECT blocks reach at most coordinate distance six, and
the final source is supported at distance two. Three subsequent forward
steps reach at most distance five. Equality is an admitted-input statement,
not equality of the periodic and infinite operators on arbitrary states.

Use the actual phase-zero occupation intertwiner of Canon v105,
HOMOGENEOUS-CAPTURE-CURRENT-RECORD: I_0=Emb Gamma^(-1) D_2*, with
D_2=diag(1,i,i,-1), tensored with identity on memory and reference.
The diagonal gauge is part of the encoded unitary, not a discarded coin
phase. It changes no support or charge. The object positions R+r and R-r
lie in 83,...,111. All token/pulse positions and the receiver at 100 fit in
this same 29-site interval. The prescribed codes are injective on this
active sector and use only -1,0,1 in the 38 occupation coordinates at each
site. Coincident object, carrier and receiver entries use their disjoint
subbanks. The unused spectator coordinates are zero.

Represent one such occupation coordinate by two qubits, with

```text
00 -> 0, 01 -> +1, 10 -> -1, 11 -> 2.
```

The fourth level is the genuine integer occupation h=2; it can be used
transiently by the compiler and has native charge 8. It is not an extra
zero-energy encoding of h=0. This is a fixed representation of the
original occupation values, not a
replacement of the receiver by a decoded archive. It uses

```text
29*38*2 = 2204 occupation qubits.
```

Add two qubits for the qutrit, one attenuation qubit and one retained
setting qubit. Thus n=2208 data/control qubits suffice. The full receiver
code and every correlation with an arbitrary external reference are
included. The reference is not represented by a finite classical table.

Compose I_0 with the two-qubit occupation encoding. On its valid code,
conjugate the complete finite unitary of
SOURCE_CIRCUIT, including the coherent setting correction. Define it to be
identity on the orthogonal invalid occupation-code subspace. The unused
fourth qutrit state is already given a unitary completion. This specifies
one full 2^n-dimensional unitary V, independently of the unknown memory.
Every valid active-sector occupation ket has native charge 10. Hence V
commutes with the following bare charge on the entire finite data space:
each encoded occupation has charges 0,2,2,8 on 00,01,10,11, exactly
2h^2; all four added control bits have charge zero. The largest data
charge is

```text
Q_max=8*38*29=8816.                                  (L1)
```

The inactive-complement identity is a declared completion, not a theorem
about arbitrary occupations under the original spatial law.

## 2. Exact local synthesis with an explicit workspace bound

For n>=3, let D=2^n. Exact column elimination factors any D-dimensional
unitary into at most D(D-1)/2 two-level rotations and at most D one-level
phases, hence at most D^2 factors. A pivot pair a,b is eliminated with a
normalized two-by-two unitary obtained from a,b and their conjugates;
zero pivots are skipped. This is a finite constructive specification and
does not require a numerical matrix run to establish existence.

For two computational strings, take a Gray path changing differing bits
one at a time. At most n-1 adjacent basis transpositions move one string
next to the other without moving the latter. Apply the desired rotation
on that pair and undo the transpositions. This costs at most 2n-1
multi-controlled one-qubit operations. Diagonal phases have the same
upper bound. All masks and inverse paths are included.

An operation with n-1 controls is implemented by masking zero controls,
computing their conjunction into n-2 initially zero scratch bits, applying
one controlled one-qubit operation, uncomputing the conjunction, and
undoing the masks. It costs at most

```text
2(n-2) Toffoli + 1 controlled rotation + 2(n-1) X <= 4n
```

gates acting on at most three qubits each. Scratch returns to zero on
the declared ready subspace. On dirty scratch the same circuit is still
a full unitary, whose different output is retained rather than omitted.
In particular the semantic-invalid-data identity is only guaranteed with
ready scratch; no identity assertion is made for dirty scratch.
Thus an unrouted realization uses at most 8n^2 4^n small gates and n-2
scratch bits.

Put the n data/control qubits and n-2 scratch qubits on a finite line,
preserving adjacent pairs for the occupation encoding. Its length is

```text
N_q=2n-2=4414.                                      (L2)
```

For each small gate move its at most three operands to consecutive
positions by adjacent SWAPs, apply it, and reverse those routing SWAPs.
Fewer than 6N_q+1<=16n operations per gate suffice. The data return to
their original physical register positions after each routed operation.
The resulting conservative count is

```text
G_0 <= 128 n^3 4^n.                                (L3)
```

This realizes V on the original occupation code, with the original
receiver at the output, and all computational scratch restored. The
fine line resolves each original spatial site into a finite register
block. The original two-microtick timing is not inherited by this added
preparation circuit.

## 3. A sharp finite reservoir for the declared bare charge

The gates in Section 2 need not conserve bare charge individually. They
can nevertheless be funded locally without supplying an energy-coherent
reservoir for this particular charge dictionary.

Give a reservoir site the ladder 0,...,B with energy E_unit*b, where
E_unit>0 and

```text
B=3Q_max+20=26468,       b_0=2Q_max=17632.            (L4)
```

Prepare one such site sharply at b_0. Put an identical ladder rail beside
the N_q-qubit line, with N_q ladder sites in total; all other ladder sites
are initially sharply at zero. These are counted initial resources.

A routed primitive acts on at most three consecutive data/scratch
qubits. Include the partners of every encoded occupation bit that it
touches. The resulting cluster A is contained in at most six consecutive
qubit positions and has a complete integer-valued local charge q_A, with
0<=q_A<=Q_max. Extend the primitive by identity on those partners.

For every local total-energy integer e with max(q_A)<=e<=B, all vectors

```text
|x>_A |e-q_A(x)>_battery
```

exist. On this full energy fiber implement the original primitive matrix
G in x. On every incomplete boundary fiber use identity. Each fiber is
complete, and the definition is a unitary on the entire finite tensor
product, commuting exactly with q_A+N_battery. This includes arbitrary
input occupation codes, not only successful branches.

For the declared ready source, data charge is 10. Throughout the lifted
word the active reservoir level equals

```text
b=2Q_max+10-q_data,  0<=q_data<=Q_max,
Q_max+10 <= b <= 2Q_max+10.                          (L5)
```

Thus its local total energy is always at least max(q_A) and at most
3Q_max+10<B. Every visited fiber is one of the full fibers. More explicitly,
put E=2Q_max+10 and define the isometry

```text
J_E phi = sum_q P_q phi tensor |E-q>_battery.
```

It is defined on the whole data/scratch space. With the working reservoir
at the gate, its local total energy is E-q_rest. The funded operation
therefore satisfies Lift(G) J_E=J_E G. Induction proves exact simulation
of the unfunded word, including all coherences and references.
At the endpoint data charge is
again 10, so the reservoir returns sharply to b_0 and decouples. This
return is for the fixed-ready input and the charge-preserving endpoint;
it does not reset an arbitrary physical input or regenerate a clock.

Move the reservoir state along the identical ladder rail by adjacent
whole-ladder SWAPs, perform the funded primitive, and return it home.
Each SWAP conserves the sum of the two ladder energies. The other rail
sites return to their original zeros. At most 2(N_q-1) rail SWAPs and one
funded interaction per primitive give

```text
G_f <= 512 n^4 4^n.                                (L6)
```

Every funded interaction involves at most six nearby qubits and one
adjacent ladder site; a rail SWAP involves two adjacent ladder sites.
No hidden arbitrarily large support is left in a named controlled-U call.
The largest local ladder dimension is explicitly 26469. The complete
hardware count here is 4414 qubits and 4414 such ladder sites, with the
38-coordinate occupation representation included in the qubit count.

## 4. Strength, runtime and the unpaid controller boundary

Fix an interaction norm cap g>0 before the circuit length is chosen. For
each funded small unitary G choose its bounded self-adjoint logarithm
K with exp(-iK tau/hbar)=G and

```text
tau=pi*hbar/g,             ||K||<=g.
```

This bounded signed control is an admitted driven interaction. A
requirement of positive control pulses can instead use the logarithm
with angles in [0,2pi) and tau=2pi*hbar/g, doubling the time bound below.
Because G commutes with the appropriate bare charge, its spectral
logarithm does too. On the sharp total-charge input, including the bare
Hamiltonian only supplies a common free phase. On arbitrary superpositions
of total energies the equality to the gate word is in the interaction
picture; the full Schrödinger evolution retains that known free factor.
The algebraic identity complement is not silently interpreted as a
stationary Schrödinger-picture complement. A serial externally
scheduled realization therefore takes at most

```text
T_prep <= (pi*hbar/g) 512 n^4 4^n,    n=2208,         (L7)
```

before the three original forward readout steps. There is no speedup by
increasing the coupling strength with the apparatus size.

This is a driven construction. The controller must supply the ordered
list of at most G_f gates, their algebraic calibration data, locations,
and timing. These exact gate matrices are finite algebraic objects
obtained by elimination, but their bit storage, numerical implementation,
clock precision and work of switching have not been bounded here. They
are explicit remaining resources, not zero-cost inputs. As an elementary
switching bound, turning one norm-g control term off and another on can
change its expectation by at most 2g; this is not a lower bound on work
or a proof of a regenerating control mechanism.

The full Hamiltonian is time dependent. Bare-charge conservation does
not prove conservation of its time-dependent control energy, nor of
Q=E0 f(U_rec). The latter need not have a local occupation density and
is not identified with E_unit H_N. A sharp reservoir for H_N therefore
does not evade the original-Q stationarity obstruction in
[RESOURCES_RESET](RESOURCES_RESET.md).

## 5. Readiness, errors and the actual extent of the result

The construction assumes the fixed original occupation basis source u2,
ready LCU bits, n-2 ready scratch bits, sharp reservoir/rail states and
the retained setting. Unknown receiver/reference data are never used as
a clean workspace. The full readout contrast additionally requires old
memory in span(d1,...,d25).

For a noisy initial state at trace distance zeta from this complete ready
input and uniform operator error at most nu in every funded gate, the
complete endpoint error, including all returned helpers and rail sites,
is at most zeta+G_f*nu. This is a sufficient engineering budget, not a
claim that the very small required nu is physically attainable. The
finite thermal reset theorem in RESOURCES_RESET supplies a separate
counted way of approximating zero-energy scratch; it does not supply the
original source, sharp excited reservoir or an autonomous controller.

For example, prepare the three LCU bits and n-2 synthesis scratch bits
from independent zero-energy thermal states by that reset protocol.
Their entire initial helper/donor block is the specified product Gibbs
state, independent of the source, old memory/reference and setting;
diagonal marginals alone are not substituted for this condition.
Keep a supplied
coherent setting as information. Then M=2209 helpers, a readiness
tolerance of 1/4000 and

```text
r=50, beta_h*d_h=ln2, beta_c*d_h>=ln(35344000),
2Mr=220900 fresh donor qubits.                       (L8)
```

The total quantum-register inventory for this helper-prepared variant is
225314 qubits and 4414 ladder sites of dimension 26469, before any timing
controller or detector. The original source basis seed and sharp
reservoir/rail states remain supplied separately. Initially the donor
mean energy is Mr*d_h*(1/3+gamma); the source and rail contribute
E_unit*(10+17632). Their temperatures and sharp/nonthermal status are
not interchanged. For these diagonal thermal helpers and diagonal
donors, the joint cooling state is classical, so the last paragraph of
RESOURCES_RESET Section 3 gives the same linear error below 1/4000 even
against the product of ideal ready helpers and the actual changed donor
marginal. Subsequent control leaves the spent donors untouched. A dirty
coherent helper input instead needs the stated square-root global bound.

One explicit local cooling layout gives every helper a hot donor rail
and a cold donor rail, each of length r. Bring donor j on each rail to
its near endpoint by j-1 adjacent SWAPs, apply the three-qubit reset,
then undo the rail SWAPs. The used donors return to their own slots in
changed states. Over r rounds this costs 2r(r-1) rail SWAPs and r reset
gates per helper, hence M(2r^2-r)=10934550 local operations for (L8).
All donor SWAPs conserve their identical gap d_h. Sequential cooling
adds at most (pi*hbar/g)*10934550 to the driven duration with the same
interaction cap. It supplies no fresh donors for a second cooling run.

The local control-term cap is g. Including the bare onsite terms, a
uniform declared term bound is max(g,E_unit*B,d_h), fixed before running
the word. Lowering the reset error increases the counted donor bank and
cooling time; it does not silently increase g.

We have proved a finite, bounded-support, bounded-strength driven
implementation on a fixed representation of the actual occupation ports,
with one explicit charge-funding scheme and a complete complement. The
following are not proved: native six-pentit gate admission, thermal
preparation of the entire original-Q source, controller self-start/reset,
material tolerances, physical selection of H_N or H_*, and indefinite
retention. None is inferred from the enormous finite gate bound.
