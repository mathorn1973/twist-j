# P-J-ODD-MOTOR-MEDIATED-BRIDGE-2 result

Status: **MEDIATED-BRIDGE-CERTIFIED in the single formal local run; public two-architecture gate pending.**

Layer: **L1 exact arithmetic, finite representation theory, and exact linear algebra only.**

The accepted verifier at pin `835d68c9c451cc1a8a62f6ff1437450b909d24d5` exited 0 with empty stderr and emitted the exact `EXPECTED.txt` bytes. No frozen falsifier fired locally.

## Decision

```text
MEDIATED-BRIDGE-CERTIFIED
```

This decision means exactly the frozen G1-G8 route passed in the accepted exact audit. It does not create a Canon or registry row. The public architecture gate remains pending until the PR workflow reproduces the same stdout on x86_64 and aarch64.

## What passed

1. **Native no-go.** Over `Q(sqrt5)`, the public step characteristic polynomial factors into the two frozen irreducible quadratics, so the generated native algebra has exactly two primitive nonzero invariant sectors. The naive third native mediator route is negative.
2. **Odd block graph.** For all five tokens the exact projectors have ranks `1,1,2`; the direct odd `P-R` block and all odd diagonal blocks vanish, while every `P/R-C` cross block has rank one.
3. **Second-order bridge.** For every token `B=P A C A R` has rank one and satisfies `B^sharp B=(5/4)R` and `B B^sharp=(5/4)P`. The normalized magnitude is therefore `sqrt5/2`.
4. **Mediator-line geometry.** The squared overlap of the two active lines inside `C` is exactly `1/5`.
5. **Negative controls.** None of `D,D^2,D^3,D^4,D+D^-1` exhibits the same direct-zero / one-mediator-nonzero pattern for any ordered sector pair in the frozen control family.
6. **Schur/resolvent audit.** The mediator sector has the frozen zero eigenvalue under `H=g+g^-1`; elimination gives orientation-independent magnitude `sqrt5 t^2/(2z)`. At token 2 the independent 24-term determinant is exactly `z^4+(5t^2-4)z^2+5t^4`.
7. **Quadratic lift.** Exact character arithmetic gives `Sym^2(V)=1+epsilon+2V`, `dim End_G(Sym^2 V)=6`, the invariant `q_+` line and the quadratic-sign `q_-` line.
8. **Selection boundary.** Pairwise direct Hom spaces among `1,epsilon,V` vanish and the frozen trilinear census passes. The repeated `2V` component remains nonselected.

## Negative result retained inside the positive probe

The native-carrier three-sector route is **closed negative**: there are only two primitive native invariant sectors. The mediated bridge appears only after the already-frozen affine token decomposition. This distinction is part of the result, not an inconvenience to be hidden.

## Scope firewall

No physical resonance is claimed. The pole at `z=0` is an algebraic resolvent pole only. No phonon, amplitudon, ferroaxial order, material, susceptibility, frequency, damping, temperature, laser/light coupling, quantum-state control, Born rule, probability, observer, decoder, force, spacetime, SI value, or L2-L6 lift is assumed or concluded.

Maximum possible later status after the required architecture gate and a separately locked fold is **T at L1 only** for the written algebraic theorems. The present probe changes no Canon, Registry, Frontier, Evidence, Gate, dependency, status, tag, or release file.
