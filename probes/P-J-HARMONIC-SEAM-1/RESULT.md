# P-J-HARMONIC-SEAM-1 result

Date: 2026-08-09

## Decision

```text
SEAM-PASS
```

**Evidence status: C at this stage.** The accepted local exact audit is one
x86_64 lane. The written derivation is a theorem candidate, but no public `T`
status is claimed by this result file. Any promotion requires review, the
repository-required x86_64/aarch64 byte-identical check, and a separate Canon
fold.

## Frozen scope decided

The exact audit returned 38/38 PASS with no tolerance and empty stderr.
Within the preregistered L1 scope:

```text
S1  The contracting Fibonacci numerator is an integral cyclotomic word:
      u_n = F_n phi - F_(n+1) = -psi^n
          = -F_(n+1) - F_n z^2 - F_n z^3.

S2  The two distinguished harmonic reads are
      H(1)  = log phi,
      H(-z) = -i pi/5,
      -5 H(-z) = i pi.

S3  Complete mu_10 real-axis classification:
      H(x) in R iff x in {1,-1}.

S4  Complete mu_10 imaginary-axis classification:
      Re H(x) = 0 iff x in {-z,-z^-1}.

S5  The same precursor A(x)=1-psi x lands on
      A(1)=phi, A(-1)=phi^-2
    and
      A(-z)=-z^2, A(-z^-1)=-z^3,
    with the torsion pair of exact order 10. The full unit-group statement is
    supplied by the written proof in PREREG, not by finite search.

S6  Principal-branch reconstruction:
      Log J = -H(1) - 2 H(-z)
            = -log phi + 2 pi i/5.
```

The complete finite classifications in S3 and S4 are exhaustive over all ten
members of `mu_10`. S1 is not a bounded Fibonacci experiment: its verifier
checks the universal coefficient recurrence identities used in the written
induction.

## What this result means

The narrow L1 result is that one integral contracting ladder has two uniquely
classified clean logarithmic axes under the full torsion weight class:

```text
free-unit real axis       x in {1,-1}
primitive-torsion phase   x in {-z,-z^-1}
```

The oriented representatives give `log phi` and `i pi` from the same harmonic
read, and those reads reconstruct `Log J` exactly.

## What this result does not mean

No layer lift occurred. This result does not derive two forces, does not promote
`AXIOM-PROJECTION-DICTIONARY [D]`, does not prove `TWO-PLACE-PHYSICS [D]`, and
does not identify the order-two sign in `mu_10` with the separate `zeta_8`
read place. It supplies no decoder, measure, observer, force, spacetime, SI
bridge, or new constant. `LOG-AXES-INDEPENDENCE [T]` and
`BOOST-COUNT-LADDER [D]` are unchanged.

## Reproducibility state

```text
pin:            61aa12c2b0e9705c3c0d9fb91fc4cfe6c80697ff
local lane:     x86_64 PASS
stdout sha256:  8198dc9c8c7dcc188d04635ec4c365e86dcb4524e28b347f2b2d1da1c943118d
stderr:         empty
GitHub x86_64:  pending
GitHub aarch64: pending
aggregate check: pending
Canon fold:     not started
```

The next allowed action is the one-probe pull request. The required GitHub jobs
must execute this same pinned verifier against the committed `EXPECTED.txt`.
