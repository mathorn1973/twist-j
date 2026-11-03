# Exact bank copying and finite reuse of one working apparatus

**NON-CANONICAL / L1.** Proposed mathematical proof for
P-RELATIVE-CONTACT-WORKBANK-REUSE-1. The symbolic statements below are
candidate theorems, pending the applicable review. This file asserts no
completed scientific execution, independent external acceptance, Canon
promotion or shortest-word result.

The local copy word was supplied after its discovery and prior results were
known. Its use here is an exposed-witness reconstruction, not a blind
discovery. The new composition and its complete resource contract are proved
below. A later finite audit must execute the pinned primitive words on the
complete new carrier; it must not substitute the displayed endpoints.

All products act in chronological order from left to right. Except in the
explicitly one-based six-place module, addresses are zero based.

## 1. Ring, contact and complete invariants

Let O=Z[j], where j is a primitive fifth root of unity, and put

    rho=j^2, u_e=1-rho^e, w_e=1+rho^e,
    u=u_1, w=w_1, b=w_2=1+rho^2.

Subscripts on u_e and w_e are modulo five. In particular u_0=0 and w_0=2.
Write z=sum(i=0..3) z_i j^i and define

    Q(z)=(5*sum_i z_i^2-(sum_i z_i)^2)/2,
    epsilon(z)=sum_i z_i mod 5.

For a complete state x, let E(x)=sum_i Q(x_i),
Sigma(x)=sum_i x_i and H(x)=sum_i x_i*conjugate(x_i). Here Q is the
positive half-trace of z*conjugate(z). It is integral because its numerator
is even modulo two, and positive definite because
(sum_i z_i)^2<=4*sum_i z_i^2.

The total contact is

    C(a,c)=(a,c)                                  if a-c is not in 2O,
    C(a,c)=(s+rho*d,s-rho*d),
        s=(a+c)/2, d=(a-c)/2                     if a-c is in 2O.

On the admitted branch s,d are integral and the output difference is
2*rho*d, so admission persists. Since rho^5=1, C^5=id and C^-1=C^4 on
the complete pair carrier. Equal entries are fixed even though admitted;
we do not assert that every admitted state has least period five. A refused
pair is fixed. Every finite contact word is therefore a global bijection.

The sum is unchanged. Since rho*conjugate(rho)=1,

    (s+rho*d)*conjugate(s+rho*d)
      +(s-rho*d)*conjugate(s-rho*d)
    =2*s*conjugate(s)+2*d*conjugate(d).

Thus H and E are preserved. The map epsilon is the ring map j->1.
Each labelled slot changes by a multiple of rho-1, so its epsilon is
preserved. A supplied whole-slot SWAP is separately an involution and
preserves complete Sigma, H and E; in general it permutes labelled residues.

Multiplication of the complete state by rho commutes with each contact.
Indeed rho is an integral unit, so it preserves the admission condition;
the admitted formula is linear and the refused formula is identity. This
equivariance will be used in section 4.

Modulo two, Phi_5(X)=X^4+X^3+X^2+X+1 is irreducible: it has no linear
root over F_2 and is not divisible by the only irreducible quadratic
X^2+X+1. Hence O/2O is F_16, the image of rho has order five, and
1+rho^e is nonzero modulo two for e=1,2,3,4. In particular b is nonzero
modulo two. This suffices for the phase decisions below; no search table is
a premise.

## 2. Bank code and the twelve-contact local identity

The fresh ten-slot bank and its five valid present records are

    M_empty=(-b,b)^5,
    M[p]=M_empty with only pair p replaced by (-rho*b,rho*b),
        p in Z/5.

Pairs are labelled and each pair is ordered negative entry first. Directly
b=(0,-1,-1,-1) in the j basis, so Q(b)=3. Multiplication by rho preserves
Q and H. Every fresh or valid recorded bank therefore has E=30 and sum
zero, with labelled residue vector (3,2)^5. The five present records are
distinct, since b!=0 and rho!=1, and none equals M_empty. A present record
labelled zero is not an empty bank.

For opposite signed entries (-rho^P*b,+rho^Q*b), the contact is admitted
exactly when P=Q modulo five. The difference is
-b*(rho^P+rho^Q); in F_16 this vanishes exactly when the two phases agree.
If admitted, the pair has center zero and both phases increment by one.
The same increment rule holds when the positive entry is listed first.

