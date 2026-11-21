# Independent pre-pin review

Author of record: A. M. Thorn <thorn@twistj.com>.

These are separate reasoning-agent reviews within the same author session,
not external peer review and not blind confirmations. Reviewers saw the
proposed results. No reviewer executed or imported scientific code.

## Mathematical and scope review

Reviewer role: `ramified_scope`, separate from the proof author
`ramified_proof`. The complete preregistration and proof were inspected.

Final disposition: **PASS on all five precisely scoped claims**.

Two pre-pin corrections were required and read back:

1. In the finite-tree capacity proof, explicitly use `G=T_K`, `S subset G`
   and the complement `G\S`. Using the infinite tree complement of a finite
   subtree would incorrectly include children below the truncation. The
   infinite-tree case now explicitly switches to `G=T` and the full subtree.
2. Remove the optional local-codec extension; it is unnecessary for the
   frozen literal-address class and was not a registered target.

The final review checked the intrinsic ideal and metric, integer orbit
counts, affine transitivity, radius induction and finite-capacity transcript
injection. The last argument includes common outside initialization, total
cell capacity, simultaneous independent input symbols and fixed completion
time. It neither presumes reversibility nor concludes a physical no-go.

Reviewed exact SHA-256:

```text
PREREG.md 5f2a073e1ce66d2492e842a7853f05319d1deb27fc02bec0bfbd834f4a7cb589
PROOF.md  3a059dbd70dc8b42bb95809f378628f869eb131ad6169ba87515bb41541db767
```

## Static verifier review

Reviewer role: `ramified_code_review`, separate from code author
`ramified_verifier`. The complete code and preregistration were inspected.

Final disposition: **PASS; no blocking defect found**.

The reviewer independently derived multiplication by beta as
`(u,v,w,z) -> (u+z,v-u+z,w-v+z,2z-w)`. Its coordinate sum is `5z`,
which gives the coded exact division. The rational matrix inverse and
integer adjugate powers provide a second membership route. Quotient digit
ordering, parent coherence, inverse maps, full cycle census, reachability,
metric witnesses, inside boundary counts and deterministic failure routes
agree with the frozen finite scope.

```text
verify.py cfd8137b9a2a50a373e48521f99e20b24793f3b374763ca00213d374176c7fa4
bytes: 10816
```

The coordinator additionally compiled source text with Python `compile`
without execution or import; syntax passed. Runtime was only estimated from
operation counts before the pin, not measured. Finite output remains absent
until the accepted bytes are publicly pinned and read back.

## Adoption boundary

The reviews accept theorem-grade proofs at L1, conditional on the declared
carriers. They do not mark the claims canonical. Exact local execution and
the required x86_64/aarch64 replay must be recorded separately. A subsequent
reviewed Canon fold is the only adoption path. All existing H/O owners and
the active Public Canon v94 authority remain unchanged by this probe.
