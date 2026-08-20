# P-QDD-J-AFFINE-APPARATUS-1 preregistration

Date: 2026-08-20

Author of record: A. M. Thorn

Status: preregistered protocol only. No scientific result is earned by this
file. The accepted verifier has formal execution count zero. It may not run
before this file, `verify.py`, and `exact_matrix.py` are committed, pushed,
and read back byte for byte from the public remote.

Public claim lock: issue 456.

## Authority

```text
STATE:          ACTIVE
CANON:          Public Canon v55
AUTHORITY:      mathorn1973/twist-j main
TAG:            canon-v55
CONTENT_COMMIT: 6236c10cd89e0a3a53fca730f50c50c237d4add0
CANON_SHA256:   e22ebb5648611780743122da67ec965394c3f97ed18b99079be028ca6ebb47a9
CANON_BYTES:    282461
BASE_COMMIT:    362e9c3a9afa9f63005eaf0a1c03baac66617012
```

Target: blocker O2 of `QDD-INSTRUMENT-APPARATUS [O]` only.

This probe classifies one restricted target-independent J-native class. It
neither claims that this is the complete class of admissible J-native apparatus
nor closes O2 globally.

## Result-exposure disclosure

Before issue 456, NON-CANONICAL chat and scratch calculations suggested a
four-element affine multiplier family and a two-element involutive sub-class.
They predate this pin and are discovery context only. Every earlier matrix,
count, transcript, witness and run is excluded from formal evidence. Static
source inspection and syntax compilation are allowed before the pin; scientific
gate execution is not.

The proofs below are frozen protocol content. The verifier audits them and does
not replace their quantifiers.

## Field 1: equation

### Primitive J data

Work over

```text
V = Q^4,
1 = (1,1,1,1)^T,
G = I_4 - (1/5) 1 1^T,
D = M_J - I_4.
```

Here `M_J` is the public multiplication-by-J matrix. The phase motor `D` is
multiplication by `zeta_5^2`, hence

```text
D^5 = I_4,
D^T G D = G.
```

Put `e_0=(1,0,0,0)^T` and

```text
u_x = D^x e_0,                    x in F_5.
```

Direct cyclotomic reduction gives the rational A_4 simplex

```text
sum_x u_x = 0,
<u_x,u_y>_G = 4/5 if x=y and -1/5 otherwise.
```

### J-affine action and stabilizer projectors

For `c in F_5^x`, `b in F_5`, define `g_(c,b)(x)=b+cx`. There is a unique
rational representation `rho(c,b)` on V satisfying

```text
rho(c,b) u_x = u_(b+cx).
```

It is faithful and G-orthogonal, and represents all 20 elements of
`AGL_1(F_5)`.

For a memory token `k in F_5`, freeze its multiplier stabilizer

```text
H_k = {h_(a,k): x -> k + a(x-k), a in F_5^x}.
```

Define, before any QDD target comparison,

```text
P_k = (1/4) sum_(a in F_5^x) rho(h_(a,k)),
Q_k = I_4 - P_k.
```

The finite-group average is the G-orthogonal projector onto the fixed space.
Since H_k fixes k and is transitive on the other four labels, its fixed space
inside the sum-zero simplex module is exactly Q u_k. Therefore

```text
P_k^2=P_k=P_k^sharp, rank(P_k)=1, im(P_k)=Q u_k,
Q_k^2=Q_k=Q_k^sharp, rank(Q_k)=3,
```

where `A^sharp=G^-1 A^T G`. Affine transport gives

```text
rho(c,b) P_k rho(c,b)^-1 = P_(b+ck).
```

### Pointer, memory, and the frozen class

Use the binary pointer `Q^2` with ready state `p_0`, record state `p_1`, and
flip `X p_0=p_1`, `X p_1=p_0`. Use memory `Q^5` with orthonormal token basis
`m_k`. The total Gram is `G tensor I_2 tensor I_5`.

For every multiplier `a in F_5^x`, define

```text
U_a = sum_(k in F_5)
      [P_k tensor I_2 + rho(h_(a,k)) Q_k tensor X]
      tensor |m_k><m_k|.
```

The complete frozen class is

```text
A_JAFF = {U_1,U_2,U_3,U_4}.
```

No multiplier is selected or fitted. The class builder uses only `M_J`, `D`,
`G`, `F_5`, its complete affine/Galois action, a binary pointer flip, and the
five memory tokens. The strings and objects `E_low`, `E_high`, and the target
projector pair are forbidden inputs to the builder.

### Reversibility, covariance, and completeness of the class

Inside memory block k, `P_k Q_k=0`, `rho(h_(a,k))` commutes with both
projectors, and both rho and X are orthogonal. Thus every U_a is reversible:

```text
U_a^sharp U_a = I.
```

For `A_(c,b)=rho(c,b) tensor I_2 tensor L(c,b)`, with
`L(c,b)m_k=m_(b+ck)`, affine transport gives

```text
A_(c,b) U_a = U_a A_(c,b).
```

The multiplier set is the complete field unit group `F_5^x`, so the frozen
class has exactly four members. Because X has order two and h_(a,k) has the
same order as a,

```text
U_a^2=I and U_a^sharp=U_a  iff a^2=1 mod 5 iff a in {1,4}.
```

### Induced instrument, still before target comparison

Prepare pointer p_0 and memory m_k, then read the pointer in `(p_0,p_1)`. The
branch maps are

```text
K_0(a,k)=P_k,
K_1(a,k)=rho(h_(a,k)) Q_k.
```

For every a,k,

```text
K_0^sharp K_0=P_k,
K_1^sharp K_1=Q_k,
K_0^sharp K_1=0,
P_k+Q_k=I.
```

