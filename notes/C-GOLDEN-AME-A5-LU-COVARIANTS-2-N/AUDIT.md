# Independent audit

This package was computed after the public pin
`1a813b6f50435d83e0dfd5011898a03fc5e4b089`, tree
`1a61fc296079a9a2964ba4649900851f7b25ec9a`, preregistration SHA-256
`b03ed300806c993cb4f4eac7249d9a6c2e7e9df9d96669d989445d4a1ade68f3`.

## Integrity

- source bytes: 8515
- source SHA-256:
  `55fbc0ba2747b4e5adc5a5abd15ac7241a461ff8182268ebdae464d8a29cc9ae`
- support: 112 entries, `40a+40b+32c`
- finite-field residues: `z=6,zbar=7,w=36,a=4,b=28,c=12`
- nonzero denominator residues: `2=2`, `w+w^-1=3` modulo 41

The prior public exact verifier replays `U`, its reshuffle and its partial
transpose with zero residuals and proves the entry field
`Q(zeta_40)`.  The n=4 runner independently reparses the pinned source.

## Graph completeness

`classify_n4_graphs.py` enumerates all `24^3=13824` normalized labeled
triples and all 2345 residual `S3` orbits.  Its explicit rewrite checks every
one of the 13800 labeled double-edge cases.  Only 24 labeled triples survive,
forming four free orbits.  This matches Burnside's independent closed form.

## Modular independence checks

The runner contracts all 16 primary matrices and all 16 stars.  Star
contractions swap `A` and `bar(A)` and transpose the output; no stored primary
matrix is substituted.  Every exact equality predicted by the graph
involution passes.

The first hard witness is selected only after the complete matrix census is
stored.  Frozen priority yields `q=0,R1`, then closure of `I,R1` adds `R1^2`.
The first nonzero three-column minor is at flattened positions `0,7,21` and
equals 31 modulo 41.

## Exact independence checks

`exact_witness.py` imports only the public exact field implementation in
`verify_source_field.py`.  It parses the source anew and does not import the
modular contraction engine.

It computes the exact `q=0,R1` matrix by two sparse binary contraction trees:

1. the cycle beginning `A0-B1`, `A1-B2`, `A2-B3`;
2. the different cycle beginning `A0-B3`, `A3-B2`, `A2-B1`.

The two complete matrices agree.  A third pass swaps `A` and `bar(A)`, then
transposes; this exact star equals the primary matrix.

The exact minor has 16 power-basis coefficients

```text
(1/256,0,3/256,0,0,0,-3/512,0,-1/512,0,3/512,0,1/512,0,-3/512,0)
```

and reduces to 31.  Exact diagonal grouping gives three distinct values with
index sets `{0,5}`, `{1,2}`, `{3,4}` and hence multiplicities `2+2+2`.

## Determinism

Two complete portable reruns must produce byte-identical
`MODULAR_RESULT.json`, `MODULAR_STDOUT.txt`, `EXACT_WITNESS.json`, and
`EXACT_STDOUT.txt`.  Their frozen hashes are recorded in `SHA256SUMS.txt`.
