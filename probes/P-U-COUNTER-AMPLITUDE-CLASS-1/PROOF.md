# Counter-dependent amplitudes and their native source factors

**Prospective proof. Candidate-T, L1; NON-CANONICAL until a separate Canon
fold. This file reports no completed formal execution.**

All statements concern exact mathematical readers of the unchanged native
architecture. A target evolution and an amplitude assignment remain declared
inputs. Neither a physical amplitude, physical time, occurrence law nor a
cross-layer realization is supplied.

## 1. Sources, overlap and domains

The source tree is public `main` commit
`16e6bd3579527f522ca7e8c85411107f6873eea8`, with the unchanged Public Canon v89
normative content declared by `STATUS.md`. The exact dependencies are:

- `DEF-ARCHITECTURE` and `KERNEL-Z6-SYNCHRONIZATION` in
  [the Canon](../../canon/CANON.md);
- canonical `U-NATIVE-CHART-AND-QDD-READBACK`, including its explicit chart
  and five-head fibres, proved in
  [native readback PROOF, sections 1-3](../P-QDD-U-NATIVE-READBACK-1/PROOF.md);
- the canonical regenerable-archive corollary under
  `U-NATIVE-COMMON-READY-SOURCE-RETENTION`;
- the merged, non-canonical exact quotient proof in
  [C-U-SELECTOR-READING-STRUCTURE-N/PROOF.md](../../notes/C-U-SELECTOR-READING-STRUCTURE-N/PROOF.md),
  and its [selector arguments, sections 3-5](../../notes/C-U-SELECTOR-READING-STRUCTURE-N/SELECTOR.md).

The source commit fixes these linked proof bytes. The thirteen-class count,
its explicit formula, and the selector obstructions were already exposed.
This is not a blind discovery. The 3125-label reader classification below is
a direct corollary of the canonical chart/readback theorem, not a new native
information-retention theorem. This probe gives the relevant reader classes
one explicit common statement and tests their exact boundaries. It does not
execute or dispose of the separately owned separable-counter probe.

Set `X=F5^6`, in native coordinate order `(p1,p4,p1p,p4p,q,r)`, and write

```text
z(x)=p1+p4+p1p+p4p+q+r,
theta_n=s_2(n) mod 2,
f_t(x)=g_(z(x)+2t)(x),  t in {0,1},
d_n=f_(theta_n),
U(n,x)=(n+1,d_n(x)),
E_0=id_X,  E_(n+1)=d_n o E_n.
```

The native `g_0,...,g_4` are `a,b,c,d,e`. They are fixed by

```text
a(x)=(p4,p1,p4p,p1p,q,r),
b(x)=(-p1p,-p4p,-p1,-p4,-q,-r),
c(x)=(-p1p+2,-p4p+1+r,-p1+2,-p4+1-r,1-q,-r),
d(x)=(2-p1,1-p4,3-p1p,4-p4p,1-q,1-r),
e(x)=(2-p1,1-p4,3-p1p,4-p4p,2-q,1-r).
```

All checkpoint arithmetic is modulo five. Distinguish two domains:

```text
Omega = N_0 x X,                         the complete declared state space;
D = {(n,x): x in X_n}, X_n=E_n(X),      origin-zero reachable states.
```

The whole-space separable theorem uses `Omega`. The general counter-reader
classification uses `D`. A state `(n,x)` outside `D` is not silently admitted
to the latter theorem. The full pointed orbit, which retains its initial
head as an input, is another source port.

## 2. Exact fixed-checkpoint factor on the whole state space

Put

```text
A=p1+p1p, B=p4+p4p,
C=p1-p1p-2, D0=p4-p4p-1,
S=A+B, T=C+D0, z=S+q+r,

kappa(x)=(S-1,-T-2r)  if z=0,
         (S,T)         if z=1 or z=2,
         (S,-T)        if z=3 or z=4,
Q(x)=[kappa(x)] in F5^2/{+1,-1}.
```

The temporary coordinate `D0` is not the reachable domain `D`. The complete
phase/control substitution table is

