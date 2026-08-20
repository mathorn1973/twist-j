# PROMO-C-TRACEKERNEL-EXTERIOR-CLOSURE-1 breaker result

Status: NON-CANONICAL INDEPENDENT BREAKER RESULT. Route:
`CONDITIONAL-PASS / L1 ONLY / NO PROMOTION`.

## Exact decision

All exact breaker gates passed:

```text
G1 G2 G3 G5 S1       PASS for primes 2 through 23
G4 G6 G7 S5          PASS on all 125 states, 15625 pairs,
                     and 1953125 Jacobi triples
S2 empty p=2 case    PASS
S3 volume rescaling  PASS for c=1,2,3,4
S4 plane control     PASS
S6 exact non-Jacobi  PASS
S7 automorphisms     PASS: Aut=SO3=120
A2/A3 kinematics     PASS: GL2=480, compatible=8, incompatible=472
S8 scope firewall    PASS
```

The independent route therefore agrees with the frozen result-exposed
conclusions:

```text
[candidate-T]
  For every prime p, the trace Gram yields the carrier
  W_p = rad(G_p mod p), dim W_p = p - 2, and its nondegenerate
  first-derived residual form g_p.

[candidate-T, conditional on EXACT-HODGE-HOME-CLOSURE]
  The only nonzero home-carrier closure occurs at p = 5.

[candidate-T, conditional on EXACT-HODGE-HOME-CLOSURE]
  At p = 5 the Hodge bracket is sl_2(F_5) and respects the public
  Phi grading 1 + 2.

[O]
  The public architecture does not force EXACT-HODGE-HOME-CLOSURE.
```

No exact mismatch fired. The full faithful public
`(det g)^-1 direct-sum g` image is not a bracket-automorphism group:
only 8 of 480 elements preserve the Hodge bracket. This sharpens the live
boundary but does not by itself fire F2, because the public dependency that
would require full kinematical equivariance of the spatial commutator has not
been derived.

## Provenance boundary

- The scalar `rho(2 I_2)` witness and the characteristic-free non-Jacobi
  counterexample were supplied by external review and were independently
  verified here. They are not blind finds.
- The 8-of-480 count was already result-exposed and was independently
  recomputed here.
- The seeded control used seed `20260820` and returned 3052 invertible
  alternating maps, 21 satisfying Jacobi, out of 4000 trials. This is a new
  independent sample, not a reproduction of the earlier exposed 3013/20
  census and not a frozen equality target. The exact counterexample, not
  either sample count, decides the weakness of an unnamed isomorphism
  premise.

## Firewalls

No claim is made that the bridge premise is forced. No L1-to-L2 lift,
canonical curvature operator, physical reading, decoder, measure, metrology,
`2I` derivation, spinor carrier, integral lift, or extension of the public
`ALPHA-SEED` scope is included.

This result earns no public scientific status. It may be consumed only by a
separate formal public probe whose accepted `PREREG.md` and new
`verify.py` are committed and pushed before their first formal execution.
