# K1: local square, a field observation equation, and its finite correlation

**NON-CANONICAL / PROPOSED OBSERVATION / ANALYTIC DERIVATION / NO FORMAL RUN.**
Notes basis: `67a7c03b7a4f37fb9d1d3e0f1150c0b87fc70960`, 2026-09-08.
Scientific authority remains Public Canon v81 as declared by `STATUS.md`.
Owner: `TT-VECTOR-STATE-NORMALIZATION [O]`, unchanged.

This note fixes one local observation of the existing
[K1 source map](V81-TT-K1-SOURCE-MAP-1.md): the traceless quadratic anisotropy
of signed, calibrated transverse electric-field samples. It specifies the
record-to-field map, places the square before the spatial Fourier transform,
and derives its complete finite covariance and normalized two-time
correlation. No actual electric-field archive, apparatus or physical K1
preparation is claimed to have been qualified. This is neither a new
apparatus proposal nor a gravitational-strain identification.

The source and its law are unchanged. The earlier slotwise square remains
the earlier mathematical observable; it is not the Fourier transform of
this local square. No new state or competing closure is introduced.

## 1. One observation equation with physical record keys

The observation consumes five preidentified locations and two preidentified
sampling windows. Its external context is

```text
(X_0, ell>0, e_1, e_2, n, J_0, J_1,
 P_0,...,P_4, raw channel keys, L_acq, o_r, C_r, O_r, E_ref>0).
```

Here `(e_1,e_2,n)` is a common oriented orthonormal frame, and the physical
point labelled `P_r` has independently registered position
`X_r=X_0+r*ell*n`, `r=0,...,4`. These labels and their order come from the
geometry/record metadata, not a permutation chosen from observed values.
`J_0,J_1` are the two fixed acquisition windows with their actual clock
labels and widths. They cannot be reselected by the resulting correlation.
The context is a concrete domain specification for this reading; no supplied
source currently certifies a physical instance of it.

Each point has two fixed raw real channels. `L_acq` is the independently
declared linear extraction of their signed samples in the two windows;
write its output as `y_r(t) in R^2`, `t=0,1`. The fixed offset `o_r`,
calibration matrix `C_r`, and orientation matrix `O_r` give

```text
(E_1(r,t), E_2(r,t))^T = O_r C_r [y_r(t)-o_r],
psi_r(t) = [E_1(r,t) + i E_2(r,t)]/E_ref.
```

`C_r` converts the two raw channels to signed electric-field components in
their documented local axes and units; `O_r` rotates those axes into the
same `(e_1,e_2)` frame. `E_ref` is a fixed independently specified field
reference in the same units. All these maps, offsets, signs and response
conventions are external calibration metadata, not quantities fitted from
the K1 target correlation. Intensity-only or unspecified polarization
records do not supply this signed two-component input. No Stokes or
intensity substitution is made.

The chosen local output is exactly

```text
q_+(r,t)     = Re[psi_r(t)^2] = (E_1^2-E_2^2)/E_ref^2,
q_cross(r,t) = Im[psi_r(t)^2] = 2 E_1 E_2/E_ref^2.
```

Its physical tensor notation, using the fixed transverse basis, is

```text
E_plus  = e_1 e_1^T - e_2 e_2^T,
E_cross = e_1 e_2^T + e_2 e_1^T,
Q = q_+ E_plus + q_cross E_cross.
```

Thus `Q` is the explicitly defined transverse, trace-free quadratic
anisotropy of the calibrated projected electric-field sample. The words
plus and cross name the components of this tensor in the common frame.
This identifies a measurable quadratic functional once its input record
and calibration are qualified. It does not identify `Q` with gravitational
metric strain, a Maxwell stress tensor, an energy density or a source of
gravitational waves.

The operator order is part of the measurand:

```text
raw signed channels -> fixed linear acquisition/extraction -> calibration
 -> common real basis -> local complex square -> spatial Fourier/readout.
```

