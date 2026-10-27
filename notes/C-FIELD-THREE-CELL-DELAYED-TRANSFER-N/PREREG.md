# Frozen three-cell delayed neutral work transfer

PUBLIC / NON-CANONICAL incubation. L1 only. Authority: none.
Candidate C-FIELD-THREE-CELL-DELAYED-TRANSFER-N, reservation issue #1309.
Owner: A. M. Thorn / codex-field-three-cell-delayed-transfer-20261001.

## Authority, custody, scope and exposure

The user authorizes a separate successor to #1308: three disjoint cells,
two stored neutral channels, a complete-step boundary storing energy in the
middle before receiver work, and a fixed-depth local schedule rather than
an end-to-end sweep. Preserve both cut controls, occupied contents, exact
inverse, preparation cost and full Gauss/energy accounting. Permanent memory,
particle interpretations and general all-length work claims are outside scope.

Fresh public main is b8ba1a07ad776cdd8d878fe0a407e07312c0e263. Activated v95
content is 5a1dd8ba6c339640940b5a013d3c412025a1f8fc; annotated tag object
7810207b27539ee35e30ffb0ed81cec32fa322c7 peels to main. Ancestry and current
STATUS/POLICY/AGENTS/CORE/FRONTIER, relevant registry/evidence/dependencies,
gate and inline proofs were read. Canon has 848893 bytes. Actual downloaded
assets of published immutable release400415362 were verified; main/tag/release
runs36766242516/36769404870/36773377591 passed, not merely an ACTIVE-looking file.

The explicit remote-head scan found178 heads. All212 open issue/PR bodies and
the complete nontruncated3874-entry public tree were inspected. Exact candidate,
reproduction and branch names are absent. Related #1296/#1297 ramified-tree
locality concerns a different carrier and requires latency with distance:
fixed depth PER STEP is compatible with it, never constant total travel time.
Moving-head memory #1294/#1295, passive optical stages #832, native carry
records #986/#987 and the QDD three-cell record extension have different
carriers/claims and are not absorbed or reopened.

Public source SHA-256 at the base:

| source | SHA-256 |
| --- | --- |
| canon/CANON.md | b4ebf2ffc7393b703d65ce62cf3e0ee382e7309a563d99ec866ee3fa82f9ba7f |
| canon/REGISTRY.tsv | a2abce1a4538785ac6a7c7874c2366a3531d460027188510394930c6d222559a |
| canon/EVIDENCE.tsv | 1258ea3dd14a5e2b512b69b08ac647626d4fac169a1ba0b6cd770832bb735600 |
| canon/DEPENDENCIES.tsv | c1b0cee2b9e320ed05ba4004da3a2265cbd2bbafe45dd18f59fb29790d477214 |
| canon/GATES.tsv | 85f7db365ff38988dbf2a994f4d8d0ba380ac00d368bcc50e4313daee9aff744 |
| notes/INTEGER-AUTOMATON-COMPOSITION-PROGRAM.md | 354c4b5292c89ab521654a642f056c39f4c99e688b5e34891369c23980d9dfd7 |

Candidate dependencies remain unmerged OPEN drafts, not Canon authority:

| PR | complete reviewed head | proof SHA-256 | final public run |
| --- | --- | --- | --- |
| #1308 | 23d57d1a0397a775f7b8ae3aaa7e2ca5dc93cf5f | 3b5889395b39c1699c362b3ee26a61a8870a25f291be2d4057841aa69ebb9e09 | 36833230091 |
| #1306 | 869998eb8c1c68f7a884fafbf683bf20db0eb7f1 | 58cc146e07a32dd36119cb9caf52e9c58c1137d7216fb0f48ba264e8da272861 | 36793890508 |
| #1304 | dcfde46760bdfd4551686be1e99b5433fa6e9adf | d9cde5b2182fbd8526865c1117730099b91d2fa1a0d78e059b3707abacffeb78 | 36784630463 |

