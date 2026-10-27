# C-FIELD-L5-ENERGY-FUNDED-COUPLING-N: frozen local law

PUBLIC / NON-CANONICAL incubation. Authority: none. Action layer: L1.
Owner: A. M. Thorn / codex-field-l5-energy-funded-coupling-20261001.
Reservation: issue #1305. One notes candidate and one standard reproduction.

## Authority, authorization, exposure and sources

The user explicitly authorized this separate coupling successor after the
reviewed field-window audit. Public main remains
b8ba1a07ad776cdd8d878fe0a407e07312c0e263, declaring Canon v95 content
5a1dd8ba6c339640940b5a013d3c412025a1f8fc. Annotated canon-v95 object
7810207b27539ee35e30ffb0ed81cec32fa322c7 peels to main. Immutable
published release 400415362 and its two asset hashes were read back;
main run 36766242516, tag run 36769404870 and release run 36773377591
remain successful. Content and activation are ancestors of public main.
STATUS/POLICY/AGENTS bytes are unchanged; current CORE/FRONTIER, relevant
registry/evidence/dependencies/gates and inline proofs were inspected.

Fresh collision scan: explicit `git ls-remote --heads origin`, 176 heads;
all 208 open issue/PR records; exact new names absent, searches complete;
notes/probes/reproduce/registry inspected. Adjacent memory, native-budget,
TT-exchange, QS and Galois coupling lanes concern different objects.

The predecessor C-FIELD-CYCLOTOMIC-WINDOW-AUDIT-N, PR #1304, remains an
open draft at dcfde46760bdfd4551686be1e99b5433fa6e9adf. Its reviewed
NON-CANONICAL disposition is PASS, including actual x86_64/aarch64 replay
in final run 36784630463. Its PROOF.md SHA-256 is
d9cde5b2182fbd8526865c1117730099b91d2fa1a0d78e059b3707abacffeb78.
It is an explicitly pinned public candidate input, not Canon authority;
this successor neither merges nor promotes it. Older #1302 failures stay
unchanged. All definitions needed below are restated; no predecessor code
or private archive is a runtime dependency.

Canonical sources at base (SHA-256):

| source | hash |
| --- | --- |
| canon/CANON.md | b4ebf2ffc7393b703d65ce62cf3e0ee382e7309a563d99ec866ee3fa82f9ba7f |
| canon/REGISTRY.tsv | a2abce1a4538785ac6a7c7874c2366a3531d460027188510394930c6d222559a |
| canon/EVIDENCE.tsv | 1258ea3dd14a5e2b512b69b08ac647626d4fac169a1ba0b6cd770832bb735600 |
| canon/DEPENDENCIES.tsv | c1b0cee2b9e320ed05ba4004da3a2265cbd2bbafe45dd18f59fb29790d477214 |
| canon/GATES.tsv | 85f7db365ff38988dbf2a994f4d8d0ba380ac00d368bcc50e4313daee9aff744 |
| notes/INTEGER-AUTOMATON-COMPOSITION-PROGRAM.md | 354c4b5292c89ab521654a642f056c39f4c99e688b5e34891369c23980d9dfd7 |

Inherited inputs: INTEGER-F-JG-INVARIANTS supplies phase coordinates,
chi and the chosen quadratic family; INTEGER-ENERGY-FUNDED-INVOLUTION
already proves the generic funded involution; FIELD-GAUSS-CONTACT-MEMORY
supplies nodewise continuity/defect bookkeeping; FIELD-EISENSTEIN-RESONANCE
already gives the chosen R18/A20/P14 matter energies and triangle channel.
This task instantiates those facts with the distinct L5 image and its exact
four-unit account. It does not rediscover the generic lift or replace the
old triangle law. The P14 reaction is not installed.

The field matrices, image, charged split and prior failures were exposed
before this task. The coupling equations, charged witness and period-ten
consequence were derived symbolically while drafting, without running a
scientific program. They are exposed targets, not blind predictions.
The earlier unlocated memo/programs are not claimed as reproduced sources.

