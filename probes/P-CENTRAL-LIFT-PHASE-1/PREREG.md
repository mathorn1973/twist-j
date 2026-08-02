# P-CENTRAL-LIFT-PHASE-1

Preregistration for the public probe P-CENTRAL-LIFT-PHASE-1: the
projective Hermitian action of the J step, the central phase retained by
the normalized symmetric-square action, and the exact unit-scalar phase
image in Q(zeta_5).

Owner: A. M. Thorn / mathorn1973, coordinated in the current Codex task.
Claim issue: #251, opened before this branch, path, pin, and any formal
execution. Base: public `main` commit
`60228fa5784f10df69ea6e3d96872b6652909628` under Public Canon v31
(STATE ACTIVE, tag `canon-v31`, content commit
`7c8b57aac8df8460cb0ef928659fb07b2444f7ff`, Canon SHA-256
`242fff6a4c9c2912e37dea6c8815e15c934f93bf38a707fb3859a27e982229c6`,
161591 bytes, tag and content commit verified ancestors of public
`main`).

## 0. Collision, chronology, and scope guard

Before issue #251, the exact probe name was checked against public
issues, pull requests, remote branches, `probes/`, the registry, the
normative ledger, and object and claim locks; no collision existed.
PR #250 is a NON-CANONICAL planning note and creates no lock.

Incubation provenance: `notes/C-CENTRAL-LIFT-PHASE-1` and the accepted
audit in `notes/C-HERM2-BORN-CONE-1` were public before this
preregistration. Their output was known. This probe is therefore
RESULT-EXPOSED and confirmatory, not prospective. The public verifier is
a narrowed and strengthened derivative: it excludes the claims owned by
the future HERM2 and COMMON probes and replaces the finite unit sweep by
a certificate matched to the universal proof below.

The probe owns only E1-E3 below. `J-PROJECTIONS`, `J-GOLDEN-BRIDGE`, and
`J-TENTH-ROOT` are inherited public T inputs and may be regression
checked, but are not new conclusions.

Explicitly excluded are the Herm2 positive/Born/causal cone, its
boundary, split-unit projectors, boost rigidity, the icosian order,
ramified glue, diagonal integrality, every integral or twisted tick and
tick ladder, physical time, a bit, U(1), electromagnetism, decoder data,
`QCarrier`, `MatterData`, L5 streams, L6 measures, and every cross-layer
lift. Nothing here closes or moves `QUADRATIC-DECODER-DATA` or any other
live row.

## 1. Equation

Let

```text
K       = Q(zeta),                 zeta^4 + zeta^3 + zeta^2 + zeta + 1 = 0,
O_K     = Z[zeta],                 conjugate(zeta) = zeta^-1 = zeta^4,
phi     = -(zeta^2 + zeta^3),      phi^-1 = phi - 1,
J       = 1 + zeta^2 = phi^-1 zeta,
zeta_10 = -zeta^3.
```

The principal embedding is `zeta = exp(2 pi i / 5)` and `sqrt(phi)`
denotes its positive real square root. Put

```text
s   = zeta_10 / sqrt(phi),
g_J = diag(s,s^-1),
A_J = diag(J,1) = s g_J.
```

For `A in GL_2(C)` define the normalized actions

```text
H_A(X) = A X A^dagger / |det A|       on Herm_2(C),
S_A(Y) = A Y A^T      / |det A|       on Sym_2(C).
```

Freeze exactly these decisions.

- **E1 (projective fifth).** `s^2 = J`,
  `s^5 = -phi^(-5/2)`, and
  `g_J^5 = -diag(phi^(-5/2),phi^(5/2))`. At spinor level the fifth
  power is a central minus sign times a positive diagonal boost. Since
  `-I` acts trivially on the normalized Herm action, the induced fifth
  Herm power is the displayed pure boost, while the spinor sign remains
  until `g_J^10`. The minus sign is not claimed as a Sym phase (the
  scalar `c=-1` acts trivially there as well). No physical tick is
  asserted.
- **E2 (projective Herm, central Sym).** For every nonzero complex
  scalar `c`,

  ```text
  H_(cA) = H_A,
  S_(cA) = (c^2 / |c|^2) S_A.
  ```

  For
  `X = [[u,w],[conjugate(w),v]]`, the J step is square-root free:

  ```text
  H_(A_J): (u,v,w) -> (phi^-1 u, phi v, zeta w),
  H_(A_J)^5:        (u,v,w) -> (phi^-5 u, phi^5 v, w).
  ```

  Moreover, with `B=diag(J,J^-1)`, one has `A_J^2=J B`. Therefore
  `H_(A_J^2)=H_B`, while
  `S_(A_J^2)=(J^2/(J conjugate(J))) S_B=zeta^2 S_B`.
