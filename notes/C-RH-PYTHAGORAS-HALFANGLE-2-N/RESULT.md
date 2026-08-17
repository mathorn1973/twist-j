# RESULT C-RH-PYTHAGORAS-HALFANGLE-2-N

```text
STATUS: NON-CANONICAL INCUBATION RESULT
ISSUE:  #355
PUBLIC CLAIM STATUS CHANGES: none
RH STATUS CHANGE: none
```

## R0. Source correction

The predecessor #354 is STOP because the HTML rendering used there omitted the final two archimedean terms of Suzuki equation (1.1). This result uses the full PDF equation only.

## R1. Prime side is exactly one square level below the critical weight

**candidate-T, elementary.** For every prime power contribution,

```text
Lambda(n)/sqrt(n) = [sqrt(Lambda(n)) n^(-1/4)]^2.
```

For fixed `t>=0`, define the direct-sum interval amplitude

```text
p_(n,t)(u) = sqrt(Lambda(n)) n^(-1/4) 1_[log n,t](u)
```

when `log n<=t`, and zero otherwise. Then

```text
P(t) = sum_n ||p_(n,t)||_L2^2.
```

Thus the critical exponent `1/2` is literally `1/4 + 1/4` at this amplitude level. This is a reformulation of the prime term, not an RH result.

## R2. One archimedean summand is an exact square, but not the whole archimedean side

**candidate-T, elementary.** Put

```text
A0(t)=4(e^(t/2)+e^(-t/2)-2).
```

Then

```text
A0(t) = [4 sinh(t/4)]^2.
```

The predecessor's stronger statement that the whole archimedean side is this square was false because it omitted `R_inf`.

## R3. Independent delayed prime legs are not positive Gram legs

**F within the frozen independent-leg model.** For `h_L(t)=(|t|-L)_+`, polarizing either `+h_L` or `-h_L` gives at `t=L/2`, `u=3L/2` a `2 x 2` principal matrix with determinant

```text
-L^2/4 < 0.
```

Therefore no proof can treat the individual delayed prime-power screw terms as independent positive Gram legs. Any positivity must arise after a larger pairing, completion, quotient, or cancellation.

`break.py` checks the normalized exact determinant `-1/4` using `Fraction` only.

## R4. The full gamma/Hurwitz-Lerch correction is a signed Pythagorean object

**candidate-T, exact source rewrite.** Let

```text
a_m = m + 1/4,
kappa = log(pi) - psi(1/4)
      = log(pi) + EulerGamma + pi/2 + 3 log 2 > 0.
```

Using

```text
C = zeta(2,1/4) = sum_(m>=0) a_m^(-2)
```

and

```text
e^(-t/2) Phi(e^(-2t),2,1/4)
  = sum_(m>=0) e^(-2 a_m t) a_m^(-2),
```

one obtains, for `t>=0`,

```text
R_inf(t)
 = -(kappa/2)t
   + (1/4) sum_(m>=0) [1-e^(-2 a_m t)]/a_m^2.
```

Define

```text
q_(m,t)(u) = e^(-a_m u)/sqrt(2a_m) 1_[0,t](u),
c_t(u)     = sqrt(kappa/2) 1_[0,t](u).
```

Then exactly

```text
R_inf(t) = sum_m ||q_(m,t)||_L2^2 - ||c_t||_L2^2.
```

So the extra archimedean term is not a positive norm. It is one positive infinite square-sum minus one negative linear square.

### Concavity and sign structure

For `t>0`, termwise differentiation is absolutely valid and gives

```text
R_inf'(t) = -kappa/2 + (1/2) sum_(m>=0) e^(-2a_m t)/a_m,
R_inf''(t)= -sum_(m>=0) e^(-2a_m t)
           = -e^(-t/2)/(1-e^(-2t)) < 0.
```

Hence `R_inf` is strictly concave. Moreover `R_inf'(t)->+infinity` as `t->0+`, `R_inf'(t)->-kappa/2` as `t->infinity`, and `R_inf(t)->-infinity`. Therefore it has exactly one positive critical point (a maximum) and exactly one positive zero after that maximum. A numerical location of that zero is diagnostic only and is not theorem evidence.

