# LARGE-CUTOFF SHELL LEMMA AND STOPPED POSITIVITY PROOF

```text
STATUS: candidate-T shell lemma; claimed G3 theorem withdrawn
ISSUE:  #357
SCOPE:  a >= log 41
RH INPUT: none
```

## Decision

The prime-power shell estimate below is exact, but the earlier conclusion

```text
q_A,a(v)>0 for every nonzero v and every a>=log 41
```

does **not** follow from it. The supplied proof treated the pole term as a sum
of positive squares. `CORRECTION.md` records the source-level error and the
correct signed formula. Large-cutoff G3 is therefore `UNDECIDED`, not
refuted.

## Valid inputs

Let

```text
x=exp(a),
psi_Ch(y)=sum_(n<=y) Lambda(n),
kappa=log(pi)-psi_dig(1/4).
```

The independently formalized Chebyshev bounds used here are

```text
psi_Ch(y)>=(9/10)y for y>=41,
psi_Ch(y)<=(6/5)y for y>=0.
```

For `a<L<2a`, the exact support-chain lemma gives

```text
||E_a v-U_L E_a v||^2>=||v||^2.
```

## Valid strict-shell estimate

The frozen capacity sum uses `L_n<2a`, so retain only

```text
x<n<x^2.
```

There is at most one integer at the upper endpoint `n=x^2`. If it is a prime
power, its omitted Mangoldt weight is at most `2log x`; otherwise the endpoint
correction is zero. Since `sqrt(n)<x` on the strict shell,

```text
sum_(x<n<x^2) Lambda(n)/sqrt(n)
 >= [psi_Ch(x^2)-psi_Ch(x)-2log x]/x
 >= (9/10)x-6/5-2(log x)/x.
```

Consequently the prime shell contributes at least

```text
[(9/20)x-3/5-(log x)/x]||v||^2
```

to `q_A,a(v)`. This is a candidate-T lemma and contains no RH input.

## Why the original closure fails

The correct pole contribution is

```text
B_a(v)=2 Re[M_+(v)conj(M_-(v))]
      =(1/2)|M_++M_-|^2-(1/2)|M_+-M_-|^2.
```

It cannot be discarded as nonnegative. The shell calculation proves only

```text
q_A,a(v)/||v||^2
 >= B_a(v)/||v||^2
    +(9/20)x-3/5-(log x)/x-kappa.
```

As a rank-two operator on `L2(-a,a)`, `B_a` has lowest eigenvalue

```text
2a-2sinh(a).
```

This independent lower bound is of order `-exp(a)` and is too costly to
combine with the displayed shell estimate. Recovering a large-cutoff theorem
requires a new joint inequality that couples the negative pole direction to
the archimedean and/or prime jump energies.

The final arithmetic in the stopped proof also read `193/20`; the scalar
expression written there equals `39/4=195/20`. This minor arithmetic error did
not cause the stop; the indefinite pole term did.

## Current scope

```text
translation-chain lemma: candidate-T
strict prime-shell estimate: candidate-T
G3 for a>=log 41: UNDECIDED
G3 for all a>0: UNDECIDED
```

No RH, Canon, Registry, frontier, or evidence status changes follow.
