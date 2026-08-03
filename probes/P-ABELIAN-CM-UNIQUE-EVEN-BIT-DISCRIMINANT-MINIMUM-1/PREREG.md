# PREREG. P-ABELIAN-CM-UNIQUE-EVEN-BIT-DISCRIMINANT-MINIMUM-1

```text
PREREGISTERED CANDIDATE / RESULT-EXPOSED / PROOF-FIRST /
FIRST FORMAL RUN PENDING REMOTE PIN READBACK
```

Public lock: issue
[#262](https://github.com/mathorn1973/twist-j/issues/262), created
`2026-08-03T16:46:49Z` before this branch, path, prospective pin, verifier
execution, or formal data. The issue claims exactly this probe, branch, path,
target, owner, and L1 scope.

Base: Public Canon v33 ACTIVE, tag `canon-v33`, activation commit and branch
parent `61f33e61bdde5adf355fb605f620f1601e154fc2`, Canon content commit
`070c1ad847db4b32ef9f91992a3bde2887749737`, Canon SHA-256
`b11214dab9fe6209f2bad543da1b4c6296a9cb5dc3cf8f7801b5fc67e892a607`,
167461 bytes. The tag equals the branch parent and the content commit is its
ancestor.

```text
LAYER:  L1 exact arithmetic only. No lift to L2-L6.
TARGET: ABELIAN-CM-UNIQUE-EVEN-BIT-DISCRIMINANT-MINIMUM, proposed T,
        proof-first: prove the exact absolute-discriminant minimum and
        equality field in the frozen abelian Galois CM class with exactly
        one quadratic character and with that character even on CM complex
        conjugation.
```

This preregistration earns no scientific status. The target is absent from
the Public Canon v33 registry. Any Canon, registry, dependency, dictionary,
or release disposition is separate reviewed work.

## 0. Chronology, exposure, and proof role

The candidate theorem, proof route, and expected mathematical outcome were
developed before the prospective pin. The current Codex/GPT seat is therefore
a result-exposed builder, not a blind discoverer. This is a confirmatory
proof-first probe. Proposed `T` rests on the complete written proof below;
the verifier audits only exact finite seams.

The accepted `verify.py` has been written and reviewed as source. Before this
pin it has not been executed, imported, or used to produce scientific output.
Only AST parsing and static source review were performed, as POLICY permits.
`EXPECTED.txt`, `RUN.md`, and `RESULT.md` do not exist at preregistration.

No independent breaker is claimed by this file. If one is later authorized,
its identity, information firewall, source pin, and decision role must be
published before it reads this verifier or any builder stdout. Merely replaying
the accepted verifier is reproduction, not an independent proof.

## 1. Equation

### 1.1 Frozen notation and input class

Write `C_2={+1,-1}` multiplicatively. For a finite Galois CM extension
`K/Q`, write

```text
G_K     = Gal(K/Q),
c_K     = canonical CM complex conjugation in G_K,
absDisc(K) = |D_K|.
```

Every `Hom(G_K,C_2)` below is an ordinary group homomorphism, and the set of
such homomorphisms includes the trivial character.

The frozen class `A` consists of fields `K/Q`, up to `Q`-isomorphism,
satisfying all five conditions:

1. `K/Q` is a finite Galois extension;
2. `G_K` is abelian;
3. `K` is a CM field;
4. `|Hom(G_K,C_2)|=2`; and
5. every quadratic character kills complex conjugation:

   ```text
   for every chi:G_K->C_2, chi(c_K)=+1.
   ```

Condition 4 says there is exactly one nontrivial quadratic character. No
degree, conductor, unit rank, total-ramification condition, cyclotomic
presentation, or physical interpretation is part of `A`.

### 1.2 Frozen theorem statement

The theorem candidate comprises E1--E3 exactly.

**E1. Universal lower bound.**

```text
For every K in A, absDisc(K) >= 125.
```

**E2. Equality classification.**

```text
For K in A, absDisc(K)=125
if and only if K is Q-isomorphic to Q(zeta_5).
```

**E3. Unique minimizer corollary.**

```text
Q(zeta_5) belongs to A and is, up to Q-isomorphism, the unique
absolute-discriminant minimizer in A.
```

E3 is an arithmetic corollary of E1 and E2. It is not the hypothesis that
Nature selects the minimum.

### 1.3 Named classical theorem inputs

The proof uses exactly the following standard theorems. They are named inputs,
not claims earned by the finite verifier.

1. For a finite Galois CM extension, CM complex conjugation is a nonidentity
   central involution.
2. For an abelian group `G`, the intersection of the kernels of every
   `G->C_2` character is the square subgroup `G^2`.
3. Minkowski's discriminant bound for a totally imaginary degree-`n` field:

   ```text
   absDisc(K) >= (pi/4)^n n^(2n)/(n!)^2.
   ```

4. Kronecker--Weber and the abelian character-field correspondence: a finite
   abelian extension of `Q` has an associated group of primitive Dirichlet
   characters canonically dual to its Galois group; primitive association
   preserves the character order and fixed field.
5. The conductor-discriminant theorem for an abelian extension:

   ```text
   absDisc(K) = product_(nontrivial chi in X_K) f(chi).
   ```

6. Primitive quadratic Dirichlet characters correspond to fundamental
   discriminants.
7. The cyclotomic discriminant formula for `Q(zeta_p)` at an odd prime `p`.

Primary reference points checked before the prospective pin are Keith
Conrad's *History of Class Field Theory*, Theorem 5.8, for input 5; MIT 18.786
Problem Set 6, Problem 2(c)--(e), for primitive association, order, fixed
field, conductor, and parity; and Keith Conrad's *Gauss and Jacobi Sums on
Finite Fields and Z/mZ*, Section 3, for the quadratic characters modulo 8.
The proof below contains every application needed at the frozen scope.

### 1.4 Complete written proof

#### Step A: the positive control

Let `K_5=Q(zeta_5)`. It is a finite abelian Galois CM extension with

```text
G_(K_5) = (Z/5Z)^x = C_4.
```

There are exactly two maps `C_4->C_2`, including the trivial map. Complex
conjugation is the unique involution, the square of a generator. The unique
nontrivial quadratic map sends a generator to `-1`, hence sends its square to
`+1`. Thus `K_5` belongs to `A`. The cyclotomic discriminant formula gives

```text
absDisc(K_5)=5^(5-2)=5^3=125.
```

This proves that the minimum, if compared against `K_5`, is at most 125.

#### Step B: the quarter-turn and degree divisibility

Let `K` belong to `A`, put `G=G_K`, and write `c=c_K`. Then

```text
c != 1, c^2=1.
```

For abelian `G`, the quotient `G/G^2` is an `F_2`-vector space. If the class
of `c` were nonzero, a linear functional on `G/G^2` would send it to `1`; its
composition with the quotient map would be a character `G->C_2` not killing
`c`. This contradicts admissibility. Therefore `c` lies in `G^2`, so

```text
c=tau^2
```

for some `tau in G`. Since `tau^2=c` is nonidentity and `c^2=1`, `tau` has
order exactly four. Lagrange's theorem gives

```text
4 divides |G|=[K:Q].                                  (A)
```

No uniqueness of `tau` is used or claimed.

#### Step C: Minkowski reduces every smaller or tied field to degree four

It is enough to classify a `K in A` with `absDisc(K)<=125`; fields above that
threshold already satisfy E1 and cannot tie E2.

Let `n=[K:Q]`. A CM field is totally imaginary. From Minkowski and `pi>3`,

```text
absDisc(K) > M(n),
M(n)=(3/4)^n n^(2n)/(n!)^2.
```

Direct exact cancellation gives

```text
M(8)=21233664/1225 > 125.                             (B1)
```

For every positive integer `n`,

```text
M(n+1)/M(n)=(3/4)(1+1/n)^(2n).                       (B2)
```

The constant, linear, and quadratic terms of the binomial expansion give

```text
(1+1/n)^(2n)
  >= 1 + 2n/n + binom(2n,2)/n^2
   = 5 - 1/n
  >= 4.
```

Hence the ratio in B2 is at least 3. By B1, `M(n)>125` for every `n>=8`.
Together with A, a field in `A` having discriminant at most 125 must satisfy

```text
n=4.                                                  (B3)
```

This is an infinite degree exclusion; the finite verifier only audits the
displayed rational identities.

#### Step D: the exactly-one-bit condition forces a cyclic quartic group

An abelian group of order four is isomorphic to `C_4` or `C_2 x C_2`. The
Klein group has four maps to `C_2`, including the trivial map. Condition 4
therefore excludes it. Thus

```text
G is isomorphic to C_4.                               (C)
```

Write `G=<sigma>`. Its unique involution is `sigma^2`, so CM complex
conjugation is `c=sigma^2`.

#### Step E: the faithful quartic Dirichlet character

By Kronecker--Weber and the character-field correspondence, `K` has an
associated primitive character group `X_K` canonically dual to `G`. Primitive
representatives are multiplied followed by primitive association. From C,

```text
X_K={1,psi,psi^2,psi^3}
```

for a primitive Dirichlet character `psi` of exact order four whose kernel
cuts out `K`. The faithful characters are `psi` and `psi^3=psi^(-1)`.

Faithfulness gives

```text
psi(c)=psi(sigma^2)=-1,
```

so `psi` is odd. Put `epsilon=psi^2`. It is the unique nontrivial quadratic
member of `X_K`, and

```text
epsilon(c)=+1,
```

so it is even. The odd faithful quartic character and the even quadratic bit
are different objects.

#### Step F: the conductor-discriminant identity

The conductor-discriminant theorem applied to the three nontrivial members of
`X_K` gives the field-discriminant identity

```text
absDisc(K)=f(psi)f(psi^2)f(psi^3).
```

An inverse primitive character has the same conductor, so

```text
absDisc(K)=f(psi)^2 f(epsilon).                       (D)
```

This is not a polynomial-discriminant or order-discriminant substitution.

#### Step G: exact small-conductor bounds

The image of an exact-order-four character contains an element of order four.
The unit groups at moduli 1 and 2 are trivial, and those at moduli 3 and 4
have exponent two. Therefore

```text
f(psi)>=5.                                            (E1)
```

The character `epsilon` is nontrivial, primitive, quadratic, and even. There
is no nontrivial primitive quadratic character at conductor 1 or 2. The
unique primitive quadratic characters at conductors 3 and 4 are odd because
they send `-1` to `-1`. Therefore

```text
f(epsilon)>=5.                                        (E2)
```

For the explicit pure 2-primary control, use

```text
(Z/2^a Z)^x = C_2 x C_(2^(a-2)) for a>=3.
```

An exact-order-four character of pure 2-power conductor requires `a>=4`, so
`f(psi)>=16`. Primitive quadratic characters correspond to fundamental
discriminants; the unique nontrivial even primitive quadratic character of
2-power conductor is the character of fundamental discriminant 8. Hence in
this branch

```text
f(epsilon)=8,
absDisc(K)>=16^2*8=2048.                              (E3)
```

Thus characteristic two supplies no hidden competitor below 125. This is
separate from `Q(zeta_8)`, whose Galois group is `C_2 x C_2` and which fails
condition 4 before the discriminant comparison.

#### Step H: lower bound and equality

Insert E1 and E2 into D:

```text
absDisc(K)=f(psi)^2 f(epsilon)>=5^2*5=125.
```

This proves E1. Equality over positive integers forces

```text
f(psi)=5 and f(epsilon)=5.                            (F)
```

The group `(Z/5Z)^x` is cyclic of order four. An exact-order-four character
on it is faithful, so its kernel is trivial. Its fixed field in
`Q(zeta_5)` therefore has degree four and is the full `Q(zeta_5)`. Thus F
implies

```text
K is Q-isomorphic to Q(zeta_5).
```

Step A gives the converse equality. This proves E2 and E3.

## 2. Code

The accepted verifier is
`probes/P-ABELIAN-CM-UNIQUE-EVEN-BIT-DISCRIMINANT-MINIMUM-1/verify.py`,
SHA-256
`955ea322ff4f59904e6d216d8bcc61e6aae5f8cbe89c9136e33a2853b51c2e34`
(11347 bytes).

It is a self-contained Python 3 standard-library program using exact integer,
rational, finite-group, and polynomial arithmetic. It has no floating point,
tolerance, randomness, argv or environment input, filesystem read or write,
network access, subprocess, dynamic code, or dependency on a prior transcript.

Its seven frozen audit gates are:

1. `GROUP-FLOOR`: enumerate `Hom(C_4,C_2)`, check that both characters kill
   the involution, exhibit its order-four root, and contrast the four maps
   from `C_2 x C_2`;
2. `MINKOWSKI`: reconstruct `M(8)` as an exact rational and audit B2 plus the
   binomial lower certificate;
3. `QUARTIC-GROUPS`: audit the involution and character counts distinguishing
   the two abelian groups of order four;
4. `SMALL-CONDUCTORS`: exhaust all homomorphisms from the unit groups at
   moduli 1 through 5 into `mu_4`, including primitiveness and parity;
5. `TWO-PRIMARY`: exhaust the primitive quadratic characters at modulus 8 and
   primitive quartic characters at modulus 16, checking parity, square
   conductor, and the 2048 floor;
6. `CONDUCTOR-PRODUCT`: audit the 125 lower product and unique integer equality
   pair `(5,5)`;
7. `ZETA-FIVE`: compute the discriminant of `Phi_5` by an exact independent
   Sylvester/Bareiss resultant and audit that 2 generates `(Z/5Z)^x`.

After the gates, the verifier writes one frozen scope line and
`RESULT 7/7 ALL PASS`. The verifier does not and cannot prove the general
character-field correspondence, conductor-discriminant theorem, or infinite
Minkowski reduction; those rest on the written proof and named classical
inputs.

Before the prospective pin the source received AST parsing and static review
only. It was not executed or imported.

## 3. Carrier and data

The theorem carrier is every `Q`-isomorphism class of finite Galois CM field
in `A`. It is not a finite catalogue. The proof reduces only a possible
smaller or tied field to degree four and then to a cyclic quartic character.

The proof carrier includes:

- every finite abelian group `G_K` meeting the two character conditions;
- CM complex conjugation as a distinguished nonidentity involution;
- every possible field degree, reduced by the exact Minkowski argument;
- the primitive Dirichlet character group attached to a cyclic quartic
  abelian field;
- every possible conductor of `psi` and `epsilon`;
- the equality field up to `Q`-isomorphism.

The audit carrier is finite and exact:

- `C_4`, `C_2 x C_2`, and all maps from them to `C_2`;
- exact rational values in the Minkowski certificate;
- all unit-group homomorphisms to `mu_4` at moduli 1 through 5, 8, and 16;
- every small-character conductor and parity value used by E1--E3;
- conductor pairs in the exact equality window;
- the integer polynomials `Phi_5` and its derivative, their Sylvester matrix,
  and the unit group modulo 5.

There is no external dataset, measured input, random seed, machine-specific
input, hidden file, or physical carrier.

## 4. Systematics

- The class `A` is frozen before any conductor or degree reduction. It may not
  be narrowed around `Q(zeta_5)` after the pin.
- `Hom(G,C_2)` includes the trivial character. Cardinality two means one
  nontrivial bit; the Klein group has cardinality four and is excluded for
  that reason.
- The evenness condition concerns the unique quadratic bit. The faithful
  quartic character is odd and must not be conflated with its even square.
- Degree four is derived only for a smaller or tied competitor. The theorem
  does not assert that every field in `A` has degree four; `Q(zeta_13)` is a
  higher-degree positive regression member removed by its discriminant.
- Minkowski supplies the infinite degree exclusion. A bounded degree scan is
  not evidence for B3.
- Kronecker--Weber, the character-field correspondence, and the
  conductor-discriminant theorem are explicit proof inputs. A finite scan of
  cyclotomic fields cannot replace them.
- `f(psi^j)` always means the conductor of the primitive character associated
  to that power. The square can be imprimitive at the original modulus.
- D is the absolute field discriminant. A defining polynomial or nonmaximal
  order discriminant is not interchangeable with it.
- The pure 2-primary branch is retained even though the general lower bound
  already excludes it. It prevents a hidden characteristic-two exception and
  separates this class from the v33 `Q(zeta_8)` control.
- Total ramification is not an admissibility premise and is not derived for
  the complete class.
- The numerical Lean notes are non-canonical and status-neutral. They are not
  a dependency or evidence source for this probe.
- Any defect in `PREREG.md` or `verify.py` after the public pin invalidates
  this probe name. The frozen files remain preserved; execution stops and a
  fresh named issue, branch, and pin are required.

## 5. Failure threshold

`THEOREM-CERTIFIED` is available only if the owner accepts the complete
written proof at exactly E1--E3, every named classical theorem is applied at
its stated scope, and every pinned audit gate passes.

A formal verifier leg passes only with exit 0, empty stderr, seven `PASS`
lines, the exact frozen `SCOPE` line, `RESULT 7/7 ALL PASS`, and stdout
byte-identical to the single committed `EXPECTED.txt` in both required GitHub
architectures.

`NEGATIVE` fires on an exact witness to any of the following:

1. a field `K in A` has `absDisc(K)<125`;
2. a field `K in A`, not `Q`-isomorphic to `Q(zeta_5)`, has
   `absDisc(K)=125`;
3. `Q(zeta_5)` fails an admissibility condition or has discriminant other
   than 125;
4. the quarter-turn, degree divisibility, Minkowski reduction, cyclic-quartic
   reduction, character correspondence, conductor-discriminant identity,
   conductor lower bound, pure 2-primary control, or equality-field
   identification is false.

`STOP` applies to unclear authority, a collision, an incomplete proof, an
unnamed or misapplied classical theorem, a field/order discriminant mismatch,
a dependency used above scope, a pin/hash/byte failure, an invalid verifier,
nonempty stderr, nonzero exit without an exact scientific witness, or any
attempted post-pin movement of the class, equation, proof inputs, systematics,
threshold, falsifier, or layer.

Every fired scientific falsifier is preserved. A verifier defect, transcript
mismatch, or architecture mismatch without an exact mathematical negation is
integrity STOP, not automatically a scientific `NEGATIVE`.

## 6. Action layer and scope firewall

Action layer: **L1 exact arithmetic only**.

The proof acts on finite Galois groups, number fields, Dirichlet characters,
conductors, and discriminants. It defines no map into L2--L6 and names no
cross-layer gate.

NO CLAIM:

- that the admissible class `A` is physically selected;
- that abelianity, the CM condition, the exactly-one-bit condition, or
  evenness is uniquely forced by `J`, the architecture, or the decoder;
- that discriminant minimization is a physical law;
- that total ramification is necessary for admissibility;
- that `J` is derived after the field is selected;
- that the minimum selects a unique embedding, root of unity, unit, or
  oriented mixed step inside `Q(zeta_5)`;
- that `TWO-PLACE-PHYSICS [D]` moves;
- any decoder, Born measure, physical bit, clock, force, observable, SI, or
  empirical conclusion;
- any lift from L1 to L2--L6.

The proposed theorem does not depend on a physical dictionary. Any later
claim that Nature adopts the admissibility conditions or the discriminant
minimum requires a separate registered hypothesis and falsifier. Any later
derivation of `J` requires a separate exact internal selector after the field
has been selected.
