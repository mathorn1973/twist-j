# P-TM-SYM2-FRAME-1 preregistration

Status: ACCEPTED FOR PIN, FORMAL GATE NOT RUN

This document freezes the complete decision surface for a self-contained
algebraic prerequisite of `TM-SYM2-MEASURE [H]`. It contains no gate output
and earns no scientific status. The formal gate must not run until this file
and the accepted verifier have been committed and pushed as the immutable
preregistration pin.

## Public identity

- Public lock: issue 92
- Owner: `TM-SYM2-FRAME recovery session`
- Branch: `probe/P-TM-SYM2-FRAME-1`
- Path: `probes/P-TM-SYM2-FRAME-1/`
- Initial base and Public Canon v11 activation commit:
  `3d8c6307f20d01ad50fc90ae1c5777926b884881`
- Canon content commit:
  `3dc0d4255ae47f0512e5dd656d92ceb308ab026a`
- Canon SHA-256:
  `d20b064c8564af4e4a22ec3d0a84a9847a3705af84fd6fee2faa6b2710d7c7e8`
- Action layer: L1 representation and frame algebra only

The theorem candidate tested here is named
`GOLDEN-SIX-LINE-SYM2-FRAME`. The historical name in the probe id records
the recovery arc. It does not identify the constructed frame with a
Thue-Morse state, stream, clock, Born reading, or physical measure.

## Falsification first

The old inference from a unique invariant metric or an isotropic second
moment to an isotropic fourth moment is invalid. The verifier carries a
negative control: the four cube body-diagonal lines have second moment
`I/3`, but their Sym2 frame operator is not SO(3)-central.

The positive candidate is killed at its exact frozen scope by any one of:

1. a golden line projector is not symmetric, rank one, idempotent, or
   trace one;
2. the six-line Gram values differ from diagonal `1`, off-diagonal `1/5`,
   or the projector sum differs from `2 I`;
3. the centered projectors do not form a rank-five regular simplex;
4. the exact `so(3)` commutant on `Sym2` has dimension other than two or is
   not spanned by the trace and traceless projectors;
5. the directly averaged frame operator fails rational descent, Galois
   agreement, or `so(3)` centrality;
6. its scalar and traceless coefficients differ from `1/3` and `2/15`,
   its trace differs from one, or their coefficient ratio differs from
   `5:2`;
7. the operator equals `(1/6) I6`, contrary to the predicted nonuniform
   six-channel result;
8. an independent exact counterexample is found on the same frozen frame.

No threshold may move after the pin.

## Equation

The rational carrier and exact rotation action are

```text
V_Q = Q^3,
W_Q = Sym2(V_Q),
rho(g) A = g A g^T                 for g in SO(3).
```

The verifier constructs the three standard integer generators of `so(3)`
and their derived action

```text
d rho(L) A = L A - A L.
```

Over characteristic zero, `SO(3)` is connected. An endomorphism commutes
with its `SO(3)` representation exactly when it commutes with the derived
`so(3)` representation. The exact rank over `Q` is unchanged after scalar
extension to `R`. Thus the complete rational Lie-algebra centralizer solve
audits the real `SO(3)` commutant.

Extend scalars only for the golden frame:

```text
K = Q(phi),                       phi^2 = phi + 1,
phi_bar = 1 - phi,                phi phi_bar = -1,
V_K = V_Q tensor_Q K,
W_K = W_Q tensor_Q K.
```

Freeze the following six representatives of projective lines in `V_K`:

```text
v1 = (0, 1,  phi)                 v2 = (0, 1, -phi)
v3 = (1,  phi, 0)                 v4 = (1, -phi, 0)
v5 = (phi, 0, 1)                  v6 = (phi, 0, -1)
r  = phi + 2
Pi = vi vi^T / r
```

Every `Pi` is a trace-one rank-one projector. The exact frame identities to
be derived, not assumed by the implementation, are

```text
Tr(Pi Pj) = 1       if i = j,
Tr(Pi Pj) = 1/5     if i != j,
sum_i Pi = 2 I3.
```

On `W_Q`, use the raw basis

```text
B = (E11, E22, E33, E12+E21, E13+E31, E23+E32)
G = diag(1, 1, 1, 2, 2, 2)
```

for the Frobenius form. Define the direct six-line frame operator

```text
M(A) = (1/6) sum_i Tr(Pi A) Pi.
```

The coefficient `1/6` in this equation is only the cardinal average over
the six frozen projective lines. It is not `GYRON-DENSITY`, a clock density,
or a physical Born factor.

Define the trace and traceless projectors

```text
P1(A) = Tr(A) I3 / 3,
P5(A) = A - P1(A).
```

The preregistered positive result is the exact operator identity

```text
M = (1/3) P1 + (2/15) P5,
Tr_W(M) = 1,
(1/3) : (2/15) = 5 : 2.
```

The ratio `5:2` is the ratio of the scalar and per-channel traceless
eigenvalues. The total trace masses of the rank-one and rank-five blocks
are `1/3` and `2/3`, hence `1:2`. These two ratios must not be conflated.

## Code

The accepted code is `verify.py` in this probe directory:

```text
SHA-256  4b84f8ddf35be025224ba5d3a44159ffecd5e93face5a0536971357928083135
bytes    12822
lines    415
```

