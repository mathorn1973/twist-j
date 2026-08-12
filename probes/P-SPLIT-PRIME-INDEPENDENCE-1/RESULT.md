# P-SPLIT-PRIME-INDEPENDENCE-1 result

```text
VERDICT: PASS, 13 of 13 checks, exit 0, empty stderr, two architectures with
byte-identical stdout. No falsifier fired. No integrity STOP condition
occurred: the two decision paths agreed on every cross-checked instance, all
twenty-six positive controls fired under both paths, the non-vacuity clause
of the height claim behaved as required, and the executed check count equals
the declared clause count.
```

## What the run establishes and what it does not

The two claims are established by the WRITTEN PROOFS in `PREREG.md`. This
run is an audit of those proofs at finite scope and carries no universal
quantifier. Its evidential role is to exclude a coding or bookkeeping error
in the statements, to demonstrate that the detector can fire, and to show
that the verdicts do not depend on the generator gauge.

```text
claim A   no nonzero integer coefficient vector in the frozen boxes gives a
          vanishing combination of split-prime rapidity classes:
          368 families, 38352 coefficient vectors, 0 relations found
          5478 instances cross-checked by the second decision path, 0
          disagreements
claim B   for all twelve frozen split primes the reduced representative
          exists and is unique, the half-period endpoint is never attained,
          both embeddings of the reduced generator exceed one, the norm
          identity holds, and the unreduced generator fails the embedding
          test, so the clause is not vacuous
controls  26 of 26 positive controls fired under both paths: inert rational
          primes, the ramified generator, a split generator times its own
          conjugate, pure unit powers, and two generators of one ideal
          differing by a unit
gauge     66 gauge instances over the frozen exponents leave every claim A
          verdict unchanged, including sign change and conjugation
```

## Rows earned

```text
SPLIT-PRIME-RAPIDITY-INDEPENDENCE            T   10. Relativity as counting
REDUCED-SPLIT-GENERATOR-HEIGHT               T   10. Relativity as counting
```

Both are theorems with written proofs, so both are earned at T. The finite
audit is deliberately NOT proposed as a separate C row: it is subsumed by
the T statements and would add a row without adding content. The corollaries
of claim A (no torsion, injectivity of the multiple map, equidistribution of
the integer-multiple orbit, and the free subgroup after a choice of
orientation) are carried inside the scope of the first row and not as rows
of their own, with the explicit warning that the equidistribution statement
concerns multiples of a fixed finite set and is not a statement about the
distribution of primes.

## Dependency

Claim A consumes `SPLIT-PRIME-RAPIDITY-CLASS [T]` of Public Canon v44,
specifically its registered log-free equivalence, and unique factorisation
of fractional ideals. Claim B consumes claim A at k = 1, m = 2 for the
unattainability of the half-period endpoint. Nothing else is consumed and
nothing outside L1 is touched.
