# Native quadratic contact obstructions

This standard-library audit supports the self-contained L1 proof
QUADRATIC-L5-NATIVE-OBSTRUCTIONS. It checks the exact marked transport and
quadratic ranks, all five registered affine generators on all 15625 states,
both fixed-bit selector phase tables, full fibre histograms, triple collisions,
and a conditional rank-four linear-frame example. The last example is not a
selected reader or an extra premise of the theorem.

Run from the repository root:

```
python3 reproduce/native-quadratic-obstructions/verify.py
```

Exit code must be zero, stderr empty and stdout byte-identical to EXPECTED.txt.
The imported public generator source is bound by SHA-256. No external package,
randomness or floating-point arithmetic is used.

The universal affine no-go and two-branch bound follow from the written
polynomial rank and root-count proofs, not a search over words. The selector
bound concerns its literal complete-domain data update. No general nonlinear
contact no-go, repeated three-label implementation, physical memory or native
binary contact is asserted. This is a supplementary proof audit, not a new
formal probe or a retrospective preregistration of exploratory calculations.
