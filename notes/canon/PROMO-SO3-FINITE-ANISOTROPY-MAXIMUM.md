# PROMO-SO3-FINITE-ANISOTROPY-MAXIMUM

Status: **NON-CANONICAL / NO AUTHORITY / PROMOTION PACKAGE ONLY.**

Basis:

```text
public authority:       Public Canon v67
basis main:             2282bcd3289ca31f84bdc0186585cb4fc1525c76
source claim issue:     #615
source probe PR:        #617
source probe:           P-SO3-FINITE-ANISOTROPY-DEPTH-1
source claim:           SO3-FINITE-ANISOTROPY-MAXIMUM
source result:          candidate-T / L1 / CONFIRMED
formal pin:             4448ad11a8026740962d06585c06b8e7d11ad6b2
verifier sha256:        f9cb216c006aa98a83ff99619955d8221d53b00484eabbffafbcba651e39cd55
expected/stdout sha256: c5f29046913ca024427be3fc1213fc15af672ca2e51917a260788e792606ccbc
bundle manifest sha256: 0fd88c1b604fd351ad147e8b0fdecc553e6e27c96f7c861f28fc10b0eb527a15
source merge:           2282bcd3289ca31f84bdc0186585cb4fc1525c76
```

The source pull request passed the required GitHub-hosted Python 3.12 x86_64
and native aarch64 jobs with byte-identical stdout and aggregate `check` PASS.
The universal theorem is proof-first; the machine computation is an exact
polyhedral audit.

This package creates no claim, status, Canon version, Registry row, Frontier
row, tag or release. It freezes the exact content of a later sealed fold so
that the fold cannot silently widen from finite-rotation representation theory
to Lorentz or physical selection.

## 1. Frozen public scope

The exact Registry scope string is:

```text
at L1 for every finite subgroup G <= SO(3), with a(G)=min{ell>=1:H_ell(R^3)^G != 0}, the complete finite-rotation classification gives a(C_n)=1 for n>=1, a(D_n)=2 for n>=2, a(A_4)=3, a(S_4)=4 and a(A_5)=6, hence a(G)<=6 with equality iff G is conjugate to the rotational icosahedral group A_5; in the winning 3D A_5 representation the two order-five rotation classes have traces phi and 1-phi, whose difference sqrt5 generates character field Q(sqrt5); finite-rotation representation theory only, with no selection of J, the physical prime p=5, a boost or rapidity, Lorentz density, decoder, measure, dynamics or L2-L6 lift
```

Its SHA-256 is

```text
e5641ef4a454429e4756d652b9215dea4e80560613607050626eb9fa892ef75b
```

The exact falsifier string is:

```text
fires if some finite G <= SO(3) has a(G)>6, if some finite G not conjugate to A_5 has a(G)=6, if A_5 has a nonzero invariant harmonic in degree 1 through 5, if H_6(R^3)^A5=0, or if the two order-five traces fail to generate Q(sqrt5); any physical selection, boost-density or higher-layer reading is outside scope; an integrity mismatch without exact mathematical negation is STOP
```

## 2. Frozen Canon insertion

Insert this block in `canon/CANON.md` under
`## 10. Relativity as counting`, before the existing Lorentz-density context.

```markdown
### SO3-FINITE-ANISOTROPY-MAXIMUM [T]

For a finite subgroup `G <= SO(3)`, let `H_l(R^3)` be the real homogeneous
harmonic polynomials of degree `l` and define

```text
a(G) = min { l >= 1 : H_l(R^3)^G != 0 }.
```

The complete finite-rotation classification has five types, with two infinite
families, and the exact harmonic depths are

```text
a(C_n) = 1,  n >= 1,
a(D_n) = 2,  n >= 2,
a(A_4) = 3,
a(S_4) = 4,
a(A_5) = 6.
```

Hence `a(G) <= 6` for every finite `G <= SO(3)`, with equality if and only if
`G` is conjugate to the rotational icosahedral group `A_5`. For `A_5`, exact
class-angle character averaging gives no invariant harmonic in degrees `1`
through `5` and multiplicity one in degree `6`. Independently, the exact
Molien series is

```text
(1 + t^15) / ((1 - t^2)(1 - t^6)(1 - t^10)).
```

The two order-five rotation classes in the winning three-dimensional `A_5`
representation have traces `phi` and `1 - phi`; their difference is `sqrt5`,
so the character field of the equality branch is `Q(sqrt5)`.

The universal quantifier is proved from the complete finite-subgroup
classification of `SO(3)` plus symbolic cyclic and rotational-dihedral
arguments. `P-SO3-FINITE-ANISOTROPY-DEPTH-1` independently audits the three
polyhedral cases by exact character and Molien arithmetic over `Q(sqrt5)`.

Scope: L1 finite-rotation representation theory only. This theorem does not
select `J`, the physical prime `p = 5`, a boost or rapidity, Lorentz density, a
decoder, a measure, dynamics, or any L2-L6 lift. It says that `A_5` uniquely
postpones the first invariant harmonic scalar to degree six; it does not
eliminate anisotropy.
```

