# P-QDD-J-CENTRALIZER-TERMINALITY-1 preregistration

Date: 2026-08-20

Author of record: A. M. Thorn

Status: preregistered protocol only. No scientific result is earned by this
file. The accepted verifier has formal execution count zero. It may not be
imported or executed before this file, `verify.py`, and `exact_matrix.py` are
committed together, pushed, and read back byte for byte from the public remote.

Public claim lock: issue 459.

## Authority

```text
STATE:          ACTIVE
CANON:          Public Canon v56
AUTHORITY:      mathorn1973/twist-j main
TAG:            canon-v56
CONTENT_COMMIT: b36c93ed8ce24a9cbd771168094db04f5a5ac06c
CANON_SHA256:   b284ed6e78341aa6e3a74652d6f1f8f4079c270461f28bf32f2d95a6bd8b6645
CANON_BYTES:    288492
BASE_COMMIT:    2fbee86973a5372bf0c96ddbd39b1610fecf72e2
```

Target: blocker O2 of `QDD-INSTRUMENT-APPARATUS [O]` only.

The active row requires a target-independent apparatus class and physical
selection law. This probe classifies one complete restricted J-native class
and tests two distinct statements inside it:

1. the negative statement that reversibility, affine covariance, ordinary
   outcome repeatability, memory preservation, and exact effects remain
   nonselective;
2. the positive conditional statement that exact fresh-pointer terminality
   selects the Lueder physical class, and strict branch idempotence fixes its
   positive representative.

This probe does not claim that the declared public architecture already
implies terminality, and it does not claim that the restricted class below is
the class of every conceivable J-native apparatus. Global O2 therefore cannot
close from this probe alone.

## Result-exposure disclosure

Before issue 459, NON-CANONICAL chat reasoning derived the expected rational
centralizer shape `Q direct-sum Q(i)`, anticipated an infinite rational-circle
family, anticipated two physical classes in the self-adjoint involutive
subclass, and observed that branch terminality should select the identity
member. Those calculations are discovery context only. Every earlier
calculation, matrix, count, transcript, and witness is excluded from formal
evidence.

The sealed predecessor `P-QDD-J-AFFINE-APPARATUS-1` exhibited a four-member
multiplier subclass. It is lineage and a boundary control. This probe
reconstructs the J simplex and affine representation from the public formulas
and proves the larger centralizer classification independently. Its
`exact_matrix.py` utility is a freshly pinned copy of the same elementary
Fraction-arithmetic design, but no predecessor verifier or output is imported
or executed.

Static source inspection and syntax parsing are allowed before the pin.
Scientific execution is forbidden.

The written proofs below are frozen protocol content. The verifier audits them;
a finite witness list does not replace their quantifiers.

## Field 1: equation

### 1. Primitive J data

Work over

```text
V = Q^4,
one = (1,1,1,1)^T,
G = I_4 - (1/5) one one^T,
D = M_J - I_4.
```

Here `M_J` is the public multiplication-by-J matrix. Since `J-1=zeta_5^2`,
`D` is multiplication by `zeta_5^2`, hence

```text
D^5 = I_4,
D^T G D = G.
```

Put

```text
u_x = D^x e_0,                     x in F_5.
```

The exact rational simplex identities are

```text
sum_x u_x = 0,
<u_x,u_y>_G = 4/5 if x=y and -1/5 otherwise.
```

For `c in F_5^x` and `b in F_5`, let `rho(c,b)` be the unique rational map

```text
rho(c,b) u_x = u_(b+cx).
```

These twenty maps form a faithful G-orthogonal representation of
`AGL_1(F_5)`.

### 2. Stabilizer decomposition, before target comparison

For each memory token `k in F_5`, define its complete multiplier stabilizer

```text
H_k = {h_(a,k): x -> k + a(x-k), a in F_5^x}
```

and its fixed-space average

```text
P_k = (1/4) sum_(a in F_5^x) rho(h_(a,k)),
Q_k = I_4 - P_k.
```

The group average is the G-orthogonal projector onto the fixed line `Q u_k`.
Thus

```text
P_k^2=P_k=P_k^sharp, rank(P_k)=1,
Q_k^2=Q_k=Q_k^sharp, rank(Q_k)=3,
P_k Q_k=Q_k P_k=0.
```

Here `A^sharp=G^-1 A^T G`.

Let

```text
g_k = rho(h_(2,k)).
```

The map `g_k` has order four. On the sum-zero simplex module its characteristic
polynomial is

```text
(x-1)(x+1)(x^2+1).
```

The `x=1` line is exactly `im(P_k)`. Define, without naming or reading any QDD
target effect,

