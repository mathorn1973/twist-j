# K1: a selected total linear metric decoder

**NON-CANONICAL / SELECTED WORKING DICTIONARY / ANALYTIC PROOF / NO FORMAL RUN**

```text
basis_main: 39055fcd6d33627b4f30b40f395a4b66bf666b9a
authority: ACTIVE Public Canon v81
scope: fixed K1 -> planar metric records and linear vacuum evolution
mathematical completion at that scope: supplied below
nonlinear gravitational completion / physical validation: NOT SUPPLIED
original O/H closure / new registered status: NONE
```

We select a concrete rule: the two unchanged local K1 squares are the first
two TT strain slices; the public spatial stencil then evolves the metric
by its linear vacuum wave equation. This is a new working dictionary and
evolution choice. It is not a claim that the axiom forces this choice.
Here "linear" describes the subsequent evolution and the equations of the
quadratic action; the initial map from `b` to strain remains quadratic.

The resulting decoder is total for every K1 word and every nonnegative
counter. It has a unique rational metric history, preserves both initial
slices, retains the spatial zero mode, and keeps Lorentz signature at every
step without reducing the K1 amplitude. It also solves the full linear
lapse/shift equations in the stated planar model. These claims have the
self-contained analytic proofs below; no sampled numerical trajectory is
used as an all-time certificate.

This is a positive completion of **one selected linear geometric decoder**.
It does not complete nonlinear gravity, the scalar comparison for `r_T`,
the entire matter/geometry/clock chain, or physical identification of K1.

## 1. The choices and their ownership

| Item | Selected value and reason |
| --- | --- |
| Role of K1 | Initial data for the geometric TT strain, not an externally prescribed stress tensor. Both existing windows remain strain values at steps 0 and 1, not a derivative jet substituted for the second window. |
| Square and normalization | The existing local square `h_t=b_t^2`, cross component zero, at the existing dimensionless K1 normalization `a=1`. No word, weight, spatial point or polarization average is added. |
| Spatial law | Preserve exactly the public planar stencil `L` below. Do not replace it by the Laplacian of a convenient rational centered difference. |
| Subsequent dynamics | Choose the linear vacuum equation `h_(n+1)=(2I-L)h_n-h_(n-1)`. It follows from the selected constrained quadratic action at this scope; a nonlinear completion is a separate problem. |
| Gauge representative | Lapse 1, shift 0, transverse trace, longitudinal and vector perturbations zero, imposed on a solution of the full linear equations **after variation**. |
| Auxiliary derivative | Choose the explicit spectral antisymmetric square root of `L` in section 3. Its finite branch choice is stated, not claimed unique or forced. It introduces no fitted coefficient. |
| Readout and time | The four-by-four metric matrices below at the same five labelled positions, with unit forward model counter. No physical duration, SI length or detector response is inferred. |

The scalar-only metric evaluation rejected in
[the preceding admission review](V81-K1-GEOMETRY-ADMISSION-1.md) stays
rejected at its scope. We do not repair it by attaching an arbitrarily
chosen scalar trace to the TT square. The scalar perturbations here are
constraint variables of the action, and their linear vacuum solution is
zero. Their nonlinear source is not replaced by a normalized intensity.

## 2. Domain, exact map and equality

Let `W` be exactly the ten words and their law in the
[fixed K1 source](V81-TT-K1-SOURCE-MAP-1.md). For
`w=(w_0,w_1,w_2,w_3)`, `r in Z/5` and `t=0,1`, put

```text
u_t=w_(t+2)-w_t,
b_t(r)=[delta_(r,u_t)+delta_(r,u_t+1)]/sqrt(2),
h_t(r)=b_t(r)^2=[delta_(r,u_t)+delta_(r,u_t+1)]/2.
```

The original local inverse Fourier field, both squares and the complete
joint law of `(u_0,u_1)` are unchanged. In particular each initial slice
has sum 1, and the pair is not replaced by independent draws.

For `S f(r)=f(r+1)` define the fixed operator

```text
L = [188 I - 29(S+S^-1) - 65(S^2+S^-2)]/324.
```

This is the planar reduction used in the merged
[lapse note](C-TT-LAPSE-CONSTRAINT-N/README.md), section 2, of the public
D3 stencil. Its row sum is zero. Define, for all `n>=1`,

