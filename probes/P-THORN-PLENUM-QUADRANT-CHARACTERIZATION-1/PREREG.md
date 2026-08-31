# P-THORN-PLENUM-QUADRANT-CHARACTERIZATION-1 preregistration

Date: 2026-08-28

Author of record: A. M. Thorn

Status: preregistered protocol only. Formal execution count: zero. No
scientific result is earned by this file. The accepted `verify.py` may be read,
parsed, compiled, and inspected statically before the immutable public pin, but
it has not been imported or executed.

Public claim lock: issue #633, opened before this file is committed.

```text
branch:  probe/P-THORN-PLENUM-QUADRANT-CHARACTERIZATION-1
path:    probes/P-THORN-PLENUM-QUADRANT-CHARACTERIZATION-1/
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
ACTION_LAYER:   L1 exact cyclotomic and ordered-embedding characterization only
```

Before the immutable issue lock and first commit, GitHub `main`, matching
issues, pull requests, public branches, `STATUS.md`, `POLICY.md`, `AGENTS.md`,
`canon/CORE.md`, `canon/FRONTIER.md`, `canon/REGISTRY.tsv`, the Canon, and the
source probe must be read back. Any collision or changed authority basis is
STOP.

This probe changes exactly its own directory. It changes no Canon, Registry,
Frontier, dependency, evidence, gate, workflow, release, decoder, Note,
promotion package, or existing probe file.

## Consumed source candidate

Merged PR #631 placed

```text
P-THORN-TRIANGLE-PENTAGON-RIGIDITY-1
THORN-TRIANGLE-PENTAGON-RIGIDITY
```

on `main` as `candidate-T / L1`. That source owns the exact conditional
equivalence

```text
S_z = 1 + N_z
iff
Phi_5(z) = 0
iff
z has exact order five.
```

It also owns the resulting scale values `phi^-2` and `phi^2`. It remains
candidate-T. This probe neither promotes it nor awards it a second evidential
credit. The source also owns the scalar primitive-third-root breaker
`t=-1,N=1,S=3`, the weak relation `S+N^-1=4`, and failure of the full closure.

The present target is strictly downstream: it classifies the four source
solutions after a standard complex embedding and a fixed square root of
minus one have been declared.

## Collision and adjacent ownership

The fresh collision scan must cover at least

```text
P-THORN-PLENUM-QUADRANT-CHARACTERIZATION-1
THORN-PLENUM-QUADRANT-CHARACTERIZATION
THORN-ORIENTED-MOUNT
PLENUM-QUADRANT
FIXED-I
ZETA20
ORIENTATION-SELECTION
```

Existing public objects retain their ownership.

1. `J-PROJECTIONS [T]` owns the principal public value of `J`.
2. `J-RAMIFIED-CHORD [T]` and `PLENUM-POINT [T]` own the public principal
   chord and plenum identities.
3. `P-THORN-TRIANGLE-PENTAGON-RIGIDITY-1` owns the candidate source closure.
4. This probe owns only the exact fixed-embedding quadrant characterization,
   its Galois nonuniqueness guard, and the new fixed-`i` mounted lift
   `T=sqrt(3)+i` of the already-owned primitive-third-root breaker.
5. No physical orientation, time direction, vacuum selector, action law, or
   preferred embedding is owned here.

This probe is `RESULT-EXPOSED`: the target table and its Galois obstruction
were derived in public discussion before the pin. That discussion is
provenance only. The proof below carries the theorem.

## Field 1: fixed carrier and embedding

Let

```text
r = zeta_20 = exp(2 pi i / 20)
i = r^5
zeta_5 = r^4
```

in the fixed standard complex embedding. Thus `i`, the real axis, the
imaginary axis, and their positive directions are declared comparison data.

For a unit-circle point `z`, define

```text
J_z = 1 + z^2,
N_z = J_z conjugate(J_z),
S_z = (1-z)(1-conjugate(z)),
T_z = 2 i (1-J_z) = -2 i z^2.
```

The admissible source locus for the main theorem is

```text
S_z = 1 + N_z.
```

By the consumed source theorem this locus consists exactly of the four
primitive fifth roots. The present theorem does not weaken or replace this
condition.

Put

```text
phi  = (1+sqrt(5))/2,
beta = phi^-1,
s_J  = positive sqrt(3-phi).
```

## Frozen result ceiling

The maximum result is

```text
THORN-PLENUM-QUADRANT-CHARACTERIZATION
candidate-T ceiling; L1 only
```

with exactly the following five parts.

### Q1. Exact fixed-i quadrant table

For `k=1,2,3,4`, put `z=zeta_5^k`. Then

