# RESULT C-ENTANGLEMENT-RELATIONAL-WEDGE-1-N

Status: **NON-CANONICAL incubation result**. One local symbolic lane only. No public T/C/D/H/O/F status is earned. No Canon, Registry, Frontier, evidence, gate, decoder, apparatus, sampling, or release change.

Authority basis at freeze: Public Canon v51, issue #419, PREREG commit `6a21d2655942abcef920c4fef99fe01c72a92ec6`.

## Verdict

```text
RELATIONAL-AREA-PURE
```

The exact pure-state relational geometry survives every frozen positive gate, while the preregistered breakers show that the one-scalar rectangle reading is not universal beyond the pure rank-two setting.

## G1. Relational norm

For

```text
x = a e0 f0 + b e0 f1 + c e1 f0 + d e1 f1,
A = [[a,b],[c,d]],
Delta = ad-bc,
r(x) = P_-- R(x tensor x) = (Delta/2) kappa,
```

with the v51 wedge convention and orthonormal local bases,

```text
||kappa||^2 = 4,
||r(x)||^2 = |Delta|^2.
```

This is the exact norm of the already-public determinant line. The oriented phase of `Delta` is not a full local-unitary invariant.

## G2. Reduced state

For `rho_A = A A^dagger`,

```text
det(rho_A) = |Delta|^2 = ||r||^2.
```

For a normalized state `Tr(rho_A)=1`, the two-dimensional identity gives

```text
Tr(rho_A^2) = 1 - 2||r||^2,
lambda_+- = (1 +- sqrt(1-4||r||^2))/2.
```

## G3. Complete pure 2 x 2 local-unitary coordinate

The Schmidt spectrum of a normalized pure two-qubit state is the unordered pair of roots of

```text
t^2 - t + ||r||^2 = 0.
```

Therefore two normalized pure two-qubit states are locally-unitarily equivalent iff they have the same `||r||`. At this scope the whole local-unitary entanglement orbit space is one interval:

```text
0 <= ||r|| <= 1/2.
```

This is a pure-state rank-two classification only.

## G4. Concurrence, external standard-QM identification

For pure two-qubit states the spin-flip overlap gives

```text
C^2 = 4 |Delta|^2,
C = 2 |Delta| = 2 ||r||.
```

This is the standard pure-state concurrence identification. It is not a TWIST-J derivation of quantum mechanics.

## G5. CHSH optimum, external standard-QM comparison

In Schmidt gauge

```text
x = s0 |00> + s1 |11>,
s0^2+s1^2=1,
C=2 s0 s1,
```

the Pauli correlation matrix is

```text
T = diag(C,-C,1).
```

The standard Horodecki two-qubit CHSH criterion therefore gives

```text
B_max = 2 sqrt(1+C^2)
      = 2 sqrt(1+4||r||^2),
B_max^2 - 4 = 16 ||r||^2.
```

Endpoints:

```text
product state: ||r||=0   -> B_max=2,
Bell state:    ||r||=1/2 -> B_max=2 sqrt(2).
```

This is an operational comparison inside standard quantum mechanics. TWIST-J has not derived the measurement settings, Born event law, sampling, locality account, or Tsirelson bound from its integer substrate.

## G6. Schmidt rectangle

In Schmidt gauge,

```text
||r|| = s0 s1.
```

Thus the user's rectangle is exact after local-unitary gauge fixing: its side lengths are the Schmidt amplitudes and its area is the relational invariant. Product states collapse the area to zero; maximally entangled states give the square `s0=s1=1/sqrt(2)` with area `1/2`.

The basis-free object is the wedge/bivector, not a privileged drawn rectangle.

## G7. Pure 2 x n generalization

For coefficient-row vectors `u,v in C^n`, exact Cauchy-Binet gives

```text
||u wedge v||^2
 = det(rho_A)
 = sum_(i<j) |A_0i A_1j - A_0j A_1i|^2.
```

Product iff `u wedge v=0`. For `n=2`, `Lambda^2 C^2` is one-dimensional and the entire bivector reduces to the determinant line. For `n>2`, the relation is a multi-component Pluecker bivector.

## Breakers

### B1. Mixed states

Exact Werner control at `p=1/2`:

```text
rho_W = p |psi-><psi-| + (1-p) I/4.
```

Its partial transpose has eigenvalues

```text
{3/8,3/8,3/8,-1/8},
```

so it is entangled, while the Horodecki CHSH quantity is

```text
M = 2 p^2 = 1/2 < 1,
```

so no CHSH violation occurs. Therefore

```text
entangled  <=>  one rectangle area  <=>  CHSH violation
```

is false for mixed states.

### B2. Higher Schmidt rank

The normalized Schmidt spectra

```text
(1/2,1/2,0)
(2/3,1/6,1/6)
```

have the same second elementary symmetric scalar

```text
e2 = 1/4,
```

but different spectra and Schmidt ranks. One scalar exterior-area measure cannot classify general rank-three bipartite pure entanglement.

### B3. Local basis phase

A local `U(2)` phase changes `Delta` by `det(U)det(V)` while preserving `|Delta|`. Hence the physically basis-independent scalar at the full local-unitary level is the norm, not the oriented phase. The oriented determinant survives only after restricting the gauge, for example to `SU(2) x SU(2)`.

### B4. No new degree of freedom

`r(x)` is a derived invariant of the joint state. The result does not add a third particle, force, field, signal, or channel. Its reality is relational: it is invariant information that exists only for the composite state and is operationally accessible in standard quantum mechanics.

### B5. TWIST-J lift remains open

The public theorem `QPAIR-SYM2-TENSOR-DEFECT [T]` supplies the exact L1 determinant line. This incubation does not supply a public bridge from that line to `MatterData`, a completed Born pairing, realized apparatus, L5 event stream, L6 measure, or CHSH experiment. `QUADRATIC-DECODER-DATA [O]` and the apparatus/sampling blockers remain unchanged.

## Scientific reading

At the frozen pure two-qubit scope, the precise statement is:

```text
entanglement is not an added bond between two objects;
its complete local-unitary magnitude is the area of the joint rank-two relation.
```

The geometric language is exact only after the scope is stated. The invariant is the norm of a wedge. The rectangle is its Schmidt-gauge representative.

## Post-result observation, NOT part of the frozen result

Writing the reduced qubit state as `rho_A=(I+b.sigma)/2` immediately suggests

```text
|b|^2 + 4||r||^2 = 1,
```

or equivalently `|b|^2 + C^2 = 1`. This was noticed after the frozen run and is not promoted or absorbed here. If pursued, it requires a fresh successor identifier and preregistration. It is potentially the exact triangle counterpart of the rectangle result.
