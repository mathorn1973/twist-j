# P-DMATTER-TOTAL-1 Route A Owner Decision

Status: OWNER-ADOPTED PROPOSAL, DEFINITION-ONLY, NOT CANON
Layer: MULTI
Candidate status ceiling after later normative authority action: D
Scientific computation authorized by this note: none

Authority readback:

```text
Public Canon tag:       canon-v23
Activation commit:      4ac41b4fac3a3794a6e9d5be1e2027d324edb806
STATUS content commit:  7830d852229ffc06c9d287d026c8ece290bf339b
CANON SHA-256:          f842b613d6f65fe07ddab92ddbe1fb9fec89217d52b781571b7380281c3fb2b1
CANON bytes:            116017
```

This note records an ownership decision. It does not promote a theorem, close
`QUADRATIC-DECODER-DATA`, move that row out of `STOP`, create a registry row,
or authorize a formal probe.

## 0. Falsification first

The decision is invalidated or stopped under any of the following conditions.

`CIRCULAR`
: A purportedly independent `D_direct`, one of its fields, or its
  implementation is defined through `Qcan`, `F_Gram`, `N_G`, the adopted
  Route A write rule, or a shared factorization helper before factorization is
  tested. Because `F_Gram` and `Qcan` are already public, a newly drafted
  `D_direct` cannot create retroactive blind independence. Only an immutable
  earlier public pin from an independent definition source can qualify.

`FIRE-POSTHOC`
: After any classification or definition-consistency result is opened, the
  candidate class, equivalence relation, `B0`, five-class semantics, effect
  list, instrument list, or meaning of an output is changed.

`NONUNIQUE(k)`
: Exactly `k >= 2` inequivalent alternative global decoders or admissible
  instrument families survive the frozen equivalence relation.

`EMPTY`
: No admissible total typed decoder exists inside the frozen candidate
  universe on the frozen domain.

`STOP`
: Any carrier, domain, bridge, equivalence, layer gate, manifest field,
  transport, or completeness proof is missing.

`DEFINITION-CONSISTENT` for a dictionary defined through `Qcan` is not an
independent factorization result. It cannot discharge
`QUADRATIC-DECODER-DATA`.

## 1. Owner decision

Route A is adopted for definition work:

```text
beta -> iota_B0 -> R_cyc

D_scoped := R_cyc o iota_B0 o beta
D_scoped  = F_Gram o Qcan o beta
```

The second equality is a derived identity of the adopted definitions. It is
not a blind scientific target.

This chain is the scoped `D_quadratic` write dictionary. Its candidate status
ceiling is `D` after a later normative authority action. It is a declared part
of the model, not a derivation of the unique physical decoder.

The following interpretations are frozen.

1. `R_cyc` is a realization of the Gram-side record. It is not an independent
   `D_direct`.
2. The five complete typed record classes in the existing `C5`
   classification are alternative global decoders. They are not simultaneous
   physical sectors.
3. The standard power basis and the complete selected candidate are distinct:

   ```text
   B0  = (1, zeta, zeta^2, zeta^3)
   c_0 = (0, B0, iota_0, L_0, H_0, Pi_0).
   ```

   Selecting `c_0`, whose basis component is `B0`, as the physical write
   dictionary is a new explicit choice among the five proposal-local
   candidates. It remains visible in the model header and is not a theorem of
   physical canonicity.
4. `Adm_GalSplit` is not adopted. Its conditional algebraic selection does not
   supply an independently frozen physical principle.
5. No basis, window, or complete-record difference is added to gauge merely
   to recover uniqueness.

The existing source surfaces remain:

- `P-DMATTER-TOTAL-1-PREDEFINITION.md`
- `P-DMATTER-TOTAL-1-DEFINITION-CANDIDATE.md`
- `P-DMATTER-TOTAL-1-CYCLOTOMIC-REALIZATION.md`
- `P-DMATTER-TOTAL-1-BRANCH-CLASSIFICATION.md`

