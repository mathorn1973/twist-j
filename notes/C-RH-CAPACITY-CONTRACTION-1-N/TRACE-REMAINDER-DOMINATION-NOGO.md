# STOPPED TRACE-REMAINDER DOMINATION NO-GO

```text
STATUS: STOP as a #357 result; auxiliary comparison retained
ISSUE:  #357
PUBLIC STATUS CHANGES: none
RH STATUS CHANGE: none
```

## 0. Post-commit decision

The claimed no-go below used the same incorrect positive pole factorization
withdrawn in `CORRECTION.md`. It is therefore **not** an `F` result for a
frozen #357 subroute. The calculation of `delta(1)` and the small-support
comparison may remain as an auxiliary source-normalization check, but it does
not decide G3 or constrain G6.

## 1. The stopped reduction

After the standard critical-line Fourier/Mellin normalization, the
archimedean Weil multiplier is

```text
2 theta'(xi)
 = Re psi(1/4+i xi/2)-log pi,
```

which is exactly the gamma multiplier used in the frozen capacity form.
Connes--Consani define the trace remainder `D` so that

```text
L = W_inf + D
```

is a positive functional without a support restriction.

The committed note then used the formula

```text
q_A = W_inf
      + |M_+|^2 + |M_-|^2
      + prime_antisymmetric_energy.
```

That premise is false for Suzuki's convolution involution. The actual pole
term is

```text
2 Re[M_+conj(M_-)]
 =(1/2)|M_++M_-|^2-(1/2)|M_+-M_-|^2.
```

Consequently the displayed rewrite through `L` and the proposed sufficient
condition

```text
D(v)
 <= |M_+(v)|^2+|M_-(v)|^2+prime_antisymmetric_energy(v).
```

do not represent the frozen capacity problem. The route was not
preregistered, and no falsifier fires from this comparison.

## 2. Exact value of the remainder kernel at the identity

Connes--Consani equation (10) gives, for `rho>=1`,

```text
delta(rho)
 = 2 sqrt(rho) [
     Si(2pi(1+rho))/(2pi(1+rho))
     + Si(2pi(rho-1))/(2pi(rho-1))
   ],
```

with the second quotient interpreted by its limit at `rho=1`.
Therefore

```text
delta(1)=2+Si(4pi)/(2pi).
```

Moreover

```text
Si(4pi)>0.
```

This needs no numerical evaluation. Pair the four half-periods:

```text
integral_0^(2pi) sin(x)/x dx
 = integral_0^pi sin(u)[1/u-1/(u+pi)]du >0,

integral_(2pi)^(4pi) sin(x)/x dx
 = integral_0^pi sin(u)[1/(u+2pi)-1/(u+3pi)]du >0.
```

Hence exactly

```text
delta(1)>2.
```

## 3. Auxiliary small-support comparison

Fix a nonzero `phi in C_c^infty(-1,1)` with

```text
I_phi = integral phi !=0,
```

and define

```text
v_a(x)=phi(x/a),
```

for sufficiently small `a>0`. Then `v_a in D_a` and, when

```text
2a<log 2,
```

there is no finite-prime term in the frozen capacity.

Let `C_a(t)` be the additive autocorrelation of `v_a`. The Connes trace
remainder can be written in the same additive normalization as

```text
D(v_a)=integral_R C_a(t) delta(exp(t)) dt.
```

Since the support of `C_a` shrinks to `0` and `delta(exp(t))` is continuous at
`t=0`,

```text
D(v_a)
 = delta(1) |integral v_a|^2
   + o(|integral v_a|^2).
```

On the other hand, uniformly on the shrinking support,

```text
exp(+x/2)=1+o(1),
exp(-x/2)=1+o(1),
```

so the two pole squares satisfy

```text
|M_+(v_a)|^2+|M_-(v_a)|^2
 = 2 |integral v_a|^2
   + o(|integral v_a|^2).
```

Because `delta(1)>2`, for all sufficiently small `a`

```text
D(v_a) > |M_+(v_a)|^2+|M_-(v_a)|^2.
```

There is no prime energy available in this range. Thus the separate inequality
comparing `D` with the **incorrect positive pole sum** fails on the smooth test
class. That is an auxiliary comparison under the displayed trace-remainder
normalization, not a breaker for the corrected `q_A`.

**Status:** candidate-T auxiliary asymptotic comparison; no #357 gate result.

## 4. Meaning

This calculation neither threatens nor supports capacity positivity. Because
the pole reservoir was mistyped, it does not show that the known positive
functional

```text
L=W_inf+D
```

cannot be used in some correctly typed joint inequality. It only rejects the
displayed comparison with `|M_+|^2+|M_-|^2`, which is not the pole term of the
frozen capacity.

Connes--Consani's archimedean work remains a comparison source involving a
pair of cutoff projections and prolate components. Importing its remainder
requires a separately frozen sign, normalization, and domain map.

## 5. Possible separately locked comparison

If separately preregistered, one may test a **coupled compression identity**
rather than the stopped scalar comparison:

```text
lossless semilocal scattering + cutoff pair
   -> orthogonal decomposition
   -> positive compressed/Sonin channel + signed prolate defect
   -> corrected R_+,R_- pair.
```

A possible exact comparison would be between the source off-diagonal
decomposition for `rho_inf rho_p`

```text
(1-P) kappa kappa_p P = E_inf + E_p + E_0
```

and the three corrected feature sectors

```text
gamma jump/pole channels,
complete-prime delayed tower,
two pole channels M_+,M_-.
```

A coefficient-level mismatch would kill only that separately frozen
intertwiner candidate before any RH question is reached. Under the current
#357 breaker order, G6 is not open while G3 is undecided. The immediate task
remains the corrected signed G3 coercivity problem.
