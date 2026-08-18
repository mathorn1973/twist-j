# RESULT C-ENTANGLEMENT-LOCAL-RELATION-PYTHAGORAS-1-N

Status: **NON-CANONICAL incubation result**. One local symbolic lane only. No public status, no Canon/Registry/frontier move.

Lock: issue #422. PREREG commit `a9b4acd484bd977a0167f51205fd990923a64391`. Breaker frozen before positive verifier at `fd351e135588690c5a12afa4da1b1823f18c5f78`.

## Verdict

```text
PYTHAGOREAN-PURE
```

For normalized pure two-qubit states, local one-qubit definiteness and relational concurrence are exactly Pythagorean complements.

## Exact chain

For

```text
rho_A = (I + b.sigma)/2,
```

one has for every qubit state

```text
det rho_A = (1-|b|^2)/4.
```

At pure two-qubit scope the predecessor relation gives

```text
det rho_A = ||r||^2,
C = 2||r||.
```

Therefore

```text
|b|^2 + 4||r||^2 = 1,
|b|^2 + C^2 = 1.
```

Equivalent local-purity form:

```text
Tr(rho_A^2) = (1+|b|^2)/2
            = 1-C^2/2,
2(1-Tr(rho_A^2)) = C^2 = 4||r||^2.
```

## Schmidt angle

Write

```text
s0 = cos theta,
s1 = sin theta,
0 <= theta <= pi/4.
```

Then

```text
|b| = cos(2 theta),
C = sin(2 theta),
||r|| = (1/2) sin(2 theta).
```

Thus the pure two-qubit local-unitary quotient is the quarter unit circle in coordinates `(|b|,C)`.

Endpoints:

```text
product: |b|=1, C=0,
Bell:    |b|=0, C=1.
```

This is the exact right-triangle counterpart of the Schmidt rectangle from #419. The rectangle has sides `s0,s1` and area `||r||=s0 s1`; doubling that area gives the second Pythagorean leg `C=2||r||`.

## Mixed-state breaker

For the Werner state at `p=1/2`,

```text
rho_A = I/2,
|b| = 0.
```

The state is Bell diagonal with eigenvalues

```text
5/8, 1/8, 1/8, 1/8,
```

and the standard Wootters concurrence is

```text
C = 5/8 - 1/8 - 1/8 - 1/8 = 1/4.
```

Hence

```text
|b|^2 + C^2 = 1/16 != 1.
```

The Pythagorean equality is therefore not a mixed-state law.

## Scope

The right triangle is state-space geometry, not an ordinary spatial triangle. It does not establish two separately conserved substances called local reality and relation. Both legs are invariants/readings of one pure joint state. The result does show an exact complementarity: at fixed global purity, loss of local Bloch-vector length is exactly converted into pure-state concurrence.

No TWIST-J decoder, Born sampling, CHSH apparatus, force, spacetime, or L2-L6 lift is supplied.
