# Six-field preregistration and frozen falsifiers

PUBLIC / NON-CANONICAL / L1. Issue #1550; program #1548 lane A.
Owner Claude-20261016-v103-aframe-gate; author A. M. Thorn, Apache-2.0.
Authority main = canon-v102 = a632c6a162dc87e60104d7a478e7650a6d5c4a1b,
content b04e22dd3ed8e4240cff347364f24670d4183a4d, Public Canon v102.
The STATUS fields, tag ancestry, five normative hashes and successful main
and tag checks were verified in this session; SOURCES.tsv binds them. The
release-event check of #1544 must have a recorded success before the first
formal execution; otherwise the run is STOP, not substituted.

## 1. Equation and exact contract

Checkpoint x=(p1,p4,p1p,p4p,q,r) in F5^6, trace z=sum(x), the five v102
generators a..e of DEF-NATIVE-WORD-CURVATURE-CLASS, selector
T_t(x)=g_(z+2t mod 5)(x), driver theta_n=popcount(n) mod 2, actual update
x_(n+1)=T_(theta_n)(x_n) from counter origin n=0. Fixed comparison map
W(p1,p4,p1p,p4p)=(p4,p1,p4p,p1p) to the field marking (a,b,c,d) of
FIELD-CHAIN-FIRST-WORK shared proof 2, h=(p4+2p1,p4p+2p1p) in F5^2,
J(u,v)=(v,u), zero gate G={h=0}, X_s={z=s}, X14=X_1 u X_4, G14=G n X14,
C={y in F5^4: y0+2y1=0, y2+2y3=0}. Field matrices A_f, B_f, L, Vinv, Vh and
H(y)=y^t B_f y/2 are copied unchanged from that shared proof.

Questions decided: (i) the exposed laws h(bx)=-Jh, h(dx)=h(ex)=-h,
h(cx)=-Jh+(r,-r) on every checkpoint; (ii) the actual a action and whether
any h-only law exists for it; (iii) the residue image of L and its relation
to W and G; (iv) every selector branch; (v) all-future gate membership on
the synchronized sheet by induction, separated from pointwise fixation;
(vi) the explicit origin-zero prefix and the exact set of initial
checkpoints gated from n=3 and at every n>=0; (vii) which parts are
inherited from U-NATIVE-INVARIANT-AND-NOWRITE. Targets (i) are exposed in
#1548; this is not a blind prediction.

## 2. Code and custody

verify.py is the sole new verifier, standard library only, written for
this probe; no prior verifier or exploratory program is imported, copied
or executed. PROOF.md is the analytic proof, written before code. The
all-time statement is proved by induction in PROOF.md; verify.py checks
its base and its inductive step on the complete finite domain and audits
every other finite predicate exhaustively. INPUTS.sha256 binds all initial
files except itself, which the public Git pin binds. Before the first
scientific execution, import, dry run or benchmark, commit, push and
publicly read back all initial files byte for byte. Compilation, static
syntax checks, hashing and written algebraic review are allowed before.

## 3. Complete carrier and nine falsifiers

Exact integers and F5 residues only. Domains are complete: 15625
checkpoints, 31250 checkpoint-bit pairs, 625 pistons and 625 residues.

F1 inherited native premises: every generator is an involution on all
15625 checkpoints; trace laws a:z, b:-z, c:2-z, d:2-z, e:3-z; (q,r) laws
a:(q,r), b:(-q,-r), c:(1-q,-r), d:(1-q,1-r), e:(2-q,1-r); selected sheet
maps T_0=(0,4,0,4,4), T_1=(2,1,1,3,1); fixed-point counts 625,25,25,1,1
with fixed points d:(1,3,4,2,3,3), e:(1,3,4,2,1,3); theta_0..2=0,1,1;
every trace reaches 1 after the bits 0,1,1; T_t(X14) lies in
X_(4+2t mod 5) for both t.

F2 field algebra and L image: exact integer identities A_f^5=I,
L=(I-A_f)(I-A_f^2), A_f L=L A_f, L^2=5A_f^3, Vinv=A_f^2 L,
Vinv L=L Vinv=5I, L^t B_f L=5B_f, det L=25, det Vh=1 and
L Vh=[[5,3,0,0],[0,1,0,0],[0,0,5,3],[0,0,0,1]]. Over all 625 residues the
image of L mod 5 equals C, |C|=25, every image residue has 25 preimages;
Vinv y=0 mod 5 iff y in C; for every representative y in C,
x=Vinv y/5 is integral and Lx=y exactly.

F3 comparison map and gate: W is an involution equal to the piston action
of a; h(p)=(W0+2W1,W2+2W3) on all 625 pistons; h(p)=0 iff W(p) in C;
W maps the 25-element ker h bijectively onto C; H(e0)=2, H(W e0)=3;
|G|=625, |G n X_s|=125 for every s, |G14|=250.

