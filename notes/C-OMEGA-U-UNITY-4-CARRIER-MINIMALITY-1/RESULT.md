# RESULT C-OMEGA-U-UNITY-4-CARRIER-MINIMALITY-1

**Status:** NON-CANONICAL incubation result. No public T/D/C/H/O/F status is created.

**Owner:** issue #321.

**Repository:** `mathorn1973/twist-j` only.

**Layer:** L1 only.

## 1. Frozen pin

The first scientific execution occurred only after this Git pin:

```text
PIN_COMMIT   4132df08ece7db3e741c9d2b1a3afa45bf4ec3cc
PREREG blob  20888a73c309c4e26f47cec9c8e286194bf0f3a9
verify blob   e605b8bb03ad95b4363258870c4e4974f898d02f
break blob    a6442648c4d12aac2fbfbacd98bdd343ec2f7487
```

Local source reconstruction was checked against the Git blob identity before execution:

```text
verify.py bytes   8722
verify.py SHA256  716a67d765403de6d9519fc3e6185a6cec465cdd3d9188261b4c485e9a2855a1
verify Git blob   e605b8bb03ad95b4363258870c4e4974f898d02f   MATCH remote

break.py bytes    7336
break.py SHA256   f8075091bb5ad46ae6af4481f1f3ce10b7177c2c827440c9e2774e99b0d99f10
break Git blob    a6442648c4d12aac2fbfbacd98bdd343ec2f7487   MATCH remote
```

The Git blob match certifies that the executed source bytes were the pinned source bytes.

## 2. Execution lane

```text
platform      Linux
architecture  x86_64
Python        3.13.5
arithmetic    exact mod 5, Python integers only
```

This is one local x86_64 lane only. It is not a two-architecture gate and earns no public status.

The breaker is a separately implemented same-session attack. It is not independent confirmation.

## 3. Exact transcripts

### verify.py

```text
exit code       0
stderr bytes    0
stdout bytes    1045
stdout SHA256   d5b7893f31c3690adc8838de56dad35300ccb22b37f1950cc2fefebbf81e64e1
```

The committed `VERIFY.stdout` is the exact stdout.

### break.py

```text
exit code       0
stderr bytes    0
stdout bytes    569
stdout SHA256   fbbe809050f8658832229c2e29ca4ade3fe1bb6e6d58ac990ace3cfc5081ba94
```

The committed `BREAK.stdout` is the exact stdout.

## 4. G1: exact Jordan multiplicities are even

**Incubation verdict:** candidate-T PASS.

Let

```text
N = A - 2I.
```

Since `A^5=2I` in characteristic 5,

```text
N^5 = 0.
```

The conjugation relation gives

```text
S N S^-1
 = A^9 - 2I
 = 4N + 3N^2 + N^3 + 2N^4
 = N u(N),

u(N)=4I+3N+N^2+2N^3.
```

`u(N)` is invertible because its constant term is `4 != 0`. It commutes with `N`. Hence for every `r`, conjugation by `S` preserves `ker N^r`.

It also preserves `N ker N^(r+1)`: if `x in ker N^(r+1)`, then

```text
S(Nx) = N u(N) Sx,
```

and both `S` and `u(N)` preserve `ker N^(r+1)`.

Therefore the canonical quotient

```text
E_r = ker(N^r) / (ker(N^(r-1)) + N ker(N^(r+1)))
```

is `S`-invariant. Its dimension is exactly the multiplicity `m_r` of Jordan blocks of size `r`.

On `E_r`,

```text
S^2 = 2I.
```

But `x^2-2` is irreducible over `F_5`. Thus every nonzero `E_r` is naturally a vector space over

```text
F_5[x]/(x^2-2) ~= F_25,
```

and therefore

```text
m_r = dim_F5(E_r) is even.
```

The breaker reaches the same parity by a different scalar obstruction:

```text
det(S)^2 = 2^(m_r).
```

For odd `m_r`, the right side is `2` or `3`, both nonsquares in `F_5`, contradiction.

## 5. G2: rank 8 is the minimum

**Incubation verdict:** candidate-T PASS.

The embedded public module `P ~= J_4(2)` has nilpotency length 4, so the ambient `N` must have at least one Jordan block of size at least 4.

By G1 every exact block multiplicity is even. Therefore:

- if a size-4 block occurs, at least two occur, consuming dimension 8;
- if a size-5 block occurs, at least two occur, consuming dimension 10.

Hence

```text
boxed: dim_F5(V) >= 8.
```

The breaker enumerated every Jordan partition through dimension 8 compatible with nilpotency exponent at most 5 and an embedded length-4 module. Eighteen lower candidate partitions were killed by odd exact-size multiplicity. No carrier below 8 survived.

