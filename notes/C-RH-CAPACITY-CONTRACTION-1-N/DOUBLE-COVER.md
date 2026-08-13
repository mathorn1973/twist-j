# SQUARE-ROOT COVER OF THE LOCAL SCATTERING PHASE

```text
STATUS: candidate-T exact algebra; NON-CANONICAL
ISSUE:  #357
RH INPUT: none
```

## 1. Exact factorization

For a rational prime `p`, put

```text
r=p^(-1/2),
q=p^(-1/4),
r=q^2.
```

Let

```text
b_r(z)=(z-r)/(1-rz)
```

be the Blaschke factor found in the completed local prime channel. Pass to the
double cover of the boundary phase,

```text
z=w^2.
```

Then exactly

```text
b_r(w^2)
 = (w^2-q^2)/(1-q^2w^2)
 = [(w-q)/(1-qw)] [(w+q)/(1+qw)]
 = b_q(w)b_(-q)(w).
```

Thus one critical-radius factor at `p^(-1/2)` splits on the two-sheeted phase
cover into two factors at the quarter-power radius `+/-p^(-1/4)`.

## 2. Same statement at the Euler denominator

For any complex `s`, choose a square-root variable

```text
beta=p^(-s/2).
```

Then

```text
1-p^(-s)=(1-beta)(1+beta).
```

On the critical line `s=1/2+i xi`,

```text
|beta|=p^(-1/4),
arg beta=-(xi log p)/2.
```

Hence the quarter-power amplitude and the half phase are not independent
rewrites. They are respectively the modulus and argument of the single local
square-root variable `p^(-s/2)`.

## 3. Interpretation of the two factors

The two factors are exchanged by the deck involution, up to sign:

```text
b_q(-w)=-b_(-q)(w).
```

They are therefore a deck-conjugate sign pair, not individually even and odd
functions. An exact linear identification with the delayed symmetric and
antisymmetric feature channels has not been proved. The result does not make
either factor individually positive in the Weil sense.

## 4. Boundary on zeta_8

No fixed eighth root is selected globally. The cover phase is the variable

```text
w=exp(i theta/2).
```

At the special base phase `z=i` (`theta=pi/2`), its two square roots are

```text
w=zeta_8 or zeta_8^5,
w^2=i.
```

No sheet is privileged. Moreover the normalized Euler half-variable
`beta/|beta|`, for `beta=p^(-s/2)`, has phase `w^(-1)` in the convention above.
Over `z=i` it therefore gives a square root of `-i`, such as `zeta_8^(-1)`,
up to the other sheet. This orientation must be kept distinct from the cover
coordinate `w` and from the transform convention in #355. Neither eighth root
is a source of positivity.

## 5. Why the square root, not an arbitrary m-th root

For complex `alpha` use the standard Blaschke factor

```text
b_alpha(w)=(w-alpha)/(1-conj(alpha)w).
```

Then algebraically one can generalize

```text
b_(q^m)(w^m)=product_(zeta^m=1) b_(q zeta)(w),
```

so an `m`-fold phase cover exists abstractly. The frozen Weil object is a
Hermitian quadratic form and the prime weight enters as a norm square, which
motivates testing `m=2` first. This motivation does not prove that the double
cover is uniquely selected; the algebra alone does not prohibit higher covers.

No Born, spin, metaplectic, or physical identification is claimed here.
