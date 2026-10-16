# Frozen synthesis contract

**PUBLIC / NON-CANONICAL / L1.** Issue #1569; program #1548.

## 1. Authority and allowed writes

The authority is `mathorn1973/twist-j main`, Public Canon v102. The base and
peeled `canon-v102` are `a632c6a162dc87e60104d7a478e7650a6d5c4a1b`, with
content ancestor `b04e22dd3ed8e4240cff347364f24670d4183a4d` and annotated tag
object `5ffacfe5e13622f51460d274c9591a28ef37358d`. All five normative
checksums and both ancestry conditions were checked against raw Git.
`canon/CANON.md` is 1024033 bytes, SHA-256
`c0657380438c965f9556b5b298a34a5e799c48a68ce66e9fe51786ce2413d7d1`.

The actual completed successful workflows are main `38939750393`, tag
`38940217812` attempt 3 and release `38956254023` attempt 2. The last closes
the pending publication check reported by the earlier intake; the intake is
not retroactively described as having checked a future completion.

The only allowed output paths are:

```text
notes/C-V103-BRIDGE-SYNTHESIS-N/README.md
notes/C-V103-BRIDGE-SYNTHESIS-N/CONTRACT.md
notes/C-V103-BRIDGE-SYNTHESIS-N/PREREG.md
notes/C-V103-BRIDGE-SYNTHESIS-N/SOURCES.tsv
notes/C-V103-BRIDGE-SYNTHESIS-N/INPUTS.sha256
notes/C-V103-BRIDGE-SYNTHESIS-N/ACCEPTANCE.md
notes/C-V103-BRIDGE-SYNTHESIS-N/SYNTHESIS.md
notes/C-V103-BRIDGE-SYNTHESIS-N/CLAIMS.tsv
notes/C-V103-BRIDGE-SYNTHESIS-N/RESULT.md
notes/C-V103-BRIDGE-SYNTHESIS-N/PROMO-C-V103-BRIDGE-SYNTHESIS-N.md
notes/canon/V103-BRIDGE-PROPOSAL.md
```

The proposed Canon path was publicly enumerated in #1569 before this pin,
as required by the intake and POLICY section 5. There are no changes to
`canon/`, policy, workflow, registry, gates, source probes or existing notes.
The branch is `notes/C-V103-BRIDGE-SYNTHESIS-N`. Commits are additive, with
named-file staging and no amendment, squash, rebase or force push after pin.

## 2. Frozen source heads

| Role | Issue / PR | Specification | Admitted result head |
|---|---|---|---|
| A | #1550 / #1557 | `7b06ea6b377930f6edeb84cb330b9d69f1b82c51` | `5c8a675cc114dd3e1f4d95226fd22ba82e3891fa` |
| RA | #1559 / #1562 | `a19a2f38517863a480476abb35fa45bfa4dfdfeb` | `2bceaeafc47f0aa44cfc83bc99cf665dc969e24f` |
| B | #1553 / #1555 | `bc1648745323a8843d2c3cb831b0f585b4e00427` | `a12efb98551f972cdfebaa070baf051216ffe7ff` |
| RB | #1565 / #1566 | `5838eb457cf2ec966682d97f4652259a5d3d6291` | `6ffde281e82ad094bfefae17a2a6a25ac9b2a388` |
| C | #1554 / #1556 | `423c6f7488b35399ff40fcc30be01df526aba795` | `ed635a114bc52c4abbc16ea660bd4d89f2d2efde` |
| RC | #1567 / #1568 | `105d22bfc457f5e3f29dfa7b3ca75694b21670fd` | `35242926001bf48d03b78cedbb2daea814c992ff` |
| D | #1551 / #1558 | `9cb2b7d89eb1fc955fb67e886e46a379cb1aba43` | `c7b5be4634738738c85c936227bfe68b99ec3b7a` |
| RD | #1560 / #1563 | `2c9718dbb9661eebdfaf150affb5a3e25eda20fa` | `2a43c0312af7189b84c099c9482b908ac8e9323b` |

Additional immutable custody surfaces are RA first result
`dac3cd215314b2d426ecfebe76890e082df9691c`, RB first result
`ca4077448fa347ac4d6ff42eb41922de558c9f02`, RC first result
`8a6902c0dbbe81ea0a66d7d2af043371cac3b5f7`, and D original result
`e3d35709a86b42c21c1bf57e2be2b3a3cf707598`.

Abandoned B predecessor #1549 / #1552:
`066ef45911f6215f7574daba80fd53616ee1c66d` to
`1844322bbb1f0b9f08ceaa9b9081b078024226d3`.
Abandoned RB predecessor #1561 / #1564:
`46e0ba7e4dafd9bb391253c9e888cfc54db574c2` to
`8e8c3f0496f85588f40b78ead34e7420b5d7d01c`.
Neither is scientific positive evidence. `SOURCES.tsv` freezes raw bytes;
no author or reviewer source is imported into this branch.

