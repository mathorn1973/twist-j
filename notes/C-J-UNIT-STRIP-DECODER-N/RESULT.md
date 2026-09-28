# C-J-UNIT-STRIP-DECODER-N result

```text
STATUS:             NON-CANONICAL INCUBATION
VERDICT:            PASS at frozen notes-only scope
ACTION LAYER:       L1 only
CANON CHANGE:       NONE
REGISTRY CHANGE:    NONE
PUBLIC PROBE:       NONE
```

No frozen mathematical falsifier fired in the accepted pinned execution.

## Candidate mathematical result

**[candidate-T] J-strip normal form.** Every nonzero element of
`Z[zeta_5]` has a unique decomposition

```text
alpha = J^n beta,       n in Z,       0 <= c(beta) < 1.
```

The strip is decided without logarithms. If
`beta bar(beta)=u+v phi`, then

```text
beta is reduced  iff  v <= 0 and u + 2v > 0.
```

**[candidate-T] Binary carry.** Products of reduced representatives require
one carry `e in {0,1}`, and the carry obeys the associativity cocycle.
The ramified witness is

```text
(1-zeta_5)^2 = -sqrt(5) J.
```

**[candidate-T] Orbit-count identity.** Using the already public
`O_K^x=mu_10 x <phi>`, `h_K=1`, and `<J>=<phi>` modulo torsion,
the strip contains exactly ten representatives per nonzero integral ideal:

```text
|B_X| = 10 A_K(X).
```

The proof also gives a complete finite coefficient box.

## Finite exact audit

**[candidate-C, one architecture]** The pinned verifier and the separately
implemented non-blind breaker agree norm by norm through 1000:

```text
|B_940|  = 3110
|B_941|  = 3150
|B_1000| = 3410.
```

The lattice enumeration and the independently coded ideal Euler recurrence
agree for every norm from 1 through 1000. The complete bound for X=941 has
coordinate radius 9; the breaker found no reduced norm<=941 point on the
next coordinate shell 10.

## Selected native scalar specialization

**[candidate-D dictionary with candidate-C capacity witness]** The public
theorem `U-COUNTER-REACHABLE-AMPLITUDE-CLASS [T]` already classifies every
exact reader on the origin-zero reachable domain as

```text
R(n,x) = L^n G(ell_n(x)).
```

Set `L(alpha)=J alpha`. Order the reduced strip representatives by
`(norm, coefficient tuple)` and map the 3125 base-five labels injectively to
the first 3125 elements of `B_941`. This chosen dictionary gives

```text
R_J(n,x) = J^n b(ell_n(x)),
R_J(U omega) = J R_J(omega).
```

For `n>=3` the strip inverse recovers the native counter and the conserved
five-label chart. The uniform algebraic norm is at most 941.

Nothing selects this lexicographic codebook. It is an existence witness, not a
canonical decoder.

## Sharp capacity statement

**[candidate-T reduction; candidate-C endpoint]** In the frozen class of
nonzero integral scalar readers which are U-to-J equivariant, globally
injective across the union of all reachable sheets `n>=3`, and uniformly
norm-bounded, distinct native labels must occupy distinct J-orbits. Hence

```text
X_min = min { X : |B_X| >= 3125 }.
```

The finite exact audit evaluates this minimum as

```text
X_min = 941.
```

This is a coding threshold for the declared scalar-reader class. It is not a
new physical constant and it does not apply to fixed-time injectivity alone.

## What changed conceptually

The important correction from the initial conversational framing is that the
existence of an equivariant native reader is not new. Public Canon already
contains the stronger classification theorem
`U-COUNTER-REACHABLE-AMPLITUDE-CLASS [T]`. The new content is the arithmetic
normal form and the exact finite capacity of one integral scalar
specialization.

## Remaining selection debt

The native theorem leaves both the target bijection `L` and assignment
`G` arbitrary. This result chooses `L=times J` and a lexicographic G; it
does not derive either choice. Therefore the next scientifically meaningful
question is not another existence construction but a selection or no-go
theorem for structurally constrained codebooks.

No physical clock, Born law, Hodge amplitude, apparatus, event, measure,
SI scale or L2-L6 bridge moves.
