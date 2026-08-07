# P-PAULI-CARRIER-ALGEBRA-1 preregistration

**Status:** PUBLIC PROBE PREREGISTRATION CANDIDATE. No formal execution before the remote pin.

**Claim issue:** #296  
**Program issue:** #295  
**Branch:** `probe/P-PAULI-CARRIER-ALGEBRA-1`  
**Path:** `probes/P-PAULI-CARRIER-ALGEBRA-1/`  
**Owner:** A. M. Thorn / claiming session  
**Action layer:** L4 support only

## Authority

Frozen against Public Canon v39 as read from public `main` at claim time:

```text
STATE:          ACTIVE
CANON:          Public Canon v39
AUTHORITY:      mathorn1973/twist-j main
TAG:            canon-v39
CONTENT_COMMIT: ab17b10412d03bf1cd69791fe22c66252502b2d4
CANON_SHA256:   698df2212f0bc782de2fb50ff04fb4026d1e276743d6fae7f10607cca770b556
CANON_BYTES:    187370
```

The tag was read back tree-identical to `main`, the content commit was read back as an ancestor, and `canon/SHA256SUMS` carried the declared Canon hash before this preregistration candidate was prepared.

## Result exposure

This probe is **RESULT-EXPOSED / confirmatory**. Before the public pin, non-canonical incubation and dry-run work found the expected Pauli relations and a one-dimensional invariant alternating space. Those outputs are excluded from evidence. This document freezes the scope, accepted verifier, exact carrier, claims and falsifiers before the first formal execution.

## Six frozen preregistration fields

### 1. Equation / claim family

On the sign quotient

```text
F5x = {1,2,3,4}
H   = {1,4} = {+1,-1}
V+  = F5x/H = {Q,N}
Q   = {1,4}
N   = {2,3}
ordered basis = (e_Q,e_N)
```

let `X` be multiplication by `2` on the quotient, `Z` the unique nontrivial quadratic character (`+1` on `Q`, `-1` on `N`), and `B = X Z`.

On the public marked integral binary-icosahedral branch, freeze

```text
K = Q(zeta_5),
S = [[0,-1],[1,0]],
T = [[zeta_5,1],[0,zeta_5^4]].
```

The probe decides P1 through P5 below.

### 2. Accepted code

Exactly one accepted verifier:

```text
probes/P-PAULI-CARRIER-ALGEBRA-1/verify.py
```

It uses the Python standard library only, exact integers, `Fraction`, the exact cyclotomic basis of `Q(zeta_5)`, and a coefficient dictionary for the generic polynomial identity. It reads no file and forms no floating-point value.

The first formal run is forbidden until this preregistration file and this exact verifier are committed and pushed together in one immutable remote pin tree and then read back from GitHub.

### 3. Carrier / data

No external dataset.

Frozen carriers:

1. the ordered two-class quotient basis `(e_Q,e_N)` above;
2. the displayed ordered basis of the public `K^2` integral `2I` representative above;
3. the tensor basis `(e1 tensor e1, e1 tensor e2, e2 tensor e1, e2 tensor e2)` for P5.

The equality `B=S` is literal matrix equality **in the two separately frozen ordered bases**. It is not a basis-free physical carrier identification.

### 4. Systematics / known ambiguities

The following are explicitly controlled rather than hidden:

- swapping the quotient basis conjugates the displayed Pauli matrices but does not change the anticommutation algebra;
- rescaling a nonzero invariant bilinear form changes only its scalar, not the invariant line;
- `SPIN-LIFT-FORCED [F]` already proves that the marked D5 lift is not unique; this probe may use only determinant-one invariance common to all relevant finite lifts, never lift uniqueness;
- the characteristic-zero integral branch and the finite quotient branch are not declared physically identical by this probe;
- no positive Hermitian decoder Gram is imported from `COLOR-CM-2I-SEMILINEAR-PAIR`; that public theorem remains L4 and explicitly excludes decoder Q/QCarrier;
- no L5 stream or L6 measure is touched.

### 5. Failure thresholds

The probe is negative if any exact frozen predicate below fails. No tolerance exists.

```text
F1  multiplication by 2 fails to swap Q and N;
F2  chi_5(2) != -1 or Z X != - X Z;
F3  B != [[0,-1],[1,0]], B^T != -B, or B^2 != -I;
F4  the generic polynomial identity A^T B A = det(A) B fails;
F5  det(S) != det(T) != 1 or either generator fails to preserve B;
F6  the simultaneous invariant bilinear-form space has K-dimension != 1;
F7  a nonzero invariant symmetric bilinear form survives;
F8  the invariant subspace of K^2 tensor K^2 has dimension != 1;
F9  its frozen generator Omega is not invariant or is swap-even.
```

