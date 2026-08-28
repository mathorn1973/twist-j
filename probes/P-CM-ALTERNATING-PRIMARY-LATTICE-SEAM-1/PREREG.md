# P-CM-ALTERNATING-PRIMARY-LATTICE-SEAM-1 preregistration

Date: 2026-08-28

Author of record: A. M. Thorn

Status: preregistered protocol only. Formal execution count zero. No
scientific result is earned by this file. The accepted `verify.py` may be
read, parsed, compiled, and inspected statically before the pin, but it has
not been imported or executed. This file and `verify.py` must be committed
together, pushed, and read back byte for byte from the public remote before
the first formal scientific execution.

Public claim lock: issue 625, opened before this file was committed.

```text
branch:  probe/P-CM-ALTERNATING-PRIMARY-LATTICE-SEAM-1
path:    probes/P-CM-ALTERNATING-PRIMARY-LATTICE-SEAM-1/
owner:   A. M. Thorn
mode:    RESULT-EXPOSED, proof-first; the verifier is an exact audit
```

## Authority

```text
STATE:          ACTIVE
CANON:          Public Canon v68
AUTHORITY:      mathorn1973/twist-j main
TAG:            canon-v68
TAG_TARGET:     b72505f55bcf2ef3d5985065ae52f3365966f32e
CONTENT_COMMIT: d755c5758406bfed13405dde0864c2ce81f5f581
CANON_SHA256:   63370401c2e25d94e7d8f94bdf142ba32fe3c2a5cdf81d1435114b669b0e5546
CANON_BYTES:    353145
BASE_COMMIT:    b72505f55bcf2ef3d5985065ae52f3365966f32e
ACTION_LAYER:   L1 exact integral/rational alternating-form algebra only
```

Immediately before issue lock and branch creation, public `main`, all remote
heads, open and closed issues and pull requests, `STATUS.md`, `POLICY.md`,
`AGENTS.md`, `canon/CORE.md`, `canon/FRONTIER.md`, the registry, Canon,
dependencies, evidence, public probes, the immutable v68 release manifest,
and release checksums were read from a clean checkout. The annotated tag
targets the activation merge, the content commit is its ancestor, the
recomputed Canon hash and byte count match `STATUS.md`, and the release's
x86_64, aarch64, and aggregate checks are successful.

This probe changes exactly its own directory. It changes no Canon, registry,
frontier, dependency, evidence, gate, release, workflow, or decoder file.

## Collision, prior exposure, and adjacent ownership

No issue, pull request, remote branch, public probe path, registry row, object
lock, or claim lock named
`P-CM-ALTERNATING-PRIMARY-LATTICE-SEAM-1` or
`CM-ALTERNATING-PRIMARY-LATTICE-SEAM` existed at lock time. The collision
search covered both names and the aliases `PRIMARY-SPLIT`, `PRIMARY-GLUE`,
`INTEGRAL-SEAM`, `LATTICE-SEAM`, `ACTION-STABLE-PERIOD`, and the relevant
matrix, Pfaffian, resultant, projector, and index-five formulas.

This probe is `RESULT-EXPOSED`. The matrices, primary factorization,
saturated lattices, index-five seam, projector, resultant, and null-eigenform
consequence were already derived independently with exact integers and
fractions and were disclosed in the public discussion before this pin. Those
calculations and any development scripts are provenance only, not evidence.
The accepted public verifier is a fresh deterministic standard-library
implementation and has never been imported or executed at pin time. Its
exposed target values are preregistered thresholds, not discoveries.

Existing public objects retain their ownership:

1. `CM-ALTERNATING-PENCIL [T]` owns `Omega_1`, `Omega_2`, their integral
   trace construction, `Pf(a Omega_1+b Omega_2)=a^2-ab-b^2`, the Pell and
   unimodular locus, the unit action, `A_J=[[1,-1],[-1,2]]`, its eigenvalues
   `phi^(+/-2)`, Pfaffian covariance, and the explicit fact that `J` does not
   scale a fixed pencil member by `phi^-2`.
2. TH7 of `P-J-LI-TORAL-HAAR-1` already audits
   `chi_(Lambda^2 M_J)=(x^2-3x+1) Phi_10(x)` on two architectures. No
   registered theorem presently owns that exact factorization. This probe
   gives it an explicit characterization but does not count it as independent
   new evidence.
