# PREREG C-ENTANGLEMENT-LOCAL-RELATION-PYTHAGORAS-1-N

Status: NON-CANONICAL incubation. No Canon/Registry/frontier/status move.

Lock: issue #422. Predecessor #419 is NON-CANONICAL and supplies no public dependency. Current public authority remains Public Canon v51.

## Frozen state geometry

For a normalized pure two-qubit state, write the reduced state of subsystem A as

```text
rho_A = (I + b.sigma)/2
```

with real Bloch vector `b`. Let `r` be the determinant-line vector normalized as in #419, so `||r||=|det A|`, and let standard pure concurrence be `C=2||r||`.

## Frozen gates

G1: `det rho_A = (1-|b|^2)/4`.

G2: using the pure-state identity `det rho_A=||r||^2`, derive

```text
|b|^2 + 4||r||^2 = 1,
|b|^2 + C^2 = 1.
```

G3 endpoints and quotient: product `(1,0)`, Bell `(0,1)`, and the normalized pure 2x2 local-unitary quotient is the quarter unit circle in `(|b|,C)`.

G4 purity:

```text
Tr rho_A^2 = (1+|b|^2)/2 = 1-C^2/2,
2(1-Tr rho_A^2)=C^2=4||r||^2.
```

G5 Schmidt angle: for `s0=cos theta`, `s1=sin theta`, `0<=theta<=pi/4`,

```text
|b|=cos(2 theta),
C=sin(2 theta),
||r||=(1/2)sin(2 theta).
```

G6 mixed breaker: Werner `p=1/2` has `rho_A=I/2`, hence `|b|=0`, while standard concurrence is `1/4`, so the equality fails: `|b|^2+C^2=1/16`.

G7 wording firewall: this is state-space geometry. It is not a spatial triangle, not a conservation of two substances, and not a TWIST-J decoder/measurement derivation. `b` and `r` are different readings of one joint pure state.

Outcome: `PYTHAGOREAN-PURE`, `PARTIAL`, `F`, or `STOP`.