Immediately after that block, retain the existing Lorentz-density paragraph
with no promotion of its interpretation. The two facts must remain logically
separate:

```text
SO3-FINITE-ANISOTROPY-MAXIMUM   selects the finite rotation type by harmonic depth.
Lorentz density construction    protects the chosen construction; it does not classify boosts.
```

No sentence of the form `Lorentz invariance forces A_5`, `density selects the
golden boost`, or `another discrete universe must resonate` is permitted by
this fold.

## 3. Exact `canon/REGISTRY.tsv` row

Append one row with the exact seven-column public schema:

```tsv
SO3-FINITE-ANISOTROPY-MAXIMUM	T	at L1 for every finite subgroup G <= SO(3), with a(G)=min{ell>=1:H_ell(R^3)^G != 0}, the complete finite-rotation classification gives a(C_n)=1 for n>=1, a(D_n)=2 for n>=2, a(A_4)=3, a(S_4)=4 and a(A_5)=6, hence a(G)<=6 with equality iff G is conjugate to the rotational icosahedral group A_5; in the winning 3D A_5 representation the two order-five rotation classes have traces phi and 1-phi, whose difference sqrt5 generates character field Q(sqrt5); finite-rotation representation theory only, with no selection of J, the physical prime p=5, a boost or rapidity, Lorentz density, decoder, measure, dynamics or L2-L6 lift	10. Relativity as counting	probes/P-SO3-FINITE-ANISOTROPY-DEPTH-1	fires if some finite G <= SO(3) has a(G)>6, if some finite G not conjugate to A_5 has a(G)=6, if A_5 has a nonzero invariant harmonic in degree 1 through 5, if H_6(R^3)^A5=0, or if the two order-five traces fail to generate Q(sqrt5); any physical selection, boost-density or higher-layer reading is outside scope; an integrity mismatch without exact mathematical negation is STOP
```

## 4. Exact `canon/NORMATIVE.tsv` row

```tsv
SO3-FINITE-ANISOTROPY-MAXIMUM	THEOREM	SO3-FINITE-ANISOTROPY-MAXIMUM	T	L1		canon/CANON.md::10. Relativity as counting
```

No dependency edge and no gate row is added. The theorem is self-contained at
L1 and the source proof owns the universal classification.

## 5. Exact `canon/EVIDENCE.tsv` row

```tsv
SO3-FINITE-ANISOTROPY-MAXIMUM	EV-SO3-FINITE-ANISOTROPY-MAXIMUM	PUBLIC_PROBE	probes/P-SO3-FINITE-ANISOTROPY-DEPTH-1	0fd88c1b604fd351ad147e8b0fdecc553e6e27c96f7c861f28fc10b0eb527a15	bundle-manifest-sha256-v1	two-architecture
```

The evidence hash is the canonical bundle-manifest SHA-256 of the merged probe
as consumed by the public verifier tooling. It is not a hash of one selected
file.

## 6. Exact `canon/HISTORY.tsv` declaration

