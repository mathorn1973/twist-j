# Selected outgoing TT vector state: exact proof

**PUBLIC; candidate-T, L1, NON-CANONICAL.** All conclusions below are
conditional on the choices in `MODEL.md` and the question frozen in
`PREREG.md`. Public lock: #1097. The authority base is Public Canon v90.
The existing isolated K1 emission and its ten-word source law are retained.
No physical clock, scalar curvature perturbation, experiment or cosmological
tensor-to-scalar ratio is supplied by this proof.

The proof establishes every all-counter assertion independently of finite
execution. The exact verifier audits finite identities and fixtures; it does
not replace these quantifiers by a finite horizon.

## 1. The unchanged source reduces to seven outgoing tensor histories

Let `e_r`, `r in Z/5`, be the marked coordinate vectors. Retain the ten words
and weights of `DEF-K1-LINEAR-METRIC` and
`DEF-K1-ISOLATED-TT-EMISSION`. For a word `w`, put

```text
u0=w2-w0,  u1=w3-w1,
H_t=(e_(u_t)+e_(u_t+1))/2,
Phi_w=H1-H0,
d1=(e0-e2)/2,  d2=(e4-e1)/2.
```

The complete source table is

| Word | Weight | Source `Phi_w` |
|---|---:|---|
| 0010 | 1/12 | d1 |
| 0011 | 1/12 | 0 |
| 0100 | 1/12 | d2 |
| 0101 | 1/12 | 0 |
| 0110 | 1/6 | d1+d2 |
| 1001 | 1/6 | -(d1+d2) |
| 1010 | 1/12 | 0 |
| 1011 | 1/12 | -d1 |
| 1100 | 1/12 | 0 |
| 1101 | 1/12 | -d2 |

This is direct substitution into the inherited source map. In particular,
each nonzero source has its negative with the same mass. The zero source has
total mass `1/3`; source signs are not independently redrawn at later times.

Use the unchanged symmetric rational operator

```text
L=[188I-29(S+S^-1)-65(S^2+S^-2)]/324,
S f(r)=f(r+1).
```

Define rational operators

```text
A0=A1=0,  A2=I,
A_(m+1)=(2I-L)A_m-A_(m-1),  m>=2.
```

The existing isolated outgoing field is exactly

```text
h_m(w)=A_m Phi_w.
```

Indeed, it has `h0=h1=0`, `h2=Phi`, and satisfies the inherited source-off
recurrence thereafter. Induction gives uniqueness, rationality and literal
prefix compatibility for every counter. Since every `Phi_w` has zero sum
and `L` annihilates constants, every `h_m(w)` has zero spatial sum.

Write `x_m=A_m d1` and `y_m=A_m d2`. The law of the entire tensor history,
before any vector lift, is therefore the following seven-atom law:

```text
0                         mass 1/3,
each of +x and -x          mass 1/12,
each of +y and -y          mass 1/12,
each of +(x+y), -(x+y)     mass 1/6.
```

The seven histories are distinct because their slices at `m=2` are distinct.
The law remains the pushforward of the original ten labelled words; grouping
equal outputs does not change their source masses.

## 2. No active packet vanishes at a later outgoing slice

The unitary transform is

```text
F_kr=z^(kr)/sqrt(5),  z=exp(2 pi i/5),  k,r in Z/5.
```

The nonzero eigenvalues of `L` are

```text
lambda_1=lambda_4=(235+18sqrt(5))/324,
lambda_2=lambda_3=(235-18sqrt(5))/324.
```

They lie strictly between zero and four. Define `omega_k in (0,pi)` by
`2 cos(omega_k)=2-lambda_k`. On the nonzero Fourier slots, solving the scalar
recurrence gives, for every `m>=2`,

```text
t_m(k)=sin((m-1)omega_k)/sin(omega_k),
F h_m(k)=t_m(k) F Phi(k).
```

The formula agrees with `t_1=0,t_2=1` and the same recurrence, which proves it
without extrapolation from a finite prefix. On the constant slot the operator
`A_m` has eigenvalue `m-1` for `m>=1`, but the source has zero constant slot.

