# P-J-FIBONACCI-BRAID-1 preregistration

Date: 2026-09-03

Author of record: A. M. Thorn

Status: **PREREGISTERED / UNRUN / NON-CANONICAL**

Public claim lock: issue #795, opened before branch creation and before this
file was committed.

```text
branch:  probe/P-J-FIBONACCI-BRAID-1
path:    probes/P-J-FIBONACCI-BRAID-1/
owner:   A. M. Thorn / delegated session 2026-09-03
mode:    RESULT-EXPOSED / PROOF-FIRST
```

The accepted `verify.py` is newly authored for this probe. It may be read,
parsed, compiled, and inspected statically before the public pin, but it has
not been imported or executed. This file and `verify.py` must be committed in
one atomic pin, pushed, and read back byte for byte from the public remote
before the first formal scientific execution.

## Authority pin

At claim lock and branch creation:

```text
STATE:          ACTIVE
CANON:          Public Canon v75
AUTHORITY:      mathorn1973/twist-j main
BASE_COMMIT:    01b861c8e36cb56f9b4b24681018beec27d521eb
TAG:            canon-v75
TAG_TARGET:     c4f00e1d9c89f503d913224dc3c09dc760dcec9d
CONTENT_COMMIT: e32e85ed7297d4320df5b345e4488d78323d550c
CANON_SHA256:   44130160a3ce29bfcdc757e255d2d1c25a010b22911edfe66cf6b132be081fbe
CANON_BYTES:    399513
ACTION_LAYER:   L1 exact cyclotomic, integral-module, and matrix algebra
```

The base is the merge of the separate NON-CANONICAL note through PR #794.
The Canon activation tuple is unchanged. The content commit is an ancestor
of the tagged activation merge, and the recorded Canon hash and byte count
match `STATUS.md` and the release checksums.

This probe changes exactly its own directory. It changes no Canon, Registry,
Frontier, dependency, gate, evidence, workflow, release, decoder, or notes
file.

## Collision and prior exposure

Immediately before issue #795 was opened, exact local and remote searches
covered open and closed issues and pull requests, branch names, commit text,
the default-branch code index, public probe paths, the Registry, and local
refs. No formal branch, formal claim lock, probe path, PR, commit, Registry
row, or object lock named `P-J-FIBONACCI-BRAID-1` existed.

Issue #793 and the merged note
`notes/C-J-FIBONACCI-BRAID-1/README.md` disclosed this identifier as a
possible later probe, but expressly authorized no formal run or pin. They
also exposed the target values below. This probe is therefore
`RESULT-EXPOSED`: the written proofs and immutable first execution, not
surprise, are the evidence.

No accepted verifier has been imported or executed. Development reasoning,
the prior note, older public verifiers, and any hand calculation are
provenance only and are not evidence for this run.

## Public inputs and ownership

The probe consumes, without re-earning:

1. `J-STEP [T]`: the integral multiplication-by-`J` action.
2. `J-TENTH-ROOT [T]`: `1-J=-zeta_5^2` is a primitive tenth root.
3. `J-GOLDEN-BRIDGE [T]`: the exact `J`, `zeta_5`, and golden identities.
4. `CM-ALTERNATING-PENCIL [T]`: the public hyperbolic basis and pullback
   action.
5. `CM-ALTERNATING-PRIMARY-LATTICE-SEAM [T]`: the full integral primary
   lattices and their fixed bases.
6. `DEF-ACTION-LAYERS`: the L1 fence.

The verifier independently reconstructs the finite identities it uses from
the displayed inputs. That audit does not create duplicate public ownership.

The external naming input is the standard chiral Fibonacci fusion model:

- C. Nayak, S. H. Simon, A. Stern, M. Freedman, S. Das Sarma,
  *Non-Abelian anyons and topological quantum computation*, Reviews of
  Modern Physics 80 (2008), 1083--1159,
  DOI `10.1103/RevModPhys.80.1083`, immutable preprint
  `arXiv:0707.1889v2`, section IV.B.2, displayed equations (164), (167),
  and (168). The displayed equations, not the convention-sensitive prose
  immediately following equation (168), are the frozen source surface.

