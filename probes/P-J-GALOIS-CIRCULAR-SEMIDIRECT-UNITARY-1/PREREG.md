# P-J-GALOIS-CIRCULAR-SEMIDIRECT-UNITARY-1 preregistration

Status: **FROZEN TARGET / RESULT-EXPOSED / PROOF-FIRST / L1 ONLY / PUBLIC
STATUS NONE.**

This preregistration owns one exact algebraic question.  It asks what the
public Galois automorphism does after the public `J` pullback is passed to the
actual integral circular quotient of the alternating-form carrier.  It also
freezes the complete character of the resulting representation.

The target values are exposed before execution.  A match confirms the two
claims below at candidate-T/L1 because the universal conclusions are carried
by the proofs in this file; the program audits their finite exact premises.
A mismatch fires the affected claim.  It is never tuned away.

```text
probe:           P-J-GALOIS-CIRCULAR-SEMIDIRECT-UNITARY-1
branch:          probe/P-J-GALOIS-CIRCULAR-SEMIDIRECT-UNITARY-1
path:            probes/P-J-GALOIS-CIRCULAR-SEMIDIRECT-UNITARY-1/
claim lock:      https://github.com/mathorn1973/twist-j/issues/797
owner:           A. M. Thorn / delegated session 2026-09-04
mode:            RESULT-EXPOSED / PROOF-FIRST
action layer:    L1 exact algebra
public basis:    Public Canon v75
base main:       a86dbf4a12a71422463d397733ca08ae8f117963
tag:             canon-v75
tag target:      c4f00e1d9c89f503d913224dc3c09dc760dcec9d
content commit:  e32e85ed7297d4320df5b345e4488d78323d550c
canon sha256:    44130160a3ce29bfcdc757e255d2d1c25a010b22911edfe66cf6b132be081fbe
canon bytes:     399513
formal runs:     0 before the atomic pin
public status:   NONE
```

## 1. Collision and authority lock

Before the claim lock was opened, the public issue index, repository tree,
Registry, object-lock surface, pull requests, and all remote heads were
searched for the exact probe and claim names and for the combined Galois,
circular, semidirect, and unitary target.  No collision was found.  The
declared v75 content commit and tag are ancestors of the stated `main`; the
Canon hash and byte count match `STATUS.md`; the latest `main` policy run at
the base commit passed.

The predecessor `P-J-FIBONACCI-BRAID-1` established the public circular
primary lattice as the rank-one module on which the pullback acts by
`delta_10=1-J`.  It did not include a Galois operator.  This probe is a fresh
successor, not a resumption or amendment.

## 2. Frozen claims and decision

```text
claim A: J-GALOIS-CIRCULAR-QUOTIENT-SEMIDIRECT-UNITARY
claim B: J-GALOIS-CIRCULAR-ODD-CHARACTER
```

Claim A is confirmed exactly when gates G01--G13 all pass.  Claim B is
confirmed exactly when gates G01--G11 and G14--G18 all pass.  Otherwise the
affected claim is `FIRED`.  `OVERALL PASS` requires both claims.

No partial numerical tolerance exists.  All equalities are exact.

## 3. Public inputs and notation

Let

```text
K   = Q(zeta),              Phi_5(zeta)=0,
O_K = Z[zeta],              basis (1,zeta,zeta^2,zeta^3),
J   = 1+zeta^2,
delta_10 = 1-J = -zeta^2.
```

The subscript on `delta_10` is mandatory.  The public real-different theorem
already uses an unadorned delta for `sqrt(5)`.

On `V_Z=O_K`, multiplication by `J` is reconstructed as

```text
M_J = [[1,0,-1,1],
       [0,1,-1,0],
       [1,0, 0,0],
       [0,1,-1,1]].
```

The Galois source is not denoted by a bare `gamma_2`, which also names the
second Stieltjes constant elsewhere.  Freeze

```text
gamma_2^Gal(zeta)=zeta^2,
U_2 = matrix of gamma_2^Gal on V_Z.
```

