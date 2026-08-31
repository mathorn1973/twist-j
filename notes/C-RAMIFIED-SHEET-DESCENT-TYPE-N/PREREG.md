# C-RAMIFIED-SHEET-DESCENT-TYPE-N preregistration

**Status:** NON-CANONICAL incubation. No authority, public status, gate, verifier permission, Canon effect or Registry effect.

```text
issue:          #668
owner:          current ChatGPT owner session, 2026-08-29
target line:    PUBLIC
public Canon:   v71
public base:    842b43e2f258469712aedf121f879767d1bd072c
action layer:   L4 exact quadratic support
formal probe:   none
```

## Frozen question

Can the square-class distinction of the ramified Hermitian nonradical null cone be given a total canonical typed meaning that is independently defined rather than supplied by a physical label?

The three levels are separated:

```text
A  intrinsic algebraic type;
B  comparison to an existing public algebraic type;
C  physical or decoder meaning.
```

## Carrier

For an odd prime `p` and `m>=1`, let

```text
B_(p,m)=F_(p^m)[eps]/(eps^2),
bar(a+b eps)=a-b eps.
```

Let `Q_p^x` be the nonradical null locus in `Herm_2(B_(p,1))`:

```text
X(a,b,c,d)=[[a,c+d eps],[c-d eps,b]],
q(X)=ab-c^2=0,
(a,b,c)!=(0,0,0).
```

Write its nonzero rank-one residue matrix as

```text
M_X=[[a,c],[c,b]]=mu x x^T,
```

where `x in F_p^2` is nonzero. The class `[mu]` in `F_p^*/(F_p^*)^2` is independent of the representation.

## Frozen candidate type

Define

```text
delta_fac(X)=min{m>=1 : X=v v^dagger for some v in B_(p,m)^2}.
```

The candidate typed output is

```text
FactorizationType={NATIVE_FACTOR,QUADRATIC_EXTENSION},
D_desc(X)=NATIVE_FACTOR       iff delta_fac(X)=1,
          QUADRATIC_EXTENSION iff delta_fac(X)=2.
```

No physical preparation or state meaning is included.

## Frozen gates

### G1 Factorization criterion

Prove or break:

```text
X=v v^dagger over B_(p,m)
iff mu is a square in F_(p^m).
```

The constructive direction must solve every nilpotent coordinate `d`.

### G2 Minimal residue-extension depth

Prove or break:

```text
[mu] square    => delta_fac(X)=1,
[mu] nonsquare => delta_fac(X)=2.
```

More generally, a nonsquare `mu in F_p^*` is square in `F_(p^m)` iff `m` is even.

### G3 Independent type and fibres

Prove or break that `D_desc` is total and basis independent, is defined without using the words square sheet or nonsquare sheet, and has fibres exactly the two canonical sheets.

### G4 Public sign-quotient comparison at p=5

Using the exact public carrier

```text
V_+=F_5^*/{+-1}={{1,4},{2,3}},
```

prove or break

```text
F_5^*/(F_5^*)^2=F_5^*/{+-1}=V_+.
```

Define only the algebraic comparison

```text
D_sign:Q_5^x->V_+,
D_sign(X)=[mu(X)].
```

No public L4-to-L1 promotion is permitted without a named gate.

### G5 Dynamics boundary

For the torsion-normalized ramified Hermitian operator `R` at `p=5`, prove or break

```text
D_sign(RX)=2 D_sign(X).
```

Distinguish exactly:

```text
D_sign(R^n X)=D_sign(X)+(n mod 2),
q(Theta_n)=theta_n=s_2(n) mod 2.
```

These streams are not equal for all `n`. Equality after replacing `n` by `s_2(n)` is a controlled construction, not an independently derived source bridge.

### G6 Public ownership audit

Search the active public repository for a total typed map from this exact ramified Hermitian carrier to `D_clock`, `MatterData`, charge sign, Born effect or outcome, apparatus event, future/past cone, physical preparation, L5 stream or L6 measure.

A positive finding must provide all of:

```text
source carrier,
codomain,
total map,
context,
equality or equivalence,
named layer gate.
```

Two-element cardinality, a shared quadratic character, a naming resemblance or a map on another carrier is not sufficient.

## Frozen breakers

1. A nonsquare-class nonradical `X` factors over `B_(p,1)`.
2. A square-class nonradical `X` fails to factor over `B_(p,1)`.
3. A nonsquare base-field coefficient becomes square in an odd-degree residue extension.
4. Some `d` obstructs factorization after `mu` acquires a square root.
5. The `p=5` quotient differs from public `V_+`.
6. Direct chronological `R^n` sheet dynamics equals the Thue-Morse bit for every `n`.
7. A physical conclusion is drawn without the six typed fields above.
8. The public `foreign qubit`, QDD pure record, Born carrier or clock carrier is silently identified with this carrier.

## Decision rule

```text
candidate-T  G1-G3 close by exact proof;
candidate-D  G4 supplies a conservative algebraic type comparison;
STOP         G6 finds no complete public physical/decoder map;
F            an exact breaker negates a positive frozen clause.
```

The result may simultaneously be candidate-T at A, candidate-D at B and STOP at C. No summary may promote the whole package to a physical bridge.

## Pre-execution record

At this commit:

```text
exact enumerations: 0
audit runs:         0
formal runs:        0
Canon edits:        0
Registry edits:     0
```
