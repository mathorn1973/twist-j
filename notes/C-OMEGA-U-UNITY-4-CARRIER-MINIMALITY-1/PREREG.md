# PREREG C-OMEGA-U-UNITY-4-CARRIER-MINIMALITY-1

**Status:** NON-CANONICAL incubation preregistration. No public scientific status.

**Owner lock:** issue #321.

**Repository:** `mathorn1973/twist-j` only.

**Layer:** L1.

**Frozen base:** `8fea65a9df7b1d0915432f9c2c8e3cf9ace7f134`.

## 1. Public inputs

Use only the registered L1 facts needed here:

- `J-STEP [T]`: multiplication by J on the rank-4 regular carrier.
- `C20-TEICHMULLER-SPLIT [T]`: after reduction mod 5, the public matrix `M` has exact order 20, `M^5 = 2I`, and one ramified Jordan block `J_4(2)`.
- predecessor incubation `C-OMEGA-U-UNITY-3-BISECTOR1`: provenance only, no public status. It supplies an exposed rank-8 witness that must be rechecked here from displayed matrices.

No decoder, physical reading, scalar-extension necessity, or L2-L6 statement is imported.

## 2. Frozen admissible class

An admissible carrier is a tuple `(V,A,S,iota)` where:

```text
V     finite-dimensional vector space over F_5,
A     in GL(V),
S     in GL(V),
iota  injective A-module map P -> V,
```

and

```text
A^5 = 2 I,
ord(A) = 20,
S^2 = A^5 = 2 I,
S A S^-1 = A^9.
```

`P` is the public rank-4 module `J_4(2)`. The image `iota(P)` is required to be A-invariant but is not required to be S-invariant.

No other extension rule is admitted or hidden.

## 3. Algebraic notation

Put

```text
N = A - 2I.
```

In characteristic 5, `A^5 = 2I` is equivalent to `N^5 = 0` because

```text
(2I + N)^5 = 2I + N^5.
```

The conjugation law gives, modulo `N^5=0`,

```text
S N S^-1 = A^9 - 2I
           = 4N + 3N^2 + N^3 + 2N^4
           = N u(N),

u(N) = 4I + 3N + N^2 + 2N^3.
```

The constant term of `u` is 4, so `u(N)` is invertible.

For `r=1,...,5`, let `m_r` denote the number of Jordan blocks of `N` of exact size `r`. One canonical realization is

```text
E_r = ker(N^r) / (ker(N^(r-1)) + N ker(N^(r+1))),
```

with the conventions `ker(N^0)=0`, `ker(N^6)=V`; `dim E_r = m_r`.

## 4. Frozen gates

### G1. Exact-size multiplicity parity

Decide whether every `E_r` is S-invariant and inherits `S^2=2I`. Since `x^2-2` is irreducible over `F_5`, target:

```text
m_r is even for every r=1,...,5.
```

Fires on one admissible tuple with odd `m_r`.

### G2. Minimal dimension

Because `iota(P)` has nilpotency index 4, `N` has a Jordan block of size at least 4. Combine with G1.

Target:

```text
dim_F5(V) >= 8.
```

Fires on one admissible carrier of dimension below 8.

### G3. Minimal Jordan type

At dimension 8, target:

```text
Jordan type of N is exactly (4,4).
```

Fires on one admissible dimension-8 carrier with another type.

### G4. Forced transversality at the minimum

For dimension 8 and any embedded copy `P0=iota(P)`, target:

```text
V = P0 direct-sum S(P0).
```

Proof route to audit: for type `(4,4)`, `V/NV` has dimension 2. Both `P0` and `S(P0)` project to lines. The induced operator `Sbar` satisfies `Sbar^2=2I`; irreducibility of `x^2-2` forbids an invariant line, so the two lines are distinct. Nakayama/direct dimension then gives the direct sum.

Fires on one admissible minimal marked carrier with nonzero intersection.

### G5. Rank-8 existence

Recheck exactly the exposed witness over `F_5`:

```text
A = M direct-sum M,
X = [[0,1,0,3],
     [0,1,4,1],
     [0,1,4,2],
     [1,3,3,0]],
S = [[0,2 X^-1],
     [X,0]],
```

with

```text
X M = M^9 X,
S^2 = 2I = A^5,
S A S^-1 = A^9.
```

Fires if any identity fails.

### G6. Pair classification

Exploratory only. Decide `UNIQUE`, `NONUNIQUE`, or `STOP` for equivalence classes of minimal `(A,S)` pairs under `F_5` change of basis. No uniqueness threshold is frozen. `STOP` is permitted and does not affect G1-G5.

## 5. Two implementations

`verify.py` and `break.py` are frozen before the first execution.

- `verify.py`: filtration/Jordan-multiplicity route plus exact witness.
- `break.py`: determinant/parity route, partition attack, and direct top-line attack.

Both use Python standard library only and exact arithmetic modulo 5.

They are two implementations by the same session. Agreement is **not** independent confirmation and is **not** a public two-architecture gate.

## 6. Output and status discipline

After the pin:

- run both scripts exactly;
- record stdout bytes and SHA-256;
- preserve every fired falsifier;
- record only `candidate-T`, `candidate-D`, `candidate-C`, `F`, or `STOP` inside incubation bookkeeping;
- create no Registry or Frontier row;
- do not call the run public evidence.

A later formal public probe must start fresh under `probes/` and obey `POLICY.md` and `AGENTS.md` independently.
