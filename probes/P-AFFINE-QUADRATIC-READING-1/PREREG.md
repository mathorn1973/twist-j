# P-AFFINE-QUADRATIC-READING-1 preregistration

Date: 2026-08-21

Author of record: A. M. Thorn

Status: preregistered protocol only. Formal execution count zero. No scientific
result is earned by this file. The accepted `verify.py` may be parsed,
compiled and inspected statically, but it is not imported or executed before
this file and `verify.py` are committed together, pushed, and read back byte
for byte from the public remote.

Public claim lock: issue 495, opened before this file was committed.

## Authority

```text
STATE:          ACTIVE
CANON:          Public Canon v59
AUTHORITY:      mathorn1973/twist-j main
TAG:            canon-v59
CONTENT_COMMIT: 5da6b883defebd8edc470db1e2e7ebde095ef20a
CANON_SHA256:   7fdea700589a21303109dbb6c33fecd2d8243d0d09184ab9d471f0a59687f641
CANON_BYTES:    314310
BASE_COMMIT:    2a5601a9ec5cd5c8e24e80f3da78ca6838608fb4
LAYER:          L1 exact arithmetic only
```

Gate performed against a clean checkout of public `main`, not an attachment or
a rendered page: `canon/SHA256SUMS` five of five OK, the recomputed hash and
byte count of `canon/CANON.md` equal the declared fields, and both `canon-v59`
and the content commit are ancestors of `main`.

The probe changes exactly `probes/P-AFFINE-QUADRATIC-READING-1/`. Canon,
registry, frontier, evidence, gate, release and workflow files are excluded.

## Collision search

Searched before drafting: open and closed issues, remote branches, `probes/`,
and the registry. No probe, branch or claim of this name exists. Adjacent
public rows, named here so that no reader mistakes this for a move on any of
them:

```text
J-MAHLER-MEASURE [T]                  already carries the M_J characteristic
                                      polynomial x^4-3x^3+4x^2-2x+1 = Phi_5(x-1)
                                      and its irreducibility. Blocks N6 and N7
                                      below are an audit of that row, not a new
                                      claim.
TRACEKERNEL-RESIDUAL-FORM [T]         already carries G_p = p I_n - 11^T as the
                                      nontrivial-root trace Gram, so the matrix
                                      5 I_4 - 11^T is public. This probe does
                                      not re-derive it; it asks whether it is
                                      the ONLY invariant of its degree.
QDD-J-AFFINE-APPARATUS-NONSELECTION [T]  uses a faithful G-orthogonal
QDD-INSTRUMENT-NONSELECTION [T]          AGL_1(F_5) action of order 20 and the
QDD-J-CENTRALIZER-NONSELECTION [T]       frozen form G = I_4-(1/5)11^T at L4
QDD-RECORD-COMPLETE-LUEDER-SELECTION [T] apparatus/support scope. Those rows
                                      IMPORT the form and the group as frozen
                                      data. This probe derives, at L1 only,
                                      that the form is the unique invariant of
                                      its degree. Deriving a form is not
                                      selecting an apparatus: no non-selection
                                      row is weakened, contradicted or moved,
                                      and no instrument, coupling, pointer or
                                      post-state law is claimed here.
READING-SPLIT [D]                     unchanged. No totality, uniqueness or
                                      completeness of the decoder is claimed.
```

## Result exposure

RESULT-EXPOSED, not blind. The statement, the census dimensions and the
Q(sqrt5) control were derived in non-canonical incubation work on this same
date and exercised there by a separate implementation with a different
structure and different check labels. Those bytes, runs and outputs are
discovery context only and are not evidence. The accepted `verify.py` here is
a fresh implementation in repository output form; it carries the residual
implementation risk that the pin deliberately forbids pre-testing. Written
proofs below carry the universal statements; the verifier audits them.

## Field 1: equation

Public notation is pinned first, because this lane has already produced one
symbol collision. `M_J = m_J` is the full step for `J = 1 + zeta_5^2`, and