For completeness, `t_m(k)` never vanishes at a nonzero slot when `m>=2`.
If it did, `omega_k/pi` would be rational, so `exp(i omega_k)` would be a root
of unity. The sum of that root and its inverse would be an algebraic integer.
But

```text
2 cos(omega_1)=(413-18sqrt(5))/324,
2 cos(omega_2)=(413+18sqrt(5))/324
```

are quadratic conjugates whose field trace is `413/162`, not an integer.
An algebraic integer has integer field trace. This is a contradiction.

Consequently `A_m` is invertible on the mean-zero subspace at every `m>=2`.
Every active packet has a nonzero slice at each such counter. Its zero spatial
sum then forces at least one positive and at least one negative entry on that
slice. This is stronger than nonzero emission only at onset, and is proved by
the spectral argument rather than by a finite run.

## 3. Two persistent signs define the complete vector law

For each entire isolated packet choose two independent fair signs
`epsilon_+,epsilon_- in {+1,-1}`, independent of the source word. They are
chosen once, persist for the whole history, and are not refreshed on passing
through a zero or a sign change. Put

```text
a_p(w)=sqrt(max(h_m(w,r),0)),
b_p(w)=sqrt(max(-h_m(w,r),0)),  p=(r,m),

v_p(w,epsilon)=epsilon_+ a_p(w)+i epsilon_- b_p(w).
```

Every square root here is the nonnegative real root. At a zero both components
are zero. Since `a_p b_p=0`,

```text
v_p^2=a_p^2-b_p^2=h_m(w,r),
|v_p|^2=a_p^2+b_p^2=|h_m(w,r)|.
```

Thus the vector square equals the unchanged emitted tensor field at every
site and every counter, including all zeros. This is a complete joint state
law on all times, not a list of unrelated one-time marginal laws.

The labelled probability space has forty atoms `(w,epsilon_+,epsilon_-)`,
each with mass `nu(w)/4`. The full vector-history pushforward has exactly
twenty-five atoms. All static words and signs give the single zero history
of mass `1/3`. The four active words with weight `1/12` give sixteen histories
of mass `1/48`; the two active words with weight `1/6` give eight histories
of mass `1/24`. For a fixed active word the four sign choices give distinct
histories because both `a` and `b` are nonzero already at onset. Histories
from distinct nonzero tensor histories cannot coincide because squaring
would then give the same tensor history. This proves the exact support count.
The same seven tensor and twenty-five vector support counts hold on every
individual slice `m>=2`: `A_m` is injective on the source span, and each
active slice contains both positive and negative entries by section 2.

For a finite prefix, its probability is the sum of masses of the labelled
atoms with that prefix. Fibres partition the finite probability space.
Restriction to a shorter prefix merely joins these fibres, proving
normalization and compatible prefix marginals for every finite horizon.

## 4. What symmetry selects, and what it does not

Fix one active real tensor history `h`. Its four selected sign-coherent lifts
are the roots with one common sign on all positive entries and one common
sign on all negative entries, over the whole history. On this set consider

```text
R(v)=-v,  C(v)=conjugate(v).
```

These commute, square to the identity, and preserve `v^2=h`. Their group is
the Klein four group. In sign coordinates, `R` changes both signs and `C`
changes only `epsilon_-`; hence their action on the four lifts is transitive
and free. A probability law invariant under both maps must assign the same
mass to all four lifts. Normalization forces each mass to be `1/4`.

There is also a minimality statement under these precisely stated invariance
requirements. For any root history of this active real `h`, some entry is
nonzero real and another is nonzero imaginary. Consequently none of
`R,C,RC` fixes that history. Each orbit has four elements. Every nonempty
finite-support invariant law on root histories therefore has support at
least four. The selected coherent law attains this lower bound.

This does not derive sign coherence, the invariance requirement, or a
physical preparation from `J`. Other four-element or larger invariant orbits
with different signs at different points exist if sign coherence is dropped.
They can change vector correlations while leaving the squared tensor field
unchanged. The chosen class and its law are explicit inputs; only uniqueness
inside that class and the stated symmetry lower bound are conclusions.

