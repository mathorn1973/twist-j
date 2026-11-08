# Forward-only coherent selection after a finite native contact

**NON-CANONICAL, L1. Candidate-T analytical construction, not independently accepted.**
Author: A. M. Thorn. License: Apache-2.0. Claim: #1745.

## 1. Exact scope and premises

The scientific source is Public Canon v105 at
`892a0b11089d34e241e1eb76d2c03247022d18e6`, specifically the declared
HOMOGENEOUS-CAPTURE-CURRENT-RECORD model and its public proofs in
`notes/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/`.
This construction changes neither that native macrostep nor its receiver.
It supplies a DIFFERENT compact preparation and a DIFFERENT readout from the
original scattering packet and Q_win/Q_full. No old numerical lower bound is
assigned to the new readout. In particular its compact pulse is not restricted
to the old safe spectral-energy window or a pure positive-velocity band.

The native one-pair, one-token-or-pulse, one-receiver law is
U_rec = T (U tensor I_D) T*, U = exp(-i beta)(W tensor V_car) C,
beta=4pi/5, W=Gamma S M2, and z_g=exp(-2pi i/5).
The two contact vectors are
A=(e1-e4)/sqrt(2), B=(e2-e3)/sqrt(2),
alpha_s=|R=s,r=0,iB; token at y=s>,
beta_s=|R=s,r=0,A; pulse at x=s,bank 1>.
C alpha_s=(3/5)alpha_s+(4/5)beta_s.
The source coin, relative shift and contact phase are exactly those in the
source, including chi_0=delta_(r=0) A, not delta_0 B.
The receiver is at z=100. All 26 carrier and 26 memory labels are admitted,
including arbitrary joint entanglement of those labels with a reference.

ADDITIONAL CONTROL PREMISES: fresh five-state and binary registers; F5 and
F5* on those five-state registers; controlled forward z_g^(-1)W and controlled
forward center translation T_R; the finite source permutation and phases below;
finite reversible Boolean flag computation; and holding the carrier/receiver
while the object-control program executes. These operations are explicitly
supplied on an extended carrier. No synthesis from the original six-pentit U,
full native occupancy implementation, local controller, energy reservoir,
autonomous stopping or elapsed-time calibration is inferred. The only native
U_rec steps are the T steps before this control program and the stated steps
after it is released. F5* is an auxiliary basis change, not a backward object
step. Neither W* nor T_R* is an executed object operation in this construction.

The analysis stays at L1: a squared norm is a branch weight. A final flag is
a coherent register, not a law selecting one realized outcome or frequencies.

## 2. Compact source and exact finite outgoing component

Fix s<100 and normalized psi_s=alpha_s with any carrier label. At the input
its nominated object bound-band weight is zero for every |P|<=1/12.
Indeed exchange of the two objects acts by r->-r and e2<->e3, leaving e1,e4
fixed. It commutes with W(P) for every P. The isolated rank-one Riesz branch
on this connected momentum interval is even: at P=0 its vector is delta_0 A,
and its exchange eigenvalue cannot change continuously from +1 to -1.
The input delta_0 iB is odd. This excludes exactly the nominated branch on
this interval, not all possible other bound branches or all point spectrum.

Let J_T select pulse position x=s+T and bank 2, leaving the object and every
label/memory/reference unchanged. For every integer T>=1, before receiver
calibration,

  J_T U^T psi_s = c_T W^T chi_s tensor |s+T,bank 2>,
  chi_s=|R=s,r=0,A>,
  c_T=exp(-i T beta)(8/25)(-4/5)^(T-1),
  q_T=|c_T|^2=(64/625)(16/25)^(T-1).                 (1)

Proof: the carrier starts as a standing token. Its displacement is at most
one per step. A pulse at the extremal right site must be emitted in the first
contact and move right at every step. From pulse bank 1 the first right-hop
coefficient of V=EQ is 2/5; from bank 2 each later right-hop coefficient is
-4/5. The first emission coefficient is 4/5. At every macrostep boundary the
extremal component is in bank 2, while C acts on bank 1 only. Thus later
contact cannot alter that component. All object histories remain coherently
in W^T chi_s; no object position, path or bound projection is used to obtain
(1). A component emitted later or not moving right at some step cannot catch
this extremal site.