## R5. Exact signed Pythagorean factorization of Suzuki's prime-side scalar

**candidate-T identity; candidate-D RH reading.** Define Hilbert direct sums

```text
H_plus  = C  (+)  direct_sum_(m>=0) L2(R_+),
H_minus = L2(R_+) (+) direct_sum_(Lambda(n)>0) L2(R_+),
```

and amplitude curves

```text
U_t = (4 sinh(t/4), (q_(m,t))_m),
V_t = (c_t, (p_(n,t))_n).
```

Then the full source equation becomes the exact indefinite norm identity

```text
Psi(t) = ||U_t||^2 - ||V_t||^2.
```

No zeros and no RH assumption enter this factorization.

By imported Suzuki Theorem 1.7 only after the identity is established,

```text
RH iff ||V_t|| <= ||U_t|| for every t>=0.
```

This is not a proof of RH. It is a reduction of Suzuki's pointwise criterion to membership of one explicit curve in the positive cone of a fixed Krein space.

## R6. What `sqrt(i)` does and does not earn

### Non-uniqueness breaker

**F for uniqueness from bilinear reconstruction alone.** Let `omega=c+is` be a unit phase and let the complex cross term be `z=a+ib`. With the convention

```text
D_omega = 4 Re(omega z),
D_bar   = 4 Re(conj(omega) z),
```

we have

```text
D_omega = 4(ca-sb),
D_bar   = 4(ca+sb).
```

Both `a` and `b` are reconstructed whenever `c*s != 0`. Infinitely many phases work. `break.py` gives the exact rational witness `omega=(3+4i)/5`. Therefore quadratic polarization alone does not select `zeta_8`.

### Balanced-conjugate boundary

**candidate-T lemma.** If one separately requires the conjugate pair to have equal sensitivity to the real and imaginary quadratures, then `|c|=|s|`. Together with `c^2+s^2=1`, this forces

```text
c^2=s^2=1/2,
omega^2 = +/- i.
```

Thus the balanced conjugate phases are exactly the odd eighth roots, up to signs and conjugation. In that precise restricted sense `sqrt(i)` is forced by a half-angle polarization. The present incubation has not derived the balancing requirement from the zeta problem, so no `zeta_8` bridge is promoted.

## R7. One-level-up target sharpened

The signed factorization identifies the real missing theorem.

A pointwise family of contractions `T_t` with `V_t=T_t U_t` is circular, because such a contraction exists exactly when the already-targeted pointwise norm inequality holds.

A genuine advance would be a **single independently defined contraction or partial isometry** on a frozen amplitude carrier, or an equivalent block-Gram factorization, that transports the whole curve `U_t` to `V_t` and whose contractivity follows without RH. This is stronger and non-circular.

The naive nested-interval amplitude embedding does not automatically give Suzuki's screw Gram kernel; its diagonal is `Psi(t)` but stationary-increment kernel structure is a separate obligation. No claim is made that a fixed contraction exists.

## Source relation

Suzuki already decomposes the full screw hermitian form into pole, prime, and archimedean pieces and proves unconditional positivity for sufficiently small intervals. The present result does not claim that decomposition as new. The narrower contribution here is the amplitude-level signed Pythagorean rewrite and the exact boundary on when a balanced conjugate polarization selects eighth roots.

## Verdict

```text
SURVIVES, narrowed.
```

The naive `all positive independent legs` route is falsified. The useful surviving structure is:

```text
prime critical weight       -> exact quarter-power amplitudes
pole term                   -> exact square
Gamma/Lerch correction      -> positive square-sum minus one square
full Psi                    -> explicit Krein norm difference
balanced complex polarization -> sqrt(+/- i), but balancing not yet zeta-forced
```

The next non-circular target is not another scalar inequality. It is an exact carrier-level map or Gram completion that turns the signed Pythagorean factorization into a fixed contraction or stationary-increment screw line without importing RH or zero data.
