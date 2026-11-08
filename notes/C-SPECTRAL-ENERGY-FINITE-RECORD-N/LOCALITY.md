# A local qubit circuit for the declared finite energy code

**NON-CANONICAL, L1. Conditional analytical candidate; independent
mathematical acceptance pending.** Author: A. M. Thorn. License: Apache-2.0.
Public reservation: #1767. This is an additional construction. It changes
none of the seven preceding candidate files or their hypotheses.

The finite abstract source/output model can be compiled into qubit gates
with uniformly bounded support and a fixed-width physical layout. The
construction is deliberately inefficient. It counts the larger raw qubit
space, its workspace, and the readiness of its padded factors. It does not
confine the original infinite walk to a finite region. Its relation to that
walk remains the endpoint dictionary in FINITE_MODEL.md.

This note specifies a circuit. The additional local autonomous history,
its clock geometry, duration and energy moments are separate constructions.
In particular a bound of four data qubits per gate is not a claim that the
corresponding autonomous term has only four sites.

## 1. Joint eigenlabels and the physical one-hot code

Let s=dim(X_f) for the fixed finite source space in FINITE_MODEL.md. Its
rounded and compressed energies commute. Choose an orthonormal common
eigenbasis indexed by alpha and write

    q_f |alpha> = d j_alpha |alpha>,
    r_f |alpha> = r_alpha |alpha>,
    q_phys=q_f+r_f,
    j_alpha in {0,...,m},       0 <= r_alpha <= d.        (L1)

The basis and the deterministic finite target unitary are specified before
the evolution. No diagonalization by a physical apparatus is being assumed.
The vectors define the encoding and its supplied couplings.

Order the labels by nondecreasing j_alpha. Between successive distinct
heights, insert a helper label at each missing integer height. Give every
helper residual zero. The resulting label chain has length ell with

    ell <= s+m,
    j_(i+1)-j_i in {0,1},       1<=i<ell.               (L2)

The order within an equal-height group is fixed once. Original eigenlabels
are encoded by exactly one excited qubit at their assigned sites and zero
at all other label sites. Helper-label states are new physical states,
not unidentified original eigenvectors.

Choose an arbitrary specified common label offset mu>=0. Label site i has
physical gap mu+d j_i+r_i and rounded gap mu+d j_i. The common offset is
constant on the one-excitation code; it can be positive without altering
the encoded energy differences. It is not omitted from the full hardware
energy or a thermal preparation account.

The battery ladder is encoded by N gap-d qubits:

    |k>_ladder -> |1^k 0^(N-k)>,       0<=k<=N.          (L3)

All 2^N raw configurations are physical. Only N+1 are the unary ladder
code. A nonunary input is never silently projected out.

Encode every finite information register in ordinary zero-energy qubits.
For a register of dimension h use ceil(log_2 h) qubits and fix an injection
of its h basis labels. The unused binary strings remain raw states. Let f
count the information qubits, including the occupied archive, the new
pointer and any retained flags. A conservative starting count for the
registers explicitly used in FINITE_MODEL.md is

    f <= 3*327681 + 655392 + 3*5 + 1 = 1638451,          (L4)

before adding any separately declared information or validity flags. The
three five-qubit blocks encode carrier labels, old memory and archive;
the last one-qubit factor is the new pointer. Larger padded f is allowed
and must be used in the resource bounds below. One extra retained composite
acceptance flag, if required, is counted by increasing f by one; it fits
within the same padded construction. The code states, including
arbitrary occupied-memory/archive/reference entanglement, are not required
to be computational basis states.

## 2. Three interleaved tracks and complete raw energies

Put b=ell+N+f and n=16b. Use n cells with three qubits per cell, in the
following physical column order:

    E_i at column 3i-2,   X_i at column 3i-1,
    Z_i at column 3i,                         1<=i<=n.  (L5)

Every E qubit has gap d. Reserve the first five Z sites for the archive.
Place the active E and X segments starting at cell 6: the first N active
E sites are the encoded battery and the first ell active X sites are the
chain (L2). The constant five-cell offset does not change any diameter
bound. Unused E sites are transport padding, initially zero in the ideal
input and restored at the end of each compiled target. Unused X sites
before the chain have height j_1, and those after it have height j_ell;
all have residual zero and are initially unoccupied. Every Z qubit has
energy zero. Place the final acceptance flag at Z_(n-1) and the fixed
pointer at Z_n. The remaining information and workspace lie between the
archive prefix and this final pair. If an extra composite flag is used,
that flag occupies Z_(n-1) and is included in f.

