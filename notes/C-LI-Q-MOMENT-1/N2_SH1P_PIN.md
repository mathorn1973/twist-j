# C-LI-Q-MOMENT-1 / N2 pin. Sigma_4 and the shifted SH-1' junction

```text
STATUS:          PRE-RUN FREEZE. NON-CANONICAL, NON-FORMAL.
LANE:            notes/j-li-q-moment-n2
BASE:            Public Canon v8, d94d4a94976a9b5d27db3a1c586e4886697daabb
VERIFIER COMMIT: 132538257e2671e50393d0f3fae42a101b47b3aa
VERIFIER SHA256: fc86ec75f31cd2884c6dffa36ba0068e778faebc06cf0c70aaae0ae3f6e80300
VERIFIER BYTES:  17534
FIRST RUN:       NOT YET EXECUTED AT THIS FREEZE
AUTHORITY:       none
```

This document freezes the N2 equation, code, precision budget, failure
thresholds, action layer, and non-claims before the first execution of the
verifier.  Static compilation occurred before this freeze; no gate in the
verifier was executed.  The earlier numerical readings used to choose the
precision budget were explicitly exploratory and are not evidence.

## 1. Equation and convention

Freeze the Stieltjes convention

```text
zeta(1+t) = t^-1 + gamma - gamma_1 t + gamma_2 t^2/2
            - gamma_3 t^3/6 + ...
```

and the paired zero-power convention

```text
log xi(1+t) = log xi(1) + sum_(k>=1) (-1)^(k+1) sigma_k t^k/k.
```

The coefficient of `t^4` must give, identically,

```text
sigma_4 = 1 + gamma^4 + 4 gamma^2 gamma_1 + 2 gamma_1^2
          + 2 gamma gamma_2 + (2/3) gamma_3 - pi^4/96.
```

There is no `gamma*zeta(3)` term in `sigma_4`.  The value `zeta(3)` remains
part of the full N2 comparator through `sigma_3`.

The pole-chart dictionary row is frozen as

```text
qw_3 = 20 sigma_1 + 10 sigma_2 + 4 sigma_3 + sigma_4.
```

The decisive shifted Hankel gate is

```text
SH-1' = det [[qw_1,qw_2],[qw_2,qw_3]]
      = qw_1 qw_3 - qw_2^2.
```

## 2. Third ladder junction

For the Li Toeplitz coefficients

```text
c_0 = 2 sigma_1,
c_1 = -sigma_2,
c_2 = -sigma_2 + sigma_3,
c_3 = -sigma_2 + 2 sigma_3 - sigma_4,
```

the antisymmetric block of `T_3` under reversal is

```text
[[c_0-c_3, c_1-c_2],
 [c_1-c_2, c_0-c_1]].
```

Its determinant must equal `SH-1'` as an exact polynomial identity.  This is
the third Hankel--Toeplitz ladder junction.  It decides one `2 by 2` block of
`T_3`; it does not decide the other block and is not a full `T_3` positivity
claim.

## 3. Code and permitted inputs

The pinned verifier is `verify_q_moment_n2.py` at the commit and hash above.
It may use only:

- integer and `Fraction` arithmetic from the Python standard library;
- the defining finite sums for `gamma_0,...,gamma_3`;
- exact outward-rounded logarithms, a rational Machin enclosure of `pi`, and
  integral comparison for `zeta(3)`; and
- the frozen N1 intervals for `sigma_1,...,sigma_3` as comparators only.

It must not read a decimal Stieltjes constant, zero list, prime table, Li
table, zeta evaluation, external file, network resource, subprocess output,
random input, or floating-point result.

## 4. Precision and independent evaluation graphs

Freeze

```text
scale             10^24
N                 200000
log series terms  32
gamma_3 max width 1e-17
```

All four Stieltjes constants are refreshed by one B4 Euler--Maclaurin rule.
For `f_p(x)=log(x)^p/x` and

```text
A_p(N) = sum_(k<=N) log(k)^p/k - log(N)^(p+1)/(p+1),
```

the verifier must prove the tail shape `f_p'''<0`, `f_p''''>0` on
`[N,infinity)` and then use

```text
gamma_p = A_p - f_p(N)/2 - f_p'(N)/12 + f_p'''(N)/720 + R_p,
|R_p| <= -f_p'''(N)/720.
```

The determinant is evaluated twice:

```text
direct:  qw_1 qw_3 - qw_2^2,
T3 form: qw_1 (qw_1 + sigma_4 - 2 sigma_3) - sigma_3^2.
```

Their interval enclosures need not be identical, but they must overlap.

## 5. Frozen gates and falsifiers

```text
N2-S4   exact symbolic sigma_4 derivation, including the absent
        gamma*zeta(3) term;
N2-J3   exact equality SH-1' = det(T_3 antisymmetric block);
N2-EM4  the common B4 tail-shape proof for gamma_0,...,gamma_3;
N2-G3   width(gamma_3) <= 1e-17;
N2-OLD  refreshed sigma_1,...,sigma_3 lie inside the frozen N1 intervals;
N2-Q3   qw_3 has a strictly positive lower endpoint;
N2-DIR  the direct SH-1' interval has a strictly positive lower endpoint;
N2-T3   the T3-block interval has a strictly positive lower endpoint;
N2-OVL  the two determinant intervals overlap.
```

Any failed algebra, tail proof, width, containment, positivity, or overlap
gate fires N2.  Thresholds are not moved after this pin.  A negative or
inconclusive determinant is retained and independently audited; it kills the
declared reference calibration or its implementation, not RH.

## 6. Action layer and stop line

N2 is an `L5` exact reference-side coefficient and positivity calibration.
It neither supplies nor lifts to an `L6` moment measure.  Passing may close
only this finite N2 gate at notes-grade candidate scope.  It does not
construct `A_J`, `B_J`, a J-native parent pair, a positive moment functional,
the other block of `T_3`, a full all-order Hankel or Toeplitz ladder, G8, or
RH.  It creates no public issue, probe, registry row, Canon edit, tag, or
release.

