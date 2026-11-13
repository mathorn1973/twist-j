# Exact contact factor and propagation boundary

**NON-CANONICAL / conditional candidate-T / L1 analytical proof.**
A. M. Thorn, 2026-10-15. Original work Apache-2.0.
Owner: ChatGPT-20261015-HB-two-projection. Issue #1509; program #1506.
Preregistration: 8112f35da7c606601cea0a29a408dfc6f9dd96e8.
The four initial files were publicly read back before this proof.

Evidence mode: AUTHORED_PROOF / SELF_REVIEWED / INDEPENDENT_REVIEW_PENDING.
No scientific program, enumerator, solver or hardware experiment was run.
Prior chat exposed the contact formula and contact update, as declared in
PREREG.md. The arguments below are a source-exposed proof, not an independent
confirmation of the author's earlier reasoning. The F collision is proved
from its integer coordinates below, not from a computed trajectory table.

## 1. Inherited definitions and Gram form

Use CONTRACT.md literally. The source matrix A=[s0 s1] is not a tape;
a_in denotes the incoming four-vector A0 of the supplied F. The work ledger
is Wlog, distinct from the wave carrier W=Q^D x Q^D. All transposes and
pairings are the coordinatewise rational ones on the fixed Dirichlet domain.
All source paths, pins and hashes are in SOURCES.json.

Let cY=sum_(j=0)^4 delta_yj. The five sites are distinct, so

    s_i=delta_yi-cY/5  (i=0,1),
    s_i^T s_j=delta_ij-1/5.

Indeed the two cross terms are each -1/5 and cY^T cY/25=5/25.
Consequently

    G=A^T A=(1/5)[[4,-1],[-1,4]],
    det G=3/5,
    G^-1=(1/3)[[4,1],[1,4]].                           (1)

The work summary is

    R(u,v)=A^T(v-Hu/2)=(rho0,rho1)^T.                  (2)

It has rank two and is onto Q^2: for any q in Q^2 choose u=0 and
v=A G^-1 q. Then R(0,v)=A^T A G^-1 q=q. No unproved finite census is
used for this rank statement.

The identities P^T P=I, J0=I-PP^T, K=I-PP^T/2 imply

    KJ0=J0, KP=P/2, K-I/2=J0/2,
    A^T J0=-(1/5) ones2 delta_y4^T.                   (3)

For the last identity, J0 kills the four port delta-vectors and retains
the fifth one. These are exact identities on the given finite carrier.

## 2. All-label work and a total reduced contact (Q1)

### Theorem R1: exact contact factor

**Status: conditional candidate-T / L1.** For every r in F5^2, both
sigma in {+1,-1}, every u,v in Q^D, every B>=0 rational and b in [0,B],
the work and complete accepted/refused contact factor through R as follows.
Write eta=eta2(r)=(eta0,eta1)^T and a=A eta. Then

    Delta_sigma=eta^T G eta/2+sigma eta^T R
               =(2 eta0^2-eta0 eta1+2 eta1^2)/5
                 +sigma(eta0 rho0+eta1 rho1).         (4)

On the reduced carrier

    Y_B=F5^2 x Q^2 x Q x ([0,B] cap Q) x {+1,-1},
    y=(r,R,Wlog,b,sigma),

let alpha(y)=1 exactly when 0<=b-Delta_sigma<=B. The map

    h_B(r,R,Wlog,b,sigma)
      =(r, R+alpha*sigma*G eta,
          Wlog+alpha*Delta_sigma,
          b-alpha*Delta_sigma, (-1)^alpha*sigma)       (5)

is a total involution. Projection pi onto these reduced coordinates
intertwines the supplied full contact and this map:

    pi H_B=h_B pi,             h_B^2=id.              (6)

### Proof

Expand the given energy difference, using sigma^2=1 and H^T=H:

    E_D(u,v+sigma*a)-E_D(u,v)
      =||a||^2/2+sigma*a^T(v-Hu/2).

Substitute a=A eta and (1)-(2), obtaining (4). If the full contact is
accepted it fixes u and shifts v by sigma*A eta; hence

    R'=R+sigma*G eta.                                 (7)

The full and reduced guards agree and their other projected updates are
identical. Refusal fixes the complete state, proving (6)'s intertwining.

