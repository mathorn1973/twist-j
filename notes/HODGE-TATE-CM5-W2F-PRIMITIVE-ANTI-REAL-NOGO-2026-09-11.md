# Hodge-Tate CM5: W2F primitive anti-real theta no-go

**STATUS: NON-CANONICAL RESEARCH NOTE.**

**Basis:** Public Canon v84 and the companion Hodge-Tate / Markman / Perry CM5 notes through
`HODGE-TATE-CM5-PERRY-W2E-A-THETA-SYMMETRY-BREAKER-2026-09-11.md`.

**Date:** 2026-09-11.

This note carries out **Gate W2F**. The target was to replace the anti-real secant direction used in W2E-A by

\[
\gamma_f=v(sf),\qquad f\in\mathcal O_F=\mathbf Z[\varphi],
\qquad s=j-j^{-1},
\]

and to ask whether a different primitive direction admits a sufficiently large honest theta/Rouquier symmetry for Perry source-`H`-semiregularity while retaining integral descent of the codimension-three correction.

The verdict is negative for the whole **primitive anti-real family** in this implementation.

The result is stronger than a bounded search. The proof splits into:

1. exact formulas valid for every `f=m+n phi`;
2. an algebraic exclusion of every auxiliary odd prime `p != 5`;
3. finite exhaustive audits of the ramified `5`-channel;
4. a parity reduction of the `2`-channel;
5. one final exact `2`-adic audit for the unique numerically possible direction `f=phi`.

No `canon/` or registry file is changed. No algebraicity theorem is claimed. The result does **not** disprove Perry weak semiregularity of the final Markman object in a different invariant category, and it does not analyze nonprimitive rational scalings as new directions.

---

## 1. Primitive directions and scope

Write

\[
f=m+n\varphi,\qquad m,n\in\mathbf Z,
\]

and call the direction primitive when

\[
\gcd(m,n)=1.
\]

This is the natural scope of W2F. Multiplying `f` by an ordinary integer `d` multiplies the secant class linearly,

\[
\gamma_{df}=d\gamma_f,
\]

so it does not give a new projective secant direction in the four-dimensional rational secant space. Such multiples belong to the separate scale branch already exposed by W2D. They can change theta arithmetic, but they are not a new answer to the W2F design question.

We impose the usual positivity condition on the divisor part. Directions failing positivity are discarded before any semiregularity question.

---

## 2. Exact universal formulas

Put

\[
F=\mathbf Q(\sqrt5),\qquad
D=A+B,\qquad E=\sqrt5(A-B),
\]

with

\[
A^3=B^3=0.
\]

For

\[
f=m+n\varphi
\]

the degree-two part of

\[
\delta_f:=-\gamma_f
\]

is

\[
\boxed{
L_f
=5(m+2n)D+(-m+2n)E.
}
\]

Define the two integral quadratic forms

\[
\boxed{
S=m^2+2mn+2n^2=(m+n)^2+n^2,
}
\]

and

\[
\boxed{
T=m^2+6mn+4n^2.
}
\]

The two real coefficients of `L_f` are

\[
5(m+2n)\pm(-m+2n)\sqrt5.
\]

Their product is

\[
\boxed{20T.}
\]

Thus positivity is equivalent to

\[
m+2n>0,\qquad T>0.
\]

The half-polarization

\[
M_f:=L_f/2
\]

is integral for every `m,n`. On each abelian-surface factor its real-multiplication norm is `5T`, hence

\[
\boxed{
h^0(M_f)=25T^2,
\qquad
h^0(L_f)=400T^2.
}
\]

The secant self-Euler characteristic is

\[
\boxed{
\chi(\delta_f,\delta_f)=800S.
}
\]

All of these formulas are exact.

---

## 3. The general correction class

The divisor-supported half-twist ansatz has correction

\[
Q_f:=\frac1{24}L_f^3-(\delta_f)_6.
\]

It always contains the same norm-form factor:

\[
\boxed{
Q_f=(5D^2-E^2)(u_fD+v_fE),
}
\]

where