The sole external mathematical premise is the categorical identification of
the displayed `F_0` and `R` as the chosen chiral Fibonacci `F`- and `R`-data
in the ordered fusion basis `(1,tau)`. No physical-realization premise is
imported. The braid relation, integral gauge, invariant form, determinants,
module isomorphism, and two decisions are established inside this probe. No
universality or density theorem is used as a premise.

## Convention lock

Put

```text
zeta = exp(2 pi i/5),
a    = phi^-1 = zeta+zeta^-1,
J    = 1+zeta^2,
delta= 1-J = -zeta^2.
```

Freeze all conventions:

```text
field basis:        (1,zeta,zeta^2,zeta^3)
alternating order:  (01,02,03,12,13,23)
pullback:           P(W)=M_J^T W M_J on covariant alternating forms
fusion basis:       (1,tau)
positive generator: the braid generator represented by R below
word action:        rightmost matrix acts first
chirality:          the exact displayed R, not its complex conjugate
ribbon lift:        the displayed linear matrices, not projective rephasings
```

In the orthonormal fusion basis freeze

```text
F_0 = [[a,       sqrt(a)],
       [sqrt(a), -a      ]],

R   = diag(zeta^-2,-zeta^-1),

rho(sigma_1)=R,
rho(sigma_2)=F_0 R F_0.
```

Use the non-orthonormal integral gauge

```text
D     = diag(sqrt(a),1),
F_O   = D^-1 F_0 D = [[a,1],[a,-a]],
G_Fib = D^* D       = diag(a,1),
B_1   = R,
B_2   = F_O R F_O.
```

The distinguished physical embedding selects

```text
a=(sqrt(5)-1)/2 in (1/2,2/3),
```

so `G_Fib` is positive definite. The verifier isolates that positive root
with rational endpoint signs; it does not introduce a floating-point square
root.

Opposite chirality, arbitrary projective rephasing, the non-unitary
Galois/Lee--Yang branch, doubled Fibonacci theory, enriched carriers, and
approximation questions are outside scope.

## Field 1: fixed equations and carriers

Let `O_K=Z[zeta]` and write multiplication by `J` in the frozen field basis.
The accepted verifier must derive, rather than merely assume,

```text
M_J =
[[1,0,-1,1],
 [0,1,-1,0],
 [1,0, 0,0],
 [0,1,-1,1]],

det(M_J)=N(J)=1.
```

Let

```text
E_Z=Alt^2(Z^4),
E_Q=E_Z tensor Q,
q(x)=x^2-3x+1,
r(x)=Phi_10(x)=x^4-x^3+x^2-x+1.
```

Freeze the public vectors

```text
Omega_1=( 1, 0, 0,1,0,1),
Omega_2=( 0, 1,-1,0,1,0),

c1=(-1, 0,1,0,0,0),
c2=( 0,-1,0,1,0,0),
c3=( 0,-1,0,0,1,0),
c4=(-1, 0,0,0,0,1).
```

Define

```text
H_Q=ker q(P),       H_Z=H_Q intersect E_Z,
C_Q=ker r(P),       C_Z=C_Q intersect E_Z.
```

The verifier must reconstruct `P` from `M_J`, recover the displayed bases as
saturated full integral intersections, and derive the restrictions rather
than inserting them as untested outputs.

## Frozen claim A

The maximum first claim is

```text
J-CM-FIBONACCI-BRAID-PROJECTIVE-NONMEMBERSHIP
[candidate-T / proof-first / L1]
```

The hyperbolic restriction in the ordered basis
`(Omega_1,Omega_2)` is

```text
A_CM=[[ 1,-1],
      [-1, 2]],

tr(A_CM)=3,
det(A_CM)=1,
kappa(A_CM)=tr(A_CM)^2/det(A_CM)=9.
```

The frozen equality class is the widest basis- and scalar-independent one:

```text
Does there exist w in B_3, lambda in C^x, G in GL_2(C) with

    A_CM=lambda G^-1 rho(w) G ?
```

### Written proof of claim A

Direct multiplication gives

```text
F_O^2=I,
B_1 B_2 B_1=B_2 B_1 B_2,
B_i^* G_Fib B_i=G_Fib  for i=1,2.
```

