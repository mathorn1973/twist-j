# Exact two-copy cancellation and the vanishing global zero-current sector

**PUBLIC, NON-CANONICAL; candidate-T written derivations.**
Working item C-PHOTON-BCHI-DIRECT-BOUND-N, issue #1143.
Author: A. M. Thorn. Date: 24 September 2026. Apache-2.0.
Public basis: Canon v91, main
`65195ab6ff6da1dcd3df17666238e16801b21838`, after #1157.

**No full-measure current-decay estimate or positive P1 gap is obtained.**
There are two new quantitative statements. A completely specified fiber
of two original copies has signed difference-current correlation
`(3/5)^(D+1)`, because opposite neutral cap pairs permit cancellation that
fixed face support forbids. Separately, the full original measure satisfies

```
P_mu(j identically zero) <= (1+2^-41)^(-floor(L/4)^4).    (A)
```

The entire normalized Fourier second-moment contribution of that global
zero-current sector obeys the same vanishing bound. This does not remove
neutral components inside configurations with currents. It prevents a
bare zero-sector comparison from supplying a surviving transverse floor.

Use exactly the measure and orientation convention of
[CONNECTED-CURRENT.md](CONNECTED-CURRENT.md):

```
mu_L(n)=Z_L^-1 2^(-|supp n|),
n in {-1,0,1}^P,   partial n=0 mod5,   j=partial n/5,
L even, L>=4,   V=L^4.
```

The aligned construction and its signed slices are from
[SIGNED-SLICES.md](SIGNED-SLICES.md). The current objective remains the
original ordered-profile inequality `b_lower > 25 chi_upper`.

## 1. Two independent copies and the restriction to be computed

Take n^(1),n^(2) independently from mu_L and put
`d_j=j^(1)-j^(2)`. Global reversal gives zero current means, and independence
gives the exact unconditional identity

```
Cov_mu(j_e,j_f)=(1/2) E_{mu x mu}[d_j(e)d_j(f)].          (1)
```

For D>=3, L=2D+4 and b=(D+1)e_1, recall

```
a(x)=partial[-c_012(x)+c_012(x-e_2)
             -c_013(x)+c_013(x-e_3)]-5p_01(x),
s=n_D=a(0)+a(b)-partial sum_{r=1}^D c_012(r e_1).
```

Let S=supp(s), N=|S|=4D+40. Define the D+1 previously absent cross-section
caps `q_r=p_02(r e_1)`, 1<=r<=D+1, and let Q be their face set. Put P_D=S
union Q, and let H_D contain P_D and every face sharing an edge with P_D.
The local fiber E_D is the following event in the actual product measure:

```
n^(1)+n^(2)=s on P_D;
n^(1)=n^(2)=0 on H_D outside P_D;
all faces outside H_D are summed in both copies.        (2)
```

In particular, on S a face with s_p=+1 or -1 must belong wholly to one
copy. On each cap the allowed pair is (0,0), (+1,-1) or (-1,+1).
Both copies separately obey every original mod-five edge constraint.
The zero halo in (2) is essential; fixing only their local sum would allow
uncontrolled exterior connections. This is conditional in the original
measure, with no arbitrary nonzero exterior conditioning theorem assumed.

## 2. Complete fiber classification

Introduce D+2 mod-five-closed chains

```
C_0=a(0),
C_r=-partial c_012(r e_1),             1<=r<=D,
C_{D+1}=a(b).
```

Their sum is s. After cap faces are omitted, their supports are disjoint
segments: endpoint segments have 20 faces each and each interior segment
has four lateral faces. The restrictions to P_D have the unique form

```
n^(1)|P_D=sum_{i=0}^{D+1} x_i C_i,
n^(2)|P_D=sum_{i=0}^{D+1} (1-x_i) C_i,
x_i in {0,1}.                                         (3)
```

To prove completeness, first examine edges not belonging to a cap. At a
neutral degree-two edge the opposite signed incidences force its two S
faces into the same copy; a nonempty proper allocation has boundary +1
or -1, which is not divisible by five. At an untouched degree-five edge,
all five signed incidences agree, so only allocating none or all five to
a copy is possible. The four lateral faces of every tube cell are linked
by their four longitudinal degree-two edges. Each endpoint patch remains
connected by these constraints after its cap is removed: the remaining
three charged central edges tie the central face and the other cups,
while the opened cup's outer cap and three side faces remain joined by
their uncut neutral edges. Thus exactly D+2 monochromatic segments remain.

On cap q_r, write z_r=n^(1)(q_r), so n^(2)(q_r)=-z_r. At each of its
neutral direction-two boundary edges the mod-five condition, whose
absolute sum is less than five, forces