It uses the Python standard library only, `Fraction` plus a minimal exact
`Q(phi)` pair field, deterministic ASCII stdout, and no files, network,
subprocesses, randomness, timestamps, floats, tolerances, or external
packages.

The verifier constructs the six projectors from the frozen vectors. It does
not construct `M` from the expected spectral formula. It must:

1. verify the field equation, both Galois roots, raw basis coordinates, and
   the full Frobenius Gram;
2. derive every projector rank, Gram, and tight-frame identity;
3. center the projectors and compute the full Gram rank five;
4. construct the integer `so(3)` generators, verify their brackets, verify
   the induced metric action, audit the canonical `P1,P5`, and solve the
   complete 36-variable commutant system, requiring rank 34 and nullity two;
5. build `M` by direct averaging on every basis element of `W_Q`;
6. require every coefficient of `M` to descend to `Q`, and require the
   Galois-conjugate frame to produce the identical operator;
7. compare the direct operator with `(1/3) P1 + (2/15) P5`, including
   centrality, coefficient ratio `5:2`, block-mass ratio `1:2`, trace, and
   the nonuniform result;
8. verify that the cube-line negative control has second moment `I/3` but
   fails the Sym2 centrality test.

The complete commutant solve is an implementation guard. Checking only that
the two preselected projectors commute would be circular.

## Carrier or data

There is no external dataset. The complete carrier is:

- `V_Q`, `W_Q`, their exact `SO(3)` and derived `so(3)` actions;
- the two exact embeddings of `K = Q(phi)` used for scalar extension;
- the six frozen projective lines and their six rank-one projectors;
- the six-dimensional raw symmetric-matrix basis and its Frobenius Gram;
- all 36 endomorphism variables in the exact commutant system;
- the four rational cube lines used only as a negative control.

The finite basis computation determines the stated linear operators on all
of `W_Q`, not only on the six frame projectors.

## Systematics frozen at the pin

- The six golden lines and equal cardinal weights are frozen inputs. Their
  selection is not derived from `J`, `U`, the checkpoint, the decoder, or a
  Thue-Morse orbit.
- No faithful three-dimensional `A5` action over `Q` is asserted. The probe
  uses exact `Q(phi)` frame coordinates and a separate rational `so(3)`
  commutant audit.
- `T-QENV-SYM2-SPLIT`, the historical `P-TM-SYM2-GATE0-1`, and all legacy
  stdout and pins are provenance only and are not premises.
- `GYRON-DENSITY [T]` is not a premise. The number `1/6` in the finite
  average is not identified with its physical density.
- A second-order tight frame does not suffice. The direct fourth-order
  frame operator and the cube negative control are both required.
- The Galois-conjugate golden frame must give the same rational operator.
- The coefficient ratio and the block trace-mass ratio are distinct and
  are checked and printed separately.
- No positivity statement is promoted to a physical measure statement.
- No L1 to L5 or L6 lift is asserted.
- No `A5` commutant dimension, Thue-Morse average, Born phase halving,
  gravity reading, or physical probability is inferred.

## Failure threshold, decision, and ceiling

The scientific failure threshold is exactly the eight numbered falsifiers
above. Audit failure is separate.

- `POSITIVE`: all eight exact gates pass. A later, separate review may
  consider `GOLDEN-SIX-LINE-SYM2-FRAME [T]` at the stated algebraic scope.
- `NEGATIVE`: the exact computation is internally valid but one or more
  frozen scientific falsifiers fire. This is a first-class result, exits
  zero, and must be preserved.
- `STOP`: a field, coordinate, projector, Lie-action, implementation,
  negative-control, stderr, hash, or reproducibility audit fails. This is an
  invalid run and exits nonzero.

Terminal stdout is one of:

```text
RESULT POSITIVE ...
RESULT NEGATIVE fired=...
RESULT STOP audit=...
```

Regardless of `POSITIVE`, the following remain unchanged:

```text
TM-SYM2-MEASURE [H]
QUADRATIC-ENVELOPE-DECODER [H]
QUADRATIC-DECODER-DATA [O]
```

The probe does not derive a TM-indexed carrier `v_n`, a TM-weighted average,
independence of a clock indicator from frame directions, a bridge from
`GYRON-DENSITY` to `P1`, or a rule multiplying the scalar channel by one
half. The arithmetic identity `1/6 = (1/2)(1/3)` is not a gate and earns no
physical conclusion.

## Formal execution, budget, and stop rule

- Formal local evidence: clean Linux aarch64 checkout of the immutable pin.
- Independent public check: clean GitHub x86_64 runner.
- Required result: identical verifier hash, exit code zero, empty stderr,
  and byte-identical stdout.
- Command:
  `python3 probes/P-TM-SYM2-FRAME-1/verify.py`
- Intended runtime: less than one second; hard public limit: 600 seconds.
- `EXPECTED.txt`, `RUN.md`, and `RESULT.md` are forbidden before the first
  formal post-pin execution.
- The pushed pin commit, `PREREG.md` SHA-256, and `verify.py` SHA-256 must be
  recorded before the first formal run and copied exactly into `RUN.md` and
  `RESULT.md` after execution.
- After the pin, the branch must not be rebased, squashed, amended, or
  force-pushed.
- A change to the equation, carrier, code predicate, systematics, action
  layer, threshold, or decision semantics invalidates the probe and requires
  a new issue, probe id, branch, path, and pin.