## 6. G3: the minimal A-type is unique

**Incubation verdict:** candidate-T PASS.

At dimension 8 a size-5 block is impossible because G1 would require two of them. A size-4 block is required by the embedded public module and G1 requires its multiplicity to be at least two.

Two size-4 blocks already consume all eight dimensions. Therefore

```text
boxed: Jordan(N) = (4,4).
```

Equivalently the minimal `A`-module is, up to `F_5[A]`-module isomorphism,

```text
P direct-sum P.
```

This classifies the minimal `A` carrier. It does not yet classify the full pair `(A,S)`.

## 7. G4: transversality is forced at the minimum

**Incubation verdict:** candidate-T PASS.

For type `(4,4)`, put

```text
R = F_5[N]/(N^4).
```

Then `V` is a free rank-2 `R`-module. Any embedded copy `P0 ~= J_4(2)` has a generator of nilpotency length 4, so its image in the two-dimensional top

```text
V/NV
```

is a nonzero line `L`.

The operator induced by `S` on the top satisfies

```text
Sbar^2 = 2I.
```

Because `x^2-2` is irreducible over `F_5`, `Sbar` has no invariant `F_5` line. Hence

```text
Sbar(L) != L.
```

The two lines therefore span `V/NV`. Thus

```text
P0 + S(P0) + NV = V.
```

Nakayama over the local ring `R` gives

```text
P0 + S(P0) = V.
```

Both summands have dimension 4 and `dim V=8`, so

```text
boxed: V = P0 direct-sum S(P0).
```

The verifier and breaker independently enumerate the two-dimensional top: there are exactly 20 matrices with `T^2=2I`; they form one `GL_2(F_5)` conjugacy class, and none fixes any of the six projective lines.

Thus the missing transversal action is not an extra choice once the minimal carrier is reached. It is forced by the same quadratic obstruction that killed rank 4.

## 8. G5: rank-8 existence

**Incubation verdict:** candidate-C PASS, preserving the preregistered label.

The displayed doubled construction satisfies exactly over `F_5`:

```text
A = M direct-sum M,
A^5 = 2I,
ord(A)=20,
S^2=2I,
SAS^-1=A^9.
```

The verifier checks the predecessor's explicit intertwiner.

The breaker does not import that matrix. It solves the full linear intertwiner equation

```text
X M = M^9 X
```

from scratch. The solution space has `F_5` dimension 4 and contains exactly 500 invertible intertwiners. From the first invertible solution it reconstructs a fresh rank-8 bisector and verifies all relations.

So the rank-8 upper bound survives an independently coded construction route within the same session.

## 9. G6: full minimal-pair classification

**Incubation verdict:** STOP.

The frozen scripts establish one conjugacy class on the two-dimensional top but do not classify all lifts of `S` through the length-4 local module. No uniqueness claim for full minimal `(A,S)` pairs is made here.

A natural next route is the nonabelian `H^1` / coprime-complement problem for the kernel of

```text
GL_2(F_5[N]/N^4) -> GL_2(F_5).
```

That kernel is a 5-group while the bisector involution has order 2 modulo its central square. Schur-Zassenhaus suggests uniqueness of the lift class, but that statement is not promoted here without its own frozen attack.

## 10. Result ledger

| Gate | Incubation result | Scope |
|---|---|---|
| G1 | candidate-T PASS | all admissible finite `F_5` carriers in the preregistered class |
| G2 | candidate-T PASS | minimal dimension lower bound |
| G3 | candidate-T PASS | dimension 8, `A`-module type |
| G4 | candidate-T PASS | dimension 8, every embedded public `P` |
| G5 | candidate-C PASS | explicit exact rank-8 existence witness |
| G6 | STOP | full `(A,S)` equivalence classification |

No falsifier F1-F7 fired for G1-G5. G6 was explicitly allowed to STOP.

## 11. Scientific conclusion

Within the frozen L1 class, the earlier dimensional escape is now classified sharply:

```text
rank 4   impossible,
rank 6   impossible,
rank 8   minimal and realized,
A-type   necessarily J_4(2) direct-sum J_4(2),
wall transversality P direct-sum S(P)   forced at the minimum.
```

So the predecessor statement

```text
scalar extension OR dimensional growth
```

can now be sharpened on the unchanged `F_5` route to

```text
minimal dimensional growth = exact doubling 4 -> 8.
```

This is an algebraic L1 statement only. It does not derive the public architecture from J, does not choose between scalar and dimensional growth physically, and does not lift to decoder or measurement layers.
