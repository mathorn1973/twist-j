# Preregistration: C-LOCAL-PAIR-EMISSION-N

Status: NON-CANONICAL; L1; candidate-T. No Canon authority is claimed.

Owner: the named local-pair-emission session under
[issue #1798](https://github.com/mathorn1973/twist-j/issues/1798).

Public basis: `mathorn1973/twist-j`, `main`,
`892a0b11089d34e241e1eb76d2c03247022d18e6`, Public Canon v105.
This note changes no Canon file, registry row or public status.

## Frozen equation and carrier

Let `J3` be the three-by-three all-ones matrix, `u = (1,1,1)^T`,
`b = u/sqrt(3)`, and `D = u^perp`. Let `p = (1,-1,0)^T/sqrt(2)` be a
declared residual-core label in `D`. On a half-line, let `S|n> = |n+1>` and
`L = 2I - S - S*`. The Hilbert space and Hamiltonian are

```text
Hspace = C^3 direct_sum (C p tensor l2(N0) tensor l2(N0)),
Hc     = I + 3 J3,
Hout   = 3 I + L tensor I + 2 I tensor L,
H      = [[Hc, g |u><delta00|],
          [g |delta00><u|, Hout]].
```

The parameter is a supplied rational `0 < g <= 1/4`; the fixed witness is
`g = 1/4`. No parameter is inferred from measured particle data. The
residual label `p` in the displayed off-diagonal block is implicit.

The output energy account is fixed as residual energy `1`, massive-channel
Hamiltonian `he = 2I + L`, and gapless-channel Hamiltonian `hnu = 2L`.
The gapless channel has quadratic low-momentum dispersion and is not called
a chiral or Weyl particle. Both coordinates are half-lines with a fixed
boundary; this is a pinned-core construction with no recoil.

## Proposed exact claims

1. The Hamiltonian is bounded, selfadjoint, strictly positive and local on
   the declared graph; pair creation occurs only at the common endpoint.
2. `D` consists of exact stable eigenstates of energy `1`.
3. The state `b` has no point or singular-continuous spectral component;
   its core survival tends to zero and its paired-output probability tends
   to one. Both outgoing excitations are present in that sector.
4. The continued bright resolvent has exactly one simple pole in
   `|z - 10| < 1/2`, on the specified local continuation through `(7,11)`.
   Its width `Gamma = -2 Im z` obeys
   `(3/2) g^2 < Gamma < (7/2) g^2`. Thus the fixed witness has
   `3/32 < Gamma < 7/32`.
5. The total energy, the declared charge assignment and the stated local
   probability and energy currents are conserved exactly.

## Method, code and data

Method: analytic proof with exact rational inequalities and spectral
integrals. There is no numerical verifier, input dataset, floating-point
fit, simulation-derived lifetime or formal gate execution in this note.
The public issue freezes the model and proposed targets before any
scientific computation. The targets and preliminary reasoning were already
visible to the coordinating session. Review is not represented as blind
confirmation.

## Failure thresholds and systematics

Any counterexample to one proposed exact assertion fires that assertion.
In particular: a bright eigenvalue, singular spectral component, wrong
continuation branch, pole outside the stated disk, failed width inequality,
unaccounted charge or energy, or a nonlocal coupling invalidates the
corresponding claim. No tolerance or threshold may be adjusted to rescue it.

The final half-line carrier is essential. Replacing it by two full lines
changes the endpoint spectral measure and can produce exterior bound
components. The full-line model is not used as evidence for these claims.

The pole width is not an exact exponential decay constant at all times.
No finite-clock approximation error is interpreted as a decay channel or
lifetime. The Hamiltonian and charge dictionary are supplied model premises;
they are not derived from the native TWIST-J update.

## Scope and promotion

Action layer: L1 only. The result is a candidate theorem about one declared
linear operator and carrier. Any particle identification, physical
occurrence, change of layer, derivation of the model premises or public
promotion requires a separate named gate. A same-session separate-context
proof review is useful adversarial checking, not a formal independent
two-agent confirmation or a two-architecture computation gate.
