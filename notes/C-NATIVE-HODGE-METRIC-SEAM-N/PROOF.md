# Hexagonal native cover and the Hodge spatial metric

Status: PUBLIC NON-CANONICAL.
Author: A. M. Thorn <thorn@twistj.com>. Owner: #1251.
Prospective pin: e0118a96f999e51ad623bb3cbc7954c38bd634a0.

The theorem-grade statements below are exact consequences of the frozen
mathematical inputs. The choice to adopt the Hodge member is candidate-D,
not a native derivation.

## 1. The linear seam hidden inside the tagged cube construction

The selected fired-commutator cover has coordinates (x,y) in Z^2 and six
unit steps

    +/-e1, +/-e2, +/-(e1+e2).

The N2 tagged cube construction uses cube coordinates z=(a,b,c) with

    x=a-c,   y=b-c.                                   (1)

The unique representative of these differences in the zero-sum plane

    P={z in R^3 : z1+z2+z3=0}

is

    p(x,y)=((2x-y)/3,(-x+2y)/3,(-x-y)/3).             (2)

Direct expansion gives

    ||p(x,y)||^2=(2/3)(x^2+y^2-xy).                  (3)

Thus the six selected unit steps all have Euclidean squared norm 2/3 in P.
They form one regular hexagonal orbit.

Let

    d=(1,1,1).

The explicit N2 map is

    Phi(r,x,y)=(x+c,y+c,c),
    c=r-max(0,x,y).

At fixed x,y, increasing r by one increases c by one, hence

    Phi(r+1,x,y)-Phi(r,x,y)=d.                        (4)

So the third direction added by tagged accumulation is exactly the diagonal
line D=R d. Equations (1)-(4) supply the linear P plus D decomposition behind
the nonlinear shell enumeration.

This statement does not say that the tag is a native metric direction. It
identifies the geometry of the already selected completion.

## 2. Complete quadratic metric class under the cover symmetry

Grant the full abstract automorphism symmetry of the selected regular
hexagon on P, while D is the distinguished tagged line. This is a symmetry
of the selected cover convention, not a claim that every such automorphism
acts on native U.

It is enough to use the coordinate-permutation subgroup S3. Let Q be a
symmetric bilinear form on R^3 invariant under every coordinate permutation.
Transpositions force the three diagonal matrix entries to agree and the
three off-diagonal entries to agree. Therefore uniquely

    Q = alpha I_3 + beta 11^T.                        (5)

Conversely every form (5) is permutation invariant. The zero-sum plane P
and diagonal line D are eigenspaces:

    Q|P has eigenvalue alpha,
    Q|D has eigenvalue alpha+3 beta.                  (6)

They are Q-orthogonal. The other abstract hexagon automorphisms act within P
and impose no further scalar on its irreducible two-dimensional plane.

For a cover unit u=p(1,0), equation (3) gives

    Q(u)=2 alpha/3.

Normalize the selected cover unit convention by Q(u)=1. Then

    alpha=3/2.                                        (7)

Define the remaining dimensionless invariant

    rho=Q(d).

By (5),

    rho=3 alpha+9 beta,

so (7) gives

    beta=rho/9-1/2.

Hence the COMPLETE normalized family is

    Q_rho=(3/2)I_3+(rho/9-1/2)11^T.                  (8)

Its two eigenvalues are

    3/2 on P,
    rho/3 on D.

Therefore

    Q_rho is positive definite iff rho>0.             (9)

There is exactly one positive dimensionless metric parameter left after the
cover unit length is fixed.

Every Q_rho with rho>0 is uniformly comparable to Euclidean distance because
its smallest and largest eigenvalues are positive finite constants. Therefore
every such metric on Z^3 has cubic large-scale ball growth. Prefix consistency
of the N2 archive also holds for every fixed rho because old coordinates and
the metric formula are never changed. Cubic growth and immutable overlaps
cannot select rho.

## 3. The exact Hodge member

The accepted fixed-J Hodge spatial block is

    q_H=(sqrt5/10)(2I_3+11^T).                        (10)

