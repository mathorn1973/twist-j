# P-QPAIR-C4-2I-MINIMALITY-1 result

Date: 2026-08-18. Preregistration pinned at commit
`c934d22b1f56a0fcb17d13bb0e66cfcd3412393f` after the public claim-lock
correction and before every accepted formal run.

## Verdict

```text
QPAIR-HERM-INTEGER-NONDESCENT                         proposed [T]
QPAIR-TRANSPOSE-FIBER-REDUNDANCY                     proposed [T]
QPAIR-TYPED-MIXED-C4-CLOSURE                         proposed [T]
QPAIR-SYM2-2I-IRREDUCIBLE                            proposed [T]
QPAIR-MINIMAL-2I-CLOSURE-OF-HERM-UNDER-MIXED-C4      proposed [T]
QPAIR-2I-ONLY-PAIR-FORCING                           proposed [F]
QPAIR-MIXED-C4-NORMALIZES-2I                         proposed [F]
formal audit                                          26/26 PASS
QUADRATIC-DECODER-DATA                                [O] / STOP, unchanged
```

The integer witness `v=(1,1)`, `zeta_5 v` proves that the Hermitian slot
does not carry a total descent of the mixed order-four state action on the
independent integral spinor lattice. The field fiber is `K^1 v`; equal
nonzero content restricts its unit part to `mu_10`, while the displayed
`2+zeta_5` witness proves that the full lattice can have wider fibers.

The symmetric slot has exactly the fibers `+-v`, so the pair and the
symmetric slot contain the same set-theoretic information. This explicitly
rules out an informational defense of two slots. It does not supply a
polynomial, rational, typed-natural, or admissible factorization.

The frozen typed pair is closed under the mixed order-four action. Relative
to the admissible class that retains the fixed Hermitian coordinates as a
linear readout and requires simultaneous stability under the marked `2I`
pullbacks and `Phi`, the least coordinate space is the full ten-dimensional
real quadratic carrier `H direct-sum S`. The marked
`Sym^2(2a)=3a` irreducibility and the explicit orbit of `z1 z2` carry the
minimality step.

## Exact negative boundaries

`2I` alone does not force a pair: `v -> vv^T` is already a single-slot
equivariant carrier, with the exact adjoint presentation
`Y -> Y epsilon^-1`. No invariant standard trace-zero Hermitian slice,
graph, or quotient is claimed in the marked nonunitary basis.

The mixed action does not normalize the marked `2I`: the conjugate of
`T_0` contains `c(z_1)` and is not `K`-linear. Hence there is no claimed
`2I semidirect-product C4`, direct product, or identification with the
distinct registered `COLOR-CM-2I-SEMILINEAR-PAIR`.

## Evidence

```text
PREREG.md    sha256 31f1ff7317c386ace36020d4515e6e5890eb4bb1e98fc96c3615042c1fed7f63  21819 B
verify.py    sha256 5ec126c323fedb03175cf17194a0fe45a83afbdfe6b2466734823c0b35786e00  20861 B
EXPECTED.txt sha256 5bca7df68594c3f6c0bca9f9f7433492fb6436bf62ba8401e47ff7482cc10929    811 B
```

The accepted local leg ran twice from a fresh detached public worktree at the
pin on Ubuntu 24.04.3 LTS, x86_64, CPython 3.12.13, with deterministic
environment, exit zero, empty stderr, and byte-identical stdout.

## Scope firewall

The carrier is `O_K^2` with independent coordinates, not the diagonal
Minkowski image of one field element and not rational `V_eff`. The result
creates five typed definitions for this carrier and admissible class, but no
bridge to `DEF-QDD-QPAIR`, MatterData, Born pairing, decoder write map,
physical `U(1)`, instrument, L5 stream, or L6 measure. It moves no QDD or
color-selection parent and creates no physical uniqueness statement.
