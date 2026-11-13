# Declared contact for the fixed phase pair

```text
Author: A. M. Thorn
License: Apache-2.0
SPDX-License-Identifier: Apache-2.0
Visibility: PUBLIC
Scientific status: NON-CANONICAL, L1
Evidence status: AUTHORED_PROOF / SELF_REVIEWED
Probe: P-J-PHASE-DECLARED-CONTACT-1
Claim issue: https://github.com/mathorn1973/twist-j/issues/1578
Public authority base: dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d
```

This is an authored algebraic proof and a same-session self-review. It is
not an independent formal review and creates no Canon promotion. Formal
execution and its evidence are recorded separately.

## 1. Scope and inherited architecture

The positive construction uses the already declared two-cell architecture
of `DEF-RESIDUAL-CONTACT-ARCHITECTURE` and the complete maps of
`CONTACT-RECORD`. Its carrier is

\[
\mathcal X=\mathbb F_5^{12}\times\{0,1\},\qquad
\omega=(p_x,q_x,r_x;p_y,q_y,r_y;\eta).
\]

Each piston tuple is in the existing order `(a,b,c,d)` and is reshaped as
the row-major matrix `[[a,b],[c,d]]`. Arithmetic on native coordinates is
in F5. The bit eta and finite word positions retain their declared types.
Inverses and operation products act right to left; chronological leaf
lists below are explicitly labelled.

The gates W_b and Ucal_i are declared additional interfaces. Their use
here does not derive them from the original five generators, the actual
autonomous U, or J. A fixed word in this extended alphabet is not by
itself a physical controller, detector, energy account or realization.

The negative comparison concerns only operations compatible with the
specified quotient pi. It is not a classification of every operation
admitted anywhere in TWIST-J, and it excludes no unspecified physical
apparatus class.

## 2. The unchanged source pair and common receiver

Let j be the marked primitive fifth root of unity. The existing
coefficient basis B0=(1,j,j^2,j^3), followed by coefficient reduction
modulo 5, gives

\[
p_+=(0,1,0,0),\qquad p_-=(4,4,4,4),
\]

for alpha_+=j and alpha_-=j^{-1}=j^4. This uses
`j^4=-1-j-j^2-j^3`; it introduces no alternative encoder.

Both piston sums are 1 in F5. For arbitrary common q_x and r_x, the two
complete sources consequently have the same quotient

\[
Q(x)=(z_x,q_x,r_x),\qquad z_x=\sum p_x+q_x+r_x.
\]

In particular, the original reference preparation `(q_x,r_x)=(0,1)`
gives the original common `Q=(2,0,1)`.

Prepare one common receiver with

\[
Y_p=I_2,\qquad p_y=(1,0,0,1),\qquad r_y=0.
\]

The value q_y is arbitrary. The bit eta is arbitrary. In every comparison
q_x, r_x, q_y and eta are held common between the two source choices.
There is one fixed word for both choices, with no message-dependent
selection of the word, reference or endpoint reader.

## 3. The existing mixed predicate distinguishes the pair

Use exactly the declared function

\[
h(X_p,Y_p)=\frac{\det(X_p+Y_p)-\det X_p-\det Y_p}{2},
\qquad \delta=1-h^4.
\]

Since

\[
\det(X_p+I_2)=\det X_p+a+d+1,
\]

the common receiver makes `h=(a+d)/2`. Therefore

\[
h(p_+,I_2)=0,\qquad h(p_-,I_2)=4,
\qquad \delta_+=1,\quad\delta_-=0.
\]

Here `1/2=3` in F5, and every nonzero field element has fourth power 1.
The predicate depends only on the actual piston coordinates. It does not
read the algebraic labels j or j^{-1}, and it is independent of q_x,
r_x, q_y, r_y and eta.

## 4. Exact contact and complete occupied-reference map

Retain the Canon definitions

\[
I_b=b_xb_y,\quad E_b=W_bI_bW_b,\quad
\tau_i=e_id_i,\quad K_i=[E_b,\tau_i],\quad
A_i=\mathcal U_iK_i\mathcal U_i.
\]

The inherited W_b control is the involution

\[
W_b(s,\eta)=
\begin{cases}
(s,\eta),&h(s)=0,\\
(I_b^{\sigma(h(s))\mathbin\oplus\eta}s,\sigma(h(s))),&h(s)\ne0,
\end{cases}
\]