On an accepted input let delta=Delta_sigma. The new r and eta are unchanged,
R'=R+sigma G eta, sigma'=-sigma, b'=b-delta. Evaluating (4) there gives

    Delta_sigma'(R')
      =eta^T G eta/2-sigma eta^T(R+sigma G eta)
      =-delta.

The new candidate stock is b'-(-delta)=b, which belongs to [0,B] by the
original carrier condition. The backward call therefore also accepts and
restores every reduced coordinate in (5). A refused input is fixed and
continues to violate the same guard on the second call. Thus h_B^2=id.
All accepted stocks are in the carrier by the two-sided guard. There is
no omitted negative-work or overflow case.

For eta=0, delta=0 and the guard always accepts, including when B=b=0.
The contact still flips sigma; an accepted zero is not declared a refusal.
For nonzero eta with zero delta, the same algebra and guard reversal apply.
This proves totality and involutivity without restrictions on occupancy.

Surjectivity of pi onto Y_B follows from the construction after (2), with
arbitrary fixed tapes. The factor is not a reconstruction of the full wave:
many different u,v share the same R. Nor is E_full asserted to be a function
of R. Equations (4)-(6) concern one supplied contact, not free propagation.

For one already specified nonzero source eta, the single linear scalar
eta^T R suffices for its exact work. A common label-independent summary is
a different question, classified in Section 4. No bit lower bound follows.

## 3. Acquisition support in the supplied stencil (Q2)

### Theorem R2: fixed local linear acquisition and contact update

**Status: conditional candidate-T / L1.** Each rho_i can be acquired using
only v on Y and u on Y+B0, where B0=Bst union {0} from CONTRACT. In particular

    rho_i=s_i^T v-(H s_i)^T u/2.                      (8)

This is a support upper bound in the supplied lattice, not a smallest
footprint or a statement about physical spatial dimension. The exact
accepted contact update is (7); refusal leaves R unchanged.

### Proof

The symmetry of H gives (8). Its first term has support in Y. Write the
kernel coefficients of H, restricted to D, as

    h(0)=10/9,
    h(d)=weight(|d|^2)/324 for d in Bst,
    h(d)=0 otherwise.

For every x in D,

    (Hs_i)_x=h(x-y_i)-(1/5) sum_(j=0)^4 h(x-y_j).      (9)

If x is outside Y+B0 all summands vanish. The entire set Y+B0 is contained
in D=Y+B0+B0 because 0 belongs to B0. Thus the proposed acquisition reads
only actual coordinates of the fixed finite domain. It neither omits nor
changes the principal Dirichlet diagonal. Equation (7) was proved above.

The support calculation gives coefficients, not a native sensor or gate.
Its admission boundary is recorded in Section 6.

## 4. Complete classification of fixed linear summaries (Q3)

### Theorem R3: kernel criterion and sharp linear rank

**Status: conditional candidate-T / L1.** Let L:W->Q^m be any one fixed
rational linear map independent of the receiver label. Allow arbitrary
functions of L(u,v), separately for every label and sign, as in CONTRACT Q3.
Then the following are equivalent:

    (a) every exact Delta_sigma(u,v;r) can be recovered from L(u,v);
    (b) ker L is contained in ker R;
    (c) there is a rational linear C:Im(L)->Q^2 with R=C L.       (10)

The least possible rank of L is exactly two. If rank L=2, L and R are
invertible linear reparameterizations of each other on their images.
This classifies the complete frozen linear-summary class even though
its allowed output decoders need not be linear.

### Proof

Among the 25 receiver labels are r0=(2,4) and r1=(0,1). The balanced lift
gives eta2(r0)=(1,0) and eta2(r1)=(0,1). At sigma=+1, (4) gives

    Delta_+(u,v;r0)=2/5+rho0,
    Delta_+(u,v;r1)=2/5+rho1.                          (11)

Assume (a). If d is in ker L, L(d)=L(0). Both arbitrary recovery functions
in (11) must return the same values at d and zero. Hence both coordinates
of R(d) vanish. This proves (b) without assuming linearity of the decoders.

Under (b), define C on Im(L) by C(Lw)=Rw. It is well-defined: if Lw=Lw'
then w-w' is in ker L, so Rw=Rw'. This also proves C is rational linear.
Thus (c) follows. Under (c), use the right side of (4) with R=C Lw to
recover each work value, proving (a).