During source/battery preparation and the compensated source program,
route only on the connected Z suffix from cell 6 through cell n-1. The
archive prefix and the pointer are untouched, including by routing swaps.
The archive-writing circuit may use the Z segment from cell 1 through
cell n-1. No earlier operation ever routes through Z_n. This placement
is why the arbitrary occupied archive can be treated as a passive
reference until its actual controlled exchange.

Define on the entire 3n-qubit space

    N_X = sum_i n_(X_i),
    E_d = d sum_i n_(E_i) + sum_i (mu+d j_i)n_(X_i),
    R = sum_i r_i n_(X_i),
    E_phys = E_d+R.                                    (L6)

The raw dimension of one such row is 2^(3n), not s times N+1 times the
logical information dimension. In particular every padded excitation,
nonunary charge pattern, multiple label excitation and occupied workspace
is part of the raw model. All the primitives below preserve E_d and N_X
on this entire space.

For the encoded one-label states with no transport excitations, E_phys
agrees with the compressed original energy plus the battery and the
declared scalar mu. At helper-label configurations it is the explicitly
assigned extended energy. No original-space interpretation of those
intermediate configurations is inferred.

## 3. Allowed local moves

The following elementary unitaries are specified with identity action on
all basis states not named in their active two-state block:

1. Adjacent E exchange or rotation: an arbitrary two-state unitary on
   |10>,|01> of E_i,E_(i+1).
2. Equal-height label exchange or rotation: the same operation on
   X_i,X_(i+1) when j_i=j_(i+1).
3. Funded adjacent label rotation: when j_(i+1)=j_i+1, an arbitrary
   two-state unitary on

       |X_i X_(i+1) E_i> = |101>, |010>.              (L7)

   Both basis states have one label excitation and equal rounded energy.
   The reverse direction is the adjoint of the same gate.
4. One-qubit operations on Z, adjacent Z SWAPs, and reversible Boolean
   operations on at most three Z sites. Physical E or X bits may control
   an operation on Z without themselves being changed.
5. A gate in items 1-3 controlled by a neighboring Z bit, and diagonal
   phases on a computational basis pattern after that pattern has been
   coherently computed into Z workspace.

A funded rotation with its Z control acts on four data qubits. All other
listed gates use at most three. They conserve E_d and N_X on arbitrary raw
states, not just on the one-hot code. They need not conserve E_phys
separately, since residual energies may change.

Arrange the Z control of (L7) at Z_i. Its four sites lie between columns
3i-2 and 3i+2. Equal-type E or Z SWAPs join neighboring cells. A Boolean
operation on three consecutive Z sites has horizontal diameter six column
spacings. Thus every primitive has support at most four and horizontal
diameter at most six. The number of possible neighboring physical sites is
bounded independently of s, m, N and f.

Only equal-type E and Z qubits are swapped for routing. In particular an
energy-bearing E qubit is not swapped with a zero-energy Z qubit. Nor are
two arbitrarily weighted X sites swapped. Label motion uses precisely the
equal-height or funded transitions above.

## 4. Connectivity in a fixed energy sector

First consider configurations with exactly one label excitation. After
subtracting its constant mu, let the total rounded integer energy be k.
At label height j the charge track must contain k-j excitations. With n
available charge qubits, that label is allowed exactly when

    0 <= k-j <= n.                                     (L8)

Because the label heights are nondecreasing, the allowed sites form a
contiguous portion of the label chain. Charge configurations with a fixed
number of excitations connect by adjacent E SWAPs. A move up by one label
height requires an occupied E_i; one exists whenever that move has a
valid endpoint. A move down requires an empty E_i, which likewise exists.
Adjacent E SWAPs bring that occupied or empty bit to E_i. An equal-height
label move needs no funding. Hence all one-label computational states in
the same rounded energy sector connect by the moves in Section 3, together
with flips of zero-energy information bits.

For endpoint states supported in the first ell active label sites and
the first N active charge sites, put c=max(ell,N). Only the first c
active E sites are needed for transport. Move the label
monotonically to its final site. It crosses at most ell-1 label edges and
at most v=j_ell-j_1<=ell-1 funded edges. Each funding bit can be brought
to its local site with at most c adjacent E swaps. Finally rearrange the
charge configuration to the desired one with at most c^2 adjacent swaps,
and flip the required information bits. A conservative path bound is

    h <= ell + v(c+1) + c^2 + f <= 4n^2.               (L9)

The actual height range v, not the absolute upper charge m, controls this
path. Thus an unused low-energy interval below every original label does
not cause an incorrect assumption m<=ell. Removing loops gives a simple
path no longer than this bound.

For a target acting only on the charge track, fixed-charge connectivity
uses E swaps alone. For a target acting only on zero-energy information,
the ordinary bit-flip graph is connected. Those two cases do not require
any assumption on N_X.