## Complete state, equality, geometry and energy

One finite oriented multigraph has vertices 0,1,2 and ordered edges
e0:0->1, e1:0->1, e2:0->2, e3:2->1. The first two edges are distinct
parallel edges. Faces: c0=e0-e1, c1=-e0+e2+e3. Boundary is +tail/-head.

```text
C=[[1,-1],[-1,0],[0,1],[0,1]],
D=[[1,1,1,0],[-1,-1,0,-1],[0,0,-1,1]], DC=0.
```

The full state is (m,b,z,r), where m=(m0,m1,m2) is an ordered triple
of Z4 matter registers at vertex0; b=(b0,b1,b2) are three untouched Z4
spectator matter registers, one at each corresponding vertex; raw field
z=(E0,E1,E2,E3,M0,M1) is in Z6; r is a stored neutral integer >=0 at
vertex0. There are 31 integer coordinates, the last constrained nonnegative.
No unstored phase, hidden history or external energy ledger is allowed.
Equality is literal on this full ordered state, never modulo phase, routing,
charge or energy. The Gauss-admitted subset is defined below; the full map
must also preserve defects outside it.

For a matter phase vector v in Z4, chi(v)=sum_i v_i and Q(v)=v^t K v:

```text
K=[[6,2,-1,2],[2,6,2,-1],[-1,2,6,2],[2,-1,2,6]].
```

This is the selected (A,B,C)=(6,2,-1) member of the canonical family,
with positive eigenvalues 9,1,7,7; neither physical energy nor measured
charge is identified by this choice. All matter vectors here use the
canonical four-phase chart, not field active coordinates by implication.

```text
Hraw(E,M)=E^t E+M^t M+E^t C M,
Htotal(m,b,z,r)=sum_j Q(mj)+sum_j Q(bj)+Hraw(z)+r,
rho=(chi(b0)+sum_j chi(mj), chi(b1), chi(b2)),
defect(m,b,z,r)=D E-rho.
```

The reservoir and spectators are real stored coordinates of this declared
mathematical architecture, and their full energies are counted. Prove
nonnegative total energy and preservation of the complete defect vector.
The subset DE=rho is therefore invariant; no rounding, charge relabeling
or imposed zero-charge simplification is allowed. All three reacting matter
registers are co-located: no edge matter transport or current is present.

## Exact field admission and fixed matter endpoints

The active embedding, static embedding and active energy are

```text
P(a,b,c,d)=(a-b,-a,b,b,c,d), S(u,v)=(u,u,v,u-v,0,0),
A=[[1,0,1,0],[0,1,0,1],[-2,1,-1,1],[1,-3,1,-2]],
B=[[4,-2,2,-1],[-2,6,-1,3],[2,-1,2,0],[-1,3,0,2]], H(x)=x^t B x/2,
L=[[1,-3,-1,-2],[-3,4,-2,1],[0,5,1,2],[5,-5,2,-1]],
N=[[1,2,1,2],[2,-1,2,-1],[0,-5,1,-3],[-5,5,-3,4]].
```

Use exact certificates A^5=I, A^t B A=B, L=(I-A)(I-A^2),
AL=LA, N=A^2 L, NL=LN=5I, L^t B L=5B and det L=25.
P and S separately generate saturated lattices; their sum has index5.
The exact integer split z=P y+S s exists iff
g(E)=2E0-3E1+E2+E3=0 mod5. Reject before division otherwise.
On admission its coordinates are

```text
a=(2E0-3E1+E2+E3)/5, b=(-E0-E1+2E2+2E3)/5,
c=M0, d=M1,
u=(2E0+2E1+E2+E3)/5, v=(E0+E1+3E2-2E3)/5.
```

