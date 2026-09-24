# Signed axial slices and an evaluated transverse floor

**PUBLIC, NON-CANONICAL; candidate-T written derivation.**
Working item C-PHOTON-BCHI-DIRECT-BOUND-N,
[#1143](https://github.com/mathorn1973/twist-j/issues/1143).
Author: A. M. Thorn. Date: 24 September 2026. Apache-2.0.
Basis: Public Canon v91, main
`6f181bb96b9b0692c03195dbc12233b14ed2b476`, after #1156.

**P1 is still open.** Signed axial slices replace raw charged-component
area by a smaller current-dependent quantity, removing arbitrary neutral
filling exactly. Its required ensemble moment is not bounded uniformly
here. Separately, the full unchanged measure has the evaluated floor
`b >= 25*2^(-173)` in every admitted profile. The same insertion proves
`chi >= 2^(-173)`, so this particular floor cannot produce the strict
comparison `b_lower > 25 chi_upper` for any valid upper bound on chi.

The fixed measure, midpoint Fourier convention, paired-component law and
exact independent component signs are those of
[CONNECTED-CURRENT.md](CONNECTED-CURRENT.md). In particular

```
mu_L(n) = Z_L^-1 2^(-|supp n|) 1{partial n = 0 mod 5},
n_p in {-1,0,1},   j=partial n/5,   V=L^4,
lambda(t)=4 sin^2(t/2),   chi_L(t)=S_j,00(t e_1)/lambda(t),
25 chi_L(t)=S_n,01,01(t e_1)          (t nonzero modulo 2pi).
```

L is even and at least four. The original thermodynamic-first,
infrared-second joint profiles are retained. No profile existence,
Fourier limit interchange or lowest-momentum replacement is asserted.

## 1. Exact signed slice quotient

For a paired component K with reference orientation eta_K and integer
current J_K=partial eta_K/5, define cyclic slice sums, r in Z/LZ,

```
A_K(r) = sum_{x: x_1=r} eta_K(p_01(x)),
B_K(r) = sum_{x: x_1=r} J_K(e_0(x)).
```

Summing the edge-zero boundary identity over x_0,x_2,x_3 cancels all
transverse differences. Exactly

```
A_K(r)-A_K(r-1)=5 B_K(r).                              (1)
```

Thus sum B_K=0 and all A_K(r) have a common residue modulo five. They need
not be divisible by five: a winding neutral 01 plane can have a nonzero
constant slice sum. Choose any integer cyclic primitive H_K of B_K.
For example H_K(0)=0 and H_K(r)=sum_{s=1}^r B_K(s). Then
`A_K=5H_K+c_K` for an integer constant c_K. Every other integer primitive
differs by an integer constant.

For every allowed nonzero character t=2pi k/L, finite orthogonality gives

```
F_K,01(t e_1) = 5 exp(-it/2) sum_r H_K(r) exp(-itr).     (2)
```

The nonzero axial response depends only on the projected current B_K.
Adding an integer-closed two-chain changes A_K only by a constant, so it
has no effect on (2), including for winding additions. This is an
algebraic invariance of fillings; it does not assert that arbitrary
additions preserve ternary coefficients, a pairing graph or the measure.

Define the nonnegative integer

```
ell_K = min_{h in Z} sum_r |H_K(r)-h|
      = (1/5) min_{c in R} sum_r |A_K(r)-c|.             (3)
```

An integer median of H_K attains the first minimum. Its image under
`H -> 5H+c_K` is a median of A_K, proving the equality. The quantity is
independent of primitive, reference sign and cyclic origin. Equivalently,
ell_K is the least absolute integer flow on the axial cycle with divergence
B_K. It vanishes for every neutral component, and also for a charged
component whose projected B_K is zero.

Subtract the minimizing constant before taking absolute values in (2):

```
|F_K,01(t e_1)| <= 5 ell_K
               <= sum_r |A_K(r)| <= m_01(K).            (4)
```

Here m_01 counts occupied 01 faces. Therefore the exact paired covariance
formula from #1156 yields the componentwise improvement

```
chi_L(t) <= Xi_L := (1/V) E_aug sum_{K charged} ell_K^2
                  <= M_L/25.                           (5)
```

This retains every cancellation inside each transverse slice and removes
its best constant before discarding interslice cancellation. It is still
an upper bound, not a replacement for the complete signed covariance.

There is also an exact charged-edge rooted form. If N_0(K) counts the
charged orientation-zero edges of K, translation invariance gives, for a
fixed orientation-zero edge e,

```
Xi_L = E_aug[1_{e charged} ell_{K(e)}^2/N_0(K(e))].      (6)
```

Each K contributes N_0(K) identical terms in the spatial sum. Components
with N_0=0 have ell=0 and are omitted. This avoids assigning long neutral
area to the charged root. No evaluated uniform upper bound on Xi_L is
obtained. An arbitrary extended current can still have large ell, and
many currents can lie in one paired component. Existing elementary-block
probabilities do not control this complete expectation.

For clarity, Parseval supplies only the frequency average

```
(1/L) sum_{k=1}^{L-1}|sum_r H_K(r) exp(-2pi i k r/L)|^2
    = sum_r |H_K(r)-mean(H_K)|^2.                        (7)
```

A square-slice sum cannot replace ell_K^2 in (5) with a universal constant:
many equally signed pulses can add coherently at low frequency. A theorem
controlling that coherence in the actual ensemble would still be needed.

## 2. The aligned neutral connector for every D>=3

Use the published cubical boundary convention and four-cup defect

```
U(x)=-c_012(x)+c_012(x-e_2)-c_013(x)+c_013(x-e_3),
a(x)=partial U(x)-5p_01(x),    partial a(x)=-5 partial p_01(x).
```

Put b=(D+1)e_1, L=2D+4 and

```
T_D=sum_{k=1}^D c_012(k e_1),
n_D=a(0)+a(b)-partial T_D.                              (8)
```

The end caps of partial T_D are p_02(e_1)-p_02(b). Their coefficients
in the two defects are respectively +1 and -1, so subtraction cancels
both. The remaining tube has four lateral faces per unit length: two
01 faces at x_2=0,1 and two 12 faces at x_0=0,1. They are disjoint from
the remaining defect faces and join them along the removed cap edges.
Each removed cap touched one charged edge; the replacement lateral face
keeps that degree equal to five. All other occupied edges have degree two.
D>=3 separates the defects and L=2D+4 prevents additional identifications.

Consequently, for all D, not just the audited instances,

```
|supp n_D|=4D+40,   m_01=2D+10,
j_D=-partial p_01(0)-partial p_01(b),
degree-five edges=8,   degree-two edges=8D+60.
```

The coefficients are ternary. The two currents are disjoint elementary
loops with the same orientation. All neutral matchings are unique and
the signed face graph is connected; the displayed n_D proves consistency.
The support therefore has exactly two signings, n_D and -n_D.

At each axial slice k the two tube 01 coefficients cancel. Each defect
has five 01 faces summing to -5 at its own axial coordinate. Hence

```
A_D(r)=-5 delta_{r,0}-5 delta_{r,D+1},
F_D,01(t e_1)=-5 exp(-it/2)[1+exp(-it(D+1))],
ell_D=2,   |F_D,01|^2/25=2+2cos(t(D+1)) <= 4.            (9)
```

The median of A_D is zero because L>=10. The old component ceiling
`(2D+10)^2/25` grows quadratically; the signed ceiling is four for all D.
For the allowed `t=4pi/(2D+4)`, (9) gives
`|F_D,01|=10 cos(pi/(D+2))`, tending to ten. This is an algebraic statement
about a sequence of supports, not a substitution for the original limit
order. Before its probability weight, one such component contributes at
most 4/V to chi_L. The support's exact probability is
`2^(-(4D+39))/Z_L`. Its nondecaying form factor neither contradicts decay
in the full measure nor provides a uniform susceptibility lower bound.

## 3. A full-measure empty-set estimate

For any finite set B of faces, let Z_emptyB be the original surface sum
with n=0 on B. The positive primal character expansion is

```
Z_L = E_{A in Z5^E} product_p Q((dA)_p),
Q(theta)=1+cos(theta),
Z_emptyB = E_{A in Z5^E} product_{p not in B} Q((dA)_p).
```

The same edge variables and all modulo-five constraints remain after
deleting those factors. Since 0<=Q<=2 and the other factors are
nonnegative, pointwise comparison proves

```
P_mu(n|_B=0)=Z_emptyB/Z_L >= 2^(-|B|).                  (10)
```

This is an unconditional full-measure statement. It asserts no bound
under arbitrary prescribed exterior face values or nonzero currents.

## 4. Isolated insertion and an evaluated b floor

Let S be the 21-face support of a(0), or its coordinate rotation to a
central 02 plaquette. Its central four edges have degree five and its
32 other edges have degree two. The central face and the four five-face
cups give 21 faces and `4*5+32*2=4*21` incidences. These incidences remain
distinct on every even L>=4.

Let B contain S and every face sharing an edge with S. Each edge meets
six lattice faces. Counting missing incidences, allowing overcount,

```
|B outside S| <= 4(6-5)+32(6-2)=132,
|B|<=153.                                               (11)
```

Starting with n|_B=0, insert either sign of the defect into S. Its boundary
is divisible by five, so this preserves every constraint and changes
exactly 21 zero faces to occupied faces. It is a bijection for each sign
onto the event E_sign specifying that pattern on S and zero on B outside
S. Thus, for their disjoint union E,

```
P(E)=2^-20 P(n|_B=0) >= rho,    rho=2^-173.               (12)
```

All exterior components are summed. On E, S is an entire isolated
occupied-face component and also a single paired component with unique
neutral matchings. There is no omitted pairing factorial.

Component sign reversal in the original surface law eliminates every
cross term between distinct occupied-face components gamma:

```
E_mu |F_I(n;t)|^2 = E_mu sum_gamma |F_I(n^gamma;t)|^2.   (13)
```

All summands are nonnegative. Retain the isolated insertions at all V
translations. No component is counted twice: its unique nonzero elementary
current loop determines the central plaquette, and hence the translation,
for L>=4. Translation invariance and division by V then give

```
S_n,II(t e_1) >= P(E_0) |F_I(a_I(0);t)|^2.              (14)
```

For central orientation 02 the five caps have axial coordinates -1,0,1,
with multiplicities 1,3,1. Their common sign is irrelevant after squaring.
For central 01 all five caps have midpoint coordinate 1/2. Therefore,
uniformly at every allowed finite-volume frequency,

```
S_n,02,02(t e_1) >= rho (3+2cos t)^2,
S_n,01,01(t e_1) >= 25 rho,
chi_L(t) >= rho                    (t nonzero).         (15)
```

These are Fourier covariance bounds in the full measure, not a local
variance substituted for an infrared response. They pass directly to
every already-admitted joint profile, or corresponding lower limits.
Taking t to zero only after the prescribed thermodynamic limit yields

```
b^omega >= 25 rho,    chi^omega >= rho,
b_lower=25*2^-173 > 0.                                 (16)
```

The finite-volume transverse error is explicit: since
`25-(3+2cos t)^2=4(1-cos t)(4+cos t)`, it is at most `10 t^2`.
Thus (15) also gives `S_n,02,02 >= 25 rho - 10 rho t^2`.

## 5. Exact disposition of the numerical comparison

For any valid uniform chi_upper on a nonempty admitted profile family,
(16) forces chi_upper>=rho. Consequently
the particular lower bound just proved obeys

```
b_lower - 25 chi_upper <= 25 rho - 25 rho = 0.           (17)
```

This floor cannot close P1, even with a perfectly sharp upper estimate.
The two insertion families are coordinate rotations of the same bounded
components, with equal infrared contributions to b and 25 chi. This
agrees with the earlier [bounded-component subtraction](README.md).
It does not assert that the true difference is nonpositive.

A finitely supported integer-closed neutral two-chain on Z^4, or one
with a finite incidence-preserving lift from the torus, has zero total
coefficient in each orientation: pair its boundary with a linear
coordinate one-cochain whose coboundary is that constant two-form. Its
fixed-orientation form factor therefore vanishes at zero. An isolated
neutral cube supplies only a lower bound proportional to lambda(t),
which vanishes in the infrared. Neutral components can contribute
positively to b at nonzero t, but finite neutral insertions do not give
the missing surviving margin. This argument does not apply to winding
neutral planes, which have no such finite lift.

The remaining task is an evaluated signed charged-covariance bound and
a stronger transverse contribution, compatible across all admitted
profiles. The slice quotient removes a demonstrated source of excessive
counting; it does not pay the ensemble sum over extended charged currents.
Neither the existing local source constants nor the new insertion floor
supplies the positive contribution from unbounded scales needed after
the common bounded part is subtracted. No uniform upper constant for
Xi_L, signed covariance decay or positive P1 gap is claimed.

## 6. Audit and review boundary

[SIGNED-PREREG-20260924.md](SIGNED-PREREG-20260924.md) freezes the finite
geometry and rational checks in [verify_signed_slices.py](verify_signed_slices.py)
before execution. They audit the proof's finite inputs, not a full-measure
partition sum or an infinite-volume inequality by enumeration. The all-D
construction and bounds above have written analytical proofs.

Separate agents independently derived the slice quotient and reviewed the
insertion argument using shared sources. This is not blind external review
or formal theorem acceptance. The finite audit remains candidate-C; ordinary
two-architecture repository CI is not its scientific gate. The inherited
pairing law, Ward identity and bounded-component cancellation keep their
existing status and are not claimed anew. P1, P2, spectral S7 and the
canonical phase obligation remain open.
