# P-J-BINARY-NORM-DESCENT-1 preregistration

Date: 2026-08-21

Author of record: A. M. Thorn

Status: preregistered protocol only. Formal execution count zero. No scientific
result is earned by this file. The accepted `verify.py` may be parsed,
compiled and inspected statically, but it is not imported or executed before
this file and `verify.py` are committed together, pushed, and read back byte
for byte from the public remote.

Public claim lock: issue 499, opened before this file was committed.

## Authority

```text
STATE:          ACTIVE
CANON:          Public Canon v59
AUTHORITY:      mathorn1973/twist-j main
TAG:            canon-v59
ACTIVATION:     7820173bdf035fa8b59e40113fdad3ac3c66f12a
CONTENT_COMMIT: 5da6b883defebd8edc470db1e2e7ebde095ef20a
CANON_SHA256:   7fdea700589a21303109dbb6c33fecd2d8243d0d09184ab9d471f0a59687f641
CANON_BYTES:    314310
BASE_COMMIT:    1b288cbed5a9ccdfed5edde906df82fa1522870e
LAYER:          L1 integral / finite-field algebra only
```

Authority was read from public `main`, not an attachment. The v59 activation
commit and declared content commit are ancestors of `BASE_COMMIT`.
`canon/SHA256SUMS` carries the same Canon SHA-256 declared by `STATUS.md`.
The probe changes exactly `probes/P-J-BINARY-NORM-DESCENT-1/`. No Canon,
Registry, Frontier, Evidence, Gate, workflow, release or status file is in
scope.

## Collision search

The exact identifiers `P-J-BINARY-NORM-DESCENT-1` and
`J-BINARY-NORM-DESCENT` were absent from open and closed issues, remote
branches and `probes/` before issue 499 claimed them.

Two adjacent public results are binding collision guards rather than targets:

```text
CARRY-PENTAD [T]
  already owns the four-bit second-carry form, Arf invariant one, its five
  nonzero singular points, O^-(4,2) ~= S_5, and the typed mod-two A4 bridge.
  This probe may compare against that geometry only at the final gate. It may
  not recount Arf=1 or O(q)=S_5 as a new theorem.

P-AFFINE-QUADRATIC-READING-1
  sealed probe on current main. At L1 in characteristic zero it proves that
  G=<D_J,u>=AGL_1(F_5) has no invariant linear scalar and one invariant
  symmetric line, Q q_+, with q_+(x)=Tr_(K+/Q)(x c(x)). Its own firewall says
  no characteristic-two reduction and no Born/physical lift. This probe asks
  for that missing exact reduction seam.
```

Open claim 316, `P-CARRY-QUADRATIC-SYMMETRY-1`, owns a prime-free carry
hierarchy question. It is not edited, resumed, used as evidence, or widened.

## Result exposure

RESULT-EXPOSED, not blind. Before the public pin, conversational reconnaissance
found the expected F16 field, a five-point binary singular locus and S5
orthogonal symmetry using a different coordinate implementation. During the
collision audit the stronger norm-trace formula and a type correction were
found: Frobenius is the reduction of the Galois generator `u`, not the
multiplication motor `D_J`. Those exploratory calculations are discovery
context only and are not evidence. The accepted verifier below is a fresh
repository implementation and deliberately carries residual implementation
risk until the pin.

## Field 1: equation and written proof

Freeze

```text
j  = zeta_5,
J  = 1 + j^2,
K  = Q(j),
O  = Z[j],
K+ = Q(j+j^-1),
c  = u^2 : j -> j^-1 = j^4,
u          : j -> j^2,
D_J = m_(j^2),
q_+(x) = Tr_(K+/Q)(x c(x)).
```

Let

```text
L = A_4 = {x in Z^5 : sum_r x_r = 0},
P(x) = sum_(r=0)^4 x_r j^r.
```

A bar means reduction modulo 2 and `alpha=bar(j)`.

### A. Binary field integrity

The polynomial

```text
Phi_5(X) mod 2 = X^4+X^3+X^2+X+1
```

