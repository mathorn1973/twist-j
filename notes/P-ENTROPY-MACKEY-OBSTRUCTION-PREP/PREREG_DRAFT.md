# P-ENTROPY-MACKEY-OBSTRUCTION preregistration

Status: PRE-PIN DRAFT — NO RESULT

This document freezes the prospective decision surface for one confirmatory
public computation.  It contains no gate output and earns no scientific
status.  Formal execution touching the cyclotomic quotient, the public
`F_5^6` carrier, or the recurrent core is forbidden until this file and the
accepted final `verify.py` have been reviewed, committed, pushed, hashed, and
read back as one immutable public pin.

## Public identity and authority

```text
issue:            https://github.com/mathorn1973/twist-j/issues/241
probe:            P-ENTROPY-MACKEY-OBSTRUCTION
branch:           probe/P-ENTROPY-MACKEY-OBSTRUCTION
path:             probes/P-ENTROPY-MACKEY-OBSTRUCTION/
owner:            mathorn1973 / A. M. Thorn, coordinated in this Codex task
parent:           ENTROPY-LAYER-BRIDGE [O]
public basis:     Public Canon v30
activation/main: b8d4d585820d04ebd008444661f3a71d6e24f423
tag:              canon-v30
content commit:   857223fcd5e7bc8c8e68f1df768d6e8222b24ee0
Canon SHA-256:    2a32dcbd61ee7792fc2cb990b7f223e08876d71bf7ddcf5ec432acd055f3986a
Canon bytes:      157167
ceiling:          C on the exact finite subclass after the required
                  two-architecture byte-identical computation gate
```

The authority tuple, tag ancestry, content ancestry, all five normative hashes,
Canon check, ledger check, public issues, pull requests, branches, registry,
probe paths and claim/object locks were checked before issue 241 was opened.
The issue claims exactly this probe.  It moves no Canon row and authorizes no
release action.

## Question and scope

At exact depth `lambda^5` and Thue–Morse substitution-factor level
`s_TM >= 2`, decide the following conditional obstruction surface.

Let

```text
O       = Z[z]/(z^4+z^3+z^2+z+1),       z = zeta_5,
lambda  = 1-z,
Q_5     = O/lambda^5,
J       = 1+z^2,
T_src(kappa,q) = (S kappa, J q).
```

The admitted target is the public recurrent readout, on each living half,

```text
X_target = (disjoint union of 312 regular D_5-sets) disjoint union D_5/C_2.
```

The prospective class consists only of measurable almost-everywhere families
of fiber bijections from `Q_5` to a living half that intertwine the source and
target extensions under the one public coordinate reconstruction, one global
`D_5`, and one common four-edge cocycle frozen below.  A block-dependent group,
Mackey range, coordinate reconstruction, cocycle, or post-hoc gauge is outside
the class.

The successful arithmetic obstruction is

```text
source component count:       629, for every s_TM >= 2,
complete common-M target menu: {313,625,1563,3125},
decision equation:            629 not in {313,625,1563,3125}.
```

Passing finite arithmetic without the written theorem chain in this document
is `INCOMPLETE / STOP`, not an obstruction result.

## Written theorem chain frozen before execution

### T1. Integral quotient and induced J action

In the basis `(1,z,z^2,z^3)`, multiplication by `z` is

```text
C =
[0 0 0 -1]
[1 0 0 -1]
[0 1 0 -1]
[0 0 1 -1].
```

Set `A=(I-C)^5` and `M=I+C^2`.  The verifier must derive, not install as its
working objects,

```text
A =
[ -5  15 -20  15]
[-10  10  -5  -5]
[  5   5 -10  10]
[-15  20 -15   5]

M =
[1 0 -1 1]
[0 1 -1 0]
[1 0  0 0]
[0 1 -1 1].
```

For an invertible integer matrix `A`, the exact signature

```text
sigma_A(x) = adj(A) x mod |det A|
```

has kernel `A Z^4`: `sigma_A(x)=0` iff `A^(-1)x` is integral.  It therefore
constructs `Z^4/AZ^4` without an assumed representative table.  GCDs of every
`k x k` minor give the determinantal divisors.  The frozen result is

```text
(Delta_1,Delta_2,Delta_3,Delta_4) = (5,25,125,3125),
SNF(A) = (5,5,5,25),
Q_5 ~= Z/5 + Z/5 + Z/5 + Z/25,
|Q_5| = 3125.
```

Because `A` and `M` are polynomials in `C`, `MA=AM`; hence `M` induces a
well-defined permutation `J_5` of the quotient.  Direct enumeration must give

```text
cycles(J_5) = {1:1,4:1,20:156},
order(J_5)  = 20,
unique fixed class = 0.
```

