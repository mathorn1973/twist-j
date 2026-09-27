# Contact-run skeleton and an all-contact quarter-turn Xi bound

**PUBLIC, NON-CANONICAL. candidate-T written proof, pending separate review.**
Owner: #1192. Author: A. M. Thorn <thorn@twistj.com>.
Date: 27 September 2026. License: Apache-2.0.
Basis: Public Canon v92, main `8b1132d828d94f83e653dab34d686a7e68394939`.

This answers a narrower, precise question than a global prism-extraction
claim. Straight contacts have a canonical ribbon skeleton, but that skeleton
need not be one product prism. More importantly, an unstructured class of
single current cycles can be controlled without extracting a prism at all.
Every cycle with at most one turn per four edges is covered, regardless of
its opposite-edge contacts. Nothing here bounds the complementary sector.

## 1. Fixed measure and observables

On every even periodic four-torus of side L>=4, V=L^4, use

    mu_L(n)=Z_L^-1 2^(-|supp n|) 1{partial n=0 mod5},
    n_p in {-1,0,1}, j=partial n/5.

Keep the one-copy paired augmentation of public-main CONNECTED-CURRENT.md.
At a neutral edge, match positive and negative occupied face incidences;
at a charged edge, all five occupied incidences belong to one component.
Its unsigned weights sum to the original Z_L. In a component K choose a
reference signing eta_K. Then J_K=partial eta_K/5 is an integer conserved
current and component signs are independent fair signs conditional on the
unsigned structure. In particular a charged edge has exactly one owner K.

The slice primitive and cost, as in public-main SIGNED-SLICES.md, are

    B_K(r)=sum_(x:x1=r) J_K(e0(x)),
    H_K(r)-H_K(r-1)=B_K(r),
    ell_K=min_(h in Z) sum_(r in Z/LZ)|H_K(r)-h|,
    Xi_L=(1/V) E_aug sum_K ell_K^2.

The primitive exists because J_K has zero total current in every direction.
For one unit simple cycle gamma write m for its edge count, c for its turns
(including the closing vertex), and n_i for its direction-i edge count.
When J_K is that single cycle, it has zero winding: its total direction-i
current equals L times its winding, and it is also a boundary divided by five.

Define Xi_quarter by retaining only components whose current is one unit
simple cycle and 4c<=m. It is a nonnegative part of Xi_L, not its replacement.

## 2. Exact contact-run skeleton

Two opposite parallel edges on a plaquette are reinforcing when their physical
current directions are opposite. Let O_+ count these pairs and O_- the other
pairs. Every current edge has at most six opposite parallel neighbors, so

    O_++O_-<=3m.                                               (1)

For each axis i and each unordered neighboring pair of transverse coordinate
lines, mark the longitudinal positions where the two selected i-edges form
a reinforcing contact. Maximal consecutive marked positions on the cyclic
longitudinal coordinate are the straight contact ribbons. Each contact belongs
to exactly one ribbon, hence, with ribbon lengths d_alpha,

    O_+=sum_alpha d_alpha.                                    (2)

No marked longitudinal circle is full. A full circle would force a whole
coordinate loop into the simple cycle; simplicity then makes it the entire
cycle, contradicting zero winding. Ribbons are therefore proper cyclic
intervals, even when they cross the periodic seam.

Split the oriented cycle into its maximal straight runs. There are c runs.
A run has constant sign on its coordinate line, and has a unique first edge
in the positive geometric coordinate order, independently of its traversal
orientation. A contact ribbon starts only when at least one of its two runs
starts: otherwise both predecessor edges and the same opposite signs would
be present, extending the ribbon backward. Charge its start to one such
run by a fixed lexicographic tie rule. A run start has at most six transverse
neighbor lines and thus receives at most six ribbon starts. Consequently

    R_+:=#{ribbons}<=6c.                                      (3)

This proves an exact, deterministic extraction dichotomy:

    O_+>6c(R-1)  =>  some reinforcing ribbon has length >=R.   (4)

It does not prove that a positive contact density alone gives a macroscopic
prism. It does not align different ribbons into one prism or control the cost
of joining them. The entropy estimate below does not require such a claim.

