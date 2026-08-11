# P-ARITH-RAPIDITY-1 result

Date: 2026-08-11

## Decision

```text
ARITH-RAPIDITY-PASS
```

All 26 preregistered checks passed with exit code 0 and empty stderr on the
local aarch64 formal leg, and the identical 2896-byte stdout was reproduced on
a second architecture (x86_64) from its own fresh clone of the pinned branch
before this record was committed. The repository-required GitHub x86_64 and
aarch64 jobs rerun the pinned verifier at pull-request time; the probe
evidence gate is complete when they reproduce the committed `EXPECTED.txt`
byte for byte. **Canon status: unchanged.** This probe PR creates no Registry
or Canon claim.

## Frozen scope decided

Within the preregistered L1 scope, at computation grade (C), as an audit of
the written proofs embedded in `PREREG.md`:

```text
G1  Decomposition identities. On the 288-point grid with 58 product
    pairs: rho and N multiplicative; the signed interval identity
    t^2 - s^2 = N(x) with sign; x conj(x) = (N, 0); the rest locus is
    class zero exactly iff ab = 0; no nonzero F-rational null vector.
G2  Units. N(phi^k) alternates to k = 12; rho(phi) = -phi^2 exactly;
    phi^n = (L_n + F_n sqrt5)/2 with L_n^2 - 5 F_n^2 = 4(-1)^n to
    n = 30; the sheet sign matches parity: Lucas is the time reading,
    sqrt5 Fibonacci the space reading, and the alternator N(phi) = -1
    exchanges the sheets.
G3  Exact class machinery. The logarithm-free +-phi^(2Z) membership
    test agrees with direct comparison for |m| <= 12, returns 0 on
    rho(sqrt5) and on rationals, and returns the exact shift n on
    phi^n for |n| <= 8.
G4  Split primes. For all 146 split p < 2000, two structurally
    independent constructions, a Pell sweep and a Euclidean gcd with
    every division step asserted norm-decreasing, both return a
    generator of norm +p, and the canonical unordered rapidity classes
    agree: R1(p) = R2(p) in every case. Orientation data, gating
    nothing: 70 pairs agree oriented, 76 only after conjugation, the
    expected signature that construction (i) fixes no orientation and
    only the unordered R(p) is canonical.
G5  Well-definedness. For all 45 split p < 500 and five generator
    variants each, the class is unchanged; the conjugate class is the
    negative, tested as rho(pi) rho(conj pi) = 1 exactly.
G6  Anchors. All 155 inert p < 2000 sit at class zero exactly; the
    ramified generator sqrt5 has rho(sqrt5) = -1 and class zero, with
    eta exactly 0 rather than 0 modulo the lattice.
G7  Frame covariance. Frame change by phi^k preserves the |N| scale,
    shifts every class by exactly k, and leaves rapidity differences
    invariant.
G8  Density witness. 583 distinct norm-one rational classes exhibited
    from the Pell parametrization with numerator and denominator under
    40: a finite witness that the rational norm-one subgroup is not
    discrete, against the discrete unit lattice of G2.
G9  Interface consistency, no claim. rho(conj pi) = rho(pi)^-1 exactly
    for all 146 split p < 2000; weights recorded as integers,
    N(p) = p split and p^2 inert.
G10 Self-audit. The printed inventory of executed check names equals
    the checks executed, 26 of 26, auditable from the stdout alone.
```

## What this result means

The signed Galois decomposition of F = Q(sqrt5) carries an exact integer
Minkowski structure: t^2 - s^2 = N(x) with sign, timelike N > 0 and
spacelike N < 0, with an empty arithmetic null locus against a nonempty
real null cone. The rapidity lattice log phi is supplied by the units
alone, while the rational norm-one points are dense among them. Every
split rational prime p carries a canonical unordered rapidity class
R(p) = {r, -r} in (R/(log phi)Z)/{+-1}, computable exactly and without
logarithms through even-index Lucas traces, agreeing across two
independent generator constructions at every tested prime, with inert
and ramified primes anchored at class zero. Arithmetic rapidity is a
number-theoretic invariant of the prime, not of the construction.

## What this result does not mean

No layer lift occurred. This result asserts nothing about zeta zeros,
the Riemann hypothesis, Weil positivity, or explicit formulae; the
Hecke-type interface of claim E is a frozen definition asserted of
nothing. No decoder movement, no physical reading beyond the existing
[D] rows, and no space-dimension conclusion from unit rank. The
universal quantifiers of claims A and C are carried by the written
proofs embedded in `PREREG.md`, not by this finite audit. No Registry
row moves and no Canon file changes with this probe.

## Reproducibility state

```text
pin:             1c4ed7e1c04c9d1813fb412a9a685465e78c5c70
PREREG sha256:   e008765f71d9b9ec4fa8ebdb8701c32d18a511b7338cd25e936547b2dd8caf08
verifier sha256: 6a7dad0baa248b3566cf8288b129749ad0e69174b589579e7feb31a1f9a7d1c4
stdout sha256:   67c6aa8aad59fe21b45e068582841ac14da46446194fe8826d41adcb1952a598
local aarch64:   PASS, Debian GNU/Linux 13, Python 3.13.5, empty stderr, 11 s
cross x86_64:    PASS, Ubuntu 22.04, Python 3.10.12, byte-identical stdout
GitHub x86_64:   pending, runs at pull-request time
GitHub aarch64:  pending, runs at pull-request time
Canon fold:      not started
```

The next boundary is the owner's review and merge of this one-probe branch
without squash or rebase, under the claim lock of issue 342. Any Registry or
Canon movement is a later, separate reviewed action; the natural home
proposed there is section 10, Relativity as counting, beside
BOOST-READING-SPLIT and BOOST-COUNT-LADDER, with ARITHMETIC-RAPIDITY-
DECOMPOSITION and SPLIT-PRIME-RAPIDITY-CLASS carried at the status the fold
earns them, the frame reading of claim D at most [H], and the interface of
claim E at most [O].