### Covariance of the common-polarization-line family

In a rotated marked frame put

```text
H_p=exp(2i alpha) h_p,
V_p=exp(i alpha)[epsilon_+ sqrt(h_p^+)
                 +i epsilon_- sqrt(h_p^-)],
h_p^+=max(h_p,0),  h_p^-=max(-h_p,0).
```

Then `V^2=H`. The alternative description of the same tensor history by
`(alpha+pi/2,-h)` gives the same vector law: exchanging the positive and
negative roots corresponds to the bijection
`(epsilon_+,epsilon_-)->(-epsilon_-,epsilon_+)` of the four equally weighted
sign pairs. Changing `alpha` by `pi` similarly flips both signs. These are
all ambiguities in describing a nonzero common complex line by a real field
and a half-angle. The zero field has the unique zero vector law.

A spatial frame rotation through `beta` sends `V` to `exp(i beta)V` and `H`
to `exp(2i beta)H`. Reflection conjugates both and sends
`alpha->-alpha`, `epsilon_-->-epsilon_-`. Therefore the selected law is
`O(2)`-covariant on this common-polarization-line family. The fixed plus-frame
law is not asserted to be invariant under every rotation; it has the stated
discrete symmetries. No general independently polarized field at each point
has been silently admitted into this selection.

Writing `V=V1+i V2`, the usual square identities hold pointwise:

```text
H_plus=V1^2-V2^2,  H_cross=2V1V2,
det([[1+H_plus,H_cross],[H_cross,1-H_plus]])=1-|H|^2.
```

The first pair is the doubled-angle spin-two representation. These identities
do not assert that the metric is positive at every amplitude or that the
vector itself solves an independently chosen linear propagation equation.

## 5. All moments, including unequal-time vector moments

For any finite collection of points and nonnegative integer exponents
`A_p,B_p`, the complete real-component moment formula is

```text
E[product_p V1_p^A_p V2_p^B_p]
 = 1_(sum A_p even) 1_(sum B_p even)
   sum_w nu(w) product_p a_p(w)^A_p b_p(w)^B_p.
```

Here `0^0=1`. This follows directly from the two independent persistent sign
averages. In other frames the same formula determines every moment after
the declared real linear rotation. Thus moments of every degree and every
finite selection of counters are specified by a realizable positive law.
There is no Gaussian closure assumption.

In particular `E[v_p|w]=0`, so `E[v_p]=0`. In the marked plus frame,

```text
C_v(p,q)=E[v_p conjugate(v_q)]
 =sum_w nu(w)[a_p(w)a_q(w)+b_p(w)b_q(w)],

P_v(p,q)=E[v_p v_q]
 =sum_w nu(w)[a_p(w)a_q(w)-b_p(w)b_q(w)]=0.
```

The last equality uses the exact equal-mass pairing `h->-h` in section 1,
which exchanges `a` and `b`. The cross sign averages vanish independently.
The persistent signs are essential: no Kronecker delta in site or counter
may be inserted into these kernels. Their Fourier covariance matrices,
including off-diagonal mode entries, are obtained by applying the fixed
unitary `F` on the indicated site indices. Spatial stationarity is not an
assumption. In particular, `P_v` vanishes in every pair of counters and modes,
while the complete covariance need not be diagonal in modes.

All displayed second moments are finite sums of square roots of nonnegative
rational numbers. They are exact real algebraic values, not generally
rational numbers. At the same point,

```text
E[V1_p^2]=E[V2_p^2]=E[|h_p|]/2,
E[V1_p V2_p]=0.
```

## 6. The fourth-order TT contraction and non-Gaussian boundary

The paired source law gives `E[h_p]=0`. Hence the connected quadratic-output
kernels are exactly

```text
K_h(p,q)=E[v_p^2 conjugate(v_q^2)]=E[h_p h_q],
P_h(p,q)=E[v_p^2 v_q^2]=E[h_p h_q].
```

