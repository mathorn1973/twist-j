# Result: exact carry moments pass the frozen audit

2026-10-29. **NON-CANONICAL. L1 conditional mathematical result.**
Status: candidate-C for the first exact finite run; the universal statements
and limits rest on the accompanying analytical proof. No canonical status is
assigned.

## First completed execution

Public source pin: `65d2ae96d55fce7f527b2807e0e1f1fb2b5cdf38`.
The five source files were committed, pushed and read back byte for byte
before the first execution. The accepted verifier, preregistration, proof,
test family and failure thresholds are unchanged after that pin.

The first run completed with exit zero, empty stderr and 8576 bytes of exact
scientific stdout, preserved unchanged in `EXPECTED.txt`.
SHA-256: `0d42d526a8b4649cc6a48879b6086e45f02427929185ff98cc7325be6123a595`.
All five prescribed audit groups passed; no failure condition fired.
The recorded environment and source identities are in `RUN.md`.

## What was checked

| Check | Completed inventory |
| --- | ---: |
| Finite formula against exact carry DP, 12 cases through N=100 | 1200 |
| Rational finite-length error bounds | 1194 |
| Complete words of lengths 1 through 4 | 9360 |
| Off-diagonal mixed letter moments | 240 |
| Centered increment cross-covariances | 120 |
| Inverse-edge checks across the declared cases | 86095 |
| Distinct units in the algebraic family scan | 70 |
| Family units admitted by the depth condition | 68 |

Ring identities, trace/Gram agreement, exact lambda division, output-word
bijections, mean carry vectors, output marginals and delayed residue laws
also passed. Every scientific comparison used integers or fractions. The
formula predicted its own initial cross moments and did not consume moments
observed by the DP.

For counting digits, the J and J^-1 graphs both closed at 1649 states and
8245 edges, with maximum first-reach depth 28. Their respective maximum Q
values were 274 and 706. Complete graph closure is asserted for these two
prescribed cases. The other inverse-edge totals report the finite encountered
states, without importing a universal closure conclusion.

The family scan split the 68 admitted units into 56 at depth one and 12 at
depth two. The analytical depth-three clause is supported by the block proof;
the finite unit list contains no depth-three example. Enumeration of that
list does not prove the universal quantifier.

## Mathematical conclusion

On the class H of units with h=v_lambda(u-s) in {1,2,3}, the proof gives

```text
lim E Q(C_N) = mu^2 Q(u-1) + 2 Q(u/J) + 12.
```

The counting alphabet has minimum 36, exactly at J and conjugate(J).
The balanced alphabet has minimum 20, exactly at all ten units
±zeta^k phi^-1, k=0,...,4. The two real minimizers are covered by the
depth-two argument. The real ±phi have balanced limit 40, and real
±phi^-1 have balanced limit 20. Their entire prescribed finite sequences
agree with the formula and its rational error bound.

The scope controls also passed. Balanced ±1 preserve zero carry for every
letter, which proves zero carry at all lengths by induction. Their actual
moment is zero, while the unadmitted algebraic functional gives 24. The
prediction routine rejected ±1 and phi^5 in both alphabets; phi^5 has exact
depth four. Thus the unrestricted all-unit minimum 20 is not claimed.

The exact all-length formula, the limit and the complete equality sets are
analytical conclusions of `PROOF.md`. The finite audit checks the stated
instances and implementation. It does not establish convergence of the
entire carry distribution.

## Interpretation and evidence boundary

The alphabets, uniform independent input words, zero initial carry and trace
quadratic reading are supplied premises. No physical preparation, occurrence
law, Hamiltonian, work, dissipation or pulse-cost account is derived here.
The inverse carry mirror remains intact. Different quadratic readings in
separately initialized forward and inverse algorithms do not establish a
physical time arrow.

Earlier incubation values were known before this audit. This pin does not
retroactively preregister those calculations. The original first run is one
architecture; subsequent required GitHub architecture checks are separate
execution evidence and compare against the same committed stdout.

No Canon file, registry row, frontier owner, policy, workflow, tag or release
is changed by this probe. The separate reversible circuit in PR #1819 remains
unchanged.
