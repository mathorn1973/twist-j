# C-OMEGA-U-UNITY-3-BISECTOR1

**Title:** Fixed-carrier bisector obstruction and the carrier-growth fork

**Status:** NON-CANONICAL INCUBATION NOTE. No public T/D/C/H/O/F status is created here.

**Date:** 2026-08-10

**Owner lock:** issue #319

**Repository:** `mathorn1973/twist-j`

**Layer:** L1 algebra only.

**Purpose:** preserve the exact fixed-carrier obstruction from the sealed 2026-08-09 incubation, record the counterexample that breaks its broader F_25-forcing interpretation, and state the corrected carrier-growth fork without changing Canon, Registry, Frontier, probes, reproductions, status, or release files.

This Note imports no local verifier or stdout as public evidence. The sealed local artifact is provenance only.

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
BASE_MAIN:      683a978811487f7d568fc10b794d4ae014dece33
TAG_COMMIT:     2d4ee6956f2da6f8ab23b7471ad7fcd73f787fa1
```

Readback before the owner lock:

- `canon/CANON.md` has the same Git blob at `CONTENT_COMMIT`, `canon-v39`, and current `main`.
- `canon/SHA256SUMS` at `canon-v39` carries the declared Canon SHA-256.
- `CONTENT_COMMIT` is an ancestor of `BASE_MAIN`, with zero commits behind.
- `canon-v39` is an ancestor of `BASE_MAIN`, with zero commits behind.
- the preceding notes PR #318 passed `architecture-x86_64`, `architecture-aarch64`, `check_policy.py`, `check_canon.py`, `check_ledger.py`, and aggregate `check`.

The current public Core explicitly does not claim that the checkpoint space, the five generators, the selector, or the decoder are uniquely derived from `J`. This incubation does not strengthen that boundary.

Public theorem rows used inside their registered scopes:

```text
J-STEP                  T
C20-TEICHMULLER-SPLIT  T
SPIN-BISECTOR           T   boundary comparison only
BORN-ORDER-STAIRCASE   T   boundary comparison only
```

No public row is modified by this Note.

---

## 1. Collision and ownership record

Before issue #319 was opened:

```text
branches matching OMEGA-U-UNITY      none
open issues matching OMEGA-U-UNITY   none
pull requests matching OMEGA-U-UNITY none
repository C-OMEGA-U-UNITY entries    none
BISECTOR-SOCLE-EMPTY Registry row     none found
```

Issue #319 owns this one incubation item:

```text
C-OMEGA-U-UNITY-3-BISECTOR1
```

No sibling candidate or public probe is claimed by this Note.

---

## 2. Sealed incubation input

The supplied archive was unpacked and its internal hash manifest rechecked. The seven pinned files passed `sha256sum -c SHA256SUMS.txt` after the archive round trip.

The supplied pins are:

```text
archive sha256  f83a76c3d3e7320aa8c31aeaa1f9ec82e186355a509fa4937f76e3216b81ddab
prereg          d1e5772966ee4643d2cfa2c4e3a840728671295023932c666a8449e515e6568b
verify.py       347df164b72a9d55aab4a7ea53a5b7527918ce4653f75dc04785ab8ab357f758
verify stdout   03ac863a5fd667070d18a80ffae068e0d8adc1d7bdac60f3be64cf4c46e00528
break.py        122df562f8c097df24c774370e2caf10f38e5a8ed3eda5669dc981d38f021263
break stdout    d7048f8e82157e1c25cc4c877c5db0c29737a557b9c9d8fbd45499e7c41bfb9c
RESULT          eee7974baf9df1cb685fb73da98c5a7baa3910281d4ad77fa2fe34b12cdad411
PROMO           5bb9e51e307c2af150a6149abbf4156be6346d35d9ec8c7b7aa4952358637628
```

A neutral local rerun also reproduced the pinned transcripts byte for byte:

```text
verify: 44 PASS, 0 FAIL
break:  10 PASS, 0 FAIL, 0 breaks
```

These single-environment reruns are not a public two-architecture gate and create no public evidence or status. The original bytes remain sealed by their hashes and are not rewritten here.

---

## 3. Frozen fixed-carrier problem

Work over `F_5`. Let `P = F_5^4` in the public J-STEP power basis. The reduced multiplication-by-J matrix is

```text
M = [1 0 4 1]
    [0 1 4 0]
    [1 0 0 0]
    [0 1 4 1].
