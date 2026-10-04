# Two retained native carry records with one added trace-exchange capability

NON-CANONICAL L1, candidate-T proof. This is a constructive theorem in the explicit enlarged architecture of CONTRACT.md. It reports no execution or public status. The native write and invariant reader are inherited from #987; the added coupling, finite two-cell preparation and calendar are declared here.

## 1. The added exchange is generic and reversible

For a cell `psi=(P,q,r)` write `kappa=sum(P)` and `z=kappa+q+r`. The native coordinate transformation

`(P,q,r) -> (P,z,r)`

is a bijection of F5^6, with inverse `q=z-kappa-r`. In this chart the proposed new operation is simply

`(s,P,z,r) -> (z,P,s,r)`.

Returning to original coordinates gives

`C(s,(P,q,r))=(z,(P,s-kappa-r,r))`.

Applying it twice returns s and q to their old values, while P and r never move. Thus C is a permutation and involution of the complete `F5 x F5^6` carrier. It preserves both piston sums A and B. This definition refers to the canonical selector trace and contains no predicate, output reader, truth table or conditional source branch. Its availability is the one added operation; reversible arithmetic alone does not derive its physical availability.

## 2. Exact native quotient and protected set

Let `A=p1+p1p`, `B=p4+p4p` and `W=A^2`, all modulo five. Summing the canonical native coordinate formulas gives the following closed quotient:

| Generator | z' | A' | B' |
|---|---|---|---|
| a | z | B | A |
| b | -z | -A | -B |
| c | 2-z | 4-A | 2-B |
| d | 2-z | -A | -B |
| e | 3-z | -A | -B |

For c the r terms cancel in B. For d/e the constants in each piston pair sum to 0 modulo five. The selector is the original `(z+2theta_n) mod5`. Thus these identities remain exact with all omitted coordinates present; they are not an approximation to full-state feedback.

On `X14={z=1 or4}`, theta=0 selects b or e, respectively; theta=1 selects d or b. Consequently, under either driver bit,

`z'=4` if theta=0, `z'=1` if theta=1, `A'=-A`, `B'=-B`.

Hence X14 is invariant and W is constant under every subsequent native step, for every counter and every continuation of the bits. This is the existing #987/U-NATIVE-INVARIANT-AND-NOWRITE retention mechanism. A=B=0 also remains true there.

## 3. The native transient writes a predicate

For any full initial cell with prescribed quotient `(z,A,B)`, apply three actual native steps whose driver prefix is 011. The selected words, dictated by the selector, are

| Initial z | Chronological selected word |
|---|---|
| 0 | a,c,e |
| 1 | b,b,d |
| 2 | c,c,e |
| 3 | d,b,d |
| 4 | e,b,d |

This follows from `z -> z,-z,2-z,2-z,3-z` for the first selected map and substituting the next driver bit into the same selector. It is not permission to choose a generator word as a control.

Substituting the quotient table through the words gives

```text
z_after = 1,
(A_after,B_after) = (B+1,A+3) if initial z=0,
(A_after,B_after) = (-A,-B)  if initial z!=0.
```

In particular, whenever the entire starting cell has A=B=0, the output is in X14 with

`W_after=1` exactly when initial z=0, and `W_after=0` otherwise.

With the already declared affine encoding `z=a+1`, this equals the unit carry `c(a)=floor((a+1)/5)` for a in `{0,...,4}`. No nonlinear source preprocessing occurred: the source encoding and added C are affine, the original state-selected native transient produces the pointer, and the inherited fixed quadratic reader W reads the predicate. The same fixed W reader then retains this bit forever by section 2.

The proof needs A=B=0, not merely W=0. The #987 warning that a displayed zero does not specify a full ready state is respected. The full preparations and their transitions are exhibited next.

## 4. Complete architecture and first contact

The complete state is `(n,s1,s2,psi1,psi2)` with fourteen independent pentit coordinates and the counter. Initial data are

`(0,a1+1,a2+1,rho,rho)`, `rho=(0,0,0,0,1,0)`.

