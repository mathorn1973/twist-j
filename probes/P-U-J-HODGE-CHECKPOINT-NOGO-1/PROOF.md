# Finite readers and the periodic part of the J-Hodge step

**L1 proof submission. No Canon promotion or physical interpretation.**

The definitions, equality and scope are exactly those of PREREG.md.
The elementary finite-orbit principle is classical linear algebra. The
purpose here is its precise application to the marked J-Hodge operator,
its predictive carrier, and fixed native free-linear codes.

## 1. The rational split

C is the coordinate five-cycle on the augmentation representation. It is
H-orthogonal, has order five and has characteristic polynomial Phi_5.
Over C choose eigenvectors f_a with eigenvalue j^a, a=1,2,3,4,
where j is the primitive fifth root fixed by the marked cycle. Then

```text
M f_a=(1+j^(2a))f_a;
A(f_a wedge f_b)=j^(a+b)(f_a wedge f_b);
L(f_a wedge f_b)=(1+j^(2a))(1+j^(2b))(f_a wedge f_b).
```

These six wedge eigenvectors form a basis. Averaging powers of A gives
T=1 on the two pairs (1,4),(2,3) and T=0 on the other four. Therefore
T,R are complementary rational projectors of ranks two and four; they
commute with L. On im T the two multipliers are

```text
(1+j^2)(1+j^3)=2+j^2+j^3=(3-sqrt(5))/2=phi^-2;
(1+j^4)(1+j)=2+j+j^4=(3+sqrt(5))/2=phi^2.
```

On im R the four multipliers, in pair order (1,2),(1,3),(2,4),(3,4), are

```text
-j^3, -j^4, -j, -j^2.
```

For example (1+j^2)(1+j^4)=1+j+j^2+j^4=-j^3 by Phi_5(j)=0.
All four are distinct primitive tenth roots. Thus p(L)T=0, q(L)R=0,
L is invertible, and L^5 R=-R. The matrices generated in G1-G5 audit
these identities without complex approximations.

## 2. Exactly which target orbits are periodic

The two real numbers phi^2>1 and 0<phi^-2<1 are not roots of unity.
For every integer d>=1, L^d-I is therefore invertible on im T.
On im R, L^10=I; each eigenvalue has exact order ten. Consequently

```text
L^d v=v for some d>=1  iff Tv=0;
im R=ker(L^10-I).
```

For a nonzero v in im R, an eigencomponent is nonzero, so its period
is divisible by ten and hence exactly ten. Equivalently the gcd of
q(X) and X^d-1 is one unless 10 divides d. The rank certificates for
d=1,2,5 in G5 are a finite alternative check of the proper divisors.

If Tv!=0 and L^a v=L^b v with a<b, invertibility gives
L^(b-a)v=v, a contradiction. Hence all forward target iterates are
distinct. This is a statement about the target operator, not about
whether a native checkpoint or its driving word repeats periodically.

## 3. The surviving part of the predictive carrier

In the ordered wedge basis let B be the wedge-pairing matrix and
G=Lambda^2 H. The Hodge operator is *=BG/sqrt(5), so K=BG satisfies
K^2=5I. Since C preserves the metric and orientation, A commutes with
K, and so do T and R. The exact identities

```text
tr(KR)=0; R(KL-LK)=0
```

are verified by G6. They can also be seen in an orthonormal real basis
adapted to the two C-rotation planes: T consists of the two plane areas,
which Hodge star exchanges, while R consists of the mixed-plane wedges.
The two M stretch factors are reciprocal, so L on the mixed sector
commutes with star. Each Hodge sign has dimension two in that sector.

Algebraically, K restricted to the four-dimensional im R has square 5I
and trace zero. Its eigenspaces for +/-sqrt(5) therefore each have
dimension two. Also R P_- L P_+=0, using R[K,L]=0 and commutation of
R with both projectors. For

```text
E_J=im P_+ + im(P_- L P_+)
```

it follows that R E_J=R(im P_+) and this image lies in E_J. Therefore

```text
E_J intersect im R=R(im P_+), dimension two.
```

This directly proves the intersection statement for the marked E_J.
Its already established dimension four and Lorentz signature belong
to the unchanged A1/A2 predecessor scope and are not new physical claims.
The same intersection argument applies after complexification, with
complex dimension two rather than an unnamed change of dimension.

## 4. Arbitrary finite reader configurations

Let Y be any finite nonempty set, y_n any sequence in it, and r a fixed
function, with no linearity, continuity, probabilistic or autonomous-source
assumption. Suppose r(y_n)=L^n v for every n>=0. The image r(Y) is finite.
Thus there are a<b with L^a v=L^b v. Section 2 gives Tv=0.
If v!=0 the target has exactly ten distinct values and period ten.
This is a necessary condition for a native reading, not a construction
of such a reading on actual U.

For the finite-horizon statement assume Tv!=0 and require exact agreement
for n=0,...,N. The N+1 target values are distinct by section 2. Their
reader configurations must therefore be distinct: at least N+1 are needed.

A fixed finite checkpoint set, a fixed-length window on a finite alphabet,
and any product with a fixed finite auxiliary state are finite Y. This
remains true for a history-dependent update of the auxiliary state, provided
its state set and output function are fixed. If the read instead receives
an unrestricted absolute counter, an unbounded history or another unbounded
register, the premise that Y is finite fails. The theorem does not exclude
that case, assert its sufficiency, or choose among those resources.

The sharp periodic control takes the separately declared set Y=Z/10,
y_n=n mod 10, and r(j)=L^j v for any nonzero v in im R. It attains the
ten-state periodic target. It is not a native-U or physical construction.
G7 audits one rational example. G8 audits a nonzero rational hyperbolic
example; the universal result is section 2, not a finite time sweep.

## 5. Fixed free-linear and coherent encodings

Let X be finite nonempty. There are at most |X|^|X| maps X->X, so the
set of their free pushforward matrices N_F is finite, even if the chosen
sequence F_n is nonperiodic. Fix B_src and D over R or C as in PREREG.md.
For every fixed source vector s the values D N_n B_src s form a finite
set. If the all-n intertwining identity holds, they equal L^n v_s with
v_s=D B_src s. Section 2, or the finite-image proof of section 4, yields
T v_s=0 for every s. Hence

```text
T D B_src=0; im(D B_src) subset im R.
```

Its dimension is at most four. If im(D B_src) lies in E_J (or its explicit
complexification), section 3 sharpens the upper bound to two.
No linear independence, positivity or norm-preservation assumption about
the source amplitudes is needed. Continuous coefficients in a fixed code
do not change the finiteness of the possible pushforward matrices.

Actual deterministic checkpoint evolution from a common initial counter
supplies maps F_n:X->X. It therefore meets the finite-address hypothesis.
The conclusion concerns a fixed input encoding and a fixed output chart
that purport to realize iterated L. It does not contradict a code theorem
that preserves or recovers the original source information through U:
transport of that information is not the assertion that it evolves by L.
A time-dependent read, an unbounded address carrier, a changed coupling or
arbitrary quantum channels would be a different comparison class.

## 6. Logical boundary

This closes the stated exact finite-reader route negatively for every
nonzero hyperbolic target component, and classifies the remaining target
periodic sector. It does not prove the full native architecture incapable
of a Lorentzian reading. In particular Omega includes an unbounded counter.
Nor does it infer a physical clock from an information lower bound.
No assertion about approximate simulation, noise, experimental observables,
physical dynamics, an occurrence law or any L2-L6 bridge is used or earned.
