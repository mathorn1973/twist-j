# Origin-zero nonlinear two-message readout on unchanged U

NON-CANONICAL / L1 / candidate-T proofs with a finite candidate-C audit.
Owner issue: [#1535](https://github.com/mathorn1973/twist-j/issues/1535).

## 0. Conventions and scope

All arithmetic is in F5. The native law is the Canon one, transcribed in
`verify.py` and cross-checked there against the Canon `(z,q,r)` quotient
table on all 15625 states: `x=(a,b,c,d,q,r)` is Canon
`(p1,p4,p1p,p4p,q,r)`, the generators are Canon `(a,b,c,d,e)` in this
order, the selector at counter `n` is `g_(z+2*theta_n)` with
`theta_n = popcount(n) mod 2` and `z` the sum of all six coordinates.
Write

```text
A = a+c,   C = a-c-2,   D = b-d-1,   z = a+b+c+d+q+r.
```

For `lam,mu in F5` prepare at counter `n=0`

```text
x0(lam,mu) = (3(lam+3), 3(mu+1), 3(-lam-1), 3(-mu-1), 0, 1).
```

Both messages are pre-loaded in this preparation (`C(x0)=lam`,
`D(x0)=mu`, section 1). Nothing is inserted later, no source clearing is
claimed, and preparation is admitted as an initial condition; its
production by a preceding native trajectory is not asserted. The readers
below are global coordinate readings of the full checkpoint, not a
transfer into a disjoint receiver block (section 6 makes the contrast
exact). No energy store, funded contact, physical instrument, occurrence
law or Canon claim is supplied.

## 1. The common prefix and the full reset

Direct substitution gives `A(x0)=1`, `C(x0)=lam`, `D(x0)=mu`, `z(x0)=2`.
The preparation is affine in the messages:
`x0(lam,mu) = x0(0,0) + lam*v_l + mu*v_m` with
`v_l=(3,0,2,0,0,0)`, `v_m=(0,3,0,2,0,0)`.

The first three selector bits are `theta_0,theta_1,theta_2 = 0,1,1`. With
`z(x0)=2` the first selected generator is `g2` (Canon `c`), and

```text
x1 = (3 lam, 3 mu, 2 lam+3, 2 mu+2, 1, 4),   z(x1)=0,   C(x1)=lam,
x2 = x0                                       (c applied twice),
x3 = (2 lam+3, 2 mu+3, 3 lam+1, 3 mu+2, 2, 0),  z(x3)=1,
```

where the step at `n=2` selects `g4` (Canon `e`), so `x3 = e(x0)`.
Also `A(x3)=4` and `D(x3)=4 mu`. These are formulas in `(lam,mu)`,
checked for all 25 pairs in the audit; the generator word `c,c,e` and the
full checkpoint reset `x2=x0` are common to all pairs.

## 2. The synchronized tail

Let `X14 = {z in {1,4}}`. On `X14` the selector admits only: at `z=1`,
`b` (bit 0) or `d` (bit 1); at `z=4`, `e` (bit 0) or `b` (bit 1). For
every state, the generator formulas give

```text
A:  b,d,e all send A to -A;
D:  b fixes D;  d,e send D to -D;
z:  b sends z to -z;  d fixes z=1;  e fixes z=4.
```

Hence `X14` is closed under both selector bits, `A` is negated at every
tail step, and `I(x) = zD/A` is invariant on `X14` wherever `A != 0`
(both cases negate exactly two of the three quantities `z`, `D`, `A`,
counting the fixed `D` under `b` against the two negations `z,A`).

The sector alone does not give `A != 0`: exactly 1250 states of `X14`
have `A=0`. The prepared trajectories give it: `A(x3)=4`, and negation
preserves nonvanishing, so `A in {1,4}`, `A^2=1`, at every `n>=3`. At
`n=3`, `I = 1 * (4 mu) / 4 = mu`; therefore `I = mu` for all `n>=3`,
under every continuation word, in particular the actual one.

The all-words closure of each `x3` in `X14` has exactly 20 states. Every
actual orbit point at `n>=3` lies in that closure by induction, and the
audit confirms the actual Thue-Morse word in fact visits all 20 (by
`n=32`). Together with the points at `n=0,1,2` this gives an exact
550-point required set: 25 blank points (the `x0`, repeated at `n=2`),
25 points at `n=1` labelled `lam`, and 500 tail points labelled `mu`.
No point carries two labels. Every statement below about "all times" is
a statement about this finite set plus the closure induction.

## 3. Two fixed readers

### 3.1 The author's piecewise reader

With `tau(z,A) = zA^3 + 1 - A^4` (so `tau = z/A` for `A != 0`, `tau = 1`
for `A=0`, and `tau != 0` for `z in {1,4}`), let

```text
T(x) = C            if z=0,
       q            if z=2,
       tau(z,A) * D if z in {1,4},
       D            if z=3,
R(x) = (z, T(x)).
```

On the prepared trajectories: `R(x0)=(2,0)`, `R(x1)=(0,lam)`,
`R(x2)=(2,0)`, and at every `n>=3`, `R(xn)=(z_n, mu)` with
`z_n in {1,4}`, because there `A != 0` and `tau*D = zD/A = mu`.
Decoding first coordinate `2` as BLANK and `0,1,4` as `PRESENT(t)` gives
`BLANK, PRESENT(lam), BLANK, PRESENT(mu), PRESENT(mu), ...` for all 25
pairs including zero messages. `T` is not affine. The pair `(z,T)`
extends to a bijective coordinate change of all of `F5^6`: with
`B=b+d`, the map `x -> (z, T, A, B, y5, y6)`, where `y5=D` if `z=0` else
`C`, and `y6=D` if `z=2` else `q`, is bijective (decode level by level;
on `z in {1,4}` recover `D=T/tau(z,A)`; then `r=z-A-B-q`). The audit
checks bijectivity on all 15625 states. The completion is piecewise in
`z` exactly as `T` is; it is the auditor's explicit completion, supplied
because the one-line sketch omits the `z=2` level, where the complement
must carry both `C` and `D`.

### 3.2 A single cubic polynomial reader

The piecewise form is not needed on this family. Let

```text
psi(x) = C*(1 - z^2) + A*z*D.
```

At `n=1`, `z=0` and `C=lam`, while `A*z*D=0`, so `psi=lam`. At every
tail point, `z^2=1`, so the first term vanishes, and
`A*z*D = A^2 * (zD/A) = mu` since `A^2=1` there. Blank is exactly `z=2`
on the required set. Hence `(z, psi)`, with `z` linear and `psi` a
polynomial of total degree 3, realizes the same six-label pattern with
decoder "BLANK iff `z=2`, else `PRESENT(psi)`". No division and no case
distinction remain.

## 4. The affine boundary: dimension exactly three

Claim: no affine map `F: F5^6 -> F5^k` with `k=1` or `k=2`, followed by
an arbitrary fixed decoder, realizes the required pattern on this
family; and an explicit affine map into `F5^3` separates all labels, so
the minimal affine receiver dimension is exactly 3.

Proof of impossibility. Write `alpha = M v_l`, `beta = M v_m` for the
linear part `M` of `F`. The linear part of generator `c` fixes both
`v_l` and `v_m`, and the linear part of `e` is `-I` (both checked in the
audit). Since `x1=c(x0)` and `x3=e(x0)` with a common word,

```text
F(x0) = u0 + alpha*lam + beta*mu,
F(x1) = u1 + alpha*lam + beta*mu,
F(x3) = u3 - alpha*lam - beta*mu.
```

If `alpha,beta` are linearly independent (needs `k=2`), then `F(x0)`
ranges over all of `F5^2`, so the decoder is BLANK everywhere,
contradicting `n=1`. Otherwise `alpha = a*e`, `beta = b*e` for one
vector `e`. At `n=1` the decoder, a function of `u1+(a*lam+b*mu)*e`,
must output `PRESENT(lam)`. If `b != 0`, the pairs `(0,0)` and
`(1, -a/b)` give the same reader value with different required labels;
hence `b=0`, i.e. `beta=0`, and `a != 0` or `F(x1)` is constant. But then
`F(x3)=u3-alpha*lam` does not depend on `mu`, while the required label
at `n=3` is `PRESENT(mu)`: pairs `(0,0)` and `(0,1)` collide. ∎

This does not contradict the origin-zero affine obstruction of
[#1520](https://github.com/mathorn1973/twist-j/pull/1520): that contract
required an exactly common affine receiver state at `n=2`, which is not
imposed or satisfied here; nor does it widen to affine maps into
`F5^k`, `k>=3`.

Sufficiency at dimension 3: the three linear forms

```text
f1 = 2b + d,   f2 = 3a + q,   f3 = 2a + 3b + r
```

(coordinate `c` ignored) take no common value on two required points
with different labels; the audit checks all 550 points (125 distinct
images). The decoder at dimension 3 is therefore a table on the image.
That is the precise tradeoff: affine needs three coordinates plus an
arbitrary table; two coordinates suffice only nonlinearly (section 3).

## 5. Quadratic polynomials inside two named codes

Inside the code of section 3.2 (marker `z`, message polynomial required
to equal the message on every present point), and inside the pair code
`(marker,msg)` = `(0,0)` on blank points and `(1,k)` on `PRESENT(k)`
points, exact linear algebra over F5 on the required set gives: no
polynomial of total degree at most 2 fits the message coordinate in
either code (the marker coordinate of the pair code does fit at degree
2), and degree 3 fits both codes. This is a finite machine-checked
statement about these two codes only. A general quadratic pair into
`F5^2` with an arbitrary decoder is **open**; only the affine case
`degree 1` is excluded in full generality, by section 4.

## 6. Coordinate access: the receiver block does not suffice

A clock-free reader that is a function of a fixed coordinate subset `S`
realizes the pattern if and only if no two required points agree on `S`
with different labels (necessity is immediate; sufficiency by arbitrary
extension off the required set). Exhaustion over all 64 subsets gives
exactly the consistent sets

```text
{a,b,c,q,r}, {a,b,d,q,r}, {a,c,d,q,r}, {b,c,d,q,r}, {a,b,c,d,q,r}:
```

`q` and `r` are both indispensable, at least three of the four piston
coordinates are necessary, and no four-coordinate access works on this
family. In particular the canonical complementary receiver block
`(b,d,q,r)` fails already at actual time `n=1`:
`x1(0,0)=(0,0,3,2,1,4)` and `x1(1,0)=(3,0,0,2,1,4)` agree on
`(b,d,q,r)=(0,2,1,4)` but require `PRESENT(0)` and `PRESENT(1)`; at
`n=1` the first message still sits in the source coordinates `(a,c)`.
Every conflict used here is between points of the actual orbits
(section 2: the required set is exactly the visited set), so the
classification is a statement about the actual `U` word, not only about
all continuation words.

Scope of section 6: this preparation family. A different family with a
common receiver block at `n=0`, of the shape of the canonical one-shot
transfer, is a separate question and is not decided here.

## 7. What this is, and is not

This is an existence statement for a native reading: one fixed,
clock-free, nonlinear (indeed cubic-polynomial) readout of actual `U`
trajectories displays a two-message BLANK/PRESENT pattern with a common
receiver *value* reset at `n=2`, from origin `n=0`, escaping the affine
scope of #1520 on two named axes at once: nonlinearity and global (as
opposed to receiver-block) access. Sections 4-6 show on this family
that neither relaxation can simply be dropped: two affine coordinates
never suffice (three are necessary and sufficient), and no
four-coordinate access suffices. It is not a funded contact, not a
later insertion or source-depletion result, not an energy or occurrence
statement, and not a uniqueness/forcing statement about admissible
readings. Which class of readings is physically admissible remains the
open question this example is meant to sharpen.