### T2. Thue–Morse product-component lemma

The two-sided Thue–Morse substitution is primitive, aperiodic, constant length
two and height one.  The specialized constant-length substitution eigenvalue
theorem says that its root-of-unity measurable eigenvalues are exactly the
dyadic roots of unity.  The pinned primary source is F. M. Dekking, *The
Spectrum of Dynamical Systems Arising from Substitutions of Constant Length*,
Z. Wahrscheinlichkeitstheorie verw. Gebiete 41 (1978), 221–239,
doi:10.1007/BF00534241, specialized to the Morse–Thue substitution
`0 -> 01, 1 -> 10`.  Equivalently, the finite-order part of its Kronecker
factor is the character group of the dyadic odometer.  This is the only
Thue–Morse spectral input used here; no continuous-spectrum or entropy claim is
made.

For an ergodic probability transformation `S` and the cyclic rotation on
`C_m`, Fourier decomposition in the cyclic coordinate identifies invariant
functions of the product with the direct sum of the eigenspaces of `S` whose
eigenvalues are `m`-th roots.  In an ergodic system each such eigenspace is
one-dimensional.  Therefore the number of product ergodic components is the
size of the intersection between the measurable eigenvalue group and the
`m`-th roots.  For Thue–Morse this is

```text
gcd(m,2^s_TM) = 2^min(v_2(m),s_TM)
```

at the level-`s_TM` dyadic factor and stabilizes to `2^v_2(m)`.  Applied to T1,

```text
c_src(0) = 1 + 1 + 156     = 158,
c_src(1) = 1 + 2 + 156*2   = 315,
c_src(s_TM) = 1 + 4 + 156*4 = 629  for every s_TM >= 2.
```

Every printed occurrence of `629` must carry the scope `s_TM>=2`.  The finite
audit at `s_TM=0..8` checks the formula; it is not the proof of the all-level
statement.  If the specialized measurable-eigenvalue theorem is rejected or
its hypotheses do not apply to the declared two-sided probability system, the
scientific decision is `INCOMPLETE / STOP`.

### T3. Finite-extension Mackey orbit lemma

Let an ergodic probability base carry a measurable cocycle into a finite group
`G`, and let `M <= G` be its Mackey range, defined up to conjugacy.  On a finite
`G`-set `Y`, the invariant sigma-algebra of the skew product is indexed by the
`M`-orbits of `Y`: after reduction to the essential range, an invariant
function is constant exactly on those orbits.  Thus the number of ergodic
components of the finite extension is the number of `M`-orbits.

Here `G=D_5`.  Every subgroup is enumerated, not merely one representative:
`D_5`, `C_5`, all five reflection subgroups `C_2`, and `{1}`.  Direct orbit
counting on each reconstructed half must give

```text
M       regular D_5-set   D_5/C_2   total on 312 regular plus singlet
D_5             1             1       313
C_5             2             1       625
each C_2        5             3       1563
{1}            10             5       3125.
```

The five reflection rows must be checked separately even though their totals
are conjugate.  Removing the common-`M` requirement gives the binding mixed
control

```text
312*a+b=629,  a in {1,2,5,10}, b in {1,3,5},
unique solution (a,b)=(2,5).
```

This shows that the common range, not cardinality alone, is load bearing.

### T4. Almost-everywhere conjugacy invariant

A measure-space isomorphism defined modulo null sets and intertwining two
transformations modulo null sets pulls back their invariant sigma-algebras
bijectively.  It therefore transports the ergodic decomposition and preserves
the finite number of ergodic components.  Consequently a source count absent
from the complete common-range target menu excludes an almost-everywhere
conjugacy only in the exactly declared class.

### T5. Haar quotient and conditional Route A embedding

The reduction map

```text
pi_5: O_(K,lambda) -> O/lambda^5
```

is a continuous surjective homomorphism of compact additive groups.  Its
pushforward of normalized Haar probability is translation invariant on the
finite quotient and hence uniform, because quotient translations act
transitively.  Each coset therefore has mass `1/3125`.

The Thue–Morse substitution matrix has normalized Perron vector `(1/2,1/2)`,
so each one-letter cylinder has mass `1/2`.  A measurable fiberwise bijection
from every `Q_5` fiber to the corresponding 3125-state living half therefore
gives, conditionally and only in this subclass,

```text
(1/2)(1/3125) = 1/6250
```

for each recurrent state.  Exact equivariance without Haar uniformity and
fiberwise bijectivity does not imply this mass.  T5 constructs no map and no L6
measure; it only types the conditional finite-subclass implication.

## Six frozen preregistration fields

### Field 1 — equation and exact gates

