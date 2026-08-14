# PREREG C-RH-HADAMARD-HORIZONTAL-SOURCE-1-N

```text
STATUS:        NON-CANONICAL INCUBATION
ISSUE LOCK:    #373
PUBLIC BASIS:  Public Canon v46
LAYER:         analytic/number-theoretic only
AUTHORITY:     none
```

## Question

Can the radial Hadamard defect exposed in #371 be obtained from a genuine prime-side two-zero quadratic source, rather than only from individual zero coordinates?

## Frozen definitions

For a nontrivial zero in the upper half plane,

```text
rho      = beta + i gamma,
rho*     = 1 - conjugate(rho),
delta    = beta - 1/2,
xi(rho)  = 1 - 1/rho,
E_C(rho) = (1/2) |1/rho - 1/rho*|^2.
```

The horizontal amplitude at real `u` is

```text
v_u(rho) = (exp(delta u), exp(-delta u)).
```

The normalized H2 antisymmetric energy is

```text
E_H(rho;u) = (exp(delta u)-exp(-delta u))^2/2
           = cosh(2 delta u)-1.
```

Use the corrected unconditional pair-correlation object and Tsang-kernel conventions from arXiv:2501.14545v2. No earlier uncorrected error term is load-bearing.

## Gates

### G1
Source-audit the unconditional `Fcal(x,T)` L2 representation and its von-Mangoldt Dirichlet-polynomial source side, without RH.

### G2
Prove exactly that the functional symmetric diagonal is `1 + E_H` at `u=alpha log T`.

### G3
Freeze upper-half-plane summation with multiplicity over every zero, so an off-line functional pair occurs twice. Put

```text
S2 = sum_(gamma>0) 1/|rho|^2.
EC = (1/2) sum_(gamma>0) E_C(rho).
```

The factor `1/2` removes the double counting of each functional pair. Prove or refute

```text
EC = S2/2 - lambda_1/2
```

or the corrected factor convention forced by the exact algebra. Prove absolute convergence before rearrangement. Decide whether vanishing is exactly RH.

### G4
Starting from a named explicit formula for a prime-counting or short-interval field, seek a quadratic form whose functional-pair block contains exactly `E_C`, with no insertion of `E_C` by definition.

### G5
Determine whether the target block can be isolated or bounded from the complete pair sum without RH, a thin-box assumption, pair uniqueness, or Weil positivity.

### G6
Check that any proposed source uses genuine two-zero quadratic information and is outside the finite strict single-profile scope killed by #363.

### G7 breaker
Freeze a separate breaker before any verification code. It must independently audit pair counting, factors two, convergence, the H2/cosh identity, source-side typing, and hidden assumptions.

## Decisions

```text
SOURCE   exact prime-side quadratic access to an aggregate controlling E_C
PARTIAL  exact horizontal H2 source, but no exact Cayley E_C isolation
F        frozen source route is proved incapable of accessing E_C
STOP     any load-bearing source, convergence, typing, or independence gap remains
```

## Exposure

The source papers, the symmetric-diagonal cosh observation, and a candidate `S2-lambda_1` relation were seen before this pin. They are exposed preparation. They are not evidence and must be re-derived below.

No zero table, rounded Li coefficients, or numerical fitting is admissible as evidence.

## Firewall

No RH status movement. No Canon, Registry or frontier edit. No physical interpretation. No L1-L6 lift. No claim that Hadamard itself creates information.
