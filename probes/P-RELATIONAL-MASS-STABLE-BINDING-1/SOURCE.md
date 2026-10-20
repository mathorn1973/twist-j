# Authority, source custody and the declared binding choice

Status: PROSPECTIVE, NON-CANONICAL, NEW_DECLARED L1
Owner: A. M. Thorn, session relational-mass-stable-binding-2026-10-20
Ownership: https://github.com/mathorn1973/twist-j/issues/1688

## Fresh public authority

The base is public main 8a2e6a3b1f35bfc2e2616c340086a7182ffbc050,
the merge of #1687, with tree 14f9477568500bf743d8fcf3b6eb1b809f1d1345.
The clean local main and fresh origin/main agreed before branching.
Required push run 39462550354 is successful on that exact head. Fresh
actual logs were read for x86_64 job 118765469361, aarch64 job
118765469937 and aggregate job 118766064922. Both architecture logs
show Python 3.12.15, 189 tests, POLICY PASS, CANON PASS v103 claims=530,
and passing ledger/gate checks. Both reproduce the predecessor with
verifier SHA-256 64fa4fd8198d778185d5c5e4cd7429accfc2f2d002bf284746ffbc7df922e104
and stdout SHA-256 a59dd2310ae9f3bface7a738c561a7290d9fe4af2e4d39a5f048b771f1ca2642.
The aggregate log says TWO-ARCHITECTURE CHECK PASS. These are baseline
receipts, not results of this new probe.

Public Canon v103 remains ACTIVE. The annotated canon-v103 tag object is
e78420dcd80c4e55e3fe39ddd06c004a6810890b; the peeled commit is
dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d. The declared content commit is
01fb76f6b3b14a6a5ec05d0017ea922390ab6f66. Both ancestry checks to the
base passed. Fresh byte checks matched all five normative hashes:

| Path | Bytes | SHA-256 |
|---|---:|---|
| canon/CANON.md | 1052518 | d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b |
| canon/CORE.md | 30714 | 9d5617a163bc7a4e1964d41861ff7f2f44009117c61debe08a4e1547c88be728 |
| canon/FRONTIER.md | 27382 | 8574c3d4b0cc70278dec7d64e2a51022718cc54497c64025d9e6021775fcbaf0 |
| canon/REGISTRY.tsv | 532811 | 5cd008147435bf1facfe93b2e05d9d7e41554d73f647ad09659aac002195890d |
| canon/CHANGELOG.md | 207770 | 79f6bd8f30b1f845ae918b7374049f4bf8e0a2270e89b4c5223469a93855f078 |

The administrative baseline is unchanged and freshly checked:

| Path | Bytes | SHA-256 |
|---|---:|---|
| STATUS.md | 2391 | 6ff52d4fc3bdeb210fe2c8ae89d54d4e5f21dfccb63aa37ddad281710ef21375 |
| POLICY.md | 17333 | da5d2cf5a021f4d069c471725e02b6d2c201e3acadd5ecfd4213a361184b7a5d |
| AGENTS.md | 21813 | 7363b83ca6d822ec35e8465fe64c1aa8cd0007bf8b99ae599c265cc49fcee6e1 |

## Collision and predecessor scope

Before claim #1688, explicit git ls-remote --heads origin read 295 remote
heads. Exact identifier searches found no match in refs, repository probes,
notes, registry, public issues or pull requests. Related binding,
oscillator, momentum, relative-position, harmonic, stable, covector and
stabilizing searches were inspected. Separately occupied lanes include:

| Lane | Distinct owned scope |
|---|---|
| #1642 / #1644 | Integer parity-dipole feedback and forced source oscillator |
| #1659 / #1669 | Local parent, scalar lapse and Noether completion |
| #1406 / #1407 | Fixed-support bound-charge displacement and field coupling |
| #1412 / #1413 | Unadopted Hilbert endpoint/gauge Hamiltonian |

None supplies the full-SPD relational pair potential declared here. Their
claims, pending work and preserved outcomes are not reopened. This session
owns only probes/P-RELATIONAL-MASS-STABLE-BINDING-1/.

The direct predecessor P-RELATIONAL-MASS-JOINT-ACTION-1 was claimed in
#1686, frozen at f19fa98dc1634ce1e17b9dec402c51920d2bea8d and completed
at 778333f1f3dfe90c42a17b0a3a660c46fad88db9 before merge #1687.
Its prospective public receipt is #1686 comment 6296327470. The merged
probe tree is 6f85719090a180d6b1d83184b341f675687f665e. Relevant public
text at the new base is bound by:

| Path under probes/P-RELATIONAL-MASS-JOINT-ACTION-1/ | Bytes | SHA-256 |
|---|---:|---|
| PROOF.md | 23220 | 8be6da2db3a7b354d5920c4bce60b54646654bf325becfa86ed4e67a8ddf29d5 |
| SOURCE.md | 9412 | 2bd4b59e92f846932f1980c9866c8b620ff07cddc774b173a2e5c8f78da44e67 |
| RESULT.md | 6844 | 77c174f4145e4b1de0951574918f5a2a00fdd6df97d2b627aef8ce14169a02c3 |

That predecessor gives one declared common action, energy exchange, GL(2)
charge and complete SPD flow with no added stabilizing potential. Its
nonempty matter energy tends to zero at both time infinities, and it has
no nonempty equilibrium or periodic full orbit. These delimit that action;
they do not exclude actions with newly declared terms. Its separate DG
step has a proved charge defect and a regular nonsymplectic witness.
Neither that step nor its certificate is a new binding solver or oracle.

