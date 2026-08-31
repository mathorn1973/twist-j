# P-PHOTON-Z5-STAR-QUADRATURE-1 preregistration

Status: FORMAL PREREGISTRATION / ANALYTICALLY EXPOSED / EXACT CLASSIFICATION / L4 ONLY

Owner: A. M. Thorn
Public claim: [issue #723](https://github.com/mathorn1973/twist-j/issues/723)
Branch: `probe/P-PHOTON-Z5-STAR-QUADRATURE-1`
Directory: `probes/P-PHOTON-Z5-STAR-QUADRATURE-1/`
Date: 2026-08-31

This freezes the complete finite class, accepted code, comparison thresholds
and all dispositions before the first formal execution. The generic
fifth-harmonic bound and a positive HALF saturation example were proved
before this pin. An unverified manual inspection of counts (2,0,2,0,2)
also suggested a possible HALF violation. Those exposures are disclosed:
this is a complete exact classification audit, not a blind prediction.
No census code, including this verifier, has been executed or imported.
No sharp global value or complete extremizer set is assumed.

## 1. Authority and scope firewall

```text
STATE:           ACTIVE
CANON:           Public Canon v72
MAIN AT CHECK:   9f88c4c93aab3139ee0a2e007f0e60891957aa21
TAG:             canon-v72
TAG TARGET:      0bc7a623627c4453cc94515ae92880ec75ae7d94
CONTENT_COMMIT:  aac8a3a4aff027beb2b08edbde1ae8e59224914c
CANON_SHA256:    39ca6e5c49d3ec2b78464045312af75618c4601f87dfa178dfd689d8a4942c70
CANON_BYTES:     374406
```

The tag/content ancestry, exact Canon bytes and passing main checks were
verified. Later unrelated public probes do not change this input.
Remote heads, open issues and PRs, all-issue exact-ID search, public contents
and lock paths were checked before claiming this fresh identity. No
predecessor is resumed, renamed, reinterpreted or amended.

The motivation is the conditional model in the merged
[Born-current note](../../notes/canon/PHOTON-BORN-CURRENT-OBSERVABLE-LEMMA.md)
and [screening criterion](../../notes/canon/PHOTON-DEFECT-SCREENING-CRITERION.md).
This probe claims ONLY the finite algebraic factor/quadrature classification
below. Its counts are not physical degrees of freedom or sampled events.

No action, source, Gibbs state, physical carrier or reading is adopted.
No infinite-volume tail, covariance screening, phase, cone, propagator,
polarization, apparatus or SI claim is tested. In particular
GATE-L4-L6-PHOTON-MASSLESS-PHASE remains open. Both photon successor roots
stay O; the old KAPPA and WINDOW claims remain terminal F. There is no Canon
fold, registry/evidence/gate change, tag, release or workflow change.

## 2. Exact finite class and coefficient conventions

Fix zeta=exp(2 pi i/5), in its principal embedding. Let

```text
k=(k0,k1,k2,k3,k4),     kb nonnegative integers,
r=sum_b kb,            0<=r<=6,
P_k(z)=product_(b=0)^4 (1+zeta^b z)^kb=sum_(a=0)^r p_a z^a.
```

Pad p_a by zero through degree six. Define the Laurent coefficients of
|P_k(exp(i theta))|^2 by c_m=sum_a p_(a+m) conjugate(p_a). In particular,

```text
C0=sum_(a=0)^6 |p_a|^2,
c5=p5 conjugate(p0)+p6 conjugate(p1),
F=c5+conjugate(c5),
D=(1/5)sum_(q=0)^4 |P_k(zeta^q)|^2,
theta(k)=|F|/D.
```

Every C0,F,D is real in Q(sqrt(5)); C0 and D are strictly positive.
The factor normalization Q(theta)=1+cos(theta)=|1+exp(i theta)|^2/2
would multiply C0,F,D by the same 2^(-r), and hence does not change theta.

The class consists of sum_(r=0)^6 binomial(r+4,4)=binomial(11,5)=462
distinct count vectors. Equal ordered factor lists are identified only
by commutativity of multiplication. No count vector is removed by
symmetry or by observed output. Phase shift and reflection are checks,
not reductions of the enumeration.

The complete output is the exact maximum theta(k) in each degree and
globally, every extremizer, its C0,F,D, the lexicographically first
witness and extremizer multiplicity, and every counterexample to the
two thresholds in section 4. Multiplicity means count-vector multiplicity,
not the number of ordered factor lists or physical configurations.

## 3. Algebraic completeness and independent checks

In Z[zeta], use the basis (1,zeta,zeta^2,zeta^3) and the relation
zeta^4=-(1+zeta+zeta^2+zeta^3). Integer polynomial multiplication followed
by descending reduction gives exact ring arithmetic. Conjugation sends
zeta^b to zeta^(-b). A real basis tuple is necessarily (a,0,c,c), whose
principal real value is

```text
a+c(zeta^2+zeta^3)=(a-c/2)-(c/2)sqrt(5).
```

Comparisons of u+v sqrt(5) use exact rational signs and, when u and v
have opposite signs, the sign of u^2-5v^2. Equality in that last
comparison is impossible for nonzero rational u,v. Division uses the
nonzero rational norm u^2-5v^2. No floating-point embedding is used.

The fifth-root average kills each Laurent mode not divisible by five.
Since the Laurent degree is at most six, this proves D=C0+F. The verifier
also computes D independently by evaluating P at all five roots. Strict
positivity follows because p0=1 and because 1+zeta^a is nonzero for every
integer a; in fact every summand in the discrete average is positive.

For every complex polynomial of degree at most six,

```text
2|c5|
 <= |p0|^2+|p5|^2+|p1|^2+|p6|^2
 <= C0.
```

The first step is the triangle inequality and 2|ab|<=|a|^2+|b|^2.
Consequently -C0<=F<=C0. These inequalities do NOT imply
|F|<=D/2: negative F can reduce D. The restricted five-phase class is
what this complete census classifies.

The known counts (2,1,1,1,1) give P=(1+z)(1+z^5), hence
C0=4,F=4,D=8 and theta=1/2. This proves the global maximum is at least
1/2 before execution. It does not prove that 1/2 is an upper bound.

Uniformly shifting the five phase indices multiplies p_a by zeta^(sa);
it leaves C0,c5,F,D unchanged because zeta^(5s)=1. Reflection conjugates
p_a and leaves real C0,F,D unchanged. The code checks both transformations
against the fully independently enumerated records.

Exhaustiveness follows by recursive composition generation with nonnegative
first coordinate from zero through the remaining total. Induction gives
each five-tuple with fixed total exactly once. The binomial count and
uniqueness checks audit this construction. Exact pair comparison totally
orders the finite real ratios, so retaining all ties gives the complete
extremizer set, not a search sample.

## 4. Frozen six fields

### Field 1: equation

Exactly the class, equalities and finite maximum problem in sections 2-3.
Classify BOTH of the following fixed predicates:

```text
HALF:         theta(k)<=1/2 for every admitted k.
STRICT_UNIT:  theta(k)<1   for every admitted k.
```

Equality passes HALF and fails STRICT_UNIT. Neither threshold moves.
For positive D=C0+F, HALF is equivalent to F>=-C0/3 together with the
already proved F<=C0. The sharp maximum is reported regardless of either
predicate's truth.

### Field 2: accepted code

```text
file:         probes/P-PHOTON-Z5-STAR-QUADRATURE-1/verify.py
sha256:       87fcc66932750cd325c8ab4f7c28e6832780e7ebd8b3bd19352b255391ce2044
bytes:        9869
command:      python3 probes/P-PHOTON-Z5-STAR-QUADRATURE-1/verify.py
dependencies: Python standard library only
arithmetic:   integers and fractions.Fraction
inputs:       none
```

The entire draft was statically and independently reviewed before this
freeze. The accepted version changes only the draft's introductory label
and adds an explicit extra-argument rejection guard; mathematical code
is unchanged. Neither draft nor accepted version was run or imported.

Frozen internal checks: cyclotomic order and sum, root norms and
conjugation, principal-embedding sign controls, degree and global counts,
tuple uniqueness/domain, independent discrete quadrature and divisibility,
real-subfield membership, positive C0 and D, generic bounds +/-F<=C0,
ratio nonnegativity, phase-shift and reflection invariance, and the
declared positive HALF saturation example.

Output is buffered until internal checks pass and ASCII is verified.
It includes all degree/global extrema and all threshold counterexamples.
A successful classification exits zero with empty stderr, including when
FAIL_HALF or FAIL_UNIT appears. An internal exception writes only the fixed
INTERNAL_ERROR line to stdout and exits 2. Extra arguments write fixed STOP
stderr and exit 2 before classification. No files, network, environment,
randomness, floating point or external datasets are consumed by the code.

### Field 3: carrier and data

The entire 462-element class above, exact Q(sqrt(5)) values in the principal
embedding, and lexicographic count-vector order. The bound r<=6 is fixed
before execution; it is the maximum number of incident plaquettes of an
edge in a free cubical subcomplex of Z^4. Degrees zero through six are all
included, even if a particular box realizes only some boundary degrees.

Orientation signs of an actual edge factor can be absorbed into the phase
index because cosine is even. Six independent opposite edges of an
interior star can realize every six-offset phase list. The finite result
itself needs only the explicitly stated polynomial class.

### Field 4: systematics and controls

Freeze continuous C0 versus discrete D; fifth versus residue-zero harmonic;
the two terms contributing to c5 at degree six; negative F and denominator
cancellation; all count vectors including phase repeats; every exact tie;
principal embedding; and strict versus non-strict comparison.

The independent quadrature cannot be replaced by a formula using C0 or c5.
Symmetry must not silently discard cases. A complex modulus of c5 must
not replace |c5+conjugate(c5)| in the unsigned ratio. No measured or rounded
value may determine a classification.

Prior analytic exposure is disclosed above. An exact counterexample to HALF
is retained even if STRICT_UNIT passes. If the sharp local constant is at
least one, that only blocks this pointwise contraction route: it does not
mean any probability is greater than one or that the model is massive.

### Field 5: failure threshold and dispositions

```text
CLASSIFIED / PASS_HALF
  All internal certificates complete; no theta(k)>1/2 exists.

CLASSIFIED / FAIL_HALF
  All internal certificates complete; every theta(k)>1/2 is printed.
  HALF is refuted at the frozen finite scope; the threshold is unchanged.

CLASSIFIED / PASS_UNIT
  All internal certificates complete; no theta(k)>=1 exists.

CLASSIFIED / FAIL_UNIT
  All internal certificates complete; every theta(k)>=1 is printed.
  STRICT_UNIT is refuted at the frozen finite scope.

STOP
  Missing authority, ownership, accepted code/pin, exact output, clean Linux
  route, architecture agreement or security review; or an internal audit/
  execution error. Such failure is not a scientific counterexample.
```

The two classification pairs are simultaneous outputs, not alternative
post hoc choices of the favorable test. The complete finite classification
is proposed at C after required reproduction; a stronger independently
written theorem may later justify T, but this pin creates no promotion.

If a pin never completes a gate, preserve its unchanged files and close
ABANDONED under policy. Never resume, rename, amend, rebase, squash or
force-push a pinned probe. A completed scientific failure is a result,
not abandonment.

### Field 6: action layer

```text
L4 ONLY: exact finite plaquette-factor data and scalar quadrature.
```

The finite character averages are algebraic definitions, not adoption of
a physical L6 probability law. No cross-layer gate is executed by this
verifier. Any subsequent application to the explicitly selected conditional
Born/current model is a separate mathematical proof, not an enlargement
of this finite probe's status or a physical reading selection.

## 5. Formal execution and readback

The Linux/aarch64 connector route has been verified available. The accepted
files travel through public Git, never as an unattached script.

1. Commit and push exactly PREREG.md and verify.py, with one parent.
2. Record the public pin, both blobs, hashes and byte counts; read both files
   back at that commit before any execution.
3. Fetch that exact pin into an isolated clean Linux checkout, verify hashes,
   authority ancestry and the clean state.
4. Run the frozen command from the repository root with LC_ALL=C LANG=C
   PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC. Capture raw stdout,
   stderr and exit status separately.
5. Only after completion, add actual stdout as EXPECTED.txt and neutral
   RUN.md/RESULT.md, without altering either pinned file.
6. Require exact-head x86_64 and aarch64 PR checks, aggregate check, manual
   review and byte-identical reproduction. Merge without squash/rebase;
   verify public files and main checks afterward.

EXPECTED is generated by the actual post-pin run, not authored from a
predicted result. Source bytes, private infrastructure details and scratch
files are excluded. Canon publication remains a separate operation.
