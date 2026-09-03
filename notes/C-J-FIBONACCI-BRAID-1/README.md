# C-J-FIBONACCI-BRAID-1: action phase, the integral J step, and the Fibonacci braid boundary

```text
STATUS:          NON-CANONICAL NOTE / NO AUTHORITY / NO PUBLIC STATUS
DATE:            2026-09-03
NOTES CLAIM:     issue #793
PUBLIC BASIS:    Public Canon v75
BASIS MAIN:      4f08791bd5401ee1616270661f7788d743f5fc26
CONTENT_COMMIT:  e32e85ed7297d4320df5b345e4488d78323d550c
CANON_SHA256:    44130160a3ce29bfcdc757e255d2d1c25a010b22911edfe66cf6b132be081fbe
CANON_BYTES:     399513
ACTION LAYER:    L1 exact algebra plus explicitly labeled literature context
FORMAL RUN:      NONE
CANON CHANGE:    NONE
```

This note separates an exact relation from three stronger readings that do
not follow from it. It creates no Canon, Registry, Frontier, dependency,
gate, evidence, release, or probe result.

The labels in this file are local and deliberately more explicit than the
public status ladder:

```text
[T-public]  an already registered theorem of Public Canon v75
[T-std]     a standard imported mathematical or physical statement
[T-note]    an exact derivation written in this note; no public status
[D-note]    a conditional dictionary proposed here, not a theorem
[E-lit]     a report of a cited experiment, with its stated boundary
[O-public]  an already registered open public obligation
[F-public]  an already registered public falsifier or closed firewall
[TYPE]      a type boundary; the comparison is undefined as stated
[F-note]    a formulation ruled out here; not a new Registry F row
[UNSUPPORTED] a stronger statement not established by the cited evidence
[N-prior]   context from an earlier non-canonical note; no authority
[N-note]    an administrative boundary or explicit non-claim
```

## 0. Verdict

There is a precise relation, but it is narrower than the first formulation.

1. In the phase law, `h` is the period in action that produces one full phase
   turn. The phase sees `S/h` only modulo integers. `[T-std]`
2. In the principal embedding, the phase of `J` is one fifth of a turn. If a
   `J` step is *defined* to enter the Feynman phase law through its normalized
   phase, its action residue is therefore `1/5 mod 1`. `[D-note]`
3. The raw multiplication step `M_J` is an exact integral determinant-one
   automorphism. It is not unitary and cannot be made unitary by any positive
   definite Hermitian form. Algebraic norm one does not replace Hilbert-space
   unitarity. `[T-public + T-note]`
4. The unitary Fibonacci braid representation admits an integral,
   non-orthonormal gauge over the same ring `Z[zeta_5]=Z[J]`. This is a real
   structural match. `[T-std + T-note]`
5. The hyperbolic operators do not match. The exact two-dimensional CM
   pullback step is not even projectively conjugate to a word in the unitary
   Fibonacci braid image. The obstruction is already the projective spectral
   invariant `tr(A)^2/det(A)`. `[T-note]`
6. The circular primary sector admits an exact abelian braid shadow after the
   action `chi_C(w)=P^e(w)` is explicitly declared: as an integral
   `Z[P]`-module it is the regular lattice of multiplication by `1-J`, and
   `1-J` is exactly the determinant of either Fibonacci braid generator in
   the frozen ribbon normalization. `[T-note]`

Thus the useful result is not "the J step is a Fibonacci braid". It is a
sharper boundary:

```text
same cyclotomic integer ring and an integral lattice      YES
same positive-unitary hyperbolic operator class            NO
circular determinant-character shadow                     YES, exactly
full representation on A_CM                               NO, projectively
full representation on displayed O_K-linear C_Z            NO, rank-one
full representation on any future enriched carrier         NOT DECIDED
public phibit = tau                                         NO; already fired
other TWIST-J object = tau                                  NOT ASSERTED HERE
```

## 1. Where `h` enters an integer path sum

The standard action phase is

```text
exp(i S / hbar) = exp(2 pi i S / h).                    [T-std]
```

It depends only on the residue class

```text
[S/h] in R/Z.                                           [T-std]
```

