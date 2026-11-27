# C-H3-NEUTRAL-COEFFICIENT-TRANSPORT-N

NON-CANONICAL / NO AUTHORITY. L1 mathematical and exact finite H3 results.
Base Public Canon v117, main 6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed.
Reservation #2109; result-exposed addenda D-G were posted separately before
the corresponding comparisons. A-C and the failed targets remain unchanged.
No formal public probe or cross-layer claim.

## 1. Ramified locality and the unbounded affine coefficient obstruction

Use O=Z[j], Phi5(j)=0, rho=j^2, J=1+rho, lambda=1-j, K=Q(j).
Reduction O[1/2] -> F5 is well-defined since 2 is invertible modulo
lambda. Every admitted relative contact on a pair (u,v) is

    ((u+v+rho(u-v))/2, (u+v-rho(u-v))/2).

Modulo lambda it is identity because rho=1 there. A refused contact
is also identity. Every branch of the site collision B preserves the
two pair sums, and multiplies their respective half-differences by
J^e and J^(-e), e in {-1,0,1}. Their residues are the nonzero factors
2^e and 2^(-e) in F5. Thus at every site the zero/nonzero predicates
of both half-differences modulo lambda, as well as both pair sums
modulo lambda, are invariant under every tick. Half-difference is
well-defined in O[1/2] also on parity-refused states. This is stronger
than merely conserving a neutral pair sum. It does not exclude
finite phase codes whose half-differences all have the same nonzero
residue.

For the specified affine coefficient encoding

    E(a)=F0+eta sum_i a_i v_i,  a in Z^4,

where eta is fixed nonzero in O and v_i is (1,-1,0,0) at a distinct
site i and zero elsewhere, let P shift the coefficient index by one
cyclically. Fix any finite native branch history, with linear map L
over O[1/2]. Reduction of L modulo lambda is site-block-local and
invertible, with relative matter multiplier u_i in F5^*. If the
history realizes L E(a)=E(Pa), the coefficient discrepancy, after
division by eta, has columns L v_i-v_(i+1). Its reduction in the
four relative-matter coordinates is diag(u_i) minus the cyclic shift.
The first three consecutive columns have a triangular 3-by-3 minor
with nonzero diagonal. The rank over F5 is therefore at least three,
and a corresponding nonzero minor proves K-rank at least three.
For completeness, det=product_i u_i-1, so among 4^4 possibilities
there are 64 rank-three and 192 rank-four cases. Both exact audits
check this classification.

For any one history the solutions of the affine endpoint equality
are empty or have dimension at most one over K. Its intersection
with Q^4, if nonempty, is a rational affine space of dimension at
most one over Q: two rational independent vectors cannot be dependent
over K in a one-dimensional K-space, since a coordinate ratio
would lie in Q. Such a line meets [-R,R]^4 in at most 2R+1 lattice
points (project onto a varying coordinate); a point meets it once.
Hence realizing all (2R+1)^4 inputs requires at least (2R+1)^3
distinct branch histories. A bounded finite-horizon native program
has only finitely many histories and cannot perform the cyclic
permutation on all Z^4 with this encoding and common affine stock.
This proof includes arbitrary fixed eta, even if eta is divisible
by lambda. It makes no claim about nonlinear encodings, different
carrier supports, input-dependent preparation, unbounded programs,
or the finite phase families constructed below.

## 2. Two-site two-tick neutral relay obstruction

On the frozen two-row geometry with identical columns and neutral
matter pairs, the complete linear branch word splits into the
material half-differences d=(d0,d1) and the four radiation rails
(g0,h0,g1,h1). Horizontal CORR is idle. Both vertical matchings on
height two are the same unordered pair. The two material rails
have the same parity decision, so only two vertical flags (one
material and one CLK) are needed per tick. The sitewise B tags
are independent e_i in {-1,0,1} at each of the two ticks. All native
histories are included in 2^4 * 3^4 =1296 linear words.

