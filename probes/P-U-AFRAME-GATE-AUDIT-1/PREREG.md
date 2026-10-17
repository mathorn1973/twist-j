# Independent native-gate audit: frozen preregistration

PUBLIC / NON-CANONICAL / L1. Public claim #1559; program #1548, lane RA.
Owner/session: ChatGPT-v103-RA-20261016-05ccc15f.
Author: A. M. Thorn. Original work: Apache-2.0.

## 1. Equation, question and equality

Audit the exact scope of P-U-AFRAME-GATE-1, author claim #1550, without
editing or importing its package. The mathematical carrier is F5^6, with
literal tuple equality, x=(p1,p4,p1p,p4p,q,r), z=sum(x) modulo 5,
theta_n=popcount(n) modulo 2, and

    T_t(x)=g_(z(x)+2t mod 5)(x),  g_0,...,g_4=a,b,c,d,e,
    x_(n+1)=T_(theta_n)(x_n),  n starts at 0.

The five affine generators are the unchanged maps in
DEF-NATIVE-WORD-CURVATURE-CLASS. On pistons use the fixed comparison
W(p1,p4,p1p,p4p)=(p4,p1,p4p,p1p), h=(2p1+p4,2p1p+p4p),
G={h=0}, X_s={z=s}, X14=X_1 union X_4, G14=G intersect X14,
and J2(u,v)=(v,u). J2 is just a two-coordinate swap, not the algebraic J.
The field input is the unchanged selected A_f,B_f,L,Vinv,Vh of the
FIELD-CONSERVATIVE-CHAIN-LAW / FIELD-CHAIN-FIRST-WORK shared proof 2;
H(y)=y^t B_f y/2 and

    C={(a,b,c,d) in F5^4 : a+2b=c+2d=0}.

The requested decisions are complete finite generator and branch laws,
the shell-image comparison, synchronized all-future gate membership,
the origin-zero prefix, exact initial-state classification, and inheritance
from the already canonical invariant V. Every comparison is literal at its
declared carrier; no metric, generator, context or source is retuned.

## 2. Code, independent derivation and source custody

The sole new scientific program is verify.py, Python standard library only.
It represents the native maps by independently transcribed sparse affine
rows, forms its own exact integer matrix checks and exhausts the complete
finite carriers. PROOF.md is the independent written derivation; it is
frozen with the code before the first scientific execution. Same-session
helpers contributed to this one RA package and are not additional
independent reviewers.

The author pin is 7b06ea6b377930f6edeb84cb330b9d69f1b82c51. Only its
PREREG.md and SOURCES.tsv have been opened. Their byte lengths and hashes,
and the admitted canonical sources, are bound by SOURCES.tsv in this audit.
The author proof, verifier, EXPECTED, RUN, RESULT and exposing PR diffs have
not been opened. They remain prohibited until this audit's own public pin,
readback and first recorded run. No previous scientific verifier is copied,
imported, executed or treated as an independent implementation.

The expected hypotheses in #1548 and the author's preregistration are
exposed. Independence is in derivation and implementation, not a claim of
blindness to those hypotheses. The explicit prefix formulas below were
derived directly from the canonical generators before comparison.

Runtime input is only the mathematical constants frozen in verify.py.
Source custody is checked at intake and pin readback, not by consulting a
mutable external service during scientific execution. INPUTS.sha256 binds
the initial own files except itself; the immutable Git commit binds it.
No first run, import, exploratory run, benchmark or dry run is permitted
before the public pin. Static parsing, compilation without execution,
file hashes and written algebraic review are permitted.

## 3. Complete carriers and nine frozen falsifiers

Any failed item is retained at its exact scope. These obligations mirror
the author's frozen questions, not its unread implementation or output.
PROOF.md states the equations and the all-time deductions explicitly.

### F1: native premises

For all 15625 checkpoints, verify all five involutions, trace laws
z,-z,2-z,2-z,3-z, the declared (q,r) laws, and fixed counts
(625,25,25,1,1). Check the sole d/e fixed tuples
(1,3,4,2,3,3) and (1,3,4,2,1,3). For both bits the selected trace tables
are (0,4,0,4,4) and (2,1,1,3,1); the initial bits are 0,1,1 and every
trace reaches 1 after them. The synchronized target trace is 4+2t mod 5.
These are inherited premises and are not claimed as new results.

