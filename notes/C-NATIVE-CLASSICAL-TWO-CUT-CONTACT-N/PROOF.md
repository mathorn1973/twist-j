# Actual native signal, conditional transduction, and the complete two-cut state

**NON-CANONICAL / conditional candidate-T / L1 analytical proof.**
Original work Apache-2.0, A. M. Thorn, 2026-10-13. Reservation #1486.

The family, distinction, transducer and schedule are fixed in CONTRACT.md,
publicly pinned and fully read back at
`7b3fa47c0223bd99fce977de6ea58d484e257033` before this proof document.
The inherited native first-step table and classical matrices were already
exposed. No scientific program, physical instrument or numerical probe was run.

## 1. Native preparation and three actual ticks

Write x=(a,b,c,d,q,r) in F5^6. All arithmetic in this section is modulo five.
The canonical generators, indexed 0 through 4, are

    g0 x=(b,a,d,c,q,r),
    g1 x=(-c,-d,-a,-b,-q,-r),
    g2 x=(2-c,1+r-d,2-a,1-r-b,1-q,-r),
    g3 x=(2-a,1-b,3-c,4-d,1-q,1-r),
    g4 x=(2-a,1-b,3-c,4-d,2-q,1-r).

Each g_j is an involution. The unchanged native update chooses
j=sum(x)+2 theta_n mod5, then applies g_j and increments n. Take
x0=(p0,p1,p2,p3,0,1), h=sum_i p_i. The total sum initially equals h+1.
For the prescribed bits theta_0,theta_1,theta_2=0,1,1, direct substitution
gives the following complete branch schedule and receivers. Here j_i is the
generator used for tick i -> i+1, and C_i=(q_i,r_i).

| h | (j0,j1,j2) | C1 | C2 | C3 |
|---|---|---|---|---|
| 0 | (1,1,3) | (0,4) | (0,1) | (1,0) |
| 1 | (2,2,4) | (1,4) | (0,1) | (2,0) |
| 2 | (3,1,3) | (1,0) | (4,0) | (2,1) |
| 3 | (4,1,3) | (2,0) | (3,0) | (3,1) |
| 4 | (0,2,4) | (0,1) | (1,4) | (1,2) |

To check that the selectors as well as the receivers are correct, the total
sum transforms under (g0,g1,g2,g3,g4) respectively as
(z,-z,2-z,2-z,3-z). Starting from h+1 gives the displayed j1,j2. Each row
therefore applies to all 125 inputs with that h, not just a representative.
Every row ends at total sum one.

All native coordinates at every boundary are specified without a reset by

    x1=g_j0 x0,   x2=g_j1 g_j0 x0,   x3=g_j2 g_j1 g_j0 x0.

For additional explicitness, the final four pistons are

| h | piston part of x3 |
|---|---|
| 0,1 | (2-p0,1-p1,3-p2,4-p3) |
| 2,3 | (-p2,-p3,-p0,-p1) |
| 4 | (p3,p2-1,p1+1,p0-1) |

Together with C3, this gives the whole native endpoint and retains all four
original degrees of freedom on the prepared family. The original pistons
were the only input-dependent preparation. The receiver and clocks were common.

## 2. Encoding is derived at the contact boundary

The contact reads the current C1, not h or the original pistons. Apply the
fixed balanced lift ell=(0,1,2,-2,-1) and
eta(q,r)=(ell(q)/2,(ell(r)+1)/2,0,0). The induced encoding is

| h | E(p)=eta(C1(p)) | preparation work E_D(0,S E(p)) |
|---|---|---|
| 0 | (0,0,0,0) | 0 |
| 1 | (1/2,0,0,0) | 1/10 |
| 2 | (1/2,1/2,0,0) | 3/20 |
| 3 | (1,1/2,0,0) | 2/5 |
| 4 | (0,1,0,0) | 2/5 |

All five vectors are different and have maximum coordinate at most one.
Consequently E(p)=E(p') if and only if h(p)=h(p'). This proves exactly the
chosen five-class distinction, not injectivity on 625 piston inputs. Present
zero is included; absence is not an additional class in this experiment.

