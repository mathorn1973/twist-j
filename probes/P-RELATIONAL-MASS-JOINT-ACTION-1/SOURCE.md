# Authority, source custody and declared common action

Status: PROSPECTIVE, NON-CANONICAL, NEW_DECLARED L1
Owner: A. M. Thorn
Ownership: https://github.com/mathorn1973/twist-j/issues/1686

## Public authority

The base is public main 4d345bf1c73da73c1922fdba9893ee5644742275,
the merge of #1685, with tree 6ce92a432db1f073eb543c680a9d5bba3fc0140f.
Required run 39457835386 passed on this exact head. The aarch64,
x86_64 and aggregate logs were read back; both architectures passed the
policy, Canon and reproduction gates, and the aggregate reported
TWO-ARCHITECTURE CHECK PASS. This is evidence for the baseline, not an
execution or result of the present probe.

Public Canon v103 remains ACTIVE. The annotated canon-v103 tag object is
e78420dcd80c4e55e3fe39ddd06c004a6810890b and its peeled commit is
dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d. The declared content commit is
01fb76f6b3b14a6a5ec05d0017ea922390ab6f66. Both commits are ancestors
of the base. The five normative files were checked against SHA256SUMS:

| Path | Bytes | SHA-256 |
|---|---:|---|
| canon/CANON.md | 1052518 | d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b |
| canon/CORE.md | 30714 | 9d5617a163bc7a4e1964d41861ff7f2f44009117c61debe08a4e1547c88be728 |
| canon/FRONTIER.md | 27382 | 8574c3d4b0cc70278dec7d64e2a51022718cc54497c64025d9e6021775fcbaf0 |
| canon/REGISTRY.tsv | 532811 | 5cd008147435bf1facfe93b2e05d9d7e41554d73f647ad09659aac002195890d |
| canon/CHANGELOG.md | 207770 | 79f6bd8f30b1f845ae918b7374049f4bf8e0a2270e89b4c5223469a93855f078 |

The administrative baseline is also byte-bound:

| Path | Bytes | SHA-256 |
|---|---:|---|
| STATUS.md | 2391 | 6ff52d4fc3bdeb210fe2c8ae89d54d4e5f21dfccb63aa37ddad281710ef21375 |
| POLICY.md | 17333 | da5d2cf5a021f4d069c471725e02b6d2c201e3acadd5ecfd4213a361184b7a5d |
| AGENTS.md | 21813 | 7363b83ca6d822ec35e8465fe64c1aa8cd0007bf8b99ae599c265cc49fcee6e1 |

## Public predecessor and retained definitions

The immediate predecessor is P-RELATIONAL-MASS-METRIC-RESPONSE-1,
claimed in #1684 and merged by #1685. Its prospective commit is
b5c8466118e546f8d93ea2071cb42ef018b6b2b6; its result commit is
4d6603d8d9fb6d2fb9eea0421a4e93ddbca81893. Public pre-execution and
post-merge receipts are issue #1684 comment 6295661391 and PR #1685
comment 6295856079. The public proof and provenance at the base are:

| Path under probes/P-RELATIONAL-MASS-METRIC-RESPONSE-1/ | Bytes | SHA-256 |
|---|---:|---|
| PROOF.md | 19980 | f93874f3e00e965a221c9968ae4c4e25358f82cb07d4ffde5b173c592750a828 |
| SOURCE.md | 6936 | acbcd2a950059467ce1a3f08f556fba98f9cb4b2b0cb35f20ee913934b900fe4 |

Its scalar field is F=Q(phi), phi^2=phi+1, with gamma=phi-1. In the
real basis (1,j), its five reference covectors are (1,0), (0,1),
(-1,gamma), (-gamma,-gamma), (gamma,-1), and
G0=[[1,gamma/2],[gamma/2,1]]. These are marked reference data, not a
unique physical metric or five continuously fixed matter histories.

For nonnegative counts n_k and fixed nonzero covectors u_k, the predecessor
defines epsilon_k=sqrt(u_k^T G u_k), E=sum n_k epsilon_k,
P=sum n_k u_k, D_G=E^2-P^T G P,
T_G=sum (n_k/epsilon_k)u_k u_k^T, and R_G=E T_G-P P^T.
Its Frobenius variation gives dE[H]=tr(T_G H)/2 and
dD_G[H]=tr(R_G H). The present common proof states and derives the
identities it needs. No predecessor program is imported, executed or used
as an oracle by a new implementation.

