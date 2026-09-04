# P-RAPIDITY-TARGET-RECONSTRUCTION-1 result

Status: PASS / proof-first candidate theorem with exact finite audit.
Public Canon v76 and all registered statuses remain unchanged.

## Result and scope

Clauses A-E of the frozen PREREG.md have self-contained proofs, independently
reviewed before execution. The accepted exact verifier passed all eight
gates and all five negative controls in its first formal Linux invocation.
No mathematical falsifier fired. The finite audit covers m=1,...,16;
the universal conclusions below rest on the written proofs, not that range.

For every polynomial of degree at most d, its value at -1 is reconstructed
uniquely from d+1 integer nodes 1-L_(2k), k=1,...,d+1. The target node is
excluded. The rational Lagrange weights have the exact q-product formula
in PREREG section 2, where q=(3-sqrt(5))/2. Their absolute sum increases
strictly to

```text
C(q)=1+2 sum_(j>=1)q^(j(j+1)/2) < 3-sqrt(5)/2 < 19/10.
```

Thus reconstruction of this one target has a uniform absolute input-error
norm below 1.9, independent of d. PREREG section 4 gives an explicit tail
bound for every K>=0 and the exact error norm for unequal input budgets.
The unweighted tail beyond the first node is below 1/2; truncating large
source values still requires the weighted value-tail bound stated there.

For independent relative errors, the monomial Q(z)=z^d, d>=1, supplies the
explicit contrasting boundary. With S=d(d+1)/2,

```text
q^(2-S) < kappa_d < 6q^(-S),
sup_(|e_k|<=eta|Q(x_k)|) |sum_k w_k e_k| = eta*kappa_d.
```

The relative amplification therefore grows as phi^(d(d+1)) within fixed
multiplicative constants. The theorem distinguishes absolute and relative
accuracy; it does not assign this worst case to the arithmetic family.

## Arithmetic meaning

The finite layer polynomial Q_N from the golden ladder has Q_N(-1)=M(N).
Its other positive golden rungs therefore determine M(N) without taking
M(N) itself as an input. This probe provides exact weights, a uniform
absolute norm, an omitted-value error formula and an explicit relative
accuracy boundary. It supplies no estimates for the input rung sums.

There is no RH conclusion, no Fourier identification, no general no-go,
and no claim that the actual B_a(N) or its estimation errors behave like
the independent monomial error box. The open trivial-rapidity bridge
remains open. This probe does not edit the Canon or registry.

## Evidence and review

The immutable public pin is recorded in RUN.md. PREREG.md and verify.py
were committed, pushed and read back byte for byte before either the
startup preflight or scientific execution. The two independent reviews
were static, proof-first and result-exposed, not blind. No pre-pin helper
calculation or development copy of the verifier was run.

The local invocation exited zero with empty stderr and 832 bytes of ASCII
LF stdout, committed exactly as EXPECTED.txt. G1-G8 passed; B1-B5 rejected
the wrong target, lost signs, duplicate nodes, inclusion of the target,
and the false relative cap. The final line is
`VERIFY RESULT 8/8 ALL PASS`.

The verifier uses only exact integers, fractions and rational pairs for
Q(sqrt(5)); its independent dense solve covers m<=6. It accepts no input,
performs no file/network/process operations, and uses no floating point.
The public bundle contains only the five named probe files, with no
external dataset, copied handoff material, private infrastructure, secrets,
binary artifacts or unreviewed third-party code. Required architecture
replay is enforced by the existing read-only pull-request workflow.

Any future Canon inclusion requires its own reviewed fold and earned
status decision. Classical Lagrange interpolation and q-product notation
are background; this result makes no novelty claim about those methods.
