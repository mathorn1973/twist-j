# Preregistration: selected two-wing law and five-context Bell witness

PUBLIC; NON-CANONICAL. P-QDD-SELECTED-BIPARTITE-LAW-1.
Owner: A. M. Thorn / selected-bipartite session 2026-09-20.
Lock: https://github.com/mathorn1973/twist-j/issues/1095.
Base: `19b88a43314fa2381ba353b9b2af614bd653ae54`.
Authority: Public Canon v90 ACTIVE, unchanged by this probe.
The author approved continuation of the selected-theory program and the
connected GitHub contributor identity. This is not blinded model selection.

## 1. Equation and conditional claim

Freeze the full ETH-QDD-2 contract in MODEL.md, extending the accepted
ETH-QDD-1 source metric, five projectors and coarse instruments. The two-wing
carrier has metric Gamma=G tensor G, G=I4-ones4/5, with selected source
phi=vec(G^-1)/2 and density rho_Phi=phi phi* Gamma. Local settings are
x,y in {0,...,4}; LOW/HIGH projectors are Pk,Qk. Independent uniform
external settings and Born occurrence are chosen inputs. The whole trial law
is

    Pr(x,y,a,b)=(1/25) tr[(M_(x,a) tensor M_(y,b)) rho_Phi
                          (M_(x,a) tensor M_(y,b))].

Targets include both no-signalling identities and the stronger local-record
no-message statement for every finite local causal protocol with fixed
preparation independent of the remote message. This is a mathematical
operation class, not a physically established spacetime separation.

The complete Bell-local comparison class has arbitrary normalized source
measure independent of settings and arbitrary normalized local responses.
For

    B=2 sum_k p(LL|k,k)-sum_(k!=l) p(LL|k,l),

prove B<=2 throughout that class, while B_Phi=35/16. Prove the fixed-effect
quantum maximum is exactly 35/16 with rho_Phi its unique maximizing density.
Every two-setting CHSH form of the same table has absolute value <=2.
The preregistered noise family gives B(v)=(45v-10)/16 and this witness
exceeds two exactly when v>14/15. This is not a full locality threshold.

No native source, single-checkpoint tensor factorization, material randomness,
physical isolation or empirical confirmation is inferred from these targets.

## 2. Carrier, code, data and frozen custody

The verifier uses standard-library exact rational arithmetic. It reads no
runtime Canon files, predecessor code, external data, random samples or
network resources. All finite-state positive witnesses have declared exact
densities. Rational matrix units span the complex operator space by complex
linearity; they are operator test inputs, not physical states.

Before first scientific execution commit, push and read back exactly:

    probes/P-QDD-SELECTED-BIPARTITE-LAW-1/PREREG.md
    probes/P-QDD-SELECTED-BIPARTITE-LAW-1/MODEL.md
    probes/P-QDD-SELECTED-BIPARTITE-LAW-1/PROOF.md
    probes/P-QDD-SELECTED-BIPARTITE-LAW-1/REVIEW.md
    probes/P-QDD-SELECTED-BIPARTITE-LAW-1/verify.py
    notes/canon/SELECTED-BIPARTITE-FOLD-PROPOSAL.md

An independent agent reviews the written mathematics before reading the new
verifier. Written analytic derivations and static syntax inspection precede
the pin; no scientific gate or numerical search is allowed before it.
The explicit table, Bell bound and spectral formula are already known from
those derivations and receive no blind-discovery credit.

## 3. Frozen exact gates

G1. Recheck the inherited metric, inverse, R isometry, five complementary
projector pairs and tight-frame identities. Check the chosen sixteen-entry
phi and its density, normalization, purity and both reduced densities I4/4.
The four physical fixtures are rho_Phi, I16/16, P0 tensor P1, and the
normalized pure state e0 tensor e0+e1 tensor e1 in Gamma.

G2. For all 25 setting pairs and four outcomes, audit the full primary joint
table, branch traces and normalization, local-order commutation and Kraus
completeness. The diagonal table is (1/4,0,0,3/4), the off-diagonal table
(1/64,15/64,15/64,33/64) in order LL,LH,HL,HH. Audit the general-state
identities on the four fixtures without claiming this finite set exhausts
all densities. Never normalize a zero branch.

G3. Audit both marginal-preservation identities for the nonselective remote
channel on every one of the 256 tensor operator matrix units, for all five
remote settings, and the two operational marginals on the four fixtures.
The universal complete local-protocol result rests on the written CP-map
proof, not on extending these finite samples by assertion.

G4. Enumerate all 1024 deterministic local LOW-set pairs. Check the formula
B=3c-ab and exact maximum two, then compare the independently computed
quantum joint table, whose value must be 35/16. The proof shows why this
census also bounds every setting-independent stochastic hidden-variable
representation, with no finite-support assumption on its original measure.

