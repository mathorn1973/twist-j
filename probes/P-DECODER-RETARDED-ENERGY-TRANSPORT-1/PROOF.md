# Exact retarded transport and local energy: conditional proof

**NON-CANONICAL / PROOF-FIRST / RESULT-EXPOSED / L1 MATHEMATICAL SCOPE.**

This supplies the uniform argument for
`P-DECODER-RETARDED-ENERGY-TRANSPORT-1`, reserved in
[#822](https://github.com/mathorn1973/twist-j/issues/822). It assigns no public
claim status and records no execution. The public basis is
`2d33c38fc0e9a4cfb0e60062eb8d628d46ea9e97`, with ACTIVE Public Canon v76.
The claim is conditional on the displayed scalar dictionary and the explicit
source and readout choices. Finite conformance tests audit this argument;
they do not replace its quantifiers over all finite supports and finite cuts.

## 1. Carrier, operator and complete finite sums

Let

```text
D3 = {x in Z^3 : x_0+x_1+x_2 is even},
V = C_c(D3,Q),
<a,b> = sum_x a_x b_x,       ||a||^2 = <a,a>.
```

Thus every state has finite support and rational coefficients. This is a
restricted mathematical carrier, not all of the Canon's `Map(D3,C)`, on
which the energy sum need not exist. Put

```text
N = union of the complete D3 shells of squared norms 2,4,8,10,16,
c_z = w_|z|^2 / 324,        (w_2,w_4,w_8,w_10,w_16)=(6,1,15,1,1),
(La)_x = sum_(z in N) c_z (a_x-a_(x+z)),
B = {0} union N.
```

The shell representatives are `(1,1,0)`, `(2,0,0)`, `(2,2,0)`, `(3,1,0)`,
and `(4,0,0)`, with all distinct signed coordinate permutations. Their
cardinalities are respectively `12,6,12,24,6`. Hence `N=-N`, `c_z=c_-z>0`,
and

```text
S = sum_z c_z = (12*6+6+12*15+24+6)/324 = 8/9.
```

For adjacent `y=x+z`, abbreviate `c_xy=c_z`. All edge sums below use all
60 neighbours at each vertex. A sum over both `x` and `y` consequently
counts each unoriented edge twice; the factors below use this convention.

Finite support and finite range justify every rearrangement. Reversing an
edge proves self-adjointness and the exact identity

```text
<a,Lb> = (1/2) sum_(x,y) c_xy (a_y-a_x)(b_y-b_x).
```

In particular `L>=0`. The elementary inequality
`(a_y-a_x)^2<=2(a_x^2+a_y^2)` gives

```text
0 <= <a,La> <= 2S ||a||^2 = (16/9)||a||^2.
```

Also `||La||<=2S||a||` follows directly from the triangle inequality and
translation invariance of the norm. No Fourier completeness, continuum
limit or spectral approximation is needed.

## 2. Forced step and conserved positive energy

The stored pair is `(u,v)=(previous,current)`. Given any `f in V`, define

```text
w = 2v-u-Lv+f,             (u,v) -> (v,w).
```

The Canon's two-slice ordering is `(current,previous)`; conversion is the
explicit swap `(u,v)->(v,u)`. It does not change the evolution. All three
fields `u,v,w` remain in `V`.

Define

```text
E(u,v) = (1/2)||v-u||^2 + (1/2)<u,Lv>.
```

Self-adjointness and the difference-of-squares identity give, for the forced
step,

```text
E(v,w)-E(u,v)
 = (1/2)<w-u, w-2v+u+Lv>
 = (1/2)<w-u,f>.
```

Thus the unforced step preserves `E` exactly. To see positivity, put
`m=(u+v)/2` and `d=v-u`. The cross terms cancel, so

```text
E(u,v) = (1/2)<m,Lm> + (1/2)<d,(I-L/4)d>
       >= (1/2)<m,Lm> + (5/18)||d||^2.
```

There is a pointwise nonnegative density, not merely a nonnegative total:

```text
e_x(u,v) = (5/18)(v_x-u_x)^2
         + (1/8) sum_y c_xy [(v_y-u_x)^2+(u_y-v_x)^2].             (1)
```

Equivalently, by expanding the two squares,

```text
e_x(u,v) = (5/18)d_x^2
         + (1/4) sum_y c_xy (m_y-m_x)^2
         + (1/16) sum_y c_xy (d_y+d_x)^2.
```

Summing either expression and reversing edges proves `sum_x e_x=E`.
Every coefficient in (1) is nonnegative. If `E=0`, its onsite term forces
`d=0`; the remaining terms force `u=v` to have the same value at all
neighbours. The norm-two edges connect `D3`: for example `(1,1,0)`,
`(1,0,1)`, `(0,1,1)` generate precisely the even-sum lattice, since the
inverse coefficients are half of the appropriate even signed coordinate
sums. A constant function on this infinite lattice has finite support only
when it is zero. Therefore

```text
E(u,v)=0  iff  u=v=0          on V x V.
```

This does not provide uniform coercivity against `||u||^2+||v||^2`.
Indeed, common indicator functions `u=v` of growing lattice boxes have
energy supported at a boundary of order `R^2`, while their squared norms
have order `R^3`. A periodic finite carrier would also retain a nonzero
constant zero-energy pair. Neither that carrier nor a coercivity claim is
being substituted here.

## 3. Exact local current and source work

First introduce a useful, not necessarily pointwise positive, density

```text
p_x(u,v) = (1/2)(v_x-u_x)^2
         + (1/4) sum_y c_xy (u_y-u_x)(v_y-v_x),
B_xy(u,v) = (c_xy/8)[(v_y-u_y)^2-(v_x-u_x)^2].
```

Direct expansion using `S=8/9` gives

```text
e_x(u,v)-p_x(u,v) = sum_y B_xy(u,v),
B_yx(u,v) = -B_xy(u,v).                                      (2)
```

For a completed step set `s=w-u` and define outgoing oriented currents

```text
Jnat_xy(u,v,w) = (c_xy/4)(v_x-v_y)(s_x+s_y),
J_xy(u,v,w) = Jnat_xy(u,v,w)-B_xy(v,w)+B_xy(u,v).              (3)
```

Both currents are antisymmetric under `x<->y`. The signs in (3) follow from
the redistribution (2). Explicitly,

```text
p_x(v,w)-p_x(u,v)
 = (1/2)s_x(w_x-2v_x+u_x)
   + (1/4) sum_y c_xy (v_y-v_x)(s_y-s_x)
 = (1/2)s_x f_x - sum_y Jnat_xy(u,v,w).
```

Adding the difference of (2) at the two pairs proves the local law

```text
e_x(v,w)-e_x(u,v)+sum_y J_xy(u,v,w) = (1/2)(w_x-u_x)f_x.       (4)
```

This holds for every rational finite-support triple satisfying the forced
step, including zero states and nonzero forcing. Forcing work can have
either sign. With `f=0`, (4) is exact local conservation. The current is a
signed energy transfer; no nonnegative particle flux or detection count is
asserted. It is evaluated after `w` has been computed and uses only the
previous pair, that completed successor and the already supplied force.

## 4. Apertures, locality, overlap and zero

An aperture is a declared finite set `R subset D3`, with literal set
equality. Its mathematical reading and the completed-step flux and work are

```text
E_R(u,v) = sum_(x in R) e_x(u,v),
Phi_R(u,v,w) = sum_(x in R, y outside R) J_xy(u,v,w),
W_R(u,v,w,f) = (1/2) sum_(x in R) (w_x-u_x)f_x.
```

Interior edges cancel by antisymmetry. Consequently

```text
E_R(v,w)-E_R(u,v)+Phi_R(u,v,w)=W_R(u,v,w,f).                  (5)
```

This is finite exact arithmetic; the complement of `R` in the flux formula
requires only the finitely many edges crossing its boundary. Equation (1)
gives `0<=E_R<=E`. Empty apertures give zero energy, flux and work. For two
apertures `R,Q`, literal indicator identities give

```text
E_R+E_Q = E_(R union Q)+E_(R intersection Q).
```

The same identity holds for `Phi` and `W`. Thus disjoint apertures are
additive, while overlapping apertures share the intersection contribution;
it is not silently counted as two different physical deposits.

Reading `e_x` requires the pair on `x+B`. Reading `E_R`, or the flux from an
already computed triple, requires its values on `R+B`; computing a new
successor from an old pair additionally uses the stencil at the required
successor sites. The density therefore has a one-stencil halo beyond the
amplitude support. It is not a point-amplitude detector. Pair energy is
available once both slices exist; the current in (3) is available only after
the next step is complete. There is no read of an uncomputed future slice.

Zero preparation and zero forcing stay zero. A nonzero global state can
have zero energy in a particular aperture, so aperture values are not an
inverse reconstruction of the source. Repeated readback creates no new
state, forcing or energy. Summing readings of the same evolving energy over
time is not an absorbed-energy ledger or a count of distinct occurrences.

## 5. Retarded Green polynomials and finite propagation

Begin with the ready pair `Y_0=(u_0,v_0)=(0,0)`. For supplied finite-support
forces `f_0,f_1,...`, the causal update is

```text
Y_(n+1) = (v_n, H v_n-u_n+f_n),       H=2I-L.
```

Only the force prefix actually supplied to a finite computation is needed.
Define polynomials in the fixed operator `H` by

```text
G_0=I,       G_1=H,
G_(r+1)=H G_r-G_(r-1)                 for r>=1.
```

Their exact closed form is

```text
G_r = sum_(j=0)^floor(r/2) (-1)^j binom(r-j,j) H^(r-2j).       (6)
```

The formula has the stated initial values. Inserting it into the recurrence
reduces each coefficient to Pascal's identity; endpoint terms agree by the
usual zero convention for out-of-range binomial coefficients. Thus (6)
holds by induction without evaluating a spectrum.

After `n>=1` forced steps the current slice is

```text
v_n = sum_(s=0)^(n-1) G_(n-1-s) f_s,                         (7)
u_n = v_(n-1),       with v_0=0.
```

For `n=1`, the update gives `v_1=f_0`. For the induction step, subtracting
`v_(n-1)` from `H v_n` combines the older terms by the defining recurrence
for `G`; the two newest terms are `G_1 f_(n-1)+G_0 f_n`.
This proves (7), while the explicit update proves uniqueness. No negative
physical time index is introduced. Two force sequences agreeing through
`f_(n-1)` give identical state and readout prefixes through `Y_n`.

Each application of `H` enlarges support by at most `B`. Since (6) has
degree at most `r` and `0 in B`,

```text
supp(G_r f) subset supp(f)+rB,
supp(v_n) subset union_(s=0)^(n-1) [supp(f_s)+(n-1-s)B].       (8)
```

Here `rB` is the `r`-fold Minkowski sum, with `0B={0}`. Thus every finite
force prefix gives finite-support rational states and exact finite
readings. Every stencil displacement has Euclidean length at most four;
(8) is a discrete finite-range dependency bound, not an SI speed, Lorentz
cone or physical causal ontology. The density halo described above is
included when turning an amplitude-support bound into a readout bound.

## 6. Chosen QDD-norm source and the post-kick cut

For the source argument `alpha=(alpha_0,...,alpha_3) in Q^4`, choose five
distinct sites

```text
(y_0,y_1,y_2,y_3,y_4)=((0,0,0),(1,1,0),(1,0,1),(0,1,1),(2,0,0)).
```

Write `a=sum_i alpha_i` and define the explicitly chosen linear injection

```text
b_i=alpha_i-a/5  (i=0,1,2,3),        b_4=-a/5,
S_source(alpha)=sum_(i=0)^4 b_i delta_(y_i).
```

This `S_source` is an injection map; it is distinct from the scalar degree
`S=8/9` used above. Distinct sites have orthonormal delta functions, so

```text
||S_source(alpha)||^2
 = sum_(i=0)^4 b_i^2
 = sum_(i=0)^3 alpha_i^2 - a^2/5
 = alpha^T (I_4-11^T/5) alpha
 = m_QDD(alpha).                                            (9)
```

Moreover `alpha_i=b_i-b_4`, so the zero fibre is exactly `alpha=0`.
Cauchy-Schwarz also gives `m_QDD>=sum_i alpha_i^2/5`, strictly positive for
nonzero `alpha`. On the decoder's admitted balanced head coefficients,
(9) is the existing total QDD weight. The rational identity does not extend
the physical meaning or admitted-source claims of the original dictionary.

The one pulse is `f_0=S_source(alpha)` followed by zero forcing. The ready
pair is `(0,0)`. Its first completed update is the preparation

```text
prepare(alpha)=(0,S_source(alpha)).
```

This is called **post-kick cut 0**. It is not the ready pair and is not the
earlier decoder's equal-two-slice initialization. The independent cut label
counts subsequent free steps: at free cut `n>=0` the current is
`G_n S_source(alpha)`; the previous is zero for `n=0` and
`G_(n-1) S_source(alpha)` for `n>=1`.

Source work during the initial kick is `||S_source(alpha)||^2/2`.
Thereafter `f=0`, so (9) and conservation give at every free cut

```text
2 E(previous,current)=m_QDD(alpha),
0 <= 2 E_R(previous,current) <= m_QDD(alpha).                (10)
```

This connects a chosen QDD-norm isometry, the selected scalar propagation,
and a finite local energy reading. It introduces neither LOW/HIGH projectors
nor five-cell Cartesian counts into the propagated energy. The source
isometry, its five marked positions, the retarded preparation and the
aperture choice are disclosed definitions, not target-independence evidence
or a derived physical source coupling.

## 7. Total records, prefix consistency and scope boundary

For any fixed admitted source, force prefix and finite declared apertures,
all state transitions, energies, currents and source-work entries above are
unique rational values obtained with finite resources at each finite cut.
All stored records refer to the stated ready/post-kick convention and to
completed pairs or transitions. An aperture record is a read of these local
values; its energy is not obtained by decoding an auxiliary source header.

Construct the first record from its declared initial pair and append one
record after each completed update. Since no update or reading depends on
the requested final length, induction proves that a shorter history is the
corresponding prefix of any longer one with the same inputs. Ordered append
retains previous immutable records and permits no duplicate or skipped cut.
Passive readback returns existing values and changes neither the state nor
the history. These laws are on generated compatible records; they are not a
reachability certificate for arbitrary forged record tuples. Any source/cut
provenance retained as auxiliary metadata is distinct from the local
aperture reading and does not prove physical source reconstruction.

The whole argument concerns L1 encoded scalar mathematics. A finite aperture
and its nonnegative energy functional are a chosen mathematical readout,
not a physical effect, instrument, detector, Born probability or realized
event. No normalization, sampler, absorption rule or repeated-occurrence law
is inferred from positivity or conservation. The signed boundary current
is not identified with the separately typed tesseract field or torus current.
The result does not establish a physical source-current-propagator-detector
chain, polarization, photon phase/F3, pole residue, SI calibration, a complete
apparatus family, Bell accounting, L6 measure, or feedback into autonomous U.
In particular it authorizes no production under issue #742.

## Public mathematical inputs

* [PHOTON-SPATIAL-TEMPORAL-TRANSFER, D](https://github.com/mathorn1973/twist-j/blob/2d33c38fc0e9a4cfb0e60062eb8d628d46ea9e97/canon/CANON.md#L6157):
  selected complete carrier, flat flux, weights, scale and homogeneous rule.
* [PHOTON-TEMPORAL-CHARACTERISTIC, T](https://github.com/mathorn1973/twist-j/blob/2d33c38fc0e9a4cfb0e60062eb8d628d46ea9e97/canon/CANON.md#L6216):
  the conditional characteristic; it grants no physical-photon conclusion.
* [The prior pointed decoder preregistration](https://github.com/mathorn1973/twist-j/blob/69c9dc34f57d5f9943681761eb6386a17d4bfc47/probes/P-DECODER-POINTED-BATCH-CONFORMANCE-1/PREREG.md):
  exact QDD quadratic weight and explicitly bounded earlier choices. Its
  source initialization is not altered or its result reused by this probe.

The energy density, its redistribution current, the retarded source adapter
and the local aperture dictionary are the present explicitly bounded
construction. Registration and any physical interpretation require their
own subsequent evidence and gates.
