# Complete threshold-law segment and fourth-moment repair

Conditional L1 exact mathematics. This proof uses the owner-selected v87
passive family and existing scalar cold source/coupling. A finite rational
ensemble is an explicit input, not an occurrence law selected by U.

## 1. Source class and full passive records

Let `Z={-2,-1,0,1,2}^4`, `s=sum_i z_i`, and

```text
t=s^2/20, l=(z0-z1-z2+z3)^2/4,
r=((z0-z3)^2+(z1-z2)^2)/2, m=t+l+r.
```

Use exactly the five partition IDs and ordered blocks

```text
PI-ALL ((t,l,r)), PI-TRACE ((t),(l,r)),
PI-LEG ((t,r),(l)), PI-PAIR ((t,l),(r)),
PI-ATOMS ((t),(l),(r)).
```

Each record has partition_id, support_state, total_weight, ordered
block_weights and normalized_weight_state. For m>0 the tags are SUPPORTED
and NORMALIZED with each block divided by m; for z=0 the total and all
blocks are zero, tags ZERO_SUPPORT and ZERO_DENOMINATOR. These are the
unchanged adopted records, with literal equality.

Put `F={z in Z:(t,l,r)=(0,1,5)}` and fix

```text
Sigma = [[1,0,-1/2,-1/2], [0,3/2,-3/2,0],
         [-1/2,-3/2,5/2,-1/2], [-1/2,0,-1/2,1]].
```

Let E be all rational probability assignments mu on Z whose complete
selected passive law is that of this atom record and for which
`sum_z mu(z) z z^T=Sigma`. Since PI-ATOMS is included, the full-law
condition is exactly `support(mu) subset F`. Every other passive view is
the specified coarsening. On F all records are supported, with total six
and normalized atoms `(0,1/6,5/6)`; normalized data are not extra ensemble
constraints once this full point law is fixed. In particular s=0 on F.

Zero remains an element of the ambient source. Its record has total zero
and its deposit/count are zero. Its zero mass in E follows from the
stipulated full record law, not outcome selection; zero-count sources in F
are retained. Each balanced source is represented by a native pointed head
with counter and last two coordinates zero, using the inverse balanced
residue map in the first four coordinates.

## 2. Exact first cold origin response

The inherited centered source is

```text
S(z)=sum_(j=0)^4 ((z,0)_j-s/5) delta_(y_j),
y=((0,0,0),(1,1,0),(1,0,1),(0,1,1),(2,0,0)).
```

The wave operator is `L f(x)=sum_d c_d[f(x)-f(x+d)]`, where d ranges
over every D3 vector of squared norm 2,4,8,10,16, with weights
6,1,15,1,1 divided by 324. The shell sizes 12,6,12,24,6 give total
weight 8/9. Thus `H=2I-L` has diagonal 10/9. At the origin, the
coefficients of H applied to the five marked sites are
`(10/9,1/54,1/54,1/54,1/324)`. Their sum is 379/324. Subtracting one
fifth of this sum from the first four coefficients gives

```text
(H S(z))_0=h0 z,
h0=(1421,-349,-349,-349)/1620.
```

For initial pair `(u,v)=(0,S(z))`, zero incoming cold slot and origin
conductance one, the registered coupling gives

```text
w0=(H S(z))_0/(1+1/2), b0=-w0/2=-h0 z/3,
D0=b0^2=(h0 z)^2/9.
```

At s=0, `h0 z=(59/54)z0`, so `D0=c z0^2`, c=3481/26244.
Fix q=1/10 and set C=floor(D0/q), with initial heat zero. Put y=z0^2.
Then y is exactly one of 0,1,4, and

```text
1 <= 34810/26244 < 2,
5 <= 139240/26244 < 6.
```

Hence y=0,1,4 gives C=0,1,5 respectively, including all zero and
multiple crossings. The following pointwise identities therefore hold on F:

```text
C=(11y+y^2)/12,
1[C>0]=(5y-y^2)/4,
1[C=5]=(y^2-y)/12,
1[C=1]=(4y-y^2)/3,
1[C=0]=(y^2-5y+4)/4.
```

## 3. Explicit indistinguishable endpoint preparations

Define P and Q by

