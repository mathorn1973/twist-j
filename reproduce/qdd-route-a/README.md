# QDD Route A dictionary reproduction

Exact reproduction of the owner-adopted QDD Route A dictionary on the finite
balanced piston carrier V_eff = ell(F_5)^4 over all 15625 checkpoints of F_5^6.
The direct cyclotomic write R_cyc o iota_B0 o beta_QDD (field arithmetic in
Q(zeta_5), sigma_4, Tr, the trace pairing, the LOW LINE Q lambda_B with
lambda_B = -zeta_5^4, the rank-one operator T_w) is compared field by field
with the factor route F_QDD o Q_QDD o beta_QDD (Gram G = I - (1/5) 1 1^T,
the frozen effect pair E_low = (1/4) 1 1^T and E_high = I - E_low of the
EFFECT_SHADOW_MINIMAL owner freeze).  Rational arithmetic only; no input,
randomness, files, environment or network.

Fifteen checks: low line, Gram, the theorem target on all 15625 checkpoints,
totality of the tagged record with the 25-head zero branch, exact
normalization, the 313 Q-fibres with sizes 25 and 50 and injectivity on
QCarrier_QDD, the input allowlist, two negative controls (rational-line
reading, omitted Gram), the projector-pair theorem along Tr_4, the closed
forms, the diagonal boundary A_dagger = A_T on V_eff, the cyclotomic pair
diagnostic, the value table of the normalized pair and the rational versus
mod-5 zero-sum counts.

Evidence for registry claims QDD-ALGEBRAIC-FACTORIZATION,
QDD-PROJECTOR-PAIR-TR4 and QDD-QCARRIER-DIAGONAL-BOUNDARY.
QUADRATIC-DECODER-DATA remains an open obligation: this bundle fills no
completion-contract field, claims no L6 reading, no apparatus, occurrence
law, sampling, post-state or SI content, and the value 1/6 in the table is a
numerical witness with no dependency.  The verifier confirms an already
derived identity of the adopted definitions; it is a conformance certificate,
not an independent readout.

Run from the repository root:

```
python3 reproduce/qdd-route-a/verify.py
```

Expected: byte identical to EXPECTED.txt, RESULT 15/15 ALL PASS, exit 0, no
stderr.  Public evidence requires the same commit to pass the public x86_64 and
aarch64 reproduction jobs; the RUNS records of those jobs are the architecture
gate.  Any CPython 3.10 or later interpreter with the standard library suffices.
