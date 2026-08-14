# BREAKER C-RH-HADAMARD-HORIZONTAL-SOURCE-1-N

```text
STATUS:      NON-CANONICAL independent breaker design
ISSUE LOCK:  #373
READ ORDER:  frozen before any verify.py
```

The breaker is deliberately written without consuming any future verifier implementation.

## B1 factor-two attack

Use `rho=beta+i gamma`, `rho*=1-conjugate(rho)`, `delta=beta-1/2` and direct 2-vector algebra only. Check

```text
H2 (exp(delta u), exp(-delta u))^T
```

and recompute the antisymmetric squared norm from scratch. Reject any formula confusing `cosh(delta u)-1`, `cosh(2 delta u)-1`, or a factor two.

## B2 Cayley-energy route A

Expand

```text
E_C(rho)=(1/2)|1/rho-1/rho*|^2
```

directly into `beta,gamma`. Verify positivity and the exact zero set before summing.

## B3 Cayley-energy route B

Independently sum the expanded square over every upper-half-plane zero with multiplicity, using the involution `rho -> rho*`, and compare with

```text
S2 = sum 1/|rho|^2,
lambda_1 = 2 sum_(gamma>0) Re(1/rho).
```

No pair representative may be selected. If the resulting identity differs from the preregistered factor convention, the result must record the correction explicitly.

## B4 convergence

Prove absolute convergence by dyadic zero counting. Any rearrangement that needs more than `N(T)=O(T log T)` and `0<beta<1` must be named. Reject a merely conditionally convergent manipulation presented as absolute.

## B5 source-side independence

Read the primary unconditional Montgomery/Tsang construction separately from the Cayley algebra. Verify that the prime-side expression exists before making any identification with `E_C`.

## B6 isolation attack

Even if a complete positive pair sum contains the symmetric diagonal, try to construct two admissible pair configurations with the same total quadratic statistic but different target symmetric-diagonal mass. If this freedom survives the frozen constraints, exact isolation has not been proved.

## B7 circularity

Reject any test kernel whose coefficient was chosen using `beta`, `gamma`, `rho*`, `E_C`, or the target pair after opening the zero-side decomposition unless an independent prime-side definition produces the same kernel.

## B8 #363 boundary

Reject any claimed advance that collapses to finitely many one-variable trigonometric moments with strict Toeplitz positivity. Such a route is already neutralized at its frozen scope by #363.

## Breaker verdict vocabulary

```text
PASS       no exact counterexample to a frozen algebra/source lemma
F          exact counterexample or proof of non-isolation at the frozen route
STOP       missing source hypothesis, incomplete convergence, or untyped limit
```
