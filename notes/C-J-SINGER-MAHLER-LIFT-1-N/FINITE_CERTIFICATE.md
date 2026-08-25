# C-J-SINGER-MAHLER-LIFT-1-N builder report

Status: NON-CANONICAL incubation. No authority.

Basis: public preregistration pin
`49ce4081e021171bc4c8c79a3fc7ffe4a496ea1a`, Public Canon v62.

Scope: exact L1 characteristic-polynomial algebra only.

## Decision summary

Let

```text
R = phi^2 = (3 + sqrt(5))/2.
```

| Tier | Decision | Exact certificate |
|---|---|---|
| A0 SINGER | `J_MIN(A0)` is false | `F-LOWER`: `(a,b,c)=(-2,0,1)` |
| A1 ORIENTED | `J_MIN(A1)` is false | `F-LOWER`: `(a,b,c)=(-1,0,0)` |
| A2 TRACE | `J_MIN(A2)` is true | complete exact enumeration of 165 coefficient triples |
| A3 DISPLACEMENT-UNIT | `J_MIN(A3)` is true | complete exact enumeration of 11 coefficient triples |

Each result meets the preregistered `candidate-T` ceiling. Nothing in this
report changes a public claim.

Numerical reconnaissance identified the following lexicographically first
records in the frozen window. The witnesses themselves are certified exactly
below.

```text
A0 first F-LOWER:  (-2, 0,  1)
A0 first non-J tie:(-2, 4, -3)
A1 first F-LOWER:  (-1, 0,  0)
A1 first non-J tie:( 3, 4,  2)
A2 lower/tie:      none except f_J itself at equality
A3 lower/tie:      none except f_J itself at equality
```

The numerical scan found 20 A0 and 10 A1 polynomials with apparent
`M(f) <= R`. It was used only to order the negative witnesses. The A0 and A1
decisions do not rely on completeness of that scan.

## 1. Complete coefficient window

For a monic quartic with `M(f) <= R`, the standard coefficient bound gives

```text
|a|, |c| <= 4R,
|b|      <= 6R.
```

The strict endpoint inequalities are exact:

```text
4R = 6 + 2 sqrt(5) < 11, because 20 < 25,
6R = 9 + 3 sqrt(5) < 16, because 45 < 49.
```

Thus the preregistered integer window

```text
-10 <= a,c <= 10,
-15 <= b   <= 15
```

contains every possible polynomial with `M(f) <= R`. In A2, parity reduces
this to

```text
a=-3,
b in {-14,-12,...,14},
c in {-10,-8,...,10},
```

which is exactly `15*11=165` triples. In A3, `c=2-b` leaves exactly 11
triples, with `b=-8,-6,...,12`.

## 2. Primitive reductions

Use bit polynomials over `F_2`:

```text
p_L = 0b10011 = X^4 + X + 1,
p_R = 0b11001 = X^4 + X^3 + 1.
```

For both moduli the exact modular checks are

```text
X^16 mod p = X,
gcd(X^4-X,p) = 1,
X^15 mod p = 1,
X^5 mod p != 1,
X^3 mod p != 1.
```

The first two checks prove irreducibility in degree four. The last three prove
that a root has exact multiplicative order 15. Thus either permitted parity
pattern gives the required Singer motor.

## 3. Compound polynomial and exact Mahler comparison

Let the four roots of

```text
f(X)=X^4+aX^3+bX^2+cX+1
```

be `alpha_i`. The six pair products are the roots of

```text
P(Y) = product_(i<j) (Y-alpha_i alpha_j)
     = Y^6 - bY^5 + (ac-1)Y^4 + (2b-a^2-c^2)Y^3
       + (ac-1)Y^2 - bY + 1.
```

This reciprocal sextic satisfies

```text
P(Y)/Y^3 = Q(Y+Y^-1),

Q(Z) = Z^3 - bZ^2 + (ac-4)Z + (4b-a^2-c^2).
```

If `f` has exactly two roots outside and two roots inside the unit circle,
then the product of the two outside roots has modulus `M(f)`. Every cross
product has strictly smaller modulus, and the inside pair has modulus below
one. Therefore

```text
M(f) = spectral_radius(P).
```

Since

```text
R + R^-1 = 3,
```

any real root `z` of `Q` with `|z|>3` yields a reciprocal pair of roots of
`P`, one having modulus strictly larger than `R`. Hence, conditionally on the
frozen two-outside/two-inside hypothesis,

```text
Q has a real root with |z|>3  implies  M(f)>R.
```

This is the exclusion certificate used in the complete A2 and A3 scans.
Sturm sequences over `Q` count the roots in `(-infinity,-3)` and
`(3,infinity)`. Roots exactly at `-3` or `3` are removed before the two open
interval counts.

## 4. Exact unit-circle and root-count certificate

Set

```text
w=(X-1)/(X+1),
X=(1+w)/(1-w).
```

Then `|X|>1` is equivalent to `Re(w)>0`. The transformed polynomial is

```text
H(w)=(1-w)^4 f((1+w)/(1-w))
    =(2-a+b-c)w^4 + 2(c-a)w^3 + (12-2b)w^2
      + 2(a-c)w + (2+a+b+c).
```

