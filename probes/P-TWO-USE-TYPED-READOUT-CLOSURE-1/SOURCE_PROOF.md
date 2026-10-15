# Independent algebraic proof for the funded two-use audit

**NON-CANONICAL / conditional L1 mathematical proof.**

Original work Apache-2.0, A. M. Thorn, 2026-10-15.

This proof is authored from the frozen source definitions before scientific
execution. It does not assert a passing verifier, an independent reproduction,
Canon promotion, native compilation, physical readiness, or indefinite
repeatability. A finite audit and the universal arguments below have distinct
scopes. Explicit numerical stencil targets remain subject to the pinned
independent verifier and its declared finite coverage.

## 1. Definitions and elementary identities

Work over the rationals on the fixed finite principal Dirichlet domain
`D = Y + B_zero + B_zero`. G1 at
`82ad219401d87c3900011d1e8801ffef4221e05b` reconciles this primary set to
705 ordered sites; DOMAIN.tsv SHA-256 is
`2e9b77cf8c507b9bc6675d9a07bf8e27ad88921c72c1efc22dcf5bdb41d8a7c0`.
The amplitude dimension is 2*705+16=1426. This certificate does not establish
any response or work target below. The five ordered source sites are
`Y = ((0,0,0),(1,1,0),(1,0,1),(0,1,1),(2,0,0))`; the first four are
ports. The stencil comprises the D3 vectors with squared length
`2,4,8,10,16`, with weights `6,1,15,1,1` divided by `324`.
The full diagonal of `L_D` is `8/9`, including at the boundary.
Let `H=2I-L_D`, and let `P` insert a four-vector at the four ports.
Thus `H=H^T` and `P^T P=I`. Write

```text
Q=PP^T,       J=I-Q,       K=I-Q/2=(I+Q)^-1,       T=KH.
Q^2=Q,       J^2=J,       KJ=J,       KP=P/2,       P^T J=0.
```

For `s=1^T z`, the source `S z` has values `z_i-s/5` at the four
ports and `-s/5` at the fifth site. Direct summation gives

```text
P^T S=G=I-11^T/5,       S^T S=G,
E(u,v)=(||u||^2+||v||^2-u^T H v)/2.
```

Use the balanced residue lift `ell(0,1,2,3,4)=(0,1,2,-2,-1)` and
`eta(q,r)=(ell(q)/2,(ell(r)+1)/2,0,0)`. A contact source is `a=S eta(r)`.
All equalities below are literal, signed, exact coordinatewise equalities.

## 2. The complete wave/tape map is a two-sided bijection

For arbitrary rational occupied wave and four tape slots, put

```text
w=K(Hv-Ju+4Pa),       b_out=a-P^T(w-u)/2,
F((u,v),(a,a1),(b0,b1),k)
 = ((v,w),(a1,b1),(b_out,b0),k+1 mod 2).
```

The forward wave equation is `(I+Q)w=Hv-Ju+4Pa`. Substitute
`a=b_out+P^T(w-u)/2`. Collecting terms gives exactly

```text
(I+Q)u=Hv-Jw+4P b_out.
```

Consequently, from an arbitrary output
`((v,w),(alpha0,alpha1),(beta0,beta1),k')`, recover

```text
u=K(Hv-Jw+4P beta0),
a=beta0+P^T(w-u)/2,
F^-1(output)=((u,v),(a,alpha0),(beta1,alpha1),k'-1 mod 2).
```

The rearrangement is reversible and has unique solutions because `I+Q`
is invertible. Substitution in either direction restores both the wave
equation and the port equation. The displayed tape permutation and clock
subtraction restore every remaining coordinate. This proves both
`F^-1 F=I` and `F F^-1=I` on the entire stated rational carrier.

For energy, put `t=w-u` and `y=P^T t/2`, so `b_out=a-y`. The forward
equation also gives `w+u-Hv=4Pa-Q t`. Symmetry of `H` yields

