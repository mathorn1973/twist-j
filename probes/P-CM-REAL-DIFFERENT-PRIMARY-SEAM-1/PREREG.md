# P-CM-REAL-DIFFERENT-PRIMARY-SEAM-1 preregistration

Date: 2026-08-28

Author of record: A. M. Thorn

Status: preregistered protocol only. Formal execution count: zero. No
scientific result is earned by this file. The accepted `verify.py` may be read,
parsed, compiled, and inspected statically before the immutable public pin, but
it has not been imported or executed.

Public claim lock: issue #632, opened before this file is committed.

```text
branch:  probe/P-CM-REAL-DIFFERENT-PRIMARY-SEAM-1
path:    probes/P-CM-REAL-DIFFERENT-PRIMARY-SEAM-1/
owner:   A. M. Thorn
mode:    RESULT-EXPOSED, proof-first; verifier is an exact audit
```

## Authority

```text
STATE:          ACTIVE
CANON:          Public Canon v68
AUTHORITY:      mathorn1973/twist-j main
TAG:            canon-v68
TAG_TARGET:     b72505f55bcf2ef3d5985065ae52f3365966f32e
CONTENT_COMMIT: d755c5758406bfed13405dde0864c2ce81f5f581
CANON_SHA256:   63370401c2e25d94e7d8f94bdf142ba32fe3c2a5cdf81d1435114b669b0e5546
CANON_BYTES:    353145
BASE_COMMIT:    0a7f87495d7df37a6acbfe8ac906593e844472cf
ACTION_LAYER:   L1 exact arithmetic and integral-lattice comparison only
```

Before this lock, GitHub `main`, matching issues, pull requests and branches,
`STATUS.md`, `POLICY.md`, `AGENTS.md`, `canon/CORE.md`, `canon/FRONTIER.md`,
`canon/REGISTRY.tsv`, the Canon, and both consumed probes were read back. The
collision scan found no prior owner of this probe or claim name. Any changed
authority basis or collision is STOP.

This transaction changes exactly its own probe directory. It changes no
Canon, Registry, Frontier, dependency, evidence, gate, workflow, release,
decoder, Note, promotion package, or existing probe file.

## Consumed public candidates

The probe consumes, without promoting or duplicating evidential credit:

1. `CM-ALTERNATING-PENCIL`, a public `[T]` row, for the integral hyperbolic
   pencil and the pullback action.
2. `P-CM-ALTERNATING-PRIMARY-LATTICE-SEAM-1`, merged as `candidate-T / L1`,
   for the rational primary decomposition, integral lattices, index-five seam,
   seam functional, action by `-1`, resultant `25`, and exact primary
   projector.
3. `P-THORN-TRIANGLE-PENTAGON-RIGIDITY-1`, merged as `candidate-T / L1`,
   only for the already exposed chord identity used to name a generator of the
   same real different.

All three inputs keep their present status. The present theorem is a typed
comparison theorem: it identifies what the already computed projector lattice
and seam are in the arithmetic of the real quadratic primary factor.

## Frozen carriers

Let

```text
E_Z = Alt^2(Z^4),
E_Q = E_Z tensor Q,
P   = pullback by the public M_J,
q(x)=x^2-3x+1,
r(x)=Phi_10(x)=x^4-x^3+x^2-x+1.
```

Let

```text
H_Q = ker q(P),          H_Z = H_Q intersect E_Z,
C_Q = ker r(P),          C_Z = C_Q intersect E_Z.
```

The public bases are

```text
H_Z = Z Omega_1 + Z Omega_2
```

and the four frozen circular basis vectors `c_1,...,c_4` from the source seam
probe. The source projector is denoted `e_H`; it is the unique rational
idempotent commuting with `P`, equal to one on `H_Q` and zero on `C_Q`.

For `w=(w01,w02,w03,w12,w13,w23)` put

```text
A(w)=w01+w03+w23,
B(w)=w02+w12+w13,
ell(w)=2A(w)+B(w) mod 5.
```

## Real quadratic order and declared trivialization

Put