Put

```text
C_Phi=(d1 d1^T+d2 d2^T)/6
       +(d1+d2)(d1+d2)^T/3.
```

Then the full two-time tensor kernel is

```text
C_h(m,n)=A_m C_Phi A_n^T.
```

In the marked plus frame this is the `++` entry of the real polarization
covariance, and the cross and mixed entries vanish. In a rotated frame it
becomes `u u^T C_h`, where `u=(cos(2alpha),sin(2alpha))`. Its polarization
trace is unchanged.

The vectors `d1,d2` are orthogonal and each has squared norm `1/2`. On their
span the two nonzero eigenvalues of `C_Phi` are `5/12` and `1/12`.
In particular `tr C_Phi=1/2`. The stacked tensor covariance of every prefix
containing onset has rank exactly two: all samples are linear combinations
of the two stacked histories `x,y`, and their onset slices are independent.
At each individual slice `m>=2` the rank is also two, by section 2.

The full real pair-of-points fourth tensor is supplied by the moment formula
above. For example,

```text
E[V1_p^2 V1_q^2]=E[h_p^+ h_q^+],
E[V1_p^2 V2_q^2]=E[h_p^+ h_q^-],
E[V2_p^2 V1_q^2]=E[h_p^- h_q^+],
E[V2_p^2 V2_q^2]=E[h_p^- h_q^-].
```

Any co-located factor `V1_p V2_p` vanishes. Subtracting products of the second
moments and contracting with the registered plus/cross quadratic matrices
gives the displayed connected kernel. This explicitly supplies the raw
moments needed by the normalization owner, rather than inferring them from
`C_v,P_v`.

There is a direct non-Gaussian witness at every point where `E|h_p|>0`.
The selected law has

```text
E[V1_p^2 V2_p^2]=0,
E[V1_p^2] E[V2_p^2]+2(E[V1_p V2_p])^2=(E|h_p|)^2/4>0.
```

The second expression is the centered Gaussian fourth-moment value, so Wick
closure is false there. Equivalently `E[v_p^4]=E[h_p^2]>0` while `P_v(p,p)=0`.
This is a witness for the selected law. It does not assert that all vector
states in any larger class are non-Gaussian. In particular, its pointwise
modulus is source-dependent; the older fixed-modulus theorem is not being
applied outside its hypotheses.

## 7. Action normalization and the primary-field boundary

Retain the public action coefficient `lambda=216 pi`. In the transverse
sector its free quadratic part is

```text
S_T[h]=A2_TT[h]/(2 lambda)
      =(1/(4 lambda)) sum_n,a
        [<Delta h_a,Delta h_a>-<h_a,Lh_a>],
a in {plus,cross}.
```

As in the public construction, this is a local variational expression with
finite-support interior variations, not a claim that the infinite on-shell
sum converges. Lapse, shift and the other metric variations belong to the
inherited full action and are not rederived by restricting first. The
existing transverse source stress remains `Phi_a/(2 lambda)` with its stated
impulse and complete-transfer convention.

The canonical quadratic field variable is

```text
q_a=h_a/sqrt(2 lambda).
```

Substitution makes the free kinetic coefficient `1/2` for each real
polarization. This identifies the tensor conversion used below and leaves
no floating normalization coefficient inside this selected convention.
It does not choose a scalar action or a physical state by itself. The state
is chosen separately in sections 1 and 3.

The compatible canonical vector readout is

```text
v_can=v/(2 lambda)^(1/4),
v_can^2=h/sqrt(2 lambda),
|v_can|^2=|h|/sqrt(2 lambda).
```

Thus applying the same vector rescaling to its square and its squared norm
gives the same field conversion factor. This does not introduce a second
action or independently determine a cosmological scalar mode.

The independent linear dynamics remain dynamics of the primary field `h`.
The lifted vector histories are then defined by their selected roots. This
order avoids the singular-pullback error. Indeed, for

```text
Q(v1,v2)=(v1^2-v2^2,2v1v2),
DQ(v)=2[[v1,-v2],[v2,v1]],
det DQ(v)=4(v1^2+v2^2).
```