The equation is T1 through T5 together with the exact target reconstruction
and common-cocycle gate below.  The public five-generator table, selector and
warmup-400/window-300 census protocol are rebuilt inside the verifier.  The
recurrent core must have 6250 states on 313 components, split on each living
half into 312 ten-point components and one five-point singlet.

One global `D_5` is constructed before any component is traversed.  On sheet
`H_1`, its rotation is the public word `d o (b e b)`; on `H_0` it is transported
by the one fixed public `b` bridge.  The ten permutations and their
multiplication table are verified on every recurrent state.

The public coordinate reconstruction for this probe freezes

```text
Gamma = {identity},
gamma(component) = identity for every component.
```

This rule is fixed before target inspection, sees no edge, point, label or
search result, and is a proper subgroup of `D_5`.  The probe classifies this
one coordinate reconstruction only; it does not classify alternative gauges.
The four normalized edges must be common across all 312 generic components and
compatible with the singlet; the cross edges are identities, the own edges are
distinct nonidentity reflections, and their product has order five and
generates `D_5`.

### Field 2 — accepted code

One self-contained `verify.py` in this directory.  Python 3.12 standard library
only; exact `int` and `Fraction` only; no float in an assertion; no network,
subprocess, dynamic import, random order, external data, file read, or file
write.  Output is deterministic, architecture-neutral and byte-stable.  The
only accepted formal command is

```text
python3 probes/P-ENTROPY-MACKEY-OBSTRUCTION/verify.py
```

The final verifier runs all mandatory synthetic controls first, then the T1/T2
source reconstruction and T5 arithmetic, then the full target and subgroup
menu, and finally the combined decision.  Target runtime must remain below the
repository workflow limit of 600 seconds.

### Field 3 — carriers and data

No external data.  Exact carriers are `Z^4/AZ^4`, the level-`s_TM` dyadic
factors used to audit T2, the public `F_5^6` kernel, its complete recurrent
core and living halves, abstract `D_5`, all 312 regular components, and the
singlet `D_5/C_2`.  Public dependencies are used only at their v30 scope:
`CENSUS-313 [C]`, `CENSUS-Z5-SHEET [C]`, `CENSUS-HOSTING [C]`,
`ENTROPY-LIVING-SET [C]`, `ENTROPY-COUNT-MATCH [C]`,
`ENTROPY-MIRROR-LAW [C]`, `COLOR-TORSOR-HOLONOMY [T]`, and only the `k=0`
compatibility facts of `ENTROPY-RG-RETURN [C]`.  The verifier nevertheless
reconstructs every finite value it consumes.

### Field 4 — systematics and preparation disclosure

```text
S1  The v30 authority tuple and five normative hashes still match at pin.
S2  Every 629 statement is explicitly scoped to s_TM>=2.
S3  The source quotient uses adjugate signatures and all minors; no imported
    quotient table or lambda-digit certificate is accepted.
S4  The all-level component statement rests on T2; s_TM=0..8 is only an audit.
S5  The recurrent core is rebuilt by the public census protocol, not a warmed
    sample or imported support list.
S6  The global D_5 exists before component traversal; no per-component group,
    basepoint, reflection, bridge or gauge may define it.
S7  Gamma and its constant rule are frozen above and never selected by labels.
S8  All 312 generic components, the singlet and all eight subgroups are direct
    inputs to exhaustive checks; no representative-only counting.
S9  Scientific disagreement exits zero and is preserved; instrument/input
    defects are STOP and exit nonzero.
S10 T5 uses translation invariance plus transitivity, never cardinality alone.
S11 Source and target are two legs of one confirmatory verifier.  The required
    architectures reproduce that instrument; they are not independent methods.
S12 No finite pass may be presented as A_A=empty or bridge closure.
```

This is not a blind prediction.  Expected source and target values and older
implementations were exposed in a non-canonical v28 incubation lane.  They have
zero evidence credit and are not runtime dependencies.  Exact disclosure:

```text
target predecessor prereg SHA-256:
  45192f7fcbe3b1699f69ccd35351c8a8ddc756e488a2f01ee0d0491e197f03e6
target predecessor code SHA-256 / bytes:
  c00a2897f6dc5038e0e08a4c22e310bae0e219206cf0200636dbf168584038e4 / 48471
real predecessor target-carrier executions: none
predecessor synthetic-only runs: four; final stdout 925 bytes, SHA-256
  e6205bab0bbfb005c4c1d0cb11ed501984e4c86d722126326b6dff7aab4f4321
compatibility planning audit SHA-256:
  6de06529ffe6bfeabd720d9bab996479074925baf711974efde4ea37e87cf956
source planning draft SHA-256:
  f6d4fb7a061b7488efdfeabd9f7894957e8478a947be1fdf1037505c4ad5cc32
```

