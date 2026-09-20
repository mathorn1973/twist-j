# A selected scalar-clock and TT cosmological comparison

**PUBLIC; candidate-T, L1, NON-CANONICAL.** This proof concerns the exact
conditional quadratic model ETH-COS-1 in MODEL.md, under public lock #1099.
It supplies the background, scalar constraints, state, continuum transfer
and finite-band cosmological ratio for that selected model. It does not
derive the selection from J, prove a finite-amplitude nonlinear Einstein
solution, or predict an isotropic primordial CMB spectrum.

All universal time statements below follow from explicit analytic solutions
or uniqueness of a linear equation. Finite exact checks audit their algebraic
ingredients; they do not establish the continuum statements by extrapolation.

## 1. A canonical scalar realizes the selected homogeneous expansion

Set `lambda=216 pi>0` and choose the continuum action

```text
S=integral sqrt(-g)[R/(2lambda)
                   -(1/2)g^(mu nu) partial_mu phi partial_nu phi
                   -V(phi)] d^4x,
V(phi)=3H_*^2/(2lambda) exp[-sqrt(3lambda)(phi-phi_*)],
H_*>0,  phi_*=0.
```

Its flat homogeneous equations, in proper chart time, are

```text
3H^2=lambda[(dot phi)^2/2+V],
dot H=-lambda(dot phi)^2/2,
ddot phi+3H dot phi+V_phi=0.
```

Define `F=1+3H_*t/2`, for `t>=0`, and

```text
a=F^(2/3), H=H_*/F,
phi=sqrt(3/lambda) log a.
```

Then `dot phi=sqrt(3/lambda)H`, `dot H=-3H^2/2`, and
`V=3H^2/(2lambda)`. Kinetic and potential densities are equal; each is
`3H^2/(2lambda)`. The first two homogeneous equations follow. For the third,
the three terms are respectively

```text
-(3/2)sqrt(3/lambda)H^2,
3sqrt(3/lambda)H^2,
-(3/2)sqrt(3/lambda)H^2,
```

whose sum is zero. Thus `epsilon=-dot H/H^2=3/2` exactly, and the background
pressure is zero. Its acceleration is negative. This solution requires no
slow-roll or inflationary approximation. A canonical scalar has propagation
speed one in the reduced action below; a zero background pressure does not
make its perturbations those of pressureless dust.

Elapsed conformal time satisfies `dt=a d eta`. Integrating with both clocks
zero at launch gives

```text
a(eta)=(1+H_*eta/2)^2,
t(eta)=2[(1+H_*eta/2)^3-1]/(3H_*).
```

Put `x=eta+x_0`, `x_0=2/H_*`. Then

```text
a=(x/x_0)^2,  a'/a=2/x,  a''/a=2/x^2.
```

All fields are smooth on the whole declared future domain because `x>=x_0>0`.
The homogeneous coefficient still gives `H^2=72 pi rho`. This is a new
canonical matter realization of the same homogeneous functional form, not an
identity with the word-dependent K1 hybrid action. In particular `H_*` is
one fixed context datum for all preparation atoms, not a second use of the
old TT source-energy channel.

## 2. The scalar variable and its constraints

Write the ADM metric as

```text
ds^2=-N^2 dt^2+g_ij(dx^i+N^i dt)(dx^j+N^j dt).
```

In comoving gauge the scalar field has no perturbation. For the scalar
calculation take `g_ij=a^2 exp(2zeta)delta_ij`, `N=1+alpha`, and the
covariant shift `N_i=partial_i psi`, at the orders consumed below. The
exponential is a convenient perturbative parametrization. It is not a
claim that the later linear solution solves the full nonlinear action.

For a homogeneous scalar the ADM action, after the usual gravitational
boundary term, is

```text
integral N sqrt(g_3) [R_3/(2lambda)
 +(K_ij K^ij-K^2)/(2lambda)
 +(dot phi)^2/(2N^2)-V] dt d^3x.
```

In this chart `R_3=a^-2 exp(-2zeta)[-4 Delta zeta-2|grad zeta|^2]`.
Expanding to second order, integrating spatial total derivatives on the
torus, and using the background equations gives the scalar quadratic
functional before the lapse and shift are eliminated:

```text
S^(2)=(1/lambda) integral a^3 {
 -3(dot zeta)^2+|grad zeta|^2/a^2
 +6H alpha dot zeta-2 alpha Delta zeta/a^2
 -(3-epsilon)H^2 alpha^2
 +2(dot zeta-H alpha)Delta psi/a^2 } dt d^3x.
```

The terms proportional to a background equation and endpoint total
derivatives do not affect interior variations. This expression also displays
the normalization cancellation directly, rather than assuming a scalar
coefficient from the homogeneous conformal action.

Variation of the shift gives
`Delta(dot zeta-H alpha)=0`. On the declared nonzero Fourier modes it fixes
`alpha=dot zeta/H`. Varying the lapse then yields

```text
Delta psi=-Delta zeta/H+a^2 epsilon dot zeta,
psi=-zeta/H+a^2 epsilon Delta^-1 dot zeta.
```

The mean-zero inverse is unique. No homogeneous lapse or shift perturbation
is inserted into the selected state. Substitution of `alpha` gives the
kinetic coefficient

```text
-3+6-(3-epsilon)=epsilon.
```

The remaining spatial terms are

```text
(1/lambda) integral [a|grad zeta|^2
                    -2(a/H)dot zeta Delta zeta] dt d^3x.
```

Their second term becomes `(a/H) d_t|grad zeta|^2` after spatial integration.
Time integration gives `-[d_t(a/H)]|grad zeta|^2`, and
`d_t(a/H)=a(1+epsilon)`. The net gradient coefficient is therefore
`-a epsilon/lambda`. Consequently

```text
S_S=(epsilon/lambda) integral
             [a^3(dot zeta)^2-a|grad zeta|^2] dt d^3x
   =(epsilon/lambda) integral
             a^2[zeta'^2-|grad zeta|^2] d eta d^3x.
```

This reduction uses the exact background equations, not small epsilon.
In a conformal metric written with scalar lapse `alpha` and shift gradient
`beta`, the same constraints are

```text
alpha=zeta'/(a'/a),
beta=-zeta/(a'/a)+epsilon Delta^-1 zeta'.
```

Thus the scalar fluctuation is the comoving spatial-curvature variable of a
specified matter theory, with its lapse and shift determined. It is not the
old intensity assigned a new name.