```text
E(v,w)-E(u,v)
 = t^T(w+u-Hv)/2
 = 2t^T Pa-t^T Q t/2
 = 4y^T a-2||y||^2
 = 2||a||^2-2||b_out||^2.
```

The four-slot tape energy changes by the opposite amount under its literal
permutation. Hence `E_full=E+2 sum_slots ||slot||^2` is preserved for every
rational occupied state, with each stored slot counted once.

## 3. Each bounded contact is an involution, including both refusals

Hold the chosen source `a`, the older wave slot `u`, and all other
non-participating coordinates fixed. For either `sigma=+1` or `sigma=-1`,
expansion of the quadratic energy gives

```text
Delta=E(u,v+sigma a)-E(u,v)
     = ||a||^2/2 + sigma a^T(v-Hu/2).
```

On the guard `0 <= b-Delta <= B`, update
`(v,W,b,sigma)` to `(v+sigma a,W+Delta,b-Delta,-sigma)`.
Otherwise retain the entire state. On an accepted image the next increment
is

```text
Delta'=E(u,v+sigma a-sigma a)-E(u,v+sigma a)=-Delta.
```

The reverse store candidate is `(b-Delta)-(-Delta)=b`, which lies in
`[0,B]`. The reverse call therefore accepts and restores all four
coordinates. A refused state remains identical and has the same failed
guard on its next call. This proves involutivity on every accepted,
shortage-refused and overflow-refused state, including equality at either
store boundary, `B=0`, zero sources and both signs.

On acceptance, the changes in `(E_full,W,b)` are `(Delta,Delta,-Delta)`;
on refusal they are zero. Therefore each contact preserves
`E_full-W`, `E_full+b`, and `W+b`.

The upper guard is essential. For example, with `a=S(e0/2)`,
`u=0,v=-2Pe0,sigma=+1`, the increment is `1/10-4/5=-7/10`.
At `b=B` acceptance would overflow. The opposite occupied wave
`v=2Pe0` has increment `9/10`, so at `b=B=4/5` it is shortage-refused.
These are occupied-state examples, not a universal funding bound.

## 4. Static apparatus permutation and joint invariants

For fixed supplied native receiver labels `r_A,r_B`, buffer capture is
`d -> d+r_B` in `F5^2`, with inverse subtraction. It commutes with
contact A: capture changes only `d`, which contact A does not read.
The static apparatus row maps at phases `0,...,7` are

```text
I, H_A L_buf, F, F, H_B, F, F, I.
```

Their inverses are respectively
`I, L_buf^-1 H_A, F^-1, F^-1, H_B, F^-1, F^-1, I`.
Thus the clocked static apparatus map has two-sided inverse

```text
(a',c') -> (T_(c'-1)^-1(a'), c'-1 mod 8).
```

Its seven-row map `M7=T6 ... T0` is a bijection. Its inverse applies
`F^-1,F^-1,H_B,F^-1,F^-1,H_A,L_buf^-1` in that temporal order.
The eighth row only rolls phase `7` to `0`.

Native steps and capture hold `(X,W,b)` fixed. The preceding energy
identities therefore prove conservation of all three joint quantities
through every phase. For an initial old archive `(c0,c1)` and otherwise
common-ready apparatus,

```text
E_full-W=2(||c0||^2+||c1||^2),
W+b=b_init,
E_full+b=2(||c0||^2+||c1||^2)+b_init.
```

This is a global permutation assertion for the static apparatus only.
It is not a global inverse assertion for the selector-defined native map
or for the composite map carrying the nonnegative native counter.

## 5. Four actual cuts and arbitrary old archives

Start with wave and incoming tape zero, old outgoing archive `(c0,c1)`,
two initially positive direction bits and blank delayed buffer. Write
`f=S z_A`, `g=S z_B`, and let `alpha_A,alpha_B` be the actual acceptance
indicators. Refusal is identity, so the fields actually added are
`alpha_A f` and `alpha_B g`. Define

```text
w1=T f, w2=T w1-Jf, a3=T w2-Jw1, a4=T a3-Jw2.
```