If `L_acq` averages a field over a window, this definition squares that
calibrated averaged field. It does not recover the average of its square.
In general `(L_acq E)^2 != L_acq(E^2)`. Moving an acquisition filter,
calibration mixing or spatial mixing through the square changes the
observable and is not licensed by the covariance transport below.

## 2. The unchanged K1 source has a definite local inverse

Retain the ten-word source `w` and its probabilities from the K1 note.
Its two overlapping windows give `u_t=b_(t+2)-b_t in {-1,0,1}` and, in
row/column order `(-1,0,1)`,

```text
p = (1/3,1/3,1/3)^T,
P = Law(u_0,u_1) = (1/12) [[1,1,2],[1,2,1],[2,1,1]].
```

Set `z=exp(2*pi*i/5)` and use the same unitary convention

```text
F_unitary(a)_x = (1/sqrt(5)) sum_r a_r z^(rx),
F_unitary^-1(b)_r = (1/sqrt(5)) sum_x b_x z^(-rx).
```

The original K1 field is
`vhat_x(t)=(1+z^x) z^(x u_t)/sqrt(10)`.
Finite character orthogonality gives its **exact local inverse**

```text
b_r(t) = F_unitary^-1(vhat(t))_r
       = [delta_(r,u_t) + delta_(r,u_t+1)]/sqrt(2).
```

The deltas use `Z/5`; `b` is real. This inverse is supplied by the fixed
K1 map, not a new choice of its state law. Its cyclic coefficient indexing
is used by the finite transform; it does not certify periodic physical
boundary conditions at the endpoints of the observed five-point sample.

The candidate physical observation equation is now explicit:

```text
psi_r(t) = a b_r(t),       a>0 fixed and common to both windows,
q_+(r,t) = a^2 h_r(t),     q_cross(r,t)=0,
h_r(t) = b_r(t)^2 = [delta_(r,u_t)+delta_(r,u_t+1)]/2.
```

`a` is the field amplitude relative to the external `E_ref`. The original
dimensionless K1 normalization is `a=1`; no physical value of `a` is
deduced here. The correlation below cancels this common scale. The
identification of the two physical windows with one K1 source pair is an
explicit candidate equation, not a derivation of a clock interval or a
physical preparation law. The pair is never replaced by two independent
draws.

For an imperfect calibrated record one must instead retain its actual
residual, `psi_obs=a b+eta`. Then exactly

```text
q_obs = a^2 b^2 + 2 a b eta + eta^2.
```

No distribution, independence, zero bias or removable covariance of `eta`
is assumed. The finite prediction below applies to the stated K1 equation;
an empirical comparison cannot treat unexplained response/noise terms as
zero or subtract them by fitting the desired correlation. This is the
remaining qualification boundary for a real record, not a second readout.

## 3. Local square before Fourier: the required correction

For arbitrary coefficient fields the chosen Fourier convention gives

```text
F_unitary(b^2)_x = (1/sqrt(5)) sum_y vhat_y vhat_(x-y),
```

a cyclic convolution, not `vhat_x^2`. In this particular K1, each local
coefficient is zero or `1/sqrt(2)`, so `b^2=b/sqrt(2)` pointwise. Therefore

```text
hhat_x(t) = F_unitary(h(t))_x
         = vhat_x(t)/sqrt(2)
         = c_x z^(x u_t),       c_x=(1+z^x)/sqrt(20),
qhat_+(x,t) = a^2 hhat_x(t),    qhat_cross(x,t)=0.
```

This is the one readout used from here onwards. `x` remains a finite
analysis-channel index. With the physical positions above its character
has the sampled spatial frequency `k_x=2*pi*x/(5*ell)`, where indices
`0,1,2,3,4` represent signed indices `0,1,2,-2,-1`. The convention uses
`+k_x` in the forward transform. These are finite sampled characters,
not a proof of propagating modes or cosmological wave numbers.