```

The public C20 theorem gives

```text
ord(M) = 20,
M^5 = 2 I,
M^10 = -I,
(M - 2I)^4 = 0 != (M - 2I)^3.
```

Put

```text
w = (1,2,3,4)^T,
W = ker(M - 2I) = span_F5(w),
dim_F5(W) = 1.
```

The fixed-carrier bisector equations are

```text
B1: S^2 = M^5 = 2I,
B2: S M S^-1 = M^a
```

for `S in GL_4(F_5)` and `a mod 20`.

The question here is only whether this system has a solution on this exact public four-dimensional carrier.

---

## 4. Fixed-carrier obstruction

**Incubation label:** candidate-T. No public theorem status is created by this Note.

### 4.1 Centrality reduces the exponent census

From `S^2 = 2I`, the square of conjugation by `S` is the identity. Applying B2 twice gives

```text
M = M^(a^2).
```

Since `ord(M)=20`,

```text
a^2 = 1 mod 20.
```

Thus only

```text
a in {1,9,11,19}
```

can survive.

### 4.2 The case a = 1

If `a=1`, then `S` centralizes `M`. Since `M` is nonderogatory, its centralizer is the commutative algebra `F_5[M]`, identified at the frozen scope with the public `A_4 = O/(5)` carrier.

The public `C20-TEICHMULLER-SPLIT [T]` theorem states that the Sylow 2-subgroup of `A_m^*` is `C_4` for every `m>=1`. In particular `A_4^*` has no element of order 8.

But `S^2=2I` and `2` has order 4 in `F_5^*`, so an invertible `S` satisfying B1 would have order 8. Contradiction.

Therefore `a=1` is empty.

### 4.3 The cases a = 11 and a = 19

The unique residue eigenvalue of `M` is `2`. For `a=11` or `19`,

```text
2^a = 3 mod 5.
```

Hence `M^a` has residue eigenvalue `3`, not `2`, so `M^a` is not similar to `M`.

Therefore `a=11` and `a=19` are empty.

### 4.4 The case a = 9

Any intertwiner satisfying

```text
X M = M^9 X
```

maps

```text
W = ker(M-2I)
```

into

```text
ker(M^9-2I) = W.
```

Thus an invertible bisector `S` at `a=9` preserves the one-dimensional line `W` and acts there by a scalar `c in F_5^*`:

```text
S w = c w.
```

B1 then gives

```text
c^2 w = S^2 w = 2 w,
```

so

```text
c^2 = 2 in F_5.
```

But the squares in `F_5` are

```text
{0,1,4}.
```

Therefore `2` is not a square. Contradiction.

So `a=9` is empty.

### 4.5 Fixed-carrier conclusion

All four admissible exponents are excluded:

```text
There is no S in GL_4(F_5) and no a mod 20 such that

S^2 = M^5 = 2I
and
S M S^-1 = M^a.
```

The sealed finite census independently returned zero solutions for all twenty exponents. The proof above is the scientific content; the local census is only incubation support.

---

## 5. The W-forced mechanism

**Incubation label:** candidate-T. No public theorem status is created here.

Square roots of `2I` do exist in `GL_4(F_5)`. The obstruction is narrower:

```text
no square root of 2I can preserve W.
```

Indeed, any `W`-preserving square root acts on the one-dimensional `W` by a scalar `c`, and again forces

```text
c^2 = 2,
```

which has no solution in `F_5`.

So the surviving mechanism is not

```text
sqrt(2I) does not exist over F_5.
```

It is

```text
a one-dimensional invariant F_5 line cannot carry sqrt(2).
```

That distinction is essential for the next section.

---

## 6. Falsification of the broad F_25-forcing reading

The sealed PROMO proposed the stronger reading:

```text
Any carrier hosting a J-normalizing bisector must have a residue field
containing sqrt(2), minimal F_25.
```

As a general carrier statement this is false.

The fixed `F_5^4` obstruction does not imply that the base field must grow. The same quadratic structure can be represented inside a higher-dimensional endomorphism algebra while the scalar field remains `F_5`.

### 6.1 Exact doubled-carrier witness over F_5

Let

```text
P_8 = P direct-sum P,
M_8 = M direct-sum M.
```

Define

```text
X = [0 1 0 3]
    [0 1 4 1]
    [0 1 4 2]
    [1 3 3 0].
```

Its inverse over `F_5` is

```text
X^-1 = [4 3 0 1]
       [1 3 2 0]
       [1 1 3 0]
       [0 4 1 0].
