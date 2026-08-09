# C-J-DEDEKIND-WEIL-ROAD-N

```text
STATUS:       NON-CANONICAL INCUBATION NOTE
AUTHORITY:    none
PUBLIC BASIS: Public Canon v39, mathorn1973/twist-j main
ISSUE LOCK:   #310
LAYER:        analytic/number-theoretic roadmap only; no L1-L6 lift claimed
COMPUTATION:  none
PROMOTION:    none
```

This note preserves one falsification-first roadmap. It creates no public
claim, no Registry row, no status change, no verifier permission, and no Canon
fold. Candidate names below are working labels only.

The purpose is to separate three different questions that are easy to conflate:

1. whether TWIST-J can construct the completed Dedekind factor natively;
2. whether TWIST-J can realize the global explicit formula or Weil form;
3. whether the resulting classical Weil form is positive.

The first two test TWIST-J. The third tests the zeros themselves.

## 1. Public basis and collision boundary

[PUBLIC AUTHORITY] At the time this note was claimed, `STATUS.md` declared:

```text
STATE:          ACTIVE
CANON:          Public Canon v39
AUTHORITY:      mathorn1973/twist-j main
TAG:            canon-v39
CONTENT_COMMIT: ab17b10412d03bf1cd69791fe22c66252502b2d4
CANON_SHA256:   698df2212f0bc782de2fb50ff04fb4026d1e276743d6fae7f10607cca770b556
CANON_BYTES:    187370
main HEAD:      6e5b796c52772afd1fe5e60048c3691b002a9302
```

The declared tag and content commit are ancestors of this `main`. The Canon
hash is the one recorded in `canon/SHA256SUMS`.

This note must not absorb or silently rewrite the following existing public
scopes.

[PUBLIC T] `PENTAGON-NORMALIZATION` already proves, on its exact registered
scope,

```text
P_0(s) = (5^(1-s) - 1) zeta(s)
```

on `Re(s)>1`, and after the named classical meromorphic continuation and
standard imported completion it records `Z_J(s)=zeta(s)` and `xi_J(s)=xi(s)`.
It explicitly does not supply a Weil realization, positivity theorem,
J-native carrier, or RH result.

[PUBLIC T/F] The zero lane already contains exact negative carrier results,
including the toral Haar no-go, the compact-boundary Hilbert-Schmidt no-go, and
the lambda-scaling single-unitary no-go. Their excluded classes remain exactly
their registered classes.

[PUBLIC T] `LAMBDA-COCYCLE-GRID-EQUIVALENCE` already identifies the exact
lambda-adic point spectrum and proves its registered equivalence between a
cocycle vector and RH plus the Cayley-angle grid condition.

[PUBLIC H] `LAMBDA-COCYCLE-ANGLES` remains the stronger cocycle-vector
hypothesis. Its falsifier already fires if RH is disproved or if the stronger
grid condition fails.

[PUBLIC O] Public Canon v39 explicitly states `RH remains O`.

[PUBLIC O] `QUANT-SUBSTRATE` already owns the physical `archimedean wall`
terminology for the Larmor and Schwinger lane. The present note is a
number-theoretic roadmap and does not reuse that ownership.

[PROCESS] Issue #309 and branch `release/canon-v40` own only the later
`J-HARMONIC-SEAM` Canon fold. This note is independent of that release surface.

## 2. Harmonic-seam mirror, and the exact boundary of that mirror

[NON-CANONICAL MATHEMATICAL NOTE] Define the branch-free logarithmic defect

```text
Delta(w,x) = log |1 - w x|.
```

The harmonic seam and the critical-line geometry are two cuts of the same
function:

```text
seam phase fiber:
    Delta(psi,x) = 0,  x in mu_10

zero geometry:
    Delta(1/rho,1) = 0  iff  Re(rho) = 1/2
```

The second identity is elementary:

```text
|1 - 1/rho| = 1
  iff |rho - 1| = |rho|
  iff Re(rho) = 1/2.
```

This is a common logarithmic geometry. It is not an inference from the finite
seam classification to the zeros of zeta. It supplies no L1-to-L6 gate and no
RH evidence.

[NON-CANONICAL MATHEMATICAL NOTE] Functional-equation pairing has a second
exact mirror. Put

```text
z_rho = 1 - 1/rho.
```

Then

```text
z_(1-rho) = 1/z_rho.
```

For a full nondegenerate quartet
`{rho,bar(rho),1-rho,1-bar(rho)}`, pairing conjugates first removes the branch
ambiguity in the real part and the reciprocal pair cancels the logarithmic
moduli. Without RH this is global reciprocal cancellation. On RH each
individual factor is already unimodular. This distinction is motivational
only here.

## 3. Candidate O1: J-DEDEKIND-COMPLETION