## 3. The signed cycle cost, including periodization

Lift gamma to a closed nearest-neighbor path in Z^4; zero winding makes the
lift closed. Its x1 span d is at most n1/2. Define the lifted slice source
B_tilde(r) by summing the signed direction-zero edges at lifted level r.
It has total sum zero and total variation norm at most n0. Its primitive
H_tilde, chosen zero before its support, is zero after it as well and is
nonzero on at most d intervening slice intervals. Any value of this primitive
is a partial sum of a zero-sum sequence. Its absolute value is at most half
the l1 norm of that sequence, hence at most n0/2. Therefore

    sum_(r in Z)|H_tilde(r)|<=d*n0/2<=n0*n1/4.                (5)

This argument takes place in the lift, not on a putative empty torus slice.
Periodize it:

    H_per(r)=sum_(k in Z) H_tilde(r+kL).

This is a finite sum, is integer, and its difference is exactly the projected
torus source B_gamma. Thus it is an admitted torus primitive. By the triangle
inequality and the option h=0 in the torus minimization,

    ell(gamma)<=sum_r |H_per(r)|
              <=sum_(r in Z)|H_tilde(r)|
              <=n0*n1/4<=m^2/16.                            (6)

This remains valid even when the lift spans several periods. It requires no
coordinate relabeling of a probability law. A simple zero-winding cycle has
at least four straight runs: fewer cannot close a nonbacktracking path in
coordinate directions. Consequently 4c<=m implies m>=16.

## 4. Existing full-measure source estimate

For completeness, the input is the integrated source comparison, not a
conditional probability under arbitrary exterior currents. For an edge set S
and prescribed nonzero current signs v on S, let Q_S(v) sum the original
face weights with that prescription and every other current unconstrained.
Finite character expansion with continuous integration on S and Z5
integration elsewhere gives, for real f supported on S,

    Q_S(v)/Q_S(0)<=exp(-5<v,f>) product_p cosh((df)_p).         (7)

One can see positivity directly: the modulus of the complex face factor is
|1+cos(theta-iy)|=cosh(y)+cos(theta). After expanding this factor, the
zero-selected-current sector is obtained, with the weight of each empty face
multiplied by cosh((df)_p). Its product bounds each nonnegative coefficient.
All unselected currents remain summed. Also Q_S(0)<=Z_L.

Take f=h gamma for a simple cycle of length m. Each edge meets six plaquettes.
The pairs of selected neighboring perpendicular edges are precisely its c
turns; the other selected pairs on a plaquette are its opposite contacts O.
For at most four selected edges on a plaquette,

    cosh(kh)<=cosh(h)^k [1+tanh(h)^2]^(k(k-1)/2).

It follows exactly as in public-main FULL-MEASURE.md section 10 that

    P(E_gamma union E_-gamma)<=2 a^m r^(c+O),
    a=exp(-5h)cosh(h)^6, r=1+tanh(h)^2,                    (8)

where E_gamma fixes j on gamma only. At h=log 2,

    a=15625/131072, r=34/25,
    B:=a r^3=4913/16384.                                  (9)

Using (1), the right side of (8) is at most 2 B^m r^c. This deliberately
pays for every contact, even when its true sign would improve the estimate.

## 5. A turn tilt pays for ALL contacts

Fix v=1/16, so rv=17/200<1. On the class 4c<=m,

    r^c = v^(-c)(rv)^c <= 2^m (rv)^c.                     (10)

Start a cycle along a fixed positive edge e. Each unoriented cycle through e
has exactly one traversal with this initial orientation; the two possible
current signs are already covered by the factor 2 in (8). Delete only its
closing test, simplicity test and quarter-turn restriction after (10) has
been used. A nonbacktracking continuation has one straight next step and six
perpendicular next steps. Assign a turn weight rv. The internal weighted
path sum is (1+6rv)^(m-1). The closing turn, when present, supplies a further
factor rv<1 and may be omitted in this upper bound. Thus for each root edge
and m>=16,

    W_m(e):=sum_(gamma through e, |gamma|=m, 4c<=m)
                  P(E_gamma union E_-gamma)
       <=2(2B)^m (1+6rv)^(m-1)
       = A q^(m-1),                                      (11)