has no root in F2. A reducible quartic over F2 with no linear factor would be a
product of two irreducible quadratics. The only monic irreducible quadratic is
`X^2+X+1`, whose square is `X^4+X^2+1`, not `Phi_5`. Therefore `Phi_5` is
irreducible over F2 and

```text
O/(2) ~= F_16.
```

For the real subfield, `t=j+j^-1` satisfies `t^2+t-1=0`; modulo two this is
`X^2+X+1`, so

```text
O_(K+)/(2) ~= F_4.
```

Three controls are frozen to block selection rhetoric:

```text
Z[i]/(2)      ~= F2[X]/((X+1)^2)            nonreduced,
Z[zeta_7]/(2) ~= F2[X]/(Phi_7)
               ~= F8 x F8                   because
               Phi_7=(X^3+X+1)(X^3+X^2+1),
Z[zeta_3]/(2) ~= F4                          field.
```

Thus “the mod-two shadow is a field” is J-specific compared with some nearby
controls but is not a uniqueness theorem for J, order five, or p=5.

### B. Galois/Frobenius descent and the motor distinction

In `F16`, the Frobenius is `F(y)=y^2`. Since `alpha` is the reduction of `j`,

```text
bar(u)(alpha)=alpha^2=F(alpha),
bar(c)(alpha)=alpha^4=F^2(alpha).
```

Both maps are F2-linear ring automorphisms and agree on the generator, hence
on all of F16:

```text
bar(u)=Frob_2,
bar(c)=Frob_2^2.
```

The multiplication motor is a different map:

```text
bar(D_J)(y)=alpha^2 y.
```

It cannot equal Frobenius because at one

```text
bar(D_J)(1)=alpha^2 != 1=Frob_2(1).
```

This inequality is a required negative control. Any result wording that calls
these two maps identical is false at the frozen type.

On the five roots `mu_5=<alpha>`, write `alpha^k` by exponent label
`k in F5`. Then

```text
bar(D_J): alpha^k -> alpha^(k+2),
Frob_2:   alpha^k -> alpha^(2k).
```

The first is translation by two and the second is dilation by two. Since two
has order four in `F5^*`, these maps generate

```text
F5 semidirect F5^* = AGL_1(F5)
```

of order twenty, sharply two-transitive on the five labels. This is the exact
residue descendant of the characteristic-zero affine pair `(D_J,u)`.

No prime-two selection follows from the exponent action. For any rational
prime `p != 5` with `p == 2 mod 5`, Frobenius on a fifth root satisfies
`j^p=j^2`; there are infinitely many such primes by Dirichlet, but the only
fact needed here is the elementary congruence. The verifier audits sample
members only; the universal statement rests on the displayed congruence.

### C. Norm-trace reduction of q_+

For integral `x in O`, put `a=x c(x) in O_(K+)`. The nontrivial embedding of
`K+` is the restriction of `u`, so

```text
q_+(x)=a+u(a).
```

After reduction modulo two, `bar(c)=Frob_2^2`, hence

```text
bar(a)=y y^4 = N_(F16/F4)(y).
```

On F4, `bar(u)` is the nontrivial Frobenius `s->s^2`; therefore

```text
q_2(y) := q_+(x) mod 2
        = Tr_(F4/F2)(y y^4)
        = Tr_(F4/F2)(N_(F16/F4)(y)).
```

This is independent of the chosen integral lift because it is the reduction of
an integral quadratic form.

Its polar form is

```text
B(y,z)=Tr_(F4/F2)(y z^4 + z y^4).
```

To prove nondegeneracy, take `y != 0` and write `z=y t`. Then

```text
B(y,yt)=Tr_(F4/F2)(N(y)(t+t^4)).
```

The relative trace `t->t+t^4` from F16 to F4 is a nonzero F4-linear map with
kernel F4, hence is onto. Multiplication by `N(y)!=0` is bijective on F4, and
the absolute trace F4->F2 is nonzero. Some `t` therefore gives `B(y,yt)=1`.
Thus the radical is zero.

