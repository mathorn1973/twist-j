# C-J-YANG-LEE-GALOIS-BRIDGE-N: the Yang-Lee edge, Galois conjugation, and the exact J boundary

```text
STATUS:          NON-CANONICAL NOTE / NO AUTHORITY / NO PUBLIC STATUS
DATE:            2026-09-12
NOTES CLAIM:     issue #968
PUBLIC BASIS:    Public Canon v84
BASIS MAIN:      f10fca3806385a491b32ef40157c51bca08576ab
CONTENT_COMMIT:  9ea313af9d9a03221e4affec3d38e1bb9231146b
CANON_SHA256:    f53c27f042cc3e940c2c5dd90ae0dba851c063c4af334732d250469ae832f2ad
CANON_BYTES:     609802
ACTION LAYER:    L1 exact algebra plus explicitly labeled literature context
FORMAL RUN:      NONE
CANON CHANGE:    NONE
```

This note asks a narrow question: where does the accepted Yang-Lee structure
meet the exact arithmetic of TWIST-J, and where does that meeting stop?

It is not a proposal to identify the TWIST-J substrate with the Yang-Lee CFT,
a Yang-Lee anyon chain, or a topological phase. It records the exact arithmetic
intersection, then states the missing dynamical bridge explicitly.

The local labels are:

```text
[T-public]   an already registered theorem in Public Canon v84
[T-std]      a standard imported mathematical or physical statement
[T-note]     an exact derivation written in this note; no public status
[D-note]     a conditional or interpretive dictionary proposed here
[O-note]     an unresolved question created only inside this note
[TYPE]       a type boundary
[NONCLAIM]   an explicit firewall
```

## 0. Verdict

The relation is stronger than a shared appearance of the golden ratio, but
weaker than a physical derivation.

1. The Yang-Lee minimal model `M(2,5)` has one nontrivial primary field with
   fusion rule `X x X = 1 + X`. `[T-std]`
2. The same fusion polynomial has two algebraic dimensions, `phi` and
   `-phi^-1`. The positive root is the Fibonacci branch and the negative root
   is the Yang-Lee Galois branch. `[T-std]`
3. In TWIST-J, the Yang-Lee dimension and topological twist can be written
   exactly as polynomials in `J`. `[T-note]`
4. In the principal embedding,

   ```text
   J = -d_YL theta_X^-1.
   ```

   This is an exact identity in `Q(zeta_5)`. `[T-note]`
5. The projective modular `T` ratio of the two Yang-Lee characters is a fifth
   root of unity, while the full character normalization has denominator 60.
   Thus the projective fifth-root structure is real, but the complete modular
   normalization is not confined to `Q(zeta_5)`. `[T-std + T-note]`
6. Rogers-Ramanujan characters have an exact finite-state binary precursor.
   This supplies an integer comparison model, not a derivation from the native
   TWIST-J orbit. `[T-std + T-note]`
7. The strongest boundary is dynamical: the fusion algebra does not select a
   Hamiltonian, a sign of interaction, or a critical CFT. Interacting
   Yang-Lee chains with the same fusion data can flow to different critical
   minimal models. `[T-std]`

So the honest summary is:

```text
same degree-4 cyclotomic field                         YES
same real quadratic subfield Q(sqrt(5))               YES
same fusion polynomial x^2-x-1                        YES
Yang-Lee dimension inside Z[J]                         YES, exactly
Yang-Lee twist inside Z[J]                             YES, exactly
J factorized by Yang-Lee dimension and twist           YES, exactly
same positive Hilbert structure                        NO
native TWIST-J dynamics derives M(2,5)                 NOT SHOWN
native TWIST-J state is a Yang-Lee anyon chain         NOT CLAIMED
```

## 1. Public TWIST-J input

Put

```text
zeta = zeta_5,
J    = 1 + zeta^2.
```

Public Canon v84 supplies

```text
N_(Q(zeta)/Q)(J) = 1,                                  [T-public: J-UNIT]
J = zeta / phi in the principal embedding,             [T-public: J-PROJECTIONS]
Z[J] = Z[zeta],                                         [T-public: J-GOLDEN-BRIDGE]
zeta = (J-1)^3.                                         [T-public]
```

The public theory treats the physical modulus/argument readings only at their
registered dictionary strength. Nothing in this note upgrades those readings.

The identity

```text
J - 1 = zeta^2
```

will be used repeatedly.

## 2. Standard Yang-Lee data

The Yang-Lee edge singularity in two dimensions is described by the
non-unitary Virasoro minimal model

```text
M(2,5),
```

with

```text
c = -22/5.                                             [T-std]
```

