# PREREG C-ENTANGLEMENT-RELATIONAL-WEDGE-1-N

Status: NON-CANONICAL incubation. No public claim. No Canon, Registry, Frontier, gate, evidence, or release change.

Authority at freeze: Public Canon v51, `mathorn1973/twist-j main`, activation `cef0a08cec219a41333b36fbfe0a0e4dc780045f`, content commit `bf25cde49bca33a5bb93ecdf50b641f0042b5211`, Canon SHA-256 `eb0f6aacb04c405f36ae1e8ece4c6c58c416884fa15fe017c2ee64bb240abec4`, 257459 bytes.

Owner lock: issue #419.

## Existing public theorem boundary

`QPAIR-SYM2-TENSOR-DEFECT [T]` already proves the exact L1 decomposition and determinant line. This incubation does not recount it. It asks only whether the norm of that line is a complete pure-state local-unitary entanglement coordinate and how it connects, under standard external quantum mechanics, to the CHSH optimum.

`BELL-MAGIC-BOUNDARY [T]` is a separate finite equatorial functional and is not consumed as an unrestricted CHSH theorem. `QUADRATIC-DECODER-DATA [O]` stays open and STOP. No `BELL-CAUSAL-ACCOUNTING` row exists or is created here.

## Frozen carrier and conventions

Use normalized `x in C^2 tensor C^2` in orthonormal local bases:

```text
x = a e0 f0 + b e0 f1 + c e1 f0 + d e1 f1,
A = [[a,b],[c,d]],
Delta = ad-bc.
```

Use the public v51 reorder and antisymmetric projector:

```text
r(x) = P_-- R(x tensor x)
     = (Delta/2) kappa,
kappa = (e0 wedge e1) tensor (f0 wedge f1),
u wedge v = u tensor v - v tensor u.
```

With orthonormal local bases, `||e0 wedge e1||^2=2`, `||f0 wedge f1||^2=2`, hence `||kappa||^2=4`.

## Frozen gates

G1 RELATIONAL NORM

```text
||r||^2 = |Delta|^2.
```

G2 REDUCED STATE

For `rho_A=A A^dagger`, normalized by `Tr rho_A=1`:

```text
det rho_A = |Delta|^2 = ||r||^2,
Tr(rho_A^2) = 1 - 2||r||^2,
lambda_+- = (1 +- sqrt(1-4||r||^2))/2.
```

G3 PURE 2x2 LOCAL-UNITARY CLASSIFICATION

Two normalized pure two-qubit states are locally-unitarily equivalent iff they have the same `||r||`. This is the Schmidt classification specialized to two coefficients. It says nothing about mixed states or higher Schmidt rank.

G4 PURE-STATE CONCURRENCE

Under the standard external two-qubit pure-state definition:

```text
C = 2|Delta| = 2||r||.
```

G5 CHSH OPTIMUM, EXTERNAL QM COMPARISON

Using the standard Horodecki two-qubit CHSH criterion:

```text
B_max = 2 sqrt(1+C^2)
      = 2 sqrt(1+4||r||^2),
B_max^2 - 4 = 16||r||^2.
```

This is not a TWIST-J derivation of measurements, Born sampling, locality, Tsirelson, or a decoder.

G6 SCHMIDT RECTANGLE

For Schmidt form `x=s0|00>+s1|11>`, `s0,s1>=0`, `s0^2+s1^2=1`:

```text
||r|| = s0 s1.
```

The rectangle is a gauge-fixed representative. The basis-free object is the wedge/bivector.

G7 PURE 2xn GENERALIZATION

For row vectors `u,v in C^n` of a normalized `2 x n` coefficient matrix:

```text
||u wedge v||^2
 = det rho_A
 = sum_(i<j) |A_0i A_1j - A_0j A_1i|^2.
```

Product iff `u wedge v=0`. For `n=2`, the bivector space is one-dimensional and reduces to `Delta`.

## Frozen breakers

B1 MIXED STATE. The pure-state rectangle must not be universalized. Use the two-qubit Werner family as exact control. The intended control facts are checked independently after this freeze: separability/entanglement and CHSH violation have different thresholds.

B2 HIGHER SCHMIDT RANK. Exhibit normalized pure states in at least `3 x 3` with equal one scalar candidate area but different Schmidt spectra, proving one scalar cannot classify general bipartite pure entanglement.

B3 LOCAL BASIS PHASE. Under local `U,V in U(2)`, `Delta -> det(U)det(V)Delta`; only `|Delta|` is invariant under the full local-unitary group. Under `SU(2) x SU(2)` the oriented determinant is invariant.

B4 NO NEW DEGREE OF FREEDOM. `r(x)` is derived from the joint state. It may be an observable invariant without becoming an independent particle, field, signal, or dynamical channel.

B5 TWIST-J LIFT. No internal decoder map from the L1 determinant line to a realized CHSH apparatus is assumed. The open QDD/apparatus/sampling boundaries remain binding.

## External theorem sources

Primary comparison sources only:

1. R. Horodecki, P. Horodecki, M. Horodecki, Physics Letters A 200 (1995) 340-344, DOI 10.1016/0375-9601(95)00214-N.
2. W. K. Wootters, Phys. Rev. Lett. 80 (1998) 2245-2248, arXiv:quant-ph/9709029.

They are external standard quantum mechanics, not TWIST-J evidence or status promotion.

## Output vocabulary

```text
RELATIONAL-AREA-PURE
PARTIAL
F
STOP
```

`RELATIONAL-AREA-PURE` requires G1-G7 and all scope breakers to hold. Any stronger mixed-state, universal Bell, decoder, or physical-substrate reading is forbidden.

## Execution discipline

This PREREG is frozen before any dedicated exact verifier or breaker execution under this identifier. Exposed conversational derivations are disclosed in issue #419 and are not evidence. A breaker is written from this file before the positive verifier is compared with it. Any future public theorem requires a fresh public probe claim.