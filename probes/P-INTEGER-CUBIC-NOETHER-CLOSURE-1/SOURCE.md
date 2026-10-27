# Authority, mathematical provenance, and declared scope

Status: NON-CANONICAL  
Action layer: L1; all new choices NEW_DECLARED  
Probe: P-INTEGER-CUBIC-NOETHER-CLOSURE-1  
Owner: A. M. Thorn, session integer-cubic-noether-2026-10-19  
Ownership: https://github.com/mathorn1973/twist-j/issues/1653

## 1. Actual public authority

STATUS.md, POLICY.md and AGENTS.md were inspected before this scientific
work. Public Canon v103 is active. Public main and the peeled canon-v103
tag identify dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d. The declared
content commit is 01fb76f6b3b14a6a5ec05d0017ea922390ab6f66, an ancestor
of that base. The base tree is 52048d642e988830fe280928e6297c5a565a7324.
The successful main checks are in workflow run 39022927713; publication
checks for that same immutable authority were observed in runs 39022952253
and 39033710211. These authority checks do not establish a result for this
new probe.

The five actual normative byte strings were hash-checked before the new
claim and are independently checked by both new implementations:

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| canon/CANON.md | 1052518 | d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b |
| canon/CORE.md | 30714 | 9d5617a163bc7a4e1964d41861ff7f2f44009117c61debe08a4e1547c88be728 |
| canon/FRONTIER.md | 27382 | 8574c3d4b0cc70278dec7d64e2a51022718cc54497c64025d9e6021775fcbaf0 |
| canon/REGISTRY.tsv | 532811 | 5cd008147435bf1facfe93b2e05d9d7e41554d73f647ad09659aac002195890d |
| canon/CHANGELOG.md | 207770 | 79f6bd8f30b1f845ae918b7374049f4bf8e0a2270e89b4c5223469a93855f078 |

POLICY.md SHA-256:
da5d2cf5a021f4d069c471725e02b6d2c201e3acadd5ecfd4213a361184b7a5d.
AGENTS.md SHA-256:
7363b83ca6d822ec35e8465fe64c1aa8cd0007bf8b99ae599c265cc49fcee6e1.

The branch is based directly on that public main, not on a companion PR.
Before its ownership claim, exact issue and PR searches, local probes and
registry searches, and an explicit remote-head scan found no collision
with P-INTEGER-CUBIC-NOETHER-CLOSURE-1. The ownership issue was created
before the first commit of the probe. GitHub connector commits use the
authenticated A. M. Thorn account metadata, including its GitHub noreply
address; this was disclosed in the ownership issue. No history rewrite is
used to change that metadata.

## 2. Canonical mathematical inputs and their original limits