3. `J-HARMONIC-SEAM [T]` owns `O_K^x=mu_10 x <phi>`.
4. `AFFINE-READING-DEGREE-CENSUS [T]` owns the dimension of the alternating
   motor-invariant sector, not the primary lattice statement below.
5. `J-TORAL-ENTROPY [T]` owns the toral eigenvalue moduli
   `phi,phi,phi^-1,phi^-1` and `h_top=2 log phi`. The unstable real two-area
   ratio `phi^2=e^(h_top)` is an L2 characterization of that theorem, not a
   Pfaffian scaling and not evidence here.
6. `BRIDGE-DEFECT [T]` retains the algebraic/transcendental separation. This
   probe supplies no `2 pi`.

The divergent branch `notes/c-j-artin-mazur-zeta-1-n` at
`424abb432306644656afda13fe0af774b9da4060`, closed issue 454, and closed
unmerged pull request 455 retain their provenance. They are not resumed,
renamed, rebased, or used as public evidence.

## Field 1: fixed equation and coordinates

Use the ordered basis `1,j,j^2,j^3` of `O_K=Z[j]`. Public `J-STEP [T]` gives
the multiplication matrix

```text
M_J =
[[1,0,-1,1],
 [0,1,-1,0],
 [1,0, 0,0],
 [0,1,-1,1]].
```

Write an alternating form in upper-triangular coordinates, in the immutable
order

```text
w = (w01,w02,w03,w12,w13,w23)^T,
E_Z = Alt^2(Z^4) = Z^6,
E_Q = E_Z tensor Q.
```

The covariant pullback action is

```text
P(W) = M_J^T W M_J.
```

The term “exterior-square action” in this probe always means this pullback on
alternating covariant forms. It is not silently replaced by the matrix on
bivectors. Those conventions have the same characteristic polynomial here,
but their coordinate matrices are transposed relative to the pairing.

Freeze

```text
q(x) = x^2 - 3x + 1,
r(x) = Phi_10(x) = x^4 - x^3 + x^2 - x + 1,

Omega_1 = (1,0, 0,1,0,1)^T,
Omega_2 = (0,1,-1,0,1,0)^T,

H_Q = ker q(P),     H_Z = H_Q intersect E_Z,
C_Q = ker r(P),     C_Z = C_Q intersect E_Z.
```

The fixed circular lattice witnesses are

```text
c1 = (-1, 0,1,0,0,0)^T,
c2 = ( 0,-1,0,1,0,0)^T,
c3 = ( 0,-1,0,0,1,0)^T,
c4 = (-1, 0,0,0,0,1)^T.
```

## Frozen theorem

The maximum later claim is

```text
CM-ALTERNATING-PRIMARY-LATTICE-SEAM [T ceiling; L1]
```

with exactly the following five parts.

S1. The pullback matrix has characteristic polynomial

```text
chi_P(x) = q(x) r(x)
         = x^6-4x^5+5x^4-5x^3+5x^2-4x+1.
```

Both factors are irreducible over `Q` and occur with multiplicity one. Thus

```text
E_Q = H_Q direct-sum C_Q.
```

The restriction `P|C_Q` has exact order ten.

S2. The hyperbolic primary plane is exactly the public CM pencil and its full
integral intersection is

```text
H_Q = Q Omega_1 direct-sum Q Omega_2,
H_Z = Z Omega_1 direct-sum Z Omega_2.
```

In particular `H_Z` is saturated in `E_Z`. This is a cross-row
characterization, not an additional physical selector.

S3. The circular integral intersection is the saturated lattice

```text
C_Z = Z c1 direct-sum Z c2 direct-sum Z c3 direct-sum Z c4.
```

The rational direct sum does not split into the two canonical integral
primary lattices:

```text
H_Z intersect C_Z = 0,
[E_Z : H_Z direct-sum C_Z] = 5,
E_Z/(H_Z direct-sum C_Z) is Z/5.
```

Put

```text
A(w) = w01+w03+w23,
B(w) = w02+w12+w13,
ell(w) = 2 A(w)+B(w) mod 5.
```

Then `ker ell=H_Z direct-sum C_Z` and

```text
ell(Pw) = -ell(w) mod 5.
```

Thus `P` acts as `-1` on the five-element seam.

S4. The exact Bezout identity is

```text
(8-3x) r(x) + (3x^3-2x^2+2x-3) q(x) = 5.
```

The unique rational primary projector with image `H_Q` and kernel `C_Q` is

```text
E_H = ((8-3P) r(P))/5
    = (-3P^5+11P^4-11P^3+11P^2-11P+8I)/5.
```