These give y=(a,b,c,d), s=(u,v). Each division is exact on admission.
Hraw(P y+S s)=H(y)+3u^2-2uv+2v^2. Actual field divergence is D E;
it equals (2u+v,-3u+v,u-2v) on the split domain.

An active y=(a,b,c,d) belongs to L Z4 iff a+2b=0 AND c+2d=0 mod5.
Only then form x=Ny/5. The inverse preserves the complete active vector;
there is no missing phase on the admitted image. Whole-shell membership
in H=5 does not imply this exact image admission.

Fix ONLY matter phase i=0. With e0,...,e3 the standard Z4 vectors,

```text
R=(e0-2e1+e2, 0, 0),
A_matter=(e0, -e1, e2-e1).
```

Their additive energies are 18 and20, and both full vector sums are
e0-2e1+e2. Their node0 total chi is zero. The individual register charges
need not be conserved; their ordered patterns retain the reaction branch.
No extra branch bit is needed because these two endpoint tuples are disjoint.
Other phases, permutations and reactions are outside the switching rule.

## Total funded gate and selected complete cell step

Define G on EVERY full integer state, retaining b exactly:

1. If m=R, require integral split z=P y+S s and y in L Z4. Set
   x=Ny/5, h=H(x), r_new=r+4h-2. If r_new>=0, return
   (A_matter,b,P x+S s,r_new).
2. If m=A_matter, require integral split z=P x+S s. Set
   h=H(x), r_new=r+2-4h. If r_new>=0, return
   (R,b,P Lx+S s,r_new).
3. Every failed endpoint, split, image or funding condition fixes the
   ENTIRE input state. No partial update or reservoir clipping is permitted.

Prove this total G is an involution, preserves Htotal, the full matter
vector sum, b and each component of D E-rho, and keeps integer r>=0.
The static s remains stored and unchanged. Its energy is not multiplied.
G instantiates the inherited funded-involution theorem after constructing
the exact unfunded endpoint/image pairing; it is not a new generic theorem.

For h=0 the R branch requires r>=2 and the A_matter branch releases two.
For h>=1, R always admits funding and deposits4h-2; the inverse needs
r>=4h-2. In particular h=1 deposits TWO surplus units after paying the
two-unit matter increase. Zero-field reservoir-funded activation is allowed
by this selected rule and must not be hidden as purely field-funded behavior.

Define the selected free field step F, leaving m,b,r fixed:

```text
T(E,M)=(E+CM, M-C^t(E+CM)),
T^-1(E',M')=((I-CC^t)E'-CM', C^t E'+M'),
F(m,b,z,r)=(m,b,Tz,r), Ucell=F after G,
Ucell^-1=G after F^-1.
```

Prove the composed map preserves the same state space, energy and pointwise
Gauss defect. For this specific law F and G commute: A preserves energy
and image admission, L commutes with A, and static/split/funding data are
retained. With F^5=I and G^2=I, the proposed complete-state identities are
Ucell^5=G and Ucell^10=I. Verify or refute them, and the explicit period10
witness below. This is a predicted algebraic limitation, not a trajectory
search or a claim of waiting time, irreversible activation, emission,
persistent writing or transport. Ucell is not the native canonical U.

Local access: all four edge and two face field registers of this one fixed
cell, the ordered reacting triple and reservoir at vertex0. Spectators are
unchanged. The free step uses the same field cell. No outside state is read
or changed; inverse has the same finite support. This specifies finite-cell
locality only, not a one-edge substep implementation, a global parallel
schedule, or compatibility of overlapping cells.

## Frozen witnesses, finite audit and failure conditions

No shell enumeration or unrestricted trajectory search is admitted. The
following exact witnesses and finite domains are fixed before execution.
They audit the universal algebraic proof; they are not a completeness claim
for all possible preparations or reaction architectures.

1. Check the field, split, image, energy and matter certificates above.
   Reconstruct the actual D from the oriented endpoints. Check the canonical
   R/A energies and full vector sums, positive matter and field metrics,
   the integral split identities, and the retained static energy.