\[
\boxed{
 u_f=
 \frac{
 5m^3+40m^2n+80mn^2+3m+40n^3+4n
 }8,
}
\]

and

\[
\boxed{
 v_f=
 -\frac{
 m^3+4m^2n-8mn^2-m-8n^3
 }8.
}
\]

Although `u_f,v_f` can be half-integral, the resulting six-form `Q_f` is integral. In the fixed CM5 integral cohomology basis its coefficients are all divisible by `5`.

The Markman `BB_1` and `BB_0` non-vanishing conditions remain nonzero for every nonzero `f`: the adjacent coefficient contains

\[
st\,f\bar f=-\sqrt5\,N_{F/\mathbf Q}(f),
\]

and the complementary coefficient is a positive real combination of the two conjugate squares. Thus W2F is not losing candidates through the Weil projection. The issue is entirely theta descent versus invariant deformation dimension.

---

## 4. Perry's necessary size bound for general f

Let `H` be an honest finite isotropic theta/Rouquier translation subgroup through which the divisor-supported source sheaf and its correction descend. Write

\[
h=|H|.
\]

The theta representation gives an `H`-eigenspace of support sections of dimension

\[
\frac{h^0(L_f)}h=\frac{400T^2}{h}.
\]

As in W2E-A, the eight standard translation/Picard directions remain. Hence

\[
e_1^H
:=\dim\operatorname{Ext}^1(G_f,G_f)^H
\ge
7+\frac{400T^2}{h}.
\]

For a free nonzero translation the equivariant Lefschetz term vanishes, so averaging gives

\[
\chi(G_f,G_f)^H=\frac{800S}{h}.
\]

Simplicity and Serre duality therefore imply

\[
\boxed{
 e_2^H
 \ge
 12+\frac{800(S+T^2)}h.
}
\]

The source fourfold has

\[
\dim HH_{-2}(X)=28.
\]

Consequently a necessary condition for Perry source-`H`-semiregularity is

\[
12+\frac{800(S+T^2)}h\le28,
\]

or

\[
\boxed{
 h\ge 50(S+T^2).
}
\]

Call this number the **Perry threshold**.

---

## 5. Auxiliary odd primes cannot help

This is the main analytic simplification of W2F.

Work over a residue field of odd characteristic

\[
p\ne5.
\]

Over a quadratic extension if necessary, write

\[
r=\sqrt5,
\qquad
q=\frac{5+r}{2},
\qquad
q'=\frac{5-r}{2}.
\]

Let `f'` be the conjugate of `f` and set

\[
x=qf-rf',
\qquad
y=rf+q'f'.
\]

Then

\[
L_f=2xA+2yB
\]

and

\[
\boxed{xy=5T.}
\]

Suppose an odd prime

\[
p\ne5
\]

divides `T`. For primitive `(m,n)`, `x` and `y` cannot both vanish modulo `p`, because that would force both `m` and `n` to vanish modulo `p`. Thus exactly one of `x,y` vanishes.

The correction in the `A,B` basis is

\[
Q_f
=(x^2y+c)A^2B+(xy^2+d)AB^2,
\]

with

