# C-H3-GALOIS-ADDRESS-MOTOR-N

NON-CANONICAL / NO AUTHORITY. L1 mathematical and finite H3 results.
Reservation and predictions before the first audit: issue #2106.
Public Canon v117 base 6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed.
Predecessor #2104 and draft #2105. No Canon fold or new physical dictionary.

## 1. A fixed asymmetric reference separates the ten signed roots

Use O=Z[j], Phi5(j)=0, rho=j^2, J=1+rho,
h(z)=z conjugate(z), phi=-j^2-j^3, and T=h(J)=2-phi.
Let S={0} union {+/-j^k:k=0,...,4}, w=2+j, c=1+j.
The element c is a unit since Jc=-j^4, hence c^-1=-Jj.
Direct expansion gives h(c)=1+phi=T^-1 and h(w)=3+2phi.

The nonnegative real-embedding witnesses h(t-w), recorded as exact
pairs (a,b) for a+b phi, are as follows.

| t | +1 | +j | +j^2 | +j^3 | +j^4 |
|---|---|---|---|---|---|
| h(t-w) | 1+phi | 4 | 5+3phi | 4+5phi | 6+phi |

| t | -1 | -j | -j^2 | -j^3 | -j^4 |
|---|---|---|---|---|---|
| h(t-w) | 7+3phi | 4+4phi | 3+phi | 4-phi | 2+3phi |

For t=0 it is 3+2phi. These formulas follow from
h(t-w)=1+h(w)-t conjugate(w)-conjugate(t)w for a root t,
and from the two cosine sums j+j^4=phi-1 and j^2+j^3=-phi.
They are exact identities of the real quadratic ring.
Since 1 and phi are linearly independent over Q, equality to 1+phi
holds only for t=+1. All eleven values exceed T at the principal
embedding (use 1<phi<2); this excludes equality to T in the ring.

## 2. A native single-address write

For each signed output address (s,b), s=+1 then -1, b=0,...,4,
set z=s j^b, r=s j^(3b), so sigma(r)=z for sigma(j)=j^2.
Let m be a fixed nonzero unit. For raw x in S prepare the H3 cell
(r0,r2,CLK,CORR)=(d,-d,0,-2f), where

    d = m c^-1 (x-rw)
    f = -J rho^-1 m z.

The preparation is one field-affine rule in the actual raw input.
The radiation stock and all reference offsets are common across
the input family. Copies and offsets are supplied, not generated
inside this apparatus. The initial CLK is zero at every address.

At a B1 collision h(f)=T h(d), with d nonzero. Since h(z)=h(r)=1
and m is nonzero, this is equivalent to h(x/r-w)=h(c)=1+phi.
By section 1, exactly the cell whose reference r equals x qualifies
if x!=0, and none qualifies for zero. B2 would require
h(x/r-w)=h(c)T^2=T, which is excluded by the same table.
There are no other first-step branch events. At a hit, the radiation
pair center is -f and its half-difference becomes J^-1 f. Therefore
the actual output register becomes

    CLK' = (J^-1-1) f
         = (J^-1-1)(-J rho^-1 m z)
         = m z.

It is zero at all other addresses. The actual value, not just a
branch flag or a decoded index, is m sigma(x) at the address
(s,2k mod 5) for x=s j^k. For x=0 the strip is empty.
A fixed observer can pick the only nonzero entry; this is a
distributed output, not a native reducer into one fixed register.
Empty output means zero only in the declared input/cut context.

The same branch selection would also work for a different assigned
permutation of the signed roots by changing the reference-to-stock
wiring. Thus this realizes the specified sigma on a finite phase
code; it does not independently select or derive sigma from the
H3 law. Every possible output phase is present in the common stock
as a payer phase. It is not a general raw-ring arithmetic circuit.

## 3. Complete autonomous two-tick recurrence on 8 by 20

Place addresses in order +0,...,+4,-0,...,-4, each duplicated on
two adjacent rows, and repeat all rows on each of the eight columns.
The unchanged H3 matching bit starts at zero. The pinned source
is reproduce/h3-referenced-record/verify.py at the base commit,
Git blob fd215e24fefbbebf83cf3985d8ebcedd590aa709.
C transports r0,r2,CLK vertically and CORR horizontally, with the
declared integral-parity refusal and rho rotation. B is the
unchanged reciprocal collision.

At the first C every matching pair is equal, so C is identity.
At the first B the previous section applies independently at all
cells. At the second C, bit one pairs the end of one address with
the start of the next. Consecutive reference phases are distinct
modulo 2, also across the sign seam and periodic wrap. The quotient
O/2O is F16: Phi5 is irreducible over F2 (ord_5(2)=4).
The five powers of j remain distinct and c,m are units there.
On two inactive neighboring addresses the difference of matter
half-differences is a unit times the difference of two distinct
root residues (w=j mod 2), hence nonzero modulo 2. Their C edge
refuses.

If exactly one neighboring address is active, write its reference
r=x. Its initial d=-m r becomes -J m r. Equality of its post-B1
residue to the inactive neighboring d'=m c^-1(r-r'w) would require

    r'/r=(1+j^4)/j mod 2,

