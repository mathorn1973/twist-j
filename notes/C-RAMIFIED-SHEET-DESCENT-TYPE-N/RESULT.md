# RESULT C-RAMIFIED-SHEET-DESCENT-TYPE-N

**Status:** NON-CANONICAL incubation result.

```text
LEVEL A  candidate-T / L4 exact algebra:
         square-class sheet = minimal Hermitian-square descent type
LEVEL B  candidate-D / unpromoted algebraic comparison at p=5:
         the descent bit lands in the existing sign quotient V_+
LEVEL C  STOP:
         no public physical or decoder map owns this source carrier
```

No Canon, Registry, Frontier, dependency, gate or public status changes.

## 1. Verdict

The square-class distinction has a canonical independently defined algebraic meaning.

It tells whether a nonradical null Hermitian form is already a Hermitian square over the first ramified neighborhood, or becomes one only after quadratic scalar extension of the residue field.

It does not presently have a physical meaning in TWIST-J.

## 2. Exact factorization theorem

Let `p` be odd, let

```text
E_m=B_(p,m)/eps B_(p,m)=F_(p^m),
B_(p,m)=E_m[eps]/(eps^2),
bar(a+b eps)=a-b eps,
```

and let

```text
X=X(a,b,c,d)
 = [[a,c+d eps],[c-d eps,b]]
```

be a nonradical null Hermitian form defined over `B_(p,1)`. Thus

```text
ab=c^2,
(a,b,c)!=(0,0,0).
```

Write the nonzero rank-one residue matrix as

```text
M_X=[[a,c],[c,b]]=mu x x^T,
```

with `x=(r,t)` nonzero in `F_p^2` and `mu in F_p^*`.

Then

```text
X=v v^dagger for some v in B_(p,m)^2
iff
mu is a square in F_(p^m).
```

### Proof, forward direction

Write

```text
v=(y_1+eps z_1,y_2+eps z_2).
```

Then

```text
v v^dagger
 = [[y_1^2,
     y_1 y_2+eps(z_1 y_2-y_1 z_2)],
    [y_1 y_2-eps(z_1 y_2-y_1 z_2),
     y_2^2]].
```

Therefore

```text
M_X=(y_1,y_2)^T(y_1,y_2).
```

The two nonzero rank-one matrices

```text
mu x x^T
and
(y_1,y_2)^T(y_1,y_2)
```

have the same image line over `E_m`. Hence

```text
(y_1,y_2)=alpha x
```

for some nonzero `alpha in E_m`, and equality of the matrices gives

```text
alpha^2=mu.
```

Thus `mu` is a square in `E_m`.

### Proof, constructive reverse direction

Assume

```text
alpha^2=mu
```

in `E_m`. Since `(r,t)` is nonzero, the linear functional

```text
(s,u) -> t s-r u
```

is surjective on `E_m^2`. Choose `s,u` satisfying

```text
t s-r u=d/alpha.
```

Put

```text
v=(alpha r+eps s,alpha t+eps u).
```

Then

```text
v v^dagger
 = [[alpha^2 r^2,
     alpha^2 r t+eps alpha(t s-r u)],
    [alpha^2 r t-eps alpha(t s-r u),
     alpha^2 t^2]]
 = X.
```

The nilpotent coordinate therefore creates no further obstruction. QED.

## 3. Minimal descent depth

Let `mu in F_p^*` be nonsquare. Then

```text
mu^((p-1)/2)=-1.
```

Inside `F_(p^m)`,

```text
mu^((p^m-1)/2)
 = (mu^((p-1)/2))^(1+p+...+p^(m-1))
 = (-1)^m,
```

because `p` is odd. Therefore

```text
mu is square in F_(p^m)
iff m is even.
```

Consequently

```text
square sheet:     delta_fac(X)=1,
nonsquare sheet:  delta_fac(X)=2.
```

This gives the independently defined total type

