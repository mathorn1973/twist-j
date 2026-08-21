# RECON-K4-W2-ORBIT-ISOSPECTRAL, 2026-08-11

NON-CANONICAL, no freeze, no result status. This is the structural route
paying off, and it changes what the overnight batch is for. Scripts
recon_k4_power_sums.py, recon_k4_isospectral.py and
recon_k4_w2_orbit_mechanism.py in the fleet handoff repo.

## The chain, in the order it came out

```text
p = 1, 2 must agree on any fiber pair, proved: F_109 carries the ten
  orbit sums, so all 55 trivial-sector quadratics are functions of it,
  and the other 99 invariant quadratics are its own coordinates. That is
  the whole 154-dimensional space of S_4-invariant quadratics, and Tr K,
  Tr K^2 are invariants of degree 1 and 2.
p = 3 to 6 agree too, on all 180 weight-2 fiber pairs tested. Not
  implied by the above, so something stronger is going on.
characteristic polynomials are IDENTICAL on 1512 of 1512 weight-2 fiber
  pairs, across all 252 patterns, several solutions each.
the mechanism: on all 1512, the second endpoint is an S_4 IMAGE of the
  first, y = g.x.
```

## The statement this suggests, and why it would close weight 2

If a weight-2 F_109 fiber pair is always an S_4 image pair, then
K(y) = P_g K(x) P_g^T with P_g a permutation matrix. Similar matrices
have identical characteristic polynomials, hence identical inertia. A
weight-2 fiber pair therefore cannot join (7,0,9) to (9,0,7) at all, and
the question is closed for the whole weight-2 class with NO search:

```text
|m| = 2 and F_109(v) = F_109(v xor m)
    =>  v xor m = g.v for some g in S_4
    =>  K(v xor m) similar to K(v)
    =>  identical spectrum, identical inertia
    =>  no weight-2 fiber pair joins the two profiles
```

This is far stronger than the inertia bound of the previous recon, which
closed only 18 patterns of 252. It closes all 252.

## The honest gaps, stated before anyone gets excited

FIRST, the orbit mechanism is EMPIRICAL at 1512 pairs. It is not proved.
The proof obligation is exactly: at weight 2, the fiber equations force
the table to be g-invariant off the transposed pair for a group element
g realizing that transposition. A candidate must derive that from the
equations, not observe it.

SECOND, 802 of the 1512 pairs satisfy the naive off-pair invariance test
as written; the other 710 are S_4 images under a group element whose
cell action is not a plain transposition of the two flipped cells, so
the test as coded is too narrow rather than the claim being false. The
right statement quantifies over the stabilizer structure and is part of
the proof obligation, not a defect of the finding.

THIRD, this is special to weight 2. The known weight-4 equal-F_109 pair
is NOT an S_4 image pair, its characteristic polynomials DIFFER, and yet
both endpoints carry inertia (7,0,9). So accidental fiber pairs, not
explained by symmetry, exist at weight 4. Everything above says nothing
about them.

FOURTH, and this is the boundary the owner already drew: even a proved
weight-2 no-go does not prove T-A. It proves T-A on the weight-2 mask
class. What generates the full fiber relation remains open, and the
weight-4 accidental pair is now the concrete evidence that the relation
is bigger than symmetry.

## What this does to the overnight batch

The 120 expensive open patterns, and the 114 cheap ones, exist to decide
by search exactly what this mechanism would decide by algebra. If the
proof obligation is discharged, the batch is unnecessary for weight 2 and
the machine should be pointed at weight 4 instead, where the accidental
pair proves symmetry is not the whole story.

Recommended order, for the owner: prove the weight-2 statement first, at
the cost of an hour of algebra rather than a night of compute; keep the
batch loaded but aimed at weight 4; and treat the weight-4 accidental
pair as the new central object, since it is the smallest thing we have
that the symmetry explanation does not cover.