| P source | mass | Q source | mass |
|---|---:|---|---:|
| (0,1,-2,1) | 1/2 | (1,-2,1,0) | 1/4 |
| (0,2,-1,-1) | 1/4 | (1,0,1,-2) | 1/4 |
| (2,0,-1,-1) | 1/4 | (1,1,-2,0) | 1/2 |

Each source lies in F by direct substitution. Their weighted outer products
both sum to the displayed Sigma; their masses sum to one. Thus both belong
to E and have exactly the same five full record laws and every quadratic
expectation `E[z^T A z]=tr(A Sigma)`. This includes the mean quadratic
energy responses of any fixed context/horizon in the existing linear cold
model; it does not extend to nonlinear or adaptively selected contexts.

P has y=0 with mass 3/4 and y=4 with mass 1/4. Q has y=1 with mass one.
Consequently their ordered count laws on (0,1,5) are `(3/4,0,1/4)` and
`(0,1,0)`. Their M4 values are 4 and 1; mean counts are 5/4 and 1,
and any-crossing masses 1/4 and 1. The discrepancy survives knowledge of
every quadratic mean and the entire passive law.

Sigma is a raw second moment. The source means are respectively
`(1/2,1,-3/2,0)` and `(1,0,-1/2,-1/2)` and differ. A centered version
is available without adding an assumption: replace every atom z of mass p
in each ensemble by z and -z of masses p/2. All passive weights, outer
products, deposits, counts and M4 are even in z, so both symmetrized
ensembles retain every assertion while their means vanish. Only for this
symmetrized version is Sigma also the centered covariance.

## 4. Complete and sharp prediction set

For arbitrary mu in E write `a=mu(y=4)`. The Sigma00 condition is E[y]=1.
Normalization and this one moment imply

```text
mu(y=1)+4a=1,
mu(y=0)=1-mu(y=1)-a=3a.
```

Nonnegativity gives 0<=a<=1/4, and the deterministic count map gives the
law `(3a,1-4a,a)` with no other supported counts. This proves containment
for every member of E, using no finite enumeration of ensembles.

For the converse, let any rational a in [0,1/4] be given and form
`mu_a=4a P+(1-4a) Q`. Its coefficients are nonnegative and sum to one;
its full passive law and raw Sigma are unchanged because both endpoints
have the same constraints. Its mass at y=4 is a. Thus every rational
point in the displayed segment is attained by an admitted rational
ensemble. This is a construction inside the complete class, not a
restriction of that class to a chosen ansatz. The same argument over the
reals proves the real-ensemble statement. It also works with the centered
endpoint versions if mean zero is additionally required.

Therefore exactly

```text
Pr(C>0)=1-3a in [1/4,1],
E[C]=1+a in [1,5/4]
```

and both bounds are attained. No calibration consisting only of further
quadratic means can reduce this segment: every mu_a has the same Sigma.

## 5. One extra fourth-moment expectation is sufficient and necessary

Since y=z0^2, the fourth source moment satisfies

```text
M4=E[y^2]=(1-4a)+16a=1+12a.
```

It follows that 1<=M4<=4 and

```text
a=(M4-1)/12,
(Pr(C=0),Pr(C=1),Pr(C=5))
  =((M4-1)/4,(4-M4)/3,(M4-1)/12),
Pr(C>0)=(5-M4)/4,
E[C]=(11+M4)/12.
```

Every admitted value of M4 in [1,4] gives one and only one count law;
every rational value is realized by the construction above. Zero added
scalar expectations cannot identify the law, since P and Q already agree
on all supplied information and disagree on the law. One scalar M4
suffices by these equations. This proves the stated minimum of one for
this frozen target law and information class, not global identification
of the source ensemble or all future nonlinear outcomes.

Finally D0=c y pointwise on F, so

```text
E[D0^2]=c^2 E[y^2]=c^2 M4,
M4=(26244/3481)^2 E[D0^2].
```

A supplied analog deposit second moment is therefore an equivalent repair.
It is an additional observable, not a sixth PassiveWeightRecord field or
an already realized physical calibration. The choice of source ensemble,
injection, coupling, clock, threshold and observation relation remains
explicit. No empirical law, Born derivation, reset, apparatus completeness
or cross-layer lift follows.