The predecessor supplies metric response, positivity/rank statements and a
visible affine-strain quartic obstruction to quadratic scalar closure. It
does not supply metric momentum, a metric kinetic term, matter equations,
a common action for this carrier, or a map from an old scalar h to G.
The earlier scalar and fixed-duration results (#1666 and #1678) remain
conditional results for their own carriers and variational problems.

## Historical source custody and limits

The following user-supplied texts were consulted for continuity. They are
historical or strategic context, not an alternative authority to public
main. Only their names and custody hashes are retained here; no archive
payload is imported.

| Supplied text | Bytes | SHA-256 |
|---|---:|---|
| 29-TWIST-J_memo_nadhled-1-.md | 16222 | 3fbd7137724036c30db0194cb9856699dae0fcdacfeb33774e4377b625587723 |
| 27-v176.md | 178063 | a5df28b2301d7b518426d38388c343831023b832b281eee80b8c82bbc3633ac7 |
| 28-TWIST_J_Canon_v184_ALL_IN_ONE.md | 230406 | cd92b8bba54658e154e8fc05eb562749f04c70b134dcc728c7236ed10378ef80 |

The memo was read in full; the two historical compilations were read in
the targeted gravity/action sections. The memo motivates explicit choice
accounting, fixed falsifiers and separation of mathematical construction
from physical realization. Its historical emphasis on a unique reading
does not override current policy: multiple independently admitted readings
may coexist. No global uniqueness claim is introduced.

The earlier outcome-exposed relational-mass proposal is already documented
in the public predecessor: PROMO-C-RELATIONAL-MASS-1.zip, 29717 bytes,
SHA-256 d0d4495d0d3d1a0cb675e93e46bf3d316dc9408ceb09b422199979cd797f5527.
It is neither public authority nor an independent prospective result of
this probe. Its programs are not inputs to the new authors or replay.

Current Canon scope governs every historical comparison. FRW-CANONICAL-FORM
does not include source-projector uniqueness, rho=rho0 ell^2 or E_total=0.
The retained FRW-INHOM construction already has a selected cubic hybrid
action; this probe does not claim to be the first common action in TWIST-J.
That construction is not a full nonlinear inhomogeneous completion. The
retained TT-SOURCE result is a selected outgoing source law, not full
microscopic depletion or nonlinear backreaction. Historical quadratic
TT 2-jet equivalence is not a nonlinear completion; tensor/vector pullback
Hessians and different normalization pairings cannot be interchanged.

## New declared action choices

The new carrier is the full real symmetric positive-definite 2 by 2 inverse
metric G with symmetric conjugate momentum Pi. Its declared kinetic energy
is K(G,Pi)=tr(G Pi G Pi)/(2 mu), with the explicit normalization mu=1.
This replaces the old scalar carrier. Neither an inherited M0 transfer nor
a hidden h-to-G identification, scalar Ward closure or old quadratic
normal form is assumed.

The n_k are fixed nonnegative integer labels. For every occupied species,
x_k and the nonzero real covector p_k are continuously varied in the action
before imposing equations of motion. The symplectic term is weighted:
sum n_k p_k^T dot{x}_k. Unoccupied species are omitted from this term and
from the phase space. The common action pairs tr(Pi dot{G}) with this matter
term and Hamiltonian K+E, where E=sum n_k sqrt(p_k^T G p_k).
Constancy of p_k in the homogeneous model must follow from its equation
of motion; it is not a frozen matter trajectory inserted before variation.

The common proof must account for metric/matter energy exchange and the
simultaneous GL(2,R) transformation of positions, covectors, G and Pi.
This is coordinate covariance of the declared finite-dimensional model,
not a proof of physical gauge freedom or Lorentz completion. The reference
five-direction preparation is a chosen initial marking, not an invariant
restriction that forbids varying occupied momenta.

The exact time-one Hamiltonian flow and a separately specified
discrete-gradient energy-preserving step have different claims. Energy
preservation of the latter does not establish that it is symplectic,
action-derived or equal to the time-one flow. Any exact algebraic step
requires its own stated domain and positivity check. Neither construction
alone supplies an explicit native integer/rational update or a layer lift.

This remains a declared mathematical L1 model. It does not select a physical
metric, source localization, spacetime continuum, lapse/clock, SI units,
native L2 realization or L5 interpretation, and does not prove equality of
inertial and gravitational mass. Public decoder order remains matter to
geometry to clock; decoded outputs do not feed the native update U.

## Independence and prospective discipline

The coordinator and proof reviewers have read the public predecessor and
the historical context. This is same-session analytical review, not external
blind review. Two independent program authors receive only the present
common contract and proof; neither receives a predecessor scientific
program or the companion implementation. No archive program, predecessor
result transcript or companion output supplies scientific values to either
independent calculation. The primary compares the completed certificates
as specified in PREREG.md.

Before any new scientific execution, import or fixture evaluation, six
prospective files must be committed, pushed and read back in full:
PREREG.md, PROOF.md, SOURCE.md, verify.py, breaker.py and FROZEN.sha256.
The manifest binds the other five files. Source inspection, AST parsing and
byte/hash checks are administrative review, not scientific execution.
The frozen contract and proof determine domains, fixtures, exact gates and
falsifiers; this provenance document records no earned outcome. No
post-outcome threshold, fixture or scientific-code replacement is allowed.
Completed FAIL and incomplete abandoned execution remain distinct under
POLICY. A later public fold is required for any Canon promotion.