```text
F    = Q(sqrt(5)),
beta = phi^-1,
u    = phi^-2 = beta^2 = 1-beta,
O    = Z[beta] = Z[u].
```

The action `u -> P|H_Z` makes `H_Z` a rank-one `O`-module. The public basis
declares the comparison trivialization

```text
iota: H_Z -> O,
iota(a Omega_1+b Omega_2)=a+b beta.
```

This trivialization is load-bearing and is not intrinsic. The ideal statements
below are independent of a generator; scalar residue coordinates are not.

Let

```text
delta = sqrt(5)=1+2 beta=3-2u,
s     = s_J^2=2-beta=delta beta=1+u.
```

Write

```text
d_F      = (delta) = (s),
d_F^-1   = delta^-1 O.
```

Here `d_F` is the real different and `d_F^-1` the codifferent.

## Frozen result ceiling

The maximum result is

```text
CM-REAL-DIFFERENT-PRIMARY-SEAM
candidate-T ceiling; L1 only
```

with the following five parts.

### D1. Different and ramified chord

The order is maximal and monogenic in the hyperbolic eigenvalue:

```text
O=Z[u],
q'(u)=2u-3=-delta.
```

Consequently

```text
d_F=(q'(u))=(delta)=(s_J^2),
d_F^-1=delta^-1 O,
s_J^4=5u.
```

The already named chord `s_J^2` supplies one generator of `d_F`. The ideal
alone does not distinguish a generator, and using this external chord element
as a coordinate normalization still does not trivialize `H_Z`. Replacing the
chosen ideal generator by a unit changes the induced residue coordinate.

### D2. Exact integral image of the rational primary projector

The literal rational image remains

```text
e_H(E_Q)=H_Q.
```

The new integral-lattice statement is

```text
e_H(E_Z)=d_F^-1 H_Z
```

as `O`-lattices inside `H_Q`. Under the declared trivialization, for every
`w in E_Z`,

```text
iota(e_H(w))=(A(w) beta+B(w))/delta.
```

Since `(A,B)` ranges over all of `Z^2`, this image is exactly
`delta^-1 O`, not merely a sublattice of it.

### D3. Canonical primary seam exact sequence

Let `R=Z[x]`, acting on `E_Z` by `x -> P`. Projection induces the intrinsic
exact sequence of `R`-modules

```text
0 -> H_Z direct_sum C_Z
  -> E_Z
  -> d_F^-1 H_Z/H_Z
  -> 0,
```

where the last arrow is

```text
w -> e_H(w)+H_Z.
```

On the target, `x` acts as multiplication by `u`. Thus `q(x)` annihilates the
target and its action factors through

```text
R/(q) = O.
```

The displayed `R`-action on `E_Z` does not factor through `O`: `q(P)` is
nonzero on the circular primary sector. Only the seam quotient and the target
acquire the induced `O`-module structure. This type distinction is
load-bearing.

Thus the already computed seam has the canonical module interpretation

```text
Q_seam=E_Z/(H_Z direct_sum C_Z)
      ~= d_F^-1 H_Z/H_Z.
```

After the declared trivialization only,

```text
Q_seam ~= d_F^-1/O ~=_O-mod O/(s_J^2).
```

Neither `d_F^-1/O` nor `Q_seam` is asserted to be a ring. The first displayed
isomorphism is intrinsic. The residue ring `O/d_F` is canonically its prime
field `F_5`; what depends on the `H_Z` trivialization and ideal-generator
normalization is the comparison map from `Q_seam` to that residue field.

### D4. Residue functional, annihilator, and action

Multiplication by `delta` gives

```text
delta iota(e_H(w))=A(w) beta+B(w).
```

Modulo `d_F`, one has `beta=2`, so this is exactly

```text
ell(w)=2A(w)+B(w) mod 5.
```

Multiplication by the chord generator `s=delta beta` instead gives `2ell`.
The two coordinates differ by the unit `beta=2 mod d_F`; they define the same
one-dimensional residue module and are not to be conflated.

Moreover

```text
Ann_O(Q_seam)=d_F=(s_J^2),
u=-1 mod d_F.
```