```text
h_(n+1)=(2I-L)h_n-h_(n-1),
H_n(r)=diag(h_n(r),-h_n(r),0),
gamma_n(r)=I3+H_n(r),
g_n(r)=diag(-1,1+h_n(r),1-h_n(r),1).
```

The decoder and its finite prefix are

```text
D_geom^K1 : W x N0 -> (Sym_4(Q))^(Z/5),
D_geom^K1(w,n)=(g_n(r))_r,
P_N(w)=((n,D_geom^K1(w,n)))_(0<=n<=N).
```

Equality is literal equality of labelled matrix entries and counters.
`Sym_4(Q)` means symmetric rational matrices, not positive matrices; the
required Lorentz signature is proved in section 4. The spatial matrices
`gamma` are positive. The time coordinate sign and model step are chosen
conventions. These are planar local metric records, not a constructed
three-dimensional manifold or an SI spacetime chart.

For a finite requested `n`, this algorithm takes finitely many exact rational
operations. Equivalently, the pair evolves by powers of the one matrix

```text
T_L = [[2I-L,-I],[I,0]],
(h_(n+1),h_n)^T = T_L^n (h_1,h_0)^T.
```

This proves existence and uniqueness for every counter by induction. It
also proves `P_M` is the restriction of `P_N` for `M<=N`: the horizon never
changes an earlier output. The first output uses only the first three bits;
the second and subsequent outputs use the four-bit source. The source
packet must be available before using both initial slices. This does not
assert a physical acquisition clock or realized-event transducer.

If an ensemble is used, its whole history law is exactly the deterministic
pushforward of the existing finite law on `W`. No additional random choice
is made at later times. No geometry output feeds the native update `U`.
No factorization of these new fields through the five algebraic QDD fields
or completion of the other decoder stages is asserted.
For `n>=2` these are evolved metric slices of the anchored initial pair,
not fresh squares of successive native Thue-Morse windows. Neither a new
source law nor stationarity under this continuation is asserted.

## 3. The actual linear action and its constraints

