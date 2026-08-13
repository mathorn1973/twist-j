# Independent post-pin `n=4` audit

## Outcome

The complete `4 legs x 4 irreducible cores` census was recomputed from a
new MATLAB-literal parser and a new named-index contractor.  Every primary
matrix agreed with an independently contracted graph star

\[
C(A,\bar A)=C(\bar A,A)^T.
\]

The first hard witness in the frozen scan order is the closure witness at
`q=0`, `R1`: if `M=C_{q=0,R1}`, then `I,M,M^2` have a nonzero three-dimensional
minor.  Its exact value in `Q(zeta_40)` reduces to `31 mod 41`.  This is an
`EXACT NO` for the preregistered arbitrary-local-unitary `1+5` A5 action and
only for that scoped hypothesis.

## Pins and conventions

- Public pin commit: `1a813b6f50435d83e0dfd5011898a03fc5e4b089` (object present).
- Pinned `PREREG.md` SHA-256:
  `b03ed300806c993cb4f4eac7249d9a6c2e7e9df9d96669d989445d4a1ade68f3`.
  The blob at the public commit and the audited working copy have this same
  digest.
- Sole tensor input SHA-256:
  `55fbc0ba2747b4e5adc5a5abd15ac7241a461ff8182268ebdae464d8a29cc9ae`.
- Tensorization: `A[i,j,k,l]=U[6*i+j,6*k+l]`.
- Open indices: axis `q` of `A0` is `ROW`, axis `q` of `B0` is `COL`; the
  final output is explicitly reordered to `(ROW,COL)`.
- Star is evaluated by swapping `A` and `bar(A)` and then transposing the two
  open indices.  It is not an ordinary transpose at the original residue.
- Field locator: `F_41`, `z=6`, `bar(z)=6^-1=7`.

The canonical witness diagram JSON has SHA-256
`2879d6a4f90221e3cbb611182dc304e3d45235b0c4467d9faeb3fd0ad1e449f3`.
It encodes `q=0`, open matching `0123`, remaining colors `(1,2,3)`, and
`R1=(1032,2310,3201)`.

## Graph-star orientation

For every core, direct permutation arithmetic found an `h in S3` fixing 0
such that, component by component,

\[
h\,p^{-1}\,h^{-1}=p.
\]

The conjugators for `(R0,R1,R2,R3)` are respectively
`0123`, `0132`, `0321`, `0321`.  This establishes graph-star equality by
dummy-copy relabeling.  The numerical audit then recomputed both sides of the
star equation for all sixteen diagrams and asserted literal equality.

## Complete modular census

The hash of a matrix is SHA-256 of its six comma-separated decimal rows,
each newline-terminated.  `star=OK` means the separately contracted star has
both the same entries and the same digest.

| leg | core | scalar | matrix SHA-256 | star |
|---:|---:|:---:|---|:---:|
| 0 | R0 | yes | `8f045c64812c3c18a884fde5d3b902a02ac80a55f568d11be3ea806cd9f0d15c` | OK |
| 0 | R1 | no | `216ab9aed14ee7c08dc13cd688d3b95b216ddad7644525c635a0dc28bdb37559` | OK |
| 0 | R2 | yes | `2f84828b4a39fe60fba047574cf50216285b718edd7a06227bc3702741c9522d` | OK |
| 0 | R3 | yes | `7bcb77109d6d0d52a281ea4fac6150ccf8f786ef239c460f08933393e09e6114` | OK |
| 1 | R0 | yes | `8f045c64812c3c18a884fde5d3b902a02ac80a55f568d11be3ea806cd9f0d15c` | OK |
| 1 | R1 | no | `e5bef014afba92e1ddddcfc3a93f54ec24f5985d0160bf91790def0361dc82fd` | OK |
| 1 | R2 | yes | `7bcb77109d6d0d52a281ea4fac6150ccf8f786ef239c460f08933393e09e6114` | OK |
| 1 | R3 | yes | `2f84828b4a39fe60fba047574cf50216285b718edd7a06227bc3702741c9522d` | OK |
| 2 | R0 | no | `b5be7566151c07630d1d9548b448f0ecec59159b03d5b8d0d2d092b6cfa83026` | OK |
| 2 | R1 | no | `df4617b8d0e8c9366ba19cddd451f5a6449dba2ad9f33d28c168424f57666806` | OK |
| 2 | R2 | no | `37fcf5414552e4fa9c1d8b960c2d8a4a1c2b35493792c487f7e661ef6208f174` | OK |
| 2 | R3 | no | `556e93f9122258b0c542f743651c0c7c3a8b98a0cbed1c9a6f97b8fb3d3f1e19` | OK |
| 3 | R0 | no | `37b8095c2f6ffeb28691887fc050faddf223b3de8c32c6f7a93b6f2b4f5f5877` | OK |
| 3 | R1 | no | `73744167ced543956c0329a69f3674923d2a7f6e12b971df72fac54a17838194` | OK |
| 3 | R2 | no | `99a628ea1af58fac6c144cc991db9501bb7e4f2251599719c35bb3d9d2b8da9d` | OK |
| 3 | R3 | no | `7554a5fae8cf58dca4992fcf9ddb33a589598e1d1db86cb4d988e1e77d97e926` | OK |