Direct substitution in the four successive `F` calls gives the wave
after the first two cuts as `(alpha_A w1,alpha_A w2)`, and the final
two slices as

```text
w3=alpha_A a3+alpha_B T g+2P c1,
w4=alpha_A a4+alpha_B(T^2-J)g+2T P c1+2P c0.
```

The actual incoming slots in order are `0,0,c1,c0`. Thus old archive
energy reaches the wave only after contact B; it cannot change either
contact guard on this common-ready family. Applying the port equation
at each cut gives

```text
R0=-P^T T S/2,
R1=P^T(S-(T^2-J)S)/2,
D2=P^T(T-T^3+TJ)S/2,
D3=P^T(T^2-T^4+T^2J+TJT)S/2,
Jp=P^T H P,

b0=alpha_A R0 z_A,
b1=alpha_A R1 z_A,
b2=alpha_A D2 z_A+alpha_B R0 z_B,
b3=alpha_A D3 z_A+alpha_B R1 z_B-Jp c1/2.
```

For example, the explicit `c1` contribution to cut 2 is
`c1-P^T(2Pc1)/2=0`; the cut-3 contribution is
`-P^T T P c1=-Jp c1/2`. The `c0` contribution cancels similarly.
The expansions of `D2,D3` use only `J^2=J` and `P^T J=0`.
These are identities for arbitrary rational archives and sources with
the stated initial conditions and actual branch indicators.

The tape pairs after consecutive cuts are
`((0,c1),(b0,c0))`, `((c1,c0),(b1,b0))`,
`((c0,b0),(b2,b1))`, `((b0,b1),(b3,b2))`.
Hence chronological cuts are read directly, and the first pair remains
available through the second use. A recorded zero is still a recorded cut;
it does not alone certify acceptance.

All six nonzero port-to-port displacements have square length two.
Thus the port diagonal of `H` is `10/9` and its off-diagonal entries
are `1/54`. The fifth-site column at the ports is `(1,6,6,0)^T/324`.
The five-site row sums are `(379,384,384,378)^T/324`; subtracting
one fifth of each row sum from the corresponding row of `P^T H P`
therefore gives

```text
Jp=(59I+11^T)/54,
M=P^T H S=(1770I-v1^T)/1620, v=(349,354,354,348)^T,
1^T v=1405, R0=-M/4,
R0^-1=-(216/59)(I+v1^T/365).
```

Indeed multiplication of `(1770I-v1^T)(I+v1^T/365)` gives `1770I`.
Thus `R0` is invertible. On the accepted/accepted branch,
`z_A=R0^-1 b0` and `z_B=R0^-1(b2-D2 z_A)` for all rational old
archives. On every branch `R0^-1 b0=alpha_A z_A`.

These arguments concern the frozen finite Dirichlet operator. The
two-cut support buffer does not by itself establish a four-cut or all-time
infinite-lattice equivalence.

## 6. Occupied second-contact work and finite funding targets

Before contact B the wave is
`(alpha_A T f,alpha_A(T^2-J)f)`. Since `K-I/2=J/2`,

```text
(T^2-J)f-H T f/2 = J(H K H f/2-f).
```

Also `Jg=-(s_B/5)delta_y4`, where `s_B=1^T z_B`. Therefore the actual
positive-direction increment before testing contact B is universally

```text
Delta_B=||g||^2/2
        -alpha_A (s_B/5) delta_y4^T(H K H S/2-S)z_A.
```

The independent stencil audit must check the numerical row target
`delta_y4^T(H K H S/2-S)=mu^T/2099520`,
`mu=(145483,173653,173653,142153)^T`. With that target established,
the mixed term is `-alpha_A s_B(mu^T z_A)/10497600`.
This formula reduces to the cold cost when contact A refused.

