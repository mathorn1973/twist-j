# Two uses on one occupied apparatus

**NON-CANONICAL / conditional candidate-T / L1 analytical proof.**
Original work Apache-2.0, A. M. Thorn, 2026-10-14. A2 #1499.
Contract pin: d3c147ae853dfede1e956d978b66e7f9d0e489d7.
All four initial files were fetched from GitHub and byte-compared before
this proof. AUTHORED_PROOF; SELF_REVIEWED; A4_REVISION_PENDING_REVIEW.
This outcome-exposed correction addresses the A4 review of the original
result abc7e65812ca0e32b77a07592f1f94900d432c89; see RESULT for the erratum
and review links. No scientific program was run. Historical source results
and the linked review/interface findings are exposed.

## 1. Claims, definitions and inherited boundary

For the exact frozen eight-phase model we prove: a full-product permutation
of its static-source apparatus; an actual shared-counter native two-use
extension with initialized-image inversion for every pair of full inputs;
a direct four-vector signed reader retaining the first pair throughout the
second use; the full cross-use law; and an explicit reachable occupied-archive
counterexample to universal clean renewal by this same table.
None asserts native compilation or physical realization.

Use S,P,L,H,K,J0,X,W,d,c from CONTRACT without changes. In particular,

    K=I-PP^T/2, P^T K=P^T/2, K P=P/2,
    K J0=J0, P^T J0=0.                                  (1)

These follow from P^T P=I. The old R proof gives 0<L<=16I/9 for the
principal Dirichlet boundary. With m=(u+v)/2 and e=(v-u)/2,

    E_D(u,v)=[m^T L m+e^T(4I-L)e]/2,

which is positive definite. These inherited identities fix the selected
energy; they are not new public claims. D remains fixed throughout four cuts.
The old infinite-lattice comparison remains a two-cut statement only.

## 2. Total elementary inverses and the apparatus permutation

For Couple((u,v),a)=((v,w),b), the inverse on arbitrary ((v,w),b) is

    u=K(Hv-J0w+4P b),
    a=b+P^T(w-u)/2.                                     (2)