| Phase z | Control t | Generator | Next phase | Next kappa |
| --- | --- | --- | --- | --- |
| 0 | 0 | a | 0 | kappa |
| 0 | 1 | c | 2 | -kappa |
| 1 | 0 | b | 4 | -kappa |
| 1 | 1 | d | 1 | -kappa |
| 2 | 0 | c | 0 | -kappa |
| 2 | 1 | e | 1 | -kappa |
| 3 | 0 | d | 4 | -kappa |
| 3 | 1 | a | 3 | kappa |
| 4 | 0 | e | 4 | -kappa |
| 4 | 1 | b | 1 | -kappa |

Thus `Q f_t=Q` for both controls. Completeness uses weak, not necessarily
directed, connectivity of the two-edge graph. Here is the constructive
content of the frozen source proof. Every phase connects to `{1,4}` by
`0->2->1`, `2->1` or `3->4`. On these terminal sheets define

```text
V=(A,B,chi(z) C,chi(z) D0),  chi(1)=1, chi(4)=-1.
```

Its controlled terminal components are exactly `[V]` under common sign;
inside each, either phase and every r are reachable. Transient excursions
give the identifications

```text
H(alpha,beta,gamma,delta)=(beta,alpha,delta-1,gamma+1),
G_k(alpha,beta,gamma,delta)=(beta+3,alpha-3,delta+k,gamma-k),
G_k H(V)=V+(3,-3,k+1,-k-1),  k in F5.
```

Their legal weak paths and coordinate substitutions are in sections 3-4 of
the linked quotient proof. The translations generate exactly
`{(a,-a,b,-b):a,b in F5}`, the kernel of
`V -> (V1+V2,V3+V4)`. Together with common sign, they connect any two
terminal representatives having the same Q. Connecting the other phases
and using the ten-case invariant proves that the weak components are
precisely the fibres of Q.

For fixed `(z,r)` and an oriented value `kappa=(u,v)`, its two sum equations
leave A and C free, giving 25 solutions. Thus every oriented value has
125 preimages on each phase sheet and 625 on X. It follows that Q has
thirteen fibres: one of size 625 and twelve of size 1250. Each fibre meets
every phase sheet. In particular Q is onto.

Consequently, for every set Y,

```text
F f_0=F=F f_1 on X
    iff F=g o Q for a unique g:F5^2/{+1,-1}->Y.
```

Now let `L:Y->Y` be a bijection and restrict a reader on the whole Omega to
the form `R(n,x)=L^n F(x)`. Its exact intertwining with U is equivalent to

```text
F(d_n x)=F(x) for every n and x.
```

Both controls occur, already at n=0 and n=1. Cancellation of the bijection
`L^(n+1)` therefore gives the complete classification

```text
R U = L R on Omega, R(n,x)=L^n F(x)
    iff R(n,x)=L^n g(Q(x)), with arbitrary g.
```

The conclusion concerns this total separable class. It does not classify
all counter-dependent readers on Omega or equate one actual trajectory
with a whole weak component.

## 3. Conserved chart on the origin-zero reachable domain

The canonical synchronization theorem gives `z(E_3x)=1` for every head.
The restriction of E_3 to each initial phase sheet is a bijection onto
`X_3={z=1}`. Thus E_3 has 3125 fibres, each of size five and containing
exactly one head from each initial phase. At n>=3,

```text
X_n={x:z(x)=4-3 theta_(n-1)}
```

and every subsequent transition `d_n:X_n->X_(n+1)` is a bijection.

To avoid confusing the target L with the chart, denote the registered
chart by Lambda. Define the integer function and clock factors

```text
S0(0)=0, S0(m)=m-S0(floor(m/2)),
t_n=(-1)^(n-3), h_n=(-1)^(n+theta_(n-1)),
N_n=S0(floor((n-1)/2))-1.
```

For n>=3 its formula is

```text
Lambda_n(x)=(alpha,beta,gamma,delta,epsilon)
          =(t_n A,t_n B,h_n C,h_n D0,t_n r-N_n).
```

It is a bijection `X_n -> F5^5`, with inverse

```text
A=t_n alpha, B=t_n beta, C=h_n gamma, D0=h_n delta,
p1=3(A+C+2), p1p=3(A-C-2),
p4=3(B+D0+1), p4p=3(B-D0-1),
r=t_n(epsilon+N_n),
q=4-3 theta_(n-1)-A-B-r.
```

The canonical chart theorem proves
`Lambda_(n+1) d_n=Lambda_n` for every n>=3. Its proof is an all-clock
identity, not an extrapolation from a finite clock sample.

