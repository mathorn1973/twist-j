# Independent implementation contract: Galois-channel optimum

**PREREGISTERED, RESULT-EXPOSED, AUTHOR-CODE-BLIND CONSTRUCTION.**
Reviewer: A. M. Thorn / Codex-scope-review-20260919.
No scientific execution is reported in this pre-execution contract.

## Frozen input, code and exposure

The reviewer read the formal PREREG.md statement, finally SHA-256
`b6187ff3b6031a42294ff20e49db977f9d4e8b4f88c92fdc6fd970ef17473064`,
the exposed proposal and statement drafts, and the inherited public
Galois-code proof and Canon definitions. The final prereg amendment changes
only the check()->string integration sentence. Targets were known.
Neither incubation audit.py, new author verify.py nor new author PROOF.md
was read before this independent implementation was locally frozen:

```text
file: BREAKER.py
sha256: 62b73abac792adb21a32d0e7becf33a83bd74542156f93802a65611022b5b11e
```

Only exact standard-library Fraction arithmetic is used. Syntax was
checked with ast.parse, without importing or executing the code. No author
implementation or output comparison preceded the freeze. This is not a
blind prediction of an unknown result.

## Exact finite attack

Reconstruct C,F,Q,D from the fixed H and matrix dimensions. Independently
construct the five- and seventeen-Kraus maps, the point-exact control,
four-state auxiliary control, full U20 and all its stated factors. Require:

- Code normalization, native endpoint action, and nonisometry of the full
  native point pushforward outside the code.
- Exact Kraus completeness; transfer of all sixteen source matrix units;
  all code/complement cross terms and their reverse; every raw output
  coordinate distribution; and the off-code coherence discrepancy.
- Choi ranks five and seventeen from independent exact elimination of
  vectorized Kraus operators. These give concrete channel ranks, not
  uniqueness of the optimal global channel.
- Every complement coordinate effect equals the stated sum of outer
  products, has rank four and satisfies A_k^2=(3/4)A_k; effects sum to Q.
- The independent simplex diagonal minor equals (1/2)I+(1/16)J and has
  rank four, certifying independence over both R and C.
- The fixed point-exact control loses the selected coded target; the
  four-state control transfers the code while its raw populations are 1/4.
- Full U20 orthogonality, complete factor-product equality, every loaded
  code column, and the matched loader/inverse-loader cancellation. Matrix
  equality includes every residual output, rather than selected ports.

Every equality is exact. Any assertion failure, exception, nonzero exit,
stderr, timeout or replay-byte mismatch fails the audit and is preserved.
No numerical tolerance or code repair after the public pin is allowed.
Finite checks of selected channels are not a search of all complex CPTP
maps and do not by themselves prove the universal claims below.

## Independent complete-class proof reasoning

For a Stinespring isometry V, exact pure-code transfer gives
`VC alpha=F alpha tensor eta_alpha`. Preservation of coherent
superpositions, or equivalently all source matrix units, forces one common
unit environment vector eta. Orthogonality of V on code and complement
gives `<F alpha tensor eta,Vz>=0` for every alpha and complement z.
F is onto the entire four-dimensional output, so Vz lies in output tensor
eta-perp. Partial trace therefore removes all cross terms and yields
`Phi(X)=DXD*+Psi(QXQ)` with Psi TP on the complement. This reasoning is
over complex Hilbert spaces; the examples being rational restrict no
universal quantifier.

At fixed k the four q_ka are orthogonal of squared norm 3/4, so
`S_k=sum_a |q_ka><q_ka|=(3/4)P_k` for a rank-four projection P_k.
For positive effects A_k summing to Q, total complement agreement is
`sum_k Tr(A_k S_k)<= (3/4)Tr Q=9`. The total fixed code contribution is
one. Mean agreement is at most 10/16=5/8; minimum agreement is at most
the mean. The explicit effects S_k attain equality at every raw point.

Mean equality forces every positive slack to vanish and hence
`A_k=P_k A_k P_k`. Expand each A_k in the q_ka basis. For each pair a,b,
the corresponding block of `sum A_k=Q` is a linear combination of the
four signed-conjugate simplex outer products. For
`q_k=e_k-(1/4)1`, the diagonal minor of `|q_k><q_k|` is
`(1/2)I+(1/16)J`; its eigenvalues are 1/2 (threefold) and 3/4.
Thus the four products are independent even with complex coefficients.
Each block fixes its coefficients to delta_ab, including all off-block
coefficients, forcing exactly A_k=S_k. Worst-coordinate equality also
forces mean equality, because all sixteen agreements are then at least
5/8 and the mean is at most 5/8. Effects are unique, channels are not.

The code uses the common environment line. For a pure auxiliary of total
dimension d, each complement coordinate effect has rank at most d-1,
since the complement occupies output tensor eta-perp. Rank four therefore
requires d>=5. The independent five-Kraus construction attains this bound.
Mixed auxiliaries count their purification. Without optimization, the
four-state control shows that exact code transfer alone does not force
five. All statements retain the external CPTP premise and provide no
physical preparation, coupling, outcome record, occurrence law or reset.

## Public pin and execution

Pin this contract and the exact independent code with the formal statement
and author verifier before either implementation executes. Public readback
must match these bytes. The lane owns the commit and execution records.

API: `check()` returns a deterministic string and prints nothing. The
author verifier uses `print(BREAKER.check())` after its JSON report.
Standalone `python3 probes/P-U-GALOIS-CHANNEL-OPTIMUM-1/BREAKER.py`
prints the return string and a newline. Its successful target line is:

```text
INDEPENDENT_BREAKER_B PASS bound=5/8 auxiliary=5 choi_ranks=5,17 raw=16 matrix_units=16
```

This line has not been observed at preregistration. After the shared public
pin, preserve the first standalone stdout as BREAKER-EXPECTED.txt and
record command, environment, exit, stderr, code and output hashes in the
review record. Use the existing probe's Linux-compatible environment and
600-second bound. Required x86_64 and aarch64 replays execute the same
independent code through the author verifier and compare the complete
combined output against the one committed EXPECTED.txt. Such replay is
reproduction; author-code-blind construction and the written argument
are the separate independent contributions.