The comparison action is the explicit planar lapse/shift construction in
[the public shift draft, fixed head 5dfbcbaa](https://github.com/mathorn1973/twist-j/blob/5dfbcbaa91934289de6308298963dfe0ed4e2ff1/notes/C-TT-SHIFT-CONSTRAINT-N/README.md),
sections 1-4. That draft is NON-CANONICAL. We use its displayed equations,
not a claim that they complete the nonlinear action of the separate
[ADM predefinition lane #911](https://github.com/mathorn1973/twist-j/issues/911).

Here is the precise derivative choice needed for the displayed linear
action. Let `F` be the existing unitary positive-exponent Fourier transform,
`s=sqrt(5)`, and

```text
lambda_0=0,
lambda_1=lambda_4=(235+18s)/324,
lambda_2=lambda_3=(235-18s)/324,
kappa=(0,sqrt(lambda_1),sqrt(lambda_2),-sqrt(lambda_2),-sqrt(lambda_1)),
D=F^dagger diag(i kappa) F.
```

All square roots are the positive real roots. Pairing the conjugate slots
shows `D` is real, `D^T=-D`, and `-D^2=D^T D=L`. This selects one orientation
branch on the marked characters. Its entries are exact real algebraic
numbers; no claim about a minimal quadratic coefficient field is needed.
The emitted metric remains rational because its recurrence uses only `L`.
This auxiliary same-carrier derivative is a choice for this linear planar
model, not an exhaustive classification of typed derivative constructions.

For the parent quadratic action, denote the lapse perturbation by `ell_0`
and shift by `N_i`. Spatial fields `H_ij` and `ell_0` are on integer
slices; shift and `K_ij` are on half slices. Let `Delta=E-1` and
`Delta_c^2=E+E^-1-2`. The nonzero spatial derivative is along axis 3:

```text
K_11=Delta H_11/2,  K_22=Delta H_22/2,  K_12=Delta H_12/2,
K_13=(Delta H_13-D N_1)/2,  K_23=(Delta H_23-D N_2)/2,
K_33=(Delta H_33-2D N_3)/2,       K=Tr(K_ij),

G2(H)=1/2 <D H_3j,D H_3j> - 1/2 <D H_33,D Tr H>
       + 1/4 <D Tr H,D Tr H> - 1/4 <D H_ij,D H_ij>,
R1(H)=D^2 H_33-D^2 Tr H=2L tau,   tau=(H_11+H_22)/2,

S2=(1/(2 lambda)) sum_n [<K_ij,K_ij>-<K,K>+G2(H)+<ell_0,R1(H)>],
lambda=216 pi.
```

Repeated spatial indices are summed, and inner products sum over `Z/5`.
The action uses no prescribed source: `rho=J_i=S_ij=0`. Variation is
under compactly supported time perturbations in the interior, with the
initial two slices supplied as data. Lapse and shift remain present until
after that variation.
The infinite-time notation denotes this local variational principle; it
does not assert convergence of the infinite sum of action values.

Substitute the selected solution representative

```text
H=diag(h,-h,0),     ell_0=0,     N_i=0.
```

The Hamiltonian and three momentum equations of the full action are
identically satisfied: `tau=0`, `K_13=K_23=0`, and `D Delta tau=0`.
The remaining Euler-Lagrange expressions are

```text
EL_H11=-(Delta_c^2+L)h/(4 lambda),
EL_H22=+(Delta_c^2+L)h/(4 lambda),
all other field EL expressions = 0.
```

Thus the recurrence in section 2 solves **all** the parent linear field
equations and constraints, not merely the TT equations obtained by dropping
lapse and shift. Its reduced action is

```text
S_TT=(1/(4 lambda)) sum_n [<Delta h,Delta h>-<h,Lh>].
```

The spatial mean is retained. Since both initial means are `1/5`, the
zero-mode recurrence has the constant solution `mean(h_n)=1/5` for every
`n`. No source mean is subtracted and no Hamiltonian equation is projected
away. At this linear vacuum order the TT stress quadratic in `H` is absent
from the lapse equation. It must be restored, with the homogeneous response,
in a higher-order action; that omission is a truncation boundary, not a
solution of the nonlinear zero-mode problem found in #909.

## 4. Uniform positivity at the unchanged K1 amplitude

We prove for every source word, site and `n>=0` that

```text
-59/100 < h_n(r) < 99/100.
```

Consequently every eigenvalue of `gamma_n(r)` exceeds `1/100`, and
`g_n(r)` has one negative and three positive eigenvalues at all times.
This is an all-time analytic bound, not a finite-horizon check.

### Fourier solution and its two real amplitudes

The four nonzero eigenvalues listed above lie strictly between 0 and 4.
For `k=1,2`, define `omega_k in (0,pi)` by
`cos omega_k=1-lambda_k/2`, and write `t_k=lambda_k/4`.
Let `Delta_u=u_1-u_0` and

```text
theta_k=2 pi k (u_0+Delta_u/2+1/2-r)/5,
delta_k=pi k Delta_u/5.
```

The paired `k,-k` contribution `y_(k,n)(r)` to the real inverse transform
is exactly

```text
(2/5) cos(pi k/5) [
  cos(theta_k) cos(delta_k) cos((n-1/2)omega_k)/cos(omega_k/2)
 -sin(theta_k) sin(delta_k) sin((n-1/2)omega_k)/sin(omega_k/2)].
```

It agrees with both initial slices and solves their scalar recurrence,
which proves the formula for all `n`. Since the sine and cosine share the
same time argument, its absolute value is bounded by `A_kr`, where

```text
A_kr^2=(4/25) cos^2(pi k/5) [
 cos^2(theta_k) cos^2(delta_k)/(1-t_k)
 +sin^2(theta_k) sin^2(delta_k)/t_k].
h_n(r)=1/5+y_(1,n)(r)+y_(2,n)(r).
```

### Complete finite amplitude bound

Put

```text
F1=(3+s)/50, F2=(3-s)/50,
C_plus=(3+s)/8, C_minus=(3-s)/8,
S_plus=(5+s)/8, S_minus=(5-s)/8,     s=sqrt(5).
```

Here `Fk=(4/25)cos^2(pi k/5)`;
`C_plus+C_minus=3/4`, and `1-C_plus=S_minus`, `1-C_minus=S_plus`.
The elementary bounds `20/9<s<9/4` imply

```text
t1>7/33, 1-t1>3/4, t2>3/20, 1-t2>4/5,
F1<21/200, F2<2/125.
```

Translations and sign reversal of `Delta_u` do not change the set of
angle classes. All nine possible `(u_0,u_1)` pairs are therefore covered
by `|Delta_u|=0,1,2`. The following strict rational bounds cover every site:

| Class | Upper bound for `A_1r^2` | Upper bound for `A_2r^2` | Hence `A_1r+A_2r` is less than |
| --- | --- | --- | --- |
| `Delta_u=0` | `7/50 < (2/5)^2` | `1/50 < (3/20)^2` | `11/20` |
| `|Delta_u|=1` | `693/4000 < (21/50)^2` | `29/300 < (8/25)^2` | `37/50` |
| `|Delta_u|=2`, `(cos^2 theta_1,cos^2 theta_2)=(1,1)` | `7/500 < (3/25)^2` | `21/1600 < (3/25)^2` | `6/25` |
| `|Delta_u|=2`, pair `(C_plus,C_minus)` | `523/3200 < (21/50)^2` | `83/2400 < (1/5)^2` | `31/50` |
| `|Delta_u|=2`, pair `(C_minus,C_plus)` | `782313/1920000 < (16/25)^2` | `10397/480000 < (3/20)^2` | `79/100` |

For `Delta_u=0`, drop `cos^2 theta<=1` in the first term. For
`|Delta_u|=1`, the bracket is a convex combination; bound it by the larger
of its two terms, using `cos^2 delta_1=C_plus`,
`sin^2 delta_1=S_minus`, `cos^2 delta_2=C_minus`,
`sin^2 delta_2=S_plus`.

For `|Delta_u|=2`, `theta_1` is an odd multiple of `pi/5` and
`theta_2=2 theta_1`, giving exactly the three pairs in the table. The
middle pair uses `C_plus C_minus=1/16` and `S_plus S_minus=5/16`.
For the last, most restrictive pair, use

```text
C_minus^2<1/100, S_plus^2<105/128,
C_plus^2<55/128, S_minus^2<49/400.

A_1r^2 < (21/200)[1/75+495/128] = 782313/1920000,
A_2r^2 < (2/125)[275/512+49/60] = 10397/480000.
```

The gaps to `(16/25)^2` and `(3/20)^2` are respectively
`4119/1920000` and `403/480000`, both positive. These substitutions also
give the preceding four rows directly. Thus `A_1r+A_2r<79/100`
uniformly. Adding the unchanged zero mode `1/5` proves the stated interval.

## 5. What is now closed, and the separate nonlinear obligation

The selected map has no unresolved mathematical output for any `w in W`
or `n>=0`: initialization, subsequent dynamics, gauge representative,
literal equality, prefix restriction and metric signature are fixed and
proved. No gain was adjusted to make the positivity proof pass. The source
law and both original K1 windows survive exactly. The construction provides
an independently checkable consequence of the selected law beyond its
initial square: every later slice obeys the fixed three-slice recurrence
and the uniform signature bound.

What is selected rather than derived is the identification of the local
square with initial metric strain and the use of this linear planar
vacuum law as the continuation. Its compatibility with the displayed
quadratic action is proved; its truth as a law of Nature is not. Measuring
a source programmed to reproduce K1 still would not independently establish
that Nature selects its word weights or this metric dictionary.

The full tensor-and-scalar owner is not closed. In particular:

- The action here supplies linear constraints only. The positive TT
  self-source, its cubic action terms, time placement, FRW zero mode and
  nonlinear constraint propagation remain with #911. These histories are
  not certified initial data or solutions of that unfinished full system.
- In a perturbative expansion `gamma(epsilon)=I+epsilon H`, the action
  verifies the first-order field equations. The exact positive matrix
  representative chosen here is `epsilon=1`. Positivity at that value is
  not a small-perturbation estimate or a controlled approximation to a
  nonlinear gravitational solution.
- The scalar perturbations vanish in this linear vacuum representative.
  The exact metric determinant `det(gamma)=1-h^2` is still available, but
  it is not adopted as a cosmological scalar perturbation or used to
  manufacture a nonzero `P_S`. No `r_T`, including zero or infinity, is
  inferred from this truncation.
- This planar model supplies no general three-dimensional extension,
  Schwarzschild/RW comparison, physical coordinate scale, detector or
  empirical geometric identification. Choosing an auxiliary spectral `D`
  here does not decide the complete typed derivative class in #911.

The policy permits a determined reading in a named context without global
decoder uniqueness. That is the completion achieved here, at the explicit
linear mathematical scope. It does not turn this working choice into a
Canon dictionary or dispose of any original physical O/H row. Further
nonlinear work should extend this concrete object or exhibit its failure
under the actual higher-order constraints, rather than silently replacing
the K1 data or discarding the zero mode.
