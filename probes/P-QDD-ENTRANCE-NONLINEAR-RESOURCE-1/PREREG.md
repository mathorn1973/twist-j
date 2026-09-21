# Preregistration: entrance origin and nonlinear resource

PUBLIC; L1; NON-CANONICAL. Owner: A. M. Thorn / entrance-origin session
2026-09-20. Lock: https://github.com/mathorn1973/twist-j/issues/1087.
Probe: P-QDD-ENTRANCE-NONLINEAR-RESOURCE-1.
Base: 691fe341a95d8fc48e3c2c5982d22419f5deced8, Public Canon v90 ACTIVE.
The author authorizes the connected GitHub contributor identity.

## 1. Equation and decision classes

Use the exact native generators on X=F5^6, x=(a,b,c,d,q,r),
z=a+b+c+d+q+r, F_t(x)=g_(z+2t)(x), t in {0,1}.
The canonical four-point code begins at counter three with
Y_h=(h,0,0,0,1-h,0), h in {1,2,3,4}. At n>=3 let
Y_h(n)=N_(3,n-3)Y_h under the actual native driver. Let
h_n(x)=(-1)^(n-3)(a+b+c+d), T_delta(x)=(p,q-delta,r+delta),
f(0)=0, f(1)=1, f(2)=f(3)=f(4)=2 and C_n=T_(f(h_n)).
At a completion cut n+d the entrance target is N_(n,d)C_n, not C_n
at an unchanged counter. The comparison includes every code amplitude.

Freeze five mathematical classes, none claimed to be the unresolved
physical class A_phys of #1086:

A. Native words and classical deterministic or stochastic causal control
through pi=(z,r). A controller may
have arbitrary memory, independent auxiliary input, random seed, variable
duration and stopping rule. Its source observations factor through pi.
Every admitted actuator must also have a pi-output determined only by
pi and the controller/auxiliary state. Native generators satisfy this
condition. An independently supplied source-sensitive actuator does not.
All controller preparation and the schedule law are source-independent.
Decide whether exact entrance is possible on the four common-pi inputs.
An arbitrary coherent superposition and interference of control programs
is not included in this point-transition class.

B. Monomial permutations of native points and any finite auxiliary
point carrier, with any independent coherent or mixed auxiliary state.
For each fixed input auxiliary point, the output native r coordinate
is represented by a polynomial of total degree at most two in the six
input native coordinates. Phases are unrestricted. Native endpoint
coordinates are compared faithfully, with no nonlinear output decoder.
Decide exact entrance on the code. This is a condition on the whole
operation, not on individual gates, and does not include every circuit
with affine controls interspersed with source-dependent native selection.

C. All two-port permutations preserving q+r and commuting with every
T_delta. Classify this whole mathematical family. It is target-independent
as a mathematical definition; physical completeness is not asserted.

D. Reversible affine field-register operations and multiply-add gates
x_k<-x_k+c*x_i*x_j on three distinct indices, arbitrary c in F5.
Adjoin three zero work registers external to the native selector.
Freeze the fourteen-block construction in CONSTRUCTION.md, including
the balanced q/r pair and its timing convention. Decide its full-state
identity with N_(n,d)C_n on each known stable sheet z in {1,4}, for
every native driver word and source-independent completed-block schedule.
No native tick is admitted between the two halves of a balanced pair.
This primitive family is additional mathematical input, not native or
physical availability inferred from successful synthesis.

E. No auxiliary registers; arbitrary invertible affine maps of the six
native coordinates before, between and after actual native selector
steps. This is a mathematical operation family, not the class of native
words and not an independently admitted physical family. The number of
native selector steps is the resource. Freeze the two-step construction
in NATIVE-ROUTING.md at launch n=3, with the actual bits theta_3=0 and
theta_4=1. Decide whether zero or one selector step can achieve the same
coherent entrance, with its proper freely evolved endpoint. An affine
map between native ticks is a completed boundary operation; no physical
duration or unchanged evolution during its implementation is assumed.

## 2. Code and immutable inputs

verify.py uses only the Python standard library, exact integers modulo
five, finite tuples and explicit matrix-unit labels. No floating point,
external packages, network, random sampling or fit is admitted. The
universal claims are written proofs in PROOF.md, CONSTRUCTION.md and
NATIVE-ROUTING.md;
the finite program audits exact premises and concrete witnesses.

Before execution freeze together PREREG.md, PROOF.md, CONSTRUCTION.md,
NATIVE-ROUTING.md, PHYSICAL-ORIGIN.md, REVIEW.md and verify.py.
Public commit and exact
file hashes are recorded after pin; all files are read back from that
commit before the first run. Only static syntax checks are allowed
before then. No predecessor scientific program is imported or rerun.
The independent reviewer does not read verify.py before completing the
written attack. Review is independent reasoning, not another execution
or another architecture.

## 3. Carrier, data and exact targets

G1. Derive the global autonomous quotient pi=(z,r) for all five
generators and both selected steps. Prove the all-history causal-control
factor theorem for class A and its negative entrance decision.

G2. Recheck stable paired transport and h_n invariance. Prove that the
four code points remain on an affine line. Native unchanged U and
commanded words cannot generate source-dependent port separation.

G3. Positive boundary control: commanded word b,d,b,e equals T_2 on
all X. Powers provide every constant paired shift. Commandability is
additional to actual selected U; the missing part is conditioned action.

G4. Prove the exact cubic minimum on the four nonzero code labels and
the complete five extensions f_tau(h)=tau+h+h^2+h^3+(3-tau)h^4.
The original f(0)=0 extension is quartic. Prove class B empty for the
entrance, including independent coherent/mixed auxiliaries through the
nonnegative diagonal-output argument. No nonlinear-amplitude claim.

