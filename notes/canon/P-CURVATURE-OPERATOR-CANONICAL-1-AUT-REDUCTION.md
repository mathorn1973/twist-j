# P-CURVATURE-OPERATOR-CANONICAL-1: affine reduction and EMPTY-obstruction disposition (NON-CANONICAL)

Status: `DRAFT / PROPOSAL-LOCAL-ALGEBRAIC-LEMMA / STOP-DEFINITION`

This note answers the practical affine-solver question left by
`P-CURVATURE-OPERATOR-CANONICAL-1-DEFINITION-CANDIDATE.md` and records the
correct disposition of its unreachable `CHILD_EMPTY` route. It is not a
public definition, probe, verifier, run, Canon change, or status proposal.
It changes no Canon object and authorizes no promotion. The scheduler stays
`STOP`.

## Authority pin

```text
Canon:              Public Canon v15
state:              ACTIVE
tag:                canon-v15
activation commit:  8f4e176c5d76f519d3493e56e438aba7856e1f01
content commit:     a850753348583e611bf7ccd5aa074030dc7e12f5
Canon SHA-256:      53237ec25b3782e833367c998c049d19459189a21c2a36638dd9e1600335976b
Canon bytes:        89288
owner row:          CURVATURE-OPERATOR-CANONICAL [O]
gate:               GATE-L1-L2-CURVATURE-CANONICAL
child candidate:    CURV-PRIMITIVE-REYNOLDS-CHILD-1
merged parent:      PR #114, source commit
                    91d08878685def0b950ca826f90ed02359bb2adc
public main readback: 3f6500afe1ea71fb60f7c7d81da9a2d4d05d2ba3
owner disposition:  V15-OWNER-FOLD-107-109.md
scheduler:          DECODER_CORE / ROOT / STOP / FORMAL
```

The merged parent and this reduction remain non-canonical and are not
authority dependencies. The owner disposition rejects the three proposed
parent filters by a structural `NONUNIQUE` no-go and retains this child only
as enrichment. A different pre-result parent surface is required before a
proposal-local definition can be frozen.

## 1. Exact affine reduction

The child definition declares an affine architecture-equivalence solver with
a finite fallback bound `120 * 5^42`. The fallback is decidable but
impractical. On the declared proposal-local equations it reduces exactly as
follows.

```text
Lemma 1 (selector slope).
    pi_bar(z_6(x)+2 eps) = z_6(h(x))+2 eps

holds for every x and eps. Because z_6 is surjective, comparison
at eps=0 and eps=1 forces

    pi_bar(z+2)=pi_bar(z)+2  for every z in F_5.

Therefore pi_bar is one of the five cyclic shifts of the generator labels.
```

For the public generators, the linear parts of `d` and `e` are both `-I`.
They are the only two members of the five-label family with that central
linear part. Conjugation must preserve the unordered pair `{d,e}`. No
nonzero cyclic shift preserves that pair, so only the identity label
permutation remains.

For the identity label permutation, write `h(x)=Mx+t`. The equations are

```text
M A_g = A_g M,
M s_g + t = A_g t + s_g,      g in {a,b,c,d,e},
1^T M = 1^T,
1^T t = 0.
```

This is a linear system in the 42 entries of `(M,t)` over `F_5`. Exact RREF
has coefficient and augmented rank 42 and the unique solution

```text
M=I_6,
t=0.
```

For each of the other four selector-compatible cyclic shifts, the
coefficient rank is 42 and the augmented rank is 43, so the system is
inconsistent. Hence, on the complete declared affine search,

```text
Aut_arch_aff = {identity}.
```

Independent exact read-back from the public generator formulas also checks
that all five generators are involutions, `(bc)^5=id`, and the `{b,d}`
action has 819 orbits. Thus the mean-zero carrier for the historical
`S={b,d}` row has dimension 818.

These are proof-first proposal-local calculations. No stdout hash, private
two-platform report, or unresolvable incubation artifact is offered as
public evidence.

## 2. Consequences for the child definition

The practical affine-solver question is proposal-locally resolved:

1. a future checker can preserve all 120 label permutations;
2. 115 are rejected by the selector equation before the affine system;
3. four cyclic shifts receive exact inconsistency certificates;
4. the identity shift receives the rank-42 unique-solution certificate.

The `5^42` enumeration fallback is therefore not reached for this declared
system. A future public checker must still implement and certify this exact
reduction; this note is not that checker.

Because the affine group is trivial, affine equivalence merges no two
distinct typed exact-equality classes. Any later uniqueness would have to
come from the frozen candidate inventory and admissibility itself, or from a
separately named prior principle. It cannot be manufactured by this affine
quotient.

## 3. The EMPTY obstruction remains

The controlling predefinition fixes the parent outcomes as

```text
EMPTY       zero admissible equivalence classes
UNIQUE      exactly one admissible equivalence class
NONUNIQUE   at least two admissible equivalence classes
STOP        incomplete, inexact, or non-reproducing classification.
```

The child retains zero operators, and `S=empty` gives a
positive-dimensional carrier. Therefore at least one admissible child class
exists and `CHILD_EMPTY` remains unreachable.

The tempting retype

```text
EMPTY iff every surviving class is a zero class
```

is rejected here. It changes the public meaning of `EMPTY`, reads the
operator value during outcome routing, and can turn one nonzero plus one or
more zero classes from `NONUNIQUE` into `UNIQUE`. That would manufacture
uniqueness by discarding counted classes.

A diagnostic label such as `ZERO_ONLY` may be reported inside a future
inventory, but it is not a parent outcome, creates no row or gate, and does
not repair acceptance item 8. The present child remains a necessarily
nonempty enrichment classification unless a prior owner fold supplies a
different complete surface without result-dependent filtering.

## 4. Exact disposition for the next day

```text
CLOSED PROPOSAL-LOCALLY:
    affine selector reduction;
    exact Aut_arch_aff inventory;
    practical affine-solver resource obstruction.

STILL OPEN:
    a complete parent surface with all four outcomes reachable;
    public checker and completeness certificate;
    canonical selector or other prior admissibility principle;
    parent gate and formal preregistration.

FORBIDDEN:
    retyping ZERO_ONLY as EMPTY;
    deleting zero rows after inspection;
    promoting a child result retroactively;
    creating a formal probe from this note.
```

`CURVATURE-OPERATOR-CANONICAL` stays `[O]`, the scheduler stays `STOP`, and
the frontier, gates, dependencies, and Canon remain unchanged.
