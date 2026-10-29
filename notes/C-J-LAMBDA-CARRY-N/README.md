# General reversible J multiplication on finite ramified digit carriers

2026-10-29. **NON-CANONICAL. L1 conditional construction.** Reservation #1818.

The preceding local construction gives multiplication by
`J=1+zeta_5^2` on `A_N=Z[zeta_5]/((1-zeta_5)^N)` for every positive
finite N, with explicit reversible cleanup and physical primitive
decompositions under supplied local and addressed pair control.

## What is preserved

The four mathematical/code inputs listed in `SOURCES.json` are byte-identical
to the locally frozen 2026-10-28 construction. That construction was already
executed locally. Its publication here does not turn those earlier runs into
a prospective public preregistration. Private run metadata and generated
historical output trees are not imported.

`THEOREMS.md` contains the all-N proofs. `compiler.py` is the original generic
row compiler. `verify_general.py` and `check_independent.py` implement the
two independent exact arithmetic representations. The new prospective probe
reruns both from these fixed bytes and compares their complete `facts`.

The complete reachable exact carry set has 1649 states for each of J and
J inverse, with 8245 edges each. This is a statement about the specified
carry representation. Minimality among all automata or physical circuits is
not claimed. The generic compiler has the upper bounds

```text
pair pulses per multiplication: 6249713 N
data plus work cells:           7N+16
including the N-cell archive:   8N+16
```

## Fresh arithmetic successor

The new work is in
[`P-J-LAMBDA-CARRY-ARITHMETIC-1`](../../probes/P-J-LAMBDA-CARRY-ARITHMETIC-1/PREREG.md).
It replaces large row lookups by four bounded integer coefficients and
small reversible base-five adders. Its proof, compiler, exact finite audit,
public pre-run pin and subsequent result record belong to that single probe.
The first prospective run must occur only after its source commit is pushed
and read back. The earlier table results are disclosed preparation.

For fresh replay, `verify_general.py` accepts `--certificate` and `--program`
with two new nonexisting output paths; it refuses to overwrite either file.
`check_independent.py` writes only its deterministic JSON to stdout.
The new public verifier handles these temporary outputs itself.

## Scope

The primitive source is Public Canon v106, especially
`C20-TEICHMULLER-SPLIT` and `QDD-AFFINE-CONTROL-REALIZATION`.
The larger bank of addressed five-level cells, clean initial work,
preparation, clock/program implementation, routing, energy account and
protection from gate errors remain separate admitted resources.

For the supplied flat preparation, the finite archive has uniform formal
word weights and the stated prime-five return formula. This does not supply
a law for one occurred outcome, choose J among units, implement the apparatus
under native U, or close `ENTROPY-MEASURABLE-OBSTRUCTION`.
No Canon, registry, frontier or public status is changed by this note.

Copyright 2026 A. M. Thorn. Apache-2.0, under the repository license.
