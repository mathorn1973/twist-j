# GAUSS HALF-FACTOR INNERNESS NO-GO

```text
STATUS: NON-CANONICAL candidate-T no-go for one post-prereg shortcut
ISSUE:  #357
PUBLIC STATUS CHANGES: none
RH STATUS CHANGE: none
```

## 1. Candidate killed

Connes--Consani factor the archimedean ratio by Gauss multiplication. For
`m>=1` and `0<=k<=m-1`, define

```text
gamma_(m,k)(s)=Gamma(s/(2m)+k/m),
phi_(m,k)(s)=gamma_(m,k)(s)/gamma_(m,k)(1-s),
```

and after an explicit pure exponential normalization obtain quasi-inner factors
`rho_inf^(m,k)` whose product is `rho_inf`. That normalization is entire and
nonzero, so it does not remove the pole obstruction below; its Hardy
orientation is otherwise not treated as harmless here.

The tempting half-angle shortcut was:

```text
for m=2, perhaps rho_inf^(2,k) rho_p is not merely quasi-inner
but actually inner, possibly for a distinguished prime such as p=5.
```

This is false for every prime `p`, every `m`, and every `k`.

## 2. Exact pole obstruction at s=0

The finite local ratio is

```text
rho_p(s)=(1-p^(s-1))/(1-p^(-s)).
```

At the origin,

```text
rho_p(s)
 = (1-p^-1)/(s log p) + O(1),
```

so it has a genuine simple pole with nonzero residue for every rational prime.

For the Gauss factor:

```text
rho_inf^(m,k)
```

has poles at the arithmetic progression

```text
s=-2k-2nm, n>=0.
```

Hence:

- if `k=0`, it has a pole at `s=0`, so the product with `rho_p` has pole order
  at least two;
- if `k>0`, it is finite and nonzero at `s=0`, because both Gamma arguments in
  its defining ratio are finite positive nonintegers there. Thus the simple
  pole of `rho_p` survives unchanged.

Therefore

```text
rho_inf^(m,k)(s) rho_p(s)
```

is not holomorphic in the left critical half-plane. It cannot be an inner
function there.

**Status:** candidate-T exact no-go for the explicitly stated
`GAUSS-PAIR-INNER` shortcut. This post-prereg label is not a public `F` claim.

## 3. Consequences

The result is uniform in `p`. In particular `p=5` is not exceptional for this
analytic gate. No TWIST-J five-selection inference is available here.

The Connes--Consani theorem that the paired factors are **quasi-inner** remains
exactly the correct statement: the relevant Hardy off-diagonal is compact,
not zero.

Thus the double-cover / half-argument algebra remains a valid structural
factorization, but it cannot supply Weil positivity by an automatic inner/model
space inclusion.

`COMPRESSED-DELAY-GENERATOR.md` records a distinct form-level comparison in
which quasi-inner off-diagonal defects are not assumed away. It is not thereby
selected as a surviving G6 target: frozen G3 remains UNDECIDED, so G4 and G6
are blocked and no replacement gate is opened here.