For T>=100-s the native receiver calibration at the outgoing site swaps the
incoming carrier label with the old memory. For any joint label/memory/reference
vector Xi this makes the right side of (1)

  c_T W^T chi_s tensor |s+T,bank 2> tensor SWAP_(L,D) Xi.       (2)

This is an operator statement on the whole 26x26 logical input, not a
postulated factorization of an initially unknown old memory. On fixed input
label 1 it transfers all old-memory/reference coherence to the pulse and writes
d1. Its amplitude and q_T are independent of the logical input.

The two-coordinate source is a specified state, not a free loader assumption.
Here is an explicit additional finite loader from a basis state. Start object
coin e1, token at s, and a fresh five-state register h=0. Apply F5 to h, then
the disjoint permutations (0,e1)<->(0,e2) and (1,e1)<->(0,e3), and phases i on
(0,e2), -i on (0,e3). The h=0 branch is exactly sqrt(2/5) alpha_s; h=2,3,4
retain the other preparation branches. All labels are spectators. Include
h=0 in the eventual acceptance predicate, without discarding those other
branches. All reported prepared-source weights then acquire exactly 2/5.
This loader is a supplied finite unitary, not yet a native-admission theorem.

## 3. A complete five-state forward-step instrument

For any unitary V define F5_(a,b)=zeta_5^(ab)/sqrt(5) and

  B(V)=(F5* tensor I) diag(I,I,I,I,V) (F5 tensor I).            (3)

With the register initially 0, its five operator coefficients are

  K_0(V)=(4I+V)/5,
  K_a(V)=zeta_5^(-4a)(V-I)/5,  a=1,2,3,4.                    (4)

This follows from the finite geometric sum. The complete block (3) is unitary,
and direct multiplication gives sum_a K_a* K_a=I. The accepted elementary
effect is

  H(V)=K_0* K_0=(17I+4V+4V*)/25
      =I-(4/25)(I-V)*(I-V),     9I/25<=H(V)<=I.             (5)

The adjoints in the mathematical effect do not require executing V*. The
actual block uses only a single forward controlled V and two auxiliary F5
basis changes. In the coordinate field O=Z[i,zeta_5], all complete-block
coefficients lie in O[1/5] when V does. The auxiliary F5 also lies there since
sqrt(5) belongs to Q(zeta_5) and 1/sqrt(5)=sqrt(5)/5.

Run m blocks with fresh registers, call the all-zero word a successful trial,
then run n such trials, without stopping or erasing any history. At the end
mark success if at least one trial was all zero. All elementary K_a are
commuting normal polynomials in V. Therefore the total effect of no successful
trial is (I-H(V)^m)^n, and the effect of at least one success is exactly

  G_(m,n)(V)=I-(I-H(V)^m)^n.                                (6)

One proof expands the complete Kraus sum: a trial has all-zero effect H^m
and complementary effect I-H^m. Products may be grouped because every Kraus
operator commutes with every other and its adjoint. Expansion of n complete
trials gives (6). This is a sum over all retained histories. It does NOT
identify the accepted state map with multiplication by G or sqrt(G).

For commuting unitaries V_R=T_R and V_W=z_g^(-1)W run the two programs on the
same object, with separate fresh records. Accept only if both succeed. Their
combined effect is

  G=G_(32768,8)(T_R) G_(8192,8)(z_g^(-1)W).                 (7)

Every branch operator commutes with each bound-band projector defined below.
The rejected branch is the sum of ALL histories not satisfying the predicate,
including a failed final carrier-position or preparation test. Equivalently
retain the coherent history and reversibly XOR the Boolean predicate into a
fresh flag. The flag=0 and flag=1 projections are exhaustive. No omitted
central rejection, signed-polynomial normalization, reset, or operator-square-
root compilation is used. This is a new effect, not a reimplementation or
retuning of either frozen detector tuple in private PR #48.

## 4. Uniform pass/stop bounds with integer certificates