All final runs passed both architecture jobs and aggregate check. Needed
definitions are restated; no predecessor executable/private archive is a
runtime dependency. The builder has read predecessor code and may reuse
audited local arithmetic. The independent challenger must not read it.
Inherited Canon inputs are INTEGER-F-JG-INVARIANTS,
INTEGER-ENERGY-FUNDED-INVOLUTION, FIELD-GAUSS-CONTACT-MEMORY and
FIELD-EISENSTEIN-RESONANCE, at their actual existing scopes. The L5 field and
local gate are candidate inputs. No generic involution theorem is rediscovered.

The requested target and all earlier mathematics were exposed. Before this
pin, symbolic reasoning (no scientific program, import or scratch numerical
calculation) selected the four layers and derived the tables41/253 below,
cuts and order controls. These are exposed targets, not blind predictions.
Implementation independence is from code/output, not from the same formulas.

## Complete carrier and local law

Cell i=0,1,2 stores ci=(mi,bi,zi,ri): three ordered reacting Z4 registers
at its vertex0, three spectator Z4 registers at vertices0,1,2, raw field
zi=(E0,E1,E2,E3,M0,M1) in Z6, and ri>=0. Each cell has31 integer coordinates.
Their fields, matter and vertices are disjoint. q0,q1>=0 are separately stored
neutral contact registers for pairs0--1 and1--2. Full state is
(c0,c1,c2,q0,q1), with95 coordinates:90 unrestricted integers and5 nonnegative
resources. Equality is literal ordered-coordinate equality; no phase, routing,
energy-shell or spectator quotient. Channel energy is q0+q1 with weight1.
The zero-matter triple ZM=((0,0,0,0),(0,0,0,0),(0,0,0,0)) is not R or AM.

The cell multigraph has distinct parallel edges0,1 and ordered edges
(0->1,0->1,0->2,2->1); faces are e0-e1 and -e0+e2+e3. With +tail/-head:

```text
C=[[1,-1],[-1,0],[0,1],[0,1]],
D=[[1,1,1,0],[-1,-1,0,-1],[0,0,-1,1]], DC=0,
K=[[6,2,-1,2],[2,6,2,-1],[-1,2,6,2],[2,-1,2,6]],
Q(v)=v^t K v, chi(v)=sum_j v_j,
Hraw(E,M)=E^t E+M^t M+E^t C M,
Hcell(m,b,z,r)=sum_j Q(mj)+sum_j Q(bj)+Hraw(z)+r,
Hjoint(c0,c1,c2,q0,q1)=Hcell(c0)+Hcell(c1)+Hcell(c2)+q0+q1,
rho_i=(chi(bi0)+sum_j chi(mij),chi(bi1),chi(bi2)),
defect_i=D Ei-rho_i.
```

The joint electric boundary is diag(D,D,D). The neutral contact register is
an added energy carrier, not an electric edge, face, charge or hidden field
coordinate. Joint Gauss means all three defects vanish. Every component of all three
defects, including nonzero defects, must be retained. Actual charges stay
fixed at each of the nine nodes; this task has no transported charge/current.

The canonical four-phase matter chart is distinct from field coordinates.
Fix only the two ordered matter endpoints

```text
R=((1,-2,1,0),(0,0,0,0),(0,0,0,0)),
AM=((1,0,0,0),(0,-1,0,0),(0,-1,1,0)).
```

Their full vector sums agree, their energies are18/20 and their node0 total
chi is zero. They encode the inverse branch. Other phases/permutations are
not identified with them; no other reaction or free matter step is installed.

The exact field data, with H(x)=x^t B x/2, are

```text
P(a,b,c,d)=(a-b,-a,b,b,c,d), S(u,v)=(u,u,v,u-v,0,0),
A=[[1,0,1,0],[0,1,0,1],[-2,1,-1,1],[1,-3,1,-2]],
B=[[4,-2,2,-1],[-2,6,-1,3],[2,-1,2,0],[-1,3,0,2]],
L=[[1,-3,-1,-2],[-3,4,-2,1],[0,5,1,2],[5,-5,2,-1]],
N=[[1,2,1,2],[2,-1,2,-1],[0,-5,1,-3],[-5,5,-3,4]].
```

