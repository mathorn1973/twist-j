# Frozen two-use controller contract

**NON-CANONICAL / L1 / proposed mathematical apparatus, not native admission.**
Original work Apache-2.0, A. M. Thorn, 2026-10-14. Reservation #1499.
Equality everywhere is literal coordinate equality, including output signs.
This contract is frozen by its first public commit; proof files are later.

## 1. Fixed classical carrier and primitive permissions

Inherit the complete classical CONTRACT at
`1b69563af4018b08d7dc75781b12e9553a8c19c3` and the contact CONTRACT at
`ea924e214ec3c29009fd4590f294954d3e5ad43f`, as pinned in SOURCES.json.
The following is a concise restatement of their definitions, not a new law.

Let D3 be the even-coordinate-sum integer lattice. The symmetric stencil B
has squared lengths (2,4,8,10,16) with weights (6,1,15,1,1)/324. Put
Y=((0,0,0),(1,1,0),(1,0,1),(0,1,1),(2,0,0)), Bz=B union {0},
D=Y+Bz+Bz, ordered lexicographically. P inserts the first four marked sites
in that order. L is the principal Dirichlet restriction of
Lf(x)=sum_d c_d(f(x)-f(x+d)); the boundary diagonal remains 8/9.
Set H=2I-L, K=(I+PP^T)^-1, J0=I-PP^T. For z in Q^4,

    S z=sum_(i=0)^3 (z_i-s/5) delta_yi -(s/5) delta_y4,
    s=sum_i z_i.

The complete classical state is X=((u,v),(A0,A1),(B0,B1),k), with
u,v in Q^D, all four tape entries in Q^4 and k in Z/2Z. The inherited F is

    w=K(Hv-J0u+4P A0), b=A0-P^T(w-u)/2,
    F X=((v,w),(A1,B1),(b,B0),k+1).

All coordinates, including occupied ones, are retained. Define
E_D(u,v)=(||v-u||^2+u^T L v)/2 and
E_full(X)=E_D(u,v)+2 sum_(T=A0,A1,B0,B1)||T||^2.

For a retained signal r=(q,r2) in F5^2 use
ell=(0,1,2,-2,-1) and eta(r)=(ell(q)/2,(ell(r2)+1)/2,0,0).
The conditional contact C_r translates v to v+S eta(r), preserves all
other X coordinates and increments a signed rational work register W by
E_D(u,v+S eta(r))-E_D(u,v). This is the existing C_*.
W is not a nonnegative battery and is not assigned a physical energy.

Permitted new control operations are a phase rotation, a receiver-controlled
addition into a retained F5^2 buffer, and phase-controlled calls to these
fixed F and C primitives. These permissions are declared mathematical
extensions, not consequences of U or J. No source-dependent initial buffer,
output-dependent gate selection, renewal operation or dissipative STOP is
permitted. Refusal/funding is absent in this signed-work reference model.
Section 7 specifies what a later funded replacement must supply.

## 2. Native source, delayed signal and all clocks

The complete state of the proposed coupled map is

    Z=(n,x_A,x_B,X,W,d,c).

Here n is the one native counter in N0; both x_i are in F5^6; X is as above;
W is rational; d is a retained F5^2 delayed receiver; c is in Z/8Z.
The fixed program is the eight-row table below, part of the law rather than
a mutable or consumed word. The update always rotates c to c+1 modulo 8.

Native tick V is

    x_i'=g_(sum(x_i)+2 theta_n mod5)(x_i), i=A,B;
    n'=n+1, theta_n=popcount(n) mod2.

It uses the unchanged five canonical generators on each independently
supplied head, with a shared counter. This two-head product and exposure of
the retained n are explicit interfaces. They are not one native six-coordinate
system or an automatically admitted physical two-source device.
There is no future Thue-Morse window, dropped bit or unspecified bit oracle;
the exact function is evaluated on the actual stored n. No five-context
sidecar or 23-state raw-residue updater is used.

The classical cut count t counts only F calls. It is not n or k. Program
phase c selects operations. Use identities A/B and cut identities 0/1
are fixed labels of those calls. For the first period the phase boundaries
have n=(0,1,1,2,3,3,4,5) and t=(0,0,0,1,2,2,3,4).
On later periods the map remains defined without any reinitialization;
native n continues. From an origin-zero start, n and c determine the period
number using these offsets, with n=5r at phase 0 and n=5r+5 at phase 7.
No additional event or round identity is discarded.

## 3. Proposed autonomous map, including used and off-ready states

Let rec(x) denote its last two native coordinates.
All operations in a row occur before advancing c.

| c | Operation on the complete state |
|---|---|
| 0 | V on both native heads; all apparatus coordinates held |
| 1 | d <- d+rec(x_B) in F5^2, and C_rec(x_A) on X,W |
| 2 | V and F on their separate factors |
| 3 | V and F on their separate factors |
| 4 | C_d on X,W; native state and d held |
| 5 | V and F on their separate factors |
| 6 | V and F on their separate factors |
| 7 | hold every coordinate except the always rotating c |

There is no test that overwrites an occupied buffer with a new symbol. At
c=1 an already occupied d is added modulo five, not replaced. All rational
wave/tape states, both k values, every phase and every n remain in the
domain. Re-entering a used program means applying this same table to its
actual state; it is not a second ready run. No claim of fresh inputs or
direct archive persistence for arbitrarily many periods is proposed.

Completion is the event predicate n=5,c=7 on the first initialized period,
with four completed F calls, not an absorbing state. Phase 7 rotates to 0.
The contract promises direct retention through this two-use horizon only.
It must explicitly report when later recirculation can consume that record.

