# PROMO-C-J-NORM-ONE-TRACE-KERNEL-SEAM-1-N

**Status:** NON-CANONICAL promotion package. No promotion occurs by this file.

## Source

```text
candidate:       C-J-NORM-ONE-TRACE-KERNEL-SEAM-1-N
issue:           #659
branch:          notes/c-j-norm-one-trace-kernel-seam-1-n
prereg commit:   a3f4fb2fb038497433153b7b8448f6ee0c9d7636
breaker commit:  631caadbe002ac386cb3387a27adae949cba88f8
verifier commit: 1ced13ab46f4e37417f4cab5d78e8bb065a0cac8
local verdict:   CANDIDATE-T / L1
```

## Proposed public attack

```text
probe:  P-J-NORM-TRACE-TANGENT-SEAM-1
branch: probe/P-J-NORM-TRACE-TANGENT-SEAM-1
layer:  L1
```

The name was collision-scanned against public issues, pull requests, remote refs, and the Registry on 2026-08-29. A formal probe must repeat that scan before lock.

## Proposed theorem outputs

### NORM-ONE-TANGENT-TRACE

For every finite separable extension `E/Q`, with

```text
T_E^1 = ker(N_E/Q : Res_E/Q G_m -> G_m),
```

one has

```text
d(N_E/Q)_1 = Tr_E/Q,
Lie(T_E^1) = ker Tr_E/Q,
dim T_E^1 = [E:Q]-1.
```

After an ordered split base change,

```text
T_E^1 ~= {(x_i) in G_m^n : product_i x_i=1} ~= G_m^(n-1).
```

### J-INTEGRAL-NORM-TRACE-SEAM

For `K=Q(zeta_5)` in the ordered integral basis `(j,j^2,j^3,j^4)`,

```text
Tr(sum_a x_a j^a) = -sum_a x_a,
Lambda_rel = O_K intersect ker Tr ~= A_3,
Lambda_rel/5Lambda_rel ~= ker(sum:F_5^4->F_5)=W_5.
```

This identifies the public residual trace carrier as the mod-five reduction of the integral tangent lattice of the norm-one torus. `TRACEKERNEL-RESIDUAL-FORM [T]` retains ownership of the residual form and its existing scope.

### J-NORMONE-DIMENSION-RANK-FIREWALL

For the same `K`,

```text
T_K^1(R) ~= R_(>0) x S^1 x S^1,
dim_R T_K^1(R)=3,
O_K^*=mu_10 x <phi>,
rank O_K^*=1.
```

The first two statements are proved directly. The unit-group product is inherited from `J-HARMONIC-SEAM [T]` and receives no new evidence credit.

## Public dependencies

```text
J-UNIT [T]
J-HARMONIC-SEAM [T]
TRACEKERNEL-RESIDUAL-FORM [T]
```

Context-only comparisons, not dependencies:

```text
ARITHMETIC-RAPIDITY-DECOMPOSITION [T]
QPAIR-CROSS-SECTOR-NONDESCENT [T]
PURE-QUBIT-LOCAL-RELATION-PYTHAGORAS [T]
```

## Proof carrier

The proof is self-contained except for the inherited unit-group product.

1. Split the restriction of scalars over a splitting field.
2. Differentiate the product norm with dual numbers.
3. Use the integral basis `(j,j^2,j^3,j^4)` and the trace of nontrivial fifth roots.
4. Reduce the split exact trace sequence modulo five.
5. Write the real points as `C^* x C^*` with one norm equation.
6. Place `J` on the carrier using `J phi=j`.

## Exact audit carrier

```text
break.py sha256:
  f7498300ac807b4b56511ea60fec0d0b25844ddd8ea0e1c0b7f94cae375c4826

verify.py sha256:
  b1ff048c01ffa51a3d77dde2d521d869aae41ed0e4c98d69450a6386abbd30f9
```

The breaker was frozen before the positive verifier. Both are standard-library, exact-arithmetic scripts. Their present runs are same-session and one-architecture only.

## Frozen falsifier

The proposed theorem fires if any of the following occurs:

```text
1. d(N)_1 differs from Tr for a finite separable extension.
2. Lie(T_E^1) differs from ker Tr or has dimension other than n-1.
3. (j,j^2,j^3,j^4) is not an integral basis or has trace row other than (-1,-1,-1,-1).
4. Lambda_rel/5Lambda_rel is not exactly W_5.
5. T_K^1(R) is not R_(>0) x S^1 x S^1.
6. The exact J embedding or norm identities fail.
7. A claimed firewall is removed or contradicted.
```

An integrity mismatch without an exact mathematical negation is STOP, not a scientific falsifier.

## Mandatory guards

```text
No claim that dimension three selects p=5 or J.
No equality of the global norm-one locus with the additive trace kernel.
No identification of torus dimension with integral-unit rank.
No canonical orientation from an ordered split chart.
No physical space, force, decoder, measure, observer, SI, or L2-L6 claim.
No derivation or selection of J.
No global decoder-uniqueness claim.
```

Exact counter-witnesses that must remain visible:

```text
N(J)=1,       Tr(J)=3,
Tr(j-j^2)=0,  N(j-j^2)=5.
```

## Promotion recommendation

The candidate is ready for a formal L1 public probe. The theorem-grade proof can support `T`; the verifier is an audit and must not be presented as independent proof. A formal computation run must occur only after the new probe preregistration and verifier are pinned on the probe branch. Public Canon and Registry edits remain deferred to a later fold.