```text
R_k = (1/4)(I - g_k + g_k^2 - g_k^3),
C_k = Q_k - R_k,
J_k = g_k C_k.
```

Then

```text
rank(R_k)=1, rank(C_k)=2,
R_k^2=R_k=R_k^sharp,
C_k^2=C_k=C_k^sharp,
R_k C_k=C_k R_k=0,
Q_k=R_k+C_k,
J_k C_k=C_k J_k=J_k,
J_k^2=-C_k,
J_k^sharp=-J_k,
R_k J_k=J_k R_k=0.
```

`R_k` is the rational sign component and `C_k` is the irreducible
`x^2+1` component.

### 3. Complete rational centralizer theorem

Freeze the admissible moving-branch algebra at token `k` as

```text
Z_k = {
  T in End_Q(V):
  T P_k=P_k T=0 and
  T rho(h)=rho(h) T for every h in H_k
}.
```

It is enough to commute with `g_k`, because `H_k=<g_k>`.

The squarefree primary decomposition of `Q_k V` is

```text
Q_k V = R_k V direct-sum C_k V,
minimal polynomials x+1 and x^2+1.
```

Every rational commutant map preserves both summands. On the one-dimensional
sign summand it is one rational scalar. On the irreducible two-dimensional
summand the commutant is the field

```text
Q[g_k C_k] = Q C_k direct-sum Q J_k isomorphic to Q(i).
```

Therefore

```text
Z_k = Q R_k direct-sum Q C_k direct-sum Q J_k
```

and every member has one unique expression

```text
T_k(e,r,s) = e R_k + r C_k + s J_k.
```

This is a theorem over Q. The verifier independently constructs all linear
commutation and support equations on the sixteen matrix entries, obtains
nullity three at all five tokens, and verifies that `R_k,C_k,J_k` are a basis.
That finite linear-algebra audit supports, but does not replace, the primary
decomposition proof.

The exact effect equation is

```text
T_k^sharp T_k = Q_k.
```

Using the multiplication table above gives

```text
T_k^sharp T_k = e^2 R_k + (r^2+s^2) C_k.
```

Hence the complete admissible orthogonal centralizer class is exactly

```text
e in {+1,-1},
r,s in Q,
r^2+s^2=1.
```

There is no fitted parameter. The rational circle is the complete solution set
to the frozen rational orthogonality equations.

### 4. Affine covariance, pointer, and memory

Affine transport satisfies

```text
rho(c,b) P_k rho(c,b)^-1 = P_(b+ck),
rho(c,b) R_k rho(c,b)^-1 = R_(b+ck),
rho(c,b) C_k rho(c,b)^-1 = C_(b+ck),
rho(c,b) J_k rho(c,b)^-1 = J_(b+ck).
```

Therefore one coefficient triple `(e,r,s)` defines one complete covariant
family across all memory tokens.

Use a binary pointer with ready state `p_0`, record state `p_1`, and flip
`X p_0=p_1`, `X p_1=p_0`. Use a five-token orthonormal memory basis `m_k`.
Define

```text
U_(e,r,s)
 = sum_(k in F_5)
   [P_k tensor I_2 + T_k(e,r,s) tensor X]
   tensor |m_k><m_k|.
```

The class builder uses only `M_J`, `D`, `G`, `F_5`, the complete affine action,
the stabilizers, the binary pointer, and the five-token memory. The target
effect names, target matrices, target weights, and target token are forbidden
inputs.

Every member is rational, reversible, memory-preserving, pointer-no-leakage,
and fully affine-covariant:

```text
U_(e,r,s)^sharp U_(e,r,s)=I,
A_(c,b) U_(e,r,s)=U_(e,r,s) A_(c,b),
```

where `A_(c,b)` transports the system and memory token together.

Preparing `p_0,m_k` and reading the pointer gives

```text
K_0(k)=P_k,
K_1(k)=T_k(e,r,s),
K_0^sharp K_0=P_k,
K_1^sharp K_1=Q_k,
K_0^sharp K_1=0.
```

### 5. Negative route: exact nonselection

The public post-state equivalence inherited from
`QDD-INSTRUMENT-NONSELECTION` is

```text
K ~_post L iff K=+L or K=-L
```

inside one nonzero effect fibre.

For every finite `t in Q`, put

```text
e_t=1,
r_t=(1-t^2)/(1+t^2),
s_t=2t/(1+t^2).
```

Then `r_t^2+s_t^2=1`. If `T(t)=+T(u)`, uniqueness of the centralizer
coordinates gives equal circle coordinates, and

```text
t=s_t/(1+r_t)
```

gives `t=u`. If `T(t)=-T(u)`, comparison of the `R_k` coefficient gives
`1=-1`, impossible. Thus