where `sigma(1)=sigma(2)=0` and `sigma(3)=sigma(4)=1`.
The paired source identity is `h(I_b s)=-h(s)`.
Consequently E_b acts as I_b on h=0 and, on h!=0, fixes the data and
flips eta. The native word tau_i fixes every other coordinate and
translates q_i by 1.

On h=0, the commutator therefore sends q_i to q_i-2=q_i+3. On h!=0,
the two translations cancel and the two bit flips cancel. In both
cases the complete factor

\[
f=(p_x,p_y,r_x,r_y,\eta)
\]

is restored. The other q coordinate is unchanged. This gives the exact
complete map

\[
K_i(f,q)=(f,q+3\delta e_i).
\]

The actual chronological twelve-leaf expansion of K_i is

```text
e_i, d_i, W_b, b_x, b_y, W_b,
d_i, e_i, W_b, b_y, b_x, W_b.
```

The reader coupling is the existing involution
`Ucal_i:r_i -> P_(q_i)(r_i)`, fixing all other coordinates, with table

| q | P_q(0), P_q(1), P_q(2), P_q(3), P_q(4) |
| --- | --- |
| 0 | 0, 2, 1, 3, 4 |
| 1 | 0, 1, 2, 3, 4 |
| 2 | 2, 1, 0, 3, 4 |
| 3 | 1, 0, 2, 3, 4 |
| 4 | 1, 0, 2, 3, 4 |

Because Ucal_y changes no piston, its preliminary action changes neither
h nor delta. Thus, on every complete input, including occupied r_y,

\[
q_y'=q_y+3\delta,\qquad
r_y'=P_{q_y+3\delta}P_{q_y}(r_y).
\]

The full inverse uses the unchanged terminal pistons to recover delta,
and then

