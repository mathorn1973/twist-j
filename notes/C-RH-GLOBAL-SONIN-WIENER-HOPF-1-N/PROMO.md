# PROMO C-RH-GLOBAL-SONIN-WIENER-HOPF-1-N

```text
STATUS: NON-CANONICAL PROMOTION PACKAGE
ISSUE:  #360
PROMOTION: not executed
```

## What survives independent re-derivation

### A. Global Sonin / Toeplitz identity

The unconditional Suzuki intersection space satisfies exactly

```text
V(0) ~=_antiunitary S(Theta_xi)
     ~=_antiunitary ker T_(conjugate Theta_xi),
```

with the second equivalence understood through the fixed sharp map between the
two Hardy halves.

This is a cross-source/operator dictionary result. It uses no RH.

Potential future status after independent review: `T` as a pure Hardy-space
identity. It does not move RH.

### B. Source Sonin orientation

Connes--Consani's Sonin space is exactly the kernel of the lower diagonal Hardy
block. Under the exact coordinate

```text
s=1/2+i z,
```

their left-critical-half-plane construction becomes the same abstract kernel
category on `H2(C_+)`.

Potential future status: `T` as a source/coordinate dictionary lemma.

### C. Finite-to-global transport lemma

If

```text
U D=N u,
D H_minus subset H_minus,
N H_plus  subset H_plus,
```

then multiplication by `D` maps `S(u)` to `S(U)`. This is elementary and exact.

Potential future status: `T` as a general Hardy lemma; no zeta content by
itself.

## The genuinely open construction

The scientifically valuable target is not another reformulation. It is to find
an independently justified Wiener--Hopf factorization

```text
Theta_xi D_F=N_F u_F_tilde
```

from one finite semilocal Connes stage into the global xi boundary phase, with
the correct Hardy-preservation directions and a nonzero transported vector.

A positive result would prove

```text
V(0)!={0}
```

unconditionally, settling the open problem explicitly stated by Suzuki. This
would still be strictly weaker than RH.

## No-go results to carry

1. `POINTWISE-EULER-IMPEDANCE-LIMIT [F]`: raw finite local logarithmic
   derivatives diverge in the real half-strip `1/2<sigma<1`; analytic
   continuation/renormalization cannot be replaced by a pointwise Euler limit.
2. `DIRECT-DEBRANGES-EQUALITY [F]`: Suzuki explicitly states that the relevant
   Connes--Consani--Moscovici de Branges spaces are not isomorphic to his
   `H(E_xi)` and have different spectral properties. This kills only direct
   equality, not an intertwiner.
3. `SUZUKI-ZERO-VECTOR-SHORTCUT [F]`: the RH-dependent special zero vectors
   cannot be imported as unconditional vectors of `V(0)`.
4. `DIRECT-BM-ON-THETA [STOP/F for the shortcut]`: the Makarov--Poltoratski
   theorem located in this incubation assumes meromorphic inner input functions.
   Applying it directly to `Theta_xi` would import the very inner property whose
   global version is RH. A prior independent quotient/inner factorization is
   required.

## What does not promote

No result about RH, GRH, Weil positivity, LAMBDA-COCYCLE, J-native carriers,
Born/decoder physics, `zeta_8`, or the polylog/Lerch surface.

The identity `V(0) ~= S(Theta)` should not be described as solving Suzuki's
open problem. The open problem is **nontriviality** of that kernel.

## Preferred next attack

Freeze a precise Toeplitz-kernel/Wiener--Hopf criterion applicable to a general
meromorphic unimodular symbol of bounded type, then prove its hypotheses for
`conjugate(Theta_xi)` without assuming Hermite--Biehler/innerness. If this
cannot be done, return to G5 and seek an explicit finite-semiloal transport
factor.

No repository action follows automatically. Any public theorem promotion needs
a separate public claim lock and review.