The work column follows directly from
E_D(0,Sz)=(sum_i z_i^2-(sum_i z_i)^2/5)/2. No output is used to define or
qualify E. In particular E is not defined through M^-1 b0. Its offset and
scale are frozen transducer choices, not quantities forced by U or J.

## 3. Complete contact and inverse on occupied inputs

Let s=eta(q,r) and a_s=S s. With the native state held unchanged during C,
the contact on the classical wave and signed work ledger is

    C:(u,v,w) -> (u,v+a_s,w+E_D(u,v+a_s)-E_D(u,v)).

The two tapes and pointer are unchanged. For arbitrary occupied wave,
tapes, pointer, native receiver and rational ledger, its inverse is

    v=v'-a_s,
    w=w'-E_D(u,v')+E_D(u,v'-a_s).

Substitution proves both compositions are the identity on the whole declared
product. This uses the retained native receiver to recover a_s. No zero or
prepared-memory premise is needed for the contact inverse. A controller that
changes or discards that receiver while applying C would be a different map.

Since the contact starts here from u=v=0, both tapes zero and pointer zero,
its ACTUAL output is

    X0(E(p))=((0,S E(p)),(0,0),(0,0),0),
    w=E0(p):=E_D(0,S E(p)).

The source-shaped wave was written by the specified translations into the
common blank receiver. This is a constructive conditional transition, not
an assertion that an unimplemented native or physical device executes it.

## 4. Both cuts obtained from the continuing wave

Use the original finite set D, principal Dirichlet L_D and marked insertion P.
To avoid overloading the work register w, call the two new wave slices v1,v2.
Put H=2I-L_D, Dg=I+PP^T and z=E(p). The unchanged cold coupler gives

    v1=Dg^-1 H S z,
    b0=-(1/2) P^T v1,
    v2=Dg^-1 [H v1-(I-PP^T) S z],
    b1=-(1/2) P^T(v2-S z).

Thus v2 is computed from the ACTUAL v1 and the remaining Sz, including loading
of all four ports. There is no second source preparation. The finite causal
domain D covers both steps, as established in lane O of the parent package.

Substitution of the unchanged response matrices yields the following exact
signed outputs. Each entry is a four-component integer numerator with the
column's common positive denominator; no rounding is used.

| h | 12960 b0 | 1399680 b1 |
|---|---|---|
| 0 | (0,0,0,0) | (0,0,0,0) |
| 1 | (-1421,354,354,348) | (192202,-47829,-47829,-48879) |
| 2 | (-1072,-1062,708,696) | (143434,145312,-95658,-97758) |
| 3 | (-2493,-708,1062,1044) | (335636,97483,-143487,-146637) |
| 4 | (698,-2832,708,696) | (-97536,386282,-95658,-97758) |

For example the h=3 row is the sum of twice the first and once the second
matrix columns at the shared half-amplitude scale. These entries follow
from b0=-M z/4 and b1=R1 z, which were themselves obtained from the complete
coupler above. The equality b1=-4 R1 M^-1 b0 is a consequence, not the way
the second output was produced. The five first outputs are distinct.

## 5. Full stage-by-stage state, including source and control

Let the complete declared mathematical state be

    Z=((n,x),X,w,(program,stage)),
    program=(U,C,U x F,U x F,STOP).

The program is the same fixed external schedule for every input. Its stages
are labels of a finite run, not a globally bijective free-running counter.
The classical pointer is part of X and is distinct from this stage counter.
At the five successive boundaries the state is exactly

    Z_init=((0,x0),X_blank,0,(program,0)),
    Z_native=((1,x1),X_blank,0,(program,1)),
    Z_source=((1,x1),((0,Sz),(0,0),(0,0),0),E0,(program,2)),
    Z_cut0=((2,x2),((Sz,v1),(0,0),(b0,0),1),E0,(program,3)),
    Z_cut1=((3,x3),((v1,v2),(0,0),(b1,b0),0),E0,(program,4)).

No native coordinate, old wave slice needed by the state, tape entry or
controller state is omitted in this product. The recorded native x3 is the
one generated by the three literal U ticks above. There is no additional
bit provider: theta is evaluated at the retained original n. Since the
transducer is disconnected after stage 2, x2 and x3 cannot rewrite the wave.

The outgoing tape itself is the retained record. Its physical order is
(b1,b0), and the chronological reader returns (b0,b1). If an independently
readable extra archive or sensor is later added, it enlarges the boundary;
no such copying operation is claimed here. Pointer return to zero does not
empty the outgoing tape. Stopping is supplied once at stage 4; renewal is open.

On these preparations the wave/port balance gives

    E_D(v1,v2)+2||b0||^2+2||b1||^2=E0=w.

The old outgoing deposits are internal retained tape energy, not also an
external outgoing flux. The active contact's E0 is the input work for this
declared classical boundary. The native system has supplied the signal that
controls this work, not a demonstrated physical energy source.

## 6. What is and is not invertible

C and F have complete inverses on their respective arbitrary occupied
carriers. The whole specified run also has an inverse ON ITS PREPARED IMAGE:

1. Recover z=-4 M^-1 b0 from the retained first output. Use the five-vector
   table to recover h; an output outside that table is outside the image.
2. Use that h to select the fixed (j0,j1,j2) and recover
   x0=g_j0 g_j1 g_j2 x3, applying j2 first. Each g_j is an involution.
3. Recover x1=g_j0 x0. Apply F^-1 twice to the complete classical endpoint,
   then C^-1 with this x1 receiver and the retained work ledger.
4. For image recognition first require endpoint n=3, stage=4 and the fixed
   program. Require the recovered x0 receiver (0,1), sum of its four pistons
   equal to the decoded h, origin zero, X_blank, work zero and the initial
   stage/program. The sum check guarantees that the recovered input really
   selects the branch word used in the inverse. These conditions characterize
   the prescribed prepared image; native and classical endpoints from
   inconsistent source classes must be rejected.

Thus all 625 full prepared inputs remain distinguishable in the COMPLETE
endpoint even though the classical observation intentionally keeps only h.
This is a proof on the specified image, not a census.

There is no inference that the full selector-defined U is bijective on every
F5^6 checkpoint or that STOP has a global permutation inverse. Generator
involutions do not prove either statement. No growing log is discarded, and
no claim is made to a universally reversible native/classical autonomous
machine. Such a claim would require a new complete occupied-controller model.

## 7. Admission boundary and the negative result for N0

In N0 every elementary operation acts on one factor alone, and all scheduling
is source-independent. Starting with a common classical state, induction over
the schedule proves that the classical state is independent of p at every
stage. For X_blank and the homogeneous F it stays exactly zero. Allowing a
fixed source-independent classical drive would still give the same output
for every p. Since h is nonconstant, no N0 construction realizes its five
distinctions in the classical record.

This proves an obstruction only for the explicitly factor-separated class.
It does not classify all possible native couplings, nonlinear contacts or
physical implementations. NC escapes precisely by adding C, which reads
the actual native receiver and writes classical amplitudes.

The balanced lift eta is not an additive homomorphism F5^2 -> Q^4. Indeed
any such additive homomorphism A obeys 5A(x)=A(5x)=A(0)=0 and is therefore
zero. A field-linear interpretation of the present nonconstant contact
would be false. The controlled lift and common bias are substantive extra
structure, even though their formulas are finite and exact.

Established: actual U delivers the five-valued signal; one explicit mixed
contact has common readiness, exact signed two-cut responses, complete
prepared state accounting, and the stated inverses and classical work law.

Not established: a compilation/admission of C from the accepted native
operations; a material converter, finite positive work store, contact/clock
realization or independent source qualification. The signed work register is
not such a store. Native/controller/sensor/reset physical energies cannot be
set to zero by omission. Physical status remains NOT_READY. The original 9/24
S/I/V qualification remains separate, and B certifies neither this contact
nor its energy or time interpretation.