### F2: field identities and complete image

Audit A_f^5=I, L=(I-A_f)(I-A_f^2), A_f L=L A_f,
L^2=5A_f^3, Vinv=A_f^2 L, Vinv L=L Vinv=5I,
L^t B_f L=5B_f, det L=25, det Vh=1, and the canonical product
L Vh with two blocks [[5,3],[0,1]]. Exhaust all 625 input residues:
image(L mod 5)=C, |C|=25, each image has 25 preimages, and
Vinv y=0 mod 5 iff y is in C. For each of the 25 representatives in C,
Vinv y/5 is integral and maps exactly to y under L.

### F3: fixed comparison

On all 625 pistons W is an involution and equals the piston action of a;
h=(W0+2W1,W2+2W3); h=0 iff W(p) is in C. The 25-point piston kernel maps
bijectively onto C. Check H(e0)=2 and H(W e0)=3, |G|=625,
|G intersect X_s|=125 for each s and |G14|=250.

### F4: generator action on the gate

For all 15625 states verify

    h(bx)=-J2 h(x), h(dx)=h(ex)=-h(x),
    h(cx)=-J2 h(x)+(r,-r),
    h(ax)=(p1+2p4,p1p+2p4p)=2h(x)+2(p1,p1p).

On pistons (h,h after a) takes 625 distinct values. The zero tuple and
(1,3,0,0,0,0) have the same h but give different h after a. Of the gated
states a retains exactly 25, precisely those with zero pistons; c retains
exactly 125, precisely those with r=0. The generators b,d,e preserve both
G and its complement. Gate preservation does not mean pointwise fixation.

### F5: complete selector table

On all 31250 pairs (x,t), compare generator, trace and h against these rows,
where k=h(ax) and Rr=(r,-r):

| t | z | generator | next z | next h |
|---|---|---|---|---|
| 0 | 0 | a | 0 | k |
| 0 | 1 | b | 4 | -J2 h |
| 0 | 2 | c | 0 | -J2 h+Rr |
| 0 | 3 | d | 4 | -h |
| 0 | 4 | e | 4 | -h |
| 1 | 0 | c | 2 | -J2 h+Rr |
| 1 | 1 | d | 1 | -h |
| 1 | 2 | e | 1 | -h |
| 1 | 3 | a | 3 | k |
| 1 | 4 | b | 1 | -J2 h |

### F6: absorbing synchronized part

On all 12500 synchronized state/bit pairs verify the complete inductive
step: selected generator b,d or e, next trace 4+2t, and next h=-h or
-J2 h. G14 and its complement inside X14 are preserved. For each t the
image of G14 is the corresponding 125-point gated sheet, with exactly
two preimages per image. There is one fixed point of T_t on X14 (the
e point for t=0, d point for t=1), both gated; each T_t moves 249 points
of G14. The written induction, rather than a finite trajectory sample,
establishes the corresponding all-future assertion.

### F7: inherited invariant and scope

Use the canonical V=(p1+p1p,p4+p4p,
chi(z)(p1-p1p-2),chi(z)(p4-p4p-1)), chi(1)=1, chi(4)=-1.
On every synchronized state/bit pair V(next)=-V. Every V value has ten
preimages in X14. The gate is the V-preimage of
S={v:2v0+v1=2v2+v3=0}; S has 25 vectors. G14 comprises exactly 13
canonical sign fibres {V,-V}, one of size 10 and twelve of size 20.
The already established V law and sign-fibre classification are credited
as inheritance, not a new invariant or a new physical memory law.

### F8: full origin-prefix classification

For zero initial state the prefix is
(0,0,0,0,0,0), (0,0,0,0,0,0), (2,1,2,1,1,0), (0,0,1,3,1,1),
with words a,c,e, traces 0,0,2,1, h=0 throughout and r3=1.
For every initial checkpoint, the sheet words s=0,...,4 are
ace, bbd, cce, dbd, ebd. Write h=h0, k=h(a x0), Rr=(r0,-r0):

