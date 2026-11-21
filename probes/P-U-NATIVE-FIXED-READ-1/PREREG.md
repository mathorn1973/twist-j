# P-U-NATIVE-FIXED-READ-1 — preregistration

Status: PUBLIC, NON-CANONICAL. Action layer: L1 only.
Owner: A. M. Thorn / native-fixed-read-20261009.
Reservation: [issue #1429](https://github.com/mathorn1973/twist-j/issues/1429).
Branch: probe/P-U-NATIVE-FIXED-READ-1.
Date: 2026-10-09, Europe/Prague.

This is an audit of disclosed, manually derived mathematical claims.
The expected conclusions were known to both implementations before execution.
No measurement data or numerical outcome was inspected to choose these readers.
The first scientific execution must follow a committed, pushed and publicly
read-back pin of this entire input package. Static parsing and administrative
hashing do not execute the scientific programs.

## 1. Authority, source and prior ownership

Public main is c164b79ce134152ac7cd600421791df74113f29f, Public Canon v100 ACTIVE.
The declared content commit a4cc9666662967527abe711441833ff600c00337 and
canon-v100 target are ancestors of that main. Fresh readback confirmed all five
normative SHA-256 values. CANON.md has 980212 bytes and SHA-256
5e4de2da8d57ff2f7e4b873e6236b0695677e20d173d894ee70562c1389648c4.
Required main checks passed in workflow 37855930685.

The probe transcribes the native generators and selector from that immutable
source; it imports no predecessor scientific program and reads no mutable Canon
at run time. Its complete runtime inputs are the files in INPUTS.sha256.
The pinned Git tree additionally binds that manifest.

Actual H0 word a,c,e and an occupied-receiver controlled translation are
inherited from [#1001](https://github.com/mathorn1973/twist-j/issues/1001#issuecomment-5666743909).
Blank-receiver persistent native writing is inherited from
[#999](https://github.com/mathorn1973/twist-j/issues/999#issuecomment-5662855170).
The protected invariant and the synchronized no-write theorem are inherited
from [MEMORY-PROOF.md](https://github.com/mathorn1973/twist-j/blob/c164b79ce134152ac7cd600421791df74113f29f/probes/P-U-NATIVE-MEMORY-EVENT-1/MEMORY-PROOF.md).
The opposite piston-source/fibre-receiver affine class is already excluded by
P-U-EARLY-SOURCE-FIBRE-CONTACT-1 and C-U-CONTACT-RENEWAL-BOUNDARIES-N.

The new scope combines an independently occupied receiver, the SAME local
reader before and after actual native writing, permanent later reading, and
a complete declared affine preparation family. M is a polynomial of the
existing protected record, not a newly discovered invariant.
The scalar coefficients coincide with factors in
[PR #1428](https://github.com/mathorn1973/twist-j/pull/1428), head
9de862afafd02ea3e49daf6e4567127dc2a01f2c; this does not implement its complete
three-cell gates or compose them.

Preflight searched the public tree, probes, notes, registry, exact issue name,
related issue scopes and all 223 actual remote heads. No exact identifier
collision was found. This covers neither private/deleted/unattached work nor
a semantic audit of every unrelated object. The issue was claimed before any
new file commit.

## 2. Equation and complete carrier

All arithmetic is exact in F5, representatives 0,1,2,3,4. The carrier is
Omega=N0 x F5^6, with coordinates (n,p1,p4,p1p,p4p,q,r). The native law is

\[
U(n,v)=(n+1,g_{z(v)+2\theta_n}(v)),\qquad
z(v)=\sum_i v_i,\quad\theta_n=\operatorname{popcount}(n)\bmod2,
\]

where (g0,g1,g2,g3,g4)=(a,b,c,d,e) are written in full in PROOF.md and
independently transcribed in both programs. No freely selected generator,
HOLD, reset, new clock, extra register or intercell gate is substituted.

For the positive results the launch time is exactly zero. The first three
actual bits are 011. Define

\[
S=p_1+p_4+p'_1+p'_4,\quad
X=2(r-q)+1,\quad
M=2[(p_1-1)(p_4-3)+(p'_1-4)(p'_4-2)].
\]

The source fibre is (q,r)=(u+4,4u+1); the receiver depends only on y.
All admissible affine receiver maps to be classified are p(y)=p0+yv with
p0,v in ker S, satisfying M(p(y))=y for every y and an affine native output
M(U^3 E(u,y))=Ay+Bu+C for every independent pair u,y in F5.

This class is fixed before enumeration. Its prospective complete answer is
20 receiver maps, with exactly four satisfying A+B=1 and C=0:

| p0 | v | A | B | C |
| --- | --- | ---: | ---: | ---: |
| (3,3,4,0) | (4,0,1,0) | 3 | 3 | 0 |
| (2,2,2,4) | (4,0,1,0) | 3 | 3 | 0 |
| (0,3,4,3) | (2,0,3,0) | 2 | 4 | 0 |
| (3,1,0,1) | (2,0,3,0) | 2 | 4 | 0 |

A+B=1 and C=0 are additional declared coefficient conditions, not a
physical selection principle. Completeness concerns this entire affine
class with these fixed readers, not every preparation or physical law.

## 3. Further positive claims and required counterexamples

For independent s,t use

\[
E_{\rm SUM}(s,t)=(t,0,-t,0,-s,s),\quad
\sigma=3(r-q),\quad
R=(1-S^2)(p_1+p'_4)+S^2 M.
\]

The SAME R reads t before and t+s at every time n>=3. Sigma reads s before
and at time three. No later permanent source reading is asserted.

On the first and third rows of the table only, let

\[
K=(p_1-1)^2+(p'_1-4)^2,\quad
T=(1-S^2)\,2p'_4+S^2\,2(K-1).
\]

This fixed receiver-local reader has T=0 on P and T=1 on Q before, after
the complete three-tick operation, and at every later time. The two chosen
preparation families contain 50 inputs. Their endpoint law is

\[
(X',M',T')=(X,(3-T)M+(3+T)X,T).
\]

The pair (X,M) alone must fail to determine that endpoint response:
the two input states (3,3,4,0,0,0) and (0,3,4,3,0,0) both read (1,0),
but the actual output receiver readings are respectively 3 and 4.
The complete corresponding outputs are frozen in PROOF.md and both programs.

The counterexample at the INTERNAL first tick is also mandatory:
for P at u=1,y=0, T at times 0,1,2,3 is (0,3,0,0).
Generally that first-tick value is 2y+3 on P and y+3 on Q.
Thus this is not an uninterrupted binary pointer. The endpoint law is not
iterable on its own outputs, because later M is invariant.
T does not realize the different energy-contact label from PR #1424.

## 4. Exact finite audits and independent methods

The primary program uses direct raw-coordinate formulas, full state selection and
literal evaluations. The independent program uses separately written homogeneous
7x7 matrices, composition and quadratic-form congruences. It was written
and hashed before the author opened primary.py; the review record states
the exposure chronology. Neither implementation is blind to the claims.

Both programs and the wrapper are standard-library Python. The domains
are fixed as follows:

1. Primary: all 15625 initial six-coordinate states and all three selected
   origin steps, with exact words on every initial trace sheet. Both:
   all 3125 H0 states compared with the full affine a,c,e word.
2. Primary: all 625 piston states under b,d,e, giving 1875 M and K
   preservation checks. Independent: exact whole-space quadratic-form
   congruences. Both verify selected stable-alphabet closure. These
   identities, together with the written induction, prove every later time;
   no bounded trajectory census is promoted to an infinite-time theorem.
3. All 125 p0 times 125 v in ker S, including zero directions: 15625
   affine candidates. Primary evaluates all y and the complete (u,y)
   output table of every line passing the input condition. Independent
   compares exact pulled-back quadratic forms. Both compare the complete
   surviving 20-row table with the analytic formula, including offsets.
4. All 100 native inputs of the four accepted coefficient templates.
5. All 25 independent SUM inputs.
6. All 50 context inputs, the common-read/different-output witness, and the
   failed first internal context reading.
7. All 90 ordered partitions into three labelled raw pairs, under all four
   possible piston permutations: 360 maximal dependency cases. No case
   may retain both donor dependencies and all three receiver dependencies.

The wrapper checks input hashes, isolated subprocess exits, empty stderr,
ASCII/LF JSON, status PASS, all common counts, complete template lists and
the explicit witnesses. It emits both actual reports in one deterministic
JSON line. Its two program timeouts are 270 seconds each within the
repository's unchanged 600-second verifier budget.

PROOF.md also gives an arbitrary-time common-clock multiset theorem for
whole-cell permutations and a 3125-state necessary bank bound.
VARIABLE-TRACE.md contains a separately reviewed analytic extension for
receiver (q,r), two piston donor pairs, arbitrary nonlinear product codes
and the SAME local readers at every fixed origin-zero duration.
AFFINE-THREE-PORT.md extends exclusion to every partition into three raw
pairs with affine independent codes, varying initial traces, arbitrary
nonlinear local readers and every fixed origin-zero duration. Other block
sizes, nonlinear preparations at other receiver positions, other launch
times and input-dependent stopping remain outside that extension.
These are written proofs; the finite program does not claim to enumerate
their unbounded durations or arbitrary nonlinear preparation functions.

## 5. Systematics, failure threshold and disposition

There is no tolerance, floating-point estimate, fit, random seed, detector
postselection or empirical data. Every equation must hold exactly on its
declared complete domain. In particular:

- a wrong native word or any mismatching raw output rejects the claimed
  source realization;
- a missing/additional affine line, coefficient or template rejects the
  completeness claim;
- any failed local input/output equality or invariant identity rejects
  the relevant reading or retention claim;
- a maximal dependency survivor rejects the stated dependency exclusion;
- absence of either declared ambiguity witness rejects that counterexample;
- cross-method disagreement is a failed audit, not a successful construction.

A hash mismatch, malformed report, timeout or execution defect is recorded
as an integrity/execution failure, not silently as a mathematical result.
Preserve the first outcome, exact streams, timestamps and input hashes.
Do not repair a pinned program or move a threshold after that run.
A completed successful audit yields EXPECTED.txt, RUN.md and RESULT.md.
If the pin never completes, preserve it and close its consumed identifier
under POLICY.md's abandoned-pin procedure, retaining the failure description.
An identified mathematical falsifier is not suppressed by that disposition.

## 6. Action layer and allowed conclusion

The strongest intended status is NON-CANONICAL, candidate-T, L1, backed by
separate assistant review and exact finite audits. The public required
x86_64/aarch64 jobs must reproduce the same EXPECTED.txt and verifier hash.
One local architecture alone is not that computation gate.

No physical preparation, physical subsystem assignment, apparatus access,
energy calibration, renewable native operation, full three-cell contact,
Hilbert coherence, photon phase, occurrence law or empirical adequacy is
closed. The missing preparation and connection mechanisms remain explicit.
No Canon, registry, frontier, workflow, merge or release change is authorized
by this probe.
