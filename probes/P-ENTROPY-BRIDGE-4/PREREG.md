# P-ENTROPY-BRIDGE-4 preregistration

Status: PRE-PIN DRAFT

This document freezes the complete finite decision surface for the fourth
probe of the ENTROPY-BRIDGE program: the arithmetic frame, canonical
pentagon quotient of the living kernel, its finite quotient holonomy, its
affine cocycle in one named gauge, and a bounded component-local cylinder
no-go. It contains no formal gate output and earns no scientific status.
Formal execution is forbidden until this document and the accepted verifier
are committed, pushed, and read back as one immutable preregistration pin.

## Public identity and action layer

```text
program:          ENTROPY-BRIDGE
probe:            P-ENTROPY-BRIDGE-4
public lock:      issue 33
owner:            entropy-bridge v4 session
branch:           probe/P-ENTROPY-BRIDGE-4
path:             probes/P-ENTROPY-BRIDGE-4/
initial base:     da5c3423891390a7960522232a73c1a6fad17db3
action layer:     L5 finite kernel/driver structure and exact lambda-tower
                  arithmetic; no L2 lift or measure claim
scientific state: candidate finite C facts inside ENTROPY-LAYER-BRIDGE [O];
                  the atom, ergodic, cohomology, and inverse-limit readings
                  remain outside the machine claims
```

The authority base is Public Canon v3, tag `canon-v3`, activation commit
`1bfee0cd907c079cc095df0a93add19400bfcabf`, content commit
`b0872ebd4fd66bed03a988e375f88e928d252057`, Canon SHA-256
`58fef832e0cc554195cbd27967c8ed00097d45c5ab9647c14ee349b6ccd3eea6`,
and Canon byte count 57264. This probe follows the sealed public probes
P-ENTROPY-BRIDGE-1, -2, and -3. Their conclusions are inputs by reference;
this verifier independently rebuilds the finite kernel carrier needed by its
own gates.

## Definitions frozen before execution

Use the public `F_5^6` kernel, generators, selector
`i = (z_6(psi) + 2 theta) mod 5`, branch maps `F_0,F_1`, and Thue-Morse
driver from the sealed probes. The recurrent components are rebuilt by the
public warmup-400/window-300 census. Define the living halves
`H_eps = Im(F_eps|R)`.

The level-k block maps are frozen recursively by

```text
Phi^(0)_eps     = F_eps,
Phi^(k+1)_eps   = Phi^(k)_(1-eps) o Phi^(k)_eps.
```

For a recurrent component `A`, half `H_s`, and level `k`, the vertex return
group is generated on `A intersect H_s` by

```text
Phi^(k)_(s-k mod 2) o Phi^(k)_eps,  eps in {0,1}.
```

Its orbits are the level-k cells. The canonical pentagon partition used by
the quotient and affine gates is the level-2 partition (the gate separately
requires equality with every level `k = 1..10`).

The affine gauge is fixed without post-run choice. On each component-half,
the named level-2 cross-letter return

```text
Phi^(2)_s o Phi^(2)_(1-s)
```

orients every five-cell. The least encoded state in the cell is coordinate
zero; successive applications of this named return receive coordinates
`1,2,3,4`. No independent cellwise choice of generator or orientation is
allowed.

For the bounded no-go, the unique size-10 component is the singlet. The
canonical size-20 component is the component having the least minimum encoded
state among all size-20 components. Words are the distinct factors in the
length-`2^16` Thue-Morse prefix. A window of length `L` is tested at cursor
positions `0`, `floor(L/2)`, and `L-1`.

## Frozen claims and gates

### G01 CORE

The census has recurrent core 6250 on 313 disjoint components: 312 of size
20 and one of size 10. The two living halves are disjoint sets of size 3125.

### G02 ARITHMETIC

With `lambda = 1-zeta_5`,

```text
J^10 + 1 is in lambda^6 O and not in lambda^7 O,
J^2  + 1 is in lambda O   and not in lambda^2 O.
```

Membership is tested exactly in the regular representation modulo 25, using
`lambda^(4+j) O = 5 lambda^j O` for `j = 1..3`.

### G03 FRAME

Each recurrent component is invariant under each branch letter separately.
For every `k = 0..10`, `eps in {0,1}`, and source half,

```text
Im(Phi^(k)_eps) = H_((eps+k) mod 2)
```

and the restriction is a bijection onto that target half.

### G04 PENTAGONS

At `k = 0` every vertex return group is trivial. For every component and
half, at every `k = 1..10`, the vertex return group is cyclic of order five
and its orbit partition is independent of k. Every orbit has five states.
Each half of a size-20 component has two pentagons; each half of the singlet
has one; each full living half therefore has

```text
312 * 2 + 1 = 625 = 5^4
```

pentagons.

### G05 EQUIVARIANCE

Each one-tick branch map sends every canonical pentagon cell onto exactly one
canonical pentagon cell.

### G06 QUOTIENT

For `k = 1..8`, every generator of the level-k vertex return group fixes each
canonical pentagon class setwise. Equivalently, the induced vertex holonomy
on the pentagon-class quotient is trivial over the frozen range.

### G07 AFFINE