For `y != 0`, the norm lies in `F4^*`. The kernel of the absolute trace on F4
is F2, so the only nonzero element of F4 with trace zero is one. Hence

```text
q_2(y)=0  iff  N_(F16/F4)(y)=1.
```

The norm kernel has size `(16-1)/(4-1)=5`. Since `alpha` has order five and
`N(alpha)=alpha^5=1`,

```text
ker N_(F16/F4) = mu_5.
```

Therefore the five cyclotomic points are exactly the complete nonzero singular
locus of the binary reduction of the affine invariant form.

The abstract consequences “minus type”, “Arf invariant one” and
`O(q) ~= S5` are collision-owned by `CARRY-PENTAD [T]`. They are not proposed
as new rows here.

### D. Exact A4 bridge

Use the simple-root basis

```text
b1=e1-e0, b2=e2-e1, b3=e3-e2, b4=e4-e3.
```

Then

```text
P(b_r)=j^(r-1)(j-1), r=1,...,4.
```

So these images are the standard O-basis of the principal ideal `(j-1)O` and

```text
P(L)=(j-1)O.
```

The index in O is `|N(j-1)|=5`, odd, so reduction modulo two makes

```text
bar(P): L/2L -> O/2O
```

an F2-linear isomorphism.

For `x=(x_0,...,x_4) in L`, write `z=P(x)`. Since
`q_+(z)=(1/2)Tr_(K/Q)(z c(z))` and

```text
Tr_(K/Q)(j^m) = 4  if m=0 mod 5,
                -1 otherwise,
```

one obtains

```text
Tr_(K/Q)(z c(z))
 = 4 sum_r x_r^2 - sum_(r!=s) x_r x_s
 = 5 sum_r x_r^2
```

because `sum_r x_r=0`. Therefore

```text
q_+(P x) = (5/2) sum_r x_r^2.
```

The sum of squares is even because `x_r^2=x_r mod 2` and the coordinate sum is
zero. Reducing gives

```text
q_+(P x) mod 2
 = (1/2) sum_r x_r^2 mod 2
 = q_A(x mod 2),
```

where `q_A` is exactly the A4 form already typed in `CARRY-PENTAD [T]`.
Thus `bar(P)` is an exact isometry from the registered carry-pentad carrier to
the norm-trace finite-field presentation.

### E. Target comparison last

Only after A-D. Under `bar(P)`, the five nonzero `q_A` singular points map to
`mu_5`, the five nonzero `q_2` singular points. This identifies two already
existing presentations of the same binary form. The `S5` orthogonal geometry
remains the registered `CARRY-PENTAD` theorem and receives no new status here.

## Field 2: code

Accepted file:

```text
probes/P-J-BINARY-NORM-DESCENT-1/verify.py
```

Standard library only. Integer arithmetic and explicit finite-field bit
polynomials only. No floats, complex floating values, approximation,
randomness, network, subprocess, external data, command-line arguments, or
filesystem reads/writes. The cyclotomic ring is represented exactly in the
basis `(1,j,j^2,j^3)` with integer polynomial reduction by Phi5. F16 is
represented exactly as four-bit polynomials modulo Phi5 mod two.

The verifier audits:

```text
A1-A4  mod-two field integrity and three comparison controls
B1-B6  Galois/Frobenius descent, motor inequality, five-point affine action
C1-C5  norm, trace, q_+ reduction, singular locus, polar nondegeneracy
D1-D5  A4 ideal image, mod-two isomorphism, pullback identity, final comparison
```

Twenty atomic checks. Deterministic stdout only. Empty stderr. Exit zero on a
clean pass, nonzero on any assertion failure. Runtime limit 120 seconds.

## Field 3: carrier

```text
characteristic-zero carrier: O = Z[zeta_5]
real fixed ring:              O_(K+)
residue carrier:              O/(2) = candidate F16
fixed residue subfield:       F4
integral bridge lattice:      A4 = {sum x_r=0}
bridge:                       P(x)=sum x_r zeta_5^r
quadratic form:               q_+(x)=Tr_(K+/Q)(x c(x))
residue quadratic form:       q_2=Tr_F4/F2 o Norm_F16/F4
five-point set:               mu_5=<alpha>
affine maps:                  multiplication by alpha^2; Frobenius y->y^2
registered final comparison:  CARRY-PENTAD q_A only
```

