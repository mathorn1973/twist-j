# C-J-SINGER-MAHLER-LIFT-1-N result

```text
STATUS:       NON-CANONICAL candidate result
AUTHORITY:    NONE
SCOPE:        L1 CHARACTERISTIC-POLYNOMIAL ONLY
FROZEN PIN:   49ce4081e021171bc4c8c79a3fc7ffe4a496ea1a
PUBLIC BASIS: Public Canon v62
```

Let

\[
f_{a,b,c}(X)=X^4+aX^3+bX^2+cX+1,
\qquad
\tau=\varphi^2=\frac{3+\sqrt5}{2},
\]

and let admissibility mean no unit-circle root and exactly two roots outside
and two roots inside the unit circle.  The preregistered statement was

\[
J_{\min}(A_r):\quad M(f)\geq\tau,
\qquad M(f)=\tau\iff f=f_J,
\]

where

\[
f_J=X^4-3X^3+4X^2-2X+1=\Phi_5(X-1).
\]

## Frozen decisions

| Tier | Frozen condition beyond admissibility | Decision |
|---|---|---|
| A0 SINGER | reduction is either primitive quartic of order 15 | **false**: exact `F-LOWER` and `F-TIE` |
| A1 ORIENTED | reduction is `X^4+X^3+1` | **false**: exact `F-LOWER` and `F-TIE` |
| A2 TRACE | A1 and `a=-3` | **candidate-T**: global exact proof; unique equality is `f_J` |
| A3 DISPLACEMENT-UNIT | A2 and `f(1)=1` | **candidate-T**: corollary; direct square fingerprint |

No frozen threshold, class, coefficient window, or firing rule was changed
after the public preregistration pin.

## Exact failure of A0 and A1

The single polynomial

\[
h(X)=X^4-X^3+1
\]

lies in A1 and therefore in A0.  It has no real root, no unit-circle root,
and hence exactly one nonreal conjugate pair inside and one outside.  The
Landau bound is exact enough:

\[
M(h)\leq\sqrt{1^2+(-1)^2+1^2}=\sqrt3<\tau.
\]

Thus both lower-bound statements fail.  Uniqueness also fails independently:

\[
f_J(-X)=X^4+3X^3+4X^2+2X+1
\]

is a distinct A1 polynomial with the same root moduli and the same Mahler
measure as `f_J`.  The reciprocal polynomial

\[
X^4f_J(1/X)=X^4-2X^3+4X^2-3X+1
\]

gives the analogous tie in the other A0 parity branch.

## Global A2 theorem

For A2, `a=-3` and `b,c` are even.  Put

\[
E=f(1)=b+c-1,
\qquad A=f(-1)=b-c+5.
\]

Both are nonzero odd integers.  Admissibility forces them to have the same
sign.

The exterior resolvent of the six pair-products of the roots is

\[
G(Y)=Y^3H(Y+Y^{-1}),
\]

where

\[
H(Z)=Z^3-bZ^2+(ac-4)Z+(4b-a^2-c^2).
\]

If `E,A>0` and `M(f)<=tau`, the outside-root product is positive and the
corresponding resolvent root is `M+M^-1`.  The two cross-pair resolvent roots
give a positive remaining factor at `Z=3`, so

\[
M(f)\leq\tau\Longrightarrow H(3)\geq0.
\]

At `a=-3`,

\[
H(3)=6-5b-9c-c^2.
\]

Combining this with `E>0` and even parity forces

\[
c=-2,\qquad b=4.
\]

If instead `E,A<0`, the four roots are real, one in each of
`(-infinity,-1)`, `(-1,0)`, `(0,1)`, `(1,infinity)`.  Writing them as
`-Y,-v,u,X` gives

\[
3=X-Y+u-v<M-M^{-1},
\]

and therefore

\[
M>\frac{3+\sqrt{13}}2>\tau.
\]

Thus `f_J` is globally the only admissible A2 polynomial with measure at
most `tau`, and its measure is exactly `tau`.  The proof does not require the
finite coefficient window.

For A3, `b+c=2`, and the same resolvent specializes to

\[
H(3)=-(c+2)^2.
\]

The nonnegative requirement therefore gives `c=-2,b=4` directly.

## Frozen-window exact verification

The preregistered coefficient bounds remain independently verified:

```text
-10 <= a,c <= 10
-15 <= b   <= 15
```

The exact primary verifier checks all 165 A2 rows and all 11 A3 rows using
integer/rational Sturm and Routh certificates.  It finds:

```text
A2: 127 rows excluded by a resolvent root |z|>3;
     among 38 residual rows, outside counts are 29x3, 8x1, 1x2;
     the sole 2-out/2-in row is (b,c)=(4,-2).

A3: every row except (b,c)=(4,-2) has a resolvent root |z|>3.
```

An independent blind breaker, frozen before comparison with the builder,
classifies all 3300 A0 rows, 1650 A1 rows, 165 A2 rows, and 11 A3 rows with
exact rational root isolation.  Its A0/A1 witnesses differ from the primary
verifier's ordering, while its positive A2/A3 decisions agree.

## What the attack clarifies

1. A primitive order-15 binary Singer shadow is not an archimedean
   minimizer.  Even choosing the `p_R` orientation does not repair this.
2. Modulo two, sign is invisible.  The exact tie `f_J(-X)` shows this
   obstruction at equality, while `X^4-X^3+1` shows a strict lower failure.
3. The signed trace condition `a=-3` is the first sufficient selector in the
   frozen A0-A3 ladder.  It restores the unique Mahler fingerprint globally.
4. The displacement-unit condition `f(1)=1` is not needed for this Mahler
   rigidity.  It may retain a separate normalization role, but that role is
   not established here.

This does not make the binary residue a selector and does not contradict the
registered no-selection controls of `J-BINARY-NORM-DESCENT`,
`J-BINARY-NORM-INDEX`, or `CARRY-PENTAD`.

## Scope firewall

The result concerns characteristic polynomials only.  It proves no integral
matrix conjugacy classification, canonical basis, exponent selection,
decoder, dynamics, entropy, probability, Born rule, physical place, or
L2-L6 statement.