Substituting the second equation into
(I+PP^T)w=Hv-J0u+4Pa gives
(I+PP^T)u=Hv-J0w+4Pb. The rearrangement is reversible. Hence

    F^-1((v,w),(alpha0,alpha1),(beta0,beta1),k')
      =((u,v),(a,alpha0),(beta1,alpha1),k'-1),            (3)

where (2) uses b=beta0. This recovers every old tape entry and both wave
slices; both inverse compositions hold on the entire occupied product.

Symmetry of L gives

    E_D(v,w)-E_D(u,v)
      =(w-u)^T(w+u-Hv)/2
      =2||a||^2-2||b||^2.

The other three tape entries are permuted, so F preserves E_full.

For retained label r put f_r=S eta(r). The contact inverse is

    v=v'-f_r,
    W=W'-E_D(u,v')+E_D(u,v'-f_r),                       (4)

with u, tapes, k and r unchanged. It is total on the rational carrier;
W is unrestricted signed work, not a battery. The occupied-buffer addition
d'=d+r_B has inverse d=d'-r_B in F5^2.

For the static-source apparatus version hold r_A,r_B fixed. Its row maps
T_c are: identity for c=0,7; F for c=2,3,5,6; C_rA together with
d+=r_B for c=1; and C_d for c=4. Each is a permutation by (2)-(4).
The two operations in row 1 commute because neither uses the changed d.
Row 4 retains d, so the inverse uses the same label. Therefore

    G(a,c)=(T_c(a),c+1 mod8),
    G^-1(a',c')=(T_(c'-1)^-1(a'),c'-1 mod8)             (5)

are mutual inverses on the entire apparatus product. This is an explicit
complete map, not a generic reversible-simulation claim or a history tape.

The native coupled map is total but (5) is not its inverse. In fact a
state n=0,c=1 has no predecessor: phase 0 always increments n. Thus that
full N0 product is not onto. Section 7 supplies only its ready-image inverse.
The T3 projection obstruction is respected: arbitrary incoming A0 changes
the F wave by 4KP A0=2P A0, so a cold projection is not imposed on every
helper state; the nonsurjective native update is not called a permutation.

## 3. Five actual native ticks, with paid-for delayed signal

The unchanged generators on x=(a,b,c0,d0,q,r), in F5, are

    g0 x=(b,a,d0,c0,q,r),
    g1 x=(-c0,-d0,-a,-b,-q,-r),
    g2 x=(2-c0,1+r-d0,2-a,1-r-b,1-q,-r),
    g3 x=(2-a,1-b,3-c0,4-d0,1-q,1-r),
    g4 x=(2-a,1-b,3-c0,4-d0,2-q,1-r).

They are involutions. Their complete-sum actions are
(z,-z,2-z,2-z,3-z), respectively. The canonical first-three-tick
table for x0=(p,0,1), h=sum(p), is

| h | (j0,j1,j2) | C1 | C2 | C3 |
|---|---|---|---|---|
| 0 | (1,1,3) | (0,4) | (0,1) | (1,0) |
| 1 | (2,2,4) | (1,4) | (0,1) | (2,0) |
| 2 | (3,1,3) | (1,0) | (4,0) | (2,1) |
| 3 | (4,1,3) | (2,0) | (3,0) | (3,1) |
| 4 | (0,2,4) | (0,1) | (1,4) | (1,2) |

Each row applies to all 125 p in its sum class, with the complete states
x1=g_j0 x0, x2=g_j1 x1, x3=g_j2 x2. Every row has sum(x3)=1.
Now theta_3=0, so j3=1 and sum(x4)=4; theta_4=1, so j4=4+2=1 mod5.
Consequently

    x4=g1 x3, x5=g1 g1 x3=x3.                          (6)

The counter has advanced to 5, not returned to 3. This same derivation
applies independently to both heads with their one common n.

At phase 1, n=1 and initial d=0, so d becomes rec(x1_B). Contact A reads
rec(x1_A). At phase 4, n=3 and the actual B head is x3_B; contact B
deliberately reads the retained d, not that different current receiver.
Thus z_A=eta(rec(x1_A)) and z_B=eta(rec(x1_B)) have exactly the five
frozen values and all 25 ordered signal pairs are realized.

The extra F5^2 register and controlled addition are explicit resources.
No source sum was preloaded into the apparatus. No finite Thue-Morse
generator, five-context updater, 23-state reader or unspecified next-bit
oracle is used. Exact theta is evaluated on the retained actual native n.

## 4. Complete continuing state and both new cuts

Write f=S z_A, g=S z_B and T=KH. On the frozen ready family define

    w1=T f,
    w2=T w1-J0 f,
    w3=T(w2+g)-J0 w1+2P c1,
    w4=T w3-J0(w2+g)+2P c0.                            (7)

These are four successive actual Couple updates. Contact B adds g only
to the current slot after cut 1. The chronological signed vectors are

    b0=-P^T w1/2,
    b1=P^T(f-w2)/2,
    b2=c1+P^T(w1-w3)/2,
    b3=c0+P^T(w2+g-w4)/2.                             (8)

No second vector is synthesized from a previous output. The complete
classical state, for every rational c0,c1, is

| Boundary | wave (u,v) | A | B | k |
|---|---|---|---|---|
| initial / after V | (0,0) | (0,0) | (c0,c1) | 0 |
| after contact A | (0,f) | (0,0) | (c0,c1) | 0 |
| after cut 0 | (f,w1) | (0,c1) | (b0,c0) | 1 |
| after cut 1 | (w1,w2) | (c1,c0) | (b1,b0) | 0 |
| after contact B | (w1,w2+g) | (c1,c0) | (b1,b0) | 0 |
| after cut 2 | (w2+g,w3) | (c0,b0) | (b2,b1) | 1 |
| after cut 3 | (w3,w4) | (b0,b1) | (b3,b2) | 0 |

Set E_A=E_D(0,f), Delta_B=E_D(w1,w2+g)-E_D(w1,w2).
The other coordinates at the same boundaries are

| c | n | native pair | d | W | completed cuts |
|---|---|---|---|---|---|
| 0 | 0 | (x0_A,x0_B) | 0 | 0 | none |
| 1 | 1 | (x1_A,x1_B) | 0 | 0 | none |
| 2 | 1 | (x1_A,x1_B) | C1_B | E_A | none |
| 3 | 2 | (x2_A,x2_B) | C1_B | E_A | 0 |
| 4 | 3 | (x3_A,x3_B) | C1_B | E_A | 0,1 |
| 5 | 3 | (x3_A,x3_B) | C1_B | E_A+Delta_B | 0,1 |
| 6 | 4 | (x4_A,x4_B) | C1_B | E_A+Delta_B | 0,1,2 |
| 7 | 5 | (x5_A,x5_B) | C1_B | E_A+Delta_B | 0,1,2,3 |

These two tables specify every coordinate. The first source's (n,X)
projection through c=4 is exactly the old U,C_*,U x F,U x F prefix,
including its allowed occupied old B. The second head and delayed capture
are disclosed extensions. The old external STOP is replaced by a total
next row, not treated as a reversible absorbing operation.

## 5. All cross-use terms and direct archive access

Separate the lingering A wave:

    a3=T w2-J0 w1, a4=T a3-J0 w2,
    D2(z_A)=P^T(w1-a3)/2, D3(z_A)=P^T(w2-a4)/2.

Use the inherited cold maps and marked port matrix

    R0 z=-P^T T S z/2,
    R1 z=P^T[S z-(T^2-J0)S z]/2,
    Jp=P^T H P=(59I+11^T)/54.

Substitution in (7)-(8) gives

    w3=a3+Tg+2P c1,
    w4=a4+(T^2-J0)g+2T P c1+2P c0,                    (9)

    b0=R0 z_A, b1=R1 z_A,
    b2=D2(z_A)+R0 z_B,
    b3=D3(z_A)+R1 z_B-(Jp/2)c1.                      (10)

In detail, the explicit incoming archive terms in (8) cancel as follows:

    b2=c1+P^T(w1-a3-Tg-2P c1)/2
      =D2(z_A)+R0 z_B+(I-P^T P)c1
      =D2(z_A)+R0 z_B,
    b3=c0+P^T(w2+g-a4-(T^2-J0)g-2T P c1-2P c0)/2
      =D3(z_A)+R1 z_B-P^T T P c1+(I-P^T P)c0
      =D3(z_A)+R1 z_B-(Jp/2)c1.

Here P^T P=I and P^T T P=P^T K H P=Jp/2. Thus c0 drops out of
all four outputs, while c1 remains in b3 through the continuing wave.
The complete wave in (9) still depends on both archives. These formulas give
all dependencies on both sources and the old archives, on fixed D. They hold for all
25 signal pairs and all rational c0,c1, including the fully blank first
subfamily. They are algebraic identities, not a finite trajectory census.

For completely arbitrary off-ready wave and incoming tapes, the total
four-cut formula remains explicit: apply C_A to (u,v); apply Couple
twice with the original A0,A1; add g to the current wave; apply Couple
with the original B1,B0. The complete F slot permutations give final
A=(b0,b1), B=(b3,b2), and the complete reversed formula uses (3)-(4).
Cold response matrices are not asserted for an arbitrary initial wave.

On the first initialized period the direct chronological reader is

| completed cuts | literal reader |
|---|---|
| none | UNWRITTEN |
| 0 | (B0) |
| 0,1 | (B1,B0) |
| 0,1,2 | (A1,B1,B0) |
| 0,1,2,3 | (A0,A1,B1,B0) |

The n,c boundaries identify the valid row. Every returned vector is tagged
PRESENT with its (use,cut) identity, including a zero vector. At c=4,5 the
first pair is (B1,B0); at c=6 it is (A1,B1); at c=7 it is (A0,A1).
Thus it remains literally readable while the second record is made.
There is no inverse simulation, copied output or additional archive.

UNWRITTEN versus PRESENT(0) belongs to this typed reader on the retained
temporal state; no sixth signal value is appended to F5. Old nonzero
amplitudes alone do not certify a new occurrence.

Across the entire frozen common-ready family, including arbitrary UNKNOWN
rational c0,c1, the record distinguishes all 25 signal pairs.
The old R0=-M/4 is invertible, with

    M=(1770I-v 1^T)/1620, v=(349,354,354,348)^T,
    1^T v=1405, M^-1=(54/59)(I+v 1^T/365).

The source-label decoder is

    z_A=R0^-1 b0,
    z_B=R0^-1(b2-D2(z_A)).

Indeed b0=R0 z_A fixes z_A uniquely, then (10) fixes z_B uniquely.
Neither c0 nor c1 occurs in these equations or is supplied to the decoder.
The five z values are distinct, so equal records even from different old
archives force the same ordered signal pair. This is archive-independent
source recovery, not archive independence of the whole record: b3 still
depends on c1. It also does not recover all four residues of either native
input. Section 7 recovers those full inputs using the retained native heads.

## 6. Reachable WARM witness and exact cold comparison

Choose p_A=(0,0,0,0), p_B=(1,0,0,0), c0=0,c1=e0, and all other
common-ready values as in CONTRACT. This is an initially occupied old
archive with selected energy 2, explicitly not a fully blank apparatus.
Both uses are actual and their signal values are different: 0 then 1.

Here z_A=0, so the first wave and both first outputs are zero. After the
actual first two F calls, the COMPLETE boundary state is

    n=3, c=4, W=0, d=(1,4),
    x_A=(2,1,3,4,1,0), x_B=(1,1,3,4,2,0),
    X=((0,0),(e0,0),(0,0),0).                          (11)

The native entries follow from the words in Section 3. The nonzero
incoming A0=e0 was transported from the initial old B1 by the actual
first trial; it is not an arbitrary manufactured intermediate state.
The two zero outputs are recorded occurrences.

At contact B the actual native receiver is C3_B=(2,0), while the retained
label is d=C1_B=(1,4). The declared contact reads the latter, giving

    z_B=e0/2,
    g=(2/5)delta_y0-(1/10)(delta_y1+delta_y2+delta_y3+delta_y4).

Its work is 1/10. The next actual two cuts give

    w3=Tg+2P e0, w4=(T^2-J0)g+2T P e0,
    b2=R0(e0/2), b3=R1(e0/2)-(Jp/2)e0.                (12)

Together with the finite stencil definition of T these are exact rational
formulas for EVERY wave coordinate. The final complete state is
X=((w3,w4),(0,0),(b3,b2),0), n=5,c=7,W=1/10,d=(1,4), with both
native heads equal to their x3 values in (11) by (6).

The inherited cold signed vectors for e0/2 are

    cold0=(-1421,354,354,348)/12960,
    cold1=(192202,-47829,-47829,-48879)/1399680.

The actual second signed record is exactly

    b2=(-1421,354,354,348)/12960,
    b3=(-585398,-60789,-60789,-61839)/1399680.            (13)

The cold comparator starts wave and all four tape slots blank, loads
the same g, and applies F twice. Its outputs are cold0,cold1. Therefore

    b2-cold0=(0,0,0,0),
    b3-cold1=(-5/9,-1/108,-1/108,-1/108).               (14)

This follows since Jp has diagonal 10/9 and off-diagonal 1/54.
In the common denominator, 1399680*(5/9)=777600 and
1399680/108=12960, yielding (13) by subtraction. No program executed
these scientific values; they are manual exact consequences of (12).

At contact B the only causal difference from the cold comparator is
the inherited incoming e0: both waves before insertion are zero.
The direct incoming contribution cancels in the first B output; its
continued wave produces the nonzero second difference in (14). This is a
rational amplitude effect, not a clock bit or occupancy flag. This witness
was reached by the first trial. The second B cut alone rejects universal
clean renewal over the frozen family. It neither claims a fully blank
first-use witness nor excludes other renewal mechanisms.
Equations (9)-(10) separately cover a fully blank first apparatus without
silently identifying its continuation with a cold second trial.

## 7. All-full-input inverse and exact ready-image recognition

Let Phi be the seven updates from c=0 to c=7 on a fixed ready family
R_(c0,c1). Its input domain is every pair in F5^4 x F5^4.
At n=5 each native head equals x3. The five distinct C3 receivers identify
h_A,h_B uniquely, without using the classical record. For each head,

    x0=g_j0 g_j1 g_j2 x5, x1=g_j0 x0,                 (15)

where the rightmost g_j2 is applied first. These are inverse words by
involution and (6). This preserves each full four-coordinate source;
there are 625^2 pairs, and no finite enumeration is used to infer the claim.

For any candidate complete endpoint the following finite exact tests
recognize the image and recover its unique initial state:

1. Require n=5,c=7 and each receiver in the C3 column. Decode its h and
   reconstruct (15). Require the reconstructed x0 receiver (0,1) AND
   the reconstructed piston sum equal to that h. Inverse words alone
   without this selector-consistency test are insufficient.
2. Reconstruct x1_A,x1_B and require d=rec(x1_B).
3. Undo F twice, then C_d, then F twice, then C_rec(x1_A), retaining
   and reversing W at the contacts. Subtract rec(x1_B) from d.
4. Require recovered wave and A slots zero, B=(c0,c1), k=0,W=0,d=0.
   The native/phase table restores the unique initial n=0,c=0.

Necessity is the forward tables and the elementary inverses. Conversely,
passing the tests supplies a common-ready source pair with the correct
piston sums. Those sums force the recorded first-three selector words;
the last two are g1,g1 by Section 3. Reapply the contact/F/buffer maps:
their two-sided inverses give exactly the proposed endpoint. Thus the
tests are sufficient, not just necessary. The same recipe recognizes the
union over c0,c1 by retaining the recovered B pair rather than comparing
it to one prescribed pair. All old archive information is recovered.

This is a left inverse on the initialized image, not a global inverse
for selector-defined U or a two-sided N0 evolution.

## 8. Exact work and complete resource stock

The selected classical boundary invariant is E_full-W: F preserves
E_full, each contact increments W by the exact change, and the remaining
rows do not change these boundary variables. This does not assign zero
physical energy to native, buffer or controller degrees of freedom.

Expanding the second contact energy gives

    E_A=||f||^2/2,
    Delta_B=||g||^2/2+g^T(w2-Hw1/2),
    W_final=E_A+Delta_B,                               (16)

and at every stage

    E_full-W=2(||c0||^2+||c1||^2).                      (17)

The mixed term in (16) is the occupied-wave correction; cold work
||g||^2/2 cannot simply be reused. Its sign is not assumed positive.
Old B does not enter the wave before contact B, so it affects (9)-(10)
but not this contact work. For the witness the initial tape energy is 2;
contact A has zero work and the first two F calls preserve that energy.
At contact B the wave is zero and

    Delta_B=[(2/5)^2+4(1/10)^2]/2=1/10.

The last two F calls preserve the resulting energy, so for the corrected
complete endpoint in (12)-(13),

    E_D(w3,w4)+2(||b3||^2+||b2||^2)=E_full_final=21/10,
    W_final=1/10, E_full_final-W_final=2.

The b2 in this identity is cold0, not cold0-e0; the historical incorrectly
printed tape entry did not describe that endpoint. Retained tape energy
is counted once, not again as exported heat.

The complete stock, present from the beginning, is: two six-residue native
heads, their one retained integer n, two rational D-vectors, four rational
four-vector tape entries, the two-state k, 25-state d, eight-state c,
rational W and the fixed program law. The tables in Section 4 specify every
stock after every stage. No slot, sign, old record, source or clock is
discarded. After consumption, c0,c1 remain invertibly encoded in the
complete state; they need not remain direct old-archive slots. The promised
new first-use record does remain a literal pair through completion.

Finite program size and slot count do not imply a finite-bit machine:
n is unbounded and Q has unbounded numerators/denominators. Bounded rational
energy does not imply a finite alphabet. No precision bound, arbitrary-N
family or unlimited direct-record capacity is claimed.

Completion is n=5,c=7, not a frozen terminal state. The next row holds data
and rotates c to 0. A later period uses the actually occupied d and tapes,
continues n from 5 and adds to d rather than clearing it. Its first F
consumes the old b0 in A0 as an incoming amplitude. Thus the first run's
direct four-slot archive is not permanent, although appropriate complete
inverse access retains its information. The theorem guarantees two uses,
not a repeatable clean device or indefinite frozen dynamics.

## 9. Contact export and unpassed bridges

CONTRACT Section 7 is the exported signature: retained F5^2 label and eta,
exact translated wave, unchanged tape coordinates, full resource and
success/refusal/direction state, exact inverse domain and the actual
occupied-state Delta. The literal events are contact A reading C1_A at n=1
and contact B reading retained d=C1_B at actual n=3. The current C3_B
receiver and a prospective current-C2 intervention at n=2 are different
inputs. For p_B=e0, eta(d)=e0/2 whereas eta(C3_B)=e0+e1/2; for h_B=0,
eta(C1_B)=0 whereas eta(C2_B)=e1. Our d is an F5^2 delayed-label register,
distinct from the rational ancilla called d in the A1 interface review.

The linked common A4 review supplies an exact obstruction to direct H_B
substitution even if a delayed-label adapter is granted: start with the
fully blank apparatus, p_A=0,p_B=e0, b=B=2/5 and sigma=+1. The accepted
zero-source first call leaves the wave and store unchanged but flips sigma
to -1. The two F calls leave the blank wave/tapes zero. The second call
has cost 1/10 for either sign and is accepted (b becomes 3/10), but inserts
-S(e0/2) where this table requires +S(e0/2). Its signed response differs
because R0(e0/2) is nonzero. Thus leaving the same direction register to
the two H_B calls does not realize two positive contacts. This blank
composition example is separate from the occupied-archive WARM witness.

A future funded contact needs a separately specified reversible label
adapter and direction rule, with their complete/initialized domains. Its
actual trajectory must satisfy BOTH store bounds

    0 <= b_init-E_A <= B,
    0 <= b_init-E_A-Delta_B <= B,

using the true mixed term (16), not just cold source energies. Success,
refusal and direction must be retained and exposed separately. PRESENT(0)
certifies an acquired cut, not funded acceptance; rejected contacts cannot
be counted as successful source uses. No such composition is constructed here.

Those are requirements on a future component, not a proof of an H_B
two-use budget or native admission. The reference model has no rejected
branch because its signed-work contact is total; it does not silently
throw away a failed battery contact.

Native compilation of C and buffer writing, physical source acquisition,
finite nonnegative funding, full control/sensor/record energy, material
renewal, SI clock, independent qualification, occurrence and L2-L6 bridges
remain UNSUPPLIED. Removing the delayed capture changes the contract and
leaves the second native timing interface unsupplied.
QUADRATIC-MEMORY-NATIVE-CONTACT and QDD-INSTRUMENT-APPARATUS stay open.
The constructive and scoped negative statements here are candidate claims,
not a Canon promotion or a proof about every physical apparatus.
