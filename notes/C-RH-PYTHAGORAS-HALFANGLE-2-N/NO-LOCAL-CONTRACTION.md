# NO INDEPENDENT PRIME-BY-PRIME CONTRACTION

```text
STATUS: candidate-T / exact negative boundary inside NON-CANONICAL incubation
ISSUE:  #355
PUBLIC STATUS CHANGE: none
```

## Statement

Fix one delayed prime-power leg

```text
h_L(t)=(|t|-L)_+,   L>0,
```

and its half-angle feature pair from `HALFANGLE-PRIME-KERNEL.md`:

```text
G_(h_L)(t,u)=<S_L(t),S_L(u)>-<C_L(t),C_L(u)>.
```

There is no contraction

```text
T_L : closure(span{S_L(t): t in R}) -> closure(span{C_L(t): t in R})
```

satisfying

```text
T_L S_L(t)=C_L(t)   for every t.
```

The same conclusion holds with the two signs interchanged.

## Proof

If such a contraction existed, then for every finite coefficient family

```text
||sum_j c_j C_L(t_j)||^2 <= ||sum_j c_j S_L(t_j)||^2.
```

Therefore the kernel

```text
G_(h_L)(t,u)=<S_L(t),S_L(u)>-<C_L(t),C_L(u)>
```

would be positive semidefinite.

But at the two points

```text
t_1=L/2,   t_2=3L/2,
```

the exact `2 x 2` principal matrix has determinant

```text
-L^2/4 < 0
```

as already frozen in `break.py`. Contradiction.

Changing the sign merely exchanges the positive and negative labels; the determinant remains negative. Hence neither half-angle sector dominates the other on the complete one-leg trajectory.

## Corollary: local SU(2) magic cannot prove RH

The matrix

```text
U = 1/sqrt(2) [[1,1],[-i,i]]
```

from `PRIME-SU2-HALFANGLE.md` is unitary. Multiplication by the central eighth-root phase that moves `U` into `SU(2)` changes no norm and no Gram inequality.

Therefore the half-angle `SU(2)` lift, including its central correction
`lambda=+/-sqrt(-i)=+/-zeta_8^(-1)`, can reorganize the two quadratures but
cannot by itself convert an indefinite delayed prime leg into a positive one.

The one-leg theorem alone says that a successful contraction must mix sectors
that the independent-leg model keeps separate. The stronger theorem below
decides which separation must be crossed.

## Stronger corollary: the whole prime sector is indefinite

Let

```text
G_P(t,u)=sum_(n>=2) Lambda(n)/sqrt(n) G_(h_(log n))(t,u).
```

Put

```text
a=(1/4)log 6,   t_1=-a,   t_2=a.
```

Then

```text
log 2 < 2a=(1/2)log 6 < log 3,   a<log 2.
```

Thus every term with `n>=3` vanishes on `{t_1,t_2}`.  The `n=2` term
has

```text
d=2a-log 2=(1/2)log(3/2)>0
```

and the exact principal matrix

```text
(log 2)/sqrt(2) [[0,d],[d,0]].
```

Its determinant is

```text
-(log 2)^2 (log(3/2))^2 / 8 < 0.
```

Therefore `G_P` is indefinite. The same determinant obstruction applies
after reversing the Krein sign. Consequently no contraction confined to the
complete finite-prime sector can carry all its sine half-angle features to
all its cosine half-angle features, or conversely. Arbitrary mixing among
prime powers is insufficient.

Any successful contraction for this explicit source-side factorization must
therefore have a nonzero finite/archimedean cross block. It must couple the
prime channels to the pole and/or Gamma/Hurwitz channels; it cannot be block
diagonal by place.

This post-preregistration corollary is an exact NON-CANONICAL review result.
It does not construct the required cross-place map and does not move RH.

The remaining possible couplings are:

```text
- prime and pole channels,
- prime and Gamma/Hurwitz channels,
- or a genuinely global completion carrying all of them.
```

The theorem does not decide which cross-place mixing exists. It rules out
both the prime-by-prime and the complete prime-only routes exactly.

## Consequence for the research target

The surviving problem is not

```text
find a good 2 x 2 unitary for every prime.
```

It is

```text
find a globally coupled contraction / colligation whose local channels are
individually indefinite but whose complete source-side Gram difference is PSD.
```

That is a stronger restriction and a cleaner falsification boundary.
