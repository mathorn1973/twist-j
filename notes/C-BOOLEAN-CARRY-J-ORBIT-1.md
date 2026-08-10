# C-BOOLEAN-CARRY-J-ORBIT-1

**Title:** Boolean carry and conditional J-orbit compatibility

**Status:** NON-CANONICAL INCUBATION NOTE. No public T/D/C/H/O/F status is created here.

**Date:** 2026-08-10

**Owner lock:** issue #317

**Layer:** L1 algebra only.

**Purpose:** preserve the strongest exact Boolean-to-J compatibility statement that survives adversarial review, while exposing every bridge premise and every method ceiling.

This Note changes no Canon, Registry, Frontier, dependency, gate, evidence, verifier, status, release, decoder, or layer assignment.

---

## 0. Public authority and readback

At creation the public authority is:

```text
STATE:          ACTIVE
CANON:          Public Canon v39
AUTHORITY:      mathorn1973/twist-j main
TAG:            canon-v39
CONTENT_COMMIT: ab17b10412d03bf1cd69791fe22c66252502b2d4
CANON_SHA256:   698df2212f0bc782de2fb50ff04fb4026d1e276743d6fae7f10607cca770b556
CANON_BYTES:    187370
BASE_MAIN:      4d8558356f2f945b34e9f7fece323771d266585a
```

`canon-v39` resolves to `2d4ee6956f2da6f8ab23b7471ad7fcd73f787fa1`. Both the tag and the declared content commit are ancestors of `BASE_MAIN`.

The current `canon/SHA256SUMS` contains exactly five normative hashes. The reviewed public workflow on the latest main ancestry ran `tools/check_canon.py` successfully on both required architectures. That checker recomputes the SHA-256 of exactly

```text
canon/CANON.md
canon/CORE.md
canon/FRONTIER.md
canon/REGISTRY.tsv
canon/CHANGELOG.md
```

and rejects any mismatch or incomplete manifest. It also verifies the `STATUS.md` Canon hash, byte count, and content-commit ancestry. This supplies the required 5/5 normative hash readback for this notes-stage basis.

The six public rows used below were read from current `canon/REGISTRY.tsv` and are unchanged:

```text
RAMIFIED-TM-LIFT        T
CARRY-PENTAD            T
C20-TEICHMULLER-SPLIT  T
QUBIT-FROM-F5           T
J-STEP                  T
J-PROJECTIONS           T
```

No status in this Note exceeds those registered scopes.

---

## 1. Scope correction: Boolean-ring normal form, not minimal functional basis

The primitive grammar

```text
{1, XOR, AND}
```

is **not** a minimal functionally complete basis. NAND alone is functionally complete.

The relevant exact property is instead the Boolean-ring algebraic normal form.
For `n` Boolean variables,

```text
B_n = F_2[x_1,...,x_n] / (x_i^2-x_i : 1<=i<=n).
```

Every Boolean function `f:F_2^n->F_2` has one and only one multilinear polynomial representation

```text
f(x) = XOR_(S subset {1,...,n}) a_S AND_(i in S) x_i,
a_S in F_2,
```

with the empty monomial equal to `1`. This is the Zhegalkin or algebraic normal form.

The displayed ring-polynomial grammar is irredundant for expressing all Boolean functions:

```text
without 1:    every generated function preserves 0;
without AND:  only affine Boolean functions are generated;
without XOR:  every generated function is monotone, hence NOT is absent.
```

No uniqueness claim is made among all possible functionally complete signatures. The uniqueness is the uniqueness of algebraic normal form in the Boolean-ring signature.

The scope is finite Boolean functions. A finite-state transition map may be represented componentwise by Boolean functions after choosing a finite Boolean encoding and, when needed, an extension from the encoded state subset to a Boolean cube. Such an encoding or off-subset extension is not claimed canonical.

---

## 2. The normalized carry extension

Let

```text
B = C_2 = F_2 = {0,1}.
```

Write

```text
a XOR b = a+b in F_2,
a AND b = ab in F_2.
```

The integer sum of two bits obeys

```text
a+b = (a XOR b) + 2(a AND b).
```

The coefficient `2` is universal and unique: the case `a=b=1` forces it.
This is the exact arithmetic clause already contained in `RAMIFIED-TM-LIFT [T]` at its registered scope.

Now consider central extensions with trivial action

```text
0 -> C_2 -> E -> C_2 -> 0.
```

Fix a normalized section `s(0)=0`. A normalized two-cocycle

```text
c:C_2 x C_2 -> C_2
```