Use six local places, numbered 1 through 6:

    1,2: source pair p; 3,4: source pair q; 5,6: fresh target pair p.

Only places 1,4,5,6 occur in the following word:

    W6=C14 C14 C45 C14 C14 C14 C16 C16 C16 C16 C14 C16.
    A=C14, B=C45, D=C16, so W6=A^2 B A^3 D^4 A D.

Let (P,Q,R,S) be the phases at these four places. Their signs are
(-,+,-,+). A increments P,Q when equal, B increments Q,R when equal,
and D increments P,S when equal. All other applications refuse.

The complete block-boundary calculation is:

| Initial (P,Q,R,S) | A^2 | B | A^3 | D^4 | A | D |
| --- | --- | --- | --- | --- | --- | --- |
| (0,0,0,0) | (2,2,0,0) | (2,2,0,0) | (0,0,0,0) | (4,0,0,4) | (4,0,0,4) | (0,0,0,0) |
| (1,0,0,0) | (1,0,0,0) | (1,1,1,0) | (4,4,1,0) | (4,4,1,0) | (0,0,1,0) | (1,0,1,1) |
| (0,1,0,0) | (0,1,0,0) | (0,1,0,0) | (0,1,0,0) | (4,1,0,4) | (4,1,0,4) | (0,1,0,0) |

The numbers of admitted contacts in these rows are respectively
10, 6 and 5. Their admission words, with A meaning admitted and R refused,
are respectively

    AARAAAAAAARA, RRAAAARRRRAA, RRRRRRAAAARA.

Thus a mark at p is copied to the target pair; a mark at q or elsewhere
leaves that target fresh. Both complete source pairs are restored, because
places 2 and 3 never change and places 1 and 4 regain their input values.
The restoration holds at the twelve-contact boundary, not at every
intermediate contact. Intermediate source pairs need not themselves have
the balanced bank-pair form.

The fresh-target hypothesis is essential to this local lemma. For example,
the same phase rules give

    (0,0,1,1)
      ->(2,2,1,1)->(2,2,1,1)->(0,0,1,1)
      ->(0,0,1,1)->(1,1,1,1)->(2,1,1,2).

This is a boundary counterexample to extending the local table to arbitrary
occupied targets. It is not a classification of all occupied global words.

## 3. A common sixty-contact bank copier

For a source bank at base a and a target bank at base d, define K(a,d)
by concatenating W6 for p=0,1,2,3,4, with q=p+1 modulo five and the
one-based local places relabelled as

    (1,2,3,4,5,6)
      ->(a+2p,a+2p+1,a+2q,a+2q+1,d+2p,d+2p+1).

Source and target banks are disjoint. This specifies every edge and its
order without an input-dependent choice.

Suppose the source is M[r] and the target M_empty. At module p there are
exactly the three possibilities in section 2: r=p, r=q, or r is elsewhere.
The source is restored at each module boundary, so this same classification
remains valid for the next module. No earlier target pair is touched again.
Induction over the five modules gives

    K(a,d): (M[r],M_empty) -> (M[r],M[r])     for every r in Z/5.

Exactly one module has p=r and exactly one has q=r. The total number of
admitted contacts is therefore 6+5+3*10=41 out of 60, independently of r.
These numbers follow from the local proof, not a runtime observation.

Global rho equivariance also proves every simultaneous rotation of these
identities. For t=0,1,2,3,4, multiply all six or all twenty coordinates
of a local or bank preparation by rho^t. The same literal word gives
rho^t times the complete original endpoint, with the identical admission
pattern. The rotated fresh bank is rho^t*M_empty, not an unrotated fresh
bank coupled to a rotated source. This corollary supplies the fifteen
local and twenty-five bank cases of the separate rotated finite audit.

This word uses only the twenty source and target coordinates. Its complete
initial and final account is 60 and sum zero; every primitive contact
preserves the complete accounts and labelled residues. The source bank
equals its initial M[r] at all five module boundaries. No primitive-level
source immutability or unrestricted occupied-target write is claimed.

The literal inverse reverses all sixty edges and replaces each contact by
four repetitions of that edge. It has 240 contacts and restores the entire
input on every complete carrier state, by section 1. In particular it
restores (M[r],M_empty) from the displayed copied pair. This is an inverse
construction, not an assertion that K is an involution. No shortest-word
or minimality claim is used.

## 4. Four-place literal copying is obstructed

