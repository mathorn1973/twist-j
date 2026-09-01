# Result — complete rational-prime atlas for `Phi_8`

> **NON-CANONICAL INCUBATION.** Maximum grade: `candidate-T / L1`. This result
> moves no Canon, Registry, Frontier, gate, evidence, or program status.

## Verdict

`C-K8-LOCAL-FACTORIZATION-ATLAS-N` survives its frozen proof obligations and
both exact audits. The accepted verifier returned `PASS`; the independently
authored blind breaker returned `NO_FALSIFIER_FOUND`. The result is therefore
packaged as `candidate-T / L1`, not as a canonical theorem.

The universal statement rests on the proof below. The exhaustive scan through
`p <= 1,000,000` is only an audit.

## Candidate theorem

Let

\[
  \Phi_8(x)=x^4+1,\qquad K_8=\mathbf Q(\zeta_8).
\]

Then `Phi_8` is irreducible over `Q` but its reduction is reducible for every
rational prime. For every odd prime the complete factor-degree type and prime
decomposition in `K_8` depend only on the residue class modulo `8`:

| `p mod 8` | `((-1)/p,(2)/p,(-2)/p)` | available routes | factor degrees | Frobenius | fixed field | `(e,f,g)` |
|---:|---|---|---|---|---|---|
| 1 | `(+,+,+)` | all three | `1+1+1+1` | `sigma_1` | `K_8` | `(1,1,4)` |
| 3 | `(-,-,+)` | `sqrt(-2)` | `2+2` | `sigma_3` | `Q(sqrt(-2))` | `(1,2,2)` |
| 5 | `(+,-,-)` | `sqrt(-1)` | `2+2` | `sigma_5` | `Q(i)` | `(1,2,2)` |
| 7 | `(-,+,-)` | `sqrt(2)` | `2+2` | `sigma_7` | `Q(sqrt(2))` | `(1,2,2)` |

At the ramified prime `2`,

\[
  \Phi_8(x)\equiv(x+1)^4\pmod2,
  \qquad (e,f,g)=(4,1,1),
\]

but `Phi_8` remains irreducible over `Q_2`.

Consequently, completely split primes have density `1/4`, primes of type
`2+2` have density `3/4`, and there is no unramified inert rational prime.

## Proof

### 1. Global and `2`-adic irreducibility

Translation gives

\[
  \Phi_8(x+1)=x^4+4x^3+6x^2+4x+2.
\]

Every non-leading coefficient is divisible by `2`, the constant coefficient
is not divisible by `4`, and the leading coefficient is not divisible by `2`.
Eisenstein at `2` therefore proves irreducibility over `Q`. The same
Eisenstein criterion over `Q_2` proves irreducibility there as well.

Modulo `2`, `x^4+1=(x+1)^4`. If `alpha=zeta_8-1`, the displayed Eisenstein
polynomial is the minimal polynomial of `alpha` over `Q_2`; hence `alpha` is a
uniformizer in a totally ramified degree-four extension. Thus
`(e,f,g)=(4,1,1)`. The ramification is wild because the residue characteristic
`2` divides `e=4`.

This is the crucial boundary: reducibility modulo every rational prime does
not imply reducibility over every `Q_p`.

### 2. The three exact routes for odd primes

The polynomial identities are

\[
  x^4+1=(x^2-i)(x^2+i),\qquad i^2=-1,
\]

\[
  x^4+1=(x^2+s x+1)(x^2-s x+1),\qquad s^2=2,
\]

\[
  x^4+1=(x^2+t x-1)(x^2-t x-1),\qquad t^2=-2.
\]

For every odd prime `p`, multiplicativity of the Legendre symbol gives

\[
  \left(\frac{-2}{p}\right)
  =\left(\frac{-1}{p}\right)\left(\frac{2}{p}\right).
\]

If the first two symbols are both `-1`, the third is `+1`; otherwise one of
the first two is already `+1`. Thus at least one route is available. The
supplementary laws

\[
  \left(\frac{-1}{p}\right)=(-1)^{(p-1)/2},\qquad
  \left(\frac{2}{p}\right)=(-1)^{(p^2-1)/8}
\]

give exactly the four rows in the table. In particular, for `p == 1 mod 8`
all three routes exist simultaneously; the routes are not unique there.

### 3. Exact factor degrees

For `p == 3 mod 8`, take `t^2=-2`. Each `t`-quadratic has discriminant
`t^2+4=2`, which is a nonsquare in this residue class, so both quadratics are
irreducible.

For `p == 7 mod 8`, take `s^2=2`. Each `s`-quadratic has discriminant
`s^2-4=-2`, again a nonsquare, so both are irreducible.

For `p == 5 mod 8`, take `i^2=-1`. The element `i` has order four. If it were a
square in `F_p`, its square root would have order eight, forcing
`8 | (p-1)`, contrary to `p == 5 mod 8`. The same holds for `-i`. Since the
discriminants of `x^2-i` and `x^2+i` are `4i` and `-4i`, both quadratics are
irreducible.

For `p == 1 mod 8`, the cyclic group `F_p^x` contains an element of order
eight. Its four odd powers are precisely the four roots of `x^4+1`, so the
polynomial splits completely.

Only `2` ramifies in `K_8`. For odd `p`, Frobenius is
`sigma_p(zeta_8)=zeta_8^p`, its order is `ord_8(p)`, and the usual cyclotomic
decomposition formula gives