For raw z, the integral split z=P(a,b,c,d)+S(u,v) exists iff
g=2E0-3E1+E2+E3=0 mod5. Only after admission form

```text
a=g/5, b=(-E0-E1+2E2+2E3)/5, c=M0, d=M1,
u=(2E0+2E1+E2+E3)/5, v=(E0+E1+3E2-2E3)/5.
```

The split is unique, and its sublattice has index5; do not project arbitrary
raw fields with rational coordinates into an undeclared integer state.
For y=(a,b,c,d), y belongs to LZ4 iff a+2b=c+2d=0 mod5. On this image,
x=Ny/5 is the unique integer preimage. LN=NL=5I, AL=LA, A^5=I,
A^t B A=B, L^t B L=5B. Static energy is3u^2-2uv+2v^2, and
Hraw(Py+Ss)=H(y)+Hstatic(s). DP_E=0, DS_E(u,v)=(2u+v,-3u+v,u-2v).

The total local reaction gate G fixes its whole input unless a branch below
is exactly recognized and the resulting resource is nonnegative:

```text
(R,b,PLx+Ss,r) -> (AM,b,Px+Ss,r+4H(x)-2);
(AM,b,Px+Ss,r) -> (R,b,PLx+Ss,r+2-4H(x)).
```

Recognition tests matter, split, image on the R branch, then funding. No
rounding, negative clipping, partial write or clearing on rejection is allowed.
G is an involution. It preserves full cell energy, matter-vector sum,
spectators, actual rho and pointwise defect; separate reacting-register
charges may change. The h=0 R branch requires r>=2; for h=1 the R branch
deposits2 and the reverse needs2. These cases are part of the chosen law.

F changes only raw field by T(E,M)=(E+CM,M-C^t(E+CM)). Its inverse is
T^-1(E',M')=((I-CC^t)E'-CM',M'+C^t E'). It preserves energy/defect,
TP=PA, TS=S, T^5=I and FG=GF for the one-cell law. G(s)=s does NOT imply
F G(s)=s. This distinction must survive all new tests and reporting.

## Four layers, full inverse and local support

Write Ai for swap(ri,qi), i=0,1, and Bi for swap(qi,r(i+1)), i=0,1.
These exchange entire nonnegative contents, including occupied channels.
They do not select a packet, copy, overwrite, clip, drain or reset anything.
For each contact the affected cell/channel energy increments are
(q-r,r-q), using the values just before that contact; other cells are fixed.

One complete step is precisely these chronological layers:

```text
G0 G1 G2 in parallel;
A0 A1 in parallel;
B0 B1 in parallel;
F0 F1 F2 in parallel.
U=F B A G.
```

G/F read and write only their own31-coordinate cell (G fixes spectators;
F changes only the six raw field coordinates). A0 reads/writes only(r0,q0),
A1 only(r1,q1); B0 only(q0,r1), B1 only(q1,r2). Within each layer supports
are disjoint. Simultaneous old-state writes or a serialization proven
equivalent by disjointness are allowed; reverse within-layer order must agree.
Across A and B the supports overlap, so reversing layers is a different law.

The inverse applies F^-1 in parallel; B; A; G. Prove both inverse identities,
legality, total energy, fixed spectators, each cell reacting-vector sum, all
nine actual charges and all nine defect entries at each primitive and layer.
G/F have zero cell-block range. On the alternating path
C0--Q0--C1--Q1--C2, each contact matching has radius1. Therefore forward and
inverse macrosteps have dependency radius at most2 edges; k steps at most2k.
This is structural dependence on stored blocks, not a claim that perturbations
always propagate at the bound or a physical speed measurement.

The finite open-chain TEMPLATE for N>=2 is exactly the same four layers:
all Gi, Ai=swap(ri,qi) for i=0..N-2, Bi=swap(qi,r(i+1)) for i=0..N-2,
all Fi. Disjoint supports prove fixed depth4, inverse, conservation and the
same radius bound for every finite N. No variable-length serial sweep is
installed. Scientific execution and paid-work witnesses are restricted to N=3;
no infinite chain, general all-length transfer/work theorem, optimal latency,
physical locality or native-U derivation is claimed.