\[
c=r(qf+rf'),
\qquad
d=r(rf-q'f').
\]

If `x=0`, then `qf=rf'`, hence

\[
c=10f'\ne0\pmod p.
\]

The kernel of `L_f` is the `A`-carrier. For every nonzero `h` in that kernel,

\[
i_hQ_f
\]

contains the nonzero term

\[
c\,(i_hA)AB.
\]

Since `A` is symplectic on its four-dimensional carrier, the map

\[
h\mapsto(i_hA)A
\]

is injective. Therefore

\[
i_hQ_f\ne0.
\]

The case `y=0` is conjugate; there `d` is nonzero and the same conclusion holds.

Thus:

\[
\boxed{
 p\ne2,5,\ p\mid T
 \quad\Longrightarrow\quad
 \text{no nonzero }p\text{-translation in }K(L_f)
 \text{ is compatible with integral descent of }Q_f.
}
\]

So **no auxiliary odd prime can contribute to the Perry symmetry group** in this divisor-supported anti-real family.

This removes the apparent escape through examples such as `T=11`, `29`, `19`, and so on without enumerating any of their theta subgroups.

---

## 6. Generic five-primary branch

Modulo `5`, put

\[
c_E:=-m+2n.
\]

First suppose

\[
c_E\not\equiv0\pmod5.
\]

Then the five-primary kernel has dimension four over `F_5`, exactly as in W2E-A. Its symplectic form is the same fixed form up to a nonzero scalar. Hence it has exactly

\[
\boxed{156}
\]

Lagrangian planes.

Because `Q_f` is divisible by `5`, every single order-five translation passes the first integrality test. A rank-two subgroup requires the double contraction

\[
i_{h_2}i_{h_1}(Q_f/5)
\]

to vanish modulo `5`.

The condition depends only on `(m,n) mod 5`. There are exactly twenty nonzero residue classes with

\[
-m+2n\not\equiv0\pmod5.
\]

The companion verifier exhausts all

\[
20\times156=3120
\]

cases and finds

\[
\boxed{0}
\]

compatible rank-two five-primary Lagrangians.

Therefore in the generic branch

\[
\boxed{|H_5|\le5.}
\]

---

## 7. Exceptional five-primary branch

Now suppose

\[
-m+2n\equiv0\pmod5.
\]

For a primitive pair `(m,n)`, write

\[
m=2n+5k.
\]

Then

\[
T=5(5k^2+10kn+4n^2).
\]

Primitivity implies `5 does not divide n`, so the parenthesis is nonzero modulo `5`. Hence

\[
\boxed{v_5(T)=1.}
\]

The five-primary kernel is now the full eight-dimensional symplectic space over `F_5`.

It is enough to use the residue representative

\[
(m,n)=(2,1),
\]

because the other nonzero exceptional residues scale the relevant form by a nonzero scalar.

Put

\[
\overline Q=Q_{2+\varphi}/5\pmod5.
\]

Consider the double-contraction map

\[
C_2:\Lambda^2\mathbf F_5^8
\longrightarrow
\Lambda^4(\mathbf F_5^8)^*,
\qquad
u\mapsto i_\nu\overline Q.
\]

The exact finite calculation gives

\[
\boxed{\operatorname{rank}C_2=23,}
\]

so its kernel has dimension five.

Among its projective nonzero elements exactly

\[
\boxed{156}
\]

are decomposable bivectors. They define 156 two-planes, and every one is isotropic for the five-primary theta pairing.

However, for each such compatible two-plane `P`, the simultaneous extension space

\[
\{w:\ i_wi_u\overline Q=i_wi_v\overline Q=0
\text{ for a basis }u,v\text{ of }P\}
\]

has dimension exactly two. It is just `P` itself.

Hence **no compatible three-dimensional five-primary subgroup exists**.

Therefore in the exceptional branch

\[
\boxed{|H_5|\le25.}
\]

This is an exact finite statement, not a random search.

---

## 8. Primitive two-primary size

Primitivity makes the two-primary arithmetic especially rigid.

If `m` is odd, then

\[
T=m^2+6mn+4n^2\equiv1\pmod2,
\]

so the two-primary part of a maximal isotropic theta subgroup has order at most

\[
\boxed{16.}
\]

If `m` is even, primitivity forces `n` odd. Write

\[
m=2k.
\]

Then

\[
T=4(k^2+3kn+n^2).
\]

The parenthesis is always odd, so

\[
\boxed{v_2(T)=2}
\]

and the two-primary isotropic order is at most

\[
\boxed{256.}
\]

These are upper bounds; descent can only reduce them.

---

## 9. Global size exclusion: all cases except one

By Section 5, no odd prime other than `5` contributes at all. Combine the preceding local bounds with the Perry threshold.

### 9.1 `m` odd, generic five-branch

Here

\[
|H|\le16\cdot5=80.
\]

But

\[
S\ge1,
\qquad T^2\ge1,
\]

so

\[
50(S+T^2)\ge100.
\]

Hence this case fails.

### 9.2 `m` odd, exceptional five-branch

Now

\[
|H|\le16\cdot25=400.
\]

The exceptional congruence forces `5|T`, so `T>=5` under positivity. Therefore

\[
50(S+T^2)>1250>400.
\]

Hence this case fails.

### 9.3 `m` even, exceptional five-branch

Here

\[
|H|\le256\cdot25=6400.
\]

The exceptional congruence and `v_2(T)=2` imply

\[
T\ge20.
\]

Thus

\[
50(S+T^2)>20000>6400.
\]

Hence this case fails.

### 9.4 `m` even, generic five-branch

Write

\[
T=4U,
\qquad U\text{ positive odd}.
\]

The raw local upper bound is

\[
|H|\le256\cdot5=1280.
\]

If

\[
U\ge3,
\]

then `T>=12`, so

\[
50(S+T^2)>7200>1280.
\]

The only possible numerical window is therefore

\[
U=1,
\qquad T=4.
\]

Even then the threshold can fit under `1280` only if

\[
S\le9.
\]

Since

\[
S=(m+n)^2+n^2,
\]

this is a finite exact Diophantine check. Under primitivity, positivity, `m` even, `n` odd, `T=4`, and `S<=9`, the unique solution is

\[
\boxed{(m,n)=(0,1),}
\]

that is,

\[
\boxed{f=\varphi.}
\]

So the entire primitive family has reduced to one last candidate.

---

## 10. The last candidate `f=phi`

For

\[
f=\varphi
\]

one has

\[
S=2,
\qquad T=4.
\]

The Perry threshold is

\[
\boxed{50(S+T^2)=900.}
\]

The polarization has type

\[
\boxed{(4,4,20,20),}
\]

so its two-primary theta module is

\[
K(L_\varphi)_2\simeq(\mathbf Z/4)^8.
\]

The generic five-primary bound remains

\[
|H_5|\le5.
\]

It remains to determine how much of the apparent order-256 two-primary symmetry survives correction descent.

The correction `Q_phi` is divisible by `4`. Put

\[
\overline Q_2:=Q_\varphi/4\pmod2.
\]

### 10.1 Independent order-four generators

For two order-four translations, reduction modulo two gives a decomposable bivector in

\[
\Lambda^2\mathbf F_2^8.
\]

Descent requires it to lie in the kernel of

\[
C_2^{(2)}:\Lambda^2\mathbf F_2^8
\to\Lambda^4(\mathbf F_2^8)^*.
\]

Exact computation gives

\[
\boxed{\operatorname{rank}C_2^{(2)}=27.}
\]

Thus the kernel is one-dimensional. Its unique nonzero bivector has skew-matrix rank eight, so it is **not decomposable**.

Therefore no two independent order-four generators can coexist in a descent-compatible subgroup.

If

\[
H_2\simeq(\mathbf Z/4)^a\oplus(\mathbf Z/2)^b,
\]

then

\[
\boxed{a\le1.}
\]

### 10.2 Order-two rank

For three order-two translations the necessary condition is vanishing of the triple contraction of `Q_phi/4 mod 2`.

The map

\[
C_3^{(2)}:\Lambda^3\mathbf F_2^8
\to\Lambda^3(\mathbf F_2^8)^*
\]

has

\[
\boxed{\operatorname{rank}C_3^{(2)}=48.}
\]

The companion verifier exhausts all

\[
\boxed{97155}
\]

three-dimensional subspaces of `F_2^8` and finds

\[
\boxed{0}
\]

on which the triple contraction vanishes.

Hence

\[
\boxed{a+b\le2.}
\]

It follows that

\[
\log_2|H_2|=2a+b=a+(a+b)\le3,
\]

so

\[
\boxed{|H_2|\le8.}
\]

Combining with the five-primary line,

\[
\boxed{|H|\le8\cdot5=40.}
\]

But the Perry threshold is `900`.

Therefore the final candidate also fails by a factor greater than twenty.

---

## 11. W2F theorem

Combining Sections 5 through 10 gives:

> **Primitive anti-real W2F no-go.**  Let
> \[
> f=m+n\varphi\in\mathcal O_F
> \]
> be primitive, nonzero, and such that `L_f` is positive. Consider the divisor-supported secant construction with correction `Q_f`, together with an honest finite isotropic theta/Rouquier translation symmetry as in W2E-A. Then no correction-compatible subgroup `H` can reach the necessary Perry source-`H`-semiregularity threshold
> \[
> |H|\ge50(S+T^2).
> \]

Equivalently,

\[
\boxed{
\text{W2F closes FAIL for every primitive anti-real secant direction in the honest theta/Rouquier source-}H\text{ implementation.}
}
\]

This is not a bounded coefficient search. The only exhaustive finite searches are over fixed finite residue spaces at `p=5` and the unique final `p=2` candidate.

---

## 12. What is not ruled out

The theorem is deliberately scoped. It does **not** rule out:

1. nonprimitive integer scalings `df`, which are not new projective secant directions and belong to the separate scale problem;
2. a coherent realization not governed by the divisor-plus-correction geometry used here;
3. a genuinely twisted or non-isotropic finite Rouquier action;
4. direct weak `H`-semiregularity of the final Markman outer object in Perry's invariant category, without source `H`-semiregularity;
5. leaving the anti-real family `v(sf)` entirely and choosing a more general rational secant vector in `B ~=_Q K`.

The fifth item is now particularly natural. W2F shows that multiplying the native anti-real generator by the full real quadratic ring does not repair the theta-descent mismatch.

---

## 13. Correct next gate

The useful next fork is no longer another search over `f in O_F`.

### W2G-A: full rational secant search

Use

\[
\mathcal B\simeq_\mathbf Q K
\]

and search a general trace-zero rational secant vector

\[
v(a),\qquad a\in K,
\qquad\operatorname{Tr}_{K/\mathbf Q}(a)=0,
\]

not restricted to the one-dimensional `F`-multiple family `a=sf`.

The target is a class whose divisor and codimension-three correction admit a large common theta symmetry.

### W2G-B: Perry weak outer semiregularity

Stop requiring source `H`-semiregularity and compute the invariant obstruction category of the actual Markman outer object directly, using Perry's weaker theorem.

After W2F, this second route is arguably the more conceptually faithful one: all source failures found so far are caused by large geometric deformation spaces, whereas the target Weil projection itself remains robustly nonzero.

---

## 14. Reproduction

The companion exact verifier

```text
notes/HODGE-TATE-CM5-W2F-PRIMITIVE-ANTI-REAL-VERIFY.py
```

reproduces:

```text
generic five residue classes        20
generic five full planes passing     0
exceptional C2 rank                 23
exceptional compatible two-planes  156
exceptional three-plane extensions   0
phi C2 rank                         27
phi C2 kernel dimension              1
phi kernel bivector skew rank        8
phi C3 rank                         48
phi compatible three-planes          0
phi three-planes checked         97155
phi H2 upper bound                   8
phi total H upper bound             40
phi Perry threshold                900
```

All finite arithmetic is over integers, `Fraction`, `F_2`, or `F_5`. No floating point is used.

---

## 15. Verdict

W2F closes **FAIL** for the entire primitive anti-real family in the natural honest theta/Rouquier source-semiregularity implementation.

The failure mechanism is now completely localized:

```text
anti-real secant directions v(sf)
        |
        +-- auxiliary odd primes p != 5: contraction obstruction
        |
        +-- generic p=5: rank <= 1
        |
        +-- ramified exceptional p=5: rank <= 2
        |
        +-- primitive p=2 size: 16 or 256
                    |
                    +-- all cases dimensionally too small
                    +-- except f=phi
                              |
                              +-- exact 2-adic descent gives |H2| <= 8
                              +-- |H| <= 40 < 900
```

So the next useful work should change either the **secant direction beyond `sf`** or the **semiregularity notion beyond source `H`-semiregularity**. Repeating the same anti-real ring search cannot close the lane.