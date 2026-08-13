# PRIME HALF-ANGLE PARITY TRANSFORM AND THE SU(2) CENTRAL PHASE

```text
STATUS: candidate-T algebra inside NON-CANONICAL incubation
ISSUE:  #355
RH STATUS CHANGE: none
BORN/DECODER STATUS CHANGE: none
```

## 1. Two square-root phase copies

For one delayed prime leg with phase `theta=L xi`, the half-angle factorization naturally begins with the two conjugate square-root phase features

```text
E_+(t,xi)=e^(+i theta/2) phi_t(xi),
E_-(t,xi)=e^(-i theta/2) phi_t(xi),
```

where `phi_t(xi)=(e^(i xi t)-1)/xi`.

Their normalized even and odd quadratures are

```text
C_hat = (E_+ + E_-)/sqrt(2),
S_hat = (E_+ - E_-)/(i sqrt(2)).
```

The unnormalized versions are exactly the cosine and sine features used in `HALFANGLE-PRIME-KERNEL.md`.

## 2. The basis-change matrix

The change of basis is

```text
[ C_hat ]     1       [ 1   1 ] [ E_+ ]
[ S_hat ]  = -----    [ -i  i ] [ E_- ].
              sqrt(2)
```

Call this matrix `U`. Direct calculation gives

```text
U^* U = I,
det U = i.
```

Thus the parity/quadrature change is unitary but not special unitary.

## 3. Determinant-one lift forces an eighth-root central phase

A scalar phase `lambda` multiplies a `2 x 2` matrix determinant by `lambda^2`. The condition

```text
det(lambda U)=1
```

therefore requires

```text
lambda^2 = 1/i = -i.
```

Hence, up to the unavoidable central sign,

```text
lambda = zeta_8^(-1)
```

for `zeta_8=e^(i pi/4)` with `zeta_8^2=i`. Equivalently the conjugate eighth root supplies the unique determinant-one central correction up to `+/-1`:

```text
zeta_8^(-1) U in SU(2).
```

This is a precise mathematical appearance of the conjugate eighth-root
correction `sqrt(-i)=zeta_8^(-1)` in the half-angle prime-kernel
factorization. It is not the assertion that the chosen correction is
literally `sqrt(i)` in the displayed orientation.

## 4. Real-space reading

Under Fourier/Plancherel, multiplication by `e^(+/- iLxi/2)` translates the oriented interval feature by `+/- L/2`. Therefore `E_+` and `E_-` are the two half-shifted copies of the same interval amplitude, while `C_hat` and `S_hat` are their even and odd combinations.

The local indefinite prime kernel is the difference of the odd and even Gram sectors. The half-angle is therefore a parity split of two translated copies, not an arbitrary phase insertion.

## 5. Exact scope

What is forced:

```text
full phase e^(iLxi)
 -> conjugate half phases e^(+/- iLxi/2)
 -> unitary even/odd transform U with det U=i
 -> determinant-one lift requires a central square root of -i,
    namely +/-zeta_8^(-1) in the displayed orientation.
```

What is **not** forced:

- a fixed `zeta_8` value of the variable half phase `e^(iLxi/2)`;
- RH or positivity;
- a global contraction between the positive and negative source-side sectors;
- a Born, spin, decoder, or physical identification.

The central `zeta_8` phase is invisible to the Gram norms themselves. Its relevance is to the `SU(2)` lift of the two-channel half-angle transform, not to the scalar inequality directly.

This distinction preserves the earlier non-uniqueness breaker: arbitrary quadratic polarization does not select `zeta_8`; the determinant-one lift of this **specific** half-angle parity transform does.
