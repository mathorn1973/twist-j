# P-CM-ALTERNATING-PRIMARY-LATTICE-SEAM-1 result

Status: **candidate-T / L1 / CM-ALTERNATING-PRIMARY-LATTICE-SEAM CONFIRMED / PUBLIC CANON STATUS UNCHANGED.**

The first formal execution of the immutable public verifier exited zero,
wrote empty stderr, and produced the exact committed `EXPECTED.txt` bytes.
All twelve frozen gates passed. No scientific falsifier fired and no equation,
basis, threshold, or interpretation moved after the pin.

## Result

Let `P(W)=M_J^T W M_J` act on
`E_Z=Alt^2(Z^4)=Z^6` in upper-triangular coordinate order
`(w01,w02,w03,w12,w13,w23)`. Put

```text
q(x)=x^2-3x+1,
r(x)=Phi_10(x)=x^4-x^3+x^2-x+1.
```

The exact characteristic polynomial is

```text
chi_P(x)=q(x)r(x)
        =x^6-4x^5+5x^4-5x^3+5x^2-4x+1.
```

The two irreducible factors occur once, so

```text
E_Q = H_Q direct-sum C_Q,
H_Q = ker q(P),
C_Q = ker r(P).
```

The circular restriction has exact order ten.

## CM characterization and the full integral intersections

For the public CM forms

```text
Omega_1=(1,0, 0,1,0,1),
Omega_2=(0,1,-1,0,1,0),
```

one has exactly

```text
H_Q = Q Omega_1 direct-sum Q Omega_2,
H_Z = H_Q intersect E_Z
    = Z Omega_1 direct-sum Z Omega_2.
```

Thus the CM pencil is the unique rational `q`-primary component and its
displayed integral lattice is the full saturated intersection. This is a
characterization of the already-public pencil, not independent evidence for a
physical scale or polarization.

The complementary full integral intersection is saturated with basis

```text
c1=(-1, 0,1,0,0,0),
c2=( 0,-1,0,1,0,0),
c3=( 0,-1,0,0,1,0),
c4=(-1, 0,0,0,0,1).
```

## The new index-five primary seam

The rational primary decomposition is not the direct sum of its two
canonical integral primary lattices:

```text
H_Z intersect C_Z = 0,
[E_Z : H_Z direct-sum C_Z] = 5,
E_Z/(H_Z direct-sum C_Z) = Z/5.
```

If

```text
A(w)=w01+w03+w23,
B(w)=w02+w12+w13,
ell(w)=2A(w)+B(w) mod 5,
```

then

```text
ker ell = H_Z direct-sum C_Z,
ell(Pw) = -ell(w) mod 5.
```

Hence `P` acts as `-1` on the five-element seam.

This does not contradict saturation of `H_Z` or `C_Z`: noncanonical integral
complements exist. The obstruction belongs specifically to the canonical
`P`-primary pair.

## Projector and ramified collision

The exact identity

```text
(8-3x)r(x)+(3x^3-2x^2+2x-3)q(x)=5
```

gives the unique `P`-equivariant rational primary projector

```text
E_H=((8-3P)r(P))/5
   =(-3P^5+11P^4-11P^3+11P^2-11P+8I)/5.
```

Its smallest common denominator is exactly five. The exact Sylvester
resultant and mod-five collision are

```text
Res(q,r)=25,
q mod 5=(x+1)^2,
r mod 5=(x+1)^4.
```

The lattice index was proved independently by the six-column determinant and
the surjective seam functional; it was not inferred from the resultant.

## Null eigenform guard

The public Pfaffian covariance and `det M_J=1` give

```text
Pf(PW)=Pf(W).
```

The two real eigenforms are

```text
omega_s=Omega_1+phi^-1 Omega_2,  P omega_s=phi^-2 omega_s,
omega_u=Omega_1-phi Omega_2,     P omega_u=phi^2 omega_u.
```

Exactly

```text
Pf(omega_s)=Pf(omega_u)=0.
```

Both are nonzero alternating 2-forms of rank two. They are not symplectic,
unimodular, rational, or integral. More generally, every eigenform for either
`phi^2` or `phi^-2` is Pfaffian-null. Therefore the scalar eigenvalues do not
contract or expand a primitive unimodular symplectic form.

The statement is deliberately narrower than “J changes no area.” Individual
two-periods do change; the frozen witness is

```text
Omega_1(e0,e1+e2)=1,
(P Omega_1)(e0,e1+e2)=0.
```

What is invariant is the four-dimensional Pfaffian, not every
two-dimensional period or Euclidean area.

## Novelty and inherited facts

The public Canon already owns the CM forms, their Pfaffian/Pell geometry,
`A_J`, the eigenvalues `phi^(+/-2)`, Pfaffian covariance, and the rejection of
scalar `phi^-2` scaling for a fixed symplectic form. A previous two-architecture
theorem gate already audited the exterior-square characteristic factorization.

The nonduplicative gain here is the explicit rational-primary
characterization together with the two full saturated integral intersections,
their index-five cyclic glue, the `-1` quotient action, the exact denominator
of the equivariant projector, and the null-eigenform protective corollary.

## Physical branch decision

Hurwitz is excluded rather than retained as a parallel justification.

The exact factor `phi^2` remains the already-owned unstable archimedean
two-area ratio

```text
phi^2=e^(h_top),  h_top=2 log phi,
```

under `J-TORAL-ENTROPY [T]`. It is not a Pfaffian scaling and is not promoted
to physical action.

If an action bridge is opened later, the selected research branch starts from
the primitive integral symplectic form `Omega_1` and a separately justified
unit period. Neither is identified with physical `h` by this result. The
`phi^2` archimedean area-ratio route is excluded as an action carrier in that
branch.

The action claim remains `STOP` until a geometric carrier, cycle or current,
polarization, normalization, phase law, real-place treatment, time
orientation, and typed layer bridge are frozen independently. The exterior
square supplies neither `2 pi` nor a phase law.

## Status ceiling

The written proof in `PREREG.md` carries the universal result. The exact
verifier audits all finite identities and scope controls. Subject to the
required pull-request integrity and two-architecture checks, this supports a
later public row

```text
CM-ALTERNATING-PRIMARY-LATTICE-SEAM [T], L1.
```

That row is not added by this probe. A Canon fold is a separate transaction.
Until such a fold, Public Canon v68 is unchanged.

## Pin and local run

```text
public claim issue:       #625
preregistration pin:      1779535e221ef9efc9fcb6a577a21050dad9aa03
verifier sha256:          7ed314282477c48b3124f06c5b70d92e830b3f85a18ecf0841f0916bdd8f9061
local architecture:       x86_64
local exit:               0
local stderr bytes:       0
local stdout bytes:       571
local stdout sha256:      564874aa8b2bdf28577947dbb82e249cf8cb338aa19dbde3ce3cf352e21ec7ff
```

The local run is one architecture lane only. The pull-request workflow
remains the required independent x86_64/aarch64 reproduction and aggregate
repository-integrity audit.