2. Let x range over {-1,0,1}^4 (81 vectors), s over
   {(0,0),(1,0),(0,1),(1,-2)}, and d_x=4H(x)-2. Let r range over the
   SET {0,1,2,max(0,d_x-1),max(0,d_x),max(0,d_x+1)}. For each pair
   of endpoints use (R,P Lx+S s,r) and (A_matter,P x+S s,r).
   Choose spectators b_j=rho_j e0 where rho=D(S s)_E, then also the
   deliberately non-Gauss variant replacing b0 by b0+e0. On every state
   test exact predicted switching/fixation, complete G^2 identity,
   Htotal, nonnegative resource, unchanged b, full matter vector sum,
   each defect component, F/G commutation, both Ucell inverse identities
   and preservation by Ucell. Do not replace this domain after observing it.
3. Exhaust y in {0,1,2,3,4}^4, s=0, b=0, m=R for r=0 and r=2.
   Compare the two congruences with divisibility of Ny and exact integral
   inversion. Require 25 image members. Require respectively
   (24 switched,601 fixed) and (25 switched,600 fixed); the sole zero
   image representative needs two reservoir units. These counts concern
   these literal representatives, not arbitrary energy shells or all states
   sharing their residues. Audit G^2, energy and defect for every fixture.
4. Required explicit examples, with w=(0,0,1,0):
   - Neutral: (R,b=0,P Lw,r=0) -> (A_matter,b=0,Pw,r=2), total23.
   - Charged: s=(1,0), b=(2e0,-3e0,e0), high raw field
     (2,2,-2,-1,1,2), low raw field (1,1,0,1,1,0). Each has actual
     divergence (2,-3,1). The exact account is
     18+8+84+0 = 20+4+84+2 = 110.
   - Reverse at w with r=0 or1 is fixed; with r=2 it switches to R,r=0.
   - At x=0: R with r=0 or1 is fixed, R,r=2 -> A_matter,r=0;
     A_matter,r=0 -> R,r=2. This exposes reservoir-funded activation.
   - R with active y=(0,0,1,-2), H(y)=5, is fixed even at r=100;
     it is offimage. The historical y=(0,0,1,1) is also rejected.
     y=(0,0,1,2) is admitted with inverse (1,0,-1,1).
   - Raw field (1,0,0,0,0,0), b=(e0,-e0,0), m=R,r=100 satisfies
     actual Gauss but is nonsplit; G fixes it. Resource does not repair
     a split/image failure and raw extraction alone is not admission.
   - Off-endpoint ordered triples (0,0,0), (A_matter[1],A_matter[0],
     A_matter[2]) and (e1-2e2+e3,0,0) remain fixed by G for low/high
     fields at w and r=0,2,100. No phase/permutation equivalence is used.
5. Negative alternatives must be explicitly falsified by exact witnesses:
   discarding the h=1 surplus loses two energy units; clipping the reverse
   budget at zero creates two; omitting spectator energy undercounts the
   charged example by84; deleting the static field destroys its nonzero
   actual charges; conflating R/A or clearing a retained register cannot
   be used as the asserted inverse. Do not execute an alternative global
   law as a new candidate or adjust the law to make these controls pass.
6. For the neutral and charged w witnesses, check exactly k=0,...,10
   using the prospective formula with static s and spectators retained:
   even k gives (R,P L A^k w+S s,r=0), odd k gives
   (A_matter,P A^k w+S s,r=2). Verify first return10, Ucell^5=G,
   and the algebraic commutation/order certificates. This is a fixed
   ten-step identity audit, not a searched delay or lifetime statistic.

One unequal identity, false exact predicate, state-space escape, negative
resource, failure of involution/inverse/energy/pointwise defect, changed
spectator or unexpected period witness falsifies the affected frozen clause.
There is no numerical tolerance. An environment, source-integrity, syntax,
runtime, timeout, stderr or stdout mismatch is STOP, distinguished from a
mathematical counterexample. Preserve it; never weaken a frozen assertion
or change code until green. Corrections require a separately named successor.