Preservation of `G_Fib` is closed under products and inverses, so every
`rho(w)` preserves it. Since `G_Fib` is positive definite in the frozen
embedding, conjugating by a positive square root of `G_Fib` makes every
`rho(w)` unitary.

For any invertible two-by-two matrix set

```text
kappa(X)=tr(X)^2/det(X).
```

This is invariant under conjugacy and under multiplication of `X` by a
nonzero scalar. If a two-by-two unitary matrix has eigenvalues
`exp(i alpha_1),exp(i alpha_2)`, then

```text
kappa=2+2 cos(alpha_1-alpha_2)
     =4 cos^2((alpha_1-alpha_2)/2)
     in [0,4].
```

The exact value `9` is outside this interval. Therefore the displayed
projective-conjugacy equation has no solution. The same continuous invariant
separates `A_CM` from the closure of the projective-unitary locus. A bounded
braid-word search is neither performed nor logically relevant.

The verifier audits the finite premises of this proof. The universal
conclusion is carried by the written argument.

## Frozen claim B

The maximum second claim is

```text
J-CIRCULAR-FIBONACCI-DETERMINANT-CHARACTER
[candidate-T / proof-first / L1]
```

On `C_Z`, start with `v=c2`. The required orbit identities are

```text
v        =c2,
P v      =c1,
P^2 v    =c1-c4,
P^3 v    =c2-c3.
```

Their coordinate matrix in the ordered public basis `(c1,c2,c3,c4)` is

```text
T=[[0,1,1, 0],
   [1,0,0, 1],
   [0,0,0,-1],
   [0,0,-1,0]],

det(T)=1.
```

The multiplication-by-`x` companion in the basis `(1,x,x^2,x^3)` of
`Z[x]/(Phi_10)` is

```text
K_delta=
[[0,0,0,-1],
 [1,0,0, 1],
 [0,1,0,-1],
 [0,0,1, 1]].
```

Define the source and target `Z[x]` actions by

```text
x.u=delta u  on Z[delta],
x.v=P v      on C_Z,

Psi(delta^n)=P^n c2,   n=0,1,2,3.
```

The verifier must derive and check the full intertwiner equation

```text
P_C T=T K_delta,
```

including the fourth companion recurrence. Since `det(T)=1`, `Psi` is an
integral `Z[x]`-module isomorphism, not merely a rational cyclicity witness.

Also

```text
delta=1-J=-zeta^2,
delta^5=-1,
delta^10=1,
zeta=-delta^3,
Z[delta]=Z[zeta]=O_K.
```

In the frozen ribbon normalization,

```text
det(B_1)=det(B_2)=delta.
```

Let `e:B_3->Z` be exponent-sum abelianization and declare

```text
chi_C:B_3->Aut_Z(C_Z),
chi_C(sigma_1)=chi_C(sigma_2)=P_C,
chi_C(w)=P_C^e(w).
```

The braid relation has exponent sum three on both sides, so `e` is
well-defined. Determinant multiplicativity, including inverse generators,
gives

```text
det(rho(w))=delta^e(w).
```

The generator intertwiner and invertibility then extend to every word:

```text
Psi(delta^e(w) u)=chi_C(w) Psi(u).
```

Thus `chi_C` is integrally isomorphic to the restriction to the underlying
`Z`-lattice of the scalar determinant character. The universal word statement
is carried by this proof; the verifier audits the generators, inverses, and
module matrices.

This is an abelian rank-one `O_K` channel. It is not the frozen irreducible
rank-two `O_K` Fibonacci representation. No claim is made about a future
carrier with additional structure.

## Field 2: accepted code

The accepted `verify.py` is a deterministic, standard-library-only exact
audit. It uses:

- integers and `fractions.Fraction`;
- fixed four-coordinate arithmetic in `Q[zeta_5]=Q[z]/(Phi_5)`;
- exact rational matrix elimination, determinants, ranks, characteristic
  polynomials, maximal-minor gcds, and polynomial evaluation;
- exact two-by-two cyclotomic matrix arithmetic and conjugation.

It uses no float, builtin complex value, tolerance, numerical eigenvalue,
NumPy, SymPy, mpmath, file input, environment-dependent input, network,
subprocess, randomness, clock, dynamic import, `eval`, `exec`, or search over
braid words. It prints no path, host, user, clock, locale, or unordered
container.

