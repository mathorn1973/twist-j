# LARGE-CUTOFF CAPACITY POSITIVITY

```text
STATUS: candidate-T, NON-CANONICAL
ISSUE:  #357
SCOPE:  a >= log 41
RH INPUT: none
```

## Statement

For every `a>=log 41` and every nonzero `v in C_c^infty(-a,a)`, the frozen
capacity form satisfies

```text
q_A,a(v) > 0.
```

## Inputs

Use the exact decomposition in `RESULT.md` and the candidate-T translation
chain bound. Let

```text
x = exp(a),
kappa = log(pi)-psi(1/4)
      = log(pi)+EulerGamma+pi/2+3log2.
```

External theorem input, independently formalized in Isabelle/AFP by Manuel
Eberl, *Concrete bounds for Chebyshev's prime counting functions* (2024):

```text
psi(y) >= (9/10)y   for y>=41,
psi(y) <= (6/5)y    for y>=0.
```

Here `psi(y)=sum_(n<=y) Lambda(n)` is the Chebyshev psi function. This is an
unconditional theorem and contains no RH input.

## Proof

The frozen capacity sum uses the strict delay cutoff `L_n<2a`, so take only
prime-power delays in the strict shell

```text
x < n < x^2.
```

Then `a<L_n<2a`, and the support-chain lemma gives

```text
||E_av-U_(L_n)E_av||^2 >= ||v||^2.
```

Therefore, discarding all other nonnegative terms,

```text
q_A,a(v)/||v||^2
 >= (1/2) sum_(x<n<x^2) Lambda(n)/sqrt(n) - kappa.
```

There is at most one integer at the upper endpoint `n=x^2`. If it is a prime
power, its omitted Mangoldt weight is at most

```text
Lambda(x^2) <= log(x^2)=2 log x;
```

otherwise the endpoint correction is zero. Since `sqrt(n)<x` on the strict
shell,

```text
sum_(x<n<x^2) Lambda(n)/sqrt(n)
 >= [psi(x^2)-psi(x)-2log x]/x
 >= (9/10)x - 6/5 - 2(log x)/x.
```

Hence

```text
q_A,a(v)/||v||^2
 >= (9/20)x - 3/5 - (log x)/x - kappa.
```

The elementary inequalities

```text
log(pi) < log 4 = 2 log 2 < 2,
EulerGamma < 1,
pi/2 < 2,
3 log 2 < 3
```

give `kappa<8`. For `x>=41`, the function `(log x)/x` is decreasing and
`log 41<4`, so

```text
(log x)/x <= (log 41)/41 < 4/41 < 1/10.
```

Therefore

```text
q_A,a(v)/||v||^2
 > (9/20)*41 - 3/5 - 1/10 - 8
 = 39/4 - 1/10
 = 193/20
 > 0.
```

Thus `q_A,a(v)>0` for every nonzero `v` whenever `a>=log 41`.

## Meaning

This closes G3 on the entire large-cutoff ray by a direct prime-side argument.
It does not use Weil positivity, zeta zeros, RH, or a numerical spectrum. The
remaining G3 domain is the compact interval

```text
0 < a < log 41.
```

No RH status movement follows.