## Independent implementation and accepted execution

Commit, push and read back this preregistration before new scientific
execution. Then the builder writes verify.py and a fresh agent independently
writes break.py using only this frozen preregistration and public base
definitions. The second author must not read builder code, proof, either
predecessor implementation or any execution output before the joint code
pin. Known targets are exposed; this is implementation independence only.
Separate static review and AST parsing are allowed before the pin; no
scientific dry run, module import or scratch numerical calculation is allowed.

Freeze both implementations, PROOF, a thin runpy bridge, README and a
prospective exact success target in one public code commit before either
implementation runs or their outputs are compared. The bridge guards this
PREREG and both source files by literal SHA-256. It does not copy runner
rules, compare EXPECTED itself, classify architecture or alter timeouts.
The primary checks the six public base source hashes above; the challenge
reconstructs independently from the frozen definitions. No runtime network,
external dependency, archival import or private source is permitted.

The scripts emit only their following one ASCII/LF line after ALL checks:

```text
PRIMARY PASS: local L5 coupling; exact account, inverse and pointwise Gauss defect
```

```text
CHALLENGER PASS: independent coupling audit; image, funding and branch controls
```

The bridge prints `IMPLEMENTATION primary`, then the primary line,
`IMPLEMENTATION challenger`, then the challenge line, then
`COUPLING PASS: NON-CANONICAL L1; one selected finite-cell law; period 10`.
These five lines with a final LF are the prospective EXPECTED.txt target,
not a measured execution record. Actual agreement is recorded only after
the unchanged runner observes it.

The standard reproduction path is
reproduce/FIELD-L5-ENERGY-FUNDED-COUPLING-N/ with verify.py, EXPECTED.txt
and README.md. First scientific command, from the clean committed root:

```text
python3 tools/check_reproduce.py --base b8ba1a07ad776cdd8d878fe0a407e07312c0e263
```

Local environment: Ubuntu22.04.5 LTS, x86_64, Python3.10.12 stdlib, WSL.
The current runner sets LC_ALL=C, LANG=C, TZ=UTC, PYTHONHASHSEED=0,
PYTHONDONTWRITEBYTECODE=1 and enforces 120 seconds for the entire bridge,
exit zero, empty stderr and stdout byte identity. Record exact checker
stdout in RUNNER.txt and neutral environment, pins, byte counts and hashes
in RUN.md. No ad-hoc formal invocation or shared checker/workflow change.

Use ordinary unchanged policy/unit/Canon/ledger/gate checks. Require actual
REPRODUCE PASS readback with the same wrapper and stdout hashes from BOTH
public PR architecture jobs, Python3.12 x86_64 and aarch64. Local agreement
or generic notes-only green CI is not that computation gate.

## Endpoint and boundaries

Deliver a self-contained proof, exact executable law and independent
challenge, outcomes and source custody, reviewed NON-CANONICAL PR and
promotion proposal. Separate universal proof from the finite audit and
list inherited facts versus this concrete construction. Disclose every
choice: multigraph and support, matter chart/metric, fixed phase/endpoints,
one selected reaction, neutral reservoir, spectators, gate order, preparation
and reader. No claimed percentage is derived from J.

The law is one closed finite cell; its explicit period-ten result rules
out describing its own alternating gate as a directed decay, escaping
product or permanent one-way record. No helper census, reaction tuning,
multicell propagation, receiver/detector, particle comparison or physical
L1--L6 bridge is part of this task. QDD-INSTRUMENT-APPARATUS,
QDD-TERMINAL-EVENT-SEMANTICS and PHOTON-MASSLESS-PHASE retain all obligations.
No merge, tag, release, Canon, sealed-probe, shared-runner or owner changes.
Choose exactly one later scoped task from the proved result after disposition;
do not start that later composition or transport task here.
