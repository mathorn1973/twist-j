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

Take only prime-power delays in the shell

```text
x < n <= x^2,
```

so

```text
a < L_n <= 2a.
```

For every such delay the support-chain lemma gives

```text
||E_av-U_(L_n)E_av||^2 >= ||v||^2.
```

(The endpoint `L_n=2a` is even stronger: supports are disjoint and the left
side is `2||v||^2`.) Hence, discarding all other nonnegative terms,

```text
q_A,a(v)/||v||^2
 >= (1/2) sum_(x<n<=x^2) Lambda(n)/sqrt(n) - kappa.
```

Because `sqrt(n)<=x` on this shell,

```text
sum_(x<n<=x^2) Lambda(n)/sqrt(n)
 >= [psi(x^2)-psi(x)]/x
 >= (9/10)x - 6/5.
```

Therefore

```text
q_A,a(v)/||v||^2
 >= (9/20)x - 3/5 - kappa.
```

It remains only to certify the constant. The elementary inequalities

```text
log(pi) < log 4 = 2 log 2 < 2,
EulerGamma < 1,
pi/2 < 2,
3 log 2 < 3
```

give

```text
kappa < 8.
```

At `x>=41`,

```text
(9/20)x - 3/5 - kappa
 > (9/20)*41 - 3/5 - 8
 = 197/20
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
