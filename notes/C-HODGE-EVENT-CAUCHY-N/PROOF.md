# Stable scalar propagation on selected Hodge events

Status: PUBLIC NON-CANONICAL. candidate-T consequences of the explicitly
selected candidate-D dictionaries. No Canon or physical-photon promotion.
Author: A. M. Thorn <thorn@twistj.com>. Owner: #1239.
Prospective source pin: 19804efeae85c5514a0801960d76612c8bba51bb.

## 1. Inputs, equality and the selected event subcarrier

Use the inherited marked E=E_+, embedding i into W_R, metric g=i^T beta i,
orthogonal projector Pi, internal projector N=I-Pi and windowed set M.
The predecessor proves that rho_H(y)=Pi rnd(H i y)/H belongs to M/H and

    ||rho_H(y)-i y||_* <= R/H,       R=10-9sqrt5/5.

The norm is max(|tau|,sqrt(g(spatial,spatial)/ct)), where t is the fourth
marked basis vector, tau(t)=1 and ct=-g(t,t). The inherited algebraic g
in the original E coordinates is

    (sqrt5/10)(2I3+11^T) direct-sum [-(2+sqrt5)/8].

Choose, as in the preceding field note, the orthogonal frame

    t=(0,0,0,1), s1=(1,-1,0,0), s2=(1,1,-2,0), s3=(1,1,1,0).

Its norms are -ct,a1,a2,a3 with

    ct=(2+sqrt5)/8,
    a1=2sqrt5/5, a2=6sqrt5/5, a3=3sqrt5/2.

Every ai>ct>0. Also 0<R<6: the upper bound is equivalent to
sqrt5>20/9, whose square is 405>400. No decimal test is used.

For integer n>=3 put delta=1/n, H=n^4. The marked ideal grid and its actual
event image are

    y(m,z)=delta*(m*t+sum_i z_i*s_i),
    w(m,z)=rnd(H i y(m,z)) in Z^6,
    e(m,z)=Pi w(m,z)/H,              (m,z) in Z x Z^3.

All field sites are actual admitted windowed events. The global error is
bounded by r_n=R delta^4 in ||.||_*.

### Injection and geometry of the marked slices

Distinct ideal grid points have distance at least delta: differing m gives
a time separation >=delta; if m agrees, orthogonality and ai/ct>1 give
spatial norm >=delta. Thus their event images differ by at least

    delta-2r_n>0,

because n^3>=27>2R. The embedding is injective on the whole infinite grid.
It is a bijection only onto Gamma_n=image(e), NOT onto M/H.

Within one m slice, two distinct points have spatial norm >=delta-2r_n
and time difference <=2r_n. Since n^3>4R, every such pair is spacelike.
For fixed z, successive m points have time difference >=delta-2r_n and
spatial norm <=2r_n, so they are future timelike. The marked slices are
antichains and the same-site lines are chronological mathematical clocks.
Their segment proper lengths are sqrt(ct)*delta+O(delta^4), not an exact
identification with METRO-TICK or the native counter.

The ideal grid is a full rank-four lattice in E_R with covering radius
C_frame*delta. Its perturbation Gamma_n therefore has covering radius
C_frame*delta+r_n and separation >=delta-2r_n. It is locally finite and
approximates E_R at O(delta). The event family, marked foliation and norm
are selected data, not derived unique physical data.

## 2. A new spatial operator, not the old all-event Box_n

Pull scalar values on Gamma_n back through the injection to f_m(z).
Do not assign fields to the unselected events M/H minus Gamma_n.
On l2(Z^3) use the counting inner product; for complex scalars use its
Hermitian version and real parts in energy cross terms. Let T_i be unit
translation in z_i and set

    K=sum_i alpha_i(2I-T_i-T_i^-1),       alpha_i=ct/ai.

Exactly,

    alpha1=(5+2sqrt5)/16,
    alpha2=(5+2sqrt5)/48,
    alpha3=(5+2sqrt5)/60,
    A=sum_i alpha_i=1/2+sqrt5/5<1,
    eta=1-A=(5-2sqrt5)/10>0.