since Jc=-j^4 and w=j mod 2. This cannot be a root residue:
a sum of two distinct roots cannot be a root in F16, because that
would be a relation with three terms among the fifth roots, whereas
the only nonzero F2 relation on the five powers is their full sum.
Thus both signed matter rails refuse across this edge as well.
At most one address is active, so an active CLK value (a unit)
also has odd difference from the inactive zero neighbor. Two zero
CLK values are equal. CORR is horizontally constant at all cuts.
Therefore the entire second C is identity. The same parity proof
covers the inverse C maps at these cuts.

At the second B, the collision at every active cell is precisely
B2, because the two relative accounts have been exchanged by B1.
Every inactive cell is unchanged. Hence the complete field returns
after two ticks and the matching bit returns too. There are sixteen
B1 events and sixteen inverse B2 events when x is nonzero, none
for x=0. This establishes repetition indefinitely on the same
prepared input; it is not fresh-input renewal or composition of
the output with another Galois step.

## 4. A single closed paired field on 8 by 44

The predecessor target is K=M_v sigma, v=j^2+j^3=j^2(1+j)=-phi.
On the integer representation of a trace-dual label by raw f,
its paired inverse-adjoint motor is j^4 sigma. Put a 20-row
m=v motor with input x in S followed by a two-row guard, then
a 20-row m=j^4 motor with independent input f_in in S followed by
a second two-row guard, wrapping periodically. All columns are
identical. Guard cells have (g,-g,0,0), repeated in both rows and
all columns, with fixed g independent of x and f_in.

For each endpoint row, the initial d has at most six distinct
residues modulo 2 as x runs over S, since signs coincide mod 2.
Only the one hit can add a different residue after B1, so at most
seven values are possible. At each guard take the union of the
two adjacent endpoint sets (size at most fourteen). In the
preregistered lexicographic order of {0,1}^4 in the power basis,
choose the first residue outside that union. This is possible
because there are sixteen residues. The exact finite witness is

    g_A=(0,0,1,0)=j^2
    g_B=(0,1,1,0)=j+j^2.

All guard B events are idle because their radiation difference
is zero. All second-C matter edges incident to a guard refuse
by its choice; the CLK edge is either between two zero values
or a zero and a unit. The interior arguments of section 3 are
unchanged. This gives one fixed, closed 352-cell field for all
121 independent ordered inputs. The two fixed strips at column
zero, rows 0,2,...,18 and 22,24,...,40 respectively, contain
the actual values v sigma(x), j^4 sigma(f_in), with one occupied
address for a nonzero input and no occupied address for zero.
No external multiplication is needed to extract those values.

Let ell(w)=[j^3]w in the power basis (1,j,j^2,j^3). For every w in O,

    ell(v j^4 sigma(w))=ell(w).

Indeed v j^4=j+j^2, and the identity on the four basis elements
1,j,j^2,j^3 follows by reducing powers modulo Phi5. Hence the
actual output values preserve ell(x f_in). Equivalently, using
the predecessor dual representation y=conjugate(f_in/delta),
delta=Phi5'(j), the pairing B(x,y)=ell(x f_in) is preserved.
The 121-pair audit uses actual occupied CLK values for this
comparison, not the target formula alone. No native pairing
reducer on the new strips or live connection to the earlier
reader is asserted.

## 5. All resources are counted

There are sixteen cells per signed address. The ten reference
roots sum to zero. Consequently
sum_r h(x-rw)=10(h(x)+3+2phi).
The complete quadratic account H of one motor block is

    H=320 h(m) T (h(x)+5+2phi).

It equals 320 h(m)(8-3phi) for zero and
320 h(m)(10-4phi) for a nonzero signed root. The scalar account
Q is the real quadratic trace of H. In particular:

| m | x=0 | x!=0 |
|---|---:|---:|
| 1 or j^4 | 4160 | 5120 |
| v=-phi | 3840 | 4480 |

The two guard pairs add
32(q(g_A)+q(g_B))=32(2+3)=160, with q(z)=Tr_real(h(z)).
Thus paired Q is 8160 for both zero, 8800 for x nonzero only,
9120 for f_in nonzero only, and 9760 for both nonzero.
The complete matter and radiation sums are each zero, since
matter pairs are opposite and all signed payer phases sum to
zero. B preserves both pair sums and the full H, not just Q.
C is idle on the declared recurrence. Every account is audited
at the initial, first and returning cuts, with both exact full
inverse compositions. This is an existence cost, not a minimum.

## 6. Status and next boundary

Sections 1-5 are proof-led mathematical candidate-T implications
at their declared L1 carrier and preparation. The 132 complete
native H3 histories are candidate-C corroboration, not an adopted
native-U or physical realization. The frozen audit includes all
11 inputs for A and all 121 ordered inputs for B. It checks all
actual cells and inverse steps; the alternate five-power ring
audit implements local C and B independently of the pinned
source and uses row symmetry to represent the complete field.
The matching transcript hashes of initial, written and returned
fields are reproduction evidence, not the only correctness
checks. Both scripts are result-exposed, not blind independent
reviewers.

The prior bounded raw-field-affine obstruction on all O is not
overturned: the admitted input set is precisely the ten signed
roots and zero. The first preparation duplicates raw inputs
with fixed offsets; the phase-selecting radiation stocks are
fixed, not supplied after the answer is known. There is no
native source-copy circuit, one-port output, native completion
marker for zero, automatic chaining of successive Galois powers,
fresh-input reset, RH estimate, curvature selection, physical
dictionary, or cross-layer gate. The period of this apparatus
is two, not the order-four Galois orbit: its second tick erases
the write by exact inverse, rather than applying sigma again.