## 5. Selecting one pair without changing the energy controls

A transition between two neighboring configurations along such a path
changes at most three data bits: two for an exchange, three for (L7), or
one for an information flip. It can be made selective by conditioning on
every other participating data bit having its prescribed computational
value. This includes any of the c-N E transport sites used along the path.
There are at most q=ell+c+f<=2b participating bits. Remaining physical
E/X padding is untouched by these paths; dirty values there are retained
spectators rather than silently treated as zero controls.

For each controlled E or X bit, transport a designated zero-energy copy
qubit along the Z track to a neighboring Z site, copy that bit with a CNOT,
then reverse the Z routing. A negative control is formed by applying X to
the copy qubit, not by flipping the physical energy-bearing control. For a
Z information bit, route the control and a copy qubit to neighboring Z
sites, copy, and restore their positions. All these are reversible coherent
operations. They copy basis predicates, not arbitrary unknown states.

Compute the AND of the copied literals into a chain of fresh zero-energy
prefix flags using Toffoli gates. Consecutive participating logical Z bits
are brought to three consecutive physical Z sites by adjacent Z SWAPs,
then restored. Route the final AND flag next to the desired physical
rotation, apply the controlled version of that rotation, and undo the flag
computation and every copy. The target data bits are excluded from the
predicate. The two named configurations therefore undergo exactly the
chosen two-state unitary, while every other main configuration is fixed.
The copied controls are unchanged during the rotation, so uncomputation is
valid for superpositions and reference-entangled states.

At most 6b zero-energy workspace bits suffice: at most 2b copied literals,
2b prefix flags and 2b reserved routing positions. There is ample room in
the n=16b Z sites after the f information bits are placed. The pointer is
excluded from this workspace. Routing permutations are restored exactly;
unrelated Z states may be displaced during routing but are not assumed
blank merely because they pass through a routing location.

For a conservative elementary-gate count, each routing of up to three
chosen Z qubits to consecutive sites and back uses at most 12n adjacent
Z swaps. A literal copy, its possible polarity flip, or an AND step plus
such routing therefore costs at most 12n+4 gates. Fewer than 8b such
operations account for all copies and ANDs together with their inverses.
The final control routing and rotation use at most 4n+1 more gates. Thus
one selective path-edge unitary, including complete cleanup, uses fewer
than

    200 b n = 3200 b^2                                 (L10)

primitives. This bound intentionally counts unnecessary routing. Each
primitive still has the support and diameter stated in Section 3.

The initialized-workspace condition is essential for the promised
selective target. On a dirty workspace the same list of elementary gates
is still a complete unitary and still conserves E_d and N_X, but need not
implement that target or act identically. Dirty workspace sectors are
not discarded. Their preparation error must be included by the autonomous
construction that uses this compiler.

## 6. Arbitrary finite targets and an explicit conservative bound

Take a unitary target on the b main qubits which commutes with the rounded
energy and has nontrivial label action only in N_X=1 sectors. Specify it
as identity on the complement of its semantic code whenever that
complement is an invariant orthogonal subspace. This retains all genuine
successes and rejections inside the program's code; rejection is not an
invalid codeword.

In each energy block, ordinary finite matrix elimination decomposes a
unitary into two-basis rotations and basis phases. Summed across all
blocks, at most 2^(2b)=4^b such rotations/phases suffice. Additional E
transport bits start and finish at zero: each rotation's paths are in
their expanded q-bit space, and its exact selective implementation is
identity on every basis state except its two named endpoints. They do
not enlarge the number of target matrix entries being eliminated. For a
two-basis rotation between nonadjacent configurations, choose a simple
path as in Section 4. Selective transpositions along its first h-1 edges,
one selective rotation at its last edge, and inverse transpositions
realize that rotation on the two original configurations. There are at
most 2h-1<=8n^2 selective path-edge operations. A basis phase uses the
same literal/AND method and has the smaller cost (L10).

It follows from n=16b and (L9)-(L10) that a single such target has an
elementary-gate realization of length at most

    4^b * 8n^2 * 200bn
       = 6553600 b^4 4^b.                              (L11)

This is a finite existence bound, not an efficiency claim. It includes
all the controls and their cleanup; it does not assume a constant-cost
global gate. The matrix coefficients and exact local rotation angles
remain specified coupling data. No expanded matrix or circuit was
computed in obtaining the bound.

Pure charge-track targets and pure zero-energy-information targets obey
the same bound by the special connectivity cases in Section 4. Therefore
three successive targets, with complete cleanup between them, have

    J <= 20000000 b^4 4^b.                             (L12)

Padding by identity gates is allowed and does not change the unitary or
the raw conservation laws.

## 7. The preparation, program and occupied archive

