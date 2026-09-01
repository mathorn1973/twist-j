# PROMO-C-K8-LOCAL-FACTORIZATION-ATLAS-N

> **PROMOTION HANDOFF ONLY — NO PROMOTION PERFORMED.** The source package is a
> NON-CANONICAL incubation with maximum grade `candidate-T / L1`. A later,
> distinct public fold must independently review and authorize any movement.

## Candidate payload

For `Phi_8(x)=x^4+1` and `K_8=Q(zeta_8)`:

1. shifted Eisenstein proves `Phi_8` irreducible over both `Q` and `Q_2`;
2. modulo every rational prime it is reducible;
3. for odd `p`, the complete atlas is

   | `p mod 8` | factor type | `(e,f,g)` | Frobenius fixed field |
   |---:|---|---|---|
   | 1 | `1+1+1+1` | `(1,1,4)` | `K_8` |
   | 3 | `2+2` via `sqrt(-2)` | `(1,2,2)` | `Q(sqrt(-2))` |
   | 5 | `2+2` via `sqrt(-1)` | `(1,2,2)` | `Q(i)` |
   | 7 | `2+2` via `sqrt(2)` | `(1,2,2)` | `Q(sqrt(2))` |

4. at `p=2`, the reduction is `(x+1)^4` and the profile is `(4,1,1)`;
5. the prime number theorem for arithmetic progressions (equivalently
   Chebotarev here) gives densities `1/4` completely split and `3/4` type
   `2+2`, with no unramified inert rational prime;
6. with ordered CRT factors `(x^2-2,x^2-3)` at `p=5`,
   `O_8/(5) ~= F_25 x F_25` and `i -> (2,3)`; `sigma_5` stays within the
   factors and `sigma_7` swaps them.

## One-line elementary core

For odd `p`,

\[
  \left(\frac{-2}{p}\right)
  =\left(\frac{-1}{p}\right)\left(\frac{2}{p}\right),
\]

so at least one of `-1,2,-2` is a square; the exact corresponding polynomial
identity supplies a quadratic factorization. The residue-class and
irreducibility arguments in `RESULT.md` upgrade this to the complete atlas.

## Evidence package

```text
LOCK ISSUE:          #749
LOCK BASE:           46be0601a78827fb4e98d5892ffa7966652d1c25
PREREG PIN:          aea19ff5238c05bb47fd39a735a440525caf09a1
verify.py SHA256:    94023c59094a20e46f644170a1d6601fec07314a74b9461d73738e44891c0f98
break.py SHA256:     0aa69d8280b02a081023d40eebf95808875c786db50894f971e79c0ed14b6b25
VERIFIER:            PASS
BLIND BREAKER:       NO_FALSIFIER_FOUND
AUDIT LIMIT:         1,000,000
```

The public issue pin predates both executions. `RUN.md`, exact stdout files,
and `SHA256SUMS` make the run reproducible. The proof in `RESULT.md`, not the
finite scan, carries universality.

## Import ledger; do not duplicate

Any fold must preserve the registered ownership of:

- `QUARTIC-CYCLOTOMIC-TOTAL-RAMIFICATION-CENSUS [T]`;
- `Z2-PLACES-SPLIT [T]`;
- `DEGREES-BY-PRIME [T]`;
- `BORN-RESIDUAL-SPLIT [T]`;
- `C8-MARKING-RIGIDITY [T]`;
- `C8-PAULI-QUOTIENT-TRANSPORT [T]`;
- `I-BILOCATED [D]`, which must remain `[D]`.

The full unit group at `p=5` is `C_24 x C_24`; the imported cyclic order-`24`
Born group is the swap-norm-one subgroup. This is a clarification of scope,
not a correction or a new promotion target.

## Promotion firewall

A later fold must retain all of these boundaries:

- “local atlas” means modular reduction and prime decomposition, not
  factorization over every `Q_p`;
- Legendre symbols are used only for odd primes; `p=2` is separate;
- for `p == 1 mod 8`, all three routes coexist;
- route variation neither contradicts nor proves global irreducibility;
- the `p=5` coordinate order is declared and no component is canonical;
- there is no RH, physical, field-merger, degree-minimality, or quartic
  uniqueness claim;
- no public status changes solely because this PROMO file exists.

## Requested later-fold decision

Review only whether the new atlas/synthesis merits a canonical `[T]` row at
`L1`. Until that separate decision is merged under `POLICY.md`, the status is
exactly `candidate-T / L1`.