For the same cover unit u=p(1,0), using sum(u)=0 and ||u||^2=2/3,

    q_H(u)
      =(sqrt5/10)*2*(2/3)
      =2sqrt5/15.                                     (11)

For d=(1,1,1),

    q_H(d)
      =(sqrt5/10)*(2*3+9)
      =3sqrt5/2.                                      (12)

Thus the scale-free ratio is exactly

    rho_H=q_H(d)/q_H(u)=45/4.                         (13)

Divide (10) by (11). The square root cancels completely:

    Q_H,norm
      =(3/4)(2I_3+11^T)
      =(3/2)I_3+(3/4)11^T
      =Q_(45/4).                                      (14)

So once a native cover unit is declared to have squared length one, the
selected Hodge spatial metric becomes rational.

This is a useful exact seam. It is not a derivation of (13) from U.

## 4. Explicit nonselection

Take instead

    Q_E=(3/2)I_3.                                     (15)

It is positive definite, invariant under the full coordinate-permutation
symmetry, and gives every cover unit squared length one. Yet

    Q_E(d)=9/2,                                       (16)

whereas the Hodge member has 45/4.

Both metrics have cubic large-scale ball growth on Z^3 and both are compatible
with the same immutable N2 coordinate archive. Therefore the frozen conditions

- the selected six-step commutator cover,
- its abstract hexagonal symmetry,
- positive definiteness,
- unit cover-step normalization,
- tagged Z^3 completion,
- prefix consistency, and
- cubic metric growth

do NOT select the Hodge metric.

The nonuniqueness is continuous: every rho>0 in (8) is admitted.

## 5. Selected Hodge seam

There is nevertheless a clean candidate-D closure if one states the choice
instead of disguising it as a theorem.

Adopt independently the already accepted fixed-J Hodge target E+ and identify
the selected cover difference plane with the zero-sum plane P of its marked
spatial coordinates. Normalize one selected commutator-cover unit to squared
length one.

Then (11)-(14) leave no additional spatial metric parameter:

    boxed Q_space = Q_(45/4).                         (17)

This dictionary consumes two inputs:

1. the selected commutator cover/completion;
2. the independently selected Hodge target.

It does not show that native U forces the second input. Within that declared
dictionary, however, the spatial metric is exact and parameter-free up to the
already removed overall scale.

## 6. Full normalized flat Lorentz form

The fourth marked E+ basis vector has exact squared norm

    -ct,   ct=(2+sqrt5)/8.                            (18)

Use the same positive normalization factor as in (14),

    lambda = 1/q_H(u)=15/(2sqrt5).

Then

    lambda ct
      = 15(2+sqrt5)/(16sqrt5)
      = (15+6sqrt5)/16.                              (19)

The selected normalized flat Lorentz metric is therefore

    g_norm =
      Q_(45/4) direct-sum [-(15+6sqrt5)/16].          (20)

The spatial eigenvalues are positive and the last coefficient is negative,
so the signature is exactly (3,1).

Multiplication of (20) by any positive scalar does not alter its null set.
Thus (20) fixes the scale-free flat cone once the candidate-D Hodge seam is
adopted.

This does not calibrate an SI length or time. It does not identify the N2
generation counter with event time, and it does not identify one event step
with METRO-TICK. The event resolution h also remains outside this theorem.

## 7. What is now closed and what is not

At this selected mathematical scope the metric problem is reduced to one
precise statement.

Before Hodge adoption, the native-cover/generative architecture admits the
one-parameter family Q_rho, rho>0. After independent Hodge adoption, the seam
fixes

    rho=45/4

and the complete scale-free flat Lorentz metric is (20).

Therefore any future claim that the existing native architecture DERIVES the
Hodge metric needs a new metric-sensitive native law that fixes rho=45/4, or
an exactly equivalent invariant condition. Reusing q_H itself to choose rho
is circular for such a derivation claim.

The previous exact microscopic spacelike one-hop response of the selected
scalar stencil remains unchanged. No photon-cone equality, physical Galois
equivalence, occurrence law, L6 measure, SI scale or curvature theorem is
obtained here.