Therefore `P` acts on the seam as multiplication by `-1`, matching the source
probe exactly.

### D5. Reduced seam versus resultant layer

The polynomial identity

```text
r(x)=(x+1)^2 q(x)+5x^2
```

gives

```text
Z[x]/(q,r) ~= O/(5)
            ~= F_5[epsilon]/(epsilon^2),
epsilon=u+1.
```

This is a nonreduced length-two object of order `25`; its order is the
resultant `Res(q,r)=25`. The primary seam is only its reduced residue line

```text
O/d_F ~= F_5
```

of order `5`. Resultant order and seam order must not be identified.

## Written proof

The trace pairing in the basis `(1,beta)` has Gram matrix

```text
[[Tr(1),    Tr(beta)],
 [Tr(beta), Tr(beta^2)]]
= [[2,-1],[-1,3]],
```

of determinant `5`. Since `beta` satisfies `beta^2+beta-1=0`, this proves that
`O=Z[beta]` is the full ring of integers and that its different is generated by
the derivative `2beta+1=delta`. Equivalently, because `u` satisfies `q`,
`q'(u)=2u-3=-delta`.

The identities `u=1-beta` and `delta=1+2beta` give

```text
delta beta=beta+2beta^2=2-beta=1+u=s,
```

so `(s)=(delta)`. Squaring gives

```text
s^2=(delta beta)^2=5 beta^2=5u.
```

The source projector has numerator

```text
[[ 2, 1, 2, 1, 1, 2],
 [-1, 2,-1, 2, 2,-1],
 [ 1,-2, 1,-2,-2, 1],
 [ 2, 1, 2, 1, 1, 2],
 [-1, 2,-1, 2, 2,-1],
 [ 2, 1, 2, 1, 1, 2]] / 5.
```

Hence, with `A=A(w)` and `B=B(w)`,

```text
e_H(w)=a Omega_1+b Omega_2,
a=(2A+B)/5,
b=(-A+2B)/5.
```

In `F`,

```text
(A beta+B)/delta
=((A beta+B)(1+2beta))/5
=(2A+B+(-A+2B)beta)/5,
```

which proves the formula in D2. The coordinate vectors `e01` and `e02` make
`A` and `B` range independently over `Z`, proving equality with the full
codifferent lattice.

The projector kills `C_Q`, restricts to the identity on `H_Q`, and commutes
with `P`. Therefore its reduction modulo `H_Z` is `R`-linear and kills exactly
`H_Z direct_sum C_Z` inside `E_Z`. Its image is
`d_F^-1 H_Z/H_Z`, proving the exact `R`-module sequence in D3. On this target
`P` acts by multiplication by `u`, so `q(P)` vanishes and the action factors
through `R/(q)=O`. This quotient has order `5`, in agreement with the
independently computed determinant of the six primary lattice columns.

Modulo `d_F=(delta)`, the equation `1+2beta=0` gives `beta=2` in `F_5`.
Reducing the displayed projector formula therefore gives `2A+B=ell`. Since
`s=1+u` vanishes modulo the different, `u=-1`, and the action statement follows.
The annihilator is exactly `d_F`, rather than merely an ideal containing it,
because the quotient is a nonzero one-dimensional `O/d_F`-module.

Finally, direct multiplication proves the polynomial identity in D5. In
`O/(5)`, the nonzero class `epsilon=u+1` satisfies `epsilon^2=0`; hence this
order-25 quotient is nonreduced. Passing to `O/(epsilon)=O/d_F` produces the
reduced order-five seam.

## Canonicity ledger

Canonical at the frozen L1 carrier:

- the primary subspaces and saturated lattices `H_Z,C_Z`;
- the rational projector `e_H`;
- the ideals `d_F,d_F^-1`;
- the equality `e_H(E_Z)=d_F^-1 H_Z` as `O`-lattices;
- the exact `R=Z[x]`-module sequence and induced `O`-module on its quotient;
- its annihilator and `P`-action.

Declared or noncanonical:

- the basis `(Omega_1,Omega_2)` and trivialization `iota`;
- use of `delta`, the externally named `s_J^2`, or `q'(u)` to normalize the
  comparison from the codifferent quotient to the residue ring;
