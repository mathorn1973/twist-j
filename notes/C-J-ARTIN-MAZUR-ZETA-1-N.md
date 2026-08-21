# C-J-ARTIN-MAZUR-ZETA-1-N

Status: **NON-CANONICAL / RESULT-EXPOSED / NO FORMAL RUN**.

This note isolates one exact candidate from historical exploratory material.
It changes no Canon, registry, frontier, evidence row, gate, or scientific
status. Historical status labels and internal version numbers are not imported.

Currency was checked against public `main` on 2026-08-20. `STATUS.md` remains
the sole authority. Public Canon v55 is active at the time of this note, and
release PR #453 for v56 is open. The release candidate is not used as an
authority or premise.

## 1. Scope and source boundary

The public inputs are only the registered L1 and L2 objects:

- `J-STEP [T]`, giving the integer multiplication matrix of
  `J = 1 + zeta_5^2`;
- `C20-TEICHMULLER-SPLIT [T]`, giving the order-twenty and regular-unipotent
  structure of its reduction modulo five.

The candidate concerns two Artin-Mazur dynamical zeta functions:

1. the toral automorphism induced by `M_J` on `R^4/Z^4`;
2. the permutation induced by `M_J mod 5` on `F_5^4`.

They are not Dedekind zeta functions, Euler factors, or p-adic zeta functions.
The notation below keeps all four uses of the word zeta separate.

## 2. Falsifiers first

The candidate fails if any of the following occurs:

1. the reduction `M_J mod 5` has a cycle length or multiplicity other than
   `1, 4, 20 x 31`;
2. the formula for `Fix_5(n)` disagrees with direct action on any state;
3. any exterior-power polynomial `P_k(z)` below is incorrect;
4. some `det(I-M_J^n)` is nonpositive, so the Lefschetz counts cannot be
   identified with Artin-Mazur fixed-point counts as written;
5. a coefficient of `log Z_AM,infinity` differs from
   `Fix_infinity(n)/n`;
6. the proposed probe imports a production-kernel, measure, physical-mixing,
   or RH statement.

An integrity mismatch in a future pinned bundle is a STOP. It is not itself a
mathematical counterexample.

## 3. The finite reduction

Let `M` be `M_J mod 5`. From `C20-TEICHMULLER-SPLIT`, put

```text
U = M^16 = 3M,
N = U - I,
N^4 = 0 != N^3.
```

On the four-dimensional carrier this makes `N` one regular nilpotent block.
Thus `ker N` is one-dimensional. Since `M = 2U`, the zero vector is fixed and
the four nonzero vectors of `ker N` form one cycle of length four under scalar
multiplication by `2`.

For `x` outside `ker N`, the `U`-period is exactly five. A shorter `M`-period
cannot arise by cancellation between the scalar and unipotent parts: when
`2^k != 1`, a power of a unipotent matrix has no nonzero eigenvector with
eigenvalue `2^(-k) != 1`; when `2^k = 1` but `5` does not divide `k`, the
`U`-part does not fix `x`. Hence every remaining point has period twenty.

Therefore

```text
625 = 1 + 4 + 31*20,
```

and the candidate formulas are

```text
Fix_5(n) = 1 + 4[4 divides n] + 620[20 divides n],

Z_AM,5(z) = 1 / ((1-z)(1-z^4)(1-z^20)^31).
```

This is a theorem about the complete finite permutation on `F_5^4`. It does
not explain the support sizes of the six-register production kernel.

## 4. The toral automorphism

Use the public matrix

```text
M_J = [[1,0,-1,1],
       [0,1,-1,0],
       [1,0, 0,0],
       [0,1,-1,1]].
```

For `0 <= k <= 4`, define

```text
P_k(z) = det(I - z wedge^k M_J).
```

Exact exterior-power arithmetic gives

```text
P_0(z) = P_4(z) = 1-z,
P_1(z) = 1-3z+4z^2-2z^3+z^4,
P_2(z) = 1-4z+5z^2-5z^3+5z^4-4z^5+z^6,
P_3(z) = 1-2z+4z^2-3z^3+z^4.
```

The eigenvalues occur in two nonreal conjugate pairs. For every positive
integer `n`, `det(I-M_J^n)` is therefore a product of two positive squared
moduli. The absolute fixed-point count equals the Lefschetz count. The standard
exterior-power identity then gives the candidate Artin-Mazur factorization

```text
Z_AM,infinity(z) = P_1(z) P_3(z) / ((1-z)^2 P_2(z)).
```

The first singularity has radius `phi^(-2)`, consistent with fixed-point growth
rate `2 log phi`. One exact audit witness is

```text
Fix_infinity(20) = 228765625 = 5^6 * 11^4.
```

The entropy statement itself is outside this note. It is handled by the
already merged probe `P-ENTROPY-RESIDUE-MATH-1` and by the separate v56 fold.

## 5. Non-formal audit

A fresh standard-library calculation, performed before this note was written,
checked the complete finite cycle census, the finite fixed-point formula
through `n=80`, all five exterior-power determinant polynomials, toral
fixed-point counts through `n=24`, and the displayed `n=20` witness. All checks
passed with integer arithmetic.

This was a one-platform, result-exposed, non-formal calculation. No script or
stdout from it is public evidence, and no public computation status is earned.

## 6. Proposed formal route

After the v56 release lane is complete and a fresh collision check passes, the
proper public object is one proof-first probe:

```text
probe:   P-J-ARTIN-MAZUR-ZETA-1
branch:  probe/P-J-ARTIN-MAZUR-ZETA-1
path:    probes/P-J-ARTIN-MAZUR-ZETA-1/
layers:  L1 finite reduction and L2 toral manifold
```

The preregistration should freeze the two carriers, all five polynomials, the
cycle proof, the sign argument, the coefficient comparison, and exact failure
thresholds before the first formal execution. Enumeration should audit the
cycle theorem, not replace it.

The intended ceiling is theorem-grade mathematics at the displayed scopes.
No status is requested by this note.

## 7. Explicit non-claims

- no derivation of production-kernel support size twenty;
- no bridge from `F_5^4` to the public checkpoint carrier `F_5^6`;
- no claim about the size-ten production support;
- no L5 stream or L6 measure;
- no Markov chain, mixing time, spectral gap, or physical entropy;
- no p-adic entropy or adelic carrier;
- no Dedekind zeta, local Euler factor, or Riemann hypothesis statement;
- no physical interpretation of a pole or periodic orbit.

The shared integer twenty is an observation on two different carriers until a
separate public intertwiner or impossibility theorem is supplied.
