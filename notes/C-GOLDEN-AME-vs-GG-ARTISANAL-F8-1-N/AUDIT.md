# Post-lock audit record

## Verdict and witness

Both scoped comparisons are exact negatives:

| comparison | verdict | first frozen mismatch |
|---|---|---|
| golden vs sym | `EXACT_NO_SYM` | `v0`: 209 vs 171 mod 241 |
| golden vs sparse | `EXACT_NO_SPARSE` | `v0`: 209 vs 171 mod 241 |

Thus the union verdict is `EXACT_NO_GG_ARTISANAL_9PLUS27`.  This excludes
arbitrary local `U(6)^4`, global phase, and all 24 party permutations for the
two frozen Gross--Goedicke orbits.  It does not classify every AME(4,6).

In the frozen basis `1,xi,...,xi^31`, `xi=zeta_120`, the exact difference for
both comparisons is

```text
(-57/4) + 3*xi^6 + (3/2)*xi^8 + (3/2)*xi^12
         - 3*xi^18 - (3/2)*xi^28 + (3/2)*xi^30.
```

Its reduction at `xi -> 3` in `F_241` is 38, proving it is nonzero.

## Gate record

- G0 source byte/SHA/Git-blob pins: PASS.
- G1 direct construction, all three exact unitarities, 48 -> 24+24 disjoint
  GL census, all 48 standard/twisted autocorrelations, exact Pi9/Pi27 ranks
  and commutators: PASS.
- G2 diagram census and party action (D0 fixed, D1--D3 full S3): PASS.
- G3 all 12 modular values in both primary and alternate factor orders: PASS.
- G4 exact power-basis witness and modular replay: PASS.
- G5 all 12 exact contractions in both factor orders: PASS.

The modular fingerprints are:

| target | `(v0,v1,v2,v3)` | `(v0,e1,e2,e3)` |
|---|---|---|
| golden | `(209,17,88,148)` | `(209,12,166,170)` |
| sym | `(171,108,108,108)` | `(171,83,47,5)` |
| sparse | `(171,108,108,108)` | `(171,83,47,5)` |

## Independence and determinism

The primary evaluator uses two frozen binary-join orders.  A separately
written compatible-tuple evaluator uses the third order
`A3,B1,A0,B3,A2,B0,A1,B2`; it independently reproduced all twelve modular
values, exact `v0=171` for both artisanal tensors, and the same 32-coordinate
golden-minus-target vector.  Its canonical result SHA-256 is
`dee5046136cab25ed9b54d252259d6835b778ca08c4f445cf6c2f7f13a158516`.

The independently written G0/G1 certificate SHA-256 is
`67c9493c92129eba274345e5042d6c38738cc53e08172ff95e6d879865384834`.
Two complete primary runs produced identical hashes for all six generated
outputs; see `TWO_RUN_DETERMINISM.json`.