Coefficient order for scalar polynomials is low-to-high. Characteristic
polynomials are reported and compared high-to-low.

## Field 3: carrier and data

There is no empirical dataset. The complete carrier is:

1. `O_K` in the frozen power basis;
2. `E_Z=Alt^2(Z^4)` in the frozen six-coordinate order;
3. the displayed public `Omega` and `c` vectors;
4. the displayed two-dimensional Fibonacci linear lift and integral gauge.

No hidden file, network response, finite braid cutoff, sampled word, or
external numerical constant is admitted.

## Field 4: systematics

The following are frozen systematic choices, not optimization parameters:

- principal positive embedding for `a`;
- chirality and exchange convention;
- full ribbon normalization of `R`;
- fusion-basis and rightmost-first convention;
- covariant alternating-form pullback, not the bivector convention;
- the two public primary bases and their order;
- projective conjugacy over `C` for claim A;
- the explicit Galois marking only where mentioned;
- compatible `O_K`-linearity for the rank-one boundary in claim B.

Changing any of these requires a new identifier and a new pin. Density cannot
be substituted for exact membership, and projective rephasing cannot be
substituted for the frozen determinant character.

## Field 5: gates, falsifiers, and decision

The accepted verifier has exactly seventeen gates.

```text
G01  exact fifth-cyclotomic field arithmetic
G02  J regular action, norm, determinant, and characteristic polynomial
G03  trace-form reconstruction of Omega_1,Omega_2 and saturation
G04  covariant pullback reconstruction, determinant, and Pfaffian covariance
G05  exact primary factorization, kernel ranks, and hyperbolic kernel membership
G06  derived A_CM, trace, determinant, and kappa
G07  integral Fibonacci gauge and generator determinants
G08  Fibonacci braid relation and noncommutativity
G09  exact Hermitian invariance and selected positive-root isolation
G10  finite proof inputs for the projective no-go
G11  full saturated circular lattice and index-five cross-check
G12  derived circular action, Phi_10 characteristic, and exact order ten
G13  unimodular c2 orbit
G14  delta identities, exact order, and ring equality
G15  full integral companion intertwiner
G16  frozen generator determinant identity
G17  B3 presentation-to-exponent-sum and inverse-generator intertwiner inputs
```

Claim A is `CONFIRMED` only if G01--G10 all pass and the written proof remains
valid. Claim B is `CONFIRMED` only if every prerequisite gate and G11--G17
pass and the written proof remains valid.

`SCIENTIFIC-FIRED-A` records an exact counterexample to the frozen
projective-nonmembership theorem or any failed finite premise. A finite
word-search miss is never evidence.

`SCIENTIFIC-FIRED-B` records an exact failure of the saturated circular
lattice, orbit unimodularity, `Z[delta]=O_K`, companion intertwiner, generator
determinants, or determinant-character proof.

`STOP` applies to authority drift, collision, pre-pin import or execution,
post-pin mutation, incomplete carrier, forbidden dependency, hidden
floating-point or complex arithmetic, file or network input, nondeterminism,
security or metadata failure, nonzero exit, nonempty stderr, transcript
mismatch, or architecture mismatch. Integrity failure alone is not a
scientific outcome.

A completed `PASS`, `SCIENTIFIC-FIRED-A`, or `SCIENTIFIC-FIRED-B` execution
exits zero with empty stderr and is followed by `EXPECTED.txt`, `RUN.md`, and
`RESULT.md`. An integrity `STOP` exits nonzero. A completed scientific
`FIRED` result is never relabelled as abandonment.

A successful probe changes no Canon status. Registration, if ever desired,
requires a separate fold.

## Frozen expected transcript

The exact successful stdout is preregistered as:

```text
SPEC FIB_CM_EXACT_V1
MODE RESULT-EXPOSED PROOF-FIRST
CHECK G01 FIELD PASS phi5=0 order_zeta=5 involution=conjugation
CHECK G02 J_REGULAR PASS det=1 norm=1 charpoly=Phi5(x-1)
CHECK G03 CM_FORMS PASS omega1=(1,0,0,1,0,1) omega2=(0,1,-1,0,1,0) saturated=yes
CHECK G04 PULLBACK PASS convention=covariant det=1 pfaffian=invariant
CHECK G05 PRIMARY PASS charpoly=q*Phi10 rank_qP=4 rank_phi10P=2 H_kernel=yes
CHECK G06 A_CM PASS matrix=((1,-1),(-1,2)) trace=3 det=1 kappa=9
CHECK G07 FIB_GAUGE PASS integral=yes det_F=-1 det_B1=det_B2=1-J
CHECK G08 FIB_BRAID PASS relation=yes noncommuting=yes
CHECK G09 FIB_HERMITIAN PASS generator_invariance=yes selected_a_interval=(1/2,2/3)
CHECK G10 A_PROOF_INPUTS PASS target_kappa=9 unitary_range=[0,4]
RESULT CLAIM_A J-CM-FIBONACCI-BRAID-PROJECTIVE-NONMEMBERSHIP CONFIRMED
CHECK G11 C_LATTICE PASS rank=4 saturated=yes seam_index=5
CHECK G12 C_ACTION PASS charpoly=Phi10 order=10
CHECK G13 C_ORBIT PASS determinant=1
CHECK G14 DELTA PASS value=1-J=-zeta^2 order=10 zeta=-delta^3
CHECK G15 MODULE PASS companion_intertwiner=yes
CHECK G16 GENERATOR_DETERMINANTS PASS value=1-J
CHECK G17 CHARACTER_PROOF_INPUTS PASS presentation=checked inverses=yes intertwiner=yes
RESULT CLAIM_B J-CIRCULAR-FIBONACCI-DETERMINANT-CHARACTER CONFIRMED
SCOPE raw_M_J=TYPE_BOUNDARY galois_branch=OUT_OF_SCOPE physical_tau_identification=NONE
RESULT OVERALL PASS gates=17 claims=2
```

Success requires exit zero, empty stderr, exact byte equality with the later
committed `EXPECTED.txt`, and byte-identical x86_64 and aarch64 workflow
replays. Any mismatch is `STOP`.

## Field 6: action layer and firewalls

This is L1 exact algebra only.

1. `PHIBIT-NOT-TAU [F]` remains closed. No phibit is identified with `tau`,
   and no other TWIST-J-object-to-anyon identification is made.
2. `CM-PERIOD-LATTICE-NONSELECTION [T]` retains its exact frozen no-go scope.
   No action, `h`, `hbar`, phase, period, geometric cycle, or physical `U(1)`
   is selected.
3. `METRO-EDGE-SCALE [O]` remains open. No SI scale or calibration is
   supplied.
4. `DEF-QDD-BRANCH-WEIGHT-PAIRING` remains an algebraic dictionary, not a
   physical Born pairing and not an input here.
5. `QDD-INSTRUMENT-APPARATUS [O]` remains open. No state, preparation,
   apparatus, effect, event, occurrence law, sampling, measure, or Born rule
   is supplied.
6. No topological protection, physical universality, quantum advantage,
   speedup, continuum limit, or L2--L6 lift is claimed.
7. The determinant character depends on the frozen linear ribbon lift. It is
   deliberately not claimed as a projective invariant.

## Formal order

1. Commit and push this `PREREG.md` and the accepted `verify.py` together in
   one atomic pin before the accepted verifier is imported or executed.
2. Read both public remote blobs back. Record the pin commit, blob identities,
   SHA-256, byte counts, line endings, and final LF in issue #795.
3. Only after that readback execute the pinned verifier exactly once in a
   neutral deterministic environment.
4. Add only `EXPECTED.txt`, `RUN.md`, and `RESULT.md` after the completed run.
5. Open one probe-only pull request and require x86_64, aarch64, aggregate
   policy PASS, exact transcript replay, and manual security review.
6. Never amend, rebase, squash, force-push, rename, resume, or reuse the probe
   after the pin.

If no gate completes after the public pin, the only abandonment route is to
leave the pinned `PREREG.md` and `verify.py` unchanged and add only a
`RESULT.md` carrying `Status: ABANDONED`; no `EXPECTED.txt` or `RUN.md` is
created, and the probe identifier remains consumed. That route is unavailable
after any completed scientific `PASS` or `FIRED` execution.
