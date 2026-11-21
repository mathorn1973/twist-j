# C-FIELD-CYCLOTOMIC-WINDOW-N: frozen assignment

PUBLIC / NON-CANONICAL incubation. No Canon authority. Action layer: L1.
Owner: A. M. Thorn / codex-field-cyclotomic-window-20260930; issue #1301.
Basis: Public Canon v95, main b8ba1a07ad776cdd8d878fe0a407e07312c0e263.
Content commit: 5a1dd8ba6c339640940b5a013d3c412025a1f8fc.

## 1. Authority, exposure, sources and ownership

The annotated canon-v95 object 7810207b27539ee35e30ffb0ed81cec32fa322c7
peels to the basis main. Main run 36766242516 passed both architectures
and check; tag run 36769404870 and release run 36773377591 passed publication.
The published release is immutable. A separate read-only agent downloaded
its assets and the successful tag artifact, ran the repository's
check_release_manifest.py, and confirmed byte identity of the manifest and
SHA256SUMS. This is activation evidence, not this candidate's computation.

Before reservation, the startup audit searched all-state issues, open PRs,
notes, probes, registry and explicitly ran `git ls-remote --heads origin`
(174 heads). No ownership collision was found. The scalar Hodge window
#1237, native cyclotomic amplitude #1000, photon transfer PR #1104 and
memory/locality PRs #1289/#1291/#1293/#1295/#1297 are different scopes.

The supplied assignment already exposed the finite-window statement,
G5, Phi5 targets and L5 identities. This is not blind discovery or testing
previously unseen predictions. The graph and cyclic-seed choices below were
made while drafting this preregistration. No new scientific program has run.
The referenced earlier Czech memo and its specific verifier/breaker were not
located in the inspected sources; no inspection or reproduction of those
particular files is claimed. Optional private archival provenance was read
as text only; it is neither authority nor imported code or runtime input.

Public source identities (SHA-256; basis Git blobs are available at main):

| source | SHA-256 |
| --- | --- |
| canon/CANON.md | b4ebf2ffc7393b703d65ce62cf3e0ee382e7309a563d99ec866ee3fa82f9ba7f |
| canon/REGISTRY.tsv | a2abce1a4538785ac6a7c7874c2366a3531d460027188510394930c6d222559a |
| canon/EVIDENCE.tsv | 1258ea3dd14a5e2b512b69b08ac647626d4fac169a1ba0b6cd770832bb735600 |
| canon/DEPENDENCIES.tsv | c1b0cee2b9e320ed05ba4004da3a2265cbd2bbafe45dd18f59fb29790d477214 |
| canon/GATES.tsv | 85f7db365ff38988dbf2a994f4d8d0ba380ac00d368bcc50e4313daee9aff744 |
| notes/INTEGER-AUTOMATON-COMPOSITION-PROGRAM.md | 354c4b5292c89ab521654a642f056c39f4c99e688b5e34891369c23980d9dfd7 |

Inherited: FIELD-SHEAR-ENERGY-BOUNDARY (inverse, energy, divergence,
completed square, positivity and the exact two-triangle zero mode),
FIELD-EISENSTEIN-RESONANCE (the different triangular norm-three channel),
FIELD-GAUSS-CONTACT-MEMORY and INTEGER-ENERGY-FUNDED-INVOLUTION (conditional
interfaces). The other six v95 additions retain their scope and ownership:
U-NATIVE-SOURCE-RECEIVER-RECORD, U-NATIVE-RECORD-CONTINUATION-BOUNDARY,
INTEGER-F-JG-INVARIANTS, INTEGER-SEPARATED-FACTOR-CERTIFICATE,
INTEGER-FINITE-PREACTIVATION-QUOTIENT, FIELD-CHARGED-SEPARATION-BOUND.
CARRY-PENTAD already supplies a different integral cyclotomic/J bridge.
No generic cyclotomic identification is claimed as newly discovered here.

## 2. Carrier, equation and equality

