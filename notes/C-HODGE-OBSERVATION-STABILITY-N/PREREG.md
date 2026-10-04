# Preregistration: stability of Hodge observation and context changes

PUBLIC-source, NON-CANONICAL, L1 mathematics only. No authority or Canon change.
Candidate: C-HODGE-OBSERVATION-STABILITY-N.
Owner: A. M. Thorn / current 2026-10-04 synthesis session.
One scoped item: what exact predictive reductions retain under finite-precision
real reading and a change of fixed-axis context.

## Basis and lineage

Public Canon v97, main 2973a432303e046aacb2cee3cea97254ea3ab8eb,
content 82ecf0aac0ee79c947000968e71573d4c65d386d. All five normative hashes,
ancestry, Canon bytes and required architecture/check jobs were checked anew.
The prior C-MEMORY-TIME-CAUSALITY-N bundle is an attached reference, not authority.
The present item neither reopens it nor promotes its statements.
Inherited sources: J-HODGE-PREDICTIVE-CLOSURE,
J-HODGE-SEMILINEAR-MEMORY, J-C5-HODGE-CONIC-ATLAS,
J-HODGE-HERM2-LOXODROME and J-HODGE-RATIONAL-CLOSURE.
A prior Born-reading note already observes that Galois conjugation can be
discontinuous in one real embedding. No discovery priority is asserted.
This is a proof-first, result-exposed synthesis, not a blind discovery test.
No GitHub writes are authorized or performed by this export.

## Equations and carrier

V=A4 in the marked basis a_i=e_i-e_0 (i=1,...,4), H=I+11^T.
W=Lambda^2 V, wedge basis (01,02,03,12,13,23), beta matrix S.
G=Lambda^2 H, K=S G, K^2=5I, P_+=(I+K/sqrt(5))/2.
C is the root-basis action of (01234), M=I+C^2, L=Lambda^2 M.
Real comparisons use the positive real embedding sqrt(5)>0, with the
ordinary finite-dimensional topology on the plus output. Exact pair-coded
arithmetic has a different topology and is NOT excluded.

1. Pick the first standard integral basis vector u with P_+ L P_- u != 0.
Let (a_n,b_n) be integers with a_0=1,b_0=0 and
(a_(n+1),b_(n+1))=(9a_n+20b_n,4a_n+9b_n).
Define w_n=(a_n I-b_n K)u, an integral wedge vector.
Prove P_+w_n=(9-4sqrt(5))^n P_+u -> 0, whereas P_+Lw_n is unbounded.
The all-n and limiting conclusions are proof claims, not finite enumeration.

2. In the inherited real six-axis atlas, define T_P in W_- and
pi_P=P_+ + Pi_(T_P). For distinct P,Q show no function h on pi_P(W_R)
satisfies pi_Q=h composed with pi_P on all unchanged source states W_R.
Use w=t_Q-Pi_(T_P)t_Q, so pi_P(w)=0 and pi_Q(w)=(4/5)t_Q !=0.
This does not exclude simultaneous transport of state AND context by A5,
new source restrictions, or a differently defined physical chart family.

3. Simultaneous reads of one, two or any three distinct axes have ranks
4,5,6 on W_R. For any three normalized axes their Gram determinant is
2/5 plus or minus 2sqrt(5)/25, strictly positive. The same-source rank
claim is not a statement that these reads are physically implementable.

## Code and exact checks

verify.py is newly written, Python standard-library only. It builds the marked
integer matrices from definitions. It audits the Pell and projection identities
for n=0,...,32, and the scalar line-projection/Gram identities in Q(sqrt(5)).
It does not import an inherited verifier, enumerate a new complete atlas, test
native contacts, or invoke an empirical dataset. No floating-point assertions.
The complete inherited atlas theorem is a declared premise.

## Systematics and failure threshold

Exact equality only. Any failed identity or zero cross witness rejects the
corresponding mathematical clause; no tolerance or threshold adjustment.
The source class is unbounded in integral coefficient height. Bounded-height
or bounded-energy physical domains must be treated separately.
Continuity of a finite-step read is not bounded long-time error propagation.
No unrestricted nonlinear-encoding dimension bound is claimed.
No L2-L6 lift, physical event, time orientation, proper time, common physical
metric, native-U realization, or public T/F promotion is asserted.

## Freeze and status

PREREG.md and verify.py will be hashed before their first execution. Local
computation is one x86_64 lane and can support only candidate-C. Self-contained
new deductions are candidate-T pending independent review. No blind second
agent or two-architecture new gate is supplied. Shared handoff/promotion must
use reviewed Git; this package is a reference export only.