By (2), rank R=2. Equation (c) implies rank L>=2. Choosing L=R attains
rank two, establishing the sharp bound. If rank L=2, inclusion (b) and
rank-nullity on the finite-dimensional W give ker L=ker R. Therefore the
induced maps W/ker R -> Im(L) and W/ker R -> Q^2 are linear isomorphisms,
which establishes the reparameterization statement.

This says nothing about a nonlinear encoding of W into a rational, an
energy-assisted summary, a label-dependent map, variable precision, an
initialized subfamily, a Boolean guard alone or the minimum number of
controller states. The logical scope is exactly CONTRACT Q3.

## 5. Exact refresh under F and failure of autonomous closure (Q4)

### Theorem R4: a one-step refresh needs an additional local scalar

**Status: conditional candidate-T / L1.** For every occupied X, let

    gamma(X)=(u_y4-(Hv)_y4/2)/5.                       (12)

Then after one supplied F,

    R(FX)=gamma(X)*ones2+2 A^T P a_in.                 (13)

Equivalently, if t=sum_(j=0)^3 (a_in)_j,

    rho0(FX)=gamma+2(a_in)_0-2t/5,
    rho1(FX)=gamma+2(a_in)_1-2t/5.                     (14)

In particular rho0(FX)-rho1(FX)=2((a_in)_0-(a_in)_1). With a_in=0
the two post-F projections are equal, for arbitrary prior wave occupancy.
Nevertheless there is NO single-valued function of the complete summary

    (R,A0,A1,B0,B1,k,E_full,r,Wlog,b,sigma)

that returns R(FX) for every occupied X. Identical native/clock spectators
may be adjoined without changing this negative conclusion.

### Proof of the refresh formula

The new wave pair is (v,w). By the exact F and (3),

    w-Hv/2
      =(K-I/2)Hv-KJ0u+4KP a_in
      =J0(Hv/2-u)+2P a_in.

Multiplying by A^T and using A^T J0=-(1/5)ones2 delta_y4^T gives
(12)-(13). Since s_i^T P a_in=(a_in)_i-t/5, (14) follows. The quantity
(Hv)_y4 reads only v on y4+B0, still within D. The formula has not replaced
that actual field acquisition by a function of the previous R.

### Exact collision including the same selected energy and tapes

Let z=(6,0,0). It belongs to D because z=y4+(4,0,0)+0 and (4,0,0)
is an admitted squared-length-16 stencil vector. It is outside Y.
Take two complete valid apparatus states X_plus and X_minus with

    u_plus=u_minus=0,
    v_plus=+delta_z, v_minus=-delta_z,
    A0=A1=B0=B1=0, k=0,
    r=(0,1), Wlog=0, B=1, b=1, sigma=+1,

and every other spectator equal. There is no contact performed here; the
transition tested is exactly F. Since s_i is supported on Y,

    R(X_plus)=R(X_minus)=(0,0),
    E_full(X_plus)=E_full(X_minus)=1/2.                (15)

Every entry of the input summary in Q4 is therefore identical.
The displacement from y4 to z is (4,0,0), so H_(y4,z)=1/324. Equations
(12)-(13) now give

    R(F X_plus)=(-1/3240,-1/3240),
    R(F X_minus)=(+1/3240,+1/3240).                    (16)

For clarity, the squared distances from z to y0,y1,y2,y3 are respectively
36,26,26,38. None is an allowed shell, so P^T H delta_z=0. Thus K H delta_z
=H delta_z and the first outgoing cut is also zero in both cases. All
output tape slots remain zero and k becomes one in both states. Their
post-F energies remain equal to 1/2: with v=+/-delta_z and w=Hv,

    E_D(v,Hv)=(||v||^2+||Hv||^2-v^T H^2 v)/2=1/2,

using H^T=H. The collision is not caused by differing tape contents,
energy, finite flags or a different boundary convention.

A function of the identical input summary (15) would have one value,
but (16) supplies two different exact values. This proves the asserted
nonexistence for every deterministic summary update, not only linear ones.

The example is an all-occupied rational-carrier witness. No claim is made
that these two states belong to the special two-use common-ready image.
It is not a contradiction to the one-scalar collapse on that image.

