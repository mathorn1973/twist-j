# P-CM-REAL-DIFFERENT-PRIMARY-SEAM-1 result

Status: **candidate-T / L1 / CM-REAL-DIFFERENT-PRIMARY-SEAM CONFIRMED / PUBLIC CANON STATUS UNCHANGED.**

The first formal execution of the immutable public verifier exited zero,
wrote empty stderr, and produced the exact committed `EXPECTED.txt` bytes.
All eleven frozen gates passed. No scientific falsifier fired and no carrier,
ideal, normalization, type, or interpretation moved after the pin.

## Result

Let `P(W)=M_J^T W M_J` act on

```text
E_Z=Alt^2(Z^4),
H_Z=ker(P^2-3P+I) intersect E_Z,
C_Z=ker(Phi_10(P)) intersect E_Z.
```

Put

```text
F=Q(sqrt(5)),
O=Z[beta]=Z[u],
beta=phi^-1,
u=phi^-2=beta^2=1-beta,
delta=sqrt(5)=1+2beta.
```

The public pullback action makes `H_Z` a rank-one `O`-module with `u` acting
as `P`. In the declared comparison trivialization

```text
iota(a Omega_1+b Omega_2)=a+b beta.
```

That trivialization is explicitly noncanonical.

## The different and the ramified chord

For `q(x)=x^2-3x+1`, exactly

```text
q'(u)=2u-3=-delta.
```

The trace Gram matrix in the basis `(1,beta)` is

```text
[[2,-1],[-1,3]],
```

with determinant five. Hence the real different and codifferent are

```text
d_F=(delta),
d_F^-1=delta^-1 O.
```

The inherited chord identity gives

```text
s_J^2=2-beta=delta beta=1+u.
```

Because `beta` is a unit,

```text
(s_J^2)=d_F,
s_J^4=5u.
```

Thus the named ramified chord supplies a generator of the real different. It
does not by itself trivialize the hyperbolic lattice or select a scalar seam
coordinate.

## Projector image and codifferent lattice

For

```text
A(w)=w01+w03+w23,
B(w)=w02+w12+w13,
```

the exact rational primary projector satisfies

```text
e_H(w)
=((2A+B)/5) Omega_1
 +((-A+2B)/5) Omega_2,

iota(e_H(w))=(A beta+B)/delta.
```

The two integer functions `A,B` range independently over `Z`. Therefore the
result is equality of full lattices, not merely equality of indices:

```text
e_H(E_Z)=d_F^-1 H_Z.
```

The literal rational image remains `e_H(E_Q)=H_Q`; the codifferent statement
concerns the image of the integral lattice.

## Canonical seam sequence and its type

Let `R=Z[x]`, with `x` acting as `P` on `E_Z,H_Z,C_Z` and as multiplication
by `u` on the target. Projection gives the exact `R`-module sequence

```text
0 -> H_Z direct_sum C_Z
  -> E_Z
  -> d_F^-1 H_Z/H_Z
  -> 0.
```

The displayed `R`-action on `E_Z` does not factor through `O`, because
`q(P)` is nonzero on the circular primary sector. On the seam target,
`q(x)` vanishes, so its action does factor through `R/(q)=O`. Consequently

```text
E_Z/(H_Z direct_sum C_Z)
 ~= d_F^-1 H_Z/H_Z
```

is the intrinsic module interpretation of the already computed primary seam.
After the declared trivialization and a generator normalization only,

```text
Q_seam ~= d_F^-1/O ~=_O-mod O/(s_J^2).
```

The seam and `d_F^-1/O` are modules, not naturally rings. The residue ring
`O/d_F` is canonically `F_5`; the comparison from the seam to that scalar
field depends on the chosen trivialization and ideal-generator normalization.

## Residue map, annihilator, and action

Multiplication by `delta` gives

```text
delta iota(e_H(w))=A(w)beta+B(w).
```

Modulo `d_F`, `beta=2`, hence the old seam functional is exactly

```text
ell(w)=2A(w)+B(w) mod 5.
```

Using the chord generator `s_J^2=delta beta` instead yields `2ell`. This is
the frozen unit-rescaling control: it preserves the quotient and its kernel
but changes the scalar coordinate.

Exactly

```text
Ann_O(Q_seam)=d_F=(s_J^2),
u=-1 mod d_F.
```

Therefore `P` acts on the seam as `-1`, agreeing with the source seam probe.

## Reduced seam versus resultant layer

The exact identity

```text
Phi_10(x)=(x+1)^2 q(x)+5x^2
```

gives

```text
Z[x]/(q,Phi_10) ~= O/(5)
                 ~= F_5[epsilon]/(epsilon^2),
epsilon=u+1.
```

This nonreduced layer has order `25`, matching
`Res(q,Phi_10)=25`. The integral primary seam is only its reduced residue line

```text
O/d_F ~= F_5
```

of order `5`. The resultant and seam orders are not the same invariant.

## Canonicity and physical boundary

Canonical at L1 are the primary lattices, projector, real different and
codifferent ideals, the projector-image equality, the exact `R`-module
sequence, the abstract residue module, its annihilator, and its `P`-action.
Noncanonical are the trivialization by `Omega_1`, the normalization of the
comparison map by a chosen different generator, and the resulting scalar seam
coordinate. `P`-equivariance cannot remove this freedom because `P` already
acts as the scalar `-1` on the seam.

The result does not choose `Omega_1`, an action unit, a period, a cycle, a
current, a polarization, a physical area, a time direction, a chirality,
`h`, `hbar`, a phase law, a decoder, an SI normalization, or any L2-L6
object. It creates no discriminant-form isometry and no physical bridge.

## Status ceiling

The written proof in `PREREG.md` carries the universal result. The exact
verifier audits the finite identities and all type and scope controls. Subject
to the required pull-request integrity and two-architecture checks, this
supports a later public row

```text
CM-REAL-DIFFERENT-PRIMARY-SEAM [T], L1.
```

That row is not added by this probe. A Canon fold is a separate transaction.
Until such a fold, Public Canon v68 is unchanged.

## Pin and local run

```text
public claim issue:       #632
preregistration pin:      cb754bd9e4d13b0a83ec99291441dff5e0ffa5c9
verifier sha256:          6ef7c8a208d21eab98c53fe6ffb7dd3017a87d91772b205baca10bbe612b1dd6
local architecture:       x86_64
local exit:               0
local stderr bytes:       0
local stdout bytes:       541
local stdout sha256:      b0621cef633d28d91793e24b1cb1d8214aabcf0d17ce49a0a91c955f82eb988d
```

The local run is one architecture lane only. The pull-request workflow
remains the required independent x86_64/aarch64 reproduction and aggregate
repository-integrity audit.