Calling `h` "one whole turn" is a useful reading of this quotient: increasing
the action by `h` leaves the phase unchanged. It is not a claim that the
dimensionful constant is internally an integer, nor that every action is
quantized. `[D-note]`

If a finite, equally weighted discrete path model permits only `N`th-root
phases, then

```text
[S/h] in (1/N Z)/Z,
v = sum_(k=0)^(N-1) c_k zeta_N^k,    c_k in N_0.        [T-std]
```

Here `c_k` counts paths in phase class `k`. Integer coefficients can also be
used after algebraic regrouping, but raw path multiplicities are
nonnegative. This is a statement about a finite discrete path sum, not the
general continuum path integral.

For the two-phase case the exact statement is

```text
[S/h] in {0,1/2} subset R/Z,
v = c_0-c_1.                                            [T-std]
```

The shorthand `S/h in Z/2` is therefore replaced: `Z/2Z` labels the two
classes, while the action residues themselves are `0` and `1/2` modulo one.

The Clifford+T comparison also needs its denominator stated. Put

```text
H_num = [[1,1],[1,-1]],       det(H_num) = -2,
H_Had = 2^(-1/2) H_num,       det(H_Had) = -1.
```

For a circuit presentation with `n_H` Hadamard occurrences, each matrix
element has a path-sum presentation

```text
2^(-n_H/2) a,    a in Z[zeta_8],                       [T-std]
```

although cancellations can reduce the displayed power. The full exact
coefficient ring is

```text
Z[1/sqrt(2),i] = Z[1/2,zeta_8],                        [T-std]
```

not merely `Z[zeta_8]`. The latter is the root-of-unity and unnormalized
numerator ring.

## 2. What the public J step proves, and what it does not

Let `zeta=zeta_5` and `J=1+zeta^2`. Public Canon v75 proves

```text
arg(J) = 2 pi/5,       |J| = phi^-1                    [T-public: J-PROJECTIONS]
N_(Q(zeta)/Q)(J) = 1                                  [T-public: J-UNIT]
```

and, in the ordered basis `(1,zeta,zeta^2,zeta^3)`, multiplication by `J` is

```text
M_J = [[1,0,-1,1],
       [0,1,-1,0],
       [1,0, 0,0],
       [0,1,-1,1]],

det(M_J)=1.                                             [T-public: J-STEP]
```

Also

```text
J-1=zeta^2,       (J-1)^3=zeta,
Z[J]=Z[zeta].                                           [T-public + T-note]
```

Therefore every iteration of the raw step maps `Z^4` bijectively to itself
and introduces no denominator. This statement is exact but narrow. The
rational CM primary projector already has unavoidable denominator five, so
"the J program never introduces a denominator" would be false once derived
projectors or normalizations are included.

More importantly, the equality

```text
det(M_J)=N(J)=1
```

is a volume and lattice statement. It is not a norm-preservation theorem on a
Hilbert space. The four archimedean eigenvalue moduli of `M_J` are

```text
phi, phi, phi^-1, phi^-1.                              [T-public: J-TORAL-ENTROPY]
```

If a matrix preserves a positive definite Hermitian form, it is similar to a
unitary matrix and every eigenvalue has modulus one. Hence:

```text
No positive definite Hermitian form makes M_J unitary.  [T-note]
```

The sentence "unitarity is replaced by the field norm" is therefore ruled
out. `[F-note]` An indefinite invariant form may exist, but it cannot by
itself supply nonnegative Born weights.

## 3. The exact `h/5` statement

In the principal embedding,

```text
phase(J) := J/|J| = zeta_5.                             [T-public]
```

Adopt, only as a conditional dictionary, the equation

```text
phase(J step) = exp(2 pi i DeltaS_J/h).                 [D-note]
```

Then and only then,

```text
DeltaS_J/h = 1/5 mod 1,
DeltaS_J    = h/5 mod h.                                [T-note, conditional on D-note]
```

This does not determine an absolute action value: every
`h/5 + m h`, `m in Z`, has the same phase. It also uses only the normalized
phase of `J`; the modulus `phi^-1` is not part of the Feynman phase.