```text
FactorizationType={NATIVE_FACTOR,QUADRATIC_SCALAR_EXTENSION},
D_desc(X)=NATIVE_FACTOR             iff X=v v^dagger over B_(p,1),
          QUADRATIC_SCALAR_EXTENSION otherwise.
```

Its two fibres are exactly the two square-class sheets.

The definition of `D_desc` does not mention a sheet label. It asks an existence question in a fixed scalar-extension tower. It is invariant under every base-defined Hermitian basis change. For `g in GL_2(B_(p,1))`,

```text
X=v v^dagger
iff
g X g^dagger=(g v)(g v)^dagger.
```

The same implication holds after every scalar extension, so the minimal residue-extension degree is a congruence invariant.

## 4. Stronger p=5 form

At `p=5`,

```text
(F_5^*)^2={1,4}={+-1}.
```

Hence the two quotient groups are literally the same quotient, not merely abstractly isomorphic:

```text
F_5^*/(F_5^*)^2
 = F_5^*/{+-1}
 = V_+.
```

The public `V_+` classes are

```text
[1]={1,4},
[2]={2,3}.
```

Therefore the total algebraic map

```text
D_sign:Q_5^x->V_+,
D_sign(X)=[mu(X)]
```

is canonical.

This is a comparison to an existing public algebraic carrier. It is not a public layer gate and it is not a physical qubit statement.

## 5. Base factorization versus quadratic scalar extension

The public ramified element is

```text
J_lambda=2.
```

Every nonsquare in `F_5^*` is `2` times a square. Therefore the p=5 result can be stated without choosing coordinates:

```text
D_desc(X)=NATIVE_FACTOR
iff
X=v v^dagger over B_(5,1),

D_desc(X)=QUADRATIC_SCALAR_EXTENSION
iff
X=2 v v^dagger over B_(5,1)
and X is not a native Hermitian square.
```

The required scalar extension is the underlying quadratic field

```text
E_2=F_25=F_5[tau]/(tau^2-2).
```

In the scalar-extended ramified Hermitian algebra

```text
B_(5,2)=B_(5,1) tensor_(F_5) F_25,
```

the involution is extended as

```text
bar tensor id.
```

It fixes `tau`. Therefore, on this specifically typed scalar extension,

```text
2 v v^dagger=(tau v)(tau v)^dagger.
```

This use of `F_25` must not be confused with the public read-place or norm carrier when that carrier uses the Frobenius involution `x->x^5`. The underlying finite field and polynomial root are the same; the involution datum is different. No equality of those Hermitian carriers is claimed.

Thus the nonsquare sheet is exactly the sheet whose strict factorization first appears after quadratic scalar extension. It is an exact field-of-definition statement. The words state, preparation, particle, Born and foreign qubit are not earned by it.

Equivalently, there is a unique exponent

```text
e_J(X) in {0,1}
```

such that

```text
2^(-e_J(X)) X
```

is a native Hermitian square. Under the literal quotient equality above,

```text
e_J(X)=D_sign(X)
```

in bit notation.

## 6. Dynamics does not supply the clock bridge

For the torsion-normalized ramified Hermitian operator `R` at `p=5`, the residue scalar multiplying the rank-one form is `3`, which has the same `V_+` class as `2`. Hence

```text
D_sign(RX)=2 D_sign(X).
```

In bit notation, direct chronological iteration gives

```text
b_R(n)=b_R(0) XOR (n mod 2).
```

The public `RAMIFIED-TM-LIFT` gives instead

```text
b_TM(n)=theta_n=s_2(n) mod 2.
```

These are not the same stream. The first mismatch occurs at

```text
n=2:
  n mod 2       =0,
  s_2(2) mod 2  =1.
```

One may construct

```text
R^(s_2(n))X
```

or multiply a native square by the public scalar `Theta_n=2^s_2(n)`. Its sheet bit is then `theta_n` by construction. This does not derive a source bridge. It imports the already known clock control into the exponent or scalar.

Therefore the ramified sheet does not independently generate the Thue-Morse clock bit.

## 7. Public ownership audit

