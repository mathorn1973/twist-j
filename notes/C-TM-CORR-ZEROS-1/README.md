# notes/C-TM-CORR-ZEROS-1

NON-CANONICAL. Incubation-lane candidate bundle, 2026-07-30. Nothing here is
evidence for a public claim and no file here creates, moves or anchors a
registry row. No formal public probe exists for this candidate: the runs are
single-platform and no public preregistration pin was made before them, so
they cannot serve a `probes/` directory. Read
`C-TM-CORR-ZEROS-1_RESULT_2026-07-30.md` for the outcome and its limits.

The subject is the balanced two-point correlation of the Thue-Morse word,
`c(k) = lim (1/N) sum_(n<N) u_n u_(n+k)` with `u_n = (-1)^(s_2(n) mod 2)`.
The claim under test is that `c(k) = 0` exactly when the odd part of `k` is
`5` or `7`.

```
PREREG-C-TM-CORR-ZEROS-1.md                 the six frozen prereg fields,
                                            frozen before any code existed
verify_tm_corr_zeros_1.py                   verifier, gates V1-V5, stdlib
                                            only, int and Fraction, no float
                                            sha256 abc364e2b6173c06eaa51d271d7c81f14cfa9bdc914afd21756fc85cc2dfb243
verify_tm_corr_zeros_1.stdout.txt           pinned stdout, exit 0, 8/8 PASS
                                            sha256 1bf97accdaf1678eb948a7abf5a251550e47148b8fa9a290861817107e0a8fae
break_tm_corr_zeros_1.py                    breaker, gates B1-B6, independent
                                            code path
                                            sha256 69d7e71667b7fbe8456443acb9921670f7838c9ff5046f5bbd24b7dd633221c0
break_tm_corr_zeros_1.stdout.txt            pinned stdout, exit 0,
                                            NO FALSIFIER FIRED
                                            sha256 4a9a6341585b2469745fd5a7e948c1a41185ab73803fec24c20df64a27ac323f
C-TM-CORR-ZEROS-1_RESULT_2026-07-30.md      result, candidate labels only,
                                            gate transcript, the fifteen
                                            preregistration defects, and the
                                            literature status
SHA256SUMS.txt                              hashes of the files above
```

## Reproduction

```sh
cd notes/C-TM-CORR-ZEROS-1
env LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
    python3 verify_tm_corr_zeros_1.py
env LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
    python3 break_tm_corr_zeros_1.py
sha256sum -c SHA256SUMS.txt
```

Expected: verifier exit 0 with stdout sha256
`1bf97accdaf1678eb948a7abf5a251550e47148b8fa9a290861817107e0a8fae`; breaker
exit 0 with stdout sha256
`4a9a6341585b2469745fd5a7e948c1a41185ab73803fec24c20df64a27ac323f`. Both were
byte-identical across two consecutive runs on Linux x86_64 with Python 3.12.3.
The verifier takes about 4 s and the breaker about 18 s. A rerun that differs
in any byte is a finding and must be preserved, not repaired.

## Status of the result

The zero classification is **proved**, not merely checked, and the proof is
short enough to verify by hand. The proof recommended in the result document
avoids 2-adic valuations entirely: rescaling `c` by `3 * 2^(L(m)-3)` turns the
recursion into an integer transfer with the single invariant "`A + B` is odd",
which closes under both branches from the base layer `m in {4,5,6,7}`.

Two limits govern how this may be used.

**Priority is not available for half the statement.** Coons, Mazáč,
Pincus-Kazmar and Stout, arXiv:2511.06386 (9 Nov 2025), states
`eta(2^n + 2^(n-2)) = 0`, and `2^n + 2^(n-2) = 5 * 2^(n-2)`, so the whole
`{5 * 2^a}` family is published; the recursion itself is classical. Literature
clearance is **not** achieved: the `7 * 2^a` family, the exhaustiveness
direction, the proof method, and the finite-`N` identity and its discrepancy
bound remain uncleared, and two likely sources were unreadable and need a human
reader. See the result document.

**One platform.** Every computational label is a candidate label. A public
probe would have to preregister and pin first, then reproduce byte-identically
on two architectures; until then a computation-only row is at most `C`.

The fold proposal is `notes/canon/PROMO-C-TM-CORR-ZEROS-1.md` and changes
nothing until a separate sealed public fold.