Write alpha=(1+rho)/2, beta=(1-rho)/2. On d the admitted C matrix
is [[alpha,beta],[beta,alpha]], and on radiation it mixes g0,g1 by
the same matrix, retaining h0,h1. The refused matrix is identity.
B multiplies d_i by J^e_i; on each radiation pair its matrix has
diagonal (1+J^(-e_i))/2 and off-diagonal (1-J^(-e_i))/2.
For each sector and word let F_t=B_t C_t. A two-tick return lies in
ker(F_2 F_1-I). For any active B tag, both its pre-B material and
radiation half-differences must be nonzero. A linear functional
identically zero on the fixed kernel makes the tag impossible.
Also a genuine transport C must change at least one of the
admitted pair differences. The exhaustive exact classification,
rejecting zero pre-material first, then zero pre-radiation, then
no possible C change, is:

    zero pre-material: 1176
    zero pre-radiation: 12
    all C changes vanish on fixed kernels: 108
    survivors: 0

The first audit computes field-valued nullspaces; the alternate
uses integral scaled matrices and fraction-free row ranks, with
a row functional nonzero on the kernel iff appending that row
increases rank. Both give exactly the same partition.
These necessary conditions already eliminate every active-C
two-tick return, without needing to impose extra parity/balance
conditions. Consequently the declared two-cell relay with fixed
neutral material, actual transport, and full two-tick return
cannot be obtained at any stock magnitude in this carrier.
This does not exclude a longer stride or an active two-dimensional
field. The classification is an exact finite computation, not a
general impossibility theorem for H3.

## 3. Frozen genuinely two-dimensional search C

For (x,y) on 8 by 4, bit zero, use background

    (s,-s,0,2J t), s=(-1)^y, t=(-1)^(x+b*y), b in {0,1}.

At (0,0) add one neutral defect delta either to material pair
or radiation pair, with the frozen 80 nonzero deltas from
+/- m j^l J^e (1-j^k). The two b choices and two kinds give
320 preparations. Test the frozen complete-field horizontal
translations +/-2 at every even stride through 256.
There are zero successes. Both spatial C directions actually
change values in all 320 trajectories. All 81152 executed ticks
preserve the complete linear sums, H,Q and exact inverse.

Eight distinct preparations close within the horizon. They are
exactly material defects delta=j^k-1, k=1,2,3,4, for each b.
The minimal full periods including bit are 240 for b=0 and 80
for b=1. The remaining 312 do not return within 256; no all-time
claim is made for them. The 8 closed cases are separately
replayed on the literal pinned native source, with no earlier
return and four distinct quarter cuts. Their common q account
is 512. The quarter hashes are records, not an independently
selected Galois reader.

## 4. D, E, F: distinct phase orbits and a clean neutral shuttle

D was declared after the preceding period census and before
cross-preparation comparisons. For each b let E_b(k) denote
the same 8-by-4 background with d(0,0)=j^k and its opposite
material rail, and k=1..4. Over the entire known period of
each input, the only intersections with these four complete
preparations are its own initial and final states. Both tested
quarter-period orientations fail for a raw fixed-port Galois
map. D also records that the actual marked d becomes 1 for
every k at the half-period.

E was declared before inspecting the other half-period
coordinates. Include k=0, the unperturbed control. At t=120
for b=0 and t=40 for b=1 all five inputs have (1,-1) at the
source; exactly two of 128 raw slots vary across the five
complete fields, both in the material pair at (0,2).
That pair has zero center and actual half-difference j^k.
The two raw values are (j^k,-j^k), and there is no
input-dependent remainder. This is a clean finite neutral
phase relocation, not merely a local distinguishability
witness. At the endpoint each input has the same complete
stock as the control outside this pair.

F then checked equality with the literal initial stock and
found, for both b and every k=0..4, exact complete vertical
translation by two rows at these half-periods, including
the unperturbed control and the matching bit. In particular
all common stock also returns at that cut. Thus these are
exact closed two-stroke shuttles on 8 by 4.