All state and matrix equalities are literal, with ordered coordinates.
Integers and rational numbers are exact; no floating point or tolerance.
For every finite integer matrix C of size e by f, e,f nonnegative, set

    T = [[I,C],[-C^t,I-C^t C]],
    E' = E+C M,             M' = M-C^t E',
    H(E,M) = E^t E+M^t M+E^t C M.

The full state is every (E,M) in Z^(e+f). Empty spectral maxima mean zero.
Decide the universal equivalence

    max spec(C^t C)<4 <=> T has finite order
                         <=> every full integer orbit is bounded.

Include C=0, rectangular and rank-deficient matrices, static kernels and
the lambda=4 Jordan boundary. In the stable case derive
mu+mu^-1=2-lambda, lambda=|1-mu|^2 and mu^N=1 for nonzero singular blocks.
Real/rational decomposition must not be advertised as an integer direct sum.

The required critical fixture is exactly the v95 incidence

    Ccrit = [[1,1],[1,0],[1,0],[0,1],[0,1]],    v=(1,1),
    E0=0, M0=v.

Prove or refute, for every n>=0,
E_n=(-1)^(n+1) n Ccrit v, M_n=(-1)^n(2n+1)v, H=2.
An adjacent-triangle assertion is limited to ordinary signed boundary
columns with three distinct unit edge incidences sharing exactly one edge.

## 3. Selected graph and integral Phi5 construction

Declare a finite oriented multigraph, vertices (0,1,2), ordered edges

    e0:0->1, e1:0->1, e2:0->2, e3:2->1.

e0 and e1 are distinct parallel edges. Ordered faces are the digon
c0=e0-e1 and triangle c1=-e0+e2+e3. Boundary uses + at tail, - at head:

    C5 = [[1,-1],[-1,0],[0,1],[0,1]],
    D  = [[1,1,1,0],[-1,-1,0,-1],[0,0,-1,1]],
    G5 = [[2,-1],[-1,3]].

Check C5^t C5=G5 and D C5=0. Raw order is (E0,E1,E2,E3,M0,M1).
Write T and its integer inverse in that order. Define, without replacing it,

    Lambda_act = ker_Q(Phi5(T)) intersect Z^6,
    Lambda_static = ker_Q(T-I) intersect Z^6,
    Phi5(t)=1+t+t^2+t^3+t^4.

Candidate active embedding is (a,b,c,d) -> (C5(a,b),c,d), to be proved
saturated by an integer extraction map. Compute the induced T_act and
energy Gram B with H=x^t B x/2. Produce static basis, integral gluing index
and congruence data, and the relation to each actual D-divergence sector.

Check Phi5(T_act)=0 and exact order five. Set J_act=I+T_act^2; test
charpoly=x^4-3x^3+4x^2-2x+1, trace=3, determinant=1. Test the explicit
module map from Z[t]/Phi5 to Lambda_act sending 1 to (0,0,1,0) and t to
T_act. Exhibit its matrix and inverse, or its exact index/obstruction.
The chosen t means zeta5, not an unrecorded Galois relabeling.

## 4. L5, image, reversal and interface

On precisely Lambda_act set L5=(I-T_act)(I-T_act^2). Decide

    L5 T_act = T_act L5,   L5^2=5 T_act^3,
    L5^* L5=5I,           H(L5 x)=5 H(x),
    det(L5)=25,           L5^-1=(T_act^2 L5)/5 on its image.

Here *=B^-1 (ordinary transpose) B. Produce Smith/Hermite certificates,
an executable necessary-and-sufficient integral image test, and an exact
inverse that rejects nonmembers before division. Test the proposed quotient
(Z/5Z)^2. Distinguish total injection, partial inverse and whole-shell
surjectivity. No shell enumeration is planned or admitted by this pin;
any whole-shell statement must have an independent exact proof or explicit
counterexample, not post-selected finite counts.

For arbitrary finite C also decide R(E,M)=(E+CM,-M), R^2=I, RTR=T^-1.
This is field reversal only. T_act is rotation; J_act is an integer unit
and must be tested against mistaken energy-isometry identification; L5 is
a similitude. Five is energy multiplier and 25 image index.