Extend the conserved label to every reachable time by

```text
ell_n(x)=Lambda_3(d_2 o ... o d_n(x)),  0<=n<3, x in X_n;
ell_n(x)=Lambda_n(x),                  n>=3,   x in X_n.
```

The early composition means the chronological transitions from tick n to
tick three. These are calculations on the supplied checkpoint, not future
measured inputs. Every ell_n is onto F5^5, since
`ell_n E_n=Lambda_3 E_3`, and

```text
ell_(n+1) d_n=ell_n on X_n for every n>=0.
```

The fibres of `ell_0` are exactly the E_3 fibres. No later reachable time
loses any further ell-label information.

## 4. Complete invertible-target amplitude class

**Theorem.** Fix any set Y and any bijection `L:Y->Y`. The readers
`R:D->Y` satisfying

```text
R(n+1,d_n(x))=L(R(n,x)) for every n>=0 and x in X_n
```

are exactly

```text
R(n,x)=L^n G(ell_n(x)),
```

where `G:F5^5->Y` is arbitrary and uniquely determined by R.

**Proof.** Put `a(x)=R(0,x)`. Iteration gives
`R(n,E_nx)=L^n a(x)`. If E_3x=E_3y, then
`L^3 a(x)=L^3 a(y)`, so a(x)=a(y) by injectivity. Thus a factors uniquely
through `ell_0`, giving a unique G. Every x in X_n is E_nx0 for some head,
so the iterated equation gives the stated formula. Conversely that formula
intertwines because `ell_(n+1)d_n=ell_n`. This proves existence,
completeness and uniqueness of the parametrization. Only injectivity of L
is needed for this argument; bijectivity is the frozen target class.

This is the canonical readback theorem applied to the initial amplitude.
There are at most 3125 distinct initial amplitude values. If Y contains
3125 distinct elements, this bound is attained by any injective G; for a
smaller finite Y the maximum is its cardinality. For a six-dimensional
characteristic-zero target, the image can span the target while remaining
finite. Spanning must not be described as surjectivity onto that carrier.

The classification works for every target bijection. The native dynamics
therefore do not select L within this class. For each stipulated L, every G
is admitted; neither the 3125-label theorem nor intertwining selects its
amplitudes. More structure or an independent selection rule is required
for a physical identification.

## 5. The thirteen-sector factor inside the five-coordinate chart

At n=3, `t_3=h_3=1` and `N_3=0`, and therefore

```text
ell_3(x)=(A,B,C,D0,r),
kappa(x)=(alpha+beta,gamma+delta).
```

At any n>=3, the synchronized phase satisfies
`chi(z)=(-1)^(theta_(n-1)+1)`. Thus
`chi(z) h_n=(-1)^(n+1)=t_n`, and

```text
kappa(x)=t_n (alpha+beta,gamma+delta).
```

Taking common-sign classes and using invariance through the first three
ticks gives, for every `(n,x)` in D,

```text
Q(x)=qbar(ell_n(x)),
qbar(alpha,beta,gamma,delta,epsilon)
      =[alpha+beta,gamma+delta].
```

The oriented map from F5^5 to F5^2 is linear and onto, with three free
coordinates in every fibre. Hence qbar has one fibre of size 125 and
twelve fibres of size 250. Multiplying these by the five heads of each
E_3 fibre recovers 625 and 1250 on the initial checkpoint domain.

Restriction to D of a whole-Omega separable reader from section 2 is
precisely the subclass `G=g o qbar` in section 4. Conversely every such G
extends by `R(n,x)=L^n g(Q(x))` to the whole-Omega separable class.
This is a strict subclass when Y has at least two elements: qbar identifies
distinct retained chart labels. Thirteen fixed-checkpoint sectors and 3125
counter-dependent labels are thus compatible results on different reader
classes, not competing claims about one information capacity.

## 6. Selector ports and exact loss of amplitude information

Summing the five generator formulas gives the complete phase maps

| Initial phase | 0 | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- | --- |
| T_0 | 0 | 4 | 0 | 4 | 4 |
| T_1 | 2 | 1 | 1 | 3 | 1 |

The first three native driver bits are 0,1,1. Therefore
`T_1 T_1 T_0` is constantly 1, giving z_3=1. Also theta_3=0, so the
selected index `i_3=z_3+2 theta_3` equals 1. Thereafter