```
z_r=x_{r-1}-x_r.                                       (4)
```

This also satisfies the remaining cap edges, including the charged
endpoint seam edge. An independent direct check is that each C_i has
boundary divisible by five, so every binary combination in (3) is
closed modulo five. Equation (4) lies in {-1,0,1}; all non-cap faces lie
in exactly one segment. Hence all combinations are ternary and admissible.
No additional cap value or allocation is possible. There are precisely
`2^(D+2)` ordered local allocations for each allowed exterior pair.

The halo isolates every possibly occupied patch face from exterior faces.
Each patch in (3) is separately closed modulo five, so the exterior
constraints are the same for every local allocation. If Z_emptyH is the
single-copy partition with all faces of H_D fixed to zero, the exterior
factor is exactly Z_emptyH squared. It cancels in the conditional law.

This goes beyond exchanging copies with each unordered face pair fixed.
With that stronger restriction on the pair (s,0), neutral degree-two
and degree-five constraints force the entire connected S into one copy.
Only (s,0) and (0,s) survive, with no endpoint cancellation. Equation (2)
allows the necessary transitions `(0,0) <-> (+1,-1)` on the caps with
their exact, unequal weights retained.

## 3. Exact partition sum and signed decay in this fiber

Every S face contributes 1/2 to the product weight, regardless of copy.
A cap contributes one when adjacent bits agree and 1/4 when they differ.
If w(x) counts neighboring unequal bits, the pair's unnormalized weight is

```
2^-N 4^-w(x).
```

The conditional law is therefore exactly the open two-state chain with
transition weight matrix

```
T = [[1, 1/4], [1/4, 1]].
```

This matrix describes the derived conditional law, not a new physical
model. Its constant and alternating eigenvectors have eigenvalues 5/4
and 3/4. Summing all binary strings gives

```
Z_local = 2^(1-N) (5/4)^(D+1),
P_{mu x mu}(E_D) = Z_local (Z_emptyH/Z_L)^2.             (5)
```

Choose orientation-zero edges e=(0,0) and f=(b,0), each with total
current s equal to -1. In (3) they have
`d_j(e)=1-2x_0`, `d_j(f)=1-2x_{D+1}`. Copy exchange makes their conditional
means zero. The complete weighted sum, with no omitted fiber states, is

```
E[d_j(e)d_j(f) | E_D] = (3/5)^(D+1),                   (6)
sum_{local allocations} weight*d_j(e)d_j(f)
    = 2^(1-N) (3/4)^(D+1).                             (7)
```

Thus the aligned geometric obstruction to independent fixed-support
reversal does admit exponential signed cancellation when these neutral
cap pairs are summed. This is a calculation in one restricted fiber.
Other pointwise sums, exterior face pairs and arbitrary charged components
have not been bounded. Their signed contributions cannot be dropped from
(1), so (6) is neither an upper nor a lower bound for the full covariance.

Conditioning also destroys the independence of the two copies. For
example inside E_D,

```
E[j^(1)_e]=E[j^(1)_f]=-1/2,
E[j^(1)_e j^(1)_f]=(1+(3/5)^(D+1))/4,
Cov(j^(1)_e,j^(1)_f | E_D)=(3/5)^(D+1)/4.
```

Consequently `(1/2)E[d_j(e)d_j(f)|E_D]` must not be called the conditional
single-copy covariance. Equation (1) applies before conditioning; averaging
all its conditional contributions would require controlling every fiber.

## 4. The globally zero-current sector has exponentially small weight

Let Q_0 be the complete partition sum with integer boundary zero and
nu_0 its normalized measure. It is exactly the continuous-angle integral

```
Q_0 = sum_{partial n=0} 2^(-|supp n|)
    = integral_{U(1)^E} product_p [1+cos((dA)_p)] dA.
```

The character expansion retains all winding integer-closed surfaces.
For any set B of faces, deleting its plaquette factors restricts n to
zero on B. Positivity and `0<=1+cos(theta)<=2` imply

```
nu_0(n|_B=0) >= 2^(-|B|).                              (8)
```

Set k=floor(L/4)^4. Place k copies of the 21-face four-cup support at
basepoints `x_a=1+4r_a`, 0<=r_a<floor(L/4), in each coordinate. Each lies
within x+[-1,1]^4, so these supports S_i are vertex-disjoint and fit
without wrapping, including when L is not divisible by four. Their
central plaquette loops J_i=-partial p_i are edge-disjoint. Write a_i for
the translated four-cup chain; partial a_i=5J_i.

For any n_0 with partial n_0=0 and any subset I on which n_0|_{S_i}=0,
insert independent signs:

```
n=n_0+sum_{i in I} sigma_i a_i,     sigma_i in {+1,-1}.
```

It is ternary and admissible, with weight `2^(-21|I|)` times the original
background weight and current `j=sum_{i in I} sigma_i J_i`. That current
uniquely identifies I and every sign, since the loops are edge-disjoint.
Subtracting the insertions recovers n_0. The map is therefore injective
into the full original state space. No surrounding empty shield is
needed; component isolation is not claimed.

Summing this family and using simultaneous emptiness, not independence,

```
Z_L/Q_0 >= E_nu0 product_i (1+2^-20 1_{n_0|S_i=0})
        = sum_I 2^(-20|I|) nu_0(n_0|_{union_{i in I}S_i}=0)
        >= sum_I 2^(-41|I|)
        = (1+2^-41)^k.                                 (9)
```

Since `P_mu(j=0)=Q_0/Z_L`, this proves (A) for every even L>=4. The
constant is small but fixed and positive, and k grows proportionally to V.

## 5. Even the complete Fourier contribution of that sector vanishes

For an arbitrary real face source g, the same finite Fourier expansion
and modulus identity used in the earlier source comparison give

```
E_nu0 exp(<n,g>)
 <= E_nu0 product_{p:n_p=0} cosh(g_p).                   (10)
```

Indeed the source integral contains factors
`1+cos((dA)_p-i g_p)`. Their moduli are
`cosh(g_p)+cos((dA)_p)>=0`. Expanding this product and integrating imposes
the original integer-zero constraints, with the cosh factor only on
empty faces. This proves (10) without a contour shift or limit exchange.

At g=0 equality holds and both linear derivatives vanish by reversal.
Taking any directional second derivative of the nonnegative difference
in (10) yields the matrix bound

```
C_n^nu0 <= diag nu_0(n_p=0) <= I.                       (11)
```

For a single-orientation Fourier vector f_p=exp(-iq c_p), its squared
norm is V. The real symmetric matrix bound also holds for its complex
quadratic form, so `0<=S_n,II^nu0(q)<=1`. Exactly

```
(1/V) E_mu[|F_I(n;q)|^2 1_{j=0}]
    = (Q_0/Z_L) S_n,II^nu0(q)
    <= (1+2^-41)^(-floor(L/4)^4).                       (12)
```

This tends to zero uniformly in every allowed q, before any infrared
limit. Thus even an excellent transverse lower bound in nu_0 cannot be
transferred through the bare factor Q_0/Z_L to obtain a surviving floor
in the full model. A comparison retaining the charged sectors in both
numerator and denominator would be necessary. No such estimate is proved.

The event j=0 is global. A configuration outside it may contain neutral
paired components and large neutral fillings within charged components.
Equations (9)-(12) do not exclude their transverse response and do not
contradict a massless phase.

## 6. What the further attempts do and do not establish

Neither result supplies the required numerical comparison. The cap chain
exhibits the desired cancellation mechanism on a completely classified
fiber; a bound after summing all geometries and exterior pairs is missing.
The zero-sector theorem eliminates a direct reference-sector transfer;
it does not establish a lower bound in the charged background.

There is also a quantitative limitation of the simple isolated-neutral-box
insertion route. The boundary of an R-by-R-by-R 012 box has 6R^2 faces and
12R^2 degree-two edges. Its edge-sharing face neighborhood has at most
54R^2 faces. Applying the earlier empty-neighborhood insertion proof gives
the certified transverse contribution

```
2^(1-60R^2) 4R^4 sin^2(tR/2).
```

Even summing these certificates over all integer R is bounded above by
`t^2 sum_{R>=1} 2^(1-60R^2) R^6`, which tends to zero. This bounds the
explicit certificate, not the actual total neutral response. No claim
that large neutral surfaces are negligible is made.

Full signed charged-face absolute summability is likewise not adopted as
a requirement: a component with a fixed small current can carry an
arbitrarily large neutral transverse filling. Controlling that entire
component would ask for more than control of its longitudinal current
response. The exact Ward split and #1157 slice quotient preserve this
distinction but do not yet yield an evaluated uniform upper constant.

The finite audit in [REPLICA-PREREG-20260924.md](REPLICA-PREREG-20260924.md)
checks geometric classification, exact rational fiber sums and the
insertion packing. It does not enumerate the full measure or prove the
all-volume results by finite sampling. Separate agents reviewed the
arguments with shared sources; this is not blind external acceptance.
All results remain candidate-T/C, NON-CANONICAL. P1, P2, spectral S7 and
the canonical phase obligation remain open.