The inequality follows from 25>20. These coefficients follow from g and
the chosen orthogonal rectangular stencil. Selecting the stencil is an
additional choice; metric matching alone does not select all possible
finite-difference schemes.

For every finitely supported f,

    <f,Kf>=sum_i alpha_i ||(T_i-I)f||^2.

Hence K is self-adjoint, positive and bounded by 4A I. The same properties
extend by continuity to l2. This is a spatial Hilbert-space operator after
the stated slice and counting norm have been selected. It is not a claim
about a physical L6 measure or self-adjointness of the predecessor Box_n.

## 3. Exact Cauchy evolution and energy

Freeze the scalar rule

    f_(m+1)-2f_m+f_(m-1)+K f_m=delta^2 j_m.             (1)

Every pair of finitely supported F-valued slices and every finite forcing
prefix determine a unique matching solution prefix. A specified all-time
source, including the zero source, determines all-time continuation.
Solving (1) for the oldest slice
also gives an exact inverse when the source is known. Finite support grows
by at most one nearest-neighbor spatial step per update, plus source support.
All F arithmetic is a pair of rational coefficients, hence representable
by integers and denominators without rounding field values.

Define

    E_m=1/2||f_(m+1)-f_m||^2+1/2 Re<f_(m+1),K f_m>.

Writing v=f_(m+1)-f_m and a=(f_(m+1)+f_m)/2 gives

    E_m=1/2<v,(I-K/4)v>+1/2<a,Ka>
          >= eta ||v||^2/2.                            (2)

This is nonnegative. If it vanishes, eta>0 forces v=0 and the edge-sum
formula forces a to be constant on connected Z^3. A finite-support or l2
constant is zero. Thus E is strictly positive on every nonzero pair in
these spaces. It does not bound the unweighted position norm uniformly
away from zero frequency. On a finite periodic audit box a constant pair
has zero energy; that control must not be mistaken for the infinite-grid
strict-positivity claim.

Taking the inner product of (1) with f_(m+1)-f_(m-1) and using symmetry
of K proves the exact work identity

    E_m-E_(m-1)=delta^2 Re<j_m,f_(m+1)-f_(m-1)>/2.      (3)

In particular E is conserved in the absence of forcing.

For unforced solutions and ||f||_delta^2=delta^3 sum_z |f(z)|^2, the
conserved scaled energy is E_delta=delta E. Equation (2) implies

    ||(f_(m+1)-f_m)/delta||_delta^2 <= 2 E_delta/eta,
    ||f_m||_delta <= ||f_0||_delta+m delta sqrt(2E_delta/eta).

This supplies finite-time energy stability with a fixed positive margin,
not a spectral mass gap or a claim of bounded position for infinite time.

## 4. Retarded Green function and sharp-enough stability bounds

Let G_0=0, G_1=I and

    G_(r+1)=(2I-K)G_r-G_(r-1).

These are finite convolution operators. Their support lies in the integer
l1 ball of radius r-1 for r>=1. Induction in (1) gives, for m>=1,

    f_m=G_m f_1-G_(m-1) f_0
          +delta^2 sum_(j=1)^(m-1) G_(m-j) j_j.         (4)

No source affects an earlier marked time. This is retardedness in the
selected foliation and finite stencil dependence, not yet Lorentz-cone
support in the actual event metric.

On a Fourier character with angles theta in [-pi,pi]^3,

    kappa(theta)=4 sum_i alpha_i sin^2(theta_i/2),
    0<=kappa<=4A<4.

Set cos omega=1-kappa/2, omega in [0,pi). The G_r multiplier is
sin(r omega)/sin omega, with limit r at omega=0. The elementary finite
geometric-sum identity bounds its absolute value by r. Parseval therefore
proves

    ||G_r||_(l2->l2)<=r.                               (5)

This is enough for the finite-time convergence below.