`qhat_+` is complex because it is a Fourier coefficient of a real plus
field. Its imaginary part is a spatial sine component, **not cross
polarization**. Cross polarization is separately zero for this candidate
in the fixed frame. All five channels and their coherent means are retained.

The new local covariance is not obtained by taking an inverse Fourier
transform of the old covariance of `vhat^2`: those are different quadratic
observables. It is derived below from the already complete unchanged K1
source. Only after the correct local square is formed can its covariance
be transported linearly.

## 4. Full covariance, including spatial and time cross terms

A real matrix representation makes every local component explicit. In
site order `(0,1,2,3,4)` and source order `(-1,0,1)`, put

```text
A = [[1,1,0],
     [0,1,1],
     [0,0,1],
     [0,0,0],
     [1,0,0]],
h(t) = (1/2) A e_(u_t),
mu_h = (1/2) A p = (1/6)(2,2,1,0,1)^T.
```

For `t,s in {0,1}`, the entire local centered covariance is

```text
Gamma_h(t,t) = (1/4) A [diag(p)-p p^T] A^T,
Gamma_h(0,1) = (1/4) A [P-p p^T] A^T,
Gamma_h(1,0) = Gamma_h(0,1)^T.
```

These are exact finite matrices, not diagonal-spectrum approximations.
For direct entrywise evaluation their middle matrices are

```text
diag(p)-p p^T = (1/9) [[2,-1,-1],[-1,2,-1],[-1,-1,2]],
P-p p^T = (1/36) [[-1,-1,2],[-1,2,-1],[2,-1,-1]].
```

The real tensor-component covariance has plus/plus block
`a^4 Gamma_h(t,s)` and zero plus/cross, cross/plus and cross/cross blocks;
its mean is `(a^2 mu_h,0)`. This is the complete covariance in the chosen
common basis, with no spatial homogeneity assumption.

For an equivalent spectral expression, retain the source polynomials

```text
f(m) = (z^(-m)+1+z^m)/3,
g(m,n) = (1/12) [z^(-m-n)+z^(-m)+2 z^(-m+n)+z^(-n)+2+z^n
                              +2 z^(m-n)+z^m+z^(m+n)],
D_ts(m,n) = f(m+n) if t=s, and g(m,n) otherwise.
```

Then the spectral mean, Hermitian covariance and pseudo-covariance are

```text
mu_qhat(x,t) = a^2 c_x f(x),
K((x,t),(y,s)) = a^4 c_x conjugate(c_y)
                  [D_ts(x,-y)-f(x)f(y)],
L((x,t),(y,s)) = a^4 c_x c_y
                  [D_ts(x,y)-f(x)f(y)].
```

They agree with `K=F Gamma F^dagger` and `L=F Gamma F^T`, with the
time-block Fourier map understood. `K` and `L` retain the cross-channel
terms; they are not replaced by five independent spectral powers.
The pseudo-covariance is required when the final readout mixes real and
imaginary spatial components.

The observation's fixed direct Fourier channels have just been specified.
If their recorded readout includes an independently fixed linear filter or
mixer **after** the square, its covariance transport is exact. For a real
map `M` on the stacked `(site,time,polarization)` record,

```text
mu_out = M mu_q,       Gamma_out = M Gamma_q M^T.
```

For a complex map `W` on the stacked Fourier channels,

```text
mu_out = W mu_qhat,
K_out = W K W^dagger,       L_out = W L W^T.
```

These formulas include temporal filters and spatial/polarization mixing
when present in that declared linear output map. They apply after local
squaring; they do not move such a filter to its input side. In general a
mixed output has a different normalized correlation from an individual
channel. The values in the next section belong to the specified direct
channels; they are not claimed invariant under arbitrary filtering.

## 5. The finite prediction and the reviewed slotwise values

For each nonzero direct channel define its two-window Hermitian correlation
by

```text
R_x^local = K((x,0),(x,1)) /
           sqrt(K((x,0),(x,0)) K((x,1),(x,1))).
```

Both marginal variances are equal and positive. The known finite law gives

