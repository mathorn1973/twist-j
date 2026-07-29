# P-PHOTON-ROUGHENING-CERTIFICATE-1 predefinition ruling (NON-CANONICAL)

Status: `DRAFT / STOP-PREDEFINITION / ISSUE-RESERVED / SOURCE-CANDIDATE-IDENTIFIED / TYPE-UNRESOLVED / NO-PROBE / NO-FORMAL-RUN`

Date: 2026-07-29

Public definition lock:
[issue #201](https://github.com/mathorn1973/twist-j/issues/201).

This note audits the primary-source candidate and freezes the decisions still
required before the `PHOTON-ROUGHENING-CERTIFICATE` reconciliation child can
become a formal probe. It is not Canon, evidence, `PREREG.md`, a verifier, a
formal run, a result, or a status proposal. It changes no public claim and
authorizes no execution.

## 1. Authority, collision, and routing pin

```text
Canon:                    Public Canon v26
state:                    ACTIVE
authority:                mathorn1973/twist-j main
tag:                      canon-v26
activation/tag target:    48213275d0ace92d8f034166179a9fee4d53d908
content commit:           138eec5b22a823469e1fa651505815a3d5b36761
Canon SHA-256:            3a62711e30b1f3e9c4ade71533354fdf669266f60f4a57ade84e31a8f2878cfd
Canon bytes:              141941
parent owner:             PHOTON-WINDOW-PROOF [O]
scheduler:                PHOTON_CONTINUUM / ROOT / READY / FORMAL
reconciliation child:     PHOTON-ROUGHENING-CERTIFICATE [O]
reconciliation layer:     NOT_APPLICABLE
definition issue:         #201
definition branch:        notes/p-photon-roughening-certificate-1-predefinition
this file:                notes/canon/P-PHOTON-ROUGHENING-CERTIFICATE-1-PREDEFINITION.md
reserved future probe:    P-PHOTON-ROUGHENING-CERTIFICATE-1
reserved formal branch:   probe/P-PHOTON-ROUGHENING-CERTIFICATE-1
reserved formal path:     probes/P-PHOTON-ROUGHENING-CERTIFICATE-1/
formal pin/run/result:    ABSENT / NOT AUTHORIZED
```

`PHOTON-ROUGHENING-CERTIFICATE` appears only in the non-normative
reconciliation table `notes/genesis/recon/FRONTIER_SPLITS.tsv`. It is not a
Registry claim, dependency, gate, or evidence item. Issue #201 is a collision
lock, not permission to create the reserved formal branch or path.

The sibling lock `PHOTON-KAPPA-LEMMA` in issue #200 is disjoint and remains
out of scope here. Neither child can close or redefine the other.

The reconciliation layer is literally `NOT_APPLICABLE`. Repository policy
requires a future formal preregistration to freeze an action layer from L1
through L6. This mismatch is a pre-pin `STOP` requiring explicit public
disposition. It may not be repaired silently by relabeling this child L1.

## 2. Exact inherited inventory and firewalls

| Source | Inherited exact content | What it does not supply |
| --- | --- | --- |
| `PHOTON-WINDOW-PROOF [O]` | asks for an electric-face roughening certificate sufficient for a declared Froehlich-Spencer class import | a cited theorem, source edition, definition of roughening, hypothesis list, or typed import map |
| `PHOTON-WINDOW-COORDINATES [T]` | the exact five-center weight `w`, its Fourier/Kramers-Wannier partner, and the fixed photon point | a lattice action family, coupling map, configuration measure, boundary condition, thermodynamic limit, or roughening predicate |
| `PHOTON-UNIVERSAL-BIT [T]` | the normalized dual character weights and exact closure of higher classes | a Gibbs measure or a theorem-class membership certificate |
| `CENTER-SPLIT-SELECTION [D]` | a dictionary reading resting on the separately declared window threshold | a proof of that threshold or permission to feed the reading back as a premise |
| `DEF-ARCHITECTURE` | the architecture on which the photon dictionary is conditional | a derived infinite-volume lattice gauge theory |
| `FRONTIER_SPLITS.tsv` | non-normative reconciliation routing | evidence, status, definitions, or formal authorization |

The public exact one-face weight is

```text
w(k) = (1+zeta_5^k)(1+zeta_5^(-k)),

w = (4, phi^2, phi^(-2), phi^(-2), phi^2),
Fourier(w) = 5(2,1,0,0,1),
b = Fourier(w)/Fourier(w)(0) = (1,1/2,0,0,1/2).
```

These coordinates alone do not define a probability law on gauge-field
configurations or an observable in an infinite-volume state.

## 3. Primary-source audit

The identifiable primary-source candidate is:

```text
Jurg Frohlich and Thomas Spencer,
"Massless phases and symmetry restoration in abelian gauge theories
and spin systems,"
Communications in Mathematical Physics 83 (1982), 411-454,
DOI: 10.1007/BF01213610.

Author archive version:
IHES prepublication P/81/40 (1981), 85 printed pages.
```

Stable primary locators:

- [journal DOI](https://doi.org/10.1007/BF01213610);
- [Springer journal record](https://link.springer.com/article/10.1007/BF01213610);
- [IHES archive record](https://omeka.ihes.fr/document/P_81_40.pdf).

No copy of the PDF is added to this repository. If a future probe imports
third-party bytes, license review, a source manifest, and a pinned hash are
separate pre-run requirements.

### 3.1 What the source actually proves

The journal abstract and the preprint both state the finite-group result for
four-dimensional `Z_N` models with `N` large. In section 3 of the IHES
preprint:

```text
beta > beta_crit(U(1)),
N > N(beta),
N(beta) -> infinity as beta -> infinity,
```

imply perimeter lower bounds for the Wilson and disorder loops. The argument
then proves existence of a finite `N_c` above which an interval of
intermediate QED phases exists.

The next printed page says explicitly:

```text
"It is believed that N_c = 5."
```

That sentence is not a theorem that `N_c=5`, nor a theorem for every
`N>=5`. In section 3.6 the proof obtains activity control only after a
condition of the form

```text
N > c_1 beta + c_7
```

for finite but unspecified constants, and the final lower bound remains
quantified by `N>N(beta)`.

The named four-dimensional actions are Wilson and Villain actions. The
source also discusses extension of its methods to a broader class of
actions, but it does not identify the TWIST-J fixed face weight, provide an
explicit `N=5` constant package for it, or state a theorem whose sole
hypothesis is an "electric face roughening certificate."

### 3.2 The word "roughening" is not yet a typed import

In the source, "roughening" appears in the introduction when discussing the
presumed roughening transition of a pure `SU(2)` theory as an obstruction.
Section 3 proves perimeter bounds and restoration of local `U(1)` invariance
for sufficiently large `N`; it does not publish a standalone `Z_N`
"electric face roughening criterion" with a finite checklist that can simply
be evaluated at `N=5`.

Therefore the Canon phrase "electric face roughening certificate sufficient
for the declared Froehlich-Spencer class import" does not yet name a source
predicate. Its observable, normalization, theorem chain, and consumed
conclusion must be frozen before a certificate can pass or fail.

## 4. Exact one-face action audit

For the Wilson action, the face factor is of the form

```text
phi_beta(theta) = exp(beta cos(theta)).
```

For positive finite `beta`, its cyclic Fourier coefficients are strictly
positive: the Bessel expansion gives each coefficient as a positive sum of
`I_(m+rN)(beta)`. The Villain heat-kernel coefficients are also strictly
positive for finite coupling.

The TWIST-J Fourier vector has exact zeros in character classes 2 and 3:

```text
Fourier(w) = 5(2,1,0,0,1).
```

Consequently the fixed TWIST-J face factor is not exactly either named
finite-coupling Wilson or Villain face factor. This is an exact equality
obstruction at the one-face level. It does not prove exclusion from every
broader action class mentioned by Frohlich and Spencer.

A future positive import must instead provide one of:

1. an exact theorem whose stated action class directly contains `w`;
2. a proved equality, implication, or comparison theorem from `w` to a named
   theorem action without changing the consumed observable;
3. a complete derivation of the needed Frohlich-Spencer estimates at this
   fixed `N=5` weight; or
4. another primary theorem explicitly covering the same carrier, action,
   regime, and conclusion.

A local convexity, Hessian, Fourier-support, or finite-face check is not by
itself an infinite-volume import.

## 5. Source-import object that must be frozen

A valid source package must publish one exact tuple

```text
S_FS = (
    authors, title, venue, year, volume, pages, DOI,
    edition, stable_locator, source_hash_if_imported, license,
    theorem_chain, theorem_pages,
    dimension, lattice, gauge_group, action,
    coupling_parameters, parameter_regime,
    finite_volume_measure, boundary_conditions, thermodynamic_limit,
    locality, positivity, regularity, summability,
    duality_or_comparison_assumptions,
    roughening_definition, observable,
    exact_conclusion_consumed
).
```

| Item | Audited source candidate | Required formal freeze | State |
| --- | --- | --- | --- |
| bibliographic identity | Frohlich-Spencer, CMP 83 (1982), 411-454, DOI above | owner confirmation that this is the declared import | `CANDIDATE-IDENTIFIED` |
| edition | journal record and IHES P/81/40 preprint | one cited edition and stable page/theorem mapping | `UNRESOLVED` |
| theorem chain | preprint section 3, especially printed pp. 53-69 | exact numbered identities/lemmas and every dependency | `UNRESOLVED` |
| dimension/lattice | four-dimensional cubic lattice | exact equality with the TWIST-J probe carrier | `UNRESOLVED` |
| group regime | `Z_N` for sufficiently large `N` | an exact route valid at `N=5` | `MISMATCH` |
| action | Wilson or Villain, with methods discussed more broadly | exact membership or comparison for the fixed TWIST-J weight | `NO-EQUALITY / BROADER-CLASS UNRESOLVED` |
| coupling | `beta`, interpolation parameter, and a theorem regime involving `beta_crit(U(1))` and `N(beta)` | exact map from the fixed photon point to every source parameter | `UNRESOLVED` |
| state | finite-volume measures and an infinite-volume limit | complete TWIST-J measure, boundary, and limit map | `UNRESOLVED` |
| roughening | no standalone criterion matching the Canon phrase was located | exact source definition and predicate | `UNRESOLVED` |
| conclusion | perimeter bounds and intermediate QED/local-`U(1)` restoration for large `N` | the exact conclusion consumed by `PHOTON-WINDOW-PROOF` and no stronger one | `UNRESOLVED` |
| source bytes | no repository copy | DOI-only citation, or separately licensed and hashed import | `DOI-ONLY` |

The current `data/EXTERNAL_SOURCES.tsv` schema serves experimental external
observables and must not be repurposed by inventing theorem metadata. A
source record, if later required, needs an explicitly approved schema.

## 6. Typed bridge that must be proved

The future certificate must fill every row with an exact proof:

| Source hypothesis or type | TWIST-J object | Required equality, implication, or domination | Proof location | State |
| --- | --- | --- | --- | --- |
| 4D infinite cubic lattice | photon cubical carrier | carrier equality, exhaustion, and boundary compatibility | absent | `UNRESOLVED` |
| `Z_N` gauge variables | declared `Z_5` edge variable | total configuration-space and gauge-action map | absent | `UNRESOLVED` |
| Wilson/Villain or accepted broader action | exact `w` and `Fourier(w)` | action equality or theorem-preserving comparison | absent | `UNRESOLVED` |
| source coupling parameters | fixed photon point | exact parameter map and proof it lies in the theorem regime | absent | `UNRESOLVED` |
| finite-volume Gibbs measure | TWIST-J configuration law | normalized measure equality or controlled domination | absent | `UNRESOLVED` |
| boundary conditions and limit | proposed photon limit | exact exhaustion and thermodynamic-limit theorem | absent | `UNRESOLVED` |
| source regularity/activity hypotheses | exact face and defect data | every quantitative hypothesis with constants | absent | `UNRESOLVED` |
| source observable | proposed electric roughening observable | equality of observables and normalization | absent | `UNRESOLVED` |
| `N>N(beta)` or successor condition | `N=5` | exact inequality or a theorem explicitly valid at 5 | absent | `UNRESOLVED` |
| perimeter/QED conclusion | parent photon conclusion | exact logical implication bounded to source scope | absent | `UNRESOLVED` |

Equal dimensions, the same abstract finite group, or compatible-looking
single-face numbers do not fill this table.

## 7. Current source ruling and false shortcuts

The present primary-source audit is `STOP`:

- the likely source is identifiable;
- the source does not prove `N_c=5`;
- the TWIST-J face factor is not equal to either named finite-coupling action;
- no exact broader-class membership theorem is pinned; and
- the Canon's "roughening certificate" is not yet a source-defined
  predicate.

This is not yet `CERTIFIED-FAILURE`. A later theorem, comparison, or direct
estimate might close the typed gap. Conversely, the phrase "it is believed"
cannot be promoted into a certificate.

The following are forbidden shortcuts:

1. replacing "sufficiently large `N`" by `N>=5`;
2. treating a belief sentence, numerical phase diagram, or Monte Carlo
   threshold as a theorem;
3. using Kramers-Wannier duality alone as a masslessness or roughening proof;
4. calling a local face inequality a thermodynamic-limit certificate;
5. claiming action-class membership without the exact class definition and
   every quantitative constant;
6. selecting a coupling after reading a desired phase conclusion;
7. using `CENTER-SPLIT-SELECTION [D]` as evidence for its own declared input;
8. importing an uncited theorem by the label "Frohlich-Spencer class"; or
9. concluding photon masslessness from perimeter decay without the exact
   theorem implication that authorizes that step.

## 8. Future outcomes

The formal lane must preserve exactly these issue-locked routes:

```text
CERTIFICATE-PASS
    A pinned primary theorem and complete typed bridge prove every source
    hypothesis for the fixed TWIST-J carrier, action, N=5 parameter regime,
    measure, observable, and consumed conclusion.

CERTIFIED-FAILURE
    An exact complete theorem proves that the frozen TWIST-J object fails the
    declared source criterion or cannot satisfy any admitted bridge.

STOP
    The source, edition, theorem chain, hypothesis, action class, parameter
    map, measure, observable, limit, bridge, completeness proof, source
    license, certificate, checker, layer disposition, or exact reproduction
    is missing or ambiguous.
```

Failure of one unfrozen action map is `STOP`, not `CERTIFIED-FAILURE`.
Negative closure requires a complete frozen admissible bridge class.

## 9. Future preregistration skeleton, still forbidden

Only after public review may a later immutable preregistration fill:

```text
EQUATION:    exact source criterion and certificate equations
CODE:        accepted exact checker, if computation is used
CARRIER:     complete TWIST-J and source carriers with equality
SYSTEMATICS: theorem dependencies, action class, coupling, measure,
             boundary, limit, observable, comparison, and source controls
THRESHOLD:   exact CERTIFICATE-PASS / CERTIFIED-FAILURE / STOP predicates
LAYER:       currently NOT_APPLICABLE in the reconciliation split
```

If formal review requires an L1-L6 assignment, `LAYER=NOT_APPLICABLE` is a
pre-pin `STOP` until the public routing is explicitly repaired. Any newly
discovered inter-layer map or dependency requires separate authorization.

## 10. Pre-pin acceptance checklist

The formal branch and path remain forbidden until:

1. this definition note is reviewed, merged, and read back publicly;
2. the owner confirms the exact primary source and edition;
3. every field of `S_FS` is exact and no `UNRESOLVED` slot remains;
4. the theorem chain and every quantitative hypothesis are pinned by stable
   page or identity references;
5. the `N=5` route is a proved theorem, not the source's belief sentence;
6. the fixed TWIST-J action, coupling, measure, boundary, limit, and
   observable have a complete typed bridge;
7. the consumed conclusion is stated without strengthening;
8. all three outcomes remain reachable and their falsifiers are exact;
9. source license and manifest requirements receive explicit disposition;
10. the action-layer mismatch receives explicit public disposition;
11. issue, branch, probe, path, and short-ID collisions are rechecked;
12. an accepted verifier, if any, is committed and pushed with `PREREG.md`
    before the first formal gate execution; and
13. remote hashes, byte counts, and LF-normalized readback are confirmed
    before any run.

## 11. Debt firewall

This note does not define roughening, prove or disprove broader
Frohlich-Spencer action-class membership, establish a `Z_5` Coulomb phase,
promote perimeter decay to photon masslessness, strengthen
`CENTER-SPLIT-SELECTION`, add third-party source bytes, edit the Canon, or
authorize a probe. It records the exact primary-source mismatch and makes the
remaining import test public and falsifiable.
