# P-J-BINARY-NORM-INDEX-1 result

Date: 2026-08-22

```text
DECISION:   J-BINARY-NORM-INDEX-CONFIRMED
CHECKS:     20 of 20 PASS, exit 0, empty stderr
PIN:        815d99ea85697bc9b4742b6036126ae8058d47e2
CLAIM LOCK: issue 522
LAYER:      L1 state only
BASIS:      Public Canon v60, tag canon-v60, content 18b21bd,
            CANON_SHA256 9387b75f...d46db0, CANON_BYTES 329876
```

No threshold moved after the pin. No falsifier fired. Nothing in this directory
changes `canon/`, the registry, the frontier, or any live `H` or `O` row; a fold
is a separate later act and is sequenced through issue 503.

## 1. What was asked

Let `K = Q(zeta_5)`, `O_K = Z[zeta_5]`, `N = N_{K/Q}` and `J = 1 + zeta_5^2`,
with `N(J) = 1`. At a prime `p` inert in `K` the residue ring is the field of
`p^4` elements. Norm one is a constraint on the reduction. How strong a
constraint, and where can a norm-one unit still generate the whole
multiplicative group of the residue field?

## 2. What was found

```text
J-BINARY-NORM-INDEX                  earned status T, scope L1
  Reduction commutes with the norm, so N(u) = 1 places ubar in the kernel of
  N_(F_(p^4)/F_p). That kernel is cyclic of order
  (p^4 - 1)/(p - 1) = (p + 1)(p^2 + 1), of index exactly p - 1. It is the whole
  group if and only if p - 1 = 1. Hence a unit of norm one can generate the
  multiplicative group of an inert residue field only at p = 2. At p = 2,
  ord(Jbar) = 15 = |F_16^x|, so J attains the one available case.

J-BINARY-NORM-ORDER-CENSUS           earned status C, scope L1, range below 2000
  Among the 156 primes inert in K below 2000, Jbar generates the whole
  norm-one subgroup exactly at p = 2 and p = 3, and at every other such prime
  its order is a proper divisor of (p + 1)(p^2 + 1).
```

The first row rests on a written proof plus an exact machine audit, which is
why it is `T` rather than `C`. The written steps are the surjectivity of the
residue norm, which fixes the index at `p - 1`, and the two order computations
`J^3 = zeta_5^3` of order five and `J^5 = zeta_5^2 + zeta_5^3` of order three,
which force `ord(Jbar) = 15`. The verifier audits both; it does not carry the
universal quantifier by itself. The second row is finite-range computation and
stays at `C`.

## 3. The controls, which are the load-bearing half

Two controls bound the reading, and both passed.

```text
GENERIC     the index is p - 1 in degrees 2, 3, 4, 6 and 8 alike. The
            uniqueness of the binary place is therefore a statement about the
            order of F_p^x. It is not a fact about J, not about the prime five,
            and not about degree four. Only the attainment is about J.

GALOIS      1 + zeta_5, 1 + zeta_5^2, 1 + zeta_5^3 and 1 + zeta_5^4 reduce to
            J^8, J, J^4 and J^2, one Frobenius orbit, all of order fifteen. The
            attainment is therefore Galois invariant and cannot distinguish the
            exponent a in J = 1 + zeta_5^a.
```

Two further controls separate the constraint from its two failure modes.
`zeta_5` has norm one and order five at `p = 2`, so norm one permits generation
without forcing it. `w = 2 + zeta_5` has `N(w) = 11`, so its residue norm is
`11 mod p`, which is `2` at `p = 3`, and it is therefore not confined to the
norm-one subgroup at all.

## 4. Relation to the parent lane

`J-BINARY-NORM-DESCENT [T]` records that `bar(D_J)` acts as `k -> k+2` while
Frobenius acts as `k -> 2k` on `mu_5`, and that field integrity modulo two does
not uniquely select `J` or characteristic two. Nothing here weakens,
contradicts or moves that row. The `GALOIS` control above reaches the same
negative conclusion on a second invariant, and the `GENERIC` control removes
the remaining way to read this result as a selection: the mechanism does not
mention `J` at all.

What is added is one lemma and one order. The lemma explains why the binary
place is the only place where the question can have a positive answer. The
order shows the answer there is positive.

## 5. Scope, stated as a firewall

```text
MAY      the index lemma, the uniqueness of p = 2, ord(Jbar) = 15, the two
         controls, and the finite census at C with its range attached.
MAY NOT  any selection of J, of the axiom exponent, or of characteristic two.
         Any zeta function, Dedekind zeta, Artin factorization, Weil conjecture
         or Riemann hypothesis statement: none is made here, and none follows.
         No decoder, apparatus, instrument, pointer, event stream or measure.
```

`SAMPLING NOT PROVIDED`. No layer lift is performed or named anywhere in this
probe.

## 6. Disclosure

RESULT-EXPOSED, not blind, as preregistered. The two theorems and the census
were derived in non-canonical incubation work on the same date and exercised
there by two implementations with different representations. Those runs are
discovery context and are not evidence. The accepted verifier was written
fresh, pinned before any execution, read back from the public remote, and run
exactly once.

The preregistration was drafted in a session that had read access to the public
remote and no write access; it could not open the claim issue, push, or pin.
The claim issue, the pin commit, the read-back and the single formal run were
performed afterwards from an authorized workstation. The invariant that matters
is unchanged and is auditable from the public history: the accepted verifier
had never been executed when its bytes were pinned.
