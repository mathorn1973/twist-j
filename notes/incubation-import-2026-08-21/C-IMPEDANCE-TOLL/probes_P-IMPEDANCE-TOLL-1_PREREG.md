# P-IMPEDANCE-TOLL-1 preregistration

Status: PRE-PIN DRAFT

This document freezes the complete decision surface for the first public
attack on the impedance reading. It contains no gate output and earns no
scientific status. Formal execution is forbidden until this document and the
accepted verifier are committed, pushed as one immutable preregistration pin,
and that remote pin is read back.

Disclosure, binding: a dry run of the accompanying verifier was executed in a
non-public incubation lane before this pin. That run carries no public status,
no gate here rests on it, and its outputs are shipped alongside this package
under `candidate_dry_run/` clearly labelled. The formal run is the one taken
after the pin. Nothing below was written after reading a gate result; the
falsifiers and thresholds were fixed first and are unchanged.

## Public identity and action layer

- Claims attacked: `OMEGA3-UNIQUE`, `TOLL-BISECTOR-ROOT`,
  `IMPEDANCE-DEFINITIONAL-IDENTITY`, `IMPEDANCE-TOLL`,
  `IMPEDANCE-CHANNEL-COUNT`
- Public lock: issue to be opened before the pin
- Owner: one named session
- Branch: `probe/P-IMPEDANCE-TOLL-1`
- Path: `probes/P-IMPEDANCE-TOLL-1/`
- Action layer: L1 state. Pure arithmetic over Q with a formal pi and a formal
  unit monoid. No L2 manifold, no L3 boundary, no L4 support, no L5 stream, no
  L6 measure. Any lift needs its own named gate.

## 0. Falsifiers first

```
F1  OMEGA. If the ratio Omega_d / Omega_(d-1) equals 2 at any integer d >= 2
    other than d = 3, or fails to equal 2 at d = 3, the uniqueness claim dies.
F2  TAIL. If the closed form r(m) = 4^m m! (m-1)! / (2m)! fails to reproduce
    the computed odd-branch ratio at any tested m, or if the exact step ratio
    r(m+1)/r(m) = 2m/(2m+1) fails to be strictly below 1 at any tested m, the
    infinite tail is not closed and the claim caps at C over the scanned
    range instead of T.
F3  EVEN BRANCH. If any even-d ratio fails to be a nonzero rational multiple
    of pi to the first power exactly, the transcendence exclusion does not
    apply and the even branch is not closed.
F4  BISECTOR. If the identity (x^k + x^(-k)) x^k = x^(2k) + 1 fails in the
    group ring at any k, the bisector root dies.
F5  DEFINITIONAL IDENTITY. If Z_0 / R_K differs from 2 alpha as a monomial in
    the declared unit symbols, the reading dies at its root.
F6  OVERCLAIM GUARD, the important one. This probe does NOT derive the channel
    counts p and 2 p. If any output line, any registry row or any Canon
    sentence produced from this probe asserts that the channel counts are
    derived here, or that Z_0 / R_K = 2 alpha is a prediction rather than an
    identity of the declared definitions, the fold is rejected. The verifier
    asserts this guard on its own output.
F7  SCOPE. No SI value, no measured comparison, no length, no plate geometry,
    no lattice constant for J. Any such statement fires the probe.
```

## 1. Equation

Three separable statements plus one reading plus one named gap.

### 1.1 The closure step in dimension d

Let `Omega_d` be the surface measure of the unit sphere in `R^d`,

```text
Omega_d = 2 pi^(d/2) / Gamma(d/2).
```

Exactly, with `m` a positive integer,

```text
d = 2m     : Omega_d = 2 pi^m / (m-1)!
d = 2m + 1 : Omega_d = 2 . 4^m . m! . pi^m / (2m)!
```

so every `Omega_d` is a rational multiple of an integer power of pi.

Claim `OMEGA3-UNIQUE`: over the integers `d >= 2`,

```text
Omega_d / Omega_(d-1) = 2   if and only if   d = 3.
```

Structure of the decision, frozen: for odd `d = 2m + 1` the ratio is the pure
rational `r(m) = 4^m m! (m-1)! / (2m)!` with `r(1) = 2` and exact step ratio
`r(m+1)/r(m) = 2m / (2m+1) < 1` for every `m >= 1`, so `r` is strictly
decreasing and attains 2 only at `m = 1`, that is `d = 3`. For even `d` the
ratio is a nonzero rational multiple of `pi^1`, which equals 2 only if pi is
rational.

Declared external import, labelled as an import: pi is irrational
(Lambert 1761; Lindemann 1882 gives transcendence, more than is needed).

### 1.2 The bisector root

Claim `TOLL-BISECTOR-ROOT`: in the group ring `Z[x]/(x^(2p) - 1)` with
`p = 5`, for every integer `k`,

```text
(x^k + x^(-k)) . x^k = x^(2k) + 1,      x^(-k) := x^(2p - k mod 2p).
```

Under the archimedean reading `x = e^(i theta / 2)` this is
`1 + e^(i theta) = 2 cos(theta/2) e^(i theta/2)`. The algebraic identity is
the claim. The identification of its 2 with the closure toll of 1.1 and with
the Born half-angle is a reading and is carried separately at D, never at T.

