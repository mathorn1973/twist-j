# TRACE-REMAINDER DOMINATION NO-GO

```text
STATUS: F for the frozen simple-domination subroute
ISSUE:  #357
PUBLIC STATUS CHANGES: none
RH STATUS CHANGE: none
```

## 1. The tempting reduction

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

Since the frozen capacity has the form

```text
q_A = W_inf
      + |M_+|^2 + |M_-|^2
      + prime_antisymmetric_energy,
```

one has algebraically

```text
q_A
 = L
   + |M_+|^2 + |M_-|^2
   + prime_antisymmetric_energy
   - D.
```

This suggested the stronger sufficient condition

```text
D(v)
 <= |M_+(v)|^2+|M_-(v)|^2+prime_antisymmetric_energy(v).
```

The present note kills that sufficient subroute.

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

## 3. Small-support asymptotic breaker

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

There is no prime energy available in this range. Thus the proposed separate
domination of the trace remainder fails on the actual smooth frozen test
class.

**Status:** exact F for `TRACE-REMAINDER-SEPARATE-DOMINATION`.

## 4. Meaning

This negative result does not threaten capacity positivity. It shows instead
that the known positive functional

```text
L=W_inf+D
```

cannot be used by simply paying for `D` with the pole and prime channels after
the fact. The positive Sonin reservoir and the trace/prolate remainder must be
coupled before taking the final inequality.

This is consistent with Connes--Consani's actual proof at the archimedean
place: they move the small square Delta into the positive reservoir Sigma by
using a pair of cutoff projections and prolate components, rather than proving
a pointwise or separate domination of the trace remainder.

## 5. Sharpened surviving target

The G6 route must now construct a **coupled compression identity**, not a
scalar domination:

```text
lossless semilocal scattering + cutoff pair
   -> orthogonal decomposition
   -> positive compressed/Sonin channel + signed prolate defect
   -> frozen R_+,R_- pair.
```

The next exact comparison is between the source off-diagonal decomposition for
`rho_inf rho_p`

```text
(1-P) kappa kappa_p P = E_inf + E_p + E_0
```

and the three frozen feature sectors

```text
gamma/pole ladder,
complete-prime delayed tower,
two pole channels M_+,M_-.
```

A coefficient-level mismatch kills that proposed intertwiner before any RH
question is reached.