The active public repository contains no total typed physical or decoder map with source `Q_5^x` or the ramified Hermitian carrier above.

### QUBIT-FROM-F5

Owns the two-element algebraic quotient `V_+`. It supplies the codomain for `D_sign`, but no source map from the Hermitian sheet carrier and no physical semantics.

### RAMIFIED-TM-LIFT

Owns the map from its one-dimensional ramified phase carrier to the Thue-Morse bit. Its public scope explicitly excludes a physical carry or phase reading and every L2-L6 lift. It does not own `Q_5^x`.

### TM-SHEET-SYNCHRONIZING-GRAPH

Owns a quadratic-class bit on a different L1 scalar sheet automaton. Its theorem says that synchronization removes that bit and retains the clock bit only as a sign in `{1,4}`. It does not map ramified Hermitian forms to physical data.

### PENTIT-ROOT-FACTS and PENTIT-ROOT-READING

Own the underlying arithmetic field `F_25`, the root `tau`, and the declared root reading at their scope. They do not identify the scalar-extended ramified involution with the public finite-field norm involution, and they do not classify the present Hermitian support as a physical preparation or outcome.

### CENTRAL-LIFT-PHASE

Owns the principal archimedean Hermitian action. Its scope excludes a ramified causal or Born cone, a common carrier and every cross-layer lift.

### Born and QDD carriers

The public Born residual algebra is the separate read-place carrier `Z[zeta_8]/5`. The QDD pure-record rows use rational projective carriers. Neither is identified with the present ramified Hermitian carrier.

### Gate audit

`canon/GATES.tsv` contains no gate from this L4 carrier to `V_+`, `D_clock`, `MatterData`, a Born outcome, an apparatus event, an L5 stream or an L6 measure.

Therefore Level C is

```text
STOP: D_sheet to PhysicalData is not currently typed.
```

## 8. What the square-class difference means

The strongest independently derived statement is:

```text
square class      = native Hermitian-square factorization,
nonsquare class   = quadratic-scalar-extension Hermitian-square factorization.
```

For TWIST-J at `p=5`, this becomes:

```text
class [1] = factorization over the base first neighborhood,
class [2] = factorization first after scalar extension to F_25.
```

This is a genuine type distinction. It is a descent obstruction, not a future/past label.

## 9. Status boundary

```text
candidate-T / L4:
  factorization criterion, minimal depth and congruence invariance.

candidate-D / algebraic comparison only:
  p=5 descent type represented in the existing quotient V_+.

STOP / physical:
  no source ownership, physical codomain, context, equality, measurable
  distinction, occurrence rule or layer gate exists for D_sheet.
```

No charge, clock, matter, Born, event, probability, measurement, causal orientation, physical dynamics or decoder-completion statement follows.

## 10. Same-session exact audit

The breaker was committed before execution.

```text
prereg commit:   2d8446c4e18cd5cb2870ed04df05ebf30cd38d91
breaker commit:  53c8df15f2a72bf8ab67a7d034eac91cf25d7bc4
break.py sha256: 66474adb9ecab7a749d3914eb2759c07b2a40f9185330b2387ee88df50b5af3f
platform:        Linux 6.18.35 x86_64
python:          3.13.5
exit code:       0
stdout bytes:    484
stdout lines:    7
stdout sha256:   4c400b75fb38f15a56b0c0d5fad950a8acde18efc18c3101a028ae5cd0f03957
stderr bytes:    0
repeat:          byte-identical
verdict:         BREAKER NO BREAK
```

The checker exhausts the native factor image for `p=3,5,7,11`, constructs every one of the 120 nonradical p=5 points over the trivially involuted scalar extension `F_25`, checks every nilpotent coordinate, audits even/odd extension degree through six for seven primes, verifies the literal p=5 quotient, exhausts the p=5 `R` sheet toggle and records the first clock mismatch at `n=2`.

This is one same-session x86_64 audit. It is not independent confirmation, not a formal public run and not a two-architecture gate. The written proof is the basis for candidate-T.