```text
Q injects into the physical post-state classes
```

at every fixed token and, after target comparison, at the frozen target
effects. The class is infinitely nonselective.

Ordinary outcome repeatability is also nonselective. For every class member,

```text
P_k K_0=K_0,
Q_k K_1=K_1.
```

A fresh repetition therefore returns the same outcome with certainty, but the
state inside the high branch can still be rotated.

The self-adjoint condition is `s=0`. Together with orthogonality it gives
`r=+1` or `r=-1`, while `e=+1` or `e=-1`. Hence there are four algebraic
self-adjoint involutive members:

```text
(e,r) in {(+1,+1),(+1,-1),(-1,+1),(-1,-1)}.
```

Modulo `T ~_post -T`, exactly two physical classes remain:

```text
[R_k+C_k] = [Q_k],
[R_k-C_k].
```

The first is the Lueder class after target comparison. The second is
inequivalent. Thus reversibility, full affine covariance, ordinary
repeatability, self-adjointness, and involutivity still do not select Lueder.

### 6. Positive route: operational and strict terminality

This route does not assume a target projector. It asks a fresh identical
apparatus to act again after one branch result.

#### 6a. Fresh-pointer ray terminality

For the moving branch require, uniformly for every token,

```text
Post_T(Tv)=Post_T(v)
```

for every input of nonzero branch weight. Equivalently, `T^2 v` and `T v`
span the same rational line.

Since `T` is invertible on the three-dimensional space `Q_k V`, put `w=T v`.
The condition says `T w` lies on the line `Q w` for every nonzero `w`.
A linear map on a space of dimension at least two that preserves every line is
a scalar. Therefore

```text
T=lambda Q_k.
```

The effect equation gives `lambda^2=1`, hence

```text
T=+Q_k or T=-Q_k.
```

These two maps are one physical post-state class under the registered sign
equivalence. Fresh-pointer ray terminality therefore selects exactly the
Lueder physical class inside the complete centralizer class.

#### 6b. Strict branch terminality

The issue's strict frozen threshold is

```text
P_k^2=P_k,
T_k^2=T_k
```

for every token. On `Q_k V`, `T_k` is invertible, so `T_k^2=T_k` implies
`T_k=Q_k`. Equivalently, comparison of the primary coefficients gives

```text
e^2=e with e^2=1, so e=1,
(r+s i)^2=(r+s i) with r^2+s^2=1, so r+s i=1.
```

Thus

```text
e=1, r=1, s=0,
T_k=Q_k
```

for every token. Strict terminality fixes the positive representative.

Both terminality results are conditional mathematical theorems. This probe
does not adopt terminality as a physical law and does not claim it follows from
`J`, `Omega`, `U`, decoder terminality, no-feedback, or any current apparatus
row. A future derivation of terminality requires a separate typed public
bridge.

### 7. Target comparison, deliberately last

Only after the class, its completeness, both routes, and all decision
conditions are frozen, compare with the public ordered QDD effects

```text
E_low=(1/4) one one^T,
E_high=I_4-E_low.
```

The simplex identity `u_2=-one` gives

```text
P_2=E_low,
Q_2=E_high.
```

Therefore every class member realizes the same frozen ordered effects and
occurrence weights at memory token `k=2`. The member

```text
e=1, r=1, s=0
```

gives

```text
K_low=E_low,
K_high=E_high,
```

the Lueder pair.

## Field 2: code

Accepted exact files:

```text
probes/P-QDD-J-CENTRALIZER-TERMINALITY-1/verify.py
probes/P-QDD-J-CENTRALIZER-TERMINALITY-1/exact_matrix.py
```

Requirements:

```text
Python standard library only
integers and Fraction only
no float, Decimal, complex approximation, randomness, subprocess, network,
external dataset, imported predecessor verifier, or imported scratch output
zero arguments
deterministic stdout
empty stderr
```

The verifier audits:

1. the J phase motor and five-vertex simplex;
2. all twenty affine maps and all five stabilizers;
3. all five `P,R,C,J` decompositions and their multiplication tables;
4. the complete forty-eight-equation rational centralizer system at every
   token and nullity three;
5. affine transport of the three centralizer basis elements;
6. exact reversible 40-dimensional couplings on representative rational-circle
   points;
7. exact branch effects, support, ordinary repeatability, and pointer
   reduction;
8. an injective finite audit subset of the rational-circle family;
9. the four self-adjoint involutive members and their two sign-quotient classes;
10. the ray-terminality physical quotient;
11. strict idempotence;
12. target comparison only after all class gates.

Universal completeness, infinitude, and terminality statements rest on the
written proofs.

