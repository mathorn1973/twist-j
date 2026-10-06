# C-CONTACT-INTERFACE-CLASSIFICATION-N: frozen interface classification

Status: NON-CANONICAL / NO AUTHORITY. Action layer: L1.
Owner: A. M. Thorn, session contact-interface-classification-20261006.
Public reservation: https://github.com/mathorn1973/twist-j/issues/1396.
This is a notes-only analytical and exact finite audit, not a formal probe.
No scientific execution precedes this preregistration.

## 1. Authority, provenance and question

The source is Public Canon v100 on public main/tag
`807dae3fe97dd6a872d5d1305a0133e8e8d856ea`, content commit
`a4cc9666662967527abe711441833ff600c00337`. Canon SHA-256 is
`5e4de2da8d57ff2f7e4b873e6236b0695677e20d173d894ee70562c1389648c4`,
980212 bytes. STATUS, POLICY, AGENTS, CORE, FRONTIER, relevant registry,
evidence and gate rows were read; all five normative hashes, content/tag
ancestry, main x86_64/aarch64/check, tag and release readbacks were verified.

The mathematical inputs are the original native maps and
DEF-RESIDUAL-CONTACT-ARCHITECTURE / CONTACT-RECORD in the pinned Canon.
The old CONTACT-RECORD reference minimum is an input, not a new claim.
Neither its sealed probe nor any current Canon file is modified.

This is a retrospective classification motivated by the known supplied
interface. The source reading h, the native involution I, dependence only
on h and eta, the reference encoding and its marked discrimination task
are DECLARED PREMISES. They are not derived from J, independently physically
admitted, or selected by this work. No assertion of blindness to the existing
successful example is made. Analytical expectations existed before the pin;
the new census has not been executed. The broad control class does NOT impose
W=id on h=0, and does NOT impose the desired contact response or use L5 or M
to select a member. Class completeness always means this specified table
class, never the complete native or physical apparatus class.

Question: which complete contact laws and prepared reference readings follow
from these restrictions, and which choices remain? Report all alternatives.
More than one law is not a falsification of the old conditional theorem or
negative closure of QUADRATIC-MEMORY-NATIVE-CONTACT. One law, if found, would
not independently admit this class either. The supplied C, W_a, preparation,
autonomous execution, physical occurrence and cross-layer questions remain
outside this candidate. This is a mathematical input to topic C in #1384;
that issue's unpublished local package is not an evidence dependency.

## 2. Complete source and conventions

All coordinate arithmetic is in F5, represented by 0,1,2,3,4. A cell is

    x=(p1,p4,p1p,p4p,q,r).

The complete carrier is X=F5^12 times {0,1}, with two cells x,y and bit eta.
The native maps used here are exactly

    b(x)=(-p1p,-p4p,-p1,-p4,-q,-r),
    d(x)=(2-p1,1-p4,3-p1p,4-p4p,1-q,1-r),
    e(x)=(2-p1,1-p4,3-p1p,4-p4p,2-q,1-r).

Products act right to left; [A,B]=A B A^-1 B^-1. Set I=b_x b_y and
tau_i=e_i d_i, i=x,y. Thus I is an involution, negates both q and r,
and tau_i fixes every coordinate except q_i -> q_i+1. Its inverse is d_i e_i.
Do not confuse tau_i with the autonomous U or introduce a clock state.

Write the piston coordinates as row-major 2 by 2 matrices Xp,Yp. Define

    h=(det(Xp+Yp)-det(Xp)-det(Yp))/2.

Division by 2 means multiplication by 3 in F5. The pinned source gives
h(I s)=-h(s), where s denotes all twelve cell coordinates. h does not depend
on q,r,eta and is unchanged by either tau_i. Every h value is attained:
one useful full-state witness has Xp=(1,0,0,0), Yp=(0,0,0,2h).
I moves the pistons of this witness even at h=0. This witnesses faithful
distinction of the two possible data actions on each h sheet.

Each table lookup below uses its CURRENT input h and eta, including inside
composed and inverse words. No initial h/eta snapshot is carried for free.

## 3. Complete control class

Let a,beta be arbitrary functions F5 times {0,1} -> {0,1}. Define on ALL X

    W(s,eta)=(I^a(h(s),eta) s, beta(h(s),eta)).