```text
z_n=4-3 theta_(n-1),
i_n=4-3 theta_(n-1)+2 theta_n,  n>=3.
```

Suppose a single family of readers, with arbitrary counter dependence,
satisfies either

```text
r_n(z(E_nx))=L^n a(x) for every n and head x,
```

or the corresponding equation with i_n. At n=3 the left side is always
`r_3(1)`. Applying `L^-3` proves that a is constant. No linearity,
bounded counter, continuity, finite memory or finite target is assumed.
Conversely every constant a permits such a counter-only target orbit.

The complete selector history has a different but still exact bound.
Its trace recurrence is closed and depends only on z(x). Conversely its
initial trace and initial selected index both equal z(x), since theta_0=0.
Thus the complete trace history, the complete index history, and their
causal prefixes containing tick zero each separate exactly five source
classes. Any source amplitude obtainable from these histories has the
form `a(x)=b(z(x))`; every such amplitude can indeed be read from tick zero.
Arbitrary nonlinear or noncausal processing does not refine these classes.

If the same amplitude also factors through Q, then it is constant. Choose
one Q fibre; section 2 proves that it contains a head of every initial
phase. On these five heads the values b(z) must all equal the one value of
the Q factor. This is a common-factor obstruction, not a restriction on
the dimension of a chosen target containing five values.

There is a stronger exact completion from the inherited sheet theorem:

```text
x -> (ell_0(x),z(x))
```

is a bijection `F5^6 -> F5^5 x F5`. Indeed each ell_0 fibre is an E_3
fibre, and contains exactly one head of each phase. Surjectivity and
injectivity follow at once. Equivalently, for a pair `(l,z)`, recover
`y=Lambda_3^-1(l)` and then apply the unique inverse of `E_3` restricted
to the initial phase sheet z. The five explicit inverse words, for
z=0,1,2,3,4 respectively, are `ace,d,e,dbd,ebd`, composed right to left,
as proved in the frozen native-readback source.

It follows that any identity

```text
G(ell_0(x))=H(z(x)) for every head x
```

forces both functions to be constant: every pair of their arguments is
realized by exactly one head. Consequently a source amplitude admitting
both a current-full-checkpoint invertible-target reader from section 4
and a selector-history reader must be constant. This does not require
the stronger restriction that the first reader factor through Q.

The product decomposition is a bijection of source labels. It supplies no
probability distribution, probabilistic independence, physical preparation
law or material memory for the discarded initial phase.

## 7. Conditional additive obstruction in characteristic zero

Suppose, in addition to the source and target choices above, that the
amplitude assignment G is required to be additive from the declared chart
group `(F5^5,+)` to the additive group of a characteristic-zero vector space
W. Then for every label l,

```text
5 G(l)=G(5l)=G(0)=0,
```

so G(l)=0. Thus the only such additive reader has zero amplitude.
The same argument applies to any target additive group with no 5-torsion.

This conclusion is conditional on adopting chart-group addition. It is
not an obstruction to nonlinear lifts of the finite labels, to a different
declared source algebra, or to a separately supplied integer carrier.
The sign quotient defining Q does not inherit vector addition without
another definition.

## 8. What is and is not closed

The declared mathematical reader classes are complete: whole-Omega
separable amplitudes factor through thirteen sectors; arbitrary
counter-dependent invertible-target amplitudes on origin-zero reachable
states factor through the 3125 retained labels; current selector ports
give only constant amplitude; full selector histories retain precisely
initial trace. The retained label and initial trace jointly identify every
head, and have no nonconstant common factor. The quotient projection and
its 125/250 fibres explain the relationship without identifying the classes.

None derives a preferred target L, a preferred G, a physical preparation,
material recording, an event or an occurrence law. The given J-Hodge
operator can be substituted for L because it is invertible, but this
substitution alone does not derive that operator from U. The chart already
transforms the synchronized native dynamics into counter advance with a
constant label; this is why arbitrary target evolutions can be attached.
The target equations do not by themselves identify the counter or a
predictive coordinate with physical time.

All results are L1 and concern the explicitly stated ports and domains.
Finite exact audits check the formulas and finite carriers; the all-clock
and arbitrary-target conclusions rest on the proofs above and their frozen
canonical dependencies.
