# A finite original-occupation Hamiltonian on the unchanged source pair

**NON-CANONICAL. L1. Conditional analytical candidate-T.**
Author: A. M. Thorn. Date: 2026-10-26. Apache-2.0.
Reservation: [#1780](https://github.com/mathorn1973/twist-j/issues/1780).
The prospective [CONTRACT.md](CONTRACT.md) is frozen at
`9f7b175341e5267113dfbe42f96db47299e27f52`.
Independent scientific acceptance is not asserted.

This construction gives an actual finite physical support for a positive
approximation to the original energy on the declared prepared source
family. It preserves the original occupation encoding, the source
vectors, the occupied receiver and arbitrary passive references. The two
settings have exactly the same complete energy law for the new generator.

The admitted physical term may act jointly on every site in its finite
region. Its size grows with the polynomial degree and required time
accuracy. This is not a few-body, bounded-range scalable implementation,
or a realization of the twelve-register apparatus in PR1779. Source
readiness and final interrogation remain supplied.

## 1. Frozen source and the finite coordinate unitary

Use the U, Q=E0 f(U), source pair and memory convention in
[CONTRACT.md](CONTRACT.md). Write the source without a passive reference
first; every operator below is tensored with its identity. The original
memory has all 26 labels. Its restriction to span(d1,...,d25) is needed
only for the inherited fresh-write contrast.

For an integer L>=7 put d=2L+1 and use the finite coordinate space

    C_L = C^d_R tensor C^d_r tensor C^d_c tensor C^4_o
          tensor C^3_a tensor C^26_l tensor C^26_m,
    dim C_L = 8112 d^3.                              (B1)

R and c represent 97-L,...,97+L; r represents -L,...,L. The three values
of a are token, pulse bank 1 and pulse bank 2. Define U_L by the eight
factors of
[PR1779 COMPACT_MODEL, section 2](https://github.com/mathorn1973/twist-j/blob/c2b06d3ee52778f804da1f84ba9f963bae1ad46e/notes/C-COMPACT-ENERGY-RECORD-N/COMPACT_MODEL.md),
with period 15 replaced by d:

    U_L = P_beta Gamma S_R S_r E_rec,L Q_p M2 C.      (B2)

All matrix entries, signs, phases and factor order are unchanged. The
coordinate shifts and pulse edges are cyclic at the endpoints of their
specified representative intervals. C rotates the contact pair exactly
when r=0 and R=c. Gamma acts at r=0. If E_L is the cyclic pulse edge,
T_L swaps the full carrier and memory labels when the represented c>=100,
and E_rec,L=T_L E_L T_L. This includes both physical cut edges and the
wrap edge; no boundary-input action is omitted.

Each factor is unitary on all of C_L. T_L commutes with the other seven
factors: they either leave c and labels unchanged or preserve c and treat
all labels identically. Thus

    U_L=T_L (U_src,L tensor I_m) T_L.                 (B3)

Let A_L:C_L -> H_rec be the coordinate-basis inclusion into the original
infinite space, retaining all internal and memory labels. This is not a
periodic identification of distinct original physical sites: each finite
basis ket is mapped to its specified representative integer coordinates.
Only the new finite dynamics wraps at the region boundary.

The seed chi_L is the same alpha_(97,0) and arbitrary old-memory input as
in the contract. Each original forward or inverse step moves each of
R,r,c by at most one. All intermediate factors satisfy the same bound
relative to their complete-step prefix. Consequently, for every integer k
with |k|<L,

    A_L U_L^k chi_L = U^k chi.                       (B4)

To prove (B4), follow the finite ordered factors from the seed. Every
visited coordinate is at distance at most |k| from its seed value, so no
cyclic crossing is reached. The inverse uses the reversed adjoint factor
order and has the same property. All contact and receiver predicates then
agree with their original integer predicates. This argument retains the
unknown memory and any reference throughout.

In particular the normalized finite sources

    psi_L,+/- = [I +/- (U_L^2-U_L^-2)] chi_L/sqrt(Z),
    Z=(39521+154 sqrt(5))/15625                       (B5)

obey A_L psi_L,+/-=psi_+/-. Their norm is the original norm. Nothing in
(B5) changes the source after inspection of a result. The predecessor's
complete preparation uses prefixes at coordinate distance at most six;
L>=7 also preserves that preparation on its admitted ready inputs. This
is a source-preparation identity, not a proof that its controller conserves
the new energy introduced below.

## 2. Positive finite energy and exact equality of the setting laws

Let q be any real-valued Laurent polynomial on the unit circle, of degree
D>=1, such that

    0 <= q(z) <= b <= 2pi,       |z|=1.              (B6)

Define the one fixed finite generator

    h_L=E0 q(U_L).                                  (B7)

Functional calculus gives 0<=h_L<=E0 b I. This same generator acts on
both source settings; the setting register, if retained, is passive.

For every bounded Borel function F on the real line, the two sources
satisfy

    <psi_L,+, F(h_L) psi_L,+>
       = <psi_L,-, F(h_L) psi_L,->.                  (B8)

Indeed D_L=U_L^2-U_L^-2 is skew-adjoint and commutes with F(h_L). Both
(I+D_L)^*(I+D_L) and (I-D_L)^*(I-D_L) equal
3I-U_L^4-U_L^-4. Inserting (B5) gives (B8). Taking F to be any spectral
indicator proves equality of the entire h_L spectral measures, not just
their expectations or finitely many moments.

Equation (B3), with T_L chi_L=chi_L, makes this common energy law
independent of the old-memory/reference input. The comparison includes
mixed memory states by purification. For retained orthogonal settings,
coherent setting-memory-reference inputs also have this same energy law:
h_L acts identically on the setting blocks, whose spectral probabilities
add. No claim is made for an unmarked arbitrary superposition of the two
source vectors.

The common h_L law need not equal the entire original-Q law. Exact
setting equality and approximation to the original energy are different
statements; the latter has the quantitative scope below.

## 3. Original energy action and complete finite-time error

Assume the polynomial has the source action bound

    ||[q(U)-f(U)] psi|| <= delta                     (B9)

uniformly on the admitted marked source, memory and reference family.
The notch sequence in [CUT_APPROXIMATION.md](CUT_APPROXIMATION.md) supplies
delta tending to zero;
it does not supply a computed stopping index. The separate
[SPECTRAL_CERTIFICATE.md](SPECTRAL_CERTIFICATE.md) proves delta<1/1200 for
one fixed normalized Abel polynomial of degree 1024*10^25. Both routes
use the same realization theorem below.

Choose any integer m>=1 and

    L=max(7,mD+3).                                  (B10)

For 0<=j<=m, q(U_L)^j times either source in (B5) is a linear combination
of U_L^k chi_L with |k|<=jD+2<L. Equation (B4) therefore proves the
complete vector identity

    A_L q(U_L)^j psi_L = q(U)^j psi.                 (B11)

It holds on the entire marked source/reference family. In particular,
the original energy-action error is

    ||A_L h_L psi_L - Q psi|| <= E0 delta.           (B12)

The source is unchanged in (B12). It has not been replaced by a spectral
bin, an adjusted finite-generator source or a projection of an infinite
spectral vector.

More generally, for 1<=k<=m, (B11) and
|x^k-y^k|<=k(2pi)^(k-1)|x-y| on [0,2pi] give

    ||A_L h_L^k psi_L-Q^k psi||
        <= E0^k k(2pi)^(k-1) delta.                 (B12a)

The same bound applies to the difference of the kth energy moments.
This is a finite-moment comparison with the original energy, in addition
to the exact setting-to-setting equality of all spectral events in (B8).

For dimensionless time s=E0 t/hbar, compare the exponential series using
(B11) through degree m. Each remaining difference has norm at most
2 b^j. Hence

    ||A_L exp(-is q(U_L)) psi_L - exp(-is q(U)) psi||
       <= eta_m(|s|b),
    eta_m(x)=2 sum_(j=m+1)^infinity x^j/j!.          (B13)

The commuting functional calculus inequality
|exp(-isx)-exp(-isy)|<=|s| |x-y| and (B9) give

    ||A_L exp(-it h_L/hbar) psi_L
           - exp(-itQ/hbar) psi||
       <= |s| delta + eta_m(|s|b).                  (B14)

This compares the complete state, including occupied memory and passive
references, before any conditioning or branch selection. It bounds the
trace distance of the corresponding density operators and remains valid
after a common complete output instrument. It does not give a normalized
conditional-state bound after an arbitrarily rare outcome.

Here is an entirely analytical uniform boundary budget for |s|<=3.
Take m=127. By b<=2pi<8<9, x=|s|b<27. For j>=128, the ratio of successive
exponential-series terms is at most 27/129<1/4, so

    eta_127(x) < 4 * 27^128/128! < 2^-62.            (B15)

For the second inequality, integrating log x gives n!>=(n/e)^n, and
e<3 gives 27^128/128!<(81/128)^128. Since 81/128<2/3 and
(2/3)^2<1/2, this is less than 2^-64. No numerical tail calculation is
used in (B15).

At s=3, each of the two original receiver probabilities changes by at
most 3delta+eta_127(3b). The inherited original contrast is >1/50, so

    Delta_L > 1/50 - 6delta - 2eta_127(3b).
    delta<=1/1200  =>  Delta_L>3/200-2^-61>1/100.     (B16)

The same receiver effect at physical site 100 is used in both laws.
All outcomes are retained. This is a sufficient quantitative implication;
the particular degree certified in SPECTRAL_CERTIFICATE.md satisfies its
hypotheses without a numerical moment execution.
Preparation errors, generator calibration errors and imperfect final
effects consume additional error; none is included for free in (B16).

For example, let the complete ready-input trace-distance error be
zeta<=1/8000 and let a self-adjoint actual generator obey
||H_actual-H_phys,L||<=E0/24000. Duhamel's bound adds at most
zeta+3/24000<=1/4000 to the state error for |s|<=3. If the final receiver
effect also differs by operator norm at most 1/4000, the two-setting
contrast loses at most 4/4000=1/1000 in total. Thus the actual
contrast still exceeds 3/200-2^-61-1/1000>1/100. These are sufficient
tolerance requirements, not achieved tolerances. Generic perturbations
need not preserve the exact equal-energy-law identity (B8), which remains
a statement about the declared ideal generator.

## 4. A literal finite physical support in the original occupation code

The original object positions are x_A=R+r and x_B=R-r. Thus all object,
token, pulse and receiver occupations in C_L fit in the physical interval

    Lambda_L={97-2L,...,97+2L},
    |Lambda_L|=4L+1,       diam Lambda_L=4L.         (B17)

Use the exact original phase-zero occupation isometry

    I=Emb Gamma^(-1) D_2^*,
    D_2=diag(1,i,i,-1),                              (B18)

with the receiver at 100, as in
[the pinned original-port realization](https://github.com/mathorn1973/twist-j/blob/191ab035be823bd9d6fdc9effba81528fa026e49/notes/C-ORIGINAL-PORT-SOURCE-PREPARATION-N/LOCAL_REALIZATION.md).
The object, carrier and receiver use their distinct prescribed subbanks
among the 29 active coordinates h1,...,h16,h25,...,h37 at each site.
The remaining nine coordinates h17,...,h24,h38 are identity spectators.
The phase gauge in (B18) is retained exactly. It is diagonal on the fixed
code, changes neither
positions nor charges, and gives a phase on each of the finite basis
vectors; it is not omitted or interpreted as an additional free dynamics.

Let J_L:C_L -> D_Lambda,active be the resulting finite-region active-code
isometry. Then, for the zero-spectator representative and with v_out the
zero-occupation vector outside the region,

    I A_L phi = (J_L phi) tensor v_spec tensor v_out. (B19)

The actual physical Hamiltonian is the single interaction

    H_Lambda = J_L h_L J_L^*,
    H_phys,L = H_Lambda tensor I_spec tensor I_out.  (B20)

This is a matrix specification on the original occupation factors.
For example its entries are the finite matrix q(U_L), conjugated by the
exact phase-weighted occupation basis map; they are not prescribed only
on successful source branches. The complete local active complement of
Ran J_L has zero Hamiltonian. Therefore

    0<=H_Lambda<=2pi E0 I,
    H_Lambda J_L=J_L h_L,                            (B21)

and the local active vacuum has zero energy. Arbitrary non-code active
occupations inside the region are in that zero complement. On onsite
spectators and outside the region there are identity factors in (B20),
not projectors onto vacuum:
there is no unsupported claim that every global state with an occupied
outside site is annihilated.

Every valid finite active code ket has original occupation charge
H_N,active=2 sum_active h_alpha^2 equal to 10. Thus (B20) commutes with the
complete occupation charge, including all spectator and outside charges,
on the natural raw occupation space. More precisely its active code block
lies within the active charge-10 eigenspace, it is zero on the local
active orthogonal complement, and hence it commutes with all active
charge spectral projections. The other factors are identity. This gives
strong commutation even when the complete raw charge is unbounded.

Combining (B19)-(B21) transfers (B12)-(B16) without extra error to the
original physical occupation space. No coordinate-register decoder is
inserted at the output. The receiver remains the original occupation
memory at site 100 with its full unknown input state and reference
correlations. Because (B20) acts as identity on onsite spectators, the
same estimates also allow arbitrary spectator states correlated with the
admitted input and included in its passive reference. No occupied
spectator is projected onto vacuum.

The count (B17) is an actual support count. Each site has 38 occupation
coordinates. On the existing four-level representation
0,+1,-1,2 of each coordinate, the term acts on

    38(4L+1) four-level occupation factors,
    equivalently 76(4L+1) occupation qubits.         (B22)

Only 29 coordinates per site participate in its active operator;
the other nine carry identity. Thus the active count is
29(4L+1) four-level factors, or 58(4L+1) qubits, within the full inventory
(B22). Its action is zero on every local unused or invalid active code
state, including active h=2 states. No synthesis workspace, extra clock or
hidden coordinate register is included in (B22). On the full integer
occupation Hilbert space the same bounded code block is extended by zero
on the remaining local active occupations. The finite representation is enough
to specify this operator, but is not a gate synthesis or hardware
fabrication claim.

There is one term, of norm at most 2pi E0, supported on all of Lambda_L.
It can be a high-order many-body interaction involving that entire
region, including its wrap coupling. Its diameter and number of physical
factors diverge when L grows. No fixed microscopic interaction diameter,
two-body decomposition, translation-invariant bulk law or economical
implementation follows from (B20).

## 5. Existence sequence and its effective-size boundary

For the positive normalized notch polynomials q_j of
[CUT_APPROXIMATION.md](CUT_APPROXIMATION.md),
j>=2, use their exact degree bound D_j=j^2+j and 0<=q_j<=2pi. They
converge pointwise to the fixed f including f(1)=0, so their source action
errors delta_j tend to zero, uniformly on the declared memory/reference
family.

For the particular >1/100 contrast target, m=127 and
L_j=127(j^2+j)+3 suffice for every j whose delta_j<=1/1200. Such an index
exists, but this construction does not provide an effective upper bound
for it or a computed successful choice.

The constant upper bound in (B15) is not an actual convergence floor.
The fixed choice L_j=127D_j+3 already has a strong limit on the whole
original active sector. Define there the dimensionless operators

    K_j=A_(L_j) q_j(U_(L_j)) A_(L_j)^*,
    0<=K_j<=2pi I.                                  (B23)

For any finitely supported coordinate vector v, let R_v bound the
distances of its support from (97,0,97). Since D_j grows and
L_j=127D_j+3, eventually R_v+D_j<L_j. Every power in the Laurent
polynomial then avoids the periodic boundary and

    K_j v=q_j(U)v.                                  (B24)

The pointwise bounded convergence in the companion note gives
q_j(U)v->f(U)v. Density of finite coordinate support and the common
2pi operator bound extend this conclusion to every vector:

    K_j -> f(U) strongly.                           (B25)

It also follows that exp(-isK_j)->exp(-is f(U)) strongly, uniformly on
every compact s interval. One elementary proof first obtains strong
convergence of every fixed power by induction and the uniform operator
bound, then truncates both exponential series with a common uniform
tail bound. Continuous energy test functions converge by the same
polynomial approximation argument. This is weak convergence of the
energy measures on each fixed input, not total-variation convergence or
uniform convergence for arbitrary sharp spectral events.

The restriction of H_phys,L_j to the complete original active code is
exactly E0 K_j in its original occupation embedding. To check the zero
part in (B23), an original basis vector outside the finite coordinate
box either has an active occupation outside Lambda_L, leaving active
local charge below 10, or has all its active occupations inside but is
not a code ket of J_L. In both cases the local active code block in
(B20) annihilates it. Injectivity of the original occupation code and
the retained diagonal gauge then establish the stated restriction.

For a bound that itself tends to zero directly in (B14), one may instead
choose m_j=j+127 and L_j=max(7,m_jD_j+3). Then both delta_j and
eta_(m_j)(6pi) tend to zero. Either construction preserves the exact
source vectors and equal setting energy laws at every finite stage.
Neither supplies an effective degree at a requested tolerance.

For the separate normalized Abel polynomial certified in
SPECTRAL_CERTIFICATE.md, a fixed choice is already available:

    N=1024*10^25,       L=127N+3,
    |Lambda_L|=4L+1=520192*10^25+13.                 (B26)

That is approximately 5.2*10^30 lattice sites in the declared physical
support, coupled by one term. Equations (B12), (B14) and (B16) then hold
with delta<1/1200, including the stated additional perturbation budget.
No search or expansion of that enormous matrix was performed. The fixed
bound is an analytical existence certificate and is not a practical
apparatus size or a claimed lower bound on what is necessary.

This does not contradict the sharp global norm obstruction in PR1779.
That result compares in operator norm on the complete infinite sector
with one fixed finite physical diameter. Each (B23) still obeys
||K_j-f(U)||>=pi by that obstruction. Strong convergence (B25) instead
fixes an input vector first, while the permitted diameter grows with j;
the quantitative contrast comparison uses the declared located source
family and finite time interval. No global uniform approximation is
claimed.

The earlier PR1774 construction used energy-bin orbit spaces whose
vectors can have infinite physical support and an exact integer-prefix
interpolation. This construction keeps the original finite-support
source and original occupation sites; its continuous-time approximation
is proved through polynomial propagation and a counted finite physical
block. It does not claim PR1774's exact integer-prefix equality for the
new Hamiltonian, or replace its separate archive construction.

## 6. Remaining physical premises and review obligations

The declared generator is time independent and its own total energy is
conserved. It approximates the nominated original Q on the stated
prepared family. It does not establish preparation of that family from
equilibrium, an energy-conserving integration with the predecessor's
preparation controller, a funded final detector, a permanent record,
renewal, or a native six-pentit derivation. The original source law and
contrast remain inherited conditional premises.

Independent review should check separately:

1. The complete finite U_L, its calibrated wrap edge, scalar phases and
   source factor order, including every boundary-input complement.
2. The forward and inverse propagation proof of (B4), all polynomial
   powers in (B11), and the strict margin in (B10).
3. Exact identity of the old and new prepared source vectors and their
   normalization, with the full 26-state memory and passive references.
4. Equality of complete setting energy laws in (B8), and its distinction
   from equality with the original-Q spectral measure.
5. Positivity, norm, source action and full finite-time estimates
   (B6)-(B16), including the factorial proof and the two-setting factor.
6. The actual physical positions, injective original occupation code,
   retained diagonal gauge and support count (B17)-(B19).
7. Full local raw completion in (B20), outside identity, vacuum energy,
   strong charge commutation and exact code intertwining.
8. The physical-factor count and acknowledgement that the one interaction
   can couple every site in the region; no smaller support is inferred.
9. The strong limit (B23)-(B25), the optional varying-m time bound, the
   absence of an effective stopping index, and preservation of the global
   operator-norm obstruction at every finite stage.
10. The distinction from PR1774 and from the compact history Hamiltonian,
    and the stated preparation, readout and renewal boundaries.

No scientific executable, matrix expansion, moment computation or
simulation was run for this proof-first note.
