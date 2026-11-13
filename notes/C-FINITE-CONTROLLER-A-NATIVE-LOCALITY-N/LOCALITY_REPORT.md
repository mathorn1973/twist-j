# Native realizability audit of finite local controller A

**NON-CANONICAL. L1 analytical draft. Independent acceptance pending.**
Candidate: C-FINITE-CONTROLLER-A-NATIVE-LOCALITY-N.
Reservation: [issue 1742](https://github.com/mathorn1973/twist-j/issues/1742).
Authority: Public Canon v105 at
[892a0b11089d34e241e1eb76d2c03247022d18e6](https://github.com/mathorn1973/twist-j/tree/892a0b11089d34e241e1eb76d2c03247022d18e6).
The source/scope protocol was published at
[896b4792e2c9028197bc0a0203eec19f784b7331](https://github.com/mathorn1973/twist-j/commit/896b4792e2c9028197bc0a0203eec19f784b7331).
No scientific program was executed.

## 1. Result and route table

The supplied A construction gives a reversible, charge-conserving local
machine **after its extra gate alphabet, ready resources, enlarged cells
and programmed head law are admitted**. It does not supply a compiler of
that machine from the unchanged occupation law or original checkpoint law.
Native realizability at that broader scope remains **OPEN**.

There are three exact narrower obstructions and one current-scope
qualification below. None is a general impossibility theorem. In particular,
an admitted enlarged construction need not be forced by J to be a valid
conditional mathematical model.

Here PROVED_AT_STATED_SCOPE and OBSTRUCTED_AT_STATED_SCOPE describe authored
analytical arguments, not new public Canon statuses.

| Route and exact class | Verdict | Reason |
| --- | --- | --- |
| Code only: arbitrary bounded-local charge-compatible encoding into original occupation cells | OPEN | No complete encoding is supplied; locality radius, cut correspondence and resources must be fixed. |
| Code only: tensor-local radius-zero encoding, original 38-coordinate cell, identical local charge, no added charged ancillas, complete A10b head domain | OBSTRUCTED_AT_STATED_SCOPE | Charge-10 cell dimension is smaller than the required number of head phases, Section 5. |
| Funded ancillas in the existing identity-spectator extension, unchanged occupation evolution | OBSTRUCTED_AT_STATED_SCOPE for operating those ancillas | Every spectator observable is conserved, while SUM and head advance change them, Section 6. |
| Funded ancillas with another active encoding and unchanged allowed evolution | OPEN | Neither a full compiler nor a complete-class obstruction is supplied. |
| Enlarged cell and changed law: the declared local gates and full one-head A10b law | PROVED_AT_STATED_SCOPE for the conditional gate construction | Complete inverse, charge and local support follow from the displayed operators; the ring current needs Section 8's seam qualification. This is not native or physical admission. |
| Original checkpoint: timeless injective state intertwiner of the complete cyclic A10b machine into a fixed positive number of actual checkpoint ticks | OBSTRUCTED_AT_STATED_SCOPE | A10b has periodic full states; the actual native counter strictly increases, Section 7. |
| Original checkpoint: finite-horizon, time-indexed, restricted-domain or history/readout relation | OPEN | A separately typed encoding, actual selector trajectory, inverse/account and spatial dictionary are missing. |

## 2. Three different laws and their source authority

Use distinct notation throughout.

1. \(U_{\rm cp}\) is the original autonomous checkpoint evolution
   \[
   \Omega=\mathbb N_0\times\mathbb F_5^6,\quad
   U_{\rm cp}(n,\psi)=(n+1,g_{\sigma(n,\psi)}\psi),\quad
   \sigma=z_6(\psi)+2(s_2(n)\bmod2)\pmod5.
   \]
   The five generators are the registered \(a,b,c,d,e\).
   An arbitrarily commanded word in those generators is not automatically
   an actual selector-driven trajectory. The counter is part of the state.
   See the [definition](https://github.com/mathorn1973/twist-j/blob/892a0b11089d34e241e1eb76d2c03247022d18e6/canon/CANON.md#L462)
   and [generator formulas](https://github.com/mathorn1973/twist-j/blob/892a0b11089d34e241e1eb76d2c03247022d18e6/canon/CANON.md#L596).
   This carrier has no supplied physical site lattice for A's neighbor gates.
2. \(U_{\rm rec}\) is the specified Hilbert-space capture/receiver law in
   HOMOGENEOUS-CAPTURE-CURRENT-RECORD. Write \(U_{\rm occ}\) for its
   occupation-space realization. The Canon proves
   \(U_{\rm occ}\mathcal I=\mathcal I U_{\rm rec}\) on the declared
   object/token-or-pulse/receiver sector, with identity on admitted occupied
   helpers and reference. It explicitly treats the coherent amplitudes,
   contact, schedule and preparation as construction data, and excludes
   derivation from \(U_{\rm cp}\). See
   [scope](https://github.com/mathorn1973/twist-j/blob/892a0b11089d34e241e1eb76d2c03247022d18e6/canon/CANON.md#L27430),
   [codes](https://github.com/mathorn1973/twist-j/blob/892a0b11089d34e241e1eb76d2c03247022d18e6/canon/CANON.md#L27479),
   and [intertwiner](https://github.com/mathorn1973/twist-j/blob/892a0b11089d34e241e1eb76d2c03247022d18e6/canon/CANON.md#L27986).
3. \(U_{\rm A}\) is the new finite programmed track machine of A1b/A10b.
   It uses \(N=32768\) periodic sites, new constituent tracks, extra
   registers and an \(M\)-phase head. Its completed native segments satisfy
   \(U_{\rm tracks}E_{\rm code}=E_{\rm code}U_{\rm rec}\) on the promised
   same-parity support cone. This is an equality to the already specified
   capture law, not a compiler from \(U_{\rm cp}\), nor a local dictionary
   from every intermediate A state into the original occupation carrier.

The source proposal states these distinctions itself. Its word “native”
for a resumed capture segment cannot license every new primitive.
The prior [issue 1741 dossier](https://github.com/mathorn1973/twist-j/issues/1741#issuecomment-6385322783)
likewise leaves allowed gate implementation and reset resources open.
Its coefficient analysis does not turn localized amplitudes into faithful
raw characteristic-five registers.

## 3. Full state and the admitted operation inventory

The complete A carrier retains both working banks, object coin lanes,
token/pulse labels and banks, receiver, all source/query/outcome/payload
registers, bus, marker helpers, head phase and position, archived information
and arbitrary untouched reference. Its initial code has one A and one B
constituent per working bank, but its full local tensor carrier includes
temporary zero/two objects or carriers in a bank during local bank swaps.

Sequential streaming may also produce unequal A/B position parities.
Then \(R=(x_A+x_B)/2\), \(r=(x_A-x_B)/2\) need not be integers.
These are valid physical-track states in A, not states to discard or
silently identify with a canonical phase-zero source slice.
The Canon explicitly supplies no asynchronous or arbitrary-occupation
extension at [the native scheduling boundary](https://github.com/mathorn1973/twist-j/blob/892a0b11089d34e241e1eb76d2c03247022d18e6/canon/CANON.md#L27534).

| Operation | Inherited content | Additional permission required by A |
| --- | --- | --- |
| Object coin, coincidence phase, contact, pulse coin/edge and receiver label exchange | Specified factors of \(U_{\rm rec}\) on its declared sector | Individually address them, select their order, complete them on new local occupation sectors and control them coherently. |
| Five-state Fourier \(H_5\), \(H_5^*\) | No general helper actuator follows from a fifth-root scalar or a five-element alphabet | Apply \(H_{5,kj}=\zeta_5^{kj}/\sqrt5\) to a charged logical register. |
| SUM5/SUM26, inverse subtraction, logical SWAP | Equal-charge codes allow these as mathematical charge-preserving unitaries | Admit the actual interactions between the encoded registers. |
| Controlled \(W,W^*,T_R,T_R^*\), relative phases | The unconditional \(W\) and source-coordinate translation are specified mathematical operators | Coherent branch-selective access, including adjoints, controlled local gates and a distributed bus. |
| Zero tests, prefix AND/XOR, outcome transposition | Classical predicates have reversible circuit extensions | Admit those state-sensitive gates, charged scratch and routing; preserve all failure branches. |
| Head translation and phase advance | No \(M\)-phase moving head is present in the original model | The position-specific A10b transition table and local phase capacity. |
| Detector hold and archive isolation | Native segments continue under \(U_{\rm rec}\) | Programmed identity on selected carrier/receiver/archive tracks while other tracks evolve. |
| Active/reserve exchange | Old-memory exchange on the existing receiver edge is inherited | Exchange every complete working bank component with a supplied reserve; this is a different operation. |

Thus native realizability fails to be *established already at the first
unprovided actuator*, such as \(H_5\) or SUM5 on a new helper.
It is not enough to prove that a gate conserves charge or that an encoding
is monomial. Neither fact identifies the gate with allowed dynamics or
bounds the support of its conjugate under an encoding.

## 4. What is verified within the enlarged gate model

These are direct analytical checks, with no executable audit.

**Logical gates and dirty bus.** SUMd sends
\((c,t)\mapsto(c,t+c\bmod d)\); subtraction is its total inverse.
A controlled unitary \(\sum_j|j\rangle\langle j|\otimes V_j\) is unitary
with adjoint \(\sum_j|j\rangle\langle j|\otimes V_j^*\).
The chosen coin and rotation blocks are unitary, and identity on an
orthogonal complementary sector gives a total unitary on that local carrier.

Let \(B\) be the broadcast SUM word. On ready bus \(0^N\),
\[
B\sum_j|j\rangle_c|0^N\rangle_b|\psi_j\rangle
 =\sum_j|j\rangle_c|j^N\rangle_b|\psi_j\rangle .
\]
After gates controlled by the unchanged local bus values, \(B^*\) restores
the bus exactly and leaves \(\sum_j|j\rangle V_j|\psi_j\rangle\).
An arbitrary reference can be included in each \(\psi_j\).
This is coherent basis fanout. It does not clone an unknown quantum state.
On dirty bus input the word remains invertible, but the displayed ready
query semantics need not hold. The dirty contents cannot be discarded.

**Local motion and inverse.** On-site lane exchange followed by the
disjoint bond exchanges (plus at x with minus at x+1) sends a plus particle
one site left and a minus particle one site right. Together with the coins
and coincidence phase this gives \(W\) on the completed code.
Descending adjacent whole-track swaps implement the finite cyclic
translation \(T_R\); reversing their exact order implements its inverse.
The finite-ring construction agrees with the infinite native law only
when the whole intervening data support avoids the seam, as A promises.

**Marker and bank exchange.** Each prefix operation
\(b_{j+1}\mathrel{\mathrm{XOR}}=b_j[f_j=0]\) is an involution.
Compute, use the final predicate to transpose Q states 0 and 1, then
uncompute every predicate/routing helper in reverse order.
The controls remain, so the helpers return on the ready domain even for
entangled data and rejected branches. Q states 2,3,4 are retained.
No receiver-value or object-box test is inserted.
This marker agrees with the predecessor only on the stated original
input cone; its off-family extension is a new choice.

Local bank SWAP is total on both banks; it retains the temporary zero/two
occupation sectors. Native evolution resumes only at the completed boundary.
For \(W_A=\mathrm{SUM}_{26}(D,R_A)V_{X_A,D}\) and complete X-bank exchange S,
the two-use word and inverse are
\[
V_{\rm two}=W_A S W_A,\qquad
V_{\rm two}^{-1}=W_A^{-1}S W_A^{-1}.
\]
D is shared and is not erased. The reserve is a supplied ready state, not a
reset of the previous output. These operator identities cover arbitrary
occupied memory and reference, without asserting the separate B/C event
or weight claims.

**Complete one-head extension.** Let
\(d_k=\ell_{k+1}-\ell_k\in\{-1,0,1\}\), with a closed linear head path,
and define, with periodic position arithmetic,
\[
U_{\rm A}|k,x\rangle|\psi\rangle
 =|k+1\bmod M,x+d_k\rangle G_{k,x}|\psi\rangle,\qquad
G_{k,x}=\begin{cases}g_k&x=\ell_k,\\I&x\ne\ell_k.\end{cases}
\]
Its inverse, on an output \((k',x')\), recovers
\(k=k'-1\bmod M\), \(x=x'-d_k\), then applies \(G_{k,x}^*\).
The head-label map is bijective and every block is unitary, so this
proves the full one-head inverse, not merely a ready-orbit inverse.
The offset \(x-\ell_k\bmod N\) is conserved. Nonzero offsets act identically
on data. Each nontrivial data operation is next to the head.
No multi-head extension or spatially homogeneous transition law follows.

## 5. Exact obstruction to one unchanged cell per site

Freeze the following subclass: a tensor-local radius-zero isometry into
one original \(\ell^2(\mathbb Z^{38})\) cell at each same physical site;
exact site-charge preservation; no extra charged ancillas; and the complete
A10b domain, including arbitrary head phase at every position. Preserving
all physical cut charges implies preserving each site charge by taking
differences of adjacent cuts.

Choose site 0, outside the flag/prefix tape and away from source 99 and
receiver 100. Put all objects and carriers elsewhere and fix all other
states. Its five-state bus and three marker transport registers each
carry charge two, hence local charge eight. Put the single charge-two
head at site 0. The \(M\) different head phases are orthogonal inputs
of the same local charge ten.

The original charge-ten sector has dimension
\[
D=\#\{h\in\mathbb Z^{38}:\sum_\alpha h_\alpha^2=5\}
 =2^5\binom{38}{5}+4\cdot38\cdot37
 =16\,067\,768.
\]
There are exactly two cases: five entries of magnitude one, or an entry
of magnitude two and a distinct entry of magnitude one.

The declared compiler lists every elementary gate as a separate head
phase. A query uses \(N\) broadcast and \(N\) inverse-broadcast gates;
already one set of 8750 queries therefore requires
\[
M\ge K\ge2N\cdot8750=573\,440\,000>D.
\]
The remaining gates and head travel can only increase M.
No isometry can map these M orthogonal states into that D-dimensional
sector. This is an exact dimension argument, not an enumerated search.

The result does not exclude positive-radius/block encodings, extra funded
charge, larger cells, a different compiler or restricting the full head
domain to a nominated history. Each changes a frozen premise. Moving charge
into neighboring cells must also re-establish the requested physical-cut
correspondence. It cannot be presented as this radius-zero realization.

## 6. Exact boundary of funded identity spectators

The established helper extension is \(U_{\rm occ}\otimes I_h\).
For every helper observable B and every fixed nonnegative integer t,
\[
(U_{\rm occ}^{t}\otimes I_h)^*(I\otimes B)
(U_{\rm occ}^{t}\otimes I_h)=I\otimes B.
\]
Supplying more occupied helper states changes charge and capacity but
does not change this identity.

For example, with helper basis input \(|1,0\rangle\),
SUM5 makes the target-zero projector change from expectation one to zero.
A head phase advance also changes phase projectors. These operations
therefore cannot be implemented on those very spectator registers by
unchanged occupation evolution, however many ticks it runs.
The same issue applies to modifying a spectator outcome or archive bank.

This obstruction is to the inherited identity-spectator placement. A
different encoding into active degrees of freedom might avoid it. No
universal statement about every funded encoding follows.

## 7. Original checkpoint counter and inverse

A nonzero-offset orbit of A10b executes identity on all data. After M
ticks the head phase returns and its displacement is \(\sum_k d_k=0\).
Thus some complete controller states satisfy \(U_{\rm A}^M s=s\).

Suppose a timeless injective state map E into the actual checkpoint carrier
obeys \(E U_{\rm A}=U_{\rm cp}^{\tau}E\), with a fixed positive integer
tick conversion \(\tau\), on the complete A10b domain. Iterating gives
\[
U_{\rm cp}^{\tau M}E(s)=E(s).
\]
The first coordinate on the left has increased by \(\tau M>0\),
a contradiction. This excludes that exact all-time state relation.
It does not treat \(\Omega\) as only \(5^6\) states, and it does not exclude
a finite-horizon or time-indexed simulation, a counter quotient, a
history reader or a different carrier.

There is a separate inverse warning. The Canon
[records literal selector collisions](https://github.com/mathorn1973/twist-j/blob/892a0b11089d34e241e1eb76d2c03247022d18e6/canon/CANON.md#L9673):
at drive bit zero,
\[
F_0(0,0,1,0,0,0)
 =F_0(3,1,3,4,1,1)
 =F_0(3,1,3,4,2,1)
 =(4,0,0,0,0,0).
\]
At the same initial counter these also have the same next counter.
Thus the actual full-domain checkpoint update has no inverse, despite the
individual generators being permutations. A reversible extension retaining
that literal update needs at least three distinguishing output records
for this one step. It adds state and does not prove reusable implementation.
Restricted common-ready subsets can behave differently; the Canon
[explicitly retains such restricted results](https://github.com/mathorn1973/twist-j/blob/892a0b11089d34e241e1eb76d2c03247022d18e6/canon/CANON.md#L5134).

## 8. Complete charge, current and the ring seam

All named logical values of a register have the same charge. Coins,
Fourier gates, controlled rotations and logical permutations therefore
preserve their stated charge sectors. Every contact pair has total
charge eight. Object/carrier routing preserves total charge; the head
remains one charge-two occupation. This is a charge account, not a
spectral-energy or physical-work account.

For full right-region charge N_R and each elementary g, use
\[
j_g=g^*N_Rg-N_R.
\]
With \(G_k=g_{k-1}\cdots g_0\), \(G_0=I\),
\[
G^*N_RG-N_R=\sum_kG_k^*j_{g_k}G_k.
\]
Insertion of the consecutive prefix charge differences proves the
telescoping identity, including all coherent cross terms.

The full N_R includes both working banks, receiver, flags, bus, helpers,
archives and head. Equal-charge logical SUM and co-located bank SWAP
have zero cut current. Neighbor SWAPs of always-occupied equal-charge
logical registers can transport information with zero charge current.
Object/carrier transport and the moving head can have nonzero current.
The native data-current theorem alone omits these controller contributions.

There is an essential qualification on the complete periodic carrier.
Define \(\theta(x)=1_{x\ge100}\) on the chosen coordinate representatives
\([-16384,16383]\), and let N_R,data count all non-head tracks.
The full one-head current is exactly
\[
\sum_{k,x}|k,x\rangle\langle k,x|\otimes
\left(G_{k,x}^*N_{R,\rm data}G_{k,x}-N_{R,\rm data}
 +2[\theta(x+d_k\bmod N)-\theta(x)]I\right).
\]
Here “mod N” returns the chosen coordinate representative.
The bijective head output labels remove cross-head blocks; the formula
also applies to coherent head/reference inputs.

**Exact seam witness.** The nominated path has a right-moving phase
with \(d_k=1\) and \(\ell_k<16383\). Take the admitted offset state
\(|k,16383\rangle\). It is not at the programmed anchor, so \(G_{k,x}=I\).
It moves to \(|k+1,-16384\rangle\); the right-region charge changes by
\(-2\), although no charge crossed the physical bond 99/100.
It crossed the periodic seam.

Consequently A11/A12 remain correct charge-variation identities, but
on the *complete ring domain* they measure a right arc with two
boundaries, not current solely through bond 99/100. For a single-bond
interpretation one must retain the no-seam promise for all moving
subsystems, including the head, or separate the seam flux explicitly.
The nominated linear head path and promised native data cone meet that
restriction; arbitrary offset head sectors do not. This qualification
does not invalidate unitarity or the telescoping algebra.

## 9. Controller resources, hold and archive duration

The declared charge ledger can be verified directly:

| Resource | Charge |
| --- | ---: |
| One X bank: object pair 4, carrier 4, 8750 query flags, source flag, outcome Q, payload R | \(4+4+2(8750+3)=17514\) |
| Two X banks and one shared receiver D | \(2(17514)+2=35030\) |
| One five-state bus per site | \(2N=65536\) |
| Three transport bits per site and 8753 prefix bits | \(2(3N+8753)=214114\) |
| One head | \(2\) |
| Complete declared ready apparatus | \(314682\) |

Any occupied reference or extra spectators add their charge. Logical zero
is charged occupation, not vacuum. Fresh second-bank controls and payload
are supplied resources; preservation of first output is not their manufacture.

Capacity and duration must be charged separately from this scalar.
Each possible head site has M internal phase values plus vacuum; the
complete one-head space has dimension NM. The bus alone has logical
capacity \(5^N\), although it is prepared in one special state.
Every filter flag remains in the full state. No constant-size cell alphabet
or size-independent native clock follows from charge two for the head.

For K elementary data/routing gates, the stated compiler moves at most
N-1 sites before each gate and at most N-1 sites home. Hence
\(M\le NK+N-1\), while \(M\ge K\). The literal construction has
\(M\ge573440000\) already from one filter's broadcast gates.
This is an intentionally inefficient finite architecture, not a practical
time bound or an exact value of M. No full gate list was executed.

During detector work A sets the carrier/receiver factors to identity while
performing object queries. During the designated archive interval no gate
acts on the archived subsystem, so for every archive observable O_A,
\(U_{\rm later}^*(O_A\otimes I)U_{\rm later}=O_A\otimes I\).
This also preserves its reduced state jointly with an untouched reference.
Both facts are consequences of the *new programmed law*.
They do not derive a pause command for unchanged \(U_{\rm rec}\).

The head phase is cyclic. It continues advancing during data hold and can
visit old gates on another lap. A supplies neither an absorbing terminal
halt of the complete state nor indefinite archive protection.
Finite data holding, finite archive isolation and stopping the complete
autonomous system are different requirements.

Finally let \(G=g_{M-1}\cdots g_0\) have eigenvalue \(e^{-i\theta}\).
The phase-by-phase eigenvector recurrence for \(U_{\rm A}\) has roots
\(\lambda^M=e^{-i\theta}\), hence eigenphases
\((\theta+2\pi m)/M\). Nonzero-offset sectors additionally contain the Mth
roots of unity. Thus the old W branch gap is not the whole-controller
spectral gap. A logarithm branch, energy scale and time per head tick
are additional premises. Charge conservation supplies none of them.

## 10. Precise missing native certificate

For an occupation/Hilbert realization, a positive native claim must provide, for each required primitive g:

- A complete isometry E and funded ready ancillas, including rejected
  branches, mixed-parity prefixes, partial bank swaps, occupied memory,
  reference correlations and the chosen full head domain.
- A declared support radius and local alphabet, with explicit dependence
  or independence on N, filter degree and M.
- An actual permitted evolution \(V_g\) and tick conversion satisfying
  \(V_gE=Eg\) on that whole domain. For the original checkpoint route,
  it must follow the actual selector and include the counter.
- Its inverse or retained-information mechanism and exact helper
  restoration; native hold and archive isolation under the same law.
- Intertwining of the actual physical-cut charge observables and currents,
  including controller transport and any boundary seam.
- An explicit distinction between conserved charge, phase capacity,
  spectral energy and physical time.

The checkpoint route instead needs a separately typed state injection into
its actual set-valued carrier, or an explicitly declared linearization or
readout relation. An isometry cannot be demanded of that bare set without
first supplying the Hilbert-space dictionary. The state-injection
obstruction in Section 7 needs no such linearization.

These are specific missing constructions, not a demand for global
uniqueness or for a derivation of every declared model from J alone.
The present inputs supply the gates as new permissions. They do not
supply the certificate above. Native realization therefore remains OPEN;
the narrow negative results state exactly which tempting shortcuts fail.

No Canon claim, Frontier owner, physical event law, residual transport
claim or cross-layer gate is changed by this audit.
