# TWIST-J in Lean

Status: **NON-CANONICAL**. This directory changes no claim, status, scope,
evidence, registry row, frontier row or Canon line.

## Direction

Owner decision of 2026-11-25: Lean is to become the only route to `T`. A
Python verifier establishes finite-range fact and can fire a falsifier; it
cannot by itself earn a theorem. Writing that rule into `POLICY.md` is a
separate policy change and has not been made. Until it is made, the existing
policy governs every status, and this directory is preparation only.

The Canon stays the authority on what a claim says. A Lean statement is a
translation of a Canon claim and is judged against the Canon text, never the
other way round. A Lean statement that is weaker, stronger or different from
its Canon row covers nothing.

## Architecture

The weak point of machine-written formal mathematics is the statement, not
the proof: a kernel-checked proof of a mistranslated statement is worthless.
The library therefore keeps two surfaces apart.

```text
statement surface   definitions and theorem types only, read by the owner
                    or an independent reviewer against the Canon text and
                    frozen by SHA-256 before any proof work starts
proof surface       untrusted; any author or agent; accepted only if the
                    pinned kernel checks it against the frozen statement
                    with no sorryAx and no project axiom
```

The statement surface lives under `Challenge/`, one file per library file:
the same definitions and theorem types with every proof replaced by `sorry`.
`Challenge/Kernel.lean` is the surface of `TwistJ/Kernel.lean` (eighteen
statements, eighteen `sorry`). It is built only on request:

```bash
lake build Challenge
```

From layer 1 onward no proof file is accepted without its challenge file.

## Pin

```text
Lean toolchain   leanprover/lean4:v4.33.1
Mathlib          0df444a360eaa60ab8c11dca51a86af692955474
Lake manifest    lake-manifest.json, every package at a full revision
```

## Build

From this directory:

```bash
lake build
lake env lean Audit.lean
```

`Audit.lean` prints the axiom footprint of every declaration. The expected
footprint is `propext` and `Quot.sound`, plus `Classical.choice` for the
cyclotomic witness. Reviewed manually on Debian 13, x86_64: build exit 0, no
`sorryAx`, no project axiom. That is a review note, not a run record.

## Layer 0: the axiom

`TwistJ/Kernel.lean` proves, in an arbitrary commutative ring, from the single
hypothesis `Phi5 j : j^4 + j^3 + j^2 + j + 1 = 0`. The hypothesis cannot be
weakened to `j^5 = 1`: at `j = 1` in `ℤ` most of the identities fail.


```text
j^5 = 1
J phi = j                      J = 1 + j^2, phi = -j^2 - j^3
(J - 1)^3 = j
phi^2 = phi + 1,  phi (1 - phi) = -1
J (-j - j^2) = 1
J^5 phi^5 = 1
(1 + j^2)(1 + j^4)(1 + j^6)(1 + j^8) = 1
(1 + j^2) + (1 + j^4) + (1 + j^6) + (1 + j^8) = 3
J (a + b j + c j^2 + d j^3) = (a - c + d) + (b - c) j + a j^2 + (b - c + d) j^3
J Jbar = 2 - phi,  (2 - phi) phi^2 = 1          Jbar = 1 + j^3
1 - J = -j^2,  (1 - J)^5 = -1,  (1 - J)^10 = 1
J^4 - 3 J^3 + 4 J^2 - 2 J + 1 = 0
```

and shows the hypothesis is inhabited by Mathlib's generator of
`CyclotomicField 5 ℚ`.

Coverage against section 1 of the Canon, as a translation check, not a status:

```text
J-GOLDEN-BRIDGE    all three displayed equations
J-STEP             step formula and characteristic polynomial; open, as
                   separate obligations: det and trace of M_J as a matrix,
                   Algebra.norm and Algebra.trace of J, and the tie between
                   the two
J-MODULUS-CHORD    J Jbar = 2 - phi and 2 - phi = phi^-2 in the ring
J-TENTH-ROOT       1 - J = -j^2 with (1 - J)^5 = -1 and (1 - J)^10 = 1, a
                   necessary condition only; primitivity (exact order ten)
                   and the archimedean value e^(-i pi/5) are open
J-UNIT             unit with explicit inverse, ring-level norm product; the
                   Mathlib Algebra.norm statement is open
J-PROJECTIONS      open (archimedean embedding)
```

The two ring-level products above are products of the four images
`1 + j^(2t)` inside the ring. They are not yet tied to `Algebra.norm` and
`Algebra.trace` of Mathlib; that tie is the next step of layer 1.

## Next layers

1. Layer 1: `Z[j]` as the ring of integers of `ℚ(ζ₅)`, the explicit carrier
   `Z^4` with `M_J`, `Algebra.norm` and `Algebra.trace`, and the unit group
   `μ₁₀ × φ^ℤ`.
2. The first proof wave: the 93 rows of `TRIAGE.md` that need only Mathlib
   and the kernel.
3. The TWIST vocabulary as a statement surface for owner review: the native
   update on `N₀ × F₅⁶`, counter, checkpoint, readout, records, ports. It
   gates the other 162 rows.

## Relation to earlier Lean work

`notes/lean-j-cyclotomic/` is unchanged and is not imported. The unmerged
branches `notes/lean-twistj-foundations-1`, `-observation-2`,
`-layer-typing-3` and `-algebraic-seed-4` (Lean 4.30.0) are sources of
inspiration only, not dependencies; anything taken from them is re-read
against the current Canon and re-proved at this pin.