The verifier must derive `U_2` from this equation rather than enter its matrix
as an accepted target.

Let

```text
E_Z = Alt^2(V_Z^*)
```

in the fixed upper-triangular coordinate order

```text
(01,02,03,12,13,23).
```

Both operators are the covariant pullbacks

```text
P(W)   = M_J^T W M_J,
S_E(W) = U_2^T W U_2.
```

This is the form carrier, not the bivector convention.  Pullback order is
contravariant and is a load-bearing systematic.

The public primary bases are frozen as

```text
Omega_1 = ( 1, 0, 0, 1, 0, 1),
Omega_2 = ( 0, 1,-1, 0, 1, 0),

c_1 = (-1, 0, 1, 0, 0, 0),
c_2 = ( 0,-1, 0, 1, 0, 0),
c_3 = ( 0,-1, 0, 0, 1, 0),
c_4 = (-1, 0, 0, 0, 0, 1).
```

Thus

```text
H_Z = Z Omega_1 + Z Omega_2,
C_Z = Z c_1 + Z c_2 + Z c_3 + Z c_4.
```

The main integral carrier of this probe is the quotient

```text
L = E_Z/H_Z,
```

not `C_Z`.  Freeze its basis as

```text
(bar e_03, bar e_12, bar e_13, bar e_23).
```

The quotient relations are

```text
bar e_01 = -bar e_12-bar e_23,
bar e_02 =  bar e_03-bar e_13.
```

They give a displayed integral quotient map with kernel exactly `H_Z` and
prove that `L` is free of rank four.

## 4. Claim A target: quotient, seam, group, and form

### 4.1 Descent and the index-five seam

The verifier must derive from the ambient matrices that both `P` and `S_E`
preserve `H_Z` and `C_Z`.  They therefore descend to `L` and restrict to the
public circular primary lattice.

Write their quotient matrices in the frozen basis as `bar P` and `bar S`.
The expected values are comparisons only:

```text
bar P = [[ 0, 1, 0, 0],
         [ 0, 1, 0,-1],
         [ 0,-1, 1, 1],
         [-1, 1,-1,-1]],

bar S = [[-1, 0, 0, 0],
         [ 0, 1, 0,-1],
         [ 1,-1, 0, 0],
         [ 0, 1, 1, 0]].
```

The natural injection of `C_Z` into `L` must have determinant of absolute
value five and must give the exact sequence

```text
0 -> C_Z -> L -> Z/5 -> 0.
```

The two induced seam actions are frozen:

```text
bar P on L/C_Z = -1 mod 5,
bar S on L/C_Z =  2 mod 5.
```

This index-five seam is part of the target, not a nuisance to be rationalized
away.  In particular, no integral equality `C_Z=L` and no integral
retraction is asserted.

### 4.2 Fractional-ideal model and semilinearity

Retain the predecessor's integral isomorphism

```text
Psi: O_K -> C_Z,
Psi(delta_10^n)=P^n c_2,       n=0,1,2,3.
```

After the natural injection `C_Z -> L`, the unique rational extension of
`Psi^-1` identifies `L` with the fractional ideal

```text
I = O_K + Z*(2+delta_10+delta_10^2+2 delta_10^3)/5
  = (1+delta_10)^(-1) O_K.
```

The verifier must compare lattices, not merely their index.  One frozen
`Z`-basis of `I` is

```text
1,
delta_10,
delta_10^3,
(2+delta_10+delta_10^2+2 delta_10^3)/5.
```

In this model the target actions are

```text
bar P = multiplication by delta_10,
bar S = gamma_3^Gal followed by multiplication by delta_10^4,
gamma_3^Gal=(gamma_2^Gal)^(-1).
```

Consequently

```text
bar S(a v)=gamma_3^Gal(a) bar S(v),
bar S bar P bar S^(-1)=bar P^3,
bar S bar P != bar P bar S.
```