```

Direct multiplication gives

```text
X M = M^9 X.
```

Now define the block matrix

```text
S_8 = [ 0       2 X^-1 ]
      [ X       0      ].
```

Then

```text
S_8^2
 = [2 X^-1 X      0     ]
   [    0        2 X X^-1]
 = 2 I_8.
```

Because exponent `9` is its own inverse modulo `20`, the intertwiner identity also gives the reverse relation needed on the upper block, and hence

```text
S_8 M_8 = M_8^9 S_8.
```

Therefore

```text
S_8 M_8 S_8^-1 = M_8^9.
```

Finally

```text
M_8^5 = 2 I_8,
```

so the exact bisector equations hold on the doubled carrier while every entry remains in `F_5`:

```text
S_8^2 = M_8^5,
S_8 M_8 S_8^-1 = M_8^9.
```

This is a direct counterexample to the broad field-extension claim.

### 6.2 What the counterexample does not refute

It does not refute the fixed public carrier obstruction in Sections 4 and 5.

It shows only that

```text
fixed-carrier failure != base-field-extension necessity.
```

The escape can be dimensional rather than scalar.

---

## 7. Correct general quadratic-module statement

There is a clean theorem behind the distinction.

Let `V` be a nonzero `F_5` vector space invariant under an endomorphism `S` satisfying

```text
S^2 = 2 I_V.
```

Since `2` is a quadratic nonresidue modulo `5`, the polynomial

```text
x^2 - 2
```

is irreducible over `F_5`. Therefore

```text
F_5[x]/(x^2-2) ~= F_25.
```

The assignment

```text
x |-> S
```

extends the `F_5` action on `V` to an action of `F_25`. Because the source is a field and `1` acts as the identity, the action is faithful.

Thus `V` is naturally an `F_25` vector space, even if the ambient carrier continues to be written as an `F_5` vector space.

Consequently

```text
dim_F5(V) = 2 dim_F25(V),
```

so every nonzero invariant subspace carrying `S^2=2I` has even `F_5` dimension.

This explains both cases:

```text
dim_F5(W) = 1     blocked,
dim_F5(W direct-sum W) = 2   admissible in principle and realized above.
```

The actual invariant requirement is therefore a quadratic-module requirement, not a theorem that the ambient scalar field label must change.

---

## 8. Corrected carrier-growth fork

**Incubation reading:** candidate-D at most. No public D claim is created here.

After the fixed `F_5^4` door closes, at least two mathematically distinct routes remain:

```text
A. scalar growth
   extend scalars from F_5 to F_25 so sqrt(2) becomes a scalar;

B. dimensional growth
   keep scalars F_5 and enlarge the relevant invariant carrier so the
   quadratic F_25 structure is represented inside End_F5(V).
