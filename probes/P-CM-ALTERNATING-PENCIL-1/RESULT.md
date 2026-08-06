# P-CM-ALTERNATING-PENCIL-1 preliminary result

Route: positive local formal leg. The pinned verifier exited zero, wrote empty
standard error, and ended with `RESULT 34/34 ALL PASS`. The independent
adversarial program ended with `RESULT 5/5 ALL PASS`. The pull-request
architecture gate is pending, so the grades below are provisional and are not
yet earned grades of record.

Scope: the alternating trace-form pencil on `O_K` and its unit action, at L1
state only. This result changes no Canon, registry, frontier, or status file.

## Evidence state

```text
pin_commit: 71717975810c805b886eebc9d045c868adab92af
prereg_sha256: 69c4204d110ebff232e42c96a739f48ddb9548b49b2fa315cc69f7451488956f
verifier_sha256: 19cdff86cc90de099a96088b39818956022fbd36d0ce48a0e2c2a3f9747e4b78
stdout_sha256: 5f790488d58802bdf467c7269e967e82a08e7b8f0f1b51a8736789c04384cdfd
stdout_bytes: 1940
stdout_lines: 35
exit_code: 0
stderr_bytes: 0
local_result: 34/34 ALL PASS
breaker_sha256: 0870c628346dcd7499cf453fcbff3c8ed25e370ea316fbd20d9cde0355c82786
breaker_stdout_sha256: 6dc623f6088e0b4a8a68343f12ecaa6c027f6288015d1ba6270803b3602d37e8
adversarial_result: 5/5 ALL PASS
architecture_gate: pending
```

No registered falsifier fired in the declared finite ranges or in the wider
adversarial searches recorded in `BREAK.md`.

## P1, provisional T

For coordinates `(a,b,c,d)` in the fixed basis, conjugation is

```text
(a-b,-b,d-b,c-b).
```

Equality with `(-a,-b,-c,-d)` is equivalent to `b=2a` and `c+d=2a`.
Writing `r=c-a` gives every solution, and only a solution, as

```text
(a,2a,a+r,a-r) = a lambda_1 + r lambda_2.
```

Direct reduction in `Z[j]` gives
`lambda_1 phi=lambda_1+lambda_2`. Since `phi^-1=phi-1`, this is
`lambda_2=lambda_1 phi^-1`. Also `Z[phi]=Z+Z phi^-1`, so
`L=lambda_1 Z[phi]`, free of rank one, with the stated integer basis.

## P2, provisional T

For `lam` in `L`, P1 gives `conj(lam)=-lam`. Trace is invariant under
conjugation. For `w=lam y conj(x)`, commutativity gives

```text
conj(w) = -lam x conj(y).
```

Therefore `Tr(lam y conj(x))=-Tr(lam x conj(y))`. Division by five proves
antisymmetry. Setting `y=x` makes the rational value equal to its negative,
so it is zero and the form is alternating.

## P3, provisional T

The trace-dual criterion says that the form is integer-valued exactly when
`lam/5` lies in the inverse different. For this cyclotomic field,

```text
D_K = (5/(1-j)),        D_K^-1 = ((1-j)/5).
```

The identities

```text
N(lambda_1)=5=N(1-j),
lambda_1=j(1-j)(1+j+j^2)
```

show `(lambda_1)=(1-j)`. P1 then places every `lam` in `L` in that ideal,
which proves integer-valuedness for the entire lattice. The trace pairing is
perfect exactly when `lam/5` generates the inverse different, equivalently
when `(lam)=(lambda_1)`.

For `lam=lambda_1 eta`, multiplication of the first trace argument by `eta`
changes the Gram determinant by

```text
N_{K/Q}(eta)=N_{K+/Q}(eta)^2.
```

It is one exactly for a unit, zero for `eta=0`, and greater than one for a
nonzero nonunit. The direct Gram calculation has Pfaffian one for `Omega_1`,
so its determinant is one.

## P4, provisional T

Direct trace reduction gives

```text
Omega_1 = [[ 0, 1, 0, 0],
           [-1, 0, 1, 0],
           [ 0,-1, 0, 1],
           [ 0, 0,-1, 0]]

Omega_2 = [[ 0, 0, 1,-1],
           [ 0, 0, 0, 1],
           [-1, 0, 0, 0],
           [ 1,-1, 0, 0]].
```

The entries of `a Omega_1+b Omega_2` are linear in `(a,b)`, hence its
Pfaffian is a binary quadratic form. Its values at `(1,0)`, `(0,1)`, and
`(1,1)` are `1`, `-1`, and `-1`. These three values determine its three
coefficients and give, for all integers `a,b`,

