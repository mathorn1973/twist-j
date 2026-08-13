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

Thus one critical-radius factor at `p^(-1/2)` splits on the phase double cover
into two parity factors at the quarter-power radius `+/- p^(-1/4)`.

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

The two factors `b_q` and `b_-q` are the even/odd (sign) pair on the double
cover. This is the local analytic counterpart of the delayed amplitude split
into symmetric and antisymmetric channels. The result does not make either
factor individually positive in the Weil sense; it only exhibits the exact
square-root carrier underlying the signed pair.

## 4. Boundary on zeta_8

No fixed eighth root is selected globally. The cover phase is the variable

```text
w=exp(i theta/2).
```

At the special base phase `z=i` (`theta=pi/2`), its square roots are precisely
odd eighth roots, e.g.

```text
w=exp(i pi/4)=zeta_8,
w^2=i.
```

Thus `sqrt(i)` is a distinguished **fiber value** of the universal half-phase
cover, not the globally fixed source of positivity. This matches the earlier
#355 non-uniqueness breaker while giving an exact reason for the appearance of
`zeta_8` whenever the underlying local phase equals `i`.

## 5. Why the square root, not an arbitrary m-th root

Algebraically one can generalize

```text
b_(q^m)(w^m)=product_(zeta^m=1) b_(q zeta)(w),
```

so an `m`-fold phase cover exists abstractly. The present attack singles out
`m=2` only because the frozen Weil object is a Hermitian **quadratic** form and
the prime weight enters as a norm square. The square-root layer is therefore
the minimal cover compatible with the quadratic/Pythagorean structure; the
algebra alone does not prohibit higher covers.

No Born, spin, metaplectic, or physical identification is claimed here.
