# Integer global Noether identity and generator nonclosure

**NON-CANONICAL, NEW_DECLARED L1.** Ownership:
https://github.com/mathorn1973/twist-j/issues/1653.

This probe takes the actual local energy/constraint extension in #1652
and checks its complete finite-horizon action. It proves and audits:

1. The full global gradient, including neighboring shift currents, with
   auxiliary variations in their actual mean-zero and co-closed spaces.
2. An exact first-order off-shell Noether completion
   delta_0 S_int+delta_1 S_0=0 and its generally nonzero second-order
   remainder for S_epsilon=S_0+epsilon S_int.
3. The explicit quadratic remainder in its first-order field-redefinition
   interpretation.
4. A proof that the specified nearest-time physical generator family
   does not close under commutators on the off-shell domain.
5. Exact integer forms of local continuity, the Noether pairing and
   the finite tangent displacement.

The first formal run is PASS. Here PASS includes verification of the
negative predictions: U=115/324 in the fixed remainder witness, a naive
central-difference defect of -1/8, a field-redefinition defect of -115/648,
and the nonclosure vector (-1/4,1/4,0,0,0). It does not mean that an exact
all-order gauge symmetry or nonlinear Einstein dynamics was obtained.

## Files and reproduction

| File | Purpose |
| --- | --- |
| PREREG.md | Frozen action, domains, transformations, integer representation, fixtures and falsifiers |
| PROOF.md | Complete global variation and proofs for arbitrary admitted rational data and finite T>=5 |
| SOURCE.md | Actual authority, companion pins, new choices and scope limits |
| verify.py | Analytic global-gradient and incidence implementation |
| breaker.py | Independently authored dual-number action and sparse-matrix implementation |
| FROZEN.sha256 | Immutable hashes of the five prospective source files |
| EXPECTED.txt | Unmodified 807-byte first scientific stdout |
| RUN.md | First-run timing, environment, hashes and prospective custody |
| RESULT.md | Observed results and their exact interpretation |
| REVIEW.md | Pre-pin analytical/static cross-review and independence disclosures |

From the repository root with Python 3.12 and the standard library:

```sh
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
  python3 -I probes/P-INTEGER-CUBIC-NOETHER-CLOSURE-1/verify.py
```

The primary launches breaker.py with the same executable and -I in a
separate process. It requires exact identity of all 767 certificate bytes
before appending its two terminal success lines. Successful final stdout
has 807 bytes, 24 LF and SHA-256
004569700d67d2c1d1614c056be97ce00eee3df732c887d30f8316e51dc5e98c.
It must match EXPECTED.txt byte for byte. The unchanged PR workflow runs
this contract on x86_64 and aarch64; actual remote receipts belong to the
PR and its completion comments.

The audit contains 798 global coordinate derivatives, 126 Noether and
126 integer Noether identities, 504 checks each of deformation, field
redefinition and integer tangent encoding, and 1140 full-array
commutator checks. Both payload digests are calculated independently.

## Interpretation

The valid local continuity and constraint compatibility from #1652 are
retained. The complete action has an exact first-order cancellation but
the frozen action/generator pair is not exactly invariant at epsilon=1.
The generator family must be enlarged or changed before its closure can
be asserted. This statement does not exclude higher-order corrections,
additional generators, different stencils, or integer gravity.

No new physical trajectory, canonical promotion, primitive denominator,
finite gauge group, banked update, ADM constraint algebra, 3D continuum
limit, Einstein-Hilbert identification or native-U realization is claimed.