Write a=1/100, b=1/12, and let B_a and B_b be the direct-integral projectors
onto the nominated simple W(P) bound branch in the respective momentum windows,
zero outside those windows. These are proof observables, not executed sharp
projectors. The public source proves a complementary zero-momentum gap
Delta_0>delta_0:=27/110 and ||W(P)-W(0)||<=|P|. No exact Delta_0 is asserted.

On |P|<=a the branch eigenvalue obeys |lambda_b(P)-z_g|<=a, and
|exp(iP)-1|<=a. Hence both elementary effects (5) are at least
1-1/62500 on the pass branch. Bernoulli's inequality gives

  G B_a >= gamma B_a,
  gamma=1-(32768/62500)^8-(8192/62500)^8 > 99/100.            (8)

The last bound follows already from 32768/62500<8/15,
8192/62500<2/15, and 100(8^8+2^8)<15^8.

For |P|<=b outside the nominated eigenbranch the spectral distance from z_g
exceeds delta_0-b=107/660>4/25. Thus H(V_W)<1-64/15625.
For |P|>=b, sin(|P|/2)>=sin(1/24)>1/25, so
H(V_R)<1-16/15625. This covers ALL of I-B_b, including unclassified object
spectrum outside the wider window.

For 0<u<1, (1-u)^k<=1/(1+ku). Since
256(64/15625)=1024(16/15625)=16384/15625>1,
the W and R stop factors raised to 256 and 1024, respectively, are each below
1/2. Each trial has 32 such blocks; its all-zero effect is below 2^(-32).
Finally 1-(1-x)^8<=8x yields

  0<=G<=I,    G(I-B_b) <= 2^(-29)(I-B_b).                  (9)

This is an effect bound, not an amplitude bound. The distinction determines
the conditional leakage in the next section. No success weights are assigned
to an L6 occurrence law.

## 5. Finite capture, conditional binding and complete old-memory transfer

For chi_s=delta_(R=s,r=0) A the source Riesz estimate gives, for |P|<=a,

  |<delta_0 A,chi_b(P)>|^2 >= 1-(11/259)^2 = 66960/67081.

The center Fourier transform of delta_s has constant modulus. Using pi<4,

  <chi_s,B_a chi_s> >= (a/pi)(66960/67081) > 1/500.          (10)

No asymptotic packet or scattering limit is used. W commutes with the branch
projectors and G, so (10) holds also for W^T chi_s at every native read time.
Combining (1), (8)-(10), then selecting the pulse front, gives

  p_T=q_T <chi_s,G chi_s> > q_T (99/50000),                 (11)
  conditional outside-B_b weight
        < 50000/(99*2^29) < 1/10^6.                       (12)

The factor q_T cancels in (12); omitting that factor in the numerator before
conditioning would be a different, generally invalid, argument. The result
holds on the full flagged state including all retained fine histories, and
also on its reduced object state. The histories may be entangled with the
object. Since all object branch operators and the carrier-front test commute
with B_b, the detector has not created the selected bound component by a
noncommuting object projection. It selects the component generated by the
native contact. It does not prove that later interacting evolution preserves
binding forever.

For the short device s=99,T=2, q_T=1024/15625. Consequently

  p_prepared > 1/8000,
  p_basis_input_with_loader > (2/5)(1/8000) = 1/20000.       (13)

These are strict L1 squared-norm lower bounds for this different compact
source and finite instrument. They are not empirical click probabilities and
not the asymptotic bound 2/10^28 from Canon.

More generally, the accepted logical effect is p_T I_(L,D). The accepted
whole-state isometry factorizes as a fixed object/history/carrier-location
vector times SWAP_(L,D). This follows from (2), label-independent filtering
and a label-independent acceptance predicate. Arbitrary source-label/memory/
reference entanglement is preserved by this swap; on fixed source label 1,
receiver d1 and the transferred old-memory/reference factor are exact.
The source-loader variant multiplies its effect by 2/5.

## 6. Actual record protection and the cost of a longer horizon

For s=99 and T=H+1, the selected pulse is at x=100+H. During the additional
filter/control program it is HELD along with the receiver, as a declared
control premise. Object gates and flag logic act trivially on its labels
and receiver. Once the original U_rec is resumed, carrier speed is at most
one per macrostep; contact changes arrangement at the same site. The only
receiver-memory coupling is the bond (99,100). Thus on the accepted branch
with source label 1, memory is exactly d1 at every subsequent native boundary
0,...,H, for arbitrary object/history/old-memory/reference correlations.

