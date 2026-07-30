# P-ENTROPY-LAW-REDUCTION-1 result

Status: PROOF-SURVIVES AT LOCAL AUDIT STAGE; PUBLIC CLAIM UNCHANGED

## Recorded decision

```text
pin integrity:              PASS
formal execution count:     1
local verifier exit:        0
local verifier stderr:      empty
finite audit:               13 of 13 PASS
written proof review:       PROOF-SURVIVES
fired falsifier:            NONE FOUND
GitHub replay:              PENDING
cross architecture:         NOT CLAIMED
scientific decision:        PROOF-SURVIVES, pending public PR replay and review
public Canon status:        UNCHANGED
ENTROPY-LAYER-BRIDGE:       O / STOP, unchanged
```

This result records a proof-first reduction theorem and its exact finite audit.
It does not construct a Route A map, prove `A_A` nonempty, prove `A_A` empty,
or close the public entropy bridge.

## The theorem that survived

Let `P` be any measurable total Route A map satisfying exact equivariance
`mu`-almost everywhere. Then

```text
Law_W(P)  if and only if  P_* mu = Uniform(R).
```

The proof has three exact parts.

1. The complete five-sheet trace automaton synchronizes after every allowed
   Thue-Morse word of length nine and forces

   ```text
   z_6(P(kappa,y)) = 4 + 2 kappa_-1 mod 5
   ```

   almost everywhere.

2. The public stationary pair law then forces, at every time,

   ```text
   selector law = (0,2/3,0,1/6,1/6),
   pair 00 mass = 1/6.
   ```

3. The source map preserves the product measure, so for every nonempty finite
   window

   ```text
   nu_(P,W) = P_* mu.
   ```

Thus the selector and pair clauses of `Law_W` are automatic under exact
equivariance, and the state clause is exactly the uniform-pushforward
condition.

## Finite audit

The accepted pinned verifier independently audited:

```text
A01  the integer J matrix, determinant, and inverse
A02  all five generators as involutions on all 15625 states
A03  all five generator trace laws on all 15625 states
A04  the complete two-row sheet transition table
A05  occurrence of all four legal Thue-Morse pairs
A06  the complete 24-word length-nine language certificate
A07  synchronization of every allowed length-nine word
A08  the final-bit sheet formula
A09  sharp failure at length eight
A10  the exact stationary pair fixed point
A11  the pair-to-selector map
A12  the exact selector distribution
A13  the frozen-window arithmetic
```

The local formal output is 13 of 13 PASS, exit 0, empty stderr, with exact
stdout SHA-256
`e99e828ff3f6531d6e660589c1c8da03f0e5d211a50faca26f968f23aa8c4ca6`.
The verifier is an audit of finite premises. It is not the source of the
universal measurable theorem.

## Failure-threshold disposition

```text
F1  generator trace law or branch table wrong                  NOT FIRED
F2  length-nine language list incomplete or excessive          NOT FIRED
F3  allowed length-nine factor not synchronizing               NOT FIRED
F4  synchronized output not fixed by final bit                 NOT FIRED
F5  source measure not invariant                               NOT FIRED BY PROOF
F6  pair law fails to give selector vector                     NOT FIRED
F7  counterexample to the equivalence                          NONE FOUND; PROOF SURVIVES
F8  census, finite-window limit, or unnamed lift imported      NOT FIRED
```

The almost-everywhere step uses a finite intersection of translated conull
sets, followed by a countable translated intersection for simultaneous time
indices. The measure step uses normalized Haar invariance under the compact
group automorphism `y -> Jy`. No recurrent-sheet census is used in the reset
proof. The action layer stays inside the already registered L2-to-L5 bridge
gate. No L6 physical measure is introduced.

## What remains open

The public positive closure target is now expressible without the redundant
window and selector clauses:

```text
Exhibit one measurable total P such that
P o tau_src = F_theta o P  mu-almost everywhere
and
P_* mu = Uniform(R).
```

The complete negative target remains the full theorem `A_A = empty`. Failure
of a cylinder, depth-five, fiberwise-bijective, inverse-system, or other
restricted construction is only a scoped STOP unless it classifies all of
`A_A`.

The existing non-canonical `notes/entropy-selection-recon` branch retains
ownership of transfer construction, finite-horizon optimization,
inverse-system, canonicity, and obstruction work. This probe does not replace
or absorb it.

## Status and repository firewall

No Canon, registry, frontier, evidence, dependency, gate, changelog, hash,
release, workflow, or authority file is changed by this probe directory. The
result earns no automatic public status. A later owner-reviewed fold may
consider the exact proof after the pull-request replay and review complete.

Issue #219 remains a tooling defect. This result makes no two-architecture
claim and does not rely on the flat legacy RUN parser to manufacture one.
