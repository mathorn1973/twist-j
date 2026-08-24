# WORKPACK K4-W4-FIBER-CENSUS
## a numerical task for the 80-core node, specified as mathematics

NON-CANONICAL incubation work. Nothing here promotes anything, and the
worker who executes it needs no TWIST-J context beyond this page. All
arithmetic is exact integer arithmetic. No floating point anywhere, and
no numerical eigenvalue routine anywhere, at any stage, for any purpose.

## 1. The objects

Cells. Let X = {0,1,2}^4 minus the binary face {0,1}^4. That is 65 cells,
fixed once in a frozen order. A TABLE is a sign assignment
v: X -> {+1,-1}, so a table is a point of {+1,-1}^65.

Operator. There are fixed 16 by 16 symmetric integer matrices K_0 and
M_j, one M_j per cell j, such that

```text
K(v) = K_0 + sum_j v_j M_j
```

K is LINEAR in the signs. This is the only property of K the task needs;
the matrices themselves come with the reference implementation.

Profile. P(v) = the inertia of K(v), written NEG/ZERO/POS, computed
exactly. Two profiles matter:

```text
P_plus  = (7, 0, 9)      P_minus = (9, 0, 7)
S_pm    = { v : P(v) in {P_plus, P_minus} }
```

Invariant map. F_109(v) is a fixed vector of 109 integers: ten orbit sums
of the signs over the ten S_4 orbits of cells, plus 78 + 15 + 6 Gram
entries of the standard, [22] and [211] isotypic data. It is
S_4-invariant and is a polynomial of degree at most 2 in the signs. Every
coordinate is an integer; equality is exact integer equality.

## 2. The exact fiber equations (this is what makes the task cheap)

Let a MASK be a set of cells to flip, and put m_j = v_j on the mask and 0
elsewhere. Flipping sends v to v - 2m. Every F_109 coordinate is
B(L_a(v), L_b(v)) for a linear map L_a and a symmetric bilinear form B
per sector, so bilinearity gives the exact criterion

```text
F_109(v) = F_109(v xor mask)
   <=>   sum_{j in O} m_j = 0                     for each of the 10 orbits
   and   B(L_a(v), L_b(m)) + B(L_a(m), L_b(v))
              = 2 B(L_a(m), L_b(m))               for each sector, a <= b
```

99 equations of the second kind, 10 balance conditions of the first. The
left side is LINEAR IN v. So for a FIXED mask and fixed signs on it, the
fiber condition is an inhomogeneous linear system in the table. Writing
v = 1 - 2z with z in {0,1}^65 makes it an integer system

```text
sum_j A_ij z_j = c_i,     c_i = (sum_j A_ij - rhs_i) / 2
```

with every c_i an integer (assert this, do not assume it). The z are
pinned on the mask by the mask's own signs. Solve exactly; never
approximately.

## 3. The pattern class for this task: weight 4

A SWAP is two cells in the SAME orbit carrying opposite signs; flipping
both preserves that orbit's sum. A weight-4 pattern is two disjoint
swaps. Enumerate them in a frozen order: all 252 weight-2 swaps in
ascending (orbit, cell, cell) order, then all unordered pairs of them
with four distinct cells.

```text
weight-2 patterns    252
weight-4 patterns  29478      <- the class of this task
```

Measured free-bit histogram (cells appearing in no equation, so free):

```text
free bits   1: 8972    2: 2916    3: 216    5: 15304
            6:  172    9:  252   19: 1646
total leaves if every solution set is enumerated: 863 639 144
```

So 27832 patterns are trivially exhaustible (at most 512 leaves each) and
1646 patterns carry 2^19 leaves each and hold 96 percent of the work.
Shard by pattern index; the shards are completely independent.

## 4. What to compute, per pattern

For each of the 29478 patterns:

1. Build the 99 equations, convert to the 0/1 form, assert integrality.
2. Enumerate the solution set V_m EXACTLY and completely where the free
   count allows, otherwise to a frozen node budget.
3. For each solution v, form the pair (v, v xor mask) and record:
   a. PROFILES: P(v) and P(v xor mask), each by TWO independent exact
      paths that must agree (fraction-free symmetric elimination, and the
      characteristic-polynomial sign count). A disagreement is a hard
      stop, not a result. Cheap safe pre-filter: both target profiles
      have an odd negative index, so both force det K < 0; a pair with
      det K >= 0 at either endpoint cannot be a target and may be skipped
      before the full inertia. This filter is provably safe and discards
      nothing reachable.
   b. OPPOSITE: whether {P(v), P(v xor mask)} = {P_plus, P_minus}. This
      is the falsifier. ONE such pair anywhere ends the question.
   c. SYMMETRY: whether v xor mask = g.v for some g in the 24-element
      S_4 action on cells. If yes the pair is SYMMETRY-EXPLAINED and its
      two operators are similar by a permutation matrix, hence
      isospectral. If no it is ACCIDENTAL.
   d. ISOSPECTRAL: whether the two characteristic polynomials are equal,
      as exact integer vectors.

## 5. What is actually being measured, and why

At weight 2 every fiber pair tested, 1512 of 1512 across all 252
patterns, turned out to be an S_4 image pair and therefore isospectral,
which forbids an opposite pair outright. Weight 4 is known to be
different: the pair

```text
0x4d21ed2f85b5c190   and   0x6d21ef0f8595c190
```

(cells numbered from bit 0; these are the sign words) has equal F_109, is
NOT an S_4 image, has DIFFERENT characteristic polynomials, and yet both
endpoints have profile (7,0,9). It is the smallest object we have that
symmetry does not explain, and it is the regression witness for this
task: any implementation must reproduce exactly those four facts.

The census therefore answers two questions at once:

```text
Q1  does any weight-4 fiber pair join (7,0,9) to (9,0,7)
Q2  what fraction of weight-4 fiber pairs is accidental rather than
    symmetry-explained, and are the accidental ones ever isospectral
```

Q1 is a falsification attempt with a one-witness threshold. Q2 is the
first real measurement of how much of the fiber relation is NOT group
symmetry, which is the structure the whole line now turns on.

## 6. Output contract

Per pattern, one record with: the four cells, the free-bit count, the
number of solutions enumerated, whether enumeration was complete,
counts of symmetry-explained, accidental, isospectral and opposite
pairs, and the explicit sign words of the first accidental pair and of
any opposite pair. One file per shard, SHA-256 of each shard file
recorded, and a final concatenation in shard order with its own SHA-256
so the whole census has a single pin.

Determinism is part of the deliverable: the same shard boundaries and the
same enumeration order must reproduce the same bytes on a rerun. Run with

```text
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
```

and no wall-clock, hostname or machine identifier anywhere in the output.

## 7. Cost

Roughly 8.6 . 10^8 leaves in the worst case, two exact 16 by 16 inertia
computations per leaf before the determinant filter and far fewer after
it. On one core that is days; on 80 cores with the filter it is a night.
The 27832 cheap patterns finish in minutes and can be reported first as a
complete partial census while the 1646 expensive ones run.

## 8. Three outcomes, and only these

```text
OPPOSITE-W4-FOUND    explicit mask and table, both profiles confirmed by
                     two exact paths. Falsifies the hypothesis that the
                     parent map decides the flow, globally, at once.
OPPOSITE-W4-EMPTY    every pattern completely enumerated, no opposite
                     pair. A statement about the weight-4 class only,
                     never about all masks.
INCOMPLETE           any pattern left at its budget. Nothing is
                     interpreted, in either direction.
```

A null result is merged, not hidden, and a fired falsifier is progress,
not failure.