\[
q_y=q_y'-3\delta,\qquad
r_y=P_{q_y'-3\delta}P_{q_y'}(r_y').
\]

Every other coordinate is restored. In particular, the entire source
`(p_x,q_x,r_x)`, the receiver pistons p_y, and eta are unchanged at
completion, not merely equal under a quotient or endpoint readout.

The table gives `P_(q+3d) P_q(0)=d` for every q in F5 and d in {0,1}.
One initial preparation r_y=0 therefore yields

\[
\boxed{r_y'=\delta,\qquad q_y'=q_y+3\delta.}
\]

For the frozen phase pair this is a genuine write into the same initially
prepared receiver:

| Source | Final q_y | Final r_y |
| --- | --- | --- |
| j | q_y+3 | 1 |
| j^{-1} | q_y | 0 |

For q_y=0, the complete receiver endpoints are respectively
`(1,0,0,1,3,1)` and `(1,0,0,1,0,0)`.
No condition r_x=0 is used. The original r_x=1 is admitted by the
complete CONTACT-RECORD map; the stronger joint preparation of the
separate RESIDUAL-STEP-RECORD theorem is not imported here.

## 5. Retention through another declared interaction

After the write, consider the complete word A_x or its inverse on the
same two cells. No clean-state assumption on r_x is imposed.

Every literal leaf of A_x acts on r_y by one of the following rules:

| Leaf | Action on r_y |
| --- | --- |
| Ucal_x, e_x, d_x, b_x | fixes r_y |
| b_y | sends r_y to -r_y |
| W_b | fixes r_y or sends r_y to -r_y |

Each leaf therefore preserves r_y^2 on the entire carrier. All these
leaves are involutions, so the reversed inverse leaf sequence has the
same property. Hence every forward or inverse literal prefix preserves

\[
\boxed{r_y^2.}
\]

At the complete A_x endpoint, even the raw r_y is restored: K_x restores
the full factor and both Ucal_x leaves fix r_y. The first record remains
distinguishable during all these prefixes by its fixed square readout.

This protection is not asserted inside an unspecified physical
implementation of W_b, under arbitrary other gates, or through arbitrary
future native waiting. It proves retention during one precisely named
subsequent interaction, not a second independently loaded message.

## 6. Exact quotient-compatible comparison envelope

For any fixed finite number of complete native cells define

\[
\pi(x_1,\ldots,x_m)=(Q(x_1),\ldots,Q(x_m)).
\]

A map F is pi-compatible when `pi F = Fbar pi` for a fixed quotient
map Fbar. Such maps preserve the equivalence relation `pi X=pi X'`,
and their finite compositions do so by substitution.

The comparison envelope includes the following operations and only
controls satisfying the restrictions stated below:

1. Slotwise original g_i and their inverses. The five quotient maps are
   `(z,q,r)`, `(-z,-q,-r)`, `(2-z,1-q,-r)`,
   `(2-z,1-q,1-r)`, and `(3-z,2-q,1-r)`.
   Each generator is an involution.
2. Actual forward U steps at common counters and common theta values.
   The selected generator depends only on z and that common driver.
   No inverse of the nonsurjective complete U is assumed.
3. Complete-cell CSUM operations and their inverses. The map
   `P(x,y)=(x,y+x)` sends `(Q_x,Q_y)` to `(Q_x,Q_y+Q_x)`;
   `Q_cs(x,y)=(x+y,y)` sends it to `(Q_x+Q_y,Q_y)`.
   Inverses use subtraction.
4. Exchanges of complete cells, included explicitly in this comparison
   envelope, which just exchange quotient blocks. Their inclusion here
   does not assert an additional native compilation theorem.
5. Ucal_i, whose quotient action is

   `(z_i,q_i,r_i) -> (z_i-r_i+P_(q_i)(r_i),q_i,P_(q_i)(r_i))`.

Common counters, an arbitrary common initial controller memory, and
source-independent common auxiliary input may be included. A controller
may select the next operation from the envelope using its own memory
and the pi history. Its memory update, guards, refusals and stopping
condition must also use only those data. Induction then gives the same
controller state, operation choice, quotient history and stopping
decision from pi-equivalent initial states.

It follows that no fixed readout of the resulting q,r histories and
such controller memory distinguishes the two original source choices
when all added cells and controller resources are prepared commonly.
The same statement holds for any fixed functional of the complete
quotient history. This is a scoped composition invariant, not a
blanket no-transmission theorem.

### Why the conclusion must not cover all receiver pistons

Take the complete-cell shear P with one common receiver y=0. It gives

\[
P(x_+,0)=(x_+,x_+),\qquad
P(x_-,0)=(x_-,x_-).
\]

The receiver's second piston is now 1 versus 4. Its Q remains the same
between the two executions. Thus this admitted algebraic shear is an
explicit counterexample to replacing the q,r conclusion by equality
of the full receiving cell. In particular, hidden piston information
can move while remaining hidden from the declared quotient.

### Where the positive contact leaves the envelope

For the common receiver I2, the two source choices have the same pi but
h=0 versus h=4. At eta=0, W_b is the identity on the first case and
applies I_b and writes eta=1 in the second. For the original references,
the resulting quotient states differ. Hence W_b is not pi-compatible.

K_y converts this already declared piston-sensitive control into a
q_y displacement. Ucal_y is separately pi-compatible; its role is to
write that displacement into the prepared r_y reference. There is no
contradiction with the quotient theorem: the positive word uses an
operation outside its explicitly defined envelope.

A passive change of coordinates does not supply this operation. A
recharting must transport both pi and the readout. Reusing the old
readout formula after changing which physical coordinates it accesses
would instead specify another interface requiring its own admission.

## 7. The exact mu_5 partition, not a complete phase reader

With the same coefficient map and receiver I2, the complete table is

| Source | a+d | h=(a+d)/2 | Written delta |
| --- | --- | --- | --- |
| 1 | 1 | 3 | 0 |
| j | 0 | 0 | 1 |
| j^2 | 0 | 0 | 1 |
| j^3 | 1 | 3 | 0 |
| j^4 | 3 | 4 | 0 |

The contact separates `{j,j^2}` from `{1,j^3,j^4}`. It separates the
frozen j versus j^{-1} pair, but it does not recover all five phase
labels or the complete algebraic mixed quantity C(alpha).

## 8. Product use has explicit resources

Two independently addressed copies use four complete native cells and
two copies of the declared eta bit:

\[
\mathcal X\times\mathcal X
=\mathbb F_5^{24}\times\{0,1\}^2.
\]

Applying A_y to each copy gives its own bit delta from that copy's
specified common receiver preparation. Every leaf acting only on the
second copy fixes the entire first copy. This elementary product
composition is distinct from the within-pair retention theorem above.

The four cells and two bits are explicit resources. Their product and
addressed fixed-word schedule are not derived from one autonomous U.
This statement supplies no later source-loading operation, fresh
archive on indefinite repetition, or physical renewal mechanism.

## 9. Syntactic controls and remaining scope

Deleting every W_b symbol is not the same statement as physically
disabling a calibrated source-sensitive interaction. In the resulting
explicitly different word E_b is replaced by I_b, and

\[
[I_b,\tau_y]:q_y\longmapsto q_y-2=q_y+3
\]

on all inputs, independently of h. Together with the unchanged Ucal_y
leaves this writes a constant 1 from r_y=0. Such a fixed cycle can be
mathematically useful; it is not an identity operation or a physical
control condition established by this proof. Any audit using a
syntactically modified word must define that word and its comparison
claim explicitly before execution.

Sections 1-9 establish the exact declared contact and retained native
record. The following composition supplies an explicit downstream
connection, preparation and guard bound.

The result does not assert physical photon identity, an energy cost,
a source-depletion process, a completion flag, an occurrence law,
autonomous native implementation, or any L2-L6 lift. In particular,
the zero branch of the completed A_y can coincide with the unused full
state, and repeating A_y can erase its earlier record. These existing
CONTACT-RECORD boundaries remain unchanged.

## 10. Actual composition with the existing funded receiver

Use two original source cells and two receiver cells, with the two
declared bits from Section 8. Identify the two receiver cells, in their
unchanged six-coordinate order, with the native heads x_A and x_B of
P-TWO-USE-TYPED-READOUT-CLOSURE-1. The complete joined carrier is

\[
(\mathbb F_5^6)^2\times\{0,1\}^2\times Z_B.
\]

Here Z_B is that existing complete apparatus carrier, including both
native heads, n, c, wave coordinates, four tape blocks, the tape pointer,
work and stock ledgers, capacity, both acceptance signs and buffer d.
There are four native cells total, not six. Neither the contact module
nor the downstream apparatus is changed. Their native b,d,e maps agree
in the same coordinate order; the verifier checks their affine basis
certificates.

Initially both receiver heads are the common `(1,0,0,1,0,0)`. The
original sources alone contain the two chosen piston inputs with their
original `(q,r)=(0,1)`. All wave and tape entries are zero, n=c=k=0,
W=0, b=B=2, both signs are +1, both added bits are zero and d=(0,0).
This common head r=0 is explicitly different from the old helper's
p-only preparation with head r=1. It is chosen commonly before any
source-sensitive transition.

For each lane, every one of the fourteen literal A_y leaves updates
that lane's original source, its bit and its actual shared head in the
joined state. There is no assignment of a precomputed contact endpoint
or eta vector. Each leaf fixes the downstream classical apparatus and
the old n,c. At prefix completion, original sources and added bits are
restored. The original sources then remain spectators.

This fixed 28-leaf prefix and the following seven existing coupled
updates are an explicitly addressed finite composition. The old c in
Z/8 controls only its original seven-step part. No autonomous controller
for the prefix, energy law for its native gates or physical source
acquisition is supplied by this composition.

### 10.1 The actual source vectors after the first native tick

The two possible head endpoints from Section 4 have quotients

\[
Q(y_+)=(1,3,1),\qquad Q(y_-)=(2,0,0).
\]

At the common initial counter n=0 the old U therefore selects g_1
for y_+ and g_2 for y_-. Its actual q,r outputs are respectively
(2,4) and (1,0). The unchanged balanced lift then gives

\[
z_+=(1,0,0,0),\qquad z_-=(1/2,1/2,0,0).
\]

These are the sources consumed by the first funded contact and by the
unchanged second-source buffer capture. They are not the eta values at
the earlier A_y endpoint before U. Both original source choices are
present before the finite word starts; the later funded contact uses
its existing captured buffer. This is not an independently arriving
second message.

### 10.2 A capacity chosen without fitting a trajectory

For the unchanged injection S and s=sum(z), its four port entries are
z_i-s/5 and its fifth entry is -s/5. Thus

\[
\|Sz\|^2=\|z\|^2-s^2/5.
\]

On a cold wave/tape state, the positive signed velocity kick has energy

\[
e_+=\tfrac12\|Sz_+\|^2=\tfrac25,
\qquad e_-=\tfrac12\|Sz_-\|^2=\tfrac3{20}.
\]

The inherited full energy is

\[
E(X)=\tfrac12(\|u\|^2+\|v\|^2-u^THv)
 +2(\|A_0\|^2+\|A_1\|^2+\|B_0\|^2+\|B_1\|^2).
\]

For completeness, H is symmetric with diagonal 10/9 and nonnegative
off-diagonal entries. Its five stencil shells have multiplicities
12,6,12,24,6 and weights 6,1,15,1,1 divided by 324. Their total is
8/9, and the principal Dirichlet restriction only removes off-diagonal
entries. Every absolute row sum of H is therefore at most 2, so
`||H||_2<=2`. Cauchy-Schwarz gives
`|u^T H v|<=2||u||||v||`, proving the displayed energy is nonnegative.
The unchanged free/tape update preserves it by the inherited exact
quadratic identity. Consequently its square root is a seminorm, and the
sum of any two transported kicks in this frozen family satisfies

\[
E(X)\le(\sqrt{e_A}+\sqrt{e_B})^2\le\tfrac85<2.
\]

The classical contact books exactly its energy difference into W and
subtracts it from b, so E=W and b+W=2 hold from the common cold initial
state. After the first contact the candidate second contact therefore
has b'=2-E' in [0,2]. Both guards accept for the common B=2, regardless
of the four ordered choices. The verifier still checks the actual
guards, exact accounts and bound at all eight downstream boundaries.

This account pays only for the declared classical wave/tape contacts.
It does not assign an energy to W_b, Ucal, the native prefix, its control,
the reference preparation or its renewal.

### 10.3 A distinction read from records after both contacts

Execute exactly the unchanged seven-step apparatus word and retain its
eight boundaries. Its native and calendar counters must be

`(0,0),(1,1),(1,2),(2,3),(3,4),(3,5),(4,6),(5,7)`.

The actual tape-cut vectors are B0 at boundaries 3,4,6,7. At completion
they occupy `(A0,A1,B1,B0)`, respectively. In particular, the first two
are retained through the second contact. Holding the first original
source fixed and changing only the second leaves wave/tape history
unchanged through boundary 4; its influence begins at its actual
contact at boundary 5.

Apply the existing `extract_direct_port_readout` with d omitted and
the existing `direct_source_reader` to that record object. The reader
receives only the actual final `(A0,B1)` tape vectors and the declared
acceptance signs. It receives no source, native head, buffer, phase
label or complete apparatus state. Its inherited exact factorization
recovers the accepted z_A and z_B. For the frozen pair family these
are independently z_+ or z_-, so the four ordered inputs give four
distinct actual retained record pairs.

The executable audit follows the entire path, from each original
source through actual contact leaves, the shared native heads, actual
U, the old eta and S, funded acceptance, wave/tape updates, and the
unchanged record-only reader. It does not establish native acquisition
or physical implementation of the supplied interfaces. It establishes
that this explicit declared composition carries the specified lost
distinction all the way to its actual retained record port.

## 11. Public mathematical dependencies

All dependencies are read at the public authority base named above:

- `DEF-RESIDUAL-CONTACT-ARCHITECTURE`: complete carrier, piston reshape,
  mixed predicate, original letters, CSUM maps, W_b and Ucal_i.
- `CONTACT-RECORD` [T]: complete K_i and A_i maps and inverses, ready
  record, literal-prefix protection and repeated-use boundaries.
- `U-NATIVE-APPARATUS-HISTORY-FACTOR` [T] and
  `U-CONTACT-SOURCE-NONINTERFERENCE` [T]: the unchanged native quotient
  and original source-interface information boundary.
- `ALGEBRAIC-RESIDUAL-REALIZATION` [T]: the accepted extended alphabet;
  its large compiled residual word is not used here.
- `P-TWO-USE-TYPED-READOUT-CLOSURE-1/SOURCE_PROOF.md`: inherited
  full-carrier funded contact, nonnegative quadratic energy, free/tape
  invariance and exact seven-step records.
- `P-TWO-USE-TYPED-READOUT-CLOSURE-1/PROOF.md`: the existing typed
  record-only factorization. Both files are under `probes/` and pinned
  in SOURCES.tsv; source reuse is not independent evidence.

Normative source:
https://github.com/mathorn1973/twist-j/blob/dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d/canon/CANON.md

Registry:
https://github.com/mathorn1973/twist-j/blob/dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d/canon/REGISTRY.tsv
