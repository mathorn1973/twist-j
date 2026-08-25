# Blind breaker audit for C-J-SINGER-MAHLER-LIFT-1-N

```text
STATUS:     NON-CANONICAL audit record
AUTHORITY:  NONE
SCOPE:      FROZEN A0-A3 CHARACTERISTIC-POLYNOMIAL DECISIONS
PIN:        49ce4081e021171bc4c8c79a3fc7ffe4a496ea1a
```

The breaker lane read only the frozen preregistration.  Before producing its
decisions it did not read the builder, theorem, or root cross-check lanes.
Each executable version was hashed before its first run.

## Version history

| Version | SHA-256 | Bytes | First-run outcome |
|---|---|---:|---|
| v1 | `851e14f86da2c59b5e1d31c29aa5be2bdf0442f47a0bfbcf8e3e4a4c01ac7b8e` | 17192 | fail-fast control caught two misplaced exterior-resolvent coefficients before a decision |
| v2 | `93b0c33d9bb9f102043e690dcce1325615b4e8bc54820ce047ca0af4b6e43c11` | 17192 | exact control and A0 decision passed; a `RECON_ONLY` name collision stopped reporting with exit 1 |
| v3 | `2fc9c5ef4dea72cf0d95bbb409d5b0edfc57c0a3a2b5245b95497e70aeef1e04` | 17346 | exit 0; all four frozen tiers decided; post-run hash unchanged |

The v1 error used the coefficients belonging to the cubic resolvent in the
sextic pair-product polynomial.  The correction changed only those two
derived coefficients.  The v3 patch changed only the reconnaissance product
function and removed early negative return so that every frozen tier was
reported.  Mathematical tests and candidate ordering were unchanged.

## v3 exact decisions

| Tier | Decision | Independent certificate |
|---|---|---|
| A0 | `NEGATIVE_F_TIE` | `(-2,4,-3)`, `p_L`, two outside, exact factor `Y^2-3Y+1` |
| A1 | `NEGATIVE_F_LOWER` | `(-1,2,-2)`, `p_R`, two outside, exact rational isolator gives `M<2<tau` |
| A2 | `POSITIVE_COMPLETE_WINDOW` | all 165 rows; only `f_J` has `M<=tau`, at equality |
| A3 | `POSITIVE_COMPLETE_WINDOW` | all 11 rows; only `f_J` has `M<=tau`, at equality |

Rows checked were 3300, 1650, 165, and 11 respectively.  Both primitive
quartics were independently checked for irreducibility and root order 15.
The target controls checked `Phi_5(X-1)`, parity, trace, `f_J(1)`, the exact
2-out/2-in split, and the equality factor.

The breaker's optional NumPy output is labelled `RECON_ONLY` and is not used
by any exact decision.
