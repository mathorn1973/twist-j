# TWO-SIDED HARDY ESCAPE

```text
STATUS: NON-CANONICAL incubation result
ISSUE:  #357
PUBLIC STATUS CHANGES: none
RH STATUS CHANGE: none
```

## 1. Interval as two ordered half-space boundaries

Work in the additive variable. Let

```text
H_c = multiplication by 1_(-infinity,c),
C_a = H_a-H_(-a),
```

so `C_a` is the orthogonal projection onto the interval `(-a,a)` up to null
endpoints. Let `U` be any translation-invariant unitary scattering operator.

The complement of the interval splits orthogonally as

```text
1-C_a = H_(-a) + (1-H_a).
```

For input supported in the interval define the two escape rows

```text
B_L = H_(-a) U C_a,
B_R = (1-H_a) U C_a.
```

Because `C_a <= 1-H_(-a)` and `C_a <= H_a`, these are exactly

```text
B_L = H_(-a) U (1-H_(-a)) C_a,
B_R = (1-H_a) U H_a C_a.
```

Thus each row is a one-sided Hardy off-diagonal block at one endpoint,
restricted to the common interval input.

## 2. Exact two-sided Pythagorean defect

The two output spaces `H_(-a)H` and `(1-H_a)H` are orthogonal. Hence there is no
left/right cross term:

```text
B_a = [B_L ; B_R],
B_a^*B_a = B_L^*B_L+B_R^*B_R.
```

Define the one-sided boundary blocks

```text
K_(-a) = H_(-a) U (1-H_(-a)),
K_a    = (1-H_a) U H_a.
```

Then exactly

```text
B_a^*B_a
 = C_a K_(-a)^*K_(-a) C_a
   + C_a K_a^*K_a C_a.
```

This is the two-sided finite-interval escape defect as the sum of two positive
one-sided Hardy defects.

**Status:** candidate-T, general projection algebra.

## 3. Translation covariance

Let `T_c` translate the additive variable and write `H_c=T_cH_0T_c^*`. Since
`U` is translation invariant,

```text
K_(-a) = T_(-a) [H_0 U (1-H_0)] T_(-a)^*,
K_a    = T_a [(1-H_0) U H_0] T_a^*.
```

Thus the two finite-interval escape channels are shifted copies of the two
orientations of the same one-sided Hardy scattering defect.

For scattering phases satisfying the usual critical-line conjugation symmetry,
the two orientations are related by reflection/conjugation and have the same
singular spectrum. The present identity does not require this extra symmetry.

## 4. Archimedean specialization

For `U=U_inf`, `ARCHIMEDEAN-ESCAPE-DEFECT.md` identifies one one-sided squared
block with the Connes--Consani prolate compression

```text
P1 P1_hat P1.
```

The opposite boundary is its translated opposite-orientation counterpart.
Therefore the **two-sided interval escape energy is built entirely from two
translated one-sided prolate defects**. No additional left/right mixed escape
operator is needed.

This is a direct bridge from the one-sided Connes prolate geometry to the
finite interval used in the localized Suzuki form.

**Status:** candidate-D for the source identification of both orientations
until the exact reflection/conjugation convention is audited against the
source; candidate-T for the projection identity itself.

## 5. Where mixed terms can still enter

The absence of a cross term in `B_a^*B_a` does not mean the localized Weil
generator splits into two positive pieces. The phase-delay identity is

```text
-i W_a^*W_a'
 = -i(S_a^*S_a'+B_L^*B_L'+B_R^*B_R'),
```

and the individual derivative summands need not be self-adjoint or positive.
Mixed meromorphic jet terms can also appear when one expands the multiplicative
scattering function itself before taking the logarithmic derivative.

Thus:

```text
escape energy level:       exact positive left + right sum,
phase-delay generator:     signed derivative problem,
Hardy pole decomposition:  may contain collision jets before log derivative.
```

This separates three levels which had previously been conflated.

## 6. Stronger geometric form

Let

```text
S_a=C_a U C_a.
```

The full output column

```text
W_a=[S_a;B_L;B_R]
```

is an isometry on `C_aH`:

```text
S_a^*S_a+B_L^*B_L+B_R^*B_R=C_a.
```

Equivalently,

```text
S_a^*S_a
 = C_a
   - C_aK_(-a)^*K_(-a)C_a
   - C_aK_a^*K_aC_a.
```

The finite interval compression loses norm only through the two endpoint escape
channels. This is the exact operator Pythagoras underlying the cutoff.

**Status:** candidate-T.

## 7. Next gate: BOUNDARY-DELAY-DERIVATIVE

The remaining non-circular task is no longer to identify the prolate defect.
It is to differentiate this three-row isometric column and compare

```text
-i(S_a^*S_a'+B_L^*B_L'+B_R^*B_R')
```

with the explicit Suzuki local-place multiplier and the two global polar
channels.

At the archimedean place the test must decide whether the source trace/prolate
correction is exactly the derivative contribution of the two shifted escape
rows after the interval embedding is fixed.

At the first finite prime it must additionally respect the exact
`D_p,N_p,b_r` update and the complete-prime cutoff law.

Falsifiers:

1. an endpoint derivative term appears with no counterpart in the localized
   Weil functional;
2. the two boundary orientations require incompatible normalizations;
3. the derivative of the escape rows reproduces the wrong sign or coefficient
   for the Connes trace remainder;
4. a mixed collision jet survives after the scalar logarithmic derivative;
5. any step invokes Weil positivity or an equivalent innerness assumption.