```text
g(m,-m)=1/6                    for m!=0 mod 5,
f(1)=f(4)=(1+sqrt(5))/6,
f(2)=f(3)=(1-sqrt(5))/6,
R_x^local = [1/6-f(x)^2]/[1-f(x)^2].
```

To check the first equality by hand, its numerator in `12*g(m,-m)` is
`4+2(z^m+z^(-m)+z^(2m)+z^(-2m))=4-2=2`, since the four exponents exhaust
the nonzero residues. The two displayed values of `f` are the real
fifth-root identities. Substitution, with no numerical execution, yields

| Channel | This local-square readout | Earlier slotwise-square readout |
| --- | --- | --- |
| `x=1,4` | `-(3 sqrt(5)+1)/44` | `(3 sqrt(5)-1)/44` |
| `x=2,3` | `(3 sqrt(5)-1)/44` | `-(3 sqrt(5)+1)/44` |
| `x=0` | Undefined: connected variance is zero | Undefined: connected variance is zero |

Thus the reviewed algebraic values for the earlier slotwise square are
correct: that observable uses `f(2x)` instead of `f(x)`. Multiplication by
two interchanges the two nonzero channel pairs. The local square therefore
**exchanges their assignments**. Both nonzero values obey

```text
44 R^2 + 2 R - 1 = 0.
```

For example, when `x=1,4`,
`f(x)^2=(3+sqrt(5))/18` gives
`R=-sqrt(5)/(15-sqrt(5))=-(3 sqrt(5)+1)/44`.
The other pair uses `(3-sqrt(5))/18` and gives the positive root.
At `x=0`, `hhat_0=1/sqrt(5)` is constant, so the correlation is `0/0`;
assigning it zero would change the definition.

The common physical field factor `a` contributes `a^4` to each covariance
and cancels exactly in this normalized correlation. This is a cancellation
within the same field/readout law. It does not cancel unknown noise,
justify a new scalar spectrum, determine an action normalization or
produce a tensor-to-scalar ratio. The predicted finite signed correlation
is conditional on the complete source and observation equation above.

## 6. What this physical reading does and does not establish

The observation functional now has physical record semantics: signed
electric-field components at named points/windows, a common transverse
basis, a specified calibration and an explicit local quadratic output.
Its chosen square has the registered double-angle transformation law and
`det(I+H)=1-|psi|^4` for the associated two-by-two traceless matrix. Those
identities do not establish that the electric-field anisotropy is a
gravitational field or satisfies a TT propagation equation. Neither a
physical source/preparation realizing the ten-word law nor the required
record/calibration instance has been supplied or certified in this work.

There is no scalar denominator hidden in the construction. The original
slot norm
`|vhat_x|^2=(2+z^x+z^(-x))/10` is deterministic, so its connected variance
vanishes in every slot. The local intensity `|b_r|^2` equals `h_r` for this
real K1 source; that equality does not independently identify it as a
cosmological scalar perturbation. Neither quantity is adopted as `P_S(k)`.

The concrete advance is the fixed order of the physical observation and
the resulting exact change in the channel correlation, with full
covariance transport supplied. The statement remains conditional finite
analysis in notes. It closes no original O/H, adds no formal T or gate,
and makes no numerical `r_T(k)` or empirical success claim.

## Sources

- [K1 source map](V81-TT-K1-SOURCE-MAP-1.md), sections 1-4: unchanged
  source, ten-word law, Fourier convention and moment polynomials.
- [TT closure input](V81-TT-NORMALIZATION-CLOSURE-INPUT-1.md), sections
  2-3: connected quadratic covariance, two-time scope and scalar boundary.
- [Canon section 14](../canon/CANON.md): registered complex square,
  `POL-READ`, determinant identity and limits of physical normalization.

The electric-field observation equation is an explicitly proposed physical
reading in this note. No external experiment is cited as having realized
it; consequently no instrument-performance or data-availability claim is
made without a primary source.