Public Canon v75 already owns the dimensionless equality

```text
one tick = 1/5 cycle = 2 pi/5                           [T-public: METRO-TICK]
```

on its declared fiber-circle carrier. No public theorem identifies that tick,
the normalized phase of the raw `J` multiplication step, and a physical
action increment as one typed object. Such an identification would require a
named bridge.

The value of `h` is not selected or calibrated here. The exact CM seam result
explicitly selects no action, `h`, `hbar`, or `2 pi`.
`CM-PERIOD-LATTICE-NONSELECTION [T]` blocks the frozen unmarked/naturality
selector route, including the declared `mu_10`-fixed decomposable-cell class;
it does not block a selector supplied with additional typed data. `[T-public]`
The closest named public SI selector is

```text
METRO-EDGE-SCALE [O-public].
```

It does not itself define a bridge from a `J` step to physical action or to
`h`. `[O-public]`

This is the surviving content of the earlier "Debt B": `h/5 per step` is a
dictionary normalization until the step is tied, by a typed and independently
testable bridge, to a measured action.

Four nearby phases must remain distinct:

| exact element | turn fraction | role |
|---|---:|---|
| `J/|J|=zeta` | `+1/5` | normalized principal phase of the J step |
| `theta_tau=zeta^2=J-1` | `+2/5` | Fibonacci topological twist |
| `det R=1-J=-zeta^2` | `-1/10` | determinant phase in the frozen ribbon normalization |
| `R_11/R_22=-zeta^-1` | `+3/10` | projective eigenvalue ratio of one braid generator |

They lie in the same cyclotomic field and are algebraically related. They are
not four names for the same `h/5` increment.

## 4. Consequence for the Born obligation

The raw task cannot be

```text
find a positive Hermitian form under which M_J is unitary,
```

because the public spectrum proves that class empty. `[T-note]` The same
obstruction holds on the hyperbolic CM pullback sector below.

A viable Born construction would instead have to name all of the following:

1. a physical state carrier distinct from, normalized from, or enlarged
   beyond the raw hyperbolic transfer;
2. its positive pairing;
3. the physical action that preserves that pairing;
4. the map from the integral substrate action to that physical action;
5. the normalization, apparatus, event, and measure layers.

The public `DEF-QDD-BRANCH-WEIGHT-PAIRING` does not pay this debt. It is an
adopted L1 algebraic branch-weight dictionary, explicitly not a physical Born
pairing and not derived from `J` or the projectors. The physical apparatus and
measure obligations remain open. `[O-public]`

## 5. What the Fibonacci model really supplies

Use the unitary Fibonacci chirality fixed by the displayed `R` matrix below,
on the fusion space of three `tau` anyons with total charge `tau`. Put

```text
zeta = exp(2 pi i/5),
a    = phi^-1 = zeta+zeta^-1.
```

In an orthonormal fusion basis the standard matrices are

```text
F_0 = [[a,       sqrt(a)],
       [sqrt(a), -a      ]],

R   = diag(zeta^-2,-zeta^-1),

rho(sigma_1)=R,       rho(sigma_2)=F_0 R F_0.           [T-std]
```

They satisfy the braid relation. The topological twist in this chirality is

```text
theta_tau=zeta^2.                                      [T-std]
```

The opposite chirality complex-conjugates these data. `[T-std]` The unitary
Fibonacci braid representation is mathematically universal: its projective
image is dense in the appropriate projective unitary group.
`[T-std, literature]`

There is an exact integral gauge. Let

```text
D   = diag(sqrt(a),1),
F_O = D^-1 F_0 D = [[a, 1],
                    [a,-a]],
G_Fib = D^* D = diag(a,1).
```

Using `a^2+a=1`, direct multiplication gives

```text
F_O^2=I,       det(F_O)=-1,
B_1=R,         B_2=F_O R F_O,
B_2=[[ a zeta^2, -zeta],
     [-a zeta,   -a   ]],
B_i in GL_2(Z[zeta]),
B_i^* G_Fib B_i=G_Fib.                                 [T-note]
```

In the distinguished physical embedding `a>0`, so `G_Fib` is positive
definite. Write `O_K=Z[zeta_5]=Z[J]`. This proves the precise ring match:

> The Fibonacci braid representation admits an invariant
> `Z[zeta_5]=Z[J]` lattice, and its generators have cyclotomic-integer
> coordinates in a non-orthonormal integral basis.

It does **not** prove that normalized physical amplitudes in an orthonormal
basis are exactly elements of `Z[zeta_5]`. Returning to the orthonormal basis
returns `sqrt(a)=phi^-1/2`; the positive form `G_Fib` is what carries unitarity
in the integral coordinates. `[T-note]`

Under the Galois embedding `zeta -> zeta^2`, `a` becomes `-phi` and `G_Fib` has
signature `(1,1)`. That is the non-unitary Galois/Lee--Yang branch, not the
physical unitary Fibonacci branch. It is a separate possible question and
must not be substituted after seeing the unitary result. `[T-note]`

### Experimental status `[E-lit]`

Superconducting processors have digitally prepared Fibonacci string-net
states and demonstrated selected creation, braiding, fusion, and sampling
operations. These are significant proofs of principle. They are not a
topologically protected universal Fibonacci computer, and the laboratory
amplitudes are not certified as exact cyclotomic integers. Therefore the safe
statement is: `[E-lit]`

> There is a mathematically universal Fibonacci braid model over the same
> cyclotomic ring, together with experimental digital proofs of principle.

The stronger sentence "a physically realized universal machine whose
amplitudes are exactly the axiom ring" is not established by the cited
experiments and must not be asserted here. `[UNSUPPORTED]`

## 6. The typed operator comparison

The raw proposal asks whether `M_J`, "or its hyperbolic reduction", lies in a
two-dimensional Fibonacci braid image. These are not two alternatives of one
typed question.

```text
M_J:                  4 by 4 over Z on O_K (Z-rank 4, O_K-rank 1)
standard Fib lattice: O_K-rank 2 (Z-rank 8), then dimension 2 over C
direct membership:    UNTYPED                                  [TYPE]
```

The public two-dimensional object is not a restriction of `M_J`. It is the
restriction of the induced pullback on alternating forms:

```text
P(W) = M_J^T W M_J                 on Alt^2(Q^4),
H_Q  = ker(P^2-3P+I),
H_Z  = Z Omega_1 direct-sum Z Omega_2,

A_CM := Mat_(Omega_1,Omega_2)(P|H_Q)
      = [[ 1,-1],
         [-1, 2]].                                      [T-public]
```

This definition removes the ambiguity. It consumes
`J-STEP`, `CM-ALTERNATING-PENCIL`, and
`CM-ALTERNATING-PRIMARY-LATTICE-SEAM`, all at L1.

The widest reasonable basis- and phase-independent comparison with the
unitary Fibonacci branch is:

```text
Does there exist w in B_3, lambda in C^x, and G in GL_2(C) such that

    A_CM = lambda G^-1 rho(w) G ?                       (Q)
```

Define, for an invertible two by two matrix,

```text
kappa(X) = tr(X)^2 / det(X).
```

This is unchanged by conjugation and multiplication by any nonzero scalar.
For the CM target,

```text
tr(A_CM)=3,       det(A_CM)=1,       kappa(A_CM)=9.      [T-note]
```

Every `rho(w)` preserves the positive form `G_Fib`, hence is similar to a
unitary matrix. If its two eigenvalues are `exp(i alpha_1)` and
`exp(i alpha_2)`, then

```text
kappa(rho(w))
  = 2+2 cos(alpha_1-alpha_2)
  = 4 cos^2((alpha_1-alpha_2)/2)
  in [0,4].                                              [T-note]
```

Since `9` is not in `[0,4]`, equation `(Q)` has no solution. This excludes,
at once:

```text
literal membership,
membership up to a global phase,
conjugacy after an arbitrary change of basis,
projective conjugacy after both changes.                [T-note]
```

The ordinary trace is already a first filter for literal membership:
`|tr(A_CM)|=3>2`. It is not the correct projective invariant; `kappa` is.