```

The sealed incubation proved neither route unique.

Therefore the correct conclusion is:

```text
The original four-dimensional F_5 piston carrier cannot host the frozen
J-normalizing bisector. Any successful replacement must supply an even-dimensional
quadratic module for x^2-2, but that can happen either by scalar extension or by
carrier enlargement over the same field.
```

This is strictly weaker than the original F_25-forcing wording and is the strongest statement preserved by this Note.

---

## 9. Status ledger inside this Note

These labels are incubation labels only.

| Item | Incubation verdict | Exact scope |
|---|---|---|
| fixed `F_5^4` bisector set is empty | candidate-T survives | L1, exact public piston carrier only |
| no `W`-preserving square root of `2I` | candidate-T survives | one-dimensional `W` only |
| `S^2=2I` makes an invariant nonzero module an `F_25` vector space | candidate-T | general finite-dimensional `F_5` module statement |
| base field `F_25` is forced for every carrier | F in incubation | refuted by explicit `F_5^8` witness |
| scalar extension or dimension growth are the two exposed routes | candidate-D boundary | not a completeness classification of all future architectures |
| exact doubled-carrier matrix witness | candidate-C / exact witness | `F_5^8` construction displayed above |

No row above is inserted into the public Registry by this Note.

---

## 10. Relation to existing public rows

### J-STEP [T]

Supplies the public multiplication-by-J matrix whose reduction mod 5 is the frozen `M`.

### C20-TEICHMULLER-SPLIT [T]

Supplies at the registered L1 scope the exact order `20`, `M^5=2I`, the one-block ramified structure, and the absence of order `8` from the relevant `A_m^*` unit groups. This is a logical input to the fixed-carrier `a=1` exclusion.

### SPIN-BISECTOR [T]

Records an order-eight `SL_2(F_25)` shadow. In this Note it is only a comparison point. It does not prove that every bisector construction must change the ambient field to `F_25`.

### BORN-ORDER-STAIRCASE [T]

Records where root orders first occur in its own frozen field-extension staircase. It does not classify all higher-dimensional `F_5` representations of the same quadratic algebra. The doubled-carrier witness does not contradict the registered scope of this row.

No public theorem is weakened by the corrected incubation reading.

---

## 11. Why no FRONTIER edit belongs here

The public `FRONTIER.md` is generated from live `H` and `O` Registry rows. A candidate-D explanatory sentence is not a live frontier row and must not be inserted by hand.

Therefore the original PROMO instruction

```text
add one FRONTIER sentence
```

is retired.

If a later formal public probe closes a theorem, any Canon or Registry fold must follow the normal public fold procedure. This incubation Note does not authorize that step.

---

## 12. Narrow future public-probe target

If this lane is promoted to a formal public probe, the scientifically clean target is only the fixed-carrier theorem, for example:

```text
P-BISECTOR-SOCLE-EMPTY-1
```

with a proposed statement bounded to:

```text
M on the public F_5^4 J-STEP carrier,
W = ker(M-2I),
no S in GL_4(F_5) satisfying S^2=M^5 and S M S^-1=M^a for any a mod 20,
and no W-preserving square root of 2I.
```

Explicit nonclaims of such a probe must include:

```text
no claim about larger F_5 carriers,
no claim that F_25 scalar extension is necessary,
no uniqueness of architecture from J,
no L2-L6 lift,
no physical reading.
```

A formal probe would require a fresh public preregistration pin, an accepted public verifier, and the required byte-identical two-architecture gate. The sealed local transcripts in Section 2 cannot substitute for that process.

---

## 13. Future attack created by the falsification

The falsification does not merely weaken the lane. It sharpens the next question.

The old fork was framed as

```text
F_5^4 or F_25.
```

The corrected fork is

```text
fixed rank 4
versus
quadratic-module growth.
```

A useful next incubation should therefore classify minimal `F_5` carrier enlargement, not assume scalar extension in advance. One possible target is:

```text
C-OMEGA-U-UNITY-4-CARRIER-MINIMALITY-1
```

Question:

```text
Among J-compatible finite F_5 carriers extending the public rank-4 piston
representation, what is the smallest dimension and equivalence class that admits
a J-normalizing bisector and still carries the required transversal wall action?
```

The displayed `F_5^8` witness proves only existence of a doubled algebraic bisector. It does not prove that rank `8` is minimal under every J-compatible extension rule, nor that it solves the original selector or wall-transversality problem. Those are separate gates.

---

## 14. Falsification discipline

The following remain first-class boundaries for any future formalization:

```text
F1  an S in GL_4(F_5) satisfying both frozen bisector equations refutes
    the fixed-carrier empty claim;

F2  a W-preserving square root of 2I refutes the socle obstruction;

F3  a root of c^2=2 in F_5 refutes the arithmetic step;

F4  an error in the centrality, centralizer, similarity, or socle argument
    refutes the corresponding proof route;

F5  any future statement that base-field extension is globally forced is
    already refuted by the displayed F_5^8 witness unless its admissible class
    explicitly excludes dimensional enlargement;

F6  any promotion using the sealed one-environment stdout as if it satisfied
    the public two-architecture gate is procedurally invalid.
```

No fired falsifier may be removed by changing the admissible class after the fact. A narrower future class must be frozen before its own execution.

---

## 15. Security and repository boundary

This Note contains no private hostnames, IP addresses, credentials, environment secret files, machine nicknames, binary artifact, model file, external dataset, or private repository reference.

Repository target is only:

```text
mathorn1973/twist-j
```

Intended diff:

```text
notes/C-OMEGA-U-UNITY-3-BISECTOR1.md   added
```

Nothing under `canon/`, `probes/`, `reproduce/`, `.github/`, or release/status surfaces is changed.

---

## Conclusion

The first nontrivial result of the bisector attack survives on the exact public piston carrier:

```text
F_5^4 cannot internalize the frozen J-normalizing bisector while preserving
the one-dimensional ramified socle.
```

The stronger interpretation does not survive:

```text
F_25 is not forced as the ambient base field for every larger carrier.
```

The exact doubled-carrier witness shows that the real requirement is a quadratic module for `x^2-2`. The next structural question is therefore not simply which field comes next, but which minimal J-compatible carrier can host that module and still recover the missing transversal action.
