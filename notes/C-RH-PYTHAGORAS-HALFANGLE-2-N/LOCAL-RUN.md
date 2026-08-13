# LOCAL RUN

```text
STATUS: NON-FORMAL INCUBATION CHECK
EVIDENCE: none for public status
```

After the corrected preregistration pin and after `break.py` was frozen, the finite exact algebraic checks were executed locally using Python `Fraction` arithmetic.

Observed exact decisions:

```text
breaker:
  delayed-leg determinant / L^2 = -1/4
  rational phase (3+4i)/5 reconstructs both quadratures
  balanced conjugate boundary gives real(omega^2)=0, |imag(omega^2)|=1

verifier:
  G1 prime critical-weight square factor: PASS
  G2 pole-term perfect square: PASS
  G4 positive Gamma/Lerch L2 coefficient: PASS
  G5 balanced half-angle algebra: PASS
```

No floating-point value decides any result. No two-architecture gate is claimed or required for this non-canonical incubation. Infinite-series convergence, strict concavity of `R_inf`, and the signed Pythagorean identity are theorem arguments in `RESULT.md`, not finite-computation claims.