Analyze L(T) on the full carrier, where it kills static states. Also decide
whether the rational extension that is L on the active space and identity
on the static space preserves the actual integer lattice and divergence.
An obstruction is an accepted outcome. Do not silently use a rational
projection as an integer operation.

The final interface states input/output lattice, image admission, energy
change, retained charges, access to raw registers, inverse and missing
phase/residue/branch data. Any future 5h->h step releases 4h; at h=1 this
is four units, unlike the existing two-unit R18->A20 activation. A future
reaction must fund the remainder explicitly. No completed coupling or
physical particle claim is part of this candidate.

## 5. Code, systematics and independent challenge

This preregistration is committed, pushed and read back before new
scientific execution. Then independent standard-library verify.py and
break.py are written and both frozen in a second public commit before
either executes. Neither frozen file is amended after execution. All file
hashes and both pins are recorded in RUN.md. A separate agent writes
break.py using only this preregistration and public definitions, without
reading verify.py, builder calculations, PROOF.md or outputs. Only after
its source is frozen may results be compared. This is implementation
independence with exposed targets, not independent discovery.

The primary implementation reconstructs matrices from the selected
incidence, extracts the active action, and checks exact certificates.
The challenge uses separately written arithmetic/step construction and
deliberately attacks rank deficiency, critical Jordan growth, bounded
special orbits of unstable C, static Phi1 contamination, unsaturated
bases, image nonmembership, hidden division by five, Euclidean-adjoint
substitution, false J energy isometry, and Gauss claims using the actual D.

Mandatory finite controls: C=0 of size 2 by 3; rectangular C=(1,0)^t;
rank-deficient diag(1,0); critical diag(2,0); unstable diag(3,0) with a
nonzero static integer orbit; Ccrit and C5. Check critical formulas at
n=0,...,12 in addition to the all-n proof. Image arithmetic is checked on
all 5^4 residue classes, with no sampling. No trajectory, shell-range,
detector, helper or multi-cell search is admitted.

Pinned local execution environment: Linux Ubuntu 22.04, x86_64, Python
3.10.12 standard library, LC_ALL=C, LANG=C, TZ=UTC, PYTHONHASHSEED=0,
PYTHONDONTWRITEBYTECODE=1, from repository root, timeout 120 seconds per
script. Record exact stdout in VERIFY.txt and BREAK.txt, empty stderr,
byte counts and SHA-256. These are ordinary admitted text files; no new
transcript exception or policy modification is requested.

Use the current repository policy, Canon, ledger and gate checkers and
normal PR workflow unchanged. The existing changed-path scientific runners
select probes/ and reproduce/, not these notes. Therefore green notes-only
CI is NOT a scientific two-architecture gate for these scripts. If an
admitted second architecture is unavailable, record that gate as unresolved;
never imply it from two agents on one host. No new formal probe, copied
checker rules or ad-hoc formal runner is authorized here.

## 6. Failure thresholds, dispositions and endpoint

One exact counterexample falsifies its affected universal clause; one
matrix inequality falsifies its affected identity. No tolerance. An
unimodularity failure requires the exact index, not a silently smaller
lattice. Missing source custody blocks only attribution/import of that
source. An integrity, syntax, runtime or environment failure is STOP for
the affected execution; preserve it and distinguish it from mathematics.
Frozen assertions/thresholds never change to obtain a passing run. Any
necessary scientific/code correction is an explicit disposition and new
successor pin under current policy, not a backdated alteration.

Endpoint: one reviewed NON-CANONICAL candidate PR with self-contained proof,
exact matrices and certificates, run/evidence limits, clause-by-clause
outcomes, construction-choice account, promotion proposal and exactly one
next scoped task justified by the result. Proof and finite audits are
distinguished. No earned public status is asserted by this note.

No Canon, release, sealed probe, shared checker, workflow or H/O owner
changes; no merge/tag/release. QDD-INSTRUMENT-APPARATUS,
QDD-TERMINAL-EVENT-SEMANTICS and PHOTON-MASSLESS-PHASE retain every obligation.
The 666-helper census, local coupling and multi-cell propagation remain
separately scoped later tasks.