There is no other dependence and no added state. In particular the h=0
branch is unrestricted by an identity condition. Admit exactly those
tables for which W is a bijection of the complete carrier. Mark separately
the subclass W^2=id. A table is encoded by the ten digits

    c[2h+eta]=2*a(h,eta)+beta(h,eta),

ordered by h=0,...,4 and eta=0,1. Raw equality of tables is literal equality
of these ten digits. The proof must establish when this is also literal
equality of complete W maps and why the small orbit description is faithful.

On each nonzero pair {k,-k}, k=1,2, use the four labels (u,eta), u=0,1,
h=(-1)^u k, ordered 2u+eta. On a free h=0 I-orbit use the same four labels
with u denoting the actual I position; table values still depend only on
h=0 and eta. This finite representation is a proof aid, not an independently
admitted replacement carrier. Fixed I states at h=0 must also be covered.

For each admitted W define, on the unchanged full carrier,

    E_W=W I W^-1,
    K_(W,i)=[E_W,tau_i].

Classify the complete K maps, not only their factor projection. Prove their
full action and inverse, whether pistons/r/eta return, whether any q action
depends on occupied eta, and exactly how many W realize each different map.
Repeat the census for the involutive W subclass. Give explicit witnesses for
every distinct contact law, in the original marked coordinates. Also locate
the existing v100 W_b in this class without changing it.

The anticipated structural claim to test is that every K restores all
coordinates except q_i and is of the form

    q_i -> q_i+3*chi(h),

where chi is binary, chi(0)=1 and chi(-h)=chi(h). These are proposed
consequences, not admission tests. An admitted W violating any of them is a
fired counterexample to this anticipated claim and must be preserved; the
class may not be narrowed. If the claim holds, represent a law by the string
chi(1)chi(2), and derive its unique even polynomial of degree at most four
over F5. Determine whether all such binary law profiles occur. No desired
profile or count is a membership filter.

## 4. Complete pointwise reference-table class

The embedded reference has all five native values. Each P_q, q in F5, is
an arbitrary permutation of {0,1,2}, extended by pointwise fixing 3 and 4.
Let C_P change only r_i by P_(q_i). It leaves every other coordinate fixed.
The inverse changes r_i by P_(q_i)^-1. Both are declared couplings.

For the fixed known experiment tau_i^3 define

    R_P=C_P^-1 tau_i^3 C_P.

An admitted reader table satisfies the marked one-query contract

    P_(q+3)^-1 P_q(0)=1  for EVERY q in F5.

The identity experiment gives C_P^-1 C_P=id and ready output 0. Classify
all tables satisfying this condition. Mark separately the tables for which
every P_q is involutive; the supplied v100 table belongs to this subclass.
This is not a classification of all reversible encoders/decoders: the fixed
pointwise-in-q form, preserved q, reference subset and marked labels are
premises. No new proof of the already established minimum three is claimed.

The known comparison table, restricted to its active subset, is

    P0=(0,2,1), P1=(0,1,2), P2=(2,1,0),
    P3=(1,0,2), P4=(1,0,2).

Three equalities/equivalences are frozen BEFORE the census:

1. Literal table equality: all fifteen values P_q(r), q=0,...,4,
   r=0,1,2 agree. The table ID is their fifteen-digit concatenation.
2. Literal complete endpoint-reader equality: the maps on all q,r agree,
   including occupied reference values. Record the fifteen-digit signature
   of P_(q+3)^-1 P_q(r); q always advances by 3 and r=3,4 stay fixed.
3. Algebraic relabelings, without claiming physical equivalence:
   q translation t acts by P_q -> P_(q+t), with complete endpoint maps
   conjugated by the actual q translation. Internal reference relabeling
   L in S3 acts by P_q -> L composed with P_q, extended to fix 3,4.
   Determine the orbits, stabilizers and complete-map equality under these
   actions. Do not assert that internal relabeling preserves pointwise
   involutivity. q labels may not be reversed or rescaled, and the marked
   external ready/output values 0,1 are never exchanged.

Derive the full occupied-reference action and inverse for every admitted
reader paired with any contact law from section 3. Any prepared readout
classification must be kept distinct from complete-map equality. An equality
of contact/readout endpoints is not equality of W prefixes, the compiled
T_alg word, its q lift, or the physical meaning of all those operations.

## 5. Exact finite audit and independent breaker