G5. Check the exact Bell operator, its spectral certificate and multiplicities:
35/16 once, 5/4 four times, -25/16 eleven times. Its top spectral projector
must equal rho_Phi. Audit the sharp fixed-effect bound, not a claim about
optimization over unspecified measurement families.

G6. Enumerate all 625 ordered setting quadruples and all eight CHSH sign
patterns with product -1. Check all 5000 forms, including repetitions,
against the computed E table; exact maximum absolute value is two.

G7. Check the complete depolarized joint table and the affine Bell law at
v=0,14/15,1 and rational witnesses strictly below and above the threshold.
The written proof supplies the full interval statement. A failed violation
below threshold does not certify locality.

G8. Audit complete local adaptive histories with two explicitly coded causal
policies per wing through depth three. For the four registered sources and
four policy pairs, all 64 joint outcome-word pairs per policy pair give 1024
leaf pairs and 1360 prefix pairs. The two local policies are
k0(h)=(len(h)+sum_i (i+1)h_i) mod5 and
k1(h)=(2+2len(h)+sum_i (i+2)h_i) mod5, with LOW=0, HIGH=1.
Check normalization, prefix consistency and both comparisons
of local marginals under a change of the remote policy. Audit retained-pair
repeatability versus whole-pair replacement and the fresh-trial product law.
General finite histories and finite local memories are covered by proof.

G9. Check exact selective steering P_y and Q_y/3 and their average I4/4.
For all 25 setting pairs, construct the setting-dependent separable source
sigma_(x,y) from MODEL (6); verify that it reproduces the same promised
table and has both marginals I4/4. Verify that these are genuinely different
sources for different settings. This negative control drops measurement
independence; it is not a local representation with one common source law.

G10. Preserve the no-message boundaries with exact controls: remote
postselection changes a conditional local probability, while the unselected
marginal remains fixed; allowing a source to depend on the remote message
can change the local marginal. An explicit communicated-control witness also
has Bob measure context zero and send his outcome: Alice uses context zero
after LOW and one after HIGH, giving Alice LOW probability 31/64 versus 1/4
with fixed context zero. These are not admitted local-only message protocols.
Check typed ZERO_SUPPORT and zero-probability branch handling.

Print deterministic G1-G10 audit lines and verdict
SELECTED-BIPARTITE-LAW, explicitly conditional on the selected inputs.
Save the actual first completed stdout byte for byte as EXPECTED.txt.

## 4. Systematics and failure threshold

One exact admitted counterexample refutes its corresponding target. A genuine
written-proof gap blocks candidate-T acceptance even if finite tests pass.
Specific scope failures include confusing covariance with operator density,
using a same-complex-rotation invariance not supplied by the real alignment,
calling CHSH nonviolation a proof of full locality, omitting half the ordered
Bell sum, replacing setting independence by marginal equality, hiding remote
postselection or loss selection, assuming reduced CP maps for arbitrary
correlated memories, treating repeated reads as fresh trials, or representing
two code copies as a factorization of one Omega state.

The frozen six files, source, table, gates and thresholds must not change
after pin. An incomplete first scientific execution consumes the identifier
and requires ABANDONED disposition under POLICY. A completed exact
counterexample must be preserved at its actual scope. Hash or architecture
byte mismatch is STOP, not permission to repair the frozen science.

There are no acquired measurements, fitted quantities, empirical error bars,
timing waveforms, SI assignments or physical noise calibrations in this probe.
Future laboratory tests require their own preparation, control and error
contract. No claim of novelty or empirical discrimination from standard
quantum mechanics is made.

## 5. Layers, adopted inputs and disposition

Conditional operator, probability and Bell-class theorems are L1 mathematical
statements. The selected physical roles are L4 supports/operations, L5 local
records and L6 occurrence law. Future dictionary bridges are separately named

    GATE-L1-L4-SELECTED-QDD-PAIR
    GATE-L4-L5-SELECTED-QDD-LOCAL-RECORD
    GATE-L5-L6-SELECTED-QDD-PAIR-LAW.

No physical bridge is passed by a finite algebraic audit. All predecessor CH
inputs and the five additional choices in MODEL are explicit. The source and
setting-law independence are adopted premises, not generated native samples.

After a completed first run add EXPECTED.txt, parser-compatible RUN.md and
RESULT.md. After public replay add ACCEPTANCE.md; require x86_64, aarch64,
aggregate check, final-head and merged-main readback, preserving the immutable
pin in a merge commit. The proof, independent review and exact verifier have
separate evidentiary roles.

BELL-CAUSAL-ACCOUNTING and the QDD physical apparatus, terminal and complete
class owners keep their original scopes. #539 and feeds_U=false are unchanged.
The adjacent pure-qubit and AME branches were collision-checked and remain
untouched. This probe contains one new probe directory and one prospective
fold note. No canon/, STATUS, workflow, release or old probe is altered.
