# NOTE-RELATIONAL-AREA-INTERACTIVE (2026-08-19)

NON-CANONICAL. Exposition artifact. Standard quantum mechanics only, explicitly
not TWIST-specific, per the owner. No claim, no verifier, no registry effect.

## What it is

`vztah-ma-tvar.html`, a single self-contained Czech interactive page. Two
draggable vectors; everything else is derived live from them. Built to make the
owner's own physical reading of entanglement graspable by hand: the relation is
real and measurable, but it is owned by neither party.

## The reading it makes visible

The two draggable vectors are the columns of the coefficient matrix `X` of a
pure two-qubit state, given their conditional meaning: `u` is the (unnormalized)
state of A when B is `|0>`, `v` is the state of A when B is `|1>`. Parallel
means B tells you nothing about A, so a product state. Perpendicular and equal
in length means B tells you everything. The measure of the difference is neither
the angle nor the lengths but the area they span.

```text
Q      = |u|^2 + |v|^2
D      = u ^ v = det X
C      = 2|D| / Q                    concurrence, scale invariant
|b|    = sqrt(1 - C^2)               local Bloch length
s0,s1  = sqrt((1 +- |b|)/2)          Schmidt numbers, s0 s1 = C/2
det rho_A = C^2/4
B_max  = 2 sqrt(1 + C^2)
```

Three linked pictures, one number:

1. Pythagoras. Legs `|b|` and `C`, hypotenuse always 1. The right angle is not
   drawn by hand, it follows from Thales on the unit-diameter circle, so the
   identity `|b|^2 + C^2 = 1` is carried by the construction rather than
   asserted. This is the #422 PYTHAGOREAN-PURE picture.
2. Rectangle. Sides `s0` and `s1`, diagonal always 1, area always `C/2`, from a
   degenerate line at product to a square at maximal. This is the #419 rectangle
   picture.
3. What A sees alone. The Bloch vector shrinking from the surface to the centre.
   The path inward is not a loss, it is exactly what appeared in the area.

Plus a CHSH meter, `2 <= B_max <= 2 sqrt2`, with the classical bound and
Tsirelson marked.

## One thing the drag makes obvious that the formulas hide

`C` factors into two independent conditions, both of which must be 1:

```text
C = sin(phi) * 2|u||v| / (|u|^2 + |v|^2)
      angle          length balance
```

The preset "kolmé, ale nevyvážené" sets the angle factor to exactly 1 while the
balance factor is `0.624`, so `C = 0.624` at a full right angle. Perpendicularity
alone does not buy maximal entanglement. The page draws the balance condition as
a dashed circle of radius `|u|` and both conditions together as a ghost target.

## Boundaries stated on the page, not in a footnote

- Mixed states do not carry the simple geometry. Werner at `p = 1/2` is
  entangled but violates no CHSH, and `|b|^2 + C^2 = 1/16`, not 1. For pure
  states any entanglement violates CHSH; for mixed states these are two
  different questions.
- Above Schmidt rank two one area no longer suffices; the parallelogram becomes
  the full bivector and only `||u ^ v||^2 = det rho_A` survives as the simple
  statement. Hard boundary: pure two qubits yes, mixed or higher rank no.
- The planar drawing is the real case. No generality is lost, since Schmidt
  puts every pure two-qubit state in real form by local rotations without moving
  `C`, `|b|` or `B_max`.

## Checks run

Rendered under Chromium at 980 and 390 px, light and dark. Every preset
verified against its intended value through the live DOM readouts:

```text
součin              C = 0,000   |b| = 1,000   B_max = 2,000   E = 0,0000
slabý               C = 0,250   |b| = 0,968   B_max = 2,062   E = 0,1176
poloviční           C = 0,500   |b| = 0,866   B_max = 2,236   E = 0,3546
Bell                C = 1,000   |b| = 0,000   B_max = 2,828   E = 1,0000 ebit
kolmé nevyvážené    C = 0,624   |b| = 0,782   B_max = 2,357   angle 1,000 x balance 0,624
```

`|b|^2 + C^2` reads `1,000000` at every preset and throughout dragging.
Pointer drag and arrow-key nudging both exercised. The only console error is the
Google Font failing to resolve in the offline sandbox; the page falls back to
Georgia and is otherwise dependency-free.

## Where it could go

It is a reading surface, not a claim. If it lands anywhere it belongs on
`twistjdotcom` beside the Czech exposition lane, or nowhere. It must not be
presented as TWIST-J content: the owner was explicit that this is standard
quantum mechanics seen from a different side, and the page says so in its own
eyebrow line.
