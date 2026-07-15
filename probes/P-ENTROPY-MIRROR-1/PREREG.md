# P-ENTROPY-MIRROR-1 preregistration

Status: PRE-PIN DRAFT

This document freezes the complete finite decision surface for the mirror-law
probe of the driven kernel: own-half involutions, alternating inverse maps,
the induced swap on canonical pentagons, the one-tick reflection coefficient
in one named gauge, and the corresponding finite composition identities. It
contains no formal gate output and earns no scientific status. Formal
execution is forbidden until this document and the accepted verifier are
committed, pushed, and read back as one immutable preregistration pin.

## Public identity and action layer

```text
program:          ENTROPY-BRIDGE
probe:            P-ENTROPY-MIRROR-1
public lock:      issue 36
owner:            A. M. Thorn
branch:           probe/P-ENTROPY-MIRROR-1
path:             probes/P-ENTROPY-MIRROR-1/
initial base:     ebc5c06f4d0bc5c0d01b931e4f26cccd72b60325
action layer:     L5 finite kernel structure; no L6 measure lift
scientific state: candidate finite C facts only; ENTROPY-LAYER-BRIDGE [O]
                  remains open
```

The authority base is Public Canon v4, tag `canon-v4`, activation commit
`ebc5c06f4d0bc5c0d01b931e4f26cccd72b60325`, content commit
`bea3b22c5e1a454bd3eca2dae6aa37eb75f70313`, Canon SHA-256
`9b5dff6f1b2b9ac1f322d17446a6f1957ee1e33c8eb90bbdfc7a13d09fc09391`,
and Canon byte count 58717. The completed public probes
P-ENTROPY-BRIDGE-1 through P-ENTROPY-BRIDGE-4 are inputs by reference. This
verifier independently rebuilds the finite kernel carrier and level-2 cell
structure needed by its own gates.

## Definitions frozen before execution

Use the public `F_5^6` kernel, generators, selector
`i = (z_6(psi) + 2 theta) mod 5`, branch maps `F_0,F_1`, and Thue-Morse
driver. Rebuild the recurrent components by the public warmup-400/window-300
census over the length-`2^16` Thue-Morse prefix. Let the recurrent support be
`R` and define the living halves

```text
H_eps = Im(F_eps | R),  eps in {0,1}.
```

Composition is read right to left. Define the level-k block maps by

```text
Phi^(0)_eps     = F_eps,
Phi^(k+1)_eps   = Phi^(k)_(1-eps) o Phi^(k)_eps.
```

For a recurrent component `A`, half `H_s`, and level `k`, the vertex return
group is generated on `A intersect H_s` by

```text
Phi^(k)_(s-k mod 2) o Phi^(k)_eps,  eps in {0,1}.
```

The canonical pentagon partition is the level-2 orbit partition already
validated by P-ENTROPY-BRIDGE-4. The public verifier reconstructs it rather
than importing another probe verifier. For every canonical cell `C`, define
the one-tick cell map by

```text
T_eps(C) = F_eps(C).
```

The gate requires this image to be one complete canonical cell.

The coherent level-2 gauge is frozen without a post-run choice. On each
component-half `H_s`, the named return

```text
Phi^(2)_s o Phi^(2)_(1-s)
```

orients every canonical five-cell. The least encoded state in the cell is
coordinate zero; successive applications of this return receive coordinates
`1,2,3,4`. No independent cellwise generator or orientation may be selected.

The unique size-10 recurrent component is called the singlet. Fixed-state
values are printed only as diagnostic witnesses; their numerical values are
not frozen acceptance inputs.

## Frozen claims and gates

### M01 CORE

The recurrent core has 6250 states on 313 components: 312 of size 20 and one
of size 10. Each component is invariant under each branch letter. The two
living halves are disjoint and have 3125 states each.

### M02 MIRROR

For each `eps in {0,1}`, the restriction `F_eps | H_eps` is an involution
with cycle type

```text
{1: 1, 2: 1562}.
```

