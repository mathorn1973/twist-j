# Sources, authority and declared additions

Status: PROSPECTIVE  
Scope: NON-CANONICAL, NEW_DECLARED L1  
Probe: P-INTEGER-LOCAL-PARENT-CLOSURE-1  
Owner: A. M. Thorn, session integer-local-parent-2026-10-19  
Ownership: https://github.com/mathorn1973/twist-j/issues/1659

## Public authority

The only normative baseline is the actual public repository
mathorn1973/twist-j. At this session's authority check, main and peeled
canon-v103 both resolve to dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d.
STATUS.md declares STATE: ACTIVE, Public Canon v103, and content commit
01fb76f6b3b14a6a5ec05d0017ea922390ab6f66. Required workflow 39022927713
is completed/success at the declared main commit.

All five files were read from the fetched public tree, byte-counted and
hashed. Both implementations independently check these actual file bytes:

| Path | Bytes | SHA-256 |
| --- | ---: | --- |
| canon/CANON.md | 1052518 | d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b |
| canon/CORE.md | 30714 | 9d5617a163bc7a4e1964d41861ff7f2f44009117c61debe08a4e1547c88be728 |
| canon/FRONTIER.md | 27382 | 8574c3d4b0cc70278dec7d64e2a51022718cc54497c64025d9e6021775fcbaf0 |
| canon/REGISTRY.tsv | 532811 | 5cd008147435bf1facfe93b2e05d9d7e41554d73f647ad09659aac002195890d |
| canon/CHANGELOG.md | 207770 | 79f6bd8f30b1f845ae918b7374049f4bf8e0a2270e89b4c5223469a93855f078 |

POLICY.md SHA-256 is
da5d2cf5a021f4d069c471725e02b6d2c201e3acadd5ecfd4213a361184b7a5d;
AGENTS.md SHA-256 is
7363b83ca6d822ec35e8465fe64c1aa8cd0007bf8b99ae599c265cc49fcee6e1.
These policy files were read; their contents are not amended here.

The canonical K1 spatial operator and the finite polynomial action/reading
context are inherited only at their declared scopes. In particular the
canonical hybrid cell-metric construction is not assumed to be an all-order
Einstein-Hilbert action, and no continuum/local gauge symmetry is imported
by attaching that interpretation to a quadratic action.

The five-site planar reduction, graph orientation, source localization,
constant reciprocal coupling and auxiliary action of the companion probes
remain declared model choices. The native U and the physical decoder are not
modified or realized by this probe.

## Non-canonical companion evidence

All companion references below are NON-CANONICAL L1 sources, not Canon
promotions. The new implementations are self-contained and do not import
earlier probe programs at runtime.

| Companion | Immutable pin | Inspected result or corrected head | Used content |
| --- | --- | --- | --- |
| P-INTEGER-AUTONOMOUS-JOINT-ENERGY-1, issue 1649 / PR 1650 | edfedd7e75c515d6d318032f526f381f66317da3 | a17fe5f2198f1693277b45bcf7c55458e8c2c381 | Autonomous action, reciprocal equations, total bond energy and offset |
| P-INTEGER-NONLINEAR-CONSTRAINT-PROPAGATION-1, issue 1651 / PR 1652 | 5e072359a029233d1c2b266c0c4bed2269752535 | 98ec11dfd25f4a7b9b890fb03b484b0c0e24313e | Vertex density, edge current, auxiliary Hodge constraints at corrected scope |
| P-INTEGER-CUBIC-NOETHER-CLOSURE-1, issue 1653 / PR 1654 | d978a878dd6044d7ba297d8402195a522e6fc8f8 | 350eb009516f29b6f98c4afb48e3820e6336bc33 | Complete finite-horizon action, first-order identity, generator and obstruction witnesses |
| P-INTEGER-SECOND-ORDER-NOETHER-CLOSURE-3, issue 1655 / PR 1658 | 56437c4ef2c2e3a5aee679bb87b693395213f644 | 96b100322f5301293cefb382ac47b4ed5c484ad3 | Exact S2 and delta2 formulas, residual decomposition, third/fourth-order defects |

The actual latest #1652 RUN.md was read remotely to confirm its prospective
pin. Its corrected PR scope separates the inherited local continuity identity
from full variations of a modified nonlinear action. This probe does not
restore the earlier overbroad description.

The direct #1658 predecessor was independently reviewed and replayed before
this probe, with the review publicly posted at
https://github.com/mathorn1973/twist-j/pull/1658#issuecomment-6278532920.
Its six frozen files are unchanged at the result head. Primary stdout is
1022 bytes / 27 LF, SHA-256
16dd61af54d97da110bd5d01eaabb834d2b656e4c9bac69874dcca4a584075ee.
Standalone breaker certificate is 982 bytes / 25 LF, SHA-256
3e1550f997b5658d8e65fbd00b209789b3f6128ae19a8b89dbf6a62829c8ae75.
Actual x86_64/aarch64 and aggregate job logs of workflow 39322225560 were
read and agree with the exact hashes. This is independent review and replay,
not a blinded experiment whose expected results were hidden.

