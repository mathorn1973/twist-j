# P-J-QUADRATIC-CARRY-NORM-SEAM-2 result

Status: **candidate-T / L1 / SEAM-CERTIFIED LOCALLY / PUBLIC CANON STATUS UNCHANGED.**

The first formal execution of the fresh immutable successor verifier exited zero, wrote empty stderr, and produced the exact `EXPECTED.txt` bytes. All 20 audit checks passed. No scientific falsifier fired and no threshold, carrier, or scope moved.

The predecessor `P-J-QUADRATIC-CARRY-NORM-SEAM-1` remains permanently stopped with no scientific conclusion. This successor consumes none of its run output or verifier logic. Its repaired G4 audit derives the multiplicativity defect by exact polynomial arithmetic rather than a literal self-comparison.

## Candidate theorem

Let

```text
j = zeta_5,
K = Q(j),
K+ = Q(sqrt5),
c(j)=j^-1,
u(j)=j^2,
H(x)=x c(x),
q0(x)=Tr_(K+/Q)(H(x)),
q1(x)=(H(x)-u(H(x)))/sqrt5.
```

For `x=a+bj+cj^2+dj^3`, the exact quadratic components are

```text
q0 = 2(a^2+b^2+c^2+d^2) - (ab+ac+ad+bc+bd+cd),
q1 = ab-ac-ad+bc-bd+cd.
```

`q0` is the registered invariant quadratic line, while `2q1` is the registered `epsilon` line. Under the frozen affine generators, `q0` is invariant and `q1` changes by the quadratic character.

### 1. Unique binary coalescence

The coefficient difference `q0-q1` has nonzero-coefficient gcd exactly `2`. Therefore, for a rational prime `ell`,

```text
q0 mod ell = q1 mod ell    iff    ell = 2.
```

At `ell=2` both become

```text
e2(a,b,c,d)=ab+ac+ad+bc+bd+cd.
```

The parent theorem `J-BINARY-NORM-DESCENT [T]` already owns the typed identification of the invariant line's mod-two reduction with the `F_16/F_4/F_2` norm-trace form and its explicit isometry to the registered Boolean carry form. The new seam is that the sign line has the same binary shadow and that prime two is the unique rational prime where these two registered character channels coalesce.

### 2. Relative norm reconstruction

The two channels reconstruct the complete relative norm:

```text
H(x)    = (q0(x)+sqrt5 q1(x))/2,
u(H(x)) = (q0(x)-sqrt5 q1(x))/2.
```

Thus the carry shadow is not an isolated binary statistic. It is the characteristic-two coalescence of the two rational coordinates that separate again over characteristic zero to recover the `Q(sqrt5)` norm.

### 3. Multiplicativity removes the continuous ambiguity

The frozen affine-covariant family

```text
F_(A,B)(x)=A q0(x)+B sqrt5 q1(x)
```

has two free rational coefficients before further structure. Normalization `F(1)=1` gives `A=1/2`. For the single frozen witness `x=1+j`, the verifier independently computes

```text
q0(x)=3, q1(x)=1, q0(x^2)=7, q1(x^2)=3,
F(x^2)-F(x)^2=(5/4)(1-4B^2).
```

Hence multiplicativity forces exactly

```text
B=+1/2 or B=-1/2.
```

These are precisely `H` and `u o H`, the Galois pair. Multiplicativity therefore removes the rational mixing freedom but does not choose an orientation between the two real embeddings.

### 4. Existing face weights recovered

For `x_k=1+j^k`, `k=0,...,4`,

```text
q0 = (8,3,3,3,3),
q1 = (0,1,-1,-1,1),
H  = (4,(3+sqrt5)/2,(3-sqrt5)/2,(3-sqrt5)/2,(3+sqrt5)/2).
```

The last vector is exactly the already-public algebraic `BORN-FACE-WEIGHTS [T]`. This probe adds a seam/dependency theorem only and earns no duplicate evidence credit for those weights.

### 5. Invariant-only no-go

```text
q0(1+j)=q0(1+j^2)=3,
H(1+j)!=(H(1+j^2)).
```

So the unique invariant scalar quadratic line alone cannot reconstruct the face weights. The `epsilon` line is essential.

## Status ceiling

The written proof in `PREREG.md` carries the universal algebraic argument. The local verifier is an exact audit. This supports at most a later public row

```text
J-QUADRATIC-CARRY-NORM-SEAM [T], L1
```

after the required pull-request x86_64/aarch64 byte-identical checks and a separate Canon fold. Until that fold, Public Canon v67 is unchanged.

## Scope firewall

No statement here says that Boolean carry derives `J`, selects `Q(zeta_5)`, or forces a physical read place. No algebraic face weight is promoted to probability. `MEASURE-BORN-VERB [D]`, `TM-SYM2-PHYSICAL-MEASURE [D]`, `TWO-PLACE-PHYSICS [D]`, `READING-SPLIT [D]`, and `QUADRATIC-DECODER-DATA [O]` do not move.

No decoder, apparatus, event, observer, measurement, spacetime, force, SI bridge, empirical result, or L2-L6 lift is claimed.

## Pin and local run

```text
public claim issue:       #622
preregistration pin:      440705a2dfb5a320e0a0ea3905cab93b2843fe24
verifier sha256:          0c80346bb502a262a7635252c50f0ce8fff231fc2466b695dc488df6208e50f5
local architecture:       x86_64
local exit:               0
local stderr bytes:       0
local stdout bytes:       1564
local stdout sha256:      650241cf430bced0a2e4e3f41bb8cb87152ded466fe5cdfc1ec74e9dd2bbfe38
```

The local run is one architecture lane only. Public theorem status is not claimed by this result file.
