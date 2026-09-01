# C-K8-LOCAL-FACTORIZATION-ATLAS-N — preregistration

> **NON-CANONICAL INCUBATION.** This directory has no Canon, Registry,
> Frontier, gate, or evidence authority. Its ceiling is `candidate-T / L1`.
> Any promotion would require a later, distinct public fold under `POLICY.md`.

## Object lock and authority basis

```text
OBJECT:          C-K8-LOCAL-FACTORIZATION-ATLAS-N
OWNER:           session-k8-atlas-2026-09-01
LOCK ISSUE:      #749
BRANCH:          notes/c-k8-local-factorization-atlas-n
PATH:            notes/C-K8-LOCAL-FACTORIZATION-ATLAS-N/
LOCK BASE:       46be0601a78827fb4e98d5892ffa7966652d1c25
PUBLIC CANON:    Public Canon v74
TAG:             canon-v74
CONTENT_COMMIT:  2561f7dcadcbbf683ce7b36219ea67378d879a5a
CANON_SHA256:    2db550cb68f6f4ee33b9194f1f6b3bc4d8fec19cd79e79a702c5357577a92c0e
CANON_BYTES:     389246
MAX GRADE:       candidate-T / L1
FORMAL PROBE:    NONE
```

This preregistration freezes the claims, proof obligations, audit inputs, and
falsifiers before either executable is run.

## Frozen mathematical question

For

\[
  \Phi _8(x)=x^4+1,\qquad K_8=\mathbf Q(\zeta _8),
\]

is there a complete, elementary rational-prime atlas which explains why
`Phi_8` is irreducible over `Q` yet reducible modulo every rational prime,
without falsely asserting reducibility over every local field `Q_p`?

Here “local atlas” means reductions modulo rational primes together with prime
decomposition data in `K_8`. It does **not** mean a claim that `Phi_8` factors
over every `Q_p`; the `Q_2` statement below says the opposite.

## Registered dependencies and candidate delta

This incubation imports, without re-proving or re-promoting, the registered
scopes of `QUARTIC-CYCLOTOMIC-TOTAL-RAMIFICATION-CENSUS [T]` (in particular
`disc(K_8)=2^8`, `2 O_8 = p^4`, and `(4,1,1)`),
`Z2-PLACES-SPLIT [T]` (the `K_8` Klein-four/involution structure),
`BORN-RESIDUAL-SPLIT [T]` (the split residual ring and conjugation swap), and
`C8-MARKING-RIGIDITY [T]` (the order-eight lift and the exponent-`5` versus
exponent-`7` actions), together with `DEGREES-BY-PRIME [T]` for the existing
`i,sqrt(2) in K_8` degree statements. `I-BILOCATED` remains exactly `[D]`.

The new candidate scope is only the complete all-rational-prime factorization
atlas, its three elementary square-root routes and fixed-field synthesis, and
the ordered `p=5` component audit. It does not claim the imported rows anew.
The nearby non-canonical note
`C-CYCLOTOMIC-RAMIFIED-HERMITIAN-SHEETS-N` uses the same mod-`8` Legendre
character pair inside a different `L4` carrier; that overlap is a dependency
surface, not an identifier or claim collision.

## Frozen candidate statements

The incubation will accept at most the following `candidate-T / L1` package.

1. `Phi_8` is irreducible over `Q`; indeed
   \(\Phi _8(x+1)=x^4+4x^3+6x^2+4x+2\) is Eisenstein at `2`.
2. For every odd prime `p`, at least one of `-1`, `2`, `-2` is a square
   modulo `p`, because
   \[
      \left(\frac{-2}{p}\right)
      =\left(\frac{-1}{p}\right)\left(\frac{2}{p}\right).
   \]
   The corresponding exact identities are
   \[
   x^4+1=(x^2-i)(x^2+i),\quad i^2=-1,
   \]
   \[
   x^4+1=(x^2+s x+1)(x^2-s x+1),\quad s^2=2,
   \]
   \[
   x^4+1=(x^2+t x-1)(x^2-t x-1),\quad t^2=-2.
   \]
3. For odd `p`, the factorization and local profile depend only on `p mod 8`:

   | `p mod 8` | square routes | factor degrees | `(e,f,g)` |
   |---:|---|---|---|
   | 1 | `-1, 2, -2` | `1+1+1+1` | `(1,1,4)` |
   | 3 | `-2` | `2+2` | `(1,2,2)` |
   | 5 | `-1` | `2+2` | `(1,2,2)` |
   | 7 | `2` | `2+2` | `(1,2,2)` |

   The two displayed quadratics in the last three rows must be shown
   irreducible, not merely multiplied back to `Phi_8`.