## Field 3: carrier or data

No external data.

```text
system        (Q^4,G)
pointer       (Q^2,I_2)
memory        (Q^5,I_5)
total         Q^4 tensor Q^2 tensor Q^5, dimension 40
class field   Q and the rational norm-one circle in Q(i)
```

All source matrices are reconstructed from the displayed public J-step and
the five-label affine action.

## Field 4: systematics and completeness

There is no measurement systematic.

Frozen exact obligations:

```text
C1  authority constants and target-independence source guard;
C2  phase motor, simplex sum, Gram, and u_2 identities;
C3  complete AGL_1(F_5) action and group law;
C4  all five stabilizer averages and 1+3 support split;
C5  all five R+C and J multiplication tables;
C6  sixteen-variable centralizer nullity three at all five tokens, with
    R,C,J a complete basis;
C7  affine transport and one common coefficient triple across memory;
C8  effect equation iff e^2=1 and r^2+s^2=1;
C9  reversible covariant pointer-memory coupling and exact branch reduction;
C10 rational-circle physical injection and ordinary-repeatability nonselection;
C11 self-adjoint involutive classification, four algebraic and two physical;
C12 ray terminality gives one physical class represented by +/-Q;
C13 strict idempotence gives exactly +Q;
C14 target comparison last, P_2=E_low and Q_2=E_high.
```

A hidden target input, omitted centralizer solution, incomplete rational
parameterization, target comparison before class completion, floating
tolerance, pre-pin execution, imported predecessor output, unnamed layer lift,
post-pin threshold change, or result-dependent route change is STOP.

## Field 5: decision, falsifiers, and routing

No tolerance exists.

```text
BIFURCATION-PASS
  C1-C14 pass; the complete class is infinitely NONUNIQUE without
  terminality; ray terminality selects one physical Lueder class; strict
  terminality fixes +Q.

CENTRALIZER-F
  an exact counterexample breaks the primary decomposition, three-dimensional
  commutant, basis, orthogonality parameterization, or affine transport.

NONSELECTION-F
  an exact counterexample breaks the rational injection, ordinary
  repeatability, self-adjoint involutive classification, or physical quotient.

TERMINALITY-F
  a non-Lueder physical class satisfies ray terminality, a nonidentity member
  satisfies strict branch idempotence, or the identity member fails either
  condition.

TARGET-F
  P_2 or Q_2 differs from the frozen target effect, or a class member fails the
  exact target effect equation.

STOP
  authority, collision, target independence, pin, exactness, completeness,
  evidence, deterministic output, security, or layer discipline fails.
```

If `BIFURCATION-PASS` is earned, the maximum later-fold candidates are:

```text
QDD-J-CENTRALIZER-APPARATUS-CLASS [T]
  the complete frozen rational orthogonal stabilizer-centralizer class and its
  affine pointer-memory realization;

QDD-J-CENTRALIZER-NONSELECTION [T]
  the class has infinitely many target-realizing post-state classes; ordinary
  repeatability is nonselective; the self-adjoint involutive subclass still
  has two physical classes;

QDD-J-TERMINALITY-SELECTION [T]
  fresh-pointer ray terminality selects the Lueder physical class and strict
  branch idempotence fixes its positive representative.
```

All three scopes are restricted to this exact L4 class. They do not close
global O2.

The threshold, class, equality, and route cannot move after the immutable pin.

## Field 6: action layer

```text
L4 apparatus/support only.
```

No L5 realized-event stream and no L6 measure are produced.

```text
SAMPLING NOT PROVIDED
```

is the only permitted sampling statement. O1 is untouched.
`QUADRATIC-DECODER-DATA [O]`, decoder completion, SI metrology, Bell causal
accounting, and every other owner remain unchanged.

## Formal sequence after the pin

1. Commit and push this file and the two accepted Python files together.
2. Read all three back from the public remote and record the immutable pin,
   SHA-256, byte counts, Git blobs, inventory, and parent on issue 459.
3. Only after that readback execute exactly once:

   ```text
   python3 probes/P-QDD-J-CENTRALIZER-TERMINALITY-1/verify.py
   ```

   from a clean checkout of the pin.
4. Record exact stdout, empty stderr, exit code, platform, architecture, Python,
   hashes, bytes, and line count.
5. Commit `EXPECTED.txt`, `RUN.md`, and `RESULT.md` without changing any pinned
   file.
6. Open one pull request changing only this probe directory. Require public
   x86_64 and aarch64 jobs to reproduce one committed stdout byte for byte.
7. Preserve any scientific falsifier or STOP first-class.
8. Merge only by merge commit. No squash, rebase, amend, force-push, or Canon
   edit.