Two different inverse domains must be addressed. First, the abstract
apparatus map on (X,W,d,c), with two immutable supplied receiver labels
r_A,r_B replacing rec(x_A),rec(x_B), has identity native rows and must be
a two-sided permutation on its whole product. Second, the autonomous
coupled map including V must have a left inverse and exact image-recognition
test on the common-ready native runs. It is NOT required or asserted to be
onto on N0 times all checkpoints. The apparatus permutation must never be
advertised as a global inverse of V or the full native selector.

## 4. Preparation and signal scope

For every independent pair (p_A,p_B) in F5^4 x F5^4, prepare

    n=0, x_i=(p_i,0,1), d=(0,0), c=0, k=0, W=0,
    u=v=0, A0=A1=0, B0=c0, B1=c1.

For each fixed rational pair (c0,c1), this is one common apparatus readiness
independent of both p's. The union of these families includes occupied old
archives; the fully blank subfamily has c0=c1=0. No slot is supplied midway.
General warm wave and incoming-tape values are also in the total map's
domain, with no cold-response promise off these ready families.

Write h_i=sum(p_i) mod5. The elementary signal family is all 25 ordered
(h_A,h_B), including zero. The delayed buffer is to capture B's actual
first-tick receiver at n=1 by reversible addition, while B itself continues
under V. The second contact at n=3 deliberately reads this paid-for buffer,
not a falsely restarted B and not its current receiver relabelled as C1.
This is an explicit source-dependent memory resource with 25 states.
The five inherited first-tick encodings are
(0,0,0,0),(1/2,0,0,0),(1/2,1/2,0,0),(1,1/2,0,0),(0,1,0,0).

If complete input preservation is established, its quantifier must cover
every pair of full four-residue inputs, not just these 25 signal labels.
The fixed stage/cut occurrence identifies present zero outputs. No sixth
absence symbol is added to a native signal: UNWRITTEN versus PRESENT(0)
is the typed reader's result using the retained program/native boundary,
not a new value of F5. Old tape values are not certified fresh events merely
because they are nonzero; origin and declared cut labels matter.

## 5. Primary target and exact comparisons

Mandatory target OCCUPIED_CONTINUATION:
derive the full state after all four actual F transitions with the second
contact between the second and third. Give a fixed direct chronological
reader of all four Q^4 outputs, and show where the first two reside at every
intermediate boundary until completion. Derive all cross-use dependence for
all rational c0,c1 and all signal pairs. A record recoverable only by undoing
the whole machine does not meet this target.

Give an exact WARM witness from a reachable first ready trial in Section 4:
explicit native/rational inputs, actual intermediate wave and tapes, a nonzero
occupied coordinate, and both actual second outputs versus a fresh second
trial. The fresh comparator starts wave/tapes blank, uses the same second
source vector, then makes exactly two F calls. The first family permits
occupied old archives; their preparation and energy must be disclosed. A
witness using them must not be mislabeled as arising from a fully blank first
apparatus. The universal cross-use formulas must also cover that fully blank
first subfamily. Require a nonzero rational output difference, or a complete
equality theorem over the fully frozen family with the corresponding negative
disposition of the claimed distinction.

Secondary target CLEAN_TRIAL_RENEWAL:
decide whether this exact table, without a new export/reset operation,
universally gives the old cold two-cut law on use B for all ready inputs.
A counterexample decides that literal claim only. Broader renewal with new
resources or a different operation remains UNSUPPLIED, not universally
impossible. Attaching a new whole apparatus is not admitted as renewal.

The finite D is unchanged. First-use causal comparison retains only its
inherited two-cut scope. The four-cut theorem, if established, is exclusively
for fixed finite D. No enlarged causal comparison is requested.

## 6. Resource, inverse and failure requirements

Supply every elementary forward/inverse formula and domain; a full ready-image
recognizer must include original piston-sum and common-ready checks, not just
a successful algebraic inverse on an inconsistent endpoint. Retain d, c, n,
all source coordinates, wave, tapes and W. State the energy invariant and
source-dependent work at both contacts, including arbitrary occupied waves.

Finite program phase and a finite number of rational slots do not imply a
finite-bit complete machine. Native n is unbounded; Q has unbounded numerator
and denominator capacity. No finite-bit, infinite-use, permanent-record,
physical zero-cost control, sampling or entropy claim is proposed.

Reject a positive assertion on any explicit admitted state violating its
inverse, typed readout, input recovery, accounting identity, readiness test
or literal cold comparison. Tolerance is zero. Failed universality is recorded
at this class, with no public F assigned to a parent O obligation.

## 7. Export to a future contact and unpassed bridges

The abstract source port is a retained F5^2 label with the fixed eta map.
A compatible contact takes (label,u,v,A,B,k,W,E_control) to a complete state,
preserves the label and unaffected tape coordinates, and on its independently
specified successful domain realizes exactly v+=S eta(label). It must supply
an inverse on its exact domain, a retained success/refusal/direction state,
and the full resource update, including work
Delta=E_D(u,v+S eta)-E_D(u,v). It must work at BOTH actual wave states here.
If a nonnegative battery is used, its admitted carrier, bounds, funding at
each call, rejected-call behavior and complete conservation law are additional
premises. A rejected call cannot be silently counted as a successful trial.

The reference contact is total with an unrestricted signed work ledger, so
the controller proof supplies no bound on a physical battery. A future H_B
or other native-admitted contact must separately meet this signature at the
actual second occupied state and retain any phase/direction needed for its
inverse. No result of A1 or its new code is consumed. Native compilation,
physical source acquisition, buffer writing, clock/control energy, independent
calibration, material memory and renewal, occurrence, SI and L2-L6 bridges
remain UNSUPPLIED. QUADRATIC-MEMORY-NATIVE-CONTACT and
QDD-INSTRUMENT-APPARATUS remain open at their registered scopes.
