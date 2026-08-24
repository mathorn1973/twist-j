# PREREG C-RH-GLOBAL-SONIN-WIENER-HOPF-1-N

```text
STATUS:       NON-CANONICAL INCUBATION PREREGISTRATION
ISSUE:        #360
AUTHORITY:    none
PUBLIC BASIS: Public Canon v46, mathorn1973/twist-j main
LAYER:        analytic/operator-theoretic only
RH INPUT:     forbidden
ZERO DATA:    forbidden for positive gates
```

## 1. Purpose

This object is an independent carrier-comparison / no-go successor to corrected
issue #357. It is not G6 of #357 and consumes no capacity-positivity result.

The narrow target is the unconditional space

```text
V(0)=L2(0,infinity) intersect K L2(0,infinity)
```

introduced by Suzuki, and its relation to Connes--Consani Sonin kernels and
ordinary Toeplitz kernels. A positive result at the strongest frozen gate would
construct a nonzero vector in `V(0)`. Suzuki explicitly states that proving or
disproving `V(0)!={0}` unconditionally is an open problem. This is strictly
weaker than RH.

## 2. Exposed preparation

The owner/session has already seen proposed identities and no-go conclusions on
the later history of #357. They are excluded as evidence. This object re-derives
all load-bearing statements from the primary sources and elementary Hardy
algebra after this preregistration.

## 3. Primary sources

1. Masatoshi Suzuki, `On the Hilbert space derived from the Weil distribution`,
   Canadian Journal of Mathematics, published online 2025-11-03, especially
   equations (5.1), (5.2), Lemma 5.1, Remark 5.2 and Section 5.1.
2. Alain Connes and Caterina Consani, `Quasi-inner functions and local factors`,
   Journal of Number Theory 226 (2021), especially the Hardy block convention,
   the definition `S(u)=ker u_22`, and the finite-place induction theorem.

No secondary paraphrase carries a theorem.

## 4. Frozen Hardy orientation

Use Suzuki's Fourier convention

```text
H_plus  = F L2(0,infinity) = H2(C_+),
H_minus = H_plus^perp,
P       = projection onto H_plus,
Q       = 1-P.
```

The antiunitary sharp map sends `H_plus` to `H_minus`.

Suzuki objects:

```text
Theta=Theta_xi=E_xi^sharp/E_xi,
K=F^(-1) M_Theta J F,
(JF)=F^sharp,
V(0)=L2(0,infinity) intersect K L2(0,infinity).
```

For a unimodular boundary symbol `u` on the same oriented boundary define

```text
S(u)=ker(Q M_u Q |_(H_minus)).
```

The Connes semilocal symbols live naturally on the boundary of the **left**
critical half-plane. Any use in the Suzuki upper-half-plane variable must state
the exact affine rotation/reflection before applying a Hardy-preservation
claim.

## 5. Frozen gates

### G1 GLOBAL-SONIN-IDENTIFICATION
Derive from Suzuki's definitions, without RH,

```text
V(0) ~=_antiunitary S(Theta).
```

Then derive the standard Toeplitz form. PASS only with all sharp operations and
Hardy halves explicit.

### G2 SOURCE-SONIN-ORIENTATION
Read Connes--Consani's block convention and verify that their Sonin construction
is the same abstract kernel `ker u_22`. Record the required coordinate map
between their left-half-plane symbol and the frozen upper-half-plane boundary.

### G3 LOGICAL SCOPE
Audit Suzuki's statement about `V(0)!={0}`. PASS only if the note clearly
separates:

```text
RH -> V(0)!={0},
V(0)!={0}  does not by itself imply RH,
```

and does not import RH-dependent model-space orthogonality.

### G4 TRANSPORT LEMMA
Prove or refute: if boundary multipliers satisfy

```text
U D=N u,
D H_minus subset H_minus,
N H_plus subset H_plus,
```

on typed multiplier domains, then multiplication by `D` maps `S(u)` to `S(U)`.

### G5 GLOBAL-SONIN-WIENER-HOPF
Find, for one finite semilocal stage after exact coordinate conversion,
non-tautological `D_F,N_F` such that

```text
Theta D_F=N_F u_F,
D_F H_minus subset H_minus,
N_F H_plus subset H_plus,
```

and prove `D_F` is nonzero on at least one nonzero vector of `S(u_F)`.

No quotient defined merely as `Theta/u_F` earns this gate.

### G6 TOEPLITZ-KERNEL
Independently attack `ker T_(conjugate Theta)` using a frozen exact
Wiener--Hopf / inner--outer / Toeplitz-kernel criterion. Any phase-density or
Beurling--Malliavin theorem must be pinned with all hypotheses before use.

### G7 NO-GO CONTROLS
Try to kill before positive construction:

```text
raw finite Euler impedance convergence for 1/2<Re s<1,
direct semilocal-space = Suzuki-space identification,
one known critical zero -> V(0)!={0},
orientation-free use of the Connes induction map,
tautological Wiener--Hopf factorization.
```

## 6. Decision labels

Only

```text
candidate-T
candidate-D
candidate-C
F
STOP
```

are allowed. No RH support label is earned by a reformulation or by nontrivial
`V(0)`.

## 7. Hard firewall

No RH/GRH proof or evidence, no Weil-positivity promotion, no public status
movement, no LAMBDA-COCYCLE grid input, no J-native/Born/decoder/physical/SI
claim, and no privileged `zeta_8` role. The separate polylog/Lerch recon is not
consumed.