It is `P`-equivariant and its smallest common denominator is exactly five.
This qualifier is essential: since `H_Z` is saturated, noncanonical integral
complements and projections exist. What fails integrally is precisely this
canonical `P`-primary split. Also

```text
|Res(q,r)| = 25,
q mod 5 = (x+1)^2,
r mod 5 = (x+1)^4.
```

The index five is proved separately by the explicit lattice determinant and
seam functional. It is not inferred from the resultant twenty-five.

S5. Pfaffian covariance and `det M_J=1` give

```text
Pf(PW) = Pf(W).
```

Consequently

```text
PW=lambda W,  lambda in {phi^2,phi^-2}
implies Pf(W)=0.
```

The two nonzero real eigenforms

```text
omega_s = Omega_1 + phi^-1 Omega_2,   P omega_s = phi^-2 omega_s,
omega_u = Omega_1 - phi Omega_2,      P omega_u = phi^2 omega_u
```

are Pfaffian-null and have rank two. They are not symplectic, and no nonzero
rational or integral form lies on either eigenline.

## Written proof

The proof is self-contained. The verifier audits its finite identities and
does not replace any universal lattice or polynomial argument.

### Pullback matrix and Pfaffian law

For the six elementary alternating matrices, direct multiplication by the
fixed integer matrix gives the six columns

```text
P =
[[ 1, 0, 1,-1, 0, 1],
 [-1, 1,-1, 1, 0,-1],
 [ 0,-1, 1, 0, 0, 1],
 [ 1, 0, 1, 0, 0, 0],
 [-1, 0,-1, 0, 1, 0],
 [ 1, 0, 0, 0,-1, 0]].
```

Integer elimination gives `det M_J=1`. For every alternating four by four
matrix, exterior algebra gives

```text
Pf(M^T W M)=det(M) Pf(W).
```

Equivalently, with

```text
Pf(w)=w01 w23-w02 w13+w03 w12,
```

substitution of the displayed six linear coordinates gives the same
quadratic polynomial. Hence `Pf(Pw)=Pf(w)` identically, not merely on sampled
forms.

### Characteristic factors and rational primary components

Exact Faddeev-LeVerrier elimination on the displayed `P` gives

```text
det(xI-P)=x^6-4x^5+5x^4-5x^3+5x^2-4x+1=q(x)r(x).
```

The discriminant of `q` is five, and `2^2<5<3^2`, so `q` is irreducible over
`Q`. Substitution gives

```text
r(-x-1)=x^4+5x^3+10x^2+10x+5,
```

which is Eisenstein at five. Thus `r` is irreducible over `Q`. The displayed
Bezout identity below makes `q` and `r` coprime over `Q`. Since both occur
once in the characteristic polynomial, the primary decomposition theorem
gives `E_Q=H_Q direct-sum C_Q`, of dimensions two and four.

Direct substitution gives

```text
P Omega_1 = Omega_1-Omega_2,
P Omega_2 = -Omega_1+2 Omega_2.
```

Therefore both independent CM forms lie in `ker q(P)`. That kernel has
dimension two, so they fill it and prove S2 over `Q`.

For the circular side, solving the two independent equations gives

```text
C_Q = {w in Q^6 :
       w01+w03+w23=0,
       w02+w12+w13=0}.
```

The four displayed `c_i` are independent and solve these equations, hence
form a `Q`-basis of `C_Q`. The identity `r(P)|C_Q=0`, together with
`r(x)=Phi_10(x)`, gives `P^5=-I` and `P^10=I` there. Since `P` is not `-I`
on `C_Q`, its order is exactly ten.

### Full integral intersections and the five-element seam

Every element of `H_Q` has the unique coordinates

```text
a Omega_1+b Omega_2=(a,b,-b,a,b,a).
```

If this vector is integral, its first two coordinates force `a,b` to be
integers. This proves the equality for `H_Z` and its saturation.

For `C_Q`, the defining map

```text
(A,B): Z^6 -> Z^2
```

is surjective because the first and second standard basis vectors map to
`(1,0)` and `(0,1)`. Its kernel is therefore saturated. Solving the two
equations integrally with free variables `w03,w12,w13,w23` gives exactly the
four displayed `c_i`, proving the equality for `C_Z`.

The determinant of the six columns

```text
[Omega_1 Omega_2 c1 c2 c3 c4]
```