F4 generator laws on all 15625 checkpoints: the three exposed b,d,e laws
and the c law (i); the a law h(ax)=(p1+2p4,p1p+2p4p)=2h+2(p1,p1p);
p->(h(p),h(ap)) takes 625 distinct values; witness x=0 and
x'=(1,3,0,0,0,0) with equal h=0 and h(ax)=(0,0), h(ax')=(2,0); a keeps
exactly 25 gated checkpoints, all with zero piston; c keeps exactly the
125 gated checkpoints with r=0; b,d,e each map G into G and its complement
into its complement.

F5 every branch: on all 31250 pairs (x,t) the selected index z+2t mod 5,
next trace and next h equal the ten-row table of PROOF.md section 4.

F6 absorbing sheet: on all 12500 pairs with x in X14, next x lies in
X_(4+2t mod 5), the generator is b,d or e, next h is -Jh for b and -h for
d,e; G14 and X14\G14 are each mapped into themselves; T_t(G14) equals
G n X_(4+2t mod 5) with exactly two preimages per image point; T_t has
exactly one fixed point on X14, (1,3,4,2,1,3) for t=0 and (1,3,4,2,3,3)
for t=1, both in G14; each T_t moves exactly 249 points of G14.

F7 inherited V relation: with V=(p1+p1p,p4+p4p,chi(z)(p1-p1p-2),
chi(z)(p4-p4p-1)), chi(1)=1, chi(4)=-1: V(T_t x)=-V(x) on all 12500
pairs; G14 equals the V-preimage of S={2v1+v2=0, 2v3+v4=0}; every V value
has exactly 10 preimages in X14; G14 is the union of exactly 13 fibres of
R={V,-V}, one of size 10 and twelve of size 20.

F8 origin-zero prefix: from x0=0 the states are (0,0,0,0,0,0),
(0,0,0,0,0,0), (2,1,2,1,1,0), (0,0,1,3,1,1), generators a,c,e, traces
0,0,2,1, h=0 at n=0..3 and r3=1. For all 15625 initial checkpoints: the
words on sheets 0..4 are ace,bbd,cce,dbd,ebd; h1,h2,h3 equal the table of
PROOF.md section 6; z3=1; 125 checkpoints of every sheet have h3=0; on X0
the h0=0/h3=0 overlap is 5 with p=(2r,r,3r,4r), q=4r, and each one-sided
difference is 120; initially gated checkpoints still gated at n=0,1,2,3
number s0:125,5,5,5; s1:125 each; s2:125,25,125,125; s3,s4:125 each;
gated at all of n=0..3: 1,125,25,125,125, total 401, the X0 one being 0.

F9 finite regression, labelled not a proof: the actual zero orbit for
n=0..4096 has h=0 at all 4097 checkpoints and lies in X14 for n>=3; from
all 15625 initial checkpoints for n=0..40, for 3<=n<=40, h_n=0 iff h_3=0
and h_n is in {h_3,-h_3,Jh_3,-Jh_3}.

Two digests are computed and recorded, not compared with a frozen value:
SHA-256 of the sorted G14 tuples and of the sorted 401 permanently gated
initial checkpoints, one LF-terminated comma-separated row per tuple.

## 4. Systematics and inference

Standard-library Python, deterministic integer residues, no tolerance,
randomness, solver, network, floating arithmetic or mutable input. Finite
exhaustion decides finite predicates. All-time gate membership follows only
from the induction in PROOF.md (step checked on all of X14 x {0,1}), never
from F9. The zero gate, the zero piston and pointwise fixation are kept
distinct. Inherited claims are rechecked as dependencies; novelty against
them is decided in RESULT.md and an inherited corollary stays inherited.

## 5. Failure and execution

The first failed frozen predicate prints its falsifier FAIL line and
RESULT FAIL, stops dependent checks and exits 0 with that exact transcript
as the scientific record; exit 0 alone never means PASS. A custody
mismatch, exception, nonzero exit, stderr or timeout is an execution
failure, not a scientific negative, and receives the repository's
consumed-pin disposition. No threshold change, input repair or hidden
rerun after the pin. After public readback and the release-check success,
from a clean Linux repository root at the pin, execute

    python3 probes/P-U-AFRAME-GATE-1/verify.py

with LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1.
Record EXPECTED.txt, RUN.md and RESULT.md; one draft PR changing only this
probe directory; unchanged required x86_64/aarch64 replay. No merge.

## 6. Action layer and scope

L1 only: exact residue-level compatibility of actual native U with the
field image gate. Not asserted: a universal integer lift of U, an
H-isometry of W, a physical port or contact, a source preparation, energy
minimum, r=0 for all n, an affine trace law, or z as a seventh register.
x_n is an F5 checkpoint, not a Z^6 trajectory. No Canon, registry,
frontier, gate, workflow, old probe or v102 release change.