The derivative is invertible away from zero and is the zero matrix at zero.
Varying a pulled-back action `S_T[Q(v)]` alone only gives
`DQ(v)^T (delta S_T/dh)=0`. At a zero vector this imposes no tensor equation.
It therefore cannot replace the independent primary-field recurrence at
the zero-start emission. The construction claims no autonomous linear
spin-one propagation or regular vector-only action inferred by that
substitution. Representation weight one and the registered label `c(1)=0`
are not being used as a new vector evolution equation.

## 8. A declared scalar intensity comparison, with no new scalar dynamics

Define the spin-zero composite intensity and its mean by

```text
s_p=|v_p|^2=|h_p|,
mu_s(p)=sum_w nu(w)|h_p(w)|.
```

It is invariant under the selected frame rotations and reflection. This is
an intensity observable of the same emitted field, not an independent
gravitational scalar perturbation. Its coefficient one is the usual squared
Euclidean doublet norm and is part of the frozen readout convention.

Its entire connected two-time kernel is

```text
C_s(p,q)=sum_w nu(w)|h_p(w)||h_q(w)|-mu_s(p)mu_s(q).
```

Mixed tensor-intensity connected moments vanish: replacing a source by its
equal-weight negative changes `h_p` in sign and leaves `|h_q|` unchanged.
This decorrelation is not independence; pointwise `s_p^2=h_p^2` exactly.

For each counter and the fixed unitary transform define raw connected powers

```text
T_m(k)=E[|F h_m(k)|^2],
I_m(k)=E[|F(s_m-mu_s,m)(k)|^2].
```

The tensor mean is zero. The intensity mean must be subtracted; discarding
that subtraction changes the comparison. A tensor polarization trace gives
the same `T_m` in every common rotated frame, with no additional factor two.
The selected normalized powers and finite ratio are

```text
P_T^fin(k,m)=T_m(k)/(2 lambda),
P_I^fin(k,m)=I_m(k)/(2 lambda),
R_TI(k,m)=P_T^fin/P_I^fin=T_m(k)/I_m(k),  whenever I_m(k)>0.
```

The intensity readout is the declared norm with coefficient one. Once it is
chosen, its displayed factor follows from the same canonical vector rescaling
as the tensor square, not from independently tuning a scalar coefficient.
This is still not a scalar-action derivation. These definitions specify exact quantities
for all five marked slots at every counter. They do not identify a site with
a cosmological coordinate, a counter with physical time, a slot with a
cosmological wave number, or `P_I^fin` with `P_S`.

### Positive denominator at every nonzero outgoing counter

At `m=0,1` both fields vanish identically; the ratio is `ZERO_SUPPORT` and is
not assigned a zero value. At every `m>=2`, however, `I_m(k)>0` for all five
slots.

To prove this, select any active packet. Section 2 gives a nonzero rational
zero-sum vector `h_m`. If `|h_m|` were constant, that constant would be
positive and the five entries of `h_m` would each equal it or its negative.
An odd number of such entries cannot have sum zero. Thus `|h_m|` is not
constant.

For a nonzero slot `k`, `z^k` has minimal polynomial
`1+X+X^2+X^3+X^4` over the rationals. A rational vector `a` satisfies
`sum_r a_r z^(kr)=0` only if all five coefficients are equal: its degree at
most four polynomial must be a constant multiple of that minimal polynomial.
Applying this to `a=|h_m|` proves its Fourier value is nonzero at every
nonzero slot. At slot zero its Fourier value is positive by nonzero
nonnegative entries.

The source law also has the zero packet with mass `1/3`. The intensity
Fourier random variable therefore takes both zero and a nonzero value with
positive probability at every slot. Its connected variance is strictly
positive. This proves the denominator assertion at all counters, not merely
on the finite audit domain. Similarly `T_m(k)>0` for `k!=0` by its onset
value in section 9 and the nonvanishing transfer; `T_m(0)=0` identically.
Hence `R_TI(0,m)=0` and `R_TI(k,m)>0` for `k!=0,m>=2`.