This separate statement concerns only two pairs, with no extra reference
or changing auxiliary coordinate. Let b be any nonzero element of O and set

    E=(-b,b,-b,b),
    A=(-rho*b,rho*b,-b,b),
    T=(-rho*b,rho*b,-rho*b,rho*b)=rho*E.

There is no fixed word F of the total contacts on these four places
satisfying both F(E)=E and F(A)=T.

Indeed global rho equivariance gives F(T)=rho*F(E)=T. Bijectivity would
then imply A=T, contrary to b!=0 and rho!=1. This proves the obstruction
without an orbit enumeration. The hypothesis b!=0 excludes the trivial
all-zero exception.

The conclusion concerns literal copying with the stated empty-state action.
It does not prohibit a different output code, an additional reference pair,
or the twenty-place one-hot copier. For that copier the complete prepared
family is not closed under global multiplication by rho, and the unchanged
neighbour is part of the explicit source bank. Global equivariance remains
true; the hypotheses of this four-place contradiction no longer apply.

## 5. The complete thirty-one-slot read apparatus

We spell out the v108 read word and its relevant proof so that the new
composition has a definite input, complete output and inverse. These
definitions agree with the declared source WORD535; no recorded execution
of that word is a premise.

The ready core I(s,r), for s in {0,1} and r in Z/5, is

    I(s,r)=(Y_s,X_r,0,u,0,0,w,0,M_empty,M_empty),

with these addresses:

| Slots | Role |
| --- | --- |
| 0..2 | source Y_s |
| 3..4 | clock X_r |
| 5 | marker g=0 |
| 6..8 | selector (A,B,skip)=(u,0,0) |
| 9 | helper h=w |
| 10 | sampling gate t=0 |
| 11..20 | working bank A |
| 21..30 | working bank B |

Put

    F=C(0,1) C(1,2), T=C(3,4),
    Y_0=(0,2,0),
    Y_e=(u_e,w_e,0)             for e=1,2,3,4,
    Y_(4+e)=(0,w_e,u_e)         for e=1,2,3,4,
    X_r=(rho^r*w,-rho^r*w).

The source index is modulo nine. The contact rotates the relative pair
(u_e,w_e) to (u_(e+1),w_(e+1)). For e=1,2,3,4, contact of w_e with zero refuses
modulo two. At the turning point the pair becomes (0,2), allowing the next
source contact; at the final point it returns to Y_0. These facts give
F(Y_a)=Y_(a+1) for all nine displayed states. The zero-centered clock gives
T(X_r)=X_(r+1). All displayed source and clock states are distinct.

Define the following oriented blocks:

    O1=C(1,5), A0=C(5,9), Bc=C(c,9), O2=C(9,10),
    E_c=A0 Bc A0^4 Bc^4,
    E_c^-1=Bc A0 Bc^4 A0^4.

For memory base q=11 or 21, let a_p=q+2p and b_p=q+2p+1 and put

    L_p=C(3,a_p)^4 C(a_p,b_p)^4 C(3,a_p) C(a_p,b_p),
    SCAN_q=product_(p=0..4) (C(3,10) L_p C(3,10)^4 T),
    W_A=E_6 O2 SCAN_11 O2^4 E_6^-1,
    W_B=E_7 O2 SCAN_21 O2^4 E_7^-1,
    D(c,d)=C(9,c)^3 C(9,d)^3 C(9,c) C(9,d) C(9,c),
    V(c,d)=A0 D(c,d) A0^4 D(c,d),
    R=O1 W_A W_B V(7,8) V(6,7) O1^4,
    S=R F^-1 R F F T,
    F^-1=C(1,2)^4 C(0,1)^4.

The products over p use increasing order. In particular the final C(9,c)
in D is present. The lengths of L_p, SCAN_q, E_c, W_A, W_B, D, V, R
and S are respectively 10, 80, 10, 105, 105, 9, 23, 261 and 535.

Here are complete local reasons for the read action.

**Marker and sampling gate.** O1 takes (source middle,g)=(2,0) to (w,u)
at Y_0. At every other source phase it refuses, leaving g=0. With h=w
and g,c in {0,u}, E_c has the following boundary action:

| Initial (g,c,h) | Final (g,c,h) |
| --- | --- |
| (0,0,w) | (0,0,w) |
| (u,0,w) | (u,0,w) |
| (0,u,w) | (0,u,w) |
| (u,u,w) | (u,0,2) |