[NON-CANONICAL CANDIDATE O] The first genuinely program-specific target is not
`zeta(s)` itself. `PENTAGON-NORMALIZATION [T]` already reaches that object. The
target is to stop importing the archimedean completion.

For

```text
K = Q(zeta_5),
r_1 = 0,
r_2 = 2,
D_K = 125 = 5^3,
```

freeze a completion convention before any future formal work. One convenient
working normalization is

```text
Lambda_K^*(s)
  = 125^(s/2) (2 pi)^(-2s) Gamma(s)^2 zeta_K(s).
```

This differs from the common `Gamma_C(s)=2(2 pi)^(-s)Gamma(s)` convention only
by an `s`-independent positive factor when squared. A future claim must freeze
which convention is used. A notation-only factor-of-two mismatch is not a
scientific falsifier.

[PUBLIC T INPUT] The discriminant is not a foreign fitted constant. The public
arithmetic already singles out `125=5^3` for `Q(zeta_5)` in its declared
number-field scopes. A future construction may use a theorem-grade public
derivation of this discriminant, but may not smuggle in an unregistered
normalization.

### Required content of a genuine O1 construction

[NON-CANONICAL CANDIDATE O] A future `J-DEDEKIND-COMPLETION` result must derive
an object `G_J(s)` from named J-native data without taking `Gamma` or the
completed zeta function as a primitive, and then prove exact equality with the
frozen classical target:

```text
G_J(s) = 125^(s/2) (2 pi)^(-2s) Gamma(s)^2
```

in the chosen normalization.

Merely defining the right-hand side and renaming it `G_J` is circular and earns
nothing.

A serious scope must also name:

```text
carrier or source object
allowed operations
domain in s
analytic continuation rule if needed
normalization convention
functional-equation transform
comparison equality
completeness of the construction class, if uniqueness is claimed
```

### O1 failure surface

[NON-CANONICAL FALSIFICATION DESIGN] O1 can fail while RH and every relevant
GRH statement remain true. Examples of fatal outcomes include:

```text
wrong gamma multiplicity
wrong discriminant exponent
wrong pi normalization after convention is frozen
failure of the s <-> 1-s transformation
an extra free dimensionless parameter
construction depends on importing Gamma in the step claimed to derive Gamma
```

This is the first branch of this roadmap where TWIST-J risks something of its
own independently of the location of zeta zeros.

No `archimedean Frobenius` is asserted. Such language may be motivation only.
An actual Frobenius-like intertwining theorem would be a separate claim.

## 4. Candidate O2a: J-WEIL-FORM-REALIZATION

[NON-CANONICAL CANDIDATE O] Even a correct completion is not a proof of RH or
GRH. The next program-specific problem is to realize the global explicit
formula or Weil quadratic form from J-native data.

A clean future target has the schematic form

```text
Q_J(f) = Q_Weil,K(f)
```

for every `f` in one complete frozen admissible test class.

The scope must not be selected after seeing signs of the form. It must freeze
at least:

```text
test-function space
Fourier/Mellin convention
finite-place contribution
archimedean contribution
normalization of the completed zeta function
pairing or involution used in the quadratic form
equality notion
domain/completeness statement
```

[NON-CANONICAL FALSIFICATION DESIGN] A counterexample to the equality above can
kill the J-native realization while GRH_K remains true. Thus O2a, like O1, is a
TWIST-J risk rather than a disguised zero hypothesis.

[NON-CANONICAL CONDITIONAL CONSEQUENCE] If a future theorem proves both

```text
Q_J(f) = Q_Weil,K(f)
```

on the full admissible class and a manifestly positive representation such as

```text
Q_J(f) = ||T_J f||^2,
```

then the classical positivity conclusion follows. Neither equality is asserted
by this note.

## 5. Classical target O2b: Weil positivity for zeta_K

[CLASSICAL TARGET, NOT A TWIST-J RESULT] At the correct full test-function
scope, Weil positivity for the completed `zeta_K` is not an intermediate step
toward GRH_K. It is an equivalent formulation of the zero statement.

For the cyclotomic field

```text
K = Q(zeta_5),
```

the Dedekind zeta factors as

```text
zeta_K(s)
  = zeta(s) L(s,chi_5) L(s,chi) L(s,bar(chi)).
```

Therefore GRH for `zeta_K` contains:

```text
RH for zeta(s),
critical-line GRH for the real nonprincipal character chi_5 mod 5,
critical-line GRH for the complex character pair chi, bar(chi).
```

The complex conjugate pair has related zero sets, so these are not four
independent conjectures, but the Dedekind statement is strictly broader than
RH for `zeta` alone.

[BOUNDARY] O2b tests the zeros themselves. Calling O2b a progress theorem would
be status inflation. The progress question is whether O2a can realize the
classical form from J-native structure.