- **E3 (universal unit phase).** The image of

  ```text
  O_K^x -> C^x,       c |-> c^2/(c conjugate(c)) = c/conjugate(c)
  ```

  is exactly `mu_5`. The inherited identity
  `1-J = -zeta^2` is a primitive element of `mu_10 \ mu_5`, so it is
  not the normalized Sym phase of an `O_K` unit scalar. This is an
  algebraic obstruction only; it is not attached here to an integral
  carrier, tick, bit, or physical U(1).

## 2. Code

The accepted verifier is
`probes/P-CENTRAL-LIFT-PHASE-1/verify.py`, a self-contained Python 3
standard-library program using exact rational arithmetic in the basis
`1,zeta,zeta^2,zeta^3`. It has no randomness, floating point,
tolerance, network access, subprocess, or filesystem write.

Its ten named gates audit:

1. `R1`, inherited norm and trace identities for `J`;
2. `R2`, the inherited polarization `phi J=zeta`;
3. `E1`, the square, fifth power, and tenth power of `zeta_10` and the
   exact algebraic consequences for `s` and its central sign;
4. `R3`, the inherited golden magnitude `J^5 phi^5=1`;
5. `E2A`, the square-root-free coefficients of `H_(A_J)`;
6. `E2B`, its fifth-power coefficients;
7. `E2C`, the factorization `A_J^2=J diag(J,J^-1)`;
8. `E2D`, the exact `zeta^2` Sym factor;
9. `E3A`, the finite root-of-unity/residue certificate used by the
   universal proof and the attainment of every element of `mu_5`;
10. `E3B`, the primitive tenth-root obstruction `1-J`.

The verifier does not infer a universal unit theorem from a bounded
unit sweep. Section 7 proves the universal step; the finite gate audits
the terminal root-of-unity classification and residue filter.

No formal execution is authorized before the immutable pin containing
this file and `verify.py` is committed and pushed. `EXPECTED.txt` must
be generated only by the first post-pin formal run.

## 3. Carrier and data

The exact synthetic inputs are `K`, `O_K`, the principal archimedean
embedding used to name the positive square root, `Herm_2(C)`, and
`Sym_2(C)` with the displayed actions. There is no external dataset,
checkpoint, orbit, decoder domain, icosian lattice, physical carrier,
or measured input.

## 4. Systematics

- Cyclotomic arithmetic is reduced modulo `Phi_5` in the frozen basis
  `(1,zeta,zeta^2,zeta^3)`.
- Complex conjugation is the Galois map `zeta -> zeta^4`.
- Reduction modulo `lambda = 1-zeta` is the coefficient sum modulo 5.
- The verifier enumerates exactly the ten roots `+-zeta^a`,
  `0 <= a < 5`, only to audit the root-of-unity and residue terminal
  used in section 7. It does not enumerate general units.
- `sqrt(phi)` is not approximated. E1 is certified after squaring and by
  the exact sign `zeta_10^5 = -1` in the principal embedding.
- Output order and spelling are frozen by the ten named gates.

## 5. Failure threshold

Formal acceptance requires exit 0, empty stderr, and stdout
byte-identical to one committed `EXPECTED.txt` on both required GitHub
architectures. Any exact witnessed negation fires a named falsifier:

- **F-CLP-1:** a frozen spinor power, J-action coefficient, fifth-power
  identity, or inherited input used at its registered scope fails;
- **F-CLP-2:** either normalized scalar law, the central factorization,
  or the `zeta^2` Sym phase fails;
- **F-CLP-3:** an `O_K` unit has phase outside `mu_5`, some element of
  `mu_5` is unattained, or `1-J` lies in `mu_5`.

A hash, byte, runtime, or implementation failure that does not exhibit
an exact negation is an integrity STOP. A fired scientific falsifier is
retained and merged; no threshold moves after the pin.

## 6. Action layer

L4 quadratic support only: two normalized actions on fixed quadratic
matrix carriers and their exact central-scalar behavior. E3 is an
algebraic unit lemma used inside that L4 conclusion, not a new state
claim or an L1-to-L4 lift. The other cyclotomic identities are inherited
inputs. There is no state update, clock, physical emission, dictionary,
L5 stream, L6 measure, or layer lift.

## 7. Proof

### 7.1 Inherited cyclotomic inputs

In `K`, direct reduction by `Phi_5` gives

```text
J conjugate(J) = phi^-2 = 2-phi,
phi J = zeta,
1-J = -zeta^2.
```

The first two give `J = phi^-1 zeta`; the last is the registered
primitive tenth-root identity. These are inherited public results. They
are restated only to make the proof self-contained and are not promoted
again.

### 7.2 The normalized scalar laws

For `c != 0`,

```text
(cA) X (cA)^dagger = |c|^2 A X A^dagger,
|det(cA)| = |c^2 det A| = |c|^2 |det A|.
```

The factors cancel, proving `H_(cA)=H_A`. Transpose instead of dagger
gives

```text
(cA) Y (cA)^T = c^2 A Y A^T,
```