For the last row, A0 gives (u_2,u,w_2), Bc refuses, A0^4 restores
(u,u,w), and Bc^4 gives (u,0,2). For the second row the Bc contacts
refuse and the A0 powers cancel. For the third row the intermediate
(c,h)=(u_2,w_2) makes A0^4 refuse and the Bc powers cancel. The first
row consists of refusals. Consequently O2, with t=0, creates (h,t)=(w,u)
exactly in the last row; otherwise it refuses on (w,0).

**Scanning a bank.** In F_16, w^3=rho^4. The element w is not in
the subgroup generated by rho: w=rho^v would force v=3, whereas
1+rho=rho^3 together with Phi_5(rho)=0 would force rho^2=rho^4.
Also b=w^2 modulo two. Thus the cosets <rho>w and <rho>b are disjoint.

With t=u, C(3,10) on the raw clock rho^r*w is admitted exactly at r=0.
It then replaces (w,u) by (b,u_2). With t=0 it refuses at every r.
On a raw clock and a memory pair (-rho^v*b,rho^v*b), the two clock-to-
memory contacts in L_p refuse by the disjoint cosets. The memory fourth
power and final contact cancel, even for an occupied pair.

At a gated scan of a fresh pair, the triple (clock,a_p,b_p) follows

    (b,-b,b)
      ->(rho^4*b,-rho^4*b,b)
      ->(rho^4*b,-rho^4*b,b)
      ->(b,-b,b)
      ->(b,-rho*b,rho*b).

The second block refuses because (1+rho^4)*b is nonzero modulo two.
The inverse sampling contact restores (w,u). Every scan step advances
the raw clock by T, so five steps encounter phase zero exactly once, at
p=-r, and return the clock to its starting phase. A gated fresh bank
becomes M[-r]. An inactive scan preserves a fresh or valid occupied bank.
Already written pairs are not revisited in that scan.

After SCAN_q, O2^4 and E_c^-1 restore g,c,h,t exactly. Only the selected
fresh bank has changed.

**Selector.** With helper w, D exchanges (u,0) and (0,u) and fixes (0,0).
With helper w_2 it fixes all three. To verify the nontrivial first case,
the successive states starting at (h,c,d)=(w,u,0) are

    (w_4,u_4,0), (w_4,u_4,0), (2,0,0), (w,0,u), (w,0,u).

Starting at (w,0,u), the successive states are

    (w,0,u), (w_4,0,u_4), (w_4,0,u_4), (2,0,0), (w,u,0).

With helper w_2, its residue differs modulo two from both 0 and u, so all
contacts refuse. For g=0, both A0 blocks in V refuse and its two D
transpositions cancel. For g=u, A0 changes (g,h) to (u_2,w_2);
the first D fixes its targets, A0^4 restores (u,w), and the final D
exchanges them. Thus V swaps its admitted token pair exactly when g=u
and restores g,h. V(7,8)V(6,7) cycles A->B->skip->A at a marker event.
Finally O1^4 restores the source and g.

We have therefore proved that a complete R restores its presented source,
clock, g=t=0 and h=w. Away from source phase zero it changes neither
selector nor either valid bank. At source phase zero it writes M[-r]
only to a selected fresh A or B bank, preserving the other valid bank,
or preserves both at skip; it then cycles the selector. These claims
are on the stated reachable token and bank family, not arbitrary active
overwrites or arbitrary intermediate marker values.

**Ten-step stage.** At an S boundary with source/clock phases (a,r),
the first R sees a and the second sees a-1 after F^-1. The final F F T
leaves boundary phases (a+1,r+1). Starting at (s,r), step t starts at
(s+t mod9,r+t mod5). The exact event list during ten steps is:

| Initial s | Step and read | Selected actions |
| --- | --- | --- |
| 0 | (0,first), (1,second), (9,first) | A, B, skip |
| 1 | (0,second), (8,first), (9,second) | A, B, skip |

There is no fourth event. Put Delta_0=1 and Delta_1=8. The word
W=S^10 of 5350 contacts consequently gives the complete core identity

    W I(s,r)=
      (Y_(s+10),X_r,0,u,0,0,w,0,M[-r],M[-r-Delta_s]).

The working records persist at subsequent complete R and S boundaries of
this forward stage, but are not asserted constant inside reads. All six
controls are ready again. The literal W^-1 has 21400 contacts and restores
I(s,r) from precisely this complete occupied state.

## 6. One write, copy and uncompute cycle