4. At `p=2`,
   \(\Phi _8(x)\equiv(x+1)^4\pmod2\), while the same shifted Eisenstein
   calculation proves `Phi_8` irreducible over `Q_2`; the local profile is
   `(e,f,g)=(4,1,1)`, with total wild ramification.
5. `Gal(K_8/Q)=(Z/8Z)^times` is the Klein four group. With
   `sigma_a(zeta_8)=zeta_8^a`, the fixed fields are

   | involution | fixed quadratic field |
   |---|---|
   | `sigma_3` | `Q(sqrt(-2))` |
   | `sigma_5` | `Q(i)` |
   | `sigma_7` | `Q(sqrt(2))` |

6. The Chebotarev/Dirichlet densities are `1/4` for complete splitting and
   `3/4` for type `2+2`; there is no unramified inert rational prime because
   no element of `V_4` has order `4` (hence its density is zero).
7. With factors ordered as
   \[
      (x^2-2)\ \text{first},\qquad (x^2-3)\ \text{second},
   \]
   one has
   \[
      \mathcal O_8/(5)\cong\mathbf F_{25}\times\mathbf F_{25},
      \qquad i=\zeta_8^2\longmapsto(2,3).
   \]
   Thus, once the conditional `[D]` marking `i=2` is externally imposed, it
   selects the first component; the arithmetic supplies no canonical
   component selector and this is not a diagonal equality. `sigma_5` acts within the two factors, whereas complex
   conjugation `sigma_7` swaps them and sends `(2,3)` to `(3,2)`.
   The full unit group of this product ring is `C_24 x C_24`; the cyclic
   order-`24` group in the imported Born row is its norm-one subgroup for the
   swap involution, not the full unit group.

## Precommitted proof route

- Use shifted Eisenstein both globally and over `Q_2`.
- Use the supplementary laws for the Legendre symbols of `-1` and `2`, plus
  multiplicativity for `-2`, to obtain the four residue rows.
- For `p == 3 mod 8`, the `t`-quadratics have discriminant `2`, a nonsquare.
- For `p == 5 mod 8`, a root `i` of `-1` has order four; it cannot be a square
  because `p-1 == 4 mod 8`, so `x^2-i` and `x^2+i` are irreducible.
- For `p == 7 mod 8`, the `s`-quadratics have discriminant `-2`, a nonsquare.
- For `p == 1 mod 8`, an element of order eight gives all four linear roots.
- Read residue degrees from Frobenius order in `(Z/8Z)^times`; treat `p=2`
  separately as ramified.
- Derive the fixed fields by the signs of `i`, `sqrt(2)`, and their product
  under `sigma_3`, `sigma_5`, `sigma_7`.
- At `p=5`, use the ordered CRT factors above and track `zeta_8^2` explicitly.

No scan is admitted as a proof of universality.

## Frozen exact audit

`verify.py` is a Python-standard-library-only verifier. Its frozen default
input is every prime `p <= 1,000,000`. It will:

- verify all three polynomial identities in the relevant quadratic quotient;
- verify shifted Eisenstein and the `p=2` reduction;
- enumerate primes by an exact sieve;
- compute Legendre symbols and modular square roots, multiply every available
  route back to `Phi_8`, and audit the predicted residue row;
- determine factor degrees independently via polynomial gcd and Frobenius
  powers modulo `Phi_8`;
- audit the `V_4` signs/fixed fields and the ordered `p=5` component action;
- fail closed on the first mismatch and emit deterministic stdout on success.

An independent breaker will be authored from this preregistration only. It is
forbidden to read or derive from `verify.py`. It will use a materially distinct
implementation and attack the decisive falsifiers below.

## Decisive falsifiers

Any one of these forces `REJECTED` rather than a candidate result:

- a failed displayed polynomial identity;
- an odd prime for which none of `-1,2,-2` is a square;
- a residue-class/factor-degree/Frobenius/local-profile mismatch;
- reducibility of `Phi_8` over `Q_2`, or any inference from modular
  reducibility to reducibility over all `Q_p`;
- a wrong fixed field;
- a diagonal interpretation of `i -> (2,3)`, wrong factor ordering, or a
  confusion of the actions of `sigma_5` and `sigma_7`;
- collision with a current canonical row at stronger scope;
- mismatch between pinned executable bytes and executed bytes.

## Explicit exclusions

There is no RH claim, physical interpretation, field merger, canonical
orientation selector, or promotion of `I-BILOCATED [D]`. This is not a formal
probe and earns no evidence credit.