- a scalar coordinate `Q_seam -> O/d_F=F_5`;
- the normalization `ell` rather than any nonzero scalar multiple.

Changing a generator or trivialization multiplies the residue coordinate by
an element of `F_5^x`. `P`-equivariance does not remove these four possible
normalizations because `P` already acts scalarly as `-1`.

## Scope boundary

This theorem is not a discriminant-form isometry claim and does not construct
an integral retraction. It does not choose `Omega_1`, an action unit, a period,
a cycle, a current, a polarization, a time direction, a chirality, a physical
area, `h`, `hbar`, a phase law, a decoder, an SI normalization, or any L2-L6
object. No action, period, physical, metrological, or higher-layer meaning is
claimed.

## Falsifiers

One exact counterexample fires the corresponding part:

1. `O` is not `Z[u]`, or its different is not `(q'(u))=(sqrt(5))`;
2. `(s_J^2)` is not the different or `s_J^4 != 5u`;
3. the integral projector image is not exactly `d_F^-1 H_Z`;
4. the intrinsic `R=Z[x]`-module sequence is not exact, or the target action
   does not factor through `O`;
5. the seam annihilator is not the different or `P` does not act by `-1`;
6. the frozen `ell` is not the reduction obtained with generator `delta`;
7. using `s_J^2` gives `ell` rather than the frozen unit multiple `2ell`;
8. the resultant layer is not order `25` and nonreduced, or the seam is not
   its reduced order-five quotient;
9. the theorem produces a canonical scalar residue coordinate or any physical
   interpretation forbidden by the scope boundary.

A stale authority basis, changed pin, nonzero verifier exit, nonempty stderr,
stdout mismatch, architecture disagreement, or scope widening is integrity
STOP, not a scientific falsifier.

## Frozen controls

```text
B1  e_H(e01)=(2/5)Omega_1-(1/5)Omega_2.
B2  e_H(e02)=(1/5)Omega_1+(2/5)Omega_2.
B3  beta/delta=(2-beta)/5 and 1/delta=(1+2beta)/5.
B4  multiplication by delta yields ell; multiplication by s_J^2 yields 2ell.
B5  epsilon=u+1 is nonzero and square-zero modulo 5.
B6  unit rescaling preserves the abstract seam but changes its F_5 coordinate.
```

## Verifier contract

The accepted `verify.py` is standard-library only. It uses integers,
`Fraction`, exact matrices, exact polynomial arithmetic, and the exact order
`Q(beta)` with `beta^2=1-beta`. It performs no floating-point operation,
tolerance test, numerical root finding, random search, network access,
subprocess, clock read, or external source import.

The written proof carries the theorem. The verifier audits:

```text
G01 source_scope_firewall
G02 public_pullback_and_primary_projector
G03 real_quadratic_order_and_unit_action
G04 different_and_codifferent
G05 ramified_chord_generates_different
G06 projector_image_equals_codifferent_lattice
G07 canonical_seam_exact_sequence
G08 seam_residue_functional
G09 annihilator_and_minus_one_action
G10 resultant_nilpotent_layer_guard
G11 scope_and_trivialization_guard
```

Success requires all gates to print `PASS`, followed exactly by

```text
DECISION CM-REAL-DIFFERENT-PRIMARY-SEAM-CONFIRMED
```

with exit zero and empty stderr. Any other outcome is STOP pending diagnosis;
no carrier, ideal, normalization, or scope may move after the pin.

## Formal run protocol

1. Commit this file and `verify.py` together as the first branch commit from
   the frozen base.
2. Push and read both files byte-identically from GitHub.
3. Record the immutable commit and hashes.
4. Run the accepted verifier once in the local formal lane.
5. Commit `EXPECTED.txt`, `RUN.md`, and `RESULT.md` without changing the pin.
6. Open one pull request changing exactly this probe directory.
7. Require byte-identical GitHub-hosted Python 3.12 x86_64 and native aarch64
   output plus aggregate `check` success.

No Canon fold, promotion package, action bridge, or physical interpretation is
part of this probe transaction.
