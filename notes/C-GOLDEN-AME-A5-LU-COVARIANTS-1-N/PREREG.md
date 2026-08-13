# C-GOLDEN-AME-A5-LU-COVARIANTS-1-N — preregistration

Status: **NON-CANONICAL INCUBATION**  
Layer: **L1 exact invariant theory**  
Lock: [issue #366](https://github.com/mathorn1973/twist-j/issues/366)  
Created: 2026-08-13  
Canon writes: **forbidden**  
Formal hypothesis computation before this pin: **none**

## 1. Purpose and strict scope

The exact negative in `C-GOLDEN-AME-TWOPLACE-1-N` ruled out a six-line `A5`
action only when every local operator was monomial. This incubation tests a
strictly larger class:

```text
rho_q : A5 -> U(6), q=0,1,2,3,
rho_q unitarily equivalent to the multiplicity-free representation 1+5,
(rho_0(g) tensor rho_1(g) tensor rho_2(g) tensor rho_3(g)) A = A.
```

The four conjugating unitaries may be arbitrary complex unitaries. They need
not be monomial or defined over `Q(zeta_40)`. No six-line incidence basis is
selected. A party action adds nothing: every homomorphism `A5 -> S4` is
trivial, since `A5` is simple and `|A5|>|S4|`.

## 2. Authority and source

| Item | Frozen value |
|---|---|
| Canon | Public Canon v46 |
| Authority | `mathorn1973/twist-j` `main` |
| Activation commit | `6545c1d0de61ff4696eb3de1a258139e8891f436` |
| Content commit | `62628ca4da2d938e4e3a122d35c0d93a6debc27f` |
| Canon SHA-256 | `6c57e714c441bd679b9f6c673352cfae44ac993433d7c4624cd9c3c93df291ff` |

The sole tensor input is `matrix-toolbox/AME_4_6` commit
`1fa4a4d4d2b9a3c6d3b6c8d802116415fb679fe8`, file `AME46_ORIGINAL.m`,
8515 bytes, Git blob `e0d0e171d58b3360c39595d677ffc401a466112d`, SHA-256
`55fbc0ba2747b4e5adc5a5abd15ac7241a461ff8182268ebdae464d8a29cc9ae`.
Use `A[i,j,k,l]=U[6i+j,6k+l]` without a preliminary gauge change.

All exact arithmetic uses `K=Q[z]/Phi_40(z)`, `z=zeta_40`, and the selected
conjugation `bar(z)=z^-1`.

## 3. Frozen one-leg covariants

Fix a leg `q` and an integer `n>=2`. Take `n` labeled copies `A^(r)` and `n`
copies `bar(A)^(s)`, with `r,s=0,...,n-1`. The index of `A^(0)` on leg `q`
is the open row index `i`; the index of `bar(A)^(0)` there is the open column
index `j`.

Choose a permutation `pi_q` of `{1,...,n-1}` and, for every `ell!=q`, a
permutation `pi_ell` of `{0,...,n-1}`. Contract by

```text
x_q^(r) = y_q^(pi_q(r))             for r=1,...,n-1,
x_ell^(r) = y_ell^(pi_ell(r))       for ell!=q, r=0,...,n-1.
```

The sum of the product of all `n` tensor entries and all `n` conjugate entries
is a `6 x 6` matrix `C(q,n,pi)[i,j]`. Direct index cancellation gives, for
every local unitary tuple,

```text
C_q((V_0 tensor ... tensor V_3)A) = V_q C_q(A) V_q^dagger.
```

This covariance identity must be proved symbolically in the result and
checked on deterministic exact test matrices; the numerical test is an audit,
not the proof.

The raw frozen diagram count on each leg is

```text
n=2: 1!*2!^3 = 8,
n=3: 2!*3!^3 = 432.
```

Diagrams are ordered lexicographically by `q`, then `pi_q`, then the other
three leg permutations in increasing leg order. No connectedness filter or
post-hoc diagram deletion is allowed.

## 4. Schur hard breaker

Assume the scoped `A5` action exists. Balanced contractions cancel the group
action on every closed wire, hence every matrix on leg `q` commutes with
`rho_q(A5)`. The representation `1+5` is a sum of two inequivalent irreducibles
with multiplicity one, so Schur's lemma gives

```text
End_A5(1+5) = C direct-sum C.
```

Consequently, on every leg:

1. all frozen covariants commute;
2. the unital star-algebra they generate has dimension at most two; and
3. every nonscalar Hermitian member has eigenvalue multiplicities `1+5`.

Any one exact violation is a universal negative for the entire scoped
arbitrary-local-unitary class. It does not merely reject one basis.

## 5. Deterministic computation

### G0 — replay

Reproduce the pin, 112-entry support, exact 2-unitarity, and entry field
`Q(zeta_40)`. Mismatch is integrity STOP.

### G1 — covariance and diagram census

Publish the index proof above. Generate exactly 8 diagrams for `n=2` and 432
for `n=3` on each leg. Hash the deterministic list.

### G2 — finite-field locator

Reduce the power basis at the frozen good prime

```text
z -> 6 in F_41,
```

where 6 is the least positive element of order 40. Conjugation becomes
`6 -> 6^-1`. Compute all eight `n=2` covariants. If no hard breaker fires,
scan the `n=3` diagrams in frozen order and compare each new matrix with all
previous matrices on that leg. Stop at the lexicographically first nonzero
commutator or third independent matrix.

A nonzero modular determinant or entry can locate and certify exact
nonvanishing because all denominators are prime to 41. A zero modular test is
not evidence of exact vanishing.

### G3 — exact witness

Recompute every matrix used by the first modular witness in `Q(zeta_40)`.
Publish:

- both complete diagram descriptors;
- the first nonzero commutator entry in row-major order;
- its 16 rational power-basis coefficients;
- direct exact substitution and the nonzero reduction modulo 41; and
- an independently written verifier or a second contraction ordering.

If the witness is algebraic dimension rather than a commutator, publish the
nonzero exact minor. If a Hermitian spectral witness is used, publish its
exact characteristic polynomial and multiplicities.

### G4 — verdict

- Any exact G3 witness: `EXACT NO` for all scoped local-unitary `1+5` actions.
- No witness through every frozen `n<=3` diagram: `INCONCLUSIVE`; this is not
  evidence for an action.
- A positive bridge requires explicit exact `rho_q` matrices satisfying all
  group and tensor equations and is not inferable from surviving covariants.

## 6. Firewalls

No numerical tolerance, approximate diagonalization, guessed `A5` basis,
monomial restriction, or post-hoc contraction family may decide the result.
The test neither compares the tensor with the Gross--Goedicke artisanal
solutions nor proves or refutes arbitrary perfect-tensor equivalence.

No outcome promotes `TWO-PLACE-PHYSICS`, the six-line frame, color, a decoder,
Born probability, error correction, fault-tolerant hardware, or any L2--L6
claim. This notes branch changes no Canon or Registry file.