### 1.3 The definitional identity

Work in the free abelian group on the symbols `e, eps_0, hbar, c, pi` with
rational coefficients. Adopt the standard definitions, declared as
definitions and not derived here:

```text
alpha := e^2 / (4 pi eps_0 hbar c)
R_K   := 2 pi hbar / e^2                (that is h / e^2)
Z_0   := 1 / (eps_0 c)                  (that is mu_0 c)
```

Claim `IMPEDANCE-DEFINITIONAL-IDENTITY`: as monomials,

```text
Z_0 = 4 pi alpha hbar / e^2      and      Z_0 / R_K = 2 alpha.
```

Both are identities of the declared definitions. This row exists precisely so
that no later summary can present `Z_0 / R_K = 2 alpha` as a prediction.

### 1.4 The reading

Claim `IMPEDANCE-TOLL`, status D, scope stated in full: on the primitive
scale `arg J = 2 pi / p` per tick, a channel that closes after `p` steps
carries the cycle factor `p (2 pi / p) = 2 pi`, and a channel that closes
after `2 p` steps carries `2 p (2 pi / p) = 4 pi`. Reading `R_K` as one
closure of the first kind and `Z_0` as one closure of the second kind puts
the ratio at `2 alpha`, and the 2 is then the same integer that 1.1 shows is
available as a geometric closure step in exactly one dimension, `d = 3`, and
that 1.2 exhibits as the bisector root. The laboratory identification of the
two objects with the measured constants remains the reading, not a
derivation.

### 1.5 The named gap

Claim `IMPEDANCE-CHANNEL-COUNT`, status O, with falsifier: the step counts
`p` and `2 p` are inputs to 1.4 and are NOT derived by this probe. The row
closes positively when the two counts are derived on the public architecture
from the primitive scale alone; it closes negatively when an exhaustive
public classification of admissible channel closures on that scale yields a
count pair other than `(p, 2 p)`, or yields more than one admissible pair.

## 2. Code

One verifier, `probes/P-IMPEDANCE-TOLL-1/verify.py`. Python standard library
only. `fractions.Fraction` and `int`. No float in any assertion. pi carried as
a formal symbol with an integer exponent; unit symbols carried as integer
exponent vectors. No filesystem read, no filesystem write, no network, no
randomness, no clock. Deterministic ordered output. Runs from the repository
root as `python3 probes/P-IMPEDANCE-TOLL-1/verify.py` under
`LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC`.
Runtime under 120 seconds.

## 3. Carrier

Pure arithmetic. The carrier of 1.1 is `Q[pi]` with integer exponents. The
carrier of 1.2 is the group ring `Z[x]/(x^10 - 1)`. The carrier of 1.3 is the
free abelian group on five unit symbols with `Q` coefficients. No kernel
state, no census, no stream, no measure, no physical carrier of any kind.

## 4. Systematics

```
S1  1.3 is definitional. Its evidential value for the programme is zero and
    its purpose is a guard against overclaim.
S2  1.2 is a one-line identity in a group ring. Its content is entirely in
    the reading, which stays at D.
S3  1.1 is a real theorem and is the only load-bearing mathematics here. Its
    even branch rests on one declared external import, the irrationality of
    pi.
S4  1.4 rests on step counts this probe does not derive. That is why 1.5
    exists as a separate O row with its own falsifier, instead of being
    folded silently into 1.4.
S5  The scan range in the verifier is finite. The infinite tail is closed by
    the closed form and its exact step ratio, not by the scan. If a reviewer
    rejects the closed-form argument the claim caps at C over the scanned
    range.
```

## 5. Failure threshold

```
G01  Omega_d exact for d = 1..40 as (rational, pi exponent)      F1
G02  ratio table for d = 2..40; equals 2 at d = 3 and nowhere else   F1
G03  odd branch: closed form matches the computed ratio for every
     tested m; r(1) = 2; step ratio 2m/(2m+1) strictly below 1      F2
G04  even branch: exponent exactly 1 and coefficient nonzero        F3
G05  primitive scale: p . (2 pi / p) = 2 pi, 2 p . (2 pi / p) = 4 pi F1
G06  bisector identity in the group ring for k = 0..9               F4
G07  Z_0 = 4 pi alpha hbar / e^2 and Z_0 / R_K = 2 alpha            F5
G08  overclaim guard: the verifier asserts that its own output names
     the channel counts as an OPEN obligation and never as derived   F6
G09  scope guard: the verifier asserts no SI unit word, no measured
     value and no length word appears in its own output              F7
G10  type guard: every asserted quantity is int or Fraction          all
```

Any gate FAIL is a probe failure and is merged as such. No threshold moves.

## 6. Action layer

L1. Declared above. No lift performed, none claimed.

## Two-platform requirement

Byte-identical stdout on two architectures is required before any
computation-grade status is recorded: one local run with neutral public
environment fields and the repository check at pull-request time on x86_64.

## Non-claims

No derivation of the channel counts. No prediction of `Z_0 / R_K`. No SI
value. No measured comparison. No length, no plate geometry, no lattice
constant for J. `METRO-EDGE-SCALE` untouched. No summary produced from this
probe may exceed the status or scope of the rows above.
