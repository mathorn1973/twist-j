# C-FIELD-CYCLOTOMIC-WINDOW-AUDIT-N: successor preregistration

PUBLIC / NON-CANONICAL incubation. Authority: none. Action layer: L1.
Owner: A. M. Thorn / codex-field-cyclotomic-window-audit-20260930.
Reservation: issue #1303. This is one candidate, not a formal probes/ lane.

## Authority, source custody and predecessor disposition

Base: public main b8ba1a07ad776cdd8d878fe0a407e07312c0e263.
Declared v95 content: 5a1dd8ba6c339640940b5a013d3c412025a1f8fc.
Annotated tag canon-v95: 7810207b27539ee35e30ffb0ed81cec32fa322c7,
peeling to base. Immutable published non-draft release: 400415362.
Fresh public readback confirmed unchanged completed activation: main run
36766242516 (both architectures and check), tag run 36769404870 and
release run 36773377591 all passed. The preceding independent activation
audit validated the downloaded assets with check_release_manifest.py;
fresh asset hashes still match. The activation manifest SHA-256 is
7544df31a47ddccba39454dc1036498551997d50d11cca5e044903f9ff572e0e;
the release SHA256SUMS asset hash is
c74a93513fd4a880ca9649259804c4f9c9f1d073d3dad910abff4de6b1b9ccac.

The fresh startup scan fetched main, read STATUS/POLICY/AGENTS/CORE/FRONTIER
and relevant Canon proofs, registry, evidence, dependencies and gates.
Explicit `git ls-remote --heads origin` returned 175 heads. Exact successor
searches returned zero; all 206 open issue/PR records contained neither
proposed successor identifier. Existing #1301/#1302 are this owner's
predecessor. #1000, #1104, #1237/#1238 and memory/locality work have distinct
objects. No competing successor owner was found before this reservation.

Public source closure at base (SHA-256):

| file | hash |
| --- | --- |
| canon/CANON.md | b4ebf2ffc7393b703d65ce62cf3e0ee382e7309a563d99ec866ee3fa82f9ba7f |
| canon/REGISTRY.tsv | a2abce1a4538785ac6a7c7874c2366a3531d460027188510394930c6d222559a |
| canon/EVIDENCE.tsv | 1258ea3dd14a5e2b512b69b08ac647626d4fac169a1ba0b6cd770832bb735600 |
| canon/DEPENDENCIES.tsv | c1b0cee2b9e320ed05ba4004da3a2265cbd2bbafe45dd18f59fb29790d477214 |
| canon/GATES.tsv | 85f7db365ff38988dbf2a994f4d8d0ba380ac00d368bcc50e4313daee9aff744 |
| notes/INTEGER-AUTOMATON-COMPOSITION-PROGRAM.md | 354c4b5292c89ab521654a642f056c39f4c99e688b5e34891369c23980d9dfd7 |

The predecessor is C-FIELD-CYCLOTOMIC-WINDOW-N, issue #1301 / draft PR
#1302, final public commit ff603881d1c297a6bbb63f88df455a4b4bf3ea74.
Its primary code pin 40b30d87b617bf412980dcf8368f46b57407ad95 stopped
on a false shortcut predicate. The old primary SHA-256 is
4a62085cfd224aa7561e7c0d195aa06653fe19a59cb17da722cf2a4051202099.
It falsely accepted y=(0,0,1,1) by a+2b=0 and 3a-b+c-d=0 modulo five.
Its unreached H=5 nonimage witness (0,0,1,2) was also false: it equals
L(1,0,-1,1). Both defects and the failed execution remain unchanged there.
No predecessor script will be rerun, repaired or relabelled successful.

The original assignment exposed the window, G5 and L identities. The
predecessor additionally exposed all matrices, correct congruences and
the true witness below. This successor is a correction and independent
audit of exposed targets, never blind discovery. The primary may adapt the
public predecessor with explicit attribution; the second implementation
must be newly written from this preregistration and public definitions,
without reading either primary source, old breaker, proof or execution
outputs before the joint code pin. No private code is copied or executed.
The earlier Czech memo and its particular programs were not located in the
predecessor custody audit; no reproduction of those files is claimed.

## Equations, carriers and exact equality

All equalities are literal in ordered integer/rational coordinates, with
no floating point, tolerance or empirical data. For every finite integer
C of size e by f (including zero/empty dimensions), define

```text
T(E,M)=(E+CM, M-C^t(E+CM)),
T=[[I,C],[-C^t,I-C^t C]],
T^-1=[[I-CC^t,-C],[C^t,I]],
H(E,M)=E^t E+M^t M+E^t C M,
R(E,M)=(E+CM,-M).
```

The proof target is max spec(C^t C)<4 iff T has finite order iff EVERY
full integer orbit is bounded. Empty spectral maxima are zero. Reuse the
inherited completed square; cover static kernels, rectangular/rank-deficient
C, critical Jordan growth and unstable states. Derive the stable nonzero
block relations mu+mu^-1=2-lambda, lambda=|1-mu|^2 and mu^N=1.
Prove R^2=I, RTR=T^-1, preservation of H and of actual DE when DC=0.
Real spectral splitting must not be called an integral direct sum.