The primary verify.py and an independently written break.py will be frozen
as Git commits with SHA-256 identities BEFORE either is executed. The breaker
will read this preregistration and its explicitly pinned source identities,
not verify.py. Freeze break.py before comparing implementations or outputs.
The author may compile and statically inspect before a code pin; no scientific
enumeration or gate run is allowed before the relevant pin. Analytical proofs
may be prepared before computation and are not described as blind discovery.

Required mathematical coverage:

- complete cell source-identity audit on all 5^6 inputs for b,d,e, tau and
  I/tau inversion, using the formulas above;
- h(I s)=-h(s) over all 5^8 piston pairs;
- every admissible control table and all involutive members, by a complete
  enumeration or a proved equivalent orbit construction; a separate raw-table
  or distinct orbit method must independently establish completeness;
- complete contact action on the small faithful I-orbit/bit description,
  with both q coordinates and both ports, and a proof transferring this to X;
- direct native-coordinate word checks for every admitted control, each
  h=0,...,4, both eta, each port i and each q_i=0,...,4, with q_other=2,
  r_x=1,r_y=2, and the displayed piston witness. Check K and its inverse
  against the derived full map. These are bounded witnesses, not an exhaustive
  census of X;
- all 6^5 reference permutation tables, or a proved equivalent complete
  construction; test the ready contract at every q and the full occupied
  map at every q and every r=0,...,4; include the involutive subclass;
- exact table and endpoint-map fibres and the frozen relabeling orbits;
- the supplied old W_b and P table only as regression witnesses of the new
  class embedding, not as a new independent confirmation of the sealed probe.

The primary and breaker may use different internal algorithms and proof
reductions. They must not import each other or any repository verifier.
Only the Python standard library, integers, finite tuples and exact modular
arithmetic are allowed. No floats, random samples or target-dependent search.
Each scientific execution has a real wall timeout of 180 seconds, LC_ALL=C,
LANG=C, PYTHONDONTWRITEBYTECODE=1, PYTHONHASHSEED=0 and TZ=UTC, and uses
python3 -I. A timeout is an incomplete audit, not a scientific exclusion.

On success both programs emit the same canonical JSON object (sort_keys=True,
separators=(',',':'), one trailing newline), with exactly these top-level keys:

    status, controls, readers

status is PASS. controls contains keys total, involutive, law_counts,
involutive_law_counts, even_polynomials, census_sha256. The law dictionaries
use all realized two-digit profiles; a polynomial is [constant,h2,h4] in F5.
Control hash input consists, in increasing ten-digit table-ID order, of

    table_id + TAB + law_profile + TAB + involutive_bit + LF.

readers contains keys total, involutive, table_q_orbits, endpoint_maps,
endpoint_q_orbits, involutive_q_orbits, internal_orbits, joint_orbits,
census_sha256. Reader hash input consists, in increasing table-ID order, of

    table_id + TAB + endpoint_signature + TAB + involutive_bit + LF.

No expected count or digest is supplied to the independent implementation.
Counts are outputs of the frozen classification, not adjustable thresholds.
Failure must print a specific exact witness or assertion description, exit
nonzero, and be retained in the first-run record. Do not overwrite a failed
transcript, alter the class, move a threshold, or call a corrected rerun the
original run. A substantive correction requires its own disclosed successor
pin/disposition. The note is not a sealed public P-probe.

## 6. Proof and result obligations

The written proof must justify the reduction from complete X, all census
counts, all claimed equivalences and complete-map inverses. It must identify
which source restrictions force each feature. The finite audit alone cannot
replace this full-carrier argument. An independent reviewer checks the proof
and the distinction between admitted tables and physical/native admission.

If several contact laws occur, exhibit their different ready outputs without
using a target L5 update, and state how to distinguish them in this declared
family. Such a comparison is only a conditional algebraic calibration task;
no preparation, detector or measurement has been supplied. A minimal number
of fixed ready-reference queries may be claimed only for the frozen query
class: each query chooses one h, starts a separate reference at 0, applies
one complete contact/reader and reads that one marked reference. No reuse,
extra output, adaptive physical apparatus or free reset is presumed.

Maximum status: candidate-T for separately reviewed exact proofs and
candidate-C for one-architecture finite audits. Ordinary notes pull-request
checks do not execute this scientific package as a two-architecture gate.
Do not upgrade those checks into scientific confirmation. Promotion requires
its own later public procedure and a PROMO disposition. Existing Canon,
registry, frontier, gates, sealed probes, workflows and releases remain
outside this write scope.