For every Routh certificate used below, the complete first column is nonzero,
neither `f(1)` nor `f(-1)` vanishes, and no auxiliary row vanishes. Therefore
there is no root on the imaginary axis for `H`, equivalently no root on the
unit circle for `f`. The number of sign changes in the first column is exactly
the number of roots of `f` outside the unit circle.

## 5. A0 exact negative witnesses

### Strict witness

```text
f_0(X)=X^4-2X^3+X+1,
(a,b,c)=(-2,0,1).
```

Its parity is `p_L`. Its exact Routh first column is

```text
(3, 6, 15, -32/5, 1).
```

There are two sign changes, so `f_0` is unit-circle-free and has exactly two
roots outside and two inside.

Its compound cubic factors as

```text
Q_0(Z)=Z^3-6Z-5=(Z+1)(Z^2-Z-5).
```

The roots are `-1` and `(1+-sqrt(21))/2`. Since `4<sqrt(21)<5`, two roots
lie in `[-2,2]` and the remaining root lies strictly in `(2,3)`. The first two
give unit-modulus roots of `P`; the last gives a reciprocal real pair whose
larger root is strictly below `R`. Therefore

```text
M(f_0)<R.
```

This exact `F-LOWER` certificate makes `J_MIN(A0)` false.

### Non-J equality witness

The first tie found by the reconnaissance ordering is

```text
f(X)=X^4-2X^3+4X^2-3X+1,
(a,b,c)=(-2,4,-3).
```

Its parity is `p_L`, its Routh first column is

```text
(11, -2, 15, 32/15, 1),
```

and its compound cubic is

```text
Q(Z)=(Z-3)(Z^2-Z-1).
```

The quadratic roots lie strictly in `(-2,2)`, while `Z=3` gives the pair
`R,R^-1`. Hence it is a second exact failure, this time `F-TIE`.

## 6. A1 exact negative witnesses

### Strict witness

```text
f_1(X)=X^4-X^3+1,
(a,b,c)=(-1,0,0).
```

Its parity is `p_R`. Its exact Routh first column is

```text
(3, 2, 15, -32/15, 1),
```

so it is unit-circle-free and has the required two-outside/two-inside split.
The compound cubic is

```text
Q_1(Z)=Z^3-4Z-1.
```

Its values at `-2,-1,0,2,3` are respectively

```text
-1, 2, -1, -1, 14.
```

There is one root in each of `(-2,-1)`, `(-1,0)`, and `(2,3)`. Since the
three disjoint intervals already contain three roots, this is the complete
root isolation. As in A0, it follows exactly that

```text
M(f_1)<R.
```

This exact `F-LOWER` certificate makes `J_MIN(A1)` false.

### Non-J equality witness

The first tie found by the reconnaissance ordering is

```text
f(X)=X^4+3X^3+4X^2+2X+1,
(a,b,c)=(3,4,2).
```

Its parity is `p_R`, its Routh first column is

```text
(1, -2, 5, 32/5, 11),
```

and its compound cubic is again

```text
Q(Z)=(Z-3)(Z^2-Z-1).
```

Thus it is an exact `F-TIE` witness in A1.

## 7. A2 complete exact classification

The exact loop covers all 165 coefficient triples in the complete window.
It splits them as follows.

```text
127: Q has a real root with |z|>3.
 38: Q has no real root with |z|>3.
```

The first 127 cannot have `M(f)<=R` if they satisfy the frozen hyperbolic
root split, by the compound lemma.

For each of the 38 residual triples, the exact Routh table is nondegenerate.
Their outside-root counts are

```text
29 have 3 roots outside,
 8 have 1 root outside,
 1 has 2 roots outside.
```

The sole two-outside residual is

```text
(b,c)=(4,-2),
f(X)=X^4-3X^3+4X^2-2X+1=f_J(X).
```

Its Routh first column is

```text
(11, 2, 15, -32/15, 1),
```

and

```text
Q_J(Z)=(Z-3)(Z^2-Z-1).
```

Consequently `M(f_J)=R`, and no other polynomial in A2 has measure at most
`R`. This proves `J_MIN(A2)` exactly and completely.

## 8. A3 complete exact classification

The 11 A3 rows `(b,c)` are

```text
(-8,10), (-6,8), (-4,6), (-2,4), (0,2), (2,0),
(4,-2), (6,-4), (8,-6), (10,-8), (12,-10).
```

Exact Sturm counts find a real root of `Q` with `|z|>3` for every row except
`(4,-2)`. The exception is exactly `f_J` and has `M(f_J)=R` as above. Thus
`J_MIN(A3)` is also proved exactly and completely, independently within its
own frozen coefficient list.

## 9. Reproduction

Run

```text
python3 exact_cert.py
```

The program uses only Python's standard-library `fractions` module. It uses no
floating point, numerical root finder, plotting package, or external computer
algebra system. A successful run ends with

```text
ALL EXACT ASSERTIONS PASS
```

The separate `recon.py` is numerical reconnaissance only and is not part of
any exact decision.