Let H_A and H_B be two disjoint fresh archive banks outside the 31 core
coordinates. For their bases a and d, define

    U(a,d)=W K(11,a) K(21,d) W^-1.

The complete word has

    5350+60+60+21400=26870 contacts.

Apply section 5 to the initial ready core. Section 3 copies its two
actual present working records to H_A,H_B, restoring both working banks.
The copier touches neither source, clock nor controls. Therefore the
complete core immediately before W^-1 is exactly the complete output of
W, not merely a state with the same two labels. W^-1 acts on that core
alone and restores every one of its 31 coordinates. The archives are its
untouched complement. Thus

    U(a,d):
      (I(s,r),M_empty,M_empty)
        ->(I(s,r),M[-r],M[-r-Delta_s]).

This is an exact word identity on the declared arithmetic carrier.
It restores the same working-bank addresses 11..30 and the initial source
and clock, not their forward-evolved values. No source or control is
assigned its desired endpoint by an external reset. The two copied records
remain in distinct, counted archive coordinates.

The identity extends with any untouched complete complement, including
arbitrary older O-valued archives: none of its edges mentions that
complement. It does not restore the used archive banks to fresh states.
There are exactly 82 admitted contacts in the two copy subwords; no
input-independent admission count for W or U is needed here.

## 7. A fixed schedule for any declared finite number of inputs

Fix an integer k>=1 before choosing the input values. The complete input
domain is I^k, where I={0,1} times Z/5. Allocate

    core:                 slots 0..30;
    archive A_j:          base 31+20j, j=0..k-1;
    archive B_j:          base 41+20j, j=0..k-1;
    queued cartridge j:   base 31+20k+5(j-1), j=1..k-1.

Each queued cartridge has five slots for (Y_(s_j),X_(r_j)).
All 2k archive banks and both working banks are initially M_empty.
The core is I(s_0,r_0). All six controls and every archive coordinate are
the same for every tuple of admitted inputs.

Let U_j=U(31+20j,41+20j). For j=1..k-1, let Pi_j be the five supplied
whole-slot transpositions exchanging core slots 0..4 with cartridge j in
their corresponding order. The complete chronological program is

    P_k=U_0 Pi_1 U_1 Pi_2 U_2 ... Pi_(k-1) U_(k-1).

This word depends on the declared finite k and the address layout, never
on input values. Every next input is present initially; the word does not
create it from the previous output or receive an external post-start input.
The same read, copy and inverse modules reuse the same working core.
Distinct archive embeddings and cartridge swaps are an explicit fixed
schedule, not a derived autonomous controller.

For completeness, an induction states the actual occupied conditions.
Just after U_j:

- the core equals I(s_j,r_j), including fresh working banks and ready
  controls;
- archives A_i,B_i for i<=j contain M[-r_i],M[-r_i-Delta_(s_i)];
- archives for i>j remain fresh;
- cartridge i for 1<=i<=j contains the restored original input
  (Y_(s_(i-1)),X_(r_(i-1)));
- cartridge i>j still contains its original queued input
  (Y_(s_i),X_(r_i)).

The base case is section 6. Pi_(j+1) exchanges only the current input
with the next untouched cartridge. It leaves the ready controls, both fresh
working banks and every archive unchanged. The next U therefore receives
its proved ready core and two genuinely fresh archive banks, with the
entire occupied prior state as an untouched complement. Section 6 proves
the next induction step. In particular no step substitutes the original
auxiliary state for its actual used state.

The final state is

    core I(s_(k-1),r_(k-1));
    archives (M[-r_j],M[-r_j-Delta_(s_j)]) for j=0..k-1;
    cartridges (Y_(s_(j-1)),X_(r_(j-1))) for j=1..k-1.

After an archive bank's own copy word has completed, no later primitive of
P_k touches it. Its coordinates and addresses are then literally retained.
The temporary source bank of a copier, by contrast, is guaranteed restored
only at its module boundaries and is intentionally erased by W^-1.

There are 26870k contacts and 5(k-1) swaps in P_k. Its unreduced literal
inverse reverses all primitives, replaces every contact by C^4, and leaves
each swap a swap: 107480k contacts and 5(k-1) swaps. These are counts
of the specified words, not optimal lengths or calibrated physical times.