No external data and no physical carrier.

## Field 4: systematics

No tolerance. Every scientific assertion is an exact equality or finite
cardinality. Hazards and required controls:

```text
Frobenius versus motor type confusion
  explicit B2 inequality at 1; output names translation and dilation separately.

field-at-two read as uniqueness
  Gaussian, zeta7 and zeta3 controls; zeta3 is itself a field control.

Frob exponent read as prime-two selection
  p == 2 mod 5 warning is written into the theorem and sample-audited.

Arf/S5 collision
  CARRY-PENTAD is named before the new result; S5 is target comparison only.

finite enumeration read as universal proof
  finite-field and trace arguments are written in Field 1; the verifier is audit.

half-integral expression treated carelessly mod two
  q_+(P x) is proved to equal 5 times the integer (sum x_r^2)/2 before reduction.

target seen too early
  CARRY-PENTAD comparison occurs only in block D after the residue class is fixed.
```

Any float in an assertion, hidden physical dictionary, pre-pin execution,
post-pin mutation, or unnamed layer lift is STOP.

## Field 5: failure threshold and decision

Thresholds never move after the pin.

```text
J-BINARY-NORM-DESCENT-CONFIRMED
  every A-D atomic statement survives, including the required negative
  statement D_J mod 2 != Frobenius, the exact norm-trace form, its mu5 singular
  locus, and the A4 isometry.

J-BINARY-NORM-DESCENT-FIRED
  one exact mathematical assertion in A-D fails. The counterexample is
  recorded as first-class result. No threshold, carrier, field or map changes.

STOP
  authority/collision/pin/integrity/scope/layer discipline fails without an
  exact mathematical negation.
```

Atomic falsifiers include reducible `Phi5 mod 2`, a nonfield O/(2), wrong
Galois/Frobenius map, accidental equality of the motor with Frobenius, affine
action not of order 20, failure of q_+ to reduce to the norm-trace form, a
singular point outside mu5, a mu5 point with nonzero q2, degenerate polar form,
or failure of the A4 pullback/isometry.

Maximum later theorem row, only after a separate fold and only at the earned
scope:

```text
J-BINARY-NORM-DESCENT [T]
```

No row for Arf, S5, Boolean completeness, Thue-Morse, Born, decoder or physical
selection is authorized by this probe.

## Field 6: layer

L1 only. Integral algebra, finite-field quotient and same-layer carrier
isometry. No L2 manifold, L3 boundary, L4 support, L5 stream or L6 measure.
No layer gate is named or attempted.

Explicit nonclaims:

```text
no uniqueness of J, p=5, order five or characteristic two;
no claim that F2, XOR, AND or Boolean completeness is J-specific;
no derivation of Thue-Morse;
no claim that quadratic degree alone selects characteristic two;
no Born probability, normalization, effect, apparatus, instrument, event,
sampling or measure;
no decoder completion, spacetime, force or SI statement.
```

`READING-SPLIT [D]`, `QUADRATIC-DECODER-DATA [O]`, and all QDD apparatus rows
remain unchanged.

```text
SAMPLING NOT PROVIDED.
```

## Formal order

1. Commit and push only `PREREG.md` and accepted `verify.py` together.
2. Read both exact remote blobs back; record commit, SHA-256 and byte counts.
3. Only then execute `verify.py` once from a clean checkout of that exact pin.
4. Add exact stdout as `EXPECTED.txt`, a neutral `RUN.md`, and `RESULT.md`
   without changing either pinned file.
5. Open one probe-only pull request.
6. Require byte-identical stdout on public x86_64 and aarch64 jobs and aggregate
   `check` before any two-architecture computation-grade claim.
7. Merge only by merge commit if and when owner/review permits. Canon treatment
   is a separate later sealed fold.