where the exact values are

    A=4B=4913/4096,
    q=2B(1+6rv)=741863/819200<1.                           (12)

The integer gap is 819200-741863=77337>0. No independence of current edges,
no restriction on opposite contacts, and no fixed-axis bundle assumption is
used. This exchanges the earlier low-contact/all-turn criterion for an
all-contact/low-turn criterion; it does not assert one class contains the other.

## 6. Exact edge rooting and a uniform tail

For each selected component with one unit cycle,

    sum_(positive lattice edges e) 1{e in supp J_K}/m_K=1.

Hence sum this identity inside the original augmented expectation. There are
4V positive edges. Each has at most one charged component owner. The event
that this component has current +/-gamma implies E_gamma union E_-gamma for
the full original current, because no other component contributes at a
charged edge of gamma. Equation (6) gives ell_K^2/m_K<=m_K^3/256. Applying
(11) separately at every edge therefore proves

    Xi_quarter(L) <= C_quarter
       := (A/64) sum_(m>=16) m^3 q^(m-1).                 (13)

The factor four is from summing 4V roots, not from an incorrect equality of
orientation-specific ell expectations. The same proof with m>=R gives

    Xi_quarter,>=R(L)<=(A/64) T_R(q), R>=16,               (14)

with

    T_R(q)=q^(R-1) [R^3/(1-q)+3R^2 q/(1-q)^2
               +3R q(1+q)/(1-q)^3
               +q(1+4q+q^2)/(1-q)^4].

The formula follows by expanding (R+n)^3 and summing the four elementary
power series. It tends to zero independently of volume. This controls both
the total selected contribution and its long-cycle tail, while leaving
neutral fillings fully summed. It is not a theorem about the full current
susceptibility or the full Xi moment.

## 7. Non-prismatic L-strips are included

The planar L-strip family in PREREG.md has, for n>=2,

    m=4n+4, c=6, O_+=2n, O_-=0, ell=2n+1.

Indeed the horizontal arm gives n reinforcing opposite-edge contacts, the
vertical arm gives another n, and no other opposite edges are at unit distance
for n>=2. They form exactly two straight contact ribbons, each of length n.
The signed primitive is n+1 on the first axial interval and one on the next n
intervals, giving ell=2n+1 on a sufficiently padded torus; translating across
a seam does not change it. Periodization can only decrease that upper cost.
The quarter-turn condition holds for all n>=5.

The earlier signed-contact sufficient class used r3=41/25, tau=73/70 and
requires r3^(2n)<=tau^(4n+4). The inequality is reversed at n=5 by an exact
rational comparison, and r3^2>tau^4 propagates that strict reversal to every
larger n. Thus the new criterion covers cycles outside that old class.

These nonrectangular cycles use only two axes. The previously declared
fixed-displacement ribbon construction, on a two-axis carrier, must have a
straight base in the other axis and therefore gives a rectangle. A declared
simple cross-section polygon times a nontrivial complementary base requires
at least three used coordinate axes. The L-strips therefore do not have any
of those specific product descriptions. This observation is not an exclusion
of every possible broader prism or piecewise-ribbon representation.

## 8. Boundary and next mathematical debt

Equations (2)-(4) give a canonical straight contact skeleton for every simple
zero-winding cycle. Equations (13)-(14) uniformly control the unrestricted
quarter-turn single-cycle sector. No global prism-extraction theorem is
assumed, proved or needed for that sector.

To cover all simple-cycle components, the remaining target is the high-turn
sector 4c>m after retaining any separately proved contact or bundle subclasses.
For the entire Xi_L, components with several current cycles and non-simple
current networks still have their own coherent-sum debt. A small bound on each
individual cycle is not an independence theorem for those components.

P1 also needs its strictly positive macroscopic comparison. Neither the
common conditional-variance floor in Canon v92 nor the new restricted upper
bound supplies it. Xi_L, Xi_L^(2), P1 and the physical-photon claims remain
open. The finite audit corroborates algebra and examples only; no independent
proof review or two-architecture scientific gate is claimed.