\[
  e=1,\qquad f=\operatorname{ord}_8(p),\qquad g=4/f.
\]

This proves both the factor-degree and `(e,f,g)` columns.

### 4. `V_4` and its fixed fields

The Galois group is

\[
  (\mathbf Z/8\mathbf Z)^\times=\{1,3,5,7\}\cong V_4,
  \qquad \sigma_a(\zeta_8)=\zeta_8^a.
\]

Writing `i=zeta_8^2` and `sqrt(2)=zeta_8+zeta_8^{-1}`, the signs are

| automorphism | `i` | `sqrt(2)` | `sqrt(-2)=i sqrt(2)` | fixed field |
|---|---:|---:|---:|---|
| `sigma_3` | `-` | `-` | `+` | `Q(sqrt(-2))` |
| `sigma_5` | `+` | `-` | `-` | `Q(i)` |
| `sigma_7` | `-` | `+` | `-` | `Q(sqrt(2))` |

Every nonidentity element has order two. Equivalently, every unramified
Frobenius has order one or two, never four. Hence there is no unramified inert
rational prime.

The prime number theorem for arithmetic progressions gives density `1/4` to
each reduced residue class modulo `8`; equivalently, Chebotarev gives density
`1/4` to each singleton conjugacy class in the abelian group `V_4`. Therefore class `1` contributes density
`1/4` of complete splitting, while classes `3,5,7` contribute total density
`3/4` of type `2+2`.

### 5. Ordered residual component audit at `p=5`

Fix the CRT factor order

\[
  (x^2-2)\ \text{first},\qquad (x^2-3)\ \text{second}.
\]

Then

\[
  x^4+1=(x^2-2)(x^2-3)\pmod5.
\]

Both `2` and `3` are nonsquares modulo `5`, so both quadratics are
irreducible. With `u^2=2` and `v^2=3`, the ordered CRT isomorphism is

\[
  \mathcal O_8/(5)
  \cong \mathbf F_5[u]/(u^2-2)\times\mathbf F_5[v]/(v^2-3)
  \cong\mathbf F_{25}\times\mathbf F_{25}.
\]

The image of `zeta_8` is `(u,v)`, so

\[
  i=\zeta_8^2\longmapsto(2,3),
\]

which is not diagonal. Frobenius `sigma_5` preserves the two ordered factors:
`u^5=-u` and `v^5=-v`, while `i` remains `(2,3)`. Complex conjugation
`sigma_7` swaps the two components and sends `i` to `-i=(3,2)`.

Thus a conditional external marking `i=2` selects the first component only
after the order has been declared. Arithmetic alone supplies no canonical
component selector, and `I-BILOCATED` remains exactly `[D]`.

The full unit group is

\[
  (\mathbf F_{25}\times\mathbf F_{25})^\times
  \cong C_{24}\times C_{24}.
\]

The cyclic order-`24` group in the imported Born row is the norm-one subgroup
for the swap involution, not the full unit group.

## Registered dependencies and exact delta

Imported without re-promotion:

- `QUARTIC-CYCLOTOMIC-TOTAL-RAMIFICATION-CENSUS [T]` — discriminant and the
  already registered `p=2` ramification profile;
- `Z2-PLACES-SPLIT [T]` — the `K_8` Klein-four structure;
- `DEGREES-BY-PRIME [T]` — the existing `i,sqrt(2) in K_8` statements;
- `BORN-RESIDUAL-SPLIT [T]` — residual splitting and conjugation swap;
- `C8-MARKING-RIGIDITY [T]` and `C8-PAULI-QUOTIENT-TRANSPORT [T]` — the
  exponent actions and absence of a canonical orientation;
- `I-BILOCATED [D]` — retained at `[D]`, never promoted or merged.

The candidate delta is only the all-prime atlas, three-route/fixed-field
synthesis, and ordered residual component audit. The nearby non-canonical
`C-CYCLOTOMIC-RAMIFIED-HERMITIAN-SHEETS-N` uses related mod-`8` characters in
a different carrier and is not a claim collision.

## Frozen audits

Both executables were publicly pinned before execution. Exact outputs are in
`EXPECTED.txt` and `BREAKER_EXPECTED.txt`.

| audit | scope | outcome |
|---|---|---|
| accepted verifier | all 78,497 odd primes `<= 1,000,000`; identities; factor degrees; `V_4`; `p=2`; ordered `p=5` | `PASS` |
| blind breaker | distinct divisor enumeration, small-field brute force, exact cyclotomic action, explicit CRT product and units | `NO_FALSIFIER_FOUND` |

The observed odd-prime row counts were `19,552`, `19,653`, `19,623`, and
`19,669` for residues `1,3,5,7`. Those finite counts do not prove the density
statement; the prime number theorem for arithmetic progressions (equivalently
Chebotarev here) does.

## Boundary and nonclaims

The available modular witnesses vary with `p`; for `p == 1 mod 8`, all three
exist together. They do not contradict one another, and their variation is
not a proof or cause of irreducibility over `Q`. Shifted Eisenstein is that
proof.

No claim is made about degree-four minimality, uniqueness among other quartic
cyclotomic fields, RH, a physical bridge, a field merger, or a canonical
orientation selector.
