# RESULT

Status: **PASS / candidate-T proof package / non-canonical**

Probe: `P-MATTER-SCALAR-TEMPORAL-CHARACTERISTIC-1`  
Public issue: #743  
Formal pin: `38ef6a4a528689b45a1b8694d69d8aae9554570c`

The pinned verifier exited `0`, wrote empty stderr, and matched
`EXPECTED.txt` byte for byte.

## Scientific result

The written proof and exact audit establish the complete scalar temporal
kinematics at the declared mathematical scope.

### 1. Exact characteristic and transfer class

For

```text
q_mu(k)=s(k)+mu^2
```

the recurrence has

```text
P_q(zeta)=zeta^2+(q-2)zeta+1,
T_q=[[2-q,-1],[1,0]],
det T_q=1,
Delta_q=q(q-4).
```

Consequently:

```text
q=0       non-identity parabolic double root at +1
0<q<4     distinct elliptic unit-modulus roots
q=4       non-identity parabolic double root at -1
q>4       real reciprocal hyperbolic roots; no real omega
```

Proposed rows:

```text
MATTER-SCALAR-TEMPORAL-CHARACTERISTIC candidate-T
MATTER-SCALAR-BRANCH-CLASSIFICATION   candidate-T
```

### 2. Zero-momentum gap

At the unique spatial zero,

```text
q_mu(0)=mu^2,
cos omega_0=1-mu^2/2.
```

Thus `0<mu<2` gives a positive dimensionless angular gap,
`mu=2` gives the `-1` parabolic endpoint, and `mu>2` has no real
zero-momentum frequency.

This is a spectral parameter statement, not a physical mass derivation.

### 3. Global safe range

The Public Canon v74 estimate

```text
0<=s(k)<=16/9
```

gives

```text
0<=mu^2<=20/9  =>  0<=s(k)+mu^2<=4
```

for every momentum. The value `20/9` is sufficient and is not asserted sharp.
At `mu^2=4`, only the spatial zero is parabolic and every nonzero momentum is
hyperbolic; above `4`, every momentum is hyperbolic.

### 4. Massive Hermitian germ and scaling

For the standard Hermitian carrier,

```text
det H=Omega^2-|k|^2.
```

The scalar massive shell is

```text
det H=M^2,
```

and the unique scaling yielding a finite nonzero mass term is

```text
mu_epsilon=epsilon M.
```

It obeys the exact inherited remainder

```text
-(epsilon^2/12) Omega^4
 <=q_(epsilon,M)-(Omega^2-|k|^2-M^2)
 <=(11/27) epsilon^2 |k|^4.
```

For `mu_epsilon=epsilon^alpha M`, `alpha>1` becomes massless and `alpha<1`
diverges. A fixed nonzero lattice `mu` therefore does not define a finite
continuum mass.

Proposed row:

```text
MATTER-SCALAR-MASSIVE-GERM candidate-T
```

## Boundary

This result does not derive:

```text
the value of mu
particle species or multiplicity
spin or a first-order matter equation
charge or coupling to the L4 photon phase
interaction, self-energy, stability or decay
occurrence or apparatus law
physical units or an SI mass
```

It opens exact massive kinematics while leaving the physical mass-origin and
matter-reading programs open.

## Exact stdout

```text
PROBE P-MATTER-SCALAR-TEMPORAL-CHARACTERISTIC-1
EXPOSURE RESULT_EXPOSED_PROOF_AUDIT
CHARACTERISTIC zeta^2+(q-2)zeta+1
TRANSFER_DETERMINANT 1
DISCRIMINANT q(q-4)
BRANCH_CLASS q=0:PARABOLIC_PLUS;0<q<4:ELLIPTIC;q=4:PARABOLIC_MINUS;q>4:HYPERBOLIC
ZERO_MOMENTUM q=mu^2;cos(omega0)=1-mu^2/2
MASSLESS_APEX mu^2=0:zeta=1_DOUBLE_NONIDENTITY
SAFE_ALL_MOMENTA_REAL_MU2_BOUND 20/9
HERM2_MASS_SHELL det(H)-M^2=Omega^2-|k|^2-M^2
SCALING mu=epsilon^alpha*M;alpha=1_UNIQUE_FINITE_NONZERO
REMAINDER temporal=1/12;spatial=11/27
NEGATIVE_CONTROLS mass_sign,temporal_sign,fixed_mu,wrong_scaling PASS
FALSIFIERS NONE
RESULT PASS
```

## Integrity

```text
verify.py sha256: 37da04c1f44759f079c1eb233b84460ad7896bcb3cee72caae689a39b590387a
stdout sha256:   aff791912f217684a9a7622f820a20d6f7325e1224acf1e7a8605f0436e10be1
stderr sha256:   e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

No Canon, Registry, Gate, Frontier, release, workflow or status file changes
in this probe.
