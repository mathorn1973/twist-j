# Fixed-pulse full-space error account with normwise roundoff bounds

PUBLIC NON-CANONICAL. Conditional L1 mathematics
and computational evidence. Apache-2.0, A. M. Thorn, 2026-10-11.
Reservation: https://github.com/mathorn1973/twist-j/issues/1460.

The preceding enlarged-space interval attempt was preserved as incomplete
after a manual resource stop. This successor retains its exact input bytes,
pulses, coherent seven-mode model, selected six branches, thermal weights,
cutoff ladder, time grids and full-space residual proof. It changes the
hot arithmetic checker to floating vector centers with analytically bounded
normwise errors. The predecessor remains unchanged and is not resumed.

Small coefficient intervals, Schur bounds, arithmetic-error recurrences and
norm reductions enclose all uncertainty introduced by the large vector
operations. The numerical candidate still defines an exact piecewise dyadic
polynomial whose full equation defect the checker attempts to bound. The account includes
the infinite displacement tail, between-node analytic remainder, endpoint
jumps, unnormalized thermal omission and restored-frame coherence evaluation.
Small observed roundoff or agreement between cutoffs is not used as a proof.

DERIVATION.md gives the mathematical contract. PREREG.md freezes the full
sources, workload and decisions. EXACT-DESIGN.md states the narrower scope
of the standard-library exact verifier:

```sh
python3 probes/P-U-CA40-BALL-CLOSURE-1/verify.py
```

Numerical execution requires Linux, 40 physical cores across two packages and all 80 logical
CPUs, AVX-512F/DQ/VL, GNU C++14.2, MPFR4.2.2 with thread-local support,
GMP6.3.0, Python3.13 and NumPy2.5. Compile without fast math or contraction:

```sh
g++ -O3 -std=c++20 -fopenmp -ffp-contract=off -fno-fast-math \
  -fno-tree-vectorize kernel.cpp validated_model.cpp -lmpfr -lgmp -o closure
python3 numerical_run.py --binary /absolute/path/closure \
  --output /absolute/path/new-output-directory
```

Development headers may be extracted into a private prefix. Preserve the
exact command, versions and binary hash. MPFR/GMP are external dependencies;
the [MPFR manual](https://www.mpfr.org/mpfr-current/mpfr.html) documents its
directed scalar arithmetic. The surrounding enclosure code needs its own
mathematical and implementation review.

The complete source pin must be publicly read back before first execution.
The runner checks source/input/binary custody around every attempted child,
explicitly binds 80 workers and preserves incomplete outcomes. Its four-hour
launch/run ceiling is a resource limit, not a promise of sufficient accuracy.

Only the selected three active branches per angle are assessed. Protected
electronic/source-reference identity remains conditional on exact darkness.
No physical ion experiment, complete work reservoir, native-contact bridge,
all-input channel guarantee or Canon promotion is claimed. Full intermediate
quintic trajectories are not retained, and exact-verifier CI is not a second
large numerical campaign.