The first historical target development hash and the timestamps/hashes of the
first two synthetic transcripts were reconstructed after the fact rather than
recorded contemporaneously.  No run above is formal evidence.  The inherited
target logic is statically adapted for public naming, neutral stdout and a
combined interface; it is not described as a new independent v30 method.

### Field 5 — controls, falsifiers and outcome vocabulary

Mandatory controls run before any real carrier:

```text
N1 TARGET REJECT: four synthetic regular D_5 components carry four different
   edge tuples; the common-cocycle checker rejects.
N2 TARGET REJECT: one of four otherwise common synthetic components has one
   edge perturbed by a reflection; the checker rejects.
N3 TARGET ACCEPT: four components genuinely share one cocycle; checker accepts.
N4 LATTICE REJECT: a synthetic integer matrix with a changed determinantal
   divisor is rejected by the minor/invariant-factor checker.
N5 CYCLE REJECT: the identity permutation on 3125 abstract points is rejected
   against the frozen J cycle census.
N6 PLATEAU REJECT: abstract census {1:1,4:1,10:2,20:155}, which preserves the
   high-level 629 plateau but changes low levels, is rejected.
N7 PRODUCT REJECT: replacing (i,j)->(i+1,j+1) by (i+1,j) on C_20 x C_8 is
   rejected against gcd(20,8)=4.
N8 TRANSLATION REJECT: an abstract order-five translation subgroup on
   Z/5 x Z/5 x Z/5 x Z/25 is rejected as nontransitive.
```

Controls test the instrument and are never evidence about the real carriers.

```text
OBSTRUCTION-CERTIFIED, ceiling C
  Every control passes; T1 through T5 and every target gate pass; one common
  cocycle survives the frozen coordinate reconstruction; both target menus are
  exactly {313,625,1563,3125}; and 629[s_TM>=2] is absent.

ROUTE-FALSIFIED
  A complete admitted-carrier computation supplies an exact witness against a
  frozen source value, common cocycle, target decomposition, subgroup menu or
  component-invariance premise.  Preserve the witness and exit zero.  Failure
  of the common cocycle falsifies this route; it does not prove the bridge empty.

STOP_INPUT_RECONSTRUCTION_DEFECT
  The v30 public carrier, generator table, census input or typed dependency
  cannot be reconstructed.  This is not scientific disagreement.

STOP_INSTRUMENT_DEFECT
  A mandatory control has the wrong verdict, a certificate fails, the code is
  nondeterministic or architecture-dependent, a float enters an assertion, or
  a forbidden dependency or side effect is present.

INCOMPLETE / STOP
  Any carrier, gauge, equality convention, T2/T3/T4/T5 premise, prospective
  pin, run record or two-architecture transcript is missing.
```

No tolerance, adaptive threshold, post-output gauge, scope repair, or expected
value change is permitted.  If this preregistration must move after the first
real-carrier execution, retire the identifier and preserve the run.

### Field 6 — action layer and firewall

```text
FROM:       L2 two-sided Thue-Morse probability system and lambda-adic source,
            through the exact finite quotient O/lambda^5
TO:         L5 finite recurrent checkpoint readout
DEPTH:      lambda^5 exactly
LEVEL:      s_TM>=2 for every 629 conclusion
MAP CLASS:  measurable a.e., fiberwise-bijective conjugacy under the frozen
            global D_5 coordinate reconstruction and identity gauge
NEW LIFT:   none
L6:         excluded
SI:         excluded
```

Explicitly excluded: variable or deeper lambda depth, nonbijective fibers,
non-factorizing maps, alternative gauges, other collar classes, arbitrary
finite-cylindrical maps, all of `A_A`, a physical measure, entropy rate,
continuum limit, SI statement, registry move, Canon edit or release action.

## Pin and execution boundary

Before the first formal run: recheck authority and collisions; statically and
adversarially review the complete final `PREREG.md` and `verify.py`; stage only
those two named files; commit as `A. M. Thorn <thorn@twistj.com>`; push the
branch; read back exact remote bytes; record the full pin commit and both
SHA-256 hashes.  Only then may the one accepted command run.  Its exact stdout
becomes `EXPECTED.txt`; neutral local metadata go in `RUN.md`; `RESULT.md`
records every fired falsifier.  The later pull request changes only this probe
directory and must pass the repository's x86_64 and aarch64 byte-identical
workflow gate.

Current freeze record:

```text
PREREG.md:        draft, not committed or pushed
verify.py:         complete static-review candidate; not committed, pushed, or executed
formal execution: none
EXPECTED/RUN/RESULT: absent
status earned:    none
```