| `z` | exact `T_z` | `N_z` | quadrant |
|---|---|---|---|
| `zeta_5` | `s_J + i phi` | `phi^-2` | I |
| `zeta_5^2` | `-phi s_J - i phi^-1` | `phi^2` | III |
| `zeta_5^3` | `+phi s_J - i phi^-1` | `phi^2` | IV |
| `zeta_5^-1` | `-s_J + i phi` | `phi^-2` | II |

On all four points,

```text
|T_z|^2 = 4,
(Re T_z)^2 = S_z,
(Im T_z)^2 = N_z^-1,
Im T_z = 2-N_z.
```

### Q2. Fixed-i principal characterization

With the standard embedding and `i=r^5` held fixed,

```text
S_z = 1+N_z,
Re T_z > 0,
Im T_z > 0
iff
z = zeta_5.
```

Equivalently, within the source closure locus the first quadrant
characterizes

```text
J_z = J,
T_z = T_pl.
```

The two signs have distinct roles:

```text
Im T_z > 0
iff
N_z = phi^-2.
```

Thus the imaginary sign chooses the contracting pair. Within that pair,

```text
T_{z^-1} = -conjugate(T_z),
```

so the real sign distinguishes `zeta_5` from `zeta_5^-1`.

### Q3. Full cyclotomic Galois nonuniqueness

The full Galois group is

```text
Gal(Q(zeta_20)/Q) = (Z/20Z)^x
                  = {1,3,7,9,11,13,17,19}.
```

For `sigma_a(r)=r^a` and the principal point `T_pl=2r^3`,
the complete quadrant census is

| `a` | `sigma_a(zeta_5)` | `sigma_a(i)` | `sigma_a(T_pl)` | quadrant |
|---:|---|---|---|:---:|
| 1 | `zeta_5` | `i` | `2r^3` | I |
| 3 | `zeta_5^3` | `-i` | `2r^9` | II |
| 7 | `zeta_5^2` | `-i` | `2r` | I |
| 9 | `zeta_5^-1` | `i` | `2r^7` | II |
| 11 | `zeta_5` | `-i` | `2r^13` | III |
| 13 | `zeta_5^3` | `i` | `2r^19` | IV |
| 17 | `zeta_5^2` | `i` | `2r^11` | III |
| 19 | `zeta_5^-1` | `-i` | `2r^17` | IV |

Hence the first quadrant occurs twice in the full Galois orbit, for
`a=1` and `a=7`. In particular,

```text
sigma_7(zeta_5)=zeta_5^2,
sigma_7(i)=-i,
sigma_7(T_pl)=2r,
```

and `sigma_7(T_pl)` is also in quadrant I.

The stabilizer of the declared `i` is

```text
{1,9,13,17}.
```

Within this stabilizer only `a=1` lies in quadrant I. Therefore the uniqueness
in Q2 is a fixed-i characterization and is not an intrinsic selector in the
abstract field `Q(zeta_20)`.

### Q4. Mounted lift of the primitive-third-root guard

The fixed plenum mount without the full Thorn closure is insufficient.
The scalar data `t=-1,N_z=1,S_z=3` and the closure failure are inherited from
the source probe and earn no new credit here. The new downstream statement is
their exact fixed-`i` mount and quadrant lift.

For

```text
z = zeta_3^2,
t = z+z^-1 = -1,
N_z = 1,
S_z = 3,
T_z = sqrt(3)+i,
```

one has

```text
|T_z|^2 = 4,
(Re T_z)^2 = S_z,
(Im T_z)^2 = N_z^-1,
Im T_z = 2-N_z = 1,
S_z + N_z^-1 = 4,
Re T_z > 0,
Im T_z > 0.
```

But

```text
S_z != 1+N_z
```

and `Phi_5(z)` is nonzero. Thus the plenum mount plus first-quadrant
positivity does not select the pentagon. The full first Thorn closure remains
load-bearing. This extends the source breaker; it does not re-earn it.

### Q5. Scope and nonselection boundary

The theorem says only:

```text
fixed standard i
+ source closure
+ first-quadrant inequalities
characterize the already public principal point.
```

It does not derive or physically select:

```text
i,
a complex embedding,
positive real or imaginary axes,
time orientation,
chirality,
the Thorn closure,
a vacuum state,
an action carrier,
h or hbar,
a decoder,
an SI normalization,
or an L2-L6 object.
```

Calling the first quadrant an “oriented positive plenum” adds no theorem unless
a separate higher-layer construction independently supplies the ordered axes
and proves the closure. No selector, physical mechanism, or preferred
embedding is claimed.

## Written proof

Write `r=zeta_20`, so `i=r^5` and `zeta_5=r^4`. For
`z=zeta_5^k=r^(4k)`,