For k=3, the archives occupy 31..90 and queued cartridges 91..95 and
96..100. The common program therefore uses 101 slots, 80610 forward
contacts and 10 forward swaps; its literal inverse uses 322440 contacts
and 10 swaps. The later finite audit has all 10^3=1000 independent input
triples. Forward and inverse trajectory totals for that corpus are
403050000 contact applications and 20000 swaps, excluding separate
construction and local-identity checks.

## 8. Complete resource accounts and current-state decoding

Directly Q(u)=5, Q(w)=Q(b)=3. The source has E=8 and sum 2 at every Y_a;
the clock has E=6 and sum zero. The six ready controls contribute E=8
and sum u+w=2, and both working banks contribute E=60 and sum zero.
Thus I(s,r) has E=82 and sum 4.

For the k-input complete preparation,

    number of slots =31+20k+5(k-1)=26+25k,
    E_total=82+60k+14(k-1)=68+74k,
    Sigma_total=4+2(k-1)=2(k+1).

The 5k designated input-system addresses contribute 14k. The remaining
26+20k auxiliary addresses have one common initial state and account
68+60k. In each initial five-slot input, source coordinate 2 is always
zero; only four coordinate values vary over I. Address allocation is
therefore distinct from counting variable coordinate values.

For k=3, E_total=290 and Sigma_total=8. The fifteen designated input
addresses contribute 42; the other 86 addresses have common account 248.
Twelve input coordinate values vary initially. These are exact initial
resource accounts, not energy burned in the process.

Every Y_a has residues (0,2,0), every X_r has residues (2,3), and the six
controls have residues (0,0,0,0,2,0). Each bank has (3,2)^5. At the
reload boundaries both exchanged input systems therefore have equal
corresponding residues. On this particular prepared family even the
supplied reload swaps leave the complete labelled residue vector unchanged.
Section 1 proves complete conservation at every contact without relying
on endpoints. All parked inputs, archives and work coordinates remain
part of the state; none is dropped from the account.

For each archive bank, a reader checks all ten current coordinates against
the five exact present-record patterns M[p]. It rejects an empty or invalid
bank rather than treating empty as label zero. If the two labels of one
experiment are (a,a'), let d=a-a' modulo five. On the proved family,

    d=Delta_s mod5,
    s=0 when d=1, s=1 when d=3,
    r=-a mod5.

Any other difference is outside this positive decoding contract. The reader
uses only the current archive coordinates, not an original input argument,
the parked inputs, current source, execution counter or saved trajectory.
Applying it to all k archive pairs recovers the full ordered input tuple.
Hence the archive reading is injective on all 10^k admitted inputs.

A separate information bound is conditional on a restricted output code.
If all information must be read from b marked five-valued banks, with no
other readable datum or presence-state option, their at most 5^b states
must distinguish 10^k inputs. Necessarily

    5^b >= 10^k.

For k=3, four such banks have only 625 states and cannot distinguish 1000
triples; at least five are necessary. The present construction supplies
six. In general it supplies 2k banks, an explicit upper bound, not a
minimum. This counting argument is not an impossibility theorem for
different record codes, larger alphabets, other readers or other carriers.

The invariant along the declared forward prefix is that each completed
cycle restores the work banks but fills two additional archive banks.
The remaining fresh archive stock is 2(k-j-1) after U_j. This is not a
monotone quantity on the complete carrier under arbitrary further
iterations or inverse execution. The complete word is reversible, and
its inverse restores the archives as well. No finite-state global
irreversibility is inferred.

## 9. Exact scope and evidence obligations

The construction proves a family of fixed finite schedules on explicitly
funded carriers. It reuses the same two working memory banks, retains the
new records elsewhere, accounts for every prepared and parked input, and
has a complete literal inverse. The universal finite-k induction uses the
same proved local identities; the 1000-case execution, when performed,
will audit the separately frozen k=3 realization.

This text supplies no execution result or external review. It does not
import search minimality, product-orbit sizes, pseudo-random tests,
unverified alternative copy words or an unsupported external-review claim
from the exposed source package. The new public audit must separately
check its word expansion, complete-state checkpoints, decoder,
conservation and inverse against its frozen contract.

No claim is made of raw-input synthesis, freely chosen post-start inputs,
contact-only compilation of the cartridge SWAPs, return of every resource
to its original state while records remain, an indefinitely reusable finite
archive, a minimum account, a shortest program, native-U realization,
autonomous schedule selection, measured energy, thermodynamic erasure,
physical time or physical occurrence. The state-dependent contact
admission is part of the supplied mathematical law; the finite edge
schedule and loading family are also supplied.
