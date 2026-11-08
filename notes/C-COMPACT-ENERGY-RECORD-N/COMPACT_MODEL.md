# A direct 140-gate realization and one finite autonomous clock

**NON-CANONICAL, L1, conditional analytical candidate-T. Independent
acceptance pending.** Author: A. M. Thorn. Apache-2.0.

This construction retains the contact-active equal-spectrum source of
PR #1777 and its complete three-step occupied-receiver output. It replaces
the generic elimination of a 2208-qubit occupation-space unitary by an
explicit factorization on the predecessor's finite coordinate code.
The coordinate code is inherited; the direct bounded-register gate list,
140-gate count and compact autonomous realization are the new statements.

The physical encoding changes. The eleven data registers below store
particle coordinates and internal labels; they are not the spatially distributed occupation
factors of the original model. Locality of the compact register device is
not locality in the simulated particle positions. Its conserved total
Hamiltonian is explicitly given, but is not identified with the nominated
original spectral energy Q=E0 f(U_rec). Initial source, clock and auxiliary
readiness remain supplied. A reversible memory-to-pointer coupling is
included. No thermal preparation, permanent record, physical outcome
selection, external display or renewed stock is asserted.

## 1. Frozen input and eleven physical data registers

The exact inherited source is
[SOURCE_CIRCUIT.md at 191ab035](https://github.com/mathorn1973/twist-j/blob/191ab035be823bd9d6fdc9effba81528fa026e49/notes/C-ORIGINAL-PORT-SOURCE-PREPARATION-N/SOURCE_CIRCUIT.md),
with the unchanged active-source identities in that same tree. Its finite
period-15 closure is already proved to agree with every admitted
preparation prefix and all three subsequent original steps. The closure
is an admitted-input statement, not equality of the finite and infinite
unitaries on arbitrary boundary states or equality of their logarithms.

Use these eleven physical data register factors:

| Register | Dimension | Valid interpretation |
| --- | ---: | --- |
| R | 15 | 0,...,14 represent 90,...,104 |
| r | 15 | 0,...,14 represent -7,...,7 |
| c | 15 | 0,...,14 represent 90,...,104 |
| o | 4 | the four object coin states |
| a | 3 | token, pulse bank 1, pulse bank 2 |
| l | 26 | carrier labels 0,...,25 |
| m | 26 | original receiver labels 0,...,25 |
| q | 3 | LCU qutrit 0,1,2 |
| b | 2 | attenuation bit |
| s | 2 | retained coherent setting |
| d | 2 | physical write pointer, initially zero |

Thus D has dimension 15^3*4*3*26^2*3*2*2*2=657072000. A separate
register-by-register binary representation requires thirty-one bits.
The main model uses the exact dimensions above with no unused binary
codes. These are eleven register sites, not eleven qubits. Put them at
the integer positions 0,...,10. The receiver register represents the
original memory at simulated coordinate 100. Its contents and all
correlations with an arbitrary passive reference remain unknown inputs.
No reference is replaced by a finite classical table.

The ready input has the original basis source
u2=|R=97,r=0,e2;c=97,token,l=0>, q=b=0, arbitrary admitted setting s,
and arbitrary state of m and reference, with d initially zero. Preparation works on all 26
memory labels. Recognition of a fresh d0 write retains the predecessor's
restriction m in span(d1,...,d25).

## 2. Eight explicit factors for every complete spatial step

Write beta=4pi/5 and g_c=2pi/5. On the finite code define these complete
register unitaries. All rotations and phases retain their exact values.

1. **C**, supported on (R,r,c,o,a): on each valid R=c and r=0,
   rotate the two orthonormal states iB tensor token and A tensor
   pulse-bank-1 by [[3/5,-4/5],[4/5,3/5]], identically on l and m.
   All other source states are fixed. Here B=(e2-e3)/sqrt(2) and
   A=(e1-e4)/sqrt(2), exactly as in the source.
2. **M2**, on o: ((I+2iX) tensor (I+2iX))/5.
3. **Q_p**, on a: [[1,-2],[2,1]]/sqrt(5) on the two pulse banks,
   identity on token.
4. **E_rec**, on (c,a,l,m): the receiver-calibrated pulse edge defined
   below; it is the identity on token.
5. **S_R**, on (R,o): cyclic R shifts -1 and +1 for object coins
   e1 and e4, respectively; identity for e2,e3.
6. **S_r**, on (r,o): cyclic r shifts -1 and +1 for object coins
   e2 and e3, respectively; identity for e1,e4.
7. **Gamma**, on r: the phase exp(-i g_c) when r represents zero,
   and identity otherwise.
8. **P_beta**: the scalar exp(-i beta) I, supported on any one register.

For E_rec, index the fifteen valid carrier positions by j=0,...,14.
The uncalibrated E is the direct sum, over j, of the matrix
[[1,-2],[2,1]]/sqrt(5) on the two states
(j,pulse-bank-1), (j+1 mod 15,pulse-bank-2). These pairs are disjoint.
Let T swap the complete 26-dimensional l and m registers when c is one
of the valid positions 100,...,104, and be the identity otherwise.
Define E_rec=T E T. This is a four-register full-space unitary, not a
free controlled whole-lattice operation. Equivalently each edge uses the
label SWAP in its off-diagonal entries exactly when its two endpoints
lie on different sides of that predicate. This includes the finite
closure's wrap edge, whose action is retained on raw boundary inputs.

On the valid code,

    U_fin = P_beta Gamma S_R S_r E_rec Q_p M2 C.       (C1)

This is the inherited finite U_rec, including its receiver calibration.
Indeed T commutes with object gates, since they leave c and labels fixed.
It commutes with Q_p, since that gate preserves c, and with contact C,
because C preserves c and treats every carrier label identically in both
arrangements. Only E is changed by conjugation. The two conditional object
shifts commute and equal the original streaming. This proves (C1) without
discarding a calibration, branch or scalar phase.

Each factor is complete on the entire D, including dirty helpers and
arbitrary boundary-coordinate states. This main model has no unused
binary codes and requires no global test for binary validity. A separate
binary implementation could extend each factor on its local unused codes,
but that would not generally equal the predecessor's globally padded
identity on every invalid binary input. That different raw completion
would require its own specification; it is not silently used here.

A conditional U_fin or U_fin* controlled by one qutrit value uses the
eight controlled factors, reversing and adjointing for the inverse. The
controlled P_beta is a qutrit phase and cannot be dropped. The largest
support is six register sites, from conditional C.

## 3. The full source, occupied-memory and pointer word has 140 gates

Use the exact predecessor preparation word, including attenuation,
amplitude amplification and coherent setting correction. Its 29 named
operations comprise twelve controlled U_rec/U_rec* calls and seventeen
other operations. The setting adds two operations, the output adds
three complete forward steps, and one last gate writes the physical
pointer. Expanding only the source calls by (C1) therefore gives exactly

    M = 12*8 + 17 + 2 + 3*8 + 1 = 140.                  (C2)

This is a constructive register-gate count, not an elementary two-qubit
gate count. No uncontrolled black-box call remains. The non-spatial gates
are the source's explicit matrices and reflections:

- L and L* act on (R,r,c,o,a,l), selecting u2,u3 and fixing their
  orthogonal complement. The unknown memory is not part of this test.
- R and J_minus act on q with their complete qutrit actions.
  T acts on (q,b).
- R_in selects q=b=0 and the fixed source basis state u2, hence acts
  on eight register sites (q,b,R,r,c,o,a,l), excluding m and s.
- S_good acts on (q,b).
- The controlled F acts on (s,R,r,c,o,a,l), and the setting Z acts on s.
- The final V_flag acts on (m,d), by
  V_flag=|d0><d0|_m tensor X_d+(I-|d0><d0|_m) tensor I_d.
  It is a complete two-register unitary. On initial pointer zero it
  correlates the new-write predicate with the physical pointer while
  retaining both outcomes coherently.

The predecessor's unconditioned overall minus can be included in the
first qutrit gate, multiplying its complete three-dimensional action by
-1. This fixes the full word's phase without an additional operation;
it does not alter the phase of a controlled U call. The full preparation
therefore agrees with its declared operator, not only its final density.

All 140 gates G_1,...,G_M are full unitaries on D, of support at most
eight of the eleven physical data registers. On the admitted ready family,

    G_M ... G_1 = V_flag (U_fin^3 V_choice W_prep tensor I_d),            (C3)

with q and b returned to zero. All coherent setting, old-memory and
reference branches are retained. The finite-coordinate support theorem
of the frozen source makes (C3) exactly the original active-source
experiment followed by this pointer isometry on that family. The target
is the full state including d. Discarding d would generally dephase the
old coherent memory output and is not called equality with that old
output. Reading d in its basis gives the same complete two-effect law
as the original receiver effect, with each outcome's post-state and all
reference correlations determined by the displayed isometry. The claim
is conditional on that source
theorem and its exact active contrast

    Delta = 65536(48533-10985 sqrt(5))
            /[5^9(39521+154 sqrt(5))] > 1/50.        (C4)

No new proof or independent acceptance of (C4) is claimed here.

## 4. One positive static Hamiltonian on twelve register sites

Append identity gates G_j=I for M<j<=K, where K=4M=560. Add one
physical clock site of dimension K+1=561 at position 11. Its initial
state |0> is supplied. This site is not 561 hidden clock sites; nor is
its internal dimension declared to be two. The total Hilbert dimension
is 561*657072000, with arbitrary passive reference external to this inventory.

Fix an energy scale g>0 before the dynamics. For 0<=j<K set

    a_j = g sqrt((j+1)(K-j))/(K+1),
    a_-1=a_K=0,
    v_j=g-a_(j-1)-a_j >= 0.

The inequality follows from a_j<=g/2. Define the raw Hamiltonian

    H=sum_(j=0)^(K-1) a_j [
        (|j><j|+|j+1><j+1|) tensor I
        - |j+1><j| tensor G_(j+1)
        - |j><j+1| tensor G_(j+1)* ]
      +sum_(j=0)^K v_j |j><j| tensor I.             (C5)

Every edge block is positive on the entire raw tensor product, since
G_(j+1) is unitary; its norm is 2a_j<=g. Each potential is positive
with norm at most g. Thus H is positive on every raw data state, including dirty helpers.
Each displayed term has at most nine physical register sites and
diameter at most 11 in the fixed one-dimensional placement. There are
560 edge terms and 561 potentials. The shared clock has incidence 1121;
the predecessor's incidence-64 theorem is not imported. Register gates
may act on many binary levels at once. No all-qubit interaction theorem,
bounded-incidence enlargement or original-space locality is asserted.

Let W_0=I and W_j=G_j ... G_1. The block-diagonal full unitary

    V=sum_j |j><j| tensor W_j

conjugates H to h_clk tensor I, where

    h_clk=g I - sum_j a_j (|j+1><j|+|j><j+1|)
         =g I - [2g/(K+1)] S_x.                    (C6)

This identity holds on the full D, including states outside readiness. The
initial clock/data/reference state evolves exactly to the history
specified by these W_j; no branch is removed.

The complete conserved energy is H itself. Its eigenvalues are

    { g(2s+1)/(K+1) : s=0,...,K },                  (C7)

each with data multiplicity dim(D). Hence H has strictly positive
minimum g/561 and norm 1121g/561. For the supplied |0> clock and any
data/reference input, the energy masses are binomial(K,s)/2^K at these
eigenvalues, independent of the data, up to the irrelevant reversal of
the index s. In particular

    <H>=g,       Var(H)=560 g^2/561^2.              (C8)

Both phase settings have the same complete H-spectral law. This is an
explicit total-energy account for the new finite generator. It does not
make H an extension of Q, identify g with E0, or prepare its nonstationary
clock boundary from equilibrium. The preparation's energy coherence is
present in the counted initial clock state.

## 5. A finite read window with exact conditional payload

Starting at clock zero, the position probability is Bin(K,p(t)), where

    p(t)=sin^2(g t/[(K+1) hbar]).

This follows by realizing spin K/2 as the symmetric power of K two-state
rotations; it is a clock-distribution identity, not independence of
repeated measurement attempts. Put

    T_h=pi hbar (K+1)/(3g),
    P_done=sum_(j=M)^K |j><j|.

For every t in [T_h,2T_h], p(t)>=3/4. If X has that binomial law,
Markov's inequality applied to 3^(-X) gives

    Pr(X<M) <= 3^(M-1)(1-p+p/3)^K
             < 3^M/2^K=(3/16)^140=:epsilon
             < 2^(-280).                           (C9)

At every accepted clock position W_j=W_M. Consequently conditioning on
P_done and tracing the clock gives exactly the endpoint (C3), including
all setting/memory/reference correlations. Completion probability is
independent of these inputs and exceeds 1-epsilon. The unconditioned
reduced data differ from that endpoint by trace distance at most epsilon.
The rejected clock branch is retained in the full instrument.

For separately supplied settings s=0,1 and the admitted 25-state old
memory, the conditional pointer-one contrast is exactly Delta in (C4),
because V_flag leaves the receiver d0 effect unchanged and transfers its
probability to the pointer. No earlier gate touches d. Thus pointer one
has zero weight at every unfinished history node, on the stated ready
input. The unconditioned pointer-one contrast and the contrast of the
joint event (done and pointer one) both equal
Pr(done)*Delta>(1-epsilon)/50>1/100. No clock postselection is needed
for this contrast. These are write contrasts, not
assertions that every completed run successfully writes or binds a pair.

At 3T_h the clock rotation returns to its initial density, the whole
data/reference input is restored, and the newly produced output is
undone. This recurrence belongs to the unmeasured closed evolution.
An inserted projective read changes that evolution and does not inherit
the recurrence without a separate calculation.

The detector-to-pointer unitary is included in the same Hamiltonian and
the pointer is counted among the twelve sites. The terminal instrument
reading P_done and the pointer basis is still a supplied final reading.
Its outcome occurrence, external display, work of external interrogation
and regeneration apparatus are not included. The original record carrier
is the explicit occupied memory register; its displaced old state and
all reference correlations are retained in the full output.

## 6. Precision and resource boundaries

The fixed exact matrices in Sections 2 and 3 and the 560 square-root
clock couplings are calibration inputs. They are not encoded into a
classical finite-precision manufacturing claim. If the complete initial
state has trace-distance error zeta and the implemented static generator
has operator error at most delta_H, Duhamel's bound gives, before any
conditioning, additional endpoint error at most

    zeta+2 T_h delta_H/hbar                         (C10)

through the stated window. Alternatively, if all actual G_j are still
unitaries with ||G_j_actual-G_j||<=nu_j, their exact history construction
has the same clock law and completed-word error at most sum_(j<=M)nu_j.
The 420 identity-tail gates have no payload calibration in that second
comparison. General Hamiltonian errors require (C10), not that special
gate-family argument.

Here are two explicit sufficient budgets. Both compare the actual finite-time
channel with the ideal finite-time history channel, rather than dropping
the small unfinished-history weight:

1. **Gate-family errors, exact clock.** Admit complete unitary actual gates
   with initial joint trace-distance error zeta<=1/8000 and
   nu_j<=1/(8000*140)=1/1120000 for every one of the 140 program gates.
   Keep the clock coefficients and identity tail exact. At each history
   node, telescoping bounds the word error by the sum of preceding nu_j;
   orthogonality of clock nodes gives the same bound for the complete
   history isometry, with any passive reference. Thus the channel error
   is at most zeta+sum_j nu_j<=1/4000. The ideal-to-completed-payload
   comparison adds epsilon if the clock is discarded without conditioning.
2. **General static-generator errors.** Admit initial zeta<=1/8000 and

       delta_H <= 3g/[64000(K+1)].                  (C11)

   Then (C10) and pi<4 give
   2T_h delta_H/hbar<=pi/32000<1/8000. The complete actual-to-ideal
   finite-time channel error is strictly below 1/4000. This is a bound
   on the full perturbation operator, not an independent allowance of
   that size for every Hamiltonian term.

In either budget, a final pointer effect with operator error at most
1/4000 changes the two-setting contrast by at most another 2/4000.
The ideal finite-time pointer contrast is Pr(done)*Delta, so the actual
contrast obeys

    Delta_pointer_actual > (1-epsilon)/50 - 4/4000
                         > 1/100.                 (C12)

This statement does not assert a 1/4000 conditional joint-state bound
after an arbitrarily rare outcome, or preserve the exponentially smaller
ideal tail under a general perturbation. The budgets protect the finite
pointer contrast and the stated unconditioned channel comparison. They
are sufficient requirements, not achieved experimental tolerances.

The resources supplied at launch are the localized source basis seed,
the pure q,b helpers, the retained setting, the zero pointer d, and one
pure 561-level clock.
The carrier label is prepared at zero. Unknown memory/reference data are
information inputs and are never treated as clean workspace. No generic
synthesis scratch, 26469-level battery rail, copied data row or thermal
donor stock is required by this specifically declared register model.
Their absence does not prove thermal or original-occupation realizability;
those are different preparation and encoding contracts.

This gives a smaller complete finite autonomous *simulation of the
prepared measurement channel*, with its own explicit conserved energy.
It preserves the original active contact and original admitted output
channel at the simulated endpoint. It leaves the physical original-Q
bridge, material preparation, apparatus readout and renewal open.

## 7. Falsifiers and separate review obligations

The construction fails if (C1) omits a receiver/phase factor, any listed
gate is not complete unitary, the support bound needs an uncounted
register, the 140 count omits an inverse or setting correction, the
source's finite closure encounters a boundary on an admitted prefix,
the history conjugation (C6) fails on any raw input, or the endpoint
does not retain arbitrary old-memory/reference correlations. Energy and
window claims fail on an incorrect spectrum, moment, binomial law or
tail inequality. A changed physical encoding must not be presented as
original occupation locality or as an exact extension of Q.

Independent review should check: (1) source pin and admitted memory
scope; (2) every local gate and raw complement; (3) receiver conjugation
and controlled phases; (4) source reflections and the 140 count;
(5) source finite-boundary agreement; (6) full-space positivity and
physical register/resource count; (7) exact history conjugation and
total-energy law; (8) finite window and reference-uniform channel;
(9) recurrence and final-instrument boundary; (10) precision and
nonthermal initial-resource account. No scientific executable, expanded
circuit, simulation or numerical search was run for this analytical note.
