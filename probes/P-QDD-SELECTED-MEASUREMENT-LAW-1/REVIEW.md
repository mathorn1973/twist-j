# Independent written review of ETH-QDD-1

PUBLIC; NON-CANONICAL. Review of P-QDD-SELECTED-MEASUREMENT-LAW-1,
prepared before its first formal execution and public pin. This is a
written mathematical and scope review, not an architecture run, empirical
result or Canon promotion. Original text Apache-2.0.

## 1. Review method and conclusion

The reviewing agent read MODEL.md, PROOF.md and PREREG.md independently
of the new verifier. It also read the source proof in
P-U-GALOIS-FIBER-CODE-1/PROOF.md, the complete channel argument in
P-QDD-V80-CLOSURE-BOUNDARIES-1/MIXED-PROOF.md, the relevant current
CORE/FRONTIER obligations, and the two accompanying selected-theory notes.
No scientific code was executed and verify.py was not read before this
review was written. The exact calculations below were checked from the
displayed equations, not inferred from a proposed program output.

**Conclusion:** no mathematical gap was found in the conditional
instrument, code-transport, record and ordered-history arguments at their
declared scope. ETH-QDD-1 is a fully specified effective measurement model
once its listed inputs are supplied. Its additional physical choices are
identified rather than presented as deductions from J or U. The written
proof is suitable for the frozen exact audit and subsequent public review.
This conclusion anticipates neither a successful verifier run nor a passed
physical cross-layer gate.

## 2. Source metric and context identification

The distinction between an operator density rho and its covariance
C=rho G^-1 is necessary and correctly retained. Positivity means
G rho is positive semidefinite, while tr(rho)=1. In orthonormal
coordinates rho becomes G^(1/2) rho G^(-1/2), an ordinary positive
trace-one density. Accordingly, code transport is W_n rho W_n^-1
for operator densities, and W_n C W_n^* for covariances. Using one
formula for both would be incorrect.

MODEL.md explicitly takes the complexified source to be K tensor_Q C,
or equivalently the four complexified source-basis columns. It does not
evaluate a complex linear combination in one principal embedding and
thereby collapse the source to one complex dimension. Galois action on
the K factor and complex coefficient extension are distinct operations.

The five context projectors follow from the specified multiplication-by-j
matrix R, with R^5=I and R^* G R=G. Starting with
u_0=(sqrt(5)/2)(1,1,1,1)^T, its four successors are
u_k=-(sqrt(5)/2)e_k. Their norms are one and distinct inner products
are -1/4. This proves both the tight-frame identity sum_k P_k=5I/4
and the pairwise LOW transition probability tr(P_k P_l)=1/16 for
k different from l. No native-time interpretation of R is required or
claimed.

The inherited code identity W_n^* W_n=G supplies an isometry on the
chosen four-dimensional code. The relation N_(m,n) W_n=W_m proves
transported-projector intertwining by composition with W_n. This uses
neither a global inverse of U nor a global unitary extension through the
native mergers. For context zero the read matches the distinguished
endpoint. Other contexts require the additional coherent controls which
the model explicitly chooses.

## 3. Complete reduced-channel argument

The attenuation matrix A is placed in the basis
(e_1-e_4,e_2-e_4,e_3-e_4), whose metric is H=I_3+11^T. G is the
identity on the sum-zero subspace, so this induced metric is exact.
The transfer to context k by R^k is an isometry. The documents correctly
avoid identifying the inherited A with Q_0 R Q_0 or with native free
evolution; selecting this attenuation test family is an explicit input.

The branch classification uses the right positivity argument. An exact
Q effect kills every branch Kraus map on P, and repeatability kills its
output in P. The remaining map is an arbitrary CPTP channel on QV.
This gives the entire reduced finite-dimensional CP branch class, including
complex Kraus entries and mixed outputs. Rank-one LOW has only its identity
channel after this restriction.

For HIGH, fixing the three attenuation profiles fixes the three rank-one
projectors obtained from B_t-B_(t+1), including B_0=I. The displayed
defect and overlap certificate is consistent with the inherited proof:
the three positive coefficients are 15/16, 215/256 and 2815/4096;
the three vectors span, and the first has nonzero overlap with each of
the other two. A fixed projector of a unital Kraus adjoint forces every
Kraus map to preserve both its image and kernel. Commutation with these
three projectors therefore forces each Kraus map to be scalar. Trace
preservation then gives the identity channel.

Thus the sharp effects, repeatability and selected three-test principle
indeed force P_k X P_k and Q_k X Q_k in the stated class. The weaker
two-test and depolarizing alternatives remain excluded only by their
actual failed conditions. The conclusion would be false if complete
positivity were replaced merely by positivity, or if preserving a test
meant agreement on only one chosen input.

This is reduced-channel completeness. It neither identifies every
microscopic implementation nor classifies an unspecified correlated
environment. The model keeps this limitation explicit.

## 4. Coherent writing, occurrence and resource accounting

