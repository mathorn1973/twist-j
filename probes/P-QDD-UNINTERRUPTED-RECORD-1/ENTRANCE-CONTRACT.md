# Next decision: physical realization of the entrance interaction

**PUBLIC; NON-CANONICAL; definition-only successor specification;
STOP-DEFINITION.** This file belongs to formalization lock
[#1085](https://github.com/mathorn1973/twist-j/issues/1085). It is not a
preregistration of a physical experiment, an adopted physical apparatus, or
an extension of this probe's mathematical verdict. No scientific execution
or physical decision is reported here.

The accepted mathematical input is the
[uninterrupted-record note](../../notes/C-QDD-UNINTERRUPTED-RECORD-N/README.md),
merged in [#1084](https://github.com/mathorn1973/twist-j/pull/1084). Physical
ownership remains with `QDD-INSTRUMENT-APPARATUS [O]` and its existing O1/O2
obligations in the active Public Canon v90. The
[v89 physical contract](../../notes/canon/v89/PHYSICAL-CONTRACT.md) and
[#539's typed apparatus contract](../../notes/canon/DEF-TYPED-APPARATUS-RECORD-CONTRACT.md)
remain the broader specifications. This file isolates one necessary
entrance-interaction question; it does not replace their unfilled fields.

## 1. The fixed mathematical comparison target

Let `X=F5^6`, with `x=(p;z,r)`, `p=(a,b,c,d)`,
`q=z-a-b-c-d-r`. The code endpoints and their actual free evolution are

```text
Y_h=(h,0,0,0,1-h,0),                    h in (1,2,4,3),
Y_h(n)=N_(3,n-3)Y_h,                   n>=3,
K_n=span_C{|Y_h(n)>:h in (1,2,4,3)}.
```

The complex envelope is a mathematical comparison space. Its use here
does not identify complex amplitudes with physical preparations. The
canonical cyclotomic code is included in this envelope under a fixed
embedding and phase convention; that convention must also be named by any
physical dictionary.

On this code, `h_n(p)=(-1)^(n-3)(a+b+c+d)` has value `h` and
`f(1)=1`, `f(2)=f(3)=f(4)=2`. The off-code extension is the already declared
`f(0)=0`. Set

```text
T_delta(p;q,r)=(p;q-delta,r+delta),
C_n(x)=T_(f(h_n(p)))x.
```

`C_n` is the target to be realized, **not an available primitive**. The
next task does not assume a controlled shift, a projector-controlled gate,
or an equivalent target-dependent coupling as an independently supplied
operation.

A real entrance process can take time. Fix its launch counter `n` and
completion counter `n+d`, including whether cuts occur before or after each
native update. The comparison target with `d` native ticks elapsed is the
isometry on the code

```text
V_(n,d)|Y_h(n)>
  = |N_(n,d) C_n Y_h(n)>
  = |T_((-1)^d f(h)) Y_h(n+d)> .                            (E1)
```

Distinct `h` give distinct final source points, so this restriction is an
isometry. No unitary extension of the native point map on the whole of `X`
is assumed. Equality with `C_n` at the original counter is not the correct
comparison for a process that has consumed `d` ticks.

The initial comparison domain is **all amplitudes in `K_n`**, equivalently
all canonical shifted source vectors through `W_n`, not just the four
basis preparations, four observed frequencies, or a chosen source. It has
the common ready port `r_n^0`. Claims for initially displaced ports or
off-code states require a separately frozen wider domain. The off-code
definition of `C_n` alone does not impose a physical all-state claim.

The launch set `D_launch subset {3,4,...}` and duration function
`d(n,c)` are to be fixed with the physical class. A witness at `n=3` alone
is a one-phase witness. A claim for every `n>=3` requires one published
control/preparation law proving the universal statement; a new choice
after inspecting each source or desired result is inadmissible.

## 2. What must be fixed before a new realization test

Publish one immutable specification `A` before testing the target. Its
fields are grouped below; their types and exact equalities must be supplied
by a later profile, not inferred from these names.

| Field group | Required content | Present state |
| --- | --- | --- |
| Physical carrier and preparation | Actual source, port, clock, control, environment and stored-record degrees; allowed initial correlations; physically prepared code and ready state; source-off disposition; equality of the complete state. | UNRESOLVED |
| Architecture and ownership | Native checkpoint correspondence, interventions allowed by the proposed architecture, owner of energy/control/resources, and a full intermediate-state projection or relation to native variables. | UNRESOLVED |
| Independently available dynamics | Primitive interaction laws, admissible controls and parameter sets, evidence for their availability, preparation operations, capacity bounds and all allowed compositions. | UNRESOLVED |
| Context and time | Physical context and phase equality; target-independent selection of context and ready state; `D_launch`, `d(n,c)`, physical elapsed time and its native-counter alignment; synchronization and stop/completion law. | UNRESOLVED |
| Full comparison dictionary | Input/output encodings, complete retained auxiliaries and environmental outputs, common phase convention, old-record custody and exact whole-state comparison with (E1). | UNRESOLVED |
| Complete admitted class | Exact membership predicate, whole-law equality, resources, controls, durations and excluded architectures; proof or exact procedure covering all members at that scope. | UNRESOLVED |
| Physical evidence and decision | Independent justification/calibration and a consequence outside the target used to select the apparatus; separately named layer gates; positive and complete-negative proof procedures. | UNRESOLVED |

These are missing physical inputs. No choice of matrices in this probe
fills them. In particular, an abstract permutation decomposition or a
Hamiltonian logarithm of `C_n` is not independent evidence that its
interactions exist on a physical carrier.

The primitive family, resource bounds and physical admission criteria must
have a justification independent of passing (E1). They cannot be defined
as “all operations realizing `C_n`,” or “all maps including `C_n`.” A
later search may synthesize a circuit from an independently fixed family;
success then proves synthesis within that family. It does not derive the
family from `U` or select the apparatus independently for the physical
program. Those are separately stated obligations.

The declared class may be restricted. Its completeness means that every
operation admitted by its published physical assumptions is covered, with
all alternative controls, initial states and resources classified. It does
not mean that there is only one apparatus. Nor does it mean every physical
apparatus belongs to this restricted class. No finite decision algorithm is
promised for an unspecified class.

## 3. The full coherent witness equation

A positive witness must publish a complete physical transition law
`Phi^A_(n,d)` and faithful comparison encodings `E_in`, `E_out`. All source,
apparatus, environment, work/control stores, clocks and previous records
must be owned by their domain and codomain. The output comparison cannot
discard an unlisted environment to make the desired equation true.

For a profile admitting a linear amplitude realization, freeze a complete
pure-state description, or a named purification of every admitted mixed
preparation. Let `eta_in` be the independently selected ready apparatus
and environment state. Let `chi` denote admissible prior-record custody.
The clean entrance witness has the following exact equation, for every
code amplitude `psi`, not merely basis populations:

```text
Phi^A_(n,d) E_in(psi tensor chi tensor eta_in)
  = exp(i phi_(n,c))
    E_out(V_(n,d) psi tensor chi tensor eta_out).             (E2)
```

Here `eta_out` includes the residual apparatus, environment, controller,
clock and consumed resources. It need not equal `eta_in`. It must be
independent of the code input `psi`, including its LOW/HIGH content.
The common phase is fixed by the declared comparison convention and cannot
depend on `h`. Preparation selection and the new interaction cannot be
controlled by `chi`; any retained administrative provenance or passive
custody transport must be explicit in the encodings and must preserve the
complete old records under their full equality.

The equation must remain valid when the code is correlated with an
untouched reference: replace `psi` by every vector in `K_n tensor H_R` and
`V_(n,d)` by `V_(n,d) tensor I_R`. This forbids a construction that silently
dephases the code, measures the fine label first, or hides which-HIGH
information in an environment. If a physical description has no linear
amplitude structure, it must supply an exact comparison relation with the
same coherent inputs, outputs and correlations; calling an unrelated point
transition “the same map” does not satisfy (E2).

For an exactly linear channel on a fixed ready preparation, an equivalent
reduced comparison can be checked on all sixteen matrix units
`|Y_h(n)><Y_l(n)|`, including the twelve off-diagonal ones, with target
`V_(n,d)|Y_h(n)><Y_l(n)|V_(n,d)^*`. The profile must additionally account for
the full retained output and prove its claimed environment and custody
factorization. Four basis-state probabilities alone are not this test.

If a proposed implementation instead leaves declared coarse-dependent
auxiliary states, its full target must say so explicitly:

```text
sum_h alpha_h |V_(n,d)Y_h(n)> tensor eta_(f(h)).
```

That is a different joint-state target from the clean (E2). It may preserve
all HIGH coherence when the three HIGH auxiliaries are the same under the
frozen phase convention, but its LOW/HIGH coherence includes those
auxiliaries. Distinct hidden states for the three HIGH inputs do not become
harmless by forgetting their label. Such a proposal needs its own fixed
comparison and accounting before testing; it is not retroactively accepted
under (E2). There is no uncounted “garbage” allowance.

## 4. Finite duration, native evolution and architectural feedback

The accepted theorem controls free native evolution **between** completed
operations. It supplies no physical interpolation during the entrance
interaction. The candidate must specify `Phi^A_(n,d)` throughout its own
duration, including the actual control schedule, clocks and backreaction.
An endpoint agreement proves endpoint agreement only. If undisturbed
source motion is claimed during that interaction, the full intermediate
joint-state correspondence must prove that additional statement at each
declared time.

At completion, (E1) gives exactly the freely evolved code source and the
required displaced native port. To use the accepted waiting theorem after
this cut, the profile must also establish that the apparatus has stopped
coupling back to the native degrees and that subsequent evolution is the
declared native `U` with the declared auxiliary dynamics. This decoupling
condition is part of the witness, not a consequence of endpoint equality.
The sign and reference at the later archive exchange count *all* elapsed
native ticks since the target entrance cut, including `d`.

An ideal zero-duration boundary operation is a mathematical convention.
A physical finite-duration claim must provide positive elapsed physical
time and its exact synchronization rule. It cannot absorb a nonzero
duration into a renamed launch counter without proving (E1) at that new
cut. Nor may it assume that native evolution pauses while a gate is applied
without declaring that different dynamics.

The existing read-only architecture of #539 requires `feeds_U=false`.
The proposed entrance changes `q,r`, even though it preserves `p,z` and
even though a later operation restores the freely evolved checkpoint.
It therefore is not a conforming read-only profile merely because its
endpoint is restored. Its physical realization requires an independently
defined intervening architecture and explicit ownership of that change.
This contract does not modify #539, the selector, the native generators
or the public counter. A copy made entirely on an external carrier may be
read-only, but it is then a different target and cannot be identified with
native `C_n` without the corresponding dictionary and proof.

## 5. The one next existence question and its dispositions

After the unresolved groups in section 2 have been filled, let
`A_phys` be the **independently specified complete admitted family**, and
let `GoodEntrance(A)` mean that all its declared preparation, custody,
duration, dynamics, decoupling and physical-admission requirements hold,
and that (E2) holds universally on its frozen launch/context/code domain.
Define the solution set

```text
R_entrance = {A in A_phys : GoodEntrance(A)}.
```

The next attack asks exactly whether `R_entrance` is empty. It does not ask
for another longer waiting-time check or merely for an abstract extension
of a four-column target matrix.

| Disposition | Evidence required | Permitted conclusion |
| --- | --- | --- |
| POSITIVE | One physically admitted member with the full universal witness equation, independent physical input certificates and the gates required by its stated scope. | The entrance exists in the frozen family and declared domain. No uniqueness or complete measuring apparatus follows. |
| EMPTY | A proof covering every member of the fully defined admitted family that none satisfies the entrance requirements. Any empty physical premise class must be identified explicitly. | This precise entrance-realization route is excluded. No universal apparatus impossibility follows from a restricted family. |
| CANDIDATE-FAIL | A named construction violates a frozen requirement, with its exact counterexample retained. | That construction fails. This does not decide `R_entrance`. |
| STOP-DEFINITION / STOP | Missing carrier, architecture, admission evidence, equality, physical correspondence, class coverage, gate or exact decision. | No physical existence or impossibility conclusion. |

If an engineering version replaces exact equality by a tolerance, it must
freeze the full comparison norm, uniform domain, independently justified
error bound and failure threshold under a new scope before execution.
Agreement of a few observed populations cannot substitute for the exact
coherent target, and a numerical fit cannot silently lower its threshold.

This file's present disposition is **STOP-DEFINITION**. It makes the next
question and witness obligations explicit. It does not supply the missing
physical family or a proof deciding that family.

## 6. Existing ownership and the boundary of any success

The related public lanes remain separate:

- [#539](https://github.com/mathorn1973/twist-j/issues/539) owns the shared
  read-only apparatus/record definition, not an intervening implementation
  of `C_n`.
- [#996](https://github.com/mathorn1973/twist-j/issues/996),
  [#997](https://github.com/mathorn1973/twist-j/issues/997) and
  [#998](https://github.com/mathorn1973/twist-j/issues/998) concern transient
  actuation, orientation and actual-clock lifting. An orientation or
  transported port is not an interaction certificate.
- [#999](https://github.com/mathorn1973/twist-j/issues/999) through
  [#1006](https://github.com/mathorn1973/twist-j/issues/1006) own distinct
  one-shot, carrier, joint-erasure, collision, point-preparation and
  coherent-code questions. Their existing claims and negative boundaries
  are not reopened by this contract.
- [#1034](https://github.com/mathorn1973/twist-j/issues/1034) through
  [#1038](https://github.com/mathorn1973/twist-j/issues/1038) include native
  preparation/readback, nonlinear ready-channel capacity and mathematical
  Galois-channel or twenty-mode coupling work. A new entrance lane must
  identify its different preparation, operation and comparison domain;
  an already constructed target-based optical completion does not fill
  this contract's physical admission fields.

Issue [#1033](https://github.com/mathorn1973/twist-j/issues/1033) was also
checked because it appeared in the earlier chat inventory. Its actual scope
is full-prime Mobius boundary persistence, not the QDD apparatus. It is not
a scientific dependency of this contract.

These issue titles and scopes were inspected when writing this file. This
is a related-work boundary, not a claim that their full contents have been
reproved or their owners' locks transferred. Before any successor is
claimed, repeat the current issue, probe, registry and remote-head collision
scan required by `AGENTS.md`. This file reserves no second probe identifier.

Even a successful entrance witness leaves the exit interaction, material
archive and its persistence, fresh capacity and source preparation, actual
single event, ordered occurrence law and full post-event/reset behavior
to their owners. O1 still requires the total typed realized-event
transducer and sampling/occurrence obligations with its physical context,
ready phase and named layer gate. O2 still requires compatible terminal
event semantics with its independent consequence and completeness of the
physical apparatus family. An entrance result does not discharge either
by naming them. `QDD-INSTRUMENT-APPARATUS [O]` remains open; no L6 measure
or independent-trial law is inferred.
