# C-J-TRACE-DUAL-NATIVE-RAIL-N

NON-CANONICAL / NO AUTHORITY. L1 mathematical and finite H3 witnesses.
Reservation and predicted numerical results: issue #2104, posted before
the first computation. Public basis v117, main
6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed. Predecessor #2102 and draft #2103.
No new physical dictionary, no Canon fold.

## 1. An integer rail is a full trace-dual label carrier

Put O=Z[j], Phi5(j)=0, B(x,y)=Tr(x conjugate(y)),
delta=Phi5'(j)=5 j^4/(j-1), and ell(w)=[j^3]w in the power basis
(1,j,j^2,j^3). Since delta^-1=(j^2-j)/5, checking w=1,j,j^2,j^3
gives Tr(w/delta)=ell(w): the numerators have traces 0,0,0,5.
Both sides are Q-linear.

The bilinear coefficient pairing (x,f)->ell(x f) on O is integral
and perfect: its matrix in the power basis is zero when the two
indices sum to less than three, and one when they sum to three.
Reversing columns gives a triangular integer matrix with diagonal
one. Consequently the map f->conjugate(f/delta) is an isomorphism of
the integer module O onto the entire trace-dual lattice O#,
and not merely onto a sublattice. For the marked bases j^i and
J j^k, i,k=1..4, the change matrices are unimodular, so the resulting
pairing is also unimodular.

This is a fixed mathematical representation. All raw rail values
are integers in O. In particular 5y=conjugate((j^2-j)f) lies in
(1-j)O, and that numerator lattice is the whole 5O#.
There is no physical fractional register or independently established
physical energy of the decoded fractional label.

## 2. Reciprocal contact supplies paired transport

Use the exact public H3 source in
reproduce/h3-referenced-record/verify.py at the base commit,
blob fd215e24fefbbebf83cf3985d8ebcedd590aa709.
At an admitted B1 contact, on the two half-differences d,f, the native
map is (d,f)->(Jd,J^-1 f), with each pair center unchanged.
B2 is its inverse. Therefore d f is invariant (also on refused
identity contacts). Under the representation y=conjugate(f/delta),
this is exactly the paired action d->Jd, y->conjugate(J)^-1 y.
B(d,y)=ell(d f) is invariant at that contact. No identical claim
about arbitrary full-field C-transport is made.

Let T=h(J)=2-phi, phi=-j^2-j^3, h(z)=z conjugate(z).
For every x=j^i, u=j^k, choose a uniform 8 by 4 field with
cell (x,-x,Ju,-Ju). C is idle for both matching bits because each
rail is spatially constant. B1 fires because h(Ju)=T h(x)=T.
B2 fires at the next tick since h(Jx)=T h(u). The bit also returns.
The complete ring quadratic account per cell is 2+2T, with positive
half-trace q=10; total q=320. Every local d f and hence ell(d f)
is retained. For the 25 choices ell(J j^(i+k)) has the values
(0,1,-1,1,-1) for i+k modulo five. The four-by-four basis
submatrix is unimodular by section 1.

For completely independent raw x,f in O, use the fixed 8 by 4 bit-0
layout from the preregistration. The two half-field regions contain
respectively (x,-x,Jx,-Jx) and (J^-1 f,-J^-1 f,f,-f).
C is idle because each matching lies in one region on the CORR rail
and the other rails are constant along each column. Each nonzero
region fires B1 by the same norm balance, while a zero region is idle.
After one tick the designated data differences are Jx and J^-1 f,
and their product and coefficient pairing are invariant.
The exact full inverse is B followed by inverse C with the original
matching bit. This is an all-input construction with input-dependent
payers and repeated copies, not a common fixed independent stock.
The finite audit covers the preregistered 81 signed and zero cases.

## 3. Native finite phase-pairing reader

Raw inputs are x,u in {0,1,j,j^2,j^3,j^4}; the dual label numerator
of interest is f=Ju. The fixed 8 by 6 field uses matter half-difference
d_a=x-j^a on columns a=0..4 and zero on padding columns.
The radiation half-difference is f_b=J(u-j^b) on rows b=0..4 and
zero on padding rows. Initialize the two matter rails d_a,-d_a,
CLK=0 and CORR=-2 f_b. This is a fixed affine preparation rule in
the two raw data values with copies and offsets; it is not a
native preparation circuit.

C is idle on the entire field: the matter rails and CLK are constant
along their vertical directions, CORR along its horizontal direction.
The marked B1 gate is exactly h(d_a)=h(u-j^b) with both differences
nonzero. For nonzero roots,
h(j^r-1) is 0 for r=0, 3-phi for r=1,4, and 2+phi for r=2,3.
For a zero input its difference to any reference has h=1.
These values are pairwise distinct. B2 would require
h(d_a)=T^2 h(u-j^b) with nonzero values; this is impossible
since at the principal embedding 0<T^2(2+phi)<1 and every
nonzero member of the four-value set is at least one.
All padding cells are idle because at least one difference is zero.

