# C-K8-LOCAL-FACTORIZATION-ATLAS-N

> **NON-CANONICAL INCUBATION — candidate-T / L1 ceiling.** This note is not a
> formal public probe, carries no evidence credit, and changes no Canon,
> Registry, Frontier, gate, or program status.

This package gives an elementary, complete rational-prime factorization atlas
for `Phi_8(x)=x^4+1` and the corresponding prime-decomposition data in
`K_8=Q(zeta_8)`. “Local” here does not mean that the polynomial factors over
every `Q_p`: it remains irreducible over `Q_2`.

## Outcome

```text
RESULT:          candidate-T / L1
VERIFIER:        PASS
BLIND BREAKER:   NO_FALSIFIER_FOUND
PRIME AUDIT:     every prime p <= 1,000,000
UNIVERSAL BASIS: written proof, not the finite scan
PIN COMMIT:      aea19ff5238c05bb47fd39a735a440525caf09a1
LOCK ISSUE:      #749
```

The candidate delta is the unified all-prime atlas, the three square-root
routes with the complete `V_4` fixed-field table, and an ordered `p=5`
residual-component audit. Existing registered rows are imported only at their
registered scopes; `I-BILOCATED` remains `[D]`.

## Files

- `PREREG.md` — frozen question, candidate statements, method, and falsifiers;
- `verify.py` — exact standard-library verifier;
- `break.py` — independently authored prereg-only breaker;
- `EXPECTED.txt`, `BREAKER_EXPECTED.txt` — exact successful stdout;
- `RUN.md` — immutable-pin and execution record;
- `RESULT.md` — proof, atlas, audit, and boundary analysis;
- `PROMO-C-K8-LOCAL-FACTORIZATION-ATLAS-N.md` — later-fold handoff only;
- `SHA256SUMS` — hashes of every package file except itself.

## Reproduction

From the repository root:

```bash
python3 notes/C-K8-LOCAL-FACTORIZATION-ATLAS-N/verify.py --limit 1000000
python3 notes/C-K8-LOCAL-FACTORIZATION-ATLAS-N/break.py \
  --expect-sha256 0aa69d8280b02a081023d40eebf95808875c786db50894f971e79c0ed14b6b25
```

Compare stdout byte-for-byte with the two expected-output files.