This is the geometric buffer argument of #1741 re-derived on the explicitly
reached output, not a new all-time retention theorem. It protects the memory,
not the binding. Its extremal-front tradeoff is explicit:

  q_(H+1)=(64/625)(16/25)^H.

A longer guaranteed buffer decreases this particular selected weight
geometrically. No global optimality or impossibility of a better source or
pulse is claimed. The T native steps do not include the detector's control
duration. Without holding, the stated implementation and time bound do not
apply; a moving concurrent detector is a separate construction.

For comparison with an arbitrary approximate implemented unitary instrument,
a uniform joint vector error eta implies a flag-weight error at most eta.
Conditioning amplifies errors by the accepted weight; no hardware precision
or implementation-error certificate is supplied by this ideal theorem.

## 7. Finite resources, rejected branches and repeat use boundary

The detector uses D=8(32768+8192)=327680 fresh five-state registers,
262144 controlled center translations and 65536 controlled z_g^(-1)W calls,
plus 2D=655360 F5/F5* basis changes. The optional source loader uses one more
five-state register, two fixed transpositions and the two displayed phases.
These counts refer to the named controlled-block abstraction, not proven
local elementary gate count, energy or physical duration.

A reversible Boolean realization can use at most 2D+32 fresh binary work/flag
registers: compute a zero-indicator for each five-state register, use AND trees
for the 16 trial words, OR trees for the two groups of eight trials, and AND
with a source-mark test and a carrier-front test. Every intermediate is kept;
classical reversible computation copies basis predicates, not arbitrary
quantum states. The carrier-front test is an explicit finite position/bank/
arrangement controlled permutation. Its local realization and routing cost are
additional admission obligations; they are not hidden in the above counts.

All data branches have a finite reachable position support. After the T native
steps, |R-s|,|r|<=T. Each subsequent object W call shifts each coordinate by at
most one, and T_R shifts the center right by one. Thus during the whole
program every branch lies in

  s-T-65536 <= R <= s+T+65536+262144,
  |r|<=T+65536,       s-T<=carrier<=s+T.                    (14)

The held carrier never moves during the detector. A finite walk realization
with unused margins outside (14) agrees exactly on the prepared input; no
sharp spatial truncation is applied to the filtered state. This avoids using
an unbounded ancilla-free effect as a finite physical device. Local occupancy
routing, controller Hamiltonian and battery remain distinct unproved tasks.
Native charge/current identities hold on the genuine U_rec segments with the
canonical weights, not automatically as the total current/energy of the
added apparatus.

The full transformation (source loader, native evolution, control blocks,
reversible predicate) is unitary, so it has an explicit reverse word. That
inverse is not a useful reusable reset: it removes the new record. Reuse with
a retained record requires a specified archive and fresh preparation/program
registers. The one-carrier model cannot silently hold the first outgoing
carrier while admitting an additional source token. No repeated many-carrier
law or all-trial product occurrence is asserted here.

## 8. Status and decisive review questions

The contribution is the exact forward-only complete filter instrument and its
composition with a compact source, finite native transport, all-label memory
swap and a reached finite protection buffer. Compact front transport and
buffer reasoning have appeared in earlier analytical discussion; no novelty
claim is made for them alone. Every result is conditional on the declared
extended control carrier and alphabet. The original asymptotic-packet finite
preparation, PR #48's fixed detector, PR #1743's native admission, the actual
v105 output's all-time retention, controller energy, faithful residual
realization and terminal occurrence remain open at their own scopes.

An independent review must try to break: the exchange-parity argument; the
front recurrence with bank ordering and the occupied receiver; the full
commuting Kraus sum rather than just a successful word; the effect/amplitude
and conditional-normalization distinctions; the explicit source mass bound;
finite support of every rejected history; and preservation of all old-memory/
reference correlations. Exact audit examples complement, not replace, these
general proofs. No Canon status or frontier row is changed by this note.