No bounded braid-word search is warranted. Fibonacci density approximates
targets inside the projective-unitary locus. The class of `A_CM` is outside
that locus, and continuity of `kappa` separates it (`9` versus `[0,4]`), so it
is not even arbitrarily approximable there. Density is irrelevant to this
target. `[T-std + T-note]`

### 6.1 The circular sector: an exact abelian braid shadow

The same public pullback has the complementary rational primary sector

```text
C_Q=ker(P^4-P^3+P^2-P+I),
C_Z=C_Q intersect Alt^2(Z^4)
   =Z c1 direct-sum Z c2 direct-sum Z c3 direct-sum Z c4,             [T-public]
```

where

```text
c1=(-1, 0,1,0,0,0),       c2=( 0,-1,0,1,0,0),
c3=( 0,-1,0,0,1,0),       c4=(-1, 0,0,0,0,1).
```

Public Canon v75 proves that `P|C_Q` has characteristic polynomial
`Phi_10` and exact order ten. There is a stronger integral statement. Direct
use of the public pullback matrix gives

```text
c2,
P c2     = c1,
P^2 c2   = c1-c4,
P^3 c2   = c2-c3.                                           [T-note]
```

These four orbit vectors have determinant `+1` in the ordered public basis
`(c1,c2,c3,c4)`. They are therefore a `Z`-basis of `C_Z`, not merely a
rational basis. Put

```text
delta=1-J=-zeta^2,       zeta=-delta^3,
Z[delta]=Z[zeta]=O_K.
```

The element `delta` is a primitive tenth root with minimal polynomial
`Phi_10`. Consequently the map

```text
Psi: Z[delta] -> C_Z,
Psi(delta^n)=P^n c2,       n=0,1,2,3.                         [T-note]
```

Here the `Z[x]` actions are declared by `x.u=delta u` on `Z[delta]` and
`x.v=P v` on `C_Z`. Thus `Psi` is an integral `Z[x]`-module isomorphism.
`[T-note]`

Equivalently,

```text
(C_Z,P) is integrally conjugate to
(Z[1-J], multiplication by 1-J).                            [T-note]
```

Now use the fixed Fibonacci ribbon normalization of section 5:

```text
det R=(zeta^-2)(-zeta^-1)=-zeta^2=1-J.
```

Since `det(F_O)^2=1`, both braid generators have determinant `1-J`. If
`e:B_3->Z` is the exponent-sum abelianization, every braid word obeys

```text
det rho(w)=(1-J)^e(w).                                      [T-note]
```

Declare the abelian action

```text
chi_C:B_3 -> Aut_Z(C_Z),       chi_C(w)=P^e(w).
```

Then `Psi` intertwines `chi_C` with the restriction to the underlying
`Z`-lattice of the scalar determinant character
`u -> det(rho(w))u=delta^e(w)u` on `O_K`. This is the exact positive relation:

> After the explicit declaration of `chi_C`, the circular pullback sector is
> integrally isomorphic to the abelian determinant-character channel of the
> frozen Fibonacci braid representation. `[T-note]`

Under the displayed `O_K`-module identification, `C_Z` has rank one, so its
`O_K`-linear endomorphisms are scalar and commute. It therefore cannot realize
the frozen irreducible rank-two `O_K` Fibonacci representation, whose braid
generators include noncommuting `F` mixing. This is a no-go only for the
displayed carrier and compatible `O_K`-linear action; it says nothing about a
future carrier with additional structure. `[T-note]`

The projective eigenvalue ratio of `R` is `-zeta^-1`, another primitive root
of `Phi_10`. It is the image of `1-J` under the explicit Galois marking
`gamma:zeta->zeta^2`; identifying the two therefore requires that marking.
The determinant identity above is basis invariant but depends on the frozen
full ribbon normalization. Arbitrary projective rephasing intentionally
erases it.

## 7. Formal-probe disposition

The note-level candidate `C-J-FIBONACCI-BRAID-1` should not become a word
search. If promoted to formal public work, the following is only a candidate
outline; it is not a preregistration or a pin:

```text
probe:       P-J-FIBONACCI-BRAID-1
claim A:     J-CM-FIBONACCI-BRAID-PROJECTIVE-NONMEMBERSHIP
claim B:     J-CIRCULAR-FIBONACCI-DETERMINANT-CHARACTER
mode:        RESULT-EXPOSED / PROOF-FIRST
layer:       L1 exact cyclotomic and matrix algebra
target A:    A_CM only; raw M_J is a TYPE boundary
target B:    (C_Z,P), delta=1-J, and det o rho
representation: unitary chirality frozen by R=diag(zeta^-2,-zeta^-1)
equality A:  projective conjugacy over C, hence all narrower equalities
equality B:  explicit integral Z[x]-module isomorphism in displayed bases
decision A:  NO by kappa(A_CM)=9 versus kappa(image) subset [0,4]
decision B:  YES by the unimodular c2 orbit and det R=1-J
search:      NONE
```

The six formal fields must reconstruct both primary restrictions from the
public `M_J` and alternating-form pullback, construct the selected integral
Fibonacci gauge, verify its braid relation and positive invariant form, audit
the exact projective no-go, verify the unimodular `c2` orbit, and prove the
determinant character. The universal statements are carried by written
proofs; an exact verifier is only their finite audit.

A non-unitary Galois/Lee--Yang comparison is not a fallback outcome. It would
be a new probe with a new identifier, representation, invariant form,
decision algorithm, and pin.

## 8. Firewalls and non-claims

1. `[F-public]` `PHIBIT-NOT-TAU [F]` remains closed: the public phibit is not
   identified with `tau`. This note makes no other TWIST-J-object-to-`tau`
   identification.
2. `[N-prior]` The older NON-CANONICAL `C-FIB-MTC-J-LOCK` records the
   modular-data coincidence `d_tau=phi`, `theta_tau=zeta^2`,
   `J=1+theta_tau` and its Galois shadow. It has no authority. The new content
   here is only the operator-level boundary.
3. `[N-note]` Agreement of coefficient rings, and even the exact circular determinant
   channel, is not agreement of the full operators, carriers, inner products,
   dynamics, or measurements.
4. `[N-note]` No Born rule, apparatus, occurrence law, probability measure, sampling
   process, topological protection, quantum advantage, or physical speedup is
   derived.
5. `[N-note]` No action, `h`, `hbar`, or SI value is derived from the CM lattice, its
   index-five seam, the braid data, or the shared ring.
6. `[N-note]` No Canon status moves. No formal probe is pinned or run by this note.

## 9. Literature used only for the labeled comparison

- M. H. Freedman, M. Larsen, Z. Wang, *A modular functor which is universal
  for quantum computation*, Communications in Mathematical Physics 227
  (2002), 605--622. DOI: <https://doi.org/10.1007/s002200200645>.
- M. H. Freedman, M. Larsen, Z. Wang, *The two-eigenvalue problem and density
  of Jones representation of braid groups*, Communications in Mathematical
  Physics 228 (2002), 177--199. DOI:
  <https://doi.org/10.1007/s002200200636>.
- C. Nayak, S. H. Simon, A. Stern, M. Freedman, S. Das Sarma,
  *Non-Abelian anyons and topological quantum computation*, Reviews of Modern
  Physics 80 (2008), 1083--1159. DOI:
  <https://doi.org/10.1103/RevModPhys.80.1083>.
- S. Xu et al., *Non-Abelian braiding of Fibonacci anyons with a
  superconducting processor*, Nature Physics 20 (2024), 1469--1475. DOI:
  <https://doi.org/10.1038/s41567-024-02529-6>.
- Z. K. Minev et al., *Realizing string-net condensation: Fibonacci anyon
  braiding for universal gates and sampling chromatic polynomials*, Nature
  Communications 16 (2025), 6225. DOI:
  <https://doi.org/10.1038/s41467-025-61493-8>.
- B. Giles, P. Selinger, *Exact synthesis of multiqubit Clifford+T circuits*,
  Physical Review A 87 (2013), 032332, for the exact Clifford+T coefficient
  ring. DOI: <https://doi.org/10.1103/PhysRevA.87.032332>.

The literature supplies context and the standard Fibonacci model. The
operator no-go of section 6 is self-contained exact algebra once the displayed
`F_0`, `R`, and the public `A_CM` are fixed.
