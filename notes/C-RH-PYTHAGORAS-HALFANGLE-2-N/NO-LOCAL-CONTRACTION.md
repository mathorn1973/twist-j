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

Therefore the half-angle `SU(2)` lift, including its forced central `sqrt(i)` phase, can reorganize the two quadratures but cannot by itself convert an indefinite delayed prime leg into a positive one.

Any successful contraction behind Suzuki positivity must mix at least two sectors that the independent-leg model keeps separate. Possibilities include:

```text
- different prime powers,
- prime and pole channels,
- prime and Gamma/Hurwitz channels,
- or a genuinely global completion carrying all of them.
```

The theorem does not decide which mixing exists. It rules out the most local route exactly.

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