For every component, half, canonical cell, `k = 0..10`, and
`eps in {0,1}`, the map induced by `Phi^(k)_eps` between the frozen source
and target gauges is affine `x -> a x + b` over `F_5`, with nonzero `a`.
For every `(k,eps)`, the set of `(a,b)` pairs is identical on all 313
components and equals the following frozen table:

```text
k=00 eps=0 (4,0) (4,2)    k=00 eps=1 (4,0) (4,2)
k=01 eps=0 (1,0) (1,3)    k=01 eps=1 (1,0) (1,3)
k=02 eps=0 (1,1) (1,3)    k=02 eps=1 (1,1) (1,3)
k=03 eps=0 (1,1) (1,4)    k=03 eps=1 (1,1) (1,4)
k=04 eps=0 (1,0) (1,3)    k=04 eps=1 (1,0) (1,3)
k=05 eps=0 (1,0) (1,3)    k=05 eps=1 (1,0) (1,3)
k=06 eps=0 (1,1) (1,3)    k=06 eps=1 (1,1) (1,3)
k=07 eps=0 (1,1) (1,4)    k=07 eps=1 (1,1) (1,4)
k=08 eps=0 (1,0) (1,3)    k=08 eps=1 (1,0) (1,3)
k=09 eps=0 (1,0) (1,3)    k=09 eps=1 (1,0) (1,3)
k=10 eps=0 (1,1) (1,3)    k=10 eps=1 (1,1) (1,3)
```

In particular, rows repeat exactly with period four wherever both indices
lie in `k = 1..10`. This table belongs only to the named gauge above. It does
not assert that its multipliers are a gauge-independent copy of the lambda
digit action.

### G08 BOUNDED-NOGO

The component-local cylinder constraint system has exactly zero solutions in
all 900 frozen cases:

```text
components:       singlet and canonical size-20 component
window lengths:   L = 4..16
cursor positions: 0, floor(L/2), L-1
cyclic clocks:     1,2,4,5,8,10,16,20,32,40,80

additional cases: singlet, cyclic clock 4, L = 17..30,
                  the same three cursor positions
```

The first block contains `2 * 13 * 3 * 11 = 858` cases and the extension
contains `14 * 3 = 42`, for 900 total. This is a bounded finite result, not a
claim about every component, clock, window, or measurable selector.

## Six frozen preregistration fields

```text
equation:     gates G01 to G08 exactly as stated above, including the full
              affine table and all 900 no-go cases.
code:         verify.py in this directory; Python 3 standard library only;
              exact integer/set/permutation arithmetic; no float; one
              process; no filesystem writes; target runtime under 120 s.
carrier:      public F_5^6 kernel constants, Thue-Morse prefix 2^16,
              regular representation of J and lambda modulo 25; no external
              data.
systematics:  census warmup 400/window 300; k ranges, components, gauges,
              factors, cursors, clocks, and affine table frozen above;
              disclosed pre-pin development below.
failure
threshold:    any gate FAIL. Every comparison is exact; no tolerance and no
              adaptive range or gauge is permitted.
action layer: L5 finite structure. A passing two-architecture run can earn C
              only for the declared finite ranges; it cannot promote the
              open entropy bridge or any measurable/infinite claim.
```

## Falsifier map

A census mismatch fires G01. Either failed ideal membership fires G02. A
component crossed by a letter or a block image with the wrong half fires G03.
A non-five cell, nonconstant partition, wrong cell census, or non-order-five
group fires G04. A split cell image fires G05. A moved quotient class fires
G06. A non-affine cell map, differing component spectrum, differing frozen
row, or broken period fires G07. A nonzero G08 count exhibits a bounded
finite selection and revives that exact case. Every fired result is retained
and merged; no range, component, gauge, or threshold moves after this pin.

## Environment and formal execution

```text
cd <repo root>
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
  python3 probes/P-ENTROPY-BRIDGE-4/verify.py
```

The first formal run occurs only after the remote preregistration pin is read
back. Its exact stdout becomes `EXPECTED.txt`; `RUN.md` records neutral
platform and architecture fields plus the pin and file hashes. A preliminary
`RESULT.md` is added before the pull request. GitHub x86_64 reruns the pinned
verifier and must produce byte-identical stdout.

## Pre-pin development disclosure

The supplied recon note and its named `recon_bridge4*.py` scripts were
incubation material outside this repository and carry no public status; those
scripts were not available here. The public verifier was reconstructed from
the sealed kernel definitions. Three explicitly non-formal Windows x86_64 dry
runs on 2026-07-14 were used before this pin to debug the gauge definition,
freeze the displayed affine table, and check the accepted table literally.
The first independently oriented each cell and was rejected because that
choice erased multiplier information by a cellwise gauge change. The second
introduced the named coherent level-2 return now frozen above; the third
checked the resulting frozen table. All three agreed on G01-G06 and G08,
including all 900 no-go cases. None is a reproduction or evidence for a
public status.

## Out of scope, explicitly

- no formal claim that the finite depth-five bijection is dead;
- no ergodic-atom theorem, spectral argument, or all-scale holonomy law;
- no measurable cohomology decision or inverse-limit factor construction;
- no gauge-independent identification of the affine multiplier with J;
- no regularity, measure transport, L2 lift, or physical interpretation;
- no registry, frontier, Canon, or release edit in this probe.

Any one of those requires a separate public proof, probe, or later sealed
Canon fold.