```text
T_z
 = -2 i z^2
 = -2 r^(5+8k)
 = 2 r^(15+8k).
```

For `k=1,2,3,4`, the exponents modulo twenty are respectively

```text
3, 11, 19, 7.
```

They lie in quadrants I, III, IV, II.

In `Q(r)` put

```text
phi  = r^2+r^-2,
s_J  = r^3+r^-3,
beta = phi-1 = phi^-1.
```

Resolving real and imaginary parts gives exactly

```text
2r^3  = s_J+i phi,
2r^11 = -phi s_J-i beta,
2r^19 = +phi s_J-i beta,
2r^7  = -s_J+i phi.
```

This proves Q1. Squaring the displayed coordinates and using the source
identities proves the mount equations. The table also gives

```text
Im T_z = 2-N_z.
```

Therefore the imaginary part is positive exactly on the contracting pair.
For fixed `i`,

```text
T_{z^-1}
 = -2 i z^-2
 = -conjugate(-2 i z^2)
 = -conjugate(T_z).
```

This preserves the imaginary part and reverses the real part. Q2 follows.

Every automorphism of `Q(r)` is uniquely `sigma_a(r)=r^a` for
`a` in `(Z/20Z)^x`. Since `T_pl=2r^3`,

```text
sigma_a(T_pl)=2r^(3a).
```

The eight exponents give the complete Q3 table. The first quadrant appears
for `a=1,7`; requiring `sigma_a(i)=i` leaves `a=1,9,13,17`, among which only
`a=1` is in quadrant I.

Finally, for `z=zeta_3^2`, direct exact reduction by
`z^2+z+1=0` gives the values in Q4. This proves that the source closure cannot
be replaced by mount and sign data. Only the mounted fixed-`i` lift is new;
the underlying scalar breaker remains owned by the source probe.

## Falsifiers

One exact counterexample fires the corresponding part:

1. any entry of the fixed-i table is false;
2. a source-closure point other than `zeta_5` lies in quadrant I, or
   `zeta_5` does not;
3. `Im T_z>0` fails to coincide with the contracting pair;
4. `T_{z^-1}=-conjugate(T_z)` fails;
5. the full Galois orbit has only one first-quadrant point, or an additional
   one besides `a=1,7`;
6. the fixed-i stabilizer has a first-quadrant point besides `a=1`;
7. the primitive-third-root control fails any mount or sign equality stated
   in Q4, satisfies the full closure, or annihilates `Phi_5`;
8. the result selects an embedding, orientation, time direction, chirality,
   vacuum, action law, or physical plenum rather than merely characterizing
   the principal point conditionally.

A stale authority basis, changed pin, source promotion, nonzero verifier exit,
nonempty stderr, stdout mismatch, architecture disagreement, or scope widening
is integrity STOP, not a scientific falsifier.

## Frozen controls

```text
B1  z=zeta_5^-1 is contracting and in quadrant II.

B2  z=zeta_5^2 is expanding and in quadrant III.

B3  z=zeta_5^3 is expanding and in quadrant IV.

B4  sigma_7 simultaneously maps zeta_5 to zeta_5^2 and i to -i,
    but keeps the transformed T in quadrant I.

B5  replacing i by -i moves the first-quadrant root from zeta_5 to
    zeta_5^2.

B6  z=zeta_3^2 gives T=sqrt(3)+i and passes the mount and quadrant
    tests while failing S=1+N.
```

## Verifier contract

The accepted `verify.py` is standard-library only. It uses integers,
`Fraction`, exact polynomial reduction in `Q[x]/Phi_20`, and exact
`Q(sqrt(3))` pairs. It performs no floating-point operation, tolerance test,
numerical root finding, random search, network access, subprocess, clock read,
or external source import.

The written proof carries the theorem. The verifier audits:

```text
G01 source_scope_firewall
G02 cyclotomic_20_carrier
G03 source_closure_four_roots
G04 fixed_i_quadrant_table
G05 fixed_i_exact_coordinates
G06 plenum_mount_identities
G07 contraction_and_conjugation_signs
G08 fixed_i_first_quadrant_unique
G09 full_galois_first_quadrant_nonunique
G10 fixed_i_stabilizer_unique
G11 mounted_third_root_lift_guard
G12 scope_nonselector_guard
```

Success requires all gates to print `PASS`, followed exactly by

```text
DECISION THORN-PLENUM-QUADRANT-CHARACTERIZATION-CONFIRMED
```

with exit zero and empty stderr. Any other outcome is STOP pending diagnosis;
no equation, carrier, sign convention, or scope may move after the pin.

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

No Canon fold, promotion package, selector claim, or physical interpretation
is part of this probe transaction.