The selected inputs are in the immutable
[Public Canon v103](https://github.com/mathorn1973/twist-j/blob/dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d/canon/CANON.md):

1. DEF-K1-LINEAR-METRIC and K1-LINEAR-METRIC-COMPLETION supply the rational
   five-site operator L and the reduced TT comparison. Only the rational
   operator is used here; the new verifier does not import or numerically
   approximate a real algebraic first-derivative branch.
2. DEF-K1-HYBRID-FRW-CELL-METRIC supplies the selected finite graph
   incidence convention, the weighted edge form of L, the local bond
   energy and edge-current construction, and the constraint-coupled
   auxiliary-field pattern. The source-dependent additions used here
   are the explicit non-canonical choices of the companions below.

The hybrid canonical definition explicitly defines a restricted polynomial
model. It does not identify that polynomial as a controlled truncation of
a larger Einstein-Hilbert action, prove a nonlinear ADM gauge algebra, or
claim pointwise positivity of its local energy density. Its selected
zero-multiplier branch retains the earlier K1 physical history. None of
those limitations is removed by merely copying its lapse/shift notation.

The present probe uses five vertices and ten edges, not a new 3D spatial
simulation. It derives complete finite-horizon variations of the explicitly
declared reduced action. It does not claim a new variation with respect to
all ten components of an unrestricted spacetime metric.

## 3. Exact non-canonical companions inspected

### P-INTEGER-AUTONOMOUS-JOINT-ENERGY-1

[Draft PR #1650](https://github.com/mathorn1973/twist-j/pull/1650), ownership
[issue #1649](https://github.com/mathorn1973/twist-j/issues/1649):

- prospective pin: edfedd7e75c515d6d318032f526f381f66317da3;
- result head: a17fe5f2198f1693277b45bcf7c55458e8c2c381;
- exact stdout: 808 bytes, 29 LF, SHA-256
  ab1a15571a69961896471aa2212771fdf379afbc9a06837b1d4c3aa30ddad42e;
- independent review:
  https://github.com/mathorn1973/twist-j/pull/1650#issuecomment-6272491077.

It supplies the autonomous reciprocal TT/source law with constant coupling
g=1/324, source context A=a/4, and its interaction-inclusive bond energy.
The common equilibrium offset used in this probe is
E_star=(4342005/8683757)A^2. All identities here are rederived on arbitrary
off-shell arrays; they do not rely on a prepared trajectory or an
all-counter bound of this companion. In particular, the off-shell field
domain is not restricted to fixed spatial mean.

### P-INTEGER-NONLINEAR-CONSTRAINT-PROPAGATION-1

[Draft PR #1652](https://github.com/mathorn1973/twist-j/pull/1652), ownership
[issue #1651](https://github.com/mathorn1973/twist-j/issues/1651):

- prospective pin: 5e072359a029233d1c2b266c0c4bed2269752535;
- result head: 2e9f465cd3d4e23e7b187bb29e029eef07d20b61;
- exact stdout: 1160 bytes, 32 LF, SHA-256
  b195d97ff97f33cb9c42255a5db95c667c085888d9168b3d5859a4e3348c4630;
- primary verifier SHA-256:
  391990de4a64cffb4e9386acc8400270913a279356cdca87f6b48621df4b80b7;
- independent breaker SHA-256:
  4d5aae167226b92dfefb68e67f2386fd3372e34f80f97331a95be886c5f1cb61;
- independent analytical/code review:
  https://github.com/mathorn1973/twist-j/pull/1652#issuecomment-6274568353.

All six frozen files were checked byte-identical from pin to result head.
The primary and breaker were independently replayed, and the exact local
stdout and actual x86_64/aarch64 job logs were inspected. Its exact
local continuity and integer Hodge construction are retained as valid
mathematical inputs. This does not validate every public interpretation.

The actual frozen model uses mean-zero vertex tau/lambda and divergence-free
edge p, not the Phi/Pi fields described in its public summary. Its local
variation test does not include the neighboring shift currents that enter
the full global variation. An unrestricted derivative with respect to edge
p also differs from a derivative in the declared ker(B^T) domain. These
distinctions motivated the new prospective action audit. The old selected
physical histories remain those of #1650; this successor does not claim
that the old polynomial extension established nonlinear Einstein dynamics.

The independent review requests description corrections on #1652. No
frozen companion file is changed, resumed, renamed, or silently treated as
a new pin. No companion executable is imported by either new program.

## 4. What is newly declared and what is proved

| Item | Origin and exact interpretation |
| --- | --- |
| L, B, W, ell, sigma, A, local density and current | Selected comparison inputs, explicitly restated |
| Full horizon T>=5, fixed physical endpoints | NEW_DECLARED variational domain |
| Arbitrary rational off-shell h,chi | NEW_DECLARED test domain; no unit-sum or on-shell restriction |
| tau,lambda in e-perp; p in ker(B^T) | Explicit auxiliary domain, with complete coordinate bases |
| S_0 and S_int, S_epsilon=S_0+epsilon S_int | NEW_DECLARED formal deformation split of the selected finite action |
| epsilon order | Formal coupling order, not homogeneous field degree or a continuum expansion |
| delta_0 alpha,lambda,N | NEW_DECLARED auxiliary transformation, including homogeneous parameter part |
| delta_1 h,chi | NEW_DECLARED nearest-time field generator selected from the exact residual pairing |
| delta_0 S_0=0 and delta_0 S_int+delta_1 S_0=0 | Exact off-shell identities on the declared domain |
| epsilon^2 U remainder | Exact variation of the frozen truncated pair, generally nonzero |
| Pure auxiliary gauge values | First-order equation-proportional field redefinition with an explicit quadratic remainder |
| Commutator and its nonclosure witness | Failure of this specified off-shell generator family, even with a state-dependent parameter in that same family |
| Fixed-mean escape | A generator in this family need not preserve the earlier prepared fixed-mean field space |
| Shared integer denominator D and parameter denominator Qp | NEW_DECLARED finite-horizon arithmetic representation |
| Integer local density/current and Dnew=20 D Qp | Exact integer identities and tangent displacement encoding, not an autonomous physical update |
| Six configurations and 21 parameters each | NEW_DECLARED finite audit, not an exhaustive test of rational arrays |
| Analytic statements for arbitrary T/data | Established by the self-contained algebraic proofs, not inferred from the finite count |

The constraint propagation identity is an exact identity involving the
inherited field residuals. Substitution of the full multiplier-dependent
Euler equations changes the residuals and requires a further argument.
The present action has a proved first-order Noether cancellation; this
does not yet give an exact gauge symmetry of S_epsilon at epsilon=1.

The nonzero U and the displayed commutator are not a general obstruction
to additional higher-order action terms, auxiliary-dependent generator
corrections, a larger generator family, different stencils, or integer
gravity. No claim is made about a complete first-class Hamiltonian
constraint algebra, recovery of nonlinear ADM equations, a continuum
manifold, native-U realization, physical time, units, or experiment.

## 5. External primary context, not imported theorems

The proofs and programs are self-contained. The following primary works
were consulted to distinguish first-order action deformations, complete
gauge consistency, and discrete constraint questions. Their conclusions
are not used as a substitute for a TWIST-J-specific proof:

- G. Barnich and M. Henneaux, "Consistent couplings between fields with a
  gauge freedom and deformations of the master equation" (1993),
  https://arxiv.org/abs/hep-th/9304057, Section 4, equations (11)-(14)
  and (18)-(20). This distinguishes simultaneous deformation of an
  action and its generators, successive consistency orders, and
  equation-proportional terms induced by field redefinitions. We do not
  assert that a BRST master equation has been constructed for this probe.
- B. Dittrich, "How to construct diffeomorphism symmetry on the lattice"
  (2012), https://arxiv.org/abs/1201.3840. This supplies context for the
  separate question of retaining gauge symmetries after discretization.
- B. Dittrich and P. A. Hoehn, "Constraint analysis for variational
  discrete systems" (2013), https://arxiv.org/abs/1303.4294. This supplies
  context for distinguishing variational constraints and gauge generators
  in discrete systems; no general theorem is specialized here without
  checking its hypotheses.

No external dataset, learned parameter, floating-point estimate or symbolic
package output defines the new scientific fixtures. Both executables use
only the Python standard library and exact rational/integer arithmetic.
The breaker uses a separately authored dual-number action and sparse
generator matrices; the primary uses explicit incidence operations and
analytic global gradients. Both calculate the certificate payloads, and
neither reads EXPECTED.txt. Their first scientific execution is reserved
until after publication and readback of the complete prospective pin.