```text
Pf(Omega_{a,b}) = a^2-a b-b^2.
```

Multiplication under the two real embeddings gives

```text
N_{K+/Q}((a-b)+b phi)
 = ((a-b)+b phi)((a-b)+b(1-phi))
 = a^2-a b-b^2.
```

Thus the finite three-value calculation is the complete polynomial proof.

## P5, provisional T

P1 rewrites the parameter as

```text
a lambda_1+b lambda_2=lambda_1((a-b)+b phi).
```

P3 and P4 therefore identify unimodularity with norm `+1` or `-1` in
`Z[phi]`.

To identify all units, take a unit, choose its sign, and multiply by an
integer power of `phi` so that its positive real value `delta` satisfies
`1<=delta<phi`. If its norm is one, its integer trace
`delta+delta^-1` lies in `[2,3)`, hence equals two and forces `delta=1`.
If its norm is minus one, its integer trace `delta-delta^-1` lies in
`[0,1)`, hence equals zero and again forces `delta=1`, contradicting that
norm. Thus every unit is `+phi^n` or `-phi^n` for an integer `n`.

The parameter orbit is consequently exactly the Pell layer. Induction from
`phi^2=phi+1` gives `phi^n=F_n phi+F_{n-1}` for `n>=1`. The pair
`(F_{n+1},F_n)` has this coefficient, so its Pfaffian is
`N(phi)^n=(-1)^n`.

## P6, provisional T

For a unit `u`, commutativity and conjugation give

```text
Omega_lam(u x,u y)=Omega_{lam u conj(u)}(x,y).
```

The factor `u conj(u)` is the relative norm and is a unit of `Z[phi]`, so P1
shows that the pencil is preserved. The kernel is the relative norm one
subgroup. The unit ranks of `K` and `K+` are both one, while the relative
norm sends every real-subfield unit `v` to `v^2`. Its image has rank one,
so its kernel has rank zero and is finite. Finite-order field units are roots
of unity, and the roots in `Q(j)` are exactly

```text
{+j^k,-j^k : 0<=k<5}.
```

All ten have relative norm one, proving equality with the kernel.

## P7, provisional T

The relative norm of `J` is

```text
J conj(J)=2-phi=(phi-1)^2=phi^-2.
```

Using `lambda_2=lambda_1 phi^-1` gives the coordinate columns

```text
lambda_1 phi^-2=lambda_1-lambda_2,
lambda_2 phi^-2=-lambda_1+2 lambda_2.
```

Thus `A_J=[[1,-1],[-1,2]]`. It has determinant one, trace three, and
characteristic polynomial `t^2-3t+1`. The two real embeddings give its
eigenvalues `phi^2` and `phi^-2`.

Parameter multiplication by `phi` has columns from
`lambda_1 phi=lambda_1+lambda_2` and `lambda_2 phi=lambda_1`, hence matrix
`[[1,1],[1,0]]` and determinant minus one. Its square is multiplication by
`phi^2`, and direct matrix multiplication gives `A_J` as that square's
inverse. The pullback by the unit `phi` uses `phi^2`, as P6 requires.

## P8, provisional T

For every alternating four by four matrix `W`, the Pfaffian identity is

```text
Pf(M^T W M)=det(M) Pf(W).
```

If `det(M)=1` and `M^T Omega M=mu Omega` for a fixed nonzero pencil member,
then P4 gives a nonzero Pfaffian, so cancellation yields `mu^2=1`. Thus `mu`
is `+1` or `-1`.

The parameter map `lam -> Omega_lam` is injective. Indeed, if the form is
zero, setting its second argument to one gives `Tr(lam x)=0` for every `x`
in `O_K`; nondegeneracy of the trace pairing forces `lam=0`. P6 now shows
that a scalar multiplier for a unit multiplication map must equal
`u conj(u)`. Such a relative norm is positive in both real embeddings, so it
cannot be `-1`. Multiplier `+1` occurs exactly in the kernel from P6, namely
the ten roots of unity.

For `J`, P7 gives parameter `lambda_1-lambda_2`, not a scalar multiple of
`lambda_1`, which is the direct entry obstruction. Finally trace invariance
and `conj(lam)=-lam` give

```text
Omega_lam(conj(x),conj(y))=-Omega_lam(x,y),
```

or `C^T Omega C=-Omega`. Conjugation is a distinct map from unit
multiplication.

## Pending gates

Each written proof above closes the corresponding universal statement, and
the local verifier audits its frozen finite consequences. The independent
adversarial program found no counterexample. Final grade `T` is available for
each item only if the required GitHub transcript is byte-identical to
`EXPECTED.txt`. Any fired falsifier remains part of the final record without
moving a threshold.