is `+5`. Hence their direct sum has index five in `E_Z`; its cokernel has
prime order and is therefore cyclic. The functional `ell=2A+B mod 5`
annihilates all six columns and is surjective. Its kernel also has index five,
so it equals `H_Z direct-sum C_Z`. Direct multiplication of its coefficient
row gives

```text
ell P = -ell mod 5,
```

which proves the quotient action in S3.

### Resultant and the exact primary projector

Expanding gives the frozen Bezout identity. It proves that

```text
E_H=((8-3P)r(P))/5
```

is the identity on `H_Q` and zero on `C_Q`; hence it is idempotent, has the
claimed image and kernel, and commutes with `P`. Explicit evaluation gives

```text
E_H = (1/5) *
[[ 2, 1, 2, 1, 1, 2],
 [-1, 2,-1, 2, 2,-1],
 [ 1,-2, 1,-2,-2, 1],
 [ 2, 1, 2, 1, 1, 2],
 [-1, 2,-1, 2, 2,-1],
 [ 2, 1, 2, 1, 1, 2]].
```

The numerator entries have content one, so the common denominator five
cannot be reduced. Since image and kernel determine a projection uniquely,
no other projector for this fixed rational primary decomposition avoids it.

The exact Sylvester determinant is `Res(q,r)=25`. Reduction modulo five gives
the two displayed powers of `x+1`; this records the ramified collision of the
two primary factors but is not used as a substitute for the index computation.

### Null eigenforms and the scope guard

On the CM basis the matrix of `P` is the public

```text
A_J=[[1,-1],[-1,2]].
```

Using `phi^2=phi+1` and `phi^-1=phi-1` gives the two displayed eigenforms and
eigenvalues exactly. Their Pfaffians are

```text
Pf(omega_s)=1-phi^-1-(phi^-1)^2=0,
Pf(omega_u)=1+phi-phi^2=0.
```

Both have `w01=1`, so a two by two minor is nonzero. A four by four
alternating determinant is the square of the Pfaffian; therefore both forms
have rank exactly two. More generally, if `PW=lambda W`, then

```text
Pf(W)=Pf(PW)=Pf(lambda W)=lambda^2 Pf(W).
```

For `lambda=phi^(+/-2)`, `lambda^2` is not one, so `Pf(W)=0`. Since these
eigenvalues are irrational while `P` has rational entries, a nonzero rational
eigenvector would make an irrational eigenvalue equal to a ratio of two
rational coordinates. Thus neither eigenline contains a nonzero rational or
integral form.

This statement does not say that `J` changes no two-dimensional period or
Euclidean area. For example, with `x=e0` and `y=e1+e2`,

```text
Omega_1(x,y)=1,
(P Omega_1)(x,y)=0.
```

It says exactly that the four-dimensional Pfaffian and unimodularity are
preserved. A Pfaffian-null eigenform is still a nonzero rank-two alternating
2-form. The Pell hyperbola describes unimodular members of this CM pencil, not
all integral symplectic forms. “Unique hyperbolic sector” means the unique
rational `q`-primary component, not a physical polarization.

## Field 2: accepted code and exactness contract

The accepted code is exactly `verify.py` in this directory as committed in
the immutable pin. It uses only Python's standard library, integer arithmetic,
`Fraction`, and the exact quadratic ring `Q(phi)`. It uses no floating-point
literal or operation, numerical eigenvalue, tolerance, random input, clock,
network, subprocess, external CAS, bounded kernel search, or architecture
branch.

The verifier must construct `P` from `M_J` and the six elementary alternating
forms rather than trust the displayed matrix. It must compute the
characteristic polynomial, kernels, determinant, seam action, Sylvester
resultant, Bezout identity, projector, Pfaffian identity, and quadratic-field
eigenlines exactly. Explicit kernel formulas and rank identities audit the
universal proof; a bounded search is not admissible evidence.

## Field 3: carrier and data contract

The only carrier is the fixed L1 lattice `E_Z=Alt^2(Z^4)` and its rational and
real scalar extensions. The only admitted data are the displayed `M_J`, the
fixed coordinate order, the public CM basis, and exact consequences computed
from them. No empirical, metrological, observational, fitted, decoded, or
external data enter.

## Field 4: systematics and negative controls

The systematic risks frozen before execution are coordinate transposition,
confusing covariant forms with bivectors, inferring index five from resultant
twenty-five, mistaking saturation for a canonical primary direct sum,
silently replacing Pfaffian invariance by invariance of every two-period,
calling a rank-two null form zero, and importing the toral entropy area ratio
as action.