G5. Reduce the entrance to q,r on a known sheet using
h_n=(-1)^(n-3)(z-q-r). Prove global port bijectivity for this fixed
sheet constant, and classify class C as (s,r)->(s,r+k(s)) with exactly
5^5 choices. Conservation and translation covariance alone do not
select the required f; no physical charge interpretation is adopted.

G6. Prove the fourteen-block class-D circuit, exact cleanup and parity
compensation for arbitrary native waits between completed blocks.
The identity holds on the whole chosen stable sheet, including h=0 and
arbitrary initial native r; zero work preparation is required.

G7. Prove full coherent equality on the code and with any untouched
reference or old record. Account for all sixteen matrix units and the
common zero final work state. No discarded fine-label environment.

G8. Preserve exact negative controls for obsolete cleanup, omitted
parity compensation, omitted nonlinear terms and class-boundary changes.
PHYSICAL-ORIGIN.md must keep missing physical admission, full interaction
duration and architecture ownership explicit. The physical entrance
question remains STOP-DEFINITION; these mathematical classes cannot
stand in for its missing complete physical family.

G9. Prove the exact class-E two-step witness, affine reversibility and
injectivity of every intermediate four-point code image. At n=3 the
free two-step map on z=1 is b squared, hence identity. Verify the target
at n=5 is N_(3,2)C_3. Prove zero-step failure by affineness and one-step
failure for either bit under arbitrary affine pre/post maps: the three
HIGH endpoints must remain an arithmetic progression; enumerate all
twenty nonconstant affine trace parametrizations for each bit, using
the trace, r and ell=-a+b-c+d second differences. A constant trace makes
the entire step affine. Thus two native selector steps are necessary
and sufficient within class E at this launch, not a minimum physical
duration or universal apparatus complexity. Native nonlinearity can
therefore suffice when the added affine routing is admitted.

Frozen finite audit ranges: all 15625 native points for generator and
selector quotients and the commanded shift; all stable points for
paired transport; actual code starts 3 through 20 for affine-line checks;
all 125 quadratic scalar polynomials and 3125 reduced degree-at-most-four
polynomials for the response comparison; all 25 port points at both
stable sheet constants and both parities; all 3125 class-C functions;
all stable inputs at both parities for the no-gap construction; all
binary words through length five and the explicit single-gap, uniform
and alternating schedule families in verify.py for code interleavings,
with actual starts 3 through 10. Matrix-unit audits use exactly those
code schedules. The pinned program defines their enumeration order.
For G9 also freeze full 15625-point checks of both supplied affine maps
and their inverses, all four intermediate trajectories and sixteen
matrix units, and all forty nonconstant affine trace parametrizations
in the one-step obstruction. NATIVE-ROUTING.md fixes the maps and witnesses
before the program is executed.
No finite word length is the basis of an all-time conclusion.

## 4. Systematics and exclusions

Source HIGH (sum of source amplitudes zero) and endpoint HIGH (three
specific basis endpoints) are not confused. The current target is the
endpoint permutation with full coherent extension; finite-field label
polynomial degree is not a quantum amplitude degree or physical
Hamiltonian interaction order.

pi deliberately omits q. Observing q, a source-dependent clock, a
prepared correlated controller or a fresh actuator with source-dependent
pi effect changes class A. Nonmonomial interference changes class B.
Affine routing that exposes h to the native selector can create higher
endpoint degree and is not excluded merely by calling its gates affine.
The conditional construction does not prove such alternatives impossible.

The class-D no-gap and interleaved comparisons use a known initial stable sheet;
global native U is not assumed injective. Its action on the used sheet
at a tick is the single selected affine bijection. Work registers are
declared external and passive during native ticks. All arithmetic blocks
and their controls are extra resources. No finite pulse inside a block
is supplied by the discrete schedule proof.

The result is analytically exposed before pin. No blind prediction or
discovery claim is available. Related #990 affine coupling/carry work,
#996-1006 and #1034-1038 retain their scopes. The new decision is this
fixed coherent entrance resource, not a reprise of waiting or the
twenty-mode code-transfer channel.

## 5. Failure threshold and disposition

Every assertion is exact. Any admitted counterexample to a stated
factorization, class-wide obstruction, classification, polynomial,
complete-state synthesis or coherent equality refutes that mathematical
target. A negative decision in A or B and a constructive witness in D or E
are both scientific outcomes. No tolerance or finite-depth substitution
may repair a failed universal claim. Preserve failures under this pin.

Incomplete execution, syntax/runtime failure, public pin/readback
mismatch, changed frozen content or architecture/byte mismatch is STOP,
not a physical or mathematical counterexample. A pin whose first formal
gate never completes is ABANDONED under POLICY and not repaired in place.

On completion add EXPECTED.txt, neutral RUN.md, RESULT.md and a separate
ACCEPTANCE.md. Public x86_64 and aarch64 must replay identical verifier
and stdout hashes and pass aggregate check. Proof acceptance can support
candidate-T at L1; no Canon row changes before a separate fold.

## 6. Action layer and physical boundary

All new mathematical decisions remain L1. No L1-to-L5 gate is earned.
No material q/r carrier, source preparation, independently available
interaction, physical clock, energy, spatial locality, clean physical
environment, archive, single event, occurrence or reset is derived.
The construction changes native q,r and cannot be presented as
feeds_U=false. A physical mapping or different architecture remains
necessary. No ENTROPY source replacement or Canon release is included.
