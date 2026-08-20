# Failure accounting

Status: **NON-CANONICAL METHOD NOTE**.

This note is a recommended checklist for recording a precise failure in
TWIST-J. It creates no claim, status, registry column, gate, layer, verifier
permission, or change to `POLICY.md`. The public Canon, registry, frontier,
and repository policy remain authoritative.

## 1. The standard

A speculative program should not be judged only by whether it becomes a final
theory. It should be judged by whether it converts broad intuitions into exact
commitments that can be derived, computed, reproduced, and broken.

A useful theory leaves more constraints than it inherited. It states not only
what it asserts, but what would kill the assertion, where the failure lives,
and what remains true after the failure.

The goal of failure accounting is not to protect the theory. It is to prevent
an indefinite rescue by changing the meaning, scope, layer, threshold, or
decoder after the result is known.

## 2. Recommended failure record

For an attack result, the compact record is

```text
F = (claim_id,
     scope,
     layer,
     frozen_threshold,
     minimal_witness,
     dependency_cut,
     surviving_claims)
```

The fields answer seven questions:

1. Which exact public claim, candidate clause, or preregistered proposition
   failed?
2. At which declared scope and action layer did it fail?
3. What threshold or equality was frozen before the result was opened?
4. What is the smallest known counterexample, contradiction, or experimental
   conflict?
5. Which named premises are actually needed to derive the failed statement?
6. Which neighboring claims remain untouched at their registered scopes?
7. Can the route be repaired only by adding a new premise, parameter, carrier,
   selector, normalization, or interpretive choice?

If a field is unresolved, record `STOP` rather than filling it by inference.
The repository status order and formal result vocabulary are not replaced by
this tuple.

## 3. Decoder and choice accounting

A short kernel is not automatically a simple theory. Complexity can move into
the decoder, projection, measure, scale, normalization, carrier, branch, or
physical dictionary.

For every repaired or successor route, record before execution:

- which choices were open;
- which choice was selected;
- which public condition selected it;
- whether the target data were already visible;
- whether a new dimensionless input entered;
- whether the repair crosses L1 through L6;
- which earlier falsifier still applies.

If several incompatible decoders satisfy the same frozen tests, that is a
nonuniqueness result. It is not evidence that the kernel explains all of them.

## 4. Elasticity warnings

A route has become scientifically elastic when any of the following occurs:

- an object's physical meaning changes after the result;
- a failed prediction is reassigned to another layer without a named gate;
- a threshold moves after execution;
- a numerical resemblance is promoted to a derivation;
- a correction factor is added without counting it as a new premise;
- the same data construct and confirm the mechanism;
- decoder nonuniqueness is presented as explanatory richness;
- a fired falsifier is removed, weakened, or silently renamed;
- a result outside the frozen carrier is used to rescue the frozen carrier.

The correct action is to preserve the failure, close or narrow its exact route,
and preregister a genuinely new candidate if one is justified.

## 5. What survives a failed theory

A precise failure can preserve substantial value:

- exact arithmetic theorems independent of the physical reading;
- minimal counterexamples and impossibility results;
- verified algorithms and finite classifications;
- explicit dependency cuts showing which results remain valid;
- hard open problems that make sense outside the original interpretation;
- a reproducible record of which rescue strategies do not work.

Global rejection is therefore rarely the most informative conclusion.
Localized failure with a minimal witness and a clean dependency cut is a
scientific asset.

The unacceptable outcome is not falsification. It is a route that cannot be
falsified because its terms keep changing.

## 6. Use in repository work

This checklist may be cited in a non-canonical note, preregistration, or result
record. Formal work must still follow `STATUS.md`, `POLICY.md`, `AGENTS.md`, and
the exact probe protocol. If this checklist conflicts with any authoritative
file, the authoritative file wins.
