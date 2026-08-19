# P-PURE-QUBIT-RELATIONAL-GEOMETRY-2 result

Status: `SCIENTIFIC RESULT / TWO-ARCHITECTURE PASS / CANON UNCHANGED`

## Verdict

The fresh immutable public pin read back exactly and the single authorized
formal run passed all 17 exact gates with exit code zero, empty stderr, and
stdout byte-identical to `EXPECTED.txt`. The self-contained proofs in
`PREREG.md` carry the universal statements; the verifier audits their exact
coordinate formulas and all three frozen scope breakers.

No public Canon row changes in this probe-only pull request. The maximum
post-workflow dispositions remain:

```text
PURE-QUBIT-RELATIONAL-AREA               T candidate
PURE-QUBIT-LOCAL-RELATION-PYTHAGORAS     T candidate
PURE-QUBIT-RELATIONAL-CHSH               T candidate
PURE-QUBIT-RELATIONAL-READING            D candidate
```

## Exact result

For a normalized pure vector in an externally supplied orthonormal
`C^2 tensor C^2` factorization, with coefficient matrix `A`, reduced state
`rho_A=A A^dagger`, determinant-line component
`r=(det(A)/2)kappa`, and `||kappa||^2=4`,

```text
||r||^2 = |det A|^2 = det rho_A,
C = 2 ||r||,
|b_vec|^2 + C^2 = 1,
Tr(rho_A^2) = 1 - C^2/2.
```

The exact unhalved-wedge extension is

```text
det(A A^dagger)
  = sum_(i<j) |u_i v_j-u_j v_i|^2
  = (1/2)||u wedge v||_tensor^2.
```

The self-contained two-setting qubit optimization, with the Horodecki result
retained as attribution and standard-QM comparison, gives

```text
B_max = 2 sqrt(1+C^2) = 2 sqrt(1+4||r||^2),
B_max^2 - 4 = 16 ||r||^2.
```

The determinant-line norm is zero exactly on product states, reaches `1/2`
exactly on maximally entangled pure two-qubit states, and determines the pure
two-qubit local-unitary orbit. The determinant phase does not.

## Falsifiers and boundaries

No scientific falsifier fired. Every correction required by the closed
predecessor passed in this fresh attack:

1. The `2 x n` audit uses the exact factor two for the declared unhalved
   ambient tensor wedge.
2. The local-`U(2)` phase witness is exactly normalized and changes phase
   while preserving determinant norm.
3. The Werner state at `p=1/2` violates both pure-state identities while
   remaining entangled and CHSH-subcritical.
4. Distinct rank-two and rank-three Schmidt spectra share `e2=1/4`, so one
   exterior scalar does not classify higher-rank spectra.

The `2 x n` identity is algebraic; concurrence and CHSH remain two-qubit
statements. No map was made from the integral QPAIR or rational piston carrier
to physical qubits. No decoder, apparatus, event, probability measure,
causal, locality, no-signalling or communication claim was tested or earned.
`BELL-MAGIC-BOUNDARY`, `QUADRATIC-DECODER-DATA` and
`QDD-INSTRUMENT-APPARATUS` remain unchanged.

## Reading at the frozen ceiling

Once a standard-QM normalized pure-two-qubit structure is supplied externally,
`||r||` may be read as relational area and as `C/2`. It is a derived invariant
of one joint state, not a third particle, force, signal or transported
substance. This conditional comparison says nothing yet about what physical
quanta are in TWIST-J or how a laboratory Bell experiment is generated.

Required workflow run `32226965301` reproduced the exact verifier and
`EXPECTED.txt` on aarch64 job `95988501590` and x86_64 job `95988501973`;
aggregate job `95988607069` passed. The two-architecture gate is PASS.

All four dispositions remain non-canonical until a separate sealed Canon fold
reviews them. The probe changes no current Canon row.