This decision does not silently strengthen any status carried by those files.

## 2. Relation to existing owner guidance

Upon reviewed merge and public-main readback, this note supersedes only the
Issue #107 routing in `V15-OWNER-FOLD-107-109.md` that retained Route B as the
conservative default pending a separate owner decision.

It preserves every other load-bearing boundary of that ruling:

```text
Adm_GalSplit               NOT ADOPTED
D_direct                   UNRESOLVED
QUADRATIC-DECODER-DATA     O / STOP
formal probe               FORBIDDEN
```

Merge and readback freeze owner guidance only. They do not grant status `D`,
complete a public manifest, create a gate, or change a Canon row.

## 3. Obligation split

The parent row `QUADRATIC-DECODER-DATA` remains `O / STOP`.

The owner decision separates four claims that must not be conflated.

```text
QDD-SCOPED-WRITE-DICTIONARY
    Candidate D only after a complete public manifest, exact definition audit,
    and later normative authority action. It excludes physical uniqueness,
    canonicity, and independent factorization.

QDD-INDEPENDENT-Q-FACTOR
    O / STOP.
    D_direct must have an immutable earlier public pin from an independently
    owned definition source. The required test is
    D_direct = F o Qcan o beta on the complete named domain.

QDD-PHYSICAL-EFFECT-SELECTION
    O / STOP.
    The physical admissible instrument family must be selected from the kernel
    and apparatus, not inserted as an unnamed input.

QDD-HYBRID-CARRIER-BRIDGE
    O / STOP.
    The algebraic hybrid label construction may be used as a definition
    candidate for the exact class dictionary. Its identification with the
    physical gyron decoder still requires a separately falsifiable bridge.
```

No registry row is created by this note. These names delimit obligations for
the definition package. Registry ownership requires a later reviewed public
fold.

## 4. Coupling-first measurement rule

The classified physical object is the instrument family `{K_a}`. Its effects
are registered shadows and certificates:

```text
E_a = K_a^sharp K_a.
```

The reverse inference is forbidden. Equality of effects does not identify
post-event instruments. Equivalence must therefore be frozen at the `K` level
as well as at the `E` level.

Every admitted physical effect must publish:

```text
effect_id
instrument_id
the exact K_a
the exact E_a
the verified equation E_a = K_a^sharp K_a
outcome_id
Born pairing
normalization and completeness equation
the exact MatterData fields that read the effect
```

A missing `instrument_id`, missing `K_a`, or missing exact certificate routes
`QDD-PHYSICAL-EFFECT-SELECTION` to `STOP`.

Exact completeness, positivity in the frozen Gram form, normalization,
outcome semantics, record semantics, and coarse-graining must be stated before
enumeration.

## 5. Hybrid carrier typing

`Veff` is a finite set, not a module. Define the linear carrier and its
injection first:

```text
V_lin = span_Q(Veff) = Q^4
j_lin : Veff -> V_lin.
```

Let `L_label` be a finite-dimensional rational label module and freeze a
separate gyron-label map:

```text
ell_gyron : GyronObject -> L_label.
```

The hybrid carrier, its Gram form, and the combined injection are

```text
C_hyb      = V_lin tensor_Q L_label
G_hyb      = G tensor I_L
j_hyb(v,g) = j_lin(v) tensor_Q ell_gyron(g).
```

`C_hyb` is the carrier and `G_hyb` is its Gram form. The coefficient ring,
dimension and basis of `L_label`, equality on labels, the role of the label,
and the domains, codomains, equalities, maps, and public layer gate for
`j_lin`, `ell_gyron`, and `j_hyb` must be frozen.

This note makes no theorem claim that the algebraic carrier is the physical
carrier. A non-public result cannot be imported as a public theorem by this
owner decision.

## 6. Required public manifest

Before any registry change or executable definition audit, the following
fields must be public, exact, and mutually typed.

