# Static review before the public preregistration pin

**NON-CANONICAL; 2026-10-04. Disposition: accepted for public pin.**
This is a separate static review of the prospective candidate, not a
scientific run, an execution result, an independent theorem-grade proof,
or a promotion of its status. Public Canon v97 and the physical HOLD
remain unchanged.

The reviewer inspected PROGRAM.json, both verifier sources, PREREG.md,
PROOF.md, MODEL.md, README.md and SOURCES.md. The original #1369 proof,
model and verifier source at its disclosed head informed the primary
source review. The native equations were compared with Canon v97's
selector and generator definitions. The independent verifier was read
only after its author reported completing it without reading any other
verifier; this review does not claim independent authorship of that code.
The external physics descriptions were reviewed as explicitly inherited
provenance, not independently repeated experimental or literature work.

Neither verifier was executed or imported for this review. No numerical
experiment, formal gate or target-search run was performed. Source
inspection and algebraic reasoning supplied the findings below. The
prospective support manifest and public byte readback remain the
coordinator's final custody steps before any scientific execution.

## Fixed recipe and operator checks

The 22 chronological macros have four exchanges, seven top-level pair
masks, two singleton controls and nine direct carrier pulses. In the
singleton schema the target pair label precedes the control label:
`["single",14,5,1,2]` means control M1=2 and target transition (0,1).
The first two unconditional writes precede their cancelling masks.

The three exchange projectors commute on the complete pair space. On
the chosen two-level square their sum is I+P, giving -P for either
geometric sign. On an equal label outside that square the three blocks
instead give i times the geometric sign. Both implementations preserve
and explicitly test this outside phase. It is never visited on the
ready-memory transfer sector. The four ordered exchanges therefore give
the original nonzero-selector minus sign, and the four final 2pi memory
pulses cancel it without erasing the retained label.

The two complement masks use beta=-pi/2; together with the preceding
positive pi rotations they act only on {2,3,4}. Five other direct masks
use beta=+pi/2. The two singleton macros use the three original angles
(+pi/4,+pi/4,-pi/4). Their completed target actions match every native
table entry. Disjoint predicates handle rotations on different target
pairs, so each active positive write reaches a target initially at zero.
There is no additional relative sign. The true monomial adjoints cancel
the control-frame phases; a phase-free permutation is not substituted.

The full helper signatures comprise four exchanges, twelve distinct
abstract masks and two singleton controls. Their intended signed-column
coverage is respectively 200, 600 and 100. The full-program checks use
the two uniform sign choices. Arbitrary mixtures of the six edge signs
follow analytically from the complete helper identities for each sign;
the uniform program cases alone are not described as exhaustive mixed-
sign enumeration.

## Exact implementations and resource accounting

Both implementations use rational polynomial arithmetic modulo X^8+1,
with X=exp(i*pi/8), and no floating-point tolerance. Static inspection
checked multiplication reduction, root exponents, half-angle carrier
coefficients, negative-angle phases and complex conjugation. The primary
propagates actual primitive words; the independent implementation builds
complete local matrices and composes them on the physical registers.
Their target equations reproduce the fixed native generators, including
the R2 decode/apply/encode offset and its selector 1.

The two sources implement the same declared canonical cycle compiler,
not competing optimizers. The affine layout audits cover every needed
physical edge and the integer multiplicities supporting the scalar
self, spectator and stationary local-profile contributions. The
unchanged 500-loop word contributes 61200 carrier pulses per G.

The prospective total is 12+52=64 G blocks and 32000 completed LS loops.
The edge exponents for {14,k}, k=2,...,7, are (4,4,16,16,20,4). Thus the
recorded Gamma_new includes every physical G occurrence and is common
to the required inputs. The forward upper bounds are consistent:

```text
carrier pulses <=64*61200+32+7*14+2*42+2+4+3=3917023;
absolute carrier angle/pi
 <=64*61200+16+7*13+2*(36+6/4)+2+8+3=3916995;
switching boundaries <=3917023+32000+1=3949024.
```

These are analytical bounds. Actual canonical counts are to be reported
by the first publicly pinned run, not asserted as executed results here.
The laboratory phase uses the actual new duration, not its upper bound
or the predecessor's duration. The incident optical-energy account is
kept distinct from a finite quantum work-source construction.

## Negative control, inverse scope and acceptance limits

With all LS loops replaced by the specified equal-duration waits, every
exchange and mask becomes identity while every carrier remains in the
schedule. The surviving word has M1=0 and q=s, but its unconditional
writes set p1=2 and p4=1. Every s!=0 fails the memory target, and s=0
fails those two data coordinates. The preregistered control is therefore
0/25, not the predecessor's 5/25. It does not assert a general prohibition
on carrier-only protocols.

The inverse check uses the assembled operations: reversed primitive
adjoints in the primary and conjugate-transposed actual macro matrices
in the independent implementation. Its scope is algebraic. No negative
LS duration, physically executable reverse program or inverse resource
bound is inferred. Every forward G token remains a positive occurrence.

The preregistration freezes zero tolerance, disclosed analytical
expectations, the new identifier, source custody, bounded execution and
failure disposition. It requires the public pin and byte readback before
execution and preserves any failure without changing this candidate.
The required new architecture checks cannot be inherited from #1369.

No blocking mathematical or implementation defect was found by static
inspection. Acceptance authorizes final custody and the specified
prospective audit; it does not predict a passing execution or certify a
device. Preparation, joint geometry calibration, physical accumulated
error, additional modes, finite controller/work states, occupied-memory
reuse and the full later history remain outside the established scope.
