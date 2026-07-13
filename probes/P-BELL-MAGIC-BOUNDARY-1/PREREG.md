# P-BELL-MAGIC-BOUNDARY-1 preregistration

Status: PRE-PIN DRAFT

This document defines the complete decision surface for the first public
attack on `BELL-MAGIC-BOUNDARY`. It contains no gate output and earns no
scientific status. The formal gate must not run until this document and the
accepted verifier have passed reciprocal source review, been committed, and
been pushed as the immutable preregistration pin.

## Public identity

- Claim: `BELL-MAGIC-BOUNDARY` [O]
- Public lock: issue 11
- Owner: master A session
- Branch: `probe/P-BELL-MAGIC-BOUNDARY-1`
- Path: `probes/P-BELL-MAGIC-BOUNDARY-1/`
- Initial base: `f4fb064c2a08cd21b9a2bc2bcfd4daf46da47bcb`
- Action layer: L3, quantum boundary

## Equation

For `n` equal to 5 or 8, let `zeta_n = exp(2 pi i/n)` and let the finite
phase-setting carrier be `Z/nZ`. Define the real equatorial correlation

```text
E_n(a,b) = Re(zeta_n^(a-b)).
```

For an ordered setting quadruple `(a0,a1,b0,b1)` in `(Z/nZ)^4`, define

```text
C_n(a0,a1,b0,b1)
  = E_n(a0,b0) + E_n(a0,b1)
    + E_n(a1,b0) - E_n(a1,b1),

S_n(a0,a1,b0,b1) = abs(C_n(a0,a1,b0,b1)).
```

The two observables are

```text
M_5 = max S_5 over (Z/5Z)^4,
M_8 = max S_8 over (Z/8Z)^4.
```

**Maximum convention freeze.** `M_n` is the maximum of the absolute functional
`S_n = abs(C_n)`, not the signed maximum of `C_n`. This matters at odd `n`,
where the signed spectrum need not be symmetric. The outer absolute value
makes a simultaneous overall sign reversal immaterial, but no other
correlation, state model, measurement family, interpolation, or continuous
optimization is part of the probe.

## Carrier and exact fields

The formal carrier contains all ordered tuples, including repeated settings:

```text
n = 5: 5^4 = 625 tuples,
n = 8: 8^4 = 4096 tuples.
```

The verifier represents `E_5` and every `S_5` exactly in `Q(sqrt(5))`, and
`E_8` and every `S_8` exactly in `Q(sqrt(2))`. Rational coefficients use
`fractions.Fraction`. Signs and comparisons use exact rational square
comparisons or certified rational enclosures of square roots. Floating-point
arithmetic, sampling, tolerances, numerical optimizers, and external packages
are forbidden.

The positive real embeddings of `sqrt(5)` and `sqrt(2)` are used. The two
phase tables must satisfy, exactly, conjugation symmetry, `E_n(0,0) = 1`,
the cosine recurrence, vanishing sum over a complete phase orbit, and the
bound `-1 <= E_n(a,b) <= 1`.

## Code and completeness certificates

The accepted code is `verify.py` in this probe directory. It must perform two
finite optimizations for each `n`:

1. full enumeration of all `n^4` ordered setting tuples;
2. the global-phase quotient with `a0 = 0`, containing `n^3` tuples.

Global-phase invariance of `S_n` follows directly from its dependence on phase
differences. The verifier certifies the quotient at maximizer level: the full
and reduced maxima must agree, every normalized full maximizer must be a
reduced maximizer, and every reduced maximizer must have exactly `n` full
lifts. It must print the exact maximum, the full and reduced maximizer counts,
and the complete ordered list of reduced maximizers.

The exhaustive computation is an exact finite proof at the declared scope.
The quotient computation is an internal completeness certificate, not a
replacement for full enumeration.

## Proposed comparison and scientific decision

The preregistered comparison is

```text
2 < M_5 < M_8.
```

The preregistered closed-form predictions for the frozen absolute convention
are

```text
M_5 = 1/2 + sqrt(5) = (1 + 2 sqrt(5))/2,
M_8 = 2 sqrt(2).
```

This is a falsifiable comparison internal to the stated finite functional.
The rational threshold `2` is used only in this exact finite comparison. It is
not promoted here as a physical local-hidden-variable interpretation. Neither
prediction is an assertion of an unrestricted Bell cap, a continuous quantum
optimum, or a Tsirelson value. The unrelated modulus bound
`max_k abs(1 + zeta_5^k) = phi` is outside this probe.

The exact maxima close the open obligation for this stated functional.
The scientific outcome is recorded as:

- `POSITIVE` if both maxima equal the preregistered closed forms and
  `2 < M_5 < M_8` holds;
- `NEGATIVE` if both maxima are computed exactly but either a predicted closed
  form or the preregistered comparison fails;
- `INVALID` if the functional is not total on either carrier or an exact
  maximum and its completeness certificates cannot be produced.

A scientifically negative result is a valid first-class outcome. The
verifier therefore exits zero when all exact audit checks pass, whether the
printed scientific decision is `POSITIVE` or `NEGATIVE`. It exits nonzero
only when the computation or an audit invariant fails. `RESULT.md` must
preserve that distinction.

## Systematics frozen at the pin

- Phase labels are residues `0, ..., n-1`; tuples are ordered.
- The correlation depends on `a-b`, not `a+b` and not a half-angle.
- The optimized value is `max abs(C_n)`, not `max C_n`.
- All four settings use the same `n`-phase carrier.
- Repeated settings and all degeneracies remain in the carrier.
- Maximizer multiplicities are counted before quotienting and after fixing
  `a0 = 0`.
- The global-phase quotient is the only symmetry reduction used for the
  completeness certificate.
- No physical uniqueness, cross-place lift, noise model, detector model, or
  continuum setting is inferred.
- The only cross-field comparison is the frozen inequality above.

## Failure thresholds and fired falsifiers

The probe is invalid if any of the following occurs:

1. a phase table identity or exact field invariant fails;
2. the enumerated carrier count differs from 625 or 4096;
3. full and quotient optimization disagree in value or multiplicity;
4. a maximum or comparison requires floating point, tolerance, or an
   unproved external value;
5. the verifier writes stderr, exits nonzero, or its formal output differs
   across the required architectures.

The scientific comparison fires negatively, without invalidating the exact
maxima, if either predicted closed form is false or if `2 < M_5 < M_8` is
false. Thresholds and semantics never move after the pin.

## Budget, run, and stop rule

- Python standard library only.
- Public CI budget: less than 15 minutes; intended verifier budget: less than
  10 seconds on a current general-purpose core.
- Formal local evidence: Linux or Linux-compatible `aarch64`, neutral public
  environment fields, exit code 0, empty stderr.
- Independent public check: GitHub `x86_64`, byte-identical stdout.
- `EXPECTED.txt`, `RUN.md`, and `RESULT.md` are forbidden before the formal
  post-pin execution.
- Any change after the pin to the equation, carrier, phase table, comparison,
  failure threshold, action layer, or verifier invalidates the run and
  requires a new probe name. The pinned branch must never be amended,
  rebased, squashed, or force-pushed.