Inherited from v95: FIELD-SHEAR-ENERGY-BOUNDARY's inverse, H, divergence,
completed square, positivity and two-triangle zero mode. The ten v95
construction theorems retain their scope. FIELD-EISENSTEIN-RESONANCE is
the distinct triangle channel; FIELD-GAUSS-CONTACT-MEMORY and
INTEGER-ENERGY-FUNDED-INVOLUTION supply conditional interfaces only.
CARRY-PENTAD already provides another integral cyclotomic/J bridge.

Selected oriented multigraph: vertices 0,1,2; edges e0:0->1, e1:0->1,
e2:0->2, e3:2->1, with distinct parallel e0,e1. Faces c0=e0-e1 and
c1=-e0+e2+e3. Boundary has + at tail and - at head. Raw order is
(E0,E1,E2,E3,M0,M1).

```text
C=[[1,-1],[-1,0],[0,1],[0,1]],
D=[[1,1,1,0],[-1,-1,0,-1],[0,0,-1,1]],
G=C^t C=[[2,-1],[-1,3]], DC=0,
P(a,b,c,d)=(a-b,-a,b,b,c,d), F(z)=(-E1,E2,M0,M1),
A=[[1,0,1,0],[0,1,0,1],[-2,1,-1,1],[1,-3,1,-2]],
B=[[4,-2,2,-1],[-2,6,-1,3],[2,-1,2,0],[-1,3,0,2]], H=x^t B x/2,
S(u,v)=(u,u,v,u-v,0,0),
K=[[0,1,0,0],[0,0,1,-1],[1,-1,0,-1],[0,1,-2,1]].
```

Prove Lambda_act=ker_Q Phi5(T) intersect Z^6=P Z^4 saturated via FP=I,
TP=PA and the complementary saturated static lattice S Z^2. Raw active
admission is PFz=z, not extraction alone. Verify Phi5(A)=0, exact order
five, actual K with columns w,Aw,A^2w,A^3w for w=(0,0,1,0), determinant
-1 and integer inverse; t=zeta5 is represented by A. For J=I+A^2 check
charpoly x^4-3x^3+4x^2-2x+1, trace3, determinant1 and integer inverse
-A-A^2. It is not an H isometry: H(1,0,0,0)=2, H(J(1,0,0,0))=3.

The active/static sum has index5. Integral splitting is equivalent to
g=2E0-3E1+E2+E3=0 mod5, equivalently 2rho0+rho2=0 with rho=DE.
Every zero-sum integer rho is realized by E=(rho0,0,0,rho2). Each fixed
rho sector is an affine active lattice; rational projections are not
automatically integer operations.

## L5, exact image and explicit regression witnesses

```text
L=(I-A)(I-A^2)=[[1,-3,-1,-2],[-3,4,-2,1],[0,5,1,2],[5,-5,2,-1]],
N=A^2 L=[[1,2,1,2],[2,-1,2,-1],[0,-5,1,-3],[-5,5,-3,4]].
```

Verify LA=AL, L^2=5A^3, NL=LN=5I, det L=25, L^t B L=5B and
L^*=B^-1 L^t B=N. Thus H(Lx)=5H(x). Supply Smith and Hermite
unimodular certificates: Smith diag(1,1,5,5), determinantal divisors
1,1,1,5,25, column Hermite [[5,3,0,0],[0,1,0,0],[0,0,5,3],[0,0,0,1]].
The exact all-integer image criterion is a+2b=0 AND c+2d=0 mod5.
Reject a nonmember BEFORE division; on admission return Ny/5. Prove the
quotient (Z/5Z)^2, distinguishing injection, partial inverse and shells.

Mandatory regression witnesses (already exposed):

- (0,0,1,1) is not in the image: N y=(3,1,-2,1).
- (0,0,1,2) IS in the image, with inverse (1,0,-1,1), of energy1.
- (0,0,1,-2) has energy5 and is NOT in the image:
  N y=(-3,4,7,-11). Whole H=1 -> H=5 shell surjectivity is false.
- w=(0,0,1,0) has H=1 and Lw has H=5, witnessing nonempty admitted image.

Full-space L_raw=(I-T)(I-T^2) annihilates static states and charges.
The rational extension L_tilde=L_raw+Phi5(T)/5 preserves actual D but
sends raw e0 to (17/5,-3/5,-9/5,-9/5,-1,3), hence is not integral
everywhere. Its exact integer domain is the above index-five split lattice;
there its energy is 5H_active+H_static. Prove the domain and inverse/image
restriction without asserting an obstruction to all other extensions.

Interface only: input/output lattice, raw admission, image test, retained
charges, full finite-cell access, inverse and required future branch/resource
record. A 5h->h reversal releases4h; at h=1 four differs from the two
required by R18->A20. No coupling, many-to-one update, phase loss, clock,
waiting time, decay exponent or physical identification is inferred.