F's direct height-8 prolongation with one marker does not
work: none of the four nontrivial inputs on either background
has the requested full vertical translation in any even
stride through 256. There is no common single-marker witness.
On 8 by 8 a separate frozen two-marker family at y=0,4,
k,l=0..4, was checked at s=120 for b=0 and s=40 for b=1.
The desired direction is +2 at b=0 and -2 at b=1.
Exactly 17 of 25 (all 16 k,l in 1..4 and (0,0)) match
that direction; 5 of 25 (the equal pairs including (0,0))
match the reverse direction. Both complete 25-input targets
fail. Single-marker and entire-family failures are retained.

## 5. G: autonomous four-stroke two-phase transport

After F, addendum G froze a new, restricted finite family
of two nonbaseline independent phases, before executing
any four-stroke continuation. No earlier failed threshold
was changed. On 8 by 8 use the exact same background as
section 3. The only two initial changes are

    d(0,0)=j^k, d(0,4)=j^l, k,l in {1,2,3,4},

and the opposite material rails; all radiation and other
material values are the same fixed background. Bit zero.
No prepared future output phase table, input-specific payer
layout or external action during evolution. The two marked
values are supplied independently as raw roots, not produced
by a native source preparer.

For b=0, s=120,a=+2; for b=1, s=40,a=-2. At every complete
stroke, for r=0,1,2,3,4, the entire field is the literal
initial field shifted vertically by r*a. In particular the
only two phase-marked pairs are at y=r*a and y=4+r*a mod 8.
All other 252 registers are the initial background at the
stroke cuts (including all radiation), and the bit is zero.
The full H is conserved, as are both complete linear sums,
with q=1024 for all 32 preparations. The count 256 refers
to raw ring slots, not to independent physical particles.

Both exact native update implementations check every tick
through 4s for each input: 10240 ticks in this G audit.
They check full inverse, complete accounts and literal
full-field equality at each stroke. The least full periods,
including bit, are:

| b | k!=l (12 inputs) | k=l (4 controls) |
|---|---:|---:|
| 0 | 480 | 240 |
| 1 | 160 | 80 |

All 24 unequal pairs have exactly four distinct stroboscopic
full states; all 8 equal controls have exactly two. This
is the actual native repeated transport of two independent
nonbaseline phase values, and no stock is replenished.
Equal values cannot distinguish the two opposite markers.

The fixed two-row translation commutes with the H3 update
(including the matching bit) because it is an even translation:
both matching masks, the horizontal edges and the sitewise
collision are unchanged. Thus once one exact full-state
translation holds at the fixed stride, induction supplies
every further shifted stroke. The verified complete period
also directly supplies indefinite repetition of this same
prepared experiment. It does not supply fresh-input renewal.

## 6. Galois address code, mathematical interpretation only

For b=1 choose the two distinct raw markers j and j^2.
Let E_r be the exact full field translated by -2r rows
from E_1(1,2), r mod 4 (E_1 here denotes background b=1).
Use the fixed four-address code that labels the position
y=-2r mod 8 of the marker j by j^(2^r mod5). The other
marker remains a necessary part of the demonstrated
carrier. The four E_r are distinct, and the actual
complete evolution satisfies F^40 E_r=E_(r+1).
The mathematical code therefore intertwines that
stroboscopic evolution with sigma(j)=j^2 on the four
nontrivial fifth roots. This is a definitional finite
address representation after G, not a native raw
Galois arithmetic map, an independent selection of sigma,
or a claim that the single-marker target F passed.
The raw phase values of both moving markers do not change
at the stroke cuts. There is no native readout circuit,
no general additive or signed/zero code, no four-independent-
coefficient transfer, no paired commutator/dual continuation,
and no claim of physical space or geometry from this result.

## 7. Status

The proof in section 1 is candidate-T at its stated L1
scope. Section 2's complete branch census and the native
finite witnesses are candidate-C, with explicit symbolic
implications. The code interpretation is conditional on
the finite G result and the declared fixed reader. The
two algorithms are separately written but result-exposed;
not a blind independent reviewer. The D-G addenda are
successor diagnostics within this non-formal incubation,
not a changed threshold or reused sealed public probe.
No formal architecture gate, physical adoption, native-U
equivalence, RH estimate, curvature selection, cross-layer
lift or Canon status change follows.