There are two primary sectors. In a standard labeling their conformal weights
are

```text
h_1 = 0,
h_X = -1/5.                                            [T-std]
```

The nontrivial fusion rule is

```text
X x X = 1 + X.                                         [T-std]
```

Any one-dimensional dimension character on this fusion ring must therefore
satisfy

```text
d^2 = d + 1,
```

hence

```text
d in {phi, -phi^-1}.                                   [T-note]
```

The unitary Fibonacci theory takes

```text
d_Fib = phi,
```

while the Yang-Lee Galois branch takes

```text
d_YL = -phi^-1.                                        [T-std]
```

This sign matters. Writing the Yang-Lee dimension simply as `phi` loses the
non-unitary Galois branch.

## 3. The Galois map is the first exact meeting point

The maximal real subfield of `Q(zeta)` is `Q(sqrt(5))`. In the principal real
embedding,

```text
phi = -zeta^2 - zeta^3.
```

Apply the Galois automorphism

```text
sigma_2 : zeta -> zeta^2.
```

Then

```text
sigma_2(phi)
  = -zeta^4 - zeta
  = -(zeta + zeta^-1)
  = -phi^-1
  = d_YL.                                              [T-note]
```

Thus the Fibonacci and Yang-Lee dimension choices are not unrelated uses of
`sqrt(5)`. They are two Galois embeddings of the same algebraic fusion root.

This is the first precise structural bridge:

```text
phi  --sigma_2-->  -phi^-1.
```

It is algebraic. It is not yet dynamical or physical.

## 4. The Yang-Lee dimension is a polynomial in J

Because

```text
J - 1 = zeta^2,
```

we have

```text
(J-1)^2 = zeta^4 = zeta^-1.
```

Using `J=zeta phi^-1`,

```text
J (J-1)^2
  = zeta phi^-1 zeta^-1
  = phi^-1.
```

Therefore

```text
boxed:  d_YL = -J (J-1)^2.                             [T-note]
```

This gives a concrete ring embedding of the Yang-Lee fusion generator:

```text
Z[X]/(X^2-X-1) -> Z[J]=Z[zeta],
X |-> -J(J-1)^2.                                       [T-note]
```

The image lies in the real subring `Z[phi]`.

The distinction is load-bearing:

```text
J^2 != J + 1.
```

`J` is not the fusion generator. A particular polynomial in `J` is.

## 5. The Yang-Lee twist and the exact factorization of J

For a chiral primary of conformal weight `h`, the topological rotation phase is

```text
theta = exp(2 pi i h).                                 [T-std]
```

For the nontrivial Yang-Lee field,

```text
h_X = -1/5,
```

so

```text
theta_X = exp(-2 pi i/5) = zeta^-1.                    [T-std]
```

Hence

```text
theta_X^-1 = zeta.
```

Together with `d_YL=-phi^-1`, this gives

```text
-d_YL theta_X^-1
  = phi^-1 zeta
  = J.
```

Therefore

```text
boxed:  J = -d_YL theta_X^-1.                          [T-note]
```

Both factors are themselves J-native:

```text
d_YL       = -J(J-1)^2,
theta_X^-1 = (J-1)^3.
```

This is the strongest exact identity in the note. It says that the principal
TWIST-J unit can be factorized into the negative Yang-Lee categorical
dimension and the inverse Yang-Lee twist.

It does not say that one TWIST-J tick is a Yang-Lee braid or a topological
rotation.

## 6. Modular T: fifth-root projective data, sixty-fold full phase

For a Virasoro character, modular `T` acts by

```text
chi_h(tau+1) = exp(2 pi i (h-c/24)) chi_h(tau).         [T-std]
```

For `c=-22/5`,

```text
-c/24 = 11/60.
```

Thus the two exponents are

```text
1-sector:  11/60,
X-sector:  -1/5 + 11/60 = -1/60.
```

So the full diagonal character matrix is

```text
T_full = diag(exp(2 pi i 11/60), exp(-2 pi i/60)).      [T-note]
```

Its relative projective phase is

```text
T_X / T_1
  = exp(-2 pi i 12/60)
  = exp(-2 pi i/5)
  = zeta^-1.                                            [T-note]
```

Therefore the fifth-root structure survives exactly after the common phase is
removed:

```text
T_projective ~ diag(1, zeta^-1).                        [T-note]
```

But the full `T_full` is not confined to `Q(zeta_5)`. Its phases require
sixtieth roots of unity.

This corrects the stronger but inaccurate statement that the full modular
matrices of `M(2,5)` have entries only in `Q(zeta_5)`.

## 7. Rogers-Ramanujan characters from exact binary counting