Equations (12)-(14) provide a constructive boundary: current gamma and the
incoming tape suffice to refresh R once. They DO NOT prove that adding one
gamma register closes future propagation, provide a gamma update, select
a minimum predictive memory or implement a native contact. Q4 is complete
at its frozen one-step scope; such further questions require a new contract.

## 6. Permission origins and what remains open (Q5)

**Status: source audit / no admission grant.** The following table records
what the pinned sources actually supply. The status names are the permission
categories frozen in A1's CONTRACT Section 3, not new Canon claim statuses.

| Component | Source and origin | Boundary |
|---|---|---|
| Original selector-defined U and native coordinates | CANON-ADMITTED as mathematical definitions, CORE and REGISTRY; A1 P-U | Not a global inverse and not a mixed rational contact |
| Fixed generator maps g_i | CANON-ADMITTED as defined maps, A1 P-G | A freely selected word is not automatically an autonomous U run |
| Retained label r, eta and insertion S eta | EXPLICITLY-SUPPLIED-COMPARISON for the mixed use, R1 CONTRACT and A1 P-ETA | Mathematical native coordinates do not by themselves authorize this rational interface |
| Rational wave/tapes, stencil D, energy and F | EXPLICITLY-SUPPLIED-COMPARISON, #1485/A2/R1 and A1 P-F | No derivation from U or physical spatial realization is supplied |
| Acquisition of rho0,rho1 | Exact mathematical formulas proved in Sections 2-3; as an actuator input still UNSUPPLIED natively | A local formula is not a native sensor or gate |
| Acquisition of gamma for refresh | Exact formula proved in Section 5; UNSUPPLIED natively | Requires actual occupied-field information not contained in old R and energy |
| Rational arithmetic and exact order comparison | EXPLICITLY-SUPPLIED-COMPARISON kinds in A1 P-REG/P-CMP | This note does not repair the bounded-register typing defect of A1 Gamma+ |
| Bounded stock actuation and source translation | H_B is a supplied target from #1496/R1; not a native letter | Factorization of its work does not compile its accepted/refused global action |
| Retained sigma and its flip | EXPLICITLY-SUPPLIED-COMPARISON in the supplied H_B | Linear summary rank does not prove minimality of control bits or authorize their erasure |
| Autonomous acquisition/control, renewal, physical energy and occurrence | UNSUPPLIED at the relevant native/physical owners | No L2-L6 or SI result is claimed |

A1's wave-blind and store-blind obstructions remain scoped to its frozen
grammars. The present note shows exactly which wave information suffices
for the supplied one-contact work. It neither claims that the old no-go
requires all wave coordinates nor that this smaller summary is admitted
by Canon. A1's Q3 compiler question remains untouched. The two current
owner rows QUADRATIC-MEMORY-NATIVE-CONTACT and QDD-INSTRUMENT-APPARATUS
remain O, with their existing full scopes and gates.

## 7. Adversarial self-review and scope ledger

This section is SELF_REVIEW, not an independent agent's review.

- Gram/rank: all five marked sites are distinct, giving (1) directly.
  The two labels in (11) really are in the full 25-label domain. The rank
  lower bound does not assume output decoders are linear.
- Contact guards: accepted images always accept the reverse increment
  because the original b is in [0,B]. Refused states are fixed. B=0,
  eta=0 and negative work are covered without dropping the upper bound.
- Scope of the factor: pi loses wave data. No proof asserts a full-state
  inverse through R, nor a value of E_full determined by R.
- F collision: z lies inside the fixed D, outside Y, with exact distances
  16 to y4 and 36,26,26,38 to the ports. Both initial energies are 1/2;
  the actual outgoing tapes also agree. No decimal or numerical window
  enters the proof of distinct next summaries.
- Native versus mathematical: all contact/wave arithmetic is inherited
  comparison content. The note grants no new operation to the native U.
- Independence: source/result exposure is disclosed. No scientific code
  ran, and no two-architecture scientific verification is claimed. A
  different owner must review these four theorem statements and proofs.

Q1, Q2 and Q3 have the positive exact dispositions in Theorems R1-R3.
Q4 has both the exact refresh formula and the negative full-summary closure
disposition in Theorem R4. Q5 identifies remaining permissions but does
not discharge them. The whole package is NON-CANONICAL, conditional
candidate-T for its mathematical statements, physical NOT_READY.