For three cells, resources immediately AFTER G, in order(r0,r1,r2,q0,q1),
are(a,b,c,p,q). A sends this to(p,q,c,a,b), B then to(p,a,b,q,c).
Every old resource survives in a unique register. This permutation is an
exact invariant-of-contents check for contact layers, not for reactions.
The channel choice, energy weight, path orientation, phase chart, gate order,
preparation and reader are architecture. No clock/direction/occupancy tag is
silently omitted; this is a fixed macrostep map, not an autonomous microclock.
Even N=2 uses a DIFFERENT complete schedule from #1308, which reacted the
receiver after contacts. Only local gates/contacts and accounting are inherited.

Define cut-j by replacing BOTH Aj and Bj with identity, leaving qj stored
and fixed. Other operations/order stay identical. These are separately
declared laws, not time-dependent reader flags. Each also has the same
reverse-order inverse and conservation. Test both cuts on identical preparation.

## Frozen boundary witnesses and preparation

Let w=(0,0,1,0), H(w)=1, Lw=(-1,-2,1,2), PLw=(1,1,-2,-2,1,2),
Pw=(0,0,0,0,1,0). Neutral initial cells are (R,0,PLw,0), (ZM,0,0,0),
(R,0,0,0), with q0=q1=0. The middle has zero energy, but all31 stored
coordinates and its contacts remain real architectural resources.

| boundary k | matter0,1,2 | r0,r1,r2,q0,q1 | H0,H1,H2,q0,q1 |
| --- | --- | --- | --- |
| 0 | R,ZM,R | 0,0,0,0,0 | 23,0,18,0,0 |
| 1 | AM,ZM,R | 0,2,0,0,0 | 21,2,18,0,0 |
| 2 | AM,ZM,R | 0,0,2,0,0 | 21,0,20,0,0 |
| 3 | AM,ZM,AM | 0,0,0,0,0 | 21,0,20,0,0 |

Source raw low fields at k=1,2,3 are respectively
PAw=(1,-1,0,0,-1,1), PA^2w=(-1,0,1,1,0,-2),
PA^3w=(1,0,-1,-1,-1,1). Middle/target fields are zero. Their spectator
registers stay zero. At first G0, energy23 remains23 while r0 becomes2;
the A layer stores those2 in q0; B moves them into middle r1 by boundary1.
At step2 A stores2 in q1, B puts them in target r2 by boundary2. At step3
target G consumes2 and changes R18 to AM20. The source loses2, middle and
channels end with net0, receiver gains2; arrival and use are distinct events.

Charged witness: add S(1,0),S(1,0),S(0,1) to the three raw fields and set
each bj=(DE)j e0, e0=(1,0,0,0). Initial actual rho are(2,-3,1),(2,-3,1),
(1,1,-2), with zero defects. Complete vector states otherwise follow the
same table, preserving static fields and all charged spectators:

```text
(110,87,56,0,0) -> (108,89,56,0,0)
                 -> (108,87,58,0,0) -> (108,87,58,0,0).
```

Total253; middle baseline87=84 spectator energy+3 static energy, no hidden18.
The neutral baseline totals41. Energy is redistributed, never created.

For each charged/neutral preparation and either channel cut, the target
remains exactly its initial (R,b,S,0) for ALL time. Prove the isolated ready
component invariant. The finite audit executes ONLY k=0..3, no search.
When q0 is cut, initially empty middle/target resources remain empty; when q1
is cut, target is isolated. The unused cut channel retains its contents.

Paid-middle control: replace only neutral middle ZM by R (cost+18, total59).
At k1 it is R with r1=2; at k2 it is AM with r1=0 and target remains R/r2=0.
Execute k0..2 only. This is an absorber at that horizon, not free passive
conduction or a claim about its infinite future.

