# PROMO C-OMEGA-U-UNITY-4-CARRIER-MINIMALITY-1

**Status:** NON-CANONICAL promotion package. No promotion occurs by this file.

## Recommended public target

If owner review accepts the incubation proof, open a fresh formal probe, suggested name:

```text
P-J-BISECTOR-CARRIER-MIN-1
```

Layer: `L1` only.

Do not reuse the incubation branch, scripts, stdout, or pin as formal evidence. Re-author the public preregistration from current `main` and run the repository's required two-architecture procedure.

## Proposed theorem scope for review

For a finite-dimensional `F_5` carrier `(V,A,S)` satisfying

```text
A^5 = 2I,
ord(A)=20,
S^2=2I,
SAS^-1=A^9,
```

and containing the public `J_4(2)` J-module as an A-invariant submodule:

1. every exact Jordan-block multiplicity of `A-2I` is even;
2. `dim_F5(V) >= 8`;
3. at dimension 8 the A-module is uniquely `J_4(2) direct-sum J_4(2)`;
4. every embedded public rank-4 module `P0` satisfies `V=P0 direct-sum S(P0)`;
5. dimension 8 is attained by an explicit exact construction over the unchanged base field `F_5`.

The public probe must preserve the predecessor falsification: it may not claim that ambient scalar extension to `F_25` is necessary.

## Proposed proof spine

```text
A^5=2I
 -> N=A-2I has N^5=0
 -> SNS^-1=N u(N), u(0)=4 != 0
 -> canonical exact-size Jordan quotients E_r are S-invariant
 -> S^2=2I on each E_r
 -> x^2-2 irreducible over F_5
 -> dim_F5(E_r) even
 -> embedded J4 requires a block of size >=4
 -> dimension >=8
 -> at dimension 8 only (4,4)
 -> top V/NV is F_5^2 with Sbar^2=2I and no invariant line
 -> P0 and S(P0) are transverse
 -> explicit doubled witness closes existence.
```

A second determinant proof should remain in the formal breaker:

```text
det(S|E_r)^2 = 2^(dim E_r),
```

which is impossible for odd dimension because `2` and `3` are nonsquares mod 5.

## Explicit nonclaims

The formal target must not claim:

- uniqueness of the full minimal pair `(A,S)`;
- a physical choice between scalar extension and carrier doubling;
- derivation of the checkpoint architecture from J;
- a decoder, probability, measurement, particle, force, or SI statement;
- any L2-L6 lift.

## Residual

Full minimal-pair classification remains a separate candidate:

```text
C-OMEGA-U-UNITY-5-BISECTOR-H1-1
```

The natural route is the nonabelian H1/complement classification for the 5-group congruence kernel of `GL_2(F_5[N]/N^4)` under the involution induced by the bisector. This package does not decide it.
