# Replacement comment for issue #407

NON-CANONICAL. Incubation record. This comment supersedes the earlier comment
in this thread in full. The earlier comment contained two errors, listed at the
end, and must be edited or struck rather than left standing beside this one.
Nothing here changes the Canon, opens a branch, or creates a gate.

## Verdict

```text
TT-VECTOR-STATE-NORMALIZATION   [O] / STOP   unchanged, not closed either way
child candidate                 candidate-T  no falsifier fired
gate created                    none
```

## Currency gate, run before the work

`main` at `4020c5373453ef4b8466a8738337be187fc238b6`. Public Canon v50 ACTIVE.
Tag `canon-v50` resolves to `6b40d54831d9204a5bee9277177b4de1dae8b529` and the
declared content commit `b68c60c5` are both ancestors of `main`.
`canon/SHA256SUMS` 5 of 5 OK. `canon/CANON.md` 240724 bytes, SHA-256
`f99f5eeb42db3e9d40bc6a46f716aa98d7af1925b66989406e0b3671ab43a9fe`, agreeing
with `STATUS.md`. No probe directory or registry identifier collides.
`canon/NORMATIVE.tsv` types `TT-SQUARING-DECODER`, `POL-READ` and the parent as
`NOT_APPLICABLE` with empty `gate_ids`; `canon/GATES.tsv` has 10 rows and none
owns this normalization.

## The blocker, in its corrected form

On `X = Z/5` at scale `a = 1`, with `z = zeta_5`:

```text
A    v_x = z^{t_x},         (t_x) iid uniform on Z/5
B    v_x = z^{t_0} eps_x,   t_0 uniform on Z/5, independent of
                            (eps_x) iid uniform on {+1,-1}
```

Both are invariant under site translation and under the four-fold site action
`(rho_u v)_x = v_{u^{-1} x}`, `u` in `(Z/5)^*`, with no accompanying action on
coefficients. Both have deterministic pointwise modulus `|v_x| = 1`. Both have
`E[v_x] = 0`, `C_{xy} = delta_{xy}`, `P_{xy} = 0`, hence `S_v(k) = 1` and
`Pi_v(k) = 0`. Every monomial of total degree at most 3 agrees, so no quadratic
functional separates them in expectation. Under the squaring readout
`w = v^2`, `S_w(k) = 1` for all `k` under `A` and `S_w(k) = 5 delta_{k,0}`
under `B`, with `Pi_w = 0` under both. The minimal separating degree is
exactly 4 and the degree-4 separators are exactly the 20 monomials
`v_x^2 conj(v_y)^2` with `x != y`.

Second part, an independent no-go. If `E[v_x] = 0`, `P_{xx} = 0` and
`|v_x|^2 = a^2` almost surely with `a > 0`, then `E[|v_x|^4] = a^4` while the
Isserlis closure demands `2 a^4`. The fourth cumulant is `K_{xx} = -a^4`,
never zero. So freezing a Wick or Gaussian boundary is not an available repair
of the parent while the pointwise modulus is held fixed.

Amplification found while trying to break the above, and disclosed as
post-freeze rather than folded in: the family is not a pair. For every `m` in
`Z/5` the law `v_x = z^{t_0} eps_x z^{m x}` shares all data through degree 3
with `A`, while `S_w(k) = 5 delta_{k, 2m}`. Those five laws and `A` and every
mixture of them are mutually indistinguishable below degree 4, and `S_w`
ranges over the flat spectrum, five distinct single-mode peaks and their
convex hull.

## Evidence

Preregistration frozen and hashed before first execution; verifier and breaker
hashed with it. Exact arithmetic in `Q(zeta_5)`, no float in any assertion,
Python standard library only.

```text
PREREG.md    sha256 091ef70b0b0f65247afab229c1d4a8a9ade7ccdaa9a0009de6f26a052a7d519d  11477 B
verify.py    sha256 68238c8609a6e651a11f760d493045e015839bd3810ed05466823e21c2a3fc7c  13398 B
breaker.py   sha256 6fc905cec73a5bc3607b384723ea0d25eaf6c91a17828b64b64075c891bcff43   9112 B
EXPECTED.txt sha256 d547022e0aad57f2fa7ab36fa1a2c575f345c8169572130a7d6bb1e0a0acefe6   4313 B
BREAK.txt    sha256 0ac5a53d4046a123d666410004e6bc9545c942ec38e98ed88c950d866301064d   1064 B
```

Verifier 63 of 63 PASS, exit 0, empty stderr, three byte-identical runs.
Breaker 13 of 13 PASS, zero breaks, on a code path sharing nothing with the
verifier: closed-form character sums against enumeration, a full sweep of all
1001 monomials of total degree at most 4, and an exact-rational scan for a
positive scale surviving the Isserlis condition.

One leg only, x86_64. No aarch64 leg, no GitHub check. Nothing here is
promoted on one leg.

## Corrections to the earlier comment in this thread

```text
E1  the earlier comment conflated global multiplication v -> i v with the
    spatial action of (Z/5)^* on sites. They are different groups acting on
    different objects. The claim that the peak can be placed in an arbitrary
    mode while spatial four-fold invariance is retained at fixed m is WRONG
    and is withdrawn. The correct statement is a trichotomy: m = 0 is
    invariant with the peak at k = 0; fixed m != 0 places the peak at k = 2m
    but breaks the spatial action; the uniform mixture over the four nonzero
    m restores the action and gives (5/4)(1 - delta_{k,0}).
E2  the earlier comment wrote Tr(C^2) style conclusions and pseudo-spectrum
    claims without fixing whether |v_x| = 1 was meant pointwise almost surely
    or in expectation. It is pointwise almost surely. Both readings were left
    open and only one supports the Wick no-go.
```

Both errors were found by audit, not by a run, and neither survives into the
frozen candidate.

## Where this leaves the parent

The parent is not closed and is not weakened. It asks for a public
vector-doublet normalization yielding a numerical `r_T(k)`; this supplies none.
What it supplies is an exhibited obstruction that narrows the repair space:
any admissible normalization must freeze fourth-moment data, the complete
state, or an explicit non-Gaussian closure rule, and it cannot reach for a
Gaussian boundary at deterministic pointwise modulus. The historical route
through `G_0 = [[6,-3],[-3,4]]` with `B^T G_0 B = G_0` stays algebraically
exact and can still normalize the historical doublet, but a homogeneous
`k`-independent prefactor cannot manufacture a `k`-dependent denominator
`r_T(k)`. That is a type mismatch, not a gap in a proof.

Next smallest step: the public child probe
`P-TT-VECTOR-MOMENT-UNDERDETERMINATION-1`, claimed in its own issue, run on
two architectures. The parent stays open.