The review requires these predecessor documentation corrections while
preserving its frozen files and EXPECTED.txt:

- The two-point quotient is 175/2592, not 157/1296; the exact derivative
  remains 47/1296 and the defect remains 1/32.
- Its frozen SOURCE.md contains a truncated normative registry digest. The
  correct digest is the complete 64-hex value in the authority table above.
- Its frozen SOURCE.md prints incorrect full pin and corrected-head SHAs for
  #1652. The correct values are those in the companion table above.
- The 1140 parameter pairs are unordered, 6*binom(20,2).

Those transcription defects are not consumed as inputs to the new probe.
The actual pinned equations and reproducible witnesses are the inputs.
No failed pin of the present identifier exists before this prospective run.
The two earlier consumed second-order probes, IDs ending -1 and -2, remain
preserved on their own branches/PRs 1656 and 1657; this probe neither resumes
nor renames them.

## Explicit new choices and proved distinctions

| Item | Status in this probe |
| --- | --- |
| Selected pullback S_exact and coefficient S3 | NEW_DECLARED L1 completion matching the predecessor through order two |
| Independent local state (y,theta,r,nu,tau,p) | NEW_DECLARED L1 parent coordinates; dimension preserved at fixed horizon |
| Exact translation action and equality of gauge orbits | NEW_DECLARED L1 gauge/equivalence contract with complete invariant tuple |
| Old-coordinate regular chart and finite transition maps | NEW_DECLARED L1 partial chart; exact domain det K_theta !=0 |
| Local state reconstruction and integer shear | NEW_DECLARED representation law using the lapse as input, not a native clock law |
| Canonical common-denominator encoding | NEW_DECLARED finite-horizon arithmetic convention, including all endpoint numerators |
| Stationary auxiliary elimination and terminal condition | Self-contained exact consequence of the selected parent action |
| Continuant nonlocality and singular-chart counterexamples | Self-contained exact limits of the old-coordinate inverse |
| Gauge-invariant metric read from y | NEW_DECLARED reader agreeing with the old h reader at theta=0; no tensor covariance claim |
| Alternative invariant quartic J | Nonuniqueness control only, not an adopted interaction or selected gravity theory |

The exact local parent does not make the old-coordinate inverse local.
Global gcd normalization does not become a bounded-stencil integer update.
The selected parent has no new nonlinear bulk dynamics after its auxiliary
equations are applied. That conclusion is about this specified completion,
not an impossibility theorem for all integer gravities or all consistent
higher-order interactions.

## External context, with no imported theorem

G. Barnich and M. Henneaux, "Consistent couplings between fields with a gauge
freedom and deformations of the master equation", Phys. Lett. B 311 (1993)
123-129, https://arxiv.org/abs/hep-th/9304057.
The primary source distinguishes general functional deformations from local
ones and discusses simultaneous deformation of actions and generators. It is
context for asking the locality/equivalence question. No BRST complex, master
equation solution, cohomology classification or theorem from that paper is
asserted for TWIST-J here. All actual claims in this probe are proved directly
in PROOF.md and audited by the frozen programs.

## Implementation and custody contract

The primary author and separate breaker author receive the same prospective
equations, fixtures, payload grammar and falsifiers. They use different state
encodings, inverse constructions and differentiation strategies. They do not
read/import each other's new program or derive fixtures from a first run.
An additional static mathematical reviewer audits the proof and source before
pinning. This is authoring separation inside the present session, not a claim
of a later blinded acceptance review.

The breaker adapts basic Fraction, Dual and incidence-arithmetic patterns from
the already reviewed #1658 standard-library implementation. Its native tuple
carrier, rational polynomial arithmetic, full temporal matrix and Dual
Gaussian elimination, stationary rank classification and canonical storage
are independently authored for this probe. The primary instead uses direct
coordinate formulas, scalar continuants and adjugate inversion, and exact
polynomial directional differences. Shared mathematical inputs and elementary
arithmetic lineage are disclosed; implementation independence does not mean
independent discovery of the preregistered equations.

All six frozen files will be published and read back before scientific
execution. The API commit metadata uses the already disclosed connected
A. M. Thorn GitHub identity; no history rewrite is used to alter metadata.
Only this one probe directory is changed by its branch. Run records report
observed events and hashes; independent proof claims are distinguished from
finite audit counts and from still-open physical interpretation.