All sixteen primary matrices and all sixteen independently contracted star
matrices are present entry-for-entry in `mod41_scan.json`.

The first two legs have no nonzero commutator.  On `q=2`, the first
commutator is `[R0,R1]`, first row-major nonzero entry `(0,0)=33`; on `q=3`,
it is `[R0,R3]`, first entry `(0,0)=28`.  These occur after the globally first
hard witness and therefore are not the lifted certificate.

## Frozen-priority first witness

At `q=0`, `R0=19 I`.  The next matrix is

\[
M=\operatorname{diag}(4,19,19,1,1,4)\pmod {41}.
\]

There is no commutator yet, and the direct span of `I,R0,R1` has dimension
two.  Multiplicative closure adds `M^2`.  Rows `(I,M,M^2)` and flattened
columns `0,7,21`, i.e. entries `(0,0),(1,1),(3,3)`, give determinant

\[
31\pmod {41}.
\]

Thus `q=0/R1`, closure word `M^2`, is the first hard locator under the exact
preregistered priority.

## Exact `Q(zeta_40)` lift

Write `zeta=zeta_40` and use the power basis `1,zeta,...,zeta^15` with

\[
\Phi_{40}(zeta)=zeta^{16}-zeta^{12}+zeta^8-zeta^4+1=0.
\]

The exact matrix is diagonal.  Its entries, with equalities indicated, are

\[
\begin{aligned}
m_0=m_5&=(220+4zeta^2-6zeta^6+7zeta^8+2zeta^{10}-7zeta^{12}+2zeta^{14})/8,\\
m_1=m_2&=(220+6zeta^2-7zeta^6+6zeta^8+3zeta^{10}-6zeta^{12}+zeta^{14})/8,\\
m_3=m_4&=(220+4zeta^2-7zeta^6+6zeta^8+2zeta^{10}-6zeta^{12}+3zeta^{14})/8.
\end{aligned}
\]

A separate contraction of the binary support tensor gives
`diag(25204,22580,15768,35140,15052,20336)` and zero off-diagonal.  Because
these are nonnegative monomial counts, this proves the exact off-diagonal
zeros without relying on modular cancellation.

The lifted minor is

\[
\Delta=
\frac{2+6zeta^2-3zeta^6-zeta^8+3zeta^{10}+zeta^{12}-3zeta^{14}}{512}.
\]

Its reduction at `zeta -> 6 mod 41` is `31`.  Since `41` divides neither 8
nor 512, this reduction homomorphism is defined and proves `Delta != 0`
exactly.

### Reconstruction and independent ordering

The input amplitudes were independently expressed over denominator 10 and
checked directly against
`c=(zeta^5+zeta^-5)/2`,
`a(zeta^2+zeta^-2)=c`, and
`b=(zeta^4+zeta^-4)a`; conjugation `zeta->zeta^-1` fixes all three.

Each exact output coefficient numerator over denominator `10^8` has the
rigorous bound

```text
87850000000000000000
```

obtained from the exact maximum support count `35140`, source-entry numerator
L1 bound `25`, and quotient multiplication L1 constant `4`.  Interpolation at
all 16 primitive roots used the split primes
`1000081,1000121,1000721,1000921`; their product is
`1001845005676236032265841 > 2*bound`, so symmetric CRT recovery is unique.

At all 64 reconstruction evaluations a second contractor used the different
tree beginning
`(A0,B1),(A1,B0),(A2,B2),(A3,B3)` and agreed exactly.  It also agreed at all
16 primitive roots in the unused split verification field `F_1001041`.
Thus the ordering audit is not inferred from the frozen tree.

## Soundness and scope

Under the scoped hypothesis, every one-leg invariant covariant belongs to the
commutant of `1 direct-sum 5`.  That commutant has dimension two.  The exact
nonzero minor proves that the single covariant `M` generates the independent
elements `I,M,M^2`, a three-dimensional subalgebra.  This contradiction is
basis-free and survives arbitrary local unitaries.

The result does not assert a preferred six-line frame, a monomial action, a
decoder, hardware behavior, or any broader claim about other representations
or symmetry groups.

## Reproducibility

Commands:

```bash
python independent_mod41.py /path/to/AME46_ORIGINAL.m --scan \
  --output INDEPENDENT_MOD41.json
python independent_exact.py /path/to/AME46_ORIGINAL.m \
  --output INDEPENDENT_EXACT.json
```

Running both commands twice produced byte-identical JSON artifacts.  The two
run hashes were respectively
`7cdb3e54a3e42c9c8547acfb884ee78025f5f1d4eb976c5a4bd3d6ecedef9925`
and
`436d9fdcb3a80f991d92e0d3f84897a01f0cd624c1a54b26986dd262843bb77a`.