## 6. Negative routes

[CLASSICAL ROUTE] A certified Robin counterexample for an integer `n>5040`
would disprove RH for the Riemann-zeta factor. Through that classical
implication it would also satisfy the already registered
`LAMBDA-COCYCLE-ANGLES [H]` condition `fires if RH is disproved`. No new claim
identifier is needed merely to receive such a witness. A public evidence and
status-change fold would still be required.

[CLASSICAL ROUTE] A negative value of the correctly normalized Weil form on an
admissible test function would disprove GRH_K directly.

[CLASSICAL ROUTE] An off-critical zero of one nonprincipal Dirichlet factor
would disprove the corresponding GRH factor even if RH for `zeta(s)` survived.

Thus Robin is a falsifier for only one factor of the full Dedekind target.

## 7. Risk taxonomy

```text
VALUES
  [PUBLIC T] exact s=1 and s=2 identities already exist at their scopes
  [PUBLIC T] PENTAGON-NORMALIZATION already normalizes to zeta(s)
  [BOUNDARY] harmonic seam gives no inference to zeta zeros

ZERO LANE
  [PUBLIC T/F/H] already nonempty:
      exact normalization
      no-go carriers
      grid equivalence
      cocycle-vector hypothesis
  [PUBLIC O] RH itself remains O

O1  J-DEDEKIND-COMPLETION
  [NON-CANONICAL CANDIDATE O]
  derive rather than import the completed Dedekind factor
  failure may kill the TWIST-J route with RH/GRH untouched

O2a J-WEIL-FORM-REALIZATION
  [NON-CANONICAL CANDIDATE O]
  derive the global explicit formula / Weil form from J-native data
  failure may kill the TWIST-J route with GRH untouched

O2b WEIL POSITIVITY FOR zeta_K
  [CLASSICAL ZERO WALL]
  equivalent to GRH_K at the correct complete scope
  not an intermediate TWIST-J theorem

NEGATIVE ROUTES
  Robin witness         -> kills the zeta/RH factor
  negative Weil form    -> kills GRH_K
  off-line Dirichlet zero -> kills its nonprincipal GRH factor
```

The central asymmetry is therefore:

```text
O1 and O2a test TWIST-J.
O2b tests the zeros.
```

## 8. P-J-HARMONIC-SEAM-1 provenance guard

[PUBLIC PROBE IDENTITY] The only public citable harmonic-seam pin is:

```text
pin_commit:        61aa12c2b0e9705c3c0d9fb91fc4cfe6c80697ff
PREREG sha256:     751807cb6a84d2e9f06dbf2995d6f9395b57d1a8ea4e285f0736dc27850565f4
PREREG bytes:      9363
verifier sha256:   9aa0b47f91c8e57c421b900d4578d159537715cca773c404209c20fd1ec71a40
verifier bytes:    9079
stdout sha256:     8198dc9c8c7dcc188d04635ec4c365e86dcb4524e28b347f2b2d1da1c943118d
stderr:            empty
probe merge:       6e5b796c52772afd1fe5e60048c3691b002a9302
```

[NON-CANONICAL PROVENANCE ONLY] Earlier preparation material reported the
following pre-pin draft identities:

```text
PREREG draft sha256:
  40c44a07b5bb8f2e6b81c7383bafd52dc44cf1fcf6034adbccfc94cd24c3d8d0
PREREG draft bytes:
  9803

verify.py draft sha256:
  d6f8f369957d07ad07f578210a88e32221aab0c3ae0dca0f0a62ed7a81342967
verify.py draft bytes:
  14055
```

These draft identities are not repository authority, not alternative pins, and
not evidence. The verifier changed materially before the public pin. This was
legal because `POLICY.md` permits rewriting, compilation, and static checks
before pinning. After pinning, the sealed bytes above are the only public probe
identity.

The draft-to-pin byte reduction is provenance, not a scientific result and not
a defect by itself. Any seam citation must use the sealed pin, not the draft
hashes.

## 9. Promotion boundary

This note authorizes no computation and no formal gate.

A future action must branch by content:

```text
J-DEDEKIND-COMPLETION
  -> separate claim issue
  -> complete equation/source/systematics/failure/action-layer scope
  -> formal protocol appropriate to the proposed proof or computation

J-WEIL-FORM-REALIZATION
  -> separate claim issue
  -> frozen test-function class and equality before execution
  -> no target leakage from observed sign behavior

Weil positivity / GRH_K
  -> do not register as progress merely by renaming the classical equivalence
  -> a TWIST-J claim must add a genuine construction or reduction
```

No future summary may say that the harmonic seam, this note, O1, or O2a proves
or supports RH beyond the exact public scopes already registered.