satisfies

```text
c(0,a)=c(a,0)=0.
```

Its only free value is therefore `c(1,1)`. Exactly two normalized cocycles exist:

```text
c_0(a,b)=0,
c_1(a,b)=ab=a AND b.
```

For a normalized one-cochain `f:C_2->C_2`, `f(0)=0`,

```text
delta f(1,1)=f(1)+f(1)-f(0)=0 in C_2,
```

and all other normalized values vanish as well. Hence every normalized coboundary is zero.

Therefore

```text
H^2(C_2,C_2) ~= C_2,
```

and `AND` is stronger than merely a representative of the nontrivial class:

```text
AND is the unique nonzero normalized representative.
```

For the nontrivial cocycle, the lift `x=s(1)` satisfies

```text
2x = kappa != 0,
4x = 0,
```

where `kappa` is the nonzero kernel element. Thus `x` has exact order four and the nonsplit extension is

```text
E ~= C_4.
```

### Exact Boolean theorem

```text
The Boolean-ring carry law has one unique nontrivial normalized central
C_2-extension. Its group is C_4 and its normalized carry cocycle is AND.
```

This theorem uses no prime, finite field, cyclotomic field, or TWIST-J input.

---

## 3. Characteristic-two obstruction

Suppose the carry group `C_4` is required to occur multiplicatively inside a finite field of characteristic two.
Every such field has cardinality `2^k`, hence

```text
|F_(2^k)^x| = 2^k - 1,
```

which is odd for every positive integer `k`.
Therefore

```text
4 does not divide |F_(2^k)^x|
```

for any `k`, and no finite field of characteristic two can contain an element of order four multiplicatively.

Thus, **conditional on demanding multiplicative field realization of the carry group**, the binary characteristic cannot host its own nonsplit carry extension.

This does not yet select characteristic five. It only proves the characteristic-two no-go inside the declared finite-field multiplicative class.

---

## 4. Bridge premise B1: EXACT-CARRY-GROUP

The first bridge premise is deliberately rigid rather than optimizing.

### EXACT-CARRY-GROUP

Require the carry extension group itself to be the complete multiplicative group of a finite field:

```text
K^x ~= C_4.
```

For a finite field `K=F_q`,

```text
|K^x| = q-1.
```

Hence

```text
q-1=4,
q=5.
```

Therefore

```text
K = F_5,
F_5^x ~= C_4.
```

There is no minimization rule here. The field is unique because the entire multiplicative group, not merely a subgroup, is frozen to be the exact carry group.

Choose `g=2`. Then

```text
g^2=-1,
g^4=1,
F_5^x=<g>.
```

For bits `a,b`, the carry extension is encoded in one multiplication:

```text
g^a g^b = (-1)^(a AND b) g^(a XOR b).
```

Equivalently:

```text
XOR = the quotient operation in F_5^x/{+-1};
AND = the central sign cocycle of the normalized section {0,1}->{1,g}.
```

The public rows supply the TWIST-J compatibility:

```text
J_lambda = [J] mod (1-zeta_5) = 2 = g,
F_5^x/{+-1} ~= C_2.
```

Thus

```text
J_lambda^a J_lambda^b
  = (-1)^(a AND b) J_lambda^(a XOR b).
```

### Conditional theorem B1

```text
Under EXACT-CARRY-GROUP, the unique normalized Boolean carry extension C_4
is realized by the complete multiplicative group F_5^x, and the registered
ramified image J_lambda=2 realizes a generator of that group.
```

No physical carry/J identification follows.

---

## 5. Price of B1: the Gaussian integer control

`EXACT-CARRY-GROUP` is a real premise. Its force disappears when the carrier class is widened.

If finite fields are replaced by rings of integers of number fields, then

```text
Z[i]^x = {+-1,+-i} = mu_4 ~= C_4.
```

The Gaussian integers therefore realize the same abstract carry group as their full unit group in characteristic zero. Their field discriminant is

```text
Disc(Q(i)) = -4.
```

Nothing in the Boolean carry extension alone excludes this route or forces a pentagonal additive carrier.

This is not a falsifier of the conditional B1 theorem. It is the explicit **price of the finite-field premise** and blocks any broader claim that Boolean carry by itself selects `F_5` or `Q(zeta_5)`.

The public TWIST-J field-selection theorems are stronger but separate statements. In particular, the current Canon has independent quartic-cyclotomic total-ramification and abelian-CM discriminant-minimum results. They are not imported here as a hidden replacement for B1 and are not physical-selection theorems.