| initial sheet | h1 | h2 | h3 |
|---|---|---|---|
| 0 | k | -J2 k+Rr | J2 k-Rr |
| 1 | -J2 h | h | -h |
| 2 | -J2 h+Rr | h | -h |
| 3 | -h | J2 h | -J2 h |
| 4 | -h | J2 h | -J2 h |

All states have z3=1. Exactly 125 per initial sheet have h3=0.
On X0, h0=h3=0 holds at precisely
(p1,p4,p1p,p4p,q,r)=(2r,r,3r,4r,4r,r), five tuples; each one-sided
difference of the initial and boundary-three gates has size 120.
Among the initially gated states the separate boundary counts n=0,1,2,3
are (125,5,5,5) on X0, (125,25,125,125) on X2, and 125 at every
boundary on X1,X3,X4. These separate counts are not cumulative survival.
The all-four-boundary intersections have sizes 1,125,25,125,125,
total 401. Induction from F6 proves permanent gate membership precisely
for those 401 states. Eventual gate membership from n=3 holds for 625
states, with 125 from each initial sheet.

### F9: explicitly finite regression

The actual zero orbit through n=4096 is gated at all 4097 boundaries and
synchronized at n>=3. For all 15625 initial states through n=40, at every
3<=n<=40 check h_n=0 iff h3=0 and
h_n in {h3,-h3,J2 h3,-J2 h3}. This finite regression is not a proof of
an infinite-time claim. SHA-256 digests of the sorted G14 and sorted 401
permanently gated initial tuples use comma-separated decimal residues,
one LF-terminated row per tuple; record them without a preselected digest.

## 4. Systematics and admissible inference

All matrix checks use exact integer algebra;
checkpoint arithmetic uses residues 0 through 4. There is no floating
point, randomness, external solver, data fitting, tolerance or adjustable
threshold. Complete exhaustion decides the finite predicates. PROOF.md
provides algebraic rank/count arguments and the all-time induction.
Exact gate membership is distinct from zero piston, fixed point,
integer-state lifting, energy availability and physical actuation.

## 5. Pin, failure and prescribed execution

Before the first run freeze, commit, push and read back PREREG.md,
PROOF.md, verify.py, SOURCES.tsv and INPUTS.sha256. The immutable commit
and every initial file hash must agree. Record the pin in the public
claim. Compilation or static parsing before that pin is not execution.

The first failed frozen scientific predicate prints its falsifier and
witness and RESULT FAIL, stops dependent work and exits zero. A zero exit
alone is not PASS. An exception, nonzero exit, nonempty stderr, custody
failure or timeout is an execution failure and receives the consumed-pin
disposition prescribed by POLICY.md. Neither a scientific negative nor an
execution defect is repaired by changing a frozen source or threshold.

The first run is the AGENTS.md section 6 repository-root command:

    python3 probes/P-U-AFRAME-GATE-AUDIT-1/verify.py

Use the existing deterministic environment LC_ALL=C, LANG=C, TZ=UTC,
PYTHONHASHSEED=0, PYTHONDONTWRITEBYTECODE=1 and the repository's 600-second
per-verifier limit. Save exact stdout as EXPECTED.txt and the neutral
execution fields in RUN.md; record status/scope in RESULT.md. Only after
the first run is recorded and committed may the author comparison begin.
The unchanged tools/check_verifier.py --base FULL_BASE_SHA then reproduces
the completed record, and the existing PR workflow provides both required
architectures and their aggregate check. No local repeated run is called
a new independent confirmation.

## 6. Action layer and excluded conclusions

L1 only. This is a distinct-owner independent audit of an explicitly
selected residue-level comparison. It does not derive a universal integer
lift of U, a native choice of a minimum-energy representative, an H-isometry
of W, a physical source or port, an energy-funded contact, a realized
message transfer, a seventh independent trace register, or global
bijectivity of the state-selected update. Inherited canonical facts retain
their existing scopes. Current authority remains Public Canon v102.

No Canon, registry, frontier, gate, old probe, author source, workflow,
limit, release or main modification is part of this audit. The separate
draft PR changes only this probe directory. Its review is submitted to a
different controller; this session does not accept its own work.