All 25 pairs a1,a2 are independent. The common receiver state contains no source value. The address law applies C to `(s1,psi1)` at n=0 and to `(s2,psi2)` at n=6, and nowhere else. After this stage at each n, both cells undergo their actual native update at that n, and n increases by one. All other state factors remain exactly as the complete law states.

At n=0, rho has z=1 and kappa=r=0. The first exchange gives

`s1'=1`, `psi1'=(0,0,0,0,a1+1,0)`.

This is exactly the existing #987 prepared family. The actual driver values at n=0,1,2 are 0,1,1. Therefore at n=3, the first receiver is in X14 and W1=c(a1). No later exchange acts on R1. Every later native step preserves W1, so

`W1(n)=c(a1)` for all n>=3.

This includes the entire second interaction. The first receiver's full checkpoint continues to evolve; it is its fixed record reading that remains unchanged. Nothing recomputes the first output from its consumed source.

## 5. The second ready state is reached without reset or holding

R2 starts at rho and has no contact before n=6. It evolves normally under the shared native counter. Direct substitutions into the full generator formulas give these complete checkpoints:

| Boundary n | R2 checkpoint `(p1,p4,p1p,p4p,q,r)` |
|---:|---|
| 0 | (0,0,0,0,1,0) |
| 1 | (0,0,0,0,4,0) |
| 2 | (0,0,0,0,1,0) |
| 3 | (2,1,3,4,0,1) |
| 4 | (2,1,3,4,0,4) |
| 5 | (2,1,3,4,0,1) |
| 6 | (2,1,3,4,0,4) |

The corresponding selected generators are b,b,d,b,b,b. Every row is source-independent. In particular at n=6, `kappa=0`, `r=4`, `z=4`, and `A=B=0`. S2 still holds its untouched independent value a2+1. The fixed second exchange therefore gives

`s2'=4`, `psi2'=(2,1,3,4,a2+2,4)`.

It leaves A=B=0 and sets z=a2+1. The actual driver bits at n=6,7,8 are again 0,1,1, since their population counts are 2,3,1. Section 3 applies to this full ready family even though its individual piston and r coordinates differ from rho. At n=9, R2 is in X14 and W2=c(a2). No further exchanges occur. Hence

`W2(n)=c(a2)` for all n>=9.

Together with section 4 this gives the permanent ordered record pair `(c(a1),c(a2))` after the two sequential contacts. The first contact is complete at n=3, strictly before the second begins at n=6. The second receiver was never reinitialized or paused; its common ready state was supplied at the start and its usable later state followed from actual U.

## 6. Independence, source exports and loss of information

R1 and its first contact depend only on a1 and the common counter. R2's evolution before n=6 uses neither source; its second contact uses only S2. Thus R1 is independent of a2 at every boundary, and R2 is independent of a1 at every boundary. Source slot S2 is unchanged through boundary n=6. It can be regarded as a previously unused independent input in a counted five-state port, not a hidden copy in the receiver.

The exchange exports the old trace. The complete source-slot output is therefore S1=1 after the first contact and S2=4 after the second; these values remain in the state. The original a values move into receiver q coordinates and are then processed by native U. They are not preserved by the composite protocol.

For example, the first receiver inputs a1=0 and a1=1 have identical full endpoints `(2,1,3,4,0,1)` at n=3 under their actual words b,b,d and c,c,e. With a2 fixed, all other complete factors also agree: S1 is already 1, S2 is the same unused input, R2 followed the same free trajectory, and the counter is the same. Therefore the COMPLETE enlarged states for `(a1,a2)=(0,0)` and `(1,0)` coincide at n=3 and remain equal forever, including n=9. This proves the whole protocol is not injective, despite the involutive added exchange. No discarded auxiliary is used to conceal this merger.

The result is consequently two composable predicate-recording contacts using two consumed inputs and two paid receiver cells. It is not a source-preserving permutation of two pentits or a full SUM operation.

## 7. Resource and timing accounting