---

## 6. Bridge premise B2: SAME-FIELD-ADD

After B1 has selected the finite field `F_5` by its multiplicative group, introduce a second explicit premise.

### SAME-FIELD-ADD

Use the additive group of the **same field** as the regular cycle carrier:

```text
(F_5,+) ~= C_5.
```

This step is not a consequence of the Boolean carry extension or of the multiplicative realization alone. It is a separate bridge premise.

Let `C` be a generator of the regular additive five-cycle. Its integral augmentation lattice is

```text
A_4 = ker(epsilon:Z[C_5]->Z),
rank_Z(A_4)=4.
```

On `A_4`,

```text
C^5=I,
char_C(X)=Phi_5(X).
```

The registered `CARRY-PENTAD [T]` identifies this lattice with

```text
(zeta_5-1) Z[zeta_5]
```

and identifies `C` with multiplication by `zeta_5`.

---

## 7. Binary two-support lift class

Freeze the integral binary-support grammar

```text
T_S = sum_(r in S) C^r,
S subset Z/5Z,
```

with coefficients only in `{0,1}`.

Require that the induced action on the ramified coinvariant

```text
A_4/(C-I)A_4 ~= F_5
```

be the universal carry coefficient `2`.

Since every `C^r` acts as `I` on the coinvariant,

```text
T_S -> |S| I mod 5.
```

Because `0<=|S|<=5`, the condition

```text
|S| = 2 mod 5
```

forces exactly

```text
|S|=2.
```

Therefore every admitted lift is

```text
T = C^a + C^b,
a != b.
```

No support point is assumed to be the identity.

Factor

```text
T = C^a (I + C^(b-a)).
```

This must be interpreted with the correct equivalence.

### Unnormalized class

Multiplication by `C^r` is a torsion-unit twist, not integral conjugation.
Together with cycle automorphisms

```text
C -> C^u,
u in (Z/5Z)^x,
```

the affine group of the five-cycle acts transitively on two-element supports.
Thus all admitted unnormalized two-support lifts form one class under

```text
mu_5 twist + C_5 automorphism.
```

This is **not** an integral-conjugacy statement.

### Support-normalized class

Translate one support point to zero. Every support becomes

```text
{0,d},
d in (Z/5Z)^x,
```

and every operator becomes

```text
I+C^d.
```

The integral coordinate automorphisms satisfy

```text
g_u C g_u^-1 = C^u.
```

Hence all `I+C^d` are integrally conjugate. Under the cyclotomic identification,

```text
I+C^d <-> 1+zeta_5^d.
```

The normalized lifts therefore form one integral/Galois orbit

```text
{1+zeta_5^d : d in (Z/5Z)^x}.
```

The public representative is

```text
I+C^2 ~=_Z M_J,
J=1+zeta_5^2.
```

### Conditional theorem B1+B2

```text
Assume EXACT-CARRY-GROUP, SAME-FIELD-ADD, and the binary two-support
augmentation-two lift grammar. Then the admitted unnormalized operators form
one class modulo mu_5 twist and C_5 automorphism. After support normalization
they form one integral-conjugacy and Galois orbit represented by M_J / J.
```

This is the strongest theorem claimed by this Note.

---

## 8. Method ceiling: the Boolean branch reaches [J], not J

The normalized integral/Galois construction cannot select the exponent `d=2`.
The Galois group acts transitively on

```text
{1+zeta_5^d : d in (Z/5Z)^x}.
```

Therefore every Galois-invariant predicate is constant on the orbit and cannot select one exponent.

The public `J-PROJECTIONS [T]` orientation enters only after choosing the principal archimedean embedding. In embedding notation,

```text
|sigma_a(J)| = phi^(-chi_5(a)).
```

Thus the four embeddings split into contracting and expanding conjugate pairs according to the quadratic character. In the principal embedding,

```text
|J| = phi^-1,
arg(J) = 2 pi/5.
```

That archimedean orientation selects the displayed representative used by the public axiom. It is not derived from the Boolean carry chain.

Hence the method ceiling is structural:

```text
Boolean/integral/Galois route -> [J]
archimedean orientation       -> displayed J representative.
```

This is not an unfinished integral invariant search. A Galois-invariant method cannot break a transitive Galois orbit.

---

## 9. Order-twenty consistency note only

The registered `C20-TEICHMULLER-SPLIT [T]` proves in

```text
R=Z[zeta_5]/(5)
```

that the public `J` has order twenty and that its generated subgroup splits as

