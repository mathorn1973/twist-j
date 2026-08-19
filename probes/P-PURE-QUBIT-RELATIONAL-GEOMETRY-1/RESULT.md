# P-PURE-QUBIT-RELATIONAL-GEOMETRY-1 result

Status: `SCIENTIFIC FALSIFIED / INTEGRITY STOP / PROBE CLOSED / CANON UNCHANGED`

## Verdict

The pinned verifier produced its expected PASS transcript, but the independent
post-run science audit fired an exact preregistered falsifier. Therefore this
probe supports no scientific or Canon promotion.

The frozen `2 x n` extension declares the unhalved ambient tensor wedge
`u wedge v = u tensor v - v tensor u` and then asserts

```text
det(A A^dagger)
  = sum_(i<j) |u_i v_j-u_j v_i|^2
  = ||u wedge v||^2.
```

For the declared norm the exact identity is instead

```text
det(A A^dagger)
  = sum_(i<j) |u_i v_j-u_j v_i|^2
  = (1/2) ||u wedge v||_tensor^2.
```

For example `u=(1,0)` and `v=(0,1)` give determinant 1, minors sum 1,
and unhalved tensor-wedge norm squared 2. This is one exact counterexample to
a universally quantified R1 equality, which meets the frozen scientific
failure threshold.

The verifier did not catch the defect because its variable `wedge_norm`
computes the minors sum rather than the ambient norm of the declared unhalved
tensor. Its byte-identical PASS output is preserved in `EXPECTED.txt` and
`RUN.md`; it is not evidence for the false statement.

The audit also retained three protocol defects: the phase witness `A=I` is
outside the normalized carrier, the printed breaker IDs do not match the
frozen B1-B3 scheme, and the interpreter guard accepts versions outside the
declared Python 3.12 workflow. None is repaired in this sealed probe.

## Disposition

```text
PURE-QUBIT-RELATIONAL-AREA               no disposition
PURE-QUBIT-LOCAL-RELATION-PYTHAGORAS     no disposition
PURE-QUBIT-RELATIONAL-CHSH               no disposition
PURE-QUBIT-RELATIONAL-READING            no disposition
```

All four IDs remain unearned and non-canonical. The public Canon is unchanged.
The threshold and files were not amended or rerun. Any corrected attack must
use a fresh identifier and fresh immutable pin.
