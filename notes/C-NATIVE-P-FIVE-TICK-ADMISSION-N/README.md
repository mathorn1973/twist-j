# Five-tick grid obstruction and the selector-admission task

**PUBLIC / NON-CANONICAL / L1. Analytical follow-up and proposed task.**
A. M. Thorn. SPDX-License-Identifier: Apache-2.0.

The section-2 corollary is candidate-T, pending independent scientific
review and a separate fold. This is not a registered public claim status.

Restricting the original update to repeated five-tick starts does not
remove the recurrence obstruction. The concrete next obligation for the
five-phase construction is admission of its changed operation selector.
The native counter and the native alphabet already exist; the permission
to actuate a different letter at a given state has not been supplied.

## 1. Sources and scope

| Source | Pinned public content | Use here |
| --- | --- | --- |
| Current authority | [Public Canon at main dc162f03](https://github.com/mathorn1973/twist-j/blob/dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d/canon/CANON.md), Public Canon v103 ACTIVE | Original U, internalized clock, synchronization and admission boundaries |
| Complete reference | [#1629 CONTRACT.md](https://github.com/mathorn1973/twist-j/blob/217cfc13befc3ab4b14444aed49e3fce7f50a7b7/notes/C-NATIVE-P-CONTACT-REALIZATION-N/CONTRACT.md) | Entire Y_(8,3), full F_P, local receiver, bank, Weyl and resource obligations |
| Recurrence and declared correction | [#1631 PROOF.md](https://github.com/mathorn1973/twist-j/blob/1088233f1b0d3945a6a76bad497950cf5d1d4f2a/probes/P-NATIVE-P-RECURRENCE-BOUNDARY-1/PROOF.md), especially sections 2, 3, 5 and 6 | Difference transport, synchronization argument and exact five-phase V |
| Frozen result scopes | [#1631 RESULT.md](https://github.com/mathorn1973/twist-j/blob/1088233f1b0d3945a6a76bad497950cf5d1d4f2a/probes/P-NATIVE-P-RECURRENCE-BOUNDARY-1/RESULT.md) | Literal-class exclusion, declared extension and unresolved native P |

The five-grid corollary below is a new analytical consequence of that
proof. The predecessor preregistered starts at every n>=3 and explicitly
left other start sets unclassified. This note states and proves one such
extension separately; it does not retrospectively widen the frozen
preregistration, finite audit or result. Its premises include the cited
proof candidates and the inherited synchronization theorem. No public
claim is promoted.

The predecessor head is 1088233f1b0d3945a6a76bad497950cf5d1d4f2a.
Successful checks and a text/status review of that head do not constitute
complete independent scientific acceptance. This follow-up also does not
supply such acceptance.

## 2. Exact corollary for the five-tick grid

Use raw coordinates x=(p1,p4,p1p,p4p,q,r) in F5^6 and

```text
z(x)=sum(x) mod 5, theta(n)=s_2(n) mod 2,
f_t(x)=g_(z(x)+2t mod 5)(x), g=(a,b,c,d,e),
U(n,x)=(n+1,f_theta(n)(x)).
```

Let U_M mean componentwise literal U on any fixed finite M>=1 original
cells with one common actual native counter, incremented once per tick.
Fix any integer N0>=3 and the admitted start set

$$
G_{N_0}=\{n\ge N_0:n\equiv0\pmod5\}.
$$

Retain all the following conditions:

| Condition | Exact requirement |
| --- | --- |
| Complete target | The entire Y_(8,3) with the permutation F_P from the reference contract |
| Encoding | Enc(n,y)=(n,e_n(y)), with faithful full-state decoding; e_n may be arbitrary, nonlinear and different at each n |
| Repeated equality | U_M^5 Enc(n,y)=Enc(n+5,F_P(y)) for every n in G_(N0) and every y in Y_(8,3) |
| Fixed raw ports | Disjoint source and receiver coordinate sets S_N and R_N across the complete M-cell carrier |
| Source-local readiness | At every admitted start the two reference witness inputs have equal encoded coordinates everywhere outside S_N, including all receiver and auxiliary coordinates |
| Present read | One receiver function of the current R_N projection, common current n and fixed common parameters agrees with the reference record throughout the complete encoded domain |

The witness is the reference pair with mu=1 versus 4, common
(q,p,u,v,b,c,d)=(1,0,1,-1,3,0,+1), common Weyl labels and fixed
spectators. Its accepted reference outputs have opposite receiver
records +1 and -1. No changing external record or source-dependent
common context is admitted.

**Corollary.** No realization satisfying these conditions exists, for
any finite M or any fixed lower bound N0.

**Proof.** For every n in G_(N0) with n-10>=N0, both predecessor starts
n-5 and n-10 remain in G_(N0). Since F_P is a permutation, two uses of
the repeated equality give, for every y in the entire reference shell,

$$
\operatorname{Enc}(n,y)
=U_M^{10}\operatorname{Enc}(n-10,F_P^{-2}y).
$$

Every actual nine-tick block synchronizes all original sheet labels;
the synchronized graph is forward invariant. Thus every encoded state
in every cell at such a late n satisfies

$$
z=4+2\theta(n-1)\pmod5.
$$

This conclusion uses full-target surjectivity and repeated simulation.
It makes no assumption that early encodings were already synchronized
or belonged to a special prepared orbit.

Choose r>=1 large enough that n_r>=N0+10, where

$$
j=4r+2,\qquad n_r=2^j-4.
$$

Since 2^4=1 modulo 5, we have 2^j=4 modulo 5 and n_r is on the admitted
grid. Also n_r+4=2^j has one binary one. The number
n_r-1=2^j-5=(2^j-1)-4 is the j-bit complement of 4, so it has
j-1=4r+1 binary ones. Hence

$$
\theta(n_r-1)=\theta(n_r+4)=1.
$$

By the exact synchronized difference formula in the predecessor proof,
with B swapping p1 with p1p and p4 with p4p and fixing q,r,

$$
\Delta x_{n_r+5}
=(-1)^5 B^{\theta(n_r-1)\oplus\theta(n_r+4)}\Delta x_{n_r}
=-\Delta x_{n_r}
$$

in every cell. For the encoded witness pair the initial difference is
supported only in S_N, and multiplication by -I retains that support.
The output receiver coordinates therefore agree. The current clock
and all permitted common context also agree, so the one present reader
returns equal records. Simulation of the reference requires +1 and -1,
a contradiction.

The times n_r are unbounded. Removing any finite prefix of the five-grid
therefore does not help. The proof does not classify arbitrary sparser
subsets, variable durations, independent clocks, moving ports, changed
preparation or additional coupling. A single prepared one-shot transfer
is compatible with the corollary. Adding finitely many literal original
cells with the same clock retains all its hypotheses.

## 3. Where the declared five-phase law crosses the class

The predecessor selects X=X_0 union X_4 and C_t=tau^(-2t) f_t, where
tau=e composed with d is raw q translation by one. Its declared V uses
the actual n as follows. At phase n mod 5=0 it executes the original
selector. At phases 1,2,3,4 it executes temporal d,d,d,d when the block
bit is zero, or e,d,e,d when the block bit is one. Every operation
advances n, and the complete phase carriers and inverse are supplied
in the pinned proof. Thus V^5(n,x)=(n+5,C_theta(n)(x)) at block starts.

Here is a direct comparison on an actual point of that complete carrier.
Let xplus=(1,1,0,0,3,0), so z(xplus)=0. At the block start n=5,
theta(5)=0 and the common first selector step is a, which fixes xplus.
Consequently (6,xplus) belongs to V's full phase-1 image.
At n=6 we also have theta(6)=0, and:

| Update at (6,xplus) | Selected operation | Complete output |
| --- | --- | --- |
| Original U | a, since z+2 theta(6)=0 | (7,(1,1,0,0,3,0)) |
| Declared V | d, since phase=1 and theta(5)=0 | (7,(1,0,3,4,3,1)) |

The original output has z=0, whereas the declared output has z=2. The
required next V phase at n=7 has sheet set {2,3}; original U does not
even map this legal input into that next prescribed slice.

The complete block also distinguishes the laws on that same input.
The actual bits at n=5,6,7,8,9 are 0,0,1,1,0. Direct substitution gives:

| Starting at (5,xplus) | Actual temporal word | Complete five-tick output |
| --- | --- | --- |
| Original U | a,a,c,e,b | (10,(3,1,0,0,1,4)) |
| Declared V | a,d,d,d,d | (10,xplus) |

This calculation identifies the exact departure: **V replaces the
literal native operation-selection law.** It is not merely the same U
observed every five ticks. These comparisons establish a different
one-tick law and a different five-tick map on V's literal carrier. The
separate corollary supplies the stronger full-P impossibility under
arbitrary encodings in its stated class.

The counter n and theta(n) are already native in
[CANON section 2](https://github.com/mathorn1973/twist-j/blob/dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d/canon/CANON.md#2-time-space-and-the-decoder).
Making the program phase a function of n supplies a closed mathematical
rule. It does not establish permission for that rule to override
g_(z+2 theta(n)). Likewise, writing a finite controller as additional
original cells leaves their literal product uncoupled. An interaction
that lets one cell steer another changes the transition law and needs
its own admission.

This distinction has a direct canonical precedent:
[QDD-PORT-QUOTIENT-ORIGIN-BOUNDARY [T]](https://github.com/mathorn1973/twist-j/blob/dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d/canon/CANON.md#qdd-port-quotient-origin-boundary-t)
exhibits the commanded word b,d,b,e for a constant translation, while
explicitly withholding actual native commandability. Its separate
controller theorem keeps its own factor-class scope; it is not being
used as a theorem about every possible controller here.
Similarly,
[DEF-RESIDUAL-CONTACT-ARCHITECTURE](https://github.com/mathorn1973/twist-j/blob/dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d/canon/CANON.md#def-residual-contact-architecture)
declares its extended architecture, extra controls and reading couplings
as supplied inputs, without asserting their independent native or
physical selection.

## 4. Concrete successor assignment: admit the actuation first

**Object.** Supply an independently admitted native coupling or control
mechanism that justifies the changed selector used by this particular
five-phase construction, or explicitly freeze a different realization
contract. A new command word or another literal common-clock product
does not by itself discharge this assignment.

The admission submission must contain the following objects before it
claims realization of P:

1. **An assumption ledger.** For each condition in section 2, state
   retained or changed. Name the exact replacement for every changed
   condition. In particular distinguish a new selection law or cell
   interaction from a restriction of observation times. If preparation,
   ports, duration, clock or context also change, state them explicitly.

2. **The complete apparatus.** Give the entire legal carrier A, every
   data/controller/work/memory coordinate, the clock, the actual
   one-tick W and its full inverse between the legal time slices. Include
   occupied states, every program branch and block-bit change. A
   controller's actuation of the data must occur in W itself. Any loader,
   reset, fresh tape or preparation needed for repetition must have its
   own declared state, transition and resource account; none is implicit.

3. **An admission certificate for actuation.** For each added operation,
   name the exact public source, pinned commit, claim status, scope and
   remaining premises that permit it to occur in the apparatus. Justify
   the state-dependent choice and its coupling to the data, as well as
   the individual letter formula. A primitive whose occurrence is only
   stipulated remains NEW_DECLARED. Autonomy, reversibility and alphabet
   membership alone do not change that status. A physical interpretation
   must name its separate cross-layer gate if one is claimed.

4. **A full-carrier compilation target.** If five actual ticks and the
   retained correction are claimed, supply faithful K(n,x)=(n,k_n(x))
   and prove

   $$
   W^5 K(n,x)=K(n+5,C_{\theta(n)}x)
   $$

   for every admitted five-grid start and every x in X_0 union X_4,
   together with the actual inverse, code-image invariance, complete
   auxiliary evolution and the source-local preparation/readback
   conditions. Any evolving auxiliary that cannot be represented by this
   complete-state equality must enlarge the comparison before a pin.
   Matching the two exposed points is insufficient. Keep the n+5 blocked
   contract distinct from the n+1 compound contract; no identity
   theta(5n)=theta(n) is available. A different timing proposal must state
   its own equality and is assessed at that different scope.

5. **An admission and resource decision.** Account for every participating
   register, cell, tick, control operation, stored bit, preparation and
   retained residue, and for any claimed conserved quantity. An unknown
   physical cost is unresolved, not zero. If the admission source is
   missing or conditional premises remain open, the construction stays
   DECLARED_EXTENSION_ONLY and full native P stays
   STOP_ADMISSION_UNSUPPLIED, even if its algebra is exact.

Only after that admission is established does the next stage prove the
whole-P obligations: a faithful encoding and one present receiver read
on all Y_(8,3), exact forward and inverse simulation, both bank bounds
and refusals, all occupied states, the complete Weyl action including
central phase, and the full resource account with retained spectators.
The corrected two-input acquisition witness supplies none of these
global identifications by itself.

This is the narrow successor of #1630/#1631 for the actuation of their
specified correction. It does not claim the broader source-control,
H_B-admission or conditional-contact work owned by
[#1398](https://github.com/mathorn1973/twist-j/issues/1398),
[#1498](https://github.com/mathorn1973/twist-j/issues/1498) and
[#1624](https://github.com/mathorn1973/twist-j/issues/1624).
No owner or queue status is reassigned.

## 5. Evidence discipline and current dispositions

This note contains an analytical derivation and a proposed assignment.
It introduces no scientific executable, run, expected-output file or
new computational result. A later executable investigation requires a
new unique formal probe, complete preregistration, source/code pins,
public readback before execution, exact recorded output and the required
architecture checks under the then-current POLICY and AGENTS rules.
The sealed predecessor identifier is not reused or resumed.

Same-session analytical reading of this follow-up is distinct from
external independent scientific acceptance. Operational checks of a
notes-only change do not verify this corollary numerically or complete
scientific acceptance of the predecessor.

| Question | Disposition after this note |
| --- | --- |
| Original frozen literal class in #1631 | NO_REALIZATION_IN_FROZEN_CLASS, with its original scope unchanged |
| Repeated five-grid variant with all section-2 conditions | Also excluded by the separate analytical corollary above, pending review as NON-CANONICAL work |
| Corrected C and five-phase V | DECLARED_EXTENSION_ONLY |
| Complete native P, bank, Weyl action and resources | STOP_ADMISSION_UNSUPPLIED |

The missing object is now specific: a natively justified mechanism that
actually enforces the changed selection law, with every state and cost
included. The grid restriction itself does not supply it.