The compiler applies to the following three named finite targets.

**Unary compression C.** If a binomial battery preparation is used, its
charge-k symmetric input vector and the desired unary output have the
same charge. Choose a unitary in that charge sector carrying the former
to the latter. For example, their coefficients can be chosen real; the
Householder reflection with normal proportional to their difference does
so, with identity used if they coincide. It acts identically on the
orthogonal complement of their span. The direct sum over charges is a
complete charge-preserving C. It is not claimed to be identity on every
nonunary input: the input being compressed is itself generally nonunary.
The supplied coherent qubits and its pure buffers remain preparation
resources. With a supplied sharp unary battery, C may be the identity.

**Compensated program.** Let P_x be the fixed finite source-basis change,
if used, and let W=U_f P_x. Encode the complete finite-battery lift
Gamma(W), with identity on all incomplete total-energy fibers and on
invalid original-label or finite-register codes. On the valid code this
is the whole program, not an accepted-branch map. Its binary extension is
unitary and preserves E_d and N_X. C and this program leave the added
archive and pointer untouched. The compiler must therefore be applied
to their smaller active registers, treating the archive/reference as
untouched, rather than allowing arbitrary synthesis steps to touch them.

**Occupied archive writer.** Let F_acc be the completed acceptance flag.
First perform its controlled exchange of the fixed raw binary memory
and archive blocks, while leaving the new pointer untouched. The two
blocks have equal binary width and zero energy. A full binary-block SWAP
is an explicit unitary extension of the 26-label logical exchange;
unused binary strings remain physical and are swapped too. This is a
declared raw extension, not a claim that an invalid binary string is an
extra accepted logical symbol. If identity on invalid memory/archive
strings is desired instead, an explicit reversible validity predicate
must be included and counted in the writer's guard.

Place F_acc and the new pointer at the final neighboring Z sites, as in
Section 2. Compile the controlled exchange without touching
the pointer and return every temporary copy and flag. The last logical
primitive is then CNOT(F_acc,P). No later circuit operation touches the
archive or pointer. Thus the pointer cannot be written before the
archive exchange has been completed. Source failure branches have
F_acc=0 and leave both the occupied archive and ready pointer unchanged.

The additional final CNOT can be absorbed into the conservative slack in
(L12). The three-target bound includes the exchange as the third target;
its explicit final pointer gate adds only one primitive. The endpoint
comparison and the reference-uniform logical permutation are those of
FINITE_MODEL.md. They do not assert that the original coherent source was
prepared as an independent reduced physical state during a compensated
source-basis change.

For an arbitrary dirty pointer the same final CNOT remains unitary and
can erase or flip an old pointer value. Its intended semantics require
the stated readiness. The operation on an occupied archive is a SWAP,
not copying or deletion. A fixed-site record in a row-transfer Hamiltonian
requires the additional physical routing proof of that construction; the
circuit-level ordering alone does not prove it.

## 8. Residual energy, thermal defects and what remains supplied

The complete raw residual satisfies

    0 <= R <= d N_X.                                   (L13)

For every compiled unitary Z, or every autonomous propagator whose
generator preserves both E_d and N_X, one has

    -d N_X <= Z^* E_phys Z-E_phys <= d N_X,
    |Delta <E_phys>| <= d <N_X>.                        (L14)

The proof uses Z^*E_d Z=E_d and applies (L13) to both Z^*RZ and R;
Z^*N_XZ=N_X. It includes arbitrary raw inputs and correlations. On an
ideal one-excitation label input the bound is d. If many data rows are
introduced, N_X counts every label site in every row, and the residual
contains every corresponding r_i. A bad-input weight eta alone gives
only the conservative bound d[1+eta(N_X,max-1)] when the good component
has exactly one label. For product thermal label copies use the actual
sum of their excited-state means. Thermal defects do not disappear from
the energy account because their output is unwanted.

The locality construction still supplies exact gate parameters, the
common eigenlabel dictionary, the prepared source code, pure or
quantitatively prepared workspace and pointer, and whichever battery
resource is declared. Zero bare energy does not prepare a pure flag.
A binomial packet requires its stated coherent resource; a sharp
charged packet requires its stated charge and purity. Their physical
preparation is a separate unitary/resource contract, not a consequence
of this compiler or of spatial locality.

Decisive failure conditions include a false connectivity assertion in
(L8)-(L9), a primitive changing E_d or N_X on a raw state, a selective
rotation failing with its specified clean workspace and an admitted
reference, a failure of the gate-count accounting, or a violation of
(L14) with the stated global excitation count. A claim of an original
spatial trajectory between code endpoints, thermal preparation without
its resources, or an efficient material implementation lies outside
the theorem. No scientific executable or gate enumeration was run.