```text
<J> ~= C_4 x C_5.
```

This is compatible with the Boolean `C_4` and additive `C_5` ingredients, but it has essentially no selection force.

Indeed, for every nonzero `d mod 5`, characteristic five gives

```text
(1+zeta_5^d)^5 = 2.
```

Moreover

```text
R^x ~= C_4 x C_5^3.
```

The principal-unit factor has exponent five because `R` has characteristic five and nilpotence depth four. Therefore the number of elements of exact order twenty is

```text
phi(4) * (5^3-1)
= 2 * 124
= 248.
```

Thus

```text
order 20,
fifth power 2,
ramified residue 2
```

are consistency checks only. They do not select `J` from its conjugates or from the wider unit group.

---

## 10. Reconnaissance disclosure

A separate one-platform exact-arithmetic reconnaissance was reported before this Note:

```text
reported grade: candidate-C
reported result: 35/35 PASS
file sha256:     5a22fdbaa6fd9d86bed847f695b1c812aec31564328abfbc503ee8af04eb55e8
stdout sha256:   7b71633d5565f3f6c7f53c2945ee2f9774bc7174b583e3772f519bfe3e26199c
```

The corresponding bytes are not imported into this repository object and were not independently reproduced in this session. The run is therefore provenance only. It is not public evidence and does not raise the Note above NON-CANONICAL status.

No verifier is required for this Note under `POLICY.md`. Any later formal theorem claim must be freshly named and prospectively preregistered.

---

## 11. Falsifiers of the conditional implications

The following are genuine mathematical falsifiers of the scoped implications:

```text
F1  a second nonzero normalized representative exists for the nontrivial
    class in H^2(C_2,C_2);

F2  a normalized coboundary changes c(1,1);

F3  the nonsplit normalized extension is not C_4;

F4  a finite field K with K^x ~= C_4 has |K| != 5;

F5  a finite characteristic-two field contains an element of multiplicative
    order four;

F6  the binary-support augmentation-two class contains a support whose
    cardinality is not two;

F7  two support-normalized operators I+C^d lie in distinct integral
    conjugacy classes;

F8  I+C^2 is not integrally conjugate to the registered M_J;

F9  the unnormalized mu_5 twist equivalence is misidentified with integral
    conjugacy;

F10 a Galois-invariant predicate is claimed to select one member of the
    transitive normalized J orbit.
```

The Gaussian integer route is **not** in this falsifier list because rejecting or widening a bridge premise does not falsify a conditional theorem. It is recorded in Section 5 as the price and scope boundary of B1.

---

## 12. Nonclaims

This Note does not claim:

```text
{1,XOR,AND} is a minimal functionally complete basis;
Boolean algebra represents arbitrary first-order or arithmetic formal systems;
Boolean algebra alone derives F_5;
Boolean algebra alone derives Q(zeta_5);
EXACT-CARRY-GROUP is physically forced;
SAME-FIELD-ADD is physically forced;
the finite-field carrier class is uniquely forced;
the binary two-support grammar is uniquely forced;
the Gaussian integer route is excluded by Boolean data;
unnormalized two-support operators are all integrally conjugate;
integral or Galois data select d=2;
order twenty selects J;
physical carry is a physical J action;
the global architecture (Omega,U,selector,D) follows from this Note;
any decoder, spacetime, force, measure, SI, or L2-L6 result.
```

The value of the Note is narrower and exact:

```text
Boolean carry fixes the normalized nonsplit C_4 extension rigidly.
Under two explicit bridge premises and one explicit lift grammar, that C_4
route meets the already registered TWIST-J construction at the normalized
integral/Galois orbit [J].
```

---

## 13. Promotion boundary

This Note earns no public status.

A future public theorem must:

1. use a new public claim identifier;
2. freeze `EXACT-CARRY-GROUP`, `SAME-FIELD-ADD`, and the binary-support lift class at the top of scope;
3. preserve the characteristic-two no-go and Gaussian-integer scope control;
4. distinguish unnormalized torsion twist from integral conjugacy;
5. preserve the archimedean method ceiling `[J]` versus `J`;
6. treat the order-twenty material only as a consistency check;
7. disclose the reported 35/35 one-platform reconnaissance as prior result exposure;
8. preregister any accepted verifier before execution;
9. treat any verifier as an audit if theorem status rests on the written proof.

Any future wording that Boolean algebra alone derives `p=5`, `Q(zeta_5)`, or the oriented representative `J` is outside this Note and must be rejected or separately proved.