At each fixed counter the enlarged state space is exactly `F5^14`; only 25 common-ready input states are used by this preparation. Two native cells are not embedded into one six-pentit checkpoint. The two source ports are explicit extra storage, including S2 while it awaits its contact. The single counter is retained, increases by one at every enlarged update and is never restarted. The complete law has two fixed address conditions n=0 and n=6 and two uses of the same C; neither address depends on a source value.

Through n=9, both receivers have made exactly nine actual native transitions. They make one more native transition at every later step. There is no controller halt, infinite blank-cell supply or subsequent rewriting programme. The pre/post-C states are algebraic factors of an enlarged update; they do not imply a zero-time physical interaction or identity with an unmodified single-cell U at that contact tick.

The following requirements remain admitted rather than derived: realization of the product carrier, its common initial preparations, an interface giving exchange access to the native trace coordinate, and the fixed addressing/activation law. No energy function or physical locality is assigned after the fact to make the operation cheap or conservative. Physical implementation of those mathematical resources is outside this L1 theorem.

## 8. A precise necessity boundary and no free renewal

If the exchanges are removed while retaining the same initial cells and passive source slots, both receivers begin in X14 with A=B=0. Their W readings are then permanently zero by section 2, independently of both fresh sources. Thus the native-only baseline cannot provide the demanded nonconstant source records on this declared preparation.

More generally, suppose an added intervention preserves A and leaves the addressed receiver in X14. Its W is unchanged during the intervention, and section 2 then preserves W through all subsequent native transitions. Thus, within this restricted actuator class and fixed reader, a nonconstant new write requires leaving X14, supplying a separately admitted transient carrier, or leaving the class of A-preserving interventions. Waiting alone supplies none of these changes. The chosen exchange preserves A and can set z=0 when the arriving source port is zero, explicitly taking the addressed ready receiver outside X14; native U then carries out the nonlinear writing transient.

The restriction to A-preserving interventions is essential. The added reversible shear `(s,p1,q)->(s,p1+s,q-s)`, with other coordinates fixed, preserves z and therefore X14 but can change A and W directly. Accordingly, invariance of X14 alone is no obstruction to arbitrary additional actuators. The necessity assertion here covers native-only continuation and the explicitly restricted A-preserving actuator class, not every interaction that preserves synchronization.

Our second receiver is paid in advance and unspent before its contact. The construction does not reset a used cell or demonstrate an unlimited cycle. The necessity result is restricted to this fixed W/receiver/continuation class; it is not a global proof that two cells or this particular exchange are minimal among all architectures.

## 9. Difference from existing conditional constructions

#987 already provides the transient carry write, common source-independent piston preparation, squared-pointer retention and the warnings about input mergers and fresh receivers. #1003 owns the broader full-endpoint readiness-family classification. This theorem reuses those conclusions with their disclosed status and supplies one particular interaction law and resource certificate for exactly two uses. The trace exchange is an additional declared primitive in this architecture, and the full evolution to the second usable ready state is proved rather than assumed anew.

#993's native-factor/freshness boundary, #994's native piston-slot exchange, #996's added q/exchange/rearming programme and #998's transported-port/native-actuation distinction remain prior ownership. In particular this is not a claim of first exchange coupling or general renewal, and the new scalar/trace operation is not identified with the already native two-slot piston exchange. The certificate concerns only the displayed preparation, two contact times, two complete receivers, consumed inputs and retained predicate readings.

#1349 instead conditionally factors a source-preserving SUM through a degenerate battery/helper carrier, with its own preparation, inverse pulse and source/counter-holding obligations. None of those gates or energies is supplied or reconstructed here. The present coupling is a trace-coordinate SWAP, the sources are consumed, the nonlinear operation comes from actual U, and the output is a pair of predicate records. The larger carrier and altered contact updates also lie outside the prior single-checkpoint full-product and literal-clock no-go premises.

The exact finite audit must still run only after the public pin and preserve full states, source exports and the merger. Its outcome and architecture status will be recorded separately. This proof supplies no physical apparatus, energy law, occurrence measure, detection semantics, material reset or indefinite renewal.
