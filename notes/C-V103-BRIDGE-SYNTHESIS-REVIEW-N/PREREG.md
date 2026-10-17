# Review specification

PUBLIC / NON-CANONICAL / L1. A. M. Thorn. Apache-2.0.
Owner: `Claude-v103-RZ-20261017`; public claim #1572; target #1569 / PR #1571.

This file records the six fields of the check so that a reader can audit
what was tested and against which threshold. It is not a pre-execution pin:
the check script was written after the synthesis was read, and run before
this package was committed. Both facts are stated here and in `README.md`.

## 1. Equation and questions

Use the literal Public Canon v102 native generators `g0` to `g4`, selector
`T_t(x)=g_(z+2t)(x)` with `theta_n=popcount(n) mod 2`, the field marking
`A_f`, `B_f`, `L`, `V_inv`, `H`, the image criterion
`y in LZ^4 iff y0+2y1=y2+2y3=0 (mod 5)`, and the contact section
`eta(q,r)=(ell(q)/2,(ell(r)+1)/2,0,0)`, `Sz(y_i)-Sz(y_4)=z_i`.

Q1: Does every mathematical statement of `SYNTHESIS.md` sections 1 to 7,
and every row of `CLAIMS.tsv`, hold under exhaustive enumeration over
`F5^6`, polynomial-identity grids that determine a quadratic form, the unit
shell inside both derived bounding boxes, and finite orbit simulation of the
declared preparation families?

Q2: Are the nine RB exclusions and the eight D corrections in
`ACCEPTANCE.md` arithmetically correct, and do the central proofs of
sections 3.2 to 3.4 depend on none of the excluded statements?

Q3: Is the all-`n>=3` quantifier of section 3.4 stated no more strongly
than the single boundary-4 obstruction supports?

Q4: Does the package meet the repository's operational requirements:
notes-only diff, commit identity, byte identity of the five pinned
specification files, repository validators, public-safety scan, custody of
the synthesis source manifest, actual CI conclusions?

## 2. Code

```text
scientific_code: break_bridge_synthesis.py (audit witness, result-exposed)
execution: one run, one architecture, exact stdout committed
custody_code: custody_check.py
pre_execution_pin: NONE (script written after reading the synthesis)
two_architecture_claim: NONE
```

Python standard library only; `int` and `Fraction`; no float anywhere.
Run from the package directory with
`LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC python3 -I break_bridge_synthesis.py`.
No source verifier of lanes A to D or RA to RD was executed or imported.
Repository validators and the GitHub API were read as operational checks;
they create no scientific evidence.

## 3. Carrier and data

Native carrier `F5^6` with the origin-zero counter; field carriers `F5^4`,
`Z^4`, `LZ^4`. Admitted sources are exactly the rows of `SOURCES.tsv`: the
v102 authority files and tools at `a632c6a162dc87e60104d7a478e7650a6d5c4a1b`,
and the eleven synthesis files at `2a3250932553c1c36e88c48f0aa0d2f69f99f2b6`
together with their five specification blobs at
`c8485301e1d72e6e47159d8f66b3a1a12a920477`. The proofs of the eight source
lanes were not read; their blobs were only hashed for custody. Receipt
bodies (issue and comment text) were read as observational metadata.

## 4. Systematics

Definitions are taken from `canon/CANON.md`, not from the synthesis, and
compared. Degree-two polynomial identities are tested on `{0,1,2}^4`, which
determines a quadratic polynomial in four variables, so grid equality is a
proof. The unit shell is enumerated in `[-6,6]^4`, which contains both
bounding boxes derived from the two square-completion identities; the
derivation of each box is itself checked. Orbit claims are tested at finite
range (`2^16` steps for the zero orbit, `2^13` for each family member) and
reported as finite witnesses to the inherited inductions, not as proofs.
The complete-receiver noninterference theorem is not computed; its
premises are read and its quotient-history step is verified.

## 5. Failure threshold

Zero tolerance. Any `FAIL` line of the check script is a candidate
counterexample and is reported verbatim; no threshold is adjusted and no
failing item is reworded into a pass. A custody mismatch, a validator
failure, a public-safety hit or a false arithmetic step in `ACCEPTANCE.md`
is reported as a finding with its exact location.

## 6. Action layer

L1 throughout. No lift is proposed or implied. No Canon text, registry row,
gate row or status is created by this review.