Its unique fixed state lies in the singlet component.

### M03 ALTERNATION

The cross restrictions are mutually inverse in the following exact
directions:

```text
F_1 o F_0 = id on H_1,
F_0 o F_1 = id on H_0.
```

### M04 SWAP

For each `eps`, the own-half action `T_eps | H_eps` fixes the singlet
pentagon and swaps the two pentagons in every size-20 component-half. Its
cell cycle type is

```text
{1: 1, 2: 312}.
```

Every cell image remains in the same recurrent component.

### M05 REFLECTION

In the frozen coherent level-2 gauge, every one-tick cell map is affine over
`F_5` with multiplier `a = 4 = -1`. On every source cell, the ordered pair of
letter maps is one of

```text
((4,0), (4,2)),
((4,2), (4,0)),
```

and each order occurs on exactly 625 of the 1250 source cells.

### M06 CONSISTENCY

On both source halves, the following cell-map composition identities hold:

```text
T_0 o T_1 = T_0 o T_0,
T_1 o T_0 = T_1 o T_1.
```

These four finite comparisons are the complete M06 gate.

## Six frozen preregistration fields

```text
equation:     gates M01 to M06 exactly as stated above.
code:         verify.py in this directory; Python 3 standard library only;
              exact integer/set/permutation arithmetic; no floats; one
              process; no filesystem writes; target runtime under 120 s.
carrier:      public F_5^6 kernel constants, Thue-Morse prefix 2^16,
              warmup 400/window 300 recurrent census; no external data.
systematics:  living halves, level-2 vertex return groups, canonical cells,
              coherent level-2 gauge, component ranges, cycle types,
              affine pairs, and exact cell counts are frozen above;
              disclosed pre-pin development is recorded below.
failure
threshold:    any gate FAIL. Every comparison is exact; no tolerance and no
              adaptive range, component, partition, or gauge is permitted.
action layer: L5 finite kernel structure. A passing two-architecture run can
              earn C only for this declared carrier; it cannot promote the
              open entropy bridge or any measurable or infinite claim.
```

## Falsifier map

A census, half, or component-invariance mismatch fires M01. A
non-involution, wrong cycle type, zero or multiple fixed states, or a fixed
state outside the singlet fires M02. Any failed state equality in the two
frozen directions fires M03. A non-five cell, wrong cell census, split or
cross-component image, moved singlet cell, or wrong own-half cycle type fires
M04. A non-affine cell map, multiplier other than four, pair outside the two
frozen orders, or order census other than 625 plus 625 fires M05. Any of the
four failed cell composition comparisons fires M06. Every fired result is
retained and merged; no threshold moves after the pin.

## Environment and formal execution

```text
cd <repo root>
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
  python3 probes/P-ENTROPY-MIRROR-1/verify.py
```

The first formal run occurs only after the remote preregistration pin is read
back. It must run on a neutral aarch64 Linux environment. Its exact stdout
becomes `EXPECTED.txt`; `RUN.md` records neutral platform and architecture
fields plus the pin and file hashes. GitHub x86_64 then reruns the pinned
verifier and must produce byte-identical stdout. `RESULT.md` is added only
after the formal record exists; the registry and Canon remain unchanged in
this probe.

## Pre-pin development disclosure

An incubation candidate and three non-formal break-it paths preceded this
public preregistration. They established plausibility, helped freeze the six
gates, and included non-formal x86_64 executions. They carry no public status,
are not evidence, and their stdout is not copied into this probe. The public
verifier was adapted into the public probe identity and is not formally
executed before its remote pin.

## Out of scope, explicitly

- no measurable, ergodic, spectral, or all-scale mirror theorem;
- no inverse-limit factor, cohomology decision, or gauge-independent normal;
- no identification of a reflection coefficient with a lambda digit;
- no construction or promotion of the equivariant selection family;
- no measure transport, L2 lift, or physical interpretation;
- no registry, frontier, Canon, or release edit in this probe.

Any one of those requires a separate public proof, probe, or later public
Canon fold.