For completeness, an additional bound controls bounded but non-l2 initial
rounding errors of plane waves. Away from theta=0, the same multiplier is
bounded by 1/|sin omega|. With U=sum alpha_i sin^2(theta_i/2),

    sin^2 omega=4U(1-U)>=4(1-A)U.

On the Fourier cube sin^2(theta_i/2)>=theta_i^2/pi^2, so
1/sin^2 omega<=C/|theta|^2. The latter function is integrable in dimension
three. Parseval bounds the l2 norm of the convolution KERNEL of G_r by a
constant C_G independent of r. Its support has at most (2r+1)^3 sites, so
Cauchy-Schwarz gives

    ||kernel(G_r)||_l1 <= C_G(2r+1)^(3/2).              (6)

Both (5) and (6) are mathematical bounds on the selected operator, not
finite-range extrapolations. Formula (4) is pointwise meaningful for bounded
initial fields because each kernel has finite support.

## 5. Stable finite-time continuum approximation

Use coordinates (tau,x1,x2,x3) in the nonnormalized orthogonal frame
(t,s1,s2,s3). The limiting equation of (1) without source is

    f_tautau=sum_i alpha_i f_xixi,

which is precisely Box_g f=0 after multiplication by -ct. In particular the
continuum principal metric is the inherited g, not an inserted extra metric.

Let f be a C4 solution on a neighborhood of 0<=tau<=T, uniformly supported
in a fixed compact spatial set there, with bounded derivatives through
order four. For v_m(z)=f(m delta,z delta), Taylor's theorem and cancellation
of the odd central moments give the unscaled defect

    d_m=v_(m+1)-2v_m+v_(m-1)+K v_m,
    ||d_m||_delta<=C_f delta^4.                        (7)

There are O(delta^-3) nonzero sites and uniformly bounded fourth derivatives;
this explains the norm estimate, rather than inferring it from a pointwise
bound without counting the support.

Initialize the exact recurrence with f_0=v_0, f_1=v_1. Apply (4)-(5) to the
error driven by -d_m. For m delta<=T,

    ||f_m-v_m||_delta
       <= C_f delta^4 sum_(r=1)^(m-1) r
       <= (C_f T^2/2) delta^2.                         (8)

Evaluating the smooth reference at the actual rounded event e(m,z) instead
of y(m,z) changes it by O(delta^4); its supported norm has the same order.
Thus (8) remains O(delta^2) for values compared at actual events. Samples
from a smooth reference need not lie in F; this convergence theorem uses the
explicit real/complex extension of the same exact coefficient law. The
executable finite-support rational/algebraic evolution is a separate scope.

The theorem is conditional on the stated smooth reference solution and
initialization. It is not a claim of convergence for arbitrary rough data,
all times growing faster than delta^-1, or every physical source.

## 6. The D3 comparison now has exact evolving event fields

This section uses only the inherited LOCAL principal-root bound, not global
D3 carrier equivalence. Let coframe momenta k range over a fixed bounded
lifted set. Use the orthonormal Hodge frame t/sqrt(ct), si/sqrt(ai).
For epsilon=delta let Omega_D(delta,k) be either principal D3 root. Set

    nu=sqrt(ct) Omega_D(delta,k),
    xi_i=sqrt(ai) k_i,
    V_m(z)=exp(i delta*(sum_i xi_i z_i-nu m)).

The inherited bound gives

    |Omega_D^2-|k|^2|<=C_K delta^2,
    |nu^2-sum_i alpha_i xi_i^2|<=ct C_K delta^2.

Expanding only the central sine symbols, with bounded frequencies, yields

    V_(m+1)-2V_m+V_(m-1)+K V_m = b_delta V_m,
    |b_delta|<=C'_K delta^4.                           (9)

Initialize an EXACT solution F_m of (1) with the corresponding plane-wave
values at the ACTUAL rounded events e(0,z),e(1,z), using the same covector.
Their difference from V_0,V_1 is bounded uniformly by C''_K delta^4.
Formula (4) separates the resulting error into two parts:

1. The forcing (9) is a single spatial character. Bound each G_r multiplier
   by r, giving O_T,K(delta^4 m^2)=O_T,K(delta^2).
2. The initial rounding errors are bounded, not asserted to be l2. Use the
   convolution-kernel bound (6), giving
   O_T,K(delta^4 (m+1)^(3/2))=O_T,K(delta^(5/2)).

Finally the plane wave at e(m,z) differs from V_m(z) by O_K(delta^4).
Therefore

    sup_(0<=m delta<=T,z in Z^3,|k|<=K)
      |F_m(z)-exp(i covector_(delta,k)(e(m,z)))|
          <= C_(T,K) delta^2.                         (10)

Each F is a true solution of the selected event recurrence, not merely a
field with small residual. The source plane waves have infinite energy and
are treated as bounded fields, not as finite-support energy fixtures.

Equation (10) supplies local finite-time scalar-mode agreement. It does NOT
make the new finite-scale dispersion equal to the old D3 dispersion. It
selects no global reciprocal-torus map, full field-space identification,
action/measure transfer, vector gauge sector, or physical photon.

## 7. Group speeds lie inside the limiting cone, but support does not

The selected grid dispersion is

    sin^2(omega/2)=U=sum_i alpha_i sin^2(theta_i/2).

Because 0<=U<=A<1 it has two real principal branches, meeting only at the
unique zero character. The zero transfer is nonidentity unipotent, not a
positive spectral gap. For a nonzero character the squared group speed in
the orthonormal Hodge frame is

    |v_group|^2=sum_i alpha_i sin^2(theta_i)/sin^2(omega).

Indeed the coordinate derivative is alpha_i sin(theta_i)/sin(omega), and
conversion of space/time units multiplies its square by ai/ct=1/alpha_i.
Put u_i=sin^2(theta_i/2) and S2=sum_i alpha_i u_i^2. The exact identity

    S2-U^2=(1-A)S2+sum_(i<j)alpha_i alpha_j(u_i-u_j)^2>=0

gives |v_group|^2=(U-S2)/(U-U^2)<=1. This is a statement about characters
of the marked graph and the ideal limiting frame. The rounded event set is
not translation invariant and is not assigned a separate exact global
Fourier basis by this statement.

Group speed is NOT the speed of the support boundary. Start with f_0=0,
f_1=delta_0. At the next slice f_2(e_i)=alpha_i!=0, although the ideal
source-to-neighbor displacement is delta(t+s_i), of squared interval

    delta^2(ai-ct)>0.

The exact audit also exhibits this spacelike displacement after rounding
at n=8, between e(1,0) and e(2,(1,0,0)). Thus exact microscopic support
inside the inherited Lorentz cone FAILS for this selected scheme. Its
retardedness is in marked m, and the limiting differential operator has
the Hodge characteristic cone. Neither fact erases that microscopic
limitation or proves a sharp Green-function support limit for singular data.

## 8. Choice ledger and result boundaries

The selected mathematical construction now has actual discrete events,
spacelike marked slices, chronological same-site lines, a unique reversible
scalar evolution, positive conserved energy, retarded Green functions and
controlled finite-time approximation of the inherited flat wave geometry.

The additional choices are not hidden: E+ and its real sign, the earlier
window, marked frame and rectangular subcarrier, deterministic rounding,
H=n^4 versus delta=1/n, slice counting norm, nearest-neighbor scalar law,
and initial data. The numerical coefficients are fixed once these are fixed.
The labels (m,z) are not identified with the native state Omega. Galois
physical equivalence and physical branch selection are not proved here.

CB-EVENT-MESH and CB-EVENT-SCALAR-EVOLUTION are only candidate dictionary
bridges as frozen in PREREG.md. All existing public gate/status owners are
unchanged. This is a consistent propagating flat SCALAR model on a selected
subcarrier, not a completed fundamental spacetime or photon theory.