The five prepared source vectors are
`Z5=(0,e0/2,(e0+e1)/2,e0+e1/2,e1)` and their cold energies are
`(0,1/10,3/20,2/5,2/5)`. The finite 25-pair check is responsible for
the numerical maximum target `B*=8224427/10497600` and the lower-capacity
branch tables. Given nonnegative increments on those pairs and that
maximum, all pairs accept both contacts iff `B* <= b_init <= B`:
necessity follows from the maximizing pair, and sufficiency follows by
applying both store inequalities to the two cumulative nonnegative costs.
No such finite cold-family bound is asserted for arbitrary occupied waves.

## 7. Prepared native inverse and the paired finite factorization

Write a native head as `(a,b,c,d,q,r)` in `F5^6`. The five maps are

```text
g0=(b,a,d,c,q,r),
g1=(-c,-d,-a,-b,-q,-r),
g2=(2-c,1+r-d,2-a,1-r-b,1-q,-r),
g3=(2-a,1-b,3-c,4-d,1-q,1-r),
g4=(2-a,1-b,3-c,4-d,2-q,1-r).
```

Substituting twice proves each is an involution. Their actions on the
complete coordinate sum `s` are `s,-s,2-s,2-s,3-s`. The selector is
`j=(s+2 theta_n) mod 5`, with `theta_n=popcount(n) mod 2`.
For prepared `(p,0,1)` let `h=sum(p) mod 5`. Propagating the complete
sum and receiver gives the following table:

| h | First three selectors | C1 | C2 | C3 |
|---|---|---|---|---|
| 0 | 1,1,3 | 0,4 | 0,1 | 1,0 |
| 1 | 2,2,4 | 1,4 | 0,1 | 2,0 |
| 2 | 3,1,3 | 1,0 | 4,0 | 2,1 |
| 3 | 4,1,3 | 2,0 | 3,0 | 3,1 |
| 4 | 0,2,4 | 0,1 | 1,4 | 1,2 |

Every row ends with complete sum `1`. Since `theta_3=0,theta_4=1`,
the next two selectors are `1,1`, so `x5=g1 g1 x3=x3`.
The five `C3` receivers are distinct. From `x5` decode `h`, then apply
the first-three word in reverse temporal order to obtain `(p,0,1)`.
The forward word depends only on `h`, and each of its maps is a
bijection; this proves exact prepared-head recovery.

For an arbitrary proposed composite endpoint, an exact ready-image
recognizer first requires `n=5,c=7` and a valid `C3` on both heads.
It reverses the corresponding words, checks receiver `(0,1)` and
`sum(p)=h`, requires `d=C1(h_B)`, and applies the static apparatus
inverse with labels `C1(h_A),C1(h_B)`. It accepts iff the result equals
the specified complete ready apparatus, including its old archive,
work, store, both direction bits and blank buffer.
Necessity follows by reversing a ready trajectory. For sufficiency,
the receiver and sum checks force the correct forward native words;
the bijective static apparatus inverse forces the entire proposed
apparatus endpoint. Thus the accepted endpoint is exactly the forward
image of the reconstructed prepared pair. No off-ready native inverse
is used.

Each sum fibre has exactly `5^3=125` prepared heads: choose three
piston residues and the last is forced. The two heads evolve
independently with the same prescribed counter. All apparatus inputs
are determined by `(h_A,h_B)`, with the second first-tick label
retained in `d`. Thus 25 source-pair apparatus classes, each of size
`125^2=15625`, partition the `625^2=390625` prepared pairs.
The same factorization holds on refused branches: refusal does not
alter native states or delayed capture and is a literal apparatus
identity. A verifier may audit every head and the paired product while
reusing an apparatus class; that is distinct from independently
simulating 390625 different rational wave trajectories. The reported
coverage must state which procedure was executed.

Global native injectivity is false. At counter zero the distinct
heads `(0,0,0,0,0,1)` and `(2,1,3,4,2,2)` select `g1` and `g4` and both
map to `(0,0,0,0,0,4)`. Moreover no native step reaches counter zero.

## 8. Direction readout, calibration and comparator scope