The scalar factor `delta_10^4`, the inverse Galois exponent, and the direction
of conjugation are all frozen.  The pure transported map
`Psi gamma_2^Gal Psi^(-1)` is a different operator: it is not silently
substituted after inspection.

### 4.3 Exact finite group

The complete target presentation is

```text
bar P^10 = I,
bar P^5  = -I,
bar S^4  = I,
bar S bar P bar S^(-1) = bar P^3.
```

All normal forms

```text
bar P^a bar S^b,       a in Z/10, b in Z/4,
```

must be distinct.  Hence

```text
G_C=<bar P,bar S> ~= C_10 semidirect_3 C_4,
|G_C|=40.
```

The central involution is `bar P^5=-I`.  With `D=bar P^6`,

```text
<D,bar S> ~= C_5 semidirect_3 C_4 ~= AGL_1(F_5),
G_C ~= C_2 x AGL_1(F_5).
```

The linear representation is faithful.  Its projective kernel is exactly

```text
{I,-I}={I,bar P^5},
```

so the projective image has order twenty.  The phrase "forty physically
distinct gates" is not licensed.

### 4.4 Explicit common positive form

Mere existence of some positive invariant form would be automatic for a
finite group and is not the frozen target.  In the displayed quotient basis
freeze

```text
G_L = [[2, 0,1, 0],
       [0, 2,0,-1],
       [1, 0,2, 1],
       [0,-1,1, 2]].
```

The required exact identities are

```text
leading principal minors(G_L) = (2,4,6,5),
bar P^T G_L bar P = G_L,
bar S^T G_L bar S = G_L.
```

The minors prove positive definiteness over the reals.  Only after scalar
restriction and complexification is the declared Hermitian form

```text
<v,w>_L = conjugate(v)^T G_L w.
```

This proves simultaneous unitarizability of the displayed representation.  It
does not select Born normalization, states, effects, or probabilities.

## 5. Claim B target: odd induced character

The characteristic polynomial of `bar P` must be

```text
Phi_10(x)=x^4-x^3+x^2-x+1.
```

Thus over `C` it has four distinct eigenlines with eigenvalues

```text
delta_10^k,       k in {1,3,7,9}.
```

The exponent-three normalizer relation acts transitively on these four
indices.  Dually, `bar S` sends the eigenline labelled by `k` to the line
labelled by `7k mod 10`; the two oriented cycles are inverse and have the same
four-element orbit.  Since every invariant subspace of an operator with simple spectrum
is a sum of eigenlines, a subspace invariant under both generators contains
either none or all four.  The representation is irreducible.

In the same spectral basis `bar S` cyclically permutes the four eigenlines,
up to nonzero scalar entries.  Therefore every group element is monomial in
that basis.  This is a transitive transporter of phase-character lines; it is
not a Hadamard-like creator of superpositions.

Freeze the full character on all forty normal forms:

```text
chi(bar P^a bar S^b)=0,                         b=1,2,3,

(chi(bar P^a))_(a=0..9)
  = (4,1,-1,1,-1,-4,-1,1,-1,1).
```

Equivalently, for `b=0`,

```text
chi(bar P^a)=sum_(k in {1,3,7,9}) delta_10^(ka)=c_10(a).
```

The frozen certificates are

```text
(1/40) sum_(g in G_C) |chi(g)|^2 = 1,
chi(bar P^5)=-4,
ker representation = {I}.
```

They identify the representation as the faithful odd-orbit constituent

```text
Ind_(C_10)^(G_C)(lambda_1),
lambda_1(bar P)=delta_10.
```

The complete complex irreducible census follows from the multiplication-by-
three orbits on `Z/10`:

```text
{0}, {5}, {1,3,7,9}, {2,4,6,8}.
```

The first two orbits each have stabilizer `C_4` and give four linear
extensions.  Each free four-element orbit gives one induced representation of
dimension four.  Hence the complete census over `C` is

