# ARCHIMEDEAN ALL-PASS CASCADE

```text
STATUS: NON-CANONICAL incubation note
ISSUE:  #357
PUBLIC STATUS CHANGES: none
RH STATUS CHANGE: none
```

## 1. Frozen archimedean scattering ratio

Use the standard real gamma factor

```text
Gamma_R(s) = pi^(-s/2) Gamma(s/2),
rho_inf(s) = Gamma_R(s)/Gamma_R(1-s).
```

On the critical line write

```text
s = 1/2 + i xi,
a = 1/4,
y = xi/2.
```

Then exactly

```text
rho_inf(1/2+i xi)
 = pi^(-i xi) Gamma(a+i y)/Gamma(a-i y),
|rho_inf|=1.
```

No zero of zeta and no RH input appears.

## 2. Exact Weierstrass all-pass product

The classical Weierstrass product

```text
1/Gamma(z)
 = z exp(gamma z)
   product_(m>=1) (1+z/m) exp(-z/m)
```

gives, with `a_m=m+a`, the exact boundary product

```text
rho_inf(1/2+i xi)
 = exp[-i xi(log pi + gamma)]
   c_a(xi)
   product_(m>=1) [c_(a_m)(xi) exp(i xi/m)],
```

where

```text
c_A(xi) = (A-i xi/2)/(A+i xi/2).
```

Every factor `c_A` is unimodular for real `xi`. The exponential factors are
pure translation phases. The product is the standard convergent Weierstrass
product for the gamma ratio; finite truncations are exact finite all-pass
cascades and converge to the displayed `rho_inf`.

**Status:** candidate-T, classical exact factorization/repackaging.

## 3. Each pole is one lossless first-order cell

Put `lambda=i xi/2`. Then

```text
c_A = (A-lambda)/(A+lambda).
```

It has the scalar continuous-time realization

```text
A_state = -A,
B = sqrt(2A),
C = sqrt(2A),
D = -1,

D + C (lambda-A_state)^(-1) B
 = -1 + 2A/(lambda+A)
 = (A-lambda)/(A+lambda).
```

On the imaginary axis this transfer function has modulus one. Thus every pole
`A=a_m=m+1/4` is an elementary lossless scattering cell. No global claim about
an infinite-dimensional conservative realization is made here; only the exact
finite cells and their convergent boundary product are asserted.

**Status:** candidate-T for each finite cell and finite cascade; infinite
operator-colligation limit remains open as a typed operator construction.

## 4. The same quarter-shift ladder controls the gamma Dirichlet energy

Differentiate the phase of the product. Since

```text
d/dxi arg c_A(xi) = -A/(A^2+(xi/2)^2),
```

one obtains

```text
d/dxi arg rho_inf(1/2+i xi)
 = -(log pi+gamma)
   - a/(a^2+(xi/2)^2)
   + sum_(m>=1)
       [1/m - a_m/(a_m^2+(xi/2)^2)].
```

The classical digamma series gives exactly

```text
d/dxi arg rho_inf(1/2+i xi)
 = Re psi(1/4+i xi/2)-log pi.
```

This is the archimedean Weil multiplier already derived independently from
Suzuki's source functional.

Moreover

```text
K(t)=e^(-t/2)/(1-e^(-2t))
    =sum_(m>=0) exp[-2(m+1/4)t].
```

Thus the same pole ladder

```text
A_m=m+1/4
```

appears simultaneously in

```text
the gamma scattering all-pass cascade,
the digamma phase derivative,
the positive jump-energy kernel K(t),
and the signed gamma square channels of predecessor #355.
```

This closes the archimedean local-object dictionary at the scalar scattering
level.

**Status:** candidate-T.

## 5. Finite places and infinity now have the same architecture

For a finite prime `p`, the incubation already proved

```text
rho_p = z_p / b_(p^-1/2)(z_p),
```

with `b_r` a lossless degree-one Blaschke transfer function. At infinity the
present note gives a convergent product of lossless first-order Cayley factors
`c_(m+1/4)` plus pure phase delays.

Hence, before imposing a finite support cutoff, every local scattering ratio
used in the semilocal product

```text
u_F = rho_inf product_(p in F) rho_p
```

has an explicit lossless factorization independent of RH.

The remaining obstruction is therefore not local losslessness. It is the
interaction of this global lossless scattering object with the finite
interval/time-frequency cutoff which produces the Weil form and the known
prolate/Sonin correction.

**Status:** candidate-D structural synthesis of exact local identities; no
claim that a single global colligation has yet been constructed.

## 6. Relation to the square-root/double-cover layer

The cell variable is already the half spectral variable

```text
lambda = i xi/2,
```

and the pole ladder starts at `1/4`. This is consistent with the exact global
half-factor identities already recorded:

```text
1-p^(-s)=(1-p^(-s/2))(1+p^(-s/2)),
Gamma_R(2u)=2^(u-1)Gamma_R(u)Gamma_R(u+1).
```

No uniqueness of the double cover among all multiplication formulas is
claimed. Its distinguished role here is only that the Weil functional is
quadratic and the current amplitude/scattering factorization is a two-leg
signed problem.

## 7. Current prior-art boundary

Connes--Consani--Moscovici's semilocal prolate work already relates the prolate
operator to the metaplectic representation of the double cover of
`SL(2,R)`, and proves stability of semilocal Sonin spaces when finite places are
added. Therefore neither the existence of a double-cover/metaplectic language
nor a semilocal prolate operator is new here.

Their 2026 `Zeta Spectral Triples` construction goes further in a different
finite-dimensional direction: it restricts the Weil quadratic form to the
scaling basis on `[lambda^-1,lambda]`, uses Euler products over
`p<=lambda^2`, and constructs rank-one perturbed self-adjoint scaling
operators. The paper explicitly leaves two essential steps open: simplicity
and evenness of the smallest Weil eigenvector, and a proof that the prolate
educated guess `k_lambda` approximates that eigenvector sufficiently well.

The present incubation must not claim those constructions as new. Its narrower
possible contribution is the explicit local factor dictionary and a proposed
route to identify the **cutoff defect itself** as the compression defect of a
fully factorized lossless scattering cascade.

## 8. Sharpened next gate: ARCHIMEDEAN-CUTOFF-DEFECT

The next construction must start with the unconditional lossless cascade above
and the exact time/support projection corresponding to `[-a,a]`. It must derive,
not insert, the known archimedean prolate remainder.

A positive outcome requires an identity of the schematic form

```text
compressed scattering energy
 = archimedean Weil energy + ||D_a v||^2
```

or an equivalent orthogonal-decomposition formula, with `D_a` independently
defined by the cutoff geometry.

The following are falsifiers:

1. the derived defect has the wrong kernel, sign, or normalization compared
   with the source prolate remainder;
2. the identity requires the Weil positivity inequality as an input;
3. the infinite cascade is used as an operator without a proved domain/limit;
4. the defect is fitted after observing the target remainder;
5. adding the first finite prime breaks compatibility with the exact
   `(D_p,N_p,b_r)` update already frozen.

If the archimedean defect identity fails, the current Sonin/colligation G6 route
is closed. If it survives, the next test is whether the complete-prime updates
preserve the same defect/compression architecture.