A useful integer precursor can be written without a continuum field.

Let

```text
b = (b_1,...,b_L),
b_i in {0,1},
b_i b_(i+1) = 0.
```

Thus adjacent ones are forbidden. Give a configuration the integer weight

```text
E(b) = sum_(i=1)^L i b_i
```

and define

```text
C_L(q) = sum_(admissible b) q^E(b).
```

Split the admissible words according to the last bit.

If `b_L=0`, one gets `C_(L-1)`. If `b_L=1`, then `b_(L-1)=0`, and deleting the
last two positions leaves an admissible word of length `L-2` with an extra
weight `q^L`. Hence

```text
C_L(q) = C_(L-1)(q) + q^L C_(L-2)(q).                  [T-note]
```

At `q=1`, the number of admissible words obeys Fibonacci recursion. With the
weight retained, the coefficientwise limit produces the Rogers-Ramanujan
series. In one standard normalization,

```text
G(q) = sum_(n>=0) q^(n^2) / (q;q)_n,
H(q) = sum_(n>=0) q^(n(n+1)) / (q;q)_n,
```

with product forms

```text
G(q) = product_(m>=0) 1/((1-q^(5m+1))(1-q^(5m+4))),
H(q) = product_(m>=0) 1/((1-q^(5m+2))(1-q^(5m+3))).    [T-std]
```

The `M(2,5)` characters are, up to the standard labeling convention,

```text
chi_1(q) = q^(11/60) H(q),
chi_X(q) = q^(-1/60) G(q).                             [T-std]
```

The useful point for TWIST-J is methodological, not identificatory:

```text
finite binary words -> exact integer polynomials -> graded limit ->
Rogers-Ramanujan characters.
```

A continuum CFT can therefore have a rigid discrete counting precursor.

But the native TWIST-J autonomous state is

```text
Omega = N_0 x F_5^6,
```

with its registered update `U`. The no-adjacent-ones language above has not
been derived as a factor, quotient, subshift, or decoder image of that native
orbit. `[TYPE]`

## 8. Why the same fusion algebra does not determine the dynamics

The interacting Yang-Lee anyon chain supplies the cleanest breaker against an
overstrong reading.

The microscopic chain uses the same Yang-Lee fusion data and local projectors,
but the sign of the local interaction matters. In the standard one-dimensional
models studied by Ardonne et al.:

```text
one coupling sign  -> critical M(3,5),  c=-3/5,
opposite sign      -> critical M(2,5),  c=-22/5.        [T-std]
```

The important fact is not the naming convention `ferromagnetic` versus
`antiferromagnetic`. It is that the fusion category alone does not select the
critical theory.

Therefore

```text
same ring + same fusion polynomial + same F-symbol class
```

does not imply

```text
same Hamiltonian + same infrared CFT.
```

For TWIST-J this is an exact warning: finding the Yang-Lee algebra inside
`Z[J]` does not establish that the native update `U` flows to `M(2,5)`.

A genuine dynamics bridge would have to identify, from public TWIST-J objects
and before looking at the target CFT:

```text
1. the two local fusion sectors,
2. the admissible fusion-chain carrier,
3. the local projector or transfer operator,
4. its sign and normalization,
5. the scaling observable,
6. the limiting critical spectrum.
```

None of these six is supplied by the identities in Sections 3 to 5.

## 9. Positivity is not preserved by Galois conjugation

The Fibonacci and Yang-Lee theories make another boundary unusually sharp.
Galois conjugation preserves algebraic equations such as the pentagon and
fusion relations, but it need not preserve positivity or Hermiticity.

This is precisely why the Yang-Lee branch is non-unitary. The literature on
Galois-conjugated topological phases shows that the non-unitary Galois branch
cannot in general be turned into an ordinary positive local topological phase
by a local basis change. `[T-std]`

This matters directly for TWIST-J because

```text
N_(Q(zeta)/Q)(J)=1
```

is an algebraic norm statement. In the principal complex embedding,

```text
|J| = phi^-1 != 1.                                    [T-public]
```

So

```text
field norm one != positive Hilbert unitarity.          [T-public + T-note]
```

The Yang-Lee comparison reinforces the existing public firewall rather than
weakening it.

## 10. What is genuinely interesting for TWIST-J

There are three levels of contact.

### 10.1 Arithmetic contact

This is exact and already strong:

```text
Q(zeta_5),
Q(sqrt(5)),
phi -> -phi^-1 by Galois,
d_YL = -J(J-1)^2,
theta_X^-1 = (J-1)^3,
J = -d_YL theta_X^-1.
```

Status inside this note: `[T-note]`.