with the same denominator, proving
`S_(cA)=(c^2/|c|^2)S_A`. These are identities for every admitted
matrix and scalar, not sampled equations.

### 7.3 The spinor fifth

Because `zeta_10=-zeta^3`,

```text
zeta_10^2 = zeta,
zeta_10^5 = -1,
zeta_10^10 = 1.
```

Hence

```text
s^2 = zeta/phi = J,
s^5 = -phi^(-5/2),
g_J^5 = -diag(phi^(-5/2),phi^(5/2)),
g_J^10 = diag(phi^-5,phi^5).
```

The minus sign is central and disappears under the projective Herm
action, but it is present on the spinor. This proves E1 without a
numerical square root.

### 7.4 The square-root-free J action and central Sym factor

Since `|J|=phi^-1`, direct multiplication gives

```text
A_J X A_J^dagger / |J|
  = [[phi^-1 u, zeta w],
     [zeta^-1 conjugate(w), phi v]].
```

Taking the fifth power uses `zeta^5=1` and gives the displayed pure
boost. Also

```text
A_J^2 = diag(J^2,1) = J diag(J,J^-1).
```

Section 7.2 makes the two Herm actions equal. For the Sym action the
scalar `c=J` contributes

```text
J^2/|J|^2 = J^2/(J conjugate(J))
          = (phi J)^2 = zeta^2.
```

This proves E2. It identifies an algebraic central phase and makes no
physical U(1) identification.

### 7.5 The universal unit-phase image

Let `c in O_K^x` and put `r=c/conjugate(c)`. It is an algebraic-integer
unit. Complex conjugation is central in `Gal(K/Q)`, so for every
embedding `tau:K -> C`,

```text
|tau(r)| = |tau(c)| / |conjugate(tau(c))| = 1.
```

Kronecker's unit-circle lemma now makes `r` a root of unity. For
completeness, the lemma follows because the monic polynomials whose
roots are the conjugates of `r^n` have integer coefficients bounded
independently of `n`; only finitely many such polynomials and roots
exist, so two actual powers of `r` coincide.

The roots of unity in `Q(zeta_5)` are exactly
`mu_10={+-zeta^a:0<=a<5}`. Indeed the cyclotomic degree condition leaves
only orders `1,2,3,4,5,6,8,10,12`. The unique quadratic subfield of the
cyclic quartic field `K` is the real field `Q(sqrt(5))`, excluding
orders `3,4,6`. For order 8 or 12 the corresponding degree-four
cyclotomic field would have to equal `K`, but each contains an imaginary
quadratic subfield, again impossible. Thus only orders dividing 10
remain.

Reduce modulo `lambda=1-zeta`. Sending `zeta` to 1 turns
`Phi_5(zeta)=0` into `5=0`, and the ideal `(1-zeta)` has norm
`Phi_5(1)=5`; hence `O_K/(1-zeta)` is exactly `F_5`. Conjugation acts
trivially because `zeta` and `zeta^-1` both reduce to 1, and a unit has
nonzero residue. Therefore

```text
r = c/conjugate(c) = 1 mod lambda.
```

Among `mu_10`, the elements `zeta^a` reduce to 1 and the elements
`-zeta^a` reduce to -1, which differs from 1 in `F_5`. Thus `r` lies in
`mu_5`. Conversely, for `c=zeta^a`,
`c/conjugate(c)=zeta^(2a)`, and multiplication by 2 permutes the five
exponents. Every element of `mu_5` occurs. This proves that the image is
exactly `mu_5`.

Finally `1-J=-zeta^2` lies in the other coset
`mu_10 \ mu_5`. It cannot be a unit-scalar Sym phase. This proves E3
without classifying the full unit group and without using a bounded
unit sweep.

### 7.6 Status and owner acceptance

Sections 7.1-7.5 are intended as an independent theorem-grade
derivation; the verifier audits their exact certificates. The
two-architecture computation gate alone supports at most C.

```text
OWNER_THEOREM_GRADE_ACCEPTANCE: ACCEPTED by A. M. Thorn / mathorn1973
on 2026-08-02 before the immutable pin; the exact section 7 proof and
scope were accepted explicitly in the current Codex task.
```

This acceptance makes T available through the independent proof, with
the verifier serving as its exact audit. The computation gate alone
would remain capped at C. No registry, frontier, or Canon file changes
in the probe pull request; any later registration is a separate sealed
fold.

## 8. Decision and status discipline

The probe closes positively when the pinned verifier exits 0 with empty
stderr and stdout byte-identical to the committed `EXPECTED.txt` on the
required x86_64 and aarch64 jobs, auditing E1-E3. It closes negatively
when a named falsifier fires. It is STOP on any non-scientific integrity
failure or if the frozen proof, scope, verifier, or threshold changes
after the pin.

The incubation output was known before the pin, so a positive run is
confirmatory. T is available only through the explicit owner acceptance
described in section 7.6; otherwise the exact computation earns at most
C. No result in this probe changes a public status by itself.