The reference writer P_k tensor S_L+Q_k tensor S_H is a unitary on
the full source and three-state pointer because the source projectors
are complementary and the two pointer swaps are unitary. Its blank-input
slice writes one common HIGH label and therefore preserves all HIGH
coherences. Agreement with the older five-state archive is asserted on
that slice only, not for dirty pointer inputs.

For a coherent or general density input, the unitary output contains
P_k rho Q_k tensor |L><H| and its adjoint as well as diagonal branch
terms. PROOF.md retains these terms. Pointer dephasing produces the
classical-record/quantum-source state; selecting one actual outcome is
then a separate Born occurrence postulate. Neither a unitary writer nor
dephasing is incorrectly treated as a proof of single-outcome occurrence.

Passive old records and fresh blank cells are supplied resources. The
record includes context, invocation, preparation and comparison time, so
equality of full records is stronger than equality of LOW proportions.
The finite-horizon capacity rule, RESOURCE_EXHAUSTED disposition and
separation of archive rereading from a new event prevent an unlimited
record from being hidden in a finite pointer.

The replacement X -> sigma tr(X) is CPTP. Its joint version replaces
both source and operative memory while preserving the archive marginal.
It removes correlations with the retained archive at the reduced level;
it is not a claim that microscopic information is destroyed or that reset
is a reversible, energy-free operation. The stated reservoir or replacement
carrier is part of the assumed resources.

## 5. Ordered laws, adaptation and zero support

At each causal protocol node the two positive branch maps sum to a
trace-preserving map. Positivity, normalization and compatible prefix
probabilities therefore follow by induction for every finite protocol,
not by extrapolating the finite census. The protocol chooses its next
setting and intervention from the recorded past. A setting lottery needs
an additional declared law; future outcomes are not permitted as inputs.

The joint-memory recursion (7a) acts on the complete finite source-memory
state. Its intervening maps are joint CPTP maps, followed by the selected
local instrument tensored with the memory identity. This makes the admitted
memory extension precise without supposing that arbitrary source-memory
correlations induce a state-independent reduced source channel. It does
not claim to classify all possible joint measuring interactions.

All zero-weight descendants remain zero. Conditional states are defined
only at positive weight; a zero raw preparation yields ZERO_SUPPORT and
no measurement event. Bounded causal stopping has total leaf probability
one. Unbounded stopping is not asserted to terminate almost surely.
The stated infinite-record extension concerns a compatible probability
measure on cylinder events, not convergence of an infinite quantum state,
an infinite physical apparatus or a native source of samples.

Repeated same-context reads with free waits only have support on the two
constant words. Fresh product preparations instead give the stated product
law when the preparation and settings are fixed and all operative memory
is reset or absent. Adaptive settings can preserve history dependence even
after replacement; the text correctly withholds unconditional independence.

## 6. Exact prospective diagnostics

The numerical fractions in the proof follow directly from its chosen maps.
For initial P_0, setting 1 followed by setting 0 gives the joint table

| First outcome | Final LOW | Final HIGH |
| --- | ---: | ---: |
| LOW | 1/256 | 15/256 |
| HIGH | 225/256 | 15/256 |

The HIGH-to-LOW weight is (1-1/16)^2. The final LOW marginal is
226/256=113/128, while omitting the intervening read leaves probability
one. All four entries are nonnegative and sum to one.

For the HIGH coherence witness, the vectors a,b,c are orthonormal in
the source metric. The coherent state (a+b)/sqrt(2) has squared overlap
5/8 with the context-1 LOW vector, whereas the equal incoherent mixture
of a and b gives 5/16. Thus a fine HIGH measurement followed by forgetting
the fine label is observably different from the chosen coarse channel.

These are useful consequences for later tests, but they are not reported
measurements or blind model-selection evidence. The model was chosen with
knowledge of earlier algebraic comparisons and ordinary quantum theory.

## 7. Acceptance and Canon boundary

PREREG.md freezes the written scope and finite exact audit before execution.
Its representative positive states are not called an exhaustive census,
and matrix units are used as an operator basis rather than as physical
preparations. The universal positivity, CP and all-protocol results rest on
the written proof. Scientific run status, byte identity and architecture
acceptance must be supplied by the later immutable run records.

The selected theory may be finished mathematically without laboratory
access. Its physical use adds CH-SOURCE, CH-CONTEXT, CH-CP,
CH-ATTENUATION, CH-BORN, CH-RECORD, CH-RENEWAL and CH-CONTROL.
Those assumptions cannot simultaneously be claimed as consequences of
the untouched deterministic substrate. In particular this active model
does not become a passive feeds_U=false decoder through restoration of
a final checkpoint.

The prospective L1-to-L4, L4-to-L5 and L5-to-L6 gates are named but
not passed. The old QDD apparatus, terminal-event and full-class owners
retain their broader scopes. Proposed conditional T statements, selected
dictionary claims at most D and physical-adequacy hypotheses are separated
in the fold proposal. No experiment, native derivation, unrestricted
apparatus completeness or Canon activation is certified by this review.