```text
D_J := M_J - I = m_{zeta_5^2}
```

is the motor. Then `mu_{D_J} = Phi_5(X)`, `mu_{M_J} = Phi_5(X - 1)`,
`det(M_J - I) = N(zeta_5^2) = 1` and `det(D_J - I) = N(zeta_5^2 - 1) = 5`.

Let `u: zeta_5 -> zeta_5^2` be the Galois generator, `c = u^2` complex
conjugation, `K = Q(zeta_5)`, `K+ = Q(sqrt5)`, and

```text
G := <D_J, u | D_J^5 = u^4 = 1, u D_J u^-1 = D_J^2>
```

the Frobenius group `AGL_1(F_5)` of order 20, sharply two-transitive on five
points. Let `V = K` as a four-dimensional `Q`-space in the basis
`1, zeta, zeta^2, zeta^3`, and

```text
q_+(x) = Tr_{K+/Q}(x c(x)).
```

### A. Absolute linear wall

```text
A  dim_Q End_{Q[G]}(V) = 1.
```

The commutant condition is a rational linear system; the rank of a rational
matrix does not change under extension of scalars, so
`dim_L End_{L[G]}(V_L) = 1` for every field `L` of characteristic zero. `G` is
finite and `char L = 0`, so Maschke applies: a reducible `V_L` would be
decomposable and its endomorphism algebra would have dimension at least two.
Hence `V_L` is irreducible for every such `L`, and every nonzero
`G`-equivariant linear map out of `V_L` is injective. No lossy equivariant
linear reading exists over any characteristic-zero field.

### B. Degree-two census

```text
B1  (V*)^G = 0
B2  (Lambda^2 V*)^G = 0
B3  (Sym^2 V*)^G = Q . q_+, of dimension exactly one
B4  q_+ is positive definite
```

Each is the dimension of the rational solution space of an invariance system,
hence field-independent by the same rank argument. With `B1` and `B2`, degree
two is the first degree carrying a nonzero invariant scalar reading, and by
`B3` it carries exactly one line. Adding the two further premises `q != 0` and
`q >= 0` singles out the ray `Q_{>0} . q_+`. Positivity is a fourth premise and
is stated as one: three premises give a line, four give a ray.

Independent route for `B3`: `G` is sharply two-transitive on five points, so it
has exactly two orbits on ordered pairs, so the invariant bilinear forms on the
permutation module `Q^5` are exactly `span{I_5, 11^T}`, and the second dies on
the augmentation.

### C. The motor-only controls

The same census under `C_5 = <D_J>` alone returns symmetric dimension two,
alternating dimension two, and endomorphism dimension four. Over `K+` the
motor even admits a lossy equivariant idempotent,

```text
E = (D_J + phi I)(D_J^2 + psi D_J + I) / sqrt5,   psi = 1 - phi,
```

of rank two, and `u E u^-1 = I - E`. So the compression wall of the motor alone
falls exactly at the adjunction of `phi`, while the affine wall of `A` stands
over every characteristic-zero field. The Galois generator is not decoration:
it is what removes the second symmetric channel, both alternating channels, and
the `K+` breach.

### D. Target comparison last

Only after the class is settled: with `P(e_x) = zeta_5^x` the augmentation
intertwiner, `J = I + T^2` on the augmentation is `M_J`, and

```text
P^T Gram(q_+) P = (5 I_5 - 11^T)/2.
```

The unique invariant is the Euclidean form of the five points. As matrices,
`5 I_4 - 11^T = 2 Gram(q_+)` and `I_4 - (1/5)11^T = (2/5) Gram(q_+)`, so both
frozen public constants are positive rational multiples of it. Whether the
carrier basis of any other public row equals this frozen `zeta`-power basis is
NOT asserted by this probe; the identification of carriers is left to whatever
row would use it.

## Field 2: code

Accepted file:

```text
probes/P-AFFINE-QUADRATIC-READING-1/verify.py
```

