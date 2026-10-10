# P-U-NATIVE-FIXED-READ-1 — result

Status: PUBLIC, NON-CANONICAL, candidate-T, L1.
Formal audit: PASS.
Author: A. M. Thorn.
Reservation: [issue #1429](https://github.com/mathorn1973/twist-j/issues/1429).
Source authority: Public Canon v100 at
c164b79ce134152ac7cd600421791df74113f29f.

## 1. Conclusion

The original dynamics performs a concrete one-shot change of an independently
occupied receiver, with the SAME receiver-local reading before and after the
operation and a permanently readable result afterward. Two scalar effects
have a shared source preparation and shared local readers. Their preparation
context can be read from existing receiver coordinates at the input, at the
output and throughout the later continuation.

The first frozen exact audit passed by both direct-coordinate and separately
authored homogeneous-matrix methods. The complete declared affine
preparation class has twenty members; four satisfy the additional
zero-offset, coefficient-sum-one condition.

This establishes preparation-to-reading identities under the unchanged
source law. It does not establish a renewable physical contact, the full
three-cell gates from PR #1428, or the energetic contact law from PR #1424.
The physical bridge remains open at preparation, usable connections,
instrument access and calibration.

## 2. Actual native operation and retained reading

All arithmetic below is in F5. The six raw coordinates are
\((p_1,p_4,p'_1,p'_4,q,r)\); the complete carrier also includes the native
counter. The launch time is exactly zero. On the initial trace sheet H0,
the first three actual ticks select \(a,c,e\), giving

\[
F=U^3|_{H_0},\qquad
F(a,b,c,d,q,r)=(d,c-r,b+1,a+r+3,q+1,r+1).
\]

These are selected native ticks, not a freely chosen generator word.
The word and earlier occupied-receiver arithmetic are inherited from
[#1001](https://github.com/mathorn1973/twist-j/issues/1001#issuecomment-5666743909).
The new conjunction is independent occupied input, the same local reader,
and permanent later retention. Blank-receiver persistent writing was already
established in
[#999](https://github.com/mathorn1973/twist-j/issues/999#issuecomment-5662855170).

Write

\[
S=p_1+p_4+p'_1+p'_4,\quad
X=2(r-q)+1,\quad
M=2[(p_1-1)(p_4-3)+(p'_1-4)(p'_4-2)].
\]

The common two-coordinate source code is
\((q,r)=(u+4,4u+1)\). Each four-coordinate receiver code depends only on its
own independent input \(y\).

| Preparation | Receiver raw code | Same-reader endpoint effect |
| --- | --- | --- |
| P | \((4y+3,3,y+4,0)\) | \((X,M)=(u,y)\mapsto(u,3y+3u)\) |
| Q | \((2y,3,3y+4,3)\) | \((X,M)=(u,y)\mapsto(u,2y+4u)\) |

The receiver result \(M\) is invariant under every later selected generator,
so it is readable at every time \(n\ge3\). The source reading \(X\) is retained
across the complete three-tick operation only; it is not asserted to stay
fixed afterward. This is one cell partitioned into two plus four coordinates,
not three independently evolving original cells.

There is also a persistent SUM with the same local reader:

\[
E_{\rm SUM}(s,t)=(t,0,-t,0,-s,s),\qquad
\sigma=3(r-q),\qquad
R=(1-S^2)(p_1+p'_4)+S^2M.
\]

At preparation, \((\sigma,R)=(s,t)\). The actual three-tick output is

\[
(0,-t-s,1,t+s+3,1-s,1+s),
\]

and the same \(R\) reads \(t+s\) at every \(n\ge3\). The source reading is
\(s\) at the initial and third ticks. All 25 independent pairs \(s,t\) are
admitted, including an already occupied receiver; \(s=0\) preserves \(t\).
The all-time conclusion follows from the exact stable-generator invariants,
not from a finite trajectory cutoff. See [PROOF.md, Sections 2–6](PROOF.md).

## 3. Preparation classification and context

For the fixed source code and readers \(X,M\), the complete affine receiver
class is defined by \(p(y)=p_0+yv\), \(S(p_0)=S(v)=0\),
\(M(p(y))=y\), and an affine output \(Ay+Bu+C\) for all independent \(u,y\).
Both exact methods examined all \(125\cdot125=15\,625\) candidates, including
zero directions, and found the same complete twenty-row list.

The additional conditions \(A+B=1\), \(C=0\) leave exactly four preparations:
two with effect \(3y+3u\), and two with effect \(2y+4u\).
Their completeness is also proved algebraically. These are declared
conditions on one reader/preparation class; they do not select a unique
physical law. The full class also includes other gains and offsets.

For the selected P and Q rows above, define the fixed receiver-local context
reader

\[
K=(p_1-1)^2+(p'_1-4)^2,\qquad
T=(1-S^2)\,2p'_4+S^2\,2(K-1).
\]

It reads 0 on P and 1 on Q at the input, after the full three ticks and at
every later tick. No additional raw register or clock argument is used.
The endpoint equation on these 50 prepared inputs is

\[
(X',M',T')=(X,(3-T)M+(3+T)X,T).
\]

The pair \((X,M)\) alone does not determine this endpoint response. The two
raw inputs

\[
(3,3,4,0,0,0),\qquad (0,3,4,3,0,0)
\]

both read \((X,M)=(1,0)\), but their actual outputs are

\[
(0,4,4,1,1,1),\qquad (3,4,4,3,1,1),
\]

whose receiver readings are 3 and 4 respectively. The retained context
resolves this particular prepared-family ambiguity.

The context claim has an explicit internal-time limit: on P at \(u=1,y=0\),
the successive readings at times \(0,1,2,3\) are \(0,3,0,0\).
Thus \(T\) is not an uninterrupted binary pointer during the operation.
The endpoint equation cannot be iterated on its own output: later \(M\)
is frozen. This is a P/Q preparation-context label, not a realization of
the direct/alternative energy-contact label in PR #1424.
See [PROOF.md, Sections 5 and 7](PROOF.md).

## 4. Exact obstacles to a complete relative contact

The target is the full three-symbol map

\[
C_\kappa(x,y,a)=(x,y+\kappa(x-a),a),\qquad \kappa\ne0.
\]

The following are separately reviewed mathematical exclusions, each with
its stated carrier and preparation assumptions.

| Carrier and preparation | Exclusion |
| --- | --- |
| One six-coordinate cell, three independent nontrivial raw blocks, one common initial trace, any local codes/readers, fixed duration | Constant trace forces a 2+2+2 partition. Every selected word has a restricted dependency form that prevents simultaneous donor retention and dependence of the receiver on all three inputs. |
| One cell, receiver \((q,r)\), two piston donor pairs, arbitrary nonlinear independent codes and the same local readers, variable initial trace, origin zero | No fixed number of actual ticks realizes \(C_\kappa\). |
| One cell, every 2+2+2 partition, independent injective affine local codes, arbitrary nonlinear same local readers, variable or constant initial trace, origin zero | No fixed number of actual ticks realizes \(C_\kappa\). |
| Complete cells on one synchronized trace sheet with a common clock; only common native evolution and whole-cell permutations | In the actual free-evolution frame the full multiset of raw states is preserved, even for data-dependent permutation choices. Returned helpers cannot implement a nontrivial relative contact. |

The first statement is proved for every common word; the finite audit also
checks all 90 ordered pair partitions against all four possible piston
permutations, giving 360 maximal dependency cases and no survivor.

The varying-trace statements are analytic all-duration proofs, not conclusions
from this finite graph audit. The strongest affine statement allows trace
selection to vary with the prepared data and permits nonlinear readers.
It does not cover other block sizes, arbitrary nonlinear preparation at
every receiver position, other launch times, correlated inputs, adaptive
stopping or additional interactions.

In the whole-cell model, if helpers may change, their multisets must satisfy

\[
h_{\rm out}=h+\delta_y-\delta_{y+\kappa(x-a)}.
\]

A fixed data-independent bank supporting all raw inputs on a synchronized
\(H_z\) must therefore contain every one of its \(5^5=3125\) states.
This is a necessary supply bound, not a sufficient native controller.
It is distinct from the earlier energy-425 Gauss-shell cycle bounds.

Proofs: [PROOF.md, Sections 8–9](PROOF.md),
[VARIABLE-TRACE.md](VARIABLE-TRACE.md),
[AFFINE-THREE-PORT.md](AFFINE-THREE-PORT.md).

## 5. First execution and falsifier disposition

The complete nine-file input package was committed and pushed at

\[
\texttt{67fde06d2aec8cead7a0bf1bad3988e65c486cdb}.
\]

Every input was fetched back from that exact public GitHub commit and compared
byte for byte before any scientific execution. Public readback completed at
2026-10-09 09:53:37 UTC. The first run began at
2026-10-09T09:54:42.226649+00:00 and completed at
2026-10-09T09:54:42.595136+00:00 on Ubuntu 22.04.5 LTS, x86_64, Python 3.10.12.

The accepted command was:

    python3 probes/P-U-NATIVE-FIXED-READ-1/verify.py

It exited zero, emitted no stderr and produced the exact 2226-byte single
JSON line in [EXPECTED.txt](EXPECTED.txt), SHA-256

    1e44ca65502810c43914b99bdf77ba35840309f2a54a217e9a4cc035e507e0cc

The frozen input hashes were unchanged afterward. The complete command,
environment, hashes and byte counts are in [RUN.md](RUN.md).

| Audit domain | Actual result |
| --- | --- |
| All origin raw states, direct method | 15,625 checked |
| All H0 states against the complete affine word, both methods | 3,125 checked |
| Stable \(M,K\) preservation, direct method | 1,875 generator/state checks |
| Stable \(M,K\) preservation, matrix method | Exact quadratic-form identities |
| Entire declared affine receiver class, both methods | 15,625 candidates; exactly 20 preparations |
| Additional coefficient conditions | Exactly 4 preparations; all 100 inputs |
| Occupied SUM | All 25 independent inputs |
| P/Q context | All 50 inputs |
| Common-read/different-output witness | Input \((1,0)\); outputs 3 and 4 |
| Internal context failure witness | \(T=(0,3,0,0)\) |
| Maximal three-pair dependency cases | 360 cases; 0 survivors |

These domains overlap; their counts are not independent experiments.
Both complete template lists and all common witnesses agree. No
preregistered falsifier of the stated scoped claims fired. The two required
ambiguity/internal-context counterexamples were present; they reject the
stronger context-free and continuously binary interpretations as intended.
There was no repaired scientific source, changed threshold or second
attempt substituted for the first outcome.

The required unchanged PR workflow must independently compare the same
EXPECTED.txt and verifier hash on x86_64 and aarch64. This result record is
written after the first local run and before those PR jobs; their eventual
live check records establish the architecture gate. The local record alone
does not claim it.

## 6. What the physical search has gained

The scalar effect, its native chronology, an occupied receiver and a fixed
retained reading are now explicit in the same construction. P and Q can be
represented by different prepared receiver microstates under the same
source law. A context reading exists within those coordinates at the
declared input/output times.

The next source obligation is a mechanism that takes an ACTUAL output into
the ready input of another interaction, while accounting for other state
and every internal tick. The displayed ready preparations have \(S=0\);
the actual output has \(S=4\), and subsequent selected generators only
alternate \(S=4\) and \(S=1\). Waiting does not return this ready family.
Meanwhile the same receiver result is invariant, preventing another
nontrivial write by continued free evolution with this reader.

The excluded preparation classes and the whole-cell multiset theorem
identify concrete limitations of simple composition routes. They neither
derive a missing coupling nor forbid all possible realizations. A proposed
new route must state its raw carriers, preparation, actual source evolution,
local instruments, context, connections and treatment of the remaining
state. Its energy observable and physical units require independent
justification.

Review is documented in [REVIEW.md](REVIEW.md): separate assistant reviews
within a coordinated team, with disclosed contributions and exposure.
The matrix source was written and hashed before its author opened the
primary program. This is not blind external human confirmation.

The scope remains NON-CANONICAL, candidate-T, L1. No Canon, registry,
frontier, workflow or release is changed. No merge, physical apparatus
experiment, energy calibration, Hilbert-coherence derivation or complete
photon-phase model is supplied by this probe.
