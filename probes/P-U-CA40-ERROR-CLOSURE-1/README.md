# Fixed-pulse seven-mode numerical error account

PUBLIC NON-CANONICAL. Conditional L1 mathematics and computer-assisted
numerical enclosures. Apache-2.0, A. M. Thorn, 2026-10-11.
Reservation: https://github.com/mathorn1973/twist-j/issues/1458.

The sealed predecessor `P-U-CA40-SINUS-COMPARISON-1` found sizeable finite
sine/full-linear differences, but did not certify their infinite-dimensional
numerical error. This successor retains its input bytes, pulses, chronology,
seven modes, thermal preparation and selected three-branch panel per angle.
It enlarges the dynamic basis and encloses the defect of the computed curve
in the full Hilbert space. It does not resume or rewrite the sealed result.

`DERIVATION.md` proves the error-account contract. `PREREG.md` freezes its
execution and decision rules. `EXACT-DESIGN.md` scopes the small exact audit;
that audit does not certify an actual floating trajectory.

The fast candidate is RK4 with an arbitrary dyadic quintic reconstruction.
An online, directed-rounding AVX-512 checker encloses the full equation
defect at rigorously enclosed Gauss nodes. A complex-time analytic bound
controls everything between nodes; a normal-order creation tail controls
states outside the guard basis. The total account includes all polynomial
endpoint jumps, unnormalized thermal omission, non-unit endpoint norms,
coefficient/function rounding and final electronic-coherence evaluation.

The original JSON decimal tokens define exact rational input parameters.
Pi, square roots and the coherent relation eta=kappa*exp(i*k*x) are enclosed
with 192-bit MPFR arithmetic. The separately stored, rounded legacy eta
array is audited by its maximum difference, not silently equated to that
identity. This is a numerical certificate for the explicitly supplied
coherent model; it does not certify measured constants or the omitted
physical interactions.

## Reproduction

The accepted exact gate, from the repository root, is:

```sh
python3 probes/P-U-CA40-ERROR-CLOSURE-1/verify.py
```

The numerical runner requires Linux, all 80 logical CPUs of two 20-core
packages, AVX-512F/DQ/VL, GNU C++14.2, MPFR4.2.2 with thread-local support,
GMP6.3.0, Python3.13 and NumPy2.5. It requires gradual underflow and nearest
rounding for the candidate; the certificate uses explicit directed SIMD
instructions. Compile without contraction, fast math or auto-vectorization:

```sh
g++ -O3 -std=c++20 -fopenmp -ffp-contract=off -fno-fast-math \
  -fno-tree-vectorize kernel.cpp validated_model.cpp -lmpfr -lgmp -o closure
python3 numerical_run.py --binary /absolute/path/closure \
  --output /absolute/path/new-output-directory
```

Development headers may be extracted into a private prefix instead of
installed system-wide; record the include paths, exact compiler command,
library/package versions and binary hash. MPFR/GMP are external runtime
dependencies, not copied implementation code. The MPFR directed-rounding
contract is documented in the [official manual](https://www.mpfr.org/mpfr-current/mpfr.html).

The source manifest and immutable public pin must be checked before a first
run. The runner serializes the unchanged JSON decimal tokens into a new
input, verifies every source and binary hash around every child, explicitly
binds all 80 workers, and preserves completed and partial receipts. Its
eight-hour launch/run budget is a ceiling, not a speed prediction.

The online checker and candidate share a process, but have separate
arithmetic paths. All final states and per-column component totals are
retained with hashes. Intermediate quintic arrays are streamed, not retained
as a full offline trajectory archive. Rechecking every intermediate defect
therefore requires deterministic replay of the pinned program. Same-session
code review is not blinded replication or a second numerical campaign.

Protected electronic registers and their external reference remain exactly
unchanged only under the inherited exact-darkness premise. The separate
unknown-source/retained-informative-record obstruction remains unchanged.
No ion experiment, physical contact admission, complete work-reservoir
account, native-U bridge or Canon promotion is supplied.
