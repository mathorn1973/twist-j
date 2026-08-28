# P-CM-PERIOD-LATTICE-NONSELECTION-1 result

Status: **candidate-T / L1 / CM-PERIOD-LATTICE-NONSELECTION CONFIRMED LOCALLY /
PUBLIC CANON STATUS UNCHANGED.**

The accepted immutable verifier was read back from the public pin before
execution. The verifier process exited zero, wrote empty captured stderr and
produced the exact committed `EXPECTED.txt` bytes. All six frozen audit gates
passed. No scientific falsifier fired.

## Exact positive result: the primitive period subgroup

For `L=Z^4`, let an integral alternating form have upper coefficients

```text
Omega=(w01,w02,w03,w12,w13,w23).
```

The exact algebraic image subgroup

```text
Per_Z(Omega)={Omega(C):C in Lambda^2 L}
```

is

```text
Per_Z(Omega)
 = gcd(w01,w02,w03,w12,w13,w23) Z.
```

The six basis bivectors give the six coefficients, and Bezout gives the gcd as
an attained value. This is a theorem about an integer pairing, not a geometric
period integral.

For the public CM pencil

```text
Omega_(a,b)=(a,b,-b,a,b,a),
Pf(Omega_(a,b))=a^2-ab-b^2,
```

one gets

```text
Per_Z(Omega_(a,b))=gcd(a,b) Z.
```

If `Pf=+-1`, every common divisor of `a,b` has square dividing `1`; hence

```text
Per_Z(Omega_(a,b))=Z
```

for every integral unimodular/Pell form. The positive primitive generator of
this L1 period subgroup is therefore exactly `1`.

## Exact pullback firewall

For every `A in GL_4(Z)`,

```text
Per_Z(A^* Omega)=Per_Z(Omega).
```

Indeed `Lambda^2 A` is a lattice automorphism. Thus the period image is
unchanged under integral change of variables.

In particular the public Pell shift and the public J-pullback preserve the
period subgroup. On the CM parameter pair,

```text
S(a,b)   =(a+b,a),
P_J(a,b) =(a-b,-a+2b),
```

and both preserve `gcd(a,b)`. Their Pfaffian actions differ:

```text
Pf(S Omega)   =-Pf(Omega),
Pf(P_J Omega) = Pf(Omega).
```

The important negative conclusion is exact:

```text
one J-pullback does not multiply the primitive integral period subgroup by
phi^-2; it maps Z to the same Z.
```

Therefore the stable eigenvalue `phi^-2` cannot be interpreted as the ratio of
this primitive period invariant before and after one J-pullback.

## No natural unit-period cell from Omega_1 alone

For the public `Omega_1`, use the four integral symplectic transvections

```text
T_v(x)=x+Omega_1(x,v)v,
v=e_0,e_1,e_2,e_3.
```

Each preserves `Omega_1`. Their common fixed lattice on `Lambda^2 Z^4` is

```text
Z Pi,
Pi=(1,0,1,0,0,1),
```

with

```text
Omega_1(Pi)=2.
```

So not one unit-period bivector is fixed even by this four-element family. A
single-cell selector depending only on the unmarked form and natural under all
its integral symplectic automorphisms would have to be fixed when the input
form is fixed. Such a selector cannot return `Omega_1(C)=1`.

The canonical object supplied by unimodularity is therefore the image subgroup
`Z`, not a distinguished generator cell in `Lambda^2 Z^4`.

## Full-pencil root-of-unity control

Multiplication by `zeta_5` lies in the public root-of-unity kernel and fixes
the complete CM pencil. Its exterior-square fixed rational space is exactly

```text
C(a,b)=(b,a,b,a,a,b).
```

For these bivectors

```text
Pf_biv(C(a,b))
 =-(a^2-ab-b^2).
```

A four-dimensional bivector is decomposable exactly on the Pfaffian-zero
quadric. The equation

```text
a^2-ab-b^2=0
```

has no nonzero rational solution. Hence the only decomposable rational
bivector fixed by the root-of-unity kernel is zero.

This independently blocks a natural fixed nonzero rank-two cell selected from
the full CM pencil alone. It does not exclude invariant nondecomposable
two-classes, cell orbits, or later selectors using additional typed data.

## Boundary for an action bridge

The exact L1 conclusion is

```text
integrality + unimodularity force the primitive period subgroup Z,
but do not force a natural individual unit-period cell;
J-pullback preserves the primitive period subgroup rather than scaling it.
```

This sharpens the next cross-layer obligation. A physical action construction
cannot be justified merely by saying that a primitive symplectic cell shrinks
by `phi^-2`, because that statement is false for the canonical integral
period subgroup and no natural individual unit-period cell is selected by the
L1 form alone.

A later positive route must introduce a separately typed object, for example a
geometric cycle class, polarization, boundary condition, stable linear
coordinate, prequantum datum or another registered carrier. Which of those is
admissible is not decided here.

## Scope firewall

This result is L1 exact lattice algebra only. `Per_Z` is an integer image
subgroup, not a torus period integral.

No torus, manifold, cohomology, homology, embedded surface, physical action,
`h`, `hbar`, `2 pi`, SI normalization, prequantization, U(1), electromagnetic
phase, decoder, apparatus, L5 event stream or L6 measure is derived.

Current public `canon/GATES.tsv` has no CM alternating-form L1-to-L2
action-period gate. This probe neither creates nor closes one.

## Local evidence

```text
pin_commit:       225f1b162f42a7aa1522841ab3df9997f153d848
prereg_sha256:    6eda2cc507656c50096a7fdeccb09a0d83dd094c7e5f4f06a8c5317172c6523f
verifier_sha256:  df3cc662b90cc4505b3eb319bd4f5cea4ea240cd012923afc59ecc89f05599bd
local_platform:   Debian GNU/Linux 13
local_arch:       x86_64
local_python:     Python 3.13.5
verifier_exit:    0
verifier_stderr:  0 bytes
stdout_bytes:     580
stdout_lines:     7
stdout_sha256:    de9393e0d0b2f2156e997d226d862b7afe99429733376c95f05509602567eeac
```

The local lane alone is reproduction, not a public two-architecture gate.
Public promotion is not earned by this probe record alone. A later Canon fold
would be separate even after the required architecture gate passes.
