# PREREG. P-DE-TRACE-DENSITY-1

Public anchor: issue #88 (the DE-CONFORMAL-WEIGHT scope decision, closed as
not planned pending the owner's dictionary decision). This probe decides the
computational outcome space of that issue. It does not reopen the issue, it
does not make the dictionary decision, and it earns no decision. Base: Public
Canon v12, main merge commit `9009a54` (fold/canon-v12-final), Canon content
commit `347419ea97adaf344571df164a7367302b115686`, CANON_SHA256
`617779dae1a300304f70a776fa8e857efa8c8540fc4b01793bd3c8407fb88fd0`, tag
`canon-v12`.

```text
LAYER:  L5 stream, homogeneous scope, scale variable chi = log a. The tested
        dictionary transports an L2 object (the trace Gram weight) to an L5
        object (the density character of the trace sector). No lift is
        claimed; the transport is the object under test.
TARGET: decide which outcome of issue #88 holds over the registered set
        R(v12) for the frontier row DE-CONFORMAL-WEIGHT [O]:
        PASS-EARNED | NEGATIVE | NONUNIQUE | STOP.
```

No scientific status is earned by this preregistration. The eventual Canon
and registry disposition is separate reviewed work and, in the PASS-of-issue
sense, an explicit owner decision that this probe cannot and does not make.

## Frozen equation set

FRW continuity in chi = log a constrains a sector by the single exact
coefficient identity

```text
d (1 + w_q) = q,   w_q = q/d - 1,   rho_q proportional to a^(-q).
```

The registered set R(v12) tested for selection power over q:

```text
R1  FRW-CANONICAL-FORM [T]: 3 H^2 = lambda rho, lambda = 216 pi, H^2 =
    72 pi rho, k_f = 1, continuity; the registry row explicitly excludes
    source-projector uniqueness and any amplitude ansatz.
R2  MEASURE-SPATIAL-ONLY [T]: Gram weights 1/p on the trace and conformal
    directions, 1 on the spatial base, 3/4 = d/(d+1).
R3  CONFORMAL-PREFACTOR [D]: K_chi5 = k/(12 V_cell) = 1/(864 pi), c_hom =
    12 K_chi5 = 1/(72 pi), 864 = 12 . 72.
R4  The DeWitt block: G[g](g,g) = d(1 - lambda d), substrate lambda =
    1/d - 4/3 = -1, value 12; control lambda = +1, value -6 (the conformal
    ghost).
R5  Architecture p = 5, d = 3.
```

Dictionary under test: `Delta_DE := gamma_tr = 1/p`, equivalent through
continuity, at p = 5 and d = 3, to `w_DE = 1/(pd) - 1 = -14/15` (the
committed COSMOLOGY-REGISTER form).

Selection question, frozen: does any member of R1..R5, or any exact relation
among their sealed constants, pin a unique q, other than by assuming
`Delta_DE := gamma_tr` itself? Circular selection is excluded by definition.

## Frozen thresholds

Binary per outcome, exact equality only, no tolerance.

```text
PASS-EARNED  iff exactly one density character q survives R(v12).
NEGATIVE     iff R(v12) excludes q = 1/p.
NONUNIQUE    iff at least two inequivalent characters survive R(v12).
STOP         iff the trace line, the scale variable, or the map fails to type.
```

Any assertion failure in the verifier fails the probe; the dead branch is
archived, never deleted; no threshold moves after the fact.

## Code

`verify.py`: Python 3 standard library only, fractions.Fraction in every
assertion, pi carried as a formal symbol and never evaluated, no floats
anywhere in the file, decimal witnesses by exact long division only and
assertion-free, runtime far under 120 s, run from repo root with

```text
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
```

Independent break path `break_de_trace_density_1.py`: hand-rolled
integer-pair rationals, no fractions import, adversarial scan for a
non-circular selector over q = n/m, |n| <= 20, 1 <= m <= 12.

## Falsifiers

```text
MATH (armed permanently): exhibition of a registered v12-sealed constraint
  that pins a unique q by a non-circular exact relation kills any NONUNIQUE
  closure of this probe.
PHYSICAL (proposed for the fold, not part of this computation): F-DE-W,
  constant w = -14/15; fires if a named public dataset release (DESI DR3 or
  later, or Euclid) excludes constant w = -14/15 at or beyond 5 sigma in its
  published constant-w posterior. The fold PR names the release.
```

## Provenance disclosure

This probe validates a frozen incubation candidate (C-DE-TRACE-DENSITY-1).
The incubation preregistration was frozen before any execution on
2026-07-20T18:23:59Z, SHA-256
`330f44be891bea77e2aebc353303c185f83d7abc5cb0bcd5fa666cb3dede9403`
(8651 bytes). The verifier committed here is byte-identical to the incubation
verifier, SHA-256
`7eaca91f6c3d73830f86750f142e910f2fd38e404821eeaeb3ac43f16c6e2188`
(7376 bytes), which was pinned before its first execution and has produced
byte-identical stdout on two author-side platforms (Ubuntu x86_64,
Python 3.11.15; Ubuntu 24.04 aarch64, Python 3.12.3), stdout SHA-256
`62127bf909d1d50624f77d744905f3c99287db816365a27b5ef458f3fddec0c5`
(3313 bytes). The public pin is this commit; the required GitHub x86_64
check at PR time re-runs the verifier, and byte identity with EXPECTED.txt
is the gate for any computation-grade status.