### 10.2 Categorical contact

The fusion ring `X^2=1+X`, its two Galois dimensions, fifth-root twist data,
and Rogers-Ramanujan modular structure all live naturally in the same
cyclotomic arithmetic. `[T-std + T-note]`

This is a meaningful comparison class.

### 10.3 Dynamical contact

This is open.

The public TWIST-J update does not currently derive the Yang-Lee fusion-chain
carrier, local interaction, conformal spectrum, or edge singularity.

That missing statement is the only bridge that would justify a stronger
physical claim.

## 11. A falsification-first successor question

The next useful question is not

```text
"Can we recognize more appearances of phi or five?"
```

It is:

```text
Does the native TWIST-J orbit admit a target-independent finite factor whose
language and local operators are the Yang-Lee fusion chain, with the interaction
selected internally rather than chosen after comparison with M(2,5)?
```

A future formal probe should freeze one candidate factor map before any
spectral comparison.

A positive result would require at least:

```text
A. a total map from a declared native carrier to admissible fusion words;
B. exact intertwining of the native update with a declared local transfer law;
C. an internally forced interaction sign and normalization;
D. an exact finite spectral consequence not used to construct the map;
E. a separately gated scaling statement before any CFT identification.
```

An immediate negative result would be earned by any exact collision

```text
same native state/context -> two inequivalent required fusion outputs,
```

or by proof that every admitted target-independent factor is trivial.

No such probe is opened here.

## 12. Nonclaims

This note does not claim:

- that Yang-Lee physics proves TWIST-J;
- that TWIST-J derives `M(2,5)`;
- that `J` is the Yang-Lee fusion generator;
- that a TWIST-J tick is an anyon braid, `F` move, or topological twist;
- that the public checkpoint is a fusion path;
- that the Rogers-Ramanujan variable `q` is the TWIST-J gauge coordinate `q`;
- that algebraic norm one is quantum unitarity;
- that the non-unitary Yang-Lee theory is a physical positive-Hilbert quantum
  phase;
- that the shared field `Q(zeta_5)` selects a unique Hamiltonian;
- that any L2 to L6 physical bridge has been supplied.

## 13. Relation to the existing Fibonacci work

Issue #793 and PR #794 already isolated the unitary Fibonacci branch and
explicitly placed the Lee-Yang/Galois branch outside that scope. The formal
Fibonacci probes then decided exact operator questions inside their own frozen
carriers.

This note does not amend those results. It occupies the branch that they
intentionally left open:

```text
unitary Fibonacci branch        existing work
Galois-conjugate Yang-Lee branch this note
physical identification         neither
```

The two branches are useful together because they exhibit the central lesson
with exceptional clarity:

```text
Galois algebra can survive while positivity changes.
```

That is directly relevant to any attempt to infer physics from the cyclotomic
field alone.

## 14. Literature context

The standard facts used above are drawn from:

1. E. Ardonne, J. Gukelberger, A. W. W. Ludwig, S. Trebst, M. Troyer,
   *Microscopic models of interacting Yang-Lee anyons*, arXiv:1012.1080.
   This is the main source for the Yang-Lee anyon chain, its Galois relation to
   the Fibonacci chain, and the `M(2,5)` / `M(3,5)` critical theories.
2. M. H. Freedman, J. Gukelberger, M. B. Hastings, S. Trebst, M. Troyer,
   Z. Wang, *Galois Conjugates of Topological Phases*, arXiv:1106.3267.
   This supplies the positivity and local-Hermitian boundary for Galois
   conjugates.
3. L. Lootens, R. Vanhove, J. Haegeman, F. Verstraete,
   *Galois conjugated tensor fusion categories and non-unitary CFT*,
   arXiv:1902.11241.
   This gives an explicit lattice treatment of non-unitary Galois-conjugated
   fusion categories and the Yang-Lee sector.

The classical Yang-Lee edge and Rogers-Ramanujan background predates these
papers. This note uses the modern anyon papers because they put the exact
Galois and dynamics boundary in one calculable setting.

## 15. Final boundary

The exact statement worth retaining is:

```text
Within Q(zeta_5), the nontrivial Yang-Lee fusion dimension and twist are
J-native, and their product reconstructs J exactly:

    d_YL = -J(J-1)^2,
    theta_X^-1 = (J-1)^3,
    J = -d_YL theta_X^-1.
```

That is a genuine algebraic meeting point between TWIST-J and an established
piece of mathematical physics.

The stronger statement remains open:

```text
native TWIST-J dynamics -> Yang-Lee fusion dynamics -> M(2,5).
```

The note stops there on purpose.
