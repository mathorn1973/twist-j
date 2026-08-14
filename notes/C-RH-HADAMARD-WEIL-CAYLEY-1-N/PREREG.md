# C-RH-HADAMARD-WEIL-CAYLEY-1-N preregistration

```text
STATUS:        NON-CANONICAL INCUBATION
AUTHORITY:     none
PUBLIC BASIS:  Public Canon v46, mathorn1973/twist-j main
ISSUE LOCK:    #371
TARGET LINE:   PUBLIC
LAYER:         analytic/number-theoretic only; no L1-L6 physical lift
OWNER:         current ChatGPT owner session
```

This file is the computation pin. No result observed after this commit may move the objects, gates, or decision vocabulary below.

## 1. Frozen objects

Let

```text
rho       = beta + i gamma,
0 < beta < 1,
gamma != 0,
rho_star  = 1 - conjugate(rho),
xi(rho)   = 1 - 1/rho.
```

The pair `rho,rho_star` is treated symbolically. No zero table is an input.

Use the normalized Hadamard matrix

```text
H2 = (1/sqrt(2)) [[1,1],[1,-1]].
```

If `xi = r exp(i alpha)` with `r>0`, define the power-pair vector

```text
v_n = (xi^n, xi_star^n)^T,   n >= 1,
(s_n,a_n)^T = H2 v_n.
```

The public rows `LAMBDA-COCYCLE-BRANCH-COLLAPSE`, `LAMBDA-COCYCLE-GRID-EQUIVALENCE`, and `LAMBDA-COCYCLE-ANGLES` retain exactly their registered scopes. Issue #363 is an inherited bounded no-go against finite strictly-positive moment-profile discrimination on the dense lambda grid.

## 2. G1 CAYLEY-PAIR

Prove exactly, without RH,

```text
xi(rho_star) = 1/conjugate(xi(rho)),
|xi(rho)| = 1 iff beta = 1/2.
```

Fires on one symbolic counterexample or an algebraic gap.

## 3. G2 HADAMARD-RADIAL-SPLIT

Derive exact formulas for `|s_1|^2` and `|a_1|^2`, both in `(r,alpha)` and in `(beta,gamma)`. Required success condition:

```text
|a_1|^2 >= 0,
|a_1|^2 = 0 iff beta = 1/2.
```

Also freeze the positive 2 x 2 channel matrix obtained by pulling `diag(|s_1|^2,|a_1|^2)` back through `H2`, and record rank on and off the critical line.

## 4. G3 POWER-LADDER

For every integer `n>=1`, derive

```text
|s_n|^2,
|a_n|^2,
```

and a recurrence in `n` using only the radial invariant `r+r^-1` or an equivalent exact scalar. Determine whether the sequence adds information beyond its first radial parameter.

## 5. G4 SIGNATURE-COMPARISON

Compare with a generic real Hermitian off-line pair block

```text
B_m = [[0,m],[m,0]],  m>0,
```

whose inertia is `(1,1)` and whose Hadamard diagonal form is `diag(m,-m)`.

Classify the Cayley construction as exactly one of:

```text
SHARPER
EQUIVALENT
PARTIAL
```

where `SHARPER` requires a basis-independent scalar/rank datum not fixed by inertia alone, and `PARTIAL` requires such a datum but no source-side access under G5.

## 6. G5 PRIME-SIDE ACCESS

Admitted source-side quantities are finite linear combinations of classical explicit-formula / public Li-Cayley power-sum data. A proposed access identity must eliminate individual zero pairing, conjugation labels, and nonlinear per-zero operations algebraically.

The route fails this gate if the radial defect requires nonlinear zero-side pairing or modulus data not expressible in the admitted linear source layer.

No use of RH, Weil positivity, or an assumed positive zero measure is allowed.

## 7. G6 FINITE-PROFILE CONTROL

If a proposed finite discriminator depends only on one strictly positive finite Toeplitz/trigonometric moment profile, compare it against issue #363. Such a discriminator is dead if #363 supplies exact grid-supported representations with identical frozen moments and arbitrary conductor tail.

This gate is a scope boundary, not a new proof of #363.

## 8. G7 BREAKER

Freeze an independent breaker before reading the verifier output. It must attack:

```text
B1  functional-pair Cayley algebra,
B2  critical-line iff condition,
B3  Hadamard channel norms and rank,
B4  claim that H2 itself adds information rather than changing basis,
B5  any claimed prime-side linearization,
B6  any finite-profile grid discriminator already excluded by #363.
```

The breaker must be derived from this preregistration, not from `verify.py`.

## 9. Decision

```text
candidate-T
    one or more complete exact lemmas survive G1-G7.

candidate-D
    an exact synthesis follows from theorem-grade ingredients but the source-side interpretation is conditional.

candidate-C
    a finite exact witness only.

F
    the proposed Hadamard-Weil-Cayley advantage is killed at its frozen scope.

STOP
    authority/collision drift, untyped source access, circularity, missing breaker, or incomplete proof.
```

The specific advantage is `F` if every nontrivial Hadamard datum is either generic inertia/congruence information, inaccessible nonlinear zero-side data, or a finite-profile discriminator neutralized by #363.

## 10. Firewall

No RH/GRH status movement. No Canon, Registry, frontier, release, Born, decoder, zeta_8, physical, SI, J-native Weil-realization, or L1-L6 conclusion. A later promotion needs a separate public fold under the then-current procedure.