The exact negative controls are:

1. the displayed period witness changes from one to zero, so the verifier
   must reject the overstatement that every two-period is invariant;
2. the integral numerator of `E_H` has content one, so deleting its factor
   `1/5` cannot remain a projector;
3. `ell P=+ell mod 5` is false while `ell P=-ell mod 5` is true;
4. the two real eigenforms are nonzero despite Pfaffian zero;
5. source inspection rejects float or complex literals and any import of a
   numerical, random, network, clock, or process library.

## Field 5: decision thresholds and falsifiers

The intended result is `CONFIRMED` exactly when every frozen theorem identity
and every negative control passes. There is no tolerance and no discretionary
borderline. Any failed theorem item fires the corresponding falsifier:

```text
F1  M_J, det M_J, the constructed pullback matrix, or exact Pfaffian
    covariance fails.
F2  The characteristic polynomial, irreducibility certificate, primary
    kernels, rational direct sum, or exact order-ten restriction fails.
F3  Either displayed full integral intersection or saturation claim fails.
F4  The six-column determinant is not +/-5, the quotient is not cyclic of
    order five, or its P-action is not -1.
F5  The Bezout identity, resultant 25, ramified mod-five identities,
    projector identities, or smallest common denominator five fails.
F6  Either displayed real eigenline is not a P-eigenline, is not
    Pfaffian-null, or its nonzero form does not have rank two.
F7  A negative scope or exact-source control fails.
STOP authority drift, collision, execution or import before the public pin,
     post-pin verifier mutation, hidden floating point, incomplete or inexact
     rank logic, bounded search substituted for proof, architecture-dependent
     stdout, nonempty stderr, or expansion beyond L1.
```

A fired result is preserved under this identifier. No equation, basis,
factor, lattice, threshold, or interpretation may move after the pin.

## Field 6: action and interpretation layer

This is L1 mathematics only. It makes no claim about action, `h`, `hbar`,
phase, `2 pi`, SI normalization, a decoder field, real-place selection,
stable/unstable time orientation, entropy production, an L2 physical area,
or any L3-L6 readout.

The programmatic choice is frozen only as a nonclaim boundary. If a later
action bridge is opened, the chosen research branch must start from the
primitive integral symplectic form `Omega_1` and a separately justified unit
period. That period is not identified with physical `h` here. The exact
factor `phi^2` remains the already-owned archimedean unstable area ratio and
entropy characterization; its area-ratio route is excluded as an action
carrier in this branch. Any physical identification is `STOP` until an L2
carrier, cycle or current, polarization, normalization, phase law,
real-place treatment, time orientation, and typed layer bridge are
independently frozen. Hurwitz is not an alternate or parallel justification.

## Frozen verifier gates and stdout schema

The formal verifier has exactly twelve ordered gates:

```text
G01 pullback_and_pfaffian_covariance
G02 characteristic_primary_factorization
G03 rational_primary_decomposition
G04 cm_pencil_identification
G05 hyperbolic_integral_saturation
G06 circular_integral_saturation
G07 index_five_cyclic_seam
G08 seam_action_minus_one
G09 resultant_and_ramification
G10 exact_primary_projector_denominator_five
G11 null_rank_two_real_eigenforms
G12 scope_and_exact_source_firewalls
```

Successful stdout must contain the probe identifier, one `PASS` line for
each gate in this order, and finish with

```text
DECISION CM-ALTERNATING-PRIMARY-LATTICE-SEAM-CONFIRMED
```

The exact bytes are recorded in `EXPECTED.txt` only after the first formal
post-pin execution.

## Formal order

1. Commit and push only this `PREREG.md` and the accepted `verify.py` together
   from the exact v68 base before `verify.py` is ever imported or executed.
2. Read both pinned blobs back from the public remote byte for byte. Record
   the pin commit, blob identities, SHA-256 hashes, byte counts, LF-only line
   endings, and final LF.
3. Execute the pinned verifier formally exactly once on the local Linux leg
   with exit zero, empty stderr, and deterministic stdout. Preserve a fired
   falsifier without moving a threshold.
4. Add only `EXPECTED.txt`, `RUN.md`, and `RESULT.md` after that execution.
5. Open one probe-only pull request linked to issue 625. Require byte-identical
   x86_64 and aarch64 output and aggregate `check` before merge.
6. Never amend, rebase, squash, force-push, rename, resume, or reuse this probe
   after its preregistration pin. A Canon fold, if earned, is a separate
   transaction.