All fixed finite-N energy shells are finite: positive matter/field forms and
nonnegative resources bound every stored integer. A bijection permutes each
shell, so all complete orbits recur. Prove this bound, not a uniform period.
No period search, no assertion U^5=I/U^10=I, no persistent memory; isolated
cell order10 and #1308 witness period5 do not transfer to this law.

## Finite exact audit and falsifiers

Use Python standard-library integers/rationals only, no random numbers,
floating-point, fitted thresholds, third-party or private runtime inputs.
The proof carries universal conclusions; the finite audit exhausts only the
following fixed fixtures, never the unbounded carrier.

1. Check DC=0, DP=0, DS, split/energy formula, the exact A,L,N identities
   above, T^5=I, TP=PA, TS=S, T energy/inverse and G endpoint energies/vector
   sums. Check det(L)=25 and the integral Hermite certificate
   V=[[1,1,1,1],[2,1,2,1],[0,-1,1,0],[-5,-2,-3,-1]], det(V)=1,
   LV=[[5,3,0,0],[0,1,0,0],[0,0,5,3],[0,0,0,1]].
   Check all625 residues in {0,1,2,3,4}^4: both congruences equal exact
   divisibility of Ny, exactly25 admitted residues, and L(Ny/5)=y there.
   No bounded brute-force preimage search is a nonmembership proof.
2. Core local templates(m,z), with zero static part:
   (R,0),(R,PLw),(AM,Pw),(ZM,0). Take all4^3=64 ordered cell-template triples.
   Baseline is((R,PLw),(ZM,0),(R,0)). Exceptional templates are:
   (AM,0), (R,PLv), (AM,Pv), (R,P(0,0,1,-2)),
   (R,(1,0,0,0,0,0)), (AM with first two matter registers swapped,Pw),
   (((0,1,-2,1),0,0),PLw), where v=(0,0,1,1), H(v)=2.
   Substitute each of these7 at each of3 positions in the baseline:21
   indexed triples. No deduplication of this declared indexed inventory.
   For every85 triple use six resource triples
   (0,0,0),(1,2,5),(2,5,6),(5,6,7),(6,7,1),(7,1,2)
   and four channel pairs(0,0),(1,2),(2,1),(3,4).
   Use three backgrounds: (a) all static(0,0); (b) static parameters
   ((1,0),(1,0),(0,1)); (c) same as(b), but add errors(1,-1,2)*e0 to
   respective b0 spectators. In all cases add static raw field first and
   set bj=(DE)j e0 before the extra errors. Every reacting template has
   total chi0. Thus backgrounds(a,b) have zero defect and(c) has respective
   defects(-1,0,0),(1,0,0),(-2,0,0). This is85*6*4*3=6120 full states.
   For every state verify legality/95 coordinates; all ten chronological
   primitive operations (3G,2A,2B,3F) and four layer boundaries; total
   energy, actual rho/defects, spectators/matter sums and read/write frames;
   local G involution and branch/funding recognition, contact involution and
   exchange account; contact resource permutation; both U^-1 U and U U^-1;
   reverse primitive order WITHIN every layer gives the same complete result.
3. Audit every primitive and boundary in the neutral/charged k0..3 witnesses,
   both cuts k0..3 and paid middle k0..2. Check full states, not merely sums.
   For source R,P(0,0,1,-2), middleZM/zero,targetR/zero, all resources empty,
   the source field has energy5 but no L preimage; local G fixes it while F
   moves it. Check k0..3 with unreacted target; prove image invariance under A
   for the all-time no-funding statement. G rejection must not mean U rest.
4. Occupied-contact fixture: all three cells off-endpoint ZM/zero raw field,
   resources(r0,r1,r2,q0,q1)=(0,1,2,3,4). AB gives(3,0,1,4,2); BA gives
   (1,2,4,0,3). Invert exactly and preserve all10 units; also audit both cut
   laws on this full fixture, both inverse identities and their frames.
   Wrong copy: at neutral source G0 output (r0,q0)=(2,0), setting q0=r0
   while retaining r0 creates2. Wrong destructive send(r,q)->(0,r) loses
   old q and identifies inputs with same r and q=0/1. Test both source
   contacts A0,A1 using r=2, q=1. Wrong destructive receive(q,r)->(0,q)
   loses old r and identifies inputs with same q and r=0/1; test both B0,B1
   with q=2,r=1. These are explicit erroneous formulas, not installed laws.
