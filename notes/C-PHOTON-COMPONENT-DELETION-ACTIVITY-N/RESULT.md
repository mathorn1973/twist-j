# RESULT - C-PHOTON-COMPONENT-DELETION-ACTIVITY-N

**Verdict:** PASS at the frozen NON-CANONICAL scope.
**Ceiling:** candidate-T written proof; candidate-C finite audit.
**Canon:** unchanged.

## Exact deletion theorem

For one fixed complete marked augmented component K with A_K faces,

\[
\frac{\widetilde w({\rm full})}
     {\widetilde w({\rm full}\setminus K)}
=
2^{1-A_K}
\prod_e\frac{(r_e-t_e)!}{r_e!}
\le
2^{1-A_K}\prod_e\frac1{t_e!}.
\]

Deletion is injective on the occurrence event, so

\[
\boxed{
P_{\rm aug}(K\ {\rm occurs})
\le
z(K)
=
2^{1-A_K}\prod_e\frac1{t_e!}.
}
\]

All exterior charged and neutral components remain summed.

## Generic incidence floor

\[
\boxed{A_K\ge5M_K/4.}
\]

This is exact but too weak by itself to sum the full component entropy.

## Infinite connected control family

For

\[
n_N=\sum_{i=0}^{N-1}(-1)^i a(-i(e_2+e_3)),
\]

the written local motif and induction give

\[
A_N=17N+4,\qquad M_N=4N.
\]

Every neutral edge has degree two, every charged edge degree five, the neutral
matching is unique, and the entire support is one augmented component.
Therefore

\[
\frac{A_N}{M_N}
=
\frac{17}{4}+\frac1N
\to\frac{17}{4},
\]

and its standalone activity is exactly

\[
z_N=2^{-17N-3}.
\]

Thus the naive universal extrapolation \(A\ge21M/4\) from one elementary loop
is false already at N=2.

This does not prove \(A\ge17M/4\) in general.

## Remaining R3 debt

The fixed-pattern weight is now controlled exactly. What remains is to sum
over all possible marked component geometries containing a rooted charged
edge.

So the bottleneck is now isolated as component entropy, not component weight.
