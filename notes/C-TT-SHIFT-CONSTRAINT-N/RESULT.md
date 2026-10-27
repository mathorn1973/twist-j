# C-TT-SHIFT-CONSTRAINT-N: local result record

**NON-CANONICAL. No authority, no public verifier gate, no Canon promotion,
no O/H closure.** Identities candidate-T (operator identities for every
antisymmetric circulant `D` with `L = -D^2`, and polynomial identities in the
explicit `D_c` model); construction and declared choices candidate-D.

## Freeze and execution order

```text
PREREG.md frozen           2026-09-08T17:04:48Z
  sha256                   d38e9fb3a272e0d8ed93cf83c744c920e91a7ca017cb8a471b760c5f1e013026
verify.py frozen           2026-09-08T17:09:47Z, after a static read and py_compile, before execution
  sha256                   a7650b047843c29bf3d3a55e4e2f849ba1eaced34a08cb65be7fb490142f827a
  run                      exit 0, 18 checks, 0 failed, stderr empty (first and only run)
  stdout                   EXPECTED.txt
                           sha256 8f56d4a5a2f99309988d83a0cded3f2fb3d08efa6673e0bbe3c55e3aee813ae7
environment, leg 1         x86_64, Ubuntu 24.04, Python 3.11.15,
                           LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
environment, leg 2         arm64, macOS 26.5, Python 3.13.13, same variables, same frozen bytes:
                           exit 0, stderr empty, stdout byte-identical (same SHA-256)
```

Two architectures, byte-identical stdout, one author and one code path. A
local two-architecture record, not the public GitHub gate.

## Kinds of check

- P1, P2: operator identities in the symbol algebra; universal in `D`.
- P3: polynomial identities in all 200 field and 80 gauge variables of the
  explicit time-periodic `D_c` model; and equality of its Euler-Lagrange
  polynomials with the P1 expressions instantiated with `D_c`, all fields,
  slices and sites.
- P4: a symbolic circulant identity and an integer non-square test.
- P5, P6, P7: exact rational array computations (ranks, solves, witnesses).

No check is declarative; none samples random configurations for a universal
claim (the random TT data in P7 are a solution witness, not a proof of
uniqueness; uniqueness on nonzero modes follows from the rank facts).

## What the run establishes, at scope

- Exact gauge invariance of the discrete lapse-shift action under the
  four-parameter linearized diffeomorphism family, on the lattice, with the
  stated time staggering (FA no fire).
- The Noether identities `(E - 1) EL_n = D EL_N3`, `(E^-1 - 1) EL_Ni = D EL_hi3`
  (`i = 1, 2`), `(E^-1 - 1) EL_N3 = 2 D EL_h33`: Hamiltonian and momentum
  constraints are preserved by the evolution equations (FB no fire).
- The exact conservation laws a prescribed source must satisfy:
  `(1 - E) rho = D J_3`, `(E^-1 - 1) J_i = D S_i3`.
- The covector K1 stress (`J = 0`, `S_33 = -iota/2`) violates them for every
  word; the K1 intensities admit a conserved completion; the transverse
  stress is unconstrained (FE no fire).
- The #909 witness `h_13 = n f(r)` is excluded by the momentum constraint in
  the zero-shift gauge and is the pure-gauge configuration `xi_1 = n D^-1 f`
  (FC no fire).
- TT-only data are exact solutions of the full constrained system; on nonzero
  modes the constraints force `tau = 0` and time-constant `h_13, h_23`
  (rank 4 of `D` and `L`) (FD no fire at linear order).
- No rational antisymmetric circulant on `Z/5` squares to the public stencil
  (discriminant `4 . 71 . 151`); the rational `D_c` gives a different
  Laplacian `L_c`.
- Zero mode: `-rho_hat_0 = 0` on the static flat background; no solution with
  the K1 energy.

## What it does not establish

No second-order TT self-source and no decision of the #909 transcriptions;
no FRW background and no solution of the homogeneous component; no
three-dimensional carrier; no Regge-Wheeler coefficient; no physical meaning
of `tau`, no `P_S`, no `r_T`. No owner condition C1 to C5 is claimed
complete. No original O/H closes.