The external action conventions are the canonical Einstein-scalar
conventions in [Maldacena, equations (2.1), (2.8), (2.10), (2.12)](https://arxiv.org/pdf/astro-ph/0210603v5). The source supplies these
continuum conventions; our background, preparation and interface are
separate choices. The displayed reduction fixes the exact factors used here.

## 3. Tensor normalization and canonical coordinates

For the transverse traceless field write

```text
gamma_ij=e^+_ij gamma_+ + e^x_ij gamma_x,
e^+=diag(1,-1,0),  e^x_12=e^x_21=1,
sum_ij e^A_ij e^B_ij=2delta_AB.
```

These tensors are transverse for the occupied modes along the third axis.
The quadratic Einstein action is

```text
S_T=(1/(8lambda)) integral a^2
       [gamma_ij' gamma_ij'-partial_l gamma_ij partial_l gamma_ij]
       d eta d^3x
   =(1/(4lambda)) integral a^2 sum_A
       [gamma_A'^2-|grad gamma_A|^2] d eta d^3x.
```

This convention agrees with the tensor normalization in
[Maldacena, equations (2.27), (2.28)](https://arxiv.org/pdf/astro-ph/0210603v5). It also matches the coefficient
of the older flat TT action when `a=1`; no equality of subsequent flat and
expanding solutions is implied.

Define

```text
q_T,A=a gamma_A/sqrt(2lambda),
q_S=a sqrt(2epsilon/lambda) zeta.
```

For a variable `q=b f`, any term `b^2(f'^2-K^2f^2)/2` becomes, after one
time integration by parts,

```text
(1/2)[q'^2-K^2q^2+(b''/b)q^2]
  -(1/2)[(b'/b)q^2]' .
```

The final total derivative specifies the boundary canonical transformation.
The selected canonical action drops it and has momentum `p=q'`. Since
epsilon is constant, `b_S` and every `b_T` are constant multiples of `a`.
All canonical fields therefore have the same equation

```text
q''+[K^2-a''/a]q=0.
```

The initial momentum in MODEL.md refers to this canonical choice. At launch
`a=1` and `a'/a=H_*`; hence `q'=q/d` entails

```text
gamma_A'=(1/d-H_*)gamma_A,
zeta'=(1/d-H_*)zeta.
```

It does not simultaneously match the old flat metric velocity `Phi/d`.
The backward difference motivates a declared canonical interface; it does
not prove a unique continuum derivative or boundary impulse.

## 4. Interpolation, common coordinates and unchanged packet data

Let `L_box=5d`, `d>0`, and use the three-torus of side `L_box`. All prepared
fields depend only on `x_3`. For a real five-vector define

```text
fhat_j=(1/sqrt(5)) sum_(r=0)^4 f_r exp(-2pi i j r/5),
I f(z)=(1/sqrt(5)) sum_(j=-2)^2 fhat_j exp(iK_j z),
K_j=2pi j/(5d).
```

The roots-of-unity identity
`sum_(j=-2)^2 exp[2pi i j(r-s)/5]=5delta_rs` proves
`I f(rd)=f_r`. Reality gives `fhat_-j=conjugate(fhat_j)`. This is the unique
interpolation in the declared five-dimensional band. After the launch,
ordinary spatial derivatives have eigenvalues `-K_j^2`, not the graph
eigenvalues in the predecessor recurrence. Interpolation is a source
interface, not a proof that these two propagation laws coincide.

Keep the ten K1 words and their earlier probabilities. Their impulses are

```text
Phi=0                           total mass 1/3,
Phi=+/-d1, d1=(e0-e2)/2         each sign mass 1/12,
Phi=+/-d2, d2=(e4-e1)/2         each sign mass 1/12,
Phi=+/-(d1+d2)                 each sign mass 1/6.
```

The new scalar source datum is
`S=Pi_0 abs(Phi)`, with `Pi_0 f=f-(sum f)/5`. Both Phi and S have zero
spatial mode in each atom. No ensemble-mean profile is subtracted from S.
Taking a norm, interpolating and subsequently propagating are distinct
operations; neither `I abs(Phi)=abs(I Phi)` nor a later identity
`zeta=abs(gamma_+)` is imposed.

Choose a common amplitude `A>0`, an independent uniform translation
`sigma in [0,L_box)`, and the two independent fair persistent root signs.
The launch data are

```text
q_T,+(0,z)=A I Phi(z-sigma)/sqrt(2lambda),  q_T,x=0,
q_S(0,z)=A I S(z-sigma)/sqrt(2lambda),
q_T,A'(0)=q_T,A(0)/d,  q_S'(0)=q_S(0)/d.
```

In particular the actual metric amplitudes at launch are
`gamma_+=A I Phi`, `zeta=A I S/sqrt(6)`. The equality of the canonical
preparation coefficients is an explicit input; the actions alone do not
select it. The scalar sector is an additional preparation. The prior
complete transfer into the TT channel does not fund this added scalar
energy without a further microscopic source model.

The clock identification is `eta_n=(n-2)d`, not the old proper-time cell
rule. Given a length calibration `ell_0`, the common physical maps are
distance `ell_0 x`, proper elapsed time `ell_0 t/c`, and physical wave number
`abs(K_j)/(ell_0 a)`. The dimensionless number `H_*d` is a context datum and
cannot be erased by calling it a unit choice.

## 5. Exact continuum transfer and its zeros

For `K=abs(K_j)>0`, let

```text
f_K(x)=cos(Kx)-sin(Kx)/(Kx),
g_K(x)=sin(Kx)+cos(Kx)/(Kx),
x=eta+x_0,  x_0=2/H_*.
```

Direct differentiation gives

```text
f_K''+(K^2-2/x^2)f_K=0,
g_K''+(K^2-2/x^2)g_K=0,
f_K g_K'-f_K' g_K=K.
```

Thus the fundamental matrix with these columns is invertible on the whole
future domain. With `gamma_0=1/d`, the unique unit launch transfer is

```text
G_j(eta)=c_j f_K(x)+s_j g_K(x),
c_j=[g_K'(x_0)-gamma_0 g_K(x_0)]/K,
s_j=[gamma_0 f_K(x_0)-f_K'(x_0)]/K.
```

The Wronskian gives `G_j(0)=1`, `G_j'(0)=gamma_0`. Hence every canonical
mode with the specified launch momentum evolves as `q_j(eta)=G_j(eta)q_j(0)`.
The transfer is real, even in j, and common to the scalar and tensor sectors.
Its full phase-space transfer has determinant one, as follows from the
constant nonzero Wronskian. Thus the Cauchy solution is unique for all future
times even when a field coordinate vanishes.

The function G is real analytic and not identically zero, so its zeros have
no finite accumulation. A zero is simple: if both G and G' vanished, linear
ODE uniqueness would contradict `G(0)=1`. There are arbitrarily late zeros:
write `c_j=R cos(delta)`, `s_j=R sin(delta)`, with R>0. Then
`G=R[cos(Kx-delta)-sin(Kx-delta)/(Kx)]`, which takes alternating values
`(-1)^n R` at every sufficiently late point `Kx-delta=n pi`. Continuity
supplies a zero between consecutive such points. No all-time field
nonvanishing result from the old discrete recurrence is imported here.
At a transfer zero both prepared
sector field powers vanish together, although the phase-space information
is not lost. Their ratio is then undefined. Its constant limiting extension
is not a claim of nonzero measured power at that instant.

## 6. A complete homogeneous, anisotropic joint state

The complete preparation measure is

```text
nu(w) times uniform(epsilon_+,epsilon_-)
      times [d sigma/L_box].
```

The same labels feed both sectors and their momenta at all times. The unique
linear solution is a deterministic map of that one preparation. It defines
a normalized joint probability law on every collection of chart points and
times; restricting a collection uses the same random variables and hence
gives compatible marginals. Static words prepare zero in both sectors and
keep their total mass 1/3.

For the normalized torus Fourier expansion the coefficient of `I f` is
`fhat_j/sqrt(5)`. Translation by sigma multiplies that coefficient by
`exp(-iK_j sigma)`. In a product of Fourier coefficients and their
conjugates, translation averaging gives exactly

```text
(1/L_box) integral_0^L_box exp[-i(2pi/L_box) n sigma] d sigma
 =1 when n=0, and 0 for every nonzero integer n.
```

Here n is the signed sum of the participating mode indices. Thus all
canonical-field and momentum moments are explicitly the corresponding
finite word sum, times the products of G or G', the fixed preparation
factors, and this integer-sum indicator. This is a complete moment rule,
not a Gaussian or Wick prescription.

All nonzero-mode means vanish after translation. Covariance is diagonal in
the Fourier mode index; pseudo-covariance pairs opposite indices as required
for real fields. Uniform translation makes the ensemble invariant under all
spatial translations on the torus: translations in the other two directions
act trivially. It does not remove the preferred third axis or populate the
second tensor polarization. No rotational isotropy follows.

The equal-mass word pairing Phi->-Phi leaves S unchanged. It follows that
every tensor-scalar two-point kernel, including arbitrary times and canonical
momenta, vanishes. This zero cross covariance is not independence; both
sectors share the packet, translation and zero event.

For completeness, a pointwise outgoing vector reading can be retained as

```text
v(eta,z)=epsilon_+ sqrt(max(gamma_+(eta,z),0))
         +i epsilon_- sqrt(max(-gamma_+(eta,z),0)).
```

It obeys `v^2=gamma_+` with the same persistent signs. Its full moments are
the explicitly normalized word/sign/translation integrals of these functions.
The roots need not be band limited or differentiable at their zeros. The
primary scalar and tensor fields are smooth solutions; no vector-only action
is obtained by varying through this singular square-root reading. Nor is
interpolating the older vector and then squaring substituted for interpolating
the tensor and then taking roots.

In detail, for any chart point and time p put
`a_p=sqrt(max(gamma_+(p),0))`, `b_p=sqrt(max(-gamma_+(p),0))`.
The vector mean, covariance and pseudo-covariance are

```text
E[v_p]=0,
C_v(p,q)=E_(w,sigma)[a_p a_q+b_p b_q],
P_v(p,q)=E_(w,sigma)[a_p a_q-b_p b_q]=0.
```

The two signs remove the cross terms. Equal-weight pairing of Phi with its
negative, at the same translation and all times, exchanges a with b, proving
the last equality simultaneously for every point pair. In a general finite
real-component product the precise rule is

```text
E[product_p (Re v_p)^n_p (Im v_p)^m_p]
 =1_(sum n_p even) 1_(sum m_p even)
  sum_w nu(w) (1/L_box) integral_0^L_box
       product_p a_p(w,sigma)^n_p b_p(w,sigma)^m_p d sigma.
```

Here `0^0=1`. For finitely many finite times the underlying smooth Fourier
fields are bounded on the compact translation interval. All these integrals
are therefore finite and specify a realizable joint moment law. No Gaussian
closure is used. The quadratic contractions are exactly
`E[v_p^2 conjugate(v_q^2)]=E[v_p^2 v_q^2]=E[gamma_+(p)gamma_+(q)]` in the
marked frame, whose tensor mean vanishes after the source average.

The full vector spectral covariance is the spatial Fourier transform of C_v;
the pseudo-covariance transform vanishes. These kernels are integrable on the
compact torus. Root-vector modes outside the original tensor band are allowed
and are determined by this same kernel; no finite-band assumption is imposed
on the nonlinear roots. The corresponding canonical root is

```text
v_can(eta,z)=[a(eta)/sqrt(2lambda)]^(1/2) v(eta,z),
v_can^2=q_T,+.
```

Its entire state and moments follow by that positive deterministic scaling.
It is distinct from the scalar clock coordinate q_S.

## 7. The translation changes the scalar fluctuation law

At the native onset write

```text
a0=abs(d1)=(e0+e2)/2,
b0=abs(d2)=(e4+e1)/2,
c0=a0+b0.
```

The absolute-value source has outputs `0,a0,b0,c0` with probabilities
`1/3,1/6,1/6,1/3`. Its unshifted mean is

```text
mu=(e0+e1+e2+e4)/4.
```

For j!=0, projecting away the spatial constant does not change the Fourier
coefficient. Define

```text
T_j=E|Phihat_j|^2,
J_j=E|Shat_j|^2.
```

After uniform translation the Fourier mean is zero, so J, the old raw source
second moment, is now the connected scalar variance before its cosmological
conversion. The predecessor's fixed-origin connected intensity power I
instead satisfies

```text
J_j=I_j+|muhat_j|^2=I_j+1/80,  j!=0.
```

Indeed, at a nonzero fifth-root mode the four occupied coefficients of mu
sum to minus the missing root, giving modulus `1/(4sqrt(5))`. Squaring gives
`1/80`. The change is a consequence of a newly selected homogeneous
preparation: the mean profile is translated along with the packet. It is not
a correction to the older fixed-origin result and cannot be omitted while
retaining the new translation law.

For an explicit calculation put `z=exp(-2pi i j/5)` and `theta=2pi j/5`.
Then

```text
d1hat=(1-z^2)/(2sqrt(5)),  d2hat=z^4 d1hat,
a0hat=(1+z^2)/(2sqrt(5)),  b0hat=z^4 a0hat.
```

Using the displayed packet masses gives

```text
T_j=[(1-cos(2theta))/10][1+(2/3)cos(theta)],
J_j=[(1+cos(2theta))/10][1+(2/3)cos(theta)].
```

Therefore the complete nonzero-mode table is

| Modes | T_j | J_j | T_j/J_j |
|---|---|---|---|
| +1,-1 | `(3+sqrt(5))/24` | `(5-sqrt(5))/120` | `5+2sqrt(5)` |
| +2,-2 | `(3-sqrt(5))/24` | `(5+sqrt(5))/120` | `5-2sqrt(5)` |

Both J values and both T values are strictly positive. Their totals over the
four occupied modes are `1/6` and `1/2`, respectively. The zero mode is
absent from both cosmological perturbation seeds by construction.

There is also a direct provenance check. In each individual active source
word, the Fourier tensor and scalar seeds have the same remaining factor
from `{1,z^4,1+z^4}`, up to an overall tensor sign. Their squared modulus
ratio is already

```text
|1-z^2|^2/|1+z^2|^2=tan(theta)^2=5+/-2sqrt(5).
```

Thus within these same seed shapes the mode ratio is insensitive to the
source masses, provided an active source has positive mass. The Thue-Morse
weights still fix the absolute powers and all higher joint moments. They
are not falsely credited with selecting a ratio that this shape identity
already fixes.

## 8. Actual scalar-curvature and metric-tensor powers

The solution coefficients in the normalized torus expansion are

```text
gamma_+,j(eta)=A G_j Phihat_j exp(-iK_j sigma)/(sqrt(5)a),
gamma_x,j=0,
zeta_j(eta)=A G_j Shat_j exp(-iK_j sigma)/(sqrt(30)a).
```

The physical tensor observable selected here is the metric contraction,
not just a sum of vector-doublet coordinates:

```text
P_T(j,eta)=sum_(i,l) E[gamma_il,j conjugate(gamma_il,j)]
         =2 sum_A E|gamma_A,j|^2,
P_S(j,eta)=E|zeta_j|^2.
```

Since all nonzero-mode means vanish, these are connected mode powers. The
polarization norm gives the factor two, and the scalar action plus the equal
canonical seed coefficient gives the factor six between geometric squared
amplitudes. Explicitly,

```text
P_T=2A^2 G_j^2 T_j/(5a^2),
P_S=A^2 G_j^2 J_j/(30a^2).
```

For any occupied mode and epoch with G_j!=0, P_S is strictly positive and

```text
r_T(j,eta)=P_T/P_S=12 T_j/J_j,
r_T(+/-1,eta)=60+24sqrt(5),
r_T(+/-2,eta)=60-24sqrt(5).
```

This is an exact all-epoch statement on positive support. The factor is not
obtained by applying the familiar two-polarization vacuum formula to a
one-polarization non-Gaussian preparation. The complete contractions and
initial data above establish it directly.

The ratio cancels the common amplitude A, transfer G, scale factor, action
conversion and torus Fourier coefficient. H_*, d and ell_0 consequently do
not occur in its values. They still determine the absolute powers, transfer
nodes, physical wave numbers and clock readings. Different contexts are not
physically identified merely because this one ratio agrees.

At launch G=1, and the ratio of total powers in the four occupied modes is
`12(1/2)/(1/6)=36`. This is not the average of the two displayed ratios.
At later epochs the two mode transfers differ, so a summed ratio need not
remain 36 even though each occupied-mode ratio remains as stated.

At a transfer node both powers vanish and r_T is undefined. The same is
true for the unprepared zero mode and every mode outside the finite band.
At A=0, if that boundary is considered, the whole perturbation state is
zero and all its ratios are undefined. No zero-over-zero value is invented.

These per-mode quantities on a finite torus are not asserted to be a smooth
three-dimensional spectral density. An identical convention for mode or
bin factors cancels between numerator and denominator; it cannot create
isotropy or populate missing modes. The fundamental mode is the selected
context pivot, not an externally supplied CMB pivot.

## 9. What is closed conditionally, and what is not derived

The selected model supplies a genuine scalar clock and curvature variable,
their action and constraints, relative tensor normalization, one complete
joint coordinate-and-momentum law, common continuum coordinates and clocks,
and a cosmological tensor-to-curvature ratio on its stated finite band. It
does not obtain the scalar by requiring its later value to equal tensor
intensity. Their identical canonical mode equation comes from the chosen
constant-epsilon background, while their different geometric normalizations
come from the displayed actions.

The decisions remain visible: canonical Einstein-scalar dynamics, the
decelerating epsilon=3/2 branch, the continuum interface, equal canonical
source coefficients, the shared launch momentum, an additional scalar
preparation, a uniform common position law, one polarization and the common
readout convention. Choosing another sound speed, momentum, relative
amplitude or background generally changes the result. Neither symmetry nor
the tensor data alone selects them.

The proof is exact for the quadratic perturbation theory. Its use as a
finite-amplitude approximation to the nonlinear action would require a
separate remainder and backreaction analysis. No microscopic preparation
energy source, quantum vacuum, inflationary origin, SI calibration,
observational CMB comparison or classification of all admissible
normalizations is supplied. The broader registered owner and the proposed
physical gates must be adjudicated separately at their full scopes.