On the ready family define `z_B=eta(d)` and
`r=b2-D2(R0^-1 b0)`. Section 5 gives `r=alpha_B R0 z_B` on every
branch. If `z_B` is zero then its contact increment is zero and the
guard always accepts, so `alpha_B=1`. If `z_B` is nonzero,
invertibility of `R0` implies `alpha_B=1` iff `r` is nonzero.
Therefore the ready-family projection `(X,W,b,d)` already determines
contact-B acceptance. Its direction bit is redundant as that acceptance
readout; it remains part of the complete transition and inverse law.

Contact-A acceptance is not similarly recoverable from this projection.
At `b_init=B=1/5`, `c1=0`, pairs `(h_A,h_B)=(0,0),(3,0)` give the same
`(X,W,b,d)` with accepted-zero and refused A respectively. Removing both
direction bits from the purely classical projection collapses all four
pairs in `{0,3}^2`. This proves the specified projection collisions,
not minimality over every possible reversible controller.

In the stipulated linear/quadratic response class, four `4x4` response
matrices, one symmetric `4x4` energy matrix and one `4x4` bilinear
matrix have `64+10+16=90` parameters. Restricting to
`Pi2=span(e0,e1)` leaves `32+3+4=39`. Runs `(z1,0),(z4,0)` determine
the two columns of each response matrix; their energies give
`G00=8E(z1)` and `G11=2E(z4)`. Run `(z2,0)` gives
`G01=4E(z2)-(G00+G11)/2`. Four basis pairs
`(z1,z1),(z1,z4),(z4,z1),(z4,z4)` determine the four entries of
`Omega` from `Delta_B-E(z_B)`, scaled by `4,2,2,1` respectively.
This is an explicit inverse calibration on the 39-dimensional restriction,
not an identification of the 51 out-of-plane parameters. Rank-one
`Omega=-1 nu^T` reduces its four entries to two and permits five runs.
A zero run is a sufficient direct calibration of added constant offsets.

For the nonlinear countermodel,
`q3(z)=z0 z1(2z0-1)` vanishes at `z0,z1,z2,z4` and has value `1/2`
at `z3`. Thus `b2+q3(z_A)u` differs by **u/2**, and
`Delta_B+lambda q3(z_B)` differs by `lambda/2`, at the designated
held-out source. The source's residual phrase "differs by u" is not
adopted. The polynomial `z0(2z0-1)(2z1-1)` vanishes on all five
sources yet is one at `(1,1)`, demonstrating the further extrapolation
boundary.

A full matched classical comparator supplies `C1(h_A),C1(h_B)` and
executes the identical static apparatus rows. The apparatus sequences
then agree by induction, for every ready source pair and old archive;
under any shared deterministic exact encoding their bytes agree.
Separation from a single-use, cold-reset, overwriting-tape or directly
shared-unreset-sign comparator concerns those specified modified laws.
It cannot separate this conditional apparatus from the full matched
classical comparator or establish a physical distinction.

## 9. Source dispositions and unpassed boundaries

The adopted inverse of `F` contains both `K` and `J`; the earlier
`Hv-w+2P b_out` expression is false. The adopted `D3` contains
`TJT`, `Jp=P^T H P`, and the decoder is the exact `R0^-1` above.
Completion is seven updates at `n=5,c=7`; the eighth update is rollover.
The two parent-disclosed residual source defects are disposed explicitly:
the nonlinear vector displacement is `u/2`, and the retained delayed
buffer plus classical record makes `sigma_B` redundant for ready-family
acceptance readout. G1 further withdraws only the later false 869-site paraphrase for this new
successor; the primary set and all dynamics remain unchanged. The independent
705-site reconstruction and exact ordered certificate are checked before
other science. These dispositions do not edit the frozen sources.

The independent finite verifier must establish its numerical stencil,
funding, branch, archive, calibration and comparator targets within its
declared coverage. Its success does not by itself prove the universal
claims; those rely on the algebra above. Native compilation, physical
energy for control and records, material renewal, an SI clock, physical
qualification, occurrence, and L2-L6 bridges remain unestablished.