## The new choice and the exact sector

The full real SPD inverse metric G, symmetric momentum Pi, Frobenius
pairing and metric kinetic energy K=tr(G Pi G Pi)/2 are retained. The
normalization remains explicitly one. There is no scalar h-to-G map,
inherited M0 transfer or scalar Ward completion.

The new term is the proper pair potential V=kappa r^T G^-1 r, kappa>0.
It is translation invariant and covariant under the same simultaneous
GL(2,R) coordinate changes. Both the functional form and coefficient are
new model declarations. No theorem selects kappa from J, native U,
historical mass-volume assertions or a measured mass.

The declared sector has two equally weighted occupied groups, with unit
multiplicities and total momentum P=p1+p2=0. Define

    r=(x1-x2)/2, rho=2p1=-2p2,
    E=sqrt(rho^T G rho), V=kappa r^T G^-1 r,
    H=K+E+V, theta=tr(Pi dG)+rho^T dr.

Thus E is exactly the sum of the two individual energies and rho is the
momentum canonically paired with the half-separation r. These factors of
two are part of the frozen carrier. Translation reduction does not freeze
the relative position or its conjugate momentum before variation.

Both matter variables are continuously varied, and the new potential
makes the momenta evolve. The predecessor's constant nonzero momenta no
longer prove avoidance of zero. The prospective binding theorem instead
uses the conserved charge J=2G Pi+r rho^T and the strict sector

    delta=det J-(tr J)^2/4 > 0.

This is a sufficient condition on the initial charge, not a charge
generated by starting with Pi=0. At Pi=0, J=r rho^T and delta<=0, so
the protected sector requires nonzero initial metric momentum. The common
proof must justify its energy/proper-separation bounds, nonvanishing
source energy and avoidance of zero momentum on the complete flow.

The bound concerns the proper half-separation sqrt(r^T G^-1 r); the pair
separation is twice that value. It does not bound the raw coordinate
vector while G evolves. Robustness is restricted to the stated two-group
P=0 sector and the exact positive-delta condition. Bounded separation
alone is not orbital stability, nor does it imply robustness under
arbitrary nonzero total momentum. Any periodic relative-equilibrium or
fixed-charge orbital-stability claim must be separately proved and stated
in the common proof and contract before pinning.

The ambient common action admits arbitrary continuously varied real
covectors. Antipodal momenta are allowed there, but they are not two
members of the old five distinct fifth-root directions. No native
five-direction catalogue or discrete momentum restriction is inherited.
The reference arithmetic used for an exact finite audit does not restrict
the real phase space of the analytical theorem.

## Historical custody and authority limits

The strategic memo was reread in full and the historical compilations in
their relevant gravity, matter and action sections. Fresh byte hashes
match the previously recorded user-supplied texts:

| Supplied text | Bytes | SHA-256 |
|---|---:|---|
| 29-TWIST-J_memo_nadhled-1-.md | 16222 | 3fbd7137724036c30db0194cb9856699dae0fcdacfeb33774e4377b625587723 |
| 27-v176.md | 178063 | a5df28b2301d7b518426d38388c343831023b832b281eee80b8c82bbc3633ac7 |
| 28-TWIST_J_Canon_v184_ALL_IN_ONE.md | 230406 | cd92b8bba54658e154e8fc05eb562749f04c70b134dcc728c7236ed10378ef80 |

No binding potential or mechanical oscillator for this SPD carrier was
found in those texts. Historical Part XVII mass-volume/proton assertions
do not supply a physical binding mechanism. Current MATTER-SCALAR rows
insert mu and exclude interaction, stability and physical mass origin;
MASS-LADDER-FORMS is a declared formula register; the color dictionary
does not prove confinement; PROTON-RESIDUAL-IS-QCD remains open and STOP.
Historical source-projector uniqueness, rho=rho0 ell^2 and E_total=0 are
expressly outside current FRW-CANONICAL-FORM and cannot select a stabilizer.

The memo requires accounting for every new choice and distinguishing a
mathematical construction from physical realization. Its historical
global-uniqueness rhetoric does not override current reading-family
policy. Existing Canon FRW joint actions retain their own scope; this
probe makes no first-common-action claim. Decoder order remains matter,
geometry, clock, and decoded outputs do not feed native U. No physical
particle identity, SI scale, source localization, native realization,
inertial/gravitational mass equality or unnamed layer lift is supplied.

## Independence and prospective discipline

The coordinator and analytical reviewers know the predecessor and the
prospective proof. This is same-session review, not external blind review.
Two new isolated code authors receive the present common contract and
proof, without a companion implementation or predecessor scientific
program. No historical program or predecessor transcript supplies values
to their independent calculations; completed certificates may be compared
only as specified in the frozen contract.

Before any new scientific execution, import or fixture evaluation, freeze,
commit, push and read back all six complete prospective files: PREREG.md,
PROOF.md, SOURCE.md, verify.py, breaker.py and FROZEN.sha256. The manifest
binds the other five. Read back the public pin receipt before the first
run. Source inspection, AST parsing and byte/hash checks may precede it;
scientific dry runs may not. No outcome-based change of fixture, threshold,
domain or scientific code is permitted. Completed FAIL and incomplete
abandoned pins retain their distinct POLICY dispositions. This source
document records no earned result and does not promote Public Canon.