```text
eight 1-dimensional irreducibles,
two   4-dimensional irreducibles,
8*1^2+2*4^2=40.
```

The even-orbit constituent has `chi(bar P^5)=+4` and kernel
`<bar P^5>`.  This distinguishes it from the frozen faithful constituent.

The character match and irreducibility are two readings of the same exact
certificate once the group presentation is fixed; they are not reported as
independent statistical confirmations.

## 6. Proof-first implications

The following universal steps are independent of exhaustive search.

1. The displayed quotient relations make `L` free of rank four with kernel
   exactly `H_Z`.  Preservation of `H_Z` gives unique descended operators.
2. The presentation relations rewrite every word to one of forty normal
   forms.  Their exact distinctness proves the presentation and group order.
3. `bar P^5=-I` supplies a central `C_2`; `bar P^6` supplies the normal
   `C_5`; the intersection is trivial, proving the direct-product statement.
4. The two Gram identities and Sylvester minors prove one common positive
   Hermitian unitarization after complexification.
5. Simple `bar P` spectrum plus transitivity of the normalizer on its
   eigenlines proves irreducibility.
6. The exact character norm one independently certifies the same
   irreducibility in finite-group character theory; the value at `bar P^5`
   selects the odd constituent.
7. The four character-index orbits and their stabilizers exhaust the dual of
   the abelian normal subgroup `C_10`; little-group induction gives the stated
   complete irreducible census and the sum of squares exhausts `|G_C|`.

The verifier audits every finite premise used above.  It is not a brute-force
replacement for these arguments.

## 7. Nine gate families and exact falsifiers

The program reports eighteen subgates grouped as follows.

1. **SOURCE/CARRIER (G01--G04).** Reconstruct the cyclotomic field,
   `M_J`, `U_2`, both ambient pullbacks, both primary lattices, and the free
   quotient.  A mismatch is a source or carrier falsifier.
2. **QUOTIENT/SEAM (G05--G07).** Derive the quotient matrices, the
   invariant index-five sublattice, its fractional-ideal model, and seam
   scalars `-1` and `2`.  Any mismatch fires claims A and B.
3. **CONTRAVARIANCE (G08).** Derive exponent three and the exact
   `delta_10^4 gamma_3^Gal` cocycle.  Exponent seven for this frozen ambient
   pullback fires claims A and B; it is not an allowed orientation swap.
4. **TYPE (G09).** Verify semilinearity and noncommutation.  Scalar
   `O_K`-linearity fires claims A and B.
5. **GROUP (G10--G11).** Verify orders, relations, forty normal forms,
   direct-product structure, and linear/projective kernels.  Any mismatch
   fires claims A and B.
6. **POSITIVE FORM (G12--G13).** Verify the explicit form, all Sylvester
   minors, and both invariances.  Any mismatch fires claim A.
7. **SPECTRAL/MONOMIAL (G14--G15).** Verify `Phi_10`, four distinct
   character indices, their transitive cycle, and the monomial implication.
   Any mismatch fires claim B.
8. **CHARACTER (G16--G17).** Verify all forty character values, norm one,
   faithfulness, induction data, and the complete irreducible census.  Any
   mismatch fires claim B.
9. **FINITE BOUNDARY (G18).** Verify closure is finite and every normal
   form normalizes the spectral-line system.  Any density, universality, or
   superposition assertion fails the scope gate rather than becoming a
   result.

Authority drift, collision, execution or import of the accepted verifier
before its public pin, post-pin mutation of `PREREG.md` or `verify.py`,
nonzero process exit, nonempty stderr, nondeterminism, transcript or hash
mismatch, architecture mismatch, forbidden dependency, and security or
metadata defects are integrity `STOP`, not scientific outcomes.
The verifier buffers its complete transcript and emits it only after all
eighteen gates and both claim decisions exist.  Any partial stdout from an
integrity `STOP` is invalid and must be quarantined rather than published.

## 8. Six required preregistration fields