5. BA schedule G;B;A;F is a different reversible, conserving law. At the
   neutral witness k1 q0=2, k2 q1=2, k3 targetR/r2=2 (no target reaction yet).
   Check exactly k0..3. The serial sweep G;A0;B0;A1;B1;F sends2 to target
   already at boundary1 and reacts it at step2, with no middle stored
   boundary. Check k0..2; its2(N-1) contact depth is not this law. Neither
   alternate order is repaired into the frozen schedule after observing it.

Zero tolerance: any violated identity, energy account, coordinate frame,
inverse, legality, charge/defect, branch, control or witness fires that clause.
Source/environment integrity, syntax/runtime/timeout, nonempty stderr or
stdout mismatch is STOP distinct from a mathematical counterexample. Preserve
failure and stop the affected claim. No edits to pinned assertions until green;
any correction requires a separately named successor with failure retained.

## Independent implementation and execution pin

Commit/push/read back this preregistration before scientific computation.
Then author primary verify.py. A fresh challenger reads only this preregistration
and public base definitions, not primary, proof, any predecessor implementation
or outputs before the joint code pin. Static review/AST are allowed; no
scientific dry run/import/scratch computation. Freeze primary, challenger,
PROOF.md, thin runpy bridge, README and prospective EXPECTED.txt together
before execution. Bridge hashes PREREG and both programs, and actually runs
both. Primary verifies the six base source hashes; challenger reconstructs
independently. No copied runner/checker policy or new workflow.

After its assertions each implementation emits one ASCII/LF line:

```text
PRIMARY PASS: three-cell delay; 6120 states; full inverse, energy and Gauss
CHALLENGER PASS: independent delay audit; both cuts, occupied contents and order controls
```

The bridge emits exactly five lines with final LF: IMPLEMENTATION primary,
primary line, IMPLEMENTATION challenger, challenger line, then
`DELAY PASS: NON-CANONICAL L1; middle at 1, arrival at 2, receiver work at 3`.
These prospective bytes are frozen before execution; agreement is only an
observed result afterward. Reproduction path:
reproduce/FIELD-THREE-CELL-DELAYED-TRANSFER-N/{verify.py,EXPECTED.txt,README.md}.

First scientific command from clean committed root:

```text
python3 tools/check_reproduce.py --base b8ba1a07ad776cdd8d878fe0a407e07312c0e263
```

Environment: Ubuntu22.04.5 LTS, x86_64, Python3.10.12, WSL standard library.
Unchanged runner sets LC_ALL=C, LANG=C, TZ=UTC, PYTHONHASHSEED=0,
PYTHONDONTWRITEBYTECODE=1,120-second limit for WHOLE bridge, exit0, empty
stderr and exact bytes. Preserve checker stdout in RUNNER.txt and neutral
pins/environment/hashes in RUN.md. Require actual matching REPRODUCE PASS
lines in BOTH public PR architecture jobs, Python3.12 x86_64/aarch64, plus
current repository checks and manual security/source review. No invented
probes/P-* or GENESIS staging records for this notes candidate.

Deliver proof, minimal dual implementation, RESULT/RUN/REVIEW, SHA256SUMS
and promotion proposal as one reviewed NON-CANONICAL draft PR. Preserve the
construction, cuts, preparation and finite recurrence boundary together.
Select one later scoped task from the result without starting it. No merge,
tag, release, Canon/shared checker/workflow/predecessor/ownership edits. No
L1--L6 lift, physical energy/current, detector or permanent record claim.
QDD-INSTRUMENT-APPARATUS, QDD-TERMINAL-EVENT-SEMANTICS and
PHOTON-MASSLESS-PHASE keep all existing obligations.
