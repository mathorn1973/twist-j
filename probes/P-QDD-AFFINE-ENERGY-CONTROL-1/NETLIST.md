# Exact elementary realization of the two affine routing maps

**PUBLIC; candidate-T, L1, NON-CANONICAL.** This is the all-state
algebraic factorization for `P-QDD-AFFINE-ENERGY-CONTROL-1`, owned by
[#1089](https://github.com/mathorn1973/twist-j/issues/1089). It changes no
native law and makes no claim that the admitted elementary operations
are physically available. Scientific execution and public acceptance
are recorded separately.

The target maps are the two explicit affine checkpoint permutations in
[the accepted entrance routing](../P-QDD-ENTRANCE-NONLINEAR-RESOURCE-1/NATIVE-ROUTING.md).
The factorization below is literal on all of `F5^6`, not merely on the
four prepared code points. There is no additional coordinate, discarded
work state, measurement, or input-dependent choice of the instruction
list.

## 1. Operations and conventions

Write a checkpoint as `x=(a,b,c,d,q,r)`. All arithmetic in this document
is modulo five. Instructions execute from top to bottom, and every
right-hand side uses the current values immediately before that
instruction. A single instruction changes only its named target, except
for an explicitly named exchange.

The target-independent elementary family is:

| Operation | Action | Admitted parameters |
| --- | --- | --- |
| `SUM(i,j,k)` | `x_j <- x_j + k*x_i` | distinct coordinates `i,j`, `k in F5*` |
| `SCALE(i,k)` | `x_i <- k*x_i` | coordinate `i`, `k in F5*` |
| `SHIFT(i,k)` | `x_i <- x_i+k` | coordinate `i`, `k in F5` |
| `SWAP(i,j)` | exchange `x_i,x_j` | distinct coordinates `i,j` |

The family is defined independently of the entrance target. The
particular words selected below are target-specific members of that
family. Admitting the family is an additional mathematical premise;
writing these words does not derive the premise from `U`.

Every operation is a permutation of the complete checkpoint space.
Its inverse is respectively `SUM(i,j,-k)`, `SCALE(i,k^-1)`,
`SHIFT(i,-k)`, or the same `SWAP(i,j)`. Hence every listed prefix and
the complete word are bijective without needing a special input state.

## 2. Five instructions for A

The first accepted routing map is

```text
A(a,b,c,d,q,r) = (a,b,c,d,q+a+b+c+d+2,r).
```

Its chronological word is:

```text
A01  q += a
A02  q += b
A03  q += c
A04  q += d
A05  q += 2
```

The source coordinates remain unchanged at every instruction, so the
displayed formula follows by addition. The word has four `SUM`
operations and one `SHIFT`. Reversing their order and subtracting each
term gives the inverse on every checkpoint.

## 3. Nineteen instructions for B

The second accepted routing map is

```text
B(a,b,c,d,q,r) = (
  a+b+3c+r+3,
  3a+3c+3r,
  4a+2r+3,
  4a+2c+d+r,
  q+4c,
  3a+3c+4r+3
).
```

Its chronological word is:

```text
B01  q += 4*c
B02  d += 4*a
B03  d += 2*c
B04  d += r
B05  c += a
B06  c += r
B07  c *= 3
B08  b += 3*a
B09  b += c
B10  b += 3*r
B11  b += 3
B12  r += c
B13  r += 3
B14  a *= 4
B15  a += 2*r
B16  a += 3*c
B17  a += 2
B18  swap(a,b)
B19  swap(b,c)
```

No operation here is simultaneous with another. In particular `c` in
B09, B12 and B16 has already been changed by B05--B07, and `r` in B15
has already been changed by B12--B13. This use of current values is
essential to the factorization.

### Direct all-state proof

Denote the original checkpoint by
`(a0,b0,c0,d0,q0,r0)`, and denote the six desired components of
`B(a0,b0,c0,d0,q0,r0)` by `(B_a,B_b,B_c,B_d,B_q,B_r)`.

After B01--B04,

```text
q = q0+4c0                    = B_q,
d = d0+4a0+2c0+r0            = B_d.
```

These two coordinates are not touched again. After B05--B07,

```text
c = 3(c0+a0+r0)              = B_b.
```

The original `a0,r0` are still present at this stage. Thus B08--B11
produce

```text
b = b0+3a0+c+3r0+3
  = b0+6a0+3c0+6r0+3
  = a0+b0+3c0+r0+3          = B_a.
```

Next B12--B13 give

```text
r = r0+c+3
  = 3a0+3c0+4r0+3          = B_r.
```

Finally B14--B17 act on the still original `a0` and the current `r,c`:

```text
a = 4a0+2r+3c+2
  = 4a0+2(3a0+3c0+4r0+3)+3(3a0+3c0+3r0)+2
  = 19a0+15c0+17r0+8
  = 4a0+2r0+3              = B_c.
```

Consequently the checkpoint before the two exchanges is

```text
(a,b,c,d,q,r) = (B_c,B_a,B_b,B_d,B_q,B_r).
```

B18 and B19 respectively turn the first three entries into
`(B_a,B_c,B_b)` and `(B_a,B_b,B_c)`. This proves the claimed equality
on every input in `F5^6`.

### Explicit inverse

The elementary inverse word is obtained without solving any new
equations: traverse B19 through B01, use the same exchanges, negate
the additions, and replace the multipliers 4 and 3 by 4 and 2.
This proves that the factorization is a globally reversible realization
of the accepted map.

For a second direct description, let the output be
`(A0,B0,C0,D0,Q0,R0)`. Its unique input is recovered sequentially by

```text
r0 = R0-B0-3
a0 = 4(C0-3-2r0)
c0 = 2B0-a0-r0
b0 = A0-3-a0-3c0-r0
d0 = D0-4a0-2c0-r0
q0 = Q0-4c0.
```

Indeed the first equation is the difference between the sixth and
second output components. The third and second output components then
recover `a0` and `c0`, followed by the remaining coordinates. This
agrees with reversibility of the elementary word.

## 4. Exact operation accounting

The count treats a nonzero fixed-gain `SUM(i,j,k)` as one operation in
the explicitly declared family.

| Word | SUM | SCALE | SHIFT | SWAP | Total |
| --- | ---: | ---: | ---: | ---: | ---: |
| A | 4 | 0 | 1 | 0 | 5 |
| B | 12 | 2 | 3 | 2 | 19 |
| Both routing words | 16 | 2 | 4 | 2 | 24 |

Every `SUM(i,j,k)` is a power of the fixed unit-gain operation
`SUM(i,j,1)`, because its controlling coordinate is unchanged. With
the positive representatives `k=1,2,3,4`, replacing each gain by that
many repetitions gives 4 unit-gain additions for A and 26 for B.
This is an explicit optional expansion to 30 unit-gain additions, not
a minimality theorem. Inverses or a different generating family can
change the operation count.

All counts are discrete word lengths. They give neither a physical
duration nor an energetic cost. The two actual native ticks in the
accepted construction are separate from these routing instructions.

## 5. Coherent action and scope

On the formal complex vector space with basis `|x>` indexed by
`F5^6`, assign each elementary permutation its literal linear lift
`|x> -> |operation(x)>`, with coefficient `+1`. Every such lift is
unitary on this formal space. Their chronological products are exactly
the corresponding lifts of A and B on all amplitudes, including
states correlated with an untouched reference. There are no ancillary
outputs and no relative phases hidden by the pointwise notation.

This factorization can therefore replace A and B in the accepted
four-point entrance identity without changing its formal coherent
action. It does not supply a physical realization of the elementary
family, physical control or duration, or a global unitary interpretation
of the selected native maps. Those are separate questions. In
particular, mathematical reversibility of A and B is not a proof of
physical availability or of `feeds_U=false`.

## 6. A determinant boundary for native words

The factorization also gives the determinant of B's six-dimensional
linear part without a determinant expansion. Each `SUM` has determinant
one, each `SHIFT` has identity linear part, the two scales contribute
`3*4`, and the two exchanges contribute `(-1)^2`. Hence

```text
det(linear B) = 3*4*(-1)^2 = 2 in F5.
```

In contrast, each of the five declared native affine generators has
linear determinant one. Generator `a` exchanges two disjoint source
pairs. Generator `b` is minus the permutation exchanging two disjoint
source pairs and fixing the two port positions; the six minus signs
contribute one. For generator `c`, the source block is the same
four-dimensional negative permutation as in `b`, with determinant one;
its dependence on `r` lies above the port block, whose two diagonal
entries are `-1,-1`, so the full determinant is one. Generators `d,e`
both have linear part `-I_6`, again with determinant one. Translations
do not affect these linear determinants.

Consequently no fixed finite word in the native generators and their
inverses has B as its complete affine checkpoint map. Also, `SUM`,
`SHIFT` and `SWAP` alone have linear determinants in `{1,-1}` and cannot
produce this exact B without enlarging that family. This is a statement
about literal affine maps over `F5`, not about every circuit with
selected native steps, auxiliaries, different encodings or equality
only on a code. Nor is this finite-field determinant the determinant
of a physical unitary operator.
