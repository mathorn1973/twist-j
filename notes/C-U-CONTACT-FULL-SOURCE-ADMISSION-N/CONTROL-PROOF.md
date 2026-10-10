# Conditional exact control circuit and its clean-energy boundary

**PUBLIC / NON-CANONICAL / conditional L1 proof / analytical result exposed.**
Author: A. M. Thorn. Original text: Apache-2.0.
Incubation reservation: [issue #1442][claim].
Public source base: `a18e65d3e43acc6cb1896296b8bd0fdecdad35a7`, Canon v101.
No scientific program was run or imported for this proof.

## 1. What is assumed and what is proved

The earlier [QDD-AFFINE-CONTROL-REALIZATION][control] supplies a conditional
control model on six distinguishable five-level systems. Local Fourier
transforms and the pair Hamiltonian `-hbar*g*N_i*N_j` implement exact
fixed-coefficient field additions; a connected local transition graph with
both displayed X- and Y-type Hamiltonians supplies local SU(5) controls.
These are previously specified mathematical control resources, not native
physical availability. Here their availability is explicitly extended to
**seven** five-level systems, including the added source, with the required
pair access. This extension is an additional carrier/control premise.

Let the complete modeled Hilbert space be `(C^5)^tensor7`, with basis labels
`(p1,p4,p1p,p4p,q,r,s)` in F5. All labels, including q,r, are arbitrary.
Center the first four labels by the fixed local shift permutation K:

```text
x=p1-1, u=p4-3, y=p1p-4, w=p4p-2, h=y-x.
```

We prove an exact circuit for the basis permutation

```text
C|x,u,y,w,q,r,s> = |x,u-2hs,y,w+2hs,q,r,s>.             (1)
```

It acts on all amplitudes, with no input-dependent phase. The raw-coordinate
unitary is `K^-1 C K`. Its source basis label is fixed; this does not assert
preservation of every source density operator or of its entire observable
algebra. The separate source-retention proof addresses that question.

The controls, time schedule, compensation of drift and physical carrier
remain premises. Compiling (1) from a previously specified broad control
family does not independently select its coefficient 2, its dependence on
h, or its availability as a native contact. No SUM normalization is used in
the circuit identity or in the energy lemma below.

## 2. Fourier reduction of the complete contact

All field arithmetic below is modulo five. Put `omega=exp(2*pi*i/5)` and
use the earlier Fourier convention

```text
F|z> = 5^(-1/2) sum_m omega^(mz)|m>.
F_uw = F_u tensor F_w, with identities on other registers.
```

After F_uw, call the two Fourier basis labels m_u,m_w. Define the diagonal
unitary D on the same seven registers by

```text
D|x,m_u,y,m_w,q,r,s>
  = omega^[2*s*(y-x)*(m_w-m_u)] |x,m_u,y,m_w,q,r,s>.
```

Then, with the rightmost operator acting first,

```text
C = F_uw^dagger D F_uw.                                (2)
```

Indeed the coefficient of an output (u',w') is the product of the two
normalized character sums with exponents
`m_u*(u-u'-2hs)` and `m_w*(w-w'+2hs)`. Each sum is one precisely when
its coefficient vanishes and otherwise zero. The unique output is (1),
with coefficient one. This proves the all-space identity, not merely a
statement about a set of preparations or basis populations.

## 3. Seven cubic phase gadgets, with occupied data restored

Perform the invertible linear change L on the Fourier-side data:

```text
y <- y-x,       m_w <- m_w-m_u.
a=s,            b=y after L,          c=m_w after L.
```

The original x and m_u are retained. The two overwritten coordinates are
data, not blank work registers. Undoing these additions restores them.
It is enough to implement the diagonal phase `omega^(2abc)`, since

```text
D = L^-1 D_abc L,       D_abc|a,b,c,...> = omega^(2abc)|a,b,c,...>.
```

The following polynomial identity holds in every commutative ring:

```text
(a+b+c)^3-(a+b)^3-(a+c)^3-(b+c)^3+a^3+b^3+c^3 = 6abc.
```

In characteristic five, 6=1. Thus twice the left side is 2abc.
For a coordinate z define the local phase

```text
Q_z(k)|z> = omega^(k*z^3)|z>.
```

For each nonempty subset T of {a,b,c}, choose a fixed pivot in T and let
B_T add every other coordinate in T into that pivot. This is an invertible
sequence of the existing fixed-gain additions. Define

```text
P_T(k) = B_T^-1 Q_pivot(k) B_T.
```

On every input this leaves all labels unchanged and multiplies by
`omega^[k*(sum_(z in T) z)^3]`. The pivot need not be initialized: it is an
arbitrary occupied input coordinate, and B_T^-1 restores its original
value. The other coordinates are retained throughout this gadget.

Use precisely these seven gadgets:

| T | k in F5 |
|---|---:|
| {a,b,c} | 2 |
| {a,b} | -2 = 3 |
| {a,c} | -2 = 3 |
| {b,c} | -2 = 3 |
| {a} | 2 |
| {b} | 2 |
| {c} | 2 |

Their completed operators are diagonal and commute. Their product is
D_abc by the polynomial identity. Each compute/phase/uncompute sequence
must be completed before the next begins; one must not reuse an unrestored
pivot. Combining the seven gadgets with L, F_uw and their inverses proves
(1) on the full seven-register space. No work ancilla or ready subspace is
used. The original q,r are spectators even when occupied. Source labels
and other data may be changed temporarily by compute steps, but every
completed gadget restores its input labels.

## 4. Local phase availability and the global-phase account

The full connected-graph SU(5) option of the earlier model is required
here. Merely listing its affine additions, Fourier transforms, shifts and
field scalings does not by itself supply the cubic phase resource.

There is no determinant obstruction to implementing Q_z(k) exactly:

```text
det Q(k) = omega^[k*(0^3+1^3+2^3+3^3+4^3)]
         = omega^(100k) = 1.
```

For an explicit diagonal decomposition, put `t_j=2*pi*k*j^3/5` for j=1..4.
On levels 0,j apply the determinant-one relative phase with entries
`exp(-i*t_j), exp(i*t_j)` and identity on other levels. Their product
has the required entry on each j and entry `exp(-i*sum_j t_j)=1` on zero.
The previously admitted local SU(5) controls supply these relative phases.
No source-dependent choice of a pulse is made in this argument.

The pair-addition identity [already proved in the Canon][control] is
phase exact when the actual implemented Fourier transform is paired with
its actual inverse. Replacing F by `exp(i*alpha)F` in such a sandwich
cancels alpha. The same pairing is required for the outer F_uw and its
inverse and for every compute/uncompute block. Negative field coefficients
are residues such as 4 or 3, not a claim of negative physical duration.
The centering shifts can also be chosen exactly in SU(5).

With exact SU(5) phases and actual inverse sandwiches, the circuit equals
(1) literally. If an implementation instead supplies local gates only up
to fixed scalar phases, their residual product must be recorded. A common
input-independent phase does not alter this isolated channel. It becomes
a relative phase if the whole circuit is coherently controlled against a
different branch; that use requires exact correction or explicit retention
of the phase. It must not be called harmless in the controlled setting.

## 5. Necessary clean additive-energy condition

This is a specialization of [QDD-CLEAN-ENERGY-OBSTRUCTION][energy], not a
new general conservation theorem or an energy assignment to F5 labels.
Choose real additive diagonal energies on the seven modeled registers:

```text
E(x,u,y,w,q,r,s) = E_x(x)+E_u(u)+E_y(y)+E_w(w)+E_q(q)+E_r(r)+E_s(s).
```

Include all other participating controls and work stores in an environment
with Hamiltonian H_E and a fixed independent normal initial state. Assume a
complete unitary strongly conserves `H_0=H_S tensor I+I tensor H_E` and
implements the exact coherent C on the whole system space with one common
final environment independent of the system input. The existing gap lemma
then forces the same energy change Delta for every input basis state.
Summing over the finite basis permutation C gives Delta=0.

Only u,w change in (1), so necessarily, for all admitted labels,

```text
E_u(u-delta)+E_w(w+delta)=E_u(u)+E_w(w),    delta=2hs.    (3)
```

Every delta in F5 is attained. In particular h=1,s=3 gives delta=1.
Equation (3) says `E_u(u-1)-E_u(u)` equals the negative of
`E_w(w+1)-E_w(w)` for independent u,w. Both sides are therefore one
constant. Summing over the five u values makes that constant zero.
The cyclic unit shift then forces both E_u and E_w to be flat. The other
five local profiles are not constrained by this argument, since C fixes
their labels. Flat receiver profiles are necessary, not a realization.

The conclusion uses global all-state exactness, clean independent
environment, strong conservation and the specified additive cut energy.
Nonadditive interaction energies, input-dependent residual controls/work
stores, externally driven unaccounted fields, approximate gates or a
restricted input code change those premises. Neither their impossibility
nor a realization in those classes follows here. Physical pulse durations,
native tick compatibility and preparation/reset costs remain unspecified.

## 6. Calibration outside the SUM orbit and disposition

At a fixed receiver basis input with h=1 and source basis label s=1, the
predicted output is exactly `u'=u-2, w'=w+2`, with all other labels fixed.
At h=0 the receiver contact is the identity. These are full-state controls
outside the occupied SUM orbit h=+/-2, independent of its unit-gain readout.

For the declared equal source superposition `|+>=5^(-1/2)sum_s |s>` and a
fixed receiver basis state with h=1, the five receiver outputs C_s(v) are
distinct and orthogonal. Tracing the receiver gives source state `I_5/5`,
whereas the input source state was `|+><+|`. The companion source-retention
proof establishes this channel statement and its wider implementation
scope. The unchanged basis label s is not unchanged source coherence.
These are conditional predictions, not observations or a Born derivation.

The result is one concrete conditional circuit and its necessary clean
energy boundary. It supplies no native carrier, physical commandability,
spatial coupling, complete controller, source preparation, acquisition of
the native counter, event law or independent selection of the contact.
The existing physical apparatus owners and gates remain open.

[claim]: https://github.com/mathorn1973/twist-j/issues/1442
[control]: https://github.com/mathorn1973/twist-j/blob/a18e65d3e43acc6cb1896296b8bd0fdecdad35a7/canon/CANON.md#L6943
[energy]: https://github.com/mathorn1973/twist-j/blob/a18e65d3e43acc6cb1896296b8bd0fdecdad35a7/canon/CANON.md#L6976