## Finite challenge, systematics and frozen success target

Both scripts must audit exact matrices/certificates and deliberately reject
static Phi1 contamination, a doubled active basis column (index2), hidden
division by five, Euclidean-adjoint substitution and J as H isometry.
Use the actual D for every selected-carrier charge assertion.

The complete finite controls are C=0 (2 by3), C=(1,0)^t, diag(1,0),
diag(2,0), diag(3,0), C above and the exact v95 fixture
Ccrit=[[1,1],[1,0],[1,0],[0,1],[0,1]]. Check the lambda4 Jordan block;
the unstable diag(3,0) has a nonzero bounded static special orbit.
For v=(1,1) and E0=0,M0=v, verify Ccrit's formulas at n=0,...,12:
E_n=(-1)^(n+1)n Ccrit v, M_n=(-1)^n(2n+1)v, H=2.
The written induction covers every n. Adjacent ordinary signed triangles
each have three distinct unit incidences and share exactly one edge;
their Gram eigenvalues4,2 obstruct this strict window only in that class.

Exhaust all625 residues y in {0,...,4}^4, compare explicit congruences,
divisibility of Ny and the enumerated mod5 image of L; require25 admitted
and600 rejected. Exhaust625 electric residues for index-five gluing and
actual charge criterion, requiring125 admitted and500 rejected. These are
complete residue domains, not low-energy shell enumerations. No shell,
trajectory, reaction, detector, helper or multicell search is admitted.

Each script prints its single following ASCII success line, with LF,
only AFTER all its checks pass; it prints no other normal output:

```text
PRIMARY PASS: exact field, lattice, L5 and 625 image residues; 25 admitted, 600 rejected
```

```text
CHALLENGER PASS: independent exact audit, scope controls and both predecessor regressions
```

The bridge prints `IMPLEMENTATION primary` before running verify.py and
`IMPLEMENTATION challenger` before running break.py, then the final line
`AUDIT PASS: exposed targets; NON-CANONICAL L1; proof required for universal claims`.
The five lines, in that order with LF and final LF, form the prospective
EXPECTED.txt. This is a predeclared success target, NOT a measured run record.
Passing stdout alone proves only execution of the declared assertions;
universal conclusions require the written proof and independent review.

## Pinning, accepted runner, failure threshold and endpoint

Commit/push/read back this PREREG before any new science. Then write the
primary and independently authored challenge; both may know this output
contract. Only static parsing/review may occur before their joint public
code pin. Freeze both source files, a thin runpy bridge with literal source
and prereg SHA-256 guards, README and prospective EXPECTED together, push
and read back, before comparison or execution. No thresholds or frozen
scientific code may change after execution. Proof and records are distinct.

First scientific invocation, from the clean committed repository root:

```text
python3 tools/check_reproduce.py --base b8ba1a07ad776cdd8d878fe0a407e07312c0e263
```

Local environment: Ubuntu22.04, x86_64, Python3.10.12 stdlib, via WSL.
Use the current unchanged runner. It sets LC_ALL=C, LANG=C, TZ=UTC,
PYTHONHASHSEED=0 and PYTHONDONTWRITEBYTECODE=1, enforces120 seconds for
the entire bridge, exit0, empty stderr and byte-identical EXPECTED.
No copied checker rules, new workflow or ad-hoc formal launcher. Save
the checker's exact stdout as RUNNER.txt and neutral metadata in RUN.md.
Actual output equality/exit/stderr are observations only after that run.
Normal policy/unit/Canon/ledger/gate checks remain unchanged.

The standard reproduction is reproduce/FIELD-CYCLOTOMIC-WINDOW-AUDIT-N/
(verify.py, EXPECTED.txt, README.md). Its bridge runs the two notes scripts
separately with runpy and shares no scientific implementation. Public CI
uses unchanged check_reproduce.py on Python3.12, x86_64 ubuntu-latest and
aarch64 ubuntu-24.04-arm. Require BOTH jobs to report this reproduction's
same wrapper and stdout hashes. Notes-only green CI or same-architecture
agreement does not satisfy the public scientific computation gate.

One exact counterexample falsifies its universal clause, one unequal
matrix falsifies its identity. Missing custody blocks attribution only.
Source, environment, runtime, timeout, stderr or output mismatch is STOP;
preserve the exact failing clause and record, and use a fresh successor
if correction is needed. Never repair the frozen source until it passes.

End with one reviewed NON-CANONICAL PR, clause dispositions, self-contained
proof and full matrices/certificates, RUN/RESULT, custody hashes, promotion
proposal, independent-choice account and one next scoped task justified
by the result. No Canon/registry/release/sealed-probe/checker/workflow/owner
edits, no merge/tag/release. QDD-INSTRUMENT-APPARATUS,
QDD-TERMINAL-EVENT-SEMANTICS and PHOTON-MASSLESS-PHASE remain fully open.
Local coupling, 666-helper census and propagation remain separate tasks.
