# C-J-SINGER-MAHLER-LIFT-1-N preregistration

Status: NON-CANONICAL incubation. No authority.
Owner: session c-j-singer-mahler-lift-1-n-20260825.
Basis: public main 48826848bb72b997648e2bd8156da840e90ec334,
Public Canon v62. This note changes no Canon claim, registry row, gate, or
dictionary.

## 1. Question

Let

```text
f_(a,b,c)(X) = X^4 + a X^3 + b X^2 + c X + 1,   a,b,c in Z,
f_J(X)       = X^4 - 3 X^3 + 4 X^2 - 2 X + 1
             = Phi_5(X - 1).
```

The companion matrix of every such `f` lies in `SL_4(Z)`. If `f mod 2`
is primitive of degree four, its companion reduction is an irreducible Singer
motor of exact order 15 in `GL_4(F_2)`.

For roots `alpha_1,...,alpha_4`, define the Mahler measure

```text
M(f) = product_i max(1, |alpha_i|).
```

The target has `M(f_J)=phi^2=(3+sqrt(5))/2` exactly.

The attack decides, at characteristic-polynomial scope only, whether `f_J`
is the unique Mahler-minimal hyperbolic two-outside/two-inside integral lift
in each of four classes frozen below.

## 2. Frozen classes

In every class, `f` must have no root on the unit circle and must have
exactly two roots, counted with multiplicity, in `|z|>1` and two in
`|z|<1`.

Let

```text
p_L = X^4 + X + 1,
p_R = X^4 + X^3 + 1.
```

These are the two primitive monic quartics over `F_2`.

```text
A0 SINGER:
   f mod 2 is p_L or p_R.

A1 ORIENTED:
   f mod 2 is p_R, the reduction of f_J.

A2 TRACE:
   f is in A1 and a = -3, equivalently Tr(C_f) = 3.

A3 DISPLACEMENT-UNIT:
   f is in A2 and f(1) = 1, equivalently det(I - C_f) = 1.
```

The nesting `A3 subset A2 subset A1 subset A0` is frozen before any
enumeration. No further rescuing condition may be added after a result.

## 3. Frozen decisions

For `r=0,1,2,3`, define `J_MIN(A_r)` to mean

```text
for every f in A_r, M(f) >= phi^2,
and equality holds only for f = f_J.
```

The decision order is A0, A1, A2, A3, but every tier is decided independently.

A tier fires negative immediately if either exact witness is certified:

```text
F-LOWER:  f in A_r and M(f) < phi^2;
F-TIE:    f in A_r, f != f_J, and M(f) = phi^2.
```

A tier passes positively only after a complete exact enumeration of every
`f` in that tier with `M(f) <= phi^2`.

## 4. Exhaustive finite window

For a monic quartic with `M(f) <= phi^2`, the coefficient bound

```text
|coefficient_k| <= binom(4,k) M(f)
```

gives exactly the sufficient integer window

```text
-10 <= a,c <= 10,
-15 <= b   <= 15,
```

because `4 phi^2 = 6 + 2 sqrt(5) < 11` and
`6 phi^2 = 9 + 3 sqrt(5) < 16`.

A positive decision outside this complete window is forbidden. A negative
witness need not use enumeration once its exact certificate is complete.

## 5. Exact certificate requirements

Floating point, numerical roots, and plotting are reconnaissance only and
never decide a tier.

Every accepted negative witness must certify, with exact integer, rational, or
algebraic inequalities:

1. the frozen coefficient and parity conditions;
2. primitivity and exact order 15 of the reduction;
3. absence of unit-circle roots;
4. the two-outside/two-inside root count;
5. the strict Mahler comparison, or exact equality, against `phi^2`.

Allowed exact routes include a written Rouché argument on a circle with
algebraic radius, an exact Schur-Cohn or resultant certificate, rational root
isolation with proved signs, and exact algebraic-number comparison.

A positive tier additionally requires an exact complete certificate for every
polynomial in the finite window, not merely a numerical scan.

## 6. Controls

The verifier or written proof must check:

```text
f_J mod 2 = p_R,
Tr(C_(f_J)) = 3,
f_J(1) = 1,
M(f_J) = phi^2,
p_L and p_R are irreducible and their root classes have exact order 15.
```

The target is a control, not an assumed minimum.

## 7. Independent breaker

The breaker is written from this frozen preregistration without reading the
builder's search or verifier. It must freeze its own code before witness
comparison. Running builder code is reproduction only.

## 8. Scope and status ceiling

This is exact L1 algebra only. It classifies characteristic polynomials and
does not classify integral conjugacy classes, ideal classes, marked lifts,
the axiom exponent, a physical characteristic-two place, a decoder, Born
registration, an apparatus, a measure, spacetime, an SI bridge, or any L2-L6
reading.

An exact negative witness may be recorded as candidate-T for the corresponding
minimality negation. A complete exact positive classification may be
candidate-T. A finite or numerical scan without a complete certificate is at
most candidate-C. Any interpretive statement about why Nature selects a tier
is at most candidate-D.

No result changes Public Canon v62 without a separate public probe and fold.