After B1, CLK'=-f_b+J^-1 f_b=(1-J)(u-j^b), which is nonzero
precisely when that gate fires; otherwise CLK remains zero.
The observation uses actual post-update CLK coordinates, not
an event list or the externally computed raw product.
For x=j^i,u=j^k, the exact support is
i-a = +/- (k-b) mod 5 with both differences nonzero.
The line a+b=i+k contains five positions, one with both zero,
so exactly four flags. For any other line a+b=m, the other
equality i-a=k-b has exactly one solution because two is invertible
modulo five; that solution has nonzero differences. Thus five
diagonal counts are a cyclic rearrangement of (4,1,1,1,1), and
the unique four determines i+k. Exactly one zero input gives no
flags because h=1 cannot equal a root-difference norm. Both
zero inputs give all 25 flags, five per line.

The fixed observer reads ell(xJu) by the table
(0,1,-1,1,-1) on the unique count-four diagonal, and zero on
the two other prescribed patterns. There are ten outputs -1,
sixteen zero (five nonzero-root pairs, eleven pairs containing
at least one zero), and ten outputs +1. In particular a zero
pairing between nonzero roots has eight actual flags; it is not
a silence convention. For exactly one zero input the all-zero
pattern is a valid read only with the known complete preparation
and fixed tick; no native completion marker is supplied.
Both-zero inputs give 25 flags. No reduction of these 25 sites
to one local output, active native reader of the counts, retention
past this cut, or native synthesis of the copied preparations
is claimed.

All accounts are explicit. Sum_a h(x-j^a) is ten when x is a root,
five when x=0, by sum_a j^a=0. The matter pair is duplicated
through six rows, so H_m=120 or 60 and q_m=240 or 120.
Sum_b h(u-j^b) similarly equals ten or five. CORR=-2J(u-j^b)
is duplicated across eight columns, so H_r=320T or 160T and
q_r=960 or 480. Thus q=1200 for all 25 nonzero-root pairs,
q=1080 when x=0 only, q=720 when u=0 only, q=600 for both zero.
The two full linear sums and the entire ring H and q are preserved
by native C and B, and the complete inverse restores the field.
Equality of q across the root family is not equality of all
initial linear sums. The audit checks all 36 fields and actual
flags, as well as equality to ell(xJu).

## 4. The remaining Galois motor and exact negative boundary

The specified predecessor commutator is K=M_v sigma,
v=j^2+j^3=j^2(1+j), sigma(j)=j^2. Its trace inverse-adjoint is
K^vee=M_(v^-1) sigma. On the present integer dual representation
the raw radiation motor corresponding to K^vee is particularly
simple:
  f' = delta conjugate(K^vee y)
     = (delta/sigma(delta)) v^-1 sigma(f)
     = j^4 sigma(f).
Indeed delta/sigma(delta)=j(1+j).
Thus the paired K motor in raw rails would be
(d,f)->(v sigma(d),j^4 sigma(f)), with exactly preserved
ell(d f). The latter follows from the trace pairing and the
coefficient identity, not from preservation of d f itself.
The reciprocal J contact in section 2 is not this motor.
Neither native Galois transformation has been implemented here.

For any finite H3 torus and bounded fixed horizon, freeze the
raw preparation z_i(x)=a_i x+b_i, with a_i,b_i in Q(j) and
admitted integral slots, and a designated single-ring output
or half-difference. Include all common stock in this preparation.
For each fixed sequence of parity and balance decisions, every
native C and B branch is Q(j)-linear on the full slots (the
identity branch included). Their finite compositions give
a field-affine expression a x+b for the output. There are
finitely many branch histories. This is independent of the
nonlinear guard conditions used to choose the history.

If v sigma(x)=a x+b agrees with one such expression, its solution
set is either empty or a translate of the Q-linear kernel
of v sigma-a. For two nonzero elements r,s in this kernel,
if a=0 neither can exist, and otherwise sigma(r/s)=r/s.
The fixed field of sigma is Q. Hence the kernel dimension is at
most one over Q. A rational affine line in Q^4 intersects the
integer coefficient box [-R,R]^4 in at most 2R+1 points, since
a varying coordinate is injective along the line. A point has at
most one. Covering the full box with (2R+1)^4 points therefore
requires at least (2R+1)^3 affine pieces. No finite bounded
native program with the stated raw affine preparation realizes
K on all O. The same proof applies to j^4 sigma on the raw
dual rail. This is a bound on affine pieces, not a claimed tick
lower bound or exclusion of finite phase codes, non-field-affine
preparations, other native alphabets or unbounded programs.

Independently, if the only varying input is a raw scalar integer
x=t with f=0 and one fixed finite common auxiliary stock, its
initial q is 2t^2+Q_aux; a required output Jt has q=3t^2, which
eventually exceeds the entire conserved input q. The analogous
signed pair has doubled values. This rules out the common-stock
unbounded raw-input contract, not the funded-copy construction
or a finite input family.

## 5. Status boundary

The coefficient pairing and stated symbolic implications are
candidate-T at L1. The finite native histories and reader are
candidate-C at their exact frozen preparations, not a physical
measurement or a formal two-architecture scientific gate.
The H3 implementation is public source-exposed evidence.
The alternate arithmetic calculation is independent of that code
but result-exposed and only verifies the reader counts, values and
account, not full native histories.
No native active readout of arbitrary O pairs, complete K motor,
source preparation, one-port reducer, later retention, RH bound,
asymptotic Euclidean rigidity, physical energy price or spatial
operator selector is supplied. No L1-to-L2/L4/L5/L6 lift is made.