Memory is preserved and the pointer PVM has no leakage on the prepared image.

Use the post-state equivalence already registered by
`QDD-INSTRUMENT-NONSELECTION`: maps in one nonzero effect fibre are equivalent
iff they differ by one global sign.

For fixed k the four moving maps `rho(h_(a,k))Q_k` are pairwise inequivalent.
If two differed by sign, their quotient rho(h_(b^-1 a,k)) would be +I or -I on
im(Q_k). Its trace on the full simplex module is 0 for a nonidentity stabilizer,
while its fixed-line trace is 1, so its trace on im(Q_k) is -1. This is neither
3 nor -3, the traces of +I_3 and -I_3. Hence a=b.

### Target comparison, deliberately last

Only after the class above is frozen, compare with the public target

```text
E_low=(1/4)11^T,
E_high=I_4-E_low.
```

The phase-simplex identity is `u_2=-1`, so

```text
P_2=E_low,
Q_2=E_high.
```

At memory token k=2 all four U_a realize the target effects. The a=1 member has
`K_0=E_low`, `K_1=E_high`, the Lueder pair. The other three have the same
effects and occurrence weights but inequivalent moving-branch post-states.
Thus the full class has four target-realizing post-state classes.

The self-adjoint involutive sub-class `{U_1,U_4}` still has two inequivalent
target-realizing classes. The Lueder member is uniquely selected only by an
extra identity/minimal-disturbance premise such as

```text
rho(h_(a,2)) Q_2 = Q_2,
```

or zero moving-branch displacement. This premise is not derived from the
frozen class axioms and is not adopted.

## Field 2: code

Accepted exact files:

```text
probes/P-QDD-J-AFFINE-APPARATUS-1/verify.py
probes/P-QDD-J-AFFINE-APPARATUS-1/exact_matrix.py
```

Python standard library only; integers and `Fraction` only; no float, Decimal,
complex approximation, random search, external dataset, or imported scratch
transcript. The verifier exhausts the five simplex vertices, all 20 affine
maps, five stabilizers, four 40-dimensional couplings, all 20 induced
instruments, and the complete target comparison. Universal statements rest on
the written proofs above.

## Field 3: carrier or data

No external data.

```text
system  (Q^4,G)
pointer (Q^2,I_2)
memory  (Q^5,I_5)
total   Q^4 tensor Q^2 tensor Q^5, dimension 40
```

## Field 4: systematics and completeness

There is no measurement systematic. Exact obligations C1-C12 are:

```text
C1 authority constants and target-independence source guard;
C2 D^5=I and D^T G D=G;
C3 complete five-vertex simplex Gram and sum;
C4 all 20 affine maps, faithfulness, law, and G-orthogonality;
C5 all five stabilizer averages, fixed lines, ranks, and transport;
C6 exactly four distinct reversible, memory-preserving, covariant U_a;
C7 all 20 induced branch formulas and effects;
C8 target comparison only after C1-C7;
C9 P_2=E_low, Q_2=E_high and exactly four target classes;
C10 involutive/self-adjoint sub-class exactly {1,4}, with two classes;
C11 displacement ranks (0,3,3,2), so zero displacement selects a=1 only as
    an added premise;
C12 preserve the written proofs and the target-independence firewall.
```

A hidden input, omitted multiplier, target effect in the class builder,
floating tolerance, pre-pin result, unnamed layer lift, post-pin scope change,
or incomplete class is STOP.

## Field 5: decision and falsifiers

No tolerance exists.

```text
NONUNIQUE
  C1-C12 pass and at least two target-realizing post-state classes survive.
UNIQUE-LUEDERS
  C1-C12 pass and exactly one target-realizing class survives, the Lueder pair.
EMPTY
  C1-C8 pass and no member realizes the target effects.
CLASS-F
  an exact counterexample breaks the primitive, affine, stabilizer,
  reversibility, covariance, completeness, or induced-instrument theorem.
TARGET-F
  an exact counterexample breaks the target comparison or class count.
INVOLUTION-F
  an exact counterexample breaks the involutive/self-adjoint classification.
STOP
  authority, collision, pin, integrity, completeness, security, evidence,
  target independence, or layer discipline fails.
```

If NONUNIQUE is earned, the maximum candidate statements are:

```text
QDD-J-AFFINE-APPARATUS-CLASS [T]
  the frozen target-independent AGL_1(F_5)-covariant class is exact and
  reversible at L4;
QDD-J-AFFINE-APPARATUS-NONSELECTION [T]
  the class has four target-realizing post-state classes, and its
  self-adjoint involutive sub-class still has two; Lueder requires an added
  identity/minimal-disturbance premise.
```

These are restricted-class statements, not a theorem about every admissible
J-native apparatus.

## Field 6: action layer

```text
L4 apparatus/support only.
```

No L5 event stream and no L6 measure are produced. `SAMPLING NOT PROVIDED` is
the only permitted sampling statement. O1 is untouched. Global O2 and
`QDD-INSTRUMENT-APPARATUS [O]` remain unchanged by this probe alone.

## Formal sequence after the pin

1. Commit and push this file and the two accepted exact Python files.
2. Read all three back from the public remote; record pin, SHA-256 and bytes on
   issue 456.
3. Only then run `python3 probes/P-QDD-J-AFFINE-APPARATUS-1/verify.py` once.
4. Commit exact `EXPECTED.txt`, neutral `RUN.md`, and `RESULT.md` without
   changing pinned files.
5. Open one PR changing only this probe directory; require x86_64 and aarch64
   byte identity.
6. A later separate Canon fold may register only the earned status and scope.