1. **Equation.** Sections 3--5 freeze every carrier, quotient, pullback,
   group, form, spectral, character, and induction equation.
2. **Code.** One newly authored deterministic `verify.py`; Python standard
   library only; exact integers, `fractions.Fraction`, and exact
   `Q(zeta_5)` arithmetic.  No file input, network, subprocess, randomness,
   clock, dynamic import, `eval`, `exec`, float, or builtin complex
   arithmetic.  Static parsing and compilation are allowed before pin;
   importing or executing the verifier is forbidden.
3. **Carrier/data.** Only the displayed integral lattices, exact matrices
   reconstructed from them, and finite group and character tables.  There is
   no empirical or external dataset.
4. **Systematics.** Basis order, covariant form pullback, contravariant
   Galois action, quotient versus sublattice, seam marking, exponents three
   versus seven, linear versus projective equality, and Hermitian
   complexification are frozen.
5. **Failure threshold.** Any exact scientific mismatch fires the named
   claim.  Integrity defects stop the probe and never become scientific
   results.
6. **Layer.** L1 exact algebra only.  There is no cross-layer lift.

## 9. Dependencies and novelty boundary

`REQUIRES`:

- `J-STEP [T]`;
- `J-TENTH-ROOT [T]`;
- `J-GOLDEN-BRIDGE [T]`;
- `AFFINE-READING-DEGREE-CENSUS [T]`;
- `AFFINE-QUADRATIC-FORM-UNIQUENESS [T]`;
- `CM-ALTERNATING-PENCIL [T]`;
- `CM-ALTERNATING-PRIMARY-LATTICE-SEAM [T]`;
- `DEF-ACTION-LAYERS`.

The Canon already contains

```text
<D_J,gamma_2^Gal> ~= AGL_1(F_5)
```

of order twenty, its absolute irreducibility, and its positive invariant
`q_+`.  This probe does not claim the first noncommuting finite system from
`J` and Galois.  Its possible new content is the descent to the actual
circular quotient, preservation of the index-five circular sublattice and
seam, the central sign extension, and the explicit odd induced character.

`QPAIR-MIXED-C4-NORMALIZES-2I [F]` concerns a different marked `K^2`
carrier and is not contradicted or retested here.

## 10. Firewalls

This probe asserts no Born rule, probability, amplitude recombination,
preparation, measurement, effect, apparatus, physical qudit, tensor-product
composition, Pauli or Clifford normalizer, `T` gate, Hamiltonian, continuous
one-parameter group, space, time, anyon, topological protection, quantum
advantage, universality, density, or L2--L6 lift.

The following distinctions are mandatory:

- semilinearity on a rank-one `Z[delta_10]` module is not complex linearity
  on one selected embedding;
- complex linearity appears only after restriction of scalars and
  complexification to a four-dimensional carrier;
- monomial transport of eigenlines is not superposition mixing or physical
  interference;
- a faithful forty-element linear image has only a twenty-element projective
  image here;
- a positive invariant Hermitian form is not a Born pairing or its physical
  normalization;
- an L1 commutator is not physical space.

Public Canon, Registry, Frontier, dependency and gate ledgers, workflows,
releases, and `STATUS.md` remain unchanged.

## 11. Formal order

1. Commit and push only this file and the accepted, unexecuted `verify.py`.
2. Read both remote blobs back; record commit, hashes, byte counts, line
   endings, and final LF on issue #797.
3. Only then execute the pinned verifier exactly once locally from the
   repository root.
4. Save exact stdout as `EXPECTED.txt`; require empty stderr and exit zero;
   record the neutral environment and hashes in `RUN.md`.
5. Add `RESULT.md` without changing either pinned file.  A fired falsifier is
   published, not hidden.
6. Open one probe-only pull request and require byte-identical GitHub-hosted
   x86_64 and aarch64 replay, aggregate policy success, and manual security
   review.
7. Never amend, rebase, squash, force-push, resume, rename, or reuse this
   probe after the pin.