Standard library only, integers and `Fraction` only, with `Q(sqrt5)` carried as
ordered `Fraction` pairs. No float, no complex, no approximation, no
randomness, no network, no subprocess, no external data, no import of
incubation or scratch material, no filesystem read or write, and no read of
`canon/`. Zero arguments. Deterministic stdout with no environment, platform,
timing or path field, so stdout is byte-identical on every architecture. Empty
stderr. Exit zero on a clean pass and nonzero on any fired check.

## Field 3: carrier

```text
group:            G = AGL_1(F_5), order 20, sharply two-transitive
module:           V = Q(zeta_5) in the basis 1, zeta, zeta^2, zeta^3
permutation model: Q^5 with T: e_x -> e_{x+1}, s_2: e_x -> e_{2x}
intertwiner:      P(e_x) = zeta_5^x, rank 4, kernel the all ones vector
control field:    K+ = Q(sqrt5) as exact Fraction pairs
target constants: 5 I_4 - 11^T and I_4 - (1/5)11^T, compared last
```

No external data.

## Field 4: systematics

No tolerance anywhere: every assertion is an exact equality of rationals or of
integers. Known hazards and their controls:

```text
symbol collision M_J versus D_J   block N pins both, and a drift fails loudly
rank over Q read as rank over L   the field-independence argument is written
                                  above, not left to the machine
uniqueness read as selection      the census is over forms, never apparatus;
                                  the L4 non-selection rows are quoted, not moved
line read as ray                  positivity is carried as a separate premise
Burnside route as the only route  the kernel computation and the orbit count
                                  are both run, and must agree
target seen too early             the frozen constants enter only in block T
```

Runtime limit 120 seconds. Hidden target input, omitted control, float in an
assertion, pre-pin execution, post-pin mutation, an unnamed layer lift, or any
sentence that reads the unique form as a physical Born rule is STOP.

## Field 5: failure threshold and decision

Thresholds never move after this pin.

```text
AFFINE-QUADRATIC-READING-CONFIRMED
  every check passes: notation pins hold, the group closes at order 20, the
  endomorphism algebra is one dimensional, the linear and alternating invariant
  spaces vanish, the symmetric invariant space is the single line Q q_+ with
  q_+ positive definite, both motor-only controls return two, the K+ idempotent
  exists and is exchanged with its complement by u, and the target comparison
  holds.

AFFINE-QUADRATIC-READING-FIRED
  any check fails. First-class outcome: the run is recorded and merged, the
  probe is sealed, and no threshold is adjusted.
```

The candidate falsifiers, one line each:

```text
a nonzero lossy G-equivariant linear reading of V over any characteristic-zero
field; a nonzero G-invariant linear functional; a nonzero G-invariant
alternating form; a G-invariant symmetric form outside Q q_+; a failure of any
notation pin; a failure of the pullback identity.
```

Maximum later rows, claimed only at the earned status and scope:

```text
AFFINE-READING-DEGREE-CENSUS [T]
AFFINE-QUADRATIC-FORM-UNIQUENESS [T]
```

Both are `L1` rows about invariant forms. Neither creates a decoder, an
apparatus, a measure or a physical reading, and neither may be summarized
beyond that scope.

## Field 6: layer

`L1` state only. No `L2` manifold, `L3` boundary, `L4` support, `L5` stream or
`L6` measure statement is made, and no lift is named or attempted. The physical
identification of `q_+` with a Born square is not part of this probe and stays
outside it.

```text
SAMPLING NOT PROVIDED.
```

## Formal order

Commit and push `PREREG.md` and `verify.py` together; read both back byte for
byte from the public remote; one formal run from the repository root; add
`EXPECTED.txt`, `RUN.md` and `RESULT.md` without changing the pin; one
probe-only pull request; byte identity on x86_64 and aarch64; aggregate
`check`; merge with a merge commit only. Registry, frontier and Canon
treatment is a separate later fold.