The source roles remain separate sessions. Their documented exposure
barriers and Git chronology are audited as provenance, not inferred merely
from identical public commit authorship. Z is fully result-exposed.
Same-session assistants belong to Z and are not additional independent
reviewers. Existing #1528 work is not an input or prerequisite of Z.

## 3. Mathematical type contract

Native states are `x=(a,b,c,d,q,r)` in `F5^6`; `z=a+b+c+d+q+r`.
The driver starts at counter zero, `theta_n=popcount(n) mod 2`.
The piston projection is `pi_P(x)=(a,b,c,d)`, with
`h=(b+2a,d+2c)` and `W(a,b,c,d)=(b,a,d,c)`.

Integer vectors use the literal canonical field coordinates in `Z^4`,
with `H(y)=y^t B_f y/2`, `L=(I-A_f)(I-A_f^2)` and `det L=25`.
The zero piston kernel `K={(a,3a,c,3c)}` and integer shell residue subgroup
`G_L={(3s,s,3t,t)}` are distinct subsets of `F5^4`; `W(K)=G_L`.
Checkpoint gate membership, unit-preimage existence, a selected integer
representative, full source preparation, a complete receiver and a funded
contact are separate predicates and typed objects.

An integer minimum is taken over the whole specified infinite coset, not
over a sampled box. A finite census may support its attainment but cannot
replace the global lower-bound and uniqueness proof. A universal orbit
claim requires induction or an explicit counterexample; finite trajectories
are not universal evidence. The declared combination includes checking the
next native step after the named `n=3` residue against the five missing unit
residues, as a direct corollary of pinned formulas, without code execution.

Reading claims freeze the preparation family, counter origin, observation
projection, fixed-time context, and equality of complete receiver states.
PRESENT(0) and BLANK, full checkpoint and projected readout, and actual
fixed-time trajectories and finite support graphs are not identified.

The rational contact uses only `(q,r)` through its declared `eta` and `S`
maps. A common complete receiver and a common source-independent protocol
are explicit premises of any indistinguishability conclusion. Alternative
preloading into `(q,r)` changes those premises and is not a native transport
proof. The integer shell and rational carrier have no presumed common
energy-preserving full-state lift.

## 4. Discrepancy contract

No source summary is accepted wholesale. A false sentence is localized with
its exact source and excluded from every dependent proposal. Unaffected
proofs can be retained with an explicit dependency argument. A defect in a
central proof that cannot be resolved by admitted text yields HOLD for that
claim; no new search or silently repaired frozen source is allowed.

D is admitted only together with its additive errata and the scoped review
at [comment 6226001948](https://github.com/mathorn1973/twist-j/pull/1558#issuecomment-6226001948).
The frozen erroneous identification `h1=B+2A` is refuted; the true identity is
`h1+h2=B+2A`. For the one-shot family the valid proof is piecewise:
`h=(2 lambda,-2 lambda)` at `n=0`, `(lambda,-lambda)` at `n=1,2`, and
`(-2Bz lambda,2Bz lambda)` only on the ready tail at `n>=3`.
The tail parameterization must never be extrapolated to `n=1,2`.
The accepted correction is a corrective review, not a new blind review.

RB's independent central unit-shell, kernel, injectivity and coset-minimum
proofs are evaluated separately from its RESULT summary and optional
higher-shell remarks. In particular, proposed synthesis does not depend on
unproved coordinate/basis relabeling, `L=I-A_f`, `det L=5`,
`B_f=L^t L/5`, `A_f u-u=-Lu`, or an asserted uniform shell-2 minimum for
the four nonzero missing unit residues. Source discrepancies in scalar
substitutions, author bounds and predecessor histories must also be recorded.
No optional higher-shell repair is authorized.

## 5. Disposition and future question

The output distinguishes inherited statements, exact candidate results,
finite candidate evidence, scoped refutations and remaining obligations.
No scientific status is earned by synthesis alone. The optional C comparison
is explicitly bounded to the five declared unweighted cells and cannot
supply physical selection, uniqueness of order five or global minimality.

A proposed next interface problem may be stated but not executed. It must
declare message-sensitive source access, full preparation and receiver,
initial common-state conditions, readout context, funding, timing and a
falsifier. Gate arrival alone is a smaller diagnostic, not a funded
transmitter. The current unchanged `(q,r)` route for a common-quotient family
is judged at its exact scope before proposing any changed route.

Final disposition is submitted for another controller's review. Z does not
mark its own result independently accepted, merge it, or publish v103.