At each finite counter all entries used in these two connected covariances
are rational. Their diagonal Fourier powers are in `Q(sqrt(5))`: imaginary
terms cancel by symmetry of the real covariance matrix, and the remaining
cosines are fifth-root real parts. The finite ratio is therefore an exactly
determined element of that field. The normalization factor `2 lambda`
cancels because the same conversion was explicitly selected on both
readouts; this cancellation is not a statement about a cosmological scalar.

## 9. Exact onset powers and their ratios

At `m=2` put

```text
a=|d1|=(e0+e2)/2,
b=|d2|=(e4+e1)/2,
c=a+b.
```

The supports of `d1,d2` are disjoint, so `|d1+d2|=a+b`. The intensity law at
onset has outputs `0,a,b,c` of masses `1/3,1/6,1/6,1/3`. Thus

```text
mu_s=c/2=(e0+e1+e2+e4)/4,
C_s=(aa^T+bb^T)/6+cc^T/12.
```

Let `theta=2 pi k/5`. With the declared positive-exponent Fourier convention,

```text
F d1(k)=(1-z^(2k))/(2sqrt(5)),
F d2(k)=z^(4k) F d1(k),
F a(k)=(1+z^(2k))/(2sqrt(5)),
F b(k)=z^(4k) F a(k).
```

Consequently

```text
T_2(k)=[(1-cos(2theta))/10] [1+(2/3)cos(theta)],
I_2(k)=[(1+cos(2theta))/10] [(3+cos(theta))/6].
```

Using `cos(2pi/5)=(sqrt(5)-1)/4` and
`cos(4pi/5)=-(sqrt(5)+1)/4` gives the full table:

| Marked slots | Raw connected `T_2` | Raw connected `I_2` | `R_TI(k,2)` |
|---|---|---|---|
| 0 | 0 | 2/15 | 0 |
| 1,4 | `(3+sqrt(5))/24` | `(7-2sqrt(5))/240` | `10(31+13sqrt(5))/29` |
| 2,3 | `(3-sqrt(5))/24` | `(7+2sqrt(5))/240` | `10(31-13sqrt(5))/29` |

The corresponding normalized entries in the second and third columns are
their displayed values divided by `2 lambda`. Every intensity entry is
positive. Parseval gives the independent aggregate identities

```text
sum_k T_2(k)=1/2,
sum_k I_2(k)=1/4.
```

The first is `E||Phi||^2`. The second is
`E|| |Phi| ||^2-||mu_s||^2=1/2-1/4`. At later counters the tensor power has
the exact formula

```text
T_m(k)=t_m(k)^2 T_2(k),  k!=0,
T_m(0)=0.
```

The intensity uses the complete inherited ten-word pushforward and absolute
value before Fourier transformation. It is not in general propagated by
this same linear scalar mode factor. Its formula in section 8 is total and
needs no new parameter, averaging law, branch or horizon-dependent choice.

## 10. Scope of the completed object

The selected construction now supplies one complete outgoing vector law,
its all-counter unequal-time covariance and pseudo-covariance, every fourth
moment, the registered quadratic TT readout, the inherited tensor action
coefficient, and one explicitly defined finite spin-zero intensity
comparison. Source preparation weights, temporal coupling and branch signs
are all accounted for. Its conditional conclusions need no empirical target
number and no fitted coefficient.

It does not establish that these are Nature's vector states or a complete
physical normalization among all admissible theories. In particular the
intensity comparator is not a cosmological scalar power. The registered
owner `TT-VECTOR-STATE-NORMALIZATION` keeps its full physical `r_T(k)`
decision clause, including the scalar action/state, coordinates, epoch and
mode identification that would be needed for that different ratio. Nor does
the construction derive a material emitter, a repetition law, an onset clock,
an outgoing nonlinear geometry, a detector or an SI conversion. Those bounds
do not prevent the selected finite theory and all its stated observables
from being mathematically complete at the declared L1 scope.