A failure to produce a basis-free physical identification is outside this scope and is not converted into a scientific negative. Any attempt to make that lift here is a protocol STOP.

### 6. Action layer / scientific decision

Layer is exactly **L4 support**.

Positive result:

```text
The two-class sign quotient carries the exact Pauli X/Z anticommutation;
B=XZ is the same integer matrix as the displayed S skeleton; and on the
frozen integral 2I branch the complete invariant bilinear-form space is the
single alternating K-line K B, equivalently the unique invariant tensor line
is swap-odd.
```

Negative result: any F1 through F9 fires.

STOP: any L5 locality, CAR/Fock completion, positive-energy interpretation, decoder Gram, QCarrier, MatterData, physical spin-statistics, or Pauli-exclusion conclusion is attempted inside this probe.

## Frozen exact claims

### P1. Quotient Pauli pair

```text
X = [[0,1],[1,0]],
Z = [[1,0],[0,-1]],
X^2 = Z^2 = I,
Z X = - X Z.
```

### P2. Common integer skeleton

```text
B = X Z = [[0,-1],[1,0]],
B^T = -B,
B^2 = -I.
```

In the frozen ordered bases this is the same displayed integer matrix as the `S` generator of `COLOR-INTEGRAL-LIFT` and the integer skeleton named by `SPIN-BISECTOR`.

### P3. Universal determinant identity

For a generic `2 x 2` matrix over every commutative ring,

```text
A^T B A = det(A) B.
```

This is a written polynomial identity, not a finite-sample claim. The verifier checks it coefficientwise in `Z[a,b,c,d]`.

### P4. Complete invariant bilinear-form classification

For arbitrary `M in Mat_2(K)`, the simultaneous equations

```text
S^T M S = M,
T^T M T = M
```

have solution space exactly

```text
K B.
```

Thus its `K`-dimension is one and the invariant symmetric subspace is zero.

### P5. Exchange line

With

```text
epsilon(v,w) = v^T B w,
Omega = e1 tensor e2 - e2 tensor e1,
```

one has

```text
epsilon(w,v) = -epsilon(v,w),
epsilon(v,v) = 0,
```

and the full invariant subspace of `K^2 tensor K^2` under the frozen generators is exactly `K Omega`, with tensor swap acting as `-1`.

## Written proof skeleton

P1 is the regular action/character relation on the two-element quotient: multiplication by `2` swaps the square and nonsquare classes and `chi_5(2)=-1`, so `ZX=-XZ`.

P2 is direct multiplication.

P3: for `A=[[a,b],[c,d]]`,

```text
B A = [[-c,-d],[a,b]],
A^T B A = [[0, cb-ad],[da-bc,0]] = (ad-bc) B.
```

P4 is a complete exact four-unknown linear system over `K`. The accepted verifier performs Gaussian elimination in the basis `1,zeta,zeta^2,zeta^3`; the resulting rank is three, contains `B`, and adding the symmetry equation makes the rank four.

P5 follows from the same determinant-one action on the top exterior line; the accepted verifier independently solves the four-dimensional tensor fixed-space system and checks the swap eigenvalue.

## Explicit nonclaims

No unique marked spin lift. No physical quotient-to-2I basis identification. No CAR. No full creation/annihilation algebra. No Fock or exterior many-body sector. No Hamiltonian or energy positivity. No locality. No `D_matter`, QCarrier, Born pairing, MatterData, measurement or physical Pauli exclusion. No L5 or L6 statement.

## Execution protocol after pin

1. Read back the pin commit and both blobs from GitHub and compare exact bytes and SHA-256.
2. Only then run `python3 probes/P-PAULI-CARRIER-ALGEBRA-1/verify.py` from repository root.
3. Require exit 0 and empty stderr.
4. Commit exact stdout as `EXPECTED.txt`, neutral environment metadata as `RUN.md`, and the result/fired-falsifier decision as `RESULT.md`.
5. Open a draft PR changing only this probe directory.
6. Required x86_64 and aarch64 GitHub jobs must reproduce the same committed stdout byte for byte before any computation-only status is earned.
7. A later Canon fold, not this probe PR, decides registry status wording.