```text
A01 coefficient ring and involutions
A02 K0, Veff, V_lin, j_lin, GyronObject, L_label, ell_gyron, j_hyb,
    and the complete totality domain
A03 beta, including the pre-update or post-update convention
A04 exact B0, c_0, and iota_B0
A05 G0, G, dagger, transpose, and sharp as distinct typed operations
A06 Qcan as an ordered pair and the exact QCarrier equality
A07 ZERO/NONZERO total tagged codomain
A08 complete MatterData_quadratic field manifest
A09 exact write map and the owner of every field
A10 stage = D_matter and leg = D_quadratic for every READOUT field
A11 Born pairing, effect IDs, instrument IDs, and normalization
A12 complete dependency DAG and an exact acyclicity check
A13 layer endpoints and public gates for beta/iota/write and hybrid transport
A14 closure manifest, feeds_U, and write targets
A15 transitive hidden-input allowlist
```

An unregistered input, a partial map on the named domain, a dependency cycle,
or a missing transport returns `STOP`.

The A01 to A15 list is a QDD overlay, not a replacement for
`DEF-DECODER-COMPLETION-CONTRACT`. Every block and identifier slot required by
that public contract remains mandatory. `UNRESOLVED` routes `STOP`;
`NOT_APPLICABLE` is legal only in slots where the public contract explicitly
permits it.

## 7. Required exact controls

The future definition audit must cover the complete published finite surface,
not a sample:

```text
all 15,625 anchored inputs
all 313 Qcan fibres
the zero fibre of size 25
all 312 nonzero sign fibres of size 50
complete-record constancy on every Qcan fibre
exact ZERO/NONZERO totality with no null output
exact normalization
negative control WRONG-FACTOR-OMIT-G
byte-identical transcripts on two independent architectures
```

These controls verify the implementation of the adopted dictionary. They do
not grant status `D` and cannot raise a later status above `D`.

## 8. Outcome semantics

`DEFINITION-CONSISTENT`
: Every field of the adopted dictionary is total, typed, exactly normalized,
  and consistent with the frozen dependency graph. This can support a later
  scoped dictionary status `D`. It is not a blind scientific pass and does
  not prove independent factorization.

`INDEPENDENT-FACTOR-PASS`
: A `D_direct` with an immutable earlier public pin, frozen independently of
  `Qcan` and `F`, is constant on `Qcan` fibres and equals
  `F o Qcan o beta` on the complete frozen domain. Only this outcome can
  address the independent factorization residue.

`NONUNIQUE(k)`
: `k` inequivalent alternatives survive. They remain visible in the model
  account and are not promoted to gauge after the result.

`EMPTY`, `CIRCULAR`, `STOP`, and `FIRE-POSTHOC`
: Have the meanings frozen in section 0.

## 9. Status accounting

This owner decision permits definition work and nothing stronger.

```text
Route A dictionary                 owner-adopted proposal; candidate ceiling D
                                   after later normative authority action
C5 complete-record result          proposal-local NONUNIQUE(5) at its frozen
                                   root-injection scope; not a registry result
c_0 (with basis B0)                explicit five-way dictionary choice
Adm_GalSplit                       NOT ADOPTED
D_direct                           UNRESOLVED
physical effect selection          O / STOP
hybrid-to-physical carrier bridge  O / STOP
independent Q factorization        O / STOP
QUADRATIC-DECODER-DATA             O / STOP, unchanged
```

No result produced from this note may promote physical uniqueness, a
zero-discrete-choice claim, the physical effect list, the carrier bridge, or
the parent QDD row.

## 10. Next allowed actions

1. Complete and review the exact public manifest A01 to A15.
2. Freeze the `K`-level and `E`-level equivalence relations before any
   classification.
3. Run a static type, totality, normalization, dependency, and security audit.
4. Propose registry rows only after public readback of the complete manifest.
5. Open a separate physical-effect-selection probe only after its instrument
   class and falsifiers are frozen.
6. Open an independent factorization probe only if a qualifying immutable
   earlier public `D_direct` pin exists.

There is no formal scientific run and no Canon fold in this owner session.