```tsv
CANON68-DECLARE-SO3-FINITE-ANISOTROPY-MAXIMUM	1	2026-08-28	canon-v68-candidate	SO3-FINITE-ANISOTROPY-MAXIMUM	DECLARE	-	T	e5641ef4a454429e4756d652b9215dea4e80560613607050626eb9fa892ef75b	EV-SO3-FINITE-ANISOTROPY-MAXIMUM	probes/P-SO3-FINITE-ANISOTROPY-DEPTH-1	0fd88c1b604fd351ad147e8b0fdecc553e6e27c96f7c861f28fc10b0eb527a15	Public Canon v68 registers the complete finite-rotation harmonic-depth classification at L1: A_5 uniquely postpones the first invariant harmonic scalar to degree six and its order-five trace field is Q(sqrt5); no boost, Lorentz-density, J-selection, physical p=5, decoder, measure, dynamics or higher-layer bridge is promoted.
```

## 7. Changelog delta

Prepend one Public Canon v68 entry with this scientific content only:

```text
Public Canon v68 adds one proof-first L1 theorem,
SO3-FINITE-ANISOTROPY-MAXIMUM [T]. The complete finite-rotation
classification gives harmonic depths 1,2,3,4,6 for C_n,D_n,A_4,S_4,A_5,
so A_5 is the unique finite rotation type attaining depth six. Its order-five
trace field is Q(sqrt5). The source probe passed the required x86_64 and
aarch64 replay with byte-identical stdout. The fold consumes no Lorentz-density
paper and makes no boost, J, physical p=5, decoder, measure, dynamics or
higher-layer selection claim.
```

No older changelog text is rewritten.

## 8. Expected ledger delta

Relative to the Public Canon v67 content currently carried on basis main:

```text
claims:                   336 -> 337
T:                        213 -> 214
D:                         43 -> 43
C:                         33 -> 33
H:                          2 -> 2
O:                         28 -> 28
F:                         17 -> 17
live H/O:                  30 -> 30
normative items:          382 -> 383
dependency edges:         616 -> 616
evidence rows:            336 -> 337
history rows:             859 -> 860
gates:                     11 -> 11
minimal reproductions:     23 -> 23
evidence none:             45 -> 45
one-architecture:           9 -> 9
recorded-audit:             31 -> 31
two-architecture:         251 -> 252
```

`canon/FRONTIER.md`, `canon/FRONTIER_PROGRAMS.tsv`, `canon/DEPENDENCIES.tsv`,
`canon/GATES.tsv`, and `canon/CORE_SELECTION.tsv` receive no scientific delta.

## 9. CORE and release identity

A v68 release must update the release identity in `canon/CORE.md` from Public
Canon v67 to Public Canon v68. This theorem is not added to the generated core
claim selection because it is not a stable orientation claim. The existing
statement that TWIST-J does not derive or justify the primitive axiom remains
unchanged.

`STATUS.md`, `README.md`, and `CITATION.cff` are release-form files. They must
not be mixed into a partial content edit. The release follows the repository's
current activation procedure and declares the exact content commit, Canon
SHA-256 and byte count only after the content tree is frozen and checked.

An empty `release/canon-v68` ref currently points at the basis commit only. It
carries no content and has no authority. A future sealed fold must either use
that exact clean ref or replace it only by a policy-compliant fast-forward from
the same basis.

## 10. SHA256SUMS and checks

No prospective normative hash is guessed in this package. After the complete
content tree is assembled, regenerate `canon/SHA256SUMS` from the exact bytes
of the five normative files and require the repository checkers to pass.

The minimum release check set is the current repository procedure, including
policy, Canon, ledger, gate-contract, status-label, preregistration and full
changed-Canon escalation. The pull-request workflow must rerun all public
probes and all minimal reproductions on both required architectures because a
`canon/` path changes.

## 11. Stop conditions

STOP and do not promote if any of these occurs:

```text
scope SHA mismatch
bundle-manifest mismatch
any Registry/NORMATIVE/EVIDENCE/HISTORY disagreement
claim count other than 337 after this one-row fold
T count other than 214 after this one-row fold
new dependency or gate required by the checker
FRONTIER semantic delta
wording that upgrades density into boost uniqueness
wording that upgrades A_5 harmonic depth into Lorentz necessity
wording that selects J or physical p=5
any changed probe byte
any failed x86_64, aarch64 or aggregate check
any normative SHA256 mismatch
```

## 12. Promotion ceiling

The only scientific promotion authorized by this package is

```text
SO3-FINITE-ANISOTROPY-MAXIMUM [T]
```

at L1 with the exact scope in section 1. Everything else remains where Public
Canon v67 currently leaves it.
